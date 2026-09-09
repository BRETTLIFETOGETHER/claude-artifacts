PAGES = []
def add(html): PAGES.append(html)

def folio(chapter, num):
    return f'''<div class="folio"><div class="thread">{chapter}</div><div>{num:02d}</div></div>'''

# =================================================================
# PAGE 1 — COVER
# =================================================================
add(f'''
<div class="page navy">
  <div class="frame" style="display:flex; flex-direction:column; justify-content:flex-end;">
    <div style="font-family:'Archivo'; font-weight:600; font-size:9pt; letter-spacing:0.22em; color:#D9B876; margin-bottom:2.2in;">GAP ANALYSIS &amp; FRAMEWORK TRANSLATION</div>
    <h1 class="display" style="font-size:25pt; color:#FBF8F1; line-height:1.2;">What&rsquo;s Missing, and Two Frameworks That Fill It</h1>
    <div style="height:0.14in;"></div>
    <div style="font-family:'Playfair'; font-style:italic; font-weight:600; font-size:13pt; color:#D9B876;">Retention. Referrals. Relational bonds. Assets under management.</div>
    <div style="height:0.24in;"></div>
    <p class="lede" style="font-size:10.3pt; color:rgba(251,248,241,0.8); max-width:5.6in;">
      Three questions, answered in order: what the Family Journey Builder still needs to
      actually serve an advisor&rsquo;s business, what habit-formation science contributes to
      building a successor, and what Covey&rsquo;s framework contributes to the same goal.
    </p>
  </div>
</div>
''')

# =================================================================
# PAGE 2 — PART ONE INTRO
# =================================================================
add(f'''
<div class="page">
  <div class="frame">
    <div class="eyebrow">PART ONE &mdash; THE GAP ANALYSIS</div>
    <div style="height:0.2in;"></div>
    <h1 class="display" style="font-size:20pt; color:var(--navy);">The thirteen modules serve the family. Four things are missing that serve the advisor&rsquo;s business.</h1>
    <div style="height:0.16in;"></div>
    <p class="lede">
      Everything built so far answers &ldquo;what does this family need?&rdquo; It doesn&rsquo;t yet
      answer the advisor&rsquo;s four real business questions: how do I keep this family as a
      client for decades, how do I earn a referral without asking for one, how do I become
      woven into the family&rsquo;s actual life rather than just their portfolio, and how do I
      grow the assets I manage without ever feeling like I&rsquo;m selling.
    </p>
    <div style="height:0.16in;"></div>
    <p class="lede">
      Four sections follow, one per outcome, each naming the specific new category,
      template, or journey that closes the gap.
    </p>
  </div>
  {folio("Part One — The Gap Analysis", 2)}
</div>
''')

# =================================================================
# PAGE 3 — RETENTION
# =================================================================
retention_items = [
    ("Milestone &amp; Trigger Event Tracker", "Births, marriages, deaths, business sales, retirements, health crises — the exact moments when a family is most likely to switch advisors if their current one doesn't show up meaningfully. Nothing in the current system tracks these dates or prompts outreach around them."),
    ("The Next-Gen Bridge Journey", "A structured, multi-session program introducing the advisor to the client's adult children years before any wealth actually transfers. This is the single highest-leverage retention tool available — most advisory relationships that end at a generational transfer end because the heirs never had a relationship with the advisor in the first place."),
    ("The Annual Family Letter Template", "A yearly letter addressed to the whole family, not just the primary client — reinforcing that the relationship is with the family, not one signature on an account."),
]
rows = "".join([f'''
    <div style="border-top:1px solid var(--line); padding:0.16in 0;">
      <div style="font-family:'Playfair'; font-weight:700; font-size:12.5pt; color:var(--navy); margin-bottom:0.05in;">{t}</div>
      <div style="font-family:'Inter'; font-size:9.3pt; color:var(--ink); line-height:1.55;">{d}</div>
    </div>''' for t, d in retention_items])
