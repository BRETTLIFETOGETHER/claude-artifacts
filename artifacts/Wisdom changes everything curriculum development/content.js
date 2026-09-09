// ============ CONTENT DATA ============

const sessions = [
  {
    n: 1, h: "HONOR", title: "When God Owns It All", sub: "The Freedom of Surrender",
    line: "Surrendering ownership and finding peace in God\u2019s authority",
    verse: "Job 1:21", verseText: "\u201CThe Lord gave and the Lord has taken away; may the name of the Lord be praised.\u201D",
    big: "When ownership transfers to God, anxiety transfers off of you. Financial wisdom doesn\u2019t begin with behavior \u2014 it begins with belief. Everything changes when you stop carrying what God never asked you to own.",
    moves: [
      "God is the Creator, Owner, and Source of everything you have and everything you are.",
      "You are a steward, not a possessor \u2014 a manager, not the owner.",
      "The first spiritual act of financial health is surrender, not strategy.",
      "Honor unlocks perspective, peace, and worship before it ever touches a budget."
    ],
    outcome: "People stop hiding and pretending, and start releasing. They make one honest declaration: \u201CLord, all I have is Yours.\u201D",
    tool: "The Owner-to-Steward Audit \u2014 naming what you grip most tightly and what changes when you manage it for God.",
    assess: "Where am I with ownership? (Do my habits match what I say I believe?)",
    practice: "Each morning, before the phone: \u201CLord, all I have is Yours. Show me how to manage it today.\u201D Then release one specific thing in writing.",
    goal: "Move from control to trust"
  },
  {
    n: 2, h: "HEART", title: "What Money Reveals", sub: "The Battle Beneath the Budget",
    line: "Letting God heal the fear, comparison, and emotions behind money",
    verse: "Matthew 6:21", verseText: "\u201CFor where your treasure is, there your heart will be also.\u201D",
    big: "Money is never just a math problem \u2014 it\u2019s a matter of the heart. What looks like a spending issue is usually a trust issue. Healing begins when God reveals the emotions beneath the decisions.",
    moves: [
      "Why money triggers fear, shame, guilt, comparison, or pride.",
      "The hidden emotional \u201Cscripts\u201D we inherited without choosing them.",
      "Contentment is learned, not natural (Philippians 4:11\u201312).",
      "Gratitude and worship are what actually realign the heart."
    ],
    outcome: "People identify their dominant financial emotion and offer it to God \u2014 beginning the shift from fear to faith and from comparison to contentment.",
    tool: "The Contentment & Comparison Check \u2014 surfacing the one comparison that most steals your peace.",
    assess: "What is my money doing in me? (A heart audit, not a behavior audit.)",
    practice: "Keep a daily gratitude list of what you already have; each time comparison rises, name it and give thanks instead.",
    goal: "Break the comparison trap"
  },
  {
    n: 3, h: "HABITS", title: "Wisdom in Motion", sub: "Small Choices That Shape a Life",
    line: "Building daily practices that create margin, freedom, and stability",
    verse: "Luke 16:10", verseText: "\u201CWhoever can be trusted with very little can also be trusted with much.\u201D",
    big: "Habits are where transformation becomes sustainable. Stewardship is discipleship \u2014 your daily choices reveal what you truly trust. Wisdom is more about rhythm than willpower.",
    moves: [
      "The five biblical habits: spend less than you earn, avoid debt, plan for margin, set godly goals, live generously.",
      "Why habits fail \u2014 emotional resistance and \u201Cbudget baggage.\u201D",
      "How consistency, little by little, builds freedom over time."
    ],
    outcome: "People take one practical step \u2014 they create or revise a simple 30-day spending plan and treat it as worship, not restriction.",
    tool: "The 30-Day Spending Plan \u2014 clarity, not control; a plan that lets your money follow your faith.",
    assess: "Which of the five habits is my weakest right now \u2014 and why?",
    practice: "Build (or rebuild) one habit. Pick a single area \u2014 giving, saving, or one spending category \u2014 and set one rule for the week.",
    goal: "Replace confusion with clarity"
  },
  {
    n: 4, h: "HEALTH", title: "From Pressure to Peace", sub: "Aligning Faith, Finances, and Family",
    line: "Aligning your financial, spiritual, and relational life for wholeness",
    verse: "Proverbs 3:5\u20138", verseText: "\u201CTrust in the Lord with all your heart \u2026 this will bring health to your body.\u201D",
    big: "True financial health isn\u2019t measured by income \u2014 it\u2019s measured by alignment. Peace comes when your faith, your relationships, and your finances are moving in the same direction. Margin is mercy.",
    moves: [
      "Wholeness versus fragmentation \u2014 when one area is out of sync, the whole life feels it.",
      "How financial health mirrors spiritual health.",
      "The connection between margin and peace.",
      "God\u2019s design for balance, rest, and rhythm."
    ],
    outcome: "People complete a Financial Health Assessment and name one area that\u2019s out of alignment \u2014 then take one step toward margin in it.",
    tool: "The Freedom Ladder + Debt-to-Peace Tracker \u2014 locating where you are and the next rung toward stability.",
    assess: "Where is my life fragmented? (Faith / finances / family alignment.)",
    practice: "Choose your one out-of-alignment area and take a single, concrete step toward margin this week.",
    goal: "Build margin, reduce anxiety"
  },
  {
    n: 5, h: "HOPE", title: "Living for What Lasts", sub: "Defining Enough and Trusting God\u2019s Future",
    line: "Replacing anxiety with long-term confidence in God\u2019s provision",
    verse: "Philippians 4:6\u20137", verseText: "\u201CDo not be anxious about anything \u2026 and the peace of God will guard your hearts.\u201D",
    big: "Hope is not optimism. Hope is anchored confidence in Christ that steadies your decisions even when circumstances shake. Without a definition of enough, you will always be chasing more.",
    moves: [
      "Hope (capital H) versus hope (lowercase) \u2014 confidence in God\u2019s character, not your circumstances.",
      "How fear of the future quietly shapes financial behavior.",
      "Why financial anxiety is a spiritual issue, not a budgeting issue.",
      "Defining \u201Cenough\u201D so generosity and rest become possible."
    ],
    outcome: "People release their greatest financial worry to God, begin praying daily for wisdom and peace, and take a first pass at defining their own \u201Cfinish line.\u201D",
    tool: "Define Enough + the Legacy Map \u2014 naming a finish line and what you want your money to be for.",
    assess: "Where does fear of the future drive my money decisions?",
    practice: "Write down your greatest financial worry, release it in prayer daily, and draft one sentence describing what \u201Cenough\u201D looks like for you.",
    goal: "Live with vision beyond self"
  },
  {
    n: 6, h: "HARVEST", title: "Open Hands, Lasting Impact", sub: "Multiplying Generosity for Kingdom Purpose",
    line: "Multiplying generosity and impact for generations to come",
    verse: "John 15:8", verseText: "\u201CThis is to my Father\u2019s glory, that you bear much fruit.\u201D",
    big: "Generosity is the visible evidence that God owns it all. When hands open, hearts fill and lives multiply. Legacy is not mainly what you leave for people \u2014 it\u2019s what you leave in them.",
    moves: [
      "Giving is the final step of stewardship \u2014 the proof of trust.",
      "Generosity breaks money\u2019s grip and outlives the giver.",
      "Legacy is measured in lives changed, not assets transferred.",
      "Open hands become God\u2019s open doors."
    ],
    outcome: "People choose one intentional act of generosity, families begin writing Legacy Letters, and the group celebrates real stories of transformation from the journey.",
    tool: "The Generosity Plan + Legacy Letter Starter \u2014 turning conviction into a concrete next act and a written blessing.",
    assess: "Am I living open-handed \u2014 and what would multiplication look like for me?",
    practice: "Take one intentional, specific act of generosity this week, and begin a Legacy Letter to someone you love.",
    goal: "Move from maintenance to multiplication"
  }
];

