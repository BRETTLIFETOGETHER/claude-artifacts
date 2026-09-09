# -*- coding: utf-8 -*-
"""The narrated edition — synthetic narration, faculty review, and what it does to the economics."""
import io

CSS = """
:root{--ink:#0c1723;--ink2:#08111c;--gold:#c19a4b;--goldlt:#e2c689;--parch:#f7f3ea;
--parch2:#efe8da;--rule:#d9cfbc;--body:#2b2a26;--muted:#6d6759;--mutedlt:#9fb0c1;
--warn:#8c3b2e;}
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
header .lede{font-size:21px;color:#cfc7b8;max-width:630px;margin-top:22px}
section{padding:58px 0 50px;border-bottom:1px solid var(--rule)}
section.dark{background:var(--ink2);color:#e6e0d3;border-bottom:none}
section.dark h2,section.dark h3,section.dark h4{color:#fbf8f1}
section.dark p{color:#d6cec0}
section.tone{background:var(--parch2)}
h2.sec{font-size:clamp(26px,4.1vw,38px);line-height:1.1;margin-top:13px;max-width:780px}
.kick{font-style:italic;color:var(--muted);margin:13px 0 0;max-width:640px;font-size:20px}
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
.tier{border-top:1px solid var(--rule);padding:26px 0}
.tier-top{display:flex;align-items:baseline;gap:14px;flex-wrap:wrap;margin-bottom:8px}
.tier h3{font-size:24px}
.badge{font-family:"Lato",sans-serif;font-size:9px;font-weight:800;letter-spacing:.16em;
text-transform:uppercase;padding:4px 9px;white-space:nowrap}
.badge.one{border:1px solid var(--rule);color:var(--muted)}
.badge.two{border:1px solid var(--gold);color:var(--gold)}
.badge.three{background:var(--gold);color:#fff}
.tier .label{font-family:"Lato",sans-serif;font-size:12.5px;line-height:1.8;color:var(--muted);
border-left:2px solid var(--gold);padding-left:16px;margin:14px 0}
.rules{border:1px solid var(--warn);background:#fffaf8;padding:24px 26px;margin-top:26px}
.rules h4{color:var(--warn);font-family:"Lato",sans-serif;font-size:10px;font-weight:800;
letter-spacing:.2em;text-transform:uppercase;margin-bottom:14px}
.rules ol{margin:0;padding-left:20px}
.rules li{margin-bottom:12px;font-size:18px}
.rules li b{font-family:"Playfair Display",serif;font-weight:700}
table{width:100%;border-collapse:collapse;margin-top:24px;font-size:17px}
th{font-family:"Lato",sans-serif;font-weight:800;font-size:10px;letter-spacing:.15em;
text-transform:uppercase;color:var(--gold);text-align:left;padding:0 14px 11px 0;
border-bottom:1px solid var(--rule);vertical-align:bottom}
td{padding:13px 14px 13px 0;border-bottom:1px solid var(--rule);vertical-align:top}
td.k{font-family:"Playfair Display",serif;font-size:17.5px;width:30%}
td.n{font-family:"Lato",sans-serif;font-size:14px;white-space:nowrap;color:var(--gold);font-weight:700}
td.s{color:var(--muted);font-size:16.5px}
section.dark td{border-color:rgba(255,255,255,.13)}
section.dark td.k{color:#fbf8f1}section.dark td.s{color:var(--mutedlt)}
section.dark td.n{color:var(--goldlt)}
.note{font-family:"Lato",sans-serif;font-size:13px;line-height:1.75;color:var(--muted);
border-top:1px solid var(--rule);margin-top:30px;padding-top:15px;max-width:710px}
section.dark .note{color:var(--mutedlt);border-color:rgba(255,255,255,.15)}
.close{background:var(--ink);color:#efeae0;padding:66px 0;text-align:center}
.close h2{font-size:clamp(25px,4vw,38px);color:#fbf8f1}
.close p{max-width:600px;margin:18px auto 0;color:#c9c0b0}
footer{background:#070d15;color:#7d8b99;padding:24px 0;font-family:"Lato",sans-serif;
font-size:10.5px;letter-spacing:.1em;text-align:center;text-transform:uppercase}
@media(max-width:720px){body{font-size:18px}.wrap{padding:0 20px}section{padding:44px 0 38px}
.item{gap:13px}.item .n{flex:0 0 30px;font-size:22px}.rules{padding:20px 18px}}
"""

