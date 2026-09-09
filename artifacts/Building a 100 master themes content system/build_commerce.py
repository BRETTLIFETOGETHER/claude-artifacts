# -*- coding: utf-8 -*-
import sys; sys.path.insert(0,'/home/claude/site')
from build_pages import shell, FOOT, ARROW
O='/home/claude/site/out/'

DOC_CSS="""
.doc{max-width:760px;margin:0 auto;background:#fff;border:1px solid var(--line);border-radius:18px;padding:44px 48px;box-shadow:0 24px 60px -34px rgba(22,52,79,.3);}
.doc .cover{text-align:center;padding:30px 0 36px;border-bottom:2px solid #E7DEC9;margin-bottom:30px;}
.doc .tabx{display:inline-block;font-family:'Hanken Grotesk';font-weight:800;font-size:11px;letter-spacing:.18em;color:#fff;background:var(--orange);padding:7px 18px;border-radius:999px;margin-bottom:18px;}
.doc h1{font-weight:900;font-size:34px;margin-bottom:8px;}
.doc .sub{color:var(--dim);font-size:15px;}
.dhead{display:flex;align-items:baseline;gap:14px;border-bottom:2px solid #E7DEC9;padding-bottom:10px;margin:34px 0 16px;}
.dhead .dn{font-family:'Hanken Grotesk';font-weight:800;font-size:12px;letter-spacing:.16em;text-transform:uppercase;color:var(--gold-d);}
.dhead .dl{margin-left:auto;font-family:'Hanken Grotesk';font-size:10.5px;letter-spacing:.12em;text-transform:uppercase;color:var(--faint);}
.dth{font-family:Georgia,serif;font-weight:600;font-size:24px;color:#1B2A4A;margin-bottom:14px;}
.dscr{background:#FBF7EE;border-left:4px solid var(--gold);border-radius:8px;padding:13px 18px;margin-bottom:16px;font-family:'Hanken Grotesk';font-weight:800;font-size:12px;letter-spacing:.06em;color:#7a5a12;text-transform:uppercase;}
.dlbl{font-family:'Hanken Grotesk';font-weight:800;font-size:11px;letter-spacing:.16em;text-transform:uppercase;color:#1B2A4A;margin:16px 0 6px;display:flex;align-items:center;gap:8px;}
.dlbl::before{content:"";width:14px;height:2px;background:var(--gold);}
.doc p{font-size:14px;line-height:1.7;color:#2C3E50;margin:0 0 10px;}
.dpray{font-style:italic;background:#F4EFE2;border-radius:8px;padding:12px 16px;font-size:13.5px;}
.dq{border:1.5px dashed #D8CBAE;border-radius:8px;padding:12px 16px;font-size:13.5px;}
.dstep{font-size:12.5px;color:#5A6B7B;}.dstep b{color:#1B2A4A;}
.docbar{max-width:760px;margin:0 auto 18px;display:flex;gap:10px;align-items:center;flex-wrap:wrap;}
.docbar .sp{margin-left:auto;font-size:12px;color:var(--faint);}
@media print{
 .navwrap,.docbar,footer{display:none!important;}
 body{background:#fff!important;}
 .doc{border:none;box-shadow:none;border-radius:0;padding:0;max-width:none;}
 .day{page-break-after:always;}
 .day:last-child{page-break-after:auto;}
}
"""

