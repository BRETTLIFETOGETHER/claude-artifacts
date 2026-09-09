# -*- coding: utf-8 -*-
import json, re

src = open("/mnt/user-data/outputs/can-library-clickable.html", encoding="utf-8").read()

def grab(name):
    m = re.search(r"^var " + name + r" = (.*);$", src, re.M)
    return json.loads(m.group(1))

ENTRIES = grab("ENTRIES")
CATS = grab("CATS")
JOURNEYS = [e for e in ENTRIES if e["kind"] == "journey"]
assert len(JOURNEYS) == 225, len(JOURNEYS)
assert len(CATS) == 15

# ---------------- the 25 family toolbox templates ----------------
# Each is drawn from Brett's own 125-tool ecosystem; "who" lists the customization
# audiences offered in the dropdown; "ins" is the generation instruction.

T = [
 ("Family Stewardship Assessment",
  "Scores the family across wealth, wisdom, relationships, values, generosity, succession, and legacy.",
  ["Whole family", "Couple", "Each adult child"],
  "Build the assessment: 7 dimensions x 4 statements, each rated 1 to 5, with a /20 per dimension and /140 total. Then give four score bands with what each band means and the first move it implies. Statements must reflect this family's actual concerns."),
 ("Couple Alignment Assessment",
  "Reveals where spouses agree and differ around money, children, giving, inheritance, and legacy.",
  ["Couple"],
  "Write 20 statements each spouse answers privately, grouped in five areas. Then give the comparison key: what strong agreement, possible misunderstanding, and different priorities each look like, and the three questions to bring to the advisor."),
 ("What's in Your Hand? Inventory",
  "Inventories time, talent, treasure, relationships, influence, experiences, and opportunities.",
  ["Whole family", "Couple", "Each adult child"],
  "Build the seven-part inventory with prompts under each heading, sized so a family can complete it in one sitting. Close with three questions that turn the inventory into a decision."),
 ("Family Values Builder",
  "Turns selected values into observable family behaviors.",
  ["Whole family", "Couple"],
  "Give a working list of candidate values drawn from this family's stated aspirations, a selection exercise, and then for the likely final five, translate each into one observable behavior a grandchild could recognize."),
 ("Family Mission Builder",
  "Produces a concise family mission statement.",
  ["Whole family", "Couple"],
  "Give the four questions that produce a mission statement, a worked example built from this family's own profile, and two alternative draft statements they can edit rather than start from blank."),
 ("Family Purpose Statement",
  "Answers what the family hopes its resources ultimately accomplish.",
  ["Whole family", "Couple"],
  "Produce a one-page instrument: three framing questions, a drafting frame, and two draft purpose statements specific to this family's business, giving, and generational situation."),
 ("Enough Calculator & Conversation",
  "Helps distinguish lifestyle needs, security, inheritance, and surplus.",
  ["Couple", "Whole family"],
  "Build the four-bucket conversation: lifestyle, security, inheritance, surplus. Give the questions that define each bucket for this family and the decision the conversation is meant to produce. Use no specific dollar figures and give no investment or tax advice."),
 ("Family Wealth Purpose Map",
  "Assigns purposes to pools of capital.",
  ["Couple", "Whole family"],
  "Give a mapping worksheet that assigns a stated purpose, a time horizon, and an intended beneficiary to each pool of family capital. Name the pools generically; do not invent balances."),
 ("Family Generosity Map",
  "Maps causes, ministries, geography, passions, and giving vehicles.",
  ["Whole family", "Each adult child", "Couple"],
  "Build the mapping exercise across causes, geography, passions, and vehicles, with prompts that surface why each matters to this family, and a final step that turns the map into one giving decision for this year."),
 ("Family Legacy Statement",
  "Defines what the family hopes to pass beyond financial assets.",
  ["Couple", "Whole family"],
  "Give the prompts that surface story, values, faith, and wisdom, then a 120-word draft legacy statement in the parents' voice that they can edit."),
 ("Family Stewardship Priority Map",
  "Ranks the family's issues into Now, Next, and Later.",
  ["Advisor"],
  "Rank this family's actual issues into ## Now, ## Next, and ## Later. Under each item give one line on why it sits there and what would move it. Be decisive rather than comprehensive."),
 ("Couple Conversation Guide",
  "Structured spouse discussion before wider family conversations.",
  ["Couple"],
  "Write the guide in six sections: Our Life, Our Wealth, Our Children, Our Giving, Our Future, Our Legacy. Three questions under each, specific to this family. Close with how to compare answers without turning it into an argument."),
 ("Family Conversation Cards",
  "Questions around wealth, values, faith, inheritance, generosity, and relationships.",
  ["Whole family", "Each adult child", "Couple", "Grandchildren"],
  "Write 18 conversation cards grouped in six categories, each a single question short enough to print on a card. Vary emotional depth so a family can start shallow and go deeper."),
 ("Inheritance Conversation Guide",
  "Helps parents communicate intentions without disclosing every financial detail.",
  ["Couple", "Whole family"],
  "Give the guide in three parts: what to say, what not to say yet, and how to answer the four questions adult children most often ask. Include language for declining to share a number without sounding evasive."),
 ("Next-Generation Conversation Guide",
  "Gives parents and adult children a structured pathway into responsibility.",
  ["Each adult child", "Whole family"],
  "Write a conversation pathway with an opening the parent can read aloud, five questions, and the responsibility milestone the conversation is meant to reach. Frame it around who they are becoming, never around amounts."),
 ("Family Meeting Kit",
  "Invitation, pre-work, agenda, exercises, facilitation, decisions, and follow-up.",
  ["Whole family"],
  "Build the full kit: invitation text, purpose statement, two pieces of pre-work, a timed two-hour agenda, an opening exercise, five conversation questions, the decision worksheet items, and the follow-up note."),
 ("Difficult Conversation Planner",
  "Prepares the family for conflict, inequity, entitlement, or relational strain.",
  ["Couple", "Advisor", "Whole family"],
  "Plan one difficult conversation this family actually faces. Sections: what is really at stake, what each person likely fears, the opening sentence, what to avoid saying, how to end well, and what to do if it goes badly."),
 ("Sibling Stewardship Guide",
  "Helps siblings prepare for shared assets and decision authority.",
  ["Each adult child", "Whole family"],
  "Write the guide for siblings who will one day decide together: the agreements to reach before they inherit, the four flashpoints to expect, and a simple decision protocol they can adopt now."),
 ("Grandparent Conversation Guide",
  "Helps grandparents intentionally transfer wisdom and story.",
  ["Grandchildren", "Couple"],
  "Write age-appropriate prompts for grandparents in three age bands, plus a short script for asking permission from the middle generation first."),
 ("Legacy Letter Builder",
  "Helps parents and grandparents write personal legacy letters.",
  ["Each adult child", "Grandchildren", "Couple"],
  "Give five prompts drawn from this family's own history, then a 120-word draft opening in the parents' voice addressed to the named recipient, written to be edited rather than sent as is."),
 ("Family Story Capture",
  "Interview prompts converted into written family stories.",
  ["Couple", "Whole family", "Grandchildren"],
  "Give 12 interview prompts across childhood, marriage, business, faith, money, failure, and turning points, plus recording instructions and the one follow-up question that gets past a rehearsed answer."),
 ("Ready to Receive Workbook",
  "Prepares heirs for increasing responsibility.",
  ["Each adult child"],
  "Build a short workbook for the named heir: a self-assessment across work, money, character, giving, and leadership, then three practices for the next 90 days and the conversation to have with their parents at the end."),
 ("Family Blessing & Commissioning Guide",
  "Helps parents intentionally affirm and commission the next generation.",
  ["Each adult child", "Whole family"],
  "Give the structure of a blessing: what is seen in them, what is entrusted to them, and what is hoped for them. Include a spoken draft for the named recipient of roughly 120 words."),
 ("Family Decision Worksheet",
  "Integrates values, relationships, finances, professional counsel, and decision criteria.",
  ["Whole family", "Couple"],
  "Produce the worksheet for this family's most pressing open decision: the decision, why now, options A B and C with honest trade-offs, who is affected, values at stake, professional advice needed, and a review date."),
 ("Family Stewardship Action Plan",
  "Converts discussion into 30-day, 90-day, and annual commitments.",
  ["Whole family", "Couple", "Advisor"],
  "Build the plan across three horizons, each item with an owner, a deadline, the support needed, the professional involved, and the advisor follow-up. Three items per horizon, no more."),
]

