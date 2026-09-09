# -*- coding: utf-8 -*-
"""The Opposition Case — seminary objections, responses, stages, institutional analysis."""

import io

CSS = """
:root{--ink:#0c1723;--ink2:#08111c;--gold:#c19a4b;--goldlt:#e2c689;--parch:#f7f3ea;
--parch2:#efe8da;--rule:#d9cfbc;--body:#2b2a26;--muted:#6d6759;--mutedlt:#9fb0c1;}
*{box-sizing:border-box}
body{margin:0;background:var(--parch);color:var(--body);
font-family:"Cormorant Garamond",Georgia,serif;font-size:19px;line-height:1.62}
.wrap{max-width:940px;margin:0 auto;padding:0 30px}
.narrow{max-width:720px}
h1,h2,h3,h4{font-family:"Playfair Display",Georgia,serif;margin:0;letter-spacing:-.01em}
.eyebrow{font-family:"Lato",sans-serif;font-weight:800;font-size:10px;letter-spacing:.26em;
text-transform:uppercase;color:var(--gold);display:block}
p{margin:0 0 15px}

header{background:var(--ink);color:#f3efe6;padding:76px 0 64px;position:relative;overflow:hidden}
header:before{content:"";position:absolute;inset:0;
background:radial-gradient(110% 76% at 6% 0%,rgba(193,154,75,.18),transparent 62%)}
header .wrap{position:relative}
header .eyebrow{color:var(--goldlt)}
header h1{font-size:clamp(38px,7vw,72px);line-height:.98;color:#fbf8f1;margin-top:18px}
header h1 em{font-style:italic;font-weight:400;color:var(--goldlt)}
header .lede{font-size:22px;color:#cfc7b8;max-width:620px;margin-top:24px}
header .stamp{font-family:"Lato",sans-serif;font-size:10px;letter-spacing:.2em;text-transform:uppercase;
color:#7d8b99;margin-top:32px;border-top:1px solid rgba(193,154,75,.3);padding-top:16px}

section{padding:66px 0 58px;border-bottom:1px solid var(--rule)}
section.dark{background:var(--ink2);color:#e6e0d3;border-bottom:none}
section.dark h2,section.dark h3,section.dark h4{color:#fbf8f1}
section.dark .kick{color:var(--mutedlt)}
section.tone{background:var(--parch2)}
h2.sec{font-size:clamp(28px,4.4vw,42px);line-height:1.08;margin-top:15px}
.kick{font-style:italic;color:var(--muted);margin:14px 0 0;max-width:640px;font-size:20px}

/* numbered argument items */
.item{display:flex;gap:26px;padding:26px 0;border-top:1px solid var(--rule)}
section.dark .item{border-color:rgba(255,255,255,.13)}
.item .n{flex:0 0 52px;font-family:"Playfair Display",serif;font-size:34px;line-height:1;
color:transparent;-webkit-text-stroke:1px var(--gold);padding-top:2px}
section.dark .item .n{-webkit-text-stroke-color:var(--goldlt)}
.item .c{flex:1 1 auto;max-width:660px}
.item h4{font-size:21px;line-height:1.25;margin-bottom:9px}
.item p{margin:0 0 12px;font-size:18px}
.item p:last-child{margin-bottom:0}
section.dark .item p{color:#cfc7b8}
.answers{font-family:"Lato",sans-serif;font-size:9.5px;font-weight:800;letter-spacing:.16em;
text-transform:uppercase;color:var(--gold);display:block;margin-bottom:7px}
.stage-when{font-family:"Lato",sans-serif;font-size:9.5px;font-weight:800;letter-spacing:.16em;
text-transform:uppercase;color:var(--gold);display:block;margin-bottom:7px}
@media(max-width:640px){.item{gap:14px}.item .n{flex:0 0 36px;font-size:26px}}

/* case studies */
.case{border-top:1px solid var(--rule);padding:30px 0}
.case-top{display:flex;align-items:baseline;gap:14px;flex-wrap:wrap;margin-bottom:6px}
.case h3{font-size:25px}
.tag{font-family:"Lato",sans-serif;font-size:9px;font-weight:800;letter-spacing:.16em;
text-transform:uppercase;padding:4px 9px;white-space:nowrap}
.tag.partner{background:var(--gold);color:#fff}
.tag.compete{border:1px solid var(--gold);color:var(--gold)}
.tag.guard{border:1px solid var(--rule);color:var(--muted)}
.case .facts{font-family:"Lato",sans-serif;font-size:12.5px;color:var(--muted);
line-height:1.8;margin:12px 0 14px;border-left:2px solid var(--gold);padding-left:16px}
.case .lesson{font-family:"Playfair Display",serif;font-size:19px;line-height:1.42;
color:var(--ink);border-top:1px solid var(--rule);padding-top:14px;margin-top:6px}
.case .lesson b{color:var(--gold);font-family:"Lato",sans-serif;font-size:9.5px;
letter-spacing:.16em;text-transform:uppercase;display:block;margin-bottom:6px;font-weight:800}

.pull{font-family:"Playfair Display",serif;font-size:24px;line-height:1.4;
border-left:3px solid var(--gold);padding-left:24px;margin:30px 0;max-width:660px}
section.dark .pull{color:var(--goldlt)}
.note{font-family:"Lato",sans-serif;font-size:13px;line-height:1.75;color:var(--muted);
border-top:1px solid var(--rule);margin-top:36px;padding-top:16px;max-width:720px}
section.dark .note{color:var(--mutedlt);border-color:rgba(255,255,255,.15)}
.close{background:var(--ink);color:#efeae0;padding:74px 0;text-align:center}
.close h2{font-size:clamp(28px,4.6vw,42px);color:#fbf8f1}
.close p{max-width:620px;margin:20px auto 0;color:#c9c0b0}
footer{background:#070d15;color:#7d8b99;padding:26px 0;font-family:"Lato",sans-serif;
font-size:10.5px;letter-spacing:.1em;text-align:center;text-transform:uppercase}
@media(max-width:720px){body{font-size:18px}.wrap{padding:0 20px}section{padding:50px 0 44px}}
"""

