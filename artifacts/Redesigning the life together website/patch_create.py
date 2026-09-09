import re
s=open('page_create.py').read()

# ============ 1. OUTPUT CARDS: unlock Devotional, clarify the locked two ============
s=s.replace("""      <button class="out avail" onclick="go('prefs')">""",
"""      <button class="out avail" onclick="selectOut('cur')">""")
s=s.replace("""      <div class="out soon">
        <span class="otag chip ink">Coming soon</span>
        <b>Daily Devotional</b>
        <span>Your series as a daily reading plan — 7, 21, 30, or 40 days in your congregation&rsquo;s hands.</span>
      </div>""",
"""      <button class="out avail" onclick="selectOut('devo')">
        <span class="otag chip gold">Week One preview</span>
        <b>Daily Devotional</b>
        <span>Your series as a daily reading plan. This preview builds Week One — seven days from your own texts; the full 40 ships with the platform.</span>
      </button>""")
s=s.replace("""        <span class="otag chip ink">Coming soon</span>
        <b>Leader Guide &amp; Training</b>
        <span>Host scripts, one-evening training, and care plans for the leaders you&rsquo;re about to raise up.</span>""",
"""        <span class="otag chip ink">At platform launch</span>
        <b>Leader Guide &amp; Training</b>
        <span>Host scripts, one-evening training, and care plans. Built by the same engine — a larger template set that switches on with the live platform, not a missing capability.</span>""")
s=s.replace("""        <span class="otag chip ink">Coming soon</span>
        <b>Full 40-Day Campaign</b>
        <span>The complete churchwide architecture — pulpit, groups, and daily reading aligned around your series.</span>""",
"""        <span class="otag chip ink">At platform launch</span>
        <b>Full 40-Day Campaign</b>
        <span>The complete churchwide architecture — pulpit, groups, and daily reading aligned. Same engine at full scale; enabled when generation moves to the live platform.</span>""")

# ============ 2. PREFS: sessions block toggles for devotional ============
s=s.replace("""      <div>
        <label class="lbl">Number of sessions</label>
        <div class="pills" id="pSess">""",
"""      <div id="sessBlock">
        <label class="lbl">Number of sessions</label>
        <div class="pills" id="pSess">""")
s=s.replace("""          <button class="pill" data-v="6">6 sessions</button>
        </div>
      </div>""",
"""          <button class="pill" data-v="6">6 sessions</button>
        </div>
      </div>
      <div id="devoLen" style="display:none">
        <label class="lbl">Length</label>
        <p style="font-size:15px;color:var(--body)"><span class="chip gold">Week One · 7 days</span>&nbsp; The preview engine builds your first week; the full platform extends it to 21, 30, or 40 days.</p>
      </div>""")