TEMPLATES = []
for i, (name, purpose, who, ins) in enumerate(T):
    TEMPLATES.append({"id": "x" + str(i + 1), "n": i + 1, "name": name, "purpose": purpose,
                      "who": who, "ins": ins})

assert len(TEMPLATES) == 25, len(TEMPLATES)

# ---------------- the top-10 interview instruments ----------------
# src 1 = in Brett's Family Legacy Intelligence instrument set; src 0 = added here.
# aud drives the subject dropdown, filled from the live family profile.

I = [
 ("Couple Legacy Interview", "couple", 1,
  "Both spouses, together, recorded. The transcript is the primary source material for everything else CAN builds.",
  "a shared three-part statement: what we received, what we built, what we want carried forward"),
 ("Patriarch Legacy Interview", "g1both", 1,
  "One elder, alone, on the story behind the decisions.",
  "a three-part legacy statement in his own words"),
 ("Matriarch Legacy Interview", "g1both", 1,
  "One elder, alone, on the story behind the decisions.",
  "a three-part legacy statement in her own words"),
 ("Next-Generation Legacy Interview", "children", 1,
  "Ten questions the adult child asks the elders, not ten questions asked of them.",
  "a four-part reflection written after the conversation"),
 ("Grandchild Legacy Interview", "g3", 0,
  "Age-appropriate questions a grandchild can ask a grandparent, with permission from the middle generation first.",
  "one story recorded and one question they still want answered"),
 ("Business Successor Interview", "children", 0,
  "For the family member expected to carry the enterprise.",
  "a three-part statement on what they are taking on, and what they are not"),
 ("Sibling Alignment Interview", "childrenGroup", 0,
  "All adult children together, before they ever have to decide together.",
  "three agreements the siblings make with each other now"),
 ("Surviving Spouse Readiness Interview", "g1both", 0,
  "The conversation that assumes one spouse will one day lead alone.",
  "a readiness statement naming what is understood and what is not yet"),
 ("Spouse-of-Heir Interview", "inlaws", 0,
  "The person who married into the family and will shape how wealth is received.",
  "a three-part statement on what they hope for their own household"),
 ("Advisor Discovery Interview", "family", 0,
  "The ten questions the advisor asks to learn the family's story beyond the financial data.",
  "the advisor's private discovery brief, never shown to the family as written"),
]

