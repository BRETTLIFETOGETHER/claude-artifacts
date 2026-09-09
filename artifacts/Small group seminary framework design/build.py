# -*- coding: utf-8 -*-
"""Render the SmallGroupSeminary.com framework + catalog document."""

import io
from courses import DISCIPLINES, COURSES, BLURBS, TIERS, codes_for, validate

TOTAL = validate()

ROMAN = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X",
         "XI", "XII", "XIII", "XIV", "XV", "XVI", "XVII", "XVIII", "XIX", "XX"]

CSS = """
:root{
  --ink:#0c1723; --ink-2:#0a1420; --navy:#132639; --gold:#c19a4b;
  --gold-lt:#e2c689; --parch:#f7f3ea; --parch-2:#efe8da;
  --rule:#d9cfbc; --body:#2b2a26; --muted:#6d6759; --muted-lt:#9fb0c1;
}
*{box-sizing:border-box}
html{-webkit-text-size-adjust:100%}
body{margin:0;background:var(--parch);color:var(--body);
  font-family:"Cormorant Garamond",Georgia,serif;font-size:19px;line-height:1.62;}
.wrap{max-width:1000px;margin:0 auto;padding:0 30px}
.narrow{max-width:760px;margin:0 auto}
h1,h2,h3,h4{font-family:"Playfair Display",Georgia,serif;font-weight:700;
  letter-spacing:-.01em;margin:0}
.eyebrow{font-family:"Lato",Helvetica,sans-serif;font-weight:800;font-size:10.5px;
  letter-spacing:.26em;text-transform:uppercase;color:var(--gold);display:block}
.util{font-family:"Lato",Helvetica,sans-serif}

/* ---------- cover ---------- */
header.cover{background:var(--ink);color:#f3efe6;padding:88px 0 74px;position:relative;overflow:hidden}
header.cover:before{content:"";position:absolute;inset:0;
  background:radial-gradient(115% 78% at 8% 0%,rgba(193,154,75,.19),transparent 62%);}
.cover .wrap{position:relative}
.cover .eyebrow{color:var(--gold-lt)}
.cover h1{font-size:clamp(46px,8.2vw,92px);line-height:.95;margin:20px 0 0;color:#fbf8f1}
.cover h1 em{font-style:italic;color:var(--gold-lt);font-weight:400}
.dotcom{font-family:"Lato",Helvetica,sans-serif;font-weight:300;font-size:13px;
  letter-spacing:.36em;text-transform:uppercase;color:#8ea1b4;margin-top:26px}
.lede{font-size:23px;line-height:1.5;color:#d9d2c4;max-width:640px;margin:26px 0 0}
.lede b{color:var(--gold-lt);font-weight:600}
.cover-rule{height:1px;background:linear-gradient(90deg,var(--gold),rgba(193,154,75,0));margin:38px 0 30px;max-width:520px}
.figs{display:flex;flex-wrap:wrap;gap:0;margin-top:8px;border-top:1px solid rgba(193,154,75,.3)}
.fig{padding:20px 30px 4px 0;margin-right:30px;border-right:1px solid rgba(255,255,255,.09)}
.fig:last-child{border-right:none}
.fig .n{font-family:"Playfair Display",serif;font-size:38px;color:var(--gold-lt);line-height:1}
.fig .l{font-family:"Lato",sans-serif;font-size:9.5px;letter-spacing:.2em;
  text-transform:uppercase;color:#8ea1b4;margin-top:7px}

/* ---------- sections ---------- */
section{padding:74px 0 66px;border-bottom:1px solid var(--rule)}
section.dark{background:var(--ink-2);color:#e6e0d3;border-bottom:none}
section.dark h2,section.dark h3{color:#fbf8f1}
section.dark .kicker{color:var(--muted-lt)}
section.tone{background:var(--parch-2)}
h2.sec{font-size:clamp(31px,4.6vw,44px);line-height:1.06;margin:16px 0 0}
.kicker{font-size:20px;color:var(--muted);margin:14px 0 0;max-width:660px;font-style:italic}
.sec-body{margin-top:26px}
.sec-body p{margin:0 0 17px}
p.first:first-letter{font-family:"Playfair Display",serif;font-size:52px;float:left;
  line-height:.82;padding:6px 11px 0 0;color:var(--gold)}

/* verdict */
.verdict{border-left:3px solid var(--gold);padding:4px 0 4px 26px;margin:30px 0 0}
.verdict p{font-family:"Playfair Display",serif;font-size:25px;line-height:1.38;margin:0}
.yes{color:var(--gold)}

/* generic list rows */
.rows{margin-top:34px;border-top:1px solid var(--rule)}
.row{display:flex;gap:26px;padding:22px 0;border-bottom:1px solid var(--rule)}
.row .lbl{flex:0 0 132px;font-family:"Lato",sans-serif;font-weight:800;font-size:10.5px;
  letter-spacing:.16em;text-transform:uppercase;color:var(--gold);padding-top:6px}
.row .txt{flex:1}
.row h4{font-size:21px;margin:0 0 6px}
.row p{margin:0;color:var(--muted);font-size:18px}
section.dark .row,section.dark .rows{border-color:rgba(255,255,255,.12)}
section.dark .row p{color:var(--muted-lt)}

/* two column */
.two{display:grid;grid-template-columns:1fr 1fr;gap:44px;margin-top:34px}
.col h4{font-size:20px;margin:0 0 10px}
.col p{margin:0 0 14px;font-size:18px}

/* ladder */
.ladder{margin-top:40px}
.rung{display:grid;grid-template-columns:66px 1fr 132px;gap:22px;align-items:baseline;
  padding:20px 0;border-bottom:1px solid rgba(255,255,255,.12)}
.rung:first-child{border-top:1px solid rgba(255,255,255,.12)}
.rung .step{font-family:"Playfair Display",serif;font-size:15px;color:var(--gold);
  letter-spacing:.08em}
.rung h4{font-size:23px;margin:0 0 5px}
.rung p{margin:0;font-size:17.5px;color:var(--muted-lt)}
.rung .load{font-family:"Lato",sans-serif;font-size:10.5px;letter-spacing:.13em;
  text-transform:uppercase;color:var(--gold-lt);text-align:right;line-height:1.7}
@media(max-width:720px){.rung{grid-template-columns:50px 1fr;}
  .rung .load{grid-column:2;text-align:left;margin-top:8px}}

/* table */
.tbl{width:100%;border-collapse:collapse;margin-top:34px;font-size:17px}
.tbl th{font-family:"Lato",sans-serif;font-weight:800;font-size:10px;letter-spacing:.16em;
  text-transform:uppercase;color:var(--gold);text-align:left;padding:0 16px 12px 0;
  border-bottom:1px solid var(--rule);vertical-align:bottom}
.tbl td{padding:16px 16px 16px 0;border-bottom:1px solid var(--rule);vertical-align:top;color:var(--body)}
.tbl td.pathname{font-family:"Playfair Display",serif;font-size:18px;width:22%}
.tbl td.small{color:var(--muted);font-size:16px}
.mark{font-family:"Lato",sans-serif;font-size:10px;letter-spacing:.12em;text-transform:uppercase;
  padding:3px 8px;border:1px solid var(--gold);color:var(--gold);white-space:nowrap}

/* steps */
.steps{counter-reset:s;margin-top:34px;padding:0;list-style:none}
.steps li{counter-increment:s;position:relative;padding:0 0 22px 62px;margin:0}
.steps li:before{content:counter(s,decimal-leading-zero);position:absolute;left:0;top:2px;
  font-family:"Lato",sans-serif;font-weight:800;font-size:12px;letter-spacing:.1em;
  color:var(--gold);border-bottom:1px solid var(--rule);padding-bottom:3px;width:34px}
.steps li b{font-family:"Playfair Display",serif;font-weight:700;display:block;font-size:19px;margin-bottom:4px}
.steps li span{color:var(--muted)}

/* catalog */
.cat-head{background:var(--ink);color:#f3efe6;padding:66px 0 58px;text-align:center}
.cat-head h2{font-size:clamp(31px,5vw,46px);color:#fbf8f1;margin-top:16px}
.cat-head p{color:#c9c0b0;font-size:20px;max-width:600px;margin:16px auto 0;font-style:italic}
.legend{display:flex;justify-content:center;gap:26px;flex-wrap:wrap;margin-top:32px}
.legend span{font-family:"Lato",sans-serif;font-size:9.5px;letter-spacing:.18em;
  text-transform:uppercase;color:#8ea1b4}
.legend i{color:var(--gold-lt);font-style:normal}

.disc{padding:56px 0 6px;border-bottom:1px solid var(--rule)}
.disc-top{display:flex;align-items:baseline;gap:18px;flex-wrap:wrap}
.disc-num{font-family:"Playfair Display",serif;font-size:15px;color:var(--gold);
  letter-spacing:.14em;flex:0 0 auto}
.disc h3{font-size:clamp(25px,3.6vw,33px);line-height:1.1}
.badge-new{font-family:"Lato",sans-serif;font-size:9px;font-weight:800;letter-spacing:.18em;
  text-transform:uppercase;background:var(--gold);color:#fff;padding:4px 9px;white-space:nowrap}
.disc-blurb{color:var(--muted);font-style:italic;margin:12px 0 0;max-width:700px;font-size:18px}
.tier{font-family:"Lato",sans-serif;font-size:9.5px;font-weight:800;letter-spacing:.22em;
  text-transform:uppercase;color:var(--gold);margin:34px 0 0;padding-bottom:8px;
  border-bottom:1px solid var(--gold)}
ol.courses{list-style:none;margin:0;padding:0}
ol.courses li{display:grid;grid-template-columns:88px 1fr;gap:20px;padding:13px 0;
  border-bottom:1px solid var(--rule)}
ol.courses .code{font-family:"Lato",sans-serif;font-size:11px;font-weight:700;
  letter-spacing:.1em;color:var(--gold);padding-top:5px}
ol.courses .t{font-family:"Playfair Display",serif;font-size:18.5px;line-height:1.28;color:#1c2b3a}
ol.courses .s{display:block;font-family:"Cormorant Garamond",serif;font-style:italic;
  font-size:17.5px;color:var(--muted);margin-top:2px;letter-spacing:0}
@media(max-width:620px){ol.courses li{grid-template-columns:1fr;gap:2px}
  ol.courses .code{padding-top:0}}

/* close */
.close{background:var(--ink);color:#efeae0;padding:80px 0;text-align:center}
.close h2{font-size:clamp(30px,5vw,44px);color:#fbf8f1}
.close p{max-width:620px;margin:20px auto 0;color:#c9c0b0;font-size:19px}
.close .cta{display:inline-block;margin-top:34px;font-family:"Lato",sans-serif;font-weight:800;
  font-size:11px;letter-spacing:.22em;text-transform:uppercase;color:var(--ink);
  background:var(--gold);padding:17px 40px;text-decoration:none}
footer{background:#070d15;color:#7d8b99;padding:30px 0;font-family:"Lato",sans-serif;font-size:11px;
  letter-spacing:.1em;text-align:center;text-transform:uppercase}
.note{font-family:"Lato",sans-serif;font-size:13px;line-height:1.7;color:var(--muted);
  border-top:1px solid var(--rule);margin-top:40px;padding-top:18px}
@media(max-width:720px){
  body{font-size:18px}.wrap{padding:0 20px}.two{grid-template-columns:1fr;gap:26px}
  section{padding:54px 0 48px}.row{flex-direction:column;gap:8px}.row .lbl{flex:none}
  .fig{padding-right:22px;margin-right:22px}
}
@media print{header.cover,section.dark,.cat-head,.close{-webkit-print-color-adjust:exact;print-color-adjust:exact}}
@media(prefers-reduced-motion:reduce){*{animation:none!important;transition:none!important}}
"""


