# -*- coding: utf-8 -*-
import pathlib
from brochure_template import FONTS, CSS, campaign_page

campaigns = [
{
 "num":"01","accent":"#b8902f","accent_soft":"#f1e8cd",
 "title_a":"","title_b":"Abundance",
 "subtitle":"The full life Jesus actually came to give",
 "problem":"Somewhere along the way, many of us settled for a smaller life than God intended \u2014 cautious, depleted, just getting by. We\u2019ve quietly assumed that scarcity is normal and that faith is mostly about endurance. But Jesus described His mission in startlingly different terms: not survival, but fullness; not barely enough, but life to the full.",
 "promise":"Abundance reintroduces your people to the heart of God. Over forty days they\u2019ll confront the thief that has been shrinking their lives and rediscover the One who came to make them full \u2014 trading a scarcity-bound existence for the abundant life Jesus has been offering all along.",
 "verse":"I have come that they may have life, and have it to the full.",
 "ref":"John 10:10 (NIV)",
 "bigidea":"God\u2019s default is not scarcity but abundance. The thief came to shrink your life; Jesus came to fill it. Most of us are living far below the line He drew.",
 "tags":["Fullness","Abundant Life","God\u2019s Heart","Scarcity","Hope"],
 "best_for":"Church &amp; Company","backbone":"John 10:10; Psalm 36:8","metaphor":"Life to the Full","felt":"The abundant life, God\u2019s generous heart",
 "sessions":[
   ("1","The Smaller Life","How we quietly settled for less than God intended."),
   ("2","The Thief\u2019s Work","Naming what\u2019s been stealing, killing, and destroying."),
   ("3","Life to the Full","What Jesus actually promised \u2014 and meant."),
   ("4","Scarcity Is Not Your Story","Unlearning the lie that there\u2019s never enough."),
   ("5","The Heart of God","Discovering a Father whose default is generosity."),
   ("6","Stepping Into Abundance","Beginning to live the fuller life on offer."),
 ],
 "journey":"Each of the 40 days names one scarcity belief and replaces it with one truth about God\u2019s abundant heart, with a partner check-in and a prayer \u2014 slowly enlarging a life that had grown too small.",
 "why":"Jesus didn\u2019t die to give His people a cramped, anxious, just-getting-by existence. He came so they could be full \u2014 and most have never stepped into it.",
 "cta":"Launch Abundance and help your people step into the full life Jesus offers.",
 "note":None,
},
{
 "num":"02","accent":"#2e8d77","accent_soft":"#d2eee6",
 "title_a":"","title_b":"Overflow",
 "subtitle":"A life so full of God it spills into everything",
 "problem":"Even people who\u2019ve tasted God\u2019s goodness often keep it carefully contained \u2014 a private faith, a Sunday fullness that never quite reaches Monday\u2019s relationships, work, or worries. But God never designed His life in us to be a sealed reservoir. When His presence truly fills a person, it was always meant to overflow.",
 "promise":"Overflow opens the floodgates. Over forty days your people learn to be so filled by God\u2019s Spirit that His life begins to spill out of them \u2014 into their homes, their work, their friendships, their fruitfulness \u2014 until the abundance within becomes blessing all around them.",
 "verse":"\u2026rivers of living water will flow from within them.",
 "ref":"John 7:38 (NIV)",
 "bigidea":"What God pours into you was never meant to stay in you. A life truly filled by Him overflows \u2014 into your relationships, your work, your fruitfulness \u2014 almost without trying.",
 "tags":["Overflow","Fruitfulness","Spirit-Filled","Blessing","Influence"],
 "best_for":"Church &amp; Company","backbone":"John 7:37\u201339; John 15:5","metaphor":"Rivers of Living Water","felt":"Overflow into every area, fruitfulness",
 "sessions":[
   ("1","The Sealed Reservoir","Why a contained faith eventually goes stale."),
   ("2","Rivers from Within","The overflowing life Jesus promised His followers."),
   ("3","Filled to Overflowing","Receiving more of the Spirit\u2019s fullness."),
   ("4","Overflow at Home and Work","Letting His life reach your everyday world."),
   ("5","Abide and Bear Fruit","How staying connected produces natural fruitfulness."),
   ("6","A Life That Spills","Becoming a source of blessing to everyone near you."),
 ],
 "journey":"Each of the 40 days pairs one way to be filled by God with one way to let that fullness overflow into someone or something around you, with a partner check-in and a prayer.",
 "why":"The most life-giving people you know aren\u2019t trying hard to bless others \u2014 they\u2019re simply so full of God that it overflows. That life is available to your people.",
 "cta":"Launch Overflow and help your people become rivers, not reservoirs.",
 "note":None,
},
{
 "num":"03","accent":"#c75d34","accent_soft":"#f6ddd0",
 "title_a":"Living Fully","title_b":"Alive",
 "subtitle":"Waking up to a vibrant, awake, fully alive life with God",
 "problem":"It\u2019s possible to be technically alive and yet mostly asleep \u2014 moving through days on autopilot, numb to wonder, dulled by routine, present but not really awake. Many believers aren\u2019t battling dramatic sin so much as a quiet deadness, a low-grade going-through-the-motions that has them existing rather than truly living.",
 "promise":"Living Fully Alive is a wake-up call. Over forty days your people shake off spiritual sleep and come alive to God, to wonder, to purpose, and to the vivid life right in front of them \u2014 discovering that the One who raises the dead delights in making His people fully, gloriously awake.",
 "verse":"Wake up, sleeper, rise from the dead, and Christ will shine on you.",
 "ref":"Ephesians 5:14 (NIV)",
 "bigidea":"God is not honored by His people sleepwalking through the one life He gave them. He came to wake the dead \u2014 and that includes the quietly numb.",
 "tags":["Vitality","Awake","Wonder","Purpose","Aliveness"],
 "best_for":"Church &amp; Company","backbone":"Ephesians 5:14; Romans 6:11","metaphor":"Waking Up","felt":"Vitality, aliveness, waking from numbness",
 "sessions":[
   ("1","Awake but Asleep","Recognizing the quiet deadness we\u2019ve called normal."),
   ("2","Wake Up, Sleeper","God\u2019s loving call out of spiritual slumber."),
   ("3","Alive to God","Becoming responsive to His presence again."),
   ("4","Recovering Wonder","Letting awe back into an ordinary life."),
   ("5","Alive to Purpose","Waking up to why you\u2019re here."),
   ("6","Fully Alive","Living vivid, awake, and present \u2014 for good."),
 ],
 "journey":"Each of the 40 days offers one small way to wake up \u2014 a moment of wonder, presence, or purpose \u2014 with a partner check-in and a prayer, until aliveness replaces autopilot.",
 "why":"The opposite of the abundant life often isn\u2019t tragedy \u2014 it\u2019s numbness. And God is in the business of waking the sleeping back to life.",
 "cta":"Launch Living Fully Alive and help your people wake up to the life in front of them.",
 "note":None,
},
{
 "num":"04","accent":"#2f6b4f","accent_soft":"#d8e8df",
 "title_a":"The Abundant","title_b":"Life",
 "subtitle":"Discovering what a truly rich life actually looks like",
 "problem":"We\u2019re handed a counterfeit version of the abundant life from the moment we\u2019re born \u2014 more money, more success, more comfort, more stuff. Many chase it for decades and arrive empty, having confused the good life with the full one. The real abundant life is richer, and more available, than the imitation we\u2019ve been sold.",
 "promise":"The Abundant Life redraws the picture. Over forty days your people trade the culture\u2019s counterfeit for the genuine article \u2014 the shepherded life of Psalm 23, marked by provision, rest, guidance, presence, and an overflowing cup \u2014 and learn to recognize and receive the true riches God freely gives.",
 "verse":"The Lord is my shepherd, I lack nothing.",
 "ref":"Psalm 23:1 (NIV)",
 "bigidea":"The abundant life was never about having more. It\u2019s about lacking nothing that truly matters \u2014 provision, peace, purpose, presence \u2014 the riches the world can\u2019t sell and can\u2019t take.",
 "tags":["True Riches","Contentment","Peace","Presence","The Good Life"],
 "best_for":"Church &amp; Company","backbone":"Psalm 23; Luke 12:15","metaphor":"Green Pastures","felt":"Redefining the good life, marks of abundance",
 "sessions":[
   ("1","The Counterfeit","The hollow version of abundance we\u2019ve all been sold."),
   ("2","I Lack Nothing","The startling claim at the heart of Psalm 23."),
   ("3","Green Pastures, Still Waters","Rediscovering rest as part of the rich life."),
   ("4","Guided and Provided For","Living under the care of a good Shepherd."),
   ("5","An Overflowing Cup","Recognizing the abundance already in your life."),
   ("6","The Truly Good Life","Stepping into riches the world can\u2019t give."),
 ],
 "journey":"Each of the 40 days names one true riches already present in your people\u2019s lives and one counterfeit to release, with a partner check-in and a prayer.",
 "why":"Many spend their whole lives chasing an abundance that was never real, while the genuine article sits unnoticed. This campaign helps them finally see it.",
 "cta":"Launch The Abundant Life and help your people find the riches that last.",
 "note":None,
},
{
 "num":"05","accent":"#5d4b8a","accent_soft":"#e3def0",
 "title_a":"More Than","title_b":"Enough",
 "subtitle":"Trusting the God whose provision always exceeds the need",
 "problem":"Many of us relate to God as if He\u2019s just barely enough \u2014 stretched thin, rationing His blessings, likely to run short if we ask for too much. So we approach Him timidly, brace for lack, and live with a quiet anxiety that there won\u2019t be enough to go around. But that is simply not the God the Bible describes.",
 "promise":"More Than Enough enlarges your people\u2019s view of God. Over forty days they\u2019ll move from a barely-enough faith to confidence in a God of immeasurable abundance \u2014 One able to do far more than they ask or imagine \u2014 and learn to live, ask, and give from that overflowing sufficiency.",
 "verse":"\u2026able to do immeasurably more than all we ask or imagine.",
 "ref":"Ephesians 3:20 (NIV)",
 "bigidea":"God is not a barely-enough God. He is a more-than-enough God \u2014 able to do immeasurably more than you ask or imagine. Most of us are simply asking far too small.",
 "tags":["Provision","Sufficiency","Immeasurably More","Trust","Confidence"],
 "best_for":"Church &amp; Company","backbone":"Ephesians 3:20; 2 Cor 9:8","metaphor":"Immeasurably More","felt":"Sufficiency, provision, beyond scarcity",
 "sessions":[
   ("1","The Barely-Enough God","The small view of God we never meant to hold."),
   ("2","Immeasurably More","What Paul believed God was able to do."),
   ("3","Twelve Baskets Left Over","A God who provides past the point of need."),
   ("4","Asking Too Small","Enlarging our prayers to match His capacity."),
   ("5","Living from Sufficiency","Trading anxiety for confident trust."),
   ("6","More Than Enough","Resting in a God who never runs short."),
 ],
 "journey":"Each of the 40 days replaces one barely-enough fear with one truth about God\u2019s more-than-enough provision and one bold, expectant prayer, with a partner check-in.",
 "why":"People shrink their lives to fit a small view of God. Enlarge their picture of His sufficiency, and watch their faith, their asking, and their living expand.",
 "cta":"Launch More Than Enough and help your people trust a more-than-enough God.",
 "note":None,
},
]

