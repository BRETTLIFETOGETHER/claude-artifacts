# -*- coding: utf-8 -*-

RULES = [
    ("01", "Short Declaratives",
     "Headlines run 3\u20136 words. Never a full explanatory sentence up top \u2014 the short line carries the weight."),
    ("02", "Threes and Parallels",
     "Lead statements repeat the same opening word or shape three times, building."),
    ("03", "The Repeating-Word Device",
     "Anchor each campaign's six weeks to one recurring word pulled from the campaign title itself."),
    ("04", "Verbs of Invitation",
     "Discover, align, clarify, refocus, flourish, belong, multiply. Never must, should, or need to."),
    ("05", "Name the Tension, Then the Hope",
     "One clause acknowledging the ache, then the turn. Don't linger in the problem."),
    ("06", "Second Person, Singular Focus",
     "Your church. Your life. Your calling. Never our or we."),
    ("07", "Plain, Accessible Faith Language",
     "God, Jesus, faith, purpose, calling, legacy, story. No theological jargon, no insider church-speak."),
    ("08", "No Exclamation Points, No Hard Sell",
     "Confidence reads as understated, not hyped."),
    ("09", "Body Copy, 20\u201335 Words",
     "Unhurried but efficient. Every sentence earns its place; no filler transitions."),
]

REACH_FOR = ["Discover", "Align", "Clarify", "Refocus", "Flourish", "Belong",
             "Multiply", "Calling", "Legacy", "Story", "Rooted", "Together"]
AVOID = ["Must / Should / Need to", "Exclamation points", "Theological jargon",
         "Insider church-speak", "\"Our\" / \"We\"", "Hype and hard sell"]

CSS = """
@page { size: 8.5in 11in; margin: 0; }
* { box-sizing: border-box; -webkit-font-smoothing: antialiased; }
html, body { margin: 0; padding: 0; }
body { font-family: 'TeX Gyre Heros', Helvetica, Arial, sans-serif; color: #1D1D1F; background: #FBFBFD; }
.page {
  width: 8.5in; height: 11in; position: relative; page-break-after: always;
  overflow: hidden; padding: 1.15in 1.05in; background: #FBFBFD;
}
.page:last-child { page-break-after: auto; }
.page.dark { background: #1D1D1F; color: #FBFBFD; }
.page-body { height: 100%; display: flex; flex-direction: column; justify-content: center; }

.eyebrow { font-size: 12px; letter-spacing: 3px; text-transform: uppercase; color: #8B1E3F; font-weight: 700; margin-bottom: 22px; }
.dark .eyebrow { color: #E3A6B8; }

h1 { font-weight: 700; margin: 0; letter-spacing: -0.5px; }
.headline { font-size: 54px; line-height: 1.08; color: #1D1D1F; max-width: 6.2in; }
.dark .headline { color: #FBFBFD; }
.subhead { font-size: 17px; font-weight: 400; color: #4A4A4E; line-height: 1.6; margin-top: 22px; max-width: 5.6in; }
.dark .subhead { color: #C7C7CC; }

.pagefoot { position: absolute; bottom: 0.6in; left: 1.05in; font-size: 10px; letter-spacing: 2px; text-transform: uppercase; color: #A1A1A6; }
.pagenum { position: absolute; bottom: 0.6in; right: 1.05in; font-size: 10px; color: #A1A1A6; letter-spacing: 1px; }
.dark .pagefoot, .dark .pagenum { color: #6E6E73; }

.cover .headline { font-size: 62px; }
.cover .taglines { margin-top: 36px; font-size: 18px; color: #4A4A4E; line-height: 1.9; }
.cover .footnote { position: absolute; bottom: 0.9in; left: 1.05in; font-size: 12px; color: #A1A1A6; letter-spacing: 1px; }

.rule-list { margin-top: 40px; }
.rule-row { display: flex; gap: 20px; padding: 20px 0; border-top: 1px solid #D2D2D7; }
.rule-row:last-child { border-bottom: 1px solid #D2D2D7; }
.rule-row .rnum { font-size: 13px; font-weight: 700; color: #8B1E3F; width: 26px; flex-shrink: 0; padding-top: 3px; }
.rule-row .rtitle { font-size: 16.5px; font-weight: 700; color: #1D1D1F; }
.rule-row .rdesc { font-size: 13px; color: #6E6E73; margin-top: 5px; max-width: 5.4in; line-height: 1.6; }

.word-cols { display: flex; gap: 60px; margin-top: 44px; }
.word-col h3 { font-size: 12px; letter-spacing: 2px; text-transform: uppercase; font-weight: 700; margin-bottom: 18px; }
.word-col.reach h3 { color: #E3A6B8; }
.word-col.avoid h3 { color: #6E6E73; }
.word-item { font-size: 15px; padding: 10px 0; border-top: 1px solid #3A3A3C; color: #FBFBFD; }
.word-col.avoid .word-item { color: #A1A1A6; }
"""

def rule_row(num, title, desc):
    return f'<div class="rule-row"><div class="rnum">{num}</div><div><div class="rtitle">{title}</div><div class="rdesc">{desc}</div></div></div>\n'

rules_p1 = "".join(rule_row(*r) for r in RULES[:5])
rules_p2 = "".join(rule_row(*r) for r in RULES[5:])
reach_items = "".join(f'<div class="word-item">{w}</div>' for w in REACH_FOR)
avoid_items = "".join(f'<div class="word-item">{w}</div>' for w in AVOID)

HTML = f"""<!DOCTYPE html>
<html>
<head><meta charset="utf-8"><style>{CSS}</style></head>
<body>

<!-- PAGE 1: COVER -->
<div class="page cover page-body">
  <div class="eyebrow">Brand Voice Guide</div>
  <h1 class="headline">Warm &amp;<br>Pastoral</h1>
  <div class="taglines">
    Helping churches go deeper.<br>
    Helping disciples grow stronger.<br>
    Helping every person discover a life that matters.
  </div>
  <div class="footnote">LifeTogether &middot; Voice &amp; Style</div>
</div>

<!-- PAGE 2: RULES 1-5 -->
<div class="page page-body">
  <div class="eyebrow">How We Sound</div>
  <h1 class="headline">Nine rules.<br>One voice.</h1>
  <div class="rule-list">
    {rules_p1}
  </div>
  <div class="pagefoot">LifeTogether</div>
  <div class="pagenum">02</div>
</div>

<!-- PAGE 3: RULES 6-9 -->
<div class="page page-body">
  <div class="eyebrow">How We Sound</div>
  <h1 class="headline">Continued.</h1>
  <div class="rule-list">
    {rules_p2}
  </div>
  <div class="pagefoot">LifeTogether</div>
  <div class="pagenum">03</div>
</div>

<!-- PAGE 4: WORDS (dark) -->
<div class="page page-body dark">
  <div class="eyebrow">The Vocabulary</div>
  <h1 class="headline">Words we<br>reach for.<br>Words we don't.</h1>
  <div class="word-cols">
    <div class="word-col reach">
      <h3>Reach For</h3>
      {reach_items}
    </div>
    <div class="word-col avoid">
      <h3>Avoid</h3>
      {avoid_items}
    </div>
  </div>
  <div class="pagefoot">LifeTogether</div>
  <div class="pagenum">04</div>
</div>

</body>
</html>
"""

with open("/home/claude/masterlib/voiceguide.html", "w") as f:
    f.write(HTML)

print("HTML written.")