# ============ 3. GENERATION ENGINE (inserted before analyze) ============
ENGINE = r"""
/* ================= DERIVATION ENGINE (preview) =================
   Builds sessions from the pastor's OWN text: extracted scripture
   references, their phrases, and a detected theme. Deterministic. */
window.outMode='cur';
function selectOut(m){window.outMode=m;
  document.getElementById('sessBlock').style.display=m==='devo'?'none':'block';
  document.getElementById('devoLen').style.display=m==='devo'?'block':'none';
  go('prefs');}
const CHAPMAX={Genesis:50,Exodus:40,Deuteronomy:34,Joshua:24,Judges:21,Ruth:4,Nehemiah:13,Job:42,Psalm:150,Psalms:150,Proverbs:31,Ecclesiastes:12,Isaiah:66,Jeremiah:52,Ezekiel:48,Daniel:12,Hosea:14,Joel:3,Amos:9,Jonah:4,Micah:7,Matthew:28,Mark:16,Luke:24,John:21,Acts:28,Romans:16,Corinthians:16,Galatians:6,Ephesians:6,Philippians:4,Colossians:4,Thessalonians:5,Timothy:6,Hebrews:13,James:5,Peter:5,Revelation:22};
const THEMES={
 covenant:{kw:['covenant','unfaithful','faithful','return','mercy','adulter','wander','pursue','redeem','bride','betray','hesed','steadfast','prostitut','gomer','wilderness','allure'],
  name:'covenant love & return',
  frames:['The God Who Won\u2019t Let Go','Bought Back','Into the Wilderness','The Long Way Home','Loved at Our Worst','Betrothed Forever'],
  aim:(ref,idea)=>`Sit inside ${ref} until the shape of God\u2019s pursuing love becomes personal \u2014 ${idea}`,
  connect:[`When has someone kept a promise to you that you had stopped expecting them to keep? What did that do to you?`,
           `Share a time you wandered from something good \u2014 a habit, a relationship, a faith rhythm. What finally turned you around?`,
           `What\u2019s the difference between being tolerated and being pursued? Where have you felt each?`,
           `Who in your life has loved you at your least lovable? Don\u2019t rush past this one.`,
           `What does the word \u201cfaithfulness\u201d bring to mind first \u2014 a person, a failure, a hope?`,
           `If God\u2019s love had a tone of voice in this passage, what would it sound like?`],
  discuss:(ref,idea,quote,book)=>[
    `Read ${ref} aloud slowly. What surprises you most about how God speaks and acts here?`,
    `${book} refuses to let us keep God\u2019s love theoretical \u2014 it uses the language of marriage, betrayal, and pursuit. Why do you think God chose imagery this raw?`,
    `Your pastor put it this way: \u201c${quote}\u201d Where does that land in your actual week?`,
    `Where are you tempted to believe you\u2019ve out-wandered God\u2019s willingness to come after you? What does this text say back?`,
    `What would \u201creturning\u201d look like for you \u2014 concretely, this week, not someday?`],
  practice:[`Each morning this week, before anything else, say ${'`'}I am pursued${'`'} out loud \u2014 then read one verse of this week\u2019s chapter.`,
    `Write the name of the season you most wandered. Hold it before God once this week and let Him rename it.`,
    `Choose one relationship where you\u2019ve been keeping score. Practice one act of undeserved kindness \u2014 hesed \u2014 before the group meets again.`],
  pray:{warm:`Thank God around the circle for one specific time He came after you when you weren\u2019t looking for Him.`,
        direct:`Name out loud \u2014 a word or a phrase is enough \u2014 the place you\u2019re most tempted to wander right now. Receive this week\u2019s text as God\u2019s answer.`,
        reflective:`Read the week\u2019s key verse three times slowly, with silence between. Let anyone who wishes pray a single sentence beginning \u201cYou are the God who\u2026\u201d`},
  between:(ref)=>`Before next session, read ${ref} in one unhurried sitting. Underline every action God takes toward His people.`},
 work:{kw:['work','job','vocation','career','monday','workplace','labor','employ','office','calling'],
  name:'work & calling',
  frames:['Made on Purpose','Work as Worship','The Original Job Description','Light in the Workplace','The Long Obedience','Commissioned to Monday'],
  aim:(ref,idea)=>`See your ordinary work through ${ref} \u2014 ${idea}`,
  connect:[`What did you want to be when you were ten \u2014 and what happened to that answer?`,
           `What\u2019s the most invisible task in your week \u2014 the one nobody notices unless you stop doing it?`,
           `Who taught you \u2014 by watching them \u2014 what good work looks like?`],
  discuss:(ref,idea,quote,book)=>[
    `Read ${ref} aloud together. Which phrase lands hardest today, and why?`,
    `Where is the line between healthy ambition and finding your identity in work? How do you know when you\u2019ve crossed it?`,
    `Your pastor said: \u201c${quote}\u201d What changes this week if you actually believe that?`,
    `Who is on your schedule this week that God may have been waiting to love through you?`,
    `What would it mean to do your most ordinary task \u201cas for the Lord\u201d \u2014 concretely?`],
  practice:[`Before your feet hit the floor each morning, ask: \u201cWho is on my schedule today that God has been waiting to love through me?\u201d Write one name daily.`,
    `Choose your most invisible task this week. Offer it each time in a one-sentence silent prayer.`],
  pray:{warm:`Thank God for the work of each person in the circle \u2014 by name, without hurry.`,
        direct:`Have each person name their workplace out loud. Pray over each one as a mission field.`,
        reflective:`Sit ninety seconds in silence with this week\u2019s text, then finish this sentence in prayer: \u201cLord, You prepared\u2026\u201d`},
  between:(ref)=>`Read ${ref} before next session. Note where work appears in the story before anything goes wrong.`},
 family:{kw:['family','marriage','parent','child','home','father','mother','generation','legacy','household'],
  name:'family & legacy',
  frames:['The Table','What We Hand Down','A House on the Rock','Blessing Out Loud','The Long Welcome','Generations'],
  aim:(ref,idea)=>`Let ${ref} reset what your home is actually for \u2014 ${idea}`,
  connect:[`What\u2019s one thing \u2014 not money \u2014 that someone older handed down to you?`,
           `Describe your family table growing up in three words. What do you want your table\u2019s three words to be?`,
           `Who blessed you out loud once \u2014 and can you still hear it?`],
  discuss:(ref,idea,quote,book)=>[
    `Read ${ref} together. What does this text assume a family is for?`,
    `Where does your actual weekly rhythm agree with that \u2014 and where does it argue?`,
    `Your pastor said: \u201c${quote}\u201d Who needs to hear that from you this week?`,
    `What\u2019s one rule in your home that has a story behind it nobody\u2019s ever told?`,
    `What do you want handed down from your life that isn\u2019t money \u2014 and what\u2019s one way to start handing it down now?`],
  practice:[`Bless someone in your home out loud this week \u2014 specific, unhurried, face to face.`,
    `Put one screen-free meal on the calendar. Ask one question at it: \u201cWhere did you see something good this week?\u201d`],
  pray:{warm:`Pray for each home represented in the circle \u2014 by street name or family name.`,
        direct:`Name one relationship at home that needs repair. Pray for the first step, not the whole road.`,
        reflective:`In quiet, picture each person at your table. Give them, one by one, to God.`},
  between:(ref)=>`Read ${ref} with someone from your household this week \u2014 or over the phone with family far away.`},
 money:{kw:['money','giving','generos','steward','treasure','tithe','wealth','provision','finances','debt'],
  name:'generosity & stewardship',
  frames:['Whose Is It?','Open Hands','First, Not Leftover','The Freedom of Enough','Storing Up','A Generous Eye'],
  aim:(ref,idea)=>`Let ${ref} loosen the grip \u2014 ${idea}`,
  connect:[`What\u2019s the best gift you ever gave \u2014 not the most expensive, the best?`,
           `What money habit did you inherit without ever deciding to?`],
  discuss:(ref,idea,quote,book)=>[
    `Read ${ref} aloud. What does it assume about who owns what?`,
    `Where does money most often get the final vote in your decisions?`,
    `Your pastor said: \u201c${quote}\u201d What would obeying that cost \u2014 and what might it free?`,
    `What\u2019s the difference between wise saving and anxious storing? How do you tell them apart in yourself?`,
    `What\u2019s one act of giving you could do this month that would actually be felt?`],
  practice:[`Give one gift this week that costs you something \u2014 secretly if possible.`,
    `Write every purchase down for seven days. At week\u2019s end, ask one question of the list: \u201cWhat do I apparently worship?\u201d`],
  pray:{warm:`Thank God for specific provision this year \u2014 name it plainly.`,
        direct:`Ask God to name the possession with the tightest grip on you \u2014 and to begin loosening it.`,
        reflective:`Hold open hands in your lap for one minute of silence. Let the posture be the prayer.`},
  between:(ref)=>`Read ${ref} again mid-week \u2014 this time next to your bank app. Let them talk to each other.`},
 prayer:{kw:['prayer','pray','worship','presence','listen','intercession','fasting','psalm'],
  name:'prayer & presence',
  frames:['First Words','The Unhurried Room','Praying the Text','When Heaven Is Quiet','Together Before God','A Praying People'],
  aim:(ref,idea)=>`Move prayer from event to atmosphere through ${ref} \u2014 ${idea}`,
  connect:[`Who taught you to pray \u2014 formally or just by being overheard?`,
           `When has a prayer been answered in a way you didn\u2019t want \u2014 at first?`],
  discuss:(ref,idea,quote,book)=>[
    `Read ${ref} aloud. What does this text teach about how God listens?`,
    `What time of day does prayer actually happen for you \u2014 and what does that timing reveal?`,
    `Your pastor said: \u201c${quote}\u201d What would your week look like if that were true of you?`,
    `What do you do with silence from heaven? What does this passage do with it?`,
    `What\u2019s one prayer you\u2019ve stopped praying that this text invites you to take up again?`],
  practice:[`Pray this week\u2019s text out loud once a day \u2014 sixty seconds, no more, no phone.`,
    `Keep a one-line answered-prayer log by your bed. One line, every night.`],
  pray:{warm:`Let each person thank God for one prayer already answered this year.`,
        direct:`Take the boldest request in the room and pray for it together, out loud, first.`,
        reflective:`Practice four minutes of shared silence. Close with one whispered word each.`},
  between:(ref)=>`Pray ${ref} each morning before next session \u2014 same chair, same time, if you can manage it.`},
 suffering:{kw:['suffer','grief','pain','trial','lament','loss','broken','wound','heal','tears','comfort'],
  name:'suffering & hope',
  frames:['The God Who Stays','Permission to Lament','Hope with Scars','Not Wasted','The Valley Psalm','Morning Comes'],
  aim:(ref,idea)=>`Bring the real weight into the light of ${ref} \u2014 ${idea}`,
  connect:[`What\u2019s a loss your group doesn\u2019t know about yet \u2014 that you\u2019re willing to name only as far as you want?`,
           `Who sat with you once in a hard season without trying to fix it? What did they do right?`],
  discuss:(ref,idea,quote,book)=>[
    `Read ${ref} slowly. Where does the text give permission you didn\u2019t know you had?`,
    `What\u2019s the difference between explanation and presence when someone is hurting? Which does God offer here?`,
    `Your pastor said: \u201c${quote}\u201d Where does that meet you \u2014 or where does it feel hard to believe?`,
    `What has suffering taught you that ease never could \u2014 and what has it cost that shouldn\u2019t be spiritualized away?`,
    `Who around you is in the valley right now? What would \u201cstaying\u201d look like?`],
  practice:[`Write one honest lament this week \u2014 no polishing. End it with one line of trust, if you can. If you can\u2019t yet, end it honestly.`,
    `Sit with someone who is hurting for twenty minutes this week. Bring nothing to fix.`],
  pray:{warm:`Pray gently over every burden named tonight \u2014 and the unnamed ones too.`,
        direct:`Invite anyone carrying something heavy to say only a name or a word. Carry each one to God together.`,
        reflective:`Light nothing, fix nothing. Keep three minutes of held silence, then pray the week\u2019s verse over the room.`},
  between:(ref)=>`Read ${ref} once more this week \u2014 on your hardest day, if one comes.`},
 identity:{kw:['identity','beloved','adopted','child of god','worth','shame','grace','new creation','belong'],
  name:'identity & belovedness',
  frames:['Before You Did Anything','No Longer','The Adopted Life','What Shame Says \u2014 and God Says','New Name','Living Loved'],
  aim:(ref,idea)=>`Let ${ref} say who you are before anything you do \u2014 ${idea}`,
  connect:[`What did you win \u2014 a ribbon, a title, a role \u2014 that mattered enormously then and not at all now?`,
           `Whose approval have you worked hardest for? How\u2019s that going?`],
  discuss:(ref,idea,quote,book)=>[
    `Read ${ref} aloud. Which identity words does the text use \u2014 and which do you actually use about yourself?`,
    `Where does shame speak loudest in your week? What exactly does it say?`,
    `Your pastor said: \u201c${quote}\u201d What competes with that voice on a Tuesday?`,
    `What\u2019s the difference between humility and self-contempt? Which does this text produce?`,
    `If you woke up actually believing this passage, what\u2019s the first thing that would change?`],
  practice:[`Every mirror this week: one sentence from this text, said to your own face. Feel silly. Do it anyway.`,
    `Catch one self-accusation per day and answer it \u2014 out loud if you\u2019re alone \u2014 with the week\u2019s verse.`],
  pray:{warm:`Speak a one-line blessing over the person to your left \u2014 who they are, not what they do.`,
        direct:`Renounce out loud, in a word, one false name you\u2019ve answered to. Receive the true one together.`,
        reflective:`Breathe slowly through the week\u2019s verse phrase by phrase. Let the last phrase become your prayer.`},
  between:(ref)=>`Read ${ref} every morning before your phone. Let it get the first word all week.`},
 mission:{kw:['mission','sent','witness','neighbor','gospel','evangel','go ','nations','city','serve'],
  name:'mission & neighbor',
  frames:['Sent People','Across the Street','Eyes Open','The Table as Mission','Good News Out Loud','A City Blessed'],
  aim:(ref,idea)=>`Trade mission-as-program for mission-as-life through ${ref} \u2014 ${idea}`,
  connect:[`Who first told you about Jesus \u2014 and what do you actually remember: the words, or the person?`,
           `Name your literal neighbors \u2014 left, right, across. How far did you get?`],
  discuss:(ref,idea,quote,book)=>[
    `Read ${ref} together. Who is sent, to whom, and with what?`,
    `What makes \u201cwitness\u201d feel heavy \u2014 and what does this text actually ask of you?`,
    `Your pastor said: \u201c${quote}\u201d Who came to mind while he said it?`,
    `Where has God already placed you that you\u2019ve been calling ordinary?`,
    `What\u2019s one door \u2014 literal or not \u2014 you could knock on this month?`],
  practice:[`Learn one neighbor\u2019s name this week. Just the name. God will handle the sequel.`,
    `Invite one person to a table \u2014 coffee counts \u2014 with no agenda except attention.`],
  pray:{warm:`Pray by name for the neighbors named tonight \u2014 and for the ones whose names we don\u2019t know yet.`,
        direct:`Ask God for one specific open door before next session \u2014 and the nerve to walk through it.`,
        reflective:`Picture your street, house by house, in silence. Pray a blessing over each roof.`},
  between:(ref)=>`Read ${ref} again, then walk your street once, slowly, praying with your eyes open.`},
 generic:{kw:[],
  name:'the heart of your series',
  frames:['Opening the Text','The Turn','What It Asks','Living It','When It Gets Hard','Sent With It'],
  aim:(ref,idea)=>`Open ${ref} together until it reads you back \u2014 ${idea}`,
  connect:[`What drew you into this series \u2014 honestly? What do you hope is different in six weeks?`,
           `Where did this week\u2019s text intersect your actual week \u2014 even sideways?`,
           `What\u2019s one question you\u2019ve always had about this part of Scripture and never asked out loud?`],
  discuss:(ref,idea,quote,book)=>[
    `Read ${ref} aloud together \u2014 twice, two voices. What did you hear the second time that you missed the first?`,
    `What does this passage assume about God that our culture doesn\u2019t?`,
    `Your pastor put it this way: \u201c${quote}\u201d Where does that meet your week?`,
    `What would obeying this text cost you? What might it free?`,
    `Who needs what you just learned \u2014 and what\u2019s stopping you from bringing it to them?`],
  practice:[`Read the week\u2019s passage once a day \u2014 same chair, same time. Underline one new word each day.`,
    `Tell one person outside the group what struck you this week. Plain words, no polish.`],
  pray:{warm:`Thank God for one specific thing this text names \u2014 around the circle, unhurried.`,
        direct:`Let each person pray one sentence that begins with a word from tonight\u2019s passage.`,
        reflective:`Read the key verse three times with silence between. Close with the Lord\u2019s Prayer, slowly.`},
  between:(ref)=>`Read ${ref} in one sitting before next session. Come back with one verse underlined and one question.`}
};
function detectTheme(txt){
  const t=txt.toLowerCase();let best='generic',score=0;
  for(const k in THEMES){ if(k==='generic')continue;
    const s=THEMES[k].kw.reduce((a,w)=>a+(t.split(w).length-1),0);
    if(s>score){score=s;best=k;} }
  return score>=2?best:'generic';
}
function parseRefs(txt){
  const vre=new RegExp('\\b((?:[1-3]\\s)?(?:'+BOOKS+'))\\s?(\\d+(?::\\d+(?:[\u2013-]\\d+)?)?)','g');
  const seen=new Set(),refs=[];
  for(const m of txt.matchAll(vre)){
    const r=m[1]+' '+m[2];
    if(!seen.has(r)){seen.add(r);refs.push({book:m[1],disp:r});}
  }
  return refs;
}
function domBook(refs){
  const c={};refs.forEach(r=>c[r.book]=(c[r.book]||0)+1);
  return Object.keys(c).sort((a,b)=>c[b]-c[a])[0]||null;
}
function titleFromQuote(q){
  if(!q)return null;
  let t=q.replace(/["\u201c\u201d]/g,'').split(/[.!?\u2014:;,]/)[0].trim();
  const ws=t.split(/\s+/); if(ws.length>6)t=ws.slice(0,6).join(' ');
  if(t.length<8)return null;
  return t.replace(/\b\w/g,c=>c.toUpperCase());
}
function spineFor(n,a){
  const refs=[...a.refs]; const bk=a.book;
  if(refs.length>=n)return refs.slice(0,n).map(r=>r.disp);
  const out=refs.map(r=>r.disp);
  if(bk){
    const used=new Set(refs.map(r=>parseInt((r.disp.match(/\s(\d+)/)||[])[1]||0)));
    const max=CHAPMAX[bk.replace(/^[1-3]\s/,'')]||12;
    for(let ch=1;out.length<n&&ch<=max;ch++){ if(!used.has(ch)){out.push(bk+' '+ch);used.add(ch);} }
  }
  while(out.length<n)out.push(out[out.length-1]||'Your key passage');
  return out;
}
function deriveSeries(a,n){
  const th=THEMES[a.theme]||THEMES.generic;
  const spine=spineFor(n,a);
  const qs=a.quotes.filter(Boolean);
  return spine.map((ref,i)=>{
    const quote=qs[i%qs.length]||a.big;
    const qt=i%2===0?titleFromQuote(qs[i%qs.length]):null;
    const t=qt||th.frames[i%th.frames.length];
    const conA=th.connect[i%th.connect.length], conB=th.connect[(i+1)%th.connect.length];
    return {t, v:ref,
      aim:th.aim(ref,a.big.replace(/\.$/,'').charAt(0).toLowerCase()+a.big.replace(/\.$/,'').slice(1)+'.'),
      connect:[conA,conB],
      recap:`This week your pastor took us into <b>${ref}</b>${a.book?` \u2014 part of the journey through ${a.book}`:''}. The line to carry into this session: <span class="yw">\u270e your words</span> \u201C${quote}\u201D`,
      discuss:th.discuss(ref,a.big,quote,a.book||'This text'),
      practice:th.practice[i%th.practice.length],
      pray:th.pray,
      between:th.between(spine[(i+1)%spine.length])};
  });
}
function deriveDevoWeek(a){
  const th=THEMES[a.theme]||THEMES.generic;
  const spine=spineFor(7,a);
  const qs=a.quotes.filter(Boolean);
  return spine.map((ref,i)=>{
    const quote=qs[i%qs.length]||a.big;
    const t=(i===0?'Begin Here':titleFromQuote(qs[i%qs.length])||th.frames[i%th.frames.length]);
    return {t:`Day ${i+1} \u00b7 ${t}`, v:ref, devo:true,
      aim:`A ten-minute morning: one passage, one honest question, one prayer to carry out the door.`,
      connect:[''],
      recap:`Open to <b>${ref}</b> and read it slowly \u2014 twice if you can. Don\u2019t hunt for the lesson yet; just let the text say what it says. Your pastor\u2019s word over this series: <span class="yw">\u270e your words</span> \u201C${quote}\u201D`,
      discuss:[`Where does ${ref} touch something that actually happened to you this month?`,
               `What one word or phrase keeps pulling your eye back? Sit with it for a moment \u2014 why that one?`,
               `${th.discuss(ref,a.big,quote,a.book||'This text')[3]}`],
      practice:`Carry today\u2019s phrase into one ordinary moment \u2014 a commute, a dish, a hallway \u2014 and let it interrupt you there.`,
      pray:th.pray,
      between:''};
  });
}
"""
anchor = "const BOOKS='Genesis|"
i=s.find(anchor)
line_end=s.find("\n",i)
s=s[:line_end+1]+ENGINE+s[line_end+1:]

