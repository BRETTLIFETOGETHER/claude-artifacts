import sys, html
sys.path.insert(0, "/home/claude")
from data1 import D1
from data2 import D2

DISC = D1 + D2
TIERS = [
    ("100", "Foundations", "Read and discuss. Open to anyone at a table."),
    ("200", "Core", "Written response each week, mentor reviewed."),
    ("300", "Advanced", "Research paper per course, oral review."),
    ("400", "Capstone and Teaching", "You build it, teach it, and are assessed on it."),
]

def e(s):
    return html.escape(s, quote=False)

total = sum(len(d[3]) + len(d[4]) + len(d[5]) + len(d[6]) for d in DISC)

CSS = """
:root{
  --navy:#101a33; --navy-2:#16223f; --navy-3:#1d2c4f;
  --gold:#b8934e; --gold-lt:#d9bc82; --cream:#f7f3ea;
  --line:rgba(217,188,130,.22);
}
*{box-sizing:border-box}
html{scroll-behavior:smooth}
body{
  margin:0; background:var(--navy); color:var(--cream);
  font-family:'Cormorant Garamond',Georgia,serif; font-size:19px; line-height:1.62;
  -webkit-font-smoothing:antialiased;
}
.wrap{max-width:1080px;margin:0 auto;padding:0 26px}
h1,h2,h3,h4{font-family:'Playfair Display',Georgia,serif;font-weight:600;line-height:1.16;margin:0}
.eyebrow{
  font-family:'Lato',system-ui,sans-serif;font-size:11px;letter-spacing:.22em;
  text-transform:uppercase;color:var(--gold-lt);opacity:.85;font-weight:700
}
.lead{font-size:22px;color:rgba(247,243,234,.86)}
p{margin:0 0 16px}
.muted{color:rgba(247,243,234,.72)}
.dim{color:rgba(247,243,234,.60)}
a{color:var(--gold-lt)}

/* hero */
header.hero{
  padding:74px 0 56px;border-bottom:1px solid var(--line);
  background:
    radial-gradient(1100px 420px at 12% -10%,rgba(184,147,78,.20),transparent 62%),
    linear-gradient(180deg,#0c1428,var(--navy));
}
.hero h1{font-size:clamp(42px,7vw,78px);letter-spacing:-.02em;margin:14px 0 6px}
.hero .dom{font-family:'Lato',sans-serif;font-size:12px;letter-spacing:.28em;text-transform:uppercase;color:var(--gold);opacity:.9}
.hero .thesis{max-width:660px;margin-top:22px;font-size:23px;color:rgba(247,243,234,.88)}
.rule{height:1px;background:var(--line);margin:0}
.stats{display:flex;flex-wrap:wrap;gap:40px;margin-top:38px}
.stat .n{font-family:'Playfair Display',serif;font-size:40px;color:var(--gold-lt);line-height:1}
.stat .l{font-family:'Lato',sans-serif;font-size:10.5px;letter-spacing:.16em;text-transform:uppercase;color:rgba(247,243,234,.6);margin-top:7px}

section{padding:62px 0;border-bottom:1px solid var(--line)}
section h2{font-size:clamp(28px,4vw,40px);margin:12px 0 18px}
section h3{font-size:23px;margin:30px 0 10px;color:var(--gold-lt)}

/* verdict */
.verdict{
  border-left:3px solid var(--gold);background:rgba(184,147,78,.08);
  padding:22px 26px;margin:22px 0 0
}
.verdict strong{color:var(--gold-lt)}

/* doors */
.doors{display:grid;gap:14px;margin-top:26px}
.door{
  display:grid;grid-template-columns:52px 1fr;gap:20px;align-items:start;
  border:1px solid var(--line);background:rgba(255,255,255,.022);padding:20px 22px
}
.door .num{font-family:'Playfair Display',serif;font-size:30px;color:var(--gold);opacity:.75;line-height:1}
.door h4{font-size:20px;margin-bottom:5px}
.door .tag{font-family:'Lato',sans-serif;font-size:10px;letter-spacing:.14em;text-transform:uppercase;padding:3px 9px;border:1px solid var(--line);color:var(--gold-lt);margin-left:10px;white-space:nowrap}

/* ladder: the signature element */
.ladder{margin-top:34px;border-top:1px solid var(--line)}
.rung{
  display:grid;grid-template-columns:66px 1fr 210px;gap:22px;align-items:start;
  padding:24px 0;border-bottom:1px solid var(--line);position:relative
}
.rung .step{
  font-family:'Lato',sans-serif;font-size:10px;letter-spacing:.16em;text-transform:uppercase;
  color:var(--gold);padding-top:6px
}
.rung h4{font-size:24px}
.rung .req{font-family:'Lato',sans-serif;font-size:12.5px;line-height:1.75;color:rgba(247,243,234,.66)}
.rung .bar{position:absolute;left:0;bottom:-1px;height:2px;background:var(--gold);opacity:.55}
.rung .who{font-family:'Lato',sans-serif;font-size:11px;letter-spacing:.1em;text-transform:uppercase;color:var(--gold-lt);opacity:.8;margin-top:8px}

/* table */
table{width:100%;border-collapse:collapse;margin-top:24px;font-size:16px}
th,td{text-align:left;padding:13px 14px;border-bottom:1px solid var(--line);vertical-align:top}
th{font-family:'Lato',sans-serif;font-size:10.5px;letter-spacing:.14em;text-transform:uppercase;color:var(--gold-lt);font-weight:700}
td.k{font-family:'Lato',sans-serif;font-size:13px;color:var(--gold-lt);white-space:nowrap}

/* modes */
.modes{display:grid;grid-template-columns:repeat(auto-fit,minmax(224px,1fr));gap:14px;margin-top:26px}
.mode{border:1px solid var(--line);padding:20px;background:rgba(255,255,255,.022)}
.mode .size{font-family:'Lato',sans-serif;font-size:10px;letter-spacing:.16em;text-transform:uppercase;color:var(--gold)}
.mode h4{font-size:19px;margin:8px 0 7px}
.mode p{font-size:16px;margin:0;color:rgba(247,243,234,.72)}

/* catalog */
.discipline{border:1px solid var(--line);margin-top:22px;background:rgba(255,255,255,.02)}
.dhead{display:grid;grid-template-columns:74px 1fr;gap:18px;padding:22px 24px 18px;border-bottom:1px solid var(--line);align-items:start}
.dhead .dn{font-family:'Playfair Display',serif;font-size:40px;color:var(--gold);opacity:.62;line-height:.9}
.dhead h3{margin:0;color:var(--cream);font-size:26px}
.dhead .sub{font-size:17px;color:rgba(247,243,234,.66);margin-top:4px}
.tier{padding:18px 24px 6px;border-bottom:1px solid rgba(217,188,130,.10)}
.tier:last-child{border-bottom:none}
.tierhead{display:flex;align-items:baseline;gap:12px;flex-wrap:wrap;margin-bottom:10px}
.tierhead .lvl{font-family:'Playfair Display',serif;font-size:15px;color:var(--gold)}
.tierhead .nm{font-family:'Lato',sans-serif;font-size:10.5px;letter-spacing:.16em;text-transform:uppercase;color:var(--gold-lt)}
.tierhead .rig{font-family:'Lato',sans-serif;font-size:11px;color:rgba(247,243,234,.5)}
ol.courses{margin:0 0 12px;padding-left:26px}
ol.courses li{margin-bottom:7px}
ol.courses .t{color:var(--cream)}
ol.courses .s{color:rgba(247,243,234,.6);font-size:16.5px}

.note{border:1px dashed var(--line);padding:18px 20px;margin-top:26px;font-size:17px;color:rgba(247,243,234,.75)}
.note b{color:var(--gold-lt)}
ul.tight{margin:0 0 16px;padding-left:22px}
ul.tight li{margin-bottom:8px}
footer{padding:52px 0 66px;text-align:center}
footer .f1{font-family:'Lato',sans-serif;font-size:11px;letter-spacing:.2em;text-transform:uppercase;color:rgba(247,243,234,.5)}
@media(max-width:720px){
  body{font-size:18px}
  .rung{grid-template-columns:1fr;gap:8px}
  .rung .step{padding-top:0}
  .door{grid-template-columns:1fr;gap:8px}
  .dhead{grid-template-columns:1fr;gap:6px}
  table{font-size:15px}
  th,td{padding:10px 8px}
}
@media(prefers-reduced-motion:reduce){html{scroll-behavior:auto}}
"""


