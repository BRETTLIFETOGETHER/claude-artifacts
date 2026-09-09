#!/usr/bin/env python3
import weasyprint, base64, pathlib

F = pathlib.Path("/home/claude/fonts")
def b64(p): return base64.b64encode((F/p).read_bytes()).decode()
anton, oswald, lora, lora_it = b64("Anton-Regular.ttf"), b64("Oswald.ttf"), b64("Lora.ttf"), b64("Lora-Italic.ttf")

# ---- Brand palette ----
NAVY   = "#15233F"
NAVY2  = "#1E3358"
GOLD   = "#E0A82E"
GOLD_D = "#C8941A"
CREAM  = "#FBF7EF"
PAPER  = "#FFFFFF"
INK    = "#23262B"
SLATE  = "#5A6472"
GREEN  = "#2E5D46"
TEAL   = "#2C6E7F"
RUST   = "#B5532A"

CSS = f"""
@font-face {{ font-family:'Anton'; src:url(data:font/ttf;base64,{anton}); }}
@font-face {{ font-family:'Oswald'; src:url(data:font/ttf;base64,{oswald}); }}
@font-face {{ font-family:'Lora'; src:url(data:font/ttf;base64,{lora}); font-style:normal; }}
@font-face {{ font-family:'Lora'; src:url(data:font/ttf;base64,{lora_it}); font-style:italic; }}

@page {{ size: 8.5in 11in; margin: 0; }}
* {{ margin:0; padding:0; box-sizing:border-box; }}
html {{ -weasy-hyphens:none; }}
body {{ font-family:'Lora',serif; color:{INK}; font-size:9.6pt; line-height:1.5; }}

.page {{ width:8.5in; height:11in; position:relative; overflow:hidden; page-break-after:always; background:{PAPER}; }}
.page:last-child {{ page-break-after:auto; }}

/* ---------- shared type ---------- */
.kicker {{ font-family:'Oswald',sans-serif; font-weight:600; letter-spacing:.22em; text-transform:uppercase; font-size:8pt; }}
.anton {{ font-family:'Anton',sans-serif; font-weight:400; text-transform:uppercase; letter-spacing:.01em; line-height:.96; }}
.osw {{ font-family:'Oswald',sans-serif; }}
h2.sec {{ font-family:'Anton',sans-serif; text-transform:uppercase; color:{NAVY}; line-height:.95; }}
em,i {{ font-style:italic; }}
strong {{ font-weight:600; }}

/* gold rule motif */
.rule {{ height:4px; background:{GOLD}; border:0; }}
.rule-navy {{ height:3px; background:{NAVY}; border:0; }}

/* ============================================================ COVER */
.cover {{ background:{NAVY}; color:{CREAM}; }}
.cover .bg-h {{ position:absolute; font-family:'Anton',sans-serif; color:rgba(255,255,255,.045);
  font-size:330pt; line-height:.8; top:-0.7in; left:-0.4in; letter-spacing:-.02em; }}
.cover .inner {{ position:absolute; inset:0; padding:0.9in 0.85in; display:flex; flex-direction:column; }}
.cover .toprow {{ display:flex; justify-content:space-between; align-items:center; }}
.badge {{ border:1.5px solid {GOLD}; color:{GOLD}; border-radius:40px; padding:6px 16px;
  font-family:'Oswald',sans-serif; font-weight:600; letter-spacing:.2em; font-size:7.5pt; text-transform:uppercase; }}
.cover .center {{ margin-top:auto; margin-bottom:auto; }}
.cover .eyebrow {{ color:{GOLD}; font-family:'Oswald',sans-serif; font-weight:500; letter-spacing:.36em;
  text-transform:uppercase; font-size:11pt; margin-bottom:18px; }}
.cover h1 {{ font-family:'Anton',sans-serif; font-size:82pt; line-height:.9; text-transform:uppercase; color:#fff; }}
.cover h1 .gold {{ color:{GOLD}; }}
.cover .sub {{ font-family:'Lora',serif; font-style:italic; font-size:17pt; color:#E9DFC9; margin-top:26px; line-height:1.35; max-width:6in; }}
.cover .q {{ border-left:4px solid {GOLD}; padding:14px 0 14px 22px; margin-top:34px; max-width:5.4in;
  font-family:'Lora',serif; font-style:italic; font-size:13pt; color:#fff; line-height:1.45; }}
.cover .foot {{ display:flex; justify-content:space-between; align-items:flex-end; }}
.cover .foot .l {{ font-family:'Oswald',sans-serif; letter-spacing:.04em; font-size:9pt; color:#B9C2D2; line-height:1.7; }}
.cover .foot .r {{ text-align:right; font-family:'Oswald',sans-serif; font-weight:600; letter-spacing:.2em;
  text-transform:uppercase; font-size:8pt; color:{GOLD}; }}
.dotbase {{ display:inline-block; }}

/* ============================================================ generic content page */
.content {{ padding:0; }}
.topband {{ background:{NAVY}; color:#fff; padding:0.42in 0.7in 0.34in; position:relative; }}
.topband .kick {{ color:{GOLD}; }}
.topband h2 {{ font-family:'Anton',sans-serif; text-transform:uppercase; font-size:30pt; line-height:.96; color:#fff; margin-top:7px; }}
.topband h2 .gold {{ color:{GOLD}; }}
.topband .tag {{ font-family:'Lora',serif; font-style:italic; color:#C9D2E0; font-size:10.5pt; margin-top:8px; max-width:6.4in; }}
.body {{ padding:0.34in 0.7in 0.4in; }}

.pagenum {{ position:absolute; bottom:0.34in; right:0.55in; font-family:'Oswald',sans-serif; font-weight:600;
  font-size:8pt; letter-spacing:.18em; color:{SLATE}; text-transform:uppercase; }}
.brandfoot {{ position:absolute; bottom:0.34in; left:0.7in; font-family:'Oswald',sans-serif; font-weight:600;
  font-size:8pt; letter-spacing:.18em; color:{GOLD_D}; text-transform:uppercase; }}

/* promise strip */
.promise {{ background:{GOLD}; color:{NAVY}; padding:18px 24px; border-radius:6px; margin:0 0 20px; }}
.promise .lab {{ font-family:'Oswald',sans-serif; font-weight:700; letter-spacing:.2em; text-transform:uppercase; font-size:8pt; }}
.promise p {{ font-family:'Lora',serif; font-style:italic; font-size:13pt; line-height:1.4; margin-top:6px; }}

/* bases table */
.bases {{ width:100%; border-collapse:separate; border-spacing:0 7px; }}
.bases td {{ padding:11px 14px; vertical-align:middle; }}
.bases .b-tag {{ width:1.55in; font-family:'Anton',sans-serif; text-transform:uppercase; font-size:12.5pt; color:#fff; border-radius:5px 0 0 5px; text-align:center; }}
.bases .b-mid {{ background:{CREAM}; }}
.bases .b-name {{ font-family:'Oswald',sans-serif; font-weight:600; font-size:11pt; color:{NAVY}; }}
.bases .b-q {{ font-family:'Oswald',sans-serif; font-weight:600; font-size:9pt; color:{GOLD_D}; letter-spacing:.06em; text-transform:uppercase; }}
.bases .b-job {{ background:{CREAM}; border-radius:0 5px 5px 0; font-family:'Lora',serif; font-style:italic; color:{SLATE}; font-size:9.5pt; }}
.b1 {{ background:{NAVY}; }} .b2 {{ background:{TEAL}; }} .b3 {{ background:{GREEN}; }} .b4 {{ background:{RUST}; }}
.firstrow td {{ box-shadow:0 0 0 2px {GOLD} inset; }}

.note {{ font-family:'Lora',serif; font-style:italic; color:{SLATE}; font-size:9pt; line-height:1.5; margin-top:4px; }}

/* two-col */
.cols {{ display:flex; gap:22px; }}
.col {{ flex:1; }}
.h3 {{ font-family:'Oswald',sans-serif; font-weight:700; text-transform:uppercase; letter-spacing:.1em;
  font-size:10pt; color:{NAVY}; margin-bottom:8px; padding-bottom:6px; border-bottom:2px solid {GOLD}; }}

.chips li {{ list-style:none; font-family:'Lora',serif; font-size:9.4pt; line-height:1.45; margin-bottom:9px; padding-left:18px; position:relative; }}
.chips li:before {{ content:'\\25C6'; color:{GOLD_D}; position:absolute; left:0; top:1px; font-size:7.5pt; }}

/* H framework cards */
.hgrid {{ display:flex; flex-direction:column; gap:8px; }}
.hrow {{ display:flex; align-items:stretch; border-radius:6px; overflow:hidden; box-shadow:0 1px 0 rgba(0,0,0,.06); }}
.hrow .letter {{ width:0.62in; color:#fff; font-family:'Anton',sans-serif; font-size:22pt; display:flex; align-items:center; justify-content:center; }}
.hrow .htxt {{ flex:1; background:{CREAM}; padding:9px 14px; display:flex; flex-direction:column; justify-content:center; }}
.hrow .hname {{ font-family:'Oswald',sans-serif; font-weight:700; text-transform:uppercase; letter-spacing:.08em; font-size:11pt; color:{NAVY}; }}
.hrow .hname span {{ color:{GOLD_D}; font-weight:500; font-style:normal; }}
.hrow .hdesc {{ font-family:'Lora',serif; font-size:9pt; color:{SLATE}; font-style:italic; margin-top:1px; }}
.hrow .hchange {{ width:1.25in; background:{NAVY}; color:{GOLD}; font-family:'Oswald',sans-serif; font-weight:600;
  text-transform:uppercase; letter-spacing:.08em; font-size:8pt; display:flex; align-items:center; justify-content:center; text-align:center; }}

/* format meta strip */
.meta {{ display:flex; gap:0; border-radius:6px; overflow:hidden; margin-top:6px; }}
.meta .m {{ flex:1; background:{NAVY}; color:#fff; padding:12px 8px; text-align:center; border-right:1px solid rgba(255,255,255,.12); }}
.meta .m:last-child {{ border-right:0; }}
.meta .big {{ font-family:'Anton',sans-serif; font-size:20pt; color:{GOLD}; }}
.meta .lab {{ font-family:'Oswald',sans-serif; font-weight:500; text-transform:uppercase; letter-spacing:.12em; font-size:7pt; color:#C9D2E0; margin-top:3px; }}

/* ============================================================ DAY pages */
.day-head {{ display:flex; align-items:flex-start; gap:16px; margin-bottom:13px; }}
.day-num {{ background:{NAVY}; color:#fff; border-radius:6px; width:0.95in; flex-shrink:0; text-align:center; padding:9px 0; }}
.day-num .d1 {{ font-family:'Oswald',sans-serif; font-weight:500; text-transform:uppercase; letter-spacing:.14em; font-size:7pt; color:{GOLD}; }}
.day-num .d2 {{ font-family:'Anton',sans-serif; font-size:27pt; line-height:.85; }}
.day-title h3 {{ font-family:'Anton',sans-serif; text-transform:uppercase; color:{NAVY}; font-size:19pt; line-height:.98; }}
.day-title .wk {{ font-family:'Oswald',sans-serif; font-weight:600; text-transform:uppercase; letter-spacing:.14em; font-size:7.5pt; color:{GOLD_D}; margin-top:5px; }}

.conv {{ background:{CREAM}; border-left:4px solid {GOLD}; padding:9px 14px; border-radius:0 5px 5px 0; margin-bottom:11px; }}
.conv .lab {{ font-family:'Oswald',sans-serif; font-weight:700; text-transform:uppercase; letter-spacing:.14em; font-size:7.5pt; color:{GOLD_D}; }}
.conv p {{ font-family:'Lora',serif; font-size:9.8pt; line-height:1.42; margin-top:2px; }}

.blocklab {{ font-family:'Oswald',sans-serif; font-weight:700; text-transform:uppercase; letter-spacing:.13em;
  font-size:8pt; color:{GREEN}; margin:9px 0 3px; }}
.day p.story {{ font-style:italic; color:#3c4350; font-size:9.4pt; line-height:1.46; }}
.day p.why {{ font-size:9.4pt; line-height:1.48; margin-bottom:5px; }}

.ron {{ background:{NAVY}; color:#F4ECD8; border-radius:6px; padding:11px 16px; margin:10px 0; }}
.ron .lab {{ font-family:'Oswald',sans-serif; font-weight:700; letter-spacing:.16em; text-transform:uppercase; font-size:7.5pt; color:{GOLD}; margin-bottom:3px; }}
.ron p {{ font-family:'Lora',serif; font-style:italic; font-size:9.6pt; line-height:1.42; }}

.qrow {{ display:flex; gap:9px; margin-top:9px; }}
.qbox {{ flex:1; background:#fff; border:1.5px solid #E7DEC9; border-top:3px solid {GOLD}; border-radius:5px; padding:8px 11px; }}
.qbox .lab {{ font-family:'Oswald',sans-serif; font-weight:700; text-transform:uppercase; letter-spacing:.07em; font-size:7pt; color:{NAVY}; margin-bottom:3px; }}
.qbox p {{ font-family:'Lora',serif; font-size:8.4pt; line-height:1.36; color:#3c4350; }}

.carry {{ margin-top:11px; background:{GOLD}; color:{NAVY}; border-radius:5px; padding:9px 15px;
  font-family:'Lora',serif; font-style:italic; font-weight:600; font-size:10pt; }}
.carry b {{ font-family:'Oswald',sans-serif; font-style:normal; font-weight:700; text-transform:uppercase;
  letter-spacing:.1em; font-size:7.5pt; margin-right:6px; }}

/* fears */
.fearbox {{ margin-bottom:11px; border-radius:6px; overflow:hidden; border:1px solid #ECE3D0; }}
.fearbox .f {{ background:{NAVY}; color:#fff; font-family:'Lora',serif; font-style:italic; font-size:10pt; padding:8px 14px; }}
.fearbox .f:before {{ content:'\\201C'; color:{GOLD}; font-size:14pt; }}
.fearbox .f:after {{ content:'\\201D'; color:{GOLD}; font-size:14pt; }}
.fearbox .a {{ background:{CREAM}; padding:8px 14px; font-size:9pt; line-height:1.44; }}
.fearbox .a .where {{ font-family:'Oswald',sans-serif; font-weight:700; text-transform:uppercase; letter-spacing:.05em;
  font-size:7.5pt; color:{GOLD_D}; }}

.tworoot {{ background:{NAVY}; color:#fff; border-radius:6px; padding:14px 18px; margin-bottom:16px; display:flex; gap:14px; align-items:center; }}
.tworoot .rt {{ flex:1; }}
.tworoot .lab {{ font-family:'Oswald',sans-serif; font-weight:700; letter-spacing:.14em; text-transform:uppercase; font-size:7.5pt; color:{GOLD}; }}
.tworoot p {{ font-family:'Lora',serif; font-size:9pt; line-height:1.4; margin-top:3px; color:#E4E9F1; }}
.tworoot .key {{ font-family:'Lora',serif; font-style:italic; font-size:9.5pt; color:#fff; }}

/* session / huddle */
.timeline {{ position:relative; margin-left:6px; }}
.tl {{ display:flex; gap:14px; margin-bottom:12px; }}
.tl .time {{ width:0.95in; flex-shrink:0; text-align:right; }}
.tl .time .mins {{ font-family:'Anton',sans-serif; font-size:15pt; color:{GOLD_D}; line-height:1; }}
.tl .time .u {{ font-family:'Oswald',sans-serif; text-transform:uppercase; letter-spacing:.1em; font-size:6.5pt; color:{SLATE}; }}
.tl .dot {{ width:14px; flex-shrink:0; position:relative; }}
.tl .dot:before {{ content:''; position:absolute; left:4px; top:3px; width:9px; height:9px; border-radius:50%; background:{GOLD}; box-shadow:0 0 0 3px {CREAM}; }}
.tl .dot:after {{ content:''; position:absolute; left:7.5px; top:12px; bottom:-14px; width:2px; background:#E2D8C2; }}
.tl:last-child .dot:after {{ display:none; }}
.tl .c {{ flex:1; padding-bottom:2px; }}
.tl .c .t {{ font-family:'Oswald',sans-serif; font-weight:700; text-transform:uppercase; letter-spacing:.05em; font-size:10pt; color:{NAVY}; }}
.tl .c p {{ font-size:8.8pt; line-height:1.4; margin-top:2px; }}
.tl .c .q {{ font-style:italic; color:{GREEN}; }}

.output {{ background:{GREEN}; color:#fff; border-radius:6px; padding:13px 18px; margin-top:6px; }}
.output .lab {{ font-family:'Oswald',sans-serif; font-weight:700; letter-spacing:.16em; text-transform:uppercase; font-size:7.5pt; color:#BFE3CE; }}
.output p {{ font-family:'Lora',serif; font-style:italic; font-size:11pt; line-height:1.4; margin-top:4px; }}

/* closing CTA page */
.closing {{ background:{NAVY}; color:{CREAM}; }}
.closing .inner {{ position:absolute; inset:0; padding:0.95in 0.85in; display:flex; flex-direction:column; }}
.closing h2 {{ font-family:'Anton',sans-serif; text-transform:uppercase; color:#fff; font-size:42pt; line-height:.95; }}
.closing h2 .gold {{ color:{GOLD}; }}
.closing .pk {{ font-family:'Lora',serif; font-style:italic; font-size:13pt; color:#D9CCAE; margin:18px 0 28px; max-width:5.6in; }}
.pkg {{ display:flex; flex-direction:column; gap:11px; margin-bottom:30px; }}
.pkg .it {{ display:flex; gap:14px; align-items:center; }}
.pkg .n {{ font-family:'Anton',sans-serif; color:{GOLD}; font-size:22pt; width:0.5in; }}
.pkg .tx .a {{ font-family:'Oswald',sans-serif; font-weight:600; text-transform:uppercase; letter-spacing:.06em; font-size:11pt; color:#fff; }}
.pkg .tx .b {{ font-family:'Lora',serif; font-style:italic; font-size:9.5pt; color:#C2CADA; }}
.closing .stamp {{ margin-top:auto; border-top:2px solid rgba(224,168,46,.4); padding-top:18px; display:flex; justify-content:space-between; align-items:flex-end; }}
.closing .stamp .l {{ font-family:'Lora',serif; font-style:italic; font-size:11pt; color:#D9CCAE; max-width:4.6in; line-height:1.4; }}
.closing .stamp .r {{ font-family:'Oswald',sans-serif; font-weight:600; letter-spacing:.2em; text-transform:uppercase; font-size:8pt; color:{GOLD}; text-align:right; }}
"""

