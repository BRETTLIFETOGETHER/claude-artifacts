import base64

SECTIONS = []
def add(html): SECTIONS.append(html)

# ---------- reusable component helpers ----------

def eyebrow(text):
    return f'<div class="eyebrow">{text}</div>'

def pull_quote(html):
    return f'<div class="quote">{html}</div>'

def takeaway(label, text):
    return f'<div class="takeaway"><span class="tlabel">{label}</span>{text}</div>'

def stack_steps(steps, cycle=False):
    """steps: list of (label, caption). Renders a numbered vertical chain."""
    n = len(steps)
    items = ""
    for i, (label, caption) in enumerate(steps):
        last = (i == n - 1)
        items += f'''
        <div class="step">
          <div class="step-num-col">
            <div class="step-num">{i+1}</div>
            {'<div class="step-line"></div>' if not last or cycle else ''}
          </div>
          <div class="step-body">
            <div class="step-label">{label}</div>
            <div class="step-caption">{caption}</div>
          </div>
        </div>'''
    note = '<div class="cycle-note">&#8635;&nbsp; and back to the beginning &mdash; the cycle repeats</div>' if cycle else ''
    return f'<div class="steps">{items}</div>{note}'

def card_grid(cards):
    """cards: list of (title, desc) — simple 2-up reason cards"""
    items = "".join([f'''
      <div class="reason-card">
        <div class="reason-title">{t}</div>
        <div class="reason-desc">{d}</div>
      </div>''' for t, d in cards])
    return f'<div class="reason-grid">{items}</div>'

def offer_card(name, sub, desc, extra=""):
    return f'''
    <div class="offer-card">
      <div class="offer-rule"></div>
      <div class="offer-name">{name}</div>
      <div class="offer-sub">{sub}</div>
      <div class="offer-desc">{desc}</div>
      {extra}
    </div>'''

def spec_row(label, value):
    return f'<div class="spec-row"><div class="spec-label">{label}</div><div class="spec-value">{value}</div></div>'

def chips(items):
    return '<div class="chip-row">' + "".join([f'<div class="chip">{c}</div>' for c in items]) + '</div>'

def faq_item(q, a):
    return f'<div class="faq"><div class="faq-q">{q}</div><div class="faq-a">{a}</div></div>'

def section(inner_html, dark=False, extra_class=""):
    cls = "section dark" if dark else "section"
    if extra_class:
        cls += " " + extra_class
    return f'<section class="{cls}"><div class="inner">{inner_html}</div></section>'

# =================================================================
# HERO
# =================================================================
add(f'''
<section class="hero">
  <div class="inner">
    <div class="hero-kicker">THE COMPLETE GUIDE &amp; WAYS TO WORK TOGETHER</div>
    <h1 class="hero-title">The Church Formation System&trade;</h1>
    <p class="hero-tagline">Helping pastors turn sermons into curriculum &mdash; curriculum into
    community &mdash; and community into movements.</p>
    <div class="hero-foot">LIFETOGETHER.COM</div>
  </div>
</section>
''')

# =================================================================
# WELCOME
# =================================================================
add(section(f'''
  {eyebrow("WELCOME")}
  <h2>Everything you need to understand the system, and every way to build it with us.</h2>
  <p>This guide has two parts. <b>Part One</b> explains why this matters, what the system
  is, how it works, and what results your church can expect. <b>Part Two</b> lays out
  every way to work with us &mdash; from a single six-week Intensive to a full year of
  partnership. Read start to finish, or jump to whatever matters most right now.</p>
'''))

# =================================================================
# PART ONE — CH 1: FUTURE OF CHURCH FORMATION
# =================================================================
add(section(f'''
  {eyebrow("PART ONE &middot; CHAPTER ONE")}
  <h2>Formation is becoming the work of the whole church, all week long.</h2>
  <p>For a hundred years, the center of church life was the Sunday service. That is not
  wrong &mdash; it is simply no longer sufficient. People are formed by what they hear once a
  week far less than they are formed by what they practice every day, in community, at
  home.</p>
  <p>The churches shaping the next generation will not simply preach well. They will
  build formation systems &mdash; ordinary rhythms that carry a message from the platform
  into daily life, without requiring a bigger staff or a bigger budget.</p>
  {takeaway("The shift underway", "From church as a place you attend, to church as a formation system you live inside.")}
'''))

# =================================================================
# CH 2: WHY MOST SERMONS END TOO SOON
# =================================================================
reasons = [
    ("No next step", "The sermon ends and nothing carries it into the week."),
    ("No shared language", "Groups, families, and staff each go their own direction."),
    ("No format beyond the stage", "A great message exists in only one form, spoken once."),
    ("No time to build more", "Staff capacity ends at the manuscript, not the curriculum."),
]
add(section(f'''
  {eyebrow("CHAPTER TWO")}
  <h2>A sermon is a moment. Formation is a path.</h2>
  <p>Most churches don&rsquo;t lack good preaching. They lack a system to carry that
  preaching forward. Four gaps show up again and again:</p>
  {card_grid(reasons)}
  {pull_quote('Your greatest sermons deserve <span class="gold">more than one Sunday.</span>')}
'''))

