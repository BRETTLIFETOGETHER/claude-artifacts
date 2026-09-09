# -*- coding: utf-8 -*-
import html as h
from data import (get_all_categories, SECTIONS, FLOURISHING_WEEKS, FLOURISHING_WORKPLACE_SERIES,
                   PURPOSE_WEEKS, PURPOSE_BASED_BUSINESS_THEMES, NEW_CATEGORIES, ORIGINAL_EXPAND)
from complete_originals import COMPLETE_ORIGINALS

def esc(s):
    return h.escape(s, quote=False)

def slugify(s):
    return "".join(c if c.isalnum() else "-" for c in s.lower()).strip("-")

cats = get_all_categories()
new_cat_names = set(NEW_CATEGORIES.keys())

# Split cats into: original-expanded sectioned (excluding manufacturing/marketplace), flat50 ones, and truly-new sectioned
original_sectioned = [c for c in cats if c[1] == "sectioned" and c[0] in ORIGINAL_EXPAND]
flat_cats = [c for c in cats if c[1] == "flat50"]
new_sectioned = [c for c in cats if c[1] == "sectioned" and c[0] in new_cat_names]

TOTAL_CAMPAIGNS = 150  # categories 1-3
for _, kind, payload in cats:
    TOTAL_CAMPAIGNS += (sum(len(v) for v in payload.values()) if kind == "sectioned" else len(payload))

TOTAL_CATEGORIES = 3 + len(cats)

# ---------------------------------------------------------------- HTML PIECES

def render_directory_only(name, titles, group_label):
    slug = slugify(name)
    items = "\n".join(
        f'<li class="d-item plain"><span class="d-num">{i+1:02d}</span><span class="d-title">{esc(t)}</span></li>'
        for i, t in enumerate(titles)
    )
    return f"""
<section class="cat-block" id="{slug}">
  <div class="cat-head">
    <span class="cat-eyebrow">{esc(group_label)}</span>
    <h2>{esc(name)}</h2>
    <p class="cat-meta">{len(titles)} flagship titles &middot; foundational collection</p>
  </div>
  <ul class="d-grid three-col">
    {items}
  </ul>
</section>
"""

def render_sectioned(name, sections_dict, group_label, badge=None):
    slug = slugify(name)
    blocks = []
    for sec_name in SECTIONS:
        entries = sections_dict[sec_name]
        items = "\n".join(
            f'<li class="d-item"><span class="d-num">{i+1:02d}</span>'
            f'<span class="d-text"><span class="d-title">{esc(t)}</span>'
            f'<span class="d-sub">{esc(s)}</span></span></li>'
            for i, (t, s) in enumerate(entries)
        )
        blocks.append(f"""
    <div class="sub-block">
      <h3 class="sub-head">{esc(sec_name)}</h3>
      <ul class="d-grid">
        {items}
      </ul>
    </div>""")
    badge_html = f'<span class="badge">{esc(badge)}</span>' if badge else ""
    return f"""
<section class="cat-block" id="{slug}">
  <div class="cat-head">
    <span class="cat-eyebrow">{esc(group_label)}</span>
    <h2>{esc(name)} {badge_html}</h2>
    <p class="cat-meta">50 flagship campaigns &middot; 5 sections &times; 10 titles</p>
  </div>
  {"".join(blocks)}
</section>
"""

def render_flat50(name, titles, group_label):
    slug = slugify(name)
    founding = titles[:25]
    expansion = titles[25:]
    f_items = "\n".join(
        f'<li class="d-item"><span class="d-num">{i+1:02d}</span>'
        f'<span class="d-text"><span class="d-title">{esc(t)}</span>'
        f'<span class="d-sub">{esc(s)}</span></span></li>'
        for i, (t, s) in enumerate(founding)
    )
    e_items = "\n".join(
        f'<li class="d-item"><span class="d-num">{i+26:02d}</span>'
        f'<span class="d-text"><span class="d-title">{esc(t)}</span>'
        f'<span class="d-sub">{esc(s)}</span></span></li>'
        for i, (t, s) in enumerate(expansion)
    )
    return f"""
<section class="cat-block" id="{slug}">
  <div class="cat-head">
    <span class="cat-eyebrow">{esc(group_label)}</span>
    <h2>{esc(name)}</h2>
    <p class="cat-meta">50 flagship campaigns &middot; founding 25 + expansion 25</p>
  </div>
  <div class="sub-block">
    <h3 class="sub-head">The Founding Twenty-Five</h3>
    <ul class="d-grid">{f_items}</ul>
  </div>
  <div class="sub-block">
    <h3 class="sub-head">The Expansion Twenty-Five</h3>
    <ul class="d-grid">{e_items}</ul>
  </div>
</section>
"""

