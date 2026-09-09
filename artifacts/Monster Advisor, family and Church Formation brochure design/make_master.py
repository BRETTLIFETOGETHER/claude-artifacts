import sys
sys.path.insert(0, "/home/claude/build")
from diagrams import (wheel_diagram, campaign_lifecycle_diagram, content_library_diagram,
                       formation_funnel_diagram, step_chain_vertical, vertical_levels, fixed)

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
      <div style="font-family:'Archivo'; font-weight:700; font-size:10.3pt; letter-spacing:0.12em; color:var(--gold);">{name}</div>
      <div style="font-family:'Playfair'; font-weight:700; font-size:12.8pt; color:var(--navy); margin:0.05in 0 0.1in;">{sub}</div>
      <p style="font-family:'Inter'; font-size:8.9pt; line-height:1.5; color:var(--ink);">{para}</p>
      <ul class="track-list">{bl}</ul>
    </div>'''

def offer_card(name, sub, desc):
    return f'''
    <div class="offer-card" style="margin-bottom:0.2in;">
      <div style="width:28px; height:2px; background:var(--gold); margin-bottom:0.16in;"></div>
      <div style="font-family:'Playfair'; font-weight:700; font-size:14pt; color:var(--navy); line-height:1.2;">{name}</div>
      <div style="font-family:'Archivo'; font-weight:600; font-size:8.2pt; letter-spacing:0.1em; text-transform:uppercase; color:var(--gold); margin:0.08in 0 0.14in;">{sub}</div>
      <p style="font-family:'Inter'; font-size:9.3pt; line-height:1.55; color:var(--ink);">{desc}</p>
    </div>'''

# =================================================================
# PAGE 1 — COVER
# =================================================================
add(f'''
<div class="page navy">
  <div class="photo" style="position:absolute; inset:0; border-radius:0;">
    <div class="cap" style="right:0.68in; bottom:0.5in; left:auto; text-align:right; font-size:6.8pt;">PHOTOGRAPHY — PASTOR STUDYING AT A WOODEN DESK, MORNING LIGHT THROUGH A WINDOW</div>
  </div>
  <div style="position:absolute; inset:0; background:linear-gradient(190deg, rgba(16,30,56,0.4) 0%, rgba(16,30,56,0.88) 55%, rgba(16,30,56,0.98) 100%);"></div>
  <div class="frame" style="display:flex; flex-direction:column; justify-content:flex-end;">
    <div style="font-family:'Archivo'; font-weight:600; font-size:9pt; letter-spacing:0.22em; color:#D9B876; margin-bottom:2.2in;">THE COMPLETE GUIDE &amp; WAYS TO WORK TOGETHER</div>
    <h1 class="display" style="font-size:32pt; color:#FBF8F1;">The Church Formation System<span style="font-size:15pt; vertical-align:super;">™</span></h1>
    <div style="height:0.24in;"></div>
    <p style="font-family:'Playfair'; font-style:italic; font-weight:500; font-size:13.5pt; color:#D9B876; line-height:1.5;">
      Helping pastors turn sermons into curriculum &mdash; curriculum into community &mdash; and
      community into movements. Everything you need to understand the system, and every
      way to build it with us.
    </p>
    <div style="height:0.5in;"></div>
    <div style="display:flex; justify-content:space-between; align-items:flex-end; font-family:'Archivo'; font-weight:500; font-size:8pt; letter-spacing:0.12em; color:rgba(251,248,241,0.55);">
      <div>LIFETOGETHER.COM</div>
      <div style="width:22px; height:2px; background:#B98D3E;"></div>
    </div>
  </div>
</div>
''')

# =================================================================
# PAGE 2 — WELCOME / CONTENTS
# =================================================================
parts = [
    ("PART ONE — UNDERSTANDING THE SYSTEM", [
        ("The Future of Church Formation", 3),
        ("Why Most Sermons End Too Soon", 4),
        ("From Message to Movement", 5),
        ("The Framework & Five Environments", 6),
        ("The Church Formation Wheel", 7),
        ("The Five-Stage Process", 8),
        ("Campaign Architecture", 11),
        ("The Pastor Content Library", 12),
        ("AI as Ministry Multiplier", 13),
        ("21, 30, and 40-Day Journeys", 14),
        ("The Ministry Publishing System", 15),
        ("The Annual Formation Calendar", 16),
        ("Crawl, Walk, Run", 17),
        ("Church Case Studies", 18),
        ("Frequently Asked Questions", 19),
    ]),
    ("PART TWO — WAYS TO WORK TOGETHER", [
        ("Multiple Offerings, One System", 20),
        ("The Campaign Builder Intensive", 21),
        ("The 90-Day Accelerator", 23),
        ("The Annual Formation Partnership", 24),
        ("Investment Overview", 25),
        ("Next Steps", 26),
        ("Your Message Matters", 27),
    ]),
]
parts_html = ""
for part_title, items in parts:
    rows = "".join([f'''
      <div style="display:flex; align-items:baseline; padding:0.06in 0; border-bottom:1px solid var(--line);">
        <div style="font-family:'Playfair'; font-weight:700; font-size:10.3pt; color:var(--navy); flex:1;">{title}</div>
        <div style="font-family:'Archivo'; font-weight:600; font-size:8.4pt; color:var(--gold); width:0.35in; text-align:right;">{pg:02d}</div>
      </div>''' for title, pg in items])
    parts_html += f'''
    <div style="font-family:'Archivo'; font-weight:700; font-size:9pt; letter-spacing:0.14em; color:var(--gold); margin:0.2in 0 0.08in;">{part_title}</div>
    {rows}'''

add(f'''
<div class="page">
  <div class="frame">
    <div class="eyebrow">WELCOME</div>
    <div style="height:0.18in;"></div>
    <h1 class="display" style="font-size:19pt; color:var(--navy);">Everything you need to understand the system, and every way to build it with us.</h1>
    <div style="height:0.12in;"></div>
    <p class="lede" style="font-size:9.6pt;">
      Part One explains why this matters, what the system is, how it works, and what
      results your church can expect. Part Two lays out every way to work with us &mdash; from
      a single six-week Intensive to a full year of partnership.
    </p>
    {parts_html}
  </div>
  {folio("Welcome", 2)}
