import sys
sys.path.insert(0, "/home/claude/build/mobile")
from components import *

S = []
def add(h): S.append(h)

add(hero(
    "THE COMPLETE MINISTRY GUIDEBOOK",
    "The Church Formation System&trade;",
    "A complete guide to why this matters, what the system is, how it works, and what your church can expect."
))

add(section(f'''
  {eyebrow("WELCOME")}
  <h2>Everything you need to move from inspiration to understanding.</h2>
  <p>This guidebook answers five questions honestly: why this matters, what the system
  is, how it works, why it is different, and what results your church can expect.</p>
'''))

add(section(f'''
  {eyebrow("CHAPTER ONE &middot; THE FUTURE OF CHURCH FORMATION")}
  <h2>Formation is becoming the work of the whole church, all week long.</h2>
  <p>For a hundred years, the center of church life was the Sunday service. That is not
  wrong &mdash; it is simply no longer sufficient. People are formed by what they hear once
  a week far less than they are formed by what they practice every day, in community,
  at home.</p>
  <p>The churches shaping the next generation will not simply preach well. They will
  build formation systems &mdash; ordinary rhythms that carry a message from the platform
  into daily life, without requiring a bigger staff or a bigger budget.</p>
  {takeaway("The shift underway", "From church as a place you attend, to church as a formation system you live inside.")}
'''))

reasons = [
    ("No next step", "The sermon ends and nothing carries it into the week."),
    ("No shared language", "Groups, families, and staff each go their own direction."),
    ("No format beyond the stage", "A great message exists in only one form, spoken once."),
    ("No time to build more", "Staff capacity ends at the manuscript, not the curriculum."),
]
add(section(f'''
  {eyebrow("CHAPTER TWO &middot; WHY MOST SERMONS END TOO SOON")}
  <h2>A sermon is a moment. Formation is a path.</h2>
  <p>Most churches don&rsquo;t lack good preaching. They lack a system to carry that
  preaching forward. Four gaps show up again and again:</p>
  {card_grid(reasons)}
  {pull_quote('Your greatest sermons deserve <span class="gold">more than one Sunday.</span>')}
'''))

add(section(f'''
  {eyebrow("CHAPTER THREE &middot; FROM MESSAGE TO MOVEMENT")}
  <h2 class="on-dark">What becomes possible with a system underneath it</h2>
  {stack_steps([
      ("MESSAGE", "One message, prepared once."),
      ("CURRICULUM", "Shaped into a resource."),
      ("COMMUNITY", "Practiced in real relationship."),
      ("MOVEMENT", "Carried into lasting change."),
  ])}
  {pull_quote('One message. <span class="gold">Many forms. One movement.</span>')}
''', dark=True))

