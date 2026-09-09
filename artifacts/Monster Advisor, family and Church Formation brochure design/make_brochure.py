import sys
sys.path.insert(0, "/home/claude/build/catalytic_campaigns")
from data import CAMPAIGNS

PAGES = []
def add(html): PAGES.append(html)

def folio(chapter, num):
    return f'''<div class="folio"><div class="thread">{chapter}</div><div>{num:02d}</div></div>'''

# =================================================================
# PAGE 1 — COVER
# =================================================================
add(f'''
<div class="page navy">
  <div class="frame" style="display:flex; flex-direction:column; justify-content:flex-end;">
    <div style="font-family:'Archivo'; font-weight:600; font-size:9pt; letter-spacing:0.22em; color:#D9B876; margin-bottom:2.2in;">CATALYTIC SUNDAY CAMPAIGNS</div>
    <h1 class="display" style="font-size:28pt; color:#FBF8F1;">Twelve Campaigns, Fully Built</h1>
    <div style="height:0.14in;"></div>
    <div style="font-family:'Playfair'; font-style:italic; font-weight:600; font-size:13.5pt; color:#D9B876;">Title, subtitle, big idea, launch message, and a four-part outline for each.</div>
    <div style="height:0.26in;"></div>
    <p class="lede" style="font-size:10.3pt; color:rgba(251,248,241,0.8); max-width:5.6in;">
      Not a single-Sunday moment anymore &mdash; each of the twelve Catalytic Sunday
      categories, elevated into a real short campaign with its own scriptural backbone.
    </p>
  </div>
</div>
''')

# =================================================================
# PAGE 2 — INTRO
# =================================================================
add(f'''
<div class="page">
  <div class="frame">
    <div class="eyebrow">HOW TO USE THIS</div>
    <div style="height:0.2in;"></div>
    <h1 class="display" style="font-size:20pt; color:var(--navy);">The essence, or the full arc &mdash; your call per campaign.</h1>
    <div style="height:0.16in;"></div>
    <p class="lede">
      Each campaign below carries a title and subtitle, a big idea explaining the core
      conviction, a launch message capturing the single-Sunday essence, and a four-part
      outline that turns it into a short series when a church wants more than one Sunday.
    </p>
    <div style="height:0.16in;"></div>
    <p class="lede">
      Every outline point carries its own distinct scripture &mdash; nothing here repeats a
      verse or a metaphor across campaigns.
    </p>
  </div>
  {folio("How to Use This", 2)}
</div>
''')

# =================================================================
# ONE PAGE PER CAMPAIGN
# =================================================================
page_num = 3
for c in CAMPAIGNS:
    outline_html = "".join([f'''
    <div style="border-top:1px solid var(--line); padding:0.12in 0;">
      <div style="display:flex; justify-content:space-between; align-items:baseline;">
        <div style="font-family:'Playfair'; font-weight:700; font-size:12pt; color:var(--navy);">{i+1}. {t}</div>
        <div style="font-family:'Archivo'; font-weight:600; font-size:8pt; color:var(--gold); letter-spacing:0.03em;">{scripture}</div>
      </div>
      <div style="font-family:'Inter'; font-size:9pt; color:var(--gray); margin-top:0.02in;">{d}</div>
    </div>''' for i, (t, d, scripture) in enumerate(c["outline"])])

    add(f'''
    <div class="page">
      <div class="frame">
        <div class="eyebrow">CAMPAIGN {page_num - 2} OF 12</div>
        <div style="height:0.14in;"></div>
        <h1 class="display" style="font-size:20pt; color:var(--navy); line-height:1.15;">{c["title"]}</h1>
        <div style="font-family:'Playfair'; font-style:italic; font-weight:500; font-size:11.5pt; color:var(--gray); margin-top:0.06in; margin-bottom:0.18in;">{c["subtitle"]}</div>

        <div class="takeaway" style="margin-bottom:0.14in;">
          <span class="label">Big Idea</span>{c["big_idea"]}
        </div>
        <div class="takeaway" style="margin-bottom:0.18in;">
          <span class="label">Launch Message &mdash; The Essence</span>{c["launch"]}
        </div>

        <div style="font-family:'Archivo'; font-weight:700; font-size:9pt; letter-spacing:0.08em; color:var(--gold); margin-bottom:0.04in;">FOUR-PART OUTLINE</div>
        {outline_html}
      </div>
      {folio(c["title"], page_num)}
    </div>
    ''')
    page_num += 1

# =================================================================
# BACK COVER
# =================================================================
add(f'''
<div class="page navy">
  <div class="frame" style="display:flex; flex-direction:column; justify-content:space-between; align-items:center; text-align:center;">
    <div></div>
    <div>
      <div style="font-family:'Archivo'; font-weight:600; font-size:9.5pt; letter-spacing:0.28em; color:#D9B876;">LIFETOGETHER</div>
      <div style="height:0.26in;"></div>
      <h1 class="display" style="font-size:20pt; color:#FBF8F1;">Twelve Sundays. Twelve campaigns. One church, moving together.</h1>
      <div style="height:0.18in;"></div>
      <p class="lede" style="max-width:4.4in; margin:0 auto;">
        Every campaign here is ready to preach as a single message, or expand into a full
        four-week series.
      </p>
      <div style="height:0.3in;"></div>
      <div style="width:30px; height:2px; background:#B98D3E; margin:0 auto;"></div>
    </div>
    <div style="font-family:'Archivo'; font-weight:500; font-size:7.6pt; letter-spacing:0.12em; color:rgba(251,248,241,0.4);">CATALYTIC SUNDAY CAMPAIGNS &middot; TWELVE FULLY BUILT</div>
  </div>
</div>
''')

# =================================================================
# ASSEMBLE
# =================================================================
with open("/home/claude/build/portrait_style.css") as f:
    base_css = f.read()

html = f'''<!DOCTYPE html>
<html><head><meta charset="utf-8">
<style>{base_css}</style></head>
<body>{"".join(PAGES)}</body></html>'''

with open("/home/claude/build/catalytic_campaigns/catalytic_campaigns_brochure.html", "w") as f:
    f.write(html)
print("Pages:", len(PAGES))
