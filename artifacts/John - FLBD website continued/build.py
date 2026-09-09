# -*- coding: utf-8 -*-
# Family Legacy Campaign - Week One content build
# Days 2-7 + Session One + Week One hub. Drop-in pages for the existing FLBD site.
import base64, pathlib, html

F = pathlib.Path("/home/claude/flbd/fonts")
OUT = pathlib.Path("/home/claude/flbd/site")
OUT.mkdir(exist_ok=True)

def b64(name):
    return base64.b64encode((F / name).read_bytes()).decode()

FACES = [
    ("Besley", 400, "normal", "Besley-400.sub.woff2"),
    ("Besley", 700, "normal", "Besley-700.sub.woff2"),
    ("Besley", 800, "normal", "Besley-800.sub.woff2"),
    ("Besley", 400, "italic", "BesleyItalic-400.sub.woff2"),
    ("Archivo", 400, "normal", "Archivo-400.sub.woff2"),
    ("Archivo", 500, "normal", "Archivo-500.sub.woff2"),
    ("Archivo", 600, "normal", "Archivo-600.sub.woff2"),
    ("Archivo", 700, "normal", "Archivo-700.sub.woff2"),
    ("EB Garamond", 400, "normal", "EBGaramond-400.sub.woff2"),
    ("EB Garamond", 400, "italic", "EBGaramondItalic-400.sub.woff2"),
]
fontcss = "\n".join(
    f"@font-face{{font-family:'{fam}';font-weight:{w};font-style:{st};font-display:swap;"
    f"src:url(data:font/woff2;base64,{b64(fn)}) format('woff2');}}"
    for fam, w, st, fn in FACES
)