# ---------------- sample.html ----------------
sample = shell('Sample Devotional','',DOC_CSS) + """
<div class="wrap" style="padding-top:34px;">
<div class="docbar">
 <a class="btn btn-white" id="backlink" href="browse.html">&#8592; Back to campaign</a>
 <button class="btn btn-orange" onclick="window.print()">Download PDF <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.6"><path d="M12 3v12M7 11l5 5 5-5M4 21h16"/></svg></button>
 <span class="sp">In the print dialog, choose \u201cSave as PDF\u201d</span>
</div>
<div class="doc" id="doc"></div>
</div>
<script src="data.js"></script><script src="engine.js"></script><script src="cart.js"></script>
<script>
const P=new URLSearchParams(location.search);
const C=Engine.get(P.get('id'))||window.CAMPAIGNS[0];
document.getElementById('backlink').href='campaign.html?id='+C[9];
document.title=C[0]+' — Sample Devotional';
const dev=Engine.devotional(C,'40-Day');
const m=Engine.meta(C);
let h=`<div class="cover"><span class="tabx">${C[3].replace('-',' ').toUpperCase()} CAMPAIGN · SAMPLE</span>
 <h1>${C[0]}</h1><div class="sub">${C[1]}<br>Daily devotional · Days 1–3 sample · Anchored in ${m.scr} (NIV)</div></div>`;
dev.days.slice(0,3).forEach(d=>{
 h+=`<div class="day"><div class="dhead"><span class="dn">${d.dn}</span><span class="dl">${C[0]} · ${d.wk}</span></div>
 <div class="dth">${d.title}</div>
 <div class="dscr">Today\u2019s reading: ${d.scr}</div>
 <div class="dlbl">Reflect</div>${d.body}
 <div class="dlbl">Pray</div><p class="dpray">${d.pray}</p>
 <div class="dlbl">Reflect &amp; Respond</div><p class="dq">${d.q}</p>
 <div class="dlbl">One Step Today</div><p class="dstep">${d.step}</p></div>`;
});
h+=`<div style="text-align:center;margin-top:26px;font-family:'Hanken Grotesk';font-size:11px;letter-spacing:.1em;color:var(--faint);">SAMPLE · THE FULL ${dev.label.toUpperCase()} INCLUDES EVERY DAY, THE 6-SESSION GROUP STUDY &amp; SERMON OUTLINES · 40DAYCAMPAIGNS.COM</div>`;
document.getElementById('doc').innerHTML=h;
</script>
""" + FOOT
open(O+'sample.html','w').write(sample)

