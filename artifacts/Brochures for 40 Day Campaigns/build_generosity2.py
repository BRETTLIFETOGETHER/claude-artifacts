# -*- coding: utf-8 -*-
import pathlib
from brochure_template import FONTS, CSS, campaign_page

campaigns = [
{
 "num":"06","accent":"#2c6e7d","accent_soft":"#d6e7eb",
 "title_a":"The Generosity","title_b":"Journey",
 "subtitle":"Growing, step by step, into a generous life",
 "problem":"Almost no one becomes generous overnight. Yet we often treat generosity like a switch we should already have flipped \u2014 and when our giving doesn\u2019t match our ideals, we feel guilty, stall out, and quietly give up. The truth is gentler and far more hopeful: generosity is a journey, and most of us are only partway down the road.",
 "promise":"The Generosity Journey gives your people a path to walk. Over forty days they\u2019ll move from wherever they are toward where God is calling them \u2014 taking the next faithful step, then the next \u2014 and discover that generosity, like any grace, is something you grow into over time.",
 "verse":"But since you excel in everything\u2026 see that you also excel in this grace of giving.",
 "ref":"2 Corinthians 8:7 (NIV)",
 "bigidea":"Generosity isn\u2019t a switch you flip; it\u2019s a road you walk. You don\u2019t have to arrive today \u2014 you only have to take the next step.",
 "tags":["Growth","Progress","Next Step","Grace","Journey"],
 "best_for":"Church &amp; Company","backbone":"2 Corinthians 8:7; Philippians 1:6","metaphor":"The Road to Generous","felt":"Growth, process, becoming generous",
 "sessions":[
   ("1","Wherever You Are","Meeting generosity as a starting line, not a standard to fail."),
   ("2","The Next Faithful Step","Why growth, not perfection, is the goal."),
   ("3","Excel in This Grace","Treating giving as a grace you can grow in."),
   ("4","Past the Plateaus","Pushing through the places generosity tends to stall."),
   ("5","Companions on the Road","Growing in generosity alongside others."),
   ("6","The Long Walk Home","Staying on the journey for a lifetime."),
 ],
 "journey":"Each of the 40 days marks one small step forward \u2014 slightly bigger, slightly braver than yesterday \u2014 with a partner check-in and a prayer, so growth becomes visible over six weeks.",
 "why":"Guilt has never made anyone generous. A clear next step, walked with others, changes people for good.",
 "cta":"Launch The Generosity Journey and help your people take their next step.",
 "note":None,
},
{
 "num":"07","accent":"#b13e63","accent_soft":"#f3dae3",
 "title_a":"Generosity Changes","title_b":"Everything",
 "subtitle":"The ripple effect of a single generous act",
 "problem":"We tend to think of a gift as a transaction \u2014 money leaves one hand and lands in another, and that\u2019s the end of it. But generosity is never that contained. A single generous act changes the giver, lifts the receiver, inspires a watcher, and sets off ripples that travel much further than we\u2019ll ever see.",
 "promise":"Generosity Changes Everything opens your people\u2019s eyes to the ripple. Over forty days they\u2019ll discover how giving transforms not just budgets but hearts, families, churches, and communities \u2014 and how their ordinary generosity becomes part of something far larger than themselves.",
 "verse":"You will be enriched in every way so that you can be generous on every occasion.",
 "ref":"2 Corinthians 9:11 (NIV)",
 "bigidea":"A gift is never just a gift. Generosity changes the giver first, then ripples outward through people and places you\u2019ll never even meet.",
 "tags":["Impact","Ripple Effect","Transformation","Community","Change"],
 "best_for":"Church &amp; Company","backbone":"2 Corinthians 9:10\u201313; Luke 6:38","metaphor":"The Ripple Effect","felt":"Impact, transformation, ripple",
 "sessions":[
   ("1","More Than a Transaction","Why a gift never stops where it lands."),
   ("2","Changed by Giving","How generosity transforms the giver first."),
   ("3","The Ripple Outward","Tracing the unexpected reach of a single gift."),
   ("4","A Generous Church","What happens when a whole community gives."),
   ("5","Generosity Is Contagious","How one open hand quietly opens others."),
   ("6","Part of Something Bigger","Joining the work God is doing through givers."),
 ],
 "journey":"Each of the 40 days connects one act of giving to its wider effect and invites your people to start a ripple, with a partner check-in and a prayer.",
 "why":"You will rarely see the full reach of your generosity \u2014 but it\u2019s always greater than the gift. That\u2019s how God designed it.",
 "cta":"Launch Generosity Changes Everything and help your people start a ripple.",
 "note":None,
},
{
 "num":"08","accent":"#c07a24","accent_soft":"#f4e5cb",
 "title_a":"","title_b":"Abundance",
 "subtitle":"Trading the fear of scarcity for the confidence of enough",
 "problem":"Underneath a lot of tight-fisted living is one quiet belief: there isn\u2019t enough, and there won\u2019t be. Scarcity thinking tells us to hoard, to fear, to grip what we have a little tighter \u2014 and it slowly shrinks our generosity, our peace, and our trust in a God who has promised to provide.",
 "promise":"Abundance confronts the scarcity lie with a bigger truth. Over forty days your people learn to see the world the way Jesus did \u2014 where five loaves feed thousands and there are baskets left over \u2014 and discover that a settled confidence in God\u2019s provision is what finally sets generosity free.",
 "verse":"And my God will meet all your needs according to the riches of his glory in Christ Jesus.",
 "ref":"Philippians 4:19 (NIV)",
 "bigidea":"Scarcity says \u201cgive carefully, there may not be enough.\u201d Abundance says \u201cgive freely, because the God who feeds thousands from a few loaves has you covered.\u201d",
 "tags":["Abundance","Provision","Trust","Scarcity","Faith"],
 "best_for":"Church &amp; Company","backbone":"Philippians 4:19; John 6:1\u201313","metaphor":"Loaves and Fishes","felt":"Abundance mindset, provision",
 "sessions":[
   ("1","The Scarcity Lie","Naming the fear that quietly shapes our giving."),
   ("2","Loaves and Fishes","How God multiplies the little we offer Him."),
   ("3","Enough, and More","Learning to trust the God who always provides."),
   ("4","Open-Handed in Abundance","Why confidence in provision frees generosity."),
   ("5","The Math of Heaven","Where less, given to God, becomes more."),
   ("6","Living from Plenty","Carrying an abundance mindset into everyday life."),
 ],
 "journey":"Each of the 40 days replaces one scarcity thought with one truth about God\u2019s provision and one freehearted act of giving, with a partner check-in and a prayer.",
 "why":"People give from the world they believe they live in. Show them they live in God\u2019s abundance, and generosity follows naturally.",
 "cta":"Launch Abundance and help your people give from confidence, not fear.",
 "note":None,
},
{
 "num":"09","accent":"#5d4b8a","accent_soft":"#e3def0",
 "title_a":"The Blessed","title_b":"Life",
 "subtitle":"Discovering that the truly blessed life is the generous one",
 "problem":"We use the word \u201cblessed\u201d constantly, and we almost always mean received \u2014 what we\u2019ve been given, what we get to enjoy, what\u2019s gone well for us. But Scripture keeps pointing somewhere else: that we\u2019re blessed in order to bless, and that the truly good life isn\u2019t found in accumulating blessings but in becoming one.",
 "promise":"The Blessed Life redefines the word. Over forty days your people learn that God\u2019s blessings were never meant to terminate on them \u2014 they were meant to flow through them \u2014 and they discover the deep, surprising joy of a life spent being a blessing to others.",
 "verse":"I will bless you\u2026 and you will be a blessing.",
 "ref":"Genesis 12:2 (NIV)",
 "bigidea":"You weren\u2019t blessed to be a reservoir of God\u2019s goodness \u2014 you were blessed to be a channel of it. The blessed life and the generous life are the same life.",
 "tags":["Blessing","Purpose","Joy","Channel","Gratitude"],
 "best_for":"Church &amp; Company","backbone":"Genesis 12:1\u20133; Acts 20:35","metaphor":"Blessed to Be a Blessing","felt":"Blessing, purpose of provision",
 "sessions":[
   ("1","What \u201cBlessed\u201d Really Means","Recovering the word from sentimentality."),
   ("2","Blessed to Bless","Why God\u2019s gifts are meant to keep moving."),
   ("3","The Reservoir Problem","What happens when blessing stops with us."),
   ("4","A Channel of Grace","Becoming the means of someone else\u2019s blessing."),
   ("5","The Joy of Being a Blessing","The unexpected gladness of giving forward."),
   ("6","A Truly Blessed Life","Living as a conduit of God\u2019s goodness."),
 ],
 "journey":"Each of the 40 days takes one blessing in your people\u2019s lives and turns it outward into a blessing for someone else, with a partner check-in and a prayer.",
 "why":"The most blessed people you know aren\u2019t the ones with the most. They\u2019re the ones who give the most away.",
 "cta":"Launch The Blessed Life and help your people become a blessing, not just receive one.",
 "note":None,
},
{
 "num":"10","accent":"#2e8d77","accent_soft":"#d2eee6",
 "title_a":"","title_b":"Overflow",
 "subtitle":"Giving from a heart so full it spills onto others",
 "problem":"A lot of us try to give from empty. Depleted, stretched, running on fumes, we squeeze out generosity by sheer willpower \u2014 and it shows. Forced giving is joyless and short-lived, because you cannot pour from a cup that has nothing left in it.",
 "promise":"Overflow flips the order. Over forty days your people learn to be filled first \u2014 by God\u2019s love, presence, and provision \u2014 until generosity stops being a duty they grind out and becomes the natural overflow of a full and grateful heart that simply spills onto everyone around them.",
 "verse":"\u2026their overflowing joy and their extreme poverty welled up in rich generosity.",
 "ref":"2 Corinthians 8:2 (NIV)",
 "bigidea":"You can\u2019t pour from an empty cup. The most generous people aren\u2019t the most disciplined \u2014 they\u2019re the most full. Generosity is meant to be an overflow, not an effort.",
 "tags":["Overflow","Fullness","Joy","Gratitude","Abundance"],
 "best_for":"Church &amp; Company","backbone":"2 Corinthians 8:2; Psalm 23:5","metaphor":"The Overflowing Cup","felt":"Overflow, joy, giving from fullness",
 "sessions":[
   ("1","Giving from Empty","Why willpower generosity always runs dry."),
   ("2","Filled First","Receiving God\u2019s love before pouring it out."),
   ("3","The Overflowing Cup","What happens when gratitude finally runs over."),
   ("4","Joy That Spills","How a full heart gives almost by accident."),
   ("5","Staying Full","Daily habits that keep the cup running over."),
   ("6","A Life of Overflow","Generosity as the natural spill of a grateful life."),
 ],
 "journey":"Each of the 40 days pairs one way to be filled by God with one way to let that fullness overflow to someone else, with a partner check-in and a prayer.",
 "why":"Generosity ground out from emptiness never lasts. Generosity that overflows from fullness never stops.",
 "cta":"Launch Overflow and help your people give from a cup that\u2019s running over.",
 "note":None,
},
]