for _c in campaigns:
    _c["category"] = "Abundance"
    _c["tier"] = "Tier 2"
    _c["audience"] = "Church + Company"

cover = """
<div class="page cover">
  <div class="frame gold"></div>
  <div class="cover-inner">
    <div class="brandmark">Lifetogether</div>
    <div class="kicker">The Campaign Library &nbsp;&middot;&nbsp; Abundance Collection</div>
    <div class="cover-rule"></div>
    <h1>The <em>Abundance</em><br>Collection</h1>
    <div class="sub">Five forty-day campaigns to help your people step out of scarcity and into the full, overflowing, fruitful life God has always intended for them.</div>
    <div class="cover-foot">
      <div class="stats">
        <div class="stat"><div class="n">5</div><div class="l">Campaigns</div></div>
        <div class="stat"><div class="n">40</div><div class="l">Day Journey</div></div>
        <div class="stat"><div class="n">6</div><div class="l">Sessions Each</div></div>
        <div class="stat"><div class="n">NIV</div><div class="l">Scripture</div></div>
      </div>
      <div class="tier">Tier 2 &nbsp;&middot;&nbsp; Overflow &amp; Fruitfulness &nbsp;&middot;&nbsp; For Churches &amp; Companies</div>
    </div>
  </div>
</div>"""

