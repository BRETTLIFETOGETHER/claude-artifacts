from shell import write

# ============================== HOW IT WORKS ==============================
H_HEAD = """
<style>
.hw-hero{padding:80px 0 64px;text-align:center}
.hw-hero .wrap{max-width:820px}
.anat{display:grid;grid-template-columns:repeat(3,1fr);gap:24px}
.an-card{background:var(--paper);border:1px solid var(--line-soft);border-radius:18px;padding:28px;box-shadow:var(--shadow)}
.an-card .ai{width:50px;height:50px;border-radius:25px 25px 9px 9px;display:flex;align-items:center;justify-content:center;font-size:20px;margin-bottom:16px}
.an-card b{display:block;font-family:var(--display);font-size:19px;font-weight:600;color:var(--ink);margin-bottom:8px}
.an-card p{font-size:14px;color:var(--body);line-height:1.6}
.fmt-tbl{display:grid;grid-template-columns:repeat(4,1fr);gap:22px}
.ft{background:var(--paper);border:1px solid var(--line-soft);border-radius:20px;padding:30px 26px;box-shadow:var(--shadow);position:relative;overflow:hidden}
.ft .big{font-family:var(--display);font-size:44px;font-weight:600;color:var(--ink);line-height:1}
.ft .fname{font-size:11.5px;font-weight:800;letter-spacing:.16em;text-transform:uppercase;color:var(--green-deep);display:block;margin:8px 0 14px}
.ft p{font-size:13.5px;color:var(--body);line-height:1.6}
.ft .use{margin-top:14px;font-size:12px;font-weight:650;color:var(--mute)}
.arc{display:grid;grid-template-columns:repeat(5,1fr);gap:0;position:relative;margin-top:44px}
.arc::before{content:'';position:absolute;top:26px;left:9%;right:9%;height:2px;background:rgba(255,255,255,.2)}
.ph{text-align:center;position:relative;padding:0 12px}
.ph .pnum{width:52px;height:52px;border-radius:26px 26px 8px 8px;margin:0 auto 16px;position:relative;z-index:1;display:flex;align-items:center;justify-content:center;font-family:var(--display);font-weight:650;font-size:19px;color:#14352A;background:#E8D9AE}
.ph b{display:block;font-size:15px;color:#F4EFE0;margin-bottom:6px}
.ph span{font-size:12.5px;color:#B9C9BB;line-height:1.5}
.launch{display:grid;grid-template-columns:repeat(4,1fr);gap:0;position:relative}
.launch::before{content:'';position:absolute;top:23px;left:11%;right:11%;height:2px;background:var(--line)}
.lw{text-align:center;padding:0 14px;position:relative}
.lw .wk{width:46px;height:46px;border-radius:23px 23px 8px 8px;margin:0 auto 14px;background:var(--green-tint);color:var(--green-deep);font-weight:700;font-size:13px;display:flex;align-items:center;justify-content:center;position:relative;z-index:1}
.lw b{display:block;font-size:14.5px;color:var(--ink);margin-bottom:5px}
.lw span{font-size:12.5px;color:var(--body);line-height:1.5}
.faq{max-width:820px;margin:0 auto;display:flex;flex-direction:column;gap:14px}
.fq{background:var(--paper);border:1px solid var(--line-soft);border-radius:16px;overflow:hidden}
.fq summary{cursor:pointer;list-style:none;padding:20px 26px;font-size:16px;font-weight:650;color:var(--ink);display:flex;justify-content:space-between;align-items:center;gap:14px}
.fq summary::-webkit-details-marker{display:none}
.fq summary::after{content:'+';font-family:var(--display);font-size:22px;color:var(--green);transition:transform .25s}
.fq[open] summary::after{transform:rotate(45deg)}
.fq .fa{padding:0 26px 22px;font-size:14.5px;color:var(--body);line-height:1.7}
@media(max-width:1080px){.anat{grid-template-columns:1fr}.fmt-tbl{grid-template-columns:repeat(2,1fr)}.arc,.launch{grid-template-columns:1fr;gap:22px}.arc::before,.launch::before{display:none}}
@media(max-width:560px){.fmt-tbl{grid-template-columns:1fr}}
</style>
"""

