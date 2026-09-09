# -*- coding: utf-8 -*-
"""The Pastor's Library Project — offer, outcomes, reconciled pricing, staffing."""
import io

CSS = """
:root{--ink:#0c1723;--ink2:#08111c;--gold:#c19a4b;--goldlt:#e2c689;--parch:#f7f3ea;
--parch2:#efe8da;--rule:#d9cfbc;--body:#2b2a26;--muted:#6d6759;--mutedlt:#9fb0c1;}
*{box-sizing:border-box}
body{margin:0;background:var(--parch);color:var(--body);
font-family:"Cormorant Garamond",Georgia,serif;font-size:19px;line-height:1.62}
.wrap{max-width:940px;margin:0 auto;padding:0 30px}
h1,h2,h3,h4{font-family:"Playfair Display",Georgia,serif;margin:0;letter-spacing:-.01em}
.eyebrow{font-family:"Lato",sans-serif;font-weight:800;font-size:10px;letter-spacing:.26em;
text-transform:uppercase;color:var(--gold);display:block}
p{margin:0 0 15px}
header{background:var(--ink);color:#f3efe6;padding:68px 0 56px;position:relative;overflow:hidden}
header:before{content:"";position:absolute;inset:0;
background:radial-gradient(112% 78% at 7% 0%,rgba(193,154,75,.18),transparent 62%)}
header .wrap{position:relative}header .eyebrow{color:var(--goldlt)}
header h1{font-size:clamp(33px,5.8vw,58px);line-height:1.03;color:#fbf8f1;margin-top:16px}
header h1 em{font-style:italic;font-weight:400;color:var(--goldlt)}
header .lede{font-size:21px;color:#cfc7b8;max-width:640px;margin-top:22px}
section{padding:58px 0 50px;border-bottom:1px solid var(--rule)}
section.dark{background:var(--ink2);color:#e6e0d3;border-bottom:none}
section.dark h2,section.dark h3,section.dark h4{color:#fbf8f1}
section.dark p{color:#d6cec0}
section.tone{background:var(--parch2)}
h2.sec{font-size:clamp(26px,4.1vw,38px);line-height:1.1;margin-top:13px;max-width:790px}
.kick{font-style:italic;color:var(--muted);margin:13px 0 0;max-width:650px;font-size:20px}
section.dark .kick{color:var(--mutedlt)}
.verdict{font-family:"Playfair Display",serif;font-size:22px;line-height:1.42;
border-left:3px solid var(--gold);padding-left:22px;margin:24px 0;max-width:670px}
section.dark .verdict{color:var(--goldlt)}
.item{display:flex;gap:22px;padding:20px 0;border-top:1px solid var(--rule)}
section.dark .item{border-color:rgba(255,255,255,.13)}
.item .n{flex:0 0 44px;font-family:"Playfair Display",serif;font-size:28px;line-height:1;
color:transparent;-webkit-text-stroke:1px var(--gold);padding-top:3px}
section.dark .item .n{-webkit-text-stroke-color:var(--goldlt)}
.item .c{flex:1 1 auto;max-width:670px}
.item h4{font-size:20px;line-height:1.25;margin-bottom:7px}
.item p{margin:0 0 9px;font-size:18px}.item p:last-child{margin-bottom:0}
.out{display:flex;gap:18px;padding:14px 0;border-bottom:1px solid var(--rule);align-items:baseline}
.out .mark{flex:0 0 20px;color:var(--gold);font-family:"Lato",sans-serif;font-size:15px}
.out .txt{flex:1;font-size:18.5px}
section.dark .out{border-color:rgba(255,255,255,.13)}
.ws{border-top:1px solid var(--rule);padding:24px 0}
.ws h3{font-size:23px;margin-bottom:5px}
.ws .who{font-family:"Lato",sans-serif;font-size:11px;letter-spacing:.14em;text-transform:uppercase;
color:var(--gold);margin-bottom:10px}
.ws ul{margin:0;padding-left:20px}.ws li{margin-bottom:6px;font-size:18px}
table{width:100%;border-collapse:collapse;margin-top:24px;font-size:17px}
th{font-family:"Lato",sans-serif;font-weight:800;font-size:10px;letter-spacing:.15em;
text-transform:uppercase;color:var(--gold);text-align:left;padding:0 14px 11px 0;
border-bottom:1px solid var(--rule);vertical-align:bottom}
td{padding:14px 14px 14px 0;border-bottom:1px solid var(--rule);vertical-align:top}
td.k{font-family:"Playfair Display",serif;font-size:18px;width:24%}
td.n{font-family:"Lato",sans-serif;font-size:14.5px;white-space:nowrap;color:var(--gold);font-weight:700}
td.s{color:var(--muted);font-size:16.5px}
section.dark td{border-color:rgba(255,255,255,.13)}
section.dark td.k{color:#fbf8f1}section.dark td.s{color:var(--mutedlt)}
section.dark td.n{color:var(--goldlt)}
.note{font-family:"Lato",sans-serif;font-size:13px;line-height:1.75;color:var(--muted);
border-top:1px solid var(--rule);margin-top:30px;padding-top:15px;max-width:720px}
section.dark .note{color:var(--mutedlt);border-color:rgba(255,255,255,.15)}
.close{background:var(--ink);color:#efeae0;padding:66px 0;text-align:center}
.close h2{font-size:clamp(25px,4vw,38px);color:#fbf8f1}
.close p{max-width:610px;margin:18px auto 0;color:#c9c0b0}
footer{background:#070d15;color:#7d8b99;padding:24px 0;font-family:"Lato",sans-serif;
font-size:10.5px;letter-spacing:.1em;text-align:center;text-transform:uppercase}
@media(max-width:720px){body{font-size:18px}.wrap{padding:0 20px}section{padding:44px 0 38px}
.item{gap:13px}.item .n{flex:0 0 30px;font-size:22px}}
"""

