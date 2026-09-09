# -*- coding: utf-8 -*-
"""Generate the LifeTogether 'Finances Collection' brochure as a single standalone HTML file.
Aesthetic direction borrowed from the Flourishing Series PDF; all written content is original."""

import html

# ---------------------------------------------------------------------------
# Collection-level content
# ---------------------------------------------------------------------------
COLLECTION = {
    "eyebrow": "LIFETOGETHER · THE FINANCES COLLECTION · TEN TIER-ONE CAMPAIGNS",
    "title_line1": "Money,",
    "title_line2_italic": "honestly.",
    "deck": ("Ten complete campaign and small-group series for the one conversation every "
             "person is already having in private — and almost no one is having out loud. "
             "Built for the church and the workplace alike, rooted in Scripture, and "
             "designed for 30-day deployment."),
    "framework": ("Faith &amp; Finances names the heart behind the wallet. Financial Wisdom builds "
                  "the skill. Money Made Simple clears the noise. Financial Peace calms the fear. "
                  "Wise with Money forms the habit. God, Money &amp; Me makes it personal. Financial "
                  "Health takes the long view. Breaking Financial Fear ends the cycle. Money and "
                  "Meaning answers what it is all for. Peace with Money is where every road leads."),
    "intro": [
        ("Money is the quiet weight under ordinary days. It is the 3&nbsp;a.m. math, the unopened "
         "envelope, the argument that was never really about the grocery bill. People can recite "
         "their theology and still feel a low hum of dread every time they check the balance — and "
         "they almost never say so. Not at work. Not at church. Sometimes not even at home."),
        ("This is the conversation a congregation and a company are both desperate to have and "
         "strangely unable to start. The Finances Collection starts it for them — ten Tier-One "
         "campaigns that meet people exactly where the stress lives, name the real problem under "
         "the numbers, and walk them toward a different relationship with money: one built on "
         "trust instead of fear, clarity instead of chaos, and generosity instead of scarcity."),
    ],
    "closing_title_a": "Ten doors.",
    "closing_title_b_italic": "One freedom.",
    "closing_body": [
        ("Every one of these campaigns opens onto the same room — a life that holds money "
         "open-handed instead of being held by it. Some people need to start with their fear. "
         "Some need a plan. Some need permission to make it simple. The collection meets each "
         "of them at their own door and leads them to the same place: peace."),
        ("Whether you launch one campaign this season or build a year of them, you are handing "
         "your people the most practical, most personal, most avoided conversation there is — "
         "and you are handing it to them with hope attached."),
    ],
    "cta_label": "START THE CONVERSATION",
    "cta_line": "Pick a door. Launch a campaign. Watch the weight lift.",
    "contact": "Brett Eastman · Founder, Lifetogether · brett@lifetogether.com · The Finances Collection · Ten-Campaign Platform",
}

