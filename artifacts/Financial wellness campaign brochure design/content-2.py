# -*- coding: utf-8 -*-
# Faith & Finances Collection — 10 volumes. All content original.
# Each volume: title (head, accent-italic tail), felt-need eyebrow, deck, pullquote,
# intro, core scripture (quote, ref), big idea, tags, subtitles, info dict, 6 sessions.
# Session: (head, tail), scripture (quote, ref), tags, [3 questions], step (label, text)

COLLECTION = {
    "deck": ("Ten complete 40-day campaigns and small-group series for the one "
             "subject Jesus spoke about more than almost any other — money — built "
             "on the conviction that how we handle a dollar is never just a money "
             "decision. It is a faith decision, made visible."),
    "framework": ("Faith & Finances helps us follow Jesus with our money. Financial "
        "Wisdom helps us decide well. Money Made Simple helps us live with less noise. "
        "Financial Peace quiets the worry. Wise with Money builds real competence. God, "
        "Money & Me heals the heart behind the habits. Financial Health builds rhythms "
        "that last. Breaking Financial Fear gives us courage. Money and Meaning connects "
        "what we have to what we're here for. And Peace with Money ends the war for good."),
}

VOLUMES = [
 # ----------------------------------------------------------------- 1
 {
  "title": ("Faith &amp;", "Finances"),
  "felt": "FOLLOWING JESUS WITH YOUR MONEY",
  "deck": ("Every paycheck, purchase, debt, and gift is a small confession of what we "
           "actually trust — and these forty days bring faith and finances into the "
           "same room and keep them there."),
  "pullquote": ("How you handle a dollar is not a money question. It is a discipleship "
                "question — and your bank statement is one of the most honest spiritual "
                "journals you will ever keep."),
  "intro": ("Faith &amp; Finances begins with a truth most of us would rather avoid: there "
            "is no neutral money. Jesus talked about money more than almost any other "
            "subject — not because He needed ours, but because He knew it would compete "
            "for the throne of our hearts. <strong>This campaign brings faith and "
            "finances into the same room for forty days, so that the way you earn, spend, "
            "save, and give becomes one more place where you follow Jesus.</strong>"),
  "scripture": ("No one can serve two masters. Either you will hate the one and love the "
                "other, or you will be devoted to the one and despise the other. You "
                "cannot serve both God and money.", "Matthew 6:24 (NIV)"),
  "bigidea": ("Money is not a side issue to your faith — it is one of the clearest places "
              "your faith becomes visible. When you stop serving money and start "
              "stewarding it for God, your finances become an act of worship instead of "
              "a source of fear."),
  "tags": ["discipleship","stewardship","trust","worship","the heart","surrender"],
  "subtitles": ["A 40-Day Journey to Following Jesus With Your Money",
                "Discovering God's Design for Faith and Finances",
                "A 40-Day Path From a Divided Heart to Whole-Life Trust",
                "Letting Your Faith Reach All the Way to Your Wallet"],
  "info": {"audience":"All church &amp; workplace — every household and every desk",
           "season":"Fall discipleship launch · New Year · Stewardship season",
           "score":"10/10 — the gateway campaign for the whole collection",
           "related":"Feeds into 40 Days of Purpose · God Owns It All"},
  "sessions": [
    (("Who Sits on the","Throne"), ("No one can serve two masters.","Matthew 6:24"),
     ["lordship","the heart","masters","surrender","treasure"],
     ["Jesus says money makes a credible bid to be our master. Where in your life does money currently have more say than you would like to admit?",
      "If a stranger studied only your spending from the last month, what would they conclude you love most? Does that match what you say you believe?",
      "What would actually change tomorrow if you treated God — not money — as the master of your financial life?"],
     ("THIS WEEK'S STEP","Before any non-essential purchase this week, pause and ask one question out loud: **\u201cLord, is this worship or worry?\u201d** Tell your partner what you noticed.")),
    (("Owner or","Steward"), ("The earth is the Lord's, and everything in it.","Psalm 24:1"),
     ["ownership","stewardship","Psalm 24","surrender","identity"],
     ["Be honest: do you live as the owner of your money or the manager of God's money? Where does the difference show up?",
      "What is one financial decision you have been making as an owner that you would make differently as a steward?",
      "What does it free you from — and free you for — to believe that none of it was ever yours to begin with?"],
     ("THIS WEEK'S STEP","Write a one-sentence statement that begins, **\u201cBecause God owns it all, this week I will steward by\u2026\u201d** Share it with your partner and pray over it.")),
    (("Counting the","Cost"), ("Suppose one of you wants to build a tower. Won't you first sit down and estimate the cost?","Luke 14:28"),
     ["honesty","budgeting","clarity","courage","planning"],
     ["Jesus assumes a wise person counts the cost before building. When did you last sit down and honestly count the cost of your own life — your income, spending, and debt?",
      "What number in your financial life are you most afraid to look at directly? What has that avoidance been costing you?",
      "Counting the cost is an act of faith, not fear. What would it look like this week to bring God into the actual numbers?"],
     ("THIS WEEK'S STEP","Sit down for thirty honest minutes and write your real numbers on one page — income, fixed costs, debt, giving. Don't fix anything yet. Just **tell the truth**, and bring it to God in prayer.")),
    (("The Freedom of","Enough"), ("Godliness with contentment is great gain.","1 Timothy 6:6"),
     ["contentment","enough","comparison","gratitude","freedom"],
     ["Paul calls contentment \u201cgreat gain.\u201d Where has the lie of \u201cjust a little more\u201d quietly set the terms of your life?",
      "Whose lifestyle are you measuring yours against — and what would change if you stopped?",
      "What in your life right now is already, genuinely, enough — and when did you last stop to thank God for it?"],
     ("THIS WEEK'S STEP","Each day this week, write down **one thing you already have that is enough**. At week's end, read the list to your partner.")),
    (("Generosity as a","Way of Life"), ("Command them to do good, to be rich in good deeds, and to be generous and willing to share.","1 Timothy 6:18"),
     ["generosity","giving","open hands","joy","freedom"],
     ["Generosity is the clearest sign that money has lost its grip on us. How free are your hands right now — and what does that reveal?",
      "Think of the most generous person you know personally. What is their relationship with money like, and what do you want to learn from them?",
      "What is one generous act, just outside your comfort zone, that God may be inviting you into this week?"],
     ("THIS WEEK'S STEP","Give one gift this week that you feel — that costs you something and requires trust. Tell your partner **before and after**.")),
    (("A Faith That Reaches the","Wallet"), ("But seek first his kingdom and his righteousness, and all these things will be given to you as well.","Matthew 6:33"),
     ["kingdom first","commitment","next steps","trust","legacy"],
     ["Over these forty days, where has your faith reached further into your finances than it had before?",
      "What is the one financial pattern God has most clearly asked you to change — and what is your next concrete step?",
      "Who in this group will ask you about that step in thirty days?"],
     ("COMMITMENT STEP","Each person names one kingdom-first financial commitment for the next 90 days — a giving practice, a debt step, or a spending boundary — and names one person in the group who will follow up. Close by praying over each commitment.")),
  ],
 },
 # ----------------------------------------------------------------- 2
 {
  "title": ("Financial","Wisdom"),
  "felt": "DECIDING WELL WITH WHAT YOU HAVE",
  "deck": ("Most money problems are not income problems — they are wisdom problems, and "
           "wisdom is the one asset available to every person, in every season, "
           "regardless of the balance in the account."),
  "pullquote": ("Most money problems are not income problems. They are wisdom problems — "
                "and wisdom is the one asset available to every person, in every season, "
                "regardless of the balance in the account."),
  "intro": ("Financial Wisdom takes seriously a claim Proverbs makes on nearly every "
            "page: there is a way to handle money that leads to life and a way that "
            "leads to ruin, and the difference is not luck or income but wisdom. Most of "
            "us were never taught it — we learned money the way we learned to swim, "
            "thrown in and improvising. <strong>This campaign replaces the improvising "
            "with the time-tested, practical, deeply biblical wisdom that turns good "
            "intentions into good decisions.</strong>"),
  "scripture": ("The plans of the diligent lead to profit as surely as haste leads to "
                "poverty.", "Proverbs 21:5 (NIV)"),
  "bigidea": ("God has not left money to chance or guesswork — the Scriptures are full "
              "of practical wisdom for earning, saving, planning, and giving. The person "
              "who builds financial decisions on God's wisdom builds a life that can "
              "stand."),
  "tags": ["wisdom","Proverbs","planning","diligence","discernment","practical"],
  "subtitles": ["A 40-Day Journey Into the Wisdom of Proverbs and Money",
                "Discovering God's Design for Wise Financial Decisions",
                "A 40-Day Path From Reacting to Planning",
                "Trading Money Stress for the Practical Wisdom of God"],
  "info": {"audience":"All church &amp; workplace — every income and every stage",
           "season":"New Year · Fall · Any season",
           "score":"10/10 — the most requested practical-money topic",
           "related":"Feeds into 40 Days of Financial Wisdom · God Owns It All"},
  "sessions": [
    (("The Two","Ways"), ("The plans of the diligent lead to profit.","Proverbs 21:5"),
     ["wisdom","folly","two ways","diligence","foundations"],
     ["Proverbs is blunt: there is a wise way and a foolish way to handle money. Looking back, where has wisdom served you — and where has folly cost you?",
      "Wisdom is available to everyone, not just the wealthy. What stops you from seeking it for your finances?",
      "What is one area where you have been hasty with money, and what would diligence look like there instead?"],
     ("THIS WEEK'S STEP","Identify the single financial decision you most often make on impulse. This week, build in a **24-hour pause** before that decision. Report back.")),
    (("A Plan You Can","Keep"), ("Won't you first sit down and estimate the cost?","Luke 14:28"),
     ["budgeting","planning","clarity","intentionality","stewardship"],
     ["A budget is just a plan that tells your money where to go before it's gone. What has kept you from making — or keeping — one?",
      "Where does your money actually go each month versus where you wish it went? What does the gap reveal?",
      "What would a plan look like that you could actually keep — simple enough to sustain, honest enough to help?"],
     ("THIS WEEK'S STEP","Build one **simple, one-page plan** for next month's money before the month begins. Keep it visible. Tell your partner one number you're committing to.")),
    (("The Discipline of","Saving"), ("Go to the ant\u2026 it stores its provisions in summer.","Proverbs 6:6\u20138"),
     ["saving","margin","patience","future","discipline"],
     ["The ant saves in summer for a winter it cannot yet see. Where in your finances are you living only for today?",
      "What \u201cwinter\u201d — an emergency, a transition, a season of less — would catch you unprepared right now?",
      "Saving is faith you can measure. What is one small, consistent step toward margin you could start this week?"],
     ("THIS WEEK'S STEP","Set up **one automatic transfer to savings** this week — any amount, however small — and make it consistent. Tell your partner the amount and the day.")),
    (("Getting Free of","Debt"), ("The borrower is slave to the lender.","Proverbs 22:7"),
     ["debt","freedom","courage","plan","perseverance"],
     ["Proverbs calls debt a kind of slavery. Where do you feel that weight most — and how long have you carried it?",
      "What is the real story behind your debt? Naming it honestly is the first step toward freedom.",
      "Freedom from debt is rarely fast, but it is almost always possible. What is one step you could take this week?"],
     ("THIS WEEK'S STEP","List your debts smallest to largest. Choose **one to attack first** and put one extra dollar — or one hundred — toward it this week. Tell your partner your plan.")),
    (("Counsel and","Community"), ("Plans fail for lack of counsel, but with many advisers they succeed.","Proverbs 15:22"),
     ["counsel","community","humility","accountability","wisdom"],
     ["Proverbs ties success to seeking counsel. Who, if anyone, actually knows the truth about your finances?",
      "Why is money the one area we most resist letting others into — and what does that secrecy cost us?",
      "Who is one wise, trustworthy person you could invite into your financial life this season?"],
     ("THIS WEEK'S STEP","Have **one honest conversation** this week with a wise person — a mentor, your spouse, a friend in this group — about a real financial decision. Report what you learned.")),
    (("Wisdom That","Lasts"), ("Whoever walks with the wise becomes wise.","Proverbs 13:20"),
     ["wisdom","legacy","commitment","perseverance","growth"],
     ["What is the single wisest financial change you've made in these forty days?",
      "Where do you still need wisdom most — and where will you go to find it?",
      "Who in this group is walking the same road, and how will you keep walking it together?"],
     ("COMMITMENT STEP","Each person names one wisdom practice to sustain for the next 90 days — a budget, a savings habit, a debt step, a counsel relationship — and names one person who will ask about it. Pray for one another's wisdom and perseverance.")),
  ],
 },
 # ----------------------------------------------------------------- 3
 {
  "title": ("Money Made","Simple"),
  "felt": "TRADING THE NOISE FOR PEACE",
  "deck": ("Complexity is where money stress hides. These forty days clear the clutter — "
           "the accounts, the subscriptions, the comparison — and replace the low hum of "
           "anxiety with the unhurried peace of enough."),
  "pullquote": ("Complexity is where money stress hides. Simplicity is not having less — "
                "it is wanting less, owing less, and finally being able to breathe."),
  "intro": ("Money Made Simple is for everyone who has felt that their finances had become "
            "a tangle they could no longer see the bottom of — too many accounts, too many "
            "subscriptions, too much noise. The Scriptures point to a quieter way: not more "
            "money, but less complication; not bigger, but clearer. <strong>This campaign "
            "clears the clutter over forty days, replacing the low hum of financial anxiety "
            "with the unhurried peace of a life simplified on purpose.</strong>"),
  "scripture": ("But godliness with contentment is great gain\u2026 if we have food and "
                "clothing, we will be content with that.", "1 Timothy 6:6, 8 (NIV)"),
  "bigidea": ("God never designed your financial life to be a source of constant noise and "
              "stress. When you simplify what you owe, owe nothing to comparison, and learn "
              "the freedom of \u201cenough,\u201d money becomes quiet again."),
  "tags": ["simplicity","contentment","clarity","enough","peace","declutter"],
  "subtitles": ["A 40-Day Journey to a Simpler, Calmer Financial Life",
                "Discovering God's Design for Contentment and Simplicity",
                "A 40-Day Path From Financial Clutter to Clarity",
                "Trading the Noise of More for the Peace of Enough"],
  "info": {"audience":"All church &amp; workplace — especially the overwhelmed and over-extended",
           "season":"New Year · Post-holiday · Lent",
           "score":"10/10 — simplicity is the cultural longing of the moment",
           "related":"Feeds into 40 Days of Whole Life Health"},
  "sessions": [
    (("Why It Got So","Complicated"), ("Life does not consist in an abundance of possessions.","Luke 12:15"),
     ["simplicity","possessions","clarity","honesty","beginnings"],
     ["When did your financial life start to feel complicated — and what added the most noise?",
      "Jesus warns that life is not measured by abundance. Where have you quietly believed the opposite?",
      "If your money were simpler, what would you have more of — time, peace, attention, margin?"],
     ("THIS WEEK'S STEP","Make one list this week of **every account, subscription, and recurring payment** you have. Don't change anything yet — just see it clearly.")),
    (("The Freedom of","Enough"), ("If we have food and clothing, we will be content with that.","1 Timothy 6:8"),
     ["contentment","enough","freedom","gratitude","simplicity"],
     ["Paul's bar for contentment is startlingly low. What would it mean to actually believe you have enough?",
      "What is the difference, in your life, between needs and wants — and when did the lines blur?",
      "Where is \u201ca little more\u201d still quietly running the show?"],
     ("THIS WEEK'S STEP","Each day this week, name one thing that is **genuinely enough**. Resist one upgrade or addition you'd normally make. Tell your partner.")),
    (("Cutting the","Clutter"), ("Let us throw off everything that hinders.","Hebrews 12:1"),
     ["declutter","subscriptions","simplify","courage","freedom"],
     ["What is one financial \u201cweight\u201d — a subscription, a payment, a possession — you've kept long after it stopped serving you?",
      "Why is it so hard to let go, even of things that drain us?",
      "What would you do with the margin if you cleared even three small things this week?"],
     ("THIS WEEK'S STEP","**Cancel or eliminate three recurring expenses** you no longer need. Add up what you saved and tell your partner.")),
    (("One Simple","System"), ("Let your \u2018Yes\u2019 be \u2018Yes,\u2019 and your \u2018No,\u2019 \u2018No.\u2019","Matthew 5:37"),
     ["clarity","system","simplicity","intentionality","peace"],
     ["Complexity multiplies decisions; simplicity reduces them. Where do you make the same money decision over and over?",
      "What would one simple, repeatable system — for spending, giving, saving — do for your peace of mind?",
      "What's one rule you could set once so you don't have to re-decide every time?"],
     ("THIS WEEK'S STEP","Create **one simple money rule** you can automate or repeat — a spending limit, a giving percentage, a \u201cno\u201d set in advance. Tell your partner your rule.")),
    (("Generous and","Light"), ("Freely you have received; freely give.","Matthew 10:8"),
     ["generosity","open hands","lightness","giving","simplicity"],
     ["Simplicity and generosity travel together — both loosen money's grip. Which comes harder for you, and why?",
      "What would it feel like to give something away simply because you can?",
      "Where might holding more loosely actually make you lighter?"],
     ("THIS WEEK'S STEP","Give one thing away this week — money, time, or a possession — **with no strings attached**. Notice how it feels. Tell your partner.")),
    (("A Quieter","Life"), ("Make it your ambition to lead a quiet life.","1 Thessalonians 4:11"),
     ["simplicity","peace","commitment","rhythm","contentment"],
     ["What is the simplest your financial life has felt in years — and what made the difference?",
      "Which simplification do you most want to keep?",
      "Who will help you resist the slow creep of complication?"],
     ("COMMITMENT STEP","Each person names one simplicity practice to keep for the next 90 days and one person who will check in. Close by thanking God for \u201cenough\u201d and praying for quiet, unhurried financial peace.")),
  ],
 },
 # ----------------------------------------------------------------- 4
 {
  "title": ("Financial","Peace"),
  "felt": "FROM MONEY ANXIETY TO REST",
  "deck": ("Money worry is one of the most common forms of anxiety there is — and peace "
           "was never something money could buy. These forty days relocate financial "
           "peace to its only reliable home: the character of God."),
  "pullquote": ("Financial peace is not the absence of money problems. It is the presence "
                "of a trust deep enough that the problems no longer run your heart."),
  "intro": ("Financial Peace is for the millions who lie awake doing math in the dark. "
            "Money worry touches the wealthy and the struggling alike, because peace was "
            "never something money could buy. Jesus spoke directly to the worried — telling "
            "them to look at the birds and the lilies, not to dismiss their needs but to "
            "relocate their trust. <strong>Over forty days, this campaign moves financial "
            "peace out of the bank account and into its only reliable home: the character "
            "of a God who already knows what you need.</strong>"),
  "scripture": ("Do not be anxious about anything, but in every situation, by prayer and "
                "petition, with thanksgiving, present your requests to God.","Philippians 4:6 (NIV)"),
  "bigidea": ("Money worry is not solved by more money — it is solved by deeper trust. The "
              "peace of God is available to the person who learns to bring every financial "
              "fear to Him before doing anything else with it."),
  "tags": ["peace","anxiety","worry","trust","rest","provision"],
  "subtitles": ["A 40-Day Journey From Money Anxiety to Lasting Peace",
                "Discovering God's Design for a Worry-Free Financial Life",
                "A 40-Day Path From Lying Awake to Resting in Trust",
                "Trading the Weight of Worry for the Peace of God"],
  "info": {"audience":"All church &amp; workplace — anyone carrying money stress",
           "season":"January · Lent · Any season",
           "score":"10/10 — anxiety is the defining felt-need of the era",
           "related":"Feeds into 40 Days of Whole Life Health · Finding Peace"},
  "sessions": [
    (("The Weight We","Carry"), ("Do not be anxious about anything.","Philippians 4:6"),
     ["anxiety","worry","honesty","the heart","peace"],
     ["Where does money worry show up in your body, your sleep, your relationships? Be specific.",
      "What is the financial fear you carry most often — and how long have you carried it?",
      "Paul says \u201cdo not be anxious about anything.\u201d Does that feel like comfort or pressure to you, and why?"],
     ("THIS WEEK'S STEP","Each night this week, write down the money worry on your mind and **pray it over to God before sleep**. Tell your partner what you notice.")),
    (("Look at the","Birds"), ("Look at the birds of the air\u2026 your heavenly Father feeds them.","Matthew 6:26"),
     ["provision","trust","worry","the Father","peace"],
     ["Jesus points to birds and lilies as evidence of a Father who provides. When have you actually seen God provide for you?",
      "What does worry assume about God that the birds quietly disprove?",
      "Where do you most need to trade anxiety for trust this week?"],
     ("THIS WEEK'S STEP","Keep a short **provision list** this week — every place, big or small, you see God provide. Read it to your partner at week's end.")),
    (("Naming the","Fear"), ("Cast all your anxiety on him because he cares for you.","1 Peter 5:7"),
     ["fear","honesty","casting","prayer","care"],
     ["Unnamed fear grows in the dark. What is the specific financial fear underneath your general money stress?",
      "Peter says to \u201ccast\u201d anxiety — to throw it, not carry it. What makes that so hard to actually do?",
      "What would change if you truly believed God cares about your specific financial situation?"],
     ("THIS WEEK'S STEP","**Name your biggest financial fear out loud** to God and to your partner this week. Speaking it is the first step to casting it.")),
    (("Peace That","Guards"), ("And the peace of God\u2026 will guard your hearts and your minds.","Philippians 4:7"),
     ["peace","prayer","thanksgiving","guarding","the mind"],
     ["Paul ties peace to a practice: prayer plus thanksgiving. Which of those is missing when you're most anxious?",
      "What does it mean that God's peace \u201cguards\u201d you — like a sentry at the door of your heart?",
      "Where do you need that guard most this season?"],
     ("THIS WEEK'S STEP","Practice the Philippians 4 pattern daily: **name the worry, pray it specifically, add thanksgiving**. Tell your partner what shifts.")),
    (("The Gift of","Margin"), ("Come to me, all you who are weary and burdened, and I will give you rest.","Matthew 11:28"),
     ["rest","margin","Sabbath","relief","peace"],
     ["Sometimes peace requires practical change, not just prayer. Where has the absence of margin made worry inevitable?",
      "What is one small step toward financial margin that would let you breathe easier?",
      "How are spiritual rest and financial margin connected in your life?"],
     ("THIS WEEK'S STEP","Take **one practical step toward margin** this week — a small saving, a cut expense, a hard conversation. Pair it with prayer. Report back.")),
    (("Resting in","Trust"), ("I have learned to be content whatever the circumstances.","Philippians 4:11"),
     ["contentment","trust","peace","commitment","rest"],
     ["Where do you have more peace about money than you did forty days ago?",
      "What practice most helped you trade worry for trust?",
      "Who will help you guard that peace when the worry returns — and it will?"],
     ("COMMITMENT STEP","Each person names one peace practice — a nightly prayer, a provision list, a margin step — to sustain for 90 days, and one person who will check in. Close by praying Philippians 4:6\u20137 over each other.")),
  ],
 },
 # ----------------------------------------------------------------- 5
 {
  "title": ("Wise with","Money"),
  "felt": "BUILDING REAL FINANCIAL COMPETENCE",
  "deck": ("There are really only five things you can do with a dollar — earn it, give "
           "it, save it, invest it, and owe it. These forty days build genuine "
           "competence in all five, so that skill becomes a form of faithfulness."),
  "pullquote": ("God is not waiting for you to have more money before He trusts you with "
                "it. He is watching what you do with what is already in your hand."),
  "intro": ("Wise with Money is the practical, sleeves-rolled-up campaign for anyone who "
            "wants to handle money skillfully — not just spiritually, but competently. "
            "Jesus told a startling parable suggesting that how we handle worldly wealth "
            "is a test of whether we can be trusted with greater things. <strong>Built "
            "around the truth that there are only five things you can do with a dollar — "
            "earn, give, save, invest, and owe — this campaign builds genuine competence "
            "over forty days, so that being wise with money becomes faithfulness.</strong>"),
  "scripture": ("So if you have not been trustworthy in handling worldly wealth, who will "
                "trust you with true riches?", "Luke 16:11 (NIV)"),
  "bigidea": ("Faithfulness with money is a skill God watches closely. The person who "
              "learns to earn, give, save, invest, and owe wisely is being trained for "
              "far more than money."),
  "tags": ["stewardship","faithfulness","skill","the five uses","trustworthy","competence"],
  "subtitles": ["A 40-Day Journey to Handling Money Skillfully and Faithfully",
                "Discovering God's Design for Wise Stewardship",
                "A 40-Day Path From Drifting to Stewarding",
                "Becoming Trustworthy With What's Already in Your Hand"],
  "info": {"audience":"All church &amp; workplace — practical for every income level",
           "season":"Fall · New Year · Any season",
           "score":"10/10 — the competence every adult quietly wants",
           "related":"Feeds into God Owns It All · 40 Days of Financial Wisdom"},
  "sessions": [
    (("Trusted With","Little"), ("Whoever can be trusted with very little can also be trusted with much.","Luke 16:10"),
     ["faithfulness","trustworthy","stewardship","beginnings","character"],
     ["Jesus links small faithfulness to large trust. Where have you been waiting for \u201cmore\u201d before you get serious?",
      "What does the way you handle today's money reveal about your readiness for tomorrow's?",
      "What is one small area where God is asking you to be trustworthy right now?"],
     ("THIS WEEK'S STEP","Pick the one area of your finances you've been ignoring and **give it honest attention** this week. Tell your partner what you found.")),
    (("Earning With","Integrity"), ("Whatever you do, work at it with all your heart, as working for the Lord.","Colossians 3:23"),
     ["work","earning","integrity","vocation","excellence"],
     ["Earning is the first use of money — and it's an act of worship. How does your faith shape the way you work and earn?",
      "Where are you tempted to cut corners or compromise to earn more?",
      "What would it mean to see your work itself as a calling, not just a paycheck?"],
     ("THIS WEEK'S STEP","Do your work **as if for the Lord** in one specific way you've been neglecting — excellence, honesty, diligence. Report back.")),
    (("Giving","First"), ("Honor the Lord with your wealth, with the firstfruits of all your crops.","Proverbs 3:9"),
     ["giving","firstfruits","generosity","priority","worship"],
     ["\u201cFirstfruits\u201d means giving first, not last. What does the order of your giving reveal about its priority?",
      "What fears come up when you imagine giving before everything else is covered?",
      "What would change if generosity were the first line of your budget, not the leftover?"],
     ("THIS WEEK'S STEP","**Give first** this week — before other spending — even a small amount. Notice what it does to your heart. Tell your partner.")),
    (("Saving and","Investing"), ("You should have put my money on deposit\u2026 so that I would have received it back with interest.","Matthew 25:27"),
     ["saving","investing","future","patience","stewardship"],
     ["In the parable of the talents, the servant who buried his is the one rebuked. Where are you \u201cburying\u201d rather than stewarding?",
      "Saving and investing are patience made practical. Where do you lack patience with money?",
      "What is one wise, simple step toward saving or investing for the future you could take this season?"],
     ("THIS WEEK'S STEP","Take **one concrete step** toward saving or investing this week — open an account, set a transfer, learn one thing. Tell your partner.")),
    (("Owing","Wisely"), ("Let no debt remain outstanding, except the continuing debt to love one another.","Romans 13:8"),
     ["debt","owing","freedom","wisdom","plan"],
     ["The fifth use of money is owing — and Scripture treats it soberly. What's your honest relationship with debt?",
      "Where has owing limited your freedom to give, save, or live generously?",
      "What is one wise step toward owing less — or owing more carefully — this season?"],
     ("THIS WEEK'S STEP","Make **one move** this week toward handling debt more wisely — a payment plan, an extra payment, a hard \u201cno.\u201d Report back to your partner.")),
    (("Faithful in All","Five"), ("Well done, good and faithful servant!","Matthew 25:21"),
     ["faithfulness","stewardship","commitment","growth","legacy"],
     ["Across earning, giving, saving, investing, and owing — which use of money are you most faithful with, and which needs the most growth?",
      "What has it done for your faith to handle money as a steward these forty days?",
      "Who will keep training alongside you?"],
     ("COMMITMENT STEP","Each person names the one of the five uses they most need to grow in, sets a 90-day step, and names a partner who will follow up. Pray for one another to hear \u201cwell done.\u201d")),
  ],
 },
 # ----------------------------------------------------------------- 6
 {
  "title": ("God, Money &amp;","Me"),
  "felt": "HEALING THE HEART BEHIND THE HABITS",
  "deck": ("Long before money is a math problem, it is a heart problem — shaped by your "
           "home, your fears, and your history. These forty days trace the wire, so God "
           "can rewrite the parts that have been holding you captive."),
  "pullquote": ("There is a money story running inside you right now — written by your "
                "family, your fears, and your history. Until you read it honestly, it "
                "will keep writing your future."),
  "intro": ("God, Money &amp; Me is the most personal of the campaigns, because it turns the "
            "lens inward. Long before money is a math problem, it is a heart problem — "
            "shaped by the home you grew up in, the messages you absorbed, and the "
            "identity you've quietly tried to build with it. Jesus said your treasure and "
            "your heart are tied together. <strong>This campaign helps you trace the wire "
            "— to uncover your real money story, bring it honestly to God, and let Him "
            "rewrite the parts that have held you captive.</strong>"),
  "scripture": ("For where your treasure is, there your heart will be also.","Luke 12:34 (NIV)"),
  "bigidea": ("Your relationship with money is more personal than practical — rooted in "
              "your heart, your history, and your identity. When you let God into that "
              "story, the way you handle money begins to change from the inside out."),
  "tags": ["the heart","identity","money story","healing","honesty","transformation"],
  "subtitles": ["A 40-Day Journey Into Your Heart, Your History, and Your Money",
                "Discovering God's Design for Your Relationship With Money",
                "A 40-Day Path From Your Old Money Story to a New One",
                "Letting God Heal the Way You See Money — and Yourself"],
  "info": {"audience":"All church &amp; workplace — deeply personal, universally relevant",
           "season":"Lent · New Year · Any season",
           "score":"10/10 — the heart-level work no budget can do",
           "related":"Feeds into 40 Days of Purpose · Whole Person Health"},
  "sessions": [
    (("Your Money","Story"), ("For where your treasure is, there your heart will be also.","Luke 12:34"),
     ["the heart","story","history","honesty","beginnings"],
     ["What did you learn about money — spoken or unspoken — in the home you grew up in?",
      "Jesus ties treasure to heart. What does the way you handle money reveal about what your heart is set on?",
      "What is one money belief you've carried for years that you've never actually examined?"],
     ("THIS WEEK'S STEP","Write a short, honest paragraph this week titled **\u201cMy Money Story.\u201d** Bring it to God in prayer and share one line with your partner.")),
    (("The Fear","Underneath"), ("There is no fear in love. But perfect love drives out fear.","1 John 4:18"),
     ["fear","scarcity","the heart","love","freedom"],
     ["Much money behavior is fear in disguise — fear of lack, of failure, of not being enough. Which fear drives you most?",
      "Where did that fear first take root in your story?",
      "What would it mean to let God's love, rather than fear, set the terms?"],
     ("THIS WEEK'S STEP","**Name the fear** under your money habits and bring it to God daily this week. Tell your partner what you discover.")),
    (("Identity and Net","Worth"), ("Life does not consist in an abundance of possessions.","Luke 12:15"),
     ["identity","worth","comparison","the heart","freedom"],
     ["Where have you let your bank balance — high or low — become a verdict on your worth?",
      "Whose approval are you trying to earn or keep with money?",
      "What would change if your identity were settled in God rather than in your finances?"],
     ("THIS WEEK'S STEP","Each day, preach one truth to yourself: **\u201cMy worth is not my net worth.\u201d** Notice where you most need to believe it. Tell your partner.")),
    (("Money and the People I","Love"), ("Keep your lives free from the love of money.","Hebrews 13:5"),
     ["relationships","marriage","honesty","the heart","peace"],
     ["Money is one of the most common sources of conflict between people. Where does it create tension in your closest relationships?",
      "What money patterns from your past are you repeating with the people you love?",
      "What honest conversation about money have you been avoiding?"],
     ("THIS WEEK'S STEP","Have **one honest, gracious money conversation** this week with someone close to you. Report back to your partner.")),
    (("Healing and","Honesty"), ("Then you will know the truth, and the truth will set you free.","John 8:32"),
     ["healing","honesty","confession","grace","freedom"],
     ["What is the thing about your finances you most hope no one ever finds out — and what does hiding it cost you?",
      "Where do you need grace, not just a budget?",
      "What would it feel like to bring the whole truth into the light, with God and with someone safe?"],
     ("THIS WEEK'S STEP","Bring **one hidden financial truth into the light** this week — confessed to God and shared with a trusted person. Report on the freedom of it.")),
    (("A New","Story"), ("The old has gone, the new is here!","2 Corinthians 5:17"),
     ["transformation","identity","commitment","hope","the heart"],
     ["How has your money story begun to change over these forty days?",
      "What old belief or pattern are you ready to leave behind for good?",
      "Who will help you live the new story when the old one tries to reassert itself?"],
     ("COMMITMENT STEP","Each person names one heart-level money pattern they're committing to change over the next 90 days, and one person who will walk with them. Close by thanking God that He makes all things new — including our relationship with money.")),
  ],
 },
 # ----------------------------------------------------------------- 7
 {
  "title": ("Financial","Health"),
  "felt": "RHYTHMS THAT LAST A LIFETIME",
  "deck": ("Financial health is not a number you hit once. Like physical health, it is "
           "built by quiet, repeatable habits — and these forty days assess where you "
           "really are and build rhythms a whole life can stand on."),
  "pullquote": ("Financial health is not a number you hit once. It is a set of quiet, "
                "repeatable habits — the kind that, practiced for a decade, build a life "
                "that can stand."),
  "intro": ("Financial Health treats your finances the way a good doctor treats your body: "
            "not with shame, but with an honest checkup and a sustainable plan. Just as "
            "physical health is built by ordinary habits repeated over time, financial "
            "health comes not from a windfall or a perfect month but from rhythms you can "
            "actually sustain. <strong>Over forty days, this campaign helps you assess "
            "where you really are, build habits that hold, and move toward steady, "
            "whole-life financial wellness.</strong>"),
  "scripture": ("Dear friend, I pray that you may enjoy good health and that all may go "
                "well with you, even as your soul is getting along well.","3 John 1:2 (NIV)"),
  "bigidea": ("Financial health is built the same way physical health is — through honest "
              "assessment and sustainable habits repeated over time. God designed your "
              "financial life to run on steady rhythms, not anxious extremes."),
  "tags": ["health","habits","rhythms","sustainability","wellness","stewardship"],
  "subtitles": ["A 40-Day Journey to Sustainable Financial Wellness",
                "Discovering God's Design for Healthy Financial Habits",
                "A 40-Day Path From Crisis to Steady Rhythms",
                "Building the Money Habits a Whole Life Can Stand On"],
  "info": {"audience":"All church &amp; workplace — pairs naturally with whole-life health",
           "season":"January · New Year · Any season",
           "score":"10/10 — health framing lowers shame and raises buy-in",
           "related":"Feeds into 40 Days of Whole Life Health"},
  "sessions": [
    (("The Honest","Checkup"), ("I pray\u2026 that all may go well with you.","3 John 1:2"),
     ["assessment","honesty","health","beginnings","courage"],
     ["A checkup only helps if it's honest. How would you actually rate your financial health right now, and why?",
      "What's the one \u201csymptom\u201d — stress, debt, no margin, no plan — you most want to address?",
      "What have you been afraid the checkup might reveal?"],
     ("THIS WEEK'S STEP","Give yourself an **honest one-page financial checkup** this week — what's well, what's not. No shame, just truth. Bring it to God.")),
    (("Habits, Not","Heroics"), ("Train yourself to be godly.","1 Timothy 4:7"),
     ["habits","discipline","rhythms","training","sustainability"],
     ["Health comes from habits, not heroics. Which money behaviors do you do consistently — and which only in crisis?",
      "What unhealthy financial habit has quietly become automatic for you?",
      "What is one small, repeatable habit that would most improve your financial health?"],
     ("THIS WEEK'S STEP","Choose **one small financial habit** to practice this week — checking your balance, logging spending, a set transfer. Keep it tiny enough to keep. Report back.")),
    (("Room to","Breathe"), ("He leads me beside quiet waters, he refreshes my soul.","Psalm 23:2\u20133"),
     ["margin","rest","breathing room","peace","health"],
     ["Living with no financial margin is like living with no breath — eventually something gives. Where are you running on empty?",
      "What would even a small cushion change about how you experience daily life?",
      "What's one step toward margin you could take this week?"],
     ("THIS WEEK'S STEP","Create or grow **one small buffer** this week — a starter emergency fund, a cut expense. Tell your partner the number and the plan.")),
    (("Treating the","Debt"), ("The borrower is slave to the lender.","Proverbs 22:7"),
     ["debt","healing","plan","perseverance","freedom"],
     ["Debt is one of the most common drains on financial health. Where is it costing you the most — in money or in peace?",
      "What's kept you from facing it head-on?",
      "What is the next single step in a realistic, sustainable plan to get free?"],
     ("THIS WEEK'S STEP","Make **one sustainable move** against debt this week — a plan, an extra payment, a consolidation conversation. Tell your partner.")),
    (("Generosity Is","Healthy"), ("A generous person will prosper; whoever refreshes others will be refreshed.","Proverbs 11:25"),
     ["generosity","giving","health","joy","freedom"],
     ["Scripture ties generosity to flourishing. How does giving — or not giving — affect your sense of financial health?",
      "Where has a tight grip on money quietly made you anxious rather than secure?",
      "What is one healthy, joyful act of generosity you could practice this week?"],
     ("THIS WEEK'S STEP","Build **one regular, sustainable giving habit** this week — a set amount or percentage you can keep. Tell your partner.")),
    (("A Life That Can","Stand"), ("Like a man building a house, who dug down deep and laid the foundation on rock.","Luke 6:48"),
     ["foundations","habits","commitment","sustainability","legacy"],
     ["Which new financial habit most improved your health these forty days?",
      "What rhythm do you most want to make permanent?",
      "Who will help you keep it when life gets hard — and it will?"],
     ("COMMITMENT STEP","Each person names one financial-health habit to sustain for the next 90 days and one person who will check in. Pray for steady, whole-life health for one another.")),
  ],
 },
 # ----------------------------------------------------------------- 8
 {
  "title": ("Breaking Financial","Fear"),
  "felt": "COURAGE TO FACE WHAT YOU'VE AVOIDED",
  "deck": ("Fear keeps the envelopes unopened and the conversations unhad. These forty "
           "days help you face what you've been avoiding, replace shame with grace, and "
           "take the small brave steps that break fear's grip."),
  "pullquote": ("Fear keeps the envelopes unopened, the conversations unhad, and the "
                "truth unfaced. Freedom begins the moment you open the envelope anyway."),
  "intro": ("Breaking Financial Fear is for everyone whose relationship with money is "
            "governed not by greed but by dread — the unopened mail, the avoided "
            "statement, the conversation perpetually postponed, the low-grade shame that "
            "says you should have this figured out by now. Fear is not a character flaw; "
            "it's a captor. <strong>And Scripture is emphatic that God did not give us a "
            "spirit of fear. Over forty days, this campaign helps you face what you've "
            "avoided and take the small, courageous steps that break fear's grip.</strong>"),
  "scripture": ("For the Spirit God gave us does not make us timid, but gives us power, "
                "love and self-discipline.","2 Timothy 1:7 (NIV)"),
  "bigidea": ("God did not give you a spirit of fear about money — He gives power, love, "
              "and a sound mind. Facing what you've avoided, in His strength and good "
              "company, is how fear finally loses its grip."),
  "tags": ["fear","courage","shame","avoidance","freedom","trust"],
  "subtitles": ["A 40-Day Journey From Money Fear to Courageous Freedom",
                "Discovering God's Design for Facing Finances Without Fear",
                "A 40-Day Path From Avoidance to Courage",
                "Opening the Envelope: Breaking Fear's Grip on Your Money"],
  "info": {"audience":"All church &amp; workplace — for the avoiders and the overwhelmed",
           "season":"New Year · Lent · Any season",
           "score":"10/10 — names a struggle most people hide",
           "related":"Feeds into Finding Peace · 40 Days of Whole Life Health"},
  "sessions": [
    (("What We're","Avoiding"), ("For God has not given us a spirit of fear.","2 Timothy 1:7"),
     ["fear","avoidance","honesty","courage","beginnings"],
     ["What financial thing — a statement, a debt, a conversation — have you been avoiding, and for how long?",
      "What do you imagine will happen if you finally face it? Is that fear telling you the truth?",
      "2 Timothy says fear isn't from God. What would it mean to refuse it just for today?"],
     ("THIS WEEK'S STEP","Open the one thing you've been avoiding this week — the statement, the bill, the number. **Just open it.** Tell your partner you did.")),
    (("Where the Fear Comes","From"), ("When I am afraid, I put my trust in you.","Psalm 56:3"),
     ["fear","roots","trust","honesty","healing"],
     ["Where did your financial fear first take root — a hard season, a family pattern, a failure?",
      "What does your fear assume about the future, and about God?",
      "The psalmist doesn't deny fear — he redirects it. What would it look like to put your trust in God in your most fearful money moment?"],
     ("THIS WEEK'S STEP","When financial fear rises this week, pray Psalm 56:3 in the moment: **\u201cWhen I am afraid, I put my trust in you.\u201d** Tell your partner what shifts.")),
    (("Trading Shame for","Grace"), ("Therefore, there is now no condemnation for those who are in Christ Jesus.","Romans 8:1"),
     ["shame","grace","freedom","honesty","identity"],
     ["Financial shame whispers that your mistakes define you. Where have you believed that?",
      "What's the difference between conviction that leads to change and shame that leads to hiding?",
      "What would it free you to do if you truly believed there's no condemnation for you?"],
     ("THIS WEEK'S STEP","Name **one financial regret** to God this week and receive His grace over it. Then take one forward step instead of hiding. Report back.")),
    (("One Brave","Step"), ("Have I not commanded you? Be strong and courageous.","Joshua 1:9"),
     ["courage","action","freedom","faith","perseverance"],
     ["Courage isn't the absence of fear; it's action in spite of it. What's one brave financial step you've been postponing?",
      "What's the smallest version of that step you could take this week?",
      "Who could go with you so you don't have to be brave alone?"],
     ("THIS WEEK'S STEP","Take **one courageous financial step** this week — make the call, start the plan, ask for help. Tell your partner before and after.")),
    (("Out of the","Dark"), ("If we walk in the light\u2026 we have fellowship with one another.","1 John 1:7"),
     ["community","light","honesty","courage","freedom"],
     ["Fear thrives in secrecy. Who actually knows the truth about your finances?",
      "What's the risk — and the relief — of letting someone safe into the real picture?",
      "Who is one trustworthy person you could bring into the light this week?"],
     ("THIS WEEK'S STEP","Tell one safe person **one true thing** about your finances this week. Notice how fear shrinks in the light. Report back.")),
    (("Free and","Unafraid"), ("So if the Son sets you free, you will be free indeed.","John 8:36"),
     ["freedom","courage","commitment","hope","perseverance"],
     ["Where are you less afraid of money than you were forty days ago?",
      "What's the next brave step on the road out of fear?",
      "Who will keep walking it with you?"],
     ("COMMITMENT STEP","Each person names one courageous financial step for the next 90 days and one person who will walk with them. Close by declaring 2 Timothy 1:7 over each other and praying for freedom from fear.")),
  ],
 },
 # ----------------------------------------------------------------- 9
 {
  "title": ("Money and","Meaning"),
  "felt": "FROM SUCCESS TO SIGNIFICANCE",
  "deck": ("You can't take it with you — but Jesus said you can send it ahead. These "
           "forty days reconnect your money to your meaning, so that even ordinary "
           "dollars serve what lasts."),
  "pullquote": ("You can't take it with you — but Jesus said you can send it ahead. The "
                "question money keeps asking is not how much, but what for."),
  "intro": ("Money and Meaning is for the person who has begun to sense that financial "
            "success, by itself, rings a little hollow — and who wants their money to "
            "mean something. Jesus made a stunning promise: that we can convert temporary "
            "wealth into permanent treasure, sending it ahead into eternity through "
            "generosity and good. <strong>This is not about guilt; it's about purpose. "
            "Over forty days, this campaign reconnects your money to your meaning — and "
            "to the deep joy of a life where what you have serves what you're here "
            "for.</strong>"),
  "scripture": ("But store up for yourselves treasures in heaven, where moths and vermin "
                "do not destroy, and where thieves do not break in and steal.","Matthew 6:20 (NIV)"),
  "bigidea": ("Money is a tool, not a trophy — and its deepest purpose is to serve what "
              "lasts. When you connect your finances to your God-given purpose, even "
              "ordinary dollars take on eternal meaning."),
  "tags": ["meaning","generosity","purpose","eternity","significance","joy"],
  "subtitles": ["A 40-Day Journey From Financial Success to Lasting Significance",
                "Discovering God's Design for Money With Meaning",
                "A 40-Day Path From Accumulating to Investing in What Lasts",
                "Sending It Ahead: Connecting Your Money to Your Purpose"],
  "info": {"audience":"All church &amp; workplace — especially mid-life and second-half adults",
           "season":"Year-end giving · Fall · Any season",
           "score":"10/10 — converts success into generosity and joy",
           "related":"Feeds into 40 Days of Purpose · God Owns It All"},
  "sessions": [
    (("Is This All There","Is?"), ("Whoever loves money never has enough.","Ecclesiastes 5:10"),
     ["meaning","contentment","purpose","honesty","beginnings"],
     ["Ecclesiastes says the love of money is a thirst that never satisfies. Where have you felt that emptiness even when things went well?",
      "What were you taught money would deliver that it never quite did?",
      "If money is a means, what's the end it's meant to serve in your life?"],
     ("THIS WEEK'S STEP","Write one honest sentence this week finishing: **\u201cI want my money to mean ___.\u201d** Bring it to God and share it with your partner.")),
    (("Treasure That","Lasts"), ("Store up for yourselves treasures in heaven.","Matthew 6:20"),
     ["eternity","treasure","generosity","perspective","purpose"],
     ["Jesus says we can \u201csend treasure ahead.\u201d What do you think He means, and do you believe it?",
      "Where are you storing up treasure that won't last — and where could you redirect some of it?",
      "What would shift if you measured wealth by what you give, not what you keep?"],
     ("THIS WEEK'S STEP","Make **one eternal investment** this week — a gift toward something that will outlast you. Tell your partner what and why.")),
    (("Generosity on","Purpose"), ("Each of you should give what you have decided in your heart to give.","2 Corinthians 9:7"),
     ["generosity","intentionality","giving","joy","purpose"],
     ["Paul describes giving that's decided, not accidental. Is your generosity intentional or leftover?",
      "What cause, person, or need has God put on your heart that your money could serve?",
      "What would it look like to give on purpose this season, not just on impulse?"],
     ("THIS WEEK'S STEP","Choose **one cause to give to on purpose** this week — decided in advance, given with joy. Tell your partner your decision.")),
    (("Rich Toward","God"), ("This is how it will be with whoever stores up things for themselves but is not rich toward God.","Luke 12:21"),
     ["priorities","the heart","generosity","purpose","freedom"],
     ["Jesus warns against being rich toward self but poor toward God. What does \u201crich toward God\u201d look like in practice?",
      "Where are you building bigger barns — and what is that costing your soul?",
      "What would being rich toward God change about your financial priorities?"],
     ("THIS WEEK'S STEP","Identify one way you've been \u201cbuilding barns\u201d and take **one step toward being rich toward God** instead. Report back.")),
    (("Money for","Good"), ("Command them\u2026 to be rich in good deeds, and to be generous and willing to share.","1 Timothy 6:18"),
     ["good works","generosity","contribution","purpose","joy"],
     ["Money can do real good in the world. Where could yours make a tangible difference right now?",
      "What's the most meaningful thing your money has ever done — and how did it feel?",
      "Where is God inviting you to be \u201crich in good deeds\u201d with what you have?"],
     ("THIS WEEK'S STEP","Use money to do **one concrete good** this week — meet a need, bless a person, fund a cause. Tell your partner the story.")),
    (("A Life of","Significance"), ("Well done, good and faithful servant!","Matthew 25:21"),
     ["significance","legacy","commitment","purpose","joy"],
     ["How has the meaning of your money changed over these forty days?",
      "What is the one purpose you most want your finances to serve from here on?",
      "Who will help you stay connected to that purpose?"],
     ("COMMITMENT STEP","Each person names one money-and-meaning commitment — a giving target, a cause, a legacy step — for the next 90 days, and one person who will follow up. Close by praying that your finances would serve what lasts.")),
  ],
 },
 # ----------------------------------------------------------------- 10
 {
  "title": ("Peace with","Money"),
  "felt": "ENDING THE WAR FOR GOOD",
  "deck": ("For many of us, money has been an enemy for so long we've forgotten peace was "
           "ever an option. These forty days help you lay the weapon down — making peace "
           "with your past, your present, and your provision."),
  "pullquote": ("For many of us, money has been an enemy for so long we've forgotten "
                "peace was ever an option. It is. You can lay the weapon down."),
  "intro": ("Peace with Money is the campaign for everyone who has been at war with their "
            "finances — striving, dreading, resenting, or fleeing money for so long they "
            "can't remember what peace would feel like. The good news running through "
            "Scripture is that the conflict can end — not because the numbers suddenly "
            "cooperate, but because contentment is rooted in a promise deeper than any "
            "balance. <strong>Over forty days, this campaign helps you make peace with "
            "your past, present, and provision, and finally rest in a security no money "
            "could buy.</strong>"),
  "scripture": ("Keep your lives free from the love of money and be content with what you "
                "have, because God has said, \u201cNever will I leave you nor forsake "
                "you.\u201d","Hebrews 13:5 (NIV)"),
  "bigidea": ("You don't have to be at war with money — or with yourself about it. Lasting "
              "peace comes not from winning the financial battle but from resting in a "
              "God who promises never to leave you."),
  "tags": ["peace","contentment","rest","healing","reconciliation","security"],
  "subtitles": ["A 40-Day Journey From War With Money to Peace With It",
                "Discovering God's Design for Contentment and Rest",
                "A 40-Day Path From Striving to Resting",
                "Laying Down the Weapon: Making Peace With Your Money"],
  "info": {"audience":"All church &amp; workplace — the capstone of the collection",
           "season":"New Year · Lent · Any season",
           "score":"10/10 — the rest every other campaign points toward",
           "related":"Feeds into Finding Peace · 40 Days of Whole Life Health"},
  "sessions": [
    (("The War We've Been","Fighting"), ("Be content with what you have.","Hebrews 13:5"),
     ["peace","contentment","honesty","the heart","beginnings"],
     ["In what way has money been an enemy, a stressor, or a source of striving in your life?",
      "How long have you been at war with your finances — and what has the fighting cost you?",
      "What would peace with money even look like for you?"],
     ("THIS WEEK'S STEP","Name the way you've been \u201cat war\u201d with money this week, and bring it honestly to God. Tell your partner **one thing you long for peace about**.")),
    (("The Promise","Underneath"), ("God has said, \u201cNever will I leave you nor forsake you.\u201d","Hebrews 13:5"),
     ["security","trust","the promise","peace","rest"],
     ["Hebrews roots contentment in a promise, not a paycheck. Where have you looked to money for the security only God can give?",
      "What does it do to your anxiety to hear \u201cI will never leave you\u201d?",
      "Where do you most need to trust that promise this season?"],
     ("THIS WEEK'S STEP","Each day this week, when money worry rises, say the promise out loud: **\u201cGod will never leave me.\u201d** Notice what changes. Tell your partner.")),
    (("Making Peace With the","Past"), ("Forgetting what is behind and straining toward what is ahead.","Philippians 3:13"),
     ["healing","past","grace","peace","freedom"],
     ["What financial regret, failure, or wound from the past still haunts your relationship with money?",
      "What would it take to forgive yourself — or someone else — for a money mistake?",
      "How is the past keeping you from peace in the present?"],
     ("THIS WEEK'S STEP","Bring **one financial regret** to God this week and ask for grace to release it. Take one step \u201cstraining toward what is ahead.\u201d Report back.")),
    (("Enough for","Today"), ("Give us today our daily bread.","Matthew 6:11"),
     ["provision","today","contentment","rest","trust"],
     ["Jesus teaches us to ask for daily bread — not a year's supply. Where do you struggle to trust God for just today?",
      "How does worrying about tomorrow steal your peace today?",
      "What would change if you trusted God for enough, one day at a time?"],
     ("THIS WEEK'S STEP","Practice **daily-bread trust** this week — focus on today's provision and gratitude, and hand tomorrow to God each morning. Tell your partner.")),
    (("Contentment as a","Practice"), ("I have learned to be content whatever the circumstances.","Philippians 4:11"),
     ["contentment","practice","gratitude","peace","rest"],
     ["Paul says he \u201clearned\u201d contentment — it's a practice, not a personality. Where are you in that learning?",
      "What pulls you out of contentment fastest — comparison, fear, desire?",
      "What practice helps you return to peace when contentment slips?"],
     ("THIS WEEK'S STEP","Practice contentment daily this week through gratitude — **name what's enough before you notice what's missing**. Tell your partner what you learn.")),
    (("Resting in","Peace"), ("Come to me, all you who are weary and burdened, and I will give you rest.","Matthew 11:28"),
     ["rest","peace","commitment","contentment","hope"],
     ["Where do you have more peace with money than you did forty days ago?",
      "What practice most helped you lay down the war?",
      "Who will help you keep the peace when the old conflict tries to return?"],
     ("COMMITMENT STEP","Each person names one peace-with-money practice — a gratitude rhythm, a daily-bread prayer, a released regret — to sustain for 90 days, and one person who will check in. Close by resting together in Matthew 11:28 and praying for lasting peace.")),
  ],
 },
]

