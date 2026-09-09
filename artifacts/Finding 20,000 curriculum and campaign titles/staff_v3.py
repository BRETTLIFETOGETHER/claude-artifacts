# -*- coding: utf-8 -*-

# ===== EVERY MODULE IS A 30-DAY / 4-WEEK CONVERSATION =====
WEEK_SHAPE = [
 ["Week 1","The conversation","Open it with a question, not a lecture. Nobody changes because they were informed.",
  ["A conversation prompt the group answers before any content","One short reading or video, under twelve minutes",
   "The honest self-assessment: where am I on this right now?","One person shares an experience of getting this wrong"]],
 ["Week 2","The practice","Do the thing in the actual job this week. Not a case study, not a simulation.",
  ["A defined practice assignment inside the real role","A short how-to reference for the week",
   "Two peers check in midweek with three words or fewer","Bring back what actually happened"]],
 ["Week 3","The obstacle","Every competency has a predictable place people get stuck. Name it and work it.",
  ["The named obstacle for this module, described plainly","What most people try first and why it fails",
   "Two workable approaches and when each applies","Group problem-solving on one real stuck situation"]],
 ["Week 4","The commitment","End on something that persists after the module closes.",
  ["What will be different in ninety days","One written commitment with a date",
   "Who will ask you about it, by name","Add the artifact to the competency portfolio"]],
]

WEEK_NOTE = ("Four weeks, thirty days, one competency. Conversational rather than instructional, because a staff member "
 "who is told something forgets it and a staff member who has to answer for it does not. Sessions run 45 to 60 minutes "
 "in a cohort or 20 to 30 minutes self-paced, and the practice assignment is the same either way.")

CONVO_RULES = [
 ["Question before content","The first ten minutes are their experience, not our material. Content lands on ground that has been opened."],
 ["Nobody teaches the whole hour","If one voice runs more than a third of the session, it stopped being a conversation."],
 ["Count to fifteen","After a real question, wait. The first answer is the polite one; the second is the true one."],
 ["Bring the actual job","Every session works on something happening this week in a real church, never a hypothetical."],
 ["The leader goes first on failure","Whoever facilitates names their own mistake before asking anyone else to."],
 ["End with a date","No session closes without something written down and a day attached to it."],
]

# ===== CRAWL / WALK / RUN =====
CWR_FRAME = [
 ["Crawl","First 90 days","Survive, learn and finish one thing. Nothing here is impressive and all of it is necessary."],
 ["Walk","Months 4 to 12","Own the role without supervision. Systems, a first team, and a written plan for the year."],
 ["Run","Year 2 and beyond","Lead beyond yourself. Develop leaders, document what you built, and produce your successor."],
]

