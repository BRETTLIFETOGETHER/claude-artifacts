# -*- coding: utf-8 -*-
import pathlib
from brochure_template import FONTS, CSS, campaign_page

campaigns = [
{
 "num":"01","accent":"#2e7d6b","accent_soft":"#d4eae5",
 "title_a":"Generous","title_b":"Living",
 "subtitle":"Generosity not as an act, but as a way of life",
 "problem":"We instinctively treat money and resources like a reservoir \u2014 something to dam up, guard, and slowly accumulate, as if security comes from how much we can hold. But reservoirs, left to themselves, grow stagnant. And a life organized around keeping rarely produces the joy it quietly promises.",
 "promise":"Generous Living offers a different design entirely: a life that flows. Over forty days your people learn to live as conduits rather than containers \u2014 letting God\u2019s provision move through them to others \u2014 and discover the strange math of the kingdom, where the refreshed are those who refresh.",
 "verse":"A generous person will prosper; whoever refreshes others will be refreshed.",
 "ref":"Proverbs 11:25 (NIV)",
 "bigidea":"Generosity isn\u2019t something you do; it\u2019s someone you become. The generous life is a river, not a reservoir \u2014 and rivers are the only water that stays fresh.",
 "tags":["Lifestyle","Generosity","Joy","Flow","Impact"],
 "best_for":"Church &amp; Company","backbone":"Proverbs 11:24\u201325; Luke 6:38","metaphor":"The River, Not the Reservoir","felt":"Lifestyle giving, flow, impact",
 "sessions":[
   ("1","Reservoir or River?","Two very different ways to relate to everything you have."),
   ("2","The Stagnation of Keeping","Why a life built on holding quietly goes stale."),
   ("3","Becoming a Conduit","Letting God\u2019s provision flow through you to others."),
   ("4","The Kingdom\u2019s Strange Math","How giving leads to gaining and keeping leads to losing."),
   ("5","Refreshed by Refreshing","Discovering the joy that only generosity unlocks."),
   ("6","A Generous Life","Living, for good, as a river rather than a reservoir."),
 ],
 "journey":"Each of the 40 days offers one small way to let something flow through you \u2014 a dollar, an hour, a kindness \u2014 plus a partner check-in and a prayer, until generosity becomes your default.",
 "why":"The people most weighed down by money are rarely the ones who give it away. Generous living is lighter, freer, and quietly happier.",
 "cta":"Launch Generous Living and help your people become rivers, not reservoirs.",
 "note":None,
},
{
 "num":"02","accent":"#b8902f","accent_soft":"#f1e8cd",
 "title_a":"Open","title_b":"Hands",
 "subtitle":"The cheerful heart behind every open-handed gift",
 "problem":"Plenty of us give \u2014 but we give with a closed heart even when our hands are open. We give reluctantly, out of guilt or pressure, calculating the minimum, half-resenting the ask. And giving like that, Scripture suggests, misses almost the entire point of generosity.",
 "promise":"Open Hands is about the heart behind the gift. Over forty days your people move from reluctant, pressured giving to the cheerful, freehearted generosity God actually delights in \u2014 discovering the sow-and-reap rhythm of His economy and the deep gladness of giving on purpose.",
 "verse":"Each of you should give what you have decided in your heart to give\u2026 for God loves a cheerful giver.",
 "ref":"2 Corinthians 9:7 (NIV)",
 "bigidea":"God isn\u2019t only interested in what leaves your hand. He\u2019s interested in what\u2019s happening in your heart while it does. The open hand and the cheerful heart belong together.",
 "tags":["Cheerful Giving","Heart","Sow &amp; Reap","Joy","Freedom"],
 "best_for":"Church &amp; Company","backbone":"2 Corinthians 9:6\u20138; Luke 6:38","metaphor":"The Cheerful Open Hand","felt":"Cheerful giving, heart posture",
 "sessions":[
   ("1","The Reluctant Giver","Why grudging generosity misses the point entirely."),
   ("2","A Cheerful Heart","The kind of giver God actually loves."),
   ("3","Sow and Reap","Understanding the rhythm of God\u2019s economy."),
   ("4","Decided in the Heart","Moving from impulse and pressure to intentional giving."),
   ("5","No Strings Attached","Giving freely, without expecting a return."),
   ("6","The Glad Hand","Living with a heart as open as your hand."),
 ],
 "journey":"Each of the 40 days invites one act of cheerful, decided giving and a quick heart-check on the motive behind it, with a partner check-in and a prayer.",
 "why":"You can give a fortune and gain nothing if your heart stays closed. Open hands begin with an open heart.",
 "cta":"Launch Open Hands and help your people become the cheerful givers God delights in.",
 "note":None,
},
{
 "num":"03","accent":"#c14d33","accent_soft":"#f5ddd2",
 "title_a":"Crazy","title_b":"Generosity",
 "subtitle":"The extravagant giving the world calls foolish and heaven calls beautiful",
 "problem":"Most of our giving is safe, sensible, and small \u2014 calculated to be generous enough to feel good but never enough to feel it. But the generosity Scripture celebrates is almost reckless: the widow\u2019s last coins, the broken jar of perfume, churches in deep poverty begging for the privilege of giving beyond their means.",
 "promise":"Crazy Generosity dares your people past sensible. Over forty days they\u2019re invited into the kind of extravagant, joyful, faith-filled giving the world calls foolish and heaven calls beautiful \u2014 the giving that changes the giver as much as the gift changes the world.",
 "verse":"They gave as much as they were able, and even beyond their ability.",
 "ref":"2 Corinthians 8:3 (NIV)",
 "bigidea":"Sensible generosity rarely changes anyone. It\u2019s the \u201ccrazy\u201d gift \u2014 the one that costs, that surprises, that makes no financial sense \u2014 that breaks something open in us and in the world.",
 "tags":["Radical","Sacrificial","Extravagant","Faith","Impact"],
 "best_for":"Church &amp; Company","backbone":"2 Corinthians 8:1\u20135; Mark 12:41\u201344","metaphor":"Beyond Their Ability","felt":"Radical generosity, sacrifice",
 "sessions":[
   ("1","The Trouble with Sensible","Why safe giving rarely changes anything."),
   ("2","Beyond Their Ability","The reckless generosity of the Macedonian church."),
   ("3","The Widow\u2019s Everything","When the smallest gift turns out to be the largest."),
   ("4","Breaking the Jar","Extravagance that looks like waste and is actually worship."),
   ("5","The Joy of Going Too Far","Why over-the-top giving produces over-the-top joy."),
   ("6","A Crazy-Generous Church","Becoming a people known for giving beyond reason."),
 ],
 "journey":"Each of the 40 days stretches generosity one notch past comfortable and offers one bold, joyful step, with a partner check-in and a prayer.",
 "why":"No one is changed by the gift they barely noticed giving. It\u2019s the generosity that costs something that sets us free.",
 "cta":"Launch Crazy Generosity and help your people give in ways the world won\u2019t understand.",
 "note":None,
},
{
 "num":"04","accent":"#9c4a6a","accent_soft":"#f0dce4",
 "title_a":"Living","title_b":"Generously",
 "subtitle":"Being generous with everything \u2014 not just money",
 "problem":"When we hear \u201cgenerosity,\u201d we almost always think money. But some of the stingiest people are generous with their checkbooks and miserly with everything else \u2014 their time, their patience, their praise, their forgiveness, their welcome. True generosity turns out to be far bigger than what\u2019s in our wallets.",
 "promise":"Living Generously expands the whole idea. Over forty days your people learn to be generous in everything \u2014 with their time, their words, their hospitality, their grace, their encouragement \u2014 until generosity becomes not just something they fund, but the way they treat every person they meet.",
 "verse":"Give, and it will be given to you. A good measure, pressed down, shaken together and running over.",
 "ref":"Luke 6:38 (NIV)",
 "bigidea":"Generosity was never meant to stop at money. The most generous people give freely with their time, their words, and their grace \u2014 everything they have, not just everything in their account.",
 "tags":["Time","Words","Hospitality","Grace","Generous Spirit"],
 "best_for":"Church &amp; Company","backbone":"Luke 6:38; Romans 12:13","metaphor":"Generous in Everything","felt":"Everyday generosity, beyond money",
 "sessions":[
   ("1","More Than Money","Why generosity is far bigger than your bank account."),
   ("2","Generous with Time","Giving people the gift of your unhurried presence."),
   ("3","Generous with Words","Becoming lavish with encouragement and praise."),
   ("4","Generous with Grace","Forgiving freely and assuming the best."),
   ("5","Generous with Welcome","Opening your table and your home."),
   ("6","A Generous Way of Life","Treating everyone you meet with open-handed kindness."),
 ],
 "journey":"Each of the 40 days names one non-financial way to be generous \u2014 a word, an hour, a welcome, a second chance \u2014 and invites your people to give it, with a partner check-in and a prayer.",
 "why":"People may forget what you funded, but they never forget how generously you treated them. This is a generosity everyone can practice, today.",
 "cta":"Launch Living Generously and help your people be generous with everything, not just money.",
 "note":None,
},
{
 "num":"05","accent":"#2f5a9e","accent_soft":"#d9e2f1",
 "title_a":"Courageous","title_b":"Generosity",
 "subtitle":"Giving boldly, before you feel ready, and trusting God",
 "problem":"For many of us, the real barrier to generosity isn\u2019t selfishness \u2014 it\u2019s fear. Fear that there won\u2019t be enough. Fear of the future. Fear of giving and regretting it. So we hold back, give cautiously, and wait for a financial security that never quite seems to arrive.",
 "promise":"Courageous Generosity confronts that fear with faith. Over forty days your people learn to give before they feel ready \u2014 to take Scripture\u2019s startling invitation to test God\u2019s faithfulness \u2014 and discover that the God who multiplied a widow\u2019s last meal can be trusted with their generosity too.",
 "verse":"Test me in this\u2026 and see if I will not throw open the floodgates of heaven.",
 "ref":"Malachi 3:10 (NIV)",
 "bigidea":"Generosity almost always requires courage, because it almost always comes before certainty. Faith gives first and trusts God for the rest.",
 "tags":["Courage","Faith","Provision","Trust","First Fruits"],
 "best_for":"Church &amp; Company","backbone":"Malachi 3:10; 1 Kings 17:8\u201316","metaphor":"Giving Before You\u2019re Ready","felt":"Courage, faith, overcoming fear in giving",
 "sessions":[
   ("1","The Fear Beneath the Wallet","Naming what really keeps us from giving."),
   ("2","The Widow\u2019s Last Meal","When giving from your lack becomes a miracle."),
   ("3","Test Me in This","Scripture\u2019s bold invitation to trust God\u2019s provision."),
   ("4","First, Not Last","Why generosity belongs at the front of the budget, not the leftovers."),
   ("5","Giving Before You\u2019re Ready","The courage to give ahead of certainty."),
   ("6","The God Who Provides","Building unshakable confidence in His faithfulness."),
 ],
 "journey":"Each of the 40 days pairs one fear to face with one courageous act of giving, plus a partner check-in and a prayer \u2014 small steps of faith that, over six weeks, break fear\u2019s grip on generosity.",
 "why":"The most generous gift you\u2019ll ever give is almost always the one that scared you. Courage is where generosity becomes faith.",
 "cta":"Launch Courageous Generosity and help your people give boldly and trust deeply.",
 "note":None,
},
]

