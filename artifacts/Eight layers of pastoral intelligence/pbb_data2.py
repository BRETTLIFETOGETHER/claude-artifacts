# -*- coding: utf-8 -*-
# Purpose Built Business — data module 2: Launch, Journeys, Roster, Founding 25
EM = "\u2014"

LAUNCH = {
    "eyebrow": "Launch It",
    "head_a": "Two doors. ", "head_em": "One launch discipline.",
    "intro": ("A marketplace ministry launches in a church or in a company " + EM + " same engine, opposite "
              "rooms. Choose the door; every phase below opens with a tap."),
}

LAUNCH_DOORS = [
    {
        "id": "church", "label": "In Your Church",
        "sub": ("Ninety days from decision to a commissioned congregation " + EM + " built on the standard "
                "campaign launch discipline, pointed at Monday."),
        "phases": [
            ("Phase 1 \u00b7 Decide", "Weeks 1\u20132", [
                "The senior pastor owns the why " + EM + " one message-level conviction, not a memo from the office.",
                "Run the Marketplace Ministry Diagnostic with the executive pastor. Ten minutes, honest answers.",
                "Name one volunteer marketplace leader " + EM + " the bridge person who already believes Monday matters.",
                "Set the launch Sunday and count every date backward from it.",
            ]),
            ("Phase 2 \u00b7 Build", "Weeks 3\u20136", [
                "Choose the campaign " + EM + " Purpose at Work, with the overview sermon already in hand.",
                "Configure the three seats: employee groups, a monthly leaders' table, private invitations for owners.",
                "Prepare the deployment-map exercise " + EM + " the church names the ten largest employers of its own people during launch month.",
                "Order print. Digital is the sample; the box of journals arriving on a Tuesday is the product.",
            ]),
            ("Phase 3 \u00b7 Recruit", "Weeks 5\u20138", [
                "Recruit hosts by name, never by announcement.",
                "Invite owners personally and privately " + EM + " a letter and a meal, not a bulletin line.",
                "Brief every group leader on the six-day devotional rhythm and the reply question.",
            ]),
            ("Phase 4 \u00b7 Prime", "Weeks 7\u20139", [
                "Send the forward-looking story question three weeks out: where have you seen God in your work?",
                "Plan Commissioning Sunday " + EM + " hands laid on workers, by name, the whole church watching.",
                "Protect the calendar: no fundraising ask within ninety days of the campaign, either side.",
            ]),
            ("Phase 5 \u00b7 Run", "The 40 Days", [
                "Preach the series. Groups meet weekly. The six-day devotional reaches the desk before the workday does.",
                "Capture stories with permission " + EM + " three naming options, ask once, show the edit.",
                "The owners' table meets twice inside the forty " + EM + " shepherding, never soliciting.",
            ]),
            ("Phase 6 \u00b7 Land", "The Weeks After", [
                "Commission workers publicly on the closing Sunday " + EM + " the nurse, the foreman, the founder, by name.",
                "Every group chooses its next study before week six ends. A group that finishes without choosing usually stops.",
                "The owners' table becomes standing. The leaders' table goes monthly.",
                "Record the first leading indicators and put the ninety-day callback on the calendar now.",
            ]),
        ],
        "rules_head": "The two rules that protect it",
        "rules": [
            "Never run marketplace formation and a fundraising ask in the same season " + EM + " ninety days minimum between them.",
            "Commission publicly, shepherd privately. Nothing shared in ministry is ever sales intelligence.",
        ],
    },
    {
        "id": "work", "label": "In Your Workplace",
        "sub": ("For the Christian owner or leader bringing formation into the company they steward " + EM +
                " starting with the smallest possible yes."),
        "phases": [
            ("Phase 1 \u00b7 The Owner's Yes", "Weeks 1\u20132", [
                "Settle your own why before you ask for anyone else's.",
                "Take the Purpose Built Business Diagnostic above " + EM + " honestly, with one other leader in the room.",
                "Sit with a peer group or one trusted owner first. Nobody should launch this alone.",
                "Choose the voice: the values-based edition company-wide, the faith-based edition as the voluntary track.",
            ]),
            ("Phase 2 \u00b7 The Quiet Build", "Weeks 3\u20135", [
                "Pick the smallest yes " + EM + " the 10-Day Sprint, one team or the whole company.",
                "Customize on the fixed spine: your company's name, your stories, your language. The architecture never changes.",
                "Brief your leadership team first. Leaders opt in before anyone else even hears of it.",
                "Put the guardrails below in writing and share them with HR before the invitation goes out.",
            ]),
            ("Phase 3 \u00b7 The Invitation", "Week 6", [
                "Launch as an invitation, never an initiative. Nobody is voluntold.",
                "On company time, voluntary, food on the table.",
                "Say plainly what it is and what it is not " + EM + " five minutes, no pressure, come once and decide.",
            ]),
            ("Phase 4 \u00b7 The Sprint", "Two Weeks", [
                "A two-minute reading opens each workday " + EM + " weekdays only, nothing on the weekend.",
                "One table conversation a week. Leaders talk least.",
                "Finish visibly: the Day 10 commitment, named out loud, celebrated once.",
            ]),
            ("Phase 5 \u00b7 The Ladder", "Months 2\u20136", [
                "Sprint, then the 21-Day Habits, then the 30-Day Flourishing Journey.",
                "Run the Flourishing Workplace Assessment before and after the thirty days.",
                "Let the results, not the owner, make the argument for the forty.",
            ]),
            ("Phase 6 \u00b7 The Rhythm", "Year One", [
                "The 40-day flagship once a year " + EM + " whole company, same season, one theme.",
                "Both assessments annually. Stories captured with permission and told at the table.",
                "One generosity project the whole company can join on the clock.",
            ]),
        ],
        "rules_head": "The guardrails " + EM + " in writing, before anything launches",
        "rules": [
            "Participation is voluntary, always " + EM + " never tracked, and never tied to reviews, advancement, or pay.",
            "The values-based edition is the company-wide default; the faith-based edition is an opt-in track, never a requirement.",
            "Every role and every belief in the building is treated with honor. This forms a workplace; it never filters one.",
            "Company time, company cost. Formation is an investment the company makes, not an extraction it performs.",
            "When in doubt, ask HR counsel first and proceed with a clear yes.",
        ],
    },
]

