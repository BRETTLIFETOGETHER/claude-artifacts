import re
s = open('/home/claude/site/engine.js').read()
assert 'function gPrayer' not in s, "already applied"

VX = r'''
/* ================= VX: compositional prose engine ================= */
function vx(r,frames,m){ return frames[Math.floor(r()*frames.length)](r,m); }

var VX_PEOPLE=["a young mom","a retired teacher","a night-shift nurse","a small-business owner","a college student","a grandfather of six","a men\u2019s-group regular","a new believer","a longtime deacon","a worship leader","a farmer outside town","a single dad","an empty-nester","a high-school senior"];
var VX_PLACE=["at the kitchen table","on the morning commute","in the break room","on the back porch","between appointments","before the house woke up","after the kids were down","in the church parking lot","over lunch on Tuesdays","in the quiet of the shop"];
var VX_TIMEBOX=["for one month","through a whole season","for forty straight days","every day for a year","longer than anyone expected","until it became a habit","week after week"];

function gRead(r,m,scr){
  var lead=pk(r,["Open ","Turn to ","Find ","Sit down with ","Begin with ","Take ","Start in "]);
  var manner=pk(r,[" and read it slowly, maybe twice"," and let it set the terms for the next few minutes"," and read it once for the room and once for yourself"," without hurry; short passages reward unhurried readers"," out loud if you can; the ear catches what the eye skims"," with a pencil nearby; underline whatever pushes back"," before the day gets a vote"," and stay until one line stays with you"]);
  var why=pk(r,["","","","",
   " The Word does its deepest work on readers who are not rushing.",
   " God has been known to hide a whole week\u2019s help in a few verses.",
   " What you are about to read has steadied people for centuries.",
   " Let Scripture speak first and everything after it gets easier."]);
  return lead+"today\u2019s reading, "+scr+","+manner+"."+why+" ";
}

function gTruth(r,m){
  var f=[
   function(r,m){ return pk(r,["Notice how","Watch the way","Do not miss how","See how plainly"])+" the passage "+pk(r,["treats "+m.c+" as a way of life, not a mood","refuses to separate believing from doing","puts God\u2019s character before our assignment","assumes "+m.c+" will cost something and promises it will be worth it","speaks to ordinary people with real bills and real fears","hands you a promise before it hands you a command"])+pk(r,[".",". That order matters.",". Get that order right and the weight shifts.",". Scripture is more practical than we let it be."]); },
   function(r,m){ return pk(r,["In God\u2019s economy,","In the arithmetic of the Kingdom,","As Scripture counts things,"])+" "+pk(r,[m.c+" is never wasted","small obedience compounds quietly and then all at once","direction matters more than speed","what you plant in secret grows in public","faithfulness is the whole assignment; fruit is God\u2019s department"])+pk(r,[".",", and twenty centuries of changed lives agree.",", which is very good news for slow travelers.",". He watches direction, not distance."]); },
   function(r,m){ return pk(r,["This text was written down so that","These verses outlived every empire that ignored them so that","Someone preserved this passage at real cost so that"])+" someone like you could "+pk(r,["stand on it in a week like this one","hear God\u2019s first word before the culture\u2019s loudest one","borrow its steadiness when yours runs thin","let "+m.c+" move from the page into "+m.ap])+"."; },
   function(r,m){ return pk(r,["God says more about "+m.c+" than about many things we argue louder about","Scripture measures "+m.c+" differently than we do","The Bible never pretends "+m.c+" is easy","God\u2019s commands about "+m.c+" are never arbitrary"])+pk(r,["; what He repeats, He means.","; He counts hearts, not headlines.","; it simply insists it is worth it.","; every one of them protects something precious in you."]); },
   function(r,m){ return pk(r,["Underline the promise before you underline the command","Read it once for information and once for invitation","Let the grace in the text reach you before the instruction does","Look at the verbs; they are where Scripture asks for your hands"])+pk(r,["; God always funds what He orders.","; the second reading is where "+m.c+" changes hands.","; every instruction here sits inside a story where God moved first.","; they are offered to anyone willing to walk them."]); }
  ];
  return vx(r,f,m);
}

function gGroundWrap(r,m,core){
  var lead=pk(r,["Hold this at the center: ","Here is the bedrock under today: ","Say it plainly: ","The whole shelf rests on this: ","If you keep one line from today, keep this: ","Underneath everything else sits a simple claim: ","Write this where you can see it: ","This is the load-bearing wall: "]);
  var land=pk(r,[""," Let that settle before you move on."," Everything else today leans on it."," Read it twice; it can carry the weight."," That is not a slogan; it is a foundation."," Build today on that and the day holds."," It was true before this morning and it will be true after."," The rest of this page is that sentence with its sleeves rolled up."]);
  return lead+core+land;
}

function gOpen(r,m){
  var f=[
   function(r,m){ return pk(r,["Somewhere between the calendar and the to-do list,","Between the school run and the second meeting,","Under the noise of an ordinary week,"])+" most of us lose sight of "+m.c+". "+pk(r,["Not on purpose; it just slips beneath the surface of busy days.","Nobody decides to drift; drift is what happens when nobody decides.","It is not rebellion, usually. It is momentum."])+" Today, "+m.t+" invites you to slow down long enough to find it again."; },
   function(r,m){ return "There is a question underneath today\u2019s reading, and it is worth sitting with before you rush ahead: "+pk(r,["what would change in "+m.ap+" if "+m.c+" became more than a word you agree with?","where has "+m.c+" quietly gone missing from your week, and who noticed first?","if a stranger audited your last month, would they find "+m.c+" anywhere in it?","what is the smallest honest step toward "+m.c+" you have been postponing?"]); },
   function(r,m){ return pk(r,["You can tell what a person really believes by watching a week of their life.","Faith shows up in calendars and bank statements long before it shows up in words.","Convictions are what survive contact with a Tuesday."])+" "+pk(r,["Not the crisis moments; the ordinary ones.","Not the highlight reel; the Tuesday afternoons.","Especially the hours nobody applauds."])+" Today presses gently on those ordinary moments, because that is where "+m.c+" is actually formed."; },
   function(r,m){ return pk(r,["Every journey has a day like this one,","Sooner or later a day like today arrives,","This is one of the hinge days,"])+" "+pk(r,["a day when the idea stops being an idea and starts asking something of you.","when admiration has to decide whether it will become practice.","when the truth moves from the page toward the door."])+" Today, "+m.c+" steps into "+m.ap+"."; },
   function(r,m){ return pk(r,["God did not design "+m.c+" to make your life smaller.","Nothing about "+m.c+" was meant to shrink you.","Whatever you have heard, "+m.c+" is not a leash."])+" "+pk(r,["He designed it to make your life sturdier.","It is scaffolding for a life that can bear weight.","It is how a soul gets load-bearing walls."])+" Today you get to test that claim against a real week."; },
   function(r,m){ return pk(r,["Grace comes first.","Before the assignment, the embrace.","Hear the welcome before the work."])+" Before today says one word about what you should do, "+pk(r,["hear what God has already done.","remember whose idea you were.","let the Father\u2019s posture toward you settle in."])+" "+cap(m.c)+" grows best in soil that knows it is loved."; },
   function(r,m){ return pk(r,["You bring a history into this page:","You did not arrive at today empty-handed:","Today meets you mid-story:"])+" old wins, old wounds, old assumptions about "+m.c+". "+pk(r,["God knows all of it and is discouraged by none of it.","None of it disqualifies you; some of it will turn out to be preparation.","He has read every chapter and still wrote your name on today."]); }
  ];
  return vx(r,f,m);
}

function gTension(r,m){
  var f=[
   function(r,m){ return pk(r,["And yet","Still,","But"])+" "+pk(r,["honesty requires admitting how rarely our days reflect it","the gap between Sunday\u2019s song and Tuesday\u2019s choices stays stubbornly open","the urgent keeps outshouting the important","old habits rarely leave without a fight","fear often gets a vote it was never given"])+"."; },
   function(r,m){ return pk(r,["Left untended,","Unwatched,","Given enough quiet neglect,"])+" "+pk(r,["even the truest convictions fade like a photograph in the sun","a full calendar hides an empty tank for a surprisingly long time","comparison sneaks in the side door and takes the joy on its way out","busyness becomes a socially acceptable way to avoid God"])+"."; },
   function(r,m){ return pk(r,["Meanwhile the culture around you","All week, the loudest voices","Every feed and every ad"])+" "+pk(r,["is discipling you in the opposite direction","keeps selling the opposite of "+m.c,"whispers that later will do"])+pk(r,[".",", one small message at a time.",", and later is where good intentions go to retire."]); },
   function(r,m){ return pk(r,["We keep waiting for a feeling","Most of us are waiting to feel ready","The heart keeps asking for a sign"])+" while "+pk(r,["God is waiting for a step.","heaven is waiting on a decision the size of a mustard seed.","the door stands open at exactly walking height."]); }
  ];
  return vx(r,f,m);
}

function gStory(r){
  var who=pk(r,VX_PEOPLE), where=pk(r,VX_PLACE), span=pk(r,VX_TIMEBOX);
  var f=[
   function(r){ var prac=pk(r,["kept a single word from each day\u2019s reading on a sticky note","prayed one sentence for each person under their roof, by name","wrote one line a night about where God showed up","read the passage before touching the phone","thanked one specific person for one specific thing","gave something away, small but real, before sunset"]);
     var pay=pk(r,["The circumstances did not change much, they said, but nearly every response to them did.","Ask them about it now and they just smile and tap the notebook.","It was the smallest decision, they say, that ever rearranged them.","Nothing dramatic happened, which is exactly how the deep things happen."]);
     return "There is "+who+" who "+prac+" "+span+", usually "+where+". "+pay; },
   function(r){ var act=pk(r,["finally read the passage aloud in group and stopped halfway","asked the oldest saint in the room what the verse had cost them","admitted out loud the thing everyone privately battles","said yes to the week\u2019s challenge without knowing how it would land"]);
     var res=pk(r,["Nobody preached; the text had already done it.","The room got quiet in the good way.","That one honest minute did what a month of fine meetings had not.","Something loosened that had been bolted down for years."]);
     return "In one small group, "+who+" "+act+". "+res; },
   function(r){ var seed=pk(r,["a jar on the counter for every unengineered provision","a list titled people who were kind when they did not have to be","a cheap notebook of one-line prayers","a photo on the fridge of the person they were still learning to forgive"]);
     var use=pk(r,["On the discouraging nights the family pours it out on the table and reads.","It gets opened exactly when cynicism starts sounding like wisdom.","It is nine pages long now and still growing.","They say it has outperformed every pep talk they ever heard."]);
     return "One household keeps "+seed+". "+use; },
   function(r){ var turn=pk(r,["a layoff","a diagnosis nobody saw coming","a season when the prayers felt unanswered","the year everything got loud"]);
     var kept=pk(r,["kept the same chair and the same hour of reading","kept showing up to the Thursday group anyway","kept saying the memory verse out loud on the drive","kept serving in the small hidden way no one tracked"]);
     var wit=pk(r,["The hard season took months to pass, they said, but the habit kept them from losing more than the season took.","Looking back, the routine was the raft.","It did not fix the situation; it fixed their footing.","What survived the year, they say, is what had been practiced before it."]);
     return "After "+turn+", "+who+" "+kept+". "+wit; },
   function(r){ var small=pk(r,["gave up the front seat for a month as a private experiment in dying to self","fasted from having an opinion for a week and just listened","walked one slow lap of the block praying for what they actually saw","set the alarm nine minutes earlier so the Word beat the feed"]);
     var after=pk(r,["They laugh about it now. They also never really went back.","Seven days taught them more than the previous seven years of hurry.","It was almost embarrassingly small, which turned out to be the point.","The habit outlived the experiment."]);
     return "One week, "+who+" "+small+". "+after; },
   function(r){ var quiet=pk(r,["set up chairs before anyone arrived, for thirty years","prayed room by room down the hallway on every night shift","blessed each bedroom doorframe after the house went dark","showed up on the ordinary Thursdays long after the casseroles stopped"]);
     var reveal=pk(r,["At the funeral, half the room stood when the family asked who had been helped; nobody had known the whole of it.","The kids found out years later; two of them cried, and all of them remembered feeling strangely safe.","Casseroles feed a week, the widow said. Thursdays rebuilt a life.","Heaven, presumably, kept better records than the bulletin did."]);
     return "There was "+who+" who "+quiet+". "+reveal; }
  ];
  return vx(r,f,null);
}

function gApply(r,m){
  var f=[
   function(r,m){ return "So what does this look like on an ordinary "+pk(r,["Tuesday","Thursday","weekday"])+"? "+pk(r,["One concrete move of "+m.c+" inside "+m.ap+", small enough to actually do, real enough to matter.","Pick the smallest honest version and do it before "+pk(r,["noon","dinner","the day closes"])+".","Not a program; a decision. One conversation, one choice, one moment claimed for "+m.c+"."]); },
   function(r,m){ return pk(r,["Lower the bar until you cannot fail, then clear it.","Do the next right thing, then the next.","Trade one complaint for one thank-you today."])+" "+pk(r,["Momentum in the Kingdom starts embarrassingly small.","You are not responsible for the staircase, only the step in front of "+m.ap+".","It sounds simple because it is; it is also how hearts get rewired."]); },
   function(r,m){ return pk(r,["Give "+m.c+" a time and a place today","Put it on the calendar, in ink","Name the hour where "+m.c+" will be tested and meet it on purpose"])+"; "+pk(r,["vague intentions evaporate, scheduled obedience shows up.","what gets scheduled gets a fighting chance.","decide now how you will answer before the moment asks."]); },
   function(r,m){ return pk(r,["Tell one person","Text a friend","Say it out loud at the table"])+" "+pk(r,["what you read this morning","the sentence you underlined","the step you intend to take"])+"; "+pk(r,["spoken truth roots deeper than silent truth.","spoken plans have a survival rate private ones do not.","your words may be the nudge someone else was praying for."]); },
   function(r,m){ return pk(r,["Practice the pause today:","Build in the three-second gap:","Before the reaction, the purchase, or the reply, breathe once and pray once:"])+" "+cap(m.c)+" lives in that gap, and so, often, does everyone\u2019s dignity."; },
   function(r,m){ return pk(r,["Serve someone secretly before sunset","Do one kind, unrequired thing for the person hardest to love this week","Give something away today: time, money, credit, or the last word"])+". "+pk(r,[cap(m.c)+" that no one applauds is "+m.c+" at full strength.","Open hands are how "+m.c+" breathes.","Hidden is not lesser; hidden is where the roots go."]); }
  ];
  return vx(r,f,m);
}

function gClose(r,m){
  var f=[
   function(r,m){ return pk(r,["Whatever today did or did not accomplish, you showed up to hear from God.","You gave God the first word today; let Him have the last one tonight.","You are one honest day further along, and that is the only comparison Scripture asks of you."])+" "+pk(r,["Never underestimate what He does with people who keep showing up.","Rest is also an act of trust.","Stack enough days this size and you get a different life."]); },
   function(r,m){ return pk(r,["Do not grade today; offer it.","The seed went into the ground today; do not dig it up to check.","Take the pressure off the moment and put your confidence in the process."])+" "+pk(r,["Graded days breed anxiety; offered days breed peace.","Water it with a little trust and go to sleep.","God works in journeys, and you are in one."]); },
   function(r,m){ return "Carry one sentence from today into the evening"+pk(r,[", and let it interrupt you at least once.",", the way you would carry a key.",", especially into the hour you are dreading."])+" "+pk(r,["Interruptions are how the Spirit edits a day.","Truth in the pocket beats truth on the shelf.","The same God who met you on this page goes ahead of you into tomorrow\u2019s calendar."]); },
   function(r,m){ return pk(r,["If today\u2019s word stung a little, that is usually the sign it landed where it was needed.","Growth is mostly invisible until suddenly it is not.","What you practiced in private today will eventually show up in public."])+" "+pk(r,["Sting fades; fruit stays.","Trust the underground season; spring keeps its appointments.","That is not pressure; that is a promise."]); },
   function(r,m){ return "Let the day end quieter than it began: "+pk(r,["two slow breaths, one honest prayer,","one thank-you spoken out loud,","thirty unhurried seconds with the memory verse,"])+" and permission to leave the unfinished with the God who never sleeps."; }
  ];
  return vx(r,f,m);
}

function gPrayer(r,m){
  var addr=pk(r,["Father,","Lord,","God of grace,","Lord Jesus,","Father in heaven,","Faithful God,"]);
  var open=pk(r,["thank You for meeting me in these words today.","You know exactly which part of this page was written for me.","thank You that Your mercies restarted this morning.","I bring You the real week, the real worries, the real me.","before I ask for anything, thank You for wanting to be asked.","You have been more patient with me than I have been with myself."]);
  var pet=pk(r,["Grow "+m.c+" in me, not as a burden I carry but as fruit You produce.","Close the gap between what I believe about "+m.c+" and how I live it.","Give me one clear chance today to practice "+m.c+", and the willingness to see it.","Teach me "+m.c+" the way You always teach: with grace, with truth, one day at a time.","Interrupt me at the right moment with what I read this morning.","Guard the hidden places where "+m.c+" is still small and easily discouraged."]);
  var sur=pk(r,["I set down my own strength and pick up Yours instead.","Be Lord of my calendar, my money, and my mouth today; they were Yours anyway.","Do in me what I cannot manufacture in myself.","Finish what You began in me, especially on the days I want to quit quietly.","Make me quick to listen, slow to speak, and easy for You to interrupt.","Let my home feel different tonight because You worked on me today."]);
  var amen=pk(r,["In Jesus\u2019 name, amen.","Amen.","Through Christ my Lord, amen.","In Your strong name, amen."]);
  return addr+" "+open+" "+pet+" "+sur+" "+amen;
}

function gQuestion(r,m){
  var f=[
   function(r,m){ return "Where in your life right now is God inviting you to take "+m.c+" more seriously, and "+pk(r,["what makes that hard?","what has been the cost of waiting?","who could help you say yes?"]); },
   function(r,m){ return pk(r,["What would the people closest to you say","What would your calendar say","What would last month\u2019s bank statement say"])+" about how "+m.c+" actually shows up in your week?"; },
   function(r,m){ return "If nothing about "+m.ap+" changed for a year, "+pk(r,["what would that cost you, and what would one small change make possible?","who besides you would pay for it?","would you be at peace with that, honestly?"]); },
   function(r,m){ return pk(r,["When was the last time "+m.c+" cost you something real,","When did God last prove Himself faithful to you,","When did you last do a hidden kindness no one could trace,"])+" and "+pk(r,["what did you learn in the paying?","why is that hard to remember in the present?","what did it do to your own heart?"]); },
   function(r,m){ return pk(r,["What is one belief about "+m.c+" you inherited without examining","What part of today\u2019s reading did you want to skip past","What are you white-knuckling that today\u2019s passage invites you to hand over"])+", and "+pk(r,["does Scripture agree with it?","what might be buried there?","what would opening that hand look like this week?"]); },
   function(r,m){ return "Who in your life models "+m.c+" well, and what one thing could you "+pk(r,["borrow from their example this week?","ask them about over coffee?","start imitating before Sunday?"]); }
  ];
  return vx(r,f,m);
}

function gStepCore(r,m,weekly){
  var horizon=weekly?pk(r,["this week","before the group meets again","every day this week"]):pk(r,["before the day ends","by tonight","before you sleep"]);
  var act=pk(r,["do one deliberate act of "+m.c+" in "+m.ap,"write today\u2019s key thought where your eyes will land, and read it once more at night","share one sentence from today with someone in your circle","set aside ten unhurried, screenless minutes and let God finish the conversation this page started","thank one specific person for one specific thing, out loud","pray one sentence for each person who lives under your roof, by name","do a hidden kindness no one can trace back to you","take one thing off tomorrow\u2019s list on purpose and treat the space as an offering","say the memory verse aloud "+(weekly?"each morning":"three times: morning, midday, night"),"circle one name of someone far from God and pray for them each time you check the time","apologize for one thing cleanly, with no comma and no excuse","choose your first five waking minutes tonight, before the feed can claim them"]);
  var tail=pk(r,["Small obedience, repeated, is how a journey like this changes a life.","Streaks are built from days exactly this size.","Hidden is the point.","Spoken plans survive; private ones evaporate.","Watch what it unlocks.","Gratitude spoken out loud waters everything this journey is planting."]);
  return cap(act)+" "+horizon+". "+tail;
}
function gStep(r,m){ return gStepCore(r,m,false); }
function gPractice(r,m){ var x=gStepCore(r,m,true); return "This week\u2019s practice: "+x.charAt(0).toLowerCase()+x.slice(1); }

function gHook(r,m){
  var f=[
   function(r,m){ return "Here is a question worth carrying into today: "+pk(r,["what would it look like if "+m.c+" showed up in "+m.ap+" before dinner tonight?","if a friend asked you over coffee what "+m.c+" actually means, what would you say?","what is the difference, in your week, between admiring "+m.c+" and living it?"]); },
   function(r,m){ return pk(r,["Most of us do not need more information about "+m.c+"; we need a moment of honesty about it.","Some words get worn smooth by church use, and "+m.c+" is one of them.","Nobody drifts into "+m.c+"; people only drift away from it."])+" "+pk(r,["Today is that moment.","Today, let Scripture give it back its edges.","Growth is always on purpose, and today is a day for purpose."]); },
   function(r,m){ return pk(r,["Before you read another word,","Slow down for sixty seconds and","Put the phone face-down and"])+" name one place in your week where "+m.c+" has been missing. "+pk(r,["Hold that place in mind as you read.","Bring it with you into the passage.","That is the address today\u2019s truth is being delivered to."]); },
   function(r,m){ return "You have read about "+m.c+" before. "+pk(r,["Today, let it read you.","Today is about crossing the line from agreement to practice.","Today, God gets the first word about it, before the critics and before your own inner voice."]); }
  ];
  return vx(r,f,m);
}

function gTomorrow(r,d,n,nextPart){
  if(d>=n) return pk(r,["Tomorrow you will look back down the whole road; finish today with gratitude for how far God has brought you.","The last page is close now. End today thankful, and come ready to remember everything.","One more sunrise and the journey turns to celebration. Walk today\u2019s step well."]);
  var lead=pk(r,["Tomorrow the journey continues","The road picks up again tomorrow","Day "+(d+1)+" is already waiting","Tomorrow adds the next stone to the path","The next page turns in the morning"]);
  var mid=nextPart?pk(r,[", crossing into "+nextPart,", and with it a new stretch called "+nextPart,"; ahead lies "+nextPart]):"";
  var tail=pk(r,[", one day, one step at a time.",". Bring today\u2019s honesty with you.",". Same time, same grace.",". Small steps, long obedience.",". You will not be walking it alone."]);
  return lead+mid+tail;
}
function gCarry(r){
  return pk(r,["carry this week\u2019s memory verse into one specific moment before evening and let it have the final word there.","say this week\u2019s verse once out loud before the day ends, wherever the day finds you.","let this week\u2019s verse interrupt you once today, right in the middle of something ordinary.","keep this week\u2019s verse within reach; one honest repetition beats ten hurried readings.","hand this week\u2019s verse to one other person today and watch it do double duty.","let this week\u2019s verse be the last thing you read tonight, after every screen has gone dark."]);
}
function gProvision(r,occ){
  return pk(r,["And because this journey was built with "+occ+" in view, do not be surprised when today\u2019s step lands close to home; that is design, not accident.","This journey was shaped for "+occ+", so if today feels unusually well-timed, it is: provision tends to look like coincidence from up close.","Built as it was for "+occ+", today\u2019s challenge may fit your week uncomfortably well. Take that as a kindness."]);
}
function gPromise(r,t,sub,c){
  if(sub){ var core=sub.replace(/\.$/,'');
    return pk(r,["This whole journey is about one promise: "+core+". Today adds one more brick to it.","Remember the sentence over the door: \u201C"+core+".\u201D Today is that sentence, practiced.","Everything here still points the same direction: "+core+". Today walks another mile of it.","The promise has not moved: "+core+". Days like this one are how it comes true."]); }
  return pk(r,["Everything in "+t+" is building toward the same place: a life where "+c+" is not an idea you visit but ground you live on.","The destination has not changed: "+c+" as home address, not vacation spot.","Every day of "+t+" leans the same way, toward "+c+" you can stand on."]);
}
function gAnchorLabel(r){ return pk(r,["Anchor for today","Carry this today","Today\u2019s anchor","Hold this line today","Take this with you"]); }
function gScrFirst(r,m,scr){
  return pk(r,["Before anything else today, open ","Let the text go first this morning: open ","Today begins in the Book: turn to ","Give Scripture the opening word; find "]) + scr + pk(r,[" and let it speak before anyone else does."," and read before the day starts negotiating."," while the coffee is still hot and the opinions are still asleep."," and let it set the table for everything below."])+" "+gTruth(r,m);
}
function gExtendWrap(r,core){
  var lead=pk(r,["One more thought before you go. ","A short word for the road. ","Before you close this page: ","Linger ten more seconds on this. "]);
  var tail=pk(r,[" Take the smallest version of today\u2019s step and let it count, because it does."," You are one faithful day further along than yesterday, and God does remarkable things with people who refuse to stop walking."," Grace has no makeup work, only next steps."," Let that be enough for today; it is."]);
  return lead+core+tail;
}
'''

