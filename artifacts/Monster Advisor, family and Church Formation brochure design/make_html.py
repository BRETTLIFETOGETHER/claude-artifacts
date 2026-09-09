import sys
sys.path.insert(0, "/home/claude/build")
from diagrams import (chain_diagram, ecosystem_diagram, wheel_diagram,
                       staircase_diagram, message_movement_diagram, timeline_diagram)

PAGES = []

def add(html):
    PAGES.append(html)

def photo(caption, extra_style=""):
    return f'''<div class="photo" style="{extra_style}">
        <div class="corner tl"></div><div class="corner br"></div>
        <div class="cap">{caption}</div>
    </div>'''

def folio(chapter, num):
    return f'''<div class="folio">
        <div class="thread">{chapter}</div>
        <div>{num:02d}</div>
    </div>'''

# =================================================================
# PAGE 1 — COVER
# =================================================================
add(f'''
<div class="page navy">
  <div class="photo" style="position:absolute; inset:0; border-radius:0;">
    <div class="cap" style="right:0.9in; bottom:0.6in; left:auto; text-align:right; font-size:7.6pt;">PHOTOGRAPHY — PASTOR IN STUDY, WARM LAMPLIGHT, MANUSCRIPT OPEN</div>
  </div>
  <div style="position:absolute; inset:0; background:linear-gradient(100deg, rgba(16,30,56,0.97) 0%, rgba(16,30,56,0.88) 30%, rgba(16,30,56,0.35) 62%, rgba(16,30,56,0.08) 100%);"></div>
  <div class="frame" style="display:flex; flex-direction:column; justify-content:space-between;">
    <div style="font-family:'Archivo'; font-weight:600; font-size:11pt; letter-spacing:0.34em; color:#D9B876;">LIFETOGETHER</div>
    <div style="max-width:6.6in;">
      <div style="font-family:'Archivo'; font-weight:600; font-size:10.5pt; letter-spacing:0.24em; color:#D9B876; margin-bottom:0.32in;">A GUIDE FOR SENIOR PASTORS &amp; MINISTRY LEADERS</div>
      <h1 class="display" style="font-size:52pt; color:#FBF8F1;">The Church<br/>Formation System<span style="font-size:22pt; vertical-align:super;">™</span></h1>
      <div style="height:0.34in;"></div>
      <p style="font-family:'Playfair'; font-style:italic; font-weight:500; font-size:16.5pt; color:#D9B876; line-height:1.5; max-width:5.6in;">
        Helping pastors turn sermons into curriculum &mdash; curriculum into community &mdash; and community into movements.
      </p>
    </div>
    <div style="display:flex; justify-content:space-between; align-items:flex-end; font-family:'Archivo'; font-weight:500; font-size:9pt; letter-spacing:0.14em; color:rgba(251,248,241,0.55);">
      <div>LIFETOGETHER.COM</div>
      <div style="width:26px; height:2px; background:#B98D3E;"></div>
    </div>
  </div>
</div>
''')

# =================================================================
# PAGE 2 — WELCOME / CONTENTS
# =================================================================
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
rows = ""
for title, desc, pg in chapters:
    rows += f'''
    <div style="display:flex; align-items:baseline; padding:0.145in 0; border-bottom:1px solid var(--line);">
      <div style="font-family:'Playfair'; font-weight:700; font-size:15pt; color:var(--navy); width:3.1in;">{title}</div>
      <div style="flex:1; font-family:'Inter'; font-size:10.3pt; color:var(--gray);">{desc}</div>
      <div style="font-family:'Archivo'; font-weight:600; font-size:10pt; color:var(--gold); width:0.5in; text-align:right;">{pg:02d}</div>
    </div>'''

add(f'''
<div class="page">
  <div class="frame">
    <div class="eyebrow">WELCOME</div>
    <div style="height:0.34in;"></div>
    <div style="display:flex; gap:0.7in;">
      <div style="width:4.7in;">
        <h1 class="display" style="font-size:32pt; color:var(--navy);">Every message deserves<br/>a longer life than one Sunday.</h1>
        <div style="height:0.24in;"></div>
        <p class="lede" style="max-width:4.5in;">
          Most churches pour weeks into a single message and then let it end when the service does.
          This guide lays out a different way &mdash; a system that carries what God says on Sunday into
          groups, homes, and daily life, all week long, all year long.
        </p>
        <div style="height:0.22in;"></div>
        <p class="lede" style="max-width:4.5in;">
          It is not a curriculum. It is not an app. It is the formation system underneath both &mdash;
          built with pastors, for pastors, so no one has to build it alone.
        </p>
      </div>
      <div style="flex:1;">
        {rows}
      </div>
    </div>
  </div>
  {folio("Welcome", 2)}
</div>
''')

