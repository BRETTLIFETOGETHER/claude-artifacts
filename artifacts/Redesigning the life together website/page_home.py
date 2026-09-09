from shell import write

HEAD = """
<style>
/* ---------- hero ---------- */
.hero{padding:84px 0 74px;position:relative;overflow:hidden}
.hero .wrap{display:grid;grid-template-columns:1.08fr .92fr;gap:56px;align-items:center}
.hero h1{margin:20px 0 22px}
.hero .lede{margin-bottom:34px}
.hero-ctas{display:flex;gap:14px;flex-wrap:wrap;align-items:center}
.hero-quiet{margin-top:20px;font-size:14.5px;color:var(--mute)}
.hero-quiet a{color:var(--green-deep);font-weight:600;border-bottom:1.5px solid rgba(35,122,82,.3)}
.hero-quiet a:hover{border-color:var(--green)}
/* fanned covers */
.fan{position:relative;height:520px}
.fan .fc{position:absolute;width:250px;border-radius:125px 125px 14px 14px;overflow:hidden;
  box-shadow:0 30px 70px rgba(20,53,42,.22);border:5px solid #fff;background:#fff;
  transition:transform .5s var(--ease)}
.fan .fc .cover{aspect-ratio:4/4.9}
.fan .fc1{left:0;top:60px;transform:rotate(-7deg);z-index:1}
.fan .fc2{left:150px;top:8px;z-index:3;width:270px}
.fan .fc3{left:320px;top:74px;transform:rotate(7deg);z-index:2}
.fan:hover .fc1{transform:rotate(-9.5deg) translateY(-6px)}
.fan:hover .fc3{transform:rotate(9.5deg) translateY(-6px)}
.fan .halo{position:absolute;inset:-40px -20px auto;height:560px;z-index:0;
  background:radial-gradient(closest-side,rgba(196,147,60,.16),transparent 70%)}
/* stat strip */
.stats{display:grid;grid-template-columns:repeat(4,1fr);gap:22px;margin-top:66px;
  border-top:1px solid var(--line);padding-top:34px}
.stats b{font-family:var(--display);font-size:34px;font-weight:600;color:var(--ink);display:block;line-height:1}
.stats span{font-size:11.5px;font-weight:700;letter-spacing:.14em;text-transform:uppercase;color:var(--mute)}
.stats .st{display:flex;flex-direction:column;gap:8px}
/* ---------- partners ---------- */
.partners{padding:44px 0 50px;border-top:1px solid var(--line-soft)}
.partners p{font-size:11.5px;font-weight:700;letter-spacing:.2em;text-transform:uppercase;color:var(--mute);text-align:center;margin-bottom:26px}
.logo-row{display:flex;flex-wrap:wrap;justify-content:center;gap:14px 40px}
.logo-row span{font-family:var(--display);font-size:19px;font-weight:600;color:#9AA79A;letter-spacing:.01em;transition:color .25s}
.logo-row span:hover{color:var(--ink)}
/* ---------- doors ---------- */
.doors{display:grid;grid-template-columns:repeat(3,1fr);gap:28px}
.door{border-radius:var(--arch) var(--arch) var(--r) var(--r);padding:150px 30px 34px;position:relative;
  overflow:hidden;display:flex;flex-direction:column;gap:12px;min-height:430px;
  transition:transform .3s var(--ease),box-shadow .3s;box-shadow:var(--shadow)}
.door:hover{transform:translateY(-7px);box-shadow:var(--shadow-lg)}
.door .dtag{font-size:11px;font-weight:800;letter-spacing:.22em}
.door h3{font-size:27px;line-height:1.15}
.door p{font-size:15px;line-height:1.6}
.door .dlink{margin-top:auto;font-weight:700;font-size:14.5px;display:inline-flex;gap:8px;align-items:center}
.door .dlink .arrow{transition:transform .2s var(--ease)}
.door:hover .dlink .arrow{transform:translateX(5px)}
.door .dart{position:absolute;top:0;left:0;right:0;height:150px;pointer-events:none}
.door-find{background:linear-gradient(180deg,#E7F1E6,#F7FBF4);border:1px solid #D7E6D4}
.door-find h3,.door-find .dlink{color:var(--green-deep)}.door-find .dtag{color:#5F8F6C}.door-find p{color:#3E5A48}
.door-path{background:linear-gradient(180deg,#EAE8F8,#F8F7FD);border:1px solid #DBD8F0}
.door-path h3,.door-path .dlink{color:#4A44A8}.door-path .dtag{color:#7A75C4}.door-path p{color:#4A4B6E}
.door-create{background:linear-gradient(180deg,#F7ECD8,#FCF8EE);border:1px solid #EBDDBE}
.door-create h3,.door-create .dlink{color:var(--gold-deep)}.door-create .dtag{color:#B08A45}.door-create p{color:#5E4E2E}
/* ---------- personalize preview ---------- */
.pp{display:grid;grid-template-columns:1fr 1.05fr;gap:60px;align-items:center}
.sampler{background:var(--paper);border:1px solid var(--line-soft);border-radius:26px;box-shadow:var(--shadow-lg);padding:36px}
.sampler .sq{padding:18px 0;border-bottom:1px solid var(--line-soft)}
.sampler .sq:first-of-type{padding-top:4px}
.sampler .sq:last-of-type{border:0}
.sampler .qq{font-size:15.5px;font-weight:600;color:var(--ink);margin-bottom:13px;line-height:1.45}
.scale{display:flex;gap:8px}
.scale button{flex:1;height:42px;border-radius:11px;border:1.5px solid var(--line);background:var(--ivory);
  font-size:13px;font-weight:650;color:var(--mute);transition:all .16s var(--ease)}
.scale button:hover{border-color:#B7A9E0;color:#5A53B8}
.scale button.sel{background:#6A63CF;border-color:#6A63CF;color:#fff;box-shadow:0 5px 14px rgba(106,99,207,.32)}
.scale-lbls{display:flex;justify-content:space-between;font-size:10.5px;font-weight:700;letter-spacing:.1em;text-transform:uppercase;color:var(--mute);margin-top:8px}
.sampler .sdone{display:none;margin-top:22px;background:#F1EFFB;border-radius:14px;padding:18px 20px;font-size:14.5px;color:#45407E;line-height:1.55}
.sampler .sdone.show{display:block;animation:pop .5s var(--ease)}
@keyframes pop{from{opacity:0;transform:translateY(8px)}to{opacity:1;transform:none}}
/* ---------- create preview ---------- */
.cp{display:grid;grid-template-columns:1.05fr 1fr;gap:60px;align-items:center}
.steps4{display:flex;flex-direction:column;gap:0}
.stp{display:flex;gap:20px;padding:20px 0;position:relative}
.stp .num{width:46px;height:46px;flex-shrink:0;border-radius:50% 50% 8px 8px;background:var(--gold-tint);
  color:var(--gold-deep);font-family:var(--display);font-weight:650;font-size:19px;
  display:flex;align-items:center;justify-content:center}
.stp:not(:last-child)::before{content:'';position:absolute;left:23px;top:66px;bottom:0;width:2px;background:var(--line)}
.stp b{display:block;font-size:16.5px;font-weight:700;color:var(--ink);margin-bottom:4px}
.stp span{font-size:14.5px;color:var(--body)}
/* mini curriculum mock */
.mock{background:var(--paper);border:1px solid var(--line-soft);border-radius:22px;box-shadow:var(--shadow-lg);overflow:hidden}
.mock-head{background:linear-gradient(120deg,#F5EBD4,#FBF5E6);padding:22px 26px;border-bottom:1px solid var(--line-soft)}
.mock-head .chip{margin-bottom:9px}
.mock-head b{font-family:var(--display);font-size:21px;font-weight:600;color:var(--ink);display:block;line-height:1.25}
.mock-head span{font-size:12.5px;color:var(--mute)}
.mock-body{padding:22px 26px;display:flex;flex-direction:column;gap:13px}
.mline{display:flex;gap:11px;align-items:flex-start;font-size:13.5px;color:var(--body)}
.mline i{width:8px;height:8px;border-radius:50%;background:var(--gold);flex-shrink:0;margin-top:6px;font-style:normal}
.mline .yw{background:#F6ECD4;border-radius:6px;padding:0 6px;color:var(--gold-deep);font-weight:600;font-size:12px;white-space:nowrap}
/* ---------- shelf ---------- */
.shelf{display:grid;grid-template-columns:repeat(4,1fr);gap:26px}
.shelf-head{display:flex;justify-content:space-between;align-items:flex-end;gap:20px;margin-bottom:46px;flex-wrap:wrap}
/* ---------- formats ---------- */
.fmt{display:grid;grid-template-columns:repeat(4,1fr);gap:24px}
.fmt-card{background:rgba(255,255,255,.07);border:1px solid rgba(255,255,255,.13);border-radius:20px;padding:30px 26px;transition:background .25s,transform .25s var(--ease)}
.fmt-card:hover{background:rgba(255,255,255,.11);transform:translateY(-4px)}
.fmt-card b{font-family:var(--display);font-size:46px;font-weight:600;color:#fff;line-height:1;display:block}
.fmt-card .fname{font-size:12px;font-weight:800;letter-spacing:.18em;text-transform:uppercase;color:#E3C88A;margin:10px 0 12px;display:block}
.fmt-card p{font-size:14px;color:#CFE0D0;line-height:1.55}
/* ---------- heritage ---------- */
.her{display:grid;grid-template-columns:1.1fr .9fr;gap:64px;align-items:center}
.her-nums{display:grid;grid-template-columns:1fr 1fr;gap:20px}
.hn{background:rgba(255,255,255,.06);border:1px solid rgba(255,255,255,.12);border-radius:18px;padding:26px 24px}
.hn b{font-family:var(--display);font-size:38px;font-weight:600;color:#F4EFE0;display:block;line-height:1}
.hn span{font-size:12px;font-weight:700;letter-spacing:.13em;text-transform:uppercase;color:#8FA694;margin-top:9px;display:block}
.her .dots40{color:#C4933C;margin-bottom:26px}
/* ---------- testimonials ---------- */
.tsti-feature{background:var(--paper);border:1px solid var(--line-soft);border-radius:28px;box-shadow:var(--shadow);
  padding:52px 58px;display:grid;grid-template-columns:auto 1fr;gap:40px;align-items:center;margin-bottom:28px}
.tsti-feature .avatar{width:96px;height:96px;border-radius:50% 50% 14px 14px;background:linear-gradient(140deg,#237A52,#2E8A5F);
  display:flex;align-items:center;justify-content:center;font-family:var(--display);font-size:34px;font-weight:600;color:#EAF4E8}
.tsti-feature blockquote{font-family:var(--display);font-style:italic;font-weight:520;font-size:clamp(20px,2.2vw,26px);line-height:1.45;color:var(--ink)}
.tsti-feature cite{display:block;font-style:normal;font-family:var(--ui);font-size:12.5px;font-weight:700;letter-spacing:.14em;text-transform:uppercase;color:var(--mute);margin-top:18px}
.tgrid{display:grid;grid-template-columns:repeat(3,1fr);gap:26px}
.tcard{background:var(--paper);border:1px solid var(--line-soft);border-radius:20px;padding:30px 28px;box-shadow:var(--shadow)}
.tcard p{font-size:14.5px;line-height:1.65;color:var(--body)}
.tcard cite{display:flex;align-items:center;gap:12px;font-style:normal;margin-top:20px}
.tcard .avatar{width:42px;height:42px;border-radius:50% 50% 9px 9px;flex-shrink:0;display:flex;align-items:center;justify-content:center;font-family:var(--display);font-weight:600;font-size:16px;color:#fff}
.tcard b{display:block;font-size:14px;color:var(--ink)}
.tcard span{font-size:12px;color:var(--mute)}
/* ---------- final split ---------- */
.split{display:grid;grid-template-columns:1fr 1fr;gap:28px}
.spanel{border-radius:var(--arch) var(--arch) var(--r) var(--r);padding:120px 42px 44px;text-align:center;box-shadow:var(--shadow)}
.spanel h3{font-size:29px;margin-bottom:12px}
.spanel p{font-size:15.5px;margin-bottom:28px;max-width:380px;margin-left:auto;margin-right:auto}
.sp-you{background:linear-gradient(180deg,#EAE8F8,#FBFAFE);border:1px solid #DDD9F1}
.sp-you h3{color:#403A9E}.sp-you p{color:#4A4B6E}
.sp-church{background:linear-gradient(180deg,#E7F1E6,#FAFCF6);border:1px solid #D6E5D3}
.sp-church h3{color:var(--green-deep)}.sp-church p{color:#3E5A48}
@media(max-width:1080px){.shelf{grid-template-columns:repeat(2,1fr)}.fmt{grid-template-columns:repeat(2,1fr)}}
@media(max-width:920px){
  .hero .wrap,.pp,.cp,.her{grid-template-columns:1fr}
  .fan{height:430px;transform:scale(.82);transform-origin:left top;margin-bottom:-70px}
  .doors,.tgrid,.split{grid-template-columns:1fr}
  .stats{grid-template-columns:repeat(2,1fr)}
  .tsti-feature{grid-template-columns:1fr;padding:36px 30px;gap:22px}
}
@media(max-width:560px){.shelf,.fmt{grid-template-columns:1fr}.fan{transform:scale(.62);margin-bottom:-160px}}
</style>
"""