</div>
''')

# =================================================================
# PAGE 3 — THE FUTURE OF CHURCH FORMATION
# =================================================================
add(f'''
<div class="page">
  <div class="frame">
    <div class="eyebrow">PART ONE, CHAPTER ONE &mdash; THE FUTURE OF CHURCH FORMATION</div>
    <div style="height:0.2in;"></div>
    <h1 class="display" style="font-size:21pt; color:var(--navy);">Formation is becoming the work of the whole church, all week long.</h1>
    <div style="height:0.16in;"></div>
    <p class="lede">
      For a hundred years, the center of church life was the Sunday service. That is not
      wrong &mdash; it is simply no longer sufficient. People are formed by what they hear once
      a week far less than they are formed by what they practice every day, in community,
      at home.
    </p>
    <div style="height:0.14in;"></div>
    <p class="lede">
      The churches shaping the next generation will not simply preach well. They will build
      formation systems &mdash; ordinary rhythms that carry a message from the platform into
      daily life, without requiring a bigger staff or a bigger budget.
    </p>
    <div style="height:0.18in;"></div>
    <div class="takeaway">
      <span class="label">The shift underway</span>
      From church as a place you attend, to church as a formation system you live inside.
    </div>
    <div style="height:0.28in;"></div>
    {photo("PHOTOGRAPHY — CONGREGATION IN WORSHIP, WIDE SHOT, WARM LIGHT", "height:2.7in;")}
  </div>
  {folio("The Future of Church Formation", 3)}
</div>
''')

# =================================================================
# PAGE 4 — WHY MOST SERMONS END TOO SOON
# =================================================================
reasons = [
    ("No next step", "The sermon ends and nothing carries it into the week."),
    ("No shared language", "Groups, families, and staff each go their own direction."),
    ("No format beyond the stage", "A great message exists in only one form, spoken once."),
    ("No time to build more", "Staff capacity ends at the manuscript, not the curriculum."),
]
reason_cards = "".join([f'''
    <div style="border-top:2px solid var(--gold); padding-top:0.14in;">
      <div style="font-family:'Playfair'; font-weight:700; font-size:11.5pt; color:var(--navy); margin-bottom:0.06in;">{t}</div>
      <div style="font-family:'Inter'; font-size:8.8pt; color:var(--ink); line-height:1.5;">{d}</div>
    </div>''' for t, d in reasons])
add(f'''
<div class="page">
  <div class="frame">
    <div class="eyebrow">CHAPTER TWO &mdash; WHY MOST SERMONS END TOO SOON</div>
    <div style="height:0.2in;"></div>
    <h1 class="display" style="font-size:21pt; color:var(--navy);">A sermon is a moment. Formation is a path.</h1>
    <div style="height:0.14in;"></div>
    <p class="lede">
      Most churches don&rsquo;t lack good preaching. They lack a system to carry that
      preaching forward. Four gaps show up again and again:
    </p>
    <div style="height:0.24in;"></div>
    <div style="display:grid; grid-template-columns:1fr 1fr; gap:0.3in;">{reason_cards}</div>
    <div style="height:0.34in;"></div>
    <div class="pull-quote">Your greatest sermons deserve <span class="mark">more than one Sunday.</span></div>
  </div>
  {folio("Why Most Sermons End Too Soon", 4)}
</div>
''')

# =================================================================
# PAGE 5 — FROM MESSAGE TO MOVEMENT
# =================================================================
add(f'''
<div class="page navy">
  <div class="frame">
    <div class="eyebrow">CHAPTER THREE &mdash; FROM MESSAGE TO MOVEMENT</div>
    <div style="height:0.16in;"></div>
    <h1 class="display" style="font-size:20pt; color:#FBF8F1;">What becomes possible with a system underneath it</h1>
    <div style="height:0.14in;"></div>
    <div style="text-align:center;">{fixed(step_chain_vertical([
        ("MESSAGE", "One message, prepared once."),
        ("CURRICULUM", "Shaped into a resource."),
        ("COMMUNITY", "Practiced in real relationship."),
        ("MOVEMENT", "Carried into lasting change."),
    ]), 7.1, 4.2)}</div>
    <div style="height:0.1in;"></div>
    <div class="pull-quote" style="font-size:14pt;">One message. <span class="mark">Many forms. One movement.</span></div>
  </div>
  {folio("From Message to Movement", 5)}