# ============ 4. buildAnalysis: real refs + theme + series title ============
s=s.replace("""    const vre=new RegExp('\\\\b((?:[1-3]\\\\s)?(?:'+BOOKS+'))\\\\s?(\\\\d+(?::\\\\d+(?:[\\u2013-]\\\\d+)?)?)','g');
    const verses=[...new Set([...txt.matchAll(vre)].map(m=>m[1]+' '+m[2]))].slice(0,6);
    const sents=txt.replace(/\\s+/g,' ').split(/(?<=[.!?])\\s/).filter(s=>s.length>40&&s.length<220);
    const big=(sents.find(s=>/\\byou\\b/i.test(s))||sents[0]||'The heart of your message.').trim();
    const pts=sents.filter(s=>/\\b(God|Jesus|Christ|Lord)\\b/.test(s)).slice(0,3);
    analysis={big,verses:verses.length?verses:['Add your key passages'],
      points:[pts.map((p,i)=>`<b>${i+1}.</b> ${p}`).join('<br>')||'<b>1.</b> Edit these to match your outline.'],
      tone:'Warm and direct \\u2014 refine this to match your voice.',
      quotes:[big, sents[1]||big, sents[2]||big, sents[3]||big]};""",
"""    const refs=parseRefs(txt);
    const sents=txt.replace(/\\s+/g,' ').split(/(?<=[.!?])\\s/).filter(s=>s.length>40&&s.length<220);
    const big=(sents.find(s=>/\\byou\\b/i.test(s))||sents[0]||'The heart of your message.').trim();
    const pts=sents.filter(s=>/\\b(God|Jesus|Christ|Lord)\\b/.test(s)).slice(0,3);
    const theme=detectTheme(txt);
    const book=domBook(refs);
    analysis={big,refs,theme,book,
      seriesTitle:book?`The ${book} Series`:(titleFromQuote(big)||'Your Series'),
      verses:refs.length?refs.slice(0,6).map(r=>r.disp):['No references detected \\u2014 the engine will suggest a spine; edit freely'],
      points:[pts.map((p,i)=>`<b>${i+1}.</b> ${p}`).join('<br>')||'<b>1.</b> Edit these to match your outline.'],
      tone:`Detected register: ${THEMES[theme].name}. Refine anything here \\u2014 this step exists so nothing gets built on a misreading.`,
      quotes:[big, sents[1]||big, sents[2]||big, sents[3]||big]};""")

