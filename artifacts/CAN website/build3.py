# -*- coding: utf-8 -*-
import json, re

src = open("/mnt/user-data/outputs/can-library-clickable.html", encoding="utf-8").read()
def grab(name):
    m = re.search(r"^var " + name + r" = (.*);$", src, re.M)
    return json.loads(m.group(1))
ENTRIES = grab("ENTRIES"); CATS = grab("CATS")
byid = {e["id"]: e for e in ENTRIES}
CATLIST = [{"name": c["name"], "titles": [byid[i]["t"] for i in c["ids"]]} for c in CATS]
assert sum(len(c["titles"]) for c in CATLIST) == 225

# ---------------- who is using this ----------------
# src 1 = named by Brett; 0 = added to complete the set.
R = [
 ("Wealth Advisor / Financial Planner", 1, "The plan, and the family behind the plan.",
  ["Goal funding and cash flow", "Spouse and heir understanding", "Next-generation readiness", "Coordinating the other professionals"]),
 ("Investment Advisor", 1, "The portfolio, and what the capital is actually for.",
  ["Purpose assigned to each pool of capital", "Risk conversations across generations", "Concentration and liquidity events", "Teaching heirs to be owners"]),
 ("Multi-Family Office", 1, "Coordination across every family need at once.",
  ["Service standards by tier", "Coordination across specialists", "Family governance", "Reporting beyond performance"]),
 ("Single-Family Office Executive", 0, "The family's internal operating system.",
  ["Family employment and roles", "Decision rights and governance", "Continuity when principals age", "Confidentiality and information flow"]),
 ("Estate Planning Attorney", 1, "Documents that actually match intentions.",
  ["Gap between documents and intentions", "Fiduciary and trustee selection", "Family understanding of the plan", "Communication before transfer"]),
 ("CPA / Tax Advisor", 1, "The annual rhythm and the arithmetic of transfer.",
  ["Annual planning cadence", "Charitable timing and vehicles", "Entity and business structure", "Coordination with counsel"]),
 ("Generosity Advisor", 1, "Giving as formation, not transaction.",
  ["Why this family gives", "Involving children and grandchildren", "Giving while living", "Moving from reactive to intentional"]),
 ("Philanthropy Advisor / Foundation Consultant", 1, "Purpose, participation, and measurable impact.",
  ["Mission and grant strategy", "Family participation and governance", "Next-generation board roles", "Measuring outcomes"]),
 ("Nonprofit / Gift Planning Officer", 1, "Donor families, not donors.",
  ["The family's giving story", "Multigenerational donor relationships", "Blended and planned gifts", "Stewardship after the gift"]),
 ("Business Succession Advisor", 0, "Moving a company and a family through the same transition.",
  ["Ownership versus management", "Successor readiness", "Sibling and in-law dynamics", "Life after the sale"]),
 ("Insurance & Risk Advisor", 0, "Protecting the people, not only the balance sheet.",
  ["Liquidity at death", "Care and incapacity", "Business continuity", "Family understanding of coverage"]),
 ("Trust Officer / Corporate Trustee", 0, "Administering intent across generations.",
  ["Distribution philosophy", "Beneficiary preparedness", "Grantor intent when circumstances change", "Beneficiary relationships"]),
 ("Private Banker", 0, "Credit, liquidity, and the family behind the balance.",
  ["Liquidity events", "Family entity structure", "Next-generation banking relationships", "Introductions to specialists"]),
 ("Family Business Consultant", 0, "The overlap of family, ownership, and enterprise.",
  ["Roles and employment policy", "Founder transition", "Sibling partnership", "Culture and values in the enterprise"]),
 ("Family Governance Consultant", 0, "Structures that outlast the founders.",
  ["Family council and constitution", "Decision rights", "Meeting rhythm", "Conflict protocols"]),
 ("Family Legacy Coach", 0, "The story, values, and wisdom being transferred.",
  ["Values and mission clarity", "Story and blessing", "Wisdom transfer", "Family conversations"]),
 ("Pastor / Ministry Leader", 0, "Faith, formation, and stewardship of what was entrusted.",
  ["Faith across generations", "Contentment and enough", "Generosity as worship", "Pastoral care through transition"]),
 ("Elder Care & Longevity Advisor", 0, "More years, planned for on purpose.",
  ["Care expectations before crisis", "Caregiver roles among siblings", "Dignity and independence", "Coordinating health and wealth"]),
 ("Valuation & M&A Advisor", 0, "The transaction, and the family it changes.",
  ["Readiness of family and enterprise", "Identity after a sale", "Proceeds with purpose", "Preparing heirs for liquidity"]),
 ("Family Counselor", 0, "The relationships wealth will otherwise strain.",
  ["Communication patterns", "Perceived fairness", "Conflict and repair", "Boundaries with adult children"]),
]
ROLES = [{"id": "r" + str(i+1), "n": i+1, "name": n, "src": s, "promise": p, "themes": t}
         for i, (n, s, p, t) in enumerate(R)]