# ---------------- curriculum.html ----------------
curr = shell('Curriculum','',DOC_CSS+"""
.fmtpick{display:flex;gap:8px;flex-wrap:wrap;}
.fmtpick a{font-family:'Hanken Grotesk';font-weight:700;font-size:12.5px;background:#fff;border:1.5px solid var(--line);border-radius:999px;padding:8px 14px;}
.fmtpick a.on{border-color:var(--orange);color:var(--orange);}
.sess{margin:30px 0;padding:22px;background:#FBFAF6;border:1px solid #EFE8D8;border-radius:14px;}
.sess h3{font-weight:900;font-size:18px;margin-bottom:4px;}
.sess .focus{font-size:13px;color:var(--dim);margin-bottom:12px;}
.sess ol{margin:6px 0 12px;padding-left:20px;}
.sess li{font-size:13.5px;line-height:1.6;margin-bottom:5px;color:#2C3E50;}
@media print{.sess{page-break-inside:avoid;background:#fff;border:none;padding:0;margin:26px 0;}}
""") + """
<div class="wrap" style="padding-top:34px;">
<div class="docbar">
 <a class="btn btn-white" id="backlink" href="browse.html">&#8592; Back</a>
 <div class="fmtpick" id="fp"></div>
 <button class="btn btn-orange" onclick="window.print()">Download PDF <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.6"><path d="M12 3v12M7 11l5 5 5-5M4 21h16"/></svg></button>
 <span class="sp">Choose \u201cSave as PDF\u201d in the print dialog</span>
</div>
<div class="doc" id="doc"></div>
</div>
<script src="data.js"></script><script src="engine.js"></script><script src="cart.js"></script>
<script>
const P=new URLSearchParams(location.search);
const C=Engine.get(P.get('id'))||window.CAMPAIGNS[0];
const FMT=P.get('fmt')||C[3];
const m=Engine.meta(C);
document.getElementById('backlink').href=(document.referrer.indexOf('confirmation')>-1)?'confirmation.html':'campaign.html?id='+C[9];
document.title=C[0]+' — '+FMT+' Curriculum';
const FMTS=['7-Day','21-Day','30-Day','40-Day','6-Week'];
document.getElementById('fp').innerHTML=FMTS.map(f=>`<a href="curriculum.html?id=${C[9]}&fmt=${f}" class="${f===FMT?'on':''}">${f}</a>`).join('');
let h=`<div class="cover"><span class="tabx">${FMT.replace('-',' ').toUpperCase()} ${FMT==='6-Week'?'GROUP SERIES':'CAMPAIGN'} · COMPLETE CURRICULUM</span>
 <h1>${C[0]}</h1><div class="sub">${C[1]} · ${window.CATS[C[2]]} · ${C[10]}<br>Anchored in ${m.scr} (NIV) · Written for ${C[11].toLowerCase()}</div></div>`;

if(FMT==='6-Week'){
 const g=Engine.groupStudy(C);
 h+=`<p style="font-size:14px;"><b>How to use this series:</b> six leader-led sessions, 60–75 minutes each. No seminary required — the leader\u2019s only job is to keep the circle honest and keep it moving. Pair it with any daily format of <em>${C[0]}</em> for churchwide alignment.</p>`;
 g.sessions.forEach(s=>{
  h+=`<div class="sess day"><h3>${s.title}</h3><div class="focus">${s.focus}</div>
   <div class="dlbl">Open (10 min)</div><p>${s.opener}</p>
   <div class="dlbl">Read together</div><p>${s.refs.join(' · ')}</p>
   <div class="dlbl">Discuss (35 min)</div><ol>${s.qs.map(q=>'<li>'+q+'</li>').join('')}</ol>
   <div class="dlbl">Pray</div><p class="dpray">${s.pray}</p>
   <div class="dlbl">This week\u2019s practice</div><p class="dq">${s.practice}</p>
   <p style="font-size:12px;color:#5A6B7B;margin-top:10px;">${s.leader}</p></div>`;});
 const ser=Engine.sermons(C);
 h+=`<div class="dhead"><span class="dn">Appendix</span><span class="dl">Weekend alignment</span></div>
 <div class="dth">Six Sermon Outlines</div>`;
 ser.forEach(s=>{h+=`<div class="sess"><h3>${s.title}</h3><p><b>Text:</b> ${s.text}</p><p>${s.big}</p><ol>${s.points.map(p=>'<li>'+p+'</li>').join('')}</ol></div>`;});
}else{
 const dev=Engine.devotional(C,FMT);
 h+=`<p style="font-size:14px;"><b>How to use this journey:</b> one reading a day — Scripture, a short reflection, a prayer, one question, one small step. Missed a day? Grace covers it; just pick up where you are. Better with a partner or a group: the 6-Week study is included with your license.</p>`;
 dev.days.forEach(d=>{
  h+=`<div class="day"><div class="dhead"><span class="dn">${d.dn}</span><span class="dl">${C[0]} · ${d.wk}</span></div>
  <div class="dth">${d.title}</div>
  <div class="dscr">Today\u2019s reading: ${d.scr}</div>
  <div class="dlbl">Reflect</div>${d.body}
  <div class="dlbl">Pray</div><p class="dpray">${d.pray}</p>
  <div class="dlbl">Reflect &amp; Respond</div><p class="dq">${d.q}</p>
  <div class="dlbl">One Step Today</div><p class="dstep">${d.step}</p></div>`;});
 const k=Engine.launchKit(C);
 h+=`<div class="dhead"><span class="dn">Launch kit</span><span class="dl">For your team</span></div>
 <div class="dth">Launching ${C[0]}</div>
 <div class="dlbl">Pulpit announcement</div><p class="dpray">${k.announce}</p>
 <div class="dlbl">Communication sequence</div><ol style="padding-left:20px;">${k.emails.map(e=>'<li style="font-size:13.5px;margin-bottom:4px;">'+e+'</li>').join('')}</ol>
 <div class="dlbl">Celebration Sunday</div><p>${k.celebration}</p>`;
}
h+=`<div style="text-align:center;margin-top:28px;font-family:'Hanken Grotesk';font-size:10.5px;letter-spacing:.1em;color:var(--faint);">${C[0].toUpperCase()} · LICENSED FOR YOUR CONGREGATION · SCRIPTURE REFERENCES NIV · 40DAYCAMPAIGNS.COM</div>`;
document.getElementById('doc').innerHTML=h;
</script>
""" + FOOT
open(O+'curriculum.html','w').write(curr)

