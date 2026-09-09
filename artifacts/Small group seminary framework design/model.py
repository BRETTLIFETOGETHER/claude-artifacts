# -*- coding: utf-8 -*-
"""Doing Seminary Together — the business model when you never sell a degree."""
import io

CSS = """
:root{--ink:#0c1723;--ink2:#08111c;--gold:#c19a4b;--goldlt:#e2c689;--parch:#f7f3ea;
--parch2:#efe8da;--rule:#d9cfbc;--body:#2b2a26;--muted:#6d6759;--mutedlt:#9fb0c1;}
*{box-sizing:border-box}
body{margin:0;background:var(--parch);color:var(--body);
font-family:"Cormorant Garamond",Georgia,serif;font-size:19px;line-height:1.62}
.wrap{max-width:940px;margin:0 auto;padding:0 30px}
.narrow{max-width:700px}
h1,h2,h3,h4{font-family:"Playfair Display",Georgia,serif;margin:0;letter-spacing:-.01em}
.eyebrow{font-family:"Lato",sans-serif;font-weight:800;font-size:10px;letter-spacing:.26em;
text-transform:uppercase;color:var(--gold);display:block}
p{margin:0 0 15px}
header{background:var(--ink);color:#f3efe6;padding:74px 0 62px;position:relative;overflow:hidden}
header:before{content:"";position:absolute;inset:0;
background:radial-gradient(112% 78% at 7% 0%,rgba(193,154,75,.18),transparent 62%)}
header .wrap{position:relative}
header .eyebrow{color:var(--goldlt)}
header h1{font-size:clamp(36px,6.6vw,66px);line-height:1.0;color:#fbf8f1;margin-top:18px}
header h1 em{font-style:italic;font-weight:400;color:var(--goldlt)}
header .lede{font-size:22px;color:#cfc7b8;max-width:640px;margin-top:24px}
section{padding:64px 0 56px;border-bottom:1px solid var(--rule)}
section.dark{background:var(--ink2);color:#e6e0d3;border-bottom:none}
section.dark h2,section.dark h3,section.dark h4{color:#fbf8f1}
section.dark .kick{color:var(--mutedlt)}
section.dark p{color:#d6cec0}
section.tone{background:var(--parch2)}
h2.sec{font-size:clamp(27px,4.3vw,40px);line-height:1.09;margin-top:15px}
.kick{font-style:italic;color:var(--muted);margin:14px 0 0;max-width:640px;font-size:20px}
.pull{font-family:"Playfair Display",serif;font-size:24px;line-height:1.4;
border-left:3px solid var(--gold);padding-left:24px;margin:28px 0;max-width:660px}
section.dark .pull{color:var(--goldlt)}
.item{display:flex;gap:26px;padding:24px 0;border-top:1px solid var(--rule)}
section.dark .item{border-color:rgba(255,255,255,.13)}
.item .n{flex:0 0 50px;font-family:"Playfair Display",serif;font-size:32px;line-height:1;
color:transparent;-webkit-text-stroke:1px var(--gold);padding-top:2px}
section.dark .item .n{-webkit-text-stroke-color:var(--goldlt)}
.item .c{flex:1 1 auto;max-width:660px}
.item h4{font-size:21px;line-height:1.25;margin-bottom:8px}
.item p{margin:0 0 11px;font-size:18px}
.item p:last-child{margin-bottom:0}
.price{font-family:"Lato",sans-serif;font-size:12.5px;line-height:1.85;color:var(--muted);
border-left:2px solid var(--gold);padding-left:16px;margin:12px 0 0}
section.dark .price{color:var(--mutedlt)}
@media(max-width:640px){.item{gap:14px}.item .n{flex:0 0 34px;font-size:25px}}
table{width:100%;border-collapse:collapse;margin-top:28px;font-size:17px}
th{font-family:"Lato",sans-serif;font-weight:800;font-size:10px;letter-spacing:.15em;
text-transform:uppercase;color:var(--gold);text-align:left;padding:0 14px 11px 0;
border-bottom:1px solid var(--rule);vertical-align:bottom}
td{padding:14px 14px 14px 0;border-bottom:1px solid var(--rule);vertical-align:top}
td.k{font-family:"Playfair Display",serif;font-size:18px;width:26%}
td.s{color:var(--muted);font-size:16px}
td.num{font-family:"Lato",sans-serif;font-size:14px;white-space:nowrap}
.two{display:grid;grid-template-columns:1fr 1fr;gap:40px;margin-top:30px}
.two h4{font-size:20px;margin-bottom:9px}
.note{font-family:"Lato",sans-serif;font-size:13px;line-height:1.75;color:var(--muted);
border-top:1px solid var(--rule);margin-top:34px;padding-top:16px;max-width:720px}
section.dark .note{color:var(--mutedlt);border-color:rgba(255,255,255,.15)}
.close{background:var(--ink);color:#efeae0;padding:70px 0;text-align:center}
.close h2{font-size:clamp(27px,4.4vw,40px);color:#fbf8f1}
.close p{max-width:620px;margin:20px auto 0;color:#c9c0b0}
footer{background:#070d15;color:#7d8b99;padding:26px 0;font-family:"Lato",sans-serif;
font-size:10.5px;letter-spacing:.1em;text-align:center;text-transform:uppercase}
@media(max-width:720px){body{font-size:18px}.wrap{padding:0 20px}section{padding:48px 0 42px}
.two{grid-template-columns:1fr;gap:24px}}
"""

