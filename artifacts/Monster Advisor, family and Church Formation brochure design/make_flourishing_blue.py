import json

with open("/home/claude/build/flourishing_parsed.json") as f:
    DIMS = json.load(f)

PAGES = []
def add(html): PAGES.append(html)

def folio(chapter, num):
    return f'''<div class="folio"><div class="thread">{chapter}</div><div>{num:02d}</div></div>'''

# =================================================================
# PAGE 1 — COVER
# =================================================================
add(f'''
<div class="page blue">
  <div class="frame" style="display:flex; flex-direction:column; justify-content:flex-end;">
    <div style="font-family:'Archivo'; font-weight:600; font-size:9pt; letter-spacing:0.22em; color:#8FB8DC; margin-bottom:2.2in;">A WHOLE-LIFE DISCIPLESHIP FRAMEWORK</div>
    <h1 class="display" style="font-size:32pt; color:#F7FAFC;">Flourishing LifeTogether&trade;</h1>
    <div style="height:0.14in;"></div>
    <div style="font-family:'Playfair'; font-style:italic; font-weight:600; font-size:14.5pt; color:#8FB8DC;">Seventeen dimensions of a whole, healthy, purposeful, and fruitful life</div>
    <div style="height:0.26in;"></div>
    <p class="lede" style="font-size:10.5pt; color:rgba(247,250,252,0.8); max-width:5.6in;">
      Eighty-five flagship campaigns, one hundred seventy curriculum pathways, five hundred
      ten sessions ready to script &mdash; organized around the whole of a person&rsquo;s life, not
      just the hour they spend in church.
    </p>
    <div style="height:0.5in;"></div>
    <div style="font-family:'Archivo'; font-weight:500; font-size:8pt; letter-spacing:0.1em; color:rgba(247,250,252,0.55);">LIFETOGETHER.COM</div>
  </div>
</div>
''')

# =================================================================
# PAGE 2 — THE BIG IDEA + TABLE OF CONTENTS (Integrated Architecture)
# =================================================================
groups = [
    ("PERSONAL FLOURISHING", ["Joy","Health","Purpose","Character","Resilience","Growth"]),
    ("RELATIONAL FLOURISHING", ["Relationships","Family","Community"]),
    ("SPIRITUAL FLOURISHING", ["Faith","Generosity","Legacy"]),
    ("VOCATIONAL & ECONOMIC FLOURISHING", ["Work","Business","Marketplace","Finances","Leadership"]),
]
name_to_dim = {d["name"]: d for d in DIMS}
toc_html = ""
for label, names in groups:
    items = "".join([f'<div class="toc-item"><span>{name_to_dim[n]["numeral"]}. Flourishing {n}</span><span class="n">P.{3 + i}</span></div>' for i, n in enumerate(names)])
    # page numbers approximate; real numbers not critical for a TOC in a brochure of this style, so keep simple text listing instead
    items = "".join([f'<div class="toc-item"><span>{name_to_dim[n]["numeral"]}. Flourishing {n}</span></div>' for n in names])
    toc_html += f'<div class="toc-group"><div class="toc-group-label">{label}</div>{items}</div>'

add(f'''
<div class="page">
  <div class="frame">
    <div class="eyebrow">THE BIG IDEA</div>
    <div style="height:0.2in;"></div>
    <h1 class="display" style="font-size:20pt; color:var(--blue);">A person doesn&rsquo;t flourish in one dimension at a time.</h1>
    <div style="height:0.14in;"></div>
    <p class="lede" style="font-size:10pt;">
      Most discipleship content picks a lane &mdash; spiritual growth, or marriage, or work, or
      money &mdash; and treats the rest of a person&rsquo;s life as someone else&rsquo;s subject.
      Flourishing LifeTogether does the opposite: seventeen dimensions, each built to the
      same depth, organized into four integrated groups so a church can address the whole
      of a person&rsquo;s life without seventeen disconnected ministries.
    </p>
    <div style="height:0.22in;"></div>
    {toc_html}
  </div>
  {folio("The Big Idea", 2)}
</div>
''')

# =================================================================
# PAGES 3-11 — TWO DIMENSIONS PER PAGE (17 dims -> 9 pages, last page has 1)
# =================================================================
def dim_card_html(d):
    chips = "".join([f'<span class="dim-pathway-chip">{p}</span>' for p in d["pathways"]])
    fs = d["flagship"]
    flagship_html = ""
    if fs:
        flagship_html = f'''
        <div class="dim-flagship">
          <div class="dim-flagship-label">Flagship Campaign</div>
          <div class="dim-flagship-title">{fs["title"]}</div>
          <div class="dim-flagship-sub">{fs["subtitle"]}</div>
        </div>'''
    return f'''
    <div class="dim-card">
      <div class="dim-num">{d["numeral"]}</div>
      <div class="dim-name">Flourishing {d["name"]}</div>
      <div class="dim-sub">{d["subtitle"]}</div>
      <div class="dim-intro">{d["intro"]}</div>
      <div class="dim-pathways">{chips}</div>
      {flagship_html}
    </div>'''

