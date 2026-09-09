# -*- coding: utf-8 -*-

THESIS = ("The number one small group in any church is the weekly staff meeting. It is the only group that meets "
 "fifty times a year, sets the culture everyone else copies, and is almost never designed. Most churches run it as "
 "a status report and then wonder why the staff is not formed, aligned or close.")

WHY = [
 ["It meets more than any other group","Fifty-plus times a year. No small group in your church gets that much time with the same people."],
 ["It sets the culture everyone copies","However this room handles disagreement, honesty and honour is how every ministry under it will."],
 ["It is the only group where all the leaders are","Whatever forms this room reaches the whole church within a year."],
 ["It is almost never designed","Agendas are built for information. Formation happens by accident or not at all."],
 ["The staff are the least pastored people in the church","Everyone here cares for others. Almost nobody here is being cared for."],
]

STRUCTURE = [
 ["The first 20 minutes","Formation","One session from the library. Conversation, not teaching. This goes first or it never happens."],
 ["The middle 30 minutes","Alignment","Decisions, dependencies and what each area needs from the others. Not status — status is an email."],
 ["The last 10 minutes","Action","Who owns what by when, said out loud, written down, reviewed next week."],
]

STRUCTURE_NOTE = ("Formation first is the whole discipline. Every staff meeting that puts business first and formation "
 "last is a staff meeting where formation never happens, because business always expands to fill the hour.")

LEADER_Q = [
 ["Does your staff meeting have a formation segment every week?",["Every week","Most weeks","Occasionally","Never"]],
 ["Does formation come first or last in the agenda?",["First","Middle","Last","Not on it"]],
 ["Could a staff member disagree with you in the meeting?",["Regularly happens","Occasionally","Rarely","Never has"]],
 ["Do you know what each staff member is carrying personally?",["All of them","Most","A few","No"]],
 ["Does anyone besides you ever lead the meeting?",["Regularly","Sometimes","Rarely","Never"]],
 ["Do decisions from the meeting get written down and reviewed?",["Always","Usually","Sometimes","No"]],
 ["Would your staff say this meeting is worth their time?",["Confident yes","Probably","Not sure","Probably not"]],
 ["Has anyone said something hard in this room in the last quarter?",["Yes, more than once","Once","No","I cannot remember"]],
 ["Do you prepare the formation segment, or improvise it?",["Prepared","Loosely planned","Improvised","There is none"]],
 ["Is there a plan for the next twelve months of this meeting?",["Yes, on a calendar","A rough idea","No","Never considered it"]],
]

LEADER_BANDS = [
 ["10 to 16","A status meeting","This is an information exchange, and information exchange can be an email. Start with one twenty-minute session a week, placed first. Nothing else changes yet."],
 ["17 to 24","A working meeting","Business runs well and formation is occasional. Put the formation segment first for one quarter and protect it even when the agenda is full."],
 ["25 to 32","A forming team","Most of it is working. The gaps are usually rotation — someone other than the leader should be running sessions — and a plan beyond next week."],
 ["33 to 40","The best small group in the church","Rare. The next frontier is whether it survives you: could someone else run this if you left, using what is written down?"],
]

STAFF_SURVEY = {
 "why":"Run this once a year with the whole staff, anonymously. The results build next year's calendar. A leader choosing all fifty-two sessions alone will choose fifty-two sessions about the things the leader is already thinking about.",
 "rules":["Anonymous, genuinely — use a form nobody on staff administers",
          "Ten minutes maximum or you will get thin answers",
          "Publish the results to the whole staff before building the calendar",
          "Build at least half the year from what they asked for",
          "Say out loud which requests you are not doing and why"],
 "qs":[["Which categories would help you most this year?","multi",
        ["Vision & Direction","Team Health & Trust","Character & Integrity","Spiritual Formation",
         "Leadership Craft","Strategy & Execution","People & Recruiting","Communication & Conflict",
         "Seasons & Pressure","Multiplication & Legacy"]],
       ["How is your own soul right now?","single",["Full","Steady","Running low","Empty"]],
       ["What do you most need from this team?",'single',
        ["Clarity about direction","Honest conversation","Practical training","Prayer and care","Time back"]],
       ["How safe is it to disagree in our staff meeting?","single",["Completely","Mostly","Somewhat","Not safe"]],
       ["What skill would most change your effectiveness?","single",
        ["Delegation","Hard conversations","Recruiting","Planning","Preaching or teaching","Managing my time"]],
       ["What is the one thing we never talk about that we should?","open",[]],
       ["What would make this meeting more valuable to you?","open",[]],
       ["Who on this team should lead a session, and on what?","open",[]]],
}

# 52-week calendar seed — timely anchored to the church year, timeless rotating
CAL52 = [
 ["January","Timely","New year, new plan",["Say It in One Sentence","Here Is the Plan","Ninety Days","Rule of Life"]],
 ["February","Timeless","The long grind",["The Long Grind","Running on Empty","Trust Is Built in Small Moments","Reading for Yourself"]],
 ["March","Timely","Toward Easter",["Before Christmas is behind us; prepare Easter now","Prayer Beyond the Meeting","Recruiting Season","One Message, Seven Ways"]],
 ["April","Timely","Easter and after",["After Easter","Celebrating","The Person Nobody Thanks","Gratitude"]],
 ["May","Timeless","People and margin",["Delegate or Drown","Time","Your Family Is Watching","Sabbath"]],
 ["June","Timely","Plan the fall",["Fall Launch","The Annual Calendar","Who Is Missing","Apprentices"]],
 ["July","Timely","Summer rhythm",["The Summer Slump","Solitude","Simplify","Saying No"]],
 ["August","Timely","Launch readiness",["Resourcing Reality","The Personal Ask","The First Ninety Days","Announce Less"]],
 ["September","Timely","Fall in motion",["The One Thing","Running a Meeting People Do Not Dread","Screening Without Insulting","Repair Fast"]],
 ["October","Timely","Budget season",["Budget Season","What Gets Measured","What We Are Not Doing","Money, Honestly"]],
 ["November","Timely","Gratitude and December prep",["Before Christmas","Gratitude","The Person Nobody Thanks","Report Honestly"]],
 ["December","Timely","Carry the season",["Abide","The Long Grind","Celebrating","Hand It On"]],
]

