"""CSS + JS assets for the artifacts site. Plain strings — no f-string brace escaping."""

CSS = r"""
/* ---------- tokens ---------- */
:root{
  --bg:#faf8f5; --panel:#ffffff; --fg:#1b1815; --mut:#6f6760; --faint:#98908a;
  --line:#e7e0d6; --line2:#f1ece4;
  --acc:#8a5a2b; --acc-soft:#f3e7d8;
  --ok:#2f6b4f; --warn:#9a6a1c; --danger:#9b3b2f;
  --shadow:0 1px 2px rgba(30,25,20,.05),0 8px 24px -12px rgba(30,25,20,.14);
  --r:12px; --maxw:1120px;
}
@media (prefers-color-scheme:dark){
  :root:not([data-theme="light"]){
    --bg:#14120e; --panel:#1c1a15; --fg:#ece7de; --mut:#9d958a; --faint:#7d7469;
    --line:#2c2820; --line2:#232019;
    --acc:#d9a44e; --acc-soft:#2a2115;
    --ok:#6fbf95; --warn:#d6a85a; --danger:#e0806f;
    --shadow:0 1px 2px rgba(0,0,0,.4),0 8px 24px -12px rgba(0,0,0,.6);
  }
}
:root[data-theme="dark"]{
  --bg:#14120e; --panel:#1c1a15; --fg:#ece7de; --mut:#9d958a; --faint:#7d7469;
  --line:#2c2820; --line2:#232019;
  --acc:#d9a44e; --acc-soft:#2a2115;
  --ok:#6fbf95; --warn:#d6a85a; --danger:#e0806f;
  --shadow:0 1px 2px rgba(0,0,0,.4),0 8px 24px -12px rgba(0,0,0,.6);
}

*,*::before,*::after{box-sizing:border-box}
html{-webkit-text-size-adjust:100%}
body{
  margin:0;background:var(--bg);color:var(--fg);
  font:16px/1.6 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;
  -webkit-font-smoothing:antialiased;
}
a{color:var(--acc);text-decoration:none}
a:hover{text-decoration:underline}
.wrap{max-width:var(--maxw);margin:0 auto;padding:0 20px}

/* ---------- header ---------- */
header.top{border-bottom:1px solid var(--line);background:var(--panel)}
.brand{display:flex;align-items:baseline;gap:12px;flex-wrap:wrap;padding:26px 0 6px}
.brand h1{
  margin:0;font-size:26px;letter-spacing:-.02em;font-weight:600;
  font-family:"Fraunces",Iowan Old Style,Georgia,serif;
}
.brand .sub{color:var(--mut);font-size:14px}
nav.tabs{display:flex;gap:4px;padding:10px 0 0;flex-wrap:wrap}
nav.tabs a{
  padding:9px 14px;border-radius:9px 9px 0 0;font-size:14.5px;font-weight:500;
  color:var(--mut);border:1px solid transparent;border-bottom:none;position:relative;top:1px;
}
nav.tabs a:hover{color:var(--fg);background:var(--line2);text-decoration:none}
nav.tabs a[aria-current="page"]{
  background:var(--bg);border-color:var(--line);color:var(--fg);
}
nav.tabs a .n{color:var(--faint);font-size:12px;margin-left:6px}

/* ---------- stats ---------- */
.stats{display:flex;gap:26px;flex-wrap:wrap;padding:18px 0 4px}
.stat .v{font-size:21px;font-weight:600;font-variant-numeric:tabular-nums;
  font-family:"Fraunces",Georgia,serif}
.stat .k{font-size:11.5px;text-transform:uppercase;letter-spacing:.08em;color:var(--faint)}

/* ---------- toolbar ---------- */
.toolbar{position:sticky;top:0;z-index:20;background:var(--bg);
  padding:14px 0 10px;border-bottom:1px solid var(--line);margin-bottom:18px}
.searchrow{display:flex;gap:8px;align-items:center}
#q{
  flex:1;min-width:0;padding:11px 13px;font-size:15px;border:1px solid var(--line);
  border-radius:10px;background:var(--panel);color:var(--fg);box-shadow:var(--shadow)
}
#q:focus{outline:2px solid var(--acc);outline-offset:-1px}
.btn{
  padding:10px 13px;font-size:13.5px;border:1px solid var(--line);border-radius:10px;
  background:var(--panel);color:var(--fg);cursor:pointer;white-space:nowrap
}
.btn:hover{border-color:var(--acc);color:var(--acc)}
.chips{display:flex;gap:6px;flex-wrap:wrap;margin-top:9px;align-items:center}
.chip{
  font-size:12.5px;padding:5px 11px;border-radius:20px;border:1px solid var(--line);
  background:var(--panel);color:var(--mut);cursor:pointer;user-select:none
}
.chip[aria-pressed="true"]{background:var(--acc-soft);border-color:var(--acc);color:var(--acc);font-weight:600}
.chip .c{opacity:.6;font-size:11px;margin-left:4px}
.spacer{flex:1}
select.sort{
  font-size:13px;padding:6px 9px;border-radius:9px;border:1px solid var(--line);
  background:var(--panel);color:var(--fg)
}
#count{color:var(--mut);font-size:13px;padding:8px 0 0;min-height:20px}

/* ---------- conversation cards ---------- */
.conv{
  background:var(--panel);border:1px solid var(--line);border-radius:var(--r);
  margin:0 0 14px;box-shadow:var(--shadow);overflow:hidden
}
.conv > h2{
  margin:0;padding:15px 18px 12px;font-size:16px;font-weight:600;line-height:1.35;
  display:flex;gap:10px;align-items:baseline;flex-wrap:wrap;
  font-family:"Fraunces",Georgia,serif
}
.conv > h2 .date{font-size:12px;color:var(--faint);font-weight:400;font-family:inherit}
.conv > h2 .ct{
  font-size:11.5px;color:var(--mut);border:1px solid var(--line);border-radius:20px;
  padding:1px 9px;font-weight:500;font-family:-apple-system,sans-serif
}
details.sum{border-top:1px solid var(--line2);background:var(--line2)}
details.sum > summary{
  cursor:pointer;padding:9px 18px;font-size:12.5px;color:var(--mut);
  list-style:none;user-select:none
}
details.sum > summary::-webkit-details-marker{display:none}
details.sum > summary::before{content:"▸ ";color:var(--faint)}
details.sum[open] > summary::before{content:"▾ "}
details.sum .body{padding:2px 18px 15px;font-size:14px;color:var(--mut);line-height:1.62;
  max-width:74ch;white-space:pre-wrap}

ul.files{list-style:none;margin:0;padding:0}
ul.files > li{
  display:flex;align-items:center;gap:10px;padding:9px 18px;
  border-top:1px solid var(--line2);font-size:14.5px;min-width:0
}
ul.files > li:hover{background:var(--line2)}
.ext{
  flex:none;font-size:9.5px;font-weight:700;text-transform:uppercase;letter-spacing:.05em;
  width:44px;text-align:center;padding:3px 0;border-radius:5px;
  background:var(--line2);color:var(--mut);border:1px solid var(--line)
}
.e-html{background:#e8f0fb;color:#2a5ea8;border-color:#cfe0f5}
.e-md{background:#eaf5ec;color:#2f6b4f;border-color:#d3e9d9}
.e-svg{background:#f6ecfa;color:#7a3f97;border-color:#e8d6f0}
.e-py{background:#fdf3dd;color:#8a6516;border-color:#f3e3bd}
.e-js,.e-jsx{background:#fdf0e6;color:#a35a1e;border-color:#f5ddc8}
:root[data-theme="dark"] .ext,
:root:not([data-theme="light"]) .ext{background:var(--line2);color:var(--mut);border-color:var(--line)}
@media(prefers-color-scheme:dark){:root:not([data-theme="light"]) .ext{
  background:var(--line2);color:var(--mut);border-color:var(--line)}}

.fname{flex:1;min-width:0;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.badges{display:flex;gap:5px;flex:none}
.b{font-size:10px;padding:2px 7px;border-radius:20px;border:1px solid var(--line);color:var(--mut)}
.b.ok{color:var(--ok);border-color:currentColor}
.b.warn{color:var(--warn);border-color:currentColor}
.sz{flex:none;color:var(--faint);font-size:11.5px;font-variant-numeric:tabular-nums;width:62px;text-align:right}
.hide{display:none !important}
.snippet{padding:0 18px 10px 72px;font-size:12.5px;color:var(--mut);line-height:1.55}
.snippet mark{background:var(--acc-soft);color:var(--acc);padding:0 2px;border-radius:3px}

.empty{padding:60px 20px;text-align:center;color:var(--mut)}
footer{border-top:1px solid var(--line);margin-top:40px;padding:22px 0 60px;
  color:var(--faint);font-size:13px}

/* ---------- viewer pages ---------- */
.vhead{border-bottom:1px solid var(--line);background:var(--panel);padding:16px 0}
.vhead .crumb{font-size:13px;color:var(--mut);margin-bottom:5px}
.vhead h1{margin:0;font-size:20px;font-family:"Fraunces",Georgia,serif;font-weight:600;
  word-break:break-word}
.vhead .meta{margin-top:8px;display:flex;gap:8px;flex-wrap:wrap;align-items:center}
.doc{max-width:78ch;margin:34px auto 90px;padding:0 20px;font-size:16.5px;line-height:1.72}
.doc h1,.doc h2,.doc h3,.doc h4{font-family:"Fraunces",Georgia,serif;line-height:1.28;
  margin:1.9em 0 .55em;font-weight:600}
.doc h1{font-size:1.75em}.doc h2{font-size:1.38em}.doc h3{font-size:1.14em}
.doc h1,.doc h2{border-bottom:1px solid var(--line);padding-bottom:.28em}
.doc p{margin:0 0 1.05em}
.doc ul,.doc ol{padding-left:1.4em;margin:0 0 1.05em}
.doc li{margin:.28em 0}
.doc blockquote{margin:1.2em 0;padding:.2em 0 .2em 1.1em;border-left:3px solid var(--acc);
  color:var(--mut);font-style:italic}
.doc table{border-collapse:collapse;width:100%;margin:1.3em 0;font-size:.92em;display:block;overflow-x:auto}
.doc th,.doc td{border:1px solid var(--line);padding:8px 11px;text-align:left;vertical-align:top}
.doc th{background:var(--line2);font-weight:600}
.doc code{font:13.5px/1.5 ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;
  background:var(--line2);padding:.14em .38em;border-radius:4px}
.doc pre{background:var(--line2);border:1px solid var(--line);border-radius:9px;
  padding:13px 15px;overflow-x:auto;margin:1.2em 0}
.doc pre code{background:none;padding:0;font-size:13px;line-height:1.55}
.doc img{max-width:100%;height:auto}
.doc hr{border:0;border-top:1px solid var(--line);margin:2em 0}

.codewrap{max-width:var(--maxw);margin:26px auto 90px;padding:0 20px}
.codewrap pre{background:var(--panel);border:1px solid var(--line);border-radius:11px;
  padding:16px 18px;overflow-x:auto;font:13px/1.6 ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;
  box-shadow:var(--shadow)}
.codewrap pre .lineno{color:var(--faint);user-select:none;padding-right:14px}

@media (max-width:600px){
  .brand h1{font-size:22px}
  .stats{gap:16px}
  .sz{display:none}
  ul.files > li{padding:10px 13px;gap:8px}
  .conv > h2{padding:13px 13px 10px}
  details.sum > summary,details.sum .body{padding-left:13px;padding-right:13px}
  .snippet{padding-left:13px}
  .doc{font-size:16px}
}
@media print{.toolbar,nav.tabs,footer,.btn{display:none}}
"""

