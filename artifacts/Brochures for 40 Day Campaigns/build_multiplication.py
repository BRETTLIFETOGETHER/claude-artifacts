# -*- coding: utf-8 -*-
import pathlib
from brochure_template import FONTS, CSS, campaign_page

campaigns = [
{
 "num":"01","accent":"#2a5b86","accent_soft":"#d7e3ed",
 "title_a":"","title_b":"Leverage",
 "subtitle":"The kingdom principle of outsized impact from small beginnings",
 "problem":"Most of us think in terms of addition \u2014 do a little good, then a little more, one effort at a time. It\u2019s faithful, but it\u2019s slow, and it quietly caps what a single life can accomplish. Meanwhile, Jesus kept describing a kingdom that works nothing like addition: a tiny seed that becomes the largest tree, a little yeast that works through the whole batch.",
 "promise":"Leverage reorients your people to the math of the kingdom. Over forty days they\u2019ll discover the principle of multiplication built into everything God does \u2014 and learn to position their small, faithful inputs where they yield a disproportionate, lasting return for His purposes.",
 "verse":"Though it is the smallest of all seeds, \u2026 it becomes a tree.",
 "ref":"Matthew 13:32 (NIV)",
 "bigidea":"The kingdom doesn\u2019t run on addition; it runs on multiplication. A small thing, placed in the right spot, can yield a return all out of proportion to its size.",
 "tags":["Multiplication","Leverage","The Mustard Seed","Impact","Strategy"],
 "best_for":"Company &amp; Church","backbone":"Matthew 13:31\u201333; Zechariah 4:10","metaphor":"The Mustard Seed","felt":"The multiplication mindset, leverage principle",
 "sessions":[
   ("1","Addition vs. Multiplication","Why one faithful life can do far more than we think."),
   ("2","The Mustard Seed","How God turns the small into the staggering."),
   ("3","A Little Yeast","The quiet power of well-placed influence."),
   ("4","Small Beginnings","Why God starts most multiplication with something tiny."),
   ("5","The Right Fulcrum","Placing your effort where it yields the most."),
   ("6","A Leveraged Life","Living for multiplied, not merely added, impact."),
 ],
 "journey":"Each of the 40 days identifies one small, well-placed action with outsized potential and invites your people to take it, with a partner check-in and a prayer.",
 "why":"A life of addition does some good. A life of multiplication changes everything around it \u2014 and most people have no idea the leverage already in their hands.",
 "cta":"Launch Leverage and help your people trade addition for multiplication.",
 "note":None,
},
{
 "num":"02","accent":"#2f7050","accent_soft":"#d8e8df",
 "title_a":"Multiplying","title_b":"Your Life",
 "subtitle":"Reproducing what God has done in you in the lives of others",
 "problem":"Most of us pour our best energy into things that stop when we do \u2014 tasks, projects, achievements that end with our involvement. But the one investment that keeps multiplying long after we\u2019re gone is the one we most often neglect: pouring our lives into other people who will, in turn, pour into others.",
 "promise":"Multiplying Your Life shifts your people from producing to reproducing. Over forty days they learn the ancient pattern of multiplication through people \u2014 the way Paul invested in Timothy, who invested in others \u2014 and discover the deep joy of a life whose impact outlives and outgrows them.",
 "verse":"\u2026entrust to reliable people who will also be qualified to teach others.",
 "ref":"2 Timothy 2:2 (NIV)",
 "bigidea":"The most multiplying thing you can do with your life is to give it away to people \u2014 because people, unlike projects, go on to multiply into others.",
 "tags":["Discipleship","Mentoring","Reproduction","Legacy","Investing in People"],
 "best_for":"Company &amp; Church","backbone":"2 Timothy 2:2; Mark 3:14","metaphor":"Four Generations","felt":"Discipleship, reproducing your life in others",
 "sessions":[
   ("1","Producing vs. Reproducing","Why most of our impact stops when we do."),
   ("2","The Paul-and-Timothy Pattern","God\u2019s design for multiplying through people."),
   ("3","Investing in a Few","Why depth with a handful beats breadth with a crowd."),
   ("4","Four Generations Deep","Reliable people who teach reliable people."),
   ("5","The Joy of Pouring In","Discovering the gladness of giving your life away."),
   ("6","A Multiplied Life","Building impact that outlives you."),
 ],
 "journey":"Each of the 40 days invests one intentional moment in another person \u2014 a word, a lesson, an encouragement \u2014 with a partner check-in and a prayer, building the habit of pouring into others.",
 "why":"You can spend a life producing and leave little behind, or spend it reproducing and watch your impact multiply for generations. The choice is daily.",
 "cta":"Launch Multiplying Your Life and help your people pour into the next generation.",
 "note":None,
},
{
 "num":"03","accent":"#5b4a86","accent_soft":"#e3def0",
 "title_a":"Kingdom","title_b":"Multiplication",
 "subtitle":"Joining the exponential spread of God\u2019s kingdom",
 "problem":"We often picture the kingdom of God advancing slowly, one careful convert at a time \u2014 and we play our small part and hope it adds up. But the kingdom in Scripture moves very differently: a few disciples become thousands, the word spreads and multiplies, a single seed yields thirty, sixty, a hundredfold. We\u2019ve been thinking too small about what God wants to do.",
 "promise":"Kingdom Multiplication enlarges your people\u2019s vision. Over forty days they\u2019ll catch sight of the exponential way God\u2019s kingdom actually grows \u2014 and find their place in a movement far bigger than themselves, sowing seeds that multiply well beyond what they could ask or imagine.",
 "verse":"\u2026they hear the word, accept it, and produce a crop \u2014 thirty, sixty or even a hundred times.",
 "ref":"Mark 4:20 (NIV)",
 "bigidea":"God isn\u2019t running an addition project; He\u2019s growing a movement. The same kingdom that started with twelve has never stopped multiplying \u2014 and your people are part of it.",
 "tags":["Kingdom","The Gospel","Movements","Hundredfold","Mission"],
 "best_for":"Company &amp; Church","backbone":"Mark 4:1\u201320; Acts 6:7","metaphor":"Thirty, Sixty, a Hundredfold","felt":"Kingdom/gospel multiplication, movements",
 "sessions":[
   ("1","Thinking Too Small","Why we underestimate what God wants to do."),
   ("2","Thirty, Sixty, a Hundredfold","The exponential harvest Jesus described."),
   ("3","From Twelve to the World","How the kingdom has always multiplied."),
   ("4","Sowing for a Movement","Scattering seed with multiplication in mind."),
   ("5","Your Part in the Spread","Finding your place in something bigger."),
   ("6","A Multiplying Kingdom","Living for a harvest beyond your lifetime."),
 ],
 "journey":"Each of the 40 days plants one seed for the kingdom \u2014 a conversation, an invitation, a prayer \u2014 trusting God for a multiplied harvest, with a partner check-in and a prayer.",
 "why":"A church thinking in addition plays small. A church catching God\u2019s vision for multiplication starts movements. The difference begins with vision.",
 "cta":"Launch Kingdom Multiplication and help your people sow for a multiplied harvest.",
 "note":None,
},
{
 "num":"04","accent":"#b8902f","accent_soft":"#f1e8cd",
 "title_a":"Leveraged for","title_b":"Impact",
 "subtitle":"Using your platform, position, and resources to make a real difference",
 "problem":"Most of us underestimate the leverage already sitting in our hands \u2014 a job, a network, a budget, a skill set, a seat at some table. We treat these as merely ours to enjoy or get by on, never realizing they\u2019re tools that could be aimed at something far bigger. And so enormous potential for good sits idle.",
 "promise":"Leveraged for Impact helps your people put what they have to work. Over forty days they\u2019ll learn to leverage their platform, position, and resources \u2014 turning the temporal things they manage into eternal impact \u2014 and discover how much good a single, strategically deployed life can actually do.",
 "verse":"Use worldly wealth to gain friends for yourselves, so that\u2026 you will be welcomed into eternal dwellings.",
 "ref":"Luke 16:9 (NIV)",
 "bigidea":"The resources, relationships, and influence you already have are leverage \u2014 temporary tools that can be aimed at eternal impact. The only question is whether you\u2019ll use them.",
 "tags":["Platform","Resources","Impact","Marketplace","Strategy"],
 "best_for":"Company &amp; Church","backbone":"Luke 16:9; Genesis 50:20","metaphor":"Temporal for Eternal","felt":"Leveraging your platform and resources for impact",
 "sessions":[
   ("1","The Leverage in Your Hands","Taking inventory of what you\u2019ve underestimated."),
   ("2","Temporal for Eternal","Trading what won\u2019t last for what will."),
   ("3","Your Platform on Purpose","Aiming your position at something bigger."),
   ("4","Resources as Tools","Deploying what you manage for lasting good."),
   ("5","Strategic Generosity","Placing your impact where it counts most."),
   ("6","A Life That Counts","Becoming a person whose leverage serves the kingdom."),
 ],
 "journey":"Each of the 40 days identifies one resource or relationship your people hold and one way to leverage it for lasting impact, with a partner check-in and a prayer.",
 "why":"God has handed your people more leverage than they realize. Help them see it and aim it, and watch ordinary lives make extraordinary impact.",
 "cta":"Launch Leveraged for Impact and help your people aim what they have at what lasts.",
 "note":None,
},
{
 "num":"05","accent":"#2d7a8a","accent_soft":"#d6e9ed",
 "title_a":"Stewarding","title_b":"Influence",
 "subtitle":"Recognizing you were positioned, for such a time as this",
 "problem":"Many of us assume influence belongs to other people \u2014 the famous, the powerful, the platformed \u2014 and quietly excuse ourselves from the responsibility of it. But every one of us has been positioned: in a family, a workplace, a community, a moment. And influence that goes unrecognized is influence that goes unused, right when it was needed most.",
 "promise":"Stewarding Influence opens your people\u2019s eyes to their God-given position. Over forty days they\u2019ll come to see the sphere of influence they already hold \u2014 and, like Esther, recognize they may have come to it \u201cfor such a time as this,\u201d learning to deploy it courageously to multiply good.",
 "verse":"\u2026who knows but that you have come to your royal position for such a time as this?",
 "ref":"Esther 4:14 (NIV)",
 "bigidea":"You were positioned on purpose. The influence you hold \u2014 however ordinary it seems \u2014 was given for a moment and a mission bigger than yourself.",
 "tags":["Influence","Position","Courage","Timing","Multiplication"],
 "best_for":"Company &amp; Church","backbone":"Esther 4:12\u201316; Daniel 1","metaphor":"Positioned on Purpose","felt":"Using influence and position for kingdom purposes",
 "sessions":[
   ("1","Influence Is Not for the Few","Recognizing the sphere you already have."),
   ("2","For Such a Time as This","Esther\u2019s discovery of her positioned purpose."),
   ("3","Positioned on Purpose","Why God places His people where He does."),
   ("4","The Courage to Use It","Stepping into influence when it counts."),
   ("5","Multiplying the Good","Deploying your influence for others, not yourself."),
   ("6","A Positioned People","Living awake to the moments you\u2019re made for."),
 ],
 "journey":"Each of the 40 days names one sphere of influence your people hold and one courageous way to use it for good, with a partner check-in and a prayer.",
 "why":"History turns on people who recognized their moment and used their influence for others. Your people are positioned for such a time \u2014 if they\u2019ll see it.",
 "cta":"Launch Stewarding Influence and help your people step into the moment they were made for.",
 "note":None,
},
]

