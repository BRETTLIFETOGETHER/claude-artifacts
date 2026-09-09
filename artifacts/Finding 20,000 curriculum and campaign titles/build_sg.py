# -*- coding: utf-8 -*-
import json
import sg_lib as L

payload = {"thesis":L.THESIS,"sixwhy":L.SIX_WHY,"aud":L.AUDIENCES,"pack":L.PACK,
 "wm":L.WORDMATH,"aff":L.AFFINITY,"cl":L.CLUSTERS,"pipe":L.PIPELINE,
 "pipenote":L.PIPELINE_NOTE,"sevena":L.SEVEN_A,"week":L.WEEK_ANSWER}
NS = sum(len(c["st"]) for c in L.CLUSTERS)
NSESS = sum(len(s["ss"]) for c in L.CLUSTERS for s in c["st"])

CSS = """*{box-sizing:border-box;margin:0;padding:0}
:root{--blue:#1d4ed8;--blue-d:#1e3a8a;--blue-l:#3b82f6;--blue-p:#eff6ff;--blue-b:#dbeafe;
--ink:#0f172a;--body:#334155;--mute:#64748b;--faint:#94a3b8;
--line:#e2e8f0;--bg:#f8fafc;--white:#fff;--max:1160px;
--sh:0 1px 2px rgba(15,23,42,.04),0 4px 12px rgba(15,23,42,.05);
--sh-l:0 2px 4px rgba(15,23,42,.04),0 12px 32px rgba(15,23,42,.08)}
html{scroll-behavior:smooth}
body{font-family:'Inter',system-ui,sans-serif;background:var(--bg);color:var(--body);
line-height:1.62;font-size:16.5px;-webkit-font-smoothing:antialiased}
.wrap{max-width:var(--max);margin:0 auto;padding:0 24px}
h1,h2,h3,h4{color:var(--ink);line-height:1.15;letter-spacing:-.022em;font-weight:700}
section{padding:72px 0}
.eyebrow{font-size:11.5px;font-weight:700;letter-spacing:.14em;text-transform:uppercase;color:var(--blue);margin-bottom:13px}
h2.sh{font-size:33px}
p.lede{font-size:18px;color:var(--mute);margin-top:11px;max-width:68ch}
header{position:sticky;top:0;z-index:60;background:rgba(255,255,255,.96);
backdrop-filter:saturate(180%) blur(12px);border-bottom:1px solid var(--line)}
.nav{display:flex;align-items:center;gap:20px;height:62px}
.brand{font-weight:800;font-size:15.5px;color:var(--ink);flex-shrink:0}
.brand span{color:var(--blue)}
.nav nav{display:flex;gap:18px;margin-left:auto;overflow-x:auto;scrollbar-width:none}
.nav nav::-webkit-scrollbar{display:none}
.nav a{color:var(--mute);text-decoration:none;font-size:13.5px;font-weight:500;white-space:nowrap;cursor:pointer}
.nav a:hover{color:var(--blue)}
.hero{background:var(--white);border-bottom:1px solid var(--line);padding:80px 0 60px}
.hero h1{font-size:50px;font-weight:800;letter-spacing:-.035em;max-width:18ch}
.hero h1 em{font-style:normal;color:var(--blue)}
.hero .l2{font-size:20px;color:var(--mute);margin-top:20px;max-width:68ch}
.stats{display:flex;flex-wrap:wrap;margin-top:30px;border-top:1px solid var(--line);border-bottom:1px solid var(--line)}
.stats>div{flex:1 1 125px;padding:18px 15px 18px 0}
.stats b{display:block;font-size:26px;color:var(--blue);font-weight:800;letter-spacing:-.03em}
.stats span{font-size:12.5px;color:var(--mute);display:block;margin-top:2px}
.wrow{display:flex;gap:16px;padding:14px 0;border-bottom:1px solid var(--line);align-items:baseline}
.wrow:last-child{border-bottom:0}
.wrow .wk{font-size:16.5px;color:var(--ink);font-weight:600;min-width:265px;flex-shrink:0}
.wrow .wv{flex:1;font-size:16px;color:var(--mute)}
.four{display:grid;grid-template-columns:repeat(4,1fr);gap:12px;margin-top:22px}
.fc{border:1px solid var(--line);border-radius:12px;padding:22px 19px;background:var(--white)}
.fc h4{font-size:19px}
.fc .fs{font-size:14px;color:var(--blue);font-weight:600;margin-top:3px}
.fc p{font-size:15px;color:var(--mute);margin-top:10px;line-height:1.55}
.pk{display:flex;gap:14px;padding:14px 0;border-bottom:1px solid var(--line);align-items:baseline}
.pk:last-child{border-bottom:0}
.pk .pn{font-size:16.5px;color:var(--ink);font-weight:600;min-width:200px;flex-shrink:0}
.pk .pw{font-size:13px;color:var(--blue);font-weight:700;min-width:165px;flex-shrink:0}
.pk .pd{flex:1;font-size:15.5px;color:var(--mute)}
.pk .pt{font-size:13px;color:var(--faint);min-width:70px;text-align:right;flex-shrink:0}
.wm{display:flex;gap:14px;padding:14px 0;border-bottom:1px solid var(--line);align-items:baseline}
.wm:last-child{border-bottom:0}
.wm .wl{font-size:16.5px;color:var(--ink);font-weight:600;min-width:250px;flex-shrink:0}
.wm .wn{font-size:19px;color:var(--blue);font-weight:800;letter-spacing:-.02em;min-width:170px;flex-shrink:0}
.wm .wd{flex:1;font-size:15.5px;color:var(--mute)}
.affg{display:flex;flex-wrap:wrap;gap:7px;margin-top:18px}
.af{border:1px solid var(--line);background:var(--white);border-radius:8px;padding:9px 14px;
font-family:inherit;font-size:14px;color:var(--body);cursor:pointer;font-weight:500}
.af:hover{border-color:var(--blue-l);color:var(--blue)}
.af.on{background:var(--blue);border-color:var(--blue);color:#fff}
.afd{margin-top:14px;background:var(--blue-p);border:1px solid var(--blue-b);border-radius:11px;
padding:16px 20px;font-size:16px;color:var(--blue-d)}
.afd b{color:var(--blue)}
.cgrid{display:grid;grid-template-columns:repeat(3,1fr);gap:12px;margin-top:20px}
.cc{background:var(--white);border:1px solid var(--line);border-radius:12px;padding:20px 18px;
cursor:pointer;text-align:left;font-family:inherit;transition:all .18s}
.cc:hover{border-color:var(--blue-l);box-shadow:var(--sh-l);transform:translateY(-2px)}
.cc .cn{font-size:10.5px;font-weight:700;letter-spacing:.1em;text-transform:uppercase;color:var(--faint)}
.cc h4{font-size:18px;margin-top:5px}
.cc .cs{font-size:14px;color:var(--blue);font-weight:600;margin-top:3px}
.cc p{font-size:14.5px;color:var(--mute);margin-top:8px;line-height:1.5}
.back{background:none;border:0;color:var(--blue);font-family:inherit;font-size:14px;font-weight:600;cursor:pointer;padding:0;margin-bottom:16px}
.det{background:var(--white);border:1px solid var(--line);border-radius:15px;overflow:hidden;box-shadow:var(--sh)}
.dh{padding:26px 30px;border-bottom:1px solid var(--line)}
.dh h3{font-size:27px}
.dh .ds{font-size:17px;color:var(--blue);font-weight:600;margin-top:4px}
.dh p{font-size:16.5px;color:var(--mute);margin-top:10px;max-width:70ch}
.sr{display:flex;gap:14px;padding:16px 30px;border-bottom:1px solid var(--line);cursor:pointer;
align-items:baseline;background:none;border-left:0;border-right:0;border-top:0;width:100%;text-align:left;font-family:inherit;color:inherit}
.sr:last-child{border-bottom:0}
.sr:hover .st2{color:var(--blue)}
.sr .sn{font-size:11.5px;font-weight:700;color:var(--blue);min-width:22px;flex-shrink:0}
.sr .sb{flex:1}
.sr .st2{font-size:18px;color:var(--ink);font-weight:600;display:block}
.sr .ss2{font-size:15px;color:var(--mute);margin-top:2px;display:block}
.sr .sx{font-size:12.5px;color:var(--faint);flex-shrink:0}
.sess{padding:8px 30px 22px}
.sess .sl{font-size:10.5px;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:var(--blue);margin:16px 0 8px}
.sess ol{margin-left:18px}
.sess li{font-size:17px;color:var(--body);margin-bottom:8px}
.pill{display:inline-block;font-size:14px;background:var(--blue-p);color:var(--blue-d);
border:1px solid var(--blue-b);padding:6px 12px;border-radius:7px;margin:3px 4px 3px 0}
.pipe{border:1px solid var(--line);border-radius:12px;background:var(--white);margin-bottom:10px;overflow:hidden}
.ph2{padding:18px 22px;background:var(--bg);border-bottom:1px solid var(--line);cursor:pointer;
display:flex;gap:14px;align-items:baseline;flex-wrap:wrap}
.ph2 .pnum{font-size:13px;font-weight:800;color:var(--blue);min-width:26px}
.ph2 h4{font-size:19px;flex:1;min-width:170px}
.ph2 .pdd{font-size:15px;color:var(--mute);width:100%;padding-left:40px}
.pb2{padding:8px 22px 16px 62px;display:none}
.pipe.on .pb2{display:block}
.pb2 ul{list-style:none}
.pb2 li{font-size:15.5px;color:var(--body);padding:5px 0 5px 18px;position:relative}
.pb2 li::before{content:"";position:absolute;left:0;top:13px;width:6px;height:6px;border-radius:99px;background:var(--blue-b)}
.aa{display:flex;gap:14px;padding:13px 0;border-bottom:1px solid var(--line);align-items:baseline}
.aa:last-child{border-bottom:0}
.aa .al{font-size:17px;color:var(--blue);font-weight:800;min-width:120px;flex-shrink:0}
.aa .ad{flex:1;font-size:16px;color:var(--mute)}
.big{background:var(--white);border-left:3px solid var(--blue);padding:20px 25px;margin-top:22px;
font-size:20px;color:var(--ink);font-weight:600;letter-spacing:-.02em;border-radius:0 11px 11px 0}
.cta{background:var(--blue-d);color:#fff;text-align:center;padding:68px 0}
.cta h2{color:#fff;font-size:33px;letter-spacing:-.03em}
.cta p{color:#bfdbfe;font-size:18px;margin-top:13px;max-width:62ch;margin-left:auto;margin-right:auto}
footer{background:var(--ink);color:var(--faint);padding:26px 0;font-size:13.5px}
@media(max-width:1000px){.cgrid{grid-template-columns:repeat(2,1fr)}.four{grid-template-columns:repeat(2,1fr)}
.hero h1{font-size:37px}}
@media(max-width:640px){section{padding:48px 0}.hero{padding:48px 0 40px}.hero h1{font-size:28px}
.hero .l2{font-size:17px}h2.sh{font-size:24px}.cgrid,.four{grid-template-columns:1fr}
.dh,.sr,.sess{padding-left:20px;padding-right:20px}
.wrow,.pk,.wm,.aa{flex-direction:column;gap:4px}
.wrow .wk,.pk .pn,.pk .pw,.wm .wl,.wm .wn,.aa .al{min-width:0}
.pk .pt{text-align:left}.pb2{padding-left:24px}.cta h2{font-size:24px}}
@media(prefers-reduced-motion:reduce){*{transition:none!important}}"""

