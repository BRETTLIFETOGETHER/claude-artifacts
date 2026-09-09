import sys, pickle, re
sys.path.insert(0, "/home/claude/build/mobile")
from components import build_css

with open("/home/claude/build/mobile/_extracted_bodies.pkl", "rb") as f:
    extracted = pickle.load(f)

files = [
    ("formation-system", "The Church Formation System", "19-page brochure", "The complete story: from the problem, through the framework, masterclass, and crawl-walk-run model, to the three ways we help."),
    ("overview", "Executive Overview", "8-page brochure", "A concise leave-behind covering the challenge, the five-step process, and how we can help."),
    ("flagship", "Flagship Guidebook", "23-page brochure", "Every chapter, every diagram, every detail of the Church Formation System, from vision to next steps."),
    ("intensive", "Campaign Builder Intensive", "15-page brochure", "What happens if we work together — the six-week process, deliverables, and investment overview."),
    ("purpose-library", "Biblical Purpose Library", "13-page brochure", "Know God, Belong, Grow, Serve, Live Sent, and Multiply — the campaigns, classes, and daily journeys built on it."),
    ("advisor-network", "Christian Advisor Network", "17-page brochure", "A growth, client-engagement, family-legacy, and church-partnership platform for Christian financial advisors."),
    ("master", "MASTER Unified Guide", "28-page brochure", "The full system and all three ways to work together, combined into a single unified resource."),
]

# ---- Hub / table of contents section ----
toc_cards = ""
for anchor, title, tag, desc in files:
    toc_cards += f'''
    <a class="lib-card" href="#{anchor}">
      <div class="lib-title">{title}</div>
      <p class="lib-desc">{desc}</p>
      <div class="lib-foot"><span class="lib-tag">{tag}</span><span class="lib-arrow">&darr;</span></div>
    </a>'''

hub_section = f'''
<section class="hub-hero">
  <div class="inner">
    <div class="hub-kicker">LIFETOGETHER</div>
    <h1 class="hub-title">The Church Formation System Library</h1>
    <p class="hub-sub">Every guide, every brochure, in one single page &mdash; built for
    your iPhone. Tap any card to jump straight to it below.</p>
  </div>
</section>
<div class="lib-list">
  {toc_cards}
</div>
'''

# ---- Each library section, wrapped with a divider header + back-to-top link ----
body_parts = [hub_section]
for anchor, title, tag, desc in files:
    divider = f'''
<section class="lib-divider" id="{anchor}">
  <div class="inner">
    <div class="lib-divider-kicker">{tag}</div>
    <h1 class="lib-divider-title">{title}</h1>
    <a href="#top" class="back-to-top">&uarr; Back to Library Index</a>
  </div>
</section>
'''
    body_parts.append(divider)
    body_parts.append(extracted[anchor])
    body_parts.append(f'<div class="section-end"><a href="#top" class="back-to-top">&uarr; Back to Library Index</a></div>')

full_body = "".join(body_parts)

EXTRA_CSS = '''
#top{ position:relative; }
.hub-hero{ background:var(--navy); background-image:linear-gradient(160deg,#16274A 0%,#0E1930 100%); }
.hub-hero .inner{ padding:60px 24px 36px; }
.hub-kicker{ font-family:'Archivo'; font-weight:600; font-size:11.5px; letter-spacing:0.22em; color:var(--gold-bright); margin-bottom:20px; }
.hub-title{ font-family:'Playfair'; font-weight:700; font-size:29px; line-height:1.18; color:var(--white); margin-bottom:14px; }
.hub-sub{ font-family:'Inter'; font-size:14.5px; line-height:1.6; color:rgba(251,248,241,0.85); max-width:420px; }

.lib-list{ padding:8px 24px 40px; max-width:520px; margin:0 auto; background:var(--navy); background-image:linear-gradient(160deg,#16274A 0%,#0E1930 100%); }
.lib-card{ display:block; border:1px solid rgba(217,184,118,0.3); border-radius:10px; padding:18px; margin-top:14px; text-decoration:none; color:inherit; background:rgba(255,255,255,0.03); }
.lib-card:first-child{ margin-top:0; }
.lib-title{ font-family:'Playfair'; font-weight:700; font-size:17px; color:#FBF8F1; margin-bottom:6px; }
.lib-desc{ font-family:'Inter'; font-size:13px; line-height:1.5; color:rgba(251,248,241,0.75); margin-bottom:12px; }
.lib-foot{ display:flex; justify-content:space-between; align-items:center; }
.lib-tag{ font-family:'Archivo'; font-weight:600; font-size:10px; letter-spacing:0.06em; color:rgba(251,248,241,0.5); }
.lib-arrow{ font-family:'Playfair'; font-weight:700; color:var(--gold-bright); font-size:16px; }

.lib-divider{ background:var(--gold); background-image:linear-gradient(135deg,#C6A15B 0%,#9E7A32 100%); }
.lib-divider .inner{ padding:36px 24px 22px; text-align:center; }
.lib-divider-kicker{ font-family:'Archivo'; font-weight:700; font-size:10.5px; letter-spacing:0.16em; text-transform:uppercase; color:rgba(16,30,56,0.65); margin-bottom:8px; }
.lib-divider-title{ font-family:'Playfair'; font-weight:700; font-size:24px; color:var(--navy); margin-bottom:14px; }
.back-to-top{ display:inline-block; font-family:'Archivo'; font-weight:600; font-size:11px; letter-spacing:0.06em; color:var(--navy); text-decoration:none; border-bottom:1px solid rgba(16,30,56,0.4); padding-bottom:2px; }
.section-end{ text-align:center; padding:28px 24px 40px; background:var(--white); }
.section-end .back-to-top{ color:var(--gold); border-bottom:1px solid var(--gold); }
'''

css = build_css() + EXTRA_CSS

html = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1">
<title>LifeTogether — Church Formation System Library</title>
<style>{css}</style>
</head>
<body id="top">
{full_body}
</body>
</html>'''

with open("/home/claude/build/mobile/combined_library.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Total size:", len(html), "chars (~%.1f MB)" % (len(html)/1024/1024))
