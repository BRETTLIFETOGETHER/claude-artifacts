/* browse.html — 16k rows, virtualized, faceted, instant search, URL-stateful */
(function(){
"use strict";
const A=window.App,D=A.D,ROWS=A.ROWS,N=ROWS.length;
const $=s=>document.querySelector(s);
const AFF=D.aff,SEA=D.seasons;
const FMTS=[["7-Day",1],["21-Day",2],["30-Day",4],["40-Day",8],["6-Session Study",16],["Catalytic Sunday",32]];
const COLL=[["Flagship",1],["Seasonal",2],["New",4],["Pastor's Shelf",8]];
const GRADES=["AA","A","B"];
/* ---------- search index */
const tokRe=/[a-z0-9']+/g;
const inv=new Map();
function tokensOf(o){const src=(o.t+" "+(o.s||"")+" "+A.themeLabel(o.th)+" "+A.chLabel(o.ch)+" "+A.refOf(o)).toLowerCase();
 return src.match(tokRe)||[]}
ROWS.forEach((o,i)=>{new Set(tokensOf(o)).forEach(t=>{let a=inv.get(t);if(!a)inv.set(t,a=[]);a.push(i)})});
const KEYS=[...inv.keys()].sort();
function idsForPrefix(p){const out=[];let lo=0,hi=KEYS.length;
 while(lo<hi){const m=(lo+hi)>>1;KEYS[m]<p?lo=m+1:hi=m}
 for(let i=lo;i<KEYS.length&&KEYS[i].startsWith(p);i++)out.push(...inv.get(KEYS[i]));
 return out}
function searchIds(q){const ts=(q.toLowerCase().match(tokRe)||[]).filter(t=>t.length>1);
 if(!ts.length)return null;
 let set=null;
 for(const t of ts){const ids=idsForPrefix(t);const s=new Set(ids);
  set=set?new Set([...set].filter(i=>s.has(i))):s;
  if(!set.size)break}
 return set||new Set()}
/* ---------- state */
const S={ch:new Set(),fmt:0,aff:0,coll:0,se:new Set(),g:new Set(),q:"",sort:"rel"};
function parseURL(){const p=new URLSearchParams(location.search);
 (p.get("ch")||"").split(",").filter(Boolean).forEach(x=>S.ch.add(+x));
 S.fmt=+(p.get("f")||0);S.aff=+(p.get("a")||0);S.coll=+(p.get("c")||0);
 (p.get("se")||"").split(",").filter(Boolean).forEach(x=>S.se.add(+x));
 (p.get("g")||"").split(",").filter(Boolean).forEach(x=>S.g.add(x));
 S.q=p.get("q")||"";S.sort=p.get("s")||"rel"}
function pushURL(){const p=new URLSearchParams();
 if(S.ch.size)p.set("ch",[...S.ch].join(","));if(S.fmt)p.set("f",S.fmt);
 if(S.aff)p.set("a",S.aff);if(S.coll)p.set("c",S.coll);
 if(S.se.size)p.set("se",[...S.se].join(","));if(S.g.size)p.set("g",[...S.g].join(","));
 if(S.q)p.set("q",S.q);if(S.sort!=="rel")p.set("s",S.sort);
 history.replaceState(null,"", location.pathname+(p.toString()?"?"+p:""))}
/* ---------- filtering */
let CUR=[];
function apply(){
 const qset=S.q?searchIds(S.q):null;
 CUR=[];
 for(let i=0;i<N;i++){const o=ROWS[i];
  if(qset&&!qset.has(i))continue;
  if(S.ch.size&&!S.ch.has(o.ch))continue;
  if(S.fmt&&!(o.f&S.fmt))continue;
  if(S.aff&&!(o.af&S.aff))continue;
  if(S.coll&&!(o.co&S.coll))continue;
  if(S.se.size&&!S.se.has(o.se))continue;
  if(S.g.size&&!S.g.has(o.g))continue;
  CUR.push(i)}
 sortCur();counts();renderMeta();V.reset();pushURL()}
function sortCur(){const s=S.sort;
 const key={rel:i=>-( (ROWS[i].co&1?4:0)+(ROWS[i].g==="AA"?3:ROWS[i].g==="A"?2:0)+(ROWS[i].co&4?1:0) ),
  pop:i=>-( (ROWS[i].g==="AA"?4:ROWS[i].g==="A"?3:ROWS[i].g==="B"?2:1)+(ROWS[i].co&1?2:0) ),
  new:i=>-( (ROWS[i].co&4?1e6:0)+parseInt(ROWS[i].id.slice(2)) ),
  az:null, len:null}[s];
 if(s==="az")CUR.sort((a,b)=>ROWS[a].t.localeCompare(ROWS[b].t));
 else if(s==="len"){const L=o=>o.f&8?40:o.f&4?30:o.f&2?21:o.f&1?7:o.f&16?6:1;CUR.sort((a,b)=>L(ROWS[b])-L(ROWS[a]))}
 else CUR.sort((a,b)=>key(a)-key(b)||ROWS[a].t.localeCompare(ROWS[b].t))}
/* ---------- facet counts */
function counts(){
 const cCh=new Array(D.channels.length).fill(0),cF={},cA=new Array(12).fill(0),cC={},cS={},cG={};
 for(const i of CUR){const o=ROWS[i];cCh[o.ch]++;
  FMTS.forEach(([n,b])=>{if(o.f&b)cF[n]=(cF[n]||0)+1});
  for(let k=0;k<12;k++)if(o.af&(1<<k))cA[k]++;
  COLL.forEach(([n,b])=>{if(o.co&b)cC[n]=(cC[n]||0)+1});
  if(o.se>=0)cS[o.se]=(cS[o.se]||0)+1;
  cG[o.g]=(cG[o.g]||0)+1}
 document.querySelectorAll("[data-cnt]").forEach(el=>{
  const[k,v]=el.getAttribute("data-cnt").split(":");
  const n=k==="ch"?cCh[+v]:k==="f"?cF[v]||0:k==="a"?cA[+v]:k==="c"?cC[v]||0:k==="se"?cS[+v]||0:cG[v]||0;
  el.textContent=n.toLocaleString()})}
/* ---------- virtual list */
const V={cols:1,rowH:392,pad:3,mounted:new Map(),
 reset(){this.mounted.forEach(el=>el.remove());this.mounted.clear();this.measure();this.paint(true)},
 measure(){const w=$("#vlist").clientWidth;this.cols=Math.max(1,Math.floor((w+18)/214));
  $("#vlist").style.height=Math.ceil(CUR.length/this.cols)*this.rowH+"px"},
 paint(force){const st=window.scrollY-$("#vlist").getBoundingClientRect().top-window.scrollY- -0; // top offset
  const top=$("#vlist").offsetTop, y=Math.max(0,window.scrollY-top);
  const r0=Math.max(0,Math.floor(y/this.rowH)-this.pad),
        r1=Math.min(Math.ceil(CUR.length/this.cols),Math.ceil((y+innerHeight)/this.rowH)+this.pad);
  for(const[r,el]of this.mounted)if(r<r0||r>=r1){el.remove();this.mounted.delete(r)}
  for(let r=r0;r<r1;r++){if(this.mounted.has(r))continue;
   const div=document.createElement("div");div.className="vrow";div.style.top=r*this.rowH+"px";
   let html="";for(let c=0;c<this.cols;c++){const idx=CUR[r*this.cols+c];if(idx==null)break;html+=A.cardHTML(ROWS[idx])}
   div.innerHTML=html;$("#vlist").appendChild(div);A.paintCovers(div);this.mounted.set(r,div)}}};
addEventListener("scroll",()=>V.paint(),{passive:true});
addEventListener("resize",()=>{V.measure();V.mounted.forEach(el=>el.remove());V.mounted.clear();V.paint()});
/* ---------- meta + empty state */
function renderMeta(){$("#rescount").textContent=CUR.length.toLocaleString()+" campaigns";
 const chips=[];S.ch.forEach(c=>chips.push(["ch",c,A.chLabel(c)]));
 FMTS.forEach(([n,b])=>{if(S.fmt&b)chips.push(["f",b,n])});
 AFF.forEach((n,i)=>{if(S.aff&(1<<i))chips.push(["a",i,n])});
 COLL.forEach(([n,b])=>{if(S.coll&b)chips.push(["c",b,n])});
 S.se.forEach(s=>chips.push(["se",s,SEA[s]]));S.g.forEach(g=>chips.push(["g",g,"Grade "+g]));
 $("#activef").innerHTML=chips.map(([k,v,n])=>`<button class="fchip" data-rm="${k}:${v}">${A.escapeH(n)} ✕</button>`).join("");
 const empty=$("#empty");
 if(!CUR.length){empty.classList.remove("hide");
  const near=nearest();$("#nearby").innerHTML=near.map(i=>A.cardHTML(ROWS[i])).join("");A.paintCovers($("#nearby"))}
 else empty.classList.add("hide")}
function nearest(){const t={...S};const relax=[()=>S.g.clear(),()=>S.se.clear(),()=>S.coll=0,()=>S.aff=0,()=>S.fmt=0,()=>S.q="",()=>S.ch.clear()];
 for(const r of relax){r();const q=S.q?searchIds(S.q):null;const out=[];
  for(let i=0;i<N&&out.length<3;i++){const o=ROWS[i];
   if(q&&!q.has(i))continue;if(S.ch.size&&!S.ch.has(o.ch))continue;if(S.fmt&&!(o.f&S.fmt))continue;
   if(S.aff&&!(o.af&S.aff))continue;if(S.coll&&!(o.co&S.coll))continue;
   if(S.se.size&&!S.se.has(o.se))continue;if(S.g.size&&!S.g.has(o.g))continue;out.push(i)}
  if(out.length){Object.assign(S,{ch:t.ch,fmt:t.fmt,aff:t.aff,coll:t.coll,se:t.se,g:t.g,q:t.q});return out}}
 Object.assign(S,t);return[0,1,2]}
/* ---------- rail build */
function rail(){
 const g=(title,items)=>`<h4>${title}</h4>`+items.join("");
 let h="";
 h+=g("Channel",D.channels.map((c,i)=>lab(`ch:${i}`,c.name,S.ch.has(i))));
 h+=g("Format",FMTS.map(([n,b])=>lab(`f:${b}`,n,S.fmt&b)));
 h+=g("Affinity",AFF.map((n,i)=>lab(`a:${i}`,n,S.aff&(1<<i))));
 h+=g("Collection",COLL.map(([n,b])=>lab(`c:${b}`,n,S.coll&b)));
 h+=g("Season",SEA.map((n,i)=>lab(`se:${i}`,n,S.se.has(i))));
 h+=g("Priority grade",GRADES.map(gr=>lab(`g:${gr}`,"Grade "+gr,S.g.has(gr))));
 $("#railbody").innerHTML=h;
 function lab(key,name,on){const[k,v]=key.split(":");
  return `<label><input type="checkbox" data-k="${key}" ${on?"checked":""}> ${A.escapeH(name)} <span class="cnt" data-cnt="${key}"></span></label>`}}
document.addEventListener("change",e=>{const el=e.target.closest("[data-k]");if(!el)return;
 const[k,v]=el.getAttribute("data-k").split(":");toggle(k,v,el.checked);apply()});
document.addEventListener("click",e=>{const rm=e.target.closest("[data-rm]");if(rm){const[k,v]=rm.getAttribute("data-rm").split(":");toggle(k,v,false);rail();apply()}
 if(e.target.id==="clearall"){Object.assign(S,{ch:new Set(),fmt:0,aff:0,coll:0,se:new Set(),g:new Set(),q:""});$("#q").value="";rail();apply()}
 if(e.target.id==="mfilters")$(".rail").classList.toggle("open")});
function toggle(k,v,on){
 if(k==="ch"){on?S.ch.add(+v):S.ch.delete(+v)}
 else if(k==="f"){S.fmt=on?S.fmt|+v:S.fmt&~+v}
 else if(k==="a"){S.aff=on?S.aff|(1<<+v):S.aff&~(1<<+v)}
 else if(k==="c"){S.coll=on?S.coll|+v:S.coll&~+v}
 else if(k==="se"){on?S.se.add(+v):S.se.delete(+v)}
 else if(k==="g"){on?S.g.add(v):S.g.delete(v)}}
/* ---------- boot */
let deb;$("#q").addEventListener("input",e=>{clearTimeout(deb);deb=setTimeout(()=>{S.q=e.target.value.trim();apply()},120)});
$("#sort").addEventListener("change",e=>{S.sort=e.target.value;sortCur();V.reset();pushURL()});
parseURL();$("#q").value=S.q;$("#sort").value=S.sort;rail();
const t0=performance.now();apply();
$("#perf").textContent=`Indexed ${N.toLocaleString()} campaigns in ${Math.round(performance.now()-t0)}ms`;
})();