CSS = fontcss + r"""
:root{
  --cream:#F4EFE3; --paper:#FCF9F1; --ink:#26251E; --muted:#6E6A5B;
  --green:#1C3A2D; --green-deep:#152E23; --gold:#B4872C; --gold-soft:#D8B45F;
  --line:#E3DAC3;
}
*{margin:0;padding:0;box-sizing:border-box}
html{font-size:16px;scroll-padding-top:84px}
body{background:var(--cream);color:var(--ink);font-family:'Archivo',system-ui,sans-serif;line-height:1.6;-webkit-font-smoothing:antialiased}
img,svg{max-width:100%}
a{color:var(--green);text-decoration-thickness:1px;text-underline-offset:3px}
a:hover{color:var(--green-deep)}
:focus-visible{outline:2px solid var(--gold);outline-offset:2px;border-radius:2px}
.skip{position:absolute;left:-9999px;top:0;background:var(--green);color:var(--paper);padding:.6rem 1rem;z-index:99;border-radius:0 0 8px 0}
.skip:focus{left:0}
@media(prefers-reduced-motion:reduce){*,*::before,*::after{transition:none!important;animation:none!important}}

/* ---------- header ---------- */
header.site{background:var(--cream);border-bottom:1px solid var(--line)}
.bar{max-width:1060px;margin:0 auto;padding:.9rem 1.25rem;display:flex;align-items:center;gap:1.1rem;flex-wrap:wrap}
.mark{display:flex;align-items:baseline;gap:.5rem;text-decoration:none}
.mark b{font-family:'Besley',serif;font-weight:800;font-size:1.16rem;color:var(--green-deep);letter-spacing:-.01em}
.mark span{font-size:.8rem;font-weight:600;color:var(--gold);letter-spacing:.06em}
nav.top{display:flex;gap:1.1rem;margin-left:auto;align-items:center}
nav.top a{font-weight:600;font-size:.92rem;text-decoration:none;color:var(--ink);padding:.25rem 0;border-bottom:2px solid transparent}
nav.top a:hover{border-bottom-color:var(--gold)}
nav.top a[aria-current="page"]{border-bottom-color:var(--gold);color:var(--green-deep)}
.daychip{font-size:.8rem;font-weight:700;color:var(--paper);background:var(--green);padding:.34rem .7rem;border-radius:999px;white-space:nowrap}

/* ---------- day ribbon (signature) ---------- */
.ribbonwrap{max-width:1060px;margin:0 auto;padding:.8rem 1.25rem .2rem;display:flex;align-items:flex-end;gap:1rem}
.ribbon{display:flex;align-items:flex-end;gap:3px;flex:1;height:22px}
.ribbon i{display:block;width:100%;max-width:14px;height:9px;border-radius:2px;background:var(--line)}
.ribbon i.done{background:var(--green)}
.ribbon i.now{background:var(--gold);height:20px}
.ribbon i.wk{margin-left:8px}
.riblabel{font-size:.74rem;font-weight:700;color:var(--muted);letter-spacing:.08em;white-space:nowrap;padding-bottom:1px}

/* ---------- layout ---------- */
main{max-width:1060px;margin:0 auto;padding:2.4rem 1.25rem 3rem}
.col{max-width:720px}
.kicker{font-size:.78rem;font-weight:700;letter-spacing:.14em;text-transform:uppercase;color:var(--gold);margin-bottom:.9rem}
h1{font-family:'Besley',serif;font-weight:800;font-size:clamp(2.1rem,5.4vw,3.25rem);line-height:1.07;letter-spacing:-.012em;color:var(--green-deep)}
.dek{font-family:'Besley',serif;font-style:italic;font-weight:400;font-size:clamp(1.12rem,2.4vw,1.32rem);line-height:1.5;color:#4A4638;margin:1rem 0 0}
.rule{height:1px;background:var(--line);margin:1.9rem 0}

/* scripture plate */
.scripture{background:var(--paper);border-left:3px solid var(--gold);border-radius:0 12px 12px 0;padding:1.4rem 1.6rem;margin:0 0 2rem}
.scripture p{font-family:'EB Garamond',serif;font-size:clamp(1.22rem,2.6vw,1.42rem);line-height:1.55;color:#2C2A22}
.scripture .ref{display:block;margin-top:.8rem;font-family:'Archivo',sans-serif;font-size:.8rem;font-weight:700;letter-spacing:.1em;text-transform:uppercase;color:var(--gold)}

/* reading prose */
.reading p{font-family:'Besley',serif;font-weight:400;font-size:1.155rem;line-height:1.82;margin:0 0 1.35rem;color:var(--ink)}
.reading p:last-child{margin-bottom:0}

/* practice blocks */
.block{border-radius:12px;padding:1.35rem 1.5rem;margin:1.4rem 0}
.block .lab{font-size:.76rem;font-weight:700;letter-spacing:.13em;text-transform:uppercase;margin-bottom:.55rem}
.q{border:1.5px solid var(--green);background:transparent}
.q .lab{color:var(--green)}
.q p{font-family:'Besley',serif;font-size:1.18rem;line-height:1.55;color:var(--green-deep)}
.s{background:var(--paper);border-left:4px solid var(--gold);border-radius:0 12px 12px 0}
.s .lab{color:var(--gold)}
.s p{font-size:1.02rem;line-height:1.7}
.pr{border-top:1px solid var(--line);border-bottom:1px solid var(--line);border-radius:0;padding:1.5rem .2rem}
.pr .lab{color:var(--muted)}
.pr p{font-family:'EB Garamond',serif;font-style:italic;font-size:1.28rem;line-height:1.6;color:#33312A}

/* advisor band */
.advisor{background:var(--green-deep);color:#EFE9D8;margin:2.6rem 0 0;border-radius:14px;padding:1.8rem 1.7rem}
.advisor .lab{font-size:.76rem;font-weight:700;letter-spacing:.13em;text-transform:uppercase;color:var(--gold-soft);margin-bottom:.7rem}
.advisor p{font-size:1rem;line-height:1.75;max-width:62ch}
.advisor .ask{font-family:'EB Garamond',serif;font-style:italic;font-size:1.22rem;line-height:1.5;color:var(--gold-soft);margin-top:1rem}

/* prev/next */
.pn{display:grid;grid-template-columns:1fr 1fr;gap:1rem;margin-top:2.6rem}
.pn a{display:block;background:var(--paper);border:1px solid var(--line);border-radius:12px;padding:1.1rem 1.25rem;text-decoration:none;color:var(--ink);transition:transform .15s ease,border-color .15s ease}
.pn a:hover{transform:translateY(-2px);border-color:var(--gold)}
.pn .dir{font-size:.74rem;font-weight:700;letter-spacing:.11em;text-transform:uppercase;color:var(--muted)}
.pn .ttl{font-family:'Besley',serif;font-weight:700;font-size:1.12rem;color:var(--green-deep);margin-top:.25rem}
.pn a.next{text-align:right}
@media(max-width:640px){.pn{grid-template-columns:1fr}.pn a.next{text-align:left}}

/* buttons */
.btn{display:inline-block;background:var(--green);color:var(--paper);font-weight:600;font-size:1rem;padding:.78rem 1.35rem;border-radius:10px;text-decoration:none}
.btn:hover{background:var(--green-deep);color:var(--paper)}
.btn.gold{background:var(--gold);color:#241D0E}
.btn.gold:hover{background:#9E7524;color:var(--paper)}

/* session page */
.seg{display:grid;grid-template-columns:78px 1fr;gap:1.2rem;margin:1.9rem 0;align-items:start}
.seg .min{background:var(--paper);border:1px solid var(--line);border-radius:10px;text-align:center;padding:.55rem .3rem;font-weight:700;font-size:.82rem;color:var(--green-deep)}
.seg .min b{display:block;font-family:'Besley',serif;font-size:1.3rem;line-height:1.1}
.seg h3{font-family:'Besley',serif;font-weight:700;font-size:1.42rem;color:var(--green-deep);margin-bottom:.5rem}
.seg p{font-size:1.02rem;line-height:1.7;margin-bottom:.8rem;max-width:62ch}
.say{background:var(--paper);border-left:3px solid var(--green);border-radius:0 10px 10px 0;padding:1rem 1.2rem;margin:.6rem 0}
.say p{font-family:'Besley',serif;font-style:italic;font-size:1.08rem;line-height:1.6;margin:0}
.qs{counter-reset:tq;margin:.4rem 0 0;max-width:62ch}
.qs div{counter-increment:tq;display:grid;grid-template-columns:34px 1fr;gap:.7rem;padding:.75rem 0;border-bottom:1px solid var(--line);align-items:start}
.qs div:last-child{border-bottom:0}
.qs div::before{content:counter(tq);font-family:'Besley',serif;font-weight:800;color:var(--gold);font-size:1.15rem;line-height:1.35}
.qs p{font-family:'Besley',serif;font-size:1.12rem;line-height:1.5;color:var(--ink)}
.ground{display:grid;gap:.6rem;margin:.6rem 0 0;max-width:62ch}
.ground div{background:var(--paper);border:1px solid var(--line);border-radius:10px;padding:.8rem 1rem;font-size:.98rem;line-height:1.55}
.ground b{color:var(--green-deep)}
@media(max-width:560px){.seg{grid-template-columns:1fr}.seg .min{display:inline-block;padding:.4rem .8rem}.seg .min b{display:inline;font-size:1rem;margin-right:.3rem}}

/* hub */
.rhythm{display:flex;gap:.9rem;flex-wrap:wrap;margin:1.6rem 0 0}
.rhythm span{background:var(--paper);border:1px solid var(--line);border-radius:999px;padding:.5rem 1rem;font-weight:600;font-size:.92rem}
.engine{font-family:'Besley',serif;font-style:italic;font-size:1.15rem;color:#4A4638;margin-top:1rem}
.cards{display:grid;grid-template-columns:repeat(auto-fill,minmax(236px,1fr));gap:1rem;margin-top:2rem}
.card{background:var(--paper);border:1px solid var(--line);border-radius:14px;padding:1.15rem 1.2rem;text-decoration:none;color:var(--ink);display:flex;flex-direction:column;gap:.4rem;transition:transform .15s ease,border-color .15s ease}
.card:hover{transform:translateY(-2px);border-color:var(--gold)}
.card .dn{display:flex;align-items:center;gap:.6rem;font-size:.76rem;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:var(--gold)}
.card .start{background:var(--gold);color:#241D0E;border-radius:999px;padding:.14rem .6rem;letter-spacing:.06em}
.card h3{font-family:'Besley',serif;font-weight:700;font-size:1.22rem;color:var(--green-deep)}
.card p{font-size:.95rem;line-height:1.55;color:#4A4638}
.card .sref{margin-top:auto;font-size:.78rem;font-weight:700;letter-spacing:.09em;text-transform:uppercase;color:var(--muted)}
.card.session{grid-column:1/-1;background:var(--green-deep);border-color:var(--green-deep);color:#EFE9D8}
.card.session h3{color:var(--paper);font-size:1.5rem}
.card.session p{color:#D8D2BE;max-width:62ch}
.card.session .dn{color:var(--gold-soft)}
.card.session .go{margin-top:.4rem;color:var(--gold-soft);font-weight:600}

/* footer */
footer.site{border-top:1px solid var(--line);margin-top:3rem}
.foot{max-width:1060px;margin:0 auto;padding:1.6rem 1.25rem 2.2rem;display:flex;flex-wrap:wrap;gap:.9rem 2rem;align-items:baseline;font-size:.88rem;color:var(--muted)}
.foot b{font-family:'Besley',serif;color:var(--green-deep);font-weight:700}
.foot a{color:var(--green)}
"""

