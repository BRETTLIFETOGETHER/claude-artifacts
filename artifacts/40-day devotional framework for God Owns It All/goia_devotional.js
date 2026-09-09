const {
  Document, Packer, Paragraph, TextRun, HeadingLevel,
  AlignmentType, PageOrientation, BorderStyle, ShadingType,
  PageBreak, WidthType, LevelFormat
} = require('docx');
const fs = require('fs');

// Color palette
const NAVY = "1B3A5C";
const GOLD = "C8943A";
const LIGHT_BLUE = "D6E8F5";
const LIGHT_GOLD = "FDF3E3";
const GRAY = "595959";
const SECTION_COLORS = {
  "MOVEMENT ONE": "1B3A5C",
  "MOVEMENT TWO": "2E6E8A",
  "MOVEMENT THREE": "3A7A3A",
  "MOVEMENT FOUR": "7A3A6B",
  "MOVEMENT FIVE": "8B4513",
  "MOVEMENT SIX": "1B3A5C",
};

const movements = [
  {
    number: "MOVEMENT ONE",
    title: "The Question That Changes Everything",
    subtitle: "Days 1–7 | Perspective & Ownership",
    description: "The entire journey begins with a single question: Who owns it? Ron Blue taught that the answer to this question has the potential to transform every financial decision we make. Before we can learn to live, give, manage debt, or grow — we must settle the foundational reality that God owns it all. These seven days lay the cornerstone of the entire 40-day journey.",
    color: "1B3A5C",
    days: [
      {
        day: 1,
        title: "The Car Keys and the Kingdom",
        subtitle: "What Changes When the Owner Walks In",
        theme: "God's Total Ownership",
        scripture: "Psalm 24:1 — \"The earth and everything in it, the world and its inhabitants, belong to the LORD.\"",
        summary: "Ron Blue opens with the story of giving his children access to the family car — full access, but always understanding it was Dad's car for Dad's convenience. This disarmingly simple illustration unlocks the most foundational truth in biblical stewardship: God has given us full access to everything He owns, but it remains His — for His purposes, at His pleasure. The question isn't whether we have resources. The question is whose resources they really are.",
        spiritual_objective: "Awaken the reader to the reality that ownership — not just behavior — must shift. This is not a call to feel guilty about possessions but to experience freedom through releasing the illusion of ownership.",
        application: "Write down three things you think of as \"yours\" — a house, a career, a savings account, a relationship. Beside each one, write: \"Held in trust for the Owner.\" Begin each morning this week by saying aloud: \"Lord, today I manage what is already Yours.\""
      },
      {
        day: 2,
        title: "The Iceberg and the Invisible Life",
        subtitle: "Why What You Believe About Money Shows Up in Everything",
        theme: "Behavior Follows Belief",
        scripture: "Proverbs 23:7 — \"As a man thinks within himself, so he is.\"",
        summary: "Ron Blue taught using the iceberg as a picture of financial life: the visible part is behavior — how we spend, save, and give. But beneath the waterline lies the belief system that drives everything. Culture tells us money equals success, significance, and security. God's Word tells an entirely different story. Until the belief beneath the surface changes, behavior above it never will — not lastingly.",
        spiritual_objective: "Help the reader identify the invisible belief system driving their financial decisions, so they can begin aligning it with biblical truth rather than cultural pressure.",
        application: "Ask yourself: When I think about money, do I feel anxious or at peace? Do I feel successful when I have more and inadequate when I have less? Trace that feeling back to a belief. Write it down. Then write beside it what God's Word says is true instead."
      },
      {
        day: 3,
        title: "Three Questions You've Been Asking Wrong",
        subtitle: "Trading \"Will I Ever Have Enough?\" for a Better Question",
        theme: "Biblical Financial Worldview",
        scripture: "Matthew 6:19–21 — \"For where your treasure is, there your heart will be also.\"",
        summary: "Most people come to financial planning asking three questions: Will I ever have enough? Will it stay enough? How much is enough? Ron Blue identified these as the wrong questions — or rather, questions born from a worldview that positions us as the owner. The biblical worldview asks instead: Who owns it? How much is enough to be faithful with? And is the next steward prepared? Changing the question changes the entire answer.",
        spiritual_objective: "Shift the reader from a scarcity-anxiety posture toward a stewardship-faithfulness posture — from grasping to receiving and managing with open hands.",
        application: "Spend ten minutes journaling around this question: \"If I truly believed God owned everything I have, what would I stop worrying about today?\" Let the answer reveal where your heart's real treasure lies."
      },
      {
        day: 4,
        title: "Money as Tool, Test, and Testimony",
        subtitle: "The Three Ways God Uses Your Finances to Shape You",
        theme: "God's Purposes for Money",
        scripture: "Luke 16:10 — \"Whoever can be trusted with very little can also be trusted with much.\"",
        summary: "Ron Blue taught that God uses money in our lives in three specific ways: as a tool to accomplish His purposes, as a test of our trust and priorities, and as a testimony to those around us of His goodness and our devotion. Your bank statement, your credit card history, your giving record — none of these are merely financial documents. They are spiritual ones. They reveal what you truly believe about God.",
        spiritual_objective: "Invite the reader to see their financial life as one of the most transparent windows into their spiritual life — and to respond with sober, hopeful self-examination rather than shame.",
        application: "Look at your last 30 days of spending. Ask three questions about what you see: What does this show I've been using money as a tool to accomplish? What does this reveal about what I really trust? What does this testify to the people who know me?"
      },
      {
        day: 5,
        title: "Owners Grip. Stewards Receive.",
        subtitle: "What Open Hands Actually Feel Like",
        theme: "The Shift from Owner to Steward",
        scripture: "1 Chronicles 29:14 — \"For everything comes from You, and we have given You only what comes from Your own hand.\"",
        summary: "There is a posture difference between an owner and a steward. Owners grip tightly — they plan, protect, and defend their assets. Stewards hold with open hands — they receive instruction because their hands are open. The transcript from RBI teaching says it plainly: rest begins when we stop pretending to be the owner. Every morning's first prayer — \"Lord, all I have is Yours, show me how to manage it today\" — is an act of spiritual formation, not just a financial discipline.",
        spiritual_objective: "Lead the reader into a genuine, practical experience of releasing control — not as loss, but as relief. To hold loosely is not to value less; it is to trust more.",
        application: "Identify one area of your finances you've been holding too tightly — a savings account, a career decision, a financial goal. Write it down and pray: \"Lord, this belongs to You. I release my grip. Show me how to steward what is already Yours.\" Return to this prayer daily this week."
      },
      {
        day: 6,
        title: "The Steward's Job Description",
        subtitle: "Using God's Resources to Accomplish God's Plans",
        theme: "Definition and Practice of Stewardship",
        scripture: "1 Corinthians 4:2 — \"It is required that those who have been given a trust must prove faithful.\"",
        summary: "Stewardship has a simple definition in RBI teaching: using God's resources to accomplish God's plans. Not our resources for our comfort. Not our plans seasoned with a little generosity. The steward's job is to find out what the owner wants done and do it — with the time, money, talent, relationships, and truth entrusted to them. God measures faithfulness, not net worth. He looks for managers He can trust, not portfolios He can admire.",
        spiritual_objective: "Ground the reader in a concrete, freeing definition of stewardship that removes the pressure of ownership and replaces it with the dignity of faithful management.",
        application: "Write out a brief \"stewardship mission statement\" for your own life: one or two sentences describing how you want to use what God has entrusted to you this season. Post it somewhere you'll see it daily — not as a performance goal but as a compass for decision-making."
      },
      {
        day: 7,
        title: "The Faked Life",
        subtitle: "Why Stewardship Is the One Thing You Cannot Pretend",
        theme: "Conviction and Integrity in Financial Life",
        scripture: "James 3:17 — \"The wisdom from above is first pure, then peace-loving, gentle, compliant, full of mercy and good fruits, without favoritism and hypocrisy.\"",
        summary: "Ron Blue made one of his most striking observations in the manuscript: stewardship is the only area of the Christian life that can't be faked. You can perform generosity publicly while being tightfisted privately. But over time, where your money actually goes reveals where your heart actually is. The way we spend our money is not just a financial record — it is a measure and reflection of our real priorities. Changed behavior always begins with changed thinking — not the reverse.",
        spiritual_objective: "Call the reader to honest self-examination — not condemnation — and to the profound freedom of aligning their financial life with their stated beliefs about God.",
        application: "End this first movement in silence and prayer. Ask God to reveal any gap between what you say you believe about Him and what your financial life actually reflects. Write down one conviction — a well-thought-out resolution between you and God — about who owns your resources. This is not a rule. It is a stake in the ground."
      }
    ]
  },
  {
    number: "MOVEMENT TWO",
    title: "Principles That Don't Move",
    subtitle: "Days 8–14 | Biblical Money Management",
    description: "God's Word contains timeless financial principles that apply in every economic climate, at every income level, and in every life stage. These principles are not strategies — they are expressions of wisdom that flows from a stewardship worldview. Over the next seven days, we examine the five foundational principles of biblical money management and how they reshape the practical decisions of daily life.",
    color: "2E6E8A",
    days: [
      {
        day: 8,
        title: "The Principle That Makes All the Others Possible",
        subtitle: "Spending Less Than You Earn Is Not a Budget Tip — It's a Theology",
        theme: "Spend Less Than You Earn / Margin",
        scripture: "Proverbs 21:20 — \"A wise person's house has the finest furnishings; fools waste their money.\"",
        summary: "The first of Ron Blue's five money management principles — spend less than you earn — is not a budgeting technique. It is the practical expression of stewardship. Without margin, there is nothing to give, nothing to save, and no flexibility to respond to God's direction. Margin — the difference between what comes in and what goes out — is the breathing room through which financial faithfulness becomes possible. Without it, every other principle collapses.",
        spiritual_objective: "Help the reader see margin not as restriction but as preparation — the space where generosity, obedience, and opportunity can live.",
        application: "Calculate your current margin: what comes in each month versus what goes out. If your margin is zero or negative, this is your most important starting point. If you have margin, examine whether it is being used intentionally or quietly absorbed by lifestyle creep."
      },
      {
        day: 9,
        title: "Giving Breaks What Accumulation Cannot",
        subtitle: "Why Generosity Is the Antidote to Money's Power Over You",
        theme: "Give Generously / Giving Breaks the Power of Money",
        scripture: "2 Corinthians 9:7 — \"Each person should do as he has decided in his heart — not reluctantly or out of necessity, for God loves a cheerful giver.\"",
        summary: "The second principle — give generously — does something money itself cannot: it breaks money's power over us. Ron Blue taught that giving is not about emptying ourselves but about becoming conduits rather than containers. When we give, we declare with our dollars that we believe God owns it all and that His economy is more reliable than our accumulation. The kingdom of heaven is worth far more than anything we own. As Jim Elliot said, he is no fool who gives what he cannot keep to gain what he cannot lose.",
        spiritual_objective: "Free the reader from the fear that giving costs them something — and invite them into the discovery that generosity is not depletion but declaration.",
        application: "Identify one act of generosity this week that stretches you just beyond your comfort zone — not into irresponsibility, but into faith. Then give it with open hands and notice what happens in your heart afterward."
      },
      {
        day: 10,
        title: "The Dangerous Master",
        subtitle: "What Debt Does to Your Future Before the Future Arrives",
        theme: "Avoid Debt / Debt Mortgages the Future",
        scripture: "Proverbs 22:7 — \"The rich rule over the poor, and the borrower is a slave to the lender.\"",
        summary: "The third principle — avoid debt — is not about prohibition but about principle. Ron Blue was clear: the Bible does not say borrowing money is a sin. It says the borrower is a slave to the lender. And slaves don't have the flexibility to follow God wherever He leads. Debt precommits your future dollars, mortgaging your ability to respond to God's direction. Getting into debt is easy. Getting out is far harder. The magic of compounding works beautifully for the saver — and brutally for the borrower.",
        spiritual_objective: "Establish a sober, biblically grounded posture toward debt — neither shame-based nor permissive, but wise. Help the reader see debt as a spiritual flexibility issue, not merely a financial one.",
        application: "List every debt you currently carry. Beside each one, honestly answer: Does having this debt limit my ability to respond freely to what God might ask of me? Let the answer guide your next steps — not guilt, but clarity."
      },
      {
        day: 11,
        title: "The Ant Knows Something You Don't",
        subtitle: "Planning for What You Cannot See Is Called Wisdom, Not Worry",
        theme: "Build Financial Margin / Plan for the Unexpected",
        scripture: "Proverbs 6:6–8 — \"Go to the ant, you slacker! Observe its ways and become wise... It prepares its provisions in summer; it gathers its food during harvest.\"",
        summary: "The fourth principle — plan for financial margin — is rooted in the biblical wisdom of anticipation. The ant does not wait for winter to begin storing. Nor does it panic when winter comes, because it prepared. Building margin — an emergency fund, savings for the unexpected — is not a lack of faith in God's provision. It is stewardship of the provision He has already given. The unexpected will occur. The question is not whether — but whether you'll be ready.",
        spiritual_objective: "Distinguish between anxiety-driven hoarding and wisdom-driven preparation, helping the reader embrace margin-building as an act of faith and faithfulness rather than fear.",
        application: "If you do not have an emergency fund, determine today what your first milestone is — even if it is only $500. If you do have one, evaluate whether it is adequate for your household's needs. Pray over your savings goal: every goal is a statement of faith."
      },
      {
        day: 12,
        title: "Every Goal Is a Statement of Faith",
        subtitle: "Why Nehemiah's Building Plan Is Also Your Financial Plan",
        theme: "Set Long-Term Goals / Goal Setting as Faith",
        scripture: "Proverbs 16:9 — \"A man's heart plans his way, but the LORD determines his steps.\"",
        summary: "The fifth principle — set long-term goals — is more than financial planning. Ron Blue taught that every goal you set is a statement of faith. Nehemiah's story shows the pattern: identify the need, pray specifically, experience appropriate fear, survey the situation honestly, set a clear goal, and rely on God for the result. The goal will always be accomplished if God put it in your heart — and God will get all the glory. Short-term thinking produces short-term results. Long-term perspective produces peace.",
        spiritual_objective: "Restore goal-setting as a sacred, faith-filled practice — not mere ambition, but partnership with God around what He has placed on the reader's heart.",
        application: "Write down one financial goal for the next 12 months. Make it specific and measurable. Then pray over it: \"Lord, if this goal is from You, provide what I cannot. If it is not from You, redirect me.\" Hold the goal with open hands, but hold it."
      },
      {
        day: 13,
        title: "The Longer Your View, the Better Your Decisions",
        subtitle: "Three Truths About Financial Decision-Making That Change Everything",
        theme: "Financial Decision-Making Principles",
        scripture: "James 4:13–14 — \"You don't even know what tomorrow will bring — what your life will be! For you are like smoke that appears for a little while, then vanishes.\"",
        summary: "Ron Blue offered three transferable decision-making principles: there is no such thing as an independent financial decision (everything affects everything else); the longer-term your perspective, the better your decision today; and financial maturity is being able to give up today's desires for future benefits. These principles do not require a large income. They require wisdom — which God gives generously to those who ask.",
        spiritual_objective: "Develop the reader's capacity for long-horizon thinking in their finances, freeing them from the tyranny of the immediate and the comparison trap of the present.",
        application: "Before your next significant financial decision, ask: How will this look not in one month but in one year? In five years? In eternity? The longer the view, the clearer the choice usually becomes."
      },
      {
        day: 14,
        title: "The Checkbook That Doesn't Lie",
        subtitle: "When Your Spending Plan Becomes a Discipleship Document",
        theme: "Budget as Worship / Spending Plan as Spiritual Tool",
        scripture: "Matthew 6:21 — \"For where your treasure is, there your heart will be also.\"",
        summary: "Ron Blue said it plainly in his teaching: a spending plan — what many call a budget — is not a control document. It is a discipleship document. It shows whether your financial behavior aligns with your spiritual beliefs and convictions. Stewardship transforms when a budget stops being about restriction and starts being about revelation — revealing where your real priorities live. When you invite God into your spending plan, you turn routine management into stewardship and stewardship into worship.",
        spiritual_objective: "Redeem the reader's relationship with their budget — stripping away the shame, anxiety, and resentment often attached to it — and replace it with a posture of worship and intentionality.",
        application: "Review your current budget or spending plan — or create a simple one this week. Ask over each category: Does this reflect what I say I believe about God, generosity, and provision? Make one adjustment this week that brings behavior and belief into alignment."
      }
    ]
  },
  {
    number: "MOVEMENT THREE",
    title: "Learning the Secret of Enough",
    subtitle: "Days 15–21 | Live: Contentment & Lifestyle",
    description: "Lifestyle is the biggest choice any of us will make with our finances. It is also the most spiritually loaded one. The question at the center of this movement — \"How much is enough?\" — is not a math problem. It is a faith question. Ron Blue taught that the answer to this question is not a number. It is a Person. These seven days explore the Prosperity Paradox, the disease of materialism, and the learned secret of contentment.",
    color: "3A7A3A",
    days: [
      {
        day: 15,
        title: "The American Dream and the Paradox Inside It",
        subtitle: "More Choices Is Not the Same Thing as More Freedom",
        theme: "The Prosperity Paradox",
        scripture: "Hebrews 13:5 — \"Be satisfied with what you have, for He Himself has said, I will never leave you or forsake you.\"",
        summary: "Ron Blue shared his own journey — from a green trailer with a young wife and few choices, to 50 years later with 25 family members, multiple homes, businesses, college tuitions, and an overwhelming array of financial decisions. He called it the Paradox of Prosperity: the more you have doesn't give you more freedom. It may give you less real freedom because now you're confronted with a multitude of choices you've got to make. The American Dream does not give you financial freedom. It gives you more to decide.",
        spiritual_objective: "Release the reader from the cultural assumption that more is always better, and open them to the unexpected peace that comes from setting a finish line rather than endlessly chasing more.",
        application: "Reflect honestly: Has accumulating more in your life produced more peace or more complexity? Name one area where abundance has actually created burden. Ask God what \"enough\" looks like in that area for this season of your life."
      },
      {
        day: 16,
        title: "The Answer Was Always What You Already Have",
        subtitle: "Hebrews 13:5 and the Question That Finally Has an Answer",
        theme: "Contentment / How Much Is Enough",
        scripture: "Philippians 4:11–13 — \"I have learned in whatever situation I am to be content... I can do all things through him who strengthens me.\"",
        summary: "For years Ron Blue helped people mathematically determine \"how much is enough\" — running the numbers, modeling the scenarios. Then, reading Hebrews 13:5 for perhaps the hundredth time, the answer came clearly: enough is exactly what you have right now, because Jesus said \"I will never leave you or forsake you.\" Security is never a number. If you don't define enough, then more will define you. The number always moves. Enough is not about how much you have — it's about Whom you trust.",
        spiritual_objective: "Bring genuine rest to the reader's ongoing anxiety about financial adequacy — not through financial achievement but through anchoring trust in God's unchanging presence and provision.",
        application: "Spend five minutes each morning this week simply saying: \"Lord, I have enough because I have You.\" Then notice what that prayer does to your anxiety about your financial situation throughout the day."
      },
      {
        day: 17,
        title: "Materialism Is Not About How Much You Own",
        subtitle: "What a Mud Hut and a D Battery Taught Ron Blue About Worship",
        theme: "Materialism / The Definition That Changes Everything",
        scripture: "1 Timothy 6:6 — \"Godliness with contentment is great gain.\"",
        summary: "In Africa, watching a little girl play joyfully with a D battery on a pile of discarded rocks, Ron Blue asked a local pastor about the greatest hindrance to the gospel. The answer stunned him: materialism. The pastor explained that materialism is not about having a lot and wanting more. It is defined by worshiping what you have and what you want — believing that having more things can bring contentment and joy. This sickness is present in every corner of the world and is just as prevalent among the poor as among the rich.",
        spiritual_objective: "Redefine materialism in the reader's heart — not as a wealth problem but as a worship problem — so they can address its root rather than just its symptoms.",
        application: "Where does the desire for more show up most consistently in your life? Is it your home, your wardrobe, your technology, your experiences? Name it honestly. Then ask: What need am I actually trying to meet through more? Bring that need to God directly."
      },
      {
        day: 18,
        title: "Contentment Is Learned, Not Inherited",
        subtitle: "The Apostle Paul Said He Had to Practice This — So Do You",
        theme: "Learning Contentment as a Spiritual Discipline",
        scripture: "Philippians 4:11 — \"I have learned to be content in whatever circumstances I am.\"",
        summary: "Paul wrote from a prison cell — not a comfort zone. And he used a loaded word: learned. Contentment isn't automatic. It isn't the result of having enough money, enough stability, or enough margin. It is a skill we develop as we walk with God. Ron Blue taught: contentment is taught by God and practiced by us. You can't be grateful and discontent at the same time. Gratitude turns what you have into enough. Every morning, thanking God for three specific things money can't buy is not a spiritual cliché — it is a training program.",
        spiritual_objective: "Move contentment from an abstract virtue to a daily practiced discipline — something the reader actively cultivates rather than passively waits to feel.",
        application: "For the next seven days, begin every morning by naming three specific things you are grateful for that money cannot buy. Keep a running list. At the end of the week, review what the list reveals about the actual richness of your life."
      },
      {
        day: 19,
        title: "Setting a Finish Line in a Culture That Never Does",
        subtitle: "The Freedom That Comes When You Decide \"This Is Enough\"",
        theme: "Lifestyle Finish Line / Defining Enough",
        scripture: "1 Timothy 6:8 — \"If we have food and clothing, we will be content with these.\"",
        summary: "We live in a culture that doesn't set finish lines. We are confronted every day with people accumulating more and more — and we haven't stopped to ask where our finish line actually is. In RBI teaching, a lifestyle finish line is the decision — made prayerfully, with your spouse or a trusted friend — about what constitutes enough for your household. It is not a poverty line. It is a freedom line. Once drawn, it transforms your relationship with money from chasing to choosing.",
        spiritual_objective: "Empower the reader to make one of the most liberating financial decisions available to them: defining their lifestyle finish line — an act of both wisdom and worship.",
        application: "Begin a conversation — with your spouse, or in your journal if you are single — about what your household's lifestyle finish line looks like. What is the home that is \"enough\"? The car? The income? This is a faith conversation, not just a financial one."
      },
      {
        day: 20,
        title: "Provision, Contentment, Enjoyment",
        subtitle: "What 1 Timothy Says Is Actually the Right Christian Lifestyle",
        theme: "The Three Standards of a Christian Lifestyle",
        scripture: "1 Timothy 6:17 — \"Instruct those who are rich in the present age not to be arrogant or to set their hope on the uncertainty of wealth, but on God, who richly provides us with all things to enjoy.\"",
        summary: "Ron Blue turned to 1 Timothy to define what the right Christian lifestyle actually looks like — and found three standards, not one. First: provision. We are commanded to provide for our families. Second: contentment. God wants us to have the necessities of life. Third: enjoyment. God richly provides things to enjoy. This is not legalism — there is no single lifestyle God requires of all Christians. The only appropriate Christian lifestyle is the one God has provided for you, and you can only determine that by spending time on your knees.",
        spiritual_objective: "Free the reader from both legalism and comparison in their lifestyle choices — toward a personal, prayerful posture of gratitude for exactly what God has provided.",
        application: "Write one sentence about what provision looks like for your family right now. One sentence about what contentment looks like. One sentence about what enjoyment looks like. Then ask: Am I living within these three, or am I reaching beyond them in ways that produce anxiety rather than peace?"
      },
      {
        day: 21,
        title: "Your Spending Plan Is How You Show Up to the Conversation",
        subtitle: "Delayed Gratification Is the Only Way to Expand What's Available",
        theme: "Delayed Gratification / Financial Maturity",
        scripture: "Proverbs 13:11 — \"Wealth obtained by fraud will dwindle, but whoever earns it through labor will multiply it.\"",
        summary: "Ron Blue offered a transferable concept for the LIVE section of the pie: the only way to increase the pieces of the pie excluding your lifestyle is delayed gratification. Financial maturity is being able to give up today's desires for future benefits. Every dollar not consumed today is a dollar available for giving, saving, or investing tomorrow. The butterfly effect of money is real: $1.50 saved daily becomes nearly $11,000 over 20 years. Small decisions, compounded over time, produce dramatically different destinations.",
        spiritual_objective: "Build in the reader a long-horizon perspective toward lifestyle decisions — replacing impulsive consumption with intentional restraint as an expression of stewardship and wisdom.",
        application: "Identify one regular expense that represents an easy, low-sacrifice place to exercise delayed gratification. Calculate what redirecting those dollars over 12 months could accomplish — toward debt reduction, emergency savings, or generosity. Make the decision this week."
      }
    ]
  },
  {
    number: "MOVEMENT FOUR",
    title: "You Can't Take It With You — But You Can Send It Ahead",
    subtitle: "Days 22–28 | Give: Generosity & the Treasure Principle",
    description: "Giving is not a financial topic. It is a theological one. When we give, Ron Blue taught, we are not performing an act — we are participating in the character of God. God so loved that He gave. Generosity is how we were created to live. This movement explores the motivations for giving, the transforming power of the Treasure Principle, and what it means to become a conduit rather than a container of God's resources.",
    color: "7A3A6B",
    days: [
      {
        day: 22,
        title: "You're About to Talk About the Sensitive Thing",
        subtitle: "Why Giving Makes People Nervous and What That Reveals",
        theme: "Our Relationship with Giving / Emotional Barriers",
        scripture: "2 Corinthians 8:9 — \"For you know the grace of our Lord Jesus Christ: Though He was rich, for your sake He became poor, so that by His poverty you might become rich.\"",
        summary: "Ron Blue acknowledged it plainly: of all the topics in biblical stewardship, giving is the most emotionally loaded. Many believers carry shame, guilt, fear, or skepticism into any conversation about generosity. The study asks participants to name their emotional response: shame, joy, guilt, fear, or other. The reason giving touches something so deep is that it goes directly to the question of ownership. Giving positions our hearts to respond in gratitude for God's provision and to surrender to His ownership of all we have.",
        spiritual_objective: "Create a safe, honest entry point into the topic of generosity — releasing shame and guilt while inviting the reader toward the joy that giving was always meant to produce.",
        application: "Name your honest emotional response when you think about giving. Don't perform the right answer. Write down the real one. Then ask: Where did that response come from? What would it take for giving to feel like freedom rather than obligation?"
      },
      {
        day: 23,
        title: "The Five Reasons the Bible Says to Give",
        subtitle: "And the One That Surprised Even Ron Blue",
        theme: "Biblical Motivations for Giving",
        scripture: "Matthew 25:21 — \"Well done, good and faithful slave! You were faithful over a few things; I will put you in charge of many things.\"",
        summary: "Ron Blue identified five motivations the Bible gives for generosity: gratitude for God's grace, accountability for what has been entrusted to us, the rewards promised in Scripture, the declaration that God owns it all, and — the one that moved Ron most — love for the Lord Jesus Christ who was rich but became poor so we might become rich. Giving out of love is not obligation. It is response. When we understand what was given for us, what we give in return looks very different.",
        spiritual_objective: "Replace obligation-driven giving with love-driven giving — rooting generosity not in duty or guilt but in a deepening response to the gospel.",
        application: "Read 2 Corinthians 8:9 slowly. Sit with what it means that Jesus, who was rich, became poor for you. Let that sink for several minutes before you pray. Then ask God: What would it look like for my giving to flow from gratitude for this — rather than from duty, fear, or expectation of return?"
      },
      {
        day: 24,
        title: "Tithing Is the Training Wheels",
        subtitle: "What Happens When You Decide the Floor Is Just the Beginning",
        theme: "Tithing as Starting Point / Proportionate Giving",
        scripture: "Exodus 23:19 — \"Bring the best of the firstfruits of your land to the house of the LORD your God.\"",
        summary: "Ron Blue said it memorably: tithing is the training wheels of giving. The tithe is where faithfulness begins, not where it ends. And giving from the first — from the firstfruits, before we know whether the rest will come — is an act of declaration. It declares that God is the owner and we are managers returning a portion to Him for His use. Proportionate giving, planned giving, and precommitted giving are three disciplines that move generosity from reaction to intention.",
        spiritual_objective: "Encourage the reader who is not yet giving proportionately and challenge the reader who has stopped there — both toward the next faithful step in generosity.",
        application: "Evaluate your current giving honestly: Are you giving? Proportionately? Planned in advance? Precommitted before the month begins? Identify your next faithful step — not the final step, but the next one — and make a specific commitment."
      },
      {
        day: 25,
        title: "The Treasure Principle That Changes Everything",
        subtitle: "You Can't Take It With You — But You Can Send It Ahead",
        theme: "The Treasure Principle / Heart Follows Money",
        scripture: "Matthew 6:19–21 — \"For where your treasure is, there your heart will be also.\"",
        summary: "Randy Alcorn's Treasure Principle — which Ron Blue embraced and taught — distills the message of Matthew 6 into a single unforgettable idea: You can't take it with you, but you can send it ahead. Everything we accumulate here will one day become worthless. What we send ahead — through giving that advances the kingdom — nothing can destroy. Jesus' statement in Matthew 6:21 works in both directions: your heart follows your money. If you want to know where your heart is, follow the money. If you want to move your heart, move your money.",
        spiritual_objective: "Reorient the reader's entire financial imagination toward eternity — not to induce guilt about what they own but to ignite excitement about what they can send ahead.",
        application: "Spend time with Matthew 6:19–21 and ask: If my heart truly follows my treasure, where is my heart right now? Then ask the more exciting question: If I began sending more ahead, what would happen to my heart over the next 12 months?"
      },
      {
        day: 26,
        title: "Howard Hughes and the Prison Money Built",
        subtitle: "What Happens to the Soul That Refuses to Give",
        theme: "Giving as Liberation / Danger of Hoarding",
        scripture: "Luke 12:15 — \"Watch out and be on guard against all greed because one's life is not in the abundance of his possessions.\"",
        summary: "Howard Hughes died with $2.5 billion — miserable, alone, having pushed everyone he loved away. His fortune had built a prison. The manuscript of God Owns It All uses his story as a warning: wealth without generosity doesn't bring freedom; it brings bondage. Meanwhile, the widow at the temple gave everything she had — and was seen and honored by Jesus. The kingdom of heaven is worth far more than anything we own. Giving breaks the power money has over us, and that power is real.",
        spiritual_objective: "Confront the real spiritual danger of hoarding — not through shame but through the stark contrast between lives lived in accumulation and lives lived in generosity.",
        application: "Ask yourself honestly: Is there any area of your financial life where accumulation has become its own end — where having more has become a source of identity or security rather than a resource to steward? Name it. Pray over it. Consider a specific act of generosity in that very area as a declaration of freedom."
      },
      {
        day: 27,
        title: "Conduits, Not Containers",
        subtitle: "We Need the Money to Flow Through Us, Not Stop with Us",
        theme: "Generosity as Identity / Conduit vs. Container",
        scripture: "Proverbs 11:25 — \"A generous person will be enriched, and the one who gives a drink of water will receive water.\"",
        summary: "The language Ron Blue used in the curriculum is worth sitting with: we need to be conduits and not containers of the resources God gives us. A container holds. A conduit flows. The difference is not how much passes through — it is orientation. Generosity is holistic: it is time, talent, treasure, and testimony. Whatever God has put in your hands, you have the opportunity to freely receive it and to generously distribute it. Every time we give, we step a little closer to the very heart of God.",
        spiritual_objective: "Expand the reader's vision of generosity beyond money to include the full range of resources God has entrusted to them — time, relationships, skills, and story.",
        application: "List three non-financial ways you can be a conduit this week: an hour of time given to someone who needs it, a skill offered freely, a piece of your story shared with someone who needs to hear it. Then do those three things."
      },
      {
        day: 28,
        title: "Joy Always Follows Generosity",
        subtitle: "Why This Is Not a Coincidence but a Design",
        theme: "Generosity as Worship / Joy as the Return",
        scripture: "John 3:16 — \"God loved the world in this way: He gave His One and Only Son.\"",
        summary: "Ron Blue said it plainly in the LT Production transcript: when you give, you're not performing an act — you're participating in His character. For God so loved that He gave. Generosity directly reflects the character and nature of God. Joy always follows generosity because it is how we were created to live. People stop waiting until they have enough to give and discover a joy they didn't know was possible. Generosity doesn't deplete — it multiplies. It adds. It overflows.",
        spiritual_objective: "Leave the reader with a deep, settled conviction that generosity is not sacrifice — it is participation in the nature of God, and joy is the inevitable return.",
        application: "Think of the most joyful experience of giving you have ever had — a gift that cost you something, an act of generosity that surprised even you. Write it down. Let it remind you: this is who you were made to be. Ask God where He is inviting you into that joy again."
      }
    ]
  },
  {
    number: "MOVEMENT FIVE",
    title: "The Weight We Were Not Meant to Carry",
    subtitle: "Days 29–33 | Owe: Debt, Taxes & Freedom",
    description: "Debt is one of the most emotionally and spiritually charged topics in biblical stewardship — not because it is taboo but because it is consequential. The Bible does not say debt is sin. But it is honest about what debt does: it makes you a slave to the lender, it presumes upon a future only God knows, and it may close doors through which God was preparing to walk. These five days offer honest, biblically grounded wisdom for navigating the OWE piece of the pie.",
    color: "8B4513",
    days: [
      {
        day: 29,
        title: "You Are a Slave to Someone",
        subtitle: "The Question Is Only to Whom",
        theme: "Debt as Bondage / Slavery to the Lender",
        scripture: "Proverbs 22:7 — \"The rich rule over the poor, and the borrower is a slave to the lender.\"",
        summary: "Ron Blue was direct: anytime you borrow money, you are a slave to the lender. This doesn't depend on the lender's kindness. It doesn't matter if the lender is a bank, a friend, or a parent. The relationship has changed. The lender always has first call on your money. Your debt doesn't define you — but it can confine you. Before any conversation about how to get out of debt, we must sit with the honest weight of what debt costs beyond the interest rate.",
        spiritual_objective: "Help the reader feel, not just understand, the real cost of debt — not to produce shame but to clarify motivation and generate genuine resolve toward freedom.",
        application: "Name every obligation you currently carry. For each one, ask: Does this debt limit my ability to follow God freely? Does it produce anxiety or peace? This inventory is not about shame — it is about clarity. Clarity is the beginning of freedom."
      },
      {
        day: 30,
        title: "Presuming on What Only God Knows",
        subtitle: "The Spiritual Danger Inside Every Loan Agreement",
        theme: "Debt Presumes on the Future / James 4 Warning",
        scripture: "James 4:13–14 — \"You don't even know what tomorrow will bring — what your life will be! For you are like smoke that appears for a little while, then vanishes.\"",
        summary: "Ron Blue identified two specific spiritual dangers of debt: it presumes upon a future only God knows, and it may deny God an opportunity to provide in His own way and time. When Ron started his financial planning firm in 1979, he intended to use a bank line of credit. Instead, he did not draw on it — and watched God provide in ways he would have missed if he had borrowed first. Debt puts our confidence in future circumstances in the place of God.",
        spiritual_objective: "Develop in the reader a healthy spiritual caution toward debt — not fear-based paralysis but wise, faith-filled restraint that leaves room for God to work.",
        application: "Before your next debt decision, ask the four questions Ron Blue developed: Is the economic return greater than the economic cost? Is there a guaranteed way to repay? Will this debt create spiritual or relational danger? Are my spouse and I in agreement? If you cannot answer all four with confidence, wait."
      },
      {
        day: 31,
        title: "Getting In Is Easy. Getting Out Is a Different Story.",
        subtitle: "The Magic of Compounding Works Against You When You Owe",
        theme: "The Economics and Psychology of Debt",
        scripture: "Romans 13:8 — \"Do not owe anyone anything, except to love one another.\"",
        summary: "The magic of compounding — which works so beautifully for the saver and investor — works brutally for the borrower. Interest paid is wealth lost. Ron Blue was unambiguous: credit card debt and consumer debt almost never make economic sense. Getting into debt is easy. Getting out is far harder. The psychological weight of debt — the constant awareness of what is owed — is real and documented. Until we experience life without the bondage of debt, it is impossible to fully understand how much of a chain it is.",
        spiritual_objective: "Motivate the reader toward a concrete debt-elimination plan, fueled not by financial urgency alone but by the vision of the spiritual and relational freedom waiting on the other side.",
        application: "If you carry consumer debt, determine your payoff priority today: begin with the highest-interest debt or the smallest balance for early momentum. Commit to one additional payment this month, however small. Every extra payment is a declaration: I am moving toward freedom."
      },
      {
        day: 32,
        title: "Financial Issues Are Symptoms of Heart Issues",
        subtitle: "What Your Debt and Your Tax Return Are Really Telling You",
        theme: "Debt as Symptom / Heart Diagnosis",
        scripture: "Hebrews 4:12 — \"The word of God is living and effective and sharper than any double-edged sword... It judges the thoughts and intentions of the heart.\"",
        summary: "Ron Blue offered a provocative reframe: debt is often a symptom of spending more than we make. And spending more than we make is a symptom of something in the heart — comparison, fear, identity tied to possession, refusal to delay gratification. Taxes, he noted, are a symptom of income — and he called them worthy of gratitude for that reason. Financial issues are symptoms of heart issues. Treating the symptom without addressing the root produces temporary change, not lasting transformation.",
        spiritual_objective: "Move the reader from surface-level financial behavior change toward the deeper work of heart examination and spiritual renewal — where lasting change actually lives.",
        application: "Ask yourself honestly: What heart issue most drives my debt or financial stress? Is it comparison? Fear of scarcity? Identity in material things? The need to be seen as successful? Name it. Bring it to God. Then ask for wisdom — which He promises to give generously to those who ask."
      },
      {
        day: 33,
        title: "The Toothpaste and the Lesson You Can't Unlearn",
        subtitle: "Why the Time to Make Good Decisions Is Before You Need To",
        theme: "Wisdom Over Impulse / The Cost of Debt Decisions",
        scripture: "Luke 14:28 — \"For which of you, wanting to build a tower, doesn't first sit down and calculate the cost to see if he has enough to complete it?\"",
        summary: "The manuscript uses the image of toothpaste: easy to squeeze out, nearly impossible to put back. Debt is the same. The time to make the wise decision about borrowing is before the decision, not after. Luke 14's tower-builder sits down to count the cost before construction begins — not halfway through when the foundation is laid but the money is gone. Count the cost first. Calculate the true price — not just the interest rate but the freedom, flexibility, and opportunity cost of every obligation you take on.",
        spiritual_objective: "Build pre-decision wisdom habits into the reader's financial decision-making — so that future debt decisions are made from conviction and calculation, not impulse and emotion.",
        application: "Write out what \"counting the cost\" looks like for your household before any major debt decision. Include the financial cost, the opportunity cost, the relational cost, and the spiritual cost. Make this a practice, not just a concept."
      }
    ]
  },
  {
    number: "MOVEMENT SIX",
    title: "Faithful with Little, Trusted with Much",
    subtitle: "Days 34–40 | Grow: Margin, Faithfulness & Legacy",
    description: "The final movement brings the entire journey full circle. Grow is not about accumulation for its own sake. It is about building the margin that makes generosity, provision, and long-term faithfulness possible — and about the legacy that faithful stewardship creates across generations. These final seven days move from the practical discipline of saving and investing to the eternal horizon of what we leave behind: not just wealth, but wisdom; not just assets, but faith.",
    color: "1B3A5C",
    days: [
      {
        day: 34,
        title: "The Five Stages and Where You Are Right Now",
        subtitle: "Struggling, Surviving, Stable, Secure, or Surplus — And the One Way Through",
        theme: "Sequential Investing / The 5S Journey",
        scripture: "Luke 16:10 — \"Whoever can be trusted with very little can also be trusted with much.\"",
        summary: "Ron Blue introduced the sequential investing framework — five stages on a financial journey from struggling to surplus. The stages are: struggling (eliminate high-interest debt), surviving (create an emergency fund), stable (save for major purchases), secure (diversify toward long-term goals), and surplus (complete long-term goals and determine what to do with the excess). The only way to move from one level to the next is the same at every stage: spend less than you earn, and do it over a long period of time.",
        spiritual_objective: "Give the reader an honest, hopeful assessment of where they stand on their financial journey — and the clarity that there is a path forward from wherever they are.",
        application: "Place yourself honestly on the sequential investing journey. Which stage are you in right now? What is the very next step that would move you forward? Write it down. Commit to beginning that step this month. Every goal is a statement of faith."
      },
      {
        day: 35,
        title: "The Magic Is Not What You Think",
        subtitle: "A Little Bit Over a Long Time Becomes a Lot",
        theme: "Compounding / Faithful Small Steps Over Time",
        scripture: "Proverbs 13:11 — \"Wealth gained hastily will dwindle, but whoever gathers little by little will increase it.\"",
        summary: "The magic of compounding works for those who save consistently over time. Ron Blue shared stories of people the world would never consider wealthy by appearance — who accumulated remarkable resources simply by spending less than they earned and doing it faithfully over decades. Net worth is always and only a measure of God's provision. The goal of saving is not to achieve security through accumulation — we already established that security is never a number. The goal is to be ready for whatever God has next.",
        spiritual_objective: "Restore hope and motivation to readers who feel they started too late or have too little — by showing that faithfulness over time, not large starting amounts, is what builds meaningful margin.",
        application: "Calculate what setting aside even a small amount consistently — whatever that amount is for your household — would produce over 10 years with modest growth. Let the number inspire you. Then begin, or increase, this week."
      },
      {
        day: 36,
        title: "Net Worth Is a Measure of God's Provision",
        subtitle: "Not a Scoreboard. Not Your Identity. His.",
        theme: "Stewardship of Wealth / Net Worth in Eternal Context",
        scripture: "Deuteronomy 8:17–18 — \"Be careful not to say in your heart: My power and my own ability has built this wealth for me. But remember that the LORD your God gives you the power to gain wealth.\"",
        summary: "One of Ron Blue's personal convictions from the manuscript: net worth is always and only a measure of God's provision. Not your cleverness. Not your discipline alone. Not your sacrifice. God's provision — channeled through your faithfulness. This reframe changes how we think about both having much and having little. Accumulation is not evidence of God's favor. Loss is not evidence of His absence. In both, He remains the owner, and we remain stewards accountable for faithful management.",
        spiritual_objective: "Free the reader from identity-attachment to their net worth — both the pride that comes with abundance and the shame that comes with scarcity — grounding them instead in the unchanging truth of God's ownership.",
        application: "Look at your current net worth honestly. Practice saying, without pride or shame: \"This is a measure of God's provision to this point. He owns it all. I am accountable for what I do with it next.\" Let that be your posture — not performance."
      },
      {
        day: 37,
        title: "Stewardship Transforms Relationships",
        subtitle: "What Happens When Couples Pray Over the Spending Plan Together",
        theme: "Money and Relationships / Financial Unity",
        scripture: "Amos 3:3 — \"Can two walk together unless they have agreed to meet?\"",
        summary: "Ron Blue taught that stewardship transforms relationships — particularly marriage. When couples pray over their spending plan together, arguments turn into alignment. They are no longer fighting each other — they are partnering with God together. Money is no longer a scorecard. It becomes a shared act of stewardship. The source of most financial conflict in relationships is not actually money. It is misaligned beliefs about ownership, security, and identity — the very things this entire journey addresses at the root.",
        spiritual_objective: "Help the reader apply stewardship principles to their most important financial relationship — whether as a couple, within a family, or as a community of believers walking together in financial accountability.",
        application: "If you are married: schedule a specific time this week to review your finances together — not to fight about money but to pray over your spending plan as an act of shared stewardship. If you are single: identify one trusted friend with whom you can share your financial goals and convictions and ask for mutual accountability."
      },
      {
        day: 38,
        title: "Legacy Is Not What You Leave After You Die",
        subtitle: "It Is What You Live While You Are Alive",
        theme: "Legacy as Daily Living / Stewardship Across Generations",
        scripture: "Proverbs 13:22 — \"A good man leaves an inheritance for his children's children.\"",
        summary: "Ron Blue reframed legacy entirely in the LT Production teaching: legacy is not what you plan for the end of your life. It begins the moment you start living God's way. He identified two types of inheritance: one that passes down resources without relationship — which often causes confusion — and one that passes down values before wealth, which produces unity and gratitude. Don't transfer money until you've transferred wisdom. Your legacy is being written right now, in the daily decisions of faithful stewardship.",
        spiritual_objective: "Expand the reader's understanding of legacy beyond estate planning to include the daily, relational, and spiritual inheritance they are building or neglecting right now.",
        application: "Ask yourself: What financial values am I passing to the people who are watching my life — my children, younger believers, my community? More is caught than taught. What are they catching from you right now? Identify one specific way this week to make your stewardship more visible and more deliberate."
      },
      {
        day: 39,
        title: "Write the Letter Your Family Needs to Read",
        subtitle: "The Most Valuable Thing You'll Leave Behind May Have No Dollar Amount",
        theme: "Legacy Letter / Transferring Wisdom",
        scripture: "Psalm 78:4 — \"We will not hide them from their children, telling the next generation the praiseworthy deeds of the LORD, His power, and the wonders He has done.\"",
        summary: "Ron Blue encouraged every person at a certain stage of life to write a legacy letter: a document that records not the financial details but the spiritual ones — what you believe about God's ownership, the lessons learned through provision and loss, the story of His faithfulness. The heirs should never be surprised — not just about the finances, but about the values that drove every decision. Your story may be the most valuable inheritance your family ever receives. Finishing well is a part of stewardship.",
        spiritual_objective: "Invite the reader into one of the most meaningful acts of stewardship available to them: articulating and communicating the spiritual convictions that have shaped their financial life — so those convictions outlive them.",
        application: "Begin a legacy letter today — even if it is only a paragraph. Address it to your children, your grandchildren, or someone whose life your story might shape. Tell them: what you believe about God. What He has taught you about money. Where He has been faithful when you could not see ahead. What you hope they will hold onto after you are gone."
      },
      {
        day: 40,
        title: "Well Done, Good and Faithful Servant",
        subtitle: "The Only Return on Investment That Will Matter When Everything Else Is Gone",
        theme: "Faithful Stewardship / Eternal Accountability and Peace",
        scripture: "Matthew 25:21 — \"Well done, good and faithful slave! You were faithful over a few things; I will put you in charge of many things. Share your master's joy!\"",
        summary: "The journey ends where it began: with the Owner. God does not measure success the way the world does. He measures faithfulness. He said the same thing to the servant with two talents as to the one with five: well done. Not well accumulated. Not well achieved. Well done. If God owns it all — and He does — your goal is not to leave wealth behind. It is to send faith ahead. Legacy is continuity, not control. It is the flow of God's truth and resources through your life into the lives of others. Every act of trust, every gift, every lesson shared is a seed of eternal impact.",
        spiritual_objective: "Bring the reader to a place of settled peace, deep hope, and renewed commitment — not to perform stewardship better but to live it more freely, more joyfully, and more faithfully as a response to the God who owns it all.",
        application: "Return to the convictions you wrote on Day 7. Read them again. Have they deepened over these 40 days? Add to them now. Then do one final thing: offer the whole of your financial life to God in prayer — every account, every debt, every goal, every plan — and release it into the hands of the One who owns it all. Then rest. You are not the owner. You are the steward. And that is more than enough."
      }
    ]
  }
];