# =================================================================
# CH 3: FROM MESSAGE TO MOVEMENT
# =================================================================
add(section(f'''
  {eyebrow("CHAPTER THREE")}
  <h2 class="on-dark">What becomes possible with a system underneath it</h2>
  {stack_steps([
      ("MESSAGE", "One message, prepared once."),
      ("CURRICULUM", "Shaped into a resource groups and families can use."),
      ("COMMUNITY", "Practiced together, in real relationship."),
      ("MOVEMENT", "Carried into lasting, visible change."),
  ])}
  {pull_quote('One message. <span class="gold">Many forms. One movement.</span>')}
''', dark=True))

# =================================================================
# CH 4: FRAMEWORK & FIVE ENVIRONMENTS (funnel as depth list)
# =================================================================
add(section(f'''
  {eyebrow("CHAPTER FOUR")}
  <h2>Five environments. One deepening path.</h2>
  <p>The Church Formation Framework names the five environments where a message keeps
  doing its work. Each environment reaches fewer people than the one before it &mdash; and
  forms each of them more deeply.</p>
  {stack_steps([
      ("WEEKEND", "The whole church hears one message together."),
      ("GROUPS", "Circles of real relationship discuss it."),
      ("DAILY", "Individuals practice it in a daily rhythm."),
      ("FAMILY", "Households carry it into the home."),
      ("MISSION", "A shaped few carry it into the world."),
  ])}
  {takeaway("Why this matters", "Breadth and depth are not in competition. A good system gives you both, on purpose.")}
'''))

# =================================================================
# CH 5: THE CHURCH FORMATION WHEEL (cycle)
# =================================================================
add(section(f'''
  {eyebrow("CHAPTER FIVE")}
  <h2>The Church Formation Wheel</h2>
  <p>The same five environments, in motion. The wheel turns every week &mdash; the message
  never stops moving through the life of the church.</p>
  {stack_steps([
      ("WEEKEND", "The message is preached with clarity and conviction."),
      ("GROUPS", "The message is discussed in circles of real relationship."),
      ("DAILY", "The message becomes a daily rhythm of reflection."),
      ("FAMILY", "The message shapes conversation around the table."),
      ("MISSION", "The message moves outward into action."),
  ], cycle=True)}
'''))

# =================================================================
# CH 6: FIVE-STAGE PROCESS
# =================================================================
add(section(f'''
  {eyebrow("CHAPTER SIX")}
  <h2 class="on-dark">Five stages turn a sermon into a system.</h2>
  <p class="on-dark-p">Every campaign your church builds moves through the same five
  disciplines. Learn them once, and your team can repeat them with every future message.</p>
  {chips(["DISCERN","DEVELOP","PRODUCE","PUBLISH","MOBILIZE"])}
''', dark=True))

stage_details = [
    ("DISCERN", "Hearing it clearly", "A team identifies the one true center of a message &mdash; the single idea everything else will serve.",
     ["Name the one idea worth building around", "Separate the message from the moment", "Identify the Scripture that carries it", "Spot where it touches daily life"]),
    ("DEVELOP", "Shaping the path", "A message becomes a multi-week arc with its own pacing and spiritual logic, not just a topic.",
     ["Map the week-by-week arc", "Set the pace between conviction and rest", "Build in the turn toward application", "Design the invitation at the end"]),
    ("PRODUCE", "Building every format", "The arc becomes curriculum, devotionals, and training, each shaped for how it will actually be used.",
     ["Write small group discussion guides", "Draft daily devotional content", "Build a leader training kit", "Prepare family conversation prompts"]),
    ("PUBLISH", "Packaging with excellence", "The finished campaign is designed, proofed, and formatted so it feels like a resource, not a handout.",
     ["Design a cover and visual identity", "Typeset every printed and digital piece", "Proof theology, tone, and Scripture", "Prepare it for licensing or release"]),
    ("MOBILIZE", "Getting it into hands", "A campaign only forms people if it launches well, so this stage ends with a real activation plan.",
     ["Build the launch and promotion plan", "Train leaders to carry the content well", "Prepare the pulpit announcement path", "Plan the on-ramp to what comes next"]),
]
stage_html = ""
for name, sub, para, bullets in stage_details:
    bl = "".join([f"<li>{b}</li>" for b in bullets])
    stage_html += f'''
    <div class="stage-card">
      <div class="stage-name">{name}</div>
      <div class="stage-sub">{sub}</div>
      <p class="stage-desc">{para}</p>
      <ul class="stage-list">{bl}</ul>
    </div>'''
add(section(stage_html + pull_quote('Your team doesn&rsquo;t just receive curriculum. <span class="gold">They learn to build it, every time.</span>')))

