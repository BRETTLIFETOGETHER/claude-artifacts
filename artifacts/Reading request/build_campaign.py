#!/usr/bin/env python3
import weasyprint, base64, pathlib
F = pathlib.Path("/home/claude/fonts")
def b64(p): return base64.b64encode((F/p).read_bytes()).decode()
anton, oswald, lora, lora_it = b64("Anton-Regular.ttf"), b64("Oswald.ttf"), b64("Lora.ttf"), b64("Lora-Italic.ttf")

NAVY="#15233F"; NAVY2="#1E3358"; GOLD="#E0A82E"; GOLD_D="#C8941A"; CREAM="#FBF7EF"
PAPER="#FFFFFF"; INK="#23262B"; SLATE="#5A6472"; GREEN="#2E5D46"; TEAL="#2C6E7F"; RUST="#B5532A"

# H accent colors for the six weeks
HC = {"Honor":NAVY,"Heart":TEAL,"Habits":GREEN,"Health":GOLD_D,"Hope":RUST,"Harvest":NAVY2}

CSS = f"""
@font-face {{ font-family:'Anton'; src:url(data:font/ttf;base64,{anton}); }}
@font-face {{ font-family:'Oswald'; src:url(data:font/ttf;base64,{oswald}); }}
@font-face {{ font-family:'Lora'; src:url(data:font/ttf;base64,{lora}); font-style:normal; }}
@font-face {{ font-family:'Lora'; src:url(data:font/ttf;base64,{lora_it}); font-style:italic; }}
@page {{ size:8.5in 11in; margin:0; }}
* {{ margin:0; padding:0; box-sizing:border-box; }}
body {{ font-family:'Lora',serif; color:{INK}; font-size:9.6pt; line-height:1.5; }}
.page {{ width:8.5in; height:11in; position:relative; overflow:hidden; page-break-after:always; background:{PAPER}; }}
.page:last-child {{ page-break-after:auto; }}
.kicker {{ font-family:'Oswald',sans-serif; font-weight:600; letter-spacing:.22em; text-transform:uppercase; font-size:8pt; }}
em,i {{ font-style:italic; }} strong {{ font-weight:600; }}

/* ============ COVER (distinct: gold top band + navy lower, split) ============ */
.cv {{ position:absolute; inset:0; }}
.cv .top {{ position:absolute; top:0; left:0; right:0; height:4.35in; background:{GOLD}; overflow:hidden; }}
.cv .top .ghost {{ position:absolute; right:-0.5in; top:-1.7in; font-family:'Anton',sans-serif;
  font-size:300pt; color:rgba(21,35,63,.10); line-height:.8; }}
.cv .bot {{ position:absolute; top:4.35in; left:0; right:0; bottom:0; background:{NAVY}; }}
.cv .inner {{ position:absolute; inset:0; padding:0.85in 0.85in 0.85in; display:flex; flex-direction:column; }}
.cv .toprow {{ display:flex; justify-content:space-between; align-items:center; }}
.badge-d {{ border:1.5px solid {NAVY}; color:{NAVY}; border-radius:40px; padding:6px 16px;
  font-family:'Oswald',sans-serif; font-weight:700; letter-spacing:.18em; font-size:7.5pt; text-transform:uppercase; }}
.badge-l {{ border:1.5px solid {GOLD}; color:{GOLD}; border-radius:40px; padding:6px 16px;
  font-family:'Oswald',sans-serif; font-weight:600; letter-spacing:.18em; font-size:7.5pt; text-transform:uppercase; }}
.cv .eyebrow {{ margin-top:0.55in; font-family:'Oswald',sans-serif; font-weight:600; letter-spacing:.34em;
  text-transform:uppercase; font-size:11pt; color:{NAVY}; }}
.cv h1 {{ font-family:'Anton',sans-serif; text-transform:uppercase; line-height:.88; margin-top:14px; }}
.cv h1 .l1 {{ display:block; font-size:74pt; color:{NAVY}; }}
.cv h1 .l2 {{ display:block; font-size:74pt; color:{NAVY}; }}
.cv h1 .l3 {{ display:block; font-size:74pt; color:#fff; margin-top:2px; }}
.cv .ribbon {{ position:absolute; top:3.95in; left:0.85in; right:0.85in; }}
.cv .sub {{ font-family:'Oswald',sans-serif; font-weight:500; letter-spacing:.05em; text-transform:uppercase;
  font-size:13pt; color:{GOLD}; }}
.cv .hook {{ margin-top:auto; }}
.cv .hook .big {{ font-family:'Anton',sans-serif; text-transform:uppercase; color:#fff; font-size:31pt; line-height:1.0; }}
.cv .hook .big span {{ color:{GOLD}; }}
.cv .hook .ln {{ font-family:'Lora',serif; font-style:italic; font-size:13.5pt; color:#D9CCAE; margin-top:16px; max-width:5.6in; line-height:1.4; }}
.cv .foot {{ display:flex; justify-content:space-between; align-items:flex-end; border-top:2px solid rgba(224,168,46,.35); padding-top:16px; margin-top:24px; }}
.cv .foot .l {{ font-family:'Oswald',sans-serif; letter-spacing:.04em; font-size:8.5pt; color:#B9C2D2; line-height:1.7; }}
.cv .foot .r {{ text-align:right; font-family:'Oswald',sans-serif; font-weight:700; letter-spacing:.18em; text-transform:uppercase; font-size:8pt; color:{GOLD}; }}

/* ============ content shells ============ */
.topband {{ background:{NAVY}; color:#fff; padding:0.42in 0.7in 0.34in; }}
.topband .kick {{ color:{GOLD}; }}
.topband h2 {{ font-family:'Anton',sans-serif; text-transform:uppercase; font-size:29pt; line-height:.96; color:#fff; margin-top:7px; }}
.topband h2 .gold {{ color:{GOLD}; }}
.topband .tag {{ font-family:'Lora',serif; font-style:italic; color:#C9D2E0; font-size:10.5pt; margin-top:8px; max-width:6.4in; }}
.body {{ padding:0.34in 0.7in 0.4in; }}
.pagenum {{ position:absolute; bottom:0.34in; right:0.55in; font-family:'Oswald',sans-serif; font-weight:600; font-size:8pt; letter-spacing:.18em; color:{SLATE}; text-transform:uppercase; }}
.brandfoot {{ position:absolute; bottom:0.34in; left:0.7in; font-family:'Oswald',sans-serif; font-weight:600; font-size:8pt; letter-spacing:.18em; color:{GOLD_D}; text-transform:uppercase; }}

.promise {{ background:{GOLD}; color:{NAVY}; padding:18px 24px; border-radius:6px; margin:0 0 18px; }}
.promise .lab {{ font-family:'Oswald',sans-serif; font-weight:700; letter-spacing:.2em; text-transform:uppercase; font-size:8pt; }}
.promise p {{ font-family:'Lora',serif; font-style:italic; font-size:13pt; line-height:1.4; margin-top:6px; }}
.h3 {{ font-family:'Oswald',sans-serif; font-weight:700; text-transform:uppercase; letter-spacing:.1em; font-size:10pt; color:{NAVY}; margin-bottom:8px; padding-bottom:6px; border-bottom:2px solid {GOLD}; }}
.note {{ font-family:'Lora',serif; font-style:italic; color:{SLATE}; font-size:9pt; line-height:1.5; }}
.cols {{ display:flex; gap:22px; }} .col {{ flex:1; }}
.chips li {{ list-style:none; font-family:'Lora',serif; font-size:9.4pt; line-height:1.45; margin-bottom:9px; padding-left:18px; position:relative; }}
.chips li:before {{ content:'\\25C6'; color:{GOLD_D}; position:absolute; left:0; top:1px; font-size:7.5pt; }}

/* this/changes/everything definition */
.tce {{ display:flex; gap:10px; margin:4px 0 16px; }}
.tce .b {{ flex:1; border-radius:6px; overflow:hidden; border:1px solid #ECE3D0; }}
.tce .b .h {{ font-family:'Anton',sans-serif; text-transform:uppercase; color:#fff; font-size:15pt; padding:9px 12px; }}
.tce .b .t {{ background:{CREAM}; padding:9px 12px; font-size:8.6pt; line-height:1.42; }}

/* six-week arc table */
.arc {{ width:100%; border-collapse:separate; border-spacing:0 6px; }}
.arc td {{ padding:9px 12px; vertical-align:middle; }}
.arc .wk {{ width:0.5in; font-family:'Anton',sans-serif; color:#fff; font-size:14pt; text-align:center; border-radius:5px 0 0 5px; }}
.arc .changes {{ background:{CREAM}; font-family:'Oswald',sans-serif; font-weight:700; text-transform:uppercase; letter-spacing:.04em; font-size:9.5pt; color:{NAVY}; width:1.7in; }}
.arc .theme {{ background:{CREAM}; font-family:'Oswald',sans-serif; font-weight:600; font-size:9pt; color:{GOLD_D}; text-transform:uppercase; letter-spacing:.03em; width:1.15in; }}
.arc .q {{ background:{CREAM}; border-radius:0 5px 5px 0; font-family:'Lora',serif; font-style:italic; color:{SLATE}; font-size:9pt; }}

/* three channels diagram */
.chan {{ display:flex; gap:10px; margin:2px 0 8px; }}
.chan .c {{ flex:1; border-radius:6px; background:{NAVY}; color:#fff; padding:13px 14px; position:relative; }}
.chan .c .n {{ font-family:'Oswald',sans-serif; font-weight:700; text-transform:uppercase; letter-spacing:.08em; font-size:10pt; color:{GOLD}; }}
.chan .c p {{ font-size:8.6pt; line-height:1.4; margin-top:4px; color:#D7DEEA; }}
.chan .arrow {{ align-self:center; font-family:'Anton',sans-serif; color:{GOLD}; font-size:18pt; }}

/* session / devotional samples */
.samp-head {{ display:flex; align-items:flex-start; gap:15px; margin-bottom:12px; }}
.samp-tag {{ flex-shrink:0; border-radius:6px; color:#fff; text-align:center; padding:8px 12px; min-width:1.05in; }}
.samp-tag .a {{ font-family:'Oswald',sans-serif; font-weight:500; text-transform:uppercase; letter-spacing:.12em; font-size:7pt; color:rgba(255,255,255,.8); }}
.samp-tag .b {{ font-family:'Anton',sans-serif; font-size:15pt; line-height:1; margin-top:2px; }}
.samp-title h3 {{ font-family:'Anton',sans-serif; text-transform:uppercase; color:{NAVY}; font-size:18pt; line-height:1.0; }}
.samp-title .wk {{ font-family:'Oswald',sans-serif; font-weight:600; text-transform:uppercase; letter-spacing:.13em; font-size:7.5pt; color:{GOLD_D}; margin-top:4px; }}
.blab {{ font-family:'Oswald',sans-serif; font-weight:700; text-transform:uppercase; letter-spacing:.13em; font-size:8pt; color:{GREEN}; margin:11px 0 4px; }}
.scrip {{ background:{CREAM}; border-left:4px solid {GOLD}; padding:8px 14px; border-radius:0 5px 5px 0; font-style:italic; font-size:9.2pt; line-height:1.4; margin:3px 0 4px; }}
.samp p {{ font-size:9.5pt; line-height:1.55; margin-bottom:6px; }}
.samp p.it {{ font-style:italic; color:#3c4350; }}
.qlist {{ counter-reset:q; }}
.qlist li {{ list-style:none; position:relative; padding-left:24px; margin-bottom:5px; font-size:9.2pt; line-height:1.4; }}
.qlist li:before {{ counter-increment:q; content:counter(q); position:absolute; left:0; top:0; width:16px; height:16px;
  background:{NAVY}; color:#fff; border-radius:50%; font-family:'Oswald',sans-serif; font-weight:700; font-size:8pt; text-align:center; line-height:16px; }}
.pray {{ background:{NAVY}; color:#F4ECD8; border-radius:6px; padding:11px 16px; margin-top:10px; }}
.pray .lab {{ font-family:'Oswald',sans-serif; font-weight:700; letter-spacing:.16em; text-transform:uppercase; font-size:7.5pt; color:{GOLD}; margin-bottom:3px; }}
.pray p {{ font-family:'Lora',serif; font-style:italic; font-size:9.4pt; line-height:1.42; }}
.step {{ margin-top:9px; background:{GOLD}; color:{NAVY}; border-radius:5px; padding:9px 15px; font-family:'Lora',serif; font-size:9.6pt; }}
.step b {{ font-family:'Oswald',sans-serif; font-weight:700; text-transform:uppercase; letter-spacing:.1em; font-size:7.5pt; margin-right:6px; }}

/* launch timeline */
.tl2 {{ display:flex; gap:14px; margin-bottom:12px; }}
.tl2 .when {{ width:1.15in; flex-shrink:0; text-align:right; }}
.tl2 .when .b {{ font-family:'Anton',sans-serif; font-size:13pt; color:{NAVY}; line-height:1; }}
.tl2 .when .s {{ font-family:'Oswald',sans-serif; text-transform:uppercase; letter-spacing:.08em; font-size:6.5pt; color:{SLATE}; margin-top:2px; }}
.tl2 .dot {{ width:14px; flex-shrink:0; position:relative; }}
.tl2 .dot:before {{ content:''; position:absolute; left:4px; top:3px; width:9px; height:9px; border-radius:50%; background:{GOLD}; box-shadow:0 0 0 3px {CREAM}; }}
.tl2 .dot:after {{ content:''; position:absolute; left:7.5px; top:13px; bottom:-13px; width:2px; background:#E2D8C2; }}
.tl2:last-child .dot:after {{ display:none; }}
.tl2 .c {{ flex:1; }}
.tl2 .c .t {{ font-family:'Oswald',sans-serif; font-weight:700; text-transform:uppercase; letter-spacing:.04em; font-size:9.5pt; color:{NAVY}; }}
.tl2 .c p {{ font-size:8.7pt; line-height:1.42; margin-top:2px; }}
.tl2 .c .o {{ font-style:italic; color:{GREEN}; }}
.keyrule {{ background:{NAVY}; color:#fff; border-radius:6px; padding:12px 16px; margin-top:6px; }}
.keyrule .lab {{ font-family:'Oswald',sans-serif; font-weight:700; letter-spacing:.14em; text-transform:uppercase; font-size:7.5pt; color:{GOLD}; }}
.keyrule p {{ font-family:'Lora',serif; font-size:9.2pt; line-height:1.45; margin-top:3px; color:#E4E9F1; }}
.keyrule .key {{ font-style:italic; color:#fff; }}

/* roles cards */
.role {{ display:flex; gap:12px; align-items:flex-start; margin-bottom:11px; background:{CREAM}; border-radius:6px; padding:11px 14px; border-left:4px solid {GOLD}; }}
.role .ico {{ font-family:'Anton',sans-serif; color:{GOLD_D}; font-size:17pt; line-height:1; width:0.35in; flex-shrink:0; }}
.role .tx .a {{ font-family:'Oswald',sans-serif; font-weight:700; text-transform:uppercase; letter-spacing:.04em; font-size:10pt; color:{NAVY}; }}
.role .tx .a span {{ color:{GOLD_D}; }}
.role .tx p {{ font-size:8.9pt; line-height:1.42; margin-top:2px; }}
.role .tx .time {{ font-family:'Oswald',sans-serif; font-style:normal; text-transform:uppercase; letter-spacing:.05em; font-size:7pt; color:{SLATE}; margin-top:3px; }}

/* weekend arc messages */
.msg {{ display:flex; gap:0; margin-bottom:8px; border-radius:6px; overflow:hidden; }}
.msg .ltr {{ width:0.95in; color:#fff; display:flex; flex-direction:column; align-items:center; justify-content:center; padding:10px 0; flex-shrink:0; }}
.msg .ltr .n {{ font-family:'Oswald',sans-serif; font-weight:500; font-size:7pt; letter-spacing:.1em; text-transform:uppercase; opacity:.85; }}
.msg .ltr .h {{ font-family:'Anton',sans-serif; font-size:14pt; line-height:1; }}
.msg .mid {{ flex:1; background:{CREAM}; padding:9px 14px; }}
.msg .mid .ttl {{ font-family:'Oswald',sans-serif; font-weight:700; text-transform:uppercase; letter-spacing:.03em; font-size:9.5pt; color:{NAVY}; }}
.msg .mid .idea {{ font-size:8.7pt; line-height:1.4; margin-top:2px; color:#3c4350; }}
.msg .mid .txt {{ font-family:'Oswald',sans-serif; font-weight:500; text-transform:uppercase; letter-spacing:.05em; font-size:6.8pt; color:{GOLD_D}; margin-top:3px; }}

/* outcomes / fears */
.oc {{ display:flex; flex-wrap:wrap; gap:9px; margin-bottom:14px; }}
.oc .o {{ flex:1 1 46%; background:{CREAM}; border-radius:6px; border-top:3px solid {GREEN}; padding:10px 13px; }}
.oc .o .t {{ font-family:'Oswald',sans-serif; font-weight:700; text-transform:uppercase; letter-spacing:.04em; font-size:9pt; color:{GREEN}; }}
.oc .o p {{ font-size:8.7pt; line-height:1.4; margin-top:3px; }}
.fearbox {{ margin-bottom:9px; border-radius:6px; overflow:hidden; border:1px solid #ECE3D0; }}
.fearbox .f {{ background:{NAVY}; color:#fff; font-family:'Lora',serif; font-style:italic; font-size:9.6pt; padding:7px 14px; }}
.fearbox .f:before {{ content:'\\201C'; color:{GOLD}; }} .fearbox .f:after {{ content:'\\201D'; color:{GOLD}; }}
.fearbox .a {{ background:{CREAM}; padding:7px 14px; font-size:8.7pt; line-height:1.42; }}

/* closing */
.closing {{ background:{NAVY}; color:{CREAM}; }}
.closing .inner {{ position:absolute; inset:0; padding:1.2in 0.85in 0.95in; display:flex; flex-direction:column; }}
.closing .kick {{ color:{GOLD}; letter-spacing:.28em; }}
.closing h2 {{ font-family:'Anton',sans-serif; text-transform:uppercase; color:#fff; font-size:48pt; line-height:.95; margin-top:8px; }}
.closing h2 .gold {{ color:{GOLD}; }}
.closing .pk {{ font-family:'Lora',serif; font-style:italic; font-size:14pt; color:#D9CCAE; margin-top:22px; max-width:5.7in; }}
.pkg {{ display:flex; flex-direction:column; gap:18px; margin-top:0.5in; margin-bottom:auto; }}
.pkg .it {{ display:flex; gap:16px; align-items:flex-start; }}
.pkg .n {{ font-family:'Anton',sans-serif; color:{GOLD}; font-size:24pt; width:0.55in; line-height:1; }}
.pkg .tx .a {{ font-family:'Oswald',sans-serif; font-weight:600; text-transform:uppercase; letter-spacing:.05em; font-size:12pt; color:#fff; }}
.pkg .tx .b {{ font-family:'Lora',serif; font-style:italic; font-size:10pt; color:#C2CADA; margin-top:2px; }}
.closing .stamp {{ margin-top:0.4in; border-top:2px solid rgba(224,168,46,.4); padding-top:20px; display:flex; justify-content:space-between; align-items:flex-end; }}
.closing .stamp .l {{ font-family:'Lora',serif; font-style:italic; font-size:11pt; color:#D9CCAE; max-width:4.7in; line-height:1.4; }}
.closing .stamp .r {{ font-family:'Oswald',sans-serif; font-weight:600; letter-spacing:.2em; text-transform:uppercase; font-size:8pt; color:{GOLD}; text-align:right; }}
"""