# ---------------------------------------------------------------- TOC
toc_entries = [name for name, _ in COMPLETE_ORIGINALS]
toc_entries += [name for name, _, _ in original_sectioned]
toc_entries += [name for name, _, _ in flat_cats]
toc_entries += [name for name, _, _ in new_sectioned]
toc_html = "\n".join(
    f'<li><a href="#{slugify(n)}"><span class="toc-num">{i+1:02d}</span>{esc(n)}</a></li>'
    for i, n in enumerate(toc_entries)
)
toc_html += f'<li class="toc-featured"><a href="#flourishing-workplace"><span class="toc-num">&#9733;</span>Flourishing Workplace</a></li>'
toc_html += f'<li class="toc-featured"><a href="#purpose-based-business"><span class="toc-num">&#9733;</span>Purpose Based Business</a></li>'

# ---------------------------------------------------------------- ORIGINAL 3
originals_html = "".join(
    render_directory_only(name, titles, "Founding Collection")
    for name, titles in COMPLETE_ORIGINALS
)

# ---------------------------------------------------------------- 16 EXPANDED ORIGINALS
expanded_html = "".join(
    render_sectioned(name, payload, "Business & Workplace Intelligence\u2122 &middot; Expanded to 50")
    for name, kind, payload in original_sectioned
)

# ---------------------------------------------------------------- FLAT 50s (Manufacturing, Marketplace Ministry)
flat_html = "".join(
    render_flat50(name, payload, "Business & Workplace Intelligence\u2122 &middot; Expanded to 50")
    for name, kind, payload in flat_cats
)

# ---------------------------------------------------------------- 20 NEW CATEGORIES
new_html = "".join(
    render_sectioned(name, payload, "New Vertical &middot; Business & Workplace Intelligence\u2122")
    for name, kind, payload in new_sectioned
)

# ---------------------------------------------------------------- FLOURISHING WORKPLACE
weeks_html = "".join(
    f'<div class="week-chip"><span class="week-num">WK {i+1}</span><span class="week-name">{esc(w)}</span></div>'
    for i, w in enumerate(FLOURISHING_WEEKS)
)
flourishing_items = "\n".join(
    f'<li class="d-item"><span class="d-num">{i+1:02d}</span>'
    f'<span class="d-text"><span class="d-title">{esc(t)}</span>'
    f'<span class="d-sub">{esc(s)}</span></span></li>'
    for i, (t, s) in enumerate(FLOURISHING_WORKPLACE_SERIES)
)
flourishing_html = f"""
<section class="cat-block featured" id="flourishing-workplace">
  <div class="cat-head">
    <span class="cat-eyebrow">Featured Category &middot; The Flourishing Framework, Applied to Work</span>
    <h2>Flourishing Workplace <span class="badge gold">6-Criteria Series</span></h2>
    <p class="cat-meta">Every series in this category shares the same six-week backbone &mdash; the proven
       Flourishing framework, reapplied to the workplace.</p>
  </div>
  <div class="criteria-box">
    <div class="label">The Shared Six-Week Framework</div>
    <div class="week-row">{weeks_html}</div>
    <p>Rather than inventing a new structure per title, every Flourishing Workplace series walks the same six
       dimensions &mdash; vertical (with God), relational (together), interior (from within), vocational
       (through contribution), outward (for others), and generational (across generations) &mdash; spoken in
       the language of work.</p>
  </div>
  <div class="sub-block">
    <h3 class="sub-head">The Flourishing Workplace Series</h3>
    <ul class="d-grid">{flourishing_items}</ul>
  </div>
</section>
"""

