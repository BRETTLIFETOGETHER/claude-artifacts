# -*- coding: utf-8 -*-
import json, html
with open("fonts_b64.json") as f: F=json.load(f)
def esc(s): return html.escape(s, quote=True)

def hex2rgb(h):
    h=h.lstrip('#'); return tuple(int(h[i:i+2],16) for i in (0,2,4))
def rgb2hex(t): return '#%02x%02x%02x'%tuple(max(0,min(255,int(round(x))))for x in t)
def mix(h,o,t):
    a=hex2rgb(h);b=hex2rgb(o);return rgb2hex(tuple(a[i]+(b[i]-a[i])*t for i in range(3)))
def darken(h,t): return mix(h,'#000000',t)
def lighten(h,t): return mix(h,'#ffffff',t)

GOLD="#b08a3e"; GOLD_L="#c9a44e"; INK="#2b2622"; CREAM="#f6f1e7"; PAPER="#fbf8f1"; TAN="#f1e6cd"
C   = "#22335c"                 # deep sapphire / indigo — "wisdom"
DARK= darken(C,0.16); DEEP=darken(C,0.34); TINT=lighten(C,0.92)

FONT_CSS=f"""
@font-face{{font-family:'Playfair';font-weight:400 900;font-style:normal;src:url(data:font/ttf;base64,{F['Playfair']}) format('truetype');}}
@font-face{{font-family:'Playfair';font-weight:400 900;font-style:italic;src:url(data:font/ttf;base64,{F['PlayfairItalic']}) format('truetype');}}
@font-face{{font-family:'Garamond';font-weight:400 800;font-style:normal;src:url(data:font/ttf;base64,{F['Garamond']}) format('truetype');}}
@font-face{{font-family:'Garamond';font-weight:400 800;font-style:italic;src:url(data:font/ttf;base64,{F['GaramondItalic']}) format('truetype');}}
"""

