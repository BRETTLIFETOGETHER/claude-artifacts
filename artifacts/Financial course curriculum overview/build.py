# -*- coding: utf-8 -*-
"""Finances Campaign Catalog — HTML build + Playwright PDF render."""
import base64, pathlib, re
from data_top10_a import TOP10_A
from data_top10_b import TOP10_B
from data_library import OVERVIEW, LIBRARY, GROUPS

TOP10 = TOP10_A + TOP10_B
FONTS = pathlib.Path('fonts')

def b64(p): return base64.b64encode((FONTS/p).read_bytes()).decode()
def esc(s):
    return (str(s).replace('&','&amp;').replace('<','&lt;').replace('>','&gt;'))

# ---------------------------------------------------------------- fonts
FONT_CSS = f"""
@font-face{{font-family:'Playfair';src:url(data:font/ttf;base64,{b64('PlayfairDisplay.ttf')}) format('truetype');font-weight:400 900;font-style:normal;}}
@font-face{{font-family:'Playfair';src:url(data:font/ttf;base64,{b64('PlayfairDisplay-Italic.ttf')}) format('truetype');font-weight:400 900;font-style:italic;}}
@font-face{{font-family:'Spectral';src:url(data:font/ttf;base64,{b64('Spectral-Regular.ttf')}) format('truetype');font-weight:400;font-style:normal;}}
@font-face{{font-family:'Spectral';src:url(data:font/ttf;base64,{b64('Spectral-Medium.ttf')}) format('truetype');font-weight:500;font-style:normal;}}
@font-face{{font-family:'Spectral';src:url(data:font/ttf;base64,{b64('Spectral-SemiBold.ttf')}) format('truetype');font-weight:600;font-style:normal;}}
@font-face{{font-family:'Spectral';src:url(data:font/ttf;base64,{b64('Spectral-Italic.ttf')}) format('truetype');font-weight:400;font-style:italic;}}
@font-face{{font-family:'Spectral';src:url(data:font/ttf;base64,{b64('Spectral-MediumItalic.ttf')}) format('truetype');font-weight:500;font-style:italic;}}
@font-face{{font-family:'Archivo';src:url(data:font/ttf;base64,{b64('Archivo.ttf')}) format('truetype');font-weight:100 900;font-style:normal;}}
"""

def sprig(color, w=34, op=0.95):
    return (f'<svg viewBox="0 0 40 64" width="{w}" xmlns="http://www.w3.org/2000/svg" '
            f'style="display:block">'
            f'<path d="M20 62 C20 44 20 26 20 6" stroke="{color}" stroke-width="1.3" '
            f'stroke-linecap="round" fill="none" opacity="{op}"/>'
            f'<g fill="{color}" opacity="{op}">'
            f'<ellipse cx="12.5" cy="19" rx="6.6" ry="3.1" transform="rotate(-34 12.5 19)"/>'
            f'<ellipse cx="27.5" cy="26" rx="6.6" ry="3.1" transform="rotate(34 27.5 26)"/>'
            f'<ellipse cx="12.5" cy="33" rx="6.1" ry="2.9" transform="rotate(-34 12.5 33)"/>'
            f'<ellipse cx="27.5" cy="40" rx="6.1" ry="2.9" transform="rotate(34 27.5 40)"/>'
            f'<ellipse cx="20" cy="7.5" rx="4.6" ry="2.6"/></g></svg>')