H_BODY = """
<section class="hw-hero">
  <div class="wrap">
    <span class="eyebrow bare">How It Works</span>
    <h1 class="mt16">A campaign is a church,<br><em>aligned</em>.</h1>
    <p class="lede mt24" style="margin:24px auto 0">For forty days — or thirty, or twenty-one, or seven — the pulpit, the groups, and every daily reading point at the same truth. That alignment is the method behind the largest churchwide movements in history, and it&rsquo;s what every Lifetogether campaign delivers out of the box.</p>
  </div>
</section>

<section class="band-white tight">
  <div class="wrap">
    <div class="sec-head">
      <span class="eyebrow">The anatomy of a campaign</span>
      <h2>Three streams.<br>One <em>current</em>.</h2>
    </div>
    <div class="anat">
      <div class="an-card rv"><span class="ai" style="background:var(--green-tint);color:var(--green-deep)">⛪</span><b>The pulpit</b><p>Complete weekend message builds — title, texts, preaching ideas, and outline — for every week of the campaign. Preached in your voice, never ours.</p></div>
      <div class="an-card rv"><span class="ai" style="background:#EFEDFA;color:#5A53B8">◉</span><b>The groups</b><p>Session-by-session guides with discussion, practice, and prayer — plus a Leader Kit that recruits, trains, and cares for hosts in one evening.</p></div>
      <div class="an-card rv"><span class="ai" style="background:var(--gold-tint);color:var(--gold-deep)">☀</span><b>The daily reading</b><p>Ten minutes a morning in every participant&rsquo;s hands — adult, youth, and family editions of the same journey, at the same table.</p></div>
    </div>
  </div>
</section>

<section class="tight">
  <div class="wrap">
    <div class="sec-head">
      <span class="eyebrow">Four formats</span>
      <h2>Choose the <em>commitment</em>,<br>not just the topic.</h2>
    </div>
    <div class="fmt-tbl">
      <div class="ft rv"><span class="big">7</span><span class="fname">The Taste</span><p>One week to sample a theme with almost no barrier to entry.</p><p class="use">Use it for: post-assessment starts, sermon-series companions, first-time participants.</p></div>
      <div class="ft rv"><span class="big">21</span><span class="fname">The Habit</span><p>Three weeks — the shortest arc that reliably changes a daily rhythm.</p><p class="use">Use it for: prayer, Scripture, and practice-forming journeys.</p></div>
      <div class="ft rv"><span class="big">30</span><span class="fname">The Month</span><p>A full month of formation that fits calendar seasons cleanly.</p><p class="use">Use it for: Lent, stewardship month, group semesters.</p></div>
      <div class="ft rv"><span class="big">40</span><span class="fname">The Movement</span><p>The classic churchwide campaign — the format that made the movement.</p><p class="use">Use it for: fall &amp; new-year launches, vision seasons, whole-church alignment.</p></div>
    </div>
  </div>
</section>

<section class="band-ink tight">
  <div class="wrap">
    <div class="sec-head">
      <span class="eyebrow" style="color:#C9A45A">The daily arc</span>
      <h2>Five phases inside every journey.</h2>
      <p class="lede">The same architecture certified across all 383 flagship campaigns — so a first-timer and a forty-year believer can walk the same road at the same time.</p>
    </div>
    <div class="arc">
      <div class="ph rv"><span class="pnum">1</span><b>Invitation</b><span>A gentle on-ramp. Presence over readiness.</span></div>
      <div class="ph rv"><span class="pnum">2</span><b>Foundations</b><span>The scriptural backbone, one text at a time.</span></div>
      <div class="ph rv"><span class="pnum">3</span><b>Practice</b><span>Truth becomes habit — small and repeatable.</span></div>
      <div class="ph rv"><span class="pnum">4</span><b>Perseverance</b><span>When novelty fades, formation begins.</span></div>
      <div class="ph rv"><span class="pnum">5</span><b>Commissioning</b><span>Sent, not finished. The next season named.</span></div>
    </div>
  </div>
</section>

<section class="band-white tight">
  <div class="wrap">
    <div class="sec-head">
      <span class="eyebrow">The launch rhythm</span>
      <h2>Six weeks from decision<br>to <em>Day One</em>.</h2>
    </div>
    <div class="launch">
      <div class="lw rv"><span class="wk">-6</span><b>Decide &amp; date</b><span>Pick the campaign and the Sunday it starts. Everything counts back from there.</span></div>
      <div class="lw rv"><span class="wk">-4</span><b>Recruit hosts</b><span>The Leader Kit&rsquo;s scripts and one-evening training turn members into hosts.</span></div>
      <div class="lw rv"><span class="wk">-2</span><b>Sign up the church</b><span>Two weekends of invitation — groups, devotionals, and family editions in hand.</span></div>
      <div class="lw rv"><span class="wk">0</span><b>Launch Sunday</b><span>The first message lands, Day One begins next morning — and it ends, forty days later, at Celebration Sunday.</span></div>
    </div>
  </div>
</section>

<section class="tight">
  <div class="wrap">
    <div class="sec-head center">
      <span class="eyebrow bare">Questions pastors ask</span>
      <h2>Asked. <em>Answered.</em></h2>
    </div>
    <div class="faq">
      <details class="fq rv"><summary>Do we have to use your sermons?</summary><p class="fa">No. Every campaign ships complete message builds, but they are raw material for your voice — outlines, texts, and preaching ideas, not scripts. And with the pastor tools, the platform runs the other direction too: your own series becomes the campaign.</p></details>
      <details class="fq rv"><summary>What if our church already has a series planned?</summary><p class="fa">That&rsquo;s the Create door. Upload the series and the platform builds the group curriculum, devotionals, and campaign structure around your teaching — your words visibly marked throughout. Start at <a href="create.html" style="color:var(--green-deep);font-weight:650">For Pastors &amp; Leaders</a>.</p></details>
      <details class="fq rv"><summary>How much production work lands on our staff?</summary><p class="fa">Almost none. Devotionals, group guides, leader kits, family editions, and graphics arrive finished — print and digital masters included. Your team&rsquo;s job is invitation and shepherding, not assembly.</p></details>
      <details class="fq rv"><summary>What about languages?</summary><p class="fa">English today, with Spanish and Portuguese editions rolling out across the flagship shelf — same campaigns, same days, one congregation in three languages.</p></details>
      <details class="fq rv"><summary>What translation do you use?</summary><p class="fa">The NIV is our scripture standard throughout, used by permission of Biblica. Every verse reference in every campaign is verse-bound and machine-audited — no paraphrased claims wearing a reference they didn&rsquo;t earn.</p></details>
    </div>
  </div>
</section>

<section class="band-green tight">
  <div class="wrap" style="display:flex;justify-content:space-between;align-items:center;gap:26px;flex-wrap:wrap">
    <div>
      <h2 style="font-size:clamp(26px,3.2vw,38px)">See it, don&rsquo;t just read about it.</h2>
      <p class="lede" style="color:#DCEBDD">Walk Day One of a flagship campaign right now — free, no account.</p>
    </div>
    <a class="btn btn-gold btn-lg" href="reader.html?a=community&c=life-together&f=40">Preview Day One <span class="arrow">→</span></a>
  </div>
</section>
"""

