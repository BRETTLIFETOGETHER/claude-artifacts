# -*- coding: utf-8 -*-
import pathlib
from catalog_engine import build_catalog, render_pdf

cfg = {
 "category":"Stewardship",
 "doc_title":"Stewardship Campaign Library",
 "accent":"#2f5d4a",   # stewardship deep green
 "accent2":"#c19a4b",
 "positioning":("A complete library of 100 ready-to-run stewardship campaigns that help churches, companies, "
   "and families manage all they\u2019ve been given \u2014 time, talent, treasure, trust, and testimony \u2014 as faithful stewards of God."),
 "why_matters":("Stewardship is the quiet master-theme of the Christian life \u2014 the truth that everything we have is "
   "entrusted, not owned. It touches money, time, gifts, influence, relationships, and the world itself, reframing the "
   "whole of life as a trust to manage well. Few topics are more biblical, more practical, or more freeing \u2014 yet most "
   "people have only ever heard \u2018stewardship\u2019 preached as a polite word for giving."),
 "core_problem":("Most people live as owners, not managers \u2014 gripping their time, money, and gifts as if they were theirs "
   "to spend however they please. Ownership is a heavy, anxious posture that quietly distorts every decision. Leaders sense "
   "the deeper biblical vision of stewardship but lack a ready, well-produced pathway to teach it across all of life."),
 "transformation":("These campaigns move people from owners to managers, from gripping to open hands, and from autopilot "
   "to intentional faithfulness \u2014 until they steward every part of life (time, talent, treasure, trust, and testimony) "
   "as a trust from God."),
 "who_needs":[
   ("Churches","A complete stewardship pathway that goes far beyond the annual giving push \u2014 pastoral, practical, and whole-life."),
   ("Companies","A framework for faithful, accountable management of talent, time, and resources that resonates in any workplace."),
   ("Advisors &amp; Donors","A values-aligned vision of stewardship to share with clients and partners who manage much."),
   ("Families","A way to raise children and order a household around faithful management rather than entitlement."),
 ],
 "outcomes":[
   "A clear identity shift from owner to manager",
   "Faithful management of time, money, gifts, and influence",
   "Reduced anxiety and a looser grip on possessions",
   "Increased generosity, trust, and intentionality",
   "Greater order and purpose across the whole of life",
   "A lasting legacy of faithful stewardship",
 ],
 "use_cases":[
   ("Churchwide Stewardship Series","A whole-life series that goes far beyond the annual giving push."),
   ("40-Day Spiritual Campaign","A full-church journey with weekend messages, small groups, and daily readings."),
   ("21-Day Workplace Challenge","A short, high-engagement experience on faithful management for a company or team."),
   ("4-Week Sermon Companion","A focused message series with sermon-aligned small-group guides."),
   ("Advisor &amp; Donor Resource","A premium resource gifted to clients, partners, and ministry supporters."),
 ],
 "stats":[("100","Campaigns"),("10","Expanded"),("10","Themes"),("4","Formats"),("NIV","Scripture")],
 "components":["Daily Readings & Reflections","Six Group-Session Guides","Weekend Message Outlines",
               "Spiritual-Partner Prompts","Launch & Promotion Kit"],

 "top10":[
 {"n":"01","title":"Life Stewardship","pos":"Manage your whole life \u2014 not just your money \u2014 as a trust from God.",
  "felt":"Whole-life stewardship","aud":"Church & Company",
  "summary":"The foundational campaign that expands stewardship beyond money to every area of life \u2014 time, talent, treasure, trust, and testimony.",
  "marketing":("The flagship entry point for the category. Life Stewardship lifts stewardship out of the offering plate and "
     "applies it to the whole of life, reframing everything a person holds as something entrusted, not owned."),
  "problem":("We tend to think of stewardship as a money word \u2014 something that comes up at offering time. But the truth is "
     "bigger and far more freeing: every part of our lives is on loan. Our hours, gifts, relationships, and influence are all entrusted."),
  "transformation":("Participants learn to see their entire life as something to manage well for God \u2014 time, talent, treasure, "
     "trust, and testimony \u2014 and discover the deep freedom of holding it all with open hands."),
  "sessions":[("The Five T\u2019s","Time, talent, treasure, trust, and testimony."),("Owner or Manager?","The shift that changes everything."),
     ("Stewarding Time","Managing your most limited resource."),("Stewarding Talent","Putting your gifts to work for God."),
     ("Stewarding Treasure","Holding money with open hands."),("A Faithful Life","Managing the whole of life well.")],
  "scriptures":"1 Peter 4:10  \u00b7  1 Corinthians 4:1\u20132  \u00b7  Psalm 24:1  \u00b7  Matthew 25:21",
  "aud_full":"Church & Company \u2014 the ideal on-ramp to the entire stewardship category.",
  "formats":"4-Session Series  \u00b7  21-Day Challenge  \u00b7  30-Day Devotional  \u00b7  40-Day Campaign (recommended)",
  "bigidea":"You don\u2019t own your life \u2014 you manage it. And the moment you accept that, everything you hold becomes lighter to carry and richer to give.",
  "ideal":"All-church on-ramps, new believers, and anyone who thinks stewardship is only about money.",
  "pairs":"Entrusted  \u00b7  Living as a Steward",
  "outcomes":["An owner-to-manager mindset","Faithful management of all five T\u2019s","A lighter grip and open hands"]},

 {"n":"02","title":"Entrusted","pos":"Receive the truth that everything you have is on loan from God.",
  "felt":"Ownership & trust","aud":"Church & Company",
  "summary":"A campaign built on the parable of the talents \u2014 everything we hold is entrusted, and one day we will give an account of how we managed it.",
  "marketing":("Entrusted goes to the root of stewardship: the radical idea that nothing is truly ours. It reframes life as a "
     "trust to be managed faithfully for an Owner who will one day return."),
  "problem":("We instinctively say \u2018my time, my money, my life\u2019 \u2014 as if we own it all outright. But Scripture insists we own "
     "nothing; we\u2019ve simply been entrusted with what belongs to God, and entrusted things come with accountability."),
  "transformation":("Participants trade the heavy posture of ownership for the freeing role of a trusted manager, learning to "
     "handle what they\u2019ve been given with faithfulness and joy."),
  "sessions":[("Nothing Is Ours","The truth that reframes everything."),("The Talents","Entrusted, and expected to invest."),
     ("The Master Returns","Living ready to give an account."),("Faithful with What\u2019s His","Managing God\u2019s resources well."),
     ("Buried or Invested?","Why playing it safe isn\u2019t faithful."),("Well Done","Living for the Owner\u2019s approval.")],
  "scriptures":"Matthew 25:14\u201330  \u00b7  Luke 16:12  \u00b7  1 Chronicles 29:14  \u00b7  Psalm 24:1",
  "aud_full":"Church & Company \u2014 a powerful theology-of-ownership reset for committed and new believers alike.",
  "formats":"4-Session Series  \u00b7  21-Day Challenge  \u00b7  30-Day Devotional  \u00b7  40-Day Campaign",
  "bigidea":"You will give an account not for what you owned, but for how you managed what was never yours to begin with.",
  "ideal":"Believers ready to reckon with ownership; strong for stewardship-season launches.",
  "pairs":"Life Stewardship  \u00b7  Faithful Stewardship",
  "outcomes":["Freedom from the ownership burden","An eternal, accountable perspective","Faithful handling of God\u2019s resources"]},

 {"n":"03","title":"Stewarding What Matters","pos":"Give your best management to the things that matter most.",
  "felt":"Priorities & focus","aud":"Church & Company",
  "summary":"A priorities campaign that aims stewardship at what is most important \u2014 soul, relationships, and calling \u2014 not just money and tasks.",
  "marketing":("Stewarding What Matters confronts a subtle failure: managing the urgent while neglecting the important. It "
     "helps people steward the things that will still matter in eternity."),
  "problem":("It\u2019s possible to be a diligent manager of all the wrong things \u2014 busy with the urgent while quietly neglecting "
     "the important. Many steward their inboxes and bank accounts carefully while letting their relationships, health, and souls run on empty."),
  "transformation":("Participants learn to identify and steward what matters most \u2014 their walk with God, their relationships, "
     "their calling \u2014 giving their best management to the things of lasting worth."),
  "sessions":[("Urgent vs. Important","Why we steward the wrong things."),("Stewarding Your Soul","Managing your interior life."),
     ("Stewarding Relationships","Tending what money can\u2019t buy."),("Stewarding Your Calling","Investing in your God-given purpose."),
     ("Stewarding Your Body","Caring for the temple you\u2019ve been given."),("First Things First","Ordering life around what lasts.")],
  "scriptures":"Matthew 6:33  \u00b7  Luke 10:41\u201342  \u00b7  Mark 8:36  \u00b7  Ephesians 5:15\u201316",
  "aud_full":"Church & Company \u2014 resonates with busy professionals and overextended families.",
  "formats":"4-Session Series  \u00b7  21-Day Challenge  \u00b7  30-Day Devotional  \u00b7  40-Day Campaign",
  "bigidea":"You can be a flawless manager of trivial things and a poor steward of your one and only life. What you steward matters as much as how well you steward it.",
  "ideal":"The busy and overextended; anyone managing everything but the important things.",
  "pairs":"Life Stewardship  \u00b7  The Stewarded Life",
  "outcomes":["Clear life priorities","Better-tended relationships and soul","A focus on what lasts"]},

 {"n":"04","title":"Faithful Stewardship","pos":"Prove faithful in the small things, and be trusted with more.",
  "felt":"Faithfulness in the small","aud":"Church & Company",
  "summary":"A faithfulness campaign rooted in \u2018whoever is faithful with little\u2019 \u2014 character built and trust earned in the small, unseen things.",
  "marketing":("Faithful Stewardship zeroes in on the quality God actually looks for: faithfulness. It shows that greatness in "
     "God\u2019s economy is built in the small, unglamorous, unseen places."),
  "problem":("We dream of being trusted with big things while quietly cutting corners on small ones. But God\u2019s economy runs in "
     "reverse: faithfulness in little is the prerequisite for being trusted with much."),
  "transformation":("Participants build the character of faithfulness in the small and unseen places, and position themselves "
     "to be entrusted with more."),
  "sessions":[("Faithful with Little","Where real stewardship begins."),("The Unseen Test","Character in the things no one sees."),
     ("Trusted with More","How faithfulness opens doors."),("The Cost of Cutting Corners","Why small compromises matter."),
     ("Diligence Over Flash","The quiet virtue God rewards."),("Good and Faithful","Living for the right verdict.")],
  "scriptures":"Luke 16:10  \u00b7  Matthew 25:21  \u00b7  1 Corinthians 4:2  \u00b7  Colossians 3:23",
  "aud_full":"Church & Company \u2014 excellent for workplaces, leaders, and discipleship contexts.",
  "formats":"4-Session Series  \u00b7  21-Day Challenge  \u00b7  30-Day Devotional  \u00b7  40-Day Campaign",
  "bigidea":"God doesn\u2019t entrust much to those who haven\u2019t been faithful with little. The big break you\u2019re waiting for is usually hiding inside the small thing you\u2019re neglecting.",
  "ideal":"Leaders, workplaces, and anyone wanting to be trusted with more.",
  "pairs":"Entrusted  \u00b7  Living as a Steward",
  "outcomes":["Integrity in the small things","Character that earns trust","Faithfulness as a way of life"]},

 {"n":"05","title":"Stewardship That Lasts","pos":"Steward your life for a harvest the next generation will enjoy.",
  "felt":"Legacy & the long view","aud":"Church & Company",
  "summary":"A legacy campaign \u2014 stewarding today for generations you\u2019ll never meet, planting trees whose shade you\u2019ll never sit in.",
  "marketing":("Stewardship That Lasts lifts people\u2019s eyes past their own lifetime, calling them to manage their resources and "
     "lives for a harvest their children\u2019s children will reap."),
  "problem":("We tend to steward for ourselves and our own horizon \u2014 this year, this decade, this life. But the most meaningful "
     "stewardship reaches beyond us, and a generation that only manages for itself leaves little behind."),
  "transformation":("Participants learn to steward with the long view \u2014 building, saving, and investing for a legacy of faith "
     "and provision that blesses generations to come."),
  "sessions":[("Planting Trees","Stewarding for shade you\u2019ll never sit in."),("An Inheritance for Their Children","The long view of legacy."),
     ("The Generational Mindset","Managing beyond your lifetime."),("Faith That Outlives You","Stewarding a spiritual legacy."),
     ("Building to Bless","Investing in those who come after."),("A Lasting Stewardship","Leaving more than you found.")],
  "scriptures":"Proverbs 13:22  \u00b7  Psalm 78:4\u20137  \u00b7  Deuteronomy 6:6\u20137  \u00b7  Psalm 145:4",
  "aud_full":"Church & Company \u2014 strong for parents, grandparents, and legacy-minded leaders and givers.",
  "formats":"4-Session Series  \u00b7  21-Day Challenge  \u00b7  30-Day Devotional  \u00b7  40-Day Campaign",
  "bigidea":"The truest stewards plant trees whose shade they\u2019ll never sit in. A life managed only for yourself ends with you; a life stewarded for others outlives you.",
  "ideal":"Parents, grandparents, and legacy-minded leaders and givers.",
  "pairs":"Life Stewardship  \u00b7  Kingdom Stewardship",
  "outcomes":["A multi-generational mindset","Intentional legacy building","Faith and provision that outlive you"]},

 {"n":"06","title":"Living as a Steward","pos":"Make stewardship a daily identity, not an occasional decision.",
  "felt":"Daily identity","aud":"Church & Company",
  "summary":"An identity campaign that turns stewardship from a one-time concept into a daily way of living and seeing.",
  "marketing":("Living as a Steward moves stewardship from idea to identity \u2014 a daily lens through which a person sees every "
     "hour, dollar, and decision as managed on God\u2019s behalf."),
  "problem":("Most of us treat stewardship as a topic we agree with rather than an identity we inhabit. We nod at the concept "
     "on Sunday and live like owners by Monday, because stewardship never became who we are."),
  "transformation":("Participants internalize the identity of a steward until it shapes their daily decisions, rhythms, and "
     "reflexes \u2014 seeing all of life as managed for God."),
  "sessions":[("More Than a Concept","Why stewardship has to become identity."),("The Steward\u2019s Eyes","Seeing everything as managed, not owned."),
     ("Daily Decisions","Stewardship in the small choices."),("The Steward\u2019s Rhythms","Habits that keep you faithful."),
     ("When No One\u2019s Watching","Stewardship as character."),("A Steward for Life","Living the identity for good.")],
  "scriptures":"1 Corinthians 4:1\u20132  \u00b7  Colossians 3:17  \u00b7  1 Peter 4:10  \u00b7  Titus 1:7",
  "aud_full":"Church & Company \u2014 ideal as a follow-up that cements stewardship as a lasting identity.",
  "formats":"4-Session Series  \u00b7  21-Day Challenge  \u00b7  30-Day Devotional  \u00b7  40-Day Campaign",
  "bigidea":"Stewardship was never meant to be a decision you make; it\u2019s a person you become. A steward doesn\u2019t manage well on occasion \u2014 they see all of life as managed.",
  "ideal":"Those ready to move stewardship from belief to lived identity.",
  "pairs":"Life Stewardship  \u00b7  The Stewarded Life",
  "outcomes":["A steward\u2019s identity and lens","Faithful daily decisions","Stewardship as second nature"]},

 {"n":"07","title":"Kingdom Stewardship","pos":"Manage all you\u2019ve been given for the King and His kingdom.",
  "felt":"Kingdom purpose","aud":"Church & Company",
  "summary":"A mission-driven campaign \u2014 stewarding resources, gifts, and influence for the advance of God\u2019s kingdom, not just personal security.",
  "marketing":("Kingdom Stewardship raises the aim of management from personal comfort to the King\u2019s purposes, calling people "
     "to deploy what they\u2019ve been given for something far bigger than themselves."),
  "problem":("Even faithful managers can aim their stewardship too low \u2014 at personal security, comfort, and provision alone. "
     "But we manage the King\u2019s resources for the King\u2019s purposes, and a stewardship that never serves the kingdom has missed its point."),
  "transformation":("Participants learn to steward their time, talent, and treasure for the advance of God\u2019s kingdom \u2014 putting "
     "what they manage to work for the mission."),
  "sessions":[("The King\u2019s Resources","Whose kingdom your stewardship serves."),("Put It to Work","The call to invest for the King."),
     ("Beyond Personal Security","Stewardship aimed higher."),("Kingdom Returns","Investing in what God is building."),
     ("Deployed for the Mission","Your gifts on kingdom assignment."),("For the King","Living as a kingdom steward.")],
  "scriptures":"Luke 19:11\u201327  \u00b7  Matthew 6:33  \u00b7  1 Corinthians 4:2  \u00b7  Matthew 25:21",
  "aud_full":"Church & Company \u2014 compelling for engaged believers and mission-minded marketplace leaders.",
  "formats":"4-Session Series  \u00b7  21-Day Challenge  \u00b7  30-Day Devotional  \u00b7  40-Day Campaign",
  "bigidea":"You\u2019re not managing your kingdom; you\u2019re managing His. The point of stewardship was never your security \u2014 it was the King\u2019s purposes.",
  "ideal":"Mission-minded believers and marketplace leaders.",
  "pairs":"Stewarding Your Influence  \u00b7  Stewardship That Lasts",
  "outcomes":["Kingdom-aimed stewardship","Resources deployed for mission","A bigger purpose for what you manage"]},

 {"n":"08","title":"The Stewarded Life","pos":"Bring every corner of your life under wise, faithful management.",
  "felt":"Order & wholeness","aud":"Church & Company",
  "summary":"A whole-life-order campaign that brings the scattered pieces of life \u2014 schedule, money, health, relationships \u2014 under one wise management.",
  "marketing":("The Stewarded Life is about order and wholeness \u2014 taking a scattered, reactive life and bringing each part "
     "under intentional, God-honoring management."),
  "problem":("Many lives are a collection of unmanaged areas \u2014 a chaotic schedule, drifting finances, neglected health, frayed "
     "relationships. The pieces run on their own with no one truly managing the whole, and the result is quiet chaos."),
  "transformation":("Participants bring each area of life under wise, intentional management, discovering the peace and "
     "effectiveness of a well-stewarded life."),
  "sessions":[("The Unmanaged Life","Naming the areas running on their own."),("Taking Inventory","An honest look at every area."),
     ("Ordering the Chaos","Bringing structure to the scattered."),("The Well-Managed Schedule","Stewarding your days."),
     ("Whole-Life Health","Managing body, mind, and soul."),("A Life in Order","The peace of being well-stewarded.")],
  "scriptures":"1 Corinthians 14:40  \u00b7  Proverbs 27:23\u201324  \u00b7  Ephesians 5:15\u201316  \u00b7  Luke 14:28",
  "aud_full":"Church & Company \u2014 a strong fit for those feeling scattered, overwhelmed, or out of order.",
  "formats":"4-Session Series  \u00b7  21-Day Challenge  \u00b7  30-Day Devotional  \u00b7  40-Day Campaign",
  "bigidea":"An unmanaged life doesn\u2019t stay neutral \u2014 it drifts toward chaos. The stewarded life is simply a life where every part has finally come under wise management.",
  "ideal":"The scattered and overwhelmed; anyone wanting their whole life in order.",
  "pairs":"Stewarding What Matters  \u00b7  Living as a Steward",
  "outcomes":["A well-ordered life","Each area intentionally managed","Peace in place of chaos"]},

 {"n":"09","title":"Stewarding Your Influence","pos":"Manage your reach, words, and example as a trust from God.",
  "felt":"Influence & example","aud":"Church & Company",
  "summary":"An influence campaign \u2014 every person has a platform of relationships and example to steward well for good.",
  "marketing":("Stewarding Your Influence treats reputation, relationships, words, and example as a trust to manage \u2014 helping "
     "people use the platform they already have for good."),
  "problem":("We assume influence belongs to leaders and celebrities and excuse ourselves from stewarding it. But every one of "
     "us has a platform \u2014 a circle of relationships, a reputation, a daily example \u2014 and influence left unmanaged is wasted or misused."),
  "transformation":("Participants learn to steward their influence \u2014 their words, example, and relationships \u2014 as a trust from "
     "God, using it intentionally to point others toward Him."),
  "sessions":[("You Have Influence","Recognizing the platform you already hold."),("A City on a Hill","Stewarding your visible example."),
     ("The Weight of Words","Managing what you say."),("Influence Up Close","Stewarding your closest relationships."),
     ("Influence on Purpose","Using your reach for good."),("A Faithful Witness","Stewarding influence for God\u2019s glory.")],
  "scriptures":"Matthew 5:14\u201316  \u00b7  Proverbs 22:1  \u00b7  Colossians 4:5\u20136  \u00b7  1 Timothy 4:12",
  "aud_full":"Church & Company \u2014 strong for leaders, parents, and anyone with a sphere of influence.",
  "formats":"4-Session Series  \u00b7  21-Day Challenge  \u00b7  30-Day Devotional  \u00b7  40-Day Campaign",
  "bigidea":"Influence isn\u2019t reserved for the famous \u2014 it\u2019s entrusted to everyone. The only question is whether you\u2019ll steward the platform you already have.",
  "ideal":"Leaders, parents, and anyone with a circle of relationships.",
  "pairs":"Kingdom Stewardship  \u00b7  Faithful Stewardship",
  "outcomes":["Awareness of your real influence","Words and example managed well","Influence used intentionally for good"]},

 {"n":"10","title":"Living Open-Handed","pos":"Hold everything loosely, with hands open to receive and release.",
  "felt":"Open hands & freedom","aud":"Church & Company",
  "summary":"A freedom campaign on the open-handed posture \u2014 holding possessions, plans, and people loosely before God.",
  "marketing":("Living Open-Handed addresses the clenched grip beneath so much anxiety, teaching the freeing posture of holding "
     "everything loosely \u2014 open to receive from God and open to release to others."),
  "problem":("The clenched fist is our default \u2014 we grip our money, our plans, even our people out of fear, as if holding "
     "tighter will keep them safe. But a closed hand can neither receive what God wants to give nor release what He asks."),
  "transformation":("Participants learn the open-handed posture of a steward \u2014 holding all they\u2019ve been given loosely, free to "
     "receive and free to release \u2014 and find the lightness that ownership could never give."),
  "sessions":[("The Clenched Fist","Why we grip what we have."),("The Lord Gave","Holding possessions loosely."),
     ("The Lord Has Taken Away","Trusting God when things are released."),("Open to Receive","Letting God give freely."),
     ("Open to Release","The freedom of letting go."),("An Open-Handed Life","Living light and free.")],
  "scriptures":"Acts 20:35  \u00b7  Job 1:21  \u00b7  1 Timothy 6:7  \u00b7  Ecclesiastes 5:15",
  "aud_full":"Church & Company \u2014 restorative and freeing; well-suited to seasons of change or loss.",
  "formats":"4-Session Series  \u00b7  21-Day Challenge  \u00b7  30-Day Devotional  \u00b7  40-Day Campaign",
  "bigidea":"A clenched fist can\u2019t receive and can\u2019t give. The open hand is the only posture that\u2019s free \u2014 free to be filled by God and free to bless others.",
  "ideal":"Anyone with a tight grip on possessions, plans, or control.",
  "pairs":"Life Stewardship  \u00b7  Stewardship That Lasts",
  "outcomes":["A loosened grip","Freedom from possession anxiety","Open hands to receive and release"]},
 ],

 "library":[
  ("Foundations of Stewardship", [
    ("Life Stewardship","T1",True),("Entrusted","T1",True),("Living as a Steward","T1",True),
    ("The Stewarded Life","T1",True),("Owner or Manager?","T1",False),("Whose Is It, Really?","T2",False),
    ("The Faithful Manager","T2",False),("Stewardship 101","T2",False),("The Heart of a Steward","T2",False),
    ("Everything Belongs to God","T2",False)]),
  ("Stewarding Time", [
    ("Redeeming the Time","T1",False),("The Gift of Today","T1",False),("Numbering Your Days","T1",False),
    ("Time Well Spent","T2",False),("The Stewarded Calendar","T2",False),("Margin & Rhythm","T2",False),
    ("First Things First","T2",False),("The Tyranny of Hurry","T2",False),("Sabbath & Stewardship","T2",False),
    ("Make It Count","T2",False)]),
  ("Stewarding Talent & Gifts", [
    ("Use Your Gifts","T1",False),("Created to Contribute","T1",False),("The Talents Entrusted","T1",False),
    ("Discover Your Design","T2",False),("Gifts on Purpose","T2",False),("Don\u2019t Bury It","T2",False),
    ("Serving with Your Strengths","T2",False),("The Gift of You","T2",False),("Called and Equipped","T2",False),
    ("Stewarding Your Potential","T2",False)]),
  ("Stewarding Treasure & Money", [
    ("Money as Stewardship","T1",False),("Faithful with Finances","T1",False),("The Steward\u2019s Wallet","T1",False),
    ("Managing God\u2019s Money","T2",False),("Open-Handed Finances","T2",False),("First Fruits","T2",False),
    ("The Generous Steward","T2",False),("Treasure in Heaven","T2",False),("Wise with Wealth","T2",False),
    ("Every Dollar Entrusted","T2",False)]),
  ("Stewarding Trust & Faithfulness", [
    ("Faithful Stewardship","T1",True),("Faithful with Little","T1",False),("Trusted with More","T1",False),
    ("The Faithfulness Factor","T2",False),("Integrity Unseen","T2",False),("Diligence & Devotion","T2",False),
    ("Proven Faithful","T2",False),("The Long Obedience","T2",False),("Well Done","T2",False),
    ("Counted Trustworthy","T2",False)]),
  ("Stewarding Testimony & Influence", [
    ("Stewarding Your Influence","T1",True),("A City on a Hill","T1",False),("The Weight of Words","T1",False),
    ("Your Everyday Witness","T2",False),("Influence on Purpose","T2",False),("Salt & Light","T2",False),
    ("The Stewarded Reputation","T2",False),("Leading by Example","T2",False),("Your Sphere of Influence","T2",False),
    ("A Faithful Witness","T2",False)]),
  ("Stewarding Body, Soul & Health", [
    ("Stewarding What Matters","T1",True),("The Temple Entrusted","T1",False),("Soul Care","T1",False),
    ("Body & Stewardship","T2",False),("Stewarding Your Mind","T2",False),("Rest & Renewal","T2",False),
    ("Healthy & Whole","T2",False),("Caring for the Vessel","T2",False),("Stewarding Your Energy","T2",False),
    ("First, Your Soul","T2",False)]),
  ("Stewarding Relationships & Home", [
    ("Stewarding Relationships","T1",False),("The Stewarded Home","T1",False),("Tending What Matters","T1",False),
    ("Faithful in Friendship","T2",False),("Stewarding Your Marriage","T2",False),("Stewarding Your Family","T2",False),
    ("Present & Faithful","T2",False),("The Gift of People","T2",False),("Investing in Others","T2",False),
    ("Households of Faith","T2",False)]),
  ("Kingdom & Legacy Stewardship", [
    ("Kingdom Stewardship","T1",True),("Stewardship That Lasts","T1",True),("Planting Trees","T1",False),
    ("An Inheritance That Lasts","T2",False),("For the King","T2",False),("Deployed for the Mission","T2",False),
    ("Generational Stewardship","T2",False),("Building to Bless","T2",False),("Kingdom Returns","T2",False),
    ("A Legacy of Faith","T2",False)]),
  ("The Open-Handed Life", [
    ("Living Open-Handed","T1",True),("Hold It Loosely","T1",False),("The Open Hand","T1",False),
    ("Free to Give","T2",False),("Content & Free","T2",False),("Loosening the Grip","T2",False),
    ("Receive and Release","T2",False),("The Unclenched Life","T2",False),("Enough in His Hands","T2",False),
    ("Travel Light","T2",False)]),
 ],
}

doc, npages = build_catalog(cfg)
pathlib.Path("/tmp/stewardship_catalog.html").write_text(doc, encoding="utf-8")
render_pdf("/tmp/stewardship_catalog.html", "/tmp/stewardship_catalog.pdf")
print("Stewardship catalog:", npages, "pages")
