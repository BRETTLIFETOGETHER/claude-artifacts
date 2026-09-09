import sys
sys.path.insert(0, "/home/claude/build")
from diagrams import (message_movement_diagram, step_chain_diagram, wheel_diagram,
                       generic_staircase, generic_timeline, campaign_lifecycle_diagram,
                       content_library_diagram, formation_funnel_diagram)

PAGES = []
def add(html): PAGES.append(html)

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

def eyebrow_chapter(n, name):
    return f"CHAPTER {n:02d} &mdash; {name}".upper() if False else f"CHAPTER {n} &mdash; {name}"

# =================================================================
# PAGE 1 — COVER
# =================================================================
add(f'''
<div class="page navy">
  <div class="photo" style="position:absolute; inset:0; border-radius:0;">
    <div class="cap" style="right:0.9in; bottom:0.6in; left:auto; text-align:right; font-size:7.6pt;">PHOTOGRAPHY — PASTOR STUDYING AT A WOODEN DESK, MORNING LIGHT THROUGH A WINDOW</div>
  </div>
  <div style="position:absolute; inset:0; background:linear-gradient(100deg, rgba(16,30,56,0.97) 0%, rgba(16,30,56,0.9) 34%, rgba(16,30,56,0.36) 64%, rgba(16,30,56,0.08) 100%);"></div>
  <div class="frame" style="display:flex; flex-direction:column; justify-content:space-between;">
    <div style="font-family:'Archivo'; font-weight:600; font-size:10.5pt; letter-spacing:0.3em; color:#D9B876;">LIFETOGETHER</div>
    <div style="max-width:7in;">
      <div style="font-family:'Archivo'; font-weight:600; font-size:10pt; letter-spacing:0.22em; color:#D9B876; margin-bottom:0.3in;">THE COMPLETE MINISTRY GUIDEBOOK</div>
      <h1 class="display" style="font-size:48pt; color:#FBF8F1;">The Church<br/>Formation System<span style="font-size:20pt; vertical-align:super;">™</span></h1>
      <div style="height:0.3in;"></div>
      <p style="font-family:'Playfair'; font-style:italic; font-weight:500; font-size:15.5pt; color:#D9B876; line-height:1.5; max-width:5.7in;">
        A complete guide to why this matters, what the system is, how it works, and what
        your church can expect.
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
    ("The Future of Church Formation", "Why this season calls for a new approach", 3),
    ("Why Most Sermons End Too Soon", "The gap between preaching and formation", 4),
    ("From Message to Movement", "What becomes possible with a system", 5),
    ("The Formation Framework & Environments", "The architecture underneath everything", 6),
    ("Weekend, Groups, Daily, Family, Mission", "The formation wheel in motion", 7),
    ("The Five-Stage Process", "Discern, Develop, Produce, Publish, Mobilize", 9),
    ("Campaign Architecture", "How one campaign is built and lives", 11),
    ("The Pastor Content Library", "A library that compounds every year", 12),
    ("AI as Ministry Multiplier", "Producing more without preaching more", 13),
    ("21, 30, and 40-Day Journeys", "Choosing the right length for the moment", 14),
    ("The Ministry Publishing System", "From draft to a finished resource", 15),
    ("The Annual Formation Calendar", "A rhythm for the whole church year", 16),
    ("Crawl, Walk, Run", "Growing into the system at your pace", 17),
    ("Church Case Studies", "What this looks like in real churches", 18),
    ("Frequently Asked Questions", "Honest answers to common questions", 19),
    ("The Church Formation Partnership", "Ongoing coaching for the whole journey", 20),
    ("Next Steps", "How to begin", 21),
]
rows1 = "".join([f'''
    <div style="padding:0.075in 0; border-bottom:1px solid var(--line);">
      <div style="display:flex; align-items:baseline;">
        <div style="font-family:'Playfair'; font-weight:700; font-size:10.8pt; color:var(--navy); flex:1;">{title}</div>
        <div style="font-family:'Archivo'; font-weight:600; font-size:8.8pt; color:var(--gold); width:0.35in; text-align:right;">{pg:02d}</div>
      </div>
      <div style="font-family:'Inter'; font-size:8.1pt; color:var(--gray);">{desc}</div>
    </div>''' for title, desc, pg in chapters[:9]])
rows2 = "".join([f'''
    <div style="padding:0.075in 0; border-bottom:1px solid var(--line);">
      <div style="display:flex; align-items:baseline;">
        <div style="font-family:'Playfair'; font-weight:700; font-size:10.8pt; color:var(--navy); flex:1;">{title}</div>
        <div style="font-family:'Archivo'; font-weight:600; font-size:8.8pt; color:var(--gold); width:0.35in; text-align:right;">{pg:02d}</div>
      </div>
      <div style="font-family:'Inter'; font-size:8.1pt; color:var(--gray);">{desc}</div>
    </div>''' for title, desc, pg in chapters[9:]])

add(f'''
<div class="page">
  <div class="frame">
    <div class="eyebrow">WELCOME TO THE GUIDEBOOK</div>
    <div style="height:0.2in;"></div>
    <h1 class="display" style="font-size:22pt; color:var(--navy); max-width:8.4in;">Everything you need to move from inspiration to understanding.</h1>
    <div style="height:0.14in;"></div>
    <p class="lede" style="max-width:8.2in; font-size:10.3pt;">
      This guidebook exists to answer five questions honestly: why this matters, what the
      system is, how it works, why it is different, and what results your church can expect.
      Read it in order, or jump to the chapter that matters most to you right now.
    </p>
    <div style="height:0.18in;"></div>
    <div style="display:flex; gap:0.5in;">
      <div style="flex:1;">{rows1}</div>
      <div style="flex:1;">{rows2}</div>
    </div>
  </div>
  {folio("Welcome", 2)}
</div>
''')

# =================================================================
# PAGE 3 — CH.1 THE FUTURE OF CHURCH FORMATION
# =================================================================
add(f'''
<div class="page">
  <div class="frame" style="display:flex; gap:0.75in;">
    <div style="width:4.5in; display:flex; flex-direction:column; justify-content:center;">
      <div class="eyebrow">CHAPTER ONE &mdash; THE FUTURE OF CHURCH FORMATION</div>
      <div style="height:0.28in;"></div>
      <h1 class="display" style="font-size:31pt; color:var(--navy);">Formation is becoming the work of the whole church, all week long.</h1>
      <div style="height:0.22in;"></div>
      <p class="lede">
        For a hundred years, the center of church life was the Sunday service. That is not
        wrong &mdash; it is simply no longer sufficient. People are formed by what they hear once
        a week far less than they are formed by what they practice every day, in community,
        at home.
      </p>
      <div style="height:0.16in;"></div>
      <p class="lede">
        The churches shaping the next generation will not simply preach well. They will build
        formation systems &mdash; ordinary rhythms that carry a message from the platform into
        daily life, without requiring a bigger staff or a bigger budget.
      </p>
      <div style="height:0.2in;"></div>
      <div class="takeaway">
        <span class="label">The shift underway</span>
        From church as a place you attend, to church as a formation system you live inside.
      </div>
    </div>
    <div style="flex:1;">{photo("PHOTOGRAPHY — CONGREGATION IN WORSHIP, WIDE SHOT, WARM LIGHT", "height:100%;")}</div>
  </div>
  {folio("The Future of Church Formation", 3)}
</div>
''')

# =================================================================
# PAGE 4 — CH.2 WHY MOST SERMONS END TOO SOON
# =================================================================
reasons = [
    ("No next step", "The sermon ends and nothing carries it into the week."),
    ("No shared language", "Groups, families, and staff each go their own direction."),
    ("No format beyond the stage", "A great message exists in only one form, spoken once."),
    ("No time to build more", "Staff capacity ends at the manuscript, not the curriculum."),
]
reason_cards = "".join([f'''
    <div style="flex:1; border-top:2px solid var(--gold); padding-top:0.16in;">
      <div style="font-family:'Playfair'; font-weight:700; font-size:13.5pt; color:var(--navy); margin-bottom:0.08in;">{t}</div>
      <div style="font-family:'Inter'; font-size:9.4pt; color:var(--ink); line-height:1.5;">{d}</div>
    </div>''' for t, d in reasons])

add(f'''
<div class="page">
  <div class="frame">
    <div class="eyebrow">CHAPTER TWO &mdash; WHY MOST SERMONS END TOO SOON</div>
    <div style="height:0.26in;"></div>
    <h1 class="display" style="font-size:29pt; color:var(--navy); max-width:8.2in;">A sermon is a moment. Formation is a path.</h1>
    <div style="height:0.18in;"></div>
    <p class="lede" style="max-width:8in;">
      Most churches don&rsquo;t lack good preaching. They lack a system to carry that preaching
      forward. Four gaps show up again and again:
    </p>
    <div style="height:0.3in;"></div>
    <div style="display:flex; gap:0.4in;">{reason_cards}</div>
    <div style="height:0.4in;"></div>
    <div class="pull-quote">Your greatest sermons deserve <span class="mark">more than one Sunday.</span></div>
  </div>
  {folio("Why Most Sermons End Too Soon", 4)}
</div>
''')

# =================================================================
# PAGE 5 — CH.3 FROM MESSAGE TO MOVEMENT
# =================================================================
add(f'''
<div class="page navy">
  <div class="frame">
    <div class="eyebrow">CHAPTER THREE &mdash; FROM MESSAGE TO MOVEMENT</div>
    <div style="height:0.2in;"></div>
    <h1 class="display" style="font-size:27pt; color:#FBF8F1;">What becomes possible with a system underneath it</h1>
    <div style="width:100%; height:2.5in;">{message_movement_diagram()}</div>
    <div style="height:0.05in;"></div>
    <div style="width:100%; height:1.7in;">{step_chain_diagram([("SERMON","One message, studied and preached with care."),("CURRICULUM","Shaped into formats groups and families can use."),("COMMUNITY","Lived out together, in real relationship.")])}</div>
    <div style="height:0.1in;"></div>
    <div class="pull-quote" style="max-width:7.5in;">One message. <span class="mark">Many forms. One movement.</span></div>
  </div>
  {folio("From Message to Movement", 5)}
</div>
''')

# =================================================================
# PAGE 6 — CH.4/5 FRAMEWORK & FIVE ENVIRONMENTS (funnel)
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
  <div class="frame" style="display:flex; gap:0.7in;">
    <div style="width:4.3in; display:flex; flex-direction:column; justify-content:center;">
      <div class="eyebrow">CHAPTERS FOUR &amp; FIVE &mdash; THE FRAMEWORK &amp; ENVIRONMENTS</div>
      <div style="height:0.24in;"></div>
      <h1 class="display" style="font-size:27pt; color:var(--navy);">Five environments. One deepening path.</h1>
      <div style="height:0.2in;"></div>
      <p class="lede">
        The Church Formation Framework names the five environments where a message keeps
        doing its work. Each environment reaches fewer people than the one before it &mdash;
        and forms each of them more deeply.
      </p>
      <div style="height:0.18in;"></div>
      <div class="takeaway">
        <span class="label">Why this matters</span>
        Breadth and depth are not in competition. A good system gives you both, on purpose.
      </div>
    </div>
    <div style="flex:1;">
      <div style="width:100%; height:5.9in;">{formation_funnel_diagram(funnel_stages)}</div>
    </div>
  </div>
  {folio("The Framework & Environments", 6)}
</div>
''')