# =================================================================
# CH 7: CAMPAIGN ARCHITECTURE (lifecycle, cycle)
# =================================================================
add(section(f'''
  {eyebrow("CHAPTER SEVEN")}
  <h2>The Campaign Lifecycle</h2>
  <p>Campaign Architecture is how one campaign is built &mdash; and how it lives on. No
  campaign is a one-time event. Every one seeds the next.</p>
  {stack_steps([
      ("PLAN", "Choose the theme and the season."),
      ("BUILD", "Produce every format from one message."),
      ("LAUNCH", "Mobilize the whole church together."),
      ("SUSTAIN", "Reinforce it through groups and daily practice."),
      ("MULTIPLY", "Let it shape the next campaign."),
  ], cycle=True)}
'''))

# =================================================================
# CH 8: PASTOR CONTENT LIBRARY
# =================================================================
years = [("Year 1", 5), ("Year 2", 11), ("Year 3", 19), ("Year 4", 28), ("Year 5+", 40)]
max_v = max(v for _, v in years)
bars = "".join([f'''
  <div class="bar-row">
    <div class="bar-label">{yr}</div>
    <div class="bar-track"><div class="bar-fill" style="width:{v/max_v*100:.0f}%;"></div></div>
    <div class="bar-value">{v}</div>
  </div>''' for yr, v in years])
add(section(f'''
  {eyebrow("CHAPTER EIGHT")}
  <h2>A library that compounds every year you build it.</h2>
  <p>Every campaign you build stays in your library &mdash; ready to relaunch, adapt, or hand
  to a new group of leaders. Five years in, most churches are running almost entirely on
  content they already own.</p>
  <div class="bar-chart">{bars}</div>
  <div class="bar-caption">CUMULATIVE CAMPAIGNS IN YOUR LIBRARY</div>
'''))

# =================================================================
# CH 9: AI AS MINISTRY MULTIPLIER
# =================================================================
add(section(f'''
  {eyebrow("CHAPTER NINE")}
  <h2 class="on-dark">A multiplier for your message, never a substitute for it.</h2>
  <p class="on-dark-p">AI does not write your theology, and it does not preach your
  sermon. It takes what you have already studied and prayed over, and helps produce the
  devotionals, discussion guides, and training materials that would otherwise take a
  team of writers months to complete. Every word is still reviewed by pastors for
  theology, tone, and truth before it reaches your congregation.</p>
  <div class="equation">One message &nbsp;<span class="gold">&times;</span>&nbsp; AI production &nbsp;<span class="gold">=</span>&nbsp; <span class="gold">Nine formats</span></div>
  {takeaway("Without AI", "Producing nine formats from one message once cost $15,000&ndash;$40,000 in writing alone.")}
  {takeaway("With AI", "The same nine formats can be produced in days, at a fraction of the cost, with every word still pastor-reviewed.")}
''', dark=True))

# =================================================================
# CH 10: 21/30/40-DAY JOURNEYS
# =================================================================
journeys = [
    ("21-Day Challenge", "A focused sprint", "Best for a single habit, a launch moment, or a season with limited attention &mdash; like January or a new sermon series kickoff."),
    ("30-Day Journey", "A full month", "Best for a themed month tied to the calendar &mdash; stewardship in the fall, prayer in January, family in May."),
    ("40-Day Campaign", "A complete season", "Best for your most significant churchwide moments &mdash; the journeys people will remember years later."),
]
add(section(f'''
  {eyebrow("CHAPTER TEN")}
  <h2>Choosing the right length for the moment.</h2>
  {"".join([offer_card(n,s,d) for n,s,d in journeys])}
  {takeaway("How to choose", "Match the length to the weight of the moment &mdash; a 40-day format on a light topic will feel padded, and a 21-day format on a heavy one will feel rushed.")}
'''))

# =================================================================
# CH 11: MINISTRY PUBLISHING SYSTEM
# =================================================================
add(section(f'''
  {eyebrow("CHAPTER ELEVEN")}
  <h2>From a rough draft to a finished, launch-ready resource.</h2>
  <p>A campaign is only as strong as its final execution. The Publishing System is the
  quality bar every resource passes through before it reaches your church.</p>
  {stack_steps([
      ("DRAFT", "The message and study content are written and organized."),
      ("DESIGN", "A visual identity and layout are applied to every piece."),
      ("PROOF", "Theology, tone, and Scripture are reviewed line by line."),
      ("PACKAGE", "Print and digital formats are finalized and tested."),
      ("RELEASE", "The finished campaign is delivered, ready to launch."),
  ])}
'''))