# ============ 5. buildDoc: derive from the sermon (sample keeps its polished library) ============
s=s.replace("""  const lib=sessionLib(analysis.quotes);
  const pick={4:[0,1,3,5],5:[0,1,2,3,5],6:[0,1,2,3,4,5]}[prefs.sess];
  sessions=pick.map(i=>JSON.parse(JSON.stringify(lib[i])));
  cur=0;
  document.getElementById('edTitle').textContent='More Than a Job \\u2014 Small Group Curriculum';
  if(!isSample) document.getElementById('edTitle').textContent='Your Series \\u2014 Small Group Curriculum';
  document.getElementById('edMeta').textContent=`${prefs.sess} sessions \\u00b7 ${prefs.aud} \\u00b7 ${prefs.church} \\u00b7 from the teaching of ${prefs.pastor}`;""",
"""  if(window.outMode==='devo'){
    sessions=isSample?deriveDevoWeek({...analysis,refs:parseRefs('Ephesians 2:10 Colossians 3:23 Genesis 2:15 Matthew 5:16 Colossians 3:17 Galatians 6:9 Matthew 28:19'),theme:'work',book:null}):deriveDevoWeek(analysis);
    cur=0;
    document.getElementById('edTitle').textContent=(isSample?'More Than a Job':analysis.seriesTitle)+' \\u2014 Daily Devotional \\u00b7 Week One';
    document.getElementById('edMeta').textContent=`7 days \\u00b7 ${prefs.aud} \\u00b7 ${prefs.church} \\u00b7 from the teaching of ${prefs.pastor}`;
  } else if(isSample){
    const lib=sessionLib(analysis.quotes);
    const pick={4:[0,1,3,5],5:[0,1,2,3,5],6:[0,1,2,3,4,5]}[prefs.sess];
    sessions=pick.map(i=>JSON.parse(JSON.stringify(lib[i])));
    cur=0;
    document.getElementById('edTitle').textContent='More Than a Job \\u2014 Small Group Curriculum';
    document.getElementById('edMeta').textContent=`${prefs.sess} sessions \\u00b7 ${prefs.aud} \\u00b7 ${prefs.church} \\u00b7 from the teaching of ${prefs.pastor}`;
  } else {
    sessions=deriveSeries(analysis,+prefs.sess);
    cur=0;
    document.getElementById('edTitle').textContent=analysis.seriesTitle+' \\u2014 Small Group Curriculum';
    document.getElementById('edMeta').innerHTML=`${prefs.sess} sessions \\u00b7 ${prefs.aud} \\u00b7 ${prefs.church} \\u00b7 from the teaching of ${prefs.pastor} &nbsp;<span class="chip gold" title="Built from your sermon by the on-device preview engine. The production platform reads deeper with Lifetogether\\u2019s AI engine.">Preview engine \\u00b7 built from your sermon</span>`;
  }""")

