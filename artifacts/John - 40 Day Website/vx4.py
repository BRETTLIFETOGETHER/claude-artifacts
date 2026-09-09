import re
s = open('/home/claude/site/engine.js').read()
E = []

def rep(old, new, tag):
    global s
    assert old in s, tag
    s = s.replace(old, new, 1)
    E.append(tag)

# 1) gStoryMoral: tails become '; '-joined clauses (single sentence, lead is m.c-infused)
rep('''  var tail=pk(r,[""," Yours will look different, and that is the point."," The ingredients are all within reach of an ordinary week."," Small is not the opposite of significant; hidden is not the opposite of real."," The same Spirit is available at your address."," Borrow the pattern; God supplies the rest."," It cost less than expected and paid more."]);
  return lead+tail;''',
'''  var tail=pk(r,["","; yours will look different, and that is the point","; the ingredients are all within reach of an ordinary week","; small is not the opposite of significant there","; the same Spirit is on call at your address","; borrow the pattern and let God supply the rest","; it cost less than expected and paid more than promised","; the entry requirements were a pulse and a yes"]);
  return lead.replace(/\\.$/,"")+tail+".";''', "moral fuse")

# 2) gTomorrow: '.'-style tails become ';'-clauses
rep('''  var tail=pk(r,[", one day, one step at a time.",". Bring today\\u2019s honesty with you.",". Same time, same grace.",". Small steps, long obedience.",". You will not be walking it alone.",". Come as you are; that has always been the dress code.",". The manna will be fresh again."]);''',
'''  var tail=pk(r,[", one day, one step at a time.","; bring today\\u2019s honesty with you.","; same time, same grace.","; small steps, long obedience.","; you will not be walking it alone.","; come as you are, which has always been the dress code.","; the manna will be fresh again.","; pack tonight\\u2019s gratitude, it travels well."]);''', "tomorrow fuse")

# 3) gClose frames: fuse two-sentence patterns with '; '
rep('''return pk(r,["Whatever today did or did not accomplish, you showed up to hear from God.","You gave God the first word today; let Him have the last one tonight.","You are one honest day further along, and that is the only comparison Scripture asks of you.","However the hours went, this page happened, and that counts.","Day "+d+" goes into the books tonight, imperfect and offered."])+" "+pk(r,["Never underestimate what He does with people who keep showing up.","Rest, too, is an act of "+m.c+".","Stack enough days this size and you get a different life.","He is not grading Day "+d+"; He is growing something through it.","Showing up is most of the miracle.","In the economy of "+m.c+", present beats impressive."]);''',
'''var l1=pk(r,["Whatever today did or did not accomplish, you showed up to hear from God","You gave God the first word today; let Him have the last one tonight","You are one honest day further along, and that is the only comparison Scripture asks of you","However the hours went, this page happened, and that counts","Day "+d+" goes into the books tonight, imperfect and offered"]); return l1+pk(r,["; never underestimate what He does with people who keep showing up.","; rest, too, is an act of "+m.c+".","; stack enough days this size and you get a different life.","; He is not grading Day "+d+", He is growing something through it.","; showing up is most of the miracle.","; in the economy of "+m.c+", present beats impressive."]);''', "close f1 fuse")

rep('''return pk(r,["Do not grade today; offer it.","The seed went into the ground today; do not dig it up to check.","Take the pressure off the moment and put your confidence in the process.","Close the ledger; open your hands.","Let the day be a deposit, not a verdict."])+" "+pk(r,["Graded days breed anxiety; offered days breed peace.","Water Day "+d+" with a little trust and go to sleep.","God works in journeys, and "+m.t+" is one.","Sleep is a nightly rehearsal of trust; take the rehearsal.","Tomorrow inherits whatever "+m.c+" you plant tonight."]);''',
'''var l2=pk(r,["Do not grade today; offer it","The seed went into the ground today; do not dig it up to check","Take the pressure off the moment and put your confidence in the process","Close the ledger and open your hands","Let the day be a deposit, not a verdict"]); return l2+pk(r,[", because graded days breed anxiety and offered days breed peace.",", then water Day "+d+" with a little trust and go to sleep.",", for God works in journeys, and "+m.t+" is one.",", and let sleep be its nightly rehearsal of trust.",", since tomorrow inherits whatever "+m.c+" you plant tonight."]);''', "close f2 fuse")