intro = """
<div class="page intro">
  <div class="frame"></div>
  <div class="intro-inner">
    <div class="kicker">Before You Begin</div>
    <h2>You were made for more<br>than <em>barely getting by</em>.</h2>
    <p class="lead">Jesus drew a sharp contrast: a thief who comes to steal, kill, and destroy \u2014 and a Savior who came so we could have life to the full. Yet so many believers live somewhere far below that line: depleted, cautious, asleep, bracing for lack. <strong>The Abundance Collection is built to change that.</strong> Five distinct, forty-day journeys move your people out of scarcity and into the overflowing, fruitful, fully alive life God always intended.</p>
    <div class="howrow">
      <div class="howcard"><div class="hn">40</div><h4>A Daily Rhythm</h4><p>Every day offers a short reading, one practical step, a spiritual-partner check-in, and a written prayer &mdash; small, repeatable, and easy to keep.</p></div>
      <div class="howcard"><div class="hn">6</div><h4>A Weekly Gathering</h4><p>Six group sessions give the journey its backbone, turning private renewal into shared momentum across your church or team.</p></div>
      <div class="howcard"><div class="hn">1</div><h4>A Clear Outcome</h4><p>Each campaign is built around one transformation &mdash; so your people don\u2019t just read about the abundant life, they begin to live it.</p></div>
    </div>
    <div class="contents">
      <div class="ct">Inside This Collection</div>
      <div class="clist">
        <div class="cli"><span class="cnum">01</span><span><span class="cnm">Abundance</span><br><span class="cds">Step into the full life Jesus gives</span></span></div>
        <div class="cli"><span class="cnum">02</span><span><span class="cnm">Overflow</span><br><span class="cds">Let God\u2019s fullness spill into everything</span></span></div>
        <div class="cli"><span class="cnum">03</span><span><span class="cnm">Living Fully Alive</span><br><span class="cds">Wake up from numbness to vitality</span></span></div>
        <div class="cli"><span class="cnum">04</span><span><span class="cnm">The Abundant Life</span><br><span class="cds">Find the riches that actually last</span></span></div>
        <div class="cli"><span class="cnum">05</span><span><span class="cnm">More Than Enough</span><br><span class="cds">Trust a God who never runs short</span></span></div>
      </div>
    </div>
  </div>
</div>"""

