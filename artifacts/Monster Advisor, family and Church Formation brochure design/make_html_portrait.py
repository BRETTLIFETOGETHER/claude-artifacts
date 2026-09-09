import sys
sys.path.insert(0, "/home/claude/build")
from diagrams import (ecosystem_diagram, wheel_diagram, vertical_levels, step_chain_vertical)

PAGES = []
def add(html): PAGES.append(html)

def photo(caption, extra_style=""):
    return f'''<div class="photo" style="{extra_style}">
        <div class="corner tl"></div><div class="corner br"></div>
        <div class="cap">{caption}</div>
    </div>'''

def folio(chapter, num):
    return f'''<div class="folio"><div class="thread">{chapter}</div><div>{num:02d}</div></div>'''

def track_card(name, sub, para, bullets):
    bl = "".join([f'<li>{b}</li>' for b in bullets])
    return f'''
    <div class="track-card" style="margin-bottom:0.2in;">
      <div style="font-family:'Archivo'; font-weight:700; font-size:10.8pt; letter-spacing:0.13em; color:var(--gold);">{name}</div>
      <div style="font-family:'Playfair'; font-weight:700; font-size:13.5pt; color:var(--navy); margin:0.05in 0 0.1in;">{sub}</div>
      <p style="font-family:'Inter'; font-size:9.2pt; line-height:1.5; color:var(--ink);">{para}</p>
      <ul class="track-list">{bl}</ul>
    </div>'''

# PAGE 1 — COVER
add(f'''
<div class="page navy">
  <div class="photo" style="position:absolute; inset:0; border-radius:0;">
    <div class="cap" style="right:0.68in; bottom:0.5in; left:auto; text-align:right; font-size:6.8pt;">PHOTOGRAPHY — PASTOR IN STUDY, WARM LAMPLIGHT, MANUSCRIPT OPEN</div>
  </div>
  <div style="position:absolute; inset:0; background:linear-gradient(190deg, rgba(16,30,56,0.4) 0%, rgba(16,30,56,0.88) 55%, rgba(16,30,56,0.98) 100%);"></div>
  <div class="frame" style="display:flex; flex-direction:column; justify-content:flex-end;">
    <div style="font-family:'Archivo'; font-weight:600; font-size:9pt; letter-spacing:0.24em; color:#D9B876; margin-bottom:2.2in;">A GUIDE FOR SENIOR PASTORS &amp; MINISTRY LEADERS</div>
    <h1 class="display" style="font-size:33pt; color:#FBF8F1;">The Church Formation System<span style="font-size:16pt; vertical-align:super;">™</span></h1>
    <div style="height:0.26in;"></div>
    <p style="font-family:'Playfair'; font-style:italic; font-weight:500; font-size:13.5pt; color:#D9B876; line-height:1.5;">
      Helping pastors turn sermons into curriculum &mdash; curriculum into community &mdash; and
      community into movements.
    </p>
    <div style="height:0.5in;"></div>
    <div style="display:flex; justify-content:space-between; align-items:flex-end; font-family:'Archivo'; font-weight:500; font-size:8pt; letter-spacing:0.12em; color:rgba(251,248,241,0.55);">
      <div>LIFETOGETHER.COM</div>
      <div style="width:22px; height:2px; background:#B98D3E;"></div>
    </div>
  </div>
</div>
''')