def page(inner, cls=""):
    return f'<div class="page {cls}">{inner}</div>'

def topband(kick, title_html, tag):
    return f'''<div class="topband">
      <div class="kicker kick">{kick}</div>
      <h2>{title_html}</h2>
      <div class="tag">{tag}</div></div>'''

def foot(num):
    return f'<div class="brandfoot">Wisdom Changes Everything</div><div class="pagenum">First Base &middot; {num}</div>'

# ---------------- COVER ----------------
cover = f'''
<div class="bg-h">H</div>
<div class="inner">
  <div class="toprow">
    <div class="badge">Ron Blue Institute</div>
    <div class="badge">First Base &middot; The Why</div>
  </div>
  <div class="center">
    <div class="eyebrow">Financial Wisdom Pathway</div>
    <h1>Wisdom<br>Changes<br><span class="gold">Everything</span></h1>
    <div class="sub">30 Days of Financial Wisdom for Pastors &amp; Church Leaders</div>
    <div class="q">What if the one subject Jesus taught on most is the one your church has never truly discipled?</div>
  </div>
  <div class="foot">
    <div class="l">A leadership vision journey<br>Built on Ron Blue&rsquo;s 6 H&rsquo;s<br>Concept draft for review</div>
    <div class="r">Wisdom &rarr; Culture &rarr;<br>Campaign &rarr; Ministry</div>
  </div>
</div>'''
P1 = page(cover, "cover")

