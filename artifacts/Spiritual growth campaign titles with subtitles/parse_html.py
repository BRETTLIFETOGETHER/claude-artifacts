import json
from bs4 import BeautifulSoup

# Map each HTML file to a canonical Collection name.
FILES = {
    "top-100-flagship-campaigns.html":      "Top 100 Flagship",
    "flagship-campaigns-expansion.html":    "Top 100 Flagship",
    "flagship-campaigns-200-more.html":     "Top 100 Flagship",
    "preaching-forecast-titles.html":       "Preaching Forecast",
    "capital-campaign-100.html":            "Capital Campaign",
    "discipleship-500.html":                "Discipleship",
}
BASE = "/mnt/user-data/outputs/"

def section_label(li):
    """Walk backwards to find the nearest category/band header for this <li>."""
    # nearest ancestor <section class=cat> or preceding .cat-title / .band h2
    cur = li
    # First, look for an enclosing section.cat with a .cat-title
    sec = li.find_parent("section", class_="cat")
    if sec:
        ct = sec.find(class_="cat-title")
        if ct:
            return ct.get_text(" ", strip=True)
    # Otherwise, find the nearest preceding .band h2 or .cat-title in document order
    for el in li.find_all_previous(["h2"]):
        cls = el.get("class") or []
        if "cat-title" in cls:
            return el.get_text(" ", strip=True)
        # band h2 lives inside div.band
        parent = el.find_parent("div", class_="band")
        if parent is not None and el is parent.find("h2"):
            return el.get_text(" ", strip=True)
    return ""

def parse_file(fname):
    with open(BASE + fname, encoding="utf-8") as f:
        soup = BeautifulSoup(f.read(), "html.parser")
    rows = []
    for li in soup.select("ol.titles li"):
        name_el = li.find(class_="t-name")
        sub_el = li.find(class_="t-sub")
        if not name_el:
            continue
        title = name_el.get_text(" ", strip=True)
        sub = sub_el.get_text(" ", strip=True) if sub_el else ""
        cat = section_label(li)
        rows.append({"category": cat, "title": title, "subtitle": sub})
    return rows

all_rows = []
counts = {}
for fname, coll in FILES.items():
    rows = parse_file(fname)
    for r in rows:
        r["collection"] = coll
        r["source"] = fname
    all_rows.extend(rows)
    counts[fname] = len(rows)

for f, c in counts.items():
    print(f"{c:>4}  {f}")
print("TOTAL parsed:", len(all_rows))

# quick sanity: show a couple sample rows per file
with open("/home/claude/html_rows.json", "w", encoding="utf-8") as f:
    json.dump(all_rows, f, ensure_ascii=False)

# show 2 samples from discipleship + forecast to check category capture
for coll in ["Discipleship","Preaching Forecast","Top 100 Flagship","Capital Campaign"]:
    ex = [r for r in all_rows if r["collection"]==coll][:2]
    for r in ex:
        print(f"  [{coll}] cat='{r['category']}' | {r['title']} — {r['subtitle']}")
