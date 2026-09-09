#!/usr/bin/env python3
# -*- coding: utf-8 -*-

MINISTRIES = [
    ("Women's Ministry", [
        ("Chosen", "Discovering Your Identity in Christ"),
        ("Enough", "Breaking Free from Comparison and Perfectionism"),
        ("Rooted", "Building a Faith That Holds Under Pressure"),
        ("Sisterhood", "Living Life in Authentic Community"),
        ("Unhurried", "Finding Rest for Your Soul in a Busy Season"),
    ]),
    ("Men's Ministry", [
        ("Undivided", "Living with Integrity When No One's Watching"),
        ("Built to Lead", "Becoming the Man Your Family Needs"),
        ("Band of Brothers", "The Power of Real Male Friendship"),
        ("Strength Under Control", "Anger, Ambition, and the Heart of a Godly Man"),
        ("The Long Obedience", "Finishing Well in Faith and Family"),
    ]),
    ("Marriage Ministry", [
        ("One Flesh", "Building an Unbreakable Marriage"),
        ("Recover the Fire", "Reigniting Intimacy and Connection"),
        ("Fight Fair", "Navigating Conflict Without Losing Each Other"),
        ("Together for Good", "Weathering Hard Seasons as a Team"),
        ("Second Half", "Rediscovering Your Marriage After the Kids Leave"),
    ]),
    ("Singles Ministry", [
        ("Whole", "Finding Wholeness Before Half"),
        ("Worth the Wait", "A Biblical Vision for Dating and Purity"),
        ("Not Alone", "Community for the Single Season"),
        ("Called and Complete", "Purpose Beyond Relationship Status"),
        ("Ready for Someday", "Preparing Now for the Marriage to Come"),
    ]),
    ("Young Adults Ministry", [
        ("Undefined", "Finding Your Identity Before the World Names You"),
        ("Real World Faith", "Following Jesus After You Leave Home"),
        ("Adulting with Purpose", "Career, Money, and Calling"),
        ("Not Yet Settled", "Faith in the Uncertain Twenties"),
        ("Fully Known", "Friendship and Belonging in a Lonely Generation"),
    ]),
    ("Senior Adults Ministry", [
        ("Still Bearing Fruit", "Purpose in Every Season of Life"),
        ("Legacy", "Passing Down What Matters Most"),
        ("Finishing Strong", "Faith, Health, and Hope in Later Years"),
        ("Grandparenting on Purpose", "Shaping the Next Generation"),
        ("The Best Is Yet", "Facing Aging and Eternity with Confidence"),
    ]),
    ("Parenting Ministry", [
        ("Raising Faith", "Passing Down What You Believe"),
        ("Grace-Based Parenting", "Leading Without Losing Your Kids' Hearts"),
        ("The Teen Years", "Staying Connected When They're Pulling Away"),
        ("Screens and Souls", "Guiding Kids Through a Digital World"),
        ("Parenting Together", "Staying United When You Disagree"),
    ]),
    ("Family Ministry", [
        ("One Household", "Building a Family That Follows Jesus Together"),
        ("Family Rhythms", "Simple Habits That Shape a Home"),
        ("Blended and Whole", "Thriving as a Step-Family"),
        ("Family Table", "Conversations That Draw You Closer"),
        ("Generations", "Connecting Grandparents, Parents, and Kids in Faith"),
    ]),
    ("Divorce Care & Recovery Ministry", [
        ("After the Vows", "Healing After Divorce"),
        ("Rebuilding", "A New Foundation for a New Season"),
        ("Co-Parenting with Grace", "Putting Kids First After Divorce"),
        ("Whole Again", "Reclaiming Your Identity Beyond Marriage"),
        ("Starting Over", "Hope for the Next Chapter"),
    ]),
    ("Grief & Loss Ministry", [
        ("Even So", "Grieving with Hope"),
        ("The Long Way Home", "Walking Through Loss Without Rushing It"),
        ("When Someone You Love Is Gone", "Facing the First Year"),
        ("Grief Has No Timeline", "Permission to Not Be Okay"),
        ("Held", "Finding God in the Darkest Season"),
    ]),
    ("Recovery Ministry", [
        ("Free Indeed", "Breaking the Cycle of Addiction"),
        ("One Day at a Time", "A Biblical Path to Lasting Recovery"),
        ("Honest", "Facing What's Really Going On"),
        ("New Wineskins", "Life After Addiction"),
        ("Chains Broken", "Hope for the Struggle You Can't Talk About"),
    ]),
    ("Financial & Generosity Ministry", [
        ("God Owns It All", "A Biblical Path to Financial Freedom"),
        ("Debt-Free Faith", "Breaking the Cycle of Financial Bondage"),
        ("Generous Living", "Discovering the Joy of Open Hands"),
        ("Margin", "Managing Money Without Managing Anxiety"),
        ("Legacy Giving", "Stewarding What You'll Leave Behind"),
    ]),
    ("Care & Counseling Ministry", [
        ("Held Together", "Support for Life's Hardest Seasons"),
        ("You're Not Crazy", "Understanding Anxiety, Depression, and Faith"),
        ("Safe People", "Building a Circle That Helps You Heal"),
        ("Permission to Struggle", "Mental Health and the Christian Life"),
        ("Come As You Are", "Care Without Judgment"),
    ]),
    ("Prayer Ministry", [
        ("Unceasing", "Building a Life of Prayer"),
        ("The Prayer Catalyst", "7 Days That Change How You Pray"),
        ("Bold Access", "Praying with Confidence"),
        ("Prayer Warriors", "Interceding for Your Church and City"),
        ("Silent No More", "Finding Your Voice in Prayer"),
    ]),
    ("Small Group / Community Life Ministry", [
        ("Better Together", "Why You Weren't Meant to Do Life Alone"),
        ("Circle Up", "Starting and Leading a Thriving Group"),
        ("Real Community", "Moving from Acquaintance to Family"),
        ("The Group That Changes You", "Vulnerability and Growth"),
        ("Multiply", "Turning Your Group into a Movement"),
    ]),
    ("Discipleship & Spiritual Formation Ministry", [
        ("Formed", "Becoming Like Jesus On Purpose"),
        ("The Practices", "Ancient Habits for a Modern Faith"),
        ("Deep Roots", "Moving from Belief to Formation"),
        ("Apprentice", "Following Jesus the Way the First Disciples Did"),
        ("Slow Growth", "Spiritual Formation in an Instant World"),
    ]),
    ("Evangelism & Outreach Ministry", [
        ("Unashamed", "Sharing Your Faith with Confidence"),
        ("Everyday Mission", "Living Sent Where You Already Are"),
        ("Bridge Builders", "Reaching Neighbors Who Don't Believe"),
        ("One Conversation Away", "The Simplicity of Sharing Jesus"),
        ("Love First", "Outreach That Leads with Compassion"),
    ]),
    ("Missions Ministry", [
        ("Sent", "Discovering Your Part in God's Global Mission"),
        ("The Nations", "Praying and Giving Toward a Global Vision"),
        ("Go and Stay", "Short-Term Trips That Create Long-Term Fruit"),
        ("Local and Global", "One Mission, Two Mission Fields"),
        ("Kingdom Without Borders", "Living a Sent Life"),
    ]),
    ("Volunteer & Serve Team Ministry", [
        ("Called to Serve", "Discovering Your Ministry Fit"),
        ("Behind the Scenes", "The Theology of Faithful Serving"),
        ("Serve Team Culture", "Excellence Without Burnout"),
        ("Every Member a Minister", "Activating Your Whole Church"),
        ("Serving from Overflow", "Avoiding Volunteer Burnout"),
    ]),
    ("Membership & Assimilation Ministry", [
        ("Belong Before You Believe", "Welcoming Every Guest Well"),
        ("Rooted Here", "Moving from Attender to Member"),
        ("Next Steps", "Finding Your Place in Church Life"),
        ("Home", "What It Means to Truly Belong to a Church Family"),
        ("From Visitor to Family", "The First 90 Days"),
    ]),
    ("Leadership Development Ministry", [
        ("Multiplying Leaders", "Developing Who's Next"),
        ("The Leader's Soul", "Staying Spiritually Healthy While Leading Others"),
        ("Elder and Deacon Foundations", "Leading with Character"),
        ("Succession", "Passing the Baton Well"),
        ("Lead from Overflow", "Avoiding Ministry Burnout"),
    ]),
    ("Marketplace & Workplace Ministry", [
        ("Faith at Work", "Living Sent in the Nine-to-Five"),
        ("Kingdom Business", "Leading a Company with Christian Values"),
        ("Called to the Marketplace", "Purpose Beyond the Pulpit"),
        ("Ethics on the Clock", "Integrity When It Costs You"),
        ("Purpose Driven Business", "The 40-Day Formation Model for Leaders and Teams"),
    ]),
    ("Special Needs & Disability Ministry", [
        ("Every Family Belongs", "Welcoming the Disability Community"),
        ("Uniquely Made", "Faith Formation for Every Ability"),
        ("Not Forgotten", "Support for Special Needs Parents"),
        ("Full Access", "Building a Church Where Everyone Fits"),
        ("Different, Not Less", "Seeing Disability Through God's Eyes"),
    ]),
    ("Widows & Widowers Ministry", [
        ("After Goodbye", "Faith and Life After Losing a Spouse"),
        ("Still Whole", "Rediscovering Identity After Widowhood"),
        ("The Empty Chair", "Grief, Memory, and Moving Forward"),
        ("Alone but Not Lonely", "Community After Loss"),
        ("New Normal", "Rebuilding a Life You Didn't Choose"),
    ]),
    ("Military, First Responders & Veterans Ministry", [
        ("Called to Serve, Called to Christ", "Faith in Uniform"),
        ("Battle Ready", "Facing Trauma, PTSD, and the Weight of Service"),
        ("Home Front", "Supporting Military and First Responder Families"),
        ("After the Uniform", "Finding Purpose in Civilian Life"),
        ("Brothers and Sisters in Arms", "Community for Those Who Serve"),
    ]),
]