# =================================================================
# PAGE 3 — THE PROBLEM (copy)
# =================================================================
add(f'''
<div class="page">
  <div class="frame" style="display:flex; gap:0.75in;">
    <div style="width:4.3in; display:flex; flex-direction:column; justify-content:center;">
      <div class="eyebrow">CHAPTER ONE &mdash; THE PROBLEM</div>
      <div style="height:0.3in;"></div>
      <h1 class="display" style="font-size:34pt; color:var(--navy);">Churches don&rsquo;t lack sermons.<br/>They lack systems.</h1>
      <div style="height:0.26in;"></div>
      <p class="lede">
        Most sermons are preached once, and then forgotten. The study is done. The illustration lands.
        The room responds. And by Tuesday, very little of it remains.
      </p>
      <div style="height:0.16in;"></div>
      <p class="lede">
        Most churches build disconnected sermon series, disconnected ministries, disconnected groups,
        and disconnected discipleship &mdash; each one working hard, none of them working together.
      </p>
      <div style="height:0.22in;"></div>
      <div class="takeaway">
        <span class="label">The shift</span>
        There is a better way &mdash; one message, carried through a system, instead of five ministries pulling in five directions.
      </div>
    </div>
    <div style="flex:1;">
      {photo("PHOTOGRAPHY — SENIOR PASTOR PREACHING, CONGREGATION IN SOFT FOCUS", "height:100%;")}
    </div>
  </div>
  {folio("The Problem", 3)}
</div>
''')

# =================================================================
# PAGE 4 — THE PROBLEM (diagram)
# =================================================================
add(f'''
<div class="page">
  <div class="frame">
    <div class="eyebrow">THE PROBLEM &mdash; CONTINUED</div>
    <div style="height:0.28in;"></div>
    <h1 class="display" style="font-size:27pt; color:var(--navy); max-width:8in;">From scattered effort to one connected system.</h1>
    <div style="height:0.32in;"></div>
    <div style="width:100%; height:4.1in;">{chain_diagram()}</div>
    <div style="height:0.18in;"></div>
    <div class="takeaway">
      <span class="label">Takeaway</span>
      A system doesn&rsquo;t replace the sermon &mdash; it gives the sermon somewhere to go on Monday.
    </div>
  </div>
  {folio("The Problem", 4)}
</div>
''')

# =================================================================
# PAGE 5 — THE OPPORTUNITY (copy)
# =================================================================
opp_items = [
    "Small Group Curriculum", "Daily Devotionals", "Family Conversations",
    "Leadership Development", "Ministry Training", "Podcasts &amp; Video",
    "Published Books", "Future Campaigns",
]
opp_col1 = "".join([f'<div class="opp-item">{x}</div>' for x in opp_items[:4]])
opp_col2 = "".join([f'<div class="opp-item">{x}</div>' for x in opp_items[4:]])
opp_label = '<div style="font-family:\'Archivo\'; font-weight:600; font-size:9.5pt; letter-spacing:0.16em; color:var(--gold); margin-bottom:0.16in;">EVERY MESSAGE CAN BECOME</div>'

add(f'''
<div class="page">
  <div class="frame">
    <div class="eyebrow">CHAPTER TWO &mdash; THE OPPORTUNITY</div>
    <div style="height:0.3in;"></div>
    <div style="display:flex; gap:0.75in;">
      <div style="width:4.5in;">
        <h1 class="display" style="font-size:32pt; color:var(--navy);">Imagine every sermon<br/>becoming a library.</h1>
        <div style="height:0.24in;"></div>
        <p class="lede">
          One message, prepared once, can quietly become the source material for an entire season
          of discipleship &mdash; without adding a single hour to a pastor&rsquo;s week.
        </p>
        <div style="height:0.26in;"></div>
        <div class="pull-quote"><span class="mark">&ldquo;</span>One message. Many expressions. A single source of truth for the whole church.<span class="mark">&rdquo;</span></div>
      </div>
      <div style="flex:1; display:flex; flex-direction:column; justify-content:center;">
        {opp_label}
        <div style="display:flex; gap:0.4in;">
          <div style="flex:1; display:flex; flex-direction:column;">{opp_col1}</div>
          <div style="flex:1; display:flex; flex-direction:column;">{opp_col2}</div>
        </div>
      </div>
    </div>
  </div>
  {folio("The Opportunity", 5)}
</div>
''')

