const {
  Document, Packer, Paragraph, TextRun, HeadingLevel,
  AlignmentType, PageBreak, BorderStyle, ShadingType,
  LevelFormat, WidthType, Table, TableRow, TableCell
} = require('docx');
const fs = require('fs');

// ─────────────────────────────────────────────
// DATA: 40-Day Devotional Framework
// Organized into 6 Movements drawn from RBI source material
// ─────────────────────────────────────────────

const movements = [
  {
    number: 1,
    title: "MOVEMENT ONE: WHO REALLY OWNS THIS?",
    subtitle: "Days 1–7 | The Foundation of Everything",
    description: "Before any budget, any plan, any spreadsheet — there is a question of ownership. These seven days establish the theological and emotional bedrock of the entire journey: God owns it all. Everything changes when that becomes more than a phrase.",
    days: [
      {
        day: 1,
        title: "The Question Underneath Every Question",
        subtitle: "Why your financial anxiety may be a spiritual symptom",
        theme: "The Root Issue: Ownership vs. Fear",
        scripture: "Psalm 24:1 — "The earth is the Lord's, and everything in it, the world, and all who live in it."",
        summary: "Most of us begin our financial lives with the wrong question. We ask "How much do I have?" or "Will I have enough?" — but those questions rest on a flawed assumption: that we are the owners. Ron Blue's foundational insight is that until the question of ownership is settled, every financial decision will be driven by fear rather than faith. Today is about naming that fear honestly and introducing the question that resolves it.",
        spiritual_obj: "To surface the anxiety you carry about money and locate its source in the assumption of ownership — not in circumstances.",
        practical: "Write down your single greatest financial fear or worry. Don't try to fix it yet. Just name it. Then write above it: "This belongs to God." This is not denial — it is the beginning of honest stewardship."
      },
      {
        day: 2,
        title: "You Possess Much, But You Own Nothing",
        subtitle: "The liberating difference between a steward and an owner",
        theme: "Ownership Transfer — From Owner to Steward",
        scripture: "Deuteronomy 8:17–18 — "You may say to yourself, 'My power and the strength of my hands produced this wealth for me.' But remember the Lord your God, for it is he who gives you the ability to produce wealth."",
        summary: "Ron Blue uses a vivid image: when his daughter borrowed his car to drive, she had every benefit of using it — but he could reclaim it any moment. That is the life of a steward. We receive much, we use much, but we own nothing. This shift from owner to steward is not a demotion — it is the beginning of financial peace. An owner bears the weight of ultimate responsibility. A steward carries faithful responsibility. Only one of those is sustainable.",
        spiritual_obj: "To experience the emotional relief that comes from releasing the burden of ownership back to God.",
        practical: "Take a walk around your home or property. As you look at each possession, practice saying quietly: "This belongs to God. I am the manager, not the owner." Notice what loosens in you."
      },
      {
        day: 3,
        title: "Your Checkbook Knows the Truth",
        subtitle: "What your spending reveals about what you actually believe",
        theme: "Stewardship Cannot Be Faked",
        scripture: "Matthew 6:21 — "For where your treasure is, there your heart will be also."",
        summary: "Ron Blue offers one of his most honest observations: you can't fake stewardship. What you actually believe about God's ownership will show up in your spending — not in your stated convictions, but in your actual choices. This is not meant to produce shame. It is meant to create clarity. Your financial life is a theological document. It tells a story about who you trust, what you worship, and what you fear.",
        spiritual_obj: "To invite honest self-examination — not condemnation — about the gap between what you say you believe and how you actually handle money.",
        practical: "Review the last 30 days of spending in one category — food, entertainment, or shopping. Ask honestly: Does this spending reflect someone who believes God owns it all? What one adjustment would bring more alignment?"
      },
      {
        day: 4,
        title: "The Money That Sits on the Throne",
        subtitle: "How money becomes a false master — and how to dethrone it",
        theme: "The Spiritual Power of Money",
        scripture: "Matthew 6:24 — "No one can serve two masters. Either you will hate the one and love the other, or you will be devoted to the one and despise the other. You cannot serve both God and money."",
        summary: "Jesus does not say money is evil. He says it is a rival master — one that offers to answer the same questions that only God can truly answer: Am I safe? Am I secure? Do I have enough? When money sits on the throne of our decision-making, we become reactive, anxious, and ultimately enslaved. Transferring ownership to God is not a financial strategy — it is an act of dethronement. Ownership transfer removes money from the throne and puts God back where He belongs.",
        spiritual_obj: "To identify one specific area of your life where money — not God — has been functioning as your source of security or identity.",
        practical: "Name one financial decision you've been avoiding because it feels too risky or too generous. Ask: Am I avoiding this because I'm acting like an owner rather than a steward? Bring that decision to prayer today."
      },
      {
        day: 5,
        title: "Every Spending Decision Is a Spiritual Decision",
        subtitle: "There is nothing more spiritual about a tithe check than a grocery run",
        theme: "The Spirituality of Ordinary Money Choices",
        scripture: "Colossians 3:17 — "And whatever you do, whether in word or deed, do it all in the name of the Lord Jesus, giving thanks to God the Father through him."",
        summary: "One of Ron Blue's most clarifying statements is this: every spending decision is a spiritual decision. There is nothing inherently more holy about giving to your church than buying a car or taking a vacation. All of it — every dollar — belongs to God and is used in His presence. The sacred/secular divide in our finances is a myth. Buying groceries for your family is an act of stewardship. Paying off debt is an act of stewardship. The question is never "Is this spiritual?" The question is always "Is this faithful?"",
        spiritual_obj: "To dissolve the false boundary between 'spiritual giving' and 'ordinary spending' — and to see the whole of financial life as lived before God.",
        practical: "Before each spending decision today — no matter how small — pause and ask: "Is this faithful stewardship of what God has entrusted to me?" Practice this for one full day and notice what shifts."
      },
      {
        day: 6,
        title: "The Tool That Lost Its Power",
        subtitle: "When money becomes a servant instead of a master, everything changes",
        theme: "Money as a Tool for God's Purposes",
        scripture: "1 Timothy 6:17–18 — "Command those who are rich in this present world not to be arrogant nor to put their hope in wealth, which is so uncertain, but to put their hope in God, who richly provides us with everything for our enjoyment. Command them to do good, to be rich in good deeds, and to be generous and willing to share."",
        summary: "When God is the owner, money becomes a tool — and when money is only a tool, it loses its power over you. This is one of the most practically liberating truths in the entire Master Your Money framework. People who are enslaved to money often have either too much or too little of it. The issue is never the amount — it is the relationship. Stewardship repositions money from master to instrument: useful, important, morally significant, but no longer in charge.",
        spiritual_obj: "To begin experiencing money as a tool for God's purposes rather than a measure of your worth or security.",
        practical: "Identify one way you can use money this week as a deliberate tool for good — not because you are obligated, but because you are a steward with resources to deploy. It can be small. Make it intentional."
      },
      {
        day: 7,
        title: "Signing the Deed",
        subtitle: "The ownership transfer that changes the rest of your financial life",
        theme: "Formal Surrender and the Beginning of Peace",
        scripture: "Romans 12:1 — "Therefore, I urge you, brothers and sisters, in view of God's mercy, to offer your bodies as a living sacrifice, holy and pleasing to God — this is your true and proper worship."",
        summary: "Ron Blue asks readers to do something concrete: list everything they possess, then return ownership to God through a simple prayer of commitment — and sign it. This is not a magic ritual. It is a spiritual act of alignment that makes the abstract concrete. The same principle applies to your finances. Today is the day to stop knowing that God owns it all and start living as though it is true. The deed belongs to Him. Your signature is the act of surrender that everything else rests on.",
        spiritual_obj: "To move from intellectual agreement about God's ownership to a concrete, personal act of surrender — establishing the spiritual foundation for the entire 40-day journey.",
        practical: "Write a simple prayer of ownership transfer. Name your possessions, your income, your debts, and your future. Sign it and date it. Keep it somewhere visible. This is your starting place."
      }
    ]
  },

  {
    number: 2,
    title: "MOVEMENT TWO: WHERE ARE YOU, AND WILL YOU BE OKAY?",
    subtitle: "Days 8–14 | Honest Assessment and the Question Beneath All Questions",
    description: "Before you can plan, you have to know where you stand. These seven days guide you through an honest look at your current financial reality — not to produce shame, but to create clarity. They also address the deepest financial fear most people carry: Will I ever have enough?",
    days: [
      {
        day: 8,
        title: "Will I Ever Have Enough?",
        subtitle: "The question underneath the spreadsheet that only one answer can settle",
        theme: "The Core Fear: Scarcity and Security",
        scripture: "Philippians 4:19 — "And my God will meet all your needs according to the riches of his glory in Christ Jesus."",
        summary: "Ron Blue identifies three questions that haunt most people's financial lives: Will I ever have enough? Will it continue to be enough? How much is enough? These are not merely financial questions — they are theological ones. If all that I have is mine, then there is never enough to feel truly safe. But if it is God's — if He is the provider, the owner, the sustainer — then the question of enough has a different answer entirely. The goal today is not to calculate your way to security. It is to locate where your security actually comes from.",
        spiritual_obj: "To bring the deepest financial fear — Will I be okay? — into honest conversation with God, and to begin receiving His answer rather than a balance sheet's answer.",
        practical: "Write out your honest answer to: "What would it take for me to feel financially secure?" Then ask yourself: Is that number actually achievable — or does the target keep moving? Pray about what you find."
      },
      {
        day: 9,
        title: "Taking Stock Without Shame",
        subtitle: "How to look honestly at where you are — and why that honesty is a gift",
        theme: "Financial Self-Awareness: Net Worth and Cash Flow",
        scripture: "Proverbs 27:23 — "Be sure you know the condition of your flocks, give careful attention to your herds."",
        summary: "You cannot manage what you cannot see. A statement of net worth and a summary of cash flow are not exercises in self-judgment — they are acts of responsible stewardship. Ron Blue emphasizes that the first step of any sound financial plan is simply to summarize your present situation with honesty. Many people avoid this step because they are afraid of what they will find. But clarity — even uncomfortable clarity — is always more useful than avoidance. A steward who doesn't know the condition of what they manage cannot manage it well.",
        spiritual_obj: "To approach financial self-assessment with the calm courage of a steward who trusts the Owner, rather than the dread of someone alone with a problem.",
        practical: "Today, write a simple list of everything you own and everything you owe. Don't analyze it yet — just see it. This is your net worth snapshot. Bring it to God: \"Lord, this is what You've entrusted to me. Show me how to manage it well.\""
      },
      {
        day: 10,
        title: "What Is Actually Coming In, and Where Is It Going?",
        subtitle: "The cash flow conversation most people have been avoiding",
        theme: "Cash Flow Clarity: Income and Expenses",
        scripture: "Luke 14:28 — "Suppose one of you wants to build a tower. Won't you first sit down and estimate the cost to see if you have enough money to complete it?"",
        summary: "Jesus commends counting the cost before building. The same wisdom applies to your financial life. Knowing your cash flow — what comes in, what goes out, and what remains — is not optional financial planning. It is basic biblical stewardship. Many people discover that their cash flow problem is not an income problem but a spending pattern problem. The goal is not condemnation. The goal is visibility. You cannot make faithful decisions about money you cannot see.",
        spiritual_obj: "To overcome the emotional resistance to tracking money — and to experience the clarity that comes from honest visibility into your own financial patterns.",
        practical: "Track every dollar that comes in and goes out this week — even imperfectly. Use a notebook, an app, or a spreadsheet. At the end of the week, look at the whole picture and ask: Does this reflect the priorities of a faithful steward?"
      },
      {
        day: 11,
        title: "The Five Stages — and Honest About Which One You're In",
        subtitle: "Struggling, Surviving, Stable, Secure, or Surplus: where are you really?",
        theme: "Your Financial Stage and the Journey Forward",
        scripture: "Ecclesiastes 4:6 — "Better one handful with tranquility than two handfuls with toil and chasing after the wind."",
        summary: "Ron Blue describes five stages of financial life: Struggling, Surviving, Stable, Secure, and Surplus. The goal of the journey is not necessarily to reach Surplus — it is to move faithfully through whatever stage you are in. Most people want to jump from Struggling to Secure without passing through the hard work of Stable. But each stage has its own lessons, its own faithfulness, and its own invitation from God. Knowing where you are — honestly — is the first act of wisdom. Contentment is possible at every stage.",
        spiritual_obj: "To accept your current financial stage without shame or denial — and to find God's invitation within it rather than just through it.",
        practical: "Identify honestly which of the five stages describes your current financial reality. Write a paragraph about what it feels like to be there. Then ask: What does faithful stewardship look like from exactly where I am — not where I wish I was?"
      },
      {
        day: 12,
        title: "The Comparison Trap",
        subtitle: "Why neighbor-watching is one of the most expensive habits you have",
        theme: "Contentment vs. Discontentment",
        scripture: "Philippians 4:11–12 — "I have learned, in whatever state I am, to be content. I know how to be abased, and I know how to abound."",
        summary: "Discontentment is not just an emotional problem — it is an economic one. When we measure our financial life against the lifestyles of others, we always find ourselves lacking. Ron Blue identifies this as one of the most subtle and destructive traps in financial life. The antidote is not complacency — settling for less than God intends — but genuine contentment: grateful, celebrating, honoring God from within your actual circumstances rather than chasing the circumstances of someone else.",
        spiritual_obj: "To distinguish between holy ambition (improving faithfulness) and sinful discontentment (measuring worth by comparison) — and to choose contentment as an act of spiritual discipline.",
        practical: "Identify one area where you regularly compare your finances to others (neighborhood, cars, vacations, giving). Confess the anxiety that comparison produces. Write one thing you are genuinely grateful for in your current financial reality."
      },
      {
        day: 13,
        title: "How Much Is Enough?",
        subtitle: "The question that money can never answer but faith can",
        theme: "Defining 'Enough' — the Finish Line Question",
        scripture: "1 Timothy 6:6–8 — "Godliness with contentment is great gain. For we brought nothing into this world, and we can take nothing out of it. But if we have food and clothing, we will be content with that."",
        summary: "Ron Blue frames this as one of life's most critical financial questions — and notes that most people never answer it. Without a definition of "enough," the accumulation never stops, generosity is always deferred, and the soul remains in a permanent state of wanting more. The question "How much is enough?" is actually a question about what money is for, what life is for, and who God is. The answer is different for every person — but it must be answered. Until it is, the finish line keeps moving.",
        spiritual_obj: "To begin developing your own honest answer to "How much is enough?" — and to allow that answer to shape your financial decisions rather than market pressure or comparison.",
        practical: "Write your answer to this question: If I had [X] in savings and [Y] in income, I would feel that my financial life was genuinely secure. Then ask: Is that number what God has called me to — or what fear has told me I need?"
      },
      {
        day: 14,
        title: "When Fear Rules, Peace Is Impossible",
        subtitle: "How settled ownership quiets the anxiety that money can't fix",
        theme: "From Financial Fear to Financial Peace",
        scripture: "Isaiah 26:3 — "You will keep in perfect peace those whose minds are steadfast, because they trust in you."",
        summary: "Randy Brunson, a longtime financial advisor, observes a consistent pattern: when people believe they own everything on their balance sheet, fear rules. When they genuinely accept that God owns it all, peace returns. Financial peace is not the absence of financial problems. It is the presence of a settled answer to the question of ownership. The person who knows that God is the owner — and that God is good — does not need a perfect balance sheet to experience peace. That peace is available to you today, wherever you are financially.",
        spiritual_obj: "To move from financial anxiety driven by ownership thinking to financial peace rooted in trusting the Provider.",
        practical: "Identify the specific financial fear that most occupies your mind. Pray this simple prayer: "Lord, this belongs to You. You are the owner. I trust You with this. Show me what faithful stewardship looks like from this place.""
      }
    ]
  },

  {
    number: 3,
    title: "MOVEMENT THREE: THE WISDOM THAT NEVER CHANGES",
    subtitle: "Days 15–21 | Biblical Principles That Work in Every Season",
    description: "God's financial wisdom is transcendent, transferable, transformative, and timeless — Ron Blue's four T's. These seven days move into the core biblical principles that undergird all sound financial decision-making, regardless of income, stage of life, or economic climate.",
    days: [
      {
        day: 15,
        title: "Principles That Outlast Every Market",
        subtitle: "Why God's financial wisdom works when economic predictions don't",
        theme: "The Timeless Nature of Biblical Financial Wisdom",
        scripture: "James 1:5 — "If any of you lacks wisdom, you should ask God, who gives generously to all without finding fault, and it will be given to you."",
        summary: "Ron Blue insists that biblical financial wisdom is not situational advice for good economic times — it is transcendent truth that works in every season, every economy, every income level. Inflation or deflation. Boom or recession. Struggling or surplus. The core principles of God's design for money do not change with the Dow Jones. This is profoundly stabilizing. You do not need to predict the market. You need to practice the principles. Wisdom, not prediction, is what financial faithfulness requires.",
        spiritual_obj: "To anchor your financial decision-making in the stability of God's wisdom rather than the volatility of economic prediction.",
        practical: "Think of one recent financial decision you made based on fear of what might happen economically. Then ask: What would this decision look like if it was made from God's wisdom rather than market anxiety? Write down the difference."
      },
      {
        day: 16,
        title: "Spend Less Than You Earn — Always",
        subtitle: "The simplest financial principle is also the most violated",
        theme: "The Foundation Principle: Positive Cash Flow",
        scripture: "Proverbs 21:20 — "The wise store up choice food and olive oil, but fools gulp theirs down."",
        summary: "Of all of Ron Blue's principles, this one is the most fundamental: spend less than you earn. It sounds obvious. It is rarely practiced. In a world of easy credit, relentless advertising, and the cultural pressure to consume, spending more than you earn has become nearly normalized. But the math is ruthless. Every month of negative cash flow is a month of moving backward. Every month of positive cash flow is a month of building margin. Margin is not a luxury — it is the breathing room that makes every other good financial decision possible.",
        spiritual_obj: "To embrace spending less than you earn not as deprivation but as the deliberate choice of a person who has a plan and a purpose.",
        practical: "Calculate your actual cash flow from last month: total income minus total expenses. If it's positive, identify how to protect that margin. If it's negative, identify one specific expense to reduce — not someday, but this week."
      },
      {
        day: 17,
        title: "We Are in a Growth Process",
        subtitle: "Faithfulness is the goal — not a particular income or net worth",
        theme: "The Process Principle: Growth Over Perfection",
        scripture: "Luke 16:10 — "Whoever can be trusted with very little can also be trusted with much, and whoever is dishonest with very little will also be dishonest with much."",
        summary: "Ron Blue's second core biblical principle is that we are in a growth process. God is not measuring your faithfulness by your income, your net worth, or the size of your giving check. He is measuring it by the trajectory of your stewardship — whether you are growing in wisdom, generosity, and discipline over time. This is liberating for people who feel behind, ashamed of past mistakes, or overwhelmed by where they are. God does not require that you arrive. He requires that you grow.",
        spiritual_obj: "To release the shame of past financial mistakes and embrace the grace-filled reality that faithful growth — not perfect performance — is what God asks of a steward.",
        practical: "Identify one area of your financial life where you have grown in the last year — even if the growth was small. Celebrate that growth. Then identify one area where you want to grow in the next six months. Write a simple first step."
      },
      {
        day: 18,
        title: "The Amount Is Not the Point",
        subtitle: "Why a retired pastor who never earned more than $8,000 a year mastered money",
        theme: "The Faithfulness Principle: It Is Not About How Much",
        scripture: "Mark 12:43–44 — "'Truly I tell you, this poor widow has put more into the treasury than all the others. They all gave out of their wealth; but she, out of her poverty, put in everything — all she had to live on.'"",
        summary: "Ron Blue tells of an 80-year-old retired pastor who had never earned more than $8,000 in a single year, had no debt, and tithed faithfully his whole life. He was one of the most financially wise people Ron had ever met. The amount you earn or manage is not the measure of your stewardship. What matters is what you do with whatever God has entrusted to you. Faithfulness is the criterion. Not wealth. Not income. Not investment returns. Faithfulness.",
        spiritual_obj: "To unhook your sense of financial faithfulness from the size of your income or net worth — and to recommit to faithfulness at whatever level God has entrusted to you.",
        practical: "Read the parable of the talents (Matthew 25:14–30). Notice that the servant who was faithful with two talents received the same commendation as the one faithful with five. Write what "well done, good and faithful servant" would mean for your specific financial situation."
      },
      {
        day: 19,
        title: "Avoid Debt Like the Plague",
        subtitle: "Why borrowing always costs more than you think — spiritually and financially",
        theme: "The Debt Danger: Compounding Against You",
        scripture: "Proverbs 22:7 — "The rich rule over the poor, and the borrower is slave to the lender."",
        summary: "Debt is not a sin — but it is almost always a trap. Ron Blue outlines the economic dangers clearly: compounding works against the borrower just as powerfully as it works for the saver. He also identifies two spiritual dangers: debt presumes upon the future, and debt may deny God an opportunity to work. The ease of getting into debt is itself the first trap — because getting out is rarely easy. The standard he offers is clear: whenever you borrow money for any reason, there must be a guaranteed way to repay it. Not a hoped-for way. A guaranteed way.",
        spiritual_obj: "To take seriously the spiritual — not just financial — dangers of debt, and to develop a posture of avoidance rather than accommodation toward new borrowing.",
        practical: "List every debt you currently carry. For each one, assess: Did this debt meet Ron Blue's four criteria? (Does it make economic sense? Unity with spouse? Spiritual peace? Meets a goal no other way?) What does honest assessment reveal?"
      },
      {
        day: 20,
        title: "Faith Requires Action",
        subtitle: "The last biblical principle is also the one most people skip",
        theme: "The Action Principle: Wisdom Demands a Step",
        scripture: "James 2:17 — "Faith by itself, if it is not accompanied by action, is dead."",
        summary: "Ron Blue's final core principle is the one that transforms all the others from interesting ideas into actual change: faith requires action. You can believe that God owns it all. You can know that you should spend less than you earn. You can understand the dangers of debt. But until a decision is made — a budget is written, a debt payment begins, a giving plan is set — nothing changes. Financial faithfulness is not a passive position. It is a series of deliberate, consistent choices, made by faith, over time.",
        spiritual_obj: "To move from understanding biblical financial principles to making one specific, concrete decision based on them today.",
        practical: "Choose one principle from this week that you have known but not acted on. Write the specific, measurable action you will take this week. Set a date. Tell someone. Faith without action is incomplete stewardship."
      },
      {
        day: 21,
        title: "Wisdom Is Always Transcendent, Transferable, Transformative, and Timeless",
        subtitle: "Why these principles work for anyone, anywhere, at any income level",
        theme: "The Unchanging Nature of God's Financial Design",
        scripture: "Proverbs 3:13–14 — "Blessed are those who find wisdom, those who gain understanding, for she is more profitable than silver and yields better returns than gold."",
        summary: "Ron Blue offers four words to describe biblical wisdom in financial life: transcendent (above any economic system), transferable (works for anyone), transformative (it changes you), and timeless (never expires). These are not just encouraging adjectives — they are a profound claim. God's wisdom for money is not advice for people with a certain income or in a certain culture or during a certain economic era. It is truth that works. It has always worked. It always will. The question is whether you will apply it.",
        spiritual_obj: "To move from knowing about God's financial wisdom to trusting it enough to actually live by it — regardless of circumstances.",
        practical: "Review the six principles covered this week. Write a sentence describing which one you need most right now, and write one concrete application for your current financial season. Pray for the courage to act on it."
      }
    ]
  },

  {
    number: 4,
    title: "MOVEMENT FOUR: THE PLAN THAT SETS YOU FREE",
    subtitle: "Days 22–28 | Financial Planning as an Act of Faithful Obedience",
    description: "A financial plan is not a constraint — it is a road map for faithfulness. These seven days move from principles to practice: setting faith-based goals, building a budget, creating margin, avoiding the most common mistakes, and establishing the sequential strategy that builds lasting financial health.",
    days: [
      {
        day: 22,
        title: "Goals That Come from Prayer, Not Fear",
        subtitle: "How to set financial goals that God actually authored",
        theme: "Faith-Based Financial Goals",
        scripture: "Proverbs 16:3 — "Commit to the Lord whatever you do, and he will establish your plans."",
        summary: "Ron Blue argues that most people set financial goals based on fear (what they dread losing) or desire (what they want to accumulate) rather than faith (what God has called them to steward). Faith-based goals emerge from prayer, reflection, and a genuine question: What has God placed in my care, and what does He want me to do with it? Goals that come from that process have a different quality — they create direction, crystallize thinking, provide motivation, and keep us accountable to something larger than our own appetites.",
        spiritual_obj: "To begin the process of setting financial goals not as a personal ambition exercise but as a spiritual formation practice of listening to what God wants for your stewardship.",
        practical: "Spend 15 minutes in prayer today — not asking for money, but asking: Lord, what do You want for my financial life in the next year? In the next five years? Write down what comes. These are your starting points for faith-based goals."
      },
      {
        day: 23,
        title: "The Four Barriers That Steal Your Future",
        subtitle: "Why most people never set goals — and what to do about it",
        theme: "Overcoming the Obstacles to Goal-Setting",
        scripture: "Habakkuk 2:2 — "Then the Lord replied: 'Write down the revelation and make it plain on tablets so that a herald may run with it.'"",
        summary: "Ron Blue identifies four barriers that keep most people from setting financial goals: fear of failure, the false assumption that goals take too much time, uncertainty about what goals to set, and the absence of a goal-setting process. Behind all four is a common thread — the belief that the future is more uncertain than God is faithful. Written, measurable, prayerfully discerned goals are not a sign of arrogance about the future. They are an act of trust that God is worth planning for.",
        spiritual_obj: "To identify which of the four barriers most strongly prevents you from setting financial goals — and to address it honestly in prayer.",
        practical: "Choose one financial goal — giving, saving, debt reduction, or a major purchase — and write it in specific, measurable terms. Include a date. Post it somewhere visible. A goal that is not written is still a wish."
      },
      {
        day: 24,
        title: "Budget: The Word That Feels Like a Cage But Isn't",
        subtitle: "Why a spending plan is one of the most liberating things you can build",
        theme: "The Budget as a Tool of Faithfulness",
        scripture: "Luke 16:11 — "So if you have not been trustworthy in handling worldly wealth, who will trust you with true riches?"",
        summary: "A budget is simply a plan for your money that reflects your values and priorities. Without one, money flows toward whatever is most immediately urgent or emotionally compelling — rarely toward what you actually care about most. Ron Blue describes the budget process as estimating, recording, building, and controlling. Each step builds visibility and intention into your financial life. A budget doesn't restrict your freedom — it expresses your freedom. It is proof that you are choosing your financial priorities rather than letting them choose you.",
        spiritual_obj: "To reframe the budget from a restrictive constraint into a faithful expression of your values and priorities — a spiritual document as much as a financial one.",
        practical: "Build a simple monthly budget today. Categories: giving, taxes, debt, savings, living expenses. Assign a number to each. Total it against your income. If it doesn't balance, something has to change — and now you know what."
      },
      {
        day: 25,
        title: "The Most Common Mistakes — and Why Smart People Make Them",
        subtitle: "A consumptive lifestyle, no budget, and driving to the poor house",
        theme: "Avoiding the Three Financial Traps",
        scripture: "1 Timothy 6:9 — "Those who want to get rich fall into temptation and a trap and into many foolish and harmful desires that plunge people into ruin and destruction."",
        summary: "Ron Blue identifies three most common financial mistakes: living a consumptive lifestyle (spending everything that comes in), having no budget (flying financially blind), and making poor decisions about cars (one of the most consistent wealth destroyers). Behind all three is a common dynamic: the gap between what we can afford and what we want others to think we can afford. Appearing to be financially healthy is not the same as being financially healthy. Stewardship sometimes means driving an older car so you can give more, save more, or owe less.",
        spiritual_obj: "To honestly assess whether any of the three most common financial mistakes is currently operating in your life — and to feel the freedom of choosing differently.",
        practical: "Review your last major financial decision — a car, a house, a purchase. Ask: Was this decision driven by what I could genuinely afford, or by the desire to project a certain image? What would a steward have decided?"
      },
      {
        day: 26,
        title: "Margin Is Not a Luxury — It Is Obedience",
        subtitle: "Why breathing room in your finances is a spiritual priority",
        theme: "Creating Financial Margin",
        scripture: "Proverbs 21:20 — "The wise store up choice food and olive oil, but fools gulp theirs down."",
        summary: "Margin is the space between what you earn and what you spend. Without margin, every financial emergency becomes a crisis, every unexpected bill becomes a debt, and every opportunity for generosity becomes a conflict. Ron Blue describes margin as the breathing room that makes faithful decision-making possible. When everything is consumed, life becomes fragile. When margin exists, you can respond to God's nudges rather than just your circumstances. Margin is not laziness — it is preparation. It is the financial equivalent of leaving room for God to work.",
        spiritual_obj: "To recognize margin not as accumulation for its own sake but as the space that allows faithful, responsive, generous living.",
        practical: "Calculate your current margin (income minus expenses). If it's zero or negative, identify two specific expenses you could reduce this month to create even $50 of margin. If you have margin, identify whether it is being used purposefully or simply drifting toward consumption."
      },
      {
        day: 27,
        title: "The Sequential Strategy — One Step at a Time",
        subtitle: "Why the order of your financial priorities matters as much as the amount",
        theme: "The Sequential Investment Strategy",
        scripture: "1 Corinthians 14:40 — "But everything should be done in a fitting and orderly way."",
        summary: "Ron Blue's Sequential Investment Strategy provides a clear, step-by-step framework for using your margin: first, eliminate consumer debt (it earns you an immediate 12–28% return); second, establish three to six months of emergency savings; third, save for major purchases; fourth, diversify for long-term goals; fifth, use investment funds to complete remaining goals. The power of this strategy is in its sequence. It removes the pressure of constant competing priorities and replaces it with a clear, ordered path forward. One step at a time.",
        spiritual_obj: "To replace the overwhelm of competing financial priorities with the clarity and peace of a simple, ordered strategy.",
        practical: "Identify which step of the Sequential Investment Strategy describes your current situation. Write what completion of that step looks like for you. What is the first concrete action to move toward it this month?"
      },
      {
        day: 28,
        title: "Planning Is Not the Opposite of Faith",
        subtitle: "Why preparing for the future honors God rather than doubting Him",
        theme: "Planning as an Expression of Faith",
        scripture: "Proverbs 13:16 — "All who are prudent act with knowledge, but fools expose their folly."",
        summary: "Some believers resist financial planning because it feels like a lack of trust in God's provision. But planning is not the opposite of faith — it is an expression of it. When your heart is surrendered to God's ownership, planning becomes an act of wisdom and worship rather than control and anxiety. Ron Blue teaches that the goal of a financial plan is not to predict the future but to align your present decisions with your goals, your values, and God's purposes. The plan serves the mission. It does not replace dependence on God.",
        spiritual_obj: "To embrace financial planning as a spiritual discipline rather than a secular exercise — and to see your plan as an act of faithful preparation rather than anxious control.",
        practical: "Write a one-paragraph summary of your current financial situation (where you are) and a one-paragraph description of where you want to be in three years financially. What one decision made today would most move you from the first paragraph to the second?"
      }
    ]
  },

  {
    number: 5,
    title: "MOVEMENT FIVE: THE FREEDOM FOUND IN GIVING",
    subtitle: "Days 29–35 | Generosity as Spiritual Formation, Not Financial Obligation",
    description: "Giving is not a tax you pay to God after you have handled everything else. It is the practice that trains your soul toward freedom. These seven days explore the transformative, disruptive, and deeply liberating nature of biblical generosity — from wherever you are financially.",
    days: [
      {
        day: 29,
        title: "Generosity Is What Free People Do",
        subtitle: "You don't graduate into giving — you grow into it",
        theme: "Generosity as Spiritual Discipline, Not Financial Reward",
        scripture: "2 Corinthians 9:7 — "Each of you should give what you have decided in your heart to give, not reluctantly or under compulsion, for God loves a cheerful giver."",
        summary: "One of the most powerful statements in the Master Your Money teaching is this: generosity is not what rich people do — it is what free people do. And freedom is available at any income level. The myth that you should wait until you are financially stable before you begin giving is exactly that — a myth. Generosity is a discipline, not a reward. It begins wherever you are, because generosity grows as your trust in God grows. The soul that gives regularly — even modestly — is being formed into someone who trusts the Provider. And that trust deepens with each act of giving.",
        spiritual_obj: "To dismantle the belief that you must wait until financial stability arrives before practicing generosity — and to begin the discipline now, from wherever you are.",
        practical: "Make one intentional act of giving this week — not because you are obligated, but because you are free. Set an amount, choose a recipient, and give it. Decide in your heart before you give it. Notice what happens in you afterward."
      },
      {
        day: 30,
        title: "Where Your Treasure Goes, Your Heart Follows",
        subtitle: "You don't wait to feel generous — you choose generosity and your heart catches up",
        theme: "Giving as Heart Transformation",
        scripture: "Matthew 6:19–21 — "Do not store up for yourselves treasures on earth... But store up for yourselves treasures in heaven... For where your treasure is, there your heart will be also."",
        summary: "Jesus makes a counterintuitive claim about the relationship between money and the heart: the heart follows the treasure. Most of us assume we wait until we feel generous before we give. But Scripture suggests the opposite: you choose to give, and your heart gradually catches up. Giving redirects the heart from accumulation to impact, from fear to faith, from control to surrender. This is why giving changes everything — not just your bank account, but your anxiety level, your gratitude, your ability to trust God day to day.",
        spiritual_obj: "To experience the truth that obedient giving precedes the feeling of generosity — and to trust the process of heart transformation that follows the act.",
        practical: "Identify one area of financial life where fear is operating — a reluctance to give, to invest, to trust. Choose one act of financial obedience in that area this week. Take the step before you feel ready. Journal what happens."
      },
      {
        day: 31,
        title: "Giving Breaks the Power of Money",
        subtitle: "Why the most financially anxious people are often the least generous",
        theme: "Generosity as Deliverance from Money's Power",
        scripture: "Luke 12:15 — "Watch out! Be on your guard against all kinds of greed; life does not consist in an abundance of possessions."",
        summary: "Michael Blue, Ron's son, writes: "Giving breaks the power of money." This is not a metaphor — it is a described spiritual reality. People who hold tightly to money, waiting until they feel financially secure before they give, rarely feel financially secure. The grip tightens rather than loosens. But people who give regularly — even sacrificially — report something unexpected: the power of money over their emotions diminishes. Generosity is not just a financial virtue. It is a form of deliverance from money's capacity to master you.",
        spiritual_obj: "To identify where money holds power over your emotions or decisions — and to practice the discipline of giving as a specific act of breaking that power.",
        practical: "Think of something you own that holds disproportionate power over you — a savings account you are afraid to touch, a possession you are afraid to lose, an income you are afraid to give from. Name it. Then ask: What would it mean to hold this with open hands?"
      },
      {
        day: 32,
        title: "Decide Before You Give",
        subtitle: "Why generosity planned in advance is generosity that actually happens",
        theme: "Intentional, Planned Giving",
        scripture: "2 Corinthians 9:5 — "So I thought it necessary to urge the brothers to visit you in advance and finish the arrangements for the generous gift you had promised."",
        summary: "The teaching is clear: decide in your heart before you give. Generosity that is purely reactive — responding to emotional appeals or spontaneous moments — is inconsistent and often misaligned with your actual financial priorities. Ron Blue teaches that planned, intentional giving — decided in advance, from conviction rather than compulsion — is the most sustainable and the most transformative form of generosity. When you decide ahead of time how and where you will give, giving becomes part of your financial plan rather than a disruption to it. And a cheerful giver is someone who gives without reluctance — because they already decided.",
        spiritual_obj: "To build generosity into your financial plan with the same intentionality you bring to paying bills or saving for retirement.",
        practical: "Write a giving plan for the next three months: Where will you give? How much? When? Keep it simple. Then set it up as an automatic transaction or a calendar reminder. Planned generosity is kept generosity."
      },
      {
        day: 33,
        title: "Generosity Is for Every Stage — Not Just Surplus",
        subtitle: "The widow's offering was not a special exception — it was the standard",
        theme: "Giving at Every Income Level",
        scripture: "Luke 21:2–4 — "He also saw a poor widow put in two very small copper coins. 'Truly I tell you,' he said, 'this poor widow has put in more than all the others.'"",
        summary: "One of the most common myths about giving is that it is for people who have surplus — that generosity becomes possible only after debt is gone, savings are built, and income has stabilized. But Scripture consistently celebrates giving from scarcity as well as abundance. Ron Blue is clear: generosity is not something you graduate into — it is something you grow into. Faithful giving at every stage builds the muscle of trust that makes generosity sustainable at every stage. The posture matters more than the amount.",
        spiritual_obj: "To release the belief that your current financial stage disqualifies you from practicing real generosity — and to find one act of meaningful giving possible right now.",
        practical: "Consider the widow's two coins. What is the equivalent in your life — an amount that would genuinely cost you something, that would require trust? Pray about whether God is calling you to give that amount to something specific this week."
      },
      {
        day: 34,
        title: "Giving Aligns Today with Eternity",
        subtitle: "The only financial action with eternal consequences",
        theme: "Eternal Significance of Earthly Generosity",
        scripture: "Matthew 6:20 — "But store up for yourselves treasures in heaven, where moths and vermin do not destroy, and where thieves do not break in and steal."",
        summary: "Giving is the only financial action that has eternal consequences. Every dollar given to God's purposes goes ahead of you — it arrives in eternity before you do. Ron Blue notes that a wise person said he wanted to be the richest man in heaven, meaning he wanted to send as much as possible ahead. This is not about earning favor with God — it is about expressing worship. Giving is how finite resources take on infinite significance. It is the act that most clearly declares: I believe in a kingdom that outlasts everything I can accumulate.",
        spiritual_obj: "To cultivate an eternal perspective on money — seeing current generosity as an investment in what lasts, not just a loss of what is temporary.",
        practical: "Consider your current giving in light of eternity. What percentage of your financial resources is being directed toward things that will outlast your lifetime? Write down one specific change you would make to your giving if you took eternity seriously."
      },
      {
        day: 35,
        title: "Open Hands, Quiet Strength",
        subtitle: "What contentment feels like when generosity is finally part of who you are",
        theme: "The Joy and Freedom of a Generous Life",
        scripture: "Acts 20:35 — "It is more blessed to give than to receive."",
        summary: "At the end of the generosity movement comes the fruit: joy, gratitude, freedom from fear. Ron Blue repeatedly observes that the most content people he has met are always givers. Not because giving makes you rich, but because giving trains the soul to trust the Provider rather than the portfolio. The quiet strength of open hands — being willing to release, to share, to give — is the posture of a person who has genuinely settled the ownership question. Contentment does not come from accumulation. It comes from alignment: your heart and your hands pointed in the same direction.",
        spiritual_obj: "To experience — or to anticipate — the specific kind of freedom and contentment that accompanies a genuinely generous life.",
        practical: "Reflect on a time when you gave something that cost you something real. What did you feel afterward? If you have not yet experienced that kind of giving, write a prayer asking God to prepare your heart for it. Then take one step toward it this week."
      }
    ]
  },

  {
    number: 6,
    title: "MOVEMENT SIX: FAITHFUL TO THE END — AND BEYOND",
    subtitle: "Days 36–40 | Stewardship After Death, Legacy, and the Long View",
    description: "Faithful stewardship does not end at retirement or even at death. These final five days move into the deepest and most often-avoided territory of financial faithfulness: estate planning, legacy, the passing of wisdom to the next generation — and the ultimate question of what your money says about what you believed.",
    days: [
      {
        day: 36,
        title: "You Never See a Hearse Pulling a U-Haul",
        subtitle: "What you cannot take with you — and what you can send ahead",
        theme: "The Reality of Death and the Stewardship It Demands",
        scripture: "1 Timothy 6:7 — "For we brought nothing into this world, and it is certain that we can carry nothing out."",
        summary: "Ron Blue opens the chapter on estate planning with a direct statement: everyone will die, we will take nothing with us, and we will probably die at a time other than when we plan. These are not morbid observations — they are the foundation of wise estate planning. The person who refuses to plan for their own death is not trusting God more. They are failing the people they will leave behind. Estate planning is an act of love, clarity, and ongoing stewardship. Not planning is, as Ron puts it bluntly, one of the more selfish omissions a person can make.",
        spiritual_obj: "To overcome the avoidance of estate planning by seeing it as an act of love and faithfulness rather than a morbid exercise.",
        practical: "Answer honestly: Do you have a will? Does your spouse know the full picture of your financial life? Have you named guardians for your children? If the answer to any of these is no — that is your first action. Make the call, set the appointment, write the document."
      },
      {
        day: 37,
        title: "Both Spouses Need to Hold the Whole Picture",
        subtitle: "What happens when one person carries all the financial knowledge",
        theme: "Shared Stewardship and Marital Financial Transparency",
        scripture: "Ecclesiastes 4:9 — "Two are better than one, because they have a good return for their labor."",
        summary: "Financial advisor Kale Dowell consistently encounters the same dangerous pattern: one spouse knows the entire financial picture, and the other does not. Then the phone rings on the worst day of the surviving spouse's life — and they are left to manage what they never understood. This is not malice. It is absence of preparation. Stewardship shared is stewardship that survives. Both spouses need to know: the accounts, the advisors, the insurance, the debts, the giving intentions, and the plan for what happens next.",
        spiritual_obj: "To take responsibility for sharing financial knowledge within your household as an act of love, preparation, and stewardship.",
        practical: "Schedule a financial summit with your spouse (or trusted person if unmarried): review accounts, named beneficiaries, life insurance, giving plans, and the contact list for your advisors. If this conversation has never happened, today it begins."
      },
      {
        day: 38,
        title: "The Inheritance That Money Cannot Carry",
        subtitle: "What you pass on that outlasts any dollar figure in a will",
        theme: "Relational, Spiritual, and Character Inheritance",
        scripture: "Proverbs 13:22 — "A good person leaves an inheritance for their children's children."",
        summary: "Kale Dowell asks his clients to picture a fuller inheritance than financial capital alone: relational capital, intellectual capital, character capital, and spiritual capital. If you had to bankrupt one, which would it be? Almost without exception — believers and non-believers alike — choose financial. That realization resets the room. Parents stop trying to solve tomorrow's problems with dollars and start thinking like disciplers: What relationships should we build now? What wisdom should we write down? What convictions do we want to pass on while we can still look our children in the eye?",
        spiritual_obj: "To expand your definition of the inheritance you are building — beyond net worth to the wisdom, values, and faith you are actively transferring to the next generation.",
        practical: "Write a short legacy letter to the next generation in your life — children, grandchildren, spiritual heirs. Not about money. About what you believe, what you have learned, and what you hope they will carry forward. This is your most important estate document."
      },
      {
        day: 39,
        title: "Giving While You Can Still See It",
        subtitle: "Why Ron Blue believes most charitable giving should happen before death",
        theme: "Generosity as a Living Act, Not a Final Gesture",
        scripture: "Proverbs 3:27 — "Do not withhold good from those to whom it is due, when it is in your power to act."",
        summary: "Ron Blue is direct: the majority of charitable giving should be done while income is being earned — not deferred until death. After death, you have no more control over the property anyway, and it is not actually giving in the full sense of the word. Giving while alive means you can see the impact, feel the joy, and be shaped by the experience of open-handed generosity. The legacy of giving is most powerful when it is lived, not just documented. Give now. Give visibly. Give in ways that disciple the next generation into generosity.",
        spiritual_obj: "To evaluate whether your current giving practices reflect the urgency and joy of someone who wants to give now — not merely to arrange transfers after death.",
        practical: "Review your current estate plans or charitable intentions. What percentage of your planned giving is designated to happen after death? What could you give now — in a way that you could witness, be shaped by, and use to model generosity for others?"
      },
      {
        day: 40,
        title: "Well Done, Good and Faithful Servant",
        subtitle: "The commendation is available to every steward who chooses faithfulness over fear",
        theme: "The Finish Line: Faithfulness, Not Wealth",
        scripture: "Matthew 25:21 — "His master replied, 'Well done, good and faithful servant! You have been faithful with a few things; I will put you in charge of many things. Come and share your master's happiness!'"",
        summary: "Ron Blue writes that his deepest desire for every reader — and his own desire for his own life — is that when they stand before God, they will have confidence and expect to hear: "Well done, good and faithful servant." This is the finish line. Not a net worth number. Not a giving percentage. Not a perfect financial record. Faithfulness. Stewardship that reflected trust in the Owner, care for what was entrusted, and a willingness to hold it all with open hands. This is the hope that makes the entire 40-day journey worth it — and the invitation that was always there, waiting for you to say yes.",
        spiritual_obj: "To receive and rest in the grace-filled reality that God's commendation awaits every faithful steward — and to close this journey with surrender, gratitude, and renewed commitment.",
        practical: "Write your answer to this: What would it mean for the next year of your financial life to be described as "faithful"? Not perfect. Faithful. Then write one decision — about giving, spending, saving, planning, or debt — that would bring you closest to that description. Make it today."
      }
    ]
  }
];

