PAGES = []
def add(html): PAGES.append(html)

def folio(chapter, num):
    return f'''<div class="folio"><div class="thread">{chapter}</div><div>{num:02d}</div></div>'''

def compact_module(n, group, name, purpose, how, tip):
    return f'''
    <div class="mod-card">
      <div class="mod-n">{n}</div>
      <div class="mod-group">{group}</div>
      <div class="mod-name">{name}</div>
      <div class="mod-purpose">{purpose}</div>
      <div class="mod-how"><span class="mod-label">How to use it</span>{how}</div>
      <div class="mod-tip"><span class="mod-label">Tip</span>{tip}</div>
    </div>'''

def full_module_page(eyebrow, n, name, purpose, steps, tip, num):
    step_html = "".join([f'<div class="pb-step"><div class="pb-step-n">{i+1}</div><div>{s}</div></div>' for i, s in enumerate(steps)])
    return f'''
<div class="page">
  <div class="frame">
    <div class="eyebrow">LIVE MODULE {n} &mdash; {eyebrow}</div>
    <div style="height:0.16in;"></div>
    <h1 class="display" style="font-size:20pt; color:var(--navy);">{name}</h1>
    <div style="height:0.1in;"></div>
    <p class="lede" style="font-size:10.3pt;">{purpose}</p>
    <div style="height:0.18in;"></div>
    <div class="pb-steps">{step_html}</div>
    <div style="height:0.16in;"></div>
    <div class="takeaway"><span class="label">Tip</span>{tip}</div>
  </div>
  {folio(name, num)}
</div>
'''

# =================================================================
# PAGE 1 — COVER
# =================================================================
add(f'''
<div class="page navy">
  <div class="frame" style="display:flex; flex-direction:column; justify-content:flex-end;">
    <div style="font-family:'Archivo'; font-weight:600; font-size:9pt; letter-spacing:0.22em; color:#D9B876; margin-bottom:2.2in;">HOW TO USE EVERY MODULE</div>
    <h1 class="display" style="font-size:27pt; color:#FBF8F1;">The Family Stewardship Playbook</h1>
    <div style="height:0.14in;"></div>
    <div style="font-family:'Playfair'; font-style:italic; font-weight:600; font-size:13.5pt; color:#D9B876;">Nineteen modules. What each one is for, and how to actually run it.</div>
    <div style="height:0.24in;"></div>
    <p class="lede" style="font-size:10.3pt; color:rgba(251,248,241,0.8); max-width:5.6in;">
      Thirteen foundational modules from the original specification, plus six built out
      since &mdash; Retention, Relational Bonds, AUM Growth, the Successor &amp; Steward
      Journey, Family Business, and Stories.
    </p>
  </div>
</div>
''')

# =================================================================
# PAGE 2 — HOW TO USE THIS PLAYBOOK
# =================================================================
add(f'''
<div class="page">
  <div class="frame">
    <div class="eyebrow">HOW TO USE THIS PLAYBOOK</div>
    <div style="height:0.2in;"></div>
    <h1 class="display" style="font-size:20pt; color:var(--navy);">Start with the six that are already live.</h1>
    <div style="height:0.16in;"></div>
    <p class="lede">
      This playbook covers all nineteen modules, but they&rsquo;re not all built the same way
      yet. The final six &mdash; Retention, Relational Bonds, AUM Growth, the Successor &amp;
      Steward Journey, Family Business, and Stories &mdash; exist today as a working,
      interactive prototype. The first thirteen are fully specified with example prompts,
      ready to build next.
    </p>
    <div style="height:0.2in;"></div>
    <div class="takeaway"><span class="label">The original thirteen</span>Sources &middot; Family Map &middot; Finder &middot; Coaching &middot; Scripts &middot; Builders &middot; Habits &middot; Toolbox &middot; Library Builder &middot; Calendar &middot; Cohort &middot; Library &middot; Publish</div>
    <div style="height:0.14in;"></div>
    <div class="takeaway"><span class="label">Built and live today</span>Retention &middot; Relational Bonds &middot; AUM Growth &middot; Successor &amp; Steward Journey &middot; Family Business &middot; Stories</div>
  </div>
  {folio("How to Use This Playbook", 2)}
</div>
''')

