# -*- coding: utf-8 -*-
"""Reusable proposal-style Campaign Catalog engine (US Letter, multi-page).
Feed it a cfg dict (see build_*_catalog.py data files) and it returns full HTML."""
import pathlib

FONTS = pathlib.Path("/tmp/fonts_embed.css").read_text()

_CSS = """
*{margin:0;padding:0;box-sizing:border-box;-webkit-print-color-adjust:exact;print-color-adjust:exact;}
:root{ --navy:#11243f; --navy2:#0b1a30; --cream:#f7f3ea; --ink:#243140; --soft:#5a6675;
 --line:#dcd3bf; --accent:%ACCENT%; --gold:%ACCENT2%; }
@page{ size:8.5in 11in; margin:0; }
html,body{ background:#33373f; font-family:'Spectral',serif; color:var(--ink); }
.page{ position:relative; width:8.5in; height:11in; overflow:hidden; background:#fff; page-break-after:always; }
.page:last-child{ page-break-after:auto; }
.pad{ position:absolute; inset:0.6in 0.62in 0.55in 0.62in; }
.pad.flex{ display:flex; flex-direction:column; }
.grow{ flex:1 1 0; min-height:0; }

.rhead{ position:absolute; top:0.34in; left:0.62in; right:0.62in; display:flex; justify-content:space-between;
 align-items:center; font-family:'Archivo',sans-serif; font-size:6.6pt; letter-spacing:.2em; text-transform:uppercase;
 color:#9aa2ad; border-bottom:1px solid var(--line); padding-bottom:5px; }
.rhead .b{ color:var(--accent); font-weight:700; }
.rfoot{ position:absolute; bottom:0.34in; left:0.62in; right:0.62in; display:flex; justify-content:space-between;
 align-items:center; font-family:'Archivo',sans-serif; font-size:6.4pt; letter-spacing:.18em; text-transform:uppercase;
 color:#aab1bb; border-top:1px solid var(--line); padding-top:5px; }

/* PAGE 1 OVERVIEW */
.ov-band{ position:absolute; top:0; left:0; right:0; height:3.05in;
 background:linear-gradient(150deg,#15294a 0%,#0c1c34 60%,#0a1727 100%); color:#f1ead9; }
.ov-band .frame{ position:absolute; inset:0.28in; border:1px solid rgba(193,154,75,.4); }
.ov-band .inner{ position:absolute; inset:0.5in 0.7in; display:flex; flex-direction:column; }
.brand{ font-family:'Archivo',sans-serif; font-weight:700; letter-spacing:.4em; text-transform:uppercase; font-size:8pt; color:var(--gold); }
.doctype{ font-family:'Archivo',sans-serif; font-weight:600; letter-spacing:.28em; text-transform:uppercase; font-size:7pt; color:#b9b297; margin-top:3px; }
.ov-title{ font-family:'Playfair Display',serif; font-weight:800; font-size:42pt; line-height:.98; margin-top:auto; }
.ov-title em{ font-style:italic; color:var(--gold); }
.ov-sub{ font-family:'Archivo',sans-serif; font-weight:600; letter-spacing:.16em; text-transform:uppercase; font-size:7.4pt; color:#cdbf9f; margin-top:9px; }
.ov-orn{ display:flex; align-items:center; gap:9px; margin-top:13px; }
.ov-orn .ln{ height:1px; width:46px; background:var(--gold); }
.ov-orn .dot{ width:5px; height:5px; background:var(--gold); transform:rotate(45deg); }
.ov-pos{ font-family:'Spectral',serif; font-style:italic; font-size:11pt; line-height:1.45; color:#e7dfcc; margin-top:13px; max-width:6.4in; }
.ov-body{ position:absolute; top:3.32in; left:0.62in; right:0.62in; bottom:0.5in; }
.sec-label{ font-family:'Archivo',sans-serif; font-weight:700; letter-spacing:.18em; text-transform:uppercase; font-size:7.4pt; color:var(--accent); margin-bottom:4px; display:flex; align-items:center; gap:6px;}
.sec-label::before{ content:""; width:14px; height:2px; background:var(--accent); display:inline-block; }
.sec-body{ font-size:8.7pt; line-height:1.5; color:#3f4855; }
.two{ display:flex; gap:0.34in; margin-top:8px; } .two > div{ flex:1; }
.mt{ margin-top:11px; }
.who{ display:grid; grid-template-columns:1fr 1fr; gap:7px 0.3in; margin-top:7px; }
.who .wt{ font-family:'Playfair Display',serif; font-weight:700; font-size:9.4pt; color:var(--navy); }
.who .wd{ font-size:7.7pt; line-height:1.4; color:#5a6470; }
.cols2{ display:flex; gap:0.34in; margin-top:6px;} .outlist{ flex:1; }
.outlist .o{ font-size:8.2pt; line-height:1.5; color:#3f4855; padding-left:13px; position:relative; }
.outlist .o::before{ content:""; position:absolute; left:0; top:6px; width:5px; height:5px; background:var(--gold); border-radius:50%; }
.uc{ display:flex; flex-direction:column; gap:5px; margin-top:6px; }
.uc .u{ display:flex; gap:8px; align-items:baseline; }
.uc .ut{ font-family:'Archivo',sans-serif; font-weight:700; font-size:7.7pt; color:var(--navy); min-width:1.9in; }
.uc .ud{ font-size:7.7pt; line-height:1.35; color:#5a6470; flex:1; }
.statband{ display:flex; margin-top:12px; border:1px solid var(--line); }
.statband .s{ flex:1; text-align:center; padding:8px 4px; border-right:1px solid var(--line); }
.statband .s:last-child{ border-right:none; }
.statband .sn{ font-family:'Playfair Display',serif; font-size:17pt; color:var(--accent); line-height:1; }
.statband .sl{ font-family:'Archivo',sans-serif; font-size:6pt; letter-spacing:.18em; text-transform:uppercase; color:#8a929d; margin-top:4px; }

/* PAGE 2 TOP 10 */
.ptitle{ font-family:'Playfair Display',serif; font-weight:800; font-size:23pt; color:var(--navy); line-height:1; }
.ptitle em{ font-style:italic; color:var(--accent); }
.psub{ font-size:9pt; line-height:1.4; color:#5a6470; margin-top:6px; max-width:6.2in; }
.t10{ margin-top:12px; border-top:2.5px solid var(--navy); }
.t10 .row{ display:flex; gap:14px; padding:6.7px 0; border-bottom:1px solid var(--line); align-items:flex-start; }
.t10 .rn{ font-family:'Playfair Display',serif; font-weight:800; font-size:14pt; color:var(--accent); width:0.4in; flex-shrink:0; line-height:1; padding-top:1px; }
.t10 .rn .rn-rule{ width:16px; height:2px; background:var(--gold); margin-top:4px; }
.t10 .rmid{ flex:1; }
.t10 .rt{ font-family:'Playfair Display',serif; font-weight:700; font-size:11.5pt; color:var(--navy); line-height:1.05; }
.t10 .rp{ font-family:'Spectral',serif; font-style:italic; font-size:8.3pt; color:var(--accent); margin-top:2px; }
.t10 .rs{ font-size:7.7pt; line-height:1.36; color:#566069; margin-top:3px; }
.t10 .rmeta{ width:1.5in; flex-shrink:0; text-align:right; padding-top:2px; }
.t10 .rfelt{ font-family:'Archivo',sans-serif; font-weight:700; font-size:6.8pt; letter-spacing:.09em; text-transform:uppercase; color:var(--navy); }
.t10 .raud{ font-family:'Archivo',sans-serif; font-size:6.5pt; letter-spacing:.06em; color:#8a929d; margin-top:3px; }
.t10-foot{ margin-top:8px; font-family:'Spectral',serif; font-style:italic; font-size:8.2pt; color:#7a828d; text-align:center; }

/* EXPANDED CAMPAIGN */
.cnum{ position:absolute; top:0.5in; right:0.62in; font-family:'Playfair Display',serif; font-weight:900; font-size:62pt; line-height:1; color:var(--accent); opacity:.1; }
.c-kick{ font-family:'Archivo',sans-serif; font-weight:700; letter-spacing:.2em; text-transform:uppercase; font-size:7pt; color:var(--accent); display:flex; align-items:center; gap:7px; }
.c-kick::before{ content:""; width:5px; height:5px; background:var(--accent); transform:rotate(45deg); display:inline-block; }
.c-title{ font-family:'Playfair Display',serif; font-weight:800; font-size:27pt; color:var(--navy); line-height:1; margin-top:5px; }
.c-pos{ font-family:'Spectral',serif; font-style:italic; font-size:11pt; color:var(--accent); margin-top:6px; }
.c-rule{ width:42px; height:3px; background:var(--accent); margin:9px 0; }
.c-mkt{ font-size:9pt; line-height:1.5; color:#3f4855; }
.c-bigidea{ position:relative; border-left:3px solid var(--accent); background:var(--cream); padding:11px 15px 12px 15px; margin-top:12px; overflow:hidden; }
.c-bigidea .quo{ position:absolute; top:-12px; right:10px; font-family:'Playfair Display',serif; font-weight:800; font-size:54pt; color:var(--accent); opacity:.1; line-height:1; }
.c-bigidea .bl{ font-family:'Archivo',sans-serif; font-weight:700; letter-spacing:.18em; text-transform:uppercase; font-size:6.6pt; color:var(--accent); margin-bottom:4px; }
.c-bigidea p{ font-family:'Playfair Display',serif; font-size:11.5pt; line-height:1.4; color:var(--navy); position:relative; }
.c-pt{ display:flex; gap:0.32in; margin-top:13px; } .c-pt > div{ flex:1; }
.c-blabel{ font-family:'Archivo',sans-serif; font-weight:700; letter-spacing:.16em; text-transform:uppercase; font-size:7pt; color:var(--accent); margin-bottom:4px; }
.c-btext{ font-size:8.6pt; line-height:1.5; color:#46505c; }
.c-arc{ margin-top:15px; }
.c-arc-h{ font-family:'Archivo',sans-serif; font-weight:700; letter-spacing:.16em; text-transform:uppercase; font-size:7.6pt; color:var(--navy); border-top:2px solid var(--navy); padding-top:7px; margin-bottom:10px; display:flex; justify-content:space-between; }
.c-arc-h .fmt{ color:var(--accent); font-weight:600; letter-spacing:.1em; }
.sgrid{ display:grid; grid-template-columns:1fr 1fr; gap:11px 0.34in; }
.scell{ display:flex; gap:9px; align-items:baseline; }
.scell .sn{ font-family:'Playfair Display',serif; font-weight:800; font-size:11pt; color:var(--accent); width:15px; flex-shrink:0; }
.scell .st{ font-family:'Playfair Display',serif; font-weight:700; font-size:9.6pt; color:var(--navy); }
.scell .sd{ font-size:8pt; color:#697381; line-height:1.32; }
.c-comp{ margin-top:16px; }
.c-comp-h{ font-family:'Archivo',sans-serif; font-weight:700; letter-spacing:.16em; text-transform:uppercase; font-size:7.4pt; color:var(--navy); border-top:2px solid var(--navy); padding-top:7px; margin-bottom:8px; }
.chips{ display:flex; flex-wrap:wrap; gap:6px; }
.chip{ font-family:'Archivo',sans-serif; font-size:7.4pt; font-weight:500; letter-spacing:.04em; color:var(--navy); border:1px solid var(--line); border-radius:20px; padding:4px 10px; background:#fcfaf4; }
.c-extra{ display:flex; gap:0.34in; margin-top:14px; } .c-extra .m{ flex:1; }
.c-extra .ml{ font-family:'Archivo',sans-serif; font-weight:700; letter-spacing:.14em; text-transform:uppercase; font-size:6.6pt; color:var(--accent); margin-bottom:3px; }
.c-extra .mv{ font-size:8.2pt; line-height:1.4; color:#46505c; }
.c-glance{ display:flex; border:1px solid var(--line); margin-top:14px; }
.c-glance .g{ flex:1; padding:7px 8px; border-right:1px solid var(--line); }
.c-glance .g:last-child{ border-right:none; }
.c-glance .gl{ font-family:'Archivo',sans-serif; font-weight:700; letter-spacing:.12em; text-transform:uppercase; font-size:5.8pt; color:#9aa2ad; margin-bottom:3px; }
.c-glance .gv{ font-family:'Playfair Display',serif; font-size:9.4pt; color:var(--navy); line-height:1.1; }
.c-foot{ padding-top:14px; }
.c-scrip{ background:var(--navy); color:#f1ead9; padding:9px 13px; display:flex; align-items:center; gap:12px; }
.c-scrip .sl{ font-family:'Archivo',sans-serif; font-weight:700; letter-spacing:.16em; text-transform:uppercase; font-size:6.6pt; color:var(--gold); flex-shrink:0; }
.c-scrip .sv{ font-family:'Spectral',serif; font-size:8.8pt; color:#e7dfcc; }
.c-meta{ display:flex; gap:0.34in; margin-top:9px; } .c-meta .m{ flex:1; }
.c-meta .ml{ font-family:'Archivo',sans-serif; font-weight:700; letter-spacing:.14em; text-transform:uppercase; font-size:6.4pt; color:#9aa2ad; margin-bottom:2px; }
.c-meta .mv{ font-size:7.8pt; line-height:1.35; color:#46505c; }

/* LIBRARY */
.lib-cols{ columns:2; column-gap:0.4in; margin-top:12px; }
.libgroup{ break-inside:avoid; margin-bottom:11px; }
.libgroup h4{ font-family:'Archivo',sans-serif; font-weight:700; letter-spacing:.12em; text-transform:uppercase; font-size:7.6pt; color:var(--accent); padding-bottom:4px; border-bottom:1px solid var(--line); margin-bottom:5px; }
.libitem{ display:flex; align-items:baseline; gap:6px; padding:2.2px 0; }
.libitem .li-t{ font-family:'Spectral',serif; font-size:8.6pt; color:var(--navy); flex:1; }
.libitem .li-t.star{ font-weight:600; }
.libitem .li-star{ color:var(--gold); font-size:7pt; }
.libitem .li-tier{ font-family:'Archivo',sans-serif; font-size:5.8pt; font-weight:700; letter-spacing:.05em; color:#fff; background:#9aa2ad; border-radius:2px; padding:1px 3px; }
.libitem .li-tier.t1{ background:var(--accent); }
.lib-legend{ margin-top:8px; font-family:'Archivo',sans-serif; font-size:6.6pt; letter-spacing:.1em; text-transform:uppercase; color:#8a929d; display:flex; gap:16px; align-items:center; }
.lib-legend .lg-star{ color:var(--gold); }
"""

