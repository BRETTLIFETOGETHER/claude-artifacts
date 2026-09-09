# -*- coding: utf-8 -*-
import json, re

def grab(path, name):
    s = open(path, encoding="utf-8").read()
    m = re.search(r"^var " + name + r" = (.*);$", s, re.M)
    return json.loads(m.group(1))

LIB = "/mnt/user-data/outputs/can-library-clickable.html"
WS  = "/mnt/user-data/outputs/can-family-workspace.html"
PRO = "/mnt/user-data/outputs/can-professional-edition.html"

ALL = grab(LIB, "ENTRIES")
CATS = grab(LIB, "CATS")
GROUPS = grab(LIB, "GROUPS")
JOURNEYS = [e for e in ALL if e["kind"] == "journey"]
TOOLS125 = [e for e in ALL if e["kind"] == "tool"]

TEMPLATES = grab(WS, "TEMPLATES")
INSTRUMENTS = grab(WS, "INSTRUMENTS")

ROLES = grab(PRO, "ROLES")
ASSESSMENTS = grab(PRO, "ASSESSMENTS")
MATTERS = grab(PRO, "MATTERS")
RHYTHM = grab(PRO, "RHYTHM")

ENGINES = [
 ("home",        "Home",        "0", "The platform",              "One family, one profile, seven engines."),
 ("know",        "Know",        "1", "Family Intelligence",       "Know the family before you advise the family."),
 ("prescribe",   "Prescribe",   "2", "Stewardship Prescription",  "Recommend the right conversation at the right time."),
 ("personalize", "Personalize", "3", "Personalization & Publishing", "Make every resource feel written for this family."),
 ("prepare",     "Prepare",     "4", "Advisor Intelligence",      "Remember more, prepare better, relate more deeply."),
 ("experience",  "Experience",  "5", "Family Experience",         "Turn insight into conversation, and conversation into action."),
 ("measure",     "Measure",     "6", "Relationship Intelligence", "Measure what traditional AUM reporting cannot see."),
 ("firm",        "Firm",        "7", "Enterprise Intelligence",   "Scale what existed only in great advisors' heads."),
]
ENGINES = [{"k": k, "tab": t, "n": n, "name": nm, "promise": p} for k, t, n, nm, p in ENGINES]

