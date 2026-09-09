import sys
sys.path.insert(0, "/home/claude/build/mobile")
from components import *

S = []
def add(h): S.append(h)

add(hero(
    "A CONSULTING GUIDE FOR SENIOR PASTORS",
    "Campaign Builder Intensive",
    "A collaborative ministry-building process that turns your sermons into a complete churchwide discipleship experience."
))

stuck_reasons = [
    ("Too many good ideas", "A dozen directions worth pursuing, and no clear place to start."),
    ("No bandwidth to build", "Weekly ministry already fills every hour your team has."),
    ("Uncertainty about the path", "Turning a sermon into a full experience feels like guesswork."),
    ("Past momentum that faded", "An earlier attempt lost steam somewhere around week two."),
]
add(section(f'''
  {eyebrow("WHY CHURCHES GET STUCK")}
  <h2>You don&rsquo;t need another idea. You need a process.</h2>
  <p>Almost every pastor we talk with already has more than enough vision and content to
  build a full campaign. What&rsquo;s missing isn&rsquo;t inspiration &mdash; it&rsquo;s a clear, guided
  process to get from a sermon idea to a finished, launch-ready experience.</p>
  {card_grid(stuck_reasons)}
  {pull_quote('You already have the message. <span class="gold">You just need the process to build with it.</span>')}
'''))

audiences = ["Vision campaigns", "Spiritual growth campaigns", "Stewardship campaigns", "Family campaigns", "Prayer campaigns", "Custom sermon-based journeys"]
add(section(f'''
  {eyebrow("WHAT WE BUILD TOGETHER")}
  <h2 class="on-dark">Not curriculum writing. Not coaching alone.</h2>
  <p class="on-dark-p">This is a collaborative ministry-building process that helps pastors
  transform their sermons into a complete churchwide discipleship experience &mdash; built
  with your team, not delivered to them.</p>
  {chips(audiences)}
''', dark=True))

week_chips = ["WEEK 1 DISCOVER","WEEK 2 DISCERN","WEEK 3 DESIGN","WEEK 4 DEVELOP","WEEK 5 PRODUCE","WEEK 6 LAUNCH"]
add(section(f'''
  {eyebrow("THE SIX-WEEK INTENSIVE")}
  <h2>Six weeks. One complete campaign blueprint.</h2>
  <p>Each week builds on the last, moving your team from a raw idea to a finished,
  launch-ready plan &mdash; with our team working alongside yours the entire way.</p>
  {chips(week_chips)}
'''))

weeks_detail = [
    ("WEEK 1 &middot; DISCOVER", "We start by listening &mdash; to your church&rsquo;s season, your congregation&rsquo;s needs, and the message God has already given you to preach.",
     ["Review your church's current season", "Clarify your campaign's purpose", "Identify your congregation's real needs", "Set the outcomes you're building toward"]),
    ("WEEK 2 &middot; DISCERN", "Together we identify the single true center of your message &mdash; the one idea strong enough to carry a full campaign.",
     ["Name the one idea worth building around", "Choose the Scripture that carries it", "Separate the message from the moment", "Confirm it fits your church's voice"]),
    ("WEEK 3 &middot; DESIGN", "Your message becomes a multi-week arc, with its own pacing, structure, and turn toward application.",
     ["Map the full campaign arc, week by week", "Design the emotional and spiritual pacing", "Plan the invitation and response points", "Sketch the formats each week will need"]),
    ("WEEK 4 &middot; DEVELOP", "The arc becomes real content &mdash; curriculum, devotionals, and training, shaped for how your church will actually use them.",
     ["Draft small group discussion guides", "Outline daily devotional content", "Build a leader training framework", "Prepare family conversation prompts"]),
    ("WEEK 5 &middot; PRODUCE", "We plan the video, design, and production elements at a level your church can sustain long after the intensive ends.",
     ["Plan your video and teaching content", "Set the visual identity and design direction", "Scope what your team can produce in-house", "Identify where outside help is worth it"]),
    ("WEEK 6 &middot; LAUNCH BLUEPRINT", "Everything comes together into one finished, launch-ready plan &mdash; including your very next step, on Day 41.",
     ["Finalize the promotion and launch calendar", "Prepare the pulpit announcement path", "Train leaders to carry the campaign well", "Set your Day 41 strategy"]),
]
stage_html = ""
for name, para, bullets in weeks_detail:
    bl = "".join([f"<li>{b}</li>" for b in bullets])
    stage_html += f'''
    <div class="stage-card">
      <div class="stage-name">{name}</div>
      <p class="stage-desc">{para}</p>
      <ul class="stage-list">{bl}</ul>
    </div>'''
add(section(stage_html + pull_quote('Six weeks from now, you won&rsquo;t just have an idea. <span class="gold">You&rsquo;ll have a launch-ready campaign.</span>')))

deliverables = ["Campaign strategy", "Sermon roadmap", "Curriculum outline", "Video plan", "Leader resources", "Promotion plan", "Launch calendar", "Day 41 strategy"]
add(section(f'''
  {eyebrow("DELIVERABLES")}
  <h2>What you walk away with</h2>
  <p>Eight concrete deliverables, ready to hand to your staff and launch team.</p>
  {chips(deliverables)}
  {takeaway("Why Day 41 matters", "Most campaigns end on Day 40 with no plan for what comes next. Yours won&rsquo;t &mdash; the Day 41 strategy is built in from the start.")}
'''))

