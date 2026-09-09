#!/usr/bin/env python3
"""
board_extract.py
================
Reconstruct board rosters across many nonprofits from IRS Form 990 / 990-PF data.

Solves the problem that manual research cannot: ~25 organizations x ~10 years of
filings x ~15 officers per filing = several thousand rows. This pulls them all,
then derives (a) who is current, (b) who departed and when, and (c) which people
sit on more than one board in your set.

DATA SOURCE
-----------
ProPublica Nonprofit Explorer API (free, public, no key required), which mirrors
the IRS e-file XML release. Filings are the authoritative record: Part VII of the
990 and Part VIII of the 990-PF list every officer, director, and trustee.

KNOWN LIMITS -- read these before trusting output
-------------------------------------------------
1. Organizations the IRS designates as churches or associations of churches file
   NOTHING. They will come back empty. That is a real finding, not a bug -- see
   CHURCH_STATUS_LIKELY below. For those, check the org's own website for a
   voluntary "public disclosure copy."
2. Only e-filed returns have XML. Paper filings before ~2018 may be image-only
   and will not parse. Coverage is strong 2018+, patchy before.
3. Filings lag 12-24 months. The most recent roster on file is not necessarily
   today's board. Always confirm current members against the org's own site.
4. Name matching for interlocks is fuzzy. "ROBERT H MACLELLAN" and
   "BOB MACLELLAN" will not match; "JOHN SMITH" at two orgs may be two people.
   Treat interlocks.csv as a lead list requiring human confirmation.
5. 990 Part VII mixes trustees with paid staff. Filter on the title column.

USAGE
-----
    pip install requests
    python board_extract.py                    # uses ORGS below
    python board_extract.py --orgs my.txt      # one org name (or EIN) per line
    python board_extract.py --out ./results

OUTPUT
------
    rosters_long.csv    one row per person per filing year
    roster_summary.csv  one row per person per org, with first/last year + status
    interlocks.csv      people appearing at 2+ organizations
    coverage.csv        what was found per org -- CHECK THIS FIRST
"""

import argparse
import csv
import json
import os
import re
import sys
import time
import urllib.parse
import xml.etree.ElementTree as ET
from collections import defaultdict

try:
    import requests
except ImportError:
    sys.exit("Missing dependency. Run:  pip install requests")

API = "https://projects.propublica.org/nonprofits/api/v2"
XML_URL = "https://projects.propublica.org/nonprofits/download-xml?object_id={}"
NS = {"irs": "http://www.irs.gov/efile"}
PAUSE = 0.6  # be polite to a free public API

# ---------------------------------------------------------------------------
# Target organizations.
#
# EINs below were verified during research. Anything without a verified EIN is
# resolved by name search -- ALWAYS check coverage.csv to confirm the matched
# entity is the one you meant. Common-name orgs match the wrong entity often.
# ---------------------------------------------------------------------------

VERIFIED_EINS = {
    "Maclellan Family Foundations": "626041468",
    "Givers Legacy Foundation": "593498416",   # see note below
    "Servant Foundation (The Signatry)": "431890105",
    "Biblica": "841194554",
}

# NOTE ON GIVERS LEGACY: EIN 59-3498416 is filed under BOTH names in different
# databases -- Charity Navigator's FY2024 record shows "Givers Legacy Foundation
# Inc." (giverslegacy.com, Clearwater FL) while Cause IQ and Instrumentl label
# the same EIN "Trustbridge Global Foundation USA Inc." This is almost certainly
# a rename, direction unconfirmed. Resolve before treating them as two entities.

