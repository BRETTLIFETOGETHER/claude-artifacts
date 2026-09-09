/* engine.js — curated edition
   Composes complete campaign content on demand for every campaign in data.js.
   Deterministic per campaign ID (seeded PRNG): the same campaign always renders
   the same devotional, group study, sermons, youth/children editions, and kits.
   Hand-authored DEEP content (window.DEEP) overrides the engine wherever present.
   Scripture: daily reading references are NIV citations; weekly memory verses are
   quoted from the King James Version (public domain) pending the Biblica license. */
(function(){
'use strict';

/* ---------------- PRNG ---------------- */
function seedOf(str){ var h=1779033703^str.length; for(var i=0;i<str.length;i++){ h=Math.imul(h^str.charCodeAt(i),3432918353); h=h<<13|h>>>19; } return function(){ h=Math.imul(h^h>>>16,2246822507); h=Math.imul(h^h>>>13,3266489909); return (h^=h>>>16)>>>0; }; }
function rngFor(id,salt){ var s=seedOf(id+'::'+(salt||'')) ; var a=s(); return function(){ a|=0; a=a+0x6D2B79F5|0; var t=Math.imul(a^a>>>15,1|a); t=t+Math.imul(t^t>>>7,61|t)^t; return ((t^t>>>14)>>>0)/4294967296; }; }
function pk(r,arr){ return arr[Math.floor(r()*arr.length)]; }
function pkN(r,arr,n){ var c=arr.slice(),out=[]; while(out.length<n&&c.length){ out.push(c.splice(Math.floor(r()*c.length),1)[0]); } return out; }
function rot(arr,i){ return arr[i%arr.length]; }

/* ---------------- shared memory-verse bank (KJV, public domain) ---------------- */
var MV={
 own:{v:"Psalm 24:1",t:"The earth is the LORD's, and the fulness thereof; the world, and they that dwell therein."},
 trust:{v:"Proverbs 3:5-6",t:"Trust in the LORD with all thine heart; and lean not unto thine own understanding. In all thy ways acknowledge him, and he shall direct thy paths."},
 treasure:{v:"Matthew 6:21",t:"For where your treasure is, there will your heart be also."},
 first:{v:"Matthew 6:33",t:"But seek ye first the kingdom of God, and his righteousness; and all these things shall be added unto you."},
 content:{v:"Philippians 4:11",t:"Not that I speak in respect of want: for I have learned, in whatsoever state I am, therewith to be content."},
 legacy:{v:"Proverbs 13:22",t:"A good man leaveth an inheritance to his children's children: and the wealth of the sinner is laid up for the just."},
 faithful:{v:"Luke 16:10",t:"He that is faithful in that which is least is faithful also in much: and he that is unjust in the least is unjust also in much."},
 giver:{v:"2 Corinthians 9:7",t:"Every man according as he purposeth in his heart, so let him give; not grudgingly, or of necessity: for God loveth a cheerful giver."},
 work:{v:"Colossians 3:23",t:"And whatsoever ye do, do it heartily, as to the Lord, and not unto men."},
 shepherd:{v:"Psalm 23:1",t:"The LORD is my shepherd; I shall not want."},
 fear:{v:"Isaiah 41:10",t:"Fear thou not; for I am with thee: be not dismayed; for I am thy God: I will strengthen thee; yea, I will help thee; yea, I will uphold thee with the right hand of my righteousness."},
 rest:{v:"Matthew 11:28",t:"Come unto me, all ye that labour and are heavy laden, and I will give you rest."},
 peace:{v:"John 14:27",t:"Peace I leave with you, my peace I give unto you: not as the world giveth, give I unto you. Let not your heart be troubled, neither let it be afraid."},
 still:{v:"Psalm 46:10",t:"Be still, and know that I am God: I will be exalted among the heathen, I will be exalted in the earth."},
 house:{v:"Joshua 24:15",t:"And if it seem evil unto you to serve the LORD, choose you this day whom ye will serve; but as for me and my house, we will serve the LORD."},
 train:{v:"Proverbs 22:6",t:"Train up a child in the way he should go: and when he is old, he will not depart from it."},
 welldone:{v:"Matthew 25:21",t:"His lord said unto him, Well done, thou good and faithful servant: thou hast been faithful over a few things, I will make thee ruler over many things: enter thou into the joy of thy lord."},
 weary:{v:"Galatians 6:9",t:"And let us not be weary in well doing: for in due season we shall reap, if we faint not."},
 light:{v:"Matthew 5:16",t:"Let your light so shine before men, that they may see your good works, and glorify your Father which is in heaven."},
 wisdom:{v:"James 1:5",t:"If any of you lack wisdom, let him ask of God, that giveth to all men liberally, and upbraideth not; and it shall be given him."},
 confident:{v:"Philippians 1:6",t:"Being confident of this very thing, that he which hath begun a good work in you will perform it until the day of Jesus Christ."},
 good:{v:"Romans 8:28",t:"And we know that all things work together for good to them that love God, to them who are the called according to his purpose."},
 go:{v:"Matthew 28:19",t:"Go ye therefore, and teach all nations, baptizing them in the name of the Father, and of the Son, and of the Holy Ghost."},
 workmanship:{v:"Ephesians 2:10",t:"For we are his workmanship, created in Christ Jesus unto good works, which God hath before ordained that we should walk in them."},
 finished:{v:"2 Timothy 4:7",t:"I have fought a good fight, I have finished my course, I have kept the faith."},
 number:{v:"Psalm 90:12",t:"So teach us to number our days, that we may apply our hearts unto wisdom."},
 abide:{v:"John 15:5",t:"I am the vine, ye are the branches: He that abideth in me, and I in him, the same bringeth forth much fruit: for without me ye can do nothing."},
 tithe:{v:"Malachi 3:10",t:"Bring ye all the tithes into the storehouse, that there may be meat in mine house, and prove me now herewith, saith the LORD of hosts, if I will not open you the windows of heaven, and pour you out a blessing, that there shall not be room enough to receive it."},
 ofThee:{v:"1 Chronicles 29:14",t:"But who am I, and what is my people, that we should be able to offer so willingly after this sort? for all things come of thee, and of thine own have we given thee."},
 faith:{v:"Hebrews 11:1",t:"Now faith is the substance of things hoped for, the evidence of things not seen."},
 build:{v:"Psalm 127:1",t:"Except the LORD build the house, they labour in vain that build it: except the LORD keep the city, the watchman waketh but in vain."},
 plans:{v:"Jeremiah 29:11",t:"For I know the thoughts that I think toward you, saith the LORD, thoughts of peace, and not of evil, to give you an expected end."}
};

/* ---------------- family knowledge banks ---------------- */
var KB={
st:{ label:"Stewardship & Financial Wisdom",
 concepts:["ownership","stewardship","trust","provision","margin","faithfulness","wisdom","freedom","gratitude","surrender"],
 partArc:["The Ownership Question","The Stewardship Question","The Confidence Question","The Contentment Question","The Generosity Question","The Legacy Question"],
 mem:[MV.own,MV.trust,MV.faithful,MV.content,MV.giver,MV.legacy],
 read:["Psalm 24:1-2","Matthew 6:19-24","Luke 12:13-21","Matthew 25:14-30","Proverbs 3:5-10","1 Chronicles 29:10-14","Luke 16:1-13","Philippians 4:10-13","1 Timothy 6:6-10","2 Corinthians 9:6-11","Proverbs 13:11-22","Deuteronomy 8:11-18","Ecclesiastes 5:10-20","Psalm 50:9-12"],
 sessions:[["Ownership","When ownership changes hands, everything changes."],["Faithfulness","God measures stewardship by faithfulness, not by size."],["Trust","Peace comes from trusting the Provider, not the provision."],["Wisdom","Every financial decision is first a spiritual decision."],["Generosity","Open hands are the surest sign of a surrendered heart."],["Legacy","What you steward today becomes what you leave tomorrow."]],
 sens:false, money:true },
ct:{ label:"Contentment & Treasure",
 concepts:["contentment","enough","treasure","simplicity","rest","gratitude","perspective","joy","freedom","trust"],
 partArc:["Naming the Ache","Where Treasure Lives","Learning Enough","The Freedom of Less","Grateful Living","Treasure That Lasts"],
 mem:[MV.content,MV.treasure,MV.first,MV.rest,MV.trust,MV.still],
 read:["Philippians 4:10-13","Matthew 6:19-24","1 Timothy 6:6-10","Ecclesiastes 5:10-12","Psalm 23","Luke 12:22-34","Hebrews 13:5-6","Proverbs 30:7-9","Matthew 13:44-46","Psalm 73:25-28","2 Corinthians 4:16-18","Colossians 3:1-4"],
 sessions:[["The Ache for More","The pursuit of more never delivers what it promises."],["Where Treasure Lives","Your heart always follows your treasure."],["Learning Enough","Enough is learned, not earned."],["Simple Riches","Simplicity makes room for what matters most."],["Grateful Eyes","Gratitude turns what you have into enough."],["Eternal Treasure","Only treasure in heaven holds its value forever."]],
 sens:false, money:true },
gn:{ label:"Generosity & Giving",
 concepts:["generosity","joy","open hands","blessing","overflow","cheerfulness","sacrifice","trust","gratitude","impact"],
 partArc:["The Generous Heart of God","Why Giving Changes Us","First and Best","Giving Together","Generosity as a Lifestyle","A Legacy of Generosity"],
 mem:[MV.giver,MV.ofThee,MV.tithe,MV.treasure,MV.weary,MV.legacy],
 read:["2 Corinthians 9:6-15","2 Corinthians 8:1-9","Malachi 3:6-12","1 Chronicles 29:10-17","Luke 6:38","Acts 20:32-35","Proverbs 11:24-25","Matthew 6:1-4","Mark 12:41-44","1 Timothy 6:17-19","Luke 19:1-10","Philippians 4:14-19"],
 sessions:[["The Giver Behind Every Gift","You are never more like God than when you give."],["The Joy Exchange","Giving trades anxiety for joy."],["First and Best","Generosity begins where leftovers end."],["Generous Together","Giving multiplies when families and churches do it together."],["The Open-Handed Life","Generosity is a lifestyle before it is a transaction."],["Giving That Outlives You","A generous life leaves a generous legacy."]],
 sens:false, money:true },
km:{ label:"Kingdom Impact & Mission",
 concepts:["eternity","mission","purpose","multiplication","influence","sending","compassion","harvest","obedience","impact"],
 partArc:["Seeing What Lasts","Kingdom First","Sent People","Loving Your Neighbor","Multiplying Disciples","An Eternal Legacy"],
 mem:[MV.first,MV.go,MV.light,MV.workmanship,MV.weary,MV.welldone],
 read:["Matthew 6:19-21,33","Matthew 28:16-20","Acts 1:6-8","Matthew 5:13-16","2 Corinthians 5:16-21","John 4:34-38","Luke 10:1-9","Matthew 25:31-40","1 Peter 4:7-11","Colossians 4:2-6","Romans 10:13-15","Revelation 7:9-12"],
 sessions:[["Living for What Lasts","Only two things on earth are eternal — God's Word and people."],["Kingdom First","Seek first the Kingdom, and everything else finds its place."],["You Are Sent","Every follower of Jesus is a missionary somewhere."],["Compassion in Action","The gospel travels best along lines of love."],["Multiply","Disciples who make disciples change the world."],["Eternal Impact","Invest your one life where the returns never end."]],
 sens:false, money:false },
lg:{ label:"Family Legacy & Wealth Transfer",
 concepts:["legacy","inheritance","preparation","unity","values","wisdom","blessing","story","trust","purpose"],
 partArc:["More Than Money","What You're Really Passing Down","Preparing People, Not Just Papers","Conversations That Unite","Wisdom Before Wealth","A Legacy That Lasts"],
 mem:[MV.legacy,MV.train,MV.house,MV.number,MV.build,MV.confident],
 read:["Proverbs 13:22","Psalm 78:1-8","Deuteronomy 6:4-9","Proverbs 24:3-4","2 Timothy 1:3-7","1 Kings 2:1-4","Psalm 127","Proverbs 4:1-9","Genesis 48:8-16","Ecclesiastes 2:18-21","Psalm 145:4-7","Joshua 4:1-7"],
 sessions:[["More Than an Estate","Your true legacy is measured in lives, not ledgers."],["Values Before Valuables","What your family believes outlasts what your family owns."],["Prepare the Family First","Prepare your heirs for the wealth before you prepare the wealth for your heirs."],["The Conversations That Matter","Unspoken plans divide families; shared vision unites them."],["Wisdom Transfer","Wisdom is the inheritance that grows when it's given away."],["Built to Endure","A God-centered legacy blesses generations you will never meet."]],
 sens:false, money:true },
hr:{ label:"Heirs & the Next Generation",
 concepts:["character","responsibility","readiness","identity","calling","gratitude","work","faith","courage","stewardship"],
 partArc:["Who Before What","Character Before Capital","Learning Faithfulness","Rooted Identity","Ready for Responsibility","Launched with Purpose"],
 mem:[MV.train,MV.workmanship,MV.faithful,MV.trust,MV.confident,MV.first],
 read:["Proverbs 22:6","Luke 16:10-12","1 Timothy 4:12","Psalm 119:9-16","Ephesians 2:8-10","Proverbs 3:1-12","Daniel 1:8-20","2 Timothy 2:1-7","Ecclesiastes 12:1","Colossians 3:12-17","Matthew 25:14-23","Jeremiah 29:11-13"],
 sessions:[["Who Before What","Who your children become matters more than what they receive."],["Character Before Capital","Character is the container every inheritance is poured into."],["Faithful in Little","Small responsibilities are the training ground for great ones."],["Rooted, Not Entitled","Gratitude and identity in Christ are the antidotes to entitlement."],["Ready to Receive","Readiness is built through practice, not promised by age."],["Launched with Purpose","The goal is not a comfortable heir but a faithful steward."]],
 sens:false, money:false },
fm:{ label:"Family, Marriage & Home",
 concepts:["unity","love","communication","grace","purpose","blessing","forgiveness","joy","faith at home","togetherness"],
 partArc:["The Home God Builds","One Heart","Words That Build","Grace Around the Table","Faith at Home","A Household on Mission"],
 mem:[MV.house,MV.build,MV.train,MV.light,MV.trust,MV.good],
 read:["Joshua 24:14-15","Psalm 127","Deuteronomy 6:4-9","Ephesians 4:29-32","Colossians 3:12-21","1 Corinthians 13:4-8","Proverbs 24:3-4","Ephesians 5:21-33","Psalm 128","Philippians 2:1-8","1 Peter 4:8-10","Mark 10:6-9"],
 sessions:[["The Home God Builds","Unless the Lord builds the house, its builders labor in vain."],["One Heart, One Direction","Unity is a daily choice before it is a family trait."],["Words That Build","Homes rise or fall on the words spoken inside them."],["Grace at the Center","Grace received becomes grace given — starting at home."],["Faith Begins at Home","The most influential congregation you'll ever pastor eats at your table."],["A Family on Mission","God blesses families so families can bless the world."]],
 sens:false, money:false },
wk:{ label:"Business, Work & Succession",
 concepts:["calling","excellence","integrity","purpose","service","influence","succession","diligence","witness","stewardship"],
 partArc:["Work as Worship","Whose Business Is It?","Integrity in the Details","People Over Profit","Influence in the Marketplace","Finishing and Passing It On"],
 mem:[MV.work,MV.faithful,MV.first,MV.build,MV.light,MV.welldone],
 read:["Colossians 3:22-24","Genesis 2:15","Proverbs 16:1-3","Matthew 25:14-30","Proverbs 11:1-3","Luke 19:11-26","Ecclesiastes 2:24-26","1 Thessalonians 4:11-12","Daniel 6:1-5","Proverbs 22:29","Ephesians 6:5-9","Psalm 90:16-17"],
 sessions:[["Work as Worship","Monday matters to God as much as Sunday."],["God Owns the Business","Ownership belongs to God; leadership belongs to you."],["Integrity in the Details","Trust is built in the small decisions no one sees."],["People Over Profit","A business that serves people serves its true bottom line."],["Salt and Light at Work","Your workplace is your most natural mission field."],["Succession with Purpose","Finish well by preparing the ones who come next."]],
 sens:false, money:true },
ld:{ label:"Leadership, Wisdom & Calling",
 concepts:["wisdom","character","calling","vision","humility","courage","discernment","influence","servanthood","purpose"],
 partArc:["The Source of Wisdom","Character First","Hearing the Call","Leading Like Jesus","Decisions That Honor God","Influence That Lasts"],
 mem:[MV.wisdom,MV.trust,MV.workmanship,MV.light,MV.first,MV.confident],
 read:["James 1:2-8","Proverbs 9:10-12","Psalm 25:4-10","Mark 10:42-45","Proverbs 16:1-9","1 Kings 3:5-14","Philippians 2:1-11","Romans 12:1-8","Proverbs 4:20-27","Micah 6:8","Joshua 1:6-9","2 Chronicles 1:7-12"],
 sessions:[["Wisdom Starts Here","The fear of the Lord is where real wisdom begins."],["Character Before Competence","Who you are always outruns what you do."],["Discovering Your Calling","God's call is heard most clearly in surrender."],["The Servant Leader","In God's Kingdom, the way up is down."],["Decisions God Honors","Wise decisions begin with an open Bible and an open hand."],["A Leader's Legacy","Influence that lasts is influence given away."]],
 sens:false, money:false },
fa:{ label:"Faith & Spiritual Formation",
 concepts:["grace","abiding","prayer","community","obedience","growth","worship","discipleship","hope","love"],
 partArc:["Rooted in Grace","Abiding Daily","Praying with Confidence","Growing Together","Following Fully","Bearing Fruit"],
 mem:[MV.abide,MV.faith,MV.trust,MV.confident,MV.light,MV.first],
 read:["John 15:1-11","Ephesians 2:1-10","Psalm 1","Philippians 3:7-14","Matthew 6:5-15","Acts 2:42-47","Colossians 2:6-7","Romans 12:1-2","Hebrews 10:19-25","Galatians 5:22-26","2 Peter 1:3-8","Psalm 119:105-112"],
 sessions:[["Rooted in Grace","You grow from acceptance, not for acceptance."],["The Abiding Life","Fruitfulness flows from staying connected to Jesus."],["Learning to Pray","Prayer is less about the right words and more about the right direction."],["Better Together","Nobody grows to maturity alone."],["Following Fully","Discipleship is saying yes to Jesus one day at a time."],["A Life That Bears Fruit","The evidence of growth is love that others can see."]],
 sens:false, money:false },
ss:{ label:"Life Stages & Seasons",
 concepts:["seasons","purpose","transition","wisdom","hope","courage","perspective","fruitfulness","peace","calling"],
 partArc:["Naming the Season","God of Every Season","Letting Go Well","What This Season Is For","New Strength","Finishing Well"],
 mem:[MV.number,MV.plans,MV.good,MV.finished,MV.trust,MV.confident],
 read:["Ecclesiastes 3:1-11","Psalm 90:1-12","Isaiah 43:18-19","Philippians 3:12-14","Psalm 92:12-15","Jeremiah 29:11-13","2 Timothy 4:6-8","Psalm 71:17-18","Joshua 14:6-12","Isaiah 46:3-4","Lamentations 3:22-26","John 21:15-19"],
 sessions:[["A Time for Everything","Every season of life has a God-given purpose."],["The God Who Doesn't Change","Seasons turn; God's faithfulness doesn't."],["Letting Go Well","Releasing the last season is how you receive the next one."],["Purpose in This Chapter","Your current season is an assignment, not an accident."],["Strength for Today","God's mercies are new for exactly the day you're in."],["Finishing Well","The best chapters can still be ahead of you."]],
 sens:true, money:false },
hp:{ label:"Hope, Healing & Flourishing",
 concepts:["hope","peace","comfort","healing","rest","courage","presence","renewal","trust","joy"],
 partArc:["Bringing It to God","The God Who Is Near","Peace Beyond Circumstances","One Day at a Time","Renewed Strength","Anchored Hope"],
 mem:[MV.peace,MV.fear,MV.rest,MV.still,MV.shepherd,MV.plans],
 read:["Psalm 23","Philippians 4:4-9","Matthew 11:28-30","Psalm 34:15-18","Isaiah 41:8-13","John 14:25-27","Psalm 46:1-11","Lamentations 3:19-26","2 Corinthians 1:3-7","Romans 15:13","Isaiah 40:28-31","Revelation 21:1-5"],
 sessions:[["Honest Before God","Hope begins where honesty meets God's presence."],["The God Who Draws Near","The Lord is close to the brokenhearted."],["Peace That Passes Understanding","God's peace guards hearts that circumstances can't explain."],["Grace for Today","You don't need strength for the whole road — only for today."],["Wings Like Eagles","Those who hope in the Lord renew their strength."],["An Anchor for the Soul","Hope in Christ holds in every storm."]],
 sens:true, money:false }
};
var FAM_BY_CAT={1:'st',2:'ct',3:'gn',4:'km',5:'lg',6:'hr',7:'fm',8:'wk',9:'ld',10:'fa',11:'ss',12:'hp'};

/* ---------------- audience phrasing ---------------- */
function audPhrase(C){
  var a=(C[11]||'').toLowerCase();
  if(!a) return "your life";
  if(a.indexOf('church')>-1||a.indexOf('congregation')>-1) return "your church family";
  if(a.indexOf('couple')>-1) return "your marriage";
  if(a.indexOf('grandparent')>-1) return "your grandchildren's lives";
  if(a.indexOf('parent')>-1) return "your family";
  if(a.indexOf('student')>-1||a.indexOf('young')>-1) return "this season of your life";
  if(a.indexOf('client')>-1) return "the families you serve";
  if(a.indexOf('owner')>-1||a.indexOf('executive')>-1||a.indexOf('leader')>-1) return "your leadership";
  if(a.indexOf('heir')>-1) return "what you've been entrusted with";
  if(a.indexOf('famil')>-1) return "your family";
  return "your life";
}

/* ---------------- devotional ---------------- */
var DAY_TITLES=[
 "The {C} You Were Made For","When {C} Feels Far Away","What {C} Really Costs","{C} in the Small Things",
 "The Slow Work of {C}","{C} Begins Today","Where {C} Takes Root","The Other Side of {C}",
 "{C} Without Fear","Practicing {C}","A Heart Shaped by {C}","{C} for the Long Haul",
 "Choosing {C} Again","The Quiet Strength of {C}","{C} in Real Life","When God Grows {C}",
 "More Than {C}","{C} You Can Give Away","The Fruit of {C}","Learning {C} Together",
 "{C} Under Pressure","What {C} Makes Possible","Trading Worry for {C}","{C} One Step at a Time"
];
function cap(s){ return s.charAt(0).toUpperCase()+s.slice(1); }

var OPENS=[
 "Somewhere between the calendar and the to-do list, most of us lose sight of {c}. Not on purpose — it just slips beneath the noise of ordinary days. Today, {t} invites you to slow down long enough to find it again.",
 "There is a question underneath today's reading, and it's worth sitting with before you rush ahead: what would change in {ap} if {c} became more than a word you agree with?",
 "You can tell what a person really believes by watching a week of their life. Not the crisis moments — the ordinary ones. Today's journey through {t} presses gently on those ordinary moments, because that's where {c} is actually formed.",
 "Every journey has a day like this one — a day when the idea stops being an idea and starts asking something of you. Today, {c} moves from the page into {ap}.",
 "Think back over the last month. Where did {c} show up — and where was it missing? That's not a guilt question. It's a grace question, because God never points at a gap without offering to fill it.",
 "Some truths are learned in a moment; others are learned over a lifetime. {cC} is the second kind. Today is one more step in that lifelong learning — small, honest, and closer to God than yesterday.",
 "The world around you is loud about almost everything except what matters most. Today, let Scripture get the first word about {c} — before the culture, before the critics, before even your own inner voice.",
 "If you could see {ap} the way God sees it, today's theme would not feel like a demand. It would feel like an invitation. That's the spirit to carry into this reading about {c}."
];
var TRUTHS=[
 "Scripture doesn't treat {c} as an optional upgrade for especially spiritual people; it treats it as the natural shape of a life that trusts God.",
 "Notice how today's passage refuses to separate believing from doing — in the Bible, {c} is always something you practice, not just something you affirm.",
 "The writers of Scripture knew what we forget: {c} is less about willpower and more about worship. What you treasure trains your heart.",
 "God is not asking you to manufacture {c} out of thin air. He is asking you to receive it — the way soil receives seed — and then to guard what grows.",
 "Today's reading turns the usual logic upside down: the world says security produces peace, but Scripture says {c} produces a peace that circumstances cannot take away.",
 "There is a reason this passage has steadied believers for thousands of years. It tells the truth about God's character first, and only then asks something of ours.",
 "In God's economy, {c} is never wasted. Every small act of obedience compounds — quietly, invisibly, and then all at once.",
 "The invitation of this passage is not to try harder but to trust deeper. {cC} grows in the soil of confidence in who God is."
];
var APPLYS=[
 "So what does this look like on an ordinary Tuesday? It looks like bringing {c} into {ap} in one concrete way — small enough to actually do, real enough to matter.",
 "For {ap}, the application is wonderfully practical: choose one place today where {c} can move from intention to action. Don't wait for the perfect moment; faithfulness prefers the available one.",
 "You don't need to overhaul everything by tonight. You need one honest step. Ask God to show you where {c} belongs in {ap} today, and then take that step before the day ends.",
 "The gap between what we believe and how we live closes one decision at a time. Today's decision: let {c} shape a single conversation, a single choice, a single moment in {ap}.",
 "Here's the beautiful thing about {c}: it scales. It works in a small apartment and a large company, in a full house and a quiet one. Whatever today holds for {ap}, there is room for it.",
 "Growth rarely announces itself. It shows up as one slightly braver, slightly more generous, slightly more trusting choice. Look for that choice in {ap} today — it will be there."
];
var CLOSES=[
 "Be encouraged: God finishes what He starts. Today's small yes is part of a work He has been doing in you longer than you know — and He is not close to done.",
 "You will not master this in a day, and you were never meant to. Take the pressure off. Walk with God through it, and let tomorrow's reading meet you one step further down the road.",
 "Whatever today brought before you opened this page, this remains true: God is with you, God is for you, and God is at work. Carry that into the rest of your day.",
 "The journey continues tomorrow, but the grace doesn't wait until then. It goes with you — into the meeting, the kitchen, the commute, and every place {c} will be tested and grown.",
 "Don't measure today by how much you felt; measure it by the direction you're facing. Facing God, even imperfectly, is exactly what this journey is for.",
 "End today with gratitude for one thing — however small. Gratitude is how {c} puts down roots."
];
var PRAYERS=[
 "Father, thank You for meeting me in these words today. Grow {c} in me — not as a burden I carry, but as fruit You produce. Give me eyes to see the one step You're inviting me to take, and courage to take it. In Jesus' name, amen.",
 "Lord, You know the parts of my life where {c} comes hard. I bring them to You honestly. Do in me what I cannot do in myself, and let today be one more day of walking with You. Amen.",
 "God, thank You that You are patient with slow learners. Teach me {c} the way You always teach — with grace, with truth, and one day at a time. Amen.",
 "Father, make this more than words on a page. Let {c} take root in {ap}, and let my life quietly point the people around me to You. In Jesus' name, amen.",
 "Lord Jesus, You lived {c} perfectly, and You live in me now. Shape my desires, steady my heart, and lead my steps today. Amen.",
 "God of grace, I don't want to just admire {c} — I want to live it. Fill the gap between what I believe and how I live, starting today. Amen."
];
var QUESTIONS=[
 "Where in your life right now is God inviting you to take {c} more seriously — and what makes that hard?",
 "If someone watched your last seven days, where would they see {c} — and where would they see its absence?",
 "What is one fear or habit that competes with {c} in your heart? What would surrender look like there?",
 "Who in your life models {c} well? What is one thing you could learn from watching them?",
 "How does today's passage change the way you think about {c} — even slightly?",
 "What would it look like for {ap} to be marked by {c} a year from now? What starts today?",
 "When has God grown {c} in you through a season you didn't choose? What did you learn?",
 "What is the smallest real step toward {c} you could take before this day ends?"
];
var STEPS=[
 "Write today's memory verse somewhere you'll see it three times today — a mirror, a dashboard, a lock screen — and say it out loud each time.",
 "Tell one person — a spouse, a friend, a group member — what stood out to you today, and ask what stood out to them.",
 "Take five unhurried minutes of silence today. No phone, no agenda. Just sit with today's verse and let God have the last word.",
 "Identify one decision you'll face today and make it through the lens of today's reading — then note tonight how it went.",
 "Pray today's prayer again at midday. Set a reminder now so the day doesn't swallow the intention.",
 "Do one small, concrete act that expresses {c} today — quietly, without announcing it — and thank God for the chance.",
 "Before bed, write two sentences: where you saw God today, and where you needed Him. Keep them for the end of this journey.",
 "Share one sentence of encouragement with someone walking this campaign with you."
];
var MONEY_NOTE="A gentle word as we begin: this journey shares biblical and spiritual principles, not professional financial, legal, or tax advice — for decisions in those areas, walk with a qualified advisor as well as with God.";
var CARE_NOTE="And a gentle word before we begin: if this season feels heavy, you don't have to carry it alone. Share it with your pastor, a trusted friend, or a professional counselor — reaching out is an act of faith, not a failure of it.";

function fill(tpl,map){ return tpl.replace(/\{cC\}/g,cap(map.c)).replace(/\{C\}/g,cap(map.c)).replace(/\{c\}/g,map.c).replace(/\{t\}/g,map.t).replace(/\{ap\}/g,map.ap).replace(/\{th\}/g,map.th); }

function fmtDays(fmt){ return fmt==='7-Day'?7:fmt==='21-Day'?21:fmt==='40-Day'?40:30; }
function partsFor(C,fam,n){
  var deep=(window.DEEP||{})[C[9]];
  if(deep&&deep.parts&&n===40) return deep.parts.map(function(p){return p.title;});
  var arc=fam.partArc;
  if(n===7) return [arc[0]];
  if(n===21) return [arc[0],arc[2],arc[5]];
  if(n===40) return arc.slice(0,6);
  return [arc[0],arc[1],arc[3],arc[4],arc[5]]; // 30-day → 5 parts
}
function partSpans(n,k){ // n days into k parts
  var base=Math.floor(n/k), rem=n%k, out=[], d=1;
  for(var i=0;i<k;i++){ var len=base+(i<rem?1:0); out.push([d,d+len-1]); d+=len; }
  return out;
}

function devotional(C,fmtOverride){
  var fam=KB[FAM_BY_CAT[C[2]]];
  var fmt=fmtOverride||C[3]; if(fmt==='6-Week') fmt='30-Day';
  var n=fmtDays(fmt);
  var parts=partsFor(C,fam,n), spans=partSpans(n,parts.length);
  var ap=audPhrase(C), th=C[10], t=C[0];
  var deep=(window.DEEP||{})[C[9]];
  var days=[];
  for(var d=1; d<=n; d++){
    var pi=spans.findIndex(function(s){return d>=s[0]&&d<=s[1];});
    var week=Math.ceil(d/7);
    var r=rngFor(C[9],'day'+d);
    var c=rot(fam.concepts,(d-1)+Math.floor(r()*3));
    var map={c:c,t:t,ap:ap,th:th};
    var title=fill(rot(DAY_TITLES,(d*7+C[9].charCodeAt(3))%DAY_TITLES.length),{c:cap(c),t:t,ap:ap,th:th});
    var mem=rot(fam.mem,week-1);
    var scr=rot(fam.read,(d-1)%fam.read.length);
    var p1=fill(rot(OPENS,d%OPENS.length),map);
    var p2="Open today's reading — "+scr+" — and read it slowly, maybe twice. "+fill(rot(TRUTHS,(d*3)%TRUTHS.length),map)+" "+fill(rot(TRUTHS,(d*3+1)%TRUTHS.length),map);
    var p3=fill(rot(APPLYS,d%APPLYS.length),map)+(C[12]?" And because this journey was built with "+C[12].toLowerCase()+" in view, don't be surprised if today's step lands close to home — that's not coincidence; that's provision.":"");
    var p4=fill(rot(CLOSES,d%CLOSES.length),map);
    if(d===1){
      if(deep&&deep.day1){ title=deep.day1.title; p1=deep.day1.sub+". "+p1; }
      if(C[1]) p1="\u201C"+C[1]+".\u201D That's the promise over this whole journey — and it starts here. "+p1;
      if(fam.sens) p4+=" "+CARE_NOTE;
      if(fam.money) p4+=" "+MONEY_NOTE;
    }
    days.push({
      dn:"DAY "+d,
      wk:"Part "+(pi+1)+" · "+parts[pi],
      title:title,
      mem:mem,
      scr:scr+" (NIV)",
      body:"<p>"+p1+"</p><p>"+p2+"</p><p>"+p3+"</p><p>"+p4+"</p>",
      pray:fill(rot(PRAYERS,d%PRAYERS.length),map),
      q:fill(rot(QUESTIONS,d%QUESTIONS.length),map),
      step:fill(rot(STEPS,d%STEPS.length),map)
    });
  }
  return { label: fmt+" Devotional", fmt:fmt, days:days, parts:parts.map(function(p,i){return {n:i+1,title:p,days:"Days "+spans[i][0]+"–"+spans[i][1]};}) };
}

/* ---------------- group study ---------------- */
var WELCOMES=[
 "Welcome to Session {n}. Before anything else, take a breath — this hour is not a performance, it's a table. Everyone's honest answer is welcome here.",
 "Welcome back, everyone. Whether your week was steady or scattered, you're exactly where you're supposed to be for the next hour.",
 "Welcome to Session {n} of {t}. Tonight builds on everything so far, so let's start by checking in before we dive in."
];
var MOVE_EX=[
 "Read the passage aloud together, then let it breathe for a moment before discussing. Notice what it says about God before noticing what it asks of us.",
 "Have two people read the passage in turn. Ask the group: what word or phrase stands out — and why might God be underlining it for you this week?",
 "Read the passage, then retell it in your own words as a group. Plain language often uncovers what familiar language hides.",
 "Read the passage together. Then ask: where have you seen this truth proven — in Scripture, in history, or in someone at this table?"
];
var MOVE_APP=[
 "Application: name one specific place this truth touches your week — a decision, a relationship, a habit — and say it out loud to the group.",
 "Application: pair up for three minutes. Each person answers: what would obeying this look like for me before we meet again?",
 "Application: as a group, agree on one shared practice for the week that expresses this point, and plan to report back next session.",
 "Application: write one sentence — 'This week, this truth means I will ____' — and keep it visible until the group meets again."
];
var PRACTICES=[
 "This week's practice: revisit this session's key scripture every morning and let it set the day's direction.",
 "This week's practice: have one intentional conversation about this session's big idea with someone outside the group.",
 "This week's practice: take one concrete step your group named tonight, and jot down what happened so you can share it next week.",
 "This week's practice: pray this session's big idea back to God each day — one honest minute is enough.",
 "This week's practice: watch for one moment where this session's truth gets tested in real life, and respond on purpose rather than on autopilot.",
 "This week's practice: encourage one group member midweek — a text is enough — with something from tonight's discussion."
];
var GROUP_CLOSE="Close in prayer: thank God for what was shared tonight, pray for one specific need voiced around the circle, and ask Him to make this week's practice real. If your church is walking the daily devotional together, remind the group which days come next.";

function groupStudy(C){
  var fam=KB[FAM_BY_CAT[C[2]]];
  var deep=(window.DEEP||{})[C[9]];
  var ap=audPhrase(C), t=C[0];
  var sessions=[];
  for(var i=0;i<6;i++){
    var r=rngFor(C[9],'sess'+(i+1));
    var base=fam.sessions[i];
    var mem=rot(fam.mem,i), reads=pkN(r,fam.read,4);
    var c=rot(fam.concepts,i*2);
    var map={c:c,t:t,ap:ap,th:C[10]};
    var s={
      n:i+1,
      title:base[0],
      sub:null,
      big:base[1],
      key:mem.v,
      support:reads.slice(0,3),
      welcome:fill(rot(WELCOMES,i%WELCOMES.length).replace('{n}',i+1),map),
      openQ:i===0
        ? "As we begin "+t+(C[1]?" — "+C[1].toLowerCase():"")+" — what made you say yes to this journey, and what do you hope is different six weeks from now?"
        : fill(rot(QUESTIONS,(i*3)%QUESTIONS.length),map),
      movements:[],
      dqs:[],
      practice:rot(PRACTICES,i%PRACTICES.length),
      close:GROUP_CLOSE,
      challenge:null
    };
    var mvTitles=[
      ["What God Says First","Seeing "+cap(c)+" in Scripture","Where We Resist","Living It This Week"],
      ["The Heart of the Matter","The Truth Beneath the Surface","Counting the Cost","Taking the Step"],
      ["God's Character","Our Calling","The Common Obstacle","The Concrete Practice"]
    ][i%3];
    for(var m=0;m<4;m++){
      s.movements.push({
        t:mvTitles[m],
        scr:m===0?mem.v:reads[m-1]||rot(fam.read,i+m),
        ex:rot(MOVE_EX,(i+m)%MOVE_EX.length),
        dq:fill(rot(QUESTIONS,(i*4+m)%QUESTIONS.length),map),
        app:rot(MOVE_APP,(i+m)%MOVE_APP.length)
      });
    }
    s.dqs=pkN(r,QUESTIONS,6).map(function(q){return fill(q,map);});
    if(i===0){
      if(fam.money) s.welcome+=" "+MONEY_NOTE;
      if(fam.sens) s.welcome+=" "+CARE_NOTE;
    }
    /* DEEP overrides */
    if(deep&&deep.sessions&&deep.sessions[i]){
      var d=deep.sessions[i];
      if(d.title) s.title=d.title;
      if(d.sub) s.sub=d.sub;
      if(d.question){ s.sub=s.sub||d.question; s.openQ=d.question; }
      if(d.bigIdea) s.big=d.bigIdea;
      if(d.big) s.big=d.big||s.big;
      if(d.verse) s.key=d.verse;
      if(d.challenge){ s.challenge=d.challenge; s.practice="This week's challenge — "+d.challenge+": put this session's big idea into practice through the "+d.challenge+" exercise, and come ready to share how it went."; }
      if(d.exercise){ s.challenge=d.exercise; s.practice="This week's family exercise — "+d.exercise+": work through it together before the next session, and bring one insight back to the group."; }
    }
    sessions.push(s);
  }
  return { title:C[0], sessions:sessions };
}

/* ---------------- sermons ---------------- */
function sermons(C){
  var fam=KB[FAM_BY_CAT[C[2]]];
  var gs=groupStudy(C);
  return gs.sessions.map(function(s,i){
    var r=rngFor(C[9],'serm'+(i+1));
    var reads=pkN(r,fam.read,3);
    return {
      n:i+1,
      title:s.title,
      text:s.key,
      big:s.big,
      opener:"Open with a story or moment your people will recognize — the everyday place where this week's tension shows up — then name it plainly: this is where "+s.title.toLowerCase()+" meets real life.",
      points:[
        {t:"What God declares",scr:s.key,note:"Ground the message in the text before the takeaways. Let the congregation hear what God says about "+C[10].toLowerCase()+" before hearing what we should do."},
        {t:"Why we struggle",scr:reads[0],note:"Name the honest obstacle — the fear, the habit, the cultural script — without shame. People lean in when the preacher tells the truth about the struggle."},
        {t:"The way forward",scr:reads[1],note:"Show the gospel path: what Christ has done, and the concrete response this week. Tie it to the group study and this week's daily readings so Sunday doesn't end on Sunday."}
      ],
      close:"Land the plane on the big idea — \u201C"+s.big+"\u201D — and give one clear next step: join a group, take this week's challenge, and keep the daily readings going all week."
    };
  });
}

/* ---------------- youth & children ---------------- */
function youth(C){
  var gs=groupStudy(C);
  var ap="your world — school, friends, family, and the version of you nobody sees";
  return gs.sessions.map(function(s,i){
    var r=rngFor(C[9],'youth'+(i+1));
    return {
      n:i+1,
      title:s.title,
      hook:"Start with the real question behind this session: where does \u201C"+s.big.toLowerCase().replace(/\.$/,'')+"\u201D actually show up in "+ap+"?",
      truth:s.big,
      scr:s.key,
      dqs:[
        "Be honest — is this easy or hard for you right now? Why?",
        "What would change at school or online if you actually lived this out this week?",
        "Who's one person who models this well? What do they do differently?"
      ],
      challenge:"This week: pick one moment — one conversation, one post, one decision — and let this session's truth call the shot. Come back ready to tell the group what happened."
    };
  });
}
function children(C){
  var gs=groupStudy(C);
  return gs.sessions.map(function(s,i){
    return {
      n:i+1,
      title:s.title,
      bigTruth:s.big,
      verse:s.key,
      story:"Tell the Bible story behind "+s.key+" in your own words — keep it short, act it out where you can, and land on one sentence: \u201C"+s.big+"\u201D",
      activity:"Activity: have the kids draw or build one picture of this week's big truth, then let volunteers show and tell. End by saying the memory verse together twice — once loud, once in a whisper.",
      question:"Ask: \u201CWhere can you live this out at home or at school this week?\u201D Take every answer seriously.",
      prayer:"Close with a simple echo prayer — you say a line, they repeat it — thanking God for this week's truth and asking for help to live it."
    };
  });
}

/* ---------------- leader & launch kits ---------------- */
function leaderKit(C){
  var fam=KB[FAM_BY_CAT[C[2]]];
  var kit={
    hostTips:[
      "You don't need to be a teacher — you need to be a host. Your job is questions, not answers; the content carries the teaching.",
      "Start and end on time, every week. Trust is built by respecting the clock.",
      "Silence after a question isn't failure — count to ten in your head before rescuing it. The best answers come after the pause.",
      "Follow up midweek with one text to the group. Groups that hear from their leader between sessions finish the journey.",
      "Share the load early: ask someone to bring snacks, someone to read, someone to pray. Shared ownership is the seed of the next group."
    ],
    rhythm:[
      "Gather & check in (10 min) — how did last week's practice go?",
      "Open the session — welcome and opening question (10 min)",
      "Four movements — read, discuss, apply (35–40 min)",
      "Decide the week's practice together (5 min)",
      "Pray for one another (10 min)"
    ],
    care:[
      "Pray for each member by name once a week — it will change how you lead.",
      "If someone shares something heavy, thank them, don't fix them, and follow up privately within 48 hours.",
      "Notice absences early. A 'we missed you' message in week two prevents a disappearance in week four."
    ],
    checklist:[
      "Read the session and the week's devotional days before the group meets",
      "Confirm host home, time, and childcare plan",
      "Have extra devotionals on hand for newcomers",
      "Assign next week's snack and Scripture readers before everyone leaves"
    ]
  };
  if(fam.sens) kit.care.unshift("This campaign touches tender ground. Open Session 1 by naming that gently, keep the pace unhurried, and have your church's care pathway ready — pastor, counselor, or support ministry — for anyone who needs more than a group can give.");
  if(fam.money) kit.care.push("Money topics can surface stress and shame. Remind the group that this journey teaches biblical principles, not professional financial advice, and that no one's numbers are up for discussion unless they offer them.");
  return kit;
}
function launchKit(C){
  return {
    runway:[
      {wk:"6 weeks out",items:["Set the launch Sunday and Celebration Sunday dates","Pastor announces the campaign vision from the platform","Recruit group hosts — one host per 8–10 adults expected"]},
      {wk:"4 weeks out",items:["Host orientation (use the Leader Kit)","Open group sign-ups after each service and online","Order or print devotionals for the whole congregation"]},
      {wk:"2 weeks out",items:["Preview the series in services — read Day 1 aloud","Youth and children's directors align their editions to the same weeks","Send the all-church launch email with group placements"]},
      {wk:"Launch week",items:["Kickoff Sunday: sermon 1 + devotionals in every hand","Groups meet for Session 1 within 72 hours of Sunday","Pastor's midweek video or email keeps momentum going"]}
    ],
    sunday:["Preach the six messages in step with the six sessions","Testimony moment each week from a group member","On-ramp every Sunday: it's never too late to join a group"],
    celebration:["Celebration Sunday: stories, baptisms if fitting, and next-step commitments","Capture testimonies in writing and video for the next launch","Announce the next campaign date before people leave the room"]
  };
}

/* ---------------- meta & API ---------------- */
function get(id){ return (window.CAMPAIGNS||[]).find(function(r){return r[9]===id;}); }
function meta(C){
  var fam=KB[FAM_BY_CAT[C[2]]];
  var dv=devotional(C);
  return { scr: C[13]||fam.mem[0].v, family:fam.label, parts:dv.parts, fmt:dv.fmt };
}

window.Engine={ get:get, meta:meta, devotional:devotional, groupStudy:groupStudy, sermons:sermons, youth:youth, children:children, leaderKit:leaderKit, launchKit:launchKit, KB:KB, FAM_BY_CAT:FAM_BY_CAT };
})();