// ─────────────────────────────────────────────
// DOCUMENT BUILDER
// ─────────────────────────────────────────────

function makeRun(text, opts = {}) {
  return new TextRun({ text, font: "Georgia", size: opts.size || 24, bold: opts.bold, italics: opts.italic, color: opts.color || "000000" });
}

function makePara(children, opts = {}) {
  return new Paragraph({
    children,
    alignment: opts.align || AlignmentType.LEFT,
    spacing: { before: opts.before || 80, after: opts.after || 80, line: opts.line || 280 },
    indent: opts.indent ? { left: opts.indent } : undefined,
    border: opts.border || undefined
  });
}

function makeHeading(text, level, color = "1A3A5C") {
  const sizes = { 1: 44, 2: 32, 3: 28, 4: 26 };
  return new Paragraph({
    children: [new TextRun({ text, font: "Georgia", size: sizes[level] || 28, bold: true, color })],
    spacing: { before: 300, after: 160 }
  });
}

function dividerLine() {
  return new Paragraph({
    children: [new TextRun({ text: "────────────────────────────────────────────────────", font: "Arial", size: 18, color: "B8860B" })],
    spacing: { before: 120, after: 120 }
  });
}

function spacer(before = 120, after = 120) {
  return new Paragraph({ children: [new TextRun("")], spacing: { before, after } });
}