add(f'''
<div class="page">
  <div class="frame">
    <div class="eyebrow">RETENTION</div>
    <div style="height:0.16in;"></div>
    <h1 class="display" style="font-size:19pt; color:var(--navy);">Keeping the family for decades, not years.</h1>
    <div style="height:0.1in;"></div>
    {rows}
  </div>
  {folio("Retention", 3)}
</div>
''')

# =================================================================
# PAGE 4 — REFERRALS
# =================================================================
referral_items = [
    ("The Referral Moment Trigger", "Right now, nothing in the system creates a natural opening for a referral. The best moment to ask isn't a scheduled quarterly check-in — it's immediately after a family finishes something meaningful, like a Builder or a breakthrough Family Map conversation, when the value is freshest and most emotionally real."),
    ("The Advocate Journey", "A short, optional path for families who've completed a full journey — capturing their story as a testimonial, and giving them an actual toolkit (a one-page handout, a short script) to pass along to a friend, rather than just asking them to \u2018send people my way.\u2019"),
    ("Cross-Referral Built Into Cohort", "The existing Cohort module already helps a family build a small group. Adding an explicit \u2018invite a friend family\u2019 step to that flow turns something that already exists into a natural referral engine, instead of a separate ask."),
]
rows2 = "".join([f'''
    <div style="border-top:1px solid var(--line); padding:0.16in 0;">
      <div style="font-family:'Playfair'; font-weight:700; font-size:12.5pt; color:var(--navy); margin-bottom:0.05in;">{t}</div>
      <div style="font-family:'Inter'; font-size:9.3pt; color:var(--ink); line-height:1.55;">{d}</div>
    </div>''' for t, d in referral_items])
add(f'''
<div class="page">
  <div class="frame">
    <div class="eyebrow">REFERRALS</div>
    <div style="height:0.16in;"></div>
    <h1 class="display" style="font-size:19pt; color:var(--navy);">Earning the introduction without ever asking for it.</h1>
    <div style="height:0.1in;"></div>
    {rows2}
  </div>
  {folio("Referrals", 4)}
</div>
''')

# =================================================================
# PAGE 5 — RELATIONAL BONDS
# =================================================================
relational_items = [
    ("The Family Meeting Facilitator", "A structured agenda template plus discussion prompts the advisor can use to run &mdash; or simply attend well &mdash; an actual family governance meeting. Advisors who are structurally present in family decision-making, not just financial reviews, become nearly impossible to replace."),
    ("The Multi-Generational Calendar", "Birthdays, anniversaries, graduations &mdash; not just account reviews and tax deadlines. An advisor who's woven into the family's actual rhythm of life is a relationship, not a vendor."),
    ("The Family Ledger", "A living, shared document tracking family decisions and commitments over time &mdash; what was agreed at the last family meeting, what values were named in the Family Values Builder, what's changed since. Gives every family meeting a memory instead of starting over each time."),
]
rows3 = "".join([f'''
    <div style="border-top:1px solid var(--line); padding:0.16in 0;">
      <div style="font-family:'Playfair'; font-weight:700; font-size:12.5pt; color:var(--navy); margin-bottom:0.05in;">{t}</div>
      <div style="font-family:'Inter'; font-size:9.3pt; color:var(--ink); line-height:1.55;">{d}</div>
    </div>''' for t, d in relational_items])
add(f'''
<div class="page">
  <div class="frame">
    <div class="eyebrow">RELATIONAL BONDS</div>
    <div style="height:0.16in;"></div>
    <h1 class="display" style="font-size:19pt; color:var(--navy);">Becoming part of the family's life, not just its portfolio.</h1>
    <div style="height:0.1in;"></div>
    {rows3}
  </div>
  {folio("Relational Bonds", 5)}
</div>
''')

