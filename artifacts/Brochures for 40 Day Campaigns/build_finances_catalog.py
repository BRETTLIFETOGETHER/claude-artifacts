# -*- coding: utf-8 -*-
import pathlib
from catalog_engine import build_catalog, render_pdf

cfg = {
 "category":"Finances",
 "doc_title":"Finances Campaign Catalog",
 "tier":"Tier 1",
 "accent":"#1f5c47",   # finances green
 "accent2":"#c19a4b",
 "positioning":("A complete library of 100 ready-to-run campaigns that help churches, companies, and families handle "
   "money God\u2019s way \u2014 trading anxiety, debt, and the chase for more for contentment, freedom, wisdom, and peace."),
 "why_matters":("Money is one of the most spiritual subjects in all of Scripture and one of the most stressful realities in "
   "everyday life. Jesus spoke about it constantly, because nothing reveals or rivals our trust in God more clearly. Yet most "
   "people carry quiet financial stress, debt, and fear with little help connecting their faith to their finances. A church "
   "that disciples its people in a faithful, freeing relationship with money meets one of the deepest practical needs they have."),
 "core_problem":("Capable, faithful people are stressed, stretched, and silently anxious about money \u2014 chasing more, weighed "
   "down by debt, and unsure how their faith touches their finances at all. They want a better way but rarely find one that is "
   "both genuinely biblical and genuinely practical. Leaders see the need but have few resources that speak to money with grace, wisdom, and hope."),
 "transformation":("These campaigns move people from anxiety to peace, from debt to freedom, from chasing more to contentment, "
   "and from managing money to handling it as an act of faith \u2014 until their finances reflect their trust in God."),
 "who_needs":[
   ("Churches","A complete, grace-filled pathway for discipling people in a faithful, freeing relationship with money."),
   ("Companies","A values-rich framework on contentment, wisdom, and financial wellbeing that serves any team."),
   ("Advisors &amp; Donors","A faith-centered vision of money and meaning to share with clients and giving partners."),
   ("Families","A way to build a household that handles money wisely, freely, and without fear."),
 ],
 "outcomes":[
   "A faithful, biblical relationship with money",
   "Freedom from debt and the grip of money",
   "Contentment in place of the chase for more",
   "Relief from financial anxiety and fear",
   "Practical wisdom for everyday money decisions",
   "Peace and purpose in how money is handled",
 ],
 "use_cases":[
   ("Churchwide Finances Series","A grace-filled series connecting faith and everyday money."),
   ("40-Day Spiritual Campaign","Weekend messages, small groups, and daily readings."),
   ("21-Day Money Challenge","A short, practical reset on faith and finances."),
   ("4-Week Sermon Companion","A focused message series with sermon-aligned small-group guides."),
   ("Advisor &amp; Donor Resource","A premium resource for clients and giving partners."),
 ],
 "stats":[("100","Campaigns"),("10","Expanded"),("10","Themes"),("4","Formats"),("NIV","Scripture")],
 "components":["Daily Readings & Reflections","Six Group-Session Guides","Weekend Message Outlines",
               "Spiritual-Partner Prompts","Launch & Promotion Kit"],

 "top10":[
 {"n":"01","title":"Faith & Finances","pos":"See your money for what it really is \u2014 a discipleship issue, not just a math one.",
  "felt":"Faith & money","aud":"Church & Company",
  "summary":"The foundational campaign \u2014 connecting faith and money, and recovering the freeing truth that how we handle money is one of the clearest windows into the heart.",
  "marketing":("The flagship entry point for the category. Faith & Finances reconnects two things we tend to keep apart \u2014 Sunday "
     "faith and Monday money \u2014 revealing that Scripture treats how we handle money as a frontline discipleship issue."),
  "problem":("We file money under \u2018practical\u2019 and faith under \u2018spiritual,\u2019 and rarely let the two meet. But Jesus refused that "
     "split. He spoke about money more than almost any other subject \u2014 not because heaven needed it, but because nothing reveals and rivals our devotion to God quite like it."),
  "transformation":("Participants come to see money the way Scripture does \u2014 as a spiritual matter that reveals the heart \u2014 and "
     "begin to handle it as an act of worship and trust rather than mere management."),
  "sessions":[("Sunday Faith, Monday Money","The split Jesus never made."),("Why Jesus Talked About Money","The subject He wouldn\u2019t leave alone."),
     ("God Owns It All","Stewardship as the starting point."),("What Your Money Reveals","The heart behind the budget."),
     ("Worship or Worry","The two directions money pulls."),("A New Way with Money","Handling it as an act of faith.")],
  "scriptures":"Matthew 6:24  \u00b7  Haggai 2:8  \u00b7  Luke 16:11  \u00b7  1 Timothy 6:17\u201319",
  "aud_full":"Church & Company \u2014 the ideal on-ramp to the entire finances category.",
  "formats":"4-Session Series  \u00b7  21-Day Challenge  \u00b7  30-Day Devotional  \u00b7  40-Day Campaign (recommended)",
  "bigidea":"Jesus talked about money more than almost anything else \u2014 not because heaven needs your money, but because nothing else so quietly competes for your heart.",
  "ideal":"All-church on-ramps; anyone who keeps faith and money in separate boxes.",
  "pairs":"God, Money & Me  \u00b7  Money Wise",
  "outcomes":["Faith and money reconnected","Money seen as a heart issue","A worshipful approach to money"]},

 {"n":"02","title":"Money & Contentment","pos":"Get off the \u2018just a little more\u2019 treadmill for good.",
  "felt":"Contentment","aud":"Church & Company",
  "summary":"A contentment campaign \u2014 confronting the quiet lie that a little more will finally be enough, and learning the rare, freeing secret of godliness with contentment.",
  "marketing":("Money & Contentment names the treadmill almost everyone is on \u2014 the belief that a little more will finally "
     "satisfy \u2014 and teaches the learned, counter-cultural secret Paul called great gain."),
  "problem":("There\u2019s a number in our heads where we believe we\u2019d finally feel secure \u2014 and the moment we reach it, the number "
     "moves. The hunger for \u2018a little more\u2019 is endless by design, and it quietly steals the joy of everything we already have."),
  "transformation":("Participants learn what Paul said he had to learn \u2014 the secret of being content in plenty and in want \u2014 "
     "discovering that godliness with contentment, not accumulation, is the real wealth."),
  "sessions":[("The Number That Moves","Why \u2018a little more\u2019 is never enough."),("The Treadmill of More","The hunger that can\u2019t be fed."),
     ("Great Gain","Godliness with contentment as true wealth."),("The Secret Paul Learned","Contentment as a skill, not a circumstance."),
     ("Enough, and Grateful","Receiving today as sufficient."),("Free from More","A life off the treadmill.")],
  "scriptures":"1 Timothy 6:6\u201310  \u00b7  Philippians 4:11\u201313  \u00b7  Hebrews 13:5  \u00b7  Ecclesiastes 5:10",
  "aud_full":"Church & Company \u2014 a freeing reset for the chronically discontent.",
  "formats":"4-Session Series  \u00b7  21-Day Challenge  \u00b7  30-Day Devotional  \u00b7  40-Day Campaign",
  "bigidea":"Contentment isn\u2019t getting what you want \u2014 it\u2019s a secret you learn. Paul called godliness with contentment \u2018great gain,\u2019 because the person who has it has already won the game everyone else is still chasing.",
  "ideal":"Anyone on the \u2018a little more\u2019 treadmill; the discontent and comparison-weary.",
  "pairs":"Faith & Finances  \u00b7  Peace with Money",
  "outcomes":["Freedom from the \u2018more\u2019 treadmill","The learned secret of contentment","Gratitude for what you have"]},

 {"n":"03","title":"Money Made Simple","pos":"Cut through the money stress with a few simple, biblical principles.",
  "felt":"Clarity & simplicity","aud":"Church & Company",
  "summary":"A clarifying campaign \u2014 untangling the overwhelm around money with a handful of simple, time-tested biblical principles anyone can follow.",
  "marketing":("Money Made Simple cuts through the noise. It replaces financial overwhelm with a few clear, biblical principles "
     "\u2014 spend less than you earn, give first, save wisely, avoid the debt trap \u2014 that anyone can actually follow."),
  "problem":("Money feels impossibly complicated \u2014 budgets, debt, apps, advice from every direction \u2014 and the overwhelm leaves "
     "many of us avoiding it entirely. But the Bible\u2019s core money wisdom is remarkably simple; we\u2019ve just buried it under noise and shame."),
  "transformation":("Participants trade overwhelm for clarity \u2014 learning a handful of simple, biblical money principles they can "
     "actually live by \u2014 and discover that faithfulness with money is less complicated than they feared."),
  "sessions":[("Buried in Complexity","Why money feels so overwhelming."),("Count the Cost","The wisdom of a simple plan."),
     ("Spend Less Than You Make","The principle everything rests on."),("Give First, Save Next","Ordering money God\u2019s way."),
     ("The Debt Trap","Why borrowed money enslaves."),("Simple and Free","A clear, livable way with money.")],
  "scriptures":"Luke 14:28  \u00b7  Proverbs 21:5  \u00b7  Proverbs 22:7  \u00b7  Proverbs 13:11",
  "aud_full":"Church & Company \u2014 practical and accessible; great for all money stages.",
  "formats":"4-Session Series  \u00b7  21-Day Challenge  \u00b7  30-Day Devotional  \u00b7  40-Day Campaign",
  "bigidea":"God\u2019s money wisdom isn\u2019t complicated \u2014 we\u2019ve just buried it. Spend less than you earn, give first, avoid debt, and trust God: simple to say, freeing to live.",
  "ideal":"The overwhelmed and money-avoidant; anyone wanting a simple plan.",
  "pairs":"Free with Money  \u00b7  Money Wise",
  "outcomes":["Clarity instead of overwhelm","A few livable money principles","Confidence to face finances"]},

 {"n":"04","title":"Free with Money","pos":"Break the grip of debt and the hold money has on you.",
  "felt":"Freedom from debt","aud":"Church & Company",
  "summary":"A freedom campaign \u2014 breaking free from the slavery of debt and the quiet grip money holds, into the liberty of owing no one and trusting God.",
  "marketing":("Free with Money confronts the modern bondage of debt and the subtler grip money holds on the soul \u2014 and charts "
     "the path to real freedom: owing no one, ruled by nothing, holding money with an open hand."),
  "problem":("Scripture is blunt: the borrower is slave to the lender. Many of us feel that slavery every month \u2014 owned by "
     "payments, pressured by what we owe, unable to be generous or free. And even those without debt can be quietly mastered by the love of money."),
  "transformation":("Participants begin to break free \u2014 from the chains of debt and the grip of money\u2019s hold \u2014 learning to owe no "
     "one but love, to hold money loosely, and to live with the liberty God intends."),
  "sessions":[("Slave to the Lender","The bondage Scripture names plainly."),("The Weight of Owing","What debt does to the soul."),
     ("The Love That Enslaves","How money masters even the debt-free."),("The Path to Free","Practical first steps out of bondage."),
     ("Owe No One but Love","Living unchained and generous."),("Free Indeed","The liberty of a heart money can\u2019t own.")],
  "scriptures":"Proverbs 22:7  \u00b7  Romans 13:8  \u00b7  1 Timothy 6:9\u201310  \u00b7  Galatians 5:1",
  "aud_full":"Church & Company \u2014 hopeful and practical; powerful for the debt-burdened.",
  "formats":"4-Session Series  \u00b7  21-Day Challenge  \u00b7  30-Day Devotional  \u00b7  40-Day Campaign",
  "bigidea":"The borrower is slave to the lender \u2014 and money will master anyone who lets it. Real freedom isn\u2019t a bigger balance; it\u2019s owing no one and being owned by nothing but God.",
  "ideal":"The debt-burdened; anyone who feels owned by money.",
  "pairs":"Money Made Simple  \u00b7  Money & Contentment",
  "outcomes":["A path out of debt","Freedom from money\u2019s grip","Liberty to live and give"]},

 {"n":"05","title":"Money Wise","pos":"Handle money with the kind of wisdom Scripture promises.",
  "felt":"Wisdom with money","aud":"Church & Company",
  "summary":"A wisdom campaign \u2014 applying the practical, time-tested wisdom of Scripture to earning, saving, spending, and planning, the way the wise have always handled what they\u2019re given.",
  "marketing":("Money Wise brings biblical wisdom to bear on everyday money \u2014 the ant\u2019s foresight, the wisdom of saving, the "
     "folly of get-rich-quick \u2014 helping people handle what they have the way the wise always have."),
  "problem":("We\u2019re surrounded by money advice and short on money wisdom. Get-rich-quick schemes, impulse spending, no margin "
     "for the future \u2014 the foolish patterns Proverbs warned about thousands of years ago are alive and well, and quietly costing us."),
  "transformation":("Participants grow wise with money \u2014 learning the foresight, diligence, and patience Scripture commends \u2014 so "
     "they handle what they\u2019ve been given shrewdly, faithfully, and well."),
  "sessions":[("Advice vs. Wisdom","Why information isn\u2019t enough."),("Consider the Ant","The wisdom of foresight and saving."),
     ("Slow and Steady","Why get-rich-quick gets nowhere."),("The Diligent Hand","Work, patience, and provision."),
     ("Counsel and Planning","The wisdom of a plan and good advisors."),("Wise with What You\u2019re Given","Faithful handling for a lifetime.")],
  "scriptures":"Proverbs 6:6\u20138  \u00b7  Proverbs 13:11  \u00b7  Proverbs 21:20  \u00b7  Proverbs 15:22",
  "aud_full":"Church & Company \u2014 practical money wisdom for every stage of life.",
  "formats":"4-Session Series  \u00b7  21-Day Challenge  \u00b7  30-Day Devotional  \u00b7  40-Day Campaign",
  "bigidea":"The money mistakes Proverbs warned about are still the ones we make. Wisdom with money isn\u2019t complicated genius \u2014 it\u2019s foresight, diligence, and patience, applied faithfully over time.",
  "ideal":"Anyone wanting practical money wisdom; savers, planners, and the impulsive alike.",
  "pairs":"Money Made Simple  \u00b7  Faith & Finances",
  "outcomes":["Practical money wisdom","Foresight and patience with money","Faithful handling of resources"]},

 {"n":"06","title":"God, Money & Me","pos":"Settle the question of who\u2019s really on the throne of your life.",
  "felt":"Lordship & money","aud":"Church & Company",
  "summary":"A lordship campaign \u2014 confronting the rivalry between God and money for the throne of our lives, and choosing daily whom we will actually serve.",
  "marketing":("God, Money & Me names the showdown Jesus described: no one can serve two masters. It helps people see money\u2019s "
     "bid to rule them and choose, daily, to keep God on the throne."),
  "problem":("Jesus said it plainly: you cannot serve both God and money. Yet most of us try \u2014 keeping God for Sunday and letting "
     "money quietly run Monday through Saturday. Money makes a subtle, relentless bid to be our master, and we rarely notice we\u2019ve handed it the throne."),
  "transformation":("Participants confront money\u2019s bid for lordship in their own hearts \u2014 and learn to dethrone it daily, keeping "
     "God in His rightful place and money in its rightful role as a servant, never a master."),
  "sessions":[("Two Masters","The choice Jesus says we can\u2019t avoid."),("The Quiet Takeover","How money climbs onto the throne."),
     ("Mammon","Money\u2019s strange bid to become a god."),("Who\u2019s Really Lord?","An honest look at your week."),
     ("Dethroning Money","Putting it back in its place."),("God on the Throne","A life with one Master.")],
  "scriptures":"Matthew 6:24  \u00b7  Luke 16:13  \u00b7  Colossians 3:5  \u00b7  Matthew 6:33",
  "aud_full":"Church & Company \u2014 a pointed, personal heart-check for everyone.",
  "formats":"4-Session Series  \u00b7  21-Day Challenge  \u00b7  30-Day Devotional  \u00b7  40-Day Campaign",
  "bigidea":"You cannot serve two masters \u2014 and money is always applying for the job. The question isn\u2019t whether you\u2019ll have money, but whether money will have you.",
  "ideal":"Everyone; anyone who senses money has more of them than they\u2019d like.",
  "pairs":"Faith & Finances  \u00b7  Money & the Heart",
  "outcomes":["Money dethroned as master","God kept on the throne","A clear daily allegiance"]},

 {"n":"07","title":"Money & the Heart","pos":"Follow the money \u2014 it will lead you straight to your heart.",
  "felt":"Treasure & the heart","aud":"Church & Company",
  "summary":"A heart-diagnostic campaign on Matthew 6:21 \u2014 where your treasure goes, your heart follows; learning to read your spending as a map of your loves, and to invest where it lasts.",
  "marketing":("Money & the Heart turns a famous verse into a mirror: where your treasure is, there your heart will be also. It "
     "teaches people to read their spending as a map of their affections \u2014 and to move their treasure toward what lasts."),
  "problem":("We assume our hearts lead and our money follows. Jesus said it works the other way too: where you put your treasure "
     "is where your heart ends up. Our bank statements quietly reveal \u2014 and shape \u2014 what we actually love, often exposing a gap between our stated values and our spending."),
  "transformation":("Participants learn to read their spending as a map of their hearts \u2014 and to deliberately move their treasure "
     "toward God and others \u2014 trusting Jesus\u2019 promise that the heart will follow the treasure home."),
  "sessions":[("Follow the Money","What your spending reveals."),("Where Your Treasure Is","The verse that reads your heart."),
     ("The Heart Follows","How treasure pulls affection after it."),("Storing Up","Earthly moth and rust vs. heavenly permanence."),
     ("Treasure That Lasts","Investing where it can\u2019t be lost."),("A Heart Sent Home","Moving your treasure toward God.")],
  "scriptures":"Matthew 6:19\u201321  \u00b7  Luke 12:32\u201334  \u00b7  1 Timothy 6:18\u201319  \u00b7  Matthew 6:33",
  "aud_full":"Church & Company \u2014 a revealing, gently convicting campaign for all.",
  "formats":"4-Session Series  \u00b7  21-Day Challenge  \u00b7  30-Day Devotional  \u00b7  40-Day Campaign",
  "bigidea":"Jesus said where your treasure goes, your heart follows. That means your bank statement is a kind of map of your loves \u2014 and you can move your heart by moving your treasure.",
  "ideal":"Anyone wanting their money to match their values; the spiritually reflective.",
  "pairs":"God, Money & Me  \u00b7  Money & Meaning",
  "outcomes":["Spending read as a heart-map","Treasure moved toward what lasts","Money aligned with values"]},

 {"n":"08","title":"Breaking Financial Fear","pos":"Trade the 3 a.m. money panic for a settled trust in God\u2019s provision.",
  "felt":"Money anxiety","aud":"Church & Company",
  "summary":"A campaign for the anxious \u2014 confronting the fear that grips us about money and the future, and replacing it with trust in a Father who feeds the birds and clothes the fields.",
  "marketing":("Breaking Financial Fear speaks to the 3 a.m. money worry almost everyone knows. It confronts financial anxiety "
     "head-on and replaces it with the deep trust Jesus offered when He pointed to the birds and the lilies."),
  "problem":("Money fear has a particular grip \u2014 the late-night math, the what-ifs, the knot in the stomach. Even people with "
     "enough lie awake afraid it won\u2019t last. It\u2019s one of the most common anxieties there is, and willpower alone has never once quieted it."),
  "transformation":("Participants learn to bring their financial fears to the God who feeds the birds and clothes the lilies \u2014 "
     "exchanging the exhausting habit of worry for a settled, practiced trust in His provision."),
  "sessions":[("The 3 A.M. Math","The particular grip of money fear."),("Consider the Birds","What Jesus says to the anxious."),
     ("Your Father Knows","The provision behind the promise."),("Worry Changes Nothing","Naming the futility of fear."),
     ("Seek First","The reorder that quiets anxiety."),("A Settled Heart","Trading worry for trust.")],
  "scriptures":"Matthew 6:25\u201334  \u00b7  Philippians 4:6\u20137  \u00b7  1 Peter 5:7  \u00b7  Psalm 37:25",
  "aud_full":"Church & Company \u2014 includes gentle pastoral framing for the anxious.",
  "formats":"4-Session Series  \u00b7  21-Day Challenge  \u00b7  30-Day Devotional  \u00b7  40-Day Campaign",
  "bigidea":"Worry has never once added a dollar or a day. Jesus points the financially afraid to the birds and the lilies \u2014 not to shame the fear, but to reintroduce us to the Father who feeds them.",
  "ideal":"The anxious and sleepless; anyone gripped by money fear.",
  "pairs":"Peace with Money  \u00b7  Money & Contentment",
  "outcomes":["Relief from money anxiety","Trust in God\u2019s provision","A settled, less fearful heart"]},

 {"n":"09","title":"Money & Meaning","pos":"Turn your money into something that will outlast you.",
  "felt":"Purpose & impact","aud":"Church & Company",
  "summary":"A purpose campaign \u2014 lifting money from mere survival to significance; using what we have for what matters and what lasts beyond this life.",
  "marketing":("Money & Meaning lifts the conversation from managing money to deploying it for what matters \u2014 turning ordinary "
     "finances into instruments of purpose, generosity, and eternal impact."),
  "problem":("Even when the bills are paid, a quiet question remains: is this all my money is for \u2014 survival, comfort, a little "
     "more? Money handled only for itself feels strangely empty, and many sense their resources could mean something more without knowing how."),
  "transformation":("Participants discover how to put their money to work for purpose \u2014 storing up treasure in heaven, being rich "
     "toward God and generous toward others \u2014 so their finances become an instrument of lasting meaning, not just maintenance."),
  "sessions":[("Just for This?","The emptiness of money without meaning."),("Rich Toward God","The wealth that actually counts."),
     ("Treasure in Heaven","Sending it ahead where it lasts."),("Use Worldly Wealth Well","Money as an instrument of good."),
     ("Generous and Significant","Resources that bless and outlast you."),("Money with Meaning","Finances in service of purpose.")],
  "scriptures":"Luke 12:16\u201321  \u00b7  1 Timothy 6:18\u201319  \u00b7  Luke 16:9  \u00b7  Matthew 6:20",
  "aud_full":"Church & Company \u2014 purpose-rich; great for those asking \u2018what\u2019s it all for?\u2019",
  "formats":"4-Session Series  \u00b7  21-Day Challenge  \u00b7  30-Day Devotional  \u00b7  40-Day Campaign",
  "bigidea":"Money handled only for itself always feels empty. Its deepest meaning is found the moment it stops being the point and starts serving one \u2014 rich toward God, generous toward people, sent ahead to where it lasts.",
  "ideal":"Those with \u2018enough\u2019 who sense money should mean more; the purpose-seeking.",
  "pairs":"Money & the Heart  \u00b7  Faith & Finances",
  "outcomes":["Money deployed for purpose","An eternal perspective on wealth","Generosity and significance"]},

 {"n":"10","title":"Peace with Money","pos":"End the war with money and finally find rest.",
  "felt":"Rest & peace","aud":"Church & Company",
  "summary":"A capstone campaign \u2014 ending the lifelong tension with money and entering a settled peace rooted in God\u2019s presence and provision rather than a number.",
  "marketing":("Peace with Money is the category\u2019s restful capstone. It moves people from a lifelong, low-grade war with money "
     "into a settled peace \u2014 not because the numbers all worked out, but because their security finally rests in God."),
  "problem":("For many, money is a quiet, constant source of tension \u2014 never quite enough, never fully at rest, a low-grade war "
     "that no raise or windfall seems to end. We keep believing peace lies just past the next financial milestone, and it never does."),
  "transformation":("Participants find a peace with money that doesn\u2019t depend on a number \u2014 rooting their security in God\u2019s "
     "presence and promise to never leave them \u2014 and lay down the exhausting war for good."),
  "sessions":[("The Quiet War","The tension money keeps stirring."),("Never the Next Number","Why milestones don\u2019t bring peace."),
     ("Keep Your Life Free","Contentment and the promise behind it."),("Never Will I Leave You","The presence that steadies us."),
     ("The God of Enough","Resting in His provision."),("At Peace with Money","Laying down the war for good.")],
  "scriptures":"Hebrews 13:5  \u00b7  Philippians 4:6\u20137  \u00b7  Psalm 23:1  \u00b7  Matthew 11:28\u201330",
  "aud_full":"Church & Company \u2014 a restful, hope-filled close to the category.",
  "formats":"4-Session Series  \u00b7  21-Day Challenge  \u00b7  30-Day Devotional  \u00b7  40-Day Campaign",
  "bigidea":"Peace with money never comes from the next milestone \u2014 the goalposts always move. It comes from the One who said \u2018I will never leave you,\u2019 which is why contentment and His presence are named in the very same breath.",
  "ideal":"Anyone locked in a low-grade war with money; a fitting close to the category.",
  "pairs":"Money & Contentment  \u00b7  Breaking Financial Fear",
  "outcomes":["An end to the money war","Peace not tied to a number","Security rooted in God"]},
 ],

 "library":[
  ("Faith & Money Foundations", [
    ("Faith & Finances","T1",True),("Money & Faith","T1",False),("God Owns It All","T1",False),
    ("The Spiritual Side of Money","T2",False),("Sunday Faith, Monday Money","T2",False),("Money Matters to God","T2",False),
    ("A Biblical View of Money","T2",False),("Whose Money Is It?","T2",False),("Money as Worship","T2",False),
    ("Faith Over Finances","T2",False)]),
  ("Contentment & Enough", [
    ("Money & Contentment","T1",True),("The Secret of Contentment","T1",False),("Off the Treadmill","T1",False),
    ("Godliness with Contentment","T2",False),("The Number That Moves","T2",False),("Content in Plenty and Want","T2",False),
    ("The Cure for More","T2",False),("Grateful and Free","T2",False),("When Is It Enough?","T2",False),
    ("The Contented Life","T2",False)]),
  ("Simplicity & a Plan", [
    ("Money Made Simple","T1",True),("A Simple Plan","T1",False),("Spend Less Than You Earn","T1",False),
    ("Count the Cost","T2",False),("The Family Budget","T2",False),("Give First, Save Next","T2",False),
    ("Untangling Your Finances","T2",False),("Money Without Overwhelm","T2",False),("The Simple Money Plan","T2",False),
    ("Clarity with Cash","T2",False)]),
  ("Freedom from Debt", [
    ("Free with Money","T1",True),("Out of Debt","T1",False),("Owe No One","T1",False),
    ("Slave to the Lender","T2",False),("Breaking the Debt Cycle","T2",False),("The Weight of Owing","T2",False),
    ("Free Indeed","T2",False),("Debt and Freedom","T2",False),("Unchained from Money","T2",False),
    ("The Path to Free","T2",False)]),
  ("Money Wisdom", [
    ("Money Wise","T1",True),("Wise with Money","T1",False),("Consider the Ant","T1",False),
    ("The Wisdom of Saving","T2",False),("Slow and Steady","T2",False),("Get-Rich-Slow","T2",False),
    ("The Diligent Hand","T2",False),("Planning and Counsel","T2",False),("Foresight with Money","T2",False),
    ("Shrewd and Faithful","T2",False)]),
  ("Money & Lordship", [
    ("God, Money & Me","T1",True),("Two Masters","T1",False),("Who\u2019s on the Throne?","T1",False),
    ("Money or Mammon","T2",False),("Dethroning Money","T2",False),("You Cannot Serve Both","T2",False),
    ("Money\u2019s Quiet Takeover","T2",False),("One Master","T2",False),("Christ over Money","T2",False),
    ("Serving God, Not Money","T2",False)]),
  ("Money & the Heart", [
    ("Money & the Heart","T1",True),("Where Your Treasure Is","T1",False),("Follow the Money","T1",False),
    ("Treasure and Affection","T2",False),("What Your Spending Reveals","T2",False),("Storing Up Treasure","T2",False),
    ("Heart and Wallet","T2",False),("Treasure That Lasts","T2",False),("The Map of Your Loves","T2",False),
    ("A Heart Sent Home","T2",False)]),
  ("Money & Anxiety", [
    ("Breaking Financial Fear","T1",True),("Consider the Birds","T1",False),("The 3 A.M. Math","T1",False),
    ("Anxious for Nothing","T2",False),("Worry and Money","T2",False),("Your Father Knows","T2",False),
    ("Casting Your Cares","T2",False),("Fear Not for Tomorrow","T2",False),("The Worry-Free Wallet","T2",False),
    ("Trusting His Provision","T2",False)]),
  ("Money & Purpose", [
    ("Money & Meaning","T1",True),("Rich Toward God","T1",False),("Treasure in Heaven","T1",False),
    ("Money with a Mission","T2",False),("What\u2019s It All For?","T2",False),("Significance Over Survival","T2",False),
    ("Use Worldly Wealth Well","T2",False),("Money That Outlasts You","T2",False),("Investing in Eternity","T2",False),
    ("Purpose in Your Provision","T2",False)]),
  ("Peace & Rest with Money", [
    ("Peace with Money","T1",True),("The End of the Money War","T1",False),("Never Will I Leave You","T1",False),
    ("Rest for the Weary Wallet","T2",False),("The God of Enough","T2",False),("Beyond the Next Number","T2",False),
    ("Settled About Money","T2",False),("At Rest with Money","T2",False),("Money and the Soul\u2019s Rest","T2",False),
    ("Free from the Money Fight","T2",False)]),
 ],
}

doc, npages = build_catalog(cfg)
pathlib.Path("/tmp/finances_catalog.html").write_text(doc, encoding="utf-8")
render_pdf("/tmp/finances_catalog.html", "/tmp/finances_catalog.pdf")
print("Finances catalog (elevated):", npages, "pages")