anchor = 'var MONEY_NOTE='
i = s.index(anchor)
s = s[:i] + VX + '\n' + s[i:]

old = '''    /* building blocks */
    var open=fill(px(OPENS,2,d),map)+" "+px(TENSIONS,3,d);
    var hook=fill(px(HOOKS,4,d),map);
    var word=[
      "Open today's reading, "+scr+", and read it slowly, maybe twice. ",
      "Turn to "+scr+" and let it set the terms for the next few minutes. ",
      "Today's text is "+scr+". Read it once for the room and once for yourself. ",
      "Take "+scr+" slowly today; short passages reward unhurried readers. "
    ][(H2+d)%4]
      +fill(px(TRUTHS,5,d),map)+" "+rot(fam.ground,(d-1+((H^H2)>>>1)%fam.ground.length)%fam.ground.length)
      +" "+fill(px(TRUTHS,6,d),map);
    var story=px(STORIES,7,d);
    var apply=fill(px(APPLYS,8,d),map)+" "+fill(px(APPLYS,9,d),map)
      +(C[12]?" And because this journey was built with "+C[12].toLowerCase()+" in view, don't be surprised if today's step lands close to home. That is not coincidence; that is provision.":"")
      +" "+rot(fam.ground,(d+2+(H2>>>2)%7)%fam.ground.length);
    var close=fill(px(CLOSES,10,d),map);
    /* campaign promise line, woven in every few days so the journey keeps its own voice */
    var promise = C[1] ? "This whole journey is about one promise: "+C[1].replace(/\\.$/,'')+". Today adds one more brick to it."
                       : "Everything in "+t+" is building toward the same place: a life where "+c+" is not an idea you visit but ground you live on.";
    /* four rotating day structures */
    var shape=(H+d)%4, paras;
    if(shape===0)      paras=[open, word, story, apply, close];
    else if(shape===1) paras=[hook, word, apply+" "+px(TENSIONS,11,d), story, close];
    else if(shape===2) paras=[story, open, word, apply, close];
    else               paras=["Before anything else today, open "+scr+" and let it speak first. "+fill(px(TRUTHS,12,d),map), hook, story, apply, close];'''