# =================================================================
# PAGE 6 — AUM GROWTH
# =================================================================
aum_items = [
    ("The Complete Financial Picture", "A permission-based module that helps surface assets not currently under this advisor's management &mdash; retirement accounts elsewhere, real estate, business interests, other advisory relationships. Framed entirely as \u2018helping the family see the whole picture,\u2019 never as prospecting, and always with the family's explicit consent."),
    ("The Business Exit Readiness Journey", "For business-owner clients specifically, a structured path toward a liquidity event &mdash; one of the single largest asset-growth moments in any advisory relationship, and one that's lost more often than won when the advisor isn't already present for the conversation years in advance."),
    ("The Giving Vehicle Setup Journey", "Walks a family from an abstract generosity goal to an actual structured giving vehicle &mdash; a donor-advised fund or family foundation &mdash; that the advisor helps establish and manage. Turns the Generosity content already in the system into an actual asset-management outcome."),
]
rows4 = "".join([f'''
    <div style="border-top:1px solid var(--line); padding:0.16in 0;">
      <div style="font-family:'Playfair'; font-weight:700; font-size:12.5pt; color:var(--navy); margin-bottom:0.05in;">{t}</div>
      <div style="font-family:'Inter'; font-size:9.3pt; color:var(--ink); line-height:1.55;">{d}</div>
    </div>''' for t, d in aum_items])
add(f'''
<div class="page">
  <div class="frame">
    <div class="eyebrow">ASSETS UNDER MANAGEMENT</div>
    <div style="height:0.16in;"></div>
    <h1 class="display" style="font-size:19pt; color:var(--navy);">Growing the relationship without ever selling.</h1>
    <div style="height:0.1in;"></div>
    {rows4}
  </div>
  {folio("Assets Under Management", 6)}
</div>
''')

# =================================================================
# PAGE 7 — PART TWO INTRO: ATOMIC HABITS
# =================================================================
add(f'''
<div class="page navy">
  <div class="frame">
    <div class="eyebrow">PART TWO &mdash; WHAT HABIT-FORMATION SCIENCE CONTRIBUTES</div>
    <div style="height:0.2in;"></div>
    <h1 class="display" style="font-size:20pt; color:#FBF8F1;">Becoming a successor is an identity change, not a task list.</h1>
    <div style="height:0.16in;"></div>
    <p class="lede">
      The most useful contribution from modern habit-formation research isn&rsquo;t a specific
      technique &mdash; it&rsquo;s the underlying premise: people don&rsquo;t sustain behavior because
      they decided to. They sustain it because the behavior became part of who they believe
      they are, the environment made it easy, and the process felt satisfying long before
      the results showed up. Succession planning almost always skips straight to the tasks
      &mdash; learn the financials, meet the board &mdash; without ever building the identity or the
      environment that would make those tasks stick.
    </p>
  </div>
  {folio("Part Two — Habit-Formation Science", 7)}
</div>
''')

# =================================================================
# PAGE 8 — ATOMIC HABITS TRANSLATIONS 1
# =================================================================
habit_items = [
    ("Identity Before Behavior", "Before teaching a successor to read a balance sheet, help them answer a different question first: what kind of person leads this family's legacy? Habit change that starts with identity (\u2018I am someone who stewards this well\u2019) outlasts habit change that starts with a task (\u2018I should learn to read financials\u2019)."),
    ("The Four Levers of a New Habit", "Any new succession habit is easier to build if it's obvious (visible on a shared calendar, not a private intention), attractive (paired with something the successor already enjoys), easy (scaled down to almost nothing at first), and satisfying (some small, immediate reward or acknowledgment, not just a distant future payoff)."),
    ("Habit Stacking", "New governance habits stick better when they're attached to a ritual that already exists &mdash; \u2018after Sunday dinner, we spend ten minutes on one family business topic\u2019 &mdash; rather than asking a successor to create an entirely new habit from nothing."),
]
rows5 = "".join([f'''
    <div style="border-top:1px solid var(--line); padding:0.16in 0;">
      <div style="font-family:'Playfair'; font-weight:700; font-size:12.5pt; color:var(--navy); margin-bottom:0.05in;">{t}</div>
      <div style="font-family:'Inter'; font-size:9.3pt; color:var(--ink); line-height:1.55;">{d}</div>
    </div>''' for t, d in habit_items])