# =================================================================
# PAGE 6 — OPPORTUNITY ECOSYSTEM DIAGRAM
# =================================================================
add(f'''
<div class="page">
  <div class="frame">
    <div class="eyebrow">THE OPPORTUNITY &mdash; CONTINUED</div>
    <div style="height:0.22in;"></div>
    <div style="display:flex; justify-content:space-between; align-items:flex-end;">
      <h1 class="display" style="font-size:27pt; color:var(--navy);">The Pastor&rsquo;s Content Ecosystem</h1>
      <div class="takeaway" style="max-width:2.6in;">
        <span class="label">Takeaway</span>
        Nine formats. One message. Nothing built twice.
      </div>
    </div>
    <div style="height:0.1in;"></div>
    <div style="width:100%; height:4.75in;">{ecosystem_diagram()}</div>
  </div>
  {folio("The Opportunity", 6)}
</div>
''')

# =================================================================
# PAGE 7 — FRAMEWORK INTRO
# =================================================================
fw_items = [
    ("Weekend", "The message is preached with clarity and conviction."),
    ("Groups", "The message is discussed in circles of real relationship."),
    ("Daily", "The message becomes a daily rhythm of reflection."),
    ("Family", "The message shapes conversation around the table."),
    ("Mission", "The message moves outward into action."),
]
fw_rows = "".join([f'''
    <div style="display:flex; gap:0.22in; padding:0.13in 0; border-bottom:1px solid var(--line);">
      <div style="font-family:'Playfair'; font-weight:700; font-size:13.5pt; color:var(--navy); width:1.35in;">{n}</div>
      <div style="font-family:'Inter'; font-size:10.3pt; color:var(--ink); flex:1;">{d}</div>
    </div>''' for n, d in fw_items])

add(f'''
<div class="page">
  <div class="frame" style="display:flex; gap:0.75in;">
    <div style="width:4.5in; display:flex; flex-direction:column; justify-content:center;">
      <div class="eyebrow">CHAPTER THREE &mdash; THE FRAMEWORK</div>
      <div style="height:0.28in;"></div>
      <h1 class="display" style="font-size:31pt; color:var(--navy);">Five environments.<br/>One formation path.</h1>
      <div style="height:0.22in;"></div>
      <p class="lede">
        People are formed in more than one place. The Church Formation Framework names the five
        environments where a single message keeps doing its work &mdash; long after the sermon ends.
      </p>
      <div style="height:0.22in;"></div>
      {fw_rows}
    </div>
    <div style="flex:1;">
      {photo("PHOTOGRAPHY — SMALL GROUP AROUND A LIVING ROOM TABLE, EVENING LIGHT", "height:100%;")}
    </div>
  </div>
  {folio("The Framework", 7)}
</div>
''')

# =================================================================
# PAGE 8 — FRAMEWORK WHEEL
# =================================================================
add(f'''
<div class="page">
  <div class="frame">
    <div class="eyebrow">THE FRAMEWORK &mdash; CONTINUED</div>
    <div style="height:0.1in;"></div>
    <h1 class="display" style="font-size:27pt; color:var(--navy);">The Church Formation Wheel</h1>
    <div style="width:100%; height:5.2in;">{wheel_diagram()}</div>
    <div class="takeaway">
      <span class="label">Takeaway</span>
      The wheel turns every week &mdash; the message never stops moving through the life of the church.
    </div>
  </div>
  {folio("The Framework", 8)}
</div>
''')

# =================================================================
# PAGE 9 — MASTERCLASS INTRO
# =================================================================
track_bar = "".join([f'<div class="track-chip">{t}</div>' for t in ["DISCERN","DEVELOP","PRODUCE","PUBLISH","MOBILIZE"]])
add(f'''
<div class="page navy">
  <div class="frame" style="display:flex; flex-direction:column; justify-content:center;">
    <div class="eyebrow">CHAPTER FOUR &mdash; THE CHURCH FORMATION MASTERCLASS</div>
    <div style="height:0.3in;"></div>
    <h1 class="display" style="font-size:34pt; color:#FBF8F1; max-width:7.5in;">Five tracks.<br/>One trained team.</h1>
    <div style="height:0.26in;"></div>
    <p class="lede" style="max-width:6.3in;">
      The Masterclass is how a church staff learns to build inside the system &mdash; not just use it.
      Each track hands your team a discipline they can return to with every future message.
    </p>
    <div style="height:0.4in;"></div>
    <div style="display:flex; gap:0.14in;">{track_bar}</div>
  </div>
  {folio("The Masterclass", 9)}
</div>
''')

