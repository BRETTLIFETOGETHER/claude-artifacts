import sys
sys.path.insert(0, "/home/claude/build")
from diagrams import step_chain_diagram, generic_staircase

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

# =================================================================
# PAGE 1 — COVER
# =================================================================
add(f'''
<div class="page navy">
  <div class="photo" style="position:absolute; inset:0; border-radius:0;">
    <div class="cap" style="right:0.9in; bottom:0.6in; left:auto; text-align:right; font-size:7.6pt;">PHOTOGRAPHY — PASTOR IN CONVERSATION WITH SMALL GROUP LEADERS</div>
  </div>
  <div style="position:absolute; inset:0; background:linear-gradient(100deg, rgba(16,30,56,0.97) 0%, rgba(16,30,56,0.88) 32%, rgba(16,30,56,0.32) 64%, rgba(16,30,56,0.08) 100%);"></div>
  <div class="frame" style="display:flex; flex-direction:column; justify-content:space-between;">
    <div style="font-family:'Archivo'; font-weight:600; font-size:10pt; letter-spacing:0.3em; color:#D9B876;">EXECUTIVE OVERVIEW</div>
    <div style="max-width:6.9in;">
      <h1 class="display" style="font-size:44pt; color:#FBF8F1;">LifeTogether Church<br/>Formation System<span style="font-size:19pt; vertical-align:super;">™</span></h1>
      <div style="height:0.28in;"></div>
      <p class="lede" style="max-width:6.4in; font-size:12.5pt;">
        A practical framework for helping churches create meaningful spiritual growth through
        churchwide campaigns, small groups, and customized formation journeys.
      </p>
      <div style="height:0.34in;"></div>
      <p style="font-family:'Playfair'; font-style:italic; font-weight:500; font-size:16.5pt; color:#D9B876; line-height:1.4;">
        You bring the message. We&rsquo;ll help you build the movement.
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
# PAGE 2 — THE CHALLENGE
# =================================================================
challenge_items = [
    "A small-group study", "A daily devotional", "A family discussion",
    "A leadership resource", "A ministry tool", "A future campaign",
]
ch_col1 = "".join([f'<div class="opp-item">{x}</div>' for x in challenge_items[:3]])
ch_col2 = "".join([f'<div class="opp-item">{x}</div>' for x in challenge_items[3:]])

add(f'''
<div class="page">
  <div class="frame">
    <div class="eyebrow">THE CHALLENGE</div>
    <div style="height:0.28in;"></div>
    <div style="display:flex; gap:0.75in;">
      <div style="width:4.6in;">
        <h1 class="display" style="font-size:31pt; color:var(--navy);">Great churches don&rsquo;t lack sermons.<br/>They lack systems.</h1>
        <div style="height:0.22in;"></div>
        <p class="lede">
          Every week pastors invest hours studying Scripture, praying, preparing, and preaching.
          Yet by the following week, most of those messages have already been replaced by the
          next sermon.
        </p>
      </div>
      <div style="flex:1; display:flex; flex-direction:column; justify-content:center;">
        <div style="font-family:'Archivo'; font-weight:600; font-size:9.5pt; letter-spacing:0.14em; color:var(--gold); margin-bottom:0.05in;">IMAGINE IF EVERY SERMON BECAME</div>
        <p style="font-family:'Inter'; font-size:10pt; color:var(--gray); margin-bottom:0.2in;">Imagine if every message became more than a weekend experience.</p>
        <div style="display:flex; gap:0.4in;">
          <div style="flex:1; display:flex; flex-direction:column;">{ch_col1}</div>
          <div style="flex:1; display:flex; flex-direction:column;">{ch_col2}</div>
        </div>
      </div>
    </div>
    <div style="height:0.36in;"></div>
    <div class="pull-quote">Your greatest sermons deserve <span class="mark">more than one Sunday.</span></div>
  </div>
  {folio("The Challenge", 2)}
</div>
''')

# =================================================================
# PAGE 3 — THE OPPORTUNITY
# =================================================================
add(f'''
<div class="page">
  <div class="frame">
    <div class="eyebrow">THE OPPORTUNITY</div>
    <div style="height:0.26in;"></div>
    <h1 class="display" style="font-size:31pt; color:var(--navy);">From Message to Movement</h1>
    <div style="height:0.3in;"></div>
    <div style="display:flex; gap:0.7in;">
      <div style="width:4.5in;">
        <div class="escalate">
          <div class="e1">Most churches think in sermon series.</div>
          <div class="e2">Healthy churches think in discipleship pathways.</div>
          <div class="e3">Transformational churches think in movements.</div>
        </div>
        <div style="height:0.24in;"></div>
        <p class="lede">
          The Church Formation System helps pastors move from isolated messages to intentional
          spiritual journeys.
        </p>
      </div>
      <div style="flex:1; display:flex; flex-direction:column; justify-content:center;">
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
      </div>
    </div>
    <div style="height:0.3in;"></div>
    <div class="pull-quote">Everything else <span class="mark">flows from that question.</span></div>
  </div>
  {folio("The Opportunity", 3)}
</div>
''')

# =================================================================
# PAGE 4 — HOW IT WORKS
# =================================================================
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
    <div style="height:0.24in;"></div>
    <h1 class="display" style="font-size:31pt; color:var(--navy);">Five simple steps</h1>
    <div style="height:0.2in;"></div>
    <div style="width:100%; height:4.9in;">{step_chain_diagram(steps)}</div>
  </div>
  {folio("How It Works", 4)}
</div>
''')

