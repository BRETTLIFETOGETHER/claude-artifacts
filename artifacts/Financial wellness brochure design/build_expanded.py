# -*- coding: utf-8 -*-
"""The Stewardship Collection — Expanded Edition.
All ten campaigns, pastor-facing marketing. Flourishing design system.
Accents match the canonical shipped brochure exactly."""
import base64, pathlib

FDIR = pathlib.Path("/home/claude/fonts")
b64 = lambda n: base64.b64encode((FDIR / n).read_bytes()).decode()

def face(fam, f, w, s="normal"):
    return (f"@font-face{{font-family:'{fam}';font-style:{s};font-weight:{w};font-display:block;"
            f"src:url(data:font/ttf;base64,{b64(f)}) format('truetype');}}")

FONT_CSS = "".join([
    face("Playfair Display", "PlayfairDisplay-var.ttf", "400 900"),
    face("Playfair Display", "PlayfairDisplay-Italic-var.ttf", "400 900", "italic"),
    face("Archivo", "Archivo-var.ttf", "400 700"),
    face("Spectral", "Spectral-Light.ttf", "300"),
    face("Spectral", "Spectral-LightItalic.ttf", "300", "italic"),
    face("Spectral", "Spectral-Regular.ttf", "400"),
    face("Spectral", "Spectral-Italic.ttf", "400", "italic"),
    face("Spectral", "Spectral-Medium.ttf", "500"),
    face("Spectral", "Spectral-MediumItalic.ttf", "500", "italic"),
    face("Spectral", "Spectral-SemiBold.ttf", "600"),
])

# Three movements the collection travels through
MOVEMENTS = {
    1: ("Movement One", "The Reframe", "Who owns it — and who are you? Two campaigns that settle the question everything else stands on."),
    4: ("Movement Two", "The Practice", "Four campaigns that take the conviction into the calendar, the character, the ordinary day, and the whole person."),
    8: ("Movement Three", "The Horizon", "Three campaigns that lift the eyes — to the generations, the Kingdom, and the open hand the whole collection is walking toward."),
}