# ---------------------------------------------------------------- CSS
CSS = """
*{margin:0;padding:0;box-sizing:border-box;}
:root{
 --ink:#0b1726; --ink2:#17283b; --body:#34414e;
 --gold:#c9a35c; --gold-deep:#9c7b2e; --gold-pale:#efe2c4;
 --ever:#1d4334; --ever2:#2f5c47; --ever-pale:#e8efe9;
 --paper:#fbf8f1; --panel:#f4eddf; --panel2:#efe7d5;
 --muted:#7c7365; --line:rgba(11,23,38,.16); --line-soft:rgba(11,23,38,.08);
 --cream:#f6efe1;
}
html,body{background:#5a5a5a;}
.page{position:relative;width:8.5in;height:11in;overflow:hidden;background:var(--paper);
 color:var(--body);font-family:'Spectral',serif;font-size:10.5px;line-height:1.5;
 padding:0.72in 0.74in 0.6in;page-break-after:always;}
.page.last{page-break-after:auto;}
p{font-family:'Spectral',serif;}
.kicker{font-family:'Archivo',sans-serif;font-weight:700;letter-spacing:.2em;
 text-transform:uppercase;font-size:8.5px;color:var(--ever2);}
.kicker.gold{color:var(--gold-deep);}
.grule{height:2px;border:0;background:linear-gradient(90deg,var(--gold),var(--gold-deep) 70%,transparent);}
.hair{height:1px;background:var(--line);border:0;}
.pf{font-family:'Playfair',serif;}
.serif{font-family:'Spectral',serif;}
.pgnum{position:absolute;bottom:0.34in;right:0.74in;font-family:'Archivo',sans-serif;
 font-size:8px;letter-spacing:.16em;color:var(--muted);text-transform:uppercase;}
.foot-mark{position:absolute;bottom:0.32in;left:0.74in;font-family:'Archivo',sans-serif;
 font-size:8px;letter-spacing:.22em;color:var(--muted);text-transform:uppercase;}

/* ---- cover ---- */
.cover{background:var(--ink);color:var(--cream);padding:0;}
.cover .frame{position:absolute;inset:0.42in;border:1px solid rgba(201,163,92,.34);}
.cover .inner{position:absolute;inset:0;display:flex;flex-direction:column;
 align-items:center;justify-content:center;text-align:center;padding:1in 0.9in;}
.cover .topkick{position:absolute;top:0.92in;left:0;right:0;text-align:center;
 font-family:'Archivo',sans-serif;font-weight:700;letter-spacing:.42em;font-size:9.5px;
 color:var(--gold);text-transform:uppercase;}
.cover h1{font-family:'Playfair',serif;font-weight:800;font-size:74px;line-height:.98;
 color:#fff;letter-spacing:.01em;}
.cover .sub1{font-family:'Archivo',sans-serif;font-weight:600;letter-spacing:.34em;
 text-transform:uppercase;font-size:13px;color:var(--gold);margin-top:14px;}
.cover .rule{width:120px;height:2px;background:linear-gradient(90deg,transparent,var(--gold),transparent);
 margin:26px auto;}
.cover .blurb{font-family:'Spectral',serif;font-style:italic;font-size:14.5px;line-height:1.62;
 color:#d9e0e6;max-width:5.1in;margin:0 auto;}
.cover .count{margin-top:30px;font-family:'Archivo',sans-serif;font-weight:700;font-size:10px;
 letter-spacing:.28em;text-transform:uppercase;color:var(--ink);background:var(--gold);
 padding:9px 20px;border-radius:2px;display:inline-block;}
.cover .wm{position:absolute;bottom:1.0in;left:0;right:0;text-align:center;}
.cover .wm .lt{font-family:'Playfair',serif;font-weight:700;font-size:18px;color:#fff;letter-spacing:.02em;}
.cover .wm .tag{font-family:'Archivo',sans-serif;font-weight:600;letter-spacing:.32em;
 font-size:8px;text-transform:uppercase;color:var(--gold);margin-top:6px;}
.cover .sprigwrap{margin:0 auto 4px;width:34px;}

/* ---- generic heading block ---- */
.head{display:flex;justify-content:space-between;align-items:flex-end;}
.head .ttl{font-family:'Playfair',serif;font-weight:800;color:var(--ink);font-size:30px;line-height:1.04;}
.page-intro{font-family:'Spectral',serif;font-size:11px;line-height:1.62;color:var(--body);}

/* ---- overview ---- */
.ov-lede{font-family:'Spectral',serif;font-style:italic;font-size:14px;line-height:1.62;
 color:var(--ink2);}
.ov-h{font-family:'Playfair',serif;font-weight:700;color:var(--ever);font-size:14.5px;margin-bottom:5px;}
.ov-body{font-size:10.4px;line-height:1.62;color:var(--body);}
.pullquote{background:var(--ever);color:var(--cream);padding:18px 22px;border-radius:3px;
 font-family:'Playfair',serif;font-style:italic;font-size:15px;line-height:1.5;}
.pullquote .src{font-family:'Archivo',sans-serif;font-style:normal;font-weight:600;
 letter-spacing:.18em;font-size:8px;text-transform:uppercase;color:var(--gold-pale);margin-top:9px;}
.aud-grid{display:grid;grid-template-columns:1fr 1fr;gap:11px;}
.aud-card{background:var(--panel);border-left:2.5px solid var(--gold);padding:11px 13px;border-radius:2px;}
.aud-card h4{font-family:'Playfair',serif;font-weight:700;color:var(--ink);font-size:12.5px;margin-bottom:4px;}
.aud-card p{font-size:9.4px;line-height:1.5;color:var(--body);}
.out-list{list-style:none;}
.out-list li{position:relative;padding-left:18px;margin-bottom:7px;font-size:10.2px;line-height:1.5;}
.out-list li:before{content:"";position:absolute;left:0;top:6px;width:7px;height:7px;
 background:var(--gold);transform:rotate(45deg);}

/* ---- top10 overview rows ---- */
.t10row{display:flex;gap:13px;align-items:flex-start;padding:5px 0;border-top:1px solid var(--line-soft);}
.t10row:first-of-type{border-top:0;}
.t10num{font-family:'Playfair',serif;font-weight:800;color:var(--ever);font-size:25px;
 line-height:1;width:0.48in;flex:none;text-align:right;}
.t10body{flex:1;}
.t10body .tt{font-family:'Playfair',serif;font-weight:700;color:var(--ink);font-size:14px;line-height:1.05;}
.t10body .tg{font-family:'Spectral',serif;font-style:italic;color:var(--ever2);font-size:9.4px;margin-top:1px;}
.t10body .hk{font-size:9.2px;line-height:1.36;color:var(--body);margin-top:2.5px;}
.t10meta{font-family:'Archivo',sans-serif;font-size:7.4px;letter-spacing:.06em;color:var(--muted);
 text-transform:uppercase;margin-top:2.5px;}
.t10meta b{color:var(--ever2);font-weight:700;}

/* ---- campaign overview page ---- */
.c-top{display:flex;justify-content:space-between;align-items:center;margin-bottom:4px;}
.badge{font-family:'Archivo',sans-serif;font-weight:700;letter-spacing:.14em;font-size:7.6px;
 text-transform:uppercase;padding:4px 9px;border-radius:2px;}
.badge.t1{background:var(--ever);color:var(--cream);}
.badge.t2{background:var(--gold);color:var(--ink);}
.c-title{font-family:'Playfair',serif;font-weight:800;color:var(--ink);font-size:33px;line-height:1.02;}
.c-tag{font-family:'Spectral',serif;font-style:italic;color:var(--ever2);font-size:13px;margin-top:3px;}
.scrip{background:var(--ever);color:var(--cream);padding:13px 18px;border-radius:3px;
 display:flex;gap:14px;align-items:flex-start;}
.scrip .q{font-family:'Spectral',serif;font-style:italic;font-size:11.6px;line-height:1.5;flex:1;}
.scrip .r{font-family:'Archivo',sans-serif;font-weight:700;letter-spacing:.12em;font-size:8px;
 text-transform:uppercase;color:var(--gold-pale);white-space:nowrap;padding-top:2px;}
.c-lead{font-size:10.6px;line-height:1.62;color:var(--body);}
.info2{display:grid;grid-template-columns:1fr 1fr;gap:10px;}
.info-card{background:var(--panel);border-radius:2px;padding:10px 12px;border-top:2px solid var(--gold);}
.info-card .lab{font-family:'Archivo',sans-serif;font-weight:700;letter-spacing:.16em;font-size:7.4px;
 text-transform:uppercase;color:var(--ever2);margin-bottom:4px;}
.info-card p{font-size:9.6px;line-height:1.48;color:var(--body);}
.sec-h{font-family:'Archivo',sans-serif;font-weight:700;letter-spacing:.18em;font-size:8.4px;
 text-transform:uppercase;color:var(--ink);display:flex;align-items:center;gap:9px;}
.sec-h:after{content:"";flex:1;height:1px;background:var(--line);}
.sess-grid{display:grid;grid-template-columns:1fr 1fr;gap:7px 16px;}
.sess{display:flex;gap:8px;}
.sess .n{font-family:'Playfair',serif;font-weight:800;color:var(--ever);font-size:14px;
 line-height:1;width:14px;flex:none;}
.sess .st{font-family:'Spectral',serif;font-weight:600;color:var(--ink);font-size:9.8px;line-height:1.2;}
.sess .sd{font-family:'Spectral',serif;font-style:italic;color:var(--muted);font-size:8.6px;line-height:1.3;}
.foot-row{display:flex;justify-content:space-between;align-items:center;gap:14px;}
.pills{display:flex;gap:6px;flex-wrap:wrap;}
.pill{font-family:'Archivo',sans-serif;font-weight:600;font-size:7.6px;letter-spacing:.08em;
 text-transform:uppercase;border:1px solid var(--gold);color:var(--gold-deep);
 padding:3px 8px;border-radius:10px;}
.aud-line{font-family:'Archivo',sans-serif;font-size:8px;letter-spacing:.06em;color:var(--muted);
 text-transform:uppercase;text-align:right;}

/* ---- 40-day map ---- */
.map-cols{display:grid;grid-template-columns:1fr 1fr;gap:0 22px;}
.mv{margin-bottom:8px;break-inside:avoid;}
.mv-h{display:flex;gap:8px;align-items:baseline;border-bottom:1px solid var(--gold);
 padding-bottom:3px;margin-bottom:5px;}
.mv-rom{font-family:'Playfair',serif;font-weight:800;color:var(--gold-deep);font-size:13px;line-height:1;}
.mv-t{font-family:'Archivo',sans-serif;font-weight:700;letter-spacing:.1em;font-size:8.4px;
 text-transform:uppercase;color:var(--ink);}
.mv-s{font-family:'Spectral',serif;font-style:italic;color:var(--muted);font-size:8px;margin-left:auto;}
.day{display:flex;gap:7px;margin-bottom:3.5px;}
.day .dn{font-family:'Archivo',sans-serif;font-weight:800;color:#fff;background:var(--ever2);
 font-size:7px;letter-spacing:.02em;border-radius:2px;padding:2px 0;width:23px;flex:none;
 text-align:center;height:13px;}
.day .dx{flex:1;}
.day .dt{font-family:'Spectral',serif;font-weight:600;color:var(--ink);font-size:9px;line-height:1.18;}
.day .ds{font-family:'Spectral',serif;font-style:italic;color:var(--body);font-size:7.8px;line-height:1.2;}
.day .dr{font-family:'Archivo',sans-serif;color:var(--ever2);font-size:7px;letter-spacing:.02em;
 font-weight:600;margin-top:.5px;}

/* ---- library index ---- */
.lib-cols{column-count:2;column-gap:24px;}
.lib-group{break-inside:avoid;margin-bottom:9px;}
.lib-gh{display:flex;align-items:baseline;gap:8px;border-bottom:1.5px solid var(--ever);
 padding-bottom:3px;margin-bottom:6px;}
.lib-gh .gt{font-family:'Playfair',serif;font-weight:700;color:var(--ever);font-size:12px;}
.lib-gh .gc{font-family:'Archivo',sans-serif;font-weight:700;font-size:7.4px;letter-spacing:.1em;
 color:var(--gold-deep);margin-left:auto;text-transform:uppercase;}
.lib-e{break-inside:avoid;margin-bottom:6px;}
.lib-e .l1{display:flex;gap:6px;align-items:baseline;}
.lib-e .ln{font-family:'Archivo',sans-serif;font-weight:700;color:var(--muted);font-size:7.6px;
 width:15px;flex:none;}
.lib-e .lt{font-family:'Spectral',serif;font-weight:600;color:var(--ink);font-size:9.6px;line-height:1.18;}
.lib-e .star{color:var(--gold-deep);font-size:8px;}
.lib-e .lh{font-family:'Spectral',serif;font-style:italic;color:var(--body);font-size:8.2px;
 line-height:1.32;margin:1px 0 0 21px;
 display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden;}
.lib-e .lm{font-family:'Archivo',sans-serif;font-size:6.6px;letter-spacing:.05em;color:var(--muted);
 margin:1px 0 0 21px;text-transform:uppercase;}

/* ---- closing ---- */
.cta{background:var(--ever);color:var(--cream);border-radius:4px;padding:26px 30px;}
.cta h2{font-family:'Playfair',serif;font-weight:800;color:#fff;font-size:26px;line-height:1.05;}
.cta p{font-family:'Spectral',serif;font-size:11px;line-height:1.62;color:#dfe7e0;margin-top:10px;}
.use{margin-top:6px;}
.use-item{display:flex;gap:11px;padding:8px 0;border-top:1px solid var(--line-soft);}
.use-item:first-child{border-top:0;}
.use-item .ut{font-family:'Spectral',serif;font-weight:600;color:var(--ink);font-size:10.4px;
 width:1.85in;flex:none;}
.use-item .ud{font-size:9.6px;line-height:1.46;color:var(--body);}
.disc{background:var(--panel);border-radius:3px;padding:12px 15px;}
.disc .lab{font-family:'Archivo',sans-serif;font-weight:700;letter-spacing:.16em;font-size:7.4px;
 text-transform:uppercase;color:var(--ever2);margin-bottom:4px;}
.disc p{font-size:8.8px;line-height:1.5;color:var(--muted);}
.endwm{text-align:center;}
.endwm .lt{font-family:'Playfair',serif;font-weight:700;color:var(--ink);font-size:17px;}
.endwm .tag{font-family:'Archivo',sans-serif;font-weight:600;letter-spacing:.3em;font-size:7.6px;
 text-transform:uppercase;color:var(--gold-deep);margin-top:5px;}
.spacer{flex:1;}
.col{display:flex;flex-direction:column;height:100%;}
"""