# ----------------------------------------------------------------------------
FAV = ("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E"
       "%3Crect width='32' height='32' rx='7' fill='%23152E23'/%3E"
       "%3Ctext x='16' y='22' text-anchor='middle' font-family='Georgia,serif' font-weight='700' "
       "font-size='17' fill='%23D8B45F'%3EFL%3C/text%3E%3C/svg%3E")

def ribbon(day):
    ticks = []
    for i in range(1, 41):
        cls = []
        if i < day: cls.append("done")
        if i == day: cls.append("now")
        if i in (8, 15, 22, 29, 36): cls.append("wk")
        ticks.append(f'<i class="{" ".join(cls)}"></i>' if cls else "<i></i>")
    return (f'<div class="ribbonwrap" aria-hidden="true"><div class="ribbon">{"".join(ticks)}</div>'
            f'<div class="riblabel">DAY {day} OF 40</div></div>')

def shell(title, desc, body, chip, active="", day=None):
    rib = ribbon(day) if day else ""
    def cur(k): return ' aria-current="page"' if active == k else ""
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:type" content="website">
<link rel="icon" href="{FAV}">
<link rel="stylesheet" href="flbd-weekone.css">
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="site">
  <div class="bar">
    <a class="mark" href="index.html"><b>Family Legacy</b><span>by Design</span></a>
    <nav class="top" aria-label="Site">
      <a href="index.html">Home</a>
      <a href="Week_One_Family_Legacy.html"{cur("week")}>Week One</a>
    </nav>
    <span class="daychip">{chip}</span>
  </div>
</header>
{rib}
<main id="main">
{body}
</main>
<footer class="site">
  <div class="foot">
    <span><b>The Family Legacy Campaign</b> &nbsp;·&nbsp; Family Legacy by Design × Lifetogether</span>
    <span><a href="mailto:brett@lifetogether.com">brett@lifetogether.com</a></span>
    <span>Scripture quotations are from the King James Version.</span>
  </div>