LINES = [
("Church site license", "The floor. Recurring, unglamorous, and not where you win.",
 """Annual, tiered by attendance, unlimited members and unlimited courses, all four delivery editions
 included, certificates printed by the church from the platform. This is the same budget line a church
 already spends on a video library, which sets both the price band and the ceiling. It is a real
 business and it is a grind: won one church at a time, renewed one church at a time.""",
 ["Under 250 attendance &nbsp;&mdash;&nbsp; $1,200 / year",
  "250 to 999 &nbsp;&mdash;&nbsp; $2,400 / year",
  "1,000 to 2,999 &nbsp;&mdash;&nbsp; $4,800 / year",
  "3,000 and above &nbsp;&mdash;&nbsp; $7,500 / year"]),
("Denominational and network license", "This is the actual company.",
 """One signature covers two hundred to two thousand churches. It is also the motion you have run for
 twenty-five years, and the one nobody else attempting this can run at all. A network licenses the
 full library for its churches, sets its own doctrinal line, and handles distribution internally,
 which means your cost of sale collapses and your renewal risk moves from a thousand small decisions
 to a handful of relationships. The recognition problem solves itself in the same stroke: a
 denomination that licenses the curriculum will eventually recognize the credential for lay
 licensing, because it is now their credential.""",
 ["Small network, under 100 churches &nbsp;&mdash;&nbsp; $30,000 / year",
  "Mid network, 100 to 500 &nbsp;&mdash;&nbsp; $80,000 / year",
  "Large denomination, 500 plus &nbsp;&mdash;&nbsp; $150,000 to $400,000 / year",
  "Priced per church, discounted steeply against the direct rate"]),
("Denominational editions", "Where the doctrinal problem becomes the product line.",
 """A twenty-discipline catalog necessarily touches baptism, eschatology, Calvinism, gender, and
 governance. Teaching all positions neutrally is the right default and it satisfies nobody
 completely. The edition solves it: the Reformed edition takes the Reformed position, the Wesleyan
 edition takes the Wesleyan one, and the denomination's own theologians sign the pages where it
 matters. Charge a setup fee for the customization and then the ongoing license on top. The deeper
 value is not the fee. It is that a denomination that has edited the curriculum now owns it, and
 organizations do not abandon what they have put their name inside.""",
 ["Edition setup, light &mdash; positions and language only &nbsp;&mdash;&nbsp; $25,000",
  "Edition setup, full &mdash; positions, added courses, branding &nbsp;&mdash;&nbsp; $75,000",
  "Then the network license rate on top, annually"]),
("Individual and leader subscription", "The funnel, not the business.",
 """A leader whose church has not licensed can subscribe directly. Keep it cheap, keep it simple, and
 do not build the model on it. Its real job is demand generation: a small group leader who finds it
 and loves it becomes the person who walks into the executive pastor's office and asks the church to
 buy it.""",
 ["$24 / month, or $199 / year",
  "Converts to a free seat the moment the leader's church licenses"]),
("Library and rights licensing", "The long tail nobody sees coming.",
 """Once a hundred credentialed faculty have taught on film, you hold a video library with real
 academic names attached to it. That is licensable well beyond the local church: to seminaries for
 their own non-degree tiers, to Bible colleges, to Christian schools, to international partners, and
 to publishers for derivative print. It is also the asset that makes the whole thing acquirable if
 you ever want that.""",
 ["Institutional library license &nbsp;&mdash;&nbsp; negotiated, typically $25,000 to $100,000 / year",
  "International and translation rights &nbsp;&mdash;&nbsp; granted free where the church cannot pay"]),
]

