# -*- coding: utf-8 -*-
import html

def esc(s):
    return html.escape(s, quote=True)

CSS = """
:root {
  --navy: #0f1a2e; --navy-mid: #162035; --navy-light: #1e2d4a;
  --gold: #c9a84c; --gold-light: #e2c97e; --gold-pale: #f0dfa0;
  --cream: #f5f0e8; --cream-dark: #ede4d2;
  --text-light: #cdc0ab; --text-muted: #8892a8; --text-faint: #5f6a83;
  --white: #ffffff;
  --forest: #16261a; --plum: #201229; --olive: #22240f; --teal: #0d211f; --umber: #221207;
}
* { margin:0; padding:0; box-sizing:border-box; }
html { scroll-behavior: smooth; }
body { font-family:'Lato',sans-serif; background:var(--navy); color:var(--cream); line-height:1.6; font-size:16px; -webkit-font-smoothing:antialiased; }
em { font-style:italic; color:var(--gold-light); }
h1,h2,h3 { font-family:'Playfair Display',serif; font-weight:700; }
a { color:inherit; }

/* ===== COVER / HERO ===== */
.cover { min-height:100vh; background:var(--navy); display:flex; flex-direction:column; justify-content:center; padding:70px 26px; position:relative; overflow:hidden; }
.cover::before { content:''; position:absolute; top:0; right:0; width:50%; height:100%; background:linear-gradient(150deg,var(--navy-light) 0%,#0a1220 100%); clip-path:polygon(22% 0,100% 0,100% 100%,0 100%); }
.cover::after { content:''; position:absolute; bottom:0; left:0; width:100%; height:3px; background:linear-gradient(90deg,var(--gold) 0%,var(--gold-pale) 45%,transparent 100%); }
.kicker { font-size:10.5px; font-weight:700; letter-spacing:3.5px; text-transform:uppercase; color:var(--gold); margin-bottom:26px; position:relative; z-index:1; }
.cover h1 { font-size:clamp(2rem,8vw,3.3rem); line-height:1.1; color:var(--white); position:relative; z-index:1; max-width:660px; }
.lede { font-family:'Cormorant Garamond',serif; font-size:1.28rem; font-style:italic; font-weight:400; color:var(--text-light); margin-top:20px; max-width:560px; position:relative; z-index:1; }
.meta { display:flex; gap:0; margin-top:44px; position:relative; z-index:1; flex-wrap:wrap; border-top:1px solid rgba(201,168,76,0.25); padding-top:22px; }
.meta > div { padding-right:32px; margin-right:0; }
.meta .n { font-family:'Playfair Display',serif; font-size:1.9rem; color:var(--gold-light); line-height:1; }
.meta .l { font-size:9.5px; letter-spacing:1.8px; text-transform:uppercase; color:var(--text-muted); margin-top:5px; }
.cover-tag { margin-top:40px; font-size:10.5px; letter-spacing:2px; text-transform:uppercase; color:var(--text-faint); position:relative; z-index:1; }

/* ===== SECTION SHELLS ===== */
section.block { padding:58px 24px; }
.bg-navy{background:var(--navy);} .bg-forest{background:var(--forest);} .bg-plum{background:var(--plum);}
.bg-olive{background:var(--olive);} .bg-teal{background:var(--teal);} .bg-umber{background:var(--umber);}

/* ===== NAV / TOC ===== */
.toc-nav { padding:40px 24px; background:var(--navy); border-bottom:1px solid rgba(201,168,76,0.18); }
.toc-nav .toc-title { font-size:1.4rem; color:var(--white); margin-bottom:4px; }
.toc-nav .toc-note { font-size:0.82rem; color:var(--text-faint); margin-bottom:22px; }
.toc-nav a.toc-link { display:flex; align-items:baseline; gap:14px; padding:9px 0; text-decoration:none; border-bottom:1px solid rgba(255,255,255,0.06); font-size:0.92rem; color:var(--cream); }
.toc-nav a.toc-link .ix { font-family:'Playfair Display',serif; color:var(--gold); font-size:0.85rem; min-width:26px; }
.toc-nav .toc-group { font-size:9.5px; letter-spacing:2.5px; text-transform:uppercase; color:var(--gold-light); margin:22px 0 4px; }

/* ===== NARRATIVE / STRATEGY BLOCKS ===== */
.intro-eyebrow { font-size:10px; letter-spacing:3px; text-transform:uppercase; color:var(--gold); margin-bottom:6px; }
.intro-eyebrow .ix { font-family:'Playfair Display',serif; font-size:1.3rem; color:var(--gold-light); margin-right:10px; }
.intro h2 { font-size:clamp(1.5rem,6vw,2.15rem); color:var(--white); margin:8px 0 16px; }
.intro p { color:var(--text-light); font-size:0.98rem; margin-bottom:14px; max-width:660px; }
.intro p:first-of-type::first-letter {
  font-family:'Playfair Display',serif; font-size:2.6rem; float:left; line-height:0.8; padding-right:8px; padding-top:6px; color:var(--gold-light);
}
.criteria-box { border-top:1px solid rgba(201,168,76,0.35); border-bottom:1px solid rgba(201,168,76,0.35); padding:18px 0; margin:26px 0; }
.criteria-box .label { font-size:10px; letter-spacing:2px; text-transform:uppercase; color:var(--gold); margin-bottom:10px; }
.criteria-box p { margin-bottom:8px; font-size:0.9rem; max-width:none; }
.criteria-box p:last-child { margin-bottom:0; }
.pull-quote { font-family:'Cormorant Garamond',serif; font-style:italic; font-size:1.35rem; color:var(--gold-pale); border-left:2px solid var(--gold); padding-left:20px; margin:24px 0; max-width:600px; line-height:1.45; }

.formula-grid { display:grid; grid-template-columns:1fr; gap:1px; margin-top:22px; background:rgba(201,168,76,0.18); }
.formula-card { background:var(--navy); padding:16px 18px; }
.formula-name { font-size:10px; letter-spacing:2px; text-transform:uppercase; color:var(--gold-light); margin-bottom:4px; }
.formula-pattern { font-family:'Cormorant Garamond',serif; font-style:italic; font-size:1.1rem; color:var(--white); margin-bottom:4px; }
.formula-note { font-size:0.84rem; color:var(--text-muted); }

.session-map { display:grid; grid-template-columns:repeat(7,1fr); gap:5px; margin:20px 0; }
.session-day { background:rgba(255,255,255,0.04); padding:9px 3px; text-align:center; border-bottom:2px solid rgba(255,255,255,0.08); }
.session-day.sunday { background:rgba(201,168,76,0.14); border-bottom:2px solid var(--gold); }
.session-day-label { font-size:8px; letter-spacing:1px; text-transform:uppercase; color:var(--text-faint); }
.session-day-name { font-family:'Playfair Display',serif; font-size:0.72rem; color:var(--white); margin-top:3px; }
.legacy-box { border-left:2px solid var(--gold); padding:4px 0 4px 16px; margin:20px 0; font-size:0.85rem; color:var(--text-light); max-width:640px; }
.legacy-box .label { font-size:10px; letter-spacing:2px; text-transform:uppercase; color:var(--gold-light); margin-bottom:6px; }

/* ===== CATEGORY OUTLINE (quick-reference list before full listings) ===== */
.outline-wrap { margin:26px 0 6px; }
.outline-label { font-size:10px; letter-spacing:2px; text-transform:uppercase; color:var(--text-muted); margin-bottom:12px; }
.outline-list { columns:1; column-gap:36px; list-style:none; }
.outline-list li { display:flex; align-items:baseline; gap:10px; padding:7px 0; border-bottom:1px solid rgba(255,255,255,0.06); break-inside:avoid; }
.outline-list .rn { font-family:'Playfair Display',serif; color:var(--gold); font-size:0.85rem; min-width:22px; }
.outline-list .nm { font-size:0.88rem; color:var(--cream); }
.outline-list .ct { font-size:0.72rem; color:var(--text-faint); margin-left:auto; white-space:nowrap; }

/* ===== CATEGORY SECTION HEADER ===== */
.cat-header { padding-bottom:6px; }
.cat-eyebrow { font-size:10.5px; letter-spacing:2px; text-transform:uppercase; color:var(--gold); margin-bottom:10px; display:flex; align-items:center; gap:12px; }
.cat-num-badge { font-family:'Playfair Display',serif; color:var(--gold-light); font-size:1rem; border-bottom:1px solid var(--gold); padding-bottom:2px; }
.cat-header h2 { font-size:clamp(1.35rem,6vw,1.9rem); color:var(--white); margin:4px 0 8px; }
.cat-tagline { font-family:'Cormorant Garamond',serif; font-style:italic; font-size:1.15rem; color:var(--gold-pale); margin-bottom:8px; }
.cat-desc { color:var(--text-light); font-size:0.9rem; max-width:600px; margin-bottom:20px; }

/* ===== TITLE DIRECTORY LIST (replaces card grid) ===== */
.showcase-label { font-size:10px; letter-spacing:2px; text-transform:uppercase; color:var(--text-muted); margin-bottom:2px; margin-top:22px; }
.title-list { list-style:none; margin-top:10px; }
.title-list li { padding:10px 0; border-bottom:1px solid rgba(255,255,255,0.055); }
.title-row { display:flex; align-items:baseline; gap:10px; flex-wrap:wrap; }
.title-num { font-family:'Playfair Display',serif; font-size:0.7rem; color:var(--text-faint); min-width:20px; }
.title-name { font-size:0.94rem; color:var(--white); flex:1; min-width:180px; }
.title-formula { font-size:7.5px; letter-spacing:1px; text-transform:uppercase; color:var(--gold-light); border:1px solid rgba(201,168,76,0.35); border-radius:8px; padding:1.5px 7px; white-space:nowrap; }
.title-desc { font-size:0.78rem; color:var(--text-faint); margin-left:30px; margin-top:2px; display:block; }
@media (min-width:760px) { .title-list.cols-2 { columns:2; column-gap:34px; } .title-list.cols-2 li { break-inside:avoid; } }

/* ===== SHOWCASE (flagship formula demo) ===== */
.showcase-grid { display:grid; grid-template-columns:1fr; gap:1px; margin-bottom:8px; background:rgba(255,255,255,0.06); }
.showcase-item { background:var(--navy-mid); padding:10px 14px; display:flex; flex-direction:column; gap:2px; }
.showcase-tag { font-size:9px; letter-spacing:1.5px; text-transform:uppercase; color:var(--gold-light); }
.showcase-title { font-size:0.9rem; color:var(--white); }

.divider { height:1px; background:linear-gradient(90deg,transparent,rgba(201,168,76,0.45),transparent); }

/* ===== CALENDAR MAP ===== */
.cal-list { list-style:none; margin-top:14px; }
.cal-list li { display:flex; gap:14px; padding:13px 0; border-bottom:1px solid rgba(255,255,255,0.06); align-items:flex-start; }
.cal-when { font-family:'Playfair Display',serif; font-size:0.78rem; color:var(--gold); min-width:150px; flex-shrink:0; }
.cal-body .cal-title { font-size:0.95rem; color:var(--white); display:block; }
.cal-body .cal-cat { font-size:0.72rem; color:var(--gold-light); display:block; margin:2px 0 3px; }
.cal-body .cal-note { font-size:0.82rem; color:var(--text-faint); }

/* ===== BACK COVER / COLOPHON ===== */
.back-cover { background:var(--navy); padding:90px 26px 70px; text-align:center; position:relative; }
.back-cover .gold-rule { width:48px; height:1px; background:var(--gold); margin:0 auto 30px; }
.back-cover .quote { font-family:'Cormorant Garamond',serif; font-style:italic; font-size:1.35rem; color:var(--cream); max-width:620px; margin:0 auto 18px; line-height:1.5; }
.back-cover .attribution { font-size:0.82rem; letter-spacing:1px; color:var(--gold-light); margin-bottom:34px; }
.back-cover .contact { font-size:0.8rem; color:var(--text-muted); letter-spacing:0.5px; }
.back-cover .contact a { color:var(--gold-light); text-decoration:none; }
.back-cover .mark { font-family:'Playfair Display',serif; font-size:1.1rem; color:var(--text-faint); margin-top:36px; letter-spacing:1px; }

@media (min-width:760px) {
  .cover { padding:110px 90px; } section.block { padding:80px 80px; } .toc-nav{ padding:60px 80px; }
  .outline-list { columns:2; }
}
@media (min-width:1080px) { .outline-list { columns:3; } }
"""