# =================================================================
# PAGE 10 — MASTERCLASS TRACKS 1-3
# =================================================================
tracks_1_3 = [
    ("DISCERN", "Hearing the message clearly", "Before anything is built, a team learns to identify the single true center of a message &mdash; the one idea everything else will serve.",
     ["Name the one idea worth building around", "Separate the message from the moment", "Identify the Scripture that carries it", "Spot where it touches real daily life"]),
    ("DEVELOP", "Shaping it into a path", "A message becomes a multi-week arc with its own structure, pacing, and emotional and spiritual logic &mdash; not just a topic.",
     ["Map the week-by-week arc", "Set the pace between conviction and rest", "Build in the turn toward application", "Design the invitation at the end"]),
    ("PRODUCE", "Building every format", "The arc becomes curriculum, devotionals, and training &mdash; each shaped for how it will actually be used.",
     ["Write small group discussion guides", "Draft daily devotional content", "Build a leader training kit", "Prepare family conversation prompts"]),
]
def track_card(name, sub, para, bullets):
    bl = "".join([f'<li>{b}</li>' for b in bullets])
    return f'''
    <div class="track-card">
      <div style="font-family:'Archivo'; font-weight:700; font-size:12.5pt; letter-spacing:0.16em; color:var(--gold);">{name}</div>
      <div style="font-family:'Playfair'; font-weight:700; font-size:15.5pt; color:var(--navy); margin:0.06in 0 0.14in;">{sub}</div>
      <p style="font-family:'Inter'; font-size:9.7pt; line-height:1.55; color:var(--ink); min-height:0.95in;">{para}</p>
      <ul class="track-list">{bl}</ul>
    </div>'''

cards_1_3 = "".join([track_card(*t) for t in tracks_1_3])
add(f'''
<div class="page">
  <div class="frame">
    <div class="eyebrow">THE MASTERCLASS &mdash; TRACKS ONE THROUGH THREE</div>
    <div style="height:0.26in;"></div>
    <div style="display:flex; gap:0.42in;">{cards_1_3}</div>
  </div>
  {folio("The Masterclass", 10)}
</div>
''')

# =================================================================
# PAGE 11 — MASTERCLASS TRACKS 4-5 + quote
# =================================================================
tracks_4_5 = [
    ("PUBLISH", "Packaging it with excellence", "The finished campaign is designed, proofed, and formatted so it feels like a resource, not a handout.",
     ["Design a cover and visual identity", "Typeset every printed and digital piece", "Proof theology, tone, and Scripture", "Prepare it for licensing or release"]),
    ("MOBILIZE", "Getting it into hands", "A campaign only forms people if it launches well &mdash; so the track ends with a real activation plan, not just a finished file.",
     ["Build the launch and promotion plan", "Train leaders to carry the content well", "Prepare the pulpit announcement path", "Plan the on-ramp to what comes next"]),
]
cards_4_5 = "".join([track_card(*t) for t in tracks_4_5])
add(f'''
<div class="page">
  <div class="frame">
    <div class="eyebrow">THE MASTERCLASS &mdash; TRACKS FOUR AND FIVE</div>
    <div style="height:0.26in;"></div>
    <div style="display:flex; gap:0.5in;">
      <div style="width:6.5in; display:flex; gap:0.42in;">{cards_4_5}</div>
      <div style="flex:1; display:flex; align-items:center;">
        <div class="pull-quote">Your team doesn&rsquo;t just receive curriculum. <span class="mark">They learn to build it.</span></div>
      </div>
    </div>
  </div>
  {folio("The Masterclass", 11)}
</div>
''')

