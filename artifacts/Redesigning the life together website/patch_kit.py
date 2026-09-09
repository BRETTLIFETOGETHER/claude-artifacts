import re
s=open('page_create.py').read()

# ================= 1. LANDING: the Any Given Sunday pitch =================
s=s.replace("""          <button class="btn btn-gold btn-lg" onclick="go('upload')">Start with one sermon <span class="arrow">→</span></button>
          <button class="btn btn-outline btn-lg" onclick="loadSample();go('upload')">Try it with a sample</button>""",
"""          <button class="btn btn-gold btn-lg" onclick="go('upload')">Start with one sermon <span class="arrow">→</span></button>
          <button class="btn btn-outline btn-lg" onclick="loadSample();go('upload')">Try it with a sample</button>
        </div>
        <div class="mt32" style="background:#F4F4EF;border:1px solid var(--line);border-left:6px solid var(--lt-orange);border-radius:3px;padding:18px 22px;max-width:560px">
          <b style="color:var(--ink);font-size:15.5px">The Any-Given-Sunday promise.</b>
          <p style="font-size:14px;color:var(--body);line-height:1.6;margin-top:6px">Finish preaching Saturday night, drop the message in, and your groups have a session <b>this week</b> — digital tonight. Give us <b>30 minutes a week</b> — 10&ndash;15 minutes of teaching plus seven 90-second daily videos (we write the scripts) — and every week becomes a complete kit. Week by week they stand alone; at week six, roll them up into a study your groups can run any Tuesday night.</p>""")

# ================= 2. OUTPUTS: Weekly Kit as the flagship choice =================
s=s.replace("""    <div class="outs">
      <button class="out avail" onclick="selectOut('cur')">""",
"""    <div class="outs">
      <button class="out avail" onclick="selectOut('kit')" style="grid-column:1/-1;border-color:var(--lt-orange);border-width:2px">
        <span class="otag lbl-bar orange" style="padding:5px 12px">This week&rsquo;s kit — everything below</span>
        <b>The Weekly Kit · Any Given Sunday</b>
        <span>One message in → the whole week out: the small group session, seven daily devotions, seven 90-second video scripts for you to record, leader coaching, the memory verse, and youth &amp; children&rsquo;s notes. Standalone this week; rolls up into a study later.</span>
      </button>
      <button class="out avail" onclick="selectOut('cur')">""")

# ================= 3. PREFS: kit note =================
s=s.replace("""      <div id="devoLen" style="display:none">
        <label class="lbl">Length</label>
        <p style="font-size:15px;color:var(--body)"><span class="chip gold">Week One · 7 days</span>&nbsp; The preview engine builds your first week; the full platform extends it to 21, 30, or 40 days.</p>
      </div>""",
"""      <div id="devoLen" style="display:none">
        <label class="lbl">Length</label>
        <p style="font-size:15px;color:var(--body)"><span class="chip gold">Week One · 7 days</span>&nbsp; The preview engine builds your first week; the full platform extends it to 21, 30, or 40 days.</p>
      </div>
      <div id="kitNote" style="display:none">
        <label class="lbl">This week&rsquo;s kit</label>
        <p style="font-size:15px;color:var(--body)"><span class="chip gold">Standalone week</span>&nbsp; Session + 7 dailies + 7 video scripts + leader, memory, youth &amp; kids. Works best when you give it 10&ndash;15 minutes of your recorded teaching — minimum ten, never more than fifteen. We guard your time.</p>
      </div>""")
s=s.replace("""function selectOut(m){window.outMode=m;
  document.getElementById('sessBlock').style.display=m==='devo'?'none':'block';
  document.getElementById('devoLen').style.display=m==='devo'?'block':'none';
  go('prefs');}""",
"""function selectOut(m){window.outMode=m;
  document.getElementById('sessBlock').style.display=(m==='devo'||m==='kit')?'none':'block';
  document.getElementById('devoLen').style.display=m==='devo'?'block':'none';
  document.getElementById('kitNote').style.display=m==='kit'?'block':'none';
  go('prefs');}""")

