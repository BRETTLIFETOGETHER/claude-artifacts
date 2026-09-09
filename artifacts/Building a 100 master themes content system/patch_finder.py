# -*- coding: utf-8 -*-
import re
p='/home/claude/site/out/finder.html'
f=open(p).read()

NEW = r"""<script src="data.js"></script>
<script>
const HUE={1:['var(--c1a)','var(--c1b)'],2:['var(--c2a)','var(--c2b)'],3:['var(--c3a)','var(--c3b)'],4:['var(--c4a)','var(--c4b)'],
5:['var(--c5a)','var(--c5b)'],6:['var(--c6a)','var(--c6b)'],7:['var(--c7a)','var(--c7b)'],8:['var(--c8a)','var(--c8b)'],9:['var(--c9a)','var(--c9b)'],10:['var(--c10a)','var(--c10b)']};
const CHNAME=window.CATS;
const SEAS={new:'New Year',lent:'Lent & Easter',fall:'Fall kickoff',advent:'Advent & Christmas',yearend:'year-end giving',any:'any season'};
const OUTL={groups:'launch and strengthen groups',generosity:'grow generosity',emotional:'bring peace & emotional health',discipleship:'deepen discipleship',outreach:'mobilize outreach'};
// row: [title,sub,cat,fmt,seasons[],outcomes[],pop,new,flag,id,theme,audience,event,scripture]
const DATA=window.CAMPAIGNS;

/* ---- questions (6) ---- */
const Q=[
 {key:'outcome',h:'What do you most want to happen?',sub:'Pick the change you\u2019re hoping for in your church.',opts:[
   ['groups','Launch or strengthen groups','Get people into real community','var(--c5a)','M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2M9 11a4 4 0 1 0 0-8 4 4 0 0 0 0 8zM23 21v-2a4 4 0 0 0-3-3.9'],
   ['generosity','Grow generosity','Open hands, kingdom giving','var(--c6a)','M12 17v5M9 10.8V5a3 3 0 0 1 6 0v5.8a4 4 0 1 1-6 0z'],
   ['emotional','Bring peace & healing','Care for anxious, weary hearts','var(--c3a)','M20.8 5.6a5.5 5.5 0 0 0-7.8 0L12 6.6l-1-1a5.5 5.5 0 0 0-7.8 7.8L12 22l8.8-8.6a5.5 5.5 0 0 0 0-7.8z'],
   ['discipleship','Deepen discipleship','A closer walk with Christ','var(--c1a)','M4 5a2 2 0 0 1 2-2h6v16H6a2 2 0 0 0-2 2zM20 5a2 2 0 0 0-2-2h-6v16h6a2 2 0 0 1 2 2z'],
   ['outreach','Mobilize outreach','Reach the community','var(--c8a)','M12 2a10 10 0 1 0 0 20 10 10 0 0 0 0-20zM2 12h20M12 2a15 15 0 0 1 0 20M12 2a15 15 0 0 0 0 20'],
 ]},
 {key:'audience',h:'Who is this campaign mainly for?',sub:'We\u2019ll surface the right editions too.',opts:[
   ['church','The whole church','One movement, everyone together','var(--c9a)','M3 21h18M5 21V8l7-5 7 5v13M9 21v-5h6v5'],
   ['families','Families & the home','Parents, kids, next-gen faith','var(--c4a)','M9 21v-6h6v6M3 10l9-7 9 7v9a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z'],
   ['leaders','Leaders & staff','Develop your team','var(--c7a)','M3 3v18h18M7 14l4-4 3 3 5-6'],
   ['groups','A small-group season','Curriculum for groups','var(--c5a)','M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2M9 11a4 4 0 1 0 0-8 4 4 0 0 0 0 8z'],
 ]},
 {key:'feel',h:'Where is your church right now?',sub:'This helps us match the tone.',opts:[
   ['vision','Ready for fresh vision','Energy, momentum, a next step','var(--c9a)','M12 2l2.4 5 5.6.8-4 3.9 1 5.5L12 15.8 6 18.2l1-5.5-4-3.9 5.6-.8z'],
   ['hard','Walking through something hard','Grief, anxiety, weariness','var(--c3a)','M20.8 5.6a5.5 5.5 0 0 0-7.8 0L12 6.6l-1-1a5.5 5.5 0 0 0-7.8 7.8L12 22l8.8-8.6a5.5 5.5 0 0 0 0-7.8z'],
   ['deeper','Hungry to go deeper','Ready to grow in the Word','var(--c1a)','M4 5a2 2 0 0 1 2-2h6v16H6a2 2 0 0 0-2 2z'],
   ['reach','Wanting to reach out','Turn outward to the community','var(--c8a)','M12 2a10 10 0 1 0 0 20 10 10 0 0 0 0-20zM2 12h20'],
   ['belong','Craving connection','Build belonging & community','var(--c5a)','M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2M9 11a4 4 0 1 0 0-8'],
 ]},
 {key:'season',h:'When are you planning to launch?',sub:'Campaigns can auto-surface for the season.',opts:[
   ['new','New Year','January reset & prayer','var(--c3a)','M12 2v4M12 18v4M2 12h4M18 12h4M12 8a4 4 0 1 0 0 8 4 4 0 0 0 0-8z'],
   ['lent','Lent & Easter','The road to resurrection','var(--c2a)','M12 2v20M6 8h12'],
   ['fall','Fall kickoff','Launch the ministry year','var(--c5a)','M12 2C8 6 6 9 6 13a6 6 0 0 0 12 0c0-4-2-7-6-11z'],
   ['yearend','Year-end giving','Generosity season','var(--c6a)','M20 12v8H4v-8M2 7h20v5H2zM12 22V7M12 7S9 2 6.5 3.5 8 7 12 7zM12 7s3-5 5.5-3.5S16 7 12 7z'],
   ['advent','Advent & Christmas','Waiting on the King','var(--c7a)','M12 2l2.4 5 5.6.8-4 3.9 1 5.5L12 15.8 6 18.2l1-5.5-4-3.9 5.6-.8z'],
   ['any','No particular season','Evergreen, launch anytime','var(--c1a)','M12 6v6l4 2M12 2a10 10 0 1 0 0 20 10 10 0 0 0 0-20z'],
 ]},
 {key:'format',h:'How long can your church commit?',sub:'Every campaign comes in multiple lengths.',opts:[
   ['7-Day','7 days','A short, high-energy week','var(--c8a)','M12 6v6l4 2M12 2a10 10 0 1 0 0 20 10 10 0 0 0 0-20z'],
   ['21-Day','21 days','Enough to form a habit','var(--c5a)','M12 6v6l4 2M12 2a10 10 0 1 0 0 20 10 10 0 0 0 0-20z'],
   ['30-Day','30 days','A clean calendar month','var(--c2a)','M8 2v4M16 2v4M3 9h18M5 4h14a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2z'],
   ['40-Day','40 days','A full churchwide movement','var(--c6a)','M12 6v6l4 2M12 2a10 10 0 1 0 0 20 10 10 0 0 0 0-20z'],
   ['6-Week','A 6-week group series','Leader-led small groups','var(--c7a)','M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2M9 11a4 4 0 1 0 0-8 4 4 0 0 0 0 8z'],
   ['any','Not sure yet','Show me the best fit','var(--c9a)','M9.1 9a3 3 0 1 1 5.8 1c0 2-3 3-3 3M12 17h.01M12 2a10 10 0 1 0 0 20 10 10 0 0 0 0-20z'],
 ]},
 {key:'size',h:'How large is your church?',sub:'Average weekend attendance — this shapes your launch plan (and your pricing tier).',opts:[
   ['u100','Under 100','One service, one family feel','var(--c1a)','M3 21h18M5 21V8l7-5 7 5v13'],
   ['100','100 – 250','Groups & volunteer teams forming','var(--c5a)','M3 21h18M5 21V8l7-5 7 5v13M9 21v-5h6v5'],
   ['250','251 – 500','Multi-service, staff-led ministries','var(--c6a)','M3 21h18M5 21V8l7-5 7 5v13M9 21v-5h6v5M9 12h6'],
   ['500','501 – 1,000','Large single-site momentum','var(--c7a)','M3 21h18M5 21V8l7-5 7 5v13M9 21v-5h6v5M9 12h6M9 9h6'],
   ['1000','Over 1,000 / multisite','Campuses & network scale','var(--c9a)','M2 21h20M4 21V10l6-4v15M14 21V6l6 4v11M8 13h.01M8 17h.01M18 13h.01M18 17h.01'],
 ]},
];
const FEEL2CH={vision:[1],hard:[2,9],deeper:[7],reach:[10],belong:[8]};
const FEEL2OUT={vision:'discipleship',hard:'emotional',deeper:'discipleship',reach:'outreach',belong:'groups'};
const AUD2CH={church:[],families:[3,4],leaders:[7],groups:[8]};
const SIZEL={u100:'under 100',100:'100–250',250:'251–500',500:'501–1,000',1000:'over 1,000'};
const SIZEPRICE={u100:'$49/mo ($490/yr)','100':'$89/mo ($890/yr)','250':'$149/mo ($1,490/yr)','500':'$249/mo ($2,490/yr)','1000':'custom network pricing'};

/* ---- state ---- */
const stage=document.getElementById('stage');
let step=-1; const ans={};

function render(){
  if(step===-1)return intro();
  if(step>=Q.length)return results('matches');
  const q=Q[step];
  stage.innerHTML=`
   <div class="prog">
     <div class="meta">
       <span class="step">Question ${step+1} of ${Q.length}</span>
       ${step>0?'<span class="back" id="back"><svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.6"><path d="M15 18l-6-6 6-6"/></svg> Back</span>':'<span class="back" id="back"><svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.6"><path d="M15 18l-6-6 6-6"/></svg> Start over</span>'}
     </div>
     <div class="bar"><div class="fill" style="width:${(step/Q.length)*100}%"></div></div>
   </div>
   <div class="q">
     <h2>${q.h}</h2>
     <div class="qsub">${q.sub}</div>
     <div class="opts">
       ${q.opts.map(o=>`<button class="opt ${ans[q.key]===o[0]?'sel':''}" data-v="${o[0]}">
          <span class="oi" style="background:${o[3]}"><svg width="21" height="21" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9"><path d="${o[4]}"/></svg></span>
          <span><span class="ot">${o[1]}</span><span class="od">${o[2]}</span></span>
          <span class="chk"><svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><path d="M5 12l5 5 9-11"/></svg></span>
        </button>`).join('')}
     </div>
   </div>`;
  stage.querySelectorAll('.opt').forEach(b=>b.addEventListener('click',()=>{
    ans[q.key]=b.dataset.v;
    stage.querySelectorAll('.opt').forEach(x=>x.classList.remove('sel'));b.classList.add('sel');
    setTimeout(()=>{step++;render();window.scrollTo({top:0,behavior:'smooth'});},240);
  }));
  const back=document.getElementById('back');
  if(back)back.addEventListener('click',()=>{ if(step===0){step=-1;} else {step--;} render();window.scrollTo({top:0}); });
}

function intro(){
  stage.innerHTML=`<div class="intro">
    <span class="badge">Campaign Finder</span>
    <h1>Find your church\u2019s next campaign</h1>
    <p>Answer six quick questions and we\u2019ll search all 1,000+ campaigns to recommend your three best fits — with the right format, season, and a launch plan sized to your church.</p>
    <button class="btn btn-orange" id="start" style="font-size:16px;padding:15px 28px;">Start the finder <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.6"><path d="M5 12h14M13 6l6 6-6 6"/></svg></button>
    <div class="mini">Takes about 45 seconds · No sign-in required</div>
  </div>`;
  document.getElementById('start').addEventListener('click',()=>{step=0;render();});
}

/* ---- scoring against the full library ---- */
function score(row){
  const [t,s2,ch,fmt,seas,outs,pop,nw,flag]=row; let s=0; const hits=[];
  if(ans.outcome && outs.includes(ans.outcome)){s+=6;hits.push('outcome');}
  if(ans.season && ans.season!=='any'){ if(seas.includes(ans.season)){s+=4;hits.push('season');} else if(seas.includes('any')){s+=1.5;} }
  if(ans.format && ans.format!=='any'){ if(fmt===ans.format){s+=4;hits.push('format');} }
  if(ans.audience){ const set=AUD2CH[ans.audience]||[]; if(set.includes(ch)){s+=3;hits.push('aud');} if(ans.audience==='church'&&flag)s+=1.5; }
  if(ans.feel){ if((FEEL2CH[ans.feel]||[]).includes(ch)){s+=4;hits.push('feel');}
    if(FEEL2OUT[ans.feel] && outs.includes(FEEL2OUT[ans.feel])){s+=2;if(!hits.includes('outcome'))hits.push('outcome');} }
  if(flag)s+=1.2;
  s+=pop/100;
  return {s,hits};
}
function fitPct(s){ return Math.min(98, Math.round(70 + s*1.55)); }
function whyText(row,hits){
  const [t,s2,ch,fmt]=row; const parts=[];
  if(hits.includes('outcome')&&ans.outcome)parts.push(`helps you ${OUTL[ans.outcome]}`);
  if(hits.includes('season')&&ans.season&&ans.season!=='any')parts.push(`fits ${SEAS[ans.season]}`);
  if(hits.includes('format')&&ans.format&&ans.format!=='any')parts.push(`runs as a ${fmt} campaign`);
  if(hits.includes('feel')&&!hits.includes('outcome'))parts.push(`lands in ${CHNAME[ch]}`);
  if(hits.includes('aud'))parts.push(`is written toward ${row[11].toLowerCase()}`);
  if(!parts.length)parts.push(`a strong, proven fit in ${CHNAME[ch]}`);
  let str=parts.slice(0,3).join(', ').replace(/,([^,]*)$/,', and$1');
  return str.charAt(0).toUpperCase()+str.slice(1)+'.';
}

let RANKED=null;
function results(tab){
  if(!RANKED){
    const seen=new Set();
    RANKED=DATA.map(r=>({r,...score(r)})).sort((a,b)=>b.s-a.s)
      .filter(o=>{const th=o.r[10]; if(seen.has(th))return false; seen.add(th); return true;});
  }
  const top=RANKED[0], r2=RANKED[1], r3=RANKED[2];
  const tabs=`<div style="display:flex;gap:8px;justify-content:center;margin-bottom:26px;">
    <button class="btn ${tab==='matches'?'btn-dark':'btn-white'}" id="tabm">Your matches</button>
    <button class="btn ${tab==='custom'?'btn-dark':'btn-white'}" id="tabc">Customize &amp; launch</button></div>`;
  if(tab==='matches')renderMatches(tabs,top,r2,r3); else renderCustomize(tabs,top);
  document.getElementById('tabm').addEventListener('click',()=>results('matches'));
  document.getElementById('tabc').addEventListener('click',()=>results('custom'));
}

function renderMatches(tabs,top,r2,r3){
  const covBig=(row)=>{const ch=row[2];const[a,b]=HUE[ch];
    return `<div class="cov big"><div class="canvas" style="--ca:${a};--cb:${b}"><div class="tab"><b>${row[3].replace('-',' ').toUpperCase()}</b></div><div class="nm">${row[0]}</div><span class="fmt">${row[3]}</span></div></div>`;};
  const covSm=(row)=>{const ch=row[2];const[a,b]=HUE[ch];
    return `<div class="cov sm"><div class="canvas" style="--ca:${a};--cb:${b}"><div class="tab"><b>${row[3].replace('-',' ').toUpperCase()}</b></div><div class="nm">${row[0]}</div></div></div>`;};
  const runner=(o)=>`<div class="runner">${covSm(o.r)}
     <div class="rinfo"><div class="fit">${fitPct(o.s)}% match</div><h4>${o.r[0]}</h4>
       <div class="ch">${CHNAME[o.r[2]]} · ${o.r[3]}</div>
       <div class="why">${whyText(o.r,o.hits)}</div>
       <a class="btn btn-white" href="campaign.html?id=${o.r[9]}" style="font-size:13px;padding:9px 15px;">Preview</a></div></div>`;
  stage.innerHTML=`<div class="res">
    <h1>Your top matches</h1>
    <div class="rsub">Scored against all ${DATA.length.toLocaleString()} campaigns. Here are the three built for this moment.</div>
    ${tabs}
    <div class="topmatch">
      <span class="rank">★ Best match</span>
      ${covBig(top.r)}
      <div class="tm-info">
        <span class="fit"><svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4"><path d="M12 2l2.4 5 5.6.8-4 3.9 1 5.5L12 15.8 6 18.2l1-5.5-4-3.9 5.6-.8z"/></svg> ${fitPct(top.s)}% match</span>
        <h3>${top.r[0]}</h3>
        <div class="ch">${CHNAME[top.r[2]]} · ${top.r[10]} · ${top.r[3]} campaign</div>
        <div class="why">${whyText(top.r,top.hits)} <em>${top.r[1]}.</em></div>
        <div class="acts">
          <a class="btn btn-dark" href="campaign.html?id=${top.r[9]}">Preview campaign <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.6"><path d="M7 17 17 7M8 7h9v9"/></svg></a>
          <button class="btn btn-white" id="gocustom">Customize it</button>
        </div>
      </div>
    </div>
    <div class="runners">${runner(r2)}${runner(r3)}</div>
    <div class="foot">
      <button class="btn btn-white" id="restart">Start over</button>
      <a class="btn btn-orange" href="browse.html">Browse the full library <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.6"><path d="M5 12h14M13 6l6 6-6 6"/></svg></a>
    </div>
  </div>`;
  document.getElementById('gocustom').addEventListener('click',()=>results('custom'));
  document.getElementById('restart').addEventListener('click',()=>{Object.keys(ans).forEach(k=>delete ans[k]);RANKED=null;step=-1;render();window.scrollTo({top:0});});
}

function renderCustomize(tabs,top){
  const r=top.r; const fmt=(ans.format&&ans.format!=='any')?ans.format:r[3];
  const size=ans.size||'100'; const days={'7-Day':'7 days','21-Day':'21 days','30-Day':'30 days','40-Day':'40 days','6-Week':'6 weekly sessions'}[fmt];
  const groupTip={u100:'Aim for 6–10 groups of 8. In a church your size the pastor personally inviting hosts fills the roster fastest.',
   '100':'Aim for 12–25 groups. Recruit hosts three weeks out; a live sign-up moment in the service fills most of them.',
   '250':'Aim for 25–50 groups. Appoint 2–3 coach volunteers so no host feels alone, and open online sign-ups alongside the lobby table.',
   '500':'Aim for 50–100 groups. Run host orientation twice (in person + Zoom) and assign a coach per 8–10 hosts.',
   '1000':'Plan by campus: one launch team per site, shared start date, central host training. Network licensing includes a planning call with us.'}[size];
  const card=(h,b)=>`<div style="background:#fff;border:1px solid var(--line);border-radius:16px;padding:18px;text-align:left;">
    <div style="font-family:'Hanken Grotesk';font-weight:800;font-size:14.5px;margin-bottom:5px;">${h}</div>
    <div style="font-size:13px;color:var(--ink-2);line-height:1.55;">${b}</div></div>`;
  stage.innerHTML=`<div class="res">
    <h1>Customize &amp; launch</h1>
    <div class="rsub">Your plan for <b>${r[0]}</b> — sized for a church of ${SIZEL[size]}.</div>
    ${tabs}
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:14px;text-align:left;">
      ${card('Format for your church', `You chose <b>${days}</b>. ${fmt==='40-Day'?'The full movement — six aligned sermons carry the weekend while the church reads daily.':fmt==='6-Week'?'A leader-led group series; pair it with the daily devotional for churchwide reach.':'Every campaign also runs as the classic 40-Day movement when you\u2019re ready for it.'} All five formats are included with your license.`)}
      ${card('Launch timeline', `<b>Weeks 1–2:</b> pick &amp; customize · <b>Weeks 3–5:</b> recruit hosts, promote, open sign-ups · <b>Week 6:</b> Launch Sunday, everyone starts Day 1 · <b>Final weekend:</b> Celebration Sunday. The launch kit includes every script and graphic.`)}
      ${card('Group launch for your size', groupTip)}
      ${card('Sermon alignment', `Six message outlines match the ${fmt==='6-Week'?'six sessions':'weekly arc'} of <em>${r[0]}</em> — anchored in ${r[13]} (NIV). Preach them as-is or fold the outline into your own series.`)}
      ${card('Make it yours', `Every license: print-ready PDF (Letter/A5) with congregation print rights, plus Canva import today. All Access adds editable Google Docs/Word. One-click "Open in Canva" is in development and free at launch.`)}
      ${card('Pastor-branded edition', `Your logo, colors, and your pastor\u2019s name across all four member-facing formats — done for you, $499 per campaign. <a href="pricing.html#premium" style="color:var(--orange);font-weight:700;">See premium options →</a>`)}
    </div>
    <div style="background:#FBF7EE;border:1px solid #EFE3C8;border-radius:16px;padding:16px 20px;margin:16px 0 22px;font-size:13.5px;text-align:left;">
      <b style="font-family:'Hanken Grotesk';">Your tier:</b> at ${SIZEL[size]} attendance, All Access is <b>${SIZEPRICE[size]}</b> — or run just this campaign for <b>$199</b>. <a href="pricing.html" style="color:var(--orange);font-weight:700;">Full pricing →</a>
    </div>
    <div class="foot">
      <a class="btn btn-dark" href="campaign.html?id=${r[9]}">Preview ${r[0]}</a>
      <a class="btn btn-orange" href="get-access.html">Start this campaign <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.6"><path d="M5 12h14M13 6l6 6-6 6"/></svg></a>
    </div>
  </div>`;
}

render();
</script>"""

start = f.index('<script>\nconst HUE=')
end = f.index('</script>', start) + len('</script>')
f = f[:start] + NEW + f[end:]
open(p,'w').write(f)
print('finder rewritten', len(f))