DATA={
 "eyebrow":"LIFETOGETHER \u00b7 A 40-DAY CAMPAIGN & SMALL GROUP SERIES",
 "title":"Wisdom-Driven", "accent":"Life.",
 "category":"DISCERNMENT, DECISIONS & THE WELL-BUILT LIFE",
 "subhead":("We have never had more access to information \u2014 and never felt less sure of what "
            "to do with it. This is a 40-day journey out of reactive, anxious decision-making into "
            "a life quietly built on the wisdom that comes from God."),
 "pullquote":("\u201cKnowledge is knowing what is true. Wisdom is knowing what to do. One fills "
              "your head; the other builds your life.\u201d"),
 "body":("The Wisdom-Driven Life addresses the gap at the center of modern living: we have never had "
         "more information and never felt less certain of the next right step. Scripture insists "
         "that wisdom is not the same as intelligence, education, or data \u2014 it is the God-given "
         "skill of living well, of making the right call in the real, pressured, ordinary moments of "
         "a life. <b>A foolish person can know a great deal and still build an entire life on sand; "
         "a wise person fears the Lord, asks for help, seeks counsel, and builds on the rock.</b> "
         "This series gives a congregation the conviction and the daily practice to trade reactive, "
         "anxious living for a life driven by the wisdom that comes from above."),
 "scripture":("\u201cIf any of you lacks wisdom, you should ask God, who gives generously to all "
              "without finding fault, and it will be given to you.\u201d"),
 "scripture_ref":"\u2014 James 1:5 (NIV)",
 "subtitles":["A 40-Day Journey from Information to Wisdom",
              "Discovering God\u2019s Design for a Well-Built Life",
              "A 40-Day Path to Wiser Decisions, Words, and Relationships",
              "Building Your Life on the Wisdom That Comes from God"],
 "bigidea":("Wisdom is not the same as knowledge \u2014 it is the God-given skill of living well: "
            "fearing the Lord, asking Him for direction, weighing decisions, guarding our words, and "
            "building a life on the rock rather than the sand. The wise life is not the smartest "
            "life; it is the most surrendered one."),
 "tags":["fear of the Lord","discernment","decisions","wise counsel","James 1:5","the well-built life"],
 "info":[("Format","40-Day Journey + 6-Session Small Group"),
         ("Audience","All church \u2014 anyone facing decisions, change, or overwhelm"),
         ("Best Season","New Year \u00b7 Fall launch \u00b7 Any season"),
         ("Best For","Church \u00b7 Company \u00b7 Family"),
         ("Core Theme","Wisdom, discernment & godly decision-making"),
         ("Related Campaign","Pairs with Family Legacy by Design \u00b7 the wisdom transfer")],
 "sessions":[
  {"t":"Two Ways","a":"to Live",
   "s":"\u201cThe fear of the Lord is the beginning of wisdom, and knowledge of the Holy One is understanding.\u201d \u2014 Proverbs 9:10",
   "tags":["fear of the Lord","two paths","foundation","Proverbs 9","beginning"],
   "q":["Wisdom begins with the fear of the Lord \u2014 a reverent trust that He, not you, is God. Where is that trust strong in your life, and where is it thin?",
        "What is the difference between being smart and being wise? Name someone you\u2019d call truly wise \u2014 what marks their life?",
        "Where have you recently confused having information with actually knowing what to do?"],
   "step":"Before each decision this week, pause and ask one question: \u201cWhat would the fear of the Lord lead me to do here?\u201d"},
  {"t":"Ask","a":"for It",
   "s":"\u201cIf any of you lacks wisdom, you should ask God, who gives generously to all without finding fault.\u201d \u2014 James 1:5",
   "tags":["prayer","asking","dependence","James 1","humility"],
   "q":["James says wisdom is available simply for the asking. Why do we so rarely ask \u2014 and what does that reluctance reveal?",
        "Where are you currently leaning on your own understanding instead of asking God for wisdom?",
        "What decision are you facing right now that you have never actually prayed about?"],
   "step":"Name one decision you\u2019re facing and pray James 1:5 over it every day this week, watching for how God answers."},
  {"t":"Wisdom in","a":"the Decision",
   "s":"\u201cTrust in the Lord with all your heart and lean not on your own understanding \u2026 and he will make your paths straight.\u201d \u2014 Proverbs 3:5\u20136",
   "tags":["decisions","trust","discernment","Proverbs 3","guidance"],
   "q":["\u201cLean not on your own understanding.\u201d When has your own understanding led you wrong \u2014 and what would leaning on God have looked like?",
        "How do you usually make big decisions \u2014 by fear, by impulse, by what others think, or by seeking God? Be honest.",
        "What is one area where you sense God asking you to trust Him beyond what makes sense to you?"],
   "step":"Run one decision you\u2019re wrestling with through a simple grid this week: Is it wise? Is it loving? Does it honor God? Write your answers down."},
  {"t":"The Words","a":"of the Wise",
   "s":"\u201cThe wisdom that comes from heaven is first of all pure; then peace-loving, considerate \u2026 full of mercy.\u201d \u2014 James 3:17",
   "tags":["words","peace","James 3","gentleness","wisdom from above"],
   "q":["Heavenly wisdom is peace-loving and considerate \u2014 not just correct. Where are you \u201cright\u201d but not wise in how you speak?",
        "Wisdom balances truth and love. Which do you tend to drop under pressure \u2014 truth or love?",
        "What is one relationship where wiser words would change everything?"],
   "step":"Before speaking into anything tense this week, ask: \u201cIs it true? Is it kind? Is it the right time?\u201d Hold your words until all three are yes."},
  {"t":"Wisdom in","a":"Community",
   "s":"\u201cPlans fail for lack of counsel, but with many advisers they succeed.\u201d \u2014 Proverbs 15:22",
   "tags":["counsel","community","Proverbs 15","friendship","accountability"],
   "q":["Proverbs says plans fail without counsel. Who are the wise voices you actually invite into your decisions \u2014 and is that circle big enough?",
        "\u201cWalk with the wise and become wise.\u201d Who are you becoming like, based on who you spend the most time with?",
        "Where have you made an important decision in isolation that wise counsel might have changed?"],
   "step":"Identify one wise person and ask them for honest input on a real decision or area of your life this week."},
  {"t":"The Wise","a":"Builder","commit":True,
   "s":"\u201cEveryone who hears these words of mine and puts them into practice is like a wise man who built his house on the rock.\u201d \u2014 Matthew 7:24",
   "tags":["commitment","obedience","foundation","Matthew 7","well-built life"],
   "q":["Jesus says wisdom is not hearing truth but doing it. Where do you already know the wise thing \u2014 and simply need to do it?",
        "Integrity means your life looks the same on Tuesday as on Sunday. Where is the gap between what you know and how you live?",
        "After these 40 days, in what one area do you most want your life to become wisdom-driven?"],
   "commit":("Each person names one area of life \u2014 a decision, a relationship, a habit, a pattern of "
             "words \u2014 they will hand over to God\u2019s wisdom for the next 90 days, and one person who "
             "will ask them about it. Close by asking God together for the wisdom He promises to give.")},
 ],
 "closing_kicker":"Forty days. Six sessions.",
 "closing_title":"A life built on the rock.",
 "closing_body":("The Wisdom-Driven Life is a complete 40-day campaign and six-session small group "
                 "journey that moves a congregation from information overload to genuine wisdom \u2014 "
                 "learning to fear the Lord, ask Him for direction, decide with discernment, speak "
                 "with grace, seek wise counsel, and build a life that stands. Not the smartest life. "
                 "The wisest one."),
 "cta":"Launch the campaign churchwide, in small groups, or as a personal 40-day journey \u2014 and start building on the rock.",
 "footer":("Brett Eastman \u00b7 Founder, Lifetogether \u00b7 brett@lifetogether.com \u00b7 "
           "The Wisdom-Driven Life \u00b7 A 40-Day Campaign \u00b7 Drawn from Family Legacy by Design"),
}

