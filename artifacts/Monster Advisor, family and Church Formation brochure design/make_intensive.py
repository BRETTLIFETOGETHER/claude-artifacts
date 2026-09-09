import sys
sys.path.insert(0, "/home/claude/build")
from diagrams import step_chain_diagram

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

def track_card(name, sub, para, bullets):
    bl = "".join([f'<li>{b}</li>' for b in bullets])
    return f'''
    <div class="track-card">
      <div style="font-family:'Archivo'; font-weight:700; font-size:11.5pt; letter-spacing:0.14em; color:var(--gold);">{name}</div>
      <div style="font-family:'Playfair'; font-weight:700; font-size:14pt; color:var(--navy); margin:0.06in 0 0.12in;">{sub}</div>
      <p style="font-family:'Inter'; font-size:9.2pt; line-height:1.5; color:var(--ink); min-height:0.7in;">{para}</p>
      <ul class="track-list">{bl}</ul>
    </div>'''

# =================================================================
# PAGE 1 — COVER
# =================================================================
add(f'''
<div class="page navy">
  <div class="photo" style="position:absolute; inset:0; border-radius:0;">
    <div class="cap" style="right:0.9in; bottom:0.6in; left:auto; text-align:right; font-size:7.6pt;">PHOTOGRAPHY — PASTOR AND CONSULTANT REVIEWING A CAMPAIGN OUTLINE TOGETHER</div>
  </div>
  <div style="position:absolute; inset:0; background:linear-gradient(100deg, rgba(16,30,56,0.97) 0%, rgba(16,30,56,0.89) 33%, rgba(16,30,56,0.34) 64%, rgba(16,30,56,0.08) 100%);"></div>
  <div class="frame" style="display:flex; flex-direction:column; justify-content:space-between;">
    <div style="font-family:'Archivo'; font-weight:600; font-size:10.5pt; letter-spacing:0.3em; color:#D9B876;">LIFETOGETHER</div>
    <div style="max-width:6.9in;">
      <div style="font-family:'Archivo'; font-weight:600; font-size:10pt; letter-spacing:0.22em; color:#D9B876; margin-bottom:0.3in;">A CONSULTING GUIDE FOR SENIOR PASTORS</div>
      <h1 class="display" style="font-size:46pt; color:#FBF8F1;">Campaign Builder<br/>Intensive</h1>
      <div style="height:0.3in;"></div>
      <p style="font-family:'Playfair'; font-style:italic; font-weight:500; font-size:16pt; color:#D9B876; line-height:1.5; max-width:5.8in;">
        A collaborative ministry-building process that turns your sermons into a complete
        churchwide discipleship experience.
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
# PAGE 2 — WHY CHURCHES GET STUCK
# =================================================================
stuck_reasons = [
    ("Too many good ideas", "A dozen directions worth pursuing, and no clear place to start."),
    ("No bandwidth to build", "Weekly ministry already fills every hour your team has."),
    ("Uncertainty about the path", "Turning a sermon into a full experience feels like guesswork."),
    ("Past momentum that faded", "An earlier attempt lost steam somewhere around week two."),
]
stuck_cards = "".join([f'''
    <div style="flex:1; border-top:2px solid var(--gold); padding-top:0.16in;">
      <div style="font-family:'Playfair'; font-weight:700; font-size:13.5pt; color:var(--navy); margin-bottom:0.08in;">{t}</div>
      <div style="font-family:'Inter'; font-size:9.4pt; color:var(--ink); line-height:1.5;">{d}</div>
    </div>''' for t, d in stuck_reasons])

add(f'''
<div class="page">
  <div class="frame">
    <div class="eyebrow">WHY CHURCHES GET STUCK</div>
    <div style="height:0.26in;"></div>
    <h1 class="display" style="font-size:29pt; color:var(--navy); max-width:8.2in;">You don&rsquo;t need another idea. You need a process.</h1>
    <div style="height:0.18in;"></div>
    <p class="lede" style="max-width:8in;">
      Almost every pastor we talk with already has more than enough vision and content to
      build a full campaign. What&rsquo;s missing isn&rsquo;t inspiration &mdash; it&rsquo;s a clear, guided
      process to get from a sermon idea to a finished, launch-ready experience.
    </p>
    <div style="height:0.3in;"></div>
    <div style="display:flex; gap:0.4in;">{stuck_cards}</div>
    <div style="height:0.4in;"></div>
    <div class="pull-quote">You already have the message. <span class="mark">You just need the process to build with it.</span></div>
  </div>
  {folio("Why Churches Get Stuck", 2)}
</div>
''')

# =================================================================
# PAGE 3 — WHAT WE BUILD TOGETHER
# =================================================================
audiences = [
    "Vision campaigns", "Spiritual growth campaigns", "Stewardship campaigns",
    "Family campaigns", "Prayer campaigns", "Custom sermon-based journeys",
]
aud_col1 = "".join([f'<div class="opp-item">{x}</div>' for x in audiences[:3]])
aud_col2 = "".join([f'<div class="opp-item">{x}</div>' for x in audiences[3:]])

add(f'''
<div class="page">
  <div class="frame">
    <div class="eyebrow">WHAT WE BUILD TOGETHER</div>
    <div style="height:0.26in;"></div>
    <div style="display:flex; gap:0.75in;">
      <div style="width:4.6in;">
        <h1 class="display" style="font-size:28pt; color:var(--navy);">Not curriculum writing. Not coaching alone.</h1>
        <div style="height:0.2in;"></div>
        <p class="lede">
          This is a collaborative ministry-building process that helps pastors transform
          their sermons into a complete churchwide discipleship experience &mdash; built with
          your team, not delivered to them.
        </p>
        <div style="height:0.18in;"></div>
        <p class="lede">
          It works for churches preparing to launch any kind of sermon-based journey.
        </p>
      </div>
      <div style="flex:1; display:flex; flex-direction:column; justify-content:center;">
        <div style="font-family:'Archivo'; font-weight:600; font-size:9.5pt; letter-spacing:0.14em; color:var(--gold); margin-bottom:0.16in;">BUILT FOR CHURCHES PREPARING TO LAUNCH</div>
        <div style="display:flex; gap:0.4in;">
          <div style="flex:1; display:flex; flex-direction:column;">{aud_col1}</div>
          <div style="flex:1; display:flex; flex-direction:column;">{aud_col2}</div>
        </div>
      </div>
    </div>
  </div>
  {folio("What We Build Together", 3)}
</div>
''')

# =================================================================
# PAGE 4 — THE SIX-WEEK INTENSIVE (intro, navy divider)
# =================================================================
week_chips = "".join([f'<div class="track-chip">WEEK {i+1}<br/><span style="font-size:8.6pt; letter-spacing:0.06em;">{w}</span></div>' for i, w in enumerate(["DISCOVER","DISCERN","DESIGN","DEVELOP","PRODUCE","LAUNCH BLUEPRINT"])])
add(f'''
<div class="page navy">
  <div class="frame" style="display:flex; flex-direction:column; justify-content:center;">
    <div class="eyebrow">THE SIX-WEEK INTENSIVE</div>
    <div style="height:0.28in;"></div>
    <h1 class="display" style="font-size:32pt; color:#FBF8F1; max-width:7.6in;">Six weeks. One complete campaign blueprint.</h1>
    <div style="height:0.24in;"></div>
    <p class="lede" style="max-width:6.4in;">
      Each week builds on the last, moving your team from a raw idea to a finished,
      launch-ready plan &mdash; with our team working alongside yours the entire way.
    </p>
    <div style="height:0.4in;"></div>
    <div style="display:flex; gap:0.16in; flex-wrap:wrap;">{week_chips}</div>
  </div>
  {folio("The Six-Week Intensive", 4)}
</div>
''')

# =================================================================
# PAGE 5 — WEEKS 1-3
# =================================================================
weeks_1_3 = [
    ("WEEK 1", "Discover", "We start by listening &mdash; to your church&rsquo;s season, your congregation&rsquo;s needs, and the message God has already given you to preach.",
     ["Review your church's current season", "Clarify your campaign's purpose", "Identify your congregation's real needs", "Set the outcomes you're building toward"]),
    ("WEEK 2", "Discern", "Together we identify the single true center of your message &mdash; the one idea strong enough to carry a full campaign.",
     ["Name the one idea worth building around", "Choose the Scripture that carries it", "Separate the message from the moment", "Confirm it fits your church's voice"]),
    ("WEEK 3", "Design", "Your message becomes a multi-week arc, with its own pacing, structure, and turn toward application.",
     ["Map the full campaign arc, week by week", "Design the emotional and spiritual pacing", "Plan the invitation and response points", "Sketch the formats each week will need"]),
]
add(f'''
<div class="page">
  <div class="frame">
    <div class="eyebrow">THE SIX-WEEK INTENSIVE &mdash; WEEKS ONE THROUGH THREE</div>
    <div style="height:0.24in;"></div>
    <div style="display:flex; gap:0.4in;">{"".join([track_card(*t) for t in weeks_1_3])}</div>
  </div>
  {folio("The Six-Week Intensive", 5)}
</div>
''')

# =================================================================
# PAGE 6 — WEEKS 4-6 + quote
# =================================================================
weeks_4_6 = [
    ("WEEK 4", "Develop", "The arc becomes real content &mdash; curriculum, devotionals, and training, shaped for how your church will actually use them.",
     ["Draft small group discussion guides", "Outline daily devotional content", "Build a leader training framework", "Prepare family conversation prompts"]),
    ("WEEK 5", "Produce", "We plan the video, design, and production elements at a level your church can sustain long after the intensive ends.",
     ["Plan your video and teaching content", "Set the visual identity and design direction", "Scope what your team can produce in-house", "Identify where outside help is worth it"]),
    ("WEEK 6", "Launch Blueprint", "Everything comes together into one finished, launch-ready plan &mdash; including your very next step, on Day 41.",
     ["Finalize the promotion and launch calendar", "Prepare the pulpit announcement path", "Train leaders to carry the campaign well", "Set your Day 41 strategy"]),
]
add(f'''
<div class="page">
  <div class="frame">
    <div class="eyebrow">THE SIX-WEEK INTENSIVE &mdash; WEEKS FOUR THROUGH SIX</div>
    <div style="height:0.24in;"></div>
    <div style="display:flex; gap:0.4in;">{"".join([track_card(*t) for t in weeks_4_6])}</div>
    <div style="height:0.32in;"></div>
    <div class="pull-quote">Six weeks from now, you won&rsquo;t just have an idea. <span class="mark">You&rsquo;ll have a launch-ready campaign.</span></div>
  </div>
  {folio("The Six-Week Intensive", 6)}
</div>
''')

# =================================================================
# PAGE 7 — DELIVERABLES
# =================================================================
deliverables = [
    "Campaign strategy", "Sermon roadmap", "Curriculum outline", "Video plan",
    "Leader resources", "Promotion plan", "Launch calendar", "Day 41 strategy",
]
grid_cells = "".join([f'<div class="build-cell">{b}</div>' for b in deliverables])
add(f'''
<div class="page">
  <div class="frame">
    <div class="eyebrow">DELIVERABLES</div>
    <div style="height:0.22in;"></div>
    <h1 class="display" style="font-size:28pt; color:var(--navy); max-width:8in;">What you walk away with</h1>
    <div style="height:0.14in;"></div>
    <p class="lede" style="max-width:8in;">Eight concrete deliverables, ready to hand to your staff and launch team.</p>
    <div style="height:0.28in;"></div>
    <div class="build-grid two-row">{grid_cells}</div>
    <div style="height:0.3in;"></div>
    <div class="takeaway">
      <span class="label">Why Day 41 matters</span>
      Most campaigns end on Day 40 with no plan for what comes next. Yours won&rsquo;t &mdash; the Day 41 strategy is built in from the start.
    </div>
  </div>
  {folio("Deliverables", 7)}
</div>
''')

# =================================================================
# PAGE 8 — OPTIONAL 90-DAY ACCELERATOR
# =================================================================
add(f'''
<div class="page">
  <div class="frame" style="display:flex; gap:0.75in;">
    <div style="width:4.6in; display:flex; flex-direction:column; justify-content:center;">
      <div class="eyebrow">OPTIONAL &mdash; THE 90-DAY ACCELERATOR</div>
      <div style="height:0.24in;"></div>
      <h1 class="display" style="font-size:28pt; color:var(--navy);">From blueprint to a fully launched campaign</h1>
      <div style="height:0.2in;"></div>
      <p class="lede">
        The Intensive gives your church a complete plan. For churches who want hands-on
        help carrying that plan all the way to launch, the 90-Day Accelerator adds ongoing
        production support and coaching through the entire launch season.
      </p>
      <div style="height:0.18in;"></div>
      <div class="takeaway">
        <span class="label">Best for</span>
        Churches ready to move quickly &mdash; from a finished blueprint to a fully launched campaign in one season.
      </div>
    </div>
    <div style="flex:1;">{photo("PHOTOGRAPHY — LAUNCH TEAM PREPARING MATERIALS BEFORE A SERVICE", "height:100%;")}</div>
  </div>
  {folio("The 90-Day Accelerator", 8)}
</div>
''')

# =================================================================
# PAGE 9 — ANNUAL CHURCH FORMATION PARTNERSHIP
# =================================================================
add(f'''
<div class="page navy">
  <div class="frame" style="display:flex; flex-direction:column; justify-content:center;">
    <div class="eyebrow">FOR THE LONGER JOURNEY &mdash; THE ANNUAL PARTNERSHIP</div>
    <div style="height:0.24in;"></div>
    <h1 class="display" style="font-size:28pt; color:#FBF8F1; max-width:7.4in;">A twelve-month relationship, for churches building a whole formation calendar.</h1>
    <div style="height:0.2in;"></div>
    <p class="lede" style="max-width:6.4in;">
      Some churches need one campaign built well. Others are ready to build an entire year
      of formation, and to develop their own team&rsquo;s ability to build campaigns without
      outside help. The Annual Church Formation Partnership is ongoing coaching, planning,
      and content development across a full year &mdash; the natural next step after your first
      Intensive.
    </p>
  </div>
  {folio("The Annual Formation Partnership", 9)}
</div>
''')

# =================================================================
# PAGE 10 — INVESTMENT OVERVIEW
# =================================================================
compare_rows = [
    ("Length", "Six weeks", "One season (about 90 days)", "Twelve months"),
    ("Best for", "Your first complete campaign blueprint", "Carrying that blueprint to a full launch", "A whole year of formation, and a trained team"),
    ("Format", "Guided weekly planning sessions", "Hands-on production &amp; launch support", "Ongoing coaching &amp; team training"),
    ("Investment", "A one-time program fee", "A one-time program fee for the season", "An ongoing annual partnership fee"),
]
def compare_row(label, a, b, c, header=False):
    cls = "cmp-head" if header else "cmp-row"
    return f'''
    <div class="{cls}">
      <div class="cmp-cell cmp-label">{label}</div>
      <div class="cmp-cell">{a}</div>
      <div class="cmp-cell">{b}</div>
      <div class="cmp-cell">{c}</div>
    </div>'''
header_row = compare_row("", "Campaign Builder<br/>Intensive", "90-Day<br/>Accelerator", "Annual Formation<br/>Partnership", header=True)
body_rows = "".join([compare_row(l,a,b,c) for l,a,b,c in compare_rows])

add(f'''
<div class="page">
  <div class="frame">
    <div class="eyebrow">INVESTMENT OVERVIEW</div>
    <div style="height:0.24in;"></div>
    <h1 class="display" style="font-size:26pt; color:var(--navy);">Three ways to work together</h1>
    <div style="height:0.28in;"></div>
    <div class="cmp-table">{header_row}{body_rows}</div>
    <div style="height:0.24in;"></div>
    <p style="font-family:'Inter'; font-size:9pt; color:var(--gray); font-style:italic; max-width:8in;">
      Specific investment figures vary by church size and scope, and are confirmed during your
      strategy conversation.
    </p>
  </div>
  {folio("Investment Overview", 10)}
</div>
''')

# =================================================================
# PAGE 11 — FAQ
# =================================================================
faqs = [
    ("What if we fall behind during one of the six weeks?", "The process is flexible enough to adjust &mdash; we build around your church's calendar, not the other way around."),
    ("Do we need video production experience?", "No. We help you scope a video plan that matches your church's actual capacity, from simple to fully produced."),
    ("What size church is this built for?", "The Intensive has worked for churches from a few hundred to several thousand &mdash; the process scales to your team."),
    ("Can our staff keep building after the Intensive ends?", "Yes. That is the goal. You leave with both a finished blueprint and a repeatable process your team can use again."),
    ("What happens after the six weeks?", "You launch with a complete plan in hand. Many churches choose the 90-Day Accelerator for launch support, or the Annual Partnership to keep building."),
]
faq_rows = "".join([f'''
    <div style="padding:0.14in 0; border-bottom:1px solid var(--line);">
      <div style="font-family:'Playfair'; font-weight:700; font-size:12.5pt; color:var(--navy); margin-bottom:0.05in;">{q}</div>
      <div style="font-family:'Inter'; font-size:9.4pt; color:var(--ink); line-height:1.5; max-width:7.8in;">{a}</div>
    </div>''' for q, a in faqs])
add(f'''
<div class="page">
  <div class="frame">
    <div class="eyebrow">FREQUENTLY ASKED QUESTIONS</div>
    <div style="height:0.18in;"></div>
    <h1 class="display" style="font-size:25pt; color:var(--navy);">Honest answers before you decide</h1>
    <div style="height:0.16in;"></div>
    {faq_rows}
  </div>
  {folio("Frequently Asked Questions", 11)}
</div>
''')

# =================================================================
# PAGE 12 — SUCCESS STORIES (placeholders)
# =================================================================
stories = [
    ("Church Name Placeholder", "Vision Campaign", "Went from a single sermon idea to a fully launched, churchwide campaign in six weeks."),
    ("Church Name Placeholder", "Stewardship Campaign", "Built a complete campaign blueprint their staff has now reused for two additional seasons."),
    ("Church Name Placeholder", "Family Campaign", "Launched with the highest first-time small group sign-up rate in the church's history."),
]
story_cards = "".join([f'''
    <div class="case-card">
      {photo("PHOTOGRAPHY PLACEHOLDER — PASTOR PORTRAIT", "height:1.6in;")}
      <div style="height:0.14in;"></div>
      <div style="font-family:'Playfair'; font-weight:700; font-size:13pt; color:var(--navy);">{name}</div>
      <div style="font-family:'Archivo'; font-weight:600; font-size:8.6pt; letter-spacing:0.1em; text-transform:uppercase; color:var(--gold); margin:0.05in 0 0.1in;">{tag}</div>
      <p style="font-family:'Inter'; font-size:9.2pt; line-height:1.5; color:var(--ink);">{result}</p>
    </div>''' for name, tag, result in stories])
add(f'''
<div class="page">
  <div class="frame">
    <div class="eyebrow">SUCCESS STORIES</div>
    <div style="height:0.18in;"></div>
    <h1 class="display" style="font-size:26pt; color:var(--navy);">What churches are building</h1>
    <div style="height:0.08in;"></div>
    <p style="font-family:'Inter'; font-size:9.6pt; color:var(--gray); font-style:italic; max-width:8in;">Stories below are shown in placeholder format, ready to be replaced with your church's own results.</p>
    <div style="height:0.22in;"></div>
    <div style="display:flex; gap:0.36in;">{story_cards}</div>
  </div>
  {folio("Success Stories", 12)}
</div>
''')

# =================================================================
# PAGE 13 — NEXT STEPS
# =================================================================
steps = [
    ("01", "Schedule a strategy conversation", "A complimentary conversation about your church's next campaign."),
    ("02", "Confirm your six-week schedule", "We'll find six weeks that work with your church's calendar."),
    ("03", "Begin Week One: Discover", "Your Campaign Builder Intensive begins."),
    ("04", "Walk away with a launch-ready blueprint", "Then choose your next step &mdash; launch on your own, or bring us alongside."),
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
    <div class="eyebrow">NEXT STEPS</div>
    <div style="height:0.2in;"></div>
    <h1 class="display" style="font-size:27pt; color:var(--navy);">How to begin</h1>
    <div style="height:0.22in;"></div>
    <div style="max-width:6.6in;">{step_rows}</div>
  </div>
  {folio("Next Steps", 13)}
</div>
''')