# Per-role crawl/walk/run goals: {role_id: [[3 crawl],[3 walk],[3 run]]}
CWR = {
"senior":[["Preach twelve consecutive weeks","Meet the twelve most influential members","Write a one-page assessment of what you found"],
 ["Publish a twelve-month preaching calendar","Get one written direction the elders can repeat","Lead a staff or leader team meeting weekly"],
 ["Develop and release two leaders","Run a churchwide formation season","Name a succession plan on paper"]],
"exec":[["Read three years of financials","Meet every staff member individually","Document one broken process end to end"],
 ["Deliver an annual operating plan and budget","Run a structured hiring process once","Establish a five-number board dashboard"],
 ["Restructure one area of the organization","Build a two-deep bench in every seat","Coach another executive leader"]],
"worship":[["Lead four services and review each","Learn every current volunteer's name and role","Fix one thing about rehearsal"],
 ["Build a rotating team of twelve","Design a full service, not just a set","Plan one full season of worship"],
 ["Raise three worship leaders who lead without you","Run the department on a budget","Build a residency or apprentice track"]],
"groups":[["Attend every existing group once","Launch ten groups","Train six hosts in ninety minutes"],
 ["Run a churchwide launch","Place new people inside three weeks","Coach every leader weekly for a term"],
 ["Build the coach layer above the leaders","Write one curriculum from your own preaching","Multiply groups without splitting friendships"]],
"kids":[["Complete safeguarding certification","Audit ratios, check-in and rooms","Recruit a team of ten"],
 ["Align curriculum to the church's big idea","Build one milestone pathway","Survey and respond to twenty parents"],
 ["Develop coordinators who run their own areas","Write and run a crisis protocol","Train children's leaders beyond your church"]],
"students":[["Run a weekly gathering for a term","Recruit six adult leaders","Meet twenty parents"],
 ["Build student small groups","Design a retreat with follow-through","Launch a parent track"],
 ["Develop six student leaders","Send students on mission","Build the senior-year launch"]],
"elder":[["Attend six meetings and say little","Read the governing documents and last three budgets","Pray for the congregation by name"],
 ["Write one doctrinal position paper","Mediate one conflict","Participate fully in an annual pastor review"],
 ["Chair a board or committee","Mentor two newer elders","Lead through one governance crisis"]],
"finance":[["Produce three months of clean financials","Implement two-person counting","Learn the housing allowance rules"],
 ["Build a budget from ministry plans","Write a reserve policy","Deliver a board report anyone can read"],
 ["Pass an external audit","Lead a capital project's finances","Train another church administrator"]],
"steward":[["Analyze three years of giving by household","Fix first-gift follow-up","Teach on money once"],
 ["Publish an annual generosity calendar","Run one financial discipleship class","Report impact without asking"],
 ["Lead a capital campaign","Start the legacy conversation","Build advisor partnerships"]],
"marriage":[["Take six couples through premarital","Build a referral list of three counsellors","Run one enrichment event"],
 ["Train eight mentor couples","Launch a parenting track","Design a marriage retreat"],
 ["Write a restoration protocol","Multiply to twenty mentor couples","Train marriage leaders elsewhere"]],
"men":[["Launch one group of eight","Sustain it six months","Learn why men are missing here"],
 ["Run a retreat with follow-through","Multiply to four groups","Build a service project rhythm"],
 ["Build a discipleship pathway","Raise twelve leaders","Reach unchurched men measurably"]],
"women":[["Lead one study of twelve","Reach three life stages","Create a room where women tell the truth"],
 ["Run a retreat","Form ten mentor pairs","Build a care network"],
 ["Build a full pathway","Raise twelve leaders","Train directors beyond your church"]],
"missions":[["Establish one local partnership","Lead one short-term team","Learn your city honestly"],
 ["Write a global strategy with focus","Care well for three sent workers","Prepare and debrief teams properly"],
 ["Send a planter or worker","Build indigenous leadership","Adopt an unreached people group"]],
"care":[["Complete twenty visits","Build a referral list","Learn what never to say"],
 ["Build a care team of twelve","Lead six funerals","Launch one support group"],
 ["Write a trauma and disclosure protocol","Build coverage that survives your absence","Partner with licensed clinicians"]],
"disciple":[["Map the current pathway honestly","Teach one class","Name the biggest formation gap"],
 ["Design a full pathway with visible steps","Run four core classes","Build an assessment"],
 ["Align the whole church to one strategy","Write original curriculum","Build the leader pipeline"]],
"connect":[["Audit the guest experience with fresh eyes","Fix follow-up inside forty-eight hours","Train the greeter team"],
 ["Build the assimilation pathway","Track retention for six months","Place people into groups in three weeks"],
 ["Improve retention measurably","Build multi-service consistency","Audit another church"]],
"comms":[["Run twelve weeks of clean weekend media","Write a one-page brand guide","Cut the announcement list in half"],
 ["Build a communication calendar","Rebuild the digital front door","Write a crisis communication plan"],
 ["Communicate a churchwide campaign end to end","Develop volunteer creatives","Build brand architecture"]],
"volunteer":[["Place twenty volunteers","Implement screening","Write role descriptions for every job"],
 ["Build the serving pathway","Run a ministry fair","Get onboarding inside three weeks"],
 ["Build a team-leader pipeline","Sustain ninety percent coverage","Train serving directors elsewhere"]],
"campus":[["Lead twelve weekends","Build the volunteer team","Be the pastor of that room"],
 ["Develop campus staff","Establish one local partnership","Report campus health honestly"],
 ["Launch a campus","Develop your successor","Lead peer campus pastors"]],
"ops":[["Establish a maintenance schedule","Run twelve events cleanly","Learn the building"],
 ["Build preventive maintenance","Train a security team","Write an emergency plan"],
 ["Manage a building project","Set multisite standards","Master-plan the campus"]],
}