def hero():
    return f"""
<header class="hero"><div class="wrap">
  <div class="eyebrow">LifeTogether &middot; Feasibility Study and Curriculum Map</div>
  <h1>Small Group<br>Seminary</h1>
  <div class="dom">smallgroupseminary.com</div>
  <p class="thesis">Seminary-depth theological training, delivered at a table in a local church,
  with real coursework, real supervision, and a credential that means something.
  Not a shortcut. A longer road, walked in company.</p>
  <div class="stats">
    <div class="stat"><div class="n">20</div><div class="l">Disciplines</div></div>
    <div class="stat"><div class="n">{total}</div><div class="l">Courses</div></div>
    <div class="stat"><div class="n">5</div><div class="l">Credential rungs</div></div>
    <div class="stat"><div class="n">4</div><div class="l">Rigor levels</div></div>
    <div class="stat"><div class="n">5</div><div class="l">Delivery modes</div></div>
  </div>
</div></header>"""


def verdict():
    return """
<section><div class="wrap">
  <div class="eyebrow">The Question</div>
  <h2>Is this plausible, and can it scale?</h2>
  <p>Yes on both, with one hard boundary. The idea is not speculative, because a
  church-based, competency-based theological school already exists and is accredited: the
  Antioch School of Church Planting and Leadership Development, the credentialing arm of
  BILD International. It is accredited by the Distance Education Accrediting Commission,
  a federally recognized agency, and it grants ministry credentials from certificate
  through doctorate to students who do their work inside a local church under local
  mentors. Students enroll either through a partner church or as individuals whose church
  commits to mentoring them. That is a working proof that your instinct is not naive.</p>

  <div class="verdict">
    <p><strong>The boundary:</strong> you can build the curriculum, the cohorts, the homework,
    the supervision, and the certificate immediately, with nobody's permission. What you cannot
    do without an accredited institution is grant a degree, or call the thing a degree, or imply
    one. That single line determines the entire architecture below. Everything else is design.</p>
    <p style="margin:0"><strong>The trade you already named:</strong> drop the biblical languages
    and the credential stops being an M.Div. Extend the timeline and the volume of work, and it
    can honestly approach M.Div depth in every other respect. Say that out loud in the marketing
    rather than hiding it, and the product becomes more credible, not less.</p>
  </div>
</div></section>"""