# ---------------- PAGE 2: OVERVIEW ----------------
bases_rows = ""
rows = [
    ("1ST &middot; WISDOM","b1","Wisdom Changes Everything","Why?","Convince &amp; energize the leaders", True),
    ("2ND &middot; CULTURE","b2","Financial Wisdom Culture","How?","Align &amp; ready the team", False),
    ("3RD &middot; CAMPAIGN","b3","This Changes Everything: 40 Days","What?","Mobilize the congregation", False),
    ("HOME &middot; MINISTRY","b4","Financial Wisdom Ministry","Lasting?","Make it permanent", False),
]
for tag,cl,name,q,job,first in rows:
    fr = "firstrow" if first else ""
    bases_rows += f'''<tr class="{fr}">
      <td class="b-tag {cl}">{tag}</td>
      <td class="b-mid"><div class="b-name">{name}</div></td>
      <td class="b-mid"><div class="b-q">{q}</div></td>
      <td class="b-job">{job}</td></tr>'''

overview_body = f'''
<div class="promise">
  <div class="lab">The One-Line Promise</div>
  <p>In 30 days, your leadership team moves from seeing money as a problem to manage to seeing financial discipleship as a mission to lead &mdash; with one vision, one language, and one conviction strong enough to change your church.</p>
</div>

<div class="h3">Where It Fits &middot; The Four Bases</div>
<table class="bases">{bases_rows}</table>
<div class="note">You cannot skip the Why. A team that isn&rsquo;t convinced will not build, align, or launch &mdash; everything downstream runs on the conviction this resource creates. <strong>Pastor Advisor</strong> stands off the path as a separate, personal resource.</div>

<div style="height:14px"></div>
<div class="cols">
  <div class="col">
    <div class="h3">Who It&rsquo;s For</div>
    <ul class="chips">
      <li>Senior pastors &amp; executive pastors</li>
      <li>Elders &amp; key ministry leaders</li>
      <li>A <strong>team journey</strong> &mdash; read daily, gather weekly</li>
      <li>Built for any role, married or single</li>
    </ul>
  </div>
  <div class="col">
    <div class="h3">What Leaders Walk Away With</div>
    <ul class="chips">
      <li>Conviction that <strong>God owns it all</strong></li>
      <li>Financial discipleship as the <strong>Great Commission</strong></li>
      <li>The shift <strong>from fundraising to faith-building</strong></li>
      <li>A shared vocabulary &mdash; the 6 H&rsquo;s</li>
    </ul>
  </div>
</div>

<div style="height:10px"></div>
<div class="meta">
  <div class="m"><div class="big">30</div><div class="lab">Days</div></div>
  <div class="m"><div class="big">6</div><div class="lab">Weeks / H&rsquo;s</div></div>
  <div class="m"><div class="big">5</div><div class="lab">Days Each</div></div>
  <div class="m"><div class="big">1</div><div class="lab">Team, Aligned</div></div>
</div>
'''
P2 = page(topband("First Base &middot; The Why at a Glance",
     'Wisdom <span class="gold">Changes</span> Everything',
     'The hook: what it is, where it fits, and what it does &mdash; in one minute.') +
     f'<div class="body">{overview_body}</div>' + foot("Overview"), "content")