JOURNEYS_META = {
    "eyebrow": "Campaigns & Journeys",
    "head_a": "Every journey, ", "head_em": "outlined to the day.",
    "intro": ("The format is the length; the framework is the content; the rhythm is the workday. Every journey "
              "below runs Monday to Friday " + EM + " a two-minute reading to open the day, one table "
              "conversation a week, nothing on the weekend. Forty days is eight working weeks. Tap any journey "
              "to open its full outline."),
    "rhythm": ("The annual rhythm most companies settle into: one forty-day campaign, two sprints, both "
               "assessments " + EM + " and a subscription that makes the whole library theirs."),
}

# Each journey: id, name, spine, price, buyer, body, weeks: [(week label, theme, [day titles])]
JOURNEYS = [
    {
        "id": "j10", "name": "10-Day Company Sprint", "spine": "The Purpose Sprint",
        "price": "$4,500\u2013$12,000", "buyer": "CHRO or VP of People",
        "body": "Two working weeks. A fast, visible culture signal " + EM + " the whole company touches one theme together, and it is over before skepticism organizes.",
        "weeks": [
            ("Week 1", "Why We Exist", [
                "The Question Behind the Work",
                "More Than a Paycheck",
                "Who We Serve",
                "What We Refuse to Do",
                "The Story So Far",
            ]),
            ("Week 2", "How We Work", [
                "Craft as Character",
                "The People Beside You",
                "Truth in the Room",
                "Generous by Design",
                "The Commitment We Keep",
            ]),
        ],
    },
    {
        "id": "j21", "name": "21-Day Team Challenge", "spine": "The Monday Habits",
        "price": "$4,500\u2013$12,000", "buyer": "Department heads",
        "body": "Four working weeks and a capstone day. One habit per week, practiced where the work actually happens, with a demonstrable shift inside thirty days.",
        "weeks": [
            ("Week 1", "Presence", [
                "Show Up Whole",
                "The First Ten Minutes",
                "Work as Offering",
                "The Pause Before the Send",
                "End the Day Honestly",
            ]),
            ("Week 2", "Excellence", [
                "Do It Right the First Time",
                "The Detail Nobody Sees",
                "Finish What You Start",
                "Ask the Better Question",
                "Sign Your Work",
            ]),
            ("Week 3", "Care", [
                "Learn One Name's Story",
                "The Encouragement Economy",
                "Disagree Face to Face",
                "Carry Someone's Friday",
                "Celebrate Out Loud",
            ]),
            ("Week 4", "Generosity", [
                "Give Credit Away",
                "The Open Hand at Work",
                "Serve Someone Junior",
                "Fair When It Costs",
                "Leave It Better",
            ]),
            ("Day 21", "The Commitment", [
                "The Habit Each Person Keeps " + EM + " named out loud, kept in writing",
            ]),
        ],
    },
    {
        "id": "j30", "name": "30-Day Team Journey", "spine": "The Flourishing Journey",
        "price": "$9,000\u2013$25,000", "buyer": "CHRO or CLO",
        "body": "Six working weeks on the six Flourishing criteria " + EM + " one criterion per week " + EM + " with the Flourishing Workplace Assessment run before and after, so the change is measured, not asserted.",
        "weeks": [
            ("Week 1", "Flourishing with God", [
                "Work on Purpose",
                "The Sacred Ordinary",
                "Conviction in the Decision",
                "A Pause That Belongs to You",
                "Whose Approval Matters",
            ]),
            ("Week 2", "Flourishing Together", [
                "Known, Not Just Staffed",
                "The First-Month Welcome",
                "Conflict, Early and Kind",
                "Wins Worth Sharing",
                "The Table at Work",
            ]),
            ("Week 3", "Flourishing from Within", [
                "Character on the Clock",
                "Wellbeing Before Workload",
                "Rest Is a Skill",
                "Feedback That Travels Up",
                "The Person You Are Becoming Here",
            ]),
            ("Week 4", "Flourishing through Contribution", [
                "Who Your Work Serves",
                "Excellence as Integrity",
                "Strengths in the Right Seat",
                "Honor the Craft",
                "The Work Only You Can Do",
            ]),
            ("Week 5", "Flourishing for Others", [
                "The Community Outside the Walls",
                "Generosity with a Budget Line",
                "Fair When It Costs Us",
                "Vendors and Neighbors",
                "Impact You Can Name",
            ]),
            ("Week 6", "Flourishing Across Generations", [
                "The Mentor and the Mentee",
                "Building Your Replacement",
                "What Outlasts the Founder",
                "The Story New People Join",
                "The Flourishing Commitment",
            ]),
        ],
    },
    {
        "id": "j40", "name": "40-Day Company Campaign", "spine": "Purpose Built " + EM + " the Flagship Forty",
        "price": "$18,000\u2013$60,000", "buyer": "CEO and CHRO",
        "body": "Eight working weeks. The five purposes carried into the company, framed by the argument at the front and the practices and commitment at the back " + EM + " the full campaign architecture, from the loading dock to the corner office.",
        "weeks": [
            ("Week 1", "The Argument " + EM + " Work Matters", [
                "The First Job Ever Given",
                "Fifty Hours of Meaning",
                "More Than Monday Survival",
                "The Company as a Calling",
                "Why We Are Doing This Together",
            ]),
            ("Week 2", "Worship " + EM + " Work as Offering", [
                "Excellence as Devotion",
                "Integrity When No One Checks",
                "The Craft and the Creator",
                "An Audience of One",
                "Offering the Ordinary",
            ]),
            ("Week 3", "Fellowship " + EM + " Known at Work", [
                "Belonging on Purpose",
                "The Person Behind the Role",
                "Eating Together Still Works",
                "Carrying One Another's Load",
                "The Culture We Keep",
            ]),
            ("Week 4", "Discipleship " + EM + " Growth on Purpose", [
                "Character as a KPI",
                "The Feedback That Forms Us",
                "Learning Out Loud",
                "The Habit Audit",
                "Who Is Building You",
            ]),
            ("Week 5", "Ministry " + EM + " Serving Through the Work", [
                "Every Role Serves Someone",
                "The Customer as Neighbor",
                "Problems Worth Solving",
                "Service Beyond the Job Description",
                "The Ministry of Competence",
            ]),
            ("Week 6", "Mission " + EM + " Sent from Here", [
                "The Company as a Sent Thing",
                "Generosity in the Budget",
                "The City Around the Building",
                "Witness Without a Script",
                "Impact, Measured and Told",
            ]),
            ("Week 7", "The Practices", [
                "The Weekly Table",
                "Prayer, Voluntary and Real",
                "The Encouragement Rhythm",
                "Rest as Policy",
                "The Story Capture",
            ]),
            ("Week 8", "The Commitment", [
                "What We Now Believe About Work",
                "The Values That Will Cost Us",
                "Each Person's One Thing",
                "The Company's One Thing",
                "Commissioning Day",
            ]),
        ],
    },
]