def _css(cfg): return _CSS.replace("%ACCENT%", cfg["accent"]).replace("%ACCENT2%", cfg["accent2"])

def _rhead(cfg, section):
    return (f'<div class="rhead"><span><span class="b">LIFETOGETHER</span> &nbsp;\u00b7&nbsp; {cfg["doc_title"]}</span>'
            f'<span>{section}</span></div>')
def _rfoot(cfg, page):
    return (f'<div class="rfoot"><span>{cfg["category"]} \u00b7 Campaign Catalog</span><span>Page {page}</span></div>')

def _page_overview(cfg):
    who = "".join(f'<div class="w"><div class="wt">{t}</div><div class="wd">{d}</div></div>' for t,d in cfg["who_needs"])
    o = cfg["outcomes"]; half=(len(o)+1)//2
    out_l="".join(f'<div class="o">{x}</div>' for x in o[:half]); out_r="".join(f'<div class="o">{x}</div>' for x in o[half:])
    uc="".join(f'<div class="u"><div class="ut">{t}</div><div class="ud">{d}</div></div>' for t,d in cfg["use_cases"])
    sb="".join(f'<div class="s"><div class="sn">{n}</div><div class="sl">{l}</div></div>' for n,l in cfg["stats"])
    return f"""
<div class="page">
  <div class="ov-band"><div class="frame"></div><div class="inner">
    <div class="brand">Lifetogether</div>
    <div class="doctype">The Campaign Library &nbsp;\u00b7&nbsp; Category Catalog &amp; Strategy Overview</div>
    <div class="ov-title">{cfg["category"]}</div>
    <div class="ov-sub">Campaign Catalog</div>
    <div class="ov-orn"><span class="ln"></span><span class="dot"></span></div>
    <div class="ov-pos">{cfg["positioning"]}</div>
  </div></div>
  <div class="ov-body">
    <div class="two">
      <div><div class="sec-label">Why This Category Matters</div><div class="sec-body">{cfg["why_matters"]}</div></div>
      <div><div class="sec-label">The Core Problem</div><div class="sec-body">{cfg["core_problem"]}</div>
        <div class="sec-label mt">The Transformation</div><div class="sec-body">{cfg["transformation"]}</div></div>
    </div>
    <div class="sec-label mt">Who Needs This</div><div class="who">{who}</div>
    <div class="two mt">
      <div><div class="sec-label">Key Outcomes</div><div class="cols2"><div class="outlist">{out_l}</div><div class="outlist">{out_r}</div></div></div>
      <div><div class="sec-label">Sample Use Cases</div><div class="uc">{uc}</div></div>
    </div>
    <div class="statband">{sb}</div>
  </div>
</div>"""

