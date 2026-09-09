# -*- coding: utf-8 -*-

TITLE = "Family Legacy Intelligence"
TM = "\u2122"
SUBTITLE = "The 10-Minute Family Legacy Assessment"
DECK = ("Discover what your family has received, what it must strengthen, "
        "and what it is called to pass forward.")
AUDIENCE = "Designed for Christian Financial Advisors Serving High-Capacity Families"

PREAMBLE = ("This experience helps a family move beyond financial planning into a deeper "
            "conversation about faith, relationships, wisdom, stewardship, generosity, and "
            "multigenerational legacy. It is not intended to measure whether a family is "
            "\u201cgood\u201d or \u201cbad.\u201d It helps identify the first area of Family "
            "Legacy Intelligence" + TM + " your family may want to explore.")

INSTRUCTIONS = ("Rate each statement from 1 to 5. Answer honestly based on what is happening "
                "now \u2014 not what you hope will happen someday.")

SCALE = [
    ("1", "Not true of our family"),
    ("2", "Rarely true"),
    ("3", "Somewhat true"),
    ("4", "Mostly true"),
    ("5", "Clearly and consistently true"),
]

SECTIONS = [
    {
        "n": 1,
        "roman": "I",
        "title": "Faith and Spiritual Heritage",
        "short": "Faith and Spiritual Heritage",
        "q": "What have we received spiritually, and what are we intentionally passing forward?",
        "color": "#2B5C9B",
        "items": [
            "Our children and grandchildren understand the faith convictions that guide our family.",
            "We regularly tell stories about God\u2019s faithfulness throughout our family\u2019s history.",
            "Prayer, Scripture, worship, and spiritual conversations are natural parts of our family life.",
            "We have intentionally discussed what we hope future generations will believe about God.",
        ],
    },
    {
        "n": 2,
        "roman": "II",
        "title": "Family Story, Identity, and Values",
        "short": "Family Story, Identity, and Values",
        "q": "Does our family know who we are and what we stand for?",
        "color": "#0F7A6C",
        "items": [
            "Our family knows the important people, sacrifices, challenges, and turning points that shaped us.",
            "We can clearly name the values we want our family to represent.",
            "Our financial and lifestyle decisions generally reflect those values.",
            "Our children and grandchildren experience a meaningful sense of family identity and belonging.",
        ],
    },
    {
        "n": 3,
        "roman": "III",
        "title": "Relationships and Family Unity",
        "short": "Relationships and Family Unity",
        "q": "Are our relationships strong enough to carry the legacy we hope to leave?",
        "color": "#B85C3B",
        "items": [
            "Family members can discuss difficult subjects without withdrawing, attacking, or dividing.",
            "We have addressed \u2014 or are actively addressing \u2014 significant hurts, conflicts, and misunderstandings.",
            "Family members feel heard, respected, loved, and valued across generations.",
            "Our family knows how to disagree while protecting relationships and honoring one another.",
        ],
    },
    {
        "n": 4,
        "roman": "IV",
        "title": "Wisdom and Next-Generation Preparation",
        "short": "Wisdom and Next-Generation Preparation",
        "q": "Are we preparing our heirs for responsibility, not merely inheritance?",
        "color": "#6B4E9E",
        "items": [
            "We intentionally share the lessons we have learned through faith, work, success, failure, and adversity.",
            "Our children and grandchildren are developing the character and competence needed to steward responsibility.",
            "We have meaningful conversations about work, calling, money, generosity, leadership, and purpose.",
            "Younger family members are gradually being invited into age-appropriate family decisions and responsibilities.",
        ],
    },
    {
        "n": 5,
        "roman": "V",
        "title": "Stewardship, Wealth, and Generosity",
        "short": "Stewardship, Wealth, and Generosity",
        "q": "Do our resources serve our faith, values, family, and Kingdom purpose?",
        "color": "#A8811C",
        "items": [
            "Our family has a shared understanding that everything ultimately belongs to God.",
            "We have explained the purpose behind our wealth, property, business interests, opportunities, and influence.",
            "Our children and grandchildren are being prepared to receive resources without developing entitlement.",
            "Giving, serving, and generosity are shared family practices rather than private financial transactions.",
        ],
    },
    {
        "n": 6,
        "roman": "VI",
        "title": "Succession, Communication, and Enduring Legacy",
        "short": "Succession, Communication, and Enduring Legacy",
        "q": "Have we prepared the people as carefully as we have prepared the documents?",
        "color": "#2F6B45",
        "items": [
            "Our estate, succession, business, and charitable plans reflect our deeper values and intentions.",
            "Appropriate family members understand the general direction of our plans and the reasons behind them.",
            "We have identified the stories, beliefs, blessings, wisdom, and instructions we want preserved.",
            "We have a practical process for continuing legacy conversations across generations.",
        ],
    },
]

DISCERN_INTRO = ("Your lowest-scoring section may reveal the first layer of Family Legacy "
                 "Intelligence your family should explore. However, the lowest score is not "
                 "automatically the first priority. Consider three questions:")

QUESTIONS = [
    "Where would growth create the greatest positive impact?",
    "Which issue becomes more difficult if we continue postponing it?",
    "Where do we currently sense God inviting us to act?",
]

BANDS = [
    ("96\u2013120", "Intentional Legacy Formation",
     "Your family has established many strong legacy practices. Your next opportunity is to document, deepen, and multiply them."),
    ("72\u201395", "Emerging Legacy Alignment",
     "Important pieces are present, but greater clarity, communication, and intentionality are needed."),
    ("48\u201371", "Legacy Conversations Needed",
     "Your family has valuable stories, faith, wisdom, and resources, but much of the legacy remains undocumented or undiscussed."),
    ("24\u201347", "Begin with Trust and Discovery",
     "Start slowly. Prioritize relationships, listening, family stories, and shared values before addressing complex financial or succession decisions."),
]

# page grouping: page 1 -> sections 1-2, page 2 -> sections 3-5, page 3 -> section 6 + scoring
GROUPS = [[0, 1], [2, 3, 4], [5]]
