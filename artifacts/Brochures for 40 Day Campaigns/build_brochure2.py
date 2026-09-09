# -*- coding: utf-8 -*-
import pathlib
from brochure_template import FONTS, CSS, campaign_page

campaigns = [
{
 "num":"06","accent":"#5b4a8a","accent_soft":"#e3def0",
 "title_a":"God, Money","title_b":"&amp; Me",
 "subtitle":"Settling the most personal question money asks",
 "problem":"Money is never really about money. Beneath every budget is a quieter question we rarely say out loud: who is actually in charge of my life? For most of us, money has slipped onto the throne so gradually we never noticed it sit down.",
 "promise":"God, Money &amp; Me brings the relationship into the open. Over forty days your people confront the question of lordship head-on \u2014 whose money is it, who do I trust, who runs my life \u2014 until God, not money, is back at the center where He belongs.",
 "verse":"Watch out! Be on your guard against all kinds of greed; life does not consist in an abundance of possessions.",
 "ref":"Luke 12:15 (NIV)",
 "bigidea":"The real question is never \u201cwhat should I do with my money?\u201d but \u201cwho owns me?\u201d Settle that, and every other money question gets simpler.",
 "tags":["Lordship","Surrender","Idolatry","The Heart","Trust"],
 "best_for":"Church &amp; Company","backbone":"Luke 12:13\u201321","metaphor":"Who\u2019s on the Throne","felt":"Surrender, money\u2019s grip, the heart",
 "sessions":[
   ("1","The Quiet Coup","How money slips onto the throne of a life without anyone deciding to put it there."),
   ("2","The Rich Fool","Jesus\u2019 sharpest warning about a life built around accumulation."),
   ("3","Whose Is It, Really?","Reckoning honestly with the question of who truly owns what we hold."),
   ("4","Two Loves","Why the heart cannot finally serve both God and money."),
   ("5","The Great Exchange","Trading the exhausting grip of control for the freedom of trust."),
   ("6","Back on the Throne","Restoring God to the center of your finances \u2014 for good."),
 ],
 "journey":"Each of the 40 days invites one honest heart-check, one practical step of surrender, a spiritual-partner conversation, and a written prayer \u2014 a daily realignment of who sits at the center.",
 "why":"Until the lordship question is settled, every financial fix is temporary. Settle it, and everything else begins to change.",
 "cta":"Launch God, Money &amp; Me and help your people put God back at the center.",
 "note":None,
},
{
 "num":"07","accent":"#4e8358","accent_soft":"#dcebe0",
 "title_a":"Financial","title_b":"Health",
 "subtitle":"Building lasting wellness in how you handle money",
 "problem":"We schedule physical checkups, count our steps, and watch what we eat \u2014 but most of us have never once checked our financial vital signs. So small problems go unnoticed until they become emergencies, and we treat money like a recurring crisis instead of a daily habit.",
 "promise":"Financial Health treats money the way we treat the body: with regular checkups and small, repeatable habits. Over forty days your people learn to read their financial vital signs and build the everyday rhythms that produce real wholeness across earning, saving, spending, and giving.",
 "verse":"I pray that you may enjoy good health and that all may go well with you, even as your soul is getting along well.",
 "ref":"3 John 1:2 (NIV)",
 "bigidea":"Financial health is built the same way physical health is \u2014 through small, consistent habits, not heroic one-time fixes.",
 "tags":["Wellness","Habits","Budgeting","Vital Signs","Wholeness"],
 "best_for":"Church &amp; Company","backbone":"3 John 1:2; Prov 27:23\u201324","metaphor":"Financial Vital Signs","felt":"Budgeting, debt, healthy habits",
 "sessions":[
   ("1","Check the Vital Signs","Learning to read the simple numbers that reveal your true financial condition."),
   ("2","Know Your Flocks","The ancient wisdom of paying careful attention to all you have."),
   ("3","The Four Habits","Earning, saving, spending, and giving in healthy proportion."),
   ("4","Treating the Debt","A clear, hopeful path toward addressing what you owe."),
   ("5","Building the Reserve","Why margin and savings are the immune system of a healthy financial life."),
   ("6","A Lifetime of Wellness","Turning forty days of habits into a permanently healthier life."),
 ],
 "journey":"Every day offers one small, doable habit and a quick vital-sign check, plus a partner check-in and a prayer \u2014 daily reps that build real financial fitness over six weeks.",
 "why":"Like the body, our finances rarely fail all at once. They erode in the small, unattended habits \u2014 and they heal there too.",
 "cta":"Launch Financial Health and help your people build money habits that last.",
 "note":None,
},
{
 "num":"08","accent":"#9e3b2f","accent_soft":"#f1dcd5",
 "title_a":"Breaking","title_b":"Financial Fear",
 "subtitle":"Confronting the dread and scarcity that drive us",
 "problem":"Beneath many money struggles is not a math problem but a fear problem \u2014 a gnawing dread of running out, a scarcity voice that insists there will never be enough no matter what the numbers say. Fear makes us hoard, panic, avoid, and decide badly.",
 "promise":"Breaking Financial Fear confronts that voice directly. Over forty days your people learn to name their fear, expose its lies, and replace a scarcity mindset with a settled confidence in a God who provides \u2014 trading paralysis for courage.",
 "verse":"For the Spirit God gave us does not make us timid, but gives us power, love and self-discipline.",
 "ref":"2 Timothy 1:7 (NIV)",
 "bigidea":"Fear lies about your future. Faith tells the truth about your Provider. Courage is simply choosing to believe the right voice.",
 "tags":["Fear","Scarcity","Courage","Provision","Freedom"],
 "best_for":"Church &amp; Company","backbone":"2 Timothy 1:7; Isaiah 41:10","metaphor":"Breaking the Grip","felt":"Money fear, scarcity, debt dread",
 "sessions":[
   ("1","Name the Fear","Bringing the unspoken dread into the light, where it loses its power."),
   ("2","The Scarcity Lie","Exposing the voice that insists there will never be enough."),
   ("3","Consider the Provider","Why the One who feeds the birds can be trusted with you."),
   ("4","Courage in the Numbers","Facing your real financial picture without flinching."),
   ("5","From Hoarding to Open Hands","How trust loosens fear\u2019s white-knuckle grip."),
   ("6","Walking Free","Living with courage long after the forty days are done."),
 ],
 "journey":"Each day pairs a fear to confront with a truth to stand on and one small act of courage \u2014 daily steps that, over six weeks, quietly break fear\u2019s hold.",
 "why":"Financial fear rarely announces itself, yet it shapes nearly every money decision we make \u2014 and freedom begins the moment it\u2019s named.",
 "cta":"Launch Breaking Financial Fear and help your people trade dread for courage.",
 "note":"A gentle note: This campaign addresses financial fear and stress with spiritual encouragement and is not a substitute for professional financial or mental-health advice. Anyone carrying acute fear or distress is warmly encouraged to reach out to a trusted counselor or advisor.",
},
{
 "num":"09","accent":"#b07d2b","accent_soft":"#f0e6cd",
 "title_a":"Money and","title_b":"Meaning",
 "subtitle":"Connecting what you have to what truly matters",
 "problem":"Many people quietly chase more money believing it will finally deliver meaning \u2014 and then arrive, exhausted, to find the meaning isn\u2019t there. We\u2019ve confused the tool for the treasure, and a life spent accumulating can end up strangely empty.",
 "promise":"Money and Meaning realigns the two. Over forty days your people discover that money is a powerful tool for a meaningful life \u2014 never a substitute for one \u2014 and learn to direct what they have toward the things that will still matter in a hundred years.",
 "verse":"\u2026so that they may take hold of the life that is truly life.",
 "ref":"1 Timothy 6:19 (NIV)",
 "bigidea":"Money is a terrible master and a poor god \u2014 but in the right hands it\u2019s a powerful tool for building a life that truly matters.",
 "tags":["Purpose","Meaning","Alignment","Legacy","Generosity"],
 "best_for":"Church &amp; Company","backbone":"1 Timothy 6:17\u201319; Eccl 5:10","metaphor":"The Compass","felt":"Purpose, alignment, meaning",
 "sessions":[
   ("1","The Empty Pursuit","Why more money so rarely delivers the meaning it promises."),
   ("2","Tool, Not Treasure","Putting money back in its proper place \u2014 useful, not ultimate."),
   ("3","What Matters Most","Naming the values your money should be serving."),
   ("4","Aligning the Spend","Bringing your spending into line with your deepest priorities."),
   ("5","Rich Toward Others","How generosity turns money into lasting meaning."),
   ("6","A Life That Counts","Building a legacy that outlives your bank balance."),
 ],
 "journey":"Each of the 40 days connects one money decision to one deeper value, with a partner check-in and a prayer \u2014 daily practice in spending your life, not just your money, on what matters.",
 "why":"At the end, no one wishes they had accumulated more. They wish their money had meant more \u2014 and it still can.",
 "cta":"Launch Money and Meaning and help your people spend their lives on what lasts.",
 "note":None,
},
{
 "num":"10","accent":"#2f7d86","accent_soft":"#d6eaed",
 "title_a":"Peace with","title_b":"Money",
 "subtitle":"Ending the war and finding a settled relationship",
 "problem":"Many of us carry a long, complicated history with money \u2014 old mistakes we still feel, shame we never named, a low-grade striving that no amount ever seems to satisfy. We\u2019re not at war with our budget so much as with money itself, and the fighting is exhausting.",
 "promise":"Peace with Money helps your people lay down their arms. Over forty days they make peace with their financial past, release the shame and the striving, and build a settled, grace-filled relationship with money rooted in contentment and the unshakable presence of God.",
 "verse":"Be content with what you have, because God has said, \u201cNever will I leave you nor forsake you.\u201d",
 "ref":"Hebrews 13:5 (NIV)",
 "bigidea":"You can stop fighting with money. Peace doesn\u2019t come from finally having enough \u2014 it comes from knowing the One who is always enough.",
 "tags":["Contentment","Grace","Reconciliation","Shame Released","Rest"],
 "best_for":"Church &amp; Company","backbone":"Hebrews 13:5; Phil 4:11\u201313","metaphor":"The Settled Treaty","felt":"Shame, striving, contentment",
 "sessions":[
   ("1","The Long War","Recognizing the exhausting, often hidden conflict we have with money."),
   ("2","Grace for the Past","Releasing old money mistakes and the shame that clings to them."),
   ("3","The End of Striving","Why more is never the real answer to the ache for enough."),
   ("4","The Secret of Content","Learning, like Paul, to be at rest in plenty or in want."),
   ("5","An Unshakable Anchor","Resting your security in a God who never leaves."),
   ("6","A Settled Heart","Walking into a lifelong, peaceful relationship with money."),
 ],
 "journey":"Each day offers a short reading, one step toward contentment or reconciliation, a partner check-in, and a prayer \u2014 small daily peace treaties that, over six weeks, end a long war.",
 "why":"The goal isn\u2019t a perfect balance sheet but a peaceful heart \u2014 and that kind of peace is available to anyone, at any income.",
 "cta":"Launch Peace with Money and help your people finally lay down the fight.",
 "note":None,
},
]