FORM_CSS="""
.cgrid{display:grid;grid-template-columns:1.15fr .85fr;gap:24px;align-items:start;}
@media(max-width:840px){.cgrid{grid-template-columns:1fr;}}
.field{margin-bottom:13px;}
.field label{font-family:'Hanken Grotesk';font-weight:700;font-size:12px;letter-spacing:.05em;text-transform:uppercase;color:var(--dim);display:block;margin-bottom:5px;}
.field input,.field select{width:100%;border:1px solid var(--line);border-radius:12px;padding:12px 14px;font-family:'Inter';font-size:14px;background:#fff;}
.row2{display:grid;grid-template-columns:1fr 1fr;gap:12px;}
.err{display:none;background:#FDF0EF;border:1px solid #F2C7C2;color:#9A2D22;border-radius:12px;padding:12px 15px;font-size:13.5px;margin:10px 0;}
.ok2{background:#EDF9F0;border:1px solid #BFE8CB;color:#1E6B34;border-radius:12px;padding:12px 15px;font-size:13.5px;margin:10px 0;}
.item{display:flex;gap:14px;background:#fff;border:1px solid var(--line);border-radius:16px;padding:16px;margin-bottom:12px;align-items:center;}
.item .cv{width:64px;flex:none;aspect-ratio:3/3.5;border-radius:9px;display:flex;align-items:center;justify-content:center;color:#fff;font-family:'Hanken Grotesk';font-weight:800;font-size:9px;text-align:center;padding:6px;line-height:1.1;}
.item .it{font-family:'Hanken Grotesk';font-weight:800;font-size:15px;}
.item .is{font-size:12px;color:var(--dim);}
.item select{border:1px solid var(--line);border-radius:9px;padding:7px 9px;font-size:12.5px;font-family:'Hanken Grotesk';font-weight:700;}
.item .rm{margin-left:auto;color:var(--faint);cursor:pointer;font-size:20px;line-height:1;background:none;border:none;}
.item .rm:hover{color:#C8484C;}
.item .pr{font-family:'Hanken Grotesk';font-weight:900;font-size:15px;min-width:64px;text-align:right;}
.sumline{display:flex;justify-content:space-between;font-size:14px;padding:7px 0;}
.sumline.total{font-family:'Hanken Grotesk';font-weight:900;font-size:18px;border-top:2px solid var(--line);margin-top:8px;padding-top:12px;}
.paytabs{display:flex;gap:8px;margin-bottom:14px;}
.paytab{font-family:'Hanken Grotesk';font-weight:700;font-size:13px;padding:9px 16px;border-radius:999px;border:1.5px solid var(--line);background:#fff;cursor:pointer;}
.paytab.on{border-color:var(--orange);color:var(--orange);}
.demo{background:#FFF7E8;border:1px solid #F2DFB4;color:#7A5A12;border-radius:12px;padding:11px 15px;font-size:12.5px;margin-bottom:16px;}
"""

CATHEX={1:['#7B5FE0','#3F2E86'],2:['#4F86E0','#26417F'],3:['#C8484C','#7E2326'],4:['#E0703F','#8A3A1E'],5:['#E8A52E','#9A6810'],
6:['#36A85E','#176233'],7:['#16A88F','#0C5A4E'],8:['#E2542F','#8A2A14'],9:['#5A6B8C','#2E3A52'],10:['#C99A3C','#7E601C']}
import json
HEXJS='const CATHEX='+json.dumps(CATHEX)+';'