closing = """
<div class="page close">
  <div class="frame"></div>
  <div class="close-inner">
    <div class="kicker">Ready When You Are</div>
    <h2>Help your people<br>live <em>full</em>.</h2>
    <p class="cp">From the first glimpse of God\u2019s abundant heart to a life that overflows, these five campaigns lead your people out of scarcity and into the full, fruitful, fully alive life Jesus came to give. Choose where your church or team is ready to grow, or journey through all five across a season.</p>
    <div class="close-list">
      <div class="cl-row"><span class="cln">01</span><span class="clt">Abundance</span><span class="cld">Life to the full</span></div>
      <div class="cl-row"><span class="cln">02</span><span class="clt">Overflow</span><span class="cld">Rivers of living water</span></div>
      <div class="cl-row"><span class="cln">03</span><span class="clt">Living Fully Alive</span><span class="cld">Waking up</span></div>
      <div class="cl-row"><span class="cln">04</span><span class="clt">The Abundant Life</span><span class="cld">Green pastures</span></div>
      <div class="cl-row"><span class="cln">05</span><span class="clt">More Than Enough</span><span class="cld">Immeasurably more</span></div>
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
<title>The Abundance Collection \u2014 Lifetogether</title>
<style>{FONTS}</style>
<style>{CSS}</style>
</head><body>{pages}</body></html>"""

pathlib.Path("/tmp/abundance.html").write_text(doc, encoding="utf-8")
print("HTML written:", len(doc), "chars")
