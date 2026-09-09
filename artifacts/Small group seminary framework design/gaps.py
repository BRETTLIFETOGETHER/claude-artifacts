# -*- coding: utf-8 -*-
"""Gaps, models, and the third-party validation answer."""
import io

CSS = """
:root{--ink:#0c1723;--ink2:#08111c;--gold:#c19a4b;--goldlt:#e2c689;--parch:#f7f3ea;
--parch2:#efe8da;--rule:#d9cfbc;--body:#2b2a26;--muted:#6d6759;--mutedlt:#9fb0c1;}
*{box-sizing:border-box}
body{margin:0;background:var(--parch);color:var(--body);
font-family:"Cormorant Garamond",Georgia,serif;font-size:19px;line-height:1.62}
.wrap{max-width:920px;margin:0 auto;padding:0 30px}
h1,h2,h3,h4{font-family:"Playfair Display",Georgia,serif;margin:0;letter-spacing:-.01em}
.eyebrow{font-family:"Lato",sans-serif;font-weight:800;font-size:10px;letter-spacing:.26em;
text-transform:uppercase;color:var(--gold);display:block}
p{margin:0 0 15px}
header{background:var(--ink);color:#f3efe6;padding:66px 0 54px;position:relative;overflow:hidden}
header:before{content:"";position:absolute;inset:0;
background:radial-gradient(112% 78% at 7% 0%,rgba(193,154,75,.18),transparent 62%)}
header .wrap{position:relative}header .eyebrow{color:var(--goldlt)}
header h1{font-size:clamp(33px,5.8vw,56px);line-height:1.03;color:#fbf8f1;margin-top:16px}
header h1 em{font-style:italic;font-weight:400;color:var(--goldlt)}
header .lede{font-size:21px;color:#cfc7b8;max-width:620px;margin-top:22px}
section{padding:58px 0 50px;border-bottom:1px solid var(--rule)}
section.dark{background:var(--ink2);color:#e6e0d3;border-bottom:none}
section.dark h2,section.dark h3,section.dark h4{color:#fbf8f1}
section.dark p{color:#d6cec0}
section.tone{background:var(--parch2)}
h2.sec{font-size:clamp(26px,4.1vw,38px);line-height:1.1;margin-top:13px;max-width:780px}
.kick{font-style:italic;color:var(--muted);margin:13px 0 0;max-width:640px;font-size:20px}
section.dark .kick{color:var(--mutedlt)}
.verdict{font-family:"Playfair Display",serif;font-size:22px;line-height:1.42;
border-left:3px solid var(--gold);padding-left:22px;margin:24px 0;max-width:660px}
section.dark .verdict{color:var(--goldlt)}
.item{display:flex;gap:22px;padding:20px 0;border-top:1px solid var(--rule)}
section.dark .item{border-color:rgba(255,255,255,.13)}
.item .n{flex:0 0 44px;font-family:"Playfair Display",serif;font-size:28px;line-height:1;
color:transparent;-webkit-text-stroke:1px var(--gold);padding-top:3px}
section.dark .item .n{-webkit-text-stroke-color:var(--goldlt)}
.item .c{flex:1 1 auto;max-width:670px}
.item h4{font-size:20px;line-height:1.25;margin-bottom:7px}
.item p{margin:0 0 9px;font-size:18px}.item p:last-child{margin-bottom:0}
.sev{font-family:"Lato",sans-serif;font-size:9px;font-weight:800;letter-spacing:.15em;
text-transform:uppercase;padding:3px 8px;margin-left:8px;white-space:nowrap;vertical-align:middle}
.sev.new{background:var(--gold);color:#fff}
.sev.add{border:1px solid var(--gold);color:var(--gold)}
.sev.cant{border:1px solid var(--rule);color:var(--muted)}
table{width:100%;border-collapse:collapse;margin-top:24px;font-size:17px}
th{font-family:"Lato",sans-serif;font-weight:800;font-size:10px;letter-spacing:.15em;
text-transform:uppercase;color:var(--gold);text-align:left;padding:0 14px 11px 0;
border-bottom:1px solid var(--rule);vertical-align:bottom}
td{padding:13px 14px 13px 0;border-bottom:1px solid var(--rule);vertical-align:top}
td.k{font-family:"Playfair Display",serif;font-size:17.5px;width:27%}
td.s{color:var(--muted);font-size:16.5px}
section.dark td{border-color:rgba(255,255,255,.13)}
section.dark td.k{color:#fbf8f1}section.dark td.s{color:var(--mutedlt)}
.note{font-family:"Lato",sans-serif;font-size:13px;line-height:1.75;color:var(--muted);
border-top:1px solid var(--rule);margin-top:30px;padding-top:15px;max-width:710px}
section.dark .note{color:var(--mutedlt);border-color:rgba(255,255,255,.15)}
.close{background:var(--ink);color:#efeae0;padding:66px 0;text-align:center}
.close h2{font-size:clamp(25px,4vw,38px);color:#fbf8f1}
.close p{max-width:600px;margin:18px auto 0;color:#c9c0b0}
footer{background:#070d15;color:#7d8b99;padding:24px 0;font-family:"Lato",sans-serif;
font-size:10.5px;letter-spacing:.1em;text-align:center;text-transform:uppercase}
@media(max-width:720px){body{font-size:18px}.wrap{padding:0 20px}section{padding:44px 0 38px}
.item{gap:13px}.item .n{flex:0 0 30px;font-size:22px}}
"""