# =================================================================
# PAGE 7 — CH.6 WEEKEND+GROUPS+DAILY+FAMILY+MISSION (Wheel)
# =================================================================
add(f'''
<div class="page">
  <div class="frame">
    <div class="eyebrow">CHAPTER SIX &mdash; WEEKEND + GROUPS + DAILY + FAMILY + MISSION</div>
    <div style="height:0.1in;"></div>
    <h1 class="display" style="font-size:27pt; color:var(--navy);">The Church Formation Wheel</h1>
    <div style="width:100%; height:5.2in;">{wheel_diagram()}</div>
    <div class="takeaway">
      <span class="label">Takeaway</span>
      The wheel turns every week &mdash; the same message moving through five environments, on repeat.
    </div>
  </div>
  {folio("Weekend, Groups, Daily, Family, Mission", 7)}
</div>
''')

# =================================================================
# PAGE 8 — CH.7 FIVE-STAGE PROCESS INTRO
# =================================================================
track_bar = "".join([f'<div class="track-chip">{t}</div>' for t in ["DISCERN","DEVELOP","PRODUCE","PUBLISH","MOBILIZE"]])
add(f'''
<div class="page navy">
  <div class="frame" style="display:flex; flex-direction:column; justify-content:center;">
    <div class="eyebrow">CHAPTER SEVEN &mdash; THE FIVE-STAGE PROCESS</div>
    <div style="height:0.28in;"></div>
    <h1 class="display" style="font-size:32pt; color:#FBF8F1; max-width:7.5in;">Five stages turn a sermon into a system.</h1>
    <div style="height:0.24in;"></div>
    <p class="lede" style="max-width:6.3in;">
      Every campaign your church builds moves through the same five disciplines. Learn them
      once, and your team can repeat them with every future message.
    </p>
    <div style="height:0.4in;"></div>
    <div style="display:flex; gap:0.14in;">{track_bar}</div>
  </div>
  {folio("The Five-Stage Process", 8)}
</div>
''')

