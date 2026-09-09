# -*- coding: utf-8 -*-
import json
import fingrow_data as F

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
section{padding:80px 0}
.eyebrow{font-size:11.5px;font-weight:700;letter-spacing:.14em;text-transform:uppercase;color:var(--blue);margin-bottom:14px}
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
.hero{background:var(--white);border-bottom:1px solid var(--line);padding:88px 0 70px}
.hero h1{font-size:55px;font-weight:800;letter-spacing:-.035em;max-width:17ch}
.hero h1 em{font-style:normal;color:var(--blue)}
.hero .l2{font-size:21px;color:var(--mute);margin-top:22px;max-width:64ch}
.stats{display:flex;flex-wrap:wrap;margin-top:34px;border-top:1px solid var(--line);border-bottom:1px solid var(--line)}
.stats>div{flex:1 1 150px;padding:20px 18px 20px 0}
.stats b{display:block;font-size:29px;color:var(--blue);font-weight:800;letter-spacing:-.03em}
.stats span{font-size:13.5px;color:var(--mute);display:block;margin-top:3px}
.two{display:grid;grid-template-columns:1fr 1fr;gap:16px;margin-top:30px}
.tw{background:var(--white);border:1px solid var(--line);border-radius:14px;padding:28px 26px}
.tw:last-child{border-color:var(--blue-b);background:var(--blue-p)}
.tw .tg{font-size:10.5px;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:var(--faint)}
.tw:last-child .tg{color:var(--blue)}
.tw h3{font-size:24px;margin-top:8px}
.tw p{font-size:16.5px;color:var(--mute);margin-top:10px;line-height:1.6}
.tw:last-child p{color:var(--blue-d)}
.tw .pills{display:flex;flex-wrap:wrap;gap:6px;margin-top:16px}
.tw .pills span{font-size:13.5px;background:var(--bg);border:1px solid var(--line);padding:6px 11px;border-radius:7px}
.tw:last-child .pills span{background:var(--white);border-color:var(--blue-b)}
.dgrid{display:grid;grid-template-columns:repeat(3,1fr);gap:12px;margin-top:26px}
.dc{background:var(--white);border:1px solid var(--line);border-radius:12px;padding:22px 20px;
cursor:pointer;text-align:left;font-family:inherit;transition:all .18s}
.dc:hover{border-color:var(--blue-l);box-shadow:var(--sh-l);transform:translateY(-2px)}
.dc.on{border-color:var(--blue);border-width:2px;padding:21px 19px}
.dc h4{font-size:18px}
.dc p{font-size:14.5px;color:var(--mute);margin-top:7px;line-height:1.5}
.dbody{margin-top:18px;background:var(--white);border:1px solid var(--line);border-radius:15px;
overflow:hidden;box-shadow:var(--sh)}
.dh2{padding:28px 32px;border-bottom:1px solid var(--line)}
.dh2 h3{font-size:26px}
.dh2 .q{font-size:18px;color:var(--blue);font-weight:600;margin-top:6px}
.dh2 p{font-size:16.5px;color:var(--mute);margin-top:12px;max-width:70ch}
.dsub{padding:22px 32px}
.dsub .lb{font-size:11px;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:var(--blue);margin-bottom:12px}
.dsub ul{list-style:none;display:grid;grid-template-columns:1fr 1fr;gap:8px 24px}
.dsub li{font-size:16px;color:var(--body);padding-left:20px;position:relative}
.dsub li::before{content:"";position:absolute;left:0;top:10px;width:7px;height:7px;border-radius:99px;background:var(--blue-b)}
.dtools{padding:0 32px 22px}
.dtools .pills{display:flex;flex-wrap:wrap;gap:7px;margin-top:10px}
.dtools .pills span{font-size:14px;background:var(--blue-p);color:var(--blue-d);border:1px solid var(--blue-b);
padding:7px 13px;border-radius:8px;font-weight:500}
.dband{padding:20px 32px;background:var(--bg);border-top:1px solid var(--line);font-size:16.5px;color:var(--ink)}
.dband b{display:block;font-size:11px;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:var(--blue);margin-bottom:5px}
.assess{background:var(--white);border:1px solid var(--line);border-radius:16px;box-shadow:var(--sh-l);overflow:hidden;margin-top:26px}
.ahead{padding:26px 32px;border-bottom:1px solid var(--line);display:flex;justify-content:space-between;
align-items:center;gap:18px;flex-wrap:wrap}
.ahead h3{font-size:22px}
.prog{display:flex;align-items:center;gap:12px}
.ptrk{width:130px;height:6px;background:var(--line);border-radius:99px;overflow:hidden}
.pfil{height:100%;background:var(--blue);width:0;border-radius:99px;transition:width .3s}
.pct{font-size:13px;font-weight:700;color:var(--blue);min-width:56px;text-align:right}
.qs{padding:10px 32px 6px}
.qrow{padding:16px 0;border-bottom:1px solid var(--line)}
.qrow:last-child{border-bottom:0}
.qt{font-size:16.5px;color:var(--ink);font-weight:500;margin-bottom:11px}
.opts{display:flex;gap:8px;flex-wrap:wrap}
.opt{border:1px solid var(--line);background:var(--white);border-radius:8px;padding:8px 14px;
font-family:inherit;font-size:14px;color:var(--body);cursor:pointer;font-weight:500;transition:all .15s}
.opt:hover{border-color:var(--blue-l);color:var(--blue)}
.opt.on{background:var(--blue);border-color:var(--blue);color:#fff}
.afoot{padding:22px 32px;background:var(--bg);border-top:1px solid var(--line);
display:flex;justify-content:space-between;align-items:center;gap:16px;flex-wrap:wrap}
.afoot .note{font-size:14px;color:var(--mute)}
.btn{background:var(--blue);color:#fff;border:0;border-radius:9px;padding:12px 24px;
font-family:inherit;font-size:15px;font-weight:600;cursor:pointer}
.btn:hover{background:var(--blue-d)}
.btn:disabled{background:var(--line);color:var(--faint);cursor:not-allowed}
.res{margin-top:20px;background:var(--white);border:2px solid var(--blue);border-radius:16px;overflow:hidden}
.rh{padding:30px 32px;background:var(--blue);color:#fff}
.rh .rl{font-size:11.5px;font-weight:700;letter-spacing:.14em;text-transform:uppercase;opacity:.85}
.rh .sc{font-size:46px;font-weight:800;letter-spacing:-.03em;margin-top:6px}
.rh h3{color:#fff;font-size:26px;margin-top:4px}
.rh p{font-size:17px;margin-top:10px;opacity:.92;max-width:62ch}
.rb{padding:26px 32px}
.rb .lb{font-size:11px;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:var(--blue);margin-bottom:12px}
.bandrow{display:flex;gap:14px;padding:12px 0;border-bottom:1px solid var(--line);align-items:baseline}
.bandrow:last-child{border-bottom:0}
.bandrow.hit{background:var(--blue-p);margin:0 -12px;padding:12px}
.bandrow .bn{font-size:15px;font-weight:700;color:var(--blue);min-width:74px}
.bandrow .bt{font-size:16.5px;font-weight:600;color:var(--ink);min-width:220px}
.bandrow .bd{flex:1;font-size:15.5px;color:var(--mute)}
.trow{display:flex;gap:16px;padding:15px 0;border-bottom:1px solid var(--line);align-items:baseline}
.trow .tk{font-size:16.5px;color:var(--ink);font-weight:600;min-width:230px;flex-shrink:0}
.trow .tw2{font-size:13px;color:var(--blue);font-weight:700;min-width:120px;flex-shrink:0}
.trow .tv{flex:1;font-size:16px;color:var(--mute)}
.trow .tg2{font-size:10.5px;font-weight:700;letter-spacing:.1em;text-transform:uppercase;color:var(--navy);
background:var(--blue-p);color:var(--blue);padding:4px 9px;border-radius:5px;flex-shrink:0}
.bar{display:flex;gap:14px;padding:18px 0;border-bottom:1px solid var(--line);align-items:flex-start}
.bar .bnum{font-size:17px;font-weight:800;color:var(--blue);min-width:96px;flex-shrink:0;letter-spacing:-.02em}
.bar .bb{flex:1}
.bar .bt2{font-size:19px;font-weight:700;color:var(--ink)}
.bar .bd2{font-size:16px;color:var(--mute);margin-top:5px}
.bar ul{list-style:none;margin-top:10px;display:grid;grid-template-columns:1fr 1fr;gap:6px 20px}
.bar li{font-size:15px;color:var(--body);padding-left:18px;position:relative}
.bar li::before{content:"";position:absolute;left:0;top:10px;width:6px;height:6px;border-radius:99px;background:var(--blue-b)}
.eng{background:var(--white);border:1px solid var(--line);border-radius:14px;padding:26px;margin-top:14px}
.eng .en2{display:flex;justify-content:space-between;gap:14px;align-items:baseline;flex-wrap:wrap}
.eng h4{font-size:23px}
.eng .lib{font-size:12.5px;font-weight:700;color:var(--blue);background:var(--blue-p);
border:1px solid var(--blue-b);padding:5px 11px;border-radius:7px}
.eng .ed{font-size:16.5px;color:var(--mute);margin-top:10px;max-width:70ch}
.eng ul{list-style:none;margin-top:14px;display:grid;grid-template-columns:1fr 1fr;gap:7px 22px}
.eng li{font-size:15.5px;color:var(--body);padding-left:18px;position:relative}
.eng li::before{content:"";position:absolute;left:0;top:10px;width:6px;height:6px;border-radius:99px;background:var(--blue-b)}
.three{display:grid;grid-template-columns:repeat(3,1fr);gap:14px;margin-top:26px}
.th{background:var(--white);border:1px solid var(--line);border-radius:13px;padding:24px}
.th h4{font-size:20px}
.th .s{font-size:14.5px;color:var(--blue);font-weight:600;margin-top:3px}
.th p{font-size:15.5px;color:var(--mute);margin-top:10px;line-height:1.55}
.big{background:var(--white);border-left:3px solid var(--blue);padding:24px 28px;margin-top:26px;
font-size:22px;color:var(--ink);font-weight:600;letter-spacing:-.02em;border-radius:0 12px 12px 0}
.cta{background:var(--blue-d);color:#fff;text-align:center;padding:72px 0}
.cta h2{color:#fff;font-size:36px;letter-spacing:-.03em}
.cta p{color:#bfdbfe;font-size:18px;margin-top:14px;max-width:58ch;margin-left:auto;margin-right:auto}
footer{background:var(--ink);color:var(--faint);padding:30px 0;font-size:14px}
@media(max-width:1000px){.dgrid,.three{grid-template-columns:repeat(2,1fr)}.two{grid-template-columns:1fr}
.hero h1{font-size:40px}}
@media(max-width:640px){section{padding:52px 0}.hero{padding:52px 0 44px}.hero h1{font-size:31px}
.hero .l2{font-size:18px}h2.sh{font-size:26px}.dgrid,.three{grid-template-columns:1fr}
.dsub ul,.bar ul,.eng ul{grid-template-columns:1fr}
.qs,.ahead,.afoot,.dh2,.dsub,.dtools,.dband,.rb,.rh{padding-left:20px;padding-right:20px}
.trow,.bar{flex-direction:column;gap:6px}.trow .tk,.trow .tw2,.bar .bnum{min-width:0}
.bandrow{flex-direction:column;gap:4px}.bandrow .bt{min-width:0}
.rh .sc{font-size:36px}.cta h2{font-size:26px}}
@media(prefers-reduced-motion:reduce){*{transition:none!important}}"""

SHELL = """<!DOCTYPE html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1"><title>__TITLE__</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<style>__CSS__</style></head><body>__BODY__<script>__JS__</script></body></html>"""

# ---------- FINANCIAL ----------
FIN_BODY = """
<header><div class="wrap nav"><div class="brand">Church Financial <span>Health</span></div>
<nav><a data-j="split">Two Houses</a><a data-j="domains">Six Domains</a><a data-j="check">Health Check</a>
<a data-j="teach">Sermons</a><a data-j="curric">Curriculum</a><a data-j="coach">Coaching</a></nav></div></header>
<div class="hero"><div class="wrap">
<div class="eyebrow">Financial Intelligence to Financial Formation</div>
<h1>A funded church and a <em>generous church</em> are not the same thing.</h1>
<p class="l2">Most financial health products handle the institution's money or the household's money. Confusing the two is how a budget gets met while a congregation stays exactly as it was. This handles both, and keeps them distinct.</p>
<div class="stats"><div><b>6</b><span>domains</span></div><div><b>12</b><span>question health check</span></div>
<div><b>8</b><span>curriculum tracks</span></div><div><b>755</b><span>sermon messages</span></div>
<div><b>6</b><span>coaching tracks</span></div></div></div></div>
<section id="split"><div class="wrap"><div class="eyebrow">The Structure</div>
<h2 class="sh">Two houses, one roof.</h2>
<p class="lede">A church has two entirely different money problems, and almost nobody separates them. One is a competency problem. The other is a heart problem, and it is not solved by better bookkeeping.</p>
<div class="two" id="split2"></div></div></section>
<section id="domains" style="background:var(--white);border-top:1px solid var(--line);border-bottom:1px solid var(--line)">
<div class="wrap"><div class="eyebrow">The Library</div><h2 class="sh">Six domains, each with its own floor.</h2>
<p class="lede">Select a domain to see what it covers, the tools inside it, and the minimum credible standard.</p>
<div class="dgrid" id="dgrid"></div><div id="dbody"></div></div></section>
<section id="check"><div class="wrap"><div class="eyebrow">Diagnostic</div>
<h2 class="sh">Twelve questions. Then the honest answer.</h2>
<p class="lede">Scored one to four across both houses. Nothing here is scored against another church.</p>
<div id="assessbox"></div><div id="resbox"></div></div></section>
<section id="teach" style="background:var(--white);border-top:1px solid var(--line)"><div class="wrap">
<div class="eyebrow">Preaching</div><h2 class="sh">Seven hundred and fifty-five messages on money.</h2>
<p class="lede">Drawn from the sermon library. End-of-year giving alone runs six tracks and a hundred and seventy titles.</p>
<div id="serm"></div>
<div class="big">Never run formation and an ask in the same six weeks. Ninety days minimum between them, or the covenant is a lie and the congregation knows it.</div></div></section>
<section id="curric"><div class="wrap"><div class="eyebrow">Curriculum</div>
<h2 class="sh">Eight tracks, from struggling to significance.</h2>
<p class="lede">The progression is deliberate: struggling to stability to surplus to stewardship to significance. A church with only a budgeting class serves one end of its congregation.</p>
<div id="curr"></div></div></section>
<section id="coach" style="background:var(--white);border-top:1px solid var(--line)"><div class="wrap">
<div class="eyebrow">Coaching</div><h2 class="sh">The staff needs one shared language about money.</h2>
<p class="lede">Six coaching tracks by seat, plus one half-day that stops the team having six different conversations about the same money.</p>
<div id="coach2"></div></div></section>
<div class="cta"><div class="wrap"><h2>Fund the mission. Form the people. In that order, and never confused.</h2>
<p>Built on the same intelligence-to-formation architecture as the rest of the platform.</p></div></div>
<footer><div class="wrap">Church Financial Health &middot; Six domains &middot; Eight curriculum tracks &middot; 755 messages</div></footer>
"""

FIN_JS = """
var D=__DATA__;var st={dom:0,ans:{},shown:false};
function el(i){return document.getElementById(i);}
function rSplit(){var h="",i,j;for(i=0;i<D.split.length;i++){var s=D.split[i];
h+='<div class="tw"><div class="tg">'+s[1]+'</div><h3>'+s[0]+'</h3><p>'+s[2]+'</p><div class="pills">';
for(j=0;j<s[3].length;j++){h+='<span>'+s[3][j]+'</span>';}h+='</div></div>';}el("split2").innerHTML=h;}
function rDom(){var h="",i,j;for(i=0;i<D.dom.length;i++){h+='<button class="dc'+(st.dom===i?" on":"")+'" data-d="'+i+'">';
h+='<h4>'+D.dom[i].n+'</h4><p>'+D.dom[i].one+'</p></button>';}el("dgrid").innerHTML=h;
var X=D.dom[st.dom];h='<div class="dbody"><div class="dh2"><h3>'+X.n+'</h3><div class="q">'+X.one+'</div><p>'+X.why+'</p></div>';
h+='<div class="dsub"><div class="lb">What it covers</div><ul>';
for(j=0;j<X.sub.length;j++){h+='<li>'+X.sub[j]+'</li>';}h+='</ul></div>';
h+='<div class="dtools"><div class="lb">Tools included</div><div class="pills">';
for(j=0;j<X.tools.length;j++){h+='<span>'+X.tools[j]+'</span>';}h+='</div></div>';
h+='<div class="dband"><b>The floor</b>'+X.band+'</div></div>';el("dbody").innerHTML=h;
var b=document.querySelectorAll(".dc");for(i=0;i<b.length;i++){b[i].onclick=function(){st.dom=parseInt(this.getAttribute("data-d"),10);rDom();};}}
function nAns(){var n=0,i;for(i=0;i<D.qs.length;i++){if(st.ans[i]!==undefined)n++;}return n;}
function score(){var s=0,i;for(i=0;i<D.qs.length;i++){if(st.ans[i]!==undefined)s+=(4-st.ans[i]);}return s;}
function rAssess(){var i,j,n=nAns(),t=D.qs.length,p=Math.round(n/t*100);
var h='<div class="assess"><div class="ahead"><h3>Financial health check</h3><div class="prog">';
h+='<div class="ptrk"><div class="pfil" style="width:'+p+'%"></div></div><div class="pct">'+n+' of '+t+'</div></div></div><div class="qs">';
for(i=0;i<D.qs.length;i++){h+='<div class="qrow"><div class="qt">'+(i+1)+'. '+D.qs[i][0]+'</div><div class="opts">';
for(j=0;j<D.qs[i][1].length;j++){h+='<button class="opt'+(st.ans[i]===j?" on":"")+'" data-q="'+i+'" data-o="'+j+'">'+D.qs[i][1][j]+'</button>';}
h+='</div></div>';}
h+='</div><div class="afoot"><div class="note">Answer all twelve for an accurate band.</div>';
h+='<button class="btn" id="see"'+(n<t?" disabled":"")+'>See your score</button></div></div>';
el("assessbox").innerHTML=h;
var o=document.querySelectorAll(".opt");for(i=0;i<o.length;i++){o[i].onclick=function(){
var q=parseInt(this.getAttribute("data-q"),10),v=parseInt(this.getAttribute("data-o"),10);
if(st.ans[q]===v){delete st.ans[q];}else{st.ans[q]=v;}rAssess();if(st.shown)rRes();};}
var s=el("see");if(s){s.onclick=function(){st.shown=true;rRes();el("resbox").scrollIntoView({block:"start"});};}}
function rRes(){var box=el("resbox");if(!st.shown){box.innerHTML="";return;}
var sc=score(),i,hit=-1;
for(i=0;i<D.bands.length;i++){var r=D.bands[i][0].split(" to ");if(sc>=parseInt(r[0],10)&&sc<=parseInt(r[1],10))hit=i;}
if(hit<0)hit=0;
var h='<div class="res"><div class="rh"><div class="rl">Your score</div><div class="sc">'+sc+' / 48</div>';
h+='<h3>'+D.bands[hit][1]+'</h3><p>'+D.bands[hit][2]+'</p></div><div class="rb"><div class="lb">All four bands</div>';
for(i=0;i<D.bands.length;i++){h+='<div class="bandrow'+(i===hit?" hit":"")+'"><span class="bn">'+D.bands[i][0]+'</span>';
h+='<span class="bt">'+D.bands[i][1]+'</span><span class="bd">'+D.bands[i][2]+'</span></div>';}
box.innerHTML=h+'</div></div>';}
function rSerm(){var h="",i;for(i=0;i<D.serm.length;i++){h+='<div class="trow"><span class="tk">'+D.serm[i][0]+'</span>';
h+='<span class="tw2">'+D.serm[i][1]+' messages</span><span class="tv">'+D.serm[i][2]+'</span></div>';}el("serm").innerHTML=h;}
function rCurr(){var h="",i;for(i=0;i<D.curric.length;i++){h+='<div class="trow"><span class="tk">'+D.curric[i][0]+'</span>';
h+='<span class="tw2">'+D.curric[i][1]+'</span><span class="tv">'+D.curric[i][2]+'</span>';
h+='<span class="tg2">'+D.curric[i][3]+'</span></div>';}el("curr").innerHTML=h;}
function rCoach(){var h="",i;for(i=0;i<D.coach.length;i++){h+='<div class="trow"><span class="tk">'+D.coach[i][0]+'</span>';
h+='<span class="tw2">'+D.coach[i][1]+'</span><span class="tv">'+D.coach[i][2]+'</span></div>';}el("coach2").innerHTML=h;}
rSplit();rDom();rAssess();rRes();rSerm();rCurr();rCoach();
var jl=document.querySelectorAll("[data-j]");for(var z=0;z<jl.length;z++){jl[z].onclick=function(){
el(this.getAttribute("data-j")).scrollIntoView({block:"start"});};}
"""

fin_data = {"split": F.FIN_SPLIT, "dom": F.FIN_DOMAINS, "qs": F.FIN_QS, "bands": F.FIN_BANDS,
            "serm": F.FIN_SERMONS, "curric": F.FIN_CURRIC, "coach": F.FIN_COACH}
out = SHELL.replace("__TITLE__", "Church Financial Health — Fund the Mission, Form the People")
out = out.replace("__CSS__", CSS).replace("__BODY__", FIN_BODY)
out = out.replace("__JS__", FIN_JS.replace("__DATA__", json.dumps(fin_data, separators=(",", ":"))))
open("/mnt/user-data/outputs/church-financial-health.html", "w", encoding="utf-8").write(out)
print("financial:", round(len(out)/1024, 1), "KB")

# ---------- GROWTH ----------
GROW_BODY = """
<header><div class="wrap nav"><div class="brand">Church <span>Growth</span></div>
<nav><a data-j="math">The Math</a><a data-j="engines">Five Engines</a><a data-j="barriers">Barriers</a>
<a data-j="check">Diagnostic</a><a data-j="stages">Stages</a></nav></div></header>
<div class="hero"><div class="wrap">
<div class="eyebrow">Growth Intelligence to Church Formation</div>
<h1>Most churches try to fix growth with more <em>reach</em> when the leak is retention.</h1>
<p class="l2">If a hundred guests visit and eighty never return, another hundred guests changes nothing. Every strategy here starts by finding the leak, because reach spending on a leaking church is the most common waste in ministry.</p>
<div class="stats"><div><b>3</b><span>growth motions</span></div><div><b>5</b><span>engines</span></div>
<div><b>6</b><span>size barriers</span></div><div><b>10</b><span>question diagnostic</span></div>
<div><b>6</b><span>lifecycle stages</span></div></div></div></div>
<section id="math"><div class="wrap"><div class="eyebrow">First Principles</div>
<h2 class="sh">Three motions, and only one of them compounds.</h2>
<div class="three" id="math2"></div>
<div class="big" id="truth"></div></div></section>
<section id="engines" style="background:var(--white);border-top:1px solid var(--line);border-bottom:1px solid var(--line)">
<div class="wrap"><div class="eyebrow">The Engines</div><h2 class="sh">Invite. Welcome. Connect. Serve. Send.</h2>
<p class="lede">Five engines, each with its own library behind it. A church that runs all five compounds; a church that runs one plateaus at the ceiling of that one.</p>
<div id="eng"></div></div></section>
<section id="barriers"><div class="wrap"><div class="eyebrow">Ceilings</div>
<h2 class="sh">Every church stops at a number, and the number is predictable.</h2>
<p class="lede">Growth barriers are structural, not spiritual. Each one breaks for a specific reason and clears for a specific reason.</p>
<div id="bars"></div></div></section>
<section id="check" style="background:var(--white);border-top:1px solid var(--line)"><div class="wrap">
<div class="eyebrow">Diagnostic</div><h2 class="sh">Ten questions. Then stop guessing.</h2>
<p class="lede">Find out whether you have a reach problem, a retention problem or a leadership problem, before spending a dollar on any of them.</p>
<div id="assessbox"></div><div id="resbox"></div></div></section>
<section id="stages"><div class="wrap"><div class="eyebrow">Lifecycle</div>
<h2 class="sh">The same number means different things.</h2>
<p class="lede">Two hundred people in a three-year-old plant and two hundred in an eighty-year-old church are completely different situations requiring opposite interventions.</p>
<div id="stg"></div></div></section>
<div class="cta"><div class="wrap"><h2>Find the leak. Then open the tap.</h2>
<p>Growth strategy built on the same intelligence-to-formation architecture as the rest of the platform.</p></div></div>
<footer><div class="wrap">Church Growth &middot; Five engines &middot; Six barriers &middot; Ten-question diagnostic</div></footer>
"""

GROW_JS = """
var D=__DATA__;var st={ans:{},shown:false};
function el(i){return document.getElementById(i);}
function rMath(){var h="",i;for(i=0;i<D.math.length;i++){h+='<div class="th"><h4>'+D.math[i][0]+'</h4>';
h+='<div class="s">'+D.math[i][1]+'</div><p>'+D.math[i][2]+'</p></div>';}el("math2").innerHTML=h;
el("truth").innerHTML=D.truth;}
function rEng(){var h="",i,j;for(i=0;i<D.eng.length;i++){var E=D.eng[i];
h+='<div class="eng"><div class="en2"><h4>'+E[0]+'</h4><span class="lib">'+E[4]+'</span></div>';
h+='<div class="s" style="font-size:15px;color:var(--blue);font-weight:600">'+E[1]+'</div>';
h+='<p class="ed">'+E[2]+'</p><ul>';
for(j=0;j<E[3].length;j++){h+='<li>'+E[3][j]+'</li>';}h+='</ul></div>';}el("eng").innerHTML=h;}
function rBars(){var h="",i,j;for(i=0;i<D.bars.length;i++){var B=D.bars[i];
h+='<div class="bar"><span class="bnum">'+B[0]+'</span><span class="bb"><span class="bt2">'+B[1]+'</span>';
h+='<div class="bd2">'+B[2]+'</div><ul>';
for(j=0;j<B[3].length;j++){h+='<li>'+B[3][j]+'</li>';}h+='</ul></span></div>';}el("bars").innerHTML=h;}
function nAns(){var n=0,i;for(i=0;i<D.qs.length;i++){if(st.ans[i]!==undefined)n++;}return n;}
function score(){var s=0,i;for(i=0;i<D.qs.length;i++){if(st.ans[i]!==undefined)s+=(4-st.ans[i]);}return s;}
function rAssess(){var i,j,n=nAns(),t=D.qs.length,p=Math.round(n/t*100);
var h='<div class="assess"><div class="ahead"><h3>Growth diagnostic</h3><div class="prog">';
h+='<div class="ptrk"><div class="pfil" style="width:'+p+'%"></div></div><div class="pct">'+n+' of '+t+'</div></div></div><div class="qs">';
for(i=0;i<D.qs.length;i++){h+='<div class="qrow"><div class="qt">'+(i+1)+'. '+D.qs[i][0]+'</div><div class="opts">';
for(j=0;j<D.qs[i][1].length;j++){h+='<button class="opt'+(st.ans[i]===j?" on":"")+'" data-q="'+i+'" data-o="'+j+'">'+D.qs[i][1][j]+'</button>';}
h+='</div></div>';}
h+='</div><div class="afoot"><div class="note">Answer all ten for an accurate band.</div>';
h+='<button class="btn" id="see"'+(n<t?" disabled":"")+'>See the diagnosis</button></div></div>';
el("assessbox").innerHTML=h;
var o=document.querySelectorAll(".opt");for(i=0;i<o.length;i++){o[i].onclick=function(){
var q=parseInt(this.getAttribute("data-q"),10),v=parseInt(this.getAttribute("data-o"),10);
if(st.ans[q]===v){delete st.ans[q];}else{st.ans[q]=v;}rAssess();if(st.shown)rRes();};}
var s=el("see");if(s){s.onclick=function(){st.shown=true;rRes();el("resbox").scrollIntoView({block:"start"});};}}
function rRes(){var box=el("resbox");if(!st.shown){box.innerHTML="";return;}
var sc=score(),i,hit=-1;
for(i=0;i<D.bands.length;i++){var r=D.bands[i][0].split(" to ");if(sc>=parseInt(r[0],10)&&sc<=parseInt(r[1],10))hit=i;}
if(hit<0)hit=0;
var h='<div class="res"><div class="rh"><div class="rl">Your score</div><div class="sc">'+sc+' / 40</div>';
h+='<h3>'+D.bands[hit][1]+'</h3><p>'+D.bands[hit][2]+'</p></div><div class="rb"><div class="lb">All four bands</div>';
for(i=0;i<D.bands.length;i++){h+='<div class="bandrow'+(i===hit?" hit":"")+'"><span class="bn">'+D.bands[i][0]+'</span>';
h+='<span class="bt">'+D.bands[i][1]+'</span><span class="bd">'+D.bands[i][2]+'</span></div>';}
box.innerHTML=h+'</div></div>';}
function rStg(){var h="",i;for(i=0;i<D.stages.length;i++){h+='<div class="trow"><span class="tk">'+D.stages[i][0]+'</span>';
h+='<span class="tw2">'+D.stages[i][1]+'</span><span class="tv">'+D.stages[i][2]+'</span></div>';}el("stg").innerHTML=h;}
rMath();rEng();rBars();rAssess();rRes();rStg();
var jl=document.querySelectorAll("[data-j]");for(var z=0;z<jl.length;z++){jl[z].onclick=function(){
el(this.getAttribute("data-j")).scrollIntoView({block:"start"});};}
"""

grow_data = {"math": F.GROW_MATH, "truth": F.GROW_TRUTH, "eng": F.GROW_ENGINES, "bars": F.GROW_BARRIERS,
             "qs": F.GROW_QS, "bands": F.GROW_BANDS, "stages": F.GROW_STAGES}
out2 = SHELL.replace("__TITLE__", "Church Growth — Find the Leak, Then Open the Tap")
out2 = out2.replace("__CSS__", CSS).replace("__BODY__", GROW_BODY)
out2 = out2.replace("__JS__", GROW_JS.replace("__DATA__", json.dumps(grow_data, separators=(",", ":"))))
open("/mnt/user-data/outputs/church-growth-platform.html", "w", encoding="utf-8").write(out2)
print("growth:", round(len(out2)/1024, 1), "KB")
