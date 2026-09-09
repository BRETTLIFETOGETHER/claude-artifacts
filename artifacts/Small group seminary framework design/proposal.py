# -*- coding: utf-8 -*-
"""The Pastor's Library Project — pastor and board facing proposal."""
import io

CSS = """
:root{--ink:#0c1723;--ink2:#08111c;--gold:#c19a4b;--goldlt:#e2c689;--parch:#f7f3ea;
--parch2:#efe8da;--rule:#d9cfbc;--body:#2b2a26;--muted:#6d6759;--mutedlt:#9fb0c1;}
*{box-sizing:border-box}
body{margin:0;background:var(--parch);color:var(--body);
font-family:"Cormorant Garamond",Georgia,serif;font-size:19px;line-height:1.63}
.wrap{max-width:900px;margin:0 auto;padding:0 34px}
h1,h2,h3,h4{font-family:"Playfair Display",Georgia,serif;margin:0;letter-spacing:-.01em}
.eyebrow{font-family:"Lato",sans-serif;font-weight:800;font-size:10px;letter-spacing:.26em;
text-transform:uppercase;color:var(--gold);display:block}
p{margin:0 0 15px}
.ph{background:#fff5d9;border-bottom:1px dotted var(--gold);padding:0 3px;font-style:normal}
header{background:var(--ink);color:#f3efe6;padding:80px 0 66px;position:relative;overflow:hidden}
header:before{content:"";position:absolute;inset:0;
background:radial-gradient(112% 80% at 8% 0%,rgba(193,154,75,.2),transparent 62%)}
header .wrap{position:relative}header .eyebrow{color:var(--goldlt)}
header h1{font-size:clamp(34px,6vw,60px);line-height:1.02;color:#fbf8f1;margin-top:18px}
header h1 em{font-style:italic;font-weight:400;color:var(--goldlt)}
header .prep{margin-top:34px;border-top:1px solid rgba(193,154,75,.32);padding-top:20px;
font-family:"Lato",sans-serif;font-size:12px;letter-spacing:.09em;line-height:2;color:#a9b6c4}
header .prep b{color:var(--goldlt);letter-spacing:.16em;text-transform:uppercase;font-size:9.5px;
display:inline-block;min-width:118px}
section{padding:58px 0 50px;border-bottom:1px solid var(--rule)}
section.dark{background:var(--ink2);color:#e6e0d3;border-bottom:none}
section.dark h2,section.dark h3,section.dark h4{color:#fbf8f1}
section.dark p{color:#d6cec0}
section.tone{background:var(--parch2)}
h2.sec{font-size:clamp(26px,4.1vw,38px);line-height:1.1;margin-top:13px;max-width:780px}
.kick{font-style:italic;color:var(--muted);margin:13px 0 0;max-width:640px;font-size:20px}
section.dark .kick{color:var(--mutedlt)}
.narrow{max-width:700px}
.pull{font-family:"Playfair Display",serif;font-size:23px;line-height:1.42;
border-left:3px solid var(--gold);padding-left:24px;margin:26px 0;max-width:660px}
section.dark .pull{color:var(--goldlt)}
.ws{border-top:1px solid var(--rule);padding:24px 0}
.ws h3{font-size:22px;margin-bottom:4px}
.ws .who{font-family:"Lato",sans-serif;font-size:10.5px;letter-spacing:.15em;text-transform:uppercase;
color:var(--gold);margin-bottom:10px}
.ws ul{margin:0;padding-left:20px}.ws li{margin-bottom:6px;font-size:18px}
.out{display:flex;gap:16px;padding:12px 0;border-bottom:1px solid var(--rule);align-items:baseline}
.out .mark{flex:0 0 16px;color:var(--gold);font-size:14px}
.out .txt{flex:1;font-size:18.5px}
section.dark .out{border-color:rgba(255,255,255,.13)}
table{width:100%;border-collapse:collapse;margin-top:24px;font-size:17px}
th{font-family:"Lato",sans-serif;font-weight:800;font-size:10px;letter-spacing:.15em;
text-transform:uppercase;color:var(--gold);text-align:left;padding:0 14px 11px 0;
border-bottom:1px solid var(--rule);vertical-align:bottom}
td{padding:13px 14px 13px 0;border-bottom:1px solid var(--rule);vertical-align:top}
td.k{font-family:"Playfair Display",serif;font-size:17.5px;width:32%}
td.n{font-family:"Lato",sans-serif;font-size:14.5px;white-space:nowrap;color:var(--gold);font-weight:700;text-align:right}
td.s{color:var(--muted);font-size:16.5px}
tr.total td{border-bottom:none;border-top:2px solid var(--gold);padding-top:16px}
tr.total td.k{font-size:19px}tr.total td.n{font-size:17px}
section.dark td{border-color:rgba(255,255,255,.13)}
section.dark td.k{color:#fbf8f1}section.dark td.s{color:var(--mutedlt)}
section.dark td.n{color:var(--goldlt)}
.qa{border-top:1px solid var(--rule);padding:20px 0}
.qa h4{font-size:20px;margin-bottom:8px}
.qa p{margin:0;font-size:18px}
.honest{border:1px solid var(--gold);background:#fff;padding:24px 26px;margin-top:28px}
.honest h4{font-family:"Lato",sans-serif;font-size:10px;font-weight:800;letter-spacing:.2em;
text-transform:uppercase;color:var(--gold);margin-bottom:12px}
.honest p{font-size:17.5px;margin-bottom:12px}.honest p:last-child{margin-bottom:0}
.note{font-family:"Lato",sans-serif;font-size:13px;line-height:1.75;color:var(--muted);
border-top:1px solid var(--rule);margin-top:28px;padding-top:15px;max-width:700px}
section.dark .note{color:var(--mutedlt);border-color:rgba(255,255,255,.15)}
.close{background:var(--ink);color:#efeae0;padding:70px 0;text-align:center}
.close h2{font-size:clamp(25px,4vw,38px);color:#fbf8f1}
.close p{max-width:600px;margin:18px auto 0;color:#c9c0b0}
.close .sig{margin-top:34px;font-family:"Lato",sans-serif;font-size:11px;letter-spacing:.16em;
text-transform:uppercase;color:#8ea1b4;line-height:2.1}
footer{background:#070d15;color:#7d8b99;padding:24px 0;font-family:"Lato",sans-serif;
font-size:10.5px;letter-spacing:.1em;text-align:center;text-transform:uppercase}
@media(max-width:720px){body{font-size:18px}.wrap{padding:0 20px}section{padding:44px 0 38px}
td.k{width:auto}}
@media print{header,section.dark,.close{-webkit-print-color-adjust:exact;print-color-adjust:exact}
section{page-break-inside:avoid}}
"""