# =================================================================
# PAGE 12 — CRAWL WALK RUN — staircase
# =================================================================
add(f'''
<div class="page">
  <div class="frame">
    <div class="eyebrow">CHAPTER FIVE &mdash; THE CRAWL, WALK, RUN MODEL</div>
    <div style="height:0.22in;"></div>
    <h1 class="display" style="font-size:27pt; color:var(--navy); max-width:8in;">Every church starts where it is &mdash; and grows from there.</h1>
    <div style="height:0.22in;"></div>
    <p class="lede" style="max-width:8in;">
      No church is asked to arrive fully built. The model has five levels, and most churches move
      through them over time &mdash; at whatever pace fits their staff, their calendar, and their capacity.
    </p>
    <div style="width:100%; height:4.15in;">{staircase_diagram()}</div>
  </div>
  {folio("Crawl, Walk, Run", 12)}
</div>
''')

# =================================================================
# PAGE 13 — CRAWL WALK RUN — timeline + quote/takeaway
# =================================================================
add(f'''
<div class="page">
  <div class="frame">
    <div class="eyebrow">THE CRAWL, WALK, RUN MODEL &mdash; CONTINUED</div>
    <div style="height:0.22in;"></div>
    <h1 class="display" style="font-size:26pt; color:var(--navy);">A typical 18 to 24 month formation roadmap</h1>
    <div style="height:0.28in;"></div>
    <div style="width:100%; height:2.5in;">{timeline_diagram()}</div>
    <div style="height:0.3in;"></div>
    <div style="display:flex; gap:0.75in; align-items:flex-start;">
      <div class="pull-quote" style="flex:1;">You don&rsquo;t need to build the whole system in year one. <span class="mark">You just need to take the next step.</span></div>
      <div class="takeaway" style="width:3in;">
        <span class="label">Practical takeaway</span>
        Most churches begin at Level One with a licensed campaign, and don&rsquo;t build original content until their team has run the system at least once.
      </div>
    </div>
  </div>
  {folio("Crawl, Walk, Run", 13)}
</div>
''')

# =================================================================
# PAGE 14 — WHAT WE HELP CHURCHES BUILD
# =================================================================
build_items = [
    "21-Day Challenges", "30-Day Journeys", "40-Day Campaigns", "Small Group Studies",
    "Sermon Series", "Leader Training", "Devotionals", "Family Resources",
    "Books", "Video Studies", "Digital Experiences", "Membership Courses", "Ministry Systems",
]
grid_cells = "".join([f'<div class="build-cell">{b}</div>' for b in build_items[:-1]])
grid_cells += f'<div class="build-cell wide"><span class="rule"></span>{build_items[-1]}<span class="rule"></span></div>'
add(f'''
<div class="page">
  <div class="frame">
    <div class="eyebrow">CHAPTER SIX &mdash; WHAT WE HELP YOU BUILD</div>
    <div style="height:0.24in;"></div>
    <h1 class="display" style="font-size:29pt; color:var(--navy); max-width:8in;">Every format a message can become.</h1>
    <div style="height:0.1in;"></div>
    <p class="lede" style="max-width:8in;">Everything here is built from one thing: the pastor&rsquo;s own message.</p>
    <div style="height:0.3in;"></div>
    <div class="build-grid">{grid_cells}</div>
  </div>
  {folio("What We Help You Build", 14)}
</div>
''')

# =================================================================
# PAGE 15 — MESSAGE -> MOVEMENT diagram + quote
# =================================================================
add(f'''
<div class="page navy">
  <div class="frame">
    <div class="eyebrow">WHAT WE HELP YOU BUILD &mdash; CONTINUED</div>
    <div style="height:0.2in;"></div>
    <h1 class="display" style="font-size:27pt; color:#FBF8F1;">Message &rarr; Movement</h1>
    <div style="width:100%; height:2.6in;">{message_movement_diagram()}</div>
    <div style="height:0.15in;"></div>
    <div class="pull-quote" style="max-width:7.5in;">Everything built from the pastor&rsquo;s own message. <span class="mark">Nothing built from scratch, twice.</span></div>
  </div>
  {folio("What We Help You Build", 15)}
</div>
''')

