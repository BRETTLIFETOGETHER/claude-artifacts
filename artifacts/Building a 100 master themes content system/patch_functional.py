# -*- coding: utf-8 -*-
import re
O='/home/claude/site/out/'

# ---------- 1. signin: fix literal \u2014 ----------
h=open(O+'signin.html').read()
h=h.replace('</a> \\u2014 it takes','</a> \u2014 it takes')
open(O+'signin.html','w').write(h)

# ---------- 2. index: real campaigns everywhere ----------
h=open(O+'index.html').read()
if 'data.js' not in h:
    h=h.replace('<script src="cart.js"></script>','<script src="data.js"></script>\n<script src="cart.js"></script>')
# clickable cover CSS
h=h.replace('</style>','a.cov{color:inherit;text-decoration:none;display:block;}\n.cov .canvas{cursor:pointer;}\n</style>',1)

# cover() -> anchor with id
h=h.replace('''function cover(title, sub, ch, fmt){
  const [a,b]=HUE[ch];
  return `<div class="cov" style="--ca:${a};--cb:${b}">''',
'''function cover(title, sub, ch, fmt, id){
  const [a,b]=HUE[ch];
  return `<a class="cov" href="${id?('campaign.html?id='+id):'browse.html'}" style="--ca:${a};--cb:${b}">''')
h=h.replace('''      ${fmt?`<span class="fmt">${fmt}</span>`:''}
    </div></div>`;
}''','''      ${fmt?`<span class="fmt">${fmt}</span>`:''}
    </div></a>`;
}
function findC(title,theme){const D=window.CAMPAIGNS;
  return D.find(r=>r[0]===title)||D.find(r=>r[10]===(theme||title)&&r[8]===1)||D.find(r=>r[10]===(theme||title));}''')

# hero cluster -> real linked covers
old_cluster=h[h.index('/* hero cluster */'):h.index('/* originals row */')]
new_cluster='''/* hero cluster */
const HC=[['God Owns It All','God Owns It All'],['40 Days of Peace','Peace'],['Life Together','Life Together'],['The Generous Life','Generous Life'],['Rooted','Rooted']];
const cl=document.getElementById('cluster');
const cls=['c-a','c-b','c-c','c-d','c-e'];
HC.forEach((hx,i)=>{const r=findC(hx[0],hx[1]); if(!r)return;
  const d=document.createElement('a');d.className='cov '+cls[i];d.href='campaign.html?id='+r[9];
  const [ca,cb]=HUE[r[2]];
  d.innerHTML=`<div class="canvas" style="--ca:${ca};--cb:${cb}">
    <div class="tab"><b>40 DAY</b><span>CAMPAIGNS</span></div>
    <div class="ttl"><div class="nm">${r[0]}</div><div class="sb">${window.CATS[r[2]]}</div></div></div>`;
  cl.appendChild(d);});

'''
h=h.replace(old_cluster,new_cluster)

# originals row -> top flagship by popularity (dedup theme)
old_orig=h[h.index('/* originals row */'):h.index('/* audience category covers */')]
new_orig='''/* most popular this season: real flagships */
const seenTh=new Set();
const TOPPOP=window.CAMPAIGNS.filter(r=>r[8]===1).sort((a,b)=>b[6]-a[6])
  .filter(r=>{if(seenTh.has(r[10]))return false;seenTh.add(r[10]);return true;}).slice(0,12);
const rowA=document.getElementById('rowA');
TOPPOP.forEach(r=>rowA.insertAdjacentHTML('beforeend',cover(r[0],r[1],r[2],r[3],r[9])));

'''
h=h.replace(old_orig,new_orig)

# audience rows -> real theme flagships
old_cats=h[h.index('/* audience category covers */'):h.index("renderCats('groups');")]
new_cats='''/* audience category covers: real theme flagships */
const AUDSETS={
 groups:['Group Up','Belong','One Another','Never Alone','Life Together'],
 families:['Family Legacy','Passing Down Faith','Parenting on Purpose','Grandparent Legacy','Family Mission'],
 leaders:['Calling','Serving','Mentoring','Following Jesus','Stewarding Time']};
const CATLAB={groups:['New Groups','Belonging','One Another','Connection','Community'],
 families:['Legacy','Faith at Home','Parenting','Grandparents','Mission'],
 leaders:['Calling','Serving','Mentoring','Discipleship','Time']};
const catRow=document.getElementById('catRow');
function renderCats(k){
  catRow.innerHTML='';
  AUDSETS[k].forEach((th,i)=>{const r=findC(th,th); if(!r)return;
    const wrap=document.createElement('div');wrap.className='cat';
    wrap.innerHTML=`<div class="lab">${CATLAB[k][i]}</div>${cover(r[0],r[1],r[2],'',r[9])}`;
    catRow.appendChild(wrap);
  });
}
'''
h=h.replace(old_cats,new_cats)
open(O+'index.html','w').write(h)