# =================================================================
# PAGE 9 — FIVE-STAGE PROCESS TRACKS 1-3
# =================================================================
def track_card(name, sub, para, bullets):
    bl = "".join([f'<li>{b}</li>' for b in bullets])
    return f'''
    <div class="track-card">
      <div style="font-family:'Archivo'; font-weight:700; font-size:12pt; letter-spacing:0.15em; color:var(--gold);">{name}</div>
      <div style="font-family:'Playfair'; font-weight:700; font-size:14.5pt; color:var(--navy); margin:0.06in 0 0.12in;">{sub}</div>
      <p style="font-family:'Inter'; font-size:9.4pt; line-height:1.5; color:var(--ink); min-height:0.85in;">{para}</p>
      <ul class="track-list">{bl}</ul>
    </div>'''

tracks_1_3 = [
    ("DISCERN", "Hearing it clearly", "A team identifies the one true center of a message &mdash; the single idea everything else will serve.",
     ["Name the one idea worth building around", "Separate the message from the moment", "Identify the Scripture that carries it", "Spot where it touches daily life"]),
    ("DEVELOP", "Shaping the path", "A message becomes a multi-week arc with its own pacing and spiritual logic, not just a topic list.",
     ["Map the week-by-week arc", "Set the pace between conviction and rest", "Build in the turn toward application", "Design the invitation at the end"]),
    ("PRODUCE", "Building every format", "The arc becomes curriculum, devotionals, and training, each shaped for how it will actually be used.",
     ["Write small group discussion guides", "Draft daily devotional content", "Build a leader training kit", "Prepare family conversation prompts"]),
]
add(f'''
<div class="page">
  <div class="frame">
    <div class="eyebrow">THE FIVE-STAGE PROCESS &mdash; STAGES ONE THROUGH THREE</div>
    <div style="height:0.24in;"></div>
    <div style="display:flex; gap:0.4in;">{"".join([track_card(*t) for t in tracks_1_3])}</div>
  </div>
  {folio("The Five-Stage Process", 9)}
</div>
''')