JS = r"""
(function(){
  'use strict';
  var root=document.documentElement;

  /* ---- theme ---- */
  try{var t=localStorage.getItem('ca-theme'); if(t) root.setAttribute('data-theme',t);}catch(e){}
  var tb=document.getElementById('theme');
  if(tb) tb.addEventListener('click',function(){
    var cur=root.getAttribute('data-theme');
    var next = cur==='dark' ? 'light' : cur==='light' ? 'dark'
      : (window.matchMedia('(prefers-color-scheme:dark)').matches?'light':'dark');
    root.setAttribute('data-theme',next);
    try{localStorage.setItem('ca-theme',next);}catch(e){}
  });

  var q=document.getElementById('q');
  if(!q) return;                          /* viewer pages: theme only */

  var convs=[].slice.call(document.querySelectorAll('.conv'));
  var items=[].slice.call(document.querySelectorAll('ul.files > li'));
  var countEl=document.getElementById('count');
  var chips=[].slice.call(document.querySelectorAll('.chip[data-ext]'));
  var sortSel=document.getElementById('sort');
  var active=new Set();
  var index=null, indexLoading=false;

  function esc(s){return s.replace(/[&<>"]/g,function(c){
    return({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'})[c];});}

  /* ---- lazy full-text index ---- */
  function loadIndex(cb){
    if(index){cb();return;}
    if(indexLoading)return;
    indexLoading=true;
    fetch('search-index.json').then(function(r){return r.json();}).then(function(d){
      index={}; d.forEach(function(row){ index[row.k]=row.t; });
      indexLoading=false; cb();
    }).catch(function(){ indexLoading=false; index={}; cb(); });
  }

  function clearSnippets(){
    [].slice.call(document.querySelectorAll('.snippet')).forEach(function(n){n.remove();});
  }

  function snippetFor(li,term){
    if(!index)return;
    var body=index[li.dataset.k];
    if(!body)return;
    var i=body.toLowerCase().indexOf(term);
    if(i<0)return;
    var s=Math.max(0,i-70), e=Math.min(body.length,i+term.length+110);
    var txt=(s>0?'…':'')+body.slice(s,e).replace(/\s+/g,' ')+(e<body.length?'…':'');
    var d=document.createElement('div');
    d.className='snippet';
    d.innerHTML=esc(txt).replace(new RegExp('('+term.replace(/[.*+?^${}()|[\]\\]/g,'\\$&')+')','ig'),'<mark>$1</mark>');
    li.insertAdjacentElement('afterend',d);
  }

  function run(){
    var term=q.value.trim().toLowerCase();
    var deep = term.length>=3;
    clearSnippets();
    if(deep && !index){ loadIndex(run); }

    var shownFiles=0, shownConvs=0;
    convs.forEach(function(sec){
      var convHit = !term || sec.dataset.n.indexOf(term)>=0;
      var any=false;
      [].slice.call(sec.querySelectorAll('ul.files > li')).forEach(function(li){
        var extOk = active.size===0 || active.has(li.dataset.ext);
        var textOk = !term || convHit || li.dataset.n.indexOf(term)>=0;
        if(!textOk && deep && index){
          var body=index[li.dataset.k];
          if(body && body.toLowerCase().indexOf(term)>=0) textOk=true;
        }
        var show = extOk && textOk;
        li.classList.toggle('hide',!show);
        if(show){ any=true; shownFiles++;
          if(term && deep && index && li.dataset.n.indexOf(term)<0) snippetFor(li,term); }
      });
      sec.classList.toggle('hide',!any);
      if(any) shownConvs++;
    });

    countEl.textContent = (term||active.size)
      ? shownFiles.toLocaleString()+' file'+(shownFiles===1?'':'s')+' in '
        + shownConvs.toLocaleString()+' conversation'+(shownConvs===1?'':'s')
        + (deep?'  ·  searching contents':'')
      : '';
    var emp=document.getElementById('empty');
    if(emp) emp.classList.toggle('hide',shownFiles>0);
  }

  q.addEventListener('input',run);

  chips.forEach(function(ch){
    ch.addEventListener('click',function(){
      var e=ch.dataset.ext;
      if(active.has(e)){active.delete(e);ch.setAttribute('aria-pressed','false');}
      else{active.add(e);ch.setAttribute('aria-pressed','true');}
      run();
    });
  });

  /* ---- sorting ---- */
  if(sortSel){
    var parent=convs.length?convs[0].parentNode:null;
    var origConv=convs.slice();
    sortSel.addEventListener('change',function(){
      var v=sortSel.value;
      if(!parent)return;
      var arr=origConv.slice();
      if(v==='name') arr.sort(function(a,b){return a.dataset.n.localeCompare(b.dataset.n);});
      else if(v==='old') arr.sort(function(a,b){return (a.dataset.d||'').localeCompare(b.dataset.d||'');});
      else if(v==='new') arr.sort(function(a,b){return (b.dataset.d||'').localeCompare(a.dataset.d||'');});
      else if(v==='size') arr.sort(function(a,b){return (+b.dataset.sz)-(+a.dataset.sz);});
      else if(v==='count') arr.sort(function(a,b){return (+b.dataset.c)-(+a.dataset.c);});
      arr.forEach(function(s){parent.appendChild(s);});
      try{localStorage.setItem('ca-sort',v);}catch(e){}
    });
    try{var sv=localStorage.getItem('ca-sort');
      if(sv){sortSel.value=sv;sortSel.dispatchEvent(new Event('change'));}}catch(e){}
  }

  /* ---- expand / collapse all summaries ---- */
  var ex=document.getElementById('expand');
  if(ex) ex.addEventListener('click',function(){
    var ds=[].slice.call(document.querySelectorAll('details.sum'));
    var opening=!ds.every(function(d){return d.open;});
    ds.forEach(function(d){d.open=opening;});
    ex.textContent=opening?'Collapse all':'Expand all';
  });

  /* ---- keyboard ---- */
  document.addEventListener('keydown',function(e){
    if(e.key==='/'&&document.activeElement!==q){e.preventDefault();q.focus();q.select();}
    if(e.key==='Escape'&&document.activeElement===q){q.value='';run();q.blur();}
  });

  run();
})();
"""