CAL_RULES = [
 ["Twelve timely, forty timeless","The twelve tied to the church calendar are fixed. The other forty rotate by need."],
 ["One category per month, roughly","Coherence beats variety. A month on team health does more than four unrelated sessions."],
 ["Somebody else leads at least a third","If the senior leader runs every session, it is a class rather than a team practice."],
 ["Leave four weeks empty","Crises, guests and the weeks that get cancelled. A full calendar guarantees failure by March."],
 ["Repeat the best ones","A session that worked can run again in eighteen months with a different team and land harder."],
 ["Never run high-trust sessions early","Character, Team Health and Multiplication sessions need a year of shared history first."],
]

RETREAT = {
 "why":"Four one-day retreats a year does more than one three-day retreat, because the quarterly rhythm matches how work actually moves. Same format each time so nobody has to reinvent it.",
 "shape":[
  ["8:30","Arrive and eat","30 min","No agenda. People need to arrive before they can think. Do not start early to be efficient."],
  ["9:00","Look back honestly","60 min","What happened last quarter — what worked, what did not, what we learned. The leader names a failure first."],
  ["10:00","One formation session","60 min","A longer version of a library session, from the category the staff survey asked for."],
  ["11:00","Break, properly","20 min","Outside if possible. Not a working break."],
  ["11:20","The one question","70 min","A single strategic question for the quarter ahead, decided in the room. Not five questions."],
  ["12:30","Lunch together","60 min","No business. This is the relational hour and it is not optional."],
  ["13:30","Build the quarter","90 min","Each person writes their team plan and personal plan. Silent work, then pairs, then the room."],
  ["15:00","Commit out loud","45 min","Each person names one team outcome and one personal commitment with a date."],
  ["15:45","Pray for each other","30 min","By name, out loud, for the specific thing they just named."],
  ["16:15","End early","","Ending early is a gift and it teaches that we finish what we start."],
 ],
 "rules":["Off site, phones in a basket","Nobody presents a report","One decision, not a list",
          "The leader talks least","Everyone leaves with a written plan","End early, always"],
}

TOOLBOX = [
 ["Weekly agenda template","The 20/30/10 structure with the formation slot pre-placed first"],
 ["Session leader card","One page a staff member can run a session from with no preparation"],
 ["Annual calendar grid","Fifty-two weeks with the twelve timely anchors fixed"],
 ["Staff survey form","The eight questions, formatted for anonymous collection"],
 ["Leader self-assessment","The ten-question meeting health check with bands"],
 ["Quarterly retreat run sheet","The one-day shape with timings"],
 ["Decision log","What was decided, who owns it, by when, reviewed weekly"],
 ["Rotation schedule","Who leads which session across the year"],
 ["New staff onboarding brief","How this meeting works, given to every new hire"],
 ["Year-end review sheet","What formed us, what we would repeat, what we would drop"],
]

JOURNEYS = [
 ["The First Ninety Days","12 sessions","A new senior leader's first quarter of staff meetings. Trust and clarity before anything else.",
  ["Say It in One Sentence","The Meeting After the Meeting","Trust Is Built in Small Moments","Whose Vision Is It",
   "One Team, Not Six Departments","Listening","Time","Delegate or Drown","Who Is Missing","Assume the Best",
   "Here Is the Plan","Ninety Days"]],
 ["Rebuilding a Broken Team","12 sessions","After conflict, a departure or a failure. Slow, and in this order.",
  ["Assume the Best","When Somebody Leaves","The Meeting After the Meeting","Repair Fast","Disagree Without Damage",
   "Gossip","What You Tolerate","When You Were Wrong","Trust Is Built in Small Moments","The Person Nobody Thanks",
   "One Team, Not Six Departments","Celebrating"]],
 ["The Formation Year","12 sessions","A year on the leader's own soul. Best run as every-other-week.",
  ["Running on Empty","Reading for Yourself","Prayer Beyond the Meeting","Solitude","Sabbath","Confession",
   "Fasting","Gratitude","The Dark Stretch","The Private Life","Rule of Life","Abide"]],
 ["Getting Aligned","12 sessions","For a staff pulling in different directions. Vision and strategy together.",
  ["Say It in One Sentence","Whose Vision Is It","A Preferred Future","The One Thing","What We Are Not Doing",
   "What Gets Measured","The Annual Calendar","Saying No","Resourcing Reality","Why It Stalled","Ninety Days","Here Is the Plan"]],
 ["Building the Bench","12 sessions","When the constraint is leadership production rather than ideas.",
  ["Who Is Missing","The Personal Ask","Apprentices","Developing Rather Than Using","Why They Leave",
   "The First Ninety Days","Delegate or Drown","Giving Feedback","The Difficult Volunteer","Four Generations",
   "Raising Your Replacement","Give Them Away"]],
 ["Surviving a Hard Season","12 sessions","Shortfall, decline, crisis or exhaustion. Care before strategy.",
  ["Burnout","Running on Empty","The Long Grind","When Giving Drops","A Crisis in the Church","The Dark Stretch",
   "Who Pastors the Pastor","Your Family Is Watching","Assume the Best","Report Honestly","Celebrating","Abide"]],
]
