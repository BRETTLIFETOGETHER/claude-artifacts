/* Editions layer — Youth and Kids & Family, generated from the same
   verse-bound day atoms as the adult engine. Authored pools, per-campaign
   dealt decks (no repeats until pool exhaustion), editable Word output. */
(function(){
"use strict";
const E=window.Engine;
function mul(a){return function(){a|=0;a=a+0x6D2B79F5|0;var t=Math.imul(a^a>>>15,1|a);t=t+Math.imul(t^t>>>7,61|t)^t;return((t^t>>>14)>>>0)/4294967296}}
function seed(s){let h=2166136261;for(let i=0;i<s.length;i++){h^=s.charCodeAt(i);h=Math.imul(h,16777619)}return h>>>0}
const DECKS={};
function deal(id,slot,pool,i){
 const k=id+"|"+slot, cyc=Math.floor(i/pool.length), key=k+"|"+cyc;
 if(!DECKS[key]){const r=mul(seed(key));const d=pool.map((_,x)=>x);
  for(let j=d.length-1;j>0;j--){const q=Math.floor(r()*(j+1));[d[j],d[q]]=[d[q],d[j]]}
  DECKS[key]=d}
 return pool[DECKS[key][i%pool.length]];
}
function esc(s){return String(s).replace(/&/g,"&amp;").replace(/</g,"&lt;")}

/* ---------------- YOUTH ---------------- */
const Y_HOOK=[
"Be honest: would the people who see you every day say this is true of you?",
"Nobody posts about this part of their life. That is exactly why it matters.",
"You have felt this in a hallway before — the moment everyone is watching and no one is looking.",
"There is a version of you that shows up online and a version that shows up at 11pm. Today is for the second one.",
"Some things you cannot skip, screenshot, or speed up. This is one of them.",
"You already know somebody who needs today's verse. It might be you.",
"The quiet kid in your class understands this better than most adults. Ask yourself why.",
"If your week had a caption, what would it be? Hold that thought.",
"This is not about trying harder. You have tried harder. This is about something else.",
"Everyone is performing something. Today you get to stop for ten minutes.",
"You do not need more information. You need one honest minute. This is it.",
"Somewhere between first period and practice, you decided some things about yourself. Let's check them.",
"The pressure you feel is real. So is what God says about it. Both can be true at once.",
"Today's reading is short on purpose. What it asks of you is not.",
"You can fake a lot of things. You cannot fake peace. Keep reading.",
"If God actually meant this verse, something in your week has to change. Find out what."
];
const Y_REAL=[
"Here is the thing about {W}: it does not wait until you are older to matter.",
"{W} is not a church word. It is a Tuesday word — it shows up in group chats, tryouts, and the seat you choose at lunch.",
"Most people your age think {W} is for someday. Scripture treats it like it is for today.",
"You will make a decision about {W} this week whether you notice it or not. Better to notice.",
"Adults talk about {W} like it is complicated. The verse you just read makes it startlingly simple.",
"{W} is decided in small, unphotographed moments. You will get about three of them today.",
"The world has a counterfeit version of {W}. It looks similar and costs more. Learn the difference now.",
"Your friends are already teaching you their version of {W}. Today God gets a turn.",
"If {W} were easy, everyone would have it. The verse tells you where it actually comes from.",
"You cannot inherit {W} from your parents or download it from anyone. It gets built — starting today.",
"{W} at your age is not smaller than {W} at forty. It is the foundation version. Foundations matter most.",
"Nobody drifts into {W}. People drift away from it. Today is a steering day."
];
const Y_DARE=[
"Send one honest text you have been avoiding. Today.",
"Sit somewhere new at lunch and learn one name you did not know this morning.",
"Say the true thing out loud to one person — kindly, but actually say it.",
"Put your phone in another room for thirty minutes and let the quiet happen.",
"Thank one adult specifically — name the thing they did. Watch their face.",
"Do the chore nobody asked you to do, and tell no one.",
"Write today's verse on your hand or your mirror. Let it interrupt you.",
"Ask a friend a second question after they answer the first one. Then actually listen.",
"Give away something you like — not something you were done with.",
"Apologize for the thing you have been justifying. Short and real beats long and polished.",
"Invite the person who is always on the edge of the group into the middle of it.",
"Skip one thing you always do and use that time to pray for three people by name.",
"Tell your parent or guardian one true thing about your week — the real version.",
"Encourage somebody who competes with you. Mean it.",
"Stand up for someone today even if it costs you social points. Especially then.",
"Fast one app until sunset. Notice what you reach for instead.",
"Write down the lie you believe most often. Then write today's verse under it.",
"Pray with your eyes open on the way to school — whole trip, no music."
];
const Y_TALK=[
"Where does this get hardest for you — school, home, online — and why there?",
"Who do you know that actually lives this out? What is different about them?",
"What would change in your friend group if you took today's verse seriously?",
"What is the cost of doing this at your age? Is it worth it? Be honest.",
"When did you last feel the opposite of today's word? What happened?",
"If a younger student asked you about this, what would you tell them?",
"What is one thing adults get wrong about this — and one thing they get right?",
"Which is harder for you: believing this is true, or acting like it is? Why?",
"What would you have to stop doing to start doing this?",
"Where have you already seen God do this in your life, even a little?",
"Who makes it easier for you to live this way? Who makes it harder?",
"If you did today's dare, what happened? If you skipped it, what stopped you?",
"What scares you about taking this seriously?",
"What is one place this week you can practice this where nobody will see?"
];
const Y_PRAY=[
"God, I do not want to fake this part. Make it real in me, starting with today.",
"Jesus, you know what my week actually looks like. Meet me in the true version, not the posted one.",
"Father, I believe — help the part of me that is still deciding.",
"God, give me the guts to do today's dare and the honesty to admit if I do not.",
"Jesus, be louder than the voices I listen to most. You know which ones.",
"God, I want the real thing, not the performance. Start wherever you need to.",
"Father, make this verse true of me before anyone is watching.",
"Jesus, I hand you the thing I keep taking back. You know what it is.",
"God, use me today for someone who feels invisible. Show me who.",
"Father, I am tired of pretending I am fine. Today I would rather be honest with you.",
"Jesus, make my private life match my public one — and make both look like you.",
"God, thank you that you are not waiting for me to be older to take me seriously."
];

function youthDay(o,fmt,i,n){
 const d=E.day(o,fmt,i,n);
 const W=(d.word||"").toLowerCase();
 return {unit:d.unit,n:d.n,title:d.title||d.word,ref:d.ref,word:d.word,sunday:d.sunday,
  hook:deal(o.id,"yhook",Y_HOOK,i),
  real:deal(o.id,"yreal",Y_REAL,i).replace(/\{W\}/g,W),
  truth:d.truth,
  dare:deal(o.id,"ydare",Y_DARE,i),
  q1:d.q, q2:deal(o.id,"ytalk",Y_TALK,i),
  pray:deal(o.id,"ypray",Y_PRAY,i)};
}
function youthHTML(d){
 return `<h2>${esc(d.word)}</h2><p class="muted">${esc(d.unit)} ${d.n} · Read ${esc(d.ref)} — twice, slowly.</p>
<p><b>Straight up.</b> ${esc(d.hook)}</p>
<p>${esc(d.real)}</p>
<p><i>${esc(d.truth)}</i></p>
<p><b>The dare.</b> ${esc(d.dare)}</p>
<p><b>Talk it out.</b> ${esc(d.q1)}</p>
<p>${esc(d.q2)}</p>
<p><b>Pray it.</b> ${esc(d.pray)}</p>`;
}

/* ------------- KIDS & FAMILY (Table Talk) ------------- */
const K_WONDER=[
"If kindness had a color at our table tonight, what color would it be — and why?",
"What is one thing that made you laugh today? Tell the long version.",
"If our family had a team name for this week, what should it be?",
"What is something you saw today that you think God was happy about?",
"Who was brave today — you, or someone you watched? What happened?",
"If you could give one person in this house a prize tonight, who gets it and for what?",
"What sound would today make if it were a song — loud, quiet, bouncy, slow?",
"What is one thing you are wondering about God lately? Any question counts.",
"If tonight's dinner could talk, what would it say about our family?",
"What was the hardest part of today? You can say it. We are listening.",
"Who needed a friend today? Did they find one?",
"If we could send one giant thank-you balloon into the sky tonight, whose name goes on it?",
"What is something you can do now that you could not do last year?",
"If Jesus sat in the empty chair tonight, what would you want to ask him first?",
"What made someone at this table smile today? Catch them telling it.",
"What is one small thing we could do as a family tomorrow that would make someone's day better?"
];
const K_FRAME=[
"Hand the Bible to the youngest reader who can. Everyone else, listen with your eyes closed.",
"Read it once in a normal voice, then once in a whisper. Which way made you listen harder?",
"Have two people read it — one verse-half each — like passing a ball.",
"Read it slowly. Every time you hear God's name, everyone taps the table once.",
"Let the oldest person read it tonight, the way they wish someone had read it to them.",
"Read it, then have everyone say the one word they remember most.",
"Read it twice. The second time, stop before the last word and let the family finish it.",
"One person reads; everyone else holds one hand open on the table, ready to receive it."
];
const K_BIG=[
"Big idea: God's {W} is for our whole house — even the smallest person at this table.",
"Big idea: {W} is something our family can practice together, one small day at a time.",
"Big idea: God does not wait for us to be grown-ups to give us {W}.",
"Big idea: {W} starts at home — at this table, in these chairs, tonight.",
"Big idea: when one of us practices {W}, the whole family gets stronger.",
"Big idea: God loves to grow {W} in families that ask him for it.",
"Big idea: {W} is not just for church. It is for kitchens, cars, and bunk beds.",
"Big idea: our family does not have to be perfect for God to build {W} in us.",
"Big idea: little steps of {W} count. God sees every one.",
"Big idea: tonight, {W} has a seat at our table."
];
const K_Q=[
"When did someone make room for you this week? How did it feel?",
"What is one way our family already does this — and one way we could do it more?",
"Who do we know who needs this right now? What could we do for them this week?",
"What makes this hard for kids? What makes it hard for grown-ups?",
"If you practiced this at school or work tomorrow, what would you do first?",
"When have you seen someone in this family do this? Tell the story.",
"What would our home feel like if we did this every single day?",
"What is one word from tonight's verse you want to keep? Why that one?",
"Who taught you about this first? What did they do?",
"If we forget everything else, what is the one thing from tonight to remember?",
"What is something you want to ask God for help with this week?",
"How could we surprise someone with this before Sunday?",
"What part of tonight's verse sounds like good news to you?",
"Where in our week is the best time to practice this together?"
];
const K_DO=[
"Everyone writes or draws one worry on paper. Fold them into the middle of the table and pray over the pile together.",
"Go around twice: first time say one thank-you, second time say one hope for tomorrow.",
"Make a family high-five chain — each person adds one word of tonight's verse as you go.",
"Pick one person this family will secretly encourage this week. Plan it right now.",
"Everyone points to someone at the table and says one true, kind sentence about them.",
"Draw tonight's verse as a picture in two minutes. Stick the drawings on the fridge.",
"Build the verse: each person says the next word from memory until the family finishes it.",
"Choose a family signal — a word or a hand sign — that means 'remember tonight's verse.' Practice it three times.",
"Set a one-minute timer and let everyone say prayer requests fast — popcorn style.",
"Trade chairs with the person across from you and say one thing you appreciate about their spot in this family.",
"Plan one small act of generosity for a neighbor this week. Put it on the calendar before you leave the table.",
"Everyone holds hands and squeezes a 'pulse' around the circle while one person prays.",
"Write tonight's one big word on a sticky note for every bedroom door.",
"Let the youngest choose a motion for tonight's word. Everyone does it together on the count of three.",
"Each person names one place they will see tomorrow — home, school, work — and how the verse could show up there.",
"Make tomorrow's breakfast plan include one act of kindness. Decide who does what.",
"Have everyone whisper the verse to the person on their left, all the way around, like the best kind of telephone.",
"Pick a family memory that matches tonight's word. Let two people tell it together."
];
const K_PRAY=[
"God, thank you for this table and every person around it. Grow tonight's big word in our house. Amen.",
"Father, you know each name here. Help our family practice this together tomorrow. Amen.",
"Jesus, thank you for being with us at dinner and at bedtime. Make our home look more like you. Amen.",
"God, bless the person each of us thought of tonight. Show our family how to love them well. Amen.",
"Father, thank you for the laughing parts and the hard parts of today. We give you both. Amen.",
"Jesus, help the smallest and the biggest person in this house believe tonight's verse. Amen.",
"God, make our family brave enough to do what we planned tonight. Amen.",
"Father, watch over everyone who could not be at this table tonight. Keep them close to you. Amen.",
"Jesus, we want our home to be a place where you feel welcome. Come be with us. Amen.",
"God, thank you that we do not have to be perfect to be yours. Hold this family together. Amen.",
"Father, tuck tonight's verse into our dreams and wake us up ready to live it. Amen.",
"Jesus, thank you for stories, food, and each other. Teach us your way all week. Amen."
];

function kidsDay(o,fmt,i,n){
 const d=E.day(o,fmt,i,n);
 const W=(d.word||"").toLowerCase();
 return {unit:d.unit,n:d.n,title:d.title||d.word,ref:d.ref,word:d.word,sunday:d.sunday,
  wonder:deal(o.id,"kwon",K_WONDER,i),
  frame:deal(o.id,"kfrm",K_FRAME,i),
  big:deal(o.id,"kbig",K_BIG,i).replace(/\{W\}/g,W),
  q:deal(o.id,"kq",K_Q,i),
  act:deal(o.id,"kdo",K_DO,i),
  pray:deal(o.id,"kpray",K_PRAY,i)};
}
function kidsHTML(d){
 return `<h2>${esc(d.word)}</h2><p class="muted">${esc(d.unit)} ${d.n} · Table Talk for the whole family</p>
<p><b>Wonder together.</b> ${esc(d.wonder)}</p>
<p><b>Read together — ${esc(d.ref)}.</b> ${esc(d.frame)}</p>
<p><i>${esc(d.big)}</i></p>
<p><b>Family question.</b> ${esc(d.q)}</p>
<p><b>Do together.</b> ${esc(d.act)}</p>
<p><b>Table prayer.</b> ${esc(d.pray)}</p>`;
}

function fullDoc(o,fmt,n,dayFn,htmlFn,label){
 let h=`<h1>${esc(o.t)} — ${label}</h1><p><i>${esc(o.s||"")}</i></p>`;
 for(let i=0;i<n;i++){h+=`<hr/>`+htmlFn(dayFn(o,fmt,i,n))}
 return E.docWrap(`${o.t} — ${label}`,h);
}
window.Editions={
 youthDay,youthHTML,kidsDay,kidsHTML,
 fullYouth:(o,fmt,n)=>fullDoc(o,fmt,n,youthDay,youthHTML,"Youth Edition"),
 fullKids:(o,fmt,n)=>fullDoc(o,fmt,n,kidsDay,kidsHTML,"Kids & Family Edition")
};
})();