for _c in campaigns: _c["category"] = "Generosity"

cover = """
<div class="page cover">
  <div class="frame gold"></div>
  <div class="cover-inner">
    <div class="brandmark">Lifetogether</div>
    <div class="kicker">The Campaign Library &nbsp;&middot;&nbsp; Generosity &nbsp;&middot;&nbsp; Volume Two</div>
    <div class="cover-rule"></div>
    <h1>The <em>Generosity</em><br>Collection</h1>
    <div class="sub">Five more forty-day campaigns that follow generosity all the way out \u2014 from the journey of becoming generous to the ripple, abundance, blessing, and overflow it unleashes.</div>
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
    <h2>Generosity doesn\u2019t end<br>with the <em>gift</em>.</h2>
    <p class="lead">A single act of giving sets something in motion. It grows in the giver, ripples into the community, and slowly reshapes how a person sees abundance, blessing, and the whole point of what they\u2019ve been given. <strong>This second volume follows generosity all the way out</strong> \u2014 five distinct, forty-day journeys that move your people from the first faithful step into a life of overflow.</p>
    <div class="howrow">
      <div class="howcard"><div class="hn">40</div><h4>A Daily Rhythm</h4><p>Every day offers a short reading, one practical step, a spiritual-partner check-in, and a written prayer &mdash; small, repeatable, and easy to keep.</p></div>
      <div class="howcard"><div class="hn">6</div><h4>A Weekly Gathering</h4><p>Six group sessions give the journey its backbone, turning private change into shared momentum across your church or team.</p></div>
      <div class="howcard"><div class="hn">1</div><h4>A Clear Outcome</h4><p>Each campaign is built around one transformation &mdash; so your people don\u2019t just admire generosity, they begin to live in its overflow.</p></div>
    </div>
    <div class="contents">
      <div class="ct">Inside This Volume</div>
      <div class="clist">
        <div class="cli"><span class="cnum">06</span><span><span class="cnm">The Generosity Journey</span><br><span class="cds">Grow, step by step, into a generous life</span></span></div>
        <div class="cli"><span class="cnum">07</span><span><span class="cnm">Generosity Changes Everything</span><br><span class="cds">See the ripple effect of every gift</span></span></div>
        <div class="cli"><span class="cnum">08</span><span><span class="cnm">Abundance</span><br><span class="cds">Trade scarcity for trust in God\u2019s supply</span></span></div>
        <div class="cli"><span class="cnum">09</span><span><span class="cnm">The Blessed Life</span><br><span class="cds">Be blessed in order to bless others</span></span></div>
        <div class="cli"><span class="cnum">10</span><span><span class="cnm">Overflow</span><br><span class="cds">Give from a heart that\u2019s running over</span></span></div>
      </div>
    </div>
  </div>
</div>"""