# ================= 4. KIT DERIVATION ENGINE =================
KIT = r"""
/* ---------- weekly kit parts ---------- */
function deriveScripts(a){
  const th=THEMES[a.theme]||THEMES.generic;
  const spine=spineFor(7,a); const qs=a.quotes.filter(Boolean);
  const hooks=[
   'Hey church \u2014 before this day gets loud, give me ninety seconds.',
   'Good morning. One text, one thought, and you\u2019re on your way.',
   'Wherever this finds you \u2014 the car, the kitchen, the break room \u2014 pause with me.',
   'Day '+' '+'\u2014 you made it back. That matters more than you think.',
   'Ninety seconds. That\u2019s all. But God can do a lot with ninety seconds.',
   'Before you check anything else this morning, check this.',
   'Last one of the week \u2014 and I saved something for you.'];
  return spine.map((ref,i)=>{
    const quote=qs[i%qs.length]||a.big;
    return {d:i+1, ref,
      body:`${i===3?'Day four \u2014 you made it back. That matters more than you think.':hooks[i]}\n\nToday we\u2019re in ${ref}. Open it later if you can \u2014 for now, just hear this: ${quote}\n\nHere\u2019s the one thought I want you to carry: ${th.aim(ref,'let this be more than information today').replace(/\u2014.*$/,'').trim()}. Not someday \u2014 today, in the middle of your actual schedule.\n\nSo here\u2019s your question for the day: where will this meet you before dinner? Name the moment. Watch for it.\n\nLord, walk this into our ${['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday'][i%7]}. Amen. \u2014 See you tomorrow.`};
  });
}
function deriveLeader(a,sess){
  const th=THEMES[a.theme]||THEMES.generic;
  return {
    prep:`Before your group meets: read ${sess.v} once through, unhurried. Then pray through your roster by name \u2014 thirty seconds each. That\u2019s the whole prep. You are a host, not a professor; the material below does the heavy lifting.`,
    run:`Run order (75 min): Connect 10 \u00b7 Watch/recap the teaching 10\u201315 \u00b7 Discuss 35 \u00b7 Practice hand-off 5 \u00b7 Pray 10. If discussion catches fire on question two, let questions three through five go \u2014 depth beats coverage every single week.`,
    tip:`This week\u2019s facilitation key: the theme is ${th.name}. When someone shares something real, resist the urge to fix or teach. Say \u201cthank you for trusting us with that\u201d \u2014 and let silence do its work before moving on.`,
    care:`Care prompt: one person in your group had a harder week than they\u2019ll volunteer. Text two members before Thursday: \u201cThinking of you \u2014 how can I pray?\u201d You\u2019re not checking a box; you\u2019re building the net.`
  };
}
function deriveMemory(a){
  const spine=spineFor(1,a);
  return {ref:spine[0],
    plan:`Say ${spine[0]} aloud once after each daily devotional \u2014 seven repetitions by Sunday. Write it on one card: bathroom mirror or dashboard. Families: say it together at one meal; youngest goes first.`};
}
function deriveYouth(a,sess){
  const th=THEMES[a.theme]||THEMES.generic;
  return {
    connect:[`Phones face-down in the middle. First one to grab theirs owes the group snacks next week. Now \u2014 everybody answer: what\u2019s one thing from this week you\u2019d actually want prayer for?`,
             `Two truths and a lie \u2014 about your week. Group guesses the lie. (Leader goes first and goes honest.)`],
    teach:`Same text as the adults \u2014 ${sess.v} \u2014 because students don\u2019t need a junior gospel. Read it out loud in two voices. Then one sentence from your pastor to put on the table: \u201C${(a.quotes[0]||a.big)}\u201D`,
    discuss:[`Real talk: does ${sess.v} sound like good news or pressure to you today? Why?`,
             `Where does this collide with what school, your feed, or your friend group says this week?`,
             `What\u2019s one thing you could actually do about this before Friday \u2014 small counts?`],
    send:`Close standing up. One-sentence prayers only \u2014 popcorn style. Leader ends with the memory verse over the room.`
  };
}
function deriveKids(a,sess){
  return {
    table:`Table Talk (5 min at dinner): \u201cTonight\u2019s Bible spot is ${sess.v}.\u201d Read one or two verses in a kids\u2019 translation. Ask: \u201cWhat do you think God is like in this part?\u201d There are no wrong answers at this table.`,
    activity:`Do Together: draw the story \u2014 one page, stick figures welcome. Stick it on the fridge; that\u2019s this week\u2019s gallery. Bonus: act it out in sixty seconds with stuffed-animal casting.`,
    blessing:`Blessing to say over your child at bedtime: \u201cGod made you, God sees you, and God is not letting go of you \u2014 not tonight, not ever.\u201D Same words every night this week; repetition is the point.`
  };
}
function deriveKit(a){
  const session=deriveSeries(a,1)[0];
  return {session, days:deriveDevoWeek(a), scripts:deriveScripts(a),
          leader:deriveLeader(a,session), memory:deriveMemory(a),
          youth:deriveYouth(a,session), kids:deriveKids(a,session)};
}
"""
i=s.find("function deriveKit") 
anchor="function deriveDevoWeek(a){"
j=s.find(anchor)
# insert KIT after deriveDevoWeek's closing — find the end of that function block: next "\n}\n" after j
end=s.find("\n}\n", s.find("return spine.map",j))
s=s[:end+3]+KIT+s[end+3:]

