# -*- coding: utf-8 -*-
import html
from data import CATEGORIES, NAMING_FORMULAS, PALETTE

def esc(s):
    return html.escape(s, quote=True)

# ---- CSS ----
CSS = """
:root {
  --navy: #0f1a2e; --navy-mid: #162035; --navy-light: #1e2d4a;
  --gold: #c9a84c; --gold-light: #e2c97e; --gold-pale: #f0dfa0;
  --cream: #f5f0e8; --cream-dark: #ede4d2;
  --text-light: #d4c9b8; --text-muted: #9aa7c2;
  --white: #ffffff;
  --forest: #16261a; --forest-light: #1d3324;
  --plum: #201229; --plum-light: #2a1836;
  --olive: #22240f; --olive-light: #2c2f14;
  --teal: #0d211f; --teal-light: #123029;
  --umber: #221207; --umber-light: #2c1a0c;
}
* { margin:0; padding:0; box-sizing:border-box; }
html { scroll-behavior: smooth; }
body {
  font-family: 'Lato', sans-serif;
  background: var(--navy);
  color: var(--cream);
  line-height: 1.55;
  font-size: 16px;
}
em { font-style: italic; color: var(--gold-light); }
h1, h2, h3 { font-family: 'Playfair Display', serif; font-weight: 700; }
.serif-alt { font-family: 'Cormorant Garamond', serif; }

/* ===== COVER ===== */
.cover {
  min-height: 100vh; background: var(--navy);
  display:flex; flex-direction:column; justify-content:center; align-items:flex-start;
  padding: 64px 28px; position: relative; overflow:hidden;
}
.cover::before {
  content:''; position:absolute; top:0; right:0; width:55%; height:100%;
  background: linear-gradient(135deg, var(--navy-light) 0%, #0a1220 100%);
  clip-path: polygon(20% 0, 100% 0, 100% 100%, 0% 100%);
}
.cover::after {
  content:''; position:absolute; bottom:0; left:0; width:100%; height:3px;
  background: linear-gradient(90deg, var(--gold) 0%, var(--gold-pale) 50%, transparent 100%);
}
.cover-eyebrow {
  font-size: 11px; font-weight:700; letter-spacing:3px; text-transform:uppercase;
  color: var(--gold); margin-bottom:22px; position:relative; z-index:1;
}
.cover h1 {
  font-size: clamp(2.1rem, 8vw, 3.4rem); line-height:1.08; color: var(--white);
  position:relative; z-index:1; max-width: 640px;
}
.cover h1 em { color: var(--gold-light); font-style: italic; }
.cover-sub {
  font-family:'Cormorant Garamond', serif; font-size: 1.35rem; font-style:italic;
  color: var(--text-light); margin-top:18px; max-width: 520px; position:relative; z-index:1;
}
.cover-stats {
  display:flex; gap:28px; margin-top:40px; position:relative; z-index:1; flex-wrap:wrap;
}
.cover-stat-num { font-family:'Playfair Display',serif; font-size:2rem; color:var(--gold-light); }
.cover-stat-label { font-size:10px; letter-spacing:2px; text-transform:uppercase; color:var(--text-muted); margin-top:2px; }
.cover-footer { margin-top:56px; font-size:11px; letter-spacing:2px; text-transform:uppercase; color:var(--text-muted); position:relative; z-index:1; }

/* ===== SECTION SHELLS ===== */
section.block { padding: 56px 22px; }
.bg-navy { background: var(--navy); }
.bg-forest { background: var(--forest); }
.bg-plum { background: var(--plum); }
.bg-olive { background: var(--olive); }
.bg-teal { background: var(--teal); }
.bg-umber { background: var(--umber); }

/* ===== INTRO / FRAMEWORK ===== */
.intro-eyebrow { font-size:10px; letter-spacing:3px; text-transform:uppercase; color:var(--gold); margin-bottom:14px; }
.intro h2 { font-size: clamp(1.5rem, 6vw, 2.1rem); color:var(--white); margin-bottom:14px; }
.intro p { color: var(--text-light); font-size: 0.98rem; margin-bottom: 14px; max-width: 640px; }
.criteria-box {
  border: 1px solid rgba(201,168,76,0.35); border-radius: 4px; padding: 18px 20px; margin: 22px 0;
  background: rgba(201,168,76,0.05);
}
.criteria-box .label { font-size:10px; letter-spacing:2px; text-transform:uppercase; color:var(--gold); margin-bottom:8px; }
.criteria-box p { margin-bottom:8px; font-size:0.92rem; }
.criteria-box p:last-child { margin-bottom:0; }

.formula-grid { display:grid; grid-template-columns: 1fr; gap:12px; margin-top:22px; }
.formula-card {
  border-left: 3px solid var(--gold); background: rgba(255,255,255,0.03);
  padding: 14px 16px; border-radius: 2px;
}
.formula-name { font-size:10px; letter-spacing:2px; text-transform:uppercase; color:var(--gold-light); margin-bottom:4px; }
.formula-pattern { font-family:'Cormorant Garamond',serif; font-style:italic; font-size:1.15rem; color:var(--white); margin-bottom:4px; }
.formula-note { font-size:0.85rem; color:var(--text-muted); }

/* ===== TOC ===== */
.toc h2 { color:var(--white); font-size:1.6rem; margin-bottom:6px; }
.toc-sub { color:var(--text-muted); font-size:0.85rem; margin-bottom:22px; }
.toc-group-label { font-size:10px; letter-spacing:2px; text-transform:uppercase; color:var(--gold); margin: 22px 0 10px; }
.toc-list { list-style:none; }
.toc-list li { border-bottom: 1px solid rgba(255,255,255,0.08); padding: 10px 0; }
.toc-list a { color: var(--cream); text-decoration:none; font-size:0.95rem; display:flex; justify-content:space-between; gap:10px; }
.toc-num { color: var(--gold); font-family:'Playfair Display',serif; margin-right:10px; }
.toc-tag { font-size:9px; letter-spacing:1.5px; text-transform:uppercase; color:var(--gold-light); border:1px solid rgba(201,168,76,0.4); border-radius:10px; padding:2px 8px; white-space:nowrap; }

/* ===== CATEGORY SECTION HEADER ===== */
.cat-header { padding-bottom: 8px; }
.cat-eyebrow { font-size:11px; letter-spacing:2px; text-transform:uppercase; color:var(--gold); margin-bottom:10px; display:flex; align-items:center; gap:10px; }
.cat-num-badge {
  display:inline-flex; align-items:center; justify-content:center;
  width:30px; height:30px; border:1px solid var(--gold); border-radius:50%;
  font-family:'Playfair Display',serif; color:var(--gold-light); font-size:0.85rem;
}
.new-badge { background: var(--gold); color: var(--navy); font-weight:700; border-radius:10px; padding:2px 9px; font-size:9px; letter-spacing:1px; }
.cat-header h2 { font-size: clamp(1.4rem, 6vw, 2rem); color: var(--white); margin: 6px 0 10px; }
.cat-header h2 em { font-style: italic; color: var(--gold-light); }
.cat-tagline { font-family:'Cormorant Garamond',serif; font-style:italic; font-size:1.2rem; color: var(--gold-pale); margin-bottom:10px; }
.cat-desc { color: var(--text-light); font-size:0.92rem; max-width:620px; margin-bottom: 22px; }

/* ===== FLAGSHIP FORMULA SHOWCASE ===== */
.showcase-label { font-size:10px; letter-spacing:2px; text-transform:uppercase; color:var(--text-muted); margin-bottom:10px; }
.showcase-grid { display:grid; grid-template-columns:1fr; gap:8px; margin-bottom:28px; }
.showcase-item { background: rgba(255,255,255,0.04); border-radius:3px; padding:10px 14px; display:flex; flex-direction:column; gap:2px; }
.showcase-tag { font-size:9px; letter-spacing:1.5px; text-transform:uppercase; color: var(--gold-light); }
.showcase-title { font-size:0.93rem; color: var(--white); }

/* ===== TITLE CARDS ===== */
.cards-grid { display:grid; grid-template-columns:1fr; gap:10px; }
.title-card {
  background: rgba(255,255,255,0.035); border-radius:4px; padding:13px 15px;
  border-left: 2px solid rgba(201,168,76,0.5);
}
.card-top { display:flex; justify-content:space-between; align-items:baseline; gap:8px; margin-bottom:4px; }
.card-num { font-size:0.72rem; color:var(--text-muted); font-family:'Playfair Display',serif; }
.card-formula { font-size:8.5px; letter-spacing:1px; text-transform:uppercase; color:var(--gold-light); border:1px solid rgba(201,168,76,0.35); border-radius:8px; padding:1px 7px; white-space:nowrap; }
.card-title { font-size:0.97rem; color: var(--white); font-weight:400; display:block; margin-bottom:3px; }
.card-desc { font-size:0.82rem; color: var(--text-muted); }

.divider { height:1px; background: linear-gradient(90deg, transparent, rgba(201,168,76,0.4), transparent); }

/* ===== BACK / COLOPHON ===== */
.colophon { background: var(--navy); padding: 60px 22px; text-align:center; }
.colophon h3 { color:var(--white); font-size:1.3rem; margin-bottom:10px; }
.colophon p { color: var(--text-muted); font-size:0.85rem; max-width:480px; margin: 0 auto 8px; }
.colophon .gold-rule { width:60px; height:2px; background:var(--gold); margin: 20px auto; }

@media (min-width: 720px) {
  .cover { padding: 100px 90px; }
  section.block { padding: 80px 80px; }
  .cards-grid { grid-template-columns: 1fr 1fr; }
  .formula-grid { grid-template-columns: 1fr 1fr; }
  .showcase-grid { grid-template-columns: 1fr 1fr; }
}
@media (min-width: 1080px) {
  .cards-grid { grid-template-columns: 1fr 1fr 1fr; }
}
"""