def page(inner, cls=""): return f'<div class="page {cls}">{inner}</div>'
def topband(kick,title,tag): return f'<div class="topband"><div class="kicker kick">{kick}</div><h2>{title}</h2><div class="tag">{tag}</div></div>'
def foot(n): return f'<div class="brandfoot">Wisdom Changes Everything</div><div class="pagenum">Third Base &middot; {n}</div>'

# ---------- COVER ----------
cover = f'''<div class="cv">
  <div class="top"><div class="ghost">40</div></div>
  <div class="bot"></div>
  <div class="inner">
    <div class="toprow">
      <div class="badge-d">Ron Blue Institute</div>
      <div class="badge-d">Third Base &middot; The Catalyst</div>
    </div>
    <div class="eyebrow">A Church-Wide Campaign</div>
    <h1><span class="l1">Wisdom</span><span class="l2">Changes</span><span class="l3">Everything</span></h1>
    <div class="hook">
      <div class="big">40 Days. One Church.<br><span>Everything Changes.</span></div>
      <div class="ln">A synchronized 40-day journey that moves your whole congregation together &mdash; from financial anxiety to biblical wisdom, from ownership to overflow.</div>
      <div class="foot">
        <div class="l">Weekend messages &middot; Small groups &middot; Daily devotionals<br>Built on Ron Blue&rsquo;s 6 H&rsquo;s &middot; Concept draft for review</div>
        <div class="r">Wisdom &rarr; Culture &rarr;<br>Campaign &rarr; Ministry</div>
      </div>
    </div>
  </div>
</div>'''
P1 = page(cover)

