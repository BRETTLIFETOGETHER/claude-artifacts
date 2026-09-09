import re
s = open('/home/claude/site/engine.js').read()

# ---- gDeeper: theme/title/day-infused banks ----
old = re.search(r'function gDeeper\(r,m,d\)\{[\s\S]*?\n\}', s)
assert old, "gDeeper"
new = r'''function gDeeper(r,m,d){
  var a=pk(r,["One more thought before you go.","A short word for the road.","Before you close this page, linger here a moment.","Take ten more seconds for this.","A last thing, and it matters.","Day "+d+" has one more thing to say.","Before Day "+d+" closes, hear this.","One footnote to today, worth the ink.","Do not leave the page quite yet.","Here is the quiet postscript to Day "+d+"."]);
  var b=pk(r,["Journeys like "+m.t+" work by accumulation, not intensity; the reading was short on purpose.","If you came to Day "+d+" with nothing left, you came to the right page; God has never required a full tank at the door.","Somewhere in your church, someone else read this exact page of "+m.t+" today, at a kitchen table or in a hospital chair; you are not walking alone.","The same weakness resurfacing on different days is not failure; it is the curriculum of "+m.c+", and every pass takes more ground than you can feel.","The enemy\u2019s favorite word on a road like this is later; Scripture\u2019s favorite is today, and every today you choose loosens the old pattern.","Feelings are the caboose, not the engine of "+m.c+"; keep making small right choices and let the feelings catch up on their own schedule.","If you miss a day of "+m.t+", do not double up and do not drop out; grace has no makeup work, only next steps.","Bring today\u2019s question about "+m.c+" to your group this week; readings are personal, but they were never meant to stay private.","Forty different mornings will read this page forty different ways; Day "+d+"\u2019s reading is the only one assigned to you.","What "+m.t+" is really building is not knowledge of "+m.c+" but reflexes of it, and reflexes are trained, not downloaded.","By Day "+d+" the novelty has usually worn off, which is excellent news; what remains after novelty is the actual material.","There is a version of you on the far side of "+m.t+" who is very glad you did not stop here.","The Word you just read will keep working after you close it; Scripture has never needed us watching to grow something.","In a season built around "+m.c+", the small days are the load-bearing ones, and today was one of them."]);
  var c2=pk(r,["That is how ordinary people end up with unrecognizable lives: not by leaps, but by days like Day "+d+".","Keep a one-line log of what God says through "+m.t+"; by the last day it will be worth more than anything else you own from this season.","Encourage one person a few days behind you in "+m.t+"; steadying someone else is the fastest way to steady yourself.","Let tonight\u2019s smallest act of "+m.c+" count, because it does.","Repetition in the direction of "+m.c+" is the whole secret, and you are in it.","What feels like a small day now will look like a hinge from ten years out.","You are being formed at walking speed, which is the only speed formation trusts.","Hold the line of "+m.c+" one more day; lines held daily become a life.","Tomorrow will borrow whatever steadiness you bank tonight.","Day "+d+" held. That sentence, repeated enough times, is a testimony.","The ledger of "+m.t+" only ever asks one entry: present.","Somewhere ahead, a harder day is already grateful for the "+m.c+" you practiced on an easy one."]);
  return a+" "+b+" "+c2;
}'''
s = s[:old.start()] + new + s[old.end():]

# ---- gStory: adverbial prefix + occasional who-echo on the payoff sentence ----
old = 'var who=pk(r,VX_PEOPLE), where=pk(r,VX_PLACE), span=pk(r,VX_TIMEBOX);'
assert old in s
s = s.replace(old, old + '\n  var adv=pk(r,["","","Years on, ","To this day, ","Even now, ","Ask around and you hear it plainly: ","Looking back, "]);')
# apply adv to each frame's terminal sentence variable
s = s.replace('return "There is "+who+" who "+prac+" "+span+", usually "+where+". "+pay;',
              'return "There is "+who+" who "+prac+" "+span+", usually "+where+". "+adv+pay.charAt(0).toLowerCase()===adv?adv+pay:adv+(adv?pay.charAt(0).toLowerCase()+pay.slice(1):pay);')
# ^ too clever; fix simply below with helper
s = s.replace('function gStory(r){',
'''function advJoin(adv,x){ return adv? adv + x.charAt(0).toLowerCase()+x.slice(1) : x; }
function gStory(r){''')
s = s.replace('return "There is "+who+" who "+prac+" "+span+", usually "+where+". "+adv+pay.charAt(0).toLowerCase()===adv?adv+pay:adv+(adv?pay.charAt(0).toLowerCase()+pay.slice(1):pay);',
              'return "There is "+who+" who "+prac+" "+span+", usually "+where+". "+advJoin(adv,pay);')
s = s.replace('return "In one small group, "+who+" "+act+". "+res;',
              'return "In one small group, "+who+" "+act+". "+advJoin(adv,res);')