def P(x):
    return '<span class="ph">%s</span>' % x

WORKSTREAMS = [
("The Archive", "Weeks 1 to 8",
 ["Full intake of everything &mdash; files, folders, drives, cassettes, and the boxes in the office nobody has opened in years",
  "Digitization, transcription, and cleanup of the complete preaching record",
  "Indexing by topic, book, passage, occasion, formation outcome and campaign hinge",
  "<b>The Coverage Report</b> &mdash; what has been preached, what has never been preached, and where the gaps are",
  "A written rights and ownership review, so the board knows exactly what the church holds"]),
("The Library", "Months 2 to 6",
 ["Ten timeless small group studies drawn from " + P("[Pastor]") + "'s own preaching",
  "The membership series and the vision-and-values campaign",
  "The top felt-need series, selected from the Coverage Report rather than from instinct",
  "A financial health track and a generosity track built on his convictions, not a licensed program",
  "Easter and Christmas devotional series, written to be reused every year"]),
("The Publication", "Months 4 to 10",
 ["The book &mdash; manuscript, cover, interior design, and print-ready files",
  "The churchwide campaign built from the book, in the forty-day shape",
  "Journals and participant workbooks, print-ready",
  "Narrated audio editions of the core library"]),
("The Platform and the Partnership", "Months 1 to 12",
 ["The working Pastor's Library site: search, sort, filter, and staff access from any device",
  "The twenty-part church intelligence library, benchmarked against current practice",
  "An eighteen-month preaching calendar with campaigns positioned",
  "Three to four timely campaigns aimed at what the next eighteen months will actually require",
  "Monthly working sessions with " + P("[Pastor]") + " and the team for twelve months"]),
]