ORGS = [
    # --- verified / already researched ---
    "Maclellan Family Foundations",
    "Givers Legacy Foundation",
    "Servant Foundation (The Signatry)",
    # --- Chattanooga cluster: expect trustee overlap with Maclellan ---
    "The Generosity Trust",
    # --- giving infrastructure ---
    "Barnabas Foundation",
    "WaterStone",
    "Christian Community Foundation of South Florida",
    "In His Steps Foundation",
    # --- large operating ministries ---
    "Prison Fellowship Ministries",
    "Awana Clubs International",
    "Samaritans Purse",
    "Compassion International",
    "Focus on the Family",
    "Christian Broadcasting Network",
    "CRISTA Ministries",
    "American Bible Society",
    "Museum of the Bible",
    "Educational Media Foundation",
    # --- publishing / media ---
    "David C Cook",
    "RightNow Media",
    "Living Stream Ministry",
    # --- outliers: different sector, will not interlock with the above ---
    "Lilly Endowment",
    "Thrivent Financial for Lutherans",
    "Stand Together Trust",
    "Lynda and Stewart Resnick Foundation",
]

# Orgs that plausibly claim church / association-of-churches status and may file
# nothing at all. Biblica is the proven case: ProPublica's record stops at FY2021
# with the note that the IRS designates it a church -- yet Biblica voluntarily
# posts 990s on its own site. Expect the same pattern here. Empty != nonexistent.
CHURCH_STATUS_LIKELY = {
    "Focus on the Family",
    "Christian Broadcasting Network",
    "Living Stream Ministry",
    "RightNow Media",
    "Samaritans Purse",
}

# Title strings that indicate governance rather than paid staff.
BOARD_TITLE_PAT = re.compile(
    r"\b(TRUSTEE|DIRECTOR|CHAIR|CHAIRMAN|CHAIRWOMAN|CHAIRPERSON|BOARD|"
    r"SECRETARY|TREASURER|PRESIDENT|VICE\s*CHAIR|GOVERNOR|OVERSEER|MEMBER)\b",
    re.I,
)
# Titles that look like governance but are really staff roles.
STAFF_OVERRIDE_PAT = re.compile(
    r"\b(DIRECTOR OF|SENIOR DIRECTOR|MANAGING DIRECTOR|EXECUTIVE DIRECTOR|"
    r"DEVELOPMENT DIRECTOR|STRATEGY DIRECTOR|PROGRAM DIRECTOR|ART DIRECTOR)\b",
    re.I,
)


def looks_like_board(title: str) -> bool:
    if not title:
        return False
    if STAFF_OVERRIDE_PAT.search(title):
        return False
    return bool(BOARD_TITLE_PAT.search(title))


def normalize_name(raw: str) -> str:
    """Aggressive normalization for cross-org matching. Deliberately lossy."""
    if not raw:
        return ""
    s = raw.upper()
    s = re.sub(r"\b(DR|MR|MRS|MS|REV|HON|PROF|SIR)\.?\b", " ", s)
    s = re.sub(r"\b(JR|SR|II|III|IV|PHD|MD|CPA|ESQ|CFP|JD)\.?\b", " ", s)
    s = re.sub(r"[^A-Z\s]", " ", s)
    parts = [p for p in s.split() if len(p) > 1]  # drop middle initials
    if len(parts) < 2:
        return " ".join(parts)
    return f"{parts[0]} {parts[-1]}"  # first + last only


def get_json(url, params=None, tries=3):
    for attempt in range(tries):
        try:
            r = requests.get(url, params=params, timeout=30,
                             headers={"User-Agent": "board-research/1.0"})
            if r.status_code == 200:
                return r.json()
            if r.status_code == 404:
                return None
        except Exception as e:
            if attempt == tries - 1:
                print(f"    ! request failed: {e}", file=sys.stderr)
        time.sleep(1.5 * (attempt + 1))
    return None