HEAD = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>The Master 40-Day Campaign Library &middot; LifeTogether</title>
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,600;0,700;1,400;1,600&family=Cormorant+Garamond:ital,wght@0,300;0,400;0,600;1,300;1,400&family=Lato:wght@300;400;700;900&display=swap" rel="stylesheet">
<style>
""" + CSS + """
</style>
</head>
<body>
"""

def build_cover():
    return f"""
<section class="cover">
  <p class="cover-eyebrow">LifeTogether Ministries &middot; Campaign &amp; Curriculum Library</p>
  <h1>The Master 40-Day<br><em>Campaign Library</em></h1>
  <p class="cover-sub">Every proven title, every way to say it &mdash; organized into one consolidated churchwide reference.</p>
  <div class="cover-stats">
    <div><div class="cover-stat-num">30</div><div class="cover-stat-label">Categories</div></div>
    <div><div class="cover-stat-num">600</div><div class="cover-stat-label">Titles</div></div>
    <div><div class="cover-stat-num">5</div><div class="cover-stat-label">Naming Formulas</div></div>
    <div><div class="cover-stat-num">All</div><div class="cover-stat-label">Ages &middot; Weekend-Driven</div></div>
  </div>
  <p class="cover-footer">Consolidated Edition &middot; Deduplicated &amp; Expanded</p>
