# -*- coding: utf-8 -*-
# Purpose Built Business — the company door, navy/gold system. Content data.

EM = "\u2014"

META = {
    "brand_a": "Life", "brand_b": "together",
    "eyebrow": "LifeTogether Marketplace Intelligence \u00b7 The Company Door",
    "h1_a": "Purpose Built ", "h1_em": "Business",
    "sub": ("A company that forms its people. Forty-day formation architecture, two flagship frameworks, "
            "a library of 2,025 titles across 165 categories " + EM + " built for the Christian business "
            "leader who wants Monday to mean something."),
    "cta1": ("Take the Diagnostic", "#diagnostic"),
    "cta2": ("See the Library", "#library"),
    "stats": [
        ("165", "Categories"),
        ("2,025", "Titles"),
        ("20", "Industry Verticals"),
        ("40", "Days " + EM + " the Formation Unit"),
    ],
    "status_chip": "Developing \u00b7 Internal edition \u00b7 prospect names appear " + EM + " remove before external use",
}

NAV = [
    ("The Argument", "#argument"),
    ("Frameworks", "#frameworks"),
    ("Diagnostic", "#diagnostic"),
    ("Flourishing", "#flourishing"),
    ("Three Seats", "#seats"),
    ("Launch It", "#launch"),
    ("Journeys", "#journeys"),
    ("The Library", "#library"),
    ("Pricing", "#pricing"),
    ("Founding 25", "#founding"),
    ("Strategy", "#strategy"),
]

ARGUMENT = {
    "eyebrow": "The Argument",
    "head_a": "Training informs. ", "head_em": "Formation transforms.",
    "paras": [
        ("Corporate learning has a completion problem, and everyone in the room knows it. Libraries of courses "
         "sit unopened; compliance modules get clicked through; culture decks get applauded and shelved. The "
         "missing ingredient was never content. It was architecture " + EM + " a whole company moving through "
         "one thing, together, for a defined season."),
        ("That architecture exists. It carried tens of millions of people through churchwide campaigns over "
         "twenty-five years: one theme, one rhythm, daily readings, weekly gatherings, leaders equipped, and an "
         "ending that lands. Purpose Built Business is that engine, rebuilt for the company " + EM + " forty "
         "days at a time, from the loading dock to the corner office."),
        ("And it is one half of a pair. The church door " + EM + " Marketplace Ministry " + EM + " forms a "
         "congregation for Monday. This door forms the company itself. Same engine underneath. Different buyer, "
         "different voice, different economics. Sunday equips Monday; Monday becomes mission."),
    ],
    "quote": "The marketplace is not where your people leave ministry. It is one of the primary places they do it.",
}

FRAMEWORKS = {
    "eyebrow": "Two Flagship Frameworks",
    "head_a": "One engine. ", "head_em": "Two front doors.",
    "intro": ("Every campaign, sprint, and study in the library hangs on one of two frameworks " + EM +
              " both recovered, both proven in their church-side originals, both rebuilt in marketplace language."),
    "f1": {
        "name": "Purpose Based Business",
        "tag": "The five-week framework",
        "body": ("The five biblical purposes, mapped to the life of a company. Five weeks, one purpose per week, "
                 "the whole organization on the same page."),
        "rows": [
            ("Worship", "Work as an offering " + EM + " excellence, integrity, and craft as devotion, not just output."),
            ("Fellowship", "A company where people are known " + EM + " belonging built on purpose, not proximity."),
            ("Discipleship", "Growth on purpose " + EM + " character developed as deliberately as competence."),
            ("Ministry", "Serving through the work itself " + EM + " every role able to name who it serves."),
            ("Mission", "The company as a sent thing " + EM + " impact beyond the walls, measured and told."),
        ],
        "note": "Eight founding themes in the recovered source; the five-purpose spine is the framework.",
    },
    "f2": {
        "name": "The Flourishing Workplace",
        "tag": "The six-week framework",
        "body": ("Six criteria of human flourishing, applied to the place people spend fifty hours a week. "
                 "Six weeks, one criterion per week " + EM + " and the live assessment below measures all six."),
        "rows": [
            ("Flourishing with God", "Work treated as meaningful to God " + EM + " not merely a means to an end."),
            ("Flourishing Together", "Real relationships, early conflict, people known rather than staffed."),
            ("Flourishing from Within", "Character, wellbeing, rest, and honest feedback that travels upward."),
            ("Flourishing through Contribution", "Strengths deployed, craft honored, excellence as integrity."),
            ("Flourishing for Others", "Generosity in the budget, service the whole company can join."),
            ("Flourishing Across Generations", "Mentoring, succession, and a story new people get to join."),
        ],
        "note": "The six-criteria structure is the recovered original; series titles carry it into the library.",
    },
}

