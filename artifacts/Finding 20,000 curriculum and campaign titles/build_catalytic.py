# -*- coding: utf-8 -*-
import json
import catalytic_lib as L

payload = {"thesis": L.THESIS, "dist": L.DISTINCTION, "place": L.PLACEMENTS,
           "get": L.WHAT_YOU_GET, "dp": L.DEVO_PATTERN, "drule": L.DEVO_RULE,
           "camps": L.CAMPAIGNS}

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
.brand{font-weight:800;font-size:16px;color:var(--ink);flex-shrink:0}
.brand span{color:var(--blue)}
.nav nav{display:flex;gap:20px;margin-left:auto;overflow-x:auto;scrollbar-width:none}
.nav nav::-webkit-scrollbar{display:none}
.nav a{color:var(--mute);text-decoration:none;font-size:14px;font-weight:500;white-space:nowrap;cursor:pointer}
.nav a:hover{color:var(--blue)}
.hero{background:var(--white);border-bottom:1px solid var(--line);padding:84px 0 66px}
.hero h1{font-size:54px;font-weight:800;letter-spacing:-.035em;max-width:17ch}
.hero h1 em{font-style:normal;color:var(--blue)}
.hero .l2{font-size:20px;color:var(--mute);margin-top:22px;max-width:66ch}
.stats{display:flex;flex-wrap:wrap;margin-top:32px;border-top:1px solid var(--line);border-bottom:1px solid var(--line)}
.stats>div{flex:1 1 140px;padding:19px 18px 19px 0}
.stats b{display:block;font-size:28px;color:var(--blue);font-weight:800;letter-spacing:-.03em}
.stats span{font-size:13.5px;color:var(--mute);display:block;margin-top:3px}
.vs{display:grid;grid-template-columns:1fr 1fr;gap:16px;margin-top:24px}
.vc{border:1px solid var(--line);border-radius:14px;padding:26px;background:var(--white)}
.vc:last-child{border-color:var(--blue);border-width:2px;padding:25px;background:var(--blue-p)}
.vc .vt{font-size:11px;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:var(--faint)}
.vc:last-child .vt{color:var(--blue)}
.vc h4{font-size:23px;margin-top:7px}
.vc .vs2{font-size:16px;color:var(--blue-l);font-weight:600;margin-top:4px}
.vc p{font-size:16px;color:var(--mute);margin-top:11px;line-height:1.6}
.vc:last-child p{color:var(--blue-d)}
.vc .vf{font-size:15px;margin-top:14px;padding-top:12px;border-top:1px solid var(--line);font-style:italic;color:var(--mute)}
.pl{display:grid;grid-template-columns:repeat(3,1fr);gap:14px;margin-top:22px}
.plc{border:1px solid var(--line);border-radius:12px;padding:22px 20px;background:var(--white)}
.plc .pn{font-size:11px;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:var(--blue)}
.plc h4{font-size:20px;margin-top:6px}
.plc p{font-size:15.5px;color:var(--mute);margin-top:9px;line-height:1.55}
.plc .pb{font-size:14.5px;color:var(--blue-d);margin-top:12px;padding-top:10px;border-top:1px solid var(--line);font-weight:600}
.wrow{display:flex;gap:16px;padding:15px 0;border-bottom:1px solid var(--line);align-items:baseline}
.wrow .wk{font-size:16.5px;color:var(--ink);font-weight:600;min-width:230px;flex-shrink:0}
.wrow .wv{flex:1;font-size:16px;color:var(--mute)}
.d7{display:grid;grid-template-columns:repeat(7,1fr);gap:8px;margin-top:20px}
.d7c{border:1px solid var(--line);border-radius:10px;padding:14px 11px;background:var(--white);text-align:center}
.d7c .dn{font-size:10px;font-weight:700;letter-spacing:.1em;text-transform:uppercase;color:var(--blue)}
.d7c h5{font-size:15px;margin-top:5px}
.d7c p{font-size:12.5px;color:var(--mute);margin-top:5px;line-height:1.4}
.cgrid{display:grid;grid-template-columns:repeat(3,1fr);gap:12px;margin-top:22px}
.cc{background:var(--white);border:1px solid var(--line);border-radius:12px;padding:22px 20px;
cursor:pointer;text-align:left;font-family:inherit;transition:all .18s}
.cc:hover{border-color:var(--blue-l);box-shadow:var(--sh-l);transform:translateY(-2px)}
.cc h4{font-size:19px}
.cc .cs{font-size:14.5px;color:var(--blue);font-weight:600;margin-top:3px}
.cc .cg{font-size:13px;color:var(--faint);margin-top:11px}
.back{background:none;border:0;color:var(--blue);font-family:inherit;font-size:14px;font-weight:600;cursor:pointer;padding:0;margin-bottom:16px}
.pack{background:var(--white);border:1px solid var(--line);border-radius:15px;overflow:hidden;box-shadow:var(--sh)}
.ph{padding:30px 32px;border-bottom:1px solid var(--line)}
.ph .pc{font-size:11px;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:var(--blue)}
.ph h3{font-size:30px;margin-top:8px}
.ph .ps{font-size:19px;color:var(--mute);margin-top:5px;font-style:italic}
.ptabs{display:flex;flex-wrap:wrap;gap:7px;padding:18px 32px;border-bottom:1px solid var(--line);background:var(--bg)}
.pt2{border:1px solid var(--line);background:var(--white);border-radius:8px;padding:9px 15px;
font-family:inherit;font-size:13.5px;color:var(--body);cursor:pointer;font-weight:500}
.pt2:hover{border-color:var(--blue-l);color:var(--blue)}
.pt2.on{background:var(--blue);border-color:var(--blue);color:#fff}
.pbody{padding:26px 32px}
.gsec{padding-bottom:20px;margin-bottom:20px;border-bottom:1px solid var(--line)}
.gsec:last-child{border-bottom:0;margin-bottom:0;padding-bottom:0}
.gsec .gl{font-size:10.5px;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:var(--blue);margin-bottom:9px}
.gsec .gq{font-size:21px;color:var(--ink);font-weight:600;letter-spacing:-.02em;line-height:1.35}
.gsec p{font-size:17px;color:var(--body)}
.mv{padding:14px 0;border-bottom:1px solid var(--line)}
.mv:last-child{border-bottom:0}
.mv .mn{font-size:12px;font-weight:700;color:var(--blue)}
.mv .mt{font-size:18px;color:var(--ink);font-weight:600;margin-top:4px}
.mv .ml2{font-size:16px;color:var(--blue-d);margin-top:5px;font-style:italic}
.dr{display:flex;gap:14px;padding:15px 0;border-bottom:1px solid var(--line);align-items:baseline}
.dr:last-child{border-bottom:0}
.dr .dn2{font-size:12px;font-weight:700;color:var(--blue);min-width:44px;flex-shrink:0}
.dr .db{flex:1}
.dr .dt{font-size:17px;color:var(--ink);font-weight:600}
.dr .dp{font-size:13.5px;color:var(--blue);font-weight:600;margin-top:2px}
.dr .di{font-size:15.5px;color:var(--mute);margin-top:4px}
.dr .dq{font-size:15.5px;color:var(--body);margin-top:5px;font-style:italic}
.dr .da{font-size:14.5px;color:var(--blue-d);margin-top:5px}
.lad{display:grid;grid-template-columns:repeat(3,1fr);gap:12px;margin-top:6px}
.lc{border:1px solid var(--line);border-radius:11px;padding:18px 16px;background:var(--bg)}
.lc .ln{font-size:11px;font-weight:700;letter-spacing:.1em;text-transform:uppercase;color:var(--blue)}
.lc ol{margin:10px 0 0 16px;color:var(--body)}
.lc li{font-size:14.5px;margin-bottom:5px}
.lc p{font-size:14.5px;color:var(--mute);margin-top:9px}
.note2{background:#fffbeb;border:1px solid #fde68a;border-left:3px solid #f59e0b;border-radius:0 10px 10px 0;
padding:18px 22px;margin-top:20px;font-size:16px;color:#78350f}
.big{background:var(--white);border-left:3px solid var(--blue);padding:22px 26px;margin-top:24px;
font-size:21px;color:var(--ink);font-weight:600;letter-spacing:-.02em;border-radius:0 12px 12px 0}
.cta{background:var(--blue-d);color:#fff;text-align:center;padding:70px 0}
.cta h2{color:#fff;font-size:34px;letter-spacing:-.03em}
.cta p{color:#bfdbfe;font-size:18px;margin-top:14px;max-width:60ch;margin-left:auto;margin-right:auto}
footer{background:var(--ink);color:var(--faint);padding:28px 0;font-size:14px}
@media(max-width:1000px){.d7{grid-template-columns:repeat(4,1fr)}.cgrid{grid-template-columns:repeat(2,1fr)}
.vs,.pl,.lad{grid-template-columns:1fr}.hero h1{font-size:38px}}
@media(max-width:640px){section{padding:50px 0}.hero{padding:50px 0 42px}.hero h1{font-size:30px}
.hero .l2{font-size:18px}h2.sh{font-size:25px}.d7{grid-template-columns:repeat(2,1fr)}
.cgrid{grid-template-columns:1fr}.ph,.ptabs,.pbody{padding-left:20px;padding-right:20px}
.wrow,.dr{flex-direction:column;gap:5px}.wrow .wk,.dr .dn2{min-width:0}.cta h2{font-size:25px}}
@media(prefers-reduced-motion:reduce){*{transition:none!important}}"""

BODY = """
<header><div class="wrap nav"><div class="brand">Catalytic <span>Sermon Engine</span></div>
<nav><a data-j="diff">Overview vs Week One</a><a data-j="place">Three Placements</a>
<a data-j="get">What You Get</a><a data-j="devo">The Seven Days</a><a data-j="lib">Worked Examples</a></nav></div></header>

<div class="hero"><div class="wrap">
<div class="eyebrow">One Sunday, Any Sunday</div>
<h1>Every campaign can become <em>one sermon</em> that stands entirely alone.</h1>
<p class="l2" id="thesis"></p>
<div class="stats"><div><b>1</b><span>standalone sermon</span></div><div><b>7</b><span>daily devotionals</span></div>
<div><b>1</b><span>group guide</span></div><div><b>6</b><span>ladder rungs</span></div>
<div><b>52</b><span>Sundays a year</span></div></div></div></div>

<section id="diff"><div class="wrap"><div class="eyebrow">The Distinction</div>
<h2 class="sh" id="distline"></h2>
<div class="vs" id="vs"></div>
<div class="note2" id="distwhy"></div></div></section>

<section id="place" style="background:var(--white);border-top:1px solid var(--line);border-bottom:1px solid var(--line)">
<div class="wrap"><div class="eyebrow">Placement</div>
<h2 class="sh">Before, during, or never continued.</h2>
<p class="lede">The same sermon works in three positions, and the pastor chooses based on what he is trying to accomplish rather than on what the kit assumes.</p>
<div class="pl" id="pl"></div></div></section>

<section id="get"><div class="wrap"><div class="eyebrow">The Package</div>
<h2 class="sh">Five things arrive with every sermon.</h2>
<div id="get2" style="margin-top:20px"></div></div></section>

<section id="devo" style="background:var(--white);border-top:1px solid var(--line)"><div class="wrap">
<div class="eyebrow">The Week</div><h2 class="sh">Seven days is one idea, not seven ideas.</h2>
<div class="d7" id="d7"></div>
<div class="big" id="drule"></div></div></section>

<section id="lib"><div class="wrap"><div id="libhead"><div class="eyebrow">Worked Examples</div>
<h2 class="sh">Six campaigns, built all the way through.</h2>
<p class="lede">Each one shows the complete package &mdash; the standalone sermon, the seven days, the group guide and the ladder into three, four, six weeks or twenty-one, thirty, forty days. The same engine runs against every campaign in the library.</p></div>
<div class="cgrid" id="cgrid"></div><div id="detail"></div></div></section>

<div class="cta"><div class="wrap"><h2>Inspire, encourage, equip &mdash; on any given Sunday.</h2>
<p>One sermon that can stay one sermon, or become six weeks, or become forty days. The pastor decides after he preaches it, not before.</p></div></div>
<footer><div class="wrap">Catalytic Sermon Engine &middot; One Sunday &middot; Seven days &middot; One group guide &middot; Six ways forward</div></footer>
"""

JS = """
var D=__DATA__;var st={c:null,tab:"sermon"};
function el(i){return document.getElementById(i);}
el("thesis").innerHTML=D.thesis;
el("distline").innerHTML=D.dist.line;
el("distwhy").innerHTML="<strong>Why it matters.</strong> "+D.dist.why;
el("drule").innerHTML=D.drule;

function rDist(){var h="",i;for(i=0;i<D.dist.rows.length;i++){var r=D.dist.rows[i];
h+='<div class="vc"><div class="vt">'+(i===0?"Most kits ship this":"This is the one that sells")+'</div>';
h+='<h4>'+r[0]+'</h4><div class="vs2">'+r[1]+'</div><p>'+r[2]+'</p>';
h+='<div class="vf">'+r[3]+'</div></div>';}el("vs").innerHTML=h;}

function rPlace(){var h="",i;for(i=0;i<D.place.length;i++){var p=D.place[i];
h+='<div class="plc"><div class="pn">'+p[1]+'</div><h4>'+p[0]+'</h4><p>'+p[2]+'</p>';
h+='<div class="pb">'+p[3]+'</div></div>';}el("pl").innerHTML=h;}

function rGet(){var h="",i;for(i=0;i<D.get.length;i++){
h+='<div class="wrow"><span class="wk">'+D.get[i][0]+'</span><span class="wv">'+D.get[i][1]+'</span></div>';}
el("get2").innerHTML=h;}

function rD7(){var h="",i;for(i=0;i<D.dp.length;i++){
h+='<div class="d7c"><div class="dn">'+D.dp[i][0]+'</div><h5>'+D.dp[i][1]+'</h5><p>'+D.dp[i][2]+'</p></div>';}
el("d7").innerHTML=h;}

function rCards(){
if(st.c!==null){el("cgrid").innerHTML="";el("libhead").style.display="none";return;}
el("libhead").style.display="block";
var h="",i;for(i=0;i<D.camps.length;i++){var c=D.camps[i];
h+='<button class="cc" data-c="'+i+'"><h4>'+c.s.t+'</h4><div class="cs">'+c.s.sub+'</div>';
h+='<div class="cg">From: '+c.t+' &middot; 7 days &middot; group guide &middot; 6 ways forward</div></button>';}
el("cgrid").innerHTML=h;
var b=document.querySelectorAll(".cc");for(i=0;i<b.length;i++){b[i].onclick=function(){
st.c=parseInt(this.getAttribute("data-c"),10);st.tab="sermon";rAll();};}}

function rDetail(){var box=el("detail");
if(st.c===null){box.innerHTML="";return;}
var c=D.camps[st.c],S=c.s,i,h='<button class="back" id="bk">&larr; All six examples</button>';
h+='<div class="pack"><div class="ph"><div class="pc">From the campaign: '+c.t+'</div>';
h+='<h3>'+S.t+'</h3><div class="ps">'+S.sub+'</div></div>';
var TABS=[["sermon","The Sermon"],["days","Seven Days"],["group","Group Guide"],["ladder","What Follows"]];
h+='<div class="ptabs">';
for(i=0;i<TABS.length;i++){h+='<button class="pt2'+(st.tab===TABS[i][0]?" on":"")+'" data-t="'+TABS[i][0]+'">'+TABS[i][1]+'</button>';}
h+='</div><div class="pbody">';
if(st.tab==="sermon"){
 h+='<div class="gsec"><div class="gl">Big idea</div><div class="gq">'+S.idea+'</div></div>';
 h+='<div class="gsec"><div class="gl">Text</div><p>'+S.text+'</p></div>';
 h+='<div class="gsec"><div class="gl">The open</div><p>'+S.hook+'</p></div>';
 h+='<div class="gsec"><div class="gl">Movements &mdash; with the landing line written out</div>';
 for(i=0;i<S.moves.length;i++){h+='<div class="mv"><div class="mn">0'+(i+1)+'</div>';
  h+='<div class="mt">'+S.moves[i][0]+'</div><div class="ml2">'+S.moves[i][1]+'</div></div>';}
 h+='</div>';
 h+='<div class="gsec"><div class="gl">The close</div><div class="gq">'+S.close+'</div></div>';
 h+='<div class="gsec"><div class="gl">Before they leave</div><p>'+S.ask+'</p></div>';
}
else if(st.tab==="days"){
 h+='<div class="gsec"><div class="gl">Seven daily devotionals from this one message</div>';
 for(i=0;i<c.d.length;i++){var dd=c.d[i];
  h+='<div class="dr"><span class="dn2">Day '+(i+1)+'</span><span class="db">';
  h+='<span class="dt">'+dd[0]+'</span><span class="dp">'+dd[1]+'</span>';
  h+='<span class="di">'+dd[2]+'</span><span class="dq">'+dd[3]+'</span>';
  h+='<span class="da">Today: '+dd[4]+'</span></span></div>';}
 h+='</div>';
}
else if(st.tab==="group"){
 h+='<div class="gsec"><div class="gl">Open with this</div><div class="gq">'+c.g.open+'</div></div>';
 h+='<div class="gsec"><div class="gl">Four questions</div><ol style="margin-left:18px">';
 for(i=0;i<c.g.qs.length;i++){h+='<li style="font-size:17px;margin-bottom:8px">'+c.g.qs[i]+'</li>';}
 h+='</ol></div>';
 h+='<div class="gsec"><div class="gl">Application</div><p>'+c.g.apply+'</p></div>';
 h+='<div class="gsec"><div class="gl">Prayer</div><p>'+c.g.pray+'</p></div>';
}
else{
 h+='<div class="gsec"><div class="gl">If they want more &mdash; six ways forward from the same message</div>';
 h+='<div class="lad">';
 var keys=[["3","Three weeks"],["4","Four weeks"],["6","Six weeks"]];
 for(i=0;i<keys.length;i++){h+='<div class="lc"><div class="ln">'+keys[i][1]+'</div><ol>';
  var a=c.l[keys[i][0]];for(var j=0;j<a.length;j++){h+='<li>'+a[j]+'</li>';}
  h+='</ol></div>';}
 h+='</div><div class="lad" style="margin-top:12px">';
 var k2=[["21","Twenty-one days"],["30","Thirty days"],["40","Forty days"]];
 for(i=0;i<k2.length;i++){h+='<div class="lc"><div class="ln">'+k2[i][1]+'</div><p>'+c.l[k2[i][0]]+'</p></div>';}
 h+='</div></div>';
 h+='<div class="gsec"><div class="gl">And if they want none of it</div><p>The sermon was complete. Nothing is owed, nothing was withheld, and the pastor can preach it again in three years to a congregation that is two-thirds new.</p></div>';
}
h+='</div></div>';
box.innerHTML=h;
el("bk").onclick=function(){st.c=null;rAll();};
var t=document.querySelectorAll(".pt2");
for(i=0;i<t.length;i++){t[i].onclick=function(){st.tab=this.getAttribute("data-t");rDetail();};}}

function rAll(){rCards();rDetail();}
rDist();rPlace();rGet();rD7();rAll();
var jl=document.querySelectorAll("[data-j]");for(var z=0;z<jl.length;z++){jl[z].onclick=function(){
var t=this.getAttribute("data-j");if(t==="lib"){st.c=null;rAll();}
el(t).scrollIntoView({block:"start"});};}
"""

SHELL = """<!DOCTYPE html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Catalytic Sermon Engine &mdash; One Sunday, Any Sunday</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<style>__CSS__</style></head><body>__BODY__<script>__JS__</script></body></html>"""

out = SHELL.replace("__CSS__", CSS).replace("__BODY__", BODY)
out = out.replace("__JS__", JS.replace("__DATA__", json.dumps(payload, separators=(",", ":"))))
open("/mnt/user-data/outputs/catalytic-sermon-engine.html", "w", encoding="utf-8").write(out)
print("campaigns:", len(L.CAMPAIGNS), "| KB:", round(len(out)/1024, 1))
