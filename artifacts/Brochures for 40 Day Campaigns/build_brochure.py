# -*- coding: utf-8 -*-
import pathlib, html

FONTS = pathlib.Path("/tmp/fonts_embed.css").read_text()

# ---------------------------------------------------------------- DATA
campaigns = [
{
 "num":"01","accent":"#b3892f","accent_soft":"#f0e4c8",
 "title_a":"Faith &","title_b":"Finances",
 "subtitle":"Bringing your faith into every financial decision",
 "problem":"For many of us, faith and money live in two different rooms. We worship on Sunday and worry on Monday, never letting what we believe touch what we spend. Money quietly becomes the one corner of life God is asked to stay out of.",
 "promise":"Faith &amp; Finances tears down the wall between belief and bank account. Over forty days your people learn to make every decision \u2014 saving, spending, giving, owing \u2014 an act of worship, until their money finally tells the truth about what they love.",
 "verse":"For where your treasure is, there your heart will be also.",
 "ref":"Matthew 6:21 (NIV)",
 "bigidea":"Your bank statement is a spiritual document. How you handle money reveals \u2014 and reshapes \u2014 what your heart actually trusts.",
 "tags":["Faith Integration","Worship","Trust","Money &amp; the Heart","Discipleship"],
 "best_for":"Church &amp; Company","backbone":"Matthew 6:19\u201324","metaphor":"Treasure &amp; the Heart","felt":"Money stress, simplicity, integrating faith",
 "sessions":[
   ("1","Two Masters","Why you cannot serve both God and money \u2014 and why pretending you can leaves you exhausted."),
   ("2","Follow the Treasure","Tracing what your spending quietly reveals about what you truly worship."),
   ("3","Worship with Your Wallet","Turning ordinary transactions into deliberate acts of trust."),
   ("4","The Anxiety Antidote","How faith dismantles the fear that drives so many money decisions."),
   ("5","Open Hands","Moving from gripping to giving as the natural overflow of trust."),
   ("6","A Whole Life","Carrying Sunday faith into Monday\u2019s budget \u2014 for good."),
 ],
 "journey":"Each of the 40 days offers a short reading, one practical money step, a spiritual-partner check-in, and a written prayer \u2014 a daily rhythm that slowly rewires how your people see all they own.",
 "why":"Nothing exposes the real condition of our faith faster than how we handle a dollar \u2014 and nothing transforms a life faster than surrendering it.",
 "cta":"Launch Faith &amp; Finances and help your people stop living divided.",
 "note":None,
},
{
 "num":"02","accent":"#245a45","accent_soft":"#d8e7df",
 "title_a":"Financial","title_b":"Wisdom",
 "subtitle":"The learnable skill of making consistently wise money decisions",
 "problem":"Plenty of capable, well-meaning people make poor money decisions \u2014 not for lack of income, but for lack of a plan. We react instead of prepare, guess instead of know, and mistake good intentions for good outcomes.",
 "promise":"Financial Wisdom hands your people the practical, time-tested skill of deciding well. Over forty days they trade impulse for foresight, learning the proverbs and habits that turn scattered money into a stable, well-built life.",
 "verse":"The plans of the diligent lead to profit as surely as haste leads to poverty.",
 "ref":"Proverbs 21:5 (NIV)",
 "bigidea":"Wisdom is the bridge between good intentions and good outcomes. You don\u2019t drift into financial health \u2014 you build it, one wise decision at a time.",
 "tags":["Proverbs","Planning","Decision-Making","Diligence","Foresight"],
 "best_for":"Church &amp; Company","backbone":"Proverbs 21:5; 6:6\u20138","metaphor":"The Wise Builder","felt":"Budgeting, debt, money decisions",
 "sessions":[
   ("1","The House Wisdom Builds","Why the skill of deciding well is the foundation everything else rests on."),
   ("2","Learn from the Ant","The quiet power of foresight, preparation, and small consistent steps."),
   ("3","Plans, Not Panic","Replacing reactive money habits with a simple, written plan."),
   ("4","The Counsel of Many","How wise people borrow wisdom from others before they decide."),
   ("5","The Trap of Haste","Recognizing the impulse decisions that quietly drain a life."),
   ("6","Built to Last","Turning forty days of good decisions into lifelong habits."),
 ],
 "journey":"Forty daily entries pair a proverb with one concrete decision to practice \u2014 a small, repeatable act of wisdom that compounds over six weeks into a noticeably different financial life.",
 "why":"The gap between the life people want and the life they have is almost always a gap in wisdom \u2014 and wisdom can be learned.",
 "cta":"Launch Financial Wisdom and give your people the skill no one taught them.",
 "note":None,
},
{
 "num":"03","accent":"#1f6b6b","accent_soft":"#d3e7e7",
 "title_a":"Money Made","title_b":"Simple",
 "subtitle":"Cutting through the complexity to find real peace",
 "problem":"Money has never felt more complicated. Endless accounts, apps, subscriptions, and statements pile up until the whole thing feels too overwhelming to even look at \u2014 so we avoid it, and the chaos quietly grows.",
 "promise":"Money Made Simple clears the clutter. Over forty days your people build one plan they can actually follow, discover the freedom of living with margin, and learn the ancient secret no complexity can buy: enough really is enough.",
 "verse":"But godliness with contentment is great gain.",
 "ref":"1 Timothy 6:6 (NIV)",
 "bigidea":"Simplicity isn\u2019t deprivation \u2014 it\u2019s freedom. When you stop chasing more and start managing what you have, money finally gets quiet.",
 "tags":["Simplicity","Contentment","Budgeting","Margin","Clarity"],
 "best_for":"Church &amp; Company","backbone":"1 Timothy 6:6\u201310","metaphor":"Margin &amp; the Cleared Table","felt":"Overwhelm, budgeting, simplicity",
 "sessions":[
   ("1","The Cost of Complicated","Why financial chaos quietly drains your energy and your joy."),
   ("2","Enough","Rediscovering contentment in a culture that always whispers \u201cmore.\u201d"),
   ("3","One Simple Plan","Building a budget so clear your people will actually use it."),
   ("4","The Power of Margin","Creating the breathing room that turns stress into peace."),
   ("5","Cutting the Clutter","Simplifying accounts, subscriptions, and the noise that hides the numbers."),
   ("6","Free to Live","What becomes possible when money stops shouting."),
 ],
 "journey":"Each day removes one source of financial noise and adds one simple step toward clarity \u2014 so by day forty, your people aren\u2019t merely more disciplined, they\u2019re more free.",
 "why":"Most people don\u2019t need a more complicated system. They need a simpler one they\u2019ll actually keep.",
 "cta":"Launch Money Made Simple and trade your people\u2019s overwhelm for margin.",
 "note":None,
},
{
 "num":"04","accent":"#345f8e","accent_soft":"#d7e2ee",
 "title_a":"Financial","title_b":"Peace",
 "subtitle":"Releasing the fear and finding rest with money",
 "problem":"For millions, money is the last thing they think about at night and the first thing they dread in the morning. It isn\u2019t always about the amount \u2014 it\u2019s the low, constant hum of worry that no balance ever seems to silence.",
 "promise":"Financial Peace addresses the fear beneath the figures. Over forty days your people learn to break the worry cycle, anchor their security in something steadier than a balance, and build a calm relationship with money that doesn\u2019t rise and fall with the markets.",
 "verse":"And the peace of God, which transcends all understanding, will guard your hearts and your minds in Christ Jesus.",
 "ref":"Philippians 4:7 (NIV)",
 "bigidea":"Peace isn\u2019t the absence of bills \u2014 it\u2019s the presence of trust. You can have little and rest deeply, or have plenty and never sleep.",
 "tags":["Peace","Anxiety","Trust","Rest","Security"],
 "best_for":"Church &amp; Company","backbone":"Matthew 6:25\u201334","metaphor":"Stilled Waters","felt":"Money stress, anxiety, fear",
 "sessions":[
   ("1","The Weight We Carry","Naming the quiet dread money creates \u2014 without shame."),
   ("2","Consider the Birds","What Jesus\u2019 words about worry mean for your bank account."),
   ("3","Breaking the Cycle","Practical steps to interrupt anxious money thinking."),
   ("4","A Steadier Security","Anchoring your peace in something the markets can\u2019t move."),
   ("5","One Day at a Time","Trading tomorrow\u2019s \u201cwhat ifs\u201d for today\u2019s faithfulness."),
   ("6","Rest","Building a calm relationship with money that outlasts forty days."),
 ],
 "journey":"Every day offers a short reading, a calming practice, and a prayer crafted to quiet the mind and steady the heart \u2014 small daily deposits of peace over six unhurried weeks.",
 "why":"Financial worry steals more sleep, joy, and presence than almost anything else \u2014 and your people were never meant to carry it alone.",
 "cta":"Launch Financial Peace and help your people finally exhale.",
 "note":"A gentle note: This campaign offers spiritual and practical encouragement and is not a substitute for professional financial or mental-health advice. Anyone in acute distress is warmly encouraged to reach out to a trusted counselor or advisor.",
},
{
 "num":"05","accent":"#a5632f","accent_soft":"#efddca",
 "title_a":"Wise with","title_b":"Money",
 "subtitle":"Becoming a faithful manager of all you\u2019ve been given",
 "problem":"Most of us live as owners \u2014 as if our money is ours to spend however we please, with no one to answer to and no larger plan. But ownership is a heavy, anxious posture, and it rarely leads anywhere generous.",
 "promise":"Wise with Money reframes the whole relationship: you are not an owner but a manager, entrusted with resources for a purpose bigger than yourself. Over forty days your people learn to steward what they have with confidence \u2014 and to taste the deep joy of giving it away.",
 "verse":"Whoever can be trusted with very little can also be trusted with much.",
 "ref":"Luke 16:10 (NIV)",
 "bigidea":"It was never yours to own \u2014 only yours to steward. And the faithful manager, not the anxious owner, is the one who finally gets to enjoy it.",
 "tags":["Stewardship","Generosity","Faithfulness","The Long Game","Giving"],
 "best_for":"Church &amp; Company","backbone":"Matthew 25:14\u201330","metaphor":"The Faithful Steward","felt":"Stewardship, generosity, purpose",
 "sessions":[
   ("1","Owner or Manager?","The single shift that changes everything about money."),
   ("2","Faithful with Little","Why how you handle small amounts decides what you\u2019re trusted with."),
   ("3","Investing the Talents","Putting what you\u2019ve been given to work \u2014 not burying it in fear."),
   ("4","The Long Game","Thinking past this month toward a life and legacy that lasts."),
   ("5","The Joy of Generosity","Discovering that giving is the steward\u2019s greatest reward."),
   ("6","Well Done","Living for the words every faithful manager longs to hear."),
 ],
 "journey":"Each of the forty days pairs a stewardship principle with one act of faithful management or generosity \u2014 turning a six-week campaign into a lifelong identity.",
 "why":"The goal was never simply to have more, but to hear \u201cwell done\u201d \u2014 and to become the kind of person money can flow through, not just to.",
 "cta":"Launch Wise with Money and trade ownership\u2019s anxiety for the steward\u2019s joy.",
 "note":None,
},
]