# =================================================================
# PAGE 10 — FIVE-STAGE PROCESS TRACKS 4-5 + quote
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
    <div style="height:0.24in;"></div>
    <div style="display:flex; gap:0.5in;">
      <div style="width:6.5in; display:flex; gap:0.4in;">{"".join([track_card(*t) for t in tracks_4_5])}</div>
      <div style="flex:1; display:flex; align-items:center;">
        <div class="pull-quote">Your team doesn&rsquo;t just receive curriculum. <span class="mark">They learn to build it, every time.</span></div>
      </div>
    </div>
  </div>
  {folio("The Five-Stage Process", 10)}
</div>
''')

# =================================================================
# PAGE 11 — CH.8 CAMPAIGN ARCHITECTURE (lifecycle diagram)
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
    <div class="eyebrow">CHAPTER EIGHT &mdash; CAMPAIGN ARCHITECTURE</div>
    <div style="height:0.1in;"></div>
    <div style="display:flex; justify-content:space-between; align-items:flex-end;">
      <h1 class="display" style="font-size:26pt; color:var(--navy);">The Campaign Lifecycle</h1>
      <div class="takeaway" style="max-width:2.7in;">
        <span class="label">Why it matters</span>
        No campaign is a one-time event. Every one seeds the next.
      </div>
    </div>
    <div style="width:100%; height:5.1in;">{campaign_lifecycle_diagram(lifecycle_stages)}</div>
  </div>
  {folio("Campaign Architecture", 11)}
</div>
''')

