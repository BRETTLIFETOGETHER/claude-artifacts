# -*- coding: utf-8 -*-
import pathlib
from catalog_engine import build_catalog, render_pdf

cfg = {
 "category":"Family Legacy",
 "doc_title":"Family Legacy Campaign Library",
 "tier":"Tier 2",
 "accent":"#6e2f3a",   # heritage burgundy
 "accent2":"#c19a4b",
 "positioning":("A complete library of 100 ready-to-run campaigns that help churches, companies, and families build a "
   "lasting legacy of faith \u2014 passing down what matters most to children, grandchildren, and generations they\u2019ll never meet."),
 "why_matters":("Long after the estate is settled and the name is half-remembered, what truly shapes a family is the faith, "
   "character, and mission handed from one generation to the next. Yet that kind of legacy never happens by accident \u2014 it is "
   "received, built, blessed, and passed forward on purpose. Scripture is relentless on this: faith is always one generation "
   "from being lost. A church that disciples its people to leave a spiritual legacy secures the future of the faith itself."),
 "core_problem":("Most people deeply want to leave their children something that lasts \u2014 and quietly assume it will simply "
   "happen. So they leave the most important inheritance to chance, defer legacy to \u2018someday,\u2019 and never do the intentional "
   "work of passing faith forward. Leaders see the longing but lack a clear, practical pathway to help families build and "
   "hand down a legacy of faith."),
 "transformation":("These campaigns move families from drifting to designing and from hoping to handing down \u2014 helping them "
   "build a spiritual legacy, bless the next generation, and pass faith forward so it reaches children\u2019s children and beyond."),
 "who_needs":[
   ("Churches","A complete legacy pathway that disciples families to pass faith forward \u2014 pastoral, practical, and deeply formational."),
   ("Companies","A values-rich framework on legacy, purpose, and generational thinking that resonates with any leader or team."),
   ("Advisors &amp; Donors","A meaningful vision of the legacy that outlasts an estate, to share with clients and partners."),
   ("Families","A guided path to build a household of faith and hand it down to children and grandchildren."),
 ],
 "outcomes":[
   "Clarity on the spiritual inheritance worth passing down",
   "A family built on purpose, with mission and values",
   "Faith woven into everyday family life",
   "The recovered practice of blessing the next generation",
   "A generational mindset that lives beyond one lifespan",
   "Faith passed forward so the next generation knows the Lord",
 ],
 "use_cases":[
   ("Churchwide Legacy Series","A whole-church journey into building and passing down a legacy of faith."),
   ("40-Day Spiritual Campaign","Weekend messages, small groups, and daily readings."),
   ("21-Day Family Challenge","A short, focused experience for families building a legacy together."),
   ("4-Week Sermon Companion","A focused message series with sermon-aligned small-group guides."),
   ("Advisor &amp; Donor Resource","A premium resource for clients and partners thinking about legacy."),
 ],
 "stats":[("100","Campaigns"),("10","Expanded"),("10","Themes"),("4","Formats"),("NIV","Scripture")],
 "components":["Daily Readings & Reflections","Six Group-Session Guides","Weekend Message Outlines",
               "Spiritual-Partner Prompts","Launch & Promotion Kit"],

 "top10":[
 {"n":"01","title":"Family Legacy","pos":"Leave your children the one inheritance that won\u2019t appear in your will.",
  "felt":"Spiritual inheritance","aud":"Church & Company",
  "summary":"The foundational campaign \u2014 the truest inheritance isn\u2019t financial but spiritual: the faith, character, and stories you pass to your children and grandchildren.",
  "marketing":("The flagship entry point for the category. Family Legacy lifts the idea of inheritance off the estate and onto "
     "the soul, helping people get intentional about the faith and character they\u2019re actually passing down."),
  "problem":("When we picture what we\u2019ll leave our children, we picture money, property, the contents of a will. But the "
     "inheritance that truly shapes a family for generations is the faith, the stories, the character we hand down \u2014 and unlike money, that legacy is built on purpose or not at all."),
  "transformation":("Participants get intentional about the spiritual inheritance they\u2019re passing to their children and "
     "grandchildren \u2014 telling the next generation the goodness of God \u2014 so the truest part of their legacy lives on long after the estate is settled."),
  "sessions":[("More Than a Will","The inheritance no estate can hold."),("What You\u2019re Really Leaving","An honest look at your spiritual estate."),
     ("Tell the Next Generation","Handing down the goodness of God."),("Character Outlives Cash","Why who you are outlasts what you leave."),
     ("On Purpose, or Not at All","The legacy that only intention builds."),("A Hundred Years From Now","Leaving what will still matter then.")],
  "scriptures":"Psalm 78:1\u20137  \u00b7  Deuteronomy 4:9  \u00b7  2 Timothy 1:5  \u00b7  Proverbs 22:6",
  "aud_full":"Church & Company \u2014 the ideal on-ramp to the entire family-legacy category.",
  "formats":"4-Session Series  \u00b7  21-Day Challenge  \u00b7  30-Day Devotional  \u00b7  40-Day Campaign (recommended)",
  "bigidea":"The most valuable thing you\u2019ll ever pass down won\u2019t appear in your will. It\u2019s the faith, the character, the stories \u2014 the inheritance that actually shapes a soul.",
  "ideal":"All-church on-ramps; parents and grandparents thinking about what they\u2019ll leave.",
  "pairs":"Building a Spiritual Legacy  \u00b7  Faith for Generations",
  "outcomes":["A clear view of your spiritual inheritance","Intentionality about what you pass down","Faith handed to the next generation"]},

 {"n":"02","title":"Leaving a Lasting Legacy","pos":"Build a life whose impact still stands long after you\u2019re gone.",
  "felt":"A legacy that endures","aud":"Church & Company",
  "summary":"A long-view campaign \u2014 building a life and legacy that doesn\u2019t fade, that finishes well and blesses generations you\u2019ll never meet.",
  "marketing":("Leaving a Lasting Legacy lifts people\u2019s eyes to the long view, calling them to build a life that outlasts them "
     "\u2014 remembered for what truly matters and blessing children\u2019s children."),
  "problem":("Most legacies fade faster than we\u2019d like to admit \u2014 a name half-remembered, accomplishments forgotten within a "
     "generation. We pour our lives into things that don\u2019t outlast us and quietly fear that when we\u2019re gone, little will remain."),
  "transformation":("Participants learn to build a life and a family legacy that endures \u2014 the kind that blesses children\u2019s "
     "children, finishes well, and is remembered for what truly matters long after they\u2019re gone."),
  "sessions":[("The Legacies That Fade","Why most of what we build won\u2019t last."),("Remembered Forever","The kind of life Scripture says endures."),
     ("Rooted in What Lasts","Building on a foundation that holds."),("To Children\u2019s Children","A legacy that reaches three generations out."),
     ("Finishing the Story Well","Ending the way you\u2019ll want to be remembered."),("A Lasting Mark","Living now for what will still stand later.")],
  "scriptures":"Psalm 112:1\u20136  \u00b7  Proverbs 13:22  \u00b7  2 Timothy 4:7  \u00b7  Hebrews 11:4",
  "aud_full":"Church & Company \u2014 strong for parents, grandparents, and legacy-minded leaders.",
  "formats":"4-Session Series  \u00b7  21-Day Challenge  \u00b7  30-Day Devotional  \u00b7  40-Day Campaign",
  "bigidea":"Almost everything you build will be forgotten. But a life rooted in righteousness leaves a legacy that endures \u2014 remembered, fruitful, blessing generations you\u2019ll never meet.",
  "ideal":"Those thinking about how they\u2019ll finish and what they\u2019ll leave behind.",
  "pairs":"Family Legacy  \u00b7  Legacy Living",
  "outcomes":["A long-view perspective on life","A legacy built to endure","A faithful, well-finished story"]},

 {"n":"03","title":"Generations","pos":"Take your place in a chain of faith that runs back generations \u2014 and forward.",
  "felt":"The chain of faith","aud":"Church & Company",
  "summary":"A campaign on the multi-generational chain of faith \u2014 honoring the faith handed to you and becoming the strong link that passes it on.",
  "marketing":("Generations helps people take their place in the line \u2014 honoring the faith handed down to them, recognizing "
     "their role as a vital link between past and future, and passing it on stronger than they found it."),
  "problem":("Faith was always meant to travel through families, handed from one generation to the next like a lit candle. But "
     "the chain so often breaks: a generation that received much passes on little, and the faith alive in the grandparents grows faint by the grandchildren. We rarely see ourselves as the crucial link."),
  "transformation":("Participants honor the faith handed to them, recognize their place as a vital link between past and future, "
     "and learn to pass on \u2014 strengthened, not weakened \u2014 the living faith that once lived in a Lois and a Eunice and now lives in them."),
  "sessions":[("A Chain of Faith","How faith was designed to move through families."),("Lois, Eunice, and You","Three generations and a faith handed down."),
     ("Honoring What You Received","Gratitude for the faith passed to you."),("The Link You Choose to Be","Your place between those before and after."),
     ("Breaking and Building","Ending the patterns, starting the godly ones."),("Stronger Than You Found It","Handing the faith forward, strengthened.")],
  "scriptures":"2 Timothy 1:5  \u00b7  Psalm 145:4  \u00b7  Deuteronomy 6:2  \u00b7  Judges 2:10",
  "aud_full":"Church & Company \u2014 connects grandparents, parents, and children in one story.",
  "formats":"4-Session Series  \u00b7  21-Day Challenge  \u00b7  30-Day Devotional  \u00b7  40-Day Campaign",
  "bigidea":"You are a link in a chain of faith that stretches back generations and forward into ones you\u2019ll never see. The chain is only as strong as the link you choose to be.",
  "ideal":"Multi-generational families; anyone aware of the faith they did or didn\u2019t receive.",
  "pairs":"Passing Faith Forward  \u00b7  The Generational Life",
  "outcomes":["A sense of your place in the chain","Gratitude for inherited faith","Faith passed on, strengthened"]},

 {"n":"04","title":"Faith for Generations","pos":"Pass living faith to your children \u2014 woven into ordinary days.",
  "felt":"Spiritual parenting","aud":"Church & Company",
  "summary":"An everyday-transmission campaign \u2014 the ancient pattern of impressing faith on your children, woven into the ordinary fabric of family life.",
  "marketing":("Faith for Generations equips parents and grandparents to pass faith on with intention \u2014 weaving it into the "
     "ordinary moments of family life so that living faith actually reaches the next generation."),
  "problem":("Many parents deeply want their children to know God \u2014 and quietly assume it will simply happen, that faith will "
     "rub off through church attendance and good intentions. But faith is rarely caught by accident; without intentional, everyday transmission, the most precious thing we have to give can miss the very people we love most."),
  "transformation":("Participants learn the ancient pattern of weaving faith into the ordinary fabric of family life \u2014 impressing "
     "it on their children as they sit at home and walk along the road \u2014 so that living faith reaches the next generation, not by accident, but on purpose."),
  "sessions":[("Caught, Not Assumed","Why faith rarely transmits on its own."),("Impress Them","The deliberate work of handing faith down."),
     ("As You Walk Along the Road","Weaving faith into ordinary moments."),("The Family Altar","Simple rhythms that carry faith down a generation."),
     ("When Faith Gets Hard","Staying faithful through doubt and distance."),("Faith That Reaches Them","Making sure the next generation knows God.")],
  "scriptures":"Deuteronomy 6:4\u20139  \u00b7  Psalm 78:5\u20136  \u00b7  Proverbs 22:6  \u00b7  Ephesians 6:4",
  "aud_full":"Church & Company \u2014 a practical, hands-on guide for parents and grandparents.",
  "formats":"4-Session Series  \u00b7  21-Day Challenge  \u00b7  30-Day Devotional  \u00b7  40-Day Campaign",
  "bigidea":"Faith is rarely caught by accident. It\u2019s passed on by parents and grandparents intentional enough to weave it into the ordinary moments of everyday family life.",
  "ideal":"Parents and grandparents wanting to pass faith to their kids; family-ministry contexts.",
  "pairs":"Family Legacy  \u00b7  Blessing the Next Generation",
  "outcomes":["Practical faith-transmission tools","Faith woven into everyday family life","Children who come to know God"]},

 {"n":"05","title":"Family by Design","pos":"Build your family on purpose instead of by default.",
  "felt":"Family mission","aud":"Church & Company",
  "summary":"An intentionality campaign \u2014 moving from a family shaped by accident to one built on purpose, with a clear mission, shared values, and intentional rhythms.",
  "marketing":("Family by Design hands people the blueprint \u2014 moving them from a family shaped by accident to one built on "
     "purpose, with a clear mission, shared values, and the decisive declaration that this household will follow the Lord."),
  "problem":("Most families don\u2019t choose their culture \u2014 they drift into it. Without a clear mission or shared values, family "
     "life gets shaped by busyness, screens, and whatever the calendar demands, and we wake up years later wondering how we got here. A family left to default rarely becomes the family we hoped for."),
  "transformation":("Participants move from a family shaped by accident to one built on purpose \u2014 clarifying their family\u2019s "
     "mission, values, and rhythms, and making the decisive declaration that, whatever others do, this household will serve the Lord."),
  "sessions":[("Drift or Design","How most families are shaped by default."),("As for Me and My House","The declaration that sets the direction."),
     ("Your Family\u2019s Mission","Naming what your family is actually for."),("The Values You Stand On","Choosing the few things you won\u2019t bend on."),
     ("Rhythms That Form Us","Building the habits that shape your culture."),("A Family on Purpose","Becoming the household you\u2019ve chosen to be.")],
  "scriptures":"Joshua 24:15  \u00b7  Proverbs 24:3\u20134  \u00b7  Deuteronomy 6:6\u20137  \u00b7  Psalm 127:1",
  "aud_full":"Church & Company \u2014 practical and clarifying; strong for parents of all ages.",
  "formats":"4-Session Series  \u00b7  21-Day Challenge  \u00b7  30-Day Devotional  \u00b7  40-Day Campaign",
  "bigidea":"A family is either built on purpose or shaped by default \u2014 and default rarely drifts anywhere good. The strongest families are simply the ones designed on purpose.",
  "ideal":"Families wanting clarity and intention; couples building a home culture.",
  "pairs":"Building a Spiritual Legacy  \u00b7  Legacy Living",
  "outcomes":["A clear family mission and values","Intentional family rhythms","A household built on purpose"]},

 {"n":"06","title":"Legacy Living","pos":"Stop saving your legacy for the end \u2014 you\u2019re building it today.",
  "felt":"Legacy as daily living","aud":"Church & Company",
  "summary":"A present-tense campaign \u2014 legacy isn\u2019t an end-of-life event but a way of living now; building tomorrow\u2019s legacy in today\u2019s ordinary choices.",
  "marketing":("Legacy Living flips the timeline. It shows that legacy isn\u2019t something settled at the end of life but something "
     "built in the present \u2014 and teaches people to live each ordinary day in light of the legacy it\u2019s quietly creating."),
  "problem":("We treat legacy as a someday concern \u2014 something to think about near the end, when there\u2019s time to get our affairs "
     "in order. But by then the legacy is already mostly written. The truth is uncomfortable and freeing: you\u2019re building your legacy today, in choices that feel far too ordinary to matter."),
  "transformation":("Participants learn to number their days and live each one in light of the legacy it\u2019s creating \u2014 trading "
     "\u2018someday\u2019 for today \u2014 so that an intentional present quietly builds a legacy that takes care of itself."),
  "sessions":[("The Someday Trap","Why we postpone the legacy we\u2019re already building."),("Teach Us to Number Our Days","Letting mortality make us wise."),
     ("Today Is the Legacy","How ordinary days become a lasting story."),("Begin with the End","Living backward from who you want to have been."),
     ("The Wisdom of Limits","Why a numbered life is a focused one."),("A Legacy Lived, Not Left","Building it now, not deferring it.")],
  "scriptures":"Psalm 90:12  \u00b7  Ephesians 5:15\u201316  \u00b7  James 4:14  \u00b7  Ecclesiastes 7:2",
  "aud_full":"Church & Company \u2014 motivating and clarifying for any age or stage.",
  "formats":"4-Session Series  \u00b7  21-Day Challenge  \u00b7  30-Day Devotional  \u00b7  40-Day Campaign",
  "bigidea":"Legacy isn\u2019t written at the end of a life \u2014 it\u2019s written every ordinary day along the way. You\u2019re not planning to leave a legacy someday; you\u2019re building one right now.",
  "ideal":"Anyone who keeps deferring legacy to \u2018someday\u2019; all ages and stages.",
  "pairs":"Leaving a Lasting Legacy  \u00b7  Family by Design",
  "outcomes":["Legacy lived in the present","Days numbered and used well","An end-in-mind way of living"]},

 {"n":"07","title":"Blessing the Next Generation","pos":"Recover the lost art of speaking blessing over your children.",
  "felt":"The spoken blessing","aud":"Church & Company",
  "summary":"A campaign on the power of the blessing \u2014 recovering the biblical practice of speaking identity, worth, and God\u2019s favor over the next generation.",
  "marketing":("Blessing the Next Generation recovers a nearly lost practice: the intentional, spoken blessing. It teaches "
     "people to speak identity, worth, and the favor of God over their children and grandchildren \u2014 and shows what it does in a young soul to be blessed by name."),
  "problem":("Scripture is full of fathers and mothers laying hands on children and speaking blessing over them by name \u2014 and "
     "most of us have never done it. We assume our children know they\u2019re loved and valued, while leaving the most powerful words unspoken. A generation is growing up unblessed, hungry for words we never thought to say."),
  "transformation":("Participants recover the biblical practice of blessing \u2014 learning to speak identity, worth, and God\u2019s favor "
     "over the next generation, intentionally and out loud \u2014 and discover what it does in a child to hear a blessing spoken over them by name."),
  "sessions":[("The Words We Never Said","The blessing this generation is missing."),("The Lord Bless You","The ancient benediction over God\u2019s people."),
     ("Blessed by Name","What the patriarchs spoke over their children."),("Identity and Favor","The two things a blessing gives."),
     ("Let the Children Come","How Jesus blessed the young."),("A Blessing Spoken","Making the blessing a family practice.")],
  "scriptures":"Numbers 6:24\u201326  \u00b7  Genesis 48:14\u201316  \u00b7  Mark 10:13\u201316  \u00b7  Genesis 27:27\u201329",
  "aud_full":"Church & Company \u2014 tender and practical; powerful for parents and grandparents.",
  "formats":"4-Session Series  \u00b7  21-Day Challenge  \u00b7  30-Day Devotional  \u00b7  40-Day Campaign",
  "bigidea":"Every child is quietly asking two questions: Am I loved? and What\u2019s special about me? The spoken blessing answers both \u2014 and most are still waiting to hear it.",
  "ideal":"Parents and grandparents; anyone who\u2019s left the blessing unspoken.",
  "pairs":"Faith for Generations  \u00b7  Generations",
  "outcomes":["The recovered practice of blessing","Children who hear their worth spoken","A family marked by blessing"]},

 {"n":"08","title":"The Generational Life","pos":"Zoom out and live for a story far bigger than your lifespan.",
  "felt":"A generational mindset","aud":"Church & Company",
  "summary":"A perspective campaign \u2014 adopting a generational mindset that lives beyond one\u2019s own lifespan, anchored in God\u2019s covenant faithfulness to a thousand generations.",
  "marketing":("The Generational Life is a shift in vision. It calls people out of the narrow horizon of their own lifespan into "
     "a generational mindset \u2014 living, deciding, and praying with generations they\u2019ll never meet in view, anchored in God\u2019s faithfulness to a thousand generations."),
  "problem":("We instinctively live inside the borders of our own lifespan \u2014 our years, our plans, our horizon. But Scripture "
     "keeps zooming out, speaking of God\u2019s faithfulness to a thousand generations and one generation declaring His works to the next. A life lived only for itself is a life lived far too small."),
  "transformation":("Participants adopt a generational mindset \u2014 learning to think, decide, and pray with generations in view \u2014 "
     "and find their place in God\u2019s long, faithful story that runs from those before them to those they\u2019ll never meet."),
  "sessions":[("The Length of a Life","Why we live smaller than we were made to."),("To a Thousand Generations","The scope of God\u2019s covenant faithfulness."),
     ("One Generation to the Next","Each one declaring His works onward."),("Decisions with Descendants in Mind","Choosing for those not yet born."),
     ("Praying Down the Line","Interceding for generations to come."),("The Generational Life","Living inside a story bigger than yourself.")],
  "scriptures":"Psalm 145:4  \u00b7  Deuteronomy 7:9  \u00b7  Psalm 100:5  \u00b7  Psalm 102:18",
  "aud_full":"Church & Company \u2014 vision-expanding; strong for leaders and forward-thinkers.",
  "formats":"4-Session Series  \u00b7  21-Day Challenge  \u00b7  30-Day Devotional  \u00b7  40-Day Campaign",
  "bigidea":"God thinks in thousands of generations; we can barely see past our own. The generational life is simply learning to live inside His timeline instead of ours.",
  "ideal":"Anyone living only for their own lifespan; visionary and forward-thinking leaders.",
  "pairs":"Generations  \u00b7  Leaving a Lasting Legacy",
  "outcomes":["A generational mindset","Decisions made with descendants in view","A place in God\u2019s long story"]},

 {"n":"09","title":"Building a Spiritual Legacy","pos":"Legacy doesn\u2019t happen by accident \u2014 learn to build it, stone by stone.",
  "felt":"Building legacy intentionally","aud":"Church & Company",
  "summary":"A hands-on campaign on the deliberate construction of a spiritual legacy \u2014 the practices, stones of remembrance, and traditions that build what you\u2019ll leave.",
  "marketing":("Building a Spiritual Legacy is the practical workshop of the category. It moves from why legacy matters to how "
     "it\u2019s built \u2014 the deliberate practices, memorial stones, recorded stories, and traditions that construct a legacy of faith, brick by brick."),
  "problem":("A spiritual legacy doesn\u2019t happen by accident any more than a house builds itself. Yet most of us leave it to "
     "chance \u2014 hoping our faith somehow transfers, never doing the deliberate work of building something to leave. We admire others\u2019 legacies without realizing they were constructed, on purpose, stone by stone."),
  "transformation":("Participants learn to build a spiritual legacy intentionally \u2014 setting up stones of remembrance, recording "
     "their faith story, establishing traditions and written blessings \u2014 doing the deliberate, joyful work of constructing what they\u2019ll one day leave behind."),
  "sessions":[("No Legacy by Accident","Why what lasts has to be built."),("Stones of Remembrance","Marking what God has done so others ask."),
     ("Tell Them the Story","Recording a faith worth passing on."),("Traditions That Carry Faith","Building rhythms that outlive you."),
     ("The Written Blessing","Putting your legacy into words that remain."),("Building to Leave","The deliberate work of a lasting legacy.")],
  "scriptures":"Joshua 4:4\u20137  \u00b7  Proverbs 24:3\u20134  \u00b7  1 Chronicles 28:9\u201310  \u00b7  Psalm 102:18",
  "aud_full":"Church & Company \u2014 practical and hands-on; ideal for those ready to build.",
  "formats":"4-Session Series  \u00b7  21-Day Challenge  \u00b7  30-Day Devotional  \u00b7  40-Day Campaign",
  "bigidea":"No one drifts into a spiritual legacy. Like Joshua\u2019s stones by the river, it\u2019s built on purpose \u2014 marked, recorded, and handed down so the next generation stops to ask, \u2018What do these mean?\u2019",
  "ideal":"Those ready to do the practical work of building a legacy; intentional families.",
  "pairs":"Family Legacy  \u00b7  Family by Design",
  "outcomes":["A built, intentional legacy","Stones of remembrance and recorded faith","Traditions that outlive you"]},

 {"n":"10","title":"Passing Faith Forward","pos":"Faith is always one generation from being lost \u2014 don\u2019t drop the baton.",
  "felt":"The forward handoff","aud":"Church & Company",
  "summary":"A capstone campaign on the urgent handoff of faith \u2014 the relay where each generation must pass the baton forward, or watch faith fade in the next.",
  "marketing":("Passing Faith Forward is the category\u2019s urgent capstone. Drawing on the sobering account of a generation that "
     "grew up not knowing the Lord, it casts faith as a relay \u2014 a baton that must be deliberately passed forward, generation after generation, or dropped."),
  "problem":("Faith is always exactly one generation from being lost. Scripture records the chilling moment it happened \u2014 a "
     "generation arose that did not know the Lord or what He had done. It wasn\u2019t conquest that nearly ended Israel\u2019s faith; it was a failed handoff. The baton was simply never passed."),
  "transformation":("Participants take up the urgent, joyful work of passing faith forward \u2014 not only to their own children but "
     "to faithful others who will pass it on again \u2014 so that the baton keeps moving and no generation on their watch grows up not knowing the Lord."),
  "sessions":[("One Generation Away","How quickly faith can be lost."),("A Generation That Did Not Know","The warning of Judges 2."),
     ("The Relay of Faith","Why the handoff is everything."),("Entrust to Faithful People","Passing it beyond your own family."),
     ("Till I Declare It to the Next","A lifelong commitment to the handoff."),("Pass the Baton","Keeping faith moving forward on your watch.")],
  "scriptures":"2 Timothy 2:2  \u00b7  Judges 2:10  \u00b7  Psalm 71:18  \u00b7  Psalm 78:6\u20137",
  "aud_full":"Church & Company \u2014 an urgent, mobilizing capstone to the category.",
  "formats":"4-Session Series  \u00b7  21-Day Challenge  \u00b7  30-Day Devotional  \u00b7  40-Day Campaign",
  "bigidea":"Faith is never more than one generation from extinction. It isn\u2019t lost in a single dramatic blow \u2014 it\u2019s lost in a quiet, missed handoff. Your job is simply not to drop the baton.",
  "ideal":"Every believer; mobilizing and commissioning contexts.",
  "pairs":"Generations  \u00b7  Faith for Generations",
  "outcomes":["Urgency about passing faith on","A faith entrusted beyond your family","A handoff that doesn\u2019t drop"]},
 ],

 "library":[
  ("The Inheritance That Lasts", [
    ("Family Legacy","T2",True),("The Real Inheritance","T2",False),("More Than a Will","T2",False),
    ("What You Leave Behind","T2",False),("Treasures Worth Passing On","T2",False),("The Inheritance of Faith","T2",False),
    ("Beyond the Estate","T2",False),("A Heritage of Faith","T2",False),("Worth More Than Money","T2",False),
    ("The Gift You Pass Down","T2",False)]),
  ("A Legacy That Endures", [
    ("Leaving a Lasting Legacy","T2",True),("Remembered Forever","T2",False),("Finishing Well","T2",False),
    ("A Legacy That Lasts","T2",False),("To Children\u2019s Children","T2",False),("The Lasting Mark","T2",False),
    ("Built to Endure","T2",False),("A Life Worth Remembering","T2",False),("What Will Still Stand","T2",False),
    ("The Long View","T2",False)]),
  ("The Chain of Generations", [
    ("Generations","T2",True),("The Chain of Faith","T2",False),("Lois, Eunice, and Timothy","T2",False),
    ("Three Generations","T2",False),("The Strong Link","T2",False),("Honoring Those Before","T2",False),
    ("Faith Handed Down","T2",False),("Breaking and Building","T2",False),("The Generations Before Us","T2",False),
    ("Stronger Than You Found It","T2",False)]),
  ("Passing Faith to Your Children", [
    ("Faith for Generations","T2",True),("Impress Them on Your Children","T2",False),("Raising Kids Who Know God","T2",False),
    ("The Family Altar","T2",False),("Spiritual Parenting","T2",False),("Faith at Home","T2",False),
    ("As You Walk Along the Road","T2",False),("Discipling Your Children","T2",False),("Teaching the Next Generation","T2",False),
    ("Faith That Reaches Them","T2",False)]),
  ("Building Your Family on Purpose", [
    ("Family by Design","T2",True),("As for Me and My House","T2",False),("Your Family\u2019s Mission","T2",False),
    ("Building a Family Culture","T2",False),("Family Values","T2",False),("Drift or Design","T2",False),
    ("The Intentional Family","T2",False),("Family on Purpose","T2",False),("Rhythms That Shape Us","T2",False),
    ("A Household of Faith","T2",False)]),
  ("Legacy Living Today", [
    ("Legacy Living","T2",True),("Number Your Days","T2",False),("Begin with the End","T2",False),
    ("Living on Purpose","T2",False),("Today Is the Legacy","T2",False),("The Wisdom of Limits","T2",False),
    ("Make the Days Count","T2",False),("A Life Lived Forward","T2",False),("Living with the End in Mind","T2",False),
    ("Don\u2019t Wait for Someday","T2",False)]),
  ("The Blessing", [
    ("Blessing the Next Generation","T2",True),("The Spoken Blessing","T2",False),("The Lord Bless You","T2",False),
    ("Blessed by Name","T2",False),("Words of Blessing","T2",False),("The Father\u2019s Blessing","T2",False),
    ("Speaking Identity and Favor","T2",False),("Let the Children Come","T2",False),("A Family of Blessing","T2",False),
    ("The Gift of Words","T2",False)]),
  ("The Generational Mindset", [
    ("The Generational Life","T2",True),("To a Thousand Generations","T2",False),("One Generation to Another","T2",False),
    ("Thinking Generationally","T2",False),("Beyond Your Lifespan","T2",False),("Decisions for Descendants","T2",False),
    ("Praying Down the Line","T2",False),("A Bigger Story","T2",False),("The Long Timeline","T2",False),
    ("Living for Generations","T2",False)]),
  ("Building a Spiritual Legacy", [
    ("Building a Spiritual Legacy","T2",True),("Stones of Remembrance","T2",False),("Tell Them the Story","T2",False),
    ("No Legacy by Accident","T2",False),("The Written Blessing","T2",False),("Traditions That Last","T2",False),
    ("Recording Your Faith","T2",False),("Building to Leave","T2",False),("What Do These Stones Mean?","T2",False),
    ("The Legacy Project","T2",False)]),
  ("Passing Faith Forward", [
    ("Passing Faith Forward","T2",True),("Pass the Baton","T2",False),("One Generation Away","T2",False),
    ("The Relay of Faith","T2",False),("Entrust to Faithful People","T2",False),("Don\u2019t Drop the Baton","T2",False),
    ("A Generation That Knew the Lord","T2",False),("Keep Faith Moving","T2",False),("The Handoff","T2",False),
    ("Forward to the Next","T2",False)]),
 ],
}

doc, npages = build_catalog(cfg)
pathlib.Path("/tmp/family_legacy_catalog.html").write_text(doc, encoding="utf-8")
render_pdf("/tmp/family_legacy_catalog.html", "/tmp/family_legacy_catalog.pdf")
print("Family Legacy catalog:", npages, "pages")
