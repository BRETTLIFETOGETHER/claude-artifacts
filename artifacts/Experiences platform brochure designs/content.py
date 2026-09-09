# -*- coding: utf-8 -*-
# Shared content for Whole-Church Formation(TM) brochure — both design versions
# pull from the same data so copy never drifts between editions.

TITLE = "Whole-Church Formation\u2122"
KICKER = "The Next Generation of Churchwide Discipleship"
SUBHEAD = "A Comprehensive Churchwide Discipleship Process, Program, and Plan"

OPENING_LEAD = [
    "Most churches are rich in biblical teaching.",
    "They have gifted pastors, faithful leaders, inspiring sermons, committed volunteers, thriving ministries, and a genuine desire to make disciples.",
]
OPENING_QUESTION = "How do we intentionally connect everything we do into one unified process that helps people become fully devoted followers of Jesus?"
FRAGMENTED_MINISTRIES = [
    "Weekend messages", "Small groups", "Men\u2019s ministry", "Women\u2019s ministry",
    "Students", "Children", "Marriage", "Parents", "Financial stewardship",
    "Serving", "Leadership", "Mission",
]
OPENING_RESULT = [
    "Often these ministries are effective individually, but disconnected collectively.",
    "The result is good ministry\u2014but fragmented discipleship.",
]

WHAT_IS = {
    "eyebrow": "Definition",
    "title": "What Is Whole-Church Formation\u2122?",
    "body": [
        "Whole-Church Formation\u2122 is a comprehensive strategy that intentionally aligns every major ministry environment around one shared discipleship process.",
        "It transforms isolated programs into one integrated journey of spiritual growth.",
    ],
    "reframe_from": "\u201cWhat curriculum should we teach next?\u201d",
    "reframe_to": "\u201cHow are we forming the people God has entrusted to our church?\u201d",
}

# The seven formation environments — order carries no hierarchy, but the
# roman numeral treatment matches the church's own directory convention.
ENVIRONMENTS = [
    ("I", "Personal Formation", "Helping every person know God more deeply through Scripture, prayer, worship, reflection, spiritual practices, and daily obedience."),
    ("II", "Family Formation", "Helping parents disciple children, strengthen marriages, build healthy homes, and establish biblical conversations across generations."),
    ("III", "Group Formation", "Helping people experience authentic biblical community through meaningful weekly conversations and practical application."),
    ("IV", "Ministry Formation", "Helping every ministry leader confidently choose, customize, and teach experiences designed specifically for the people they serve."),
    ("V", "Leadership Formation", "Helping pastors, staff, volunteers, coaches, hosts, and ministry leaders continually grow while developing new leaders."),
    ("VI", "Churchwide Formation", "Aligning weekend teaching, ministries, families, groups, serving opportunities, digital communication, testimonies, and next steps around one shared spiritual priority."),
    ("VII", "Missional Formation", "Helping people discover their gifts, live with purpose, serve generously, share their faith, and become everyday missionaries."),
]

# The five desired outcomes
OUTCOMES = [
    ("Faith", "Knowing God. Trusting Jesus. Living by Scripture."),
    ("Formation", "Growing Christlike character through daily spiritual practices."),
    ("Family & Community", "Building healthy relationships, stronger families, and authentic biblical community."),
    ("Purpose", "Discovering gifts, calling, ministry, vocation, and God\u2019s unique purpose."),
    ("Impact", "Serving others. Living generously. Sharing faith. Changing communities."),
]

RHYTHM_INTRO = "Daily Formation. Weekly Conversation. Churchwide Transformation."
RHYTHM_SUB = "This simple framework explains how genuine spiritual transformation happens."