</div>
''')

# =================================================================
# PAGE 6 — FRAMEWORK & FIVE ENVIRONMENTS (funnel)
# =================================================================
funnel_stages = [
    ("Weekend", "The whole church hears one message together.", 1.0),
    ("Groups", "Circles of real relationship discuss it.", 0.8),
    ("Daily", "Individuals practice it in a daily rhythm.", 0.62),
    ("Family", "Households carry it into the home.", 0.46),
    ("Mission", "A shaped few carry it into the world.", 0.32),
]
add(f'''
<div class="page">
  <div class="frame">
    <div class="eyebrow">CHAPTER FOUR &mdash; THE FRAMEWORK &amp; FIVE ENVIRONMENTS</div>
    <div style="height:0.18in;"></div>
    <h1 class="display" style="font-size:21pt; color:var(--navy);">Five environments. One deepening path.</h1>
    <div style="height:0.14in;"></div>
    <p class="lede">
      The Church Formation Framework names the five environments where a message keeps
      doing its work. Each environment reaches fewer people than the one before it &mdash;
      and forms each of them more deeply.
    </p>
    <div style="height:0.18in;"></div>
    <div style="text-align:center;">{fixed(formation_funnel_diagram(funnel_stages), 6.6, 4.9)}</div>
    <div style="height:0.16in;"></div>
    <div class="takeaway">
      <span class="label">Why this matters</span>
      Breadth and depth are not in competition. A good system gives you both, on purpose.
    </div>
  </div>
  {folio("The Framework & Five Environments", 6)}
</div>
''')

# =================================================================
# PAGE 7 — THE CHURCH FORMATION WHEEL
# =================================================================
add(f'''
<div class="page">
  <div class="frame">
    <div class="eyebrow">CHAPTER FIVE &mdash; WEEKEND + GROUPS + DAILY + FAMILY + MISSION</div>
    <div style="height:0.1in;"></div>
    <h1 class="display" style="font-size:20pt; color:var(--navy);">The Church Formation Wheel</h1>
    <div style="text-align:center;">{fixed(wheel_diagram(), 7.1, 6.9)}</div>
    <div class="takeaway">
      <span class="label">Takeaway</span>
      The wheel turns every week &mdash; the same message moving through five environments, on repeat.
    </div>
  </div>
  {folio("The Church Formation Wheel", 7)}
</div>
''')

# =================================================================
# PAGE 8 — FIVE-STAGE PROCESS INTRO
# =================================================================
track_bar = "".join([f'<div class="track-chip">{t}</div>' for t in ["DISCERN","DEVELOP","PRODUCE","PUBLISH","MOBILIZE"]])
add(f'''
<div class="page navy">
  <div class="frame" style="display:flex; flex-direction:column; justify-content:center;">
    <div class="eyebrow">CHAPTER SIX &mdash; THE FIVE-STAGE PROCESS</div>
    <div style="height:0.22in;"></div>
    <h1 class="display" style="font-size:25pt; color:#FBF8F1;">Five stages turn a sermon into a system.</h1>
    <div style="height:0.18in;"></div>
    <p class="lede">
      Every campaign your church builds moves through the same five disciplines. Learn
      them once, and your team can repeat them with every future message.
    </p>
    <div style="height:0.3in;"></div>
    <div style="display:grid; grid-template-columns:1fr 1fr; gap:0.14in;">{track_bar}</div>
  </div>
  {folio("The Five-Stage Process", 8)}
</div>
''')

# =================================================================
# PAGE 9 — FIVE-STAGE TRACKS 1-3
# =================================================================
tracks_1_3 = [
    ("DISCERN", "Hearing it clearly", "A team identifies the one true center of a message &mdash; the single idea everything else will serve.",
     ["Name the one idea worth building around", "Separate the message from the moment", "Identify the Scripture that carries it", "Spot where it touches daily life"]),
    ("DEVELOP", "Shaping the path", "A message becomes a multi-week arc with its own pacing and spiritual logic, not just a topic.",
     ["Map the week-by-week arc", "Set the pace between conviction and rest", "Build in the turn toward application", "Design the invitation at the end"]),
    ("PRODUCE", "Building every format", "The arc becomes curriculum, devotionals, and training, each shaped for how it will actually be used.",
     ["Write small group discussion guides", "Draft daily devotional content", "Build a leader training kit", "Prepare family conversation prompts"]),
]
add(f'''
<div class="page">
  <div class="frame">
    <div class="eyebrow">THE FIVE-STAGE PROCESS &mdash; STAGES ONE THROUGH THREE</div>
    <div style="height:0.16in;"></div>
    {"".join([track_card(*t) for t in tracks_1_3])}
  </div>
  {folio("The Five-Stage Process", 9)}
</div>
''')

# =================================================================
# PAGE 10 — FIVE-STAGE TRACKS 4-5 + quote
# =================================================================
tracks_4_5 = [
    ("PUBLISH", "Packaging with excellence", "The finished campaign is designed, proofed, and formatted so it feels like a resource, not a handout.",
     ["Design a cover and visual identity", "Typeset every printed and digital piece", "Proof theology, tone, and Scripture", "Prepare it for licensing or release"]),
    ("MOBILIZE", "Getting it into hands", "A campaign only forms people if it launches well, so this stage ends with a real activation plan.",
     ["Build the launch and promotion plan", "Train leaders to carry the content well", "Prepare the pulpit announcement path", "Plan the on-ramp to what comes next"]),
]
add(f'''
<div class="page">
  <div class="frame">
    <div class="eyebrow">THE FIVE-STAGE PROCESS &mdash; STAGES FOUR AND FIVE</div>
    <div style="height:0.16in;"></div>
    {"".join([track_card(*t) for t in tracks_4_5])}
    <div style="height:0.06in;"></div>
    <div class="pull-quote" style="font-size:13.5pt;">Your team doesn&rsquo;t just receive curriculum. <span class="mark">They learn to build it, every time.</span></div>
  </div>
  {folio("The Five-Stage Process", 10)}
