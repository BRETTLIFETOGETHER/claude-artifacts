# -*- coding: utf-8 -*-
import csv, html as H
from collections import OrderedDict, defaultdict

def esc(s):
    return H.escape(s, quote=False)

def slug(s):
    return "".join(c if c.isalnum() else "-" for c in s.lower()).strip("-")

SECTIONS = ["Calling & Purpose", "Leadership & Character", "Stewardship & Excellence",
            "Relationships & Culture", "Legacy & Kingdom Impact"]

new_cats = OrderedDict()
with open("campaigns.csv") as f:
    for row in csv.DictReader(f):
        new_cats.setdefault(row["Category"], defaultdict(list))[row["Section"]].append(
            (row["Title"], row["Subtitle"]))

NEW_CATEGORY_BLURBS = {
    "Physicians": "Doctors carrying the weight of diagnosis, healing, and patient care.",
    "Dentists": "Dental professionals building trust one appointment at a time.",
    "Nurses": "The bedside calling -- endurance, compassion, and sacred presence.",
    "Therapists & Counselors": "Carrying others' pain without losing your own soul.",
    "Accountants & CPAs": "Stewardship, precision, and integrity in the numbers.",
    "Architects": "Designing spaces that serve people and reflect the Creator.",
    "Commercial Real Estate": "High-stakes deals and the character to negotiate with integrity.",
    "Insurance Professionals": "Protecting families through the policies and the claims.",
    "Bankers": "Stewarding other people's money with wisdom and trust.",
    "Private Equity & Venture Capital": "Capital, character, and the pressure to return results.",
    "Family Office Executives": "Stewarding generational wealth for the families you serve.",
    "Engineers": "Precision and purpose in every design and build.",
    "Scientists": "Discovery as an act of worship in the laboratory.",
    "University Faculty": "Shaping minds under publish-or-perish pressure.",
    "Coaches & Consultants": "Advising others while staying grounded yourself.",
    "Human Resources": "Caught in the middle, called to serve every employee well.",
    "Manufacturing Executives": "Leading operations with excellence and care for your workforce.",
    "Franchise Owners": "Running the business while building people, not just locations.",
    "Restaurant & Hospitality Owners": "Serving guests and staff through the rush and the rebuild.",
    "Agriculture & Food Producers": "Feeding people faithfully, season after uncertain season.",
}

def render_ts_list(pairs, start=1):
    return "\n".join(
        f'<li class="d-item"><span class="d-num">{i:02d}</span>'
        f'<span class="d-text"><span class="d-title">{esc(t)}</span>'
        f'<span class="d-sub">{esc(s)}</span></span></li>'
        for i, (t, s) in enumerate(pairs, start=start)
    )

total_campaigns = sum(sum(len(v) for v in sec.values()) for sec in new_cats.values())

toc_html = "\n".join(
    f'<li><a href="#{slug(n)}"><span class="toc-num">{i+1:02d}</span>{esc(n)}</a></li>'
    for i, n in enumerate(new_cats.keys())
)

cat_blocks = ""
for name, sections in new_cats.items():
    blocks = []
    for sec_name in SECTIONS:
        pairs = sections[sec_name]
        blocks.append(f"""
    <div class="sub-block">
      <h3 class="sub-head">{esc(sec_name)}</h3>
      <ul class="d-grid">{render_ts_list(pairs)}</ul>
    </div>""")
    cat_blocks += f"""
<section class="cat-block" id="{slug(name)}">
  <div class="cat-head">
    <span class="cat-eyebrow">New Vertical &middot; Business &amp; Workplace Intelligence&trade;</span>
    <h2>{esc(name)}</h2>
    <p class="cat-blurb">{esc(NEW_CATEGORY_BLURBS.get(name, ""))}</p>
    <p class="cat-meta">50 flagship campaigns &middot; 5 sections &times; 10 titles</p>
  </div>
  {"".join(blocks)}
</section>
"""

