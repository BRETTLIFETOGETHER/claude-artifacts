# -*- coding: utf-8 -*-
import json, html
from content import COLLECTION, TITLES

with open("fonts_b64.json") as f:
    F = json.load(f)

def esc(s): return html.escape(s, quote=True)

# ---- color helpers ----------------------------------------------------------
def hex2rgb(h):
    h=h.lstrip('#'); return tuple(int(h[i:i+2],16) for i in (0,2,4))
def rgb2hex(t): return '#%02x%02x%02x'%tuple(max(0,min(255,int(round(x))))for x in t)
def mix(h, other, t):
    a=hex2rgb(h); b=hex2rgb(other); return rgb2hex(tuple(a[i]+(b[i]-a[i])*t for i in range(3)))
def darken(h,t): return mix(h,'#000000',t)
def lighten(h,t): return mix(h,'#ffffff',t)

GOLD   = "#b08a3e"
GOLD_L = "#c9a44e"
INK    = "#2b2622"
CREAM  = "#f6f1e7"
PAPER  = "#fbf8f1"
TAN    = "#f1e6cd"   # subtitle-options box

# ---- font face block --------------------------------------------------------
FONT_CSS = f"""
@font-face {{ font-family:'Playfair'; font-weight:400 900; font-style:normal;
  src:url(data:font/ttf;base64,{F['Playfair']}) format('truetype'); }}
@font-face {{ font-family:'Playfair'; font-weight:400 900; font-style:italic;
  src:url(data:font/ttf;base64,{F['PlayfairItalic']}) format('truetype'); }}
@font-face {{ font-family:'Garamond'; font-weight:400 800; font-style:normal;
  src:url(data:font/ttf;base64,{F['Garamond']}) format('truetype'); }}
@font-face {{ font-family:'Garamond'; font-weight:400 800; font-style:italic;
  src:url(data:font/ttf;base64,{F['GaramondItalic']}) format('truetype'); }}
"""

def tags(lst, color):
    chips="".join(f'<span class="chip">{esc(t)}</span>' for t in lst)
    return f'<div class="chips" style="--c:{color}">{chips}</div>'

# ---- session card -----------------------------------------------------------
def session_card(n, s, color):
    accent = lighten(color,0.55)
    title = f'{esc(s["t"])} <i>{esc(s["a"])}</i>'
    qs="".join(f'<div class="q"><span class="qm">Q</span><p>{esc(q)}</p></div>' for q in s["q"])
    if s.get("commit"):
        step = (f'<div class="step commit"><div class="step-label">Commitment Step</div>'
                f'<p>{esc(s["commit"])}</p></div>')
    else:
        step = (f'<div class="step"><div class="step-label">This Week\u2019s Step</div>'
                f'<p>{esc(s["step"])}</p></div>')
    return f"""
    <div class="card">
      <div class="card-head" style="--c:{color}">
        <div class="sess-no">Session {n}</div>
        <div class="sess-title">{title}</div>
      </div>
      <div class="card-body">
        <p class="verse">{esc(s["s"])}</p>
        {tags(s["tags"], color)}
        <div class="dq-label">Discussion Questions</div>
        {qs}
        {step}
      </div>
    </div>"""

# ---- a single title spread --------------------------------------------------
ROMAN={1:"ONE",2:"TWO",3:"THREE",4:"FOUR",5:"FIVE",6:"SIX",7:"SEVEN",8:"EIGHT",9:"NINE",10:"TEN"}