# =================================================================
# PAGE 14 — CALL TO ACTION / BACK COVER
# =================================================================
add(f'''
<div class="page navy">
  <div class="photo" style="position:absolute; inset:0; border-radius:0;">
    <div class="cap" style="right:0.9in; bottom:0.6in; left:auto; text-align:right; font-size:7.6pt;">PHOTOGRAPHY — PASTOR AND FAMILY, GOLDEN HOUR, CHURCH LOBBY IN SOFT FOCUS</div>
  </div>
  <div style="position:absolute; inset:0; background:linear-gradient(80deg, rgba(16,30,56,0.96) 0%, rgba(16,30,56,0.75) 46%, rgba(16,30,56,0.22) 100%);"></div>
  <div class="frame" style="display:flex; flex-direction:column; justify-content:center;">
    <div class="eyebrow">CALL TO ACTION</div>
    <div style="height:0.26in;"></div>
    <p class="lede" style="max-width:6.2in; font-size:12.5pt;">
      You don&rsquo;t need to start from scratch. You already possess years of God-given
      teaching. The Campaign Builder Intensive simply helps organize, expand, and multiply
      that message into a transformational journey that reaches people far beyond Sunday.
    </p>
    <div style="height:0.28in;"></div>
    <h1 class="display" style="font-size:24pt; color:#FBF8F1; max-width:6.6in;">Your greatest sermons deserve more than one Sunday.</h1>
    <div style="height:0.16in;"></div>
    <p class="lede" style="max-width:6in;">
      They deserve to become a movement that shapes lives, strengthens families, equips
      leaders, and leaves a legacy that outlives your ministry.
    </p>
    <div style="height:0.3in;"></div>
    <div style="width:34px; height:2px; background:#B98D3E;"></div>
    <div style="height:0.2in;"></div>
    <div style="font-family:'Archivo'; font-weight:500; font-size:10pt; letter-spacing:0.08em; color:rgba(251,248,241,0.75);">LIFETOGETHER.COM &nbsp;&middot;&nbsp; BRETT@LIFETOGETHER.COM</div>
  </div>
  {folio("Call to Action", 14)}
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
.track-chip{
  font-family:'Archivo'; font-weight:600; font-size:9pt; letter-spacing:0.1em; text-align:center;
  color:#D9B876; border:1px solid rgba(217,184,118,0.5); border-radius:6px;
  padding:0.12in 0.16in; line-height:1.5;
}
.track-card{ flex:1; }
.track-list{ list-style:none; padding:0; margin:0; }
.track-list li{
  font-family:'Inter'; font-size:8.8pt; color:var(--ink); line-height:1.5;
  padding:0.05in 0 0.05in 0.15in; position:relative; border-top:1px solid var(--line);
}
.track-list li::before{ content:'\\2013'; position:absolute; left:0; color:var(--gold); }
.build-grid{ display:grid; grid-template-columns:repeat(4, 1fr); gap:0.22in; }
.build-cell{
  font-family:'Playfair'; font-weight:700; font-size:12.5pt; color:var(--navy);
  background:var(--cream); border-left:3px solid var(--gold);
  padding:0.2in 0.22in; line-height:1.25;
}
.case-card{ flex:1; border-top:1px solid var(--line); padding-top:0.2in; }
.cmp-table{ display:flex; flex-direction:column; }
.cmp-head, .cmp-row{ display:flex; }
.cmp-head{ border-bottom:2px solid var(--navy); padding-bottom:0.14in; }
.cmp-row{ border-bottom:1px solid var(--line); padding:0.16in 0; }
.cmp-cell{ flex:1; font-family:'Inter'; font-size:9.8pt; color:var(--ink); padding-right:0.3in; }
.cmp-head .cmp-cell{ font-family:'Playfair'; font-weight:700; font-size:11.5pt; color:var(--navy); }
.cmp-label{ font-family:'Archivo'; font-weight:600; font-size:8.8pt; letter-spacing:0.1em; text-transform:uppercase; color:var(--gold); flex:0 0 1.2in; }
.cmp-head .cmp-label{ color:transparent; }
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

with open("/home/claude/build/intensive.html", "w") as f:
    f.write(html)

print("Pages:", len(PAGES))