INSTRUMENTS = []
for i, (name, aud, src, purpose, closing) in enumerate(I):
    INSTRUMENTS.append({"id": "i" + str(i + 1), "n": i + 1, "name": name, "aud": aud,
                        "src": src, "purpose": purpose, "closing": closing})

assert len(INSTRUMENTS) == 10, len(INSTRUMENTS)

STATS = {"journeys": 225, "cats": 15, "templates": 25, "days": 225 * 30, "sessions": 225 * 4,
         "instruments": len(INSTRUMENTS), "questions": len(INSTRUMENTS) * 10}

html = open("/home/claude/template2.html", encoding="utf-8").read()
html = html.replace("/*__ENTRIES__*/", json.dumps(JOURNEYS, ensure_ascii=False))
html = html.replace("/*__CATS__*/", json.dumps(CATS, ensure_ascii=False))
html = html.replace("/*__TEMPLATES__*/", json.dumps(TEMPLATES, ensure_ascii=False))
html = html.replace("/*__INSTRUMENTS__*/", json.dumps(INSTRUMENTS, ensure_ascii=False))
html = html.replace("/*__STATS__*/", json.dumps(STATS, ensure_ascii=False))
open("/mnt/user-data/outputs/can-family-workspace.html", "w", encoding="utf-8").write(html)
print("journeys", len(JOURNEYS), "cats", len(CATS), "templates", len(TEMPLATES))
print("wrote", len(html), "bytes")
