# -*- coding: utf-8 -*-
import csv, html as H
from collections import OrderedDict, defaultdict
from original20 import (TITLE_ONLY_CATEGORIES, EXAMPLE_CATEGORIES, SUBTITLED_25_CATEGORIES,
                         EXAMPLE_WITH_SUBTITLE_CATEGORIES)
from flourishing import FLOURISHING_WEEKS, FLOURISHING_WORKPLACE_SERIES

def esc(s):
    return H.escape(s, quote=False)

def slug(s):
    return "".join(c if c.isalnum() else "-" for c in s.lower()).strip("-")

SECTIONS = ["Calling & Purpose", "Leadership & Character", "Stewardship & Excellence",
            "Relationships & Culture", "Legacy & Kingdom Impact"]

# ---- Load the 20 new categories from the authoritative campaigns.csv ----
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

# ================= RENDER HELPERS =================

def render_directory_list(titles_only):
    items = "\n".join(
        f'<li class="d-item plain"><span class="d-num">{i+1:02d}</span>'
        f'<span class="d-title">{esc(t)}</span></li>'
        for i, t in enumerate(titles_only)
    )
    return f'<ul class="d-grid three-col">{items}</ul>'

def render_ts_list(pairs, start=1):
    return "\n".join(
        f'<li class="d-item"><span class="d-num">{i:02d}</span>'
        f'<span class="d-text"><span class="d-title">{esc(t)}</span>'
        f'<span class="d-sub">{esc(s)}</span></span></li>'
        for i, (t, s) in enumerate(pairs, start=start)
    )

def cat_section(name, blurb, meta, body_html, group_label, badge=""):
    # NOTE: group_label and meta are trusted, code-authored strings that intentionally
    # contain HTML entities (e.g. &middot;, &times;) -- they must NOT be re-escaped.
    return f"""
<section class="cat-block" id="{slug(name)}">
  <div class="cat-head">
    <span class="cat-eyebrow">{group_label}</span>
    <h2>{esc(name)}{badge}</h2>
    <p class="cat-blurb">{esc(blurb)}</p>
    <p class="cat-meta">{meta}</p>
  </div>
  {body_html}
</section>
"""

# ---- 1) Title-only founding categories (1-3) ----
title_only_html = ""
for name, blurb, titles in TITLE_ONLY_CATEGORIES:
    title_only_html += cat_section(
        name, blurb, f"{len(titles)} flagship titles &middot; founding collection",
        render_directory_list(titles), "Founding Collection"
    )

# ---- 2) Example categories (10 each, title only, awaiting full 50-title build-out) ----
example_html = ""
for name, blurb, examples in EXAMPLE_CATEGORIES:
    example_html += cat_section(
        name, blurb,
        f"{len(examples)} of 50 shown &middot; full expansion follows the shared 5-section framework",
        render_directory_list(examples), "Original Channel &middot; Awaiting Full Expansion"
    )

# ---- 3) Example categories WITH subtitle + expand note (10 each) ----
example_sub_html = ""
for name, pairs, expand_note in EXAMPLE_WITH_SUBTITLE_CATEGORIES:
    body = f'<ul class="d-grid">{render_ts_list(pairs)}</ul>'
    body += f'<p class="expand-note"><strong>To expand into:</strong> {esc(expand_note)}</p>'
    example_sub_html += cat_section(
        name, "", f"{len(pairs)} of 50 shown &middot; full expansion follows the shared 5-section framework",
        body, "Original Channel &middot; Awaiting Full Expansion"
    )

# ---- 4) The two 25-title categories (Manufacturing, Marketplace Ministry) ----
sub25_html = ""
for name, blurb, pairs in SUBTITLED_25_CATEGORIES:
    sub25_html += cat_section(
        name, blurb, f"{len(pairs)} of 50 shown &middot; the founding twenty-five",
        f'<ul class="d-grid">{render_ts_list(pairs)}</ul>', "Original Channel &middot; Founding 25 of 50"
    )