OUTCOMES = [
"Eighteen months of preaching planned, written, and aligned across the pulpit, the groups, and the households.",
"Every message ever preached at " + P("[Church]") + " digitized, indexed, and findable in seconds.",
"One complete book manuscript in " + P("[Pastor]") + "'s own voice and under his own name.",
"Ten small group studies so the groups in this church are studying their own pastor.",
"Four launch-ready campaigns including Easter and Christmas, each with sermon, devotional, group session, children's version and print file.",
"A membership series and a vision-and-values series the staff can run without the senior pastor in the room.",
"A searchable platform the whole staff uses, and a preaching calendar that answers what comes next before anyone asks.",
"An archive complete enough that a successor could run this church's teaching calendar from it alone.",
]

BOARD = [
("Who owns the work?",
 """The church owns everything produced in this engagement &mdash; the studies, the campaigns, the
 devotional series, the platform content, and the book's church-use rights. """ + P("[Pastor]") + """
 retains authorship credit and personal-use rights to his own sermons, and receives a complete
 personal copy of the digitized archive. LifeTogether retains only its own engine, templates, and
 production systems, which are the tools rather than the output. All of this is written into the
 agreement rather than assumed."""),
("What happens if the pastor leaves?",
 """The library stays. That is a large part of why this is worth doing. Today, thirty years of this
 church's teaching lives in one man's memory and one man's filing system, and the day he leaves,
 most of it leaves with him. When this engagement is finished, the church holds the teaching record,
 the campaigns, the curriculum, and the calendar independent of any individual."""),
("What does it cost after the first year?",
 """Nothing is required. The platform subscription is included for three full years as part of the
 engagement. If the church chooses to continue past year three, it renews at the standard rate for
 its size, and if it does not, the church keeps every file produced during the engagement in a
 permanent, exportable form."""),
("How do we know it is working?",
 """Four checkpoints with defined deliverables: the Coverage Report at week eight, the platform live
 with the full archive indexed at month four, the first campaign launched at month six, and the book
 manuscript complete at month ten. Each is a specific artifact the board can look at. If the week
 eight report does not convince you, the engagement can stop there."""),
("What is the real risk?",
 """That the church buys a large project and it becomes a folder nobody opens. That risk is real, and
 the two things that reduce it are both in the design: the monthly working sessions keep it on
 somebody's calendar, and the preaching calendar makes the library load-bearing rather than
 optional. If the archive is where next month's sermon comes from, it does not become a folder."""),
]


