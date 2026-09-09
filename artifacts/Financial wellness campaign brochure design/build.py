# -*- coding: utf-8 -*-
import base64, html, os
from content import PLATFORM, THEMES, SERIES

FONT_DIR = "/home/claude/work/fonts"

def b64(name):
    with open(os.path.join(FONT_DIR, name), "rb") as f:
        return base64.b64encode(f.read()).decode()

FONT_FACE = f"""
@font-face {{ font-family:'Playfair Display'; font-weight:400 900; font-style:normal;
  src:url(data:font/ttf;base64,{b64('PlayfairDisplay.ttf')}) format('truetype'); font-display:swap; }}
@font-face {{ font-family:'Playfair Display'; font-weight:400 900; font-style:italic;
  src:url(data:font/ttf;base64,{b64('PlayfairDisplay-Italic.ttf')}) format('truetype'); font-display:swap; }}
@font-face {{ font-family:'Archivo'; font-weight:100 900; font-style:normal;
  src:url(data:font/ttf;base64,{b64('Archivo.ttf')}) format('truetype'); font-display:swap; }}
@font-face {{ font-family:'Spectral'; font-weight:400; font-style:normal;
  src:url(data:font/ttf;base64,{b64('Spectral-Regular.ttf')}) format('truetype'); font-display:swap; }}
@font-face {{ font-family:'Spectral'; font-weight:500; font-style:normal;
  src:url(data:font/ttf;base64,{b64('Spectral-Medium.ttf')}) format('truetype'); font-display:swap; }}
@font-face {{ font-family:'Spectral'; font-weight:600; font-style:normal;
  src:url(data:font/ttf;base64,{b64('Spectral-SemiBold.ttf')}) format('truetype'); font-display:swap; }}
@font-face {{ font-family:'Spectral'; font-weight:400; font-style:italic;
  src:url(data:font/ttf;base64,{b64('Spectral-Italic.ttf')}) format('truetype'); font-display:swap; }}
"""

def esc(s): return html.escape(s, quote=False)

def lspace(text):
    # letter-spaced eyebrow rendering handled by CSS; just return escaped
    return esc(text)

def tags_html(tags, cls="tag"):
    return "".join(f'<span class="{cls}">{esc(t)}</span>' for t in tags)

# ---------- COVER ----------
def cover():
    p = PLATFORM
    t = p["title_lines"]
    return f"""
<section class="page cover">
  <div class="cover-frame">
    <div class="kicker gold">{esc(p['kicker'])}</div>
    <h1 class="cover-title">
      <span class="ct-1">{esc(t[0])}</span>
      <span class="ct-2">{esc(t[1])}</span>
      <span class="ct-3">{esc(t[2])}</span>
    </h1>
    <p class="cover-deck">{esc(p['deck'])}</p>
    <div class="cover-grid">
      {''.join(cover_chip(s) for s in SERIES)}
    </div>
    <div class="cover-foot">{esc(p['footer'])} <span class="lt">Lifetogether</span></div>
  </div>
</section>"""

def cover_chip(s):
    th = THEMES[s["theme"]]
    title = " ".join(s["title"])
    return f"""<div class="chip" style="--edge:{th['edge']}">
      <span class="chip-n">{s['n']:02d}</span>
      <span class="chip-t">{esc(title)}</span></div>"""

# ---------- FRAMEWORK PAGE ----------
def framework():
    p = PLATFORM
    intro = "".join(f"<p>{esc(par)}</p>" for par in p["intro"])
    return f"""
<section class="page framework">
  <div class="fw-head">
    <div class="kicker">THE FLOURISHING OF FINANCES</div>
    <h2 class="fw-title">Six things you can feel.<br>One way God designed money to work.</h2>
  </div>
  <div class="fw-sentence">
    <div class="kicker gold">{esc(p['framework_label'])}</div>
    <p class="fw-quote">{esc(p['framework_sentence'])}</p>
  </div>
  <div class="fw-body">{intro}</div>
  <div class="fw-grid">
    {''.join(grid_card(s) for s in SERIES)}
  </div>
</section>"""