# ---------- PAGE 2: POSITIONING + PROMISE ----------
body2 = f'''
<div class="promise"><div class="lab">The Core Promise</div>
<p>In 40 days, your whole church moves together from financial anxiety to biblical wisdom &mdash; discovering that when God owns everything, everything changes: your heart, your habits, your household, your hope, and your legacy.</p></div>

<div class="h3">What It Is</div>
<p style="font-size:9.6pt; line-height:1.55; margin-bottom:7px">The <strong>catalyst</strong> of the pathway &mdash; the moment the vision your leaders carried (Wisdom) and the culture they built (Culture) becomes an experience the <strong>entire congregation</strong> lives together. Not a fundraising drive, a budgeting class, or a one-time series. A synchronized, church-wide discipleship journey from ownership to overflow.</p>
<p style="font-size:9.6pt; line-height:1.55; margin-bottom:12px">By design it is the bridge between Culture and Ministry. The leadership came ready. The campaign mobilizes the congregation. And what it ignites becomes the living material for an ongoing Financial Wisdom Ministry. <strong>The campaign is the spark &mdash; built to light something that lasts.</strong></p>

<div class="h3">This / Changes / Everything</div>
<div class="tce">
  <div class="b"><div class="h" style="background:{NAVY}">This</div><div class="t">Biblical financial wisdom &mdash; the truth that God owns everything and invites us to steward all He has entrusted.</div></div>
  <div class="b"><div class="h" style="background:{GOLD_D}">Changes</div><div class="t">Transformation &mdash; the way God reshapes our heart, habits, household, finances, generosity, and legacy.</div></div>
  <div class="b"><div class="h" style="background:{GREEN}">Everything</div><div class="t">All of life &mdash; money touches worship, trust, relationships, stress, decisions, family, and God&rsquo;s plan.</div></div>
</div>

<div class="h3">Every Person Walks Away</div>
<div class="cols">
  <div class="col"><ul class="chips">
    <li>Settling the question: <strong>What has God entrusted to me?</strong></li>
    <li>Seeing what their money reveals about what they trust</li>
  </ul></div>
  <div class="col"><ul class="chips">
    <li>Living wisdom they can apply this week</li>
    <li>Moving from pressure toward <strong>peace and freedom</strong></li>
  </ul></div>
</div>
'''
P2 = page(topband("Third Base &middot; The Catalyst",
   'Wisdom <span class="gold">Changes</span> Everything',
   'When God&rsquo;s wisdom begins to shape your financial life, it doesn&rsquo;t stay in one category. It changes everything.') +
   f'<div class="body">{body2}</div>' + foot("Overview"), "content")

# ---------- PAGE 3: STRUCTURE (channels + arc) ----------
arc_rows = ""
arcs = [
 ("1","…What I Own","Honor","What has God entrusted to me?"),
 ("2","…What I Love","Heart","What does my money reveal about me?"),
 ("3","…How I Live","Habits","How do I live wisely day to day?"),
 ("4","…How I Heal","Health","How do I move from pressure to peace?"),
 ("5","…What I Hope For","Hope","What future am I trusting God for?"),
 ("6","…What I Leave Behind","Harvest","What will my life produce for the Kingdom?"),
]
for w,ch,th,q in arcs:
    arc_rows += f'''<tr><td class="wk" style="background:{HC[th]}">{w}</td>
      <td class="changes">{ch}</td><td class="theme">{th}</td><td class="q">{q}</td></tr>'''

body3 = f'''
<div class="h3">The Engine &middot; Three Synchronized Channels</div>
<div class="chan">
  <div class="c"><div class="n">Weekend</div><p>Six messages, one per theme, opening each week for the whole church.</p></div>
  <div class="arrow">&rarr;</div>
  <div class="c"><div class="n">Small Group</div><p>Six gatherings where the theme becomes conversation &amp; accountability.</p></div>
  <div class="arrow">&rarr;</div>
  <div class="c"><div class="n">Daily Home</div><p>Forty short readings with family prompts, between Sundays.</p></div>
</div>
<div class="note" style="margin-bottom:16px">A congregant doesn&rsquo;t hear an idea once &mdash; they encounter it <strong>three ways in the same week</strong>: in worship, in community, and in private. That synchronization is what turns content into culture and a moment into momentum.</div>

<div class="h3">The Six-Week Arc</div>
<table class="arc">{arc_rows}</table>
<div class="note" style="margin-top:10px">The arc climbs from <strong>surrender</strong> (Week 1) to <strong>commissioning</strong> (Week 6). The campaign walks all six H&rsquo;s as a full journey &mdash; the church doesn&rsquo;t just prepare for harvest, it walks all the way into it together as the climax. <em>(The same 6-H framework runs through every base of the pathway.)</em></div>
'''
P3 = page(topband("How It Runs",
   'The <span class="gold">Catalyst</span> Engine',
   'One theme, three channels, six weeks &mdash; reaching every person, every household, every group.') +
   f'<div class="body">{body3}</div>' + foot("Structure"), "content")

# ---------- PAGE 4: THE TWO TOCs ----------
def toc_week(letter_color, wk, theme, sub, days):
    dd = " &middot; ".join(days)
    return f'''<div style="margin-bottom:9px">
      <div style="display:flex; align-items:center; gap:8px; margin-bottom:3px">
        <span style="font-family:'Anton',sans-serif; color:#fff; background:{letter_color}; border-radius:4px; padding:2px 9px; font-size:11pt">{wk}</span>
        <span style="font-family:'Oswald',sans-serif; font-weight:700; text-transform:uppercase; letter-spacing:.06em; font-size:9.5pt; color:{NAVY}">{theme}</span>
        <span style="font-family:'Lora',serif; font-style:italic; color:{GOLD_D}; font-size:8.5pt">{sub}</span>
      </div>
      <div style="font-size:8.3pt; color:{SLATE}; line-height:1.4; padding-left:4px">{dd}</div>
    </div>'''

sessions = [
 ("1 &mdash; When God Owns It All","Honor: The Freedom of Surrender"),
 ("2 &mdash; What Money Reveals","Heart: The Battle Beneath the Budget"),
 ("3 &mdash; Wisdom in Motion","Habits: Small Choices That Shape a Life"),
 ("4 &mdash; From Pressure to Peace","Health: Aligning Faith, Finances, Family"),
 ("5 &mdash; Living for What Lasts","Hope: Generosity, Legacy, Kingdom Impact"),
 ("6 &mdash; Open Hands, Lasting Impact","Harvest: Multiplying Generosity"),
]
sess_html = ""
for s,sub in sessions:
    sess_html += f'''<div style="display:flex; gap:8px; margin-bottom:7px; align-items:baseline">
      <span style="font-family:'Oswald',sans-serif; font-weight:700; color:{NAVY}; font-size:9.3pt">Session {s}</span></div>
      <div style="font-family:'Lora',serif; font-style:italic; color:{SLATE}; font-size:8.4pt; margin:-5px 0 8px 0">{sub}</div>'''

weeks = [
 (NAVY,"1","Honor","This Changes What I Own",["The Owner of Everything","What Has God Entrusted","Open Hands","Owner or Steward?","The Lie of \u201CMine\u201D","Everything on Loan","Surrender Changes the Weight"]),
 (TEAL,"2","Heart","This Changes What I Love",["Where Your Treasure Is","Two Masters","What Money Promises","The Comparison Trap","Fear &amp; False Security","Contentment","A Heart That Trusts"]),
 (GREEN,"3","Habits","This Changes How I Live",["Wisdom You Can Practice","Five Uses of Money","Spend Less Than You Earn","The Slow Fade of Debt","Margin","Plans Are Faith","Small Choices"]),
 (GOLD_D,"4","Health","This Changes How I Heal",["From Pressure to Peace","When Money Steals Sleep","Honesty First","Wisdom Before Wealth","Faith, Finances, Family","Freedom Is the Goal","A Healthier You"]),
 (RUST,"5","Hope","This Changes What I Hope For",["Redefining Success","How Much Is Enough?","Storing Up What Lasts","Eternal Perspective","The Future You Trust","Living Lightly","Hope Money Can&rsquo;t Buy"]),
 (NAVY2,"6","Harvest","This Changes What I Leave Behind",["The Generous Life","Generosity as Worship","A Legacy Worth Leaving","Multiplied for Kingdom","This Changes Everything"]),
]
toc_html = "".join(toc_week(c,w,th,sub,days) for c,w,th,sub,days in weeks)