CAMPAIGNS = [
    {
        "ac": "#16453a", "tint": "#e9f3ef", "num": "1", "rank": "Rank 1",
        "title": "Life", "title_em": "Stewardship", "role": "The reframe",
        "tagline": "Nothing here is ours.",
        "hook": "Your people think stewardship is a money sermon. It isn't. It's their whole life.",
        "pitch": ("Five trusts — time, talent, treasure, trust, testimony. One reframe: owner or manager? "
                  "This is the on-ramp campaign that makes every other stewardship conversation possible, "
                  "because it moves the topic off the offering plate and onto the whole of life."),
        "launch": "Kicking off a ministry year, opening a stewardship emphasis, or preaching to a mixed-maturity room.",
        "wins": "Everyone. Church and workplace.",
        "verse": "The earth is the Lord's, and everything in it.",
        "ref": "Psalm 24:1 (NIV)",
    },
    {
        "ac": "#1e2d4f", "tint": "#eef1f8", "num": "2", "rank": "Rank 2",
        "title": "", "title_em": "Entrusted", "role": "The identity",
        "tagline": "You didn't earn the starting line.",
        "hook": "The parable of the talents, aimed straight at the self-made myth.",
        "pitch": ("Identity-level, not behavior-level. This is the campaign that turns faithfulness from "
                  "guilt into gratitude — and names the fear that's got your people's gifts buried in the "
                  "ground. It ends where every steward wants to land: well done."),
        "launch": "You want depth after Life Stewardship, or foundational teaching for new believers and leaders.",
        "wins": "New believers, leaders, anyone quietly exhausted by ownership.",
        "verse": "Well done, good and faithful servant!",
        "ref": "Matthew 25:21 (NIV)",
    },
    {
        "ac": "#3a3115", "tint": "#f5f1e5", "num": "3", "rank": "Rank 3",
        "title": "Stewarding", "title_em": "What Matters", "role": "The calendar",
        "tagline": "Best, not more.",
        "hook": "Your most faithful people are managing the wrong things beautifully.",
        "pitch": ("The highest-felt-need campaign in the collection. Mary and Martha, the urgent versus the "
                  "essential, and the honest audit nobody wants to run. Busy congregations feel this one in "
                  "week one — it's the easiest launch in the catalog."),
        "launch": "January, back-to-school, or any season your church is running on fumes.",
        "wins": "The overcommitted, leaders, families in demanding seasons.",
        "verse": "Be very careful, then, how you live — not as unwise but as wise.",
        "ref": "Ephesians 5:15 (NIV)",
    },
    {
        "ac": "#1f3a2c", "tint": "#edf4ef", "num": "4", "rank": "Rank 4",
        "title": "Faithful", "title_em": "Stewardship", "role": "The character",
        "tagline": "Faithful in very little.",
        "hook": "God's measure isn't size. It's faithfulness.",
        "pitch": ("The character campaign. Integrity when no one's watching, honest work, a kept word, the "
                  "long obedience. This is the one that builds the people you'll want leading everything "
                  "else — which makes it a leadership-pipeline play, not just a series."),
        "launch": "Building a leadership culture, or after a season that exposed integrity gaps.",
        "wins": "Leaders, emerging leaders, marketplace believers.",
        "verse": "Whoever can be trusted with very little can also be trusted with much.",
        "ref": "Luke 16:10 (NIV)",
    },
    {
        "ac": "#1f3550", "tint": "#edf1f7", "num": "5", "rank": "Rank 5",
        "title": "Stewardship", "title_em": "That Lasts", "role": "The horizon",
        "tagline": "Leave it better.",
        "hook": "The rich fool built bigger barns. What are you building?",
        "pitch": ("The generational campaign — character, resources, and faith handed forward. Three "
                  "legacies, one finish line. This one moves your second-half givers and your parents like "
                  "nothing else in the collection, and it opens the legacy conversation naturally."),
        "launch": "Year-end, a legacy or capital emphasis, or a parents and grandparents push.",
        "wins": "Parents, leaders, second-half-of-life congregants.",
        "verse": "A good person leaves an inheritance for their children's children.",
        "ref": "Proverbs 13:22 (NIV)",
    },
    {
        "ac": "#15403f", "tint": "#eaf4f3", "num": "6", "rank": "Rank 6",
        "title": "Living as", "title_em": "a Steward", "role": "The daily rhythm",
        "tagline": "Stewardship on a Tuesday.",
        "hook": "Stewardship is an identity before it's an activity.",
        "pitch": ("The everyday campaign. Work, money, time, and rest — the four rooms your people actually "
                  "live in, walked through one at a time until managing rather than owning becomes instinct. "
                  "This is the one that keeps stewardship from being an annual event."),
        "launch": "You want stewardship to stick past the series, or you're launching marketplace groups.",
        "wins": "Working adults, everyday disciples, anyone who's been through a stewardship series before.",
        "verse": "Whatever you do, work at it with all your heart, as working for the Lord.",
        "ref": "Colossians 3:23 (NIV)",
    },
    {
        "ac": "#27264f", "tint": "#eeeef7", "num": "7", "rank": "Rank 7",
        "title": "Kingdom", "title_em": "Stewardship", "role": "The mission",
        "tagline": "Whose kingdom are you building?",
        "hook": "A person can manage their life beautifully and still build a very small kingdom.",
        "pitch": ("The mission campaign. Treasure in heaven, resources aimed at what God is doing, and the "
                  "only earthly investment that lasts forever — people. This is the series that turns "
                  "careful managers into Kingdom investors, and it pairs naturally with a missions or "
                  "vision push."),
        "launch": "A missions emphasis, a vision series, or the season you're casting a bigger why.",
        "wins": "Givers, leaders, the mission-driven.",
        "verse": "Seek first his kingdom and his righteousness.",
        "ref": "Matthew 6:33 (NIV)",
    },
    {
        "ac": "#3a1f3d", "tint": "#f3edf4", "num": "8", "rank": "Rank 8",
        "title": "The Stewarded", "title_em": "Life", "role": "The whole person",
        "tagline": "No corner left on autopilot.",
        "hook": "Most people steward one area of life well and quietly abandon the rest.",
        "pitch": ("The whole-person campaign. Body, mind, soul, and relationships — the honest examination "
                  "your people avoid, held with grace rather than guilt. This is the reset series, and it "
                  "surfaces the areas your care ministry usually hears about far too late."),
        "launch": "New Year, Lent, or any season calling for an honest reset.",
        "wins": "The growth-minded, self-examiners, anyone running on autopilot.",
        "verse": "Search me, God, and know my heart.",
        "ref": "Psalm 139:23 (NIV)",
    },
    {
        "ac": "#46201f", "tint": "#f6ece9", "num": "9", "rank": "Rank 9",
        "title": "Stewarding", "title_em": "Your Influence", "role": "The witness",
        "tagline": "Everyone leads someone.",
        "hook": "Influence is a trust, not a trophy — and your people have more of it than they think.",
        "pitch": ("The witness campaign. Words, reputation, testimony, platform — the reach every person "
                  "already has and mostly underestimates. It ends by multiplying: pouring into someone else. "
                  "A quiet evangelism and leadership-pipeline series wearing everyday clothes."),
        "launch": "An outreach season, a leadership push, or a parents and marketplace emphasis.",
        "wins": "Leaders, parents, marketplace influencers, every everyday witness.",
        "verse": "Let your light shine before others.",
        "ref": "Matthew 5:16 (NIV)",
    },
    {
        "ac": "#4a3a16", "tint": "#f5f0e3", "num": "10", "rank": "Rank 10",
        "title": "Living", "title_em": "Open-Handed", "role": "The destination",
        "tagline": "Give it away.",
        "hook": "The closed fist can't receive anything either.",
        "pitch": ("The finale, and the campaign the other nine have been walking toward. Receive with "
                  "gratitude, release with joy, until generosity is a reflex rather than a decision. This is "
                  "your year-end giving series — and it never once has to guilt anyone into it."),
        "launch": "Year-end giving, a generosity emphasis, or the New Year.",
        "wins": "Everyone. The natural close of the collection.",
        "verse": "Freely you have received; freely give.",
        "ref": "Matthew 10:8 (NIV)",
    },
]

