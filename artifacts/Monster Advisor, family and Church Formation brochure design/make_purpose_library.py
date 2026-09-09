import sys
sys.path.insert(0, "/home/claude/build")
from diagrams import step_chain_vertical, vertical_levels, fixed

PAGES = []
def add(html): PAGES.append(html)

def photo(caption, extra_style=""):
    return f'''<div class="photo" style="{extra_style}">
        <div class="corner tl"></div><div class="corner br"></div>
        <div class="cap">{caption}</div>
    </div>'''

def folio(chapter, num):
    return f'''<div class="folio"><div class="thread">{chapter}</div><div>{num:02d}</div></div>'''

# =================================================================
# PAGE 1 — COVER
# =================================================================
add(f'''
<div class="page navy">
  <div class="photo" style="position:absolute; inset:0; border-radius:0;">
    <div class="cap" style="right:0.68in; bottom:0.5in; left:auto; text-align:right; font-size:6.8pt;">PHOTOGRAPHY — DIVERSE CONGREGATION, HANDS RAISED IN WORSHIP, WARM LIGHT</div>
  </div>
  <div style="position:absolute; inset:0; background:linear-gradient(190deg, rgba(16,30,56,0.4) 0%, rgba(16,30,56,0.88) 55%, rgba(16,30,56,0.98) 100%);"></div>
  <div class="frame" style="display:flex; flex-direction:column; justify-content:flex-end;">
    <div style="font-family:'Archivo'; font-weight:600; font-size:9pt; letter-spacing:0.22em; color:#D9B876; margin-bottom:2.2in;">A NEW GENERATION OF CHURCHWIDE CAMPAIGNS &amp; CURRICULUM</div>
    <h1 class="display" style="font-size:30pt; color:#FBF8F1;">The Biblical Purpose Library<span style="font-size:14pt; vertical-align:super;">™</span></h1>
    <div style="height:0.24in;"></div>
    <p style="font-family:'Playfair'; font-style:italic; font-weight:500; font-size:13.5pt; color:#D9B876; line-height:1.5;">
      Helping people know God, belong, grow, serve, live sent, and multiply their lives.
    </p>
    <div style="height:0.2in;"></div>
    <p class="lede" style="font-size:10pt; color:rgba(251,248,241,0.75);">
      Built from more than 25 years of churchwide campaign, curriculum, and small-group
      ministry experience &mdash; and 500+ church partnerships.
    </p>
    <div style="height:0.5in;"></div>
    <div style="display:flex; justify-content:space-between; align-items:flex-end; font-family:'Archivo'; font-weight:500; font-size:8pt; letter-spacing:0.12em; color:rgba(251,248,241,0.55);">
      <div>LIFETOGETHER CHURCH&trade; &nbsp;&middot;&nbsp; THE WHOLE-CHURCH DISCIPLESHIP PLATFORM</div>
      <div style="width:22px; height:2px; background:#B98D3E;"></div>
    </div>
  </div>
</div>
''')

# =================================================================
# PAGE 2 — THE BIG IDEA
# =================================================================
purposes = [
    ("1", "Know God"), ("2", "Belong Together"), ("3", "Become Like Jesus"),
    ("4", "Serve with Your Gifts"), ("5", "Live Sent"), ("6", "Multiply Your Life"),
]
purpose_grid = "".join([f'''
    <div class="purpose-cell">
      <div class="purpose-num">{n}</div>
      <div class="purpose-name">{name}</div>
    </div>''' for n, name in purposes])
add(f'''
<div class="page">
  <div class="frame">
    <div class="eyebrow">THE BIG IDEA</div>
    <div style="height:0.2in;"></div>
    <h1 class="display" style="font-size:21pt; color:var(--navy);">The biblical purposes have helped shape a generation.</h1>
    <div style="height:0.16in;"></div>
    <p class="lede">
      For decades, the biblical foundations of worship, fellowship, discipleship, ministry,
      and mission have helped thousands of churches clarify how people grow and live as
      followers of Jesus. Brett Eastman served on the original Purpose Driven ministry team
      and later authored and co-developed numerous Purpose Driven small-group resources
      published by Zondervan.
    </p>
    <div style="height:0.1in;"></div>
    <p class="lede">
      Today, LifeTogether is building a new generation of customizable campaigns,
      curriculum, classes, devotionals, and discipleship experiences that help churches go
      deeper and wider in these biblical foundations.
    </p>
    <div style="height:0.22in;"></div>
    <div class="pull-quote" style="font-size:13.5pt;"><span class="mark">&ldquo;</span>The biblical purposes are not merely church programs.<span class="mark">&rdquo;</span> They are a whole-life framework for becoming the people God created us to be.</div>
    <div style="height:0.28in;"></div>
    <div class="purpose-grid">{purpose_grid}</div>
  </div>
  {folio("The Big Idea", 2)}
</div>
''')

