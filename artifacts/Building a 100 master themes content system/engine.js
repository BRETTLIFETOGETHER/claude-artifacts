/* Lifetogether Content Engine — composes complete curriculum for any campaign.
   Voice: pastoral, plain, felt-need first, one small obedience per day. */
(function(){
'use strict';

/* ---------- seeded randomness (deterministic per campaign) ---------- */
function seedFrom(str){let h=2166136261;for(let i=0;i<str.length;i++){h^=str.charCodeAt(i);h=Math.imul(h,16777619);}return h>>>0;}
function rng(seed){let s=seed||1;return function(){s=Math.imul(48271,s)%2147483647;return (s&2147483647)/2147483648;};}
function pick(r,arr){return arr[Math.floor(r()*arr.length)];}

/* ---------- Scripture banks (NIV references, curated per category) ---------- */
const UNIV=["Psalm 23:1-6","Psalm 46:1-3","Psalm 62:5-8","Psalm 103:1-5","Psalm 121:1-8","Psalm 139:1-10",
"Isaiah 40:28-31","Lamentations 3:22-24","Romans 8:28-32","Romans 12:1-2","2 Corinthians 12:9-10",
"Philippians 1:6","Colossians 3:1-4","Hebrews 12:1-3","James 1:2-5","1 Peter 5:6-7"];
const BANK={
1:["Ephesians 2:8-10","Psalm 139:13-16","Jeremiah 1:4-8","1 Peter 2:9-10","Genesis 1:26-28","Romans 12:3-8",
"1 Corinthians 12:4-7","Esther 4:12-14","Exodus 3:9-12","Isaiah 43:1-4","Galatians 2:20","2 Timothy 1:6-9",
"Matthew 5:13-16","John 15:15-16","Acts 17:26-28","Proverbs 16:3-4","Isaiah 6:1-8","Colossians 1:15-17",
"Judges 6:11-16","1 Samuel 16:6-7","Luke 5:1-11","Ephesians 1:3-6","Philippians 3:12-14","Psalm 57:2"],
2:["Philippians 4:4-9","John 14:25-27","Matthew 11:28-30","Isaiah 26:3-4","Psalm 4:6-8","Matthew 6:25-34",
"1 Peter 5:6-11","Psalm 94:18-19","Isaiah 41:10-13","2 Timothy 1:7","Psalm 34:4-8","John 16:31-33",
"Exodus 33:12-14","Psalm 91:1-6","Proverbs 3:21-26","Mark 4:35-41","Psalm 127:1-2","Zephaniah 3:17",
"Psalm 42:5-8","1 Kings 19:3-9","Habakkuk 3:17-19","Romans 15:13","Psalm 116:5-9","Nehemiah 8:9-12"],
3:["1 Corinthians 13:4-8","Ephesians 4:29-32","Colossians 3:12-15","Genesis 2:22-25","Ecclesiastes 4:9-12",
"Ephesians 5:25-33","Song of Songs 8:6-7","Proverbs 15:1-4","James 1:19-21","Ruth 1:16-17","1 John 4:7-12",
"Philippians 2:1-5","Proverbs 17:17","Matthew 19:4-6","Romans 12:9-13","1 Peter 4:8-10","Proverbs 31:10-12",
"Hosea 2:19-20","Matthew 5:23-24","Proverbs 27:17","Galatians 6:1-2","Malachi 2:13-16","John 13:34-35","Genesis 29:20"],
4:["Deuteronomy 6:4-9","Psalm 78:1-7","Proverbs 22:6","Joshua 24:14-15","Psalm 127:3-5","Ephesians 6:1-4",
"2 Timothy 1:3-5","Psalm 103:17-18","Deuteronomy 4:9-10","Proverbs 1:8-9","Psalm 71:17-18","Genesis 18:17-19",
"Exodus 12:24-27","Isaiah 38:19","Proverbs 13:22","3 John 1:4","Luke 2:41-52","Psalm 145:3-7",
"Mark 10:13-16","Proverbs 6:20-22","1 Samuel 1:26-28","Titus 2:1-8","Deuteronomy 11:18-21","Psalm 128:1-4"],
5:["Proverbs 3:9-10","Matthew 6:19-24","1 Timothy 6:6-10","Luke 12:15-21","Psalm 24:1-2","Proverbs 21:5",
"1 Timothy 6:17-19","Philippians 4:11-13","Proverbs 22:7","Ecclesiastes 5:10-12","Matthew 25:14-21","Luke 16:10-13",
"Proverbs 13:11","Hebrews 13:5","Deuteronomy 8:17-18","Proverbs 6:6-8","Haggai 1:5-7","Malachi 3:8-10",
"2 Corinthians 9:8","Proverbs 30:7-9","Luke 14:28-30","Psalm 37:21-26","Proverbs 11:24-25","1 Chronicles 29:11-14"],
6:["2 Corinthians 9:6-11","Acts 20:32-35","Luke 6:38","Proverbs 11:24-25","2 Corinthians 8:1-5","Matthew 6:1-4",
"1 Timothy 6:17-19","Malachi 3:10-12","Mark 12:41-44","1 Chronicles 29:14-17","Deuteronomy 15:7-11","Luke 12:32-34",
"Proverbs 19:17","Hebrews 13:16","2 Corinthians 8:9","Psalm 112:5-9","Isaiah 58:10-11","Luke 21:1-4",
"Romans 12:13","Galatians 6:9-10","Matthew 10:8","Acts 4:32-35","Proverbs 22:9","John 3:16"],
7:["Luke 9:23-25","John 15:1-8","Colossians 2:6-7","Psalm 1:1-3","Matthew 4:18-22","Matthew 11:28-30",
"John 8:31-32","Philippians 3:7-11","2 Peter 3:18","Galatians 5:22-25","Romans 8:5-11","Psalm 119:9-16",
"Joshua 1:8-9","Matthew 7:24-27","1 Thessalonians 5:16-18","Hebrews 5:12-14","John 13:12-17","Luke 14:25-33",
"Mark 1:35-39","Psalm 63:1-5","Acts 2:42-47","Ephesians 3:16-19","2 Timothy 3:14-17","John 10:27-28"],
8:["Acts 2:42-47","Hebrews 10:24-25","Romans 12:4-5","1 Corinthians 12:12-27","Galatians 6:2","John 13:34-35",
"Ecclesiastes 4:9-12","1 Thessalonians 5:11","Ephesians 4:1-6","Colossians 3:12-14","1 Peter 4:8-10","Romans 15:5-7",
"Philippians 2:1-4","James 5:16","Proverbs 27:17","Acts 4:32-35","1 John 1:5-7","Romans 12:10",
"Genesis 2:18","Matthew 18:19-20","Hebrews 3:12-13","2 Corinthians 1:3-4","Psalm 133:1-3","Luke 24:28-32"],
9:["Romans 5:1-5","2 Corinthians 4:7-9","Psalm 34:17-19","Isaiah 43:1-3","Romans 8:35-39","James 1:2-4",
"Psalm 30:4-5","2 Corinthians 4:16-18","1 Peter 1:3-7","Psalm 42:11","Isaiah 61:1-3","John 16:33",
"Lamentations 3:19-26","Psalm 34:18","Revelation 21:3-5","Joel 2:25-27","Psalm 27:13-14","Habakkuk 3:17-19",
"2 Corinthians 1:3-5","Job 42:10-12","Psalm 126:5-6","Hebrews 6:19","Romans 15:13","Matthew 5:4"],
10:["Matthew 28:18-20","Acts 1:8","2 Corinthians 5:17-20","Matthew 5:14-16","John 20:21","Romans 10:13-15",
"1 Peter 3:15-16","Jeremiah 29:4-7","Luke 10:25-37","Micah 6:8","Isaiah 58:6-9","Matthew 25:34-40",
"Colossians 4:2-6","Acts 8:26-31","Luke 19:1-10","Psalm 96:1-3","Matthew 9:35-38","Philemon 1:6",
"2 Timothy 4:6-8","Psalm 71:17-18","Isaiah 6:8","Acts 13:36","John 4:35-38","1 Corinthians 15:58"]};

/* ---------- week arcs (6 movements of every journey) ---------- */
const ARCS=[
 {t:"Naming the Need", f:"getting honest about where we are, and why God's Word speaks to it"},
 {t:"The Truth Beneath", f:"planting the anchor passage deep, so truth outshouts the old scripts"},
 {t:"A Changed Heart", f:"letting God work below the surface — motives, fears, and hopes"},
 {t:"Putting It Into Practice", f:"turning conviction into daily habits and small obediences"},
 {t:"Never Alone", f:"walking it out with others — because nobody does this alone"},
 {t:"Sent to Live It", f:"carrying what God has done into your home, work, and world"}];

/* ---------- day title banks by phase ---------- */
const DTITLES=[
 ["Where This Journey Begins","The Sentence Under the Surface","Getting Honest","Why This, Why Now","The God Who Meets You Here","Starting Where You Are","The First Step Is Showing Up"],
 ["The Anchor Passage","Truth That Holds","What God Actually Says","Reading It Slowly","The Promise Behind the Verse","Old Words, Present Power","Write It on the Doorframe"],
 ["The Heart of the Matter","Below the Waterline","What You Really Believe","Trading Lies for Truth","The Fear Beneath","New Desires","A Heart Set Free"],
 ["One Small Obedience","Practice Makes Faithful","The Daily Choice","Habits of the Heart","Do It Today","The Ten-Minute Difference","Faithful in Little"],
 ["Better Together","Tell Someone","The Gift of Being Known","Carrying Each Other","Two Are Better","Your Spiritual Partner","The Circle That Holds You"],
 ["Sent From Here","Living It Out Loud","What You'll Take With You","The Story You'll Tell","Passing It On","A New Normal","The Journey Continues"]];

/* ---------- reflection paragraph templates ({W},{need},{theme},{aud},{scr},{title}) ---------- */
const P1=[ // openers by phase
 ["Every journey like this one starts with a sentence — a quiet, honest sentence most of us have thought but rarely said out loud: \u201c{need}.\u201d If that sentence sounds familiar, take a breath. You are not the only one, and you are not without hope. God has been meeting people exactly here for thousands of years.",
  "Be honest for a moment: how long have you carried this? {need} isn\u2019t just a thought that visits occasionally — for many of us it has become the background music of our lives. Today, we stop pretending it isn\u2019t playing. Naming a need is not weakness; in Scripture, it is almost always the doorway to grace.",
  "Jesus had a habit of asking questions He already knew the answers to — \u201cWhat do you want me to do for you?\u201d He asks not because He is uninformed, but because something happens in us when we say it out loud. So say it: \u201c{need}.\u201d That honest sentence is the soil this whole journey grows in."],
 ["Today we slow down inside the anchor passage for this journey — {scr}. Don\u2019t rush it. Read it twice. Notice who it was written to, and what was happening when it was written. This is not a fortune cookie; it is a promise with the character of God behind it.",
  "There\u2019s a difference between knowing a verse and being held by it. {scr} was written into real dust, real disappointment, real life — and it speaks into yours. The goal this week is not to memorize information but to let one passage move from your head to your bones.",
  "The people of God have always fought their battles with borrowed words. When the old script starts again — \u201c{need}\u201d — you need a truer sentence ready. That is what {scr} is for. Write it somewhere you\u2019ll see it every morning of this journey."],
 ["Real change never happens only at the level of behavior. Underneath every habit is a hope, and underneath every hope is a belief about God. This week, we let God work below the waterline — not just what you do about {W.toLowerCase}, but what you believe when no one is asking.",
  "The heart, Scripture says, is where life flows from. You can rearrange the furniture of your schedule and still live in the same old house. So this week the question gets personal: what is the fear underneath, and what would it mean to hand it — actually hand it — to God?",
  "Grace works from the inside out. Willpower works from the outside in, and it runs out by Thursday. The difference in this journey will not be your discipline; it will be what happens in your heart when God\u2019s truth and your honesty finally sit in the same room."],
 ["Forty days doesn\u2019t change a life. Forty small obediences do. Today the journey turns practical — not what you feel about {W.toLowerCase}, but what you will do about it before the sun goes down. Small is not the enemy of significant. Small is how significant starts.",
  "Jesus ended His most famous sermon with a construction report: two builders, two foundations, one storm. The difference wasn\u2019t information — both heard the same words. The difference was practice. Today, pick the smallest brick you can actually lay, and lay it.",
  "There is a version of faith that stays in the notebook. God is inviting you into the other kind — the kind with calluses. Ask Him one question this morning and mean it: \u201cWhat is the one thing You want me to do about this today?\u201d Then do that one thing."],
 ["Whatever God is doing in you through this journey, He did not design it to stay private. Nobody does this alone — not because we\u2019re weak, but because we were built for it. Isolation is where old patterns hide; community is where they heal.",
  "Somewhere in your life there is a person who needs to hear what God is teaching you — and whose voice you need in return. Call them your spiritual partner, your friend, your group; the title matters less than the honesty. Growth that is witnessed becomes growth that lasts.",
  "The New Testament almost never says \u201cyou\u201d singular. It says \u201cyou all\u201d — carry each other, encourage one another, confess to each other. This week, let someone into what God is doing. It will feel risky. It is also how everything good gets multiplied."],
 ["Every journey with God ends in a sending. What He has been building in you these weeks was never only for you — it\u2019s for your home, your work, your street. The question of this final stretch is simple: what will be different on the first ordinary Tuesday after this ends?",
  "Moses came down the mountain with his face shining and a job to do. You don\u2019t get to stay on the mountain either. Take stock today: what has actually changed? Name it, thank God for it, and then ask Him where He wants to spend it.",
  "The best evidence of these weeks will not be your notes; it will be your neighbors. As this journey closes, God is turning you outward. Somebody near you is carrying the same quiet sentence you started with — and now you know the way through."]];
const P2=[ // second paragraphs by phase
 ["So begin simply. Read today\u2019s passage slowly. Underline one phrase that feels like it was written for you. Then invite God into these days — not to watch you try harder, but to do in you what you have not been able to do in yourself. That\u2019s what this journey is for.",
  "Here\u2019s the good news you can stand on today: God is not waiting at the finish line of this journey, disappointed you took so long. He is here at the starting line, glad you came. Grace goes first. Everything else in these days flows from that.",
  "One more thing before you go: tell one person you\u2019re starting this. Not for accountability points — because spoken intentions grow roots. A journey announced is a journey begun."],
 ["Try this today: read the anchor passage out loud, once, slowly. Hearing truth in your own voice does something silent reading can\u2019t. Then carry one phrase with you — on a card, on your phone, on the bathroom mirror — and let it interrupt you all day.",
  "Scripture calls itself a lamp — not a floodlight. It rarely shows the whole road; it reliably shows the next step. That\u2019s enough. Trust the passage for today\u2019s step and let tomorrow\u2019s worry wait for tomorrow\u2019s light.",
  "Truth becomes conviction through repetition. Athletes call it reps; the psalmists called it meditation — day and night, turning the words over like a stone in your pocket. Give this passage its reps this week and watch what it starts to carry."],
 ["Pray dangerously today: \u201cSearch me, God, and know my heart.\u201d Not because He needs the report — because you need the honesty. What He surfaces, He surfaces to heal, never to shame. That is His pattern on every page of the Gospels.",
  "Notice your self-talk today — the sentences that run when things go wrong. Write down the loudest one tonight. Then set it next to this week\u2019s passage and ask the simple question: which of these voices is telling the truth?",
  "Change of heart is slow work, and slow is not the same as stuck. A farmer doesn\u2019t dig up seeds to check on them. Give God the field, keep showing up to water it, and trust the growth to the only One who has ever made anything grow."],
 ["Make it concrete before you close this page: what, where, when. \u201cI will ____ at ____ today.\u201d Vague intentions evaporate; scheduled obedience shows up. And when you do it — however small — tell your spiritual partner one sentence about it. Practiced and witnessed: that\u2019s how habits take.",
  "Expect resistance today, and don\u2019t be alarmed by it. Every new obedience feels awkward the first ten times — that\u2019s not failure, that\u2019s formation. The awkwardness is the feeling of a new path being walked into the grass.",
  "Remember the scale God works on: a mustard seed, a boy\u2019s lunch, a cup of cold water. Heaven has never despised a small beginning. Neither should you. Do today\u2019s small thing like it matters, because it does."],
 ["Here\u2019s a step most people skip: ask for help this week — real help, out loud, from a real person. Something in us would rather struggle privately than be seen needing. But every \u201cone another\u201d in the New Testament assumes you\u2019ll let someone close enough to obey it.",
  "If you\u2019re doing this journey with a group, don\u2019t waste the circle. Go one layer more honest than feels comfortable this week. Someone in that room is waiting for a person to go first. Be the one who goes first.",
  "And if the people around you are hard right now — if community itself is the wound — start smaller: one safe person, one honest conversation, this week. God\u2019s answer to loneliness has always had a face and a name."],
 ["Before this journey fades into the calendar, capture it. Write down the one truth you most need to keep, the one habit you\u2019re keeping, and the one person you\u2019ll keep walking with. Journeys end; what they built doesn\u2019t have to.",
  "Ask God for your assignment this week — not in the abstract, but with a name attached. Who is the person He\u2019s been putting in front of you? Your next step probably starts with a text, an invitation, or a table.",
  "Celebrate before you close. Seriously — mark it. God has been at work in you these weeks, and gratitude sets glue on growth. Then get some rest, because sent people need full tanks."]];

/* ---------- prayers / questions / steps by phase ---------- */
const PRAYERS=[
 ["Father, You know exactly where this finds me. I\u2019m done pretending. Meet me in these days — open Your Word, open my heart, and lead me one honest step at a time. In Jesus\u2019 name, amen.",
  "Lord, I bring You the sentence I\u2019ve been carrying. You are not surprised by it and not put off by it. Begin something new in me starting today. Amen."],
 ["God, plant this passage deeper than my circumstances. When the old script starts again, let Your words be the ones my heart says back. Make truth louder than fear. Amen.",
  "Father, thank You that Your Word is a promise with Your character behind it. I take my stand on it today — not on my feelings, not on my track record, on You. Amen."],
 ["Search me, God, and know my heart. Surface what needs surfacing, heal what needs healing, and replace the lies I\u2019ve believed with the truth of who You are. Amen.",
  "Lord, work below my waterline. I don\u2019t just want new behavior; I want a new heart. Do in me what only You can do. Amen."],
 ["God, save me from a faith of good intentions. Show me today\u2019s one small obedience and give me the courage to take it before tonight. Amen.",
  "Father, make me faithful in the little things today. I bring You my ordinary Tuesday and ask You to make it holy ground. Amen."],
 ["Lord, You said it is not good to be alone — and You meant me. Give me the courage to be known this week: to speak honestly, to ask for help, to let someone in. Amen.",
  "Father, thank You for the people You\u2019ve put around me. Knit us together in this journey, and make our honesty a place where Your healing happens. Amen."],
 ["God, don\u2019t let this end when the reading plan does. Seal what You\u2019ve built, show me who You\u2019re sending me to, and make my ordinary life the proof of these weeks. Amen.",
  "Father, I want to finish this journey sent, not just finished. Put a name on my heart and a next step in front of me. I\u2019m Yours. Amen."]];
const QS=[
 ["What made you pick up this journey — and what do you honestly hope is different at the end of it?",
  "When did you first notice this need in your life? What has it cost you to carry it alone?"],
 ["Which word or phrase in the anchor passage speaks most directly to your situation right now — and why that one?",
  "What would change about this week if you actually believed this passage was written with you in mind?"],
 ["What is the fear or belief underneath this struggle that you\u2019ve never said out loud?",
  "If God searched your heart on this topic today, what do you think He would gently put His finger on?"],
 ["What is the smallest concrete step you could take today in the direction this journey is pointing?",
  "Where does this truth most need to show up in your actual schedule this week?"],
 ["Who is one person you could invite into what God is doing in you — and what\u2019s kept you from asking?",
  "When has someone else\u2019s honesty made it easier for you to be honest? Who needs that gift from you now?"],
 ["What is the one truth from these weeks you most need to carry forward — and how will you keep it in front of you?",
  "Who around you is carrying the sentence you started this journey with? What would it look like to walk toward them?"]];
const STEPS=[
 ["Tell one person you\u2019re starting this journey, and invite them to do it with you.",
  "Write today\u2019s honest sentence at the top of a journal page — then write one sentence of hope beneath it."],
 ["Write the anchor verse on a card and put it where you\u2019ll see it every morning of this journey.",
  "Read the anchor passage out loud once today — slowly, like it\u2019s addressed to you. It is."],
 ["Tonight, write down the loudest sentence your inner critic said today. Next to it, write what this week\u2019s passage says instead.",
  "Take ten unhurried minutes today to pray Psalm 139:23-24 and simply listen."],
 ["Choose one action — small, specific, today — and complete it before you sleep. Then text your spiritual partner one sentence about it.",
  "Put tomorrow\u2019s obedience on your calendar right now, with a time attached."],
 ["Send the text: invite one person to coffee, a walk, or your table this week — and go one layer more honest than usual.",
  "In your group this week, share one real thing this journey has surfaced. Go first."],
 ["Write a short letter to yourself about what God did in these weeks. Date it. Read it in six months.",
  "Choose your one person — and take the first step toward them within 48 hours."]];

/* ---------- audience/event flavor lines ---------- */
function flavor(c,r){
  const aud=c[11], evt=c[12];
  const lines=[
   `And because this edition was written with ${aud.toLowerCase()} in mind, keep your own season in view as you read — God\u2019s truth doesn\u2019t change, but it lands with particular kindness right where you live.`,
   `A word for ${aud.toLowerCase()}: your season is not an obstacle to this journey; it\u2019s the address where God intends to meet you.`,
   `If this finds you near the season of ${String(evt).toLowerCase()}, read gently. God is not rushing you, and neither is this journey.`,
   `Whatever today held for you, remember: this journey was built for real life — interrupted days included. Grace covers the missed mornings; just come back tomorrow.`];
  return pick(r,lines);
}

/* ---------- format plans ---------- */
function plan(fmt){
  if(fmt==='7-Day')  return {days:7, weeks:[[0,1],[1,1],[2,1],[3,1],[3,1],[4,1],[5,1]], label:'7-Day Journey'};
  if(fmt==='21-Day') return {days:21, phase:d=>d<=3?0:d<=7?1:d<=11?2:d<=15?3:d<=18?4:5, label:'21-Day Journey'};
  if(fmt==='30-Day') return {days:30, phase:d=>d<=4?0:d<=10?1:d<=16?2:d<=22?3:d<=26?4:5, label:'30-Day Journey'};
  return {days:40, phase:d=>Math.min(5,Math.floor((d-1)/7)), label:'40-Day Campaign'};
}

/* ---------- public API ---------- */
const Engine={
 get:function(id){return (window.CAMPAIGNS||[]).find(r=>r[9]===id);},
 meta:function(c){const m=window.THEMEMETA[c[10]];return {cat:m[0],scr:m[1],need:m[2],W:m[3]};},
 weekTitle:function(i,W){return ARCS[i].t+" — "+W;},
 devotional:function(c,fmt){
  const m=this.meta(c), r=rng(seedFrom(c[9]+fmt));
  const P=plan(fmt), days=[];
  const bank=BANK[m.cat].slice(), ubank=UNIV.slice();
  for(let d=1;d<=P.days;d++){
    const ph = P.phase? P.phase(d) : P.weeks[d-1][0];
    const first = days.filter(x=>x.ph===ph).length===0;
    const scr = (d===1||d===P.days)? m.scr : (d%4===0? ubank[(seedFrom(c[9])+d)%ubank.length] : bank[(seedFrom(c[9])*7+d*3)%bank.length]);
    const tpick=(seedFrom(c[9])+d*5)%DTITLES[ph].length;
    let title = first && ph===0 && d===1 ? "Where This Journey Begins" : DTITLES[ph][tpick];
    const p1=P1[ph][(seedFrom(c[9]+'p1')+d)%P1[ph].length].split('{need}').join(m.need)
      .split('{scr}').join(m.scr).split('{W.toLowerCase}').join(m.W.toLowerCase());
    const p2=P2[ph][(seedFrom(c[9]+'p2')+d)%P2[ph].length];
    const fl = (d%5===0)? '<br><br>'+flavor(c,r) : '';
    days.push({ph, n:d, dn:'Day '+String(d).padStart(2,'0'),
      wk:ARCS[ph].t, title, scr:scr+' (NIV)',
      body:'<p>'+p1+'</p><p>'+p2+fl+'</p>',
      pray:PRAYERS[ph][(d+seedFrom(c[9]))%2], q:QS[ph][(d*3+seedFrom(c[9]))%2], step:STEPS[ph][(d*7+seedFrom(c[9]))%2]});
  }
  return {label:plan(fmt).label, days};
 },
 groupStudy:function(c){
  const m=this.meta(c), r=rng(seedFrom(c[9]+'grp'));
  const sessions=ARCS.map((a,i)=>{
    const refs=[ i===0? m.scr : BANK[m.cat][(seedFrom(c[9])+i*5)%BANK[m.cat].length],
                 BANK[m.cat][(seedFrom(c[9])+i*9+3)%BANK[m.cat].length],
                 UNIV[(seedFrom(c[9])+i*4)%UNIV.length] ];
    return {n:i+1, title:'Session '+(i+1)+': '+a.t, focus:'This session is about '+a.f+'.',
     opener: pick(r,["Go around the circle: what\u2019s one word for how your week actually went?",
       "Share a high and a low from the past week — thirty seconds each.",
       "What\u2019s one thing from this week\u2019s readings that stuck with you, bothered you, or wouldn\u2019t leave you alone?"]),
     refs:refs.map(x=>x+' (NIV)'),
     qs:[QS[i][0],QS[i][1],
       "Read the first passage together. What word or phrase stands out — and why?",
       "Where have you seen this truth show up (or go missing) in your week?",
       "What would obeying this look like in your actual schedule — name a day and a time.",
       "What\u2019s one fear or obstacle that makes this hard for you? Be specific.",
       "How can this group help you take your next step before we meet again?",
       "Who outside this circle needs what we talked about tonight?"],
     pray:PRAYERS[i][0],
     practice:STEPS[i][0],
     leader:"Leader note: your job is not to have the answers — it\u2019s to keep the circle honest and keep it moving. Draw out the quiet ones with \u201cWhat do you think, ___?\u201d, land the practice before you close, and end on time. Nobody does this alone — including you: text a co-leader after each session with one win and one question."};
  });
  return {label:'6-Week Group Series', sessions};
 },
 sermons:function(c){
  const m=this.meta(c);
  return ARCS.map((a,i)=>({n:i+1, title:'Week '+(i+1)+': '+a.t,
    text: i===0? m.scr+' (NIV)' : BANK[m.cat][(seedFrom(c[9])+i*5)%BANK[m.cat].length]+' (NIV)',
    big:'Big idea: '+a.f.charAt(0).toUpperCase()+a.f.slice(1)+'.',
    points:['1. The honest starting point — where the text meets the felt need: \u201c'+m.need+'\u201d',
            '2. The truth of the text — what God says, promises, and asks',
            '3. The next step — one specific obedience for this week, done together']}));
 },
 launchKit:function(c){
  const m=this.meta(c);
  return {announce:'\u201cChurch, for the next season we\u2019re doing something together. Every one of us — same journey, same Scriptures, same conversations. It\u2019s called '+c[0]+', and it starts on Launch Sunday. Grab a devotional, join a group, and let\u2019s see what God does when a whole church moves together.\u201d',
   emails:['T-3 weeks: announce the campaign & open group sign-ups','T-2 weeks: pastor\u2019s personal invitation + host training','T-1 week: final push — \u201ceveryone starts Day 1 together\u201d','Launch day: Day 1 link + group reminders','Midpoint: encouragement + a story from the congregation','Final week: Celebration Sunday invitation'],
   celebration:'End with Celebration Sunday: 2–3 stories from the journey, a moment of commitment around '+m.scr+', and a clear next step into ongoing groups.'};
 }
};
window.Engine=Engine;
})();