OUTCOMES = [
"Eighteen months of preaching planned, written, and aligned across the pulpit, the groups, and the households &mdash; so the question of what comes next is answered before it is asked.",
"Every message he has ever preached digitized, indexed, and findable by topic, passage, occasion, and outcome in under five seconds.",
"One complete book manuscript in his own voice, under his own name, drawn from what he has already said rather than from what he still has to write.",
"Ten small group studies built from his preaching, so the groups in his church are finally studying him rather than somebody else.",
"Four launch-ready campaign kits including Easter and Christmas, each with sermon, devotional, group session, children's version, and print file.",
"A membership series and a vision-and-values series his staff can run without him in the room.",
"A financial health and generosity track his church has almost certainly never had, built on his convictions rather than a licensed program.",
"Twelve months of working access to someone who has done this across five hundred churches, on a scheduled cadence rather than when there is a crisis.",
"A searchable platform his whole staff uses, indexed against twenty domains of church practice rather than sitting in a folder.",
"And the one that matters most to a man over fifty-five: a successor could run this church's teaching calendar from the archive alone.",
]

WORKSTREAMS = [
("The Archive", "Weeks 1 to 8 &nbsp;&middot;&nbsp; Aggregate and Curate",
 ["Intake of everything &mdash; files, boxes, cassettes, hard drives, the sermon folder nobody has opened since 2009",
  "Digitization, transcription, and cleanup",
  "Indexing against topic, book, passage, occasion, formation outcome and campaign hinge",
  "The Coverage Report: what he has preached, what he has never preached, and where the holes are",
  "Rights and ownership review, so everyone knows what can travel"]),
("The Library", "Months 2 to 6 &nbsp;&middot;&nbsp; Customize",
 ["The top ten timeless small group studies, drawn from his own material",
  "The membership series and the vision-and-values campaign",
  "The top felt-need series, chosen from the Coverage Report rather than from a hunch",
  "Financial health and generosity, built on his convictions",
  "Easter and Christmas devotional series, reusable every year"]),
("The Publication", "Months 4 to 10 &nbsp;&middot;&nbsp; Publish",
 ["The book &mdash; manuscript, cover, interior, and the campaign that carries it",
  "The churchwide campaign built from the book, in the Purpose Driven shape",
  "Print editions of the journals and workbooks",
  "The audio and narrated editions of the core library"]),
("The Platform and the Partnership", "Months 1 to 12 &nbsp;&middot;&nbsp; The engine and the relationship",
 ["The working Pastor's Library site: search, sort, filter, and staff access",
  "The twenty-part church intelligence library benchmarked against best practice",
  "The eighteen-month preaching calendar with campaigns placed",
  "Three to four timely campaigns positioned against what the next eighteen months will actually require",
  "Monthly working sessions with the pastor and the team for twelve months"]),
]