# ---------------------------------------------------------------- CSS
CSS = """
*{margin:0;padding:0;box-sizing:border-box;-webkit-print-color-adjust:exact;print-color-adjust:exact;}
:root{
 --navy:#11243f; --navy2:#0b1a30; --cream:#f7f3ea; --cream2:#efe7d6;
 --ink:#22303f; --gold:#c19a4b; --gold-d:#a87f33; --line:#d9cfb8;
}
@page{ size:A4; margin:0; }
html,body{ background:#2a2f38; font-family:'Spectral',serif; color:var(--ink); }
.page{ position:relative; width:210mm; height:297mm; overflow:hidden;
 page-break-after:always; background:var(--cream); }
.page:last-child{ page-break-after:auto; }

/* frame */
.frame{ position:absolute; inset:10mm; border:1px solid var(--line);
 outline:3px solid var(--line); outline-offset:3px; pointer-events:none; }
.frame.gold{ border-color:rgba(193,154,75,.55); outline-color:rgba(193,154,75,.35); }

.kicker{ font-family:'Archivo',sans-serif; font-weight:600; letter-spacing:.34em;
 text-transform:uppercase; font-size:8.2pt; }
.serif{ font-family:'Playfair Display',serif; }

/* ============ COVER ============ */
.cover{ background:radial-gradient(120% 90% at 50% 0%, #1c3357 0%, transparent 60%),
 linear-gradient(155deg,#15294a 0%,#0c1c34 55%,#0a1727 100%); color:#f3ecdb; }
.cover .frame{ inset:9mm; border-color:rgba(193,154,75,.5); outline-color:rgba(193,154,75,.3); }
.cover-inner{ position:absolute; inset:9mm; display:flex; flex-direction:column;
 align-items:center; text-align:center; padding:24mm 20mm; }
.cover .kicker{ color:var(--gold); margin-top:6mm; }
.cover-rule{ width:54px; height:2px; background:var(--gold); margin:9mm auto; opacity:.9; }
.cover h1{ font-family:'Playfair Display',serif; font-weight:800; font-size:50pt;
 line-height:1.02; letter-spacing:-.01em; margin:2mm 0; }
.cover h1 em{ font-style:italic; color:var(--gold); }
.cover .sub{ font-family:'Spectral',serif; font-style:italic; font-size:14.5pt;
 line-height:1.55; color:#d9d0bd; max-width:135mm; margin:10mm auto 0; }
.cover-foot{ margin-top:auto; width:100%; }
.stats{ display:flex; justify-content:center; gap:0; align-items:stretch;
 border-top:1px solid rgba(193,154,75,.35); border-bottom:1px solid rgba(193,154,75,.35);
 padding:6mm 0; margin-bottom:8mm; }
.stat{ flex:1; padding:0 4mm; border-right:1px solid rgba(193,154,75,.22); }
.stat:last-child{ border-right:none; }
.stat .n{ font-family:'Playfair Display',serif; font-size:24pt; color:var(--gold); line-height:1; }
.stat .l{ font-family:'Archivo',sans-serif; font-size:6.6pt; letter-spacing:.22em;
 text-transform:uppercase; color:#c8bfa9; margin-top:3mm; }
.cover .tier{ font-family:'Archivo',sans-serif; font-size:7.6pt; letter-spacing:.3em;
 text-transform:uppercase; color:#b7ac93; }
.brandmark{ font-family:'Archivo',sans-serif; font-weight:700; letter-spacing:.42em;
 text-transform:uppercase; font-size:8.5pt; color:var(--gold); }

/* ============ INTRO ============ */
.intro-inner{ position:absolute; inset:10mm; padding:20mm 20mm; display:flex; flex-direction:column; }
.intro .kicker{ color:var(--gold-d); }
.intro h2{ font-family:'Playfair Display',serif; font-weight:800; font-size:33pt;
 line-height:1.06; margin:7mm 0 0; color:var(--navy); }
.intro h2 em{ font-style:italic; color:var(--gold-d); }
.lead{ font-size:12.5pt; line-height:1.7; color:#3c4654; margin-top:8mm; max-width:150mm; }
.lead strong{ color:var(--navy); font-weight:600; }
.howrow{ display:flex; gap:7mm; margin-top:11mm; }
.howcard{ flex:1; background:#fff; border:1px solid var(--line); padding:7mm 6mm; position:relative; }
.howcard .hn{ font-family:'Playfair Display',serif; font-size:20pt; color:var(--gold-d); line-height:1; }
.howcard h4{ font-family:'Archivo',sans-serif; font-weight:700; font-size:9pt; letter-spacing:.06em;
 text-transform:uppercase; color:var(--navy); margin:4mm 0 3mm; }
.howcard p{ font-size:9.6pt; line-height:1.55; color:#56606d; }
.contents{ margin-top:auto; border-top:2px solid var(--navy); padding-top:6mm; }
.contents .ct{ font-family:'Archivo',sans-serif; font-weight:700; letter-spacing:.24em;
 text-transform:uppercase; font-size:8pt; color:var(--gold-d); margin-bottom:5mm; }
.clist{ display:grid; grid-template-columns:1fr 1fr; gap:3.5mm 12mm; }
.cli{ display:flex; gap:5mm; align-items:baseline; }
.cli .cnum{ font-family:'Playfair Display',serif; font-size:12pt; color:var(--gold-d); width:9mm; }
.cli .cnm{ font-family:'Playfair Display',serif; font-weight:700; font-size:12pt; color:var(--navy); }
.cli .cds{ font-style:italic; font-size:9.4pt; color:#6a7480; }

/* ============ CAMPAIGN SPREAD ============ */
.camp-inner{ position:absolute; inset:10mm; padding:13mm 13mm 11mm; display:flex; flex-direction:column; }
.bignum{ position:absolute; top:6mm; right:12mm; font-family:'Playfair Display',serif;
 font-weight:900; font-size:150pt; line-height:.8; color:var(--accent); opacity:.085; z-index:0; }
.camp-head{ position:relative; z-index:1; }
.camp-kicker{ color:var(--accent); }
.camp-title{ font-family:'Playfair Display',serif; font-weight:800; font-size:40pt;
 line-height:.98; letter-spacing:-.01em; color:var(--navy); margin-top:4mm; }
.camp-title em{ font-style:italic; color:var(--accent); }
.camp-sub{ font-style:italic; font-size:12.5pt; color:#5c6672; margin-top:3.5mm; }
.accent-rule{ width:46px; height:3px; background:var(--accent); margin:6mm 0 0; }

.body-grid{ display:flex; gap:9mm; margin-top:8mm; position:relative; z-index:1; }
.main-col{ flex:1.85; min-width:0; }
.side-col{ flex:1; min-width:0; }

.section-label{ font-family:'Archivo',sans-serif; font-weight:700; letter-spacing:.2em;
 text-transform:uppercase; font-size:8pt; color:var(--accent); margin-bottom:2.5mm; }
.section-body{ font-size:10.4pt; line-height:1.62; color:#3f4956; }
.pp-block{ margin-bottom:6mm; }

.scripture{ background:var(--navy); color:#f1ead9; padding:7mm 7mm 6mm; margin:1mm 0 6mm;
 position:relative; }
.scripture::before{ content:"\\201C"; font-family:'Playfair Display',serif; font-size:46pt;
 color:var(--gold); position:absolute; top:-2mm; left:4mm; opacity:.5; }
.scripture .v{ font-family:'Playfair Display',serif; font-style:italic; font-size:13pt;
 line-height:1.5; padding-left:9mm; }
.scripture .r{ font-family:'Archivo',sans-serif; font-size:7.4pt; letter-spacing:.22em;
 text-transform:uppercase; color:var(--gold); margin-top:4mm; padding-left:9mm; }

.bigidea{ border-left:3px solid var(--accent); background:var(--accent-soft);
 padding:5mm 6mm; margin-bottom:6mm; }
.bigidea .bl{ font-family:'Archivo',sans-serif; font-weight:700; letter-spacing:.2em;
 text-transform:uppercase; font-size:7.4pt; color:var(--accent); margin-bottom:2.5mm; }
.bigidea p{ font-family:'Playfair Display',serif; font-size:12pt; line-height:1.45; color:var(--navy); }

.tags{ display:flex; flex-wrap:wrap; gap:2.5mm; }
.tag{ font-family:'Archivo',sans-serif; font-size:7.4pt; font-weight:500; letter-spacing:.08em;
 text-transform:uppercase; color:var(--accent); border:1px solid var(--accent);
 border-radius:20px; padding:1.6mm 3.5mm; }

/* sidebar card */
.infocard{ background:#fff; border:1px solid var(--line); }
.infocard .ih{ background:var(--navy); color:#f1ead9; padding:4.5mm 6mm;
 font-family:'Archivo',sans-serif; font-weight:700; letter-spacing:.2em; text-transform:uppercase; font-size:8pt; }
.inforow{ padding:4mm 6mm; border-bottom:1px solid var(--cream2); }
.inforow:last-child{ border-bottom:none; }
.inforow .il{ font-family:'Archivo',sans-serif; font-weight:600; letter-spacing:.14em;
 text-transform:uppercase; font-size:6.8pt; color:#9aa3ad; margin-bottom:1.5mm; }
.inforow .iv{ font-family:'Playfair Display',serif; font-size:11pt; color:var(--navy); line-height:1.25; }
.inforow .iv.sm{ font-family:'Spectral',serif; font-size:9.6pt; font-style:italic; color:#54606c; }

.note{ margin-top:5mm; background:var(--accent-soft); border:1px solid var(--accent);
 padding:4mm 5mm; font-size:8.4pt; line-height:1.5; color:#4a5360; font-style:italic; }
.note b{ font-style:normal; font-family:'Archivo',sans-serif; font-weight:700;
 letter-spacing:.04em; color:var(--accent); }

/* sessions */
.curric{ margin-top:7mm; position:relative; z-index:1; }
.curric-head{ display:flex; align-items:baseline; justify-content:space-between;
 border-top:2px solid var(--navy); padding-top:4mm; margin-bottom:4.5mm; }
.curric-head .ch{ font-family:'Archivo',sans-serif; font-weight:700; letter-spacing:.2em;
 text-transform:uppercase; font-size:8.5pt; color:var(--navy); }
.curric-head .cmeta{ font-family:'Archivo',sans-serif; font-size:7.2pt; letter-spacing:.18em;
 text-transform:uppercase; color:var(--accent); }
.sgrid{ display:grid; grid-template-columns:1fr 1fr 1fr; gap:4mm; }
.scard{ border:1px solid var(--line); background:#fff; padding:4.5mm 4.5mm; position:relative; }
.scard .sn{ font-family:'Playfair Display',serif; font-weight:800; font-size:13pt; color:var(--accent); }
.scard .st{ font-family:'Playfair Display',serif; font-weight:700; font-size:10.6pt;
 color:var(--navy); line-height:1.15; margin:1.5mm 0 2mm; }
.scard .sd{ font-size:8.4pt; line-height:1.45; color:#5d6772; }

/* footer band */
.foot-band{ margin-top:auto; display:flex; gap:7mm; align-items:flex-end;
 border-top:1px solid var(--line); padding-top:5mm; position:relative; z-index:1; }
.foot-why{ flex:1.6; }
.foot-why .fl{ font-family:'Archivo',sans-serif; font-weight:700; letter-spacing:.2em;
 text-transform:uppercase; font-size:7.2pt; color:var(--accent); margin-bottom:2mm; }
.foot-why p{ font-size:9.6pt; line-height:1.55; color:#4a5360; font-style:italic; }
.foot-cta{ flex:1; text-align:right; }
.foot-cta .ct{ display:inline-block; background:var(--accent); color:#fff;
 font-family:'Archivo',sans-serif; font-weight:600; font-size:8.4pt; letter-spacing:.05em;
 padding:3.5mm 6mm; line-height:1.35; text-align:left; }

/* ============ CLOSING ============ */
.close{ background:linear-gradient(160deg,#15294a 0%,#0b1a30 100%); color:#f3ecdb; }
.close .frame{ border-color:rgba(193,154,75,.5); outline-color:rgba(193,154,75,.3); }
.close-inner{ position:absolute; inset:10mm; padding:26mm 22mm; display:flex;
 flex-direction:column; text-align:center; align-items:center; }
.close .kicker{ color:var(--gold); }
.close h2{ font-family:'Playfair Display',serif; font-weight:800; font-size:40pt;
 line-height:1.04; margin:8mm 0 0; }
.close h2 em{ font-style:italic; color:var(--gold); }
.close .cp{ font-family:'Spectral',serif; font-size:13pt; font-style:italic; line-height:1.65;
 color:#d8cfbc; max-width:140mm; margin:9mm auto 0; }
.close-list{ margin:12mm auto 0; width:100%; max-width:150mm; }
.cl-row{ display:flex; align-items:baseline; gap:6mm; padding:3.5mm 0;
 border-bottom:1px solid rgba(193,154,75,.25); text-align:left; }
.cl-row .cln{ font-family:'Playfair Display',serif; font-size:14pt; color:var(--gold); width:9mm; }
.cl-row .clt{ font-family:'Playfair Display',serif; font-weight:700; font-size:14pt; color:#f3ecdb; flex:1; }
.cl-row .cld{ font-style:italic; font-size:9.6pt; color:#b9b09b; }
.close-cta{ margin-top:13mm; }
.close-cta .btn{ display:inline-block; background:var(--gold); color:#11243f;
 font-family:'Archivo',sans-serif; font-weight:700; letter-spacing:.12em; text-transform:uppercase;
 font-size:9.5pt; padding:4.5mm 12mm; }
.close-foot{ margin-top:auto; padding-top:10mm; }
.close-foot .niv{ font-family:'Archivo',sans-serif; font-size:7pt; letter-spacing:.24em;
 text-transform:uppercase; color:#a89e87; margin-bottom:4mm; }
"""

