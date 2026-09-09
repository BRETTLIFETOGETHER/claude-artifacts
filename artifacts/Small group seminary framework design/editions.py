# -*- coding: utf-8 -*-
"""Editions, certification, the sending model, and the hundred-faculty prospect list."""
import io

# (name, affiliation, note, warm)  warm: "" | "prior" | "client" | "talbot"
FACULTY = [
("Systematic Theology", [
 ("Fred Sanders", "Biola, Torrey Honors", "Trinity and classical theism for non-specialists", "talbot"),
 ("Kevin Vanhoozer", "Trinity Evangelical", "Theological method; would set the standard for the discipline", ""),
 ("Michael Horton", "Westminster Seminary California", "Reformed anchor; essential for the Reformed edition", ""),
 ("Beth Felker Jones", "Northern Seminary", "Wesleyan anchor; essential for the Wesleyan edition", ""),
 ("Kelly Kapic", "Covenant College", "Suffering, humanity, and doctrine that reaches the pew", ""),
]),
("Old Testament", [
 ("Sandra Richter", "Westmont College", "The Epic of Eden; already teaches lay audiences at scale", ""),
 ("Carmen Joy Imes", "Biola, Talbot", "Bearing God's Name; unusually good on video", "talbot"),
 ("Christopher J. H. Wright", "Langham Partnership", "Old Testament ethics and mission; global reach", ""),
 ("Bill T. Arnold", "Asbury Theological", "Pentateuch and historical books", ""),
 ("Iain Provan", "Regent College", "Regent's whole model is lay theological education", ""),
]),
("New Testament", [
 ("Mark Strauss", "Bethel Seminary", "Already taught for you. First call in the discipline", "prior"),
 ("Michael Wilkins", "Biola, Talbot", "Already taught for you. Matthew and discipleship", "prior"),
 ("Nijay Gupta", "Northern Seminary", "Prolific, church-facing, mid-career, high yes probability", ""),
 ("Lynn Cohick", "Houston Christian University", "Pauline letters and women in the early church", ""),
 ("Craig Keener", "Asbury Theological", "Acts and background; the reference standard", ""),
]),
("Church History", [
 ("Thomas Kidd", "Midwestern Seminary", "American evangelicalism, awakenings, Whitefield", ""),
 ("Jennifer Powell McNutt", "Wheaton College", "Reformation and the history of the church's teaching", ""),
 ("Michael Haykin", "Southern Seminary", "Patristics and Baptist history", ""),
 ("Bruce Gordon", "Yale Divinity", "Calvin and the Reformation; prestige signal", ""),
 ("Chris Gehrz", "Bethel University", "Writes history for ordinary Christians deliberately", ""),
]),
("Hermeneutics", [
 ("Craig Blomberg", "Denver Seminary", "Interpretation and gospel reliability", ""),
 ("Jeannine Brown", "Bethel Seminary", "Scripture as Communication; the textbook choice", ""),
 ("Michael Gorman", "St. Mary's Seminary", "Reading Paul; cross-tradition credibility", ""),
 ("Douglas Moo", "Wheaton College", "Translation and the epistles", ""),
 ("Matthew Bates", "Quincy University", "Accessible on method and on faith itself", ""),
]),
("Apologetics", [
 ("Sean McDowell", "Biola, Talbot", "Youth and deconstruction; enormous existing audience", "talbot"),
 ("Rebecca McLaughlin", "Author, Confronting Christianity", "Best current writer for the honest skeptic", ""),
 ("Gavin Ortlund", "Truth Unites", "Charitable, historically grounded, native to video", ""),
 ("Paul Copan", "Palm Beach Atlantic", "Hard Old Testament questions", ""),
 ("Michael Licona", "Houston Christian University", "Resurrection evidence", ""),
]),
("Homiletics", [
 ("Bryan Chapell", "Author, Christ-Centered Preaching", "The standard text on redemptive preaching", ""),
 ("Jared Alcantara", "Baylor, Truett Seminary", "Practices of preaching; strong on cross-cultural", ""),
 ("Charlie Dates", "Salem Baptist Church, Chicago", "Practitioner of the first rank", ""),
 ("Jeffrey Arthurs", "Gordon-Conwell", "Preaching genre by genre", ""),
 ("Scott Gibson", "Baylor, Truett Seminary", "Preaching history and method", ""),
]),
("Pastoral Care", [
 ("Diane Langberg", "Clinical psychologist, author", "Trauma and abuse in the church; the essential voice", ""),
 ("Ed Welch", "CCEF", "Biblical counseling with clinical seriousness", ""),
 ("Curt Thompson", "Psychiatrist, author", "Neuroscience, shame, and formation", ""),
 ("Chuck DeGroat", "Western Theological Seminary", "Narcissism and leadership failure in the church", ""),
 ("John Swinton", "University of Aberdeen", "Disability, dementia, and practical theology", ""),
]),
("Christian Ethics", [
 ("Karen Swallow Prior", "Author and literary scholar", "Ethics through literature and imagination", ""),
 ("Andy Crouch", "Praxis", "Culture making, power, and technology", ""),
 ("Matthew Lee Anderson", "Baylor University", "Bioethics and Christian moral reasoning", ""),
 ("Charles Camosy", "Creighton University", "Beginning and end of life; cross-tradition", ""),
 ("Jake Meador", "Mere Orthodoxy", "Political theology, work, and place", ""),
]),
("Leadership and Missiology", [
 ("Ed Stetzer", "Dean, Talbot School of Theology", "First call of all hundred, for reasons beyond the course", "talbot"),
 ("Tod Bolsinger", "Formerly Fuller Seminary", "Canoeing the Mountains; adaptive leadership", ""),
 ("Michael Goheen", "Missional theology", "The church's mission across the biblical story", ""),
 ("Todd Wilson", "Center for Pastor Theologians", "Pastor as theologian; ideal ally for the whole project", ""),
 ("Amy Sherman", "Sagamore Institute", "Vocational stewardship and church-based mission", ""),
]),
("Biblical Theology", [
 ("Patrick Schreiner", "Midwestern Seminary", "Kingdom, canon, and accessible biblical theology", ""),
 ("Matthew Emerson", "Oklahoma Baptist University", "Canon and creed together", ""),
 ("Chris Bruno", "Author, The Whole Story of the Bible", "Already writes exactly this course", ""),
 ("Jason DeRouchie", "Midwestern Seminary", "Old Testament in Christian Scripture", ""),
 ("Brandon Crowe", "Westminster Theological", "Gospels and biblical theology", ""),
]),
("Spiritual Formation", [
 ("Ruth Haley Barton", "Transforming Center", "Formation for leaders; deep church credibility", ""),
 ("John Mark Comer", "Practicing the Way", "Largest current audience in formation by a wide margin", ""),
 ("James Bryan Smith", "Friends University", "The Good and Beautiful series; built for small groups", ""),
 ("Rich Villodas", "New Life Fellowship", "Formation in an urban, multiethnic congregation", ""),
 ("Gary Moon", "Martin Institute, Dallas Willard Center", "Carries the Willard stream", ""),
]),
("Worship", [
 ("Constance Cherry", "Indiana Wesleyan", "The Worship Architect; the practical standard", ""),
 ("Glenn Packiam", "Rockharbor Church", "Pastor-scholar on worship and formation", ""),
 ("Zac Hicks", "Author, The Worship Pastor", "Written for the volunteer, not the academy", ""),
 ("Sandra Van Opstal", "Chasing Justice", "Multiethnic worship", ""),
 ("Bob Kauflin", "Sovereign Grace Music", "Congregational song and theology", ""),
]),
("Discipleship and Groups", [
 ("Jen Wilkin", "Author and Bible teacher", "Largest lay Bible-literacy platform in evangelicalism", ""),
 ("Greg Ogden", "Author, Transforming Discipleship", "The triad model; native to this thesis", ""),
 ("Bill Donahue", "Author, Leading Life-Changing Small Groups", "Willow-era group architecture", ""),
 ("Jim Putman", "Real Life Ministries", "Discipleship as a whole-church system", ""),
 ("Alan Hirsch", "Movement Leaders Collective", "Multiplication and movement theory", ""),
]),
("Evangelism", [
 ("Rico Tice", "Christianity Explored", "Built a global lay evangelism curriculum already", ""),
 ("Sam Chan", "City Bible Forum", "Evangelism in a secular age; genuinely funny on camera", ""),
 ("Elliot Clark", "Training Leaders International", "Witness under pressure and in exile", ""),
 ("Jerry Root", "Wheaton College", "Evangelism and Lewis", ""),
 ("Mack Stiles", "Author, Evangelism", "Ordinary, unforced personal witness", ""),
]),
("Marriage and Family", [
 ("Kara Powell", "Fuller Youth Institute", "Sticky Faith; the research base on teens and faith", ""),
 ("Gary Thomas", "Author, Sacred Marriage", "Marriage as formation rather than happiness", ""),
 ("Justin Whitmel Earley", "Author, Habits of the Household", "Family practice, currently the best-selling frame", ""),
 ("Chap Clark", "Author and researcher", "Adolescents and abandonment", ""),
 ("Scott Stanley", "University of Denver", "Marriage research; empirical credibility", ""),
]),
("Money, Work and Vocation", [
 ("Ron Blue", "Ron Blue Institute", "Your own client. The anchor for this entire discipline", "client"),
 ("Tom Nelson", "Made to Flourish", "Pastor-led theology of work across a church network", ""),
 ("Art Rainer", "Institute for Christian Financial Health", "Practical household finance for churches", ""),
 ("Greg Forster", "Oikonomia Network", "Theology of economics and vocation", ""),
 ("Chris Horst", "HOPE International", "Poverty, enterprise, and development", ""),
]),
("World Religions", [
 ("Harold Netland", "Trinity Evangelical", "Religious pluralism; the scholarly standard", ""),
 ("Gerald McDermott", "Anglican theologian", "World religions and Christian theology", ""),
 ("Ayman Ibrahim", "Southern Seminary", "Islam, taught fairly and firsthand", ""),
 ("Matthew Bennett", "Cedarville University", "Islam and Christian witness", ""),
 ("Miriam Adeney", "Seattle Pacific University", "Global Christianity and cross-cultural ministry", ""),
]),
("Christian Thought", [
 ("Alan Jacobs", "Baylor University", "Reading, attention, and the Christian intellectual life", ""),
 ("Jessica Hooten Wilson", "Pepperdine University", "Literature as formation; superb teacher", ""),
 ("James K. A. Smith", "Calvin University", "Desire, habit, and the modern self", ""),
 ("Craig Bartholomew", "Kirby Laing Centre", "Christian philosophy and the biblical worldview", ""),
 ("Holly Ordway", "Word on Fire Institute", "Imagination and apologetics; Catholic, so edition-scope it", ""),
]),
("Culture and Technology", [
 ("Felicia Wu Song", "Westmont College", "Restless Devices; digital life and the self", ""),
 ("Jason Thacker", "Boyce College and ERLC", "AI ethics from an evangelical frame", ""),
 ("Derek Schuurman", "Calvin University", "Computing and Christian faith; actual technical depth", ""),
 ("Tony Reinke", "Desiring God", "Smartphones, technology, and the soul", ""),
 ("Read Mercer Schuchardt", "Wheaton College", "Media ecology and attention", ""),
]),
]