def doors():
    rows = [
        ("1", "Church-issued certificate", "Available now",
         "Your nonprofit issues it, the local church signs it, the transcript is yours. No approval "
         "needed from anyone. Zero portability into higher education, which is fine for the large "
         "majority of laypeople who will never enroll in a degree program."),
        ("2", "Third-party credit recommendation", "12 to 24 months",
         "The American Council on Education evaluates individual courses through its Learning "
         "Evaluations program and recommends a specific number of credit hours at a specific level. "
         "This is how Sophia and StraighterLine make non-accredited coursework transferable at "
         "hundreds of institutions without themselves being schools. It is the single highest-leverage "
         "move available to you, because it converts a certificate into currency without changing "
         "what you are."),
        ("3", "Articulation agreements", "Rolling, one school at a time",
         "A written agreement with a specific seminary or Bible college specifying exactly which of "
         "your courses count for what credit in their program. Negotiated individually, and easiest "
         "with schools that already want adult and non-traditional students. With 500 church "
         "relationships you have unusual leverage here, because you bring them enrollment."),
        ("4", "Partner-institution degree", "12 to 36 months to structure",
         "The Antioch School model, inverted for your benefit. An already accredited school grants "
         "the degree; your church network delivers the formation and the supervision. The student "
         "gets a real M.Min or M.A. in Ministry. You get to stay a publisher and a platform instead "
         "of becoming a university."),
        ("5", "Your own accreditation", "Five to eight years, do not start here",
         "Institutional accreditation requires governance separation, credentialed faculty, financial "
         "audits, library resources, student services, and a multi-year self-study and site visit. "
         "It is a legitimate destination and a terrible starting point. Revisit it only after doors "
         "two through four have proven the demand."),
    ]
    out = ['<section><div class="wrap"><div class="eyebrow">Credentialing</div>',
           "<h2>Five doors, and only one of them is closed to you today</h2>",
           '<p class="muted">These are not alternatives to choose between. They are a sequence. '
           'Ship through door one, pursue door two in parallel, and use doors three and four to '
           'give your strongest students somewhere to go.</p>',
           '<div class="doors">']
    for n, t, tag, body in rows:
        out.append(f'<div class="door"><div class="num">{n}</div><div>'
                   f'<h4>{e(t)}<span class="tag">{e(tag)}</span></h4>'
                   f'<p class="muted" style="margin:0">{e(body)}</p></div></div>')
    out.append("</div></div></section>")
    return "\n".join(out)