# ---------------------------------------------------------------- PURPOSE BASED BUSINESS (full brochure layout)
purpose_weeks_html = "".join(
    f'<div class="purpose-card"><span class="purpose-num">{i+1}</span>'
    f'<span class="purpose-name">{esc(name)}</span><span class="purpose-desc">{esc(desc)}</span></div>'
    for i, (name, desc) in enumerate(PURPOSE_WEEKS)
)
theme_items = "\n".join(
    f'<li class="d-item"><span class="d-num">{i+1:02d}</span>'
    f'<span class="d-text"><span class="d-title">{esc(t)}</span>'
    f'<span class="d-sub">{esc(s)}</span></span></li>'
    for i, (t, s) in enumerate(PURPOSE_BASED_BUSINESS_THEMES)
)
purpose_html = f"""
<section class="cat-block featured purpose-page" id="purpose-based-business">
  <div class="purpose-hero">
    <span class="cat-eyebrow">Featured Category &middot; Not Yet Expanded</span>
    <h2>Purpose Based Business</h2>
    <p class="purpose-deck">One unifying framework, reused &mdash; the same five biblical purposes that
       anchor the Biblical Purpose Library, now spoken in the language of ownership, leadership, and the
       marketplace. Five purposes. One weekly rhythm for every business series.</p>
  </div>

  <div class="purpose-framework">
    <div class="label">The Weekly Framework &mdash; Five Purposes, Five Weeks</div>
    <div class="purpose-grid">{purpose_weeks_html}</div>
    <p class="framework-note">Every Purpose Based Business series &mdash; regardless of audience or
       industry &mdash; will be built on this same five-week backbone: Worship, Fellowship, Discipleship,
       Ministry, and Mission, translated into the language of running a company.</p>
  </div>

  <div class="sub-block">
    <h3 class="sub-head">Purpose Built &mdash; Early Themes</h3>
    <p class="theme-note">Not yet expanded into full campaigns. These are directional themes only, each
       waiting to be built out on the five-purpose weekly framework above.</p>
    <ul class="d-grid">{theme_items}</ul>
  </div>
</section>
"""