EDITIONS = [
("Church Edition", "no", "Customized to that church's Pastor's Library",
 """The church's own sermon archive becomes the illustration and application layer. Their pastor
 introduces each session. Their doctrinal line is set where the course presents options. Their name
 is on the certificate. This edition is the most valuable one commercially and it is the one that
 must never carry a seminary's endorsement, because the moment a school blesses a product a pastor
 can edit, it has blessed five hundred things it cannot see. Do not ask for the blessing here. Do
 not accept it if offered."""),
("Network Edition", "denomination", "Positions set by the denomination, blessed by the denomination",
 """A denomination or network licenses the library, its own theologians settle the disputed pages,
 and the credential becomes theirs. The endorsement here is denominational rather than academic,
 which is the right currency: a Wesleyan pastor cares more that the Wesleyan network stands behind
 the material than that a seminary reviewed it. This is also where lay licensing recognition
 eventually comes from."""),
("Pathway Edition", "seminary", "Locked, unmodifiable, reviewed by the partner school",
 """A fixed subset of courses, frozen at the version the partner seminary reviewed, with no
 customization permitted at all. Same content, same faculty, same scripts. The only difference is
 that nobody can touch it. This is the only edition that carries a school's name, and it is
 deliberately the smallest of the three."""),
]

PCT = [
("Everyone exposed inside a licensed church", "100%",
 "Participants, in the sense that the material is available to them and most will encounter it in some group."),
("Start at least one full course", "25 to 40%",
 "Of adults in an engaged congregation, over a two-year window. Higher where the pastor makes it normative from the platform, materially lower where it is offered as an option among options."),
("Finish a course they start", "60 to 75%",
 "Small groups hold people far better than online courses do. Open online course completion sits in the single digits to low teens; a cohort meeting weekly with people who notice absence is a different animal entirely."),
("Want a certificate for it", "12 to 20%",
 "Of those who finish. The certificate matters to a specific temperament and to people in seasons of transition, and it is close to irrelevant to everyone else."),
("Pursue a multi-course credential", "3 to 5%",
 "Of finishers. This is the group that finishes twelve or twenty-four courses over years, and it is the real spine of the program's reputation."),
("Pursue accredited credit through a partner", "1 to 2%",
 "Of finishers. Small as a percentage and large as a number, and it is the entire pipeline argument you will make to a seminary."),
]