# ---------------------------------------------------------------------------
# Per-title content (all original)
# Each: accent (dark panel), tint (page wash), num, eyebrow, title, title_italic,
# strap, quote, problem, transformation, scripture, scripture_ref, big_idea, tags[],
# subtitles[], info{}, sessions[ {n,title,title_italic,verse,line} ]
# ---------------------------------------------------------------------------
TITLES = [
    {
        "accent": "#1e2d4f", "accent_soft": "#2c3f66", "tint": "#eef1f8",
        "num": "1", "eyebrow": "CAMPAIGN ONE · THE HEART BEHIND THE WALLET",
        "title": "Faith &amp;", "title_italic": "Finances",
        "strap": ("Before money is a math problem, it is a faith problem — and getting the heart right "
                  "is what finally makes the numbers lighter to carry."),
        "quote": ("Show me your calendar and your bank statement, and I will show you what you "
                  "actually believe."),
        "problem": ("Most of us treat money as a spreadsheet and then wonder why it keeps breaking our "
                    "hearts. We budget the symptoms and never touch the source. But every financial "
                    "decision is quietly a spiritual one — a small vote for what we trust, what we fear, "
                    "and who we think is really in charge of our provision."),
        "transformation": ("Faith &amp; Finances moves money out of the place of anxiety and into the place "
                           "of worship. When trust replaces fear at the root, generosity, patience, and "
                           "peace start to grow on their own. This is the first campaign in the "
                           "collection because it is the soil everything else is planted in."),
        "scripture": ("No one can serve two masters. Either you will hate the one and love the other, "
                      "or you will be devoted to the one and despise the other. You cannot serve both "
                      "God and money."),
        "scripture_ref": "Matthew 6:24 (NIV)",
        "big_idea": ("Every financial decision is a spiritual decision in disguise. When the heart is "
                     "settled in trust, money stops being a master and becomes what it was always meant "
                     "to be — a tool in the hands of a free and grateful person."),
        "tags": ["trust", "provision", "worship", "first principles", "the heart"],
        "subtitles": [
            "A 30-Day Journey to a Trusting Relationship with Money",
            "Discovering What God Has to Say About Your Wallet",
            "A 30-Day Path from Money Anxiety to Money as Worship",
        ],
        "info": {
            "Audience": "All church &amp; workplace — the right place to begin",
            "Best Season": "January · Fall stewardship · Series launch",
            "Best For": "First-time money conversations, mixed audiences",
            "Felt Need": "Money stress rooted in trust and fear",
        },
        "sessions": [
            {"n": "1", "title": "The Money Behind", "ti": "the Money", "verse": "Matthew 6:21",
             "line": "Where your treasure is, your heart follows — so we start by finding out where it already is."},
            {"n": "2", "title": "Two Masters,", "ti": "One Heart", "verse": "Matthew 6:24",
             "line": "Naming the quiet rivalry between trusting God and trusting the balance."},
            {"n": "3", "title": "The God Who", "ti": "Provides", "verse": "Philippians 4:19",
             "line": "Trading the math of scarcity for the memory of a Father who has always come through."},
            {"n": "4", "title": "An Open", "ti": "Hand", "verse": "1 Timothy 6:17-18",
             "line": "What changes the moment we decide to hold everything we have a little more loosely."},
        ],
    },
    {
        "accent": "#1f3a2c", "accent_soft": "#2c5440", "tint": "#edf4ef",
        "num": "2", "eyebrow": "CAMPAIGN TWO · PRACTICAL WISDOM FOR REAL DECISIONS",
        "title": "Financial", "title_italic": "Wisdom",
        "strap": ("Most money trouble is not a lack of income — it is a lack of a plan you actually "
                  "follow, and wisdom is just good decisions made before the pressure hits."),
        "quote": ("A plan you keep beats a fortune you fumble. Wisdom is the difference between "
                  "earning money and keeping it."),
        "problem": ("Good people make money decisions one panic at a time. Without a simple framework, "
                    "every choice — the purchase, the loan, the splurge, the gift — feels like a gamble "
                    "made in the moment. The result is a life that is busy with money and never quite "
                    "ahead of it."),
        "transformation": ("Financial Wisdom replaces reaction with rhythm. Drawing on the plain, "
                           "field-tested wisdom of Proverbs, it builds the decision-making muscle behind "
                           "the budget so that the right move becomes the natural one — long before the "
                           "bill, the temptation, or the emergency arrives."),
        "scripture": ("The plans of the diligent lead to profit as surely as haste leads to poverty."),
        "scripture_ref": "Proverbs 21:5 (NIV)",
        "big_idea": ("Wisdom is good decisions made early. This campaign trains people to think before "
                     "they spend, plan before they panic, and build the kind of quiet financial "
                     "diligence that compounds into freedom over time."),
        "tags": ["wisdom", "planning", "diligence", "decisions", "Proverbs"],
        "subtitles": [
            "A 30-Day Journey to Wiser Money Decisions",
            "Discovering God's Practical Design for Your Finances",
            "A 30-Day Path from Reacting to Planning",
        ],
        "info": {
            "Audience": "All church &amp; workplace — every income level",
            "Best Season": "New Year · Back-to-school · Budget season",
            "Best For": "Practical learners, young families, professionals",
            "Felt Need": "Budgeting, planning, money decision fatigue",
        },
        "sessions": [
            {"n": "1", "title": "The Plan Before", "ti": "the Pressure", "verse": "Proverbs 21:5",
             "line": "Why diligence quietly out-earns hustle, and how to build a plan you will actually keep."},
            {"n": "2", "title": "Borrowing", "ti": "and Bondage", "verse": "Proverbs 22:7",
             "line": "An honest look at debt — what it costs, what it owns, and the first step out."},
            {"n": "3", "title": "Honoring", "ti": "God First", "verse": "Proverbs 3:9-10",
             "line": "The counterintuitive math of putting the first portion in God's hands."},
            {"n": "4", "title": "Slow Money", "ti": "Grows", "verse": "Proverbs 13:11",
             "line": "Trading the lottery mindset for the patient, ordinary discipline that lasts."},
        ],
    },
    {
        "accent": "#15403f", "accent_soft": "#1f5b59", "tint": "#eaf4f3",
        "num": "3", "eyebrow": "CAMPAIGN THREE · CLARITY OVER COMPLEXITY",
        "title": "Money Made", "title_italic": "Simple",
        "strap": ("You do not need a finance degree. You need one honest page, four simple moves, and "
                  "the courage to stop avoiding the conversation."),
        "quote": ("Clarity is kindness. The moment money gets simple, peace gets possible."),
        "problem": ("Money feels complicated on purpose — apps, accounts, advice, and a hundred "
                    "competing voices — until people freeze and avoid it altogether. Avoidance feels "
                    "like relief for about a day, and then the same dread comes back heavier. "
                    "Complexity is not a sign of sophistication; it is the thing keeping people stuck."),
        "transformation": ("Money Made Simple strips it all back to what fits on one page and can be "
                           "kept by anyone. Four uncomplicated moves replace forty anxious ones. "
                           "Participants leave with a budget they understand, a rhythm they can keep, "
                           "and the calm that comes from finally being able to look."),
        "scripture": ("But seek first his kingdom and his righteousness, and all these things will be "
                      "given to you as well."),
        "scripture_ref": "Matthew 6:33 (NIV)",
        "big_idea": ("Simplicity is the doorway to peace. When the whole picture fits on one honest "
                     "page, fear loses its hiding place — and an ordinary person can finally manage "
                     "their money instead of being managed by it."),
        "tags": ["simplicity", "clarity", "budgeting", "margin", "focus"],
        "subtitles": [
            "A 30-Day Journey to a Money Plan You Understand",
            "Discovering the Beautiful Simplicity of Stewardship",
            "A 30-Day Path from Overwhelmed to Clear",
        ],
        "info": {
            "Audience": "All church &amp; workplace — especially the overwhelmed",
            "Best Season": "January · Any season · New-believer track",
            "Best For": "Avoiders, beginners, the financially anxious",
            "Felt Need": "Overwhelm, avoidance, complexity, no system",
        },
        "sessions": [
            {"n": "1", "title": "One Honest", "ti": "Page", "verse": "Luke 14:28",
             "line": "Counting the cost on purpose — the freeing act of writing the whole truth down once."},
            {"n": "2", "title": "The Four-Move", "ti": "Budget", "verse": "Proverbs 27:23",
             "line": "Know the state of your flocks: a four-move plan simple enough to actually keep."},
            {"n": "3", "title": "Enough,", "ti": "on Purpose", "verse": "1 Timothy 6:6-8",
             "line": "Why naming 'enough' is the quiet superpower that makes simplicity stick."},
            {"n": "4", "title": "A Rhythm", "ti": "You Can Keep", "verse": "Matthew 6:34",
             "line": "Trading the someday overhaul for a small weekly rhythm that holds for years."},
        ],
    },
    {
        "accent": "#16324f", "accent_soft": "#214a70", "tint": "#ebf1f7",
        "num": "4", "eyebrow": "CAMPAIGN FOUR · FROM ANXIETY TO PEACE",
        "title": "Financial", "title_italic": "Peace",
        "strap": ("The bill is real. So is the peace that is bigger than the bill — a calm that does "
                  "not depend on the number in the account."),
        "quote": ("Peace is not a balance in an account. It is a trust in a Father — and that kind of "
                  "peace survives the actual numbers."),
        "problem": ("For millions of people, money is the anxiety running quietly underneath everything "
                    "else: the avoidance, the shame, the math that wakes them at 3&nbsp;a.m., the "
                    "argument that erupts over something small. They are not bad with money. They are "
                    "tired of being afraid of it."),
        "transformation": ("Financial Peace moves money from the place of dread to the place of prayer. "
                           "It teaches contentment as a skill that can be practiced, gives anxious "
                           "people language for the fear, and surrounds them with a community that "
                           "carries the weight together. The goal is not a bigger number — it is a "
                           "quieter heart."),
        "scripture": ("Do not be anxious about anything, but in every situation, by prayer and petition, "
                      "with thanksgiving, present your requests to God. And the peace of God, which "
                      "transcends all understanding, will guard your hearts and your minds in Christ "
                      "Jesus."),
        "scripture_ref": "Philippians 4:6-7 (NIV)",
        "big_idea": ("Financial peace is not the absence of financial problems — it is the presence of "
                     "enough trust that the problems no longer run the heart. This campaign hands "
                     "anxious people a peace that can survive the actual numbers."),
        "tags": ["peace", "anxiety", "trust", "contentment", "rest"],
        "subtitles": [
            "A 30-Day Journey from Money Anxiety to Genuine Peace",
            "Discovering the Calm Beneath the Numbers",
            "A 30-Day Path to a Quieter Heart About Money",
        ],
        "info": {
            "Audience": "All church &amp; workplace — high stress, all incomes",
            "Best Season": "January · Post-holidays · Tax season",
            "Best For": "The anxious, over-functioners, stressed households",
            "Felt Need": "Money stress, anxiety, shame, sleepless nights",
        },
        "sessions": [
            {"n": "1", "title": "The 3 A.M.", "ti": "Math", "verse": "Philippians 4:6-7",
             "line": "Bringing the anxious midnight arithmetic into the light, and into prayer."},
            {"n": "2", "title": "Naming", "ti": "the Fear", "verse": "Psalm 23:1",
             "line": "What it does to fear when we name it honestly before the Shepherd who provides."},
            {"n": "3", "title": "Contentment", "ti": "as a Skill", "verse": "Philippians 4:11-13",
             "line": "Paul learned to be content — which means it can be practiced, not just wished for."},
            {"n": "4", "title": "Carrying It", "ti": "Together", "verse": "Galatians 6:2",
             "line": "Why money fear loses its grip the moment it stops being a secret."},
        ],
    },
    {
        "accent": "#3a3115", "accent_soft": "#5a4c22", "tint": "#f5f1e5",
        "num": "5", "eyebrow": "CAMPAIGN FIVE · THE EVERYDAY STEWARD",
        "title": "Wise with", "title_italic": "Money",
        "strap": ("Faithfulness is not measured by the size of the account — it is measured by what "
                  "you do, today, with whatever is already in it."),
        "quote": ("Stewardship does not start someday when there is more. It starts now, with this "
                  "paycheck, this decision, this dollar."),
        "problem": ("People put off being generous, organized, or wise until 'someday' — when there is "
                    "more margin, more income, more time. But someday never has a date, and the habits "
                    "we postpone are exactly the ones that would have created the margin we are waiting "
                    "for. The delay is the trap."),
        "transformation": ("Wise with Money replaces waiting with stewarding. It builds small, faithful "
                           "habits — the weekly review, the first-fruit gift, the unhurried decision — "
                           "that compound quietly into freedom. Faithful in little, the campaign "
                           "insists, is the only road that has ever led to faithful in much."),
        "scripture": ("His master replied, 'Well done, good and faithful servant! You have been faithful "
                      "with a few things; I will put you in charge of many things.'"),
        "scripture_ref": "Matthew 25:21 (NIV)",
        "big_idea": ("Stewardship is a today decision, not a someday dream. The person who is faithful "
                     "with a little builds the character, the habits, and the trust that turn ordinary "
                     "income into extraordinary freedom over a lifetime."),
        "tags": ["stewardship", "faithfulness", "habits", "generosity", "ownership"],
        "subtitles": [
            "A 30-Day Journey to Faithful, Everyday Stewardship",
            "Discovering the Habits That Build Financial Freedom",
            "A 30-Day Path from Waiting to Stewarding",
        ],
        "info": {
            "Audience": "All church &amp; workplace — every season of life",
            "Best Season": "Fall stewardship · New Year · Any season",
            "Best For": "Habit-builders, givers-in-training, all stages",
            "Felt Need": "Inconsistency, postponed habits, drift",
        },
        "sessions": [
            {"n": "1", "title": "Faithful", "ti": "in Little", "verse": "Matthew 25:21",
             "line": "Why the small, unseen decisions are the ones that actually shape a financial life."},
            {"n": "2", "title": "The Steward's", "ti": "Mindset", "verse": "1 Corinthians 4:2",
             "line": "Moving from owner to manager — and the surprising relief that comes with it."},
            {"n": "3", "title": "Habits", "ti": "That Hold", "verse": "Proverbs 24:27",
             "line": "Putting first things first: the simple rhythms that quietly build margin over time."},
            {"n": "4", "title": "Generous", "ti": "on Purpose", "verse": "Acts 20:35",
             "line": "Discovering, by practice, that it really is more blessed to give than to receive."},
        ],
    },
    {
        "accent": "#3a1f3d", "accent_soft": "#562f5a", "tint": "#f3edf4",
        "num": "6", "eyebrow": "CAMPAIGN SIX · THE MOST PERSONAL MONEY STORY",
        "title": "God, Money", "title_italic": "&amp; Me",
        "strap": ("Your relationship with money started long before your first paycheck — and naming "
                  "that story is where real freedom begins."),
        "quote": ("This is not a series about the economy. It is a series about you, your story, and "
                  "the God who wants to rewrite it."),
        "problem": ("We inherit money stories — scarcity, striving, secrecy, shame — usually before we "
                    "are old enough to remember learning them. Then we spend adulthood running scripts "
                    "we never chose, mistaking them for personality or even principle. The numbers are "
                    "never really the issue. The story underneath them is."),
        "transformation": ("God, Money &amp; Me is the most personal campaign in the collection. It "
                           "gently surfaces the inherited story, names the idols and fears hiding inside "
                           "it, and reconnects a person's worth to something deeper than net worth. The "
                           "result is not just a better budget — it is a freed heart."),
        "scripture": ("Then he said to them, 'Watch out! Be on your guard against all kinds of greed; "
                      "life does not consist in an abundance of possessions.'"),
        "scripture_ref": "Luke 12:15 (NIV)",
        "big_idea": ("Your money story was written into you early — but it is not the final word. When "
                     "worth is rooted in God rather than in the balance, the inherited script of fear "
                     "and striving can finally be rewritten."),
        "tags": ["identity", "healing", "scarcity", "story", "freedom"],
        "subtitles": [
            "A 30-Day Journey into Your Personal Money Story",
            "Discovering the God Who Rewrites What You Inherited",
            "A 30-Day Path from Inherited Fear to a Free Heart",
        ],
        "info": {
            "Audience": "All church &amp; workplace — deeper, reflective track",
            "Best Season": "Lent · Small-group season · Any season",
            "Best For": "Reflective groups, those ready to go deeper",
            "Felt Need": "Scarcity mindset, money shame, inherited fear",
        },
        "sessions": [
            {"n": "1", "title": "Where It", "ti": "Started", "verse": "Luke 12:15",
             "line": "Tracing the money story you absorbed before you could choose it."},
            {"n": "2", "title": "Naming", "ti": "the Idols", "verse": "Colossians 3:5",
             "line": "Gently surfacing what money has quietly come to promise — security, status, control."},
            {"n": "3", "title": "Worth Beyond", "ti": "Worth", "verse": "Luke 12:6-7",
             "line": "Reattaching your value to the Father who counts the hairs on your head."},
            {"n": "4", "title": "A New", "ti": "Story", "verse": "2 Corinthians 5:17",
             "line": "Stepping into the new-creation freedom that lets you hold money without fear."},
        ],
    },
    {
        "accent": "#13362b", "accent_soft": "#1d5040", "tint": "#e9f2ee",
        "num": "7", "eyebrow": "CAMPAIGN SEVEN · THE LONG, SUSTAINABLE VIEW",
        "title": "Financial", "title_italic": "Health",
        "strap": ("Financial health is not a finish line you cross once — it is an ordinary, "
                  "sustainable way of living you can keep for forty years."),
        "quote": ("Healthy finances look boring on purpose: margin, no surprises, and room to be "
                  "generous. The boredom is the breakthrough."),
        "problem": ("Most people crash-diet their finances — a burst of intense discipline after a "
                    "scare, followed by a quiet slide back to the old patterns. The cycle is "
                    "exhausting and it never compounds. Health is not a sprint of willpower; it is a "
                    "rhythm a person can actually sustain when life gets normal again."),
        "transformation": ("Financial Health builds the durable, unglamorous wellness that lasts: "
                           "margin instead of edge-living, a buffer instead of a crisis, and the long "
                           "view instead of the next emergency. It trades the dramatic overhaul for "
                           "the steady habits that quietly produce a resilient, generous, peaceful "
                           "financial life."),
        "scripture": ("Dear friend, I pray that you may enjoy good health and that all may go well with "
                      "you, even as your soul is getting along well."),
        "scripture_ref": "3 John 1:2 (NIV)",
        "big_idea": ("Real financial health is sustainable, not heroic. It is the unglamorous habit of "
                     "living with margin, building a buffer, and taking the long view — the kind of "
                     "ordinary wellness that holds up across decades, not just for one disciplined month."),
        "tags": ["health", "margin", "sustainability", "resilience", "long view"],
        "subtitles": [
            "A 30-Day Journey to Sustainable Financial Wellness",
            "Discovering the Habits That Last for Decades",
            "A 30-Day Path from Crisis Cycles to Lasting Margin",
        ],
        "info": {
            "Audience": "All church &amp; workplace — the long-haul track",
            "Best Season": "New Year · Mid-year reset · Any season",
            "Best For": "Crisis-cycle breakers, families, planners",
            "Felt Need": "Living on the edge, no buffer, repeated crises",
        },
        "sessions": [
            {"n": "1", "title": "Margin", "ti": "Is Health", "verse": "Proverbs 21:20",
             "line": "Why the wise store up a little — and how a small buffer changes everything."},
            {"n": "2", "title": "Out of the", "ti": "Crisis Cycle", "verse": "Proverbs 6:6-8",
             "line": "Learning from the ant: storing in the good season so the hard one does not flatten you."},
            {"n": "3", "title": "Building", "ti": "Resilience", "verse": "Genesis 41:35-36",
             "line": "Joseph's seven-year plan, scaled down to a buffer that absorbs life's surprises."},
            {"n": "4", "title": "Health", "ti": "That Lasts", "verse": "Proverbs 15:16",
             "line": "Better a little with the fear of the Lord — choosing the rhythm you can keep for life."},
        ],
    },
    {
        "accent": "#46201f", "accent_soft": "#6b322f", "tint": "#f6ece9",
        "num": "8", "eyebrow": "CAMPAIGN EIGHT · BREAKING THE CYCLE",
        "title": "Breaking", "title_italic": "Financial Fear",
        "strap": ("Fear is an expensive landlord — driving the avoidance, the impulse buy, and the "
                  "debt that feels like a sentence. It is time to stop paying its rent."),
        "quote": ("Fear and debt feed each other. Break the loop, and you do not just fix the numbers "
                  "— you get your courage back."),
        "problem": ("Fear drives the worst money decisions: the avoidance that lets the problem grow, "
                    "the impulse spending that soothes for an hour, the silence in a marriage, the "
                    "debt that starts to feel like a life sentence. People are not failing for lack of "
                    "information. They are stuck in a cycle of dread that keeps them from looking at "
                    "all."),
        "transformation": ("Breaking Financial Fear faces the cycle head-on. It helps people look at "
                           "the actual number without flinching, name the fear out loud, and take one "
                           "concrete step toward free — then another. With courage, a plan, and a "
                           "community walking alongside, the loop finally breaks and freedom becomes "
                           "a real direction, not a fantasy."),
        "scripture": ("For the Spirit God gave us does not make us timid, but gives us power, love and "
                      "self-discipline."),
        "scripture_ref": "2 Timothy 1:7 (NIV)",
        "big_idea": ("Fear is the engine under most money trouble, and debt is the fuel it runs on. "
                     "This campaign breaks the cycle — replacing timidity with the power, love, and "
                     "self-discipline that God actually gives, one courageous step at a time."),
        "tags": ["fear", "freedom", "debt", "courage", "breakthrough"],
        "subtitles": [
            "A 30-Day Journey from Fear and Debt to Freedom",
            "Discovering the Courage to Face the Number",
            "A 30-Day Path Out of the Money-Fear Cycle",
        ],
        "info": {
            "Audience": "All church &amp; workplace — those feeling trapped",
            "Best Season": "January · After the holidays · Any season",
            "Best For": "Debt-burdened, fear-driven, the stuck and silent",
            "Felt Need": "Debt, fear, avoidance, feeling trapped",
        },
        "sessions": [
            {"n": "1", "title": "Facing", "ti": "the Number", "verse": "2 Timothy 1:7",
             "line": "The brave first act: looking at the real total with the Spirit's courage, not timidity."},
            {"n": "2", "title": "The Bondage", "ti": "of Borrowing", "verse": "Proverbs 22:7",
             "line": "An honest reckoning with what debt costs and what it quietly owns."},
            {"n": "3", "title": "One Step", "ti": "Toward Free", "verse": "Luke 14:28",
             "line": "Counting the cost and choosing one concrete, doable move out of the cycle."},
            {"n": "4", "title": "Walking Out", "ti": "Together", "verse": "Romans 13:8",
             "line": "Owe no one anything but love — and why the journey to free is never walked alone."},
        ],
    },
    {
        "accent": "#27264f", "accent_soft": "#3a3970", "tint": "#eeeef7",
        "num": "9", "eyebrow": "CAMPAIGN NINE · WHAT MONEY IS ACTUALLY FOR",
        "title": "Money and", "title_italic": "Meaning",
        "strap": ("The question was never how much. It was always what for — and answering it turns "
                  "money from a master into the means of a meaningful life."),
        "quote": ("Money is a terrible master and a wonderful tool. Aimed at meaning, it becomes the "
                  "means of a generous, joy-filled, and eternal life."),
        "problem": ("People chase more and arrive empty. They accumulate the thing they were sure would "
                    "satisfy, only to find the goalposts have quietly moved again. Somewhere in the "
                    "pursuit of money, the point of money got lost — and a full account can sit right "
                    "next to a hollow life."),
        "transformation": ("Money and Meaning reconnects the dollars to a purpose worth having. It "
                           "reframes wealth as a tool for generosity, for legacy, and for investing in "
                           "what actually lasts. Participants stop asking 'how do I get more?' and "
                           "start asking 'what is this for?' — and discover the life that is truly "
                           "life."),
        "scripture": ("Command them to do good, to be rich in good deeds, and to be generous and "
                      "willing to share. In this way they will lay up treasure for themselves as a firm "
                      "foundation for the coming age, so that they may take hold of the life that is "
                      "truly life."),
        "scripture_ref": "1 Timothy 6:18-19 (NIV)",
        "big_idea": ("The point of money was never accumulation — it was contribution. When wealth is "
                     "aimed at generosity and eternal things, it stops being a hollow pursuit and "
                     "becomes the means of taking hold of the life that is truly life."),
        "tags": ["meaning", "generosity", "purpose", "eternity", "legacy"],
        "subtitles": [
            "A 30-Day Journey from Accumulating to Investing in What Lasts",
            "Discovering What Your Money Is Actually For",
            "A 30-Day Path from More to Meaning",
        ],
        "info": {
            "Audience": "All church &amp; workplace — including the comfortable",
            "Best Season": "Year-end giving · Fall · Any season",
            "Best For": "Givers, leaders, the successful-but-empty",
            "Felt Need": "Emptiness, purpose, generosity, legacy",
        },
        "sessions": [
            {"n": "1", "title": "What Is", "ti": "It For?", "verse": "1 Timothy 6:18-19",
             "line": "Reopening the oldest question — and discovering money was always meant to be aimed."},
            {"n": "2", "title": "The Generosity", "ti": "Reflex", "verse": "2 Corinthians 9:7",
             "line": "Becoming a cheerful giver — and how generosity quietly rewires a heart."},
            {"n": "3", "title": "Investing in", "ti": "What Lasts", "verse": "Matthew 6:19-21",
             "line": "Storing treasure where moth and rust do not reach, and the heart follows."},
            {"n": "4", "title": "The Life That", "ti": "Is Truly Life", "verse": "Luke 12:33-34",
             "line": "Trading the hollow chase for the full, generous life God calls truly alive."},
        ],
    },
    {
        "accent": "#163a34", "accent_soft": "#1f5650", "tint": "#eaf2ef",
        "num": "10", "eyebrow": "CAMPAIGN TEN · WHERE EVERY ROAD LEADS",
        "title": "Peace with", "title_italic": "Money",
        "strap": ("You can make peace with money — not by finally having more of it, but by learning "
                  "to hold it differently for the rest of your life."),
        "quote": ("Peace with money is contentment plus trust. When God is enough, money finally "
                  "stops running the show."),
        "problem": ("Even people with enough rarely feel at peace with money. There is a low-grade war "
                    "underneath the comfort — the comparison, the never-enough, the guilt, the quiet "
                    "sense that more would finally settle it. It never does. The war is not about the "
                    "amount; it is about the grip."),
        "transformation": ("Peace with Money is where every road in this collection leads. It cures "
                           "comparison with gratitude, replaces never-enough with contentment, and "
                           "anchors the whole relationship in the God who promised never to leave. The "
                           "result is a settled, grateful, free relationship with money that can hold "
                           "for a lifetime."),
        "scripture": ("Keep your lives free from the love of money and be content with what you have, "
                      "because God has said, 'Never will I leave you nor forsake you.'"),
        "scripture_ref": "Hebrews 13:5 (NIV)",
        "big_idea": ("Peace with money is not a balance you reach — it is a posture you choose: "
                     "contented, grateful, and anchored in a God who will never leave. When He is "
                     "enough, the war finally ends and money becomes something you hold instead of "
                     "something that holds you."),
        "tags": ["contentment", "peace", "gratitude", "rest", "freedom"],
        "subtitles": [
            "A 30-Day Journey to a Settled, Grateful Relationship with Money",
            "Discovering Contentment That Does Not Depend on the Balance",
            "A 30-Day Path from the Quiet War to Lasting Peace",
        ],
        "info": {
            "Audience": "All church &amp; workplace — a fitting series finale",
            "Best Season": "New Year · Series conclusion · Any season",
            "Best For": "Everyone — the destination of the collection",
            "Felt Need": "Comparison, never-enough, restlessness, guilt",
        },
        "sessions": [
            {"n": "1", "title": "The Quiet", "ti": "War", "verse": "Hebrews 13:5",
             "line": "Naming the low-grade money war that comfort never quite ends — and its real cure."},
            {"n": "2", "title": "The Cure for", "ti": "Comparison", "verse": "Galatians 6:4",
             "line": "Why measuring your life against someone else's is the thief of every financial peace."},
            {"n": "3", "title": "Gratitude Changes", "ti": "the Math", "verse": "1 Thessalonians 5:18",
             "line": "How a daily practice of thanks quietly turns 'not enough' into 'more than enough.'"},
            {"n": "4", "title": "At Peace", "ti": "for Good", "verse": "Philippians 4:11-12",
             "line": "Learning Paul's secret of contentment in any circumstance — and keeping it for life."},
        ],
    },
]