def tag_html(tags):
    return "".join(f'<span class="tag">{t}</span>' for t in tags)

def sessions_html(ss):
    return "".join(
        f'<div class="scard"><div class="sn">{n}</div><div class="st">{html.escape(t)}</div><div class="sd">{d}</div></div>'
        for (n,t,d) in ss)

def campaign_page(c):
    note = f'<div class="note"><b>{c["note"].split(":")[0]}:</b> {c["note"].split(":",1)[1].strip()}</div>' if c["note"] else ""
    return f"""
<div class="page" style="--accent:{c['accent']};--accent-soft:{c['accent_soft']};">
  <div class="frame"></div>
  <div class="camp-inner">
    <div class="bignum">{c['num']}</div>
    <div class="camp-head">
      <div class="kicker camp-kicker">Finances &nbsp;&middot;&nbsp; Tier 1 &nbsp;&middot;&nbsp; Church + Company</div>
      <h1 class="camp-title">{c['title_a']} <em>{c['title_b']}</em></h1>
      <div class="camp-sub">{c['subtitle']}</div>
      <div class="accent-rule"></div>
    </div>
    <div class="body-grid">
      <div class="main-col">
        <div class="pp-block">
          <div class="section-label">The Problem</div>
          <div class="section-body">{c['problem']}</div>
        </div>
        <div class="pp-block">
          <div class="section-label">The Promise</div>
          <div class="section-body">{c['promise']}</div>
        </div>
        <div class="scripture">
          <div class="v">{c['verse']}</div>
          <div class="r">{c['ref']}</div>
        </div>
        <div class="bigidea">
          <div class="bl">The Big Idea</div>
          <p>{c['bigidea']}</p>
        </div>
        <div class="tags">{tag_html(c['tags'])}</div>
      </div>
      <div class="side-col">
        <div class="infocard">
          <div class="ih">Campaign Details</div>
          <div class="inforow"><div class="il">Best For</div><div class="iv">{c['best_for']}</div></div>
          <div class="inforow"><div class="il">Format</div><div class="iv">40 Days &middot; 6 Sessions</div></div>
          <div class="inforow"><div class="il">Scripture Backbone</div><div class="iv">{c['backbone']}</div></div>
          <div class="inforow"><div class="il">Guiding Metaphor</div><div class="iv">{c['metaphor']}</div></div>
          <div class="inforow"><div class="il">Felt Need</div><div class="iv sm">{c['felt']}</div></div>
        </div>
        {note}
      </div>
    </div>
    <div class="curric">
      <div class="curric-head">
        <div class="ch">The Six-Session Journey</div>
        <div class="cmeta">One session per week &middot; six weeks</div>
      </div>
      <div class="sgrid">{sessions_html(c['sessions'])}</div>
    </div>
    <div class="foot-band">
      <div class="foot-why">
        <div class="fl">Why It Matters</div>
        <p>{c['why']}</p>
      </div>
      <div class="foot-cta"><span class="ct">{c['cta']}</span></div>
    </div>
  </div>
</div>"""