# =================================================================
# PAGE 3 — WHY NOW
# =================================================================
checks = [
    "Understand why they are here", "Develop a daily relationship with God",
    "Belong in authentic community", "Grow in spiritual and emotional maturity",
    "Discover and use their gifts", "Live on mission in everyday life",
    "Pass faith, wisdom, and leadership forward",
]
check_html = "".join([f'<div class="check-item"><span class="check-mark">&#10003;</span>{c}</div>' for c in checks])
add(f'''
<div class="page">
  <div class="frame">
    <div class="eyebrow">WHY NOW</div>
    <div style="height:0.2in;"></div>
    <h1 class="display" style="font-size:21pt; color:var(--navy);">Churches do not need more disconnected content.</h1>
    <div style="height:0.14in;"></div>
    <p class="lede">
      They need an integrated discipleship system that helps people move from inspiration
      to transformation.
    </p>
    <div style="height:0.2in;"></div>
    <div class="check-grid">{check_html}</div>
    <div style="height:0.24in;"></div>
    <p class="lede">
      Most churches already have sermons, groups, classes, ministries, volunteer
      opportunities, and leadership pathways. The challenge is helping people see how
      everything fits together. The LifeTogether Biblical Purpose Library provides a shared
      framework connecting the weekend, small groups, daily devotionals, Adult Bible
      Fellowship classes, families, leaders, students, children, worship, and ministry
      involvement.
    </p>
    <div style="height:0.2in;"></div>
    <div class="takeaway">
      <span class="label">One biblical framework</span>
      Every person. Every ministry. Every next step.
    </div>
  </div>
  {folio("Why Now", 3)}
</div>
''')

# =================================================================
# PAGE 4 — FLAGSHIP CAMPAIGN: A LIFE THAT MATTERS
# =================================================================
weeks = [
    ("WEEK 1", "Created to Know God", "Building life around worship, relationship, and the presence of God."),
    ("WEEK 2", "Designed to Belong", "Finding spiritual family, authentic community, and meaningful relationships."),
    ("WEEK 3", "Formed to Become Like Jesus", "Developing Christlike character, habits, wisdom, and maturity."),
    ("WEEK 4", "Gifted to Serve", "Discovering strengths, spiritual gifts, and meaningful contribution."),
    ("WEEK 5", "Sent to Make a Difference", "Living as Christ's representative at home, work, church, and in the community."),
    ("WEEK 6", "Called to Multiply", "Passing faith, wisdom, leadership, and influence to others."),
]
week_cards = "".join([f'''
    <div class="week-card">
      <div class="week-tag">{wk}</div>
      <div class="week-title">{t}</div>
      <div class="week-desc">{d}</div>
    </div>''' for wk, t, d in weeks])
add(f'''
<div class="page">
  <div class="frame">
    <div class="eyebrow">FLAGSHIP CAMPAIGN</div>
    <div style="height:0.16in;"></div>
    <h1 class="display" style="font-size:23pt; color:var(--navy);">A Life That Matters</h1>
    <div style="height:0.06in;"></div>
    <p style="font-family:'Playfair'; font-style:italic; font-weight:500; font-size:12.5pt; color:var(--gold); margin-bottom:0.18in;">
      40 days to know God, belong, grow, serve, live sent, and multiply your life.
    </p>
    <div class="week-grid">{week_cards}</div>
    <div style="height:0.18in;"></div>
    <p style="font-family:'Inter'; font-size:9.6pt; color:var(--gray); font-style:italic;">
      The clearest broad churchwide introduction to the complete Biblical Purpose Library.
    </p>
  </div>
  {folio("Flagship Campaign", 4)}
</div>
''')

# =================================================================
# PAGE 5 — CAMPAIGN COLLECTION: TWO PROVEN PATHS
# =================================================================
def collection_card(title, sub, bullets, best_for):
    bl = "".join([f'<li>{b}</li>' for b in bullets])
    return f'''
    <div class="collection-card">
      <div class="collection-title">{title}</div>
      <div class="collection-sub">{sub}</div>
      <ul class="collection-list">{bl}</ul>
      <div class="collection-best"><span class="label">Best for</span>{best_for}</div>
    </div>'''