GOLD = "#c9a13b"
GOLD_LT = "#dcc074"
NAVY = "#172542"
INK = "#1c1c1c"
CREAM = "#f9f5ec"

# ---------------------------------------------------------------------------
# HTML assembly
# ---------------------------------------------------------------------------

def tags_html(tags, cls="tag"):
    return "".join(f'<span class="{cls}">{t}</span>' for t in tags)

def overview_cards():
    cards = []
    for t in TITLES:
        cards.append(f"""
        <div class="ov-card" style="--ac:{t['accent']};--tint:{t['tint']}">
          <div class="ov-num">{t['num']}</div>
          <div class="ov-body">
            <div class="ov-title">{t['title']} <em>{t['title_italic']}</em></div>
            <div class="ov-sub">{t['subtitles'][0]}</div>
            <div class="ov-badges"><span>30-Day</span><span>4-Session</span><span>Tier&nbsp;1</span></div>
          </div>
        </div>""")
    return "\n".join(cards)

def session_cards(t):
    cells = []
    for s in t["sessions"]:
        cells.append(f"""
          <div class="sess">
            <div class="sess-head">
              <div class="sess-label">SESSION {s['n']}</div>
              <div class="sess-title">{s['title']} <em>{s['ti']}</em></div>
            </div>
            <div class="sess-verse">{s['verse']}</div>
            <p class="sess-line">{s['line']}</p>
          </div>""")
    return "\n".join(cells)

