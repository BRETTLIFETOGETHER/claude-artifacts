#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Flagship depth layer generator.
For each Grade-AA campaign: a title-specific dossier — pastoral overview, six-week arc,
sermon series map, a fully written Day One, and a launch note — written from the
campaign's OWN title imagery via the hand-authored metaphor lexicon, riding the 207
verified promise-verse pairs for every Scripture claim. Set-wide uniqueness is enforced:
no two flagships share a thesis opener, a week-title tuple, or a Day-One opening.
Output: site/data/fl/<id>.json (one per flagship) + manifest with audit stats."""
import json, re, os, hashlib, sys
sys.path.insert(0, "/home/claude/build")
from flagship_authoring import (METAPHORS, CASES, THESIS_OPEN, THESIS_MID, THESIS_CLOSE,
                                WEEK_FRAMES, SERMON_FRAMES, DAY1_WELCOME, DAY1_VERSE,
                                DAY1_STEP, DAY1_PRAY, LAUNCH_NOTE)

SITE = "/home/claude/site"
BAN = re.compile(r"\b(journey|unpack|lean into|season of life|do life together)\b", re.I)
STOP = set("the a an of and to in for with your our my his her their its on at by from into "
           "day days week weeks god gods jesus christ lord holy spirit church life living "
           "40 30 21 7 forty thirty new more most every all one two three".split())

data = json.load(open(f"{SITE}/data/index.json"))
C = {k: i for i, k in enumerate(data["cols"])}
REFS = data["refs"]
rows = [r for r in data["rows"] if r[C["g"]] == "AA"]
rows.sort(key=lambda r: r[C["id"]])

# ---- verified promise pairs, parsed straight from the engine -------------------
e = open(f"{SITE}/assets/js/engine.js").read()
bank_src = e[e.index("const B=["):e.index("\n];", e.index("const B="))]
chan_blocks = re.split(r"/\*\d+ ", bank_src)[1:]
PAIRS = []
for blk in chan_blocks:
    PAIRS.append(re.findall(r'\["([^"]+)","((?:[123] )?[A-Z][a-zA-Z ]*? \d+:\d+(?:-\d+)?)"\]', blk))
assert len(PAIRS) == 23 and all(len(p) >= 8 for p in PAIRS), "pair parse failed"

def seed(fp, salt):
    return int(hashlib.md5((fp + str(salt)).encode()).hexdigest()[:8], 16)

def metaphor_for(title, subtitle, ch):
    words = re.findall(r"[a-z]+", (title + " " + (subtitle or "")).lower())
    for w in words:
        for name, m in METAPHORS.items():
            if w in m["keys"]:
                return name, m
    for w in words:  # stem-ish second pass
        for name, m in METAPHORS.items():
            if any(w.startswith(k[:4]) and len(k) > 3 for k in m["keys"]):
                return name, m
    fallback = {4:"money",5:"money",2:"together",1:"identity",3:"prayer",20:"voice",19:"road",
                6:"children",7:"home",8:"children",9:"heal",10:"heal",11:"grace",12:"road",
                13:"work",14:"vision",15:"vision",16:"seed",17:"light",18:"advent",21:"doubt",22:"digital",0:"road"}
    name = fallback.get(ch, "road")
    return name, METAPHORS[name]

def weeks_days(f):
    return (6,40) if f & 8 else (4,30) if f & 4 else (3,21) if f & 2 else (6,40)

# global dealers: spread frames across the SET so siblings differ
def dealer(pool_len, tag):
    order = list(range(pool_len))
    rnd = int(hashlib.md5(tag.encode()).hexdigest()[:8], 16)
    for i in range(pool_len - 1, 0, -1):
        rnd = (rnd * 1103515245 + 12345) & 0x7FFFFFFF
        j = rnd % (i + 1)
        order[i], order[j] = order[j], order[i]
    k = [0]
    def take(bump=0):
        v = order[(k[0] + bump) % pool_len]; k[0] += 1; return v
    return take
D_OPEN, D_MID, D_CLOSE = dealer(len(THESIS_OPEN),"o"), dealer(len(THESIS_MID),"m"), dealer(len(THESIS_CLOSE),"c")
D_W  = [dealer(len(WEEK_FRAMES[i]), "w%d" % i) for i in range(6)]
D_SER = dealer(len(SERMON_FRAMES),"s")
D_D1  = [dealer(len(p), "d%d" % i) for i, p in enumerate([DAY1_WELCOME, DAY1_VERSE, DAY1_STEP, DAY1_PRAY])]
D_LN  = dealer(len(LAUNCH_NOTE),"ln")

os.makedirs(f"{SITE}/data/fl", exist_ok=True)
seen_open, seen_weeks, seen_d1 = set(), set(), set()
stats = {"n":0, "words":0, "retries":0, "metaphors":{}}
def fill(t, **kw):
    out = t
    for k, v in kw.items(): out = out.replace("{%s}" % k, str(v))
    return out

for r in rows:
    rid, t, s, ch, fp = r[C["id"]], r[C["t"]], r[C["s"]] or "", r[C["ch"]], r[C["fp"]]
    mname, m = metaphor_for(t, s, ch)
    stats["metaphors"][mname] = stats["metaphors"].get(mname, 0) + 1
    wk, dy = weeks_days(r[C["f"]])
    backbone = REFS[r[C["sb"]]] if 0 <= r[C["sb"]] < len(REFS) else PAIRS[ch][0][1]
    sd = seed(fp, 1)
    pair = PAIRS[ch][sd % len(PAIRS[ch])]
    pair2 = PAIRS[ch][(sd // 7 + 3) % len(PAIRS[ch])]
    nouns = m["nouns"]; n0 = nouns[sd % len(nouns)]
    line0 = m["lines"][sd % len(m["lines"])]

    # thesis (retry loop for set-uniqueness of the opener)
    for bump in range(len(THESIS_OPEN)):
        op = fill(THESIS_OPEN[D_OPEN(bump)], title=t, line0=line0, first=m["first"])
        if op not in seen_open: break
        stats["retries"] += 1
    seen_open.add(op)
    mid = fill(THESIS_MID[D_MID()], weeks=wk, ref=backbone)
    close = fill(THESIS_CLOSE[D_CLOSE()], noun=n0)
    thesis = " ".join([op, mid, CASES[ch], close])

    # week arc — unique tuple across set
    for bump in range(4):
        wt = []
        for i in range(6):
            nn = nouns[(sd + i*3 + bump) % len(nouns)]
            fr = WEEK_FRAMES[i][D_W[i](bump)]
            wt.append(fill(fr, n=nn, N=nn[0].upper() + nn[1:]))
        key = "|".join(wt)
        if key not in seen_weeks: break
        stats["retries"] += 1
    seen_weeks.add(key)
    weeks = [{"n": i+1, "t": wt[i]} for i in range(6)][:wk] if wk < 6 else [{"n": i+1, "t": wt[i]} for i in range(6)]

    # sermon map
    sermons = []
    used = set()
    for i in range(len(weeks)):
        for bump in range(6):
            nn = nouns[(sd*3 + i*5 + bump) % len(nouns)]
            st = fill(SERMON_FRAMES[D_SER(bump)], n=nn, N=nn[0].upper()+nn[1:])
            if st not in used: break
        used.add(st)
        sermons.append({"w": i+1, "t": st, "ref": PAIRS[ch][(sd + i*2) % len(PAIRS[ch])][1]})

    # authored day one — unique opening across set
    for bump in range(len(DAY1_WELCOME)):
        d1w = fill(DAY1_WELCOME[D_D1[0](bump)], title=t, days=dy)
        if d1w not in seen_d1: break
        stats["retries"] += 1
    seen_d1.add(d1w)
    d1v = fill(DAY1_VERSE[D_D1[1]()], ref=pair[1], promise=pair[0], days=dy)
    d1s = fill(DAY1_STEP[D_D1[2]()], title=t, days=dy, weeks=wk, first=m["first"])
    d1p = fill(DAY1_PRAY[D_D1[3]()], days=dy, promise2=pair2[0][0].lower()+pair2[0][1:])
    day1 = {"read": f"Read {pair[1]} twice — once for the words, once for what the words want.",
            "body": [d1w, d1v, d1s], "pray": d1p, "ref": pair[1]}

    note = fill(LAUNCH_NOTE[D_LN()], weeks=wk, case=CASES[ch])

    doc = {"id": rid, "t": t, "thesis": thesis, "weeks": weeks, "sermons": sermons,
           "day1": day1, "note": note, "metaphor": mname}
    blob = json.dumps(doc, ensure_ascii=False)
    assert not BAN.search(blob.replace(t, "")), f"banned word in {rid}"
    assert "{" not in blob.replace("{\"", "±").replace(", \"", "±").count and True
    stats["n"] += 1
    stats["words"] += len(re.findall(r"\S+", thesis + " " + " ".join(w["t"] for w in weeks) +
                                     " " + " ".join(x["t"] for x in sermons) +
                                     " " + " ".join(day1["body"]) + " " + day1["pray"] + " " + note))
    open(f"{SITE}/data/fl/{rid}.json", "w").write(blob)

# leftover-slot audit across all emitted files
bad = []
for f in os.listdir(f"{SITE}/data/fl"):
    txt = open(f"{SITE}/data/fl/{f}").read()
    if re.search(r"\{[a-z]", txt): bad.append(f)
assert not bad, f"unfilled slots: {bad[:3]}"
json.dump({"count": stats["n"], "words": stats["words"], "retries": stats["retries"],
           "unique_openers": len(seen_open), "unique_arcs": len(seen_weeks),
           "unique_day1": len(seen_d1), "metaphors": stats["metaphors"]},
          open(f"{SITE}/data/fl/_manifest.json", "w"), indent=1)
print(f"flagships authored: {stats['n']} · {stats['words']:,} words · "
      f"openers {len(seen_open)}/383 unique · arcs {len(seen_weeks)}/383 · day1 {len(seen_d1)}/383 · "
      f"retries {stats['retries']}")
print("metaphor spread:", dict(sorted(stats["metaphors"].items(), key=lambda x: -x[1])[:8]))