</section>
"""

def build_intro():
    formula_html = ""
    for name, pattern, note in NAMING_FORMULAS:
        formula_html += f"""
        <div class="formula-card">
          <div class="formula-name">{esc(name)}</div>
          <div class="formula-pattern">{esc(pattern)}</div>
          <div class="formula-note">{esc(note)}</div>
        </div>"""
    return f"""
<section class="block bg-navy intro">
  <p class="intro-eyebrow">How This Library Works</p>
  <h2>One theme, <em>five ways</em> to say it</h2>
  <p>Every campaign in this library is built on a single underlying theme &mdash; Purpose, Hope, Freedom, Peace &mdash; expressed through five reusable naming formulas. Pick the formula that fits your season, your audience, and your art direction.</p>
  <div class="formula-grid">{formula_html}
  </div>
  <div class="criteria-box">
    <div class="label">Scope of This Library</div>
    <p><strong>Only series that work across all ages, and are built for the weekend.</strong> Every category here is written for the whole church at once &mdash; kids, teens, and adults each running their own edition of the same six-week arc, gathered by the same Sunday sermon &mdash; not narrow small-group-only or single-demographic content.</p>
    <p>That's why you won't find gender-specific, career-stage, or life-stage-only titles here. Those belong in the Small Group Finder / Builder library. This is the churchwide, weekend-driven core.</p>
  </div>
