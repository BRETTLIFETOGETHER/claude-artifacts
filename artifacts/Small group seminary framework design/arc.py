# -*- coding: utf-8 -*-
"""Insert the five-movement opening argument after the cover."""

SRC = "/mnt/user-data/outputs/smallgroupseminary-framework-and-catalog.html"
s = open(SRC, encoding="utf-8").read()

CSS = """
/* ---------- the five movements ---------- */
.arc{background:var(--parch);padding:0;border-bottom:1px solid var(--rule)}
.arc-open{padding:70px 0 8px;text-align:center}
.arc-open h2{font-size:clamp(29px,4.6vw,42px);line-height:1.08;margin-top:16px}
.arc-open p{max-width:560px;margin:16px auto 0;font-style:italic;color:var(--muted);font-size:20px}
.mv{padding:52px 0;border-top:1px solid var(--rule)}
.mv:first-of-type{border-top:none}
.mv.dark{background:var(--ink-2);color:#e6e0d3}
.mv.dark h3{color:#fbf8f1}
.mv.dark .mv-num{color:var(--gold-lt);-webkit-text-stroke-color:var(--gold-lt)}
.mv.dark .mv-label{color:var(--gold-lt)}
.mv-inner{display:flex;gap:40px;align-items:flex-start;max-width:1000px;margin:0 auto;padding:0 30px}
.mv-rail{flex:0 0 108px;position:relative;padding-top:4px}
.mv-num{font-family:"Playfair Display",serif;font-size:74px;line-height:.8;color:transparent;
 -webkit-text-stroke:1px var(--gold);display:block}
.mv-label{font-family:"Lato",sans-serif;font-weight:800;font-size:9.5px;letter-spacing:.24em;
 text-transform:uppercase;color:var(--gold);margin-top:14px;display:block}
.mv-body{flex:1 1 auto;max-width:640px}
.mv-body h3{font-size:clamp(24px,3.6vw,33px);line-height:1.14;margin-bottom:20px}
.mv-body p{margin:0 0 16px;font-size:19px}
.mv-body p:last-child{margin-bottom:0}
.mv-body .turn{font-family:"Playfair Display",serif;font-size:22px;line-height:1.4;
 border-left:3px solid var(--gold);padding-left:20px;margin:24px 0}
.mv.dark .mv-body .turn{color:var(--gold-lt)}
@media(max-width:760px){
 .mv-inner{flex-direction:column;gap:14px;padding:0 20px}
 .mv-rail{flex:none;display:flex;align-items:baseline;gap:16px;padding-top:0}
 .mv-num{font-size:48px}.mv-label{margin-top:0}
 .mv-body{max-width:none}
}
"""