</div>
''')

# =================================================================
# PAGE 11 — CAMPAIGN ARCHITECTURE (lifecycle)
# =================================================================
lifecycle_stages = [
    ("Plan", "Choose the theme and the season"),
    ("Build", "Produce every format from one message"),
    ("Launch", "Mobilize the whole church together"),
    ("Sustain", "Reinforce it through groups and daily practice"),
    ("Multiply", "Let it shape the next campaign"),
]
add(f'''
<div class="page">
  <div class="frame">
    <div class="eyebrow">CHAPTER SEVEN &mdash; CAMPAIGN ARCHITECTURE</div>
    <div style="height:0.1in;"></div>
    <h1 class="display" style="font-size:20pt; color:var(--navy);">The Campaign Lifecycle</h1>
    <div style="text-align:center;">{fixed(campaign_lifecycle_diagram(lifecycle_stages), 7.1, 6.3)}</div>
    <div class="takeaway">
      <span class="label">Why it matters</span>
      No campaign is a one-time event. Every one seeds the next.
    </div>
  </div>
  {folio("Campaign Architecture", 11)}
</div>
''')

# =================================================================
# PAGE 12 — THE PASTOR CONTENT LIBRARY
# =================================================================
add(f'''
<div class="page">
  <div class="frame">
    <div class="eyebrow">CHAPTER EIGHT &mdash; THE PASTOR CONTENT LIBRARY</div>
    <div style="height:0.18in;"></div>
    <h1 class="display" style="font-size:20pt; color:var(--navy);">A library that compounds every year you build it.</h1>
    <div style="height:0.14in;"></div>
    <p class="lede">
      Every campaign you build stays in your library &mdash; ready to relaunch, adapt, or hand
      to a new group of leaders. Five years in, most churches are running almost entirely
      on content they already own.
    </p>
    <div style="height:0.2in;"></div>
    <div style="text-align:center;">{fixed(content_library_diagram(), 7.1, 4.6)}</div>
  </div>
  {folio("The Pastor Content Library", 12)}
</div>
''')

# =================================================================
# PAGE 13 — AI AS MINISTRY MULTIPLIER
# =================================================================
add(f'''
<div class="page navy">
  <div class="frame">
    <div class="eyebrow">CHAPTER NINE &mdash; AI AS MINISTRY MULTIPLIER</div>
    <div style="height:0.2in;"></div>
    <h1 class="display" style="font-size:22pt; color:#FBF8F1;">A multiplier for your message, never a substitute for it.</h1>
    <div style="height:0.16in;"></div>
    <p class="lede">
      AI does not write your theology, and it does not preach your sermon. It takes what
      you have already studied and prayed over, and helps produce the devotionals,
      discussion guides, and training materials that would otherwise take a team of
      writers months to complete. Every word is still reviewed by pastors for theology,
      tone, and truth before it reaches your congregation.
    </p>
    <div style="height:0.26in;"></div>
    <div class="equation">
      <span>One message</span><span class="op">&times;</span><span>AI production</span><span class="op">=</span><span class="result">Nine formats</span>
    </div>
    <div style="height:0.22in;"></div>
    <div class="takeaway">
      <span class="label">Without AI</span>
      Producing nine formats from one message once cost $15,000&ndash;$40,000 in writing alone.
    </div>
    <div style="height:0.16in;"></div>
    <div class="takeaway">
      <span class="label">With AI</span>
      The same nine formats can be produced in days, at a fraction of the cost, with every word still pastor-reviewed.
    </div>
  </div>
  {folio("AI as Ministry Multiplier", 13)}
</div>
''')

# =================================================================
# PAGE 14 — 21/30/40-DAY JOURNEYS
# =================================================================
journeys = [
    ("21-Day Challenge", "A focused sprint", "Best for a single habit, a launch moment, or a season with limited attention &mdash; like January or a new sermon series kickoff."),
    ("30-Day Journey", "A full month", "Best for a themed month tied to the calendar &mdash; stewardship in the fall, prayer in January, family in May."),
    ("40-Day Campaign", "A complete season", "Best for your most significant churchwide moments &mdash; the journeys people will remember years later."),
]
journey_cards = "".join([offer_card(n, s, d) for n, s, d in journeys])
add(f'''
<div class="page">
  <div class="frame">
    <div class="eyebrow">CHAPTER TEN &mdash; 21, 30, AND 40-DAY JOURNEYS</div>
    <div style="height:0.2in;"></div>
    <h1 class="display" style="font-size:21pt; color:var(--navy);">Choosing the right length for the moment.</h1>
    <div style="height:0.24in;"></div>
    {journey_cards}
    <div style="height:0.16in;"></div>
    <div class="takeaway">
      <span class="label">How to choose</span>
      Match the length to the weight of the moment &mdash; a 40-day format on a light topic will feel padded, and a 21-day format on a heavy one will feel rushed.
    </div>
  </div>
  {folio("21, 30, and 40-Day Journeys", 14)}