function labeledField(label, value) {
  return new Paragraph({
    children: [
      new TextRun({ text: label + "  ", font: "Georgia", size: 22, bold: true, color: "1A3A5C" }),
      new TextRun({ text: value, font: "Georgia", size: 22, color: "222222" })
    ],
    spacing: { before: 100, after: 100 },
    indent: { left: 360 }
  });
}

const children = [];

// ── COVER PAGE ──
children.push(spacer(1200, 80));
children.push(new Paragraph({
  children: [new TextRun({ text: "MASTER YOUR MONEY", font: "Georgia", size: 60, bold: true, color: "1A3A5C" })],
  alignment: AlignmentType.CENTER,
  spacing: { before: 0, after: 160 }
}));
children.push(new Paragraph({
  children: [new TextRun({ text: "A 40-Day Devotional Journey", font: "Georgia", size: 36, italics: true, color: "B8860B" })],
  alignment: AlignmentType.CENTER,
  spacing: { before: 0, after: 320 }
}));
children.push(dividerLine());
children.push(spacer(120, 120));
children.push(new Paragraph({
  children: [new TextRun({ text: "Based on the teaching of Ron Blue and the Ron Blue Institute", font: "Georgia", size: 24, italics: true, color: "444444" })],
  alignment: AlignmentType.CENTER,
  spacing: { before: 0, after: 80 }
}));
children.push(new Paragraph({
  children: [new TextRun({ text: "From the Master Your Money curriculum and published manuscript", font: "Georgia", size: 22, italics: true, color: "666666" })],
  alignment: AlignmentType.CENTER,
  spacing: { before: 0, after: 600 }
}));
children.push(spacer(400, 80));
children.push(new Paragraph({
  children: [new TextRun({ text: "Ownership  ·  Stewardship  ·  Faithfulness  ·  Generosity  ·  Legacy", font: "Georgia", size: 22, color: "B8860B" })],
  alignment: AlignmentType.CENTER,
  spacing: { before: 0, after: 80 }
}));
children.push(new Paragraph({ children: [new PageBreak()] }));