RHYTHM = [
    {
        "name": "Daily Formation",
        "lead": "Every participant receives a beautifully designed Daily Spiritual Growth Journey.",
        "items": ["Scripture", "Inspirational teaching", "Personal reflection", "Prayer", "Journaling", "Practical application"],
        "result": "Faith becomes part of everyday life\u2014not simply a weekend activity.",
    },
    {
        "name": "Weekly Conversation",
        "lead": "People gather together in:",
        "items": ["Small Groups", "Adult Bible Fellowships", "Sunday School Classes", "Men\u2019s Ministry", "Women\u2019s Ministry",
                   "Marriage Groups", "Parenting Groups", "Leadership Teams", "Student Ministries", "Workplace Groups", "Family Conversations"],
        "result": "Personal growth becomes relational transformation. People encourage one another, share stories, ask questions, and apply biblical truth together.",
    },
    {
        "name": "Churchwide Transformation",
        "lead": None,
        "items": ["Weekend messages", "Daily journeys", "Group conversations", "Family discussions", "Children\u2019s lessons",
                   "Student ministry", "Serving opportunities", "Digital communication", "Testimonies", "Celebration weekends"],
        "note": "All reinforce the same biblical truth.",
        "result": "The church begins moving together rather than separately.",
    },
]

# One Message, Multiple Experiences
ONE_MESSAGE_EXAMPLE = "40 Days of Prayer"
ONE_MESSAGE_EDITIONS = [
    "Personal Experience Edition", "Family Experience Edition", "Marriage Experience Edition",
    "Small Group Experience Edition", "Ministry Experience Edition", "Student Experience Edition",
    "Children\u2019s Experience Edition", "Leadership Experience Edition", "Retreat Experience Edition",
    "Churchwide Experience Edition", "Custom Church Edition",
]
ONE_MESSAGE_CLOSE = ["One biblical theme.", "One publishing system.", "Unlimited ministry applications."]

# The Multi-Edition Difference — full editions with descriptions
EDITIONS = [
    ("Personal Experience Edition", "Daily personal formation.", None),
    ("Family Experience Edition", "Helping parents disciple children through:",
     ["Family conversations", "Children\u2019s activities", "Teen discussions", "Family prayer", "Service projects", "Memory verses", "Weekly family experiences"]),
    ("Small Group Experience Edition", "Conversation guides. Leader guides. Video sessions. Weekly discussion.", None),
    ("Ministry Experience Edition", "Designed specifically for:",
     ["Men\u2019s Ministry", "Women\u2019s Ministry", "Marriage Ministry", "Parenting Ministry", "Young Adults", "Students",
      "Seniors", "Recovery", "Leadership", "Financial Ministry", "Volunteer Teams", "Adult Bible Fellowships"]),
    ("Churchwide Experience Edition", "One church. One message. One unified journey.", None),
    ("Retreat Experience Edition", "Weekend experiences.",
     ["Leadership retreats", "Marriage retreats", "Prayer retreats", "Family retreats"]),
    ("Leadership Experience Edition", "Developing pastors, staff, coaches, hosts, elders, and ministry leaders.", None),
]

MULTI_EDITION_LEAD = [
    "This is what makes LifeTogether fundamentally different.",
    "Most curriculum publishers create one product.",
    "LifeTogether creates an entire ecosystem.",
]

# Choose the Right Experience — length ladder, shortest to longest.
# Order here is meaningful (duration), so the ladder / numbering is earned.
EXPERIENCES = [
    {
        "name": "Catalyst Sundays\u2122", "length": "1 Sunday",
        "tag": "One Message. One Moment. One Meaningful Next Step.",
        "fits": ["Vision Sundays", "Prayer Sundays", "Stewardship Sundays", "Easter Preparation", "Fall Launch",
                 "Small Group Launch", "Volunteer Recruitment"],
    },
    {
        "name": "7-Day Experiences", "length": "7 days",
        "tag": "A focused spiritual reset.",
        "fits": ["Prayer", "Gratitude", "Serving", "Forgiveness", "Vision", "Easter", "Christmas", "Generosity"],
    },
    {
        "name": "21-Day Experiences", "length": "21 days",
        "tag": "A spiritual habit builder\u2014or habit breaker.",
        "fits": ["Prayer", "Bible Reading", "Financial Wisdom", "Peace", "Faith Over Fear", "Generosity", "Identity", "Spiritual Disciplines"],
    },
    {
        "name": "30-Day Experiences", "length": "30 days",
        "tag": "Four weeks of formation. Six gatherings to build community.",
        "fits": ["Four-week sermon series", "Launching new small groups", "Existing groups", "Marriage", "Parenting",
                 "Emotional Health", "Leadership", "Financial Wisdom"],
        "flow": ["Open House", "Four Weekly Conversations", "Celebration & Next Steps"],
        "flow_note": "Content builds understanding. Community builds transformation.",
    },
    {
        "name": "40-Day Experiences", "length": "40 days",
        "tag": "The most comprehensive churchwide experience.",
        "fits": ["Church vision", "Discipleship", "Prayer", "Purpose", "Financial Wisdom", "Generosity", "Family", "Emotional Health", "Outreach"],
        "flow_note": "A complete churchwide transformation process.",
    },
]