PROCESS = [
("Declaration", "The student enrolls in the Pathway Edition and knows from day one it is different",
 """Locked content, real deadlines, submitted work, and a named reviewer. The declaration matters
 psychologically as much as administratively. People behave differently when they have said out loud
 that they are going for it."""),
("Assessed work", "Written responses, one substantial paper per course, and a taught session",
 """The taught session is the differentiator and the thing a seminary cannot easily replicate at
 distance: the student teaches sixty minutes to a real group in their own church, filmed, and both
 the reviewer and the student's pastor evaluate it."""),
("Named reviewer", "A faculty member from the hundred, or a partner-school adjunct",
 """Compensated per portfolio, not per hour. The reviewer can and does return work as insufficient.
 This is the single line item that costs real money, and it applies to three to five percent of
 finishers rather than all of them, which is what makes it affordable."""),
("Portfolio", "The student's complete body of work, packaged to the partner's specification",
 """Not a transcript claim. The actual work: papers, the filmed teaching session, the pastor's
 evaluation, the reviewer's assessments. Prior learning assessment runs on evidence, not on
 assertion."""),
("Award by the partner", "Advanced standing or credit, granted by the accredited institution",
 """The degree is theirs and always was. You are the preparation and the evidence pipeline. That
 sentence, said early and repeated, is what turns an institutional threat into an institutional
 asset."""),
]


