# -*- coding: utf-8 -*-
import pathlib
from catalog_engine import build_catalog, render_pdf

cfg = {
 "category":"Wisdom",
 "doc_title":"Wisdom & Decision-Making Campaign Library",
 "tier":"Tier 2",
 "accent":"#5a3760",   # deep plum
 "accent2":"#c19a4b",
 "positioning":("A complete library of 100 ready-to-run campaigns that help churches, companies, and families decide "
   "well, discern rightly, and order their priorities \u2014 trading guesswork and anxiety for the wisdom that begins with God."),
 "why_matters":("Every life is the sum of its decisions \u2014 and most people were never taught how to make them. We face "
   "constant choices about work, money, relationships, and direction with little more than gut feel and good intentions, then "
   "live with years of second-guessing. Scripture devotes whole books to wisdom because God knows decisions are where faith "
   "meets the road. A church that disciples its people in wisdom shapes not just their beliefs, but the entire trajectory of their lives."),
 "core_problem":("Capable, sincere people make poor decisions \u2014 not for lack of information, but for lack of wisdom. They lean "
   "on their own understanding, decide in a fog, and confuse what merely seems right with what is. Leaders see people stuck, "
   "anxious, and drifting, but have few resources that teach biblical wisdom and discernment in a clear, practical way."),
 "transformation":("These campaigns move people from guesswork to wisdom, from confusion to clarity, and from anxious "
   "indecision to confident, God-directed choices \u2014 until deciding well becomes a way of life, not a recurring crisis."),
 "who_needs":[
   ("Churches","A complete wisdom pathway that disciples decision-making and discernment \u2014 practical, biblical, and life-shaping."),
   ("Companies","A framework for sound judgment, clear priorities, and wise decisions that strengthens any team or leader."),
   ("Advisors &amp; Donors","A grounded vision of biblical wisdom to share with clients and partners who weigh big decisions."),
   ("Families","A way to raise discerning children and build a household that decides well and orders its priorities."),
 ],
 "outcomes":[
   "A foundation for wisdom that begins with God",
   "A clear, repeatable way to make decisions",
   "Sharper discernment between good, bad, and best",
   "Freedom from decision paralysis and second-guessing",
   "Wiser everyday choices in work, words, and relationships",
   "A life increasingly directed and ordered by wisdom",
 ],
 "use_cases":[
   ("Churchwide Wisdom Series","A whole-church journey into biblical wisdom and decision-making."),
   ("40-Day Spiritual Campaign","Weekend messages, small groups, and daily wisdom readings."),
   ("21-Day Decision Challenge","A short, focused experience for a season of big decisions."),
   ("4-Week Sermon Companion","A focused message series with sermon-aligned small-group guides."),
   ("Advisor &amp; Donor Resource","A premium resource for clients and partners facing major choices."),
 ],
 "stats":[("100","Campaigns"),("10","Expanded"),("10","Themes"),("4","Formats"),("NIV","Scripture")],
 "components":["Daily Readings & Reflections","Six Group-Session Guides","Weekend Message Outlines",
               "Spiritual-Partner Prompts","Launch & Promotion Kit"],

 "top10":[
 {"n":"01","title":"Wise Decisions","pos":"Begin where all real wisdom begins \u2014 and never decide blind again.",
  "felt":"Foundations of wisdom","aud":"Church & Company",
  "summary":"The foundational campaign on biblical wisdom \u2014 where it begins, why it\u2019s worth more than gold, and how the fear of the Lord reshapes every decision that follows.",
  "marketing":("The flagship entry point for the category. Wise Decisions goes underneath technique to the root: real wisdom "
     "begins not with smarter strategies but with the fear of the Lord \u2014 and from that root, better decisions grow."),
  "problem":("We treat wisdom as a skill we can pick up \u2014 a few better habits, a sharper pros-and-cons list. But Scripture says "
     "wisdom has a starting point we keep skipping: the fear of the Lord. Without it we\u2019re merely clever; with it we finally begin to be wise."),
  "transformation":("Participants discover what biblical wisdom actually is, where it begins, and how to ask God for it \u2014 "
     "building every decision on the one foundation that holds."),
  "sessions":[("Smarter Isn\u2019t Wiser","Why intelligence and wisdom aren\u2019t the same."),("Where Wisdom Begins","The fear of the Lord as the true starting line."),
     ("Worth More Than Gold","Why Scripture prizes wisdom above everything."),("Ask, and It Is Given","The startling promise of James 1:5."),
     ("Christ, Our Wisdom","Where the search for wisdom finally lands."),("Wise from the Root","Decisions that grow from the right foundation.")],
  "scriptures":"Proverbs 9:10  \u00b7  Proverbs 4:7  \u00b7  James 1:5  \u00b7  1 Corinthians 1:30",
  "aud_full":"Church & Company \u2014 the ideal on-ramp to the entire wisdom category.",
  "formats":"4-Session Series  \u00b7  21-Day Challenge  \u00b7  30-Day Devotional  \u00b7  40-Day Campaign (recommended)",
  "bigidea":"Wisdom doesn\u2019t begin with information \u2014 it begins with awe. The fear of the Lord is the doorway, and everyone who skips it stays merely clever, never truly wise.",
  "ideal":"All-church on-ramps; anyone who wants to decide from a deeper foundation.",
  "pairs":"Walking in Wisdom  \u00b7  Decide Well",
  "outcomes":["A true foundation for wisdom","Decisions rooted in the fear of the Lord","Confidence to ask God for wisdom"]},

 {"n":"02","title":"Walking in Wisdom","pos":"Make wisdom not just a decision you make, but a way you walk.",
  "felt":"Daily wise living","aud":"Church & Company",
  "summary":"A daily-living campaign on Ephesians 5 \u2014 wisdom not as an occasional big decision, but as a careful, intentional daily walk that redeems the time.",
  "marketing":("Walking in Wisdom moves wisdom out of the crisis moment and into the everyday. It teaches people to watch how "
     "they walk \u2014 living carefully, intentionally, and wisely through ordinary days."),
  "problem":("We save wisdom for the big decisions and sleepwalk through the small ones \u2014 the daily choices about time, words, "
     "and attention that quietly add up to a life. But Scripture says to watch carefully how we walk, not as unwise but as wise."),
  "transformation":("Participants learn to carry wisdom into the ordinary \u2014 walking carefully, redeeming the time, and making the "
     "most of every opportunity \u2014 until wise living becomes a daily rhythm, not a rare event."),
  "sessions":[("Watch How You Walk","Wisdom in the steps no one notices."),("Not as the Unwise","The two ways to move through a day."),
     ("Redeeming the Time","Making the most of the days you\u2019re given."),("Wisdom in the Ordinary","The small choices that shape a life."),
     ("Walking in Step","Keeping pace with the Spirit\u2019s wisdom."),("A Wise Walk","Living wisely all the way to the end.")],
  "scriptures":"Ephesians 5:15\u201316  \u00b7  Colossians 4:5  \u00b7  Psalm 90:12  \u00b7  Proverbs 14:8",
  "aud_full":"Church & Company \u2014 turns wisdom into a sustainable daily practice.",
  "formats":"4-Session Series  \u00b7  21-Day Challenge  \u00b7  30-Day Devotional  \u00b7  40-Day Campaign",
  "bigidea":"Wisdom isn\u2019t reserved for the crossroads; it\u2019s how you cross the room. A wise life is mostly built in the small, daily steps no one is watching.",
  "ideal":"Anyone whose wisdom shows up only in emergencies; daily-discipleship contexts.",
  "pairs":"Wise Decisions  \u00b7  The Wise Life",
  "outcomes":["Wisdom as a daily walk","Intentionality in ordinary days","Time redeemed, not wasted"]},

 {"n":"03","title":"Decide Well","pos":"Trade guesswork and gut-feel for a wise way to decide.",
  "felt":"The decision process","aud":"Church & Company",
  "summary":"A practical decision-making campaign \u2014 a clear, repeatable, biblical process for facing any choice with trust, counsel, and prayer instead of guesswork.",
  "marketing":("Decide Well hands people a process. It replaces the anxious mix of gut-feel and guesswork with a clear, "
     "repeatable, biblical way to face any decision \u2014 trusting God, gathering wisdom, and finding peace."),
  "problem":("Most of us decide the way the world does \u2014 weighing pros and cons, trusting our gut, hoping for the best \u2014 and then "
     "second-guess it for weeks. We\u2019ve never been given a wise, repeatable way to actually make a decision."),
  "transformation":("Participants gain a clear, biblical framework for deciding \u2014 leaning on God rather than themselves, seeking "
     "counsel, asking for wisdom, and recognizing the peace that confirms the way \u2014 so they can decide and move forward without regret."),
  "sessions":[("The Tyranny of the Decision","Why choices leave us stuck."),("Lean Not on Your Own","Trading self-reliance for trust."),
     ("The Safety of Counsel","Why the wise borrow wisdom."),("Ask for Wisdom","Bringing the decision to God first."),
     ("The Peace That Confirms","Recognizing God\u2019s quiet yes."),("Decide and Move","Choosing well, then letting go.")],
  "scriptures":"Proverbs 3:5\u20136  \u00b7  James 1:5  \u00b7  Proverbs 15:22  \u00b7  Colossians 3:15",
  "aud_full":"Church & Company \u2014 immediately practical; ideal for those facing real decisions.",
  "formats":"4-Session Series  \u00b7  21-Day Challenge  \u00b7  30-Day Devotional  \u00b7  40-Day Campaign",
  "bigidea":"A good decision isn\u2019t mostly about getting the right answer \u2014 it\u2019s about going to the right Source. Lean not on your own understanding, and the path straightens out.",
  "ideal":"Anyone facing a decision; young adults, leaders, and the chronically indecisive.",
  "pairs":"Knowing What to Do  \u00b7  God\u2019s Direction",
  "outcomes":["A repeatable way to decide","Less second-guessing","Peace in the decision"]},

 {"n":"04","title":"Knowing What to Do","pos":"Find clarity in the moments you genuinely don\u2019t know.",
  "felt":"Clarity in confusion","aud":"Church & Company",
  "summary":"A guidance campaign for the ache of not knowing \u2014 how God brings clarity and instruction when the right path simply isn\u2019t obvious.",
  "marketing":("Knowing What to Do meets people in the fog. It speaks to the specific ache of genuine confusion \u2014 when the answer "
     "isn\u2019t obvious and you\u2019re truly stuck \u2014 and shows how God instructs those who ask."),
  "problem":("Sometimes we\u2019re not avoiding the wise choice \u2014 we honestly can\u2019t see it. The options blur, the path forks into fog, "
     "and we\u2019re left stuck, anxious, and afraid of getting it wrong. We don\u2019t need more willpower; we need to be shown the way."),
  "transformation":("Participants learn to bring their genuine confusion to God \u2014 who promises to instruct and counsel \u2014 and to "
     "wait, watch, and walk forward in the clarity He gives, even when it comes one step at a time."),
  "sessions":[("When You Honestly Don\u2019t Know","Naming the fog without shame."),("I Will Instruct You","God\u2019s promise to the genuinely stuck."),
     ("Ask the One Who Knows","Bringing confusion to the right place."),("Clarity Comes in Steps","Why God often lights one step at a time."),
     ("Waiting Without Panicking","Trusting God\u2019s timing for the answer."),("Shown the Way","Moving forward in the light you\u2019re given.")],
  "scriptures":"James 1:5  \u00b7  Psalm 32:8  \u00b7  Psalm 25:4\u20135  \u00b7  Proverbs 3:6",
  "aud_full":"Church & Company \u2014 comforting for anyone facing a genuinely unclear decision.",
  "formats":"4-Session Series  \u00b7  21-Day Challenge  \u00b7  30-Day Devotional  \u00b7  40-Day Campaign",
  "bigidea":"God doesn\u2019t shame the confused \u2014 He instructs them. \u2018I will teach you the way you should go\u2019 is a promise made to people who honestly don\u2019t yet know it.",
  "ideal":"The stuck and uncertain; anyone in a genuinely unclear season.",
  "pairs":"Decide Well  \u00b7  God\u2019s Direction",
  "outcomes":["Clarity in confusing seasons","Freedom from decision paralysis","Confidence God will instruct"]},

 {"n":"05","title":"Discernment","pos":"Train your heart to tell not just good from bad, but good from best.",
  "felt":"Discernment & perception","aud":"Church & Company",
  "summary":"A discernment campaign on the trained skill of perceiving rightly \u2014 distinguishing wise from foolish, true from false, and good from best.",
  "marketing":("Discernment develops the most underrated skill in the Christian life: the trained ability to perceive what\u2019s "
     "really going on and to tell not just right from wrong, but good from best."),
  "problem":("Most of our hardest choices aren\u2019t between obvious good and obvious evil \u2014 they\u2019re between options that all look "
     "reasonable. Without discernment we\u2019re easily fooled by what merely seems right, and we settle for good when God was offering best."),
  "transformation":("Participants grow a discerning heart \u2014 trained by practice and the Spirit to see beneath the surface, test "
     "what they hear, and discern what is best \u2014 so they\u2019re no longer fooled by what only looks wise."),
  "sessions":[("When Everything Looks Right","The choices wisdom can\u2019t make on autopilot."),("A Discerning Heart","The gift Solomon asked for over riches."),
     ("Trained by Practice","How discernment is grown, not gifted."),("Good, or Best?","Discerning what is excellent, not just acceptable."),
     ("Testing the Spirits","Telling God\u2019s voice from the convincing counterfeits."),("Seeing Clearly","A heart that perceives what\u2019s really there.")],
  "scriptures":"Hebrews 5:14  \u00b7  1 Kings 3:9  \u00b7  Philippians 1:9\u201310  \u00b7  1 John 4:1",
  "aud_full":"Church & Company \u2014 deepens spiritual perception for all maturity levels.",
  "formats":"4-Session Series  \u00b7  21-Day Challenge  \u00b7  30-Day Devotional  \u00b7  40-Day Campaign",
  "bigidea":"The hardest decisions aren\u2019t good versus evil \u2014 they\u2019re good versus best. Discernment is the trained heart that can finally tell the difference.",
  "ideal":"Anyone facing reasonable-looking options; leaders and decision-makers.",
  "pairs":"Wise Decisions  \u00b7  Pathways of Wisdom",
  "outcomes":["A discerning, perceptive heart","Ability to tell good from best","Resistance to convincing counterfeits"]},

 {"n":"06","title":"Better Choices","pos":"See how today\u2019s small choices quietly become your life.",
  "felt":"Everyday choices","aud":"Church & Company",
  "summary":"A campaign on the cumulative power of everyday choices \u2014 how the small, ordinary decisions we barely notice compound into the shape of a life.",
  "marketing":("Better Choices reveals a quiet truth: a life is the sum of its choices. It helps people see the compounding "
     "weight of small, daily decisions and learn to choose well in the ordinary moments."),
  "problem":("We wait for the big, dramatic decisions to define us and barely notice the small ones \u2014 the daily, ordinary "
     "choices about what we do, watch, say, and pursue. But those are the ones quietly compounding into the people we\u2019re becoming."),
  "transformation":("Participants wake up to the weight of their everyday choices \u2014 that today\u2019s small decisions are sowing "
     "tomorrow\u2019s harvest \u2014 and learn to choose life, again and again, in the ordinary moments that actually shape a destiny."),
  "sessions":[("The Choices That Add Up","How small decisions quietly compound."),("Choose Life","The daily decision set before us."),
     ("You Reap What You Sow","The harvest hidden in today\u2019s choices."),("The Way That Seems Right","Why our instincts can mislead us."),
     ("One Better Choice","Changing a life one decision at a time."),("Becoming Who You Choose","The person your choices are forming.")],
  "scriptures":"Deuteronomy 30:19  \u00b7  Galatians 6:7\u20138  \u00b7  Proverbs 14:12  \u00b7  Joshua 24:15",
  "aud_full":"Church & Company \u2014 motivating and practical; great for habit and life change.",
  "formats":"4-Session Series  \u00b7  21-Day Challenge  \u00b7  30-Day Devotional  \u00b7  40-Day Campaign",
  "bigidea":"No one chooses a wasted life in a single decision. We choose it \u2014 or escape it \u2014 in a thousand small ones. Today\u2019s ordinary choice is quietly becoming tomorrow\u2019s harvest.",
  "ideal":"Anyone wanting real change; habit-formation and life-direction contexts.",
  "pairs":"Walking in Wisdom  \u00b7  The Wise Life",
  "outcomes":["Awareness of small choices\u2019 weight","Better everyday decisions","A life shaped on purpose"]},

 {"n":"07","title":"Wisdom for Real Life","pos":"Put wisdom to work where you actually live \u2014 on Monday.",
  "felt":"Applied wisdom","aud":"Church & Company",
  "summary":"An applied-wisdom campaign \u2014 the practical wisdom of Proverbs and James for the real arenas of work, words, relationships, and money.",
  "marketing":("Wisdom for Real Life brings wisdom down to where people actually live. Drawing on Proverbs and James, it applies "
     "God\u2019s wisdom to the everyday arenas of work, words, conflict, money, and relationships."),
  "problem":("We can love the idea of wisdom on Sunday and have no idea how it touches Monday \u2014 the tense conversation, the money "
     "decision, the difficult coworker, the words we wish we could take back. Wisdom stays abstract when we need it with skin on."),
  "transformation":("Participants learn to apply God\u2019s wisdom to the real arenas of life \u2014 their work, their words, their "
     "relationships, their money \u2014 discovering that the wisdom of Proverbs and James is astonishingly practical when it\u2019s actually put to work."),
  "sessions":[("Wisdom with Skin On","Faith that touches Monday morning."),("Wisdom for Your Words","Taming the most untamable thing."),
     ("Wisdom for Your Work","Diligence, integrity, and rest."),("Wisdom for Your Relationships","Conflict, counsel, and company."),
     ("Wisdom for Your Money","What Proverbs knows about your wallet."),("Wisdom That Shows","A good life that proves its wisdom.")],
  "scriptures":"James 3:13  \u00b7  Proverbs 16:24  \u00b7  Colossians 3:23  \u00b7  Proverbs 13:20",
  "aud_full":"Church & Company \u2014 broad, practical appeal; strong for marketplace audiences.",
  "formats":"4-Session Series  \u00b7  21-Day Challenge  \u00b7  30-Day Devotional  \u00b7  40-Day Campaign",
  "bigidea":"Real wisdom isn\u2019t proved in a debate; it\u2019s proved in a life. As James says, show your wisdom by your good life \u2014 in your words, your work, and the way you treat people.",
  "ideal":"Marketplace audiences; anyone wanting wisdom that touches everyday life.",
  "pairs":"Walking in Wisdom  \u00b7  Better Choices",
  "outcomes":["Wisdom applied to real life","Wiser words, work, and relationships","Faith that touches Monday"]},

 {"n":"08","title":"The Wise Life","pos":"Build a life that still stands when the storms come.",
  "felt":"A life built on wisdom","aud":"Church & Company",
  "summary":"A life-building campaign on the wise vs. foolish builder \u2014 wisdom as the long work of constructing a life that endures.",
  "marketing":("The Wise Life lifts wisdom from single decisions to the whole architecture of a life. Drawing on the wise and "
     "foolish builders, it casts a vision for a life constructed to stand when the storms come."),
  "problem":("Two builders, two houses, identical on the outside \u2014 until the storm. Jesus said the difference wasn\u2019t talent or "
     "appearance, but foundation. Many of us are building impressive lives on sand, and we won\u2019t know it until the rains test what we\u2019ve made."),
  "transformation":("Participants step back from the next decision to the whole structure of their lives \u2014 learning to build on "
     "the rock of Christ\u2019s words, by wisdom, so their house stands firm when the inevitable storms arrive."),
  "sessions":[("Two Builders, One Storm","Why some lives stand and others fall."),("Built on the Rock","The foundation that doesn\u2019t shift."),
     ("By Wisdom a House Is Built","The slow, faithful work of building well."),("Number Your Days","Letting mortality make you wise."),
     ("The Storms Will Come","Building for the test, not just the photo."),("A Life That Stands","Wisdom built to last a lifetime.")],
  "scriptures":"Matthew 7:24\u201327  \u00b7  Proverbs 24:3\u20134  \u00b7  Psalm 90:12  \u00b7  Proverbs 9:1",
  "aud_full":"Church & Company \u2014 a vision-casting campaign about the whole shape of a life.",
  "formats":"4-Session Series  \u00b7  21-Day Challenge  \u00b7  30-Day Devotional  \u00b7  40-Day Campaign",
  "bigidea":"Two lives can look identical until the storm. The wise life isn\u2019t the most impressive one \u2014 it\u2019s the one built, decision by decision, on the rock that holds.",
  "ideal":"Anyone thinking about the long arc of their life; all maturity levels.",
  "pairs":"Better Choices  \u00b7  Pathways of Wisdom",
  "outcomes":["A life built to endure","Wisdom as long-term construction","A foundation that holds in storms"]},

 {"n":"09","title":"God\u2019s Direction","pos":"Trust the God who directs your steps even as you plan.",
  "felt":"Direction & guidance","aud":"Church & Company",
  "summary":"A guidance campaign on life direction \u2014 trusting God to establish your steps and lead the overall course of your life at its bigger crossroads.",
  "marketing":("God\u2019s Direction speaks to the bigger question behind our decisions: where is my life going? It teaches people to "
     "plan thoughtfully while trusting the God who promises to direct their steps."),
  "problem":("Beneath our daily choices runs a bigger ache: where is my life actually heading? We plan and strive and worry over "
     "the trajectory, gripping the wheel \u2014 and quietly forget the promise that, while we plan our course, it\u2019s the Lord who establishes our steps."),
  "transformation":("Participants learn to hold their plans with open hands \u2014 planning wisely while trusting God to direct the "
     "larger course of their lives \u2014 and find peace in the One who guides their steps even when the whole road isn\u2019t visible."),
  "sessions":[("Where Is My Life Going?","The bigger question under our decisions."),("We Plan, He Directs","The partnership of Proverbs 16:9."),
     ("Show Me Your Ways","Asking God for direction, not just answers."),("Open and Closed Doors","Reading God\u2019s leading without superstition."),
     ("Directed, Not Driven","Trading anxious striving for trust."),("He Directs My Steps","A life confidently led by God.")],
  "scriptures":"Proverbs 16:9  \u00b7  Psalm 25:4\u20135  \u00b7  Proverbs 3:6  \u00b7  Jeremiah 29:11",
  "aud_full":"Church & Company \u2014 grounding for those wrestling with life direction.",
  "formats":"4-Session Series  \u00b7  21-Day Challenge  \u00b7  30-Day Devotional  \u00b7  40-Day Campaign",
  "bigidea":"You\u2019re free to plan your course \u2014 you\u2019re just not in charge of establishing your steps. And that\u2019s the most freeing arrangement there is: you plan, He directs.",
  "ideal":"Those at major crossroads; anyone anxious about their life\u2019s direction.",
  "pairs":"Knowing What to Do  \u00b7  Decide Well",
  "outcomes":["Peace about life direction","Plans held with open hands","Trust in God to direct steps"]},

 {"n":"10","title":"Pathways of Wisdom","pos":"Step onto the road whose every path leads to peace.",
  "felt":"The path of wisdom","aud":"Church & Company",
  "summary":"A capstone campaign on the way of wisdom \u2014 Proverbs\u2019 two roads, and the pleasant, peaceful, light-filled path Wisdom calls us to walk.",
  "marketing":("Pathways of Wisdom is the category\u2019s capstone, drawing on the road imagery of Proverbs: two ways lie before us, "
     "and Wisdom calls us onto her paths \u2014 the road that grows brighter and ends in peace and life."),
  "problem":("Proverbs keeps picturing two roads \u2014 the way of wisdom and the way of folly \u2014 and we keep imagining wisdom\u2019s road "
     "must be the harder, grimmer one. But Scripture insists the opposite: wisdom\u2019s ways are pleasant, and all her paths are peace. We\u2019ve been avoiding the very road that leads home."),
  "transformation":("Participants are invited onto the path of wisdom \u2014 the road Proverbs calls pleasant, peaceful, and "
     "ever-brightening \u2014 learning to choose Wisdom\u2019s way at every fork until the whole direction of their lives bends toward life."),
  "sessions":[("Two Roads","The choice Proverbs sets before every one of us."),("Her Paths Are Peace","Why wisdom\u2019s way is the pleasant one."),
     ("The Path That Brightens","A road that grows lighter to the dawn."),("At Every Fork","Choosing wisdom\u2019s way again and again."),
     ("The Company on the Road","Walking the path with the wise."),("The Road Home","Where the way of wisdom finally leads.")],
  "scriptures":"Proverbs 3:17  \u00b7  Proverbs 4:18  \u00b7  Proverbs 4:11\u201312  \u00b7  Matthew 7:13\u201314",
  "aud_full":"Church & Company \u2014 an inspiring capstone to the wisdom journey.",
  "formats":"4-Session Series  \u00b7  21-Day Challenge  \u00b7  30-Day Devotional  \u00b7  40-Day Campaign",
  "bigidea":"We imagine wisdom\u2019s road is the hard, joyless one. Scripture says the opposite: her ways are pleasant, and all her paths are peace. It was always the road home.",
  "ideal":"Anyone choosing their life\u2019s direction; a fitting close to the category.",
  "pairs":"Discernment  \u00b7  The Wise Life",
  "outcomes":["A vision of wisdom\u2019s path","Confidence wisdom leads to peace","Choosing wisdom\u2019s way at every fork"]},
 ],

 "library":[
  ("Foundations of Wisdom", [
    ("Wise Decisions","T2",True),("The Beginning of Wisdom","T2",False),("The Fear of the Lord","T2",False),
    ("Get Wisdom","T2",False),("Wisdom from Above","T2",False),("Christ Our Wisdom","T2",False),
    ("Ask for Wisdom","T2",False),("Wiser Than Solomon","T2",False),("The Worth of Wisdom","T2",False),
    ("Foundations of Wisdom","T2",False)]),
  ("Walking Wisely Each Day", [
    ("Walking in Wisdom","T2",True),("Watch How You Walk","T2",False),("Wise in the Ordinary","T2",False),
    ("Redeeming the Time","T2",False),("The Wise Routine","T2",False),("Numbering Your Days","T2",False),
    ("Everyday Wisdom","T2",False),("Wisdom for Today","T2",False),("In Step with Wisdom","T2",False),
    ("The Careful Walk","T2",False)]),
  ("Making Wise Decisions", [
    ("Decide Well","T2",True),("The Decision-Making Guide","T2",False),("Lean Not on Your Own","T2",False),
    ("Before You Decide","T2",False),("Crossroads","T2",False),("The Wisdom to Choose","T2",False),
    ("Counsel and Clarity","T2",False),("Weighing the Options","T2",False),("Decide and Move","T2",False),
    ("No More Second-Guessing","T2",False)]),
  ("Guidance & Knowing God\u2019s Will", [
    ("Knowing What to Do","T2",True),("I Will Instruct You","T2",False),("Finding God\u2019s Will","T2",False),
    ("When You Don\u2019t Know","T2",False),("Clarity in the Fog","T2",False),("Show Me Your Way","T2",False),
    ("The God Who Guides","T2",False),("Guidance for the Stuck","T2",False),("Wisdom When It\u2019s Unclear","T2",False),
    ("Led by God","T2",False)]),
  ("Discernment & Insight", [
    ("Discernment","T2",True),("A Discerning Heart","T2",False),("Good or Best?","T2",False),
    ("Seeing Clearly","T2",False),("Testing the Spirits","T2",False),("Trained to Discern","T2",False),
    ("The Gift of Insight","T2",False),("Beneath the Surface","T2",False),("What Is Best","T2",False),
    ("Wisdom to Perceive","T2",False)]),
  ("Choices & Consequences", [
    ("Better Choices","T2",True),("Choose Life","T2",False),("You Reap What You Sow","T2",False),
    ("The Power of a Choice","T2",False),("Small Choices, Big Life","T2",False),("The Way That Seems Right","T2",False),
    ("Choices That Last","T2",False),("One Decision Away","T2",False),("Sowing and Reaping","T2",False),
    ("Choosing Well","T2",False)]),
  ("Wisdom for Everyday Life", [
    ("Wisdom for Real Life","T2",True),("Wisdom for Your Words","T2",False),("Wisdom for Your Work","T2",False),
    ("Wisdom for Your Relationships","T2",False),("Wisdom for Your Money","T2",False),("Wisdom with Skin On","T2",False),
    ("The Wisdom of Proverbs","T2",False),("Practical Wisdom","T2",False),("Wisdom for Hard Conversations","T2",False),
    ("Street-Level Wisdom","T2",False)]),
  ("Building a Wise Life", [
    ("The Wise Life","T2",True),("Built on the Rock","T2",False),("Two Builders","T2",False),
    ("By Wisdom a House Is Built","T2",False),("A Life That Stands","T2",False),("The Wise and the Foolish","T2",False),
    ("Foundations That Hold","T2",False),("Building Well","T2",False),("Wisdom for a Lifetime","T2",False),
    ("The House Wisdom Builds","T2",False)]),
  ("God\u2019s Direction & Your Path", [
    ("God\u2019s Direction","T2",True),("He Directs My Steps","T2",False),("We Plan, He Directs","T2",False),
    ("Where Is My Life Going?","T2",False),("Open and Closed Doors","T2",False),("Directed, Not Driven","T2",False),
    ("Trusting the Path","T2",False),("Plans and Providence","T2",False),("Finding Your Way","T2",False),
    ("Led Step by Step","T2",False)]),
  ("The Way of Wisdom", [
    ("Pathways of Wisdom","T2",True),("Her Paths Are Peace","T2",False),("Two Roads","T2",False),
    ("The Path That Brightens","T2",False),("The Way of Wisdom","T2",False),("Wisdom\u2019s Invitation","T2",False),
    ("The Road Home","T2",False),("At Every Fork","T2",False),("The Brighter Way","T2",False),
    ("Walking Wisdom\u2019s Road","T2",False)]),
 ],
}

doc, npages = build_catalog(cfg)
pathlib.Path("/tmp/wisdom_catalog.html").write_text(doc, encoding="utf-8")
render_pdf("/tmp/wisdom_catalog.html", "/tmp/wisdom_catalog.pdf")
print("Wisdom catalog:", npages, "pages")