# PAGE 2 — WELCOME / CONTENTS
chapters = [
    ("The Problem", "Why sermons alone don't form disciples", 3),
    ("The Opportunity", "What becomes possible when a message keeps working", 5),
    ("The Formation Framework", "Five environments, one continuous path", 7),
    ("The Formation Masterclass", "Five tracks that train your team to build", 9),
    ("The Crawl, Walk, Run Model", "How churches grow into the system at their own pace", 12),
    ("What We Help You Build", "Every format a message can become", 14),
    ("Three Ways We Help", "Choose the level of partnership that fits your church", 16),
    ("Your Message Matters", "The legacy a system makes possible", 18),
]
rows = "".join([f'''
    <div style="display:flex; align-items:baseline; padding:0.11in 0; border-bottom:1px solid var(--line);">
      <div style="font-family:'Playfair'; font-weight:700; font-size:12pt; color:var(--navy); flex:1;">{title}</div>
      <div style="font-family:'Archivo'; font-weight:600; font-size:9pt; color:var(--gold); width:0.4in; text-align:right;">{pg:02d}</div>
    </div>
    <div style="font-family:'Inter'; font-size:8.8pt; color:var(--gray); margin-top:-0.06in; margin-bottom:0.02in;">{desc}</div>''' for title, desc, pg in chapters])

add(f'''
<div class="page">
  <div class="frame">
    <div class="eyebrow">WELCOME</div>
    <div style="height:0.24in;"></div>
    <h1 class="display" style="font-size:22pt; color:var(--navy);">Every message deserves a longer life than one Sunday.</h1>
    <div style="height:0.18in;"></div>
    <p class="lede">
      Most churches pour weeks into a single message and then let it end when the service
      does. This guide lays out a different way &mdash; a system that carries what God says on
      Sunday into groups, homes, and daily life, all week long, all year long. It is not a
      curriculum. It is not an app. It is the formation system underneath both.
    </p>
    <div style="height:0.24in;"></div>
    {rows}
  </div>
  {folio("Welcome", 2)}
</div>
''')

# PAGE 3 — THE PROBLEM (copy)
add(f'''
<div class="page">
  <div class="frame">
    <div class="eyebrow">CHAPTER ONE &mdash; THE PROBLEM</div>
    <div style="height:0.24in;"></div>
    <h1 class="display" style="font-size:24pt; color:var(--navy);">Churches don&rsquo;t lack sermons. They lack systems.</h1>
    <div style="height:0.2in;"></div>
    <p class="lede">
      Most sermons are preached once, and then forgotten. The study is done. The illustration
      lands. The room responds. And by Tuesday, very little of it remains.
    </p>
    <div style="height:0.14in;"></div>
    <p class="lede">
      Most churches build disconnected sermon series, disconnected ministries, disconnected
      groups, and disconnected discipleship &mdash; each one working hard, none of them working
      together.
    </p>
    <div style="height:0.2in;"></div>
    <div class="takeaway">
      <span class="label">The shift</span>
      There is a better way &mdash; one message, carried through a system, instead of five ministries pulling in five directions.
    </div>
    <div style="height:0.3in;"></div>
    {photo("PHOTOGRAPHY — SENIOR PASTOR PREACHING, CONGREGATION IN SOFT FOCUS", "height:3in;")}
  </div>
  {folio("The Problem", 3)}
</div>
''')

# PAGE 4 — THE PROBLEM (diagram)
add(f'''
<div class="page">
  <div class="frame">
    <div class="eyebrow">THE PROBLEM &mdash; CONTINUED</div>
    <div style="height:0.22in;"></div>
    <h1 class="display" style="font-size:21pt; color:var(--navy);">From scattered effort to one connected system.</h1>
    <div style="height:0.2in;"></div>
    <p class="lede">
      Disconnected efforts pull in five directions at once: the weekend message, small
      groups, daily habits, family life, and mission &mdash; each working hard alone. A system
      threads all five into one connected path.
    </p>
    <div style="height:0.18in;"></div>
    <div style="width:100%; height:4.6in;">{step_chain_vertical([
        ("WEEKEND", "The message is preached to the whole church."),
        ("GROUPS", "The same message is discussed in real relationship."),
        ("DAILY", "The message becomes a daily rhythm."),
        ("FAMILY", "The message shapes the home."),
        ("MISSION", "The message moves outward into action."),
    ])}</div>
    <div style="height:0.3in;"></div>
    <div class="takeaway">
      <span class="label">Takeaway</span>
      A system doesn&rsquo;t replace the sermon &mdash; it gives the sermon somewhere to go on Monday.
    </div>
  </div>
  {folio("The Problem", 4)}
</div>
''')