cover = """
<div class="page cover">
  <div class="frame gold"></div>
  <div class="cover-inner">
    <div class="brandmark">Lifetogether</div>
    <div class="kicker">The Campaign Library &nbsp;&middot;&nbsp; Generosity Collection</div>
    <div class="cover-rule"></div>
    <h1>The <em>Generosity</em><br>Collection</h1>
    <div class="sub">Five forty-day campaigns to move your people from holding back to giving freely \u2014 into open-handed, joyful, courageous generosity that changes them and the world around them.</div>
    <div class="cover-foot">
      <div class="stats">
        <div class="stat"><div class="n">5</div><div class="l">Campaigns</div></div>
        <div class="stat"><div class="n">40</div><div class="l">Day Journey</div></div>
        <div class="stat"><div class="n">6</div><div class="l">Sessions Each</div></div>
        <div class="stat"><div class="n">NIV</div><div class="l">Scripture</div></div>
      </div>
      <div class="tier">Tier 1 &nbsp;&middot;&nbsp; Giving &amp; Open Hands &nbsp;&middot;&nbsp; For Churches &amp; Companies</div>
    </div>
  </div>
</div>"""

intro = """
<div class="page intro">
  <div class="frame"></div>
  <div class="intro-inner">
    <div class="kicker">Before You Begin</div>
    <h2>No one ever gave their way<br>into <em>regret</em>.</h2>
    <p class="lead">Ask anyone who has learned to give freely and they\u2019ll tell you the same thing: generosity is the most joyful risk they ever took. Yet for most of us, an instinct to grip quietly wins \u2014 and we miss the freedom and gladness God designed giving to produce. <strong>The Generosity Collection is built to change that.</strong> Five distinct, forty-day journeys move your people from holding back to giving freely \u2014 in their hearts, their habits, and their whole way of life.</p>
    <div class="howrow">
      <div class="howcard"><div class="hn">40</div><h4>A Daily Rhythm</h4><p>Every day offers a short reading, one practical step, a spiritual-partner check-in, and a written prayer &mdash; small, repeatable, and easy to keep.</p></div>
      <div class="howcard"><div class="hn">6</div><h4>A Weekly Gathering</h4><p>Six group sessions give the journey its backbone, turning private change into shared momentum across your church or team.</p></div>
      <div class="howcard"><div class="hn">1</div><h4>A Clear Outcome</h4><p>Each campaign is built around one transformation &mdash; so your people don\u2019t just admire generosity, they actually begin to live it.</p></div>
    </div>
    <div class="contents">
      <div class="ct">Inside This Collection</div>
      <div class="clist">
        <div class="cli"><span class="cnum">01</span><span><span class="cnm">Generous Living</span><br><span class="cds">Make generosity a whole way of life</span></span></div>
        <div class="cli"><span class="cnum">02</span><span><span class="cnm">Open Hands</span><br><span class="cds">Become the cheerful giver God loves</span></span></div>
        <div class="cli"><span class="cnum">03</span><span><span class="cnm">Crazy Generosity</span><br><span class="cds">Dare to give past sensible</span></span></div>
        <div class="cli"><span class="cnum">04</span><span><span class="cnm">Living Generously</span><br><span class="cds">Be generous with everything, not just money</span></span></div>
        <div class="cli"><span class="cnum">05</span><span><span class="cnm">Courageous Generosity</span><br><span class="cds">Give boldly and trust God</span></span></div>
      </div>
    </div>
  </div>
</div>"""

