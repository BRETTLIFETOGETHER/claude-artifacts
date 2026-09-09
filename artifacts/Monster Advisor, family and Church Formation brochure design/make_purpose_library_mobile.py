import sys
sys.path.insert(0, "/home/claude/build/mobile")
from components import *

S = []
def add(h): S.append(h)

add(hero(
    "A NEW GENERATION OF CHURCHWIDE CAMPAIGNS &amp; CURRICULUM",
    "The Biblical Purpose Library&trade;",
    "Helping people know God, belong, grow, serve, live sent, and multiply their lives.",
    '<p class="hero-sub">Built from more than 25 years of churchwide campaign, curriculum, and small-group ministry experience &mdash; and 500+ church partnerships.</p>'
))

purposes = [("1","Know God"),("2","Belong Together"),("3","Become Like Jesus"),("4","Serve with Your Gifts"),("5","Live Sent"),("6","Multiply Your Life")]
purpose_html = "".join([f'<div class="purpose-cell"><div class="purpose-num">{n}</div><div class="purpose-name">{name}</div></div>' for n, name in purposes])
add(section(f'''
  {eyebrow("THE BIG IDEA")}
  <h2>The biblical purposes have helped shape a generation.</h2>
  <p>For decades, the biblical foundations of worship, fellowship, discipleship, ministry,
  and mission have helped thousands of churches clarify how people grow and live as
  followers of Jesus. Brett Eastman served on the original Purpose Driven ministry team
  and later authored and co-developed numerous Purpose Driven small-group resources
  published by Zondervan.</p>
  <p>Today, LifeTogether is building a new generation of customizable campaigns,
  curriculum, classes, devotionals, and discipleship experiences that help churches go
  deeper and wider in these biblical foundations.</p>
  {pull_quote('&ldquo;The biblical purposes are not merely church programs.&rdquo; They are a whole-life framework for becoming the people God created us to be.')}
  <div class="purpose-grid">{purpose_html}</div>
'''))

checks = [
    "Understand why they are here", "Develop a daily relationship with God",
    "Belong in authentic community", "Grow in spiritual and emotional maturity",
    "Discover and use their gifts", "Live on mission in everyday life",
    "Pass faith, wisdom, and leadership forward",
]
add(section(f'''
  {eyebrow("WHY NOW")}
  <h2 class="on-dark">Churches do not need more disconnected content.</h2>
  <p class="on-dark-p">They need an integrated discipleship system that helps people move
  from inspiration to transformation.</p>
  {check_list(checks)}
  <p class="on-dark-p">Most churches already have sermons, groups, classes, ministries,
  volunteer opportunities, and leadership pathways. The challenge is helping people see
  how everything fits together.</p>
  {takeaway("One biblical framework", "Every person. Every ministry. Every next step.")}
''', dark=True))

weeks = [
    ("WEEK 1", "Created to Know God", "Building life around worship, relationship, and the presence of God."),
    ("WEEK 2", "Designed to Belong", "Finding spiritual family, authentic community, and meaningful relationships."),
    ("WEEK 3", "Formed to Become Like Jesus", "Developing Christlike character, habits, wisdom, and maturity."),
    ("WEEK 4", "Gifted to Serve", "Discovering strengths, spiritual gifts, and meaningful contribution."),
    ("WEEK 5", "Sent to Make a Difference", "Living as Christ's representative at home, work, church, and in the community."),
    ("WEEK 6", "Called to Multiply", "Passing faith, wisdom, leadership, and influence to others."),
]
week_html = "".join([f'<div class="week-card"><div class="week-tag">{wk}</div><div class="week-title">{t}</div><div class="week-desc">{d}</div></div>' for wk,t,d in weeks])
add(section(f'''
  {eyebrow("FLAGSHIP CAMPAIGN")}
  <h2>A Life That Matters</h2>
  <p style="font-family:'Playfair'; font-style:italic; color:var(--gold); font-size:15px;">40 days to know God, belong, grow, serve, live sent, and multiply your life.</p>
  <div class="week-grid">{week_html}</div>
  <p class="fine-print">The clearest broad churchwide introduction to the complete Biblical Purpose Library.</p>
'''))

