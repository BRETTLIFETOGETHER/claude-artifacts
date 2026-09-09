import sys
sys.path.insert(0, "/home/claude/build/mobile")
from components import *

S = []
def add(h): S.append(h)

add(hero(
    "A GUIDE FOR SENIOR PASTORS &amp; MINISTRY LEADERS",
    "The Church Formation System&trade;",
    "Helping pastors turn sermons into curriculum &mdash; curriculum into community &mdash; and community into movements."
))

chapters = [
    ("The Problem", "Why sermons alone don't form disciples"),
    ("The Opportunity", "What becomes possible when a message keeps working"),
    ("The Formation Framework", "Five environments, one continuous path"),
    ("The Formation Masterclass", "Five tracks that train your team to build"),
    ("The Crawl, Walk, Run Model", "How churches grow into the system at their own pace"),
    ("What We Help You Build", "Every format a message can become"),
    ("Three Ways We Help", "Choose the level of partnership that fits your church"),
    ("Your Message Matters", "The legacy a system makes possible"),
]
toc_html = "".join([f'<div class="case-card"><div class="case-name">{t}</div><p class="case-result">{d}</p></div>' for t, d in chapters])
add(section(f'''
  {eyebrow("WELCOME")}
  <h2>Every message deserves a longer life than one Sunday.</h2>
  <p>Most churches pour weeks into a single message and then let it end when the service
  does. This guide lays out a different way &mdash; a system that carries what God says on
  Sunday into groups, homes, and daily life, all week long, all year long. It is not a
  curriculum. It is not an app. It is the formation system underneath both.</p>
  {toc_html}
'''))

add(section(f'''
  {eyebrow("CHAPTER ONE &middot; THE PROBLEM")}
  <h2>Churches don&rsquo;t lack sermons. They lack systems.</h2>
  <p>Most sermons are preached once, and then forgotten. The study is done. The
  illustration lands. The room responds. And by Tuesday, very little of it remains.</p>
  <p>Most churches build disconnected sermon series, disconnected ministries,
  disconnected groups, and disconnected discipleship &mdash; each one working hard, none of
  them working together.</p>
  {takeaway("The shift", "There is a better way &mdash; one message, carried through a system, instead of five ministries pulling in five directions.")}
'''))

add(section(f'''
  {eyebrow("THE PROBLEM &middot; CONTINUED")}
  <h2 class="on-dark">From scattered effort to one connected system.</h2>
  <p class="on-dark-p">Disconnected efforts pull in five directions at once: the weekend
  message, small groups, daily habits, family life, and mission &mdash; each working hard
  alone. A system threads all five into one connected path.</p>
  {stack_steps([
      ("WEEKEND", "The message is preached to the whole church."),
      ("GROUPS", "The same message is discussed in real relationship."),
      ("DAILY", "The message becomes a daily rhythm."),
      ("FAMILY", "The message shapes the home."),
      ("MISSION", "The message moves outward into action."),
  ])}
  {takeaway("Takeaway", "A system doesn&rsquo;t replace the sermon &mdash; it gives the sermon somewhere to go on Monday.")}
''', dark=True))

opp_items = ["Small Group Curriculum", "Daily Devotionals", "Family Conversations", "Leadership Development", "Ministry Training", "Podcasts &amp; Video", "Published Books", "Future Campaigns"]
add(section(f'''
  {eyebrow("CHAPTER TWO &middot; THE OPPORTUNITY")}
  <h2>Imagine every sermon becoming a library.</h2>
  <p>One message, prepared once, can quietly become the source material for an entire
  season of discipleship &mdash; without adding a single hour to a pastor&rsquo;s week.</p>
  {pull_quote('One message. <span class="gold">Many expressions. A single source of truth for the whole church.</span>')}
  {chips(opp_items)}
'''))