assert old in s, "devotional beats anchor"
new = '''    /* building blocks (VX compositional) */
    var rB=rngFor(C[9],'vx'+d);
    var open=gOpen(rB,map)+" "+gTension(rB,map);
    var hook=gHook(rB,map);
    var groundCore=rot(fam.ground,(d-1+((H^H2)>>>1)%fam.ground.length)%fam.ground.length);
    var word=gRead(rB,map,scr)+gTruth(rB,map)+" "+gGroundWrap(rB,map,groundCore)+" "+gTruth(rB,map);
    var story=gStory(rB);
    var apply=gApply(rB,map)+" "+gApply(rB,map)
      +(C[12]?" "+gProvision(rB,C[12].toLowerCase()):"");
    var close=gClose(rB,map);
    var promise=gPromise(rB,t,C[1],c);
    /* four rotating day structures */
    var shape=(H+d)%4, paras;
    if(shape===0)      paras=[open, word, story, apply, close];
    else if(shape===1) paras=[hook, word, apply+" "+gTension(rB,map), story, close];
    else if(shape===2) paras=[story, open, word, apply, close];
    else               paras=[gScrFirst(rB,map,scr), hook, story, apply, close];'''
s = s.replace(old, new)

old = 'pray:fill(px(PRAYERS,14,d),map),'
assert old in s
s = s.replace(old, 'pray:gPrayer(rB,map),')
old = 'q:fill(px(QUESTIONS,15,d),map),'
assert old in s
s = s.replace(old, 'q:gQuestion(rB,map),')
m2 = re.search(r'step:fill\(px\(STEPS,16,d\),map\)\+"[^"]*"', s)
assert m2, "step anchor"
s = s[:m2.start()] + 'step:gStep(rB,map)' + s[m2.end():]