# ---------------- cart.html ----------------
cart = shell('Your Cart','',FORM_CSS) + """
<div class="wrap">
<header class="head"><span class="eb">Your cart</span><h1>Ready when you are</h1>
<p>Each campaign is a one-time $199 whole-church license — every format, the 6-session group study, sermon outlines, launch kit, and congregation print rights.</p></header>
<section class="section"><div class="cgrid">
<div id="items"></div>
<div class="card" style="background:#fff;border:1px solid var(--line);border-radius:18px;padding:22px;">
 <h3 style="font-weight:900;font-size:17px;margin-bottom:10px;">Order summary</h3>
 <div id="sum"></div>
 <a class="btn btn-orange" href="checkout.html" id="co" style="width:100%;justify-content:center;margin-top:14px;">Check out """+ARROW+"""</a>
 <a class="btn btn-white" href="browse.html" style="width:100%;justify-content:center;margin-top:8px;">Keep browsing</a>
 <p style="font-size:12px;color:var(--faint);margin-top:12px;">Considering several campaigns? <a href="pricing.html" style="color:var(--orange);font-weight:700;">All Access</a> covers the whole 10,000+ library from $49/mo.</p>
</div>
</div></section>
</div>
<script src="data.js"></script><script src="cart.js"></script>
<script>
"""+HEXJS+"""
const FMTS=['40-Day','30-Day','21-Day','7-Day','6-Week'];
function draw(){
 const c=LT.cart(); const el=document.getElementById('items');
 if(!c.length){el.innerHTML='<div style="background:#fff;border:1px solid var(--line);border-radius:16px;padding:34px;text-align:center;color:var(--dim);"><b style="font-family:\\'Hanken Grotesk\\';color:var(--ink);display:block;margin-bottom:6px;">Your cart is empty</b>Browse 10,000+ campaigns or take the Finder for a guided pick.<div style="margin-top:14px;"><a class="btn btn-orange" href="browse.html">Browse campaigns</a> <a class="btn btn-white" href="finder.html">Take the Finder</a></div></div>';
  document.getElementById('co').style.display='none';}
 else{
  el.innerHTML=c.map((x,i)=>{const r=LT.row(x.id)||[x.id,'',1];const[a,b]=CATHEX[r[2]]||CATHEX[1];
   return `<div class="item"><div class="cv" style="background:linear-gradient(160deg,${a},${b})">${r[0]}</div>
    <div><div class="it">${r[0]}</div><div class="is">${window.CATS[r[2]]} · ${r[10]}</div>
     <select onchange="LT.setFmt(${i},this.value);draw()">${FMTS.map(f=>`<option ${f===x.fmt?'selected':''}>${f}</option>`).join('')}</select></div>
    <div class="pr">$${LT.PRICE}</div>
    <button class="rm" title="Remove" onclick="LT.remove(${i});draw()">×</button></div>`;}).join('');
  document.getElementById('co').style.display='';
 }
 document.getElementById('sum').innerHTML=`
  <div class="sumline"><span>${c.length} campaign license${c.length===1?'':'s'}</span><span>$${LT.total()}</span></div>
  <div class="sumline"><span>All formats &amp; group study</span><span>Included</span></div>
  <div class="sumline"><span>Congregation print rights</span><span>Included</span></div>
  <div class="sumline total"><span>Total</span><span>$${LT.total()}</span></div>`;
 LT.badge();
}
draw();
</script>
""" + FOOT
open(O+'cart.html','w').write(cart)