THEIRS = [
("The heresy risk is real and it is not hypothetical",
 """Every serious error in church history was taught confidently by someone sincere who believed he was
 being faithful to the text. Seminaries exist partly as a filter: faculty who can catch a bad reading
 before it reaches a congregation, and a governance structure that can remove a teacher who will not
 be corrected. Remove the filter and you have not democratized theology, you have deregulated it. A
 catalog of four hundred courses without a faculty behind it is four hundred opportunities for
 something subtly wrong to be taught confidently to a room that has no way to know."""),
("Calling it seminary is an integrity problem, not a marketing decision",
 """This is the objection with the most force behind it, and it is a moral objection rather than a
 legal one. The word carries a status that has been earned by institutions over centuries through
 accreditation, faculty credentialing, and accountability. Borrowing the word without the substance
 transfers that credibility to something that has not paid for it. And when a graduate walks into an
 elder meeting believing he is seminary-trained, the person who let him believe it bears
 responsibility for the misunderstanding, whatever the fine print said."""),
("Without the languages, this is informed reading, not exegesis",
 """A student who cannot work in Greek or Hebrew is permanently dependent on translators and
 commentators for every disputed question. He can learn what scholars have concluded. He cannot weigh
 the evidence himself, which means at the exact point where interpretation matters most, he is
 repeating rather than reasoning. That is a fine thing to be. It is not theological education in the
 sense the word has meant for a thousand years, and calling it that inflates it."""),
("Formation is embodied, supervised, and slow",
 """Ministry preparation is not information transfer, which is why accredited programs require field
 education, clinical pastoral education with licensed supervisors, and years of faculty relationship.
 Character is shaped under people who can see you over time and tell you hard truths. A twelve-week
 cohort with a trained volunteer is a fine environment for learning content and a poor one for the
 slow work of forming a person who will carry other people's crises."""),
("A credential nobody can fail is not a credential",
 """If completion is verified by attendance and self-report, the certificate measures persistence, not
 competence. Real assessment requires someone with standing who is willing to tell a student the work
 is not good enough, and a structure that supports that person when the student complains. Absent
 that, churches will read the credential as an indication of readiness that it was never designed to
 carry, and will hand people responsibility they have not been evaluated for."""),
("It accelerates the erosion of institutions the church cannot rebuild",
 """Theological education is already under financial strain. Schools are merging and consolidating,
 and the Master of Divinity has been declining for years. A well-distributed lay alternative pulls
 exactly the curious, motivated adults who represent the future of the enrollment pipeline. Once the
 deep capacities go, the languages, the manuscript work, the research faculty, the church cannot
 conjure them back in a generation. Cheap and accessible has a long history of hollowing out the
 expensive and necessary."""),
("Commercial incentives and doctrinal integrity pull in opposite directions",
 """A ministry that sells subscriptions has a structural interest in enrolled, satisfied students, and
 satisfaction is a poor proxy for faithfulness. Doctrine is not a consumer product, and the pressure
 to keep churches renewing will, over enough years, push toward whatever teaches easily and offends
 least. Institutions with endowments and tenure are slow and expensive precisely so that they can
 afford to say things their market does not want to hear."""),
]