# ---------- 3. campaign.html: Add to cart replaces Add to my plan; working Canva & editable export ----------
h=open(O+'campaign.html').read()
h=h.replace('<a class="btn btn-white" href="get-access.html">Add to my plan</a>',
            '<a class="btn btn-white" href="#" id="addbtn">Add to cart</a>')
h=h.replace('href="how-it-works.html#exports" style="font-size:13px;padding:9px 15px;">Open in Canva',
            'href="#" id="canvabtn" style="font-size:13px;padding:9px 15px;">Open in Canva')
h=h.replace('<div class="xnote">Import the PDF into Canva today · one-click integration in development</div>',
            '<div class="xnote">Downloads your editable file and opens Canva in a new tab — drop the file straight in. One-click integration in development.</div>')
h=h.replace('href="how-it-works.html#exports" style="font-size:13px;padding:9px 15px;">Export editable copy</a>',
            'href="#" id="docbtn" style="font-size:13px;padding:9px 15px;">Export editable copy (.doc)</a>')

# driver additions
h=h.replace("document.getElementById('startbtn').addEventListener('click',function(e){e.preventDefault();",
"""function selFmt(){const on=document.querySelector('#fmts .fmt.on');
 return on?on.textContent.replace(' Campaign','').replace(' Group',''):FMT;}
document.getElementById('addbtn').addEventListener('click',function(e){e.preventDefault();
 LT.add(ID,selFmt());LT.badge();
 this.textContent='Added to cart \\u2713';this.style.borderColor='var(--orange)';this.style.color='var(--orange)';});
function curriculumHTML(){
 const dev=Engine.devotional(C,'40-Day'), g=Engine.groupStudy(C), m=Engine.meta(C);
 let s='<h1>'+T+'</h1><p><i>'+S+'</i></p><p>'+window.CATS[CH]+' \\u00b7 '+THEME+' \\u00b7 Anchored in '+SCR+' (NIV)</p><hr>';
 dev.days.forEach(d=>{s+='<h2>'+d.dn+' \\u2014 '+d.title+'</h2>'
  +'<p><b>This week\\u2019s memory verse ('+d.mem.v+', KJV):</b> \\u201C'+d.mem.t+'\\u201D</p>'
  +'<p><b>Today\\u2019s reading:</b> '+d.scr+'</p>'+d.body
  +'<p><b>Pray:</b> <i>'+d.pray+'</i></p><p><b>Reflect &amp; respond:</b> '+d.q+'</p><p><b>One step today:</b> '+d.step+'</p><hr>';});
 s+='<h1>6-Week Group Series</h1>';
 g.sessions.forEach(x=>{s+='<h2>'+x.title+'</h2><p>'+x.focus+'</p><p><b>Open:</b> '+x.opener+'</p><p><b>Read together:</b> '+x.refs.join(' \\u00b7 ')+'</p><ol>'+x.qs.map(q=>'<li>'+q+'</li>').join('')+'</ol><p><b>Pray:</b> <i>'+x.pray+'</i></p><p><b>This week\\u2019s practice:</b> '+x.practice+'</p><hr>';});
 s+='<p style="font-size:10pt;color:#666;">Memory verses KJV (public domain) \\u00b7 daily reading references NIV \\u2014 NIV text ships under the Biblica license at launch \\u00b7 40daycampaigns.com</p>';
 return s;
}
function downloadDoc(){
 const html='<html xmlns:o="urn:schemas-microsoft-com:office:office" xmlns:w="urn:schemas-microsoft-com:office:word"><head><meta charset="utf-8"><title>'+T+'</title></head><body style="font-family:Georgia,serif;">'+curriculumHTML()+'</body></html>';
 const blob=new Blob(['\\ufeff'+html],{type:'application/msword'});
 const a=document.createElement('a');a.href=URL.createObjectURL(blob);
 a.download=T.replace(/[^\\w \\-&]/g,'')+' - Editable Curriculum.doc';
 document.body.appendChild(a);a.click();a.remove();
}
document.getElementById('docbtn').addEventListener('click',function(e){e.preventDefault();downloadDoc();
 this.textContent='Downloaded \\u2713';});
document.getElementById('canvabtn').addEventListener('click',function(e){e.preventDefault();
 downloadDoc();window.open('https://www.canva.com','_blank');});
document.getElementById('startbtn').addEventListener('click',function(e){e.preventDefault();""")
# startbtn now uses selFmt
h=h.replace(""" const on=document.querySelector('#fmts .fmt.on');
 const fmt=on?on.textContent.replace(' Campaign','').replace(' Group',''):FMT;
 LT.add(ID,fmt);location.href='cart.html';});""",
" LT.add(ID,selFmt());location.href='cart.html';});")
open(O+'campaign.html','w').write(h)