BODY = """
<header><div class="wrap nav"><div class="brand">Small Group <span>Curriculum</span></div>
<nav><a data-j="week">This Week</a><a data-j="six">Why Six</a><a data-j="find">The Library</a>
<a data-j="pack">What Ships</a><a data-j="who">Four Audiences</a><a data-j="pastor">Pastor&rsquo;s Library</a></nav>
</div></header>

<div class="hero"><div class="wrap">
<div class="eyebrow">Finder &amp; Builder</div>
<h1>What are we studying <em>this week</em>?</h1>
<p class="l2" id="thesis"></p>
<div class="stats"><div><b>15</b><span>clusters</span></div><div><b>120</b><span>studies</span></div>
<div><b>720</b><span>sessions</span></div><div><b>20</b><span>affinity editions</span></div>
<div><b>2,400</b><span>combinations</span></div><div><b>6</b><span>sessions, always</span></div></div></div></div>

<section id="week"><div class="wrap"><div class="eyebrow">The Question</div>
<h2 class="sh">Five inputs, ninety seconds, one answer.</h2>
<p class="lede">Most groups answer this by asking around, buying whatever is on the shelf and starting three weeks late.</p>
<div id="week2" style="margin-top:20px"></div>
<div class="big">A group that cannot answer this question in one meeting will drift for a month, and some of them will not come back.</div></div></section>

<section id="six" style="background:var(--white);border-top:1px solid var(--line);border-bottom:1px solid var(--line)">
<div class="wrap"><div class="eyebrow">The Constraint</div>
<h2 class="sh">Every study is six sessions. No exceptions.</h2>
<p class="lede">One length means one format, one leader training, one print template, and a group that never has to relearn anything.</p>
<div id="six2" style="margin-top:20px"></div></div></section>

<section id="find"><div class="wrap"><div id="fh"><div class="eyebrow">The Library</div>
<h2 class="sh">Fifteen clusters. One hundred and twenty studies.</h2>
<p class="lede">Choose the room first, then the topic. The affinity edition changes the examples, the pace and the questions &mdash; never the theology or the structure.</p>
<div class="eyebrow" style="margin-top:26px">Who is in the room</div>
<div class="affg" id="affg"></div><div class="afd" id="afd"></div></div>
<div class="cgrid" id="cg"></div><div id="detail"></div></div></section>

<section id="pack" style="background:var(--white);border-top:1px solid var(--line);border-bottom:1px solid var(--line)">
<div class="wrap"><div class="eyebrow">What Ships</div>
<h2 class="sh">Six components with every study.</h2>
<p class="lede">Including a ten-minute teaching script, written out, for a pastor or a host who would rather read than improvise.</p>
<div id="pack2" style="margin-top:20px"></div>
<div class="eyebrow" style="margin-top:44px">The Word Math</div>
<h3 style="font-size:22px">How much writing this actually is.</h3>
<div id="wm2" style="margin-top:14px"></div>
<div class="big">Fifty-eight million words across all editions. That number is the entire argument for generating from a source rather than commissioning writers.</div></div></section>

<section id="who"><div class="wrap"><div class="eyebrow">One Subscription</div>
<h2 class="sh">Four audiences, one library.</h2>
<p class="lede">Included in the church platform subscription rather than sold separately, because the value is that everybody uses the same thing.</p>
<div class="four" id="aud2"></div></div></section>

<section id="pastor" style="background:var(--white);border-top:1px solid var(--line)"><div class="wrap">
<div class="eyebrow">The Pastor&rsquo;s Library Project</div>
<h2 class="sh">How a pastor loads thirty years of preaching.</h2>
<p class="lede" id="pipenote"></p>
<div id="pipe2" style="margin-top:22px"></div>
<div class="eyebrow" style="margin-top:44px">The Standard</div>
<h3 style="font-size:22px">Straight A&rsquo;s &mdash; all seven, not five.</h3>
<p class="lede">An archive that is authentic but never analyzed is still a folder. One that is analyzed but never approved is not his.</p>
<div id="sevena" style="margin-top:16px"></div></div></section>

<div class="cta"><div class="wrap"><h2>Never ask what we are studying next again.</h2>
<p>One hundred and twenty studies, twenty editions, six sessions every time &mdash; and the pastor&rsquo;s own archive underneath all of it.</p></div></div>
<footer><div class="wrap">Small Group Curriculum &middot; 120 studies &middot; 720 sessions &middot; 20 editions &middot; 2,400 combinations</div></footer>
"""