def resolve_ein(name: str):
    """Return (ein, matched_name, confidence). Confidence is advisory only."""
    if name in VERIFIED_EINS:
        return VERIFIED_EINS[name], name, "verified"
    digits = re.sub(r"\D", "", name)
    if len(digits) == 9:
        return digits, name, "supplied-ein"

    data = get_json(f"{API}/search.json", {"q": name})
    time.sleep(PAUSE)
    if not data or not data.get("organizations"):
        return None, None, "not-found"

    orgs = data["organizations"]
    target = normalize_name(name)
    for o in orgs:  # prefer an exact-ish name hit
        if normalize_name(o.get("name", "")) == target:
            return str(o["ein"]), o.get("name"), "name-exact"
    top = orgs[0]
    return str(top["ein"]), top.get("name"), "name-fuzzy-VERIFY"


def parse_people(xml_bytes):
    """Extract (person, title, hours, comp) from any 990 variant."""
    out = []
    try:
        root = ET.fromstring(xml_bytes)
    except ET.ParseError:
        return out

    # Group elements across 990, 990-EZ, and 990-PF schema variants.
    group_tags = [
        "Form990PartVIISectionAGrp",       # 990
        "OfficerDirectorTrusteeEmplGrp",   # 990-EZ
        "OfficerDirTrstKeyEmplInfoGrp",    # 990-PF
        "OfficerDirTrstKeyEmplGrp",        # 990-PF variant
        "CompensationHighestPaidEmplGrp",
    ]
    name_tags = ["PersonNm", "PersonNamePart1Txt", "BusinessNameLine1Txt",
                 "BusinessNameLine1", "NamePerson"]
    title_tags = ["TitleTxt", "Title"]
    hour_tags = ["AverageHoursPerWeekRt", "AvgHrsPerWkDevotedToPosRt",
                 "AverageHrsPerWkDevotedToPosRt"]
    comp_tags = ["ReportableCompFromOrgAmt", "CompensationAmt"]

    def first_text(node, tags):
        for t in tags:
            el = node.find(f".//irs:{t}", NS)
            if el is not None and el.text and el.text.strip():
                return el.text.strip()
            el = node.find(f".//{t}")  # namespace-less fallback
            if el is not None and el.text and el.text.strip():
                return el.text.strip()
        return ""

    for tag in group_tags:
        nodes = root.findall(f".//irs:{tag}", NS) or root.findall(f".//{tag}")
        for n in nodes:
            person = first_text(n, name_tags)
            if not person:
                continue
            out.append({
                "person": person,
                "title": first_text(n, title_tags),
                "hours": first_text(n, hour_tags),
                "comp": first_text(n, comp_tags),
            })
    return out