def grid_card(s):
    th = THEMES[s["theme"]]
    title = " ".join(s["title"])
    scr_ref = s["scripture"][1].replace(" (NIV)", "")
    return f"""<div class="gcard" style="--dark:{th['dark']};--edge:{th['edge']}">
      <div class="gcard-bar"></div>
      <div class="gcard-body">
        <div class="gcard-n">{s['n']:02d}</div>
        <div class="gcard-title">{esc(title)}</div>
        <div class="gcard-cat">{esc(s['category'].split('· ',1)[1])}</div>
        <div class="gcard-meta"><span>40-Day</span><span>6-Session</span><span>Tier 1</span></div>
      </div>
    </div>"""

# ---------- SERIES SECTION ----------
def series_section(s):
    th = THEMES[s["theme"]]
    style = f"--dark:{th['dark']};--deep:{th['deep']};--tint:{th['tint']};--edge:{th['edge']}"
    title_h = f'<span class="st-a">{esc(s["title"][0])}</span> <span class="st-b">{esc(s["title"][1])}</span>'
    scr_text, scr_ref = s["scripture"]
    subs = "".join(f"<div class='sub'>{esc(x)}</div>" for x in s["subtitles"])

    info = s["info"]
    info_rows = [
        ("Format", "40-Day Journey + 6-Session Small Group"),
        ("Audience", info["Audience"]),
        ("Best Season", info["Best Season"]),
        ("Tier", "Tier 1 — highest market demand"),
        ("Best For", "Church · Company"),
        ("Core Felt Need", "Debt · budgeting · money stress · simplicity"),
        ("Why It Matters", info["Why it matters"]),
    ]
    info_html = "".join(
        f"<div class='inforow'><span class='infok'>{esc(k)}</span>"
        f"<span class='infov'>{esc(v)}</span></div>" for k, v in info_rows)

    sessions = "".join(session_card(s, sess, i) for i, sess in enumerate(s["sessions"], 1))

    return f"""
<section class="page series" style="{style}">
  <div class="band">
    <div class="band-num">{s['n']}</div>
    <div class="band-inner">
      <div class="kicker band-cat">{esc(s['category'])}</div>
      <h2 class="band-title">{title_h}</h2>
      <p class="band-line">{esc(s['band_line'])}</p>
    </div>
  </div>

  <div class="content">
    <div class="lead">
      <blockquote class="pull">{esc(s['pull'])}</blockquote>
      <div class="lead-body">{esc(s['body'])}</div>
      <div class="scripture">
        <div class="kicker">Core Scripture</div>
        <p class="scr-text">{esc(scr_text)}</p>
        <p class="scr-ref">— {esc(scr_ref)}</p>
      </div>
    </div>
    <aside class="side">
      <div class="info">
        <div class="kicker">Series Information</div>
        {info_html}
      </div>
      <div class="subs">
        <div class="kicker">Subtitle Options</div>
        {subs}
      </div>
    </aside>
  </div>

  <div class="bigidea">
    <div class="kicker">The Big Idea</div>
    <p class="bi-text">{esc(s['bigidea'])}</p>
    <div class="tags">{tags_html(s['tags'])}</div>
  </div>

  <div class="curriculum">
    <div class="kicker cur-label">Small Group Curriculum — Six Sessions</div>
    <div class="sessions">{sessions}</div>
  </div>
</section>"""