</footer>
</body>
</html>"""

# ----------------------------------------------------------------------------
# WEEK ONE CONTENT
# ----------------------------------------------------------------------------
DAYS = {
2: dict(
 slug="Day_Two_Family_Legacy.html",
 title="Already in Motion",
 dek="You are not deciding whether to leave a legacy. You are deciding whether to notice the one you\u2019re leaving.",
 sv="One generation shall praise thy works to another, and shall declare thy mighty acts.",
 sref="Psalm 145:4 · KJV",
 card="Legacy doesn\u2019t wait for someday — it posts entries every day, in the ordinary hours.",
 body=[
"Most families file legacy under someday. Someday, when the estate plan is finished. Someday, when the kids are older, when the business sells, when life slows down enough to think. I understand the instinct — I\u2019m a CPA by training, and someday is the most common entry I never found on a balance sheet. But years at family tables have taught me this: legacy doesn\u2019t wait for someday. It keeps its own books, and it posts entries every day.",
"It posted one this morning, in how breakfast went. It posts one in the car on the way to school, in what you talk about and what you never talk about. It posts one in the way an apology gets made in your house — or doesn\u2019t. In what gets celebrated at your table, and what gets quietly ignored. None of these entries feel important on the day they\u2019re recorded. All of them compound.",
"Children are natural auditors. They don\u2019t take our word for what the family values; they reconcile the statements against the transactions. We say faith matters, and they check the ledger. We say people come before money, and they check the ledger. Long before anyone reads a will, our families have read us — and what they catch will always outweigh what they were taught.",
"This is why I say every family already has a legacy in motion. The only question is whether it\u2019s moving by design or by default. And hear me — default is not the villain of this story. Some of what your family hands down by habit is beautiful, and you\u2019ll want to keep it. Default simply means unexamined. It means the most important transfer your family will ever make is happening without anyone watching the wire.",
"So today\u2019s work is not to fix anything. It is simply to open the books — to notice. Yesterday you saw where this journey ends: forty days from now, at a family meeting, with commitments named out loud. Today begins the quiet inventory that will make that meeting honest.",
 ],
 q="What is your family passing down right now that no one ever decided to pass down?",
 step="Write down two things you caught — not were taught — in the home you grew up in: one you want to keep handing forward, and one you\u2019re ready to retire. Keep the paper. It comes back to the table this week.",
 prayer="Father, open my eyes to the inheritance already moving through my house. Show me what we\u2019re handing down in the ordinary hours — and give me the courage to look at it honestly. Amen.",
 adv="In your meetings this week, listen for the word someday — \u201csomeday we\u2019ll sit down with the kids.\u201d Someday is the sound of a legacy running on default. When you hear it, don\u2019t correct it. Just note the family\u2019s name; by the end of this week you\u2019ll know exactly what to offer them.",
 ask="Ask one couple: \u201cIf nothing changed, what would your family inherit from you besides money?\u201d",
),
3: dict(
 slug="Day_Three_Family_Legacy.html",
 title="More Than Money",
 dek="The largest wealth transfer in history is underway. The most valuable things crossing the table won\u2019t appear on a statement.",
 sv="Take heed, and beware of covetousness: for a man\u2019s life consisteth not in the abundance of the things which he possesseth.",
 sref="Luke 12:15 · KJV",
 card="Legacy lives in five areas, not one — and money is a single seat at a five-seat table.",
 body=[
"We are living through the largest transfer of wealth the world has ever seen. Trillions of dollars are moving from one generation to the next, and an entire industry — my industry — has built itself around moving that money well. Here is what the industry is slower to say: wealth alone has never made a family wise, and it has never once made a family whole.",
"When I ask parents what they want to leave their children, the first answers are usually numbers — the house, the accounts, the business. But if we sit long enough, a different list surfaces. Their faith. Their name, and what it stands for. The stories that explain who this family is. A way of treating people. No one\u2019s deepest hope for their grandchildren is a clean transfer of assets. It\u2019s that the things that matter most would actually arrive.",
"That is why I teach families to see legacy in five areas, not one: personal, family, financial, business, and charitable. Money is one seat at a five-seat table. It is an important seat — I have spent my working life helping families steward it — but give it the only chair, and the household falls out of balance. Jesus said it plainly: a life does not consist in the abundance of possessions. A full barn and a quiet table is not a legacy. It is just a full barn.",
"And here is the door this opens. If legacy lives in five areas, then this journey is not reserved for the wealthy. Every family — whatever the balance sheet says — holds a personal legacy, a family legacy, a charitable legacy. Some of the richest inheritances I have ever watched change hands came with modest estates attached. The wealth transfer makes headlines. The wisdom transfer makes families.",
"Today, simply take the measure. Five areas. One honest look.",
 ],
 q="Which of the five areas has received the most of your attention — and which has received the least?",
 step="On paper, rank the five areas — personal, family, financial, business, charitable — from most tended to least tended in your family right now. No fixing today. Clarity first.",
 prayer="Lord, You have entrusted our family with more than money. Show us the whole inheritance — and keep us from polishing one seat at the table while the others sit empty. Amen.",
 adv="Your client\u2019s statement reports one area of the five. In your next review, ask about a second one by name — \u201cCan I ask how the family side of your legacy is doing?\u201d — and watch what happens to the meeting. Few advisors ever ask. The ones who do become a different kind of advisor to that family.",
 ask="Ask one client: \u201cOf the five areas of your legacy — personal, family, financial, business, charitable — which one keeps you up at night?\u201d",
),
4: dict(
 slug="Day_Four_Family_Legacy.html",
 title="Why Strong Families Drift",
 dek="The numbers behind failed inheritances are sobering — and almost none of them are about money.",
 sv="And there arose another generation after them, which knew not the LORD, nor yet the works which he had done for Israel.",
 sref="Judges 2:10 · KJV",
 card="Seven of ten transfers fail by the second generation — and the causes live in the living room, not the portfolio.",
 body=[
"I want to be honest with you today, and I want you to hear it the way it is meant — not as a verdict on your family, but as the reason this journey exists. The research our field has watched for decades says the same thing again and again: roughly seven of ten wealth transfers fail by the second generation. By the third, it is closer to nine of ten. The inheritance arrives, and the family it was meant to bless comes apart around it.",
"When people hear those numbers, they assume the failures are technical — bad documents, bad tax planning, bad investments. That is not what I have found at the tables where I have sat. The clear majority of these breakdowns trace to broken trust and poor communication. About a quarter trace to heirs who were never prepared for what they received. Only a sliver — the smallest slice — comes down to financial mistakes. Which means most families spend most of their money guarding the smallest risk.",
"Scripture shows us how the drift happens, and the verse is quieter than you would expect. Judges says a generation arose \u201cwhich knew not the LORD, nor yet the works which he had done.\u201d It does not say they rebelled. It does not say they rejected anything. It says they did not know — because somewhere along the line, the telling stopped. Drift is rarely a decision. It is a silence, repeated.",
"Maybe you feel the ache of that in your own house — the conversation that has been easier to postpone than to have, the story that never quite gets told, the tension everyone has learned to step around. Hear me clearly: that ache is not condemnation. It is invitation. Families do not drift because they are bad; they drift because no one showed them how to steer. Tomorrow is about grace, and I mean that. Today is only about telling the truth.",
"You do not have to hold the conversation today. You only have to stop pretending it is not there.",
 ],
 q="Where has silence felt safer than conversation in your family?",
 step="Privately, on paper, name one conversation your family has been postponing. You are not committing to have it this week. You are simply done pretending it does not exist.",
 prayer="Father, You know the rooms in our family where the telling stopped. Give me the honesty to name what we have avoided — and the hope to believe that silence does not get the last word. Amen.",
 adv="The greatest threat to your clients\u2019 plans is not in the portfolio. It is an unheld conversation. The documents guard the smallest slice of the risk; the living room holds the rest. Think of one family on your book whose plan is excellent and whose communication is thin — that gap is where your next real work is.",
 ask="Ask them: \u201cYour plan says what you want done. Does your family know why?\u201d",
),
5: dict(
 slug="Day_Five_Family_Legacy.html",
 title="It\u2019s Not Too Late",
 dek="Whatever yesterday stirred up, today is for this: God restores years, and design can begin anywhere.",
 sv="And I will restore to you the years that the locust hath eaten\u2026",
 sref="Joel 2:25 · KJV",
 card="You don\u2019t need an advisor, a big estate, or a perfect plan to begin. You need a small yes.",
 body=[
"If yesterday\u2019s reading landed with a thud somewhere in your chest, this page is for you. Maybe the numbers sounded like your family\u2019s story already half-written. Maybe there is distance between you and a child, a parent, a sibling — and it has been there so long it feels structural. Maybe your family has never once prayed together, and starting now feels like walking into church for the first time and sitting in the front row.",
"So let me say what I have learned to say early and often: it is not too late. Restoring years is one of God\u2019s specialties — \u201cI will restore to you the years that the locust hath eaten.\u201d He does not say He will explain the years, or excuse them. He says He will restore them. Design does not require a blank page. God has been writing new chapters in used books for a very long time.",
"And you do not need much to begin. You do not need an advisor. You do not need a large estate. You certainly do not need a perfect plan or a perfect family — no one at this table has one, including the man writing these words. What you need is a small yes. One noticing, like Day Two\u2019s. One honest ranking, like Day Three\u2019s. One named conversation, like yesterday\u2019s. That is how a legacy turns from default toward design — not in a leap, but in a series of small yeses.",
"One more word, gently. Some family wounds are heavier than a forty-day journey is built to carry — deep estrangement, old harm, grief that still has weight. If that is your house, walking this road with a pastor or a counselor beside you is not a detour from the journey. It is wisdom, and it may be the most by-design decision you make all year. Go slow. Grace sets the pace here.",
"Passing on wealth without preparing hearts can leave confusion behind it. But the reverse is just as true, and it is today\u2019s good news: hearts can begin being prepared tonight — whatever the balance sheet says, and whatever the last ten years have said.",
 ],
 q="What would it look like to trade one regret for one beginning this week?",
 step="Finish this sentence on paper: \u201cIt is not too late for ______.\u201d Fold it. Bring it to this week\u2019s family conversation — sharing it is optional; carrying it is the point.",
 prayer="Lord of restored years, take what the locusts have eaten in our family and begin giving it back. I bring You my small yes today. Amen.",
 adv="Somewhere on your book is a family quietly convinced they have already failed — the estrangement, the inheritance that went badly once before. They do not need a grade from you; they need a guide. Restoration is a service no custodian offers, and it is the one this family will never forget.",
 ask="Call one of them this week: \u201cWould you be open to a fresh conversation about the family side of your plan — no documents, just the family?\u201d",
),
6: dict(
 slug="Day_Six_Family_Legacy.html",
 title="The Table",
 dek="Legacy travels at the speed of conversation. This is the week your family\u2019s table gets its job back.",
 sv="And thou shalt teach them diligently unto thy children, and shalt talk of them when thou sittest in thine house, and when thou walkest by the way, and when thou liest down, and when thou risest up.",
 sref="Deuteronomy 6:7 · KJV",
 card="Daily inspiration plus weekly conversation leads to family transformation — set the first table this week.",
 body=[
"If the first five days have been about seeing — the legacy already in motion, the five areas, the honest numbers, the grace to begin — today is about the delivery system. Because a legacy, whatever else it is, has to travel. And God\u2019s design for how it travels is almost embarrassingly ordinary: talking. At the table. In the car. At bedtime and at breakfast. Deuteronomy does not prescribe a seminar. It describes a rhythm.",
"That rhythm is the engine of the whole forty days, and it is simple enough to say in one line: daily inspiration plus weekly conversation leads to family transformation. A short reading each day — that is the inspiration; you are holding it now. One unhurried conversation each week — that is where the reading becomes the family\u2019s. Day after day, week after week, the ordinary rhythm does what no single dramatic moment can.",
"The table matters more here than we tend to admit. It is the family\u2019s original meeting room — older than any boardroom, and more consequential. What your family\u2019s calendar honors, your family becomes. Most households can find forty-five minutes for a practice, a show, a scroll. This week, the table gets forty-five of those minutes back.",
"So here is this week\u2019s assignment, and it is the most practical one yet: set the first Family Conversation. Pick the night. Pick the table. Then invite each person — not a group text; an actual invitation, by name. \u201cI\u2019d love you at the table Thursday. It matters to me that you\u2019re there.\u201d You will find the whole conversation laid out for you in Session One — the questions, the reading, the ground rules. Your only job today is to get it on the calendar.",
"And remember where this road ends. Day Forty is a family meeting, where commitments are named out loud. The weekly table is where you rehearse for it — one honest conversation at a time.",
 ],
 q="When did your family last have an unhurried conversation — no screens, no agenda except each other?",
 step="Set the day, time, and place for Session One this week. Then invite each person by name, personally. What gets scheduled gets to happen.",
 prayer="Father, give our table its job back. Set a time this week, guard it from the calendar\u2019s noise, and meet us there. Amen.",
 adv="What gets scheduled gets to happen — and some families need borrowed ground to schedule it on. Offering your conference room and a date can do more for a client family this week than any allocation change. Neutral territory plus a trusted witness is often the whole unlock.",
 ask="Offer it plainly: \u201cWould it help if the first family conversation happened at my office? I\u2019ll hold Thursday evening for you.\u201d",
),
7: dict(
 slug="Day_Seven_Family_Legacy.html",
 title="Before You Speak",
 dek="The first conversation isn\u2019t won by the best speech at the table. It\u2019s won by the best listening.",
 sv="Wherefore, my beloved brethren, let every man be swift to hear, slow to speak, slow to wrath.",
 sref="James 1:19 · KJV",
 card="Clarity begins in the ear — lower the bar on purpose, and let every voice be heard.",
 body=[
"Tonight, or sometime this week, your family sits down for Session One. So today\u2019s reading is short on new ideas and long on posture — because the first conversation will rise or fall on one thing, and it is not eloquence.",
"In our work with families we come back to three words: clarity, alignment, communication. Everyone assumes communication means talking. It does not — not at first. Communication begins in the ear. Before a family can align around anything, every voice has to actually be heard, and heard all the way to the end. James gives the order of operations: swift to hear, slow to speak. Notice which one comes first.",
"So lower the bar for tonight, on purpose. The goal of the first conversation is not agreement. It is not solving the thing you named on Day Four. It is not a breakthrough — though don\u2019t be surprised if one wanders in anyway. The goal is simpler, and rarer: everyone leaves the table having been heard. Hearts before spreadsheets, always. Some voices in your family have been waiting years for that. One of them may be yours.",
"Make one private resolution before you sit down: no one leaves the table smaller. Blessing outranks correction tonight. If a teenager says something half-formed, it gets received, not graded. If a grandparent circles an old story again, it gets honored — old stories circle because they carry cargo. You are not editing each other tonight. You are hearing each other.",
"Bring your papers — Day Two\u2019s caught-not-taught list, Day Five\u2019s folded sentence. Share what you choose; carry the rest. Then take a breath and remember the horizon this whole journey walks toward: not a tidy estate, but a family that hears \u201cwell done.\u201d That is worth forty-five careful minutes.",
 ],
 q="What do you hope to hear at the table this week? Not say — hear.",
 step="Before the conversation, write down one question you will ask, and one thing you will not bring up on this first night. Restraint is a gift you give the room.",
 prayer="Lord, make me swift to hear at my own table. Guard my tongue, soften my ears, and let every person You have placed in this family leave our first conversation larger, not smaller. Amen.",
 adv="If you are facilitating Session One this week, your instrument is the question mark. Aim for the family doing four-fifths of the talking, and write down their exact phrases — verbatim family language is the raw material the Day Forty meeting is built from.",
 ask="Open the evening with: \u201cMy job tonight is to ask and to listen. This table belongs to your family.\u201d",
),
}

NAV_CHAIN = [
    ("Day_One_Family_Legacy.html", "Day One · The Choice"),
    ("Day_Two_Family_Legacy.html", "Day Two · Already in Motion"),
    ("Day_Three_Family_Legacy.html", "Day Three · More Than Money"),
    ("Day_Four_Family_Legacy.html", "Day Four · Why Strong Families Drift"),
    ("Day_Five_Family_Legacy.html", "Day Five · It\u2019s Not Too Late"),
    ("Day_Six_Family_Legacy.html", "Day Six · The Table"),
    ("Day_Seven_Family_Legacy.html", "Day Seven · Before You Speak"),
    ("Session_One_Family_Legacy.html", "Session One · By Design"),
]

def day_page(n, d):
    i = n - 1  # index in NAV_CHAIN
    prev_href, prev_ttl = NAV_CHAIN[i - 1]
    next_href, next_ttl = NAV_CHAIN[i + 1]
    paras = "\n".join(f"<p>{p}</p>" for p in d["body"])
    body = f"""
