# -*- coding: utf-8 -*-
import pathlib
from brochure_template import FONTS, CSS, campaign_page

campaigns = [
{
 "num":"06","accent":"#34507e","accent_soft":"#d8e0ee",
 "title_a":"Living as","title_b":"a Steward",
 "subtitle":"The everyday posture that turns ordinary days into worship",
 "problem":"It\u2019s one thing to believe you\u2019re a steward. It\u2019s another to live like one at 7 a.m. on a Tuesday. For most of us, stewardship stays a Sunday idea \u2014 agreed with in principle, forgotten by Monday \u2014 while our actual days run on autopilot, owned by habit, hurry, and self.",
 "promise":"Living as a Steward moves stewardship from belief to behavior. Over forty days your people learn to carry a steward\u2019s mindset into their work, their homes, and their ordinary routines \u2014 until even the most unremarkable day becomes an act of worship offered to an audience of One.",
 "verse":"Whatever you do, work at it with all your heart, as working for the Lord, not for human masters.",
 "ref":"Colossians 3:23 (NIV)",
 "bigidea":"Stewardship isn\u2019t something you do once a year at the offering. It\u2019s a way of living you practice every ordinary hour.",
 "tags":["Daily Life","Work","Worship","Mindset","Integrity"],
 "best_for":"Church &amp; Company","backbone":"Colossians 3:23\u201324; 1 Cor 10:31","metaphor":"An Audience of One","felt":"Daily practice, work, identity",
 "sessions":[
   ("1","Stewardship by 7 a.m.","Bringing a steward\u2019s mindset into the very start of the day."),
   ("2","An Audience of One","Why who you work for changes how you work."),
   ("3","The Steward at Home","Managing your household and relationships as a sacred trust."),
   ("4","Faithful in the Routine","Finding worship in the unremarkable, repeated tasks."),
   ("5","Margin for the Master","Leaving room in your days for what God might ask."),
   ("6","A Steward\u2019s Ordinary Day","Living the whole rhythm of life on purpose."),
 ],
 "journey":"Each of the 40 days takes one ordinary moment \u2014 a task, a meal, a meeting, a chore \u2014 and reframes it as something offered to God, with a partner check-in and a prayer.",
 "why":"Most of life isn\u2019t spent on mountaintops. It\u2019s spent on Tuesdays. Stewardship that doesn\u2019t touch Tuesday doesn\u2019t touch much.",
 "cta":"Launch Living as a Steward and help your people worship God in their ordinary days.",
 "note":None,
},
{
 "num":"07","accent":"#5e4b86","accent_soft":"#e3def0",
 "title_a":"Kingdom","title_b":"Stewardship",
 "subtitle":"Managing all you have to advance what matters most to God",
 "problem":"Even faithful stewards can quietly aim too low \u2014 managing their resources mainly for their own comfort, security, and future. But the King didn\u2019t entrust us with time, talent, and treasure simply so we\u2019d be well-off. He gave them to be invested in something far larger than ourselves: His kingdom.",
 "promise":"Kingdom Stewardship lifts your people\u2019s sights. Over forty days they learn to manage all they\u2019ve been given as capital for God\u2019s mission \u2014 putting their resources to work for eternal returns and discovering the joy of being part of the King\u2019s business.",
 "verse":"Put this money to work until I come back.",
 "ref":"Luke 19:13 (NIV)",
 "bigidea":"You weren\u2019t entrusted with resources just to be comfortable. You were entrusted with them to be useful \u2014 to put what you hold to work for the King until He returns.",
 "tags":["Kingdom","Mission","Eternal Returns","Investment","Purpose"],
 "best_for":"Church &amp; Company","backbone":"Luke 19:11\u201327; Matthew 6:33","metaphor":"The King\u2019s Business","felt":"Mission, kingdom purpose, eternal investment",
 "sessions":[
   ("1","Aiming Too Low","Why comfort is a poor goal for a steward of the King."),
   ("2","The King\u2019s Business","Seeing your resources as capital for God\u2019s mission."),
   ("3","Put It to Work","Why God entrusts in order to multiply, not merely to store."),
   ("4","Eternal Returns","Investing in what pays dividends forever."),
   ("5","Stewards on Mission","Joining what God is doing with all you have."),
   ("6","Until He Comes","Living every day as the King\u2019s faithful representative."),
 ],
 "journey":"Each of the 40 days connects one resource \u2014 an hour, a skill, a dollar \u2014 to one kingdom purpose and one small act of investing it, with a partner check-in and a prayer.",
 "why":"The question isn\u2019t only \u201cam I managing this well?\u201d but \u201cwhat am I managing it for?\u201d Kingdom stewardship answers both.",
 "cta":"Launch Kingdom Stewardship and help your people put all they have to work for the King.",
 "note":None,
},
{
 "num":"08","accent":"#2f6b4f","accent_soft":"#d8e8df",
 "title_a":"The Stewarded","title_b":"Life",
 "subtitle":"What a life fully surrendered to God becomes",
 "problem":"We try to steward pieces of our lives \u2014 a budget here, a calendar there \u2014 while keeping the deeper self under our own control. But a life managed in fragments stays fragmented: anxious, scattered, quietly exhausting. The one thing we rarely surrender is the whole.",
 "promise":"The Stewarded Life invites your people to offer everything. Over forty days they move from managing parts to surrendering the whole self to God \u2014 and discover that a fully yielded life isn\u2019t a diminished one but an integrated, ordered, and surprisingly peaceful one.",
 "verse":"\u2026offer your bodies as a living sacrifice, holy and pleasing to God \u2014 this is your true and proper worship.",
 "ref":"Romans 12:1 (NIV)",
 "bigidea":"The ultimate act of stewardship isn\u2019t managing your resources better \u2014 it\u2019s surrendering yourself entirely. A fully yielded life is a fully alive one.",
 "tags":["Surrender","Wholeness","Worship","Integration","Rest"],
 "best_for":"Church &amp; Company","backbone":"Romans 12:1\u20132; Galatians 2:20","metaphor":"A Life Fully Yielded","felt":"Surrender, wholeness, identity",
 "sessions":[
   ("1","The Life We Withhold","Naming the parts of ourselves we never hand over."),
   ("2","A Living Sacrifice","What it means to offer the whole self to God."),
   ("3","From Fragments to Whole","How surrender brings a scattered life together."),
   ("4","No Longer My Own","The freedom of belonging completely to God."),
   ("5","Ordered from the Inside","Why inner surrender produces outer peace."),
   ("6","Fully Alive","The unexpected joy of a fully stewarded life."),
 ],
 "journey":"Each day surfaces one area still held back and offers one small act of surrender, with a partner check-in and a prayer \u2014 a daily yielding of the whole self.",
 "why":"You can manage your money perfectly and still never give God the one thing He most wants: you.",
 "cta":"Launch The Stewarded Life and help your people surrender the whole, not just the parts.",
 "note":None,
},
{
 "num":"09","accent":"#b08423","accent_soft":"#f0e6cc",
 "title_a":"Stewarding Your","title_b":"Influence",
 "subtitle":"Using your reach, your words, and your example for good",
 "problem":"We rarely think of our influence as something to manage \u2014 yet every one of us holds it: over a family, a team, a friend group, a feed of followers, a watching child. And influence left unstewarded doesn\u2019t stay neutral. It quietly shapes people, for better or worse, whether we mean it to or not.",
 "promise":"Stewarding Your Influence helps your people steward the reach they already have. Over forty days they learn to see their words, example, leadership, and relationships as a trust \u2014 and to use that influence intentionally to point others toward what is good, true, and God-honoring.",
 "verse":"\u2026let your light shine before others, that they may see your good deeds and glorify your Father in heaven.",
 "ref":"Matthew 5:16 (NIV)",
 "bigidea":"You are already influencing someone. The only question is whether you\u2019re stewarding that influence on purpose \u2014 or leaking it by accident.",
 "tags":["Influence","Leadership","Words","Example","Testimony"],
 "best_for":"Church &amp; Company","backbone":"Matthew 5:14\u201316; Titus 2:7","metaphor":"A City on a Hill","felt":"Influence, leadership, testimony",
 "sessions":[
   ("1","You Have Influence","Recognizing the reach you didn\u2019t know you had."),
   ("2","Light on a Hill","Why your example is meant to be seen, not hidden."),
   ("3","Stewarding Your Words","The weight and power of what you say."),
   ("4","Leading Where You Are","Influencing well in the spaces you already occupy."),
   ("5","Influence as Testimony","Letting your life quietly point to God."),
   ("6","A Lasting Mark","Using your influence for what outlives you."),
 ],
 "journey":"Each of the 40 days names one relationship or platform and offers one intentional act of positive influence, with a partner check-in and a prayer.",
 "why":"Influence is the one resource we all spend whether we manage it or not. Stewarding it on purpose changes the people around you.",
 "cta":"Launch Stewarding Your Influence and help your people use their reach for good.",
 "note":None,
},
{
 "num":"10","accent":"#b25a39","accent_soft":"#f2ddd2",
 "title_a":"Living","title_b":"Open-Handed",
 "subtitle":"The freedom of holding everything loosely",
 "problem":"Most of us live with closed fists \u2014 gripping our money, our time, our plans, our stuff, afraid of what we might lose. But a clenched hand can\u2019t give and can\u2019t receive. The grip we think keeps us safe is often the very thing that keeps us anxious, exhausted, and small.",
 "promise":"Living Open-Handed teaches your people the freedom of the loosened grip. Over forty days they learn to hold everything as a gift rather than a possession \u2014 quick to give, slow to cling \u2014 and discover the deep, generous joy Jesus promised to those who release rather than hoard.",
 "verse":"It is more blessed to give than to receive.",
 "ref":"Acts 20:35 (NIV)",
 "bigidea":"An open hand can do what a closed fist never will: give freely, receive gratefully, and let go without fear. That\u2019s the steward\u2019s freedom.",
 "tags":["Generosity","Holding Loosely","Freedom","Giving","Open Hands"],
 "best_for":"Church &amp; Company","backbone":"Acts 20:35; 2 Cor 9:6\u20138","metaphor":"The Open Hand","felt":"Generosity, holding loosely, freedom",
 "sessions":[
   ("1","The Cost of the Closed Fist","How gripping what we have quietly steals our peace."),
   ("2","Everything Is a Gift","Learning to hold what we have as borrowed, not owned."),
   ("3","Quick to Give","Building the reflex of open-handed generosity."),
   ("4","Slow to Cling","Loosening our grip on money, plans, and control."),
   ("5","More Blessed to Give","Discovering the joy Jesus promised to the generous."),
   ("6","A Life of Open Hands","Living free, light, and always ready to give."),
 ],
 "journey":"Each of the 40 days invites one small act of letting go or giving away, with a partner check-in and a prayer \u2014 a daily loosening of the grip until open hands become second nature.",
 "why":"The tightest grip and the heaviest heart usually belong to the same person. Open hands are lighter \u2014 and far more free.",
 "cta":"Launch Living Open-Handed and help your people trade the closed fist for the open hand.",
 "note":None,
},
]