cover = """
<div class="page cover">
  <div class="frame gold"></div>
  <div class="cover-inner">
    <div class="brandmark">Lifetogether</div>
    <div class="kicker">The Campaign Library &nbsp;&middot;&nbsp; Finances &nbsp;&middot;&nbsp; Volume Two</div>
    <div class="cover-rule"></div>
    <h1>The <em>Finances</em><br>Collection</h1>
    <div class="sub">Five more forty-day campaigns \u2014 meeting your people in the deeper places money touches: the heart, their health, their fear, their meaning, and their peace.</div>
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
    <h2>The hardest money problems<br>aren\u2019t on the <em>spreadsheet</em>.</h2>
    <p class="lead">For most people, the deepest financial struggles are matters of the heart \u2014 fear, meaning, shame, surrender, and the slow erosion of healthy habits. <strong>The Finances Collection, Volume Two goes there.</strong> Each of these five campaigns takes one of money\u2019s most personal challenges and walks your people through forty unhurried days toward a genuinely freer relationship with what they have.</p>
    <div class="howrow">
      <div class="howcard"><div class="hn">40</div><h4>A Daily Rhythm</h4><p>Every day offers a short reading, one practical step, a spiritual-partner check-in, and a written prayer &mdash; small, repeatable, and easy to keep.</p></div>
      <div class="howcard"><div class="hn">6</div><h4>A Weekly Gathering</h4><p>Six group sessions give the journey its backbone, turning private change into shared momentum across your church or team.</p></div>
      <div class="howcard"><div class="hn">1</div><h4>A Clear Outcome</h4><p>Each campaign is built around one transformation &mdash; so your people don\u2019t just learn about money, they actually change how they live with it.</p></div>
    </div>
    <div class="contents">
      <div class="ct">Inside This Volume</div>
      <div class="clist">
        <div class="cli"><span class="cnum">06</span><span><span class="cnm">God, Money &amp; Me</span><br><span class="cds">Settle the question of lordship</span></span></div>
        <div class="cli"><span class="cnum">07</span><span><span class="cnm">Financial Health</span><br><span class="cds">Wellness through small, steady habits</span></span></div>
        <div class="cli"><span class="cnum">08</span><span><span class="cnm">Breaking Financial Fear</span><br><span class="cds">Trade scarcity and dread for courage</span></span></div>
        <div class="cli"><span class="cnum">09</span><span><span class="cnm">Money and Meaning</span><br><span class="cds">Connect money to what truly matters</span></span></div>
        <div class="cli"><span class="cnum">10</span><span><span class="cnm">Peace with Money</span><br><span class="cds">End the war; live content and free</span></span></div>
      </div>
    </div>
  </div>
</div>"""