def ladder():
    rungs = [
        ("Rung 1", "Certificate of Completion", "Any layperson, any table",
         "5 courses in one discipline &middot; Level 100 &middot; Rigor L1<br>"
         "Attendance and participation &middot; no written work required<br>"
         "About 10 months at one course per two months<br>"
         "Signed by the pastor, issued by the church", 20),
        ("Rung 2", "Certificate in Biblical Studies", "The serious lay student",
         "15 courses &middot; Old Testament, New Testament, Hermeneutics &middot; Rigor L2<br>"
         "500-word written response per session, mentor graded to rubric<br>"
         "About 2.5 years &middot; one Certified Mentor required<br>"
         "Transcript with hours and rubric scores", 38),
        ("Rung 3", "Diploma in Ministry", "Lay pastors, elders, staff without training",
         "30 courses across 10 disciplines &middot; Rigor L2 with two L3 disciplines<br>"
         "Supervised ministry practicum, 150 logged hours<br>"
         "Oral review before a three-person panel &middot; about 4 years<br>"
         "This is the tier most Bible college certificates actually match", 60),
        ("Rung 4", "Fellowship of the Small Group Seminary", "The M.Div-shaped tier, honestly labeled",
         "60 courses across all 20 disciplines &middot; Rigor L3<br>"
         "Research paper per course &middot; capstone project &middot; 2 years supervised ministry<br>"
         "Pastor attestation of character and fruit &middot; 6 to 9 years part-time<br>"
         "Comparable to an M.Div in seat time and written volume, minus languages and academic research method", 84),
        ("Rung 5", "Degree Bridge", "Granted by the partner school, not by you",
         "Fellowship transcript submitted for block credit<br>"
         "Residual coursework, languages, and thesis completed with the partner<br>"
         "Degree conferred: M.Min, M.A. in Ministry, or M.Div<br>"
         "Your name appears as the training partner, never as the grantor", 100),
    ]
    out = ['<section><div class="wrap"><div class="eyebrow">The Signature Structure</div>',
           "<h2>The credential ladder</h2>",
           '<p class="muted">One library of courses. Five places to stop. A person can enter at a '
           'Tuesday night table with no ambition beyond understanding Genesis, and the same system '
           'will carry them, if they want it, to a degree granted by an accredited school. Nobody '
           'has to commit to the top to start at the bottom.</p>',
           '<div class="ladder">']
    for step, name, who, req, pct in rungs:
        out.append(f'<div class="rung"><div class="step">{e(step)}</div>'
                   f'<div><h4>{e(name)}</h4><div class="who">{e(who)}</div></div>'
                   f'<div class="req">{req}</div>'
                   f'<div class="bar" style="width:{pct}%"></div></div>')
    out.append("</div>")
    out.append('<div class="note"><b>Read the timeline as a feature.</b> You said you would accept '
               'a longer road in exchange for dropping the languages. Here is the actual arithmetic: '
               'one eight-week course every two months puts the Fellowship at roughly nine years, and '
               'two concurrent courses puts it at four and a half. A traditional M.Div is three to four '
               'years full-time and unavailable to almost everyone who would enroll in this. The honest '
               'pitch is not faster. It is reachable.</div>')
    out.append("</div></section>")
    return "\n".join(out)


