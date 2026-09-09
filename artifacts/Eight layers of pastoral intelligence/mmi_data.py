# -*- coding: utf-8 -*-
# Marketplace Ministry Intelligence — content data
# The church door of the marketplace vertical. Sibling to Church Financial Health / Church Growth.

META = {
    "eyebrow": "LifeTogether Intelligence Platform · The Church Door",
    "title": "Marketplace Ministry Intelligence",
    "tm": "\u2122",
    "subtitle": "Discipling your congregation for the fifty hours you never see.",
    "status_chip": "Concept \u2014 configured from the Ministry Intelligence engine",
}

AUDIENCES = [
    {
        "id": "sp", "label": "Senior Pastor",
        "text": ("Your people spend more waking hours at work than anywhere else, and almost none of your "
                 "teaching, prayer, or pastoral care follows them there. This is not another program. It is a "
                 "ministry category \u2014 the way Men's Ministry or Recovery is a category \u2014 built on the conviction "
                 "that the marketplace is not where your people leave ministry. It is one of the primary places "
                 "they do it. Sunday equips Monday."),
    },
    {
        "id": "xp", "label": "Executive Pastor",
        "text": ("What this costs to run: one volunteer marketplace leader, one campaign a year, one to three "
                 "affinity groups, and a diagnostic your staff can score in ten minutes. What exists already: a "
                 "worked 40-day campaign, built frameworks, and study editions configured from the core library. "
                 "What to measure: the leading indicators in Domain Six \u2014 because workplace fruit arrives on a "
                 "career timeline, not a semester timeline."),
    },
    {
        "id": "ml", "label": "Marketplace Leader",
        "text": ("You are the bridge person \u2014 the one who already believes Monday matters and wonders why the "
                 "church calendar doesn't. This platform gives you the map: a diagnostic that names what your "
                 "church is missing, three seats to build for (employees, leaders, owners), starter studies that "
                 "won't lose a new group, and a story engine that brings Monday back into the room on Sunday."),
    },
    {
        "id": "bo", "label": "Business Owner",
        "text": ("You are asked to fund every ministry in the church. This is the first one built for you. Not to "
                 "reach your wallet \u2014 to shepherd your ownership: the loneliness of the chair, leading people "
                 "biblically, generosity through the business rather than after it, and the succession conversation "
                 "that should happen long before a letter of intent. What you share here is never sales "
                 "intelligence. Ever."),
    },
]

OVERVIEW = {
    "hours_left_num": "3",
    "hours_left_label": "hours a week your church sees its people",
    "hours_right_num": "50",
    "hours_right_label": "hours a week their workplace sees them",
    "insight_head": "The structural insight",
    "insight_line": "A church that affirms work and a church that equips for it are not the same thing.",
    "insight_body": ("Most churches bless work from the platform once a year and equip for it never. The "
                     "affirmation is sincere. It is also the end of the strategy. Meanwhile the congregation's "
                     "largest unreached mission field is the one its own members already occupy forty hours a "
                     "week \u2014 with full-time access no missionary will ever be granted."),
    "map_line": ("Most churches can name their missionaries overseas and cannot name the ten largest employers "
                 "of their own members."),
    "pair_head": "Intelligence \u2192 Formation",
    "pair_body": ("Like every platform in this family, it comes as a pair. The diagnostic tells a church whether "
                  "it actually disciples anyone for Monday \u2014 and where the gap is. The formation library fixes "
                  "what the diagnostic finds: a churchwide campaign, studies by seat, an owners' table, and a "
                  "measurement rhythm honest enough to admit what it cannot see."),
}