s = s.replace('return "One household keeps "+seed+". "+use;',
              'return "One household keeps "+seed+". "+advJoin(adv,use);')
s = s.replace('return "After "+turn+", "+who+" "+kept+". "+wit;',
              'return "After "+turn+", "+who+" "+kept+". "+advJoin(adv,wit);')
s = s.replace('return "One week, "+who+" "+small+". "+after;',
              'return "One week, "+who+" "+small+". "+advJoin(adv,after);')
s = s.replace('return "There was "+who+" who "+quiet+". "+reveal;',
              'return "There was "+who+" who "+quiet+". "+advJoin(adv,reveal);')

# ---- gStoryMoral: composed bridge appended to story ~always (adds length + unique sentence) ----
ins_after = s.index('function gApply(r,m){')
moral = r'''function gStoryMoral(r,m){
  var lead=pk(r,["That is what "+m.c+" looks like off the page.","File that under "+m.c+" with skin on.","Stories like that are "+m.c+" in work clothes.","Nothing in that story required talent; all of it required "+m.c+".","That is the shape "+m.c+" tends to take in real houses.","Multiply that by a congregation and you can feel where "+m.t+" is headed.","No stage, no spotlight; just "+m.c+" doing what it does.","Somewhere in that story is a door with your name on it."]);
  var tail=pk(r,[""," Yours will look different, and that is the point."," The ingredients are all within reach of an ordinary week."," Small is not the opposite of significant; hidden is not the opposite of real."," The same Spirit is available at your address."," Borrow the pattern; God supplies the rest."," It cost less than expected and paid more."]);
  return lead+tail;
}
'''
s = s[:ins_after] + moral + s[ins_after:]

# route: story := gStory + moral
old = 'var story=gStory(rB);'
assert old in s
s = s.replace(old, 'var story=gStory(rB)+" "+gStoryMoral(rB,map);')

# ---- gClose tails: infuse m.c / day into agnostic tails ----
old = '"Never underestimate what He does with people who keep showing up.","Rest is also an act of trust.","Stack enough days this size and you get a different life.","He is not grading; He is growing something.","Showing up is most of the miracle."'
assert old in s
s = s.replace(old, '"Never underestimate what He does with people who keep showing up.","Rest, too, is an act of "+m.c+".","Stack enough days this size and you get a different life.","He is not grading Day "+d+"; He is growing something through it.","Showing up is most of the miracle.","In the economy of "+m.c+", present beats impressive."')
old = '"Graded days breed anxiety; offered days breed peace.","Water it with a little trust and go to sleep.","God works in journeys, and you are in one.","Sleep is a nightly rehearsal of trust; take the rehearsal.","Tomorrow inherits whatever you plant tonight."'
assert old in s
s = s.replace(old, '"Graded days breed anxiety; offered days breed peace.","Water Day "+d+" with a little trust and go to sleep.","God works in journeys, and "+m.t+" is one.","Sleep is a nightly rehearsal of trust; take the rehearsal.","Tomorrow inherits whatever "+m.c+" you plant tonight."')
old = '"Sting fades; fruit stays.","Trust the underground season; spring keeps its appointments.","That is not pressure; that is a promise.","Depth is being added where you cannot see it yet.","The harvest never asks how the planting felt."'
assert old in s
s = s.replace(old, '"Sting fades; the fruit of "+m.c+" stays.","Trust the underground season; spring keeps its appointments.","That is not pressure; that is a promise.","Depth in "+m.c+" is being added where you cannot see it yet.","The harvest never asks how Day "+d+"\u2019s planting felt."')

# ---- gRead why bank: widen + infuse ----
old = '" The Word does its deepest work on readers who are not rushing.",\n   " God has been known to hide a whole week\\u2019s help in a few verses.",'
assert old in s
s = s.replace(old, '" The Word does its deepest work on readers who are not rushing.",\n   " God has been known to hide a whole week\\u2019s help in a few verses.",\n   " Read it as a page of "+m.t+", written for exactly this stretch.",\n   " Somewhere in it is the day\\u2019s word on "+m.c+"; stay until you find it.",')

# ---- gApply agnostic tails: two get m.c ----
old = '"Faithfulness compounds faster than brilliance.","Ten humble minutes beat one heroic intention."'
assert old in s
s = s.replace(old, '"Faithfulness compounds faster than brilliance.","Ten humble minutes of "+m.c+" beat one heroic intention.","Little, done today, outruns much, planned for someday."')

# ---- reduce gDeeper firing: body slightly longer via second truth already? add threshold ease 380->360 ----
old = 'if(wcount<380) bodyHtml+="<p>"+gDeeper(rB,map,d)+"</p>";'
assert old in s
s = s.replace(old, 'if(wcount<360) bodyHtml+="<p>"+gDeeper(rB,map,d)+"</p>";')

open('/home/claude/site/engine.js','w').write(s)
print("v3 token-infusion applied")