# ---------------- professional assessments ----------------
A = [
 ("Enneagram", "Nine types; motivation and stress behavior.", "https://www.enneagraminstitute.com/", "Type and wing, e.g. 3w2"),
 ("CliftonStrengths", "Formerly StrengthsFinder. Talent themes, ranked.", "https://www.gallup.com/cliftonstrengths/", "Top 5 themes"),
 ("Myers-Briggs (MBTI)", "Four preference pairs across sixteen types.", "https://www.myersbriggs.org/", "Four-letter type, e.g. ENFP"),
 ("DISC", "Dominance, Influence, Steadiness, Conscientiousness.", "https://www.discprofile.com/", "Primary and secondary style"),
 ("Big Five (IPIP-NEO)", "Openness, Conscientiousness, Extraversion, Agreeableness, Neuroticism. Public-domain item pool.", "https://ipip.ori.org/", "Five scores or percentiles"),
 ("Kolbe A Index", "Instinctive method of operation, four action modes.", "https://www.kolbe.com/", "Four-number result, e.g. 7-4-2-6"),
 ("Working Genius", "Six types of work that energize or drain.", "https://www.workinggenius.com/", "Two geniuses, two frustrations"),
 ("VIA Character Strengths", "Twenty-four character strengths, ranked.", "https://www.viacharacter.org/", "Top 5 strengths"),
]
ASSESSMENTS = [{"id": "a" + str(i+1), "name": n, "desc": d, "url": u, "hint": h}
               for i, (n, d, u, h) in enumerate(A)]

# ---------------- what families actually care about ----------------
M = [
 ("Succession", "Who takes over, and are they ready?",
  ["No named successor", "Documents that predate the current family", "Founder cannot picture stepping back"]),
 ("Longevity", "If we live another twenty-five years, what are they for?",
  ["Retirement framed as an ending", "No plan for the last third", "Identity fused to the career"]),
 ("Inheritance", "What transfers, when, and what do they already assume?",
  ["Children guessing at amounts", "Fair versus equal unresolved", "No conversation has ever happened"]),
 ("Next-Generation Readiness", "Are they becoming people who can carry this?",
  ["Entitlement worries named out loud", "No financial responsibility milestones", "One child disengaged"]),
 ("Family Unity & Communication", "Will money bring us closer or push us apart?",
  ["Subjects everyone avoids", "One member speaks for the family", "Old grievances still active"]),
 ("Generosity", "What should we give, and who decides?",
  ["Giving is reactive", "Children not involved", "Charitable vehicle underused"]),
 ("Business Transition", "Does the company outlive the founder, or get sold?",
  ["Ownership and management conflated", "In-law questions unresolved", "No life-after-sale picture"]),
 ("Health, Care & Aging", "Who cares for whom, and on what terms?",
  ["Care expectations unspoken", "One sibling carrying it alone", "No incapacity decisions made"]),
 ("Faith & Values Transfer", "Will what we believe survive the transfer?",
  ["Values assumed rather than named", "Generations believe differently", "No shared practice"]),
 ("Legacy & Story", "What will they remember when we are gone?",
  ["Elder stories uncaptured", "No letters or recordings", "History known to one person only"]),
 ("Purpose of Wealth", "What is all of this actually for?",
  ["No stated purpose for the capital", "Enough never defined", "Accumulation as the default"]),
 ("Governance & Continuity", "How does this family decide once the founders are gone?",
  ["No family meeting rhythm", "Decision rights undefined", "Nothing written down"]),
]
MATTERS = [{"id": "m" + str(i+1), "n": i+1, "name": n, "q": q, "signals": s}
           for i, (n, q, s) in enumerate(M)]

# ---------------- the annual rhythm seed ----------------
RHYTHM = [
 ("Annual Stewardship Review", "review", 90, "The family conversation before the performance conversation."),
 ("Family Meeting", "meeting", 120, "Multigenerational, facilitated, with pre-work."),
 ("Midyear Follow-Up", "zoom", 45, "Progress against the three priorities."),
 ("Generosity Conversation", "meeting", 60, "What the family gives, and who decides."),
 ("Next-Generation Touchpoint", "zoom", 45, "One conversation with each adult child."),
 ("Story Capture Session", "meeting", 90, "Recorded elder interview."),
]

STATS = {"roles": len(ROLES), "assessments": len(ASSESSMENTS), "matters": len(MATTERS),
         "journeys": 225, "rhythm": len(RHYTHM)}
assert len(ROLES) == 20 and len(ASSESSMENTS) == 8 and len(MATTERS) == 12

html = open("/home/claude/template3.html", encoding="utf-8").read()
for k, v in [("ROLES", ROLES), ("ASSESSMENTS", ASSESSMENTS), ("MATTERS", MATTERS),
             ("RHYTHM", RHYTHM), ("CATLIST", CATLIST), ("STATS", STATS)]:
    html = html.replace("/*__" + k + "__*/", json.dumps(v, ensure_ascii=False))
open("/mnt/user-data/outputs/can-professional-edition.html", "w", encoding="utf-8").write(html)
print("roles", len(ROLES), "named-by-Brett", sum(r["src"] for r in ROLES),
      "assessments", len(ASSESSMENTS), "matters", len(MATTERS))
print("wrote", len(html), "bytes")