page_num = 3
i = 0
while i < len(DIMS):
    pair = DIMS[i:i+2]
    cards = "".join([dim_card_html(d) for d in pair])
    chapter_label = " & ".join([f'{d["numeral"]}. {d["name"]}' for d in pair])
    add(f'''
    <div class="page">
      <div class="frame">
        <div class="eyebrow">THE SEVENTEEN DIMENSIONS</div>
        <div style="height:0.16in;"></div>
        {cards}
      </div>
      {folio(chapter_label, page_num)}
    </div>
    ''')
    page_num += 1
    i += 2

# =================================================================
# NEXT PAGE — BY THE NUMBERS / INTEGRATED ARCHITECTURE
# =================================================================
stats = [("17", "Dimensions"), ("170", "Curriculum Pathways"), ("85", "Flagship Campaigns"), ("510", "Sessions Ready to Script")]
stats_html = "".join([f'<div style="text-align:center;"><div style="font-family:\'Playfair\'; font-weight:700; font-size:26pt; color:var(--blue);">{n}</div><div style="font-family:\'Archivo\'; font-weight:600; font-size:8.5pt; letter-spacing:0.08em; color:var(--gray); margin-top:0.04in;">{l}</div></div>' for n, l in stats])
add(f'''
<div class="page">
  <div class="frame">
    <div class="eyebrow">THE INTEGRATED ARCHITECTURE</div>
    <div style="height:0.18in;"></div>
    <h1 class="display" style="font-size:20pt; color:var(--blue);">Every campaign is now a real six-session experience &mdash; not just a title and a subtitle.</h1>
    <div style="height:0.24in;"></div>
    <div style="display:flex; justify-content:space-between; gap:0.2in; padding:0.3in 0.1in; background:var(--cream); border-radius:4px; margin-bottom:0.3in;">
      {stats_html}
    </div>
    <div class="takeaway">
      <span class="label">Personal Flourishing</span>
      Joy &middot; Health &middot; Purpose &middot; Character &middot; Resilience &middot; Growth
    </div>
    <div style="height:0.14in;"></div>
    <div class="takeaway">
      <span class="label">Relational Flourishing</span>
      Relationships &middot; Family &middot; Community
    </div>
    <div style="height:0.14in;"></div>
    <div class="takeaway">
      <span class="label">Spiritual Flourishing</span>
      Faith &middot; Generosity &middot; Legacy
    </div>
    <div style="height:0.14in;"></div>
    <div class="takeaway">
      <span class="label">Vocational &amp; Economic Flourishing</span>
      Work &middot; Business &middot; Marketplace &middot; Finances &middot; Leadership
    </div>
  </div>
  {folio("The Integrated Architecture", page_num)}
</div>
''')
page_num += 1

# =================================================================
# BACK COVER
# =================================================================
add(f'''
<div class="page blue">
  <div class="frame" style="display:flex; flex-direction:column; justify-content:space-between; align-items:center; text-align:center;">
    <div></div>
    <div>
      <div style="font-family:'Archivo'; font-weight:600; font-size:9.5pt; letter-spacing:0.28em; color:#8FB8DC;">LIFETOGETHER</div>
      <div style="height:0.26in;"></div>
      <h1 class="display" style="font-size:21pt; color:#F7FAFC;">A whole life, built one dimension at a time.</h1>
      <div style="height:0.18in;"></div>
      <p class="lede" style="max-width:4.4in; margin:0 auto;">
        Every dimension is ready to build from directly &mdash; start with the one your church
        needs most this season.
      </p>
      <div style="height:0.3in;"></div>
      <div style="width:30px; height:2px; background:#8FB8DC; margin:0 auto;"></div>
      <div style="height:0.2in;"></div>
      <div style="font-family:'Archivo'; font-weight:500; font-size:9pt; letter-spacing:0.08em; color:rgba(247,250,252,0.75);">LIFETOGETHER.COM &nbsp;&middot;&nbsp; BRETT@LIFETOGETHER.COM</div>
    </div>
    <div style="font-family:'Archivo'; font-weight:500; font-size:7.6pt; letter-spacing:0.12em; color:rgba(247,250,252,0.4);">FLOURISHING LIFETOGETHER&trade;</div>
  </div>
</div>
''')

# =================================================================
# ASSEMBLE
# =================================================================
with open("/home/claude/build/flourishing_blue_style.css") as f:
    base_css = f.read()

html = f'''<!DOCTYPE html>
<html><head><meta charset="utf-8">
<style>{base_css}</style></head>
<body>{"".join(PAGES)}</body></html>'''

with open("/home/claude/build/flourishing_brochure_blue.html", "w") as f:
    f.write(html)
print("Pages:", len(PAGES))