for _c in campaigns:
    _c["category"] = "Multiplication"
    _c["tier"] = "Tier 2"
    _c["audience"] = "Company + Church"

cover = """
<div class="page cover">
  <div class="frame gold"></div>
  <div class="cover-inner">
    <div class="brandmark">Lifetogether</div>
    <div class="kicker">The Campaign Library &nbsp;&middot;&nbsp; Multiplication Collection</div>
    <div class="cover-rule"></div>
    <h1>The <em>Multiplication</em><br>Collection</h1>
    <div class="sub">Five forty-day campaigns to help your people move from addition to multiplication \u2014 leveraging their lives, influence, and resources for outsized kingdom impact.</div>
    <div class="cover-foot">
      <div class="stats">
        <div class="stat"><div class="n">5</div><div class="l">Campaigns</div></div>
        <div class="stat"><div class="n">40</div><div class="l">Day Journey</div></div>
        <div class="stat"><div class="n">6</div><div class="l">Sessions Each</div></div>
        <div class="stat"><div class="n">NIV</div><div class="l">Scripture</div></div>
      </div>
      <div class="tier">Tier 2 &nbsp;&middot;&nbsp; Influence &amp; Scale &nbsp;&middot;&nbsp; For Companies &amp; Churches</div>
    </div>
  </div>
</div>"""