# cover
cover = """
<div class="page cover">
  <div class="frame gold"></div>
  <div class="cover-inner">
    <div class="brandmark">Lifetogether</div>
    <div class="kicker">The Campaign Library &nbsp;&middot;&nbsp; Finances Collection</div>
    <div class="cover-rule"></div>
    <h1>The <em>Finances</em><br>Collection</h1>
    <div class="sub">Five forty-day campaigns to help your people overcome debt, budgeting stress, and money anxiety &mdash; and find wisdom, peace, simplicity, and freedom.</div>
    <div class="cover-foot">
      <div class="stats">
        <div class="stat"><div class="n">5</div><div class="l">Campaigns</div></div>
        <div class="stat"><div class="n">40</div><div class="l">Day Journey</div></div>
        <div class="stat"><div class="n">6</div><div class="l">Sessions Each</div></div>
        <div class="stat"><div class="n">NIV</div><div class="l">Scripture</div></div>
      </div>
      <div class="tier">Tier 1 &nbsp;&middot;&nbsp; For Churches &amp; Companies</div>
    </div>
  </div>
</div>"""

# intro
intro = """
<div class="page intro">
  <div class="frame"></div>
  <div class="intro-inner">
    <div class="kicker">Before You Begin</div>
    <h2>Money is the conversation<br>most people are <em>afraid</em> to have.</h2>
    <p class="lead">It quietly shapes our marriages, our sleep, our sense of security, and our walk with God &mdash; yet it remains the one area many of us never bring into the light. <strong>The Finances Collection changes that.</strong> Each campaign takes a single, honest struggle &mdash; fear, complexity, foolish habits, a divided heart, an ownership mindset &mdash; and walks your people through forty unhurried days toward a genuinely different relationship with money.</p>
    <div class="howrow">
      <div class="howcard"><div class="hn">40</div><h4>A Daily Rhythm</h4><p>Every day offers a short reading, one practical step, a spiritual-partner check-in, and a written prayer &mdash; small, repeatable, and easy to keep.</p></div>
      <div class="howcard"><div class="hn">6</div><h4>A Weekly Gathering</h4><p>Six group sessions give the journey its backbone, turning private change into shared momentum across your church or team.</p></div>
      <div class="howcard"><div class="hn">1</div><h4>A Clear Outcome</h4><p>Each campaign is built around one transformation &mdash; so your people don\u2019t just learn about money, they actually change how they live with it.</p></div>
    </div>
    <div class="contents">
      <div class="ct">Inside This Collection</div>
      <div class="clist">
        <div class="cli"><span class="cnum">01</span><span><span class="cnm">Faith &amp; Finances</span><br><span class="cds">Bring faith into every money decision</span></span></div>
        <div class="cli"><span class="cnum">02</span><span><span class="cnm">Financial Wisdom</span><br><span class="cds">The learnable skill of deciding well</span></span></div>
        <div class="cli"><span class="cnum">03</span><span><span class="cnm">Money Made Simple</span><br><span class="cds">Trade complexity for clarity and margin</span></span></div>
        <div class="cli"><span class="cnum">04</span><span><span class="cnm">Financial Peace</span><br><span class="cds">Release the fear, find rest with money</span></span></div>
        <div class="cli"><span class="cnum">05</span><span><span class="cnm">Wise with Money</span><br><span class="cds">Steward all you\u2019ve been given, generously</span></span></div>
      </div>
    </div>
  </div>
</div>"""