# ---------------------------------------------------------------- page builders
def cover_page():
    return f"""<div class="page cover">
  <div class="frame"></div>
  <div class="topkick">{esc(OVERVIEW['kicker'])}</div>
  <div class="inner">
    <div class="sprigwrap">{sprig('#c9a35c',34)}</div>
    <h1>Finances</h1>
    <div class="sub1">Campaign Catalog</div>
    <div class="rule"></div>
    <div class="blurb">{esc(OVERVIEW['subtitle'])}</div>
    <div class="count">100 Campaign Opportunities</div>
  </div>
  <div class="wm">
    <div class="lt">LifeTogether</div>
    <div class="tag">Churchwide &amp; Workplace Campaigns</div>
  </div>
</div>"""

def overview_page_1(pg):
    return f"""<div class="page">
  <div class="kicker gold">{esc(OVERVIEW['kicker'])}</div>
  <hr class="grule" style="margin:7px 0 14px;">
  <h1 class="pf" style="font-size:46px;font-weight:800;color:var(--ink);line-height:1;">The Finances Category</h1>
  <p class="ov-lede" style="margin:14px 0 16px;">{esc(OVERVIEW['lede'])}</p>
  <div style="display:grid;grid-template-columns:1.55fr 1fr;gap:24px;align-items:start;">
    <div>
      <div class="ov-h">A Subject the Church Cannot Afford to Avoid</div>
      <p class="ov-body" style="margin-bottom:13px;">{esc(OVERVIEW['positioning'])}</p>
      <div class="ov-h">Why This Matters Now</div>
      <p class="ov-body">{esc(OVERVIEW['why_now'])}</p>
    </div>
    <div>
      <div class="pullquote">
        Jesus spoke about money more than almost any other subject — not because He wanted our resources, but because He wanted our hearts.
        <div class="src">The Heart of This Catalog</div>
      </div>
      <div style="margin-top:18px;text-align:center;">{sprig('#1d4334',30)}</div>
    </div>
  </div>
  <hr class="hair" style="margin:18px 0 14px;">
  <div style="display:grid;grid-template-columns:1fr 1fr;gap:24px;">
    <div>
      <div class="ov-h" style="color:var(--ink);">The Core Problem</div>
      <p class="ov-body">{esc(OVERVIEW['problem'])}</p>
    </div>
    <div>
      <div class="ov-h" style="color:var(--ever);">The Transformation</div>
      <p class="ov-body">{esc(OVERVIEW['transformation'])}</p>
    </div>
  </div>
  <div class="foot-mark">LifeTogether · Finances Campaign Catalog</div>
  <div class="pgnum">{pg:02d}</div>
</div>"""