# ----- The 40-Day daily reading plan, grouped into the six weekly sessions -----
PLAN=[
 {"wk":1,"days":"Days 1\u20137","title":"Two Ways to Live","theme":"The Fear of the Lord",
  "items":[
   (1,"Begin Here","Proverbs 9:10","Wisdom starts with the fear of the Lord. Name where you have been starting instead."),
   (2,"Wisdom or Folly","Proverbs 14:8","The wise think about where the road leads; the fool does not. Which are you today?"),
   (3,"Two Builders","Matthew 7:24\u201327","Same storm, two foundations. Honestly, what is your life built on?"),
   (4,"Not Wise in Your Own Eyes","Proverbs 3:7","Where are you trusting only your own judgment? Hand it to God."),
   (5,"Everything Is Vanity","Ecclesiastes 1:2","Solomon had it all and called it meaningless. What are you chasing that can\u2019t satisfy?"),
   (6,"A Reverent Heart","Psalm 111:10","Reverence isn\u2019t dread of punishment; it\u2019s awe that reorders everything. Sit in it."),
   (7,"The Tree by Water","Psalm 1:1\u20133","Two ways diverge. Choose the path that leads to a tree planted by streams of water.")]},
 {"wk":2,"days":"Days 8\u201314","title":"Ask for It","theme":"Wisdom from God",
  "items":[
   (8,"Just Ask","James 1:5","Wisdom is one honest prayer away. Ask for it today, out loud."),
   (9,"Ask Without Doubting","James 1:6","Bring God your real question and trust Him with the answer."),
   (10,"Solomon\u2019s Request","1 Kings 3:9","He could ask for anything and asked for a discerning heart. What would you ask for?"),
   (11,"More Than Gold","Proverbs 3:13\u201314","Wisdom is more profitable than silver. Treat it that way today."),
   (12,"The Spirit Guides","John 16:13","You are not left to figure life out alone. Invite the Spirit into one decision."),
   (13,"Hidden in Christ","Colossians 2:3","All wisdom is hidden in Jesus. Go to Him, not just to more information."),
   (14,"Dig for It","Proverbs 2:3\u20135","Wisdom is found by those who search like miners. Where will you dig this week?")]},
 {"wk":3,"days":"Days 15\u201321","title":"Wisdom in the Decision","theme":"Trust & Discernment",
  "items":[
   (15,"Lean Not","Proverbs 3:5","Trust Him with your whole heart; lean not on your own understanding."),
   (16,"Straight Paths","Proverbs 3:6","Submit your ways and He straightens the path. Name one way to submit today."),
   (17,"Count the Cost","Luke 14:28","The wise build only after counting the cost. What decision needs honest counting?"),
   (18,"Slow the Impulse","Proverbs 19:2","\u201cTo be hasty is to miss the way.\u201d Where do you need to slow down?"),
   (19,"Test It","1 Thessalonians 5:21","Test everything; hold to what is good. What needs testing before you commit?"),
   (20,"Peace as Umpire","Colossians 3:15","Let the peace of Christ rule \u2014 and referee \u2014 your decisions today."),
   (21,"Wise, Loving, Honoring","Philippians 1:9\u201310","Run today\u2019s choice through three filters: Is it wise? Loving? Honoring to God?")]},
 {"wk":4,"days":"Days 22\u201328","title":"The Words of the Wise","theme":"Wisdom in Speech",
  "items":[
   (22,"Life and Death","Proverbs 18:21","The tongue carries life or death. Which did your words carry today?"),
   (23,"Slow to Speak","James 1:19","Quick to listen, slow to speak, slow to anger. Practice the order."),
   (24,"The Right Word","Proverbs 25:11","A word fitly spoken is gold set in silver. Whom can you encourage with one?"),
   (25,"Truth in Love","Ephesians 4:15","Truth without love wounds; love without truth flatters. Aim for both."),
   (26,"Guard the Gate","Proverbs 21:23","Guarding your mouth guards your life. Hold back one word you\u2019d regret."),
   (27,"A Gentle Answer","Proverbs 15:1","A gentle answer turns away wrath. Try it in your hardest conversation."),
   (28,"Wisdom from Above","James 3:17","Pure, peace-loving, considerate, merciful. Let that describe your speech today.")]},
 {"wk":5,"days":"Days 29\u201335","title":"Wisdom in Community","theme":"Counsel & Companions",
  "items":[
   (29,"Many Counselors","Proverbs 15:22","Plans fail without counsel. Who will you invite into yours?"),
   (30,"Walk with the Wise","Proverbs 13:20","You become like your company. Audit your closest five."),
   (31,"Iron Sharpens Iron","Proverbs 27:17","Growth needs friction from a faithful friend. Who sharpens you?"),
   (32,"Faithful Wounds","Proverbs 27:6","A friend\u2019s honest wound beats an enemy\u2019s flattery. Receive correction well."),
   (33,"Carry the Load","Galatians 6:2","Wisdom shares the weight. Whose burden can you help carry today?"),
   (34,"Humble Enough to Ask","Proverbs 11:2","\u201cWith humility comes wisdom.\u201d Ask for help in one area of pride."),
   (35,"Two Are Better","Ecclesiastes 4:9\u201312","A cord of three strands is not quickly broken. Gather your people.")]},
 {"wk":6,"days":"Days 36\u201340","title":"The Wise Builder","theme":"Doing the Word",
  "items":[
   (36,"Hear and Do","Matthew 7:24","The wise don\u2019t just hear; they build. What will you build today?"),
   (37,"Not Hearers Only","James 1:22","Hearing without doing deceives us. Put one truth into practice now."),
   (38,"Tuesday Integrity","Luke 16:10","Faithful in little, faithful in much. Be the same on Tuesday as on Sunday."),
   (39,"Don\u2019t Grow Weary","Galatians 6:9","The harvest comes to those who don\u2019t give up. Keep building."),
   (40,"Built on the Rock","Matthew 7:25","The storm came and the house stood. Commit to the life you\u2019ve begun.")]},
]