# ===== MISSION / VISION / VALUES PER ROLE =====
MVV = {
"senior":["To feed, lead and guard this congregation so that people are formed into the likeness of Christ.",
 "A church where the whole congregation is being formed, not merely gathered — and where more leaders leave than arrive.",
 ["The Word is preached faithfully, not cleverly","People matter more than the platform","We develop leaders rather than recruit helpers","Nothing is announced that the elders have not already owned","The pastor's household is not sacrificed to the church"]],
"exec":["To convert vision into systems, staffing and budget so that ministry actually happens.",
 "A church where nothing important depends on one person's memory, and where the plan survives a departure.",
 ["Clarity is kindness","Roles before people, people before money","Write it down or it does not exist","Decisions have owners and dates","We build capacity, not heroics"]],
"worship":["To lead this congregation in worshipping God together, and to build the team that carries it every week.",
 "A room where the congregation is singing rather than watching, led by a team that is being discipled as it serves.",
 ["The congregation is the choir","What we sing is what they will believe in ten years","Rehearsal is discipleship","Excellence serves worship; it never replaces it","We raise leaders and give the platform away"]],
"groups":["To move people out of rows and into circles where they are known, cared for and formed.",
 "A church where every person who wants to be known is known, and every group is producing its next leader.",
 ["Host, do not teach","Finite commitments get real yeses","Care happens in the circle, not the office","Every group names its apprentice in week one","Nobody is placed and forgotten"]],
"kids":["To form the youngest disciples well and to equip the parents who do the daily work.",
 "Children who own a faith of their own, in a ministry parents trust completely with what they love most.",
 ["Safety is not negotiable","Parents are the primary disciplers","Consistency beats novelty","Every child is known by name","This is not childcare"]],
"students":["To walk with teenagers through the years that decide whether the faith becomes theirs.",
 "Students who arrive at twenty-two still following, with five adults who never stopped showing up.",
 ["Doubt is welcome here","Consistency beats charisma","Presence outside the building matters most","We give students real responsibility","Parents are partners, not customers"]],
"elder":["To shepherd, govern and guard the doctrine and direction of this church.",
 "A board that shepherds rather than manages, and that hands on a healthier church than it received.",
 ["We are shepherds before we are directors","What is said here stays here","We support the pastor and hold him accountable — both","Doctrine is guarded, not debated annually","We decide slowly and communicate clearly"]],
"finance":["To steward the money, the buildings and the compliance so that ministry is never limited by disorder.",
 "A church whose finances would survive any audit and whose congregation trusts the numbers completely.",
 ["Two sets of eyes on everything","Transparency builds trust","Preventive beats reactive","Every number has a name behind it","We serve ministry; we do not govern it"]],
"steward":["To form generous disciples and fund the mission without ever manipulating anyone.",
 "A congregation whose generosity is a discipleship outcome, and whose giving is the by-product rather than the goal.",
 ["Teach before you ask","Participation matters more than amount","No one is a revenue line","We report impact and ask for nothing that day","God owns it all — that is the premise, not the conclusion"]],
"marriage":["To strengthen the households this church is actually made of.",
 "Marriages that make it, households that are safe, and mentor couples multiplying faster than crises arrive.",
 ["Prevention costs less than restoration","We know our limits and refer early","Every season of household is welcome here","Confidentiality is absolute","Couples are discipled by couples"]],
"men":["To call men into faith, brotherhood and responsibility.",
 "Men who are followed by their sons, trusted by their wives, and shoulder to shoulder with other men.",
 ["Shoulder to shoulder, not face to face","Task before talk","Finite asks, real commitments","No shame, no performance","Every group produces the next leader"]],
"women":["To build a community where women are discipled, known and deployed.",
 "Women of every season formed in Scripture, mentored across generations, and leading with confidence.",
 ["Formation, not decoration","Every season belongs — single, married, mothering, widowed","Safety before depth","Older and younger together, deliberately","We teach the Bible seriously"]],
"missions":["To send this church outward — into the city and to the nations.",
 "A church known in its own city and multiplying beyond it, sending its best rather than its spare.",
 ["Partnership over paternalism","Depth over breadth","We send our best on purpose","Indigenous leadership is the goal","Local and global are one assignment"]],
"care":["To carry people through the worst weeks of their lives.",
 "A congregation where nobody suffers alone and the church is still present after everyone else has gone.",
 ["Presence before answers","We stay after the casseroles stop","We know our limits and refer without shame","Confidentiality is care","The caregivers are cared for too"]],
"disciple":["To own the answer to how a person actually grows in this church.",
 "A visible pathway from first visit to leading, that every member could describe in one sentence.",
 ["Formation over programming","One pathway, not twelve options","Every step names the next step","We measure transformation, not attendance","Depth is respect"]],
"connect":["To make sure the person who visited once comes back and belongs.",
 "A church where no guest sits alone, and where belonging takes weeks rather than years.",
 ["The first ninety seconds decide","Follow up in forty-eight hours","Connect people to people, not to programmes","Nobody is a number in a system","The second visit is the one that matters"]],
"comms":["To make sure the right message reaches the right people in time to act.",
 "A church that says less and is heard more, in one voice everyone recognises.",
 ["Announce less, better","Clarity over cleverness","One church, one voice","Stories beat announcements","The website is the front door"]],
"volunteer":["To turn attenders into servants and to keep them from burning out.",
 "A church where serving is the normal experience of membership and every team produces its own leaders.",
 ["Serving is discipleship, not staffing","Finite asks, defined roles","Onboard in three weeks or lose them","Honour specifically and publicly","Sustainable beats maximum"]],
"campus":["To lead one location of this church with local depth and full alignment.",
 "A campus that is a full church in its neighbourhood, not a viewing room for someone else's service.",
 ["Carry the vision faithfully","Be the pastor of this room","Local ministry, aligned direction","Communicate up honestly","Raise the next campus pastor here"]],
"ops":["To keep the building, the systems and the logistics working invisibly.",
 "A facility that serves ministry so well that nobody notices it, and systems that never fail on a Sunday.",
 ["Invisible is the standard","Preventive over reactive","Checklists over heroics","Safety is ministry","The building serves the mission"]],
}