DIAG = {
    "eyebrow": "Live Instrument \u00b7 No. 1",
    "head_a": "The Purpose Built ", "head_em": "Business Diagnostic",
    "intro": ("Twelve questions, scored out of 48, answerable by an owner and an HR leader together in ten "
              "minutes. It does not measure whether your company performs " + EM + " it measures whether it forms."),
    "confidential": ("Your answers stay on this page. Nothing is stored, transmitted, or used as sales "
                     "intelligence " + EM + " here or anywhere in this system."),
}

DIAGNOSTIC = [
    ("Could most employees say why this company exists " + EM + " beyond making money?",
     [("It has never been articulated", 0), ("It is on the wall", 1), ("It has been taught once", 2), ("It is common language here", 4)]),
    ("Do your stated values ever cost you anything?",
     [("Honestly, no", 0), ("Rarely", 1), ("Sometimes, quietly", 2), ("Yes " + EM + " and we tell those stories", 4)]),
    ("Does the company ever move through anything together " + EM + " a season, a study, a challenge?",
     [("Never", 0), ("An offsite, occasionally", 1), ("We have, once", 2), ("It is an annual rhythm", 4)]),
    ("Are managers developed to shepherd people " + EM + " not only to drive performance?",
     [("No", 0), ("We point to books", 1), ("Occasional training", 2), ("A leader track runs continuously", 4)]),
    ("Does day one teach who we are " + EM + " or only what to do?",
     [("Paperwork and passwords", 0), ("A culture slide", 1), ("A real story, once", 2), ("Formation begins on day one", 4)]),
    ("Do you measure culture with anything beyond turnover?",
     [("No", 0), ("An annual survey nobody reads", 1), ("A survey we act on", 2), ("Named indicators, reviewed quarterly", 4)]),
    ("Does the business give in a way employees can see " + EM + " and join?",
     [("Giving is private, if it happens", 0), ("A year-end check", 1), ("Occasional service days", 2), ("Generosity is an operating value with a budget line", 4)]),
    ("Is there a natural, voluntary place for conversations about meaning, calling, and faith?",
     [("It would be awkward here", 0), ("It happens in corners", 1), ("Leaders have opened the door", 2), ("Voluntary rhythms exist and are healthy", 4)]),
    ("Is the owner or CEO in any formation community of peers?",
     [("No", 0), ("An industry group, occasionally", 1), ("Informal friendships", 2), ("A committed peer group that tells the truth", 4)]),
    ("Has ownership ever discussed what the company is for " + EM + " beyond the exit?",
     [("The exit is the plan", 0), ("It has come up", 1), ("Once, seriously", 2), ("A written conviction exists", 4)]),
    ("Is character celebrated as loudly as results?",
     [("Results only", 0), ("Character gets a mention", 1), ("Sometimes, deliberately", 2), ("Both, in public, by name", 4)]),
    ("Do people leave this company better than they came " + EM + " and would you know?",
     [("We have never asked", 0), ("We hope so", 1), ("Exit conversations suggest it", 2), ("We ask, we track, we could show you", 4)]),
]

BANDS = [
    (0, 14, "Well-Run, Unformed",
     "The company may perform " + EM + " and forms no one on purpose. Begin with the argument, not a program: one leadership conversation about what this company is for."),
    (15, 26, "Values on the Wall",
     "The most common band in the marketplace: sincere values, real intentions, and no architecture carrying them into anyone's week. The fastest move is a single team sprint " + EM + " small, visible, finished."),
    (27, 38, "Formation Underway",
     "Rhythms exist. The gaps are almost always the owner's own formation and measurement. The peer group and the culture indicators are your next two moves."),
    (39, 48, "Purpose Built",
     "The company forms its people and could prove it. Your work now is multiplication " + EM + " your story becomes the case study that gives another owner permission."),
]

