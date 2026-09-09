# -*- coding: utf-8 -*-
import json
from staff_roles import ROLES, LEVEL_NAMES

DEVOS = [
 ["Foundation","Called and Kept","Forty days on identity before competence. Who you are when the role is taken away."],
 ["Competence","Faithful in Small Things","Fifty-six days on diligence, integrity and the unseen work."],
 ["Leadership","The Weight and the Yoke","Seventy days on carrying responsibility without being crushed by it."],
 ["Multiplication","What You Leave Behind","Eighty-four days on succession, legacy and releasing what you built."],
]

CUSTOM = [
 ["Denominational affiliation",["Baptist","Non-denominational","Methodist","Presbyterian","Pentecostal / Charismatic","Lutheran","Anglican / Episcopal","Reformed","Bible / Evangelical Free","Restoration Movement"],
  "Changes governance modules, ordination language, and which historical voices are cited."],
 ["Theological persuasion",["Reformed","Wesleyan-Arminian","Pentecostal-Charismatic","Broadly Evangelical","Confessional / Liturgical"],
  "Changes the devotional exegesis, the disputed-questions handling, and the theology electives."],
 ["Church size",["Under 100","100 to 250","250 to 500","500 to 1,000","1,000 to 2,500","Over 2,500"],
  "Changes staffing assumptions, delegation depth, and whether a role is one person or a team."],
 ["Stage",["Church plant","Growing","Plateaued","Replant / turnaround","Established","Multisite"],
  "Changes urgency, sequence, and which competencies come first."],
 ["Delivery",["Self-paced","Cohort / small group","Blended"],
  "Changes pacing, peer work, and how competency is verified."],
]

PROCESS = [
 ["Recruit","Find and assess","Role profile, competency screen, theological fit, reference discipline, and a written scorecard before anyone is interviewed."],
 ["Train","Build the competency","The four-level track for that role, with modules, reading, practice assignments and the companion devotional."],
 ["Develop","Deepen and coach","A coach, a cohort, quarterly review against the competency map, and stretch assignments inside the real job."],
 ["Multiply","Reproduce the role","Every level ends by requiring the person to train someone else. Nobody certifies at Expert without two people trained to completion."],
]

DELIVERY = [
 ["Self-paced","One person, their own clock",
  ["Video modules and written guides","Practice assignment after each module","Self-check quiz per module",
   "Portfolio submitted at the end of each level","Coach review at level completion only"],
  "Best for a solo staff member, a bivocational leader, or a church with one person in the role."],
 ["Cohort","Six to twelve peers, same pace",
  ["Weekly ninety-minute session","Peer case work on real situations","Assignments due between sessions",
   "Cohort leader trained and supplied","Group portfolio review"],
  "Best for a staff team, a denominational cohort, or a network training several churches at once."],
 ["Blended","Modules alone, practice together",
  ["Content consumed individually","Monthly cohort gathering for application","Coach assigned per person",
   "Peer accountability partner","Combined self and peer assessment"],
  "Best for larger churches and for Advanced and Expert levels, where practice matters more than content."],
]

ASSESS = [
 ["Knowledge check","Per module","A short check after each module. Not a gate, a rehearsal — spaced retrieval, retakeable."],
 ["Practice assignment","Per module","Something done in the actual job that week. Reviewed by a coach, not graded by a machine."],
 ["Competency portfolio","Per level","The artifacts named in the certification requirement — a plan, a document, a recorded conversation."],
 ["Peer and supervisor review","Per level","360 input from the people who see the work, against the published competency map."],
 ["Oral examination","Advanced and Expert","A live conversation with a certified assessor. Character and judgment cannot be tested on paper."],
 ["Multiplication proof","Expert only","Names of people trained to completion. No exceptions, and no substitutions."],
]