# ---- 5) The 20 new categories (full 50, from campaigns.csv) ----
new_html = ""
for name, sections in new_cats.items():
    blocks = []
    for sec_name in SECTIONS:
        pairs = sections[sec_name]
        blocks.append(f"""
    <div class="sub-block">
      <h3 class="sub-head">{esc(sec_name)}</h3>
      <ul class="d-grid">{render_ts_list(pairs)}</ul>
    </div>""")
    body = "".join(blocks)
    new_html += cat_section(
        name, NEW_CATEGORY_BLURBS.get(name, ""),
        "50 flagship campaigns &middot; 5 sections &times; 10 titles",
        body, "New Vertical &middot; Business &amp; Workplace Intelligence\u2122"
    )

# ---- 6) Flourishing Workplace (6-criteria featured category) ----
week_chips = "".join(
    f'<div class="week-chip"><span class="week-num">WK {i+1}</span>'
    f'<span class="week-name">{esc(w)}</span></div>'
    for i, (w, d) in enumerate(FLOURISHING_WEEKS)
)
week_desc = "".join(
    f'<li class="d-item plain"><span class="d-num">{i+1:02d}</span>'
    f'<span class="d-text"><span class="d-title">{esc(w)}</span>'
    f'<span class="d-sub">{esc(d)}</span></span></li>'
    for i, (w, d) in enumerate(FLOURISHING_WEEKS)
)
flourishing_html = f"""
<section class="cat-block featured" id="flourishing-workplace">
  <div class="cat-head">
    <span class="cat-eyebrow">Featured Category &middot; The Flourishing Framework, Applied to Work</span>
    <h2>Flourishing Workplace <span class="badge gold">6-Criteria Series</span></h2>
    <p class="cat-blurb">Every series in this category shares LifeTogether's proven six-week Flourishing
       backbone, reapplied to the workplace.</p>
  </div>
  <div class="criteria-box">
    <div class="label">The Shared Six-Week Framework</div>
    <div class="week-row">{week_chips}</div>
    <ul class="d-grid" style="margin-top:22px;">{week_desc}</ul>
  </div>
  <div class="sub-block">
    <h3 class="sub-head">The Flourishing Workplace Series</h3>
    <ul class="d-grid">{render_ts_list(FLOURISHING_WORKPLACE_SERIES)}</ul>
  </div>
</section>
"""

# ---- 7) Purpose Based Business (already laid out as its own brochure; embedded here for the master directory) ----
PURPOSE_WEEKS = [
    ("Worship", "Work as Worship", "Discovering God's presence in the ordinary work of business — where excellence, not just Sunday, becomes an offering."),
    ("Fellowship", "Team as Family", "Building a culture of authentic belonging, where colleagues become companions rather than just coworkers."),
    ("Discipleship", "Growing Leaders, Not Just Employees", "Developing character alongside competence, so people leave better than they arrived."),
    ("Ministry", "Serving Through Your Business", "Using the gifts of the company — products, profits, and people — to bless customers and community."),
    ("Mission", "Business on Mission", "Carrying Kingdom purpose beyond the walls of the company — into the marketplace, the city, and the world."),
]
purpose_weeks_html = "".join(
    f'<div class="purpose-card"><span class="purpose-num">{i+1:02d}</span>'
    f'<span class="purpose-name">{esc(purpose)}</span>'
    f'<span class="purpose-title">{esc(title)}</span>'
    f'<span class="purpose-desc">{esc(desc)}</span></div>'
    for i, (purpose, title, desc) in enumerate(PURPOSE_WEEKS)
)
purpose_html = f"""
<section class="cat-block featured purpose-page" id="purpose-based-business">
  <div class="purpose-hero">
    <span class="cat-eyebrow">Featured Category &middot; Not Yet Expanded</span>
    <h2>Purpose Based Business</h2>
    <p class="purpose-deck">Every LifeTogether churchwide campaign is built on five biblical purposes —
       Worship, Fellowship, Discipleship, Ministry, and Mission. Purpose Based Business carries that same
       architecture into the workplace: five weeks, five purposes, one company learning to see its ordinary
       work as an extension of God's Kingdom.</p>
  </div>
  <div class="purpose-framework">
    <div class="label">Five Weeks. Five Purposes. One Company on Mission.</div>
    <div class="purpose-grid">{purpose_weeks_html}</div>
  </div>
  <div class="sub-block">
    <h3 class="sub-head">Purpose Built &mdash; Early Themes</h3>
    <p class="theme-note">This is the purpose-built theme layer only &mdash; the weekly architecture, not yet
       expanded into full session content, discussion guides, or campaign variants. A dedicated brochure for
       this category has also been laid out separately (<em>purpose-based-business-brochure.html</em>).</p>
  </div>
</section>
"""