# ===== QUARTERLY PLANNER =====
PLANNER_TEAM = [
 ["The one outcome","What will be different for the people we serve in ninety days? One sentence, one outcome."],
 ["The three priorities","Everything the team will work on. If there is a fourth, name what it displaces."],
 ["Who owns what","Every priority has one name and one date. Shared ownership is no ownership."],
 ["What we are not doing","Written down and communicated. The un-doing list is what makes the doing list possible."],
 ["The people plan","Who joins the team, who moves up, who needs a harder assignment, who needs rest."],
 ["The budget line","What this quarter costs and whether it is approved. Plans without money are wishes."],
 ["The evidence","What will exist at the end that does not exist now, that somebody else could look at."],
 ["The review date","On the calendar, with a named person, before the quarter starts."],
]

PLANNER_PERSONAL = [
 ["My one competency","One thing from the level map I am working on this quarter. Not three."],
 ["My practice","What I will do differently in the actual job, weekly, to build it."],
 ["What I am giving away","One thing I currently do that somebody else will own by the end of the quarter."],
 ["My hard conversation","The one I have been avoiding, with a date attached."],
 ["My learning","One book, one course, one person to sit under. Choose one, not a list."],
 ["My rhythms","Sabbath, sleep, exercise, prayer, family. Written down or it does not survive a busy quarter."],
 ["My margin","What I will say no to this quarter to protect the above."],
 ["Who is asking me","The name of the person who will ask about all of this in ninety days."],
]