JS = """
var D=__DATA__;var st={aff:0,cl:null,s:null};
function el(i){return document.getElementById(i);}
el("thesis").innerHTML=D.thesis;
el("pipenote").innerHTML=D.pipenote;

function rows(id,arr){var h="",i;for(i=0;i<arr.length;i++){
h+='<div class="wrow"><span class="wk">'+arr[i][0]+'</span><span class="wv">'+arr[i][1]+'</span></div>';}
el(id).innerHTML=h;}

function rAff(){var h="",i;for(i=0;i<D.aff.length;i++){
h+='<button class="af'+(st.aff===i?" on":"")+'" data-a="'+i+'">'+D.aff[i][0]+'</button>';}
el("affg").innerHTML=h;
el("afd").innerHTML='<b>'+D.aff[st.aff][0]+' edition.</b> '+D.aff[st.aff][1];
var b=document.querySelectorAll(".af");for(i=0;i<b.length;i++){b[i].onclick=function(){
st.aff=parseInt(this.getAttribute("data-a"),10);rAff();rDet();};}}

function rCl(){
if(st.cl!==null){el("cg").innerHTML="";el("fh").style.display="none";return;}
el("fh").style.display="block";
var h="",i;for(i=0;i<D.cl.length;i++){var c=D.cl[i];
h+='<button class="cc" data-c="'+i+'"><div class="cn">'+c.st.length+' studies</div>';
h+='<h4>'+c.n+'</h4><div class="cs">'+c.sub+'</div><p>'+c.why+'</p></button>';}
el("cg").innerHTML=h;
var b=document.querySelectorAll(".cc");for(i=0;i<b.length;i++){b[i].onclick=function(){
st.cl=parseInt(this.getAttribute("data-c"),10);st.s=null;rAll();};}}

function rDet(){var box=el("detail");
if(st.cl===null){box.innerHTML="";return;}
var c=D.cl[st.cl],i,A=D.aff[st.aff][0];
var h='<button class="back" id="bk">&larr; '+(st.s===null?"All fifteen clusters":c.n)+'</button>';
if(st.s===null){
 h+='<div class="det"><div class="dh"><h3>'+c.n+'</h3><div class="ds">'+c.sub+'</div><p>'+c.why+'</p>';
 h+='<p style="font-size:15px;color:var(--faint);margin-top:8px">Showing the <strong>'+A+'</strong> edition. Every study is six sessions.</p></div>';
 for(i=0;i<c.st.length;i++){var s=c.st[i];
  h+='<button class="sr" data-s="'+i+'"><span class="sn">'+(i+1)+'</span><span class="sb">';
  h+='<span class="st2">'+s.t+'</span><span class="ss2">'+s.sub+'</span></span>';
  h+='<span class="sx">6 sessions &rsaquo;</span></button>';}
 h+='</div>';
}else{
 var s=c.st[st.s];
 h+='<div class="det"><div class="dh"><h3>'+s.t+'</h3><div class="ds">'+s.sub+'</div>';
 h+='<p style="font-size:15px;color:var(--faint);margin-top:8px">'+c.n+' &middot; <strong>'+A+'</strong> edition &middot; 6 sessions &middot; 24,480 words</p></div>';
 h+='<div class="sess"><div class="sl">The six sessions</div><ol>';
 for(i=0;i<s.ss.length;i++){h+='<li>'+s.ss[i]+'</li>';}
 h+='</ol>';
 h+='<div class="sl">What ships with it</div><div>';
 for(i=0;i<D.pack.length;i++){h+='<span class="pill">'+D.pack[i][0]+'</span>';}
 h+='</div>';
 h+='<div class="sl">Available in every edition</div><div>';
 for(i=0;i<D.aff.length;i++){h+='<span class="pill" style="'+(i===st.aff?"background:var(--blue);color:#fff;border-color:var(--blue)":"background:var(--bg);color:var(--body);border-color:var(--line)")+'">'+D.aff[i][0]+'</span>';}
 h+='</div></div></div>';
}
box.innerHTML=h;
el("bk").onclick=function(){if(st.s!==null){st.s=null;}else{st.cl=null;}rAll();};
var b=document.querySelectorAll(".sr");
for(i=0;i<b.length;i++){b[i].onclick=function(){st.s=parseInt(this.getAttribute("data-s"),10);rAll();};}}

function rPack(){var h="",i;for(i=0;i<D.pack.length;i++){var p=D.pack[i];
h+='<div class="pk"><span class="pn">'+p[0]+'</span><span class="pw">'+p[1]+'</span>';
h+='<span class="pd">'+p[2]+'</span><span class="pt">'+p[3]+'</span></div>';}
el("pack2").innerHTML=h;
h="";for(i=0;i<D.wm.length;i++){var w=D.wm[i];
h+='<div class="wm"><span class="wl">'+w[0]+'</span><span class="wn">'+w[1]+'</span>';
h+='<span class="wd">'+w[2]+'</span></div>';}
el("wm2").innerHTML=h;}

function rAud(){var h="",i;for(i=0;i<D.aud.length;i++){
h+='<div class="fc"><h4>'+D.aud[i][0]+'</h4><div class="fs">'+D.aud[i][1]+'</div>';
h+='<p>'+D.aud[i][2]+'</p></div>';}el("aud2").innerHTML=h;}

function rPipe(){var h="",i,j;for(i=0;i<D.pipe.length;i++){var p=D.pipe[i];
h+='<div class="pipe'+(i===0?" on":"")+'"><div class="ph2" data-p="'+i+'"><span class="pnum">'+p[0]+'</span>';
h+='<h4>'+p[1]+'</h4><div class="pdd">'+p[2]+'</div></div><div class="pb2"><ul>';
for(j=0;j<p[3].length;j++){h+='<li>'+p[3][j]+'</li>';}
h+='</ul></div></div>';}
el("pipe2").innerHTML=h;
var b=document.querySelectorAll(".ph2");for(i=0;i<b.length;i++){b[i].onclick=function(){
this.parentNode.classList.toggle("on");};}
h="";for(i=0;i<D.sevena.length;i++){
h+='<div class="aa"><span class="al">'+D.sevena[i][0]+'</span><span class="ad">'+D.sevena[i][1]+'</span></div>';}
el("sevena").innerHTML=h;}

function rAll(){rCl();rDet();}
rows("week2",D.week);rows("six2",D.sixwhy);rAff();rAll();rPack();rAud();rPipe();
var jl=document.querySelectorAll("[data-j]");for(var z=0;z<jl.length;z++){jl[z].onclick=function(){
var t=this.getAttribute("data-j");if(t==="find"){st.cl=null;st.s=null;rAll();}
el(t).scrollIntoView({block:"start"});};}
"""

SHELL = """<!DOCTYPE html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Small Group Curriculum &mdash; Finder, Builder and the Pastor's Library</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<style>__CSS__</style></head><body>__BODY__<script>__JS__</script></body></html>"""

out = SHELL.replace("__CSS__", CSS).replace("__BODY__", BODY)
out = out.replace("__JS__", JS.replace("__DATA__", json.dumps(payload, separators=(",", ":"))))
open("/mnt/user-data/outputs/small-group-curriculum.html", "w", encoding="utf-8").write(out)
print("studies:", NS, "| sessions:", NSESS, "| KB:", round(len(out)/1024, 1))
