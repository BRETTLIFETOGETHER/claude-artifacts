PAGES = []
def add(html): PAGES.append(html)

def folio(chapter, num):
    return f'''<div class="folio"><div class="thread">{chapter}</div><div>{num:02d}</div></div>'''

def prompt_block(text):
    return f'<div class="prompt-block">{text}</div>'

def module_page(eyebrow, group, title, purpose, prompts, num, extra_note=""):
    prompt_html = "".join([f'<div class="prompt-label">EXAMPLE PROMPT</div>{prompt_block(p)}' for p in prompts])
    note_html = f'<div class="takeaway"><span class="label">Note</span>{extra_note}</div>' if extra_note else ""
    return f'''
<div class="page">
  <div class="frame">
    <div class="eyebrow">{group}</div>
    <div style="height:0.16in;"></div>
    <h1 class="display" style="font-size:20pt; color:var(--navy);">{title}</h1>
    <div style="height:0.1in;"></div>
    <p class="lede" style="font-size:10.3pt;">{purpose}</p>
    <div style="height:0.2in;"></div>
    {prompt_html}
    {note_html}
  </div>
  {folio(eyebrow, num)}
</div>
'''

# =================================================================
# PAGE 1 — COVER
# =================================================================
add(f'''
<div class="page navy">
  <div class="frame" style="display:flex; flex-direction:column; justify-content:flex-end;">
    <div style="font-family:'Archivo'; font-weight:600; font-size:9pt; letter-spacing:0.22em; color:#D9B876; margin-bottom:2.2in;">AI PROMPT ARCHITECTURE &amp; MODULE SPECIFICATION</div>
    <h1 class="display" style="font-size:28pt; color:#FBF8F1;">The Family Journey Builder</h1>
    <div style="height:0.14in;"></div>
    <div style="font-family:'Playfair'; font-style:italic; font-weight:600; font-size:14pt; color:#D9B876;">One tab. A fully customized family plan, beyond the finances.</div>
    <div style="height:0.24in;"></div>
    <p class="lede" style="font-size:10.3pt; color:rgba(251,248,241,0.8); max-width:5.6in;">
      Thirteen modules, each with a defined purpose and working example prompts &mdash;
      designed to be embedded as a single tab across the Church platform, the Christian
      Advisor Network, Family Legacy By Design, and Financial Wisdom Ministry alike.
    </p>
  </div>
</div>
''')

# =================================================================
# PAGE 2 — THE BIG IDEA
# =================================================================
add(f'''
<div class="page">
  <div class="frame">
    <div class="eyebrow">THE BIG IDEA</div>
    <div style="height:0.2in;"></div>
    <h1 class="display" style="font-size:21pt; color:var(--navy);">A journey, not a document.</h1>
    <div style="height:0.16in;"></div>
    <p class="lede">
      Most planning tools produce a single static document &mdash; an assessment result, a
      values statement, a plan. The Family Journey Builder is different: it&rsquo;s a connected
      system where what a family uploads personalizes what they&rsquo;re coached on, what
      they&rsquo;re coached on shapes what they build, what they build feeds a growth plan,
      and the growth plan becomes an actual calendar with real next steps.
    </p>
    <div style="height:0.16in;"></div>
    <p class="lede">
      It is not a finance tool, though finances can be part of it. It is built around
      relationships and family goals &mdash; individual and corporate &mdash; with money as one
      input among many, not the organizing idea.
    </p>
    <div style="height:0.2in;"></div>
    <div class="takeaway">
      <span class="label">How it's meant to be embedded</span>
      As a single tab on any existing platform &mdash; the same thirteen modules, re-skinned in that platform&rsquo;s voice and branding, drawing on that platform&rsquo;s content library underneath.
    </div>
  </div>
  {folio("The Big Idea", 2)}
</div>
''')