function makeHR(color = "CCCCCC") {
  return new Paragraph({
    border: { bottom: { style: BorderStyle.SINGLE, size: 6, color: color, space: 1 } },
    spacing: { after: 120 }
  });
}

function sectionHeader(label, color) {
  return new Paragraph({
    children: [new TextRun({ text: label, color: color, bold: true, size: 24, font: "Arial" })],
    spacing: { before: 120, after: 60 }
  });
}

function makeBodyText(text, options = {}) {
  return new Paragraph({
    children: [new TextRun({
      text,
      font: "Arial",
      size: 22,
      color: options.color || "2C2C2C",
      bold: options.bold || false,
      italics: options.italics || false
    })],
    spacing: { before: options.spaceBefore || 60, after: options.spaceAfter || 120 },
    alignment: options.alignment || AlignmentType.LEFT
  });
}

function buildDayContent(day, mov) {
  const dayColor = mov.color || NAVY;
  const items = [];

  // Page break before each day (except day 1)
  if (day.day > 1) {
    items.push(new Paragraph({ children: [new PageBreak()] }));
  }

  // Day number badge
  items.push(new Paragraph({
    children: [new TextRun({ text: `DAY ${day.day}`, bold: true, size: 20, color: "FFFFFF", font: "Arial" })],
    shading: { fill: dayColor, type: ShadingType.CLEAR },
    spacing: { before: 0, after: 80 },
    indent: { left: 180, right: 180 }
  }));

  // Title
  items.push(new Paragraph({
    heading: HeadingLevel.HEADING_2,
    children: [new TextRun({ text: day.title, bold: true, size: 36, font: "Arial", color: dayColor })]
  }));

  // Subtitle
  items.push(new Paragraph({
    children: [new TextRun({ text: day.subtitle, italics: true, size: 24, font: "Arial", color: GRAY })],
    spacing: { before: 0, after: 160 }
  }));

  items.push(makeHR(dayColor));

  // Core Theme
  items.push(sectionHeader("CORE THEME", dayColor));
  items.push(makeBodyText(day.theme, { bold: false }));

  // Scripture
  items.push(sectionHeader("PRIMARY SCRIPTURE", dayColor));
  items.push(new Paragraph({
    children: [new TextRun({ text: day.scripture, italics: true, size: 22, font: "Arial", color: "3A3A3A" })],
    shading: { fill: LIGHT_BLUE, type: ShadingType.CLEAR },
    spacing: { before: 60, after: 180 },
    indent: { left: 360, right: 360 }
  }));

  // Day Focus
  items.push(sectionHeader("TODAY'S FOCUS", dayColor));
  items.push(makeBodyText(day.summary, { spaceAfter: 180 }));

  // Spiritual Objective
  items.push(sectionHeader("SPIRITUAL & EMOTIONAL OBJECTIVE", dayColor));
  items.push(makeBodyText(day.spiritual_objective, { spaceAfter: 180 }));

  // Application
  items.push(sectionHeader("PRACTICAL APPLICATION", dayColor));
  items.push(new Paragraph({
    children: [new TextRun({ text: day.application, size: 22, font: "Arial", color: "2C2C2C" })],
    shading: { fill: LIGHT_GOLD, type: ShadingType.CLEAR },
    spacing: { before: 60, after: 200 },
    indent: { left: 280, right: 280 }
  }));

  items.push(makeHR("DDDDDD"));

  return items;
}