def build():
    h = io.StringIO(); W = h.write
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
header{background:var(--ink);color:#f3efe6;padding:72px 0 60px;position:relative;overflow:hidden}
header:before{content:"";position:absolute;inset:0;
background:radial-gradient(112% 78% at 7% 0%,rgba(193,154,75,.18),transparent 62%)}
header .wrap{position:relative}
header .eyebrow{color:var(--goldlt)}
header h1{font-size:clamp(35px,6.4vw,64px);line-height:1.0;color:#fbf8f1;margin-top:18px}
header h1 em{font-style:italic;font-weight:400;color:var(--goldlt)}
header .lede{font-size:22px;color:#cfc7b8;max-width:640px;margin-top:24px}
section{padding:62px 0 54px;border-bottom:1px solid var(--rule)}
section.dark{background:var(--ink2);color:#e6e0d3;border-bottom:none}
section.dark h2,section.dark h3,section.dark h4{color:#fbf8f1}
section.dark p{color:#d6cec0}
section.dark .kick{color:var(--mutedlt)}
section.tone{background:var(--parch2)}
h2.sec{font-size:clamp(27px,4.3vw,40px);line-height:1.09;margin-top:15px}
.kick{font-style:italic;color:var(--muted);margin:14px 0 0;max-width:640px;font-size:20px}
.pull{font-family:"Playfair Display",serif;font-size:23px;line-height:1.42;
border-left:3px solid var(--gold);padding-left:24px;margin:28px 0;max-width:660px}
section.dark .pull{color:var(--goldlt)}
.item{display:flex;gap:24px;padding:24px 0;border-top:1px solid var(--rule)}
section.dark .item{border-color:rgba(255,255,255,.13)}
.item .n{flex:0 0 46px;font-family:"Playfair Display",serif;font-size:30px;line-height:1;
color:transparent;-webkit-text-stroke:1px var(--gold);padding-top:3px}
section.dark .item .n{-webkit-text-stroke-color:var(--goldlt)}
.item .c{flex:1 1 auto;max-width:660px}
.item h4{font-size:20px;line-height:1.25;margin-bottom:8px}
.item p{margin:0 0 10px;font-size:18px}
.item p:last-child{margin-bottom:0}
.bless{font-family:"Lato",sans-serif;font-size:9.5px;font-weight:800;letter-spacing:.15em;
text-transform:uppercase;padding:4px 9px;display:inline-block;margin-bottom:9px}
.bless.no{border:1px solid var(--rule);color:var(--muted)}
.bless.denomination{border:1px solid var(--gold);color:var(--gold)}
.bless.seminary{background:var(--gold);color:#fff}
table{width:100%;border-collapse:collapse;margin-top:26px;font-size:17px}
th{font-family:"Lato",sans-serif;font-weight:800;font-size:10px;letter-spacing:.15em;
text-transform:uppercase;color:var(--gold);text-align:left;padding:0 14px 11px 0;
border-bottom:1px solid var(--rule);vertical-align:bottom}
td{padding:14px 14px 14px 0;border-bottom:1px solid var(--rule);vertical-align:top}
td.k{font-family:"Playfair Display",serif;font-size:18px;width:34%}
td.pc{font-family:"Lato",sans-serif;font-weight:700;font-size:16px;color:var(--gold);white-space:nowrap;width:16%}
td.s{color:var(--muted);font-size:16.5px}
.disc{padding:26px 0;border-top:1px solid var(--rule)}
.disc h3{font-size:20px;font-family:"Lato",sans-serif;font-weight:800;font-size:11px;
letter-spacing:.2em;text-transform:uppercase;color:var(--gold);margin-bottom:4px}
.fac{display:flex;gap:16px;padding:9px 0;border-bottom:1px solid rgba(217,207,188,.55);align-items:baseline}
.fac:last-child{border-bottom:none}
.fac .nm{flex:0 0 210px;font-family:"Playfair Display",serif;font-size:17.5px}
.fac .af{flex:0 0 190px;font-family:"Lato",sans-serif;font-size:11.5px;color:var(--muted);
letter-spacing:.04em;line-height:1.5}
.fac .wh{flex:1 1 auto;font-style:italic;color:var(--muted);font-size:16.5px}
.warm{font-family:"Lato",sans-serif;font-size:8.5px;font-weight:800;letter-spacing:.12em;
text-transform:uppercase;background:var(--gold);color:#fff;padding:2px 6px;margin-left:7px;
white-space:nowrap;vertical-align:middle}
@media(max-width:760px){.fac{flex-direction:column;gap:2px;padding:11px 0}
.fac .nm,.fac .af{flex:none}.item{gap:14px}.item .n{flex:0 0 32px;font-size:24px}}
.warnbox{border:1px solid var(--gold);padding:22px 24px;margin-top:26px;background:#fff}
.warnbox p{margin:0 0 10px;font-family:"Lato",sans-serif;font-size:13.5px;line-height:1.75;color:var(--body)}
.warnbox p:last-child{margin:0}
.warnbox b{color:var(--gold);letter-spacing:.1em;text-transform:uppercase;font-size:10px}
.note{font-family:"Lato",sans-serif;font-size:13px;line-height:1.75;color:var(--muted);
border-top:1px solid var(--rule);margin-top:32px;padding-top:16px;max-width:720px}
section.dark .note{color:var(--mutedlt);border-color:rgba(255,255,255,.15)}
.close{background:var(--ink);color:#efeae0;padding:70px 0;text-align:center}
.close h2{font-size:clamp(26px,4.3vw,40px);color:#fbf8f1}
.close p{max-width:620px;margin:20px auto 0;color:#c9c0b0}
footer{background:#070d15;color:#7d8b99;padding:26px 0;font-family:"Lato",sans-serif;
font-size:10.5px;letter-spacing:.1em;text-align:center;text-transform:uppercase}
@media(max-width:720px){body{font-size:18px}.wrap{padding:0 20px}section{padding:46px 0 40px}}
"""
    W("""<!DOCTYPE html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Editions, Certification, and the Hundred</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,700;1,400&family=Cormorant+Garamond:ital,wght@0,400;0,600;1,400&family=Lato:wght@300;400;700;800&display=swap" rel="stylesheet">
<style>""" + CSS + "</style></head><body>")

    W("""<header><div class="wrap">
<span class="eyebrow">Doing Seminary Together &nbsp;&middot;&nbsp; Architecture and Faculty</span>
<h1>Three editions,<br><em>one of them frozen</em></h1>
<p class="lede">Where the seminary blessing attaches, how many people actually want a credential,
what the certification path looks like, and a hundred names to build it with.</p>
</div></header>""")

    W("""<section><div class="wrap">
<span class="eyebrow">Compete or Coordinate</span>
<h2 class="sec">Customization and accreditation are opposites</h2>
<p class="kick">This is the whole answer to which edition gets blessed, and it falls out of one
constraint rather than a negotiation.</p>
<div style="margin-top:22px;max-width:700px">
<p>A seminary cannot endorse a product that a pastor is free to edit. The instant the church edition
pulls in that congregation's own sermon library, sets its own doctrinal positions, and adds its own
pastor's introductions, it has become five hundred different products, and no institution can put its
name on something it will never see. That is not institutional stubbornness. It is the correct
position and you should not ask them to take a different one.</p>
<p>So the blessing attaches to the version nobody can touch. Same content, same faculty, same
scripts, frozen at the reviewed version. It will be the smallest of the three editions by enrollment
and the most important of the three by reputation.</p>
</div>""")
    for i, (name, bless, tag, body) in enumerate(EDITIONS, 1):
        label = {"no": "No seminary endorsement, by design",
                 "denomination": "Blessed by the denomination",
                 "seminary": "Blessed by the seminary"}[bless]
        W('<div class="item"><span class="n">%d</span><div class="c">'
          '<span class="bless %s">%s</span><h4>%s</h4>'
          '<p style="font-style:italic;color:var(--muted);margin-bottom:9px">%s</p><p>%s</p></div></div>'
          % (i, bless, label, name, tag, " ".join(body.split())))
    W("""<div class="pull">You do both, and the answer to compete-or-coordinate is that you compete in
the church edition, coordinate in the pathway edition, and never let the two share a
certificate.</div>
</div></section>""")

    W("""<section class="dark"><div class="wrap">
<span class="eyebrow">Take Rate</span>
<h2 class="sec">What percentage actually want certification</h2>
<p class="kick">Estimates, not data. Reasoned from adjacent categories and clearly labeled as
guesses, because nobody has run this exact program at scale.</p>
<table style="color:#e6e0d3">
<tr><th>Stage</th><th>Estimate</th><th>Reasoning</th></tr>""")
    for k, pc, why in PCT:
        W('<tr><td class="k" style="color:#fbf8f1">%s</td><td class="pc" style="color:var(--goldlt)">%s</td>'
          '<td class="s" style="color:var(--mutedlt)">%s</td></tr>' % (k, pc, why))
    W("""</table>
<div class="pull">The low certification number is not a weakness in the model. It is the reason the
model works.</div>
<p>Run it through a real congregation. A church of two thousand adults, thirty percent of whom start
a course over two years, is six hundred students. Around four hundred finish. Sixty to eighty want a
certificate, which costs you a sheet of paper. Perhaps twenty pursue a multi-course credential.
Four to eight go after accredited credit through your partner.</p>
<p>Those last four to eight are the entire argument you make to a seminary, and it is a good one:
one church produced them, they did not exist before, and every one of them enrolls at your partner
school. Multiply by a hundred churches and you are the largest single feeder into that institution in
the country.</p>
<p class="note">The eighty-five percent who never want a credential are what make this a licensing
business rather than a tuition business. If most people wanted certification, you would need a
registrar, a reader corps, an appeals process, and everything else you deliberately declined to
build. Low take-rate is what keeps the cost structure a publisher's.</p>
</div></section>""")

    W("""<section class="tone"><div class="wrap">
<span class="eyebrow">The Process</span>
<h2 class="sec">What certification actually looks like, and who to do it with</h2>""")
    for i, (stage, tag, body) in enumerate(PROCESS, 1):
        W('<div class="item"><span class="n">%d</span><div class="c"><h4>%s</h4>'
          '<p style="font-style:italic;color:var(--muted);margin-bottom:9px">%s</p><p>%s</p></div></div>'
          % (i, stage, tag, " ".join(body.split())))
    W("""<h3 style="font-size:24px;margin-top:40px">Who to do it with, in order</h3>
<table>
<tr><th>Partner</th><th>Case for</th><th>Case against</th></tr>
<tr><td class="k">Talbot</td><td class="s">Talbot Embedded already exists and needs local ministry
contexts. Stetzer's mandate is expanding access. You are an alum, which is the single best door in
institutional life.</td><td class="s">A dean cannot get ahead of his faculty on credentialing. Slow,
and the framing has to be perfect.</td></tr>
<tr><td class="k">A competency-based accredited school</td><td class="s">Already built for portfolio
assessment and mentor teams. Will move faster and argue less, because you are describing what they
already do.</td><td class="s">Less brand weight with the churches you are selling to. Solves the
mechanics, not the credibility.</td></tr>
<tr><td class="k">Acquire a small accredited school</td><td class="s">Fastest route to owning the
credential outright. Schools in this position exist right now and some are actively seeking
partners.</td><td class="s">You would be buying an institution with an institution's costs, which is
the exact cost structure the whole model was designed to avoid.</td></tr>
</table>
<p class="note">Recommendation: pursue Talbot as the named partner and a competency-based school as
the fallback, and open both conversations in the same quarter. Do not open the acquisition
conversation until one of the first two has failed, because acquiring reverses the economics that
make this worth doing.</p>
</div></section>""")

    W("""<section><div class="wrap"><div class="narrow">
<span class="eyebrow">The Sending Model</span>
<h2 class="sec">On the Latter-day Saint comparison</h2>
<div style="margin-top:20px">
<p>The instinct is a good one and worth taking seriously rather than as a throwaway. It is also worth
knowing that the parallel is closer than you may realize: the Latter-day Saints already run a lay
seminary system, and it enrolls hundreds of thousands of teenagers in daily scripture study before
school. They did not build a program. They built an expectation.</p>
<p>Four mechanisms transfer cleanly. The first is that it is <em>normative rather than
elective</em> — not something offered among the options in the bulletin, but what people here do,
announced from the platform by the pastor as the church's ordinary path. That single decision moves
participation more than any marketing you could buy, and it is a pastor's decision, not
yours.</p>
<p>The second is that <em>everyone is expected to teach</em>. A structure with no paid local clergy
has to produce teachers or it collapses, which is precisely the condition your five hundred churches
are already in without admitting it. The third is <em>public commissioning</em>: named, in front of
the congregation, on a Sunday. The fourth is that finishing is an <em>assignment rather than a
graduation</em>. Not you have completed the coursework, but you now have a group, a class, or a
place to go.</p>
<div class="pull">A school ends with a diploma. A sending system ends with an
assignment.</div>
<p>What does not transfer is the part that makes theirs work: centralized authority, a correlated
curriculum, and structural obligation. Evangelical churches are congregational and voluntary. You
cannot mandate anything, and any attempt to will fail loudly. You can only make something normative,
which is slower, and depends entirely on whether the senior pastor will stand up and say this is what
we do here.</p>
<p>One practical caution. The comparison is genuinely illuminating internally and will land badly in
public materials with a fair number of pastors, for reasons that have nothing to do with the
mechanism. Use the mechanism. Do not use the name.</p>
</div></div></div></section>""")

    W("""<section class="tone"><div class="wrap">
<span class="eyebrow">The Hundred</span>
<h2 class="sec">Faculty and advisor prospects, five per discipline</h2>
<p class="kick">Selected for one criterion above all others: people who already teach the church and
not only the academy, because they are the ones who will say yes.</p>
<div class="warnbox">
<p><b>Read this before using the list</b></p>
<p>Nobody named here has been contacted, has agreed to anything, or has any association with this
project. This is a prospect list assembled from public work and public affiliation, and it should
never be presented to anyone as a faculty roster, an advisory board, or a list of participants.</p>
<p>Institutional affiliations shift constantly and some of these are certain to be out of date.
Verify every name, title, and institution before a single outreach email goes out. Confirm each
person is currently living and active; a prospect list of this length assembled from prior knowledge
will contain errors of that kind.</p>
<p>The list itself is a positioning decision, not a neutral inventory. It deliberately spans Reformed,
Wesleyan, Baptist, Anglican, and broadly evangelical scholarship, plus one Catholic voice, because
denominational editions are impossible without that breadth. That same breadth guarantees objections
from both flanks. Decide the theological perimeter before you recruit, not after.</p>
</div>""")
    for disc, people in FACULTY:
        W('<div class="disc"><h3>%s</h3>' % disc)
        for nm, af, wh, warm in people:
            badge = ""
            if warm == "prior":
                badge = '<span class="warm">Prior collaborator</span>'
            elif warm == "client":
                badge = '<span class="warm">Current client</span>'
            elif warm == "talbot":
                badge = '<span class="warm">Talbot</span>'
            W('<div class="fac"><span class="nm">%s%s</span><span class="af">%s</span>'
              '<span class="wh">%s</span></div>' % (nm, badge, af, wh))
        W('</div>')
    W("""<p class="note">Sequence the outreach by warmth rather than by prestige. Strauss and Wilkins
have already taught for you and should be the first two calls, not because they are the most famous
names on the page but because the second call is easier when the first one said yes. Ron Blue anchors
the stewardship discipline through an existing working relationship. The Talbot cluster gives you a
natural reason to be in front of Stetzer. Recruit those seven or eight first, then use their names to
open the next thirty, and expect the last twenty to be genuinely hard.</p>
</div></section>""")

    W("""<div class="close"><div class="wrap">
<h2>Compete in the church edition.<br>Coordinate in the pathway edition.</h2>
<p>Never let the two share a certificate, and recruit the first eight faculty from people who have
already said yes to you once.</p>
</div></div>
<footer><div class="wrap">LifeTogether Ministries &middot; Doing Seminary Together &middot; Editions,
certification, and faculty prospects &middot; August 2026</div></footer></body></html>""")
    return h.getvalue()


if __name__ == "__main__":
    out = build()
    p = "/mnt/user-data/outputs/doing-seminary-together-editions-and-faculty.html"
    open(p, "w", encoding="utf-8").write(out)
    n = sum(len(v) for _, v in FACULTY)
    print("bytes:", len(out), "| faculty:", n, "| disciplines:", len(FACULTY))
    print("div balance:", out.count("<div") - out.count("</div>"))