</div>
''')

# =================================================================
# PAGE 15 — MINISTRY PUBLISHING SYSTEM
# =================================================================
pub_steps = [
    ("DRAFT", "The message and study content are written and organized."),
    ("DESIGN", "A visual identity and layout are applied to every piece."),
    ("PROOF", "Theology, tone, and Scripture are reviewed line by line."),
    ("PACKAGE", "Print and digital formats are finalized and tested."),
    ("RELEASE", "The finished campaign is delivered, ready to launch."),
]
add(f'''
<div class="page">
  <div class="frame">
    <div class="eyebrow">CHAPTER ELEVEN &mdash; THE MINISTRY PUBLISHING SYSTEM</div>
    <div style="height:0.18in;"></div>
    <h1 class="display" style="font-size:20pt; color:var(--navy);">From a rough draft to a finished, launch-ready resource.</h1>
    <div style="height:0.12in;"></div>
    <p class="lede">
      A campaign is only as strong as its final execution. The Publishing System is the
      quality bar every resource passes through before it reaches your church.
    </p>
    <div style="height:0.16in;"></div>
    <div style="text-align:center;">{fixed(step_chain_vertical(pub_steps), 7.1, 4.6)}</div>
  </div>
  {folio("The Ministry Publishing System", 15)}
</div>
''')

# =================================================================
# PAGE 16 — ANNUAL FORMATION CALENDAR
# =================================================================
calendar_stops = [
    ("JAN &ndash; FEB", "New Year vision and spiritual growth campaign."),
    ("MAR &ndash; APR", "An Easter season journey toward the resurrection."),
    ("MAY &ndash; JUN", "A family and relationships campaign."),
    ("JUL &ndash; AUG", "A lighter 21-day summer challenge."),
    ("SEP &ndash; OCT", "A prayer or discipleship-deepening season."),
    ("NOV &ndash; DEC", "A stewardship and generosity campaign into the new year."),
]
add(f'''
<div class="page">
  <div class="frame">
    <div class="eyebrow">CHAPTER TWELVE &mdash; THE ANNUAL FORMATION CALENDAR</div>
    <div style="height:0.16in;"></div>
    <h1 class="display" style="font-size:19pt; color:var(--navy);">A rhythm for the whole church year</h1>
    <div style="height:0.12in;"></div>
    <p class="lede" style="font-size:9.8pt;">
      Most churches plan one series at a time. A formation calendar plans the whole year
      at once &mdash; so every campaign has a season, and no two seasons compete for attention.
    </p>
    <div style="height:0.12in;"></div>
    <div style="text-align:center;">{fixed(step_chain_vertical(calendar_stops), 7.1, 4.9)}</div>
    <div style="height:0.1in;"></div>
    <div class="takeaway">
      <span class="label">Practical takeaway</span>
      Plan the calendar a full year ahead, then build one campaign at a time inside it.
    </div>
  </div>
  {folio("The Annual Formation Calendar", 16)}
</div>
''')

# =================================================================
# PAGE 17 — CRAWL WALK RUN
# =================================================================
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
    <div class="eyebrow">CHAPTER THIRTEEN &mdash; CRAWL, WALK, RUN</div>
    <div style="height:0.16in;"></div>
    <h1 class="display" style="font-size:20pt; color:var(--navy);">Every church starts where it is, and grows from there.</h1>
    <div style="height:0.12in;"></div>
    <p class="lede">
      No church is asked to arrive fully built. Most move through these five levels over
      eighteen to twenty-four months, at whatever pace fits their staff and calendar.
    </p>
    <div style="text-align:center;">{fixed(vertical_levels(crawl_levels), 7.1, 5.2)}</div>
  </div>
  {folio("Crawl, Walk, Run", 17)}
</div>
''')

# =================================================================
# PAGE 18 — CHURCH CASE STUDIES
# =================================================================
cases = [
    ("Church Name Placeholder", "Mid-size congregation &middot; Suburban", "40-Day Stewardship Campaign", "Small group participation increased [XX]% during the campaign season."),
    ("Church Name Placeholder", "Multisite congregation &middot; Urban", "30-Day Family Journey", "Households reported measurably stronger at-home spiritual conversation."),
    ("Church Name Placeholder", "Church plant &middot; Rural", "21-Day Prayer Challenge", "First-time small group sign-ups reached their highest point in the church's history."),
]
case_cards = "".join([f'''
    <div class="case-card" style="margin-bottom:0.2in;">
      <div style="font-family:'Playfair'; font-weight:700; font-size:12pt; color:var(--navy);">{name}</div>
      <div style="font-family:'Archivo'; font-weight:600; font-size:7.6pt; letter-spacing:0.06em; color:var(--gray); margin:0.03in 0 0.06in;">{meta}</div>
      <div style="font-family:'Archivo'; font-weight:600; font-size:7.8pt; letter-spacing:0.1em; text-transform:uppercase; color:var(--gold); margin-bottom:0.05in;">{campaign}</div>
      <p style="font-family:'Inter'; font-size:8.8pt; line-height:1.5; color:var(--ink);">{result}</p>
    </div>''' for name, meta, campaign, result in cases])