MOVEMENTS = [
 ("I", "The Problem", "dark",
  "The church has run a two-tier system for four hundred years",
  ["""Ask a pastor how many people in his congregation are genuinely equipped to teach the Bible, and
watch what happens to his face. He will name three, maybe five, in a church of eight hundred. He is
not being uncharitable. He is describing a real shortage, and that shortage quietly determines what
his church can and cannot attempt.""",
   """Look at who is actually carrying the teaching load in an ordinary congregation. A woman who has
taught the same class for eleven years and has never once been taught how to read a passage in its
context. An elder who signed a doctrinal statement he could not defend if a college student pushed
on it. A group leader who gets asked, on a Tuesday night, why God allowed a miscarriage, and has
nothing to reach for but instinct and kindness. None of these people are lazy or incurious. They
were never trained, because the only place to get trained asks for an undergraduate degree, a
relocation, three years, and a bill most of them will never be positioned to pay.""",
   """So the church runs two tiers. There are the few who went and the many who did not, and what
separates them is not hunger or capacity. It is access. The cost of that gap never shows up on a
Sunday morning, when the trained person is in the pulpit. It shows up on the days he is not in the
room, in a hospital corridor, in a text message from a son who has stopped believing, in a marriage
ending quietly while three people who love that couple stand around wishing they knew what to
say.""",
   """<span class="turn">Doctrine that was never examined fails at exactly the moment it is needed.
That is the problem, and it is not a problem of ignorance. The church has never had more content
available to it. Formation is what got locked inside an institution most of the church cannot
enter.</span>"""]),

 ("II", "The Solution", "",
  "Stop sending people to the school. Put the school where the people already are.",
  ["""The instinctive fix is to make seminary cheaper or shorter, and many good institutions have
tried. Tuition comes down, a program moves online, a certificate gets bolted to the bottom of the
degree. It helps at the margins and never touches the actual barrier, because the barrier was never
only money or time. It is that a church has to send a person away in order to have them trained, and
the people who most need the training are precisely the ones who cannot go.""",
   """Turn it around. Do not move the student to the school. Move the school into the room the student
is already sitting in on a Tuesday night.""",
   """That room is not a concession. It may be the better classroom. Twelve people around a table,
meeting weekly for twelve weeks, reading the same book, answerable to each other, walking out
afterward into the exact lives the material is meant to address. A seminary would call that a cohort
with an integrated ministry practicum and price it accordingly. The church calls it a small group
and gives it away.""",
   """What has been missing from that room is not honesty or commitment. What has been missing is
content with a spine. Most small group material is written to be finishable, which is a real virtue,
and it has trained a generation to expect six weeks and a video. Put a genuine course in the same
room, twelve sessions with real reading and real work, taught by someone worth listening to, and it
turns out that people rise to it. That is the whole solution, and it is nearly embarrassing in its
simplicity: seminary-grade content, delivered through the small group, paced for an adult with a job
and children."""]),

 ("III", "The Breakthrough", "dark",
  "The delivery system was finished before anyone realized it was a school",
  ["""Here is the part that makes this buildable rather than merely desirable.""",
   """An institution that wanted to teach four hundred courses in the format just described would have
to construct nearly all of it from nothing. It would need local sites, a trained facilitator in each
one, a weekly rhythm churches would actually keep, participant materials, teaching scripts, and
relationships with enough congregations to make the effort worth it. That build takes decades, which
is why nobody has done it. Institutions are good at faculty and poor at neighborhoods.""",
   """That system already exists. It was assembled over twenty-five years, across five hundred
churches, for entirely unrelated reasons. The twelve-week cohort, the trained volunteer leader, the
participant workbook, the leader guide, the teaching script, the discussion arc, the campaign that
lines the pulpit up with the living room. Every one of those pieces was built to serve small group
ministry. None of them were built to be a school. Together they are one anyway.""",
   """The faculty problem, which is the other thing that makes a seminary expensive, has already been
solved here once. Deepening Life Together put real seminary faculty in front of ordinary small
groups, teaching books of the Bible, biblical characters, and the parables. Members who could never
have gotten into those classrooms sat under those teachers in a living room, and it worked. The
proof of concept is years old and sitting on a shelf.""",
   """<span class="turn">So the breakthrough is not a technology and not an idea. It is a recognition.
The slow, unglamorous half of building a seminary, the distribution and the rhythm and the trained
leaders and the trust of five hundred churches, was finished years ago by people who believed they
were doing something else entirely.</span>"""]),

 ("IV", "The Reformation", "",
  "The Reformation handed the church a Bible. It never handed over the training.",
  ["""The word is heavy and should not be thrown around, so here is the specific claim, which is
narrower than it first sounds.""",
   """The Reformation's great educational act was to put Scripture into the language of ordinary
people and to insist that ordinary people were competent to read it. Tyndale wanted a plowboy to
know more of the Bible than a priest did. Luther wrote a catechism small enough for a father to
teach his own household, which tells you the Reformers took lay training seriously and were not
content to leave it to the clergy.""",
   """Then something happened across the following four centuries that nobody intended. The text
stayed in the hands of the people. The training migrated. Theological education professionalized,
moved into the academy, attached itself to degrees and credit hours and admissions requirements, and
became the property of the vocationally called. The plowboy kept his Bible. He never received the
tools to handle it, and after a few generations it stopped occurring to anyone that he should.""",
   """The arrangement we have inherited is a strange one. Every member owns a Bible, most own three
translations and a study app, and almost none have been taught how the book works, where a doctrine
comes from, or how to tell a sound teaching from a merely plausible one. Access without competence.
That is not what the Reformers were after.""",
   """<span class="turn">Finishing that sentence is the claim, and it is a reformation of access
rather than of doctrine. Nothing here revises what the church confesses. The courses teach the
historic positions fairly and leave the line where it belongs, with the local church. The conviction
the Reformers applied to the text is simply applied now to the training that makes the text
usable.</span>"""]),

 ("V", "The Revolution", "dark",
  "A school graduates a class. A reproduction system doubles.",
  ["""Suppose it works. Suppose a hundred thousand ordinary members across a few thousand churches
finish real coursework over the next decade. What actually changes?""",
   """The first thing is who can teach. A congregation's teaching capacity is capped by the number of
trained people inside it, which for most churches is a handful. Release that constraint and the
pastor is no longer the only theological resource in the building. Classes multiply because there
are people qualified to lead them. Groups go deeper because leaders have stopped improvising. The
bottleneck that has shaped what churches are willing to attempt for a century simply moves.""",
   """The second is where doubt gets met. Deconstruction rarely begins with an argument nobody could
answer. It begins with a question somebody was embarrassed to ask, in a church where no one seemed
equipped to take it seriously. A congregation full of members who have worked through hard texts and
disputed doctrines and the problem of evil is a congregation where that question gets asked out
loud, early, over coffee, by someone who is not frightened of it.""",
   """The third is where this goes once it leaves. A course of study that needs no campus, no
relocation, no undergraduate prerequisite, and no biblical languages is a course of study that
travels. The fastest-growing parts of the global church are outrunning every accredited institution
trying to train their leaders, and they are not waiting for permission. Church-based and
cohort-delivered is the only shape of theological education that can move at the speed the church is
actually growing.""",
   """Underneath all three sits the mechanism that makes this a movement rather than a program. Paul
told Timothy to entrust what he had learned to reliable people who would themselves be qualified to
teach others, which is four generations inside a single sentence. That sentence is the design
specification. Every course ends with the student teaching. Every credential requires that somebody
else finished because of you.""",
   """<span class="turn">A school measures how many it graduated. This measures how many its
graduates trained. A thing that reproduces does not add. It doubles.</span>"""]),
]