def fetch_org(name):
    ein, matched, conf = resolve_ein(name)
    result = {"org": name, "ein": ein or "", "matched_name": matched or "",
              "confidence": conf, "filings": 0, "rows": 0, "note": ""}
    rows = []

    if not ein:
        result["note"] = "no EIN found"
        if name in CHURCH_STATUS_LIKELY:
            result["note"] += " | church status likely -- check org website"
        return result, rows

    data = get_json(f"{API}/organizations/{ein}.json")
    time.sleep(PAUSE)
    if not data:
        result["note"] = "org lookup failed"
        return result, rows

    filings = data.get("filings_with_data", []) or []
    result["filings"] = len(filings)
    if not filings:
        result["note"] = "no machine-readable filings"
        if name in CHURCH_STATUS_LIKELY:
            result["note"] += " | church status likely -- check org website"
        return result, rows

    for f in filings:
        obj = f.get("object_id")
        year = f.get("tax_prd_yr") or (str(f.get("tax_prd", ""))[:4])
        if not obj:
            continue
        try:
            r = requests.get(XML_URL.format(obj), timeout=45,
                             headers={"User-Agent": "board-research/1.0"})
            time.sleep(PAUSE)
            if r.status_code != 200 or not r.content:
                continue
            for p in parse_people(r.content):
                rows.append({
                    "org": name, "ein": ein, "year": year,
                    "person": p["person"], "title": p["title"],
                    "hours": p["hours"], "comp": p["comp"],
                    "is_board": "Y" if looks_like_board(p["title"]) else "N",
                    "norm": normalize_name(p["person"]),
                })
        except Exception as e:
            print(f"    ! {name} {year}: {e}", file=sys.stderr)

    result["rows"] = len(rows)
    if conf == "name-fuzzy-VERIFY":
        result["note"] = "FUZZY MATCH -- confirm this is the right entity"
    return result, rows


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--orgs", help="file with one org name or EIN per line")
    ap.add_argument("--out", default="./results")
    ap.add_argument("--board-only", action="store_true",
                    help="restrict summary/interlocks to governance titles")
    args = ap.parse_args()

    targets = ORGS
    if args.orgs:
        with open(args.orgs) as fh:
            targets = [l.strip() for l in fh if l.strip()
                       and not l.startswith("#")]

    os.makedirs(args.out, exist_ok=True)
    all_rows, coverage = [], []

    for i, name in enumerate(targets, 1):
        print(f"[{i}/{len(targets)}] {name}")
        cov, rows = fetch_org(name)
        coverage.append(cov)
        all_rows.extend(rows)
        print(f"    ein={cov['ein'] or '-'}  filings={cov['filings']}  "
              f"rows={cov['rows']}  {cov['note']}")

    # --- rosters_long.csv ---
    long_path = os.path.join(args.out, "rosters_long.csv")
    cols = ["org", "ein", "year", "person", "title", "hours", "comp",
            "is_board", "norm"]
    with open(long_path, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=cols)
        w.writeheader()
        w.writerows(all_rows)

    # --- roster_summary.csv: first/last year seen, current vs departed ---
    scope = [r for r in all_rows if r["is_board"] == "Y"] if args.board_only \
        else all_rows
    latest_year = defaultdict(int)
    for r in scope:
        try:
            latest_year[r["org"]] = max(latest_year[r["org"]], int(r["year"]))
        except (ValueError, TypeError):
            pass

    agg = defaultdict(lambda: {"years": [], "titles": set()})
    for r in scope:
        k = (r["org"], r["norm"], r["person"])
        try:
            agg[k]["years"].append(int(r["year"]))
        except (ValueError, TypeError):
            pass
        if r["title"]:
            agg[k]["titles"].add(r["title"])

    sum_path = os.path.join(args.out, "roster_summary.csv")
    with open(sum_path, "w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(["org", "person", "norm", "first_year", "last_year",
                    "years_served", "status", "titles_held"])
        for (org, norm, person), d in sorted(agg.items()):
            if not d["years"]:
                continue
            lo, hi = min(d["years"]), max(d["years"])
            status = "current" if hi >= latest_year.get(org, 0) else "DEPARTED"
            w.writerow([org, person, norm, lo, hi, len(set(d["years"])),
                        status, " | ".join(sorted(d["titles"]))])

    # --- interlocks.csv: same normalized name at 2+ organizations ---
    by_person = defaultdict(set)
    for r in scope:
        if r["norm"]:
            by_person[r["norm"]].add(r["org"])
    inter_path = os.path.join(args.out, "interlocks.csv")
    with open(inter_path, "w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(["normalized_name", "org_count", "organizations"])
        for norm, orgs in sorted(by_person.items(),
                                 key=lambda kv: -len(kv[1])):
            if len(orgs) > 1:
                w.writerow([norm, len(orgs), " | ".join(sorted(orgs))])

    # --- coverage.csv ---
    cov_path = os.path.join(args.out, "coverage.csv")
    with open(cov_path, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=["org", "ein", "matched_name",
                                           "confidence", "filings", "rows",
                                           "note"])
        w.writeheader()
        w.writerows(coverage)

    print(f"\nWrote {len(all_rows)} rows across {len(targets)} organizations.")
    print(f"  {cov_path}   <- READ THIS FIRST")
    print(f"  {long_path}")
    print(f"  {sum_path}")
    print(f"  {inter_path}")
    print("\nReminder: filings lag 12-24 months. Confirm 'current' members "
          "against each organization's own board page before relying on them.")


if __name__ == "__main__":
    main()