ORGANIC = [
 ["Apprenticeship","Watch, help, lead, hand off — the four-stage handoff that predates every curriculum."],
 ["Real work as the classroom","Every assignment happens inside the actual job that week, never in a simulation."],
 ["Table learning","A cohort eating together before it studies. Formation runs on relationship, not modules."],
 ["Story and testimony","Practitioners telling what went wrong, which is what people actually remember."],
 ["Coaching over instruction","Questions before answers. The coach's job is to make them think, not to inform them."],
 ["Formation before function","The devotional runs the whole way through. Competence without character is a liability."],
]

def esc(s):
    return s.replace("\\", "\\\\").replace("'", "\\'")

payload = {"roles": ROLES, "lv": LEVEL_NAMES, "devos": DEVOS, "custom": CUSTOM,
           "proc": PROCESS, "deliv": DELIVERY, "assess": ASSESS, "organic": ORGANIC}

TOTAL_MODULES = sum(len(l["m"]) for r in ROLES for l in r["lv"])

CSS = """
*{box-sizing:border-box;margin:0;padding:0}
:root{--blue:#1d4ed8;--blue-d:#1e3a8a;--blue-l:#3b82f6;--blue-p:#eff6ff;--blue-b:#dbeafe;
--ink:#0f172a;--body:#334155;--mute:#64748b;--faint:#94a3b8;
--line:#e2e8f0;--bg:#f8fafc;--white:#fff;--max:1180px;
--sh:0 1px 2px rgba(15,23,42,.04),0 4px 12px rgba(15,23,42,.05);
--sh-l:0 2px 4px rgba(15,23,42,.04),0 12px 32px rgba(15,23,42,.08)}
html{scroll-behavior:smooth}
body{font-family:'Inter',system-ui,-apple-system,sans-serif;background:var(--bg);color:var(--body);
line-height:1.65;font-size:17px;-webkit-font-smoothing:antialiased}
.wrap{max-width:var(--max);margin:0 auto;padding:0 24px}
h1,h2,h3,h4{color:var(--ink);line-height:1.15;letter-spacing:-.022em;font-weight:700}
section{padding:80px 0}
.eyebrow{font-size:11.5px;font-weight:700;letter-spacing:.14em;text-transform:uppercase;
color:var(--blue);margin-bottom:14px}
h2.sh{font-size:35px}
p.lede{font-size:18px;color:var(--mute);margin-top:12px;max-width:66ch}
header{position:sticky;top:0;z-index:60;background:rgba(255,255,255,.95);
backdrop-filter:saturate(180%) blur(12px);border-bottom:1px solid var(--line)}
.nav{display:flex;align-items:center;gap:26px;height:64px}
.brand{font-weight:800;font-size:16px;color:var(--ink);letter-spacing:-.02em;flex-shrink:0}
.brand span{color:var(--blue)}
.nav nav{display:flex;gap:22px;margin-left:auto;overflow-x:auto;scrollbar-width:none}
.nav nav::-webkit-scrollbar{display:none}
.nav a{color:var(--mute);text-decoration:none;font-size:14px;font-weight:500;white-space:nowrap;cursor:pointer}
.nav a:hover{color:var(--blue)}
.hero{background:var(--white);border-bottom:1px solid var(--line);padding:88px 0 72px}
.hero h1{font-size:56px;font-weight:800;letter-spacing:-.035em;max-width:17ch}
.hero h1 em{font-style:normal;color:var(--blue)}
.hero .l2{font-size:21px;color:var(--mute);margin-top:22px;max-width:64ch}
.stats{display:flex;flex-wrap:wrap;margin-top:36px;border-top:1px solid var(--line);border-bottom:1px solid var(--line)}
.stats>div{flex:1 1 150px;padding:20px 18px 20px 0}
.stats b{display:block;font-size:30px;color:var(--blue);font-weight:800;letter-spacing:-.03em}
.stats span{font-size:13.5px;color:var(--mute);display:block;margin-top:3px}
.arrow4{display:grid;grid-template-columns:repeat(4,1fr);gap:0;margin-top:32px;
border:1px solid var(--line);border-radius:14px;overflow:hidden;background:var(--white)}
.a4{padding:24px 22px;border-right:1px solid var(--line)}
.a4:last-child{border-right:0}
.a4 .n4{font-size:11px;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:var(--blue)}
.a4 h4{font-size:19px;margin-top:9px}
.a4 .s4{font-size:14px;color:var(--blue-l);font-weight:600;margin-top:3px}
.a4 p{font-size:14.5px;color:var(--mute);margin-top:10px;line-height:1.55}
.filt{display:flex;flex-wrap:wrap;gap:8px;margin-top:26px}
.fb{border:1px solid var(--line);background:var(--white);border-radius:8px;padding:8px 15px;
font-family:inherit;font-size:14px;color:var(--body);cursor:pointer;font-weight:500}
.fb:hover{border-color:var(--blue-l);color:var(--blue)}
.fb.on{background:var(--blue);border-color:var(--blue);color:#fff}
.roles{display:grid;grid-template-columns:repeat(4,1fr);gap:12px;margin-top:22px}
.rc{background:var(--white);border:1px solid var(--line);border-radius:12px;padding:20px 18px;
cursor:pointer;text-align:left;font-family:inherit;transition:all .18s}
.rc:hover{border-color:var(--blue-l);box-shadow:var(--sh-l);transform:translateY(-2px)}
.rc .rt{font-size:10.5px;font-weight:700;letter-spacing:.1em;text-transform:uppercase;color:var(--faint)}
.rc h4{font-size:17px;margin-top:8px;line-height:1.25}
.rc p{font-size:13.5px;color:var(--mute);margin-top:7px;line-height:1.5}
.rc .go{font-size:12.5px;font-weight:600;color:var(--blue);margin-top:12px}
.back{background:none;border:0;color:var(--blue);font-family:inherit;font-size:14px;font-weight:600;
cursor:pointer;padding:0;margin-bottom:18px}
.rhero{background:var(--white);border:1px solid var(--line);border-radius:16px;padding:32px;
box-shadow:var(--sh);margin-bottom:24px}
.rhero .rt2{font-size:11px;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:var(--blue)}
.rhero h2{font-size:33px;margin-top:10px}
.rhero .pp{font-size:19px;color:var(--mute);margin-top:10px;max-width:66ch}
.resp{display:flex;flex-wrap:wrap;gap:8px;margin-top:20px}
.resp span{font-size:14px;background:var(--bg);border:1px solid var(--line);padding:7px 13px;border-radius:7px}
.anchor{margin-top:22px;padding:18px 22px;background:var(--blue-p);border-left:3px solid var(--blue);
border-radius:0 10px 10px 0}
.anchor .al{font-size:11px;font-weight:700;letter-spacing:.12em;text-transform:uppercase;
color:var(--blue);margin-bottom:6px}
.anchor .ar2{font-size:20px;font-weight:700;color:var(--ink);letter-spacing:-.02em}
.anchor p{font-size:15.5px;color:var(--blue-d);margin-top:6px}
.lvtabs{display:grid;grid-template-columns:repeat(4,1fr);gap:10px;margin-bottom:20px}
.lt2{background:var(--white);border:1px solid var(--line);border-radius:11px;padding:16px 14px;
cursor:pointer;text-align:left;font-family:inherit;transition:all .16s}
.lt2:hover{border-color:var(--blue-l)}
.lt2.on{border-color:var(--blue);border-width:2px;padding:15px 13px;box-shadow:var(--sh)}
.lt2 .ln{font-size:10.5px;font-weight:700;letter-spacing:.1em;text-transform:uppercase;color:var(--faint)}
.lt2.on .ln{color:var(--blue)}
.lt2 h5{font-size:16px;color:var(--ink);font-weight:700;margin-top:6px}
.lt2 .wk{font-size:13px;color:var(--mute);margin-top:2px}
.lvbody{background:var(--white);border:1px solid var(--line);border-radius:16px;overflow:hidden;box-shadow:var(--sh)}
.lvh{padding:28px 32px;border-bottom:1px solid var(--line)}
.lvh h3{font-size:25px}
.lvh p{font-size:16px;color:var(--mute);margin-top:6px;max-width:70ch}
.mods{padding:8px 32px}
.md{display:flex;gap:16px;padding:16px 0;border-bottom:1px solid var(--line);align-items:baseline}
.md:last-child{border-bottom:0}
.md .mn2{font-size:12px;font-weight:700;color:var(--blue);min-width:26px;flex-shrink:0}
.md .mb{flex:1}
.md .mt2{font-size:17px;color:var(--ink);font-weight:600}
.md .ms{font-size:15px;color:var(--mute);margin-top:3px}
.lvf{padding:24px 32px;background:var(--bg);border-top:1px solid var(--line)}
.lvf .fl{font-size:11px;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:var(--blue);margin-bottom:6px}
.lvf .fv{font-size:16.5px;color:var(--ink)}
.lvf .fr{margin-top:16px;padding-top:16px;border-top:1px solid var(--line)}
.dev{margin-top:20px;background:var(--blue-d);border-radius:14px;padding:26px 30px;color:#fff}
.dev .dl{font-size:11px;font-weight:700;letter-spacing:.14em;text-transform:uppercase;color:#93c5fd;margin-bottom:8px}
.dev h4{color:#fff;font-size:23px}
.dev p{color:#bfdbfe;font-size:16px;margin-top:8px;max-width:64ch}
.cust{display:grid;grid-template-columns:repeat(2,1fr);gap:14px;margin-top:28px}
.cu{background:var(--white);border:1px solid var(--line);border-radius:13px;padding:22px 24px}
.cu h4{font-size:17px}
.cu .opts2{display:flex;flex-wrap:wrap;gap:6px;margin-top:12px}
.cu .opts2 button{border:1px solid var(--line);background:var(--white);border-radius:7px;padding:6px 12px;
font-family:inherit;font-size:13.5px;color:var(--body);cursor:pointer}
.cu .opts2 button:hover{border-color:var(--blue-l);color:var(--blue)}
.cu .opts2 button.on{background:var(--blue);border-color:var(--blue);color:#fff}
.cu .eff{font-size:14px;color:var(--mute);margin-top:12px;line-height:1.5;font-style:italic}
.prof{background:var(--blue-p);border:1px solid var(--blue-b);border-radius:13px;padding:22px 26px;margin-top:20px}
.prof .pl2{font-size:11px;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:var(--blue);margin-bottom:8px}
.prof .pv{font-size:17px;color:var(--blue-d)}
.three3{display:grid;grid-template-columns:repeat(3,1fr);gap:14px;margin-top:28px}
.d3{background:var(--white);border:1px solid var(--line);border-radius:13px;padding:24px}
.d3 h4{font-size:19px}
.d3 .sub3{font-size:14px;color:var(--blue);font-weight:600;margin-top:3px}
.d3 ul{list-style:none;margin-top:14px}
.d3 li{font-size:14.5px;color:var(--body);padding:5px 0 5px 17px;position:relative}
.d3 li::before{content:"";position:absolute;left:0;top:14px;width:6px;height:6px;border-radius:99px;background:var(--blue-b)}
.d3 .best{font-size:14px;color:var(--mute);margin-top:14px;padding-top:12px;border-top:1px solid var(--line);font-style:italic}
.trow{display:flex;gap:16px;padding:15px 0;border-bottom:1px solid var(--line);align-items:baseline}
.trow .tk{font-size:16.5px;color:var(--ink);font-weight:600;min-width:220px;flex-shrink:0}
.trow .tw{font-size:13px;color:var(--blue);font-weight:600;min-width:130px;flex-shrink:0}
.trow .tv{flex:1;font-size:16px;color:var(--mute)}
.org{display:grid;grid-template-columns:repeat(2,1fr);gap:12px;margin-top:26px}
.og{background:var(--white);border:1px solid var(--line);border-radius:12px;padding:20px 22px}
.og h4{font-size:17px}
.og p{font-size:14.5px;color:var(--mute);margin-top:6px;line-height:1.55}
.cta{background:var(--blue-d);color:#fff;text-align:center;padding:74px 0}
.cta h2{color:#fff;font-size:38px;letter-spacing:-.03em}
.cta p{color:#bfdbfe;font-size:18px;margin-top:14px;max-width:58ch;margin-left:auto;margin-right:auto}
footer{background:var(--ink);color:var(--faint);padding:30px 0;font-size:14px}
@media(max-width:1000px){.roles{grid-template-columns:repeat(2,1fr)}
.arrow4,.lvtabs,.three3{grid-template-columns:repeat(2,1fr)}
.a4:nth-child(2){border-right:0}.a4:nth-child(-n+2){border-bottom:1px solid var(--line)}
.hero h1{font-size:40px}.cust,.org{grid-template-columns:1fr}}
@media(max-width:640px){
section{padding:52px 0}.hero{padding:52px 0 44px}.hero h1{font-size:32px}.hero .l2{font-size:18px}
h2.sh{font-size:26px}.roles,.arrow4,.lvtabs,.three3{grid-template-columns:1fr}
.a4{border-right:0;border-bottom:1px solid var(--line)}.a4:last-child{border-bottom:0}
.rhero,.mods,.lvh,.lvf{padding-left:20px;padding-right:20px}.rhero{padding:22px 20px}
.trow{flex-direction:column;gap:4px}.trow .tk,.trow .tw{min-width:0}
.cta h2{font-size:27px}}
@media(prefers-reduced-motion:reduce){*{transition:none!important}}
"""