# ================= TOC =================
toc_order = []
toc_order += [n for n, *_ in TITLE_ONLY_CATEGORIES]
toc_order += [n for n, *_ in EXAMPLE_CATEGORIES]
toc_order += [n for n, *_ in EXAMPLE_WITH_SUBTITLE_CATEGORIES]
toc_order += [n for n, *_ in SUBTITLED_25_CATEGORIES]
toc_order += list(new_cats.keys())

toc_html = "\n".join(
    f'<li><a href="#{slug(n)}"><span class="toc-num">{i+1:02d}</span>{esc(n)}</a></li>'
    for i, n in enumerate(toc_order)
)
toc_html += '<li class="toc-featured"><a href="#flourishing-workplace"><span class="toc-num">&#9733;</span>Flourishing Workplace</a></li>'
toc_html += '<li class="toc-featured"><a href="#purpose-based-business"><span class="toc-num">&#9733;</span>Purpose Based Business</a></li>'

# ================= TOTALS =================
def count_pairs(lst):
    return len(lst)

total = 0
total += sum(len(t) for _, _, t in TITLE_ONLY_CATEGORIES)
total += sum(len(e) for _, _, e in EXAMPLE_CATEGORIES)
total += sum(len(p) for _, p, _ in EXAMPLE_WITH_SUBTITLE_CATEGORIES)
total += sum(len(p) for _, _, p in SUBTITLED_25_CATEGORIES)
total += sum(sum(len(v) for v in sec.values()) for sec in new_cats.values())
total_categories = 20 + len(new_cats)

