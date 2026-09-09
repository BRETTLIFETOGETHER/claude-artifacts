# -*- coding: utf-8 -*-
import os
OUT='/home/claude/site/out'

HEAD = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} — 40 Day Campaigns</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Hanken+Grotesk:wght@500;600;700;800;900&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>
:root{{--ink:#16161D;--ink-2:#3A3A45;--dim:#5E5E6B;--faint:#8A8A98;--orange:#F26C1E;--orange-d:#DE5E12;
--gold:#E4AC43;--gold-d:#C68E2A;--line:#ECE9F2;--card:#F5F3F9;--white:#FFFFFF;
--c1:#7B5FE0;--c2:#4F86E0;--c3:#C8484C;--c4:#E0703F;--c5:#36A85E;--c6:#E8A52E;--c7:#16A88F;--c8:#E2542F;--c9:#5A6B8C;--c10:#C99A3C;}}
*{{box-sizing:border-box;}}
body{{margin:0;color:var(--ink);font-family:'Inter',sans-serif;-webkit-font-smoothing:antialiased;line-height:1.55;
background:radial-gradient(46% 40% at 92% 0%, rgba(225,216,250,.7), transparent 60%),
radial-gradient(40% 36% at 99% 18%, rgba(252,222,214,.55), transparent 60%),#fff;background-attachment:fixed;}}
a{{text-decoration:none;color:inherit;}}
h1,h2,h3,h4{{font-family:'Hanken Grotesk',sans-serif;margin:0;letter-spacing:-.02em;}}
.wrap{{max-width:1180px;margin:0 auto;padding:0 28px;}}
.btn{{display:inline-flex;align-items:center;gap:8px;font-family:'Hanken Grotesk';font-weight:700;font-size:14px;
padding:11px 18px;border-radius:999px;border:none;cursor:pointer;transition:.16s;white-space:nowrap;}}
.btn-dark{{background:var(--ink);color:#fff;}}.btn-dark:hover{{background:#000;}}
.btn-orange{{background:var(--orange);color:#fff;}}.btn-orange:hover{{background:var(--orange-d);}}
.btn-white{{background:#fff;color:var(--ink);border:1px solid var(--line);}}.btn-white:hover{{box-shadow:0 8px 20px -12px rgba(0,0,0,.25);}}
.navwrap{{position:sticky;top:0;z-index:60;padding:16px 16px 0;}}
.nav{{max-width:1180px;margin:0 auto;display:flex;align-items:center;gap:20px;background:rgba(255,255,255,.72);
backdrop-filter:blur(16px);border:1px solid rgba(22,22,29,.07);border-radius:999px;padding:9px 12px 9px 18px;
box-shadow:0 12px 32px -18px rgba(40,30,80,.32);}}
.brand{{display:flex;align-items:center;gap:10px;}}
.mark{{width:36px;height:36px;border-radius:10px;position:relative;background:linear-gradient(135deg,var(--gold),var(--gold-d));
display:flex;align-items:center;justify-content:center;box-shadow:0 5px 13px -5px rgba(228,172,67,.7);}}
.mark b{{font-family:'Hanken Grotesk';font-weight:900;font-size:14px;color:#26190A;}}
.mark i{{position:absolute;right:-4px;bottom:-4px;width:15px;height:15px;border-radius:5px;background:var(--orange);
border:2.5px solid #fff;display:flex;align-items:center;justify-content:center;}}
.mark i::after{{content:"";border-left:5px solid #fff;border-top:3px solid transparent;border-bottom:3px solid transparent;margin-left:1px;}}
.brand .a{{font-family:'Hanken Grotesk';font-weight:800;font-size:15.5px;}}.brand .a span{{color:var(--gold-d);}}
.nlinks{{display:flex;gap:22px;margin-left:6px;}}
.nlinks a{{font-family:'Hanken Grotesk';font-weight:700;font-size:13px;letter-spacing:.03em;text-transform:uppercase;color:var(--ink-2);}}
.nlinks a.on{{color:var(--orange);}}
.nright{{margin-left:auto;display:flex;gap:9px;align-items:center;}}
.head{{padding:56px 0 22px;}}
.head .eb{{font-family:'Hanken Grotesk';font-weight:800;font-size:13px;letter-spacing:.14em;text-transform:uppercase;color:var(--orange);}}
.head h1{{font-weight:900;font-size:clamp(32px,4.4vw,50px);line-height:1.05;margin:12px 0 12px;}}
.head p{{font-size:17px;color:var(--ink-2);max-width:62ch;margin:0;}}
.section{{padding:38px 0;}}
.section h2{{font-weight:900;font-size:clamp(23px,3vw,30px);margin-bottom:6px;}}
.section .sd{{font-size:15px;color:var(--dim);margin-bottom:22px;max-width:66ch;}}
.cards{{display:grid;gap:16px;}}
.card{{background:#fff;border:1px solid var(--line);border-radius:18px;padding:22px;}}
.card h3{{font-weight:800;font-size:17px;margin-bottom:6px;}}
.card p{{font-size:14px;color:var(--ink-2);margin:0;}}
.num{{font-family:'Hanken Grotesk';font-weight:900;font-size:13px;color:#fff;background:var(--orange);width:26px;height:26px;
border-radius:8px;display:inline-flex;align-items:center;justify-content:center;margin-bottom:12px;}}
.ii{{width:40px;height:40px;border-radius:12px;background:#FBEFE4;color:var(--orange-d);display:flex;align-items:center;justify-content:center;margin-bottom:12px;}}
footer{{background:var(--ink);color:#fff;margin-top:70px;}}
footer .wrap{{display:flex;align-items:center;gap:26px;flex-wrap:wrap;padding:34px 28px;}}
.fnav{{display:flex;gap:20px;flex-wrap:wrap;margin-left:auto;}}
.fnav a{{font-family:'Hanken Grotesk';font-weight:700;font-size:13px;color:rgba(255,255,255,.75);}}
.fnav a:hover{{color:#fff;}}
.fbar{{border-top:1px solid rgba(255,255,255,.12);padding:16px 28px;display:flex;justify-content:space-between;gap:14px;flex-wrap:wrap;
font-size:12px;color:rgba(255,255,255,.55);max-width:1180px;margin:0 auto;}}
.fbar a{{color:rgba(255,255,255,.7);}}
{extra_css}
@media(max-width:760px){{.nlinks{{display:none;}}}}
@media(prefers-reduced-motion:reduce){{*{{transition:none!important;}}}}
:focus-visible{{outline:3px solid var(--orange);outline-offset:2px;border-radius:6px;}}
</style>
</head>
<body>
<div class="navwrap"><nav class="nav">
  <a class="brand" href="index.html"><span class="mark"><b>40</b><i></i></span><span class="a">40 Day <span>Campaigns</span></span></a>
  <div class="nlinks">
    <a href="browse.html"{on_browse}>Campaigns</a><a href="finder.html"{on_finder}>Finder</a>
    <a href="how-it-works.html"{on_how}>How It Works</a><a href="pricing.html"{on_pricing}>Pricing</a>
    <a href="churches.html"{on_church}>For Churches</a>
  </div>
  <div class="nright"><a class="btn btn-white" href="signin.html">Sign in</a><a class="btn btn-orange" href="get-access.html">Get access</a></div>
</nav></div>
"""

FOOT = """
<footer>
  <div class="wrap">
    <a class="brand" href="index.html"><span class="mark"><b>40</b><i></i></span><span class="a" style="color:#fff">40 Day <span style="color:var(--gold)">Campaigns</span></span></a>
    <div class="fnav">
      <a href="browse.html">Browse</a><a href="finder.html">Finder</a><a href="how-it-works.html">How It Works</a>
      <a href="pricing.html">Pricing</a><a href="churches.html">For Churches</a><a href="faq.html">FAQ</a>
      <a href="about.html">About</a><a href="contact.html">Contact</a>
    </div>
  </div>
  <div class="fbar"><span>© 2026 40daycampaigns.com · A Lifetogether ministry · Built in the Purpose Driven tradition</span>
  <span>1,000+ campaigns · 50 themes · 10 categories · NIV throughout · <a href="contact.html">Say hello</a></span></div>
</footer>
</body>
</html>"""

def shell(title, on, extra_css=''):
    flags = {k: '' for k in ['on_browse','on_finder','on_how','on_pricing','on_church']}
    if on: flags['on_'+on] = ' class="on"'
    return HEAD.format(title=title, extra_css=extra_css, **flags)

ARROW='<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.6"><path d="M5 12h14M13 6l6 6-6 6"/></svg>'

# ---------------- HOW IT WORKS ----------------
hiw_css = """.grid3{grid-template-columns:repeat(3,1fr);} .grid4{grid-template-columns:repeat(4,1fr);} .grid5{grid-template-columns:repeat(5,1fr);}
@media(max-width:900px){.grid3,.grid4,.grid5{grid-template-columns:1fr 1fr;}} @media(max-width:560px){.grid3,.grid4,.grid5{grid-template-columns:1fr;}}
.fmtcard b{display:block;font-family:'Hanken Grotesk';font-weight:900;font-size:22px;color:var(--orange);}
.exp{display:flex;gap:14px;align-items:flex-start;}
"""
how = shell('How It Works','how',hiw_css) + """
<div class="wrap">
<header class="head"><span class="eb">How it works</span>
<h1>One campaign. Your whole church, moving together.</h1>
<p>A churchwide campaign aligns the weekend sermon, the small-group study, and every member's daily devotional around one theme for a season — so Sunday doesn't end on Sunday. Here's the process from first click to Celebration Sunday.</p>
</header>

<section class="section" id="what"><h2>What is a campaign?</h2>
<div class="sd">Every campaign in the library is one theme delivered three ways at once, so the whole church hears one message all week long.</div>
<div class="cards grid3">
<div class="card"><div class="ii">📖</div><h3>Daily devotional</h3><p>A short daily reading — Scripture (NIV), reflection, prayer, and one next step — for every member, every day of the campaign.</p></div>
<div class="card"><div class="ii">🪑</div><h3>Small-group study</h3><p>Six leader-led sessions with discussion questions, so groups process together what the church is reading individually.</p></div>
<div class="card"><div class="ii">🎤</div><h3>Sermon series</h3><p>Six aligned message outlines for the weekend, so the pulpit, the living room, and the quiet time all point the same direction.</p></div>
</div></section>

<section class="section" id="process"><h2>The campaign process</h2>
<div class="sd">Most churches run this in about six weeks of prep plus the campaign itself. Nothing here requires a big staff — a solo pastor with a volunteer team can do all of it.</div>
<div class="cards grid5">
<div class="card"><span class="num">1</span><h3>Pick</h3><p>Browse 1,000+ campaigns across 50 themes, or let the <a href="finder.html" style="color:var(--orange);font-weight:600">Campaign Finder</a> recommend three matches in six questions.</p></div>
<div class="card"><span class="num">2</span><h3>Choose a format</h3><p>Every campaign runs as a 7-Day, 21-Day, 30-Day, or 40-Day journey, or a 6-Week group series. Pick what your church can commit to.</p></div>
<div class="card"><span class="num">3</span><h3>Customize</h3><p>Add your church name, adjust wording, or order a pastor-branded edition. Export to print PDF, Canva, or Google Docs.</p></div>
<div class="card"><span class="num">4</span><h3>Launch</h3><p>Use the launch kit — graphics, announcement scripts, leader training, and a group sign-up push — to start everyone on Day 1 together.</p></div>
<div class="card"><span class="num">5</span><h3>Celebrate</h3><p>End with Celebration Sunday: stories, baptisms, next steps — and a clear on-ramp to your next season.</p></div>
</div></section>

<section class="section" id="formats"><h2>Choosing a format</h2>
<div class="sd">Same theme, five lengths. A rule of thumb: first campaign ever? Start with 21 days. Churchwide movement with sermon alignment? That's the classic 40.</div>
<div class="cards grid5">
<div class="card fmtcard"><b>7-Day</b><h3>The spark</h3><p>A high-energy week — great for New Year prayer, Holy Week, or testing the waters.</p></div>
<div class="card fmtcard"><b>21-Day</b><h3>The habit</h3><p>Three weeks is long enough to form a daily rhythm without exhausting volunteers.</p></div>
<div class="card fmtcard"><b>30-Day</b><h3>The month</h3><p>A clean calendar month — ideal for themed months like generosity in November.</p></div>
<div class="card fmtcard"><b>40-Day</b><h3>The movement</h3><p>The full churchwide journey with six aligned sermons. Our flagship format.</p></div>
<div class="card fmtcard"><b>6-Week</b><h3>The group series</h3><p>Leader-led curriculum for a small-group semester, with or without the daily devotional.</p></div>
</div></section>

<section class="section" id="included"><h2>What's included in every campaign</h2>
<div class="sd">One license covers your whole congregation — every format, every asset, print rights included.</div>
<div class="cards grid4">
<div class="card"><h3>Daily devotional</h3><p>Every day of the journey: Scripture (NIV), a pastoral reflection, a prayer, one question, and one small step.</p></div>
<div class="card"><h3>6-session group study</h3><p>Leader guides, discussion questions, and icebreakers — written for first-time hosts, not seminary grads.</p></div>
<div class="card"><h3>6 sermon outlines</h3><p>Weekend message outlines aligned to each week of the campaign, ready to make your own.</p></div>
<div class="card"><h3>Launch kit</h3><p>Promo graphics, announcement scripts, email/text sequences, leader-training video outline, and a Celebration Sunday guide.</p></div>
</div></section>

<section class="section" id="exports"><h2>Editing & exports</h2>
<div class="sd">Everything is yours to adapt. Three ways to take a campaign and make it your church's own:</div>
<div class="cards grid3">
<div class="card exp"><div><h3>Print-ready PDF</h3><p>Download the devotional as a formatted booklet (Letter or A5), ready for your local print shop. A free sample is on every campaign page.</p></div></div>
<div class="card exp"><div><h3>Canva template</h3><p>Import the PDF into Canva today to restyle with your church's brand. One-click "Open in Canva" is in development and included free at platform launch.</p></div></div>
<div class="card exp"><div><h3>Google Docs / Word</h3><p>All-Access members receive fully editable copies — adapt wording, add local stories, or translate. Delivered with your subscription.</p></div></div>
</div>
<div style="margin-top:22px;display:flex;gap:12px;flex-wrap:wrap;">
<a class="btn btn-orange" href="browse.html">Browse the library """+ARROW+"""</a>
<a class="btn btn-white" href="pricing.html">See pricing</a>
<a class="btn btn-white" href="faq.html">Read the FAQ</a>
</div></section>
</div>
""" + FOOT

# ---------------- PRICING ----------------
pr_css = """.tiers{display:grid;grid-template-columns:1fr 1.15fr 1fr;gap:18px;align-items:start;}
@media(max-width:900px){.tiers{grid-template-columns:1fr;}}
.tier{background:#fff;border:1px solid var(--line);border-radius:22px;padding:26px;position:relative;}
.tier.hot{border:2px solid var(--orange);box-shadow:0 24px 50px -30px rgba(242,108,30,.45);}
.tier .tag{position:absolute;top:-13px;left:24px;background:var(--orange);color:#fff;font-family:'Hanken Grotesk';font-weight:800;font-size:11px;letter-spacing:.08em;text-transform:uppercase;padding:5px 12px;border-radius:999px;}
.tier h3{font-weight:900;font-size:19px;}
.tier .who{font-size:13px;color:var(--dim);margin:3px 0 14px;}
.price{font-family:'Hanken Grotesk';font-weight:900;font-size:38px;line-height:1;}
.price small{font-size:14px;font-weight:700;color:var(--dim);}
.per{font-size:12.5px;color:var(--faint);margin:4px 0 16px;}
.feat{list-style:none;margin:0 0 20px;padding:0;}
.feat li{font-size:13.5px;color:var(--ink-2);padding:6px 0 6px 26px;position:relative;}
.feat li::before{content:"✓";position:absolute;left:2px;color:var(--orange);font-weight:900;}
.atable{width:100%;border-collapse:collapse;background:#fff;border-radius:16px;overflow:hidden;border:1px solid var(--line);}
.atable th,.atable td{padding:13px 18px;font-size:14px;text-align:left;border-bottom:1px solid var(--line);}
.atable th{font-family:'Hanken Grotesk';font-weight:800;font-size:12px;letter-spacing:.08em;text-transform:uppercase;color:var(--faint);background:var(--card);}
.atable td b{font-family:'Hanken Grotesk';font-weight:800;}
.faq{border-bottom:1px solid var(--line);padding:16px 0;}
.faq b{font-family:'Hanken Grotesk';font-weight:800;font-size:15px;display:block;margin-bottom:5px;}
.faq p{font-size:14px;color:var(--ink-2);margin:0;}
.fine{font-size:12px;color:var(--faint);margin-top:26px;line-height:1.6;}
"""
pricing = shell('Pricing','pricing',pr_css) + """
<div class="wrap">
<header class="head"><span class="eb">Pricing</span>
<h1>Simple pricing for churches of every size</h1>
<p>One license always covers your entire congregation — devotional, group study, sermon outlines, launch kit, and print rights. No per-seat math, no surprise fees.</p>
</header>

<section class="section" id="tiers">
<div class="tiers">
<div class="tier">
  <h3>Single Campaign</h3><div class="who">For your next series — one campaign, everything included</div>
  <div class="price">$199</div><div class="per">one-time · per campaign · whole-church license</div>
  <ul class="feat">
    <li>Any one campaign from the 1,000+ library</li>
    <li>All 5 formats (7, 21, 30, 40-Day &amp; 6-Week)</li>
    <li>Daily devotional + 6-session group study</li>
    <li>6 sermon outlines + full launch kit</li>
    <li>Print-ready PDF with congregation print rights</li>
    <li>Yours to run again in future years</li>
  </ul>
  <a class="btn btn-dark" href="get-access.html" style="width:100%;justify-content:center;">Choose a campaign</a>
</div>
<div class="tier hot"><span class="tag">Most popular</span>
  <h3>All Access</h3><div class="who">The whole library, all year — priced by weekly attendance</div>
  <div class="price">from $49<small>/mo</small></div><div class="per">billed annually · see the attendance table below</div>
  <ul class="feat">
    <li>Unlimited campaigns from all 50 themes</li>
    <li>Every format, every audience edition</li>
    <li>Editable Google Docs / Word copies</li>
    <li>Campaign Finder team workspace</li>
    <li>New campaigns added monthly</li>
    <li>Priority support &amp; launch coaching call</li>
  </ul>
  <a class="btn btn-orange" href="get-access.html" style="width:100%;justify-content:center;">Start All Access</a>
</div>
<div class="tier" id="premium">
  <h3>Premium &amp; Custom</h3><div class="who">Make it unmistakably yours</div>
  <div class="price">from $499</div><div class="per">per project · quoted before work begins</div>
  <ul class="feat">
    <li>Pastor-branded edition — your logo, colors &amp; pastor's name across all formats ($499/campaign)</li>
    <li>Fully custom campaign written for your church's vision (from $4,900)</li>
    <li>Network, denomination &amp; multisite licensing</li>
    <li>Translation-ready source files</li>
  </ul>
  <a class="btn btn-white" href="contact.html" style="width:100%;justify-content:center;">Talk to us</a>
</div>
</div>
</section>

<section class="section"><h2>All Access by attendance</h2>
<div class="sd">Fair pricing that scales with your weekend attendance — comparable church media libraries charge similar or more for a fraction of the campaign depth.</div>
<table class="atable">
<tr><th>Average weekly attendance</th><th>Monthly</th><th>Annual (2 months free)</th></tr>
<tr><td><b>Under 100</b></td><td>$49/mo</td><td>$490/yr</td></tr>
<tr><td><b>100 – 250</b></td><td>$89/mo</td><td>$890/yr</td></tr>
<tr><td><b>251 – 500</b></td><td>$149/mo</td><td>$1,490/yr</td></tr>
<tr><td><b>501 – 1,000</b></td><td>$249/mo</td><td>$2,490/yr</td></tr>
<tr><td><b>Over 1,000 / multisite / networks</b></td><td colspan="2"><a href="contact.html" style="color:var(--orange);font-weight:700;">Custom — talk to us</a></td></tr>
</table>
</section>

<section class="section" id="faq"><h2>Pricing questions</h2>
<div class="faq"><b>Does one license really cover our whole church?</b><p>Yes. Every price on this page is a congregation-wide license — print the devotional for every household, run unlimited groups, use it across your campuses' weekend services. Multisite churches over 1,000 use network pricing.</p></div>
<div class="faq"><b>What's the difference between Single Campaign and All Access?</b><p>Single Campaign is a one-time purchase of one campaign, forever. All Access is an annual subscription to the entire 1,000+ library plus editable source files and everything we add during your term.</p></div>
<div class="faq"><b>Can we cancel All Access?</b><p>Anytime. Annual plans refund unused full months in your first 60 days; after that your access simply runs through the end of the term. Campaigns you've already launched stay launched.</p></div>
<div class="faq"><b>Is there a guarantee?</b><p>30 days, no questions. If your first campaign isn't a fit, we refund it in full.</p></div>
<div class="faq"><b>Do you discount for church plants and small churches?</b><p>Yes — plants under 3 years old and churches under 50 in attendance get 40% off any tier. <a href="contact.html" style="color:var(--orange);font-weight:600;">Just ask.</a></p></div>
<div class="fine">All prices USD. Scripture quotations are from the Holy Bible, New International Version® (NIV®), used with permission of Biblica, Inc. Licenses cover use within your local congregation and its ministries; resale and redistribution outside your church are not permitted. Prices shown are launch pricing and are locked for the life of your subscription.</div>
</section>
</div>
""" + FOOT

# ---------------- FOR CHURCHES / AUDIENCES ----------------
ch_css = """.aud{display:grid;grid-template-columns:1fr 1fr;gap:18px;}
@media(max-width:800px){.aud{grid-template-columns:1fr;}}
.story{background:#fff;border:1px solid var(--line);border-radius:18px;padding:22px;}
.story .q{font-family:'Hanken Grotesk';font-weight:700;font-size:15.5px;line-height:1.45;margin-bottom:12px;}
.story .who{font-size:12.5px;color:var(--dim);}
.stories{display:grid;grid-template-columns:repeat(3,1fr);gap:16px;}
@media(max-width:860px){.stories{grid-template-columns:1fr;}}
"""
churches = shell('For Churches','church',ch_css) + """
<div class="wrap">
<header class="head"><span class="eb">Who it's for</span>
<h1>Built for churches. Loved by families, advisors &amp; networks.</h1>
<p>Lifetogether campaigns started in the local church — and the same library now serves homes, advisor practices, and whole networks. Find your fit below.</p>
</header>

<section class="section" id="churches"><h2>Churches</h2>
<div class="sd">The core of everything we build. One campaign aligns your weekend services, small groups, and every member's daily devotional around a single theme — so momentum from Sunday carries through Saturday.</div>
<div class="cards aud">
<div class="card"><h3>For senior pastors</h3><p>Pick a theme, and the sermon series, group study, and daily devotional arrive already aligned. You preach; the campaign carries the message into the week. <a href="how-it-works.html" style="color:var(--orange);font-weight:600;">See the process →</a></p></div>
<div class="card"><h3>For groups &amp; discipleship pastors</h3><p>Campaigns are the best group-launch engine we know: churches typically see their biggest sign-up wave of the year when a churchwide campaign begins. Every study is written for first-time hosts.</p></div>
</div></section>

<section class="section" id="families"><h2>Families</h2>
<div class="sd">A whole category of campaigns — Family &amp; Parenting, plus Family Legacy themes — is written for the home: dinner-table conversations, milestone moments, and faith that gets passed down on purpose.</div>
<div class="cards aud">
<div class="card"><h3>Around the table</h3><p>Campaigns like <em>Passing Down Faith</em> and <em>Parenting on Purpose</em> turn daily readings into family conversations. <a href="browse.html?cat=4" style="color:var(--orange);font-weight:600;">Browse Family &amp; Parenting →</a></p></div>
<div class="card"><h3>Across generations</h3><p><em>Grandparent Legacy</em> and <em>Family Legacy</em> campaigns help grandparents and legacy families bless the next generation with more than money.</p></div>
</div></section>

<section class="section" id="advisors"><h2>Advisors</h2>
<div class="sd">Financial advisors, CPAs, and wealth managers use Money &amp; Stewardship and Generosity campaigns as client journeys — a 40-day conversation about what money is for.</div>
<div class="cards aud">
<div class="card"><h3>For the practice</h3><p>Walk client families through <em>God Owns It All</em> or <em>Family Legacy</em> ahead of estate and giving decisions. <a href="browse.html?cat=5" style="color:var(--orange);font-weight:600;">Browse Money &amp; Stewardship →</a></p></div>
<div class="card"><h3>For giving conversations</h3><p>Generosity &amp; Kingdom Impact campaigns give donor families shared language before they build a giving plan. <a href="browse.html?cat=6" style="color:var(--orange);font-weight:600;">Browse Generosity →</a></p></div>
</div></section>

<section class="section" id="networks"><h2>Networks &amp; denominations</h2>
<div class="sd">Run one campaign across a hundred churches at once — shared launch dates, shared momentum, network-level reporting, and custom licensing. <a href="contact.html" style="color:var(--orange);font-weight:600;">Talk to us about network licensing →</a></div>
</section>

<section class="section" id="stories"><h2>Church stories</h2>
<div class="sd">Early results from churches running Lifetogether-tradition campaigns. (Names shared with permission; full written case studies are being prepared for platform launch.)</div>
<div class="stories">
<div class="story"><div class="q">"Our groups doubled during the campaign — and eight months later, most of them are still meeting."</div><div class="who">Groups pastor · suburban church of ~450</div></div>
<div class="story"><div class="q">"For forty days the whole church was having one conversation. I've never seen alignment like that here."</div><div class="who">Senior pastor · church of ~180</div></div>
<div class="story"><div class="q">"The launch kit did the heavy lifting. Two volunteers ran what used to take our whole staff."</div><div class="who">Executive pastor · church of ~900</div></div>
</div>
<div style="margin-top:22px;"><a class="btn btn-orange" href="get-access.html">Bring a campaign to your church """+ARROW+"""</a></div>
</section>
</div>
""" + FOOT

# ---------------- ABOUT ----------------
about = shell('About','') + """
<div class="wrap">
<header class="head"><span class="eb">About Lifetogether</span>
<h1>Helping the whole church do life together</h1>
<p>40 Day Campaigns is the campaign library of Lifetogether, founded by Brett Eastman — built in the Purpose Driven tradition to become the world's largest library of churchwide campaigns.</p>
</header>
<section class="section"><h2>Our story</h2>
<div class="sd" style="max-width:72ch;">Brett Eastman helped pioneer the churchwide campaign model through leadership at Saddleback Church and Willow Creek — seasons that produced some of the most-used small-group tools in the modern church and proved a simple idea: churches change fastest when everyone reads, discusses, and hears the same thing at the same time. Lifetogether exists to put that model within reach of every church — not just the megachurch with a publishing arm. Fifty themes. A thousand campaigns and growing. Every felt need a pastor plans around, ready to launch.</div>
</section>
<section class="section"><h2>What we believe about the work</h2>
<div class="cards" style="grid-template-columns:repeat(3,1fr);">
<div class="card"><h3>Scripture first</h3><p>Every campaign is anchored in a passage, not a personality. NIV throughout, used with permission of Biblica.</p></div>
<div class="card"><h3>Pastoral, not academic</h3><p>Plain language, honest felt needs, and gentle care on hard topics — grief, anxiety, money stress — with encouragement toward real-life support.</p></div>
<div class="card"><h3>Together, always</h3><p>Nobody does this alone. Every campaign is designed to be walked with a group, a family, or a friend.</p></div>
</div></section>
<section class="section">
<div style="display:flex;gap:12px;flex-wrap:wrap;">
<a class="btn btn-orange" href="browse.html">Explore the library """+ARROW+"""</a>
<a class="btn btn-white" href="contact.html">Get in touch</a>
</div></section>
</div>
""" + FOOT

# ---------------- CONTACT ----------------
ct_css = """.cgrid{display:grid;grid-template-columns:1.1fr .9fr;gap:26px;}
@media(max-width:820px){.cgrid{grid-template-columns:1fr;}}
.field{margin-bottom:14px;}
.field label{font-family:'Hanken Grotesk';font-weight:700;font-size:12.5px;letter-spacing:.04em;text-transform:uppercase;color:var(--dim);display:block;margin-bottom:6px;}
.field input,.field textarea,.field select{width:100%;border:1px solid var(--line);border-radius:12px;padding:12px 14px;font-family:'Inter';font-size:14px;background:#fff;}
.ok{display:none;background:#EDF9F0;border:1px solid #BFE8CB;color:#1E6B34;border-radius:12px;padding:14px 16px;font-size:14px;margin-top:14px;}
"""
contact = shell('Contact','',ct_css) + """
<div class="wrap">
<header class="head"><span class="eb">Contact</span>
<h1>Talk to a real person</h1>
<p>Questions about a campaign, pricing, network licensing, or a walkthrough for your team — send a note and we'll reply within one business day.</p>
</header>
<section class="section"><div class="cgrid">
<div class="card">
<div class="field"><label>Your name</label><input id="cn" type="text" placeholder="Pastor Sam Rivera"></div>
<div class="field"><label>Email</label><input id="ce" type="email" placeholder="sam@yourchurch.org"></div>
<div class="field"><label>Church / organization</label><input id="cc" type="text" placeholder="Grace Community Church"></div>
<div class="field"><label>What can we help with?</label><select id="ct"><option>Request a walkthrough</option><option>Pricing question</option><option>Pastor-branded / custom campaign</option><option>Network or denomination licensing</option><option>Something else</option></select></div>
<div class="field"><label>Message</label><textarea id="cm" rows="4" placeholder="Tell us a little about your church and what you're planning…"></textarea></div>
<button class="btn btn-orange" id="csend">Send message</button>
<div class="ok" id="cok">Thanks — your message is ready in your email app. If it didn't open, write us directly at <b>hello@40daycampaigns.com</b>.</div>
</div>
<div>
<div class="card" style="margin-bottom:16px;"><h3>Email</h3><p><a href="mailto:hello@40daycampaigns.com" style="color:var(--orange);font-weight:700;">hello@40daycampaigns.com</a></p></div>
<div class="card" style="margin-bottom:16px;"><h3>Walkthroughs</h3><p>15-minute screen-share for you or your whole staff — we'll match campaigns to your calendar and answer anything. Choose "Request a walkthrough" in the form.</p></div>
<div class="card"><h3>Social</h3><p>Our channels go live with the platform launch — until then, this inbox is the fastest way to reach us.</p></div>
</div>
</div></section>
</div>
<script>
document.getElementById('csend').addEventListener('click',()=>{
 const v=id=>document.getElementById(id).value;
 const body=encodeURIComponent(`Name: ${v('cn')}\nChurch: ${v('cc')}\nTopic: ${v('ct')}\n\n${v('cm')}`);
 location.href=`mailto:hello@40daycampaigns.com?subject=${encodeURIComponent(v('ct')+' — '+(v('cc')||'website inquiry'))}&body=${body}`;
 document.getElementById('cok').style.display='block';
});
</script>
""" + FOOT

# ---------------- SIGN IN ----------------
si = shell('Sign in','',ct_css) + """
<div class="wrap">
<header class="head"><span class="eb">Sign in</span>
<h1>Member sign-in opens at platform launch</h1>
<p>Accounts, saved plans, and your church's campaign dashboard arrive with the full platform. Request early access and we'll create your account on day one.</p>
</header>
<section class="section"><div class="cgrid">
<div class="card">
<div class="field"><label>Email</label><input type="email" placeholder="you@yourchurch.org" disabled style="background:var(--card);"></div>
<div class="field"><label>Password</label><input type="password" placeholder="••••••••" disabled style="background:var(--card);"></div>
<button class="btn btn-dark" disabled style="opacity:.45;cursor:not-allowed;">Sign in (available at launch)</button>
<p style="font-size:13px;color:var(--dim);margin-top:14px;">Not a member yet? <a href="get-access.html" style="color:var(--orange);font-weight:700;">Request early access →</a></p>
</div>
<div><div class="card"><h3>Why early access?</h3><p>Founding churches get launch pricing locked for life, first pick of pastor-branded slots, and a hands-on launch coaching call. <a href="pricing.html" style="color:var(--orange);font-weight:600;">See pricing →</a></p></div></div>
</div></section>
</div>
""" + FOOT

# ---------------- GET ACCESS ----------------
ga = shell('Get access','',ct_css) + """
<div class="wrap">
<header class="head"><span class="eb">Get access</span>
<h1>Bring a campaign to your church</h1>
<p>Tell us about your church and what you're planning — we'll set you up with the right tier, and founding churches lock launch pricing for life.</p>
</header>
<section class="section"><div class="cgrid">
<div class="card">
<div class="field"><label>Your name</label><input id="gn" type="text" placeholder="Pastor Sam Rivera"></div>
<div class="field"><label>Email</label><input id="ge" type="email" placeholder="sam@yourchurch.org"></div>
<div class="field"><label>Church name</label><input id="gc" type="text" placeholder="Grace Community Church"></div>
<div class="field"><label>Average weekly attendance</label><select id="gs"><option>Under 100</option><option>100 – 250</option><option>251 – 500</option><option>501 – 1,000</option><option>Over 1,000 / multisite</option></select></div>
<div class="field"><label>Which tier interests you?</label><select id="gt"><option>All Access (annual)</option><option>Single Campaign ($199)</option><option>Premium / pastor-branded</option><option>Not sure yet — help me choose</option></select></div>
<div class="field"><label>Campaign or theme you have in mind (optional)</label><input id="gk" type="text" placeholder="e.g., God Owns It All, or 'something on anxiety'"></div>
<button class="btn btn-orange" id="gsend">Request access</button>
<div class="ok" id="gok">Request drafted in your email app — send it and we'll reply within one business day. Or write <b>hello@40daycampaigns.com</b> directly.</div>
</div>
<div>
<div class="card" style="margin-bottom:16px;"><h3>What happens next</h3><p>1. We reply with your tier and a launch-window suggestion.<br>2. You pick a campaign (or take the <a href="finder.html" style="color:var(--orange);font-weight:600;">Finder</a>).<br>3. We schedule your launch coaching call.</p></div>
<div class="card"><h3>No pressure, ever</h3><p>Every tier has a 30-day guarantee, and this request doesn't commit you to anything — it starts a conversation.</p></div>
</div>
</div></section>
</div>
<script>
document.getElementById('gsend').addEventListener('click',()=>{
 const v=id=>document.getElementById(id).value;
 const body=encodeURIComponent(`Name: ${v('gn')}\nChurch: ${v('gc')}\nAttendance: ${v('gs')}\nTier: ${v('gt')}\nCampaign in mind: ${v('gk')}`);
 location.href=`mailto:hello@40daycampaigns.com?subject=${encodeURIComponent('Early access request — '+(v('gc')||'new church'))}&body=${body}`;
 document.getElementById('gok').style.display='block';
});
</script>
""" + FOOT

# ---------------- FAQ ----------------
faq_css = """.faq{border-bottom:1px solid var(--line);padding:18px 0;}
.faq b{font-family:'Hanken Grotesk';font-weight:800;font-size:16px;display:block;margin-bottom:6px;}
.faq p{font-size:14.5px;color:var(--ink-2);margin:0;max-width:76ch;}
"""
faqp = shell('FAQ','',faq_css) + """
<div class="wrap">
<header class="head"><span class="eb">FAQ</span>
<h1>Everything pastors ask us</h1>
<p>The straight answers — and if yours isn't here, <a href="contact.html" style="color:var(--orange);font-weight:700;">just ask</a>.</p>
</header>
<section class="section">
<div class="faq"><b>What exactly is a "campaign"?</b><p>One theme, delivered three ways at once for a set season: a daily devotional for every member, a 6-session small-group study, and 6 aligned sermon outlines — plus a launch kit. <a href="how-it-works.html" style="color:var(--orange);font-weight:600;">Full walkthrough here.</a></p></div>
<div class="faq"><b>How big is the library?</b><p>1,000+ campaigns across 50 themes in 10 categories, each available in 5 formats (7-Day, 21-Day, 30-Day, 40-Day, and 6-Week group series). New campaigns are added monthly for All Access members.</p></div>
<div class="faq"><b>Which Bible translation do you use?</b><p>NIV throughout, used with permission of Biblica, Inc.</p></div>
<div class="faq"><b>How long does prep take?</b><p>Most churches run about six weeks of prep: pick and customize (weeks 1–2), recruit hosts and promote (weeks 3–5), launch Sunday (week 6). The launch kit includes the whole timeline.</p></div>
<div class="faq"><b>Do we need a big staff?</b><p>No. Everything is written for a solo pastor with a volunteer team — group studies assume first-time hosts, and the launch kit includes ready-to-read announcement scripts.</p></div>
<div class="faq"><b>Can we edit the materials?</b><p>Yes. Print PDFs come with every license; All Access adds fully editable Google Docs/Word files; Canva import works today with one-click integration in development. Pastor-branded editions are done for you.</p></div>
<div class="faq"><b>What does it cost?</b><p>$199 for a single campaign, or All Access from $49/month (by attendance). <a href="pricing.html" style="color:var(--orange);font-weight:600;">Full pricing here.</a></p></div>
<div class="faq"><b>How do sensitive topics get handled?</b><p>Campaigns on grief, anxiety, burnout, and financial stress use gentle, pastoral framing — permission to go slow, comforting Scripture, and consistent encouragement toward a pastor, trusted friend, or professional support where that's wise.</p></div>
<div class="faq"><b>Is there a guarantee?</b><p>30 days on everything, no questions asked.</p></div>
<div style="margin-top:24px;display:flex;gap:12px;flex-wrap:wrap;">
<a class="btn btn-orange" href="finder.html">Find your campaign """+ARROW+"""</a>
<a class="btn btn-white" href="contact.html">Ask something else</a>
</div>
</section>
</div>
""" + FOOT

for name, html in [('how-it-works.html',how),('pricing.html',pricing),('churches.html',churches),
                   ('about.html',about),('contact.html',contact),('signin.html',si),
                   ('get-access.html',ga),('faq.html',faqp)]:
    open(os.path.join(OUT,name),'w').write(html)
    print('built', name, len(html))