write("how-it-works.html", "How It Works — Campaigns, Formats & the Daily Arc | Lifetogether", H_BODY, active="how", head=H_HEAD)


# ============================== PRICING ==============================
P_HEAD = """
<style>
.pr-hero{padding:80px 0 56px;text-align:center}
.pr-hero .wrap{max-width:780px}
.tiers{display:grid;grid-template-columns:repeat(3,1fr);gap:24px;align-items:stretch}
.tier{background:var(--paper);border:1.5px solid var(--line-soft);border-radius:22px;padding:36px 32px;display:flex;flex-direction:column;box-shadow:var(--shadow);position:relative}
.tier.hot{border-color:var(--green);box-shadow:0 24px 60px rgba(35,122,82,.16)}
.tier .pop{position:absolute;top:-14px;left:50%;transform:translateX(-50%)}
.tier .tname{font-family:var(--display);font-size:23px;font-weight:600;color:var(--ink)}
.tier .tfor{font-size:13px;color:var(--mute);margin:4px 0 20px}
.tier .price{font-family:var(--display);font-size:52px;font-weight:600;color:var(--ink);line-height:1}
.tier .per{font-size:13px;color:var(--mute);margin:6px 0 24px}
.tier ul{list-style:none;display:flex;flex-direction:column;gap:11px;margin-bottom:28px}
.tier li{font-size:14px;color:var(--body);display:flex;gap:10px;align-items:flex-start;line-height:1.5}
.tier li::before{content:'✓';color:var(--green);font-weight:700;flex-shrink:0}
.tier li.plus::before{content:'+';color:var(--gold-deep)}
.tier .btn{margin-top:auto;justify-content:center}
.alt{display:grid;grid-template-columns:1fr 1fr;gap:24px;margin-top:26px}
.alt-card{background:var(--paper);border:1.5px dashed var(--line);border-radius:20px;padding:30px 32px;display:flex;justify-content:space-between;align-items:center;gap:20px;flex-wrap:wrap}
.alt-card b{font-family:var(--display);font-size:20px;font-weight:600;color:var(--ink);display:block;margin-bottom:5px}
.alt-card span{font-size:13.5px;color:var(--body)}
.guarantee{display:flex;gap:18px;align-items:center;background:linear-gradient(150deg,#EDF4EA,#F8F3E3);border-radius:20px;padding:28px 34px;margin-top:40px}
.guarantee .gi{width:58px;height:58px;flex-shrink:0;border-radius:29px 29px 10px 10px;background:var(--green);color:#fff;display:flex;align-items:center;justify-content:center;font-size:24px}
.guarantee b{font-family:var(--display);font-size:19px;color:var(--ink);display:block;margin-bottom:4px}
.guarantee span{font-size:14px;color:var(--body)}
@media(max-width:1080px){.tiers{grid-template-columns:1fr}.alt{grid-template-columns:1fr}}
</style>
"""