# closing
closing = """
<div class="page close">
  <div class="frame"></div>
  <div class="close-inner">
    <div class="kicker">Ready When You Are</div>
    <h2>Help your people find<br><em>freedom</em> with money.</h2>
    <p class="cp">Pick the campaign that meets your church or team where they are today &mdash; or run all five across a season. However you begin, you\u2019ll be giving your people something they rarely receive: an honest, hope-filled, forty-day path to a healthier relationship with money.</p>
    <div class="close-list">
      <div class="cl-row"><span class="cln">01</span><span class="clt">Faith &amp; Finances</span><span class="cld">Money &amp; the heart</span></div>
      <div class="cl-row"><span class="cln">02</span><span class="clt">Financial Wisdom</span><span class="cld">Deciding well</span></div>
      <div class="cl-row"><span class="cln">03</span><span class="clt">Money Made Simple</span><span class="cld">Clarity &amp; margin</span></div>
      <div class="cl-row"><span class="cln">04</span><span class="clt">Financial Peace</span><span class="cld">Rest &amp; trust</span></div>
      <div class="cl-row"><span class="cln">05</span><span class="clt">Wise with Money</span><span class="cld">Steward &amp; give</span></div>
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
<title>The Finances Collection \u2014 Lifetogether</title>
<style>{FONTS}</style>
<style>{CSS}</style>
</head><body>{pages}</body></html>"""

pathlib.Path("/tmp/finances_brochure.html").write_text(doc, encoding="utf-8")
# also a clean copy for outputs (same file)
print("HTML written:", len(doc), "chars")
