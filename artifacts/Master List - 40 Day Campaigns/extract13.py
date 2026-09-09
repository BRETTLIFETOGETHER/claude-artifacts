import re, os, json, html as htmlmod
from collections import Counter

D = "/home/claude/ltlib/LifeTogether-Library"


def clean(s):
    s = re.sub(r"<[^>]+>", "", s)
    s = htmlmod.unescape(s)
    return re.sub(r"\s+", " ", s).strip()


# ---------- INDEX artifacts ----------
idx = open(os.path.join(D, "INDEX.html"), encoding="utf-8", errors="replace").read()
m = re.search(r"var A=(\[.*?\]);", idx, re.S)
ARTIFACTS = json.loads(m.group(1)) if m else []
print("index artifacts:", len(ARTIFACTS))

# ---------- structured cards ----------
CARD_PATTERNS = [
    # life-of-christ-sessions: <span class='sn'>0001</span><h4 class='st'>Title</h4><p class='ss'>Sub</p>
    re.compile(r"class='sn'>([^<]*)</span>\s*<h4 class='st'>(.*?)</h4>\s*<p class='ss'>(.*?)</p>", re.S),
    # lifetogether-life-of-christ / red-letter: scn / sct / scs
    re.compile(r"class='scn'>([^<]*)</span>\s*<h4 class='sct'>(.*?)</h4>\s*<p class='scs'>(.*?)</p>", re.S),
]
SERMON = re.compile(r"class='sc-r'>([^<]*)</span><span class='sc-t'>(.*?)</span></div>\s*"
                    r"<span class='sc-v'>(.*?)</span>\s*<p class='sc-hk'>(.*?)</p>", re.S)
CATNAME = re.compile(r"<h3 class='(?:cnm|catnm|catn)'[^>]*>(.*?)</h3>", re.S)
CAT_ANY = re.compile(r"<h3[^>]*>(.*?)</h3>", re.S)
SECTION = re.compile(r"<h2[^>]*>(.*?)</h2>", re.S)


def cards_for(fname, h):
    out = []
    # index positions of category and section headings so each card can inherit them
    cats = [(m.start(), clean(m.group(1))) for m in CAT_ANY.finditer(h)]
    secs = [(m.start(), clean(m.group(1))) for m in SECTION.finditer(h)]

    def ctx(pos, arr):
        cur = ""
        for p, v in arr:
            if p <= pos:
                cur = v
            else:
                break
        return cur

    for pat in CARD_PATTERNS:
        for m in pat.finditer(h):
            num, t, sub = clean(m.group(1)), clean(m.group(2)), clean(m.group(3))
            if t:
                out.append(dict(num=num, title=t, sub=sub, cat=ctx(m.start(), cats),
                                sec=ctx(m.start(), secs), kind="series", file=fname))
    for m in SERMON.finditer(h):
        rank, t, verse, hook = clean(m.group(1)), clean(m.group(2)), clean(m.group(3)), clean(m.group(4))
        if t:
            out.append(dict(num=rank, title=t, sub=hook, cat=ctx(m.start(), cats),
                            sec=ctx(m.start(), secs), kind="sermon", file=fname, verse=verse))
    return out


all_cards, per_file = [], Counter()
for f in sorted(os.listdir(D)):
    if not f.endswith(".html"):
        continue
    h = open(os.path.join(D, f), encoding="utf-8", errors="replace").read()
    c = cards_for(f, h)
    if c:
        per_file[f] = len(c)
        all_cards += c

print("cards:", len(all_cards))
for f, n in per_file.most_common():
    print(f"   {f[:40]:42s} {n}")
print("unique titles:", len({c['title'].lower() for c in all_cards}))
json.dump({"artifacts": ARTIFACTS, "cards": all_cards}, open("/home/claude/mtl/rows13.json", "w"))
for c in all_cards[:6] + all_cards[3000:3006] + all_cards[-6:]:
    print(f"  [{c['kind']:6s}] {c['num'][:5]:6s} {c['title'][:44]:46s} | {c['sub'][:38]:40s} | {c['cat'][:24]} | {c['file'][:24]}")
