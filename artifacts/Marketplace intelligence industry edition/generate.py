import pandas as pd

SECTIONS = [
    "Calling & Purpose",
    "Leadership & Character",
    "Stewardship & Excellence",
    "Relationships & Culture",
    "Legacy & Kingdom Impact",
]

CALLING_T = [
    "The {role}'s Calling",
    "Called to {verb_title}",
    "Faith in {workplace_title}",
    "More Than {task_article} {task_title}",
    "Sacred Work",
    "Created to {verb_title}",
    "The Ministry of {domain_title}",
    "Beyond the {task_title}",
    "Ordinary Days, Eternal Purpose",
    "Faith at Work",
]
CALLING_S = [
    "Discovering God's purpose in {domain}",
    "Living out a sacred trust as {article} {role_lc}",
    "Christ present in every {workplace_lc}",
    "Seeing the whole person behind the {task_lc}",
    "{verbing} as an offering to God",
    "Reflecting the Creator through {domain}",
    "Faithfulness in the daily work of {domain}",
    "Building trust one {task_lc} at a time",
    "Finding meaning in routine {domain} work",
    "Living authentically as {article} {role_lc} for Christ",
]

LEADERSHIP_T = [
    "Leading with Integrity",
    "The Trusted {role}",
    "Grace Under Pressure",
    "Wisdom in {workplace_title}",
    "The Servant {role}",
    "Courage to Tell the Truth",
    "Leading Through Uncertainty",
    "Character on Call",
    "The {role}'s Example",
    "Leading Well, Serving Well",
]
LEADERSHIP_S = [
    "Leading by character, not just title",
    "Character that earns lasting confidence",
    "Leading through the moments that matter most",
    "Discernment beyond the {task_lc}",
    "Leadership expressed through service, not status",
    "Honesty in the hardest conversations",
    "Faith when the answers aren't clear yet",
    "Who you are when no one's watching",
    "Mentoring the next generation of {role_plural_lc}",
    "Influence built on trust, not title",
]

STEWARDSHIP_T = [
    "Excellence as Worship",
    "Stewarding Your Training",
    "The Disciplined {role}",
    "Guarding Against Burnout",
    "Faithful in the Details",
    "Stewarding Trust",
    "The Long Obedience",
    "Wise Use of Time",
    "Lifelong Learning, Lifelong Faith",
    "The Whole-Person {role}",
]
STEWARDSHIP_S = [
    "Bringing your best {task_lc} as an offering",
    "Using hard-won expertise for eternal purposes",
    "Excellence without idolizing achievement",
    "A sustainable rhythm for a demanding calling",
    "Precision as an act of care",
    "Guarding what's been entrusted to you",
    "Excellence over a career, not just a day",
    "Stewarding a full schedule with peace",
    "Growing in skill and in Christ together",
    "Excellence that includes the soul, not just the {task_lc}",
]

RELATIONSHIPS_T = [
    "Beyond the {task_title}",
    "The Healthy Team",
    "Compassion in Conflict",
    "Serving Like Family",
    "Building Trust Quickly",
    "The Collegial {role}",
    "Culture of Care",
    "Listening First",
    "Faith Among Colleagues",
    "Protecting What Matters Most at Home",
]
RELATIONSHIPS_S = [
    "Building real relationships beyond the {task_lc}",
    "A culture that supports every {role_lc}",
    "Navigating hard conversations with grace",
    "Treating clients and coworkers like family",
    "Earning confidence in a short window of time",
    "Honoring peers across every specialty and role",
    "Building a workplace people trust",
    "Presence as the first and best gift",
    "Living authentically in a secular workplace",
    "Guarding home while serving others well",
]

