# -*- coding: utf-8 -*-
import re
O='/home/claude/site/out/'
e=open(O+'engine.js').read()

NEW = r'''
 /* ---------- SERMONS: full message builds ---------- */
 sermons:function(c){
  const m=this.meta(c), W=m.W, B=BANK[m.cat], s0=seedFrom(c[9]+'ser');
  const bref=(i,j)=>B[(s0+i*7+j*3)%B.length]+' (NIV)';
  const uref=(i,j)=>UNIV[(s0+i*5+j)%UNIV.length]+' (NIV)';
  const ST=[
   ['The Sentence Under the Surface','Getting honest about the need nobody says out loud'],
   ['Truth That Holds','Planting the anchor passage deeper than the circumstances'],
   ['Below the Waterline','Letting God work on the heart before the habits'],
   ['Faith With Work Boots On','Turning conviction into one obedience at a time'],
   ['Nobody Does This Alone','Why this journey was never meant to be private'],
   ['Sent From Here','Carrying what God has done into your everyday world']];
  const IDEAS=[
   [['Name what everyone is carrying','Every person in the room walked in carrying a version of the same sentence: \u201c{need}.\u201d Some have carried it for a week, some for thirty years. The sermon\u2019s first job is not to fix it but to say it out loud \u2014 because in Scripture, honest confession of need is almost always the doorway God walks through.'],
    ['Show them they are not the exception','Isolation convinces people their struggle is unique and therefore hopeless. Walk the congregation through how the people of God \u2014 psalmists, prophets, apostles \u2014 voiced this exact need without being disqualified by it. Normalizing the need removes the shame that keeps people from bringing it to God.'],
    ['Introduce the anchor for the journey','Read {scr} slowly and let it breathe. Tell the church this one passage will be the backbone of the next six weeks \u2014 on their mirrors, in their groups, in their kids\u2019 lessons. One church, one passage, one journey.'],
    ['Lower the bar to entry','People assume a spiritual journey requires spiritual momentum they don\u2019t have. Dismantle that: the only requirement for Day 1 is showing up honest. Grace goes first; God is at the starting line, not just the finish line.'],
    ['Call them into the journey together','End with the invitation: a devotional in every hand, a group for every person, everyone starting Day 1 on the same morning. The ask is specific \u2014 grab the book, join a group, tell one person you\u2019re in.']],
   [['One passage, read like a promise','{scr} is not a motivational quote; it is a promise with the character of God behind it. Preach the context \u2014 who first heard these words, what they were facing \u2014 and then close the distance to the person in row seven facing \u201c{need}.\u201d'],
    ['The old script versus the true script','Everyone runs on internal sentences \u2014 most of them installed by fear, failure, or somebody else\u2019s voice. Scripture replaces scripts by repetition. Show the church how meditation works: same words, turned over daily, until truth outshouts the old tape.'],
    ['Truth is load-bearing','The question is never whether people will build their lives on something \u2014 only whether the foundation holds weight. Contrast the two builders of Matthew 7: identical storms, different outcomes, and the difference was practiced truth.'],
    ['From information to anchor','Bible knowledge that stays in the notebook changes nothing. Give the congregation one concrete habit for the week \u2014 the anchor verse on a card, read aloud each morning \u2014 and explain why spoken truth lands deeper than skimmed truth.'],
    ['A church standing on the same rock','Cast the vision of what happens when a whole congregation memorizes the same promise in the same month \u2014 conversations change, groups deepen, kids quote it at dinner. Shared truth becomes shared culture.']],
   [['Behavior grows from belief','You can rearrange the furniture of a schedule and still live in the same old house. This week the journey goes below the waterline \u2014 to the beliefs about God underneath the behavior. Real change is an inside-out work only grace can do.'],
    ['The fear beneath the need','Underneath \u201c{need}\u201d there is usually a quieter fear \u2014 of not being enough, not being safe, not being loved. Name the fear gently from the pulpit; people cannot surrender what they have never admitted holding.'],
    ['The dangerous prayer','Teach Psalm 139:23\u201324 as this week\u2019s prayer: search me, know me, lead me. God surfaces what He intends to heal, never to shame \u2014 that is His pattern on every page of the Gospels.'],
    ['Grace works from the inside out','Willpower works outside-in and runs out by Thursday. Grace works inside-out and doesn\u2019t. Contrast self-improvement with transformation \u2014 one is managed, the other is surrendered.'],
    ['Slow is not stuck','Heart change is farm work, not factory work. A farmer doesn\u2019t dig up seed to check on it. Free your people from the tyranny of instant results and call them to keep showing up to water the field.']],
   [['Forty small obediences','A journey doesn\u2019t change a life; forty small obediences do. Move the church from inspiration to practice: what, specifically, will be different before the sun goes down tonight?'],
    ['The genius of small','Heaven has never despised small beginnings \u2014 a mustard seed, a boy\u2019s lunch, a cup of cold water. Preach smallness as strategy, not settling: small is how significant starts.'],
    ['Schedule it or lose it','Vague intentions evaporate; scheduled obedience shows up. Teach the sentence \u201cI will ____ at ____\u201d and have the congregation write it in the service. Obedience with a timestamp survives the week.'],
    ['Expect resistance, keep walking','Every new obedience feels awkward the first ten times \u2014 that is formation, not failure. Prepare people for the resistance so it doesn\u2019t surprise them out of the journey.'],
    ['Practice in front of witnesses','Obedience that is witnessed becomes obedience that lasts. Connect this week\u2019s practice to their group and their spiritual partner \u2014 one sentence texted after the step is taken.']],
   [['\u201cYou\u201d was always plural','The New Testament almost never says \u201cyou\u201d singular \u2014 it says \u201cyou all.\u201d Carry each other. Encourage one another. Confess to each other. Preach the grammar: this journey was written to a people, not a person.'],
    ['Isolation is where old patterns hide','What stays hidden stays in charge. James 5:16 ties confession to healing for a reason \u2014 the need loses power the moment it is spoken in a safe circle.'],
    ['The ministry of going first','Every honest group has one person who went first. Call your people to be that person this week \u2014 one layer more honest than comfortable \u2014 and watch what it unlocks for everyone else.'],
    ['Community with skin on','Love is not a feeling the church has; it is a casserole, a text, a chair pulled up. Give three concrete one-anothers for the week and make them small enough that no one can claim exemption.'],
    ['The circle that holds you','Tell the story \u2014 yours or your church\u2019s \u2014 of a circle that held someone when life broke. Then make the ask plain: if you are not in a group, this week is the week. Nobody does this alone.']],
   [['Every journey ends in a sending','Moses came down the mountain with his face shining and a job to do. The final week turns the church from receiving to carrying: what God built in you was never only for you.'],
    ['Take inventory before you take territory','Have the congregation name what actually changed in six weeks \u2014 write it, speak it, thank God for it. Gratitude sets glue on growth; unnamed growth quietly evaporates.'],
    ['Your assignment has a name','Somebody near each of your people is carrying the sentence this journey started with \u2014 \u201c{need}.\u201d Ask God publicly for the name. The next step is usually a text, an invitation, or a table.'],
    ['A new normal, not a finished program','The danger of every campaign is the last page. Give the church its ongoing rhythm \u2014 the group that keeps meeting, the practice that stays daily \u2014 so the journey becomes a lifestyle.'],
    ['Celebrate what God did','End the series the way Scripture ends every rescue: with celebration. Stories, testimonies, a table, a song. Celebration Sunday isn\u2019t a victory lap for the church; it\u2019s worship aimed at the God who moved.']]];
  const OUT=[
   ['Open with the sentence: \u201c{need}\u201d \u2014 let the room feel seen',
    'I. The need we all carry (name it without shame)','II. The God who meets people exactly here (biblical witnesses)','III. The anchor for the journey: {scr}','IV. The only entry requirement: honesty',
    'Landing: grace goes first \u2014 God is at the starting line','Call: take the devotional, join a group, start Day 1 together'],
   ['Open with a story of something that held \u2014 and something that didn\u2019t',
    'I. The promise in context: what {scr} meant then','II. The promise in your kitchen: what it means Monday','III. Old scripts vs. the true script (how meditation rewires)','IV. Two builders, one storm (practiced truth holds)',
    'Landing: truth becomes an anchor through repetition','Call: the anchor verse on a card \u2014 read aloud every morning this week'],
   ['Open with the house metaphor: new furniture, same foundation',
    'I. Behavior grows from belief (below the waterline)','II. The fear beneath \u201c{need}\u201d','III. The dangerous prayer: search me, know me (Psalm 139)','IV. Grace works inside-out; willpower runs out',
    'Landing: slow is not stuck \u2014 heart change is farm work','Call: pray Psalm 139:23\u201324 daily this week and write down what surfaces'],
   ['Open with the two-builders report: same sermon, different outcomes',
    'I. Forty small obediences (how journeys actually change lives)','II. The genius of small (mustard seeds and lunches)','III. \u201cI will ____ at ____\u201d \u2014 obedience with a timestamp','IV. Expect resistance; it\u2019s formation, not failure',
    'Landing: practiced and witnessed \u2014 how habits take','Call: write the sentence, set the time, text your partner tonight'],
   ['Open with the plural \u201cyou\u201d \u2014 the grammar of the New Testament',
    'I. Written to a people, not a person','II. Isolation is where old patterns hide (James 5:16)','III. The ministry of going first','IV. Love with skin on: three one-anothers for this week',
    'Landing: the circle that holds you when life breaks','Call: if you\u2019re not in a group, this is the week \u2014 sign up as you leave'],
   ['Open with Moses coming down the mountain \u2014 shining, and sent',
    'I. Every journey ends in a sending','II. Take inventory: name what God changed','III. Your assignment has a name (who carries the old sentence?)','IV. A new normal: the rhythm that continues',
    'Landing: what He built in you was never only for you','Call: Celebration Sunday \u2014 bring your story, bring your person']];
  return ARCS.map((a,i)=>{
    const fill=t=>t.split('{need}').join(m.need).split('{scr}').join(m.scr).split('{W}').join(W);
    return {n:i+1, wk:'Week '+(i+1)+' \u00b7 '+a.t,
     title:ST[i][0]+': '+W, subtitle:fill(ST[i][1]),
     texts:[ i===0? m.scr+' (NIV)' : bref(i,0), bref(i,1), uref(i,2) ],
     ideas:IDEAS[i].map((id,j)=>({h:(j+1)+'. '+id[0], p:fill(id[1]), refs:[bref(i,3+j), (j%2? uref(i,j): bref(i,8+j))]})),
     outline:OUT[i].map(fill)};
  });
 },
 /* ---------- YOUTH EDITION ---------- */
 youth:function(c){
  const m=this.meta(c), W=m.W, B=BANK[m.cat], s0=seedFrom(c[9]+'yth');
  const bref=(i,j)=>B[(s0+i*9+j*4)%B.length]+' (NIV)';
  const T=[['Real Talk','getting honest about \u201c{need}\u201d \u2014 no church answers allowed'],
   ['Receipts','what God actually says, and why you can trust it'],
   ['Under the Hood','the stuff underneath the stuff'],
   ['Do Something','faith that shows up at school on Monday'],
   ['Your People','why the lone-wolf thing never works'],
   ['Go Time','taking this out of the room']];
  const HOOK=[
   'Everyone answer in one word: how\u2019s life actually going this week? No \u201cfine\u201d allowed.',
   'Would you rather: everyone knows your search history, or everyone knows your 3 a.m. thoughts? Why?',
   'What\u2019s a rule you follow on the outside but argue with on the inside?',
   'What\u2019s the smallest thing you ever did that turned out to matter a lot?',
   'Who\u2019s one person who showed up for you when it counted? What did they do?',
   'If this group had a highlight reel from the last six weeks, what\u2019s on it?'];
  const TALK=[
   'Here\u2019s the honest version: a lot of us walk around carrying the thought \u201c{need}\u201d \u2014 we just get good at hiding it behind grades, jokes, or a highlight feed. Tonight nobody has to perform. God isn\u2019t shocked by the real you; He\u2019s the only one who fully knows it and stays.',
   'Anyone can say \u201ctrust God.\u201d Tonight we look at the receipts \u2014 {scr} \u2014 who it was written to, what they were going through, and why these words have held up for thousands of years of real life, including yours.',
   'Most of us try to fix the outside \u2014 act better, post better, perform better. God starts underneath: the fears and beliefs driving the whole thing. That\u2019s scarier and way better, because whatever He surfaces, He surfaces to heal.',
   'Faith that only exists in this room isn\u2019t faith yet \u2014 it\u2019s a hobby. This week, {W.toLowerCase} gets a body: one small, specific thing you actually do. Small counts. Small is how everything real starts.',
   'The lone-wolf Christian thing sounds cool and works terribly. You were built for a crew \u2014 people who know the real story and stay. Tonight we practice being that for each other.',
   'Six weeks in \u2014 something\u2019s different, even if it\u2019s small. Last step: this was never just for you. Somebody at your school is carrying the exact sentence you started with. You know the way through now.'];
  const QS=[
   ['On a 1\u201310, how much does \u201c{need}\u201d describe your week? Why that number?','Where do you feel it most \u2014 school, home, online, alone at night?','What do you usually do with that feeling: bury it, feed it, or hand it off?','Read the first passage. What surprises you about how honest the Bible is?','What would change if you actually believed God isn\u2019t disappointed you\u2019re here?','What\u2019s one honest sentence you could pray tonight \u2014 for real?'],
   ['What\u2019s a promise somebody broke to you? How does that affect trusting God\u2019s promises?','Read {scr} out loud. What word hits hardest? Why?','What\u2019s the \u201cold script\u201d that plays in your head on bad days?','How is reading a verse every day different from just knowing it exists?','Where could you put this verse so you actually see it \u2014 lock screen, mirror, locker?','Who\u2019s one friend you could send it to this week?'],
   ['What\u2019s the difference between fixing behavior and changing a heart?','What fear might be hiding underneath \u201c{need}\u201d for people our age?','Why is it easier to perform than to be honest?','Read the passages. Which one feels like it\u2019s about the inside of you?','What\u2019s one thing you\u2019d let God \u201csearch\u201d if you knew He\u2019d be gentle with it?','What would praying \u201csearch me\u201d actually look like this week?'],
   ['Why do big intentions usually die by Wednesday?','What\u2019s the smallest real step you could take on this before Friday?','Fill it in out loud: \u201cI will ____ at ____.\u201d','What usually stops you \u2014 forgetting, fear, or friends?','How could this group make your step easier?','Who will you text after you do it?'],
   ['Who actually knows the real you \u2014 not the feed version? ','Why does saying something out loud take its power down?','What makes a group safe enough to be honest in?','Read James 5:16. What\u2019s the connection between honesty and healing?','What\u2019s one layer more honest you could go tonight?','How can we have each other\u2019s backs at school this week \u2014 specifically?'],
   ['What actually changed for you in these six weeks \u2014 even 5%?','Who at your school might be carrying the sentence we started with?','What would \u201cwalking toward them\u201d look like \u2014 realistically?','What\u2019s the one habit from this journey you\u2019re keeping?','How do we keep this group going after the campaign ends?','What\u2019s your one-sentence story of these six weeks?'];
  const CH=[
   'Tell one trusted person the honest version of your week \u2014 this week.',
   'Put the anchor verse on your lock screen and read it out loud every morning.',
   'Pray \u201csearch me\u201d once a day for a week. Write down anything that surfaces.',
   'Do your \u201cI will ____ at ____\u201d step, then text the group a \u2705.',
   'Send one encouraging text a day to somebody in this group. Six days, six people.',
   'Invite one friend to church or to this group before we celebrate.'];
  return {label:'Youth Edition \u00b7 6 Sessions', sessions:ARCS.map((a,i)=>{
    const fill=t=>t.split('{need}').join(m.need).split('{scr}').join(m.scr).split('{W.toLowerCase}').join(W.toLowerCase());
    return {n:i+1, title:'Session '+(i+1)+': '+T[i][0], sub:fill(T[i][1]), hook:HOOK[i], talk:fill(TALK[i]),
     refs:[ i===0? m.scr+' (NIV)' : bref(i,0), bref(i,1), UNIV[(s0+i)%UNIV.length]+' (NIV)'],
     qs:QS[i].map(fill), challenge:CH[i],
     leader:'Leader tip: students smell performance instantly \u2014 answer the first question yourself, honestly, before anyone else. Keep phones in a basket, keep the circle small, and follow up mid-week with one text per student.'};});}
 },
 /* ---------- CHILDREN'S EDITION ---------- */
 children:function(c){
  const m=this.meta(c), W=m.W;
  const L=[
   ['God Sees Me','God knows exactly how I feel \u2014 and He loves me.','Tell the story of the day Jesus stopped for one person in a big crowd (Mark 10:46\u201352). Bartimaeus couldn\u2019t see, and everybody told him to be quiet \u2014 but Jesus stopped, asked what he needed, and helped him. Big crowds don\u2019t hide us from Jesus. He sees each of us, knows how we feel, and wants us to tell Him.','Feelings faces: draw four faces (happy, sad, worried, excited). Ask kids to point to today\u2019s face and finish the sentence \u201cGod, today I feel\u2026\u201d'],
   ['God\u2019s Word Is True','What God says is stronger than what I feel.','Tell the story of the wise and foolish builders (Matthew 7:24\u201327). Two houses looked the same on a sunny day \u2014 the storm showed the difference. Building on the rock means hearing God\u2019s words AND doing them. When we learn a verse by heart, we\u2019re laying a brick on the rock.','Build it: stack blocks on a wobbly pillow, then on the floor. Blow like a storm! Which one stood? Say the memory verse together each time a block goes on the \u201crock.\u201d'],
   ['God Changes Hearts','God helps me on the inside, not just the outside.','Tell the story of Zacchaeus (Luke 19:1\u201310). He climbed a tree to see Jesus \u2014 and Jesus saw HIM. After one meal with Jesus, Zacchaeus\u2019s heart changed, and then his choices changed all by themselves. Jesus doesn\u2019t just want us to act nice on the outside; He makes us new on the inside.','Heart swap: give each child a paper heart. On one side draw a \u201cgrumpy\u201d pattern, flip it for a bright one. Practice: when we ask Jesus, He flips our hearts.'],
   ['I Can Obey Today','Little obediences make God smile.','Tell the story of the boy with the small lunch (John 6:1\u201313). Five loaves and two fish \u2014 tiny! But he gave what he had, and Jesus fed thousands. God loves small gifts given with a big yes. You\u2019re not too little to do something that matters today.','Lunch-bag relay: teams carry a small \u201clunch\u201d across the room and back. Debrief: small things + Jesus = big things. Pick one small kind thing to do at home tonight.'],
   ['We Need Each Other','God gave me friends so we can help each other.','Tell the story of the four friends and the roof (Mark 2:1\u201312). One man couldn\u2019t get to Jesus alone \u2014 so his friends carried him, and even dug through a roof! Some days we\u2019re the carriers; some days we\u2019re the one being carried. That\u2019s exactly how God designed His family.','Stretcher carry: in teams of four, carry a stuffed animal on a blanket around a cone \u2014 gently! Talk: who carries you? Who could you carry this week?'],
   ['I Can Tell Others','My story about Jesus is worth sharing.','Tell the story of the boy Samuel (1 Samuel 3). God spoke, and Samuel answered, \u201cSpeak, Lord, I\u2019m listening\u201d \u2014 and then told others what God said, even though he was young. Kids aren\u2019t the church of tomorrow; you\u2019re part of God\u2019s team today, and your voice counts.','Telephone \u2014 truth edition: whisper the Big Truth around the circle; say it loud together at the end. Then practice one sentence each child could tell a friend this week.']];
  return {label:'Children\u2019s Edition \u00b7 6 Lessons', lessons:ARCS.map((a,i)=>{
    const mem=memFor(c,m,i);
    return {n:i+1, title:'Lesson '+(i+1)+': '+L[i][0], big:'Big Truth: '+L[i][1], story:L[i][2],
      mem, activity:L[i][3],
      qs:['What was your favorite part of the story?','When could you remember the Big Truth this week \u2014 at home, at school, at bedtime?','What\u2019s one thing you want to tell God right now?'],
      family:'Family takeaway: at dinner or bedtime, ask your child to teach YOU the Big Truth and say the memory verse together. One question to ask: \u201cWhere did you see God today?\u201d'};});}
 },
 /* ---------- LEADER TRAINING & RECRUITMENT ---------- */
 leaderKit:function(c){
  const m=this.meta(c), W=m.W;
  return {label:'Leader Training & Recruitment Kit',
   training:{
    role:'You do not need to be a Bible scholar, a teacher, or \u201cready.\u201d A host is a facilitator with a living room and a willing heart: you open the door, press play on the questions, and keep the circle honest and moving. God supplies the growth; you supply the chairs.',
    points:[
     {h:'1. Set the temperature, not the agenda',p:'Groups take their emotional cues from the leader in the first ten minutes. Arrive settled, greet everyone by name, and answer the opening question honestly yourself \u2014 first. Your realness gives everyone else permission.'},
     {h:'2. Ask, then wait eight seconds',p:'The most common leader mistake is fearing silence. After a question, count eight slow seconds before rescuing the room \u2014 the best answers live on the far side of the pause. Draw out the quiet ones by name, gently: \u201cWhat do you think, Sam?\u201d'},
     {h:'3. Keep it honest and keep it moving',p:'Your two jobs in every discussion: depth and momentum. If sharing turns to speeches, honor it and redirect \u2014 \u201cThat\u2019s good; let\u2019s hear another voice.\u201d If the room stays shallow, go one layer deeper yourself and watch the circle follow.'},
     {h:'4. Land the practice before you close',p:'A session without a next step is a conversation, not a journey. In the last ten minutes, make sure every person names their one step for the week \u2014 specific enough to text a \u2705 about.'},
     {h:'5. Shepherd between the sessions',p:'The meeting is a third of the ministry. One text per person mid-week \u2014 \u201cpraying for your step, how\u2019s it going?\u201d \u2014 doubles what happens in the room. Nobody does this alone, including you: debrief weekly with your co-leader or coach.'}],
    firstNight:['Chairs in a circle, snacks out, phones in a basket','Name tags for week one \u2014 yes, really','Open with the icebreaker; answer it first yourself','Read the group agreement: confidentiality, no fixing, everyone shares airtime','Keep session one to 75 minutes \u2014 end wanting more','Close by trading numbers and scheduling week two out loud'],
    care:['If someone shares something heavy: thank them, don\u2019t fix them, follow up privately within 24 hours.','If a pastoral issue surfaces beyond the group\u2019s depth, loop in your campus pastor \u2014 you are a shepherd, not a counselor.','Pray for your roster by name once a week; it changes how you see the room.']},
   recruit:{
    pulpit:'\u201cChurch, in three weeks we begin '+c[0]+' \u2014 all of us, together. And here\u2019s what I need: living rooms. If you have a couch, a coffee pot, and a willing heart, you can host a group. You don\u2019t need to be a teacher \u2014 the material does the heavy lifting, we\u2019ll train you this Sunday after service, and I\u2019ll be with you every step. Would you take one card as you leave and pray one dangerous prayer: God, is this me?\u201d',
    personal:'\u201cHey \u2014 when I prayed about who could host a group for '+c[0]+', your name kept coming up. Before you say you\u2019re not qualified: it\u2019s your living room, six weeks, questions provided, and I\u2019ll train you and back you the whole way. Would you pray about it and give me an answer by Sunday?\u201d',
    timeline:['T-3 weeks \u2014 Cast vision from the pulpit; hand out host cards; open sign-ups','T-2 weeks \u2014 Host training after each service (45 minutes); confirm rosters and homes','T-1 week \u2014 Commission hosts publicly in the service; final push: \u201ceveryone in a group by Sunday\u201d'],
    faq:[{q:'\u201cI\u2019ve never led anything.\u201d',a:'Perfect \u2014 our best hosts usually start there. The curriculum carries the content; you carry the coffee.'},
     {q:'\u201cMy home is too small / too messy.\u201d',a:'Lived-in beats impressive every time. Six chairs and a door that opens is the whole requirement.'},
     {q:'\u201cWhat if they ask a question I can\u2019t answer?\u201d',a:'Say the four magic words: \u201cGreat question \u2014 I\u2019ll find out.\u201d Then ask your coach. Nobody expects a seminary.'},
     {q:'\u201cHow long am I committing for?\u201d',a:'Six weeks. That\u2019s the whole ask. Most hosts choose to keep going \u2014 but the commitment ends with the campaign.'}]}};
 },
 launchKit:'''

e2=re.sub(r" sermons:function\(c\)\{.*?\n \},\n launchKit:", NEW, e, flags=re.S)
assert e2!=e and 'youth:function' in e2 and 'children:function' in e2 and 'leaderKit:function' in e2
open(O+'engine.js','w').write(e2)
print('engine upgraded:', len(e2),'bytes')