# ---------------------------------------------------------------- FULL PAGE
CSS = """
:root{
  --navy:#0a1424; --navy2:#0f1d33; --navy3:#13233d;
  --gold:#c9a24c; --gold-light:#e6cd8a;
  --cream:#f3ecdd; --muted:rgba(243,236,221,.62); --muted2:rgba(243,236,221,.4);
  --rule:rgba(201,162,76,.25);
}
*{box-sizing:border-box;}
html{scroll-behavior:smooth;}
body{
  margin:0; background:var(--navy); color:var(--cream);
  font-family:'Lato',sans-serif; font-size:16px; line-height:1.5;
}
h1,h2,h3{font-family:'Playfair Display',serif; margin:0; font-weight:700;}
em, .em{font-family:'Cormorant Garamond',serif; font-style:italic;}
a{color:var(--gold-light); text-decoration:none;}
.wrap{max-width:1100px; margin:0 auto; padding:0 28px;}

/* HERO */
.hero{padding:96px 0 64px; text-align:center; border-bottom:1px solid var(--rule);
  background:radial-gradient(ellipse at 50% -10%, rgba(201,162,76,.14), transparent 60%);}
.hero .eyebrow{font-family:'Cormorant Garamond',serif; font-style:italic; color:var(--gold-light);
  font-size:1.15rem; letter-spacing:.04em;}
.hero h1{font-size:clamp(2.4rem,5vw,4.2rem); margin:18px 0 20px; line-height:1.08;}
.hero h1 em{color:var(--gold-light); font-style:italic;}
.hero p.deck{max-width:680px; margin:0 auto; color:var(--muted); font-size:1.15rem;}
.stat-bar{display:flex; justify-content:center; gap:56px; margin-top:48px; flex-wrap:wrap;}
.stat{text-align:center;}
.stat .n{font-family:'Playfair Display',serif; font-size:2.2rem; color:var(--gold-light);}
.stat .l{font-size:.78rem; letter-spacing:.12em; text-transform:uppercase; color:var(--muted2);}

/* FRAMEWORK EXPLAINER */
.framework{padding:64px 0; border-bottom:1px solid var(--rule); background:var(--navy2);}
.framework h2{font-size:1.9rem; text-align:center; margin-bottom:10px;}
.framework .sub{text-align:center; color:var(--muted); max-width:640px; margin:0 auto 36px;}
.framework-cols{display:grid; grid-template-columns:repeat(5,1fr); gap:18px;}
.framework-cols div{border:1px solid var(--rule); border-radius:4px; padding:18px 14px; text-align:center;}
.framework-cols .fn{font-family:'Playfair Display',serif; color:var(--gold-light); font-size:1.4rem;}
.framework-cols .ft{font-size:.85rem; margin-top:8px; color:var(--muted);}

/* TOC */
.toc{padding:56px 0; border-bottom:1px solid var(--rule);}
.toc h2{font-size:1.6rem; margin-bottom:24px; text-align:center;}
.toc ul{list-style:none; margin:0; padding:0; column-count:2; column-gap:40px;}
@media(min-width:760px){.toc ul{column-count:3;}}
.toc li{break-inside:avoid; margin-bottom:10px; font-size:.92rem; border-bottom:1px dotted var(--rule); padding-bottom:8px;}
.toc a{color:var(--cream); display:flex; gap:10px;}
.toc a:hover{color:var(--gold-light);}
.toc-num{color:var(--gold); font-variant-numeric:tabular-nums; min-width:22px;}
.toc-featured a{color:var(--gold-light); font-family:'Cormorant Garamond',serif; font-style:italic; font-size:1.05rem;}

/* CATEGORY BLOCKS */
.cat-block{padding:56px 0; border-bottom:1px solid var(--rule);}
.cat-block:nth-of-type(even){background:rgba(255,255,255,.012);}
.cat-head{margin-bottom:28px;}
.cat-eyebrow{font-family:'Cormorant Garamond',serif; font-style:italic; color:var(--gold-light); font-size:1rem;}
.cat-head h2{font-size:2rem; margin-top:8px;}
.cat-meta{color:var(--muted); font-size:.88rem; margin-top:6px;}
.badge{display:inline-block; font-family:'Lato',sans-serif; font-size:.62rem; letter-spacing:.1em;
  text-transform:uppercase; border:1px solid var(--gold); color:var(--gold-light); padding:3px 9px;
  border-radius:20px; vertical-align:middle; margin-left:10px;}
.badge.gold{background:rgba(201,162,76,.14);}

.sub-block{margin-top:30px;}
.sub-head{font-size:1.05rem; color:var(--gold-light); letter-spacing:.02em; margin-bottom:14px;
  padding-bottom:8px; border-bottom:1px solid var(--rule); font-family:'Playfair Display',serif;}

.d-grid{list-style:none; margin:0; padding:0; display:grid; grid-template-columns:1fr 1fr; gap:0 32px;}
.d-grid.three-col{grid-template-columns:1fr 1fr 1fr;}
@media(max-width:720px){.d-grid, .d-grid.three-col{grid-template-columns:1fr;}}
.d-item{display:flex; gap:12px; padding:9px 0; border-bottom:1px solid rgba(255,255,255,.05);}
.d-item.plain{align-items:baseline;}
.d-num{color:var(--gold); font-size:.78rem; font-variant-numeric:tabular-nums; padding-top:2px; min-width:20px;}
.d-text{display:flex; flex-direction:column;}
.d-title{font-weight:700; font-size:.96rem;}
.d-sub{font-family:'Cormorant Garamond',serif; font-style:italic; color:var(--muted); font-size:.92rem; margin-top:1px;}

/* FLOURISHING / FEATURED */
.featured{background:linear-gradient(180deg, rgba(201,162,76,.06), transparent 40%);}
.criteria-box{border:1px solid var(--gold); border-radius:6px; padding:24px 26px; margin:24px 0 8px; background:rgba(201,162,76,.05);}
.criteria-box .label{font-size:.72rem; letter-spacing:.14em; text-transform:uppercase; color:var(--gold-light); margin-bottom:14px;}
.criteria-box p{color:var(--muted); font-size:.94rem; margin:12px 0 0;}
.week-row{display:flex; flex-wrap:wrap; gap:10px;}
.week-chip{border:1px solid var(--rule); border-radius:20px; padding:6px 14px; display:flex; gap:8px; align-items:baseline; font-size:.82rem;}
.week-chip .week-num{color:var(--gold); font-size:.68rem; letter-spacing:.06em;}

/* PURPOSE BASED BUSINESS PAGE */
.purpose-page{background:radial-gradient(ellipse at 50% 0%, rgba(201,162,76,.1), transparent 55%);}
.purpose-hero{text-align:center; max-width:720px; margin:0 auto 40px;}
.purpose-hero h2{font-size:2.4rem; margin:14px 0;}
.purpose-deck{color:var(--muted); font-size:1.05rem;}
.purpose-framework{border-top:1px solid var(--rule); border-bottom:1px solid var(--rule); padding:36px 0; margin:20px 0 40px;}
.purpose-framework .label{text-align:center; font-size:.75rem; letter-spacing:.14em; text-transform:uppercase; color:var(--gold-light); margin-bottom:26px;}
.purpose-grid{display:grid; grid-template-columns:repeat(5,1fr); gap:14px;}
@media(max-width:900px){.purpose-grid{grid-template-columns:repeat(2,1fr);}}
.purpose-card{border:1px solid var(--gold); border-radius:6px; padding:20px 14px; text-align:center; background:rgba(201,162,76,.04);}
.purpose-card .purpose-num{display:block; font-family:'Playfair Display',serif; font-size:1.6rem; color:var(--gold-light);}
.purpose-card .purpose-name{display:block; font-family:'Playfair Display',serif; font-weight:700; margin:8px 0 6px; font-size:1.05rem;}
.purpose-card .purpose-desc{display:block; font-family:'Cormorant Garamond',serif; font-style:italic; color:var(--muted); font-size:.88rem;}
.framework-note{text-align:center; color:var(--muted); max-width:600px; margin:22px auto 0; font-size:.92rem;}
.theme-note{color:var(--muted); font-size:.9rem; margin-bottom:16px;}

footer{padding:56px 0 80px; text-align:center; color:var(--muted2); font-size:.82rem;}
"""