# Deep tone, light tint, and a one-word mood per volume (index-aligned to VOLUMES)
PALETTE = [
 {"dark":"#16273f","deep":"#101d31","tint":"#eceff4","mood":"NAVY"},      #1 navy
 {"dark":"#1d3a2a","deep":"#152b1f","tint":"#e9efe9","mood":"FOREST"},    #2 forest
 {"dark":"#48412c","deep":"#372f1d","tint":"#f0ece1","mood":"STONE"},     #3 warm stone
 {"dark":"#123f3c","deep":"#0c2e2c","tint":"#e6efed","mood":"TEAL"},      #4 teal
 {"dark":"#3a2a1c","deep":"#2b1e13","tint":"#efe9e1","mood":"ESPRESSO"},  #5 espresso
 {"dark":"#372540","deep":"#281a30","tint":"#ede9f0","mood":"PLUM"},      #6 plum
 {"dark":"#143b30","deep":"#0e2b23","tint":"#e6efe9","mood":"EMERALD"},   #7 emerald
 {"dark":"#4a212b","deep":"#36161e","tint":"#f2e9eb","mood":"WINE"},      #8 wine
 {"dark":"#1c2c49","deep":"#142037","tint":"#eaedf3","mood":"INDIGO"},    #9 indigo
 {"dark":"#21433c","deep":"#16302b","tint":"#e8efec","mood":"SLATE"},     #10 slate-teal
]