BODY = """
<!-- ================= HERO ================= -->
<section class="hero">
  <div class="wrap">
    <div>
      <span class="eyebrow rv">The Lifetogether Formation Platform</span>
      <h1 class="rv">Where do you<br>want to <em>grow</em>?</h1>
      <p class="lede rv">Twenty-five years of churchwide campaigns, now an intelligent platform. Take a ten-minute assessment and receive a path built for where you are — or bring your own teaching and watch it become curriculum your whole church can walk together.</p>
      <div class="hero-ctas rv">
        <a class="btn btn-primary btn-lg" href="assessment.html">Take the 10-Minute Assessment</a>
        <a class="btn btn-outline btn-lg" href="create.html">Bring Your Teaching to Life</a>
      </div>
      <p class="hero-quiet rv">Already know what you need? <a href="browse.html">Browse the campaign library →</a></p>
    </div>
    <div class="fan rv" aria-hidden="true">
      <div class="halo"></div>
      <div class="fc fc1"><div class="cover" data-cover="prayer"></div></div>
      <div class="fc fc2"><div class="cover" data-cover="life-together"></div></div>
      <div class="fc fc3"><div class="cover" data-cover="a-life-worth"></div></div>
    </div>
  </div>
  <div class="wrap">
    <div class="stats rv">
      <div class="st"><b>25+</b><span>Years of Campaigns</span></div>
      <div class="st"><b>500+</b><span>Church Partnerships</span></div>
      <div class="st"><b>1,000+</b><span>Campaign Titles</span></div>
      <div class="st"><b>4</b><span>Formats · 7 / 21 / 30 / 40</span></div>
    </div>
  </div>
</section>

<!-- ================= PARTNERS ================= -->
<div class="partners">
  <div class="wrap">
    <p>Trusted by the churches that shaped a generation</p>
    <div class="logo-row rv">
      <span>Saddleback</span><span>Willow Creek</span><span>Oak Hills</span><span>Mariners</span>
      <span>Seacoast</span><span>Church of the Highlands</span><span>Bayside</span>
      <span>Parkview</span><span>NewSpring</span><span>Rock Church</span>
    </div>
  </div>
</div>

<!-- ================= THREE DOORS ================= -->
<section class="band-white">
  <div class="wrap">
    <div class="sec-head center">
      <span class="eyebrow bare">Three doors. One table behind all of them.</span>
      <h2>Start wherever <em>you</em> are.</h2>
      <p class="lede">Some people know exactly what they need. Some want help discovering it. And some carry a message of their own. The platform meets all three.</p>
    </div>
    <div class="doors">
      <a class="door door-find rv" href="browse.html">
        <svg class="dart" viewBox="0 0 340 150" preserveAspectRatio="xMidYMax meet" aria-hidden="true">
          <circle cx="170" cy="150" r="104" fill="none" stroke="#237A52" stroke-width="2" opacity=".25"/>
          <circle cx="170" cy="150" r="74" fill="none" stroke="#237A52" stroke-width="2" opacity=".35"/>
          <circle cx="170" cy="150" r="44" fill="none" stroke="#237A52" stroke-width="2.4" opacity=".5"/>
          <circle cx="170" cy="150" r="15" fill="#237A52" opacity=".85"/>
        </svg>
        <span class="dtag">FIND</span>
        <h3>Know what you need? Go straight to it.</h3>
        <p>Twenty-three formation channels, seasonal collections, and the editors&rsquo; flagship shelf — hand-curated, ready to launch, searchable when you want the whole library.</p>
        <span class="dlink">Browse the library <span class="arrow">→</span></span>
      </a>
      <a class="door door-path rv" href="assessment.html">
        <svg class="dart" viewBox="0 0 340 150" preserveAspectRatio="xMidYMax meet" aria-hidden="true">
          <path d="M60 150 C 110 70, 230 70, 280 150" fill="none" stroke="#6A63CF" stroke-width="2.4" opacity=".5"/>
          <path d="M90 150 C 130 95, 210 95, 250 150" fill="none" stroke="#6A63CF" stroke-width="2.2" opacity=".38"/>
          <circle cx="170" cy="86" r="13" fill="#6A63CF" opacity=".85"/>
          <circle cx="110" cy="120" r="6" fill="#6A63CF" opacity=".5"/>
          <circle cx="230" cy="120" r="6" fill="#6A63CF" opacity=".5"/>
        </svg>
        <span class="dtag">PERSONALIZE</span>
        <h3>Not sure where to start? Let&rsquo;s find out together.</h3>
        <p>A ten-minute assessment, a personal profile of strengths and growth areas, and a path you choose — never one chosen for you. Then a daily experience built for it.</p>
        <span class="dlink">Find my path <span class="arrow">→</span></span>
      </a>
      <a class="door door-create rv" href="create.html">
        <svg class="dart" viewBox="0 0 340 150" preserveAspectRatio="xMidYMax meet" aria-hidden="true">
          <line x1="170" y1="20" x2="170" y2="150" stroke="#C4933C" stroke-width="2.4" opacity=".55"/>
          <line x1="120" y1="46" x2="120" y2="150" stroke="#C4933C" stroke-width="2.2" opacity=".4"/>
          <line x1="220" y1="46" x2="220" y2="150" stroke="#C4933C" stroke-width="2.2" opacity=".4"/>
          <line x1="76" y1="80" x2="76" y2="150" stroke="#C4933C" stroke-width="2" opacity=".28"/>
          <line x1="264" y1="80" x2="264" y2="150" stroke="#C4933C" stroke-width="2" opacity=".28"/>
          <circle cx="170" cy="20" r="9" fill="#C4933C" opacity=".9"/>
        </svg>
        <span class="dtag">CREATE</span>
        <h3>Pastors — your sermon shouldn&rsquo;t end on Sunday.</h3>
        <p>Upload a message you&rsquo;ve already preached. We read it the way you meant it, then build small group curriculum, devotionals, and campaigns around your words.</p>
        <span class="dlink">Start with one sermon <span class="arrow">→</span></span>
      </a>
    </div>
  </div>
</section>

<!-- ================= PERSONALIZE PREVIEW ================= -->
<section>
  <div class="wrap pp">
    <div>
      <span class="eyebrow rv" style="color:#6A63CF">Find My Path</span>
      <h2 class="rv mt16">The platform that asks about <em style="color:#5A53B8">you</em> first.</h2>
      <p class="lede rv mt16">Most resource libraries hand you a search box. Lifetogether starts with a conversation — six dimensions of formation, a profile that shows strengths as clearly as growth areas, and recommendations you choose from. Try three questions right here.</p>
      <div class="mt32 rv"><a class="btn btn-primary" href="assessment.html">Start the full assessment <span class="arrow">→</span></a></div>
    </div>
    <div class="sampler rv" id="sampler">
      <span class="chip" style="background:#EFEDFA;color:#4A44A8">A taste of the assessment</span>
      <div class="sq">
        <p class="qq">I can name the purpose God has for this season of my life.</p>
        <div class="scale" data-q="0">
          <button>1</button><button>2</button><button>3</button><button>4</button><button>5</button>
        </div>
        <div class="scale-lbls"><span>Not yet</span><span>Consistently true</span></div>
      </div>
      <div class="sq">
        <p class="qq">Prayer is a daily rhythm for me, not an emergency line.</p>
        <div class="scale" data-q="1">
          <button>1</button><button>2</button><button>3</button><button>4</button><button>5</button>
        </div>
        <div class="scale-lbls"><span>Not yet</span><span>Consistently true</span></div>
      </div>
      <div class="sq">
        <p class="qq">My family talks about faith as naturally as we talk about our week.</p>
        <div class="scale" data-q="2">
          <button>1</button><button>2</button><button>3</button><button>4</button><button>5</button>
        </div>
        <div class="scale-lbls"><span>Not yet</span><span>Consistently true</span></div>
      </div>
      <div class="sdone" id="sdone">
        <b>That&rsquo;s the idea.</b> Twenty-four questions like these become a personal profile — and a path you choose. <a href="assessment.html" style="color:#4A44A8;font-weight:700">Take the full assessment →</a>
      </div>
    </div>
  </div>
</section>

<!-- ================= CREATE PREVIEW ================= -->
<section class="band-white">
  <div class="wrap cp">
    <div>
      <span class="eyebrow rv" style="color:var(--gold-deep)">For Pastors &amp; Leaders</span>
      <h2 class="rv mt16">One sermon in.<br>A whole campaign <em class="gold">out</em>.</h2>
      <p class="lede rv mt16">You already did the hardest part — you heard from God and preached it. The platform takes that message and builds the discipleship infrastructure around it, with your words kept visibly at the center.</p>
      <div class="steps4 mt24">
        <div class="stp rv"><span class="num">1</span><div><b>Upload your sermon</b><span>A transcript, your notes, a manuscript — whatever you have.</span></div></div>
        <div class="stp rv"><span class="num">2</span><div><b>We read it the way you meant it</b><span>Big idea, scripture spine, key points — you confirm before anything is built.</span></div></div>
        <div class="stp rv"><span class="num">3</span><div><b>Choose what to create</b><span>Small group curriculum first. Devotionals and full 40-day campaigns next.</span></div></div>
        <div class="stp rv"><span class="num">4</span><div><b>Review, edit, and share</b><span>Session-by-session editing, then branded PDF and Word for your leaders.</span></div></div>
      </div>
      <div class="mt24 rv"><a class="btn btn-gold" href="create.html">Start with one sermon <span class="arrow">→</span></a></div>
    </div>
    <div class="mock rv">
      <div class="mock-head">
        <span class="chip gold">Generated from your sermon</span>
        <b>More Than a Job — Small Group Curriculum</b>
        <span>5 sessions · Leader-ready · Pastor Dave Miller, Grace Community</span>
      </div>
      <div class="mock-body">
        <div class="mline"><i></i><span><b>Session 1 · Made on Purpose.</b> Opens with your Ephesians 2:10 framing and the story of the two carpenters.</span></div>
        <div class="mline"><i></i><span>&ldquo;You are not an accident looking for a reason.&rdquo; <span class="yw">your words</span></span></div>
        <div class="mline"><i></i><span><b>Discuss.</b> Five questions moving from observation to obedience.</span></div>
        <div class="mline"><i></i><span><b>Practice.</b> One workplace conversation this week, named in advance.</span></div>
        <div class="mline"><i></i><span><b>Between sessions.</b> Daily readings drawn from your series texts.</span></div>
      </div>
    </div>
  </div>
</section>

<!-- ================= FEATURED SHELF ================= -->
<section>
  <div class="wrap">
    <div class="shelf-head">
      <div>
        <span class="eyebrow">This Season at Lifetogether</span>
        <h2 class="mt16">Hand-picked. <em>Launch-ready.</em></h2>
      </div>
      <a class="btn btn-outline" href="browse.html">View the full library <span class="arrow">→</span></a>
    </div>
    <div class="shelf" id="homeShelf"></div>
  </div>
</section>

<!-- ================= FORMATS ================= -->
<section class="band-green">
  <div class="wrap">
    <div class="sec-head">
      <span class="eyebrow" style="color:#BFE3C6">Four formats · One architecture</span>
      <h2>As short as a week.<br>As deep as a movement.</h2>
    </div>
    <div class="fmt">
      <div class="fmt-card rv"><b>7</b><span class="fname">The Taste</span><p>One week to sample a theme — perfect after the assessment, or as a churchwide on-ramp.</p></div>
      <div class="fmt-card rv"><b>21</b><span class="fname">The Habit</span><p>Three weeks to establish one practice. The shortest arc that changes a rhythm.</p></div>
      <div class="fmt-card rv"><b>30</b><span class="fname">The Month</span><p>A full month of formation — a natural fit for calendar seasons and group semesters.</p></div>
      <div class="fmt-card rv"><b>40</b><span class="fname">The Movement</span><p>The classic churchwide campaign: pulpit, groups, and daily reading aligned for forty days.</p></div>
    </div>
  </div>
</section>

<!-- ================= HERITAGE ================= -->
<section class="band-ink">
  <div class="wrap her">
    <div>
      <div class="dots40 rv" aria-hidden="true" id="dotsHeritage"></div>
      <span class="eyebrow rv" style="color:#C9A45A">Since the beginning of the movement</span>
      <h2 class="rv mt16">Built on the campaigns that built the modern church.</h2>
      <p class="lede rv mt16">Our team helped design and launch the largest churchwide campaigns in history — from the small group systems of Saddleback and Willow Creek to <em style="color:#E3C88A">40 Days of Purpose</em> and beyond — moving millions of people into groups where formation actually happens. That methodology is what this platform runs on.</p>
      <div class="mt32 rv"><a class="btn btn-gold" href="about.html">Read our story <span class="arrow">→</span></a></div>
    </div>
    <div class="her-nums">
      <div class="hn rv"><b>25+</b><span>Years of churchwide campaigns</span></div>
      <div class="hn rv"><b>500+</b><span>Church partnerships</span></div>
      <div class="hn rv"><b>27</b><span>Published case studies</span></div>
      <div class="hn rv"><b>Millions</b><span>Connected into groups</span></div>
    </div>
  </div>
</section>

<!-- ================= TESTIMONIALS ================= -->
<section class="band-white">
  <div class="wrap">
    <div class="sec-head center">
      <span class="eyebrow bare">In their words</span>
      <h2>The pastors we&rsquo;ve <em>served</em>.</h2>
    </div>
    <div class="tsti-feature rv">
      <div class="avatar">RW</div>
      <div>
        <blockquote>&ldquo;When it comes to the dream-it-up phase of a project — where you imagine the possibilities, consider the alternatives, and produce a scenario for communicating your message in a compelling way — I&rsquo;ve never met anyone who can match Brett&rsquo;s genius.&rdquo;</blockquote>
        <cite>Rick Warren · Saddleback Church</cite>
      </div>
    </div>
    <div class="tgrid">
      <div class="tcard rv">
        <p>&ldquo;Lifetogether is not just the name of an organization. It&rsquo;s what they do. Brett Eastman and his team have come alongside us to produce better leaders, more polished curriculum, stronger groups — and, maybe best of all, lots more groups.&rdquo;</p>
        <cite><span class="avatar" style="background:var(--c-work)">GA</span><span><b>Gene Appel</b><span>Eastside Christian Church</span></span></cite>
      </div>
      <div class="tcard rv">
        <p>&ldquo;Brett&rsquo;s ministry, heart, and skills made it possible for us to quadruple our small-group involvement. He is a competent and hands-on coach with the sensitivity necessary to make it all come together.&rdquo;</p>
        <cite><span class="avatar" style="background:var(--c-mission)">WC</span><span><b>Wayne Cordeiro</b><span>New Hope Oahu</span></span></cite>
      </div>
      <div class="tcard rv">
        <p>&ldquo;Now we can almost make the ridiculous claim that we have as many people connected in groups as we have attending in a given weekend. It never would have been possible without my friends at Lifetogether.&rdquo;</p>
        <cite><span class="avatar" style="background:var(--c-freedom)">TH</span><span><b>Tim Harlow</b><span>Parkview Christian Church</span></span></cite>
      </div>
    </div>
  </div>
</section>

<!-- ================= FINAL SPLIT ================= -->
<section>
  <div class="wrap split">
    <div class="spanel sp-you rv">
      <h3>For you.</h3>
      <p>Ten minutes from now you could be holding a profile of where you are — and a path you chose for where you&rsquo;re going.</p>
      <a class="btn btn-primary btn-lg" style="background:#5A53B8;box-shadow:0 8px 22px rgba(90,83,184,.3)" href="assessment.html">Take the assessment</a>
    </div>
    <div class="spanel sp-church rv">
      <h3>For your church.</h3>
      <p>One sermon becomes a five-session curriculum before your next staff meeting. Bring a message you believe in.</p>
      <a class="btn btn-primary btn-lg" href="create.html">Transform a sermon</a>
    </div>
  </div>
</section>
"""

