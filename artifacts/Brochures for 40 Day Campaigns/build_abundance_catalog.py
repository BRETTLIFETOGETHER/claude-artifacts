# -*- coding: utf-8 -*-
import pathlib
from catalog_engine import build_catalog, render_pdf

cfg = {
 "category":"Abundance",
 "doc_title":"Abundance Campaign Library",
 "tier":"Tier 2",
 "accent":"#a0532d",
 "accent2":"#c19a4b",
 "positioning":("A complete library of 100 ready-to-run campaigns that move churches, companies, and families out of "
   "survival mode and into the abundant, overflowing life Jesus came to give \u2014 marked by fullness, fruitfulness, grace, and joy."),
 "why_matters":("Jesus said He came so that we might have life, and have it to the full \u2014 yet so many believers live thin, "
   "depleted, survival-mode lives that look nothing like the abundance He promised. The gap between the life on offer and the "
   "life most people actually experience is enormous. A church that helps its people step into genuine abundance \u2014 not "
   "material excess, but fullness of life, grace, and joy \u2014 offers something the world is desperate for and cannot manufacture."),
 "core_problem":("Many people, including faithful believers, are simply running on empty \u2014 going through the motions, "
   "white-knuckling their way through life, settling for survival when Jesus offered fullness. They believe in the abundant "
   "life in theory but have never tasted it. Leaders long to lead people into it but lack a clear, biblical, well-produced pathway."),
 "transformation":("These campaigns move people from empty to full, from surviving to flourishing, and from scarcity to "
   "overflow \u2014 awakening them to the abundant life Jesus came to give and teaching them to live from its fullness."),
 "who_needs":[
   ("Churches","A life-giving series that calls people beyond survival into the fullness Jesus promised \u2014 hopeful, biblical, and energizing."),
   ("Companies","A framework for flourishing, gratitude, and wholehearted living that lifts the spirit of any team."),
   ("Advisors &amp; Donors","An inspiring vision of the truly abundant life to share with clients and partners."),
   ("Families","A way to cultivate a home marked by fullness, gratitude, and joy rather than hurry and scarcity."),
 ],
 "outcomes":[
   "A shift from survival mode to genuine fullness of life",
   "Freedom from the scarcity mindset",
   "A flourishing, fruitful, deeply rooted spiritual life",
   "Greater gratitude, joy, and contentment",
   "A life that overflows onto others",
   "A settled confidence in God\u2019s more-than-enough",
 ],
 "use_cases":[
   ("Churchwide Vision Series","A hope-filled, energizing series casting a vision of the abundant life."),
   ("40-Day Spiritual Campaign","Weekend messages, small groups, and daily readings."),
   ("21-Day Gratitude & Joy Challenge","A short, uplifting experience cultivating abundance and gratitude."),
   ("4-Week Sermon Companion","A focused message series with sermon-aligned small-group guides."),
   ("Advisor &amp; Donor Resource","A premium, inspiring resource for clients and partners."),
 ],
 "stats":[("100","Campaigns"),("10","Expanded"),("10","Themes"),("4","Formats"),("NIV","Scripture")],
 "components":["Daily Readings & Reflections","Six Group-Session Guides","Weekend Message Outlines",
               "Spiritual-Partner Prompts","Launch & Promotion Kit"],

 "top10":[
 {"n":"01","title":"Abundance","pos":"Stop merely surviving the life Jesus died to make full.",
  "felt":"Full life vs. existing","aud":"Church & Company",
  "summary":"The foundational campaign on John 10:10 \u2014 confronting the thin, survival-mode life and stepping into the full, abundant life Jesus promised.",
  "marketing":("The flagship entry point for the category. Abundance confronts the gap between the life Jesus offered and the "
     "depleted, survival-mode existence most settle for \u2014 and calls people into the fullness He came to give."),
  "problem":("Jesus drew a hard line between two figures: a thief who comes to steal, kill, and destroy, and a Shepherd who comes "
     "to give life. Many of us are living proof of the thief\u2019s work \u2014 alive, but barely; surviving, not thriving; quietly settling "
     "for a half-life when Jesus came to give the full one."),
  "transformation":("Participants confront what has been quietly stealing their fullness and step into the abundant life Jesus "
     "purchased at the cross \u2014 not more possessions, but more life, beginning now and stretching into eternity."),
  "sessions":[("The Thief at the Door","Naming what quietly drains your life."),("Life to the Brim","The fullness Jesus actually died to give."),
     ("The Half-Life We Settle For","Why survival masquerades as living."),("What\u2019s Been Stealing You","Bringing the thief into the light."),
     ("Crossing Into Fullness","Receiving the life already purchased."),("Alive, at Last","Living the abundance He came to give.")],
  "scriptures":"John 10:10  \u00b7  Psalm 23:1  \u00b7  John 1:16  \u00b7  Ephesians 3:20",
  "aud_full":"Church & Company \u2014 the ideal on-ramp to the entire abundance category.",
  "formats":"4-Session Series  \u00b7  21-Day Challenge  \u00b7  30-Day Devotional  \u00b7  40-Day Campaign (recommended)",
  "bigidea":"Jesus didn\u2019t endure the cross to hand you a slightly better version of the life you already had. He came so the thief\u2019s half-life would give way to His full one \u2014 life to the brim, here and now.",
  "ideal":"All-church on-ramps; anyone running on empty or settling for survival.",
  "pairs":"Overflow  \u00b7  The Abundant Life",
  "outcomes":["A move from surviving to thriving","Clarity on what steals fullness","The abundant life Jesus promised"]},

 {"n":"02","title":"Overflow","pos":"Be filled by God until your life can\u2019t help but spill over.",
  "felt":"Inner overflow","aud":"Church & Company",
  "summary":"A campaign on John 7:38 \u2014 the inner spring of living water that, once filled, overflows from within onto everyone around.",
  "marketing":("Overflow reveals the secret of a contagious life: an interior spring of living water that, once filled by Christ, "
     "can\u2019t help but spill over onto everyone around."),
  "problem":("We try to pour life into others while running dry ourselves \u2014 squeezing out kindness, patience, and faith from a "
     "cup that\u2019s already empty. But Jesus never asked us to manufacture the flow. He promised a source: His own Spirit, welling "
     "up inside, so the giving comes from fullness instead of fumes."),
  "transformation":("Participants learn to be filled at the source \u2014 Jesus Himself \u2014 until rivers of living water flow from "
     "within them, and their fullness naturally overflows onto the people around them."),
  "sessions":[("The Dry Riverbed","Why we run out of what we keep giving."),("Come to the Well","Returning to the only source that fills."),
     ("A Spring, Not a Cistern","The living water Jesus put within you."),("Filled Past the Brim","Receiving more than you could hold."),
     ("The Spilling Life","How fullness blesses without trying."),("Rivers from Within","A life that overflows for good.")],
  "scriptures":"John 7:37\u201338  \u00b7  John 4:14  \u00b7  Psalm 23:5  \u00b7  Ephesians 5:18",
  "aud_full":"Church & Company \u2014 restorative and energizing, especially for the depleted.",
  "formats":"4-Session Series  \u00b7  21-Day Challenge  \u00b7  30-Day Devotional  \u00b7  40-Day Campaign",
  "bigidea":"The overflowing life was never about willpower or output. Jesus promised a spring \u2014 His own Spirit \u2014 welling up inside you, until what fills you simply runs over onto everyone you meet.",
  "ideal":"The depleted and poured-out; anyone serving from empty.",
  "pairs":"Abundance  \u00b7  Abundant Grace",
  "outcomes":["A filled, overflowing interior life","A source that never runs dry","Fullness that blesses others"]},

 {"n":"03","title":"Living Fully Alive","pos":"Wake from the sleepwalk and feel your life again.",
  "felt":"Awakening & vibrancy","aud":"Church & Company",
  "summary":"A wake-up-call campaign on Ephesians 5:14 \u2014 rousing people from spiritual sleepwalking into vibrant, fully-alive faith.",
  "marketing":("Living Fully Alive is a wake-up call. It rouses people from the spiritual sleepwalking of routine, numbness, and "
     "autopilot into the vibrant, wide-awake life Christ shines on."),
  "problem":("Many believers are alive but not truly living \u2014 spiritually asleep, going through the motions, numb to the wonder "
     "of God. The lights are on, but inside it\u2019s autopilot, and the years are blurring past unfelt. We were raised with Christ to "
     "walk in newness of life; too often we simply drowse through it."),
  "transformation":("Participants hear the call to wake up, shake off the numbness, and come fully alive to God, to wonder, and "
     "to the life right in front of them \u2014 present, awake, and vibrantly alive."),
  "sessions":[("Awake but Asleep","The numbness we mistake for normal."),("Wake Up, Sleeper","The summons to come alive."),
     ("Where the Wonder Went","Recovering a heart that feels."),("Show Up for Your Life","The grace of full presence."),
     ("Shined Awake","Coming alive in the light of Christ."),("Wide Awake","Living every ordinary day fully alive.")],
  "scriptures":"Ephesians 5:14  \u00b7  Romans 13:11  \u00b7  John 11:25\u201326  \u00b7  Ephesians 2:4\u20135",
  "aud_full":"Church & Company \u2014 an energizing reset for the spiritually weary or numb.",
  "formats":"4-Session Series  \u00b7  21-Day Challenge  \u00b7  30-Day Devotional  \u00b7  40-Day Campaign",
  "bigidea":"Grace doesn\u2019t just forgive the dead \u2014 it raises them. \u2018Wake up, sleeper, and Christ will shine on you\u2019 is the gospel\u2019s call out of numb routine into a life that can finally be felt.",
  "ideal":"The numb and routine-bound; anyone going through the motions.",
  "pairs":"Abundance  \u00b7  Overflowing Joy",
  "outcomes":["An awakening from autopilot","Recovered wonder and vibrancy","Full presence and aliveness"]},

 {"n":"04","title":"The Abundant Life","pos":"Find abundance not in getting more, but in being kept.",
  "felt":"Provision & care","aud":"Church & Company",
  "summary":"A Psalm 23 campaign that grounds abundance in the Shepherd\u2019s care \u2014 green pastures, still waters, a restored soul, an overflowing cup.",
  "marketing":("The Abundant Life roots abundance where it belongs \u2014 not in circumstances, but in the care of the Good Shepherd, "
     "whose leading brings green pastures, restoration, and a cup that overflows."),
  "problem":("We chase abundance in circumstances \u2014 more income, more comfort, more control \u2014 and stay anxious and empty. We\u2019ve "
     "never learned the quieter truth of Psalm 23: that the overflowing cup belongs to the sheep who is led, not the one who "
     "strives, and abundance is what spills over when we let ourselves be kept."),
  "transformation":("Participants learn to receive abundance as the fruit of the Shepherd\u2019s care \u2014 lying down in green pastures, "
     "led beside still waters, soul restored, cup overflowing \u2014 and find rest, provision, and security in His leading."),
  "sessions":[("Whose You Are","Abundance begins with belonging."),("Made to Lie Down","The rest we keep refusing."),
     ("He Restores My Soul","Renewal for the worn-through places."),("Even the Valley","Abundance that survives the dark."),
     ("My Cup Overflows","The lavish care of the Shepherd."),("Goodness on Your Trail","A life pursued by mercy.")],
  "scriptures":"Psalm 23  \u00b7  John 10:11  \u00b7  Philippians 4:19  \u00b7  Psalm 16:11",
  "aud_full":"Church & Company \u2014 comforting and grounding; strong for anxious seasons.",
  "formats":"4-Session Series  \u00b7  21-Day Challenge  \u00b7  30-Day Devotional  \u00b7  40-Day Campaign",
  "bigidea":"The overflowing cup of Psalm 23 belongs to the sheep, not the shepherd. Abundance isn\u2019t what you achieve \u2014 it\u2019s what spills over when you finally let yourself be led, fed, and kept by God.",
  "ideal":"The anxious and weary; those chasing abundance in circumstances.",
  "pairs":"Abundance  \u00b7  More Than Enough",
  "outcomes":["Abundance grounded in God\u2019s care","Rest and restoration","An overflowing cup"]},

 {"n":"05","title":"More Than Enough","pos":"Trade your small prayers for a God of immeasurable more.",
  "felt":"God\u2019s limitless more","aud":"Church & Company",
  "summary":"An Ephesians 3:20 campaign that lifts people\u2019s eyes from their small expectations to the immeasurably-more capacity of God.",
  "marketing":("More Than Enough confronts the smallness of our expectations and lifts our eyes to a God who is able to do "
     "immeasurably more than all we ask or imagine \u2014 abundance rooted in His size, not our circumstances."),
  "problem":("We pray small and imagine smaller. Conditioned by scarcity, we approach God with timid, hedged requests, never "
     "daring to believe He might do more. Yet Paul says God is able to do immeasurably more than all we ask or imagine \u2014 and our "
     "shrunken expectations, not His limited power, are what quietly cap the abundance we experience."),
  "transformation":("Participants learn to anchor their hope not in their circumstances but in the limitless capacity of God \u2014 "
     "the One who does immeasurably more than all we ask or imagine \u2014 and to live with bold, expectant faith."),
  "sessions":[("The Prayers We Shrink","How scarcity edits our asking."),("Immeasurably More","The God who outgives our imagining."),
     ("The Power Within You","Where the \u2018more\u2019 actually comes from."),("Beyond What You\u2019d Dare","Stretching a too-small vision of God."),
     ("Ask Like He\u2019s Able","The courage of expectant faith."),("A More-Than-Enough God","Living from His limitless supply.")],
  "scriptures":"Ephesians 3:20\u201321  \u00b7  Philippians 4:19  \u00b7  2 Corinthians 9:8  \u00b7  Malachi 3:10",
  "aud_full":"Church & Company \u2014 faith-expanding; great for vision and momentum.",
  "formats":"4-Session Series  \u00b7  21-Day Challenge  \u00b7  30-Day Devotional  \u00b7  40-Day Campaign",
  "bigidea":"We shrink our asking to the size of our fear. But the God \u2018able to do immeasurably more\u2019 isn\u2019t limited by our circumstances or our imagination \u2014 only, sometimes, by how little we dare to bring Him.",
  "ideal":"The scarcity-minded; anyone whose small expectations cap their hope.",
  "pairs":"The Abundant Life  \u00b7  Kingdom Overflow",
  "outcomes":["Bigger expectations of God","Freedom from scarcity thinking","Bold, expectant faith"]},

 {"n":"06","title":"Kingdom Overflow","pos":"Stop chasing abundance and start seeking the King.",
  "felt":"Kingdom-first abundance","aud":"Church & Company",
  "summary":"A Matthew 6:33 campaign on the paradox of abundance \u2014 it comes not by chasing it, but by seeking first God\u2019s kingdom.",
  "marketing":("Kingdom Overflow reveals the great paradox of abundance: it\u2019s found not by pursuing it directly, but by seeking "
     "first the kingdom of God \u2014 and finding everything else added."),
  "problem":("We chase abundance head-on \u2014 more security, more provision, more of everything \u2014 and the harder we grasp, the more "
     "it slips away. Jesus turned the formula inside out: seek first the kingdom, and all these things are added. We\u2019ve been "
     "seeking the gifts and missing the Giver, then wondering why we still feel empty."),
  "transformation":("Participants learn to seek first God\u2019s kingdom and righteousness \u2014 trusting that everything else is added \u2014 "
     "and discover that abundance overflows from a kingdom-first life rather than a self-first one."),
  "sessions":[("The Harder You Grasp","Why chasing abundance empties you."),("Seek First","The reorder that changes everything."),
     ("All These Things Added","The promise hidden behind the priority."),("Treasure That Won\u2019t Rust","Investing where moth and rust can\u2019t reach."),
     ("The Unworried Heart","Freedom from the anxious chase."),("Kingdom Overflow","Abundance as the gift of a God-first life.")],
  "scriptures":"Matthew 6:31\u201333  \u00b7  Matthew 6:19\u201321  \u00b7  Luke 12:31\u201332  \u00b7  Proverbs 3:9\u201310",
  "aud_full":"Church & Company \u2014 reorders priorities; strong for whole-life discipleship.",
  "formats":"4-Session Series  \u00b7  21-Day Challenge  \u00b7  30-Day Devotional  \u00b7  40-Day Campaign",
  "bigidea":"Abundance is the one thing you lose by grasping and gain by releasing. Seek first the kingdom \u2014 want the King more than the gifts \u2014 and the overflow follows on its own.",
  "ideal":"The anxious strivers; anyone grasping for security and coming up empty.",
  "pairs":"More Than Enough  \u00b7  Flourishing in Christ",
  "outcomes":["Reordered priorities","Freedom from anxious striving","Abundance as kingdom overflow"]},

 {"n":"07","title":"Flourishing in Christ","pos":"Sink roots deep enough to flourish through any drought.",
  "felt":"Flourishing & fruitfulness","aud":"Church & Company",
  "summary":"A Psalm 1 campaign on the flourishing life \u2014 a tree planted by streams, deeply rooted, bearing fruit in season, thriving even in drought.",
  "marketing":("Flourishing in Christ paints the picture of Psalm 1: a tree planted by streams of water, drawing deep from its "
     "source, bearing fruit in season and green even in drought \u2014 the rooted, flourishing life."),
  "problem":("Many of us are trying to flourish without roots \u2014 chasing growth and fruit while disconnected from the source that "
     "produces them. But Jesus was clear: apart from Him we can do nothing. The branch doesn\u2019t manufacture fruit; it bears what "
     "the vine sends up. So we wither in the first drought and wonder why the flourishing life stays out of reach."),
  "transformation":("Participants learn that flourishing flows from rootedness \u2014 being planted deep by the stream of Christ \u2014 "
     "and discover the sustained fruitfulness of a life that thrives in every season."),
  "sessions":[("Fruit Without Roots","Why striving withers in the heat."),("Planted by the Stream","The secret of the flourishing tree."),
     ("Down Where It\u2019s Quiet","The hidden work of deep roots."),("Fruit in Its Season","Letting growth keep God\u2019s timing."),
     ("Green in the Drought","Thriving when the season turns hard."),("A Life That Flourishes","Sustained fruit from a deep source.")],
  "scriptures":"Psalm 1:1\u20133  \u00b7  Jeremiah 17:7\u20138  \u00b7  John 15:5  \u00b7  Colossians 2:6\u20137",
  "aud_full":"Church & Company \u2014 a rich growth-and-rootedness campaign for all levels.",
  "formats":"4-Session Series  \u00b7  21-Day Challenge  \u00b7  30-Day Devotional  \u00b7  40-Day Campaign",
  "bigidea":"Flourishing was never produced by the branch \u2014 it\u2019s drawn up through the roots. Planted by the Stream who is Christ, you bear fruit in season and stay green when everything around you browns.",
  "ideal":"The burned-out; anyone chasing growth without rootedness.",
  "pairs":"Kingdom Overflow  \u00b7  Abundant Grace",
  "outcomes":["Deeper spiritual roots","Sustained fruitfulness","Thriving in every season"]},

 {"n":"08","title":"Abundant Grace","pos":"Live from a grace that never once runs low.",
  "felt":"Grace upon grace","aud":"Church & Company",
  "summary":"A John 1:16 campaign on the inexhaustible grace of God \u2014 the deepest abundance of all, grace upon grace from His fullness.",
  "marketing":("Abundant Grace points to the truest abundance \u2014 not material, but the endless, layered grace of God: from His "
     "fullness we have all received, grace upon grace, never running out."),
  "problem":("Many believers live as though grace is scarce \u2014 rationing it, fearing they\u2019ve used too much, striving to earn what "
     "was freely given. They treat the most abundant thing in the universe as if it might run out. But John says that from "
     "Christ\u2019s fullness we have all received grace upon grace \u2014 wave after wave, never billed, never depleted."),
  "transformation":("Participants discover the inexhaustible supply of God\u2019s grace \u2014 grace upon grace, from His fullness \u2014 and "
     "learn to live freely and gratefully from an abundance that never runs dry."),
  "sessions":[("Rationing the Unlimited","Why we hoard what can\u2019t run out."),("Out of His Fullness","The bottomless source of grace."),
     ("Grace Upon Grace","Wave after wave, never earned."),("The End of Earning","Receiving what you could never deserve."),
     ("Living Loved","Grace as the air you breathe."),("Abundant Grace","A life built on an endless supply.")],
  "scriptures":"John 1:16  \u00b7  2 Corinthians 9:8  \u00b7  Ephesians 1:7\u20138  \u00b7  Romans 5:20",
  "aud_full":"Church & Company \u2014 freeing and gospel-rich; great for the weary and striving.",
  "formats":"4-Session Series  \u00b7  21-Day Challenge  \u00b7  30-Day Devotional  \u00b7  40-Day Campaign",
  "bigidea":"The deepest abundance isn\u2019t in your account \u2014 it\u2019s in His fullness. \u2018Grace upon grace\u2019 means the supply was never rationed, never earned, and never once runs dry; it only keeps arriving.",
  "ideal":"The striving and grace-starved; anyone who treats grace as scarce.",
  "pairs":"Overflow  \u00b7  Flourishing in Christ",
  "outcomes":["Freedom from grace-scarcity","An end to earning","A life from God\u2019s fullness"]},

 {"n":"09","title":"Living with Open Hands","pos":"Unclench, and let abundance flow through you again.",
  "felt":"Receive & release","aud":"Church & Company",
  "summary":"A Matthew 10:8 campaign on open hands as the channel of abundance \u2014 freely received, freely give; you keep receiving by releasing.",
  "marketing":("Living with Open Hands reveals the flow of abundance: it moves through open hands, not clenched fists. Those who "
     "know they\u2019ve freely received hold everything loosely \u2014 free to receive more and release freely."),
  "problem":("We instinctively clench \u2014 gripping what we have out of fear there won\u2019t be more. But Jesus said, \u2018Freely you have "
     "received; freely give,\u2019 and a closed fist can do neither. The very grip we think protects our abundance is the thing that "
     "stops more from arriving."),
  "transformation":("Participants learn to live with open hands \u2014 freely receiving and freely giving \u2014 and discover that "
     "abundance keeps flowing to those who keep it moving."),
  "sessions":[("The Clenched Fist","How fear chokes off the flow."),("Freely Received","Remembering it was all a gift."),
     ("Freely Give","The release that keeps the river moving."),("A Channel, Not a Dam","Becoming a means of blessing."),
     ("Hands Open to Heaven","Ready for what God sends next."),("The Open-Handed Life","Living inside the flow of grace.")],
  "scriptures":"Matthew 10:8  \u00b7  Luke 6:38  \u00b7  2 Corinthians 9:6\u20138  \u00b7  Acts 20:35",
  "aud_full":"Church & Company \u2014 connects abundance and generosity; broad appeal.",
  "formats":"4-Session Series  \u00b7  21-Day Challenge  \u00b7  30-Day Devotional  \u00b7  40-Day Campaign",
  "bigidea":"\u2018Freely you have received; freely give.\u2019 Open hands are the only hands that can do both \u2014 the clenched fist that guards your abundance is the very thing that stops more from arriving.",
  "ideal":"The fearful grippers; anyone whose tight hold blocks the flow.",
  "pairs":"Overflow  \u00b7  Overflowing Joy",
  "outcomes":["An open-handed posture","Freedom from the clenched grip","Abundance that keeps flowing"]},

 {"n":"10","title":"Overflowing Joy","pos":"Let the surest sign of abundance be your joy.",
  "felt":"Fullness of joy","aud":"Church & Company",
  "summary":"A John 15:11 campaign on joy as the truest mark of abundance \u2014 the complete, overflowing joy of abiding in Christ.",
  "marketing":("Overflowing Joy names the truest sign of the abundant life: not possessions, but a complete, overflowing joy \u2014 "
     "the very joy of Jesus, flowing from a life that abides in Him."),
  "problem":("We often measure abundance by what we have, while joy quietly drains away. We can accumulate plenty and still feel "
     "flat, because the fullness we were made for isn\u2019t found in things. Jesus measured the abundant life differently \u2014 by joy \u2014 "
     "and located its source not in circumstances but in staying close to Him."),
  "transformation":("Participants discover that the abundant life overflows as joy \u2014 the complete joy Jesus promised \u2014 and learn "
     "to abide in Him until that joy fills and spills over into everyday life."),
  "sessions":[("Full Hands, Flat Heart","Why plenty can still feel empty."),("That Your Joy Be Complete","The gladness Jesus promised."),
     ("Joy at the Source","Abiding as the secret of joy."),("Joy the Storms Can\u2019t Reach","Gladness beyond circumstance."),
     ("The Grateful Overflow","How thanksgiving multiplies joy."),("Overflowing Joy","The abundant life you can feel.")],
  "scriptures":"John 15:11  \u00b7  Psalm 16:11  \u00b7  Nehemiah 8:10  \u00b7  Philippians 4:4",
  "aud_full":"Church & Company \u2014 uplifting; a fitting, hope-filled close to the category.",
  "formats":"4-Session Series  \u00b7  21-Day Challenge  \u00b7  30-Day Devotional  \u00b7  40-Day Campaign",
  "bigidea":"Jesus measured the abundant life not in possessions but in joy \u2014 \u2018that my joy may be in you, and your joy be complete.\u2019 It isn\u2019t manufactured by effort; it\u2019s the overflow of a life still attached to the Vine.",
  "ideal":"Anyone with plenty but little joy; gratitude and renewal contexts.",
  "pairs":"Living Fully Alive  \u00b7  Living with Open Hands",
  "outcomes":["Joy as the mark of abundance","Gladness beyond circumstances","An overflowing, grateful heart"]},
 ],

 "library":[
  ("The Abundant Life", [
    ("Abundance","T2",True),("Life to the Full","T2",False),("The Good Life","T2",False),
    ("More Than Existing","T2",False),("Made for More","T2",False),("The Life He Promised","T2",False),
    ("Beyond Survival","T2",False),("Full and Free","T2",False),("The Life That Is Truly Life","T2",False),
    ("Alive in Christ","T2",False)]),
  ("Overflow & Living Water", [
    ("Overflow","T2",True),("Rivers of Living Water","T2",False),("The Overflowing Life","T2",False),
    ("Springs Within","T2",False),("Filled to Overflowing","T2",False),("Come and Drink","T2",False),
    ("Never Thirsty Again","T2",False),("The Inner Spring","T2",False),("Pouring Out","T2",False),
    ("An Overflowing Heart","T2",False)]),
  ("Fully Alive & Awake", [
    ("Living Fully Alive","T2",True),("Wake Up, Sleeper","T2",False),("Coming Alive","T2",False),
    ("More Than Going Through the Motions","T2",False),("Awake and Alive","T2",False),("The End of Numb","T2",False),
    ("Vibrant Faith","T2",False),("Truly Living","T2",False),("From Surviving to Thriving","T2",False),
    ("Fully Present, Fully Alive","T2",False)]),
  ("The Shepherd\u2019s Provision", [
    ("The Abundant Life","T2",True),("Green Pastures","T2",False),("My Cup Overflows","T2",False),
    ("The Good Shepherd","T2",False),("I Shall Not Want","T2",False),("Still Waters","T2",False),
    ("He Restores My Soul","T2",False),("Led Beside Quiet Waters","T2",False),("Provided For","T2",False),
    ("The Shepherd\u2019s Care","T2",False)]),
  ("More Than Enough", [
    ("More Than Enough","T2",True),("Immeasurably More","T2",False),("The God of More","T2",False),
    ("Beyond What You Ask","T2",False),("Exceedingly Abundantly","T2",False),("Above All We Imagine","T2",False),
    ("No Lack","T2",False),("The Limitless God","T2",False),("Enough, and to Spare","T2",False),
    ("His Riches in Glory","T2",False)]),
  ("Kingdom Abundance", [
    ("Kingdom Overflow","T2",True),("Seek First","T2",False),("All These Things","T2",False),
    ("The Kingdom Life","T2",False),("Treasure in the Kingdom","T2",False),("Upside-Down Abundance","T2",False),
    ("Kingdom First","T2",False),("The Abundance of the King","T2",False),("Heaven\u2019s Economy","T2",False),
    ("Rich Toward God","T2",False)]),
  ("Flourishing & Fruitfulness", [
    ("Flourishing in Christ","T2",True),("The Tree by the Stream","T2",False),("Bearing Fruit","T2",False),
    ("Rooted and Thriving","T2",False),("Fruit in Season","T2",False),("Planted to Flourish","T2",False),
    ("A Flourishing Life","T2",False),("Deep Roots","T2",False),("Thriving in Every Season","T2",False),
    ("The Fruitful Life","T2",False)]),
  ("Abundant Grace", [
    ("Abundant Grace","T2",True),("Grace Upon Grace","T2",False),("From His Fullness","T2",False),
    ("Lavished with Grace","T2",False),("The Inexhaustible Supply","T2",False),("Grace That Never Runs Out","T2",False),
    ("Riches of His Grace","T2",False),("More Than Enough Grace","T2",False),("Living from Fullness","T2",False),
    ("The Gift of Grace","T2",False)]),
  ("Open Hands & Flow", [
    ("Living with Open Hands","T2",True),("Freely Received, Freely Give","T2",False),("The Open-Handed Life","T2",False),
    ("Receive and Release","T2",False),("Holding Loosely","T2",False),("The Channel of Blessing","T2",False),
    ("Hands Open to Heaven","T2",False),("Give and It Will Be Given","T2",False),("Keep the Flow Going","T2",False),
    ("Open to Abundance","T2",False)]),
  ("Joy, Gratitude & the Full Heart", [
    ("Overflowing Joy","T2",True),("That Your Joy May Be Complete","T2",False),("The Joy of the Lord","T2",False),
    ("Full of Joy","T2",False),("Gratitude & Abundance","T2",False),("A Thankful Heart","T2",False),
    ("Counting the Blessings","T2",False),("Joy Unspeakable","T2",False),("The Grateful Life","T2",False),
    ("Abundant and Glad","T2",False)]),
 ],
}

doc, npages = build_catalog(cfg)
pathlib.Path("/tmp/abundance_catalog.html").write_text(doc, encoding="utf-8")
render_pdf("/tmp/abundance_catalog.html", "/tmp/abundance_catalog.pdf")
print("Abundance catalog (elevated):", npages, "pages")