# ---------------- the engine tools (from the Seven Engines console) ----------------
ET = [
 ("know","Family Discovery Brief","What we now know, and what we still need to ask.","Advisor",1,0,
  "Headings: ## What We Know, ## What This Suggests, ## What We Do Not Yet Know (the specific questions to ask next)."),
 ("know","Family Priority Map","Urgency, risk, opportunity, and gap.","Advisor",1,0,
  "Headings: ## High Urgency, ## Moderate Risk, ## Opportunity, ## Gap, ## Advisor Relationship Risk. One short paragraph each, naming the family members involved."),
 ("know","Family Opportunity Summary","The lowest-conflict doors into this family.","Advisor",0,0,
  "Identify three entry points that would create family participation with the least relational friction, ranked. For each: why it is low-conflict for this family, who to involve first, and what it could unlock next."),
 ("know","Life Transition Alerts","What is coming that no one has scheduled.","Advisor",0,0,
  "List the life, business, and family transitions this family is likely approaching in the next 12 to 60 months based on ages, roles, and business facts given. For each: the signal in the profile, the planning window, and the conversation that should happen before it arrives. Do not invent facts."),

 ("prescribe","Recommended Next Step","The single most useful next experience.","Advisor",1,1,
  "Format exactly: ## Primary Recommendation, ## Why, ## Who Participates, ## Desired Outcome, ## Advisor Role, ## Recommended Follow-On, ## Confidence (High, Moderate, or More Information Needed, with one sentence of justification). The recommendation must be an exact title from the library."),
 ("prescribe","Full Prescription Sheet","Journey, conversation, meeting, assessment, specialist, content, action.","Advisor",1,1,
  "One recommendation in each of the seven categories, using these headings: ## Journey, ## Conversation, ## Meeting, ## Assessment, ## Specialist, ## Content, ## Action. One or two sentences each. End with ## Sequence ordering them across the next twelve months."),
 ("prescribe","Specialist Recommendation","Who else belongs in the room, and why now.","Advisor",0,0,
  "Recommend two or three outside specialists, each in this format: ## Issue Identified, then Professional to Consider, Why, and Advisor Role. Coordinate rather than replace."),

 ("personalize","Personalized 30-Day Journey","Week map plus Day One, written for this family by name.","Family",0,1,
  "Build the opening of a personalized 30-day journey. Sections: ## The Journey (addressed to the parents by name, naming the children), ## Week One Understand, ## Week Two Reflect, ## Week Three Discuss, ## Week Four Decide (one or two sentences each), then ## Day One in full with a short teaching, one reflection question, one personal action, and one conversation prompt."),
 ("personalize","Couple Discussion Guide","Align the marriage before the children are invited in.","Family",0,0,
  "Sections: ## Our Life, ## Our Wealth, ## Our Children, ## Our Giving, ## Our Future, ## Our Legacy. Three questions under each, specific to this family. Close with ## Before You Compare Answers."),
 ("personalize","Next-Generation Guide","Their own experience, not their parents' material.","Family",0,0,
  "Address the adult children by name, one section per child reflecting that child's noted situation, plus a shared ## Before You Inherit Anything section. Frame the central question as who am I becoming before I receive more responsibility."),
 ("personalize","Family Meeting Guide","The family-facing invitation and agenda.","Family",0,0,
  "Sections: ## Why We Are Meeting (from the parents, in their voice), ## What to Expect, ## Before You Come, ## What We Will Discuss, ## What We Will Not Decide Yet. Warm enough that a disengaged adult child would still come."),
 ("personalize","Legacy Letter Starter","The letter the next generation actually keeps.","Family",0,0,
  "Sections: ## What to Write About (five prompts from this family's history), then ## A Draft Opening of roughly 120 words in the parents' voice, addressed to their children by name, written to be edited."),

 ("prepare","Family Stewardship Intelligence Brief","Never walk into a significant meeting unprepared.","Advisor",1,0,
  "Headings: ## Who Is Attending, ## What Matters Right Now, ## What They Told Us Last Time, ## Who Is Missing, ## What I Should Ask, ## What I Should Listen For, ## What I Should Avoid, ## What Could Come Next. Where history is not captured, say so plainly."),
 ("prepare","Five Questions to Ask","Prioritized, and in order.","Advisor",1,0,
  "Give exactly five questions for the next meeting, numbered in the order they should be asked. Under each, one line on why this question now and what a concerning answer would sound like."),
 ("prepare","Follow-Up Draft","The 48-hour note, ready to edit.","Advisor",0,0,
  "Draft the 48-hour follow-up: priorities, decisions to confirm, outstanding questions, assigned actions with owners, one warm personal line. Under 200 words, with one clearly marked blank for the professional's own sentence."),
 ("prepare","Next Best Action","One move, this week.","Advisor",1,0,
  "Headings: ## The Action, ## Why This One First, ## Exactly How (a script or specific steps), ## What Success Looks Like in 30 Days. Be decisive; do not list alternatives."),
 ("prepare","Advisor Value Story","Language for explaining what is different.","Advisor",0,0,
  "Write five versions of this professional's value story for this family: ## Thirty Seconds, ## Sixty Seconds, ## Faith-Forward, ## Next Generation, ## Acquisition. Each in first person, in the named professional's voice, and each usable out loud without editing."),

 ("experience","Family Meeting Kit","Agenda, exercise, worksheet, follow-up.","Advisor",0,0,
  "Headings: ## Objective, ## Participants, ## Opening Exercise, ## Agenda with timings for two hours, ## Conversation Questions (five), ## Decision Worksheet Items, ## Closing, ## Follow-Up Owners. Written for the professional as facilitator."),
 ("experience","Generosity Experience","Generosity as an experience, not content.","Family",0,0,
  "Design the Generous Together experience across seven steps: giving interests assessment, teaching, personal reflection, family cause map, family meeting, giving decision, follow-up impact conversation. One short paragraph per step, including how it could re-engage a disconnected adult child."),
 ("experience","Decision Worksheet & Action Plan","From discussion to decision to owner.","Family",0,0,
  "Headings: ## The Decision, ## Why It Matters Now, ## Options A B and C with honest trade-offs, ## Who Is Affected, ## Values at Stake, ## Professional Advice Needed, ## Review Date. Then ## Action Plan with 30-day, 90-day, and one-year items, each with a named owner."),

 ("measure","Relationship Depth Report","Computed scores, with the narrative behind them.","Advisor",1,0,
  "Headings: ## What the Numbers Say, ## Where the Trust Is Concentrated, ## What Would Happen If the Primary Advisor Retired Tomorrow, ## The Three Moves That Change the Score. Use the supplied numbers exactly; do not recalculate."),
 ("measure","Relationship Risk Alert","Classification, drivers, and the actions that clear it.","Advisor",1,0,
  "Use the supplied classification and drivers exactly. Headings: ## Classification, ## What Is Driving It (each driver, one line), ## Recommended Actions (four, in priority order, each with an owner and a timeframe), ## If Nothing Changes."),

 ("firm","Relationship Equity Rollup","What one household changes at the firm level.","CEO",1,0,
  "Headings: ## This Household Today, ## What Changes If the Recommended Journey Completes, ## The Same Pattern Across the Book (reason by proportion only, and state clearly that firm-wide figures are illustrative until real data is connected), ## What Leadership Should Track Monthly."),
 ("firm","Client Experience Standards","What every family in this tier is guaranteed to receive.","CEO",0,0,
  "Headings: ## Premier Family Standard (ten annual guarantees), ## Platinum and UHNW Standard (what it adds), ## How We Will Know It Happened (the evidence leadership can audit). Write it as firm policy, not aspiration."),
]
ETOOLS = [{"id": "et" + str(i+1), "e": e, "n": i+1, "name": nm, "sub": sb, "aud": au,
           "metrics": bool(mx), "library": bool(lb), "ins": ins}
          for i, (e, nm, sb, au, mx, lb, ins) in enumerate(ET)]