# =================================================================
# PAGES 3-9 — ORIGINAL 13 MODULES, COMPACT, 2 PER PAGE
# =================================================================
orig_modules = [
    ("INPUT", "Sources", "Upload existing PDFs, Word documents, dictated notes, emails, spreadsheets, or past chats.",
     "Drop a document in, review the extracted profile draft, and confirm or correct anything flagged as ambiguous before it's saved.",
     "Never let it silently overwrite a fact &mdash; always show what changed and let the family confirm."),
    ("DISCOVERY", "Family Map", "Aggregates individual assessments into one shared, comparable family or couples view.",
     "Run individual assessments first, then generate the Map to see alignment and divergence, not just separate scores.",
     "Describe patterns, never rank family members against each other."),
    ("DISCOVERY", "Finder", "Recommends exactly one best next step, instead of an overwhelming menu.",
     "Ask Finder after any milestone &mdash; a completed course, a Family Map update &mdash; not just at the start of the relationship.",
     "One recommendation, with a one-line reason, beats a list every time."),
    ("GUIDANCE", "Coaching", "Role-based coaching &mdash; what a lawyer, CPA, wealth manager, or family office professional would likely raise.",
     "Use before a real meeting with that professional, to prepare better questions, not to replace the meeting.",
     "Every output should end with 'ask your [professional] about this' &mdash; never advice given directly."),
    ("GUIDANCE", "Scripts", "Word-for-word conversation scripts, tailored by relationship &mdash; advisor, parent, child, grandchild.",
     "Specify who's speaking and to whom before generating &mdash; the same conversation reads differently by relationship.",
     "Include a graceful exit line for when the other person isn't ready to continue."),
    ("BUILDING", "Builders", "Guided document-builders &mdash; Purpose, Life Message, Family Values, Succession, Relationship, Marriage.",
     "Ask one question at a time, wait for the answer, and draft the final document in the person's own words.",
     "A personal, single-person edition exists for every Builder, not just the couple/family version."),
    ("BUILDING", "Habits", "Turns a stated goal into one small, sustainable habit, not a giant program.",
     "Start with a habit small enough to be nearly impossible to fail at, then build from there.",
     "Anchor new habits to something that already happens regularly."),
    ("BUILDING", "Toolbox", "A menu of specific skill-building tools mapped to a desired outcome.",
     "Start from the outcome the family wants, not a list of available tools.",
     "Every tool should point toward a deeper course or curriculum for anyone who wants to go further."),
    ("PLANNING", "Library Builder", "Compiles everything completed into one running Growth Plan.",
     "Regenerate it after any major milestone so it stays current, not just built once.",
     "Keep it to a few pages &mdash; use the family's own words wherever they already exist."),
    ("PLANNING", "Calendar", "Sequences the Growth Plan into a realistic twelve-month plan.",
     "Build it around the family's actual stated capacity, not an ideal pace.",
     "No more than one major commitment per month."),
    ("COMMUNITY", "Cohort", "Helps a family build a small group around this content with friends or extended family.",
     "Generate an invitation and a first discussion question together, not just a generic invite.",
     "Suggest a realistic group size and meeting cadence up front."),
    ("CONTENT", "Library", "Full-catalog search across roughly 15,000 items, by topic, theme, or outcome.",
     "Search by the outcome the family actually wants, not just a keyword.",
     "Translate a family's own words into the underlying theme before searching."),
    ("OUTPUT", "Publish", "Turns any output into a finished, branded deliverable &mdash; PDF, PowerPoint, brochure, template, print-ready, or InDesign file.",
     "Choose the format based on how it will actually be used &mdash; a slide deck for a family meeting, a PDF for a keepsake.",
     "Always carry over the family's chosen branding automatically."),
]