YOURS = [
("Objection 1 — heresy risk",
 "Name the faculty, publish the review, and make the guardrail visible",
 """The objection is correct in principle and the answer is structural, not rhetorical. Every course
 carries a named author and a named reviewer with printed credentials, and no course ships without a
 second reader in that discipline. Where the church legitimately disagrees, the course teaches the
 major positions fairly and leaves the line to the local church rather than resolving it in the
 workbook. Then go further than they expect: commission two seminary faculty to audit the curriculum
 independently and publish their critique unedited. An institution willing to print its own bad
 review is making a claim about itself that no marketing can make."""),
("Objection 2 — the integrity problem",
 "Print the ceiling on the certificate itself",
 """This is the only objection with the power to end the project, and it is entirely within your
 control. Every certificate states the hours completed, what was assessed and by whom, and in the
 same size type, what it does not confer: not a degree, not accreditation, not a qualification for
 ordination, not a license to counsel. Most degree marketing in Christian higher education is
 considerably vaguer about its own limits than that. If the word seminary cannot survive that
 disclosure, change the word — but do not carry the word and hide the ceiling."""),
("Objection 3 — no languages",
 "Concede it publicly, then turn it into the partnership door",
 """Do not argue this one. Agree, immediately and in print: this is not exegetical training, and a
 student who wants to weigh a disputed reading should go to seminary. Teach the toolkit so a member
 can check a word study rather than conduct one, and say plainly that checking is the ceiling. Then
 name the accredited partner who teaches the languages and publish the transfer path. Conceding the
 strongest objection is what buys credibility on the other six."""),
("Objection 4 — formation is embodied",
 "The mentor is the student's own pastor, who has known him for a decade",
 """This one can be answered on the merits. The supervision here is an elder or pastor in the
 student's own congregation who has watched him under pressure for years, plus a cohort of people who
 see him weekly. That is a denser observational field than a faculty advisor two thousand miles from
 the student's church, seen twice a semester. It is also not a novel argument: accredited
 competency-based programs already run on mentor teams, and the accreditors accepted the
 reasoning."""),
("Objection 5 — no real assessment",
 "Agree, then publish the numbers",
 """Concede that a course nobody grades measures attendance. That is exactly why the Participant
 track is labeled as unassessed on its own certificate. The Student and Fellow tracks are read by
 credentialed discipline readers who can and do fail work. Publish the reader roster, the ratio of
 readers to students, and the pass rate. A program that publishes its pass rate is making a
 falsifiable claim; almost nobody in this market does."""),
("Objection 6 — it erodes the institutions",
 "The data points the other way, and the pipeline runs toward them",
 """Total enrollment in accredited theological schools is at its highest level since 2006, and a
 substantial part of that growth is non-degree students, a trend running five years and still
 climbing. The market is already moving toward non-degree study whether or not anyone builds this.
 The live question is who serves it and with what accountability. Meanwhile the direction of travel
 for a Small Group Seminary student who catches fire is toward an accredited school, not away from
 it — so track that number and report it to the deans annually. Be their top of funnel and prove
 it."""),
("Objection 7 — commercial incentives",
 "Disclose the economics and give it away where the church cannot pay",
 """Publish the model: what a church pays, what a reader costs, what is bundled free. Then remove the
 incentive where it matters most by licensing the whole curriculum at no cost into contexts that
 cannot pay, and reporting those numbers alongside the revenue. On the broader point, say it
 charitably but say it: tuition-dependent institutions also carry enrollment incentives. The
 difference worth arguing about is not whether incentives exist but which ones are disclosed."""),
]