def collection_card(title, sub, bullets, best_for):
    bl = "".join([f'<li>{b}</li>' for b in bullets])
    return f'<div class="collection-card"><div class="collection-title">{title}</div><div class="collection-sub">{sub}</div><ul class="collection-list">{bl}</ul><div class="collection-best"><span class="label">Best for</span>{best_for}</div></div>'

add(section(f'''
  {eyebrow("CAMPAIGN COLLECTION")}
  <h2>Two proven paths into purpose</h2>
  {collection_card("Made for More", "40 days to discover the life God designed you to live",
      ["More Than Existing","Made for His Presence","Made for His Family","Made to Become","Made to Contribute","Made to Multiply"],
      "New Year, churchwide vision, calling, purpose, and spiritual renewal.")}
  {collection_card("Your Life on Purpose", "30 days to align every part of your life with what matters most",
      ["Your Center","Your People","Your Formation","Your Contribution","Your Mission","Your Legacy"],
      "Adults, young professionals, workplace groups, ABFs, and personal journeys.")}
'''))

add(section(f'''
  {eyebrow("CAMPAIGN COLLECTION &middot; CONTINUED")}
  <h2>Whole-life formation for every season</h2>
  {collection_card("Designed to Flourish", "40 days to grow spiritually, relationally, personally, and purposefully",
      ["Flourishing with God","Flourishing Together","Flourishing from Within","Flourishing through Contribution","Flourishing for Others","Flourishing across Generations"],
      "Faith-friendly audiences, families, workplaces, advisors, and community groups.")}
  {collection_card("The Whole-Life Disciple", "40 days to follow Jesus in every role, relationship, and responsibility",
      ["A Life of Worship","A Life Together","A Life Being Formed","A Life of Service","A Life on Mission","A Life That Reproduces"],
      "Mature believers, ministry leaders, Church Seminary, and volunteer development.")}
  <p class="fine-print">Designed to Flourish draws on LifeTogether&rsquo;s existing Flourish campaign content &mdash; already written, tested, and proven across the broader campaign library.</p>
'''))

def mini_card(title, sub, bullets):
    return f'<div class="mini-card"><div class="mini-title">{title}</div><div class="mini-sub">{sub}</div><div class="mini-bullets">{" &middot; ".join(bullets)}</div></div>'
add(section(f'''
  {eyebrow("ADDITIONAL FLAGSHIP SERIES")}
  <h2 class="on-dark">More ways to begin</h2>
  {mini_card("Your Next Faithful Chapter", "30 days to clarify your calling, refocus your priorities, and multiply your impact.",
      ["Remember your story","Recognize your design","Renew your relationship with God","Refocus your season","Respond to your assignment","Reproduce your wisdom"])}
  {mini_card("Living What Matters Most", "Six biblical priorities that shape an extraordinary life.",
      ["Love God first","Love people well","Grow every day","Serve with joy","Live sent","Leave a legacy"])}
  {mini_card("Rooted", "Building a faith that lasts through every season of life.",
      ["Rooted in Christ","Scripture","Community","Character","Mission","The future"])}
  {mini_card("Living Fully Alive", "Discovering the life Jesus came to give.",
      ["Alive in Christ","Together","In truth","Through service","For others","With eternal purpose"])}
''', dark=True))

experience_items = [
    ("Weekend Teaching", "Six sermon outlines, pastor preparation notes, message illustrations, slides and graphics, response moments, and worship recommendations."),
    ("Small Groups", "Four- or six-session curriculum, Master Teaching videos, leader guide, participant workbook, discussion questions, and group action steps."),
    ("Daily Journey", "30- or 40-day devotional, journaling, prayer prompts, personal application, and QR-linked audio or video."),
    ("Adult Bible Fellowship", "8&ndash;12 week class edition, expanded lecture notes, biblical and historical context, maps, charts, timelines, teacher resources, and student workbook."),
    ("Families and Generations", "Couples, family discussion, student, elementary, preschool, and intergenerational editions."),
]
exp_html = "".join([f'<div class="exp-row"><div class="exp-name">{n}</div><div class="exp-desc">{d}</div></div>' for n,d in experience_items])
add(section(f'''
  {eyebrow("COMPLETE EXPERIENCE")}
  <h2>More than a sermon series</h2>
  {exp_html}
'''))