SCRIPTS = """
<script>
document.addEventListener('DOMContentLoaded',()=>{
  // hero fan covers
  document.querySelectorAll('[data-cover]').forEach(el=>{
    const f = FLAG[el.dataset.cover];
    el.innerHTML = coverSVG(f) + `<span class="cv-title" style="font-size:19px">${f.t}</span><span class="cv-days">${f.days} DAYS</span>` + (f.star?'<span class="cv-star">★</span>':'');
  });
  // featured shelf
  renderCards('#homeShelf',[FLAG['life-together'],FLAG['prayer'],FLAG['god-owns-it-all'],FLAG['living-light'],FLAG['a-life-worth'],FLAG['easter'],FLAG['unplugged'],FLAG['purpose']]);
  // heritage dots (40, all on)
  const dh=document.getElementById('dotsHeritage');
  if(dh) dh.innerHTML=Array.from({length:40},(_,i)=>`<i class="${i<40?'on':''}"></i>`).join('');
  // sampler
  const answered=new Set();
  document.querySelectorAll('#sampler .scale').forEach(sc=>{
    sc.querySelectorAll('button').forEach(b=>b.addEventListener('click',()=>{
      sc.querySelectorAll('button').forEach(x=>x.classList.remove('sel'));
      b.classList.add('sel');answered.add(sc.dataset.q);
      if(answered.size===3)document.getElementById('sdone').classList.add('show');
    }));
  });
});
</script>
"""

write("index.html", "Lifetogether — Where Do You Want to Grow? | The Christian Formation Platform", BODY, active="", head=HEAD, scripts=SCRIPTS)