add(f'''
<div class="page">
  <div class="frame">
    <div class="eyebrow">CHAPTER FOURTEEN &mdash; CHURCH CASE STUDIES</div>
    <div style="height:0.16in;"></div>
    <h1 class="display" style="font-size:20pt; color:var(--navy);">What this looks like in real churches</h1>
    <div style="height:0.06in;"></div>
    <p style="font-family:'Inter'; font-size:8.6pt; color:var(--gray); font-style:italic;">Case studies below are shown in placeholder format, ready to be replaced with your church's own story and results.</p>
    <div style="height:0.18in;"></div>
    {case_cards}
  </div>
  {folio("Church Case Studies", 18)}
</div>
''')

# =================================================================
# PAGE 19 — FAQ
# =================================================================
faqs = [
    ("Do we have to give up our own preaching style?", "No. The system is built around your pastor's own messages &mdash; it organizes and extends your voice, it never replaces it."),
    ("Will this create more work for our staff?", "Most of the production work is handled for you. Your team's role is review and mobilization, not writing from scratch."),
    ("What if our church is small?", "The Crawl, Walk, Run model exists for this reason. Most small churches begin at Level One with a licensed campaign."),
    ("How much does this cost?", "It depends on the level of partnership you choose &mdash; see Multiple Offerings, next, for the three ways to work with us."),
    ("How is AI used, and is it reviewed?", "AI helps produce first drafts of formats like devotionals and guides. Every piece is reviewed by pastors before your church ever sees it."),
]
faq_rows = "".join([f'''
    <div style="padding:0.1in 0; border-bottom:1px solid var(--line);">
      <div style="font-family:'Playfair'; font-weight:700; font-size:10.5pt; color:var(--navy); margin-bottom:0.03in;">{q}</div>
      <div style="font-family:'Inter'; font-size:8.6pt; color:var(--ink); line-height:1.5;">{a}</div>
    </div>''' for q, a in faqs])
add(f'''
<div class="page">
  <div class="frame">
    <div class="eyebrow">CHAPTER FIFTEEN &mdash; FREQUENTLY ASKED QUESTIONS</div>
    <div style="height:0.16in;"></div>
    <h1 class="display" style="font-size:19pt; color:var(--navy);">Honest answers to common questions</h1>
    <div style="height:0.14in;"></div>
    {faq_rows}
  </div>
  {folio("Frequently Asked Questions", 19)}
</div>
''')

# =================================================================
# PAGE 20 — PART TWO DIVIDER: MULTIPLE OFFERINGS, ONE SYSTEM
# =================================================================
add(f'''
<div class="page navy">
  <div class="frame" style="display:flex; flex-direction:column; justify-content:center;">
    <div class="eyebrow">PART TWO &mdash; WAYS TO WORK TOGETHER</div>
    <div style="height:0.24in;"></div>
    <h1 class="display" style="font-size:27pt; color:#FBF8F1;">Multiple offerings, one system.</h1>
    <div style="height:0.2in;"></div>
    <p class="lede">
      Everything in Part One is the same system, whichever way you enter it. Some churches
      need one campaign built well over six weeks. Others are ready to build a whole year
      of formation. What follows are the three ways to work with us &mdash; so you can choose
      the level of partnership that fits your church right now.
    </p>
    <div style="height:0.3in;"></div>
    <div style="display:grid; grid-template-columns:1fr 1fr; gap:0.14in;">
      <div class="track-chip">CAMPAIGN BUILDER<br/><span style="font-size:8pt;">INTENSIVE</span></div>
      <div class="track-chip">90-DAY<br/><span style="font-size:8pt;">ACCELERATOR</span></div>
      <div class="track-chip">ANNUAL FORMATION<br/><span style="font-size:8pt;">PARTNERSHIP</span></div>
    </div>
  </div>
  {folio("Multiple Offerings, One System", 20)}
</div>
''')

# =================================================================
# PAGE 21 — CAMPAIGN BUILDER INTENSIVE
# =================================================================
week_chips = "".join([f'<div class="track-chip">WEEK {i+1}<br/><span style="font-size:7.6pt;">{w}</span></div>' for i, w in enumerate(["DISCOVER","DISCERN","DESIGN","DEVELOP","PRODUCE","LAUNCH"])])
add(f'''
<div class="page">
  <div class="frame">
    <div class="eyebrow">OFFERING ONE &mdash; THE CAMPAIGN BUILDER INTENSIVE</div>
    <div style="height:0.18in;"></div>
    <h1 class="display" style="font-size:21pt; color:var(--navy);">Six weeks. One complete campaign blueprint.</h1>
    <div style="height:0.14in;"></div>
    <p class="lede">
      A collaborative, six-week planning process that turns a pastor&rsquo;s own message into a
      complete, launch-ready campaign &mdash; built with your team, not delivered to them. It is
      not curriculum writing, and it is not coaching alone.
    </p>
    <div style="height:0.2in;"></div>
    <div style="display:grid; grid-template-columns:1fr 1fr 1fr; gap:0.12in;">{week_chips}</div>
    <div style="height:0.24in;"></div>
    <div class="takeaway">
      <span class="label">Best for</span>
      Churches preparing to launch a vision, spiritual growth, stewardship, family, or prayer campaign &mdash; or any custom sermon-based journey.
    </div>
    <div style="height:0.18in;"></div>
    <div class="takeaway">
      <span class="label">You walk away with</span>
      Campaign strategy, sermon roadmap, curriculum outline, video plan, leader resources, promotion plan, launch calendar, and a Day 41 strategy.
    </div>
  </div>
  {folio("The Campaign Builder Intensive", 21)}
</div>
''')