def session_card(series, sess, idx):
    qs = "".join(f"<li>{esc(q)}</li>" for q in sess["q"])
    tag_line = tags_html(sess["tags"], "stag")
    if "commit" in sess:
        step_block = (f"<div class='step commit'><div class='kicker step-k'>Commitment Step</div>"
                      f"<p>{esc(sess['commit'])}</p></div>")
    else:
        step_block = (f"<div class='step'><div class='kicker step-k'>This Week\u2019s Step</div>"
                      f"<p>{esc(sess['step'])}</p></div>")
    title = f'<span class="sc-a">{esc(sess["t"][0])}</span> <span class="sc-b">{esc(sess["t"][1])}</span>'
    return f"""<div class="session">
      <div class="sc-head">
        <div class="kicker sc-eyebrow">Session {idx}</div>
        <h3 class="sc-title">{title}</h3>
      </div>
      <div class="sc-body">
        <p class="sc-verse">{esc(sess['v'])}</p>
        <div class="stags">{tag_line}</div>
        <div class="kicker sc-q-label">Discussion Questions</div>
        <ol class="sc-q">{qs}</ol>
        {step_block}
      </div>
    </div>"""

# ---------- CLOSING ----------
def closing():
    p = PLATFORM
    lines = "".join(f"<span>{esc(l)}</span>" for l in p["closing_title"])
    return f"""
<section class="page closing">
  <div class="close-inner">
    <h2 class="close-title">{lines}</h2>
    <p class="close-body">{esc(p['closing_body'])}</p>
    <div class="close-stats">
      <div class="stat"><div class="stat-n">10</div><div class="stat-l">40-Day Campaigns</div></div>
      <div class="stat"><div class="stat-n">60</div><div class="stat-l">Small Group Sessions</div></div>
      <div class="stat"><div class="stat-n">1</div><div class="stat-l">Transformed Relationship<br>with Money</div></div>
    </div>
    <div class="close-cta">
      <div class="cta-lead">Start the journey</div>
      <div class="cta-line">Choose your church\u2019s first title \u2014 and launch a season no one comes through unchanged.</div>
      <div class="cta-tag gold">brett@lifetogether.com</div>
    </div>
    <div class="cover-foot light">{esc(p['footer'])} · Complete Reference <span class="lt">Lifetogether</span></div>
  </div>
</section>"""