FACULTY = [
("Do not ask them to write. Ask them to correct.",
 """This is the move that makes four hundred courses possible, and it inverts every cost in
 traditional curriculum development. Asking a scholar to author a twelve-session course is asking for
 a hundred and fifty hours and eighteen months, and most will decline. Handing that same scholar a
 finished script in their own specialty and asking them to mark it up is asking for twenty hours, and
 most will say yes. The intellectual contribution is nearly identical. The friction is not
 comparable."""),
("Pay them properly and give them the reach.",
 """Honorarium plus a royalty on the course, not a favor and not exposure. But name the second thing
 honestly too: a professor whose course runs in two thousand churches has a platform no academic
 publisher can offer, and for many mid-career faculty that is the more valuable half of the
 deal."""),
("One scholar carries three to five courses.",
 """Nobody reviews four hundred courses and nobody should. A New Testament scholar takes the four or
 five in their actual specialty. A hundred faculty at four courses each is the full catalog, and it
 is the only arithmetic in which four hundred is a real number rather than an aspiration."""),
("The review is the doctrinal guardrail, and it is also the marketing.",
 """The heresy objection dies the moment every course carries a named author and a named reviewer with
 printed credentials. That same page is the strongest sales asset you will ever have, because a
 pastor deciding whether to trust this is not evaluating a platform, he is looking for names he
 recognizes."""),
("Film while you have them.",
 """A scholar who has already reviewed the script can teach it on camera in a single day. Capture the
 master session then, or you will be negotiating a second yes eighteen months later with someone
 whose calendar has moved on."""),
]

PHASES = [
("Year One", "Build the row, sign the first network",
 "20 flagship courses (the 101 row, one per discipline), 20 to 25 faculty recruited, "
 "the Tommy pilot running all four delivery editions, one denominational conversation to signature.",
 "~$300,000 build", "~$150,000 revenue", "Net negative. This is the investment year and should be named as one."),
("Year Two", "Depth in the disciplines churches ask for",
 "80 more courses, 60 faculty total, first two denominational editions shipped, "
 "150 churches direct, three network licenses.",
 "~$1,200,000 build", "~$1,000,000 revenue", "Approaching breakeven on operations, still funding content."),
("Year Three", "Catalog past 200, editions as a real line",
 "100 more courses, the individual subscription opened, library licensing begins, "
 "500 churches direct, eight networks.",
 "~$1,500,000 build", "~$3,000,000 revenue", "First materially profitable year. Content spend continues by choice, not necessity."),
]