# ---------------- checkout.html ----------------
checkout = shell('Checkout','',FORM_CSS) + """
<div class="wrap">
<header class="head"><span class="eb">Checkout</span><h1>Almost there</h1></header>
<section class="section"><div class="cgrid">
<div class="card" style="background:#fff;border:1px solid var(--line);border-radius:18px;padding:24px;">
 <div class="demo"><b>Launch preview:</b> payment processing goes live with the platform — no card will be charged today. Complete checkout to receive your full curriculum downloads immediately.</div>
 <h3 style="font-weight:900;font-size:16px;margin-bottom:12px;">Billing details</h3>
 <div class="row2"><div class="field"><label>Full name</label><input id="bn" placeholder="Pastor Sam Rivera"></div>
 <div class="field"><label>Email (for receipts)</label><input id="be" placeholder="sam@yourchurch.org"></div></div>
 <div class="row2"><div class="field"><label>Church / organization</label><input id="bc" placeholder="Grace Community Church"></div>
 <div class="field"><label>ZIP / postal code</label><input id="bz" placeholder="92688"></div></div>
 <h3 style="font-weight:900;font-size:16px;margin:18px 0 12px;">Payment method</h3>
 <div class="paytabs">
  <button class="paytab on" data-p="card">Card</button>
  <button class="paytab" data-p="paypal">PayPal</button>
  <button class="paytab" data-p="invoice">Invoice my church</button>
 </div>
 <div id="pay-card">
  <div class="field"><label>Card number</label><input id="cardn" inputmode="numeric" placeholder="4242 4242 4242 4242"></div>
  <div class="row2"><div class="field"><label>Expiry</label><input placeholder="MM / YY"></div>
  <div class="field"><label>CVC</label><input placeholder="123"></div></div>
 </div>
 <div id="pay-paypal" style="display:none;"><div class="field"><label>PayPal email</label><input placeholder="you@yourchurch.org"></div>
  <p style="font-size:12.5px;color:var(--dim);">You\u2019ll confirm in PayPal after platform launch; today this completes as a preview order.</p></div>
 <div id="pay-invoice" style="display:none;"><div class="field"><label>Accounts-payable email</label><input placeholder="finance@yourchurch.org"></div>
  <div class="field"><label>PO number (optional)</label><input placeholder="PO-2026-041"></div>
  <p style="font-size:12.5px;color:var(--dim);">Net-30 invoice, emailed within one business day at launch.</p></div>
 <div class="err" id="err"></div>
 <button class="btn btn-orange" id="place" style="width:100%;justify-content:center;margin-top:8px;">Complete order """+ARROW+"""</button>
</div>
<div class="card" style="background:#fff;border:1px solid var(--line);border-radius:18px;padding:22px;">
 <h3 style="font-weight:900;font-size:16px;margin-bottom:10px;">Your order</h3>
 <div id="mini"></div><div id="sum"></div>
 <p style="font-size:12px;color:var(--faint);margin-top:12px;">30-day guarantee on everything. Licenses cover use within your congregation.</p>
</div>
</div></section>
</div>
<script src="data.js"></script><script src="cart.js"></script>
<script>
document.querySelectorAll('.paytab').forEach(t=>t.addEventListener('click',()=>{
 document.querySelectorAll('.paytab').forEach(x=>x.classList.remove('on'));t.classList.add('on');
 ['card','paypal','invoice'].forEach(p=>document.getElementById('pay-'+p).style.display=(t.dataset.p===p?'':'none'));}));
function draw(){const c=LT.cart();
 if(!c.length){location.href='cart.html';return;}
 document.getElementById('mini').innerHTML=c.map(x=>`<div class="sumline"><span>${LT.title(x.id)} <span style="color:var(--faint)">· ${x.fmt}</span></span><span>$${LT.PRICE}</span></div>`).join('');
 document.getElementById('sum').innerHTML=`<div class="sumline total"><span>Total</span><span>$${LT.total()}</span></div>`;}
draw();
document.getElementById('place').addEventListener('click',()=>{
 const bn=document.getElementById('bn').value.trim(), be=document.getElementById('be').value.trim();
 const err=document.getElementById('err');
 if(!bn||!be){err.textContent='Please add your name and email so we can attach your license.';err.style.display='block';return;}
 LT.placeOrder({name:bn,email:be,church:document.getElementById('bc').value,method:document.querySelector('.paytab.on').dataset.p});
 location.href='confirmation.html';
});
</script>
""" + FOOT
open(O+'checkout.html','w').write(checkout)