# ---------------- PAGE 3: THE 6 H'S + WHY NOW ----------------
hdata = [
    ("H",NAVY,"Honor","God owns it all","Our Posture"),
    ("H",TEAL,"Heart","Money reveals what we trust","Our Discernment"),
    ("H",GREEN,"Habits","Wisdom becomes practice","Our Discipleship"),
    ("H",GOLD_D,"Health","Wisdom brings peace &amp; margin","Our Care"),
    ("H",RUST,"Hope","Eternal perspective on enough","Our Mission"),
    ("H",NAVY2,"Harvest","Generosity, legacy, Kingdom impact","Our Fruit"),
]
hrows = ""
for L,c,name,desc,change in hdata:
    hrows += f'''<div class="hrow">
      <div class="letter" style="background:{c}">{L}</div>
      <div class="htxt"><div class="hname">{name}</div><div class="hdesc">{desc}</div></div>
      <div class="hchange">{change}</div></div>'''

h_body = f'''
<div class="hgrid">{hrows}</div>
<div class="note" style="margin-top:10px">The journey climbs from <strong>surrender</strong> (Honor) to <strong>fruit</strong> (Harvest) &mdash; ending with a team commissioned to build. The same framework runs through Culture and the Campaign, so a team fluent in it here is already speaking the language the whole church will share.</div>

<div style="height:16px"></div>
<div class="tworoot">
  <div class="rt">
    <div class="lab">Why It Matters Now</div>
    <p>Households in your pews are under historic financial pressure &mdash; debt, anxiety, comparison, and silence. The world disciples them about money every single day. The church, in most cases, has simply ceded the ground.</p>
    <div class="key" style="margin-top:7px">This is the church&rsquo;s moment to claim a frontier it was uniquely made to claim.</div>
  </div>
</div>

<div class="h3">Each Day Contains</div>
<ul class="chips">
  <li>A <strong>conviction</strong> &mdash; the day&rsquo;s big idea in one line</li>
  <li>A <strong>story</strong> that names a leadership team&rsquo;s real experience</li>
  <li>A <strong>teaching in Ron Blue&rsquo;s voice</strong>, anchored to Scripture and the Great Commission</li>
  <li>Three discussion layers &mdash; <strong>personal reflection, team conversation, a wisdom question</strong></li>
</ul>
'''
P3 = page(topband("The Framework &amp; The Urgency",
     'Ron&rsquo;s <span class="gold">6 H&rsquo;s</span>',
     'The spine of the journey &mdash; and the shared language that runs through every resource downstream.') +
     f'<div class="body">{h_body}</div>' + foot("Framework"), "content")

