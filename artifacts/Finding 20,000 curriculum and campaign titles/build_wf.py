# -*- coding: utf-8 -*-
import json
import wf_lib as W
import print_lib as P

payload = {"thesis":W.THESIS,"why":W.WHY,"cats":W.CATS,
 "pthesis":P.PRINT_THESIS,"prules":P.PRINT_RULES,
 "groups":[{"n":g[0],"c":g[1],"d":g[2],"tt":[{"n":t[0],"f":t[1],"s":t[2],"u":t[3]} for t in g[3]]} for g in P.GROUPS],
 "integ":P.INTEGRATION,"econ":P.ECONOMICS}
NE = sum(len(c["ee"]) for c in W.CATS)
NT = sum(len(g["tt"]) for g in payload["groups"])

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
.nav{display:flex;align-items:center;gap:22px;height:62px}
.brand{font-weight:800;font-size:15.5px;color:var(--ink);flex-shrink:0}
.brand span{color:var(--blue)}
.nav nav{display:flex;gap:19px;margin-left:auto;overflow-x:auto;scrollbar-width:none}
.nav nav::-webkit-scrollbar{display:none}
.nav a{color:var(--mute);text-decoration:none;font-size:13.5px;font-weight:500;white-space:nowrap;cursor:pointer}
.nav a:hover{color:var(--blue)}
.hero{background:var(--white);border-bottom:1px solid var(--line);padding:80px 0 62px}
.hero h1{font-size:50px;font-weight:800;letter-spacing:-.035em;max-width:18ch}
.hero h1 em{font-style:normal;color:var(--blue)}
.hero .l2{font-size:20px;color:var(--mute);margin-top:20px;max-width:66ch}
.stats{display:flex;flex-wrap:wrap;margin-top:30px;border-top:1px solid var(--line);border-bottom:1px solid var(--line)}
.stats>div{flex:1 1 130px;padding:18px 16px 18px 0}
.stats b{display:block;font-size:27px;color:var(--blue);font-weight:800;letter-spacing:-.03em}
.stats span{font-size:13px;color:var(--mute);display:block;margin-top:2px}
.wrow{display:flex;gap:16px;padding:14px 0;border-bottom:1px solid var(--line);align-items:baseline}
.wrow:last-child{border-bottom:0}
.wrow .wk{font-size:16.5px;color:var(--ink);font-weight:600;min-width:270px;flex-shrink:0}
.wrow .wv{flex:1;font-size:16px;color:var(--mute)}
.cgrid{display:grid;grid-template-columns:repeat(2,1fr);gap:12px;margin-top:22px}
.cc{background:var(--white);border:1px solid var(--line);border-radius:12px;padding:22px 20px;
cursor:pointer;text-align:left;font-family:inherit;transition:all .18s}
.cc:hover{border-color:var(--blue-l);box-shadow:var(--sh-l);transform:translateY(-2px)}
.cc .cn{font-size:10.5px;font-weight:700;letter-spacing:.1em;text-transform:uppercase;color:var(--faint)}
.cc h4{font-size:20px;margin-top:6px}
.cc .cs{font-size:14.5px;color:var(--blue);font-weight:600;margin-top:3px}
.cc p{font-size:15px;color:var(--mute);margin-top:9px;line-height:1.55}
.back{background:none;border:0;color:var(--blue);font-family:inherit;font-size:14px;font-weight:600;cursor:pointer;padding:0;margin-bottom:16px}
.det{background:var(--white);border:1px solid var(--line);border-radius:15px;overflow:hidden;box-shadow:var(--sh)}
.dh{padding:28px 32px;border-bottom:1px solid var(--line)}
.dh h3{font-size:28px}
.dh .ds{font-size:18px;color:var(--blue);font-weight:600;margin-top:4px}
.dh p{font-size:16.5px;color:var(--mute);margin-top:11px;max-width:70ch}
.dh .dw{font-size:14.5px;color:var(--faint);margin-top:9px}
.dsec{padding:22px 32px;border-bottom:1px solid var(--line)}
.dsec:last-child{border-bottom:0}
.dsec .dl{font-size:10.5px;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:var(--blue);margin-bottom:10px}
.pill{display:inline-block;font-size:14px;background:var(--blue-p);color:var(--blue-d);
border:1px solid var(--blue-b);padding:6px 12px;border-radius:7px;margin:3px 4px 3px 0}
.pill.g{background:var(--bg);color:var(--body);border-color:var(--line)}
.ee{display:grid;grid-template-columns:1fr 1fr;gap:0 26px}
.er{display:flex;gap:12px;padding:11px 0;border-bottom:1px solid var(--line);align-items:baseline}
.er .en{font-size:11.5px;font-weight:700;color:var(--blue);min-width:22px;flex-shrink:0}
.er .eb{flex:1}
.er .et{font-size:16.5px;color:var(--ink);font-weight:600;display:block}
.er .es{font-size:14.5px;color:var(--mute);margin-top:2px;display:block}
.note{background:#fffbeb;border-top:1px solid #fde68a;padding:20px 32px}
.note .dl{color:#b45309}
.note p{font-size:16px;color:#78350f}
.big{background:var(--white);border-left:3px solid var(--blue);padding:20px 25px;margin-top:22px;
font-size:20px;color:var(--ink);font-weight:600;letter-spacing:-.02em;border-radius:0 11px 11px 0}
.gg{border:1px solid var(--line);border-radius:12px;background:var(--white);margin-bottom:12px;overflow:hidden}
.ghd{padding:18px 22px;background:var(--bg);border-bottom:1px solid var(--line);cursor:pointer;
display:flex;gap:12px;align-items:baseline;flex-wrap:wrap}
.ghd h4{font-size:19px;flex:1;min-width:190px}
.ghd .gc{font-size:12.5px;font-weight:700;color:var(--blue);background:var(--white);
border:1px solid var(--blue-b);padding:4px 10px;border-radius:6px}
.ghd .gd{font-size:14.5px;color:var(--mute);width:100%}
.gbd{padding:6px 22px 14px;display:none}
.gg.on .gbd{display:block}
.tr2{display:flex;gap:14px;padding:12px 0;border-bottom:1px solid var(--line);align-items:baseline}
.tr2:last-child{border-bottom:0}
.tr2 .tn{font-size:16.5px;color:var(--ink);font-weight:600;min-width:230px;flex-shrink:0}
.tr2 .tf{font-size:13px;color:var(--blue);font-weight:700;min-width:150px;flex-shrink:0}
.tr2 .ts{font-size:13px;color:var(--faint);min-width:110px;flex-shrink:0}
.tr2 .tu{flex:1;font-size:15.5px;color:var(--mute)}
.cta{background:var(--blue-d);color:#fff;text-align:center;padding:68px 0}
.cta h2{color:#fff;font-size:33px;letter-spacing:-.03em}
.cta p{color:#bfdbfe;font-size:18px;margin-top:13px;max-width:60ch;margin-left:auto;margin-right:auto}
footer{background:var(--ink);color:var(--faint);padding:26px 0;font-size:13.5px}
@media(max-width:1000px){.cgrid{grid-template-columns:1fr}.ee{grid-template-columns:1fr}.hero h1{font-size:37px}}
@media(max-width:640px){section{padding:48px 0}.hero{padding:48px 0 40px}.hero h1{font-size:28px}
.hero .l2{font-size:17px}h2.sh{font-size:24px}
.dh,.dsec,.note{padding-left:20px;padding-right:20px}
.wrow,.tr2{flex-direction:column;gap:4px}.wrow .wk,.tr2 .tn,.tr2 .tf{min-width:0}
.cta h2{font-size:24px}}
@media(prefers-reduced-motion:reduce){*{transition:none!important}}"""

BODY = """
<header><div class="wrap nav"><div class="brand">Weddings, Funerals <span>&amp; Print</span></div>
<nav><a data-j="why">The Gap</a><a data-j="find">The Library</a><a data-j="print">100 Templates</a>
<a data-j="integ">Integration</a><a data-j="econ">Economics</a></nav></div></header>

<div class="hero"><div class="wrap">
<div class="eyebrow">Finder &amp; Builder</div>
<h1>The largest gap in Christian publishing, and <em>nobody has filled it</em>.</h1>
<p class="l2" id="thesis"></p>
<div class="stats"><div><b>10</b><span>categories</span></div><div><b>200</b><span>services and messages</span></div>
<div><b>50</b><span>tools</span></div><div><b>40</b><span>add-ins</span></div>
<div><b>100</b><span>print templates</span></div></div></div></div>

<section id="why"><div class="wrap"><div class="eyebrow">Why This</div>
<h2 class="sh">Five reasons this is worth more than another sermon library.</h2>
<div id="why2" style="margin-top:20px"></div>
<div class="big">A family will remember what you said at their mother&rsquo;s funeral for thirty years, word for word, accurately or not. Nothing else a pastor preaches carries that.</div></div></section>

<section id="find" style="background:var(--white);border-top:1px solid var(--line);border-bottom:1px solid var(--line)">
<div class="wrap"><div id="fh"><div class="eyebrow">The Library</div>
<h2 class="sh">Ten categories. Two hundred services.</h2>
<p class="lede">Five for weddings, five for funerals. Each opens to twenty worked entries, five tools, four add-ins, five grounding passages and leader notes written for a pastor with forty-eight hours.</p></div>
<div class="cgrid" id="cg"></div><div id="detail"></div></div></section>

<section id="print"><div class="wrap"><div class="eyebrow">Production</div>
<h2 class="sh">One hundred print templates.</h2>
<p class="lede">Every library on this platform describes a deliverable and none of them produces one. This is the layer that turns a described resource into a file a church hands somebody on Sunday. Select any group to open it.</p>
<div id="grp" style="margin-top:22px"></div>
<div class="eyebrow" style="margin-top:44px">Seven Rules</div>
<h3 style="font-size:22px">What separates a template from a document.</h3>
<div id="prules" style="margin-top:14px"></div></div></section>

<section id="integ" style="background:var(--white);border-top:1px solid var(--line)"><div class="wrap">
<div class="eyebrow">Integration</div><h2 class="sh">How the templates attach to the curriculum.</h2>
<p class="lede">The mapping is fixed rather than chosen each time, which is what makes generation possible at all.</p>
<div id="integ2" style="margin-top:20px"></div></div></section>

<section id="econ"><div class="wrap"><div class="eyebrow">Economics</div>
<h2 class="sh">Why print is the product and digital is the sample.</h2>
<div id="econ2" style="margin-top:20px"></div>
<div class="big">A church will download a PDF and never use it. A box of ninety journals arriving on a Tuesday gets used.</div></div></section>

<div class="cta"><div class="wrap"><h2>The moment a family first meets a church.</h2>
<p>Weddings and funerals are how households decide whether to come back. Printed properly, they are also the best thing a church ever hands anyone.</p></div></div>
<footer><div class="wrap">Weddings, Funerals &amp; Print &middot; 10 categories &middot; 200 services &middot; 100 templates</div></footer>
"""

JS = """
var D=__DATA__;var st={c:null,g:{}};
function el(i){return document.getElementById(i);}
el("thesis").innerHTML=D.thesis;

function rWhy(){var h="",i;for(i=0;i<D.why.length;i++){
h+='<div class="wrow"><span class="wk">'+D.why[i][0]+'</span><span class="wv">'+D.why[i][1]+'</span></div>';}
el("why2").innerHTML=h;
h="";for(i=0;i<D.prules.length;i++){
h+='<div class="wrow"><span class="wk">'+D.prules[i][0]+'</span><span class="wv">'+D.prules[i][1]+'</span></div>';}
el("prules").innerHTML=h;
h="";for(i=0;i<D.integ.length;i++){
h+='<div class="wrow"><span class="wk">'+D.integ[i][0]+'</span><span class="wv">'+D.integ[i][1]+'</span></div>';}
el("integ2").innerHTML=h;
h="";for(i=0;i<D.econ.length;i++){
h+='<div class="wrow"><span class="wk">'+D.econ[i][0]+'</span><span class="wv">'+D.econ[i][1]+'</span></div>';}
el("econ2").innerHTML=h;}

function rCats(){
if(st.c!==null){el("cg").innerHTML="";el("fh").style.display="none";return;}
el("fh").style.display="block";
var h="",i;for(i=0;i<D.cats.length;i++){var c=D.cats[i];
h+='<button class="cc" data-c="'+i+'"><div class="cn">'+(i<5?"Weddings":"Funerals")+' &middot; '+c.ee.length+' entries</div>';
h+='<h4>'+c.n+'</h4><div class="cs">'+c.sub+'</div><p>'+c.why+'</p></button>';}
el("cg").innerHTML=h;
var b=document.querySelectorAll(".cc");for(i=0;i<b.length;i++){b[i].onclick=function(){
st.c=parseInt(this.getAttribute("data-c"),10);rAll();};}}

function rDet(){var box=el("detail");
if(st.c===null){box.innerHTML="";return;}
var c=D.cats[st.c],i,h='<button class="back" id="bk">&larr; All ten categories</button>';
h+='<div class="det"><div class="dh"><h3>'+c.n+'</h3><div class="ds">'+c.sub+'</div>';
h+='<p>'+c.why+'</p><div class="dw">When: '+c.when+'</div></div>';
h+='<div class="dsec"><div class="dl">Twenty worked entries</div><div class="ee">';
for(i=0;i<c.ee.length;i++){
 h+='<div class="er"><span class="en">'+(i<9?"0":"")+(i+1)+'</span><span class="eb">';
 h+='<span class="et">'+c.ee[i][0]+'</span><span class="es">'+c.ee[i][1]+'</span></span></div>';}
h+='</div></div>';
h+='<div class="dsec"><div class="dl">Tools in this category</div><div>';
for(i=0;i<c.tools.length;i++){h+='<span class="pill">'+c.tools[i]+'</span>';}
h+='</div></div>';
h+='<div class="dsec"><div class="dl">Add-ins &mdash; the printed pieces that ship with it</div><div>';
for(i=0;i<c.addins.length;i++){h+='<span class="pill g">'+c.addins[i]+'</span>';}
h+='</div></div>';
h+='<div class="dsec"><div class="dl">Grounding passages</div><div>';
for(i=0;i<c.pas.length;i++){h+='<span class="pill">'+c.pas[i]+'</span>';}
h+='</div></div>';
h+='<div class="note"><div class="dl">Leader notes</div><p>'+c.notes+'</p></div></div>';
box.innerHTML=h;
el("bk").onclick=function(){st.c=null;rAll();};}

function rGroups(){var h="",i,j;for(i=0;i<D.groups.length;i++){var g=D.groups[i];
h+='<div class="gg'+(st.g[i]?" on":"")+'"><div class="ghd" data-g="'+i+'"><h4>'+g.n+'</h4>';
h+='<span class="gc">'+g.c+'</span><div class="gd">'+g.d+'</div></div><div class="gbd">';
for(j=0;j<g.tt.length;j++){var t=g.tt[j];
 h+='<div class="tr2"><span class="tn">'+t.n+'</span><span class="tf">'+t.f+'</span>';
 h+='<span class="ts">'+t.s+'</span><span class="tu">'+t.u+'</span></div>';}
h+='</div></div>';}
el("grp").innerHTML=h;
var b=document.querySelectorAll(".ghd");for(i=0;i<b.length;i++){b[i].onclick=function(){
var k=parseInt(this.getAttribute("data-g"),10);st.g[k]=!st.g[k];rGroups();};}}

function rAll(){rCats();rDet();}
rWhy();rAll();rGroups();
var jl=document.querySelectorAll("[data-j]");for(var z=0;z<jl.length;z++){jl[z].onclick=function(){
var t=this.getAttribute("data-j");if(t==="find"){st.c=null;rAll();}
el(t).scrollIntoView({block:"start"});};}
"""

SHELL = """<!DOCTYPE html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Weddings, Funerals &amp; Print &mdash; Finder, Builder and 100 Templates</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<style>__CSS__</style></head><body>__BODY__<script>__JS__</script></body></html>"""

out = SHELL.replace("__CSS__", CSS).replace("__BODY__", BODY)
out = out.replace("__JS__", JS.replace("__DATA__", json.dumps(payload, separators=(",", ":"))))
open("/mnt/user-data/outputs/weddings-funerals-print.html", "w", encoding="utf-8").write(out)
print("entries:", NE, "| templates:", NT, "| KB:", round(len(out)/1024, 1))
