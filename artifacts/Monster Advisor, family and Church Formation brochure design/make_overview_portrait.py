import sys
sys.path.insert(0, "/home/claude/build")
from diagrams import step_chain_vertical, vertical_levels

PAGES = []
def add(html): PAGES.append(html)

def photo(caption, extra_style=""):
    return f'''<div class="photo" style="{extra_style}">
        <div class="corner tl"></div><div class="corner br"></div>
        <div class="cap">{caption}</div>
    </div>'''

def folio(chapter, num):
    return f'''<div class="folio"><div class="thread">{chapter}</div><div>{num:02d}</div></div>'''

# PAGE 1 — COVER
add(f'''
<div class="page navy">
  <div class="photo" style="position:absolute; inset:0; border-radius:0;">
    <div class="cap" style="right:0.68in; bottom:0.5in; left:auto; text-align:right; font-size:6.8pt;">PHOTOGRAPHY — PASTOR IN CONVERSATION WITH SMALL GROUP LEADERS</div>
  </div>
  <div style="position:absolute; inset:0; background:linear-gradient(190deg, rgba(16,30,56,0.4) 0%, rgba(16,30,56,0.88) 55%, rgba(16,30,56,0.98) 100%);"></div>
  <div class="frame" style="display:flex; flex-direction:column; justify-content:flex-end;">
    <div style="font-family:'Archivo'; font-weight:600; font-size:9.5pt; letter-spacing:0.3em; color:#D9B876; margin-bottom:2.2in;">EXECUTIVE OVERVIEW</div>
    <h1 class="display" style="font-size:32pt; color:#FBF8F1;">LifeTogether Church Formation System&trade;</h1>
    <div style="height:0.22in;"></div>
    <p class="lede" style="font-size:11pt;">
      A practical framework for helping churches create meaningful spiritual growth through
      churchwide campaigns, small groups, and customized formation journeys.
    </p>
    <div style="height:0.26in;"></div>
    <p style="font-family:'Playfair'; font-style:italic; font-weight:500; font-size:14pt; color:#D9B876; line-height:1.4;">
      You bring the message. We&rsquo;ll help you build the movement.
    </p>
    <div style="height:0.5in;"></div>
    <div style="display:flex; justify-content:space-between; align-items:flex-end; font-family:'Archivo'; font-weight:500; font-size:8pt; letter-spacing:0.12em; color:rgba(251,248,241,0.55);">
      <div>LIFETOGETHER.COM</div>
      <div style="width:22px; height:2px; background:#B98D3E;"></div>
    </div>
  </div>
</div>
''')

# PAGE 2 — THE CHALLENGE
challenge_items = ["A small-group study", "A daily devotional", "A family discussion", "A leadership resource", "A ministry tool", "A future campaign"]
ch_col1 = "".join([f'<div class="opp-item">{x}</div>' for x in challenge_items[:3]])
ch_col2 = "".join([f'<div class="opp-item">{x}</div>' for x in challenge_items[3:]])
add(f'''
<div class="page">
  <div class="frame">
    <div class="eyebrow">THE CHALLENGE</div>
    <div style="height:0.24in;"></div>
    <h1 class="display" style="font-size:24pt; color:var(--navy);">Great churches don&rsquo;t lack sermons. They lack systems.</h1>
    <div style="height:0.18in;"></div>
    <p class="lede">
      Every week pastors invest hours studying Scripture, praying, preparing, and preaching.
      Yet by the following week, most of those messages have already been replaced by the
      next sermon.
    </p>
    <div style="height:0.28in;"></div>
    <div style="font-family:'Archivo'; font-weight:600; font-size:8.6pt; letter-spacing:0.14em; color:var(--gold); margin-bottom:0.05in;">IMAGINE IF EVERY SERMON BECAME</div>
    <p style="font-family:'Inter'; font-size:9.6pt; color:var(--gray); margin-bottom:0.16in;">Imagine if every message became more than a weekend experience.</p>
    <div style="display:flex; gap:0.4in;">
      <div style="flex:1;">{ch_col1}</div>
      <div style="flex:1;">{ch_col2}</div>
    </div>
    <div style="height:0.36in;"></div>
    <div class="pull-quote">Your greatest sermons deserve <span class="mark">more than one Sunday.</span></div>
  </div>
  {folio("The Challenge", 2)}
</div>
''')