# ---------------- DAY PAGE BUILDER ----------------
def day_page(num, title, week, conv, story_label, story, why_label, why_paras, ron, refl, team, wis, carry, pnum):
    why_html = "".join(f'<p class="why">{p}</p>' for p in why_paras)
    inner = f'''
    <div class="body" style="padding-top:0.5in">
      <div class="day-head">
        <div class="day-num"><div class="d1">Day</div><div class="d2">{num}</div></div>
        <div class="day-title"><h3>{title}</h3><div class="wk">{week}</div></div>
      </div>
      <div class="conv"><div class="lab">Today&rsquo;s Conviction</div><p>{conv}</p></div>
      <div class="blocklab">{story_label}</div>
      <p class="story">{story}</p>
      <div class="blocklab">{why_label}</div>
      <div class="day">{why_html}</div>
      <div class="ron"><div class="lab">Ron&rsquo;s Principle</div><p>{ron}</p></div>
      <div class="qrow">
        <div class="qbox"><div class="lab">Leadership Reflection</div><p>{refl}</p></div>
        <div class="qbox"><div class="lab">Team Conversation</div><p>{team}</p></div>
        <div class="qbox"><div class="lab">The Wisdom Question</div><p>{wis}</p></div>
      </div>
      <div class="carry"><b>Carry It Forward</b>{carry}</div>
    </div>'''
    return page(inner + foot(pnum), "content")

# A section divider strip atop the first day page
def day_divider():
    return ""

DAY1 = day_page("01","The Owner of Everything","Week 1 &middot; Honor: God Owns It All",
  "Everything the church will ever do with financial discipleship begins with one truth: God owns it all &mdash; and we, as leaders, are stewards of a mission, not owners of an institution.",
  "A Story",
  "A leadership team sits around a table on a Tuesday night, the budget projected on the wall. The numbers are tight. The conversation circles the familiar territory &mdash; what to cut, what to delay, how to make up the gap. And without anyone deciding it, the room has taken a posture: this is ours to fund, ours to protect, ours to carry. The mission has become an institution to keep alive.",
  "The Why",
  ["Ron Blue gave his life to four words: <em>God owns it all.</em> Not most of it. Not the spiritual portion. All of it. &ldquo;The earth is the Lord&rsquo;s, and everything in it&rdquo; (Psalm 24:1). For church leaders, this is not a doctrine to affirm and move past. It is the ground every other conviction in this journey stands on.",
   "If God owns it all, then your church is not yours to fund, fix, or carry &mdash; it is His to build. Your role shifts from anxious owner to faithful steward. Ownership asks, <em>How do we make this work?</em> Stewardship asks, <em>Lord, what have You entrusted to us?</em> One produces pressure. The other produces peace &mdash; and a far bigger vision.",
   "And that puts financial discipleship squarely inside the Great Commission. Jesus said <em>make disciples</em> &mdash; teaching them to obey everything He commanded. He commanded a great deal about money. A church that disciples people in marriage, parenting, and purpose but stays silent about money has left a frontier unclaimed."],
  "God owns it all. We are not owners; we are stewards. Stewardship is the use of God-given resources to accomplish God-given goals.",
  "Where am I &mdash; and where are we as a team &mdash; carrying the weight of ownership over a mission that actually belongs to God?",
  "When our church talks about money, does it sound like we believe God owns it all &mdash; or like an institution managing its needs?",
  "If we truly led as stewards of God&rsquo;s mission rather than owners of an institution, what is the first thing that would change?",
  "Honor doesn&rsquo;t begin with a budget. It begins with surrender &mdash; and surrender is where the vision gets bigger, not smaller.",
  "Day 1")