body4 = f'''
<div class="cols">
  <div class="col">
    <div class="h3">The Small-Group Spine &middot; 6 Sessions</div>
    {sess_html}
  </div>
  <div class="col">
    <div class="h3">The Daily Devotional &middot; 40 Days</div>
    {toc_html}
  </div>
</div>
'''
P4 = page(topband("The Full Journey",
   'What&rsquo;s <span class="gold">Inside</span>',
   'Six small-group sessions and forty daily readings, mapped to the six-week arc.') +
   f'<div class="body">{body4}</div>' + foot("Contents"), "content")

# ---------- SAMPLE BUILDER (session) ----------
def session_page(numlabel, color, title, sub, big, scrips, teaching, qs, app, prayer, pnum):
    qhtml = "".join(f"<li>{q}</li>" for q in qs)
    sc = "<br>".join(scrips)
    inner = f'''<div class="body" style="padding-top:0.5in; padding-bottom:0.3in">
      <div class="samp-head">
        <div class="samp-tag" style="background:{color}"><div class="a">Small Group</div><div class="b">{numlabel}</div></div>
        <div class="samp-title"><h3>{title}</h3><div class="wk">{sub}</div></div>
      </div>
      <div class="blab">The Big Idea</div>
      <div class="samp"><p>{big}</p></div>
      <div class="scrip">{sc}</div>
      <div class="blab">Teaching Summary</div>
      <div class="samp"><p>{teaching}</p></div>
      <div class="blab">Discussion</div>
      <ul class="qlist">{qhtml}</ul>
      <div class="step"><b>This Week&rsquo;s Step</b>{app}</div>
      <div class="pray"><div class="lab">Closing Prayer</div><p>{prayer}</p></div>
    </div>'''
    return page(inner + foot(pnum), "content")

S1 = session_page("Session 1", NAVY, "When God Owns It All", "Week 1 &middot; Honor: The Freedom of Surrender",
  "For the next forty days we ask one question together as a church: <em>what changes when God owns everything?</em> Most of us assume what we earn is ours and handling it well is mostly about being responsible. This week challenges that at the root. The Bible&rsquo;s claim is bigger: God owns it all, and we are stewards of what He has entrusted. That single shift &mdash; from owner to steward &mdash; is where financial wisdom begins, and it changes everything that follows.",
  ["<strong>Psalm 24:1</strong> &mdash; the earth and everything in it belong to the Lord.",
   "<strong>1 Chronicles 29:11&ndash;12</strong> &mdash; everything in heaven and earth is God&rsquo;s.",
   "<strong>Luke 16:11&ndash;12</strong> &mdash; faithful with what belongs to Another, trusted with what is truly ours."],
  "Ron Blue spent his life on four words: God owns it all. And here&rsquo;s why that&rsquo;s good news rather than a loss &mdash; ownership is exhausting. Owners carry pressure and the endless question, <em>How do I make this work?</em> Stewards carry something lighter: an assignment, and one question, <em>How do I faithfully manage what belongs to God?</em> When we stop pretending to own what was always His, the weight changes. We&rsquo;re responsible for faithfulness, and the results belong to God. That&rsquo;s not a smaller life. It&rsquo;s a freer one.",
  ["When you hear &ldquo;God owns it all,&rdquo; what&rsquo;s your honest first reaction?",
   "Where do you most feel the <em>pressure of ownership</em> &mdash; that it all depends on you?",
   "What&rsquo;s the difference between believing it on Sunday and living it on Tuesday?",
   "If you saw yourself as a steward this week, what&rsquo;s one thing that might change?"],
  "Write one sentence where you&rsquo;ll see it daily: &ldquo;This is not mine. I am a steward of what God has entrusted to me.&rdquo; Notice what comes up &mdash; and bring it to the daily readings.",
  "Father, You own everything &mdash; the earth, our lives, and all You&rsquo;ve placed in our hands. We confess how easily we live as if it&rsquo;s ours. Teach us the freedom of open hands, and help us trade the pressure of ownership for the peace of faithful stewardship. Amen.",
  "Session 1")

S2 = session_page("Session 2", TEAL, "What Money Reveals", "Week 2 &middot; Heart: The Battle Beneath the Budget",
  "Your bank statement is one of the most honest spiritual documents you own &mdash; not because money is bad, but because how we handle it reveals what we actually trust, fear, and love. We can profess God is our security on Sunday and reach for money as our security every other day. This week isn&rsquo;t about guilt; it&rsquo;s about clarity. Jesus said where your treasure is, your heart will be also &mdash; so follow your money, and you&rsquo;ll find your heart.",
  ["<strong>Matthew 6:21</strong> &mdash; where your treasure is, your heart will be also.",
   "<strong>Matthew 6:24</strong> &mdash; you cannot serve both God and money.",
   "<strong>Luke 12:15</strong> &mdash; life does not consist in the abundance of possessions."],
  "Jesus treated money as a <em>heart</em> issue because money makes promises only God can keep. It promises security, so we trust it instead of God. It promises worth, so we measure ourselves by it. It promises freedom, so we chase it and find ourselves owned by it. Ron Blue observed money is the chief competitor for our hearts &mdash; the one rival Jesus named by name. The issue is almost never the math; it&rsquo;s what money has come to mean to us. Bring that into the light, and money loses its grip &mdash; not because we budgeted better, but because we stopped asking money to be God.",
  ["If someone studied only your spending, what would they conclude you treasure most?",
   "Which of money&rsquo;s promises pulls hardest &mdash; security, worth, or freedom?",
   "When do you reach for money to calm a fear? What&rsquo;s the fear underneath?",
   "What would change if your worth were already settled in God, not your balance?"],
  "This week, notice &mdash; without judging &mdash; the moments money stirs something in you: anxiety, comparison, the urge to buy. Each time, ask: <em>what is my heart actually looking for right now?</em>",
  "Father, our money tells the truth about our hearts, and we don&rsquo;t always like what it says. Where we&rsquo;ve asked money to be our security, our worth, or our freedom &mdash; forgive us, and free us. Settle our hearts in You, so we hold money with an open hand instead of a clenched one. Amen.",
  "Session 2")

S3 = session_page("Session 3", GREEN, "Wisdom in Motion", "Week 3 &middot; Habits: Small Choices That Shape a Life",
  "For two weeks we&rsquo;ve worked on the inside &mdash; who owns it all, and what our money reveals. But a changed heart still has to live in a world of paychecks and a hundred small decisions a week. This is where many of us get stuck: we believe the right things and nothing actually changes. The freeing truth this week: biblical financial wisdom isn&rsquo;t abstract &mdash; it&rsquo;s livable, practical habits anyone can begin. You don&rsquo;t need a finance degree. You&rsquo;re already becoming someone through your daily money habits; the only question is whether you&rsquo;re becoming that person on purpose.",
  ["<strong>Luke 16:10</strong> &mdash; whoever is faithful with little will be faithful with much.",
   "<strong>Proverbs 21:5</strong> &mdash; the plans of the diligent lead to profit.",
   "<strong>Proverbs 13:11</strong> &mdash; wealth gathered little by little will grow."],
  "Ron Blue distilled biblical financial wisdom into a handful of livable principles: spend less than you earn, avoid debt, build margin, set long-term goals, give generously. None requires expertise &mdash; they require <em>practice.</em> Wisdom isn&rsquo;t primarily something you know; it&rsquo;s something you do, repeatedly, until it becomes who you are. Nobody becomes financially wise in one heroic decision &mdash; they become wise one small, faithful choice at a time, compounded over years. That&rsquo;s wonderful news: you can&rsquo;t always choose your salary, but you can always choose your next decision. Jesus put it plainly &mdash; faithful in little, faithful in much.",
  ["Of Ron&rsquo;s five practices, which comes most naturally to you, and which feels hardest?",
   "Where have you believed the right thing but struggled to actually do it? What gets in the way?",
   "Who are your current money habits forming you into?",
   "What&rsquo;s one small, specific, repeatable choice you could start this week?"],
  "Pick exactly one practice to put in motion &mdash; small enough that you&rsquo;ll actually do it. Track every dollar for seven days, set aside one amount, or pause 24 hours before one purchase. The goal isn&rsquo;t transformation by Sunday; it&rsquo;s proving a wise choice is within reach.",
  "Father, we&rsquo;ve believed the right things about money &mdash; now help us live them. Give us the grace of small faithfulness: the discipline to make one wise choice, then another, until wisdom becomes the way we live. Thank You that we don&rsquo;t need to be experts &mdash; only faithful with the little in front of us. Amen.",
  "Session 3")