def rigor():
    rows = [
        ("L1", "Read and Discuss", "None", "Attendance and participation",
         "Table leader", "Certificate of Completion"),
        ("L2", "Write and Respond", "500 words per session", "Rubric score by a Certified Mentor",
         "Certified Mentor", "Certificate in Biblical Studies, Diploma"),
        ("L3", "Research and Defend", "2,500-word paper per course", "Paid reader plus oral review",
         "Reader Pool", "Fellowship"),
        ("L4", "Teach and Supervise", "Teach the material to a live group", "Recorded session assessed against a teaching rubric",
         "Supervisor", "Certified Mentor and Table Leader credentials"),
    ]
    out = ['<section><div class="wrap"><div class="eyebrow">The Scaling Mechanism</div>',
           "<h2>One content library, four rigor overlays</h2>",
           '<p class="muted">This is the part that makes the whole thing buildable. You do not write '
           'four curricula for four credential levels. You write one course and attach four assessment '
           'overlays to it. A retired welder and a future church planter sit at the same table, read '
           'the same material, and earn different credentials because they elected different rigor. '
           'It is the same create-once, configure-many-ways architecture already running underneath '
           'the publishing platform.</p>',
           "<table><thead><tr><th>Level</th><th>Mode</th><th>Weekly output</th>"
           "<th>How it is assessed</th><th>Who assesses</th><th>Unlocks</th></tr></thead><tbody>"]
    for a, b, c, d, f, g in rows:
        out.append(f"<tr><td class='k'>{e(a)}</td><td>{e(b)}</td><td>{e(c)}</td>"
                   f"<td>{e(d)}</td><td>{e(f)}</td><td>{e(g)}</td></tr>")
    out.append("</tbody></table>")
    out.append('<div class="note"><b>The real constraint is not content. It is grading.</b> '
               'Four hundred courses is a fixed cost, and producing large libraries is already what '
               'you do. Assessment is a marginal cost that rises with every student, and it is the '
               'thing that quietly kills programs like this. Three defenses: keep L1 entirely '
               'peer-and-leader assessed with no central grading; use rubric-driven structured peer '
               'review plus a mentor sign-off at L2; and pay readers only at L3 and L4, where students '
               'are few and tuition can carry the cost. Price the tiers so that grading is funded by '
               'the tier that requires it.</div>')
    out.append("</div></section>")
    return "\n".join(out)


def modes():
    ms = [
        ("3 to 12", "The Table", "The default. Weekly, ninety minutes, one Certified Table Leader, discussion-driven. Everything is written for this room first."),
        ("2", "The Pair", "Paul and Timothy. Fastest progress and highest accountability. Ideal for a pastor training an intern or two elders working through doctrine together."),
        ("1", "Solo with Mentor", "Self-paced with a monthly mentor call. For rural churches, shift workers, and anyone without a cohort within driving distance."),
        ("15 to 40", "The Class", "A church-wide cohort taught by staff on a semester rhythm. This is the on-ramp that fills the tables."),
        ("Cross-church", "The Network Cohort", "Online, mixed-church, denominationally sponsored. Where the platform economics get interesting and where a partner school will want to plug in."),
    ]
    out = ['<section><div class="wrap"><div class="eyebrow">Delivery</div>',
           "<h2>The same course, five rooms</h2>",
           '<p class="muted">You asked whether this could run in a small group, in pairs, individually, '
           'or in cohorts. All four, plus a fifth. The content is authored once for the table, and each '
           'other mode is a facilitation variant of it rather than a separate product.</p>',
           '<div class="modes">']
    for size, name, body in ms:
        out.append(f'<div class="mode"><div class="size">{e(size)}</div>'
                   f'<h4>{e(name)}</h4><p>{e(body)}</p></div>')
    out.append("</div></div></section>")
    return "\n".join(out)