rep('''return pk(r,["If today\\u2019s word stung a little, that is usually the sign it landed where it was needed.","Growth is mostly invisible until suddenly it is not.","What you practiced in private today will eventually show up in public.","If nothing felt dramatic, good; roots rarely do.","Do not confuse quiet with nothing happening."])+" "+pk(r,["Sting fades; the fruit of "+m.c+" stays.","Trust the underground season; spring keeps its appointments.","That is not pressure; that is a promise.","Depth in "+m.c+" is being added where you cannot see it yet.","The harvest never asks how Day "+d+"’s planting felt."]);''',
'''var l4=pk(r,["If today\\u2019s word stung a little, that is usually the sign it landed where it was needed","Growth is mostly invisible until suddenly it is not","What you practiced in private today will eventually show up in public","If nothing felt dramatic, good, because roots rarely do","Do not confuse quiet with nothing happening"]); return l4+pk(r,["; sting fades and the fruit of "+m.c+" stays.","; the underground season is still a season, and spring keeps its appointments.","; that is not pressure, that is a promise.","; depth in "+m.c+" is being added where you cannot see it yet.","; the harvest never asks how Day "+d+"\\u2019s planting felt."]);''', "close f4 fuse")

# 4) gApply frame 2: fuse
rep('''return pk(r,["Lower the bar until you cannot fail, then clear it.","Do the next right thing, then the next.","Trade one complaint for one thank-you today.","Shrink the assignment until courage is optional.","Start closer than feels impressive."])+" "+pk(r,["Momentum in the Kingdom starts embarrassingly small.","You are not responsible for the staircase, only the step in front of "+m.ap+".","It sounds simple because it is; it is also how hearts get rewired.","Faithfulness compounds faster than brilliance.","Ten humble minutes of "+m.c+" beat one heroic intention.","Little, done today, outruns much, planned for someday."]);''',
'''var a2=pk(r,["Lower the bar until you cannot fail, then clear it","Do the next right thing, then the next","Trade one complaint for one thank-you today","Shrink the assignment until courage is optional","Start closer than feels impressive"]); return a2+pk(r,["; momentum in the Kingdom starts embarrassingly small.","; you are not responsible for the staircase, only the step in front of "+m.ap+".","; it sounds simple because it is, and it is also how hearts get rewired.","; faithfulness compounds faster than brilliance.","; ten humble minutes of "+m.c+" beat one heroic intention.","; little, done today, outruns much, planned for someday."]);''', "apply f2 fuse")

# 5) gApply frame 6: fuse
rep('''+". "+pk(r,[cap(m.c)+" that no one applauds is "+m.c+" at full strength.","Open hands are how "+m.c+" breathes.","Hidden is not lesser; hidden is where the roots go.","Secrecy keeps the motive clean and the joy strange.","Let heaven be the only audience today."]); }''',
'''+pk(r,[", because "+m.c+" that no one applauds is "+m.c+" at full strength.",", since open hands are how "+m.c+" breathes.",", for hidden is not lesser, hidden is where the roots go.",", and let secrecy keep the motive clean and the joy strange.",", with heaven as the only audience today.",", and let the receipt stay between you and God."]); }''', "apply f6 fuse")

# 6) gOpen frame1 mid + frame3 mid: fuse into surrounding
rep('''+" most of us lose sight of "+m.c+". "+pk(r,["Not on purpose; it just slips beneath the surface of busy days.","Nobody decides to drift; drift is what happens when nobody decides.","It is not rebellion, usually. It is momentum.","No one schedules the forgetting; it books itself.","The loss is quiet, which is why it goes unnoticed so long.","It leaks out through a hundred small hurries."])''',
'''+" most of us lose sight of "+m.c+pk(r,[", not on purpose, it just slips beneath the surface of busy days.",", and nobody decides to drift; drift is what happens when nobody decides.",", not from rebellion, usually, but from momentum.",", because no one schedules the forgetting; it books itself.",", and the loss is quiet, which is why it goes unnoticed so long.",", leaking out through a hundred small hurries.",", the way keys vanish: nearby, unnoticed, urgent only later."])''', "open f1 fuse")

rep('''+" "+pk(r,["Not the crisis moments; the ordinary ones.","Not the highlight reel; the Tuesday afternoons.","Especially the hours nobody applauds.","Mostly in the minutes that never make it to prayer requests.","In traffic, in checkout lines, in the last hour before bed.","In the small rooms where no one is grading."])+" Today presses gently''',
'''+pk(r,[" \\u2014 not the crisis moments, the ordinary ones."," \\u2014 not the highlight reel, the Tuesday afternoons."," \\u2014 especially the hours nobody applauds."," \\u2014 mostly in minutes that never make it to prayer requests."," \\u2014 in traffic, in checkout lines, in the last hour before bed."," \\u2014 in the small rooms where no one is grading."])+" Today presses gently''', "open f3 fuse")