function buildMovement(mov) {
  const items = [];

  // Page break before movement
  items.push(new Paragraph({ children: [new PageBreak()] }));

  // Movement header
  items.push(new Paragraph({
    children: [new TextRun({ text: mov.number, bold: true, size: 22, color: "FFFFFF", font: "Arial" })],
    shading: { fill: mov.color, type: ShadingType.CLEAR },
    spacing: { before: 0, after: 40 },
    indent: { left: 180, right: 180 }
  }));

  items.push(new Paragraph({
    heading: HeadingLevel.HEADING_1,
    children: [new TextRun({ text: mov.title, bold: true, size: 44, font: "Arial", color: mov.color })]
  }));

  items.push(new Paragraph({
    children: [new TextRun({ text: mov.subtitle, italics: true, size: 26, font: "Arial", color: GRAY })],
    spacing: { before: 0, after: 200 }
  }));

  items.push(makeHR(mov.color));

  items.push(new Paragraph({
    children: [new TextRun({ text: mov.description, size: 22, font: "Arial", color: "3A3A3A" })],
    spacing: { before: 120, after: 240 }
  }));

  items.push(makeHR("CCCCCC"));

  // Each day
  for (const day of mov.days) {
    for (const item of buildDayContent(day, mov)) {
      items.push(item);
    }
  }

  return items;
}