# =================================================================
# PAGE 3 — SYSTEM MAP
# =================================================================
groups_map = [
    ("INPUT", "Sources", "What the family brings to personalize everything else."),
    ("DISCOVERY", "Family Map &middot; Finder", "Where the family actually is, and what to do about it next."),
    ("GUIDANCE", "Coaching &middot; Scripts", "What to say, and what the professionals in their life would say."),
    ("BUILDING", "Builders &middot; Habits &middot; Toolbox", "The documents, habits, and skills the family creates."),
    ("PLANNING", "Library Builder &middot; Calendar", "Turning everything above into one running plan with dates."),
    ("COMMUNITY", "Cohort", "Doing it with other families, not alone."),
    ("CONTENT", "Library", "The full 15,000-item catalog, searchable by outcome."),
    ("OUTPUT", "Publish", "Every result, in a finished, shareable format."),
]
rows = "".join([f'''
    <div style="display:flex; gap:0.24in; padding:0.14in 0; border-top:1px solid var(--line);">
      <div style="font-family:'Archivo'; font-weight:700; font-size:9pt; letter-spacing:0.1em; color:var(--gold); width:1.15in; flex-shrink:0;">{g}</div>
      <div style="width:2.1in; flex-shrink:0;"><div style="font-family:'Playfair'; font-weight:700; font-size:11.5pt; color:var(--navy);">{m}</div></div>
      <div style="font-family:'Inter'; font-size:9.3pt; color:var(--ink); line-height:1.45;">{d}</div>
    </div>''' for g, m, d in groups_map])
add(f'''
<div class="page">
  <div class="frame">
    <div class="eyebrow">SYSTEM MAP</div>
    <div style="height:0.16in;"></div>
    <h1 class="display" style="font-size:19pt; color:var(--navy);">Thirteen modules, eight functions.</h1>
    <div style="height:0.12in;"></div>
    {rows}
    <div style="height:0.2in;"></div>
    <div class="takeaway">
      <span class="label">A note on domains vs. modules</span>
      Everything above is a tool &mdash; a verb. Family Stewardship, Family Legacy, and Financial Wisdom are content domains &mdash; nouns the tools work on. The same thirteen modules apply regardless of which domain a family is working in.
    </div>
  </div>
  {folio("System Map", 3)}
</div>
''')

# =================================================================
# PAGE 4 — SOURCES
# =================================================================
add(module_page(
    "Sources", "INPUT &mdash; MODULE 1 OF 13", "Sources",
    "Everything a family or advisor already has &mdash; PDFs, Word documents, dictated notes, emails, reports, spreadsheets, even transcripts of past conversations &mdash; can be uploaded here so every other module personalizes around what's actually true for this family, not generic content.",
    [
        "Review the uploaded document and extract: (1) names, relationships, and roles of everyone mentioned, (2) explicit values or priorities the family has already stated, (3) open questions or unresolved tensions, (4) any prior commitments, plans, or numbers referenced. Summarize as a structured family profile draft, and flag anything ambiguous for the family to confirm rather than guessing.",
        "Compare this newly uploaded document against the family's existing profile. Identify anything that updates, contradicts, or adds detail to what's already on file. Do not silently overwrite existing information &mdash; list each proposed change for the family to confirm before saving.",
    ],
    4,
    "Accepted formats: PDF, Word, Excel/CSV, plain-text dictation exports, email threads, and prior chat transcripts. Every Source should be attributable &mdash; the system should always be able to say which document a given fact came from."
))

# =================================================================
# PAGE 5 — FAMILY MAP
# =================================================================
add(module_page(
    "Family Map", "DISCOVERY &mdash; MODULE 2 OF 13", "Family Map",
    "Aggregates every individual assessment a family has taken &mdash; Faith &amp; Practice, Whole-Life Stewardship, Marriage &amp; Money, Next-Generation Readiness, and others &mdash; into one shared, comparable view, instead of a stack of separate, disconnected reports.",
    [
        "Given individual assessment results for [Spouse A] and [Spouse B], build a side-by-side Couples Map: for each dimension, show both scores, flag anywhere they diverge by more than a moderate amount, and suggest one conversation starter per divergence &mdash; phrased for a couple at their kitchen table, not a clinician's office.",
        "Given assessment results across every family member provided, build a single Family Map showing where the family is aligned, where individuals differ from the group, and where a generational gap between parents and adult children is visible. Describe patterns, not rankings &mdash; never compare family members against each other by score.",
    ],
    5
))