# =================================================================
# CH 12: ANNUAL FORMATION CALENDAR
# =================================================================
add(section(f'''
  {eyebrow("CHAPTER TWELVE")}
  <h2>A rhythm for the whole church year</h2>
  <p>Most churches plan one series at a time. A formation calendar plans the whole year
  at once &mdash; so every campaign has a season, and no two seasons compete for attention.</p>
  {stack_steps([
      ("JAN&ndash;FEB", "New Year vision and spiritual growth campaign."),
      ("MAR&ndash;APR", "An Easter season journey toward the resurrection."),
      ("MAY&ndash;JUN", "A family and relationships campaign."),
      ("JUL&ndash;AUG", "A lighter 21-day summer challenge."),
      ("SEP&ndash;OCT", "A prayer or discipleship-deepening season."),
      ("NOV&ndash;DEC", "A stewardship and generosity campaign into the new year."),
  ])}
  {takeaway("Practical takeaway", "Plan the calendar a full year ahead, then build one campaign at a time inside it.")}
'''))

# =================================================================
# CH 13: CRAWL WALK RUN
# =================================================================
add(section(f'''
  {eyebrow("CHAPTER THIRTEEN")}
  <h2>Every church starts where it is, and grows from there.</h2>
  <p>No church is asked to arrive fully built. Most move through these five levels over
  eighteen to twenty-four months, at whatever pace fits their staff and calendar.</p>
  {stack_steps([
      ("USE OURS", "Launch proven Lifetogether campaigns as they are."),
      ("CUSTOMIZE OURS", "Adapt content and language to your church's voice."),
      ("BUILD YOURS", "Create original campaigns from your pastor's own messages."),
      ("PUBLISH YOURS", "Package your campaigns for other churches to license."),
      ("MULTIPLY YOURS", "Train other pastors to build within your formation system."),
  ])}
'''))

# =================================================================
# CH 14: CASE STUDIES
# =================================================================
cases = [
    ("Church Name Placeholder", "Mid-size congregation &middot; Suburban", "40-Day Stewardship Campaign", "Small group participation increased [XX]% during the campaign season."),
    ("Church Name Placeholder", "Multisite congregation &middot; Urban", "30-Day Family Journey", "Households reported measurably stronger at-home spiritual conversation."),
    ("Church Name Placeholder", "Church plant &middot; Rural", "21-Day Prayer Challenge", "First-time small group sign-ups reached their highest point in the church's history."),
]
case_html = "".join([f'''
  <div class="case-card">
    <div class="case-name">{name}</div>
    <div class="case-meta">{meta}</div>
    <div class="case-campaign">{campaign}</div>
    <p class="case-result">{result}</p>
  </div>''' for name, meta, campaign, result in cases])
add(section(f'''
  {eyebrow("CHAPTER FOURTEEN")}
  <h2>What this looks like in real churches</h2>
  <p class="fine-print">Case studies below are shown in placeholder format, ready to be replaced with your church&rsquo;s own story and results.</p>
  {case_html}
'''))

# =================================================================
# CH 15: FAQ
# =================================================================
faqs = [
    ("Do we have to give up our own preaching style?", "No. The system is built around your pastor's own messages &mdash; it organizes and extends your voice, it never replaces it."),
    ("Will this create more work for our staff?", "Most of the production work is handled for you. Your team's role is review and mobilization, not writing from scratch."),
    ("What if our church is small?", "The Crawl, Walk, Run model exists for this reason. Most small churches begin at Level One with a licensed campaign."),
    ("How much does this cost?", "It depends on the level of partnership you choose &mdash; see Multiple Offerings, next, for the three ways to work with us."),
    ("How is AI used, and is it reviewed?", "AI helps produce first drafts of formats like devotionals and guides. Every piece is reviewed by pastors before your church ever sees it."),
]
add(section(f'''
  {eyebrow("CHAPTER FIFTEEN")}
  <h2>Honest answers to common questions</h2>
  {"".join([faq_item(q,a) for q,a in faqs])}
'''))

# =================================================================
# PART TWO DIVIDER
# =================================================================
add(section(f'''
  {eyebrow("PART TWO &middot; WAYS TO WORK TOGETHER")}
  <h2 class="on-dark">Multiple offerings, one system.</h2>
  <p class="on-dark-p">Everything in Part One is the same system, whichever way you enter
  it. Some churches need one campaign built well over six weeks. Others are ready to
  build a whole year of formation. What follows are the three ways to work with us &mdash;
  so you can choose the level of partnership that fits your church right now.</p>
  {chips(["CAMPAIGN BUILDER INTENSIVE","90-DAY ACCELERATOR","ANNUAL PARTNERSHIP"])}
''', dark=True))

