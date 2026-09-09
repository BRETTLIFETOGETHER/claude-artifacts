import re, json
from collections import Counter

F = "/mnt/user-data/uploads/Big_big_Top_5000_Preaching_Categories_2026-2030_so_much__1_.txt"
L = [l.strip() for l in open(F, encoding="utf-8-sig").read().replace("\r\n", "\n").split("\n")]
START = 18693                                   # everything before this was already ingested as source 12
seg = L[START:]

COLLECTION = re.compile(r"^COLLECTION \d+\s*[—–-]\s*(.+?)™?$")
DOMAIN_HDR = re.compile(r"^DOMAIN \d+$")
DOMAIN_DEF = re.compile(r"^Domain (\d+)\s*[—–-]\s*(.+)$")
CATEGORY = re.compile(r"^[★\s]*([A-Z0-9][A-Z0-9 ,&'’\-/]{5,})™?$")
NUMBERED = re.compile(r"^[★\s]*(\d{1,3})\.\s+(.+)$")
DESC = re.compile(r"^Description \+ Outcome:\s*(.+)$")
STAR = re.compile(r"^★")
SEPAR = re.compile(r"^_+$")

rows = []
collection = domain = category = ""
domains, collections = [], []
i = 0
while i < len(seg):
    l = seg[i]
    if not l or SEPAR.match(l):
        i += 1
        continue
    nxt = seg[i + 1] if i + 1 < len(seg) else ""

    m = COLLECTION.match(l)
    if m:
        collection = m.group(1).strip()
        collections.append(collection)
        i += 1
        continue
    m = DOMAIN_DEF.match(l)
    if m:
        domains.append((m.group(2).strip(), nxt if nxt and not NUMBERED.match(nxt) else ""))
        i += 1
        continue
    if DOMAIN_HDR.match(l):
        domain = seg[i + 1].strip().rstrip("™") if i + 1 < len(seg) else ""
        i += 2
        continue

    m = NUMBERED.match(l)
    if m:
        num, body = m.group(1), m.group(2).strip()
        star = bool(STAR.match(l))
        dm = DESC.match(nxt) if nxt else None
        if dm:                                                     # tool: title + description/outcome
            rows.append(dict(kind="tool", num=num, title=body, sub=dm.group(1).strip(),
                             domain=domain, category=category, collection=collection, star=star))
            i += 2
            continue
        if re.search(r"\s[—–]\s", body):                            # journey written on one line
            t, s = re.split(r"\s[—–]\s", body, 1)
            rows.append(dict(kind="journey", num=num, title=t.strip(), sub=s.strip(),
                             domain=domain, category=category, collection=collection, star=star))
            i += 1
            continue
        if nxt and not NUMBERED.match(nxt) and not SEPAR.match(nxt) and 3 <= len(nxt.split()) <= 24:
            rows.append(dict(kind="journey", num=num, title=body, sub=nxt.strip(),
                             domain=domain, category=category, collection=collection, star=star))
            i += 2
            continue
        rows.append(dict(kind="journey", num=num, title=body, sub="",
                         domain=domain, category=category, collection=collection, star=star))
        i += 1
        continue

    m = CATEGORY.match(l)
    if m and len(l.split()) <= 9 and not l.startswith("Description"):
        category = m.group(1).strip().title()
        i += 1
        continue
    i += 1

print("rows:", len(rows), "|", Counter(r["kind"] for r in rows))
print("with subtitle:", sum(1 for r in rows if r["sub"]), "| starred:", sum(1 for r in rows if r["star"]))
print("domains:", len(domains), "| collections:", len(collections))
print("distinct domains seen on rows:", len({r["domain"] for r in rows if r["domain"]}))
json.dump({"rows": rows, "domains": domains, "collections": collections},
          open("/home/claude/mtl/rows16.json", "w"))
for r in rows[:4] + [x for x in rows if x["kind"] == "tool"][:4] + rows[-4:]:
    print(f"  [{r['kind']:7s}] {r['num']:>4s} {r['title'][:44]:46s} | {r['sub'][:40]:42s} | {r['domain'][:22]} / {r['category'][:20]}")
