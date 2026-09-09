# -*- coding: utf-8 -*-

CAMPAIGNS = [
    {
        "num": "01",
        "title": "A Life That Matters",
        "subtitle": "40 Days to Know God, Belong, Grow, Serve, Live Sent, and Multiply Your Life",
        "tag": "The flagship introduction to the Biblical Purpose Library. Perfect for churchwide campaigns.",
        "weeks": [
            "Created to Know God",
            "Designed to Belong",
            "Formed to Become Like Jesus",
            "Gifted to Serve",
            "Sent to Make a Difference",
            "Called to Multiply",
        ],
    },
    {
        "num": "02",
        "title": "Made for More",
        "subtitle": "Discover the Life God Designed You to Live",
        "tag": "Helping people move beyond success toward significance.",
        "weeks": [
            "More Than Existing",
            "Made for His Presence",
            "Made for His Family",
            "Made to Become",
            "Made to Contribute",
            "Made to Multiply",
        ],
    },
    {
        "num": "03",
        "title": "Your Life on Purpose",
        "subtitle": "Align Every Part of Your Life with What Matters Most",
        "tag": "Ideal for adults, young professionals, workplace groups, and life planning.",
        "weeks": [
            "Your Center",
            "Your People",
            "Your Formation",
            "Your Contribution",
            "Your Mission",
            "Your Legacy",
        ],
    },
    {
        "num": "04",
        "title": "Designed to Flourish",
        "subtitle": "Growing Spiritually, Relationally, Personally, and Purposefully",
        "tag": "Helping believers flourish in every area of life.",
        "weeks": [
            "Flourishing with God",
            "Flourishing Together",
            "Flourishing from Within",
            "Flourishing through Contribution",
            "Flourishing for Others",
            "Flourishing Across Generations",
        ],
    },
    {
        "num": "05",
        "title": "The Whole-Life Disciple",
        "subtitle": "Following Jesus in Every Role, Relationship, and Responsibility",
        "tag": "Helping believers integrate faith into every part of life.",
        "weeks": [
            "A Life of Worship",
            "A Life Together",
            "A Life Being Formed",
            "A Life of Service",
            "A Life on Mission",
            "A Life That Reproduces",
        ],
    },
    {
        "num": "06",
        "title": "Your Next Faithful Chapter",
        "subtitle": "Clarify Your Calling. Refocus Your Priorities. Multiply Your Impact.",
        "tag": "Especially designed for second-half adults, retirees, pastors, and legacy-minded leaders.",
        "weeks": [
            "Remember Your Story",
            "Recognize Your Design",
            "Renew Your Relationship with God",
            "Refocus Your Season",
            "Respond to Your Assignment",
            "Reproduce Your Wisdom",
        ],
    },
    {
        "num": "07",
        "title": "Living What Matters Most",
        "subtitle": "Six Biblical Priorities That Shape an Extraordinary Life",
        "tag": "Best for churchwide discipleship, membership, new believers, and annual vision emphasis.",
        "weeks": [
            "Love God First",
            "Love People Well",
            "Grow Every Day",
            "Serve with Joy",
            "Live Sent",
            "Leave a Legacy",
        ],
    },
    {
        "num": "08",
        "title": "Rooted",
        "subtitle": "Building a Faith That Lasts for Every Season of Life",
        "tag": "Best for spiritual formation, discipleship, new believers, and churches wanting stronger biblical foundations.",
        "weeks": [
            "Rooted in Christ",
            "Rooted in Scripture",
            "Rooted in Community",
            "Rooted in Character",
            "Rooted in Mission",
            "Rooted for the Future",
        ],
    },
    {
        "num": "09",
        "title": "Living Fully Alive",
        "subtitle": "Discovering the Life Jesus Came to Give",
        "tag": "Best for evangelism, churchwide renewal, Easter follow-up, community outreach, and spiritual growth.",
        "weeks": [
            "Alive in Christ",
            "Alive Together",
            "Alive in Truth",
            "Alive through Service",
            "Alive for Others",
            "Alive with Eternal Purpose",
        ],
    },
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
.headline { font-size: 58px; line-height: 1.06; color: #1D1D1F; max-width: 6.1in; }
.dark .headline { color: #FBFBFD; }
.subhead {
  font-size: 19px;
  font-weight: 400;
  color: #4A4A4E;
  line-height: 1.55;
  margin-top: 24px;
  max-width: 5.4in;
}
.dark .subhead { color: #C7C7CC; }

.pagefoot {
  position: absolute;
  bottom: 0.6in;
  left: 1.05in;
  font-size: 10px;
  letter-spacing: 2px;
  text-transform: uppercase;
  color: #A1A1A6;
}
.pagenum {
  position: absolute;
  bottom: 0.6in;
  right: 1.05in;
  font-size: 10px;
  color: #A1A1A6;
  letter-spacing: 1px;
}
.dark .pagefoot, .dark .pagenum { color: #6E6E73; }

/* COVER */
.cover { display: flex; flex-direction: column; justify-content: center; height: 100%; }
.cover .eyebrow { text-align: left; }
.cover .headline { font-size: 66px; max-width: 6.3in; }
.cover .taglines {
  margin-top: 40px;
  font-size: 19px;
  color: #4A4A4E;
  line-height: 1.9;
  font-weight: 400;
}
.cover .footnote {
  position: absolute;
  bottom: 0.9in;
  left: 1.05in;
  font-size: 12px;
  color: #A1A1A6;
  letter-spacing: 1px;
}

/* SIMPLE STATEMENT PAGES */
.statement-page { display: flex; flex-direction: column; justify-content: center; height: 100%; }
.statement-page p.body {
  font-size: 15px;
  color: #3A3A3C;
  line-height: 1.85;
  margin-top: 8px;
  max-width: 5.6in;
}

/* FEATURE GRID (why this library) */
.feature-grid {
  margin-top: 44px;
  columns: 2;
  column-gap: 40px;
}
.feature-item {
  break-inside: avoid;
  padding: 15px 0;
  border-top: 1px solid #D2D2D7;
  font-size: 14.5px;
  color: #1D1D1F;
  font-weight: 600;
}

/* CAMPAIGN PAGES */
.campaign-page { height: 100%; display: flex; flex-direction: column; justify-content: center; }
.campaign-page .eyebrow-row { display:flex; align-items:baseline; gap: 14px; }
.campaign-page .cnum { font-size: 13px; color: #A1A1A6; letter-spacing: 1px; }
.campaign-page .headline { font-size: 52px; margin-top: 18px; }
.campaign-page .subtitle { font-size: 20px; color: #6E6E73; font-weight: 400; margin-top: 16px; max-width: 5.6in; line-height: 1.45; }
.campaign-page .tag { font-size: 13.5px; color: #8E8E93; margin-top: 14px; max-width: 5.4in; }
.campaign-page .weeks { margin-top: 46px; }
.week-row {
  display: flex;
  align-items: baseline;
  padding: 14px 0;
  border-top: 1px solid #D2D2D7;
}
.week-row:last-child { border-bottom: 1px solid #D2D2D7; }
.week-row .wk-num { font-size: 13px; color: #8B1E3F; font-weight: 700; width: 90px; flex-shrink: 0; letter-spacing: 0.5px; }
.week-row .wk-title { font-size: 16px; color: #1D1D1F; font-weight: 500; }

/* OUTPUT STACK PAGE */
.stack-list { margin-top: 44px; }
.stack-row { padding: 22px 0; border-top: 1px solid #D2D2D7; }
.stack-row:last-child { border-bottom: 1px solid #D2D2D7; }
.stack-row .stack-name { font-size: 19px; font-weight: 700; color: #1D1D1F; }
.stack-row .stack-desc { font-size: 13.5px; color: #6E6E73; margin-top: 6px; max-width: 5.6in; line-height: 1.6; }

/* FUTURE PAGE */
.future-grid { margin-top: 40px; columns: 3; column-gap: 26px; }
.future-item { break-inside: avoid; font-size: 12.5px; color: #3A3A3C; padding: 9px 0; border-top: 1px solid #D2D2D7; }
.dark .future-item { color: #E5E5E7; border-top: 1px solid #3A3A3C; }
.dark .future-item { color: #E5E5E7; border-top: 1px solid #3A3A3C; }

.vision {
  margin-top: 46px;
  font-size: 27px;
  font-weight: 700;
  color: #1D1D1F;
  line-height: 1.4;
  max-width: 6in;
}
.vision .accent { color: #8B1E3F; }
"""

def week_rows(weeks):
    rows = ""
    for i, w in enumerate(weeks, start=1):
        rows += f'<div class="week-row"><div class="wk-num">Week {i:02d}</div><div class="wk-title">{w}</div></div>\n'
    return rows

def campaign_page(c, page_no):
    return f"""
<div class="page campaign-page">
  <div class="eyebrow-row">
    <span class="eyebrow" style="margin-bottom:0;">Campaign {c['num']}</span>
    <span class="cnum">of 09</span>
  </div>
  <h1 class="headline">{c['title']}</h1>
  <div class="subtitle">{c['subtitle']}</div>
  <div class="tag">{c['tag']}</div>
  <div class="weeks">
    {week_rows(c['weeks'])}
  </div>
  <div class="pagefoot">LifeTogether</div>
  <div class="pagenum">{page_no:02d}</div>
</div>
"""

feature_items = "".join(
    f'<div class="feature-item">{t}</div>'
    for t in [
        "Weekend sermon outlines", "Six-session small-group curriculum",
        "Daily devotionals", "Adult Bible Fellowship edition",
        "Teaching notes", "Discussion guides",
        "Family applications", "Digital resources",
        "Campaign planning tools",
    ]
)

stack_rows = "".join(
    f'<div class="stack-row"><div class="stack-name">{name}</div><div class="stack-desc">{desc}</div></div>\n'
    for name, desc in OUTPUT_STACK
)

future_items = "".join(f'<div class="future-item">{e}</div>' for e in FUTURE_EDITIONS)

campaign_pages_html = "".join(campaign_page(c, i + 6) for i, c in enumerate(CAMPAIGNS))

HTML = f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>{CSS}</style>
</head>
<body>

<!-- PAGE 1: COVER -->
<div class="page cover">
  <div class="eyebrow">Master Library Catalog</div>
  <h1 class="headline">LifeTogether<br>Biblical Purpose<br>Library</h1>
  <div class="taglines">
    Helping churches go deeper.<br>
    Helping disciples grow stronger.<br>
    Helping every person discover a life that matters.
  </div>
  <div class="footnote">LifeTogether &middot; Discipleship Resources</div>
</div>

<!-- PAGE 2: LEGACY -->
<div class="page statement-page">
  <div class="eyebrow">Our Foundation</div>
  <h1 class="headline">Thirty years.<br>Fifty million readers.<br>One foundation.</h1>
  <p class="body">For over 30 years, the five biblical purposes have helped shape thousands of churches and inspired more than 50 million readers around the world. LifeTogether builds on those timeless biblical foundations with a new generation of churchwide campaigns, devotionals, curriculum, classes, and discipleship experiences &mdash; designed to help churches go deeper, wider, and further in every purpose.</p>
  <div class="pagefoot">LifeTogether</div>
  <div class="pagenum">02</div>
</div>

<!-- PAGE 3: FOUNDER -->
<div class="page statement-page">
  <div class="eyebrow">Our Founder</div>
  <h1 class="headline">Built by someone<br>who helped build<br>the original.</h1>
  <p class="body">LifeTogether founder Brett Eastman served on the original Purpose Driven ministry team and authored and co-developed many of the original Purpose Driven small-group resources published by Zondervan. Today, LifeTogether is helping churches apply those same biblical foundations through a new generation of customizable campaigns, curriculum, and discipleship tools &mdash; for every age and stage of life.</p>
  <div class="pagefoot">LifeTogether</div>
  <div class="pagenum">03</div>
</div>

<!-- PAGE 4: WHY THIS LIBRARY (statement only) -->
<div class="page statement-page">
  <div class="eyebrow">Why This Library</div>
  <h1 class="headline">One foundation.<br>Every format your<br>church needs.</h1>
  <p class="body">For more than three decades, the biblical purposes of worship, fellowship, discipleship, ministry, and mission have transformed churches around the world. LifeTogether expands those same biblical themes into a comprehensive discipleship library for today's church.</p>
  <div class="pagefoot">LifeTogether</div>
  <div class="pagenum">04</div>
</div>

<!-- PAGE 5: EVERY SERIES INCLUDES (list, own page) -->
<div class="page statement-page">
  <div class="eyebrow">In Every Series</div>
  <h1 class="headline">Nine things,<br>every time.</h1>
  <div class="feature-grid" style="margin-top:56px;">
    {feature_items}
  </div>
  <div class="pagefoot">LifeTogether</div>
  <div class="pagenum">05</div>
</div>

{campaign_pages_html}

<!-- PAGE 15: EVERY CAMPAIGN INCLUDES -->
<div class="page statement-page">
  <div class="eyebrow">The Full Stack</div>
  <h1 class="headline">Everything your<br>church needs.<br>Every campaign.</h1>
  <div class="stack-list">
    {stack_rows}
  </div>
  <div class="pagefoot">LifeTogether</div>
  <div class="pagenum">15</div>
</div>

<!-- PAGE 16: WHAT'S NEXT (statement only) -->
<div class="page statement-page dark">
  <div class="eyebrow">What's Next</div>
  <h1 class="headline">Nine campaigns.<br>Dozens of futures.</h1>
  <p class="body" style="color:#C7C7CC;">These nine campaigns become the foundation for dozens of specialized editions, each applying the same biblical framework to a specific audience or season of life.</p>
  <div class="pagefoot">LifeTogether</div>
  <div class="pagenum">16</div>
</div>

<!-- PAGE 17: FUTURE EDITIONS LIST -->
<div class="page statement-page dark">
  <div class="eyebrow">Specialized Editions</div>
  <h1 class="headline" style="font-size:44px;">Fifteen editions.<br>One framework.</h1>
  <div class="future-grid" style="margin-top:52px;">
    {future_items}
  </div>
  <div class="pagefoot">LifeTogether</div>
  <div class="pagenum">17</div>
</div>

<!-- PAGE 18: CLOSING VISION -->
<div class="page statement-page dark">
  <div class="eyebrow">The Vision</div>
  <div class="vision" style="font-size:40px; max-width:6.2in;">A <span class="accent">30-volume</span> Biblical Purpose Library &mdash; one theological backbone, serving every ministry context, for every age and stage of life.</div>
  <div class="pagefoot">LifeTogether</div>
  <div class="pagenum">18</div>
</div>

</body>
</html>
"""

with open("/home/claude/masterlib/brochure.html", "w") as f:
    f.write(HTML)

print("HTML written.")