# ================= 5. KIT EDITOR =================
# kit part tabs UI injected above session tabs; renderKit routes parts
s=s.replace("""  } else {
    sessions=deriveSeries(analysis,+prefs.sess);""",
"""  } else if(window.outMode==='kit'){
    window.kit = isSample
      ? deriveKit({...analysis,refs:parseRefs('Ephesians 2:10 Colossians 3:23 Genesis 2:15 Matthew 5:16 Colossians 3:17 Galatians 6:9 Matthew 28:19'),theme:'work',book:null,seriesTitle:'More Than a Job'})
      : deriveKit(analysis);
    window.kitPart='session';
    sessions=[window.kit.session];cur=0;
    document.getElementById('edTitle').textContent=(isSample?'More Than a Job':analysis.seriesTitle)+' \\u2014 This Week\\u2019s Kit';
    document.getElementById('edMeta').innerHTML=`Any Given Sunday \\u00b7 ${prefs.aud} \\u00b7 ${prefs.church} \\u00b7 from the teaching of ${prefs.pastor} &nbsp;<span class="chip gold">Standalone week \\u00b7 rolls up into a study</span>`;
    renderKitBar();renderKitPart();show('st-editor');return;
  } else {
    sessions=deriveSeries(analysis,+prefs.sess);""")

