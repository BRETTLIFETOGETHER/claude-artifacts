# -*- coding: utf-8 -*-
# The Finances Series — 10 Tier-1 campaign titles, 40-Day / 6-Session format.
# Tone: pastoral, practical, Purpose Driven. NIV scripture. No seminary jargon.

PLATFORM = {
    "kicker": "LIFETOGETHER · THE FINANCES SERIES · COMPLETE TEN-TITLE PLATFORM",
    "title_lines": ["The", "Finances", "Series."],
    "deck": ("Ten complete 40-day campaigns and small group series for the one area "
             "of life that quietly shapes every other — built on the conviction that "
             "the way a person handles money is not a financial issue first. It is a "
             "faith issue, a freedom issue, and a heart issue."),
    "framework_label": "THE GOVERNING FRAMEWORK SENTENCE",
    "framework_sentence": (
        "Faith & Finances aligns the heart. Financial Wisdom teaches the mind. "
        "Money Made Simple clears the clutter. Financial Peace calms the worry. "
        "Wise with Money builds the skill. God, Money & Me searches the soul. "
        "Financial Health forms the habits. Breaking Financial Fear sets us free. "
        "Money and Meaning gives it all a purpose. Peace with Money ends the war. "
        "Together, they make money a servant again — never a master."),
    "intro": [
        ("Money is the most talked-about subject in the Bible after the Kingdom of God — "
         "and the most avoided subject in the average church. Jesus knew why. \u201cWhere your "
         "treasure is,\u201d He said, \u201cthere your heart will be also.\u201d Money is never only about "
         "money. It is about trust, security, identity, fear, generosity, and worship. Which is "
         "exactly why a congregation that learns to handle money God\u2019s way is a congregation "
         "that grows in nearly every other area at the same time."),
        ("The Finances Series is the church\u2019s answer to a culture drowning in debt, comparison, "
         "and quiet financial anxiety. Each title is a complete 40-day journey paired with a "
         "six-session small group experience \u2014 designed to work for one person, a married couple, "
         "a small group, an entire congregation, or a company workforce. Every campaign names a real "
         "problem people are already living with, and points to the specific transformation God offers "
         "in its place."),
        ("Each title stands alone. Together, the ten form the most complete biblical-finance "
         "discipleship platform available \u2014 a full ministry calendar that can carry a church or "
         "company from financial fear to financial freedom, one honest, hopeful season at a time."),
    ],
    "closing_title": ["Ten campaigns.", "One relationship", "with money \u2014 made new."],
    "closing_body": (
        "The Finances Series is the most complete biblical-finance discipleship platform available "
        "\u2014 ten 40-day journeys, sixty small group sessions, and a full ministry calendar that helps "
        "every person move from stress to stewardship, from fear to freedom, and from owning their "
        "money to being free to give it away."),
    "footer": ("Brett Eastman · Founder, Lifetogether · brett@lifetogether.com · "
               "The Finances Series · Ten-Title Platform"),
}

# Color themes per series. Each: dark band + matching light tint.
# (dark, deep, mid, lighttint, ink-on-tint)
THEMES = {
    "navy":    {"dark": "#162540", "deep": "#1f3357", "tint": "#eef1f6", "edge": "#c9a86a"},
    "forest":  {"dark": "#1c3326", "deep": "#274936", "tint": "#edf1ec", "edge": "#c9a86a"},
    "stone":   {"dark": "#3c3a33", "deep": "#54514733", "tint": "#f3f1ea", "edge": "#bfa468"},
    "teal":    {"dark": "#143536", "deep": "#1e4a4b", "tint": "#e9f0ef", "edge": "#cdab63"},
    "bronze":  {"dark": "#3a3119", "deep": "#574927", "tint": "#f2efe4", "edge": "#caa75f"},
    "plum":    {"dark": "#2c1f38", "deep": "#412f53", "tint": "#efeaf2", "edge": "#c9a86a"},
    "pine":    {"dark": "#13302a", "deep": "#1d473d", "tint": "#e8f0ec", "edge": "#cdab63"},
    "oxblood": {"dark": "#3a181b", "deep": "#55262a", "tint": "#f4eae9", "edge": "#caa75f"},
    "indigo":  {"dark": "#1b1f40", "deep": "#2a3057", "tint": "#ecedf5", "edge": "#c9a86a"},
    "steel":   {"dark": "#1f2c38", "deep": "#314454", "tint": "#ecf0f3", "edge": "#c9a86a"},
}