DISCERNMENT = [
    ("Impact", "Where would movement matter most to your people in the next twelve months?"),
    ("Urgency", "Which gap is costing you someone " + EM + " a leader, a culture, a succession " + EM + " right now?"),
    ("Invitation", "Where is God already stirring this? A conversation that keeps recurring, a leader who keeps asking."),
]

FLOUR = {
    "eyebrow": "Live Instrument \u00b7 No. 2",
    "head_a": "The Flourishing ", "head_em": "Workplace Assessment",
    "intro": ("Twenty-four statements across the six criteria, rated one to five " + EM + " strongly disagree to "
              "strongly agree. Ten minutes, scored out of 120, with a subtotal for each criterion so you can see "
              "not just how much your workplace flourishes, but where."),
    "scale": ["1 \u00b7 Strongly disagree", "2 \u00b7 Disagree", "3 \u00b7 Unsure", "4 \u00b7 Agree", "5 \u00b7 Strongly agree"],
}

# 6 dimensions x 4 statements, rated 1-5, /120
FLOUR_DIMS = [
    ("With God", [
        "Work here is treated as meaningful to God, not merely a means to an end.",
        "Prayer or reflection has a natural, voluntary place in our rhythm.",
        "Leaders speak openly about their own faith without pressuring anyone.",
        "Decisions are weighed against conviction, not only outcome.",
    ]),
    ("Together", [
        "People here are known, not just staffed.",
        "New people are folded into real relationships in their first month.",
        "Conflict is handled face to face, and early.",
        "We celebrate one another's wins outside the org chart.",
    ]),
    ("From Within", [
        "People could name how they have grown in character here in the last year.",
        "Managers ask about wellbeing before workload.",
        "Rest is modeled by leadership, not merely permitted.",
        "Honest feedback travels upward without penalty.",
    ]),
    ("Through Contribution", [
        "Every role here can explain who is served by its work.",
        "Excellence is taught as a form of integrity.",
        "People are deployed to their strengths, not just to openings.",
        "Craft and quality are honored in public.",
    ]),
    ("For Others", [
        "The company serves its community in ways employees can join on company time.",
        "Generosity shows up in the budget, not only the newsletter.",
        "Customers and vendors would call us fair even when it costs us.",
        "We pay attention to our impact on people outside our walls.",
    ]),
    ("Across Generations", [
        "Younger employees are deliberately mentored by senior ones.",
        "We are building leaders who could replace us.",
        "Ownership has a stated plan for what outlasts them.",
        "The company's story is told to new people as something they join.",
    ]),
]

FLOUR_BANDS = [
    (24, 59, "Begin with Trust and Purpose",
     "Flourishing has not been asked of this workplace yet. Start with one criterion " + EM + " Together is usually the door " + EM + " and one visible practice."),
    (60, 83, "Foundations Forming",
     "Pockets of health, no shared architecture. The six-week Flourishing Workplace journey exists precisely for this band."),
    (84, 104, "Emerging Flourishing Culture",
     "The culture is real and uneven " + EM + " your two lowest criteria name the next two quarters."),
    (105, 120, "A Flourishing Workplace",
     "Rare air. Protect it in writing, measure it annually, and let your people tell the story " + EM + " it recruits better than any brand campaign."),
]

SEATS_INTRO = ("Three seats, one gospel. An edition changes examples, pace, and questions " + EM +
               " never the theology or the structure.")