TWO_DOORS = {
    "head": "One engine. Two doors. Never confused.",
    "church": {
        "label": "The Church Door",
        "name": "Marketplace Ministry",
        "body": ("This platform. Sold to churches. A ministry category the local church runs \u2014 formation for "
                 "the congregation's Monday. Formation language, pastoral economics, the church price list."),
        "tag": "This page",
    },
    "company": {
        "label": "The Company Door",
        "name": "Marketplace Intelligence\u2122",
        "body": ("The training catalog a business buys: 165 categories, 2,025 titles, scaling from 10 to 1,000 "
                 "employees, capable of Christian, values-based, or secular voice. Outcomes language, corporate "
                 "economics, its own price list."),
        "tag": "Separate price list",
    },
    "rule": ("Same engine underneath. Different buyer, different voice, different door. The church door never "
             "sells the company door \u2014 it earns it."),
}

INTEGRATION = [
    ("The Profile", "Reads the Church Intelligence Profile before it produces anything \u2014 one profile, written once, read by everything."),
    ("The Engine", "Configured from Ministry Intelligence, inheriting its two newest dimensions: the Household and the Deferred Outcome. The workplace is invisible to the church the way the household is invisible to student ministry \u2014 and the outcome shows up in a career, not a semester."),
    ("Great Commission", "Mission Through Vocation wires into Great Commission Intelligence \u2014 the Go verb, practiced fifty hours a week."),
    ("Christian Life", "The member's private entry point stays private. Christian Life Intelligence belongs to the person who takes it."),
    ("The Story Engine", "The forward-looking question gathers Monday stories weeks before the sermon that needs them."),
]

RULES = [
    ("The church door never sells the company door.",
     "Company training conversations are owner-initiated, happen off campus, and live on a separate price list. A ministry that becomes a funnel stops being a ministry."),
    ("Nothing shared in ministry becomes sales intelligence.",
     "What an owner or employee discloses in formation is confidential, permission-based, and never used to advance a sale. Written into the system, not optional."),
    ("Never run marketplace formation and a fundraising ask in the same six weeks.",
     "Ninety days minimum between them. The moment formation feels like a setup, both die."),
    ("Commission publicly, shepherd privately.",
     "Send workers with the whole church watching. Care for their struggles where nobody is."),
    ("The owner is a sheep, not a segment.",
     "Owners enter through ordinary formation like everyone else. The owners' table is pastoral care, not a prospect list."),
    ("Measure leading indicators. Never claim outcomes you cannot see.",
     "Stories captured, people prayed for by name, groups running, mentoring pairs \u2014 honest evidence, honestly reported."),
]