CSS = """
:root{
  --navy:#101a33; --navy-2:#16223f;
  --gold:#b8934e; --gold-light:#d9bc82;
  --cream:#f7f3ea; --hair:rgba(184,147,78,.35);
  --muted:rgba(247,243,234,.82); --muted2:rgba(247,243,234,.6);
}
*{box-sizing:border-box;}
html{scroll-behavior:smooth;}
body{margin:0; background:var(--navy); color:var(--cream); font-family:'Cormorant Garamond',serif; font-size:17px;}
h1,h2,h3{font-family:'Playfair Display',serif; margin:0; font-weight:600; color:#fbf7ee;}
a{color:var(--gold-light); text-decoration:none;}
.wrap{max-width:1180px; margin:0 auto; padding:0 28px;}
.page-narrow{max-width:820px; margin:0 auto; padding:0 40px;}

/* HERO -- matches the Purpose-Based Business brochure exactly */
.hero{padding:96px 0 60px; text-align:center; border-bottom:1px solid var(--hair);}
.eyebrow{font-family:'Cormorant Garamond',serif; letter-spacing:.32em; text-transform:uppercase;
  font-size:12.5px; color:var(--gold-light);}
h1.title{font-family:'Playfair Display',serif; font-weight:600; font-size:44px; line-height:1.15;
  text-align:center; margin:18px 0 10px; color:#fbf7ee;}
.subtitle{text-align:center; font-style:italic; font-size:20px; color:var(--gold-light);
  margin:0 0 30px; font-weight:400;}
.rule{width:120px; height:1px; background:var(--gold); margin:0 auto 40px; opacity:.6;}
.intro{font-size:18.5px; line-height:1.75; color:#e9e3d4; text-align:center; max-width:640px;
  margin:0 auto 20px;}
.intro .dropcap{font-family:'Playfair Display',serif; font-size:56px; float:left; line-height:0.8;
  padding-right:10px; padding-top:6px; color:var(--gold);}
.stat-bar{display:flex; justify-content:center; gap:56px; margin-top:44px; flex-wrap:wrap;}
.stat{text-align:center;}
.stat .n{font-family:'Playfair Display',serif; font-size:2.1rem; color:var(--gold-light);}
.stat .l{font-family:'Lato',sans-serif; font-size:.72rem; letter-spacing:.1em; text-transform:uppercase; color:var(--muted2);}

/* FRAMEWORK STRIP */
.framework{padding:56px 0; border-bottom:1px solid var(--hair); background:var(--navy-2);}
.framework h2{font-size:1.7rem; text-align:center; margin-bottom:8px;}
.framework .sub{text-align:center; color:var(--muted); max-width:640px; margin:0 auto 32px; font-style:italic;}
.framework-cols{display:grid; grid-template-columns:repeat(5,1fr); gap:16px;}
.framework-cols div{border:1px solid var(--hair); border-radius:4px; padding:16px 12px; text-align:center;}
.framework-cols .fn{font-family:'Playfair Display',serif; color:var(--gold-light); font-size:1.3rem;}
.framework-cols .ft{font-family:'Lato',sans-serif; font-size:.82rem; margin-top:8px; color:var(--muted);}
@media(max-width:760px){.framework-cols{grid-template-columns:repeat(2,1fr);}}

/* TOC */
.toc{padding:52px 0; border-bottom:1px solid var(--hair);}
.toc h2{font-size:1.5rem; margin-bottom:22px; text-align:center;}
.toc ul{list-style:none; margin:0; padding:0; column-count:2; column-gap:40px;}
@media(min-width:760px){.toc ul{column-count:2;}}
.toc li{break-inside:avoid; margin-bottom:9px; font-size:.95rem; border-bottom:1px dotted var(--hair); padding-bottom:7px;}
.toc a{color:var(--cream); display:flex; gap:10px;}
.toc a:hover{color:var(--gold-light);}
.toc-num{color:var(--gold); font-variant-numeric:tabular-nums; min-width:22px;}

/* CATEGORY BLOCKS */
.cat-block{padding:52px 0; border-bottom:1px solid var(--hair);}
.cat-block:nth-of-type(even){background:rgba(255,255,255,.012);}
.cat-head{margin-bottom:26px;}
.cat-eyebrow{font-style:italic; letter-spacing:.06em; color:var(--gold-light); font-size:.95rem;}
.cat-head h2{font-size:1.85rem; margin-top:8px;}
.cat-blurb{color:#e9e3d4; font-size:1.02rem; margin-top:8px; max-width:640px;}
.cat-meta{font-family:'Lato',sans-serif; color:var(--muted2); font-size:.78rem; margin-top:6px; letter-spacing:.03em;}

.sub-block{margin-top:28px;}
.sub-head{font-size:1.05rem; color:var(--gold-light); margin-bottom:14px; padding-bottom:8px;
  border-bottom:1px solid var(--hair); font-family:'Playfair Display',serif;}

.d-grid{list-style:none; margin:0; padding:0; display:grid; grid-template-columns:1fr 1fr; gap:0 32px;}
@media(max-width:720px){.d-grid{grid-template-columns:1fr;}}
.d-item{display:flex; gap:12px; padding:8px 0; border-bottom:1px solid rgba(255,255,255,.05);}
.d-num{font-family:'Lato',sans-serif; color:var(--gold); font-size:.76rem; padding-top:3px; min-width:20px;}
.d-text{display:flex; flex-direction:column;}
.d-title{font-family:'Lato',sans-serif; font-weight:700; font-size:.95rem; color:var(--cream);}
.d-sub{font-style:italic; color:var(--muted); font-size:.94rem; margin-top:1px;}

footer{padding:60px 0 90px; text-align:center; color:var(--muted2); font-family:'Lato',sans-serif; font-size:.82rem;}
footer .mark{font-family:'Playfair Display',serif; font-size:14px; letter-spacing:.28em; text-transform:uppercase; color:var(--gold);}
footer .tag{margin-top:8px; font-size:14.5px; font-style:italic; color:rgba(247,243,234,.5); font-family:'Cormorant Garamond',serif;}

@media (max-width:600px){
  h1.title{font-size:32px;}
  .intro{font-size:17px;}
}
"""