def catalog_html():
    out = io.StringIO()
    for idx, (prefix, name, status) in enumerate(DISCIPLINES):
        codes = codes_for(prefix)
        out.write('<div class="disc"><div class="wrap">')
        out.write('<div class="disc-top"><span class="disc-num">%s</span><h3>%s</h3>'
                  % (ROMAN[idx], name))
        if status == "new":
            out.write('<span class="badge-new">New Discipline</span>')
        out.write('</div>')
        out.write('<p class="disc-blurb">%s</p>' % BLURBS[prefix])
        current = None
        for i, (title, sub) in enumerate(COURSES[prefix]):
            if TIERS[i] != current:
                if current is not None:
                    out.write('</ol>')
                current = TIERS[i]
                label = {"Foundation": "Foundation &nbsp;&middot;&nbsp; entry level",
                         "Core": "Core &nbsp;&middot;&nbsp; the working middle",
                         "Advanced": "Advanced &nbsp;&middot;&nbsp; depth and practicum"}[current]
                out.write('<p class="tier">%s</p><ol class="courses">' % label)
            out.write('<li><span class="code">%s</span><span class="t">%s'
                      '<span class="s">%s</span></span></li>' % (codes[i], title, sub))
        out.write('</ol></div></div>')
    return out.getvalue()