# =================================================================
# PAGE 6 — FINDER
# =================================================================
add(module_page(
    "Finder", "DISCOVERY &mdash; MODULE 3 OF 13", "Finder",
    "Recommends the single best next step &mdash; not an overwhelming menu &mdash; based on where the family already is, drawing on their Family Map, their Sources, and what they've already completed in the system.",
    [
        "Given this family's Family Map and their history of completed content, recommend exactly one next step: a specific course, conversation, challenge, or habit. Explain in two sentences why this is the right next step now, and briefly why it's a better fit than the next two most obvious alternatives.",
        "The family has just completed [journey/course name]. Given their Family Map and what this journey typically surfaces, propose the single most natural next step &mdash; the thing most families in a similar position choose next &mdash; and one alternative for a family in a different season.",
    ],
    6
))

# =================================================================
# PAGE 7 — COACHING
# =================================================================
add(module_page(
    "Coaching", "GUIDANCE &mdash; MODULE 4 OF 13", "Coaching",
    "Role-based coaching that helps a family member understand what a lawyer, CPA, wealth manager, philanthropy manager, or family office professional would likely raise given their profile &mdash; so they walk into that real meeting with better questions, not a substitute for the meeting itself.",
    [
        "Acting as an experienced estate attorney reviewing this family's profile, list the three questions this family is most likely under-asking their actual attorney, and explain in plain language why each matters. Never give legal advice directly &mdash; frame everything as 'ask your attorney about...'",
        "Acting as a CPA, review this family's stated goals and flag two or three areas where a tax conversation is probably overdue, phrased as questions to bring to their own CPA. Repeat this same pattern for a wealth manager, a philanthropy manager, and a family office professional, each with role-appropriate questions.",
    ],
    7,
    "Every Coaching output should end with the same disclaimer: this prepares you for the conversation, it does not replace the professional."
))

# =================================================================
# PAGE 8 — SCRIPTS
# =================================================================
add(module_page(
    "Scripts", "GUIDANCE &mdash; MODULE 5 OF 13", "Scripts",
    "Word-for-word conversation scripts and Q&amp;A, tailored by relationship &mdash; advisor to family, parent to child, grandchild to grandparent &mdash; so nobody has to invent the opening line for a hard conversation from scratch.",
    [
        "Write an opening script, 120 to 150 words, for an adult child initiating a legacy conversation with an aging parent who has never discussed estate plans. Tone: respectful, not transactional. Include one soft opening question and one graceful exit line if the parent isn't ready to continue.",
        "Write a script an advisor can use to introduce the Whole-Life Stewardship Assessment to a new client in the first ten minutes of a meeting, without it sounding like a sales pitch. Include two likely objections and a one-line response to each.",
    ],
    8,
    "Scripts should always specify who is speaking and to whom &mdash; the same conversation reads differently from a spouse, a parent, an adult child, or an advisor."
))

# =================================================================
# PAGE 9 — BUILDERS
# =================================================================
builders_list = ["Purpose Builder", "Life Message Builder", "Family Values Builder", "Succession Builder", "Relationship Builder", "Marriage Builder"]
chips = "".join([f'<span class="chip">{b}</span>' for b in builders_list])
add(f'''
<div class="page">
  <div class="frame">
    <div class="eyebrow">BUILDING &mdash; MODULE 6 OF 13</div>
    <div style="height:0.16in;"></div>
    <h1 class="display" style="font-size:20pt; color:var(--navy);">Builders</h1>
    <div style="height:0.1in;"></div>
    <p class="lede" style="font-size:10.3pt;">A family of guided document-builders, each walking one person or couple through a structured set of questions to produce a finished, personal document in their own words &mdash; not a fill-in-the-blank template.</p>
    <div style="height:0.14in;"></div>
    <div class="chip-row">{chips}</div>
    <div style="height:0.2in;"></div>
    <div class="prompt-label">EXAMPLE PROMPT &mdash; LIFE MESSAGE BUILDER</div>
    {prompt_block("You are guiding someone through the Life Message Builder. Ask one question at a time. Start with: &lsquo;If your grandchildren only remembered one thing you believed, what would you want it to be?&rsquo; Wait for their answer before asking the next question. After eight to ten questions, draft a one-page Life Message written in their own words and voice, not generic language.")}
    <div class="prompt-label">EXAMPLE PROMPT &mdash; MARRIAGE BUILDER</div>
    {prompt_block("You are guiding a couple through the Marriage Builder. Ask each spouse the same question separately and privately, then reveal both answers side by side before moving to the next question.")}
    <div style="height:0.14in;"></div>
    <div class="takeaway"><span class="label">Personal edition</span>A single-person version of each Builder exists for anyone working through it alone &mdash; same questions, adapted for an individual voice rather than a couple or a family group.</div>
  </div>
  {folio("Builders", 9)}
</div>
''')