# ---------- 4. browse cards: Add to cart mini button ----------
h=open(O+'browse.html').read()
h=h.replace('</style>','''.addmini{position:absolute;right:10px;top:10px;z-index:3;font-family:'Hanken Grotesk';font-weight:800;font-size:11px;letter-spacing:.04em;background:rgba(255,255,255,.94);border:none;border-radius:999px;padding:7px 11px;cursor:pointer;color:var(--ink);opacity:0;transition:opacity .15s;box-shadow:0 6px 16px -8px rgba(0,0,0,.4);}
.cov:hover .addmini{opacity:1;}
.addmini:hover{background:var(--orange);color:#fff;}
.cov .canvas{position:relative;}
</style>''',1)
h=h.replace('''      <div class="tab"><b>${fmt.replace('-',' ').toUpperCase()}</b></div><div class="nm">${t}</div>
      ${flag?'<span class="flag">Flagship</span>':''}<span class="fmt">${fmt}</span></div>''',
'''      <div class="tab"><b>${fmt.replace('-',' ').toUpperCase()}</b></div><div class="nm">${t}</div>
      ${flag?'<span class="flag">Flagship</span>':''}<span class="fmt">${fmt}</span>
      <button class="addmini" data-id="${id}" data-fmt="${fmt}">+ Add to cart</button></div>''')
h=h.replace("document.getElementById('more').addEventListener('click'",
'''grid.addEventListener('click',function(e){
  const b=e.target.closest('.addmini');if(!b)return;
  e.preventDefault();e.stopPropagation();
  LT.add(b.dataset.id,b.dataset.fmt);LT.badge();
  b.textContent='Added \\u2713';b.style.opacity=1;setTimeout(()=>{b.textContent='+ Add to cart';},1400);
});
document.getElementById('more').addEventListener('click' ''')
open(O+'browse.html','w').write(h)

# ---------- 5. finder: Add to cart beside Preview ----------
h=open(O+'finder.html').read()
h=h.replace('''<a class="btn btn-white" href="campaign.html?id=${o.r[9]}" style="font-size:13px;padding:9px 15px;">Preview</a></div></div>`;''',
'''<a class="btn btn-white" href="campaign.html?id=${o.r[9]}" style="font-size:13px;padding:9px 15px;">Preview</a>
       <a class="btn btn-white addcart" data-id="${o.r[9]}" data-fmt="${o.r[3]}" href="#" style="font-size:13px;padding:9px 15px;">+ Add to cart</a></div></div>`;''')
h=h.replace('''<a class="btn btn-dark" href="campaign.html?id=${top.r[9]}">Preview campaign <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.6"><path d="M7 17 17 7M8 7h9v9"/></svg></a>''',
'''<a class="btn btn-dark" href="campaign.html?id=${top.r[9]}">Preview campaign <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.6"><path d="M7 17 17 7M8 7h9v9"/></svg></a>
          <a class="btn btn-white addcart" data-id="${top.r[9]}" data-fmt="${top.r[3]}" href="#">+ Add to cart</a>''')
h=h.replace('''<a class="btn btn-dark" href="campaign.html?id=${r[9]}">Preview ${r[0]}</a>''',
'''<a class="btn btn-dark" href="campaign.html?id=${r[9]}">Preview ${r[0]}</a>
      <a class="btn btn-white addcart" data-id="${r[9]}" data-fmt="${r[3]}" href="#">+ Add to cart</a>''')
h=h.replace('</body>','''<script>
document.addEventListener('click',function(e){
 const b=e.target.closest('.addcart');if(!b)return;
 e.preventDefault();LT.add(b.dataset.id,b.dataset.fmt);LT.badge();
 b.textContent='Added \\u2713';setTimeout(()=>{b.textContent='+ Add to cart';},1400);
});
</script>
</body>''')
open(O+'finder.html','w').write(h)
print('all patches applied')