DOMAINS = [
    {
        "num": "01", "name": "Theology of Work",
        "q": "Does this church teach a doctrine of vocation?",
        "body": ("Work appears on page one of the Bible, before the fall \u2014 and in most churches it never appears "
                 "in the pulpit at all. This domain measures whether the congregation has actually been taught "
                 "that ordinary work matters to God, or has merely inferred that it funds the things that do."),
        "subs": ["Work as worship", "Calling beyond clergy", "The goodness of ordinary work", "Excellence and profit", "Rest and sabbath", "Work in the biblical story"],
        "tools": ["Six-week vocation pulpit series map", "Vocation Scripture spine", "Teaching brief: work before the fall", "The Labor-Day-plus calendar"],
        "floor": "Work is taught from the pulpit at least once a year \u2014 a full message, not a Labor Day nod.",
        "line": "If work only appears in the announcements, the congregation learns it does not appear in the gospel.",
    },
    {
        "num": "02", "name": "Commissioning & Identity",
        "q": "Are workers sent as ministers, or thanked as volunteers?",
        "body": ("Every-member-a-minister is preached everywhere and practiced almost nowhere. The test is not the "
                 "slogan; it is whether anyone has ever been publicly sent to a workplace the way teams are sent "
                 "on mission trips \u2014 and whether members carry an identity at work deeper than a job title."),
        "subs": ["Every member a minister, made real", "Commissioning moments", "Workplace testimony", "Identity beyond the title", "The new-job blessing"],
        "tools": ["Workplace commissioning liturgy", "This Is My Mission Field Sunday", "Testimony capture protocol", "New-job and retirement blessing rhythm"],
        "floor": "The church has publicly commissioned someone to a workplace \u2014 not only to a mission trip.",
        "line": "We lay hands on the team going to Kenya for ten days and say nothing to the nurse going to the hospital for thirty years.",
    },
    {
        "num": "03", "name": "Formation for Monday",
        "q": "Does a pathway exist from Sunday to Tuesday?",
        "body": ("A sermon on calling with no group behind it is a compliment, not a ministry. This domain measures "
                 "the pathway: marketplace groups, studies matched to the three seats, a devotional rhythm that "
                 "reaches the desk, and mentoring that pairs gray hair with ambition."),
        "subs": ["Marketplace affinity groups", "Studies by seat", "The six-day Monday devotional", "Mentoring pairs", "The starter-study rule"],
        "tools": ["Marketplace group launch kit", "Seat selector", "Six-day devotional arc", "Monthly leaders' table"],
        "floor": "At least one marketplace-affinity group is running.",
        "line": "A sermon on calling with no group behind it is a compliment, not a ministry.",
    },
    {
        "num": "04", "name": "The Owners",
        "q": "Does anyone pastor the owners as owners?",
        "body": ("Business owners are the most solicited and least shepherded people in most churches \u2014 asked to "
                 "fund every ministry and offered none of their own. Ownership is a distinct discipleship terrain: "
                 "the loneliness of the chair, payroll pressure, succession, and the one conversation that must "
                 "happen before the letter of intent."),
        "subs": ["Ownership as stewardship", "The loneliness of the chair", "Succession before the sale", "Generosity through the business", "The family in the business"],
        "tools": ["The Owners' Table (shepherded peer circle)", "Pre-exit conversation guide", "Succession readiness check", "Owner care rhythm"],
        "floor": "Owners are known by name and shepherded \u2014 not only solicited.",
        "line": "Business owners are asked to fund every ministry in the church and offered none of their own.",
    },
    {
        "num": "05", "name": "Mission Through Vocation",
        "q": "Where has God already deployed this congregation?",
        "body": ("Your church already has full-time workers embedded in dozens or hundreds of companies, schools, "
                 "hospitals, and job sites \u2014 with relational access no outreach event will ever buy. This domain "
                 "measures whether anyone has mapped that deployment and equipped it for natural witness and "
                 "service through skill."),
        "subs": ["The congregation deployment map", "Witness without a script", "Service through skill", "Industry prayer", "City presence", "Great Commission wiring"],
        "tools": ["Deployment map: the ten-largest-employers exercise", "Vocational skills registry", "Workplace prayer directory", "Adopt-an-industry model"],
        "floor": "The church can name the ten largest employers of its own members.",
        "line": "Your church already has full-time workers in two hundred companies. Nobody has a map.",
    },
    {
        "num": "06", "name": "The Deferred Outcome",
        "q": "How would we know if any of this worked?",
        "body": ("Workplace fruit ripens on a career timeline, and the context is invisible to the church \u2014 which "
                 "is why most churches measure nothing here and quietly conclude nothing happened. The honest "
                 "answer is leading indicators: stories captured with permission, people prayed for by name, "
                 "groups running, pairs meeting."),
        "subs": ["Leading indicators", "Story capture with permission", "The invisible context", "The 90-day callback", "Honest reporting"],
        "tools": ["Monday story engine with the forward-looking question", "Leading-indicator set", "90-day campaign callback", "Annual marketplace review"],
        "floor": "At least one captured, permissioned workplace story per quarter.",
        "line": "Workplace fruit ripens in careers, not semesters. Measure leading indicators or you will measure nothing.",
    },
]

DIAG_INTRO = {
    "purpose": ("Twelve questions, scored out of 48, answerable by a senior pastor and executive pastor together "
                "in about ten minutes. It does not measure whether your people work \u2014 they do. It measures "
                "whether your church has ever built anything for the fifty hours it never sees."),
    "confidential": ("Answers belong to the church. Nothing entered here is stored, transmitted, or used as "
                     "sales intelligence."),
}

