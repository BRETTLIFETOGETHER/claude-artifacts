# -*- coding: utf-8 -*-
import json
from meeting_lib import CATS
import meeting_meta as M

payload = {
 "cats": [{"n": c[0], "s": c[1], "w": c[2],
           "ss": [{"t": s[0], "sub": s[1], "oq": s[2], "sc": s[3], "qs": s[4],
                   "turn": s[5], "act": s[6], "note": s[7]} for s in c[3]]} for c in CATS],
 "thesis": M.THESIS, "why": M.WHY, "struct": M.STRUCTURE, "structnote": M.STRUCTURE_NOTE,
 "lq": M.LEADER_Q, "lb": M.LEADER_BANDS, "survey": M.STAFF_SURVEY,
 "cal": M.CAL52, "calrules": M.CAL_RULES, "retreat": M.RETREAT,
 "toolbox": M.TOOLBOX, "journeys": M.JOURNEYS,
}
NSESS = sum(len(c["ss"]) for c in payload["cats"])

CSS = """*{box-sizing:border-box;margin:0;padding:0}
:root{--blue:#1d4ed8;--blue-d:#1e3a8a;--blue-l:#3b82f6;--blue-p:#eff6ff;--blue-b:#dbeafe;
--ink:#0f172a;--body:#334155;--mute:#64748b;--faint:#94a3b8;
--line:#e2e8f0;--bg:#f8fafc;--white:#fff;--max:1160px;
--sh:0 1px 2px rgba(15,23,42,.04),0 4px 12px rgba(15,23,42,.05);
--sh-l:0 2px 4px rgba(15,23,42,.04),0 12px 32px rgba(15,23,42,.08)}
html{scroll-behavior:smooth}
body{font-family:'Inter',system-ui,-apple-system,sans-serif;background:var(--bg);color:var(--body);
line-height:1.65;font-size:17px;-webkit-font-smoothing:antialiased}
.wrap{max-width:var(--max);margin:0 auto;padding:0 24px}
h1,h2,h3,h4{color:var(--ink);line-height:1.15;letter-spacing:-.022em;font-weight:700}
section{padding:76px 0}
.eyebrow{font-size:11.5px;font-weight:700;letter-spacing:.14em;text-transform:uppercase;color:var(--blue);margin-bottom:14px}
h2.sh{font-size:34px}
p.lede{font-size:18px;color:var(--mute);margin-top:12px;max-width:66ch}
header{position:sticky;top:0;z-index:60;background:rgba(255,255,255,.95);
backdrop-filter:saturate(180%) blur(12px);border-bottom:1px solid var(--line)}
.nav{display:flex;align-items:center;gap:24px;height:62px}
.brand{font-weight:800;font-size:16px;color:var(--ink);letter-spacing:-.02em;flex-shrink:0}
.brand span{color:var(--blue)}
.nav nav{display:flex;gap:20px;margin-left:auto;overflow-x:auto;scrollbar-width:none}
.nav nav::-webkit-scrollbar{display:none}
.nav a{color:var(--mute);text-decoration:none;font-size:14px;font-weight:500;white-space:nowrap;cursor:pointer}
.nav a:hover{color:var(--blue)}
.hero{background:var(--white);border-bottom:1px solid var(--line);padding:84px 0 68px}
.hero h1{font-size:54px;font-weight:800;letter-spacing:-.035em;max-width:17ch}
.hero h1 em{font-style:normal;color:var(--blue)}
.hero .l2{font-size:20px;color:var(--mute);margin-top:22px;max-width:64ch}
.stats{display:flex;flex-wrap:wrap;margin-top:32px;border-top:1px solid var(--line);border-bottom:1px solid var(--line)}
.stats>div{flex:1 1 140px;padding:19px 18px 19px 0}
.stats b{display:block;font-size:28px;color:var(--blue);font-weight:800;letter-spacing:-.03em}
.stats span{font-size:13.5px;color:var(--mute);display:block;margin-top:3px}
.wrow{display:flex;gap:16px;padding:15px 0;border-bottom:1px solid var(--line);align-items:baseline}
.wrow .wk2{font-size:16.5px;color:var(--ink);font-weight:600;min-width:280px;flex-shrink:0}
.wrow .wv{flex:1;font-size:16px;color:var(--mute)}
.s3{display:grid;grid-template-columns:repeat(3,1fr);gap:14px;margin-top:22px}
.s3c{border:1px solid var(--line);border-radius:12px;padding:22px 20px;background:var(--white)}
.s3c:first-child{border-color:var(--blue);border-width:2px;padding:21px 19px;background:var(--blue-p)}
.s3c .t3{font-size:11px;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:var(--blue)}
.s3c h4{font-size:20px;margin-top:6px}
.s3c .l3{font-size:13.5px;color:var(--blue-l);font-weight:600;margin-top:2px}
.s3c p{font-size:15.5px;color:var(--mute);margin-top:9px}
.cgrid{display:grid;grid-template-columns:repeat(2,1fr);gap:12px;margin-top:24px}
.cc{background:var(--white);border:1px solid var(--line);border-radius:12px;padding:22px 20px;
cursor:pointer;text-align:left;font-family:inherit;transition:all .18s}
.cc:hover{border-color:var(--blue-l);box-shadow:var(--sh-l);transform:translateY(-2px)}
.cc .cn{font-size:11px;font-weight:700;letter-spacing:.1em;text-transform:uppercase;color:var(--faint)}
.cc h4{font-size:20px;margin-top:6px}
.cc .cs2{font-size:14.5px;color:var(--blue);font-weight:600;margin-top:3px}
.cc p{font-size:15px;color:var(--mute);margin-top:9px;line-height:1.55}
.back{background:none;border:0;color:var(--blue);font-family:inherit;font-size:14px;font-weight:600;cursor:pointer;padding:0;margin-bottom:16px}
.slist{margin-top:16px}
.sr{display:flex;gap:14px;padding:15px 2px;border-bottom:1px solid var(--line);cursor:pointer;
align-items:baseline;background:none;border-left:0;border-right:0;border-top:0;width:100%;text-align:left;font-family:inherit;color:inherit}
.sr:hover .st{color:var(--blue)}
.sr .sn{font-size:12px;font-weight:700;color:var(--blue);min-width:26px;flex-shrink:0}
.sr .sb2{flex:1}
.sr .st{font-size:18px;color:var(--ink);font-weight:600;display:block}
.sr .ss{font-size:15px;color:var(--mute);margin-top:3px;display:block}
.sr .add{font-size:12px;font-weight:700;color:var(--blue);background:var(--blue-p);border:1px solid var(--blue-b);
padding:5px 10px;border-radius:6px;flex-shrink:0}
.sr .add.in{background:var(--blue);color:#fff;border-color:var(--blue)}
.guide{background:var(--white);border:1px solid var(--line);border-radius:15px;overflow:hidden;box-shadow:var(--sh);margin-top:16px}
.gh{padding:28px 32px;border-bottom:1px solid var(--line)}
.gh .gc{font-size:11px;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:var(--blue)}
.gh h3{font-size:28px;margin-top:8px}
.gh .gs{font-size:18px;color:var(--mute);margin-top:5px;font-style:italic}
.gsec{padding:22px 32px;border-bottom:1px solid var(--line)}
.gsec:last-child{border-bottom:0}
.gsec .gl{font-size:10.5px;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:var(--blue);margin-bottom:9px}
.gsec .gq{font-size:20px;color:var(--ink);font-weight:600;letter-spacing:-.02em;line-height:1.35}
.gsec ol{margin-left:18px;color:var(--body)}
.gsec li{font-size:17px;margin-bottom:8px}
.gsec .gt{font-size:18px;color:var(--blue-d);font-weight:600;font-style:italic;line-height:1.5}
.gsec p{font-size:17px;color:var(--body)}
.gnote{padding:22px 32px;background:#fffbeb;border-top:1px solid #fde68a}
.gnote .gl{color:#b45309}
.gnote p{font-size:16px;color:#78350f}
.assess{background:var(--white);border:1px solid var(--line);border-radius:16px;box-shadow:var(--sh-l);overflow:hidden;margin-top:24px}
.ahead{padding:24px 30px;border-bottom:1px solid var(--line);display:flex;justify-content:space-between;align-items:center;gap:16px;flex-wrap:wrap}
.ahead h3{font-size:21px}
.prog{display:flex;align-items:center;gap:12px}
.ptrk{width:120px;height:6px;background:var(--line);border-radius:99px;overflow:hidden}
.pfil{height:100%;background:var(--blue);width:0;border-radius:99px;transition:width .3s}
.pct{font-size:13px;font-weight:700;color:var(--blue);min-width:52px;text-align:right}
.qs{padding:8px 30px 4px}
.qrow{padding:15px 0;border-bottom:1px solid var(--line)}
.qrow:last-child{border-bottom:0}
.qt{font-size:16.5px;color:var(--ink);font-weight:500;margin-bottom:10px}
.opts{display:flex;gap:7px;flex-wrap:wrap}
.opt{border:1px solid var(--line);background:var(--white);border-radius:8px;padding:8px 14px;
font-family:inherit;font-size:14px;color:var(--body);cursor:pointer;font-weight:500}
.opt:hover{border-color:var(--blue-l);color:var(--blue)}
.opt.on{background:var(--blue);border-color:var(--blue);color:#fff}
.afoot{padding:20px 30px;background:var(--bg);border-top:1px solid var(--line);display:flex;
justify-content:space-between;align-items:center;gap:14px;flex-wrap:wrap}
.afoot .note{font-size:14px;color:var(--mute)}
.btn{background:var(--blue);color:#fff;border:0;border-radius:9px;padding:12px 22px;
font-family:inherit;font-size:15px;font-weight:600;cursor:pointer}
.btn:hover{background:var(--blue-d)}
.btn:disabled{background:var(--line);color:var(--faint);cursor:not-allowed}
.btn.ghost{background:var(--white);color:var(--blue);border:1px solid var(--blue)}
.res{margin-top:18px;background:var(--white);border:2px solid var(--blue);border-radius:16px;overflow:hidden}
.rh{padding:28px 30px;background:var(--blue);color:#fff}
.rh .rl{font-size:11.5px;font-weight:700;letter-spacing:.14em;text-transform:uppercase;opacity:.85}
.rh .sc{font-size:42px;font-weight:800;letter-spacing:-.03em;margin-top:5px}
.rh h3{color:#fff;font-size:25px;margin-top:3px}
.rh p{font-size:17px;margin-top:9px;opacity:.92;max-width:62ch}
.rb{padding:24px 30px}
.bandrow{display:flex;gap:14px;padding:12px 0;border-bottom:1px solid var(--line);align-items:baseline}
.bandrow:last-child{border-bottom:0}
.bandrow.hit{background:var(--blue-p);margin:0 -10px;padding:12px 10px}
.bandrow .bn{font-size:14.5px;font-weight:700;color:var(--blue);min-width:70px}
.bandrow .bt{font-size:16.5px;font-weight:600;color:var(--ink);min-width:210px}
.bandrow .bd{flex:1;font-size:15.5px;color:var(--mute)}
.svq{padding:16px 0;border-bottom:1px solid var(--line)}
.svq:last-child{border-bottom:0}
.svq .sq{font-size:16.5px;color:var(--ink);font-weight:600;margin-bottom:9px}
.svq textarea{width:100%;min-height:60px;background:var(--bg);border:1px solid var(--line);border-radius:8px;
padding:10px 12px;font-family:inherit;font-size:15px;color:var(--ink);resize:vertical}
.svq textarea:focus,.svq input:focus{outline:none;border-color:var(--blue)}
.cal{display:grid;grid-template-columns:repeat(4,1fr);gap:12px;margin-top:22px}
.mo{border:1px solid var(--line);border-radius:12px;padding:18px 16px;background:var(--white)}
.mo .mh{display:flex;justify-content:space-between;align-items:baseline;gap:8px}
.mo h4{font-size:18px}
.mo .tag{font-size:10px;font-weight:700;letter-spacing:.1em;text-transform:uppercase;padding:3px 7px;border-radius:5px}
.mo .tag.t1{background:var(--blue);color:#fff}
.mo .tag.t2{background:var(--bg);color:var(--mute);border:1px solid var(--line)}
.mo .mt{font-size:13.5px;color:var(--blue);font-weight:600;margin-top:3px}
.mo ul{list-style:none;margin-top:11px}
.mo li{font-size:14px;color:var(--body);padding:5px 0 5px 15px;position:relative;line-height:1.4}
.mo li::before{content:"";position:absolute;left:0;top:12px;width:5px;height:5px;border-radius:99px;background:var(--blue-b)}
.plan{background:var(--white);border:2px solid var(--blue);border-radius:14px;padding:24px 28px;margin-top:22px}
.plan h3{font-size:22px}
.plan .pc2{font-size:15px;color:var(--mute);margin-top:5px}
.plan .picked{display:flex;flex-wrap:wrap;gap:7px;margin-top:14px}
.plan .picked span{font-size:14px;background:var(--blue-p);color:var(--blue-d);border:1px solid var(--blue-b);
padding:7px 12px;border-radius:7px}
.plan .empty{font-size:15.5px;color:var(--faint);margin-top:12px;font-style:italic}
.rtr{display:flex;gap:14px;padding:13px 0;border-bottom:1px solid var(--line);align-items:baseline}
.rtr .rt2{font-size:14px;font-weight:700;color:var(--blue);min-width:52px;flex-shrink:0}
.rtr .rn{font-size:17px;color:var(--ink);font-weight:600;min-width:200px;flex-shrink:0}
.rtr .rd{font-size:12.5px;color:var(--faint);min-width:56px;flex-shrink:0}
.rtr .rv{flex:1;font-size:15.5px;color:var(--mute)}
.jr{border:1px solid var(--line);border-radius:12px;padding:20px 22px;margin-top:12px;background:var(--white)}
.jr .jh{display:flex;justify-content:space-between;gap:12px;align-items:baseline;flex-wrap:wrap}
.jr h4{font-size:20px}
.jr .jc{font-size:12.5px;font-weight:700;color:var(--blue)}
.jr p{font-size:15.5px;color:var(--mute);margin-top:7px}
.jr .jl{display:flex;flex-wrap:wrap;gap:6px;margin-top:12px}
.jr .jl span{font-size:13.5px;background:var(--bg);border:1px solid var(--line);padding:6px 11px;border-radius:6px}
.note2{background:#fffbeb;border:1px solid #fde68a;border-left:3px solid #f59e0b;border-radius:0 10px 10px 0;
padding:16px 20px;margin-top:18px;font-size:15.5px;color:#78350f}
.big{background:var(--white);border-left:3px solid var(--blue);padding:22px 26px;margin-top:24px;
font-size:21px;color:var(--ink);font-weight:600;letter-spacing:-.02em;border-radius:0 12px 12px 0}
.cta{background:var(--blue-d);color:#fff;text-align:center;padding:70px 0}
.cta h2{color:#fff;font-size:34px;letter-spacing:-.03em}
.cta p{color:#bfdbfe;font-size:18px;margin-top:14px;max-width:58ch;margin-left:auto;margin-right:auto}
footer{background:var(--ink);color:var(--faint);padding:28px 0;font-size:14px}
@media(max-width:1000px){.cal{grid-template-columns:repeat(2,1fr)}.cgrid{grid-template-columns:1fr}
.s3{grid-template-columns:1fr}.hero h1{font-size:38px}}
@media(max-width:640px){section{padding:50px 0}.hero{padding:50px 0 42px}.hero h1{font-size:30px}
.hero .l2{font-size:18px}h2.sh{font-size:25px}.cal{grid-template-columns:1fr}
.gh,.gsec,.gnote,.qs,.ahead,.afoot,.rb,.rh{padding-left:20px;padding-right:20px}
.wrow,.rtr,.bandrow{flex-direction:column;gap:4px}.wrow .wk2,.rtr .rn,.bandrow .bt{min-width:0}
.sr{flex-wrap:wrap}.cta h2{font-size:25px}}
@media(prefers-reduced-motion:reduce){*{transition:none!important}}"""