# =================================================================
# PAGE 22 — INTENSIVE: WHY CHURCHES GET STUCK (support page)
# =================================================================
stuck_reasons = [
    ("Too many good ideas", "A dozen directions worth pursuing, and no clear place to start."),
    ("No bandwidth to build", "Weekly ministry already fills every hour your team has."),
]
stuck_cards = "".join([f'''
    <div style="border-top:2px solid var(--gold); padding-top:0.14in; margin-bottom:0.2in;">
      <div style="font-family:'Playfair'; font-weight:700; font-size:12pt; color:var(--navy); margin-bottom:0.06in;">{t}</div>
      <div style="font-family:'Inter'; font-size:9pt; color:var(--ink); line-height:1.5;">{d}</div>
    </div>''' for t, d in stuck_reasons])
add(f'''
<div class="page">
  <div class="frame">
    <div class="eyebrow">THE CAMPAIGN BUILDER INTENSIVE &mdash; CONTINUED</div>
    <div style="height:0.2in;"></div>
    <h1 class="display" style="font-size:21pt; color:var(--navy);">You don&rsquo;t need another idea. You need a process.</h1>
    <div style="height:0.16in;"></div>
    <p class="lede">
      Almost every pastor we talk with already has more than enough vision and content to
      build a full campaign. What&rsquo;s missing isn&rsquo;t inspiration &mdash; it&rsquo;s a clear, guided
      process to get from a sermon idea to a finished, launch-ready experience.
    </p>
    <div style="height:0.24in;"></div>
    {stuck_cards}
    <div style="height:0.2in;"></div>
    <div class="pull-quote">You already have the message. <span class="mark">You just need the process to build with it.</span></div>
  </div>
  {folio("The Campaign Builder Intensive", 22)}
</div>
''')

# =================================================================
# PAGE 23 — 90-DAY ACCELERATOR
# =================================================================
add(f'''
<div class="page">
  <div class="frame">
    <div class="eyebrow">OFFERING TWO &mdash; THE 90-DAY ACCELERATOR</div>
    <div style="height:0.2in;"></div>
    <h1 class="display" style="font-size:21pt; color:var(--navy);">From blueprint to a fully launched campaign</h1>
    <div style="height:0.16in;"></div>
    <p class="lede">
      The Intensive gives your church a complete plan. For churches who want hands-on
      help carrying that plan all the way to launch, the 90-Day Accelerator adds ongoing
      production support and coaching through the entire launch season.
    </p>
    <div style="height:0.18in;"></div>
    <div class="takeaway">
      <span class="label">Best for</span>
      Churches ready to move quickly &mdash; from a finished blueprint to a fully launched campaign in one season.
    </div>
    <div style="height:0.3in;"></div>
    {photo("PHOTOGRAPHY — LAUNCH TEAM PREPARING MATERIALS BEFORE A SERVICE", "height:3in;")}
  </div>
  {folio("The 90-Day Accelerator", 23)}
</div>
''')

# =================================================================
# PAGE 24 — ANNUAL FORMATION PARTNERSHIP (+ leader pathway)
# =================================================================
leader_levels = [
    ("1", "Participant", "Experiences a campaign as a small group member."),
    ("2", "Group Leader", "Leads others through the discussion guide."),
    ("3", "Coach", "Trains and supports several group leaders."),
    ("4", "Campaign Builder", "Helps shape original campaigns for the church."),
]
add(f'''
<div class="page navy">
  <div class="frame">
    <div class="eyebrow">OFFERING THREE &mdash; THE ANNUAL FORMATION PARTNERSHIP</div>
    <div style="height:0.16in;"></div>
    <h1 class="display" style="font-size:20pt; color:#FBF8F1;">A twelve-month coaching relationship, not a one-time purchase.</h1>
    <div style="height:0.12in;"></div>
    <p class="lede" style="font-size:9.8pt;">
      The Partnership pairs your team with ongoing coaching, planning, and content
      development as you build a full formation calendar &mdash; and as your own people grow
      into leaders inside the system.
    </p>
    <div style="height:0.12in;"></div>
    <div style="text-align:center;">{fixed(vertical_levels(leader_levels), 7.1, 4.5)}</div>
  </div>
  {folio("The Annual Formation Partnership", 24)}
</div>
''')

# =================================================================
# PAGE 25 — INVESTMENT OVERVIEW / COMPARISON
# =================================================================
compare_rows = [
    ("Length", "Six weeks", "One season (~90 days)", "Twelve months"),
    ("Best for", "Your first campaign blueprint", "Carrying it to a full launch", "A whole year, and a trained team"),
    ("Format", "Guided weekly planning", "Hands-on production &amp; launch support", "Ongoing coaching &amp; training"),
    ("You leave with", "One completed campaign blueprint", "One fully launched campaign", "A trained team and a repeatable system"),
    ("Investment", "A one-time program fee", "A one-time program fee", "An ongoing annual partnership fee"),
]
def compare_row(label, a, b, c, header=False):
    cls = "cmp-head" if header else "cmp-row"
    return f'''<div class="{cls}"><div class="cmp-cell cmp-label">{label}</div><div class="cmp-cell">{a}</div><div class="cmp-cell">{b}</div><div class="cmp-cell">{c}</div></div>'''