P_BODY = """
<section class="pr-hero">
  <div class="wrap">
    <span class="eyebrow bare">Pricing</span>
    <h1 class="mt16">Priced for the church<br>of <em>150</em> — and 15,000.</h1>
    <p class="lede mt24" style="margin:24px auto 0">Every plan includes the full flagship library and every edition of every campaign. What scales is your congregation — and how deep the platform&rsquo;s intelligence goes.</p>
    <p class="mt24"><span class="chip gold">★ Founding church pricing — locked for life</span></p>
  </div>
</section>

<section class="band-white tight">
  <div class="wrap">
    <div class="tiers">
      <div class="tier rv">
        <span class="tname">Starter</span><span class="tfor">Churches up to 150</span>
        <span class="price">$49</span><span class="per">per month · billed annually</span>
        <ul>
          <li>Full flagship library — all 383 campaigns</li>
          <li>All four formats · 7 / 21 / 30 / 40</li>
          <li>Adult edition, digital delivery</li>
          <li>Group guides &amp; leader kits</li>
          <li>Weekend message builds</li>
        </ul>
        <a class="btn btn-outline" href="about.html#contact">Start with Starter</a>
      </div>
      <div class="tier hot rv">
        <span class="pop chip" style="background:var(--green);color:#fff">Most churches choose this</span>
        <span class="tname">Standard</span><span class="tfor">Churches up to 750</span>
        <span class="price">$149</span><span class="per">per month · billed annually</span>
        <ul>
          <li>Everything in Starter</li>
          <li class="plus">Youth &amp; Children/Family editions</li>
          <li class="plus">Print masters &amp; graphics packs</li>
          <li class="plus">Seasonal planner &amp; launch tools</li>
          <li class="plus">Member assessment &amp; personal paths</li>
        </ul>
        <a class="btn btn-primary" href="about.html#contact">Start with Standard</a>
      </div>
      <div class="tier rv">
        <span class="tname">Complete</span><span class="tfor">Unlimited congregation size</span>
        <span class="price">$249</span><span class="per">per month · billed annually</span>
        <ul>
          <li>Everything in Standard</li>
          <li class="plus">Pastor content transformation — sermons into curriculum</li>
          <li class="plus">Church-branded editions</li>
          <li class="plus">Spanish &amp; Portuguese as released</li>
          <li class="plus">Priority support &amp; launch coaching</li>
        </ul>
        <a class="btn btn-outline" href="about.html#contact">Start with Complete</a>
      </div>
    </div>
    <div class="alt">
      <div class="alt-card rv">
        <div><b>Single Campaign License</b><span>One flagship campaign, every edition, one launch — no subscription.</span></div>
        <div style="text-align:right"><span class="price" style="font-size:34px">$499</span><br><a class="btn btn-outline btn-sm mt8" href="about.html#contact">License one campaign</a></div>
      </div>
      <div class="alt-card rv">
        <div><b>Networks &amp; Denominations</b><span>Multi-church libraries, shared reporting, co-branded editions — built with you.</span></div>
        <a class="btn btn-ink" href="about.html#contact">Talk with our team</a>
      </div>
    </div>
    <div class="guarantee rv">
      <span class="gi">✓</span>
      <div><b>The 30-day launch guarantee</b><span>Launch any campaign. If your church isn&rsquo;t seeing groups form and people walking daily within thirty days, we&rsquo;ll refund the month and help you re-plan the launch — free.</span></div>
    </div>
    <p class="small mt24" style="text-align:center">Prototype pricing shown for review — final tiers configured with Stripe at launch.</p>
  </div>
</section>
"""