cover = """
<div class="page cover">
  <div class="frame gold"></div>
  <div class="cover-inner">
    <div class="brandmark">Lifetogether</div>
    <div class="kicker">The Campaign Library &nbsp;&middot;&nbsp; Stewardship &nbsp;&middot;&nbsp; Volume Two</div>
    <div class="cover-rule"></div>
    <h1>The <em>Stewardship</em><br>Collection</h1>
    <div class="sub">Five more forty-day campaigns that move stewardship from idea to way of life \u2014 in your people\u2019s daily work, their mission, their surrender, their influence, and their open-handed generosity.</div>
    <div class="cover-foot">
      <div class="stats">
        <div class="stat"><div class="n">5</div><div class="l">Campaigns</div></div>
        <div class="stat"><div class="n">40</div><div class="l">Day Journey</div></div>
        <div class="stat"><div class="n">6</div><div class="l">Sessions Each</div></div>
        <div class="stat"><div class="n">NIV</div><div class="l">Scripture</div></div>
      </div>
      <div class="tier">Tier 1 &nbsp;&middot;&nbsp; Titles 06\u201310 &nbsp;&middot;&nbsp; For Churches &amp; Companies</div>
    </div>
  </div>
</div>"""

intro = """
<div class="page intro">
  <div class="frame"></div>
  <div class="intro-inner">
    <div class="kicker">Before You Begin</div>
    <h2>Stewardship isn\u2019t a topic.<br>It\u2019s a <em>way of living</em>.</h2>
    <p class="lead">It\u2019s one thing to agree that we\u2019re stewards. It\u2019s another to actually live like one \u2014 in our work, our mission, our surrender, our influence, and the way we hold what we own. <strong>This second volume takes stewardship out of the abstract</strong> and into the texture of everyday life, with five distinct forty-day journeys that help your people not just understand stewardship, but embody it.</p>
    <div class="howrow">
      <div class="howcard"><div class="hn">40</div><h4>A Daily Rhythm</h4><p>Every day offers a short reading, one practical step, a spiritual-partner check-in, and a written prayer &mdash; small, repeatable, and easy to keep.</p></div>
      <div class="howcard"><div class="hn">6</div><h4>A Weekly Gathering</h4><p>Six group sessions give the journey its backbone, turning private change into shared momentum across your church or team.</p></div>
      <div class="howcard"><div class="hn">1</div><h4>A Clear Outcome</h4><p>Each campaign is built around one transformation &mdash; so your people don\u2019t just learn about stewardship, they begin to live it out.</p></div>
    </div>
    <div class="contents">
      <div class="ct">Inside This Volume</div>
      <div class="clist">
        <div class="cli"><span class="cnum">06</span><span><span class="cnm">Living as a Steward</span><br><span class="cds">Steward your ordinary, everyday life</span></span></div>
        <div class="cli"><span class="cnum">07</span><span><span class="cnm">Kingdom Stewardship</span><br><span class="cds">Manage all you have for God\u2019s mission</span></span></div>
        <div class="cli"><span class="cnum">08</span><span><span class="cnm">The Stewarded Life</span><br><span class="cds">Surrender the whole self to God</span></span></div>
        <div class="cli"><span class="cnum">09</span><span><span class="cnm">Stewarding Your Influence</span><br><span class="cds">Use your reach and example for good</span></span></div>
        <div class="cli"><span class="cnum">10</span><span><span class="cnm">Living Open-Handed</span><br><span class="cds">Hold everything loosely and give freely</span></span></div>
      </div>
    </div>
  </div>
</div>"""