add(section(f'''
  {eyebrow("CHAPTER FOUR &middot; THE FRAMEWORK &amp; ENVIRONMENTS")}
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

add(section(f'''
  {eyebrow("CHAPTER FIVE &middot; THE CHURCH FORMATION WHEEL")}
  <h2>Weekend + Groups + Daily + Family + Mission</h2>
  <p>The wheel turns every week &mdash; the same message moving through five environments,
  on repeat.</p>
  {stack_steps([
      ("WEEKEND", "The message is preached with clarity and conviction."),
      ("GROUPS", "The message is discussed in circles of real relationship."),
      ("DAILY", "The message becomes a daily rhythm of reflection."),
      ("FAMILY", "The message shapes conversation around the table."),
      ("MISSION", "The message moves outward into action."),
  ], cycle=True)}
'''))

add(section(f'''
  {eyebrow("CHAPTER SIX &middot; THE FIVE-STAGE PROCESS")}
  <h2 class="on-dark">Five stages turn a sermon into a system.</h2>
  <p class="on-dark-p">Every campaign your church builds moves through the same five
  disciplines. Learn them once, and your team can repeat them with every future message.</p>
  {chips(["DISCERN","DEVELOP","PRODUCE","PUBLISH","MOBILIZE"])}
''', dark=True))

stages = [
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
for name, sub, para, bullets in stages:
    bl = "".join([f"<li>{b}</li>" for b in bullets])
    stage_html += f'''
    <div class="stage-card">
      <div class="stage-name">{name}</div>
      <div class="stage-sub">{sub}</div>
      <p class="stage-desc">{para}</p>
      <ul class="stage-list">{bl}</ul>
    </div>'''
add(section(stage_html + pull_quote('Your team doesn&rsquo;t just receive curriculum. <span class="gold">They learn to build it, every time.</span>')))

add(section(f'''
  {eyebrow("CHAPTER SEVEN &middot; CAMPAIGN ARCHITECTURE")}
  <h2>The Campaign Lifecycle</h2>
  <p>No campaign is a one-time event. Every one seeds the next.</p>
  {stack_steps([
      ("PLAN", "Choose the theme and the season."),
      ("BUILD", "Produce every format from one message."),
      ("LAUNCH", "Mobilize the whole church together."),
      ("SUSTAIN", "Reinforce it through groups and daily practice."),
      ("MULTIPLY", "Let it shape the next campaign."),
  ], cycle=True)}
'''))

years = [("Year 1", 5), ("Year 2", 11), ("Year 3", 19), ("Year 4", 28), ("Year 5+", 40)]
max_v = max(v for _, v in years)
bars = "".join([f'''
  <div class="bar-row">
    <div class="bar-label">{yr}</div>
    <div class="bar-track"><div class="bar-fill" style="width:{v/max_v*100:.0f}%;"></div></div>
    <div class="bar-value">{v}</div>
  </div>''' for yr, v in years])
add(section(f'''
  {eyebrow("CHAPTER EIGHT &middot; THE PASTOR CONTENT LIBRARY")}
  <h2>A library that compounds every year you build it.</h2>
  <p>Every campaign you build stays in your library &mdash; ready to relaunch, adapt, or hand
  to a new group of leaders. Five years in, most churches are running almost entirely on
  content they already own.</p>
  <div class="bar-chart">{bars}</div>
  <div class="bar-caption">CUMULATIVE CAMPAIGNS IN YOUR LIBRARY</div>
'''))

add(section(f'''
  {eyebrow("CHAPTER NINE &middot; AI AS MINISTRY MULTIPLIER")}
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

journeys = [
    ("21-Day Challenge", "A focused sprint", "Best for a single habit, a launch moment, or a season with limited attention &mdash; like January or a new sermon series kickoff."),
    ("30-Day Journey", "A full month", "Best for a themed month tied to the calendar &mdash; stewardship in the fall, prayer in January, family in May."),
    ("40-Day Campaign", "A complete season", "Best for your most significant churchwide moments &mdash; the journeys people will remember years later."),
]
add(section(f'''
  {eyebrow("CHAPTER TEN &middot; 21, 30, AND 40-DAY JOURNEYS")}
  <h2>Choosing the right length for the moment.</h2>
  {"".join([offer_card(n,s,d) for n,s,d in journeys])}
  {takeaway("How to choose", "Match the length to the weight of the moment &mdash; a 40-day format on a light topic will feel padded, and a 21-day format on a heavy one will feel rushed.")}
'''))

add(section(f'''
  {eyebrow("CHAPTER ELEVEN &middot; THE MINISTRY PUBLISHING SYSTEM")}
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

add(section(f'''
  {eyebrow("CHAPTER TWELVE &middot; THE ANNUAL FORMATION CALENDAR")}
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

add(section(f'''
  {eyebrow("CHAPTER THIRTEEN &middot; CRAWL, WALK, RUN")}
  <h2 class="on-dark">Every church starts where it is, and grows from there.</h2>
  <p class="on-dark-p">No church is asked to arrive fully built. Most move through these
  five levels over eighteen to twenty-four months, at whatever pace fits their staff and
  calendar.</p>
  {stack_steps([
      ("USE OURS", "Launch proven Lifetogether campaigns as they are."),
      ("CUSTOMIZE OURS", "Adapt content and language to your church's voice."),
      ("BUILD YOURS", "Create original campaigns from your pastor's own messages."),
      ("PUBLISH YOURS", "Package your campaigns for other churches to license."),
      ("MULTIPLY YOURS", "Train other pastors to build within your formation system."),
  ])}
''', dark=True))

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
  {eyebrow("CHAPTER FOURTEEN &middot; CHURCH CASE STUDIES")}
  <h2>What this looks like in real churches</h2>
  <p class="fine-print">Case studies below are shown in placeholder format, ready to be replaced with your church&rsquo;s own story and results.</p>
  {case_html}
'''))

faqs = [
    ("Do we have to give up our own preaching style?", "No. The system is built around your pastor's own messages &mdash; it organizes and extends your voice, it never replaces it."),
    ("Will this create more work for our staff?", "Most of the production work is handled for you. Your team's role is review and mobilization, not writing from scratch."),
    ("What if our church is small?", "The Crawl, Walk, Run model exists for this reason. Most small churches begin at Level One with a licensed campaign."),
    ("How much does this cost?", "Investment depends on the level of partnership you choose. A strategy conversation will give you a clear, specific answer."),
    ("How is AI used, and is it reviewed?", "AI helps produce first drafts of formats like devotionals and guides. Every piece is reviewed by pastors before your church ever sees it."),
]
add(section(f'''
  {eyebrow("CHAPTER FIFTEEN &middot; FREQUENTLY ASKED QUESTIONS")}
  <h2>Honest answers to common questions</h2>
  {"".join([faq_item(q,a) for q,a in faqs])}
'''))

leader_levels = [
    ("PARTICIPANT", "Experiences a campaign as a small group member."),
    ("GROUP LEADER", "Leads others through the discussion guide."),
    ("COACH", "Trains and supports several group leaders."),
    ("CAMPAIGN BUILDER", "Helps shape original campaigns for the church."),
]
add(section(f'''
  {eyebrow("CHAPTER SEVENTEEN &middot; THE CHURCH FORMATION PARTNERSHIP")}
  <h2 class="on-dark">A twelve-month coaching relationship, not a one-time purchase.</h2>
  <p class="on-dark-p">The Partnership pairs your team with ongoing coaching, planning,
  and content development as you build a full formation calendar &mdash; and as your own
  people grow into leaders inside the system.</p>
  {stack_steps(leader_levels)}
''', dark=True))

steps = [
    ("01", "Schedule a strategy conversation", "A complimentary conversation to talk through your church's specific season and needs."),
    ("02", "Choose your starting level", "Decide together whether to license, customize, or build an original campaign first."),
    ("03", "Build your first campaign", "Move through the five-stage process with our team alongside yours."),
    ("04", "Launch, and plan the next one", "Mobilize your church, then begin filling in your annual formation calendar."),
]
add(section(f'''
  {eyebrow("CHAPTER EIGHTEEN &middot; NEXT STEPS")}
  <h2>How to begin</h2>
  {numstep_list(steps)}
'''))

add(closing(
    "A CLOSING CHALLENGE",
    "Your life&rsquo;s work deserves to keep discipling people long after you first preach it.",
    "Every message you have already prepared, every year of study behind your pulpit, is capable of forming people for years beyond the Sunday it was first spoken. The system simply gives it somewhere to go.",
    footer_mark="THE CHURCH FORMATION SYSTEM&trade; &middot; FLAGSHIP GUIDEBOOK"
))

html = assemble("LifeTogether — Flagship Guidebook", "".join(S))
with open("/home/claude/build/mobile/flagship_mobile.html", "w", encoding="utf-8") as f:
    f.write(html)
print("Sections:", len(S), "size:", len(html))