ADDITIONS = [
("The Transition File", "highest",
 """The one nobody sells and every pastor over fifty-five thinks about at two in the morning. Not
 legacy as a marketing word &mdash; an actual handoff document. What this church believes and why,
 the forty decisions that shaped it, the stories a successor has to know before he tells them wrong,
 the things that are non-negotiable and the things that only look non-negotiable. If the archive is
 his life's work, this is the instruction manual for it. Lead with this in any conversation with a
 pastor past fifty."""),
("The Weddings and Funerals File", "highest",
 """He has done hundreds. They are the most reused and least organized material in the entire
 archive, they are needed on four days' notice with no time to prepare, and they are the moments the
 congregation remembers longest. Curated, indexed by situation, with his own words at the graveside
 of a child and at the wedding of a couple nobody thought would make it. The highest value per hour
 of anything in the library, and almost nobody thinks to ask for it."""),
("The Counseling and Crisis Playbook", "high",
 """The twenty-five conversations he has had two hundred times. What he actually says to the couple
 in the third year, the parent of the addict, the widow at eight weeks. This is the most transferable
 pastoral knowledge in the building and it exists nowhere but in his head. Capturing it is also the
 fastest way to make his staff competent."""),
("Rights, Ownership, and Estate", "high",
 """Who owns his sermons. What happens to them when he leaves, retires, or dies. Whether the church
 or the pastor holds the copyright, what the employment agreement actually says, and what he wants
 done with thirty years of work. Most pastors have never considered it, and raising it is what turns
 the engagement from a purchase into stewardship. It is also the conversation that makes a family
 want to fund it."""),
("Three Books, Not One", "high",
 """Most thirty-year archives contain three books, not one, and they are usually a teaching book, a
 story book, and a book he has been circling for a decade without knowing it. Naming all three in the
 Coverage Report and building one is a better offer than building the only one he had thought
 of."""),
("The Next Generation Translation", "high",
 """His big ideas rendered at three levels &mdash; adult, student, child &mdash; so a family talks
 about the same thing at dinner that the church talked about on Sunday. This is the deliverable
 pastors get most emotional about, because it is the one that reaches their own grandchildren."""),
("The Second Language Edition", "medium",
 """Spanish in most of the country, and whatever the church's actual second language is elsewhere.
 Rarely offered, disproportionately valued, and frequently the thing that unlocks a part of the
 congregation the church has been failing quietly for years."""),
("The Staff Onboarding Library", "medium",
 """New hires currently absorb the culture over eighteen months by watching. His archive is the
 culture, organized. Twelve pieces that a new staff member reads or watches in their first month, and
 the church stops relying on osmosis."""),
("The Board and Elder Formation Series", "medium",
 """Governance is where pastors get hurt. A series built from his own convictions, for his own board,
 addressing the questions that surface right before a conflict rather than during one."""),
("The Weekly Audio Edition", "medium",
 """The archive as an evergreen podcast feeding the congregation between Sundays. Under the narrated
 production model this is now inexpensive, and it converts a static library into a weekly touch that
 keeps the church inside his teaching all year."""),
]

