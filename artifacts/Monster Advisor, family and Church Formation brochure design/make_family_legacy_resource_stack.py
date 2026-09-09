PAGES = []
def add(html): PAGES.append(html)

def folio(chapter, num):
    return f'''<div class="folio"><div class="thread">{chapter}</div><div>{num:02d}</div></div>'''

def step_chain(steps, dark=False):
    html = ""
    n = len(steps)
    for i, (t, d) in enumerate(steps):
        last = i == n - 1
        html += f'''
        <div class="step-row">
          <div style="display:flex; flex-direction:column; align-items:center;">
            <div class="step-circle">{i+1}</div>
            {'<div class="step-line"></div>' if not last else ''}
          </div>
          <div style="padding-top:0.02in;">
            <div class="step-title">{t}</div>
            <div class="step-desc">{d}</div>
          </div>
        </div>'''
    return html

# =================================================================
# PAGE 1 — COVER
# =================================================================
add(f'''
<div class="page navy">
  <div class="frame" style="display:flex; flex-direction:column; justify-content:flex-end;">
    <div style="font-family:'Archivo'; font-weight:600; font-size:9pt; letter-spacing:0.22em; color:#D4AC5C; margin-bottom:2.2in;">THE STANDARDIZED RESOURCE &amp; ADVISOR SYSTEM</div>
    <h1 class="display" style="font-size:27pt; color:#FBF9F4;">Family Legacy Resource Stack&trade;</h1>
    <div style="height:0.14in;"></div>
    <div style="font-family:'Playfair'; font-style:italic; font-weight:600; font-size:13.5pt; color:#D4AC5C;">One architecture. Forty domains. Hundreds of journeys. One lifetime family formation system.</div>
    <div style="height:0.28in;"></div>
    <p class="lede" style="font-size:10.5pt; color:rgba(251,249,244,0.8); max-width:5.6in;">
      For every Family Legacy Intelligence&trade; domain &mdash; the standardized system that
      turns legacy from a one-time planning event into a lifetime developmental journey.
    </p>
  </div>
</div>
''')

# =================================================================
# PAGE 2 — EXECUTIVE SUMMARY
# =================================================================
add(f'''
<div class="page">
  <div class="frame">
    <div class="eyebrow">EXECUTIVE SUMMARY</div>
    <div style="height:0.2in;"></div>
    <h1 class="display" style="font-size:21pt; color:var(--navy);">The Family Legacy Operating System&trade;</h1>
    <div style="height:0.16in;"></div>
    <p class="lede">
      A unified framework designed to help families understand who they are, what matters
      most, and how to intentionally pass faith, values, wisdom, relationships, and
      stewardship across generations.
    </p>
    <div style="height:0.14in;"></div>
    <p class="lede">
      It functions as a complete operating system for family life and legacy formation, not
      a collection of disconnected tools. At its core, the system organizes all family legacy
      work into forty interconnected domains &mdash; each representing a critical dimension of
      family life, from identity and faith to wealth, governance, and next-generation
      development. Together, these domains form a comprehensive map of family flourishing
      and continuity.
    </p>
    <div style="height:0.22in;"></div>
    <div class="takeaway">
      <span class="label">The problem this solves</span>
      Most families have assets, values, and intentions &mdash; but no system to intentionally transfer them across generations.
    </div>
  </div>
  {folio("Executive Summary", 2)}
</div>
''')

# =================================================================
# PAGE 3 — PURPOSE OF THE SYSTEM
# =================================================================
purposes = [
    "Understand their current reality — clarity",
    "Identify what matters most now — discernment",
    "Grow through guided experiences — formation",
    "Have meaningful conversations — alignment",
    "Take practical action — implementation",
    "Create lasting legacy artifacts — continuity",
    "Continue progressing over time — momentum",
]
purpose_html = "".join([f'<div style="padding:0.1in 0; border-top:1px solid var(--line); font-family:\'Inter\'; font-size:10.3pt;">{p}</div>' for p in purposes])
add(f'''
<div class="page">
  <div class="frame">
    <div class="eyebrow">PURPOSE OF THE SYSTEM</div>
    <div style="height:0.2in;"></div>
    <h1 class="display" style="font-size:20pt; color:var(--navy);">This system helps families do seven things.</h1>
    <div style="height:0.16in;"></div>
    {purpose_html}
    <div style="height:0.22in;"></div>
    <div class="pull-quote">It transforms legacy from <span class="mark">a one-time planning event</span> into a lifetime developmental journey.</div>
  </div>
  {folio("Purpose of the System", 3)}
</div>
''')