def overview_page_2(pg):
    auds = "".join(
        f'<div class="aud-card"><h4>{esc(t)}</h4><p>{esc(d)}</p></div>'
        for t,d in OVERVIEW['audiences'])
    outs = "".join(f'<li>{esc(o)}</li>' for o in OVERVIEW['outcomes'])
    return f"""<div class="page">
  <div class="kicker gold">Who It Serves · What Changes</div>
  <hr class="grule" style="margin:7px 0 16px;">
  <h1 class="pf" style="font-size:30px;font-weight:800;color:var(--ink);">Built for Your Church — and Your Workplace</h1>
  <p class="page-intro" style="margin:10px 0 16px;">These campaigns are designed to flex across the settings where money pressure is most real, uniting weekend teaching, small-group community, and daily devotional rhythm around a single transformative theme.</p>
  <div class="aud-grid" style="margin-bottom:18px;">{auds}</div>
  <hr class="hair" style="margin:4px 0 16px;">
  <div style="display:grid;grid-template-columns:1.15fr 1fr;gap:26px;align-items:start;">
    <div>
      <div class="sec-h" style="margin-bottom:11px;">What Changes in Your People</div>
      <ul class="out-list">{outs}</ul>
    </div>
    <div>
      <div class="pullquote" style="background:var(--ink);">
        From owner to steward. From fear to peace. From debt to freedom. From scarcity to generosity. From never-enough to genuinely enough.
        <div class="src">The Finances Arc</div>
      </div>
      <p class="ov-body" style="margin-top:14px;">Every campaign in the library that follows is built to move people somewhere specific along that arc — through Scripture, honest community, and grace rather than guilt or gimmicks.</p>
    </div>
  </div>
  <div class="foot-mark">LifeTogether · Finances Campaign Catalog</div>
  <div class="pgnum">{pg:02d}</div>
</div>"""