DAY2 = day_page("02","Stewards of a Mission, Not Owners of an Institution","Week 1 &middot; Honor: God Owns It All",
  "The shift from owning an institution to stewarding a mission changes not just how we feel, but how we lead, decide, and ask.",
  "A Story",
  "A founding pastor walks his campus on a quiet Saturday. He built this. But somewhere over the years the church he planted to reach a city became a thing he had to protect. Decisions started flowing from a single instinct &mdash; guard what we&rsquo;ve built. He doesn&rsquo;t notice until a younger leader asks why they haven&rsquo;t tried anything risky in five years &mdash; and he hears himself give an answer that sounds responsible and is actually just fear.",
  "The Why",
  ["There&rsquo;s a world of difference between an owner running an institution and a steward advancing a mission. The owner asks protective questions &mdash; <em>How do we sustain this? How do we avoid risk?</em> Notice what they orbit: survival. An institution&rsquo;s deepest instinct is self-preservation.",
   "The steward asks different questions entirely &mdash; <em>What has God entrusted to us, and for what purpose?</em> Ron defined stewardship as the use of God-given resources to accomplish God-given goals &mdash; a definition with direction built in. Stewardship is never merely about keeping. It&rsquo;s about deploying for a purpose beyond ourselves.",
   "This changes what money is <em>for.</em> If the church is an institution, money keeps it alive, and every money conversation carries the anxiety of survival. If the church is a mission, money is fuel for a calling &mdash; and teaching people to handle it wisely frees them and equips the mission. Survival is a small, exhausting story. Mission is a large, energizing one."],
  "Stewardship is the use of God-given resources to accomplish God-given goals. The steward&rsquo;s question is never &lsquo;How do I keep this?&rsquo; but &lsquo;How do I deploy this faithfully?&rsquo;",
  "Honestly &mdash; am I leading a mission or protecting an institution? Where can I feel the difference in my own decisions?",
  "Where have we made decisions this year out of self-preservation rather than mission? What would we have decided as stewards of a calling?",
  "If we believed our money was fuel for a mission, what is one thing we&rsquo;d start funding &mdash; or stop funding &mdash; this year?",
  "An institution asks how to survive. A mission asks what God wants done. Stewards lead missions.",
  "Day 2")

DAY3 = day_page("03","The Discipleship Frontier We&rsquo;ve Left Unclaimed","Week 1 &middot; Honor: God Owns It All",
  "Financial discipleship isn&rsquo;t a topic the church has handled poorly &mdash; it&rsquo;s a frontier the church has largely never entered. And that&rsquo;s an opportunity, not just an indictment.",
  "A Story",
  "A discipleship pastor maps her church&rsquo;s pathway on a whiteboard &mdash; new believers, baptism, groups, marriage, parenting, leadership. It&rsquo;s thorough. A volunteer studies the board and asks an innocent question: &ldquo;Where&rsquo;s money?&rdquo; The room goes quiet. There&rsquo;s a stewardship sermon every fall and a benevolence fund &mdash; but on a board mapping how this church forms a whole disciple, there is no path for the one subject Jesus addressed most. Not a bad path. No path.",
  "The Why",
  ["We assume the church has <em>tried</em> to disciple people about money and just hasn&rsquo;t done it well. The truth is closer to this: in most churches it was never really attempted as discipleship at all. There&rsquo;s been fundraising, the occasional stewardship series, crisis benevolence &mdash; but no deliberate, ongoing pathway the way we&rsquo;ve built for marriage or parenting.",
   "That&rsquo;s why &lsquo;frontier&rsquo; is the right word. A frontier isn&rsquo;t a place you failed; it&rsquo;s a place you haven&rsquo;t gone yet. Meanwhile, someone <em>is</em> discipling your people about money &mdash; advertisers, comparison, anxiety. The world is relentlessly forming your congregation about money, and the church has simply ceded the ground.",
   "Here&rsquo;s what makes it exciting rather than merely convicting: no one is better positioned to claim this than the church. Only the church can address the <em>heart</em> beneath the money &mdash; the trust, fear, worship, and eternal perspective that actually drive financial behavior."],
  "The world disciples your people about money every day. The only question is whether the church will join the conversation Jesus started &mdash; or leave His people to be formed by everyone else.",
  "If I mapped our real discipleship pathway, where would financial formation appear &mdash; a genuine path, or a once-a-year event?",
  "Who is currently discipling our people about money? What voices are forming their financial lives more than we are?",
  "If we treated financial discipleship as an unclaimed frontier rather than a sensitive topic, how would our posture change?",
  "We haven&rsquo;t failed at this frontier. We just haven&rsquo;t entered it. The ground is open.",
  "Day 3")