# =================================================================
# PAGE 12 — CH.9 THE PASTOR CONTENT LIBRARY
# =================================================================
add(f'''
<div class="page">
  <div class="frame">
    <div class="eyebrow">CHAPTER NINE &mdash; THE PASTOR CONTENT LIBRARY</div>
    <div style="height:0.2in;"></div>
    <h1 class="display" style="font-size:26pt; color:var(--navy); max-width:8in;">A library that compounds every year you build it.</h1>
    <div style="height:0.16in;"></div>
    <p class="lede" style="max-width:8in;">
      Every campaign you build stays in your library &mdash; ready to relaunch, adapt, or hand to
      a new group of leaders. Five years in, most churches are running almost entirely on
      content they already own.
    </p>
    <div style="height:0.2in;"></div>
    <div style="width:100%; height:4.2in;">{content_library_diagram()}</div>
  </div>
  {folio("The Pastor Content Library", 12)}
</div>
''')

# =================================================================
# PAGE 13 — CH.10 AI AS MINISTRY MULTIPLIER
# =================================================================
add(f'''
<div class="page navy">
  <div class="frame" style="display:flex; gap:0.75in;">
    <div style="width:4.7in; display:flex; flex-direction:column; justify-content:center;">
      <div class="eyebrow">CHAPTER TEN &mdash; AI AS MINISTRY MULTIPLIER</div>
      <div style="height:0.24in;"></div>
      <h1 class="display" style="font-size:28pt; color:#FBF8F1;">A multiplier for your message, never a substitute for it.</h1>
      <div style="height:0.2in;"></div>
      <p class="lede">
        AI does not write your theology, and it does not preach your sermon. It takes what
        you have already studied and prayed over, and helps produce the devotionals,
        discussion guides, and training materials that would otherwise take a team of
        writers months to complete.
      </p>
      <div style="height:0.16in;"></div>
      <p class="lede">
        Every word is still reviewed by pastors for theology, tone, and truth before it
        reaches your congregation.
      </p>
    </div>
    <div style="flex:1; display:flex; flex-direction:column; justify-content:center; gap:0.3in;">
      <div class="equation">
        <span>One message</span><span class="op">&times;</span><span>AI production</span><span class="op">=</span><span class="result">Nine formats</span>
      </div>
      <div class="takeaway">
        <span class="label">Without AI</span>
        Producing nine formats from one message once cost $15,000&ndash;$40,000 in writing alone.
      </div>
      <div class="takeaway">
        <span class="label">With AI</span>
        The same nine formats can be produced in days, at a fraction of the cost, with every word still pastor-reviewed.
      </div>
    </div>
  </div>
  {folio("AI as Ministry Multiplier", 13)}
</div>
''')

# =================================================================
# PAGE 14 — CH.11 21/30/40-DAY JOURNEYS
# =================================================================
journeys = [
    ("21-Day Challenge", "A focused sprint", "Best for a single habit, a launch moment, or a season with limited attention &mdash; like January or a new sermon series kickoff."),
    ("30-Day Journey", "A full month", "Best for a themed month tied to the calendar &mdash; stewardship in the fall, prayer in January, family in May."),
    ("40-Day Campaign", "A complete season", "Best for your most significant churchwide moments &mdash; the journeys people will remember years later."),
]
journey_cards = "".join([f'''
    <div class="offer-card">
      <div style="width:34px; height:2px; background:var(--gold); margin-bottom:0.2in;"></div>
      <div style="font-family:'Playfair'; font-weight:700; font-size:16pt; color:var(--navy); line-height:1.2;">{name}</div>
      <div style="font-family:'Archivo'; font-weight:600; font-size:9pt; letter-spacing:0.1em; text-transform:uppercase; color:var(--gold); margin:0.1in 0 0.16in;">{sub}</div>
      <p style="font-family:'Inter'; font-size:9.6pt; line-height:1.55; color:var(--ink);">{desc}</p>
    </div>''' for name, sub, desc in journeys])
add(f'''
<div class="page">
  <div class="frame">
    <div class="eyebrow">CHAPTER ELEVEN &mdash; 21, 30, AND 40-DAY JOURNEYS</div>
    <div style="height:0.22in;"></div>
    <h1 class="display" style="font-size:27pt; color:var(--navy); max-width:8in;">Choosing the right length for the moment.</h1>
    <div style="height:0.3in;"></div>
    <div style="display:flex; gap:0.4in;">{journey_cards}</div>
    <div style="height:0.3in;"></div>
    <div class="takeaway">
      <span class="label">How to choose</span>
      Match the length to the weight of the moment, not the other way around &mdash; a 40-day format on a light topic will feel padded, and a 21-day format on a heavy one will feel rushed.
    </div>
  </div>
  {folio("21, 30, and 40-Day Journeys", 14)}
</div>
''')