STAGES = [
("Stage One", "Beneath notice", "Months 0 to 18",
 """Nobody in institutional theological education is aware this exists. It is too small to register
 and there is no reason for a dean to hear about it. This is the most valuable window in the entire
 sequence and the one most people waste on marketing. Spend it instead on the things that are
 impossible to add later under scrutiny: the published standard, the named faculty, the independent
 audit, and one signed articulation agreement."""),
("Stage Two", "Private concern", "Year 1 to 2",
 """Pastors start mentioning it to deans. The question surfaces in hallway conversations at ETS and
 in denominational meetings. Nothing is written down yet and nothing is public, which means the
 entire stage is decided by whether the first thing a dean hears comes from you or about you. The
 difference between those two is the difference between the next four stages being a conversation and
 being a defense."""),
("Stage Three", "Public critique", "Year 2 to 3",
 """An article appears, or a podcast episode. The framing will be some version of do-it-yourself
 seminary and the danger of untrained teachers, and it will lead with objections one, two, and five.
 It may not name you. Do not rebut it in public. Answer it by having already published everything it
 asks for, and by asking its author to review a course."""),
("Stage Four", "Differentiation", "Year 3 to 4",
 """Institutions respond by restating clearly what only they can do: languages, exegesis,
 accreditation, ordination pathways, research. This stage looks adversarial and is actually the most
 useful thing that happens to you. It clarifies the market, tells churches which product is for which
 person, and gives you permission to stop explaining what you are not."""),
("Stage Five", "Absorption", "Year 4 to 6",
 """The strongest schools stop arguing and start building their own version or partnering with an
 existing one. This is the stage where the fight ends, because the leaders have joined. It is worth
 understanding that Talbot has effectively arrived here early and pre-emptively, before any of the
 first four stages have happened to you."""),
("Stage Six", "Normalization", "Year 6 to 10",
 """Church-based lay theological credentials become an ordinary category that nobody argues about,
 the way a certificate or diploma tier is ordinary now. Denominations recognize them for lay
 licensing. Some accredited schools grant advanced standing for them. At that point the strategic
 question stops being legitimacy and becomes market share, which is a much better problem."""),
]

HELPS = [
("Publish the standard before anyone asks for it",
 """Hours, assessors, reading loads, pass rates, and an explicit statement of what the credential does
 not confer, on the website from day one. Everything the critique will demand, already there."""),
("Go to the deans before you go to the pastors",
 """One conversation with a dean before an article gets written is worth more than any rebuttal
 afterward. Ask them to critique the curriculum, not endorse it. Critique invites ownership;
 endorsement requests invite caution."""),
("Build the transfer bridge as a feature, not a footnote",
 """Finish here, transfer there, with a named partner and a published credit map. It converts the
 sharpest objection into the clearest product benefit and makes you a feeder rather than a
 substitute."""),
("Commission an adversarial review and print it unedited",
 """Pay two credentialed faculty to find the weaknesses and publish what they find with no editorial
 control. It is the cheapest credibility available and it cannot be faked."""),
("Report the pipeline back to the institutions annually",
 """Track how many students go on to accredited programs and tell the schools the number. If it is
 real, it settles objection six permanently. If it is not, you need to know that before they do."""),
("Give the curriculum away where the church cannot pay",
 """Free licensing into the fastest-growing and least-resourced parts of the global church removes the
 commercial objection at its root and is the right thing to do independent of the argument."""),
("Never say the sentence that starts the war",
 """Some version of you do not need seminary will be tempting in a headline and it is the one sentence
 that turns a partnership into a defense. The correct sentence is that most of the church was never
 going to seminary, and something has to be true for them too."""),
]

