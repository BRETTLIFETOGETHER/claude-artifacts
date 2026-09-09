# -*- coding: utf-8 -*-

CAMPAIGNS = [
    ("01", "A Life That Matters", "40 Days to Know God, Belong, Grow, Serve, Live Sent, and Multiply Your Life"),
    ("02", "Made for More", "Discover the Life God Designed You to Live"),
    ("03", "Your Life on Purpose", "Align Every Part of Your Life with What Matters Most"),
    ("04", "Designed to Flourish", "Growing Spiritually, Relationally, Personally, and Purposefully"),
    ("05", "The Whole-Life Disciple", "Following Jesus in Every Role, Relationship, and Responsibility"),
    ("06", "Your Next Faithful Chapter", "Clarify Your Calling. Refocus Your Priorities. Multiply Your Impact."),
    ("07", "Living What Matters Most", "Six Biblical Priorities That Shape an Extraordinary Life"),
    ("08", "Rooted", "Building a Faith That Lasts for Every Season of Life"),
    ("09", "Living Fully Alive", "Discovering the Life Jesus Came to Give"),
]

OUTPUT_STACK = [
    ("Weekend Experience", "Six-sermon series, pastor prep guide, presentation slides, graphics, promotion."),
    ("Daily Journey", "30- or 40-day devotional, journal edition, family edition, student edition."),
    ("Groups", "Six-session curriculum, leader guide, discussion questions, video option."),
    ("Adult Bible Fellowship", "Expanded teacher guide, historical notes, maps, charts, master teaching manuscript."),
    ("Churchwide Resources", "Prayer guide, worship recommendations, campaign calendar, volunteer resources, celebration weekend, follow-up pathway."),
]

FUTURE_EDITIONS = [
    "Men's Purpose Journey", "Women's Purpose Journey", "Student Purpose Journey",
    "Young Adult Purpose Journey", "Parenting with Purpose", "Marriage on Purpose",
    "Financial Purpose", "Workplace Purpose", "Retirement with Purpose",
    "Legacy Purpose", "Church Leadership Purpose", "Pastor Purpose",
    "Mission on Purpose", "Community Impact Purpose", "Family Legacy Purpose",
]

CSS = """
@page { size: 8.5in 11in; margin: 0; }
* { box-sizing: border-box; -webkit-font-smoothing: antialiased; }
html, body { margin: 0; padding: 0; }
body {
  font-family: 'TeX Gyre Heros', Helvetica, Arial, sans-serif;
  color: #1D1D1F;
  background: #FBFBFD;
}
.page {
  width: 8.5in;
  height: 11in;
  position: relative;
  page-break-after: always;
  overflow: hidden;
  padding: 1.15in 1.05in;
  background: #FBFBFD;
}
.page:last-child { page-break-after: auto; }
.page.dark { background: #1D1D1F; color: #FBFBFD; }

.eyebrow {
  font-size: 12px;
  letter-spacing: 3px;
  text-transform: uppercase;
  color: #8B1E3F;
  font-weight: 700;
  margin-bottom: 22px;
}
.dark .eyebrow { color: #E3A6B8; }

h1 { font-weight: 700; margin: 0; letter-spacing: -0.5px; }
.headline { font-size: 54px; line-height: 1.08; color: #1D1D1F; max-width: 6.2in; }
.dark .headline { color: #FBFBFD; }
.subhead {
  font-size: 17px;
  font-weight: 400;
  color: #4A4A4E;
  line-height: 1.6;
  margin-top: 22px;
  max-width: 5.6in;
}
.dark .subhead { color: #C7C7CC; }

.pagefoot {
  position: absolute; bottom: 0.6in; left: 1.05in;
  font-size: 10px; letter-spacing: 2px; text-transform: uppercase; color: #A1A1A6;
}
.pagenum {
  position: absolute; bottom: 0.6in; right: 1.05in;
  font-size: 10px; color: #A1A1A6; letter-spacing: 1px;
}
.dark .pagefoot, .dark .pagenum { color: #6E6E73; }

.page-body { height: 100%; display: flex; flex-direction: column; justify-content: center; }

/* COVER */
.cover .headline { font-size: 62px; }
.cover .taglines { margin-top: 36px; font-size: 18px; color: #4A4A4E; line-height: 1.9; }
.cover .footnote { position: absolute; bottom: 0.9in; left: 1.05in; font-size: 12px; color: #A1A1A6; letter-spacing: 1px; }

/* GENERIC LIST ROW */
.list { margin-top: 40px; }
.row { padding: 16px 0; border-top: 1px solid #D2D2D7; }
.row:last-child { border-bottom: 1px solid #D2D2D7; }
.dark .row { border-top: 1px solid #3A3A3C; }
.dark .row:last-child { border-bottom: 1px solid #3A3A3C; }

.row-title { font-size: 17px; font-weight: 700; color: #1D1D1F; }
.dark .row-title { color: #FBFBFD; }
.row-desc { font-size: 12.5px; color: #6E6E73; margin-top: 5px; max-width: 5.6in; line-height: 1.55; }
.dark .row-desc { color: #A1A1A6; }

.row.compact { display: flex; align-items: baseline; gap: 16px; padding: 12px 0; }
.row.compact .cnum { font-size: 12px; color: #8B1E3F; font-weight: 700; width: 26px; flex-shrink: 0; }
.dark .row.compact .cnum { color: #E3A6B8; }
.row.compact .row-title { font-size: 15.5px; }
.row.compact .row-desc { margin-top: 2px; font-size: 12px; }

/* FEATURE GRID */
.feature-grid { margin-top: 30px; columns: 2; column-gap: 40px; }
.feature-item { break-inside: avoid; padding: 13px 0; border-top: 1px solid #D2D2D7; font-size: 13.5px; color: #1D1D1F; font-weight: 600; }

/* FUTURE GRID */
.future-grid { margin-top: 28px; columns: 3; column-gap: 24px; }
.future-item { break-inside: avoid; font-size: 12px; color: #E5E5E7; padding: 8px 0; border-top: 1px solid #3A3A3C; }

.vision { margin-top: 40px; font-size: 26px; font-weight: 700; line-height: 1.4; max-width: 6.1in; color: #FBFBFD; }
.vision .accent { color: #E3A6B8; }
"""