write("pricing.html", "Pricing — Plans for Every Church | Lifetogether", P_BODY, active="pricing", head=P_HEAD)


# ============================== ABOUT ==============================
A_HEAD = """
<style>
.ab-hero{padding:84px 0 70px}
.ab-hero .wrap{display:grid;grid-template-columns:1.1fr .9fr;gap:60px;align-items:center}
.ab-story p{font-size:16.5px;line-height:1.8;color:#3B4A41;margin-bottom:20px}
.ab-story p b{color:var(--ink)}
.tl{position:relative;padding-left:34px;display:flex;flex-direction:column;gap:26px}
.tl::before{content:'';position:absolute;left:8px;top:8px;bottom:8px;width:2px;background:var(--line)}
.tl-item{position:relative}
.tl-item::before{content:'';position:absolute;left:-32px;top:5px;width:14px;height:14px;border-radius:7px 7px 3px 3px;background:var(--green)}
.tl-item.gold::before{background:var(--gold)}
.tl-item .yr{font-family:var(--display);font-size:18px;font-weight:650;color:var(--ink)}
.tl-item p{font-size:14px;color:var(--body);line-height:1.6;margin-top:4px}
.tsti-feature{background:var(--paper);border:1px solid var(--line-soft);border-radius:28px;box-shadow:var(--shadow);padding:48px 54px;display:grid;grid-template-columns:auto 1fr;gap:38px;align-items:center;margin-bottom:26px}
.tsti-feature .avatar{width:92px;height:92px;border-radius:46px 46px 13px 13px;background:linear-gradient(140deg,#237A52,#2E8A5F);display:flex;align-items:center;justify-content:center;font-family:var(--display);font-size:32px;font-weight:600;color:#EAF4E8}
.tsti-feature blockquote{font-family:var(--display);font-style:italic;font-weight:520;font-size:clamp(19px,2vw,24px);line-height:1.5;color:var(--ink)}
.tsti-feature cite{display:block;font-style:normal;font-family:var(--ui);font-size:12px;font-weight:700;letter-spacing:.14em;text-transform:uppercase;color:var(--mute);margin-top:16px}
.tgrid{display:grid;grid-template-columns:repeat(2,1fr);gap:24px}
.tcard{background:var(--paper);border:1px solid var(--line-soft);border-radius:20px;padding:30px 30px;box-shadow:var(--shadow)}
.tcard p{font-size:14.5px;line-height:1.7;color:var(--body)}
.tcard cite{display:flex;align-items:center;gap:12px;font-style:normal;margin-top:18px}
.tcard .avatar{width:42px;height:42px;border-radius:21px 21px 8px 8px;flex-shrink:0;display:flex;align-items:center;justify-content:center;font-family:var(--display);font-weight:600;font-size:16px;color:#fff}
.tcard b{display:block;font-size:14px;color:var(--ink)}
.tcard span{font-size:12px;color:var(--mute)}
.logo-row{display:flex;flex-wrap:wrap;justify-content:center;gap:14px 40px;margin-top:26px}
.logo-row span{font-family:var(--display);font-size:19px;font-weight:600;color:#9AA79A}
.three{display:grid;grid-template-columns:repeat(3,1fr);gap:24px}
.tc{background:rgba(255,255,255,.06);border:1px solid rgba(255,255,255,.12);border-radius:18px;padding:28px}
.tc b{font-family:var(--display);font-size:19px;color:#F4EFE0;display:block;margin-bottom:8px}
.tc p{font-size:13.5px;color:#B9C9BB;line-height:1.6}
.contact{background:var(--paper);border:1px solid var(--line-soft);border-radius:24px;box-shadow:var(--shadow);padding:44px;display:grid;grid-template-columns:1fr 1fr;gap:44px;align-items:center}
.contact .cline{display:flex;gap:13px;align-items:center;font-size:15px;color:var(--body);margin-top:14px}
.contact .cline i{width:38px;height:38px;flex-shrink:0;border-radius:19px 19px 7px 7px;background:var(--green-tint);color:var(--green-deep);display:flex;align-items:center;justify-content:center;font-style:normal}
@media(max-width:1080px){.tgrid{grid-template-columns:1fr}.three{grid-template-columns:1fr}}
@media(max-width:920px){.ab-hero .wrap,.contact{grid-template-columns:1fr}.tsti-feature{grid-template-columns:1fr;padding:34px 28px;gap:20px}}
</style>
"""