# =================================================================
# OFFERING 1: CAMPAIGN BUILDER INTENSIVE
# =================================================================
add(section(f'''
  {eyebrow("OFFERING ONE")}
  <h2>The Campaign Builder Intensive</h2>
  <p><b>Six weeks. One complete campaign blueprint.</b> A collaborative, six-week
  planning process that turns a pastor&rsquo;s own message into a complete, launch-ready
  campaign &mdash; built with your team, not delivered to them. It is not curriculum
  writing, and it is not coaching alone.</p>
  {chips(["WEEK 1 DISCOVER","WEEK 2 DISCERN","WEEK 3 DESIGN","WEEK 4 DEVELOP","WEEK 5 PRODUCE","WEEK 6 LAUNCH"])}
  {takeaway("Best for", "Churches preparing to launch a vision, spiritual growth, stewardship, family, or prayer campaign &mdash; or any custom sermon-based journey.")}
  {takeaway("You walk away with", "Campaign strategy, sermon roadmap, curriculum outline, video plan, leader resources, promotion plan, launch calendar, and a Day 41 strategy.")}
  <p class="fine-print" style="margin-top:20px;">Almost every pastor we talk with already has more than enough vision and content to
  build a full campaign. What&rsquo;s missing isn&rsquo;t inspiration &mdash; it&rsquo;s a clear, guided
  process to get from a sermon idea to a finished, launch-ready experience.</p>
  {pull_quote('You already have the message. <span class="gold">You just need the process to build with it.</span>')}
'''))

# =================================================================
# OFFERING 2: 90-DAY ACCELERATOR
# =================================================================
add(section(f'''
  {eyebrow("OFFERING TWO")}
  <h2>The 90-Day Accelerator</h2>
  <p><b>From blueprint to a fully launched campaign.</b> The Intensive gives your church
  a complete plan. For churches who want hands-on help carrying that plan all the way to
  launch, the 90-Day Accelerator adds ongoing production support and coaching through
  the entire launch season.</p>
  {takeaway("Best for", "Churches ready to move quickly &mdash; from a finished blueprint to a fully launched campaign in one season.")}
'''))

# =================================================================
# OFFERING 3: ANNUAL FORMATION PARTNERSHIP (+ leader pathway)
# =================================================================
add(section(f'''
  {eyebrow("OFFERING THREE")}
  <h2 class="on-dark">The Annual Formation Partnership</h2>
  <p class="on-dark-p"><b>A twelve-month coaching relationship, not a one-time
  purchase.</b> The Partnership pairs your team with ongoing coaching, planning, and
  content development as you build a full formation calendar &mdash; and as your own people
  grow into leaders inside the system.</p>
  {stack_steps([
      ("PARTICIPANT", "Experiences a campaign as a small group member."),
      ("GROUP LEADER", "Leads others through the discussion guide."),
      ("COACH", "Trains and supports several group leaders."),
      ("CAMPAIGN BUILDER", "Helps shape original campaigns for the church."),
  ])}
''', dark=True))

# =================================================================
# INVESTMENT OVERVIEW (spec cards instead of a wide table)
# =================================================================
invest_html = f'''
  <div class="invest-card">
    <div class="invest-name">Campaign Builder Intensive</div>
    {spec_row("Length", "Six weeks")}
    {spec_row("Best for", "Your first campaign blueprint")}
    {spec_row("Format", "Guided weekly planning")}
    {spec_row("You leave with", "One completed campaign blueprint")}
    {spec_row("Investment", "A one-time program fee")}
  </div>
  <div class="invest-card">
    <div class="invest-name">90-Day Accelerator</div>
    {spec_row("Length", "One season (about 90 days)")}
    {spec_row("Best for", "Carrying a blueprint to a full launch")}
    {spec_row("Format", "Hands-on production &amp; launch support")}
    {spec_row("You leave with", "One fully launched campaign")}
    {spec_row("Investment", "A one-time program fee")}
  </div>
  <div class="invest-card">
    <div class="invest-name">Annual Formation Partnership</div>
    {spec_row("Length", "Twelve months")}
    {spec_row("Best for", "A whole year of formation, and a trained team")}
    {spec_row("Format", "Ongoing coaching &amp; team training")}
    {spec_row("You leave with", "A trained team and a repeatable system")}
    {spec_row("Investment", "An ongoing annual partnership fee")}
  </div>
'''
add(section(f'''
  {eyebrow("WAYS TO WORK TOGETHER &middot; AT A GLANCE")}
  <h2>Investment overview</h2>
  {invest_html}
  <p class="fine-print">Specific investment figures vary by church size and scope, and
  are confirmed during your strategy conversation.</p>
'''))

# =================================================================
# NEXT STEPS
# =================================================================
steps = [
    ("01", "Schedule a strategy conversation", "A complimentary conversation to talk through your church's specific season and needs."),
    ("02", "Choose your offering", "Intensive, Accelerator, or Partnership &mdash; whichever fits where your church is right now."),
    ("03", "Build your first campaign", "Move through the five-stage process with our team alongside yours."),
    ("04", "Launch, and plan the next one", "Mobilize your church, then begin filling in your annual formation calendar."),
]
steps_html = "".join([f'''
  <div class="numstep">
    <div class="numstep-n">{n}</div>
    <div>
      <div class="numstep-t">{t}</div>
      <div class="numstep-d">{d}</div>
    </div>
  </div>''' for n, t, d in steps])
add(section(f'''
  {eyebrow("NEXT STEPS")}
  <h2>How to begin</h2>
  {steps_html}
'''))