# =================================================================
# PAGE 10 — HABITS
# =================================================================
add(module_page(
    "Habits", "BUILDING &mdash; MODULE 7 OF 13", "Habits",
    "Turns a stated goal &mdash; &lsquo;be a better leader,&rsquo; &lsquo;be a more present parent&rsquo; &mdash; into a small, sustainable habit, in the spirit of Atomic Habits: tiny, specific, and nearly impossible to fail at, not a giant program nobody keeps.",
    [
        "The user wants to become a more present parent. Using habit-formation principles &mdash; cue, craving, response, reward &mdash; propose one two-minute daily habit and one weekly habit that would move them toward that goal. Make the first habit almost impossible to fail at, and explain the cue that will trigger it.",
        "The user completed [Builder or Assessment] and it surfaced a gap in [specific area]. Propose a 21-day habit sequence &mdash; three stages of one week each &mdash; that closes that gap gradually rather than all at once.",
    ],
    10
))

# =================================================================
# PAGE 11 — TOOLBOX
# =================================================================
add(module_page(
    "Toolbox", "BUILDING &mdash; MODULE 8 OF 13", "Toolbox",
    "A menu of specific skill-building tools &mdash; not just content &mdash; mapped to the outcome someone wants. Using a tool can lead naturally into a full course, curriculum, or journey when someone wants to go deeper.",
    [
        "Given the stated goal &lsquo;[X]&rsquo;, list three tools from the Toolbox that build the underlying skill. For each, give one sentence on what it trains and which course or curriculum it unlocks if the person wants to go further.",
    ],
    11
))

# =================================================================
# PAGE 12 — LIBRARY BUILDER
# =================================================================
add(module_page(
    "Library Builder", "PLANNING &mdash; MODULE 9 OF 13", "Library Builder",
    "Compiles everything the family has produced &mdash; completed assessments, Builder outputs, Coaching notes &mdash; into one running Growth Plan, instead of leaving them with a dozen disconnected documents to manage themselves.",
    [
        "Compile this family's completed assessments, Builder outputs, and Coaching notes into a single Growth Plan document with three sections: Where We Are, What We're Working On, and What's Next. Keep it to four pages. Use the family's own words wherever they already exist rather than rewriting them.",
    ],
    12
))

# =================================================================
# PAGE 13 — CALENDAR
# =================================================================
add(module_page(
    "Calendar", "PLANNING &mdash; MODULE 10 OF 13", "Calendar",
    "Sequences everything in the Growth Plan into a realistic one-year plan &mdash; which journey, course, conversation, skill, or habit happens in which month, paced to what the family can actually sustain.",
    [
        "Given this family's Growth Plan and their stated capacity (time available per week), build a twelve-month calendar sequencing their recommended journeys, conversations, and habits. No more than one major commitment per month. Flag natural seasonal fits &mdash; legacy conversations in the fourth quarter, generosity content before year-end.",
    ],
    13
))

# =================================================================
# PAGE 14 — COHORT
# =================================================================
add(module_page(
    "Cohort", "COMMUNITY &mdash; MODULE 11 OF 13", "Cohort",
    "Helps a family build a small group around this content &mdash; friends, extended family, or a church group &mdash; going through the same journey together, with the content and structure to actually sustain it.",
    [
        "Generate an invitation message a family could send to three to five other families to start a cohort around [specific journey]. Include a suggested meeting cadence, a realistic group size, and the first discussion question to open the first gathering.",
    ],
    14
))