add(f'''
<div class="page">
  <div class="frame">
    <div class="eyebrow">TRANSFERABLE PRINCIPLES &mdash; 1 OF 2</div>
    <div style="height:0.16in;"></div>
    <h1 class="display" style="font-size:19pt; color:var(--navy);">Three principles for building the successor's identity and rhythm.</h1>
    <div style="height:0.1in;"></div>
    {rows5}
  </div>
  {folio("Transferable Principles", 8)}
</div>
''')

# =================================================================
# PAGE 9 — ATOMIC HABITS TRANSLATIONS 2
# =================================================================
habit_items2 = [
    ("Start Absurdly Small", "The intimidation of \u2018learn to run the business\u2019 or \u2018learn to manage the family's giving\u2019 is exactly why succession gets postponed for years. Scaling the first version of the habit down to something almost trivial &mdash; read one page of the financials, sit in on one meeting without speaking &mdash; removes the resistance that keeps people from starting at all."),
    ("Design the Environment", "The most reliable habits aren't willpower-driven, they're environment-driven. Structurally including the successor in meetings by default, rather than waiting for them to ask to be included, does more to build the habit than any amount of encouragement."),
    ("A Readiness Scorecard", "A simple self-audit &mdash; where am I already engaged, where am I avoiding &mdash; makes progress visible to the successor themselves, which is often more motivating than anyone else's assessment of their readiness."),
    ("Never Miss Twice", "A multi-year succession journey will have dropped weeks and skipped meetings. The standard that actually holds isn't perfection &mdash; it's never letting one missed commitment become two in a row."),
]
rows6 = "".join([f'''
    <div style="border-top:1px solid var(--line); padding:0.15in 0;">
      <div style="font-family:'Playfair'; font-weight:700; font-size:12pt; color:var(--navy); margin-bottom:0.04in;">{t}</div>
      <div style="font-family:'Inter'; font-size:9.1pt; color:var(--ink); line-height:1.5;">{d}</div>
    </div>''' for t, d in habit_items2])
add(f'''
<div class="page">
  <div class="frame">
    <div class="eyebrow">TRANSFERABLE PRINCIPLES &mdash; 2 OF 2</div>
    <div style="height:0.16in;"></div>
    <h1 class="display" style="font-size:19pt; color:var(--navy);">Four more principles for actually sustaining the work.</h1>
    <div style="height:0.1in;"></div>
    {rows6}
    <div style="height:0.16in;"></div>
    <div class="takeaway"><span class="label">Where this plugs in</span>The existing Habits module is the natural home for all seven of these &mdash; reframed specifically around succession and generosity stewardship rather than generic personal habits.</div>
  </div>
  {folio("Transferable Principles", 9)}
</div>
''')

# =================================================================
# PAGE 10 — PART THREE INTRO: COVEY
# =================================================================
add(f'''
<div class="page navy">
  <div class="frame">
    <div class="eyebrow">PART THREE &mdash; WHAT COVEY'S FRAMEWORK CONTRIBUTES</div>
    <div style="height:0.2in;"></div>
    <h1 class="display" style="font-size:20pt; color:#FBF8F1;">Where habit science explains how change sticks, Covey explains what to change first.</h1>
    <div style="height:0.16in;"></div>
    <p class="lede">
      Stephen Covey's well-known framework of personal effectiveness contributes something
      different than habit science does &mdash; not the mechanics of building a habit, but the
      sequence of priorities underneath good stewardship and succession: character before
      technique, clarity of purpose before action, and understanding before being
      understood. Several of his most well-known ideas map almost exactly onto tools
      already built into this system.
    </p>
  </div>
  {folio("Part Three — Covey's Framework", 10)}
</div>
''')