TIERS = [
("Narrated", "one", "AI-drafted, human-edited, faculty-reviewed, synthetic narration",
 """The catalog tier. A script generated from the course engine, edited by a writer, reviewed line by
 line by a credentialed scholar in that discipline, then rendered as audio by a synthetic voice with
 no name, no persona, and no face. This is what makes four hundred courses a real number instead of
 an aspiration.""",
 "Reviewed by [Name], [Institution]. Script AI-drafted and human-edited. Narrated by a synthetic voice."),
("Voiced", "two", "Same script, read by a human narrator",
 """Identical content, read by an actual person who is a narrator rather than a scholar. Costs a few
 hundred dollars more per course and removes the synthetic-voice objection entirely. The right tier
 for anything that will be scrutinised, and for every course a denomination puts its name on.""",
 "Reviewed by [Name], [Institution]. Script AI-drafted and human-edited. Read by [Narrator]."),
("Taught", "three", "The scholar teaches it, on film",
 """The flagship. The scholar who reviewed it also delivers it, and their face and credentials are on
 the screen. Expensive, slow, and the only tier that answers the question a pastor is actually asking
 when he asks who teaches this.""",
 "Written, reviewed and taught by [Name], [Institution]."),
]

RISKS = [
("Undisclosed synthesis would destroy everything else you have built",
 """Your entire strategic position is that you are the most transparent institution in the
 conversation. That is the argument that answers the integrity objection, opens the Talbot
 conversation, and makes the denominational sale. A synthetic voice discovered rather than disclosed
 does not damage one product. It retroactively makes every honest thing you have published look like
 marketing."""),
("The reviewer's name is the credential, so the reviewer must know exactly what they signed",
 """A scholar who reviews a script and later discovers their name appears beneath a synthetic voice
 they never heard will withdraw, and will say why. Consent has to be specific and in writing: which
 course, which tier, what the narration is, where their name appears, and their right to pull it. Get
 this wrong once with a well-known name and the faculty recruitment strategy is finished."""),
("Never clone a real scholar's voice",
 """The temptation arrives the moment you have filmed anyone, and it is a bright line. Synthesising
 Strauss or Wilkins reading a course they did not read is a different category of act from narrating
 an anonymous script, however carefully permission was obtained. Do not go near it."""),
("The heresy objection gets harder, not easier",
 """Machine-drafted content invites the sharpest version of the first objection, and the answer
 cannot be that the draft is fine. The answer has to be that the review is more rigorous than what
 most published curriculum receives, with a named reviewer, a published standard, and an attestation
 of what was checked. Build the review before you build the audio."""),
("Review that is fast enough to be cheap is not review",
 """The whole model turns on the reviewer actually reading it. The failure mode is obvious and
 predictable: a scholar with four courses and a deadline skims, signs, and the guardrail becomes
 decorative. Pay per course rather than per set, require line comments rather than an approval, and
 audit a sample against a second reader."""),
]