CASES = [
("Talbot School of Theology", "partner", "Most likely partner. Already building this.",
 ["Ed Stetzer became dean in July 2023 and was installed in February 2024. He remains dean as of the "
  "2026 academic year.",
  "Talbot Embedded, funded by a Lilly grant, launches regional hybrid modular cohorts that embed "
  "Talbot training inside local ministry contexts. San Diego and Seattle opened in spring 2026, with "
  "Orlando, Chicago, Houston, Portland, the Bay Area, Phoenix, and Honolulu announced.",
  "In June 2026 Biola announced the acquisition of Phoenix Seminary, which donated its assets and "
  "rebranded as Talbot Seminary Phoenix, creating the second largest seminary in the country without "
  "a denominational affiliation at more than 1,800 graduate students.",
  "Talbot has become the named partner seminary for the Aspire Network, with further partnerships "
  "announced including Acts 29 and Stonecroft."],
 """Talbot is not the opponent in this story. It is running a version of the same thesis with
 accreditation attached, and it is scaling capacity through consolidation while its stated need is
 distribution into local ministry contexts. That is precisely the asset you hold and precisely the
 asset an institution cannot buy. Approach Talbot as the articulation partner, not as the incumbent
 to be disrupted."""),
("California Baptist University", "compete", "Competes by extending its own online degrees.",
 ["Southern Baptist affiliated, accredited by WSCUC, with a School of Christian Ministries and a "
  "Division of Online and Professional Studies offering dozens of online degrees.",
  "Offers a Bachelor of Applied Theology aimed at pastoral leaders, and a fully asynchronous online "
  "Christian Ministries degree described as suited to students far from campus or already serving in "
  "ministry."],
 """CBU has already claimed the adjacent territory at the undergraduate level, and its online
 Christian Ministries degree targets the same adult already serving in a church. The distinction to
 hold is that CBU sells an accredited degree to an individual, while you sell a formation system to a
 congregation. If those blur, you lose, because they have the accreditation and you do not. Keep the
 church, not the student, as the customer."""),
("Liberty University", "compete", "The precedent for what distribution does to an institution.",
 ["Distance education dates to the mid-1980s, when the School of Lifelong Learning mailed videotaped "
  "lectures and test packets to students. One early advertisement invited people to turn their living "
  "room into a college.",
  "By 2024 Liberty reported roughly 124,000 online students against about 16,000 on campus, with "
  "under twelve percent of students attending in person.",
  "Liberty Theological Seminary is now among the largest seminaries in the country by enrollment."],
 """This is the closest historical rhyme you have, and it should be read both ways. The institution
 that captured distribution became the largest Christian university in the world, and the residential
 campus became a rounding error in its own enrollment. That is the upside. The downside is equally
 instructive: scale invited permanent questions about rigor and identity that the school has never
 fully answered. Distribution wins the market and does not by itself win the argument."""),
("Jon Wallace and Azusa Pacific", "compete", "The separate-wrapper structural template.",
 ["President of APU from 2000 to 2019, after 43 years at the institution.",
  "Built six to seven regional campuses across Southern California and launched Los Angeles Pacific "
  "University as a separate institution for the online market."],
 """The most useful thing in this case is structural rather than strategic. When a new delivery model
 threatens the economics or the identity of the residential institution, one answer is to put it in a
 separate legal and brand wrapper rather than force it through the existing one. That is a live
 template for how a seminary could partner with Small Group Seminary without asking its faculty to
 approve it as their own program."""),
("Wayne Cordeiro and New Hope", "partner", "The pastor who bought the school.",
 ["New Hope Christian College in Eugene, formerly Eugene Bible College, has been accredited by the "
  "Association for Biblical Higher Education since 1983.",
  "The board planned to close the college and sell its assets in 2010. New Hope International, the "
  "church, invested 3.7 million dollars to stabilize it, and the school was renamed.",
  "Cordeiro served as president from 2010 and again from 2017, moving to chancellor in 2024. The "
  "college planted New Hope West on campus in 2020 as a lab church providing hands-on practicum."],
 """This is the case nobody in your position considers, and it deserves an hour. A church can acquire
 accreditation rather than apply for it. Small accredited schools are under real financial pressure
 and some are actively seeking partners — Phoenix Seminary donated its entire campus rather than
 close. Acquiring or affiliating with a struggling ABHE school is a materially faster path to a real
 credential than a multi-year accreditation application. The caution in the same case is just as
 sharp: New Hope nearly died, and required sustained subsidy from a church that believed in it."""),
]