audiences = ["Churchwide Campaigns","Small Groups","Adult Bible Fellowship","Sunday School","Church Seminary","Men","Women","Singles","Couples","Parents","Young Adults","Students","Children","Business Leaders","Christian Advisors","Legacy Families","Volunteer Leaders","Ministry Teams","Workplace Groups","Community Outreach"]
aud_html = "".join([f'<div class="aud-cell">{a}</div>' for a in audiences])
add(section(f'''
  {eyebrow("ONE FOUNDATION, MANY MINISTRIES")}
  <h2>Every campaign can be customized for</h2>
  <div class="aud-grid">{aud_html}</div>
  <p>The biblical foundation remains consistent. The illustrations, applications,
  language, depth, format, and ministry outcomes adapt to the audience.</p>
'''))

adapt_factors = ["Pastor teaching","Church theology","Mission and vision","Ministry philosophy","Church history","Local stories","Congregational needs","Geographic context","Age and life stage","Spiritual maturity","Preferred Bible translation","Sermon calendar","Ministry pathways","Branding and design"]
adapt_html = "".join([f'<div class="adapt-cell">{a}</div>' for a in adapt_factors])
add(section(f'''
  {eyebrow("THE LIFETOGETHER DIFFERENCE")}
  <h2>One biblical foundation. Your church&rsquo;s voice.</h2>
  <div class="adapt-grid">{adapt_html}</div>
  {takeaway("The process", "Find it. Build it. Brand it. Publish it. Launch it. Multiply it.")}
  {stack_steps([
      ("FIND IT", "Discover the best-fit resource."),
      ("BUILD IT", "Customize content and components."),
      ("BRAND IT", "Apply the church's identity and voice."),
      ("PUBLISH IT", "Create digital, print, video, and mobile resources."),
      ("LAUNCH IT", "Deploy the experience across the whole church."),
      ("MULTIPLY IT", "Develop leaders, groups, ministries, and disciples."),
  ])}
'''))

begin_levels = [
    ("READY-TO-LAUNCH EDITION", "Choose an existing campaign and begin quickly &mdash; proven content, editable branding, digital resources, sermon and group tools, daily journey."),
    ("PASTOR-CONNECTED EDITION", "Integrate the pastor's voice and current teaching &mdash; pastor welcome, sermon alignment, local stories, QR-linked videos, church mission and next steps."),
    ("FULLY CUSTOM EDITION", "Build an original campaign from your church's message &mdash; custom strategy, original devotional, custom curriculum, filmed Master Teaching, family and student editions, LifeTogether Studios."),
]
add(section(f'''
  {eyebrow("THREE WAYS TO BEGIN")}
  <h2 class="on-dark">Choose the right starting point</h2>
  {stack_steps(begin_levels)}
''', dark=True))

add(closing(
    "CALL TO ACTION",
    "Help your whole church live a life that matters.",
    "Bring the biblical purposes into weekend worship, daily devotion, small groups, adult classes, family life, serving, mission, leadership, and legacy. LifeTogether helps your church turn timeless biblical truth into a shared discipleship journey that reaches every person, strengthens every ministry, and multiplies impact for generations.",
    cta_text="Explore the Biblical Purpose Library",
    footer_mark="40 DAY CAMPAIGNS&trade; &middot; CHURCH SEMINARY&trade; &middot; LIFETOGETHER STUDIOS&trade;"
))

html = assemble("LifeTogether — Biblical Purpose Library", "".join(S))
with open("/home/claude/build/mobile/purpose_library_mobile.html", "w", encoding="utf-8") as f:
    f.write(html)
print("Sections:", len(S), "size:", len(html))