S4 = session_page("Session 4", GOLD_D, "From Pressure to Peace", "Week 4 &middot; Health: Aligning Faith, Finances &amp; Family",
  "Four weeks in, something honest may be surfacing: underneath ownership, the heart, and wise habits, many of us are simply tired. Money has been a source of pressure for so long we&rsquo;ve stopped noticing the weight &mdash; the tightness at the card reader, the silence between spouses, the 2 a.m. math. Here&rsquo;s what this week wants you to hear: God isn&rsquo;t only interested in your stewardship. He&rsquo;s interested in your <em>peace.</em> Financial health isn&rsquo;t only the numbers being right &mdash; it&rsquo;s the whole person, faith and finances and family, coming into alignment so money serves your life instead of strangling it.",
  ["<strong>Matthew 11:28</strong> &mdash; come to me, all who are weary, and I will give you rest.",
   "<strong>Philippians 4:6&ndash;7</strong> &mdash; do not be anxious; the peace of God will guard your hearts.",
   "<strong>Proverbs 17:1</strong> &mdash; better a dry crust with peace than a house full of strife."],
  "Notice the order this journey followed. We started with surrender, not techniques &mdash; because peace doesn&rsquo;t come from controlling your money but from releasing it to the One who owns it anyway. Much of our pressure is the weight of carrying what was never ours to carry alone. And peace is available <em>now</em> &mdash; not on the far side of being debt-free, but today, in the middle of unfinished work. Financial health is a direction, not a destination you must reach before you&rsquo;re allowed to rest. Money and family belong in the same conversation, because financial pressure rarely stays in a spreadsheet &mdash; it leaks into marriages, parenting, and sleep. When faith, finances, and family align, the whole household can breathe.",
  ["Where has money been a pressure you&rsquo;ve simply gotten used to carrying?",
   "How does financial pressure show up in your home, even when no one names it?",
   "&ldquo;Peace is available now, not on the far side of perfect finances.&rdquo; Is that hard to believe? Why?",
   "What would it look like this week to bring one money worry to God instead of carrying it alone?"],
  "Name one financial pressure you&rsquo;ve carried &mdash; out loud, specifically, to God, and if you&rsquo;re comfortable, to one other person. Don&rsquo;t solve it yet. The step is simply to stop carrying it in silence, because silent pressure compounds and shared pressure begins to lift.",
  "Father, we&rsquo;re tired in places we&rsquo;ve stopped admitting. You see the pressure we&rsquo;ve carried around money, and how it&rsquo;s seeped into our homes and our sleep. Thank You that You offer rest, not just instructions. Today we bring the weight to You. Bring our faith, our finances, and our families into alignment, and let our whole households finally breathe. Amen.",
  "Session 4")

S5 = session_page("Session 5", RUST, "Living for What Lasts", "Week 5 &middot; Hope: Generosity, Legacy &amp; Kingdom Impact",
  "Here&rsquo;s a question that quietly reorders a life: <em>what are you actually living for?</em> Most of us run hard toward goals we&rsquo;ve never examined &mdash; more security, more comfort, a bigger number. There&rsquo;s nothing wrong with provision, but Jesus invited us to something larger: to store up treasure where it actually lasts, and to measure our lives by an eternal scoreboard. This week is about hope &mdash; the solid confidence that our lives can count for something beyond our own comfort and our own lifespan. When you live for what lasts, you hold the temporary more loosely and invest in the eternal more freely.",
  ["<strong>Matthew 6:19&ndash;21</strong> &mdash; store up treasures in heaven, where they won&rsquo;t fade.",
   "<strong>1 Timothy 6:6&ndash;8</strong> &mdash; godliness with contentment is great gain.",
   "<strong>2 Corinthians 4:18</strong> &mdash; fix your eyes on what is unseen and eternal."],
  "Two ideas anchor this week. The first is contentment &mdash; Paul called it &ldquo;great gain,&rdquo; the rare ability to say &ldquo;I have enough.&rdquo; In a culture engineered to keep us wanting more, contentment is revolutionary, because it&rsquo;s the only thing that satisfies the hunger more money promises to fill but never does. The second is eternal perspective. Ron Blue taught for decades that how you handle money echoes into eternity &mdash; generosity is an investment in the only economy that lasts forever. What we give away, what we invest in people and God&rsquo;s Kingdom, is the only part of our financial lives that survives us. Everything else stays here. When you fix your hope on the eternal, generosity stops feeling like loss and starts feeling like the smartest investment you&rsquo;ll ever make.",
  ["Be honest: what have you mostly been living for with your money?",
   "Where is contentment hardest &mdash; and what keeps &lsquo;enough&rsquo; always just out of reach?",
   "What does it actually mean to &lsquo;store up treasure in heaven&rsquo; &mdash; practically, for you?",
   "If you fixed your hope on what lasts, what&rsquo;s one thing you&rsquo;d invest in that outlives you?"],
  "Answer one question on paper: <em>What do I want my life and resources to count for &mdash; beyond myself, and beyond my lifetime?</em> Then identify one concrete way to start moving toward it now, however small. Living for what lasts isn&rsquo;t a someday decision; it&rsquo;s a direction you can step toward this week.",
  "Father, lift our eyes. We&rsquo;ve spent so much of our lives running toward things that don&rsquo;t last. Teach us contentment &mdash; the freedom of &lsquo;enough.&rsquo; And teach us to store up treasure where it truly lasts, investing what You&rsquo;ve entrusted to us in people and in Your Kingdom. Fix our hope on what is unseen and eternal. Make our lives count for what matters to You. Amen.",
  "Session 5")

S6 = session_page("Session 6", NAVY2, "Open Hands, Lasting Impact", "Week 6 &middot; Harvest: Multiplying Generosity for Kingdom Purpose",
  "We started six weeks ago with a single, unsettling truth: God owns it all. We&rsquo;ve followed it through the heart, the habits, the healing, and the hope. Today we arrive where the journey was always heading &mdash; the harvest. The point of financial wisdom was never just freedom <em>from</em> something &mdash; debt, pressure, anxiety. It was freedom <em>for</em> something. God sets us free so we can become generous. The open hand that received everything as a gift is the same open hand that gives. This is the climax &mdash; not a tighter grip on a healthier balance, but a looser grip and a bigger life.",
  ["<strong>2 Corinthians 9:6&ndash;8</strong> &mdash; God loves a cheerful giver and supplies all we need.",
   "<strong>Luke 6:38</strong> &mdash; give, and it will be given to you, pressed down and overflowing.",
   "<strong>1 Timothy 6:18&ndash;19</strong> &mdash; be generous, storing up treasure for the life that is truly life."],
  "Generosity is not the tax you pay for being blessed &mdash; it&rsquo;s the evidence that the journey worked. The pattern has held all six weeks: believe God owns it all (Honor), see what money does to your heart (Heart), build wise habits (Habits), find peace instead of pressure (Health), fix your hope on what lasts (Hope) &mdash; and generosity isn&rsquo;t forced. It overflows. Ron Blue spent his life proving it: giving is a result, not a goal. You don&rsquo;t manufacture a generous life by gritting your teeth; you become generous by becoming free, and the free person can&rsquo;t help but open their hands. And notice the word <em>multiplying</em> &mdash; generosity spreads. One open-handed person makes others braver. A church full of it can change a community.",
  ["Over six weeks &mdash; Honor, Heart, Habits, Health, Hope &mdash; which changed you most, and why?",
   "Where have you noticed your grip loosening? Where is it still tight?",
   "What&rsquo;s the difference between giving out of obligation and giving out of overflow?",
   "If generosity is the harvest of this journey, what&rsquo;s one way to live more open-handed this week?"],
  "Pick one concrete act of generosity for the next seven days &mdash; not a vague intention, a specific act. Then think past it: this campaign ends, but the journey doesn&rsquo;t have to. Talk as a group about how you&rsquo;ll keep going. The 40 days were the spark; what you do now decides whether it becomes a fire.",
  "Father, six weeks ago we admitted that You own it all. Today we&rsquo;ve seen where that truth leads &mdash; to open hands and a generous life. Don&rsquo;t let it stop here. Make us a people marked not by what we hold, but by what we give &mdash; for the good of others, the joy of our own hearts, and the advance of Your Kingdom. This changes everything. Amen.",
  "Session 6")

# ---------- DEVOTIONAL WEEK PAGE (compact, all 7) ----------
def dev_card(day, title, scrip, body, color):
    return f'''<div style="margin-bottom:9px; border-radius:6px; overflow:hidden; border:1px solid #ECE3D0;">
      <div style="display:flex; align-items:center; gap:10px; background:{color}; color:#fff; padding:6px 12px">
        <span style="font-family:'Anton',sans-serif; font-size:12pt">{day}</span>
        <span style="font-family:'Oswald',sans-serif; font-weight:700; text-transform:uppercase; letter-spacing:.04em; font-size:9.5pt">{title}</span>
        <span style="margin-left:auto; font-family:'Lora',serif; font-style:italic; font-size:7.6pt; opacity:.85">{scrip}</span>
      </div>
      <div style="background:#fff; padding:7px 12px; font-size:8.5pt; line-height:1.44">{body}</div>
    </div>'''

devs = [
 ("1","The Owner of Everything","Psalm 24:1","Most of us carry a quiet weight we&rsquo;ve never named &mdash; <em>this is all mine, and it depends on me.</em> Day one questions that: God owns everything, and you steward what He&rsquo;s placed in your hands. Ownership produces pressure; stewardship produces peace. Wisdom begins not with a budget, but with surrender.",NAVY),
 ("2","What Has God Entrusted to Me?","1 Peter 4:10","A steward&rsquo;s first job is to know what they&rsquo;ve been given &mdash; and it&rsquo;s bigger than money: time, abilities, relationships, a family, a season. The owner asks what to do with his stuff; the steward asks what the Owner wants done with what&rsquo;s in his care.",NAVY),
 ("3","The Freedom of Open Hands","Job 1:21","A clenched hand can&rsquo;t receive or give &mdash; only guard. The open hand holds the same things without the death grip, free to enjoy them as gifts and release them in trust. Open hands aren&rsquo;t a loss of security; they&rsquo;re where real security was always found.",NAVY),
 ("4","Owner or Steward?","1 Corinthians 4:2","Every money decision sits at one fork: owner or steward? The owner&rsquo;s standard is always <em>more</em> and never rests. The steward&rsquo;s standard is faithfulness &mdash; a finish line you can actually cross tonight. Same money, two entirely different weights.",NAVY),
 ("5","The Lie of \u201CMine\u201D","1 Corinthians 4:7","The little word &ldquo;mine&rdquo; hides a lie that breeds anxiety, comparison, and a tight grip. Paul punctures it: <em>what do you have that you did not receive?</em> If everything was received, anxiety eases, comparison loses fuel, and the grip can loosen.",NAVY),
 ("6","Everything Is on Loan","1 Timothy 6:7","You came with nothing and will leave with nothing &mdash; everything between is on loan. Far from bleak, it&rsquo;s freeing: you don&rsquo;t have to grip it forever or find your identity in it. Steward it well, enjoy it, hold it ready to return. Travel light.",NAVY),
 ("7","Surrender Changes the Weight","1 Peter 5:7","The week&rsquo;s quiet movement has been surrender &mdash; not giving up, but setting down a weight never meant to be carried alone. &ldquo;Cast all your anxiety on Him.&rdquo; It&rsquo;s the doorway to everything ahead: <em>It was never mine. It&rsquo;s His. And I can finally rest.</em>",NAVY),
]
dev_html = "".join(dev_card(*d) for d in devs)
body_dev = f'''
<div class="note" style="margin-bottom:11px">The daily devotional carries each week&rsquo;s theme into the home. Here is the full <strong>Honor week</strong> &mdash; seven readings that build deliberately from <em>it&rsquo;s all His</em> to <em>surrender and rest.</em> Each day in the published resource also includes Reflect, a Household prompt, a Prayer, and One Step.</div>
{dev_html}
'''
PDEV = page(topband("The Daily Rhythm",
   'Sample Week &middot; <span class="gold">Honor</span>',
   'What a congregant lives at home &mdash; Days 1&ndash;7, the complete first week.') +
   f'<div class="body">{body_dev}</div>' + foot("Devotional Week"), "content")