const weeks = [
  { h: "HONOR", title: "God Owns It All", focus: "The theology of ownership \u2014 surrender and peace.", days: [
    ["1", "The Owner of Everything", "Establishing the foundation of all financial wisdom", "Psalm 24:1"],
    ["2", "The Illusion of Ownership", "Why we assume control that was never ours", "Deuteronomy 8:17\u201318"],
    ["3", "The Transfer of Ownership", "The decisive moment of surrender", "Luke 16:11"],
    ["4", "The Stewardship Mandate", "Living as a manager, not an owner", "1 Corinthians 4:2"],
    ["5", "Every Decision Is Spiritual", "Money as a tool, test, and testimony", "Luke 16:10"],
    ["6", "God as Provider", "Replacing self-reliance with trust", "Matthew 6:31\u201333"],
    ["7", "The Surrendered Life", "Living fully under God\u2019s ownership", "Proverbs 3:5\u20136"]
  ]},
  { h: "HEART", title: "What Money Reveals", focus: "The contentment journey \u2014 gratitude over greed.", days: [
    ["8", "Where Your Treasure Is", "The connection between money and the heart", "Matthew 6:21"],
    ["9", "Fear and Security", "Why money feels like safety", "Hebrews 13:5"],
    ["10", "The Comparison Trap", "When someone else defines your life", "2 Corinthians 10:12"],
    ["11", "Joy in Enough", "Discovering contentment", "1 Timothy 6:6"],
    ["12", "Wealth or Worship", "What are you really pursuing?", "Matthew 6:24"],
    ["13", "Learning to Be Content", "A discipline of the heart", "Philippians 4:11\u201312"],
    ["14", "The Heart Check", "What money is doing in you", "Luke 12:15"]
  ]},
  { h: "HABITS", title: "Wisdom in Motion", focus: "The practice of stewardship \u2014 systems of wisdom.", days: [
    ["15", "The Five Uses of Money", "The framework for every financial decision", "Luke 16:10"],
    ["16", "The Principle of Planning", "Intentional living versus reactive spending", "Proverbs 21:5"],
    ["17", "Spending with Purpose", "Aligning values with decisions", "Matthew 6:33"],
    ["18", "The Discipline of Giving", "Generosity as a structured priority", "2 Corinthians 9:6\u20137"],
    ["19", "Building Margin", "Creating capacity for freedom", "Proverbs 27:23"],
    ["20", "Faithfulness in Process", "Consistency over time", "Luke 16:10"],
    ["21", "The Long-Term Mindset", "Decisions that shape a lifetime", "Galatians 6:7"]
  ]},
  { h: "HEALTH", title: "From Pressure to Peace", focus: "The integration of life and finances \u2014 from stress to stability.", days: [
    ["22", "The Freedom Ladder", "Understanding your current position", "Proverbs 21:20"],
    ["23", "The Budget of Peace", "A plan aligned with purpose", "Proverbs 21:5"],
    ["24", "Debt Doesn\u2019t Define You", "Understanding its true impact", "Proverbs 22:7"],
    ["25", "Healthy Boundaries", "Living within God\u2019s design", "Hebrews 13:5"],
    ["26", "Faith Over Fear", "Trusting God in uncertainty", "Isaiah 41:10"],
    ["27", "Building Reserves", "Preparing for the unexpected", "Proverbs 6:6\u20138"],
    ["28", "Rest and Renewal", "Living from peace, not pressure", "Matthew 11:28"]
  ]},
  { h: "HOPE", title: "Living for What Lasts", focus: "The eternal perspective \u2014 purpose and legacy.", days: [
    ["29", "Why We Give", "Aligning with God\u2019s mission", "Acts 20:35"],
    ["30", "Seed and Harvest", "The principle of multiplication", "2 Corinthians 9:10"],
    ["31", "Richer in Heaven", "Investing in eternity", "Matthew 6:20"],
    ["32", "Passing the Torch", "Teaching the next generation", "Proverbs 13:22"],
    ["33", "Faith for the Future", "Trusting what you cannot see", "Hebrews 11:1"],
    ["34", "Stories That Last", "Living a life worth telling", "Psalm 145:4"],
    ["35", "The Joy of Hope", "Living with confidence and purpose", "Romans 15:13"]
  ]},
  { h: "HARVEST", title: "Open Hands, Lasting Impact", focus: "Multiplying what matters \u2014 movement and mission.", days: [
    ["36", "Blessed to Be a Blessing", "Living beyond yourself", "Genesis 12:2"],
    ["37", "Living Sent", "Your life on mission", "Matthew 28:19"],
    ["38", "Your Story as Seed", "Multiplying through influence", "2 Corinthians 9:11"],
    ["39", "A Legacy Life", "What you leave behind", "Psalm 112:6"],
    ["40", "Wisdom Changes Everything", "From ownership to overflow", "John 15:8"]
  ]}
];

module.exports = { sessions, weeks };