HTML = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>20 New Marketplace Channels &mdash; LifeTogether Business &amp; Workplace Intelligence&trade;</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,500;0,600;0,700;1,500&family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;1,400&family=Lato:wght@400;700&display=swap" rel="stylesheet">
<style>{CSS}</style>
</head>
<body>

<section class="hero">
  <div class="page-narrow">
    <div class="eyebrow">LifeTogether Business &amp; Workplace Intelligence&trade;</div>
    <h1 class="title">20 New Marketplace Channels</h1>
    <div class="subtitle">Twenty Professions. One Shared Architecture.</div>
    <div class="rule"></div>
    <p class="intro"><span class="dropcap">F</span>rom the exam room to the deal room, the plant floor to
       the dining room &mdash; twenty new professional verticals, each built on the same five-section,
       fifty-campaign framework already proven across LifeTogether's Business &amp; Workplace
       Intelligence&trade; library.</p>
    <div class="stat-bar">
      <div class="stat"><div class="n">20</div><div class="l">New Categories</div></div>
      <div class="stat"><div class="n">{total_campaigns:,}</div><div class="l">Flagship Campaigns</div></div>
      <div class="stat"><div class="n">5</div><div class="l">Sections per Category</div></div>
      <div class="stat"><div class="n">10</div><div class="l">Titles per Section</div></div>
    </div>
  </div>
</section>

<section class="framework">
  <div class="wrap">
    <h2>One Framework, Every Profession</h2>
    <p class="sub">Every category below shares the identical backbone &mdash; only the language of the
       vocation changes.</p>
    <div class="framework-cols">
      <div><div class="fn">01</div><div class="ft">Calling &amp; Purpose</div></div>
      <div><div class="fn">02</div><div class="ft">Leadership &amp; Character</div></div>
      <div><div class="fn">03</div><div class="ft">Stewardship &amp; Excellence</div></div>
      <div><div class="fn">04</div><div class="ft">Relationships &amp; Culture</div></div>
      <div><div class="fn">05</div><div class="ft">Legacy &amp; Kingdom Impact</div></div>
    </div>
  </div>
</section>

<section class="toc">
  <div class="wrap">
    <h2>The Twenty Channels</h2>
    <ul>{toc_html}</ul>
  </div>
</section>

<div class="wrap">
  {cat_blocks}
</div>

<footer>
  <div class="mark">LifeTogether</div>
  <div class="tag">Twenty-five years. Five hundred churches. Twenty new marketplace channels.</div>
</footer>

</body>
</html>
"""

with open("/mnt/user-data/outputs/lifetogether-20-new-categories-brochure.html", "w") as f:
    f.write(HTML)

print("Categories:", len(new_cats), "| Campaigns:", total_campaigns)