def row(title, desc, compact=False, num=None):
    if compact:
        return f'<div class="row compact"><div class="cnum">{num}</div><div><div class="row-title">{title}</div><div class="row-desc">{desc}</div></div></div>\n'
    return f'<div class="row"><div class="row-title">{title}</div><div class="row-desc">{desc}</div></div>\n'

campaign_rows = "".join(row(t, s, compact=True, num=n) for n, t, s in CAMPAIGNS)
stack_rows = "".join(row(n, d) for n, d in OUTPUT_STACK)
feature_items = "".join(
    f'<div class="feature-item">{t}</div>' for t in [
        "Weekend sermon outlines", "Six-session small-group curriculum",
        "Daily devotionals", "Adult Bible Fellowship edition",
        "Teaching notes", "Discussion guides",
        "Family applications", "Digital resources", "Campaign planning tools",
    ]
)
future_items = "".join(f'<div class="future-item">{e}</div>' for e in FUTURE_EDITIONS)

HTML = f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>{CSS}</style>
</head>
<body>

<!-- PAGE 1: COVER -->
<div class="page cover page-body">
  <div class="eyebrow">Master Library Overview</div>
  <h1 class="headline">LifeTogether<br>Biblical Purpose<br>Library</h1>
  <div class="taglines">
    Helping churches go deeper.<br>
    Helping disciples grow stronger.<br>
    Helping every person discover a life that matters.
  </div>
  <div class="footnote">LifeTogether &middot; Discipleship Resources</div>
</div>

<!-- PAGE 2: FOUNDATION (legacy + founder combined) -->
<div class="page page-body">
  <div class="eyebrow">Our Foundation</div>
  <h1 class="headline">Thirty years.<br>Fifty million readers.<br>One legacy.</h1>
  <div class="subhead">
    For over 30 years, the five biblical purposes have helped shape thousands of churches and inspired more than 50 million readers around the world. LifeTogether builds on those timeless biblical foundations with a new generation of churchwide campaigns, devotionals, curriculum, classes, and discipleship experiences.
    <br><br>
    Founder Brett Eastman served on the original Purpose Driven ministry team and co-developed many of its original small-group resources published by Zondervan. Today, LifeTogether carries that legacy forward &mdash; for every age and stage of life.
  </div>
  <div class="pagefoot">LifeTogether</div>
  <div class="pagenum">02</div>
</div>

<!-- PAGE 3: WHY THIS LIBRARY -->
<div class="page page-body">
  <div class="eyebrow">Why This Library</div>
  <h1 class="headline">One foundation.<br>Every format your<br>church needs.</h1>
  <div class="subhead">LifeTogether expands the five biblical purposes into a comprehensive discipleship library for today's church. Every series includes:</div>
  <div class="feature-grid">
    {feature_items}
  </div>
  <div class="pagefoot">LifeTogether</div>
  <div class="pagenum">03</div>
</div>

<!-- PAGE 4: NINE CAMPAIGNS OVERVIEW -->
<div class="page page-body">
  <div class="eyebrow">The Campaigns</div>
  <h1 class="headline">Nine campaigns.<br>One framework.</h1>
  <div class="subhead">Each campaign is a complete 40-day churchwide journey &mdash; six weeks, one framework, built to be led together.</div>
  <div class="list">
    {campaign_rows}
  </div>
  <div class="pagefoot">LifeTogether</div>
  <div class="pagenum">04</div>
</div>

<!-- PAGE 5: EVERY CAMPAIGN INCLUDES -->
<div class="page page-body">
  <div class="eyebrow">The Full Stack</div>
  <h1 class="headline">Everything your<br>church needs.<br>Every campaign.</h1>
  <div class="list">
    {stack_rows}
  </div>
  <div class="pagefoot">LifeTogether</div>
  <div class="pagenum">05</div>
</div>

<!-- PAGE 6: FUTURE LIBRARY + VISION (dark, combined) -->
<div class="page page-body dark">
  <div class="eyebrow">What's Next</div>
  <h1 class="headline">Nine campaigns.<br>Dozens of futures.</h1>
  <div class="subhead" style="color:#C7C7CC;">These nine campaigns become the foundation for dozens of specialized editions &mdash; each applying the same framework to a specific audience or season of life.</div>
  <div class="future-grid">
    {future_items}
  </div>
  <div class="vision">A <span class="accent">30-volume</span> Biblical Purpose Library &mdash; one theological backbone, serving every ministry context.</div>
  <div class="pagefoot">LifeTogether</div>
  <div class="pagenum">06</div>
</div>

</body>
</html>
"""

with open("/home/claude/masterlib/overview.html", "w") as f:
    f.write(HTML)

print("HTML written.")