DAY4 = day_page("04","What Jesus Talked About Most","Week 1 &middot; Honor: God Owns It All",
  "Jesus made money a central subject of discipleship &mdash; and a church that follows Him cannot treat as marginal what He treated as central.",
  "A Story",
  "A seminary-trained pastor, twenty years in, decides one afternoon to actually count. He&rsquo;d always known Jesus &ldquo;talked about money a lot.&rdquo; But he sits with the Gospels and tallies it &mdash; and the number stuns him. Roughly one in ten verses touches money or possessions; sixteen of thirty-eight parables deal with resources. He&rsquo;s preached most of those parables &mdash; and somehow consistently made them about something else.",
  "The Why",
  ["It&rsquo;s one of the most quietly astonishing facts in Scripture: Jesus said more about money and possessions than about heaven and hell combined. More than prayer. More than faith. If frequency tells us anything about emphasis &mdash; and surely it does &mdash; money was central to how He formed disciples.",
   "Why? Not for its own sake. Jesus addressed money because it is the most reliable diagnostic of the human heart available. &ldquo;Where your treasure is, there your heart will be also.&rdquo; You can hide a lot about your spiritual condition, but your relationship with money quietly tells the truth.",
   "This puts a church in a striking position. If we follow a Lord who made money central to formation, we cannot in good conscience make it marginal. And notice: Jesus was never transactional. He used money to expose idolatry, call out false security, and reveal generosity as the mark of a transformed heart. He treated money as <em>discipleship</em> &mdash; exactly the thing we&rsquo;ve struggled to do."],
  "Jesus addressed money more than almost any subject &mdash; not because money mattered most to Him, but because it reveals the heart more honestly than anything else.",
  "Have I consistently made Jesus&rsquo; money teachings about <em>something else</em> &mdash; because money itself felt too uncomfortable to address head-on?",
  "If a newcomer judged our priorities by how often we teach on subjects, where would money rank &mdash; versus where it ranked for Jesus?",
  "What would it look like to let Jesus&rsquo; actual emphasis set our discipleship priorities, rather than our comfort?",
  "We follow a Lord who made money central. We are not free to make it marginal.",
  "Day 4")

DAY5 = day_page("05","From Fundraising to Faith-Building","Week 1 &middot; Honor: God Owns It All",
  "The deepest reframe of this entire journey: we are not raising money; we are building faith. And that single shift frees a leader to lead.",
  "A Story",
  "A pastor confesses he dreads one Sunday more than any other &mdash; the stewardship sermon. Everyone knows what it&rsquo;s really about: the budget is behind, and he&rsquo;s there to close the gap. He hates how it makes him feel, like a salesman in a robe. His mentor asks a question that rearranges everything: &ldquo;What if you never had to give that sermon again &mdash; and instead only ever talked about your people&rsquo;s freedom?&rdquo;",
  "The Why",
  ["Most pastors carry a low-grade dread about money in the church, and it traces to a single confusion: they&rsquo;ve fused two different things. <em>Fundraising</em> and <em>faith-building</em> live in the same drawer, so every time money comes up, the anxiety of asking comes with it.",
   "But they&rsquo;re opposites. Fundraising begins with the institution&rsquo;s need and asks people to meet it. Faith-building begins with the person&rsquo;s discipleship and trusts God to provide for the church as a byproduct. Ron spent his life on a sentence that dissolves the dread: <em>giving is a result, not a goal.</em> Aim at the heart, and generosity follows the way fruit follows a healthy tree.",
   "This frees the leader. You&rsquo;re no longer the institution&rsquo;s collector; you&rsquo;re the people&rsquo;s shepherd. And here&rsquo;s the paradox Ron watched play out repeatedly: churches that stop fundraising and start discipling almost always become <em>more</em> generous, not less &mdash; because a transformed heart gives freely where obligation gives reluctantly."],
  "Giving is a result, not a goal. Aim at the heart, and generosity follows. Disciple the person, and the church will be provided for.",
  "Have I fused fundraising and faith-building into the same dreaded conversation? What would change if I fully separated them?",
  "Which posture do our people actually hear &mdash; &lsquo;the church needs this from you&rsquo; or &lsquo;God wants this freedom for you&rsquo;?",
  "What is one place we currently &lsquo;fundraise&rsquo; that we could genuinely reframe &mdash; not just reword &mdash; as faith-building?",
  "Stop raising money. Start building faith. The generosity will come &mdash; and so will the freedom, starting with yours.",
  "Day 5")

# ---------------- FEARS PAGE ----------------
fears = [
    ("People will think we just want money.","This is faith-building, not fundraising &mdash; and the difference is the whole point.","Day 5 &middot; Honor"),
    ("I don&rsquo;t feel qualified to teach about money.","You&rsquo;re not the expert. The pastor casts vision; the framework carries the expertise.","Day 11 &middot; Habits"),
    ("This is just Financial Peace 2.0.","Not a budgeting program &mdash; whole-life discipleship: heart, habits, health, hope, harvest.","Day 4 &middot; Honor"),
    ("Our wealthy families will feel targeted.","The framework disciples them with dignity &mdash; legacy and calling, never their checkbook.","Weeks 5&ndash;6"),
    ("The struggling families will feel ashamed.","Grace-based and step-oriented; their pain is something the church exists to meet.","Day 17 &middot; Health"),
    ("Our people won&rsquo;t engage.","Wisdom speaks to every stage &mdash; struggling, stable, and surplus alike.","Day 19 &middot; Health"),
    ("This will sound like the prosperity gospel.","Anchored in the opposite &mdash; ownership, contentment, and &lsquo;how much is enough.&rsquo;","Days 1 &amp; 22"),
    ("What happens after 30 days &mdash; does it fade?","This is First Base. Day 30 commissions the team straight into Culture and the pathway.","Day 30"),
]
fear_html = ""
for f,a,w in fears:
    fear_html += f'''<div class="fearbox"><div class="f">{f}</div>
      <div class="a">{a} <span class="where">&nbsp;&rarr; {w}</span></div></div>'''

# split into two columns
half = 4
fcol1 = "".join(fear_html.split('<div class="fearbox">')[1:half+1])
fcol1 = '<div class="fearbox">' + '<div class="fearbox">'.join(fear_html.split('<div class="fearbox">')[1:half+1])
fcol2 = '<div class="fearbox">' + '<div class="fearbox">'.join(fear_html.split('<div class="fearbox">')[half+1:])