add(f'''
<div class="page">
  <div class="frame">
    <div class="eyebrow">CAMPAIGN COLLECTION</div>
    <div style="height:0.18in;"></div>
    <h1 class="display" style="font-size:22pt; color:var(--navy);">Two proven paths into purpose</h1>
    <div style="height:0.22in;"></div>
    {collection_card("Made for More", "40 days to discover the life God designed you to live",
        ["More Than Existing", "Made for His Presence", "Made for His Family", "Made to Become", "Made to Contribute", "Made to Multiply"],
        "New Year, churchwide vision, calling, purpose, and spiritual renewal.")}
    <div style="height:0.2in;"></div>
    {collection_card("Your Life on Purpose", "30 days to align every part of your life with what matters most",
        ["Your Center", "Your People", "Your Formation", "Your Contribution", "Your Mission", "Your Legacy"],
        "Adults, young professionals, workplace groups, ABFs, and personal journeys.")}
  </div>
  {folio("Campaign Collection", 5)}
</div>
''')

# =================================================================
# PAGE 6 — CAMPAIGN COLLECTION: WHOLE-LIFE FORMATION
# =================================================================
add(f'''
<div class="page">
  <div class="frame">
    <div class="eyebrow">CAMPAIGN COLLECTION &mdash; CONTINUED</div>
    <div style="height:0.18in;"></div>
    <h1 class="display" style="font-size:22pt; color:var(--navy);">Whole-life formation for every season</h1>
    <div style="height:0.22in;"></div>
    {collection_card("Designed to Flourish", "40 days to grow spiritually, relationally, personally, and purposefully",
        ["Flourishing with God", "Flourishing Together", "Flourishing from Within", "Flourishing through Contribution", "Flourishing for Others", "Flourishing across Generations"],
        "Faith-friendly audiences, families, workplaces, advisors, and community groups.")}
    <div style="height:0.2in;"></div>
    {collection_card("The Whole-Life Disciple", "40 days to follow Jesus in every role, relationship, and responsibility",
        ["A Life of Worship", "A Life Together", "A Life Being Formed", "A Life of Service", "A Life on Mission", "A Life That Reproduces"],
        "Mature believers, ministry leaders, Church Seminary, and volunteer development.")}
    <div style="height:0.2in;"></div>
    <p style="font-family:'Inter'; font-size:9.4pt; color:var(--gray); font-style:italic;">
      Designed to Flourish draws on LifeTogether&rsquo;s existing Flourish campaign content &mdash;
      already written, tested, and proven across the broader campaign library.
    </p>
  </div>
  {folio("Campaign Collection", 6)}
</div>
''')

# =================================================================
# PAGE 7 — ADDITIONAL FLAGSHIP SERIES
# =================================================================
def mini_card(title, sub, bullets):
    return f'''
    <div class="mini-card">
      <div class="mini-title">{title}</div>
      <div class="mini-sub">{sub}</div>
      <div class="mini-bullets">{" &middot; ".join(bullets)}</div>
    </div>'''
add(f'''
<div class="page">
  <div class="frame">
    <div class="eyebrow">ADDITIONAL FLAGSHIP SERIES</div>
    <div style="height:0.18in;"></div>
    <h1 class="display" style="font-size:21pt; color:var(--navy);">More ways to begin</h1>
    <div style="height:0.2in;"></div>
    {mini_card("Your Next Faithful Chapter", "30 days to clarify your calling, refocus your priorities, and multiply your impact.",
        ["Remember your story", "Recognize your design", "Renew your relationship with God", "Refocus your season", "Respond to your assignment", "Reproduce your wisdom"])}
    {mini_card("Living What Matters Most", "Six biblical priorities that shape an extraordinary life.",
        ["Love God first", "Love people well", "Grow every day", "Serve with joy", "Live sent", "Leave a legacy"])}
    {mini_card("Rooted", "Building a faith that lasts through every season of life.",
        ["Rooted in Christ", "Scripture", "Community", "Character", "Mission", "The future"])}
    {mini_card("Living Fully Alive", "Discovering the life Jesus came to give.",
        ["Alive in Christ", "Together", "In truth", "Through service", "For others", "With eternal purpose"])}
  </div>
  {folio("Additional Flagship Series", 7)}
</div>
''')