i = 0
page_num = 3
while i < len(orig_modules):
    pair = orig_modules[i:i+2]
    cards = "".join([compact_module(i+j+1, g, n, p, h, t) for j, (g, n, p, h, t) in enumerate(pair)])
    add(f'''
    <div class="page">
      <div class="frame">
        <div class="eyebrow">THE ORIGINAL THIRTEEN</div>
        <div style="height:0.14in;"></div>
        {cards}
      </div>
      {folio("The Original Thirteen", page_num)}
    </div>
    ''')
    page_num += 1
    i += 2

# =================================================================
# NEW MODULE PAGES — FULL TREATMENT (LIVE PROTOTYPE)
# =================================================================
add(full_module_page(
    "RETENTION", 14, "Milestone Tracker & the Next-Gen Bridge Journey",
    "Tracks the exact moments most likely to trigger a switch, and builds the relationship with the next generation years before any wealth transfers.",
    [
        "Add every known milestone &mdash; births, marriages, business sales, retirements &mdash; as they become known, not just at year-end review.",
        "Check the suggested outreach action for each milestone type before it happens, not after.",
        "Move the Next-Gen Bridge Journey forward one stage at a time &mdash; Introduce, Include, Educate, Involve, Transition &mdash; never skip to Transition.",
    ],
    "The single highest-leverage stage is Introduce. Most failed generational transfers trace back to an heir who was never introduced at all.",
    page_num
))
page_num += 1

add(full_module_page(
    "RELATIONAL BONDS", 15, "Family Meeting Facilitator & Multi-Generational Calendar",
    "Gives the advisor tools and planners to become part of the family's actual rhythm, not just its quarterly reviews.",
    [
        "Pick the meeting type that matches what's actually happening &mdash; an annual meeting needs different questions than a values conversation.",
        "Use the generated agenda as a starting point, not a script to read verbatim.",
        "Add birthdays, anniversaries, and milestones to the calendar as they come up in conversation, not from a static import.",
    ],
    "The calendar's value isn't the dates themselves &mdash; it's the reminder to reach out about something that isn't a financial event.",
    page_num
))
page_num += 1

add(full_module_page(
    "AUM GROWTH", 16, "Complete Financial Picture & Business Exit Readiness",
    "Explicitly permission-based &mdash; helps the family see their whole financial picture. Never framed as prospecting.",
    [
        "Walk through each asset category with the family present, marking each as managed here, held elsewhere, or unknown.",
        "Only discuss a 'held elsewhere' asset further with the family's explicit invitation to do so.",
        "Use the Exit Readiness scorecard well before a sale is imminent &mdash; readiness work takes years, not months.",
    ],
    "A low Exit Readiness score isn't a problem to fix today &mdash; it's the reason to start the conversation today.",
    page_num
))
page_num += 1

add(full_module_page(
    "SUCCESSOR &amp; STEWARD JOURNEY", 17, "Successor & Steward Journey",
    "Sequenced Covey's way &mdash; Identity, Priority, Habits, Collaboration &mdash; and built to stick using habit-formation mechanics. Draws its content from the seventeen Flourishing LifeTogether dimensions.",
    [
        "Start at Identity &amp; Purpose even if the successor is eager to skip to the practical work &mdash; the sequence matters.",
        "Protect a real, recurring block of calendar time for Priority before moving to Habits.",
        "Choose up to four Flourishing dimensions that match this successor's actual gaps to build their development plan.",
    ],
    "This module needs no new content to launch &mdash; it's a new lens on the Flourishing library that already exists.",
    page_num
))
page_num += 1

add(full_module_page(
    "FAMILY BUSINESS", 18, "Family Business",
    "A shared, honest picture of how the family business is actually governed, and who's ready for what role.",
    [
        "Complete the governance checklist first &mdash; it usually surfaces gaps nobody had named out loud.",
        "Add every family member with any real involvement, not just the presumed successor.",
        "Revisit readiness scores at least annually &mdash; readiness changes faster than most families update the record.",
    ],
    "A low governance score is common and not alarming on its own &mdash; treat it as the starting checklist, not a verdict.",
    page_num
))
page_num += 1