# ============ 6. renderSession + docHTML: devotional labels ============
s=s.replace("""function renderSession(){
  const s=sessions[cur];
  const ci=altConnect[cur]||0;""",
"""function renderSession(){
  const s=sessions[cur];
  const ci=altConnect[cur]||0;
  const devo=!!s.devo;
  const L=devo?{unit:'Day',aim:'Today',recap:'Read',discuss:'Reflect',practice:'Respond \\u00b7 today',pray:'Pray'}
             :{unit:'Session',aim:'The aim',recap:'From Sunday \\u00b7 5 min',discuss:'Discuss \\u00b7 35 min',practice:'Practice \\u00b7 this week',pray:'Pray \\u00b7 10 min'};""")
s=s.replace("""      <span class="chip gold">Session ${cur+1} of ${sessions.length} \\u00b7 ${s.v}</span>""",
"""      <span class="chip gold">${L.unit} ${cur+1} of ${sessions.length} \\u00b7 ${s.v}</span>""")
s=s.replace("""      <div class="blk"><div class="bh"><label class="lbl">The aim</label></div>
        <p contenteditable="true" onblur="sessions[${cur}].aim=this.textContent">${s.aim}</p></div>
      <div class="blk"><div class="bh"><label class="lbl">Connect · 10 min</label>
        <button class="regen" onclick="regenConnect(this)">\\u21bb Try another</button></div>
        <p contenteditable="true" id="connectBlk">${s.connect[ci%s.connect.length]}</p></div>
      <div class="blk"><div class="bh"><label class="lbl">From Sunday · 5 min</label></div>
        <p contenteditable="true">${s.recap}</p></div>
      <div class="blk"><div class="bh"><label class="lbl">Discuss · 35 min</label></div>
        <p contenteditable="true">${s.discuss.map((q,i)=>`<b>${i+1}.</b> ${q}`).join('<br><br>')}</p></div>
      <div class="blk"><div class="bh"><label class="lbl">Practice · this week</label></div>
        <p contenteditable="true">${s.practice}</p></div>
      <div class="blk"><div class="bh"><label class="lbl">Pray · 10 min</label></div>
        <p contenteditable="true">${s.pray[prefs.tone]}</p></div>
      <div class="blk"><div class="bh"><label class="lbl">Between sessions</label></div>
        <p contenteditable="true">${s.between}</p></div>""",
"""      <div class="blk"><div class="bh"><label class="lbl">${L.aim}</label></div>
        <p contenteditable="true" onblur="sessions[${cur}].aim=this.textContent">${s.aim}</p></div>
      ${devo?'':`<div class="blk"><div class="bh"><label class="lbl">Connect \\u00b7 10 min</label>
        <button class="regen" onclick="regenConnect(this)">\\u21bb Try another</button></div>
        <p contenteditable="true" id="connectBlk">${s.connect[ci%s.connect.length]}</p></div>`}
      <div class="blk"><div class="bh"><label class="lbl">${L.recap}</label></div>
        <p contenteditable="true">${s.recap}</p></div>
      <div class="blk"><div class="bh"><label class="lbl">${L.discuss}</label></div>
        <p contenteditable="true">${s.discuss.map((q,i)=>`<b>${i+1}.</b> ${q}`).join('<br><br>')}</p></div>
      <div class="blk"><div class="bh"><label class="lbl">${L.practice}</label></div>
        <p contenteditable="true">${s.practice}</p></div>
      <div class="blk"><div class="bh"><label class="lbl">${L.pray}</label></div>
        <p contenteditable="true">${s.pray[prefs.tone]}</p></div>
      ${devo?'':`<div class="blk"><div class="bh"><label class="lbl">Between sessions</label></div>
        <p contenteditable="true">${s.between}</p></div>`}""")