def _page_top10(cfg):
    rows=""
    for c in cfg["top10"]:
        rows+=(f'<div class="row"><div class="rn">{c["n"]}<div class="rn-rule"></div></div>'
               f'<div class="rmid"><div class="rt">{c["title"]}</div>'
               f'<div class="rp">{c["pos"]}</div><div class="rs">{c["summary"]}</div></div>'
               f'<div class="rmeta"><div class="rfelt">{c["felt"]}</div><div class="raud">{c["aud"]}</div></div></div>')
    return f"""
<div class="page">{_rhead(cfg,"Top 10 \u00b7 At a Glance")}
  <div class="pad"><div class="ptitle">The Top 10 <em>{cfg["category"]}</em> Campaigns</div>
    <div class="psub">The ten strongest, most-requested campaigns in the {cfg["category"]} category \u2014 each expanded, one per page, on the spreads that follow. The complete 100-campaign library appears at the back of this catalog.</div>
    <div class="t10">{rows}</div>
    <div class="t10-foot">Every campaign is available in 4-session, 21-day, 30-day, and 40-day formats. All Scripture is NIV.</div>
  </div>{_rfoot(cfg,2)}</div>"""

def _page_campaign(cfg, c, page):
    sg=""
    for i,(st,sd) in enumerate(c["sessions"],1):
        sg+=f'<div class="scell"><div class="sn">{i}</div><div><div class="st">{st}</div><div class="sd">{sd}</div></div></div>'
    chips="".join(f'<span class="chip">{x}</span>' for x in cfg["components"])
    outcomes="  \u00b7  ".join(c["outcomes"])
    return f"""
<div class="page">{_rhead(cfg,f"Expanded Campaign {c['n']} of 10")}
  <div class="cnum">{c['n']}</div>
  <div class="pad flex">
    <div class="c-kick">{cfg["category"]} &nbsp;\u00b7&nbsp; Campaign {c['n']} &nbsp;\u00b7&nbsp; {cfg.get("tier","Tier 1")}</div>
    <div class="c-title">{c['title']}</div>
    <div class="c-pos">{c['pos']}</div>
    <div class="c-rule"></div>
    <div class="c-mkt">{c['marketing']}</div>
    <div class="c-bigidea"><div class="quo">\u201d</div><div class="bl">The Big Idea</div><p>{c['bigidea']}</p></div>
    <div class="grow"></div>
    <div class="c-pt">
      <div><div class="c-blabel">The Core Problem</div><div class="c-btext">{c['problem']}</div></div>
      <div><div class="c-blabel">The Transformation Promise</div><div class="c-btext">{c['transformation']}</div></div>
    </div>
    <div class="grow"></div>
    <div class="c-arc"><div class="c-arc-h"><span>The 6-Session Arc</span><span class="fmt">Expandable &amp; Flexible</span></div>
      <div class="sgrid">{sg}</div></div>
    <div class="grow"></div>
    <div class="c-comp"><div class="c-comp-h">Campaign Components</div><div class="chips">{chips}</div></div>
    <div class="c-extra"><div class="m"><div class="ml">Key Outcomes</div><div class="mv">{outcomes}</div></div></div>
    <div class="c-extra" style="margin-top:11px;">
      <div class="m"><div class="ml">Ideal For</div><div class="mv">{c['ideal']}</div></div>
      <div class="m"><div class="ml">Pairs Well With</div><div class="mv">{c['pairs']}</div></div></div>
    <div class="c-glance">
      <div class="g"><div class="gl">Primary Format</div><div class="gv">40-Day Campaign</div></div>
      <div class="g"><div class="gl">Sessions</div><div class="gv">6 Sessions</div></div>
      <div class="g"><div class="gl">Felt Need</div><div class="gv">{c['felt']}</div></div>
      <div class="g"><div class="gl">Audience</div><div class="gv">{c['aud']}</div></div></div>
    <div class="grow"></div>
    <div class="c-foot"><div class="c-scrip"><span class="sl">Key Scriptures</span><span class="sv">{c['scriptures']}</span></div>
      <div class="c-meta">
        <div class="m"><div class="ml">Intended Audience</div><div class="mv">{c['aud_full']}</div></div>
        <div class="m"><div class="ml">Format Flexibility</div><div class="mv">{c['formats']}</div></div></div></div>
  </div>{_rfoot(cfg,page)}</div>"""