def languages():
    return """
<section><div class="wrap">
  <div class="eyebrow">The Hardest Design Decision</div>
  <h2>What to do about Greek and Hebrew</h2>
  <p class="muted">Languages are the single clearest line between a seminary degree and everything
  below it. Three honest options, and a recommendation.</p>

  <h3>Option A &middot; Drop them and say so</h3>
  <p class="muted">Call it an English-Bible ministry track, plainly, in the marketing. This is what
  most non-M.Div tracks at Bible colleges functionally are. The cost is that no serious school will
  treat the credential as M.Div equivalent, and no honest person should claim it is.</p>

  <h3>Option B &middot; Languages as an optional elective spine</h3>
  <p class="muted">Two years of tutored, self-paced Greek and Hebrew, gated by a proctored exam,
  required only for the top rung. Realistic completion rates for self-paced language study without
  daily class accountability are low, so plan for most students to skip it, and design the credential
  so that skipping it is not a failure.</p>

  <h3>Option C &middot; Language literacy as a required discipline</h3>
  <p class="muted">A required twenty-course discipline that teaches students to use the fruits of the
  languages responsibly: lexicons without the word fallacies, interlinears for their actual purpose,
  translation comparison, discourse structure visible in English, and a unit on what you may never
  claim without the languages. It produces students who know the boundary of their own competence,
  which is more than many language-trained graduates can say.</p>

  <div class="verdict"><p style="margin:0"><strong>Recommendation: C as required, B as optional,
  and A as the honest label.</strong> Discipline 12 in the catalog below is built this way. It is
  also, incidentally, the most defensible and most distinctive thing in the entire curriculum, because
  no seminary teaches a student the shape of their own limits.</p></div>
</div></section>"""


def benchmark():
    return """
<section><div class="wrap">
  <div class="eyebrow">Curriculum Validation</div>
  <h2>How to prove the map is right</h2>
  <p class="muted">The twenty disciplines below are built to the standard shape of an accredited
  Master of Divinity: biblical studies, exegetical method, theology, church history, practical
  theology, spiritual formation, and supervised field work, typically distributed across roughly
  seventy-two to ninety graduate credit hours. That shape is well established and the map reflects
  it. What has <em>not</em> been done is a line-by-line audit against real syllabi, and that is the
  next discrete piece of work rather than something to assume.</p>

  <h3>The audit set, seminary side</h3>
  <p class="muted">Dallas, Gordon-Conwell, Trinity Evangelical, Southern, Southeastern, Reformed
  Theological, Westminster, Fuller, Talbot, and Denver. Add Beeson, Covenant, and Phoenix if you
  want a thirteen-school spread across traditions.</p>

  <h3>The audit set, Bible college and certificate side</h3>
  <p class="muted">Moody, Columbia International, Multnomah, Lancaster Bible, Grace, Cedarville
  graduate studies, Liberty, and Johnson. These matter more than the seminaries for your purpose,
  because their non-M.Div tracks are the credential shape you are actually competing with, and their
  registrars are the ones most likely to sign an articulation agreement.</p>

  <div class="note"><b>What the audit produces:</b> a matrix of every required course at all
  twenty-one schools, mapped against these twenty disciplines, showing coverage gaps, over-built
  areas, and the exact courses a partner school would need to see before granting block credit.
  That document is what you put in front of a registrar. It is a bounded, deliverable piece of
  research and it should happen before any of these courses are written.</div>
</div></section>"""


def caution():
    return """
<section><div class="wrap">
  <div class="eyebrow">Before You Buy the Domain Signage</div>
  <h2>Two cautions worth paying a lawyer about</h2>
  <ul class="tight muted">
    <li><b style="color:var(--gold-lt)">The words themselves are regulated.</b> Many states restrict
    who may use terms like seminary, college, and degree, and who may issue anything that implies a
    degree. Religious exemptions exist in a good number of states, but they vary widely in scope and
    several require registration or an affidavit. Which state your entity registers in materially
    changes what you may print on a certificate. This is a specific question for education counsel
    in your state, not something to resolve from a template.</li>
    <li><b style="color:var(--gold-lt)">Keep the grantor and the trainer separate from day one.</b>
    Structure it so the certificate is issued by your institute and any degree flows only through the
    accredited partner. That separation protects the brand if a state regulator ever asks, and it
    makes door four dramatically easier to negotiate, because the partner school is not being asked
    to share its degree-granting authority, only to recognize your coursework.</li>
  </ul>
  <p class="muted" style="margin-top:18px">Neither of these is a reason not to build it. Both are
  reasons to have the conversation before the first certificate is printed rather than after.</p>
</div></section>"""