# ================= CSS (matches the established Purpose-Based Business brochure design system) =================
CSS = """
:root{
  --navy:#101a33; --navy-2:#16223f;
  --gold:#b8934e; --gold-light:#d9bc82;
  --cream:#f7f3ea; --hair:rgba(184,147,78,.35);
  --muted:rgba(247,243,234,.82); --muted2:rgba(247,243,234,.6);
  --ink-bright:#fbf7ee;
}
*{box-sizing:border-box;}
html{scroll-behavior:smooth;}
body{margin:0; background:var(--navy); color:var(--cream); font-family:'Cormorant Garamond',serif; font-size:17px;}
h1,h2,h3{font-family:'Playfair Display',serif; margin:0; font-weight:600; color:var(--ink-bright);}
a{color:var(--gold-light); text-decoration:none;}
.wrap{max-width:1180px; margin:0 auto; padding:0 28px;}

/* HERO */
.hero{padding:100px 0 60px; text-align:center; border-bottom:1px solid var(--hair);}
.hero .eyebrow{font-family:'Cormorant Garamond',serif; letter-spacing:.32em; text-transform:uppercase;
  font-size:13px; color:var(--gold-light);}
.hero h1{font-family:'Playfair Display',serif; font-weight:600; font-size:clamp(2.2rem,5vw,3.6rem);
  margin:20px 0 14px; line-height:1.15; color:var(--ink-bright);}
.hero .subtitle{font-style:italic; font-size:1.25rem; color:var(--gold-light); margin-bottom:8px;}
.rule{width:120px; height:1px; background:var(--gold); margin:26px auto; opacity:.7;}
.hero p.deck{max-width:680px; margin:0 auto; color:var(--cream); font-size:1.1rem; line-height:1.7;}
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
@media(min-width:760px){.toc ul{column-count:3;}}
.toc li{break-inside:avoid; margin-bottom:9px; font-size:.92rem; border-bottom:1px dotted var(--hair); padding-bottom:7px;}
.toc a{color:var(--cream); display:flex; gap:10px;}
.toc a:hover{color:var(--gold-light);}
.toc-num{color:var(--gold-light); font-variant-numeric:tabular-nums; min-width:22px;}
.toc-featured a{color:var(--gold-light); font-style:italic; font-size:1.02rem;}

/* CATEGORY BLOCKS */
.cat-block{padding:52px 0; border-bottom:1px solid var(--hair);}
.cat-block:nth-of-type(even){background:rgba(255,255,255,.02);}
.cat-head{margin-bottom:26px;}
.cat-eyebrow{font-style:italic; letter-spacing:.06em; color:var(--gold-light); font-size:.95rem;}
.cat-head h2{font-size:1.85rem; margin-top:8px;}
.cat-blurb{color:var(--cream); font-size:1.02rem; margin-top:8px; max-width:640px;}
.cat-meta{font-family:'Lato',sans-serif; color:var(--muted2); font-size:.78rem; margin-top:6px; letter-spacing:.03em;}
.expand-note{font-family:'Lato',sans-serif; color:var(--muted); font-size:.85rem; margin-top:18px; font-style:italic;}
.badge{display:inline-block; font-family:'Lato',sans-serif; font-size:.6rem; letter-spacing:.1em;
  text-transform:uppercase; border:1px solid var(--gold); color:var(--gold-light); padding:3px 9px;
  border-radius:20px; vertical-align:middle; margin-left:10px;}
.badge.gold{background:rgba(184,147,78,.16);}

.sub-block{margin-top:28px;}
.sub-head{font-size:1.05rem; color:var(--gold-light); margin-bottom:14px; padding-bottom:8px;
  border-bottom:1px solid var(--hair); font-family:'Playfair Display',serif;}

.d-grid{list-style:none; margin:0; padding:0; display:grid; grid-template-columns:1fr 1fr; gap:0 32px;}
.d-grid.three-col{grid-template-columns:1fr 1fr 1fr;}
@media(max-width:720px){.d-grid, .d-grid.three-col{grid-template-columns:1fr;}}
.d-item{display:flex; gap:12px; padding:8px 0; border-bottom:1px solid rgba(255,255,255,.07);}
.d-item.plain{align-items:baseline;}
.d-num{font-family:'Lato',sans-serif; color:var(--gold-light); font-size:.76rem; padding-top:3px; min-width:20px;}
.d-text{display:flex; flex-direction:column;}
.d-title{font-family:'Lato',sans-serif; font-weight:700; font-size:.95rem; color:var(--ink-bright);}
.d-sub{font-style:italic; color:var(--muted); font-size:.94rem; margin-top:1px;}

/* FLOURISHING FEATURED */
.featured{background:linear-gradient(180deg, rgba(184,147,78,.08), transparent 40%);}
.criteria-box{border:1px solid var(--gold); border-radius:6px; padding:24px 26px; margin:24px 0 8px; background:rgba(184,147,78,.07);}
.criteria-box .label{font-family:'Lato',sans-serif; font-size:.7rem; letter-spacing:.14em; text-transform:uppercase; color:var(--gold-light); margin-bottom:14px;}
.week-row{display:flex; flex-wrap:wrap; gap:10px;}
.week-chip{border:1px solid var(--hair); border-radius:20px; padding:6px 14px; display:flex; gap:8px; align-items:baseline; font-family:'Lato',sans-serif; font-size:.8rem;}
.week-chip .week-num{color:var(--gold-light); font-size:.66rem; letter-spacing:.06em;}

/* PURPOSE BASED BUSINESS PAGE */
.purpose-page{background:radial-gradient(ellipse at 50% 0%, rgba(184,147,78,.1), transparent 55%);}
.purpose-hero{text-align:center; max-width:720px; margin:0 auto 36px;}
.purpose-hero h2{font-size:2.2rem; margin:14px 0;}
.purpose-deck{color:var(--cream); font-size:1.05rem; line-height:1.7;}
.purpose-framework{border-top:1px solid var(--hair); border-bottom:1px solid var(--hair); padding:32px 0; margin:20px 0 36px;}
.purpose-framework .label{text-align:center; font-family:'Playfair Display',serif; font-style:italic; font-size:1.3rem; color:var(--ink-bright); margin-bottom:26px;}
.purpose-grid{display:grid; grid-template-columns:repeat(5,1fr); gap:14px;}
@media(max-width:900px){.purpose-grid{grid-template-columns:repeat(2,1fr);}}
.purpose-card{border:1px solid var(--gold); border-radius:6px; padding:20px 14px; text-align:center; background:rgba(184,147,78,.06);}
.purpose-card .purpose-num{display:block; font-family:'Playfair Display',serif; font-size:1.4rem; color:var(--gold-light);}
.purpose-card .purpose-name{display:block; font-family:'Lato',sans-serif; text-transform:uppercase; letter-spacing:.1em; font-size:.68rem; color:var(--gold-light); margin:8px 0 6px;}
.purpose-card .purpose-title{display:block; font-family:'Playfair Display',serif; font-weight:600; font-size:1.02rem; color:var(--ink-bright);}
.purpose-card .purpose-desc{display:block; font-style:italic; color:var(--muted); font-size:.85rem; margin-top:6px;}
.theme-note{font-family:'Lato',sans-serif; color:var(--muted); font-size:.88rem; font-style:italic; line-height:1.6;}

footer{padding:56px 0 80px; text-align:center; color:var(--muted2); font-family:'Lato',sans-serif; font-size:.8rem;}
footer .mark{font-family:'Playfair Display',serif; font-size:.85rem; letter-spacing:.28em; text-transform:uppercase; color:var(--gold-light);}
"""

