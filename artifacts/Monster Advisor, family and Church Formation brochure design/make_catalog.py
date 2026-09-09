import sys
sys.path.insert(0, "/home/claude/build/flourishing")
sys.path.insert(0, "/home/claude/build")
from data import DIMENSIONS

PAGES = []
def add(html): PAGES.append(html)

def folio(chapter, num):
    return f'''<div class="folio"><div class="thread">{chapter}</div><div>{num:02d}</div></div>'''

# =================================================================
# PAGE 1 — COVER
# =================================================================
add(f'''
<div class="page navy">
  <div class="photo" style="position:absolute; inset:0; border-radius:0;">
    <div class="cap" style="right:0.68in; bottom:0.5in; left:auto; text-align:right; font-size:6.8pt;">PHOTOGRAPHY — SUNRISE OVER OPEN FIELD, SINGLE PATH, WARM LIGHT</div>
  </div>
  <div style="position:absolute; inset:0; background:linear-gradient(190deg, rgba(16,30,56,0.4) 0%, rgba(16,30,56,0.88) 55%, rgba(16,30,56,0.98) 100%);"></div>
  <div class="frame" style="display:flex; flex-direction:column; justify-content:flex-end;">
    <div style="font-family:'Archivo'; font-weight:600; font-size:9pt; letter-spacing:0.22em; color:#D9B876; margin-bottom:2.2in;">A COMPLETE REFERENCE CATALOG</div>
    <h1 class="display" style="font-size:32pt; color:#FBF8F1;">Flourishing LifeTogether&trade;</h1>
    <div style="height:0.16in;"></div>
    <div style="font-family:'Playfair'; font-style:italic; font-weight:600; font-size:14.5pt; color:#D9B876;">Seventeen Dimensions of a Whole, Healthy, Purposeful, and Fruitful Life</div>
    <div style="height:0.26in;"></div>
    <div style="display:flex; gap:0.5in; flex-wrap:wrap;">
      <div><div class="cov-stat">17</div><div class="cov-stat-label">Dimensions</div></div>
      <div><div class="cov-stat">170</div><div class="cov-stat-label">Curriculum Pathways</div></div>
      <div><div class="cov-stat">85</div><div class="cov-stat-label">Flagship Campaigns</div></div>
      <div><div class="cov-stat">510</div><div class="cov-stat-label">Sessions, Ready to Script</div></div>
    </div>
  </div>
</div>
''')

# =================================================================
# PAGE 2 — HOW TO USE THIS CATALOG
# =================================================================
add(f'''
<div class="page">
  <div class="frame">
    <div class="eyebrow">HOW TO USE THIS CATALOG</div>
    <div style="height:0.2in;"></div>
    <h1 class="display" style="font-size:21pt; color:var(--navy);">Every dimension of a flourishing life, in one place.</h1>
    <div style="height:0.16in;"></div>
    <p class="lede">
      This catalog exists to make one conversation easier: helping an advisor or a family
      find the right starting point among seventeen real dimensions of a flourishing life.
      Every campaign below is a real six-session experience, not just a title and
      subtitle &mdash; ready to build from directly.
    </p>
    <div style="height:0.18in;"></div>
    <p class="lede">
      Each of the following pages covers one dimension in full: its ten curriculum
      pathways &mdash; the topics that dimension actually covers &mdash; and its five flagship
      campaigns, each with all six session titles outlined.
    </p>
    <div style="height:0.22in;"></div>
    <div class="takeaway">
      <span class="label">For an advisor, meeting with a family</span>
      Start with the dimension that matches the conversation already happening &mdash; a
      transition, a hard season, a family decision &mdash; then let the five campaigns and
      thirty sessions show exactly how deep that conversation can go.
    </div>
    <div style="height:0.16in;"></div>
    <div class="takeaway">
      <span class="label">For a family, choosing together</span>
      There is no wrong place to start. Read a few taglines aloud, notice which dimension
      names something you&rsquo;re already living through, and begin there.
    </div>
  </div>
  {folio("How to Use This Catalog", 2)}
</div>
''')

# =================================================================
# PAGE 3 — THE INTEGRATED ARCHITECTURE
# =================================================================
groups = [
    ("Personal Flourishing", ["Joy","Health","Purpose","Character","Resilience","Growth"]),
    ("Relational Flourishing", ["Relationships","Family","Community"]),
    ("Spiritual Flourishing", ["Faith","Generosity","Legacy"]),
    ("Vocational &amp; Economic Flourishing", ["Work","Business","Marketplace","Finances","Leadership"]),
]
group_html = "".join([f'''
    <div class="arch-group">
      <div class="arch-group-title">{title}</div>
      <div class="arch-group-items">{" &middot; ".join(items)}</div>
    </div>''' for title, items in groups])