def top10_overview_page(pg):
    rows = ""
    for c in TOP10:
        rows += f"""<div class="t10row">
      <div class="t10num">{c['num']:02d}</div>
      <div class="t10body">
        <div class="tt">{esc(c['title'])}</div>
        <div class="tg">{esc(c['tagline'])}</div>
        <div class="hk">{esc(c['positioning'])}</div>
        <div class="t10meta"><b>Felt need:</b> {esc(c['felt_need'])}</div>
      </div>
    </div>"""
    return f"""<div class="page">
  <div class="kicker gold">The Flagship Campaigns</div>
  <hr class="grule" style="margin:6px 0 9px;">
  <div class="head">
    <h1 class="ttl" style="font-size:27px;">The Top 10 Campaigns</h1>
    <div style="font-family:'Archivo';font-size:8px;letter-spacing:.2em;text-transform:uppercase;color:var(--muted);text-align:right;">Fully expanded<br>on the pages that follow</div>
  </div>
  <p class="page-intro" style="margin:6px 0 4px;">Ten flagship journeys, each presented in full on the following pages — complete positioning, a six-session small-group outline, and a day-by-day 40-day devotional map.</p>
  {rows}
  <div class="foot-mark">LifeTogether · Finances Campaign Catalog</div>
  <div class="pgnum">{pg:02d}</div>
</div>"""