old = 'if(wcount<380) bodyHtml+="<p>"+px(EXTEND,13,d)+"</p>";'
assert old in s
s = s.replace(old, 'if(wcount<380) bodyHtml+="<p>"+gExtendWrap(rB,px(EXTEND,13,d))+"</p>";')

# --- the anchor/carry/tomorrow tail (the 168x offender) ---
m3 = re.search(r'body:bodyHtml\+"<p><em>Anchor for today:</em> "\+mem\.v\+" \u2014 "\+\[[\s\S]*?"</p>",', s)
assert m3, "tail anchor"
tail_new = ('body:bodyHtml+"<p><em>"+gAnchorLabel(rB)+":</em> "+mem.v+" \\u2014 "+gCarry(rB)'
            '+" "+gTomorrow(rB,d,n,(d===spans[pi][1]&&parts[pi+1])?parts[pi+1]:null)+"</p>",')
s = s[:m3.start()] + tail_new + s[m3.end():]

# --- groupStudy: route questions & practices through generators ---
cnt1 = len(re.findall(r'fill\(rot\(QUESTIONS,\(HH\+i\*3\)%QUESTIONS\.length\),map\)', s))
s = re.sub(r'fill\(rot\(QUESTIONS,\(HH\+i\*3\)%QUESTIONS\.length\),map\)', 'gQuestion(rGS,map)', s)
cnt2 = len(re.findall(r'fill\(rot\(QUESTIONS,\(HH\+i\*4\+m\)%QUESTIONS\.length\),map\)', s))
s = re.sub(r'fill\(rot\(QUESTIONS,\(HH\+i\*4\+m\)%QUESTIONS\.length\),map\)', 'gQuestion(rGS,map)', s)
cnt3 = len(re.findall(r'rot\(PRACTICES,\(HH\+i\*3\)%PRACTICES\.length\)', s))
s = re.sub(r'rot\(PRACTICES,\(HH\+i\*3\)%PRACTICES\.length\)', 'gPractice(rGS,map)', s)
# declare rGS at the top of the session loop
m4 = re.search(r'for\(var i=0;i<NS;i\+\+\)\{', s)
assert m4, "session loop anchor"
s = s[:m4.end()] + "\n    var rGS=rngFor(C[9],'gs'+i);" + s[m4.end():]

open('/home/claude/site/engine.js','w').write(s)
print("VX installed; groupStudy Q/practice routed (%d/%d/%d)" % (cnt1,cnt2,cnt3))