HTML = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>LifeTogether Workplace Intelligence&trade; &mdash; Master Directory</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@600;700;800&family=Cormorant+Garamond:ital,wght@0,500;1,500;1,600&family=Lato:wght@400;700&display=swap" rel="stylesheet">
<style>{CSS}</style>
</head>
<body>

<section class="hero">
  <div class="wrap">
    <span class="eyebrow">LifeTogether Ministries &middot; Business &amp; Workplace Intelligence&trade;</span>
    <h1>The Master Directory<br><em>Every Vertical, One Framework</em></h1>
    <p class="deck">Forty workplace verticals. One shared five-part architecture. A single library built to
       meet Christians in every profession &mdash; from the exam room to the factory floor to the boardroom
       &mdash; with the same rigor as LifeTogether's church and family libraries.</p>
    <div class="stat-bar">
      <div class="stat"><div class="n">{TOTAL_CATEGORIES}</div><div class="l">Categories</div></div>
      <div class="stat"><div class="n">{TOTAL_CAMPAIGNS:,}+</div><div class="l">Flagship Campaigns</div></div>
      <div class="stat"><div class="n">5</div><div class="l">Sections per Category</div></div>
      <div class="stat"><div class="n">2</div><div class="l">Featured Frameworks</div></div>
    </div>
  </div>
</section>

<section class="framework">
  <div class="wrap">
    <h2>One Framework, Every Vertical</h2>
    <p class="sub">Every expanded and new category in this directory is built on the same five-section,
       fifty-title architecture &mdash; so the library scales without losing coherence.</p>
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
  {originals_html}
  {expanded_html}
  {flat_html}
  {new_html}
  {flourishing_html}
  {purpose_html}
</div>

<footer>
  LifeTogether Ministries &middot; Business &amp; Workplace Intelligence&trade; Master Directory<br>
  {TOTAL_CATEGORIES} categories &middot; {TOTAL_CAMPAIGNS:,}+ flagship campaigns &middot; internal working document
</footer>

</body>
</html>
"""

with open("/mnt/user-data/outputs/lifetogether-workplace-intelligence-master-directory.html", "w") as f:
    f.write(HTML)

print("Wrote HTML,", len(HTML), "bytes")
print("Total categories:", TOTAL_CATEGORIES, "Total campaigns:", TOTAL_CAMPAIGNS)