# =================================================================
# PAGE 4 — HOW THE 40 DOMAINS WORK TOGETHER
# =================================================================
domain_categories = [
    "Identity & Story", "Faith & Spiritual Heritage", "Values & Vision",
    "Relationships & Reconciliation", "Wealth & Stewardship", "Parenting & Next Generation",
    "Governance & Succession", "Generosity & Impact", "Communication, Health & Emotional Systems",
    "Business, Property & Enterprise Legacy", "Global, Cultural & Digital Legacy",
]
dom_chips = "".join([f'<span class="chip">{d}</span>' for d in domain_categories])
add(f'''
<div class="page">
  <div class="frame">
    <div class="eyebrow">HOW THE FORTY DOMAINS WORK TOGETHER</div>
    <div style="height:0.2in;"></div>
    <h1 class="display" style="font-size:19pt; color:var(--navy);">Not separate silos. A connected ecosystem of family life.</h1>
    <div style="height:0.16in;"></div>
    <div style="display:flex; flex-wrap:wrap; gap:0.1in; margin-bottom:0.26in;">{dom_chips}</div>
    <p class="lede" style="font-size:10.3pt;">The system is designed as a dynamic pathway, not a checklist:</p>
    <div style="height:0.1in;"></div>
    {"".join([f'<div style="padding:0.08in 0; font-family:Inter; font-size:10pt; border-top:1px solid var(--line);">{s}</div>' for s in [
        "Families begin in one domain based on their most urgent need",
        "Each domain reveals insights that naturally lead to the next",
        "Every experience produces clarity that unlocks deeper conversations",
        "Every conversation leads to action and tangible outcomes",
        "Every outcome points to the next best domain to explore",
    ]])}
    <div style="height:0.2in;"></div>
    <div class="takeaway"><span class="label">The result</span>A continuous cycle of discovery, formation, and activation across generations.</div>
  </div>
  {folio("How the Forty Domains Work Together", 4)}
</div>
''')

# =================================================================
# PAGE 5 — THE CORE FLOW (8-step chain)
# =================================================================
core_flow = [
    ("DISCOVER", "What is happening in this family right now?"),
    ("DISCERN", "What matters most in this season?"),
    ("JOURNEY", "What experience will help the family grow?"),
    ("EQUIP", "What tools will help them act wisely?"),
    ("CREATE", "What tangible legacy artifact should be produced?"),
    ("ACTIVATE", "What will the family do in the next 90 days?"),
    ("REVIEW", "What changed as a result?"),
    ("CONTINUE", "What is the next best conversation or journey?"),
]
add(f'''
<div class="page navy">
  <div class="frame">
    <div class="eyebrow">THE CORE FLOW OF THE SYSTEM</div>
    <div style="height:0.16in;"></div>
    <h1 class="display" style="font-size:19pt; color:#FBF9F4;">Every domain follows the same integrated progression.</h1>
    <div style="height:0.18in;"></div>
    {step_chain(core_flow, dark=True)}
  </div>
  {folio("The Core Flow", 5)}
</div>
''')

# =================================================================
# PAGE 6 — HOW FAMILIES USE THE SYSTEM END-TO-END
# =================================================================
family_stages = [
    ("Entry: Discovery", "An assessment or conversation reveals strengths, gaps, risks, opportunities, and readiness level."),
    ("Formation: Journey Experience", "A structured experience — a 21-day personal or family journey, a four-session facilitated family experience, guided reflection, Scripture, and conversation."),
    ("Equipping: Practical Tools", "Worksheets, planning tools, conversation guides, decision frameworks, and templates for action."),
    ("Legacy Creation: Tangible Outcomes", "Each domain produces a permanent artifact — a family mission statement, a spiritual legacy letter, a governance charter, a generosity plan, a family storybook."),
]
add(f'''
<div class="page">
  <div class="frame">
    <div class="eyebrow">HOW FAMILIES USE THE SYSTEM END-TO-END</div>
    <div style="height:0.18in;"></div>
    <h1 class="display" style="font-size:19pt; color:var(--navy);">Four stages, every time.</h1>
    <div style="height:0.16in;"></div>
    {step_chain(family_stages)}
    <div style="height:0.14in;"></div>
    <div class="takeaway"><span class="label">Institutional memory</span>Every legacy artifact a family creates becomes part of the permanent record &mdash; the institutional memory of the family.</div>
  </div>
  {folio("How Families Use the System", 6)}
</div>
''')