# =================================================================
# PAGE 5 — WHAT WE HELP YOU BUILD
# =================================================================
build_items = [
    "21-Day Challenges", "30-Day Journeys", "40-Day Campaigns", "Small-Group Studies",
    "Daily Devotionals", "Leader Guides", "Family Resources", "Video Studies",
    "Ministry Playbooks", "Digital Courses", "Churchwide Formation Experiences",
]
grid_cells = "".join([f'<div class="build-cell">{b}</div>' for b in build_items])
add(f'''
<div class="page">
  <div class="frame">
    <div class="eyebrow">WHAT WE HELP YOU BUILD</div>
    <div style="height:0.22in;"></div>
    <h1 class="display" style="font-size:24pt; color:var(--navy); max-width:8.4in; line-height:1.25;">Whether you begin with one sermon series or an entire ministry strategy, we can help you create:</h1>
    <div style="height:0.28in;"></div>
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

# =================================================================
# PAGE 6 — A PATHWAY THAT FITS YOUR CHURCH
# =================================================================
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
    <div style="height:0.22in;"></div>
    <h1 class="display" style="font-size:31pt; color:var(--navy);">Start where you are</h1>
    <div style="width:100%; height:5.3in;">{generic_staircase(levels)}</div>
  </div>
  {folio("A Pathway That Fits Your Church", 6)}
</div>
''')

# =================================================================
# PAGE 7 — HOW WE CAN HELP
# =================================================================
offers = [
    ("Church Formation Intensive", "A six-week planning experience", "A focused six-week planning experience that results in a complete campaign blueprint."),
    ("90-Day Campaign Accelerator", "From idea to launch-ready", "Hands-on coaching to move from idea to launch-ready."),
    ("Annual Church Formation Partnership", "An 18 to 24 month strategy", "Ongoing coaching, planning, content development, and strategic guidance as you build an intentional 18-to-24-month formation strategy."),
]
offer_cards = "".join([f'''
    <div class="offer-card">
      <div style="width:34px; height:2px; background:var(--gold); margin-bottom:0.2in;"></div>
      <div style="font-family:'Playfair'; font-weight:700; font-size:16.5pt; color:var(--navy); line-height:1.22;">{name}</div>
      <div style="font-family:'Archivo'; font-weight:600; font-size:9.1pt; letter-spacing:0.1em; text-transform:uppercase; color:var(--gold); margin:0.1in 0 0.18in;">{sub}</div>
      <p style="font-family:'Inter'; font-size:9.8pt; line-height:1.55; color:var(--ink);">{desc}</p>
    </div>''' for name, sub, desc in offers])

