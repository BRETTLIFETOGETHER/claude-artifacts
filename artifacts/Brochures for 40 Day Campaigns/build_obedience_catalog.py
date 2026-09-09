# -*- coding: utf-8 -*-
import pathlib
from catalog_engine import build_catalog, render_pdf

cfg = {
 "category":"Following God",
 "doc_title":"Following God Campaign Library",
 "tier":"Tier 2",
 "accent":"#4b4a86",   # contemplative indigo
 "accent2":"#c19a4b",
 "positioning":("A complete library of 100 ready-to-run campaigns that help your church learn to hear God\u2019s voice, "
   "discern His leading, and respond with a wholehearted yes \u2014 turning hearing into a lifetime of joyfully following Him."),
 "why_matters":("Hearing and obeying God is the heartbeat of discipleship \u2014 and the place most believers feel the most "
   "uncertain. They long to hear from God and quietly wonder why He seems silent, or they hear clearly and struggle to obey. "
   "Few topics are more central to spiritual maturity, yet few are taught with practical, grace-filled clarity. A church that "
   "disciples its people to hear and follow God grows disciples who can actually be led."),
 "core_problem":("Most believers want to follow God but feel stuck between two gaps: a hearing gap \u2014 they aren\u2019t sure how to "
   "discern His voice \u2014 and a doing gap \u2014 they hear and hesitate. The result is a faith that admires obedience more than it "
   "practices it. Leaders sense the need but lack a ready, biblically grounded pathway to teach listening and obedience across "
   "the whole of life."),
 "transformation":("These campaigns move people from straining to hear toward a confident, responsive life of hearing and "
   "following God \u2014 noticing His voice, discerning His leading, obeying the nudge, and answering with a wholehearted yes."),
 "who_needs":[
   ("Churches","A complete discipleship pathway on hearing and obeying God \u2014 pastoral, practical, and deeply formational."),
   ("Small Groups &amp; Classes","Ready-made content for groups learning together to listen for and follow God\u2019s leading."),
   ("Pastors &amp; Leaders","A framework for forming a congregation that can be led by the Spirit, not just informed."),
   ("Individuals &amp; Families","A guided path to a more personal, responsive walk with God at home."),
 ],
 "outcomes":[
   "Greater confidence in hearing God\u2019s voice",
   "Growing discernment between God\u2019s voice and the noise",
   "A shift from hesitating to obeying promptly",
   "A responsive, surrendered, yielded heart",
   "A congregation that can be led by the Spirit",
   "Deeper intimacy and trust in everyday life",
 ],
 "use_cases":[
   ("Churchwide Formation Series","A whole-church journey into hearing and obeying God."),
   ("40-Day Spiritual Campaign","Weekend messages, small groups, and daily listening practices."),
   ("21-Day Listening Challenge","A short, focused experience learning to hear God\u2019s voice."),
   ("4-Week Sermon Companion","A focused message series with sermon-aligned small-group guides."),
   ("Small-Group &amp; Class Curriculum","Ready-made content for groups and classes."),
 ],
 "stats":[("100","Campaigns"),("10","Expanded"),("10","Themes"),("4","Formats"),("NIV","Scripture")],
 "components":["Daily Readings & Reflections","Six Group-Session Guides","Weekend Message Outlines",
               "Spiritual-Partner Prompts","Launch & Promotion Kit"],

 "top10":[
 {"n":"01","title":"Whispers","pos":"Learn to notice the quiet, gentle voice of God.",
  "felt":"Hearing God in the quiet","aud":"Church",
  "summary":"A foundational campaign that teaches people to quiet the noise and recognize the soft, gentle voice through which God most often speaks.",
  "marketing":("The flagship entry point for the category. Whispers addresses the most common frustration in the spiritual "
     "life \u2014 \u2018why is God silent?\u2019 \u2014 and reveals that the problem usually isn\u2019t God\u2019s silence, but our listening."),
  "problem":("Many of us are waiting for God to shout \u2014 a sign, an open door, an unmistakable word \u2014 and miss the way He most "
     "often speaks: softly. The problem usually isn\u2019t that God has gone silent. It\u2019s that His voice is quieter than the noise we\u2019ve surrounded ourselves with."),
  "transformation":("Participants learn to quiet the noise, slow down, and notice the gentle promptings of God they\u2019ve been "
     "missing \u2014 discovering that the same God who spoke to Elijah in a whisper is still speaking."),
  "sessions":[("Waiting for Thunder","Why we miss the voice we strain to hear."),("Not in the Wind","What Elijah learned about how God speaks."),
     ("Quieting the Noise","Turning down the volume to hear."),("The Gentle Voice","Recognizing the soft promptings we overlook."),
     ("Leaning In","Cultivating the stillness where God speaks."),("A Listening Life","Living attentive to the whisper.")],
  "scriptures":"1 Kings 19:11\u201313  \u00b7  Psalm 46:10  \u00b7  John 10:27  \u00b7  1 Samuel 3:10",
  "aud_full":"Church \u2014 the ideal on-ramp to the entire hearing-and-obedience category.",
  "formats":"4-Session Series  \u00b7  21-Day Challenge  \u00b7  30-Day Devotional  \u00b7  40-Day Campaign (recommended)",
  "bigidea":"God rarely competes with the noise. He whispers \u2014 and the whisper is only missed by those too busy or too loud to lean in and listen.",
  "ideal":"All-church on-ramps; anyone who wonders why God seems silent.",
  "pairs":"Listening for His Voice  \u00b7  Hearing and Responding",
  "outcomes":["Attentiveness to God\u2019s quiet voice","Less noise, more stillness","Confidence that God is speaking"]},

 {"n":"02","title":"Living Obedience","pos":"Turn what you hear from God into how you live.",
  "felt":"Obedience as a way of life","aud":"Church",
  "summary":"A campaign that closes the gap between hearing and doing \u2014 building the daily habit of actually obeying God\u2019s Word, not just admiring it.",
  "marketing":("Living Obedience confronts the most common spiritual stall: hearing clearly and obeying rarely. It moves people "
     "from admiring God\u2019s Word to actually doing what it says."),
  "problem":("It\u2019s possible to hear God clearly and still not obey Him. We nod along on Sunday, underline the verse, feel the "
     "conviction \u2014 and then live Monday exactly as we would have anyway. The gap is rarely a hearing problem; it\u2019s a doing problem."),
  "transformation":("Participants move from admiring God\u2019s Word to actually obeying it \u2014 building the daily habit of saying yes \u2014 "
     "until obedience stops being an occasional decision and becomes a settled way of life."),
  "sessions":[("The Hearing-Doing Gap","Why knowing isn\u2019t the same as following."),("Doers, Not Hearers","The self-deception of an unobeyed word."),
     ("The First Yes","Obeying before you understand the whole plan."),("Obedience in the Small","The everyday habit of saying yes."),
     ("When Obedience Costs","Following even when it\u2019s hard."),("A Yielded Life","Living so obedience becomes second nature.")],
  "scriptures":"James 1:22\u201325  \u00b7  Luke 6:46  \u00b7  John 14:15  \u00b7  Matthew 7:24\u201327",
  "aud_full":"Church \u2014 excellent for discipleship classes and groups serious about growth.",
  "formats":"4-Session Series  \u00b7  21-Day Challenge  \u00b7  30-Day Devotional  \u00b7  40-Day Campaign",
  "bigidea":"Hearing without doing isn\u2019t neutral \u2014 it\u2019s self-deception. Obedience is where faith stops being an idea and becomes a life.",
  "ideal":"Believers stuck between conviction and action; discipleship contexts.",
  "pairs":"Whispers  \u00b7  Daily Surrender",
  "outcomes":["A closed hearing-to-doing gap","Obedience as a daily habit","Faith that actually moves"]},

 {"n":"03","title":"Hearing and Responding","pos":"Learn the back-and-forth rhythm of walking with God.",
  "felt":"Responsive relationship","aud":"Church",
  "summary":"A relationship campaign that builds the responsive posture of young Samuel \u2014 moving from passive hearing to an active, willing yes.",
  "marketing":("Hearing and Responding builds the rhythm of a real relationship with God \u2014 not a one-way hotline, but a living "
     "back-and-forth of His speaking and our willing response."),
  "problem":("We often treat hearing from God as a one-way event \u2014 we ask, He answers, and the conversation ends. But Scripture "
     "pictures a living rhythm of God speaking and His people responding, and many of us have never learned how to actually answer when He speaks."),
  "transformation":("Participants learn the responsive posture of young Samuel \u2014 \u2018Speak, for your servant is listening\u2019 \u2014 moving "
     "from passive hearing to an active, willing yes, until walking with God becomes a real, ongoing conversation."),
  "sessions":[("More Than a Hotline","Hearing God as relationship, not request line."),("Speak, I\u2019m Listening","Samuel\u2019s posture of ready attentiveness."),
     ("The Willing Yes","Responding before you know the details."),("When the Answer Is Hard","Saying yes even when it stretches you."),
     ("Staying in the Conversation","Keeping the dialogue going."),("A Responsive Heart","Always ready to hear and answer.")],
  "scriptures":"1 Samuel 3:1\u201310  \u00b7  John 10:4  \u00b7  Revelation 3:20  \u00b7  Psalm 27:8",
  "aud_full":"Church \u2014 deepens a personal, responsive walk with God.",
  "formats":"4-Session Series  \u00b7  21-Day Challenge  \u00b7  30-Day Devotional  \u00b7  40-Day Campaign",
  "bigidea":"Hearing God isn\u2019t a transaction; it\u2019s a conversation. And every conversation needs a response \u2014 a willing \u2018yes, Lord\u2019 that keeps the relationship moving.",
  "ideal":"Those who hear from God but struggle to respond; relationship-focused groups.",
  "pairs":"Whispers  \u00b7  Saying Yes to God",
  "outcomes":["A responsive, two-way walk with God","A ready \u2018yes, Lord\u2019","Ongoing conversation with God"]},

 {"n":"04","title":"Prompted by God","pos":"Recognize and obey the Spirit\u2019s nudges in the moment.",
  "felt":"Spirit-led promptings","aud":"Church",
  "summary":"A real-time campaign that trains people to notice and act on the Holy Spirit\u2019s in-the-moment nudges \u2014 before the moment passes.",
  "marketing":("Prompted by God trains people to recognize and obey the Spirit\u2019s real-time leading \u2014 the nudges to call, to give, "
     "to speak \u2014 and to act before they explain them away."),
  "problem":("Most of us have felt it \u2014 a sudden nudge to call someone, to give, to speak up. And most of us have learned to "
     "second-guess it, explain it away, or ignore it. We\u2019re surrounded by quiet promptings and skilled at talking ourselves out of them."),
  "transformation":("Participants learn to recognize the Spirit\u2019s real-time leading \u2014 the way Philip was sent to a single chariot "
     "\u2014 and to act on it quickly, before the moment and the courage pass."),
  "sessions":[("The Nudge You Ignored","The promptings we talk ourselves out of."),("Led to the Chariot","How the Spirit guided Philip."),
     ("Was That God or Me?","Growing in discernment."),("Obey Quickly","Why promptings have a short shelf life."),
     ("Small Prompts, Big Stories","How ordinary nudges become moments."),("Led by the Spirit","Living attentive and ready to be sent.")],
  "scriptures":"Acts 8:26\u201340  \u00b7  Romans 8:14  \u00b7  John 16:13  \u00b7  Galatians 5:25",
  "aud_full":"Church \u2014 activating and practical; strong for outreach-minded congregations.",
  "formats":"4-Session Series  \u00b7  21-Day Challenge  \u00b7  30-Day Devotional  \u00b7  40-Day Campaign",
  "bigidea":"The Spirit still nudges. The question isn\u2019t whether God is prompting His people \u2014 it\u2019s whether we\u2019ll act on the prompt before we explain it away.",
  "ideal":"Believers wanting a more active, Spirit-led everyday faith.",
  "pairs":"Listening for His Voice  \u00b7  Following God\u2019s Whisper",
  "outcomes":["Quicker obedience to the Spirit","Sharper discernment of nudges","A more active, sent faith"]},

 {"n":"05","title":"Listening for His Voice","pos":"Build the discipline of discerning God\u2019s voice among the many.",
  "felt":"Discernment & practice","aud":"Church",
  "summary":"A discernment campaign that builds the practice of listening and the skill of telling God\u2019s voice apart from the thousand competing ones.",
  "marketing":("Listening for His Voice builds the discipline of discernment \u2014 the practice of making space, testing what you "
     "hear, and growing familiar enough with the Shepherd\u2019s voice to recognize it above the noise."),
  "problem":("We live in the noisiest era in history, surrounded by a thousand competing voices \u2014 culture, fear, the crowd, our "
     "own desires. The real challenge isn\u2019t only hearing God; it\u2019s telling His voice apart from all the others clamoring for our obedience."),
  "transformation":("Participants learn the practice of listening \u2014 making space, testing what they hear, and growing familiar "
     "with the Shepherd\u2019s voice \u2014 until they can recognize it, and follow it, above all the rest."),
  "sessions":[("A Thousand Voices","The voices competing for your obedience."),("The Shepherd\u2019s Voice","How sheep know the One they follow."),
     ("Making Space to Listen","The practice of unhurried attention."),("Testing What You Hear","Discerning God from the counterfeits."),
     ("Familiar with His Voice","The intimacy that recognizes Him."),("Following the Voice","Letting what you hear shape where you go.")],
  "scriptures":"John 10:1\u201327  \u00b7  1 John 4:1  \u00b7  Hebrews 5:14  \u00b7  Isaiah 30:21",
  "aud_full":"Church \u2014 a practical discipline-building campaign for all maturity levels.",
  "formats":"4-Session Series  \u00b7  21-Day Challenge  \u00b7  30-Day Devotional  \u00b7  40-Day Campaign",
  "bigidea":"Sheep don\u2019t follow a stranger \u2014 they know their Shepherd\u2019s voice. Discernment isn\u2019t a gift for a few; it\u2019s a familiarity anyone can grow.",
  "ideal":"Anyone confused by competing voices; spiritual-formation contexts.",
  "pairs":"Whispers  \u00b7  Prompted by God",
  "outcomes":["The discipline of listening","Discernment between voices","Familiarity with the Shepherd\u2019s voice"]},

 {"n":"06","title":"Radical Obedience","pos":"Embrace the costly, all-in obedience that changes everything.",
  "felt":"Costly obedience","aud":"Church",
  "summary":"A courage campaign that calls people past convenient obedience into the wholehearted, leave-the-nets obedience where life with God really begins.",
  "marketing":("Radical Obedience calls people past comfortable, convenient faith into the costly, all-in obedience Scripture "
     "celebrates \u2014 the kind that drops the nets and follows."),
  "problem":("Most of us are comfortable with convenient obedience \u2014 the kind that fits our schedule and never asks too much. "
     "But the obedience Scripture celebrates is rarely convenient: fishermen dropping their nets, a father climbing a mountain, a girl risking everything on a yes."),
  "transformation":("Participants confront the places they\u2019ve been negotiating with God \u2014 obeying up to a point \u2014 and find the "
     "courage for the wholehearted, leave-the-nets obedience where the real adventure with God begins."),
  "sessions":[("Convenient Obedience","The limits we place on our yes."),("Leave the Nets","The immediate, costly obedience of the first disciples."),
     ("The Negotiated Surrender","Obeying up to a point and no further."),("When Obedience Costs","Following when the price is real."),
     ("The Adventure Begins","Why the radical yes opens life up."),("All In","Living with nothing held back.")],
  "scriptures":"Matthew 4:18\u201322  \u00b7  Luke 9:57\u201362  \u00b7  Genesis 22:1\u201318  \u00b7  Luke 14:25\u201333",
  "aud_full":"Church \u2014 a faith-stretching campaign for committed disciples.",
  "formats":"4-Session Series  \u00b7  21-Day Challenge  \u00b7  30-Day Devotional  \u00b7  40-Day Campaign",
  "bigidea":"God rarely asks for a little. He asks for everything \u2014 and the radical, costly yes is the doorway to the very life with Him we long for.",
  "ideal":"Committed believers ready to go all-in; discipleship and missions contexts.",
  "pairs":"Living Obedience  \u00b7  Daily Surrender",
  "outcomes":["Courage for costly obedience","An end to negotiated faith","An all-in walk with God"]},

 {"n":"07","title":"Spirit-Led Decisions","pos":"Bring every choice under the guidance of God.",
  "felt":"Guidance & decisions","aud":"Church",
  "summary":"A guidance campaign that gives people a better way to decide \u2014 bringing their choices, big and small, under the Spirit\u2019s direction.",
  "marketing":("Spirit-Led Decisions gives people a better way to decide \u2014 trading pros-and-cons and gut feel for the guidance "
     "of the Spirit, trusting the God who makes paths straight."),
  "problem":("Life is a relentless series of decisions \u2014 jobs, moves, relationships, money \u2014 and most of us make them the way "
     "the world does: pros and cons, gut feel, hope for the best. We believe God guides, but rarely know how to invite His leading."),
  "transformation":("Participants learn to bring their choices \u2014 big and small \u2014 under the guidance of the Spirit, trusting the "
     "God who promises that those who submit their ways to Him will find their paths made straight."),
  "sessions":[("The Weight of Choosing","Why decisions drain us."),("Lean Not on Your Own","From self-reliance to Spirit-reliance."),
     ("Submit Your Ways","Inviting God into a decision."),("Open and Closed Doors","Reading God\u2019s leading without superstition."),
     ("Peace as a Compass","How God\u2019s peace confirms the way."),("Straight Paths","Living as someone consistently led.")],
  "scriptures":"Proverbs 3:5\u20136  \u00b7  Romans 12:2  \u00b7  James 1:5  \u00b7  Colossians 3:15",
  "aud_full":"Church \u2014 practical and widely applicable; strong for life\u2019s crossroads.",
  "formats":"4-Session Series  \u00b7  21-Day Challenge  \u00b7  30-Day Devotional  \u00b7  40-Day Campaign",
  "bigidea":"God cares about your decisions more than you do \u2014 and He\u2019s promised to guide the steps of anyone humble enough to ask. Guidance is available; we simply have to seek it.",
  "ideal":"Anyone facing decisions; young adults, leaders, and those at crossroads.",
  "pairs":"Prompted by God  \u00b7  Following God\u2019s Whisper",
  "outcomes":["A way to decide with God","Less anxious decision-making","Confidence in God\u2019s guidance"]},

 {"n":"08","title":"Following God\u2019s Whisper","pos":"Walk in the direction He quietly points, one step at a time.",
  "felt":"Following guidance","aud":"Church",
  "summary":"A faith-to-walk campaign that builds the courage to act on God\u2019s quiet guidance one obedient step at a time, even without the full map.",
  "marketing":("Following God\u2019s Whisper builds the faith to walk \u2014 to act on God\u2019s quiet, partial guidance one obedient step at "
     "a time, trusting the voice that says \u2018this is the way.\u2019"),
  "problem":("Sometimes the hardest part of obedience isn\u2019t hearing God \u2014 it\u2019s that what we hear is so small. A nudge toward a "
     "hard conversation, a quiet sense to wait or go. Rarely a floodlit map; usually just enough light for the next step. And when the whisper points somewhere uncertain, we stall."),
  "transformation":("Participants learn to act on God\u2019s quiet guidance one obedient step at a time \u2014 trusting the voice behind "
     "them saying \u2018this is the way\u2019 \u2014 even when they can\u2019t yet see where the path leads."),
  "sessions":[("Just Enough Light","Why God rarely shows the whole path."),("This Is the Way","Trusting the voice that points direction."),
     ("The Hesitation Habit","What keeps us from following."),("One Step at a Time","Obeying the guidance you have."),
     ("Following into the Unknown","Walking by faith when it\u2019s unclear."),("A Followed Life","Moving at God\u2019s whisper.")],
  "scriptures":"Isaiah 30:21  \u00b7  Psalm 119:105  \u00b7  Proverbs 16:9  \u00b7  Hebrews 11:8",
  "aud_full":"Church \u2014 strengthening for those in uncertain or transitional seasons.",
  "formats":"4-Session Series  \u00b7  21-Day Challenge  \u00b7  30-Day Devotional  \u00b7  40-Day Campaign",
  "bigidea":"God usually gives enough light for the next step, not the whole staircase. Following His whisper means trusting the step you can see to the God who sees the rest.",
  "ideal":"Those in uncertain seasons; anyone waiting for the \u2018whole plan\u2019 before moving.",
  "pairs":"Listening for His Voice  \u00b7  Spirit-Led Decisions",
  "outcomes":["Faith to take the next step","Less hesitation, more following","Trust amid uncertainty"]},

 {"n":"09","title":"Daily Surrender","pos":"Lay down your will before God, one morning at a time.",
  "felt":"Daily surrender","aud":"Church",
  "summary":"A surrender campaign that makes yielding a daily rhythm \u2014 laying down your own agenda each morning and praying \u2018not my will, but Yours.\u2019",
  "marketing":("Daily Surrender makes yielding a rhythm rather than a one-time event \u2014 teaching people to lay down their own "
     "agenda each morning and discover the freedom of a life no longer theirs to carry alone."),
  "problem":("We tend to think of surrender as a single, dramatic moment \u2014 an altar call, a one-time handing over of the keys. "
     "But our will doesn\u2019t stay surrendered. By breakfast the next day, we\u2019ve quietly taken back control. Surrender won\u2019t hold unless it\u2019s renewed, daily."),
  "transformation":("Participants learn to lay down their own agenda each morning \u2014 to pray \u2018not my will, but Yours\u2019 before the day "
     "takes over \u2014 and discover the unexpected freedom of a life that\u2019s no longer theirs to carry alone."),
  "sessions":[("The Surrender That Won\u2019t Hold","Why one-time yielding slips away."),("Take Up Your Cross Daily","The everyday rhythm Jesus described."),
     ("Not My Will","Praying Gethsemane\u2019s prayer in your own life."),("Reclaiming the Throne","How quickly we take control back."),
     ("The Freedom of Yielding","Why surrender becomes relief."),("Surrendered Today","The daily habit of laying it down.")],
  "scriptures":"Luke 9:23  \u00b7  Luke 22:42  \u00b7  Romans 12:1  \u00b7  Galatians 2:20",
  "aud_full":"Church \u2014 deeply formational; a strong fit for spiritual-renewal seasons.",
  "formats":"4-Session Series  \u00b7  21-Day Challenge  \u00b7  30-Day Devotional  \u00b7  40-Day Campaign",
  "bigidea":"Surrender isn\u2019t a one-time transaction; it\u2019s a daily renewal. The will you handed God yesterday has a way of climbing back onto the throne by morning.",
  "ideal":"Anyone wanting a more yielded daily walk; renewal and recommitment contexts.",
  "pairs":"Living Obedience  \u00b7  Radical Obedience",
  "outcomes":["A daily rhythm of surrender","A more yielded will","Freedom from carrying it all"]},

 {"n":"10","title":"Saying Yes to God","pos":"Offer a willing, available yes \u2014 before you even know the question.",
  "felt":"Availability & the yes","aud":"Church",
  "summary":"A campaign that cultivates a pre-decided yes \u2014 moving people from cautious, conditional answers to the open availability of \u2018Here am I. Send me.\u2019",
  "marketing":("Saying Yes to God cultivates a pre-decided yes \u2014 moving people from cautious, conditional answers to the open, "
     "willing availability God is always looking for."),
  "problem":("Many of us answer God conditionally. We want to know the cost, the plan, and the destination before we commit \u2014 a "
     "\u2018yes, if\u2019 rather than a \u2018yes, Lord.\u2019 But God rarely shows the whole assignment before the yes; He\u2019s looking for people available enough to say yes first."),
  "transformation":("Participants move from cautious, conditional answers to the open, willing availability of Isaiah \u2014 \u2018Here am "
     "I. Send me\u2019 \u2014 and discover the adventure that opens for those who say yes before they know exactly what they\u2019re agreeing to."),
  "sessions":[("Yes, If","The conditions we attach to our obedience."),("Here Am I","Isaiah\u2019s available, unconditional answer."),
     ("Yes Before the Question","Deciding your answer in advance."),("Mary\u2019s Yes","The trusting surrender of \u2018let it be to me.\u2019"),
     ("The Cost and the Joy","Counting both, and saying yes anyway."),("A Sent People","Living available to whatever God asks.")],
  "scriptures":"Isaiah 6:8  \u00b7  Luke 1:38  \u00b7  Matthew 4:19\u201320  \u00b7  Acts 9:6",
  "aud_full":"Church \u2014 a commissioning, momentum-building close to a season of growth.",
  "formats":"4-Session Series  \u00b7  21-Day Challenge  \u00b7  30-Day Devotional  \u00b7  40-Day Campaign",
  "bigidea":"God usually asks for the yes before He gives the details. The most usable people in His hands are simply the ones who\u2019ve already decided their answer is yes.",
  "ideal":"Anyone sensing a call; commissioning and mobilization contexts.",
  "pairs":"Hearing and Responding  \u00b7  Radical Obedience",
  "outcomes":["A pre-decided yes","Availability over hesitation","Readiness to be sent"]},
 ],

 "library":[
  ("Hearing God\u2019s Voice", [
    ("Whispers","T2",True),("The Still Small Voice","T2",False),("Learning to Hear God","T2",False),
    ("A Listening Heart","T2",False),("Quiet Enough to Hear","T2",False),("When God Speaks","T2",False),
    ("The Gentle Whisper","T2",False),("Ears to Hear","T2",False),("Hearing God Today","T2",False),
    ("The Voice We Miss","T2",False)]),
  ("Discernment & the Shepherd\u2019s Voice", [
    ("Listening for His Voice","T2",True),("The Shepherd\u2019s Voice","T2",False),("Knowing His Voice","T2",False),
    ("Discerning God\u2019s Will","T2",False),("Is That God or Me?","T2",False),("Testing What You Hear","T2",False),
    ("A Thousand Voices","T2",False),("The Discerning Heart","T2",False),("Tuning In","T2",False),
    ("Recognizing His Voice","T2",False)]),
  ("The Spirit\u2019s Promptings", [
    ("Prompted by God","T2",True),("Led by the Spirit","T2",False),("The Spirit\u2019s Nudge","T2",False),
    ("Obey the Nudge","T2",False),("Divine Appointments","T2",False),("Sensitive to the Spirit","T2",False),
    ("Following the Prompt","T2",False),("Spirit-Led Living","T2",False),("The Inner Witness","T2",False),
    ("Quick to Obey","T2",False)]),
  ("Living Obedience", [
    ("Living Obedience","T2",True),("Doers of the Word","T2",False),("Obedience as a Lifestyle","T2",False),
    ("The First Yes","T2",False),("Obey in the Small Things","T2",False),("When Obedience Is Hard","T2",False),
    ("Faith That Acts","T2",False),("The Obedient Walk","T2",False),("Hearing and Doing","T2",False),
    ("A Life of Obedience","T2",False)]),
  ("Radical & Costly Obedience", [
    ("Radical Obedience","T2",True),("Leave the Nets","T2",False),("All In","T2",False),
    ("Costly Obedience","T2",False),("The Hard Yes","T2",False),("Counting the Cost","T2",False),
    ("Wholehearted","T2",False),("No Holding Back","T2",False),("When God Asks Everything","T2",False),
    ("The Adventure of Obedience","T2",False)]),
  ("Guidance & Decisions", [
    ("Spirit-Led Decisions","T2",True),("Knowing God\u2019s Will","T2",False),("Straight Paths","T2",False),
    ("Open and Closed Doors","T2",False),("Deciding with God","T2",False),("Wisdom for the Crossroads","T2",False),
    ("Guided by Peace","T2",False),("Finding God\u2019s Direction","T2",False),("The Guided Life","T2",False),
    ("Lean Not on Your Own","T2",False)]),
  ("Following One Step at a Time", [
    ("Following God\u2019s Whisper","T2",True),("This Is the Way","T2",False),("One Step at a Time","T2",False),
    ("Just Enough Light","T2",False),("Walking by Faith","T2",False),("Following into the Unknown","T2",False),
    ("The Next Step","T2",False),("Trusting the Path","T2",False),("Step Out","T2",False),
    ("A Followed Life","T2",False)]),
  ("Surrender & the Yielded Will", [
    ("Daily Surrender","T2",True),("Not My Will","T2",False),("The Daily Cross","T2",False),
    ("Yielded","T2",False),("Take Up Your Cross","T2",False),("Surrendered Today","T2",False),
    ("The Freedom of Yielding","T2",False),("Letting Go and Letting God","T2",False),("A Surrendered Life","T2",False),
    ("Off the Throne","T2",False)]),
  ("Saying Yes & Availability", [
    ("Saying Yes to God","T2",True),("Here Am I","T2",False),("Send Me","T2",False),
    ("The Willing Yes","T2",False),("Yes Before the Question","T2",False),("Available to God","T2",False),
    ("Mary\u2019s Yes","T2",False),("An Unconditional Yes","T2",False),("Ready and Willing","T2",False),
    ("The Yes That Changes Everything","T2",False)]),
  ("A Responsive, Listening Life", [
    ("Hearing and Responding","T2",True),("Speak, Your Servant Is Listening","T2",False),("A Responsive Heart","T2",False),
    ("The Listening Life","T2",False),("Walking with God","T2",False),("In Step with the Spirit","T2",False),
    ("The Ongoing Conversation","T2",False),("Attentive to God","T2",False),("A Heart That Answers","T2",False),
    ("Living Responsively","T2",False)]),
 ],
}

doc, npages = build_catalog(cfg)
pathlib.Path("/tmp/following_god_catalog.html").write_text(doc, encoding="utf-8")
render_pdf("/tmp/following_god_catalog.html", "/tmp/following_god_catalog.pdf")
print("Following God catalog:", npages, "pages")
