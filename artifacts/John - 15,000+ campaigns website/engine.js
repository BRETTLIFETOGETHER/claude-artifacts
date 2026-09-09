/* Lifetogether content engine — deterministic, seeded per campaign+day.
   Generates complete devotional days, sermon builds, and group sessions for any
   catalog row or free topic. Same seed → same text, so pages are stable & shareable. */
(function(){
"use strict";
const A=()=>window.App, D=()=>window.App.D;
function mul(a){return function(){a|=0;a=a+0x6D2B79F5|0;var t=Math.imul(a^a>>>15,1|a);t=t+Math.imul(t^t>>>7,61|t)^t;return((t^t>>>14)>>>0)/4294967296}}
function stream(seed){const r=mul(seed);const last={};return{
 pick(key,arr){let i=Math.floor(r()*arr.length);if(arr.length>1&&i===last[key])i=(i+1)%arr.length;last[key]=i;return arr[i]},
 int(n){return Math.floor(r()*n)}, r}}
function esc(s){return String(s??"").replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;")}
function fill(t,slots){return t.replace(/\{(\w+)\}/g,(_,k)=>slots[k]??"")}
function lc(s){return s? s[0].toLowerCase()+s.slice(1):s}

/* ---------------- per-channel banks: noun / img / tension / promise / practice ---------------- */
const B=[
/*0 Purpose*/{n:["your calling","the assignment in front of you","the life you were made for","your next obedient step","the work God prepared","your one short life"],
 i:["a lamp on a dark path","seed going into soil","a runner settling into stride","a compass finding north","hands finally opened","a door you almost walked past"],
 t:["you're busy but not sure it matters","everyone else seems to have found their lane","you keep waiting to feel ready","the dream and the mortgage argue daily","you've confused activity with purpose"],
 p:["God prepared good works for you before you found them","your purpose is assigned, not achieved","He who called you is faithful to finish","obedience today is enough for today","the Author of your story has not lost the plot"],
 pr:["write one sentence: what you sense God asking this season","tell one person the step you've been avoiding","say yes to the small task you've deemed beneath you","cancel one thing that exists only to impress","pray Isaiah's prayer — 'Here am I. Send me' — before checking your phone","do the next right thing without announcing it"]},
/*1 Identity*/{n:["who you already are","your true name","the person under the performance","your belovedness","the identity Christ purchased"],
 i:["a mirror wiped clean","a name written in stone","a child asleep in strong arms","clothes that finally fit","a title deed with your name on it"],
 t:["you perform for a verdict already rendered","other people's opinions run your inner weather","one old failure still introduces you","you're exhausted from auditioning"],
 p:["you are chosen before you are useful","nothing can separate you from His love","the verdict came in at the cross: beloved","God's opinion of you is not under review"],
 pr:["read the verse aloud with your own name in it","refuse one act of image-management today","write the old label, then write the new one over it","let a compliment land without deflecting it","thank God for one thing about how He made you"]},
/*2 Community*/{n:["real belonging","the people God gave you","life around the table","being fully known","the family of God"],
 i:["chairs pulled close around a table","a rope of three strands","stones fit into one wall","a porch light left on","a meal that runs long"],
 t:["you're surrounded and still lonely","being known feels riskier than being liked","your schedule keeps community theoretical","you left the last group hurt"],
 p:["it is not good to be alone — and you don't have to be","two are better than one, and He designed it that way","the church is a body, and you are a part it needs","grace grows best in company"],
 pr:["text one person: 'praying for you — what's one thing?'","invite someone to your actual table this week","answer 'how are you' honestly once today","show up early and stay ten minutes late","confess one small real thing to a safe person"]},
/*3 Prayer*/{n:["unhurried prayer","the practice of His presence","a listening life","honest conversation with God","holy rhythm"],
 i:["a door closed on the noise","incense rising","a well you keep returning to","dawn before the house wakes","an open Bible and an empty chair"],
 t:["your prayers feel like leaving voicemails","hurry has eaten your quiet","you talk to God only in emergencies","silence makes you reach for the phone"],
 p:["your Father hears in secret and rewards openly","the Spirit prays when you have no words","He is near to all who call on Him","prayer is not performance; it is presence"],
 pr:["set a ten-minute timer and just listen","pray the verse back to God in your own words","take one worry and hand it over out loud","fast one meal and let hunger be a bell for prayer","keep a one-line prayer journal tonight"]},
/*4 Money*/{n:["contentment","open-handed trust","enough","peace with what you have","faithful stewardship"],
 i:["an open hand instead of a fist","a table with room to spare","a ledger surrendered","seed kept back versus seed sown","a lighter backpack"],
 t:["there's more month than money","comparison keeps moving your finish line","one number owns your mood","you'd give more if you feared less"],
 p:["your Father knows what you need before you ask","godliness with contentment is great gain","He owns it all — you were never the owner, only the manager","seek first the kingdom and the rest gets added"],
 pr:["write every expense down for one day, without judgment","give one small unplanned gift today","name out loud what 'enough' would actually be","thank God for three provisions before any request","delay one purchase 48 hours and pray about it"]},
/*5 Generosity*/{n:["a generous life","cheerful giving","open hands","kingdom investment","the joy of release"],
 i:["a farmer scattering seed at dawn","rivers that flow versus ponds that stagnate","two small coins that outweighed the treasury","a table set for extra guests"],
 t:["you intend to give more someday","scarcity whispers louder than Scripture","generosity feels like loss, not worship","you give leftovers, not firstfruits"],
 p:["God loves a cheerful giver and funds one too","whoever sows generously reaps generously","it is more blessed to give than to receive","you can't out-give the One who gave His Son"],
 pr:["give something today that costs you comfort","move giving to the first line of the budget, on paper","bless one person anonymously","ask God to show you one need within reach","tell your money where it's going before the month does"]},
/*6 Family Legacy*/{n:["the story you're handing down","a legacy that outlives you","your family's spiritual inheritance","faith at your table","the next generation"],
 i:["an oak planted for grandchildren","a baton passed at full stride","a table that seats four generations","stones stacked by a river as a memorial","a letter sealed for someday"],
 t:["the calendar is passing faster than the values are","wealth may outrun wisdom","you never heard the family's faith stories told","succession is a topic everyone postpones"],
 p:["His faithfulness continues through all generations","a good person leaves an inheritance to children's children","the promise is for you and for your children","God keeps covenant to a thousand generations"],
 pr:["tell one family story of God's faithfulness at dinner","write a one-page blessing to a child or grandchild","name your family's three values out loud together","schedule the conversation you've been postponing","pray a Scripture over each family member by name"]},
/*7 Marriage*/{n:["your covenant","the marriage you're building","oneness","tending the vows","your first small group of two"],
 i:["two rowers finding one rhythm","a house on rock while rain falls","a garden weeded weekly","cords braided strong","a fire tended nightly"],
 t:["you're managing logistics, not sharing life","the same argument keeps changing costumes","tenderness lost to tiredness","you keep score without meaning to"],
 p:["love keeps no record of wrongs — and can be learned","what God joined, God sustains","grace received becomes grace given","two really are better than one"],
 pr:["ask 'what's one way I can love you well this week?' and just listen","bless your spouse out loud before critique","put one screen down for one full evening","forgive the small thing before sundown","pray for your spouse by name, daily, this week"]},
/*8 Parenting*/{n:["the children in your care","faith at home","your family's rhythm","the long work of formation","your kids' hearts"],
 i:["arrows shaped and sent","a trellis for a young vine","little eyes watching your hands","bread rising slowly","training wheels coming off"],
 t:["the days are long and the years are gone by Friday","you correct behavior and miss the heart","screens parent when you're tired","you fear you're getting it wrong"],
 p:["He gently leads those with young","grace covers imperfect parents raising imperfect kids","train a child in the way, and the way holds","your Father parents you as you parent them"],
 pr:["ask each child one real question at dinner and wait","bless your child aloud at bedtime tonight","apologize to your kid for one specific thing","put the phone in another room from 6 to 8","read the verse together and let them ask anything"]},
/*9 Emotional*/{n:["peace","an unhurried heart","honest lament","rest for your soul","hope with roots"],
 i:["an anchor beneath the waves","morning after a long night","a weighted blanket of grace","tears kept in a bottle","breath slowing in safe arms"],
 t:["your mind writes disaster drafts at 2 a.m.","you're tired in a place sleep can't reach","you smile in public and sigh in the car","grief keeps its own calendar"],
 p:["the peace of God stands guard over hearts and minds","He is close to the brokenhearted","weeping may stay the night, but joy comes","cast the anxiety — He is holding you"],
 pr:["breathe the verse slowly four times: in on the promise, out on the fear","write the worry down, then write 'God, this is Yours'","take a ten-minute walk without input in your ears","tell one safe person how you actually are","end tonight naming three mercies from today"]},
/*10 Health*/{n:["your body","wholeness","strength for today","the long road of healing","care that honors dignity"],
 i:["a temple lovingly kept","clay held by careful hands","a lamp refilled with oil","stitches doing quiet work","a shepherd slowing for the flock"],
 t:["the diagnosis rearranged the future","caregiving is holy and exhausting","your body feels like an opponent","waiting rooms have become a lifestyle"],
 p:["His power is made perfect in weakness","He heals the brokenhearted and binds up wounds","though the outer self wastes, the inner self renews","your body matters to the God who made it"],
 pr:["thank God for one thing your body did today","drink water, walk ten minutes, sleep on time — as worship","ask for help with one task you've been carrying alone","pray for your caregiver or the one you care for, by name","memorize the verse for the waiting room"]},
/*11 Freedom*/{n:["freedom","the new life","walking in the light","breaking the cycle","a clean start"],
 i:["chains on the floor of an open cell","a path out of the old neighborhood","dawn ending a long night","an old coat finally taken off","a river you cross once"],
 t:["the habit promises relief and delivers shame","you've quit a dozen times alone","secrecy is the soil it grows in","you fear you're the exception grace missed"],
 p:["whom the Son sets free is free indeed","confession breaks what secrecy feeds","no temptation lacks a way out","there is now no condemnation"],
 pr:["tell one trusted person the true thing today","remove one trigger from arm's reach tonight","replace the habit's time slot with a named practice","celebrate one day of freedom without minimizing it","write the lie, then the verse that answers it"]},
/*12 Seasons*/{n:["this season","the transition you're in","a new chapter","the waiting","what comes next"],
 i:["leaves turning on schedule","a doorway between rooms","tide going out before it returns","a field lying fallow on purpose","luggage packed by the door"],
 t:["the old normal is gone and the new one hasn't introduced itself","waiting feels like wasting","everyone asks what's next and you don't know","you grieve what was while others celebrate"],
 p:["there is a time for everything under heaven","He makes all things beautiful in their time","the One who began will complete","His presence goes with you into the next room"],
 pr:["name this season honestly in one sentence to God","keep one anchor habit steady while everything moves","ask someone two seasons ahead one real question","write a short goodbye to what's ending","take one small step that belongs to the next chapter"]},
/*13 Work*/{n:["your work","the desk as an altar","integrity under pressure","calling in the marketplace","Monday faith"],
 i:["salt dissolving into the whole dish","a lamp on a stand in an open office","scales that balance true","a craftsman's unhurried bench","light under a door"],
 t:["Sunday and Monday feel like different countries","the metrics never say 'enough'","cutting the corner would be so easy","your title has become your identity"],
 p:["work heartily — you serve the Lord, not the ladder","He establishes the work of your hands","integrity walks securely","faithfulness in little is the résumé heaven reads"],
 pr:["do today's hardest task first, as unto the Lord","encourage one colleague specifically and honestly","keep one promise that has gotten inconvenient","take a real lunch break and thank God in it","pray for the person at work who costs you the most"]},
/*14 Leadership*/{n:["servant leadership","the people you lead","influence held loosely","the towel and the basin","raising up others"],
 i:["a basin, a towel, and dusty feet","a shepherd who knows names","a ladder held steady for someone else","a candle lighting candles"],
 t:["the pedestal is lonelier than it looks","you're leading on an empty tank","developing people is slower than doing it yourself","criticism lands harder than it should"],
 p:["the greatest among you serves","He equips the called","your labor in the Lord is not in vain","authority under God is safe to steward"],
 pr:["do one hidden act of service no one can credit","hand a real responsibility to someone rising","ask your team 'what's one thing I should change?' and don't defend","rest one evening as an act of trust","pray for each person you lead, by name, this week"]},
/*15 Church Vision*/{n:["our shared vision","the church's next chapter","alignment","one direction together","the mission of this house"],
 i:["many oars, one drumbeat","a wall rebuilt gate by gate","a city on a hill at dusk","blueprints unrolled on a table"],
 t:["good ministries pull in five directions","vision on the wall isn't vision in the halls","momentum stalled and nobody said it out loud","we count what's easy, not what matters"],
 p:["unless the Lord builds, the builders labor in vain","He gives the growth","one body, many parts, one Head","the gates of hell still lose"],
 pr:["pray for your church's leaders by name today","say the mission in your own words to one person","volunteer for the unglamorous gap","invite one person who's drifted back for Sunday","write one line: what our church could be in five years"]},
/*16 Ministries*/{n:["the mission you steward","people at the margins","faithful ministry","partners in the work","the cause God gave you"],
 i:["five loaves in willing hands","a bridge built plank by plank","a lighthouse in bad weather","seed money becoming a field"],
 t:["needs outrun resources every quarter","donor letters are easier than donor prayers","the founder's fire needs a fireplace","success metrics and kingdom metrics diverge"],
 p:["God supplies seed to the sower","He is not unjust to forget your work","the King says 'you did it to Me'","He completes what He starts"],
 pr:["thank one partner today with no ask attached","pray for the people you serve before the plan to serve them","share one story of change with your team","do the small faithful task before the visible one","invite one intercessor deeper into the mission"]},
/*17 Mission*/{n:["your neighbor","the people God is sending you to","everyday witness","the harvest around you","love with an address"],
 i:["a porch conversation that goes long","salt and light in an ordinary kitchen","a net let down one more time","sandals by an open door"],
 t:["you love the nations and skip the neighbor","the gospel feels awkward in your own mouth","you're waiting to be 'ready' to share","compassion stays a feeling, not a schedule"],
 p:["you will receive power to be witnesses","beautiful are the feet that bring good news","the harvest is plentiful still","He stands ready to speak through you"],
 pr:["learn one neighbor's name and one real thing about them","pray for three people by name who are far from God","meet one practical need quietly this week","tell one small piece of your story when the door opens","invite one person to a meal before an event"]},
/*18 Calendar*/{n:["this holy season","the rhythm of the year","sacred time","the feast ahead","a set-apart week"],
 i:["candles lit one week at a time","palms laid on a dusty road","an empty tomb at first light","a table set for remembrance","a year hinged on grace"],
 t:["the season arrives and finds you unprepared","busyness eats the holy days first","tradition without wonder goes hollow","January's resolve is gone by February"],
 p:["the Word became flesh and moved in","He is risen, just as He said","His mercies restart with the morning","every season points to the same Savior"],
 pr:["light a candle tonight and read the passage aloud","fast one comfort this week and feast on Scripture","write who you'll invite before the big Sunday","keep one hour genuinely still this week","mark the day with gratitude before entertainment"]},
/*19 LoC*/{n:["the words of Jesus","the way of the Rabbi","red-letter obedience","life with Christ","the Kingdom He announced"],
 i:["dust of the Rabbi on your sandals","nets dropped on the shore","a narrow gate and a good road","bread broken at His table","a lamp He lights in you"],
 t:["you admire Jesus more than you follow Him","His hardest sentences get skimmed","familiarity has dulled the edges","you'd rather discuss the words than do them"],
 p:["His yoke fits and His burden is light","the one who hears and does builds on rock","abide in Him and fruit follows","He is with you to the end of the age"],
 pr:["read the words of Jesus for today twice, slowly","do the verse before you discuss the verse","ask 'Lord, what are You saying to me?' and sit one minute","obey one red-letter command literally today","memorize the line you most want to soften"]},
/*20 Bible*/{n:["the Word","Scripture-shaped life","the story of God","truth that reads you","a Book that breathes"],
 i:["a sword that operates gently","honey on the tongue","a lamp for the next step only","roots by the stream","bread for today"],
 t:["your Bible is open on the app and closed in the heart","you read for information, not transformation","hard passages get quietly skipped","you know verses and miss the Voice"],
 p:["all Scripture is God-breathed and useful","His word does not return empty","blessed are those who hear and keep it","the Word is living and active — still"],
 pr:["read today's chapter aloud, unhurried","write the one verse that snagged you and carry it","ask one honest question of the text and sit with it","obey the plainest command you read today","share one verse with one person, no commentary"]},
/*21 Doubt*/{n:["honest faith","your real questions","faith with room to breathe","belief and unbelief together","seeking that God honors"],
 i:["scars offered to trembling hands","a night of wrestling that ends in blessing","clouds that don't cancel the sun","a candle carried through fog"],
 t:["church answers feel smaller than your questions","you're afraid honesty will cost you God","deconstruction has no exit ramp in sight","doubt feels like betrayal"],
 p:["'I believe; help my unbelief' is a prayer He answers","He is gentle with bruised reeds","those who seek, find","Thomas got scars, not a scolding"],
 pr:["write your realest question and pray it verbatim","tell one safe believer where you actually are","keep one practice steady while the questions work","read one Gospel chapter as a skeptic and a seeker","thank God for one thing you still can't explain"]},
/*22 Digital*/{n:["attention","an undistracted heart","digital wisdom","presence over pixels","a discerning mind"],
 i:["a phone face-down at a full table","a fast from the feed","a garden fence around your mind","an unhurried walk with pockets empty"],
 t:["the scroll eats the margins of your day","outrage is engineered and you keep clicking","you check the phone before you check in with God","AI answers fast; wisdom comes slow"],
 p:["be transformed by renewed thinking, not conformed by the feed","whatever is true and lovely — think on these","He gives wisdom generously to askers","you can test everything and hold the good"],
 pr:["move the loudest app off your first screen tonight","take a two-hour sabbath from all screens","before sharing, ask: true, kind, necessary?","let the phone charge outside the bedroom","pray before you post, once, today"]},
];
/* pattern grammars */
const OPEN=["It is an ordinary {daypart}, and {tension}. You are not the only one — and this is exactly where today's word, {word}, wants to meet you.",
 "Somewhere between the calendar and the quiet, {tension}. Scripture does not scold that; it starts there.",
 "Picture {img}. Hold that picture, because {tension} — and God has something better than advice for it.",
 "Be honest for a moment: {tension}. Today is not about trying harder. It is about {word2}.",
 "Most of us don't need a lecture on {word2}; we need a way in. Start with this: {tension}.",
 "{Word} sounds simple until you need it on a Tuesday. And you do — because {tension}."]
const TRUTH=["Read {ref} again, slowly. {Promise}. That is not a slogan; it is the ground under your feet for the next twenty-four hours.",
 "In {ref}, the point is almost embarrassingly direct: {promise}. The question is never whether it is true, but whether you will let it be true of you today.",
 "{Ref} was written to real people with real {noun2} — and it says {promise}. Let the second reading move it from your notes to your nerves.",
 "Here is what {ref} refuses to let us forget: {promise}. Faith is agreeing with that sentence out loud before your feelings vote.",
 "{Promise} — that is the claim of {ref}. It reads like {img}, and it is meant to be leaned on, not framed."]
const TURN=["So what does {word2} look like before dinner? Smaller than you fear and sooner than you planned. Not a new life by Friday — one honest move today.",
 "The gap between knowing and living closes one small obedience at a time. {Word} is not a mood to wait for; it is a step to take.",
 "Don't spiritualize this into someday. {Word2} has a today-sized version, and taking it will teach you more than another week of thinking about it.",
 "Formation is rarely dramatic. It looks like {img} — slow, repeated, real. Today, choose the small version on purpose."]
const STEPL=["Today's step: {practice}.","Before the day ends: {practice}. Small, concrete, done.","Your one move today — {practice}. Then tell your partner or group you did it.","Practice: {practice}. Not perfectly; just actually."]
const QL=["Where has {tension2} been most true for you this week — and what would {word2} change about that one place?",
 "What is the today-sized version of {word2} you have been postponing, and why that one?",
 "If {ref} were fully true of you, what is the first thing someone close to you would notice?",
 "What makes {word2} feel risky right now — and what does today's passage say back to that?"]
const PRAYL=["Father, You know that {tension2}. I bring You the real version of me, not the presentable one. Grow {word2} in me today — not by my straining, but by Your Spirit. Amen.",
 "Lord Jesus, {promise2}. I choose to believe that out loud. Give me courage for one small obedience before this day ends. Amen.",
 "Spirit of God, I cannot manufacture {word2}, and I am done pretending I can. Do in me what only You do, and let someone near me feel the difference. Amen.",
 "Father, thank You that {promise2}. Take my hurry, my fear, and my excuses, and lead me one honest step today. Amen."]
const DAYPART=["Tuesday morning","weekday afternoon","quiet evening","early morning","late commute","ordinary weekday"];

function ctxOf(o){const ci=o.ch??o.ci;return{ci,bank:B[ci]||B[0],pool:(window.SPOOLS[ci]||window.SPOOLS[0]).map(i=>D().refs[i]),
 steps:(window.STEPWORDS[ci]||window.STEPWORDS[0]).concat(window.STEPWORDS.verbs)}}
function slots(s,c,word,ref){const w2=lc(word);
 return{word,Word:word,word2:w2,Word2:word[0].toUpperCase()+w2.slice(1),ref,Ref:ref,
  noun:s.pick("n",c.bank.n),noun2:lc(s.pick("n2",c.bank.n)),img:s.pick("i",c.bank.i),
  tension:s.pick("t",c.bank.t),tension2:lc(s.pick("t2",c.bank.t)),
  promise:s.pick("p",c.bank.p),Promise:(x=>x[0].toUpperCase()+x.slice(1))(s.pick("p3",c.bank.p)),promise2:lc(s.pick("p2",c.bank.p)),
  practice:s.pick("pr",c.bank.pr),daypart:s.pick("dp",DAYPART)}}
function seedOf(o,salt){return (parseInt(o.fp,16)||7)^(salt*2654435761)}

/* ---------------- public: day ---------------- */
function day(o,fmtKey,i,total){const c=ctxOf(o);
 const s=stream(seedOf(o,100+i));
 const word=c.steps[(seedOf(o,7)+i*13)%c.steps.length];
 const ref=c.pool[(seedOf(o,11)+i*17)%c.pool.length];
 const ref2=c.pool[(seedOf(o,11)+i*17+5)%c.pool.length];
 const sl=slots(s,c,word,ref);
 const sunday=fmtKey!=="study"&&fmtKey!=="year"&&(i%7===6);
 const unit=fmtKey==="study"?"Session":fmtKey==="year"?"Month":"Day";
 return{n:i+1,unit,word,ref,ref2,sunday,
  read:`Read ${ref} — once for information, once for invitation.`,
  open:fill(s.pick("o",OPEN),sl), truth:fill(s.pick("tr",TRUTH),sl), turn:fill(s.pick("tu",TURN),sl),
  step:fill(s.pick("st",STEPL),sl), q:fill(s.pick("q",QL),sl), pray:fill(s.pick("py",PRAYL),sl)}}
function dayHTML(d,o,labels){labels=labels||{};return `
 <p class="eyebrow gold" style="margin-bottom:4px">${esc(o.t)} · ${d.unit} ${d.n}${d.sunday?" · Sunday":""}</p>
 <h2 style="margin:.1em 0 .3em">${esc(d.word)}</h2>
 <p style="font-style:italic;color:var(--navy-700);border-left:3px solid var(--gold);padding-left:14px;margin:.4em 0 1em">${esc(d.read)}</p>
 <p>${esc(d.open)}</p><p>${esc(d.truth)}</p><p>${esc(d.turn)}</p>
 <p><b>${labels.step||"Today's step"}.</b> ${esc(d.step)}</p>
 <p><b>${labels.reflect||"Reflect"}.</b> ${esc(d.q)}</p>
 <p><b>${labels.pray||"Pray"}.</b> ${esc(d.pray)}</p>
 <p class="muted" style="font-family:var(--ff-label);font-size:11px;letter-spacing:.05em">${labels.also||"Going deeper"}: ${esc(d.ref2)}</p>`}

/* ---------------- sermon ---------------- */
const MOVE_H=[["Name the ache","Ground it in the text","Send them with one step"],
 ["The world's version","God's version","Your Tuesday version"],
 ["What we're all feeling","What God is saying","What we're doing about it"],
 ["The tension","The truth","The turn"]];
function sermon(o,w,opts){opts=opts||{};const c=ctxOf(o);const s=stream(seedOf(o,500+w));
 const word=c.steps[(seedOf(o,7)+w*29)%c.steps.length];
 const texts=[0,1,2].map(k=>c.pool[(seedOf(o,19)+w*23+k*7)%c.pool.length]);
 const sl=slots(s,c,word,texts[0]);
 const heads=s.pick("mh",MOVE_H);
 const big=fill(s.pick("big",["{Promise} — and this week we stop admiring that sentence and start living it.",
  "The gospel's answer to {tension2} is not a technique; it is {word2} — received, then practiced.",
  "You were made for {noun2}, and {ref} shows the way in."]),sl);
 const moves=heads.map((h,mi)=>{const t=texts[mi];const sl2=slots(s,c,word,t);
  const body=[fill(s.pick("m1",["Open the movement by naming it plainly: {tension}. Let the room feel seen before it feels taught.",
   "Walk {ref} phrase by phrase here; resist summarizing what the text says better slowly.",
   "Contrast {img} with the counterfeit our culture sells; the difference preaches itself."]),sl2),
   fill(s.pick("m2",["Land the claim: {promise}. Say it twice; the second time, let silence do some work.",
   "Bring one true story — yours or the church's — where {word2} became visible.",
   "Anticipate the objection out loud ('but what about…') and answer it from {ref}, not from cleverness."]),sl2)].join(" ");
  return{h:`${mi+1}. ${h}`,ref:t,body}});
 const ill=[`Object/image: ${s.pick("il1",c.bank.i)} — put it on the platform or the screen and return to it in each movement.`,
  `Story prompt: a moment this month when ${lc(s.pick("il2",c.bank.t))} — told with permission, ending in ${lc(s.pick("il3",c.bank.p))}.`];
 const land=fill(s.pick("land",["Close small on purpose: one step — {practice} — named specifically, dated, and done before next Sunday.",
  "End with response, not summary: {practice}. Invite the room to stand or write or come — motion seals meaning."]),sl);
 const respond=fill("Response moment: a prayer of confession before commission — grace first, then sending. Give thirty full seconds of silence, then pray {ref} over the room.",sl);
 return{w:w+1,word,title:`${word}: ${fill(s.pick("ti",["The {Word} You Were Made For","When {Word} Feels Far Away","What {Word} Actually Costs","The Practice of {Word}","Where {Word} Begins","{Word}, Together"]),sl)}`,
  big,texts,moves,ill,land,respond}}
function sermonHTML(sm,labels){labels=labels||{};return `
 <div class="sermon"><h4>${labels.week||"Week"} ${sm.w} · ${esc(sm.title)}</h4>
 <div class="texts">${sm.texts.join(" · ")}</div>
 <p><b>${labels.big||"Big idea"}.</b> ${esc(sm.big)}</p>
 ${sm.moves.map(m=>`<p><b>${esc(m.h)}</b> <span class="muted">(${m.ref})</span><br>${esc(m.body)}</p>`).join("")}
 <p><b>${labels.ill||"Illustrations"}.</b> ${esc(sm.ill[0])} ${esc(sm.ill[1])}</p>
 <p><b>${labels.land||"Landing"}.</b> ${esc(sm.land)} ${esc(sm.respond)}</p></div>`}

/* ---------------- group session ---------------- */
function session(o,w){const c=ctxOf(o);const s=stream(seedOf(o,900+w));
 const word=c.steps[(seedOf(o,7)+w*29)%c.steps.length];
 const refs=[0,1].map(k=>c.pool[(seedOf(o,31)+w*19+k*5)%c.pool.length]);
 const sl=slots(s,c,word,refs[0]);
 return{w:w+1,word,refs,
  open:fill(s.pick("go",["When has {tension2} shown up for you lately — small version or big?",
   "Fill in the blank and explain: 'For me, {word2} usually feels ______.'",
   "Describe {img} — where has your week looked like that, or the opposite?"]),sl),
  watch:`Video ${w+1} (12–15 min): the teaching walks ${refs[0]} and lands on one practice for the week.`,
  qs:[fill("What word or phrase in {ref} snagged you on the second reading — and why that one?",sl),
   fill(s.pick("g2",["Where do you most feel the gap between believing '{promise2}' and living it?",
    "What would change in your closest relationship if {word2} grew 10% this month?"]),sl),
   fill(s.pick("g3",["What is the counterfeit version of {word2} our culture sells — and where have you bought it?",
    "Who models {word2} well in your life, and what exactly do they do?"]),sl),
   fill("What is your today-sized step — and what usually stops you at exactly that point?",sl)],
  practice:fill("This week's shared practice: {practice}. Pair up and agree to one text-message check-in by Thursday.",sl),
  pray:fill("Prayer: go around once — one sentence each, honest, unpolished. Close by praying {ref} over the group.",sl),
  next:`Next time: ${refs[1]}.`}}
function sessionHTML(g,labels){labels=labels||{};return `
 <div class="edbox"><h4>${labels.session||"Session"} ${g.w} · ${esc(g.word)}</h4>
 <p class="muted" style="margin:.2em 0 .8em;font-family:var(--ff-label);font-size:11.5px;letter-spacing:.05em">${g.refs[0]} · 45–60 min</p>
 <p><b>${labels.open||"Open"} (10).</b> ${esc(g.open)}</p>
 <p><b>${labels.watch||"Watch"} (15).</b> ${esc(g.watch)}</p>
 <p><b>${labels.discuss||"Discuss"} (25).</b></p><ol style="margin:.2em 0 .8em 18px">${g.qs.map(q=>`<li>${esc(q)}</li>`).join("")}</ol>
 <p><b>${labels.practice||"Practice"}.</b> ${esc(g.practice)}</p>
 <p><b>${labels.pray||"Pray"} (10).</b> ${esc(g.pray)} <span class="muted">${esc(g.next)}</span></p></div>`}

/* ---------------- full-document exports ---------------- */
function docWrap(title,inner){return `<html xmlns:w="urn:schemas-microsoft-com:office:word"><head><meta charset="utf-8"><style>body{font-family:Georgia,serif;line-height:1.5;max-width:640px}h1,h2,h3{font-family:Arial,sans-serif;color:#172542}h1{border-bottom:2px solid #C9A13B;padding-bottom:6px}.k{color:#B98D3E;font-family:Arial;font-size:11px;letter-spacing:2px}</style></head><body><p class="k">LIFETOGETHER · 40 DAY CAMPAIGNS</p><h1>${esc(title)}</h1>${inner}</body></html>`}
function fullDevotional(o,fmtKey,days,labels){let inner="";
 for(let i=0;i<days;i++){const d=day(o,fmtKey,i,days);
  inner+=`<h2>${d.unit} ${d.n} — ${esc(d.word)}${d.sunday?" (Sunday)":""}</h2><p><i>${esc(d.read)}</i></p><p>${esc(d.open)}</p><p>${esc(d.truth)}</p><p>${esc(d.turn)}</p><p><b>Step.</b> ${esc(d.step)}</p><p><b>Reflect.</b> ${esc(d.q)}</p><p><b>Pray.</b> ${esc(d.pray)}</p>`}
 return docWrap(`${o.t} — ${days}-Day Devotional`,inner)}
function fullSermons(o,n){let inner="";
 for(let w=0;w<n;w++){const sm=sermon(o,w);
  inner+=`<h2>Week ${sm.w} — ${esc(sm.title)}</h2><p><i>${sm.texts.join(" · ")}</i></p><p><b>Big idea.</b> ${esc(sm.big)}</p>${sm.moves.map(m=>`<h3>${esc(m.h)} <small>(${m.ref})</small></h3><p>${esc(m.body)}</p>`).join("")}<p><b>Illustrations.</b> ${esc(sm.ill[0])} ${esc(sm.ill[1])}</p><p><b>Landing.</b> ${esc(sm.land)} ${esc(sm.respond)}</p>`}
 return docWrap(`${o.t} — Sermon Builds`,inner)}
function fullGroup(o,n){let inner="";
 for(let w=0;w<n;w++){const g=session(o,w);
  inner+=`<h2>Session ${g.w} — ${esc(g.word)} <small>(${g.refs[0]})</small></h2><p><b>Open.</b> ${esc(g.open)}</p><p><b>Watch.</b> ${esc(g.watch)}</p><p><b>Discuss.</b></p><ol>${g.qs.map(q=>`<li>${esc(q)}</li>`).join("")}</ol><p><b>Practice.</b> ${esc(g.practice)}</p><p><b>Pray.</b> ${esc(g.pray)} ${esc(g.next)}</p>`}
 return docWrap(`${o.t} — Small Group Guide`,inner)}
function download(name,html){const b=new Blob(["\ufeff",html],{type:"application/msword"});
 const a=document.createElement("a");a.href=URL.createObjectURL(b);a.download=name;a.click()}

/* ---------------- standalone topic → context (sermon/group builders, no catalog row) ---- */
const CH_KEYS=[["purpose","calling","mission","meaning"],["identity","worth","enough","beloved"],["community","belong","friend","group","together"],["prayer","worship","fast","sabbath","spirit"],["money","finance","debt","budget","steward","content"],["gener","give","tith","legacy gift"],["legacy","family legacy","generation","inherit","heir","estate"],["marriage","husband","wife","couple"],["parent","kids","children","family","teen"],["anxiety","peace","grief","fear","hope","depress","stress","rest","burnout"],["health","body","illness","healing","caregiv"],["freedom","addict","habit","recovery","shame","forgive"],["season","transition","waiting","single","retire","divorce","widow"],["work","job","career","business","marketplace","calling at work","leader at work"],["lead","serve","volunteer","team","elder"],["vision","values","church","membership","revival"],["ministry","nonprofit","donor","missionary org"],["evangel","neighbor","outreach","justice","mercy","nations","witness"],["advent","christmas","easter","lent","new year","thanksgiving","summer"],["jesus","sermon on the mount","red letter","gospel of","beatitude"],["bible","scripture","psalm","james","romans","study of"],["doubt","question","deconstruct","skeptic","wrestle"],["phone","screen","digital","technology","ai","social media"]];
function topicCtx(topic){const t=(topic||"").toLowerCase();let ci=0,best=0;
 CH_KEYS.forEach((ks,i)=>{const sc=ks.reduce((s,k)=>s+(t.includes(k)?1:0),0);if(sc>best){best=sc;ci=i}});
 let h=0;for(const ch of topic)h=(h*31+ch.charCodeAt(0))|0;
 return{ch:ci,fp:(Math.abs(h)>>>0).toString(16).padStart(6,"0").slice(0,6),t:topic}}

window.Engine={day,dayHTML,sermon,sermonHTML,session,sessionHTML,
 fullDevotional,fullSermons,fullGroup,download,docWrap,topicCtx,banks:B};
})();