def build():
    h = io.StringIO(); W = h.write
    W("""<!DOCTYPE html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>The Pastor's Library Project &mdash; Proposal</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,700;1,400&family=Cormorant+Garamond:ital,wght@0,400;0,600;1,400&family=Lato:wght@300;400;700;800&display=swap" rel="stylesheet">
<style>""" + CSS + "</style></head><body>")

    W("""<header><div class="wrap">
<span class="eyebrow">A Proposal from LifeTogether Ministries</span>
<h1>The Pastor's<br><em>Library Project</em></h1>
<div class="prep">
<b>Prepared for</b>""" + P("[Pastor Name]") + """ and the Board of """ + P("[Church Name]") + """<br>
<b>Prepared by</b>Brett Eastman, LifeTogether Ministries<br>
<b>Date</b>""" + P("[Date]") + """<br>
<b>Valid through</b>""" + P("[Date + 60 days]") + """
</div></div></header>""")

    # 1 situation
    W("""<section><div class="wrap"><div class="narrow">
<span class="eyebrow">The Situation</span>
<h2 class="sec">Thirty years of work, and almost none of it can be found</h2>
<div style="margin-top:22px">
<p>We have worked with more than five hundred churches over twenty-five years, and the same thing is
true in nearly every one of them. The most valuable teaching asset the congregation owns is the
senior pastor's own body of work, and it is the one asset nobody has ever helped him steward.</p>
<p>A pastor we worked with had handwritten every message he ever preached. Boxes of paper in a garage.
Thirty years of study, prayer, and pastoral care, sitting in cardboard, and every Monday morning he
started a new message from nothing anyway.</p>
<div class="pull">The most under-stewarded resource in any congregation is the senior pastor's own
library. He has already done the work. Nobody has ever helped him keep it.</div>
<p>This proposal is not a criticism of how """ + P("[Church]") + """ has operated. Every church we
know is in the same position, because there has never been anyone whose job it was to do anything
about it. What follows is a twelve-month engagement to change that, and to turn what
""" + P("[Pastor]") + """ has already preached into something this church can use for the next
decade.</p>
</div></div></div></section>""")

    # 2 what we propose
    W("""<section class="tone"><div class="wrap">
<span class="eyebrow">What We Propose</span>
<h2 class="sec">Four workstreams over twelve months</h2>
<p class="kick">Aggregate. Curate. Customize. Publish. The same four moves in every engagement, run
in sequence so the church sees progress every month rather than at the end.</p>""")
    for name, when, items in WORKSTREAMS:
        W('<div class="ws"><h3>%s</h3><div class="who">%s</div><ul>' % (name, when))
        for it in items:
            W("<li>%s</li>" % it)
        W("</ul></div>")
    W("</div></section>")

    # 3 the platform bundle
    W("""<section class="dark"><div class="wrap">
<span class="eyebrow">Included at No Additional Charge</span>
<h2 class="sec">The whole LifeTogether platform, for three years</h2>
<p class="kick">The library is what we build for this church. The platform is everything we have
already built for every church, and it comes with the engagement.</p>
<div style="max-width:700px;margin-top:24px">
<p>An archive on its own is a filing cabinet. What makes it useful is the system that reads it,
searches it, and turns it into something the church can run on a Sunday. That system already exists,
and rather than sell it separately we include it, because the engagement does not work without
it.</p>
</div>
<table style="color:#e6e0d3">
<tr><th>What is included</th><th>What it is</th><th>Value if bought alone</th></tr>
<tr><td class="k">Church All-Access, three years</td><td class="s">The full LifeTogether intelligence operating system across all six ministry environments &mdash; the weekend, the week, the group, the classroom, the team, and the household. Unlimited seats for staff, volunteers, group leaders and members.</td><td class="n">$10,470</td></tr>
<tr><td class="k">The Sermon Curator platform</td><td class="s">5,155 messages across 73 categories, searchable alongside this church's own archive, with service design, illustration prompts and next-step architecture attached to each one.</td><td class="n">Included in All-Access</td></tr>
<tr><td class="k">The 40 Days campaign library</td><td class="s">17,319 churchwide campaigns across 23 channels, each with sermon builds, daily devotionals and group sessions. Unlimited use for three years rather than priced per campaign.</td><td class="n">$17,910</td></tr>
<tr><td class="k">All 22 diagnostics</td><td class="s">Free permanently for every church, including this one. Ministry health, staff, groups, generosity, and formation.</td><td class="n">No charge, ever</td></tr>
<tr class="total"><td class="k">Platform value included</td><td class="s">Three years, no additional cost, no renewal obligation</td><td class="n">$28,380</td></tr>
</table>
<p class="note">Why we include rather than sell it: the engagement produces a profile of this church
&mdash; its pastor, its people, its season, its gaps &mdash; that nothing else we do can produce. The
platform is what reads that profile. Charging separately for the thing that makes the work usable
would be selling a car and invoicing for the keys.</p>
</div></section>""")

    # 4 outcomes
    W("""<section><div class="wrap">
<span class="eyebrow">Outcomes</span>
<h2 class="sec">What is true twelve months from now</h2>
<div style="margin-top:24px;max-width:740px">""")
    for o in OUTCOMES:
        W('<div class="out"><span class="mark">&#9679;</span><span class="txt">%s</span></div>' % o)
    W("""</div>
<p class="note">We make no claims about attendance, giving, or engagement. Those depend on a great
many things outside this engagement, and any provider who promises them should be asked how they
intend to prove it.</p>
</div></section>""")

    # 5 board section
    W("""<section class="tone"><div class="wrap">
<span class="eyebrow">For the Board</span>
<h2 class="sec">The five questions a board should ask</h2>
<p class="kick">Answered here rather than in a meeting, so the conversation can be about whether to
do it rather than about what it is.</p>
<div style="margin-top:26px;max-width:730px">""")
    for q, a in BOARD:
        W('<div class="qa"><h4>%s</h4><p>%s</p></div>' % (q, " ".join(a.split())))
    W("</div></div></section>")

    # 6 investment
    W("""<section class="dark"><div class="wrap">
<span class="eyebrow">Investment</span>
<h2 class="sec">Four levels. Our recommendation for """ + P("[Church]") + """ is Level Three.</h2>
<table style="color:#e6e0d3">
<tr><th>Level</th><th>Scope</th><th>Investment</th></tr>
<tr><td class="k">One &middot; Discovery and Audit</td><td class="s">Intake, digitization sample, the Coverage Report, an architecture recommendation, and one message produced end to end. Four to six weeks.</td><td class="n">$8,500 &ndash; 15,000</td></tr>
<tr><td class="k">Two &middot; The Working Library</td><td class="s">Full archive indexed, platform live, ten studies, one campaign, twelve-month preaching calendar.</td><td class="n">$28,000 &ndash; 45,000</td></tr>
<tr><td class="k">Three &middot; The Full System</td><td class="s">Everything in this proposal: all four workstreams, the book and its campaign, Easter and Christmas, financial health and generosity, membership, vision and values, and twelve months of partnership.</td><td class="n">$65,000 &ndash; 125,000</td></tr>
<tr><td class="k">Four &middot; The Legacy Edition</td><td class="s">Adds the Transition File for succession, the weddings and funerals archive, the counseling playbook, a next-generation translation of the core teaching, a second-language edition, and full rights and estate work.</td><td class="n">$175,000 +</td></tr>
</table>
<h3 style="font-size:23px;margin-top:40px">Three ways churches fund this</h3>
<table style="color:#e6e0d3">
<tr><th>Source</th><th>How it usually works</th></tr>
<tr><td class="k">The church budget</td><td class="s">Approved as curriculum and communications spend, often replacing what the church already pays for licensed studies and campaign materials.</td></tr>
<tr><td class="k">One family</td><td class="s">A household in the congregation funds it as a gift honoring their pastor. This is the most common path at Level Three, and it is frequently the most meaningful thing that family has ever given toward.</td></tr>
<tr><td class="k">A foundation</td><td class="s">Funded as part of a named cohort of churches, with a published standard and a shared coverage report.</td></tr>
</table>
<p class="note">Payment is milestone-based, not up front: thirty percent at signing, thirty percent at
the Coverage Report, twenty-five percent at platform launch, and fifteen percent on delivery of the
manuscript.</p>
</div></section>""")

    # 7 honest status + founding
    W("""<section><div class="wrap"><div class="narrow">
<span class="eyebrow">Where This Stands</span>
<h2 class="sec">What you should know before deciding</h2>
<div class="honest"><h4>Said plainly</h4>
<p>We have built the components of this over twenty-five years &mdash; the campaign library, the
curriculum system, the sermon platform, the production engine. We have not yet completed a full
Pastor's Library engagement end to end for a single church. """ + P("[Church]") + """ would be among
the first.</p>
<p>We would rather tell you that than have you discover it. It is also why the founding terms below
exist, and why the engagement is structured so you can stop after the Coverage Report at week eight
if what you see does not convince you.</p>
</div>
<h3 style="font-size:23px;margin-top:36px">Founding cohort terms</h3>
<p style="margin-top:14px">For the first ten churches, the engagement is offered at a reduced rate,
with the platform locked at today's pricing for three years. In exchange we ask three things, and
only three: that the church actually uses it, with the platform live and the first campaign launched
within six months; one honest twenty-minute call each quarter about what is working and what is not;
and one approved case study at the end of the year. We will ask for introductions only if the work
has been good, and never as a condition.</p>
<p class="note">Placeholders in this document are marked in yellow and must be filled before it
travels. Investment figures shown are the standard ladder; the specific number for
""" + P("[Church]") + """ appears on the signature page.</p>
</div></div></section>""")

    W("""<div class="close"><div class="wrap">
<h2>Start with week eight.</h2>
<p>The Coverage Report will tell you, in print, what this church has preached for thirty years and
what it has never preached once. Whatever you decide about the rest, that document is worth having.
Let us begin there.</p>
<div class="sig">Brett Eastman &nbsp;&middot;&nbsp; LifeTogether Ministries<br>
""" + P("[email]") + """ &nbsp;&middot;&nbsp; """ + P("[phone]") + """</div>
</div></div>
<footer><div class="wrap">LifeTogether Ministries &middot; The Pastor's Library Project &middot;
Proposal for """ + P("[Church Name]") + """</div></footer></body></html>""")
    return h.getvalue()


if __name__ == "__main__":
    out = build()
    p = "/mnt/user-data/outputs/pastors-library-proposal.html"
    open(p, "w", encoding="utf-8").write(out)
    print("bytes:", len(out), "| div:", out.count("<div") - out.count("</div>"),
          "| sections:", out.count("<section"), out.count("</section>"),
          "| tables:", out.count("<table"), out.count("</table>"),
          "| placeholders:", out.count('class="ph"'))