assert len(MINISTRIES) == 25
for name, titles in MINISTRIES:
    assert len(titles) == 5, name

def esc(s):
    return (s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))

# ---------- Part 1: directory grid of 25 ministries ----------
directory_items = []
for i, (name, _) in enumerate(MINISTRIES, start=1):
    slug = f"m{i:02d}"
    directory_items.append(f'''
        <a class="dir-item" href="#{slug}">
          <span class="dir-num">{i:02d}</span>
          <span class="dir-name">{esc(name)}</span>
        </a>''')
directory_html = "\n".join(directory_items)

# ---------- Part 2: accordion of 25 ministries x 5 titles ----------
accordion_items = []
for i, (name, titles) in enumerate(MINISTRIES, start=1):
    slug = f"m{i:02d}"
    title_rows = "\n".join(
        f'''            <li><span class="t-title">{esc(t)}</span><span class="t-dash">&mdash;</span><span class="t-tag">{esc(tag)}</span></li>'''
        for t, tag in titles
    )
    accordion_items.append(f'''
      <details class="acc" id="{slug}">
        <summary>
          <span class="acc-num">{i:02d}</span>
          <span class="acc-name">{esc(name)}</span>
          <span class="acc-toggle" aria-hidden="true"></span>
        </summary>
        <ul class="title-list">
{title_rows}
        </ul>
      </details>''')
