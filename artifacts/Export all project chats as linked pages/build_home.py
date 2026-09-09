#!/usr/bin/env python3
"""Build the 40daycampaigns.com home page — self-contained single file, every nav link working."""
import base64
from pathlib import Path

FONTS = Path("/home/claude/fonts")
OUT = Path("/home/claude/home_build")
OUT.mkdir(exist_ok=True)

def b64(name):
    p = FONTS / name
    return base64.b64encode(p.read_bytes()).decode() if p.exists() else None

hk, sp = b64("Hanken.ttf"), b64("Spectral.ttf")
font_css = ""
if hk: font_css += "@font-face{font-family:'Hanken Grotesk';src:url(data:font/ttf;base64,%s);font-weight:100 900;}" % hk
if sp: font_css += "@font-face{font-family:'Spectral';src:url(data:font/ttf;base64,%s);font-weight:400;}" % sp

CATS = [
    ("Finances", "#0E7490", "#67E8F9"), ("Peace & Emotional Health", "#4338CA", "#A5B4FC"),
    ("Stewardship", "#B45309", "#FCD34D"), ("Generosity", "#BE185D", "#F9A8D4"),
    ("Relationships", "#B91C1C", "#FCA5A5"), ("Purpose", "#6D28D9", "#C4B5FD"),
    ("Whole Life Health", "#047857", "#6EE7B7"), ("Marketplace", "#1D4ED8", "#93C5FD"),
    ("Prayer", "#7C2D12", "#FDBA74"), ("Hope & Healing", "#9D174D", "#FBCFE8"),
]
cat_cards = "".join(
    f'<a class="cat" href="#cta" style="background:linear-gradient(135deg,{a} 0%,{b} 130%);">'
    f'<div class="cat-count">1,000 campaigns</div><div class="cat-name">{n}</div>'
    f'<div class="cat-tab"></div></a>'
    for n, a, b in CATS)

FEATURED = [
    ("God Owns It All", "Stewardship", "#B45309", "#FCD34D"),
    ("Finding Peace", "Peace & Emotional Health", "#4338CA", "#A5B4FC"),
    ("Money Wise", "Finances", "#0E7490", "#67E8F9"),
    ("Made to Give", "Generosity", "#BE185D", "#F9A8D4"),
    ("Hope Rising", "Hope & Healing", "#9D174D", "#FBCFE8"),
    ("Flourish", "Whole Life Health", "#047857", "#6EE7B7"),
]
feat_cards = "".join(
    f'<a class="feat" href="#cta"><div class="feat-cover" style="background:linear-gradient(150deg,{a} 0%,{b} 140%);">'
    f'<span class="feat-days">40 DAYS</span><span class="feat-title">{t}</span></div>'
    f'<div class="feat-meta">{c}</div></a>'
    for t, c, a, b in FEATURED)

