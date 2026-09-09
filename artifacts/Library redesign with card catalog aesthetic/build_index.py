#!/usr/bin/env python3
# Builds the new "card catalog" INDEX.html from data.json
import json, re

d = json.load(open('/home/claude/library/data.json'))
A, GN, GD = d['A'], d['GN'], d['GD']

# Track codes + colors recalibrated for light paper
GK = ["FL", "MP", "FN", "PL", "SE", "CP", "CL", "BS"]
GC = ["#8A6B24", "#3D5B8C", "#3F7263", "#9C3D3A", "#467A54", "#7A4E7A", "#64488C", "#2F6B6B"]

# Assign call numbers by order within each group; refresh colors
counters = [0] * len(GN)
for rec in A:
    gi = rec['gi']
    counters[gi] += 1
    rec['cn'] = GK[gi] + "-" + ("%02d" % counters[gi])
    rec['c'] = GC[gi]

total = len(A)
sup = sum(1 for x in A if x['s'].startswith('Superseded'))
cur = total - sup

def dkey(s):
    m = re.match(r'(\d+)/(\d+)', s)
    return (int(m.group(1)), int(m.group(2))) if m else (0, 0)
latest = max(A, key=lambda x: dkey(x['d']))['d']

stats = str(total) + " WORKS &middot; " + str(len(GN)) + " TRACKS &middot; " + str(cur) + " CURRENT &middot; " + str(sup) + " SUPERSEDED &middot; UPDATED " + latest

def js(obj):
    return json.dumps(obj, ensure_ascii=True, separators=(',', ':')).replace('</', '<\\/')