def campaign_overview_page(c, pg):
    tier_t2 = c['tier'].startswith('Tier 2')
    badge_cls = 't2' if tier_t2 else 't1'
    formats = "".join(f'<span class="pill">{esc(f)}</span>' for f in c['formats'])
    info = [
        ("The Felt Need", c['felt_need']),
        ("Why It Matters", c['why_matters']),
        ("The Core Problem", c['problem']),
        ("The Transformation", c['transformation']),
    ]
    info_html = "".join(
        f'<div class="info-card"><div class="lab">{esc(l)}</div><p>{esc(v)}</p></div>'
        for l,v in info)
    sess = ""
    for i,(st,sd) in enumerate(c['sessions'],1):
        sess += (f'<div class="sess"><div class="n">{i}</div><div>'
                 f'<div class="st">{esc(st)}</div><div class="sd">{esc(sd)}</div></div></div>')
    return f"""<div class="page">
  <div class="c-top">
    <div class="kicker gold">Flagship Campaign &nbsp;·&nbsp; N<sup>o</sup> {c['num']:02d}</div>
    <span class="badge {badge_cls}">{esc(c['tier'])}</span>
  </div>
  <hr class="grule" style="margin:6px 0 12px;">
  <h1 class="c-title">{esc(c['title'])}</h1>
  <div class="c-tag">{esc(c['tagline'])}</div>
  <div class="scrip" style="margin:13px 0 13px;">
    <div class="q">&ldquo;{esc(c['core_text'])}&rdquo;</div>
    <div class="r">{esc(c['core_ref'])}</div>
  </div>
  <p class="c-lead" style="margin-bottom:13px;">{esc(c['marketing'])}</p>
  <div class="info2" style="margin-bottom:14px;">{info_html}</div>
  <div class="sec-h" style="margin-bottom:9px;">The Six-Session Small-Group Journey</div>
  <div class="sess-grid" style="margin-bottom:14px;">{sess}</div>
  <hr class="hair" style="margin:0 0 11px;">
  <div class="foot-row">
    <div>
      <div style="font-family:'Archivo';font-weight:700;letter-spacing:.16em;font-size:7.2px;text-transform:uppercase;color:var(--ever2);margin-bottom:5px;">Available Formats</div>
      <div class="pills">{formats}</div>
    </div>
    <div class="aud-line">{esc(c['audience'])}</div>
  </div>
  <div class="foot-mark">LifeTogether · Finances Campaign Catalog</div>
  <div class="pgnum">{pg:02d}</div>
</div>"""