def chips(lst, light=False):
    cls="chip light" if light else "chip"
    return '<div class="chips">'+"".join(f'<span class="{cls}">{esc(t)}</span>' for t in lst)+'</div>'

def card(n,s):
    title=f'{esc(s["t"])} <i>{esc(s["a"])}</i>'
    qs="".join(f'<div class="q"><span class="qm">Q</span><p>{esc(q)}</p></div>' for q in s["q"])
    if s.get("commit"):
        step=f'<div class="step commit"><div class="step-label">Commitment Step</div><p>{esc(s["commit"])}</p></div>'
    else:
        step=f'<div class="step"><div class="step-label">This Week\u2019s Step</div><p>{esc(s["step"])}</p></div>'
    return f"""<div class="card"><div class="card-head"><div class="sess-no">Session {n}</div>
      <div class="sess-title">{title}</div></div>
      <div class="card-body"><p class="verse">{esc(s["s"])}</p>{chips(s["tags"])}
      <div class="dq-label">Discussion Questions</div>{qs}{step}</div></div>"""

def cover():
    toc="".join(
        f'<li><span class="tn">{i+1}</span><span class="tt"><b>{esc(s["t"]+" "+s["a"])}</b>'
        f'<i>{esc(s["s"].split(" \u2014 ")[-1])}</i></span></li>'
        for i,s in enumerate(DATA["sessions"]))
    return f"""<section class="cover">
      <div class="cover-eyebrow">{esc(DATA['eyebrow'])}</div>
      <div class="cover-cat">{esc(DATA['category'])}</div>
      <h1 class="cover-title">{esc(DATA['title'])}<br><span class="ct-accent">{esc(DATA['accent'])}</span></h1>
      <p class="cover-sub">{esc(DATA['subhead'])}</p>
      <div class="hero-scripture">
        <div class="hs-q">\u201c</div>
        <p class="hs-t">{esc(DATA['scripture'].strip(chr(8220)+chr(8221)))}</p>
        <p class="hs-r">{esc(DATA['scripture_ref'])}</p>
      </div>
      <div class="badges"><span><b>40</b>days</span><span><b>6</b>sessions</span><span><b>1</b>well-built life</span></div>
      <div class="toc-wrap"><div class="toc-label">The Six-Session Journey</div>
        <ul class="toc">{toc}</ul></div>
      <div class="cover-foot">{esc(DATA['footer'])}</div>
    </section>"""