// Build full document
const allChildren = [];

// Cover page
allChildren.push(new Paragraph({ children: [new PageBreak()] }));

allChildren.push(new Paragraph({
  children: [new TextRun({ text: "GOD OWNS IT ALL", bold: true, size: 72, font: "Arial", color: NAVY })],
  alignment: AlignmentType.CENTER,
  spacing: { before: 2880, after: 200 }
}));

allChildren.push(new Paragraph({
  children: [new TextRun({ text: "A 40-Day Devotional Framework", size: 36, font: "Arial", color: GOLD, italics: true })],
  alignment: AlignmentType.CENTER,
  spacing: { before: 0, after: 120 }
}));

allChildren.push(new Paragraph({
  children: [new TextRun({ text: "Based on the Teaching of Ron Blue and the Ron Blue Institute", size: 26, font: "Arial", color: GRAY })],
  alignment: AlignmentType.CENTER,
  spacing: { before: 0, after: 800 }
}));

allChildren.push(makeHR(GOLD));

allChildren.push(new Paragraph({
  children: [new TextRun({ text: "Ownership · Stewardship · Contentment · Generosity · Faithfulness · Legacy", size: 22, font: "Arial", color: GRAY, italics: true })],
  alignment: AlignmentType.CENTER,
  spacing: { before: 200, after: 1440 }
}));