GAPS = [
("Theological research and writing", "new",
 """Nearly every top-ten core opens with a research and writing course, and the catalog has nothing
 like it. Theological Method sits at ST 305 and teaches how a doctrine is built, not how to use a
 library, evaluate a commentary, tell a good source from a confident one, or write a paper somebody
 will grade. It is the prerequisite for the entire Fellow track and it is absent. Add it early in
 Hermeneutics, not late."""),
("Next Generation ministry", "new",
 """The largest structural hole. Twenty disciplines and not one course on children's or student
 ministry, while next-gen is the hardest staffing need in most congregations and a standard
 concentration in every seminary on the list. The Family discipline covers parenting, which is a
 different subject from ministering to somebody else's fourteen-year-old. This should be discipline
 twenty-one, twenty courses, and it will sell faster than several of the twenty you have."""),
("Church administration, law, and safeguarding", "new",
 """Polity and bylaws, employment law, clergy tax, liability and insurance, background checks,
 mandatory reporting, and a written child protection policy. Seminaries have been adding this for a
 decade because the consequences of not knowing it have become severe. For a program training
 volunteers rather than clergy, this is not merely a curriculum gap, it is the largest liability
 exposure in the whole model. Discipline twenty-two."""),
("Field education as an architecture", "add",
 """You have practicum courses. Accredited programs have field education, which is a different
 animal: a defined placement, logged hours, a supervisor with standing, a mid-term and final
 evaluation on a rubric, and a learning covenant signed before it starts. The four practicum courses
 in the catalog imply this without providing it. Build the architecture once and every practicum
 course inherits it."""),
("The integrative capstone", "add",
 """Master's programs end with synthesis, and the credential ladder promises a capstone at Rung Four
 that no course teaches anybody how to do. Add one course on the integrative project itself: framing
 a question, gathering evidence across disciplines, and defending a conclusion in front of
 people."""),
("Chaplaincy and institutional ministry", "add",
 """Hospital, hospice, military, prison, first responder, and workplace chaplaincy. A growing track
 in accredited programs and an enormous lay-adjacent field, and the catalog does not mention it. Two
 or three courses inside Pastoral Care, with the honest note that formal chaplaincy endorsement runs
 through denominations and certifying bodies you are not part of."""),
("Denominational polity and ordination preparation", "add",
 """Required for ordination nearly everywhere and structurally impossible to teach generically, which
 is exactly why it belongs in the denominational editions rather than the master catalog. Specify it
 as a required module every edition must supply, so the gap is filled by the partner rather than left
 open."""),
("Rural, small-church, and revitalization ministry", "add",
 """Your stated buyer is the bivocational pastor and the church under two hundred and fifty. The
 catalog is written for a church with departments. Nothing addresses the pastor who is the entire
 staff, the congregation of sixty that has declined for fifteen years, or the revitalization
 question that dominates that conversation. This is a positioning gap more than a content one."""),
("Ministry with people with disabilities", "add",
 """Now standard in accredited programs and represented in the catalog only by one faculty prospect's
 specialty. One course in Pastoral Care, one in Next Generation, and an accessibility pass across the
 delivery editions themselves."""),
("Greek and Hebrew exegesis of specific books", "cant",
 """Worth stating precisely rather than under the general heading of languages. The core requirement
 at the schools you are benchmarking against is not language survey, it is four to six courses of
 exegesis in the original text. That is the actual gap, it is intentional, and naming it at that
 level of specificity is more credible than conceding languages in the abstract."""),
("Clinical Pastoral Education", "cant",
 """A unit of CPE requires a certified supervisor and a clinical placement, and the certification runs
 through a body you cannot join. It cannot be replicated, approximated, or renamed. Put it on the
 published list of what this program does not deliver, alongside the languages, and point to where a
 student can go get it."""),
]