MORE_THAN_CURRICULUM = ["LifeTogether is more than curriculum.", "More than devotionals.", "More than sermon resources.",
                         "More than campaigns.", "It is a customizable Church Formation System."]

# Two products
PRODUCTS = [
    ("Daily Spiritual Growth Journey", "A beautifully designed full-color book helping people grow every day.",
     ["Individuals", "Families", "Gift editions", "Churchwide distribution"]),
    ("Weekly Conversation Guide", "The curriculum resource for:",
     ["Groups", "Ministries", "Classes", "Leadership Teams", "Families"]),
]
PRODUCTS_NOTE = "Churches may purchase either resource independently\u2014or combine them for maximum impact."

# Customization tiers
CUSTOMIZATION = [
    ("Ready-to-Use Edition", "Launch immediately.", None),
    ("Personalized Church Edition", "Featuring:",
     ["Church branding", "Pastor introduction", "Local stories", "Custom applications", "Church ministries", "Sermon alignment"]),
    ("Pastor\u2019s Message Edition", "Transform your own sermons\u2026 Books\u2026 Teaching archives\u2026 Life message\u2026 Into a complete churchwide formation experience.", None),
    ("Fully Custom Signature Edition", "An entirely original experience professionally developed with your church or ministry.", None),
]

POD = {
    "title": "Print-on-Demand Publishing",
    "lead": "Every subscribing church receives access to a digital publishing platform.",
    "items": ["Create custom editions without maintaining inventory.", "Participants order only what they need.",
              "No warehouse.", "No minimum quantities.", "No wasted books."],
    "close": ["Professional publishing.", "Direct shipping."],
}

FINDER = {
    "title": "The Ministry Curriculum Finder\u2122",
    "lead": "Every ministry leader asks: \u201cWhat should we teach next?\u201d",
    "body": "LifeTogether helps leaders instantly discover experiences by:",
    "facets": ["Audience", "Topic", "Biblical theme", "Length", "Ministry season", "Felt need", "Teaching style", "Desired outcome"],
    "close": ["Ready to use.", "Lightly customized.", "Or completely personalized."],
}

DIFFERENCE_LEAD = ["Most churches already possess extraordinary content.", "They simply lack the publishing system to multiply its impact."]
DIFFERENCE_PAIRS = [
    ("Messages", "movements"), ("Sermons", "daily journeys"), ("Content", "conversations"),
    ("Listeners", "participants"), ("Participants", "practitioners"), ("Groups", "communities"),
    ("Families", "discipleship environments"), ("Ministries", "coordinated formation pathways"),
    ("Church initiatives", "lasting movements"),
]

IMAGINE_CHAIN = [
    "One sermon\u2026 becomes a seven-day journey.",
    "One journey\u2026 becomes a family experience.",
    "One family\u2026 joins a small group.",
    "One group\u2026 launches another.",
    "One ministry\u2026 adopts the experience.",
    "An entire church\u2026 moves together.",
]

FOOTER = {
    "system": "LifeTogether Church Formation System\u2122",
    "system_sub": "The platform that helps churches turn biblical teaching into lifelong transformation.",
    "wcf": "Whole-Church Formation\u2122",
    "wcf_sub": "Forming people of faith, character, purpose, community, and mission.",
    "experiences": "LifeTogether Experiences\u2122",
    "experiences_sub": "One Experience. Personalized for Every Person, Every Family, Every Group, Every Ministry, and Your Entire Church.",
    "rhythm": "Daily Formation. Weekly Conversation. Churchwide Transformation.",
}