intro = """
<div class="page intro">
  <div class="frame"></div>
  <div class="intro-inner">
    <div class="kicker">Before You Begin</div>
    <h2>God\u2019s kingdom doesn\u2019t add.<br>It <em>multiplies</em>.</h2>
    <p class="lead">A mustard seed becomes the largest tree. A little yeast works through the whole batch. Twelve ordinary followers become a movement that reaches the world. <strong>Multiplication is the math of the kingdom</strong> \u2014 and most of us are still living by addition, doing a little good one effort at a time while the leverage in our hands sits unused. These five distinct, forty-day journeys help your people move from adding to multiplying \u2014 through their lives, their influence, and all they\u2019ve been given.</p>
    <div class="howrow">
      <div class="howcard"><div class="hn">40</div><h4>A Daily Rhythm</h4><p>Every day offers a short reading, one practical step, a spiritual-partner check-in, and a written prayer &mdash; small, repeatable, and easy to keep.</p></div>
      <div class="howcard"><div class="hn">6</div><h4>A Weekly Gathering</h4><p>Six group sessions give the journey its backbone, turning private growth into shared momentum across your company or church.</p></div>
      <div class="howcard"><div class="hn">1</div><h4>A Clear Outcome</h4><p>Each campaign is built around one transformation &mdash; so your people don\u2019t just admire multiplication, they begin to live it.</p></div>
    </div>
    <div class="contents">
      <div class="ct">Inside This Collection</div>
      <div class="clist">
        <div class="cli"><span class="cnum">01</span><span><span class="cnm">Leverage</span><br><span class="cds">Trade addition for multiplication</span></span></div>
        <div class="cli"><span class="cnum">02</span><span><span class="cnm">Multiplying Your Life</span><br><span class="cds">Reproduce your life in others</span></span></div>
        <div class="cli"><span class="cnum">03</span><span><span class="cnm">Kingdom Multiplication</span><br><span class="cds">Join the exponential spread of the kingdom</span></span></div>
        <div class="cli"><span class="cnum">04</span><span><span class="cnm">Leveraged for Impact</span><br><span class="cds">Aim your platform at what lasts</span></span></div>
        <div class="cli"><span class="cnum">05</span><span><span class="cnm">Stewarding Influence</span><br><span class="cds">Step into the moment you\u2019re made for</span></span></div>
      </div>
    </div>
  </div>
</div>"""