closing = """
<div class="page close">
  <div class="frame"></div>
  <div class="close-inner">
    <div class="kicker">Ready When You Are</div>
    <h2>From understanding stewardship<br>to <em>living</em> it.</h2>
    <p class="cp">These five campaigns meet your people in the everyday places stewardship is actually lived \u2014 their Tuesday mornings, their mission, their surrender, their influence, and their grip on what they hold. Choose where your church or team is ready to grow, or move through all five across a season.</p>
    <div class="close-list">
      <div class="cl-row"><span class="cln">06</span><span class="clt">Living as a Steward</span><span class="cld">Everyday worship</span></div>
      <div class="cl-row"><span class="cln">07</span><span class="clt">Kingdom Stewardship</span><span class="cld">On mission</span></div>
      <div class="cl-row"><span class="cln">08</span><span class="clt">The Stewarded Life</span><span class="cld">Full surrender</span></div>
      <div class="cl-row"><span class="cln">09</span><span class="clt">Stewarding Your Influence</span><span class="cld">Reach for good</span></div>
      <div class="cl-row"><span class="cln">10</span><span class="clt">Living Open-Handed</span><span class="cld">Holding loosely</span></div>
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
<title>The Stewardship Collection, Volume Two \u2014 Lifetogether</title>
<style>{FONTS}</style>
<style>{CSS}</style>
</head><body>{pages}</body></html>"""

pathlib.Path("/tmp/stewardship_v2.html").write_text(doc, encoding="utf-8")
print("HTML written:", len(doc), "chars")
