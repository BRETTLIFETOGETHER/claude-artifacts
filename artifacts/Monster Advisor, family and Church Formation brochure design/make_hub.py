import sys
sys.path.insert(0, "/home/claude/build/mobile")
from components import build_css

libraries = [
    ("The Church Formation System", "The original guide", "The complete story: from the problem, through the framework, masterclass, and crawl-walk-run model, to the three ways we help.", "formation_system_mobile.html", "19-page brochure"),
    ("Executive Overview", "The short version", "A concise leave-behind covering the challenge, the five-step process, and how we can help.", "overview_mobile.html", "8-page brochure"),
    ("Flagship Guidebook", "The definitive deep dive", "Every chapter, every diagram, every detail of the Church Formation System, from vision to next steps.", "flagship_mobile.html", "23-page brochure"),
    ("Campaign Builder Intensive", "The consulting offer", "What happens if we work together — the six-week process, deliverables, and investment overview.", "intensive_mobile.html", "15-page brochure"),
    ("Biblical Purpose Library", "The curriculum platform", "Know God, Belong, Grow, Serve, Live Sent, and Multiply — the campaigns, classes, and daily journeys built on it.", "purpose_library_mobile.html", "13-page brochure"),
    ("Christian Advisor Network", "For financial advisors", "A growth, client-engagement, family-legacy, and church-partnership platform for Christian financial advisors.", "advisor_network_mobile.html", "17-page brochure"),
    ("MASTER Unified Guide", "Everything, in one place", "The full system and all three ways to work together, combined into a single unified resource.", "master_mobile.html", "28-page brochure"),
]

cards = ""
for title, kicker, desc, href, tag in libraries:
    cards += f'''
    <a class="lib-card" href="{href}">
      <div class="lib-kicker">{kicker}</div>
      <div class="lib-title">{title}</div>
      <p class="lib-desc">{desc}</p>
      <div class="lib-foot"><span class="lib-tag">{tag}</span><span class="lib-arrow">&rarr;</span></div>
    </a>'''

CSS_EXTRA = '''
.hub-hero{ background:var(--navy); background-image:linear-gradient(160deg,#16274A 0%,#0E1930 100%); }
.hub-hero .inner{ padding:60px 24px 40px; }
.hub-kicker{ font-family:'Archivo'; font-weight:600; font-size:11.5px; letter-spacing:0.22em; color:var(--gold-bright); margin-bottom:20px; }
.hub-title{ font-family:'Playfair'; font-weight:700; font-size:30px; line-height:1.16; color:var(--white); margin-bottom:16px; }
.hub-sub{ font-family:'Inter'; font-size:15px; line-height:1.6; color:rgba(251,248,241,0.85); max-width:420px; }

.lib-list{ padding:8px 24px 60px; max-width:520px; margin:0 auto; }
.lib-card{ display:block; border:1px solid var(--line); border-radius:10px; padding:20px; margin-top:16px; text-decoration:none; color:inherit; }
.lib-card:first-child{ margin-top:0; }
.lib-kicker{ font-family:'Archivo'; font-weight:600; font-size:10.5px; letter-spacing:0.12em; text-transform:uppercase; color:var(--gold); margin-bottom:6px; }
.lib-title{ font-family:'Playfair'; font-weight:700; font-size:19px; color:var(--navy); margin-bottom:8px; }
.lib-desc{ font-family:'Inter'; font-size:13.5px; line-height:1.55; color:var(--ink); margin-bottom:14px; }
.lib-foot{ display:flex; justify-content:space-between; align-items:center; }
.lib-tag{ font-family:'Archivo'; font-weight:600; font-size:10.5px; letter-spacing:0.06em; color:var(--gray); }
.lib-arrow{ font-family:'Playfair'; font-weight:700; color:var(--gold); font-size:16px; }

.hub-note{ max-width:520px; margin:0 auto; padding:0 24px 50px; font-family:'Inter'; font-size:12.5px; color:var(--gray); font-style:italic; text-align:center; line-height:1.6; }
'''

html = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1">
<title>LifeTogether — Church Formation System Library</title>
<style>{build_css()}{CSS_EXTRA}</style>
</head>
<body>
<section class="hub-hero">
  <div class="inner">
    <div class="hub-kicker">LIFETOGETHER</div>
    <h1 class="hub-title">The Church Formation System Library</h1>
    <p class="hub-sub">Every guide, every brochure, in one place &mdash; built for your
    iPhone. Tap any library below to open it.</p>
  </div>
</section>
<div class="lib-list">
  {cards}
</div>
<div class="hub-note">Each library opens as its own page and can be saved to your Home Screen for one-tap access. THE CHURCH FORMATION SYSTEM&trade;</div>
</body>
</html>'''

with open("/home/claude/build/mobile/index.html", "w", encoding="utf-8") as f:
    f.write(html)
print("Hub size:", len(html))
