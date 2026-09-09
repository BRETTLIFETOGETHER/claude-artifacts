# -*- coding: utf-8 -*-
import pathlib
from brochure_template import FONTS, CSS, campaign_page

campaigns = [
{
 "num":"01","accent":"#2f6b4f","accent_soft":"#d8e8df",
 "title_a":"Life","title_b":"Stewardship",
 "subtitle":"Managing all you\u2019ve been given \u2014 your whole life, not just your money",
 "problem":"We tend to think of stewardship as a money word \u2014 something that comes up at offering time. But the truth is bigger and far more freeing: every part of our lives is on loan. Our hours, our gifts, our relationships, our influence \u2014 all of it entrusted, all of it accountable, and most of it managed on autopilot.",
 "promise":"Life Stewardship widens the lens. Over forty days your people learn to see their entire life as something to manage well for God \u2014 their time, talent, treasure, trust, and testimony \u2014 and discover the deep freedom of holding it all with open hands.",
 "verse":"Each of you should use whatever gift you have received to serve others, as faithful stewards of God\u2019s grace in its various forms.",
 "ref":"1 Peter 4:10 (NIV)",
 "bigidea":"You don\u2019t own your life \u2014 you manage it. And the moment you accept that, everything you hold becomes lighter to carry and richer to give.",
 "tags":["Whole-Life","Time","Talent","Treasure","Open Hands"],
 "best_for":"Church &amp; Company","backbone":"1 Peter 4:10; 1 Cor 4:1\u20132","metaphor":"The Entrusted Life","felt":"Whole-life stewardship \u00b7 all five T\u2019s",
 "sessions":[
   ("1","It\u2019s All on Loan","Why nothing you have is finally yours \u2014 and why that\u2019s good news."),
   ("2","Stewarding Time","Treating your hours as the non-renewable gift they are."),
   ("3","Stewarding Talent","Putting your God-given gifts to work for others."),
   ("4","Stewarding Treasure","Managing money as one part of a much bigger trust."),
   ("5","Trust &amp; Testimony","Caring for your relationships and your story as sacred responsibilities."),
   ("6","The Open Hand","Living the whole of life with a manager\u2019s freedom."),
 ],
 "journey":"Each of the 40 days takes one area of life \u2014 a few hours, a gift, a dollar, a relationship \u2014 and offers one small act of faithful management, plus a partner check-in and a prayer.",
 "why":"Most people steward their money while quietly squandering everything else. Whole-life stewardship changes how you hold all of it.",
 "cta":"Launch Life Stewardship and help your people manage their whole lives well.",
 "note":None,
},
{
 "num":"02","accent":"#a8842f","accent_soft":"#f0e7cf",
 "title_a":"","title_b":"Entrusted",
 "subtitle":"Recognizing the sacred trust God has placed in your hands",
 "problem":"To be entrusted with something is one of the highest honors another person can give \u2014 and God has entrusted each of us with far more than we realize: people, gifts, resources, opportunities, even the gospel itself. Yet most of us hold these trusts casually, as if they simply happened to land in our hands.",
 "promise":"Entrusted helps your people feel both the weight and the wonder of being trusted by God. Over forty days they learn to name what has been placed in their care, to guard it well, and to live with the quiet dignity of a person who has been given something that matters.",
 "verse":"Now it is required that those who have been given a trust must prove faithful.",
 "ref":"1 Corinthians 4:2 (NIV)",
 "bigidea":"Nothing in your hands is an accident. It was entrusted \u2014 and what is entrusted is meant to be guarded, grown, and one day returned with interest.",
 "tags":["Trust","Responsibility","Honor","Faithfulness","Calling"],
 "best_for":"Church &amp; Company","backbone":"1 Corinthians 4:1\u20132; 1 Tim 6:20","metaphor":"The Sacred Trust","felt":"Trust, identity, responsibility",
 "sessions":[
   ("1","The Honor of Being Trusted","Why entrustment is a gift before it is a duty."),
   ("2","Name What\u2019s in Your Hands","Taking honest inventory of all God has placed in your care."),
   ("3","Guard the Trust","Protecting what matters most from neglect and drift."),
   ("4","Grow What You\u2019re Given","Why a trust is meant to be multiplied, not merely maintained."),
   ("5","Accountable, Not Anxious","Living responsibly without living in fear."),
   ("6","Trusted with More","How faithfulness today opens the door to greater trust tomorrow."),
 ],
 "journey":"Each day names one thing entrusted to your people and offers one act of faithful care \u2014 a daily practice of treating ordinary things as the sacred trusts they are.",
 "why":"People rise to what they are trusted with. When your people grasp how much God has entrusted to them, they begin to live differently.",
 "cta":"Launch Entrusted and help your people live worthy of the trust they\u2019ve been given.",
 "note":None,
},
{
 "num":"03","accent":"#2d6a7a","accent_soft":"#d6e7ec",
 "title_a":"Stewarding","title_b":"What Matters",
 "subtitle":"Giving your best to the things that last the longest",
 "problem":"It is possible to manage your money carefully while quietly squandering the things that matter far more \u2014 your time, your attention, your relationships, your one short life. The urgent always shouts; the important rarely does. And so we steward our spreadsheets and neglect our souls.",
 "promise":"Stewarding What Matters reorders the priorities. Over forty days your people learn to number their days, identify what truly deserves their best, and steward their time and attention as carefully as they\u2019ve ever stewarded a dollar.",
 "verse":"Teach us to number our days, that we may gain a heart of wisdom.",
 "ref":"Psalm 90:12 (NIV)",
 "bigidea":"You will give your life to something. Stewardship is simply making sure you give it \u2014 on purpose \u2014 to the things that matter most.",
 "tags":["Priorities","Time","Attention","Relationships","What Lasts"],
 "best_for":"Church &amp; Company","backbone":"Psalm 90:12; Matthew 6:33","metaphor":"Numbering the Days","felt":"Time, priorities, what lasts",
 "sessions":[
   ("1","The Urgent and the Important","Why the loudest things are rarely the most valuable."),
   ("2","Number Your Days","Letting the brevity of life clarify what deserves your best."),
   ("3","Stewarding Attention","Reclaiming your focus in an age built to steal it."),
   ("4","Stewarding Relationships","Giving the people who matter most more than your leftovers."),
   ("5","First Things First","Putting the kingdom, not the calendar, in charge of your life."),
   ("6","A Well-Spent Life","Choosing, daily, to invest where it truly counts."),
 ],
 "journey":"Each of the 40 days asks one simple question \u2014 does this deserve my best? \u2014 and offers one small reordering, with a partner check-in and a prayer.",
 "why":"At the end of life, no one regrets a balanced budget over a wasted one. They regret giving their best to things that never mattered.",
 "cta":"Launch Stewarding What Matters and help your people spend their lives on purpose.",
 "note":None,
},
{
 "num":"04","accent":"#a85733","accent_soft":"#f0ddd0",
 "title_a":"Faithful","title_b":"Stewardship",
 "subtitle":"The everyday discipline of being trustworthy in the small things",
 "problem":"We tend to imagine stewardship as the big, dramatic decision \u2014 the major gift, the bold sacrifice. But faithfulness is built in the small, unseen, repeated choices no one applauds: the honest expense report, the kept promise, the quiet integrity when no one is watching. And it\u2019s exactly there that most of us drift.",
 "promise":"Faithful Stewardship builds the muscle of everyday faithfulness. Over forty days your people learn that character is forged in small things, that trustworthiness compounds, and that the path to \u201cwell done\u201d is paved with a thousand ordinary faithful moments.",
 "verse":"Well done, good and faithful servant! You have been faithful with a few things; I will put you in charge of many things.",
 "ref":"Matthew 25:21 (NIV)",
 "bigidea":"God isn\u2019t looking for impressive. He\u2019s looking for faithful. And faithful is something you can be today, with whatever is already in your hands.",
 "tags":["Faithfulness","Integrity","Consistency","Character","Trustworthy"],
 "best_for":"Church &amp; Company","backbone":"Matthew 25:21; Luke 16:10","metaphor":"Faithful in the Small Things","felt":"Faithfulness, integrity, consistency",
 "sessions":[
   ("1","Faithful in Little","Why how you handle small things decides everything."),
   ("2","When No One Is Watching","Integrity as the quiet core of all stewardship."),
   ("3","The Compounding of Character","How small faithful choices add up to a trustworthy life."),
   ("4","Finishing What You Start","The underrated faithfulness of following through."),
   ("5","Faithful Through the Dry Seasons","Staying steady when faithfulness goes unrewarded."),
   ("6","Well Done","Living today for the words you long to hear at the end."),
 ],
 "journey":"Each day names one small place to be faithful \u2014 a promise, a task, a dollar, a word \u2014 and invites your people to follow through, with a partner check-in and a prayer.",
 "why":"No one becomes faithful in the big things who was careless in the small ones. Stewardship is won or lost in the ordinary.",
 "cta":"Launch Faithful Stewardship and help your people become trustworthy in everything.",
 "note":None,
},
{
 "num":"05","accent":"#7a5a2e","accent_soft":"#ecddc6",
 "title_a":"Stewardship","title_b":"That Lasts",
 "subtitle":"Building a legacy of faithfulness that outlives you",
 "problem":"Most of us steward only for the moment \u2014 this month\u2019s budget, this week\u2019s calendar, this year\u2019s goals. But a steward with no long view leaves nothing behind. We plant little for the generations after us, invest little in what will outlast us, and risk arriving at the end having managed a lifetime that simply\u2026 ends.",
 "promise":"Stewardship That Lasts lifts your people\u2019s eyes to the horizon. Over forty days they learn to steward with a generational and eternal view \u2014 to plant trees they\u2019ll never sit under, build a legacy of faith and generosity, and invest in what will still matter long after they\u2019re gone.",
 "verse":"A good person leaves an inheritance for their children\u2019s children.",
 "ref":"Proverbs 13:22 (NIV)",
 "bigidea":"The truest test of stewardship isn\u2019t what you accumulate in your lifetime \u2014 it\u2019s what you leave behind, and Who you point the next generation toward.",
 "tags":["Legacy","Generations","The Long View","Testimony","Endurance"],
 "best_for":"Church &amp; Company","backbone":"Proverbs 13:22; Matthew 6:20","metaphor":"Trees You\u2019ll Never Sit Under","felt":"Legacy, the long view, testimony",
 "sessions":[
   ("1","The Short-View Problem","Why managing only for today leaves nothing for tomorrow."),
   ("2","Plant Trees You\u2019ll Never Sit Under","Stewarding for a generation you may never meet."),
   ("3","An Inheritance of Faith","Passing on what matters most \u2014 not just what\u2019s in the account."),
   ("4","Treasures That Don\u2019t Rust","Investing in what genuinely lasts forever."),
   ("5","Your Testimony as Legacy","Stewarding your story for the people who come next."),
   ("6","Finishing Well","Living the final chapter with the long view in mind."),
 ],
 "journey":"Each of the 40 days connects one present choice to a lasting outcome and offers one small investment in the future, with a partner check-in and a prayer.",
 "why":"We are all writing a story the next generation will read. Stewardship that lasts makes sure it\u2019s worth passing on.",
 "cta":"Launch Stewardship That Lasts and help your people build a legacy that endures.",
 "note":None,
},
]