def info_rows(info):
    rows = []
    for k, v in info.items():
        rows.append(f'<li><span class="ik">{k}</span><span class="iv">{v}</span></li>')
    rows.insert(0, '<li><span class="ik">Format</span><span class="iv">30-Day Journey + 4-Session Small Group</span></li>')
    rows.append('<li><span class="ik">Tier</span><span class="iv">Tier 1 — top-demand category</span></li>')
    return "\n".join(rows)

def subtitle_box(subs):
    items = "".join(f"<p>{s}</p>" for s in subs)
    return f'<div class="subbox"><div class="boxlabel">SUBTITLE OPTIONS</div>{items}</div>'

def title_spread(t):
    return f"""
  <section class="spread" style="--ac:{t['accent']};--ac-soft:{t['accent_soft']};--tint:{t['tint']}">
    <header class="band">
      <div class="band-num">{t['num']}</div>
      <div class="band-text">
        <div class="eyebrow gold">{t['eyebrow']}</div>
        <h2 class="band-title">{t['title']} <em>{t['title_italic']}</em></h2>
        <p class="strap">{t['strap']}</p>
      </div>
    </header>

    <div class="cols">
      <div class="col-main">
        <p class="pullquote">&ldquo;{t['quote']}&rdquo;</p>
        <p class="body"><span class="lede">The problem.</span> {t['problem']}</p>
        <p class="body"><span class="lede">The transformation.</span> {t['transformation']}</p>
        <div class="scripture">
          <div class="boxlabel light">CORE SCRIPTURE</div>
          <p class="verse">&ldquo;{t['scripture']}&rdquo;</p>
          <div class="verse-ref">— {t['scripture_ref']}</div>
        </div>
      </div>
      <aside class="col-side">
        <div class="infobox">
          <div class="boxlabel light">CAMPAIGN INFORMATION</div>
          <ul class="info">
            {info_rows(t['info'])}
          </ul>
        </div>
        {subtitle_box(t['subtitles'])}
      </aside>
    </div>

    <div class="bigidea">
      <div class="boxlabel light">THE BIG IDEA</div>
      <p>{t['big_idea']}</p>
      <div class="tags">{tags_html(t['tags'], "tag light")}</div>
    </div>

    <div class="curriculum">
      <div class="curr-label">SMALL-GROUP CURRICULUM — FOUR SESSIONS</div>
      <div class="sess-grid">
        {session_cards(t)}
      </div>
    </div>
  </section>"""