TPL = r"""<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>The LifeTogether Library</title>
<link href="https://fonts.googleapis.com/css2?family=Archivo:wght@400;500;600;700;800&family=Courier+Prime:wght@400;700&family=Libre+Caslon+Display&family=Libre+Caslon+Text:ital,wght@0,400;0,700;1,400&display=swap" rel="stylesheet">
<style>
:root{--paper:#EDEAE0;--paper2:#E6E2D5;--card:#FBFAF4;--ink:#1F2A24;--ink2:#4C554E;--faint:#7C837A;--rule:#CFC9B6;--stamp:#565A9C;}
*{margin:0;padding:0;box-sizing:border-box;}
html{scroll-behavior:smooth;}
body{font-family:'Archivo',sans-serif;background:var(--paper);color:var(--ink);-webkit-font-smoothing:antialiased;}
body::before{content:'';position:fixed;inset:0;pointer-events:none;background:radial-gradient(ellipse at 50% -10%,rgba(255,255,255,.55),transparent 60%);}
a{color:inherit;}
button{font-family:'Archivo',sans-serif;}

/* ---- Bookplate masthead ---- */
.plate-wrap{padding:40px 18px 26px;position:relative;z-index:1;}
.plate{max-width:640px;margin:0 auto;border:1.5px solid var(--ink);box-shadow:inset 0 0 0 4px var(--paper),inset 0 0 0 5px rgba(31,42,36,.45);padding:30px 22px 24px;text-align:center;background:var(--card);}
.eyebrow{font-family:'Courier Prime',monospace;font-size:10.5px;font-weight:700;letter-spacing:3.5px;color:var(--ink2);margin-bottom:14px;}
h1{font-family:'Libre Caslon Display',serif;font-weight:400;font-size:clamp(30px,6.4vw,46px);line-height:1.04;letter-spacing:-.5px;margin-bottom:12px;}
.sub{font-family:'Libre Caslon Text',serif;font-style:italic;font-size:14.5px;line-height:1.6;color:var(--ink2);max-width:460px;margin:0 auto 18px;}
.stats{font-family:'Courier Prime',monospace;font-size:10px;font-weight:700;letter-spacing:1.6px;color:var(--faint);border-top:1px solid var(--rule);padding-top:14px;}

/* ---- Finder ---- */
.finder{position:sticky;top:0;z-index:50;background:rgba(237,234,224,.94);backdrop-filter:blur(10px);border-bottom:1px solid var(--rule);padding:10px 16px 0;}
.fin{max-width:1060px;margin:0 auto;}
.srch{width:100%;background:var(--card);border:1px solid var(--rule);border-bottom:2px solid var(--ink2);color:var(--ink);padding:11px 13px;font-size:14px;font-family:'Courier Prime',monospace;outline:none;}
.srch::placeholder{color:var(--faint);}
.srch:focus{border-color:var(--ink);border-bottom-color:var(--ink);}
.tabs{display:flex;gap:6px;flex-wrap:wrap;padding:9px 0 0;}
.tb{position:relative;border:1px solid var(--rule);border-bottom:none;background:var(--paper2);color:var(--ink2);font-size:10.5px;font-weight:800;letter-spacing:1.4px;padding:8px 12px 10px;cursor:pointer;border-radius:7px 7px 0 0;font-family:'Courier Prime',monospace;}
.tb:hover{background:var(--card);color:var(--ink);}
.tb.on{background:var(--card);color:var(--ink);border-color:var(--cc,var(--ink));border-bottom:none;box-shadow:inset 0 3px 0 var(--cc,var(--ink));}
.tb:focus-visible,.srch:focus-visible,.card:focus-visible{outline:2px solid var(--ink);outline-offset:2px;}

/* ---- Drawers ---- */
.wrap{max-width:1060px;margin:0 auto;padding:30px 16px 60px;position:relative;z-index:1;}
.grp{margin-bottom:44px;}
.grp-h{display:flex;align-items:baseline;gap:12px;flex-wrap:wrap;border-bottom:2px solid var(--gc);padding:0 2px 10px;margin-bottom:10px;}
.grp-k{font-family:'Courier Prime',monospace;font-size:11px;font-weight:700;letter-spacing:1.5px;color:var(--card);background:var(--gc);padding:3px 8px;border-radius:3px;}
.grp-t{font-family:'Libre Caslon Display',serif;font-size:clamp(19px,3vw,24px);line-height:1.1;}
.grp-n{font-family:'Courier Prime',monospace;font-size:10.5px;font-weight:700;letter-spacing:1.5px;color:var(--faint);margin-left:auto;}
.grp-d{font-size:12.5px;line-height:1.55;color:var(--ink2);max-width:640px;padding:0 2px;margin-bottom:8px;}
.cards{display:grid;grid-template-columns:repeat(auto-fill,minmax(320px,1fr));gap:26px 20px;padding-top:16px;}

/* ---- Catalog cards ---- */
.card{position:relative;display:block;text-decoration:none;background:var(--card);border:1px solid var(--rule);border-radius:3px;padding:15px 15px 14px;box-shadow:0 1px 0 rgba(31,42,36,.08),0 6px 14px -10px rgba(31,42,36,.28);}
.tab{position:absolute;top:-13px;left:13px;background:var(--cc);color:var(--card);font-family:'Courier Prime',monospace;font-size:10px;font-weight:700;letter-spacing:1.4px;padding:3px 10px 2px;border-radius:6px 6px 0 0;}
.c-meta{font-family:'Courier Prime',monospace;font-size:10.5px;color:var(--faint);letter-spacing:.4px;margin-bottom:7px;display:flex;gap:8px;flex-wrap:wrap;align-items:center;}
.dot{width:6px;height:6px;border-radius:50%;background:var(--cc);display:inline-block;flex:none;}
.c-t{font-family:'Libre Caslon Text',serif;font-weight:700;font-size:17.5px;line-height:1.25;margin-bottom:7px;}
.c-sm{font-size:12.8px;line-height:1.6;color:var(--ink2);}
.pts{margin-top:9px;border-top:1px dashed var(--rule);padding-top:8px;}
.pt{display:block;font-size:11.5px;line-height:1.5;color:var(--ink2);}
.pt::before{content:'\2014\00a0';color:var(--cc);font-weight:700;}
.card.sup{opacity:.82;background:#F4F1E7;}
.card.sup .c-t{color:var(--ink2);}
.stamp{position:absolute;top:8px;right:10px;transform:rotate(-7deg);border:2px solid var(--stamp);color:var(--stamp);font-family:'Courier Prime',monospace;font-size:9.5px;font-weight:700;letter-spacing:2.5px;padding:2px 7px 1px;border-radius:2px;opacity:.8;mix-blend-mode:multiply;}
.none{font-family:'Libre Caslon Text',serif;font-style:italic;text-align:center;color:var(--ink2);padding:70px 20px;font-size:15px;}

/* ---- Reference desk ---- */
.foot{max-width:1060px;margin:0 auto;padding:0 16px 70px;position:relative;z-index:1;}
.ref{display:block;text-decoration:none;border:1px dashed var(--ink2);border-radius:3px;padding:14px 16px;background:transparent;}
.ref b{font-family:'Courier Prime',monospace;font-size:10.5px;font-weight:700;letter-spacing:2px;color:var(--ink2);display:block;margin-bottom:4px;}
.ref span{font-family:'Libre Caslon Text',serif;font-style:italic;font-size:13.5px;color:var(--ink);}
.colophon{font-family:'Courier Prime',monospace;font-size:9.5px;letter-spacing:1.6px;color:var(--faint);text-align:center;padding-top:26px;}

@media (prefers-reduced-motion:no-preference){
 .card,.tb{transition:transform .16s ease,box-shadow .16s ease,background .16s ease;}
 @media (hover:hover){
  .card:hover{transform:translateY(-3px);box-shadow:0 1px 0 rgba(31,42,36,.08),0 14px 24px -12px rgba(31,42,36,.35);}
 }
}
@media (max-width:520px){
 .cards{grid-template-columns:1fr;}
 .plate{padding:24px 16px 20px;}
 .grp-n{margin-left:0;width:100%;}
}
</style></head><body>

<div class="plate-wrap"><div class="plate">
 <div class="eyebrow">LIFETOGETHER MINISTRIES &middot; WORKING ARCHIVE</div>
 <h1>The LifeTogether Library</h1>
 <div class="sub">Every working artifact, catalogued in eight tracks. Superseded versions stay on the shelf &mdash; stamped, not deleted.</div>
 <div class="stats">@@STATS@@</div>
</div></div>

<div class="finder"><div class="fin">
 <input id="q" class="srch" type="search" placeholder="Search titles, files, summaries, call numbers&hellip;" oninput="render()" aria-label="Search the library">
 <div class="tabs" id="tabs"></div>
</div></div>

<div class="wrap" id="out"></div>

<div class="foot">
 <a class="ref" href="CHATS-AND-PROJECTS.html" target="_blank">
  <b>REFERENCE DESK</b>
  <span>The map of chats and projects &mdash; where each artifact was made &rarr;</span>
 </a>
 <div class="colophon">CATALOGUED BY HAND &middot; SHELVED IN ONE FOLDER &middot; OPEN ANY CARD</div>
</div>

<script>
var A=@@A@@,GN=@@GN@@,GD=@@GD@@,GC=@@GC@@,GK=@@GK@@;
var act=-1;
function esc(s){return (s||"").replace(/</g,"&lt;");}
function tabs(){
  var h="<button class='tb"+(act===-1?" on":"")+"' onclick='setG(-1)'>ALL</button>";
  for(var i=0;i<GN.length;i++){
    h+="<button class='tb"+(act===i?" on":"")+"' style='--cc:"+GC[i]+"' title='"+esc(GN[i])+"' onclick='setG("+i+")'>"+GK[i]+"</button>";
  }
  document.getElementById("tabs").innerHTML=h;
}
function setG(i){act=i;tabs();render();}
function render(){
  var q=document.getElementById("q").value.toLowerCase().trim();
  var h="",shown=0;
  for(var gi=0;gi<GN.length;gi++){
    if(act!==-1&&act!==gi)continue;
    var rows="",n=0;
    for(var j=0;j<A.length;j++){
      var a=A[j];
      if(a.gi!==gi)continue;
      if(q){
        var hay=(a.cn+" "+a.t+" "+a.f+" "+a.sm+" "+a.p.join(" ")+" "+a.g).toLowerCase();
        if(hay.indexOf(q)===-1)continue;
      }
      shown++;n++;
      var sup=a.s.indexOf("Superseded")===0;
      var pts="";
      for(var k=0;k<a.p.length;k++)pts+="<span class='pt'>"+esc(a.p[k])+"</span>";
      rows+="<a class='card"+(sup?" sup":"")+"' href='"+a.f+"' target='_blank' style='--cc:"+a.c+"'>"+
       "<span class='tab'>"+a.cn+"</span>"+
       (sup?"<span class='stamp'>SUPERSEDED</span>":"")+
       "<div class='c-meta'><span class='dot'></span><span>"+esc(a.f)+"</span><span>"+esc(a.d)+"</span><span>"+esc(a.s)+"</span></div>"+
       "<div class='c-t'>"+esc(a.t)+"</div>"+
       "<div class='c-sm'>"+esc(a.sm)+"</div>"+
       (pts?"<div class='pts'>"+pts+"</div>":"")+"</a>";
    }
    if(!rows)continue;
    h+="<div class='grp'><div class='grp-h' style='--gc:"+GC[gi]+"'>"+
     "<span class='grp-k'>"+GK[gi]+"</span>"+
     "<span class='grp-t'>"+esc(GN[gi])+"</span>"+
     "<span class='grp-n'>"+n+" WORK"+(n===1?"":"S")+"</span></div>"+
     "<div class='grp-d'>"+esc(GD[gi])+"</div>"+
     "<div class='cards'>"+rows+"</div></div>";
  }
  document.getElementById("out").innerHTML=shown?h:"<div class='none'>Nothing on this shelf matches. Try a shorter word.</div>";
}
tabs();render();
</script></body></html>
"""

out = (TPL.replace('@@STATS@@', stats)
          .replace('@@A@@', js(A))
          .replace('@@GN@@', js(GN))
          .replace('@@GD@@', js(GD))
          .replace('@@GC@@', js(GC))
          .replace('@@GK@@', js(GK)))

open('/home/claude/library/INDEX.html', 'w', encoding='utf-8').write(out)
print("written", len(out), "bytes")