fears_body = f'''
<div class="tworoot">
  <div class="rt">
    <div class="lab">The Two Fears Underneath All the Others</div>
    <p><strong style="color:{GOLD}">Suspicion</strong> &mdash; &ldquo;People will think we just want their money.&rdquo; &nbsp;&bull;&nbsp; <strong style="color:{GOLD}">Shame</strong> &mdash; &ldquo;I&rsquo;m not qualified / our own house isn&rsquo;t in order.&rdquo;</p>
    <div class="key" style="margin-top:7px">The master key to both: <strong>lead with wisdom, not giving.</strong> &ldquo;We need to talk about money&rdquo; triggers suspicion. &ldquo;We want to grow in wisdom&rdquo; disarms it.</div>
  </div>
</div>
<div class="cols">
  <div class="col">{fcol1}</div>
  <div class="col">{fcol2}</div>
</div>
<div class="note" style="margin-top:4px">Nearly every fear, honestly faced, becomes the very reason to do this work. The objections aren&rsquo;t obstacles to the vision &mdash; they <em>are</em> the vision, seen from the underside.</div>
'''
PF = page(topband("Pre-Empt Every Hesitation in the Room",
     'Fears This <span class="gold">Journey</span> Answers',
     'Hand this to a hesitant elder before you pitch &mdash; and you&rsquo;ve answered the objection before it&rsquo;s voiced.') +
     f'<div class="body">{fears_body}</div>' + foot("Fears Answered"), "content")

# ---------------- HUDDLE / TEAM SESSION PAGE ----------------
tls = [
    ("5","min","Opening","Read Psalm 24:1 together. One sentence each: <span class='q'>where did this week touch a nerve about how we lead around money?</span> Surface, don&rsquo;t solve."),
    ("35","min","The Core Conversation","Owners or stewards? (Day 1&ndash;2). The unclaimed frontier (Day 3). Following Jesus&rsquo; emphasis (Day 4). And the reframe that frees us &mdash; fundraising vs. faith-building (Day 5). <span class='q'>Don&rsquo;t rush to agreement; the friction is where alignment happens.</span>"),
    ("10","min","The Wisdom Question","One question, agreed together &mdash; the output of the week. Name it specifically. Write it down. Not a list &mdash; one thing."),
    ("5","min","Close","Pray together, naming the one commitment. The facilitator carries it into Week 2."),
]
tl_html = ""
for m,u,t,p in tls:
    tl_html += f'''<div class="tl"><div class="time"><div class="mins">{m}</div><div class="u">{u}</div></div>
      <div class="dot"></div><div class="c"><div class="t">{t}</div><p>{p}</p></div></div>'''

huddle_body = f'''
<div class="note" style="margin-bottom:12px">The daily readings are done alone. <strong>This is where the journey becomes a team.</strong> After each leader has read the week&rsquo;s five days, the team gathers once &mdash; about 60 minutes &mdash; to process Honor together before moving into Heart. One ground rule, stated aloud: <em>this is about our posture as leaders, not anyone&rsquo;s personal finances.</em></div>

<div class="timeline">{tl_html}</div>

<div class="output">
  <div class="lab">What This Session Produces</div>
  <p>&ldquo;If we truly led as stewards of God&rsquo;s mission rather than owners of an institution &mdash; starting now &mdash; what is the ONE thing that would change first about how we lead?&rdquo;</p>
</div>
<div class="note" style="margin-top:10px">Multiply this across six weeks and a leadership team doesn&rsquo;t just read a book together &mdash; they arrive at Week 6 sharing one conviction, one language, and six concrete commitments. <strong>That&rsquo;s a team ready to build. That&rsquo;s what First Base is for.</strong></div>
'''
PH = page(topband("The Team Journey, Made Real",
     'Sample Team <span class="gold">Huddle</span> &middot; Week 1',
     'One worked example of the weekly gathering &mdash; the rhythm repeats for all six weeks.') +
     f'<div class="body">{huddle_body}</div>' + foot("Team Session"), "content")

# ---------------- CLOSING / CTA ----------------
closing = f'''
<div class="inner">
  <div class="kicker" style="color:{GOLD};letter-spacing:.28em">The Presentation Package</div>
  <h2>Everything You Need<br>To <span class="gold">Believe It</span></h2>
  <div class="pk">Four pieces that work together &mdash; the hook, the proof, the disarmer, and the proof it runs.</div>
  <div class="pkg">
    <div class="it"><div class="n">1</div><div class="tx"><div class="a">One-Page Overview</div><div class="b">The hook &mdash; what it is, where it fits, at a glance.</div></div></div>
    <div class="it"><div class="n">2</div><div class="tx"><div class="a">Honor Week &middot; Days 1&ndash;5</div><div class="b">The proof &mdash; the voice and the arc, fully written.</div></div></div>
    <div class="it"><div class="n">3</div><div class="tx"><div class="a">Fears This Journey Answers</div><div class="b">The disarmer &mdash; every hesitation, pre-empted.</div></div></div>
    <div class="it"><div class="n">4</div><div class="tx"><div class="a">Sample Team Huddle</div><div class="b">The proof that &lsquo;team-based&rsquo; is real, not asserted.</div></div></div>
  </div>
  <div class="stamp">
    <div class="l">Only Week 1 is written. Weeks 2&ndash;6 exist as titled outlines, ready to build once the concept is approved &mdash; the right place to stop before greenlight.</div>
    <div class="r">Wisdom Changes<br>Everything<br><span style="color:#8893A6">First Base &middot; The Why</span></div>
  </div>
</div>'''
PC = page(closing, "closing")

HTML = f"<!doctype html><html><head><meta charset='utf-8'><style>{CSS}</style></head><body>{P1}{P2}{P3}{DAY1}{DAY2}{DAY3}{DAY4}{DAY5}{PF}{PH}{PC}</body></html>"

pathlib.Path("/home/claude/wce.html").write_text(HTML)
weasyprint.HTML(string=HTML).write_pdf("/home/claude/Wisdom_Changes_Everything.pdf")
print("PDF built")