KITUI = r"""
/* ---------- kit editor ---------- */
const KITPARTS=[['session','Group Session'],['days','Daily Devotions'],['scripts','Video Scripts'],['leader','Leader Coaching'],['memory','Memory Verse'],['youth','Youth'],['kids','Children & Family']];
function renderKitBar(){
  let bar=document.getElementById('kitBar');
  if(!bar){
    bar=document.createElement('div');bar.id='kitBar';
    bar.style.cssText='display:flex;gap:8px;flex-wrap:wrap;margin:0 0 18px';
    const pane=document.getElementById('docPane');
    pane.parentElement.insertBefore(bar,pane);
  }
  bar.style.display='flex';
  bar.innerHTML=KITPARTS.map(([k,n])=>`<button class="pill ${window.kitPart===k?'sel':''}" onclick="window.kitPart='${k}';renderKitBar();renderKitPart()">${n}</button>`).join('');
}
function hideKitBar(){const b=document.getElementById('kitBar');if(b)b.style.display='none';}
function renderKitPart(){
  const K=window.kit,p=window.kitPart,pane=document.getElementById('docPane');
  document.querySelector('.sess-tabs')?.style.setProperty('display', (p==='session'||p==='days')?'':'none');
  if(p==='session'){sessions=[K.session];cur=0;renderTabs();renderSession();return;}
  if(p==='days'){sessions=K.days;cur=Math.min(cur,6);renderTabs();renderSession();return;}
  const head=(t,sub)=>`<div class="doc-head"><span class="chip gold">${t}</span><h3>${sub}</h3><p class="dsub">${prefs.church} \u00b7 from the teaching of ${prefs.pastor}</p></div>`;
  const blk=(l,body,path)=>`<div class="blk"><div class="bh"><label class="lbl">${l}</label></div><p contenteditable="true" onblur="${path}=this.innerText">${body.replace(/\n/g,'<br>')}</p></div>`;
  if(p==='scripts'){
    pane.innerHTML=head('7 \u00d7 90-second daily videos','Your scripts \u2014 record on a phone')+
      `<div class="doc-body"><p style="font-size:13.5px;color:var(--mute);margin-bottom:14px">Teleprompter-ready. Each runs \u2248 90 seconds at a natural pace. Record all seven in one sitting \u2014 about fifteen minutes \u2014 and you\u2019ve fed your church for a week.</p>`+
      K.scripts.map((sc,i)=>blk(`Day ${sc.d} \u00b7 ${sc.ref} \u00b7 \u224890 sec`,sc.body,`window.kit.scripts[${i}].body`)).join('')+`</div>`;
  }
  if(p==='leader'){
    const L=K.leader;
    pane.innerHTML=head('Leader coaching','One page for your hosts')+
      `<div class="doc-body">`+blk('Before the group',L.prep,'window.kit.leader.prep')+blk('Run order',L.run,'window.kit.leader.run')+blk('This week\u2019s facilitation key',L.tip,'window.kit.leader.tip')+blk('Care prompt',L.care,'window.kit.leader.care')+`</div>`;
  }
  if(p==='memory'){
    const M=K.memory;
    pane.innerHTML=head('Memory verse','The week\u2019s anchor text')+
      `<div class="doc-body">`+blk('This week\u2019s verse',M.ref+' (NIV) \u2014 print the full text from your Bible software; verse text ships licensed in the full platform.','window.kit.memory.ref')+blk('The seven-day plan',M.plan,'window.kit.memory.plan')+`</div>`;
  }
  if(p==='youth'){
    const Y=K.youth;
    pane.innerHTML=head('Youth edition','Same text \u00b7 re-aimed, not watered down')+
      `<div class="doc-body">`+blk('Connect',Y.connect.join('\n\n'),'window.kit.youth._c')+blk('The text on the table',Y.teach,'window.kit.youth.teach')+blk('Real talk',Y.discuss.map((q,i)=>(i+1)+'. '+q).join('\n\n'),'window.kit.youth._d')+blk('Send',Y.send,'window.kit.youth.send')+`</div>`;
  }
  if(p==='kids'){
    const C=K.kids;
    pane.innerHTML=head('Children & Family','For the table and the bedside')+
      `<div class="doc-body">`+blk('Table talk',C.table,'window.kit.kids.table')+blk('Do together',C.activity,'window.kit.kids.activity')+blk('Bedtime blessing',C.blessing,'window.kit.kids.blessing')+`</div>`;
  }
}
function kitDocHTML(){
  const K=window.kit;const h4=t=>`<h4 style="color:#2E4C97">${t}</h4>`;
  const part=(t)=>`<div style="page-break-before:always"></div><h2 style="color:#1C1C1C;border-bottom:3px solid #7CA457;padding-bottom:6px">${t}</h2>`;
  const savedSessions=sessions; sessions=[K.session]; const sess=docHTML(); sessions=K.days; const days=docHTML(); sessions=savedSessions;
  return sess
   + part('Daily Video Scripts \u2014 7 \u00d7 90 seconds')+K.scripts.map(sc=>`${h4('Day '+sc.d+' \u00b7 '+sc.ref+' \u00b7 \u224890 sec')}<p>${sc.body.replace(/\n/g,'<br>')}</p>`).join('')
   + part('Daily Devotions \u2014 Week One')+days
   + part('Leader Coaching')+h4('Before the group')+`<p>${K.leader.prep}</p>`+h4('Run order')+`<p>${K.leader.run}</p>`+h4('Facilitation key')+`<p>${K.leader.tip}</p>`+h4('Care prompt')+`<p>${K.leader.care}</p>`
   + part('Memory Verse')+h4(K.memory.ref)+`<p>${K.memory.plan}</p>`
   + part('Youth Edition')+h4('Connect')+`<p>${K.youth.connect.join('<br><br>')}</p>`+h4('The text on the table')+`<p>${K.youth.teach}</p>`+h4('Real talk')+`<p>${K.youth.discuss.map((q,i)=>`<b>${i+1}.</b> ${q}`).join('<br><br>')}</p>`+h4('Send')+`<p>${K.youth.send}</p>`
   + part('Children & Family')+h4('Table talk')+`<p>${K.kids.table}</p>`+h4('Do together')+`<p>${K.kids.activity}</p>`+h4('Bedtime blessing')+`<p>${K.kids.blessing}</p>`;
}
"""
s=s.replace("/* ---------- weekly kit parts ---------- */", "/* ---------- weekly kit parts ---------- */")
s=s.replace("function renderKitBar();", "function renderKitBar();")
# insert KITUI before renderSession definition
k=s.find("function renderSession(){")
s=s[:k]+KITUI+"\n"+s[k:]