add(f'''
<div class="page navy">
  <div class="frame">
    <div class="eyebrow on-dark">THE INTEGRATED ARCHITECTURE</div>
    <div style="height:0.2in;"></div>
    <h1 class="display" style="font-size:22pt; color:#FBF8F1;">Seventeen dimensions, four families.</h1>
    <div style="height:0.16in;"></div>
    <p class="lede" style="color:rgba(251,248,241,0.85);">
      No dimension stands alone. Each belongs to a larger family of flourishing &mdash;
      useful for seeing how a conversation in one area often opens the door to another.
    </p>
    <div style="height:0.3in;"></div>
    {group_html}
  </div>
  {folio("The Integrated Architecture", 3)}
</div>
''')

# =================================================================
# PAGES 4–20 — ONE PER DIMENSION
# =================================================================
def campaign_block(c):
    sess_html = "".join([f'<div class="sess-item"><span class="sess-n">{i+1}</span>{s}</div>' for i, s in enumerate(c["sessions"])])
    return f'''
    <div class="camp-card">
      <div class="camp-head">
        <span class="camp-title">{c["title"]}</span>
        <span class="camp-sub">&mdash; {c["sub"]}</span>
      </div>
      <div class="camp-sessions">{sess_html}</div>
    </div>'''

for idx, d in enumerate(DIMENSIONS):
    pathway_html = "".join([f'<div class="pw-item">{p}</div>' for p in d["pathways"]])
    campaigns_html = "".join([campaign_block(c) for c in d["campaigns"]])
    page_num = 4 + idx
    add(f'''
<div class="page">
  <div class="frame">
    <div class="eyebrow">DIMENSION {d["roman"]} OF XVII</div>
    <div style="height:0.12in;"></div>
    <h1 class="display" style="font-size:19pt; color:var(--navy); margin:0;">{d["name"]}</h1>
    <div style="font-family:'Playfair'; font-style:italic; font-weight:500; font-size:10.5pt; color:var(--gold); margin-top:0.04in;">{d["tagline"]}</div>
    <p style="font-family:'Inter'; font-size:8.6pt; color:var(--ink); line-height:1.5; margin-top:0.1in; margin-bottom:0;">{d["intro"]}</p>
    <div class="pw-grid">{pathway_html}</div>
    <div class="camp-section-label">FIVE FLAGSHIP CAMPAIGNS &middot; SIX SESSIONS EACH</div>
    <div class="camp-grid">{campaigns_html}</div>
  </div>
  {folio(d["name"], page_num)}
</div>
''')

# =================================================================
# PAGE 21 — CLOSING / HOW TO CHOOSE
# =================================================================
add(f'''
<div class="page navy">
  <div class="photo" style="position:absolute; inset:0; border-radius:0;">
    <div class="cap" style="right:0.68in; bottom:0.5in; left:auto; text-align:right; font-size:6.8pt;">PHOTOGRAPHY — ADVISOR AND FAMILY, TABLE CONVERSATION, WARM LIGHT</div>
  </div>
  <div style="position:absolute; inset:0; background:linear-gradient(190deg, rgba(16,30,56,0.4) 0%, rgba(16,30,56,0.9) 55%, rgba(16,30,56,0.98) 100%);"></div>
  <div class="frame" style="display:flex; flex-direction:column; justify-content:flex-end;">
    <div class="eyebrow on-dark">CHOOSING TOGETHER</div>
    <div style="height:0.2in;"></div>
    <h1 class="display" style="font-size:22pt; color:#FBF8F1;">Every flourishing life is different. Every starting point is valid.</h1>
    <div style="height:0.16in;"></div>
    <p class="lede" style="color:rgba(251,248,241,0.85);">
      Some families begin with Faith, or Family, or Legacy &mdash; the dimensions that feel
      most urgent right now. Others begin with Joy, or Health, or Resilience &mdash; because
      that is where they actually are this season. There is no required order. Seventeen
      dimensions, one hundred seventy pathways, and eighty-five campaigns exist so that
      wherever a family starts, there is somewhere real to go next.
    </p>
  </div>
  {folio("Choosing Together", 21)}
</div>
''')

