const { sessions } = require("./content2.js");

// [num, title, subtitle, verse, daily prompt]  — subtitles are the project's 40-day research subtitles
const weeks = [
  { h: "HONOR", title: "God Owns It All", focus: "The theology of ownership \u2014 surrender and peace.", days: [
    ["1", "The Owner of Everything", "Establishing the foundation of all financial wisdom", "Psalm 24:1", "Name three things today that came from God\u2019s hand. How does holding them as a manager change how you use them?"],
    ["2", "The Illusion of Ownership", "Why we assume control that was never ours", "Deuteronomy 8:17\u201318", "Where are you quietly saying \u201CI built this\u201D? Thank God for one thing you didn\u2019t earn."],
    ["3", "The Transfer of Ownership", "The decisive moment of surrender", "Luke 16:11", "What decision are you gripping? Picture handing it to the Owner."],
    ["4", "The Stewardship Mandate", "Living as a manager, not an owner", "1 Corinthians 4:2", "The bar is faithfulness, not results. Where does that lift pressure off you today?"],
    ["5", "Every Decision Is Spiritual", "Money as a tool, test, and testimony", "Luke 16:10", "Make one small money decision today as a deliberate act of worship."],
    ["6", "God as Provider", "Replacing self-reliance with trust", "Matthew 6:31\u201333", "Where are you anxious about provision? Name a time God came through before."],
    ["7", "The Surrendered Life", "Living fully under God\u2019s ownership", "Proverbs 3:5\u20136", "Surrender is daily. What\u2019s one thing to re-surrender right now?"]
  ]},
  { h: "HEART", title: "What Money Reveals", focus: "The contentment journey \u2014 gratitude over greed.", days: [
    ["8", "The Comparison Trap", "When someone else defines your life", "2 Corinthians 10:12", "Whose life are you measuring against? Hand that comparison to God."],
    ["9", "Joy in Enough", "Discovering contentment", "1 Timothy 6:6", "List five things you already have that you once prayed for."],
    ["10", "When God Says \u201CRest\u201D", "Trusting without striving", "Psalm 46:10", "Where do you need to stop striving and trust God\u2019s provision today?"],
    ["11", "Practicing Gratitude", "Shifting your focus", "1 Thessalonians 5:18", "Write down three things you\u2019re grateful for before you ask for anything."],
    ["12", "Wealth or Worship", "What are you really pursuing?", "Matthew 6:24", "Be honest \u2014 where does money compete for first place today?"],
    ["13", "Learning to Be Content", "A discipline of the heart", "Philippians 4:11\u201312", "Contentment is learned. What are you \u201Cin school\u201D for right now?"],
    ["14", "Heart Check", "What money is doing in you", "Luke 12:15", "Where is \u201Cmore\u201D loudest in you? Speak gratitude over it instead."]
  ]},
  { h: "HABITS", title: "Wisdom in Motion", focus: "The practice of stewardship \u2014 systems of wisdom.", days: [
    ["15", "The Five Uses of Money", "The framework for every financial decision", "Luke 16:10", "Of give, save, owe, live, grow \u2014 which is weakest? Take one step."],
    ["16", "The Principle of Planning", "Intentional living versus reactive spending", "Proverbs 21:5", "Where are you reactive with money? Make one plan today."],
    ["17", "Spending with Purpose", "Aligning values with decisions", "Matthew 6:33", "Before one purchase today, ask: does this reflect my values or reshape them?"],
    ["18", "The Discipline of Giving", "Generosity as a structured priority", "2 Corinthians 9:6\u20137", "Plan one gift in advance instead of giving on impulse."],
    ["19", "Building Margin", "Creating capacity for freedom", "Proverbs 27:23", "Look honestly at one number you\u2019ve been avoiding."],
    ["20", "Faithfulness in Process", "Consistency over time", "Luke 16:10", "Pick one small habit and do it today, even imperfectly."],
    ["21", "The Long-Term Mindset", "Decisions that shape a lifetime", "Galatians 6:7", "What is today\u2019s habit sowing for ten years from now?"]
  ]},
  { h: "HEALTH", title: "From Pressure to Peace", focus: "The integration of life and finances \u2014 from stress to stability.", days: [
    ["22", "The Freedom Ladder", "Understanding your current position", "Proverbs 21:20", "Honestly locate yourself on the ladder. What\u2019s the next rung?"],
    ["23", "The Budget of Peace", "A plan aligned with purpose", "Proverbs 21:5", "A plan is clarity, not a cage. Name one thing a plan would calm."],
    ["24", "Debt Doesn\u2019t Define You", "Understanding its true impact", "Proverbs 22:7", "Debt describes a situation, not your future. Name one next step."],
    ["25", "Healthy Boundaries", "Living within God\u2019s design", "Hebrews 13:5", "Where do you need a \u201Cno\u201D to protect a \u201Cyes\u201D?"],
    ["26", "Faith Over Fear", "Trusting God in uncertainty", "Isaiah 41:10", "What financial fear needs to hear \u201Cdo not fear, I am with you\u201D?"],
    ["27", "Building Reserves", "Preparing for the unexpected", "Proverbs 6:6\u20138", "The ant stores in season. What small reserve could you start?"],
    ["28", "Rest and Renewal", "Living from peace, not pressure", "Matthew 11:28", "Bring one money weight to Jesus and leave it there today."]
  ]},
  { h: "HOPE", title: "Living for What Lasts", focus: "The eternal perspective \u2014 purpose and legacy.", days: [
    ["29", "Why We Give", "Aligning with God\u2019s mission", "Acts 20:35", "Recall a time giving brought you more joy than keeping did."],
    ["30", "Seed and Harvest", "The principle of multiplication", "2 Corinthians 9:10", "What \u201Cseed\u201D is in your hand right now to sow?"],
    ["31", "Richer in Heaven", "Investing in eternity", "Matthew 6:20", "Name one eternal investment you could make this week."],
    ["32", "Passing the Torch", "Teaching the next generation", "Proverbs 13:22", "What wisdom \u2014 not just wealth \u2014 do you want to pass on?"],
    ["33", "Faith for the Future", "Trusting what you cannot see", "Hebrews 11:1", "Act today on one promise you can\u2019t yet see."],
    ["34", "Stories That Last", "Living a life worth telling", "Psalm 145:4", "What story of God\u2019s provision could you tell the next generation?"],
    ["35", "The Joy of Hope", "Living with confidence and purpose", "Romans 15:13", "Where do you need hope to overflow into a money decision?"]
  ]},
  { h: "HARVEST", title: "Open Hands, Lasting Impact", focus: "Multiplying what matters \u2014 movement and mission.", days: [
    ["36", "Blessed to Be a Blessing", "Living beyond yourself", "Genesis 12:2", "You\u2019re blessed to bless. Whom could you bless this week?"],
    ["37", "Living Sent", "Your life on mission", "Matthew 28:19", "How could your resources serve God\u2019s mission today?"],
    ["38", "Your Story as Seed", "Multiplying through influence", "2 Corinthians 9:11", "Your testimony multiplies. Who needs to hear yours?"],
    ["39", "A Legacy Life", "What you leave behind", "Psalm 112:6", "What do you want remembered \u2014 and how do today\u2019s choices build it?"],
    ["40", "Wisdom Changes Everything", "From ownership to overflow", "John 15:8", "Looking back over 40 days: what has changed? Thank God; take one next step."]
  ]}
];