SEATS = [
    {
        "id": "owner", "label": "The Owner",
        "q": "What does faithful ownership look like?",
        "who": ("Founders, franchisees, family-business owners, practice principals. The seat that decides "
                "whether any of this happens " + EM + " and the loneliest chair in the church."),
        "path": [
            ("Begin", "The Purpose Built Business Diagnostic " + EM + " above, ten minutes, honest"),
            ("Join", "An owner's peer group " + EM + " the ten-study formation library below was built for that room"),
            ("Lead", "Bring the company through its first sprint, then its first forty days"),
            ("Endure", "Succession, generosity through the business, and the pre-exit conversation " + EM + " years before the letter of intent"),
        ],
    },
    {
        "id": "leader", "label": "Company & Market Leaders",
        "q": "How do I lead people and culture biblically?",
        "who": ("Executives, managers, site supervisors, market and regional leaders " + EM + " everyone "
                "responsible for other people's work and, whether titled for it or not, their flourishing."),
        "path": [
            ("Begin", "The Flourishing Workplace Assessment " + EM + " run it with your own team"),
            ("Learn", "The leaders' track: management as shepherding, culture as stewardship"),
            ("Practice", "A 21-day team challenge " + EM + " one habit, visibly finished"),
            ("Multiply", "Mentor one emerging leader; the pipeline is the point"),
        ],
    },
    {
        "id": "team", "label": "The Team",
        "q": "How does my Tuesday matter?",
        "who": ("The whole company " + EM + " the people the campaign was actually built for. Daily readings "
                "under two minutes, weekly table conversations, and an ending that lands."),
        "path": [
            ("Begin", "A 7\u201310 day team sprint " + EM + " small enough to say yes to"),
            ("Journey", "The 30-day team journey with pre- and post-assessment"),
            ("Together", "The 40-day company campaign " + EM + " one theme, every level, same season"),
            ("Continue", "The annual rhythm: one campaign, two sprints, and the assessments each year"),
        ],
    },
]

PEER = {
    "eyebrow": "The Owner's Peer Group",
    "head_a": "Ten studies for ", "head_em": "the loneliest chair.",
    "intro": ("The peer group of Christian business owners " + EM + " doing life, business, and faith formation "
              "together " + EM + " is the single most powerful formation environment available to the owner. "
              "These ten studies were built to be done in that community, and they are the natural content spine "
              "for peer networks and chapter rooms."),
    "line": "The owner who has no peer community has no one who can tell them the truth about themselves.",
    "studies": [
        ("The Owner's Peer Group", "Building the Formation Community That Every Christian Business Owner Needs", "Proverbs 27:17", "4 wks"),
        ("Raw Honesty Among Owners", "The Conversations That Business Owner Peer Groups Almost Never Have But Always Need", "James 5:16", "3 wks"),
        ("The Accountability Structure", "Building the Relational Framework Where Truth Is Welcome", "Proverbs 27:6", "3 wks"),
        ("When the Business Is Struggling", "What the Peer Group Offers the Owner in a Down Season That Nothing Else Can", "2 Corinthians 1:4", "3 wks"),
        ("Celebrating Success Together", "The Formation That Happens When Business Success Is Celebrated in Community", "Proverbs 11:25", "2 wks"),
        ("The Wisdom of Multiple Counselors", "How to Use the Collective Intelligence of a Peer Group for Major Business Decisions", "Proverbs 11:14", "3 wks"),
        ("Faith and Business Together", "What It Looks Like When Christian Business Owners Talk About Both Simultaneously", "Colossians 3:23", "3 wks"),
        ("The Mentoring Relationship", "Finding and Being the Business Mentor That Every Owner Needs", "2 Timothy 2:2", "3 wks"),
        ("Succession " + EM + " The Peer Conversation", "Having the Business Exit Conversation in the Safety of a Trusted Peer Community", "2 Kings 2:9", "3 wks"),
        ("Legacy " + EM + " What Will We Have Built Together", "The Peer Group That Asks the Ultimate Question Together", "Psalm 78:4\u20137", "3 wks"),
    ],
}