# 7) gRead: why becomes ';'-clause fused to the manner sentence
rep('''  var why=pk(r,["","","",
   " The Word does its deepest work on readers who are not rushing.",
   " God has been known to hide a whole week\\u2019s help in a few verses.",
   " Read it as a page of "+m.t+", written for exactly this stretch.",
   " Somewhere in it is the day\\u2019s word on "+m.c+"; stay until you find it.",
   " What you are about to read has steadied people for centuries.",
   " Let Scripture speak first and everything after it gets easier.",
   " A text this old has outlived every hurry that ever ignored it.",
   " These lines were prayed over before you were born.",
   " Expect one sentence to follow you into the afternoon.",
   " Somebody once crossed an ocean to keep this page in the language you read."]);
  return lead+"today\\u2019s reading, "+scr+","+manner+"."+why+" ";''',
'''  var why=pk(r,["","","",
   "; the Word does its deepest work on readers who are not rushing",
   "; God has been known to hide a whole week\\u2019s help in a few verses",
   "; read it as a page of "+m.t+", written for exactly this stretch",
   "; somewhere in it is the day\\u2019s word on "+m.c+", so stay until you find it",
   "; what you are about to read has steadied people for centuries",
   "; let Scripture speak first and everything after it gets easier",
   "; a text this old has outlived every hurry that ever ignored it",
   "; these lines were prayed over before you were born",
   "; expect one sentence to follow you into the afternoon",
   "; somebody once crossed an ocean to keep this page in your language"]);
  return lead+"today\\u2019s reading, "+scr+","+manner+why+". ";''', "read fuse")

# 8) gGroundWrap: land becomes ';'-clause
rep('''  var land=pk(r,[""," Let that settle before you move on."," Everything else today leans on it."," Read it twice; it can carry the weight."," That is not a slogan; it is a foundation."," Build today on that and the day holds."," It was true before this morning and it will be true after."," The rest of this page is that sentence with its sleeves rolled up."," Churches have been built on less."," Say it once out loud; some truths need air."]);''',
'''  var land=pk(r,["","","; let that settle before you move on","; everything else today leans on it","; read it twice, it can carry the weight","; that is not a slogan, it is a foundation","; build today on that and the day holds","; it was true before this morning and it will be true after","; the rest of this page is that sentence with its sleeves rolled up","; churches have been built on less","; say it once out loud, some truths need air"]);''', "ground land fuse")
rep('return lead+head+restStr+land;','return lead+head.replace(/\\.$/,"")+ (restStr? restStr.replace(/\\.$/,"") : "") + land + ".";', "ground assemble")

# 9) gHook frames 2 & 4: fuse second sentences
rep('''])+" "+pk(r,["Today is that moment.","Today, let Scripture give it back its edges.","Growth is always on purpose, and today is a day for purpose.","Today is about closing that gap by an inch."]); },''',
''']).replace(/\\.$/,"")+pk(r,["; today is that moment.","; today, let Scripture give it back its edges.",", and growth is always on purpose, today included.","; today is about closing that gap by an inch.","; consider this page the appointment."]); },''', "hook f2 fuse")
rep('''return "You have read about "+m.c+" before. "+pk(r,["Today, let it read you.","Today is about crossing the line from agreement to practice.","Today, God gets the first word about it, before the critics and before your own inner voice.","Today, expect it to ask for your hands, not just your highlighter."]);''',
'''return "You have read about "+m.c+" before"+pk(r,["; today, let it read you.","; today is about crossing the line from agreement to practice.","; today, God gets the first word about it, before the critics and before your own inner voice.","; today, expect it to ask for your hands, not just your highlighter.","; today it does the reading."]);''', "hook f4 fuse")

# 10) gTension frame4 landing fuse (short but some >40 composites) & frame1 punct-clauses stay (already single sentence)
rep('''+" while "+pk(r,["God is waiting for a step.","heaven is waiting on a decision the size of a mustard seed.","the door stands open at exactly walking height.","the invitation sits there with today\\u2019s date on it.","obedience idles in the driveway with the engine running."]); }''',
'''+" while "+pk(r,["God is waiting for a step","heaven is waiting on a decision the size of a mustard seed","the door stands open at exactly walking height","the invitation sits there with today\\u2019s date on it","obedience idles in the driveway with the engine running","the water is not getting any warmer for the watching"])+pk(r,[".",", which is a very short walk.",", closer than the excuse.",", and it has your name on it."]); }''', "tension f4 widen")

open('/home/claude/site/engine.js','w').write(s)
print("v4 fuse pass:", len(E), "edits:", ", ".join(E))