HTML = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>LifeTogether Workplace Intelligence&trade; &mdash; Master Directory</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,500;0,600;0,700;1,500&family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;1,400&family=Lato:wght@400;700&display=swap" rel="stylesheet">
<style>{CSS}</style>
</head>
<body>

<section class="hero">
  <div class="wrap">
    <span class="eyebrow">LifeTogether Ministries</span>
    <h1>Business &amp; Workplace Intelligence&trade;</h1>
    <div class="subtitle">The Master Directory</div>
    <div class="rule"></div>
    <p class="deck">One unified directory joining the original channel architecture with twenty new
       professional verticals &mdash; every category built on the same five-part framework, so the library
       scales without losing coherence.</p>
    <div class="stat-bar">
      <div class="stat"><div class="n">{total_categories}</div><div class="l">Categories</div></div>
      <div class="stat"><div class="n">{total:,}+</div><div class="l">Flagship Campaigns Shown</div></div>
      <div class="stat"><div class="n">5</div><div class="l">Sections per Category</div></div>
      <div class="stat"><div class="n">2</div><div class="l">Featured Frameworks</div></div>
    </div>
  </div>
</section>

<section class="framework">
  <div class="wrap">
    <h2>One Framework, Every Vertical</h2>
    <p class="sub">Every new and fully expanded category in this directory is built on the same
       five-section, fifty-title architecture.</p>
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
    <h2>Directory Index</h2>
    <ul>{toc_html}</ul>
  </div>
</section>

<div class="wrap">
  {title_only_html}
  {example_html}
  {example_sub_html}
  {sub25_html}
  {new_html}
  {flourishing_html}
  {purpose_html}
</div>

<footer>
  <div class="mark">LifeTogether</div>
  <div style="margin-top:10px;">Business &amp; Workplace Intelligence&trade; Master Directory &middot;
  {total_categories} categories &middot; {total:,}+ campaigns shown &middot; internal working document</div>
</footer>

</body>
</html>
"""

with open("/mnt/user-data/outputs/lifetogether-workplace-intelligence-master-directory.html", "w") as f:
    f.write(HTML)

print("Categories:", total_categories, "| Campaigns shown:", total)