assert len(ETOOLS) == 24, len(ETOOLS)

STATS = {
 "journeys": len(JOURNEYS), "cats": len(CATS), "tools125": len(TOOLS125),
 "templates": len(TEMPLATES), "instruments": len(INSTRUMENTS),
 "questions": len(INSTRUMENTS) * 10, "roles": len(ROLES),
 "assessments": len(ASSESSMENTS), "matters": len(MATTERS),
 "days": len(JOURNEYS) * 30, "sessions": len(JOURNEYS) * 4, "engines": 7,
}
assert STATS["journeys"] == 225 and STATS["tools125"] == 125
assert STATS["templates"] == 25 and STATS["instruments"] == 10
assert STATS["roles"] == 20 and STATS["matters"] == 12

CATLIST = [{"name": c["name"], "titles": [next(e for e in JOURNEYS if e["id"] == i)["t"] for i in c["ids"]]} for c in CATS]

html = open("/home/claude/template4.html", encoding="utf-8").read()
for k, v in [("JOURNEYS", JOURNEYS), ("CATS", CATS), ("TOOLS125", TOOLS125), ("GROUPS", GROUPS),
             ("TEMPLATES", TEMPLATES), ("INSTRUMENTS", INSTRUMENTS), ("ROLES", ROLES),
             ("ASSESSMENTS", ASSESSMENTS), ("MATTERS", MATTERS), ("RHYTHM", RHYTHM),
             ("CATLIST", CATLIST), ("ENGINES", ENGINES), ("STATS", STATS)]:
    html = html.replace("/*__" + k + "__*/", json.dumps(v, ensure_ascii=False))
open("/mnt/user-data/outputs/can-platform.html", "w", encoding="utf-8").write(html)
print(json.dumps(STATS))
print("wrote", len(html), "bytes")