def campaign_map_page(c, pg):
    cols = [c['movements'][:3], c['movements'][3:]]
    def render_mv(mv):
        days = ""
        for (n,t,s,r) in mv['days']:
            days += (f'<div class="day"><div class="dn">{n:02d}</div><div class="dx">'
                     f'<div class="dt">{esc(t)}</div>'
                     f'<div class="ds">{esc(s)}</div>'
                     f'<div class="dr">{esc(r)}</div></div></div>')
        return (f'<div class="mv"><div class="mv-h">'
                f'<div class="mv-rom">{esc(mv["roman"])}</div>'
                f'<div class="mv-t">{esc(mv["title"])}</div>'
                f'<div class="mv-s">{esc(mv["subtitle"])}</div></div>{days}</div>')
    colA = "".join(render_mv(m) for m in cols[0])
    colB = "".join(render_mv(m) for m in cols[1])
    return f"""<div class="page">
  <div class="c-top">
    <div class="kicker gold">The 40-Day Devotional Journey</div>
    <div style="font-family:'Playfair';font-style:italic;color:var(--ever2);font-size:12px;">{esc(c['title'])}</div>
  </div>
  <hr class="grule" style="margin:6px 0 5px;">
  <p style="font-family:'Spectral';font-style:italic;color:var(--muted);font-size:9px;margin-bottom:11px;">
    Forty days, grouped into six movements that align with the small-group sessions. Each day carries a title, a one-line focus, and the Scriptures that anchor it.</p>
  <div class="map-cols">
    <div>{colA}</div>
    <div>{colB}</div>
  </div>
  <div class="foot-mark">LifeTogether · Finances Campaign Catalog</div>
  <div class="pgnum">{pg:02d}</div>
</div>"""