STETZER_SAY = [
("What he would say publicly",
 """Something close to: the need is real, the church is under-trained, and I am glad somebody is
 taking it seriously. Followed immediately by the question of what it is called and what it claims.
 He has spent his career arguing that the academy and the church belong to each other, and his
 public register on institutional matters tends to be generous first and precise second. He is
 unlikely to write the critical article. He is very likely to be quoted in it."""),
("What he would ask, in order",
 """Who wrote it. Who reviewed it. Who grades it. What is the ceiling on the credential and where is
 that ceiling printed. And then the one that matters most to him institutionally: does a student who
 finishes this have somewhere to go next. Have all five answers in writing before the meeting, and
 lead with the ceiling rather than the vision."""),
("What he would want",
 """Named faculty, an honest ceiling, and a transfer path. If those three exist, this stops being a
 threat to Talbot and becomes a supply line into Talbot Embedded, which is the initiative he is
 personally building and needs local ministry contexts to fill. His stated expansion list already
 includes markets where you have church relationships."""),
("What he would do",
 """Most probably explore whether Small Group Seminary can function as the pre-Talbot tier — the
 on-ramp that identifies serious lay students in a congregation and hands the strongest of them to a
 Talbot Embedded cohort. Talbot has already demonstrated it will formalize partnerships of this
 shape with networks rather than only with individuals."""),
]