# =================================================================
# PAGE 15 — CH.12 MINISTRY PUBLISHING SYSTEM
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
    <div class="eyebrow">CHAPTER TWELVE &mdash; THE MINISTRY PUBLISHING SYSTEM</div>
    <div style="height:0.2in;"></div>
    <h1 class="display" style="font-size:27pt; color:var(--navy);">From a rough draft to a finished, launch-ready resource.</h1>
    <div style="height:0.16in;"></div>
    <p class="lede" style="max-width:8in;">
      A campaign is only as strong as its final execution. The Publishing System is the
      quality bar every resource passes through before it reaches your church.
    </p>
    <div style="width:100%; height:3.9in;">{step_chain_diagram(pub_steps)}</div>
  </div>
  {folio("The Ministry Publishing System", 15)}
</div>
''')

# =================================================================
# PAGE 16 — CH.13 ANNUAL FORMATION CALENDAR
# =================================================================
calendar_stops = [
    ("Jan &ndash; Feb", "New Year vision and spiritual growth campaign"),
    ("Mar &ndash; Apr", "An Easter season journey toward the resurrection"),
    ("May &ndash; Jun", "A family and relationships campaign"),
    ("Jul &ndash; Aug", "A lighter 21-day summer challenge"),
    ("Sep &ndash; Oct", "A prayer or discipleship-deepening season"),
    ("Nov &ndash; Dec", "A stewardship and generosity campaign into the new year"),
]
add(f'''
<div class="page">
  <div class="frame">
    <div class="eyebrow">CHAPTER THIRTEEN &mdash; THE ANNUAL FORMATION CALENDAR</div>
    <div style="height:0.2in;"></div>
    <h1 class="display" style="font-size:27pt; color:var(--navy);">A rhythm for the whole church year</h1>
    <div style="height:0.2in;"></div>
    <p class="lede" style="max-width:8in;">
      Most churches plan one series at a time. A formation calendar plans the whole year at
      once &mdash; so every campaign has a season, and no two seasons compete for attention.
    </p>
    <div style="height:0.24in;"></div>
    <div style="width:100%; height:2.5in;">{generic_timeline(calendar_stops)}</div>
    <div style="height:0.3in;"></div>
    <div class="takeaway">
      <span class="label">Practical takeaway</span>
      Plan the calendar a full year ahead, then build one campaign at a time inside it &mdash; the calendar is the map, not the workload.
    </div>
  </div>
  {folio("The Annual Formation Calendar", 16)}
</div>
''')

# =================================================================
# PAGE 17 — CH.14 CRAWL WALK RUN
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
    <div class="eyebrow">CHAPTER FOURTEEN &mdash; CRAWL, WALK, RUN</div>
    <div style="height:0.2in;"></div>
    <h1 class="display" style="font-size:27pt; color:var(--navy); max-width:8in;">Every church starts where it is, and grows from there.</h1>
    <div style="height:0.16in;"></div>
    <p class="lede" style="max-width:8in;">
      No church is asked to arrive fully built. Most move through these five levels over
      eighteen to twenty-four months, at whatever pace fits their staff and calendar.
    </p>
    <div style="width:100%; height:4.3in;">{generic_staircase(crawl_levels)}</div>
  </div>
  {folio("Crawl, Walk, Run", 17)}
</div>
''')

# =================================================================
# PAGE 18 — CH.15 CHURCH CASE STUDIES (placeholders)
# =================================================================
cases = [
    ("Church Name Placeholder", "Mid-size congregation &middot; Suburban", "40-Day Stewardship Campaign", "Small group participation increased [XX]% during the campaign season."),
    ("Church Name Placeholder", "Multisite congregation &middot; Urban", "30-Day Family Journey", "Households reported measurably stronger at-home spiritual conversation."),
    ("Church Name Placeholder", "Church plant &middot; Rural", "21-Day Prayer Challenge", "First-time small group sign-ups reached their highest point in the church's history."),
]
case_cards = "".join([f'''
    <div class="case-card">
      {photo("PHOTOGRAPHY PLACEHOLDER — CONGREGATION PORTRAIT", "height:1.7in;")}
      <div style="height:0.16in;"></div>
      <div style="font-family:'Playfair'; font-weight:700; font-size:13.5pt; color:var(--navy);">{name}</div>
      <div style="font-family:'Archivo'; font-weight:600; font-size:8.3pt; letter-spacing:0.08em; color:var(--gray); margin:0.04in 0 0.1in;">{meta}</div>
      <div style="font-family:'Archivo'; font-weight:600; font-size:8.6pt; letter-spacing:0.1em; text-transform:uppercase; color:var(--gold); margin-bottom:0.06in;">{campaign}</div>
      <p style="font-family:'Inter'; font-size:9.3pt; line-height:1.5; color:var(--ink);">{result}</p>
    </div>''' for name, meta, campaign, result in cases])

