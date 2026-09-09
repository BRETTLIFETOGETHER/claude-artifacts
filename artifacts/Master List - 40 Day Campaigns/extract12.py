import re, json
from collections import Counter

F = "/mnt/user-data/uploads/Big_big_Top_5000_Preaching_Categories_2026-2030_so_much.txt"
L = [l.strip() for l in open(F, encoding="utf-8-sig").read().replace("\r\n", "\n").replace("\r", "\n").split("\n")]

SMALL = {"a", "an", "the", "and", "or", "of", "in", "on", "for", "to", "with", "at", "by", "from", "as", "is", "it",
         "your", "you", "&", "but", "not", "that", "this", "when", "who", "what", "why", "how"}
NUMONLY = re.compile(r"^\d{1,3}$")
NUMTITLE = re.compile(r"^(\d{1,3})[.)]\s+(.+)$")
BULLET = re.compile(r"^\*\s+(.+)$")
TAGSUF = re.compile(r"(NEW|RISING|HOT|TOTAL|SOON)$")


def words(l):
    return [w for w in re.sub(r"[^\w&'\- ]", " ", l).split() if w]


def titlecase(l):
    w = words(l)
    if not (1 <= len(w) <= 12):
        return False
    sig = [x for x in w if x.lower() not in SMALL]
    if not sig:
        return len(w) <= 3 and w[0][:1].isupper()
    caps = sum(1 for x in sig if x[:1].isupper() or x[:1].isdigit())
    return caps / len(sig) >= 0.75 and not l.endswith((".", ":", ";"))


def sentencecase(l):
    w = words(l)
    if not (2 <= len(w) <= 20):
        return False
    if not w[0][:1].isupper():
        return False
    sig = [x for x in w[1:] if x.lower() not in SMALL and len(x) > 2]
    if not sig:
        return False
    lower = sum(1 for x in sig if x[:1].islower())
    return lower / len(sig) >= 0.6


def prose(l):
    return len(l.split()) >= 16 or (l.endswith(".") and len(l.split()) >= 9)


rows, cat, i = [], "", 0
while i < len(L):
    l = L[i]
    if not l or set(l) == {"_"}:
        i += 1
        continue
    nxt = L[i + 1] if i + 1 < len(L) else ""
    nxt2 = L[i + 2] if i + 2 < len(L) else ""

    if NUMONLY.match(l) and nxt and titlecase(nxt) and not prose(nxt):
        if nxt2 and sentencecase(nxt2) and not prose(nxt2) and len(nxt2.split()) <= 14:
            rows.append((i + 1, TAGSUF.sub("", nxt).strip(), nxt2, cat, "card"))
            i += 3
            continue
        cat = TAGSUF.sub("", nxt).strip()
        i += 2
        continue

    m = NUMTITLE.match(l)
    if m:
        body = m.group(2).strip()
        if titlecase(nxt) and not sentencecase(nxt):
            cat = body
            i += 1
            continue
        if sentencecase(nxt) and not prose(nxt):
            rows.append((i, body, nxt, cat, "num"))
            i += 2
            continue
        if titlecase(body):
            rows.append((i, body, "", cat, "num"))
        i += 1
        continue

    m = BULLET.match(l)
    if m:
        b = m.group(1).strip()
        if titlecase(b) and len(words(b)) >= 2:
            rows.append((i, b, "", cat, "bullet"))
        i += 1
        continue

    if titlecase(l) and not prose(l):
        if sentencecase(nxt) and not prose(nxt) and len(nxt.split()) <= 14:
            rows.append((i, l, nxt, cat, "pair"))
            i += 2
            continue
        if titlecase(nxt) or not nxt:
            rows.append((i, l, "", cat, "solo"))
            i += 1
            continue
    i += 1

print("rows:", len(rows), "| with subtitle:", sum(1 for r in rows if r[2]))
print(Counter(r[4] for r in rows))
print("categories seen:", len({r[3] for r in rows}))
for r in rows[:12] + rows[900:912] + rows[3000:3012] + rows[-12:]:
    print(f"{r[0]:6d} [{r[4]:6s}] {r[1][:46]:48s} | {r[2][:40]:42s} | {r[3][:26]}")
json.dump(rows, open("/home/claude/mtl/rows12.json", "w"))
