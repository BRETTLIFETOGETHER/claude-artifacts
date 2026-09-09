import sys
sys.path.insert(0, "/home/claude/build/mobile")
from components import *

S = []
def add(h): S.append(h)

add(hero(
    "EXECUTIVE OVERVIEW",
    "LifeTogether Church Formation System&trade;",
    "You bring the message. We&rsquo;ll help you build the movement.",
    '<p class="hero-sub">A practical framework for helping churches create meaningful spiritual growth through churchwide campaigns, small groups, and customized formation journeys.</p>'
))

challenge_items = ["A small-group study", "A daily devotional", "A family discussion", "A leadership resource", "A ministry tool", "A future campaign"]
add(section(f'''
  {eyebrow("THE CHALLENGE")}
  <h2>Great churches don&rsquo;t lack sermons. They lack systems.</h2>
  <p>Every week pastors invest hours studying Scripture, praying, preparing, and preaching.
  Yet by the following week, most of those messages have already been replaced by the
  next sermon.</p>
  <p><b>Imagine if every message became more than a weekend experience.</b> Imagine if
  every sermon became:</p>
  {card_grid([(x, "") for x in challenge_items])}
  {pull_quote('Your greatest sermons deserve <span class="gold">more than one Sunday.</span>')}
'''))

add(section(f'''
  {eyebrow("THE OPPORTUNITY")}
  <h2 class="on-dark">From Message to Movement</h2>
  <p class="on-dark-p">Most churches think in sermon series. Healthy churches think in
  discipleship pathways. Transformational churches think in movements. The Church
  Formation System helps pastors move from isolated messages to intentional spiritual
  journeys.</p>
  <p class="on-dark-p"><b>Instead of asking</b> &ldquo;What should I preach next?&rdquo; &mdash;
  <b>we begin by asking</b> &ldquo;What does God want to form in our people over the next 18
  to 24 months?&rdquo;</p>
  {pull_quote('Everything else <span class="gold">flows from that question.</span>')}
''', dark=True))

add(section(f'''
  {eyebrow("HOW IT WORKS")}
  <h2>Five simple steps</h2>
  {stack_steps([
      ("DISCERN", "Clarify what God is calling your church to become."),
      ("DEVELOP", "Transform sermons into curriculum, devotionals, leader guides, and discussion resources."),
      ("PRODUCE", "Create engaging videos and teaching experiences at a level your church can sustain."),
      ("PUBLISH", "Package everything into a complete campaign experience."),
      ("MOBILIZE", "Launch your church into one unified spiritual journey, and prepare for what comes next."),
  ])}
'''))

build_items = ["21-Day Challenges","30-Day Journeys","40-Day Campaigns","Small-Group Studies","Daily Devotionals","Leader Guides","Family Resources","Video Studies","Ministry Playbooks","Digital Courses","Churchwide Formation Experiences"]
add(section(f'''
  {eyebrow("WHAT WE HELP YOU BUILD")}
  <h2>Whether you begin with one sermon series or an entire ministry strategy, we can help you create:</h2>
  {chips(build_items)}
  {takeaway("Takeaway", "Each resource is designed to strengthen discipleship, not simply create content.")}
'''))

add(section(f'''
  {eyebrow("A PATHWAY THAT FITS YOUR CHURCH")}
  <h2>Start where you are</h2>
  {stack_steps([
      ("USE A PROVEN CAMPAIGN", "Launch quickly using a trusted framework."),
      ("CUSTOMIZE A CAMPAIGN", "Add your stories, your voice, and your church's unique next steps."),
      ("BUILD AN ORIGINAL CAMPAIGN", "Transform your own sermons into a complete discipleship journey."),
      ("BUILD A MINISTRY LIBRARY", "Organize years of teaching into a reusable content system."),
      ("MULTIPLY YOUR MINISTRY", "Publish, share, and extend your church's impact for years to come."),
  ])}
'''))

offers = [
    ("Church Formation Intensive", "A six-week planning experience", "A focused six-week planning experience that results in a complete campaign blueprint."),
    ("90-Day Campaign Accelerator", "From idea to launch-ready", "Hands-on coaching to move from idea to launch-ready."),
    ("Annual Church Formation Partnership", "An 18 to 24 month strategy", "Ongoing coaching, planning, content development, and strategic guidance as you build an intentional 18-to-24-month formation strategy."),
]
add(section(f'''
  {eyebrow("HOW WE CAN HELP")}
  <h2>Every church is different. That&rsquo;s why we offer several ways to work together.</h2>
  {"".join([offer_card(n,s,d) for n,s,d in offers])}
  {pull_quote('Wherever you are today, <span class="gold">we&rsquo;ll help you take the next step.</span>')}
'''))

add(closing(
    "YOUR MESSAGE MATTERS",
    "Your greatest sermons shouldn&rsquo;t end on Sunday.",
    "They can become curriculum. That curriculum can build community. That community can become a movement. And that movement can shape lives long after the message is preached.",
    footer_mark="LIFETOGETHER CHURCH FORMATION SYSTEM&trade;"
))

html = assemble("LifeTogether — Executive Overview", "".join(S))
with open("/home/claude/build/mobile/overview_mobile.html", "w", encoding="utf-8") as f:
    f.write(html)
print("Sections:", len(S), "size:", len(html))
