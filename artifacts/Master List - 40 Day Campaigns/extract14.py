import re, json, html as htmlmod
from collections import Counter

F = "/mnt/user-data/uploads/flourishing_lifetogether_brochure.html"
h = open(F, encoding="utf-8", errors="replace").read()


def clean(s):
    s = re.sub(r"<[^>]+>", " ", s)
    return re.sub(r"\s+", " ", htmlmod.unescape(s)).strip()


# ---- section context: dimension / library headers
SECTIONS = []
for m in re.finditer(r'<section class="lib-header"[^>]*>\s*<p class="lib-eyebrow">(.*?)</p>\s*<h3>(.*?)</h3>\s*'
                     r'(?:<p class="lib-tagline">(.*?)</p>)?', h, re.S):
    SECTIONS.append((m.start(), clean(m.group(1)), clean(m.group(2)), clean(m.group(3) or "")))
DIMS = []
for m in re.finditer(r'<h2[^>]*>(.*?)</h2>', h, re.S):
    t = clean(m.group(1))
    if t:
        DIMS.append((m.start(), t))


def ctx(pos, arr, idx):
    cur = ""
    for item in arr:
        if item[0] <= pos:
            cur = item[idx]
        else:
            break
    return cur


rows = []

# ---- campaign cards (title + subtitle + optional devotional day list)
for m in re.finditer(r'<div class="campaign-card">(.*?)(?=<div class="campaign-card">|<section|</section>)', h, re.S):
    blk = m.group(1)
    t = re.search(r'<div class="campaign-title">(.*?)</div>', blk, re.S)
    s = re.search(r'<div class="campaign-sub">(.*?)</div>', blk, re.S)
    if not t:
        continue
    title = clean(re.sub(r'<span class="top-pick-badge">.*?</span>', "", t.group(1), flags=re.S))
    top = "top-pick-badge" in t.group(1)
    sub = clean(s.group(1)) if s else ""
    sec = ctx(m.start(), SECTIONS, 2)
    dim = ctx(m.start(), DIMS, 1)
    rows.append(dict(kind="campaign", num="", title=title, sub=sub, sec=sec, dim=dim, top=top))
    for d in re.finditer(r'<li><span class="sn">(\d+)</span>(.*?)</li>', blk, re.S):
        rows.append(dict(kind="day", num=d.group(1), title=clean(d.group(2)), sub="", sec=sec, dim=dim,
                         parent=title, top=False))

# ---- directory series (dnum / dtitle / dsub)
for m in re.finditer(r'<span class="dnum">(.*?)</span>\s*<span class="dtitle">(.*?)</span>\s*'
                     r'<span class="dsub">(.*?)</span>', h, re.S):
    rows.append(dict(kind="series", num=clean(m.group(1)), title=clean(m.group(2)), sub=clean(m.group(3)),
                     sec=ctx(m.start(), SECTIONS, 2), dim=ctx(m.start(), DIMS, 1), top=False))

# ---- the nineteen dimensions and the assessment areas
dimlist = []
for m in re.finditer(r"(\w+):\s*\{name:\s*'(.*?)',\s*qs:\s*\[[^\]]*\],\s*campaigns:\s*\[(.*?)\]\}", h, re.S):
    camps = [clean(x) for x in re.findall(r"'(.*?)'", m.group(3))]
    dimlist.append((m.group(2), camps))

print("sections:", len(SECTIONS), "| dims(h2):", len(DIMS), "| assessment areas:", len(dimlist))
print(Counter(r["kind"] for r in rows))
print("unique titles:", len({r["title"].lower() for r in rows if r["kind"] != "day"}))
print("\nsection headers:")
for _, eyebrow, name, tag in SECTIONS[:8]:
    print(f"   {eyebrow[:22]:24s} {name[:34]:36s} {tag[:46]}")
print("\nsamples:")
for r in rows[:5] + [x for x in rows if x["kind"] == "series"][:5] + [x for x in rows if x["kind"] == "day"][:4]:
    print(f"  [{r['kind']:8s}] {r.get('num',''):4s} {r['title'][:40]:42s} | {r['sub'][:36]:38s} | {r['sec'][:26]}")
json.dump({"rows": rows, "dims": dimlist,
           "sections": [(e, n, t) for _, e, n, t in SECTIONS]}, open("/home/claude/mtl/rows14.json", "w"))