HTML = """<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Church Staff Intelligence — Staff Formation for Every Role</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<style>__CSS__</style></head><body>

<header><div class="wrap nav">
  <div class="brand">Church Staff <span>Intelligence</span></div>
  <nav>
    <a data-j="roles">The 20 Roles</a><a data-j="levels">Four Levels</a><a data-j="customize">Customize</a>
    <a data-j="delivery">Delivery</a><a data-j="certify">Certification</a><a data-j="process">Recruit to Multiply</a>
  </nav>
</div></header>

<div class="hero"><div class="wrap">
  <div class="eyebrow">Staff Intelligence to Staff Formation</div>
  <h1>Most churches hire for competence and then <em>develop nobody</em>.</h1>
  <p class="l2">Twenty roles. Four levels each. Every module anchored to a biblical figure who actually did the job, with a companion devotional running the whole way through — because competence without character is a liability, not an asset.</p>
  <div class="stats">
    <div><b>20</b><span>core staff roles</span></div>
    <div><b>80</b><span>development tracks</span></div>
    <div><b>__MODS__</b><span>training modules</span></div>
    <div><b>36</b><span>weeks, entry to expert</span></div>
    <div><b>4</b><span>certification levels</span></div>
  </div>
</div></div>

<section id="process"><div class="wrap">
  <div class="eyebrow">One System</div>
  <h2 class="sh">Recruit. Train. Develop. Multiply.</h2>
  <p class="lede">Most churches do the first one and hope for the rest. This is the same process for every role, at any size, in any stage.</p>
  <div class="arrow4" id="proc"></div>
</div></section>

<section id="roles" style="background:var(--white);border-top:1px solid var(--line);border-bottom:1px solid var(--line)">
  <div class="wrap" id="rolesection">
  <div class="eyebrow">The Library</div>
  <h2 class="sh">Twenty roles, each with a full development track.</h2>
  <p class="lede">Select any role to open its responsibilities, biblical anchor, four levels and certification requirements.</p>
  <div class="filt" id="filt"></div>
  <div class="roles" id="roles"></div>
</div>
<div class="wrap" id="roledetail" style="display:none"></div>
</section>

<section id="levels"><div class="wrap">
  <div class="eyebrow">The Ladder</div>
  <h2 class="sh">Four levels, and nobody skips one.</h2>
  <p class="lede">Every role runs the same ladder, so a church can talk about development in one language across the whole staff.</p>
  <div id="lvgrid"></div>
  <div class="eyebrow" style="margin-top:52px">Companion Devotionals</div>
  <h3 style="font-size:24px">The biblical backbone runs the whole way through.</h3>
  <p class="lede">One devotional series per level, taken daily alongside the modules. Formation and competence at the same time, never one then the other.</p>
  <div id="devos"></div>
</div></section>

<section id="customize" style="background:var(--white);border-top:1px solid var(--line)">
  <div class="wrap">
  <div class="eyebrow">Customization</div>
  <h2 class="sh">The same ladder, tuned to your church.</h2>
  <p class="lede">A Baptist church plant of eighty and a Presbyterian multisite of four thousand need the same competencies and completely different emphases. Set the profile and the track adjusts.</p>
  <div class="cust" id="cust"></div>
  <div class="prof" id="prof"></div>
</div></section>

<section id="delivery"><div class="wrap">
  <div class="eyebrow">Delivery</div>
  <h2 class="sh">Self-paced, cohort, or both.</h2>
  <p class="lede">The content is identical. What changes is the pace, the peer work and how competency gets verified.</p>
  <div class="three3" id="deliv"></div>
  <div class="eyebrow" style="margin-top:52px">Organic Learning</div>
  <h3 style="font-size:24px">The half a curriculum cannot deliver.</h3>
  <p class="lede">Every track carries an organizational spine and an organic one. The modules are the spine. These are the reason anyone actually changes.</p>
  <div class="org" id="org"></div>
</div></section>

<section id="certify" style="background:var(--white);border-top:1px solid var(--line)">
  <div class="wrap">
  <div class="eyebrow">Certification</div>
  <h2 class="sh">Six ways competency is verified.</h2>
  <p class="lede">A certificate that only proves someone watched videos is worth nothing. Character and judgment cannot be tested on paper, so they are examined in conversation and demonstrated in the actual job.</p>
  <div id="assess"></div>
  <div class="prof" style="margin-top:30px">
    <div class="pl2">The rule that protects the credential</div>
    <div class="pv">Nobody certifies at Expert without naming two people they trained to completion. No exceptions and no substitutions &mdash; the level is called Multiplication, and a credential that does not require it is a participation award.</div>
  </div>
</div></section>

<div class="cta"><div class="wrap">
  <h2>One stop for recruiting, training, developing and multiplying every role.</h2>
  <p>Any church, any size, any stage. Built on the same intelligence-to-formation architecture as the rest of the LifeTogether platform.</p>
</div></div>

<footer><div class="wrap">Church Staff Intelligence &middot; Staff Formation &middot; 20 roles &middot; 80 tracks &middot; __MODS__ modules</div></footer>

<script>
var D = __DATA__;
var st = {cat:"All", role:null, lv:0, prof:{}};

function esc2(s){ return String(s); }

function renderProc(){
  var h = "", i;
  for (i=0;i<D.proc.length;i++){
    h += '<div class="a4"><div class="n4">Step ' + (i+1) + '</div><h4>' + D.proc[i][0] + '</h4>';
    h += '<div class="s4">' + D.proc[i][1] + '</div><p>' + D.proc[i][2] + '</p></div>';
  }
  document.getElementById("proc").innerHTML = h;
}

function cats(){
  var out = ["All"], i;
  for (i=0;i<D.roles.length;i++){
    if (out.indexOf(D.roles[i].cat) === -1){ out.push(D.roles[i].cat); }
  }
  return out;
}

function renderRoles(){
  var cs = cats(), h = "", i;
  for (i=0;i<cs.length;i++){
    h += '<button class="fb' + (st.cat===cs[i]?" on":"") + '" data-f="' + cs[i] + '">' + cs[i] + '</button>';
  }
  document.getElementById("filt").innerHTML = h;
  h = "";
  for (i=0;i<D.roles.length;i++){
    var r = D.roles[i];
    if (st.cat !== "All" && r.cat !== st.cat){ continue; }
    h += '<button class="rc" data-r="' + i + '"><div class="rt">' + r.cat + '</div>';
    h += '<h4>' + r.n + '</h4><p>' + r.p + '</p>';
    h += '<div class="go">4 levels &middot; open track &rsaquo;</div></button>';
  }
  document.getElementById("roles").innerHTML = h;
  var fb = document.querySelectorAll(".fb");
  for (i=0;i<fb.length;i++){
    fb[i].onclick = function(){ st.cat = this.getAttribute("data-f"); renderRoles(); };
  }
  var rc = document.querySelectorAll(".rc");
  for (i=0;i<rc.length;i++){
    rc[i].onclick = function(){
      st.role = parseInt(this.getAttribute("data-r"),10); st.lv = 0; renderDetail();
      document.getElementById("roles").scrollIntoView({block:"start"});
    };
  }
}

function profLine(){
  var keys = [], i;
  for (i=0;i<D.custom.length;i++){
    var v = st.prof[i];
    if (v){ keys.push(v); }
  }
  return keys.length ? keys.join("  &middot;  ") : "No profile set — showing the standard track for every role.";
}

function renderDetail(){
  var box = document.getElementById("roledetail");
  var list = document.getElementById("rolesection");
  if (st.role === null){ box.style.display = "none"; list.style.display = "block"; return; }
  list.style.display = "none"; box.style.display = "block";
  var r = D.roles[st.role], i;
  var h = '<button class="back" id="bk">&larr; All twenty roles</button>';
  h += '<div class="rhero"><div class="rt2">' + r.cat + '</div><h2>' + r.n + '</h2>';
  h += '<p class="pp">' + r.p + '</p><div class="resp">';
  for (i=0;i<r.r.length;i++){ h += '<span>' + r.r[i] + '</span>'; }
  h += '</div><div class="anchor"><div class="al">Biblical anchor</div>';
  h += '<div class="ar2">' + r.a + '</div><p>' + r.fig + '</p></div></div>';
  h += '<div class="lvtabs">';
  for (i=0;i<4;i++){
    h += '<button class="lt2' + (st.lv===i?" on":"") + '" data-l="' + i + '">';
    h += '<div class="ln">' + D.lv[i][1] + '</div><h5>' + D.lv[i][0] + '</h5>';
    h += '<div class="wk">' + D.lv[i][2] + ' &middot; ' + r.lv[i].m.length + ' modules</div></button>';
  }
  h += '</div>';
  var L = r.lv[st.lv];
  h += '<div class="lvbody"><div class="lvh"><h3>' + D.lv[st.lv][0] + ' &mdash; ' + D.lv[st.lv][1] + '</h3>';
  h += '<p>' + D.lv[st.lv][3] + '</p></div><div class="mods">';
  for (i=0;i<L.m.length;i++){
    h += '<div class="md"><span class="mn2">' + (i<9?"0":"") + (i+1) + '</span><span class="mb">';
    h += '<span class="mt2">' + L.m[i][0] + '</span><span class="ms">' + L.m[i][1] + '</span></span></div>';
  }
  h += '</div><div class="lvf"><div class="fl">Outcome</div><div class="fv">' + L.o + '</div>';
  h += '<div class="fr"><div class="fl">Certification requires</div><div class="fv">' + L.c + '</div></div></div></div>';
  var dv = D.devos[st.lv];
  h += '<div class="dev"><div class="dl">Companion devotional &middot; ' + dv[0] + ' level</div>';
  h += '<h4>' + dv[1] + '</h4><p>' + dv[2] + '</p></div>';
  h += '<div class="prof" style="margin-top:18px"><div class="pl2">Tuned for</div><div class="pv">' + profLine() + '</div></div>';
  box.innerHTML = h;
  document.getElementById("bk").onclick = function(){ st.role = null; renderDetail(); renderRoles();
    document.getElementById("roles").scrollIntoView({block:"start"}); };
  var lt = document.querySelectorAll(".lt2");
  for (i=0;i<lt.length;i++){
    lt[i].onclick = function(){ st.lv = parseInt(this.getAttribute("data-l"),10); renderDetail(); };
  }
}

function renderLevels(){
  var h = '<div class="arrow4">', i;
  for (i=0;i<D.lv.length;i++){
    h += '<div class="a4"><div class="n4">Level ' + (i+1) + '</div><h4>' + D.lv[i][0] + '</h4>';
    h += '<div class="s4">' + D.lv[i][1] + ' &middot; ' + D.lv[i][2] + '</div><p>' + D.lv[i][3] + '</p></div>';
  }
  document.getElementById("lvgrid").innerHTML = h + '</div>';
  h = "";
  for (i=0;i<D.devos.length;i++){
    h += '<div class="trow"><span class="tk">' + D.devos[i][1] + '</span>';
    h += '<span class="tw">' + D.devos[i][0] + '</span>';
    h += '<span class="tv">' + D.devos[i][2] + '</span></div>';
  }
  document.getElementById("devos").innerHTML = h;
}

function renderCustom(){
  var h = "", i, j;
  for (i=0;i<D.custom.length;i++){
    h += '<div class="cu"><h4>' + D.custom[i][0] + '</h4><div class="opts2">';
    for (j=0;j<D.custom[i][1].length;j++){
      var on = st.prof[i] === D.custom[i][1][j];
      h += '<button data-c="' + i + '" data-v="' + j + '"' + (on?' class="on"':'') + '>' + D.custom[i][1][j] + '</button>';
    }
    h += '</div><div class="eff">' + D.custom[i][2] + '</div></div>';
  }
  document.getElementById("cust").innerHTML = h;
  var bs = document.querySelectorAll(".opts2 button");
  for (i=0;i<bs.length;i++){
    bs[i].onclick = function(){
      var c = parseInt(this.getAttribute("data-c"),10), v = parseInt(this.getAttribute("data-v"),10);
      var val = D.custom[c][1][v];
      if (st.prof[c] === val){ delete st.prof[c]; } else { st.prof[c] = val; }
      renderCustom(); renderProf(); if (st.role !== null){ renderDetail(); }
    };
  }
  renderProf();
}
function renderProf(){
  document.getElementById("prof").innerHTML =
    '<div class="pl2">Your church profile</div><div class="pv">' + profLine() + '</div>';
}

function renderDeliv(){
  var h = "", i, j;
  for (i=0;i<D.deliv.length;i++){
    h += '<div class="d3"><h4>' + D.deliv[i][0] + '</h4><div class="sub3">' + D.deliv[i][1] + '</div><ul>';
    for (j=0;j<D.deliv[i][2].length;j++){ h += '<li>' + D.deliv[i][2][j] + '</li>'; }
    h += '</ul><div class="best">' + D.deliv[i][3] + '</div></div>';
  }
  document.getElementById("deliv").innerHTML = h;
  h = "";
  for (i=0;i<D.organic.length;i++){
    h += '<div class="og"><h4>' + D.organic[i][0] + '</h4><p>' + D.organic[i][1] + '</p></div>';
  }
  document.getElementById("org").innerHTML = h;
}

function renderAssess(){
  var h = "", i;
  for (i=0;i<D.assess.length;i++){
    h += '<div class="trow"><span class="tk">' + D.assess[i][0] + '</span>';
    h += '<span class="tw">' + D.assess[i][1] + '</span>';
    h += '<span class="tv">' + D.assess[i][2] + '</span></div>';
  }
  document.getElementById("assess").innerHTML = h;
}

renderProc(); renderRoles(); renderDetail(); renderLevels(); renderCustom(); renderDeliv(); renderAssess();
var jl = document.querySelectorAll("[data-j]");
for (var z=0; z<jl.length; z++){
  jl[z].onclick = function(){
    var t = this.getAttribute("data-j");
    if (t === "roles" && st.role !== null){ st.role = null; renderDetail(); renderRoles(); }
    document.getElementById(t).scrollIntoView({block:"start"});
  };
}
</script></body></html>
"""

out = HTML.replace("__CSS__", CSS)
out = out.replace("__DATA__", json.dumps(payload, separators=(",", ":")))
out = out.replace("__MODS__", str(TOTAL_MODULES))

open("/mnt/user-data/outputs/church-staff-intelligence.html", "w", encoding="utf-8").write(out)
print("roles:", len(ROLES), "| modules:", TOTAL_MODULES, "| KB:", round(len(out)/1024, 1))
