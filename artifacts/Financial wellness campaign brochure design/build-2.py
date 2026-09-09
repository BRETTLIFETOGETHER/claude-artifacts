# -*- coding: utf-8 -*-
import re, html as _html, sys, importlib
_MOD = sys.argv[1] if len(sys.argv) > 1 else 'content'
_C = importlib.import_module(_MOD)
COLLECTION, VOLUMES, PALETTE = _C.COLLECTION, _C.VOLUMES, _C.PALETTE
def _cf(k, d):  # collection field with fallback
    return COLLECTION.get(k, d)

# ---------- fonts ----------
FB = {}
for line in open('fonts_b64.txt'):
    k, b = line.strip().split('|', 1)
    FB[k] = b
def face(fam, key, weight, style='normal'):
    return (f"@font-face{{font-family:'{fam}';src:url(data:font/ttf;base64,{FB[key]}) "
            f"format('truetype');font-weight:{weight};font-style:{style};font-display:swap;}}")
FONT_CSS = "\n".join([
    face('Playfair','PlayfairV','400 900','normal'),
    face('Playfair','PlayfairIt','400 900','italic'),
    face('Spectral','SpectralR','400'), face('Spectral','SpectralM','500'),
    face('Spectral','SpectralSB','600'), face('Spectral','SpectralB','700'),
    face('Spectral','SpectralI','400','italic'), face('Spectral','SpectralMI','500','italic'),
    face('Archivo','ArchivoV','300 800'),
])

WORDS = ["ONE","TWO","THREE","FOUR","FIVE","SIX","SEVEN","EIGHT","NINE","TEN"]

def md(t):  # **bold** -> <strong>
    return re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', t)

def chips(tags, cls="chip"):
    return "".join(f'<span class="{cls}">{t}</span>' for t in tags)

# ---------- per-session card ----------
def session_card(i, s):
    (head, tail), (squote, sref), tags, qs, (steplabel, steptext) = s
    qhtml = "".join(
        f'<div class="q"><span class="qmark">›</span><span>{_html.escape(q)}</span></div>'
        for q in qs)
    step_cls = "step commit" if "COMMIT" in steplabel else "step"
    return f"""<div class="scard">
  <div class="scard-head">
    <div class="snum">SESSION {i}</div>
    <h4 class="stitle">{head} <em>{tail}</em></h4>
  </div>
  <div class="scard-body">
    <p class="sverse">&ldquo;{_html.escape(squote)}&rdquo; <span class="sref">{_html.escape(sref)}</span></p>
    <div class="chiprow">{chips(tags,'tchip')}</div>
    <div class="qlabel">Discussion questions</div>
    {qhtml}
    <div class="{step_cls}"><div class="steplabel">{steplabel}</div><p>{md(steptext)}</p></div>
  </div>
</div>"""

# ---------- per-volume ----------
def volume(idx, v):
    pal = PALETTE[idx]
    head, tail = v["title"]
    info = v["info"]
    subs = "".join(f'<li>{s}</li>' for s in v["subtitles"])
    sessions = "".join(session_card(i+1, s) for i, s in enumerate(v["sessions"]))
    squote, sref = v["scripture"]
    style = (f"--dark:{pal['dark']};--deep:{pal['deep']};--tint:{pal['tint']};")
    return f"""<section class="vol" style="{style}">
 <header class="banner">
   <div class="ghost">{idx+1}</div>
   <div class="banner-in">
     <div class="b-eyebrow">Volume {WORDS[idx]} &nbsp;·&nbsp; {v['felt']}</div>
     <h2 class="vtitle">{head}{(' <em>'+tail+'</em>') if tail else ''}</h2>
     <p class="b-deck">{v['deck']}</p>
   </div>
 </header>
 <div class="vbody">
   <div class="lede">
     <div class="lede-l">
       <blockquote class="pull">&ldquo;{v['pullquote']}&rdquo;</blockquote>
       <p class="intro">{md(v['intro'])}</p>
       <div class="scripbox">
         <div class="scriplabel">Core Scripture</div>
         <p class="scripq">&ldquo;{_html.escape(squote)}&rdquo;</p>
         <div class="scripref">{_html.escape(sref)}</div>
       </div>
     </div>
     <aside class="lede-r">
       <div class="info">
         <div class="info-h">Series Information</div>
         <dl>
           <dt>Format</dt><dd>40-Day Journey + 6-Session Small Group</dd>
           <dt>Audience</dt><dd>{info['audience']}</dd>
           <dt>Best Season</dt><dd>{info['season']}</dd>
           <dt>Tier</dt><dd>Tier 1 — top-priority build</dd>
           <dt>Score</dt><dd>{info['score']}</dd>
           <dt>Related</dt><dd>{info['related']}</dd>
         </dl>
       </div>
       <div class="subs">
         <div class="subs-h">Subtitle Options</div>
         <ul>{subs}</ul>
       </div>
     </aside>
   </div>
   <div class="bigidea">
     <div class="bi-label">The Big Idea</div>
     <p>{v['bigidea']}</p>
     <div class="bi-chips">{chips(v['tags'],'ochip')}</div>
   </div>
   <div class="curr-label"><span>Small Group Curriculum</span><i>Six Sessions · 40 Days</i></div>
   <div class="grid">{sessions}</div>
 </div>
</section>"""