BODY = """
<header><div class="wrap nav"><div class="brand">Staff Meeting <span>Builder</span></div>
<nav><a data-j="why">Why</a><a data-j="find">Find a Session</a><a data-j="check">Meeting Check</a>
<a data-j="survey">Staff Survey</a><a data-j="calendar">52 Weeks</a><a data-j="journeys">Journeys</a>
<a data-j="retreat">Retreats</a><a data-j="tools">Toolbox</a></nav></div></header>

<div class="hero"><div class="wrap">
<div class="eyebrow">Church Staff Meeting Finder &amp; Builder</div>
<h1>Your staff meeting is the <em>best small group</em> in your church. Or it is a status report.</h1>
<p class="l2" id="thesis"></p>
<div class="stats"><div><b>10</b><span>categories</span></div><div><b>100</b><span>sessions</span></div>
<div><b>52</b><span>week calendar</span></div><div><b>6</b><span>journeys</span></div>
<div><b>4</b><span>quarterly retreats</span></div></div></div></div>

<section id="why"><div class="wrap"><div class="eyebrow">The Case</div>
<h2 class="sh">Five reasons this is the most important hour of your week.</h2>
<div id="why2" style="margin-top:22px"></div>
<div class="eyebrow" style="margin-top:44px">The Shape</div>
<h2 class="sh">Sixty minutes, in this order.</h2>
<div class="s3" id="struct"></div>
<div class="big" id="structnote"></div></div></section>

<section id="find" style="background:var(--white);border-top:1px solid var(--line);border-bottom:1px solid var(--line)">
<div class="wrap"><div id="findhead"><div class="eyebrow">The Library</div>
<h2 class="sh">Ten categories. One hundred sessions.</h2>
<p class="lede">Every session is a twenty-minute conversation with an opening question, a passage, three questions, the turn, an action and leader notes. Anyone on staff can run one with no preparation.</p></div>
<div class="cgrid" id="cgrid"></div><div id="detail"></div>
<div class="plan" id="plan"></div></div></section>

<section id="check"><div class="wrap"><div class="eyebrow">For the Leader</div>
<h2 class="sh">Is your staff meeting worth their time?</h2>
<p class="lede">Ten questions for whoever runs the meeting. Answer honestly rather than aspirationally.</p>
<div id="assessbox"></div><div id="resbox"></div></div></section>

<section id="survey" style="background:var(--white);border-top:1px solid var(--line)"><div class="wrap">
<div class="eyebrow">For the Staff</div><h2 class="sh">Ask them what they need.</h2>
<p class="lede" id="svwhy"></p>
<div class="note2" id="svrules"></div>
<div class="assess" style="margin-top:22px"><div class="ahead"><h3>Annual staff survey</h3></div>
<div class="qs" id="svqs"></div>
<div class="afoot"><div class="note">Anonymous. Results build next year's calendar.</div>
<button class="btn ghost" id="svclear">Clear</button></div></div></div></section>

<section id="calendar"><div class="wrap"><div class="eyebrow">The Year</div>
<h2 class="sh">Twelve timely months. Forty timeless weeks.</h2>
<p class="lede">The twelve anchored to the church calendar are fixed. The rest rotate by what the staff survey asked for.</p>
<div class="cal" id="cal"></div>
<div class="eyebrow" style="margin-top:44px">Rules</div>
<h3 style="font-size:22px">Six things that keep a calendar alive past March.</h3>
<div id="calrules" style="margin-top:14px"></div></div></section>

<section id="journeys" style="background:var(--white);border-top:1px solid var(--line)"><div class="wrap">
<div class="eyebrow">Journeys</div><h2 class="sh">Six twelve-session arcs for a particular season.</h2>
<p class="lede">Pre-sequenced for a specific situation. Order matters more than content in every one of these.</p>
<div id="jrn"></div></div></section>

<section id="retreat"><div class="wrap"><div class="eyebrow">Quarterly</div>
<h2 class="sh">Four one-days beat one three-day.</h2>
<p class="lede" id="rtwhy"></p>
<div id="rt" style="margin-top:22px"></div>
<div class="note2" id="rtrules"></div></div></section>

<section id="tools" style="background:var(--white);border-top:1px solid var(--line)"><div class="wrap">
<div class="eyebrow">Toolbox</div><h2 class="sh">Ten templates.</h2>
<div id="tb" style="margin-top:20px"></div></div></section>

<div class="cta"><div class="wrap"><h2>Design the hour that designs everything else.</h2>
<p>Fifty meetings a year with the people who set the culture. It is the highest-leverage room in the building.</p></div></div>
<footer><div class="wrap">Church Staff Meeting Finder &amp; Builder &middot; 10 categories &middot; 100 sessions &middot; 52-week calendar</div></footer>
"""