header_row = compare_row("", "Intensive", "Accelerator", "Partnership", header=True)
body_rows = "".join([compare_row(l,a,b,c) for l,a,b,c in compare_rows])
add(f'''
<div class="page">
  <div class="frame">
    <div class="eyebrow">WAYS TO WORK TOGETHER &mdash; AT A GLANCE</div>
    <div style="height:0.2in;"></div>
    <h1 class="display" style="font-size:21pt; color:var(--navy);">Investment overview</h1>
    <div style="height:0.24in;"></div>
    <div class="cmp-table">{header_row}{body_rows}</div>
    <div style="height:0.2in;"></div>
    <p style="font-family:'Inter'; font-size:8.3pt; color:var(--gray); font-style:italic;">
      Specific investment figures vary by church size and scope, and are confirmed during your
      strategy conversation.
    </p>
  </div>
  {folio("Investment Overview", 25)}
</div>
''')

# =================================================================
# PAGE 26 — NEXT STEPS
# =================================================================
steps = [
    ("01", "Schedule a strategy conversation", "A complimentary conversation to talk through your church's specific season and needs."),
    ("02", "Choose your offering", "Intensive, Accelerator, or Partnership &mdash; whichever fits where your church is right now."),
    ("03", "Build your first campaign", "Move through the five-stage process with our team alongside yours."),
    ("04", "Launch, and plan the next one", "Mobilize your church, then begin filling in your annual formation calendar."),
]
step_rows = "".join([f'''
    <div style="display:flex; gap:0.2in; padding:0.14in 0; border-bottom:1px solid var(--line);">
      <div style="font-family:'Playfair'; font-weight:700; font-size:17pt; color:var(--gold); width:0.5in;">{n}</div>
      <div>
        <div style="font-family:'Playfair'; font-weight:700; font-size:12pt; color:var(--navy); margin-bottom:0.03in;">{t}</div>
        <div style="font-family:'Inter'; font-size:9pt; color:var(--ink); line-height:1.5;">{d}</div>
      </div>
    </div>''' for n, t, d in steps])
add(f'''
<div class="page">
  <div class="frame">
    <div class="eyebrow">NEXT STEPS</div>
    <div style="height:0.2in;"></div>
    <h1 class="display" style="font-size:22pt; color:var(--navy);">How to begin</h1>
    <div style="height:0.2in;"></div>
    {step_rows}
  </div>
  {folio("Next Steps", 26)}
</div>
''')

# =================================================================
# PAGE 27 — CLOSING: YOUR MESSAGE MATTERS
# =================================================================
add(f'''
<div class="page navy">
  <div class="photo" style="position:absolute; inset:0; border-radius:0;">
    <div class="cap" style="right:0.68in; bottom:0.5in; left:auto; text-align:right; font-size:6.8pt;">PHOTOGRAPHY — PASTOR &amp; FAMILY, GOLDEN HOUR, CHURCH LOBBY IN SOFT FOCUS</div>
  </div>
  <div style="position:absolute; inset:0; background:linear-gradient(190deg, rgba(16,30,56,0.4) 0%, rgba(16,30,56,0.9) 55%, rgba(16,30,56,0.98) 100%);"></div>
  <div class="frame" style="display:flex; flex-direction:column; justify-content:flex-end;">
    <div class="eyebrow">YOUR MESSAGE MATTERS</div>
    <div style="height:0.22in;"></div>
    <h1 class="display" style="font-size:23pt; color:#FBF8F1;">Your greatest sermons deserve more than one Sunday.</h1>
    <div style="height:0.18in;"></div>
    <p class="lede">
      They deserve to become a movement that shapes lives, strengthens families, equips
      leaders, and leaves a legacy that outlives your ministry. You don&rsquo;t have to build it
      alone &mdash; and you don&rsquo;t have to build it all at once.
    </p>
  </div>
  {folio("Your Message Matters", 27)}
</div>
''')

# =================================================================
# PAGE 28 — BACK COVER
# =================================================================
add(f'''
<div class="page navy">
  <div class="frame" style="display:flex; flex-direction:column; justify-content:space-between; align-items:center; text-align:center;">
    <div></div>
    <div>
      <div style="font-family:'Archivo'; font-weight:600; font-size:9.5pt; letter-spacing:0.28em; color:#D9B876;">LIFETOGETHER</div>
      <div style="height:0.26in;"></div>
      <h1 class="display" style="font-size:22pt; color:#FBF8F1;">Let&rsquo;s build it together.</h1>
      <div style="height:0.18in;"></div>
      <p class="lede" style="max-width:4.4in; margin:0 auto;">
        Schedule a complimentary Church Formation Strategy Conversation to talk through
        which offering fits your church right now.
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

# =================================================================
# ASSEMBLE
# =================================================================
with open("/home/claude/build/portrait_style.css") as f:
    base_css = f.read()

extra_css = '''
.equation{ display:flex; align-items:baseline; gap:0.14in; flex-wrap:wrap; font-family:'Playfair'; font-weight:700; font-size:13pt; color:#FBF8F1; }
.equation .op{ color:var(--gold); font-size:14pt; }
.equation .result{ color:var(--gold-bright); }
'''

html = f'''<!DOCTYPE html>
<html><head><meta charset="utf-8">
<style>{base_css}{extra_css}</style></head>
<body>{"".join(PAGES)}</body></html>'''

with open("/home/claude/build/master.html", "w") as f:
    f.write(html)
print("Pages:", len(PAGES))