ROSTER = {
    "head": "The campaign roster " + EM + " pulled over, one heading",
    "intro": ("Every major campaign and framework built for the marketplace, the workplace, or the business, "
              "gathered under this roof. Each carries its door and its status honestly."),
    "rows": [
        ("Purpose Built " + EM + " the Flagship Forty", "40 days \u00b7 8 work-weeks", "Company door \u00b7 Outlined above", "The company-wide campaign; full outline in the journey drawer above."),
        ("Purpose at Work", "40 days \u00b7 church rhythm", "Church door \u00b7 Worked package", "The churchwide campaign, with the overview sermon Monday Is the Mission Field already built."),
        ("The Flourishing Workplace", "6 weeks", "Both doors \u00b7 Built framework", "The six criteria; runs as the 30-Day Team Journey in the company and as a study series in the church."),
        ("Purpose Based Business", "5 weeks", "Company door \u00b7 Built framework", "The five purposes in marketplace language; carried inside the flagship forty as weeks two through six."),
        ("Faith at Work", "4 weeks", "Both doors \u00b7 Built framework", "The on-ramp " + EM + " short enough for a skeptical first group, sturdy enough to launch the ministry."),
        ("The Monday Habits", "21 days", "Company door \u00b7 Outlined above", "Habit formation by week: presence, excellence, care, generosity, and the commitment day."),
        ("The Purpose Sprint", "10 days", "Company door \u00b7 Outlined above", "The smallest yes " + EM + " two weeks, whole company, over before skepticism organizes."),
        ("The Owner's Peer Group", "10 studies", "Both doors \u00b7 Recovered library", "The formation spine for peer rooms " + EM + " the full directory sits in the Three Seats section."),
        ("40 Days of Movement", "40 days \u00b7 custom", "Company door \u00b7 Prospective concept", "The anchor-shaped custom campaign matched to Movement Mortgage on the partner roster. A concept until an anchor says yes."),
        ("God Owns It All " + EM + " Owner's Edition", "Study series", "Both doors \u00b7 Rights pending", "The Ron Blue line applied to an enterprise; offered only once the RBI license is confirmed."),
    ],
    "note": ("And behind the named roster: every one of the 165 library categories can run in any of these "
             "formats. The roster is the front row, not the building."),
}

