# -*- coding: utf-8 -*-
import pathlib
from brochure_template import FONTS, CSS, campaign_page

campaigns = [
{
 "num":"06","accent":"#5b4a86","accent_soft":"#e3def0",
 "title_a":"Kingdom","title_b":"Overflow",
 "subtitle":"When seeking God\u2019s kingdom first unlocks a life that overflows",
 "problem":"We tend to pursue abundance for ourselves \u2014 a fuller life, more margin, more blessing \u2014 and then wonder why it so often feels hollow. We\u2019ve reversed the order Jesus gave. He never told us to chase abundance and hope the kingdom follows; He told us to seek the kingdom first, and promised the rest would be added.",
 "promise":"Kingdom Overflow restores the order. Over forty days your people learn to put God\u2019s kingdom first \u2014 and discover that the abundance which follows isn\u2019t meant to terminate on them but to overflow back into His mission, blessing a world far beyond themselves.",
 "verse":"But seek first his kingdom and his righteousness, and all these things will be given to you as well.",
 "ref":"Matthew 6:33 (NIV)",
 "bigidea":"Seek abundance and you\u2019ll miss it. Seek the kingdom first, and abundance comes \u2014 not to be hoarded, but to overflow into the very mission you put first.",
 "tags":["Kingdom","Mission","Overflow","Blessing","Purpose"],
 "best_for":"Church &amp; Company","backbone":"Matthew 6:33; 2 Corinthians 9:8","metaphor":"Kingdom First","felt":"Kingdom impact, abundance for mission",
 "sessions":[
   ("1","The Reversed Order","Why chasing abundance directly leaves us empty."),
   ("2","Seek First","The priority Jesus promised would change everything."),
   ("3","And All These Things","Trusting the provision that follows the kingdom."),
   ("4","Overflow with a Mission","Abundance aimed beyond ourselves."),
   ("5","Blessed to Build","Letting your fullness serve God\u2019s purposes."),
   ("6","A Kingdom That Overflows","Joining what God is doing in the world."),
 ],
 "journey":"Each of the 40 days takes one way to seek the kingdom first and one way to let the resulting abundance overflow outward, with a partner check-in and a prayer.",
 "why":"The abundant life was never the destination \u2014 the kingdom is. And those who seek it first end up with both.",
 "cta":"Launch Kingdom Overflow and help your people seek first and overflow outward.",
 "note":None,
},
{
 "num":"07","accent":"#3f8559","accent_soft":"#dceae0",
 "title_a":"Flourishing","title_b":"in Christ",
 "subtitle":"Becoming deeply rooted so you naturally thrive and bear fruit",
 "problem":"We treat flourishing like an achievement \u2014 something to strive for, hustle toward, and manufacture by effort. So we push harder and grow more tired, wondering why thriving stays just out of reach. But Scripture pictures flourishing as something that happens almost on its own \u2014 to a tree planted in the right place.",
 "promise":"Flourishing in Christ shifts the focus from striving to rootedness. Over forty days your people learn what it means to be deeply planted in Christ \u2014 like a tree by streams of water \u2014 so that fruitfulness, resilience, and genuine thriving become the natural overflow of where they\u2019re rooted.",
 "verse":"That person is like a tree planted by streams of water, which yields its fruit in season.",
 "ref":"Psalm 1:3 (NIV)",
 "bigidea":"You don\u2019t flourish by trying harder; you flourish by being rooted in the right place. A tree planted by water doesn\u2019t strain to bear fruit \u2014 it simply does.",
 "tags":["Flourishing","Rootedness","Fruitfulness","Thriving","Resilience"],
 "best_for":"Church &amp; Company","backbone":"Psalm 1:1\u20133; John 15:5","metaphor":"A Tree by Streams of Water","felt":"Flourishing, fruitfulness, rootedness",
 "sessions":[
   ("1","The Striving Trap","Why hustling toward flourishing leaves us dry."),
   ("2","Planted by the Water","The quiet secret of the flourishing tree."),
   ("3","Roots Before Fruit","Going deep with Christ before going far."),
   ("4","Fruit in Season","Trusting God\u2019s timing for your thriving."),
   ("5","Leaves That Don\u2019t Wither","Resilience that outlasts the dry seasons."),
   ("6","A Flourishing Life","Thriving as the natural overflow of rootedness."),
 ],
 "journey":"Each of the 40 days deepens one root \u2014 a practice that connects your people to Christ \u2014 and notices one bit of fruit, with a partner check-in and a prayer.",
 "why":"Tired, striving people don\u2019t need to try harder to flourish. They need to be planted deeper. Rootedness is the whole secret.",
 "cta":"Launch Flourishing in Christ and help your people thrive from the roots up.",
 "note":None,
},
{
 "num":"08","accent":"#bb5a78","accent_soft":"#f3dce5",
 "title_a":"Abundant","title_b":"Grace",
 "subtitle":"Living from the lavish, never-ending grace of God",
 "problem":"Many believers quietly live as if grace were rationed \u2014 a limited supply they\u2019re slowly using up, doled out in proportion to their performance. So they strive to earn what they already have, brace for God\u2019s disappointment, and miss the staggering truth at the center of the gospel: God\u2019s grace isn\u2019t scarce. It\u2019s lavish, and it never runs out.",
 "promise":"Abundant Grace immerses your people in the inexhaustible. Over forty days they\u2019ll move from a scarcity of grace \u2014 striving, earning, fearing they\u2019ve used it up \u2014 into the freedom of grace upon grace, receiving from a fullness that simply keeps on giving.",
 "verse":"Out of his fullness we have all received grace in place of grace already given.",
 "ref":"John 1:16 (NIV)",
 "bigidea":"Grace isn\u2019t a limited supply you\u2019re using up \u2014 it\u2019s grace upon grace, poured from a fullness that never empties. You can stop rationing what God lavishes.",
 "tags":["Grace","Lavish Love","Freedom","The Gospel","Rest"],
 "best_for":"Church &amp; Company","backbone":"John 1:16; Ephesians 1:7\u20138","metaphor":"Grace Upon Grace","felt":"Grace, lavish love, freedom from earning",
 "sessions":[
   ("1","Rationing Grace","The scarcity mindset that creeps into the gospel."),
   ("2","Grace Upon Grace","The endless supply John described."),
   ("3","The End of Earning","Receiving what you could never deserve."),
   ("4","Lavished, Not Doled","How extravagantly God actually gives."),
   ("5","Grace for the Failures","Why grace meets you exactly where you fall."),
   ("6","Living from Fullness","Resting in a grace that never runs out."),
 ],
 "journey":"Each of the 40 days replaces one effort to earn with one act of receiving grace, with a partner check-in and a prayer \u2014 retraining the heart to live from fullness, not lack.",
 "why":"Striving, exhausted believers are almost always living from a scarcity of grace they don\u2019t actually have. Show them the abundance, and everything changes.",
 "cta":"Launch Abundant Grace and help your people live from grace upon grace.",
 "note":None,
},
{
 "num":"09","accent":"#2d7a8a","accent_soft":"#d6e9ed",
 "title_a":"Living with","title_b":"Open Hands",
 "subtitle":"Open to receive all God gives, open to release it freely",
 "problem":"The clenched fist is our default. We grip what we have out of fear, and we close off from what God wants to give out of doubt. But a closed hand can do neither of the two things abundance requires: it can\u2019t receive what\u2019s being offered, and it can\u2019t release what\u2019s been given. The grip we think protects us actually shuts us out.",
 "promise":"Living with Open Hands trains a new posture. Over forty days your people learn to live with hands open in both directions \u2014 open to receive everything God longs to pour into their lives, and open to release it freely to others \u2014 discovering the unguarded freedom that abundance was always meant to bring.",
 "verse":"Freely you have received; freely give.",
 "ref":"Matthew 10:8 (NIV)",
 "bigidea":"The same open hand that receives is the one that gives. Clench it, and you lose both. Abundance flows only through hands held open in both directions.",
 "tags":["Open Hands","Receiving","Releasing","Trust","Freedom"],
 "best_for":"Church &amp; Company","backbone":"Matthew 10:8; Ecclesiastes 5:19","metaphor":"Open to Receive, Open to Release","felt":"Open-handedness, receiving and releasing",
 "sessions":[
   ("1","The Default Fist","Why we instinctively grip and close off."),
   ("2","Open to Receive","Letting God give you more than you\u2019ll allow."),
   ("3","Open to Release","Holding what you have loosely enough to share."),
   ("4","Freely Received","Remembering everything you hold was a gift."),
   ("5","The Unguarded Life","The freedom of hands that no longer clench."),
   ("6","Open-Handed for Good","Living ready to receive and to give."),
 ],
 "journey":"Each of the 40 days invites one open-handed act \u2014 receiving a gift gratefully or releasing one freely \u2014 with a partner check-in and a prayer, until open hands become your people\u2019s natural posture.",
 "why":"Abundance can\u2019t flow through a closed fist. Teach your people to open their hands, and both blessing and contentment start moving again.",
 "cta":"Launch Living with Open Hands and help your people receive and release freely.",
 "note":None,
},
{
 "num":"10","accent":"#d08a1f","accent_soft":"#f7e7c6",
 "title_a":"Overflowing","title_b":"Joy",
 "subtitle":"The deep, full gladness that overflows from a life in Christ",
 "problem":"Most of us settle for happiness \u2014 a mood that rises and falls with our circumstances, here on the good days and gone on the hard ones. And when joy feels absent, we assume we simply need things to go better. But the joy Jesus offers doesn\u2019t depend on circumstances at all. It\u2019s deeper, steadier, and meant to overflow.",
 "promise":"Overflowing Joy leads your people to the real thing. Over forty days they\u2019ll discover the difference between fragile happiness and the full, durable joy Jesus promised \u2014 a gladness rooted in His presence rather than their circumstances \u2014 and learn to live so full of it that it spills over onto everyone around them.",
 "verse":"\u2026that my joy may be in you and that your joy may be complete.",
 "ref":"John 15:11 (NIV)",
 "bigidea":"Happiness depends on what\u2019s happening; joy depends on Who\u2019s present. The joy Jesus gives doesn\u2019t rise and fall with your circumstances \u2014 it overflows in spite of them.",
 "tags":["Joy","Gladness","Fullness","Presence","Overflow"],
 "best_for":"Church &amp; Company","backbone":"John 15:11; Psalm 16:11","metaphor":"Joy Made Complete","felt":"Joy, gladness, the overflow of joy",
 "sessions":[
   ("1","Happiness Isn\u2019t Joy","The crucial difference most of us miss."),
   ("2","Joy Made Complete","The full gladness Jesus promised His followers."),
   ("3","Joy in His Presence","Where lasting joy is actually found."),
   ("4","Joy Through the Hard","Why real joy survives difficult seasons."),
   ("5","The Overflow of Joy","How a joyful life lifts everyone near it."),
   ("6","A People of Joy","Becoming known for a gladness the world can\u2019t explain."),
 ],
 "journey":"Each of the 40 days names one source of true joy in God\u2019s presence and one way to let it overflow to someone else, with a partner check-in and a prayer.",
 "why":"A joyless faith is one of the poorest advertisements for the abundant life. Restore your people\u2019s joy, and they become living proof of it.",
 "cta":"Launch Overflowing Joy and help your people live full of a joy the world can\u2019t explain.",
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
    <div class="kicker">The Campaign Library &nbsp;&middot;&nbsp; Abundance &nbsp;&middot;&nbsp; Volume Two</div>
    <div class="cover-rule"></div>
    <h1>The <em>Abundance</em><br>Collection</h1>
    <div class="sub">Five more forty-day campaigns that carry abundance outward and upward \u2014 into kingdom impact, flourishing, lavish grace, open-handed living, and overflowing joy.</div>
    <div class="cover-foot">
      <div class="stats">
        <div class="stat"><div class="n">5</div><div class="l">Campaigns</div></div>
        <div class="stat"><div class="n">40</div><div class="l">Day Journey</div></div>
        <div class="stat"><div class="n">6</div><div class="l">Sessions Each</div></div>
        <div class="stat"><div class="n">NIV</div><div class="l">Scripture</div></div>
      </div>
      <div class="tier">Tier 2 &nbsp;&middot;&nbsp; Titles 06\u201310 &nbsp;&middot;&nbsp; For Churches &amp; Companies</div>
    </div>
  </div>
</div>"""

intro = """
<div class="page intro">
  <div class="frame"></div>
  <div class="intro-inner">
    <div class="kicker">Before You Begin</div>
    <h2>Abundance was never meant<br>to stop with <em>you</em>.</h2>
    <p class="lead">Once your people taste the full life God offers, the question becomes what that fullness is <em>for</em>. The answer runs outward and upward \u2014 into God\u2019s kingdom, into deep-rooted flourishing, into the lavish grace that fuels it, into open hands that receive and release, and into a joy that simply overflows. <strong>This second volume follows abundance to its purpose,</strong> with five distinct, forty-day journeys that turn a full life into a life that pours out.</p>
    <div class="howrow">
      <div class="howcard"><div class="hn">40</div><h4>A Daily Rhythm</h4><p>Every day offers a short reading, one practical step, a spiritual-partner check-in, and a written prayer &mdash; small, repeatable, and easy to keep.</p></div>
      <div class="howcard"><div class="hn">6</div><h4>A Weekly Gathering</h4><p>Six group sessions give the journey its backbone, turning private renewal into shared momentum across your church or team.</p></div>
      <div class="howcard"><div class="hn">1</div><h4>A Clear Outcome</h4><p>Each campaign is built around one transformation &mdash; so your people don\u2019t just receive abundance, they begin to overflow with it.</p></div>
    </div>
    <div class="contents">
      <div class="ct">Inside This Volume</div>
      <div class="clist">
        <div class="cli"><span class="cnum">06</span><span><span class="cnm">Kingdom Overflow</span><br><span class="cds">Let abundance flow into God\u2019s mission</span></span></div>
        <div class="cli"><span class="cnum">07</span><span><span class="cnm">Flourishing in Christ</span><br><span class="cds">Thrive from being deeply rooted</span></span></div>
        <div class="cli"><span class="cnum">08</span><span><span class="cnm">Abundant Grace</span><br><span class="cds">Live from grace upon grace</span></span></div>
        <div class="cli"><span class="cnum">09</span><span><span class="cnm">Living with Open Hands</span><br><span class="cds">Receive and release freely</span></span></div>
        <div class="cli"><span class="cnum">10</span><span><span class="cnm">Overflowing Joy</span><br><span class="cds">Overflow with a joy that lasts</span></span></div>
      </div>
    </div>
  </div>
</div>"""

closing = """
<div class="page close">
  <div class="frame"></div>
  <div class="close-inner">
    <div class="kicker">Ready When You Are</div>
    <h2>Help your people<br>overflow with <em>joy</em>.</h2>
    <p class="cp">These five campaigns take the abundant life and turn it outward \u2014 into kingdom impact, deep-rooted flourishing, lavish grace, open-handed freedom, and a joy that spills onto everyone near it. Choose where your church or team is ready to grow, or move through all five across a season.</p>
    <div class="close-list">
      <div class="cl-row"><span class="cln">06</span><span class="clt">Kingdom Overflow</span><span class="cld">Kingdom first</span></div>
      <div class="cl-row"><span class="cln">07</span><span class="clt">Flourishing in Christ</span><span class="cld">Rooted and thriving</span></div>
      <div class="cl-row"><span class="cln">08</span><span class="clt">Abundant Grace</span><span class="cld">Grace upon grace</span></div>
      <div class="cl-row"><span class="cln">09</span><span class="clt">Living with Open Hands</span><span class="cld">Receive and release</span></div>
      <div class="cl-row"><span class="cln">10</span><span class="clt">Overflowing Joy</span><span class="cld">Joy made complete</span></div>
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
<title>The Abundance Collection, Volume Two \u2014 Lifetogether</title>
<style>{FONTS}</style>
<style>{CSS}</style>
</head><body>{pages}</body></html>"""

pathlib.Path("/tmp/abundance_v2.html").write_text(doc, encoding="utf-8")
print("HTML written:", len(doc), "chars")