# renderSession/back-compat: when leaving kit mode via non-kit generations, hide bar
s=s.replace("""    renderTabs();renderSession();""","""    hideKitBar();renderTabs();renderSession();""",1)

# session/day tab clicks inside kit keep part context: renderTabs uses sessions already — fine.

# fullDocHTML uses kit compile when in kit mode
s=s.replace("""    </head><body>
    <div style="text-align:center;margin-bottom:34px">
      <p style="font-size:11px;letter-spacing:3px;color:#5F8540;font-weight:bold">LIFETOGETHER \\u00b7 ${prefs.church.toUpperCase()}</p>
      <h1 style="color:#1C1C1C;font-size:30px;margin:4px 0">${title}</h1>
      <p style="color:#777;font-size:13px">From the teaching of ${prefs.pastor}</p>
    </div>${docHTML()}</body></html>`;""",
"""    </head><body>
    <div style="text-align:center;margin-bottom:34px">
      <p style="font-size:11px;letter-spacing:3px;color:#5F8540;font-weight:bold">LIFETOGETHER \\u00b7 ${prefs.church.toUpperCase()}</p>
      <h1 style="color:#1C1C1C;font-size:30px;margin:4px 0">${title}</h1>
      <p style="color:#777;font-size:13px">From the teaching of ${prefs.pastor}</p>
    </div>${window.outMode==='kit'&&window.kit?kitDocHTML():docHTML()}</body></html>`;""")
s=s.replace("a.download=(window.outMode==='devo'?'Daily-Devotional-Week-One.doc':'Small-Group-Curriculum.doc');",
            "a.download=(window.outMode==='kit'?'Weekly-Kit.doc':window.outMode==='devo'?'Daily-Devotional-Week-One.doc':'Small-Group-Curriculum.doc');")

# export lede mentions kit; savedChip logic already generic via finishEdit; save kit with series info
s=s.replace("""function finishEdit(){
  try{
    ltPush('lt_curricula',{id:ltId(),title:document.getElementById('edTitle').textContent,
      sessions:sessions.length,church:prefs.church,date:new Date().toISOString(),
      data:{sessions,prefs,analysis,isSample}});
  }catch(e){}""",
"""function finishEdit(){
  try{
    const isKit=window.outMode==='kit'&&window.kit;
    const seriesKey=(isSample?'More Than a Job':(analysis.seriesTitle||'Your Series'));
    const weekN=isKit?(ltGet('lt_curricula').filter(c=>c.type==='kit'&&c.seriesKey===seriesKey).length+1):null;
    ltPush('lt_curricula',{id:ltId(),title:document.getElementById('edTitle').textContent+(isKit?` \\u00b7 Week ${weekN}`:''),
      type:isKit?'kit':(window.outMode==='devo'?'devo':'series'),seriesKey,week:weekN,
      sessions:sessions.length,church:prefs.church,date:new Date().toISOString(),
      data:isKit?{kit:window.kit,session:window.kit.session,prefs,analysis,isSample}:{sessions,prefs,analysis,isSample}});
  }catch(e){}""")

# rollup loader: ?rollup=id1,id2
s=s.replace("""    if(q.get('cur')){""",
"""    if(q.get('rollup')){
      const ids=q.get('rollup').split(',');
      const items=ids.map(id=>ltFind('lt_curricula',id)).filter(Boolean);
      if(items.length){
        const first=items[0];
        Object.assign(prefs,first.data.prefs);analysis=first.data.analysis||{};isSample=false;window.outMode='cur';
        sessions=items.map((it,i)=>{
          const base=it.data.session||((it.data.sessions||[])[0]);
          const cp=JSON.parse(JSON.stringify(base));
          cp.t=`Week ${it.week||i+1}: ${cp.t}`;return cp;
        });
        cur=0;
        document.getElementById('edTitle').textContent=(first.seriesKey||'Your Series')+' \\u2014 The Complete Study';
        document.getElementById('edMeta').innerHTML=`${sessions.length} weeks rolled up \\u00b7 ${prefs.aud} \\u00b7 ${prefs.church} &nbsp;<span class="chip gold">Ready for any Tuesday night</span>`;
        hideKitBar();renderTabs();renderSession();show('st-editor');
      }
    }
    if(q.get('cur')){""")