# ---------- LAUNCH PATHWAY PAGE ----------
launch = [
 ("8 Weeks Out","Decide &amp; Build the Team","Pastor commits, names a campaign point person, recruits group leaders, sets the 40-day window.","Output: a date and a team."),
 ("6 Weeks Out","Train &amp; Prepare","Leaders walk the six sessions themselves; the preaching pastor maps six messages; materials in hand.","Output: trained leaders, a preaching plan."),
 ("4 Weeks Out","Promote &amp; Recruit Groups","Congregational promotion begins; group sign-ups open. The decisive phase &mdash; get people into groups before Day 1.","Output: groups filling, church aware."),
 ("2 Weeks Out","Final Push","Last call for sign-ups; distribute devotionals so everyone has theirs before Day 1; leaders confirm rosters.","Output: everyone equipped and placed."),
 ("Weeks 1&ndash;6","Run the Campaign","The rhythm runs itself: weekend opens &rarr; groups deepen &rarr; daily readings carry it home &rarr; repeat.","Output: a synchronized church, week over week."),
 ("Day 40","Land It &amp; Hand It Off","A commissioning weekend. Celebrate, gather testimonies, and name the next step before momentum cools.","Output: testimonies captured, next step named."),
]
ltl = ""
for w,t,p,o in launch:
    ltl += f'''<div class="tl2"><div class="when"><div class="b">{w.split(' ')[0]}{(' '+w.split(' ',1)[1]) if ' ' in w else ''}</div></div>
      <div class="dot"></div><div class="c"><div class="t">{t}</div><p>{p} <span class="o">{o}</span></p></div></div>'''
# simpler: rebuild when labels cleanly
ltl = ""
for w,t,p,o in launch:
    ltl += f'''<div class="tl2"><div class="when"><div class="b">{w}</div></div>
      <div class="dot"></div><div class="c"><div class="t">{t}</div><p>{p} <span class="o">{o}</span></p></div></div>'''
body_launch = f'''
<div class="note" style="margin-bottom:13px">A campaign isn&rsquo;t read &mdash; it&rsquo;s run. The work front-loads: most effort lands in the weeks <strong>before</strong> Day 1. Here is the full arc, from decision to handoff.</div>
<div class="tl2wrap">{ltl}</div>
<div class="keyrule"><div class="lab">The One Rule That Makes or Breaks It</div>
<p>The campaign succeeds or fails on <strong style="color:#fff">group enrollment before Day 1</strong>. A church that gets people into groups in the four weeks prior runs a movement; a church that launches with empty groups runs a sermon series. <span class="key">Front-load the group push.</span></p></div>
'''
PL = page(topband("What It Takes to Run It",
   'The <span class="gold">Launch</span> Pathway',
   'From the decision to launch through the handoff to ongoing ministry &mdash; the operational answer.') +
   f'<div class="body">{body_launch}</div>' + foot("Launch"), "content")

# ---------- ROLES + WEEKEND ARC PAGE ----------
roles = [
 ("01","The Voice","Senior / Preaching Pastor","Preaches the six weekend messages and lends the campaign his weight. His visible conviction gives the whole church permission to engage.","Time: the six messages &mdash; his regular preaching."),
 ("02","The Engine","Campaign Point Person","The single owner who makes it run &mdash; timeline, materials, sign-ups, stories. Often an executive or discipleship pastor. Most determines success.","Role: clear ownership, start to finish."),
 ("03","The Heart","Small Group Leaders","Lead the six sessions where transformation moves from idea to action. No financial expertise needed &mdash; the guide carries them.","Time: six sessions plus light prep."),
 ("04","The Megaphone","Communications Person","Drives the four-week promotional push &mdash; announcements, video, lobby, digital, sign-ups. Critical in pre-launch.","Time: concentrated before Day 1."),
]
rhtml = ""
for n,t,who,p,time in roles:
    rhtml += f'''<div class="role"><div class="ico">{n}</div><div class="tx">
      <div class="a">{who} <span>&middot; {t}</span></div><p>{p}</p><div class="time">{time}</div></div></div>'''

msgs = [
 ("1","Honor","This Changes What I Own","God owns it all &mdash; the truth that reframes everything. From owner to steward.","Psalm 24:1 &middot; 1 Chron 29",NAVY),
 ("2","Heart","This Changes What I Love","Your money reveals what you actually trust and treasure.","Matthew 6:21, 24",TEAL),
 ("3","Habits","This Changes How I Live","Wisdom is livable &mdash; small faithful choices shape a life.","Luke 16:10 &middot; Prov 21:5",GREEN),
 ("4","Health","This Changes How I Heal","Wisdom brings peace, margin, and freedom &mdash; God&rsquo;s care for the whole person.","Matt 11:28 &middot; Phil 4:6",GOLD_D),
 ("5","Hope","This Changes What I Hope For","Contentment and eternity reframe success and &lsquo;how much is enough.&rsquo;","Matt 6:19 &middot; 1 Tim 6:6",RUST),
 ("6","Harvest","This Changes What I Leave Behind","Generosity as worship and legacy &mdash; the commissioning climax.","2 Corinthians 9:6&ndash;8",NAVY2),
]
mhtml = ""
for n,h,t,idea,txt,c in msgs:
    mhtml += f'''<div class="msg"><div class="ltr" style="background:{c}"><div class="n">Msg {n}</div><div class="h">{h[0]}</div></div>
      <div class="mid"><div class="ttl">{h} &middot; {t}</div><div class="idea">{idea}</div><div class="txt">{txt}</div></div></div>'''

body_rw = f'''
<div class="h3">Who Does What &mdash; Four Roles</div>
{rhtml}
<div class="note" style="margin:2px 0 14px">Four roles. None require financial expertise &mdash; the framework, sessions, and devotionals carry the content. The team just carries the people.</div>
<div class="h3">The Weekend Message Arc &mdash; the Pulpit</div>
{mhtml}
'''
PR = page(topband("Who Runs It &amp; The Pulpit",
   'Roles &amp; the <span class="gold">Weekend</span> Arc',
   'The handful of seats a campaign needs &mdash; and the six-message arc that anchors each week.') +
   f'<div class="body">{body_rw}</div>' + foot("Roles &amp; Messages"), "content")

# ---------- OUTCOMES + FEARS PAGE ----------
ocs = [
 ("Groups Multiply","One of the most effective group-formation engines a church has &mdash; often forming dozens of new groups and connecting a large share of attendance into community."),
 ("Generosity Rises","As spiritual depth and alignment grow, giving tends to follow &mdash; as fruit, never the goal or the pitch."),
 ("A Moment of Unity","A whole congregation on one journey creates momentum and a shared reset no single sermon can manufacture."),
 ("It Anchors the Year","A single 40-day campaign can become the spine of a 12-month plan &mdash; and the on-ramp to a permanent ministry."),
]
ochtml = "".join(f'<div class="o"><div class="t">{t}</div><p>{p}</p></div>' for t,p in ocs)
fears = [
 ("We don&rsquo;t have staff bandwidth.","Turnkey by design &mdash; sessions, devotionals, and messages are provided. The point person coordinates; they don&rsquo;t create from scratch."),
 ("Our small groups aren&rsquo;t strong enough.","The campaign IS the on-ramp that births and strengthens groups &mdash; it doesn&rsquo;t require strong groups, it builds them."),
 ("Our calendar is already full.","40 days drops into a preaching season you&rsquo;d already fill &mdash; it replaces, it doesn&rsquo;t add. Shorter 21/30-day options exist."),
 ("What happens after 40 days?","This is the bridge, not the destination. Day 40 hands directly to the ongoing ministry &mdash; built to launch something permanent."),
]
fhtml = "".join(f'<div class="fearbox"><div class="f">{f}</div><div class="a">{a}</div></div>' for f,a in fears)
body_of = f'''
<div class="h3">What Churches Can Expect</div>
<div class="oc">{ochtml}</div>
<div class="h3">Fears This Campaign Answers</div>
{fhtml}
'''
POF = page(topband("Why It Works &amp; What to Expect",
   'Outcomes &amp; <span class="gold">Objections</span>',
   'What a church-wide campaign reliably produces &mdash; and the hesitations it pre-empts.') +
   f'<div class="body">{body_of}</div>' + foot("Outcomes &amp; Fears"), "content")

