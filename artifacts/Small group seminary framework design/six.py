# -*- coding: utf-8 -*-
"""Six decisions: Dallas, Biola, the light model, donor funding, customization, the front door."""
import io

CSS = """
:root{--ink:#0c1723;--ink2:#08111c;--gold:#c19a4b;--goldlt:#e2c689;--parch:#f7f3ea;
--parch2:#efe8da;--rule:#d9cfbc;--body:#2b2a26;--muted:#6d6759;--mutedlt:#9fb0c1;}
*{box-sizing:border-box}
body{margin:0;background:var(--parch);color:var(--body);
font-family:"Cormorant Garamond",Georgia,serif;font-size:19px;line-height:1.62}
.wrap{max-width:900px;margin:0 auto;padding:0 30px}
h1,h2,h3,h4{font-family:"Playfair Display",Georgia,serif;margin:0;letter-spacing:-.01em}
.eyebrow{font-family:"Lato",sans-serif;font-weight:800;font-size:10px;letter-spacing:.26em;
text-transform:uppercase;color:var(--gold);display:block}
p{margin:0 0 15px}
header{background:var(--ink);color:#f3efe6;padding:66px 0 56px;position:relative;overflow:hidden}
header:before{content:"";position:absolute;inset:0;
background:radial-gradient(112% 78% at 7% 0%,rgba(193,154,75,.18),transparent 62%)}
header .wrap{position:relative}
header .eyebrow{color:var(--goldlt)}
header h1{font-size:clamp(34px,6vw,58px);line-height:1.02;color:#fbf8f1;margin-top:16px}
header h1 em{font-style:italic;font-weight:400;color:var(--goldlt)}
header .lede{font-size:21px;color:#cfc7b8;max-width:620px;margin-top:22px}
section{padding:58px 0 50px;border-bottom:1px solid var(--rule)}
section.dark{background:var(--ink2);color:#e6e0d3;border-bottom:none}
section.dark h2,section.dark h3,section.dark h4{color:#fbf8f1}
section.dark p{color:#d6cec0}
section.tone{background:var(--parch2)}
.qnum{font-family:"Playfair Display",serif;font-size:14px;color:var(--gold);letter-spacing:.14em}
h2.sec{font-size:clamp(26px,4.1vw,38px);line-height:1.1;margin-top:12px;max-width:760px}
.verdict{font-family:"Playfair Display",serif;font-size:23px;line-height:1.42;
border-left:3px solid var(--gold);padding-left:22px;margin:24px 0;max-width:660px}
section.dark .verdict{color:var(--goldlt)}
.body{max-width:700px;margin-top:22px}
h4.sub{font-size:20px;margin:26px 0 10px}
.facts{font-family:"Lato",sans-serif;font-size:12.5px;line-height:1.85;color:var(--muted);
border-left:2px solid var(--gold);padding-left:16px;margin:18px 0}
section.dark .facts{color:var(--mutedlt)}
table{width:100%;border-collapse:collapse;margin-top:24px;font-size:17px}
th{font-family:"Lato",sans-serif;font-weight:800;font-size:10px;letter-spacing:.15em;
text-transform:uppercase;color:var(--gold);text-align:left;padding:0 14px 11px 0;
border-bottom:1px solid var(--rule);vertical-align:bottom}
td{padding:13px 14px 13px 0;border-bottom:1px solid var(--rule);vertical-align:top}
td.k{font-family:"Playfair Display",serif;font-size:17.5px;width:30%}
td.n{font-family:"Lato",sans-serif;font-size:14px;white-space:nowrap;color:var(--gold);font-weight:700}
td.s{color:var(--muted);font-size:16.5px}
section.dark td{border-color:rgba(255,255,255,.13)}
section.dark td.k{color:#fbf8f1}
section.dark td.s{color:var(--mutedlt)}
section.dark td.n{color:var(--goldlt)}
ul{margin:0 0 15px;padding-left:20px;max-width:680px}
li{margin-bottom:8px}
.note{font-family:"Lato",sans-serif;font-size:13px;line-height:1.75;color:var(--muted);
border-top:1px solid var(--rule);margin-top:30px;padding-top:15px;max-width:700px}
section.dark .note{color:var(--mutedlt);border-color:rgba(255,255,255,.15)}
.close{background:var(--ink);color:#efeae0;padding:66px 0;text-align:center}
.close h2{font-size:clamp(25px,4.1vw,38px);color:#fbf8f1}
.close p{max-width:600px;margin:18px auto 0;color:#c9c0b0}
footer{background:#070d15;color:#7d8b99;padding:24px 0;font-family:"Lato",sans-serif;
font-size:10.5px;letter-spacing:.1em;text-align:center;text-transform:uppercase}
@media(max-width:720px){body{font-size:18px}.wrap{padding:0 20px}section{padding:44px 0 38px}}
"""