# =================================================================
# PAGE 11 — COVEY TRANSLATIONS 1
# =================================================================
covey_items = [
    ("Begin with the End in Mind", "Covey's well-known emphasis on starting with a clear picture of the destination maps directly onto the existing Family Values Builder and Life Message Builder &mdash; a successor's development should start with a clear picture of the legacy they're stewarding toward, not a list of skills to acquire."),
    ("Put First Things First", "Succession and generosity work is almost always important but not urgent &mdash; which is exactly why it gets endlessly postponed in favor of whatever is loudest that week. The fix isn't motivation, it's a structural one: a protected, recurring block of time that can't be bumped by whatever feels urgent."),
    ("Think Win-Win", "Sibling succession and family generosity decisions are often quietly treated as zero-sum &mdash; if one child leads, another loses status. Structuring these conversations explicitly around mutual benefit, not competition, defuses a tension that otherwise undermines the whole succession process."),
]
rows7 = "".join([f'''
    <div style="border-top:1px solid var(--line); padding:0.16in 0;">
      <div style="font-family:'Playfair'; font-weight:700; font-size:12.5pt; color:var(--navy); margin-bottom:0.05in;">{t}</div>
      <div style="font-family:'Inter'; font-size:9.3pt; color:var(--ink); line-height:1.55;">{d}</div>
    </div>''' for t, d in covey_items])
add(f'''
<div class="page">
  <div class="frame">
    <div class="eyebrow">TRANSFERABLE PRINCIPLES &mdash; 1 OF 2</div>
    <div style="height:0.16in;"></div>
    <h1 class="display" style="font-size:19pt; color:var(--navy);">Three habits that set direction and priority.</h1>
    <div style="height:0.1in;"></div>
    {rows7}
  </div>
  {folio("Transferable Principles", 11)}
</div>
''')

# =================================================================
# PAGE 12 — COVEY TRANSLATIONS 2
# =================================================================
covey_items2 = [
    ("Seek First to Understand", "Maps directly onto the Scripts module. A new successor's first real job is deep listening to the founder's story and reasoning &mdash; not proposing changes &mdash; and the Scripts built for that specific conversation should be structured to slow the successor down long enough to actually listen first."),
    ("Synergize", "Family council decisions get stronger, not weaker, when they deliberately draw out different strengths &mdash; the numbers person, the relationship person, the vision-caster &mdash; rather than routing every decision through one designated successor."),
    ("Renewal Across Every Dimension", "Covey's well-known call to renew across physical, mental, social-emotional, and spiritual dimensions lines up almost exactly with the four groups already organizing Flourishing LifeTogether &mdash; Personal, Relational, Spiritual, and Vocational flourishing. A successor's development plan should draw from all four, not just the vocational one."),
]
rows8 = "".join([f'''
    <div style="border-top:1px solid var(--line); padding:0.16in 0;">
      <div style="font-family:'Playfair'; font-weight:700; font-size:12.5pt; color:var(--navy); margin-bottom:0.05in;">{t}</div>
      <div style="font-family:'Inter'; font-size:9.3pt; color:var(--ink); line-height:1.55;">{d}</div>
    </div>''' for t, d in covey_items2])
add(f'''
<div class="page">
  <div class="frame">
    <div class="eyebrow">TRANSFERABLE PRINCIPLES &mdash; 2 OF 2</div>
    <div style="height:0.16in;"></div>
    <h1 class="display" style="font-size:19pt; color:var(--navy);">Three more habits, and a direct line to Flourishing LifeTogether.</h1>
    <div style="height:0.1in;"></div>
    {rows8}
    <div style="height:0.16in;"></div>
    <div class="takeaway"><span class="label">The strongest connection in this whole document</span>Covey's four dimensions of renewal and Flourishing LifeTogether's four groups are close enough to the same idea that a Successor Development Plan could literally be organized using the seventeen Flourishing dimensions already built &mdash; no new content required, just a new lens on existing content.</div>
  </div>
  {folio("Transferable Principles", 12)}
</div>
''')