def _lib_group(name, items):
    rows=""
    for (t,tier,star) in items:
        sh='<span class="li-star">\u2605</span>' if star else ''
        rows+=(f'<div class="libitem"><span class="li-t {"star" if star else ""}">{t}</span>{sh}'
               f'<span class="li-tier {"t1" if tier=="T1" else ""}">{tier}</span></div>')
    return f'<div class="libgroup"><h4>{name}</h4>{rows}</div>'

def _page_library(cfg, groups, page, part, total):
    blocks="".join(_lib_group(n,it) for n,it in groups)
    suffix="" if total==1 else f" <span style='font-size:11pt;color:#9aa2ad'>(Part {part} of {total})</span>"
    legend=('<div class="lib-legend"><span><span class="lg-star">\u2605</span> Expanded in this catalog</span>'
            '<span><b style="color:%s">T1</b> Tier 1 &nbsp; <b>T2</b> Tier 2</span><span>100 Campaigns \u00b7 10 Themes</span></div>')%cfg["accent"]
    return f"""
<div class="page">{_rhead(cfg,"Complete Category Library")}
  <div class="pad"><div class="ptitle">The Complete <em>{cfg["category"]}</em> Library{suffix}</div>
    <div class="psub">All 100 campaign opportunities in the {cfg["category"]} category, organized by theme. The ten starred titles are expanded earlier in this catalog; every title is available for full development.</div>
    {legend}<div class="lib-cols">{blocks}</div></div>{_rfoot(cfg,page)}</div>"""

def build_catalog(cfg):
    pages=_page_overview(cfg)+_page_top10(cfg)
    pg=3
    for c in cfg["top10"]:
        pages+=_page_campaign(cfg,c,pg); pg+=1
    lib=cfg["library"]; lib1=lib[:5]; lib2=lib[5:]
    pages+=_page_library(cfg,lib1,pg,1,2); pg+=1
    pages+=_page_library(cfg,lib2,pg,2,2); pg+=1
    doc=f"""<!DOCTYPE html><html lang="en"><head><meta charset="utf-8">
<title>{cfg["doc_title"]} \u2014 Lifetogether</title>
<style>{FONTS}</style><style>{_css(cfg)}</style></head><body>{pages}</body></html>"""
    return doc, pg-1

def render_pdf(html_path, pdf_path):
    from playwright.sync_api import sync_playwright
    with sync_playwright() as p:
        b=p.chromium.launch(); pg=b.new_page()
        pg.goto("file://"+html_path, wait_until="networkidle"); pg.emulate_media(media="print")
        pg.pdf(path=pdf_path, prefer_css_page_size=True, print_background=True, width="8.5in", height="11in")
        b.close()