MISSING = [
("There is no diagnostic, and the diagnostic is your proven front door",
 """Every other platform you have built opens with an assessment, and the price list treats the
 twenty-two diagnostics as the funnel that is never gated. This has none. A ten-question instrument
 that tells a member which discipline to start in, and tells a pastor how much theological capacity
 his congregation actually has, is the cheapest thing on this list and probably the highest
 yielding."""),
("Nothing yet speaks to the student",
 """Every document produced so far addresses pastors, deans, denominations, faculty, and donors. Not
 one addresses the forty-six-year-old small group leader who would actually take the course. She is
 the person the whole thing exists for and she has not been written to once."""),
("There is no date",
 """This is architecture without a calendar. Name the first cohort start, the church, and the six
 courses, and the entire project stops being a concept. Everything else on this page can wait behind
 that."""),
("Spanish",
 """The campaign platform already ships in three languages. The fastest-growing segment of the
 American church is Hispanic, the training gap there is the widest in the country, and a
 church-based, language-light, cohort-delivered model is close to the ideal instrument for it. It is
 also the single strongest donor story in the whole plan and it is currently absent."""),
("Prison, recovery, and reentry as delivery contexts",
 """A credential that requires no campus, no prerequisite, and no tuition is close to purpose-built
 for correctional and recovery settings, where demand for exactly this is enormous and chronically
 unmet. It is also the context where the certificate means the most to the person holding it."""),
("Women, and a decision rather than a default",
 """Women carry a large share of the lay teaching load in most congregations and are roughly a
 quarter of the faculty prospect list. The denominational editions make the ordination question
 navigable, but who teaches, who is recruited, and how the courses on gender are written all need a
 stated position rather than an accumulation of defaults."""),
]

MODELS = [
("Alpha", "Distribution without a credential",
 """The closest analogue for reach. Free or nearly free, run by local volunteers, translated
 everywhere, tens of millions of participants, and no credential at all. The lesson worth taking is
 that the local host is the non-negotiable and the certificate is not; Alpha scaled on trained hosts
 and a fixed format, not on academic weight."""),
("Financial Peace University", "The commercial proof",
 """Licensed video curriculum, a trained local coordinator, a fee, and a church that runs it on a
 calendar. It is the clearest existing proof that a congregation will pay real money for a course
 with a name and a completion moment, and it is structurally almost identical to what you are
 proposing minus the transcript."""),
("Theological Education by Extension", "The movement you are rejoining",
 """TEE has existed for decades: training church leaders in their own context rather than removing
 them to a campus, with regional associations worldwide and affiliate status in some accrediting
 bodies specifically for lay training institutes and extension centers. You are not inventing a
 category. Adopting the vocabulary connects you to precedent, literature, and a network, and it makes
 the idea legible to any international partner immediately."""),
("Third Millennium Ministries", "Donor-funded, given away, multilingual",
 """Seminary-level curriculum produced with credentialed faculty, funded by donors, distributed free
 and translated widely. It is the donor-funded model already proven inside this exact category, which
 is useful evidence when you take the discipline-endowment idea to a funder."""),
("Logos and Faithlife Mobile Ed", "Competitor and channel at once",
 """They already sell seminary-level video courses from named faculty, and Dallas hands every
 incoming student a Logos package. That makes them a direct competitor for the content layer and the
 single most efficient distribution partner for it. Worth a conversation before they are worth a
 comparison chart."""),
("Evangelical Training Association", "The institution closest to what you are building",
 """ETA has been credentialing church teachers and ministry leaders since the 1930s and is listed by
 the Association for Biblical Higher Education among its peer associations. It occupies almost
 exactly your category at a fraction of your ambition. Partner, license, or acquire &mdash; but do
 not build past it without having looked at it."""),
("Church residency networks", "Be the curriculum, not the competitor",
 """Large churches increasingly run their own pastoral residencies with no curriculum behind them
 beyond whatever the executive pastor assembles. Supplying the course of study inside existing
 residencies is faster than recruiting churches to start one."""),
]