# =================================================================
# PAGE 8 — COMPLETE EXPERIENCE
# =================================================================
experience_items = [
    ("Weekend Teaching", "Six sermon outlines, pastor preparation notes, message illustrations, slides and graphics, response moments, and worship recommendations."),
    ("Small Groups", "Four- or six-session curriculum, Master Teaching videos, leader guide, participant workbook, discussion questions, and group action steps."),
    ("Daily Journey", "30- or 40-day devotional, journaling, prayer prompts, personal application, and QR-linked audio or video."),
    ("Adult Bible Fellowship", "8&ndash;12 week class edition, expanded lecture notes, biblical and historical context, maps, charts, timelines, teacher resources, and student workbook."),
    ("Families and Generations", "Couples, family discussion, student, elementary, preschool, and intergenerational editions."),
]
exp_html = "".join([f'''
    <div class="exp-row">
      <div class="exp-name">{n}</div>
      <div class="exp-desc">{d}</div>
    </div>''' for n, d in experience_items])
add(f'''
<div class="page">
  <div class="frame">
    <div class="eyebrow">COMPLETE EXPERIENCE</div>
    <div style="height:0.18in;"></div>
    <h1 class="display" style="font-size:22pt; color:var(--navy);">More than a sermon series</h1>
    <div style="height:0.2in;"></div>
    {exp_html}
  </div>
  {folio("Complete Experience", 8)}
</div>
''')

# =================================================================
# PAGE 9 — ONE FOUNDATION, MANY MINISTRIES
# =================================================================
audiences = [
    "Churchwide Campaigns", "Small Groups", "Adult Bible Fellowship", "Sunday School",
    "Church Seminary", "Men", "Women", "Singles",
    "Couples", "Parents", "Young Adults", "Students",
    "Children", "Business Leaders", "Christian Advisors", "Legacy Families",
    "Volunteer Leaders", "Ministry Teams", "Workplace Groups", "Community Outreach",
]
aud_grid = "".join([f'<div class="aud-cell">{a}</div>' for a in audiences])
add(f'''
<div class="page">
  <div class="frame">
    <div class="eyebrow">ONE FOUNDATION, MANY MINISTRIES</div>
    <div style="height:0.16in;"></div>
    <h1 class="display" style="font-size:20pt; color:var(--navy);">Every campaign can be customized for</h1>
    <div style="height:0.18in;"></div>
    <div class="aud-grid">{aud_grid}</div>
    <div style="height:0.2in;"></div>
    <p class="lede" style="font-size:10.3pt;">
      The biblical foundation remains consistent. The illustrations, applications,
      language, depth, format, and ministry outcomes adapt to the audience.
    </p>
  </div>
  {folio("One Foundation, Many Ministries", 9)}
</div>
''')

# =================================================================
# PAGE 10 — THE LIFETOGETHER DIFFERENCE
# =================================================================
adapt_factors = [
    "Pastor teaching", "Church theology", "Mission and vision", "Ministry philosophy",
    "Church history", "Local stories", "Congregational needs", "Geographic context",
    "Age and life stage", "Spiritual maturity", "Preferred Bible translation", "Sermon calendar",
    "Ministry pathways", "Branding and design",
]
adapt_html = "".join([f'<div class="adapt-cell">{a}</div>' for a in adapt_factors])
add(f'''
<div class="page">
  <div class="frame">
    <div class="eyebrow">THE LIFETOGETHER DIFFERENCE</div>
    <div style="height:0.16in;"></div>
    <h1 class="display" style="font-size:20pt; color:var(--navy);">One biblical foundation. Your church&rsquo;s voice.</h1>
    <div style="height:0.16in;"></div>
    <div class="adapt-grid">{adapt_html}</div>
    <div style="height:0.2in;"></div>
    <div class="takeaway" style="margin-bottom:0.2in;">
      <span class="label">The process</span>
      Find it. Build it. Brand it. Publish it. Launch it. Multiply it.
    </div>
    <div style="text-align:center;">{fixed(step_chain_vertical([
        ("FIND IT", "Discover the best-fit resource."),
        ("BUILD IT", "Customize content and components."),
        ("BRAND IT", "Apply the church's identity and voice."),
        ("PUBLISH IT", "Create digital, print, video, and mobile resources."),
        ("LAUNCH IT", "Deploy the experience across the whole church."),
        ("MULTIPLY IT", "Develop leaders, groups, ministries, and disciples."),
    ]), 7.1, 5.3)}</div>
  </div>
  {folio("The LifeTogether Difference", 10)}
</div>
''')