# =================================================================
# CLOSING
# =================================================================
add(f'''
<section class="closing">
  <div class="inner">
    <div class="eyebrow">YOUR MESSAGE MATTERS</div>
    <h2 class="on-dark">Your greatest sermons deserve more than one Sunday.</h2>
    <p class="on-dark-p">They deserve to become a movement that shapes lives, strengthens
    families, equips leaders, and leaves a legacy that outlives your ministry. You
    don&rsquo;t have to build it alone &mdash; and you don&rsquo;t have to build it all at once.</p>
    <div class="cta-btn">Let&rsquo;s Build It Together</div>
    <div class="closing-foot">LIFETOGETHER.COM &nbsp;&middot;&nbsp; BRETT@LIFETOGETHER.COM</div>
    <div class="closing-mark">THE CHURCH FORMATION SYSTEM&trade;</div>
  </div>
</section>
''')

# =================================================================
# CSS
# =================================================================
CSS = '''
@font-face { font-family:'Playfair'; src:url(FONT_PlayfairDisplay-Regular); font-weight:400; }
@font-face { font-family:'Playfair'; src:url(FONT_PlayfairDisplay-SemiBold); font-weight:600; }
@font-face { font-family:'Playfair'; src:url(FONT_PlayfairDisplay-Bold); font-weight:700; }
@font-face { font-family:'Playfair'; src:url(FONT_PlayfairDisplay-Italic); font-weight:400 600; font-style:italic; }
@font-face { font-family:'Inter'; src:url(FONT_Inter-Regular); font-weight:400; }
@font-face { font-family:'Inter'; src:url(FONT_Inter-Medium); font-weight:500; }
@font-face { font-family:'Inter'; src:url(FONT_Inter-SemiBold); font-weight:600; }
@font-face { font-family:'Inter'; src:url(FONT_Inter-Bold); font-weight:700; }
@font-face { font-family:'Archivo'; src:url(FONT_Archivo-Medium); font-weight:500; }
@font-face { font-family:'Archivo'; src:url(FONT_Archivo-SemiBold); font-weight:600; }
@font-face { font-family:'Archivo'; src:url(FONT_Archivo-Bold); font-weight:700; }

:root{
  --navy:#101E38; --gold:#B98D3E; --gold-bright:#D9B876;
  --white:#FBF8F1; --ink:#1C2230; --gray:#767E8E; --cream:#F1EBDD; --line:#DCD4C0;
}
*{ margin:0; padding:0; box-sizing:border-box; -webkit-text-size-adjust:100%; }
html{ background:var(--navy); }
body{ font-family:'Inter',sans-serif; color:var(--ink); background:var(--white); }

.section{ background:var(--white); }
.section.dark{ background:var(--navy); color:var(--white); }
.inner{ max-width:520px; margin:0 auto; padding:44px 24px; }

.hero{ background:var(--navy); background-image:linear-gradient(160deg,#16274A 0%,#0E1930 100%); }
.hero .inner{ padding:64px 24px 52px; text-align:left; }
.hero-kicker{ font-family:'Archivo'; font-weight:600; font-size:11.5px; letter-spacing:0.22em; color:var(--gold-bright); margin-bottom:20px; }
.hero-title{ font-family:'Playfair'; font-weight:700; font-size:34px; line-height:1.12; color:var(--white); margin-bottom:18px; }
.hero-tagline{ font-family:'Playfair'; font-style:italic; font-weight:500; font-size:17px; line-height:1.5; color:var(--gold-bright); max-width:420px; }
.hero-foot{ margin-top:40px; font-family:'Archivo'; font-weight:500; font-size:11px; letter-spacing:0.14em; color:rgba(251,248,241,0.55); }

.eyebrow{ font-family:'Archivo'; font-weight:600; font-size:11.5px; letter-spacing:0.16em; text-transform:uppercase; color:var(--gold); display:flex; align-items:center; gap:8px; margin-bottom:14px; }
.eyebrow::before{ content:''; width:20px; height:2px; background:var(--gold); flex-shrink:0; }
.dark .eyebrow{ color:var(--gold-bright); }
.dark .eyebrow::before{ background:var(--gold-bright); }

h2{ font-family:'Playfair'; font-weight:700; font-size:24px; line-height:1.22; color:var(--navy); margin-bottom:16px; }
h2.on-dark{ color:var(--white); }
p{ font-family:'Inter'; font-size:16px; line-height:1.62; color:var(--ink); margin-bottom:14px; }
p.on-dark-p{ color:rgba(251,248,241,0.9); }
p.fine-print{ font-size:13px; color:var(--gray); font-style:italic; }
.dark p.fine-print{ color:rgba(251,248,241,0.6); }
b{ font-weight:700; }

.quote{ font-family:'Playfair'; font-style:italic; font-weight:500; font-size:20px; line-height:1.4; color:var(--navy); margin:24px 0 4px; }
.dark .quote{ color:var(--white); }
.quote .gold{ color:var(--gold); font-style:normal; }
.dark .quote .gold{ color:var(--gold-bright); font-style:normal; }

.takeaway{ border-left:3px solid var(--gold); padding-left:14px; font-family:'Archivo'; font-weight:600; font-size:14.5px; line-height:1.55; color:var(--navy); margin:18px 0; }
.dark .takeaway{ color:var(--white); }
.tlabel{ display:block; font-size:11.5px; letter-spacing:0.14em; text-transform:uppercase; color:var(--gold); margin-bottom:5px; }
.dark .tlabel{ color:var(--gold-bright); }

/* step chain */
.steps{ margin:20px 0 6px; }
.step{ display:flex; gap:16px; }
.step-num-col{ display:flex; flex-direction:column; align-items:center; width:40px; flex-shrink:0; }
.step-num{ width:40px; height:40px; border-radius:50%; background:var(--navy); border:1.5px solid var(--gold); color:var(--gold-bright); font-family:'Playfair'; font-weight:700; font-size:16px; display:flex; align-items:center; justify-content:center; flex-shrink:0; }
.dark .step-num{ background:rgba(255,255,255,0.06); }
.step-line{ width:2px; flex:1; background:var(--gold); opacity:0.55; min-height:22px; }
.step-body{ padding-bottom:22px; padding-top:6px; }
.step-label{ font-family:'Archivo'; font-weight:700; font-size:13.5px; letter-spacing:0.06em; color:var(--navy); margin-bottom:4px; }
.dark .step-label{ color:var(--white); }
.step-caption{ font-family:'Inter'; font-size:14.5px; color:var(--gray); line-height:1.5; }
.dark .step-caption{ color:rgba(251,248,241,0.72); }
.cycle-note{ font-family:'Archivo'; font-size:12px; font-style:italic; color:var(--gold); letter-spacing:0.02em; padding-left:56px; margin-top:-8px; }
.dark .cycle-note{ color:var(--gold-bright); }

/* reason cards */
.reason-grid{ display:grid; grid-template-columns:1fr 1fr; gap:16px; margin:20px 0 4px; }
.reason-card{ border-top:2px solid var(--gold); padding-top:10px; }
.reason-title{ font-family:'Playfair'; font-weight:700; font-size:15px; color:var(--navy); margin-bottom:5px; line-height:1.25; }
.reason-desc{ font-family:'Inter'; font-size:13px; color:var(--ink); line-height:1.5; }

/* stage cards (five-stage detail) */
.stage-card{ border-top:1px solid var(--line); padding:20px 0; }
.stage-card:first-child{ border-top:none; padding-top:6px; }
.stage-name{ font-family:'Archivo'; font-weight:700; font-size:13px; letter-spacing:0.12em; color:var(--gold); }
.stage-sub{ font-family:'Playfair'; font-weight:700; font-size:19px; color:var(--navy); margin:4px 0 8px; }
.stage-desc{ font-size:15px; margin-bottom:10px; }
.stage-list{ list-style:none; }
.stage-list li{ font-size:14px; color:var(--ink); line-height:1.5; padding:6px 0 6px 16px; position:relative; border-top:1px solid var(--line); }
.stage-list li::before{ content:'\\2013'; position:absolute; left:0; color:var(--gold); }

/* offer cards (journeys) */
.offer-card{ border-top:1px solid var(--line); padding:20px 0; }
.offer-card:first-child{ border-top:none; padding-top:8px; }
.offer-rule{ width:26px; height:2px; background:var(--gold); margin-bottom:12px; }
.offer-name{ font-family:'Playfair'; font-weight:700; font-size:18px; color:var(--navy); }
.offer-sub{ font-family:'Archivo'; font-weight:600; font-size:11.5px; letter-spacing:0.1em; text-transform:uppercase; color:var(--gold); margin:6px 0 10px; }
.offer-desc{ font-size:14.5px; line-height:1.55; }

/* chips */
.chip-row{ display:flex; flex-wrap:wrap; gap:8px; margin:18px 0 4px; }
.chip{ font-family:'Archivo'; font-weight:600; font-size:11.5px; letter-spacing:0.06em; color:var(--gold); border:1px solid rgba(185,141,62,0.45); border-radius:20px; padding:8px 14px; }
.dark .chip{ color:var(--gold-bright); border-color:rgba(217,184,118,0.4); }

/* bar chart (content library) */
.bar-chart{ margin:22px 0 8px; }
.bar-row{ display:flex; align-items:center; gap:10px; margin-bottom:12px; }
.bar-label{ font-family:'Archivo'; font-weight:600; font-size:11px; letter-spacing:0.04em; color:var(--gray); width:56px; flex-shrink:0; }
.bar-track{ flex:1; background:var(--cream); border-radius:3px; height:16px; overflow:hidden; }
.bar-fill{ background:var(--navy); height:100%; border-radius:3px 0 0 3px; }
.bar-value{ font-family:'Playfair'; font-weight:700; font-size:14px; color:var(--navy); width:24px; text-align:right; }
.bar-caption{ font-family:'Archivo'; font-weight:600; font-size:10.5px; letter-spacing:0.14em; color:var(--gold); margin-top:4px; }

/* equation */
.equation{ font-family:'Playfair'; font-weight:700; font-size:19px; color:var(--white); margin:22px 0; line-height:1.5; }

/* case studies */
.case-card{ border-top:1px solid var(--line); padding:18px 0; }
.case-card:first-child{ border-top:none; padding-top:6px; }
.case-name{ font-family:'Playfair'; font-weight:700; font-size:16px; color:var(--navy); }
.case-meta{ font-family:'Archivo'; font-weight:600; font-size:10.5px; color:var(--gray); margin:3px 0 6px; }
.case-campaign{ font-family:'Archivo'; font-weight:600; font-size:11px; letter-spacing:0.08em; text-transform:uppercase; color:var(--gold); margin-bottom:6px; }
.case-result{ font-size:14px; line-height:1.5; }

/* faq */
.faq{ border-top:1px solid var(--line); padding:16px 0; }
.faq:first-child{ border-top:none; padding-top:6px; }
.faq-q{ font-family:'Playfair'; font-weight:700; font-size:16px; color:var(--navy); margin-bottom:5px; }
.faq-a{ font-size:14.5px; line-height:1.55; }

/* investment spec cards */
.invest-card{ border:1px solid var(--line); border-radius:8px; padding:20px; margin-bottom:18px; }
.invest-name{ font-family:'Playfair'; font-weight:700; font-size:17px; color:var(--navy); margin-bottom:12px; }
.spec-row{ display:flex; justify-content:space-between; gap:12px; padding:8px 0; border-top:1px solid var(--line); }
.spec-row:first-of-type{ border-top:none; }
.spec-label{ font-family:'Archivo'; font-weight:600; font-size:10.5px; letter-spacing:0.08em; text-transform:uppercase; color:var(--gold); flex-shrink:0; width:110px; }
.spec-value{ font-size:13.5px; text-align:right; color:var(--ink); }

/* numbered next steps */
.numstep{ display:flex; gap:16px; padding:16px 0; border-top:1px solid var(--line); }
.numstep:first-child{ border-top:none; padding-top:4px; }
.numstep-n{ font-family:'Playfair'; font-weight:700; font-size:24px; color:var(--gold); width:36px; flex-shrink:0; }
.numstep-t{ font-family:'Playfair'; font-weight:700; font-size:16px; color:var(--navy); margin-bottom:3px; }
.numstep-d{ font-size:14px; color:var(--ink); line-height:1.5; }

/* closing */
.closing{ background:var(--navy); background-image:linear-gradient(200deg,#16274A 0%,#0E1930 100%); text-align:center; }
.closing .inner{ padding:64px 24px 56px; }
.closing h2{ font-size:26px; margin-bottom:16px; }
.cta-btn{ display:inline-block; margin-top:26px; padding:14px 30px; border:1.5px solid var(--gold); border-radius:30px; font-family:'Archivo'; font-weight:600; font-size:13px; letter-spacing:0.1em; color:var(--gold-bright); }
.closing-foot{ margin-top:34px; font-family:'Archivo'; font-weight:500; font-size:11.5px; letter-spacing:0.08em; color:rgba(251,248,241,0.75); }
.closing-mark{ margin-top:14px; font-family:'Archivo'; font-weight:500; font-size:9.5px; letter-spacing:0.12em; color:rgba(251,248,241,0.4); }

@media (min-width:601px){
  .inner{ max-width:600px; }
}
'''