add(section(f'''
  {eyebrow("CHAPTER THREE &middot; THE FRAMEWORK")}
  <h2>Five environments. One formation path.</h2>
  <p>People are formed in more than one place. The Church Formation Framework names the
  five environments where a single message keeps doing its work &mdash; long after the
  sermon ends.</p>
  {stack_steps([
      ("WEEKEND", "The message is preached with clarity and conviction."),
      ("GROUPS", "The message is discussed in circles of real relationship."),
      ("DAILY", "The message becomes a daily rhythm of reflection."),
      ("FAMILY", "The message shapes conversation around the table."),
      ("MISSION", "The message moves outward into action."),
  ], cycle=True)}
  {takeaway("Takeaway", "The wheel turns every week &mdash; the message never stops moving through the life of the church.")}
'''))

add(section(f'''
  {eyebrow("CHAPTER FOUR &middot; THE FORMATION MASTERCLASS")}
  <h2 class="on-dark">Five tracks. One trained team.</h2>
  <p class="on-dark-p">The Masterclass is how a church staff learns to build inside the
  system &mdash; not just use it. Each track hands your team a discipline they can return to
  with every future message.</p>
  {chips(["DISCERN","DEVELOP","PRODUCE","PUBLISH","MOBILIZE"])}
''', dark=True))

tracks = [
    ("DISCERN", "Hearing the message clearly", "Before anything is built, a team learns to identify the single true center of a message &mdash; the one idea everything else will serve.",
     ["Name the one idea worth building around", "Separate the message from the moment", "Identify the Scripture that carries it", "Spot where it touches real daily life"]),
    ("DEVELOP", "Shaping it into a path", "A message becomes a multi-week arc with its own structure, pacing, and emotional and spiritual logic &mdash; not just a topic.",
     ["Map the week-by-week arc", "Set the pace between conviction and rest", "Build in the turn toward application", "Design the invitation at the end"]),
    ("PRODUCE", "Building every format", "The arc becomes curriculum, devotionals, and training &mdash; each shaped for how it will actually be used.",
     ["Write small group discussion guides", "Draft daily devotional content", "Build a leader training kit", "Prepare family conversation prompts"]),
    ("PUBLISH", "Packaging it with excellence", "The finished campaign is designed, proofed, and formatted so it feels like a resource, not a handout.",
     ["Design a cover and visual identity", "Typeset every printed and digital piece", "Proof theology, tone, and Scripture", "Prepare it for licensing or release"]),
    ("MOBILIZE", "Getting it into hands", "A campaign only forms people if it launches well &mdash; so the track ends with a real activation plan, not just a finished file.",
     ["Build the launch and promotion plan", "Train leaders to carry the content well", "Prepare the pulpit announcement path", "Plan the on-ramp to what comes next"]),
]
stage_html = ""
for name, sub, para, bullets in tracks:
    bl = "".join([f"<li>{b}</li>" for b in bullets])
    stage_html += f'''
    <div class="stage-card">
      <div class="stage-name">{name}</div>
      <div class="stage-sub">{sub}</div>
      <p class="stage-desc">{para}</p>
      <ul class="stage-list">{bl}</ul>
    </div>'''
add(section(stage_html + pull_quote('Your team doesn&rsquo;t just receive curriculum. <span class="gold">They learn to build it.</span>')))

add(section(f'''
  {eyebrow("CHAPTER FIVE &middot; THE CRAWL, WALK, RUN MODEL")}
  <h2>Every church starts where it is, and grows from there.</h2>
  <p>No church is asked to arrive fully built. The model has five levels, and most churches
  move through them over time &mdash; at whatever pace fits their staff, calendar, and
  capacity.</p>
  {stack_steps([
      ("USE OURS", "Launch proven Lifetogether campaigns as they are."),
      ("CUSTOMIZE OURS", "Adapt content and language to your church's voice."),
      ("BUILD YOURS", "Create original campaigns from your pastor's own messages."),
      ("PUBLISH YOURS", "Package your campaigns for other churches to license."),
      ("MULTIPLY YOURS", "Train other pastors to build within your formation system."),
  ])}
'''))