# ---------- cover ----------
def cover():
    rows = ""
    for i, v in enumerate(VOLUMES):
        head, tail = v["title"]
        _, sref = v["scripture"]
        pal = PALETTE[i]
        rows += f"""<div class="lrow">
   <div class="lnum" style="color:{pal['dark']}">{i+1:02d}</div>
   <div class="ltitle">{(head+' '+tail).strip()}<span class="lfelt">{v['felt'].title()}</span></div>
   <div class="lref">{_html.escape(sref.replace(' (NIV)',''))}</div>
 </div>"""
    return f"""<section class="cover">
 <div class="c-top">
   <div class="c-brand">Lifetogether <span>·</span> Campaign Platform</div>
   <div class="c-rule"></div>
   <div class="c-kicker">{_cf('kicker','The Ten-Volume Collection')}</div>
   <h1 class="c-title">{_cf('title_head','Faith &amp;')}<br><em>{_cf('title_tail','Finances.')}</em></h1>
   <p class="c-deck">{COLLECTION['deck']}</p>
 </div>
 <div class="c-frame">
   <div class="cf-label">The Collection in One Sentence</div>
   <p>{COLLECTION['framework']}</p>
 </div>
 <div class="ledger">
   <div class="ledger-h"><span>The Ten Campaigns</span><i>40-Day Journey · 6 Sessions Each</i></div>
   {rows}
 </div>
 <div class="c-foot">Brett Eastman &nbsp;·&nbsp; Founder, Lifetogether &nbsp;·&nbsp; brett@lifetogether.com</div>
</section>"""

# ---------- closing ----------
def closing():
    return f"""<section class="closing">
  <div class="cl-mark">✦</div>
  <h2 class="cl-title">{_cf('closing_l1','Ten volumes.')}<br>{_cf('closing_l2','One faithful life.')}<br><em>{_cf('closing_tail','All of it stewarded.')}</em></h2>
  <p class="cl-deck">{_cf('closing_deck','')}</p>
  <div class="cl-stats">
    <div class="stat"><b>10</b><span>40-Day Campaigns</span></div>
    <div class="stat"><b>60</b><span>Small-Group Sessions</span></div>
    <div class="stat"><b>400</b><span>Days of Formation</span></div>
  </div>
  <div class="cl-foot">Brett Eastman &nbsp;·&nbsp; Founder, Lifetogether &nbsp;·&nbsp; brett@lifetogether.com
   &nbsp;·&nbsp; {_cf('name','The Faith &amp; Finances Collection')}</div>
</section>"""

