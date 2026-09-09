/* The Campaign Discernment Guide — Brett's instrument pattern for the church.
   Six dimensions × four statements (scored /120), season, congregation, felt needs,
   one discernment sentence. Low dimensions set direction; direction sets the matches. */
(function(){
"use strict";
const A=window.App, F=window.FIN, $=s=>document.querySelector(s);
if(!$("#finder")||!F) return;

/* dimension → channels (primary first) and felt-need → channels */
const DIM_CH=[[20,3,19],[2,1],[9,11,21,22],[4,5],[7,8,6]],SENT_CH=[17,16,14,15,13];
DIM_CH.push(SENT_CH);
const FELT_CH={marriage:[7],money:[4,5],anx:[9,3],grief:[9,10],teens:[8,22],doubt:[21,22],lonely:[2,1],serve:[16,17]};
const TOTAL_ITEMS=24+1+3+1+1;   /* statements + season + church(3) + felt + outcome-format */

const ans={l:Array(24).fill(0),se:null,size:null,groups:null,hist:null,felt:[],out:"",fmt:"auto"};
let scr=0;   /* 0 intro · 1–6 dims · 7 season · 8 church · 9 felt · 10 outcome · 11 results */

function answered(){let n=ans.l.filter(Boolean).length;
 if(ans.se!==null)n++;if(ans.size)n++;if(ans.groups)n++;if(ans.hist)n++;
 if(ans.felt.length)n++;if(ans.fmt)n++;return n}
function progress(){const p=Math.round(100*answered()/TOTAL_ITEMS);
 const el=$("#finprog i");if(el)el.style.width=p+"%"}

function likert(name,val){return `<div class="likert" data-l="${name}">`+
 [1,2,3,4,5].map(v=>`<label class="lk${val===v?" on":""}"><input type="radio" name="${name}" value="${v}"${val===v?" checked":""}><span>${v}</span></label>`).join("")+`</div>`}
function radios(name,opts,val){return opts.map(([t,v])=>
 `<label class="qopt${val===v?" on":""}"><input type="radio" name="${name}" value="${v}"${val===v?" checked":""}>${t}</label>`).join("")}

function screenHTML(){
 if(scr===0)return `<div class="fin-intro">
  <p class="eyebrow" style="justify-content:center">${F.intro_meta}</p>
  <h2 style="text-align:center;margin:14px 0 10px">${F.intro_h}</h2>
  <p class="prose" style="max-width:60ch;margin:0 auto;text-align:center">${F.intro_p}</p>
  <div style="text-align:center;margin-top:24px"><button class="btn gold" id="fnext">${F.begin}</button></div></div>`;
 if(scr>=1&&scr<=6){const d=F.dims[scr-1];
  return `<p class="eyebrow">${scr} / 6 · ${F.h1}</p>
  <h2 style="margin:8px 0 4px">${d.t}</h2><p class="lede" style="margin:0 0 6px">${d.s}</p>
  <div class="scalekey"><span>${F.scale[0]}</span><span>${F.scale[4]}</span></div>
  ${d.st.map((s,i)=>`<div class="stmt"><p>${s}</p>${likert("s"+(scr-1)+"_"+i,ans.l[(scr-1)*4+i])}</div>`).join("")}`;
 }
 if(scr===7)return head(F.season)+`<div class="optcol">${radios("se",F.season.opts,ans.se)}</div>`;
 if(scr===8){const c=F.church;
  return head(c)+["size","groups","hist"].map(k=>
   `<h4 style="margin:16px 0 8px">${c[k].q}</h4><div class="optrow">${radios(k,c[k].opts,ans[k])}</div>`).join("")}
 if(scr===9)return head(F.felt)+`<div class="optcol">`+F.felt.opts.map(([t,v])=>
   `<label class="qopt${ans.felt.includes(v)?" on":""}"><input type="checkbox" name="felt" value="${v}"${ans.felt.includes(v)?" checked":""}>${t}</label>`).join("")+`</div>`;
 if(scr===10){const o=F.outcome;
  return head(o)+`<p class="lede" style="font-size:17px;margin:6px 0 8px">${o.lead}</p>
  <textarea id="fout" rows="3" placeholder="${o.ph.replace(/"/g,"&quot;")}" style="width:100%">${ans.out}</textarea>
  <h4 style="margin:18px 0 8px">${o.fmt_q}</h4><div class="optrow">${radios("fmt",o.fmt_opts,ans.fmt)}</div>`;
 }
 function head(x){return `<p class="eyebrow">${F.h1}</p><h2 style="margin:8px 0 4px">${x.t}</h2><p class="lede" style="margin:0 0 12px">${x.s}</p>`}
 return "";
}
function canNext(){
 if(scr===0)return true;
 if(scr>=1&&scr<=6){for(let i=0;i<4;i++)if(!ans.l[(scr-1)*4+i])return false;return true}
 if(scr===7)return ans.se!==null;
 if(scr===8)return ans.size&&ans.groups&&ans.hist;
 if(scr===9)return ans.felt.length>=1;
 if(scr===10)return !!ans.fmt;
 return true}
function render(){
 $("#fbody").innerHTML=screenHTML();
 if(scr>0)$("#fbody").insertAdjacentHTML("beforeend",
  `<div style="display:flex;gap:12px;margin-top:22px">
   <button class="btn ghost" id="fback">${F.back}</button>
   <button class="btn primary" id="fnext" ${canNext()?"":"disabled"}>${scr===10?F.see:F.next}</button></div>`);
 progress();window.scrollTo({top:0,behavior:"smooth"})}

document.addEventListener("change",e=>{
 const t=e.target;if(!t.name)return;
 if(/^s\d+_\d+$/.test(t.name)){const[,d,i]=t.name.match(/^s(\d+)_(\d+)$/);
  ans.l[+d*4+ +i]=+t.value;
  t.closest(".likert").querySelectorAll(".lk").forEach(l=>l.classList.remove("on"));
  t.closest(".lk").classList.add("on")}
 else if(t.name==="se")ans.se=t.value;
 else if(t.name==="felt"){
  if(t.checked&&ans.felt.length>=F.felt.cap){t.checked=false;return}
  ans.felt=[...document.querySelectorAll('input[name=felt]:checked')].map(x=>x.value);
  t.closest(".qopt").classList.toggle("on",t.checked)}
 else if(["size","groups","hist","fmt"].includes(t.name))ans[t.name]=t.value;
 if(t.type==="radio"&&t.name!=="felt"&&!/^s\d/.test(t.name)){
  t.closest(".optrow,.optcol")?.querySelectorAll(".qopt").forEach(l=>l.classList.remove("on"));
  t.closest(".qopt")?.classList.add("on")}
 const n=$("#fnext");if(n)n.disabled=!canNext();progress()});
document.addEventListener("input",e=>{if(e.target.id==="fout")ans.out=e.target.value});
document.addEventListener("click",e=>{
 if(e.target.id==="fnext"&&!e.target.disabled){scr++;scr<=10?render():results()}
 if(e.target.id==="fback"){scr--;render()}
 if(e.target.id==="fagain"){location.reload()}
 if(e.target.id==="fprint")window.print()});

/* ------------------------------ results ------------------------------ */
function band(sc){for(const[max,label,line]of F.res.bands)if(sc<=max)return[label,line];return["",""]}
function results(){
 const dims=F.dims.map((d,i)=>{const s=ans.l.slice(i*4,i*4+4).reduce((a,b)=>a+b,0);return{i,t:d.t,s}});
 const total=dims.reduce((a,d)=>a+d.s,0);
 const low=[...dims].sort((a,b)=>a.s-b.s).slice(0,2);
 /* channel weights */
 const chW=new Array(23).fill(0),chDim=new Array(23).fill(-1);
 dims.forEach(d=>{const need=(20-d.s);DIM_CH[d.i].forEach((ch,k)=>{
  const w=need*(k===0?.35:.2);if(w>chW[ch]){}chW[ch]+=w;if(low.some(l=>l.i===d.i))chDim[ch]=d.i})});
 ans.felt.forEach(f=>FELT_CH[f].forEach((ch,k)=>chW[ch]+=k===0?4:2.5));
 const se=+ans.se;
 /* recommended format */
 let fmt=ans.fmt;
 if(fmt==="auto")fmt=(ans.hist==="first"||ans.groups==="none")?"21":(ans.hist==="rhythm"&&ans.groups==="strong")?"40":"30";
 const fmtBit={sunday:32,"21":2,"30":4,"40":8}[fmt];
 /* score catalog */
 const why=new Map();
 const scored=A.ROWS.map((o,i)=>{let s=chW[o.ch]||0;const w=[];
  if(chDim[o.ch]>=0)w.push(F.res.why.dim.replace("{d}",F.dims[chDim[o.ch]].t));
  const f=ans.felt.find(x=>FELT_CH[x][0]===o.ch||FELT_CH[x][1]===o.ch);
  if(f)w.push(F.res.why.felt[f]);
  if(se>=0&&o.se===se){s+=3;w.push(F.res.why.season)}
  if(o.f&fmtBit)s+=1.5;
  if(o.co&1){s+=2;w.push(F.res.why.flag)}
  if(o.g==="AA")s+=1.5;else if(o.g==="A")s+=1;
  why.set(o.id,w);return[s,i]}).sort((a,b)=>b[0]-a[0]);
 const picks=[],seen=new Set();
 for(const[,i]of scored){const o=A.ROWS[i];if(seen.has(o.ch))continue;picks.push(o);seen.add(o.ch);if(picks.length===4)break}
 const boosted=new Set();DIM_CH.forEach((chs,i)=>{if(low.some(l=>l.i===i))chs.forEach(c=>boosted.add(c))});
 ans.felt.forEach(f=>FELT_CH[f].forEach(c=>boosted.add(c)));
 const wild=scored.map(([,i])=>A.ROWS[i]).find(o=>!seen.has(o.ch)&&!boosted.has(o.ch)&&(o.co&1));
 /* render */
 const seLabel=se>=0?(F.season.opts.find(([,v])=>+v===se)||[""])[0]:"";
 $("#fwiz").classList.add("hide");
 $("#fresults").classList.remove("hide");
 $("#fprofile").innerHTML=`
  <div class="fin-score"><b>${total}</b><span>${F.res.total_l}</span></div>
  <div class="dimgrid">${dims.map(d=>{const[bl]=band(d.s);return `
   <div class="dimrow"><div class="dimhead"><span>${d.t}</span><em>${d.s} / 20 · ${bl}</em></div>
   <div class="dimbar"><i style="width:${d.s*5}%"></i></div></div>`}).join("")}</div>
  <p class="prose" style="margin-top:14px">${F.res.low_line}</p>
  <div class="big-q">${band(low[0].s)[1]} ${band(low[1].s)[1]}<small>${low[0].t} · ${low[1].t}</small></div>
  ${ans.out.trim()?`<div class="big-q">${F.res.outcome_pre} “${esc(ans.out.trim())}”<small>${F.res.outcome_post}</small></div>`:""}
  <h3 style="margin-top:26px">${F.res.fmt_h}</h3>
  <p class="prose">${F.res.fmt_line[fmt]}${seLabel?` — ${F.res.season_pre} <b>${seLabel}</b>.`:""}</p>`;
 $("#fpicks").innerHTML=picks.map(o=>A.cardHTML(o)+
  `<div class="whyrow">${(why.get(o.id)||[]).slice(0,3).map(w=>`<span class="whychip">${w}</span>`).join("")}</div>`).join("");
 if(wild)$("#fwild").innerHTML=A.cardHTML(wild)+`<p class="prose" style="margin:8px 0 0">${(why.get(wild.id)||[]).slice(0,2).join(" · ")}</p>`;
 A.paintCovers($("#fresults"));
 $("#finprog i").style.width="100%";window.scrollTo({top:0,behavior:"smooth"})}
function esc(s){return s.replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/"/g,"&quot;")}
render();
})();