# =================================================================
# PAGE 11 — THREE WAYS TO BEGIN
# =================================================================
begin_levels = [
    ("1", "Ready-to-Launch Edition", "Choose an existing campaign and begin quickly &mdash; proven content, editable branding, digital resources, sermon and group tools, daily journey."),
    ("2", "Pastor-Connected Edition", "Integrate the pastor's voice and current teaching &mdash; pastor welcome, sermon alignment, local stories, QR-linked videos, church mission and next steps."),
    ("3", "Fully Custom Edition", "Build an original campaign from your church's message &mdash; custom strategy, original devotional, custom curriculum, filmed Master Teaching, family and student editions, LifeTogether Studios."),
]
add(f'''
<div class="page">
  <div class="frame">
    <div class="eyebrow">THREE WAYS TO BEGIN</div>
    <div style="height:0.18in;"></div>
    <h1 class="display" style="font-size:21pt; color:var(--navy);">Choose the right starting point</h1>
    <div style="height:0.16in;"></div>
    <div style="text-align:center;">{fixed(vertical_levels(begin_levels), 7.1, 5.0)}</div>
  </div>
  {folio("Three Ways to Begin", 11)}
</div>
''')

# =================================================================
# PAGE 12 — CALL TO ACTION
# =================================================================
add(f'''
<div class="page navy">
  <div class="photo" style="position:absolute; inset:0; border-radius:0;">
    <div class="cap" style="right:0.68in; bottom:0.5in; left:auto; text-align:right; font-size:6.8pt;">PHOTOGRAPHY — MULTI-GENERATIONAL FAMILY, CHURCH LOBBY, SOFT FOCUS</div>
  </div>
  <div style="position:absolute; inset:0; background:linear-gradient(190deg, rgba(16,30,56,0.4) 0%, rgba(16,30,56,0.9) 55%, rgba(16,30,56,0.98) 100%);"></div>
  <div class="frame" style="display:flex; flex-direction:column; justify-content:flex-end;">
    <div class="eyebrow">CALL TO ACTION</div>
    <div style="height:0.2in;"></div>
    <h1 class="display" style="font-size:22pt; color:#FBF8F1;">Help your whole church live a life that matters.</h1>
    <div style="height:0.16in;"></div>
    <p class="lede">
      Bring the biblical purposes into weekend worship, daily devotion, small groups, adult
      classes, family life, serving, mission, leadership, and legacy.
    </p>
    <div style="height:0.2in;"></div>
    <div class="takeaway">
      <span class="label">Explore the Biblical Purpose Library</span>
      Select a campaign. Build your church edition. Join the Founding Church Cohort.
    </div>
    <div style="height:0.2in;"></div>
    <p class="lede" style="font-size:10.3pt;">
      LifeTogether helps your church turn timeless biblical truth into a shared discipleship
      journey that reaches every person, strengthens every ministry, and multiplies impact
      for generations.
    </p>
  </div>
  {folio("Call to Action", 12)}
</div>
''')

# =================================================================
# PAGE 13 — BACK COVER
# =================================================================
add(f'''
<div class="page navy">
  <div class="frame" style="display:flex; flex-direction:column; justify-content:space-between; align-items:center; text-align:center;">
    <div></div>
    <div>
      <div style="font-family:'Archivo'; font-weight:600; font-size:9.5pt; letter-spacing:0.28em; color:#D9B876;">LIFETOGETHER CHURCH&trade;</div>
      <div style="height:0.26in;"></div>
      <h1 class="display" style="font-size:21pt; color:#FBF8F1;">Let&rsquo;s build it together.</h1>
      <div style="height:0.18in;"></div>
      <p class="lede" style="max-width:4.3in; margin:0 auto;">
        Schedule a consultation to explore which edition of the Biblical Purpose Library fits
        your church right now.
      </p>
      <div style="height:0.34in;"></div>
      <div style="width:30px; height:2px; background:#B98D3E; margin:0 auto;"></div>
      <div style="height:0.2in;"></div>
      <div style="font-family:'Archivo'; font-weight:500; font-size:9pt; letter-spacing:0.08em; color:rgba(251,248,241,0.75);">LIFETOGETHER.COM &nbsp;&middot;&nbsp; BRETT@LIFETOGETHER.COM</div>
    </div>
    <div style="font-family:'Archivo'; font-weight:500; font-size:7.4pt; letter-spacing:0.1em; color:rgba(251,248,241,0.4); line-height:1.8;">
      40 DAY CAMPAIGNS&trade; &nbsp;&middot;&nbsp; CHURCH SEMINARY&trade; &nbsp;&middot;&nbsp; LIFETOGETHER STUDIOS&trade;
    </div>
  </div>
</div>
''')