# =================================================================
# PAGE 16 — THREE WAYS WE HELP (intro cards)
# =================================================================
offers = [
    ("Campaign Builder Intensive", "A six-week planning process", "For a team ready to shape their first original campaign from a pastor&rsquo;s existing message."),
    ("90-Day Accelerator", "From idea to launch", "For a church ready to move quickly &mdash; from a first conversation to a fully launched campaign in one season."),
    ("Church Formation Partnership", "A twelve-month coaching relationship", "For a church building toward Level Four or Five &mdash; publishing and multiplying its own formation system."),
]
offer_cards = "".join([f'''
    <div class="offer-card">
      <div style="width:34px; height:2px; background:var(--gold); margin-bottom:0.2in;"></div>
      <div style="font-family:'Playfair'; font-weight:700; font-size:17pt; color:var(--navy); line-height:1.2;">{name}</div>
      <div style="font-family:'Archivo'; font-weight:600; font-size:9.3pt; letter-spacing:0.1em; text-transform:uppercase; color:var(--gold); margin:0.1in 0 0.18in;">{sub}</div>
      <p style="font-family:'Inter'; font-size:10pt; line-height:1.55; color:var(--ink);">{desc}</p>
    </div>''' for name, sub, desc in offers])

add(f'''
<div class="page">
  <div class="frame">
    <div class="eyebrow">CHAPTER SEVEN &mdash; THREE WAYS WE HELP</div>
    <div style="height:0.22in;"></div>
    <h1 class="display" style="font-size:29pt; color:var(--navy); max-width:8in;">Choose the level of partnership that fits your church.</h1>
    <div style="height:0.3in;"></div>
    <div style="display:flex; gap:0.4in;">{offer_cards}</div>
  </div>
  {folio("Three Ways We Help", 16)}
</div>
''')

# =================================================================
# PAGE 17 — COMPARISON CHART
# =================================================================
compare_rows = [
    ("Length", "Six weeks", "One season (about 90 days)", "Twelve months"),
    ("Best for", "A first original campaign", "A fast, full launch", "Building toward Level Four or Five"),
    ("Format", "Guided planning workshops", "Hands-on build &amp; launch support", "Ongoing coaching &amp; team training"),
    ("You leave with", "One completed campaign outline", "One fully launched campaign", "A trained team and a repeatable system"),
]
def compare_row(label, a, b, c, header=False):
    cls = "cmp-head" if header else "cmp-row"
    return f'''
    <div class="{cls}">
      <div class="cmp-cell cmp-label">{label}</div>
      <div class="cmp-cell">{a}</div>
      <div class="cmp-cell">{b}</div>
      <div class="cmp-cell">{c}</div>
    </div>'''

header_row = compare_row("", "Campaign Builder<br/>Intensive", "90-Day<br/>Accelerator", "Church Formation<br/>Partnership", header=True)
body_rows = "".join([compare_row(l,a,b,c) for l,a,b,c in compare_rows])

add(f'''
<div class="page">
  <div class="frame">
    <div class="eyebrow">THREE WAYS WE HELP &mdash; CONTINUED</div>
    <div style="height:0.24in;"></div>
    <h1 class="display" style="font-size:26pt; color:var(--navy);">At a glance</h1>
    <div style="height:0.3in;"></div>
    <div class="cmp-table">
      {header_row}
      {body_rows}
    </div>
  </div>
  {folio("Three Ways We Help", 17)}
</div>
''')

# =================================================================
# PAGE 18 — CLOSING: YOUR MESSAGE MATTERS
# =================================================================
add(f'''
<div class="page navy">
  <div class="photo" style="position:absolute; inset:0; border-radius:0;">
    <div class="cap" style="right:0.9in; bottom:0.6in; left:auto; text-align:right; font-size:7.6pt;">PHOTOGRAPHY — PASTOR &amp; FAMILY, GOLDEN HOUR, CHURCH LOBBY IN SOFT FOCUS</div>
  </div>
  <div style="position:absolute; inset:0; background:linear-gradient(80deg, rgba(16,30,56,0.95) 0%, rgba(16,30,56,0.72) 45%, rgba(16,30,56,0.2) 100%);"></div>
  <div class="frame" style="display:flex; flex-direction:column; justify-content:center;">
    <div class="eyebrow">CHAPTER EIGHT &mdash; YOUR MESSAGE MATTERS</div>
    <div style="height:0.3in;"></div>
    <h1 class="display" style="font-size:32pt; color:#FBF8F1; max-width:6.6in;">Your greatest sermons deserve more than one Sunday.</h1>
    <div style="height:0.26in;"></div>
    <p class="lede" style="max-width:6in;">
      They deserve to become a pathway that forms disciples, strengthens families, equips leaders,
      and leaves a legacy that outlives your ministry.
    </p>
  </div>
  {folio("Your Message Matters", 18)}
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
      <div style="font-family:'Archivo'; font-weight:600; font-size:10.5pt; letter-spacing:0.3em; color:#D9B876;">LIFETOGETHER</div>
      <div style="height:0.3in;"></div>
      <h1 class="display" style="font-size:26pt; color:#FBF8F1;">Let&rsquo;s build it together.</h1>
      <div style="height:0.22in;"></div>
      <p class="lede" style="max-width:4.6in; margin:0 auto;">
        You don&rsquo;t have to build the system alone &mdash; and you don&rsquo;t have to build it all at once.
      </p>
      <div style="height:0.4in;"></div>
      <div style="width:34px; height:2px; background:#B98D3E; margin:0 auto;"></div>
      <div style="height:0.24in;"></div>
      <div style="font-family:'Archivo'; font-weight:500; font-size:10pt; letter-spacing:0.08em; color:rgba(251,248,241,0.75);">LIFETOGETHER.COM &nbsp;&middot;&nbsp; BRETT@LIFETOGETHER.COM</div>
    </div>
    <div style="font-family:'Archivo'; font-weight:500; font-size:8pt; letter-spacing:0.14em; color:rgba(251,248,241,0.4);">THE CHURCH FORMATION SYSTEM&trade;</div>
  </div>
</div>
''')