# ---------- ASSEMBLE ----------
CSS = """
*{margin:0;padding:0;box-sizing:border-box}
:root{
  --gold:#c4a35a; --gold-bright:#d8bd7c;
  --ink:#22252b; --ink-soft:#4a4d54;
  --cream:#f7f3ea; --cream-2:#efe9dc; --navy:#15233c;
  --rule:rgba(34,37,43,.14);
}
html{-webkit-print-color-adjust:exact;print-color-adjust:exact}
body{font-family:'Spectral',Georgia,serif;color:var(--ink);background:#3a3f47;
  line-height:1.7;font-size:16px;-webkit-font-smoothing:antialiased}
.page{position:relative;width:8.5in;min-height:11in;margin:0 auto;background:var(--cream);
  overflow:hidden}
@media screen{.page{margin:22px auto;box-shadow:0 24px 60px rgba(0,0,0,.4)}}

.kicker{font-family:'Archivo',sans-serif;text-transform:uppercase;letter-spacing:.26em;
  font-size:10.5px;font-weight:600;color:var(--ink-soft)}
.kicker.gold{color:var(--gold)}
.gold{color:var(--gold)}
.lt{font-family:'Playfair Display',serif;font-style:italic;letter-spacing:0}

/* ---------------- COVER ---------------- */
.cover{background:var(--navy);color:#f3ede0;display:flex;padding:0}
.cover-frame{border:1px solid rgba(196,163,90,.5);margin:.42in;padding:.62in .6in .5in;
  width:100%;display:flex;flex-direction:column}
.cover .kicker{color:var(--gold-bright);letter-spacing:.24em}
.cover-title{font-family:'Playfair Display',serif;font-weight:500;line-height:.94;
  margin-top:.5in;letter-spacing:-.01em}
.cover-title span{display:block}
.ct-1{font-size:46px;font-style:italic;color:#cfd6e2;font-weight:400}
.ct-2{font-size:108px;color:#f3ede0}
.ct-3{font-size:108px;color:var(--gold-bright);font-style:italic;font-weight:500}
.cover-deck{font-size:17.5px;line-height:1.62;max-width:5.6in;margin-top:.34in;
  color:#d9ddE6;font-weight:400}
.cover-grid{display:grid;grid-template-columns:1fr 1fr;gap:9px 20px;margin-top:auto;
  padding-top:.4in}
.chip{display:flex;align-items:baseline;gap:12px;padding:9px 2px;
  border-top:1px solid rgba(196,163,90,.28)}
.chip-n{font-family:'Archivo',sans-serif;font-size:11px;font-weight:700;color:var(--edge);
  letter-spacing:.1em;min-width:24px}
.chip-t{font-family:'Playfair Display',serif;font-size:17px;color:#ede6d6}
.cover-foot{font-family:'Archivo',sans-serif;font-size:9.5px;letter-spacing:.12em;
  text-transform:uppercase;color:#9aa3b4;margin-top:.34in;display:flex;justify-content:space-between;
  border-top:1px solid rgba(196,163,90,.28);padding-top:12px}
.cover-foot .lt{font-size:13px;color:var(--gold-bright);text-transform:none;letter-spacing:0}

/* ---------------- FRAMEWORK ---------------- */
.framework{padding:.7in .68in .55in}
.fw-title{font-family:'Playfair Display',serif;font-weight:500;font-size:33px;line-height:1.16;
  margin-top:12px;color:var(--navy);letter-spacing:-.01em}
.fw-sentence{background:var(--navy);color:#eee7d8;padding:26px 30px;margin:26px 0 24px;
  border-left:4px solid var(--gold)}
.fw-quote{font-family:'Playfair Display',serif;font-style:italic;font-size:18.5px;line-height:1.6;
  margin-top:12px;color:#f1ead c;color:#f1eadc}
.fw-body{columns:2;column-gap:34px;font-size:13.5px;line-height:1.66;color:var(--ink-soft);
  text-align:justify}
.fw-body p{margin-bottom:11px;break-inside:avoid}
.fw-grid{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-top:26px}
.gcard{display:flex;background:#fff;border:1px solid var(--rule);overflow:hidden;
  break-inside:avoid}
.gcard-bar{width:7px;background:var(--dark);flex:none}
.gcard-body{padding:13px 15px;flex:1}
.gcard-n{font-family:'Archivo',sans-serif;font-size:11px;font-weight:700;color:var(--edge);
  letter-spacing:.12em}
.gcard-title{font-family:'Playfair Display',serif;font-size:21px;color:var(--ink);margin:2px 0 4px;
  font-weight:600}
.gcard-cat{font-family:'Archivo',sans-serif;font-size:9px;letter-spacing:.13em;text-transform:uppercase;
  color:var(--ink-soft);line-height:1.35}
.gcard-meta{display:flex;gap:8px;margin-top:8px}
.gcard-meta span{font-family:'Archivo',sans-serif;font-size:8.5px;letter-spacing:.1em;
  text-transform:uppercase;color:var(--dark);border:1px solid var(--rule);padding:2px 7px;border-radius:2px}

/* ---------------- SERIES ---------------- */
.series{padding:0 0 .5in}
.band{background:var(--dark);color:#f1ece0;padding:.46in .68in .42in;position:relative;overflow:hidden}
.band-num{position:absolute;left:.34in;top:50%;transform:translateY(-50%);
  font-family:'Playfair Display',serif;font-size:150px;font-weight:600;
  color:rgba(255,255,255,.06);line-height:1;pointer-events:none}
.band-inner{position:relative;padding-left:.1in}
.band-cat{color:var(--edge);letter-spacing:.22em}
.band-title{font-family:'Playfair Display',serif;font-weight:500;font-size:50px;line-height:1;
  margin:10px 0 12px;letter-spacing:-.01em}
.st-a{color:#f3 efe2;color:#f3efe2}
.st-b{color:var(--edge);font-style:italic}
.band-line{font-family:'Playfair Display',serif;font-style:italic;font-size:16px;line-height:1.5;
  max-width:6in;color:#d9d3c4;font-weight:400}

.content{display:grid;grid-template-columns:1.55fr 1fr;gap:30px;padding:.4in .68in .1in}
.pull{font-family:'Playfair Display',serif;font-style:italic;font-size:25px;line-height:1.32;
  color:var(--navy);border-left:3px solid var(--edge);padding-left:18px;margin-bottom:18px}
.series .pull{color:var(--dark)}
.lead-body{font-size:14px;line-height:1.72;color:#34373d;text-align:justify}
.scripture{background:var(--dark);color:#efe9da;padding:22px 24px;margin-top:22px;break-inside:avoid}
.scr-text{font-family:'Playfair Display',serif;font-style:italic;font-size:18px;line-height:1.5;
  margin-top:10px;color:#f2ecdd}
.scr-ref{font-family:'Archivo',sans-serif;font-size:10px;letter-spacing:.16em;text-transform:uppercase;
  margin-top:12px;color:var(--edge)}

.side{display:flex;flex-direction:column;gap:18px}
.info,.subs{background:var(--tint);padding:18px 20px;border-top:3px solid var(--dark)}
.info .kicker,.subs .kicker{margin-bottom:12px;display:block}
.inforow{display:flex;gap:10px;padding:7px 0;border-bottom:1px solid var(--rule);font-size:12px}
.inforow:last-child{border-bottom:none}
.infok{font-family:'Archivo',sans-serif;font-size:9px;letter-spacing:.1em;text-transform:uppercase;
  color:var(--ink-soft);min-width:78px;flex:none;padding-top:1px}
.infov{color:var(--ink);font-size:12.5px;line-height:1.42}
.sub{font-style:italic;font-size:13px;color:#3c3f45;padding:7px 0;border-bottom:1px solid var(--rule)}
.sub:last-child{border-bottom:none}

.bigidea{background:var(--deep);color:#f0eadb;margin:.34in .68in 0;padding:26px 30px;break-inside:avoid}
.bigidea .kicker{color:var(--edge);margin-bottom:12px;display:block}
.bi-text{font-family:'Playfair Display',serif;font-style:italic;font-size:21px;line-height:1.48;
  color:#f3eede}
.tags{display:flex;flex-wrap:wrap;gap:7px;margin-top:16px}
.tag{font-family:'Archivo',sans-serif;font-size:9px;letter-spacing:.08em;text-transform:uppercase;
  color:#e9e2d2;border:1px solid rgba(255,255,255,.28);padding:4px 10px;border-radius:2px}

.curriculum{padding:.36in .68in 0}
.cur-label{display:block;color:var(--edge);margin-bottom:16px;
  border-bottom:1px solid var(--rule);padding-bottom:12px}
.sessions{display:grid;grid-template-columns:1fr 1fr;gap:16px}
.session{border:1px solid var(--rule);background:#fff;break-inside:avoid;display:flex;flex-direction:column}
.sc-head{background:var(--dark);color:#f1ece0;padding:13px 17px}
.sc-eyebrow{color:var(--edge);letter-spacing:.18em;font-size:9px}
.sc-title{font-family:'Playfair Display',serif;font-weight:500;font-size:21px;line-height:1.08;margin-top:5px}
.sc-a{color:#f3efe3}.sc-b{color:var(--edge);font-style:italic}
.sc-body{padding:15px 17px 17px;flex:1;display:flex;flex-direction:column}
.sc-verse{font-family:'Playfair Display',serif;font-style:italic;font-size:13px;line-height:1.4;
  color:var(--dark);margin-bottom:11px}
.stags{display:flex;flex-wrap:wrap;gap:5px;margin-bottom:13px}
.stag{font-family:'Archivo',sans-serif;font-size:8px;letter-spacing:.06em;text-transform:uppercase;
  color:var(--ink-soft);background:var(--tint);padding:3px 7px;border-radius:2px}
.sc-q-label{display:block;color:var(--edge);font-size:9px;margin-bottom:8px}
.sc-q{list-style:none;counter-reset:q;flex:1}
.sc-q li{position:relative;padding-left:20px;font-size:12px;line-height:1.5;color:#34373d;
  margin-bottom:9px;counter-increment:q}
.sc-q li::before{content:counter(q);position:absolute;left:0;top:0;
  font-family:'Archivo',sans-serif;font-size:9px;font-weight:700;color:var(--edge);
  border:1px solid var(--edge);width:14px;height:14px;border-radius:50%;
  display:flex;align-items:center;justify-content:center;line-height:1}
.step{background:var(--tint);padding:12px 14px;margin-top:8px;border-left:3px solid var(--edge)}
.step.commit{border-left-color:var(--dark)}
.step-k{color:var(--dark);font-size:9px;margin-bottom:6px;display:block}
.step p{font-size:11.5px;line-height:1.52;color:#34373d}

/* ---------------- CLOSING ---------------- */
.closing{background:var(--navy);color:#f1ece0;display:flex}
.close-inner{border:1px solid rgba(196,163,90,.5);margin:.42in;padding:.7in .62in .5in;
  width:100%;display:flex;flex-direction:column}
.close-title{font-family:'Playfair Display',serif;font-weight:500;font-size:54px;line-height:1.02;
  letter-spacing:-.01em;margin-top:.3in}
.close-title span{display:block}
.close-title span:nth-child(2){color:#cfd6e2;font-style:italic;font-weight:400}
.close-title span:nth-child(3){color:var(--gold-bright);font-style:italic}
.close-body{font-size:16.5px;line-height:1.66;max-width:5.6in;margin-top:.32in;color:#d9ddE6}
.close-stats{display:flex;gap:48px;margin-top:.46in;padding-top:.32in;
  border-top:1px solid rgba(196,163,90,.3)}
.stat-n{font-family:'Playfair Display',serif;font-size:60px;color:var(--gold-bright);line-height:1;font-weight:500}
.stat-l{font-family:'Archivo',sans-serif;font-size:10px;letter-spacing:.16em;text-transform:uppercase;
  color:#aeb6c5;margin-top:10px;line-height:1.5}
.close-cta{margin-top:auto;padding-top:.5in}
.cta-lead{font-family:'Archivo',sans-serif;text-transform:uppercase;letter-spacing:.22em;font-size:11px;
  color:var(--gold-bright);font-weight:600}
.cta-line{font-family:'Playfair Display',serif;font-style:italic;font-size:23px;line-height:1.35;
  margin-top:12px;max-width:5.4in;color:#f1ead c;color:#f1eadc}
.cta-tag{font-family:'Archivo',sans-serif;letter-spacing:.14em;font-size:13px;margin-top:16px;font-weight:600}
.cover-foot.light{color:#9aa3b4;margin-top:.4in}

/* ---------------- PRINT ---------------- */
@page{size:8.5in 11in;margin:0}
@media print{
  body{background:#fff}
  .page{margin:0;box-shadow:none}
  .framework,.series,.closing{page-break-before:always;break-before:page}
  .cover{page-break-before:avoid}
  .session,.scripture,.bigidea,.gcard,.fw-sentence,.info,.subs{page-break-inside:avoid;break-inside:avoid}
  .sessions,.content,.fw-grid{page-break-inside:auto}
}
"""

def build():
    body = cover() + framework()
    for s in SERIES:
        body += series_section(s)
    body += closing()
    doc = f"""<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>The Finances Series · Lifetogether</title>
<style>{FONT_FACE}{CSS}</style>
</head><body>{body}</body></html>"""
    return doc

if __name__ == "__main__":
    out = build()
    with open("/home/claude/work/Finances_Series_Complete.html", "w", encoding="utf-8") as f:
        f.write(out)
    print("HTML bytes:", len(out))