A_BODY = """
<section class="ab-hero">
  <div class="wrap">
    <div class="ab-story">
      <span class="eyebrow">Our Story &amp; Heritage</span>
      <h1 class="mt16" style="font-size:clamp(36px,4.6vw,54px)">Bringing your message<br>to life — for <em>25 years</em>.</h1>
      <p class="mt24">Lifetogether was founded by <b>Brett Eastman</b> out of the small group ministries of <b>Saddleback Church</b> and <b>Willow Creek</b> — the two congregations that redefined what a local church could be. There, one conviction took hold and never let go: <b>transformation happens in circles, not rows.</b></p>
      <p>That conviction became the engine of the <b>Purpose Driven</b> campaign era — including <b>40 Days of Purpose</b>, the largest churchwide campaign movement in history — and a body of work that has helped move <b>millions of people into small groups</b> across more than five hundred church partnerships.</p>
      <p>For two decades we did that work church by church: consulting, publishing, and production. Now the entire methodology — the campaign architecture, the launch rhythms, the group systems, the library — lives in one intelligent platform any church can pick up on a Tuesday.</p>
    </div>
    <div class="tl rv">
      <div class="tl-item"><span class="yr">1997</span><p>Brett leads small group ministry at Willow Creek, then Saddleback — building the largest group systems in the country.</p></div>
      <div class="tl-item gold"><span class="yr">2002</span><p><b>40 Days of Purpose</b> launches — the campaign that proved a whole church can walk one road together.</p></div>
      <div class="tl-item"><span class="yr">2004</span><p>Lifetogether forms. The <i>Doing Life Together</i> series becomes a small-group standard; 500+ partnerships follow.</p></div>
      <div class="tl-item"><span class="yr">2010s</span><p>Consulting · Publishing · Production — 27 published case studies across churches of every size.</p></div>
      <div class="tl-item gold"><span class="yr">2026</span><p><b>The Lifetogether platform.</b> Twenty-five years of method, one intelligent system — find, personalize, create.</p></div>
    </div>
  </div>
</section>

<section class="band-ink tight">
  <div class="wrap">
    <div class="sec-head">
      <span class="eyebrow" style="color:#C9A45A">What we&rsquo;ve always done</span>
      <h2>Three crafts. Now one platform.</h2>
    </div>
    <div class="three">
      <div class="tc rv"><b>Consulting</b><p>Launch strategy, leadership pipelines, and campaign coaching — the playbook from five hundred launches, now built into every plan.</p></div>
      <div class="tc rv"><b>Publishing</b><p>Devotionals, curriculum, and group guides — a library of over a thousand titles led by 383 hand-finished flagships.</p></div>
      <div class="tc rv"><b>Production</b><p>The design, media, and message-craft that made campaigns feel like movements — applied to every edition we ship.</p></div>
    </div>
  </div>
</section>

<section class="band-white tight" id="stories">
  <div class="wrap">
    <div class="sec-head center">
      <span class="eyebrow bare">Church stories</span>
      <h2>In <em>their</em> words.</h2>
    </div>
    <div class="tsti-feature rv">
      <div class="avatar">RW</div>
      <div>
        <blockquote>&ldquo;When it comes to the dream-it-up phase of a project — where you imagine the possibilities, consider the alternatives, and produce a scenario for communicating your message in a compelling way — I&rsquo;ve never met anyone who can match Brett&rsquo;s genius.&rdquo;</blockquote>
        <cite>Rick Warren · Saddleback Church</cite>
      </div>
    </div>
    <div class="tgrid">
      <div class="tcard rv"><p>&ldquo;Lifetogether is not just the name of an organization. It&rsquo;s what they do. Brett Eastman and his team have come alongside us to produce better leaders, more polished curriculum, stronger groups — and, maybe best of all, lots more groups. We are grateful for their partnership.&rdquo;</p>
        <cite><span class="avatar" style="background:var(--c-work)">GA</span><span><b>Gene Appel</b><span>Eastside Christian Church</span></span></cite></div>
      <div class="tcard rv"><p>&ldquo;Brett&rsquo;s ministry, heart, and skills made it possible for us to quadruple our small-group involvement. He is a competent and hands-on coach with the sensitivity necessary to make it all come together.&rdquo;</p>
        <cite><span class="avatar" style="background:var(--c-mission)">WC</span><span><b>Wayne Cordeiro</b><span>New Hope Christian Fellowship, Oahu</span></span></cite></div>
      <div class="tcard rv"><p>&ldquo;We always felt bad about the low numbers of people we had connected in groups. But we had the excuse of rapid growth and never thought it was possible to keep up. Until Lifetogether. Now we can almost make the ridiculous claim that we have as many people connected in groups as we have attending in a given weekend.&rdquo;</p>
        <cite><span class="avatar" style="background:var(--c-freedom)">TH</span><span><b>Tim Harlow</b><span>Parkview Christian Church</span></span></cite></div>
      <div class="tcard rv"><p>&ldquo;I am a big fan of Brett Eastman and Lifetogether because he has helped me, as the pastor of a large church, to connect with our faith family in deep and significant ways. He has made the difficult possible.&rdquo;</p>
        <cite><span class="avatar" style="background:var(--c-parenting)">DO</span><span><b>Dale Oquist</b><span>Peoples Church</span></span></cite></div>
    </div>
    <p class="small center mt24">Twenty-seven full case studies available on request.</p>
    <div class="logo-row rv">
      <span>Saddleback</span><span>Willow Creek</span><span>Oak Hills</span><span>Mariners</span><span>Seacoast</span>
      <span>Church of the Highlands</span><span>Bayside</span><span>Parkview</span><span>NewSpring</span><span>Rock Church</span>
    </div>
  </div>
</section>

<section class="tight" id="contact">
  <div class="wrap">
    <div class="contact rv">
      <div>
        <span class="eyebrow">Let&rsquo;s talk about your church</span>
        <h2 class="mt16" style="font-size:clamp(26px,3.2vw,38px)">Schedule a call with our team.</h2>
        <p class="lede mt16">Thirty minutes. Bring your calendar and your next teaching series — we&rsquo;ll leave you with a launch date and a plan, whether or not you ever subscribe.</p>
        <div class="cline"><i>✉</i><a href="mailto:contact@lifetogether.com" style="color:var(--green-deep);font-weight:650">contact@lifetogether.com</a></div>
        <div class="cline"><i>☏</i><span>949-769-0777</span></div>
        <div class="cline"><i>⌂</i><span>27132A Paseo Espada, Suite 423 · San Juan Capistrano, CA 92675</span></div>
      </div>
      <div>
        <label class="lbl">Your name</label>
        <input class="input" placeholder="First and last name">
        <label class="lbl mt16">Church &amp; role</label>
        <input class="input" placeholder="Grace Community · Lead Pastor">
        <label class="lbl mt16">What are you hoping to launch?</label>
        <textarea class="input" rows="3" placeholder="A fall campaign, a groups relaunch, our own sermon series…"></textarea>
        <button class="btn btn-primary btn-lg mt24" style="width:100%;justify-content:center" onclick="this.textContent='Request received — we\\u2019ll reply within one business day.';this.disabled=true">Request the call</button>
        <p class="small mt8" style="text-align:center">Prototype form — submissions connect at launch.</p>
      </div>
    </div>
  </div>
</section>
"""

write("about.html", "Our Story — 25 Years of Churchwide Campaigns | Lifetogether", A_BODY, active="about", head=A_HEAD)