<div class="col">
  <div class="kicker">Week One · Waking Up to Legacy</div>
  <h1>{d['title']}</h1>
  <p class="dek">{d['dek']}</p>
  <div class="rule"></div>
  <figure class="scripture">
    <p>\u201c{d['sv']}\u201d</p>
    <span class="ref">{d['sref']}</span>
  </figure>
  <div class="reading">
{paras}
  </div>
  <div class="block q"><div class="lab">Today\u2019s question</div><p>{d['q']}</p></div>
  <div class="block s"><div class="lab">Today\u2019s step</div><p>{d['step']}</p></div>
  <div class="block pr"><div class="lab">Prayer</div><p>{d['prayer']}</p></div>
  <section class="advisor" aria-label="For the advisor at the table">
    <div class="lab">For the advisor at the table</div>
    <p>{d['adv']}</p>
    <p class="ask">{d['ask']}</p>
  </section>
  <nav class="pn" aria-label="Day navigation">
    <a href="{prev_href}"><span class="dir">\u2190 Previous</span><span class="ttl">{prev_ttl}</span></a>
    <a class="next" href="{next_href}"><span class="dir">Next \u2192</span><span class="ttl">{next_ttl}</span></a>
  </nav>
</div>"""
    return shell(
        f"{d['title']} · Day {['','One','Two','Three','Four','Five','Six','Seven'][n]} — Family Legacy",
        f"Day {n} of the Family Legacy 40-day journey: {d['dek']}",
        body, f"Day {n} of 40", day=n)

# ---------------------------------------------------------------- session one
def session_page():
    body = """