closing = """
<div class="page close">
  <div class="frame"></div>
  <div class="close-inner">
    <div class="kicker">Ready When You Are</div>
    <h2>Help your people discover<br>the joy of <em>giving</em>.</h2>
    <p class="cp">From an open heart to a courageous gift, these five campaigns walk your people into a generosity that genuinely changes them \u2014 lighter, freer, and more joyful than the gripping life they leave behind. Choose where your church or team is ready to grow, or journey through all five across a season.</p>
    <div class="close-list">
      <div class="cl-row"><span class="cln">01</span><span class="clt">Generous Living</span><span class="cld">River, not reservoir</span></div>
      <div class="cl-row"><span class="cln">02</span><span class="clt">Open Hands</span><span class="cld">The cheerful giver</span></div>
      <div class="cl-row"><span class="cln">03</span><span class="clt">Crazy Generosity</span><span class="cld">Past sensible</span></div>
      <div class="cl-row"><span class="cln">04</span><span class="clt">Living Generously</span><span class="cld">Generous in everything</span></div>
      <div class="cl-row"><span class="cln">05</span><span class="clt">Courageous Generosity</span><span class="cld">Give boldly</span></div>
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
<title>The Generosity Collection \u2014 Lifetogether</title>
<style>{FONTS}</style>
<style>{CSS}</style>
</head><body>{pages}</body></html>"""

pathlib.Path("/tmp/generosity.html").write_text(doc, encoding="utf-8")
print("HTML written:", len(doc), "chars")