SERIES = [
    # 1 -----------------------------------------------------------------
    {
        "n": 1, "theme": "navy",
        "title": ["Faith &", "Finances"],
        "category": "TITLE ONE · WHAT YOU BELIEVE & HOW YOU SPEND",
        "band_line": ("The way you handle money is the clearest, most honest evidence of what you "
                      "actually believe \u2014 and these forty days bring Sunday faith all the way "
                      "down to Monday\u2019s spending."),
        "pull": "\u201cHow you handle money is the loudest sermon you preach about what you truly believe.\u201d",
        "body": ("Most of us keep faith and finances in separate rooms. We worship God on Sunday "
                 "and worry about money the other six days, as if the two had nothing to do with "
                 "each other. Jesus refused that separation. He talked about money more than almost "
                 "anything else, not because He wanted our wallets, but because He wanted our hearts "
                 "\u2014 and He knew our wallets reveal where our hearts already are. "
                 "Faith & Finances is the series that closes the gap. It helps every person see their "
                 "spending, saving, debt, and giving as the most practical place their faith gets "
                 "tested \u2014 and the place it can grow the fastest."),
        "scripture": ("\u201cNo one can serve two masters. Either you will hate the one and love the "
                      "other, or you will be devoted to the one and despise the other. You cannot "
                      "serve both God and money.\u201d", "Matthew 6:24 (NIV)"),
        "subtitles": [
            "A 40-Day Journey from Sunday Faith to Monday Money",
            "Discovering What Your Finances Reveal About Your Faith",
            "A 40-Day Path to Trusting God with Every Dollar",
            "Closing the Gap Between What You Believe and How You Spend",
        ],
        "bigidea": ("Money is never just money. It is one of the truest tests of faith we will ever "
                    "take \u2014 and the person who learns to trust God with their finances has learned "
                    "to trust Him with their whole life."),
        "tags": ["faith", "trust", "stewardship", "the heart", "two masters", "discipleship"],
        "info": {"Audience": "All church · all believers · any income level",
                 "Best Season": "New Year · Fall stewardship · Anytime",
                 "Why it matters": "Money is the daily arena where faith is proven or exposed"},
        "sessions": [
            {"t": ["Two Masters,", "One Heart"], "v": "\u201cYou cannot serve both God and money.\u201d \u2014 Matthew 6:24",
             "tags": ["two masters", "devotion", "the heart", "honesty"],
             "q": ["Be honest: when you think about money, what is the dominant feeling \u2014 peace, fear, control, guilt, or something else? Where does that feeling come from?",
                   "Jesus says you cannot serve both God and money. In what one area of your finances is that competition most real for you right now?",
                   "If a stranger studied only your bank statement for the last month, what would they conclude you love most?"],
             "step": ("Pull up your spending from the last 30 days. Without judgment, write down the "
                      "three things you spent the most on outside of bills. Ask God what those three "
                      "things reveal about your heart. Share one with your spiritual partner.")},
            {"t": ["What Your", "Spending Reveals"], "v": "\u201cFor where your treasure is, there your heart will be also.\u201d \u2014 Matthew 6:21",
             "tags": ["treasure", "priorities", "self-examination", "Matthew 6"],
             "q": ["Jesus connects your treasure to your heart \u2014 not the other way around. How have you seen your spending pull your heart toward something over time?",
                   "What is one thing you spend money on that you would be a little embarrassed to defend to God? What is one thing you are proud of?",
                   "If you wanted your heart to follow God more closely this year, where would your money need to go that it isn\u2019t going now?"],
             "step": ("Choose one spending category that does not reflect your stated values. Make one "
                      "specific change to it this week \u2014 and tell your partner what you changed and why.")},
            {"t": ["The God", "Who Provides"], "v": "\u201cAnd my God will meet all your needs according to the riches of his glory in Christ Jesus.\u201d \u2014 Philippians 4:19",
             "tags": ["provision", "trust", "fear", "Philippians 4"],
             "q": ["Can you name a specific time God provided for you financially in a way you did not expect? What did it teach you?",
                   "There is a difference between God meeting your needs and God funding your wants. Where do you most often confuse the two?",
                   "What need are you carrying right now that you have never actually brought to God in prayer? What has held you back?"],
             "step": ("Write down one genuine financial need on a card and put it where you\u2019ll see it "
                      "daily. Each morning this week, hand it to God in prayer before you do anything "
                      "about it yourself.")},
            {"t": ["Trust", "Over Worry"], "v": "\u201cSeek first his kingdom and his righteousness, and all these things will be given to you as well.\u201d \u2014 Matthew 6:33",
             "tags": ["worry", "kingdom first", "priorities", "trust"],
             "q": ["Jesus tells worried people to seek the Kingdom first. In practical terms, what would \u2018Kingdom first\u2019 change about how you make money decisions?",
                   "What is the financial worry that most reliably steals your sleep or your joy? Where did it begin?",
                   "What would actually change in your week if you believed \u2014 not just agreed, but believed \u2014 that God will take care of you?"],
             "step": ("Identify your single biggest money worry. Each time it surfaces this week, "
                      "answer it out loud with Matthew 6:33. Tell your partner whether anything began "
                      "to shift.")},
            {"t": ["Faithful", "in Little"], "v": "\u201cWhoever can be trusted with very little can also be trusted with much.\u201d \u2014 Luke 16:10",
             "tags": ["faithfulness", "small things", "integrity", "Luke 16"],
             "q": ["God measures faithfulness in small amounts before He entrusts large ones. Where are you being faithful with \u2018little\u2019 right now?",
                   "Is there a small financial habit \u2014 an unpaid amount, a rounding-up, a quiet dishonesty \u2014 that you\u2019ve told yourself doesn\u2019t matter? What does it reveal?",
                   "If God doubled your income tomorrow, would your problems shrink or simply scale? What does that tell you about where to start?"],
             "step": ("Pick one small area of financial faithfulness \u2014 a debt you\u2019ve avoided, a "
                      "promise you made, an honest correction \u2014 and take care of it this week, "
                      "however small.")},
            {"t": ["A Whole-Life", "Stewardship"], "v": "\u201cIt is required that those who have been given a trust must prove faithful.\u201d \u2014 1 Corinthians 4:2",
             "tags": ["stewardship", "ownership", "commitment", "1 Corinthians 4"],
             "q": ["After these weeks, what is the single biggest shift in how you see the relationship between your faith and your finances?",
                   "If you genuinely lived as a steward rather than an owner of your money, what is the first decision that would change next month?",
                   "Who in this group has helped you see your money differently \u2014 and what do you want to keep being accountable for?"],
             "commit": ("Each person names one specific way they will \u2018serve God, not money\u2019 over the "
                        "next 90 days \u2014 a giving step, a debt step, or a trust step \u2014 and names one "
                        "person in the group who will ask them about it. Close by praying for each "
                        "other\u2019s faithfulness."),
             "tags_commit": True},
        ],
    },
    # 2 -----------------------------------------------------------------
    {
        "n": 2, "theme": "forest",
        "title": ["Financial", "Wisdom"],
        "category": "TITLE TWO · GOD\u2019S PRACTICAL WISDOM FOR EVERYDAY MONEY",
        "band_line": ("Most money problems are not income problems \u2014 they are wisdom problems, and "
                      "Scripture is full of practical, proven wisdom for the financial decisions you "
                      "make every single day."),
        "pull": "\u201cMost money trouble is not a math problem. It is a wisdom problem \u2014 and wisdom can be learned.\u201d",
        "body": ("Ask people why they\u2019re in financial stress and most will say they don\u2019t make "
                 "enough. But more income rarely fixes it \u2014 the same patterns simply scale. The real "
                 "shortage is usually wisdom: a plan, a margin, a brake on impulse, the courage to "
                 "ask for counsel. The good news is that the Bible is one of the most practical "
                 "financial books ever written. The book of Proverbs alone is a financial education "
                 "\u2014 on diligence, debt, saving, generosity, and counsel. Financial Wisdom puts that "
                 "ancient, time-tested wisdom into the hands of ordinary people making ordinary "
                 "money decisions."),
        "scripture": ("\u201cThe plans of the diligent lead to profit as surely as haste leads to "
                      "poverty.\u201d", "Proverbs 21:5 (NIV)"),
        "subtitles": [
            "A 40-Day Journey Through God\u2019s Wisdom for Your Money",
            "Discovering the Practical Financial Wisdom of Scripture",
            "A 40-Day Path to Diligent, Debt-Free, Disciplined Living",
            "Learning to Make Money Decisions God\u2019s Way",
        ],
        "bigidea": ("God\u2019s Word is not silent about money \u2014 it is full of practical, repeatable wisdom "
                    "that works in any income and any era. The person who learns it stops repeating "
                    "the patterns that keep them stuck and starts building a life that lasts."),
        "tags": ["wisdom", "Proverbs", "planning", "diligence", "counsel", "discipline"],
        "info": {"Audience": "All church · young adults · anyone starting over",
                 "Best Season": "New Year · Back-to-school · Anytime",
                 "Why it matters": "Wisdom is the missing ingredient in most money stress"},
        "sessions": [
            {"t": ["Wisdom Begins", "with the Fear of God"], "v": "\u201cThe fear of the Lord is the beginning of wisdom.\u201d \u2014 Proverbs 9:10",
             "tags": ["wisdom", "the fear of the Lord", "humility", "Proverbs 9"],
             "q": ["Wisdom starts not with a budget but with God. How does beginning your money decisions with \u2018What honors God here?\u2019 change them?",
                   "Where in your finances have you been leaning on your own understanding rather than seeking God\u2019s wisdom?",
                   "Who taught you about money growing up \u2014 and which of those lessons were wise, and which do you now need to unlearn?"],
             "step": ("Before any money decision over $100 this week, pause and pray one sentence: "
                      "\u2018God, give me wisdom here.\u2019 Notice what changes. Report back to your partner.")},
            {"t": ["The Diligent", "Make a Plan"], "v": "\u201cThe plans of the diligent lead to profit.\u201d \u2014 Proverbs 21:5",
             "tags": ["planning", "budget", "diligence", "Proverbs 21"],
             "q": ["A budget is just a plan for your money before the month spends it for you. What stops you from making one \u2014 or sticking to one?",
                   "Where in your finances are you living by \u2018haste\u2019 \u2014 reacting, impulse-buying, or guessing \u2014 instead of by a plan?",
                   "If you wrote a simple plan for next month\u2019s money, what is the one number that would scare you to look at honestly?"],
             "step": ("Write a simple plan for next month: income at the top, then giving, saving, "
                      "and spending. It does not have to be perfect \u2014 it has to exist. Bring it to your "
                      "partner.")},
            {"t": ["The Danger", "of Debt"], "v": "\u201cThe rich rule over the poor, and the borrower is slave to the lender.\u201d \u2014 Proverbs 22:7",
             "tags": ["debt", "freedom", "borrowing", "Proverbs 22"],
             "q": ["Proverbs calls the borrower a slave to the lender. Where have you felt the truth of that in your own life?",
                   "What is one debt you carry that you have quietly stopped believing you can ever escape? Is that belief true?",
                   "What would change in your daily emotional life if you owed no one anything? What would it be worth to get there?"],
             "step": ("List your debts smallest to largest. Choose the smallest one and make one "
                      "concrete move against it this week \u2014 an extra payment, a cut expense redirected, "
                      "a plan. Tell your partner.")},
            {"t": ["Counsel and", "Community"], "v": "\u201cPlans fail for lack of counsel, but with many advisers they succeed.\u201d \u2014 Proverbs 15:22",
             "tags": ["counsel", "community", "humility", "Proverbs 15"],
             "q": ["Money is the most private subject most of us have. Why is it so hard to ask for help \u2014 and what has that silence cost you?",
                   "Who is one wise person you could invite into your financial life as a counselor or accountability partner?",
                   "What money decision are you facing right now where you actually need outside counsel before you act?"],
             "step": ("Ask one trusted, wiser person this week for honest input on one financial "
                      "decision you\u2019re facing. Come back and tell the group what you learned.")},
            {"t": ["Saving and", "the Ant"], "v": "\u201cThe wise store up choice food and olive oil, but fools gulp theirs down.\u201d \u2014 Proverbs 21:20",
             "tags": ["saving", "self-control", "future", "Proverbs 21"],
             "q": ["Proverbs praises the ant who stores up in advance. What makes saving so hard \u2014 is it income, impulse, or something deeper?",
                   "Do you have any margin \u2014 any cushion \u2014 between you and the next surprise? How does living without one feel?",
                   "If you could automatically save a small amount every payday and never see it, what would you set it at to start?"],
             "step": ("Set up one automatic transfer to savings this week \u2014 even $10 a payday. The "
                      "amount matters less than the habit. Tell your partner what you started.")},
            {"t": ["Wisdom", "That Lasts"], "v": "\u201cA good person leaves an inheritance for their children\u2019s children.\u201d \u2014 Proverbs 13:22",
             "tags": ["legacy", "wisdom", "generations", "Proverbs 13"],
             "q": ["After these weeks, what is the single wisest financial change you\u2019ve made or decided to make?",
                   "What kind of financial legacy are you building right now \u2014 in money, yes, but also in the habits and beliefs your family will inherit from you?",
                   "Who is one person you could begin to pass this wisdom on to in the next season?"],
             "commit": ("Each person names the one financial-wisdom habit \u2014 planning, saving, fighting "
                        "debt, or seeking counsel \u2014 they will build over the next 90 days, and one "
                        "person who will ask them about it. Close by praying for diligence and "
                        "discipline for each other."),
             "tags_commit": True},
        ],
    },
    # 3 -----------------------------------------------------------------
    {
        "n": 3, "theme": "stone",
        "title": ["Money", "Made Simple"],
        "category": "TITLE THREE · CLEARING THE CLUTTER, COMPARISON & NOISE",
        "band_line": ("We rarely need more money as often as we need less complication \u2014 and these "
                      "forty days clear away the clutter, the comparison, and the noise to uncover "
                      "the freedom of enough."),
        "pull": "\u201cThe goal was never more. The goal was enough \u2014 and the freedom that comes with it.\u201d",
        "body": ("Modern money is loud and complicated. Endless subscriptions, buy-now-pay-later, "
                 "a feed full of everyone\u2019s highlight reel, and a quiet voice that always whispers "
                 "\u2018a little more would do it.\u2019 But Scripture points a different direction entirely: "
                 "godliness with contentment, it says, is great gain. Money Made Simple strips the "
                 "subject down to its essentials. It helps people untangle the clutter, escape the "
                 "comparison trap, build one simple plan, and rediscover the deep, almost forgotten "
                 "freedom of having enough \u2014 and knowing it."),
        "scripture": ("\u201cBut godliness with contentment is great gain. For we brought nothing into "
                      "the world, and we can take nothing out of it.\u201d", "1 Timothy 6:6\u20137 (NIV)"),
        "subtitles": [
            "A 40-Day Journey to a Simpler, Freer Financial Life",
            "Discovering the Quiet Freedom of Enough",
            "A 40-Day Path Out of Clutter, Comparison, and Complexity",
            "Untangling Your Money and Rediscovering Contentment",
        ],
        "bigidea": ("Financial peace rarely comes from earning more. It comes from wanting less, "
                    "owning less, owing less, and simplifying everything until what\u2019s left is "
                    "enough \u2014 and the freedom that was hiding underneath the noise."),
        "tags": ["simplicity", "contentment", "enough", "comparison", "margin", "freedom"],
        "info": {"Audience": "All church · busy families · over-stretched givers",
                 "Best Season": "New Year · Post-holiday · Summer reset",
                 "Why it matters": "The culture sells complexity; the gospel offers enough"},
        "sessions": [
            {"t": ["The Trap", "of More"], "v": "\u201cWhoever loves money never has enough.\u201d \u2014 Ecclesiastes 5:10",
             "tags": ["more", "discontent", "the trap", "Ecclesiastes 5"],
             "q": ["\u2018Just a little more\u2019 is the most expensive sentence in our lives. Where does that voice show up loudest for you?",
                   "Name a time you finally got the thing you were sure would satisfy you. How long did the satisfaction last?",
                   "What would it feel like to genuinely believe you already have enough? What keeps you from believing it?"],
             "step": ("This week, write down every time you feel the pull of \u2018a little more.\u2019 Don\u2019t act "
                      "on it \u2014 just notice it. Bring the list to your partner and look for the pattern.")},
            {"t": ["The Freedom", "of Enough"], "v": "\u201cI have learned to be content whatever the circumstances.\u201d \u2014 Philippians 4:11",
             "tags": ["contentment", "enough", "learned", "Philippians 4"],
             "q": ["Paul says contentment is learned, not natural. What experiences in your life have actually taught it to you?",
                   "Where are you currently more content \u2014 in plenty or in want? What does your answer reveal?",
                   "If \u2018enough\u2019 had a number for your household this season, do you know what it is? Why is that question so hard to answer?"],
             "step": ("Define \u2018enough\u2019 for one area of your life this week \u2014 enough clothes, enough "
                      "subscriptions, enough square footage \u2014 and live inside that definition on "
                      "purpose. Tell your partner what you chose.")},
            {"t": ["Untangling", "the Clutter"], "v": "\u201cLet us throw off everything that hinders.\u201d \u2014 Hebrews 12:1",
             "tags": ["clutter", "simplify", "subscriptions", "Hebrews 12"],
             "q": ["Financial clutter \u2014 unused subscriptions, scattered accounts, forgotten auto-pays \u2014 is money leaking quietly. Where is yours leaking?",
                   "What is one financial complication you\u2019ve tolerated for years simply because untangling it felt like too much work?",
                   "What hinders you most from a simpler financial life \u2014 habit, fear, comparison, or just busyness?"],
             "step": ("Cancel one subscription or recurring charge you don\u2019t truly use, and close or "
                      "consolidate one account you don\u2019t need. Tell your partner what you cleared.")},
            {"t": ["One Budget,", "One Plan"], "v": "\u201cSuppose one of you wants to build a tower. Won\u2019t you first sit down and estimate the cost?\u201d \u2014 Luke 14:28",
             "tags": ["plan", "simplicity", "clarity", "Luke 14"],
             "q": ["Jesus assumes wise people count the cost first. What would a genuinely simple money plan look like for your household \u2014 not complicated, just clear?",
                   "What is the most complicated part of your finances, and could it actually be simpler than you\u2019ve made it?",
                   "What is one number you avoid looking at \u2014 and what would change if you finally looked?"],
             "step": ("Build the simplest possible plan: what comes in, what must go out, what\u2019s left. "
                      "One page, no apps required. Show it to your partner.")},
            {"t": ["Escaping", "Comparison"], "v": "\u201cEach one should test their own actions\u2026 without comparing themselves to someone else.\u201d \u2014 Galatians 6:4",
             "tags": ["comparison", "contentment", "social media", "Galatians 6"],
             "q": ["Comparison turns a good-enough life into a disappointing one. Whose financial life are you most tempted to measure yours against?",
                   "How much of your spending is actually about keeping up with someone else\u2019s story? Be specific.",
                   "What would change if you ran your race \u2014 your income, your season, your calling \u2014 without one glance sideways?"],
             "step": ("Fast from one source of comparison this week \u2014 a feed, an app, a habit. Notice "
                      "what it does to your contentment and your spending. Report back.")},
            {"t": ["The Simple,", "Free Life"], "v": "\u201cSeek first his kingdom\u2026 and all these things will be given to you as well.\u201d \u2014 Matthew 6:33",
             "tags": ["freedom", "simplicity", "kingdom", "Matthew 6"],
             "q": ["After these weeks, where do you feel the freedom of \u2018enough\u2019 most \u2014 and where is the pull of \u2018more\u2019 still strong?",
                   "What is the one simplification that has made the biggest difference for you?",
                   "How could a simpler financial life free up money, time, or attention for what God is actually calling you to?"],
             "commit": ("Each person names one simplification \u2014 a cut expense, a defined \u2018enough,\u2019 a "
                        "comparison fast \u2014 they will keep for the next 90 days, and one person who "
                        "will check in. Close by thanking God together for the gift of enough."),
             "tags_commit": True},
        ],
    },
    # 4 -----------------------------------------------------------------
    {
        "n": 4, "theme": "teal",
        "title": ["Financial", "Peace"],
        "category": "TITLE FOUR · TRADING MONEY ANXIETY FOR REAL PEACE",
        "band_line": ("Peace is not the absence of financial pressure \u2014 it is the presence of a "
                      "trustworthy God in the middle of it, and these forty days help you find it "
                      "before the numbers ever change."),
        "pull": "\u201cFinancial peace is not waiting on the other side of your problems. It is available right now.\u201d",
        "body": ("Money is the number-one source of stress in marriages, the thing that wakes people "
                 "at 3 a.m., and a worry that doesn\u2019t politely wait until the bills arrive. We tend "
                 "to believe peace will come once the debt is gone or the account is full \u2014 but those "
                 "who reach that point usually discover the worry simply found a new target. Real "
                 "financial peace is different. It rests not on the balance but on the God behind it. "
                 "Financial Peace helps people name their worry, hand it to God daily, and discover "
                 "a peace that guards the heart even while the numbers are still being worked out."),
        "scripture": ("\u201cDo not be anxious about anything, but in every situation, by prayer and "
                      "petition, with thanksgiving, present your requests to God. And the peace of "
                      "God\u2026 will guard your hearts and your minds in Christ Jesus.\u201d",
                      "Philippians 4:6\u20137 (NIV)"),
        "subtitles": [
            "A 40-Day Journey from Money Anxiety to Real Peace",
            "Discovering Peace That Doesn\u2019t Wait for the Numbers to Change",
            "A 40-Day Path Out of Financial Worry and Fear",
            "Finding Rest in the God Who Holds Your Finances",
        ],
        "bigidea": ("Financial peace is available right now \u2014 before the debt is gone, before the "
                    "account is full \u2014 because it rests on the character of God, not the size of the "
                    "balance. The person who learns to hand the worry over daily is free long before "
                    "the math is."),
        "tags": ["peace", "anxiety", "worry", "trust", "rest", "prayer"],
        "info": {"Audience": "All church · the anxious · couples under money stress",
                 "Best Season": "January · Lent · Tax season · Anytime",
                 "Why it matters": "Money is the leading source of stress in most homes"},
        "sessions": [
            {"t": ["Naming", "the Worry"], "v": "\u201cDo not be anxious about anything\u2026 present your requests to God.\u201d \u2014 Philippians 4:6",
             "tags": ["anxiety", "honesty", "prayer", "Philippians 4"],
             "q": ["What is the specific financial worry you carry most days but rarely say out loud? Naming it is the first step to handing it over.",
                   "When does money anxiety hit you hardest \u2014 a time of day, a kind of email, a moment in the month?",
                   "What have you been doing with that worry until now \u2014 carrying it, numbing it, ignoring it, or actually praying it?"],
             "step": ("Each day this week, name your top money worry specifically and out loud to God "
                      "\u2014 before you do anything else with it. Tell your partner whether saying it "
                      "changed anything.")},
            {"t": ["The Peace", "That Guards"], "v": "\u201cAnd the peace of God\u2026 will guard your hearts and your minds.\u201d \u2014 Philippians 4:7",
             "tags": ["peace", "guard", "the mind", "Philippians 4"],
             "q": ["Paul promises a peace that guards your mind \u2014 like a soldier at the gate. What thoughts most need a guard posted in front of them right now?",
                   "Have you ever felt a peace about money that you couldn\u2019t explain by the circumstances? What was happening?",
                   "What does it mean to you that the promise is peace in the situation, not removal of it?"],
             "step": ("When the worry returns this week, pray Philippians 4:6\u20137 word for word and then "
                      "stop \u2014 do not rehearse the fear again. Track how often you had to, and tell your "
                      "partner.")},
            {"t": ["Casting", "Your Cares"], "v": "\u201cCast all your anxiety on him because he cares for you.\u201d \u2014 1 Peter 5:7",
             "tags": ["casting", "care", "surrender", "1 Peter 5"],
             "q": ["The reason we can cast our cares is that He cares for us. How easy or hard is it for you to believe God actually cares about your finances?",
                   "What\u2019s the difference between handing a worry to God and just trying harder not to worry?",
                   "Is there a financial care you keep \u2018casting\u2019 and then quietly picking back up? Why do you take it back?"],
             "step": ("Find a physical action for \u2018casting\u2019 \u2014 write the worry on paper and put it in a "
                      "box, a drawer, under your Bible. Each time you reach for it again, leave it "
                      "there. Tell your partner what you\u2019re practicing.")},
            {"t": ["Daily Bread,", "Not Yearly Bread"], "v": "\u201cGive us today our daily bread\u2026 do not worry about tomorrow.\u201d \u2014 Matthew 6:11, 34",
             "tags": ["daily bread", "today", "trust", "Matthew 6"],
             "q": ["God gave Israel manna for one day at a time. Why do you think He provides daily rather than all at once \u2014 and how does worry try to borrow tomorrow\u2019s trouble?",
                   "How much of your financial anxiety is about today\u2019s actual needs versus tomorrow\u2019s imagined ones?",
                   "What would it look like to trust God for today\u2019s provision and leave next year in His hands?"],
             "step": ("Each morning this week, thank God for today\u2019s provision before you worry about "
                      "any future month. Practice living in \u2018daily bread.\u2019 Report back to your partner.")},
            {"t": ["Content in", "Plenty and Want"], "v": "\u201cI have learned the secret of being content in any and every situation.\u201d \u2014 Philippians 4:12",
             "tags": ["contentment", "secret", "circumstances", "Philippians 4"],
             "q": ["Paul learned a \u2018secret\u2019 to peace in both plenty and want. What do you think that secret is \u2014 and have you tasted it?",
                   "Which is harder for your peace \u2014 having little, or having more and fearing the loss of it?",
                   "Where is your peace currently anchored \u2014 in your circumstances, or in something steadier?"],
             "step": ("Choose one circumstance you cannot change this week and practice contentment "
                      "inside it on purpose. Notice what it does to your peace. Tell your partner.")},
            {"t": ["Sustained Peace", "in Community"], "v": "\u201cCome to me, all you who are weary and burdened, and I will give you rest.\u201d \u2014 Matthew 11:28",
             "tags": ["rest", "community", "peace", "Matthew 11"],
             "q": ["After these weeks, where do you feel the most peace about money \u2014 and where does the old worry still grip you?",
                   "How has saying your worries out loud in this group changed their weight?",
                   "What is the one practice from this series you most need to keep in order to stay at peace?"],
             "commit": ("Each person names one peace practice \u2014 daily prayer over a worry, a casting "
                        "ritual, a thanksgiving habit \u2014 they will sustain for 90 days, and one person "
                        "who will ask after their peace. Close by praying rest over each home "
                        "represented in the room."),
             "tags_commit": True},
        ],
    },
    # 5 -----------------------------------------------------------------
    {
        "n": 5, "theme": "bronze",
        "title": ["Wise", "with Money"],
        "category": "TITLE FIVE · THE EVERYDAY SKILL OF HANDLING MONEY WELL",
        "band_line": ("Faithfulness with money is a skill you can actually learn \u2014 and these forty "
                      "days build it, one practical habit at a time, across the only five things "
                      "anyone can ever do with a dollar."),
        "pull": "\u201cThere are only five things you can do with money. Wisdom means learning to do each one well.\u201d",
        "body": ("Nobody is born knowing how to handle money, and most of us were never taught. So "
                 "we improvise \u2014 and the improvising costs us. But here is the freeing truth: handling "
                 "money well is a skill, and skills can be learned. There are really only five things "
                 "anyone can do with a dollar \u2014 earn it, save it, give it, owe it, and invest it. Wise "
                 "with Money walks through each one with Scripture and practice, so that ordinary "
                 "people become genuinely skilled, confident, and faithful with whatever God has "
                 "placed in their hands \u2014 whether that\u2019s a little or a lot."),
        "scripture": ("\u201cBe sure you know the condition of your flocks, give careful attention to your "
                      "herds; for riches do not endure forever.\u201d", "Proverbs 27:23\u201324 (NIV)"),
        "subtitles": [
            "A 40-Day Journey to Becoming Skilled and Faithful with Money",
            "Discovering the Five Things You Can Do with Every Dollar",
            "A 40-Day Path to Practical, Confident Stewardship",
            "Learning the Everyday Skill of Handling Money Well",
        ],
        "bigidea": ("Earn, save, give, owe, invest \u2014 there are only five things anyone can do with "
                    "money, and wisdom is simply learning to do each one God\u2019s way. Faithfulness is "
                    "not a personality type. It is a skill, and it can be built."),
        "tags": ["stewardship", "skill", "the five uses", "habits", "faithfulness", "practical"],
        "info": {"Audience": "All church · young adults · company workforces",
                 "Best Season": "New Year · Graduation season · Anytime",
                 "Why it matters": "Most people were never actually taught how to handle money"},
        "sessions": [
            {"t": ["Know", "Your Numbers"], "v": "\u201cBe sure you know the condition of your flocks.\u201d \u2014 Proverbs 27:23",
             "tags": ["awareness", "numbers", "honesty", "Proverbs 27"],
             "q": ["You can\u2019t steward what you won\u2019t look at. Do you actually know your real numbers \u2014 income, spending, debt, savings \u2014 or do you avoid them?",
                   "What feeling comes up when you imagine sitting down and looking at all of it honestly? Where does that feeling come from?",
                   "What is the one number you most need to know but have been afraid to find out?"],
             "step": ("Sit down and write your real numbers on one page: what you earn, owe, save, "
                      "and spend. No fixing yet \u2014 just seeing. Bring the page to your partner.")},
            {"t": ["Earn with", "Integrity"], "v": "\u201cWhatever you do, work at it with all your heart, as working for the Lord.\u201d \u2014 Colossians 3:23",
             "tags": ["work", "earning", "integrity", "Colossians 3"],
             "q": ["The first thing we do with money is earn it. How does seeing your work as \u2018for the Lord\u2019 change how you show up to it?",
                   "Is there any way you earn or handle money at work that you couldn\u2019t fully bring into the light? What needs to change?",
                   "Are you using your skills and energy faithfully \u2014 or coasting, or burning out? What would faithful earning look like in your season?"],
             "step": ("Pick one way to bring more integrity or excellence to how you earn this week "
                      "\u2014 honesty, effort, or attitude \u2014 and practice it as worship. Tell your partner.")},
            {"t": ["Save with", "Foresight"], "v": "\u201cThe wise store up choice food\u2026 but fools gulp theirs down.\u201d \u2014 Proverbs 21:20",
             "tags": ["saving", "foresight", "discipline", "Proverbs 21"],
             "q": ["Saving is delayed reward, and our culture is built on instant reward. What makes saving hardest for you?",
                   "Do you have an emergency cushion \u2014 even a small one? How does living with or without one feel?",
                   "If you saved consistently for five years, what could it free you to do or to give?"],
             "step": ("Start or increase one automatic savings habit this week, however small, and "
                      "name what it\u2019s for \u2014 an emergency, a goal, a gift. Tell your partner.")},
            {"t": ["Give", "with Joy"], "v": "\u201cEach of you should give\u2026 not reluctantly\u2026 for God loves a cheerful giver.\u201d \u2014 2 Corinthians 9:7",
             "tags": ["giving", "generosity", "joy", "2 Corinthians 9"],
             "q": ["Giving is the one use of money that breaks its grip on us. Where would you honestly place your giving \u2014 cheerful, reluctant, or absent?",
                   "What\u2019s the most joy you\u2019ve ever felt giving something away? What made it joyful?",
                   "What fear or hesitation most often keeps you from being more generous?"],
             "step": ("Give something away this week that stretches you a little \u2014 money, but it "
                      "could also be time or possessions \u2014 and pay attention to the joy. Tell your "
                      "partner what you noticed.")},
            {"t": ["Owe Nothing", "but Love"], "v": "\u201cLet no debt remain outstanding, except the continuing debt to love one another.\u201d \u2014 Romans 13:8",
             "tags": ["debt", "freedom", "love", "Romans 13"],
             "q": ["Owing is one of the five uses of money \u2014 but Scripture treats it with caution. Where is debt currently limiting your freedom?",
                   "What is the difference between debt that builds something and debt that just funds a lifestyle? Which kind is yours?",
                   "If you were debt-free, what would you be free to do \u2014 to give, to risk, to rest \u2014 that you can\u2019t do now?"],
             "step": ("Choose one debt and make one real move against it this week \u2014 a plan, an extra "
                      "payment, a cut expense redirected toward it. Tell your partner your target.")},
            {"t": ["Invest", "for Eternity"], "v": "\u201cStore up for yourselves treasures in heaven.\u201d \u2014 Matthew 6:20",
             "tags": ["investing", "eternity", "treasure", "Matthew 6"],
             "q": ["The fifth use of money is investing it \u2014 and Jesus widens the idea to eternal returns. How are you investing in things that outlast you?",
                   "Of the five uses \u2014 earn, save, give, owe, invest \u2014 which one have you grown in most over these weeks, and which still needs the most work?",
                   "What would it look like to invest some of what God\u2019s given you in His Kingdom this year?"],
             "commit": ("Each person names the one use of money \u2014 earning, saving, giving, owing, or "
                        "investing \u2014 they will most intentionally grow in over the next 90 days, and "
                        "one person who will ask about it. Close by praying for skill and faithfulness "
                        "for each other."),
             "tags_commit": True},
        ],
    },
    # 6 -----------------------------------------------------------------
    {
        "n": 6, "theme": "plum",
        "title": ["God,", "Money & Me"],
        "category": "TITLE SIX · WHAT MONEY IS DOING IN YOUR HEART",
        "band_line": ("This journey is less about your bank account and more about your heart \u2014 the "
                      "quiet place where money competes with God for your security, your identity, "
                      "and your trust."),
        "pull": "\u201cMoney is a mirror. It shows you what you actually love, fear, and trust.\u201d",
        "body": ("You can fix a budget and still be enslaved to money. The deepest financial problems "
                 "are not in the spreadsheet \u2014 they\u2019re in the heart. Money makes a wonderful servant "
                 "and a terrible master, and the difference is decided not in the bank but in the "
                 "soul. God, Money & Me is the most personal title in the series. It turns down the "
                 "noise of budgets and balances and asks the harder questions: Where does my security "
                 "really come from? What is money promising me that only God can give? Whose am I? "
                 "It\u2019s an honest, searching look at what money is quietly doing in the human heart \u2014 "
                 "and how to put it back in its place."),
        "scripture": ("\u201cFor the love of money is a root of all kinds of evil. Some people, eager for "
                      "money, have wandered from the faith.\u201d", "1 Timothy 6:10 (NIV)"),
        "subtitles": [
            "A 40-Day Journey into What Money Is Doing in Your Heart",
            "Discovering What Your Money Reveals About Your Soul",
            "A 40-Day Path to Putting Money Back in Its Place",
            "An Honest Look at God, Money, and You",
        ],
        "bigidea": ("Money is a mirror and a master-in-waiting. It reveals what we truly love, fear, "
                    "and trust \u2014 and it quietly offers to become the thing we look to for security and "
                    "identity. Real change starts not in the budget but in the heart that holds it."),
        "tags": ["the heart", "identity", "security", "idolatry", "honesty", "surrender"],
        "info": {"Audience": "All church · maturing believers · honest seekers",
                 "Best Season": "Lent · New Year · Spiritual-growth seasons",
                 "Why it matters": "Money problems are usually heart problems wearing a disguise"},
        "sessions": [
            {"t": ["The Mirror", "of Money"], "v": "\u201cFor the love of money is a root of all kinds of evil.\u201d \u2014 1 Timothy 6:10",
             "tags": ["the heart", "love of money", "the mirror", "1 Timothy 6"],
             "q": ["Paul warns against the love of money, not money itself. How can you tell the difference in your own heart?",
                   "If money is a mirror, what has it been showing you about yourself lately \u2014 your fears, your loves, your insecurities?",
                   "Where has the pursuit of money ever pulled you away from something that mattered more?"],
             "step": ("Each evening this week, ask one question before bed: \u2018What did money reveal "
                      "about my heart today?\u2019 Write down what you notice and bring one entry to your "
                      "partner.")},
            {"t": ["Where Is My", "Security?"], "v": "\u201cThough your riches increase, do not set your heart on them.\u201d \u2014 Psalm 62:10",
             "tags": ["security", "trust", "the heart", "Psalm 62"],
             "q": ["When you imagine real security, what comes to mind \u2014 a number, a paid-off house, a full account? What does that reveal?",
                   "Where have you set your heart on money to do a job only God can do \u2014 to make you feel safe, worthy, or in control?",
                   "What would change if your sense of security came from God\u2019s presence rather than your provision?"],
             "step": ("Identify one thing you\u2019ve been trusting money to make you feel \u2014 safe, valued, "
                      "in control \u2014 and each day this week, ask God to be that for you instead. Tell "
                      "your partner what you\u2019re practicing.")},
            {"t": ["The Story", "I Tell Myself"], "v": "\u201cWatch out! Be on your guard against all kinds of greed.\u201d \u2014 Luke 12:15",
             "tags": ["greed", "self-deception", "the rich fool", "Luke 12"],
             "q": ["Jesus tells of a man who said, \u2018I\u2019ll build bigger barns and then I\u2019ll relax.\u2019 What is the \u2018when I have ___, then I\u2019ll be okay\u2019 story you tell yourself?",
                   "Greed almost never feels like greed from the inside \u2014 it feels like wisdom or need. Where might that be true for you?",
                   "If God called your name tonight like He did the rich fool\u2019s, what would you wish you had done differently with your money?"],
             "step": ("Write out the financial story you secretly tell yourself \u2014 \u2018when I have ___, "
                      "then I\u2019ll finally be ___.\u2019 Examine whether it\u2019s true. Share it with your partner.")},
            {"t": ["Open Hands,", "Open Heart"], "v": "\u201cWhoever loves money never has enough.\u201d \u2014 Ecclesiastes 5:10",
             "tags": ["open hands", "contentment", "generosity", "Ecclesiastes 5"],
             "q": ["A closed fist can\u2019t receive and can\u2019t give. Where is your grip on money tightest right now?",
                   "What are you most afraid would happen if you held your money with genuinely open hands?",
                   "When have you experienced the strange freedom of giving something away that you were gripping tightly?"],
             "step": ("Practice \u2018open hands\u2019 literally: each morning, hold your hands open in prayer "
                      "and tell God your money is His to direct. Then look for one chance to give. "
                      "Tell your partner what happened.")},
            {"t": ["Whose", "Am I?"], "v": "\u201cYou are not your own; you were bought at a price.\u201d \u2014 1 Corinthians 6:19\u201320",
             "tags": ["ownership", "identity", "belonging", "1 Corinthians 6"],
             "q": ["If you are not your own \u2014 if you and everything you have belongs to God \u2014 what changes about how you hold your money?",
                   "Where do you still live as an owner rather than a steward? What would surrender look like there?",
                   "How does your identity in Christ free you from needing money to tell you who you are?"],
             "step": ("Make a written transfer of ownership: name the major things you call \u2018mine\u2019 and "
                      "deliberately hand each to God as their true owner. Bring it to your partner.")},
            {"t": ["A Surrendered", "Wallet"], "v": "\u201cFor where your treasure is, there your heart will be also.\u201d \u2014 Matthew 6:21",
             "tags": ["surrender", "the heart", "treasure", "Matthew 6"],
             "q": ["After these weeks, what has God surfaced in your heart through the mirror of money that you didn\u2019t see before?",
                   "What is the one heart-level shift \u2014 not budget-level \u2014 you most want to keep?",
                   "Who in this group has helped you be honest, and what do you want them to keep asking you?"],
             "commit": ("Each person names the one heart shift \u2014 about security, identity, greed, or "
                        "ownership \u2014 they most want to sustain over the next 90 days, and one person "
                        "who will hold them to it. Close by praying for surrendered hearts, not just "
                        "balanced budgets."),
             "tags_commit": True},
        ],
    },
    # 7 -----------------------------------------------------------------
    {
        "n": 7, "theme": "pine",
        "title": ["Financial", "Health"],
        "category": "TITLE SEVEN · BUILDING HABITS FOR A HEALTHY MONEY LIFE",
        "band_line": ("Financial health, like physical health, is built one ordinary, faithful habit "
                      "at a time \u2014 and these forty days lay the foundation for a money life that is "
                      "strong, steady, and sustainable for the long haul."),
        "pull": "\u201cNobody gets financially healthy by accident. It is built one small, faithful habit at a time.\u201d",
        "body": ("We talk about physical health \u2014 diet, exercise, rest \u2014 as something built daily. "
                 "Financial health works exactly the same way. It isn\u2019t created by a windfall or a "
                 "raise; it\u2019s built by small, repeated, God-honoring habits that compound quietly "
                 "over years. The honest check-up, the steady budget, the automatic save, the regular "
                 "gift, the slow climb out of debt \u2014 none of them is dramatic, and together they change "
                 "everything. Financial Health helps people stop chasing the one big fix and start "
                 "building the ordinary, durable habits of a financially healthy life \u2014 the kind that "
                 "frees you to serve God longer and better."),
        "scripture": ("\u201cCommit to the Lord whatever you do, and he will establish your plans.\u201d",
                      "Proverbs 16:3 (NIV)"),
        "subtitles": [
            "A 40-Day Journey to a Healthy, Sustainable Financial Life",
            "Discovering the Everyday Habits of Financial Health",
            "A 40-Day Path from Money Mess to Money Health",
            "Building the Ordinary Habits That Change Everything",
        ],
        "bigidea": ("A financially healthy life is not built by a windfall but by small, consistent, "
                    "God-honoring habits that compound over time. Health is the slow reward of "
                    "faithfulness \u2014 and it frees you to serve God longer and better."),
        "tags": ["health", "habits", "consistency", "sustainability", "discipline", "long-term"],
        "info": {"Audience": "All church · anyone rebuilding · company wellness",
                 "Best Season": "New Year · Fall reset · Anytime",
                 "Why it matters": "Lasting change comes from habits, not one-time fixes"},
        "sessions": [
            {"t": ["An Honest", "Check-Up"], "v": "\u201cLet us examine our ways and test them, and let us return to the Lord.\u201d \u2014 Lamentations 3:40",
             "tags": ["honesty", "assessment", "return", "Lamentations 3"],
             "q": ["If you gave your financial life a check-up today, what would the diagnosis be \u2014 healthy, strained, or in crisis? Be honest.",
                   "What is the one financial symptom you\u2019ve been ignoring and hoping will resolve itself?",
                   "What\u2019s one habit from your past that got you here \u2014 and are you ready to examine it honestly?"],
             "step": ("Give yourself an honest one-page check-up this week: what\u2019s healthy, what\u2019s "
                      "strained, what needs urgent care. No shame, just clarity. Bring it to your "
                      "partner.")},
            {"t": ["The Habit", "of the Budget"], "v": "\u201cWon\u2019t you first sit down and estimate the cost?\u201d \u2014 Luke 14:28",
             "tags": ["budget", "habit", "planning", "Luke 14"],
             "q": ["A budget isn\u2019t a cage \u2014 it\u2019s a habit that tells your money where to go before it disappears. What\u2019s your honest history with budgeting?",
                   "What makes a budget fall apart for you \u2014 and what would make one actually stick this time?",
                   "What is one expense that consistently surprises you, and how could a simple plan stop the surprise?"],
             "step": ("Build and use a simple budget for one week \u2014 just track and steer, don\u2019t "
                      "overhaul. Notice what you learn. Tell your partner what surprised you.")},
            {"t": ["The Habit", "of Saving"], "v": "\u201cDishonest money dwindles away, but whoever gathers money little by little makes it grow.\u201d \u2014 Proverbs 13:11",
             "tags": ["saving", "consistency", "growth", "Proverbs 13"],
             "q": ["Scripture praises \u2018little by little.\u2019 Why do we keep waiting for the big amount instead of starting with the small one?",
                   "What would having even a small cushion change about your stress level and your decisions?",
                   "What\u2019s one regular expense you could redirect, even partly, into savings starting this week?"],
             "step": ("Make saving automatic and \u2018little by little\u2019 this week \u2014 set it, forget it, and "
                      "let it grow. Report the habit you started to your partner.")},
            {"t": ["The Habit", "of Generosity"], "v": "\u201cOne person gives freely, yet gains even more.\u201d \u2014 Proverbs 11:24\u201325",
             "tags": ["generosity", "giving", "freedom", "Proverbs 11"],
             "q": ["Generosity is the habit that keeps money from owning us. Is giving currently a regular habit for you, or an occasional impulse?",
                   "Proverbs says the generous person gains. How have you seen that paradox prove true \u2014 or what keeps you from testing it?",
                   "What would it look like to make generosity the first habit in your budget instead of the leftover?"],
             "step": ("Make one act of generosity a planned habit this week \u2014 first, not last, in your "
                      "spending. Notice how it changes your grip on the rest. Tell your partner.")},
            {"t": ["Healing", "from Debt"], "v": "\u201cThe borrower is slave to the lender.\u201d \u2014 Proverbs 22:7",
             "tags": ["debt", "healing", "freedom", "Proverbs 22"],
             "q": ["Debt is a financial wound that won\u2019t heal on its own. Where are you carrying one, and how long have you carried it?",
                   "What feelings come with your debt \u2014 shame, denial, defeat \u2014 and how do those feelings keep you stuck?",
                   "What would the first step of healing look like \u2014 not the whole journey, just the first move?"],
             "step": ("Choose your smallest debt and start a simple payoff plan this week \u2014 one wound, "
                      "one plan, one first payment. Tell your partner your target date.")},
            {"t": ["Health That", "Lasts a Lifetime"], "v": "\u201cLet us not become weary in doing good, for at the proper time we will reap a harvest.\u201d \u2014 Galatians 6:9",
             "tags": ["endurance", "harvest", "long-term", "Galatians 6"],
             "q": ["After these weeks, which new financial habit feels most life-giving \u2014 and which is hardest to sustain?",
                   "Galatians warns against growing weary. Where are you tempted to quit a good habit before the harvest comes?",
                   "What support do you need to keep these habits going long after this series ends?"],
             "commit": ("Each person names the one financial-health habit \u2014 budgeting, saving, giving, "
                        "or attacking debt \u2014 they commit to sustaining for 90 days, and one person who "
                        "will check on their progress. Close by praying for endurance and a harvest "
                        "of faithfulness."),
             "tags_commit": True},
        ],
    },
    # 8 -----------------------------------------------------------------
    {
        "n": 8, "theme": "oxblood",
        "title": ["Breaking", "Financial Fear"],
        "category": "TITLE EIGHT · FROM SCARCITY & FEAR TO FAITH & FREEDOM",
        "band_line": ("Fear makes a terrible financial advisor \u2014 it tells you to hoard, to hide, and "
                      "to never let go \u2014 and these forty days trade the spirit of scarcity for a "
                      "deep, settled trust in a faithful God."),
        "pull": "\u201cFear whispers that there will never be enough. Faith answers with the God who feeds the birds.\u201d",
        "body": ("So many money decisions are driven by an emotion we rarely name: fear. Fear of not "
                 "having enough makes us hoard. Fear of looking foolish makes us hide. Fear of the "
                 "future makes us cling. Scarcity becomes the lens we see everything through, and it "
                 "quietly runs our lives. But God did not give us a spirit of fear. Breaking Financial "
                 "Fear names the scarcity mindset honestly and replaces it, not with more money, but "
                 "with a deeper trust in the God who feeds the birds and clothes the fields. It is a "
                 "journey from gripping to giving, from anxious hoarding to open-handed freedom."),
        "scripture": ("\u201cFor the Spirit God gave us does not make us timid, but gives us power, love "
                      "and self-discipline.\u201d", "2 Timothy 1:7 (NIV)"),
        "subtitles": [
            "A 40-Day Journey from Scarcity and Fear to Faith and Freedom",
            "Discovering Trust in the God Who Always Provides",
            "A 40-Day Path Out of the Scarcity Mindset",
            "Breaking the Fear That Quietly Runs Your Finances",
        ],
        "bigidea": ("Fear is the hidden hand behind so many money decisions \u2014 and the antidote is not "
                    "a fuller account but a deeper trust. The person who breaks the grip of scarcity "
                    "is finally free to hold money loosely and give it joyfully."),
        "tags": ["fear", "scarcity", "faith", "freedom", "trust", "provision"],
        "info": {"Audience": "All church · the anxious · the over-controlling",
                 "Best Season": "January · Economic uncertainty · Anytime",
                 "Why it matters": "Fear, not income, drives most unhealthy money choices"},
        "sessions": [
            {"t": ["Naming", "the Fear"], "v": "\u201cThe Spirit God gave us does not make us timid, but gives us power, love and self-discipline.\u201d \u2014 2 Timothy 1:7",
             "tags": ["fear", "honesty", "the Spirit", "2 Timothy 1"],
             "q": ["Fear hides behind respectable words like \u2018careful\u2019 and \u2018realistic.\u2019 Where does financial fear actually run your decisions?",
                   "Where did your relationship with money-fear begin \u2014 a season, a loss, a family pattern?",
                   "How would your decisions look different if they were driven by faith instead of fear?"],
             "step": ("Name your specific financial fear out loud to God and to your partner this "
                      "week \u2014 fear unspoken keeps its power. Write down the moment you most felt it.")},
            {"t": ["The Root", "of Scarcity"], "v": "\u201cSo do not worry\u2026 your heavenly Father knows that you need them.\u201d \u2014 Matthew 6:31\u201332",
             "tags": ["scarcity", "worry", "the Father", "Matthew 6"],
             "q": ["A scarcity mindset says, \u2018There will never be enough.\u2019 Where does that voice show up in your spending, saving, or giving?",
                   "Jesus says the Father already knows your needs. How does fear convince you otherwise?",
                   "What does scarcity-thinking cost you \u2014 in generosity, in peace, in relationships?"],
             "step": ("Each time scarcity speaks this week \u2014 \u2018not enough,\u2019 \u2018what if\u2019 \u2014 answer it with "
                      "Matthew 6:32: your Father knows. Track how often you had to. Tell your partner.")},
            {"t": ["The God Who", "Feeds the Birds"], "v": "\u201cLook at the birds of the air\u2026 your heavenly Father feeds them. Are you not much more valuable?\u201d \u2014 Matthew 6:26",
             "tags": ["provision", "trust", "value", "Matthew 6"],
             "q": ["Jesus points to birds and flowers as proof of God\u2019s care. When have you watched God provide in a way you couldn\u2019t have engineered?",
                   "Do you truly believe you are more valuable to God than the birds He feeds? How does fear argue against that?",
                   "What would it take for you to rest in God\u2019s provision rather than rehearse the worst case?"],
             "step": ("Keep a one-week provision log: write down every way, big or small, you see God "
                      "or others provide. Read it back at the end. Share one entry with your partner.")},
            {"t": ["From Hoarding", "to Trusting"], "v": "\u201cYou fool! This very night your life will be demanded from you.\u201d \u2014 Luke 12:20",
             "tags": ["hoarding", "barns", "trust", "Luke 12"],
             "q": ["The rich fool built bigger barns to feel safe. Where do you build \u2018barns\u2019 \u2014 piling up to soothe a fear rather than to serve a purpose?",
                   "What\u2019s the difference between wise saving and fearful hoarding? Which is driving you?",
                   "What would you do differently with money if you genuinely trusted God with your future?"],
             "step": ("Identify one \u2018barn\u2019 \u2014 something you cling to out of fear \u2014 and loosen your grip "
                      "this week by giving or releasing a piece of it. Tell your partner how it felt.")},
            {"t": ["The Courage", "to Be Generous"], "v": "\u201cGod is able to bless you abundantly, so that\u2026 you will abound in every good work.\u201d \u2014 2 Corinthians 9:8",
             "tags": ["generosity", "courage", "blessing", "2 Corinthians 9"],
             "q": ["Generosity is faith in action \u2014 it\u2019s impossible while fear is in charge. Where is fear keeping your hands closed?",
                   "When have you given despite fear and watched God meet you on the other side of it?",
                   "What is one generous act that feels a little scary \u2014 and what would it prove if you did it anyway?"],
             "step": ("Do one generous thing this week that scares you slightly \u2014 not recklessly, but "
                      "as an act of defiant trust. Tell your partner before and after.")},
            {"t": ["Walking", "in Freedom"], "v": "\u201cIt is for freedom that Christ has set us free. Stand firm, then.\u201d \u2014 Galatians 5:1",
             "tags": ["freedom", "trust", "standing firm", "Galatians 5"],
             "q": ["After these weeks, where do you feel real freedom from financial fear \u2014 and where does the old scarcity still grip you?",
                   "What is the single biggest lie fear told you about money that you no longer fully believe?",
                   "How will you \u2018stand firm\u2019 when fear inevitably comes knocking again?"],
             "commit": ("Each person names the one fear they are choosing to break \u2014 and the one act of "
                        "trust or generosity they\u2019ll practice for 90 days to break it \u2014 plus one person "
                        "who will stand with them. Close by praying freedom over each other."),
             "tags_commit": True},
        ],
    },
    # 9 -----------------------------------------------------------------
    {
        "n": 9, "theme": "indigo",
        "title": ["Money", "and Meaning"],
        "category": "TITLE NINE · WHAT YOUR MONEY IS ACTUALLY FOR",
        "band_line": ("The question is not how much money you have \u2014 it is what your money is for \u2014 "
                      "and these forty days help you trade accumulation for contribution and discover "
                      "the meaning money was always meant to carry."),
        "pull": "\u201cMoney becomes meaningful the moment it stops being about getting and starts being about giving.\u201d",
        "body": ("Plenty of people climb the whole ladder only to ask at the top, \u2018Is this all there "
                 "is?\u2019 Accumulation, it turns out, is a poor source of meaning. But money was never "
                 "meant to be only gathered \u2014 it was meant to be aimed. In God\u2019s economy, money "
                 "becomes meaningful the instant it\u2019s pointed at something bigger than ourselves: "
                 "people helped, needs met, a Kingdom advanced, a legacy left. Money and Meaning lifts "
                 "the eyes from the balance to the purpose. It helps people discover what their money "
                 "is actually for, become rich in good deeds, and leave a legacy that outlasts the "
                 "last withdrawal."),
        "scripture": ("\u201cCommand them to do good, to be rich in good deeds, and to be generous and "
                      "willing to share.\u201d", "1 Timothy 6:18 (NIV)"),
        "subtitles": [
            "A 40-Day Journey to Discovering What Your Money Is For",
            "Discovering Meaning, Generosity, and Legacy in Your Finances",
            "A 40-Day Path from Accumulation to Contribution",
            "Aiming Your Money at What Lasts Forever",
        ],
        "bigidea": ("Money finds its meaning not in accumulation but in contribution. The person who "
                    "aims their money at people, purpose, and the Kingdom discovers that giving is "
                    "where money finally makes sense \u2014 and where joy is hiding the whole time."),
        "tags": ["meaning", "purpose", "generosity", "legacy", "Kingdom", "contribution"],
        "info": {"Audience": "All church · second-half adults · the established",
                 "Best Season": "Year-end giving · Fall · Stewardship season",
                 "Why it matters": "Accumulation never satisfies; contribution gives money meaning"},
        "sessions": [
            {"t": ["Is This", "All There Is?"], "v": "\u201cYet when I surveyed all\u2026 everything was meaningless, a chasing after the wind.\u201d \u2014 Ecclesiastes 2:11",
             "tags": ["meaning", "emptiness", "the wind", "Ecclesiastes 2"],
             "q": ["The richest man alive called accumulation \u2018chasing the wind.\u2019 Have you ever reached a financial goal and felt the let-down he described?",
                   "What have you assumed would finally make your money feel meaningful \u2014 and has it?",
                   "If money is meant to be aimed, not just gathered, what has yours been aimed at so far?"],
             "step": ("Write one honest paragraph this week: \u2018What have I been hoping my money would "
                      "give me \u2014 and has it?\u2019 Bring it to your partner.")},
            {"t": ["Rich in", "Good Deeds"], "v": "\u201cCommand them\u2026 to be rich in good deeds, and to be generous and willing to share.\u201d \u2014 1 Timothy 6:18",
             "tags": ["good deeds", "generosity", "richness", "1 Timothy 6"],
             "q": ["Paul redefines wealth as being \u2018rich in good deeds.\u2019 By that measure, how rich are you becoming?",
                   "What good has your money done in someone else\u2019s life recently \u2014 and how did it feel to be part of it?",
                   "What\u2019s one need around you that your resources could actually meet?"],
             "step": ("Use your money to meet one real need this week \u2014 someone specific, something "
                      "tangible. Notice the meaning it carries. Tell your partner the story.")},
            {"t": ["Generosity", "as Purpose"], "v": "\u201cIt is more blessed to give than to receive.\u201d \u2014 Acts 20:35",
             "tags": ["generosity", "blessing", "purpose", "Acts 20"],
             "q": ["Jesus says giving is the more blessed position. Where in your life has that proven true \u2014 where giving brought more joy than getting?",
                   "What stops generosity from being a purpose rather than an occasional act for you?",
                   "If generosity were the point of your financial life, what would change about how you earn and save?"],
             "step": ("Make generosity intentional this week \u2014 plan a gift in advance rather than "
                      "waiting for leftovers. Tell your partner what you planned and why.")},
            {"t": ["Treasure", "That Lasts"], "v": "\u201cStore up for yourselves treasures in heaven, where moths and vermin do not destroy.\u201d \u2014 Matthew 6:19\u201320",
             "tags": ["treasure", "eternity", "investment", "Matthew 6"],
             "q": ["Jesus contrasts treasure that rots with treasure that lasts. Which kind are you currently storing up the most?",
                   "What\u2019s one way to convert some earthly treasure into eternal treasure this year?",
                   "How does an eternal perspective change what feels worth spending on now?"],
             "step": ("Redirect one expense this week from temporary treasure toward eternal treasure "
                      "\u2014 a gift, a need, a Kingdom investment. Tell your partner what you moved.")},
            {"t": ["The Legacy", "You Leave"], "v": "\u201cA good person leaves an inheritance for their children\u2019s children.\u201d \u2014 Proverbs 13:22",
             "tags": ["legacy", "inheritance", "generations", "Proverbs 13"],
             "q": ["What kind of financial legacy are you building \u2014 not just in dollars, but in the values and habits your life is teaching?",
                   "Is the legacy you\u2019re leaving primarily material, or is it also wisdom, faith, and generosity?",
                   "What do you most want the people after you to remember about how you handled money?"],
             "step": ("Write a short \u2018money legacy\u2019 statement \u2014 what you want your handling of money to "
                      "pass on. Share it with your partner and with one family member if you can.")},
            {"t": ["Money", "on Mission"], "v": "\u201cYou will be enriched in every way so that you can be generous on every occasion.\u201d \u2014 2 Corinthians 9:11",
             "tags": ["mission", "generosity", "purpose", "2 Corinthians 9"],
             "q": ["After these weeks, what is the new \u2018what for\u2019 behind your money \u2014 the purpose that gives it meaning?",
                   "Where is God inviting you to put your money on mission \u2014 to fund something bigger than yourself?",
                   "What would it look like for generosity to be your normal, not your exception?"],
             "commit": ("Each person names the one purpose they will aim their money toward over the "
                        "next 90 days \u2014 a person, a cause, a Kingdom investment \u2014 and one person who "
                        "will ask how it\u2019s going. Close by praying that money becomes a tool for "
                        "meaning in every life in the room."),
             "tags_commit": True},
        ],
    },
    # 10 ----------------------------------------------------------------
    {
        "n": 10, "theme": "steel",
        "title": ["Peace", "with Money"],
        "category": "TITLE TEN · ENDING THE WAR & MAKING PEACE",
        "band_line": ("You can stop fighting with money \u2014 there is a way to live at peace with it, and "
                      "with the people you share it with \u2014 and these forty days end the war and "
                      "establish a lasting truce on God\u2019s terms."),
        "pull": "\u201cMany of us are at war with money. There is a way to lay down the weapons and make peace.\u201d",
        "body": ("For a lot of people, money isn\u2019t a tool \u2014 it\u2019s a battle. A war with anxiety, with "
                 "guilt, with shame over past mistakes, with a spouse across the kitchen table at "
                 "midnight. The fighting is exhausting, and no raise ends it, because the conflict "
                 "was never really about the numbers. Peace with Money is the capstone of the series. "
                 "It gathers everything \u2014 faith, wisdom, simplicity, peace, skill, the heart, health, "
                 "freedom, meaning \u2014 and brings it home to a single, hopeful conclusion: you can stop "
                 "fighting. There is a way to make peace with money, with your past, and with the "
                 "people you share it with, on terms God Himself sets."),
        "scripture": ("\u201cKeep your lives free from the love of money and be content with what you have, "
                      "because God has said, \u2018Never will I leave you, nor forsake you.\u2019\u201d",
                      "Hebrews 13:5 (NIV)"),
        "subtitles": [
            "A 40-Day Journey to Lasting Peace with Money",
            "Discovering How to End the War and Make Peace",
            "A 40-Day Path to Contentment, Forgiveness, and Rest",
            "Making Peace with Money \u2014 and the People You Share It With",
        ],
        "bigidea": ("Many of us are quietly at war with money \u2014 anxious, guilty, and conflicted. Peace "
                    "comes not when the balance changes but when we let God set the terms of the "
                    "relationship: contentment over craving, grace over shame, unity over strife."),
        "tags": ["peace", "contentment", "grace", "marriage", "rest", "reconciliation"],
        "info": {"Audience": "All church · married couples · those carrying money shame",
                 "Best Season": "New Year · Marriage season · Series capstone",
                 "Why it matters": "Money is the leading source of conflict in marriages"},
        "sessions": [
            {"t": ["The War", "We\u2019re In"], "v": "\u201cKeep your lives free from the love of money and be content with what you have.\u201d \u2014 Hebrews 13:5",
             "tags": ["conflict", "contentment", "honesty", "Hebrews 13"],
             "q": ["If money has felt like a battle, who or what are you really fighting \u2014 the numbers, your past, your spouse, or your own heart?",
                   "What does the \u2018war with money\u2019 cost you in energy, sleep, and relationships?",
                   "Hebrews ties contentment to \u2018Never will I leave you.\u2019 How could God\u2019s presence be the ground for peace the balance can\u2019t provide?"],
             "step": ("Name the specific \u2018war\u2019 you\u2019re in with money this week \u2014 what it\u2019s really about. "
                      "Write it down honestly and share it with your partner.")},
            {"t": ["Making Peace", "with Provision"], "v": "\u201cAnd my God will meet all your needs according to the riches of his glory.\u201d \u2014 Philippians 4:19",
             "tags": ["provision", "trust", "peace", "Philippians 4"],
             "q": ["Part of peace is trusting that God will provide. Where is it hardest for you to believe that promise right now?",
                   "What\u2019s the difference between God meeting your needs and God funding your fears? Which have you been asking for?",
                   "When have you seen God provide just enough, just in time? What did it teach you about peace?"],
             "step": ("Each day this week, thank God in advance for the provision you can\u2019t yet see, "
                      "and lay down one specific worry about it. Tell your partner what shifted.")},
            {"t": ["Peace in", "the Household"], "v": "\u201cDo two walk together unless they have agreed to do so?\u201d \u2014 Amos 3:3",
             "tags": ["marriage", "unity", "household", "Amos 3"],
             "q": ["Money is the number-one source of conflict in marriages and homes. What does the conversation about money sound like in yours?",
                   "Where do you and the people you share money with most disagree \u2014 spending, saving, giving, fear? What\u2019s underneath the disagreement?",
                   "What would it take to \u2018walk together, agreed\u2019 \u2014 to get on the same financial page with the people closest to you?"],
             "step": ("Have one calm, blame-free money conversation this week with your spouse, family, "
                      "or a close partner \u2014 just to get on the same page. Report how it went to the "
                      "group.")},
            {"t": ["Releasing Guilt", "and Shame"], "v": "\u201cTherefore, there is now no condemnation for those who are in Christ Jesus.\u201d \u2014 Romans 8:1",
             "tags": ["guilt", "grace", "no condemnation", "Romans 8"],
             "q": ["Many carry quiet shame over money mistakes. What past financial decision still weighs on you?",
                   "How does carrying that shame keep you from moving forward financially and spiritually?",
                   "What does \u2018no condemnation\u2019 mean for your money story \u2014 and could God be inviting you to set down what you\u2019ve been carrying?"],
             "step": ("Name one money regret to God, receive His grace over it, and take one forward "
                      "step instead of staying stuck in it. Share what you released with your partner.")},
            {"t": ["Peace Through", "Generosity"], "v": "\u201cA generous person will prosper; whoever refreshes others will be refreshed.\u201d \u2014 Proverbs 11:25",
             "tags": ["generosity", "peace", "refreshment", "Proverbs 11"],
             "q": ["Strangely, generosity often brings the peace that hoarding promises but never delivers. Have you experienced that?",
                   "Where is your grip tightest \u2014 and could loosening it be the very thing that brings peace?",
                   "Who could you refresh this week \u2014 and how might that refresh you?"],
             "step": ("Refresh someone this week through a generous act, and watch what it does to "
                      "your own sense of peace. Tell your partner what you did and what you felt.")},
            {"t": ["A Lasting", "Peace"], "v": "\u201cLet the peace of Christ rule in your hearts\u2026 And be thankful.\u201d \u2014 Colossians 3:15",
             "tags": ["peace", "thankfulness", "rest", "Colossians 3"],
             "q": ["After this whole series, what does \u2018peace with money\u2019 now mean to you that it didn\u2019t before?",
                   "Where has the war quieted \u2014 and where do you still need to keep laying down the weapons?",
                   "What one practice will keep the peace of Christ ruling over your finances after this ends?"],
             "commit": ("Each person names the one practice \u2014 contentment, household unity, released "
                        "shame, or generosity \u2014 they will keep so that peace rules their finances for "
                        "the next 90 days, and one person who will ask after their peace. Close by "
                        "praying a lasting peace over every person and every home in the room."),
             "tags_commit": True},
        ],
    },
]