def build():
    h = io.StringIO(); W = h.write
    W("""<!DOCTYPE html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Gaps, Models, and Validation</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,700;1,400&family=Cormorant+Garamond:ital,wght@0,400;0,600;1,400&family=Lato:wght@300;400;700;800&display=swap" rel="stylesheet">
<style>""" + CSS + "</style></head><body>")

    W("""<header><div class="wrap">
<span class="eyebrow">Doing Seminary Together &nbsp;&middot;&nbsp; Gap Analysis</span>
<h1>What the syllabus<br><em>is still missing</em></h1>
<p class="lede">Eleven gaps measured against a top-ten evangelical core, six things missing that are
not curriculum at all, seven models worth borrowing, and the third-party validation route that
actually exists.</p>
</div></header>""")

    W("""<section><div class="wrap">
<span class="eyebrow">Coverage</span>
<h2 class="sec">Eleven gaps against a top-ten core</h2>
<p class="kick">Three should become new disciplines or courses immediately. Six are additions inside
existing disciplines. Two you cannot deliver and should publish as such.</p>""")
    for i, (name, sev, body) in enumerate(GAPS, 1):
        label = {"new": "Build it", "add": "Add inside", "cannot": "Cannot deliver",
                 "cant": "Cannot deliver"}[sev]
        cls = "new" if sev == "new" else ("add" if sev == "add" else "cant")
        W('<div class="item"><span class="n">%d</span><div class="c">'
          '<h4>%s<span class="sev %s">%s</span></h4><p>%s</p></div></div>'
          % (i, name, cls, label, " ".join(body.split())))
    W("""<div class="verdict">Two new disciplines takes the catalog from twenty by twenty to
twenty-two by twenty, four hundred and forty courses &mdash; and both new ones will sell faster than
several of the twenty already there.</div>
<p class="note">One methodological caution. This is measured against MDiv and MA cores as I know
them, not against pulled syllabi. Before any of it goes into a partnership conversation, run the
actual coverage matrix: extract the required core from ten schools, map every required course to one
of your disciplines, and treat anything with no home as a confirmed gap rather than a suspected
one.</p>
</div></section>""")

    W("""<section class="dark"><div class="wrap">
<span class="eyebrow">Beyond the Catalog</span>
<h2 class="sec">Six things missing that are not courses</h2>""")
    for i, (name, body) in enumerate(MISSING, 1):
        W('<div class="item"><span class="n">%d</span><div class="c"><h4>%s</h4><p>%s</p></div></div>'
          % (i, name, " ".join(body.split())))
    W("""<div class="verdict">The third one is the only one that matters this month. Everything else
on this page waits behind a first cohort with a date on it.</div>
</div></section>""")

    W("""<section class="tone"><div class="wrap">
<span class="eyebrow">Models</span>
<h2 class="sec">Seven models worth borrowing from</h2>""")
    for i, (name, tag, body) in enumerate(MODELS, 1):
        W('<div class="item"><span class="n">%d</span><div class="c"><h4>%s</h4>'
          '<p style="font-style:italic;color:var(--muted);margin-bottom:8px">%s</p><p>%s</p>'
          '</div></div>' % (i, name, tag, " ".join(body.split())))
    W("</div></section>")

    W("""<section><div class="wrap">
<span class="eyebrow">The Validation Question</span>
<h2 class="sec">A loose accrediting body does exist, and it is not the one you would guess</h2>
<div class="verdict">Not ABHE, which is closed to you. Credit recommendation through ACE or NCCRS
&mdash; independent faculty review that produces a defensible sentence without requiring you to
become an institution.</div>
<div style="max-width:700px;margin-top:22px">
<p>The obvious candidate turns out to be a dead end. Membership in the Association for Biblical
Higher Education is limited to institutions already accredited by ABHE's own commission or another
federally or CHEA-recognised accreditor, with dues in the thousands. There is no door there for a
publisher with a curriculum, only for a school. Same for the theological school associations. That
route reopens only if you acquire an accredited school, which reverses the economics that made this
worth doing.</p>
<p>The route that does exist is credit recommendation, and it is close to exactly what you described.
The American Council on Education runs Learning Evaluations, in which faculty teams drawn from
accredited colleges assess training produced outside the academy and publish a credit
recommendation. The National College Credit Recommendation Service does the same and reports more
than thirteen hundred cooperating institutions that will consider granting credit on the strength of
it. The best-known recent example is the Google career certificates, which carry ACE recommendations
of up to twelve credits.</p>
<h4 style="font-size:20px;margin:26px 0 10px">Why this fits your posture precisely</h4>
<p>NCCRS states plainly that it is not an accrediting body and that a recommended course must never
be described as credit-bearing. The permitted phrase is recommended for college credit, and the
receiving institution always decides. That is the same discipline you have already adopted
voluntarily about the word seminary, and adopting an external body that enforces it for you is worth
more than any claim you could make about yourself.</p>
<table>
<tr><th>Route</th><th>Open to you</th><th>What it produces</th></tr>
<tr><td class="k">ACE Learning Evaluations</td><td class="s">Yes</td><td class="s">Faculty-led review, a published entry in the ACE national guide, and a credit recommendation the receiving school weighs</td></tr>
<tr><td class="k">NCCRS</td><td class="s">Yes</td><td class="s">The same, with a stated network of 1,300-plus cooperating institutions and explicit language rules</td></tr>
<tr><td class="k">ABHE membership</td><td class="s">No</td><td class="s">Requires existing recognised accreditation. A door only after acquisition</td></tr>
<tr><td class="k">ICETE and regional associations</td><td class="s">Partly</td><td class="s">The global route. Some regional bodies carry affiliate tiers explicitly for lay training institutes and extension centres</td></tr>
<tr><td class="k">Unrecognised accreditors</td><td class="s">Avoid</td><td class="s">Seals are purchasable and the purchase is discoverable. One of these would end the project</td></tr>
</table>
<h4 style="font-size:20px;margin:28px 0 10px">Two honest limits</h4>
<p>Credit recommendations in this system skew undergraduate. That fits the positioning you have
already chosen, which is Bible-college tier rather than seminary tier, but it means the outcome is
credit toward a bachelor's rather than advanced standing in a Master of Divinity. Do not let anyone
in the room believe otherwise.</p>
<p>And these bodies require official records from the provider, not a badge or a completion screen.
Which returns you to the same conclusion as every other thread this month: the transcript is not a
nice-to-have feature, it is the load-bearing element that the credential, the denominational sale,
the seminary pipeline and now the credit recommendation all sit on top of.</p>
<p class="note">Recommendation: submit the six-course Year One Certificate for review by one of the
two, as soon as those six courses exist. It is the cheapest independent validation available in the
entire landscape, it produces a sentence no competitor in church media can say, and it costs a
review fee rather than an institution.</p>
</div></div></section>""")

    W("""<div class="close"><div class="wrap">
<h2>Two new disciplines, one date,<br>and a credit recommendation.</h2>
<p>Next Generation and Church Administration go in the catalog. A first cohort goes on a calendar.
And the six courses go to ACE or NCCRS the week they are finished.</p>
</div></div>
<footer><div class="wrap">LifeTogether Ministries &middot; Doing Seminary Together &middot; Gap
analysis and validation routes &middot; August 2026</div></footer></body></html>""")
    return h.getvalue()


if __name__ == "__main__":
    out = build()
    p = "/mnt/user-data/outputs/doing-seminary-together-gaps-and-validation.html"
    open(p, "w", encoding="utf-8").write(out)
    print("bytes:", len(out), "| div:", out.count("<div") - out.count("</div>"),
          "| sections:", out.count("<section"), out.count("</section>"))