arc = ['<section class="arc"><div class="wrap arc-open">',
       '<span class="eyebrow">The Case</span>',
       '<h2>Five hundred churches already meet on Tuesday night.<br>Nobody ever put a seminary in the room.</h2>',
       '<p>The argument in five movements, before any of the architecture.</p></div>']

for num, label, tone, head, paras in MOVEMENTS:
    arc.append('<div class="mv %s"><div class="mv-inner">' % tone)
    arc.append('<div class="mv-rail"><span class="mv-num">%s</span>'
               '<span class="mv-label">%s</span></div>' % (num, label))
    arc.append('<div class="mv-body"><h3>%s</h3>' % head)
    for p in paras:
        arc.append("<p>%s</p>" % " ".join(p.split()))
    arc.append('</div></div></div>')
arc.append("</section>")
ARC = "\n".join(arc)

# insert directly after the cover header, before the honest-answer section
anchor = "</div></header>"
i = s.index(anchor) + len(anchor)
s = s[:i] + "\n" + ARC + s[i:]

# the honest-answer section now follows the case, so re-label its eyebrow
s = s.replace('<span class="eyebrow">The Honest Answer First</span>',
              '<span class="eyebrow">Before the Architecture, the Reality Check</span>')

s = s.replace("</style>", CSS + "\n</style>", 1)

open(SRC, "w", encoding="utf-8").write(s)
print("movements inserted:", s.count('class="mv '))
print("turn callouts:", s.count('class="turn"'))
print("bytes:", len(s))
words = sum(len(" ".join(p.split()).split()) for _, _, _, _, ps in MOVEMENTS for p in ps)
print("prose words:", words)