closing = """
<div class="page close">
  <div class="frame"></div>
  <div class="close-inner">
    <div class="kicker">Ready When You Are</div>
    <h2>Help your people multiply<br>what God has <em>given</em>.</h2>
    <p class="cp">From the principle of leverage to a life poured into others, these five campaigns move your people out of addition and into the multiplied impact God designed them for \u2014 through people, the kingdom, their platform, and their influence. Choose where your company or church is ready to grow, or journey through all five across a season.</p>
    <div class="close-list">
      <div class="cl-row"><span class="cln">01</span><span class="clt">Leverage</span><span class="cld">The mustard seed</span></div>
      <div class="cl-row"><span class="cln">02</span><span class="clt">Multiplying Your Life</span><span class="cld">Four generations</span></div>
      <div class="cl-row"><span class="cln">03</span><span class="clt">Kingdom Multiplication</span><span class="cld">A hundredfold</span></div>
      <div class="cl-row"><span class="cln">04</span><span class="clt">Leveraged for Impact</span><span class="cld">Temporal for eternal</span></div>
      <div class="cl-row"><span class="cln">05</span><span class="clt">Stewarding Influence</span><span class="cld">For such a time</span></div>
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
<title>The Multiplication Collection \u2014 Lifetogether</title>
<style>{FONTS}</style>
<style>{CSS}</style>
</head><body>{pages}</body></html>"""

pathlib.Path("/tmp/multiplication.html").write_text(doc, encoding="utf-8")
print("HTML written:", len(doc), "chars")