def overview():
    subs="".join(f'<div class="sub-opt">{esc(x)}</div>' for x in DATA["subtitles"])
    rows="".join(f'<div class="ir"><span class="ik">{esc(k)}</span><span class="iv">{esc(v)}</span></div>'
                 for k,v in DATA["info"])
    return f"""<section class="overview">
      <div class="ov-banner"><div class="ovb-eyebrow">The Campaign</div>
        <h2 class="ovb-title">Why a <i>Wisdom-Driven</i> Life</h2></div>
      <div class="intro">
        <div class="intro-main">
          <p class="pullquote">{esc(DATA['pullquote'])}</p>
          <p class="body">{DATA['body']}</p>
          <div class="bigidea"><div class="bi-label">Big Idea</div>
            <p class="bi-text">{esc(DATA['bigidea'])}</p>{chips(DATA['tags'],light=True)}</div>
        </div>
        <aside class="intro-side">
          <div class="info-card"><div class="info-label">Series Information</div>{rows}</div>
          <div class="subs-card"><div class="subs-label">Subtitle Options</div>{subs}</div>
        </aside>
      </div>
    </section>"""

def sessions():
    cards="".join(card(i+1,s) for i,s in enumerate(DATA["sessions"]))
    return f"""<section class="sessions">
      <div class="curr-label">Small Group Curriculum &nbsp;\u2014&nbsp; Six Sessions</div>
      <div class="cards">{cards}</div></section>"""

def closing():
    return f"""<section class="closing">
      <div class="spectrum"></div>
      <div class="closing-kicker">{esc(DATA['closing_kicker'])}</div>
      <h2 class="closing-title">{esc(DATA['closing_title'])}</h2>
      <p class="closing-body">{esc(DATA['closing_body'])}</p>
      <div class="closing-stats"><div><b>40</b><span>daily readings</span></div>
        <div><b>6</b><span>group sessions</span></div><div><b>18</b><span>discussion questions</span></div></div>
      <div class="cta">{esc(DATA['cta'])}</div>
      <div class="cover-foot">{esc(DATA['footer'])}</div></section>"""

def plan_section():
    weeks=""
    for w in PLAN:
        rows="".join(
            f'<div class="day"><span class="day-n">{n}</span>'
            f'<div class="day-b"><div class="day-t">{esc(t)} <i>\u00b7 {esc(ref)}</i></div>'
            f'<p class="day-p">{esc(prompt)}</p></div></div>'
            for (n,t,ref,prompt) in w["items"])
        weeks+=f"""<div class="week">
          <div class="week-head">
            <div class="wk-left"><span class="wk-no">Week {w['wk']}</span>
              <span class="wk-days">{esc(w['days'])}</span></div>
            <div class="wk-right"><b>{esc(w['title'])}</b><i>{esc(w['theme'])}</i></div>
          </div>
          <div class="days">{rows}</div>
        </div>"""
    return f"""<section class="plan">
      <div class="ov-banner"><div class="ovb-eyebrow">The Daily Journey</div>
        <h2 class="ovb-title">The <i>40-Day</i> Reading Plan</h2>
        <p class="ovb-sub">Six weeks. Forty days. A short reading and one small practice each day \u2014 paired with the weekly group session that shares its theme.</p></div>
      {weeks}
    </section>"""