# ---------- CLOSING ----------
closing = f'''<div class="inner">
  <div class="kicker kick">The Catalyst, Complete</div>
  <h2>One Church.<br>One <span class="gold">Journey.</span><br>40 Days.</h2>
  <div class="pk">Everything a church needs to run it &mdash; the content, the proof across two channels, and the operational plan to execute.</div>
  <div class="pkg">
    <div class="it"><div class="n">01</div><div class="tx"><div class="a">The Content</div><div class="b">Positioning, promise, three-channel structure, and both tables of contents.</div></div></div>
    <div class="it"><div class="n">02</div><div class="tx"><div class="a">The Week-One Proof</div><div class="b">Sessions 1&ndash;2 and the full Honor devotional week &mdash; both channels, fully written.</div></div></div>
    <div class="it"><div class="n">03</div><div class="tx"><div class="a">The Operations</div><div class="b">Launch pathway, four roles, and the six-message weekend arc.</div></div></div>
    <div class="it"><div class="n">04</div><div class="tx"><div class="a">The Persuasion</div><div class="b">Expected outcomes and the objections every pastor is already feeling.</div></div></div>
  </div>
  <div class="stamp">
    <div class="l">Week one is fully written across both channels. Weeks 2&ndash;6 exist as titled outlines, ready to build once the concept is approved.</div>
    <div class="r">Wisdom Changes<br>Everything<br><span style="color:#8893A6">Third Base &middot; The Catalyst</span></div>
  </div>
</div>'''
PC = page(closing, "closing")

HTML_ASSEMBLY_MARKER = True

# ---------- FULL DEVOTIONAL DAY PAGE ----------
def day_page(num, title, theme, scripture, scref, paras, reflect, household, pray, step, pnum):
    body_html = "".join(f'<p>{p}</p>' for p in paras)
    inner = f'''<div class="body" style="padding-top:0.5in; padding-bottom:0.3in">
      <div class="samp-head">
        <div class="samp-tag" style="background:{NAVY}"><div class="a">Devotional</div><div class="b">Day {num}</div></div>
        <div class="samp-title"><h3>{title}</h3><div class="wk">Week 1 &middot; Honor: This Changes What I Own</div></div>
      </div>
      <div class="conv2"><span class="lab">Today&rsquo;s Theme</span> {theme}</div>
      <div class="scrip">{scripture} <span style="font-style:normal; color:{GOLD_D}; font-family:'Oswald',sans-serif; font-weight:600; font-size:8pt; letter-spacing:.04em">&mdash; {scref}</span></div>
      <div class="blab">Reading</div>
      <div class="samp daypara">{body_html}</div>
      <div class="qrow2">
        <div class="qb"><div class="l">Reflect</div><p>{reflect}</p></div>
        <div class="qb"><div class="l">For Your Household</div><p>{household}</p></div>
      </div>
      <div class="pray"><div class="lab">Pray</div><p>{pray}</p></div>
      <div class="step"><b>One Step Today</b>{step}</div>
    </div>'''
    return page(inner + foot(pnum), "content")