# PAGE 3 — THE OPPORTUNITY
add(f'''
<div class="page">
  <div class="frame">
    <div class="eyebrow">THE OPPORTUNITY</div>
    <div style="height:0.24in;"></div>
    <h1 class="display" style="font-size:24pt; color:var(--navy);">From Message to Movement</h1>
    <div style="height:0.24in;"></div>
    <div class="escalate">
      <div class="e1">Most churches think in sermon series.</div>
      <div class="e2">Healthy churches think in discipleship pathways.</div>
      <div class="e3">Transformational churches think in movements.</div>
    </div>
    <div style="height:0.2in;"></div>
    <p class="lede">
      The Church Formation System helps pastors move from isolated messages to intentional
      spiritual journeys.
    </p>
    <div style="height:0.3in;"></div>
    <div class="reframe-box">
      <div class="reframe-old">
        <div class="label">INSTEAD OF ASKING</div>
        <div class="q">&ldquo;What should I preach next?&rdquo;</div>
      </div>
      <div class="reframe-arrow">&darr;</div>
      <div class="reframe-new">
        <div class="label">WE BEGIN BY ASKING</div>
        <div class="q">&ldquo;What does God want to form in our people over the next 18 to 24 months?&rdquo;</div>
      </div>
    </div>
    <div style="height:0.3in;"></div>
    <div class="pull-quote">Everything else <span class="mark">flows from that question.</span></div>
  </div>
  {folio("The Opportunity", 3)}
</div>
''')

# PAGE 4 — HOW IT WORKS
steps = [
    ("DISCERN", "Clarify what God is calling your church to become."),
    ("DEVELOP", "Transform sermons into curriculum, devotionals, leader guides, and discussion resources."),
    ("PRODUCE", "Create engaging videos and teaching experiences at a level your church can sustain."),
    ("PUBLISH", "Package everything into a complete campaign experience."),
    ("MOBILIZE", "Launch your church into one unified spiritual journey, and prepare for what comes next."),
]
add(f'''
<div class="page">
  <div class="frame">
    <div class="eyebrow">HOW IT WORKS</div>
    <div style="height:0.22in;"></div>
    <h1 class="display" style="font-size:24pt; color:var(--navy);">Five simple steps</h1>
    <div style="height:0.2in;"></div>
    <div style="width:100%; height:7.3in;">{step_chain_vertical(steps)}</div>
  </div>
  {folio("How It Works", 4)}
</div>
''')

# PAGE 5 — WHAT WE HELP YOU BUILD
build_items = ["21-Day Challenges","30-Day Journeys","40-Day Campaigns","Small-Group Studies","Daily Devotionals","Leader Guides","Family Resources","Video Studies","Ministry Playbooks","Digital Courses","Churchwide Formation Experiences"]
grid_cells = "".join([f'<div class="build-cell">{b}</div>' for b in build_items[:-1]])
grid_cells += f'<div class="build-cell wide"><span class="rule"></span>{build_items[-1]}<span class="rule"></span></div>'
add(f'''
<div class="page">
  <div class="frame">
    <div class="eyebrow">WHAT WE HELP YOU BUILD</div>
    <div style="height:0.2in;"></div>
    <h1 class="display" style="font-size:20pt; color:var(--navy); line-height:1.3;">Whether you begin with one sermon series or an entire ministry strategy, we can help you create:</h1>
    <div style="height:0.26in;"></div>
    <div class="build-grid">{grid_cells}</div>
    <div style="height:0.3in;"></div>
    <div class="takeaway">
      <span class="label">Takeaway</span>
      Each resource is designed to strengthen discipleship, not simply create content.
    </div>
  </div>
  {folio("What We Help You Build", 5)}
</div>
''')

# PAGE 6 — A PATHWAY THAT FITS YOUR CHURCH
levels = [
    ("1", "Use a Proven Campaign", "Launch quickly using a trusted framework."),
    ("2", "Customize a Campaign", "Add your stories, your voice, and your church's unique next steps."),
    ("3", "Build an Original Campaign", "Transform your own sermons into a complete discipleship journey."),
    ("4", "Build a Ministry Library", "Organize years of teaching into a reusable content system."),
    ("5", "Multiply Your Ministry", "Publish, share, and extend your church's impact for years to come."),
]
add(f'''
<div class="page">
  <div class="frame">
    <div class="eyebrow">A PATHWAY THAT FITS YOUR CHURCH</div>
    <div style="height:0.2in;"></div>
    <h1 class="display" style="font-size:22pt; color:var(--navy);">Start where you are</h1>
    <div style="height:0.16in;"></div>
    <div style="width:100%; height:7.6in;">{vertical_levels(levels)}</div>
  </div>
  {folio("A Pathway That Fits Your Church", 6)}
</div>
''')