# PAGE 5 — THE OPPORTUNITY (copy)
opp_items = ["Small Group Curriculum", "Daily Devotionals", "Family Conversations", "Leadership Development", "Ministry Training", "Podcasts &amp; Video", "Published Books", "Future Campaigns"]
opp_col1 = "".join([f'<div class="opp-item">{x}</div>' for x in opp_items[:4]])
opp_col2 = "".join([f'<div class="opp-item">{x}</div>' for x in opp_items[4:]])
add(f'''
<div class="page">
  <div class="frame">
    <div class="eyebrow">CHAPTER TWO &mdash; THE OPPORTUNITY</div>
    <div style="height:0.22in;"></div>
    <h1 class="display" style="font-size:23pt; color:var(--navy);">Imagine every sermon becoming a library.</h1>
    <div style="height:0.16in;"></div>
    <p class="lede">
      One message, prepared once, can quietly become the source material for an entire
      season of discipleship &mdash; without adding a single hour to a pastor&rsquo;s week.
    </p>
    <div style="height:0.2in;"></div>
    <div class="pull-quote" style="font-size:13.5pt;"><span class="mark">&ldquo;</span>One message. Many expressions. A single source of truth for the whole church.<span class="mark">&rdquo;</span></div>
    <div style="height:0.3in;"></div>
    <div style="font-family:'Archivo'; font-weight:600; font-size:8.6pt; letter-spacing:0.14em; color:var(--gold); margin-bottom:0.14in;">EVERY MESSAGE CAN BECOME</div>
    <div style="display:flex; gap:0.4in;">
      <div style="flex:1;">{opp_col1}</div>
      <div style="flex:1;">{opp_col2}</div>
    </div>
  </div>
  {folio("The Opportunity", 5)}
</div>
''')

# PAGE 6 — OPPORTUNITY ECOSYSTEM DIAGRAM
add(f'''
<div class="page">
  <div class="frame">
    <div class="eyebrow">THE OPPORTUNITY &mdash; CONTINUED</div>
    <div style="height:0.18in;"></div>
    <h1 class="display" style="font-size:20pt; color:var(--navy);">The Pastor&rsquo;s Content Ecosystem</h1>
    <div style="height:0.16in;"></div>
    <div style="width:100%; height:6.4in;">{ecosystem_diagram()}</div>
    <div class="takeaway">
      <span class="label">Takeaway</span>
      Nine formats. One message. Nothing built twice.
    </div>
  </div>
  {folio("The Opportunity", 6)}
</div>
''')

# PAGE 7 — FRAMEWORK INTRO
fw_items = [
    ("Weekend", "The message is preached with clarity and conviction."),
    ("Groups", "The message is discussed in circles of real relationship."),
    ("Daily", "The message becomes a daily rhythm of reflection."),
    ("Family", "The message shapes conversation around the table."),
    ("Mission", "The message moves outward into action."),
]
fw_rows = "".join([f'''
    <div style="display:flex; gap:0.18in; padding:0.1in 0; border-bottom:1px solid var(--line);">
      <div style="font-family:'Playfair'; font-weight:700; font-size:11.5pt; color:var(--navy); width:1.1in;">{n}</div>
      <div style="font-family:'Inter'; font-size:9.2pt; color:var(--ink); flex:1;">{d}</div>
    </div>''' for n, d in fw_items])
add(f'''
<div class="page">
  <div class="frame">
    <div class="eyebrow">CHAPTER THREE &mdash; THE FRAMEWORK</div>
    <div style="height:0.22in;"></div>
    <h1 class="display" style="font-size:23pt; color:var(--navy);">Five environments. One formation path.</h1>
    <div style="height:0.18in;"></div>
    <p class="lede">
      People are formed in more than one place. The Church Formation Framework names the
      five environments where a single message keeps doing its work &mdash; long after the
      sermon ends.
    </p>
    <div style="height:0.2in;"></div>
    {fw_rows}
    <div style="height:0.24in;"></div>
    {photo("PHOTOGRAPHY — SMALL GROUP AROUND A LIVING ROOM TABLE, EVENING LIGHT", "height:2.4in;")}
  </div>
  {folio("The Framework", 7)}
</div>
''')