<div class="col">
  <div class="kicker">Week One · The Family Conversation</div>
  <h1>Session One · By Design</h1>
  <p class="dek">Forty-five minutes. One table. Every voice. The first of six conversations on the road to Day Forty.</p>
  <div class="rule"></div>
  <div class="reading">
    <p>This is the first family conversation of the Family Legacy journey. Nothing here requires preparation beyond the week\u2019s readings — and even those are optional for anyone at the table who hasn\u2019t been reading along. The only requirement is presence. One person hosts and keeps the evening moving; everyone else just comes ready to talk, and readier to listen.</p>
  </div>

  <h2 style="font-family:'Besley',serif;font-weight:700;font-size:1.5rem;color:var(--green-deep);margin:2rem 0 .4rem">Three ground rules</h2>
  <div class="ground">
    <div><b>Every voice gets the floor.</b> Youngest to oldest, no exceptions — and no interruptions until a voice is finished.</div>
    <div><b>No fixing tonight.</b> This table is for hearing, not solving. The solving comes later in the journey.</div>
    <div><b>The table holds it.</b> What\u2019s shared here stays here, unless the person who shared it says otherwise.</div>
  </div>

  <div class="seg">
    <div class="min"><b>5</b>min</div>
    <div>
      <h3>Gather</h3>
      <p>Settle in. Phones in another room. Then the host reads this aloud, word for word or in their own words:</p>
      <div class="say"><p>\u201cWe\u2019re here because our family is choosing to leave its legacy on purpose. Nothing has to be decided tonight. We\u2019re just going to talk — and even more than that, we\u2019re going to listen.\u201d</p></div>
    </div>
  </div>

  <div class="seg">
    <div class="min"><b>10</b>min</div>
    <div>
      <h3>Open</h3>
      <p>One question, around the table, every person answering before anyone responds:</p>
      <div class="say"><p>\u201cWhat\u2019s one thing this family has given you that money couldn\u2019t buy?\u201d</p></div>
    </div>
  </div>

  <div class="seg">
    <div class="min"><b>5</b>min</div>
    <div>
      <h3>Read</h3>
      <p>Have two different voices read these aloud:</p>
      <figure class="scripture" style="margin-bottom:1rem">
        <p>\u201cA good man leaveth an inheritance to his children\u2019s children.\u201d</p>
        <span class="ref">Proverbs 13:22 · KJV · The campaign\u2019s core Scripture</span>
      </figure>
      <figure class="scripture">
        <p>\u201cWe will not hide them from their children, shewing to the generation to come the praises of the LORD, and his strength, and his wonderful works that he hath done.\u201d</p>
        <span class="ref">Psalm 78:4 · KJV</span>
      </figure>
      <p>Then the host frames it in one line: an inheritance that reaches children\u2019s children has to travel through rooms like this one. Conversations are the vehicle.</p>
    </div>
  </div>

  <div class="seg">
    <div class="min"><b>20</b>min</div>
    <div>
      <h3>Talk</h3>
      <p>Four questions. Go in order; it\u2019s fine not to finish all four. Depth beats coverage.</p>
      <div class="qs">
        <div><p>If we kept living exactly as we do now, what would this family hand the next generation by default?</p></div>
        <div><p>Of the five areas of our legacy — personal, family, financial, business, charitable — which one do we most want to grow in together?</p></div>
        <div><p>Where has silence been easier than conversation for us — and what has it cost?</p></div>
        <div><p>What would \u201clegacy by design\u201d look like in our house? Try to say it in one sentence.</p></div>
      </div>
    </div>
  </div>

  <div class="seg">
    <div class="min"><b>5</b>min</div>
    <div>
      <h3>Decide</h3>
      <p>This week\u2019s commitment — simple, and it pays off on Day Forty:</p>
      <div class="block s" style="margin:.6rem 0"><div class="lab">The envelope</div><p>Each person writes one hope for what this family will be by Day Forty. Fold it, initial it, and place it in a single envelope. Seal the envelope. It is opened at the family meeting on Day Forty — and not before.</p></div>
    </div>
  </div>

  <div class="seg">
    <div class="min">Close</div>
    <div>
      <h3>Pray</h3>
      <p>If it fits your family, let each person pray one sentence first. Then the host closes:</p>
      <div class="block pr" style="margin:.6rem 0"><p>Father, thank You for every person at this table. Take the ordinary conversations of this family and turn them into inheritance. Teach us to hear each other the way You hear us. Amen.</p></div>
    </div>
  </div>

  <section class="advisor" aria-label="For the advisor facilitating">
    <div class="lab">For the advisor facilitating</div>
    <p>If a family has asked you to guide this evening, hold the running order lightly — Gather 5, Open 10, Read 5, Talk 20, Decide and Pray 5 — and hold one rule tightly: the family does four-fifths of the talking. Ask, then wait longer than is comfortable. Capture their exact phrases in their exact words; verbatim family language is the raw material the Day Forty meeting is built from. Before anyone stands up, confirm next week\u2019s date. And remember where you sit: beside the family, never between its members.</p>
    <p class="ask">Facilitating all six conversations — and the Day Forty family meeting itself — is the heart of the Family Legacy certification path. Start at the <a href="index.html" style="color:var(--gold-soft)">campaign home</a>.</p>
  </section>

  <nav class="pn" aria-label="Session navigation">
    <a href="Day_Seven_Family_Legacy.html"><span class="dir">\u2190 Previous</span><span class="ttl">Day Seven · Before You Speak</span></a>
    <a class="next" href="Week_One_Family_Legacy.html"><span class="dir">Week One \u2192</span><span class="ttl">Back to the Week One overview</span></a>
  </nav>