def title_section(d):
    c=d["color"]; dark=darken(c,0.18); deep=darken(c,0.34)
    tint=lighten(c,0.93)
    name = (f'{esc(d["title"])} <i>{esc(d["accent"])}</i>' if d["title"]
            else f'<i>{esc(d["accent"])}</i>')
    subs="".join(f'<div class="sub-opt">{esc(x)}</div>' for x in d["subtitles"])
    info_rows="".join(
        f'<div class="ir"><span class="ik">{esc(k)}</span><span class="iv">{esc(v)}</span></div>'
        for k,v in d["info"])
    cards="".join(session_card(i+1, s, c) for i,s in enumerate(d["sessions"]))
    return f"""
  <section class="title-spread" style="--c:{c};--c-dark:{dark};--c-deep:{deep};--c-tint:{tint}">
    <div class="banner">
      <div class="wmk">{d['num']}</div>
      <div class="banner-eyebrow">Series {ROMAN[d['num']]} &nbsp;\u00b7&nbsp; {esc(d['category'])}</div>
      <h2 class="banner-title">{name}</h2>
      <p class="banner-sub">{esc(d['subhead'])}</p>
    </div>

    <div class="intro">
      <div class="intro-main">
        <p class="pullquote">{esc(d['pullquote'])}</p>
        <p class="body">{d['body']}</p>
        <div class="scripture">
          <div class="sl">Core Scripture</div>
          <p class="st">{esc(d['scripture'])}</p>
          <p class="sr">{esc(d['scripture_ref'])}</p>
        </div>
      </div>
      <aside class="intro-side">
        <div class="info-card">
          <div class="info-label">Series Information</div>
          {info_rows}
        </div>
        <div class="subs-card">
          <div class="subs-label">Subtitle Options</div>
          {subs}
        </div>
      </aside>
    </div>

    <div class="bigidea">
      <div class="bi-label">Big Idea</div>
      <p class="bi-text">{esc(d['bigidea'])}</p>
      {tags(d['tags'], 'rgba(255,255,255,.4)')}
    </div>

    <div class="curr-label">Small Group Curriculum &nbsp;\u2014&nbsp; Six Sessions</div>
    <div class="cards">{cards}</div>
  </section>"""

# ---- cover ------------------------------------------------------------------
def cover():
    swatches="".join(
        f'<li><span class="sw" style="background:{d["color"]}"></span>'
        f'<span class="sw-t"><b>{esc((d["title"]+" "+d["accent"]).strip())}</b>'
        f'<i>{esc(d["subtitles"][0])}</i></span></li>'
        for d in TITLES)
    return f"""
  <section class="cover">
    <div class="cover-eyebrow">{esc(COLLECTION['eyebrow'])}</div>
    <h1 class="cover-title">{esc(COLLECTION['title'])}<br><span class="ct-accent">{esc(COLLECTION['title_accent'])}</span></h1>
    <p class="cover-lede">{esc(COLLECTION['lede'])}</p>
    <ul class="toc">{swatches}</ul>
    <div class="framework">
      <div class="fw-label">The Governing Framework Sentence</div>
      <p>{esc(COLLECTION['framework'])}</p>
    </div>
    <div class="cover-foot">{esc(COLLECTION['footer'])}</div>
  </section>"""

# ---- closing ----------------------------------------------------------------
def closing():
    bars="".join(f'<span style="background:{d["color"]}"></span>' for d in TITLES)
    return f"""
  <section class="closing">
    <div class="spectrum">{bars}</div>
    <div class="closing-kicker">{esc(COLLECTION['closing_kicker'])}</div>
    <h2 class="closing-title">{esc(COLLECTION['closing_title'])}</h2>
    <p class="closing-body">{esc(COLLECTION['closing_body'])}</p>
    <div class="closing-stats">
      <div><b>10</b><span>40-day journeys</span></div>
      <div><b>60</b><span>small group sessions</span></div>
      <div><b>2-yr</b><span>ministry calendar</span></div>
    </div>
    <div class="cover-foot">{esc(COLLECTION['footer'])}</div>
  </section>"""