cover = """
<div class="page cover">
  <div class="frame gold"></div>
  <div class="cover-inner">
    <div class="brandmark">Lifetogether</div>
    <div class="kicker">The Campaign Library &nbsp;&middot;&nbsp; Stewardship Collection</div>
    <div class="cover-rule"></div>
    <h1>The <em>Stewardship</em><br>Collection</h1>
    <div class="sub">Five forty-day campaigns to help your people manage all they\u2019ve been given \u2014 their time, talent, treasure, trust, and testimony \u2014 as faithful stewards of God.</div>
    <div class="cover-foot">
      <div class="stats">
        <div class="stat"><div class="n">5</div><div class="l">Campaigns</div></div>
        <div class="stat"><div class="n">40</div><div class="l">Day Journey</div></div>
        <div class="stat"><div class="n">6</div><div class="l">Sessions Each</div></div>
        <div class="stat"><div class="n">NIV</div><div class="l">Scripture</div></div>
      </div>
      <div class="tier">Tier 1 &nbsp;&middot;&nbsp; The Five T\u2019s &nbsp;&middot;&nbsp; For Churches &amp; Companies</div>
    </div>
  </div>
</div>"""

intro = """
<div class="page intro">
  <div class="frame"></div>
  <div class="intro-inner">
    <div class="kicker">Before You Begin</div>
    <h2>Everything you have<br>is on <em>loan</em>.</h2>
    <p class="lead">Stewardship is one of the most misunderstood words in the church \u2014 most people hear it and think only of money. But the biblical idea is far bigger: your <strong>time, talent, treasure, trust, and testimony</strong> were all entrusted to you to manage well for God. This collection takes that whole-life truth and turns it into five distinct, forty-day journeys \u2014 each one helping your people hold what they\u2019ve been given with open, faithful hands.</p>
    <div class="howrow">
      <div class="howcard"><div class="hn">40</div><h4>A Daily Rhythm</h4><p>Every day offers a short reading, one practical step, a spiritual-partner check-in, and a written prayer &mdash; small, repeatable, and easy to keep.</p></div>
      <div class="howcard"><div class="hn">6</div><h4>A Weekly Gathering</h4><p>Six group sessions give the journey its backbone, turning private change into shared momentum across your church or team.</p></div>
      <div class="howcard"><div class="hn">1</div><h4>A Clear Outcome</h4><p>Each campaign is built around one transformation &mdash; so your people don\u2019t just learn about stewardship, they actually begin to live it.</p></div>
    </div>
    <div class="contents">
      <div class="ct">Inside This Collection</div>
      <div class="clist">
        <div class="cli"><span class="cnum">01</span><span><span class="cnm">Life Stewardship</span><br><span class="cds">Steward your whole life, not just money</span></span></div>
        <div class="cli"><span class="cnum">02</span><span><span class="cnm">Entrusted</span><br><span class="cds">Recognize the sacred trust in your hands</span></span></div>
        <div class="cli"><span class="cnum">03</span><span><span class="cnm">Stewarding What Matters</span><br><span class="cds">Give your best to what lasts longest</span></span></div>
        <div class="cli"><span class="cnum">04</span><span><span class="cnm">Faithful Stewardship</span><br><span class="cds">Be trustworthy in the small things</span></span></div>
        <div class="cli"><span class="cnum">05</span><span><span class="cnm">Stewardship That Lasts</span><br><span class="cds">Build a legacy that outlives you</span></span></div>
      </div>
    </div>
  </div>
</div>"""