# =================================================================
# PAGE 15 — LIBRARY
# =================================================================
add(module_page(
    "Library", "CONTENT &mdash; MODULE 12 OF 13", "Library",
    "Full-catalog search across the entire content library &mdash; roughly 15,000 courses, classes, curricula, and pieces of content &mdash; by topic, theme, or desired outcome, not just by browsing fixed categories.",
    [
        "Given the search query &lsquo;[free text]&rsquo;, return the five most relevant items from the library, each with a one-line reason it matches, ranked by how directly it addresses the stated outcome rather than by keyword overlap alone.",
        "The family described their goal in their own words: &lsquo;[free text]&rsquo;. Translate this into the underlying themes and outcomes it maps to, then search the library against those themes rather than the literal words used.",
    ],
    15
))

# =================================================================
# PAGE 16 — PUBLISH
# =================================================================
publish_formats = ["PDF", "PowerPoint", "Brochure", "Template", "Print-Ready File", "InDesign File"]
chips2 = "".join([f'<span class="chip">{b}</span>' for b in publish_formats])
add(f'''
<div class="page">
  <div class="frame">
    <div class="eyebrow">OUTPUT &mdash; MODULE 13 OF 13</div>
    <div style="height:0.16in;"></div>
    <h1 class="display" style="font-size:20pt; color:var(--navy);">Publish</h1>
    <div style="height:0.1in;"></div>
    <p class="lede" style="font-size:10.3pt;">Turns any output from any other module into a finished, branded deliverable &mdash; in whatever format the family or advisor actually needs to use it.</p>
    <div style="height:0.14in;"></div>
    <div class="chip-row">{chips2}</div>
    <div style="height:0.2in;"></div>
    <div class="prompt-label">EXAMPLE PROMPT</div>
    {prompt_block("Take this completed Builder output and format it as a print-ready, single-page PDF using the family's chosen branding, with a title, a pull quote drawn from their own words, and a signature line at the bottom.")}
    <div class="prompt-label">EXAMPLE PROMPT</div>
    {prompt_block("Convert this Growth Plan into a six-slide PowerPoint summary suitable for the family to review together at a kitchen-table conversation &mdash; one idea per slide, minimal text, no jargon.")}
  </div>
  {folio("Publish", 16)}
</div>
''')

# =================================================================
# PAGE 17 — HOW IT CONNECTS
# =================================================================
flow_steps = [
    ("Sources", "The family uploads what they already have."),
    ("Family Map", "Their assessments become one shared picture."),
    ("Finder + Coaching + Scripts", "The system recommends, coaches, and gives language for the next conversation."),
    ("Builders + Habits + Toolbox", "The family creates real documents, habits, and skills."),
    ("Library Builder + Calendar", "Everything becomes one plan, sequenced across a year."),
    ("Cohort + Library", "The family does it with others, drawing on the full catalog."),
    ("Publish", "Every result becomes something they can hold, print, or share."),
]
flow_html = ""
for i, (t, d) in enumerate(flow_steps):
    flow_html += f'''
    <div style="display:flex; gap:0.18in; padding-bottom:{'0.18in' if i < len(flow_steps)-1 else '0'};">
      <div style="display:flex; flex-direction:column; align-items:center; width:0.32in; flex-shrink:0;">
        <div style="width:0.32in; height:0.32in; border-radius:50%; background:var(--navy); color:var(--gold-bright, #D9B876); display:flex; align-items:center; justify-content:center; font-family:'Playfair'; font-weight:700; font-size:11pt;">{i+1}</div>
        {'<div style="width:1.5px; flex:1; background:var(--gold); opacity:0.4; margin-top:0.04in;"></div>' if i < len(flow_steps)-1 else ''}
      </div>
      <div style="padding-bottom:0.06in;">
        <div style="font-family:'Playfair'; font-weight:700; font-size:12.5pt; color:var(--navy); margin-bottom:0.03in;">{t}</div>
        <div style="font-family:'Inter'; font-size:9.4pt; color:var(--gray); line-height:1.5;">{d}</div>
      </div>
    </div>'''
add(f'''
<div class="page">
  <div class="frame">
    <div class="eyebrow">HOW IT CONNECTS</div>
    <div style="height:0.16in;"></div>
    <h1 class="display" style="font-size:19pt; color:var(--navy);">One journey, not thirteen separate tools.</h1>
    <div style="height:0.16in;"></div>
    {flow_html}
  </div>
  {folio("How It Connects", 17)}
</div>
''')