# ---------------- confirmation.html ----------------
conf = shell('Order Confirmed','',FORM_CSS+"""
.dl{display:flex;gap:8px;flex-wrap:wrap;margin-top:10px;}
.dl a{font-family:'Hanken Grotesk';font-weight:700;font-size:12px;background:var(--ink);color:#fff;border-radius:999px;padding:8px 13px;}
.dl a:hover{background:#000;}
""") + """
<div class="wrap">
<header class="head"><span class="eb">Order confirmed</span><h1 id="hd">Thank you!</h1>
<p id="sub">Your campaign licenses are active. Download any format below — each opens the complete curriculum, ready to print or save as PDF.</p></header>
<section class="section" style="max-width:820px;">
<div id="list"></div>
<div class="card" style="background:#FBF7EE;border:1px solid #EFE3C8;border-radius:16px;padding:18px 22px;margin-top:6px;">
 <b style="font-family:'Hanken Grotesk';">What\u2019s next:</b> <span style="font-size:14px;">pick your launch Sunday, recruit hosts three weeks out, and start everyone on Day 1 together. The launch kit is included at the end of every daily-format download. Questions? <a href="contact.html" style="color:var(--orange);font-weight:700;">We\u2019re here.</a></span>
</div>
<div style="margin-top:18px;display:flex;gap:10px;"><a class="btn btn-white" href="account.html">View my account</a><a class="btn btn-orange" href="browse.html">Browse more campaigns</a></div>
</section>
</div>
<script src="data.js"></script><script src="cart.js"></script>
<script>
"""+HEXJS+"""
const o=LT.lastOrder();
const FMTS=['40-Day','30-Day','21-Day','7-Day','6-Week'];
if(!o){document.getElementById('hd').textContent='No recent order found';
 document.getElementById('sub').innerHTML='Your cart is waiting — <a href="cart.html" style="color:var(--orange);font-weight:700;">head back to it</a> to complete checkout.';
 document.getElementById('list').innerHTML='';}
else{
 document.getElementById('hd').textContent='Thank you, '+(o.bill.name.split(' ')[0]||'friend')+'!';
 document.getElementById('sub').innerHTML=`Order <b>${o.num}</b> · ${o.date} · ${o.items.length} campaign license${o.items.length===1?'':'s'} · $${o.total}. Download any format below.`;
 document.getElementById('list').innerHTML=o.items.map(x=>{const r=LT.row(x.id);const[a,b]=CATHEX[r[2]];
  return `<div class="item" style="align-items:flex-start;"><div class="cv" style="background:linear-gradient(160deg,${a},${b})">${r[0]}</div>
   <div style="flex:1;"><div class="it">${r[0]}</div><div class="is">${window.CATS[r[2]]} · ${r[10]} · anchored in ${r[13]} (NIV)</div>
   <div class="dl">${FMTS.map(f=>`<a href="curriculum.html?id=${x.id}&fmt=${f}" ${f===x.fmt?'style="background:var(--orange)"':''}>${f} ↓</a>`).join('')}</div></div></div>`;}).join('');
}
</script>
""" + FOOT
open(O+'confirmation.html','w').write(conf)

# ---------------- signup.html ----------------
signup = shell('Create Account','',FORM_CSS) + """
<div class="wrap">
<header class="head"><span class="eb">Create your account</span><h1>Join in about thirty seconds</h1>
<p>Your account saves your cart, keeps your orders re-downloadable, and locks founding-church pricing. (Accounts live in this browser today and sync to the cloud at platform launch.)</p></header>
<section class="section"><div class="cgrid">
<div class="card" style="background:#fff;border:1px solid var(--line);border-radius:18px;padding:24px;">
 <div class="row2"><div class="field"><label>Full name</label><input id="sn" placeholder="Pastor Sam Rivera"></div>
 <div class="field"><label>Church / organization</label><input id="sc" placeholder="Grace Community Church"></div></div>
 <div class="field"><label>Email</label><input id="se" type="email" placeholder="sam@yourchurch.org"></div>
 <div class="row2"><div class="field"><label>Password</label><input id="sp" type="password" placeholder="8+ characters"></div>
 <div class="field"><label>Weekly attendance</label><select id="ss"><option>Under 100</option><option>100 – 250</option><option>251 – 500</option><option>501 – 1,000</option><option>Over 1,000 / multisite</option></select></div></div>
 <div class="err" id="err"></div>
 <button class="btn btn-orange" id="go" style="width:100%;justify-content:center;">Create account """+ARROW+"""</button>
 <p style="font-size:13px;color:var(--dim);margin-top:12px;">Already have one? <a href="signin.html" style="color:var(--orange);font-weight:700;">Sign in</a></p>
</div>
<div><div class="card" style="background:#fff;border:1px solid var(--line);border-radius:18px;padding:20px;margin-bottom:14px;"><h3 style="font-weight:900;font-size:15px;">Founding-church perks</h3><p style="font-size:13.5px;color:var(--ink-2);">Launch pricing locked for life, first pick of pastor-branded slots, and a hands-on launch coaching call.</p></div>
<div class="card" style="background:#fff;border:1px solid var(--line);border-radius:18px;padding:20px;"><h3 style="font-weight:900;font-size:15px;">Private by design</h3><p style="font-size:13.5px;color:var(--ink-2);">Today your details stay on this device. Nothing is sent anywhere until cloud accounts launch — and you\u2019ll opt in then.</p></div></div>
</div></section>
</div>
<script src="data.js"></script><script src="cart.js"></script>
<script>
document.getElementById('go').addEventListener('click',()=>{
 const v=id=>document.getElementById(id).value.trim();
 const err=document.getElementById('err');
 if(!v('sn')||!v('se')||v('sp').length<8){err.textContent=v('sp').length<8?'Password needs at least 8 characters.':'Please fill in your name and email.';err.style.display='block';return;}
 const r=LT.signup({name:v('sn'),church:v('sc'),email:v('se').toLowerCase(),pw:v('sp'),size:v('ss')});
 if(!r.ok){err.textContent=r.msg;err.style.display='block';return;}
 location.href='account.html';
});
</script>
""" + FOOT
open(O+'signup.html','w').write(signup)