# PAGE 8 — FRAMEWORK WHEEL
add(f'''
<div class="page">
  <div class="frame">
    <div class="eyebrow">THE FRAMEWORK &mdash; CONTINUED</div>
    <div style="height:0.1in;"></div>
    <h1 class="display" style="font-size:21pt; color:var(--navy);">The Church Formation Wheel</h1>
    <div style="width:100%; height:6.9in;">{wheel_diagram()}</div>
    <div class="takeaway">
      <span class="label">Takeaway</span>
      The wheel turns every week &mdash; the message never stops moving through the life of the church.
    </div>
  </div>
  {folio("The Framework", 8)}
</div>
''')

# PAGE 9 — MASTERCLASS INTRO
track_bar = "".join([f'<div class="track-chip">{t}</div>' for t in ["DISCERN","DEVELOP","PRODUCE","PUBLISH","MOBILIZE"]])
add(f'''
<div class="page navy">
  <div class="frame" style="display:flex; flex-direction:column; justify-content:center;">
    <div class="eyebrow">CHAPTER FOUR &mdash; THE CHURCH FORMATION MASTERCLASS</div>
    <div style="height:0.24in;"></div>
    <h1 class="display" style="font-size:26pt; color:#FBF8F1;">Five tracks. One trained team.</h1>
    <div style="height:0.2in;"></div>
    <p class="lede">
      The Masterclass is how a church staff learns to build inside the system &mdash; not just
      use it. Each track hands your team a discipline they can return to with every future
      message.
    </p>
    <div style="height:0.34in;"></div>
    <div style="display:grid; grid-template-columns:1fr 1fr; gap:0.14in;">{track_bar}</div>
  </div>
  {folio("The Masterclass", 9)}
</div>
''')

# PAGE 10 — MASTERCLASS TRACKS 1-3
tracks_1_3 = [
    ("DISCERN", "Hearing the message clearly", "Before anything is built, a team learns to identify the single true center of a message &mdash; the one idea everything else will serve.",
     ["Name the one idea worth building around", "Separate the message from the moment", "Identify the Scripture that carries it", "Spot where it touches real daily life"]),
    ("DEVELOP", "Shaping it into a path", "A message becomes a multi-week arc with its own structure, pacing, and emotional and spiritual logic &mdash; not just a topic.",
     ["Map the week-by-week arc", "Set the pace between conviction and rest", "Build in the turn toward application", "Design the invitation at the end"]),
    ("PRODUCE", "Building every format", "The arc becomes curriculum, devotionals, and training &mdash; each shaped for how it will actually be used.",
     ["Write small group discussion guides", "Draft daily devotional content", "Build a leader training kit", "Prepare family conversation prompts"]),
]
add(f'''
<div class="page">
  <div class="frame">
    <div class="eyebrow">THE MASTERCLASS &mdash; TRACKS ONE THROUGH THREE</div>
    <div style="height:0.2in;"></div>
    {"".join([track_card(*t) for t in tracks_1_3])}
  </div>
  {folio("The Masterclass", 10)}
</div>
''')