def build():
    h = io.StringIO(); W = h.write
    W("""<!DOCTYPE html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>The Opposition Case &mdash; Small Group Seminary</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,700;1,400&family=Cormorant+Garamond:ital,wght@0,400;0,600;1,400&family=Lato:wght@300;400;700;800&display=swap" rel="stylesheet">
<style>""" + CSS + "</style></head><body>")

    W("""<header><div class="wrap">
<span class="eyebrow">Small Group Seminary &nbsp;&middot;&nbsp; Strategic Analysis</span>
<h1>The Opposition<br><em>and the Opening</em></h1>
<p class="lede">What the seminaries will say, what you say back, how this actually unfolds, and why
the dean of Talbot is the wrong person to treat as an opponent.</p>
<div class="stamp">Prepared August 2026 &nbsp;&middot;&nbsp; Institutional facts verified from public
sources &nbsp;&middot;&nbsp; Attributed positions are inferred from public record, not statements
about this project</div>
</div></header>""")

    W("""<section class="dark"><div class="wrap">
<span class="eyebrow">Their Case</span>
<h2 class="sec">Seven objections, made as well as their best advocates would make them</h2>
<p class="kick">Written at full strength on purpose. A version of these you can easily knock down is
worth nothing to you.</p>""")
    for i, (head, body) in enumerate(THEIRS, 1):
        W('<div class="item"><span class="n">%d</span><div class="c"><h4>%s</h4><p>%s</p></div></div>'
          % (i, head, " ".join(body.split())))
    W("""<p class="note">Three of these are correct as stated. Objections three, four and five describe
real limits of the model rather than misunderstandings of it, and the response to each is concession
plus structure rather than argument. Recognizing which objections are true is the difference between
a defensible program and a defensive one.</p>
</div></section>""")

    W("""<section><div class="wrap">
<span class="eyebrow">Your Case</span>
<h2 class="sec">Seven responses, matched to the objection they answer</h2>
<p class="kick">Four of these are concessions. That is deliberate; a program that concedes nothing
sounds like a program that has not thought about it.</p>""")
    for i, (ans, head, body) in enumerate(YOURS, 1):
        W('<div class="item"><span class="n">%d</span><div class="c">'
          '<span class="answers">%s</span><h4>%s</h4><p>%s</p></div></div>'
          % (i, ans, head, " ".join(body.split())))
    W("""<div class="pull">The winning posture is not rebuttal. It is to be the most transparent
institution in the conversation, and to be visibly useful to the schools rather than visibly
competitive with them.</div>
</div></section>""")

    W("""<section class="tone"><div class="wrap">
<span class="eyebrow">Projected Evolution</span>
<h2 class="sec">Six stages, and where you already are</h2>
<p class="kick">This sequence is predictable because it has run before, in online education, in
competency-based degrees, and in every credential the academy did not originate.</p>""")
    for i, (label, name, when, body) in enumerate(STAGES, 1):
        W('<div class="item"><span class="n">%d</span><div class="c">'
          '<span class="stage-when">%s &nbsp;&middot;&nbsp; %s</span><h4>%s</h4><p>%s</p></div></div>'
          % (i, label, when, name, " ".join(body.split())))
    W("""<p class="note">The unusual feature of your position is that Stage Five is already available
before Stages Two through Four have happened. Talbot Embedded exists now. That means the whole
adversarial arc is skippable if the first institutional conversation happens early and goes well,
and it becomes unavoidable if the first thing the institutions hear is a launch announcement.</p>
</div></section>""")

    W("""<section class="dark"><div class="wrap">
<span class="eyebrow">Supporting the Process</span>
<h2 class="sec">Seven moves that make you an ally instead of a target</h2>""")
    for i, (head, body) in enumerate(HELPS, 1):
        W('<div class="item"><span class="n">%d</span><div class="c"><h4>%s</h4><p>%s</p></div></div>'
          % (i, head, " ".join(body.split())))
    W("</div></section>")

    W("""<section><div class="wrap">
<span class="eyebrow">Institutional Responses</span>
<h2 class="sec">Three moves available to a school, and who is making which</h2>
<p class="kick">Guard the standard, compete directly, or absorb the model. Every institution picks
one, and the choice is usually visible years in advance from what they are already building.</p>""")
    for name, tag, tagline, facts, lesson in CASES:
        tagname = {"partner": "Absorb or partner", "compete": "Compete directly",
                   "guard": "Guard the standard"}[tag]
        W('<div class="case"><div class="case-top"><h3>%s</h3>'
          '<span class="tag %s">%s</span></div>' % (name, tag, tagname))
        W('<p style="color:var(--muted);font-style:italic;margin:0 0 6px">%s</p>' % tagline)
        W('<div class="facts">%s</div>' % "<br>".join(facts))
        W('<p class="lesson"><b>What it means for you</b>%s</p></div>' % " ".join(lesson.split()))
    W("</div></section>")

    W("""<section class="tone"><div class="wrap">
<span class="eyebrow">The Specific Question</span>
<h2 class="sec">What Ed Stetzer would say and do</h2>
<p class="kick">Inferred from his public record and current initiatives. He has said nothing about
this project, and everything below should be treated as a prediction rather than a position.</p>""")
    for i, (head, body) in enumerate(STETZER_SAY, 1):
        W('<div class="item"><span class="n">%d</span><div class="c"><h4>%s</h4><p>%s</p></div></div>'
          % (i, head, " ".join(body.split())))
    W("""<div class="pull">Go to Talbot first, and go with the ST 101 build rather than the manifesto.
Ask for a critique, not a blessing.</div>
<p class="note">One caution worth holding. Stetzer is a practitioner-scholar leading a faculty, and a
dean cannot get out in front of his faculty on a question of credentialing. Anything that reads as
competing with the Master of Divinity puts him in an impossible position internally. Anything framed
as identifying and preparing students who then enroll at Talbot puts him in a very easy one. The same
project can be presented either way, and the framing is the entire negotiation.</p>
</div></section>""")

    W("""<div class="close"><div class="wrap">
<h2>The argument you win is not that they are wrong.<br>It is that you are useful.</h2>
<p>Concede the three objections that are true, publish the ceiling before anyone demands it, and walk
into the first institutional conversation carrying a transfer path instead of a manifesto.</p>
</div></div>
<footer><div class="wrap">LifeTogether Ministries &middot; Small Group Seminary &middot; Opposition
and response analysis &middot; August 2026</div></footer></body></html>""")
    return h.getvalue()


if __name__ == "__main__":
    out = build()
    p = "/mnt/user-data/outputs/smallgroupseminary-opposition-analysis.html"
    open(p, "w", encoding="utf-8").write(out)
    print("bytes:", len(out))
    print("balance div:", out.count("<div") - out.count("</div>"),
          "| section:", out.count("<section"), out.count("</section>"))