</div>"""
    return shell(
        "Session One · By Design — The Week One Family Conversation",
        "The first family conversation of the Family Legacy journey: 45 minutes, one table, every voice — with a facilitation guide for advisors.",
        body, "Session One · Week One")

# --------------------------------------------------------------------- hub
def hub_page():
    cards = []
    d1 = ('<a class="card" href="Day_One_Family_Legacy.html">'
          '<div class="dn"><span>Day 1</span><span class="start">Start here</span></div>'
          '<h3>The Choice</h3><p>Every family is already leaving a legacy. The only choice left is whether it will be left by design — or by default.</p>'
          '<span class="sref">Proverbs 13:22</span></a>')
    cards.append(d1)
    for n in range(2, 8):
        d = DAYS[n]
        cards.append(
            f'<a class="card" href="{d["slug"]}">'
            f'<div class="dn"><span>Day {n}</span></div>'
            f'<h3>{d["title"]}</h3><p>{d["card"]}</p>'
            f'<span class="sref">{d["sref"].split(" · ")[0]}</span></a>')
    session = ('<a class="card session" href="Session_One_Family_Legacy.html">'
               '<div class="dn"><span>The Week One Family Conversation</span></div>'
               '<h3>Session One · By Design</h3>'
               '<p>Forty-five minutes, one table, every voice. The questions, the reading, the ground rules, and the envelope that gets opened on Day Forty — with a facilitation guide for advisors.</p>'
               '<span class="go">Open Session One \u2192</span></a>')
    cards.append(session)
    body = f"""
