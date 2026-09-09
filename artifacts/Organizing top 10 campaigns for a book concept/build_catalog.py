# -*- coding: utf-8 -*-
"""Obedience Campaign Library — v2 (reordered Top 10). Faithful rebuild of the
original catalog in the LifeTogether navy/gold editorial system, all copy verbatim.
New order: 01 Living Obedience · 02 Whispers · 03 Saying Yes to God · 04–10 shift down."""
import base64, os

FD = "fonts/fontsource-playfair-display-5.3.0/files"
FC = "fonts/fontsource-cormorant-garamond-5.3.0/files"

def b64(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()

FACES = []
def face(family, weight, style, path):
    FACES.append(
        "@font-face{font-family:'%s';font-weight:%d;font-style:%s;"
        "src:url(data:font/woff2;base64,%s) format('woff2');}" % (family, weight, style, b64(path))
    )

for w in (400, 500, 600, 700, 800, 900):
    face("Playfair Display", w, "normal", f"{FD}/playfair-display-latin-{w}-normal.woff2")
face("Playfair Display", 500, "italic", f"{FD}/playfair-display-latin-500-italic.woff2")
for w in (400, 500, 600, 700):
    face("Cormorant Garamond", w, "normal", f"{FC}/cormorant-garamond-latin-{w}-normal.woff2")
for w in (400, 500, 600):
    face("Cormorant Garamond", w, "italic", f"{FC}/cormorant-garamond-latin-{w}-italic.woff2")

# ---------------------------------------------------------------- campaign data
C = [
 dict(num="01", title="Living Obedience",
  tagline="Turn what you hear from God into how you live.",
  aag_label="OBEDIENCE AS A WAY OF LIFE",
  aag_desc="A campaign that closes the gap between hearing and doing — building the daily habit of actually obeying God\u2019s Word, not just admiring it.",
  intro="Living Obedience confronts the most common spiritual stall: hearing clearly and obeying rarely. It moves people from admiring God\u2019s Word to actually doing what it says.",
  big_idea="Hearing without doing isn\u2019t neutral — it\u2019s self-deception. Obedience is where faith stops being an idea and becomes a life.",
  problem="It\u2019s possible to hear God clearly and still not obey Him. We nod along on Sunday, underline the verse, feel the conviction — and then live Monday exactly as we would have anyway. The gap is rarely a hearing problem; it\u2019s a doing problem.",
  promise="Participants move from admiring God\u2019s Word to actually obeying it — building the daily habit of saying yes — until obedience stops being an occasional decision and becomes a settled way of life.",
  arc=[("The Hearing-Doing Gap","Why knowing isn\u2019t the same as following."),
       ("Doers, Not Hearers","The self-deception of an unobeyed word."),
       ("The First Yes","Obeying before you understand the whole plan."),
       ("Obedience in the Small","The everyday habit of saying yes."),
       ("When Obedience Costs","Following even when it\u2019s hard."),
       ("A Yielded Life","Living so obedience becomes second nature.")],
  outcomes="A closed hearing-to-doing gap \u00b7 Obedience as a daily habit \u00b7 Faith that actually moves",
  ideal="Believers stuck between conviction and action; discipleship contexts.",
  pairs="Whispers \u00b7 Daily Surrender",
  felt="Obedience as a way of life",
  scriptures="James 1:22\u201325 \u00b7 Luke 6:46 \u00b7 John 14:15 \u00b7 Matthew 7:24\u201327",
  audience="Church — excellent for discipleship classes and groups serious about growth.",
  flex="4-Session Series \u00b7 21-Day Challenge \u00b7 30-Day Devotional \u00b7 40-Day Campaign"),

 dict(num="02", title="Whispers",
  tagline="Learn to notice the quiet, gentle voice of God.",
  aag_label="HEARING GOD IN THE QUIET",
  aag_desc="A foundational campaign that teaches people to quiet the noise and recognize the soft, gentle voice through which God most often speaks.",
  intro="The flagship entry point for the category. Whispers addresses the most common frustration in the spiritual life — \u2018why is God silent?\u2019 — and reveals that the problem usually isn\u2019t God\u2019s silence, but our listening.",
  big_idea="God rarely competes with the noise. He whispers — and the whisper is only missed by those too busy or too loud to lean in and listen.",
  problem="Many of us are waiting for God to shout — a sign, an open door, an unmistakable word — and miss the way He most often speaks: softly. The problem usually isn\u2019t that God has gone silent. It\u2019s that His voice is quieter than the noise we\u2019ve surrounded ourselves with.",
  promise="Participants learn to quiet the noise, slow down, and notice the gentle promptings of God they\u2019ve been missing — discovering that the same God who spoke to Elijah in a whisper is still speaking.",
  arc=[("Waiting for Thunder","Why we miss the voice we strain to hear."),
       ("Not in the Wind","What Elijah learned about how God speaks."),
       ("Quieting the Noise","Turning down the volume to hear."),
       ("The Gentle Voice","Recognizing the soft promptings we overlook."),
       ("Leaning In","Cultivating the stillness where God speaks."),
       ("A Listening Life","Living attentive to the whisper.")],
  outcomes="Attentiveness to God\u2019s quiet voice \u00b7 Less noise, more stillness \u00b7 Confidence that God is speaking",
  ideal="All-church on-ramps; anyone who wonders why God seems silent.",
  pairs="Listening for His Voice \u00b7 Hearing and Responding",
  felt="Hearing God in the quiet",
  scriptures="1 Kings 19:11\u201313 \u00b7 Psalm 46:10 \u00b7 John 10:27 \u00b7 1 Samuel 3:10",
  audience="Church — the ideal on-ramp to the entire hearing-and-obedience category.",
  flex="4-Session Series \u00b7 21-Day Challenge \u00b7 30-Day Devotional \u00b7 40-Day Campaign (recommended)"),

 dict(num="03", title="Saying Yes to God",
  tagline="Offer a willing, available yes — before you even know the question.",
  aag_label="AVAILABILITY & THE YES",
  aag_desc="A campaign that cultivates a pre-decided yes — moving people from cautious, conditional answers to the open availability of \u2018Here am I. Send me.\u2019",
  intro="Saying Yes to God cultivates a pre-decided yes — moving people from cautious, conditional answers to the open, willing availability God is always looking for.",
  big_idea="God usually asks for the yes before He gives the details. The most usable people in His hands are simply the ones who\u2019ve already decided their answer is yes.",
  problem="Many of us answer God conditionally. We want to know the cost, the plan, and the destination before we commit — a \u2018yes, if\u2019 rather than a \u2018yes, Lord.\u2019 But God rarely shows the whole assignment before the yes; He\u2019s looking for people available enough to say yes first.",
  promise="Participants move from cautious, conditional answers to the open, willing availability of Isaiah — \u2018Here am I. Send me\u2019 — and discover the adventure that opens for those who say yes before they know exactly what they\u2019re agreeing to.",
  arc=[("Yes, If","The conditions we attach to our obedience."),
       ("Here Am I","Isaiah\u2019s available, unconditional answer."),
       ("Yes Before the Question","Deciding your answer in advance."),
       ("Mary\u2019s Yes","The trusting surrender of \u2018let it be to me.\u2019"),
       ("The Cost and the Joy","Counting both, and saying yes anyway."),
       ("A Sent People","Living available to whatever God asks.")],
  outcomes="A pre-decided yes \u00b7 Availability over hesitation \u00b7 Readiness to be sent",
  ideal="Anyone sensing a call; commissioning and mobilization contexts.",
  pairs="Hearing and Responding \u00b7 Radical Obedience",
  felt="Availability & the yes",
  scriptures="Isaiah 6:8 \u00b7 Luke 1:38 \u00b7 Matthew 4:19\u201320 \u00b7 Acts 9:6",
  audience="Church — a commissioning, momentum-building close to a season of growth.",
  flex="4-Session Series \u00b7 21-Day Challenge \u00b7 30-Day Devotional \u00b7 40-Day Campaign"),

 dict(num="04", title="Hearing and Responding",
  tagline="Learn the back-and-forth rhythm of walking with God.",
  aag_label="RESPONSIVE RELATIONSHIP",
  aag_desc="A relationship campaign that builds the responsive posture of young Samuel — moving from passive hearing to an active, willing yes.",
  intro="Hearing and Responding builds the rhythm of a real relationship with God — not a one-way hotline, but a living back-and-forth of His speaking and our willing response.",
  big_idea="Hearing God isn\u2019t a transaction; it\u2019s a conversation. And every conversation needs a response — a willing \u2018yes, Lord\u2019 that keeps the relationship moving.",
  problem="We often treat hearing from God as a one-way event — we ask, He answers, and the conversation ends. But Scripture pictures a living rhythm of God speaking and His people responding, and many of us have never learned how to actually answer when He speaks.",
  promise="Participants learn the responsive posture of young Samuel — \u2018Speak, for your servant is listening\u2019 — moving from passive hearing to an active, willing yes, until walking with God becomes a real, ongoing conversation.",
  arc=[("More Than a Hotline","Hearing God as relationship, not request line."),
       ("Speak, I\u2019m Listening","Samuel\u2019s posture of ready attentiveness."),
       ("The Willing Yes","Responding before you know the details."),
       ("When the Answer Is Hard","Saying yes even when it stretches you."),
       ("Staying in the Conversation","Keeping the dialogue going."),
       ("A Responsive Heart","Always ready to hear and answer.")],
  outcomes="A responsive, two-way walk with God \u00b7 A ready \u2018yes, Lord\u2019 \u00b7 Ongoing conversation with God",
  ideal="Those who hear from God but struggle to respond; relationship-focused groups.",
  pairs="Whispers \u00b7 Saying Yes to God",
  felt="Responsive relationship",
  scriptures="1 Samuel 3:1\u201310 \u00b7 John 10:4 \u00b7 Revelation 3:20 \u00b7 Psalm 27:8",
  audience="Church — deepens a personal, responsive walk with God.",
  flex="4-Session Series \u00b7 21-Day Challenge \u00b7 30-Day Devotional \u00b7 40-Day Campaign"),

 dict(num="05", title="Prompted by God",
  tagline="Recognize and obey the Spirit\u2019s nudges in the moment.",
  aag_label="SPIRIT-LED PROMPTINGS",
  aag_desc="A real-time campaign that trains people to notice and act on the Holy Spirit\u2019s in-the-moment nudges — before the moment passes.",
  intro="Prompted by God trains people to recognize and obey the Spirit\u2019s real-time leading — the nudges to call, to give, to speak — and to act before they explain them away.",
  big_idea="The Spirit still nudges. The question isn\u2019t whether God is prompting His people — it\u2019s whether we\u2019ll act on the prompt before we explain it away.",
  problem="Most of us have felt it — a sudden nudge to call someone, to give, to speak up. And most of us have learned to second-guess it, explain it away, or ignore it. We\u2019re surrounded by quiet promptings and skilled at talking ourselves out of them.",
  promise="Participants learn to recognize the Spirit\u2019s real-time leading — the way Philip was sent to a single chariot — and to act on it quickly, before the moment and the courage pass.",
  arc=[("The Nudge You Ignored","The promptings we talk ourselves out of."),
       ("Led to the Chariot","How the Spirit guided Philip."),
       ("Was That God or Me?","Growing in discernment."),
       ("Obey Quickly","Why promptings have a short shelf life."),
       ("Small Prompts, Big Stories","How ordinary nudges become moments."),
       ("Led by the Spirit","Living attentive and ready to be sent.")],
  outcomes="Quicker obedience to the Spirit \u00b7 Sharper discernment of nudges \u00b7 A more active, sent faith",
  ideal="Believers wanting a more active, Spirit-led everyday faith.",
  pairs="Listening for His Voice \u00b7 Following God\u2019s Whisper",
  felt="Spirit-led promptings",
  scriptures="Acts 8:26\u201340 \u00b7 Romans 8:14 \u00b7 John 16:13 \u00b7 Galatians 5:25",
  audience="Church — activating and practical; strong for outreach-minded congregations.",
  flex="4-Session Series \u00b7 21-Day Challenge \u00b7 30-Day Devotional \u00b7 40-Day Campaign"),

 dict(num="06", title="Listening for His Voice",
  tagline="Build the discipline of discerning God\u2019s voice among the many.",
  aag_label="DISCERNMENT & PRACTICE",
  aag_desc="A discernment campaign that builds the practice of listening and the skill of telling God\u2019s voice apart from the thousand competing ones.",
  intro="Listening for His Voice builds the discipline of discernment — the practice of making space, testing what you hear, and growing familiar enough with the Shepherd\u2019s voice to recognize it above the noise.",
  big_idea="Sheep don\u2019t follow a stranger — they know their Shepherd\u2019s voice. Discernment isn\u2019t a gift for a few; it\u2019s a familiarity anyone can grow.",
  problem="We live in the noisiest era in history, surrounded by a thousand competing voices — culture, fear, the crowd, our own desires. The real challenge isn\u2019t only hearing God; it\u2019s telling His voice apart from all the others clamoring for our obedience.",
  promise="Participants learn the practice of listening — making space, testing what they hear, and growing familiar with the Shepherd\u2019s voice — until they can recognize it, and follow it, above all the rest.",
  arc=[("A Thousand Voices","The voices competing for your obedience."),
       ("The Shepherd\u2019s Voice","How sheep know the One they follow."),
       ("Making Space to Listen","The practice of unhurried attention."),
       ("Testing What You Hear","Discerning God from the counterfeits."),
       ("Familiar with His Voice","The intimacy that recognizes Him."),
       ("Following the Voice","Letting what you hear shape where you go.")],
  outcomes="The discipline of listening \u00b7 Discernment between voices \u00b7 Familiarity with the Shepherd\u2019s voice",
  ideal="Anyone confused by competing voices; spiritual-formation contexts.",
  pairs="Whispers \u00b7 Prompted by God",
  felt="Discernment & practice",
  scriptures="John 10:1\u201327 \u00b7 1 John 4:1 \u00b7 Hebrews 5:14 \u00b7 Isaiah 30:21",
  audience="Church — a practical discipline-building campaign for all maturity levels.",
  flex="4-Session Series \u00b7 21-Day Challenge \u00b7 30-Day Devotional \u00b7 40-Day Campaign"),

 dict(num="07", title="Radical Obedience",
  tagline="Embrace the costly, all-in obedience that changes everything.",
  aag_label="COSTLY OBEDIENCE",
  aag_desc="A courage campaign that calls people past convenient obedience into the wholehearted, leave-the-nets obedience where life with God really begins.",
  intro="Radical Obedience calls people past comfortable, convenient faith into the costly, all-in obedience Scripture celebrates — the kind that drops the nets and follows.",
  big_idea="God rarely asks for a little. He asks for everything — and the radical, costly yes is the doorway to the very life with Him we long for.",
  problem="Most of us are comfortable with convenient obedience — the kind that fits our schedule and never asks too much. But the obedience Scripture celebrates is rarely convenient: fishermen dropping their nets, a father climbing a mountain, a girl risking everything on a yes.",
  promise="Participants confront the places they\u2019ve been negotiating with God — obeying up to a point — and find the courage for the wholehearted, leave-the-nets obedience where the real adventure with God begins.",
  arc=[("Convenient Obedience","The limits we place on our yes."),
       ("Leave the Nets","The immediate, costly obedience of the first disciples."),
       ("The Negotiated Surrender","Obeying up to a point and no further."),
       ("When Obedience Costs","Following when the price is real."),
       ("The Adventure Begins","Why the radical yes opens life up."),
       ("All In","Living with nothing held back.")],
  outcomes="Courage for costly obedience \u00b7 An end to negotiated faith \u00b7 An all-in walk with God",
  ideal="Committed believers ready to go all-in; discipleship and missions contexts.",
  pairs="Living Obedience \u00b7 Daily Surrender",
  felt="Costly obedience",
  scriptures="Matthew 4:18\u201322 \u00b7 Luke 9:57\u201362 \u00b7 Genesis 22:1\u201318 \u00b7 Luke 14:25\u201333",
  audience="Church — a faith-stretching campaign for committed disciples.",
  flex="4-Session Series \u00b7 21-Day Challenge \u00b7 30-Day Devotional \u00b7 40-Day Campaign"),

 dict(num="08", title="Spirit-Led Decisions",
  tagline="Bring every choice under the guidance of God.",
  aag_label="GUIDANCE & DECISIONS",
  aag_desc="A guidance campaign that gives people a better way to decide — bringing their choices, big and small, under the Spirit\u2019s direction.",
  intro="Spirit-Led Decisions gives people a better way to decide — trading pros-and-cons and gut feel for the guidance of the Spirit, trusting the God who makes paths straight.",
  big_idea="God cares about your decisions more than you do — and He\u2019s promised to guide the steps of anyone humble enough to ask. Guidance is available; we simply have to seek it.",
  problem="Life is a relentless series of decisions — jobs, moves, relationships, money — and most of us make them the way the world does: pros and cons, gut feel, hope for the best. We believe God guides, but rarely know how to invite His leading.",
  promise="Participants learn to bring their choices — big and small — under the guidance of the Spirit, trusting the God who promises that those who submit their ways to Him will find their paths made straight.",
  arc=[("The Weight of Choosing","Why decisions drain us."),
       ("Lean Not on Your Own","From self-reliance to Spirit-reliance."),
       ("Submit Your Ways","Inviting God into a decision."),
       ("Open and Closed Doors","Reading God\u2019s leading without superstition."),
       ("Peace as a Compass","How God\u2019s peace confirms the way."),
       ("Straight Paths","Living as someone consistently led.")],
  outcomes="A way to decide with God \u00b7 Less anxious decision-making \u00b7 Confidence in God\u2019s guidance",
  ideal="Anyone facing decisions; young adults, leaders, and those at crossroads.",
  pairs="Prompted by God \u00b7 Following God\u2019s Whisper",
  felt="Guidance & decisions",
  scriptures="Proverbs 3:5\u20136 \u00b7 Romans 12:2 \u00b7 James 1:5 \u00b7 Colossians 3:15",
  audience="Church — practical and widely applicable; strong for life\u2019s crossroads.",
  flex="4-Session Series \u00b7 21-Day Challenge \u00b7 30-Day Devotional \u00b7 40-Day Campaign"),

 dict(num="09", title="Following God\u2019s Whisper",
  tagline="Walk in the direction He quietly points, one step at a time.",
  aag_label="FOLLOWING GUIDANCE",
  aag_desc="A faith-to-walk campaign that builds the courage to act on God\u2019s quiet guidance one obedient step at a time, even without the full map.",
  intro="Following God\u2019s Whisper builds the faith to walk — to act on God\u2019s quiet, partial guidance one obedient step at a time, trusting the voice that says \u2018this is the way.\u2019",
  big_idea="God usually gives enough light for the next step, not the whole staircase. Following His whisper means trusting the step you can see to the God who sees the rest.",
  problem="Sometimes the hardest part of obedience isn\u2019t hearing God — it\u2019s that what we hear is so small. A nudge toward a hard conversation, a quiet sense to wait or go. Rarely a floodlit map; usually just enough light for the next step. And when the whisper points somewhere uncertain, we stall.",
  promise="Participants learn to act on God\u2019s quiet guidance one obedient step at a time — trusting the voice behind them saying \u2018this is the way\u2019 — even when they can\u2019t yet see where the path leads.",
  arc=[("Just Enough Light","Why God rarely shows the whole path."),
       ("This Is the Way","Trusting the voice that points direction."),
       ("The Hesitation Habit","What keeps us from following."),
       ("One Step at a Time","Obeying the guidance you have."),
       ("Following into the Unknown","Walking by faith when it\u2019s unclear."),
       ("A Followed Life","Moving at God\u2019s whisper.")],
  outcomes="Faith to take the next step \u00b7 Less hesitation, more following \u00b7 Trust amid uncertainty",
  ideal="Those in uncertain seasons; anyone waiting for the \u2018whole plan\u2019 before moving.",
  pairs="Listening for His Voice \u00b7 Spirit-Led Decisions",
  felt="Following guidance",
  scriptures="Isaiah 30:21 \u00b7 Psalm 119:105 \u00b7 Proverbs 16:9 \u00b7 Hebrews 11:8",
  audience="Church — strengthening for those in uncertain or transitional seasons.",
  flex="4-Session Series \u00b7 21-Day Challenge \u00b7 30-Day Devotional \u00b7 40-Day Campaign"),

 dict(num="10", title="Daily Surrender",
  tagline="Lay down your will before God, one morning at a time.",
  aag_label="DAILY SURRENDER",
  aag_desc="A surrender campaign that makes yielding a daily rhythm — laying down your own agenda each morning and praying \u2018not my will, but Yours.\u2019",
  intro="Daily Surrender makes yielding a rhythm rather than a one-time event — teaching people to lay down their own agenda each morning and discover the freedom of a life no longer theirs to carry alone.",
  big_idea="Surrender isn\u2019t a one-time transaction; it\u2019s a daily renewal. The will you handed God yesterday has a way of climbing back onto the throne by morning.",
  problem="We tend to think of surrender as a single, dramatic moment — an altar call, a one-time handing over of the keys. But our will doesn\u2019t stay surrendered. By breakfast the next day, we\u2019ve quietly taken back control. Surrender won\u2019t hold unless it\u2019s renewed, daily.",
  promise="Participants learn to lay down their own agenda each morning — to pray \u2018not my will, but Yours\u2019 before the day takes over — and discover the unexpected freedom of a life that\u2019s no longer theirs to carry alone.",
  arc=[("The Surrender That Won\u2019t Hold","Why one-time yielding slips away."),
       ("Take Up Your Cross Daily","The everyday rhythm Jesus described."),
       ("Not My Will","Praying Gethsemane\u2019s prayer in your own life."),
       ("Reclaiming the Throne","How quickly we take control back."),
       ("The Freedom of Yielding","Why surrender becomes relief."),
       ("Surrendered Today","The daily habit of laying it down.")],
  outcomes="A daily rhythm of surrender \u00b7 A more yielded will \u00b7 Freedom from carrying it all",
  ideal="Anyone wanting a more yielded daily walk; renewal and recommitment contexts.",
  pairs="Living Obedience \u00b7 Radical Obedience",
  felt="Daily surrender",
  scriptures="Luke 9:23 \u00b7 Luke 22:42 \u00b7 Romans 12:1 \u00b7 Galatians 2:20",
  audience="Church — deeply formational; a strong fit for spiritual-renewal seasons.",
  flex="4-Session Series \u00b7 21-Day Challenge \u00b7 30-Day Devotional \u00b7 40-Day Campaign"),
]

THEMES_P1 = [
 ("HEARING GOD\u2019S VOICE", ["Whispers \u2605","The Still Small Voice","Learning to Hear God","A Listening Heart","Quiet Enough to Hear","When God Speaks","The Gentle Whisper","Ears to Hear","Hearing God Today","The Voice We Miss"]),
 ("DISCERNMENT & THE SHEPHERD\u2019S VOICE", ["Listening for His Voice \u2605","The Shepherd\u2019s Voice","Knowing His Voice","Discerning God\u2019s Will","Is That God or Me?","Testing What You Hear","A Thousand Voices","The Discerning Heart","Tuning In","Recognizing His Voice"]),
 ("THE SPIRIT\u2019S PROMPTINGS", ["Prompted by God \u2605","Led by the Spirit","The Spirit\u2019s Nudge","Obey the Nudge","Divine Appointments","Sensitive to the Spirit","Following the Prompt","Spirit-Led Living","The Inner Witness","Quick to Obey"]),
 ("LIVING OBEDIENCE", ["Living Obedience \u2605","Doers of the Word","Obedience as a Lifestyle","The First Yes","Obey in the Small Things","When Obedience Is Hard","Faith That Acts","The Obedient Walk","Hearing and Doing","A Life of Obedience"]),
 ("RADICAL & COSTLY OBEDIENCE", ["Radical Obedience \u2605","Leave the Nets","All In","Costly Obedience","The Hard Yes","Counting the Cost","Wholehearted","No Holding Back","When God Asks Everything","The Adventure of Obedience"]),
]
THEMES_P2 = [
 ("GUIDANCE & DECISIONS", ["Spirit-Led Decisions \u2605","Knowing God\u2019s Will","Straight Paths","Open and Closed Doors","Deciding with God","Wisdom for the Crossroads","Guided by Peace","Finding God\u2019s Direction","The Guided Life","Lean Not on Your Own"]),
 ("FOLLOWING ONE STEP AT A TIME", ["Following God\u2019s Whisper \u2605","This Is the Way","One Step at a Time","Just Enough Light","Walking by Faith","Following into the Unknown","The Next Step","Trusting the Path","Step Out","A Followed Life"]),
 ("SURRENDER & THE YIELDED WILL", ["Daily Surrender \u2605","Not My Will","The Daily Cross","Yielded","Take Up Your Cross","Surrendered Today","The Freedom of Yielding","Letting Go and Letting God","A Surrendered Life","Off the Throne"]),
 ("SAYING YES & AVAILABILITY", ["Saying Yes to God \u2605","Here Am I","Send Me","The Willing Yes","Yes Before the Question","Available to God","Mary\u2019s Yes","An Unconditional Yes","Ready and Willing","The Yes That Changes Everything"]),
 ("A RESPONSIVE, LISTENING LIFE", ["Hearing and Responding \u2605","Speak, Your Servant Is Listening","A Responsive Heart","The Listening Life","Walking with God","In Step with the Spirit","The Ongoing Conversation","Attentive to God","A Heart That Answers","Living Responsively"]),
]

# ---------------------------------------------------------------- CSS
CSS = """
%(faces)s
:root{}
*{margin:0;padding:0;box-sizing:border-box;}
@page{size:letter;margin:0.52in 0.72in 0.62in 0.72in;
  @bottom-left{content:"O B E D I E N C E   \\00b7   C A M P A I G N   C A T A L O G";font-family:'Liberation Sans',Helvetica,Arial,sans-serif;font-size:5.4pt;letter-spacing:0.08em;color:#9a958a;}
  @bottom-right{content:"P A G E  " counter(page);font-family:'Liberation Sans',Helvetica,Arial,sans-serif;font-size:5.4pt;letter-spacing:0.08em;color:#9a958a;}
}
@page cover{
  @bottom-left{content:none;} @bottom-right{content:none;}
}
body{font-family:'Cormorant Garamond',serif;color:#33405c;font-size:9.6pt;line-height:1.42;}
.page{page-break-after:always;position:relative;}
.page:last-child{page-break-after:avoid;}
.cover{page:cover;}

/* ---- shared header strip ---- */
.strip{display:flex;justify-content:space-between;align-items:baseline;border-bottom:0.75pt solid #d9d3c4;padding-bottom:5pt;margin-bottom:11pt;}
.strip .l{font-family:'Liberation Sans',Helvetica,Arial,sans-serif;font-size:6.2pt;letter-spacing:0.22em;color:#1c2b4d;font-weight:bold;}
.strip .l span{color:#a49e8f;font-weight:normal;letter-spacing:0.2em;}
.strip .r{font-family:'Liberation Sans',Helvetica,Arial,sans-serif;font-size:6.2pt;letter-spacing:0.24em;color:#a49e8f;}

.lbl{font-family:'Liberation Sans',Helvetica,Arial,sans-serif;font-size:6.4pt;letter-spacing:0.18em;color:#1c2b4d;font-weight:bold;margin-bottom:4pt;}
.lbl.gold{color:#b08a2e;}
.lbl.mut{color:#a49e8f;}

/* ---- cover ---- */
.cv-title{font-family:'Playfair Display',serif;font-weight:800;font-size:46pt;color:#1c2b4d;line-height:1.02;margin:16pt 0 4pt;}
.cv-sub{font-family:'Liberation Sans',Helvetica,Arial,sans-serif;font-size:9pt;letter-spacing:0.42em;color:#b08a2e;margin-bottom:13pt;}
.cv-lead{font-family:'Cormorant Garamond',serif;font-size:12.4pt;line-height:1.5;color:#33405c;max-width:6.3in;margin-bottom:15pt;}
.cv-rule{border-top:1.4pt solid #1c2b4d;margin-bottom:13pt;}
.cv-cols{display:flex;gap:0.32in;margin-bottom:13pt;}
.cv-cols .a{flex:1.15;}
.cv-cols .b{flex:1;border-left:0.75pt solid #d9d3c4;padding-left:0.28in;}
.cv-blk{margin-bottom:11pt;}
.cv-blk p{font-size:9.4pt;line-height:1.45;}
.who{margin-bottom:9pt;}
.who .t{font-family:'Playfair Display',serif;font-weight:700;font-size:10.6pt;color:#1c2b4d;margin-bottom:1pt;}
.who p{font-size:9.1pt;line-height:1.38;color:#4a5570;}
.cv-band{display:flex;gap:0.34in;border-top:0.75pt solid #d9d3c4;padding-top:11pt;margin-bottom:13pt;}
.cv-band .col{flex:1;}
.ol li{list-style:none;font-size:9.4pt;line-height:1.5;padding-left:11pt;position:relative;}
.ol li:before{content:"\\00b7";position:absolute;left:2pt;color:#b08a2e;font-weight:bold;}
.uc{margin-bottom:5pt;font-size:9.3pt;line-height:1.34;}
.uc b{font-family:'Playfair Display',serif;font-weight:700;font-size:9.4pt;color:#1c2b4d;}
.stats{display:flex;border-top:1.4pt solid #1c2b4d;border-bottom:0.75pt solid #d9d3c4;padding:10pt 0;}
.stats .s{flex:1;text-align:center;border-left:0.75pt solid #d9d3c4;}
.stats .s:first-child{border-left:none;}
.stats .n{font-family:'Playfair Display',serif;font-weight:800;font-size:19pt;color:#1c2b4d;line-height:1;}
.stats .k{font-family:'Liberation Sans',Helvetica,Arial,sans-serif;font-size:5.8pt;letter-spacing:0.2em;color:#a49e8f;margin-top:3pt;}

/* ---- top 10 at a glance ---- */
.aag-h{font-family:'Playfair Display',serif;font-weight:800;font-size:23pt;color:#1c2b4d;margin-bottom:5pt;}
.aag-intro{font-size:10.6pt;line-height:1.45;color:#4a5570;max-width:6.1in;margin-bottom:11pt;}
.aag{display:flex;border-top:0.75pt solid #e2ddd0;padding:6.4pt 0 5.6pt;}
.aag .n{font-family:'Playfair Display',serif;font-weight:800;font-size:15pt;color:#c9c3b2;width:0.42in;flex:none;line-height:1.1;}
.aag .m{flex:1;padding-right:0.25in;}
.aag .t{font-family:'Playfair Display',serif;font-weight:800;font-size:12.6pt;color:#1c2b4d;line-height:1.1;display:inline;}
.aag .tag{font-family:'Cormorant Garamond',serif;font-style:italic;font-size:10.2pt;color:#8a7a33;margin:1pt 0 2pt;}
.aag .d{font-size:9.1pt;line-height:1.36;color:#4a5570;}
.aag .side{width:1.32in;flex:none;text-align:right;}
.aag .side .cat{font-family:'Liberation Sans',Helvetica,Arial,sans-serif;font-size:5.8pt;letter-spacing:0.14em;color:#1c2b4d;font-weight:bold;line-height:1.5;}
.aag .side .aud{display:inline-block;margin-top:4pt;font-family:'Liberation Sans',Helvetica,Arial,sans-serif;font-size:6pt;letter-spacing:0.1em;color:#8a7a33;border:0.75pt solid #d8d0ba;border-radius:999px;padding:1.6pt 7pt;}

/* ---- expanded campaign page ---- */
.ghost{position:absolute;top:0.28in;right:0;font-family:'Playfair Display',serif;font-weight:800;font-size:78pt;color:#edebe2;line-height:1;z-index:0;}
.kick{font-family:'Liberation Sans',Helvetica,Arial,sans-serif;font-size:6.4pt;letter-spacing:0.24em;color:#1c2b4d;font-weight:bold;margin-bottom:3pt;position:relative;}
.ct{font-family:'Playfair Display',serif;font-weight:800;font-size:31pt;color:#1c2b4d;line-height:1.04;position:relative;margin-bottom:2pt;}
.ctag{font-family:'Cormorant Garamond',serif;font-style:italic;font-size:12pt;color:#8a7a33;position:relative;margin-bottom:6pt;}
.tick{width:0.32in;border-top:2.4pt solid #1c2b4d;margin-bottom:7pt;}
.cintro{font-size:9.8pt;line-height:1.44;color:#33405c;margin-bottom:9pt;position:relative;max-width:6.55in;}
.bigidea{background:#f7f1e2;border-left:2.6pt solid #1c2b4d;padding:8pt 12pt 9pt;margin-bottom:11pt;position:relative;}
.bigidea .lbl{margin-bottom:3pt;}
.bigidea p{font-family:'Cormorant Garamond',serif;font-size:13pt;line-height:1.3;color:#1c2b4d;font-weight:500;}
.two{display:flex;gap:0.32in;margin-bottom:10pt;}
.two .c{flex:1;}
.two p{font-size:9.2pt;line-height:1.42;color:#4a5570;}
.arc-h{display:flex;justify-content:space-between;align-items:baseline;border-top:1.4pt solid #1c2b4d;padding-top:5pt;margin-bottom:6pt;}
.arc-h .r{font-family:'Liberation Sans',Helvetica,Arial,sans-serif;font-size:6pt;letter-spacing:0.16em;color:#1c2b4d;font-weight:bold;}
.arc{display:flex;flex-wrap:wrap;margin-bottom:9pt;}
.arc .s{width:50%;display:flex;padding:0 0.2in 6.5pt 0;}
.arc .no{font-family:'Playfair Display',serif;font-weight:700;font-size:10.5pt;color:#b08a2e;width:0.22in;flex:none;padding-top:0.5pt;}
.arc .st{font-family:'Playfair Display',serif;font-weight:700;font-size:10.6pt;color:#1c2b4d;line-height:1.15;}
.arc .ss{font-family:'Cormorant Garamond',serif;font-size:8.9pt;color:#8b8574;line-height:1.25;margin-top:0.5pt;}
.comp-h{border-top:1.4pt solid #1c2b4d;padding-top:5pt;margin-bottom:5pt;}
.pills{margin-bottom:8pt;}
.pill{display:inline-block;font-family:'Liberation Sans',Helvetica,Arial,sans-serif;font-size:6.6pt;color:#33405c;border:0.75pt solid #b9b3a2;border-radius:999px;padding:2.4pt 9pt;margin:0 3.5pt 3.5pt 0;}
.line{font-size:9.3pt;color:#33405c;margin-bottom:8pt;}
.ip{display:flex;gap:0.32in;margin-bottom:8pt;}
.ip .c{flex:1;}
.ip p{font-size:9.2pt;line-height:1.38;color:#4a5570;}
.spec{display:flex;border:0.75pt solid #d9d3c4;margin-bottom:9pt;}
.spec .c{flex:1;padding:5.5pt 9pt;border-left:0.75pt solid #d9d3c4;}
.spec .c:first-child{border-left:none;}
.spec .v{font-family:'Cormorant Garamond',serif;font-size:11pt;color:#1c2b4d;font-weight:600;line-height:1.15;}
.scrip{background:#16223e;padding:6.5pt 12pt;margin-bottom:8pt;display:flex;align-items:baseline;}
.scrip .k{font-family:'Liberation Sans',Helvetica,Arial,sans-serif;font-size:6.4pt;letter-spacing:0.18em;color:#d4a72e;font-weight:bold;margin-right:12pt;white-space:nowrap;}
.scrip .v{font-family:'Cormorant Garamond',serif;font-size:10.6pt;color:#f4efe2;font-weight:500;}
.foot2{display:flex;gap:0.32in;border-top:0.75pt solid #d9d3c4;padding-top:6pt;}
.foot2 .c{flex:1;}
.foot2 p{font-size:8.9pt;line-height:1.36;color:#4a5570;}

/* ---- complete library ---- */
.lib-h{font-family:'Playfair Display',serif;font-weight:800;font-size:21pt;color:#1c2b4d;margin-bottom:5pt;}
.lib-intro{font-size:10.4pt;line-height:1.45;color:#4a5570;max-width:6.2in;margin-bottom:8pt;}
.legend{display:flex;justify-content:space-between;align-items:baseline;border-top:1.4pt solid #1c2b4d;border-bottom:0.75pt solid #d9d3c4;padding:5pt 0;margin-bottom:10pt;}
.legend .l{font-family:'Liberation Sans',Helvetica,Arial,sans-serif;font-size:6pt;letter-spacing:0.12em;color:#8b8574;}
.legend .l b{color:#b08a2e;}
.legend .r{font-family:'Liberation Sans',Helvetica,Arial,sans-serif;font-size:6pt;letter-spacing:0.16em;color:#1c2b4d;font-weight:bold;}
.lib-cols{display:flex;gap:0.4in;}
.lib-cols .col{flex:1;}
.theme{margin-bottom:12pt;}
.theme .th{font-family:'Liberation Sans',Helvetica,Arial,sans-serif;font-size:7pt;letter-spacing:0.16em;color:#1c2b4d;font-weight:bold;border-bottom:0.75pt solid #1c2b4d;padding-bottom:3pt;margin-bottom:4.5pt;}
.trow{display:flex;justify-content:space-between;align-items:baseline;border-bottom:0.5pt solid #eeeae0;padding:2.3pt 0;}
.trow .t{font-family:'Cormorant Garamond',serif;font-size:9.8pt;color:#33405c;font-weight:500;}
.trow .t .star{color:#b08a2e;font-size:8pt;}
.trow .b{font-family:'Liberation Sans',Helvetica,Arial,sans-serif;font-size:5.6pt;letter-spacing:0.06em;color:#8a7a33;border:0.6pt solid #d8d0ba;border-radius:2pt;padding:1pt 4pt;flex:none;margin-left:8pt;}
""" % {"faces": "\n".join(FACES)}

# ---------------------------------------------------------------- HTML builders
def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

def strip(right):
    return ('<div class="strip"><div class="l">LIFETOGETHER&nbsp;&nbsp;<span>\u00b7&nbsp;&nbsp;'
            'O B E D I E N C E &nbsp; C A M P A I G N &nbsp; L I B R A R Y</span></div>'
            '<div class="r">%s</div></div>' % right)

def cover():
    who = "".join(
        '<div class="who"><div class="t">%s</div><p>%s</p></div>' % (t, esc(p)) for t, p in [
        ("Churches","A complete discipleship pathway on hearing and obeying God \u2014 pastoral, practical, and deeply formational."),
        ("Small Groups & Classes","Ready-made content for groups learning together to listen for and follow God\u2019s leading."),
        ("Pastors & Leaders","A framework for forming a congregation that can be led by the Spirit, not just informed."),
        ("Individuals & Families","A guided path to a more personal, responsive walk with God at home."),
    ])
    outcomes = "".join("<li>%s</li>" % o for o in [
        "Greater confidence in hearing God\u2019s voice",
        "Growing discernment between God\u2019s voice and the noise",
        "A shift from hesitating to obeying promptly",
        "A responsive, surrendered, yielded heart",
        "A congregation that can be led by the Spirit",
        "Deeper intimacy and trust in everyday life"])
    ucs = "".join('<div class="uc"><b>%s</b> &nbsp;%s</div>' % (a, b) for a, b in [
        ("Churchwide Formation Series","A whole-church journey into hearing and obeying God."),
        ("40-Day Spiritual Campaign","Weekend messages, small groups, and daily listening practices."),
        ("21-Day Listening Challenge","A short, focused experience learning to hear God\u2019s voice."),
        ("4-Week Sermon Companion","A focused message series with sermon-aligned small-group guides."),
        ("Small-Group & Class Curriculum","Ready-made content for groups and classes.")])
    stats = "".join('<div class="s"><div class="n">%s</div><div class="k">%s</div></div>' % (n, k) for n, k in [
        ("100","C A M P A I G N S"),("10","E X P A N D E D"),("10","T H E M E S"),
        ("4","F O R M A T S"),("NIV","S C R I P T U R E")])
    return ('<div class="page cover">'
        + strip("C A T E G O R Y &nbsp; C A T A L O G &nbsp; &amp; &nbsp; S T R A T E G Y &nbsp; O V E R V I E W")
        + '<div class="cv-title">Obedience</div>'
        + '<div class="cv-sub">C A M P A I G N &nbsp; C A T A L O G</div>'
        + '<div class="cv-lead">A complete library of 100 ready-to-run campaigns that help your church learn to hear God\u2019s voice, discern His leading, and respond with a wholehearted yes \u2014 turning hearing into a lifetime of joyful obedience.</div>'
        + '<div class="cv-rule"></div>'
        + '<div class="cv-cols"><div class="a">'
        + '<div class="cv-blk"><div class="lbl">WHY THIS CATEGORY MATTERS</div><p>Hearing and obeying God is the heartbeat of discipleship \u2014 and the place most believers feel the most uncertain. They long to hear from God and quietly wonder why He seems silent, or they hear clearly and struggle to obey. Few topics are more central to spiritual maturity, yet few are taught with practical, grace-filled clarity. A church that disciples its people to hear and follow God grows disciples who can actually be led.</p></div>'
        + '<div class="cv-blk"><div class="lbl">THE CORE PROBLEM</div><p>Most believers want to follow God but feel stuck between two gaps: a hearing gap \u2014 they aren\u2019t sure how to discern His voice \u2014 and a doing gap \u2014 they hear and hesitate. The result is a faith that admires obedience more than it practices it. Leaders sense the need but lack a ready, biblically grounded pathway to teach listening and obedience across the whole of life.</p></div>'
        + '<div class="cv-blk"><div class="lbl">THE TRANSFORMATION</div><p>These campaigns move people from straining to hear toward a confident, responsive life of hearing and following God \u2014 noticing His voice, discerning His leading, obeying the nudge, and answering with a wholehearted yes.</p></div>'
        + '</div><div class="b"><div class="lbl">WHO NEEDS THIS</div>' + who + '</div></div>'
        + '<div class="cv-band"><div class="col"><div class="lbl">KEY OUTCOMES</div><ul class="ol">' + outcomes + '</ul></div>'
        + '<div class="col"><div class="lbl">SAMPLE USE CASES</div>' + ucs + '</div></div>'
        + '<div class="stats">' + stats + '</div>'
        + '</div>')

def at_a_glance():
    rows = []
    for c in C:
        rows.append('<div class="aag"><div class="n">%s</div><div class="m">'
            '<span class="t">%s</span><div class="tag">%s</div><div class="d">%s</div></div>'
            '<div class="side"><div class="cat">%s</div><br><span class="aud">Church</span></div></div>'
            % (c["num"], esc(c["title"]), esc(c["tagline"]), esc(c["aag_desc"]), c["aag_label"].replace("&", "&amp;")))
    return ('<div class="page">'
        + strip("T O P &nbsp; 1 0 &nbsp; \u00b7 &nbsp; A T &nbsp; A &nbsp; G L A N C E")
        + '<div class="aag-h">The Top 10 Campaigns</div>'
        + '<div class="aag-intro">The ten strongest, most-requested campaigns in the Obedience category \u2014 each expanded on the pages that follow. The full 100-campaign library appears at the back of this catalog.</div>'
        + "".join(rows) + '</div>')

def campaign_page(c):
    arc = "".join('<div class="s"><div class="no">%d</div><div><div class="st">%s</div>'
                  '<div class="ss">%s</div></div></div>' % (i + 1, esc(t), esc(s))
                  for i, (t, s) in enumerate(c["arc"]))
    pills = "".join('<span class="pill">%s</span>' % p for p in
        ["Daily Readings & Reflections","Six Group-Session Guides","Weekend Message Outlines",
         "Spiritual-Partner Prompts","Launch & Promotion Kit"])
    return ('<div class="page">'
        + strip("E X P A N D E D &nbsp; C A M P A I G N &nbsp; %s &nbsp; O F &nbsp; 1 0" % c["num"])
        + '<div class="ghost">%s</div>' % c["num"]
        + '<div class="kick">OBEDIENCE &nbsp;\u00b7&nbsp; CAMPAIGN %s &nbsp;\u00b7&nbsp; TIER 2</div>' % c["num"]
        + '<div class="ct">%s</div>' % esc(c["title"])
        + '<div class="ctag">%s</div>' % esc(c["tagline"])
        + '<div class="tick"></div>'
        + '<div class="cintro">%s</div>' % esc(c["intro"])
        + '<div class="bigidea"><div class="lbl">THE BIG IDEA</div><p>%s</p></div>' % esc(c["big_idea"])
        + '<div class="two"><div class="c"><div class="lbl">THE CORE PROBLEM</div><p>%s</p></div>' % esc(c["problem"])
        + '<div class="c"><div class="lbl">THE TRANSFORMATION PROMISE</div><p>%s</p></div></div>' % esc(c["promise"])
        + '<div class="arc-h"><div class="lbl" style="margin-bottom:0">THE 6-SESSION ARC</div><div class="r">EXPANDABLE &amp; FLEXIBLE</div></div>'
        + '<div class="arc">' + arc + '</div>'
        + '<div class="comp-h"><div class="lbl" style="margin-bottom:0">CAMPAIGN COMPONENTS</div></div>'
        + '<div class="pills">' + pills + '</div>'
        + '<div class="lbl">KEY OUTCOMES</div><div class="line">%s</div>' % c["outcomes"]
        + '<div class="ip"><div class="c"><div class="lbl">IDEAL FOR</div><p>%s</p></div>' % esc(c["ideal"])
        + '<div class="c"><div class="lbl">PAIRS WELL WITH</div><p>%s</p></div></div>' % c["pairs"]
        + '<div class="spec">'
        + '<div class="c"><div class="lbl mut">PRIMARY FORMAT</div><div class="v">40-Day Campaign</div></div>'
        + '<div class="c"><div class="lbl mut">SESSIONS</div><div class="v">6 Sessions</div></div>'
        + '<div class="c"><div class="lbl mut">FELT NEED</div><div class="v">%s</div></div>' % c["felt"].replace("&", "&amp;")
        + '<div class="c"><div class="lbl mut">AUDIENCE</div><div class="v">Church</div></div>'
        + '</div>'
        + '<div class="scrip"><div class="k">KEY SCRIPTURES</div><div class="v">%s</div></div>' % c["scriptures"]
        + '<div class="foot2"><div class="c"><div class="lbl">INTENDED AUDIENCE</div><p>%s</p></div>' % esc(c["audience"])
        + '<div class="c"><div class="lbl">FORMAT FLEXIBILITY</div><p>%s</p></div></div>' % c["flex"]
        + '</div>')

def theme_block(name, titles):
    rows = []
    for t in titles:
        if t.endswith(" \u2605"):
            t_html = esc(t[:-2]) + ' <span class="star">\u2605</span>'
        else:
            t_html = esc(t)
        rows.append('<div class="trow"><div class="t">%s</div><div class="b">T2</div></div>' % t_html)
    return '<div class="theme"><div class="th">%s</div>%s</div>' % (name.replace("&", "&amp;"), "".join(rows))

def library_page(part, themes):
    left = "".join(theme_block(n, t) for n, t in themes[:3])
    right = "".join(theme_block(n, t) for n, t in themes[3:])
    return ('<div class="page">'
        + strip("C O M P L E T E &nbsp; C A T E G O R Y &nbsp; L I B R A R Y")
        + '<div class="lib-h">The Complete Obedience Library (Part %s of 2)</div>' % part
        + '<div class="lib-intro">All 100 campaign opportunities in the Obedience category, organized by theme. The ten starred titles are expanded earlier in this catalog; every title is available for full development.</div>'
        + '<div class="legend"><div class="l"><b>\u2605</b>&nbsp; EXPANDED IN THIS CATALOG &nbsp;&nbsp;&nbsp; T1 &nbsp;TIER 1 &nbsp;&nbsp;&nbsp; T2 &nbsp;TIER 2</div>'
        + '<div class="r">1 0 0 &nbsp; C A M P A I G N S &nbsp; \u00b7 &nbsp; 1 0 &nbsp; T H E M E S</div></div>'
        + '<div class="lib-cols"><div class="col">' + left + '</div><div class="col">' + right + '</div></div>'
        + '</div>')

html = ('<!DOCTYPE html><html><head><meta charset="utf-8">'
        '<title>LifeTogether \u00b7 Obedience Campaign Library \u00b7 v2</title>'
        '<style>' + CSS + '</style></head><body>'
        + cover() + at_a_glance()
        + "".join(campaign_page(c) for c in C)
        + library_page("1", THEMES_P1) + library_page("2", THEMES_P2)
        + '</body></html>')

with open("Obedience_Campaign_Library_v2.html", "w", encoding="utf-8") as f:
    f.write(html)

from weasyprint import HTML
HTML(string=html, base_url=".").write_pdf("Obedience_Campaign_Library_v2.pdf")
import subprocess
print(subprocess.run(["qpdf", "--show-npages", "Obedience_Campaign_Library_v2.pdf"],
                     capture_output=True, text=True).stdout)
print("done")