# =================================================================
# PAGE 7 — HOW ADVISORS USE THE SYSTEM
# =================================================================
advisor_uses = [
    ("Identify the Right Conversation", "Using assessments and intelligence briefs, advisors determine what issue matters most right now, what domain is most relevant, and what conversation should happen next."),
    ("Facilitate Without Overstepping", "Advisor briefings, discovery questions, conversation scripts, and green/yellow/red diagnostic signals keep advisors within the boundaries of their expertise."),
    ("Recommend the Next Best Journey", "Advisors recommend the next domain experience, sequence family development over time, and maintain momentum across generations."),
    ("Coordinate Specialists When Needed", "Legal professionals, financial advisors, therapists, family business consultants, and spiritual leaders — brought in when the domain calls for it."),
]
add(f'''
<div class="page">
  <div class="frame">
    <div class="eyebrow">HOW ADVISORS USE THE SYSTEM</div>
    <div style="height:0.18in;"></div>
    <h1 class="display" style="font-size:19pt; color:var(--navy);">The advisor becomes a trusted orchestrator, not the sole expert.</h1>
    <div style="height:0.16in;"></div>
    {step_chain(advisor_uses)}
    <div style="height:0.1in;"></div>
    <div class="takeaway"><span class="label">What the advisor never becomes</span>A therapist, an attorney, a pastor, a family counselor, or a business operator &mdash; the system keeps every role in its proper lane.</div>
  </div>
  {folio("How Advisors Use the System", 7)}
</div>
''')

# =================================================================
# PAGE 8 — THE FAMILY LEGACY RESOURCE STACK (8-layer structure)
# =================================================================
stack_layers = [
    "Intelligence Brief™ — why it matters",
    "Discovery Assessment™ — current reality",
    "21-Day Journey™ — personal formation",
    "Four-Session Family Experience™ — shared alignment",
    "Family Toolbox™ — practical execution tools",
    "Advisor Intelligence Guide™ — facilitation system",
    "Legacy Artifact Builder™ — tangible outcome",
    "Next Best Journey™ — continuity pathway",
]
stack_html = "".join([f'''
    <div style="display:flex; gap:0.16in; align-items:center; padding:0.12in 0; border-top:1px solid var(--line);">
      <div style="font-family:'Playfair'; font-weight:700; font-size:15pt; color:var(--gold); width:0.32in; flex-shrink:0;">{i+1}</div>
      <div style="font-family:'Inter'; font-size:10pt; color:var(--ink);">{layer}</div>
    </div>''' for i, layer in enumerate(stack_layers)])
add(f'''
<div class="page">
  <div class="frame">
    <div class="eyebrow">THE FAMILY LEGACY RESOURCE STACK&trade;</div>
    <div style="height:0.18in;"></div>
    <h1 class="display" style="font-size:19pt; color:var(--navy);">Every domain, the same eight-layer structure.</h1>
    <div style="height:0.14in;"></div>
    <p class="lede" style="font-size:10.3pt; margin-bottom:0.16in;">This ensures every family experience is consistent, scalable, advisor-ready, action-oriented, and generationally transferable.</p>
    {stack_html}
    <div style="height:0.18in;"></div>
    <div class="takeaway"><span class="label">The Master Family Pathway</span>Discover &rarr; Discern &rarr; Journey &rarr; Equip &rarr; Create &rarr; Activate &rarr; Review &rarr; Continue &mdash; the same progression, every domain, every time.</div>
  </div>
  {folio("The Family Legacy Resource Stack", 8)}
</div>
''')

# =================================================================
# PAGE 9 — THE RESULT: A LIVING FAMILY LEGACY SYSTEM
# =================================================================
results = [
    "A shared language for family life",
    "A decision-making framework across generations",
    "A discipleship system for faith and values",
    "A stewardship system for wealth and responsibility",
    "A communication system for difficult conversations",
    "A governance system for continuity and succession",
    "A formation system for next-generation readiness",
    "A legacy creation system for permanent artifacts",
]
results_html = "".join([f'<div style="padding:0.09in 0; border-top:1px solid rgba(212,172,92,0.25); font-family:Inter; font-size:10.3pt; color:rgba(251,249,244,0.9);">{r}</div>' for r in results])
add(f'''
<div class="page navy">
  <div class="frame">
    <div class="eyebrow">THE RESULT</div>
    <div style="height:0.18in;"></div>
    <h1 class="display" style="font-size:20pt; color:#FBF9F4;">A living family legacy system.</h1>
    <div style="height:0.16in;"></div>
    <p class="lede" style="font-size:10.3pt; margin-bottom:0.12in;">When fully implemented, the system becomes:</p>
    {results_html}
  </div>
  {folio("The Result", 9)}
</div>
''')