closing = """
<div class="page close">
  <div class="frame"></div>
  <div class="close-inner">
    <div class="kicker">Ready When You Are</div>
    <h2>Help your people live<br>in the <em>overflow</em>.</h2>
    <p class="cp">These five campaigns follow generosity past the gift \u2014 into the journey, the ripple, the abundance, the blessing, and the overflow God designed it to release. Choose where your church or team is ready to grow, or move through all five across a season.</p>
    <div class="close-list">
      <div class="cl-row"><span class="cln">06</span><span class="clt">The Generosity Journey</span><span class="cld">The next step</span></div>
      <div class="cl-row"><span class="cln">07</span><span class="clt">Generosity Changes Everything</span><span class="cld">The ripple effect</span></div>
      <div class="cl-row"><span class="cln">08</span><span class="clt">Abundance</span><span class="cld">Loaves and fishes</span></div>
      <div class="cl-row"><span class="cln">09</span><span class="clt">The Blessed Life</span><span class="cld">Blessed to bless</span></div>
      <div class="cl-row"><span class="cln">10</span><span class="clt">Overflow</span><span class="cld">A cup running over</span></div>
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
<title>The Generosity Collection, Volume Two \u2014 Lifetogether</title>
<style>{FONTS}</style>
<style>{CSS}</style>
</head><body>{pages}</body></html>"""

pathlib.Path("/tmp/generosity_v2.html").write_text(doc, encoding="utf-8")
print("HTML written:", len(doc), "chars")