# =================================================================
# ASSEMBLE
# =================================================================
with open("/home/claude/build/portrait_style.css") as f:
    base_css = f.read()

extra_css = '''
.purpose-grid{ display:grid; grid-template-columns:1fr 1fr; gap:0.18in; }
.purpose-cell{ background:var(--cream); border-left:3px solid var(--gold); padding:0.18in 0.2in; display:flex; align-items:center; gap:0.14in; }
.purpose-num{ font-family:'Playfair'; font-weight:700; font-size:16pt; color:var(--gold); flex-shrink:0; }
.purpose-name{ font-family:'Playfair'; font-weight:700; font-size:11.5pt; color:var(--navy); line-height:1.2; }

.check-grid{ display:flex; flex-direction:column; }
.check-item{ display:flex; align-items:baseline; gap:0.14in; padding:0.09in 0; border-bottom:1px solid var(--line); font-family:'Inter'; font-size:10.3pt; color:var(--ink); }
.check-mark{ color:var(--gold); font-weight:700; }

.week-grid{ display:grid; grid-template-columns:1fr 1fr; gap:0.2in; }
.week-card{ border-top:2px solid var(--gold); padding-top:0.13in; }
.week-tag{ font-family:'Archivo'; font-weight:700; font-size:9.5pt; letter-spacing:0.1em; color:var(--gold); }
.week-title{ font-family:'Playfair'; font-weight:700; font-size:12.5pt; color:var(--navy); margin:0.04in 0 0.06in; line-height:1.2; }
.week-desc{ font-family:'Inter'; font-size:9pt; color:var(--ink); line-height:1.45; }

.collection-card{ border-top:1px solid var(--line); padding-top:0.18in; }
.collection-title{ font-family:'Playfair'; font-weight:700; font-size:15pt; color:var(--navy); }
.collection-sub{ font-family:'Inter'; font-style:italic; font-size:9.8pt; color:var(--gray); margin:0.04in 0 0.12in; }
.collection-list{ list-style:none; display:flex; flex-wrap:wrap; gap:0.08in 0.2in; margin-bottom:0.14in; }
.collection-list li{ font-family:'Inter'; font-size:9.3pt; color:var(--ink); position:relative; padding-left:0.14in; }
.collection-list li::before{ content:'\\2013'; position:absolute; left:0; color:var(--gold); }
.collection-best{ font-family:'Inter'; font-size:9.3pt; color:var(--ink); }
.collection-best .label{ font-family:'Archivo'; font-weight:700; font-size:8.4pt; letter-spacing:0.1em; text-transform:uppercase; color:var(--gold); margin-right:0.08in; }

.mini-card{ border-top:1px solid var(--line); padding:0.16in 0; }
.mini-card:first-child{ padding-top:0; }
.mini-title{ font-family:'Playfair'; font-weight:700; font-size:13pt; color:var(--navy); }
.mini-sub{ font-family:'Inter'; font-style:italic; font-size:9pt; color:var(--gray); margin:0.03in 0 0.07in; }
.mini-bullets{ font-family:'Archivo'; font-weight:500; font-size:8.4pt; letter-spacing:0.02em; color:var(--gold); line-height:1.5; }

.exp-row{ border-top:1px solid var(--line); padding:0.16in 0; }
.exp-row:first-child{ padding-top:0; }
.exp-name{ font-family:'Playfair'; font-weight:700; font-size:12.5pt; color:var(--navy); margin-bottom:0.05in; }
.exp-desc{ font-family:'Inter'; font-size:9.3pt; color:var(--ink); line-height:1.5; }

.aud-grid{ display:grid; grid-template-columns:1fr 1fr; gap:0.1in 0.2in; }
.aud-cell{ font-family:'Archivo'; font-weight:600; font-size:9pt; color:var(--navy); border-bottom:1px solid var(--line); padding:0.06in 0; }

.adapt-grid{ display:grid; grid-template-columns:1fr 1fr; gap:0.08in 0.2in; }
.adapt-cell{ font-family:'Archivo'; font-weight:600; font-size:8.6pt; color:var(--gold); border-bottom:1px solid var(--line); padding:0.05in 0; }
'''

html = f'''<!DOCTYPE html>
<html><head><meta charset="utf-8">
<style>{base_css}{extra_css}</style></head>
<body>{"".join(PAGES)}</body></html>'''

with open("/home/claude/build/purpose_library.html", "w") as f:
    f.write(html)
print("Pages:", len(PAGES))