# PAGE 11 — MASTERCLASS TRACKS 4-5 + quote
tracks_4_5 = [
    ("PUBLISH", "Packaging it with excellence", "The finished campaign is designed, proofed, and formatted so it feels like a resource, not a handout.",
     ["Design a cover and visual identity", "Typeset every printed and digital piece", "Proof theology, tone, and Scripture", "Prepare it for licensing or release"]),
    ("MOBILIZE", "Getting it into hands", "A campaign only forms people if it launches well &mdash; so the track ends with a real activation plan, not just a finished file.",
     ["Build the launch and promotion plan", "Train leaders to carry the content well", "Prepare the pulpit announcement path", "Plan the on-ramp to what comes next"]),
]
add(f'''
<div class="page">
  <div class="frame">
    <div class="eyebrow">THE MASTERCLASS &mdash; TRACKS FOUR AND FIVE</div>
    <div style="height:0.2in;"></div>
    {"".join([track_card(*t) for t in tracks_4_5])}
    <div style="height:0.1in;"></div>
    <div class="pull-quote" style="font-size:14pt;">Your team doesn&rsquo;t just receive curriculum. <span class="mark">They learn to build it.</span></div>
  </div>
  {folio("The Masterclass", 11)}
</div>
''')

# PAGE 12 — CRAWL WALK RUN — vertical levels
crawl_levels = [
    ("1", "Use Ours", "Launch proven Lifetogether campaigns as they are."),
    ("2", "Customize Ours", "Adapt content and language to your church's voice."),
    ("3", "Build Yours", "Create original campaigns from your pastor's own messages."),
    ("4", "Publish Yours", "Package your campaigns for other churches to license."),
    ("5", "Multiply Yours", "Train other pastors to build within your formation system."),
]
add(f'''
<div class="page">
  <div class="frame">
    <div class="eyebrow">CHAPTER FIVE &mdash; THE CRAWL, WALK, RUN MODEL</div>
    <div style="height:0.2in;"></div>
    <h1 class="display" style="font-size:21pt; color:var(--navy);">Every church starts where it is, and grows from there.</h1>
    <div style="height:0.16in;"></div>
    <p class="lede">
      No church is asked to arrive fully built. The model has five levels, and most churches
      move through them over time &mdash; at whatever pace fits their staff, calendar, and
      capacity.
    </p>
    <div style="width:100%; height:5.9in;">{vertical_levels(crawl_levels)}</div>
  </div>
  {folio("Crawl, Walk, Run", 12)}
</div>
''')

# PAGE 13 — CRAWL WALK RUN — timeline + quote/takeaway
add(f'''
<div class="page">
  <div class="frame">
    <div class="eyebrow">THE CRAWL, WALK, RUN MODEL &mdash; CONTINUED</div>
    <div style="height:0.2in;"></div>
    <h1 class="display" style="font-size:20pt; color:var(--navy);">A typical 18 to 24 month formation roadmap</h1>
    <div style="height:0.2in;"></div>
    <div style="width:100%; height:5.7in;">{step_chain_vertical([
        ("MO. 1&ndash;3", "Launch your first campaign with our library."),
        ("MO. 4&ndash;9", "Customize campaigns to your church's voice."),
        ("MO. 10&ndash;15", "Build original campaigns from your own messages."),
        ("MO. 16&ndash;20", "Publish your campaigns for other churches."),
        ("MO. 21&ndash;24", "Train other pastors inside your formation system."),
    ])}</div>
    <div style="height:0.16in;"></div>
    <div class="takeaway">
      <span class="label">Practical takeaway</span>
      Most churches begin at Level One with a licensed campaign, and don&rsquo;t build original content until their team has run the system at least once.
    </div>
  </div>
  {folio("Crawl, Walk, Run", 13)}
</div>
''')

# PAGE 14 — WHAT WE HELP CHURCHES BUILD
build_items = ["21-Day Challenges", "30-Day Journeys", "40-Day Campaigns", "Small Group Studies", "Sermon Series", "Leader Training", "Devotionals", "Family Resources", "Books", "Video Studies", "Digital Experiences", "Membership Courses", "Ministry Systems"]
grid_cells = "".join([f'<div class="build-cell">{b}</div>' for b in build_items[:-1]])
grid_cells += f'<div class="build-cell wide"><span class="rule"></span>{build_items[-1]}<span class="rule"></span></div>'
add(f'''
<div class="page">
  <div class="frame">
    <div class="eyebrow">CHAPTER SIX &mdash; WHAT WE HELP YOU BUILD</div>
    <div style="height:0.2in;"></div>
    <h1 class="display" style="font-size:22pt; color:var(--navy);">Every format a message can become.</h1>
    <div style="height:0.1in;"></div>
    <p class="lede">Everything here is built from one thing: the pastor&rsquo;s own message.</p>
    <div style="height:0.26in;"></div>
    <div class="build-grid">{grid_cells}</div>
  </div>
  {folio("What We Help You Build", 14)}
</div>
''')