def library_pages(start_pg):
    # group -> entries (sorted by num)
    by_group = {g:[] for g in GROUPS}
    for e in LIBRARY:
        by_group[e['group']].append(e)
    for g in by_group:
        by_group[g].sort(key=lambda x:x['num'])
    # manual page distribution (balanced, groups intact)
    layout = [
        ["Foundations & Stewardship","Fear, Anxiety & Peace","Debt & Financial Freedom"],
        ["Budgeting & Order","Generosity & Giving","Contentment & Simplicity"],
        ["Provision & Trust","Wisdom, Saving & Investing","Work, Income & Calling","Money & the Heart"],
        ["Marriage & Family","Seasons & Life Stages","Workplace & Marketplace","Signature Short Formats"],
    ]
    def render_group(g):
        ents = ""
        for e in by_group[g]:
            star = ' <span class="star">&#9670;</span>' if e['top10'] else ''
            tag = "Flagship · " if e['top10'] else ""
            ents += (f'<div class="lib-e"><div class="l1">'
                     f'<div class="ln">{e["num"]:02d}</div>'
                     f'<div class="lt">{esc(e["title"])}{star}</div></div>'
                     f'<div class="lh">{esc(e["hook"])}</div>'
                     f'<div class="lm">{tag}{esc(e["tier"])}</div></div>')
        return (f'<div class="lib-group"><div class="lib-gh">'
                f'<div class="gt">{esc(g)}</div>'
                f'<div class="gc">{len(by_group[g])} Campaigns</div></div>{ents}</div>')
    pages = []
    total = len(layout)
    for i,groups in enumerate(layout):
        pg = start_pg + i
        body = "".join(render_group(g) for g in groups)
        roman = ["I","II","III","IV"][i]
        pages.append(f"""<div class="page">
  <div class="kicker gold">The Complete Library &nbsp;·&nbsp; 100 Campaigns &nbsp;·&nbsp; Part {roman} of IV</div>
  <hr class="grule" style="margin:7px 0 12px;">
  <div class="head" style="margin-bottom:12px;">
    <h1 class="ttl" style="font-size:27px;">{'The Complete Campaign Library' if i==0 else 'Campaign Library, continued'}</h1>
  </div>
  {('<p class="page-intro" style="margin:-4px 0 13px;">One hundred distinct campaign concepts across fourteen thematic collections. The ten flagship campaigns (&#9670;) are fully expanded on the preceding pages; every concept is available as a 4-session, 6-session, 21-day, 30-day, or 40-day experience.</p>' if i==0 else '')}
  <div class="lib-cols">{body}</div>
  <div class="foot-mark">LifeTogether · Finances Campaign Catalog</div>
  <div class="pgnum">{pg:02d}</div>
</div>""")
    return pages

def closing_page(pg):
    uses = "".join(
        f'<div class="use-item"><div class="ut">{esc(t)}</div><div class="ud">{esc(d)}</div></div>'
        for t,d in OVERVIEW['use_cases'])
    return f"""<div class="page last">
  <div class="kicker gold">Bring a Campaign to Your People</div>
  <hr class="grule" style="margin:7px 0 16px;">
  <div class="cta">
    <h2>{esc(OVERVIEW['cta_title'])}</h2>
    <p>{esc(OVERVIEW['cta_body'])}</p>
  </div>
  <div class="sec-h" style="margin:20px 0 6px;">Ways Churches &amp; Workplaces Use This Catalog</div>
  <div class="use">{uses}</div>
  <div style="margin:18px 0 16px;" class="disc">
    <div class="lab">A Note of Care</div>
    <p>These campaigns offer biblical and spiritual principles for handling money, fear, and stress — they are not professional financial, legal, tax, or mental-health advice. For personal financial decisions or for anxiety, grief, or stress that feels overwhelming, we warmly encourage participants to seek a qualified advisor and the support of a pastor, counselor, or trusted professional.</p>
  </div>
  <hr class="hair" style="margin:6px 0 18px;">
  <div class="endwm">
    <div style="margin:0 auto 6px;width:30px;">{sprig('#1d4334',30)}</div>
    <div class="lt">LifeTogether</div>
    <div class="tag">Churchwide &amp; Workplace Campaigns</div>
  </div>
  <div class="foot-mark">LifeTogether · Finances Campaign Catalog</div>
  <div class="pgnum">{pg:02d}</div>
</div>"""

# ---------------------------------------------------------------- assemble
def build_html():
    pages = []
    pages.append(cover_page())                 # cover (unnumbered)
    pg = 2
    pages.append(overview_page_1(pg)); pg+=1
    pages.append(overview_page_2(pg)); pg+=1
    pages.append(top10_overview_page(pg)); pg+=1
    for c in TOP10:
        pages.append(campaign_overview_page(c, pg)); pg+=1
        pages.append(campaign_map_page(c, pg)); pg+=1
    lib = library_pages(pg); pages.extend(lib); pg+=len(lib)
    pages.append(closing_page(pg))
    body = "\n".join(pages)
    html = (f"<!DOCTYPE html><html><head><meta charset='utf-8'>"
            f"<style>{FONT_CSS}{CSS}</style></head><body>{body}</body></html>")
    return html, len(pages)

if __name__ == "__main__":
    html, npages = build_html()
    out = pathlib.Path('catalog.html')
    out.write_text(html, encoding='utf-8')
    print(f"HTML written: {out} | pages composed: {npages} | size {len(html)//1024} KB")