def catalog():
    out = ['<section><div class="wrap"><div class="eyebrow">The Curriculum</div>',
           f"<h2>20 disciplines &middot; {total} courses</h2>",
           '<p class="muted">Your original ten disciplines, each expanded from ten courses to twenty '
           'and restructured into four ascending levels, plus ten new disciplines built to the same '
           'shape. Every course is eight sessions. The level determines the depth of the content; the '
           'rigor overlay determines the depth of the work. A credential is a path through this '
           'library, not a separate product.</p>',
           '<div class="note" style="margin-bottom:6px"><b>One thing to correct.</b> The names of your '
           'original ten disciplines were not in front of me, so disciplines 01 through 10 are the '
           'standard ten reconstructed from the M.Div distribution. Send me your actual ten and I will '
           're-map without losing any of the four hundred courses.</div>']
    for num, name, sub, t1, t2, t3, t4 in DISC:
        out.append('<div class="discipline">')
        out.append(f'<div class="dhead"><div class="dn">{num}</div><div>'
                   f"<h3>{e(name)}</h3><div class='sub'>{e(sub)}</div></div></div>")
        for (lvl, tname, rig), courses in zip(TIERS, [t1, t2, t3, t4]):
            out.append('<div class="tier">')
            out.append(f'<div class="tierhead"><span class="lvl">{lvl}</span>'
                       f'<span class="nm">{e(tname)}</span>'
                       f'<span class="rig">{e(rig)}</span></div>')
            out.append('<ol class="courses">')
            for t, s in courses:
                out.append(f'<li><span class="t">{e(t)}</span> '
                           f'<span class="s">&mdash; {e(s)}</span></li>')
            out.append("</ol></div>")
        out.append("</div>")
    out.append("</div></section>")
    return "\n".join(out)


def nextmoves():
    return """
<section><div class="wrap">
  <div class="eyebrow">If You Want to Move</div>
  <h2>The first four things, in order</h2>
  <ul class="tight muted">
    <li><b style="color:var(--gold-lt)">Run the syllabus audit.</b> Twenty-one schools mapped against
    these twenty disciplines. It validates or corrects everything above and it is the document a
    registrar needs. Nothing should be written before it.</li>
    <li><b style="color:var(--gold-lt)">Build one discipline all the way down.</b> Not a sampler.
    Discipline 03, Hermeneutics, all twenty courses, all four rigor overlays, one complete rubric set,
    one Certified Mentor guide. If that one discipline works in three pilot churches, the other
    nineteen are a production problem you already know how to solve.</li>
    <li><b style="color:var(--gold-lt)">Open a conversation about door four now.</b> A school that
    already serves non-traditional adults, already grants an M.Min, and already wants enrollment. You
    bring five hundred churches. That is a real offer and it takes twelve to thirty-six months, so it
    should start while the curriculum is being built, not after.</li>
    <li><b style="color:var(--gold-lt)">Design the Certified Mentor credential before the student
    credential.</b> The program lives or dies on whether there are enough qualified people to assess
    the work. Mentors are made at level L4 by graduates of the program, which means the first cohort
    has to be mentored by outside seminary graduates and pastors. Recruit them first.</li>
  </ul>
</div></section>"""


HTML = f"""<!DOCTYPE html>
<html lang="en"><head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Small Group Seminary &middot; Feasibility and Curriculum Map</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@500;600;700&family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;1,400&family=Lato:wght@400;700;900&display=swap" rel="stylesheet">
<style>{CSS}</style>
</head><body>
{hero()}
{verdict()}
{doors()}
{ladder()}
{rigor()}
{modes()}
{languages()}
{benchmark()}
{caution()}
{catalog()}
{nextmoves()}
<footer><div class="wrap">
  <div class="f1">LifeTogether &middot; Small Group Seminary &middot; 20 Disciplines &middot; {total} Courses</div>
</div></footer>
</body></html>"""

with open("/mnt/user-data/outputs/small-group-seminary.html", "w", encoding="utf-8") as f:
    f.write(HTML)

print("courses:", total)
print("disciplines:", len(DISC))
counts = [len(d[3]) + len(d[4]) + len(d[5]) + len(d[6]) for d in DISC]
print("per-discipline:", set(counts))
import os
print("bytes:", os.path.getsize("/mnt/user-data/outputs/small-group-seminary.html"))