// ── INTRODUCTION ──
children.push(spacer(200));
children.push(makeHeading("A NOTE ON THIS JOURNEY", 2));
children.push(dividerLine());
children.push(spacer(80));

const introText = [
  "This 40-day devotional framework emerges directly from the teaching of Ron Blue, the published Master Your Money manuscript, and the curriculum and transcripts of the Ron Blue Institute. It is not a supplement to that material — it is an immersion in it.",
  "",
  "Every theme, every principle, every application direction in these 40 days is drawn from the actual content Ron Blue has taught for over four decades: that God owns it all, that we are stewards not owners, that faithfulness is the measure of financial obedience, and that generosity is the discipline that frees the soul from money's power.",
  "",
  "These devotionals are organized into six movements — not as separate topics, but as a deepening progression. Each movement builds on the last. By Day 40, you will have moved through the full arc of financial discipleship: from the foundational question of ownership, through honest self-assessment, into the unchanging wisdom of Scripture, across the practical tools of planning, through the transforming practice of generosity, and finally into the long view of legacy and eternal faithfulness.",
  "",
  "This journey is not designed for people who have it together financially. It is designed for people who are willing to be honest — about their fear, their patterns, their spending, and their trust. If you bring that honesty to these 40 days, you will find that the teaching does exactly what Ron Blue has always promised: it works.",
  "",
  "Because it is grounded not in financial strategy, but in the unchanging wisdom of a God who owns everything — and who is more interested in your faithfulness than your net worth.",
];