# Embed fonts as base64 data URIs
FONT_FILES = {
    "PlayfairDisplay-Regular": "PlayfairDisplay-Regular.ttf",
    "PlayfairDisplay-SemiBold": "PlayfairDisplay-SemiBold.ttf",
    "PlayfairDisplay-Bold": "PlayfairDisplay-Bold.ttf",
    "PlayfairDisplay-Italic": "PlayfairDisplay-Italic.ttf",
    "Inter-Regular": "Inter-Regular.ttf",
    "Inter-Medium": "Inter-Medium.ttf",
    "Inter-SemiBold": "Inter-SemiBold.ttf",
    "Inter-Bold": "Inter-Bold.ttf",
    "Archivo-Medium": "Archivo-Medium.ttf",
    "Archivo-SemiBold": "Archivo-SemiBold.ttf",
    "Archivo-Bold": "Archivo-Bold.ttf",
}
for key, fname in FONT_FILES.items():
    with open(f"/home/claude/fonts/{fname}", "rb") as f:
        b64 = base64.b64encode(f.read()).decode("ascii")
    CSS = CSS.replace(f"FONT_{key}", f"data:font/ttf;base64,{b64}")

html = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1">
<title>The Church Formation System — Mobile Guide</title>
<style>{CSS}</style>
</head>
<body>
{"".join(SECTIONS)}
</body>
</html>'''

with open("/home/claude/build/mobile/master_mobile.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Sections:", len(SECTIONS), "| HTML size:", len(html), "chars")