def head(title):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{esc(title)} &middot; LifeTogether</title>
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,600;0,700;0,900;1,400;1,600&family=Cormorant+Garamond:ital,wght@0,300;0,400;0,500;0,600;1,300;1,400&family=Lato:wght@300;400;700;900&display=swap" rel="stylesheet">
<style>{CSS}</style>
</head>
<body>
"""

def cover(kicker, title_html, lede, stats):
    stat_html = ""
    for num, label in stats:
        stat_html += f'<div><div class="n">{esc(str(num))}</div><div class="l">{esc(label)}</div></div>'
    return f"""
<section class="cover">
  <p class="kicker">{esc(kicker)}</p>
  <h1>{title_html}</h1>
  <p class="lede">{lede}</p>
  <div class="meta">{stat_html}</div>
</section>
"""

def outline_of_categories(categories, label="Categories at a Glance"):
    items = ""
    for c in categories:
        items += f'<li><span class="rn">{esc(c["roman"])}</span><span class="nm">{esc(c["name"])}</span><span class="ct">{len(c["titles"])} titles</span></li>'
    return f"""
<div class="outline-wrap">
  <p class="outline-label">{esc(label)}</p>
  <ul class="outline-list">{items}</ul>
</div>
"""

def category_section(cat, bg, two_col=True):
    list_class = "title-list cols-2" if two_col else "title-list"
    rows = ""
    for i, (title, formula, desc) in enumerate(cat["titles"], 1):
        rows += f"""
      <li>
        <div class="title-row"><span class="title-num">{i:02d}</span><span class="title-name">{esc(title)}</span><span class="title-formula">{esc(formula)}</span></div>
        <span class="title-desc">{esc(desc)}</span>
      </li>"""
    return f"""
<section class="block bg-{bg} cat-header" id="cat-{cat['roman']}">
  <p class="cat-eyebrow"><span class="cat-num-badge">{cat['roman']}</span> Category {cat['roman']}</p>
  <h2>{esc(cat['name'])}</h2>
  <p class="cat-tagline">&ldquo;{esc(cat['tagline'])}&rdquo;</p>
  <p class="cat-desc">{esc(cat['description'])}</p>
  <p class="showcase-label">All {len(cat['titles'])} Titles</p>
  <ul class="{list_class}">{rows}</ul>
</section>
<div class="divider"></div>
"""

def back_cover(quote, attribution, contact_line, mark):
    return f"""
<section class="back-cover">
  <div class="gold-rule"></div>
  <p class="quote">&ldquo;{quote}&rdquo;</p>
  <p class="attribution">{esc(attribution)}</p>
  <p class="contact">{contact_line}</p>
  <div class="mark">{esc(mark)}</div>
</section>
"""

PALETTE = ["navy", "forest", "plum", "olive", "teal", "umber"]
