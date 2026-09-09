/* ════════════════════════════════════════════════════════════════
   THE FAMILY LEGACY COLLECTION · shared chrome & helpers — v4
   (matched to the Family Legacy by Design brand)
   ════════════════════════════════════════════════════════════════ */
(function(){
'use strict';

/* ---------- safe storage ---------- */
var MEM={};
window.FLstore={
  get:function(k){ try{ return localStorage.getItem(k); }catch(e){ return MEM[k]||null; } },
  set:function(k,v){ try{ localStorage.setItem(k,v); }catch(e){ MEM[k]=v; } }
};

/* ---------- the tree logomark ---------- */
window.treeSVG=function(size,color){
  color=color||'#FFFFFF';
  return '<svg class="tree" viewBox="0 0 100 100" width="'+size+'" height="'+size+'" fill="'+color+'" aria-hidden="true">'
   +'<rect x="46.6" y="52" width="6.8" height="34" rx="3"/>'
   +'<path d="M50 86c-9-2-19-4-27-3 6-5 15-6 22-5-8-3-16-9-19-16 8 1 15 6 20 11-4-7-6-16-4-24 5 6 8 14 8 21 0-7 3-15 8-21 2 8 0 17-4 24 5-5 12-10 20-11-3 7-11 13-19 16 7-1 16 0 22 5-8-1-18 1-27 3z" opacity=".001"/>'
   +'<path d="M50 12c3 7 2 14-1 19 5-4 12-6 18-5-3 6-9 10-15 12 7-1 15 1 20 6-6 3-14 3-20 1 6 3 11 9 13 16-7-1-13-5-17-10v9h-4v-9c-4 5-10 9-17 10 2-7 7-13 13-16-6 2-14 2-20-1 5-5 13-7 20-6-6-2-12-6-15-12 6-1 13 1 18 5-3-5-4-12-1-19h8z" opacity=".001"/>'
   +'<g>'
   +'<path d="M48 54c-1-8-6-15-13-18 1 8 6 15 13 18z"/>'
   +'<path d="M52 54c1-8 6-15 13-18-1 8-6 15-13 18z"/>'
   +'<path d="M48 44c-2-7-8-12-15-13 2 7 8 12 15 13z"/>'
   +'<path d="M52 44c2-7 8-12 15-13-2 7-8 12-15 13z"/>'
   +'<path d="M48.4 35c-2-6-6-10-12-12 2 6 6 11 12 12z"/>'
   +'<path d="M51.6 35c2-6 6-10 12-12-2 6-6 11-12 12z"/>'
   +'<path d="M50 32c-3-5-3-11 0-16 3 5 3 11 0 16z"/>'
   +'<circle cx="27" cy="24" r="4"/><circle cx="73" cy="24" r="4"/>'
   +'<circle cx="19" cy="38" r="3.4"/><circle cx="81" cy="38" r="3.4"/>'
   +'<circle cx="24" cy="52" r="3"/><circle cx="76" cy="52" r="3"/>'
   +'<circle cx="50" cy="10" r="4"/>'
   +'<path d="M50 92c-8-6-18-8-27-6 7-7 18-9 27-6 9-3 20-1 27 6-9-2-19 0-27 6z"/>'
   +'</g></svg>';
};

/* ---------- growth rings (kept for progress dials) ---------- */
window.ringsSVG=function(size,stroke,cls){
  stroke=stroke||"#CE9F4F";
  return '<svg class="'+(cls||'')+'" viewBox="0 0 100 100" width="'+size+'" height="'+size+'" fill="none" aria-hidden="true">'
   +'<circle cx="50" cy="50" r="10" stroke="'+stroke+'" stroke-width="2.4"/>'
   +'<circle cx="50" cy="50" r="20" stroke="'+stroke+'" stroke-width="1.9" opacity=".85"/>'
   +'<circle cx="50" cy="50" r="30" stroke="'+stroke+'" stroke-width="1.5" opacity=".64"/>'
   +'<circle cx="50" cy="50" r="40" stroke="'+stroke+'" stroke-width="1.2" opacity=".46"/>'
   +'<circle cx="50" cy="50" r="48" stroke="'+stroke+'" stroke-width="1" opacity=".3"/>'
   +'<circle cx="50" cy="50" r="2.6" fill="'+stroke+'"/></svg>';
};
window.ROMAN=["i","ii","iii","iv","v","vi","vii","viii","ix","x"];

/* ---------- stroke icons ---------- */
var P={
  sun:'<circle cx="12" cy="13.5" r="4.2"/><path d="M12 3.5v2.6M4.6 6.9l1.9 1.9M19.4 6.9l-1.9 1.9M2.5 13.5h2.6M18.9 13.5h2.6M3.5 19.5h17"/>',
  table:'<path d="M3 9.5h18M5.5 9.5V7.8c0-.7.6-1.3 1.3-1.3h10.4c.7 0 1.3.6 1.3 1.3v1.7M6 9.5V19M18 9.5V19M3.5 19h5M15.5 19h5"/>',
  quill:'<path d="M19.5 4.5c-5.5.5-9.8 3-12 7.5-1 2-1.5 4.5-1.5 7.5 3 0 5.5-.5 7.5-1.5 4.5-2.2 7-6.5 7.5-12z"/><path d="M6 18.5 15.5 9"/>',
  home:'<path d="M4.5 11 12 4.5 19.5 11M6.5 9.5V19c0 .6.4 1 1 1h9c.6 0 1-.4 1-1V9.5M10 20v-5.5h4V20"/>',
  clock:'<circle cx="12" cy="12" r="8.5"/><path d="M12 7.5V12l3.2 2"/>',
  compass:'<circle cx="12" cy="12" r="8.5"/><path d="m14.8 9.2-1.7 4.3-4 1.4 1.7-4.3z"/>',
  bridge:'<path d="M4 16.5h16M4 16.5V12c2.5-3.5 5-5 8-5s5.5 1.5 8 5v4.5M8.2 16.5v-3M12 16.5V11M15.8 16.5v-3"/>',
  scroll:'<path d="M7 4.5h11c1 0 1.8.8 1.8 1.8S19 8 18 8H7M7 4.5C5.9 4.5 5 5.4 5 6.5v12c0 .6.4 1 1 1h11.5c1 0 1.8-.8 1.8-1.8S18.5 16 17.5 16H8"/><path d="M9 11h6M9 13.7h6"/>',
  calendar:'<rect x="4" y="6" width="16" height="14" rx="1.5"/><path d="M4 10.5h16M8.5 4v3.5M15.5 4v3.5M8 14h2M14 14h2M8 17h2M14 17h2"/>',
  heart:'<path d="M12 19.5S4.5 15 4.5 9.8C4.5 7.4 6.3 5.5 8.6 5.5c1.5 0 2.7.8 3.4 2 .7-1.2 1.9-2 3.4-2 2.3 0 4.1 1.9 4.1 4.3 0 5.2-7.5 9.7-7.5 9.7z"/>',
  church:'<path d="M12 3.5v4M10.3 5.5h3.4M8 20v-7.5L12 9l4 3.5V20M4 20h16M4.5 20v-4.5L8 12.8M19.5 20v-4.5L16 12.8M12 20v-3.8"/>',
  users:'<circle cx="8.5" cy="9" r="2.8"/><circle cx="15.8" cy="10.2" r="2.2"/><path d="M3.8 19c.4-3.2 2.3-5 4.7-5s4.3 1.8 4.7 5M13.6 19c.3-2.4 1.2-3.8 2.5-4.3 1.9-.6 3.8 1 4.1 4.3"/>',
  book:'<path d="M12 6.5C10.5 5 8.5 4.5 5 4.5v14c3.5 0 5.5.5 7 2 1.5-1.5 3.5-2 7-2v-14c-3.5 0-5.5.5-7 2z"/><path d="M12 6.5v14"/>',
  story:'<path d="M12 4.5c4.5 0 8 2.8 8 6.3 0 3.5-3.5 6.3-8 6.3-.9 0-1.8-.1-2.6-.3L5 19.5l1-3.6C4.7 14.7 4 13.3 4 10.8c0-3.5 3.5-6.3 8-6.3z"/><path d="M8.5 9.8h7M8.5 12.3h4.5"/>',
  doc:'<path d="M7 3.5h7l4 4V19c0 .8-.7 1.5-1.5 1.5h-9.5C6.2 20.5 5.5 19.8 5.5 19V5c0-.8.7-1.5 1.5-1.5z"/><path d="M14 3.5V8h4.5M8.5 12h7M8.5 15.2h7"/>',
  bulb:'<path d="M12 3.5a6 6 0 0 1 3.6 10.8c-.7.6-1.1 1.2-1.1 2v.7h-5v-.7c0-.8-.4-1.4-1.1-2A6 6 0 0 1 12 3.5z"/><path d="M9.8 20h4.4M10.3 22h3.4"/>',
  check:'<path d="m5 12.5 4.5 4.5L19 7.5"/>',
  arrowr:'<path d="M4 12h15M13.5 6.5 19 12l-5.5 5.5"/>'
};
window.icon=function(name,size,sw){
  size=size||24;
  return '<svg viewBox="0 0 24 24" width="'+size+'" height="'+size+'" fill="none" stroke="currentColor" stroke-width="'+(sw||1.75)+'" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'+(P[name]||'')+'</svg>';
};

/* ---------- favicon ---------- */
(function(){
  var fav='data:image/svg+xml,'+encodeURIComponent('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" rx="14" fill="#0F2E23"/><g fill="#CE9F4F"><rect x="29.8" y="34" width="4.4" height="20" rx="2.2"/><path d="M32 36c-1-5-4-9-8-11 1 5 4 9 8 11z"/><path d="M32 36c1-5 4-9 8-11-1 5-4 9-8 11z"/><path d="M31 29c-1.4-4-4.4-7-8.4-8 1.4 4 4.4 7 8.4 8z"/><path d="M33 29c1.4-4 4.4-7 8.4-8-1.4 4-4.4 7-8.4 8z"/><path d="M32 26c-2-3-2-7 0-10 2 3 2 7 0 10z"/><circle cx="18" cy="16" r="2.6"/><circle cx="46" cy="16" r="2.6"/><circle cx="13" cy="26" r="2.2"/><circle cx="51" cy="26" r="2.2"/><circle cx="32" cy="9" r="2.6"/><path d="M32 58c-5-4-11-5-17-4 4-4 11-6 17-4 6-2 13 0 17 4-6-1-12 0-17 4z"/></g></svg>');
  var l=document.createElement('link'); l.rel='icon'; l.href=fav; document.head.appendChild(l);
})();

/* ---------- nav ---------- */
var here=(location.pathname.split('/').pop()||'index.html');
function on(p){ return here===p?' class="on"':''; }
var nav=document.createElement('div');
nav.className='navwrap overdark';
nav.innerHTML=
 '<nav class="flnav" aria-label="Main">'
 +'<a class="brand" href="index.html">'+treeSVG(40,'#FFFFFF')
 +'<span class="a">Family Legacy<span>by Design · The Collection</span></span></a>'
 +'<div class="links">'
 +'<a href="index.html"'+on('index.html')+'>Home</a>'
 +'<a href="campaigns.html"'+on('campaigns.html')+'>The Collection</a>'
 +'<a href="vision.html"'+on('vision.html')+'>The Vision</a>'
 +'<a href="pathways.html"'+on('pathways.html')+'>Pathways</a>'
 +'<a href="assessment.html"'+on('assessment.html')+'>Assessment</a>'
 +'<a href="about.html"'+on('about.html')+'>About</a>'
 +'</div>'
 +'<a class="btn grad sm cta" href="reader.html?id=family-legacy&day=1">Read Day One <span class="ar">\u2192</span></a>'
 +'</nav>';
document.body.insertBefore(nav,document.body.firstChild);
addEventListener('scroll',function(){document.body.classList.toggle('scrolled',scrollY>10);},{passive:true});

/* ---------- footer ---------- */
var foot=document.createElement('footer');
foot.className='fl-foot';
foot.innerHTML=
 '<div class="top"></div>'
 +'<div class="in">'
 +'<div><div class="bt">'+treeSVG(42,'#FFFFFF')
 +'<b>Family Legacy<span>by Design · The Campaign Collection</span></b></div>'
 +'<p class="desc">Ten journeys. Sixty table sessions. One shepherd\u2019s questions, set at every table that can\u2019t reach the living room.</p></div>'
 +'<div><div class="fh">The Collection</div><div class="fnav">'
 +'<a href="campaigns.html">All ten journeys</a>'
 +'<a href="campaign.html?id=family-legacy">Family Legacy \u00B7 the flagship</a>'
 +'<a href="campaign.html?id=wisdom-driven-life">The Wisdom-Driven Life</a>'
 +'<a href="reader.html?id=family-legacy&day=1">The Reading Room</a>'
 +'</div></div>'
 +'<div><div class="fh">The Work</div><div class="fnav">'
 +'<a href="vision.html">The Vision</a>'
 +'<a href="pathways.html">Families \u00B7 Advisors \u00B7 Churches</a>'
 +'<a href="assessment.html">How well are we doing?</a>'
 +'<a href="about.html">Tom Conway & the partnership</a>'
 +'</div></div>'
 +'</div>'
 +'<div class="bar"><span>\u00A9 2026 Family Legacy by Design \u00B7 in partnership with Lifetogether \u00B7 Rancho Santa Margarita, California</span>'
 +'<span>Built for tables, not screens</span></div>';
document.body.appendChild(foot);

/* ---------- reveals ---------- */
window.FLobserve=function(){
  var els=document.querySelectorAll('.rv:not(.in)');
  if(!('IntersectionObserver' in window)){ els.forEach(function(e){e.classList.add('in');}); return; }
  var io=new IntersectionObserver(function(es){
    es.forEach(function(en){ if(en.isIntersecting){ en.target.classList.add('in'); io.unobserve(en.target);} });
  },{threshold:.08,rootMargin:'0px 0px -4% 0px'});
  els.forEach(function(e){ io.observe(e); });
};
if(document.readyState==='loading'){ document.addEventListener('DOMContentLoaded',FLobserve); } else { FLobserve(); }

/* ---------- counters ---------- */
window.FLcount=function(){
  var els=document.querySelectorAll('[data-count]');
  if(!els.length) return;
  var reduce=matchMedia('(prefers-reduced-motion: reduce)').matches;
  var io=new IntersectionObserver(function(es){
    es.forEach(function(en){
      if(!en.isIntersecting) return; io.unobserve(en.target);
      var el=en.target; if(el.dataset.counted) return; el.dataset.counted='1';
      var end=+el.dataset.count, suf=el.dataset.suffix||'';
      if(reduce){ el.textContent=end+suf; return; }
      var t0=null, dur=1200;
      function tick(t){ if(!t0)t0=t; var p=Math.min(1,(t-t0)/dur); p=1-Math.pow(1-p,3);
        el.textContent=Math.round(end*p)+suf; if(p<1)requestAnimationFrame(tick); }
      requestAnimationFrame(tick);
    });
  },{threshold:.5});
  els.forEach(function(e){ io.observe(e); });
};
if(document.readyState==='loading'){ document.addEventListener('DOMContentLoaded',FLcount); } else { FLcount(); }

/* ---------- data helpers ---------- */
window.FLget=function(id){
  return (window.FLC&&FLC.campaigns||[]).filter(function(c){return c.id===id;})[0]||null;
};
window.qs=function(k){ return new URLSearchParams(location.search).get(k); };

/* ---------- cover renderer (product style) ---------- */
window.coverHTML=function(c){
  var len=(c.weeks?c.weeks.reduce(function(a,w){return a+w.days.length;},0):40);
  return '<a class="cov" href="campaign.html?id='+c.id+'" style="--ca:'+c.hue[0]+';--cb:'+c.hue[1]+'" aria-label="'+c.title+'">'
   +'<div class="canvas">'
   +'<span class="brand">'+treeSVG(13,'#FFFFFF')+'Family Legacy</span>'
   +'<div class="mid">'+treeSVG(96,'#E3C480')+'<div class="nm">'+c.title+'</div></div>'
   +'<div class="sb">'+c.sub+'</div>'
   +'<div class="fmt">'+len+' Days \u00B7 6 Sessions</div>'
   +'</div></a>';
};

/* ---------- sessions accordion ---------- */
window.sessionsHTML=function(c){
  return c.sessions.map(function(s,i){
    return '<details class="session"'+(i===0?' open':'')+'><summary>'
     +'<span class="n">'+(i+1)+'</span><span class="t">'+s.t+'</span>'
     +'<span class="scr">'+s.scr+'</span>'
     +'<svg class="caret" width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"><path d="M9 5l7 7-7 7"/></svg>'
     +'</summary><div class="body">'
     +'<p class="sq">'+s.sq+'</p>'
     +'<span class="capsb">Around the table</span>'
     +'<ol>'+s.qs.map(function(q){return '<li>'+q+'</li>';}).join('')+'</ol>'
     +'<div class="step"><b>This week\u2019s step</b>'+s.step+'</div>'
     +'</div></details>';
  }).join('');
};

/* ---------- reading progress ---------- */
window.FLprog={
  key:function(id){ return 'flc-days-'+id; },
  done:function(id){ try{ return JSON.parse(FLstore.get(this.key(id))||'[]'); }catch(e){ return []; } },
  mark:function(id,day){
    var d=this.done(id); if(d.indexOf(day)<0){ d.push(day); d.sort(function(a,b){return a-b;}); }
    FLstore.set(this.key(id),JSON.stringify(d)); return d;
  }
};
})();