LEGACY_T = [
    "The {role}'s Legacy",
    "Work That Points to Heaven",
    "Beyond Retirement",
    "Mentoring the Next Generation",
    "The Kingdom {role}",
    "Finish Well",
    "A Legacy of Character",
    "Generational Impact",
    "Eternal Significance in Daily Work",
    "Called Beyond {workplace_title}",
]
LEGACY_S = [
    "More than years spent in {domain}",
    "Work with significance that outlasts a career",
    "A calling that doesn't end at retirement",
    "Passing on more than skill",
    "Influence that outlasts any title",
    "Faithfulness all the way to the last {task_lc}",
    "Remembered for how you treated people",
    "Building a legacy of faith and skill",
    "Every {task_lc}, an eternal opportunity",
    "Influence that reaches your community and church",
]

SECTION_TEMPLATES = [
    (SECTIONS[0], CALLING_T, CALLING_S),
    (SECTIONS[1], LEADERSHIP_T, LEADERSHIP_S),
    (SECTIONS[2], STEWARDSHIP_T, STEWARDSHIP_S),
    (SECTIONS[3], RELATIONSHIPS_T, RELATIONSHIPS_S),
    (SECTIONS[4], LEGACY_T, LEGACY_S),
]

CATEGORIES = [
    dict(name="Physicians", role="Physician", article="a", domain="medicine",
         domain_title="Medicine", workplace_lc="exam room", workplace_title="the Exam Room",
         task_lc="diagnosis", task_title="Diagnosis", verb_title="Heal", verbing="Healing"),
    dict(name="Dentists", role="Dentist", article="a", domain="dentistry",
         domain_title="Dentistry", workplace_lc="operatory", workplace_title="the Operatory",
         task_lc="appointment", task_title="Appointment", verb_title="Restore", verbing="Restoring"),
    dict(name="Nurses", role="Nurse", article="a", domain="nursing",
         domain_title="Nursing", workplace_lc="bedside", workplace_title="the Bedside",
         task_lc="shift", task_title="Shift", verb_title="Care", verbing="Caring"),
    dict(name="Therapists & Counselors", role="Counselor", article="a", domain="counseling",
         domain_title="Counseling", workplace_lc="therapy room", workplace_title="the Therapy Room",
         task_lc="session", task_title="Session", verb_title="Counsel", verbing="Counseling"),
    dict(name="Accountants & CPAs", role="CPA", article="a", domain="accounting",
         domain_title="Accounting", workplace_lc="ledger", workplace_title="the Ledger",
         task_lc="return", task_title="Return", verb_title="Steward", verbing="Stewarding",
         role_plural_lc="CPAs"),
    dict(name="Architects", role="Architect", article="an", domain="architecture",
         domain_title="Architecture", workplace_lc="blueprint", workplace_title="the Blueprint",
         task_lc="design", task_title="Design", verb_title="Design", verbing="Designing"),
    dict(name="Commercial Real Estate", role="Broker", article="a", domain="commercial real estate",
         domain_title="Commercial Real Estate", workplace_lc="listing", workplace_title="the Listing",
         task_lc="deal", task_title="Deal", verb_title="Build", verbing="Building"),
    dict(name="Insurance Professionals", role="Agent", article="an", domain="insurance",
         domain_title="Insurance", workplace_lc="policy", workplace_title="the Policy",
         task_lc="claim", task_title="Claim", verb_title="Protect", verbing="Protecting"),
    dict(name="Bankers", role="Banker", article="a", domain="banking",
         domain_title="Banking", workplace_lc="branch", workplace_title="the Branch",
         task_lc="transaction", task_title="Transaction", verb_title="Steward", verbing="Stewarding"),
    dict(name="Private Equity & Venture Capital", role="Investor", article="an", domain="private equity and venture capital",
         domain_title="Private Equity", workplace_lc="deal room", workplace_title="the Deal Room",
         task_lc="deal", task_title="Deal", verb_title="Invest", verbing="Investing"),
    dict(name="Family Office Executives", role="Executive", article="an", domain="family office leadership",
         domain_title="Family Office Leadership", workplace_lc="family office", workplace_title="the Family Office",
         task_lc="portfolio review", task_title="Portfolio Review", verb_title="Steward", verbing="Stewarding"),
    dict(name="Engineers", role="Engineer", article="an", domain="engineering",
         domain_title="Engineering", workplace_lc="job site", workplace_title="the Job Site",
         task_lc="project", task_title="Project", verb_title="Engineer", verbing="Engineering"),
    dict(name="Scientists", role="Scientist", article="a", domain="science",
         domain_title="Science", workplace_lc="laboratory", workplace_title="the Laboratory",
         task_lc="experiment", task_title="Experiment", verb_title="Discover", verbing="Discovering"),
    dict(name="University Faculty", role="Professor", article="a", domain="academia",
         domain_title="Academia", workplace_lc="lecture hall", workplace_title="the Lecture Hall",
         task_lc="lecture", task_title="Lecture", verb_title="Teach", verbing="Teaching"),
    dict(name="Coaches & Consultants", role="Coach", article="a", domain="coaching and consulting",
         domain_title="Coaching", workplace_lc="coaching session", workplace_title="the Coaching Session",
         task_lc="session", task_title="Session", verb_title="Coach", verbing="Coaching"),
    dict(name="Human Resources", role="HR Leader", article="an", domain="human resources",
         domain_title="Human Resources", workplace_lc="interview room", workplace_title="the Interview Room",
         task_lc="hire", task_title="Hire", verb_title="Hire", verbing="Hiring",
         role_plural_lc="HR leaders"),
    dict(name="Manufacturing Executives", role="Executive", article="an", domain="manufacturing leadership",
         domain_title="Manufacturing", workplace_lc="plant floor", workplace_title="the Plant Floor",
         task_lc="production run", task_title="Production Run", verb_title="Build", verbing="Building"),
    dict(name="Franchise Owners", role="Franchise Owner", article="a", domain="franchising",
         domain_title="Franchising", workplace_lc="storefront", workplace_title="the Storefront",
         task_lc="location", task_title="Location", verb_title="Multiply", verbing="Multiplying",
         role_plural_lc="franchise owners"),
    dict(name="Restaurant & Hospitality Owners", role="Owner", article="an", domain="hospitality",
         domain_title="Hospitality", workplace_lc="dining room", workplace_title="the Dining Room",
         task_lc="table", task_title="Table", verb_title="Serve", verbing="Serving"),
    dict(name="Agriculture & Food Producers", role="Producer", article="a", domain="food production",
         domain_title="Agriculture", workplace_lc="field", workplace_title="the Field",
         task_lc="harvest", task_title="Harvest", verb_title="Grow", verbing="Growing"),
]

TASK_ARTICLE_AN = {"Appointment", "Experiment"}

rows = []
for cat in CATEGORIES:
    role_lc = cat["role"].lower() if cat["role"] not in ("CPA", "HR Leader") else cat["role"]
    role_plural_lc = cat.get("role_plural_lc", role_lc + "s")
    fmt = dict(cat)
    fmt["role_lc"] = role_lc
    fmt["role_plural_lc"] = role_plural_lc
    fmt["task_article"] = "an" if cat["task_title"] in TASK_ARTICLE_AN else "a"

    for section_name, titles, subs in SECTION_TEMPLATES:
        for i, (t_tpl, s_tpl) in enumerate(zip(titles, subs), start=1):
            title = t_tpl.format(**fmt)
            sub = s_tpl.format(**fmt)
            rows.append({
                "Category": cat["name"],
                "Section": section_name,
                "#": i,
                "Title": title,
                "Subtitle": sub,
            })

df = pd.DataFrame(rows)
print(f"Total rows: {len(df)}")
print(f"Categories: {df['Category'].nunique()}")
print(df.groupby('Category').size())
df.to_csv("/home/claude/workplace_lib/campaigns.csv", index=False)
print("saved csv")