ACCRED_ROWS = [
    ("Church-endorsed certificate",
     "None. You award your own certificate.",
     "Weeks. No approvals needed as long as you never use degree language.",
     "Start here",
     "Legal and honest. Value rests entirely on the seriousness of the transcript and the endorsement of the church."),
    ("Network and denominational recognition",
     "None, but formally recognized by named networks for licensing or lay credentialing.",
     "Six to eighteen months of relationship work per partner.",
     "Highest leverage",
     "Costs almost nothing but relational capital, and it is the single biggest driver of perceived legitimacy."),
    ("Articulation with an accredited school",
     "Theirs, not yours. Your coursework earns credit toward their degree.",
     "One to two years to negotiate. Usually via block transfer or prior learning assessment.",
     "Do this in year two",
     "The student earns a real MA or MDiv from the partner. You become the on-ramp, which is a stronger position than being the destination."),
    ("Your own accreditation",
     "DEAC, ABHE, TRACS, or ATS, depending on the credential you want to grant.",
     "Three to seven years, with a legal institution, credentialed faculty, audits, and student services.",
     "Probably unnecessary",
     "Only worth it if the degree itself is the product. It is a different company than the one you are describing."),
]


def build():
    h = io.StringIO()
    W = h.write
    W("""<!DOCTYPE html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>SmallGroupSeminary.com &mdash; Framework and Curriculum Catalog</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,700;0,900;1,400&family=Cormorant+Garamond:ital,wght@0,400;0,600;1,400&family=Lato:wght@300;400;700;800&display=swap" rel="stylesheet">
<style>""" + CSS + "</style></head><body>")

    # ---------- cover ----------
    W("""<header class="cover"><div class="wrap">
<span class="eyebrow">A LifeTogether Ministries Straw&#8209;Man Framework</span>
<h1>Small Group<br><em>Seminary</em></h1>
<div class="dotcom">smallgroupseminary.com</div>
<div class="cover-rule"></div>
<p class="lede">Seminary&#8209;grade theological education, delivered where the church already
meets. Alone, in pairs, in a small group, or in a cohort. With real homework, real supervision,
and a credential that means something &mdash; <b>without pretending to be a degree.</b></p>
<div class="figs">""")
    for n, l in [("20", "Disciplines"), (str(TOTAL), "Courses"), ("3", "Rigor tracks"),
                 ("5", "Credential rungs"), ("4", "Delivery modes")]:
        W('<div class="fig"><div class="n">%s</div><div class="l">%s</div></div>' % (n, l))
    W("</div></div></header>")

    # ---------- verdict ----------
    W("""<section><div class="wrap"><div class="narrow">
<span class="eyebrow">The Honest Answer First</span>
<h2 class="sec">Yes. And it has already been done &mdash; just never at your distribution.</h2>
<div class="verdict"><p><span class="yes">Plausible, and scalable.</span> What does not scale
cheaply is the one thing that makes a credential real: a human being reading a student's work
and saying whether it is good enough.</p></div>
<div class="sec-body">
<p class="first">Three things have to be true for this to work, and only two of them are content
problems. The curriculum scales infinitely. The credential scales as far as its reputation
carries it. Assessment and supervision are the constraint, and every design decision below is
downstream of that one fact.</p>
<p>The precedent is strong. Kairos University, formerly Sioux Falls Seminary, runs an accredited
competency&#8209;based model in which the student's own ministry context is the classroom and a
mentor team &mdash; a faculty mentor plus a personal mentor plus a vocational mentor &mdash;
carries the assessment load, funded by a flat monthly tuition. It grew past four thousand
students across more than sixty countries. The Antioch School trains church leaders with
practitioners rather than professors, in cohorts, at a fraction of traditional seminary cost,
with competency&#8209;based credentials from certificate through doctorate.</p>
<p>So the model is proven. What none of them have is five hundred church relationships and a
twenty&#8209;five year distribution engine. That is the part you already own, and it is the part
that is genuinely hard to build.</p>
<p>The trap to avoid is the one that has killed most attempts: building a program that quietly
implies a degree. The moment a member believes the certificate is a Master of Divinity, you have
created a liability and a disappointment. The framework below is built so that the credential is
honest about what it is and unembarrassed about what it is not.</p>
</div></div></div></section>""")

    # ---------- missing middle ----------
    W("""<section class="tone"><div class="wrap">
<span class="eyebrow">Positioning</span>
<h2 class="sec">The missing middle</h2>
<p class="kicker">There are two doors into theological education, and about ninety-five percent of
serious lay Christians can walk through neither.</p>
<div class="rows">""")
    for lbl, hd, tx in [
        ("Door one", "The accredited seminary",
         "Seventy-two to ninety semester credits for a Master of Divinity, with ninety long the norm. "
         "Greek and Hebrew. Three to four years. Tuition, relocation, and an undergraduate degree as a "
         "prerequisite. Built for the vocationally called."),
        ("Door two", "The Bible college or institute",
         "Less rigorous by design, but still an enrollment, a transcript, a semester calendar, and a bill. "
         "Built for the eighteen-year-old, not the forty-two-year-old small group leader with three kids."),
        ("No door", "Everyone else",
         "The Sunday school teacher who has taught for eleven years and never had a course in hermeneutics. "
         "The elder who was handed a doctrinal statement he cannot defend. The small group leader who gets "
         "asked about suffering and has nothing but instinct. These are your five hundred churches."),
        ("The opening", "A third door",
         "Seminary content, church delivery, lay pacing, graduated rigor, and a credential earned rather "
         "than attended. Longer than seminary because it is part-time. Lighter than seminary because it "
         "omits the languages. Deeper than anything a church currently offers its members.")]:
        W('<div class="row"><div class="lbl">%s</div><div class="txt"><h4>%s</h4><p>%s</p></div></div>'
          % (lbl, hd, tx))
    W("</div></div></section>")

    # ---------- ladder ----------
    W("""<section class="dark"><div class="wrap">
<span class="eyebrow">The Credential Ladder</span>
<h2 class="sec">Five rungs, each one finishable</h2>
<p class="kicker">Every rung is a complete stopping point, not a partial degree. Nobody drops out;
they finish at the level they reached.</p>
<div class="ladder">""")
    for step, title, desc, load in [
        ("Rung 1", "Certificate of Biblical Foundations",
         "Four courses, chosen from the Foundation tier. The on-ramp, designed so a first-time student "
         "finishes something within a single ministry year.",
         "4 courses<br>1 year"),
        ("Rung 2", "Certificate in Ministry",
         "Twelve courses spanning at least six disciplines, including Hermeneutics and Systematic "
         "Theology. The credential most volunteer leaders should hold.",
         "12 courses<br>2 to 3 years"),
        ("Rung 3", "Diploma in Biblical and Theological Studies",
         "Twenty-four courses with required coverage across all ten historic disciplines, plus a "
         "supervised teaching assignment inside the local church.",
         "24 courses<br>4 to 5 years"),
        ("Rung 4", "Graduate of the Seminary",
         "Forty courses, a supervised ministry practicum, a capstone project, and a signed evaluation "
         "from both a faculty reviewer and the student's own pastor.",
         "40 courses<br>6 to 8 years"),
        ("Rung 5", "Fellow and Master Teacher",
         "Sixty courses, a teaching portfolio, an oral examination before a panel, and demonstrated "
         "reproduction: the Fellow has trained others who finished.",
         "60 courses<br>9 to 12 years")]:
        W('<div class="rung"><span class="step">%s</span><div><h4>%s</h4><p>%s</p></div>'
          '<div class="load">%s</div></div>' % (step, title, desc, load))
    W("""</div>
<p class="note" style="color:#9fb0c1;border-color:rgba(255,255,255,.15)">
Scale check, stated plainly: a course at twelve sessions plus graded work sits in the neighborhood
of three semester credits, which puts Rung 4 in the range of an accredited Master of Divinity by
seat time and reading load. It is not one, and should never be described as one. It lacks the
biblical languages, the academic supervision, and the accreditation. Say so on the certificate
itself.</p></div></section>""")

    # ---------- three tracks ----------
    W("""<section><div class="wrap">
<span class="eyebrow">Degrees of Homework</span>
<h2 class="sec">One course, three levels of rigor</h2>
<p class="kicker">This is the most important design decision in the whole system. Build the content
once; sell three different levels of accountability against it.</p>
<table class="tbl"><tr><th>Track</th><th>What the student does</th><th>Weekly load</th>
<th>Who assesses</th><th>Counts toward a credential</th></tr>""")
    for tr, does, load, who, counts in [
        ("Participant", "Attends, reads the assigned chapters, joins the discussion.", "About 2 hours",
         "Nobody. Self-paced.", "No"),
        ("Student", "Adds a reading log, written responses to set questions, quizzes, and a final project.",
         "5 to 6 hours", "Rubric plus cohort facilitator, with sampled review by a discipline reader.", "Yes"),
        ("Fellow", "Adds primary source reading, a substantial paper, teaching one session, and a supervised "
                   "ministry assignment.", "8 to 10 hours",
         "A credentialed discipline reader plus the student's ministry mentor.", "Yes, with honors")]:
        W("<tr><td class='pathname'>%s</td><td>%s</td><td class='small'>%s</td>"
          "<td class='small'>%s</td><td class='small'>%s</td></tr>" % (tr, does, load, who, counts))
    W("""</table>
<div class="two"><div class="col">
<h4>Why it works commercially</h4>
<p>A church can put ninety people through a course as Participants at almost no marginal cost,
while six of them pay to be assessed. The Participants are the funnel; the Fellows are the
margin; the credential is what makes both worth doing.</p></div>
<div class="col"><h4>Why it works pedagogically</h4>
<p>Mixed-track cohorts are better cohorts. The Fellow who has to teach a session raises the
quality of the discussion for everyone in the room, and the Participants provide the audience
that makes the Fellow's assignment real.</p></div></div>
</div></section>""")

    # ---------- delivery ----------
    W("""<section class="tone"><div class="wrap">
<span class="eyebrow">Delivery</span>
<h2 class="sec">Four ways to take the same course</h2>
<div class="rows">""")
    for lbl, hd, tx in [
        ("Solo", "One person, self-paced",
         "Reading, video, workbook, and online assessment. Available, but deliberately the least "
         "supported option: it is the fallback, not the default. Solo students may earn Rungs 1 and 2 "
         "and no further, because the higher rungs require witnesses."),
        ("Pairs", "Two people, mutual accountability",
         "The dyad is the most underrated unit in discipleship and the cheapest supervision structure "
         "that exists. Each partner signs off on the other's completion. Strongest for Hermeneutics, "
         "Spiritual Formation, and Evangelism."),
        ("Small group", "Six to twelve, facilitated",
         "The default and the differentiator. A trained volunteer facilitator, a twelve-week arc, and a "
         "cohort that starts and finishes together. This is the LifeTogether native format and the "
         "reason the whole thing is credible at your scale."),
        ("Church cohort", "Twenty to sixty, taught",
         "A master teacher on video or in the room, breakout tables, and a registrar at the church. "
         "This is the Sunday-morning or midweek class, and it is how a church launches the program to "
         "its whole congregation at once.")]:
        W('<div class="row"><div class="lbl">%s</div><div class="txt"><h4>%s</h4><p>%s</p></div></div>'
          % (lbl, hd, tx))
    W("""</div>
<p class="note">One content build has to serve all four. That means every course ships with a
master teaching session, a participant workbook, a facilitator guide, a discussion arc, an
assessment bank, and a solo-study path. This is the same package architecture already running
across the campaign and Adult Bible Fellowship libraries, which is why the marginal cost of a new
course here is lower for you than for anyone else attempting it.</p>
</div></section>""")

    # ---------- anatomy + supervision ----------
    W("""<section><div class="wrap">
<span class="eyebrow">Anatomy</span>
<h2 class="sec">What one course actually is</h2>
<div class="two" style="margin-top:30px"><div class="col">
<h4>The twelve-session shape</h4>
<p>Twelve sessions, ninety minutes each. Session one frames the discipline and the question.
Sessions two through ten work the material. Session eleven is application and integration.
Session twelve is assessment and commissioning, where students present rather than receive.</p>
<h4 style="margin-top:22px">The reading spine</h4>
<p>One accessible primary text, one standard reference work, and for Fellows one primary source
from the tradition. Roughly one hundred fifty pages per course at Student level and four hundred
at Fellow level.</p>
</div><div class="col">
<h4>The supervision team</h4>
<p>Borrowed from the competency-based model and adapted for a church rather than a school. Three
people stand behind each Student and Fellow, and only one of them costs money.</p>
<div class="rows" style="margin-top:16px">
<div class="row" style="padding:14px 0"><div class="lbl" style="flex:0 0 92px">Free</div>
<div class="txt"><h4 style="font-size:18px">Cohort facilitator</h4>
<p style="font-size:17px">A trained volunteer from the church who runs the room and verifies
attendance and completion.</p></div></div>
<div class="row" style="padding:14px 0"><div class="lbl" style="flex:0 0 92px">Free</div>
<div class="txt"><h4 style="font-size:18px">Ministry mentor</h4>
<p style="font-size:17px">A pastor or elder in the student's own church who signs the practicum
and speaks to character, not just coursework.</p></div></div>
<div class="row" style="padding:14px 0;border-bottom:none"><div class="lbl" style="flex:0 0 92px">Paid</div>
<div class="txt"><h4 style="font-size:18px">Discipline reader</h4>
<p style="font-size:17px">A credentialed reader who grades written work in their field. This is
the entire variable cost of the system and the whole unit economics question.</p></div></div>
</div></div></div>
<p class="note">On automated grading: a rubric-driven first pass can triage and comment, and it
genuinely helps a reader work faster. It cannot be the assessor of record, and if it is used at
all, disclose it plainly to students. The credential is worth exactly what the assessment behind
it is worth.</p>
</div></section>""")

    # ---------- accreditation ----------
    W("""<section class="dark"><div class="wrap">
<span class="eyebrow">The Accreditation Question</span>
<h2 class="sec">Four paths, and only one of them is a trap</h2>
<p class="kicker">The short version: you can grant certificates freely, you cannot grant degrees
without authorization, and the most valuable recognition available to you is not accreditation at
all.</p>
<table class="tbl" style="color:#e6e0d3">
<tr><th>Path</th><th>What you get</th><th>What it costs</th><th></th><th>The honest read</th></tr>""")
    for name, gets, costs, mark, read in ACCRED_ROWS:
        W("<tr><td class='pathname' style='color:#fbf8f1'>%s</td><td style='color:#d9d2c4'>%s</td>"
          "<td class='small' style='color:#9fb0c1'>%s</td><td><span class='mark'>%s</span></td>"
          "<td class='small' style='color:#9fb0c1'>%s</td></tr>" % (name, gets, costs, mark, read))
    W("""</table>
<div class="two" style="margin-top:40px"><div class="col">
<h4>Language you may use freely</h4>
<p style="color:#c9c0b0">Certificate. Diploma. Fellow. Graduate of the program. Course of study.
Credential. Completion. Institute. School of ministry.</p></div>
<div class="col"><h4>Language to avoid entirely</h4>
<p style="color:#c9c0b0">Master of Divinity. Master of Arts. Master of Ministry. Bachelor.
Doctorate. Degree. Credit hour without a partner behind it. Seminary-accredited. Any abbreviation
that reads as a postgraduate title after a person's name.</p></div></div>
<p class="note" style="color:#9fb0c1;border-color:rgba(255,255,255,.15)">
I am not a lawyer, and this is the part to take to one. Degree-granting authority and the use of
words like seminary, college, and university are regulated state by state, with religious
exemptions that vary widely in scope. Two questions to put to counsel before the domain goes live:
whether your entity may use the word seminary in your state and in the states of your largest
church partners, and what disclosure language has to appear on the certificate itself. The word
seminary is doing real marketing work in this name, and it is also the single biggest source of
both legal and expectation risk. Worth pressure-testing alternatives before you commit.</p>
</div></section>""")

    # ---------- languages ----------
    W("""<section><div class="wrap"><div class="narrow">
<span class="eyebrow">The Languages Decision</span>
<h2 class="sec">Do not teach Greek and Hebrew. Teach the tools, and say why.</h2>
<div class="sec-body">
<p>You named this yourself, and the instinct is right. Original language competence is the
clearest and most defensible line between this and a Master of Divinity. Trying to half-teach it
produces students who are dangerous with a lexicon and a program that cannot honestly claim
either position.</p>
<p>The recommendation is a Languages Toolkit built into Hermeneutics as two Advanced courses:
alphabet, transliteration, lexicons, interlinears, and Bible software, with the explicit aim of
teaching a student to <em>check</em> a word study rather than to <em>conduct</em> one. Paired with
a course on common interpretive mistakes, this is genuinely more useful to a lay teacher than one
year of Greek grammar that decays in eighteen months.</p>
<p>Then put the omission in the marketing rather than the fine print. A program confident enough
to name what it does not do reads as more credible, not less. It also opens the cleanest
articulation conversation with an accredited partner: they teach the languages, you teach
everything else, and a student who wants the degree finishes it there.</p>
</div></div></div></section>""")

    # ---------- benchmarking ----------
    W("""<section class="tone"><div class="wrap">
<span class="eyebrow">Method</span>
<h2 class="sec">How to benchmark this against real seminaries</h2>
<p class="kicker">You asked whether the content could be evaluated against top evangelical seminary
syllabi and against Bible colleges. It can, and here is the sequence that produces a defensible
answer rather than an impression.</p>
<ol class="steps">
<li><b>Pull the core, not the catalog.</b><span>For ten evangelical seminaries, extract only the
required Master of Divinity core, and separately the required core of any Master of Arts in
ministry or Christian studies. Electives are noise at this stage.</span></li>
<li><b>Pull the Bible college tier separately.</b><span>Required Bible and ministry cores from the
major institutes and Bible colleges. This is the tier your credential actually competes with, and
the comparison that will flatter you most.</span></li>
<li><b>Build a coverage matrix.</b><span>Every required course from every school maps to one of
your twenty disciplines. Any required course with no home is a gap in the catalog. Any discipline
with no external match is either a genuine innovation or a self-indulgence, and you need to know
which.</span></li>
<li><b>Extract the reading lists and count frequency.</b><span>A text required at seven of ten
schools is your reading spine. A text required at one is an elective. Frequency across schools is
a better curation signal than any single expert's opinion.</span></li>
<li><b>Extract assessment types, not just topics.</b><span>What the schools actually require
students to produce &mdash; exegetical papers, sermon manuscripts, case studies, verbatims,
theological position papers &mdash; becomes your Student and Fellow assignment bank. Rigor lives
here, not in the syllabus.</span></li>
<li><b>Name what you structurally cannot deliver.</b><span>Biblical languages. Thesis supervision.
Clinical pastoral education with licensed supervisors. Field education with a credentialed
supervisor. Write this list down and publish it. It is your honesty and your partnership
roadmap.</span></li>
<li><b>Have real scholars sign the result.</b><span>Recruit named authors and reviewers per
discipline, with their credentials printed beside the course. Without names, a catalog of four
hundred courses reads as content. With them, it reads as education.</span></li>
</ol></div></section>""")

    # ---------- catalog head ----------
    W("""<div class="cat-head"><div class="wrap">
<span class="eyebrow">The Curriculum</span>
<h2>Twenty disciplines, four hundred courses</h2>
<p>Doubled to twenty courses per discipline, with ten disciplines added that were not on the
previous list. Numbered in registrar order so depth is visible at a glance.</p>
<div class="legend">
<span><i>1xx</i> &nbsp;Foundation</span><span><i>2xx</i> &nbsp;Core</span>
<span><i>3xx</i> &nbsp;Advanced</span><span><i>10</i> &nbsp;Historic disciplines</span>
<span><i>10</i> &nbsp;New disciplines</span></div>
</div></div>""")
    W(catalog_html())

    # ---------- economics ----------
    W("""<section><div class="wrap">
<span class="eyebrow">Scale and Economics</span>
<h2 class="sec">What it takes to build, and what it can charge</h2>
<p class="kicker">Straw numbers, put here to be argued with rather than believed.</p>
<div class="two" style="margin-top:34px"><div class="col">
<h4>The build is the easy half</h4>
<p>Four hundred courses at twelve sessions is forty-eight hundred sessions, which is not a year
one project and should not be attempted as one. Sequence it: twenty flagship courses, one per
discipline, then one hundred, then two hundred, then the full four hundred. Every campaign,
Adult Bible Fellowship course, and small group series already in the library is a candidate for
conversion rather than a fresh build.</p>
<h4 style="margin-top:24px">The constraint is readers</h4>
<p>One reader can carry perhaps forty Student-track papers or twelve Fellow papers per term. Model
the reader pool as the ceiling on paid enrollment, then design the Participant track to be
genuinely excellent without one, because that is where the volume lives.</p>
</div><div class="col">
<h4>Straw pricing</h4>
<p>Participant access folded into the existing church subscription at no additional charge, because
it drives the funnel. Student track priced per course in the range of a good book plus a modest
assessment fee. Fellow track priced at roughly three times Student, reflecting the real reader
hours behind it. Church site license annually for unlimited Participants with a block of assessed
seats included.</p>
<h4 style="margin-top:24px">The real business</h4>
<p>The revenue is in assessed seats and site licenses. The moat is the five hundred church
relationships and the fact that no seminary can reach a Tuesday night living room. The asset that
compounds is the transcript: once a member has eleven completed courses on file with you, they do
not restart that record anywhere else.</p>
</div></div>
<p class="note">Risk register, briefly. Perception of a diploma mill is the central threat, and the
only defense is published standards: hours, assessors, reading loads, pass rates, and an explicit
statement of what the credential does not confer. Doctrinal breadth is the second threat, because a
twenty-discipline catalog necessarily touches baptism, eschatology, Calvinism, gender, and politics;
the pattern that keeps churches on board is to teach the positions fairly, name your own, and let
the local church set the line. The third is expectation drift, where a graduate believes they are
now qualified for a pulpit or a counseling practice. Say what this prepares someone for, and say
what it does not, in the same sentence, every time.</p>
</div></section>""")

    # ---------- roadmap ----------
    W("""<section class="dark"><div class="wrap">
<span class="eyebrow">Sequence</span>
<h2 class="sec">A four-phase path to a real school</h2>
<div class="rows">""")
    for lbl, hd, tx in [
        ("Phase one", "Prove the credential in one church",
         "Twenty flagship courses, one per discipline. One pilot church, three cohorts, all three tracks "
         "running at once. Publish the standards before the first cohort starts. The deliverable is not "
         "enrollment, it is a defensible transcript."),
        ("Phase two", "Recognition before expansion",
         "Take the pilot transcript to three denominations or networks and ask them to recognize the "
         "credential for lay licensing. Simultaneously open articulation conversations with two accredited "
         "schools. Recognition is worth more than the next hundred courses."),
        ("Phase three", "Catalog to two hundred, cohorts to fifty churches",
         "Convert existing library assets aggressively. Build the reader pool and the registrar system, "
         "which is the boring infrastructure that actually determines whether this survives."),
        ("Phase four", "Four hundred courses and a named faculty",
         "Full catalog, named authors and reviewers per discipline, Fellows who have reproduced, and the "
         "articulation agreements live so a student who wants the degree has somewhere to go.")]:
        W('<div class="row"><div class="lbl">%s</div><div class="txt"><h4>%s</h4><p>%s</p></div></div>'
          % (lbl, hd, tx))
    W("</div></div></section>")

    # ---------- close ----------
    W("""<div class="close"><div class="wrap">
<span class="eyebrow">The One-Sentence Version</span>
<h2>Seminary was built for the called.<br>This is built for the committed.</h2>
<p>A layman's course of study with real reading, real homework, real supervision, and a credential
that is honest about what it is. Taken alone, in pairs, in a small group, or in a cohort &mdash;
in the church, where the people already are.</p>
<a class="cta" href="#">Steer this draft</a>
</div></div>
<footer><div class="wrap">LifeTogether Ministries &nbsp;&middot;&nbsp; SmallGroupSeminary.com
&nbsp;&middot;&nbsp; Straw-man framework and curriculum catalog &nbsp;&middot;&nbsp;
%d courses across 20 disciplines</div></footer>
</body></html>""" % TOTAL)

    return h.getvalue()


if __name__ == "__main__":
    html = build()
    with open("/mnt/user-data/outputs/smallgroupseminary-framework-and-catalog.html", "w",
              encoding="utf-8") as f:
        f.write(html)
    print("bytes:", len(html))
    print("courses:", TOTAL)