# PAGE 7 — HOW WE CAN HELP
offers = [
    ("Church Formation Intensive", "A six-week planning experience", "A focused six-week planning experience that results in a complete campaign blueprint."),
    ("90-Day Campaign Accelerator", "From idea to launch-ready", "Hands-on coaching to move from idea to launch-ready."),
    ("Annual Church Formation Partnership", "An 18 to 24 month strategy", "Ongoing coaching, planning, content development, and strategic guidance as you build an intentional 18-to-24-month formation strategy."),
]
offer_cards = "".join([f'''
    <div class="offer-card" style="margin-bottom:0.2in;">
      <div style="width:30px; height:2px; background:var(--gold); margin-bottom:0.16in;"></div>
      <div style="font-family:'Playfair'; font-weight:700; font-size:14.5pt; color:var(--navy); line-height:1.22;">{name}</div>
      <div style="font-family:'Archivo'; font-weight:600; font-size:8.3pt; letter-spacing:0.1em; text-transform:uppercase; color:var(--gold); margin:0.08in 0 0.14in;">{sub}</div>
      <p style="font-family:'Inter'; font-size:9.6pt; line-height:1.55; color:var(--ink);">{desc}</p>
    </div>''' for name, sub, desc in offers])
add(f'''
<div class="page">
  <div class="frame">
    <div class="eyebrow">HOW WE CAN HELP</div>
    <div style="height:0.2in;"></div>
    <h1 class="display" style="font-size:21pt; color:var(--navy); line-height:1.3;">Every church is different. That&rsquo;s why we offer several ways to work together.</h1>
    <div style="height:0.26in;"></div>
    {offer_cards}
    <div style="height:0.1in;"></div>
    <div class="pull-quote" style="font-size:13.5pt;">Wherever you are today, <span class="mark">we&rsquo;ll help you take the next step.</span></div>
  </div>
  {folio("How We Can Help", 7)}
</div>
''')

# PAGE 8 — BACK COVER
add(f'''
<div class="page navy">
  <div class="frame" style="display:flex; flex-direction:column; justify-content:space-between; align-items:center; text-align:center;">
    <div></div>
    <div>
      <h1 class="display" style="font-size:23pt; color:#FBF8F1;">Your greatest sermons shouldn&rsquo;t end on Sunday.</h1>
      <div style="height:0.2in;"></div>
      <p class="lede" style="max-width:4.8in; margin:0 auto;">
        They can become curriculum. That curriculum can build community. That community can
        become a movement. And that movement can shape lives long after the message is preached.
      </p>
      <div style="height:0.36in;"></div>
      <div style="width:30px; height:2px; background:#B98D3E; margin:0 auto;"></div>
      <div style="height:0.22in;"></div>
      <div style="font-family:'Playfair'; font-weight:600; font-style:italic; font-size:13pt; color:#D9B876;">Ready to begin?</div>
      <div style="height:0.1in;"></div>
      <p class="lede" style="max-width:4.6in; margin:0 auto; font-size:10pt;">
        Schedule a complimentary Church Formation Strategy Conversation. Discover how your next
        sermon series could become the beginning of your church&rsquo;s next great discipleship journey.
      </p>
    </div>
    <div>
      <div style="font-family:'Archivo'; font-weight:600; font-size:8.6pt; letter-spacing:0.22em; color:rgba(251,248,241,0.75);">LIFETOGETHER CHURCH FORMATION SYSTEM&trade;</div>
      <div style="height:0.06in;"></div>
      <div style="font-family:'Playfair'; font-style:italic; font-weight:500; font-size:10pt; color:rgba(217,184,118,0.85);">You bring the message. We&rsquo;ll help you build the movement.</div>
    </div>
  </div>
</div>
''')

with open("/home/claude/build/portrait_style.css") as f:
    base_css = f.read()

html = f'''<!DOCTYPE html>
<html><head><meta charset="utf-8">
<style>{base_css}</style></head>
<body>{"".join(PAGES)}</body></html>'''

with open("/home/claude/build/overview_portrait.html", "w") as f:
    f.write(html)
print("Pages:", len(PAGES))