<div class="col">
  <div class="kicker">The Family Legacy Campaign · Series I · Flagship</div>
  <h1>Week One</h1>
  <p class="dek">Waking up to the legacy already in motion — seven short readings, and the family\u2019s first conversation.</p>
  <div class="rhythm">
    <span>One reading a day</span>
    <span>One conversation a week</span>
    <span>One family meeting on Day Forty</span>
  </div>
  <p class="engine">Daily inspiration plus weekly conversation leads to family transformation.</p>
  <div class="rule"></div>
  <div class="reading">
    <p>Week One does one thing: it wakes the household up. The readings move from the legacy your family is already leaving, to the five areas where legacy really lives, to the honest numbers behind failed inheritances — and then to grace, to the table, and to the posture that makes a first conversation safe. By week\u2019s end, your family has sat down together once, on purpose. That is the whole assignment, and it is enough.</p>
  </div>
</div>
<div class="cards">
{''.join(cards)}
</div>
<div class="col" style="margin-top:2.2rem">
  <a class="btn gold" href="Day_One_Family_Legacy.html">Start Day One \u2192</a>
  &nbsp; <a class="btn" href="Session_One_Family_Legacy.html">Open Session One</a>
</div>"""
    return shell(
        "Week One · Waking Up to Legacy — The Family Legacy Campaign",
        "Seven daily readings and the first family conversation: Week One of the flagship 40-day Family Legacy journey.",
        body, "Week One of Six", active="week")

# --------------------------------------------------------------------- write
(OUT / "flbd-weekone.css").write_text(CSS, encoding="utf-8")
for n, d in DAYS.items():
    (OUT / d["slug"]).write_text(day_page(n, d), encoding="utf-8")
(OUT / "Session_One_Family_Legacy.html").write_text(session_page(), encoding="utf-8")
(OUT / "Week_One_Family_Legacy.html").write_text(hub_page(), encoding="utf-8")

import os
for f in sorted(OUT.iterdir()):
    print(f.name, f.stat().st_size)
