# -*- coding: utf-8 -*-
import pathlib
from brochure_template import FONTS, CSS, campaign_page

campaigns = [
{
 "num":"01","accent":"#45617f","accent_soft":"#dde3ec",
 "title_a":"","title_b":"Whispers",
 "subtitle":"Learning to notice the quiet voice of God",
 "problem":"Many of us are waiting for God to shout \u2014 a sign in the sky, a door flung open, an unmistakable word. And while we wait for the dramatic, we miss the way He most often speaks: softly. The problem usually isn\u2019t that God has gone silent. It\u2019s that His voice is quieter than the noise we\u2019ve surrounded ourselves with.",
 "promise":"Whispers teaches your people to listen for the gentle voice. Over forty days they\u2019ll learn to quiet the noise, slow down, and notice the soft promptings of God they\u2019ve been missing \u2014 discovering that the same God who spoke to Elijah in a whisper is still speaking, gently, to them.",
 "verse":"\u2026and after the fire came a gentle whisper.",
 "ref":"1 Kings 19:12 (NIV)",
 "bigidea":"God rarely competes with the noise. He whispers \u2014 and the whisper is only missed by those too busy or too loud to lean in and listen.",
 "tags":["Stillness","The Still Voice","Attentiveness","Quiet","Presence"],
 "best_for":"Church","backbone":"1 Kings 19:11\u201313","metaphor":"The Gentle Whisper","felt":"Hearing God in the quiet",
 "sessions":[
   ("1","Waiting for Thunder","Why we keep missing the voice we\u2019re straining to hear."),
   ("2","Not in the Wind","What Elijah learned about how God actually speaks."),
   ("3","Quieting the Noise","Turning down the volume so the whisper can be heard."),
   ("4","The Gentle Voice","Recognizing the soft promptings we usually overlook."),
   ("5","Leaning In","Cultivating the stillness where God speaks."),
   ("6","A Listening Life","Living attentive to the whisper, every ordinary day."),
 ],
 "journey":"Each of the 40 days carves out one small pocket of stillness, one prompt to listen, and one written prayer \u2014 a daily practice of turning down the noise until the whisper becomes clear.",
 "why":"The issue was never God\u2019s silence. Teach your people to quiet the noise, and they\u2019ll be amazed how much He\u2019s been saying.",
 "cta":"Launch Whispers and help your church hear the voice they\u2019ve been missing.",
 "note":None,
},
{
 "num":"02","accent":"#2f6b4f","accent_soft":"#d8e8df",
 "title_a":"Living","title_b":"Obedience",
 "subtitle":"Turning what you hear from God into how you live",
 "problem":"It\u2019s possible to hear God clearly and still not obey Him. We nod along on Sunday, underline the verse, feel the conviction \u2014 and then live Monday exactly as we would have anyway. The gap in most of our spiritual lives isn\u2019t a hearing problem. It\u2019s a doing problem.",
 "promise":"Living Obedience closes the gap between hearing and doing. Over forty days your people move from admiring God\u2019s Word to actually obeying it \u2014 building the daily habit of saying yes \u2014 until obedience stops being an occasional decision and becomes a settled way of life.",
 "verse":"Do not merely listen to the word, and so deceive yourselves. Do what it says.",
 "ref":"James 1:22 (NIV)",
 "bigidea":"Hearing without doing isn\u2019t neutral \u2014 it\u2019s self-deception. Obedience is where faith stops being an idea and becomes a life.",
 "tags":["Obedience","Doing","Discipleship","Surrender","Faithfulness"],
 "best_for":"Church","backbone":"James 1:22\u201325; Luke 6:46","metaphor":"Doers, Not Just Hearers","felt":"Obedience as a way of life",
 "sessions":[
   ("1","The Hearing-Doing Gap","Why knowing God\u2019s will isn\u2019t the same as following it."),
   ("2","Doers, Not Hearers","The self-deception of admiring a word we never obey."),
   ("3","The First Yes","Why obedience starts before you understand the whole plan."),
   ("4","Obedience in the Small","Building the everyday habit of saying yes to God."),
   ("5","When Obedience Costs","Following God even when it\u2019s hard or unclear."),
   ("6","A Yielded Life","Living so that obedience becomes second nature."),
 ],
 "journey":"Each of the 40 days takes one thing God has already said and turns it into one concrete act of obedience, with a partner check-in and a prayer \u2014 closing the gap between hearing and doing, day by day.",
 "why":"The most spiritually stuck people aren\u2019t the ones who can\u2019t hear God. They\u2019re the ones who hear and never move.",
 "cta":"Launch Living Obedience and help your church become doers of the Word.",
 "note":None,
},
{
 "num":"03","accent":"#2d6a7a","accent_soft":"#d6e7ec",
 "title_a":"Hearing and","title_b":"Responding",
 "subtitle":"The back-and-forth rhythm of walking with God",
 "problem":"We often treat hearing from God as a one-way event \u2014 we ask, He answers, and the conversation ends. But Scripture pictures something more like a relationship: a living rhythm of God speaking and His people responding, again and again. And many of us have never learned how to actually answer when He speaks.",
 "promise":"Hearing and Responding builds the rhythm. Over forty days your people learn the responsive posture of young Samuel \u2014 \u201cSpeak, for your servant is listening\u201d \u2014 moving from passive hearing to an active, willing yes, until walking with God becomes a real and ongoing conversation.",
 "verse":"Speak, for your servant is listening.",
 "ref":"1 Samuel 3:10 (NIV)",
 "bigidea":"Hearing God isn\u2019t a transaction; it\u2019s a conversation. And every conversation needs a response \u2014 a willing \u201cyes, Lord\u201d that keeps the relationship moving.",
 "tags":["Responsiveness","Relationship","Yes","Servant Heart","Discernment"],
 "best_for":"Church","backbone":"1 Samuel 3:1\u201310; John 10:4","metaphor":"Speak, Your Servant Is Listening","felt":"Responsive relationship, saying yes",
 "sessions":[
   ("1","More Than a Hotline","Why hearing God is a relationship, not a request line."),
   ("2","Speak, I\u2019m Listening","Learning Samuel\u2019s posture of ready attentiveness."),
   ("3","The Willing Yes","Responding to God before you know all the details."),
   ("4","When the Answer Is Hard","Saying yes even when His word stretches you."),
   ("5","Staying in the Conversation","Keeping the dialogue going through every season."),
   ("6","A Responsive Heart","Living always ready to hear and to answer."),
 ],
 "journey":"Each of the 40 days pairs a moment of listening with a small, concrete response \u2014 a yes you actually act on \u2014 plus a partner check-in and a prayer, building a real rhythm of conversation with God.",
 "why":"God is far more interested in a relationship than a broadcast. When your people learn to respond, hearing Him becomes a daily, two-way joy.",
 "cta":"Launch Hearing and Responding and help your church learn to answer when God speaks.",
 "note":None,
},
{
 "num":"04","accent":"#b0852b","accent_soft":"#f0e6cc",
 "title_a":"Prompted","title_b":"by God",
 "subtitle":"Recognizing and obeying the Spirit\u2019s nudges in the moment",
 "problem":"Most of us have felt it \u2014 a sudden nudge to call someone, to give, to speak up, to go out of our way. And most of us have learned to second-guess it, explain it away, or simply ignore it. We\u2019re surrounded by quiet promptings from the Spirit, and we\u2019ve grown skilled at talking ourselves out of them.",
 "promise":"Prompted by God trains your people to notice and obey the nudge. Over forty days they\u2019ll learn to recognize the Spirit\u2019s real-time leading \u2014 the way Philip was sent to a single chariot on a desert road \u2014 and to act on it quickly, before the moment and the courage pass.",
 "verse":"The Spirit told Philip, \u201cGo to that chariot and stay near it.\u201d",
 "ref":"Acts 8:29 (NIV)",
 "bigidea":"The Spirit still nudges. The question isn\u2019t whether God is prompting His people \u2014 it\u2019s whether we\u2019ll act on the prompt before we explain it away.",
 "tags":["Promptings","The Spirit","Discernment","Obey Quickly","Boldness"],
 "best_for":"Church","backbone":"Acts 8:26\u201340; Romans 8:14","metaphor":"The Spirit\u2019s Nudge","felt":"Spirit-led promptings, real-time obedience",
 "sessions":[
   ("1","The Nudge You Ignored","Naming the promptings we\u2019ve learned to talk ourselves out of."),
   ("2","Led to the Chariot","How the Spirit guided Philip into a divine appointment."),
   ("3","Was That God or Me?","Growing in discernment of the Spirit\u2019s leading."),
   ("4","Obey Quickly","Why promptings have a short shelf life."),
   ("5","Small Prompts, Big Stories","How ordinary nudges become extraordinary moments."),
   ("6","Led by the Spirit","Living attentive and ready to be sent."),
 ],
 "journey":"Each of the 40 days invites your people to notice one prompting and act on it the same day, with a partner check-in and a prayer \u2014 a daily practice of obeying the nudge instead of explaining it away.",
 "why":"Behind almost every story of God using someone is a moment they obeyed a nudge most people would have ignored.",
 "cta":"Launch Prompted by God and help your church act on the Spirit\u2019s leading.",
 "note":None,
},
{
 "num":"05","accent":"#514a86","accent_soft":"#e1ddef",
 "title_a":"Listening for","title_b":"His Voice",
 "subtitle":"The practice of discerning God\u2019s voice among the many",
 "problem":"We live in the noisiest era in human history, surrounded by a thousand competing voices \u2014 culture, fear, the crowd, our own desires \u2014 all claiming to know what\u2019s best. In that din, the real challenge isn\u2019t only hearing God; it\u2019s telling His voice apart from all the others clamoring for our obedience.",
 "promise":"Listening for His Voice builds the discipline of discernment. Over forty days your people learn the practice of listening \u2014 making space, testing what they hear, and growing familiar enough with the Shepherd\u2019s voice that they can recognize it, and follow it, above all the rest.",
 "verse":"My sheep listen to my voice; I know them, and they follow me.",
 "ref":"John 10:27 (NIV)",
 "bigidea":"Sheep don\u2019t follow a stranger \u2014 they know their Shepherd\u2019s voice. Discernment isn\u2019t a gift for a few; it\u2019s a familiarity anyone can grow.",
 "tags":["Discernment","Listening","The Shepherd","Practice","Wisdom"],
 "best_for":"Church","backbone":"John 10:1\u201327; 1 John 4:1","metaphor":"The Shepherd\u2019s Voice","felt":"The practice of listening, discernment",
 "sessions":[
   ("1","A Thousand Voices","Naming the many voices competing for your obedience."),
   ("2","The Shepherd\u2019s Voice","How sheep learn to know the One they follow."),
   ("3","Making Space to Listen","Building the practice of unhurried attention."),
   ("4","Testing What You Hear","Discerning God\u2019s voice from the counterfeits."),
   ("5","Familiar with His Voice","Growing the kind of intimacy that recognizes Him instantly."),
   ("6","Following the Voice","Letting what you hear shape where you go."),
 ],
 "journey":"Each of the 40 days sets aside time to listen, offers a way to test what you hear, and ends in a written prayer \u2014 a daily discipline that, over six weeks, tunes your ear to the Shepherd\u2019s voice.",
 "why":"In a world this loud, the ability to recognize God\u2019s voice may be the most important skill a believer can grow.",
 "cta":"Launch Listening for His Voice and help your church learn to know His voice.",
 "note":None,
},
]