LIBRARY = {
    "eyebrow": "The Library",
    "head_a": "Marketplace Intelligence", "head_tm": "\u2122", "head_em": " \u2014 165 categories, 2,025 titles.",
    "intro": ("Built in seven numbered parts, each merged into one master catalog with honest running totals. "
              "Fifty church-proven categories translated into marketplace language, corporate-native disciplines, "
              "twenty industry verticals, and twenty-five double-depth categories built for the moment an owner "
              "says yes."),
    "spine_head": "Every category hangs on the same five-section spine",
    "spine": ["Calling & Purpose", "Leadership & Character", "Stewardship & Excellence", "Relationships & Culture", "Legacy & Kingdom Impact"],
    "parts": [
        ("Part One \u00b7 The Conversion", "The 50 Master Curriculum Categories, translated from church to marketplace language at full 10-campaign depth.", "50 categories \u00b7 500 titles"),
        ("Part Two \u00b7 Corporate-Native", "Disciplines a church never needed: onboarding, performance management, sales, compliance, cybersecurity, emotional intelligence, succession planning.", "25 categories \u00b7 250 titles"),
        ("Part Three \u00b7 The Gap Fill", "Ten categories closing the seams between the converted and the corporate.", "10 categories \u00b7 100 titles"),
        ("Part Four \u00b7 The Expansion", "Twenty-five further categories extending the core disciplines.", "25 categories \u00b7 250 titles"),
        ("Part Five \u00b7 Decision-Closing", "Ten categories built for the buying conversation itself.", "10 categories \u00b7 100 titles"),
        ("Part Six \u00b7 Industry Verticals", "Twenty professions, each with its own fifty-campaign library on the five-section spine.", "20 categories \u00b7 500 titles"),
        ("Part Seven \u00b7 Double-Depth", "Twenty-five categories at twenty-five campaigns each " + EM + " the owner-says-yes list: AI literacy, pricing strategy, fundraising, exit readiness, culture metrics.", "25 categories \u00b7 625 titles"),
    ],
    "verticals_head": "The twenty industry verticals",
    "verticals": ["Physicians", "Dentists", "Nurses", "Therapists & Counselors", "Accountants & CPAs", "Architects",
                  "Commercial Real Estate", "Insurance Professionals", "Bankers", "Private Equity & Venture Capital",
                  "Family Office Executives", "Engineers", "Scientists", "University Faculty", "Coaches & Consultants",
                  "Human Resources", "Manufacturing Executives", "Franchise Owners", "Restaurant & Hospitality Owners",
                  "Agriculture & Food Producers"],
    "math": "50 + 25 + 10 + 25 + 10 + 20 + 25 = 165 categories \u00b7 2,025 titles. The math is stated because it is real.",
}

PROCESS = {
    "eyebrow": "The Process",
    "head_a": "Start small. ", "head_em": "Finish together.",
    "intro": ("Formation is bought in steps, and the ladder is designed so every step proves the next one. "
              "Prices are the reconciled proposal bands " + EM + " see Status."),
    "steps": [
        ("7\u201310 Day Team Sprint", "$1,500\u2013$4,500", "Team manager or HR partner",
         "The entry that avoids a procurement process. One team, one week and a half, one visible finish."),
        ("10-Day Company Sprint", "$4,500\u2013$12,000", "CHRO or VP of People",
         "A fast, visible culture signal " + EM + " the whole company touches one theme together."),
        ("21-Day Team Challenge", "$4,500\u2013$12,000", "Department heads",
         "Habit formation with a demonstrable behavior shift inside thirty days."),
        ("30-Day Team Journey", "$9,000\u2013$25,000", "CHRO or CLO",
         "Core formation with pre- and post-assessment " + EM + " the instruments above, run before and after."),
        ("40-Day Company Campaign", "$18,000\u2013$60,000", "CEO and CHRO",
         "Company-wide formation on the full campaign architecture, framed to a twelve-month payback."),
    ],
    "rhythm": ("The annual rhythm most companies settle into: one forty-day campaign, two sprints, both "
               "assessments " + EM + " and a subscription that makes the whole library theirs."),
}

PRICING = {
    "eyebrow": "Pricing",
    "head_a": "One subscription. ", "head_em": "Unlimited formation.",
    "intro": ("The annual subscription is the primary model " + EM + " every per-campaign buyer should be a "
              "subscriber within twelve months. Headcount is the only variable. Proposed and unvalidated; "
              "see Status."),
    "tiers": [
        ("Team", "Up to 25 people", "$4,800 / yr", "Four hundred a month for the whole team."),
        ("Department", "Up to 100 people", "$12,000 / yr", "One hundred twenty dollars per person per year."),
        ("Company", "Up to 500 people", "$28,000 / yr", "Fifty-six dollars per person per year " + EM + " the working average of the model."),
        ("Enterprise", "500 and above", "$60,000\u2013$150,000 / yr", "Unlimited seats, custom branding, dedicated build support."),
    ],
    "models_head": "The five revenue models behind the page",
    "models": [
        ("Per-Campaign License", "Buy one campaign, run it once. $1,500\u2013$60,000 by format. The entry, never the destination."),
        ("Annual Subscription", "Unlimited campaigns, full library, one fee. The primary model."),
        ("Custom Campaign Build", "A bespoke campaign around your specific culture challenge. $15,000\u2013$150,000; every build includes a year-one subscription."),
        ("Cohort Facilitation", "Live, facilitated formation for leadership teams. $12,000 virtual to $120,000 for an executive year " + EM + " scales only with a certified-facilitator model."),
        ("Channel & Network License", "Peer networks white-label the platform for their members " + EM + " $8,000\u2013$18,000 per chapter to $200,000 national, or a 20\u201330% revenue share."),
    ],
}