# cur loader for kit items reopens kit
s=s.replace("""      const c=ltFind('lt_curricula',q.get('cur'));
      if(c&&c.data){
        Object.assign(prefs,c.data.prefs);analysis=c.data.analysis;isSample=c.data.isSample;
        sessions=c.data.sessions;cur=0;""",
"""      const c=ltFind('lt_curricula',q.get('cur'));
      if(c&&c.data&&c.type==='kit'){
        Object.assign(prefs,c.data.prefs);analysis=c.data.analysis;isSample=c.data.isSample;
        window.outMode='kit';window.kit=c.data.kit;window.kitPart='session';
        sessions=[window.kit.session];cur=0;
        document.getElementById('edTitle').textContent=c.title.replace(/ \\u00b7 Week \\d+$/,'');
        document.getElementById('edMeta').textContent=`Any Given Sunday \\u00b7 ${prefs.aud} \\u00b7 ${prefs.church}`;
        renderKitBar();renderKitPart();show('st-editor');
      }
      else if(c&&c.data){
        Object.assign(prefs,c.data.prefs);analysis=c.data.analysis;isSample=c.data.isSample;
        sessions=c.data.sessions;cur=0;""")

open('page_create.py','w').write(s)
print("kit engine + editor + rollup loader installed")

# ================= 6. LIBRARY: series grouping + roll-up button =================
s=open('page_account.py').read()
s=s.replace("""  // curricula
  const curs=ltGet('lt_curricula');
  document.getElementById('curList').innerHTML = curs.length ? curs.map(c=>`
    <div class="itm cur">
      <div><b>${c.title}</b><span class="meta">${c.sessions} sessions · ${c.church} · saved ${new Date(c.date).toLocaleDateString()}</span></div>
      <div class="acts">
        <a class="btn btn-primary btn-sm" href="create.html?cur=${c.id}">Reopen in the studio</a>
        <button class="btn btn-outline btn-sm" onclick="ltDel('lt_curricula','${c.id}');location.reload()">Remove</button>
      </div>
    </div>`).join('') :
    `<div class="empty">Nothing generated yet. Build a curriculum from any uploaded sermon and it will live here.</div>`;""",
"""  // curricula — grouped, with weekly-kit roll-up
  const curs=ltGet('lt_curricula');
  const kitGroups={};
  curs.filter(c=>c.type==='kit').forEach(c=>{(kitGroups[c.seriesKey]=kitGroups[c.seriesKey]||[]).push(c);});
  const rollups=Object.entries(kitGroups).filter(([k,v])=>v.length>=2).map(([k,v])=>{
    const ids=v.sort((a,b)=>(a.week||0)-(b.week||0)).map(x=>x.id).join(',');
    return `<div class="itm" style="border-left-color:var(--lt-lime);background:#FBFBEF">
      <div><b>Roll up &ldquo;${k}&rdquo; — ${v.length} weeks → one study</b><span class="meta">Week by week they stood alone. Compiled, they become a study your groups can run any Tuesday night — and send to print.</span></div>
      <div class="acts"><a class="btn btn-primary btn-sm" href="create.html?rollup=${ids}">Roll up ${v.length} weeks</a></div>
    </div>`;}).join('');
  const tag=c=>c.type==='kit'?'<span class="chip lime" style="margin-right:8px">Weekly kit</span>':(c.type==='devo'?'<span class="chip" style="margin-right:8px">Devotional</span>':'');
  document.getElementById('curList').innerHTML = curs.length ? rollups + curs.map(c=>`
    <div class="itm cur">
      <div><b>${tag(c)}${c.title}</b><span class="meta">${c.sessions} session${c.sessions>1?'s':''} · ${c.church} · saved ${new Date(c.date).toLocaleDateString()}</span></div>
      <div class="acts">
        <a class="btn btn-primary btn-sm" href="create.html?cur=${c.id}">Reopen in the studio</a>
        <button class="btn btn-outline btn-sm" onclick="ltDel('lt_curricula','${c.id}');location.reload()">Remove</button>
      </div>
    </div>`).join('') :
    `<div class="empty">Nothing generated yet. Build a weekly kit from any sermon and it will live here — two weeks in the same series unlock the roll-up.</div>`;""")
open('page_account.py','w').write(s)
print("library roll-up installed")