# =================================================================
# PAGE 10 — THE BIG IDEA
# =================================================================
add(f'''
<div class="page">
  <div class="frame" style="display:flex; flex-direction:column; justify-content:center;">
    <div class="eyebrow">THE BIG IDEA</div>
    <div style="height:0.3in;"></div>
    <div class="pull-quote" style="font-size:19pt; line-height:1.4;">
      The Family Legacy Operating System&trade; transforms legacy from<br/>
      <span style="color:var(--gray); font-size:15pt;">&ldquo;What we leave behind&rdquo;</span><br/><br/>
      into<br/><br/>
      <span class="mark">&ldquo;How we intentionally form families across generations while we are still together.&rdquo;</span>
    </div>
  </div>
  {folio("The Big Idea", 10)}
</div>
''')

# =================================================================
# PAGE 11 — FINAL POSITIONING
# =================================================================
positioning = [
    ("Family Legacy Resource Stack™", "A complete system for understanding, forming, and activating family legacy across generations."),
    ("Family Legacy Advisor System™", "A guided framework that helps advisors lead families through the most important conversations of their lives."),
    ("Family Legacy Intelligence™", "A unified platform that helps families discover where they are, discern what matters now, take the right journey, create what should last, and continue moving forward."),
]
pos_html = "".join([f'''
    <div style="border-top:1px solid var(--line); padding:0.18in 0;">
      <div style="font-family:'Playfair'; font-weight:700; font-size:14pt; color:var(--navy); margin-bottom:0.06in;">{t}</div>
      <div style="font-family:'Inter'; font-size:9.6pt; color:var(--ink); line-height:1.5;">{d}</div>
    </div>''' for t, d in positioning])
add(f'''
<div class="page">
  <div class="frame">
    <div class="eyebrow">FINAL POSITIONING</div>
    <div style="height:0.18in;"></div>
    <h1 class="display" style="font-size:19pt; color:var(--navy);">Three names. One system.</h1>
    <div style="height:0.1in;"></div>
    {pos_html}
  </div>
  {folio("Final Positioning", 11)}
</div>
''')

# =================================================================
# PAGE 12 — BACK COVER
# =================================================================
add(f'''
<div class="page navy">
  <div class="frame" style="display:flex; flex-direction:column; justify-content:space-between; align-items:center; text-align:center;">
    <div></div>
    <div>
      <div style="font-family:'Archivo'; font-weight:600; font-size:9.5pt; letter-spacing:0.28em; color:#D4AC5C;">LIFETOGETHER</div>
      <div style="height:0.26in;"></div>
      <h1 class="display" style="font-size:20pt; color:#FBF9F4;">Forty domains. One family, forming across generations.</h1>
      <div style="height:0.18in;"></div>
      <p class="lede" style="max-width:4.4in; margin:0 auto;">
        Every domain follows the same trusted architecture &mdash; ready to build out one at a
        time, or as a complete system.
      </p>
      <div style="height:0.3in;"></div>
      <div style="width:30px; height:2px; background:#B4872C; margin:0 auto;"></div>
      <div style="height:0.2in;"></div>
      <div style="font-family:'Archivo'; font-weight:500; font-size:9pt; letter-spacing:0.08em; color:rgba(251,249,244,0.75);">LIFETOGETHER.COM &nbsp;&middot;&nbsp; BRETT@LIFETOGETHER.COM</div>
    </div>
    <div style="font-family:'Archivo'; font-weight:500; font-size:7.6pt; letter-spacing:0.12em; color:rgba(251,249,244,0.4);">FAMILY LEGACY RESOURCE STACK&trade;</div>
  </div>
</div>
''')

# =================================================================
# ASSEMBLE
# =================================================================
with open("/home/claude/build/family_legacy_green_style.css") as f:
    base_css = f.read()

html = f'''<!DOCTYPE html>
<html><head><meta charset="utf-8">
<style>{base_css}</style></head>
<body>{"".join(PAGES)}</body></html>'''

with open("/home/claude/build/family_legacy_resource_stack.html", "w") as f:
    f.write(html)
print("Pages:", len(PAGES))