DAYS = [
 (1,"The Owner of Everything",
  "Financial wisdom begins with one freeing truth: God owns it all, and you were made to steward &mdash; not to carry &mdash; what He&rsquo;s entrusted to you.",
  "&ldquo;The earth is the Lord&rsquo;s, and everything in it.&rdquo;","Psalm 24:1",
  ["Most of us carry a quiet weight we&rsquo;ve never named. It shows up at the kitchen table when the bills are spread out, or at 2 a.m. when the numbers run through our minds uninvited. Underneath it is an assumption so deep we rarely question it: <em>this is all mine, and it all depends on me.</em>",
   "For the next forty days, we&rsquo;re going to question that assumption together &mdash; and it starts here, on day one, with the most foundational truth in all of Scripture about money. God owns everything. The home you live in, the income you earn, the future you&rsquo;re anxious about &mdash; all of it is His, and you are a steward of what He&rsquo;s placed in your hands for a time.",
   "That might sound at first like a loss. It&rsquo;s actually the doorway to freedom. The owner lies awake worrying about everything. The person simply entrusted with something asks one question: <em>Am I using this well?</em> Ownership produces pressure. Stewardship produces peace. When you stop believing the weight of everything rests on you, you can finally set it down &mdash; not because you&rsquo;ve stopped caring, but because you&rsquo;ve remembered Whose it was all along.",
   "This is where wisdom begins. Not with a budget. With surrender. So we start by simply telling the truth: <em>It was never mine. It&rsquo;s His. And I get to steward it.</em>"],
  "Where in your life are you carrying the weight of ownership &mdash; the feeling that it all depends on you?",
  "At dinner tonight, ask: <em>If we really believed everything we have is a gift from God, what&rsquo;s one thing we might do differently this week?</em>",
  "Father, today I want to tell the truth: You own it all. I have been carrying what was never mine to carry. Teach me the freedom of open hands. Help me live this day as a steward, not an owner. Amen.",
  "Write this where you&rsquo;ll see it this week: &ldquo;This is not mine. I am a steward of what God has entrusted to me.&rdquo;","Day 1"),
 (2,"What Has God Entrusted to Me?",
  "If God owns it all, then everything in your hands is entrusted, not owned &mdash; and that changes how you hold it.",
  "&ldquo;Each of you should use whatever gift you have received to serve others, as faithful stewards of God&rsquo;s grace.&rdquo;","1 Peter 4:10",
  ["Yesterday we said the freeing words: it&rsquo;s all His. Today we ask the natural next question &mdash; <em>so what, exactly, has He entrusted to me?</em> Because a steward&rsquo;s first job is to know what they&rsquo;ve been given.",
   "The answer is bigger than your bank account. God has entrusted you with income, yes &mdash; but also with time, abilities, relationships, influence, a body, a family, a season of life. Money is just the most measurable piece of a much larger trust. The owner asks, <em>What do I want to do with my stuff?</em> The steward asks, <em>What does the Owner want done with what He&rsquo;s placed in my care?</em>",
   "That second question is quieter and far more freeing. It lifts the burden of <em>accumulating</em> and replaces it with the clarity of <em>managing.</em> You&rsquo;re no longer trying to build the biggest pile. You&rsquo;re trying to be found faithful with the specific trust you&rsquo;ve been handed &mdash; a goal you can actually reach, at any income, in any season.",
   "So take inventory honestly today. Not just your money &mdash; your whole trust. Naming it is the beginning of stewarding it well."],
  "Beyond money, what has God entrusted to you that you rarely think of as &lsquo;on loan&rsquo;? How would you hold it differently if you did?",
  "Ask together: <em>What are the three biggest things God has entrusted to our family?</em> See if money even makes the top of the list.",
  "Father, thank You for everything You&rsquo;ve placed in my care &mdash; far more than I usually notice. Help me see all of it as a trust, not a possession. Make me faithful with what You&rsquo;ve actually given, instead of anxious about what I don&rsquo;t have. Amen.",
  "Write a short list: <em>What has God entrusted to me?</em> Include more than money. Keep it where you&rsquo;ll see it.","Day 2"),
 (3,"The Freedom of Open Hands",
  "A closed hand can&rsquo;t receive or give; the open hand is the posture of both freedom and trust.",
  "&ldquo;Naked I came from my mother&rsquo;s womb, and naked I will depart. The Lord gave and the Lord has taken away; may the name of the Lord be praised.&rdquo;","Job 1:21",
  ["Picture two hands. One is clenched tight around what it holds &mdash; knuckles white, gripping, guarding. The other is open, palm up, holding the same thing loosely. Both can hold. But only the open hand can receive something new, and only the open hand can give. The clenched hand is stuck &mdash; it can only defend what it already has.",
   "That&rsquo;s a picture of two ways to live with money. The clenched life is exhausting; it can never quite enjoy what it holds because it&rsquo;s too busy protecting it. The open-handed life holds the same things &mdash; a home, an income, a future &mdash; but without the death grip. It can enjoy them as gifts and release them when needed.",
   "Job said it from the hardest place imaginable: <em>the Lord gave, and the Lord has taken away.</em> He&rsquo;d lost nearly everything, and still his hands stayed open. That&rsquo;s not resignation &mdash; it&rsquo;s trust. Open hands aren&rsquo;t a loss of security. They&rsquo;re the only place real security was ever found &mdash; not in the grip, but in the Giver.",
   "You don&rsquo;t have to manufacture this. You just have to loosen, a finger at a time. The open hand is lighter than the clenched one. Always was."],
  "What are you currently holding with a clenched fist? What would it feel like &mdash; just today &mdash; to open that hand a little?",
  "Talk about it: <em>Where as a family do we hold on tightest? What might it look like to hold that more loosely?</em>",
  "Father, I&rsquo;ve been gripping things that were never mine to clench. Loosen my hands. Teach me that open hands are free hands &mdash; able to receive Your gifts and release them in trust. Whatever You give and take, may I praise You with open palms. Amen.",
  "Sometime today, physically open your hands, palms up, and pray one sentence of release over something you&rsquo;ve been gripping.","Day 3"),
 (4,"Owner or Steward?",
  "The single most important financial question isn&rsquo;t how much you have &mdash; it&rsquo;s whether you live as an owner or a steward.",
  "&ldquo;Moreover, it is required of stewards that they be found faithful.&rdquo;","1 Corinthians 4:2",
  ["Everything in this first week comes down to one fork in the road, and you stand at it with every financial decision: <em>Am I an owner or a steward?</em> The two look identical from outside &mdash; both work, plan, save, and spend. But underneath, they&rsquo;re living in two completely different stories.",
   "The owner&rsquo;s story is about control and accumulation. <em>It&rsquo;s mine. I earned it. I&rsquo;m responsible for making it grow and keeping it safe.</em> It sounds responsible, and it&rsquo;s crushing &mdash; because an owner carries the full weight of outcomes they can&rsquo;t control.",
   "The steward&rsquo;s story is about faithfulness and trust. <em>It&rsquo;s His. My job is to manage it well and leave the results to Him.</em> The steward has only one measure of success, and it&rsquo;s reachable: faithfulness. Not successful. Not wealthy. Faithful.",
   "The owner can never rest, because the standard is always <em>more</em> and the goalposts move forever. The steward can rest tonight, because the standard is <em>faithful with what I was given today.</em> Same money, two entirely different weights to carry."],
  "In your honest day-to-day living &mdash; not your theology &mdash; are you operating more like an owner or a steward? Where&rsquo;s the tell?",
  "Ask: <em>Where do we act most like owners? Where are we learning to act like stewards?</em>",
  "Father, I want to live as a steward, not an owner &mdash; but my instincts run the other way. Retrain me. Let faithfulness, not accumulation, be how I measure a good day. Free me from the owner&rsquo;s endless &lsquo;more,&rsquo; and give me the steward&rsquo;s rest. Amen.",
  "Before one financial decision today &mdash; any size &mdash; pause and ask: <em>Owner or steward? What would a faithful steward do here?</em>","Day 4"),
 (5,"The Lie of &ldquo;Mine&rdquo;",
  "The little word &lsquo;mine&rsquo; carries a lie that quietly drives anxiety, comparison, and a tight grip &mdash; and the truth sets us free from all three.",
  "&ldquo;What do you have that you did not receive? And if you did receive it, why do you boast as though you did not?&rdquo;","1 Corinthians 4:7",
  ["It&rsquo;s one of the first words we learn as children and one of the hardest to outgrow: <em>mine.</em> We say it without thinking &mdash; my money, my house, my career. And mostly that&rsquo;s just language. But underneath the word can hide a lie, and the lie does real damage.",
   "The lie of &lsquo;mine&rsquo; says: <em>I made this. It depends on me. I have to protect it.</em> And the moment we believe that, three things follow. Anxiety &mdash; because if it&rsquo;s all mine to protect, I&rsquo;m carrying a weight I can&rsquo;t bear. Comparison &mdash; because if it&rsquo;s mine by my effort, your having more must mean I&rsquo;ve fallen short. And a tight grip &mdash; because if it&rsquo;s mine alone, I can&rsquo;t afford to be generous.",
   "Paul punctures it with a single question: <em>What do you have that you did not receive?</em> The honest answer is: nothing. The ability to earn, the health to work, the mind to plan &mdash; all received. The skill you&rsquo;re proud of was a gift before it was an achievement.",
   "This isn&rsquo;t meant to shame you. It&rsquo;s meant to free you. If everything was received, anxiety eases, comparison loses its fuel, and the grip can loosen. &lsquo;Mine&rsquo; is a small word with a heavy lie. &lsquo;Received&rsquo; is the truth that lifts it."],
  "Where does the word &lsquo;mine&rsquo; carry the most weight for you &mdash; and which does it produce most: anxiety, comparison, or a tight grip?",
  "Talk about it: <em>What&rsquo;s something we call &lsquo;ours&rsquo; that we&rsquo;d be wise to start calling &lsquo;entrusted&rsquo;?</em>",
  "Father, forgive me for the lie hidden in the word &lsquo;mine.&rsquo; Everything I have, I received from You. Free me from the anxiety, the comparison, and the grip that come from forgetting it. Let gratitude replace ownership in my heart today. Amen.",
  "Catch yourself saying or thinking &lsquo;mine&rsquo; today. Each time, silently rephrase it: <em>entrusted to me.</em>","Day 5"),
 (6,"Everything Is on Loan",
  "We arrive with nothing and leave with nothing; everything in between is on loan &mdash; and that truth makes us lighter, not poorer.",
  "&ldquo;For we brought nothing into the world, and we can take nothing out of it.&rdquo;","1 Timothy 6:7",
  ["There&rsquo;s a clarifying thought that puts every financial worry in its place: you have never permanently owned anything, and you never will. You came into the world with nothing. You will leave it the same way. Everything you&rsquo;ll ever have is something you hold for a while in between. It&rsquo;s all on loan.",
   "This sounds, at first, a little bleak. It&rsquo;s actually one of the lightest, most freeing truths in Scripture. If it&rsquo;s all on loan, several burdens lift at once. You don&rsquo;t have to grip it forever &mdash; you couldn&rsquo;t anyway. You don&rsquo;t have to find your identity in it &mdash; it&rsquo;s not staying. And you don&rsquo;t have to fear losing it the way an owner fears.",
   "A loan changes how you treat a thing. You use a borrowed tool carefully and return it well &mdash; but you don&rsquo;t build your life around it or panic about it. That&rsquo;s exactly the posture Scripture invites toward everything we have. Steward it well. Enjoy it as a gift. Hold it ready to return.",
   "This is why a stewardship mindset produces such peace. The owner is terrified of loss, because loss feels like losing part of himself. The steward holds it all as a loan and can face change with a steadiness the owner never knows. Everything is on loan. Travel light."],
  "What do you treat as permanently yours that&rsquo;s actually on loan? How would holding it as &lsquo;borrowed&rsquo; change the way you carry it?",
  "Ask: <em>If we really lived like everything is on loan, what&rsquo;s one thing we&rsquo;d worry about less?</em>",
  "Father, I brought nothing in and I&rsquo;ll take nothing out. Everything between is Yours, on loan to me for a while. Free me from gripping what I can&rsquo;t keep. Let me steward it well, enjoy it gratefully, and hold it all lightly &mdash; because You are the only treasure that lasts. Amen.",
  "Look around at what you &lsquo;own&rsquo; today and silently name it for what it is: <em>on loan, and that&rsquo;s okay.</em>","Day 6"),
 (7,"Surrender Changes the Weight",
  "Surrender isn&rsquo;t giving up &mdash; it&rsquo;s setting down a weight you were never meant to carry, and it&rsquo;s the doorway to everything that follows.",
  "&ldquo;Cast all your anxiety on him because he cares for you.&rdquo;","1 Peter 5:7",
  ["We&rsquo;ve reached the end of the first week, and it&rsquo;s worth pausing to feel how far the ground has shifted. We began with a truth &mdash; God owns it all &mdash; and followed it through entrustment, open hands, the steward&rsquo;s question, the lie of &lsquo;mine,&rsquo; and the loan we hold for a while. Underneath all of it has been one quiet movement: <em>surrender.</em>",
   "Surrender scares people, because it sounds like loss &mdash; giving up, going without. But financial surrender is the opposite of loss. It&rsquo;s setting down a weight. For years you may have carried the full burden of your finances as if everything depended on you. That weight is crushing precisely because it was never yours to carry alone. Surrender doesn&rsquo;t add a burden. It removes one.",
   "&lsquo;Cast all your anxiety on him.&rsquo; Notice the verb &mdash; <em>cast,</em> throw it off, hand it over. And the reason &mdash; <em>because he cares for you.</em> This isn&rsquo;t God demanding your resources. It&rsquo;s God offering to carry what&rsquo;s been breaking your back.",
   "This is why surrender is the doorway to the whole journey ahead. Everything still to come &mdash; the heart, the habits, the peace, the hope, the generosity &mdash; grows out of this one act of setting the weight down. So we end week one where we began, but lighter: <em>It was never mine. It&rsquo;s His. And I can finally rest.</em>"],
  "What weight around money have you been carrying as if it all depends on you? What would it feel like to genuinely hand it over today?",
  "Look back together: <em>What&rsquo;s one way we&rsquo;re already thinking differently about money than we were a week ago?</em>",
  "Father, this week You&rsquo;ve been loosening my grip, one finger at a time. Today I want to cast the whole weight onto You &mdash; the provision, the fear, the future &mdash; because You care for me and You own it all. Thank You that surrender isn&rsquo;t loss. It&rsquo;s rest. Amen.",
  "Name the heaviest money weight you&rsquo;ve carried this week, and pray one sentence handing it to God. Then notice how the rest of the day feels.","Day 7"),
]
DAYPAGES = "".join(day_page(*d) for d in DAYS)

# extra CSS appended for day format
CSS += f"""
.conv2 {{ background:{CREAM}; border-left:4px solid {GOLD}; padding:9px 14px; border-radius:0 5px 5px 0; margin-bottom:8px; font-size:9.6pt; line-height:1.45; }}
.conv2 .lab {{ font-family:'Oswald',sans-serif; font-weight:700; text-transform:uppercase; letter-spacing:.13em; font-size:7.5pt; color:{GOLD_D}; margin-right:6px; }}
.daypara p {{ font-size:9.4pt; line-height:1.52; margin-bottom:6px; }}
.qrow2 {{ display:flex; gap:10px; margin-top:9px; }}
.qb {{ flex:1; background:#fff; border:1.5px solid #E7DEC9; border-top:3px solid {GOLD}; border-radius:5px; padding:9px 12px; }}
.qb .l {{ font-family:'Oswald',sans-serif; font-weight:700; text-transform:uppercase; letter-spacing:.06em; font-size:7.5pt; color:{NAVY}; margin-bottom:3px; }}
.qb p {{ font-family:'Lora',serif; font-size:8.7pt; line-height:1.4; color:#3c4350; }}
"""

# Update the compact devotional page subtitle to read as a week-at-a-glance lead-in
PDEV = PDEV.replace("What a congregant lives at home &mdash; Days 1&ndash;7, the complete first week.",
                    "Week at a glance &mdash; the seven readings that follow, in full.")

HTML = f"<!doctype html><html><head><meta charset='utf-8'><style>{CSS}</style></head><body>{P1}{P2}{P3}{P4}{S1}{S2}{S3}{S4}{S5}{S6}{PDEV}{DAYPAGES}{PL}{PR}{POF}{PC}</body></html>"
pathlib.Path("/home/claude/camp.html").write_text(HTML)
weasyprint.HTML(string=HTML).write_pdf("/home/claude/Wisdom_Changes_Everything_Campaign.pdf")
print("campaign PDF built")