def build():
    h = io.StringIO(); W = h.write
    W("""<!DOCTYPE html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>The Narrated Edition</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,700;1,400&family=Cormorant+Garamond:ital,wght@0,400;0,600;1,400&family=Lato:wght@300;400;700;800&display=swap" rel="stylesheet">
<style>""" + CSS + "</style></head><body>")

    W("""<header><div class="wrap">
<span class="eyebrow">Doing Seminary Together &nbsp;&middot;&nbsp; Production Model</span>
<h1>The narrated edition,<br><em>and the line you cannot cross</em></h1>
<p class="lede">Synthetic narration with faculty review turns four hundred courses from a
six-million-dollar aspiration into a one-point-seven-million-dollar build. It also puts your entire
credibility strategy on a single disclosure decision.</p>
</div></header>""")

    W("""<section><div class="wrap"><div style="max-width:700px">
<span class="eyebrow">The Verdict</span>
<h2 class="sec">Yes, and it changes the economics more than anything else discussed this month</h2>
<div class="verdict">But it is not an audio professor. It is a narrated course with a named reviewer,
and the difference between those two phrases is the entire project.</div>
<p style="margin-top:22px">The instinct is right and it solves the problem I flagged as the eighteen
month gap: between deciding to recruit a hundred faculty and having anything filmed, you currently
have nothing to sell. Narration closes that gap in weeks rather than years, and it does something
better than that &mdash; it inverts the order of operations. Instead of recruiting a scholar and then
hoping they produce, you produce first and ask them to correct. Which is exactly the model you
already landed on for faculty, applied one layer deeper.</p>
<p>It also makes error cheap to fix. When a reviewer catches something in a filmed lecture, the fix
is a reshoot and a scheduling negotiation. When a reviewer catches something in a narrated course,
the fix is an edit and a re-render, and it ships the same afternoon. Over four hundred courses that
difference is not a convenience, it is the difference between a catalog that can be corrected and one
that calcifies.</p>
<p>And audio is the right medium for this audience regardless of cost. A small group leader
preparing on a commute is a real behaviour. Video is what a church buys; audio is what a person
actually finishes.</p>
<p>The outline layer you asked about already exists, incidentally. The course engine now generates a
twelve-lesson build sheet for every one of the four hundred, classified into six pedagogical
archetypes. The next layer up is the script, and that is where this decision applies.</p>
</div></div></section>""")

    W("""<section class="tone"><div class="wrap">
<span class="eyebrow">Who Is Teaching</span>
<h2 class="sec">Three tiers, disclosed on every course</h2>
<p class="kick">The same script can ship at any of the three. What changes is who speaks it and what
the label says.</p>""")
    for name, cls, tag, body, label in TIERS:
        W('<div class="tier"><div class="tier-top"><h3>%s</h3><span class="badge %s">Tier %s</span></div>'
          '<p style="font-style:italic;color:var(--muted);margin-bottom:10px">%s</p><p>%s</p>'
          '<div class="label"><b>Label that appears on the course page, the audio player, and the '
          'printed workbook:</b><br>%s</div></div>'
          % (name, cls, {"one":"one","two":"two","three":"three"}[cls], tag,
             " ".join(body.split()), label))
    W("""<div class="verdict">Tier One is the catalog. Tier Three is the proof. You ship four hundred
narrated courses so the shelf is full, and twenty taught courses so nobody doubts the enterprise
&mdash; the twenty are what you show, the four hundred are what you sell.</div>
</div></section>""")

    W("""<section class="dark"><div class="wrap">
<span class="eyebrow">Economics</span>
<h2 class="sec">What it does to the build number</h2>
<table style="color:#e6e0d3">
<tr><th>Per course</th><th>Taught tier</th><th>Narrated tier</th><th>Note</th></tr>
<tr><td class="k">Script</td><td class="n">$3,000&ndash;5,000</td><td class="n">$1,200</td><td class="s">Engine draft plus a human editorial pass, not a blank page</td></tr>
<tr><td class="k">Faculty</td><td class="n">$2,000&ndash;4,000</td><td class="n">$1,500</td><td class="s">Review only. Priced per course rather than per set, deliberately</td></tr>
<tr><td class="k">Recording</td><td class="n">$4,000&ndash;7,000</td><td class="n">$400</td><td class="s">Synthesis and audio production against a filming day and a crew</td></tr>
<tr><td class="k">Workbook and design</td><td class="n">$2,000&ndash;3,000</td><td class="n">$600</td><td class="s">Template-driven once the four editions exist</td></tr>
<tr><td class="k">Total</td><td class="n">~$15,000</td><td class="n">~$3,700</td><td class="s">Roughly a quarter</td></tr>
</table>
<table style="color:#e6e0d3;margin-top:34px">
<tr><th>Catalog</th><th>All taught</th><th>Blended</th><th>What blended means</th></tr>
<tr><td class="k">400 courses</td><td class="n">~$6,000,000</td><td class="n">~$1,700,000</td><td class="s">380 narrated at $3,700 plus 20 taught flagships at $15,000</td></tr>
<tr><td class="k">Year One row</td><td class="n">~$300,000</td><td class="n">~$110,000</td><td class="s">The twenty 101 courses, if six stay taught and fourteen are narrated</td></tr>
<tr><td class="k">Six-course pilot</td><td class="n">~$90,000</td><td class="n">~$40,000</td><td class="s">Two taught, four narrated. Inside a single funder's gift</td></tr>
</table>
<p class="note">The constraint moves rather than disappearing. Production stops being the bottleneck
and review becomes it: four hundred courses at eight to twelve hours of careful scholarly reading is
somewhere near four thousand hours of credentialed faculty time. That is the number to plan around
now, and it is why the faculty list matters more under this model rather than less.</p>
</div></section>""")

    W("""<section><div class="wrap">
<span class="eyebrow">Non-Negotiables</span>
<h2 class="sec">The disclosure rules</h2>
<p class="kick">These are not preferences. Any one of them broken takes the whole strategy with
it.</p>
<div class="rules"><h4>Five rules, no exceptions</h4><ol>
<li><b>No name, no persona, no face, ever.</b> The voice is a narrator, not a professor. It gets no
biography, no portrait, no honorific, and no invented institution. The moment it becomes a character,
you have fabricated a credential rather than narrated a course.</li>
<li><b>Retire the phrase audio professor.</b> Fine as internal shorthand, fatal in public. The
professor is the reviewer, whose name is real and printed. The audio is narration. Say it that way
internally too, because language drifts toward the shortcut.</li>
<li><b>Label every course in three places</b> &mdash; the course page, the audio player, and the
printed workbook &mdash; naming the reviewer and their institution and stating plainly that the
script was AI-drafted and human-edited and the narration is synthetic.</li>
<li><b>Written, specific reviewer consent.</b> Which course, which tier, what the narration is, where
their name appears, and an unconditional right to withdraw it. A general agreement to review is not
consent to this.</li>
<li><b>Never synthesise a real person's voice.</b> Not with permission, not for convenience, not
once.</li>
</ol></div>
<p class="note">Worth one call with counsel before launch, particularly if any of this travels
internationally: several jurisdictions have moved toward transparency obligations for synthetic
media, and the requirements are not uniform. In the United States and for a church audience this is
overwhelmingly a trust question rather than a legal one, but the two stop being separable the moment
a denomination puts its name on an edition.</p>
</div></section>""")

    W("""<section class="tone"><div class="wrap">
<span class="eyebrow">Risks</span>
<h2 class="sec">Five things that could go wrong</h2>""")
    for i, (name, body) in enumerate(RISKS, 1):
        W('<div class="item"><span class="n">%d</span><div class="c"><h4>%s</h4><p>%s</p></div></div>'
          % (i, name, " ".join(body.split())))
    W("""<div class="verdict">Handled well, this is the move that makes the catalog real. Handled
carelessly, it is the one decision in the whole plan capable of ending it.</div>
<p class="note">One reframe worth carrying into the objection conversation. Under this model the
honest claim gets stronger, not weaker: every course in the catalog has been read line by line by a
credentialed scholar who signed an attestation. Almost no church curriculum published today can say
that, including a great deal of it that was written by humans and reviewed by nobody.</p>
</div></section>""")

    W("""<div class="close"><div class="wrap">
<h2>The professor is the reviewer.<br>The audio is narration. Say it that way.</h2>
<p>Four hundred narrated courses at roughly a quarter the cost, twenty taught flagships as the proof,
and a disclosure label on every one of them.</p>
</div></div>
<footer><div class="wrap">LifeTogether Ministries &middot; Doing Seminary Together &middot; Narrated
edition production model &middot; August 2026</div></footer></body></html>""")
    return h.getvalue()


if __name__ == "__main__":
    out = build()
    p = "/mnt/user-data/outputs/doing-seminary-together-narrated-edition.html"
    open(p, "w", encoding="utf-8").write(out)
    print("bytes:", len(out), "| div:", out.count("<div") - out.count("</div>"),
          "| sections:", out.count("<section"), out.count("</section>"))