add(section(f'''
  {eyebrow("OPTIONAL &middot; THE 90-DAY ACCELERATOR")}
  <h2>From blueprint to a fully launched campaign</h2>
  <p>The Intensive gives your church a complete plan. For churches who want hands-on
  help carrying that plan all the way to launch, the 90-Day Accelerator adds ongoing
  production support and coaching through the entire launch season.</p>
  {takeaway("Best for", "Churches ready to move quickly &mdash; from a finished blueprint to a fully launched campaign in one season.")}
'''))

add(section(f'''
  {eyebrow("FOR THE LONGER JOURNEY")}
  <h2 class="on-dark">The Annual Formation Partnership</h2>
  <p class="on-dark-p">A twelve-month relationship, for churches building a whole formation
  calendar. Some churches need one campaign built well. Others are ready to build an
  entire year of formation, and to develop their own team&rsquo;s ability to build campaigns
  without outside help.</p>
''', dark=True))

invest_html = (
    spec_card("Campaign Builder Intensive", [("Length","Six weeks"),("Best for","Your first campaign blueprint"),("Format","Guided weekly planning"),("Investment","A one-time program fee")])
    + spec_card("90-Day Accelerator", [("Length","One season (~90 days)"),("Best for","Carrying it to a full launch"),("Format","Hands-on production &amp; launch support"),("Investment","A one-time program fee")])
    + spec_card("Annual Formation Partnership", [("Length","Twelve months"),("Best for","A whole year, and a trained team"),("Format","Ongoing coaching &amp; team training"),("Investment","An ongoing annual fee")])
)
add(section(f'''
  {eyebrow("INVESTMENT OVERVIEW")}
  <h2>Three ways to work together</h2>
  {invest_html}
  <p class="fine-print">Specific investment figures vary by church size and scope, and are
  confirmed during your strategy conversation.</p>
'''))

faqs = [
    ("What if we fall behind during one of the six weeks?", "The process is flexible enough to adjust &mdash; we build around your church's calendar, not the other way around."),
    ("Do we need video production experience?", "No. We help you scope a video plan that matches your church's actual capacity, from simple to fully produced."),
    ("What size church is this built for?", "The Intensive has worked for churches from a few hundred to several thousand &mdash; the process scales to your team."),
    ("Can our staff keep building after the Intensive ends?", "Yes. That is the goal. You leave with both a finished blueprint and a repeatable process your team can use again."),
    ("What happens after the six weeks?", "You launch with a complete plan in hand. Many churches choose the 90-Day Accelerator for launch support, or the Annual Partnership to keep building."),
]
add(section(f'''
  {eyebrow("FREQUENTLY ASKED QUESTIONS")}
  <h2>Honest answers before you decide</h2>
  {"".join([faq_item(q,a) for q,a in faqs])}
'''))

stories = [
    ("Church Name Placeholder", "Vision Campaign", "Went from a single sermon idea to a fully launched, churchwide campaign in six weeks."),
    ("Church Name Placeholder", "Stewardship Campaign", "Built a complete campaign blueprint their staff has now reused for two additional seasons."),
    ("Church Name Placeholder", "Family Campaign", "Launched with the highest first-time small group sign-up rate in the church's history."),
]
case_html = "".join([f'''
  <div class="case-card">
    <div class="case-name">{n}</div>
    <div class="case-campaign">{t}</div>
    <p class="case-result">{r}</p>
  </div>''' for n, t, r in stories])
add(section(f'''
  {eyebrow("SUCCESS STORIES")}
  <h2>What churches are building</h2>
  <p class="fine-print">Stories below are shown in placeholder format, ready to be replaced with your church&rsquo;s own results.</p>
  {case_html}
'''))

steps = [
    ("01", "Schedule a strategy conversation", "A complimentary conversation about your church's next campaign."),
    ("02", "Confirm your six-week schedule", "We'll find six weeks that work with your church's calendar."),
    ("03", "Begin Week One: Discover", "Your Campaign Builder Intensive begins."),
    ("04", "Walk away with a launch-ready blueprint", "Then choose your next step &mdash; launch on your own, or bring us alongside."),
]
add(section(f'''
  {eyebrow("NEXT STEPS")}
  <h2>How to begin</h2>
  {numstep_list(steps)}
'''))

add(closing(
    "CALL TO ACTION",
    "Your greatest sermons deserve more than one Sunday.",
    "You don&rsquo;t need to start from scratch. You already possess years of God-given teaching. The Campaign Builder Intensive simply helps organize, expand, and multiply that message into a transformational journey that reaches people far beyond Sunday. They deserve to become a movement that shapes lives, strengthens families, equips leaders, and leaves a legacy that outlives your ministry.",
    footer_mark="CAMPAIGN BUILDER INTENSIVE&trade;"
))

html = assemble("LifeTogether — Campaign Builder Intensive", "".join(S))
with open("/home/claude/build/mobile/intensive_mobile.html", "w", encoding="utf-8") as f:
    f.write(html)
print("Sections:", len(S), "size:", len(html))