# ---------- CSS ----------
CSS = """
*{margin:0;padding:0;box-sizing:border-box}
:root{
 --cream:#f5efe2; --card:#fcf9f1; --ink:#211c14; --body:#34302a; --muted:#6f685a;
 --gold:#bf9442; --goldlite:#dcb968; --hair:rgba(33,28,20,.14); --inkdeep:#171410;
}
html{-webkit-print-color-adjust:exact;print-color-adjust:exact}
body{font-family:'Spectral',Georgia,serif;color:var(--body);background:#cfc6b4;
 font-size:11.2pt;line-height:1.5;font-weight:400}
em{font-style:italic}
.eyb,.b-eyebrow,.c-brand,.c-kicker,.cf-label,.ledger-h,.info-h,.subs-h,.bi-label,
.curr-label,.snum,.qlabel,.steplabel,.scriplabel,.lfelt,.cl-foot,.c-foot,.lref,
.ledger-h i,.curr-label i,.stat span{
 font-family:'Archivo',Arial,sans-serif;text-transform:uppercase;letter-spacing:.22em}

/* ---- page model ---- */
.doc{background:var(--cream);width:8.5in;max-width:100%;margin:26px auto;
 box-shadow:0 10px 50px rgba(0,0,0,.3);overflow:hidden;position:relative}
.doc .vol:first-of-type,.doc .closing{}
.page{background:var(--cream);width:8.5in;min-height:11in;margin:18px auto;
 box-shadow:0 8px 36px rgba(0,0,0,.28);overflow:hidden;position:relative}
@page{size:Letter;margin:0;
  @bottom-center{content:"__RUNFOOT__";
    font-family:'Archivo',sans-serif;font-size:6.6pt;letter-spacing:.2em;
    text-transform:uppercase;color:#9a8f78}
  @bottom-right{content:counter(page);font-family:'Archivo',sans-serif;
    font-size:6.6pt;letter-spacing:.15em;color:#9a8f78;margin-right:.5in}}
@media print{.page{width:auto;min-height:0;margin:0;box-shadow:none}}

/* ===== COVER ===== */
.cover{padding:.85in .85in .55in}
.c-brand{font-size:8pt;color:var(--gold);font-weight:600}
.c-rule{height:2px;background:linear-gradient(90deg,var(--gold),rgba(191,148,66,0));margin:.32in 0 .42in}
.c-kicker{font-size:8.5pt;color:var(--muted);font-weight:500;margin-bottom:.12in}
.c-title{font-family:'Playfair';font-weight:800;color:var(--ink);font-size:74pt;
 line-height:.94;letter-spacing:-.5pt}
.c-title em{color:var(--gold);font-weight:700}
.c-deck{font-family:'Spectral';font-size:13pt;line-height:1.55;color:#43403a;
 max-width:6.1in;margin-top:.3in}
.c-frame{background:var(--inkdeep);color:#efe7d4;border-radius:3px;padding:.4in .45in;
 margin:.5in 0 .5in;border-left:5px solid var(--gold)}
.cf-label{font-size:7.6pt;color:var(--goldlite);font-weight:600;margin-bottom:.16in}
.c-frame p{font-family:'Playfair';font-style:italic;font-weight:500;font-size:13.5pt;
 line-height:1.6;color:#f1ead9}
.ledger-h{display:flex;justify-content:space-between;align-items:baseline;
 border-bottom:2px solid var(--ink);padding-bottom:7px;margin-bottom:2px}
.ledger-h span{font-size:8.4pt;font-weight:700;color:var(--ink)}
.ledger-h i{font-size:7pt;color:var(--muted);font-style:normal;font-weight:500}
.lrow{display:flex;align-items:baseline;gap:.28in;padding:8.5px 2px;
 border-bottom:1px solid var(--hair)}
.lnum{font-family:'Playfair';font-weight:700;font-size:15pt;width:.5in;flex:none}
.ltitle{font-family:'Playfair';font-weight:700;font-size:13pt;color:var(--ink);flex:1}
.lfelt{display:block;font-size:6.6pt;color:var(--muted);font-weight:500;
 letter-spacing:.16em;margin-top:3px}
.lref{font-size:7pt;color:var(--gold);font-weight:600;flex:none;letter-spacing:.12em}
.c-foot{margin-top:.4in;font-size:7pt;color:var(--muted);font-weight:500;
 padding-top:.16in;border-top:1px solid var(--hair)}

/* ===== VOLUME ===== */
.vol{page-break-before:always}
.banner{background:var(--dark);color:#f2ece0;position:relative;overflow:hidden;
 padding:.42in .7in .38in}
.ghost{position:absolute;right:.28in;top:-.26in;font-family:'Playfair';font-weight:800;
 font-size:150pt;line-height:1;color:rgba(255,255,255,.06)}
.banner-in{position:relative}
.b-eyebrow{font-size:7.8pt;color:var(--goldlite);font-weight:600;margin-bottom:.13in}
.vtitle{font-family:'Playfair';font-weight:800;font-size:37pt;line-height:1;
 color:#fbf7ee;letter-spacing:-.3pt}
.vtitle em{color:var(--goldlite);font-weight:700}
.b-deck{font-family:'Spectral';font-style:italic;font-size:11pt;line-height:1.46;
 color:#ddd4c4;max-width:5.4in;margin-top:.16in}

.vbody{background:var(--tint);padding:.34in .7in .42in}

.lede{display:flex;gap:.38in;align-items:flex-start}
.lede-l{flex:1.55;min-width:0}
.lede-r{flex:1;min-width:0}
.pull{font-family:'Playfair';font-style:italic;font-weight:500;font-size:16.5pt;
 line-height:1.3;color:var(--ink);margin-bottom:.18in}
.intro{font-size:10.4pt;line-height:1.52;color:#3b372f}
.intro strong{font-weight:600;color:var(--ink)}
.scripbox{background:var(--deep);color:#ece4d2;border-radius:3px;
 padding:.2in .26in;margin-top:.22in;border-left:4px solid var(--gold)}
.scriplabel{font-size:6.8pt;color:var(--goldlite);font-weight:600;margin-bottom:7px}
.scripq{font-family:'Playfair';font-style:italic;font-size:11.5pt;line-height:1.44;color:#f3ecdb}
.scripref{font-size:8pt;color:#b9ad95;margin-top:7px;font-style:italic;font-family:'Spectral'}

.info{background:var(--inkdeep);color:#e7dfce;border-radius:3px;padding:.22in .26in}
.info-h{font-size:7.2pt;color:var(--goldlite);font-weight:600;margin-bottom:.11in}
.info dl{display:block}
.info dt{font-size:6.5pt;color:#8f846d;font-weight:600;font-family:'Archivo';
 letter-spacing:.16em;text-transform:uppercase;margin-top:7px}
.info dd{font-size:9.2pt;line-height:1.36;color:#ece4d2;margin-top:2px;font-family:'Spectral'}
.info dt:first-child{margin-top:0}
.subs{background:#f3ead2;border:1px solid #e6d6ac;border-radius:3px;
 padding:.2in .26in;margin-top:.16in}
.subs-h{font-size:7pt;color:#a07e2c;font-weight:600;margin-bottom:.1in}
.subs ul{list-style:none}
.subs li{font-family:'Spectral';font-style:italic;font-size:9.3pt;line-height:1.35;
 color:#5b5034;padding:4px 0;border-bottom:1px solid rgba(160,126,44,.18)}
.subs li:last-child{border-bottom:none}

.bigidea{background:var(--dark);color:#f1ead9;border-radius:3px;
 padding:.26in .34in;margin:.26in 0 .28in;break-inside:avoid}
.bi-label{font-size:7.4pt;color:var(--goldlite);font-weight:600;margin-bottom:.11in}
.bigidea p{font-family:'Playfair';font-style:italic;font-weight:500;font-size:13.5pt;
 line-height:1.42;color:#f5efe1}
.bi-chips{margin-top:.15in}
.ochip{display:inline-block;font-family:'Archivo';font-size:7pt;letter-spacing:.12em;
 text-transform:uppercase;color:#e6dcc6;border:1px solid rgba(255,255,255,.28);
 border-radius:30px;padding:4px 11px;margin:0 6px 6px 0;font-weight:500}

.curr-label{display:flex;justify-content:space-between;align-items:baseline;
 border-bottom:2px solid var(--dark);padding-bottom:6px;margin-bottom:.18in}
.curr-label span{font-size:8.6pt;font-weight:700;color:var(--dark)}
.curr-label i{font-size:6.8pt;color:var(--muted);font-style:normal;font-weight:500}

/* sessions: inline-block grid for robust print pagination */
.grid{font-size:0}
.scard{display:inline-block;vertical-align:top;width:48.7%;background:var(--card);
 border:1px solid var(--hair);border-radius:3px;margin:0 0 .13in;overflow:hidden;
 break-inside:avoid;page-break-inside:avoid}
.scard:nth-child(odd){margin-right:2.5%}
.scard-head{background:var(--dark);padding:.11in .18in .12in}
.snum{font-size:6.3pt;color:var(--goldlite);font-weight:600}
.stitle{font-family:'Playfair';font-weight:700;font-size:12.5pt;color:#fbf7ee;
 line-height:1.08;margin-top:3px}
.stitle em{color:var(--goldlite);font-weight:700}
.scard-body{padding:.13in .18in .14in}
.sverse{font-family:'Spectral';font-style:italic;font-size:8.6pt;line-height:1.32;
 color:#4d473c}
.sref{font-style:normal;font-family:'Archivo';font-size:6pt;letter-spacing:.08em;
 text-transform:uppercase;color:var(--gold);white-space:nowrap}
.chiprow{margin:.07in 0 .05in}
.tchip{display:inline-block;font-family:'Archivo';font-size:5.9pt;letter-spacing:.06em;
 text-transform:uppercase;color:#6a6051;background:rgba(33,28,20,.055);
 border:1px solid var(--hair);border-radius:20px;padding:2px 6px;margin:0 3px 3px 0;font-weight:500}
.qlabel{display:none}
.q{display:flex;gap:6px;font-size:8pt;line-height:1.24;color:#3f3a31;
 padding:2.5px 0;border-top:1px dotted rgba(33,28,20,.16)}
.q:first-of-type{border-top:none;padding-top:1px}
.qmark{color:var(--gold);font-weight:700;font-family:'Playfair';flex:none;line-height:1.02}
.step{background:rgba(33,28,20,.05);border-radius:3px;padding:.09in .13in;margin-top:.08in}
.step.commit{background:var(--tint);border:1px solid var(--hair)}
.steplabel{font-size:6.1pt;color:var(--gold);font-weight:700;margin-bottom:4px}
.step p{font-size:8pt;line-height:1.34;color:#3d382f}
.step strong{font-weight:600;color:var(--ink)}

/* ===== CLOSING ===== */
.closing{page-break-before:always;background:var(--inkdeep);color:#efe7d4;
 padding:1.3in .9in;min-height:11in}
@media print{.closing{min-height:0;height:11in}}
.cl-mark{color:var(--gold);font-size:22pt;margin-bottom:.3in}
.cl-title{font-family:'Playfair';font-weight:800;font-size:46pt;line-height:1.05;
 color:#fbf6ea;letter-spacing:-.3pt}
.cl-title em{color:var(--goldlite);font-weight:700}
.cl-deck{font-family:'Spectral';font-size:12.5pt;line-height:1.65;color:#d9cfba;
 max-width:6in;margin-top:.4in}
.cl-stats{display:flex;gap:.7in;margin-top:.6in;padding-top:.4in;
 border-top:1px solid rgba(255,255,255,.16)}
.stat b{font-family:'Playfair';font-weight:800;font-size:38pt;color:var(--goldlite);
 display:block;line-height:1}
.stat span{font-size:7.4pt;color:#b6ab93;font-weight:600;margin-top:8px;display:block}
.cl-foot{margin-top:1in;font-size:7pt;color:#8d836d;font-weight:500;
 padding-top:.18in;border-top:1px solid rgba(255,255,255,.13)}
"""

def build():
    body_screen = ('<div class="doc">' + cover()
        + "".join(volume(i,v) for i,v in enumerate(VOLUMES))
        + closing() + '</div>')
    body_print = (cover()
        + "".join(volume(i,v) for i,v in enumerate(VOLUMES))
        + closing())
    shell = """<!doctype html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{name} · Lifetogether</title>
<style>{font}\n{css}</style></head><body>{body}</body></html>"""
    name = _cf('name', 'The Faith &amp; Finances Collection')
    runfoot = ("Lifetogether · " + name.replace('&amp;', '&'))
    css = CSS.replace('__RUNFOOT__', runfoot)
    slug = _cf('slug', 'Faith_and_Finances_Collection')
    open(f'{slug}.html','w').write(
        shell.format(name=name, font=FONT_CSS, css=css, body=body_screen))
    open('_print.html','w').write(
        shell.format(name=name, font=FONT_CSS, css=css, body=body_print))
    print("HTML written:", slug)

if __name__ == "__main__":
    build()