HTML=f"""<!DOCTYPE html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>The Wisdom-Driven Life \u00b7 Lifetogether</title><style>
{FONT_CSS}
*{{box-sizing:border-box;margin:0;padding:0}}
:root{{--c:{C};--dark:{DARK};--deep:{DEEP};--tint:{TINT};--gold:{GOLD};--gold-l:{GOLD_L};
  --ink:{INK};--cream:{CREAM};--paper:{PAPER};--tan:{TAN}}}
html{{-webkit-print-color-adjust:exact;print-color-adjust:exact}}
body{{font-family:'Garamond',Georgia,serif;color:var(--ink);background:var(--cream);font-size:15px;line-height:1.5}}
.page{{width:850px;margin:0 auto;background:var(--paper)}}
i{{font-style:italic}} b{{font-weight:700}}
.cover-eyebrow,.cover-cat,.info-label,.subs-label,.bi-label,.dq-label,.step-label,.curr-label,
.toc-label,.closing-kicker,.ovb-eyebrow,.hs-r,.sess-no{{font-family:'Garamond',serif;
  text-transform:uppercase;letter-spacing:.26em;font-weight:600}}

/* ---------- COVER ---------- */
.cover{{padding:70px 78px 52px;min-height:1180px;display:flex;flex-direction:column;
  background:radial-gradient(1100px 540px at 82% -10%,{lighten(C,0.80)} 0%,rgba(0,0,0,0) 58%),
  linear-gradient(180deg,#fdfbf5,var(--paper))}}
.cover-eyebrow{{font-size:11px;letter-spacing:.3em;color:var(--gold);margin-bottom:12px}}
.cover-cat{{font-size:10.5px;letter-spacing:.24em;color:var(--c);margin-bottom:30px}}
.cover-title{{font-family:'Playfair',serif;font-weight:800;font-size:88px;line-height:.94;
  letter-spacing:-.015em;color:var(--ink)}}
.ct-accent{{font-style:italic;font-weight:500;color:var(--gold)}}
.cover-sub{{font-size:18.5px;line-height:1.6;max-width:600px;margin:26px 0 0;color:#4a423a}}
.hero-scripture{{position:relative;margin:34px 0 0;padding:30px 36px 28px;border-radius:6px;
  color:#f3f1e9;background:linear-gradient(135deg,var(--deep),var(--c) 75%,var(--dark));max-width:680px}}
.hs-q{{position:absolute;left:18px;top:0;font-family:'Playfair',serif;font-size:90px;
  color:rgba(255,255,255,.14);line-height:1}}
.hs-t{{font-family:'Playfair',serif;font-style:italic;font-size:23px;line-height:1.42;position:relative}}
.hs-r{{margin-top:12px;font-size:11px;letter-spacing:.16em;color:rgba(255,255,255,.78)}}
.badges{{display:flex;gap:14px;margin:30px 0 0}}
.badges span{{display:flex;align-items:baseline;gap:7px;padding:9px 18px;border-radius:30px;
  background:#fff;border:1px solid #e7ddc7;font-size:12px;letter-spacing:.14em;text-transform:uppercase;
  color:#7c7264}}
.badges b{{font-family:'Playfair',serif;font-size:24px;font-weight:700;color:var(--c);letter-spacing:0}}
.toc-wrap{{margin-top:36px}}
.toc-label{{font-size:10px;letter-spacing:.28em;color:var(--gold);margin-bottom:16px}}
.toc{{list-style:none;columns:2;column-gap:46px}}
.toc li{{display:flex;gap:13px;break-inside:avoid;margin-bottom:14px;align-items:baseline}}
.tn{{flex:0 0 26px;height:26px;border-radius:50%;background:var(--c);color:#fff;
  font-family:'Playfair',serif;font-size:14px;font-weight:700;display:flex;align-items:center;
  justify-content:center;margin-top:2px}}
.tt{{display:flex;flex-direction:column;line-height:1.28}}
.tt b{{font-family:'Playfair',serif;font-weight:600;font-size:16px;color:var(--ink)}}
.tt i{{font-size:12px;color:#8a8073}}
.cover-foot{{margin-top:auto;padding-top:28px;font-size:11px;letter-spacing:.04em;color:#9b9081;
  border-top:1px solid rgba(0,0,0,.1)}}

/* ---------- OVERVIEW ---------- */
.overview{{break-before:page}}
.ov-banner{{position:relative;overflow:hidden;color:#f4f2ea;padding:46px 78px 40px;
  background:linear-gradient(140deg,var(--deep),var(--c) 64%,var(--dark))}}
.ovb-eyebrow{{font-size:10.5px;letter-spacing:.26em;color:rgba(255,255,255,.78);margin-bottom:12px}}
.ovb-title{{font-family:'Playfair',serif;font-weight:700;font-size:46px;line-height:1}}
.ovb-title i{{font-weight:500;color:{lighten(GOLD,0.42)}}}
.intro{{display:grid;grid-template-columns:1fr 290px;gap:40px;padding:42px 78px 10px}}
.pullquote{{font-family:'Playfair',serif;font-style:italic;font-weight:500;font-size:27px;
  line-height:1.32;color:var(--deep);margin-bottom:22px}}
.body{{font-size:15.5px;line-height:1.66;color:#43392f}} .body b{{color:var(--deep)}}
.bigidea{{margin-top:28px;padding:32px 36px;border-radius:6px;color:#f4f2ea;
  background:linear-gradient(135deg,var(--c),var(--dark))}}
.bi-label{{font-size:10px;letter-spacing:.3em;color:rgba(255,255,255,.72);margin-bottom:14px}}
.bi-text{{font-family:'Playfair',serif;font-style:italic;font-size:21px;line-height:1.46;color:#f7f5ee}}
.intro-side{{display:flex;flex-direction:column;gap:18px}}
.info-card{{background:#fff;border:1px solid #e7ddc7;border-radius:5px;padding:20px 22px}}
.info-label{{font-size:9.5px;letter-spacing:.24em;color:var(--c);margin-bottom:14px}}
.ir{{display:flex;gap:10px;padding:7px 0;border-top:1px solid #f0e8d6;font-size:13px}}
.ir:first-of-type{{border-top:none}}
.ik{{flex:0 0 84px;font-weight:700;color:#6b6052}} .iv{{color:#544a3e}}
.subs-card{{background:var(--tan);border-radius:5px;padding:18px 22px}}
.subs-label{{font-size:9.5px;letter-spacing:.24em;color:{darken(GOLD,0.12)};margin-bottom:12px}}
.sub-opt{{font-style:italic;font-size:13.5px;color:#5f5440;padding:6px 0;border-top:1px solid rgba(0,0,0,.07)}}
.sub-opt:first-of-type{{border-top:none}}
.chips{{display:flex;flex-wrap:wrap;gap:8px;margin-top:18px}}
.chip{{font-size:11px;letter-spacing:.04em;padding:4px 11px;border-radius:20px;background:var(--tint);
  border:1px solid {lighten(C,0.62)};color:var(--dark)}}
.chip.light{{background:rgba(255,255,255,.13);border:1px solid rgba(255,255,255,.3);color:#f3f1ea}}

/* ---------- SESSIONS ---------- */
.sessions{{break-before:page;padding-bottom:30px}}
.curr-label{{font-size:11px;letter-spacing:.26em;color:var(--gold);text-align:center;margin:46px 0 24px}}
.cards{{display:grid;grid-template-columns:1fr 1fr;gap:22px;padding:0 78px}}
.card{{background:#fff;border:1px solid #e9e0cc;border-radius:6px;overflow:hidden;break-inside:avoid;
  box-shadow:0 1px 2px rgba(0,0,0,.03)}}
.card-head{{padding:16px 22px;color:#f4f2ea;background:linear-gradient(135deg,var(--c),var(--dark))}}
.sess-no{{font-size:9.5px;letter-spacing:.26em;color:rgba(255,255,255,.78);margin-bottom:6px}}
.sess-title{{font-family:'Playfair',serif;font-weight:700;font-size:22px;line-height:1.12}}
.sess-title i{{font-weight:500;color:{lighten(GOLD,0.45)}}}
.card-body{{padding:20px 22px 22px}}
.verse{{font-style:italic;font-size:13.5px;line-height:1.45;color:#6a5f50;padding-bottom:14px;
  border-bottom:1px solid #efe7d5}}
.dq-label{{font-size:9px;letter-spacing:.24em;color:var(--c);margin:16px 0 10px}}
.q{{display:flex;gap:10px;padding:8px 0;border-top:1px dotted #e6dcc6}}
.q:first-of-type{{border-top:none;padding-top:2px}}
.qm{{flex:0 0 16px;height:16px;margin-top:2px;border-radius:50%;background:var(--tint);
  color:var(--dark);font-size:9px;font-weight:700;display:flex;align-items:center;justify-content:center}}
.q p{{font-size:13.5px;line-height:1.45;color:#473d31}}
.step{{margin-top:16px;padding:14px 16px;border-radius:5px;background:var(--tint);border-left:3px solid var(--c)}}
.step.commit{{background:{lighten(GOLD,0.78)};border-left-color:var(--gold)}}
.step-label{{font-size:9px;letter-spacing:.2em;color:var(--dark);margin-bottom:7px}}
.step.commit .step-label{{color:{darken(GOLD,0.15)}}}
.step p{{font-size:13px;line-height:1.5;color:#4a4034}}

/* ---------- 40-DAY PLAN ---------- */
.plan{{break-before:page;padding-bottom:34px}}
.ovb-sub{{position:relative;max-width:600px;margin-top:14px;font-size:15px;line-height:1.55;
  color:rgba(255,255,255,.9);font-style:italic}}
.week{{margin:34px 78px 0}}
.week-head{{display:flex;justify-content:space-between;align-items:center;gap:18px;
  padding:13px 22px;border-radius:6px;color:#f4f2ea;
  background:linear-gradient(135deg,var(--c),var(--dark))}}
.wk-left{{display:flex;align-items:baseline;gap:12px}}
.wk-no{{font-family:'Playfair',serif;font-weight:700;font-size:19px}}
.wk-days{{font-size:10px;letter-spacing:.22em;text-transform:uppercase;color:rgba(255,255,255,.72)}}
.wk-right{{display:flex;align-items:baseline;gap:12px;text-align:right}}
.wk-right b{{font-family:'Playfair',serif;font-weight:600;font-size:18px;color:{lighten(GOLD,0.5)}}}
.wk-right i{{font-size:11.5px;letter-spacing:.14em;text-transform:uppercase;color:rgba(255,255,255,.78)}}
.days{{display:grid;grid-template-columns:1fr 1fr;gap:10px 22px;margin-top:14px}}
.day{{display:flex;gap:12px;break-inside:avoid;padding:8px 0;
  border-bottom:1px dotted #e6dcc6;align-items:flex-start}}
.day-n{{flex:0 0 24px;height:24px;border-radius:50%;background:var(--tint);color:var(--dark);
  font-family:'Playfair',serif;font-weight:700;font-size:12.5px;display:flex;align-items:center;
  justify-content:center;margin-top:1px}}
.day-b{{flex:1}}
.day-t{{font-family:'Playfair',serif;font-weight:600;font-size:15px;color:var(--ink);line-height:1.2}}
.day-t i{{font-family:'Garamond',serif;font-weight:600;font-style:normal;font-size:11px;
  letter-spacing:.04em;color:var(--c)}}
.day-p{{font-size:12.5px;line-height:1.4;color:#5f554a;margin-top:3px}}

/* ---------- CLOSING ---------- */
.closing{{break-before:page;padding:90px 78px 56px;min-height:1180px;display:flex;flex-direction:column;
  background:linear-gradient(180deg,#fdfbf5,var(--paper))}}
.spectrum{{height:8px;border-radius:6px;margin-bottom:54px;
  background:linear-gradient(90deg,var(--deep),var(--c) 45%,var(--gold) 100%)}}
.closing-kicker{{font-size:12px;letter-spacing:.3em;color:var(--gold);margin-bottom:16px}}
.closing-title{{font-family:'Playfair',serif;font-style:italic;font-weight:500;font-size:62px;
  line-height:1;color:var(--ink);margin-bottom:28px}}
.closing-body{{font-size:18px;line-height:1.66;max-width:650px;color:#473d31}}
.closing-stats{{display:flex;gap:54px;margin-top:46px}}
.closing-stats div{{display:flex;flex-direction:column}}
.closing-stats b{{font-family:'Playfair',serif;font-weight:700;font-size:46px;color:var(--gold)}}
.closing-stats span{{font-size:12px;letter-spacing:.16em;text-transform:uppercase;color:#8a7f6f;margin-top:4px}}
.cta{{margin-top:42px;padding:22px 28px;border-radius:6px;color:#f4f2ea;font-family:'Playfair',serif;
  font-style:italic;font-size:19px;line-height:1.4;max-width:660px;
  background:linear-gradient(135deg,var(--c),var(--dark))}}
.cover-foot{{margin-top:auto;padding-top:28px;font-size:11px;letter-spacing:.04em;color:#9b9081;
  border-top:1px solid rgba(0,0,0,.1)}}
@media print{{body{{background:#fff}}.page{{width:auto;margin:0}}
  .overview,.sessions,.closing{{break-before:page}}
  .card,.toc li,.info-card,.bigidea,.hero-scripture{{break-inside:avoid}}}}
</style></head><body><div class="page">
{cover()}
{overview()}
{sessions()}
{plan_section()}
{closing()}
</div></body></html>"""

if __name__=="__main__":
    with open("/home/claude/Wisdom_Driven_Life.html","w",encoding="utf-8") as f: f.write(HTML)
    print("HTML bytes:",len(HTML))