def build():
    h = io.StringIO(); W = h.write
    W("""<!DOCTYPE html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Six Decisions &mdash; Doing Seminary Together</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,700;1,400&family=Cormorant+Garamond:ital,wght@0,400;0,600;1,400&family=Lato:wght@300;400;700;800&display=swap" rel="stylesheet">
<style>""" + CSS + "</style></head><body>")

    W("""<header><div class="wrap">
<span class="eyebrow">Doing Seminary Together &nbsp;&middot;&nbsp; Decision Brief</span>
<h1>Six answers,<br><em>and one reordering</em></h1>
<p class="lede">Dallas, Biola, the lightest revenue model available right now, how much of this
belongs on the donor side, whether customization is the real business, and where the front door
should actually be.</p>
</div></header>""")

    # 1 — Dallas
    W("""<section><div class="wrap">
<span class="qnum">Question One</span>
<h2 class="sec">What Dallas will say</h2>
<div class="verdict">They will make the languages objection harder than anyone else in the country,
and they will be right to. Do not argue with Dallas. Convert them last, with their own edition.</div>
<div class="body">
<p>DTS is the single institution with the most standing to object, and the objection is structural
rather than temperamental. Their flagship degree is not a Master of Divinity at all &mdash; it is a
four-year, 120-hour Master of Theology requiring roughly two and a half years of Greek and two years
of Hebrew. Their founding vision, still stated, is a seminary where every book of the Bible is
taught. Exegetical rigor is not one of their values. It is the institution's whole identity.</p>
<p>So the sentence you will hear from Dallas is some version of: a course of study that teaches
twenty disciplines and every book of the Bible without a day of Greek is claiming our vision while
declining our discipline. That is a fair criticism, it will be made by people who have earned the
right to make it, and the correct response is the one already in the plan &mdash; concede it in
print, name the ceiling, and point to the partner who teaches languages.</p>
<h4 class="sub">Three things about Dallas that cut the other way</h4>
<p>First, DTS already requires small-group spiritual formation: groups of five to seven students
meeting across four consecutive terms, focused on identity, community, integrity, and fidelity. They
believe the small group forms people. They have simply never used it to carry content. That is a
shorter argument than it looks.</p>
<p>Second, they already run a non-degree tier &mdash; a Certificate of Graduate Studies. The category
you are proposing is not foreign to them. It is on their own program list.</p>
<p>Third, and most usefully, DTS is dispensational and premillennial by conviction. A curriculum that
teaches eschatology fairly across positions is not neutral to them, it is a problem. Which means
Dallas is not an objection to be answered. Dallas is a denominational edition to be built, where
their faculty set the line on the pages that matter to them.</p>
<div class="facts">
Dallas Theological Seminary &nbsp;&middot;&nbsp; founded 1924, non-denominational, dispensational<br>
President Mark Yarbrough &nbsp;&middot;&nbsp; Chancellor Mark Bailey<br>
No MDiv. Flagship is the four-year ThM, 120 credit hours, with 2.5 years Greek and 2 years Hebrew<br>
Roughly 2,000 to 2,600 students, many online or at extension campuses; about 16,000 alumni<br>
Required spiritual formation in small groups of five to seven, four consecutive terms<br>
Motto: Teach Truth. Love Well.
</div>
<p class="note">Sequence Dallas last, not first. They are the hardest conversation and the most
valuable endorsement, and both of those are true for the same reason. Walk in with a Talbot letter
already in hand and the conversation is entirely different from walking in cold.</p>
</div></div></section>""")

    # 2 — Stetzer / Corey
    W("""<section class="dark"><div class="wrap">
<span class="qnum">Question Two</span>
<h2 class="sec">Will Stetzer or the Biola president partner</h2>
<div class="verdict">Stetzer, probably, on a feeder relationship. Corey, not at the concept stage
&mdash; and he is not the gate anyway. The provost is.</div>
<div class="body">
<p>These are three different conversations and it is worth not confusing them, because approaching a
president with a curriculum question is how good ideas die politely.</p>
<h4 class="sub">Ed Stetzer, dean</h4>
<p>Likely yes to a conversation and likely yes to an informal feeder relationship, because it costs
him nothing and fills the initiative he is personally building. Slow to anything with Biola's name on
a certificate, because a dean cannot get ahead of his faculty on credentialing. Lead with the
ceiling, not the vision.</p>
<h4 class="sub">Matthew Hall, provost</h4>
<p>This is the actual gate and the name to know. Any arrangement that touches credit, credential, or
the university's name runs through the provost's office, and provosts are paid to say no to exactly
this category of proposal. He came out of a serious academic environment and will read the
curriculum rather than the deck. If the named faculty and the published ceiling are real, he is
persuadable. If they are aspirational, he will find that in one meeting.</p>
<h4 class="sub">Barry Corey, president</h4>
<p>Nineteen years in the chair, and his background is not what most people assume. Before Biola he was
academic dean and chief academic officer at Gordon-Conwell, and before that its vice president for
development, where he ran a fifty-four million dollar campaign. At Biola he has led a campaign past
a hundred and eighty million and just absorbed an entire seminary through the Phoenix acquisition.</p>
<p>A president in that seat does not evaluate curriculum. He evaluates three things: enrollment
pipeline, donor story, and institutional risk. So the pitch to Corey is not the one you would make to
Stetzer. It is a number of students who arrived at Talbot Embedded because of this and would not have
otherwise, a named funder willing to underwrite it, and a clear account of what protects the Biola
name if it goes wrong.</p>
<div class="verdict">Stetzer opens the door. Hall decides. Corey funds it or blesses it, and only
after the other two have already said yes.</div>
<p class="note">Nothing here is based on any statement by any of these three about this project. It
is inference from public record and current initiatives, and it should be held loosely.</p>
</div></div></section>""")

    # 3 — light model
    W("""<section class="tone"><div class="wrap">
<span class="qnum">Question Three</span>
<h2 class="sec">The lightest revenue model available right now</h2>
<div class="verdict">Six courses, one denomination, one letter. Not four hundred courses, not
accreditation, and not a platform.</div>
<div class="body">
<p>The version of this that could be real inside six months looks nothing like the catalog. It is a
single named certificate &mdash; call it the Year One Certificate &mdash; built from six courses, one
denominational partner who licenses it for their churches, and one seminary willing to write a letter
of academic review. Not accreditation. Not articulation. A letter saying credentialed faculty
reviewed the material and found it sound. That letter does more selling than the next hundred
courses.</p>
<p>The six courses pick themselves, because they are the ones every church already wants: how to read
the Bible for yourself, the story of the Old Testament, the story of the New Testament, what doctrine
is for, what a disciple is, and anyone can teach the Bible. That is a coherent first year and it
stands alone as a product even if nothing else is ever built.</p>
<table>
<tr><th>Line</th><th>Straw</th><th>Note</th></tr>
<tr><td class="k">Six courses built</td><td class="n">$90,000</td><td class="s">At $15,000 all in per course. Materially less where existing assets convert rather than being written new</td></tr>
<tr><td class="k">One network license</td><td class="n">$80,000</td><td class="s">A mid-size denomination or church network, annually</td></tr>
<tr><td class="k">Twenty-five direct churches</td><td class="n">$60,000</td><td class="s">Founders pricing off the existing relationship base</td></tr>
<tr><td class="k">One custom church build</td><td class="n">$40,000</td><td class="s">The Pastor's Library edition, one flagship church, priced as a project</td></tr>
<tr><td class="k">Year one net</td><td class="n">+$90,000</td><td class="s">Before overhead, and assuming conversion rather than new build on at least half the courses</td></tr>
</table>
<p class="note">The whole point of the light model is that it is falsifiable inside a year. If one
denomination will not license six good courses backed by a seminary review letter, the four hundred
course catalog was never going to sell either, and you will have learned that for ninety thousand
dollars instead of six million.</p>
</div></div></section>""")

    # 4 — kingdom impact
    W("""<section><div class="wrap">
<span class="qnum">Question Four</span>
<h2 class="sec">How much of this is a Kingdom Impact thing</h2>
<div class="verdict">The build is donor-funded. The distribution is revenue-funded. Say that
publicly and the commercial-motive objection stops existing.</div>
<div class="body">
<p>More of this belongs on the donor side than anything else you have built, and for a specific
reason: donors fund access, not products. A subscription library for churches is not a fundable
sentence. Theological training for a hundred thousand lay leaders who were never going to seminary is
one of the most fundable sentences in evangelical philanthropy, and it happens to be true.</p>
<p>The structure is already sitting in the Pastor's Library Project prospectus and transfers almost
without modification. There, one family funds one library at a hundred thousand. Here, one family
funds one discipline. Roughly a hundred and fifty thousand endows the twenty courses in Systematic
Theology or Old Testament, named, in perpetuity, with the faculty honoraria and the filming inside
the number. Twenty disciplines is three million dollars and it is the entire catalog.</p>
<h4 class="sub">Why the split matters beyond the money</h4>
<p>It resolves the seventh objection structurally rather than rhetorically. When a critic says
commercial incentives will eventually corrupt the content, the answer is that the content was paid
for before anyone subscribed, by donors with no interest in enrollment, and the subscription revenue
funds operations rather than curriculum. That is not a defense. It is an org chart.</p>
<p>It also makes the free global licensing real rather than gestural. A donor-funded course carries
no marginal cost, so giving it away where the church cannot pay costs nothing and becomes the
headline rather than the footnote.</p>
<p class="note">The Signatry relationship is the obvious first conversation and the shape of it is
familiar to them &mdash; aggregating content that needs a home is close to what they already do.
Treat the discipline-endowment structure as a proposal to be tested, not a plan, until someone has
actually said yes to one.</p>
</div></div></section>""")

    # 5 — customization
    W("""<section class="dark"><div class="wrap">
<span class="qnum">Question Five</span>
<h2 class="sec">Is the customization thing bigger than you thought</h2>
<div class="verdict">Yes. It may be the business, and the seminary may be the category that makes it
sellable.</div>
<div class="body">
<p>You already learned this once on the Sermon Library and wrote it down: the money is not in the
subscriptions, it is in the builds. The same logic applies here with more force, because the object
being customized is larger.</p>
<p>A church edition assembled from that pastor's own archive is not a curriculum sale. It is his
thirty years of preaching turned into a structured course of study with his name on it, taught to his
own congregation, with his positions and his illustrations and his voice in the introductions. Nobody
can copy that, because nobody else asks for the archive. And a pastor past fifty-five will buy that
for reasons that are not primarily financial.</p>
<p>The pricing follows the object. Twenty courses built from one library is not a two-thousand-dollar
build. It is somewhere between twenty-five and seventy-five thousand, and the church that says yes to
it is not comparison-shopping against a video library.</p>
<div class="verdict">The seminary is the category. The customization is the business. Doing Seminary
Together is what makes a pastor understand what he is buying; the build is what he actually
pays for.</div>
<p class="note">The constraint you already named on the Sermon Library applies here and harder.
Three hundred churches wanting custom devotionals is an operations problem. Fifty churches wanting
custom seminaries is a bigger one, and it arrives before the revenue does. Decide the annual build
capacity before selling the first one, and price to that number rather than to demand.</p>
</div></div></section>""")

    # 6 — front door
    W("""<section class="tone"><div class="wrap">
<span class="qnum">Question Six</span>
<h2 class="sec">Attaching it to SmallGroupCurriculum.com</h2>
<div class="verdict">Yes, and it is the same move you already made with the Sermon Library. Curriculum
is the front door. Seminary is what is inside.</div>
<div class="body">
<p>Nobody searches for a small group seminary. That phrase does not exist in anyone's head, which
means the domain wins no traffic and, worse, it leads with the word that triggers every objection
before you have earned the conversation. Curriculum is what pastors and group leaders actually type,
in volume, every week of the year.</p>
<p>This is the identical logic you settled on for the Sermon Library: the free front door wins search
and matches what people expect to find, and the paid product with the real depth sits behind it. It
worked there for the same reason it will work here.</p>
<table>
<tr><th>Property</th><th>Role</th><th>What lives there</th></tr>
<tr><td class="k">SmallGroupCurriculum.com</td><td class="s"><b>Front door, free tier</b></td><td class="s">The whole curriculum world in one place &mdash; the campaign library, the ABF material, the group studies, and the course catalog. Wins search, matches volume expectation, never charged for</td></tr>
<tr><td class="k">Doing Seminary Together</td><td class="s"><b>The branded pathway</b></td><td class="s">The structured course of study inside it. Disciplines, tiers, the certificate, the faculty. This is the thing with a name, not a URL</td></tr>
<tr><td class="k">SmallGroupSeminary.com</td><td class="s"><b>Redirect and secondary asset</b></td><td class="s">Hold it, point it at the pathway, do not lead with it</td></tr>
</table>
<p>There is a second benefit that matters more than the search argument. Putting this under a
curriculum domain unifies the ecosystem instead of adding a fifth site to it. The campaign platform,
the ABF material, the group studies and Deepening Life Together stop being four separate assets and
become one library with a structured pathway running through it. That is a far stronger story to a
pastor, to a denomination, and to a donor than a standalone seminary with four hundred titles and
one built course.</p>
<p class="note">One thing to check before committing: whether SmallGroupCurriculum.com is actually
held or only on the list. The domain notes carry a mix of owned, leased, and wanted, and this
decision depends on which.</p>
</div></div></section>""")

    W("""<div class="close"><div class="wrap">
<h2>Six courses, one denomination, one letter.<br>Donors fund the build. Churches fund the use.</h2>
<p>Curriculum on the door, seminary inside, and the custom build is where the money actually is
&mdash; exactly as it turned out to be on the Sermon Library.</p>
</div></div>
<footer><div class="wrap">LifeTogether Ministries &middot; Doing Seminary Together &middot; Decision
brief &middot; August 2026</div></footer></body></html>""")
    return h.getvalue()


if __name__ == "__main__":
    out = build()
    p = "/mnt/user-data/outputs/doing-seminary-together-six-decisions.html"
    open(p, "w", encoding="utf-8").write(out)
    print("bytes:", len(out), "| div:", out.count("<div") - out.count("</div>"),
          "| sections:", out.count("<section"), out.count("</section>"))