# =================================================================
# PAGE 22 — BACK COVER
# =================================================================
add(f'''
<div class="page navy">
  <div class="frame" style="display:flex; flex-direction:column; justify-content:space-between; align-items:center; text-align:center;">
    <div></div>
    <div>
      <div style="font-family:'Archivo'; font-weight:600; font-size:9.5pt; letter-spacing:0.28em; color:#D9B876;">LIFETOGETHER</div>
      <div style="height:0.26in;"></div>
      <h1 class="display" style="font-size:20pt; color:#FBF8F1;">Flourishing LifeTogether&trade;</h1>
      <div style="height:0.14in;"></div>
      <p class="lede" style="max-width:4.4in; margin:0 auto;">
        17 dimensions &middot; 170 pathways &middot; 85 flagship campaigns &middot; 510 sessions,
        ready to script.
      </p>
      <div style="height:0.3in;"></div>
      <div style="width:30px; height:2px; background:#B98D3E; margin:0 auto;"></div>
      <div style="height:0.2in;"></div>
      <div style="font-family:'Archivo'; font-weight:500; font-size:9pt; letter-spacing:0.08em; color:rgba(251,248,241,0.75);">LIFETOGETHER.COM &nbsp;&middot;&nbsp; BRETT@LIFETOGETHER.COM</div>
    </div>
    <div style="font-family:'Archivo'; font-weight:500; font-size:7.4pt; letter-spacing:0.1em; color:rgba(251,248,241,0.4);">FLOURISHING LIFETOGETHER&trade; &middot; COMPLETE REFERENCE CATALOG</div>
  </div>
</div>
''')

# =================================================================
# ASSEMBLE
# =================================================================
with open("/home/claude/build/portrait_style.css") as f:
    base_css = f.read()

extra_css = '''
.cov-stat{ font-family:'Playfair'; font-weight:700; font-size:26pt; color:#D9B876; line-height:1; }
.cov-stat-label{ font-family:'Archivo'; font-weight:600; font-size:8pt; letter-spacing:0.08em; text-transform:uppercase; color:rgba(251,248,241,0.6); margin-top:0.06in; }

.arch-group{ border-top:1px solid rgba(217,184,118,0.3); padding:0.2in 0; }
.arch-group-title{ font-family:'Playfair'; font-weight:700; font-size:14pt; color:#FBF8F1; margin-bottom:0.06in; }
.arch-group-items{ font-family:'Archivo'; font-weight:500; font-size:9.5pt; color:#D9B876; letter-spacing:0.01em; }

.eyebrow.on-dark{ color:var(--gold-bright); }
.eyebrow.on-dark::before{ background:var(--gold-bright); }

.pw-grid{ display:grid; grid-template-columns:1fr 1fr; gap:0.03in 0.2in; margin-top:0.12in; }
.pw-item{ font-family:'Archivo'; font-weight:600; font-size:7.4pt; color:var(--gold); border-bottom:1px solid var(--line); padding:0.035in 0; letter-spacing:0.01em; }

.camp-section-label{ font-family:'Archivo'; font-weight:700; font-size:7.8pt; letter-spacing:0.12em; text-transform:uppercase; color:var(--navy); margin-top:0.16in; margin-bottom:0.08in; border-top:2px solid var(--gold); padding-top:0.08in; }

.camp-grid{ display:flex; flex-direction:column; }
.camp-card{ border-bottom:1px solid var(--line); padding:0.09in 0; }
.camp-card:last-child{ border-bottom:none; }
.camp-head{ margin-bottom:0.04in; }
.camp-title{ font-family:'Playfair'; font-weight:700; font-size:9.8pt; color:var(--navy); }
.camp-sub{ font-family:'Inter'; font-style:italic; font-size:7.6pt; color:var(--gray); }
.camp-sessions{ display:grid; grid-template-columns:1fr 1fr; gap:0.01in 0.16in; }
.sess-item{ font-family:'Inter'; font-size:6.9pt; color:var(--ink); line-height:1.42; padding:0.015in 0; }
.sess-n{ color:var(--gold); font-weight:600; margin-right:0.04in; }
'''

html = f'''<!DOCTYPE html>
<html><head><meta charset="utf-8">
<style>{base_css}{extra_css}</style></head>
<body>{"".join(PAGES)}</body></html>'''

with open("/home/claude/build/flourishing/catalog.html", "w") as f:
    f.write(html)
print("Pages:", len(PAGES))