STRATEGY = {
    "eyebrow": "Anchors & Channels \u00b7 Internal",
    "head_a": "Who carries it, ", "head_em": "and where it stands.",
    "warn": ("This section is for the internal edition only. Every name below is a prospect or a conversation "
             + EM + " none is a signed partner, and none of these names appears in the external edition."),
    "rows": [
        ("Movement Mortgage \u00b7 Casey Crawford", "Prospective anchor",
         "The priority first corporate case study; matched on the partner roster to 40 Days of Movement. The single critical gap in this entire vertical is a named anchor " + EM + " this is the shortest path to one."),
        ("Peach State Trucks \u00b7 Rick Reynolds", "Prospective anchor",
         "Matched on the partner roster to Purpose Built Business itself " + EM + " a mid-market, blue-collar proof case that would balance Movement's white-collar story. Reynolds also appears under Timothy Project; one relationship, two entry points."),
        ("Convene", "Channel prospect",
         "Christian CEO peer-advisory network. Chapter rooms are the natural home of the Owner's Peer Group library; the channel license model was built for exactly this shape."),
        ("C12", "Channel prospect",
         "The larger peer network; the licensing file names a C12 national partnership the top distribution priority " + EM + " and flags plainly that C12 is a prospect, not a signed channel. Sequencing must not assume it."),
    ],
    "notes_head": "Three strategy notes that travel with this page",
    "notes": [
        ("The anchor is the strategy.", "Without one named company that ran forty days and will say so, every price on this page is theoretical. The first sale is a case study wearing a purchase order."),
        ("Mind the price collision.", "The public campaign platform sells a church a forty-day campaign for $849. The corporate campaign must be visibly a different product " + EM + " facilitation, assessment, customization, support " + EM + " or a buyer will find both numbers."),
        ("Channels rent audiences; anchors earn them.", "Peer networks own the rooms of owners this page wants. Lead any channel conversation with their members' outcomes, not our library."),
    ],
}

STATUS = {
    "eyebrow": "Status \u00b7 Stated Honestly",
    "rows": [
        ("Platform", "Developing. Frameworks and library are built and recovered from source; this page assembles them. No component here is invented for the page."),
        ("Pricing", "Proposed and unvalidated. Where the two source sheets disagreed, the lower band is shown. No number has been tested with a buyer."),
        ("Instruments", "Both assessments are live and self-scoring on this page, drafted to the family standard. Neither has been run with a real company."),
        ("Launch & journeys", "Both launch outlines and all four journey outlines " + EM + " one hundred and one daily readings " + EM + " are drafted to the family standard on the workday rhythm. None has been field-run."),
        ("The Founding 25", "A proposed program with zero recruits. Its job is to convert the anchor gap into twenty-five parallel proofs; the founding rate is proposed, not tested."),
        ("Naming", "This page uses Purpose Built Business throughout. The Purpose Driven Business name is held back from buyer-facing use pending a rights ruling, and the Purpose Built / Purpose Driven boundary remains an open decision."),
        ("Relationships", "Every named person and organization is a prospect or a conversation. Nothing on this page implies endorsement, funding, or partnership."),
        ("The church door", "Marketplace Ministry " + EM + " the church-facing half of this vertical " + EM + " ships separately, on the church price list, and is never sold from this page."),
    ],
}

FOOTER = "Purpose Built Business \u00b7 The Company Door \u00b7 LifeTogether Marketplace Intelligence\u2122 \u00b7 Sunday Equips Monday"