// Fully written sample devotional days (to show the daily reading format)
const devSamples = [
  {
    num: "1", title: "The Owner of Everything", subtitle: "Establishing the foundation of all financial wisdom",
    verse: "Psalm 24:1", verseText: "The earth is the Lord\u2019s, and everything in it, the world, and all who live in it.",
    reading: "Financial wisdom doesn\u2019t begin with a budget. It begins with a question most of us never stop to answer: who actually owns all of this? Psalm 24:1 answers without hedging \u2014 the earth is the Lord\u2019s, and everything in it. Everything. Not most things, not just the spiritual things, not what\u2019s left after taxes. The house, the paycheck, the retirement account, the car in the driveway, the breath in your lungs \u2014 all of it, His. We resist this, because ownership feels like security. But ownership is also a weight: if it\u2019s all mine, then it all depends on me. Stewardship sets that weight down. If God owns it all, then your job isn\u2019t to carry it \u2014 it\u2019s to manage it well and trust the Owner. Everything you\u2019ll learn over the next forty days grows from this single root. Settle it here, and the rest begins to follow.",
    reflect: "Name three things today that came from God\u2019s hand. How does holding them as a manager \u2014 not an owner \u2014 change how you\u2019ll use them?",
    pray: "Father, You own it all. Loosen my grip and lift the weight I was never meant to carry. Teach me to manage well what is already Yours. Amen."
  },
  {
    num: "2", title: "The Illusion of Ownership", subtitle: "Why we assume control that was never ours",
    verse: "Deuteronomy 8:17\u201318", verseText: "You may say to yourself, \u201CMy power and the strength of my hands have produced this wealth.\u201D But remember the Lord your God, for it is he who gives you the ability to produce wealth.",
    reading: "It\u2019s a quiet lie, and most of us believe it without noticing: \u201CMy power and the strength of my hands produced this.\u201D Moses warned Israel about it on the edge of the Promised Land, right when they were about to get comfortable. Prosperity has a way of erasing the memory of where it came from. We work hard, we plan, we earn \u2014 and slowly we start to believe it\u2019s all self-made. The illusion of ownership isn\u2019t just inaccurate; it\u2019s exhausting. It makes us anxious about losing what we think we built and proud of what we think we earned. Deuteronomy 8 doesn\u2019t shame the work; it reframes it. God gives you the very ability to produce wealth. Even your capacity to earn is a gift. Remembering that doesn\u2019t make you smaller \u2014 it makes you free. The Giver is still giving.",
    reflect: "Where are you quietly saying \u201CI built this\u201D? Thank God for one specific thing you didn\u2019t actually earn on your own.",
    pray: "Father, forgive the illusion that I am self-made. Everything I have \u2014 including the strength to earn it \u2014 came from You. Keep me grateful and free. Amen."
  }
];

module.exports = { sessions, weeks, devSamples };