for _c in campaigns:
    _c["category"] = "Obedience"
    _c["tier"] = "Tier 2"
    _c["audience"] = "Church"

cover = """
<div class="page cover">
  <div class="frame gold"></div>
  <div class="cover-inner">
    <div class="brandmark">Lifetogether</div>
    <div class="kicker">The Campaign Library &nbsp;&middot;&nbsp; Obedience Collection</div>
    <div class="cover-rule"></div>
    <h1>The <em>Obedience</em><br>Collection</h1>
    <div class="sub">Five forty-day campaigns to help your church learn to hear God\u2019s voice, discern His leading, and respond with a wholehearted yes.</div>
    <div class="cover-foot">
      <div class="stats">
        <div class="stat"><div class="n">5</div><div class="l">Campaigns</div></div>
        <div class="stat"><div class="n">40</div><div class="l">Day Journey</div></div>
        <div class="stat"><div class="n">6</div><div class="l">Sessions Each</div></div>
        <div class="stat"><div class="n">NIV</div><div class="l">Scripture</div></div>
      </div>
      <div class="tier">Tier 2 &nbsp;&middot;&nbsp; Church Edition &nbsp;&middot;&nbsp; Hearing &amp; Obeying God</div>
    </div>
  </div>
</div>"""

intro = """
<div class="page intro">
  <div class="frame"></div>
  <div class="intro-inner">
    <div class="kicker">Before You Begin</div>
    <h2>The problem was never<br>that God went <em>quiet</em>.</h2>
    <p class="lead">Most believers long to hear from God \u2014 and quietly wonder why He so often seems silent. But Scripture insists He is still speaking; the harder work is on our end: learning to be still, to listen, to discern His voice among the many, and to actually obey what we hear. <strong>The Obedience Collection is built for exactly that.</strong> Five distinct, forty-day journeys move your church from straining to hear toward a confident, responsive life of hearing and following God.</p>
    <div class="howrow">
      <div class="howcard"><div class="hn">40</div><h4>A Daily Rhythm</h4><p>Every day offers a short reading, a moment to listen, a spiritual-partner check-in, and a written prayer &mdash; small, repeatable, and easy to keep.</p></div>
      <div class="howcard"><div class="hn">6</div><h4>A Weekly Gathering</h4><p>Six group sessions give the journey its backbone, turning private listening into shared momentum across your church.</p></div>
      <div class="howcard"><div class="hn">1</div><h4>A Clear Outcome</h4><p>Each campaign is built around one transformation &mdash; so your people don\u2019t just hope to hear God, they learn to recognize and follow His voice.</p></div>
    </div>
    <div class="contents">
      <div class="ct">Inside This Collection</div>
      <div class="clist">
        <div class="cli"><span class="cnum">01</span><span><span class="cnm">Whispers</span><br><span class="cds">Notice the quiet voice of God</span></span></div>
        <div class="cli"><span class="cnum">02</span><span><span class="cnm">Living Obedience</span><br><span class="cds">Turn what you hear into how you live</span></span></div>
        <div class="cli"><span class="cnum">03</span><span><span class="cnm">Hearing and Responding</span><br><span class="cds">Learn the rhythm of hearing and yes</span></span></div>
        <div class="cli"><span class="cnum">04</span><span><span class="cnm">Prompted by God</span><br><span class="cds">Obey the Spirit\u2019s nudges in the moment</span></span></div>
        <div class="cli"><span class="cnum">05</span><span><span class="cnm">Listening for His Voice</span><br><span class="cds">Discern His voice among the many</span></span></div>
      </div>
    </div>
  </div>
</div>"""

