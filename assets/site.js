
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
