import os, re, glob

OUT = "/mnt/user-data/outputs"

NAV = """<nav class="main">
      <div class="navitem"><span class="navlink">Begin</span><div class="mega"><h5>Start Here</h5>
        <a href="index.html">The Archive</a><a href="deep-well-brochure-navy.html">Find Your Starting Point</a><a href="deep-well-platform.html">Platform Overview</a></div></div>
      <div class="navitem"><span class="navlink">Manuscripts</span><div class="mega"><h5>Written Work</h5>
        <a href="The_Deep_Well_Family_Edition_Outline.html">The Deep Well · Outline</a><a href="Deep_Well_Ch1_Ch5_Ch6.html">Chapters One, Five &amp; Six</a><a href="Deep_Well_Ch3_Amos.html">Chapter Three · Amos</a><a href="Deep_Well_Ch4_and_40_Day_Outline.html">Chapter Four &amp; Forty Days</a><a href="Two_Books_Instead_of_One_draft.html">Two Books Instead of One</a></div></div>
      <div class="navitem"><span class="navlink">Advisor</span><div class="mega"><h5>Practitioner Edition</h5>
        <a href="Different_Kind_of_Advisor_Three_Editions.html">Three Editions</a><a href="Advisor_Book_Ch7_The_Conversation_That_Costs_You.html">The Conversation That Costs You</a><a href="case-studies-and-voices.html">Case Studies &amp; Voices</a></div></div>
      <div class="navitem"><span class="navlink">Instruments</span><div class="mega"><h5>Diagnostics &amp; Tools</h5>
        <a href="Deep_Well_Assessments_and_Tools.html">The Assessments</a><a href="Deep_Well_Toolbox_Expanded.html">The Toolbox</a><a href="family-library-interactive.html">Take the Assessment</a><a href="family-library.html">The Family Library</a></div></div>
      <div class="navitem"><span class="navlink">Operations</span><div class="mega"><h5>Build &amp; Partners</h5>
        <a href="Treasure_Principle_40_Day_Campaign_Proposal.html">Treasure Principle Proposal</a><a href="video-access-golive.html">Video, Access &amp; Go-Live</a><a href="deep-well-blue.html">Blue Prototype</a></div></div>
    </nav>"""

# navy pages get the shared nav; blue page keeps its own step system
NAVY = ["index.html","deep-well-platform.html","family-library.html",
        "family-library-interactive.html","case-studies-and-voices.html",
        "video-access-golive.html","deep-well-brochure-navy.html"]

for f in NAVY:
    p = os.path.join(OUT, f)
    s = open(p, encoding="utf-8").read()
    # replace the existing <nav class="main">...</nav> block with the shared one
    new, n = re.subn(r'<nav class="main">.*?</nav>', NAV, s, count=1, flags=re.S)
    if n == 0:
        print("NO NAV FOUND:", f)
        continue
    # brand always returns to the archive
    new = new.replace('<a class="brand" href="#top">', '<a class="brand" href="index.html">')
    open(p, "w", encoding="utf-8").write(new)
    print("nav wired:", f)

# ---- verify every internal href resolves ----
files = sorted(glob.glob(os.path.join(OUT, "*.html")))
existing = set(os.path.basename(x) for x in files)
bad = []
total = 0
for p in files:
    s = open(p, encoding="utf-8").read()
    for m in re.findall(r'href="([^"]+)"', s):
        if m.startswith(("http", "#", "mailto:")):
            continue
        if "' +" in m or "'+" in m:
            continue
        target = m.split("#")[0]
        if not target:
            continue
        total += 1
        if target not in existing:
            bad.append((os.path.basename(p), target))

print("\nchecked", total, "internal links across", len(files), "pages")
if bad:
    print("BROKEN:")
    for b in bad: print("  ", b[0], "->", b[1])
else:
    print("all internal links resolve")

# check JS-built catalog hrefs point at real files
import json
for p in files:
    s = open(p, encoding="utf-8").read()
    for m in re.findall(r'href:"([^"]+)"', s):
        if m not in existing:
            print("BROKEN CATALOG HREF in", os.path.basename(p), "->", m)
print("catalog hrefs verified")
print("\nfiles in site:", len(existing))