SCENARIOS = [
("Concierge", "Brett plus one producer",
 "2 to 4 full engagements per year", "$300,000 to $500,000",
 "Roughly 55%",
 """No infrastructure, no hiring risk, and every engagement personally led. This is the scenario that
 proves the model and produces the first Coverage Report, the first finished library, and the case
 study everything else depends on. It is also capped: Brett is the product, and Brett does not
 scale."""),
("Studio", "Team of five",
 "12 to 15 engagements per year", "$1,200,000 to $1,800,000",
 "Roughly 45%",
 """An archive producer, an editorial lead, a campaign producer, a platform builder, and an engagement
 lead. Margin falls because delivery is labor, and it only works if the templates from the first four
 engagements genuinely cut the hours. The editorial lead is the hard hire and the whole scenario turns
 on finding one."""),
("Engine-assisted", "Team of eight plus the platform",
 "30 to 40 engagements per year", "$3,000,000 to $4,500,000",
 "Roughly 55%",
 """Margin recovers because the engine absorbs the hours that used to be bespoke: indexing, campaign
 assembly, study generation, narration, and the calendar all run against systems that already exist
 in your stack. This is the only scenario where the Pastor's Library stops being a consultancy and
 becomes a business."""),
]


def build():
    h = io.StringIO(); W = h.write
    W("""<!DOCTYPE html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>The Pastor's Library Project &mdash; The Offer</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,700;1,400&family=Cormorant+Garamond:ital,wght@0,400;0,600;1,400&family=Lato:wght@300;400;700;800&display=swap" rel="stylesheet">
<style>""" + CSS + "</style></head><body>")

    W("""<header><div class="wrap">
<span class="eyebrow">The Pastor's Library Project &nbsp;&middot;&nbsp; Offer and Economics</span>
<h1>They come for a sermon.<br><em>They leave with thirty years.</em></h1>
<p class="lede">What a pastor actually buys, the outcomes he can hold you to, ten things he may value
more than the eleven you listed, and one reconciled price ladder instead of the four now in
circulation.</p>
</div></header>""")

    W("""<section><div class="wrap"><div style="max-width:720px">
<span class="eyebrow">The Offer</span>
<h2 class="sec">He is not buying deliverables. He is buying the end of starting over.</h2>
<p style="margin-top:22px">The pitch that works is not a list of eleven things. It is a sentence he
has been carrying for years without saying out loud: everything he has preached is sitting in boxes
and folders that nobody will ever open again, and every Monday he starts from nothing anyway.</p>
<p>Ken Sparks handwrote every message he ever preached. Boxes of paper. That story is the offer,
because every pastor over fifty hears it and recognizes his own garage.</p>
<div class="verdict">The most under-stewarded resource in any congregation is the senior pastor's
own library. He has already done the work. Nobody has ever helped him keep it.</div>
<p>So the four moves stay exactly as you named them &mdash; aggregate, curate, customize, publish
&mdash; and the offer is stated as outcomes rather than as a scope of work, because a scope of work
invites a comparison and an outcome invites a decision.</p>
</div></div></section>""")

    W("""<section class="dark"><div class="wrap">
<span class="eyebrow">Specific Outcomes</span>
<h2 class="sec">What is true when we are finished</h2>
<p class="kick">Written so he can hold you to them. Nothing here is a feeling or a percentage
increase in giving that neither of you could ever verify.</p>
<div style="margin-top:26px;max-width:740px">""")
    for o in OUTCOMES:
        W('<div class="out"><span class="mark">&#9679;</span><span class="txt">%s</span></div>' % o)
    W("""</div>
<p class="note">Deliberately absent: any claim about attendance, giving, or engagement. Those depend
on a hundred things you do not control, a pastor knows it, and promising them is how a services
engagement ends in an argument at month nine.</p>
</div></section>""")

    W("""<section class="tone"><div class="wrap">
<span class="eyebrow">The Eleven, Organized</span>
<h2 class="sec">Four workstreams, not eleven deliverables</h2>
<p class="kick">The same list you named, sequenced so a pastor can see the year rather than the
menu.</p>""")
    for name, when, items in WORKSTREAMS:
        W('<div class="ws"><h3>%s</h3><div class="who">%s</div><ul>' % (name, when))
        for it in items:
            W('<li>%s</li>' % it)
        W('</ul></div>')
    W("""<p class="note">Sequencing note that matters commercially: the Coverage Report lands in week
eight and it is the moment the engagement sells itself upward. A pastor who sees, in print, that he
has preached money four times in thirty years and never once preached suffering will buy the next
tier without being asked.</p>
</div></section>""")

    W("""<section><div class="wrap">
<span class="eyebrow">What You Did Not List</span>
<h2 class="sec">Ten things a pastor may value more</h2>
<p class="kick">The first two are the strongest offers in this entire document and neither is on
anyone's price list anywhere.</p>""")
    for i, (name, weight, body) in enumerate(ADDITIONS, 1):
        W('<div class="item"><span class="n">%d</span><div class="c"><h4>%s</h4><p>%s</p></div></div>'
          % (i, name, " ".join(body.split())))
    W("""<div class="verdict">Lead the first conversation with the Transition File and the Weddings
and Funerals File. They are cheap to produce, impossible to buy anywhere else, and they land on the
two things a pastor over fifty-five is actually thinking about.</div>
</div></section>""")

    W("""<section class="dark"><div class="wrap">
<span class="eyebrow">Pricing</span>
<h2 class="sec">One ladder, three funding doors</h2>
<div class="verdict">You currently have four price architectures in circulation for the same
conversation. Adding a fifth is the failure mode. This reconciles them.</div>
<table style="color:#e6e0d3">
<tr><th>Rung</th><th>Price</th><th>What it is</th><th>Reconciles</th></tr>
<tr><td class="k">1 &middot; Discovery and Audit</td><td class="n">$8,500 &ndash; $15,000</td>
<td class="s">Intake, digitization sample, the Coverage Report, an architecture recommendation, and one message produced end to end so he can see it. Four to six weeks.</td>
<td class="s">Platform list $8,500 and the offer's Audit floor</td></tr>
<tr><td class="k">2 &middot; The Working Library</td><td class="n">$28,000 &ndash; $45,000</td>
<td class="s">Full archive indexed, the searchable platform live, the top ten studies, one campaign, and a twelve-month preaching calendar.</td>
<td class="s">Platform list $28,000 and the offer's Architecture tier</td></tr>
<tr><td class="k">3 &middot; The Full System</td><td class="n">$65,000 &ndash; $125,000</td>
<td class="s">Everything on your list of eleven, including the book and its campaign, Easter and Christmas, financial health and generosity, membership, vision and values, and the twelve-month partnership.</td>
<td class="s">Platform list $65,000+, the offer's Full System, and the donor prospectus at $100,000</td></tr>
<tr><td class="k">4 &middot; The Legacy Edition</td><td class="n">$175,000 &ndash; $250,000+</td>
<td class="s">Adds the Transition File, weddings and funerals, the counseling playbook, three books rather than one, the next generation translation, a second language, and the rights and estate work.</td>
<td class="s">The offer's $250,000 ceiling, now with something behind the number</td></tr>
</table>
<h3 style="font-size:23px;margin-top:40px">The three doors</h3>
<table style="color:#e6e0d3">
<tr><th>Who pays</th><th>Typical rung</th><th>Why it works</th></tr>
<tr><td class="k">The church budget</td><td class="n">Rung 1 or 2</td><td class="s">Sold as curriculum and communications spend, approved by an executive pastor, no board conversation required</td></tr>
<tr><td class="k">One family in the congregation</td><td class="n">Rung 3 at $100,000</td><td class="s">Funded as an honoring gift to a pastor they love. This is exactly where the donor prospectus belongs and it should stop being a separate document</td></tr>
<tr><td class="k">A foundation, in cohort</td><td class="n">Rung 3 or 4</td><td class="s">The First One Hundred. Ten at a time, named, with a published coverage standard</td></tr>
</table>
<p class="note">The naming should collapse too. Pastor's Library is the umbrella; Legacy Edition is
Rung 4. Legacy Library as a separate brand should be retired, because two names for one engagement is
how a prospect concludes there are two products and asks which one is cheaper.</p>
</div></section>""")

    W("""<section class="tone"><div class="wrap">
<span class="eyebrow">Staffing</span>
<h2 class="sec">Three scenarios you could actually run</h2>
<p class="kick">A full Rung 3 engagement is roughly seven to nine hundred hours of real work. Every
scenario below is built off that number.</p>
<table>
<tr><th>Scenario</th><th>Team</th><th>Capacity</th><th>Revenue</th><th>Gross margin</th></tr>""")
    for name, team, cap, rev, marg, body in SCENARIOS:
        W('<tr><td class="k">%s</td><td class="s">%s</td><td class="s">%s</td>'
          '<td class="n">%s</td><td class="s">%s</td></tr>' % (name, team, cap, rev, marg))
    W("</table>")
    for i, (name, team, cap, rev, marg, body) in enumerate(SCENARIOS, 1):
        W('<div class="item"><span class="n">%d</span><div class="c"><h4>%s</h4><p>%s</p></div></div>'
          % (i, name, " ".join(body.split())))
    W("""<h3 style="font-size:23px;margin-top:36px">Where the hours actually go</h3>
<table>
<tr><th>Workstream</th><th>Hours</th><th>Who</th></tr>
<tr><td class="k">Intake, digitization, transcription</td><td class="n">40 &ndash; 80</td><td class="s">Vendor plus an archive producer. Largely outsourceable</td></tr>
<tr><td class="k">Indexing and the Coverage Report</td><td class="n">30 &ndash; 50</td><td class="s">Archive producer against the engine. The most automatable line here</td></tr>
<tr><td class="k">The book manuscript</td><td class="n">120 &ndash; 180</td><td class="s">Editorial lead. The bottleneck and the hardest hire</td></tr>
<tr><td class="k">Ten small group studies</td><td class="n">120 &ndash; 160</td><td class="s">Editorial plus the curriculum engine</td></tr>
<tr><td class="k">Campaigns and devotional series</td><td class="n">140 &ndash; 200</td><td class="s">Campaign producer against the 17,000-campaign platform</td></tr>
<tr><td class="k">Platform build and calendar</td><td class="n">60 &ndash; 80</td><td class="s">Platform builder, mostly configuration once the template exists</td></tr>
<tr><td class="k">Twelve months of consulting</td><td class="n">48 &ndash; 60</td><td class="s">Engagement lead. Brett, until it can be handed off</td></tr>
<tr><td class="k">Project management</td><td class="n">80 &ndash; 100</td><td class="s">Underestimated by everyone, every time</td></tr>
</table>
<p class="note">Two honest constraints. First, this is a services business with services economics
&mdash; at Rung 3 you are around forty-five to fifty-five percent gross margin, not software margin,
and no amount of framing changes that until the engine absorbs the hours. Second, the editorial lead
is the single point of failure. Someone who can turn a thirty-year archive into a book in another
man's voice is rare, expensive, and the reason most agencies never get past four engagements a year.
Hire that person before selling the fifth.</p>
</div></section>""")

    W("""<div class="close"><div class="wrap">
<h2>Sell Rung 1 to everyone.<br>The Coverage Report sells the rest.</h2>
<p>One ladder, three doors, and the Transition File leading every first conversation with a pastor
past fifty-five.</p>
</div></div>
<footer><div class="wrap">LifeTogether Ministries &middot; The Pastor's Library Project &middot;
Offer, outcomes, pricing and staffing &middot; August 2026</div></footer></body></html>""")
    return h.getvalue()


if __name__ == "__main__":
    out = build()
    p = "/mnt/user-data/outputs/pastors-library-offer-and-economics.html"
    open(p, "w", encoding="utf-8").write(out)
    print("bytes:", len(out), "| div:", out.count("<div") - out.count("</div>"),
          "| sections:", out.count("<section"), out.count("</section>"),
          "| tables:", out.count("<table"), out.count("</table>"))
