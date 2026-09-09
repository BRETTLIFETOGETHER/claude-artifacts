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
    ("Weekend Experience", ["Six-sermon series", "Pastor preparation guide", "Presentation slides", "Graphics", "Promotion"]),
    ("Daily Journey", ["30- or 40-day devotional", "Journal edition", "Family edition", "Student edition"]),
    ("Groups", ["Six-session curriculum", "Leader guide", "Discussion questions", "Video option"]),
    ("Adult Bible Fellowship", ["Expanded teacher guide", "Historical notes", "Maps & charts", "Master teaching manuscript"]),
    ("Churchwide Resources", ["Prayer guide", "Worship recommendations", "Campaign calendar", "Volunteer resources", "Celebration weekend", "Follow-up pathway"]),
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
* { box-sizing: border-box; }
html, body { margin: 0; padding: 0; }
body {
  font-family: 'Poppins', sans-serif;
  color: #2B2620;
  background: #FAF6EF;
}
.page {
  width: 8.5in;
  height: 11in;
  position: relative;
  page-break-after: always;
  overflow: hidden;
  padding: 0.85in 0.9in;
  background: #FAF6EF;
}
.page:last-child { page-break-after: auto; }

h1, h2, h3 { font-family: 'Lora', serif; margin: 0; }

.rule {
  height: 3px;
  width: 64px;
  background: #7A2E2E;
  margin: 18px 0 22px 0;
}
.rule.center { margin-left: auto; margin-right: auto; }
.gold { color: #B8892B; }
.maroon { color: #7A2E2E; }
.small-caps {
  text-transform: uppercase;
  letter-spacing: 2.5px;
  font-size: 11px;
  color: #B8892B;
  font-weight: 600;
}

/* COVER */
.cover { display: flex; flex-direction: column; justify-content: center; align-items: center; text-align: center; height: 100%; }
.cover .eyebrow { font-size: 13px; letter-spacing: 4px; text-transform: uppercase; color: #B8892B; font-weight: 600; margin-bottom: 26px; }
.cover h1 { font-size: 44px; color: #2B2620; line-height: 1.18; max-width: 5.6in; }
.cover .accent-word { color: #7A2E2E; }
.cover h2 { font-size: 17px; font-weight: 400; font-style: italic; color: #4A443B; margin-top: 22px; max-width: 5in; line-height: 1.5; }
.cover .bar { width: 90px; height: 3px; background: #7A2E2E; margin: 30px 0; }
.cover .taglines { font-family: 'Lora', serif; font-size: 15px; color: #5A5145; line-height: 2.1; }
.cover .footer-label { position: absolute; bottom: 0.85in; font-size: 11px; letter-spacing: 3px; text-transform: uppercase; color: #9C8F79; }

/* SECTION PAGES (legacy, founder, why) */
.section-page .eyebrow { font-size: 12px; letter-spacing: 3px; text-transform: uppercase; color: #B8892B; font-weight: 600; }
.section-page h1 { font-size: 30px; margin-top: 10px; color: #2B2620; line-height: 1.25; }
.section-page .lead {
  font-family: 'Lora', serif;
  font-style: italic;
  font-size: 19px;
  color: #4A443B;
  line-height: 1.6;
  margin: 26px 0 30px 0;
  border-left: 3px solid #7A2E2E;
  padding-left: 22px;
}
.section-page p { font-size: 13.5px; line-height: 1.85; color: #3C362E; margin: 0 0 14px 0; }
.section-page ul { margin: 0; padding-left: 20px; }
.section-page li { font-size: 13.5px; line-height: 1.9; color: #3C362E; }

.grid-2 { display: grid; grid-template-columns: 1fr 1fr; gap: 10px 30px; margin-top: 10px; }
.grid-item { font-size: 13px; padding: 10px 0; border-bottom: 1px solid #E6DCC8; color: #3C362E; }

/* CAMPAIGN PAGES */
.campaign-page { height: 100%; position: relative; }
.campaign-page .bignum {
  position: absolute;
  top: -0.25in;
  right: -0.1in;
  font-family: 'Lora', serif;
  font-size: 220px;
  color: #EFE5D2;
  font-weight: 700;
  z-index: 0;
  line-height: 1;
}
.campaign-page .content { position: relative; z-index: 1; }
.campaign-page .badge {
  display: inline-block;
  font-size: 11px;
  letter-spacing: 2px;
  text-transform: uppercase;
  color: #FAF6EF;
  background: #7A2E2E;
  padding: 6px 14px;
  border-radius: 2px;
  font-weight: 600;
}
.campaign-page h1 { font-size: 34px; margin-top: 16px; color: #2B2620; line-height: 1.2; max-width: 5.6in; }
.campaign-page .subtitle { font-family: 'Lora', serif; font-style: italic; font-size: 16px; color: #6B4A2E; margin-top: 10px; max-width: 5.6in; }
.campaign-page .tag { font-size: 12.5px; color: #6B6153; margin-top: 14px; max-width: 5.4in; line-height: 1.6; }
.campaign-page .weeks { margin-top: 34px; }
.week-row {
  display: flex;
  align-items: center;
  padding: 13px 0;
  border-bottom: 1px solid #E6DCC8;
}
.week-row .wk-num {
  font-family: 'Lora', serif;
  font-weight: 700;
  font-size: 15px;
  color: #7A2E2E;
  width: 78px;
  flex-shrink: 0;
  letter-spacing: 1px;
}
.week-row .wk-title { font-size: 14.5px; color: #2B2620; font-weight: 500; }

/* OUTPUT STACK PAGE */
.stack-page h1 { font-size: 30px; }
.stack-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 22px 34px; margin-top: 28px; }
.stack-card { border: 1px solid #E6DCC8; background: #FFFDF9; padding: 18px 20px; border-radius: 3px; }
.stack-card h3 { font-size: 15px; color: #7A2E2E; margin-bottom: 10px; }
.stack-card ul { margin: 0; padding-left: 16px; }
.stack-card li { font-size: 12px; line-height: 1.8; color: #3C362E; }

/* FUTURE PAGE */
.future-page h1 { font-size: 30px; }
.future-grid { display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 8px 22px; margin-top: 22px; }
.future-item { font-size: 12.5px; padding: 9px 0; border-bottom: 1px solid #E6DCC8; color: #3C362E; }
.vision-box {
  margin-top: 32px;
  background: #7A2E2E;
  color: #FAF6EF;
  padding: 26px 28px;
  border-radius: 3px;
}
.vision-box .small-caps { color: #E3C98A; }
.vision-box p { font-family: 'Lora', serif; font-style: italic; font-size: 15px; line-height: 1.7; margin: 10px 0 0 0; color: #FAF6EF; }

.pagenum { position: absolute; bottom: 0.5in; right: 0.9in; font-size: 10px; color: #A79A82; letter-spacing: 1px; }
.pagefoot { position: absolute; bottom: 0.5in; left: 0.9in; font-size: 10px; color: #A79A82; letter-spacing: 1px; text-transform: uppercase; }
"""

def week_rows(weeks):
    rows = ""
    for i, w in enumerate(weeks, start=1):
        rows += f'<div class="week-row"><div class="wk-num">Week {i:02d}</div><div class="wk-title">{w}</div></div>\n'
    return rows

def campaign_page(c, page_no):
    return f"""
<div class="page campaign-page">
  <div class="bignum">{c['num']}</div>
  <div class="content">
    <span class="badge">Campaign {c['num']}</span>
    <h1>{c['title']}</h1>
    <div class="subtitle">{c['subtitle']}</div>
    <div class="tag">{c['tag']}</div>
    <div class="weeks">
      {week_rows(c['weeks'])}
    </div>
  </div>
  <div class="pagefoot">LifeTogether Biblical Purpose Library</div>
  <div class="pagenum">{page_no:02d}</div>
</div>
"""

stack_cards = ""
for title, items in OUTPUT_STACK:
    lis = "".join(f"<li>{i}</li>" for i in items)
    stack_cards += f'<div class="stack-card"><h3>{title}</h3><ul>{lis}</ul></div>\n'

future_items = "".join(f'<div class="future-item">{e}</div>' for e in FUTURE_EDITIONS)

campaign_pages_html = "".join(campaign_page(c, i + 5) for i, c in enumerate(CAMPAIGNS))

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
  <h1>LifeTogether <span class="accent-word">Biblical Purpose</span> Library</h1>
  <div class="bar"></div>
  <h2>Six&nbsp;&mdash;&nbsp;now nine&nbsp;&mdash;&nbsp; churchwide campaigns built on the timeless foundations of the five biblical purposes.</h2>
  <div class="taglines">
    Helping Churches Go Deeper.<br>
    Helping Disciples Grow Stronger.<br>
    Helping Every Person Discover a Life That Matters.
  </div>
  <div class="footer-label">LifeTogether &middot; Discipleship Resources</div>
</div>

<!-- PAGE 2: LEGACY -->
<div class="page section-page">
  <div class="eyebrow">Our Foundation</div>
  <h1>Building on a Legacy of Faithfulness</h1>
  <div class="lead">
    For over 30 years, the five biblical purposes have helped shape thousands of churches and inspired more than 50 million readers around the world.
  </div>
  <p>LifeTogether builds on those timeless biblical foundations with a new generation of churchwide campaigns, devotionals, curriculum, classes, and discipleship experiences &mdash; designed to help churches go deeper, wider, and further in every purpose.</p>
  <p>Every campaign in this library carries that same DNA forward: biblically rooted, practically applied, and built for the whole church to walk through together.</p>
  <div class="pagefoot">LifeTogether Biblical Purpose Library</div>
  <div class="pagenum">02</div>
</div>

<!-- PAGE 3: FOUNDER -->
<div class="page section-page">
  <div class="eyebrow">Our Founder</div>
  <h1>A Story Rooted in Ministry</h1>
  <div class="lead">
    LifeTogether founder Brett Eastman served on the original Purpose Driven ministry team and authored and co-developed many of the original Purpose Driven small-group resources published by Zondervan.
  </div>
  <p>Today, LifeTogether is helping churches apply those same biblical foundations through a new generation of customizable campaigns, curriculum, and discipleship tools &mdash; for every age and stage of life.</p>
  <p>This library carries that history forward without standing still: it is a distinctly LifeTogether vision, broader in scope and built for the next generation of churches.</p>
  <div class="pagefoot">LifeTogether Biblical Purpose Library</div>
  <div class="pagenum">03</div>
</div>

<!-- PAGE 4: WHY THIS LIBRARY -->
<div class="page section-page">
  <div class="eyebrow">Why This Library</div>
  <h1>One Foundation, Every Format Your Church Needs</h1>
  <p>For more than three decades, the biblical purposes of worship, fellowship, discipleship, ministry, and mission have transformed churches around the world. LifeTogether expands those same biblical themes into a comprehensive discipleship library for today's church.</p>
  <div class="small-caps" style="margin-top:22px;">Every Series Includes</div>
  <div class="grid-2">
    <div class="grid-item">Weekend sermon outlines</div>
    <div class="grid-item">Six-session small-group curriculum</div>
    <div class="grid-item">Daily devotionals</div>
    <div class="grid-item">Adult Bible Fellowship edition</div>
    <div class="grid-item">Teaching notes</div>
    <div class="grid-item">Discussion guides</div>
    <div class="grid-item">Family applications</div>
    <div class="grid-item">Digital resources</div>
    <div class="grid-item">Campaign planning tools</div>
  </div>
  <div class="pagefoot">LifeTogether Biblical Purpose Library</div>
  <div class="pagenum">04</div>
</div>

{campaign_pages_html}

<!-- PAGE 14: EVERY CAMPAIGN INCLUDES -->
<div class="page stack-page">
  <div class="eyebrow">The Full Stack</div>
  <h1>Every Campaign Includes</h1>
  <p style="margin-top:10px;">A complete, ready-to-run output stack &mdash; so every campaign launches with everything your church needs, from the pulpit to the living room.</p>
  <div class="stack-grid">
    {stack_cards}
  </div>
  <div class="pagefoot">LifeTogether Biblical Purpose Library</div>
  <div class="pagenum">14</div>
</div>

<!-- PAGE 15: FUTURE LIBRARY -->
<div class="page future-page">
  <div class="eyebrow">What's Next</div>
  <h1>The Future Biblical Purpose Library</h1>
  <p style="margin-top:10px;">These nine campaigns become the foundation for dozens of specialized editions, each applying the same biblical framework to a specific audience or season of life.</p>
  <div class="future-grid">
    {future_items}
  </div>
  <div class="vision-box">
    <div class="small-caps">Strategic Vision</div>
    <p>A 30-volume Biblical Purpose Library &mdash; six core campaigns and specialized editions beneath each &mdash; sharing one theological backbone while serving every ministry context, for every age and stage of life.</p>
  </div>
  <div class="pagefoot">LifeTogether Biblical Purpose Library</div>
  <div class="pagenum">15</div>
</div>

</body>
</html>
"""

with open("/home/claude/masterlib/catalog.html", "w") as f:
    f.write(HTML)

print("HTML written.")