s=s.replace("""function docHTML(){
  return sessions.map((s,i)=>`
    <div style="page-break-after:always;font-family:Georgia,serif;max-width:680px;margin:0 auto 40px">
      <p style="font-size:11px;letter-spacing:2px;color:#5F8540;font-weight:bold">SESSION ${i+1} \\u00b7 ${s.v.toUpperCase()}</p>""",
"""function docHTML(){
  return sessions.map((s,i)=>{
   const devo=!!s.devo;
   return `
    <div style="page-break-after:always;font-family:Georgia,serif;max-width:680px;margin:0 auto 40px">
      <p style="font-size:11px;letter-spacing:2px;color:#5F8540;font-weight:bold">${devo?'DAY':'SESSION'} ${i+1} \\u00b7 ${s.v.toUpperCase()}</p>""")
s=s.replace("""      <h4 style="color:#2E4C97">The aim</h4><p>${s.aim}</p>
      <h4 style="color:#2E4C97">Connect \\u00b7 10 min</h4><p>${s.connect[(altConnect[i]||0)%s.connect.length]}</p>
      <h4 style="color:#2E4C97">From Sunday \\u00b7 5 min</h4><p>${s.recap.replace(/<span class="yw">[^<]*<\\/span>/g,'[your words] ')}</p>
      <h4 style="color:#2E4C97">Discuss \\u00b7 35 min</h4><p>${s.discuss.map((q,qi)=>`<b>${qi+1}.</b> ${q}`).join('<br><br>')}</p>
      <h4 style="color:#2E4C97">Practice \\u00b7 this week</h4><p>${s.practice}</p>
      <h4 style="color:#2E4C97">Pray \\u00b7 10 min</h4><p>${s.pray[prefs.tone]}</p>
      <h4 style="color:#2E4C97">Between sessions</h4><p>${s.between}</p>
    </div>`).join('');
}""",
"""      <h4 style="color:#2E4C97">${devo?'Today':'The aim'}</h4><p>${s.aim}</p>
      ${devo?'':`<h4 style="color:#2E4C97">Connect \\u00b7 10 min</h4><p>${s.connect[(altConnect[i]||0)%s.connect.length]}</p>`}
      <h4 style="color:#2E4C97">${devo?'Read':'From Sunday \\u00b7 5 min'}</h4><p>${s.recap.replace(/<span class="yw">[^<]*<\\/span>/g,'[your words] ')}</p>
      <h4 style="color:#2E4C97">${devo?'Reflect':'Discuss \\u00b7 35 min'}</h4><p>${s.discuss.map((q,qi)=>`<b>${qi+1}.</b> ${q}`).join('<br><br>')}</p>
      <h4 style="color:#2E4C97">${devo?'Respond \\u00b7 today':'Practice \\u00b7 this week'}</h4><p>${s.practice}</p>
      <h4 style="color:#2E4C97">Pray</h4><p>${s.pray[prefs.tone]}</p>
      ${devo?'':`<h4 style="color:#2E4C97">Between sessions</h4><p>${s.between}</p>`}
    </div>`}).join('');
}""")

# download filename adapts
s=s.replace("a.download='Small-Group-Curriculum.doc';",
            "a.download=(window.outMode==='devo'?'Daily-Devotional-Week-One.doc':'Small-Group-Curriculum.doc');")

# tabs label for devotional
s=s.replace("function renderTabs(){","function renderTabs(){\n  const unit=(sessions[0]&&sessions[0].devo)?'Day':'S';")
if "unit" in s:
    s=s.replace("`Session ${i+1}`" ,"`${unit==='Day'?'Day':'Session'} ${i+1}`")
    s=s.replace("`S${i+1}`","`${unit}${i+1}`")

open('page_create.py','w').write(s)
print("create engine patched")