FOUNDING = {
    "eyebrow": "The Founding 25 \u00b7 Proposed",
    "head_a": "Twenty-five leaders ", "head_em": "walk it into work.",
    "argument": [
        ("The single critical gap in this vertical is a named anchor " + EM + " one company that ran forty days "
         "and will say so. There are two ways to close it. Hunt one whale, or recruit twenty-five founders and "
         "close it twenty-five times in parallel."),
        ("The Founding 25 is the second way: Christian business leaders who adopt the 40-day campaign into the "
         "company they steward " + EM + " fully customized on the fixed spine, with both editions in hand. The "
         "values-based edition runs company-wide; the faith-based edition is the voluntary track. That pairing "
         "is what makes the door walkable: legal-shaped and love-shaped at the same time."),
        ("Owners trust owners. Twenty-five founders telling their own story at their own peer tables is a "
         "distribution channel no license can buy " + EM + " and every one of them arrives as a case study "
         "wearing a purchase order."),
    ],
    "gives_head": "What a Founding 25 leader receives",
    "gives": [
        "Full customization included " + EM + " your company's name, stories, and language on the fixed spine.",
        "Both editions built for you " + EM + " values-based company-wide, faith-based as the opt-in track.",
        "The founding rate: the flagship forty at half the proposed floor " + EM + " $9,000 in year one, both editions and customization included, locked for three years.",
        "A direct line to the build team; your content requests move first.",
        "Named permanently as a Founding 25 company.",
    ],
    "asks_head": "What we ask " + EM + " and only this",
    "asks": [
        "Actually run it: one sprint and one forty inside twelve months.",
        "One honest twenty-minute call each quarter.",
        "One approved case study " + EM + " only if it works.",
        "Two peer introductions " + EM + " only if it is working, never as a condition.",
    ],
    "math": ("The honest math: twenty-five founders at the founding rate does not fund a business. It funds the "
             "answer " + EM + " and it produces the twenty-five anchor stories that are, at this moment, the "
             "entire gap."),
    "toggle_head": "One week, two voices " + EM + " see the editions live",
    "toggle_note": ("Same architecture, same days, different depth of language. This is Week 2 of the flagship "
                    "forty in both editions " + EM + " the values-based edition runs company-wide; the "
                    "faith-based edition is the voluntary opt-in track."),
    "editions": {
        "faith": {
            "label": "Faith-Based Edition",
            "week": "Week 2 \u00b7 Worship " + EM + " Work as Offering",
            "days": [
                "Excellence as Devotion",
                "Integrity When No One Checks",
                "The Craft and the Creator",
                "An Audience of One",
                "Offering the Ordinary",
            ],
        },
        "values": {
            "label": "Values-Based Edition",
            "week": "Week 2 \u00b7 Craft " + EM + " Work Worth Doing Well",
            "days": [
                "Excellence as Identity",
                "Integrity When No One Checks",
                "The Craft and the Standard",
                "Work Worth Signing",
                "The Ordinary Done Well",
            ],
        },
    },
}