</section>
"""

def build_toc():
    items = ""
    for c in CATEGORIES:
        tag = '<span class="toc-tag">New</span>' if c["tag"] == "New" else ""
        items += f"""
        <li><a href="#cat-{c['roman']}"><span><span class="toc-num">{c['roman']}</span>{esc(c['name'])}</span>{tag}</a></li>"""
    return f"""
<section class="block bg-navy toc">
  <h2>Contents</h2>
  <p class="toc-sub">30 categories &middot; 20 titles each &middot; 600 total</p>
  <ul class="toc-list">{items}
  </ul>
</section>
"""

def build_category(cat, bg):
    tag_badge = '<span class="new-badge">New Category</span>' if cat["tag"] == "New" else ""
    showcase_html = ""
    for name, ex in cat["flagship"]:
        showcase_html += f"""
      <div class="showcase-item"><span class="showcase-tag">{esc(name)}</span><span class="showcase-title">{esc(ex)}</span></div>"""

    cards_html = ""
    for i, (title, formula, desc) in enumerate(cat["titles"], 1):
        cards_html += f"""
      <div class="title-card">
        <div class="card-top"><span class="card-num">{i:02d}</span><span class="card-formula">{esc(formula)}</span></div>
        <span class="card-title">{esc(title)}</span>
        <span class="card-desc">{esc(desc)}</span>
      </div>"""

    return f"""
<section class="block bg-{bg} cat-header" id="cat-{cat['roman']}">
  <p class="cat-eyebrow"><span class="cat-num-badge">{cat['roman']}</span> Category {cat['roman']} {tag_badge}</p>
  <h2>{esc(cat['name'])}</h2>
  <p class="cat-tagline">&ldquo;{esc(cat['tagline'])}&rdquo;</p>
  <p class="cat-desc">{esc(cat['description'])}</p>
  <p class="showcase-label">Flagship Theme &mdash; Shown in Four Formulas</p>
  <div class="showcase-grid">{showcase_html}
  </div>
  <p class="showcase-label">All 20 Titles in This Category</p>
  <div class="cards-grid">{cards_html}
  </div>
</section>
<div class="divider"></div>
"""

def build_colophon():
    return """
<section class="colophon">
  <div class="gold-rule"></div>
  <h3>The Master 40-Day Campaign Library</h3>
  <p>Consolidated from LifeTogether's existing campaign catalog, deduplicated, and expanded with ten additional categories grounded in current preaching-trend research.</p>
  <p>30 categories &middot; 600 titles &middot; 5 naming formulas &middot; built for the whole church, every age, every weekend.</p>
</section>
"""

def main():
    parts = [HEAD, build_cover(), build_intro(), build_toc()]
    for i, cat in enumerate(CATEGORIES):
        bg = PALETTE[i % len(PALETTE)]
        parts.append(build_category(cat, bg))
    parts.append(build_colophon())
    parts.append("</body></html>")
    html_out = "".join(parts)
    with open("/mnt/user-data/outputs/lifetogether-40-day-campaign-library.html", "w") as f:
        f.write(html_out)
    print("Written. Length:", len(html_out))

if __name__ == "__main__":
    main()
