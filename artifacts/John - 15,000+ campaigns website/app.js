/* 40dc shared runtime: data access, cart, pricing, header behaviors. Works from file:// (data ships as .js). */
(function(){
"use strict";
const D = window.DATA40;                       // set by data/index.js
const F = {S7:1,S21:2,S30:4,S40:8,ST:16,C1:32};
const FMT_META = [
 {bit:8, key:"40", name:"40-Day Journey",  days:40, sess:6, price:849, chip:"40"},
 {bit:4, key:"30", name:"30-Day Spiritual Journey", days:30, sess:4, price:649, chip:"30"},
 {bit:2, key:"21", name:"21-Day Challenge", days:21, sess:3, price:449, chip:"21"},
 {bit:1, key:"7",  name:"7-Day Experience", days:7,  sess:1, price:249, chip:"7"},
 {bit:16,key:"study", name:"6-Session Study", days:0, sess:6, price:549, chip:"Study"},
 {bit:32,key:"sunday",name:"Catalytic Sunday", days:1, sess:1, price:149, chip:"1-Day"},
];
const GRADE_PREMIUM = {AA:200, A:100};
function rowObj(r){const c=D.cols,o={};c.forEach((k,i)=>o[k]=r[i]);return o}
const ROWS = D.rows.map(rowObj);
const BYID = new Map(ROWS.map(o=>[o.id,o]));
function price(o,fmtKey){const f=FMT_META.find(x=>x.key===fmtKey)||FMT_META[0];
  return f.price + (GRADE_PREMIUM[o.g]||0)}
function fmtsOf(o){return FMT_META.filter(f=>o.f&f.bit)}
function chLabel(i){return D.channels[i].name}
function themeLabel(i){return D.themes[i][1]}
function refOf(o){return D.refs[o.sb]}
function money(n){return "$"+n.toLocaleString("en-US")}
/* ------- storage (localStorage w/ in-memory fallback for locked-down contexts) */
const mem={};const store={
 get(k){try{return JSON.parse(localStorage.getItem(k))}catch(e){return mem[k]??null}},
 set(k,v){try{localStorage.setItem(k,JSON.stringify(v))}catch(e){mem[k]=v}},
 del(k){try{localStorage.removeItem(k)}catch(e){delete mem[k]}}};
/* ------- cart */
function cart(){return store.get("cart40")||[]}
function saveCart(c){store.set("cart40",c);badge()}
function addToCart(id,fmtKey,custom){
 const c=cart();
 if(custom){c.push(custom)}
 else{const o=BYID.get(id);if(!o)return;
   const ex=c.find(l=>l.id===id&&l.fmt===fmtKey);
   if(ex)ex.qty+=1;else c.push({id,fmt:fmtKey,qty:1,t:o.t,price:price(o,fmtKey)});}
 saveCart(c);toast("Added to cart");}
function badge(){const n=cart().reduce((s,l)=>s+ (l.qty||1),0);
 document.querySelectorAll(".cartlink .n").forEach(el=>{el.textContent=n;el.style.display=n?"grid":"none"})}
function toast(msg){let t=document.querySelector(".toast40");
 if(!t){t=document.createElement("div");t.className="toast40";t.style.cssText="position:fixed;bottom:24px;left:50%;transform:translateX(-50%);background:#172542;color:#fff;font-family:'Hanken Grotesk',sans-serif;font-weight:600;padding:12px 22px;border-radius:999px;box-shadow:0 8px 30px rgba(16,30,56,.3);z-index:99;transition:opacity .3s";document.body.appendChild(t)}
 t.textContent=msg;t.style.opacity="1";clearTimeout(t._h);t._h=setTimeout(()=>t.style.opacity="0",1800)}
/* ------- shard loader (script injection: file:// safe) */
const shards={};window.SHARD=function(ci,payload){shards[ci]=payload;(shardWait[ci]||[]).forEach(fn=>fn(payload));shardWait[ci]=[]};
const shardWait={};
function loadShard(ci,cb){if(shards[ci])return cb(shards[ci]);
 (shardWait[ci]=shardWait[ci]||[]).push(cb);
 if(shardWait[ci].length>1)return;
 const s=document.createElement("script");s.src=window.REL+"data/ch"+String(ci).padStart(2,"0")+".js";document.head.appendChild(s)}
/* ------- card renderer */
function starSVG(){return '<span class="star" title="Flagship"><svg viewBox="0 0 24 24"><path d="M12 2l2.6 6.3 6.8.5-5.2 4.4 1.6 6.6L12 16.9 6.2 19.8l1.6-6.6L2.6 8.8l6.8-.5z"/></svg></span>'}
function chipLock(o){const ks=fmtsOf(o).filter(f=>f.bit<16).map(f=>f.chip);
 const extra=fmtsOf(o).filter(f=>f.bit>=16).map(f=>f.chip);
 let s="";if(ks.length)s+=`<span class="chip fmt">${ks.join(" · ")}</span>`;
 extra.forEach(e=>s+=`<span class="chip">${e}</span>`);return s}
function cardHTML(o,rel){rel=rel??window.REL;
 const url=rel+"campaign.html?id="+o.id;
 return `<article class="card">${o.co&1?starSVG():""}<button class="addbtn" data-add="${o.id}" aria-label="Add ${escapeH(o.t)} to cart">+</button>
 <a class="cover" href="${url}" data-cover="${o.id}" aria-hidden="true" tabindex="-1"></a>
 <div class="body"><h4><a href="${url}">${escapeH(o.t)}</a></h4>
 ${o.s?`<div class="sub">${escapeH(o.s)}</div>`:""}
 <div class="chips">${chipLock(o)}<span class="chip">${escapeH(chLabel(o.ch))}</span>${o.co&4?'<span class="tag-new">NEW</span>':""}</div></div></article>`}
function paintCovers(scope){ (scope||document).querySelectorAll("[data-cover]").forEach(a=>{
 if(a._done)return;const o=BYID.get(a.getAttribute("data-cover"));if(!o)return;
 a.innerHTML=window.Covers.svg(o);a._done=1})}
function escapeH(s){return String(s??"").replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;").replace(/"/g,"&quot;")}
/* ------- boot */
document.addEventListener("click",e=>{
 const b=e.target.closest("[data-add]");if(b){e.preventDefault();addToCart(b.getAttribute("data-add"), b.getAttribute("data-fmt")||defaultFmt(BYID.get(b.getAttribute("data-add"))));}
 const h=e.target.closest(".hamb");if(h){document.querySelector(".nav-links").classList.toggle("open")}
});
function defaultFmt(o){const f=fmtsOf(o)[0];return f?f.key:"40"}
document.addEventListener("DOMContentLoaded",badge);
window.App={ROWS,BYID,D,FMT_META,fmtsOf,price,money,chLabel,themeLabel,refOf,cardHTML,paintCovers,addToCart,cart,saveCart,store,loadShard,escapeH,defaultFmt,toast,mulberry:function(a){return function(){a|=0;a=a+0x6D2B79F5|0;var t=Math.imul(a^a>>>15,1|a);t=t+Math.imul(t^t>>>7,61|t)^t;return((t^t>>>14)>>>0)/4294967296}}};
})();