# =================================================================
# PAGE 18 — EMBEDDING AS A TAB
# =================================================================
add(f'''
<div class="page navy">
  <div class="frame">
    <div class="eyebrow">EMBEDDING AS A TAB</div>
    <div style="height:0.18in;"></div>
    <h1 class="display" style="font-size:20pt; color:#FBF8F1;">One system, four skins.</h1>
    <div style="height:0.16in;"></div>
    <p class="lede">
      The same thirteen modules should work identically underneath, whichever platform a
      family enters from &mdash; only the branding, tone, and starting content domain change.
    </p>
    <div style="height:0.2in;"></div>
    <div class="takeaway"><span class="label">On the Church platform</span>A pastor-facing tone, starting content pulled from 40 Day Campaigns and the Biblical Purpose Library.</div>
    <div style="height:0.14in;"></div>
    <div class="takeaway"><span class="label">On the Christian Advisor Network</span>An advisor-facing tone, Coaching weighted toward the professional roles, starting content from the Resource Rack.</div>
    <div style="height:0.14in;"></div>
    <div class="takeaway"><span class="label">On Family Legacy By Design</span>Family Map and Builders foregrounded, starting content from the Ten Titles.</div>
    <div style="height:0.14in;"></div>
    <div class="takeaway"><span class="label">On Financial Wisdom Ministry</span>Habits and Toolbox weighted toward stewardship practices, once that platform exists.</div>
  </div>
  {folio("Embedding as a Tab", 18)}
</div>
''')

# =================================================================
# PAGE 19 — BACK COVER
# =================================================================
add(f'''
<div class="page navy">
  <div class="frame" style="display:flex; flex-direction:column; justify-content:space-between; align-items:center; text-align:center;">
    <div></div>
    <div>
      <div style="font-family:'Archivo'; font-weight:600; font-size:9.5pt; letter-spacing:0.24em; color:#D9B876;">LIFETOGETHER</div>
      <div style="height:0.26in;"></div>
      <h1 class="display" style="font-size:20pt; color:#FBF8F1;">Thirteen modules. One journey.</h1>
      <div style="height:0.18in;"></div>
      <p class="lede" style="max-width:4.4in; margin:0 auto;">
        Tell me which module to build first &mdash; as a working prompt set, a live interactive
        tab, or both.
      </p>
      <div style="height:0.3in;"></div>
      <div style="width:30px; height:2px; background:#B98D3E; margin:0 auto;"></div>
    </div>
    <div style="font-family:'Archivo'; font-weight:500; font-size:7.4pt; letter-spacing:0.1em; color:rgba(251,248,241,0.4);">THE FAMILY JOURNEY BUILDER &middot; SPECIFICATION DRAFT</div>
  </div>
</div>
''')

# =================================================================
# ASSEMBLE
# =================================================================
with open("/home/claude/build/portrait_style.css") as f:
    base_css = f.read()

extra_css = '''
.prompt-label{ font-family:'Archivo'; font-weight:700; font-size:7.8pt; letter-spacing:0.12em; text-transform:uppercase; color:var(--gold); margin-bottom:0.06in; margin-top:0.14in; }
.prompt-label:first-child{ margin-top:0; }
.prompt-block{ font-family:'Inter'; font-size:9pt; line-height:1.55; color:var(--ink); background:var(--cream); border-left:3px solid var(--gold); padding:0.13in 0.16in; font-style:italic; }
.chip-row{ display:flex; flex-wrap:wrap; gap:0.1in; }
.chip{ font-family:'Archivo'; font-weight:600; font-size:8.5pt; letter-spacing:0.04em; color:var(--navy); background:var(--cream); border:1px solid var(--line); padding:0.06in 0.12in; border-radius:14px; }
'''

html = f'''<!DOCTYPE html>
<html><head><meta charset="utf-8">
<style>{base_css}{extra_css}</style></head>
<body>{"".join(PAGES)}</body></html>'''

with open("/home/claude/build/family_journey_builder.html", "w") as f:
    f.write(html)
print("Pages:", len(PAGES))