def t_html(t, em):
    t = t.strip()
    return f"{t} <em>{em}</em>" if t else f"<em>{em}</em>"

def movement(n):
    if n not in MOVEMENTS:
        return ""
    label, name, blurb = MOVEMENTS[n]
    return f"""
  <section class="movement">
    <span class="eyebrow mv-label">{label}</span>
    <h3 class="mv-name">{name}</h3>
    <p class="mv-blurb">{blurb}</p>
  </section>"""

def card(c):
    return f"""
    <article class="camp" style="--ac:{c['ac']};--tint:{c['tint']}">
      <div class="camp-band">
        <div class="camp-num">{c['num']}</div>
        <div class="camp-head">
          <span class="eyebrow role">{c['role']}</span>
          <h2 class="camp-title">{t_html(c['title'], c['title_em'])}</h2>
          <p class="tagline">{c['tagline']}</p>
        </div>
      </div>
      <div class="camp-body">
        <div class="camp-main">
          <p class="hook">{c['hook']}</p>
          <p class="pitch">{c['pitch']}</p>
          <div class="scripture">
            <p class="verse">&ldquo;{c['verse']}&rdquo;</p>
            <span class="verse-ref">{c['ref']}</span>
          </div>
        </div>
        <div class="camp-side">
          <div class="infobox">
            <ul class="info">
              <li><span class="ik">Format</span><span class="iv">40-Day Journey + 6-Session Small Group</span></li>
              <li><span class="ik">Launch It When</span><span class="iv">{c['launch']}</span></li>
              <li><span class="ik">Who It Wins</span><span class="iv">{c['wins']}</span></li>
              <li><span class="ik">Tier</span><span class="iv">Tier 1 &middot; {c['rank']} in category</span></li>
            </ul>
          </div>
        </div>
      </div>
    </article>"""

def ov_card(c):
    return f"""
      <div class="ov-card" style="--ac:{c['ac']};--tint:{c['tint']}">
        <div class="ov-num">{c['num']}</div>
        <div class="ov-body">
          <div class="ov-title">{t_html(c['title'], c['title_em'])}</div>
          <div class="ov-sub">{c['tagline']}</div>
          <div class="ov-badges"><span>40-Day</span><span>6-Session</span><span>Tier&nbsp;1</span></div>
        </div>
      </div>"""

body_sections = ""
for c in CAMPAIGNS:
    body_sections += movement(int(c["num"]))
    body_sections += card(c)

