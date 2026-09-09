# -*- coding: utf-8 -*-
import pathlib
from brochure_template import FONTS, CSS, campaign_page

campaigns = [
{
 "num":"06","accent":"#2a6e7a","accent_soft":"#d6e7ec",
 "title_a":"Multiplying","title_b":"What Matters",
 "subtitle":"Aiming your multiplying energy at the things that truly last",
 "problem":"Multiplication is powerful \u2014 which is exactly why it\u2019s dangerous when pointed at the wrong things. It\u2019s entirely possible to scale our busyness, grow our platforms, and multiply output that won\u2019t survive the test of time. We can get remarkably good at producing more of what ultimately doesn\u2019t matter.",
 "promise":"Multiplying What Matters brings discernment to the drive. Over forty days your people learn to direct their multiplying energy toward what actually lasts \u2014 building with gold rather than straw \u2014 so that the life they scale is one that will still be standing when everything temporary has burned away.",
 "verse":"\u2026the fire will test the quality of each person\u2019s work.",
 "ref":"1 Corinthians 3:13 (NIV)",
 "bigidea":"Multiplication amplifies whatever you aim it at. The crucial question isn\u2019t whether you\u2019re multiplying \u2014 it\u2019s whether the thing you\u2019re multiplying will last.",
 "tags":["Priorities","What Lasts","Eternal Focus","Discernment","Building Well"],
 "best_for":"Company &amp; Church","backbone":"1 Corinthians 3:11\u201315; Matthew 6:19\u201321","metaphor":"Gold, Not Straw","felt":"Priorities, multiplying the right things",
 "sessions":[
   ("1","Scaling the Wrong Things","How multiplication can amplify what doesn\u2019t matter."),
   ("2","Gold, Silver, Straw","The materials that survive the test \u2014 and the ones that don\u2019t."),
   ("3","What Will Last","Naming the things genuinely worth multiplying."),
   ("4","The Tyranny of More","Why \u2018more\u2019 is a poor goal on its own."),
   ("5","Building to Endure","Investing your multiplying energy in what survives."),
   ("6","A Life That Stands","Multiplying what will still matter in eternity."),
 ],
 "journey":"Each of the 40 days asks one clarifying question \u2014 does this deserve to be multiplied? \u2014 and aims one effort at what truly lasts, with a partner check-in and a prayer.",
 "why":"The most tragic thing isn\u2019t failing to multiply \u2014 it\u2019s succeeding at multiplying the wrong things. Direction matters more than speed.",
 "cta":"Launch Multiplying What Matters and help your people scale what truly lasts.",
 "note":None,
},
{
 "num":"07","accent":"#3a7d4f","accent_soft":"#dcebe0",
 "title_a":"Greater","title_b":"Impact",
 "subtitle":"Bearing more fruit by staying connected to the source",
 "problem":"When we want greater impact, our instinct is to do more \u2014 add activity, increase effort, push harder. But that strategy eventually exhausts us and rarely produces the lasting fruit we hoped for. Jesus pointed to a completely different source of greater impact: not more striving, but deeper connection.",
 "promise":"Greater Impact rewires how your people pursue fruitfulness. Over forty days they\u2019ll learn the secret of the vine \u2014 that abiding produces more than effort ever could, and that even God\u2019s pruning is aimed at greater fruit \u2014 discovering how to bear much fruit without burning out.",
 "verse":"This is to my Father\u2019s glory, that you bear much fruit.",
 "ref":"John 15:8 (NIV)",
 "bigidea":"Greater impact doesn\u2019t come from more striving; it comes from deeper abiding. The most fruitful branches aren\u2019t the busiest \u2014 they\u2019re the most connected.",
 "tags":["Fruitfulness","Abiding","Pruning","Effectiveness","Impact"],
 "best_for":"Company &amp; Church","backbone":"John 15:1\u20138","metaphor":"Pruned for More Fruit","felt":"Greater impact, increased fruitfulness",
 "sessions":[
   ("1","The Striving Ceiling","Why doing more eventually produces less."),
   ("2","Abide for Impact","The connection that fruitfulness actually requires."),
   ("3","Pruned for More","Why God cuts back the fruitful for even greater fruit."),
   ("4","Much Fruit","What Jesus promised the deeply connected life would yield."),
   ("5","Impact Without Burnout","Bearing more without running dry."),
   ("6","A Fruitful Life","Becoming a branch that consistently bears much fruit."),
 ],
 "journey":"Each of the 40 days deepens one connection to Christ and surrenders one thing to His pruning, with a partner check-in and a prayer \u2014 trading striving for abiding.",
 "why":"Driven people chase impact through effort and stall. Connected people bear much fruit almost without trying. The secret is the vine, not the hustle.",
 "cta":"Launch Greater Impact and help your people bear more fruit by abiding deeper.",
 "note":None,
},
{
 "num":"08","accent":"#5b4a86","accent_soft":"#e3def0",
 "title_a":"Exponential","title_b":"Influence",
 "subtitle":"How influence compounds and ripples far beyond you",
 "problem":"We tend to measure our influence in a straight line \u2014 the people we personally reach, the room we\u2019re actually in. Measured that way, most of us conclude our influence is small and stop there. But influence was never designed to move in straight lines. It compounds, rippling from one life to the next in ways we rarely see and routinely underestimate.",
 "promise":"Exponential Influence reveals the compounding nature of a life. Over forty days your people learn how influence spreads in expanding circles \u2014 from those nearest them outward to the ends of the earth \u2014 and how investing in a few can ripple into a reach far beyond anything they could measure.",
 "verse":"\u2026you will be my witnesses in Jerusalem\u2026 and to the ends of the earth.",
 "ref":"Acts 1:8 (NIV)",
 "bigidea":"Influence doesn\u2019t add; it compounds. Pour into the few nearest you, and the ripple moves outward in expanding circles you\u2019ll never fully see.",
 "tags":["Influence","Compounding","Ripple Effect","Reach","Legacy"],
 "best_for":"Company &amp; Church","backbone":"Acts 1:8; 2 Timothy 2:2","metaphor":"Jerusalem to the Ends of the Earth","felt":"Compounding influence, expanding reach",
 "sessions":[
   ("1","Influence in Straight Lines","Why we underestimate our actual reach."),
   ("2","Expanding Circles","How influence moves from Jerusalem outward."),
   ("3","The Power of a Few","Why pouring into a handful reaches multitudes."),
   ("4","The Unseen Ripple","Trusting the reach you\u2019ll never get to measure."),
   ("5","Compounding Over Time","How small influence grows exponentially."),
   ("6","An Influential Life","Living to start ripples that outlast you."),
 ],
 "journey":"Each of the 40 days invests in one person within your reach and trusts God for the ripple, with a partner check-in and a prayer \u2014 building influence that compounds.",
 "why":"Most people quit influencing because they only count the room they\u2019re in. Show them the compounding ripple, and ordinary lives start aiming at the ends of the earth.",
 "cta":"Launch Exponential Influence and help your people start ripples that compound.",
 "note":None,
},
{
 "num":"09","accent":"#b8902f","accent_soft":"#f1e8cd",
 "title_a":"Investing Your","title_b":"Life Well",
 "subtitle":"Spending your one and only life on what yields eternal return",
 "problem":"We carefully invest our money, weighing returns and avoiding waste \u2014 yet we spend our far more valuable and far more limited asset, our actual lives, almost carelessly. Hours, energy, and opportunity slip by unexamined. And a life spent without intention, however busy, can quietly add up to very little.",
 "promise":"Investing Your Life Well brings the discipline of stewardship to your people\u2019s days. Over forty days they\u2019ll learn to treat their time, energy, and opportunities as the precious capital they are \u2014 making the most of every opportunity \u2014 and to invest their one life where it yields the greatest, most lasting return.",
 "verse":"\u2026making the most of every opportunity, because the days are evil.",
 "ref":"Ephesians 5:16 (NIV)",
 "bigidea":"Your life is the single greatest investment you\u2019ll ever manage \u2014 limited, valuable, and impossible to get back. Spend it on purpose, or watch it spend itself.",
 "tags":["Time","Stewardship","Intentionality","No Regrets","Return"],
 "best_for":"Company &amp; Church","backbone":"Ephesians 5:15\u201316; Matthew 25:14\u201330","metaphor":"Making the Most of It","felt":"Investing your life and time well",
 "sessions":[
   ("1","Your Most Valuable Asset","Why your life is worth more than your money."),
   ("2","Making the Most of It","Treating each opportunity as capital to invest."),
   ("3","The Cost of Drift","How an unexamined life quietly adds up to little."),
   ("4","Investing for Return","Spending your days where they yield the most."),
   ("5","A Life Without Regret","Living now the way you\u2019ll wish you had."),
   ("6","Well Invested","Becoming a faithful steward of your one life."),
 ],
 "journey":"Each of the 40 days examines one way your people spend their time and redirects one piece of it toward lasting return, with a partner check-in and a prayer.",
 "why":"No one reaches the end wishing they\u2019d been busier. They wish they\u2019d invested their life more intentionally \u2014 and it\u2019s never too early to start.",
 "cta":"Launch Investing Your Life Well and help your people spend their days on purpose.",
 "note":None,
},
{
 "num":"10","accent":"#9e3b2f","accent_soft":"#f1dcd5",
 "title_a":"Living Beyond","title_b":"Yourself",
 "subtitle":"The paradox that a life poured out is the one that multiplies",
 "problem":"Almost everything in us pulls inward \u2014 toward our own comfort, our own success, our own security and lifetime. It feels like the safe way to protect a life. But Jesus described the opposite: a life clutched tightly stays a single seed, while a life given away produces a harvest. Self-protection is quietly self-limiting.",
 "promise":"Living Beyond Yourself invites your people into the great paradox of multiplication. Over forty days they\u2019ll learn that the life poured out for others and for God\u2019s purposes is the very life that multiplies \u2014 like a grain of wheat that, by falling and dying, produces many seeds.",
 "verse":"\u2026unless a kernel of wheat falls to the ground and dies, it remains only a single seed.",
 "ref":"John 12:24 (NIV)",
 "bigidea":"The self-protected life stays a single seed. The life given away \u2014 beyond your comfort, your gain, your lifetime \u2014 is the one that multiplies into a harvest.",
 "tags":["Selflessness","Significance","Legacy","Surrender","Beyond Self"],
 "best_for":"Company &amp; Church","backbone":"John 12:24\u201326; Philippians 2:3\u20134","metaphor":"The Grain of Wheat","felt":"Living beyond self, significance, legacy",
 "sessions":[
   ("1","The Inward Pull","Naming the self-focus that quietly limits us."),
   ("2","The Grain of Wheat","Jesus\u2019 paradox of dying to multiply."),
   ("3","Success or Significance","Choosing a life that counts beyond yourself."),
   ("4","Poured Out for Others","Finding life by giving it away."),
   ("5","Beyond Your Lifetime","Living for a harvest you may never see."),
   ("6","A Life That Multiplies","Becoming a seed that produces many."),
 ],
 "journey":"Each of the 40 days offers one way to live beyond yourself \u2014 a sacrifice, a service, a seed sown for others \u2014 with a partner check-in and a prayer.",
 "why":"The most multiplied lives in history were the ones most freely given away. Self-protection preserves a single seed; self-giving produces a harvest.",
 "cta":"Launch Living Beyond Yourself and help your people find life by giving it away.",
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
    <div class="kicker">The Campaign Library &nbsp;&middot;&nbsp; Multiplication &nbsp;&middot;&nbsp; Volume Two</div>
    <div class="cover-rule"></div>
    <h1>The <em>Multiplication</em><br>Collection</h1>
    <div class="sub">Five more forty-day campaigns that aim multiplication at what matters most \u2014 greater impact, exponential influence, a life well invested, and a life lived beyond yourself.</div>
    <div class="cover-foot">
      <div class="stats">
        <div class="stat"><div class="n">5</div><div class="l">Campaigns</div></div>
        <div class="stat"><div class="n">40</div><div class="l">Day Journey</div></div>
        <div class="stat"><div class="n">6</div><div class="l">Sessions Each</div></div>
        <div class="stat"><div class="n">NIV</div><div class="l">Scripture</div></div>
      </div>
      <div class="tier">Tier 2 &nbsp;&middot;&nbsp; Titles 06\u201310 &nbsp;&middot;&nbsp; For Companies &amp; Churches</div>
    </div>
  </div>
</div>"""

intro = """
<div class="page intro">
  <div class="frame"></div>
  <div class="intro-inner">
    <div class="kicker">Before You Begin</div>
    <h2>Multiplication only matters if<br>you multiply the <em>right things</em>.</h2>
    <p class="lead">Multiplication is a powerful force \u2014 and a neutral one. Aimed well, it turns one faithful life into a harvest; aimed poorly, it just scales what won\u2019t last. <strong>This second volume is about aim.</strong> Five distinct, forty-day journeys help your people point their multiplying energy at what truly matters: greater fruit, compounding influence, a well-invested life, and the kind of self-giving that produces a harvest far beyond themselves.</p>
    <div class="howrow">
      <div class="howcard"><div class="hn">40</div><h4>A Daily Rhythm</h4><p>Every day offers a short reading, one practical step, a spiritual-partner check-in, and a written prayer &mdash; small, repeatable, and easy to keep.</p></div>
      <div class="howcard"><div class="hn">6</div><h4>A Weekly Gathering</h4><p>Six group sessions give the journey its backbone, turning private growth into shared momentum across your company or church.</p></div>
      <div class="howcard"><div class="hn">1</div><h4>A Clear Outcome</h4><p>Each campaign is built around one transformation &mdash; so your people don\u2019t just multiply more, they multiply what matters.</p></div>
    </div>
    <div class="contents">
      <div class="ct">Inside This Volume</div>
      <div class="clist">
        <div class="cli"><span class="cnum">06</span><span><span class="cnm">Multiplying What Matters</span><br><span class="cds">Scale the things that truly last</span></span></div>
        <div class="cli"><span class="cnum">07</span><span><span class="cnm">Greater Impact</span><br><span class="cds">Bear more fruit by abiding deeper</span></span></div>
        <div class="cli"><span class="cnum">08</span><span><span class="cnm">Exponential Influence</span><br><span class="cds">Start ripples that compound</span></span></div>
        <div class="cli"><span class="cnum">09</span><span><span class="cnm">Investing Your Life Well</span><br><span class="cds">Spend your one life on purpose</span></span></div>
        <div class="cli"><span class="cnum">10</span><span><span class="cnm">Living Beyond Yourself</span><br><span class="cds">Find life by giving it away</span></span></div>
      </div>
    </div>
  </div>
</div>"""

closing = """
<div class="page close">
  <div class="frame"></div>
  <div class="close-inner">
    <div class="kicker">Ready When You Are</div>
    <h2>Help your people live<br>beyond <em>themselves</em>.</h2>
    <p class="cp">These five campaigns aim multiplication where it counts \u2014 at lasting fruit, compounding influence, a well-invested life, and a life poured out for others. Choose where your company or church is ready to grow, or move through all five across a season.</p>
    <div class="close-list">
      <div class="cl-row"><span class="cln">06</span><span class="clt">Multiplying What Matters</span><span class="cld">Gold, not straw</span></div>
      <div class="cl-row"><span class="cln">07</span><span class="clt">Greater Impact</span><span class="cld">Pruned for more fruit</span></div>
      <div class="cl-row"><span class="cln">08</span><span class="clt">Exponential Influence</span><span class="cld">The compounding ripple</span></div>
      <div class="cl-row"><span class="cln">09</span><span class="clt">Investing Your Life Well</span><span class="cld">Make the most of it</span></div>
      <div class="cl-row"><span class="cln">10</span><span class="clt">Living Beyond Yourself</span><span class="cld">The grain of wheat</span></div>
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
<title>The Multiplication Collection, Volume Two \u2014 Lifetogether</title>
<style>{FONTS}</style>
<style>{CSS}</style>
</head><body>{pages}</body></html>"""

pathlib.Path("/tmp/multiplication_v2.html").write_text(doc, encoding="utf-8")
print("HTML written:", len(doc), "chars")