add(section(f'''
  {eyebrow("CRAWL, WALK, RUN &middot; CONTINUED")}
  <h2 class="on-dark">A typical 18 to 24 month formation roadmap</h2>
  {stack_steps([
      ("MO. 1&ndash;3", "Launch your first campaign with our library."),
      ("MO. 4&ndash;9", "Customize campaigns to your church's voice."),
      ("MO. 10&ndash;15", "Build original campaigns from your own messages."),
      ("MO. 16&ndash;20", "Publish your campaigns for other churches."),
      ("MO. 21&ndash;24", "Train other pastors inside your formation system."),
  ])}
  {takeaway("Practical takeaway", "Most churches begin at Level One with a licensed campaign, and don&rsquo;t build original content until their team has run the system at least once.")}
''', dark=True))

build_items = ["21-Day Challenges", "30-Day Journeys", "40-Day Campaigns", "Small Group Studies", "Sermon Series", "Leader Training", "Devotionals", "Family Resources", "Books", "Video Studies", "Digital Experiences", "Membership Courses", "Ministry Systems"]
add(section(f'''
  {eyebrow("CHAPTER SIX &middot; WHAT WE HELP YOU BUILD")}
  <h2>Every format a message can become.</h2>
  <p>Everything here is built from one thing: the pastor&rsquo;s own message.</p>
  {chips(build_items)}
'''))

add(section(f'''
  {eyebrow("WHAT WE HELP YOU BUILD &middot; CONTINUED")}
  <h2 class="on-dark">Message &rarr; Movement</h2>
  {stack_steps([
      ("MESSAGE", "One message, studied and preached with care."),
      ("CURRICULUM", "Shaped into formats groups and families can use."),
      ("COMMUNITY", "Lived out together, in real relationship."),
      ("MOVEMENT", "Carried into lasting, visible change."),
  ])}
  {pull_quote('Everything built from the pastor&rsquo;s own message. <span class="gold">Nothing built from scratch, twice.</span>')}
''', dark=True))

offers = [
    ("Campaign Builder Intensive", "A six-week planning process", "For a team ready to shape their first original campaign from a pastor&rsquo;s existing message."),
    ("90-Day Accelerator", "From idea to launch", "For a church ready to move quickly &mdash; from a first conversation to a fully launched campaign in one season."),
    ("Church Formation Partnership", "A twelve-month coaching relationship", "For a church building toward Level Four or Five &mdash; publishing and multiplying its own formation system."),
]
add(section(f'''
  {eyebrow("CHAPTER SEVEN &middot; THREE WAYS WE HELP")}
  <h2>Choose the level of partnership that fits your church.</h2>
  {"".join([offer_card(n,s,d) for n,s,d in offers])}
'''))

invest_html = (
    spec_card("Campaign Builder Intensive", [("Length","Six weeks"),("Best for","A first original campaign"),("You leave with","One completed campaign outline")])
    + spec_card("90-Day Accelerator", [("Length","~90 days"),("Best for","A fast, full launch"),("You leave with","One fully launched campaign")])
    + spec_card("Church Formation Partnership", [("Length","Twelve months"),("Best for","Building toward Level Four or Five"),("You leave with","A trained team and a repeatable system")])
)
add(section(f'''
  {eyebrow("THREE WAYS WE HELP &middot; CONTINUED")}
  <h2>At a glance</h2>
  {invest_html}
'''))

add(closing(
    "CHAPTER EIGHT &middot; YOUR MESSAGE MATTERS",
    "Your greatest sermons deserve more than one Sunday.",
    "They deserve to become a pathway that forms disciples, strengthens families, equips leaders, and leaves a legacy that outlives your ministry. You don&rsquo;t have to build it alone &mdash; and you don&rsquo;t have to build it all at once.",
    footer_mark="THE CHURCH FORMATION SYSTEM&trade;"
))

html = assemble("LifeTogether — The Church Formation System", "".join(S))
with open("/home/claude/build/mobile/formation_system_mobile.html", "w", encoding="utf-8") as f:
    f.write(html)
print("Sections:", len(S), "size:", len(html))