# =================================================================
# ASSEMBLE
# =================================================================
extra_css = '''
.opp-item{
  font-family:'Playfair'; font-weight:700; font-size:14pt; color:var(--navy);
  padding:0.1in 0; border-bottom:1px solid var(--line);
}
.track-chip{
  font-family:'Archivo'; font-weight:600; font-size:9.5pt; letter-spacing:0.14em;
  color:#D9B876; border:1px solid rgba(217,184,118,0.5); border-radius:20px;
  padding:0.09in 0.2in;
}
.track-card{ flex:1; }
.track-list{ list-style:none; padding:0; margin:0; }
.track-list li{
  font-family:'Inter'; font-size:9.3pt; color:var(--ink); line-height:1.5;
  padding:0.06in 0 0.06in 0.18in; position:relative; border-top:1px solid var(--line);
}
.track-list li::before{ content:'\\2013'; position:absolute; left:0; color:var(--gold); }
.build-grid{
  display:grid; grid-template-columns:repeat(4, 1fr); gap:0.22in;
}
.build-cell{
  font-family:'Playfair'; font-weight:700; font-size:13pt; color:var(--navy);
  background:var(--cream); border-left:3px solid var(--gold);
  padding:0.22in 0.24in; line-height:1.25;
}
.build-cell.wide{
  grid-column:1 / -1; background:var(--navy); border-left:none; color:#FBF8F1;
  display:flex; align-items:center; justify-content:center; gap:0.24in;
  font-size:14pt; letter-spacing:0.02em;
}
.build-cell.wide .rule{ width:40px; height:1px; background:var(--gold); display:inline-block; }
.build-cell.wide{
  grid-column:1 / -1; background:var(--navy); border-left:none; color:#FBF8F1;
  display:flex; align-items:center; justify-content:center; gap:0.24in;
  font-size:14pt; letter-spacing:0.02em;
}
.build-cell.wide .rule{ width:40px; height:1px; background:var(--gold); display:inline-block; }
.offer-card{ flex:1; border-top:1px solid var(--line); padding-top:0.22in; }
.cmp-table{ display:flex; flex-direction:column; }
.cmp-head, .cmp-row{ display:flex; }
.cmp-head{ border-bottom:2px solid var(--navy); padding-bottom:0.14in; }
.cmp-row{ border-bottom:1px solid var(--line); padding:0.16in 0; }
.cmp-cell{ flex:1; font-family:'Inter'; font-size:10pt; color:var(--ink); padding-right:0.3in; }
.cmp-head .cmp-cell{ font-family:'Playfair'; font-weight:700; font-size:12pt; color:var(--navy); }
.cmp-label{ font-family:'Archivo'; font-weight:600; font-size:9pt; letter-spacing:0.1em; text-transform:uppercase; color:var(--gold); flex:0 0 1.3in; }
.cmp-head .cmp-label{ color:transparent; }
'''

with open("/home/claude/build/style.css") as f:
    base_css = f.read()

html = f'''<!DOCTYPE html>
<html><head><meta charset="utf-8">
<style>{base_css}
{extra_css}
</style></head>
<body>
{"".join(PAGES)}
</body></html>'''

with open("/home/claude/build/brochure.html", "w") as f:
    f.write(html)

print("Pages:", len(PAGES))
print("Written to /home/claude/build/brochure.html")