JS = """
var D=__DATA__;var st={cat:null,sess:null,ans:{},shown:false,picked:[],sv:{}};
function el(i){return document.getElementById(i);}
function esc(s){return String(s).replace(/"/g,"&quot;");}

el("thesis").innerHTML=D.thesis;
el("structnote").innerHTML=D.structnote;
el("svwhy").innerHTML=D.survey.why;
el("rtwhy").innerHTML=D.retreat.why;

function rWhy(){var h="",i;for(i=0;i<D.why.length;i++){
h+='<div class="wrow"><span class="wk2">'+D.why[i][0]+'</span><span class="wv">'+D.why[i][1]+'</span></div>';}
el("why2").innerHTML=h;
h="";for(i=0;i<D.struct.length;i++){h+='<div class="s3c"><div class="t3">'+D.struct[i][1]+'</div>';
h+='<h4>'+D.struct[i][0]+'</h4><p>'+D.struct[i][2]+'</p></div>';}el("struct").innerHTML=h;}

function rCats(){
if(st.cat!==null){el("cgrid").innerHTML="";return;}
el("findhead").style.display="block";
var h="",i;for(i=0;i<D.cats.length;i++){var c=D.cats[i];
h+='<button class="cc" data-c="'+i+'"><div class="cn">'+c.ss.length+' sessions</div>';
h+='<h4>'+c.n+'</h4><div class="cs2">'+c.s+'</div><p>'+c.w+'</p></button>';}
el("cgrid").innerHTML=h;
var b=document.querySelectorAll(".cc");for(i=0;i<b.length;i++){b[i].onclick=function(){
st.cat=parseInt(this.getAttribute("data-c"),10);st.sess=null;rAll();};}}

function rDetail(){
var box=el("detail");
if(st.cat===null){box.innerHTML="";return;}
el("findhead").style.display="none";
var c=D.cats[st.cat],i,h='<button class="back" id="bk">&larr; All ten categories</button>';
if(st.sess===null){
 h+='<div class="eyebrow">'+c.s+'</div><h2 class="sh">'+c.n+'</h2><p class="lede">'+c.w+'</p><div class="slist">';
 for(i=0;i<c.ss.length;i++){var s=c.ss[i];
  var inp=st.picked.indexOf(c.n+" :: "+s.t)!==-1;
  h+='<button class="sr" data-s="'+i+'"><span class="sn">'+(i<9?"0":"")+(i+1)+'</span><span class="sb2">';
  h+='<span class="st">'+s.t+'</span><span class="ss">'+s.sub+'</span></span>';
  h+='<span class="add'+(inp?" in":"")+'" data-add="'+i+'">'+(inp?"In the plan":"Add")+'</span></button>';}
 h+='</div>';
}else{
 var s=c.ss[st.sess];
 h+='<div class="guide"><div class="gh"><div class="gc">'+c.n+'</div><h3>'+s.t+'</h3>';
 h+='<div class="gs">'+s.sub+'</div></div>';
 h+='<div class="gsec"><div class="gl">Open with this &mdash; before any content</div><div class="gq">'+s.oq+'</div></div>';
 h+='<div class="gsec"><div class="gl">Scripture</div><p>'+s.sc+'</p></div>';
 h+='<div class="gsec"><div class="gl">Three questions</div><ol>';
 for(i=0;i<s.qs.length;i++){h+='<li>'+s.qs[i]+'</li>';}
 h+='</ol></div>';
 h+='<div class="gsec"><div class="gl">The turn &mdash; say this when the conversation flattens</div><div class="gt">'+s.turn+'</div></div>';
 h+='<div class="gsec"><div class="gl">This week</div><p>'+s.act+'</p></div>';
 h+='<div class="gnote"><div class="gl">Leader notes</div><p>'+s.note+'</p></div></div>';
 var inp2=st.picked.indexOf(c.n+" :: "+s.t)!==-1;
 h+='<p style="margin-top:16px"><button class="btn'+(inp2?" ghost":"")+'" id="addone">'+(inp2?"Remove from plan":"Add to the year")+'</button></p>';
}
box.innerHTML=h;
el("bk").onclick=function(){if(st.sess!==null){st.sess=null;}else{st.cat=null;}rAll();};
var sr=document.querySelectorAll(".sr");
for(i=0;i<sr.length;i++){sr[i].onclick=function(ev){
 var t=ev.target;
 if(t.getAttribute("data-add")!==null){
  var ix=parseInt(t.getAttribute("data-add"),10);toggle(st.cat,ix);rAll();return;}
 st.sess=parseInt(this.getAttribute("data-s"),10);rAll();};}
var a1=el("addone");
if(a1){a1.onclick=function(){toggle(st.cat,st.sess);rAll();};}}

function toggle(ci,si){var key=D.cats[ci].n+" :: "+D.cats[ci].ss[si].t;
var at=st.picked.indexOf(key);if(at===-1){st.picked.push(key);}else{st.picked.splice(at,1);}}

function rPlan(){var h='<h3>Your year</h3>';
h+='<div class="pc2">'+st.picked.length+' of 52 weeks planned. Add sessions from any category and leave four weeks empty for the ones that get cancelled.</div>';
if(st.picked.length){h+='<div class="picked">';
 for(var i=0;i<st.picked.length;i++){h+='<span>'+st.picked[i].split(" :: ")[1]+'</span>';}
 h+='</div><p style="margin-top:16px"><button class="btn ghost" id="clr">Clear the plan</button></p>';
}else{h+='<div class="empty">Nothing selected yet. Open a category and press Add on any session.</div>';}
el("plan").innerHTML=h;
var c=el("clr");if(c){c.onclick=function(){st.picked=[];rAll();};}}

function nA(){var n=0,i;for(i=0;i<D.lq.length;i++){if(st.ans[i]!==undefined)n++;}return n;}
function sc(){var s=0,i;for(i=0;i<D.lq.length;i++){if(st.ans[i]!==undefined)s+=(4-st.ans[i]);}return s;}
function rAssess(){var i,j,n=nA(),t=D.lq.length,p=Math.round(n/t*100);
var h='<div class="assess"><div class="ahead"><h3>Meeting health check</h3><div class="prog">';
h+='<div class="ptrk"><div class="pfil" style="width:'+p+'%"></div></div><div class="pct">'+n+' of '+t+'</div></div></div><div class="qs">';
for(i=0;i<D.lq.length;i++){h+='<div class="qrow"><div class="qt">'+(i+1)+'. '+D.lq[i][0]+'</div><div class="opts">';
for(j=0;j<D.lq[i][1].length;j++){h+='<button class="opt'+(st.ans[i]===j?" on":"")+'" data-q="'+i+'" data-o="'+j+'">'+D.lq[i][1][j]+'</button>';}
h+='</div></div>';}
h+='</div><div class="afoot"><div class="note">Answer all ten for an accurate band.</div>';
h+='<button class="btn" id="see"'+(n<t?" disabled":"")+'>See the result</button></div></div>';
el("assessbox").innerHTML=h;
var o=document.querySelectorAll("#assessbox .opt");for(i=0;i<o.length;i++){o[i].onclick=function(){
var q=parseInt(this.getAttribute("data-q"),10),v=parseInt(this.getAttribute("data-o"),10);
if(st.ans[q]===v){delete st.ans[q];}else{st.ans[q]=v;}rAssess();if(st.shown)rRes();};}
var s=el("see");if(s){s.onclick=function(){st.shown=true;rRes();};}}
function rRes(){var box=el("resbox");if(!st.shown){box.innerHTML="";return;}
var v=sc(),i,hit=0;
for(i=0;i<D.lb.length;i++){var r=D.lb[i][0].split(" to ");if(v>=parseInt(r[0],10)&&v<=parseInt(r[1],10))hit=i;}
var h='<div class="res"><div class="rh"><div class="rl">Your score</div><div class="sc">'+v+' / 40</div>';
h+='<h3>'+D.lb[hit][1]+'</h3><p>'+D.lb[hit][2]+'</p></div><div class="rb">';
for(i=0;i<D.lb.length;i++){h+='<div class="bandrow'+(i===hit?" hit":"")+'"><span class="bn">'+D.lb[i][0]+'</span>';
h+='<span class="bt">'+D.lb[i][1]+'</span><span class="bd">'+D.lb[i][2]+'</span></div>';}
box.innerHTML=h+'</div></div>';}

function rSurvey(){var h="",i,j;
var r="<strong>How to run it.</strong> ";
for(i=0;i<D.survey.rules.length;i++){r+=(i?" &middot; ":"")+D.survey.rules[i];}
el("svrules").innerHTML=r;
for(i=0;i<D.survey.qs.length;i++){var q=D.survey.qs[i];
h+='<div class="svq"><div class="sq">'+(i+1)+'. '+q[0]+'</div>';
if(q[1]==="open"){h+='<textarea placeholder="Their answer"></textarea>';}
else{h+='<div class="opts">';
 for(j=0;j<q[2].length;j++){var on=(q[1]==="multi")?((st.sv[i]||[]).indexOf(j)!==-1):(st.sv[i]===j);
  h+='<button class="opt'+(on?" on":"")+'" data-sq="'+i+'" data-so="'+j+'" data-m="'+(q[1]==="multi"?1:0)+'">'+q[2][j]+'</button>';}
 h+='</div>';}
h+='</div>';}
el("svqs").innerHTML=h;
var b=document.querySelectorAll("[data-sq]");for(i=0;i<b.length;i++){b[i].onclick=function(){
var q=parseInt(this.getAttribute("data-sq"),10),o=parseInt(this.getAttribute("data-so"),10);
if(this.getAttribute("data-m")==="1"){var a=st.sv[q]||[];var at=a.indexOf(o);
 if(at===-1){a.push(o);}else{a.splice(at,1);}st.sv[q]=a;}
else{st.sv[q]=(st.sv[q]===o)?undefined:o;}rSurvey();};}
var c=el("svclear");if(c){c.onclick=function(){st.sv={};rSurvey();};}}

function rCal(){var h="",i,j;for(i=0;i<D.cal.length;i++){var m=D.cal[i];
h+='<div class="mo"><div class="mh"><h4>'+m[0]+'</h4><span class="tag '+(m[1]==="Timely"?"t1":"t2")+'">'+m[1]+'</span></div>';
h+='<div class="mt">'+m[2]+'</div><ul>';
for(j=0;j<m[3].length;j++){h+='<li>'+m[3][j]+'</li>';}
h+='</ul></div>';}el("cal").innerHTML=h;
h="";for(i=0;i<D.calrules.length;i++){
h+='<div class="wrow"><span class="wk2">'+D.calrules[i][0]+'</span><span class="wv">'+D.calrules[i][1]+'</span></div>';}
el("calrules").innerHTML=h;}

function rJourneys(){var h="",i,j;for(i=0;i<D.journeys.length;i++){var J=D.journeys[i];
h+='<div class="jr"><div class="jh"><h4>'+J[0]+'</h4><span class="jc">'+J[1]+'</span></div>';
h+='<p>'+J[2]+'</p><div class="jl">';
for(j=0;j<J[3].length;j++){h+='<span>'+(j+1)+'. '+J[3][j]+'</span>';}
h+='</div></div>';}el("jrn").innerHTML=h;}

function rRetreat(){var h="",i;for(i=0;i<D.retreat.shape.length;i++){var R=D.retreat.shape[i];
h+='<div class="rtr"><span class="rt2">'+R[0]+'</span><span class="rn">'+R[1]+'</span>';
h+='<span class="rd">'+R[2]+'</span><span class="rv">'+R[3]+'</span></div>';}
el("rt").innerHTML=h;
var r="<strong>Six rules.</strong> ";
for(i=0;i<D.retreat.rules.length;i++){r+=(i?" &middot; ":"")+D.retreat.rules[i];}
el("rtrules").innerHTML=r;}

function rTools(){var h="",i;for(i=0;i<D.toolbox.length;i++){
h+='<div class="wrow"><span class="wk2">'+D.toolbox[i][0]+'</span><span class="wv">'+D.toolbox[i][1]+'</span></div>';}
el("tb").innerHTML=h;}

function rAll(){rCats();rDetail();rPlan();}
rWhy();rAll();rAssess();rRes();rSurvey();rCal();rJourneys();rRetreat();rTools();
var jl=document.querySelectorAll("[data-j]");for(var z=0;z<jl.length;z++){jl[z].onclick=function(){
var t=this.getAttribute("data-j");
if(t==="find"){st.cat=null;st.sess=null;rAll();}
el(t).scrollIntoView({block:"start"});};}
"""

SHELL = """<!DOCTYPE html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Church Staff Meeting Finder &amp; Builder</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<style>__CSS__</style></head><body>__BODY__<script>__JS__</script></body></html>"""

out = SHELL.replace("__CSS__", CSS).replace("__BODY__", BODY)
out = out.replace("__JS__", JS.replace("__DATA__", json.dumps(payload, separators=(",", ":"))))
open("/mnt/user-data/outputs/staff-meeting-builder.html", "w", encoding="utf-8").write(out)
print("sessions:", NSESS, "| KB:", round(len(out)/1024, 1))