introText.forEach(line => {
  if (line === "") { children.push(spacer(80, 80)); return; }
  children.push(makePara([makeRun(line, { size: 24 })], { before: 80, after: 80, line: 320 }));
});

children.push(new Paragraph({ children: [new PageBreak()] }));

// ── STRUCTURE OVERVIEW ──
children.push(makeHeading("THE SIX MOVEMENTS AT A GLANCE", 2));
children.push(dividerLine());
children.push(spacer(80));

movements.forEach(mv => {
  children.push(makePara([
    makeRun(mv.title, { bold: true, color: "1A3A5C", size: 24 }),
  ], { before: 160, after: 40 }));
  children.push(makePara([makeRun(mv.subtitle, { italic: true, color: "B8860B", size: 22 })], { before: 0, after: 80, indent: 360 }));
  children.push(makePara([makeRun(mv.description, { size: 22, color: "333333" })], { before: 0, after: 120, indent: 360, line: 300 }));
});

children.push(new Paragraph({ children: [new PageBreak()] }));

// ── BUILD EACH MOVEMENT AND DAY ──
movements.forEach(movement => {
  // Movement header
  children.push(spacer(240, 80));
  children.push(new Paragraph({
    children: [new TextRun({ text: movement.title, font: "Georgia", size: 36, bold: true, color: "1A3A5C" })],
    alignment: AlignmentType.CENTER,
    spacing: { before: 0, after: 120 }
  }));
  children.push(new Paragraph({
    children: [new TextRun({ text: movement.subtitle, font: "Georgia", size: 26, italics: true, color: "B8860B" })],
    alignment: AlignmentType.CENTER,
    spacing: { before: 0, after: 200 }
  }));
  children.push(dividerLine());
  children.push(spacer(120, 40));
  children.push(makePara([makeRun(movement.description, { size: 22, color: "333333" })], { before: 80, after: 160, line: 300 }));
  children.push(new Paragraph({ children: [new PageBreak()] }));

  // Each day
  movement.days.forEach(day => {
    // Day number bar
    children.push(new Paragraph({
      children: [new TextRun({ text: `DAY ${day.day}`, font: "Georgia", size: 28, bold: true, color: "FFFFFF" })],
      alignment: AlignmentType.CENTER,
      spacing: { before: 0, after: 0 },
      shading: { fill: "1A3A5C", type: ShadingType.CLEAR }
    }));
    children.push(spacer(80, 40));

    // Title and subtitle
    children.push(new Paragraph({
      children: [new TextRun({ text: day.title, font: "Georgia", size: 34, bold: true, color: "1A3A5C" })],
      spacing: { before: 80, after: 80 }
    }));
    children.push(new Paragraph({
      children: [new TextRun({ text: day.subtitle, font: "Georgia", size: 24, italics: true, color: "B8860B" })],
      spacing: { before: 0, after: 160 }
    }));
    children.push(dividerLine());
    children.push(spacer(80, 40));

    // Fields
    labelFields(children, day);

    children.push(new Paragraph({ children: [new PageBreak()] }));
  });
});