# PAGE 15 — MESSAGE -> MOVEMENT diagram + quote
add(f'''
<div class="page navy">
  <div class="frame">
    <div class="eyebrow">WHAT WE HELP YOU BUILD &mdash; CONTINUED</div>
    <div style="height:0.18in;"></div>
    <h1 class="display" style="font-size:22pt; color:#FBF8F1;">Message &rarr; Movement</h1>
    <div style="width:100%; height:5.2in;">{step_chain_vertical([
        ("MESSAGE", "One message, studied and preached with care."),
        ("CURRICULUM", "Shaped into formats groups and families can use."),
        ("COMMUNITY", "Lived out together, in real relationship."),
        ("MOVEMENT", "Carried into lasting, visible change."),
    ])}</div>
    <div style="height:0.16in;"></div>
    <div class="pull-quote">Everything built from the pastor&rsquo;s own message. <span class="mark">Nothing built from scratch, twice.</span></div>
  </div>
  {folio("What We Help You Build", 15)}
</div>
''')

# PAGE 16 — THREE WAYS WE HELP (intro cards)
offers = [
    ("Campaign Builder Intensive", "A six-week planning process", "For a team ready to shape their first original campaign from a pastor&rsquo;s existing message."),
    ("90-Day Accelerator", "From idea to launch", "For a church ready to move quickly &mdash; from a first conversation to a fully launched campaign in one season."),
    ("Church Formation Partnership", "A twelve-month coaching relationship", "For a church building toward Level Four or Five &mdash; publishing and multiplying its own formation system."),
]
offer_cards = "".join([f'''
    <div class="offer-card" style="margin-bottom:0.2in;">
      <div style="width:30px; height:2px; background:var(--gold); margin-bottom:0.16in;"></div>
      <div style="font-family:'Playfair'; font-weight:700; font-size:14.5pt; color:var(--navy); line-height:1.2;">{name}</div>
      <div style="font-family:'Archivo'; font-weight:600; font-size:8.3pt; letter-spacing:0.1em; text-transform:uppercase; color:var(--gold); margin:0.08in 0 0.14in;">{sub}</div>
      <p style="font-family:'Inter'; font-size:9.6pt; line-height:1.55; color:var(--ink);">{desc}</p>
    </div>''' for name, sub, desc in offers])
add(f'''
<div class="page">
  <div class="frame">
    <div class="eyebrow">CHAPTER SEVEN &mdash; THREE WAYS WE HELP</div>
    <div style="height:0.2in;"></div>
    <h1 class="display" style="font-size:22pt; color:var(--navy);">Choose the level of partnership that fits your church.</h1>
    <div style="height:0.26in;"></div>
    {offer_cards}
  </div>
  {folio("Three Ways We Help", 16)}
</div>
''')

# PAGE 17 — COMPARISON CHART
compare_rows = [
    ("Length", "Six weeks", "One season (about 90 days)", "Twelve months"),
    ("Best for", "A first original campaign", "A fast, full launch", "Building toward Level Four or Five"),
    ("Format", "Guided planning workshops", "Hands-on build &amp; launch support", "Ongoing coaching &amp; team training"),
    ("You leave with", "One completed campaign outline", "One fully launched campaign", "A trained team and a repeatable system"),
]
def compare_row(label, a, b, c, header=False):
    cls = "cmp-head" if header else "cmp-row"
    return f'''<div class="{cls}"><div class="cmp-cell cmp-label">{label}</div><div class="cmp-cell">{a}</div><div class="cmp-cell">{b}</div><div class="cmp-cell">{c}</div></div>'''