accordion_html = "\n".join(accordion_items)

TEMPLATE = r"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>LifeTogether Ministry Experience Library — The Top 25 &amp; The Finder Architecture</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,500;0,600;0,700;0,900;1,500;1,600&family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;1,400;1,500;1,600&family=Lato:wght@400;700;900&display=swap" rel="stylesheet">
<style>
  :root{
    --navy-950:#080f1e;
    --navy-900:#101a33;
    --navy-850:#131f3d;
    --navy-800:#16223f;
    --navy-700:#1c2a4d;
    --gold:#b8934e;
    --gold-light:#d9bc82;
    --gold-pale:#ecd9ab;
    --cream:#f7f3ea;
    --ink-bright:#fbf7ee;
    --muted:rgba(247,243,234,.82);
    --muted2:rgba(247,243,234,.58);
    --hair:rgba(184,147,78,.3);
  }
  *{box-sizing:border-box;}
  html{scroll-behavior:smooth;}
  @media (prefers-reduced-motion: reduce){ html{scroll-behavior:auto;} *{animation-duration:.001ms !important; transition-duration:.001ms !important;} }
  body{
    margin:0; background:var(--navy-900); color:var(--cream);
    font-family:'Cormorant Garamond',Georgia,serif; font-size:19px; line-height:1.65;
    -webkit-font-smoothing:antialiased;
  }
  ::selection{ background:var(--gold); color:var(--navy-950); }
  h1,h2,h3,h4,.display{ font-family:'Playfair Display',Georgia,serif; font-weight:600; margin:0; color:var(--ink-bright); }
  a{ color:var(--gold-light); text-decoration:none; }
  .wrap{ max-width:980px; margin:0 auto; padding:0 30px; }
  .eyebrow{
    font-family:'Lato',sans-serif; font-weight:700; letter-spacing:.32em; text-transform:uppercase;
    font-size:12px; color:var(--gold-light); margin:0 0 18px;
  }
  .hair{ height:1px; background:var(--hair); border:0; margin:0; }
  section{ position:relative; padding:88px 0; }
  section.alt{ background:var(--navy-850); }
  .lede{ font-size:23px; line-height:1.55; color:var(--muted); font-style:italic; max-width:700px; }
  small.cap{ font-family:'Lato',sans-serif; font-size:12.5px; letter-spacing:.05em; color:var(--muted2); text-transform:uppercase; }

  /* ---------- HERO ---------- */
  .hero{ padding:120px 0 96px; text-align:center; background:
    radial-gradient(ellipse 900px 500px at 50% -10%, rgba(184,147,78,.14), transparent 60%),
    var(--navy-950);
    border-bottom:1px solid var(--hair);
  }
  .hero .eyebrow{ text-align:center; }
  .hero h1{ font-size:52px; line-height:1.12; max-width:820px; margin:0 auto 26px; }
  .hero h1 em{ font-style:italic; color:var(--gold-light); }
  .hero .lede{ margin:0 auto; text-align:center; }
  .hero-stats{ display:flex; gap:46px; justify-content:center; margin-top:56px; flex-wrap:wrap; }
  .hero-stats div{ text-align:center; }
  .hero-stats .num{ font-family:'Playfair Display',serif; font-size:34px; color:var(--gold-light); }
  .hero-stats .lbl{ font-family:'Lato',sans-serif; font-size:11.5px; letter-spacing:.14em; text-transform:uppercase; color:var(--muted2); margin-top:4px; }

  /* ---------- PITCH BAND ---------- */
  .pitch-band{ background:var(--navy-800); border-top:1px solid var(--hair); border-bottom:1px solid var(--hair); padding:56px 0; }
  .pitch-band blockquote{ margin:0; max-width:760px; font-size:25px; font-style:italic; color:var(--ink-bright); line-height:1.5; }
  .pitch-band blockquote::before{ content:"“"; color:var(--gold); font-size:1.2em; }
  .pitch-band blockquote::after{ content:"”"; color:var(--gold); font-size:1.2em; }

  /* ---------- SECTION HEADERS ---------- */
  .sec-head{ display:flex; align-items:baseline; justify-content:space-between; gap:24px; margin-bottom:14px; flex-wrap:wrap; }
  .sec-head h2{ font-size:34px; }
  .sec-sub{ color:var(--muted2); font-size:17px; max-width:640px; margin-top:6px; }

  /* ---------- PART 1: DIRECTORY GRID ---------- */
  .integrated-note{ display:grid; grid-template-columns:repeat(4,1fr); gap:18px; margin:36px 0 44px; }
  .integrated-note .card{ border:1px solid var(--hair); padding:20px 18px; }
  .integrated-note .card .k{ font-family:'Lato',sans-serif; font-size:11px; letter-spacing:.08em; text-transform:uppercase; color:var(--gold-light); margin-bottom:8px; display:block; }
  .integrated-note .card .v{ font-size:17px; color:var(--muted); line-height:1.4; }

  .dir-grid{ display:grid; grid-template-columns:repeat(2,1fr); gap:0; border-top:1px solid var(--hair); }
  .dir-item{ display:flex; align-items:center; gap:16px; padding:15px 4px; border-bottom:1px solid var(--hair); color:var(--cream); transition:padding-left .18s ease, color .18s ease; }
  .dir-item:nth-child(odd){ border-right:1px solid var(--hair); padding-right:20px; }
  .dir-item:nth-child(even){ padding-left:20px; }
  .dir-item:hover{ color:var(--gold-light); padding-left:12px; }
  .dir-num{ font-family:'Playfair Display',serif; font-size:15px; color:var(--gold); min-width:26px; }
  .dir-name{ font-size:18.5px; }

  /* ---------- PART 2: ACCORDION ---------- */
  .acc{ border-bottom:1px solid var(--hair); }
  .acc:first-child{ border-top:1px solid var(--hair); }
  .acc summary{ cursor:pointer; list-style:none; display:flex; align-items:center; gap:20px; padding:20px 4px; }
  .acc summary::-webkit-details-marker{ display:none; }
  .acc-num{ font-family:'Playfair Display',serif; font-size:16px; color:var(--gold); min-width:30px; }
  .acc-name{ font-family:'Playfair Display',serif; font-size:21px; color:var(--ink-bright); flex:1; }
  .acc-toggle{ width:20px; height:20px; position:relative; flex-shrink:0; }
  .acc-toggle::before, .acc-toggle::after{ content:""; position:absolute; background:var(--gold-light); transition:transform .2s ease; }
  .acc-toggle::before{ width:14px; height:1.5px; top:9px; left:3px; }
  .acc-toggle::after{ width:1.5px; height:14px; left:9px; top:3px; }
  .acc[open] .acc-toggle::after{ transform:scaleY(0); }
  .title-list{ list-style:none; margin:0 0 28px; padding:0 4px 4px 50px; display:grid; gap:10px; }
  .title-list li{ font-size:18px; line-height:1.5; }
  .t-title{ font-family:'Playfair Display',serif; font-size:18.5px; color:var(--gold-pale); font-weight:600; }
  .t-dash{ color:var(--muted2); margin:0 8px; }
  .t-tag{ color:var(--muted); }

  /* ---------- PART 3: BUILDER STEPS ---------- */
  .steps{ display:grid; gap:0; margin-top:40px; }
  .step{ display:grid; grid-template-columns:64px 1fr; gap:24px; padding:28px 0; border-top:1px solid var(--hair); }
  .steps .step:last-child{ border-bottom:1px solid var(--hair); }
  .step-num{ font-family:'Playfair Display',serif; font-size:30px; color:var(--gold); }
  .step h3{ font-size:21px; margin-bottom:8px; }
  .step p{ color:var(--muted); font-size:18px; margin:0; }
  .voice-note{ margin-top:36px; padding:24px 26px; border-left:2px solid var(--gold); background:rgba(184,147,78,.06); }
  .voice-note p{ margin:0; color:var(--muted); font-size:18px; }

  /* ---------- PART 4: THREE DOORS ---------- */
  .doors{ display:grid; grid-template-columns:repeat(3,1fr); gap:22px; margin-top:40px; }
  .door{ border:1px solid var(--hair); border-top:none; border-radius:120px 120px 6px 6px; padding:46px 24px 30px; text-align:center; position:relative; }
  .door::before{ content:""; position:absolute; top:-1px; left:-1px; right:-1px; height:1px; background:var(--hair); border-radius:120px 120px 0 0; }
  .door::after{ content:""; position:absolute; top:0; left:0; right:0; height:110px; border:1px solid var(--hair); border-bottom:none; border-radius:120px 120px 0 0; }
  .door-name{ font-size:23px; margin-bottom:14px; }
  .door-for{ color:var(--muted); font-size:16.5px; line-height:1.5; margin-bottom:16px; min-height:80px; }
  .door-who{ font-family:'Lato',sans-serif; font-size:12px; letter-spacing:.05em; text-transform:uppercase; color:var(--gold-light); border-top:1px solid var(--hair); padding-top:14px; }
  .naming-box{ margin-top:40px; border:1px solid var(--hair); padding:28px 30px; }
  .naming-box h4{ font-size:17px; color:var(--gold-light); margin-bottom:16px; font-family:'Lato',sans-serif; letter-spacing:.04em; text-transform:uppercase; font-weight:700; }
  .naming-opt{ padding:12px 0; border-top:1px solid var(--hair); font-size:18px; color:var(--muted); }
  .naming-opt b{ color:var(--ink-bright); font-family:'Playfair Display',serif; font-weight:600; }

  /* ---------- PART 5: BUSINESS MODEL ---------- */
  .biz-grid{ display:grid; grid-template-columns:1fr 1fr; gap:24px; margin-top:40px; }
  .biz-card{ border:1px solid var(--hair); padding:32px 28px; }
  .biz-card.featured{ border-color:var(--gold); background:rgba(184,147,78,.05); }
  .biz-card h3{ font-size:22px; margin-bottom:12px; }
  .biz-card p{ color:var(--muted); font-size:17.5px; margin:0; }
  .biz-note{ margin-top:24px; color:var(--muted2); font-size:16.5px; font-style:italic; }

  /* ---------- PART 6A: CASCADE ---------- */
  .cascade{ margin-top:44px; }
  .cas-row{ border-top:1px solid var(--hair); padding:24px 0; display:grid; grid-template-columns:220px 1fr 1fr 130px; gap:20px; align-items:start; }
  .cascade .cas-row:last-child{ border-bottom:1px solid var(--hair); }
  .cas-role{ font-family:'Playfair Display',serif; font-size:19px; color:var(--ink-bright); }
  .cas-bar{ height:5px; background:var(--gold); margin-top:10px; border-radius:2px; }
  .cas-col small.cap{ display:block; margin-bottom:6px; }
  .cas-col p{ margin:0; font-size:16px; color:var(--muted); line-height:1.45; }
  .cas-builder{ font-family:'Lato',sans-serif; font-size:12px; letter-spacing:.04em; text-transform:uppercase; color:var(--gold-light); text-align:right; }
  .cas-builder.no{ color:var(--muted2); }

  /* ---------- PART 6B: B2B FORK ---------- */
  .fork{ display:grid; grid-template-columns:1fr 1fr; gap:22px; margin-top:36px; }
  .fork-card{ border:1px solid var(--hair); padding:26px 24px; }
  .fork-card h4{ font-size:19px; margin-bottom:10px; color:var(--gold-light); }
  .fork-card p{ margin:0; color:var(--muted); font-size:16.5px; }
  .recommend{ margin-top:22px; border-left:2px solid var(--gold); background:rgba(184,147,78,.06); padding:20px 24px; }
  .recommend p{ margin:0; color:var(--muted); font-size:17px; }
  .recommend b{ color:var(--ink-bright); }

  /* ---------- PART 6C: PRINT ONE ---------- */
  .print-one{ margin-top:40px; border:1px solid var(--gold); padding:36px; display:grid; grid-template-columns:1fr auto; gap:30px; align-items:center; }
  .print-one h3{ font-size:24px; margin-bottom:10px; }
  .print-one p{ color:var(--muted); font-size:17.5px; margin:0 0 8px; max-width:560px; }
  .price-tag{ text-align:center; }
  .price-tag .amt{ font-family:'Playfair Display',serif; font-size:44px; color:var(--gold-light); }
  .price-tag .per{ font-family:'Lato',sans-serif; font-size:11px; letter-spacing:.1em; text-transform:uppercase; color:var(--muted2); }
  .revenue-lines{ display:flex; gap:0; margin-top:34px; border-top:1px solid var(--hair); }
  .rev{ flex:1; padding:22px 20px 0; border-right:1px solid var(--hair); }
  .rev:last-child{ border-right:none; }
  .rev .lbl{ font-family:'Lato',sans-serif; font-size:11.5px; letter-spacing:.08em; text-transform:uppercase; color:var(--gold-light); margin-bottom:8px; display:block; }
  .rev p{ margin:0; color:var(--muted); font-size:16px; }

  /* ---------- PART 7: RESOURCE CATEGORIES ---------- */
  .res-list{ margin-top:40px; }
  .res{ display:grid; grid-template-columns:56px 1fr; gap:26px; padding:30px 0; border-top:1px solid var(--hair); }
  .res-list .res:last-child{ border-bottom:1px solid var(--hair); }
  .res-num{ font-family:'Playfair Display',serif; font-size:26px; color:var(--gold); }
  .res h3{ font-size:21px; margin-bottom:8px; }
  .res .felt{ color:var(--gold-pale); font-style:italic; font-size:17px; display:block; margin-bottom:8px; }
  .res p.desc{ color:var(--muted); font-size:17.5px; margin:0; }

  /* ---------- CLOSING ---------- */
  .closing{ text-align:center; padding:110px 0; background:var(--navy-950); }
  .closing blockquote{ max-width:760px; margin:0 auto; font-size:28px; font-style:italic; line-height:1.55; color:var(--ink-bright); }
  .closing blockquote::before{ content:"“"; color:var(--gold); }
  .closing blockquote::after{ content:"”"; color:var(--gold); }
  .closing .sig{ margin-top:40px; font-family:'Lato',sans-serif; font-size:12px; letter-spacing:.28em; text-transform:uppercase; color:var(--muted2); }

  @media (max-width:760px){
    .hero h1{ font-size:36px; }
    .integrated-note{ grid-template-columns:1fr 1fr; }
    .dir-grid{ grid-template-columns:1fr; }
    .dir-item:nth-child(odd){ border-right:none; padding-right:4px; }
    .dir-item:nth-child(even){ padding-left:4px; }
    .doors{ grid-template-columns:1fr; }
    .biz-grid, .fork{ grid-template-columns:1fr; }
    .cas-row{ grid-template-columns:1fr; }
    .cas-builder{ text-align:left; }
    .print-one{ grid-template-columns:1fr; text-align:center; }
    .revenue-lines{ flex-direction:column; }
    .rev{ border-right:none; border-bottom:1px solid var(--hair); padding-bottom:20px; }
    .res{ grid-template-columns:1fr; }
  }