closing = """
<div class="page close">
  <div class="frame"></div>
  <div class="close-inner">
    <div class="kicker">Ready When You Are</div>
    <h2>Help your church hear<br>and <em>follow</em> God.</h2>
    <p class="cp">From the gentle whisper to a wholehearted yes, these five campaigns walk your church into a confident, listening, obedient life with God. Choose where your people are ready to grow \u2014 noticing His voice, responding to it, obeying the nudge, or discerning it among the many \u2014 or journey through all five across a season.</p>
    <div class="close-list">
      <div class="cl-row"><span class="cln">01</span><span class="clt">Whispers</span><span class="cld">The gentle voice</span></div>
      <div class="cl-row"><span class="cln">02</span><span class="clt">Living Obedience</span><span class="cld">Doers of the Word</span></div>
      <div class="cl-row"><span class="cln">03</span><span class="clt">Hearing and Responding</span><span class="cld">A willing yes</span></div>
      <div class="cl-row"><span class="cln">04</span><span class="clt">Prompted by God</span><span class="cld">Obey the nudge</span></div>
      <div class="cl-row"><span class="cln">05</span><span class="clt">Listening for His Voice</span><span class="cld">Know the Shepherd</span></div>
    </div>
    <div class="close-cta"><span class="btn">Start Your Campaign</span></div>
    <div class="close-foot">
      <div class="niv">All Scripture taken from the New International Version (NIV)</div>
      <div class="brandmark">Lifetogether</div>
    </div>
  </div>
</div>"""

pages = cover + intro + "".join(campaign_page(c) for c in campaigns) + closing
doc = f"""<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8">
<title>The Obedience Collection \u2014 Lifetogether</title>
<style>{FONTS}</style>
<style>{CSS}</style>
</head><body>{pages}</body></html>"""

pathlib.Path("/tmp/obedience.html").write_text(doc, encoding="utf-8")
print("HTML written:", len(doc), "chars")