# Each question: text, then 4 options as (label, points) in ascending order 0/1/2/4
DIAGNOSTIC = [
    ("When did work last receive a full message from your pulpit \u2014 not a mention?",
     [("Never, or nobody can recall", 0), ("A Labor Day nod", 1), ("One full message in the last two years", 2), ("A series in the last two years", 4)]),
    ("Could a typical member say how their Tuesday matters to God \u2014 without mentioning giving or inviting?",
     [("Honestly, no", 0), ("A few could", 1), ("We have taught it once", 2), ("It is common language here", 4)]),
    ("Have you ever publicly commissioned someone to a workplace?",
     [("Never", 0), ("We honor professions occasionally", 1), ("Once", 2), ("It is a rhythm here", 4)]),
    ("Does any group or class exist specifically for marketplace life?",
     [("None", 0), ("It surfaces inside other groups", 1), ("One exists", 2), ("Groups exist by seat: employees, leaders, owners", 4)]),
    ("Could you name the ten largest employers of your own congregation?",
     [("No idea", 0), ("Could guess three", 1), ("We gathered it once", 2), ("We keep a deployment map", 4)]),
    ("Are business owners pastored as owners \u2014 not only asked as donors?",
     [("Honestly, mostly asked", 0), ("Known, but not gathered", 1), ("An informal circle exists", 2), ("A shepherded owners' table meets", 4)]),
    ("Has anyone here talked with an owner about succession or a sale before it happened?",
     [("Never", 0), ("Only after the fact", 1), ("Once or twice", 2), ("It is part of how we care for owners", 4)]),
    ("Are people prayed for by name for work situations?",
     [("Rarely", 0), ("In a crisis", 1), ("Sometimes, in groups", 2), ("A workplace prayer rhythm exists", 4)]),
    ("Does Sunday's content reach Monday \u2014 a devotional, a next step, a practice?",
     [("No", 0), ("Occasionally", 1), ("During campaigns", 2), ("Weekly", 4)]),
    ("Is anyone taught to lead and manage people biblically?",
     [("No", 0), ("We point to books", 1), ("An occasional event", 2), ("A leader track runs", 4)]),
    ("Are members equipped for natural witness and service through their vocation \u2014 beyond inviting to church?",
     [("No", 0), ("We encourage inviting", 1), ("We have taught it", 2), ("Trained, and practicing", 4)]),
    ("Do you have any evidence of workplace fruit?",
     [("None \u2014 it is invisible to us", 0), ("Anecdotes", 1), ("We capture stories sometimes", 2), ("Leading indicators, reviewed annually", 4)]),
]

BANDS = [
    (0, 14, "The Sunday Church",
     "Work is invisible between the benediction and the next gathering. Begin with Domain One \u2014 one series on vocation changes the temperature before any structure exists."),
    (15, 26, "Blessed, Not Equipped",
     "Work is affirmed from the platform and unsupported everywhere else. This is the most common band in the church \u2014 sincere affirmation standing in for a strategy. The fastest move: one marketplace group and one commissioning Sunday."),
    (27, 38, "Equipping for Monday",
     "Pathways exist. The gaps are almost always the same two: nobody pastors the owners, and nothing is measured. Domains Four and Six are your next year."),
    (39, 48, "Commissioned & Multiplying",
     "Workers are sent, owners are shepherded, and stories are coming back into the room. Your work now is multiplication \u2014 train marketplace leaders who build this in other churches."),
]

DISCERNMENT = [
    ("Impact", "Where would movement matter most in the next twelve months?"),
    ("Urgency", "Which gap is costing you people \u2014 or costing an owner \u2014 right now?"),
    ("Invitation", "Where is God already stirring this? A person, a story, an owner who has started asking questions."),
]