add(f'''
<div class="page">
  <div class="frame">
    <div class="eyebrow">CHAPTER FIFTEEN &mdash; CHURCH CASE STUDIES</div>
    <div style="height:0.2in;"></div>
    <h1 class="display" style="font-size:27pt; color:var(--navy);">What this looks like in real churches</h1>
    <div style="height:0.1in;"></div>
    <p class="lede" style="max-width:8in; font-size:10.5pt; color:var(--gray); font-style:italic;">Case studies below are shown in placeholder format, ready to be replaced with your church's own story and results.</p>
    <div style="height:0.24in;"></div>
    <div style="display:flex; gap:0.36in;">{case_cards}</div>
  </div>
  {folio("Church Case Studies", 18)}
</div>
''')

# =================================================================
# PAGE 19 — CH.16 FAQ
# =================================================================
faqs = [
    ("Do we have to give up our own preaching style?", "No. The system is built around your pastor's own messages &mdash; it organizes and extends your voice, it never replaces it."),
    ("Will this create more work for our staff?", "Most of the production work is handled for you. Your team's role is review and mobilization, not writing from scratch."),
    ("What if our church is small?", "The Crawl, Walk, Run model exists for this reason. Most small churches begin at Level One with a licensed campaign."),
    ("How much does this cost?", "Investment depends on the level of partnership you choose. A strategy conversation will give you a clear, specific answer."),
    ("How is AI used, and is it reviewed?", "AI helps produce first drafts of formats like devotionals and guides. Every piece is reviewed by pastors before your church ever sees it."),
]
faq_rows = "".join([f'''
    <div style="padding:0.16in 0; border-bottom:1px solid var(--line);">
      <div style="font-family:'Playfair'; font-weight:700; font-size:13pt; color:var(--navy); margin-bottom:0.06in;">{q}</div>
      <div style="font-family:'Inter'; font-size:9.8pt; color:var(--ink); line-height:1.55; max-width:7.6in;">{a}</div>
    </div>''' for q, a in faqs])
add(f'''
<div class="page">
  <div class="frame">
    <div class="eyebrow">CHAPTER SIXTEEN &mdash; FREQUENTLY ASKED QUESTIONS</div>
    <div style="height:0.2in;"></div>
    <h1 class="display" style="font-size:27pt; color:var(--navy);">Honest answers to common questions</h1>
    <div style="height:0.2in;"></div>
    {faq_rows}
  </div>
  {folio("Frequently Asked Questions", 19)}
</div>
''')

# =================================================================
# PAGE 20 — CH.17 CHURCH FORMATION PARTNERSHIP (+ leader pathway)
# =================================================================
leader_levels = [
    ("1", "Participant", "Experiences a campaign as a small group member."),
    ("2", "Group Leader", "Leads others through the discussion guide."),
    ("3", "Coach", "Trains and supports several group leaders."),
    ("4", "Campaign Builder", "Helps shape original campaigns for the church."),
]
add(f'''
<div class="page">
  <div class="frame">
    <div class="eyebrow">CHAPTER SEVENTEEN &mdash; THE CHURCH FORMATION PARTNERSHIP</div>
    <div style="height:0.16in;"></div>
    <h1 class="display" style="font-size:24pt; color:var(--navy); max-width:8.4in;">A twelve-month coaching relationship, not a one-time purchase.</h1>
    <div style="height:0.12in;"></div>
    <p class="lede" style="max-width:8in; font-size:11pt;">
      The Partnership pairs your team with ongoing coaching, planning, and content
      development as you build a full formation calendar &mdash; and as your own people grow
      into leaders inside the system.
    </p>
    <div style="height:0.12in;"></div>
    <div style="width:100%; height:2.5in;">{generic_staircase(leader_levels)}</div>
  </div>
  {folio("The Church Formation Partnership", 20)}
</div>
''')