header_row = compare_row("", "Intensive", "Accelerator", "Partnership", header=True)
body_rows = "".join([compare_row(l,a,b,c) for l,a,b,c in compare_rows])
add(f'''
<div class="page">
  <div class="frame">
    <div class="eyebrow">THREE WAYS WE HELP &mdash; CONTINUED</div>
    <div style="height:0.22in;"></div>
    <h1 class="display" style="font-size:21pt; color:var(--navy);">At a glance</h1>
    <div style="height:0.26in;"></div>
    <div class="cmp-table">{header_row}{body_rows}</div>
  </div>
  {folio("Three Ways We Help", 17)}
</div>
''')

# PAGE 18 — CLOSING: YOUR MESSAGE MATTERS
add(f'''
<div class="page navy">
  <div class="photo" style="position:absolute; inset:0; border-radius:0;">
    <div class="cap" style="right:0.68in; bottom:0.5in; left:auto; text-align:right; font-size:6.8pt;">PHOTOGRAPHY — PASTOR &amp; FAMILY, GOLDEN HOUR, CHURCH LOBBY IN SOFT FOCUS</div>
  </div>
  <div style="position:absolute; inset:0; background:linear-gradient(190deg, rgba(16,30,56,0.4) 0%, rgba(16,30,56,0.9) 55%, rgba(16,30,56,0.98) 100%);"></div>
  <div class="frame" style="display:flex; flex-direction:column; justify-content:flex-end;">
    <div class="eyebrow">CHAPTER EIGHT &mdash; YOUR MESSAGE MATTERS</div>
    <div style="height:0.24in;"></div>
    <h1 class="display" style="font-size:24pt; color:#FBF8F1;">Your greatest sermons deserve more than one Sunday.</h1>
    <div style="height:0.2in;"></div>
    <p class="lede">
      They deserve to become a pathway that forms disciples, strengthens families, equips
      leaders, and leaves a legacy that outlives your ministry.
    </p>
  </div>
  {folio("Your Message Matters", 18)}
</div>
''')

# PAGE 19 — BACK COVER
add(f'''
<div class="page navy">
  <div class="frame" style="display:flex; flex-direction:column; justify-content:space-between; align-items:center; text-align:center;">
    <div></div>
    <div>
      <div style="font-family:'Archivo'; font-weight:600; font-size:9.5pt; letter-spacing:0.28em; color:#D9B876;">LIFETOGETHER</div>
      <div style="height:0.26in;"></div>
      <h1 class="display" style="font-size:22pt; color:#FBF8F1;">Let&rsquo;s build it together.</h1>
      <div style="height:0.18in;"></div>
      <p class="lede" style="max-width:4in; margin:0 auto;">
        You don&rsquo;t have to build the system alone &mdash; and you don&rsquo;t have to build it all at once.
      </p>
      <div style="height:0.34in;"></div>
      <div style="width:30px; height:2px; background:#B98D3E; margin:0 auto;"></div>
      <div style="height:0.2in;"></div>
      <div style="font-family:'Archivo'; font-weight:500; font-size:9pt; letter-spacing:0.08em; color:rgba(251,248,241,0.75);">LIFETOGETHER.COM &nbsp;&middot;&nbsp; BRETT@LIFETOGETHER.COM</div>
    </div>
    <div style="font-family:'Archivo'; font-weight:500; font-size:7.6pt; letter-spacing:0.12em; color:rgba(251,248,241,0.4);">THE CHURCH FORMATION SYSTEM&trade;</div>
  </div>
</div>
''')

with open("/home/claude/build/portrait_style.css") as f:
    base_css = f.read()

html = f'''<!DOCTYPE html>
<html><head><meta charset="utf-8">
<style>{base_css}</style></head>
<body>{"".join(PAGES)}</body></html>'''

with open("/home/claude/build/brochure_portrait.html", "w") as f:
    f.write(html)
print("Pages:", len(PAGES))