PLANNER_PROFILE = ("The planner is generated from the profile: your level sets which competency options appear, "
 "church size sets realistic scope, stage sets urgency, and your assessment results shape how the personal plan "
 "is framed. A strengths-oriented leader gets different language from a detail-oriented one, and the plan is the same plan.")

# ===== ASSESSMENTS =====
ASSESS_INHOUSE = [
 ["Role Readiness","10 questions, 4 minutes","Where you sit against the competency map for your current level. Produces your Foundation-to-Expert placement."],
 ["Capacity & Margin","8 questions, 3 minutes","Hours, energy, and what is actually sustainable. Most staff plans fail on capacity rather than commitment."],
 ["Team Health","12 questions, 5 minutes","Clarity, trust, conflict and results across the team you lead. Take it yourself, then have the team take it."],
 ["Volunteer Pipeline","8 questions, 3 minutes","Recruitment, onboarding, retention and multiplication in your ministry."],
 ["Ministry Stage","6 questions, 2 minutes","Whether this ministry is starting, building, running or plateaued — which changes the whole plan."],
 ["Spiritual Rhythms","10 questions, 4 minutes","Private, never reported to a supervisor. For your own eyes and your coach's if you choose."],
]

ASSESS_THIRD = [
 ["CliftonStrengths","Gallup","34 talent themes; most people use the top five.","Useful for placement and for language about what energises someone.",
  ["Top 5 themes","All 34 ranked","Domain balance"]],
 ["Myers-Briggs / MBTI","The Myers-Briggs Company","Four-letter type across four dichotomies.","Common in church staff culture and useful as shared vocabulary.",
  ["Four-letter type","Which letters are borderline","Date taken"]],
 ["Enneagram","Various publishers","Nine types with wings, stress and growth arrows.","Widely used in ministry for self-awareness and motive rather than behaviour.",
  ["Type and wing","Stress and growth numbers","Instrument used"]],
 ["DiSC","Various publishers","Four behavioural styles, work-oriented.","Practical for team communication and conflict.",
  ["Primary and secondary style","Profile pattern"]],
 ["Working Genius","Table Group","Six types of work someone finds energising or draining.","The most operationally useful of the set for assigning actual tasks.",
  ["Two geniuses","Two competencies","Two frustrations"]],
 ["Spiritual Gifts","Denominational or church instrument","Gifts inventory per your tradition.","Should be your own church's instrument, not a generic one.",
  ["Top three gifts","Instrument used","Confirmed by others"]],
]

ASSESS_HONEST = ("A word before anyone builds a staffing decision on these. CliftonStrengths, DiSC and Working Genius "
 "have reasonable evidence behind them for what they claim &mdash; language and self-awareness. MBTI and the Enneagram "
 "have weak psychometric support: MBTI's type categories are not stable on retest for a large share of people, and the "
 "Enneagram has almost no validation as a measurement instrument, whatever its pastoral usefulness. "
 "Use all of them for vocabulary, self-awareness and conversation. Do not use any of them to hire, fire, promote or "
 "assign a role. For those decisions the better instruments are structured work samples, 360 feedback from people who "
 "have actually worked with the person, and reference calls with specific questions.")

ASSESS_USE = [
 ["Take it or enter it","Most staff already know their results. Enter what you have, take what you do not, and skip whatever your church does not use."],
 ["It informs the plan, not the verdict","Results shape how the quarterly personal plan is worded and which development options surface first."],
 ["Shared with the team, by choice","A team page shows the composite so people understand each other. Anyone can decline to publish theirs."],
 ["Never in a personnel file","These are development tools. The moment results are used in an evaluation, people start answering strategically and the instrument is finished."],
 ["Retake every two years","Roles change people. A five-year-old result describes someone who no longer exists."],
]
