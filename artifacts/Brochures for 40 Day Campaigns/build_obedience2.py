# -*- coding: utf-8 -*-
import pathlib
from brochure_template import FONTS, CSS, campaign_page

campaigns = [
{
 "num":"06","accent":"#9e3b2f","accent_soft":"#f1dcd5",
 "title_a":"Radical","title_b":"Obedience",
 "subtitle":"The costly, all-in obedience that changes everything",
 "problem":"Most of us are comfortable with convenient obedience \u2014 the kind that fits our schedule, protects our security, and never asks too much. But the obedience Scripture celebrates is rarely convenient. It\u2019s fishermen dropping their nets mid-catch, a father climbing a mountain, a young girl risking everything on a yes. Real obedience eventually costs something.",
 "promise":"Radical Obedience calls your church past comfortable. Over forty days your people will confront the places they\u2019ve been negotiating with God \u2014 obeying up to a point \u2014 and find the courage for the wholehearted, leave-the-nets obedience that has always been where the real adventure with God begins.",
 "verse":"At once they left their nets and followed him.",
 "ref":"Matthew 4:20 (NIV)",
 "bigidea":"God rarely asks for a little. He asks for everything \u2014 and the radical, costly yes is the doorway to the very life with Him we long for.",
 "tags":["Wholehearted","Costly","Surrender","Courage","All In"],
 "best_for":"Church","backbone":"Matthew 4:18\u201322; Genesis 22","metaphor":"Leave the Nets","felt":"Costly obedience, all-in",
 "sessions":[
   ("1","Convenient Obedience","Naming the limits we quietly place on our yes."),
   ("2","Leave the Nets","The immediate, costly obedience of the first disciples."),
   ("3","The Negotiated Surrender","Where we obey God up to a point and no further."),
   ("4","When Obedience Costs","Following when the price is real."),
   ("5","The Adventure Begins","Why the radical yes is where life with God opens up."),
   ("6","All In","Living with nothing held back."),
 ],
 "journey":"Each of the 40 days surfaces one area we\u2019ve been holding back and invites one bold, costly step of obedience, with a partner check-in and a prayer.",
 "why":"A half-hearted yes has never changed a life or a world. The radical obedience we fear is the very thing we were made for.",
 "cta":"Launch Radical Obedience and help your church leave the nets.",
 "note":None,
},
{
 "num":"07","accent":"#2d6a7a","accent_soft":"#d6e7ec",
 "title_a":"Spirit-Led","title_b":"Decisions",
 "subtitle":"Bringing every choice under the guidance of God",
 "problem":"Life is a relentless series of decisions \u2014 jobs, moves, relationships, money, a hundred small forks each week \u2014 and most of us make them the way the world does: pros and cons, gut feel, and hope for the best. We believe God guides, but we rarely know how to actually invite His leading into the choices that shape our lives.",
 "promise":"Spirit-Led Decisions gives your church a better way to decide. Over forty days your people learn to bring their choices \u2014 big and small \u2014 under the guidance of the Spirit, trusting the God who promises that those who submit their ways to Him will find their paths made straight.",
 "verse":"\u2026in all your ways submit to him, and he will make your paths straight.",
 "ref":"Proverbs 3:6 (NIV)",
 "bigidea":"God cares about your decisions more than you do \u2014 and He\u2019s promised to guide the steps of anyone humble enough to ask. Guidance is available; we simply have to seek it.",
 "tags":["Guidance","Decisions","Discernment","Wisdom","Direction"],
 "best_for":"Church","backbone":"Proverbs 3:5\u20136; Romans 12:2","metaphor":"Straight Paths","felt":"Decision-making, guidance, discernment",
 "sessions":[
   ("1","The Weight of Choosing","Why decisions drain us, and how God means to help."),
   ("2","Lean Not on Your Own","Trading self-reliance for Spirit-reliance."),
   ("3","Submit Your Ways","What it actually means to invite God into a decision."),
   ("4","Open and Closed Doors","Reading God\u2019s leading without superstition."),
   ("5","Peace as a Compass","How God\u2019s peace helps confirm the way."),
   ("6","Straight Paths","Living as someone consistently led by God."),
 ],
 "journey":"Each of the 40 days brings one real decision \u2014 small or large \u2014 to God in a simple, repeatable way, with a partner check-in and a prayer, building a lifelong habit of Spirit-led choosing.",
 "why":"We become the sum of our decisions. Teach your people to make them with God, and you change the whole direction of their lives.",
 "cta":"Launch Spirit-Led Decisions and help your church choose with God.",
 "note":None,
},
{
 "num":"08","accent":"#45617f","accent_soft":"#dde3ec",
 "title_a":"Following God\u2019s","title_b":"Whisper",
 "subtitle":"Walking in the direction He quietly points, one step at a time",
 "problem":"Sometimes the hardest part of obedience isn\u2019t hearing God \u2014 it\u2019s that what we hear is so small. A nudge toward a hard conversation. A quiet sense to wait, or to go. Rarely a floodlit map; usually just enough light for the next step. And when the whisper points somewhere uncertain, we hesitate, ask for more, and stall.",
 "promise":"Following God\u2019s Whisper builds the faith to walk. Over forty days your people learn to act on God\u2019s quiet guidance one obedient step at a time \u2014 trusting the voice behind them saying \u201cthis is the way\u201d \u2014 even when they can\u2019t yet see where the path leads.",
 "verse":"\u2026you will hear a voice behind you, saying, \u201cThis is the way; walk in it.\u201d",
 "ref":"Isaiah 30:21 (NIV)",
 "bigidea":"God usually gives enough light for the next step, not the whole staircase. Following His whisper means trusting the step you can see to the God who sees the rest.",
 "tags":["Guidance","Faith","Next Step","Trust","Direction"],
 "best_for":"Church","backbone":"Isaiah 30:21; Psalm 119:105","metaphor":"This Is the Way","felt":"Following guidance, one step at a time",
 "sessions":[
   ("1","Just Enough Light","Why God rarely shows the whole path at once."),
   ("2","This Is the Way","Learning to trust the voice that points the direction."),
   ("3","The Hesitation Habit","What keeps us from following the whisper."),
   ("4","One Step at a Time","Obeying the guidance you have, not the map you want."),
   ("5","Following into the Unknown","Walking by faith when the way is unclear."),
   ("6","A Followed Life","Becoming someone who moves at God\u2019s whisper."),
 ],
 "journey":"Each of the 40 days names one quiet bit of guidance and invites one small step of following it, with a partner check-in and a prayer \u2014 building the muscle of walking by faith.",
 "why":"The people God leads farthest are the ones who\u2019ll take the next step on a whisper. He shows the rest of the way to those already walking.",
 "cta":"Launch Following God\u2019s Whisper and help your church walk it out, one step at a time.",
 "note":None,
},
{
 "num":"09","accent":"#514a86","accent_soft":"#e1ddef",
 "title_a":"Daily","title_b":"Surrender",
 "subtitle":"Laying down your will before God, one morning at a time",
 "problem":"We tend to think of surrender as a single, dramatic moment \u2014 an altar call, a tearful decision, a one-time handing over of the keys. But our will doesn\u2019t stay surrendered. By breakfast the next day, we\u2019ve quietly taken back control. The trouble with surrender is that it won\u2019t hold unless it\u2019s renewed, daily.",
 "promise":"Daily Surrender makes yielding a rhythm. Over forty days your people learn to lay down their own agenda each morning \u2014 to pray \u201cnot my will, but Yours\u201d before the day takes over \u2014 and discover the unexpected freedom of a life that\u2019s no longer theirs to carry alone.",
 "verse":"Whoever wants to be my disciple must\u2026 take up their cross daily and follow me.",
 "ref":"Luke 9:23 (NIV)",
 "bigidea":"Surrender isn\u2019t a one-time transaction; it\u2019s a daily renewal. The will you handed God yesterday has a way of climbing back onto the throne by morning.",
 "tags":["Surrender","The Will","Daily","Yielding","Trust"],
 "best_for":"Church","backbone":"Luke 9:23; Luke 22:42","metaphor":"The Daily Cross","felt":"Daily surrender, yielding control",
 "sessions":[
   ("1","The Surrender That Won\u2019t Hold","Why one-time yielding quietly slips away."),
   ("2","Take Up Your Cross Daily","The everyday rhythm Jesus actually described."),
   ("3","Not My Will","Praying Gethsemane\u2019s prayer in your own life."),
   ("4","Reclaiming the Throne","Noticing how quickly we take control back."),
   ("5","The Freedom of Yielding","Why surrender feels like loss and becomes relief."),
   ("6","Surrendered Today","Building the daily habit of laying it down."),
 ],
 "journey":"Each of the 40 days begins with one small, concrete act of surrender \u2014 a worry, a plan, a right \u2014 handed to God before the day starts, with a partner check-in and a prayer.",
 "why":"We don\u2019t drift toward surrender; we drift toward control. A daily yielding is the only kind that lasts.",
 "cta":"Launch Daily Surrender and help your church lay it down, every morning.",
 "note":None,
},
{
 "num":"10","accent":"#b0852b","accent_soft":"#f0e6cc",
 "title_a":"Saying Yes","title_b":"to God",
 "subtitle":"A willing, available yes \u2014 before you even know the question",
 "problem":"Many of us answer God conditionally. We want to know the cost, the plan, and the destination before we commit \u2014 a \u201cyes, if\u201d rather than a \u201cyes, Lord.\u201d But God rarely shows the whole assignment before the yes. He\u2019s looking for people available enough to say yes first, and ask their questions on the way.",
 "promise":"Saying Yes to God cultivates a pre-decided yes. Over forty days your people move from cautious, conditional answers to the open, willing availability of Isaiah \u2014 \u201cHere am I. Send me\u201d \u2014 and discover the adventure that opens up for those who say yes before they know exactly what they\u2019re agreeing to.",
 "verse":"Here am I. Send me!",
 "ref":"Isaiah 6:8 (NIV)",
 "bigidea":"God usually asks for the yes before He gives the details. The most usable people in His hands are simply the ones who\u2019ve already decided their answer is yes.",
 "tags":["Availability","Willingness","The Yes","Trust","Sent"],
 "best_for":"Church","backbone":"Isaiah 6:8; Luke 1:38","metaphor":"Here Am I, Send Me","felt":"Willingness, availability, the yes",
 "sessions":[
   ("1","Yes, If","The quiet conditions we attach to our obedience."),
   ("2","Here Am I","Isaiah\u2019s available, unconditional answer."),
   ("3","Yes Before the Question","Deciding your answer in advance."),
   ("4","Mary\u2019s Yes","The trusting surrender of \u201clet it be to me.\u201d"),
   ("5","The Cost and the Joy","Counting both, and saying yes anyway."),
   ("6","A Sent People","Living available to whatever God asks."),
 ],
 "journey":"Each of the 40 days offers one small invitation to say yes to God \u2014 quickly, before the excuses gather \u2014 with a partner check-in and a prayer, until yes becomes your people\u2019s first instinct.",
 "why":"God\u2019s greatest work tends to flow through ordinary people who had simply already decided to say yes. Availability, not ability, is what He\u2019s after.",
 "cta":"Launch Saying Yes to God and help your church answer before they\u2019re asked.",
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
    <div class="kicker">The Campaign Library &nbsp;&middot;&nbsp; Obedience &nbsp;&middot;&nbsp; Volume Two</div>
    <div class="cover-rule"></div>
    <h1>The <em>Obedience</em><br>Collection</h1>
    <div class="sub">Five more forty-day campaigns that move your church from hearing God to following Him fully \u2014 in radical obedience, Spirit-led decisions, daily surrender, and a wholehearted yes.</div>
    <div class="cover-foot">
      <div class="stats">
        <div class="stat"><div class="n">5</div><div class="l">Campaigns</div></div>
        <div class="stat"><div class="n">40</div><div class="l">Day Journey</div></div>
        <div class="stat"><div class="n">6</div><div class="l">Sessions Each</div></div>
        <div class="stat"><div class="n">NIV</div><div class="l">Scripture</div></div>
      </div>
      <div class="tier">Tier 2 &nbsp;&middot;&nbsp; Church Edition &nbsp;&middot;&nbsp; Titles 06\u201310</div>
    </div>
  </div>
</div>"""

intro = """
<div class="page intro">
  <div class="frame"></div>
  <div class="intro-inner">
    <div class="kicker">Before You Begin</div>
    <h2>Hearing God is only half.<br>The rest is <em>following</em>.</h2>
    <p class="lead">It\u2019s one thing to recognize God\u2019s voice; it\u2019s another to follow where it leads \u2014 especially when the way is costly, the decision is hard, or the yes comes before the details. <strong>This second volume turns hearing into following.</strong> Five distinct, forty-day journeys move your church from listening toward a wholehearted life of obedience: radical, Spirit-led, surrendered, and ready to say yes.</p>
    <div class="howrow">
      <div class="howcard"><div class="hn">40</div><h4>A Daily Rhythm</h4><p>Every day offers a short reading, a step of obedience, a spiritual-partner check-in, and a written prayer &mdash; small, repeatable, and easy to keep.</p></div>
      <div class="howcard"><div class="hn">6</div><h4>A Weekly Gathering</h4><p>Six group sessions give the journey its backbone, turning private obedience into shared momentum across your church.</p></div>
      <div class="howcard"><div class="hn">1</div><h4>A Clear Outcome</h4><p>Each campaign is built around one transformation &mdash; so your people don\u2019t just intend to follow God, they actually take the step.</p></div>
    </div>
    <div class="contents">
      <div class="ct">Inside This Volume</div>
      <div class="clist">
        <div class="cli"><span class="cnum">06</span><span><span class="cnm">Radical Obedience</span><br><span class="cds">The costly, all-in yes</span></span></div>
        <div class="cli"><span class="cnum">07</span><span><span class="cnm">Spirit-Led Decisions</span><br><span class="cds">Bring every choice under God</span></span></div>
        <div class="cli"><span class="cnum">08</span><span><span class="cnm">Following God\u2019s Whisper</span><br><span class="cds">Walk it out, one step at a time</span></span></div>
        <div class="cli"><span class="cnum">09</span><span><span class="cnm">Daily Surrender</span><br><span class="cds">Lay down your will each morning</span></span></div>
        <div class="cli"><span class="cnum">10</span><span><span class="cnm">Saying Yes to God</span><br><span class="cds">A willing yes before the question</span></span></div>
      </div>
    </div>
  </div>
</div>"""

closing = """
<div class="page close">
  <div class="frame"></div>
  <div class="close-inner">
    <div class="kicker">Ready When You Are</div>
    <h2>Help your church say<br><em>yes</em> \u2014 and mean it.</h2>
    <p class="cp">These five campaigns carry your people past hearing into following \u2014 the radical yes, the Spirit-led choice, the next faithful step, the daily surrender, and the willing availability God is always looking for. Choose where your church is ready to grow, or move through all five across a season.</p>
    <div class="close-list">
      <div class="cl-row"><span class="cln">06</span><span class="clt">Radical Obedience</span><span class="cld">Leave the nets</span></div>
      <div class="cl-row"><span class="cln">07</span><span class="clt">Spirit-Led Decisions</span><span class="cld">Straight paths</span></div>
      <div class="cl-row"><span class="cln">08</span><span class="clt">Following God\u2019s Whisper</span><span class="cld">This is the way</span></div>
      <div class="cl-row"><span class="cln">09</span><span class="clt">Daily Surrender</span><span class="cld">The daily cross</span></div>
      <div class="cl-row"><span class="cln">10</span><span class="clt">Saying Yes to God</span><span class="cld">Here am I</span></div>
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
<title>The Obedience Collection, Volume Two \u2014 Lifetogether</title>
<style>{FONTS}</style>
<style>{CSS}</style>
</head><body>{pages}</body></html>"""

pathlib.Path("/tmp/obedience_v2.html").write_text(doc, encoding="utf-8")
print("HTML written:", len(doc), "chars")