# ---- full document ----------------------------------------------------------
def document():
    sections="".join(title_section(d) for d in TITLES)
    return f"""<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>The Family Legacy Collection \u00b7 Lifetogether</title>
<style>
{FONT_CSS}
*{{box-sizing:border-box;margin:0;padding:0}}
:root{{--gold:{GOLD};--gold-l:{GOLD_L};--ink:{INK};--cream:{CREAM};--paper:{PAPER};--tan:{TAN}}}
html{{-webkit-print-color-adjust:exact;print-color-adjust:exact}}
body{{font-family:'Garamond',Georgia,serif;color:var(--ink);background:var(--cream);
  font-size:15px;line-height:1.5;-webkit-font-smoothing:antialiased}}
.page{{width:850px;margin:0 auto;background:var(--paper)}}
i{{font-style:italic}} b{{font-weight:700}}

/* ---------- eyebrow / labels ---------- */
.eyebrow,.banner-eyebrow,.info-label,.subs-label,.bi-label,.sl,.dq-label,.step-label,
.curr-label,.cover-eyebrow,.fw-label,.closing-kicker{{
  font-family:'Garamond',serif;text-transform:uppercase;letter-spacing:.28em;font-weight:600}}

/* ================= COVER ================= */
.cover{{padding:74px 78px 56px;background:
  radial-gradient(1100px 520px at 78% -8%, {lighten(GOLD,0.62)} 0%, rgba(0,0,0,0) 60%),
  linear-gradient(180deg,#fdfbf5 0%, var(--paper) 100%);
  min-height:1100px;display:flex;flex-direction:column}}
.cover-eyebrow{{font-size:11px;letter-spacing:.32em;color:var(--gold);margin-bottom:46px}}
.cover-title{{font-family:'Playfair',serif;font-weight:800;font-size:78px;line-height:.96;
  letter-spacing:-.01em;color:var(--ink)}}
.ct-accent{{font-style:italic;font-weight:500;color:var(--gold)}}
.cover-lede{{font-size:18px;line-height:1.62;max-width:600px;margin:30px 0 8px;color:#4a423a}}
.toc{{list-style:none;margin:30px 0 6px;columns:2;column-gap:46px}}
.toc li{{display:flex;gap:13px;break-inside:avoid;margin-bottom:15px;align-items:baseline}}
.sw{{flex:0 0 11px;width:11px;height:11px;border-radius:2px;margin-top:5px;
  box-shadow:0 0 0 1px rgba(0,0,0,.07)}}
.sw-t{{display:flex;flex-direction:column;line-height:1.25}}
.sw-t b{{font-family:'Playfair',serif;font-weight:600;font-size:16.5px;color:var(--ink)}}
.sw-t i{{font-size:12.5px;color:#7c7264}}
.framework{{margin-top:34px;padding:30px 34px;border-radius:5px;
  background:linear-gradient(135deg,{darken(INK,0)} 0%,{lighten(INK,0.08)} 100%);color:#f2ead9}}
.fw-label{{font-size:10px;letter-spacing:.3em;color:var(--gold-l);margin-bottom:14px}}
.framework p{{font-family:'Playfair',serif;font-style:italic;font-weight:400;
  font-size:18px;line-height:1.5;color:#f4eddd}}
.cover-foot{{margin-top:auto;padding-top:30px;font-size:11px;letter-spacing:.04em;
  color:#9b9081;border-top:1px solid rgba(0,0,0,.1)}}

/* ================= TITLE SPREAD ================= */
.title-spread{{break-before:page;padding:0 0 30px}}
.banner{{position:relative;overflow:hidden;color:#fbf6ea;padding:52px 78px 44px;
  background:linear-gradient(140deg,var(--c-deep) 0%,var(--c) 62%,var(--c-dark) 100%)}}
.wmk{{position:absolute;right:42px;top:-30px;font-family:'Playfair',serif;font-weight:800;
  font-size:230px;line-height:1;color:rgba(255,255,255,.09);user-select:none}}
.banner-eyebrow{{font-size:10.5px;letter-spacing:.26em;color:rgba(255,255,255,.78);
  margin-bottom:16px;position:relative}}
.banner-title{{font-family:'Playfair',serif;font-weight:700;font-size:54px;line-height:1.0;
  letter-spacing:-.01em;position:relative}}
.banner-title i{{font-weight:500;color:{lighten(GOLD,0.42)}}}
.banner-sub{{position:relative;max-width:620px;margin-top:18px;font-size:16px;line-height:1.55;
  color:rgba(255,255,255,.9);font-style:italic;font-family:'Garamond',serif}}

.intro{{display:grid;grid-template-columns:1fr 290px;gap:40px;padding:42px 78px 8px}}
.pullquote{{font-family:'Playfair',serif;font-style:italic;font-weight:500;font-size:26px;
  line-height:1.32;color:var(--c-deep);margin-bottom:22px}}
.body{{font-size:15.5px;line-height:1.66;color:#43392f}}
.body b{{color:var(--c-deep)}}
.scripture{{margin-top:26px;padding:24px 28px;border-radius:5px;color:#f7f1e4;
  background:linear-gradient(135deg,var(--c-deep),var(--c))}}
.sl{{font-size:9.5px;letter-spacing:.28em;color:rgba(255,255,255,.7);margin-bottom:11px}}
.st{{font-family:'Playfair',serif;font-style:italic;font-size:19px;line-height:1.4}}
.sr{{margin-top:9px;font-size:12.5px;letter-spacing:.04em;color:rgba(255,255,255,.78)}}

.intro-side{{display:flex;flex-direction:column;gap:18px}}
.info-card{{background:#fff;border:1px solid #e7ddc7;border-radius:5px;padding:20px 22px;
  box-shadow:0 1px 0 rgba(0,0,0,.02)}}
.info-label{{font-size:9.5px;letter-spacing:.24em;color:var(--c);margin-bottom:14px}}
.ir{{display:flex;gap:10px;padding:7px 0;border-top:1px solid #f0e8d6;font-size:13px}}
.ir:first-of-type{{border-top:none}}
.ik{{flex:0 0 86px;font-weight:700;color:#6b6052;letter-spacing:.01em}}
.iv{{color:#544a3e}}
.subs-card{{background:var(--tan);border-radius:5px;padding:18px 22px}}
.subs-label{{font-size:9.5px;letter-spacing:.24em;color:{darken(GOLD,0.12)};margin-bottom:12px}}
.sub-opt{{font-style:italic;font-size:13.5px;color:#5f5440;padding:6px 0;
  border-top:1px solid rgba(0,0,0,.07)}}
.sub-opt:first-of-type{{border-top:none}}

.bigidea{{margin:36px 78px 6px;padding:34px 40px;border-radius:6px;color:#f6efe0;
  background:linear-gradient(135deg,var(--c) 0%,var(--c-dark) 100%);position:relative}}
.bi-label{{font-size:10px;letter-spacing:.3em;color:rgba(255,255,255,.72);margin-bottom:15px}}
.bi-text{{font-family:'Playfair',serif;font-style:italic;font-weight:400;font-size:22px;
  line-height:1.46;color:#f8f2e5}}
.chips{{display:flex;flex-wrap:wrap;gap:8px;margin-top:18px}}
.chip{{font-size:11px;letter-spacing:.04em;padding:4px 11px;border-radius:20px;
  background:rgba(255,255,255,.13);border:1px solid rgba(255,255,255,.28);color:#f5eede}}
/* chips inside light cards */
.card .chips .chip{{background:var(--c-tint);border:1px solid {lighten(GOLD,0.5)};
  color:var(--c-dark)}}

.curr-label{{font-size:11px;letter-spacing:.26em;color:var(--gold);text-align:center;
  margin:40px 0 22px}}
.cards{{display:grid;grid-template-columns:1fr 1fr;gap:22px;padding:0 78px}}
.card{{background:#fff;border:1px solid #e9e0cc;border-radius:6px;overflow:hidden;
  break-inside:avoid;box-shadow:0 1px 2px rgba(0,0,0,.03)}}
.card-head{{padding:16px 22px;color:#fbf6ea;
  background:linear-gradient(135deg,var(--c) 0%,var(--c-dark) 100%)}}
.sess-no{{font-size:9.5px;letter-spacing:.26em;text-transform:uppercase;font-weight:600;
  color:rgba(255,255,255,.78);margin-bottom:6px}}
.sess-title{{font-family:'Playfair',serif;font-weight:700;font-size:21px;line-height:1.12}}
.sess-title i{{font-weight:500;color:{lighten(GOLD,0.45)}}}
.card-body{{padding:20px 22px 22px}}
.verse{{font-style:italic;font-size:13.5px;line-height:1.45;color:#6a5f50;
  padding-bottom:14px;border-bottom:1px solid #efe7d5}}
.dq-label{{font-size:9px;letter-spacing:.24em;color:var(--c);margin:16px 0 10px;font-weight:600;
  text-transform:uppercase}}
.q{{display:flex;gap:10px;padding:8px 0;border-top:1px dotted #e6dcc6}}
.q:first-of-type{{border-top:none;padding-top:2px}}
.qm{{flex:0 0 16px;height:16px;margin-top:2px;border-radius:50%;background:var(--c-tint);
  color:var(--c-dark);font-size:9px;font-weight:700;display:flex;align-items:center;
  justify-content:center;letter-spacing:0}}
.q p{{font-size:13.5px;line-height:1.45;color:#473d31}}
.step{{margin-top:16px;padding:14px 16px;border-radius:5px;background:var(--c-tint);
  border-left:3px solid var(--c)}}
.step.commit{{background:{lighten(GOLD,0.78)};border-left-color:var(--gold)}}
.step-label{{font-size:9px;letter-spacing:.2em;color:var(--c-dark);margin-bottom:7px;font-weight:700}}
.step.commit .step-label{{color:{darken(GOLD,0.15)}}}
.step p{{font-size:13px;line-height:1.5;color:#4a4034}}
.step b{{color:var(--c-deep)}}

/* ================= CLOSING ================= */
.closing{{break-before:page;padding:90px 78px 56px;min-height:1100px;
  display:flex;flex-direction:column;
  background:linear-gradient(180deg,#fdfbf5,var(--paper))}}
.spectrum{{display:flex;height:8px;border-radius:6px;overflow:hidden;margin-bottom:54px;
  box-shadow:0 1px 2px rgba(0,0,0,.06)}}
.spectrum span{{flex:1}}
.closing-kicker{{font-size:12px;letter-spacing:.3em;color:var(--gold);margin-bottom:16px}}
.closing-title{{font-family:'Playfair',serif;font-style:italic;font-weight:500;font-size:64px;
  line-height:1.0;color:var(--ink);margin-bottom:28px}}
.closing-body{{font-size:18px;line-height:1.66;max-width:640px;color:#473d31}}
.closing-stats{{display:flex;gap:54px;margin-top:46px}}
.closing-stats div{{display:flex;flex-direction:column}}
.closing-stats b{{font-family:'Playfair',serif;font-weight:700;font-size:46px;color:var(--gold)}}
.closing-stats span{{font-size:12px;letter-spacing:.16em;text-transform:uppercase;
  color:#8a7f6f;margin-top:4px}}

@media print{{
  body{{background:#fff}}
  .page{{width:auto;margin:0}}
  .title-spread,.closing{{break-before:page}}
  .card,.toc li,.framework,.scripture,.bigidea,.info-card{{break-inside:avoid}}
}}
</style></head>
<body><div class="page">
{cover()}
{sections}
{closing()}
</div></body></html>"""

if __name__=="__main__":
    out=document()
    with open("/home/claude/Family_Legacy_Collection.html","w",encoding="utf-8") as f:
        f.write(out)
    print("HTML bytes:", len(out))