# ---------------- account.html ----------------
account = shell('My Account','',FORM_CSS+"""
.dl{display:flex;gap:6px;flex-wrap:wrap;margin-top:8px;}
.dl a{font-family:'Hanken Grotesk';font-weight:700;font-size:11.5px;background:var(--ink);color:#fff;border-radius:999px;padding:7px 12px;}
""") + """
<div class="wrap">
<header class="head"><span class="eb">My account</span><h1 id="hi">Welcome</h1><p id="who"></p></header>
<section class="section"><div class="cgrid">
<div>
 <h2 style="font-weight:900;font-size:20px;margin-bottom:12px;">Your orders</h2>
 <div id="orders"></div>
</div>
<div>
 <div class="card" style="background:#fff;border:1px solid var(--line);border-radius:18px;padding:20px;margin-bottom:14px;">
  <h3 style="font-weight:900;font-size:15px;margin-bottom:8px;">Account details</h3>
  <div id="det" style="font-size:13.5px;color:var(--ink-2);line-height:1.8;"></div>
  <button class="btn btn-white" style="margin-top:12px;" onclick="LT.signout()">Sign out</button>
 </div>
 <div class="card" style="background:#fff;border:1px solid var(--line);border-radius:18px;padding:20px;">
  <h3 style="font-weight:900;font-size:15px;">Your tier</h3>
  <p style="font-size:13.5px;color:var(--ink-2);" id="tier"></p>
  <a class="btn btn-orange" href="pricing.html" style="margin-top:8px;">See All Access</a>
 </div>
</div>
</div></section>
</div>
<script src="data.js"></script><script src="cart.js"></script>
<script>
const u=LT.user();
if(!u){location.href='signin.html';}
else{
 document.getElementById('hi').textContent='Welcome back, '+u.name.split(' ')[0];
 document.getElementById('who').textContent=(u.church?u.church+' · ':'')+u.email;
 document.getElementById('det').innerHTML=`<b>${u.name}</b><br>${u.church||'—'}<br>${u.email}<br>Attendance: ${u.size||'—'}`;
 const P={'Under 100':'$49/mo ($490/yr)','100 – 250':'$89/mo ($890/yr)','251 – 500':'$149/mo ($1,490/yr)','501 – 1,000':'$249/mo ($2,490/yr)'};
 document.getElementById('tier').textContent='At '+(u.size||'your size')+', All Access is '+(P[u.size]||'custom network pricing')+' for the entire 10,000+ library.';
 const os=LT.orders(); const FMTS=['40-Day','30-Day','21-Day','7-Day','6-Week'];
 document.getElementById('orders').innerHTML= os.length? os.map(o=>`
  <div class="item" style="align-items:flex-start;"><div style="flex:1;">
   <div class="it">${o.num} <span style="font-weight:400;color:var(--faint);font-size:12px;">· ${o.date} · $${o.total}</span></div>
   ${o.items.map(x=>`<div style="margin-top:8px;"><div class="is" style="color:var(--ink);font-weight:600;">${LT.title(x.id)}</div>
    <div class="dl">${FMTS.map(f=>`<a href="curriculum.html?id=${x.id}&fmt=${f}">${f} ↓</a>`).join('')}</div></div>`).join('')}
  </div></div>`).join('') :
  '<div style="background:#fff;border:1px solid var(--line);border-radius:16px;padding:26px;color:var(--dim);">No orders yet — <a href="browse.html" style="color:var(--orange);font-weight:700;">find your first campaign</a>.</div>';
}
</script>
""" + FOOT
open(O+'account.html','w').write(account)
print('7 pages built')