function labelFields(ch, day) {
  // Core Theme
  ch.push(makePara([makeRun("CORE THEME", { bold: true, size: 20, color: "1A3A5C" })], { before: 120, after: 40 }));
  ch.push(makePara([makeRun(day.theme, { size: 23, color: "222222" })], { before: 0, after: 160, indent: 360, line: 300 }));

  // Scripture
  ch.push(makePara([makeRun("PRIMARY SCRIPTURE", { bold: true, size: 20, color: "1A3A5C" })], { before: 80, after: 40 }));
  ch.push(new Paragraph({
    children: [new TextRun({ text: day.scripture, font: "Georgia", size: 23, italics: true, color: "333333" })],
    spacing: { before: 0, after: 160, line: 300 },
    indent: { left: 360 },
    border: { left: { style: BorderStyle.SINGLE, size: 4, color: "B8860B", space: 12 } }
  }));

  // Summary
  ch.push(makePara([makeRun("FOCUS", { bold: true, size: 20, color: "1A3A5C" })], { before: 80, after: 40 }));
  ch.push(makePara([makeRun(day.summary, { size: 23, color: "222222" })], { before: 0, after: 160, line: 320 }));

  // Spiritual objective
  ch.push(makePara([makeRun("SPIRITUAL OBJECTIVE", { bold: true, size: 20, color: "1A3A5C" })], { before: 80, after: 40 }));
  ch.push(makePara([makeRun(day.spiritual_obj, { size: 23, color: "222222" })], { before: 0, after: 160, line: 300 }));

  // Practical application
  ch.push(makePara([makeRun("PRACTICAL APPLICATION", { bold: true, size: 20, color: "1A3A5C" })], { before: 80, after: 40 }));
  ch.push(new Paragraph({
    children: [new TextRun({ text: day.practical, font: "Georgia", size: 23, color: "222222" })],
    spacing: { before: 0, after: 160, line: 300 },
    shading: { fill: "F5F0E8", type: ShadingType.CLEAR }
  }));
}