// Introduction page
allChildren.push(new Paragraph({ children: [new PageBreak()] }));

allChildren.push(new Paragraph({
  heading: HeadingLevel.HEADING_1,
  children: [new TextRun({ text: "How to Use This Devotional", bold: true, size: 44, font: "Arial", color: NAVY })]
}));

allChildren.push(makeHR(NAVY));

const introText = [
  "This 40-day devotional is rooted entirely in the source materials of the God Owns It All curriculum developed by Ron Blue and the Ron Blue Institute. Every theme, every principle, and every spiritual objective flows directly from the published manuscript, the curriculum learning objectives, and Ron Blue's recorded teaching transcripts.",
  "The journey is organized into six movements that follow the natural progression of the original six-week curriculum — but extended into a deeper, daily practice of reflection, Scripture engagement, and application. These movements are not isolated topics. They are a connected spiritual journey, each building on the one before it.",
  "MOVEMENT ONE — The Question That Changes Everything (Days 1–7): Perspective and Ownership",
  "MOVEMENT TWO — Principles That Don't Move (Days 8–14): Biblical Money Management",
  "MOVEMENT THREE — Learning the Secret of Enough (Days 15–21): Live — Contentment and Lifestyle",
  "MOVEMENT FOUR — You Can't Take It With You (Days 22–28): Give — Generosity and the Treasure Principle",
  "MOVEMENT FIVE — The Weight We Were Not Meant to Carry (Days 29–33): Owe — Debt and Freedom",
  "MOVEMENT SIX — Faithful with Little, Trusted with Much (Days 34–40): Grow — Margin, Faithfulness, and Legacy",
  "Each day includes: the devotional title and subtitle, the core theme, a primary scripture, a summary of the day's focus drawn directly from Ron Blue's teaching, a spiritual and emotional objective, and a specific practical application.",
  "We recommend reading each day's devotional in the morning, sitting with the scripture for several minutes before reading the content, and returning to the practical application at the end of the day to reflect on how you engaged with it.",
  "This is not a study to complete. It is a journey to take. Move through it at whatever pace serves your formation — but do not rush what God is building in you.",
  "The conviction at the center of everything that follows is this: When ownership changes hands, everything changes. Including hearts."
];