# =================================================================
# PAGE 21 — CH.18 NEXT STEPS
# =================================================================
steps = [
    ("01", "Schedule a strategy conversation", "A complimentary conversation to talk through your church's specific season and needs."),
    ("02", "Choose your starting level", "Decide together whether to license, customize, or build an original campaign first."),
    ("03", "Build your first campaign", "Move through the five-stage process with our team alongside yours."),
    ("04", "Launch, and plan the next one", "Mobilize your church, then begin filling in your annual formation calendar."),
]
step_rows = "".join([f'''
    <div style="display:flex; gap:0.24in; padding:0.16in 0; border-bottom:1px solid var(--line);">
      <div style="font-family:'Playfair'; font-weight:700; font-size:20pt; color:var(--gold); width:0.6in;">{n}</div>
      <div>
        <div style="font-family:'Playfair'; font-weight:700; font-size:13.5pt; color:var(--navy); margin-bottom:0.04in;">{t}</div>
        <div style="font-family:'Inter'; font-size:9.8pt; color:var(--ink); line-height:1.5;">{d}</div>
      </div>
    </div>''' for n, t, d in steps])
add(f'''
<div class="page">
  <div class="frame">
    <div class="eyebrow">CHAPTER EIGHTEEN &mdash; NEXT STEPS</div>
    <div style="height:0.2in;"></div>
    <h1 class="display" style="font-size:27pt; color:var(--navy);">How to begin</h1>
    <div style="height:0.22in;"></div>
    <div style="max-width:6.6in;">{step_rows}</div>
  </div>
  {folio("Next Steps", 21)}
</div>
''')

# =================================================================
# PAGE 22 — CLOSING VISIONARY CHALLENGE
# =================================================================
add(f'''
<div class="page navy">
  <div class="photo" style="position:absolute; inset:0; border-radius:0;">
    <div class="cap" style="right:0.9in; bottom:0.6in; left:auto; text-align:right; font-size:7.6pt;">PHOTOGRAPHY — PASTOR AND YOUNGER LEADER IN CONVERSATION, CHURCH LOBBY, SOFT FOCUS</div>
  </div>
  <div style="position:absolute; inset:0; background:linear-gradient(80deg, rgba(16,30,56,0.96) 0%, rgba(16,30,56,0.74) 46%, rgba(16,30,56,0.2) 100%);"></div>
  <div class="frame" style="display:flex; flex-direction:column; justify-content:center;">
    <div class="eyebrow">A CLOSING CHALLENGE</div>
    <div style="height:0.28in;"></div>
    <h1 class="display" style="font-size:31pt; color:#FBF8F1; max-width:6.8in;">Your life&rsquo;s work deserves to keep discipling people long after you first preach it.</h1>
    <div style="height:0.22in;"></div>
    <p class="lede" style="max-width:6.2in;">
      Every message you have already prepared, every year of study behind your pulpit, is
      capable of forming people for years beyond the Sunday it was first spoken. The system
      simply gives it somewhere to go.
    </p>
  </div>
  {folio("A Closing Challenge", 22)}
</div>
''')

# =================================================================
# PAGE 23 — BACK COVER
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
        Schedule a complimentary Church Formation Strategy Conversation to talk through
        what this could look like for your church.
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
.track-chip{
  font-family:'Archivo'; font-weight:600; font-size:9.5pt; letter-spacing:0.14em;
  color:#D9B876; border:1px solid rgba(217,184,118,0.5); border-radius:20px;
  padding:0.09in 0.2in;
}
.track-card{ flex:1; }
.track-list{ list-style:none; padding:0; margin:0; }
.track-list li{
  font-family:'Inter'; font-size:9pt; color:var(--ink); line-height:1.5;
  padding:0.055in 0 0.055in 0.16in; position:relative; border-top:1px solid var(--line);
}
.track-list li::before{ content:'\\2013'; position:absolute; left:0; color:var(--gold); }
.offer-card{ flex:1; border-top:1px solid var(--line); padding-top:0.22in; }
.equation{
  display:flex; align-items:baseline; gap:0.18in; flex-wrap:wrap;
  font-family:'Playfair'; font-weight:700; font-size:15pt; color:#FBF8F1;
}
.equation .op{ color:var(--gold); font-size:16pt; }
.equation .result{ color:var(--gold-bright, #D9B876); }
.case-card{ flex:1; border-top:1px solid var(--line); padding-top:0.2in; }
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

with open("/home/claude/build/flagship.html", "w") as f:
    f.write(html)

print("Pages:", len(PAGES))