// ── CLOSING PAGE ──
children.push(spacer(400));
children.push(new Paragraph({
  children: [new TextRun({ text: "THE INVITATION THAT REMAINS", font: "Georgia", size: 36, bold: true, color: "1A3A5C" })],
  alignment: AlignmentType.CENTER,
  spacing: { before: 0, after: 200 }
}));
children.push(dividerLine());
children.push(spacer(120));
const closingText = "This 40-day journey has moved through six movements — ownership, honest assessment, unchanging wisdom, faithful planning, transforming generosity, and legacy. But these are not steps you complete and leave behind. They are postures you return to, deepen, and practice for the rest of your life. The question from Day 1 remains the question of every day: Who really owns this? When that question is settled — truly settled, not just agreed to in principle — everything else becomes possible. The budget becomes doable. The giving becomes joyful. The planning becomes worship. The legacy becomes intentional. Ron Blue has spent four decades pointing people to the same foundation: God owns it all. When you live like that is true, you are finally free to manage money the way it was designed to be managed — not as an owner anxious about what is his, but as a steward grateful for what has been entrusted. The commendation "Well done, good and faithful servant" is not reserved for the wealthy, the generous, or the financially sophisticated. It is reserved for the faithful. And faithfulness — wherever you begin, at whatever income, with whatever history — is always available to you. Go and be faithful.";

children.push(makePara([makeRun(closingText, { size: 24, color: "222222" })], { before: 0, after: 200, line: 340 }));

// ── BUILD DOC ──
const doc = new Document({
  styles: {
    default: { document: { run: { font: "Georgia", size: 24 } } }
  },
  sections: [{
    properties: {
      page: {
        size: { width: 12240, height: 15840 },
        margin: { top: 1440, right: 1440, bottom: 1440, left: 1440 }
      }
    },
    children
  }]
});

Packer.toBuffer(doc).then(buffer => {
  fs.writeFileSync("/mnt/user-data/outputs/MYM_40Day_Devotional_Framework.docx", buffer);
  console.log("Done! File written.");
}).catch(err => {
  console.error("Error:", err);
});