closing = """
<div class="page close">
  <div class="frame"></div>
  <div class="close-inner">
    <div class="kicker">Ready When You Are</div>
    <h2>Meet your people where<br>money <em>really</em> lives.</h2>
    <p class="cp">These five campaigns reach past the budget to the beliefs underneath it. Choose the one that names what your church or team is quietly carrying \u2014 or run them across a season \u2014 and give your people a hope-filled, forty-day path to real freedom with money.</p>
    <div class="close-list">
      <div class="cl-row"><span class="cln">06</span><span class="clt">God, Money &amp; Me</span><span class="cld">Lordship &amp; surrender</span></div>
      <div class="cl-row"><span class="cln">07</span><span class="clt">Financial Health</span><span class="cld">Habits &amp; wholeness</span></div>
      <div class="cl-row"><span class="cln">08</span><span class="clt">Breaking Financial Fear</span><span class="cld">Courage over scarcity</span></div>
      <div class="cl-row"><span class="cln">09</span><span class="clt">Money and Meaning</span><span class="cld">Purpose &amp; legacy</span></div>
      <div class="cl-row"><span class="cln">10</span><span class="clt">Peace with Money</span><span class="cld">Contentment &amp; grace</span></div>
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
<title>The Finances Collection, Volume Two \u2014 Lifetogether</title>
<style>{FONTS}</style>
<style>{CSS}</style>
</head><body>{pages}</body></html>"""

pathlib.Path("/tmp/finances_v2.html").write_text(doc, encoding="utf-8")
print("HTML written:", len(doc), "chars")
