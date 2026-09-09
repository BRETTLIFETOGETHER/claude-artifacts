# -*- coding: utf-8 -*-
import pathlib
from catalog_engine import build_catalog, render_pdf

cfg = {
 "category":"Generosity",
 "doc_title":"Generosity Campaign Collection",
 "accent":"#1d6473",   # generosity deep teal
 "accent2":"#c19a4b",
 "positioning":("A complete library of 100 ready-to-run generosity campaigns that move churches, companies, and "
   "families from holding back to giving freely \u2014 into open-handed, joyful, courageous generosity that changes them "
   "and the world around them."),
 "why_matters":("Generosity is one of the clearest marks of a transformed heart and one of the most joy-producing habits "
   "in all of Scripture \u2014 yet it remains the area where the gap between belief and behavior is widest. Money grips quietly, "
   "and most people give reluctantly, if at all. A church that disciples generosity well unlocks not only resources for the "
   "mission, but freedom, joy, and trust in its people."),
 "core_problem":("Most people want to be generous and aren\u2019t \u2014 held back by fear, scarcity thinking, a tight grip, or simply "
   "never having been taught the joy of giving. Their generosity stays occasional, reluctant, and small. Leaders long to grow "
   "a culture of joyful generosity but have few resources that go beyond the annual giving appeal."),
 "transformation":("These campaigns move people from holding back to giving freely \u2014 in their hearts, their habits, and their "
   "whole way of life \u2014 until open-handed, courageous, joyful generosity becomes who they are."),
 "who_needs":[
   ("Churches","A complete generosity pathway that disciples the heart, not just the offering \u2014 joyful, biblical, and culture-shaping."),
   ("Companies","A values-rich framework for generosity, gratitude, and giving-back that strengthens any team or culture."),
   ("Advisors &amp; Donors","A compelling vision of joyful, purposeful generosity to share with clients and giving partners."),
   ("Families","A way to raise open-handed, generous children and build a household marked by giving."),
 ],
 "outcomes":[
   "A shift from reluctant to cheerful, joyful giving",
   "Greater freedom from the grip of money and fear",
   "Increased giving and engagement across the body",
   "Generosity beyond money \u2014 time, words, grace, hospitality",
   "A culture of gratitude, abundance, and open hands",
   "Lives marked by lasting, contagious generosity",
 ],
 "use_cases":[
   ("Churchwide Generosity Series","A heart-level series that goes far beyond the annual giving appeal."),
   ("40-Day Spiritual Campaign","A full-church journey with weekend messages, small groups, and daily readings."),
   ("21-Day Giving Challenge","A short, high-engagement generosity and gratitude experience for a church or team."),
   ("4-Week Sermon Companion","A focused message series with sermon-aligned small-group guides."),
   ("Advisor &amp; Donor Resource","A premium resource gifted to clients, partners, and giving supporters."),
 ],
 "stats":[("100","Campaigns"),("10","Expanded"),("10","Themes"),("4","Formats"),("NIV","Scripture")],
 "components":["Daily Readings & Reflections","Six Group-Session Guides","Weekend Message Outlines",
               "Spiritual-Partner Prompts","Launch & Promotion Kit"],

 "top10":[
 {"n":"01","title":"Generous Living","pos":"Make generosity a whole way of life \u2014 a river, not a reservoir.",
  "felt":"Lifestyle giving","aud":"Church & Company",
  "summary":"A foundational campaign that reframes generosity as an identity and a way of life rather than an occasional act \u2014 a river that flows rather than a reservoir that hoards.",
  "marketing":("The flagship entry point for the category. Generous Living lifts giving out of the occasional and into the "
     "everyday, reframing generosity as someone you become rather than something you do."),
  "problem":("We instinctively treat money and resources like a reservoir \u2014 something to dam up, guard, and slowly accumulate. "
     "But reservoirs grow stagnant, and a life organized around keeping rarely produces the joy it quietly promises."),
  "transformation":("Participants learn to live as conduits rather than containers \u2014 letting God\u2019s provision flow through them "
     "to others \u2014 and discover the strange math of the kingdom, where the refreshed are those who refresh."),
  "sessions":[("Reservoir or River?","Two ways to relate to everything you have."),("The Stagnation of Keeping","Why a life built on holding goes stale."),
     ("Becoming a Conduit","Letting God\u2019s provision flow through you."),("The Kingdom\u2019s Strange Math","How giving leads to gaining."),
     ("Refreshed by Refreshing","The joy only generosity unlocks."),("A Generous Life","Living as a river, not a reservoir.")],
  "scriptures":"Proverbs 11:24\u201325  \u00b7  Luke 6:38  \u00b7  2 Corinthians 9:6  \u00b7  Proverbs 22:9",
  "aud_full":"Church & Company \u2014 the ideal on-ramp to the entire generosity category.",
  "formats":"4-Session Series  \u00b7  21-Day Challenge  \u00b7  30-Day Devotional  \u00b7  40-Day Campaign (recommended)",
  "bigidea":"Generosity isn\u2019t something you do; it\u2019s someone you become. The generous life is a river, not a reservoir \u2014 and rivers are the only water that stays fresh.",
  "ideal":"All-church on-ramps, new believers, and anyone whose giving has stayed occasional.",
  "pairs":"Open Hands  \u00b7  Living Generously",
  "outcomes":["Generosity as a way of life","A conduit, not a container","More joy and less grip"]},

 {"n":"02","title":"Open Hands","pos":"Become the cheerful giver God actually delights in.",
  "felt":"Cheerful giving","aud":"Church & Company",
  "summary":"A heart-posture campaign that moves people from reluctant, pressured giving to the cheerful, freehearted generosity God loves.",
  "marketing":("Open Hands is about the heart behind the gift. It moves people past guilt-driven, calculated giving into the "
     "glad, decided generosity Scripture says God actually delights in."),
  "problem":("Plenty of us give \u2014 but with a closed heart even when our hands are open. We give reluctantly, out of guilt or "
     "pressure, calculating the minimum, half-resenting the ask \u2014 and miss almost the entire point."),
  "transformation":("Participants move from reluctant, pressured giving to cheerful, freehearted generosity \u2014 discovering the "
     "sow-and-reap rhythm of God\u2019s economy and the deep gladness of giving on purpose."),
  "sessions":[("The Reluctant Giver","Why grudging generosity misses the point."),("A Cheerful Heart","The kind of giver God loves."),
     ("Sow and Reap","The rhythm of God\u2019s economy."),("Decided in the Heart","From pressure to intentional giving."),
     ("No Strings Attached","Giving freely, expecting no return."),("The Glad Hand","A heart as open as your hand.")],
  "scriptures":"2 Corinthians 9:6\u20138  \u00b7  Luke 6:38  \u00b7  Proverbs 11:25  \u00b7  Deuteronomy 15:10",
  "aud_full":"Church & Company \u2014 a heart-level reset that reshapes the motive behind giving.",
  "formats":"4-Session Series  \u00b7  21-Day Challenge  \u00b7  30-Day Devotional  \u00b7  40-Day Campaign",
  "bigidea":"God isn\u2019t only interested in what leaves your hand. He\u2019s interested in what\u2019s happening in your heart while it does. The open hand and the cheerful heart belong together.",
  "ideal":"Dutiful, reluctant, or pressured givers ready to find the joy in it.",
  "pairs":"Generous Living  \u00b7  Crazy Generosity",
  "outcomes":["Cheerful, freehearted giving","Freedom from guilt-driven giving","Joy in the act of giving"]},

 {"n":"03","title":"Crazy Generosity","pos":"Dare to give past sensible \u2014 the way Scripture celebrates.",
  "felt":"Radical generosity","aud":"Church & Company",
  "summary":"A radical-giving campaign that calls people past safe and sensible into the extravagant, sacrificial generosity Scripture celebrates.",
  "marketing":("Crazy Generosity dares people past the safe and the sensible into the kind of extravagant, faith-filled giving "
     "the world calls foolish and heaven calls beautiful."),
  "problem":("Most of our giving is safe, sensible, and small \u2014 generous enough to feel good but never enough to feel it. But "
     "the generosity Scripture celebrates is almost reckless: the widow\u2019s coins, the broken jar, churches giving beyond their means."),
  "transformation":("Participants are invited into extravagant, joyful, faith-filled giving \u2014 the kind that changes the giver "
     "as much as the gift changes the world."),
  "sessions":[("The Trouble with Sensible","Why safe giving rarely changes anything."),("Beyond Their Ability","The reckless Macedonian generosity."),
     ("The Widow\u2019s Everything","When the smallest gift is the largest."),("Breaking the Jar","Extravagance that is actually worship."),
     ("The Joy of Going Too Far","Why over-the-top giving brings over-the-top joy."),("A Crazy-Generous Church","Known for giving beyond reason.")],
  "scriptures":"2 Corinthians 8:1\u20135  \u00b7  Mark 12:41\u201344  \u00b7  Mark 14:3\u20139  \u00b7  2 Corinthians 9:7",
  "aud_full":"Church & Company \u2014 a faith-stretching campaign, powerful for giving initiatives.",
  "formats":"4-Session Series  \u00b7  21-Day Challenge  \u00b7  30-Day Devotional  \u00b7  40-Day Campaign",
  "bigidea":"Sensible generosity rarely changes anyone. It\u2019s the \u2018crazy\u2019 gift \u2014 the one that costs, that surprises, that makes no financial sense \u2014 that breaks something open in us and in the world.",
  "ideal":"Believers ready to stretch; strong fuel for a generosity or capital initiative.",
  "pairs":"Open Hands  \u00b7  Courageous Generosity",
  "outcomes":["Faith-stretching, sacrificial giving","A taste of extravagant joy","A bolder generosity culture"]},

 {"n":"04","title":"Living Generously","pos":"Be generous with everything \u2014 not just money.",
  "felt":"Everyday generosity","aud":"Church & Company",
  "summary":"A breadth campaign that expands generosity beyond money to time, words, grace, hospitality, and encouragement.",
  "marketing":("Living Generously expands the whole idea \u2014 showing that the most generous people give freely not just with "
     "money, but with their time, words, grace, and welcome."),
  "problem":("When we hear \u2018generosity,\u2019 we almost always think money. But some of the stingiest people are generous with "
     "their checkbooks and miserly with everything else \u2014 their time, patience, praise, forgiveness, and welcome."),
  "transformation":("Participants learn to be generous in everything \u2014 time, words, hospitality, grace, encouragement \u2014 until "
     "generosity becomes the way they treat every person they meet."),
  "sessions":[("More Than Money","Why generosity is bigger than your account."),("Generous with Time","The gift of unhurried presence."),
     ("Generous with Words","Lavish with encouragement and praise."),("Generous with Grace","Forgiving freely, assuming the best."),
     ("Generous with Welcome","Opening your table and home."),("A Generous Way of Life","Open-handed with everyone.")],
  "scriptures":"Luke 6:38  \u00b7  Romans 12:13  \u00b7  1 Timothy 6:18  \u00b7  Acts 20:35",
  "aud_full":"Church & Company \u2014 broad appeal; a generosity everyone can practice today.",
  "formats":"4-Session Series  \u00b7  21-Day Challenge  \u00b7  30-Day Devotional  \u00b7  40-Day Campaign",
  "bigidea":"Generosity was never meant to stop at money. The most generous people give freely with their time, their words, and their grace \u2014 everything they have, not just everything in their account.",
  "ideal":"Everyone \u2014 especially those who think they can\u2019t afford to be generous.",
  "pairs":"Generous Living  \u00b7  The Blessed Life",
  "outcomes":["Generosity beyond money","More generous relationships","A generous spirit in everyday life"]},

 {"n":"05","title":"Courageous Generosity","pos":"Give boldly, before you feel ready, and trust God.",
  "felt":"Faith over fear","aud":"Church & Company",
  "summary":"A faith campaign that confronts the fear beneath holding back and builds the courage to give and trust God\u2019s provision.",
  "marketing":("Courageous Generosity names the real barrier to giving \u2014 fear \u2014 and confronts it with faith, helping people "
     "give before they feel ready and trust the God who provides."),
  "problem":("For many of us, the real barrier to generosity isn\u2019t selfishness \u2014 it\u2019s fear. Fear that there won\u2019t be enough, "
     "fear of the future, fear of giving and regretting it. So we hold back and wait for a security that never quite arrives."),
  "transformation":("Participants learn to give before they feel ready \u2014 taking Scripture\u2019s startling invitation to test God\u2019s "
     "faithfulness \u2014 and discover that the God who multiplied a widow\u2019s last meal can be trusted with their generosity too."),
  "sessions":[("The Fear Beneath the Wallet","What really keeps us from giving."),("The Widow\u2019s Last Meal","When giving from lack becomes a miracle."),
     ("Test Me in This","Scripture\u2019s bold invitation to trust."),("First, Not Last","Generosity at the front of the budget."),
     ("Giving Before You\u2019re Ready","The courage to give ahead of certainty."),("The God Who Provides","Unshakable confidence in His faithfulness.")],
  "scriptures":"Malachi 3:10  \u00b7  1 Kings 17:8\u201316  \u00b7  2 Corinthians 9:8  \u00b7  Philippians 4:19",
  "aud_full":"Church & Company \u2014 includes gentle pastoral framing; powerful in tight seasons.",
  "formats":"4-Session Series  \u00b7  21-Day Challenge  \u00b7  30-Day Devotional  \u00b7  40-Day Campaign",
  "bigidea":"Generosity almost always requires courage, because it almost always comes before certainty. Faith gives first and trusts God for the rest.",
  "ideal":"The fearful and the scarcity-minded; those who want to give but feel they can\u2019t.",
  "pairs":"Crazy Generosity  \u00b7  Abundance",
  "outcomes":["Courage to give against fear","Confidence in God\u2019s provision","Faith-filled, first-fruits giving"]},

 {"n":"06","title":"The Generosity Journey","pos":"Grow, step by step, into a generous life.",
  "felt":"Growth & process","aud":"Church & Company",
  "summary":"A growth campaign that treats generosity as a journey to walk, not a switch to flip \u2014 meeting people wherever they are and moving them forward.",
  "marketing":("The Generosity Journey gives people a path to walk. It meets them wherever they are and moves them, one faithful "
     "step at a time, toward the generous life God is calling them into."),
  "problem":("Almost no one becomes generous overnight, yet we treat generosity like a switch we should already have flipped. "
     "When our giving doesn\u2019t match our ideals, we feel guilty, stall out, and quietly give up."),
  "transformation":("Participants move from wherever they are toward where God is calling them \u2014 taking the next faithful step, "
     "then the next \u2014 discovering that generosity, like any grace, is something you grow into over time."),
  "sessions":[("Wherever You Are","Generosity as a starting line, not a standard."),("The Next Faithful Step","Growth, not perfection, is the goal."),
     ("Excel in This Grace","Treating giving as a grace you can grow in."),("Past the Plateaus","Pushing through where generosity stalls."),
     ("Companions on the Road","Growing in generosity together."),("The Long Walk Home","Staying on the journey for a lifetime.")],
  "scriptures":"2 Corinthians 8:7  \u00b7  Philippians 1:6  \u00b7  2 Corinthians 9:6  \u00b7  Proverbs 11:25",
  "aud_full":"Church & Company \u2014 a gentle, guilt-free on-ramp for all giving levels.",
  "formats":"4-Session Series  \u00b7  21-Day Challenge  \u00b7  30-Day Devotional  \u00b7  40-Day Campaign",
  "bigidea":"Generosity isn\u2019t a switch you flip; it\u2019s a road you walk. You don\u2019t have to arrive today \u2014 you only have to take the next step.",
  "ideal":"Mixed-maturity congregations; anyone discouraged by the gap between ideal and reality.",
  "pairs":"Generous Living  \u00b7  Generosity Changes Everything",
  "outcomes":["A clear next step in giving","Growth without guilt","Momentum over time"]},

 {"n":"07","title":"Generosity Changes Everything","pos":"See the ripple effect of a single generous act.",
  "felt":"Impact & ripple","aud":"Church & Company",
  "summary":"An impact campaign that opens people\u2019s eyes to how a single generous act ripples outward \u2014 changing the giver, the receiver, and the world.",
  "marketing":("Generosity Changes Everything reveals the ripple. It shows how a single gift transforms not just budgets but "
     "hearts, families, churches, and communities \u2014 far beyond what the giver will ever see."),
  "problem":("We tend to think of a gift as a transaction \u2014 money leaves one hand and lands in another, and that\u2019s the end of "
     "it. But generosity is never that contained; a single act sets off ripples that travel further than we\u2019ll ever see."),
  "transformation":("Participants discover how giving transforms the giver first, then ripples outward through people and "
     "places they\u2019ll never meet \u2014 and find their place in something far larger than themselves."),
  "sessions":[("More Than a Transaction","Why a gift never stops where it lands."),("Changed by Giving","How generosity transforms the giver first."),
     ("The Ripple Outward","The unexpected reach of a single gift."),("A Generous Church","What happens when a community gives."),
     ("Generosity Is Contagious","How one open hand opens others."),("Part of Something Bigger","Joining the work God is doing.")],
  "scriptures":"2 Corinthians 9:10\u201313  \u00b7  Luke 6:38  \u00b7  Acts 20:35  \u00b7  Proverbs 11:25",
  "aud_full":"Church & Company \u2014 inspiring and vision-casting; great for building momentum.",
  "formats":"4-Session Series  \u00b7  21-Day Challenge  \u00b7  30-Day Devotional  \u00b7  40-Day Campaign",
  "bigidea":"A gift is never just a gift. Generosity changes the giver first, then ripples outward through people and places you\u2019ll never even meet.",
  "ideal":"Congregations needing vision and momentum for a giving culture.",
  "pairs":"The Generosity Journey  \u00b7  The Blessed Life",
  "outcomes":["A vision for generosity\u2019s impact","A more contagious giving culture","Joy in being part of something bigger"]},

 {"n":"08","title":"Abundance","pos":"Trade the fear of scarcity for the confidence of enough.",
  "felt":"Abundance over scarcity","aud":"Church & Company",
  "summary":"A mindset campaign that confronts the scarcity lie and replaces it with confidence in a God who provides abundantly \u2014 which finally frees generosity.",
  "marketing":("Abundance confronts the scarcity lie that quietly shrinks our giving, replacing it with the loaves-and-fishes "
     "confidence that finally sets generosity free."),
  "problem":("Underneath a lot of tight-fisted living is one quiet belief: there isn\u2019t enough, and there won\u2019t be. Scarcity "
     "thinking tells us to hoard, to fear, to grip a little tighter \u2014 and it slowly shrinks our generosity and our peace."),
  "transformation":("Participants learn to see the world the way Jesus did \u2014 where five loaves feed thousands and baskets are "
     "left over \u2014 and discover that a settled confidence in God\u2019s provision is what finally frees generosity."),
  "sessions":[("The Scarcity Lie","The fear that quietly shapes our giving."),("Loaves and Fishes","How God multiplies what we offer."),
     ("Enough, and More","Trusting the God who provides."),("Open-Handed in Abundance","Why confidence frees generosity."),
     ("The Math of Heaven","Where less, given to God, becomes more."),("Living from Plenty","An abundance mindset in everyday life.")],
  "scriptures":"Philippians 4:19  \u00b7  John 6:1\u201313  \u00b7  2 Corinthians 9:8  \u00b7  Matthew 6:31\u201333",
  "aud_full":"Church & Company \u2014 reframes the inner story that drives giving decisions.",
  "formats":"4-Session Series  \u00b7  21-Day Challenge  \u00b7  30-Day Devotional  \u00b7  40-Day Campaign",
  "bigidea":"Scarcity says \u2018give carefully, there may not be enough.\u2019 Abundance says \u2018give freely, because the God who feeds thousands from a few loaves has you covered.\u2019",
  "ideal":"Scarcity-minded givers; anyone whose fear of lack holds them back.",
  "pairs":"Courageous Generosity  \u00b7  Overflow",
  "outcomes":["Freedom from scarcity thinking","Confidence in God\u2019s provision","Generosity that flows from trust"]},

 {"n":"09","title":"The Blessed Life","pos":"Discover that the truly blessed life is the generous one.",
  "felt":"Blessed to bless","aud":"Church & Company",
  "summary":"A purpose campaign that redefines \u2018blessed\u2019 \u2014 showing that God\u2019s blessings were meant to flow through us, not stop with us.",
  "marketing":("The Blessed Life redefines the word everyone uses and few understand \u2014 revealing that we\u2019re blessed in order to "
     "bless, and that the truly good life is the generous one."),
  "problem":("We use the word \u2018blessed\u2019 constantly, and we almost always mean received \u2014 what we\u2019ve been given, what we get to "
     "enjoy. But Scripture keeps pointing elsewhere: that we\u2019re blessed in order to bless, and the good life isn\u2019t accumulating blessings but becoming one."),
  "transformation":("Participants learn that God\u2019s blessings were never meant to terminate on them \u2014 they were meant to flow "
     "through them \u2014 and discover the deep, surprising joy of a life spent being a blessing to others."),
  "sessions":[("What \u2018Blessed\u2019 Really Means","Recovering the word from sentimentality."),("Blessed to Bless","Why God\u2019s gifts keep moving."),
     ("The Reservoir Problem","What happens when blessing stops with us."),("A Channel of Grace","Becoming the means of another\u2019s blessing."),
     ("The Joy of Being a Blessing","The gladness of giving forward."),("A Truly Blessed Life","Living as a conduit of God\u2019s goodness.")],
  "scriptures":"Genesis 12:1\u20133  \u00b7  Acts 20:35  \u00b7  Luke 6:38  \u00b7  2 Corinthians 9:8",
  "aud_full":"Church & Company \u2014 a purpose-rich reframe of what it means to be blessed.",
  "formats":"4-Session Series  \u00b7  21-Day Challenge  \u00b7  30-Day Devotional  \u00b7  40-Day Campaign",
  "bigidea":"You weren\u2019t blessed to be a reservoir of God\u2019s goodness \u2014 you were blessed to be a channel of it. The blessed life and the generous life are the same life.",
  "ideal":"Those who feel blessed and want their lives to matter for others.",
  "pairs":"Living Generously  \u00b7  Generosity Changes Everything",
  "outcomes":["A redefined view of blessing","A blessed-to-bless purpose","Joy in giving forward"]},

 {"n":"10","title":"Overflow","pos":"Give from a heart so full it spills onto others.",
  "felt":"Giving from fullness","aud":"Church & Company",
  "summary":"A fullness campaign that teaches generosity as the natural overflow of a heart filled by God \u2014 not a duty ground out from empty.",
  "marketing":("Overflow flips the order of generosity \u2014 teaching people to be filled by God first, so that giving stops being "
     "a duty they grind out and becomes the natural overflow of a grateful heart."),
  "problem":("A lot of us try to give from empty. Depleted, stretched, running on fumes, we squeeze out generosity by willpower "
     "\u2014 and it shows. Forced giving is joyless and short-lived, because you can\u2019t pour from a cup with nothing left in it."),
  "transformation":("Participants learn to be filled first \u2014 by God\u2019s love, presence, and provision \u2014 until generosity becomes "
     "the natural overflow of a full and grateful heart that simply spills onto everyone around them."),
  "sessions":[("Giving from Empty","Why willpower generosity runs dry."),("Filled First","Receiving God\u2019s love before pouring out."),
     ("The Overflowing Cup","What happens when gratitude runs over."),("Joy That Spills","How a full heart gives almost by accident."),
     ("Staying Full","Habits that keep the cup running over."),("A Life of Overflow","Generosity as the spill of a grateful life.")],
  "scriptures":"2 Corinthians 8:2  \u00b7  Psalm 23:5  \u00b7  John 7:38  \u00b7  Luke 6:45",
  "aud_full":"Church & Company \u2014 restorative; ideal for the depleted and burned-out giver.",
  "formats":"4-Session Series  \u00b7  21-Day Challenge  \u00b7  30-Day Devotional  \u00b7  40-Day Campaign",
  "bigidea":"You can\u2019t pour from an empty cup. The most generous people aren\u2019t the most disciplined \u2014 they\u2019re the most full. Generosity is meant to be an overflow, not an effort.",
  "ideal":"The depleted and weary; anyone giving from duty rather than fullness.",
  "pairs":"Abundance  \u00b7  The Blessed Life",
  "outcomes":["Generosity from fullness, not duty","A filled and grateful heart","Joyful, sustainable giving"]},
 ],

 "library":[
  ("Foundations of Generosity", [
    ("Generous Living","T1",True),("The Generous Life","T1",False),("A Lifestyle of Giving","T1",False),
    ("Becoming Generous","T2",False),("The River, Not the Reservoir","T2",False),("Giving as a Way of Life","T2",False),
    ("Open-Handed Living","T2",False),("First Steps in Generosity","T2",False),("Why We Give","T2",False),
    ("The Generous Disciple","T2",False)]),
  ("The Generous Heart", [
    ("Open Hands","T1",True),("The Cheerful Giver","T1",False),("A Willing Heart","T1",False),
    ("Giving on Purpose","T2",False),("No Strings Attached","T2",False),("The Heart Behind the Gift","T2",False),
    ("From Duty to Delight","T2",False),("Sow and Reap","T2",False),("Giving Without Grudge","T2",False),
    ("The Glad Giver","T2",False)]),
  ("Radical & Sacrificial Giving", [
    ("Crazy Generosity","T1",True),("Beyond Their Ability","T1",False),("Extravagant Giving","T1",False),
    ("The Widow\u2019s Gift","T2",False),("Breaking the Jar","T2",False),("Sacrificial Generosity","T2",False),
    ("Giving It All","T2",False),("Reckless Grace","T2",False),("Past Sensible","T2",False),
    ("All-In Generosity","T2",False)]),
  ("Generosity Beyond Money", [
    ("Living Generously","T1",True),("Generous with Time","T1",False),("Generous with Words","T1",False),
    ("The Gift of Presence","T2",False),("Generous with Grace","T2",False),("Open Table, Open Home","T2",False),
    ("Lavish Encouragement","T2",False),("Generous in Everything","T2",False),("The Generous Spirit","T2",False),
    ("More Than Money","T2",False)]),
  ("Courage, Faith & Provision", [
    ("Courageous Generosity","T1",True),("Giving Before You\u2019re Ready","T1",False),("Test Me in This","T1",False),
    ("Faith Over Fear","T2",False),("First Fruits","T2",False),("The God Who Provides","T2",False),
    ("Giving in the Lean Times","T2",False),("Trusting God with Your Giving","T2",False),("The Widow\u2019s Oil","T2",False),
    ("Bold Generosity","T2",False)]),
  ("Growing in Generosity", [
    ("The Generosity Journey","T1",True),("The Next Step","T1",False),("Growing in Grace","T1",False),
    ("Generosity Habits","T2",False),("The Giving Plan","T2",False),("From Reluctant to Ready","T2",False),
    ("One Step at a Time","T2",False),("Generosity Over a Lifetime","T2",False),("Companions in Giving","T2",False),
    ("Excel in This Grace","T2",False)]),
  ("The Impact of Generosity", [
    ("Generosity Changes Everything","T1",True),("The Ripple Effect","T1",False),("Changed by Giving","T1",False),
    ("A Generous Church","T2",False),("Generosity Is Contagious","T2",False),("The Reach of a Gift","T2",False),
    ("Giving That Transforms","T2",False),("Part of Something Bigger","T2",False),("Generosity on Mission","T2",False),
    ("Multiplied Through Giving","T2",False)]),
  ("Abundance & Scarcity", [
    ("Abundance","T1",True),("Loaves and Fishes","T1",False),("Enough, and More","T1",False),
    ("The Scarcity Lie","T2",False),("Living from Plenty","T2",False),("The Math of Heaven","T2",False),
    ("Trusting His Provision","T2",False),("Open-Handed Abundance","T2",False),("More Than Enough","T2",False),
    ("From Fear to Trust","T2",False)]),
  ("Blessing & Purpose", [
    ("The Blessed Life","T1",True),("Blessed to Be a Blessing","T1",False),("A Channel of Grace","T1",False),
    ("The Purpose of Provision","T2",False),("Giving It Forward","T2",False),("A Legacy of Generosity","T2",False),
    ("What Blessed Really Means","T2",False),("Generosity & Gratitude","T2",False),("Blessing Others","T2",False),
    ("The Generous Legacy","T2",False)]),
  ("Overflow, Joy & the Full Life", [
    ("Overflow","T1",True),("The Overflowing Cup","T1",False),("Joy That Spills","T1",False),
    ("Filled to Give","T2",False),("Giving from Fullness","T2",False),("The Joy of Giving","T2",False),
    ("Gratitude Overflowing","T2",False),("A Full and Generous Life","T2",False),("Staying Full","T2",False),
    ("Overflowing Joy","T2",False)]),
 ],
}

doc, npages = build_catalog(cfg)
pathlib.Path("/tmp/generosity_catalog.html").write_text(doc, encoding="utf-8")
render_pdf("/tmp/generosity_catalog.html", "/tmp/generosity_catalog.pdf")
print("Generosity catalog:", npages, "pages")