</style>
</head>
<body>

  <!-- ============ HERO ============ -->
  <header class="hero">
    <div class="wrap">
      <p class="eyebrow">LifeTogether Ministry Experience Library</p>
      <h1>Not a campaign login. <em>A whole-church operating system.</em></h1>
      <p class="lede">Every ministry in the church &mdash; from the women's Bible study to the grief support group &mdash; running on the same theological foundation, the same teaching architecture, and the same design system, while each ministry keeps its own voice, its own leader, and its own pace.</p>
      <div class="hero-stats">
        <div><div class="num">25</div><div class="lbl">Church Ministries</div></div>
        <div><div class="num">125</div><div class="lbl">Signature Titles</div></div>
        <div><div class="num">3</div><div class="lbl">Finders, One Library</div></div>
        <div><div class="num">7</div><div class="lbl">Resources per Ministry</div></div>
      </div>
    </div>
  </header>

  <div class="pitch-band">
    <div class="wrap">
      <blockquote>Whole church, not whole-church-at-once. Everyone can be on the same page when unity matters &mdash; and on their own page when their season of life requires it &mdash; curated and vetted by the Senior Pastor so every ministry teaches from the same accurate theology, philosophy, and strategy.</blockquote>
    </div>
  </div>

  <!-- ============ PART 1 ============ -->
  <section id="part1">
    <div class="wrap">
      <p class="eyebrow">Part One</p>
      <div class="sec-head">
        <h2>The Top 25 Church Ministries</h2>
      </div>
      <p class="sec-sub">Adult and life-stage ministries only &mdash; no children's, youth, or family companion editions unless the ministry itself is Family Ministry. Every ministry gets the same integrated package:</p>

      <div class="integrated-note">
        <div class="card"><span class="k">For the Leader</span><span class="v">Master Teaching Notes &mdash; theology, illustrations, discussion facilitation, verified Scripture citations</span></div>
        <div class="card"><span class="k">For the Group</span><span class="v">Small Group Workbook &mdash; session content, questions, application</span></div>
        <div class="card"><span class="k">For the Home</span><span class="v">Personal Journey / Devotional &mdash; a daily companion of matching length</span></div>
        <div class="card"><span class="k">Flexible Length</span><span class="v">21-day, 30-day, 40-day, or a straight week count (4, 6, 8, 10, 12+)</span></div>
      </div>

      <div class="dir-grid">
{{DIRECTORY}}
      </div>
    </div>
  </section>

  <!-- ============ PART 2 ============ -->
  <section class="alt" id="part2">
    <div class="wrap">
      <p class="eyebrow">Part Two</p>
      <div class="sec-head">
        <h2>Five Signature Titles per Ministry</h2>
      </div>
      <p class="sec-sub">125 titles total. Tap a ministry to open its five signature series.</p>
      <div class="accordion">
{{ACCORDION}}
      </div>
    </div>
  </section>

  <!-- ============ PART 3 ============ -->
  <section id="part3">
    <div class="wrap">
      <p class="eyebrow">Part Three</p>
      <div class="sec-head">
        <h2>The Curriculum Builder</h2>
      </div>
      <p class="sec-sub">Every one of the 125 titles runs through the same build.</p>

      <div class="steps">
        <div class="step">
          <div class="step-num">01</div>
          <div>
            <h3>Choose your length</h3>
            <p>21-Day, 30-Day, 40-Day, or a custom week count (4/6/8/10/12+).</p>
          </div>
        </div>
        <div class="step">
          <div class="step-num">02</div>
          <div>
            <h3>Let the system generate</h3>
            <p>Master Teaching Notes, the Small Group Workbook, and the Personal Journey/Devotional at matching length, automatically.</p>
          </div>
        </div>
        <div class="step">
          <div class="step-num">03</div>
          <div>
            <h3>Choose your customization tier</h3>
            <p>Ready to Use &nbsp;/&nbsp; Lightly Customized (branding, leader letter, dates, local application) &nbsp;/&nbsp; Fully Customized (title, teaching, stories, videos, questions, daily readings, design, pathway).</p>
          </div>
        </div>
        <div class="step">
          <div class="step-num">04</div>
          <div>
            <h3>Choose your format</h3>
            <p>Digital (app/PDF) or Print-Ready &mdash; every layout is Canva-ready so a local team can drop in their own logo, colors, and leader photo without touching the underlying content.</p>
          </div>
        </div>
      </div>

      <div class="voice-note">
        <p><strong style="color:var(--ink-bright)">Local voice, master accuracy &mdash;</strong> the Senior Pastor's own material, church library, and the LifeTogether master library are blended so every ministry teaches from the same verified theology and strategy, even when 25 different leaders are running 25 different studies.</p>
      </div>
    </div>
  </section>

  <!-- ============ PART 4 ============ -->
  <section class="alt" id="part4">
    <div class="wrap">
      <p class="eyebrow">Part Four</p>
      <div class="sec-head">
        <h2>The Finder Architecture</h2>
      </div>
      <p class="sec-sub">Three doors, one library &mdash; each solving a different search intent.</p>

      <div class="doors">
        <div class="door">
          <div class="door-name">Curriculum Finder</div>
          <div class="door-for">Browsing the full 6,200+ title master directory by ministry, felt need, theme, age, group size, teaching style, format.</div>
          <div class="door-who">Ministry &amp; small group leaders picking their next series</div>
        </div>
        <div class="door">
          <div class="door-name">Campaign Finder</div>
          <div class="door-for">Churchwide, all-in initiatives &mdash; Catalyst Sunday, 7-Day, 21-Day, 30-Day, 40-Day formats.</div>
          <div class="door-who">Senior Pastor &amp; staff planning whole-church unity moments</div>
        </div>
        <div class="door">
          <div class="door-name">Journey Finder</div>
          <div class="door-for">Individual and family daily devotional companions, self-paced. (Personal Devotionals)</div>
          <div class="door-who">Individuals, families &mdash; anyone going through material solo</div>
        </div>
      </div>

      <div class="naming-box">
        <h4>Naming Options for the Third Finder &mdash; clever, not yet clear</h4>
        <div class="naming-opt"><b>Journey Finder (Devotionals)</b> &mdash; clean, matches the "Curriculum Finder / Campaign Finder" rhythm</div>
        <div class="naming-opt"><b>The Journey Finder</b> &mdash; with "Personal Devotionals" as a permanent subhead rather than parenthetical</div>
        <div class="naming-opt"><b>My Journey Finder</b> &mdash; leans personal/possessive, distinguishes it clearly from the group-facing tools</div>
        <div class="naming-opt"><b>Daily Journey Finder</b> &mdash; foregrounds the daily-devotional use case up front</div>
      </div>
    </div>
  </section>

  <!-- ============ PART 5 ============ -->
  <section id="part5">
    <div class="wrap">
      <p class="eyebrow">Part Five</p>
      <div class="sec-head">
        <h2>The Business Model</h2>
      </div>
      <p class="sec-sub">All-Access vs. module upsells.</p>

      <div class="biz-grid">
        <div class="biz-card featured">
          <h3>All-Access Pass</h3>
          <p>One church subscription unlocks all 25 ministry libraries plus the full Campaign system. Every ministry leader and small group leader logs in under the church account and pulls what's unique to their ministry through the Finder.</p>
        </div>
        <div class="biz-card">
          <h3>Module Upsells</h3>
          <p>Family Module and Youth/Children Module are sold and licensed separately from the 25 adult/life-stage ministries, since they carry their own companion editions and production cost.</p>
        </div>
      </div>
      <p class="biz-note">Access lives at the church level, not per-leader &mdash; consistent with how the Small Group Master Brochure and campaign subscriptions already work.</p>
    </div>
  </section>

  <!-- ============ PART 6 ============ -->
  <section class="alt" id="part6">
    <div class="wrap">
      <p class="eyebrow">Part Six</p>
      <div class="sec-head">
        <h2>How Access Actually Cascades</h2>
      </div>
      <p class="sec-sub">A. Inside the church &mdash; role by role. The further down the chain, the narrower the library and the lighter the customization.</p>

      <div class="cascade">
        <div class="cas-row">
          <div>
            <div class="cas-role">Staff / Ministry Directors</div>
            <div class="cas-bar" style="width:100%"></div>
          </div>
          <div class="cas-col"><small class="cap">Sees</small><p>Full 6,200+ title library, all 25 ministries, all campaigns</p></div>
          <div class="cas-col"><small class="cap">Customization</small><p>Fully Customized &mdash; title, teaching, stories, video, design</p></div>
          <div class="cas-builder">Full Builder</div>
        </div>
        <div class="cas-row">
          <div>
            <div class="cas-role">Volunteer Ministry Leaders</div>
            <div class="cas-bar" style="width:74%"></div>
          </div>
          <div class="cas-col"><small class="cap">Sees</small><p>Their ministry's library only (e.g., Women's leader sees Women's titles)</p></div>
          <div class="cas-col"><small class="cap">Customization</small><p>Lightly Customized &mdash; branding, leader letter, dates, local application</p></div>
          <div class="cas-builder">Local Customization Builder</div>
        </div>
        <div class="cas-row">
          <div>
            <div class="cas-role">Small Group Leaders</div>
            <div class="cas-bar" style="width:46%"></div>
          </div>
          <div class="cas-col"><small class="cap">Sees</small><p>Only the specific series assigned or selected for their group</p></div>
          <div class="cas-col"><small class="cap">Customization</small><p>Ready to Use, or Lightly Customized if their ministry leader enables it</p></div>
          <div class="cas-builder no">No &mdash; they receive, they don't build</div>
        </div>
        <div class="cas-row">
          <div>
            <div class="cas-role">Congregation / Members</div>
            <div class="cas-bar" style="width:22%"></div>
          </div>
          <div class="cas-col"><small class="cap">Sees</small><p>Personal Journey Finder &mdash; devotionals, family journals, personal studies</p></div>
          <div class="cas-col"><small class="cap">Customization</small><p>Personal customization: name, family names, cover photo, dedication</p></div>
          <div class="cas-builder">Personal Journal Builder</div>
        </div>
      </div>

      <p class="sec-sub" style="margin-top:56px;">B. Outside the church &mdash; business &amp; nonprofit leaders. A real fork, worth deciding deliberately.</p>
      <div class="fork">
        <div class="fork-card">
          <h4>Option 1 &mdash; Separate B2B License</h4>
          <p>Purpose Driven Business (and a parallel nonprofit track) sells directly to companies and nonprofits, independent of any church relationship. Its own pricing, its own sales motion, its own case studies (Movement Mortgage as the flagship).</p>
        </div>
        <div class="fork-card">
          <h4>Option 2 &mdash; Church-Sponsored Bridge</h4>
          <p>A church with an active Marketplace &amp; Workplace Ministry can gift or extend Purpose Driven Business access to business owners in their congregation as a relationship-building value-add &mdash; without merging the two licensing systems.</p>
        </div>
      </div>
      <div class="recommend">
        <p><b>Recommendation:</b> keep Purpose Driven Business and the nonprofit track as their own license, sold on their own terms &mdash; but build the bridge as an option, since it turns Marketplace Ministry into a warm lead source for the B2B product rather than asking two very different buyers (a Small Groups Pastor and a company CEO) to go through the same checkout.</p>
      </div>

      <p class="sec-sub" style="margin-top:56px;">C. The "Print One" model &mdash; fully customized, single unit.</p>
      <div class="print-one">
        <div>
          <h3>A standalone micro-product</h3>
          <p>A member (or anyone, church-subscriber or not) builds one fully personalized journal or workbook through a simplified Canva-based Personal Journal Builder &mdash; their name, a dedication, a cover photo, maybe a translation preference. Output is print-ready: a downloadable PDF or a ship-to-print single copy.</p>
          <p>Priced and positioned like a personalized gift, not a curriculum purchase &mdash; a grief journal personalized with a name, a marriage journal for an anniversary, a family devotional with the kids' names on the cover. Works inside an All-Access church too: a member whose church already has the digital library pays just for the physical, personalized print copy.</p>
        </div>
        <div class="price-tag">
          <div class="amt">$25</div>
          <div class="per">Per Unit &middot; No Subscription</div>
        </div>
      </div>

      <div class="revenue-lines">
        <div class="rev"><span class="lbl">Church Subscription</span><p>Recurring</p></div>
        <div class="rev"><span class="lbl">B2B Licensing</span><p>Purpose Driven Business &amp; nonprofit track</p></div>
        <div class="rev"><span class="lbl">Individual Print-on-Demand</span><p>One-off, gift-driven</p></div>
      </div>
    </div>
  </section>

  <!-- ============ PART 7 ============ -->
  <section id="part7">
    <div class="wrap">
      <p class="eyebrow">Part Seven</p>
      <div class="sec-head">
        <h2>The Seven Ministry Builder Resource Categories</h2>
      </div>
      <p class="sec-sub">Every one of the 25 ministries gets the same seven resource types &mdash; ordered by the felt need that hits a Senior Pastor first.</p>

      <div class="res-list">
        <div class="res">
          <div class="res-num">01</div>
          <div>
            <h3>Launch &amp; Lead Guide</h3>
            <span class="felt">"Will this ministry actually get off the ground &mdash; and survive past month three?"</span>
            <p class="desc">The step-by-step for standing up this specific ministry: structure, recruiting a leader, the first 90 days, avoiding the most common reasons volunteer ministries stall or quietly die.</p>
          </div>
        </div>
        <div class="res">
          <div class="res-num">02</div>
          <div>
            <h3>Leader Training &amp; Development Course</h3>
            <span class="felt">"Is the person I'm about to hand this to actually equipped to lead it well?"</span>
            <p class="desc">A short course (video + guide) that trains the volunteer or staff leader &mdash; not just to teach content, but to shepherd people, facilitate hard conversations, and lead a group well.</p>
          </div>
        </div>
        <div class="res">
          <div class="res-num">03</div>
          <div>
            <h3>Sermon &amp; Message Support Kit</h3>
            <span class="felt">"Can I connect this to what I'm already preaching, so the whole church feels the momentum?"</span>
            <p class="desc">Message outlines, illustrations, and launch-Sunday material the Senior Pastor can use to introduce or reinforce the ministry from the platform &mdash; tying the small group experience to the sermon calendar.</p>
          </div>
        </div>
        <div class="res">
          <div class="res-num">04</div>
          <div>
            <h3>Core Campaigns &amp; Curriculum Library</h3>
            <span class="felt">"What are they actually going to teach, week to week?"</span>
            <p class="desc">The customizable campaign/series content itself &mdash; the 125 titles, in 21/30/40-day or custom-week formats, at Ready to Use / Lightly / Fully Customized tiers.</p>
          </div>
        </div>
        <div class="res">
          <div class="res-num">05</div>
          <div>
            <h3>Best-Practices Playbook &amp; Small Group Handbook</h3>
            <span class="felt">"Will this still be healthy &mdash; and growing &mdash; a year from now?"</span>
            <p class="desc">The sustaining wisdom: how to multiply groups, keep volunteer leaders from burning out, measure ministry health, and scale without losing quality.</p>
          </div>
        </div>
        <div class="res">
          <div class="res-num">06</div>
          <div>
            <h3>Devotional &amp; Personal Journeys</h3>
            <span class="felt">"Does this reach people beyond the one hour a week they're in the room?"</span>
            <p class="desc">The daily, personal or family-length companion to the group series, so engagement extends into people's homes between sessions.</p>
          </div>
        </div>
        <div class="res">
          <div class="res-num">07</div>
          <div>
            <h3>Tools, Templates &amp; Operational Toolkit</h3>
            <span class="felt">"Do we have the operational plumbing to actually run this without reinventing it every time?"</span>
            <p class="desc">Transferable, non-content assets: sign-up forms, communication and social templates, event checklists, budget templates &mdash; the reusable back-office layer behind every ministry.</p>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- ============ CLOSING ============ -->
  <footer class="closing">
    <div class="wrap">
      <blockquote>This isn't a campaign login. It's your church's whole-life discipleship operating system &mdash; every ministry running on the same theological foundation, the same design system, and the same easy-to-use finder, so your people can be in step together when it matters, and in step with where they are personally the rest of the time.</blockquote>
      <div class="sig">LifeTogether Ministries</div>
    </div>
  </footer>

</body>
</html>
"""

html = TEMPLATE.replace("{{DIRECTORY}}", directory_html).replace("{{ACCORDION}}", accordion_html)

out_path = "/home/claude/ministry-library/lifetogether-ministry-experience-library.html"
with open(out_path, "w", encoding="utf-8") as f:
    f.write(html)

print("wrote", out_path, len(html), "bytes")