SEATS = [
    {
        "id": "employee", "label": "The Employee",
        "q": "How do I follow Jesus at work?",
        "who": ("The nurse, the teacher, the coder, the foreman, the analyst. The vast majority of the "
                "congregation \u2014 and the seat every other seat depends on."),
        "path": [
            ("Starter", "Purpose at Work \u2014 the 40-day campaign, or Faith at Work as a four-week on-ramp"),
            ("Deeper", "Core studies in the Marketplace edition \u2014 same theology, examples set at the desk and the job site"),
            ("Group", "A marketplace group or industry table \u2014 people who understand the pressure without a translation"),
            ("Next step", "Commissioning \u2014 and a story captured for the church that sent them"),
        ],
    },
    {
        "id": "leader", "label": "The Leader",
        "q": "How do I lead people and culture biblically?",
        "who": ("Managers, executives, principals, charge nurses, site supervisors \u2014 anyone responsible for other "
                "people's work and, whether they know it or not, other people's flourishing."),
        "path": [
            ("Starter", "A leading-people study in the Leaders edition \u2014 management as shepherding"),
            ("Deeper", "The Flourishing Workplace \u2014 six weeks, strongest when run with their own team"),
            ("Group", "A monthly leaders' table \u2014 peers carrying the same weight"),
            ("Next step", "Mentor one emerging leader \u2014 the pipeline is the point"),
        ],
    },
    {
        "id": "owner", "label": "The Owner",
        "q": "What does faithful ownership look like?",
        "who": ("Founders, franchisees, family-business owners, practice principals. The most solicited and least "
                "shepherded seat in the church \u2014 and the one person who will eventually cross every door in "
                "this vertical."),
        "path": [
            ("Starter", "God Owns It All \u2014 Owner's Edition, where stewardship meets a balance sheet"),
            ("Deeper", "The Owners' Table \u2014 confidential, shepherded, and never a prospect list"),
            ("Group", "Succession and the pre-exit conversation \u2014 years before the letter of intent"),
            ("Next step", "The Owner's Journey \u2014 the tab that follows this one"),
        ],
    },
]

SEAT_NOTE = ("An edition changes examples, pace, and questions \u2014 never the theology or the structure. Three "
             "seats, one gospel.")

FORMATION_INTRO = ("Nothing below was invented for this page. Every track is a built framework, a worked package, "
                   "or a configuration of the core library \u2014 which is why this vertical costs a configuration, "
                   "not a platform. Status labels are honest.")

TRACKS = [
    ("Purpose at Work", "The 40-day churchwide campaign. Overview sermon already worked: Monday Is the Mission Field \u2014 big idea, four movements, seven-day devotional, group guide, and the ladder into the full campaign.", "Worked package", "Campaign"),
    ("Faith at Work", "The four-week on-ramp \u2014 short enough for a skeptical first group, sturdy enough to launch the ministry.", "Built framework", "Study"),
    ("The Flourishing Workplace", "Six weeks on culture and human flourishing. Built to be run by a leader with their own team \u2014 which is where it does its best work.", "Built framework", "Study"),
    ("Calling & Vocation", "Six sessions from the Purpose & Calling cluster \u2014 the theological foundation under everything else on this page.", "Configured", "Study"),
    ("Core Library \u2014 Marketplace Edition", "The study library in marketplace voice: examples at the desk, questions about the meeting that went wrong.", "Configured", "Edition"),
    ("Core Library \u2014 Leaders Edition", "The same library for people-leaders: culture, decisions, the weight of other people's livelihoods.", "Configured", "Edition"),
    ("Core Library \u2014 Business Owners Edition", "The same library for the chair: ownership, payroll, profit, succession.", "Configured", "Edition"),
    ("God Owns It All \u2014 Owner's Edition", "The Ron Blue line applied to an enterprise. Configuration pending rights confirmation on the RBI license \u2014 labeled honestly until it is.", "Configured \u00b7 rights pending", "Edition"),
]

DEVO = {
    "head": "The six-day Monday arc",
    "body": "Sunday is the sermon; Monday through Saturday belong to it \u2014 delivered to the desk, under two minutes a day.",
    "days": [
        ("Mon", "The hook again \u2014 at your desk this time"),
        ("Tue", "The text"),
        ("Wed", "The honest part \u2014 the meeting that went wrong"),
        ("Thu", "The practice"),
        ("Fri", "The person \u2014 who at work needs what you heard Sunday"),
        ("Sat", "Bring it back"),
    ],
}

