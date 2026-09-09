/* finder / builder / cart+checkout+confirmation / account — page detects which blocks exist */
(function(){
"use strict";
const A=window.App,D=A.D,$=s=>document.querySelector(s);
/* =============================== FINDER =============================== */
if($("#finder")){
const QS=[
 {q:"How large is your weekend attendance?",k:"size",opts:[["Under 200","s"],["200–800","m"],["800–2,500","l"],["2,500+","xl"]]},
 {q:"How many weeks can you give this on the preaching calendar?",k:"weeks",opts:[["One big Sunday","sunday"],["Three weeks","21"],["Four to five weeks","30"],["Six weeks — we're all in","40"]]},
 {q:"What is the primary goal of this season?",k:"goal",opts:[["Spiritual formation & depth","form"],["Get people into groups","groups"],["Reach new people","reach"],["Generosity & vision","gen"],["Care for hurting people","care"]]},
 {q:"What season will you launch in?",k:"season",opts:[["New Year","2"],["Lent / Easter","3"],["Back to school / Fall","9"],["Advent / Christmas","0"],["Summer","8"],["No particular season","-1"]]},
 {q:"What is your congregation feeling most right now?",k:"felt",opts:[["Anxious & tired","anx"],["Disconnected","disc"],["Financial pressure","money"],["Questions & doubt","doubt"],["Ready to grow","grow"]]},
 {q:"Are you ready to run youth & children's editions alongside adults?",k:"eds",opts:[["Yes — whole church","yes"],["Adults first, kids later","later"]]},
 {q:"Budget comfort for a churchwide campaign?",k:"budget",opts:[["Keep it lean","lean"],["Standard","std"],["Invest for maximum impact","max"]]},
];
let qi=0;const ans={};
function renderQ(){const q=QS[qi];
 $("#finder .progress i").style.width=(qi/QS.length*100)+"%";
 $("#qbody").innerHTML=`<h3>${q.q}</h3>`+q.opts.map(([t,v])=>`<label class="qopt"><input type="radio" name="q" value="${v}">${t}</label>`).join("")+
 `<div style="display:flex;gap:12px;margin-top:16px">${qi?'<button class="btn ghost" id="back">Back</button>':""}<button class="btn primary" id="next" disabled>${qi===QS.length-1?"See my campaigns":"Next"}</button></div>`;
 document.querySelectorAll('input[name=q]').forEach(r=>r.addEventListener("change",e=>{$("#next").disabled=false;
  document.querySelectorAll(".qopt").forEach(l=>l.classList.remove("on"));e.target.closest(".qopt").classList.add("on")}))}
document.addEventListener("click",e=>{
 if(e.target.id==="next"){ans[QS[qi].k]=document.querySelector('input[name=q]:checked').value;
  qi++;qi<QS.length?renderQ():results()}
 if(e.target.id==="back"){qi--;renderQ()}
 if(e.target.id==="again"){qi=0;for(const k in ans)delete ans[k];$("#results").classList.add("hide");$("#qwrap").classList.remove("hide");renderQ()}});
function results(){
 const fmtBit={sunday:32,"21":2,"30":4,"40":8}[ans.weeks]||8;
 const goalCh={form:[0,3,19,20],groups:[2],reach:[17,18],gen:[5,4,6],care:[9,10,11,21]}[ans.goal]||[];
 const feltCh={anx:[9,3],disc:[2,1],money:[4,5,6],doubt:[21,22],grow:[0,19,20]}[ans.felt]||[];
 const se=+ans.season;
 const why=new Map();
 function score(o){let s=0,w=[];
  if(o.f&fmtBit){s+=2;w.push(({32:"fits a single catalytic Sunday","2":"fits a 3-week window","4":"fits a 4–5 week window","8":"built for a full 6-week run"})[String(fmtBit)])}
  if(goalCh.includes(o.ch)){s+=3;w.push("matches your goal of "+({form:"formation & depth",groups:"getting people into groups",reach:"reaching new people",gen:"generosity & vision",care:"caring for hurting people"})[ans.goal])}
  if(feltCh.includes(o.ch)){s+=3;w.push("speaks to a congregation feeling "+({anx:"anxious and tired",disc:"disconnected",money:"financial pressure",doubt:"honest questions",grow:"ready to grow"})[ans.felt])}
  if(se>=0&&o.se===se){s+=3;w.push("made for this exact season")}
  if(o.co&1){s+=2;w.push("a hand-curated flagship")}
  if(o.g==="AA")s+=1.5;else if(o.g==="A")s+=1;
  if(ans.eds==="yes"&&(o.af&33)){s+=.5}
  if(ans.budget==="lean"&&(o.f&2))s+=.5;
  if(ans.budget==="max"&&(o.f&8))s+=.5;
  return[s,w]}
 const scored=A.ROWS.map((o,i)=>{const[s,w]=score(o);why.set(o.id,w);return[s,i]}).sort((a,b)=>b[0]-a[0]);
 const picks=[],chSeen=new Set();
 for(const[s,i]of scored){const o=A.ROWS[i];if(chSeen.has(o.ch))continue;picks.push(o);chSeen.add(o.ch);if(picks.length===3)break}
 const sig=new Set([...goalCh,...feltCh]);
 const unexpected=scored.map(([s,i])=>A.ROWS[i]).find(o=>!sig.has(o.ch)&&!chSeen.has(o.ch)&&(o.co&1));
 $("#qwrap").classList.add("hide");$("#results").classList.remove("hide");
 $("#picks").innerHTML=picks.map((o,n)=>`<div><div style="max-width:230px">${A.cardHTML(o)}</div>
  <div class="why"><b>Why #${n+1}:</b> ${why.get(o.id).slice(0,3).join("; ")||"a strong all-church fit"}.</div></div>`).join("");
 if(unexpected)$("#wild").innerHTML=`<div style="max-width:230px">${A.cardHTML(unexpected)}</div>
  <div class="why"><b>The one you didn't ask for:</b> churches that run ${A.escapeH(A.chLabel(unexpected.ch))} right after a felt-need series see the deepest follow-through. Hold it for your next window.</div>`;
 A.paintCovers($("#results"))}
renderQ()}
/* =============================== BUILDER =============================== */
if($("#builder")){
let step=0;const B={voice:"pastoral"};
const STEPS=[
 {t:"Pastor Intelligence",d:"Your voice, your convictions, the message God has put on your heart.",body:`
  <div class="field"><label>The message in one sentence</label><input id="b-idea" placeholder="e.g., Our church needs to trust God with money before we can be generous"></div>
  <div class="field"><label>Texts God keeps bringing you back to (optional)</label><input id="b-texts" placeholder="e.g., 1 Timothy 6, Matthew 6"></div>
  <div class="field"><label>Your preaching voice</label><select id="b-voice"><option value="pastoral">Warm & pastoral</option><option value="prophetic">Direct & prophetic</option><option value="teacher">Careful teacher</option><option value="storyteller">Storyteller</option></select></div>`},
 {t:"Lifetogether Intelligence",d:"Twenty-five years of campaign architecture, applied to your message.",body:`
  <div class="field"><label>Which formation channel is closest?</label><select id="b-ch">${D.channels.map((c,i)=>`<option value="${i}">${c.name}</option>`).join("")}</select></div>
  <div class="field"><label>Format</label><select id="b-fmt"><option value="40">40-Day Journey — deepest formation</option><option value="30">30-Day Spiritual Journey</option><option value="21">21-Day Challenge</option><option value="7">7-Day Experience</option></select></div>`},
 {t:"Church Intelligence",d:"Your congregation's size, season, and readiness.",body:`
  <div class="field"><label>Weekend attendance</label><select id="b-size"><option>Under 200</option><option>200–800</option><option>800–2,500</option><option>2,500+</option></select></div>
  <div class="field"><label>Launch window</label><select id="b-when"><option>New Year</option><option>Lent / Easter</option><option>Fall</option><option>Advent</option><option>Flexible</option></select></div>
  <div class="field"><label>Editions</label><select id="b-eds"><option value="all">All four — whole church</option><option value="adult">Adult + Leader to start</option></select></div>`}];
function renderB(){const s=STEPS[step];
 $("#bsteps").innerHTML=STEPS.map((x,i)=>`<div class="intel" style="opacity:${i===step?1:.55}"><div class="num">${i+1}</div><h3>${x.t}</h3><p class="muted" style="font-size:14.5px">${x.d}</p>${i===step?x.body+`<div style="display:flex;gap:12px;margin-top:8px">${i?'<button class="btn ghost" id="bback">Back</button>':""}<button class="btn primary" id="bnext">${i===2?"Build my campaign brief":"Continue"}</button></div>`:""}</div>`).join("");
 if(B["idea"])try{$("#b-idea").value=B.idea}catch(e){}}
document.addEventListener("click",e=>{
 if(e.target.id==="bnext"){["idea","texts","voice","ch","fmt","size","when","eds"].forEach(k=>{const el=$("#b-"+k);if(el)B[k]=el.value});
  if(step===0&&!(B.idea||"").trim()){A.toast("Give us the message in one sentence");return}
  step++;step<3?renderB():brief()}
 if(e.target.id==="bback"){step--;renderB()}});
function brief(){
 const ch=+B.ch||0,fmt=B.fmt||"40",days=+fmt||40,sess={40:6,30:4,21:3,7:1}[fmt];
 const pool=window.SPOOLS[ch].map(i=>D.refs[i]);
 const seed=(B.idea||"x").split("").reduce((s,c)=>s+c.charCodeAt(0),0);
 const r=A.mulberry(seed);const pick=n=>{const a=[...pool],o=[];while(o.length<n&&a.length)o.push(a.splice(Math.floor(r()*a.length),1)[0]);return o};
 const words=(B.idea||"").toLowerCase().match(/[a-z']+/g)||[];
 const key=words.filter(w=>w.length>4&&!["about","before","after","church","every","their","would","could","needs","first"].includes(w));
 const kw=key[0]?key[0][0].toUpperCase()+key[0].slice(1):"Trust";
 const titles=[`${kw} First`,`The ${kw} Journey`,`${days} Days of ${kw}`,`${kw}, Together`];
 const texts=pick(sess);
 const price={40:2900,30:2400,21:1900,7:1200}[fmt]+(B.eds==="all"?600:0);
 $("#builder .qcard").classList.add("hide");
 $("#brief").classList.remove("hide");
 $("#brief .inner").innerHTML=`
  <p class="eyebrow gold">Your custom campaign brief</p>
  <h2>${titles[0]}</h2>
  <p class="lede">${A.escapeH(B.idea)}</p>
  <div class="twocol" style="margin:26px 0">
   <div class="edbox"><h4>Architecture</h4><ul>
    <li><b>Format:</b> ${days}-Day ${fmt==="7"?"Experience":"Journey"} · ${sess} weekend session${sess>1?"s":""}</li>
    <li><b>Channel:</b> ${A.chLabel(ch)}</li>
    <li><b>Launch window:</b> ${B.when}</li><li><b>Editions:</b> ${B.eds==="all"?"Adult · Youth · Children & Family · Leader":"Adult + Leader"}</li>
    <li><b>Voice calibration:</b> ${B.voice}</li></ul></div>
   <div class="edbox"><h4>Session map</h4><ul>${texts.map((t,i)=>`<li><b>Week ${i+1}:</b> ${t}${B.texts&&i===0?` <span class="muted">(anchored to your texts: ${A.escapeH(B.texts)})</span>`:""}</li>`).join("")}</ul></div>
  </div>
  <div class="edbox"><h4>Alternate titles to test with your team</h4><p style="margin:0">${titles.slice(1).join(" · ")}</p></div>
  <div class="summary" style="margin-top:26px"><div class="row"><span>Custom ${days}-Day campaign, scoped & written for your church</span><b>${A.money(price)}</b></div>
   <div class="row muted" style="font-size:13.5px">Includes sermon builds in your voice, daily devotional, group curriculum${B.eds==="all"?", youth & children's editions":""}, leader kit, and launch coaching call.</div></div>
  <div style="display:flex;gap:12px;margin-top:20px;flex-wrap:wrap">
   <button class="btn primary" id="baddcart">Add custom campaign to cart — ${A.money(price)}</button>
   <button class="btn ghost" id="bagain">Start over</button></div>`;
 $("#baddcart").addEventListener("click",()=>{A.addToCart(null,null,{custom:true,id:"CUSTOM-"+Date.now(),fmt,qty:1,t:"Custom Campaign: "+titles[0],price});location.href="cart.html"});
 $("#bagain").addEventListener("click",()=>{step=0;$("#brief").classList.add("hide");$("#builder .qcard").classList.remove("hide");renderB()})}
renderB()}
/* =============================== CART =============================== */
if($("#cartpage")){
function draw(){const c=A.cart();
 if(!c.length){$("#cartpage").innerHTML=`<p class="lede">Your cart is empty.</p><a class="btn primary" href="browse.html">Browse 16,000+ campaigns</a>`;return}
 $("#cartpage").innerHTML=c.map((l,i)=>{
  const o=l.custom?null:A.BYID.get(l.id);
  const cov=o?`<div style="width:64px">${window.Covers.svg(o)}</div>`:`<div style="width:64px;aspect-ratio:3/4;border-radius:8px;background:#172542;color:#E4C878;display:grid;place-items:center;font-family:'Hanken Grotesk';font-weight:700">C</div>`;
  const fm=A.FMT_META.find(f=>f.key===l.fmt);
  return `<div class="cartline">${cov}<div><b>${A.escapeH(l.t)}</b><div class="muted" style="font-size:13.5px">${fm?fm.name:"Custom build"} · all editions</div></div>
   <div><button class="btn sm ghost" data-dec="${i}">−</button> ${l.qty} <button class="btn sm ghost" data-inc="${i}">+</button></div>
   <div style="text-align:right"><b>${A.money(l.price*l.qty)}</b><br><button class="btn sm ghost" data-del="${i}" style="margin-top:6px">Remove</button></div></div>`}).join("")+
 `<div class="summary" style="margin-top:22px"><div class="row"><span>Subtotal</span><b>${A.money(tot())}</b></div>
  <div class="row"><span>Launch coaching call</span><b>Included</b></div>
  <div class="row total"><span>Total</span><span>${A.money(tot())}</span></div></div>
  <div style="display:flex;gap:12px;margin-top:22px"><a class="btn primary" href="checkout.html">Proceed to checkout</a><a class="btn ghost" href="browse.html">Keep browsing</a></div>`;
 A.paintCovers&&0}
function tot(){return A.cart().reduce((s,l)=>s+l.price*l.qty,0)}
document.addEventListener("click",e=>{
 const c=A.cart();
 const inc=e.target.closest("[data-inc]"),dec=e.target.closest("[data-dec]"),del=e.target.closest("[data-del]");
 if(inc){c[+inc.getAttribute("data-inc")].qty++;A.saveCart(c);draw()}
 if(dec){const l=c[+dec.getAttribute("data-dec")];l.qty=Math.max(1,l.qty-1);A.saveCart(c);draw()}
 if(del){c.splice(+del.getAttribute("data-del"),1);A.saveCart(c);draw()}});
draw()}
/* =============================== CHECKOUT =============================== */
if($("#checkout")){
const c=A.cart();if(!c.length)location.href="cart.html";
const tot=c.reduce((s,l)=>s+l.price*l.qty,0);
$("#osum").innerHTML=c.map(l=>`<div class="row"><span>${A.escapeH(l.t)} ×${l.qty}</span><b>${A.money(l.price*l.qty)}</b></div>`).join("")+
 `<div class="row total"><span>Total due</span><span>${A.money(tot)}</span></div>`;
let method="card";
document.querySelectorAll(".paytab").forEach(t=>t.addEventListener("click",()=>{
 document.querySelectorAll(".paytab").forEach(x=>x.classList.remove("on"));t.classList.add("on");
 method=t.getAttribute("data-m");
 document.querySelectorAll(".payform").forEach(f=>f.classList.add("hide"));
 $("#pf-"+method).classList.remove("hide")}));
/* ----------------------------------------------------------------------
   STRIPE INTEGRATION SEAM
   Replace placeOrder()'s success branch with:
     const res = await fetch(YOUR_BACKEND + "/create-checkout-session", {
       method:"POST", headers:{"Content-Type":"application/json"},
       body: JSON.stringify({lines: A.cart(), method})
     });
     const {url} = await res.json();  location.href = url;   // Stripe-hosted checkout
   Then point Stripe's success_url at confirmation.html?order=<session_id>
   and fulfill downloads server-side from the webhook. Nothing else changes.
---------------------------------------------------------------------- */
function need(id,test){const f=$("#"+id).closest(".field");const ok=test($("#"+id).value.trim());f.classList.toggle("bad",!ok);return ok}
$("#place").addEventListener("click",()=>{
 let ok=need("co-church",v=>v.length>1)&&need("co-name",v=>v.length>1)&&need("co-email",v=>/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(v));
 if(method==="card")ok=need("cc-num",v=>v.replace(/\s/g,"").length>=15)&&need("cc-exp",v=>/^\d{2}\/\d{2}$/.test(v))&&need("cc-cvc",v=>v.length>=3)&&ok;
 if(method==="invoice")ok=need("po-num",v=>v.length>0)&&ok;
 if(!ok){A.toast("Check the highlighted fields");return}
 const order={n:"LT-"+Math.random().toString(36).slice(2,8).toUpperCase(),when:Date.now(),lines:c,total:tot,
   church:$("#co-church").value,name:$("#co-name").value,email:$("#co-email").value,method};
 const os=A.store.get("orders40")||[];os.push(order);A.store.set("orders40",os);
 A.saveCart([]);location.href="confirmation.html?o="+order.n});
}
/* =============================== CONFIRMATION =============================== */
if($("#confirm")){
const n=new URLSearchParams(location.search).get("o");
const order=(A.store.get("orders40")||[]).find(x=>x.n===n)||(A.store.get("orders40")||[]).slice(-1)[0];
if(order){$("#ordno").textContent=order.n;$("#ordch").textContent=order.church;
 $("#ordsum").innerHTML=order.lines.map(l=>`<div class="row"><span>${A.escapeH(l.t)} ×${l.qty}</span><b>${A.money(l.price*l.qty)}</b></div>`).join("")+
  `<div class="row total"><span>${order.method==="invoice"?"To be invoiced":"Paid"}</span><span>${A.money(order.total)}</span></div>`;
 const files=[["Adult Devotional — Week One","devotional",docWeek],["Sermon Builds & Preaching Ideas","sermons",docSermons],["Small Group Leader Kit","leaderkit",docLeader],["Launch Roadmap & Timeline","roadmap",docRoad]];
 $("#dls").innerHTML=files.map(([t,k])=>`<div class="dl"><div class="ic">DOC</div><div style="flex:1"><b>${t}</b><div class="muted" style="font-size:13px">Editable Word document — starts your build today</div></div><button class="btn sm navy" data-dl="${k}">Download</button></div>`).join("");
 const first=order.lines[0];const o=first&&!first.custom?A.BYID.get(first.id):null;
 function head(t){return `<h1 style="font-family:Arial;color:#172542">${t}</h1><p style="color:#B98D3E;font-family:Arial;font-size:12px;letter-spacing:2px">${(o?o.t:first.t).toUpperCase()} · LIFETOGETHER / 40 DAY CAMPAIGNS</p><hr>`}
 function docWeek(){let b=head("Adult Devotional — Week One");for(let d=1;d<=7;d++)b+=`<h2 style="font-family:Arial;color:#172542">Day ${d}</h2><p><i>Scripture, reflection, one honest step, and a prayer — expand each day from the sample-day pattern on the campaign page.</i></p><p>Reading: ${o?window.SPOOLS[o.ch].map(i=>A.D.refs[i])[d%20]:"John 15:5"}</p>`;return b}
 function docSermons(){let b=head("Sermon Builds");for(let w=1;w<=6;w++)b+=`<h2 style="font-family:Arial">Week ${w}</h2><p>Title · three texts · five preaching ideas · full outline. Generated on the campaign page — paste your week here and shape it in your voice.</p>`;return b}
 function docLeader(){return head("Small Group Leader Kit")+`<h2 style="font-family:Arial">Recruiting hosts</h2><p>The ask is one sentence: "Would you open your home for six weeks?" Hosts are not teachers — the video teaches; hosts make room.</p><h2 style="font-family:Arial">The first meeting</h2><p>Names, food, one question, short video, one honest answer each, prayer. Forty-five minutes. End on time and they will come back.</p><h2 style="font-family:Arial">A simple session order</h2><p>Open (10) · Video (15) · Discuss (25) · Pray (10).</p>`}
 function docRoad(){return head("Launch Roadmap")+["6 weeks out — announce the series and recruit hosts","5 weeks out — host orientation & materials","4 weeks out — sign-up Sunday #1","3 weeks out — sign-up Sunday #2, children & youth teams briefed","2 weeks out — sermon prep from the builds, testing videos","1 week out — commitment Sunday","Launch Sunday — every ministry, one message","Week 7 — Celebration Sunday: stories, baptisms, next steps"].map((s,i)=>`<h3 style="font-family:Arial">${s.split(" — ")[0]}</h3><p>${s.split(" — ")[1]}</p>`).join("")}
 document.addEventListener("click",e=>{const b=e.target.closest("[data-dl]");if(!b)return;
  const k=b.getAttribute("data-dl");const body={devotional:docWeek,sermons:docSermons,leaderkit:docLeader,roadmap:docRoad}[k]();
  const blob=new Blob(["\ufeff",`<html xmlns:w="urn:schemas-microsoft-com:office:word"><head><meta charset="utf-8"></head><body>${body}</body></html>`],{type:"application/msword"});
  const a=document.createElement("a");a.href=URL.createObjectURL(blob);a.download=(o?o.slug:"custom")+"-"+k+".doc";a.click()})}
}
/* =============================== ACCOUNT =============================== */
if($("#account")){
const os=(A.store.get("orders40")||[]).slice().reverse();
$("#orders").innerHTML=os.length?os.map(x=>`<tr><td>${x.n}</td><td>${new Date(x.when).toLocaleDateString()}</td><td>${x.lines.map(l=>A.escapeH(l.t)).join("; ")}</td><td>${A.money(x.total)}</td><td><a href="confirmation.html?o=${x.n}">Downloads</a></td></tr>`).join(""):
 `<tr><td colspan="5" class="muted">No orders yet — your purchased campaigns and downloads will live here.</td></tr>`;
const lib=new Map();os.forEach(x=>x.lines.forEach(l=>{if(!l.custom&&!lib.has(l.id))lib.set(l.id,A.BYID.get(l.id))}));
if(lib.size){$("#library").innerHTML=[...lib.values()].filter(Boolean).map(o=>A.cardHTML(o)).join("");A.paintCovers($("#library"))}
else $("#library").innerHTML=`<p class="muted">Your library is empty. <a href="browse.html">Find your first campaign.</a></p>`}
})();