add(full_module_page(
    "STORIES", 19, "Stories",
    "Legacy, history, and value-based stories from the family, captured once and available to every generation after &mdash; helping the next generation understand and build on the family's why.",
    [
        "Use the provided prompts to get a reluctant storyteller started &mdash; a specific question is easier to answer than 'tell me a story.'",
        "Tag every story with the value it reflects so the library can be searched by value later, not just browsed chronologically.",
        "Capture stories from every generation, not just the oldest &mdash; a story from a young parent is as valuable as one from a grandparent.",
    ],
    "The best stories usually come from a specific moment, not a general summary &mdash; push for the scene, not the lesson.",
    page_num
))
page_num += 1

# =================================================================
# BACK COVER
# =================================================================
add(f'''
<div class="page navy">
  <div class="frame" style="display:flex; flex-direction:column; justify-content:space-between; align-items:center; text-align:center;">
    <div></div>
    <div>
      <div style="font-family:'Archivo'; font-weight:600; font-size:9.5pt; letter-spacing:0.24em; color:#D9B876;">LIFETOGETHER</div>
      <div style="height:0.26in;"></div>
      <h1 class="display" style="font-size:20pt; color:#FBF8F1;">Nineteen modules. One family journey.</h1>
      <div style="height:0.18in;"></div>
      <p class="lede" style="max-width:4.4in; margin:0 auto;">
        Six are live today. Thirteen are ready to build. Tell me which one's next.
      </p>
      <div style="height:0.3in;"></div>
      <div style="width:30px; height:2px; background:#B98D3E; margin:0 auto;"></div>
    </div>
    <div style="font-family:'Archivo'; font-weight:500; font-size:7.4pt; letter-spacing:0.1em; color:rgba(251,248,241,0.4);">THE FAMILY STEWARDSHIP PLAYBOOK</div>
  </div>
</div>
''')

# =================================================================
# ASSEMBLE
# =================================================================
with open("/home/claude/build/portrait_style.css") as f:
    base_css = f.read()

extra_css = '''
.mod-card{ border-top:2px solid var(--gold); padding-top:0.14in; margin-bottom:0.22in; }
.mod-n{ font-family:'Playfair'; font-weight:700; font-size:11pt; color:var(--gold); display:inline; }
.mod-group{ font-family:'Archivo'; font-weight:700; font-size:7.5pt; letter-spacing:0.1em; color:var(--gray); margin:0.04in 0; }
.mod-name{ font-family:'Playfair'; font-weight:700; font-size:14pt; color:var(--navy); margin-bottom:0.05in; }
.mod-purpose{ font-family:'Inter'; font-size:9pt; color:var(--ink); line-height:1.45; margin-bottom:0.08in; }
.mod-how, .mod-tip{ font-family:'Inter'; font-size:8.6pt; color:var(--ink); line-height:1.45; margin-bottom:0.05in; }
.mod-label{ font-family:'Archivo'; font-weight:700; font-size:7.2pt; letter-spacing:0.08em; text-transform:uppercase; color:var(--gold); margin-right:0.06in; }

.pb-steps{ }
.pb-step{ display:flex; gap:0.16in; padding:0.1in 0; border-top:1px solid var(--line); font-family:'Inter'; font-size:9.4pt; color:var(--ink); line-height:1.5; }
.pb-step:first-child{ border-top:none; }
.pb-step-n{ font-family:'Playfair'; font-weight:700; font-size:12pt; color:var(--gold); width:0.28in; flex-shrink:0; }
'''

html = f'''<!DOCTYPE html>
<html><head><meta charset="utf-8">
<style>{base_css}{extra_css}</style></head>
<body>{"".join(PAGES)}</body></html>'''

with open("/home/claude/build/family_stewardship_playbook.html", "w") as f:
    f.write(html)
print("Pages:", len(PAGES))