spreads = "\n".join(title_spread(t) for t in TITLES)
overview = overview_cards()

HTML = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>The Finances Collection · Lifetogether</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,500;0,600;0,700;0,800;1,500;1,600;1,700&family=Spectral:ital,wght@0,300;0,400;0,500;0,600;1,400;1,500&family=Archivo:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>
  :root{{
    --gold:{GOLD}; --gold-lt:{GOLD_LT}; --navy:{NAVY}; --ink:{INK}; --cream:{CREAM};
  }}
  *{{box-sizing:border-box;}}
  html{{-webkit-text-size-adjust:100%;}}
  body{{
    margin:0; background:#e7e2d6; color:var(--ink);
    font-family:'Spectral',Georgia,serif; line-height:1.6;
    -webkit-font-smoothing:antialiased;
  }}
  .page{{
    max-width:940px; margin:0 auto; background:#fff;
    box-shadow:0 1px 60px rgba(20,30,55,.14);
  }}
  .eyebrow{{
    font-family:'Archivo',sans-serif; font-weight:600; font-size:11px;
    letter-spacing:.28em; text-transform:uppercase;
  }}
  .gold{{color:var(--gold);}}
  em{{font-style:italic;}}

  /* ---------- COVER ---------- */
  .cover{{
    background:
      radial-gradient(120% 90% at 78% -10%, rgba(201,161,59,.20), transparent 55%),
      linear-gradient(160deg,#1c2c50 0%, var(--navy) 55%, #111d36 100%);
    color:#f3eee2; padding:88px 70px 64px; position:relative; overflow:hidden;
  }}
  .cover::before{{
    content:""; position:absolute; left:0; right:0; top:0; height:6px;
    background:linear-gradient(90deg,var(--gold),var(--gold-lt));
  }}
  .cover .eyebrow{{color:var(--gold-lt); margin-bottom:38px;}}
  .cover h1{{
    font-family:'Playfair Display',serif; font-weight:700;
    font-size:104px; line-height:.94; margin:0 0 26px; letter-spacing:-.02em;
  }}
  .cover h1 em{{color:var(--gold-lt); font-weight:600;}}
  .cover .deck{{
    font-size:21px; line-height:1.55; max-width:600px; color:#e6ddc9;
    font-weight:300; margin:0 0 46px;
  }}
  .cover-strip{{
    display:flex; gap:0; border-top:1px solid rgba(220,192,116,.32);
    padding-top:26px; flex-wrap:wrap;
  }}
  .cover-strip div{{
    flex:1 1 0; min-width:140px; padding:4px 22px 4px 0;
    border-right:1px solid rgba(220,192,116,.18);
  }}
  .cover-strip div:last-child{{border-right:0;}}
  .cs-big{{font-family:'Playfair Display',serif; font-size:38px; color:var(--gold-lt); line-height:1;}}
  .cs-lab{{font-family:'Archivo',sans-serif; font-size:10.5px; letter-spacing:.18em; text-transform:uppercase; color:#cdc3ac; margin-top:8px;}}

  /* ---------- FRAMEWORK ---------- */
  .frame{{padding:66px 70px 60px; background:var(--cream);}}
  .frame .section-eyebrow{{color:var(--gold); margin-bottom:22px; display:block;}}
  .frame-quote{{
    background:var(--navy); color:#efe9da; border-radius:3px;
    padding:34px 40px; margin:0 0 46px; position:relative;
  }}
  .frame-quote::before{{
    content:""; position:absolute; left:0; top:0; bottom:0; width:4px;
    background:linear-gradient(var(--gold),var(--gold-lt));
  }}
  .frame-quote .boxlabel{{margin-bottom:14px;}}
  .frame-quote p{{
    font-family:'Spectral',serif; font-style:italic; font-size:18.5px;
    line-height:1.62; margin:0; color:#f1ead9;
  }}
  .frame-intro p{{font-size:17px; line-height:1.72; margin:0 0 18px; color:#33312c;}}

  /* ---------- OVERVIEW GRID ---------- */
  .overview{{padding:56px 70px 64px; background:#fff;}}
  .overview h3{{
    font-family:'Playfair Display',serif; font-weight:600; font-size:30px;
    margin:0 0 6px; color:var(--navy);
  }}
  .overview .sub{{font-size:15px; color:#6f6a5d; margin:0 0 34px; font-style:italic;}}
  .ov-grid{{display:grid; grid-template-columns:1fr 1fr; gap:16px;}}
  .ov-card{{
    display:flex; gap:18px; align-items:stretch;
    background:var(--tint); border-radius:4px; overflow:hidden;
    border:1px solid rgba(0,0,0,.05);
  }}
  .ov-num{{
    flex:0 0 56px; background:var(--ac); color:#fff;
    font-family:'Playfair Display',serif; font-size:30px; font-weight:600;
    display:flex; align-items:center; justify-content:center;
  }}
  .ov-body{{padding:14px 18px 14px 0;}}
  .ov-title{{font-family:'Playfair Display',serif; font-size:21px; color:var(--navy); line-height:1.1;}}
  .ov-title em{{color:var(--ac);}}
  .ov-sub{{font-size:12.5px; color:#5f5a4f; margin:5px 0 9px; font-style:italic; line-height:1.4;}}
  .ov-badges span{{
    font-family:'Archivo',sans-serif; font-size:9px; letter-spacing:.1em; text-transform:uppercase;
    background:rgba(0,0,0,.06); color:#4a463d; padding:3px 8px; border-radius:20px; margin-right:5px;
  }}

  /* ---------- TITLE SPREAD ---------- */
  .spread{{background:var(--tint); padding:0 0 58px;}}
  .band{{
    background:var(--ac); color:#fff; padding:46px 70px 40px;
    display:flex; gap:30px; align-items:flex-start; position:relative; overflow:hidden;
  }}
  .band::after{{
    content:""; position:absolute; left:0; right:0; bottom:0; height:4px;
    background:linear-gradient(90deg,var(--gold),var(--gold-lt));
  }}
  .band-num{{
    font-family:'Playfair Display',serif; font-size:118px; font-weight:700;
    line-height:.8; color:rgba(255,255,255,.14); margin-top:-6px; flex:0 0 auto;
  }}
  .band-text{{padding-top:8px;}}
  .band .eyebrow{{color:var(--gold-lt); margin-bottom:14px; display:block;}}
  .band-title{{
    font-family:'Playfair Display',serif; font-weight:700; font-size:52px;
    margin:0 0 14px; line-height:1; letter-spacing:-.01em;
  }}
  .band-title em{{color:var(--gold-lt); font-weight:600;}}
  .strap{{font-size:16.5px; line-height:1.55; max-width:620px; color:rgba(255,255,255,.86); margin:0; font-style:italic; font-weight:300;}}

  .cols{{display:grid; grid-template-columns:1.55fr 1fr; gap:34px; padding:44px 70px 0;}}
  .pullquote{{
    font-family:'Playfair Display',serif; font-style:italic; font-weight:500;
    font-size:26px; line-height:1.32; color:var(--ac); margin:0 0 26px; letter-spacing:-.01em;
  }}
  .body{{font-size:15.5px; line-height:1.72; margin:0 0 18px; color:#322f2a;}}
  .lede{{font-family:'Archivo',sans-serif; font-weight:700; font-size:11px; letter-spacing:.12em; text-transform:uppercase; color:var(--ac); margin-right:6px;}}
  .scripture{{
    background:var(--ac); color:#f3eee2; border-radius:3px; padding:26px 30px; margin-top:28px;
  }}
  .scripture .verse{{font-family:'Spectral',serif; font-style:italic; font-size:17px; line-height:1.55; margin:0 0 12px; color:#f4eedd;}}
  .verse-ref{{font-family:'Archivo',sans-serif; font-size:11px; letter-spacing:.14em; text-transform:uppercase; color:var(--gold-lt);}}

  .col-side > div{{margin-bottom:18px;}}
  .infobox{{background:var(--ac); color:#eee; border-radius:3px; padding:22px 24px;}}
  .info{{list-style:none; margin:0; padding:0;}}
  .info li{{display:flex; flex-direction:column; padding:9px 0; border-bottom:1px solid rgba(255,255,255,.12);}}
  .info li:last-child{{border-bottom:0; padding-bottom:0;}}
  .ik{{font-family:'Archivo',sans-serif; font-size:9.5px; letter-spacing:.16em; text-transform:uppercase; color:var(--gold-lt); margin-bottom:3px;}}
  .iv{{font-size:13.5px; line-height:1.4; color:#f2eee4;}}
  .subbox{{background:#fff; border:1px solid rgba(0,0,0,.08); border-left:3px solid var(--gold); border-radius:3px; padding:20px 22px;}}
  .subbox p{{font-style:italic; font-size:13.5px; line-height:1.4; margin:0 0 10px; color:#4f4a40;}}
  .subbox p:last-child{{margin-bottom:0;}}

  .boxlabel{{font-family:'Archivo',sans-serif; font-weight:700; font-size:10px; letter-spacing:.2em; text-transform:uppercase; color:var(--ac); margin-bottom:12px;}}
  .boxlabel.light{{color:var(--gold-lt);}}

  .bigidea{{
    margin:36px 70px 0; background:var(--ac-soft);
    color:#f4efe4; border-radius:3px; padding:32px 38px;
  }}
  .bigidea p{{
    font-family:'Playfair Display',serif; font-style:italic; font-weight:500;
    font-size:22px; line-height:1.42; margin:0 0 20px; color:#f6f0e3; letter-spacing:-.005em;
  }}
  .tags{{display:flex; flex-wrap:wrap; gap:8px;}}
  .tag{{
    font-family:'Archivo',sans-serif; font-size:10.5px; letter-spacing:.06em;
    background:rgba(255,255,255,.10); color:#efe8d8; padding:5px 12px; border-radius:20px;
    border:1px solid rgba(255,255,255,.16);
  }}

  .curriculum{{margin:40px 70px 0;}}
  .curr-label{{font-family:'Archivo',sans-serif; font-weight:700; font-size:10.5px; letter-spacing:.24em; text-transform:uppercase; color:var(--ac); border-bottom:1px solid rgba(0,0,0,.12); padding-bottom:12px; margin-bottom:20px;}}
  .sess-grid{{display:grid; grid-template-columns:1fr 1fr; gap:16px;}}
  .sess{{background:#fff; border:1px solid rgba(0,0,0,.07); border-radius:4px; overflow:hidden;}}
  .sess-head{{background:var(--ac); color:#fff; padding:14px 18px 13px;}}
  .sess-label{{font-family:'Archivo',sans-serif; font-size:9px; letter-spacing:.2em; text-transform:uppercase; color:var(--gold-lt); margin-bottom:5px;}}
  .sess-title{{font-family:'Playfair Display',serif; font-size:19px; line-height:1.05;}}
  .sess-title em{{color:var(--gold-lt);}}
  .sess-verse{{font-family:'Archivo',sans-serif; font-size:10.5px; letter-spacing:.1em; text-transform:uppercase; color:var(--ac); padding:13px 18px 0;}}
  .sess-line{{font-size:13.5px; line-height:1.55; color:#403c34; padding:6px 18px 18px; margin:0; font-style:italic;}}

  /* ---------- CLOSING ---------- */
  .closing{{
    background:
      radial-gradient(120% 100% at 20% 0%, rgba(201,161,59,.18), transparent 55%),
      linear-gradient(150deg,#1b2b4f, var(--navy) 60%, #101c34);
    color:#f1ebdc; padding:80px 70px 70px; position:relative;
  }}
  .closing::before{{content:""; position:absolute; left:0; right:0; top:0; height:6px; background:linear-gradient(90deg,var(--gold),var(--gold-lt));}}
  .closing .eyebrow{{color:var(--gold-lt); margin-bottom:26px; display:block;}}
  .closing h2{{font-family:'Playfair Display',serif; font-weight:700; font-size:64px; line-height:.98; margin:0 0 32px; letter-spacing:-.02em;}}
  .closing h2 em{{color:var(--gold-lt); font-weight:600;}}
  .closing .cbody{{max-width:620px;}}
  .closing .cbody p{{font-size:17px; line-height:1.7; color:#e3dac6; margin:0 0 18px; font-weight:300;}}
  .cta{{margin-top:42px; padding-top:30px; border-top:1px solid rgba(220,192,116,.3);}}
  .cta-label{{font-family:'Archivo',sans-serif; font-weight:700; font-size:11px; letter-spacing:.26em; text-transform:uppercase; color:var(--gold-lt); margin-bottom:14px;}}
  .cta-line{{font-family:'Playfair Display',serif; font-style:italic; font-size:27px; line-height:1.3; color:#f4eede; margin:0;}}

  /* ---------- FOOTER ---------- */
  .footer{{background:#0e1830; color:#9aa3b6; font-family:'Archivo',sans-serif; font-size:11px; letter-spacing:.1em; padding:20px 70px; text-align:center;}}
  .footer .gold{{color:var(--gold-lt);}}

  /* ---------- RESPONSIVE ---------- */
  @media(max-width:760px){{
    .cover{{padding:60px 30px 44px;}}
    .cover h1{{font-size:62px;}}
    .frame,.overview,.closing{{padding-left:30px; padding-right:30px;}}
    .band{{padding:34px 30px 30px; flex-direction:column; gap:8px;}}
    .band-num{{font-size:74px;}}
    .band-title{{font-size:38px;}}
    .cols{{grid-template-columns:1fr; padding:32px 30px 0; gap:24px;}}
    .bigidea,.curriculum{{margin-left:30px; margin-right:30px;}}
    .sess-grid,.ov-grid{{grid-template-columns:1fr;}}
    .closing h2{{font-size:44px;}}
    .footer{{padding:18px 24px;}}
  }}

  /* ---------- PRINT ---------- */
  @media print{{
    body{{background:#fff;}}
    .page{{box-shadow:none; max-width:none;}}
    .cover,.closing{{-webkit-print-color-adjust:exact; print-color-adjust:exact;}}
    .spread, .cover, .frame, .overview, .closing{{page-break-inside:avoid; break-inside:avoid;}}
    .spread{{page-break-before:always;}}
    .band, .scripture, .infobox, .bigidea, .sess-head, .frame-quote, .ov-num{{-webkit-print-color-adjust:exact; print-color-adjust:exact;}}
  }}
  @page{{margin:0;}}
</style>
</head>
<body>
<div class="page">

  <!-- COVER -->
  <section class="cover">
    <div class="eyebrow">{COLLECTION['eyebrow']}</div>
    <h1>{COLLECTION['title_line1']}<br><em>{COLLECTION['title_line2_italic']}</em></h1>
    <p class="deck">{COLLECTION['deck']}</p>
    <div class="cover-strip">
      <div><div class="cs-big">10</div><div class="cs-lab">Tier-One Campaigns</div></div>
      <div><div class="cs-big">30</div><div class="cs-lab">Day Journey Each</div></div>
      <div><div class="cs-big">40</div><div class="cs-lab">Small-Group Sessions</div></div>
      <div><div class="cs-big">2</div><div class="cs-lab">Audiences · Church &amp; Work</div></div>
    </div>
  </section>

  <!-- FRAMEWORK -->
  <section class="frame">
    <span class="eyebrow section-eyebrow">THE GOVERNING FRAMEWORK</span>
    <div class="frame-quote">
      <div class="boxlabel light">ONE COLLECTION · TEN DOORS</div>
      <p>{COLLECTION['framework']}</p>
    </div>
    <div class="frame-intro">
      <p>{COLLECTION['intro'][0]}</p>
      <p>{COLLECTION['intro'][1]}</p>
    </div>
  </section>

  <!-- OVERVIEW -->
  <section class="overview">
    <h3>The collection at a glance.</h3>
    <p class="sub">Ten complete campaigns — each a stand-alone 30-day journey with four-session small-group curriculum.</p>
    <div class="ov-grid">
      {overview}
    </div>
  </section>

  <!-- TITLE SPREADS -->
  {spreads}

  <!-- CLOSING -->
  <section class="closing">
    <span class="eyebrow">WHY THIS CAMPAIGN MATTERS</span>
    <h2>{COLLECTION['closing_title_a']}<br><em>{COLLECTION['closing_title_b_italic']}</em></h2>
    <div class="cbody">
      <p>{COLLECTION['closing_body'][0]}</p>
      <p>{COLLECTION['closing_body'][1]}</p>
    </div>
    <div class="cta">
      <div class="cta-label">{COLLECTION['cta_label']}</div>
      <p class="cta-line">{COLLECTION['cta_line']}</p>
    </div>
  </section>

  <div class="footer"><span class="gold">Lifetogether</span> &nbsp;·&nbsp; {COLLECTION['contact']}</div>

</div>
</body>
</html>"""

out = "/mnt/user-data/outputs/Finances_Collection_Lifetogether.html"
with open(out, "w", encoding="utf-8") as f:
    f.write(HTML)

print("WROTE", out)
print("bytes:", len(HTML))