HTML = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>The Stewardship Collection &middot; Expanded Edition &middot; Lifetogether</title>
<style>
{FONT_CSS}
  :root{{ --gold:#c9a13b; --gold-lt:#dcc074; --navy:#172542; --ink:#1c1c1c; --cream:#f9f5ec; }}
  *{{box-sizing:border-box;}}
  body{{margin:0; background:#e7e2d6; color:var(--ink); font-family:'Spectral',Georgia,serif; line-height:1.6; -webkit-font-smoothing:antialiased;}}
  .page{{max-width:940px; margin:0 auto; background:#fff; box-shadow:0 1px 60px rgba(20,30,55,.14);}}
  .eyebrow{{font-family:'Archivo',sans-serif; font-weight:600; font-size:11px; letter-spacing:.28em; text-transform:uppercase;}}
  em{{font-style:italic;}}

  .cover{{background:radial-gradient(120% 90% at 78% -10%, rgba(201,161,59,.20), transparent 55%), linear-gradient(160deg,#1c2c50 0%, var(--navy) 55%, #111d36 100%); color:#f3eee2; padding:82px 70px 58px; position:relative; overflow:hidden;}}
  .cover::before{{content:""; position:absolute; left:0; right:0; top:0; height:6px; background:linear-gradient(90deg,var(--gold),var(--gold-lt));}}
  .cover .eyebrow{{color:var(--gold-lt); margin-bottom:34px;}}
  .cover h1{{font-family:'Playfair Display',serif; font-weight:700; font-size:96px; line-height:.94; margin:0 0 24px; letter-spacing:-.02em;}}
  .cover h1 em{{color:var(--gold-lt); font-weight:600;}}
  .cover .deck{{font-size:20.5px; line-height:1.55; max-width:620px; color:#e6ddc9; font-weight:300; margin:0 0 44px;}}
  .cover-strip{{display:flex; border-top:1px solid rgba(220,192,116,.32); padding-top:26px; flex-wrap:wrap;}}
  .cover-strip div{{flex:1 1 0; min-width:130px; padding:4px 22px 4px 0; border-right:1px solid rgba(220,192,116,.18);}}
  .cover-strip div:last-child{{border-right:0;}}
  .cs-big{{font-family:'Playfair Display',serif; font-size:38px; color:var(--gold-lt); line-height:1;}}
  .cs-lab{{font-family:'Archivo',sans-serif; font-size:10.5px; letter-spacing:.18em; text-transform:uppercase; color:#cdc3ac; margin-top:8px;}}

  .frame{{padding:60px 70px 56px; background:var(--cream);}}
  .frame .section-eyebrow{{color:var(--gold); margin-bottom:22px; display:block;}}
  .frame-quote{{background:var(--navy); color:#efe9da; border-radius:3px; padding:32px 40px; margin:0 0 40px; position:relative;}}
  .frame-quote::before{{content:""; position:absolute; left:0; top:0; bottom:0; width:4px; background:linear-gradient(var(--gold),var(--gold-lt));}}
  .frame-quote .boxlabel{{margin-bottom:14px; color:var(--gold-lt); display:block;}}
  .frame-quote p{{font-family:'Spectral',serif; font-style:italic; font-size:18.5px; line-height:1.62; margin:0; color:#f1ead9;}}
  .frame-intro p{{font-size:16.5px; line-height:1.72; margin:0 0 16px; color:#33312c;}}
  .frame-intro p:last-child{{margin-bottom:0;}}

  .overview{{padding:56px 70px 64px; background:#fff; page-break-after:always;}}
  .overview h3{{font-family:'Playfair Display',serif; font-weight:600; font-size:30px; margin:0 0 6px; color:var(--navy);}}
  .overview .sub{{font-size:15px; color:#6f6a5d; margin:0 0 34px; font-style:italic;}}
  .ov-grid{{display:grid; grid-template-columns:1fr 1fr; gap:16px;}}
  .ov-card{{display:flex; gap:18px; background:var(--tint); border-radius:4px; overflow:hidden; border:1px solid rgba(0,0,0,.05); break-inside:avoid;}}
  .ov-num{{flex:0 0 56px; background:var(--ac); color:#fff; font-family:'Playfair Display',serif; font-size:30px; font-weight:600; display:flex; align-items:center; justify-content:center;}}
  .ov-body{{padding:14px 18px 14px 0;}}
  .ov-title{{font-family:'Playfair Display',serif; font-size:21px; color:var(--navy); line-height:1.1;}}
  .ov-title em{{color:var(--ac);}}
  .ov-sub{{font-size:12.5px; color:#5f5a4f; margin:5px 0 9px; font-style:italic; line-height:1.4;}}
  .ov-badges span{{font-family:'Archivo',sans-serif; font-size:9px; letter-spacing:.1em; text-transform:uppercase; background:rgba(0,0,0,.06); color:#4a463d; padding:3px 8px; border-radius:20px; margin-right:5px;}}

  .movement{{background:var(--navy); color:#f1ead9; padding:44px 70px 40px; position:relative; page-break-before:always; break-before:page;}}
  .movement::before{{content:""; position:absolute; left:0; right:0; top:0; height:4px; background:linear-gradient(90deg,var(--gold),var(--gold-lt));}}
  .mv-label{{color:var(--gold-lt); display:block; margin-bottom:12px;}}
  .mv-name{{font-family:'Playfair Display',serif; font-weight:700; font-size:42px; margin:0 0 12px; line-height:1;}}
  .mv-blurb{{font-family:'Spectral',serif; font-style:italic; font-weight:300; font-size:17px; line-height:1.6; margin:0; max-width:660px; color:#ded5c1;}}

  .camp{{background:var(--tint); break-inside:avoid; page-break-inside:avoid;}}
  .camp-band{{background:var(--ac); color:#fff; padding:38px 70px 32px; display:flex; gap:26px; align-items:flex-start; position:relative; overflow:hidden;}}
  .camp-band::after{{content:""; position:absolute; left:0; right:0; bottom:0; height:4px; background:linear-gradient(90deg,var(--gold),var(--gold-lt));}}
  .camp-num{{font-family:'Playfair Display',serif; font-size:96px; font-weight:700; line-height:.8; color:rgba(255,255,255,.14); flex:0 0 auto; margin-top:-4px;}}
  .camp-head{{padding-top:6px;}}
  .role{{color:var(--gold-lt); display:block; margin-bottom:12px;}}
  .camp-title{{font-family:'Playfair Display',serif; font-weight:700; font-size:46px; margin:0 0 12px; line-height:1; letter-spacing:-.01em;}}
  .camp-title em{{color:var(--gold-lt); font-weight:600;}}
  .tagline{{font-family:'Spectral',serif; font-style:italic; font-size:17px; color:rgba(255,255,255,.84); margin:0; font-weight:300;}}
  .camp-body{{display:grid; grid-template-columns:1.55fr 1fr; gap:32px; padding:36px 70px 44px;}}
  .hook{{font-family:'Playfair Display',serif; font-style:italic; font-weight:500; font-size:24px; line-height:1.32; color:var(--ac); margin:0 0 20px; letter-spacing:-.01em;}}
  .pitch{{font-size:15.5px; line-height:1.72; margin:0; color:#322f2a;}}
  .scripture{{background:var(--ac); color:#f3eee2; border-radius:3px; padding:22px 26px; margin-top:24px;}}
  .scripture .verse{{font-family:'Spectral',serif; font-style:italic; font-size:16px; line-height:1.55; margin:0 0 10px; color:#f4eedd;}}
  .verse-ref{{font-family:'Archivo',sans-serif; font-size:10.5px; letter-spacing:.14em; text-transform:uppercase; color:var(--gold-lt);}}
  .infobox{{background:var(--ac); color:#eee; border-radius:3px; padding:22px 24px;}}
  .info{{list-style:none; margin:0; padding:0;}}
  .info li{{display:flex; flex-direction:column; padding:9px 0; border-bottom:1px solid rgba(255,255,255,.12);}}
  .info li:last-child{{border-bottom:0; padding-bottom:0;}}
  .ik{{font-family:'Archivo',sans-serif; font-size:9.5px; letter-spacing:.16em; text-transform:uppercase; color:var(--gold-lt); margin-bottom:4px;}}
  .iv{{font-size:13px; line-height:1.45; color:#f2eee4;}}

  .thru{{padding:60px 70px 56px; background:#fff; page-break-before:always;}}
  .thru h3{{font-family:'Playfair Display',serif; font-weight:600; font-size:30px; margin:0 0 6px; color:var(--navy);}}
  .thru .sub{{font-size:15px; color:#6f6a5d; margin:0 0 32px; font-style:italic;}}
  .arc{{display:grid; grid-template-columns:repeat(5,1fr); gap:10px; margin-bottom:16px;}}
  .arc-step{{background:var(--cream); border:1px solid rgba(0,0,0,.06); border-top:3px solid var(--ac); border-radius:3px; padding:14px 12px;}}
  .arc-n{{font-family:'Playfair Display',serif; font-size:24px; color:var(--ac); line-height:1; margin-bottom:7px;}}
  .arc-t{{font-family:'Archivo',sans-serif; font-size:9.5px; letter-spacing:.14em; text-transform:uppercase; color:#6f6a5d; margin-bottom:5px;}}
  .arc-d{{font-size:12.5px; line-height:1.45; color:#3d3a33;}}
  .thru-body p{{font-size:16.5px; line-height:1.72; color:#33312c; margin:22px 0 0;}}

  .close{{background:radial-gradient(110% 90% at 80% 0%, rgba(201,161,59,.16), transparent 55%), linear-gradient(160deg,#1c2c50, var(--navy) 60%, #111d36); color:#f1ebdd; padding:70px 70px 58px; position:relative;}}
  .close::before{{content:""; position:absolute; left:0; right:0; top:0; height:4px; background:linear-gradient(90deg,var(--gold),var(--gold-lt));}}
  .close h2{{font-family:'Playfair Display',serif; font-weight:700; font-size:54px; line-height:1.02; margin:0 0 22px; letter-spacing:-.015em;}}
  .close h2 em{{color:var(--gold-lt); font-weight:600;}}
  .close p{{font-size:17px; line-height:1.7; max-width:640px; color:#ded5c1; font-weight:300; margin:0 0 16px;}}
  .cta{{margin-top:34px; border-top:1px solid rgba(220,192,116,.3); padding-top:28px;}}
  .cta .eyebrow{{color:var(--gold-lt); display:block; margin-bottom:12px;}}
  .cta .cta-line{{font-family:'Playfair Display',serif; font-style:italic; font-size:22px; color:#f4eedd; margin:0;}}
  .footbar{{background:#101c33; padding:20px 70px; font-family:'Archivo',sans-serif; font-size:10px; letter-spacing:.16em; text-transform:uppercase; color:#7d8699;}}

  @media print{{
    body{{background:#fff;}}
    .page{{box-shadow:none; max-width:none;}}
    .camp, .ov-card{{page-break-inside:avoid;}}
    .cover,.close,.movement{{-webkit-print-color-adjust:exact; print-color-adjust:exact;}}
  }}
  @page{{ size:Letter; margin:0; }}
</style>
</head>
<body>
<div class="page">

  <header class="cover">
    <span class="eyebrow">Lifetogether &middot; The Stewardship Collection &middot; Expanded Edition</span>
    <h1>Nothing here<br><em>is ours.</em></h1>
    <p class="deck">The complete ten-campaign collection — every one a 40-day journey with six-session
    small-group curriculum, each taking a distinct door into the same conviction. Built for the local
    church and the workplace, rooted in Scripture, ready to launch.</p>
    <div class="cover-strip">
      <div><div class="cs-big">10</div><div class="cs-lab">Tier-One Campaigns</div></div>
      <div><div class="cs-big">40</div><div class="cs-lab">Day Journey Each</div></div>
      <div><div class="cs-big">60</div><div class="cs-lab">Small-Group Sessions</div></div>
      <div><div class="cs-big">400</div><div class="cs-lab">Daily Devotionals</div></div>
    </div>
  </header>

  <section class="frame">
    <span class="eyebrow section-eyebrow">Why a Collection, Not a Series</span>
    <div class="frame-quote">
      <span class="eyebrow boxlabel">The Pastor's Problem</span>
      <p>Most churches run one stewardship series a year, in the fall, about money — and everyone in the
      room knows what's coming before the first slide. The topic has been reduced to a budget line, and
      the discipleship in it gets lost.</p>
    </div>
    <div class="frame-intro">
      <p>These ten campaigns take stewardship back. Each one takes a distinct door into the same
      conviction — that nothing we hold is finally ours — and each stands alone as a complete churchwide
      series with a 40-day devotional journey and six weeks of small-group curriculum.</p>
      <p>Distinct doors matter. No two campaigns here share a biblical backbone or a metaphor, which means
      a church can run one every season for years without a single repeat. Run one this fall, or build a
      multi-year discipleship calendar and watch the whole idea change shape in your congregation: from an
      annual appeal into a way of life.</p>
    </div>
  </section>

  <section class="overview">
    <h3>The collection at a glance.</h3>
    <p class="sub">Ten complete campaigns — each a stand-alone 40-day journey with six-session small-group curriculum.</p>
    <div class="ov-grid">
{"".join(ov_card(c) for c in CAMPAIGNS)}
    </div>
  </section>

{body_sections}

  <section class="thru">
    <h3>The through-line for a pastor.</h3>
    <p class="sub">Ten campaigns, one deliberate progression — a multi-year discipleship calendar.</p>
    <div class="arc">
      <div class="arc-step" style="--ac:#16453a"><div class="arc-n">1</div><div class="arc-t">Reframes</div><div class="arc-d">Life Stewardship moves it off the offering plate.</div></div>
      <div class="arc-step" style="--ac:#1e2d4f"><div class="arc-n">2</div><div class="arc-t">Anchors</div><div class="arc-d">Entrusted settles the identity beneath it.</div></div>
      <div class="arc-step" style="--ac:#3a3115"><div class="arc-n">3</div><div class="arc-t">Wins</div><div class="arc-d">Stewarding What Matters takes the calendar.</div></div>
      <div class="arc-step" style="--ac:#1f3a2c"><div class="arc-n">4</div><div class="arc-t">Builds</div><div class="arc-d">Faithful Stewardship forms the character.</div></div>
      <div class="arc-step" style="--ac:#1f3550"><div class="arc-n">5</div><div class="arc-t">Lifts</div><div class="arc-d">Stewardship That Lasts opens the horizon.</div></div>
    </div>
    <div class="arc">
      <div class="arc-step" style="--ac:#15403f"><div class="arc-n">6</div><div class="arc-t">Sustains</div><div class="arc-d">Living as a Steward makes it a daily rhythm.</div></div>
      <div class="arc-step" style="--ac:#27264f"><div class="arc-n">7</div><div class="arc-t">Aims</div><div class="arc-d">Kingdom Stewardship points it at the mission.</div></div>
      <div class="arc-step" style="--ac:#3a1f3d"><div class="arc-n">8</div><div class="arc-t">Examines</div><div class="arc-d">The Stewarded Life leaves no corner out.</div></div>
      <div class="arc-step" style="--ac:#46201f"><div class="arc-n">9</div><div class="arc-t">Sends</div><div class="arc-d">Stewarding Your Influence turns it outward.</div></div>
      <div class="arc-step" style="--ac:#4a3a16"><div class="arc-n">10</div><div class="arc-t">Lands</div><div class="arc-d">Living Open-Handed is where it all arrives.</div></div>
    </div>
    <div class="thru-body">
      <p>Two or three a year covers the full arc in under four years. Run them in order and you end with a
      church that gives — without a single guilt-driven sermon.</p>
    </div>
  </section>

  <footer class="close">
    <h2>Launch the one<br><em>your church needs.</em></h2>
    <p>Every campaign arrives complete: a 40-day devotional journey, six weeks of small-group curriculum
    with discussion questions and application steps, a weekly arc your weekend messages can follow, and
    clear next steps for the day the series ends.</p>
    <p>Ten campaigns, ten distinct biblical backbones, one conviction — so the category never repeats
    itself and your people never see it coming.</p>
    <div class="cta">
      <span class="eyebrow">Bring stewardship back to your church</span>
      <p class="cta-line">Pick a door. Launch a campaign. Build a church that holds it all open-handed.</p>
    </div>
  </footer>
  <div class="footbar">Brett Eastman &middot; Founder, Lifetogether &middot; brett@lifetogether.com &middot; The Stewardship Collection &middot; Expanded Edition</div>

</div>
</body>
</html>"""

OUT_HTML = "/mnt/user-data/outputs/Stewardship_Collection_Expanded_Edition_Lifetogether.html"
OUT_PDF = "/mnt/user-data/outputs/Stewardship_Collection_Expanded_Edition_Lifetogether.pdf"
pathlib.Path(OUT_HTML).write_text(HTML, encoding="utf-8")
print("HTML written")

from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    b = p.chromium.launch(args=["--force-color-profile=srgb"])
    pg = b.new_page(viewport={"width": 940, "height": 1250})
    pg.goto(pathlib.Path(OUT_HTML).resolve().as_uri())
    pg.wait_for_timeout(3000)
    pg.emulate_media(media="print")
    pg.wait_for_timeout(1000)
    pg.pdf(path=OUT_PDF, format="Letter", print_background=True,
           margin={"top": "0", "bottom": "0", "left": "0", "right": "0"})
    b.close()
print("PDF written")