closing = """
<div class="page close">
  <div class="frame"></div>
  <div class="close-inner">
    <div class="kicker">Ready When You Are</div>
    <h2>Help your people live<br>as faithful <em>stewards</em>.</h2>
    <p class="cp">From the whole of life to the smallest daily choice, these five campaigns help your people see all they hold as a trust from God \u2014 and learn to manage it with freedom, faithfulness, and a view toward what lasts. Choose where your church or team needs to begin, or journey through all five across a season.</p>
    <div class="close-list">
      <div class="cl-row"><span class="cln">01</span><span class="clt">Life Stewardship</span><span class="cld">The whole life</span></div>
      <div class="cl-row"><span class="cln">02</span><span class="clt">Entrusted</span><span class="cld">The sacred trust</span></div>
      <div class="cl-row"><span class="cln">03</span><span class="clt">Stewarding What Matters</span><span class="cld">First things first</span></div>
      <div class="cl-row"><span class="cln">04</span><span class="clt">Faithful Stewardship</span><span class="cld">Faithful in little</span></div>
      <div class="cl-row"><span class="cln">05</span><span class="clt">Stewardship That Lasts</span><span class="cld">A lasting legacy</span></div>
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
<title>The Stewardship Collection \u2014 Lifetogether</title>
<style>{FONTS}</style>
<style>{CSS}</style>
</head><body>{pages}</body></html>"""

pathlib.Path("/tmp/stewardship.html").write_text(doc, encoding="utf-8")
print("HTML written:", len(doc), "chars")