html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>40 Day Campaigns — The World's Largest Christian Campaign Platform</title>
<style>
{font_css}
:root{{--orange:#F26C1E;--gold:#E4AC43;--ink:#1F2430;--soft:#5B6472;--paper:#FFFFFF;--wash:#FFF7F0;--wash2:#F4F7FB;--line:#ECE7DF;}}
*{{margin:0;padding:0;box-sizing:border-box;}}
html{{scroll-behavior:smooth;}}
body{{font-family:'Hanken Grotesk',-apple-system,'Segoe UI',sans-serif;color:var(--ink);background:var(--paper);line-height:1.6;}}
a{{text-decoration:none;color:inherit;}}
.wrap{{max-width:1180px;margin:0 auto;padding:0 22px;}}
.eyebrow{{font-size:12px;font-weight:700;letter-spacing:2.5px;text-transform:uppercase;color:var(--orange);}}
h2{{font-size:36px;font-weight:800;letter-spacing:-.6px;line-height:1.15;margin:10px 0 14px;}}
.lede{{font-family:'Spectral',Georgia,serif;font-size:18px;color:var(--soft);max-width:640px;}}
.btn{{display:inline-block;background:var(--orange);color:#fff;font-weight:700;font-size:15.5px;padding:14px 28px;border-radius:999px;transition:all .2s;box-shadow:0 6px 18px rgba(242,108,30,.28);}}
.btn:hover{{transform:translateY(-2px);box-shadow:0 10px 24px rgba(242,108,30,.36);}}
.btn.ghost{{background:#fff;color:var(--ink);border:1.5px solid var(--line);box-shadow:none;}}
.btn.ghost:hover{{border-color:var(--orange);color:var(--orange);}}
/* nav */
.nav{{position:sticky;top:0;z-index:50;background:rgba(255,255,255,.92);backdrop-filter:blur(10px);border-bottom:1px solid var(--line);}}
.nav-in{{max-width:1180px;margin:0 auto;display:flex;align-items:center;gap:28px;padding:14px 22px;}}
.logo{{font-weight:800;font-size:19px;letter-spacing:-.3px;}}
.logo em{{font-style:normal;color:var(--orange);}}
.nav-links{{display:flex;gap:24px;flex:1;justify-content:center;}}
.nav-links a{{font-size:14.5px;font-weight:600;color:var(--soft);}}
.nav-links a:hover{{color:var(--orange);}}
.nav .btn{{padding:10px 20px;font-size:14px;}}
/* hero */
.hero{{background:radial-gradient(1100px 520px at 15% -10%, var(--wash) 0%, transparent 60%),radial-gradient(900px 480px at 95% 0%, var(--wash2) 0%, transparent 55%);padding:84px 0 30px;}}
.hero-grid{{display:grid;grid-template-columns:1.05fr .95fr;gap:44px;align-items:center;}}
.hero h1{{font-size:54px;font-weight:800;letter-spacing:-1.4px;line-height:1.06;margin:14px 0 18px;}}
.hero h1 em{{font-style:normal;color:var(--orange);}}
.hero .lede{{margin-bottom:26px;}}
.hero-ctas{{display:flex;gap:14px;flex-wrap:wrap;}}
.hero-art{{position:relative;height:420px;}}
.hcard{{position:absolute;width:200px;height:265px;border-radius:14px;box-shadow:0 18px 40px rgba(31,36,48,.22);display:flex;flex-direction:column;justify-content:flex-end;padding:16px;color:#fff;overflow:hidden;}}
.hcard .d{{font-size:10.5px;font-weight:800;letter-spacing:2px;opacity:.85;}}
.hcard .t{{font-size:19px;font-weight:800;line-height:1.15;letter-spacing:-.3px;}}
.hcard::after{{content:'';position:absolute;left:0;right:0;bottom:0;height:8px;background:var(--orange);border-radius:0 8px 0 0;width:46%;}}
/* stats */
.stats{{border-top:1px solid var(--line);border-bottom:1px solid var(--line);background:#fff;}}
.stats-in{{max-width:1180px;margin:0 auto;display:flex;flex-wrap:wrap;justify-content:space-between;padding:26px 22px;gap:18px;}}
.stat b{{display:block;font-size:30px;font-weight:800;letter-spacing:-.8px;color:var(--ink);}}
.stat span{{font-size:12.5px;font-weight:700;letter-spacing:1.5px;text-transform:uppercase;color:var(--soft);}}
section{{padding:74px 0;}}
.alt{{background:var(--wash2);}}
.warm{{background:var(--wash);}}
/* categories */
.cat-grid{{display:grid;grid-template-columns:repeat(5,1fr);gap:16px;margin-top:26px;}}
.cat{{position:relative;border-radius:14px;min-height:150px;padding:18px;display:flex;flex-direction:column;justify-content:flex-end;color:#fff;overflow:hidden;transition:transform .2s,box-shadow .2s;box-shadow:0 8px 20px rgba(31,36,48,.14);}}
.cat:hover{{transform:translateY(-4px);box-shadow:0 14px 30px rgba(31,36,48,.22);}}
.cat-count{{font-size:11px;font-weight:800;letter-spacing:1.5px;text-transform:uppercase;opacity:.85;}}
.cat-name{{font-size:18px;font-weight:800;letter-spacing:-.3px;line-height:1.2;}}
.cat-tab{{position:absolute;top:0;left:0;width:44%;height:7px;background:rgba(255,255,255,.85);border-radius:0 0 8px 0;}}
/* funnel */
.split{{display:grid;grid-template-columns:1fr 1fr;gap:46px;align-items:center;}}
.quote{{font-family:'Spectral',Georgia,serif;font-size:23px;line-height:1.5;color:var(--ink);border-left:4px solid var(--gold);padding-left:22px;}}
.quote small{{display:block;margin-top:12px;font-family:'Hanken Grotesk',sans-serif;font-size:12px;font-weight:700;letter-spacing:2px;text-transform:uppercase;color:var(--soft);}}
/* formats */
.fmt-grid{{display:grid;grid-template-columns:1fr 1fr;gap:20px;margin-top:26px;}}
.fmt{{background:#fff;border:1px solid var(--line);border-radius:16px;padding:30px;box-shadow:0 8px 22px rgba(31,36,48,.07);}}
.fmt .tag{{display:inline-block;font-size:11px;font-weight:800;letter-spacing:2px;text-transform:uppercase;color:#fff;background:var(--orange);border-radius:999px;padding:6px 14px;margin-bottom:14px;}}
.fmt.gold .tag{{background:var(--gold);color:var(--ink);}}
.fmt h3{{font-size:25px;font-weight:800;letter-spacing:-.5px;margin-bottom:8px;}}
.fmt p{{font-size:15px;color:var(--soft);margin-bottom:14px;}}
.fmt ul{{list-style:none;}}
.fmt li{{font-size:14.5px;padding:7px 0 7px 26px;position:relative;border-top:1px dashed var(--line);}}
.fmt li::before{{content:'✓';position:absolute;left:2px;color:var(--orange);font-weight:800;}}
.fmt.gold li::before{{color:var(--gold);}}
/* includes */
.inc-grid{{display:grid;grid-template-columns:repeat(3,1fr);gap:16px;margin-top:26px;}}
.inc{{background:#fff;border:1px solid var(--line);border-radius:14px;padding:22px;box-shadow:0 6px 16px rgba(31,36,48,.06);}}
.inc b{{display:block;font-size:16.5px;font-weight:800;margin-bottom:5px;}}
.inc span{{font-size:14px;color:var(--soft);}}
/* featured */
.feat-row{{display:grid;grid-template-columns:repeat(6,1fr);gap:16px;margin-top:26px;}}
.feat-cover{{aspect-ratio:3/4;border-radius:12px;display:flex;flex-direction:column;justify-content:flex-end;padding:14px;color:#fff;box-shadow:0 10px 22px rgba(31,36,48,.16);transition:transform .2s;position:relative;overflow:hidden;}}
.feat:hover .feat-cover{{transform:translateY(-5px);}}
.feat-days{{font-size:9.5px;font-weight:800;letter-spacing:2px;opacity:.85;}}
.feat-title{{font-size:16.5px;font-weight:800;line-height:1.15;letter-spacing:-.3px;}}
.feat-meta{{font-size:12.5px;font-weight:700;color:var(--soft);margin-top:9px;}}
/* packages */
.pack{{display:grid;grid-template-columns:1fr 1fr;gap:20px;margin-top:26px;}}
.price-card{{background:#fff;border:1.5px solid var(--line);border-radius:16px;padding:30px;text-align:left;}}
.price-card.hot{{border-color:var(--orange);box-shadow:0 12px 30px rgba(242,108,30,.16);}}
.price-card .pc-tag{{font-size:11px;font-weight:800;letter-spacing:2px;text-transform:uppercase;color:var(--orange);}}
.price-card h3{{font-size:23px;font-weight:800;margin:8px 0 4px;}}
.price-card .amt{{font-size:34px;font-weight:800;letter-spacing:-1px;}}
.price-card .amt small{{font-size:14px;font-weight:600;color:var(--soft);}}
.price-card p{{font-size:14.5px;color:var(--soft);margin:10px 0 0;}}
/* heritage */
.her{{display:grid;grid-template-columns:1.1fr .9fr;gap:46px;align-items:center;}}
.her-stats{{display:grid;grid-template-columns:1fr 1fr;gap:14px;}}
.hstat{{background:#fff;border:1px solid var(--line);border-radius:14px;padding:22px;text-align:center;}}
.hstat b{{display:block;font-size:30px;font-weight:800;color:var(--orange);letter-spacing:-.8px;}}
.hstat span{{font-size:12px;font-weight:700;letter-spacing:1.5px;text-transform:uppercase;color:var(--soft);}}
/* faq */
details{{background:#fff;border:1px solid var(--line);border-radius:12px;padding:18px 22px;margin-top:12px;}}
summary{{cursor:pointer;font-weight:700;font-size:16px;list-style:none;position:relative;padding-right:28px;}}
summary::after{{content:'+';position:absolute;right:2px;top:-2px;font-size:22px;color:var(--orange);}}
details[open] summary::after{{content:'–';}}
details p{{margin-top:10px;font-size:15px;color:var(--soft);}}
/* cta */
.cta{{background:linear-gradient(135deg,#20140C 0%, #3A2312 60%, #6E3A12 130%);color:#fff;text-align:center;padding:84px 0;}}
.cta h2{{color:#fff;font-size:40px;}}
.cta .lede{{color:rgba(255,255,255,.82);margin:0 auto 28px;}}
.cta .btn{{background:var(--gold);color:var(--ink);}}
.footer{{background:#14100C;color:rgba(255,255,255,.75);padding:34px 0;font-size:14px;}}
.foot-in{{max-width:1180px;margin:0 auto;padding:0 22px;display:flex;justify-content:space-between;gap:16px;flex-wrap:wrap;}}
.foot-in b{{color:#fff;}}
@media(max-width:960px){{.hero-grid,.split,.fmt-grid,.her,.pack{{grid-template-columns:1fr;}}.hero-art{{display:none;}}.cat-grid{{grid-template-columns:repeat(2,1fr);}}.feat-row{{grid-template-columns:repeat(3,1fr);}}.inc-grid{{grid-template-columns:1fr 1fr;}}.hero h1{{font-size:38px;}}h2{{font-size:29px;}}}}
</style>
</head>
<body>

<nav class="nav"><div class="nav-in">
<a class="logo" href="#top">40 <em>Day</em> Campaigns</a>
<div class="nav-links">
<a href="#categories">Browse</a><a href="#formats">Formats</a><a href="#includes">What's Included</a><a href="#packages">Packages</a><a href="#heritage">About</a>
</div>
<a class="btn" href="#cta">Get Access</a>
</div></nav>

<header class="hero" id="top"><div class="wrap"><div class="hero-grid">
<div>
<div class="eyebrow">The World's Largest Christian Campaign Platform</div>
<h1>10,000 campaigns.<br>One church-wide <em>movement.</em></h1>
<p class="lede">The only platform that reaches your senior pastor, your small group leaders, your students, your children, and your families — all in the same campaign, all in the same week, all in your church's voice.</p>
<div class="hero-ctas"><a class="btn" href="#categories">Browse the Library</a><a class="btn ghost" href="#formats">See How It Works</a></div>
</div>
<div class="hero-art">
<div class="hcard" style="left:6%;top:8%;transform:rotate(-6deg);background:linear-gradient(150deg,#B45309,#FCD34D);"><span class="d">40 DAYS</span><span class="t">God Owns It All</span></div>
<div class="hcard" style="left:38%;top:22%;transform:rotate(3deg);background:linear-gradient(150deg,#4338CA,#A5B4FC);"><span class="d">40 DAYS</span><span class="t">Finding Peace</span></div>
<div class="hcard" style="left:66%;top:2%;transform:rotate(8deg);background:linear-gradient(150deg,#047857,#6EE7B7);"><span class="d">40 DAYS</span><span class="t">Flourish</span></div>
</div>
</div></div></header>

<div class="stats"><div class="stats-in">
<div class="stat"><b>10,000</b><span>Campaigns</span></div>
<div class="stat"><b>100</b><span>Themes</span></div>
<div class="stat"><b>10</b><span>Categories</span></div>
<div class="stat"><b>500+</b><span>Church Partnerships</span></div>
<div class="stat"><b>25+</b><span>Years of Campaigns</span></div>
</div></div>

<section id="categories"><div class="wrap">
<div class="eyebrow">Browse the Library</div>
<h2>Every felt need. Every season. Every church.</h2>
<p class="lede">Ten categories, one hundred themes, and a thousand campaigns behind every door — each one a complete 40-day journey for your whole congregation.</p>
<div class="cat-grid">{cat_cards}</div>
</div></section>

<section class="alt" id="funnel"><div class="wrap"><div class="split">
<div>
<div class="eyebrow">The Spiritual Funnel</div>
<h2>Don't launch your next series cold.</h2>
<p class="lede">Most sermon series lose momentum after launch Sunday. A campaign does the opposite — it creates momentum before week two even begins, moving people from awareness to engagement, from engagement to relationship, from relationship to testimony, and from testimony to response.</p>
</div>
<div class="quote">"Every ministry initiative needs a funnel. The campaign is that funnel — the spark that starts a congregation moving, and the engine that sustains a season of transformation."<small>The Lifetogether Campaign Architecture</small></div>
</div></div></section>

<section id="formats"><div class="wrap">
<div class="eyebrow">Two Formats · One Platform</div>
<h2>The spark, and the engine.</h2>
<p class="lede">The Seven Day Experience and the 40-Day Campaign are not competing products. They are partners. Every church can start somewhere. Every church can go further.</p>
<div class="fmt-grid">
<div class="fmt"><span class="tag">The Spark · Start Here</span><h3>The Seven Day Experience</h3>
<p>Kickoff Sunday to Celebration Sunday — eight days total. A low-barrier, finishable experience any church can execute, powered by Each One Ask One activation.</p>
<ul><li>Anyone can say yes to one week</li><li>Stories and engagement visible within seven days</li><li>Attaches to any sermon series, holiday, or season</li><li>Adult, Youth, and Children's + Family editions — simultaneously</li></ul></div>
<div class="fmt gold"><span class="tag">The Engine · Go Deeper</span><h3>The 40-Day Campaign</h3>
<p>A defined six-week season of transformation — fall, spring, or Lent — with formats at 7, 21, 30, or 40 days to fit your calendar.</p>
<ul><li>Deep formation across weeks and months</li><li>Six-session small group study built in</li><li>Church-wide alignment from pulpit to living room</li><li>Ten categories of felt-need themes to choose from</li></ul></div>
</div>
</div></section>

<section class="warm" id="includes"><div class="wrap">
<div class="eyebrow">What's Included</div>
<h2>Every campaign. Every person. Every day.</h2>
<p class="lede">Complete campaign ecosystems — fully branded for your church, print-ready, and built on 25 years of campaign architecture.</p>
<div class="inc-grid">
<div class="inc"><b>Daily Devotionals</b><span>A complete 40-day reading journey for every adult in your church.</span></div>
<div class="inc"><b>Six-Session Group Study</b><span>Small group curriculum with discussion questions and weekly practices.</span></div>
<div class="inc"><b>Six Full Sermons</b><span>Complete message outlines, preaching ideas, and supporting texts for the pulpit.</span></div>
<div class="inc"><b>Youth Edition</b><span>Six student sessions translating the theme for the next generation.</span></div>
<div class="inc"><b>Children's Edition</b><span>Bible-story lessons with activities and parent send-homes.</span></div>
<div class="inc"><b>Leader Training Kit</b><span>Host training, ask scripts, launch timeline, and recruitment tools.</span></div>
</div>
</div></section>

<section id="featured"><div class="wrap">
<div class="eyebrow">Featured Campaigns</div>
<h2>Start with a flagship.</h2>
<div class="feat-row">{feat_cards}</div>
</div></section>

<section class="alt" id="packages"><div class="wrap">
<div class="eyebrow">Campaign Packages</div>
<h2>Four tiers. Four formats. Everything your church needs.</h2>
<div class="pack">
<div class="price-card"><div class="pc-tag">Start Here</div><h3>Seven Day Experience</h3>
<div class="amt">From $199 <small>Starter · $599 Custom · $1,499 Premium Pathway</small></div>
<p>The low-risk pilot before 40 days — a series launch or capital campaign runway your whole church can finish.</p></div>
<div class="price-card hot"><div class="pc-tag">Most Popular</div><h3>Digital Essentials</h3>
<div class="amt">$1,499 <small>one-time</small></div>
<p>Tier one of four complete campaign ecosystems — adult, youth, children, and family editions, fully branded for your church and print-ready.</p></div>
</div>
</div></section>

<section id="heritage"><div class="wrap"><div class="her">
<div>
<div class="eyebrow">The Lifetogether Heritage</div>
<h2>Built on the campaigns that shaped a generation.</h2>
<p class="lede">From Willow Creek to Saddleback and the Purpose Driven Life campaign rooms, this platform carries twenty-five years of churchwide campaign architecture — the same model that helped hundreds of churches move an entire congregation in the same direction at the same time. Now it's yours, at a scale never possible before.</p>
</div>
<div class="her-stats">
<div class="hstat"><b>25+</b><span>Years</span></div>
<div class="hstat"><b>500+</b><span>Churches</span></div>
<div class="hstat"><b>4</b><span>Editions per Campaign</span></div>
<div class="hstat"><b>40</b><span>Days of Formation</span></div>
</div>
</div></div></section>

<section class="warm" id="faq"><div class="wrap">
<div class="eyebrow">Questions</div>
<h2>What pastors ask first.</h2>
<details open><summary>How is this different from buying a study off the shelf?</summary><p>A study serves a group. A campaign moves a church — pulpit, groups, students, children, and homes aligned around one theme for one season, in your church's voice.</p></details>
<details><summary>We've never run a churchwide campaign. Where do we start?</summary><p>Start with the Seven Day Experience. It's a finishable, low-barrier week that builds momentum and proves the model before you commit to a full 40-day season.</p></details>
<details><summary>Can we brand the materials for our church?</summary><p>Yes — every package includes fully branded, print-ready editions across adult, youth, children's, and family formats.</p></details>
</div></section>

<section class="cta" id="cta"><div class="wrap">
<h2>Your next 40 days can change everything.</h2>
<p class="lede">Join the churches building movements, not just sermon series.</p>
<a class="btn" href="mailto:brett@lifetogether.com">Get Access</a>
</div></section>

<footer class="footer"><div class="foot-in">
<div><b>40 Day Campaigns</b> · A Lifetogether Platform</div>
<div>brett@lifetogether.com · 40daycampaigns.com</div>
</div></footer>

</body>
</html>"""

(OUT / "index.html").write_text(html)
print(f"Home page written: {len(html)/1024:.0f} KB, fonts embedded: {sum(1 for x in (hk,sp) if x)}/2")

# Verify every internal anchor resolves
import re
hrefs = set(re.findall(r'href="#([^"]+)"', html))
ids = set(re.findall(r'id="([^"]+)"', html))
missing = hrefs - ids
assert not missing, f"Broken anchors: {missing}"
print(f"Anchor check: {len(hrefs)} internal links, all resolve to page sections")
