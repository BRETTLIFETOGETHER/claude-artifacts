/* campaign.html?id=M-xxxxx — complete detail, every day fully written by the engine. */
(function(){
"use strict";
const A=window.App,D=A.D,E=window.Engine,$=s=>document.querySelector(s);
const LBL=window.PAGE_LBL||{};
const id=new URLSearchParams(location.search).get("id");
const o=A.BYID.get(id)||A.ROWS[0];
const rng=A.mulberry(parseInt(o.fp,16)||7);
const POOL=window.SPOOLS[o.ch].map(i=>D.refs[i]);
function pick(arr,n){const a=[...arr];const out=[];while(out.length<n&&a.length)out.push(a.splice(Math.floor(rng()*a.length),1)[0]);return out}

document.title=o.t+" — 40 Day Campaigns";
$("#crumb").innerHTML=`<a href="index.html">Home</a> / <a href="channel.html?c=${o.ch}">${A.escapeH(A.chLabel(o.ch))}</a> / <a href="theme.html?t=${o.th}">${A.escapeH(A.themeLabel(o.th))}</a>`;
$("#cover").innerHTML=window.Covers.svg(o);
$("#title").textContent=o.t;
$("#subtitle").textContent=o.s||"";
$("#ref").textContent=A.refOf(o);
if(o.co&1)$("#flag").classList.remove("hide");

const fmts=A.fmtsOf(o);let curF=fmts[0];
$("#fmts").innerHTML=fmts.map((f,i)=>`<button class="fmt-opt ${i?"":"on"}" data-f="${f.key}">${f.name}</button>`).join("");
function setPrice(){$("#price").innerHTML=A.money(A.price(o,curF.key))+` <small>${LBL.perchurch||"per church · all four editions included"}${o.g==="AA"||o.g==="A"?` · Grade ${o.g}`:""}</small>`;
 $("#addbig").setAttribute("data-fmt",curF.key)}
document.addEventListener("click",e=>{const b=e.target.closest(".fmt-opt");if(!b)return;
 document.querySelectorAll(".fmt-opt").forEach(x=>x.classList.remove("on"));b.classList.add("on");
 curF=fmts.find(f=>f.key===b.getAttribute("data-f"));setPrice();renderBody()});
$("#addbig").setAttribute("data-add",o.id);setPrice();

A.loadShard(o.ch,sh=>{const rec=sh.rows.find(r=>r.id===o.id);if(!rec)return;
 $("#promise").textContent=rec.sum||"";
 if(rec.aud)$("#aud").innerHTML=`<b>${LBL.best_for||"Best for"}:</b> ${A.escapeH(rec.aud)}`;
 if(rec.fn)$("#felt").innerHTML=`<b>${LBL.felt||"Felt need"}:</b> ${A.escapeH(rec.fn)}`;
 if(rec.nest)renderNest(rec.nest)});
function renderNest(n){const el=$("#nest");el.classList.remove("hide");let h="";
 if(n.sessions&&n.sessions.length){h+=`<h3>${LBL.in_series||"The six sessions in this series"}</h3><div class="grid g2">`+
  n.sessions.map((s,i)=>`<div class="edbox"><h4>Session ${i+1} · ${A.escapeH(s.t)}</h4>${s.s?`<p class="muted">${A.escapeH(s.s)}</p>`:""}</div>`).join("")+`</div>`}
 if(n.devotional&&n.devotional.length){h+=`<h3 style="margin-top:28px">${LBL.dev_along||"The 40-day devotional that runs alongside"}</h3><div class="arc">`+
  n.devotional.map((d,i)=>`<div class="day"><b>Day ${i+1} — ${A.escapeH(d.t)}</b><span>${A.escapeH(d.w||"")}</span></div>`).join("")+`</div>`}
 el.querySelector(".inner").innerHTML=h}

/* -------- format-aware body -------- */
function daysOf(){return curF.key==="year"?12:(curF.days||curF.sess||1)}
function sessOf(){return curF.key==="year"?12:(curF.sess||1)}
let DAYS=[];
function renderBody(){
 const resource=curF.key==="resource";
 $("#arcsec").classList.toggle("hide",resource);
 $("#sermsec").classList.toggle("hide",resource||curF.key==="year");
 $("#sesssec").classList.toggle("hide",resource);
 $("#ressec").classList.toggle("hide",!resource);
 if(resource){renderResource();return}
 arc();sermons();sessions()}
function arc(){const n=daysOf();DAYS=[];const el=$("#arc");
 let h="";
 for(let i=0;i<n;i++){const d=E.day(o,curF.key,i,n);DAYS.push(d);
  h+=`<button class="day${d.sunday?" sun":""}" data-day="${i}" style="text-align:left;cursor:pointer;font-family:inherit">
   <b>${d.unit} ${d.n} · ${A.escapeH(d.word)}</b><span>${d.ref}</span></button>`}
 el.innerHTML=h;
 $("#archead").textContent=(curF.key==="study"?(LBL.arc_sess||"The session arc"):curF.key==="year"?(LBL.arc_year||"Twelve monthly milestones"):`${LBL.arc_pre||"The"} ${n}${LBL.arc_post||"-day arc — every day fully written: Scripture, devotional, step, and prayer"}`);
 $("#dlrow").classList.remove("hide")}
function sermons(){const n=curF.key==="sunday"?1:sessOf();const el=$("#sermons");
 let h="";for(let w=0;w<Math.min(n,6);w++)h+=E.sermonHTML(E.sermon(o,w),LBL);
 el.innerHTML=h}
function sessions(){const n=curF.key==="sunday"?1:Math.min(sessOf(),6);
 let h="";for(let w=0;w<n;w++)h+=E.sessionHTML(E.session(o,w),LBL);
 $("#sess").innerHTML=h}
function renderResource(){
 const c=E.banks[o.ch];const s=A.mulberry(parseInt(o.fp,16)||7);
 $("#resbody").innerHTML=`<div class="grid g2">
  <div class="edbox"><h4>${LBL.res_inside||"What's inside"}</h4><ul>
   <li>${LBL.res_1||"Presenter deck & speaker notes"}</li><li>${LBL.res_2||"Participant handout (print & digital)"}</li>
   <li>${LBL.res_3||"Promotion kit: email, slide, social copy"}</li><li>${LBL.res_4||"Follow-up next-step pathway into a full campaign"}</li></ul></div>
  <div class="edbox"><h4>${LBL.res_use||"How churches use it"}</h4><p style="margin:0">${A.escapeH(c.p[Math.floor(s()*c.p.length)][0].toUpperCase()+c.p[Math.floor(s()*c.p.length)].slice(1))}. ${LBL.res_use_p||"Run it as a stand-alone evening, a staff training, or the on-ramp Sunday before a full 40/30/21/7-day launch on the same theme."}</p></div></div>`}

/* -------- day modal -------- */
function openDay(i){const d=DAYS[i]||E.day(o,curF.key,i,daysOf());
 $("#modal .inner").innerHTML=E.dayHTML(d,o,LBL);
 $("#modal").dataset.day=i;$("#modal").classList.remove("hide")}
document.addEventListener("click",e=>{
 const dbtn=e.target.closest("[data-day]");if(dbtn&&!e.target.closest("#modal")){openDay(+dbtn.getAttribute("data-day"))}
 if(e.target.id==="modal"||e.target.closest(".mclose"))$("#modal").classList.add("hide");
 if(e.target.id==="prevday"||e.target.id==="nextday"){const i=+$("#modal").dataset.day+(e.target.id==="nextday"?1:-1);
  if(i>=0&&i<daysOf())openDay(i)}});
$("#preview").addEventListener("click",()=>openDay(0));
$("#printday").addEventListener("click",()=>{const i=+($("#modal").dataset.day||0);
 const d=DAYS[i]||E.day(o,curF.key,i,daysOf());
 const w=window.open("","_blank");
 w.document.write(E.docWrap(`${o.t} — ${d.unit} ${d.n}`,`<h2>${A.escapeH(d.word)}</h2><p><i>${A.escapeH(d.read)}</i></p><p>${A.escapeH(d.open)}</p><p>${A.escapeH(d.truth)}</p><p>${A.escapeH(d.turn)}</p><p><b>Step.</b> ${A.escapeH(d.step)}</p><p><b>Reflect.</b> ${A.escapeH(d.q)}</p><p><b>Pray.</b> ${A.escapeH(d.pray)}</p>`));
 w.document.close();w.focus();w.print()});
$("#worddoc").addEventListener("click",()=>{const i=+($("#modal").dataset.day||0);
 const d=DAYS[i]||E.day(o,curF.key,i,daysOf());
 E.download(`${o.slug}-day-${d.n}.doc`,E.docWrap(`${o.t} — ${d.unit} ${d.n}`,$("#modal .inner").innerHTML))});
$("#canva").addEventListener("click",()=>window.open("https://www.canva.com/create/","_blank","noopener"));

/* -------- full-document downloads -------- */
$("#dl-dev").addEventListener("click",()=>E.download(`${o.slug}-devotional.doc`,E.fullDevotional(o,curF.key,daysOf())));
$("#dl-ser").addEventListener("click",()=>E.download(`${o.slug}-sermon-builds.doc`,E.fullSermons(o,curF.key==="sunday"?1:sessOf())));
$("#dl-grp").addEventListener("click",()=>E.download(`${o.slug}-group-guide.doc`,E.fullGroup(o,curF.key==="sunday"?1:Math.min(sessOf(),6))));

/* related */
(function(){const rel=A.ROWS.filter(r=>r.th===o.th&&r.id!==o.id).slice(0,10);
 if(!rel.length)return;$("#relrow").innerHTML=rel.map(r=>A.cardHTML(r)).join("");A.paintCovers($("#relrow"))})();
renderBody();A.paintCovers(document);
})();