for (const text of introText) {
  const isBullet = text.startsWith("MOVEMENT");
  allChildren.push(new Paragraph({
    children: [new TextRun({ text, size: 22, font: "Arial", color: isBullet ? NAVY : "2C2C2C", bold: isBullet })],
    spacing: { before: 80, after: isBullet ? 60 : 140 },
    indent: isBullet ? { left: 360 } : {}
  }));
}

// Build all movements
for (const mov of movements) {
  for (const item of buildMovement(mov)) {
    allChildren.push(item);
  }
}

const doc = new Document({
  styles: {
    default: {
      document: { run: { font: "Arial", size: 22 } }
    },
    paragraphStyles: [
      {
        id: "Heading1", name: "Heading 1", basedOn: "Normal", next: "Normal", quickFormat: true,
        run: { size: 44, bold: true, font: "Arial", color: NAVY },
        paragraph: { spacing: { before: 360, after: 200 }, outlineLevel: 0 }
      },
      {
        id: "Heading2", name: "Heading 2", basedOn: "Normal", next: "Normal", quickFormat: true,
        run: { size: 36, bold: true, font: "Arial" },
        paragraph: { spacing: { before: 240, after: 120 }, outlineLevel: 1 }
      }
    ]
  },
  sections: [{
    properties: {
      page: {
        size: { width: 12240, height: 15840 },
        margin: { top: 1440, right: 1440, bottom: 1440, left: 1440 }
      }
    },
    children: allChildren
  }]
});

Packer.toBuffer(doc).then(buffer => {
  fs.writeFileSync("/mnt/user-data/outputs/GOIA_40Day_Devotional.docx", buffer);
  console.log("Done: GOIA_40Day_Devotional.docx");
}).catch(err => {
  console.error("Error:", err);
  process.exit(1);
});