# =================================================================
# PAGE 13 — SYNTHESIS
# =================================================================
add(f'''
<div class="page navy">
  <div class="frame">
    <div class="eyebrow">SYNTHESIS</div>
    <div style="height:0.2in;"></div>
    <h1 class="display" style="font-size:20pt; color:#FBF8F1;">One new module: the Successor &amp; Steward Journey.</h1>
    <div style="height:0.16in;"></div>
    <p class="lede">
      Both frameworks point at the same gap in the same place. Rather than bolting on
      &ldquo;Atomic Habits content&rdquo; and &ldquo;Covey content&rdquo; as two separate additions, they combine
      into one fourteenth module: a Successor &amp; Steward Journey that uses Covey&rsquo;s
      sequence &mdash; identity and purpose first, then priority, then collaboration &mdash; and
      habit science&rsquo;s mechanics to actually make each stage stick.
    </p>
    <div style="height:0.2in;"></div>
    <div class="takeaway"><span class="label">Stage 1 — Identity &amp; Purpose</span>Life Message Builder + Family Values Builder, reframed as &ldquo;who am I becoming as a steward,&rdquo; not a skills checklist.</div>
    <div style="height:0.14in;"></div>
    <div class="takeaway"><span class="label">Stage 2 — Priority</span>A protected, recurring calendar block for succession work, defended against whatever feels urgent that week.</div>
    <div style="height:0.14in;"></div>
    <div class="takeaway"><span class="label">Stage 3 — Small, Sustained Habits</span>Two-minute starting habits, stacked onto existing family rituals, tracked with a simple Readiness Scorecard.</div>
    <div style="height:0.14in;"></div>
    <div class="takeaway"><span class="label">Stage 4 — Collaboration</span>Family council practice built on understanding-first listening and win-win framing, not top-down instruction.</div>
  </div>
  {folio("Synthesis", 13)}
</div>
''')

# =================================================================
# PAGE 14 — BACK COVER
# =================================================================
add(f'''
<div class="page navy">
  <div class="frame" style="display:flex; flex-direction:column; justify-content:space-between; align-items:center; text-align:center;">
    <div></div>
    <div>
      <div style="font-family:'Archivo'; font-weight:600; font-size:9.5pt; letter-spacing:0.24em; color:#D9B876;">LIFETOGETHER</div>
      <div style="height:0.26in;"></div>
      <h1 class="display" style="font-size:20pt; color:#FBF8F1;">Fourteen modules now, not thirteen.</h1>
      <div style="height:0.18in;"></div>
      <p class="lede" style="max-width:4.6in; margin:0 auto;">
        The Successor &amp; Steward Journey is ready to add to the Family Journey Builder
        specification &mdash; or to prototype as its own live module first.
      </p>
      <div style="height:0.3in;"></div>
      <div style="width:30px; height:2px; background:#B98D3E; margin:0 auto;"></div>
    </div>
    <div style="font-family:'Archivo'; font-weight:500; font-size:7.4pt; letter-spacing:0.1em; color:rgba(251,248,241,0.4);">GAP ANALYSIS &amp; FRAMEWORK TRANSLATION &middot; DRAFT</div>
  </div>
</div>
''')

# =================================================================
# ASSEMBLE
# =================================================================
with open("/home/claude/build/portrait_style.css") as f:
    base_css = f.read()

html = f'''<!DOCTYPE html>
<html><head><meta charset="utf-8">
<style>{base_css}</style></head>
<body>{"".join(PAGES)}</body></html>'''

with open("/home/claude/build/advisor_gap_habits_covey.html", "w") as f:
    f.write(html)
print("Pages:", len(PAGES))