def build():
    h = io.StringIO(); W = h.write
    W("""<!DOCTYPE html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>The Business Model &mdash; Doing Seminary Together</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,700;1,400&family=Cormorant+Garamond:ital,wght@0,400;0,600;1,400&family=Lato:wght@300;400;700;800&display=swap" rel="stylesheet">
<style>""" + CSS + "</style></head><body>")

    W("""<header><div class="wrap">
<span class="eyebrow">Doing Seminary Together &nbsp;&middot;&nbsp; Business Model</span>
<h1>What you sell<br><em>when you never sell a degree</em></h1>
<p class="lede">Certificate of completion only. No accreditation, no assessment obligation, no
registrar. That is not a lesser business than an accredited one. It is a structurally better one,
and this is why.</p>
</div></header>""")

    W("""<section><div class="wrap"><div class="narrow">
<span class="eyebrow">The Reframe</span>
<h2 class="sec">Drop the certification and the economics stop being a school's</h2>
<div style="margin-top:22px">
<p>Every expensive thing about a seminary comes from the credential rather than the content. The
registrar exists because credits transfer. Financial aid administration exists because degrees
qualify for it. Accreditation compliance, faculty tenure, library requirements, student services, the
reader who has to grade every paper because the grade means something legally — all of it is
downstream of granting a degree.</p>
<p>Remove the degree and every one of those costs disappears. What remains is content production,
faculty honoraria, a platform, and account support. That is a publishing cost structure. You build a
course once and license it indefinitely at no marginal cost per student, which means the hundredth
church costs almost nothing to serve and the thousandth costs less.</p>
<div class="pull">You are not selling education to students. You are selling formation
infrastructure to institutions, and the certificate is the thing that makes the institution look
good for buying it.</div>
<p>That single sentence determines everything else. The customer is the church or the denomination,
not the member. The product is a system a church can run, not a course a person takes. And the
certificate, which generates no revenue at all, is the highest-leverage object in the entire model
because it is what makes completion visible, repeatable, and worth celebrating from a platform on a
Sunday morning.</p>
</div></div></div></section>""")

    W("""<section class="dark"><div class="wrap">
<span class="eyebrow">Revenue</span>
<h2 class="sec">Five lines, and only one of them is the company</h2>
<p class="kick">Numbers below are straw. They are here to be argued with, not believed.</p>""")
    for i, (name, tag, body, prices) in enumerate(LINES, 1):
        W('<div class="item"><span class="n">%d</span><div class="c"><h4>%s</h4>'
          '<p style="font-style:italic;color:var(--goldlt);margin-bottom:10px">%s</p><p>%s</p>'
          '<div class="price">%s</div></div></div>'
          % (i, name, tag, " ".join(body.split()), "<br>".join(prices)))
    W("""<p class="note">The honest read on line one: church-by-church licensing puts you in the most
crowded band in church media, competing against video libraries that have been buying that budget
line for a decade. You will win some of it and it will never be the business. Lines two and three are
the business, and they are the two nobody else attempting this can execute, because they run on
denominational relationships rather than on marketing spend.</p>
</div></section>""")

    W("""<section class="tone"><div class="wrap"><div class="narrow">
<span class="eyebrow">The Certificate</span>
<h2 class="sec">It earns nothing and it is the most valuable thing you make</h2>
<div class="two">
<div><h4>What it actually does</h4>
<p><b>Retention.</b> A member with eleven completed courses on record does not restart that record
somewhere else. Nobody in church media has a switching cost. You would.</p>
<p><b>Status.</b> The church gets something to hand somebody in front of the congregation. Public
completion is the single best enrollment driver a program like this has, and it costs you a sheet of
paper.</p>
<p><b>Proof.</b> Completions are the only metric that demonstrates the product works, and that
number is what you carry into a denominational negotiation and into the first conversation with an
accredited school.</p></div>
<div><h4>What you deliberately do not sell</h4>
<p><b>Tuition.</b> The moment a student pays for education rather than a church paying for
curriculum, you have implied an assessment obligation you have chosen not to carry.</p>
<p><b>Degrees, or anything that sounds like one.</b> Legal exposure, and a promise you cannot
keep.</p>
<p><b>Per-course fees as the primary line.</b> They suppress exactly the volume that makes the
certificate valuable. Let the courses be free inside a license and charge for the license.</p></div>
</div>
<p class="note">Print the ceiling on the certificate itself: hours completed, what was covered, and in
the same size type, that it is not a degree, not accreditation, and not a qualification for ordination
or counseling. This is the integrity objection, and it is fully answerable for the cost of one line of
type.</p>
</div></div></section>""")

    W("""<section><div class="wrap">
<span class="eyebrow">Production</span>
<h2 class="sec">The hundred faculty model</h2>
<p class="kick">Your instinct here is the thing that makes the catalog buildable. It deserves to be
written down as a method rather than left as a hunch.</p>""")
    for i, (head, body) in enumerate(FACULTY, 1):
        W('<div class="item"><span class="n">%d</span><div class="c"><h4>%s</h4><p>%s</p></div></div>'
          % (i, head, " ".join(body.split())))
    W("""<table>
<tr><th>Per course, all in</th><th>Straw cost</th><th>Note</th></tr>
<tr><td class="k">Script</td><td class="num">$3,000 &ndash; 5,000</td><td class="s">Twelve sessions written to the fixed six-stage shape</td></tr>
<tr><td class="k">Faculty review</td><td class="num">$2,000 &ndash; 4,000</td><td class="s">Share of a set honorarium covering three to five courses</td></tr>
<tr><td class="k">Filming</td><td class="num">$4,000 &ndash; 7,000</td><td class="s">One day per scholar, multiple courses captured together</td></tr>
<tr><td class="k">Workbook and design</td><td class="num">$2,000 &ndash; 3,000</td><td class="s">Participant, facilitator, and the four editions</td></tr>
<tr><td class="k">Total</td><td class="num">$12,000 &ndash; 19,000</td><td class="s">Call it $15,000 straw. Four hundred courses is roughly $6M, which is why the twenty-course Year One row is the only sane starting point</td></tr>
</table>
<p class="note">Every existing asset that converts is a course you do not pay full freight for.
Deepening Life Together, the Adult Bible Fellowship material, and the campaign backlist are all
conversion candidates, and conversion runs at a fraction of new build. Audit the shelf before
commissioning anything.</p>
</div></section>""")

    W("""<section class="dark"><div class="wrap">
<span class="eyebrow">Three Year Straw</span>
<h2 class="sec">What the shape looks like</h2>
<table style="color:#e6e0d3">
<tr><th>Year</th><th>Focus</th><th>Build</th><th>Revenue</th></tr>""")
    for yr, focus, detail, build, rev, note in PHASES:
        W('<tr><td class="k" style="color:#fbf8f1">%s</td>'
          '<td><b style="font-family:Playfair Display,serif">%s</b><br>'
          '<span style="color:var(--mutedlt);font-size:16px">%s</span></td>'
          '<td class="num" style="color:var(--mutedlt)">%s</td>'
          '<td class="num" style="color:var(--goldlt)">%s<br>'
          '<span style="color:var(--mutedlt);font-size:12px">%s</span></td></tr>'
          % (yr, focus, detail, build, rev, note))
    W("""</table>
<p class="note">The load-bearing assumption in all of this is the denominational line. If networks
sign, the model works at these numbers and probably better. If they do not, this becomes a
church-by-church media business with a good product and ordinary economics, and the honest move at
that point is to say so early rather than to grind.</p>
</div></section>""")

    W("""<section class="tone"><div class="wrap">
<span class="eyebrow">Open Decisions</span>
<h2 class="sec">Four things that have to be settled before the pilot</h2>

<div class="item"><span class="n">1</span><div class="c">
<h4>The name. Doing Seminary Together is better than Small Group Seminary.</h4>
<p>It sits inside the family you already built — Doing Life Together, then Deepening Life Together,
now this — which means it arrives carrying twenty-five years of recognition rather than starting
from zero. It also does something quieter and more useful: making seminary the thing you are doing
together rather than the institution you are attending lowers the credential claim without hiding
anything, which is exactly the posture the integrity objection requires. Keep SmallGroupSeminary.com
as the domain and the search asset. Lead with Doing Seminary Together as the brand.</p></div></div>

<div class="item"><span class="n">2</span><div class="c">
<h4>The cat is out of the bag, and how you say that determines who your allies are.</h4>
<p>The underlying claim is true. Laypeople are already pursuing theological formation without
institutional oversight, on video platforms and increasingly by asking a chatbot doctrinal questions
at midnight, and no institution is going to put that back. But there are two ways to say it. Said one
way it means the seminaries have lost and should get out of the road, which starts a fight you cannot
win and do not need. Said the other way it means unsupervised theological formation is now the
default, and the only open question is whether it happens with a curriculum, a named faculty, and a
church around it. That version makes every dean in the country an ally.</p></div></div>

<div class="item"><span class="n">3</span><div class="c">
<h4>Placing this under the Rick arrangement.</h4>
<p>I do not know the terms, so this is a flag rather than a recommendation. Three things change
depending on the answer. Distribution and credibility accelerate enormously, and that is the obvious
half. Less obvious: the terms will govern who owns the filmed faculty content and the derivative
rights, which is the single most valuable long-term asset in the model, and that needs to be explicit
before a hundred scholars are recorded. And the association narrows you slightly with confessional
and Reformed networks who read Purpose Driven as a theological position rather than a method —
which matters precisely because denominational licensing is the business. Worth mapping which
networks it opens and which it closes before signing.</p></div></div>

<div class="item"><span class="n">4</span><div class="c">
<h4>What the Tommy pilot has to produce.</h4>
<p>Not enrollment. A pilot that produces enthusiasm and no artifacts has cost you a year. It has to
produce four things: a defensible transcript for at least one finished student, completion and drop
rates by delivery edition, a facilitator who was trained rather than gifted and still succeeded, and
a signed testimonial from the senior pastor about what changed in the church. Those four are what you
carry into the first denominational meeting and into the first conversation with Talbot. Design the
pilot backward from them.</p></div></div>
</div></section>""")

    W("""<div class="close"><div class="wrap">
<h2>Sell the license. Give away the certificate.<br>The certificate is what makes the license
renew.</h2>
<p>Church and network licensing carries the revenue, denominational editions carry the margin and the
loyalty, and the hundred faculty carry the credibility that makes all three possible.</p>
</div></div>
<footer><div class="wrap">LifeTogether Ministries &middot; Doing Seminary Together &middot; Business
model straw &middot; August 2026</div></footer></body></html>""")
    return h.getvalue()


if __name__ == "__main__":
    out = build()
    p = "/mnt/user-data/outputs/doing-seminary-together-business-model.html"
    open(p, "w", encoding="utf-8").write(out)
    print("bytes:", len(out), "| div balance:", out.count("<div") - out.count("</div>"),
          "| sections:", out.count("<section"), out.count("</section>"))