add(f'''
<div class="page">
  <div class="frame">
    <div class="eyebrow">HOW WE CAN HELP</div>
    <div style="height:0.24in;"></div>
    <h1 class="display" style="font-size:27pt; color:var(--navy); max-width:8.2in;">Every church is different. That&rsquo;s why we offer several ways to work together.</h1>
    <div style="height:0.32in;"></div>
    <div style="display:flex; gap:0.4in;">{offer_cards}</div>
    <div style="height:0.34in;"></div>
    <div class="pull-quote">Wherever you are today, <span class="mark">we&rsquo;ll help you take the next step.</span></div>
  </div>
  {folio("How We Can Help", 7)}
</div>
''')

# =================================================================
# PAGE 8 — BACK COVER
# =================================================================
add(f'''
<div class="page navy">
  <div class="frame" style="display:flex; flex-direction:column; justify-content:space-between; align-items:center; text-align:center;">
    <div></div>
    <div>
      <h1 class="display" style="font-size:28pt; color:#FBF8F1; max-width:6.8in;">Your greatest sermons shouldn&rsquo;t end on Sunday.</h1>
      <div style="height:0.24in;"></div>
      <p class="lede" style="max-width:5.6in; margin:0 auto;">
        They can become curriculum. That curriculum can build community. That community can
        become a movement. And that movement can shape lives long after the message is preached.
      </p>
      <div style="height:0.4in;"></div>
      <div style="width:34px; height:2px; background:#B98D3E; margin:0 auto;"></div>
      <div style="height:0.26in;"></div>
      <div style="font-family:'Playfair'; font-weight:600; font-style:italic; font-size:14.5pt; color:#D9B876;">Ready to begin?</div>
      <div style="height:0.12in;"></div>
      <p class="lede" style="max-width:5.4in; margin:0 auto; font-size:11pt;">
        Schedule a complimentary Church Formation Strategy Conversation. Discover how your next
        sermon series could become the beginning of your church&rsquo;s next great discipleship journey.
      </p>
    </div>
    <div>
      <div style="font-family:'Archivo'; font-weight:600; font-size:9.5pt; letter-spacing:0.24em; color:rgba(251,248,241,0.75);">LIFETOGETHER CHURCH FORMATION SYSTEM&trade;</div>
      <div style="height:0.08in;"></div>
      <div style="font-family:'Playfair'; font-style:italic; font-weight:500; font-size:11pt; color:rgba(217,184,118,0.85);">You bring the message. We&rsquo;ll help you build the movement.</div>
    </div>
  </div>
</div>
''')

# =================================================================
# ASSEMBLE
# =================================================================
extra_css = '''
.opp-item{
  font-family:'Playfair'; font-weight:700; font-size:13pt; color:var(--navy);
  padding:0.09in 0; border-bottom:1px solid var(--line);
}
.build-grid{
  display:grid; grid-template-columns:repeat(4, 1fr); gap:0.22in;
}
.build-cell{
  font-family:'Playfair'; font-weight:700; font-size:12.5pt; color:var(--navy);
  background:var(--cream); border-left:3px solid var(--gold);
  padding:0.2in 0.22in; line-height:1.25;
}
.offer-card{ flex:1; border-top:1px solid var(--line); padding-top:0.22in; }

.escalate div{ font-family:'Playfair'; font-weight:600; color:var(--navy); line-height:1.3; }
.escalate .e1{ font-size:13pt; color:var(--gray); font-weight:500; }
.escalate .e2{ font-size:17pt; color:var(--navy); margin:0.08in 0; }
.escalate .e3{ font-size:23pt; color:var(--gold); font-weight:700; }

.reframe-box{
  background:var(--cream); border-radius:2px; padding:0.32in 0.34in;
}
.reframe-old, .reframe-new{ }
.reframe-box .label{
  font-family:'Archivo'; font-weight:600; font-size:8.6pt; letter-spacing:0.16em;
  color:var(--gold); margin-bottom:0.08in;
}
.reframe-box .q{
  font-family:'Playfair'; font-style:italic; font-weight:600; font-size:14pt; color:var(--navy); line-height:1.35;
}
.reframe-old .q{ color:var(--gray); }
.reframe-arrow{
  text-align:center; color:var(--gold); font-size:16pt; margin:0.14in 0; font-family:'Archivo';
}
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

with open("/home/claude/build/overview.html", "w") as f:
    f.write(html)

print("Pages:", len(PAGES))