STORY = {
    "head": "The story engine, pointed at Monday",
    "body": ("Three weeks before the Purpose at Work series, the devotional asks the forward-looking question: "
             "Where have you seen God in your work? The pastor opens the series with a story from row twelve "
             "about the exact thing he is about to teach. Permission protocol applies in full \u2014 three naming "
             "options, ask once, show the edit, and a reply from someone in crisis is never source material."),
}

SERMON_MAP = {
    "head": "Sermon library mapping",
    "body": ("The 5,155-title sermon library will be pulled for this vertical the way it was for Financial "
             "Health: work and calling, purpose, integrity, leadership, and generosity-at-work categories mapped "
             "with real counts. Counts pending the library pull \u2014 stated honestly rather than estimated."),
}

JOURNEY_INTRO = ("The business owner is the one person who crosses every door in this ecosystem \u2014 which is why "
                 "this vertical matters beyond its own revenue. Six stages. The integrity rules travel with them.")

JOURNEY = [
    ("1", "Discipled", "The owner sits in ordinary formation first \u2014 a sheep before a segment. The church door treats ownership as a discipleship terrain, not a giving capacity."),
    ("2", "Leading", "The Owners' Table and the Leaders track: leading their own people biblically, carrying the chair with peers who understand it."),
    ("3", "Training the Company", "The company door opens \u2014 Marketplace Intelligence\u2122 for their business. Owner-initiated, off campus, off the church price list. The church door never sells it; it earns it."),
    ("4", "Generous Through the Business", "God Owns It All and the Journey of Generosity: giving as an operating value of the enterprise, not an event at its end."),
    ("5", "The Exit", "The asset track: give before you sell, the advisor liaison, and the pre-exit question \u2014 the one conversation that must happen before the letter of intent."),
    ("6", "Legacy", "Family Legacy Ministry and the advisor stack: the family, the story, the next generation. The marketplace vertical hands the owner to the legacy vertical it was always connected to."),
]

PRICING_INTRO = ("Proposed, not validated \u2014 mirroring the Financial Wisdom precedent so the ladder stays "
                 "coherent. Attendance is the only variable, seats are unlimited everywhere, and the company "
                 "door prices on its own list.")

PRICING = [
    ("Campaign only", "Purpose at Work as a standalone churchwide campaign, priced on the standard campaign ladder by attendance.",
     [("Under 250", "$590"), ("250\u20131,000", "$1,190"), ("1,000\u20132,500", "$1,990"), ("Over 2,500", "$2,890")]),
    ("Full Marketplace Ministry", "Campaign + all study editions + the diagnostic + the Owners' Table materials + leader training + the story engine. Flat, like Financial Wisdom's full ministry.",
     [("All sizes", "$3,900 / yr")]),
    ("Inside the bundle", "Slots into All-Access plus Ministry as a third full programme beside Financial Wisdom and Family Legacy. Bundle repricing to be ruled before anything ships.",
     [("Status", "To be ruled")]),
]

STATUS = [
    ("Platform status", "Concept \u2014 a configuration of built assets, not a new build. The diagnostic, domains, seats, and journey on this page are drafted to the family standard and unreviewed by a real church."),
    ("Pricing", "Proposed and unvalidated. Every number is reasoned from the existing ladder, none tested with a buyer."),
    ("Sermon counts", "Pending the library pull. No counts are estimated on this page."),
    ("Rights", "God Owns It All \u2014 Owner's Edition requires RBI license confirmation before it is offered."),
    ("Naming", "The Purpose Driven Business / Purpose Built boundary in the marketplace lane remains open and is deliberately not resolved here. This page uses neither name."),
    ("The company door", "Marketplace Intelligence\u2122 (165 categories / 2,025 titles) is referenced, never sold, on this page. Its economics live on a separate list."),
]

FOOTER = "Marketplace Ministry Intelligence \u00b7 The Church Door \u00b7 LifeTogether Intelligence Platform \u00b7 Sunday Equips Monday"
