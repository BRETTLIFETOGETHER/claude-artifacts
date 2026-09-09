from shell import write

HEAD = """
<style>
.aswrap{max-width:820px;margin:0 auto;padding:0 30px}
.stage{display:none;padding:60px 0 90px;animation:fadeUp .55s var(--ease)}
.stage.on{display:block}
@keyframes fadeUp{from{opacity:0;transform:translateY(16px)}to{opacity:1;transform:none}}
.prog{display:flex;gap:9px;justify-content:center;margin:30px 0 8px}
.prog i{width:26px;height:10px;border-radius:2px;background:#E3E3DA;transition:all .35s var(--ease)}
.prog i.done{background:var(--lt-green)}
.prog i.cur{background:var(--lt-lime)}
.prog-lbl{text-align:center;font-family:var(--display);font-size:12px;font-weight:700;letter-spacing:.22em;text-transform:uppercase;color:var(--mute);margin-bottom:24px}
.intro-grid{display:grid;grid-template-columns:1fr 1fr;gap:16px;margin:34px 0}
.ig{background:#fff;border:1px solid var(--line);border-radius:3px;padding:20px 22px;display:flex;gap:14px;align-items:flex-start}
.ig i{width:34px;height:34px;border-radius:2px;flex-shrink:0;display:flex;align-items:center;justify-content:center;font-size:15px;font-style:normal}
.ig b{display:block;font-size:15px;color:var(--ink);margin-bottom:3px}
.ig span{font-size:13.5px;color:var(--body);line-height:1.5}
/* about-you */
.ab-q{margin-bottom:30px}
.ab-q .hint{font-size:13px;color:var(--mute);margin-top:8px}
.pills .pill.multi.sel{background:var(--lt-green);border-color:var(--lt-green)}
/* mode cards */
.modes{display:grid;grid-template-columns:1fr 1fr;gap:18px;margin-top:32px}
.mode{position:relative;text-align:left;background:#fff;border:1.5px solid var(--line);border-radius:3px;padding:28px;transition:all .2s var(--ease);cursor:pointer}
.mode:hover{border-color:var(--lt-green);transform:translateY(-3px);box-shadow:var(--shadow)}
.mode b{display:block;font-size:18px;color:var(--ink);margin-bottom:7px}
.mode span{font-size:14px;color:var(--body);line-height:1.55}
.mode .mtag{display:inline-block;font-family:var(--display);font-size:10.5px;letter-spacing:.2em;padding:5px 10px;margin-bottom:12px}
/* question card */
.dimhead{display:flex;align-items:center;gap:13px;margin-bottom:8px}
.dimhead .dot{width:13px;height:13px;flex-shrink:0}
.dimhead h3{font-size:23px}
.dimsub{font-size:15px;color:var(--body);margin-bottom:28px}
.q{background:#fff;border:1px solid var(--line);border-radius:3px;padding:22px 26px;margin-bottom:15px}
.q .qq{font-size:16.5px;font-weight:600;color:var(--ink);line-height:1.5;margin-bottom:15px}
.scale{display:flex;gap:9px}
.scale button{flex:1;height:46px;border-radius:2px;border:1.5px solid var(--line);background:var(--sand);font-size:14px;font-weight:700;color:var(--mute);transition:all .15s var(--ease)}
.scale button:hover{border-color:var(--lt-green);color:var(--lt-green-deep)}
.scale button.sel{background:var(--lt-blue);border-color:var(--lt-blue);color:#fff}
.scale-lbls{display:flex;justify-content:space-between;font-size:10.5px;font-weight:700;letter-spacing:.09em;text-transform:uppercase;color:var(--mute);margin-top:9px}
.stage-nav{display:flex;justify-content:space-between;align-items:center;margin-top:32px;gap:14px;flex-wrap:wrap}
.stage-nav .hint{font-size:13px;color:var(--mute)}
/* voices */
.vgrid{display:flex;gap:10px;flex-wrap:wrap;margin-top:8px}
.vchipc{border:1.5px solid var(--line);background:#fff;color:#3A3A36;font-size:14px;font-weight:600;padding:11px 18px;border-radius:999px;transition:all .16s}
.vchipc:hover{border-color:var(--lt-green)}
.vchipc.sel{background:var(--lt-blue);border-color:var(--lt-blue);color:#fff}
.vchipc.style{border-style:dashed}
.vchipc.style.sel{background:var(--lt-green);border-color:var(--lt-green)}
/* processing */
.proc{min-height:52vh;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center}
.proc .parch{position:relative;width:104px;height:104px;margin-bottom:36px}
.proc .parch::before{content:'';position:absolute;inset:0;border:3px solid #E3E3DA;border-radius:3px}
.proc .parch::after{content:'';position:absolute;inset:0;border:3px solid var(--lt-green);border-radius:3px;clip-path:inset(100% 0 0 0);animation:fillup 3.6s var(--ease) forwards}
@keyframes fillup{to{clip-path:inset(0 0 0 0)}}
.proc .pline{font-family:var(--ui);font-weight:300;font-size:23px;color:var(--ink);min-height:34px}
/* profile */
.pf-name{font-family:var(--ui);font-size:clamp(30px,3.8vw,42px);font-weight:300;color:var(--ink);letter-spacing:-.012em}
.pf-sum{background:#fff;border:1px solid var(--line);border-radius:3px;padding:32px 36px;box-shadow:var(--shadow);margin:32px 0 24px}
.pf-sum p{font-size:16.5px;line-height:1.75;color:var(--body)}
.pf-sum p b{color:var(--ink)}
.bars{display:flex;flex-direction:column;gap:18px;margin:6px 0}
.bar-row{display:grid;grid-template-columns:230px 1fr 92px;gap:18px;align-items:center}
.bar-row .bl{font-size:14.5px;font-weight:600;color:var(--ink);display:flex;align-items:center;gap:10px}
.bar-row .bl i{width:10px;height:10px;flex-shrink:0}
.track{height:12px;background:var(--sand);overflow:hidden}
.fill{height:100%;width:0;transition:width 1.1s var(--ease)}
.bar-row .bv{font-family:var(--display);font-size:12px;font-weight:700;letter-spacing:.12em;text-transform:uppercase;text-align:right}
.pf-note{font-size:13.5px;color:var(--mute);margin-top:16px}
/* choose */
.areas{display:grid;grid-template-columns:1fr 1fr;gap:16px;margin-top:32px}
.area{position:relative;text-align:left;background:#fff;border:1.5px solid var(--line);border-radius:3px;padding:24px 26px;transition:all .2s var(--ease);cursor:pointer}
.area:hover{border-color:var(--lt-green);transform:translateY(-3px);box-shadow:var(--shadow)}
.area .sg{position:absolute;top:16px;right:16px}
.area b{display:flex;align-items:center;gap:10px;font-size:17px;color:var(--ink);margin-bottom:6px}
.area b i{width:11px;height:11px}
.area span{font-size:13.5px;color:var(--body);line-height:1.55}
/* books */
.books{display:grid;grid-template-columns:repeat(3,1fr);gap:14px;margin-top:32px}
.bk{text-align:left;background:#fff;border:1.5px solid var(--line);border-radius:3px;padding:20px 22px;cursor:pointer;transition:all .18s}
.bk:hover{border-color:var(--lt-green);transform:translateY(-2px)}
.bk b{display:block;font-family:var(--display);font-size:17px;letter-spacing:.08em;text-transform:uppercase;color:var(--ink)}
.bk span{font-size:12.5px;color:var(--mute)}
/* path */
.path-head{display:flex;align-items:center;gap:14px;margin-bottom:8px}
.path-head .dot{width:14px;height:14px}
.fmt-pills{display:flex;gap:10px;flex-wrap:wrap;margin:24px 0 36px}
.match{display:grid;grid-template-columns:repeat(3,1fr);gap:24px}
.match .why{font-size:13px;color:var(--lt-green-deep);font-weight:600;padding:0 20px 18px;margin-top:-6px}
.also{margin-top:34px;background:#fff;border:1px solid var(--line);border-left:6px solid var(--lt-blue);border-radius:3px;padding:20px 24px;display:flex;justify-content:space-between;align-items:center;gap:18px;flex-wrap:wrap}
.also b{font-size:16px;color:var(--ink)}
.also span{display:block;font-size:13.5px;color:var(--body);margin-top:3px}
.path-cta{background:#F4F4EF;border:1px solid var(--line);border-radius:3px;padding:32px 36px;margin-top:40px;display:flex;justify-content:space-between;align-items:center;gap:26px;flex-wrap:wrap}
.path-cta b{font-family:var(--ui);font-weight:700;font-size:21px;color:var(--ink);display:block;margin-bottom:5px}
.path-cta span{font-size:14.5px;color:var(--body)}
.custom-tease{margin-top:22px;background:var(--lt-blue);border-radius:3px;padding:24px 28px;display:flex;justify-content:space-between;align-items:center;gap:20px;flex-wrap:wrap;color:#C4CFE8}
.custom-tease b{color:#fff;font-size:17px;display:block;margin-bottom:4px}
@media(max-width:760px){
  .intro-grid,.areas,.modes{grid-template-columns:1fr}
  .books{grid-template-columns:1fr 1fr}
  .bar-row{grid-template-columns:1fr;gap:7px}
  .bar-row .bv{text-align:left}
  .match{grid-template-columns:1fr}
}
</style>
"""

BODY = """
<!-- STAGE · INTRO -->
<section class="stage on" id="st-intro">
  <div class="aswrap">
    <span class="eyebrow">Find My Path</span>
    <h1 class="mt16" style="font-size:clamp(42px,5.4vw,64px)">Ten minutes.<br>Built around <em>you.</em></h1>
    <p class="lede mt24">This isn&rsquo;t a quiz with a winner. It starts with who you are — your season, your tradition, what you&rsquo;re actually hungry for — and shapes everything after that around your answers. It ends with a path <b style="color:var(--ink)">you</b> choose, and Day One free.</p>
    <div class="intro-grid">
      <div class="ig"><i style="background:#EAF0E2;color:#5F8540">1</i><div><b>Tell us who you are</b><span>Season of life, background, and what you want right now — the questions adapt from there.</span></div></div>
      <div class="ig"><i style="background:#E8EDF6;color:#2E4C97">2</i><div><b>Choose your route</b><span>Let your profile lead — or skip straight to going deeper in a book of the Bible.</span></div></div>
      <div class="ig"><i style="background:#EAF0E2;color:#5F8540">3</i><div><b>Answer honestly</b><span>Score where you are, not where you wish you were. There are no wrong answers here.</span></div></div>
      <div class="ig"><i style="background:#E8EDF6;color:#2E4C97">4</i><div><b>You decide</b><span>We suggest. You choose. Then Day One of a real campaign, personalized and free.</span></div></div>
    </div>
    <button class="btn btn-primary btn-lg" onclick="go('about')">Start with who you are <span class="arrow">→</span></button>
    <p class="small mt16">Built on the six formation dimensions behind 25 years of Lifetogether churchwide campaigns.</p>
  </div>
</section>

<!-- STAGE · ABOUT YOU -->
<section class="stage" id="st-about">
  <div class="aswrap">
    <span class="eyebrow">First — you</span>
    <h2 class="mt16">The path starts with<br><em>who&rsquo;s walking it.</em></h2>
    <div class="mt32">
      <div class="ab-q">
        <label class="lbl">First name <span style="text-transform:none;letter-spacing:0;font-weight:400">(so we can talk like people)</span></label>
        <input class="input" id="fname" placeholder="Your first name" maxlength="24" style="max-width:360px">
      </div>
      <div class="ab-q">
        <label class="lbl">Your season of life</label>
        <div class="pills" data-one="season">
          <button class="pill" data-v="student">Student (13–18)</button>
          <button class="pill" data-v="young">College &amp; twenties</button>
          <button class="pill" data-v="building">Building career or family</button>
          <button class="pill" data-v="parents">Raising kids at home</button>
          <button class="pill" data-v="midlife">Midlife &amp; transition</button>
          <button class="pill" data-v="legacy">Legacy season</button>
        </div>
        <p class="hint">This changes which questions you get — a high schooler and a grandparent shouldn&rsquo;t be asked the same things.</p>
      </div>
      <div class="ab-q">
        <label class="lbl">You are</label>
        <div class="pills" data-one="gender">
          <button class="pill" data-v="w">A woman</button>
          <button class="pill" data-v="m">A man</button>
          <button class="pill" data-v="x">Prefer not to say</button>
        </div>
      </div>
      <div class="ab-q">
        <label class="lbl">Your church background</label>
        <div class="pills" data-one="denom">
          <button class="pill" data-v="Non-denominational">Non-denominational</button>
          <button class="pill" data-v="Baptist">Baptist</button>
          <button class="pill" data-v="Methodist / Wesleyan">Methodist / Wesleyan</button>
          <button class="pill" data-v="Presbyterian / Reformed">Presbyterian / Reformed</button>
          <button class="pill" data-v="Lutheran">Lutheran</button>
          <button class="pill" data-v="Pentecostal / Charismatic">Pentecostal / Charismatic</button>
          <button class="pill" data-v="Catholic">Catholic</button>
          <button class="pill" data-v="Anglican / Episcopal">Anglican / Episcopal</button>
          <button class="pill" data-v="Another tradition">Another tradition</button>
          <button class="pill" data-v="Exploring">Exploring — no church home yet</button>
        </div>
      </div>
      <div class="ab-q">
        <label class="lbl">How you&rsquo;d describe yourself</label>
        <div class="pills" data-one="role">
          <button class="pill" data-v="Exploring faith">Exploring faith</button>
          <button class="pill" data-v="Growing believer">Growing believer</button>
          <button class="pill" data-v="Group leader">Group leader</button>
          <button class="pill" data-v="Pastor or church staff">Pastor / church staff</button>
          <button class="pill" data-v="Marketplace leader">Marketplace leader</button>
        </div>
      </div>
      <div class="ab-q">
        <label class="lbl">Right now, you most want… <span style="text-transform:none;letter-spacing:0;font-weight:400">(pick up to two)</span></label>
        <div class="pills" data-multi="wants" data-max="2">
          <button class="pill multi" data-v="clarity">Clarity</button>
          <button class="pill multi" data-v="peace">Peace</button>
          <button class="pill multi" data-v="connection">Connection</button>
          <button class="pill multi" data-v="momentum">Momentum</button>
          <button class="pill multi" data-v="healing">Healing</button>
          <button class="pill multi" data-v="depth">To go deeper</button>
          <button class="pill multi" data-v="fresh">A fresh start</button>
          <button class="pill multi" data-v="family">A stronger family</button>
          <button class="pill multi" data-v="work">Purpose in my work</button>
          <button class="pill multi" data-v="curious">Honestly — just curious</button>
        </div>
      </div>
    </div>
    <div class="stage-nav">
      <button class="btn btn-ghost" onclick="go('intro')">← Back</button>
      <span class="hint" id="aboutHint">Choose your season to continue</span>
      <button class="btn btn-primary" id="aboutNext" disabled onclick="go('mode')">Continue <span class="arrow">→</span></button>
    </div>
  </div>
</section>

<!-- STAGE · MODE -->
<section class="stage" id="st-mode">
  <div class="aswrap">
    <span class="eyebrow">Choose your route</span>
    <h2 class="mt16" id="modeTitle">How should we build<br>your path?</h2>
    <div class="modes">
      <button class="mode" onclick="startQuestions()">
        <span class="mtag lbl-bar green" style="padding:5px 10px">Recommended</span>
        <b>Read me, then recommend</b>
        <span>Twenty-four honest statements across six dimensions of a formed life — shaped to your season — then a profile and a path you choose.</span>
      </button>
      <button class="mode" onclick="go('book')">
        <span class="mtag lbl-bar blue" style="padding:5px 10px">Direct route</span>
        <b>Take me deeper into a book of the Bible</b>
        <span>Skip the profile. Pick a book — Psalms, Proverbs, John, Acts and more — and go straight to journeys built on that text.</span>
      </button>
    </div>
  </div>
</section>

<!-- STAGE · BOOK PICKER -->
<section class="stage" id="st-book">
  <div class="aswrap">
    <span class="eyebrow">Scripture first</span>
    <h2 class="mt16">Which book is<br>calling you?</h2>
    <div class="books" id="bookGrid"></div>
    <p class="small mt24"><button class="btn btn-ghost" style="padding:0" onclick="go('mode')">← Back</button></p>
  </div>
</section>

<!-- STAGE · QUESTIONS -->
<section class="stage" id="st-q">
  <div class="aswrap">
    <div class="prog" id="prog"></div>
    <p class="prog-lbl" id="progLbl"></p>
    <div id="qhost"></div>
    <div class="stage-nav">
      <button class="btn btn-ghost" id="backBtn" onclick="back()">← Back</button>
      <span class="hint" id="navHint">Answer all four to continue</span>
      <button class="btn btn-primary" id="nextBtn" disabled onclick="nextSec()">Continue <span class="arrow">→</span></button>
    </div>
  </div>
</section>

<!-- STAGE · VOICES -->
<section class="stage" id="st-voices">
  <div class="aswrap">
    <span class="eyebrow">Last one</span>
    <h2 class="mt16">Which voices have<br><em>shaped you?</em></h2>
    <p class="lede mt16">Choose any that resonate — teachers Lifetogether has produced alongside, and the styles you gravitate toward. This tunes the voice of your path. Skipping is fine.</p>
    <label class="lbl mt32">Teachers</label>
    <div class="vgrid" id="vTeachers"></div>
    <label class="lbl mt24">Or simply the style</label>
    <div class="vgrid" id="vStyles"></div>
    <div class="stage-nav">
      <button class="btn btn-ghost" onclick="go('sec',5)">← Back</button>
      <button class="btn btn-primary btn-lg" onclick="process1()">See my profile <span class="arrow">→</span></button>
    </div>
  </div>
</section>

<!-- STAGE · PROCESSING -->
<section class="stage" id="st-proc">
  <div class="aswrap proc">
    <div class="parch"></div>
    <p class="pline" id="procLine">Reading your answers…</p>
    <p class="small mt16">Deterministic scoring — the same answers always produce the same profile.</p>
  </div>
</section>

<!-- STAGE · PROFILE -->
<section class="stage" id="st-profile">
  <div class="aswrap">
    <span class="eyebrow">Your formation profile</span>
    <h1 class="pf-name mt16" id="pfName">Here&rsquo;s where you are.</h1>
    <div class="pf-sum"><p id="pfNarr"></p></div>
    <div class="pf-sum">
      <div class="bars" id="bars"></div>
      <p class="pf-note">Emerging → Growing → Steady → Strong. Every band is a season, not a sentence.</p>
    </div>
    <div class="stage-nav">
      <button class="btn btn-ghost" onclick="go('voices')">← Adjust</button>
      <button class="btn btn-primary btn-lg" onclick="go('choose')">Choose my growth area <span class="arrow">→</span></button>
    </div>
  </div>
</section>

<!-- STAGE · CHOOSE -->
<section class="stage" id="st-choose">
  <div class="aswrap">
    <span class="eyebrow">Your call</span>
    <h2 class="mt16">Where do you want<br>to grow <em>first?</em></h2>
    <p class="lede mt16">We&rsquo;ve marked what your profile suggests — but this is a door you walk through, not one you&rsquo;re pushed through.</p>
    <div class="areas" id="areas"></div>
  </div>
</section>

<!-- STAGE · PATH -->
<section class="stage" id="st-path">
  <div class="aswrap" style="max-width:1080px">
    <span class="eyebrow">Your path</span>
    <div class="path-head mt16"><span class="dot" id="pathDot"></span><h2 id="pathTitle"></h2></div>
    <p class="lede" id="pathLede"></p>
    <label class="lbl mt32" style="margin-bottom:12px">Choose your commitment</label>
    <div class="fmt-pills" id="fmtPills">
      <button class="pill" data-f="7">7 days · The Taste</button>
      <button class="pill sel" data-f="21">21 days · The Habit</button>
      <button class="pill" data-f="30">30 days · The Month</button>
      <button class="pill" data-f="40">40 days · The Movement</button>
    </div>
    <div class="match" id="matchCards"></div>
    <div id="alsoHost"></div>
    <div class="path-cta">
      <div><b id="ctaTitle">Begin Day One — free.</b><span>No account, no card. The first day of the campaign we matched first, personalized to you.</span></div>
      <a class="btn btn-primary btn-lg" id="beginBtn" href="reader.html">Begin Day One <span class="arrow">→</span></a>
    </div>
    <div class="custom-tease">
      <div><b>Want it truly custom?</b>These are hand-finished flagships matched to you. The full platform goes further — generating custom curriculum from your church&rsquo;s own teaching or any book of Scripture.</div>
      <a class="btn btn-gold" href="create.html">See how →</a>
    </div>
    <p class="small mt24" style="text-align:center"><a href="#" onclick="go('choose');return false" style="color:var(--lt-orange);font-weight:700">← Choose a different area</a> &nbsp;·&nbsp; <a href="browse.html" style="color:var(--lt-orange);font-weight:700">Browse the full library instead</a></p>
  </div>
</section>
"""

SCRIPTS = r"""
<script>
/* ================= CONTEXT ================= */
const ctx={name:'',season:'',gender:'',denom:'',role:'',wants:[],mode:'profile',book:'',voices:[],styles:[]};
const WANTWORDS={clarity:'clarity',peace:'peace',connection:'connection',momentum:'momentum',healing:'healing',depth:'depth',fresh:'a fresh start',family:'a stronger family',work:'purpose in your work',curious:'honest curiosity'};

/* ================= TEACHERS & STYLES (Lifetogether-produced voices) ================= */
const TEACHERS=[
 {n:'Rick Warren',s:['practical','story']},{n:'Max Lucado',s:['gentle','story']},
 {n:'Tony Evans',s:['bold','bible']},{n:'Christine Caine',s:['bold','gentle']},
 {n:'Dr. David Jeremiah',s:['bible']},{n:'Judah Smith',s:['story','gentle']},
 {n:'Miles McPherson',s:['bold','story']},{n:'Randy Frazee',s:['bible','practical']},
 {n:'Ron Blue',s:['practical']},{n:'Greg Surratt',s:['practical','story']}
];
const STYLES=[
 {k:'story',n:'Story-driven preaching'},{k:'bible',n:'Verse-by-verse Bible teaching'},
 {k:'bold',n:'Bold, challenging truth'},{k:'gentle',n:'Gentle encouragement'},
 {k:'practical',n:'Practical, step-by-step'}
];
const STYLEPHRASE={story:'story-driven teaching',bible:'deep, verse-by-verse Bible teaching',bold:'bold, challenging truth',gentle:'gentle encouragement',practical:'practical, step-by-step wisdom'};

/* ================= ADAPTIVE STATEMENTS ================= */
/* each: {b:base, student, young, parents, legacy} — falls back to base */
const DIMS=[
 {k:'purpose',n:'Purpose & Calling',v:'--c-purpose',
  sub:{b:'Why you\u2019re here — and what this season is for.',student:'What your life is for — starting now, not someday.'},
  qs:[
   {b:'If a friend asked what God is doing in my life this season, I could give a real answer.',
    student:'If a friend asked why God made me, I could take a real shot at answering.'},
   {b:'My ordinary week — work, errands, all of it — feels connected to something bigger than me.',
    student:'School, practice, my job — the everyday stuff feels connected to something bigger than a grade.',
    parents:'Even the carpool-and-deadlines version of my week feels connected to something eternal.'},
   {b:'Looking at how I actually spent the last month, my time went to what I say matters most.',
    student:'Looking at my last month, my time actually went to things I\u2019d say matter.'},
   {b:'I\u2019ve said yes to something recently mainly because I sensed God asking me to.'}
  ],
  m:{b:['purpose','made-for-this','shape'],student:['real-students','made-for-this','purpose'],young:['made-for-this','adulting','purpose'],legacy:['purpose','a-life-worth','shape']},
  why:{b:['The classic churchwide journey through the question itself.','Calling for the season you\u2019re actually in.','Discover how you\u2019re wired before deciding where to serve.'],
       student:['Faith that\u2019s actually yours — built for students.','Calling for the season you\u2019re actually in.','The question that started the movement.'],
       young:['Faith for the twenties nobody prepped you for.','Young-adult calling and Kingdom purpose.','The question that started the movement.'],
       legacy:['The question never retires.','Purpose that outlives you.','How you\u2019re wired still matters — maybe more now.']}},
 {k:'rhythms',n:'Spiritual Rhythms',v:'--c-prayer',
  sub:{b:'Prayer, Scripture, and unhurried time with God as a way of life.'},
  qs:[
   {b:'Prayer shows up in my normal days — not just when something goes wrong.'},
   {b:'Something I read in Scripture recently actually changed a decision I made.',
    student:'Something from the Bible — youth group, my own reading — actually changed how I handled something recently.'},
   {b:'There\u2019s unhurried quiet somewhere in my week — no phone, no agenda, just God.',
    student:'I sometimes put the phone down on purpose just to get quiet with God.'},
   {b:'Worship happens somewhere in my week, not only at a weekend service.'}
  ],
  m:{b:['prayer','proverbs','rhythms']},
  why:{b:['Forty days that turn prayer from event to atmosphere.','One chapter of wisdom for every decision ahead.','Sustainable practices — built for real schedules.']}},
 {k:'community',n:'Relationships & Community',v:'--c-community',
  sub:{b:'Being truly known — and letting others carry life with you.'},
  qs:[
   {b:'Somebody outside my house knows how I\u2019m actually doing — not the highlight reel.',
    student:'At least one friend or leader knows how I\u2019m actually doing — not the version I post.'},
   {b:'I\u2019m part of a group — formal or not — where my faith is known and encouraged.'},
   {b:'When life gets heavy, my instinct is to let someone carry it with me, not to disappear.'},
   {b:'I\u2019ve had a genuinely honest spiritual conversation in the last two weeks.'}
  ],
  m:{b:['life-together','better-together','beloved']},
  why:{b:['Our flagship — the campaign that gives the platform its name.','What biblical community actually takes.','Connection begins with knowing you\u2019re already loved.']}},
 {k:'peace',n:'Peace & Emotional Health',v:'--c-emotional',
  sub:{b:'Rest, honesty about what you feel, and freedom from what weighs on you.'},
  qs:[
   {b:'Most nights I sleep, and most weeks I truly rest.',student:'I actually sleep — and I get real breaks from the pressure.'},
   {b:'Anxious thoughts visit, but they don\u2019t run my week.'},
   {b:'I can usually name what I\u2019m feeling — and I bring the real version to God.'},
   {b:'There\u2019s no forgiveness — asked for or offered — stuck in my chest right now.'}
  ],
  m:{b:['living-light','soul-care','healing'],student:['real-students','living-light','soul-care']},
  why:{b:['A gentle, honest 40-day walk out from under anxiety.','Psalm 23, slowly — the rest your soul needs.','Because everyone is healing from something.'],
       student:['Authentic faith for students — pressure included.','A gentle walk out from under anxiety.','Psalm 23, slowly.']}},
 {k:'stewardship',n:'Generosity & Stewardship',v:'--c-money',
  sub:{b:'Money, time, and talent held with open hands.',student:'The money and time you already have — handled on purpose.'},
  qs:[
   {b:'I have an actual plan for my money, and my faith helped write it.',
    student:'The money I do have — job, gifts, allowance — I handle on purpose, not by accident.'},
   {b:'Giving comes off the top for me — a first decision, not a leftover.',
    student:'I give some of what I have — and honestly, I like doing it.'},
   {b:'Deep down I operate like a manager of God\u2019s stuff, not an owner of mine.'},
   {b:'Money worries exist, but they don\u2019t get the final vote in my decisions.',
    student:'Money stress — mine or my family\u2019s — doesn\u2019t get the final vote on my peace.'}
  ],
  m:{b:['god-owns-it-all','generosity','steward-heart']},
  why:{b:['Ron Blue\u2019s biblical financial wisdom — freedom starts with ownership.','Why giving changes everything — 2 Corinthians 9, applied.','Time, talent, and treasure as one faithful life.']}},
 {k:'family',n:'Family & Legacy',v:'--c-family',
  sub:{b:'The faith, wisdom, and story you\u2019re handing to the people after you.',
       student:'Home — and the people who are shaping you.',
       young:'The family you came from, and the one you\u2019re becoming.'},
  qs:[
   {b:'Faith comes up at our table as naturally as the week\u2019s schedule.',
    student:'Faith comes up at home — or with the family I\u2019ve found — as naturally as everyday stuff.'},
   {b:'The people coming after me are hearing our story — not just our rules.',
    student:'There\u2019s an older believer — parent, grandparent, leader — whose story I actually know and want to learn from.',
    young:'I\u2019m intentionally learning from believers a generation ahead of me.'},
   {b:'Our home has rhythms — meals, blessings, honest conversations — that quietly shape us.',
    student:'My home, whatever it looks like, has rhythms — meals, check-ins — that quietly shape me.'},
   {b:'I could tell you what I want to hand down that isn\u2019t money.',
    student:'I could tell you what I hope people say my life was about — and it isn\u2019t stuff.'}
  ],
  m:{b:['a-life-worth','home-run','built-to-last'],student:['home-run','the-prodigal','real-students'],young:['built-to-last','the-prodigal','a-life-worth'],parents:['home-run','built-to-last','a-life-worth']},
  why:{b:['Leaving faith, wisdom, and purpose to the next generation.','Build the family that wins at what matters most.','A marriage on the rock holds up everything else.'],
       student:['A family that wins at what matters — starting with you.','The most famous welcome-home ever told.','Authentic faith, at home too.'],
       young:['Foundations now for the family you\u2019re becoming.','The most famous welcome-home ever told.','What you\u2019ll hand down starts today.'],
       parents:['Build the family that wins at what matters most.','Marriage on the rock — Matthew 7:24.','What are we actually handing them?']}}
];
const pick=(o)=>o[ctx.season]||o.b;
const BANDS=[{max:2.5,l:'Emerging',c:'#C6552E'},{max:3.5,l:'Growing',c:'#C98F2E'},{max:4.3,l:'Steady',c:'#4E86B8'},{max:9,l:'Strong',c:'#5F8540'}];
const ans=Array.from({length:6},()=>[0,0,0,0]);
let sec=0, chosen=null, fmt=21;

/* ================= BOOKS ================= */
const BOOKS=[
 {n:'Psalms',d:'The prayer book of the Bible',m:['soul-care','prayer'],note:'Psalm 23, slowly — then a church that prays as one.'},
 {n:'Proverbs',d:'Wisdom for every decision',m:['proverbs','steward-heart'],note:'A chapter of wisdom for every decision you\u2019ll make this year.'},
 {n:'Matthew',d:'The Kingdom, taught',m:['built-to-last','parables'],note:'The Sermon on the Mount\u2019s rock — and the stories Jesus told.'},
 {n:'Luke',d:'The Gospel of the welcomed',m:['the-prodigal','parables'],note:'Forty days inside the most famous parable ever told.'},
 {n:'John',d:'That you may believe',m:['one-john17','beloved'],note:'John 17\u2019s unity — and living loved in John\u2019s Gospel.'},
 {n:'Acts',d:'The church, sent',m:['living-sent','life-together'],note:'Everyday mission — and the community that makes it possible.'},
 {n:'Nehemiah',d:'Vision, prayer, rebuilding',m:['nehemiah','purpose'],note:'For anyone standing in front of a wall that needs rebuilding.'},
 {n:'1 Kings · Elijah',d:'Burnout and restoration',m:['elijah','soul-care'],note:'The prophet who burned out — and the God who fed him first.'},
 {n:'The whole story',d:'Genesis to Revelation',m:['bible-in-40','purpose'],note:'The entire narrative of Scripture in forty days.'}
];

/* ================= STAGING ================= */
function show(id){document.querySelectorAll('.stage').forEach(s=>s.classList.remove('on'));
  document.getElementById(id).classList.add('on');window.scrollTo({top:0});}
function go(where,i){
  if(where==='sec'){sec=i;renderSec();show('st-q');}
  else show('st-'+where);
}
function back(){ if(sec===0){show('st-mode')} else {sec--;renderSec()} }
function startQuestions(){ctx.mode='profile';sec=0;renderSec();show('st-q');}

/* about-you pills */
document.addEventListener('DOMContentLoaded',()=>{
  document.querySelectorAll('[data-one]').forEach(g=>{
    g.querySelectorAll('.pill').forEach(p=>p.addEventListener('click',()=>{
      g.querySelectorAll('.pill').forEach(x=>x.classList.remove('sel'));
      p.classList.add('sel');ctx[g.dataset.one]=p.dataset.v;syncAbout();
    }));
  });
  document.querySelectorAll('[data-multi]').forEach(g=>{
    const max=+g.dataset.max||99;
    g.querySelectorAll('.pill').forEach(p=>p.addEventListener('click',()=>{
      const key=g.dataset.multi;
      if(p.classList.contains('sel')){p.classList.remove('sel');ctx[key]=ctx[key].filter(v=>v!==p.dataset.v);}
      else{
        if(ctx[key].length>=max){const first=ctx[key].shift();g.querySelector(`[data-v="${first}"]`).classList.remove('sel');}
        p.classList.add('sel');ctx[key].push(p.dataset.v);
      }
    }));
  });
  document.querySelectorAll('#fmtPills .pill').forEach(p=>p.addEventListener('click',()=>{
    document.querySelectorAll('#fmtPills .pill').forEach(x=>x.classList.remove('sel'));
    p.classList.add('sel');fmt=+p.dataset.f;syncBegin();
  }));
  // voices
  document.getElementById('vTeachers').innerHTML=TEACHERS.map(t=>`<button class="vchipc" data-n="${t.n}">${t.n}</button>`).join('');
  document.getElementById('vStyles').innerHTML=STYLES.map(s=>`<button class="vchipc style" data-k="${s.k}">${s.n}</button>`).join('');
  document.querySelectorAll('#vTeachers .vchipc').forEach(b=>b.addEventListener('click',()=>{
    b.classList.toggle('sel');
    ctx.voices=[...document.querySelectorAll('#vTeachers .sel')].map(x=>x.dataset.n);
  }));
  document.querySelectorAll('#vStyles .vchipc').forEach(b=>b.addEventListener('click',()=>{
    b.classList.toggle('sel');
    ctx.styles=[...document.querySelectorAll('#vStyles .sel')].map(x=>x.dataset.k);
  }));
  // book grid
  document.getElementById('bookGrid').innerHTML=BOOKS.map((b,i)=>`
    <button class="bk" onclick="chooseBook(${i})"><b>${b.n}</b><span>${b.d}</span></button>`).join('');
});
function syncAbout(){
  const ok=!!ctx.season;
  document.getElementById('aboutNext').disabled=!ok;
  document.getElementById('aboutHint').textContent=ok?'':'Choose your season to continue';
  ctx.name=document.getElementById('fname').value.trim();
}

/* ================= QUESTIONS ================= */
function renderSec(){
  ctx.name=document.getElementById('fname').value.trim();
  const d=DIMS[sec];
  document.getElementById('prog').innerHTML=DIMS.map((_,i)=>`<i class="${i<sec?'done':i===sec?'cur':''}"></i>`).join('');
  document.getElementById('progLbl').textContent=`Section ${sec+1} of 6 \u00b7 ${d.n}`;
  document.getElementById('qhost').innerHTML=`
    <div class="dimhead"><span class="dot" style="background:var(${d.v})"></span><h3>${d.n}</h3></div>
    <p class="dimsub">${pick(d.sub)}</p>
    ${d.qs.map((q,qi)=>`
      <div class="q"><p class="qq">${pick(q)}</p>
        <div class="scale" data-qi="${qi}">${[1,2,3,4,5].map(v=>`<button class="${ans[sec][qi]===v?'sel':''}" onclick="pickAns(${qi},${v},this)">${v}</button>`).join('')}</div>
        <div class="scale-lbls"><span>Not yet true of me</span><span>Consistently true</span></div>
      </div>`).join('')}`;
  syncNext();
}
function pickAns(qi,v,btn){
  ans[sec][qi]=v;
  btn.parentElement.querySelectorAll('button').forEach(b=>b.classList.remove('sel'));
  btn.classList.add('sel');syncNext();
}
function syncNext(){
  const done=ans[sec].every(v=>v>0);
  document.getElementById('nextBtn').disabled=!done;
  document.getElementById('navHint').textContent=done?'':'Answer all four to continue';
}
function nextSec(){ if(sec<5){sec++;renderSec()} else show('st-voices'); }

/* ================= SCORING & PROFILE ================= */
const scores=()=>DIMS.map((d,i)=>({...d,avg:ans[i].reduce((a,b)=>a+b,0)/4}));
const band=a=>BANDS.find(b=>a<=b.max);
function process1(){
  show('st-proc');
  const lines=['Reading your answers\u2026','Weighing your season and what you told us you want\u2026','Listening for the voices that shaped you\u2026','Matching hand-finished campaigns\u2026','Writing your profile\u2026'];
  let i=0;const el=document.getElementById('procLine');
  const t=setInterval(()=>{i++;if(i<lines.length){el.textContent=lines[i]}else{clearInterval(t);profile()}},900);
}
const SEASONWORD={student:'a student',young:'in your twenties',building:'building a career and a life',parents:'raising kids at home',midlife:'in a midlife season',legacy:'in a legacy season'};
function profile(){
  const sc=scores();
  const sorted=[...sc].sort((a,b)=>a.avg-b.avg);
  const hi=sorted[5], gentle=sorted[0];
  window._low=sorted.slice(0,3).map(s=>s.k);
  document.getElementById('pfName').innerHTML=ctx.name?`${ctx.name}, here&rsquo;s where you are.`:'Here&rsquo;s where you are.';
  let who=[];
  if(ctx.season)who.push(SEASONWORD[ctx.season]);
  if(ctx.role&&ctx.role!=='Growing believer')who.push(ctx.role.toLowerCase());
  const whoLine=who.length?`As someone ${who.join(' \u2014 and a ')}, `:'';
  const wants=ctx.wants.map(w=>WANTWORDS[w]);
  const wantLine=wants.length?`You told us what you most want right now is <b>${wants.join('</b> and <b>')}</b> \u2014 your path leads with that. `:'';
  const st=[...new Set(ctx.styles.concat(...ctx.voices.map(n=>TEACHERS.find(t=>t.n===n).s)))];
  const voiceLine=st.length?`And because you lean toward ${st.slice(0,2).map(k=>STYLEPHRASE[k]).join(' and ')}${ctx.voices.length?` \u2014 voices like ${ctx.voices.slice(0,2).join(' and ')} \u2014`:''} we\u2019ll keep your path in that register. `:'';
  const denomLine=ctx.denom==='Exploring'?`You said you\u2019re still exploring \u2014 every campaign here is built to welcome exactly that. `:(ctx.denom&&['Catholic','Anglican / Episcopal','Lutheran','Orthodox'].includes(ctx.denom)?`Coming from a ${ctx.denom} background, you\u2019ll find these journeys broad-stream and Scripture-anchored, with room for your tradition\u2019s rhythms. `:'');
  document.getElementById('pfNarr').innerHTML=
    whoLine+`your strongest dimension right now is <b>${hi.n}</b> \u2014 that\u2019s a resource, not a coincidence. `+
    `The area readiest for attention is <b>${gentle.n}</b>; not because something\u2019s wrong, but because a small daily practice there would likely change the most, soonest. `+
    wantLine+voiceLine+denomLine+
    `Below is the whole picture \u2014 read it the way a good friend would.`;
  document.getElementById('bars').innerHTML=sc.map(s=>{
    const b=band(s.avg);
    return `<div class="bar-row">
      <span class="bl"><i style="background:var(${s.v})"></i>${s.n}</span>
      <div class="track"><div class="fill" data-w="${s.avg/5*100}" style="background:var(${s.v})"></div></div>
      <span class="bv" style="color:${b.c}">${b.l}</span></div>`;
  }).join('');
  show('st-profile');
  setTimeout(()=>document.querySelectorAll('.fill').forEach(f=>f.style.width=f.dataset.w+'%'),150);
  renderAreas();
}

/* ================= CHOOSE & PATH ================= */
function renderAreas(){
  const sc=scores();
  document.getElementById('areas').innerHTML=sc.map(s=>`
    <button class="area" onclick="choose('${s.k}')">
      ${window._low&&window._low.includes(s.k)?'<span class="sg chip">Suggested for you</span>':''}
      <b><i style="background:var(${s.v})"></i>${s.n}</b>
      <span>${pick(s.sub)}</span>
    </button>`).join('');
}
function wantsPhrase(){const w=ctx.wants.map(x=>WANTWORDS[x]);return w.length?w.join(' and '):''}
function choose(k){
  chosen=DIMS.find(d=>d.k===k);
  const slugs=pick(chosen.m), whys=pick(chosen.why);
  document.getElementById('pathDot').style.background=`var(${chosen.v})`;
  document.getElementById('pathTitle').textContent=chosen.n;
  const wp=wantsPhrase();
  document.getElementById('pathLede').textContent=
    `Three hand-finished campaigns, matched to this dimension, your season${wp?`, and your hunger for ${wp}`:''}. Every one is launch-ready today.`;
  document.getElementById('matchCards').innerHTML=slugs.map((slug,i)=>{
    const f=FLAG[slug];
    return `<div>${campaignCard(f)}<p class="why">\u21b3 ${whys[i]}</p></div>`;
  }).join('');
  // gender-aware extra suggestion in community
  const alsoHost=document.getElementById('alsoHost');alsoHost.innerHTML='';
  if(k==='community'&&(ctx.gender==='w'||ctx.gender==='m')){
    const extra=ctx.gender==='w'?FLAG['daring-to-be']:FLAG['men-who-win'];
    alsoHost.innerHTML=`<div class="also"><div><b>Also for you: ${extra.t}</b><span>${extra.s}</span></div><a class="btn btn-outline btn-sm" href="campaign.html">Take a look</a></div>`;
  }
  window._first=FLAG[slugs[0]];
  saveProfile();
  initReveal();syncBegin();show('st-path');
}
function chooseBook(i){
  const b=BOOKS[i];ctx.mode='book';ctx.book=b.n;
  chosen={k:'bible',n:b.n,v:'--c-bible'};
  document.getElementById('pathDot').style.background='var(--c-bible)';
  document.getElementById('pathTitle').textContent=b.n;
  document.getElementById('pathLede').textContent=b.note+' These journeys are built on that text — verse-bound, hand-finished, launch-ready.';
  document.getElementById('matchCards').innerHTML=b.m.map(slug=>{
    const f=FLAG[slug];
    return `<div>${campaignCard(f)}<p class="why">\u21b3 Built on ${b.n}.</p></div>`;
  }).join('');
  document.getElementById('alsoHost').innerHTML='';
  window._first=FLAG[b.m[0]];
  saveProfile();
  initReveal();syncBegin();show('st-path');
}
function saveProfile(){
  try{
    localStorage.setItem('lt_profile',JSON.stringify({area:chosen.n,k:chosen.k,v:chosen.v,
      slug:window._first.slug,camp:window._first.t,fmt:fmt,name:ctx.name,
      season:ctx.season,wants:ctx.wants,date:new Date().toISOString()}));
  }catch(e){}
}
function syncBegin(){
  if(!window._first)return;
  const areaKey=(chosen&&chosen.k&&chosen.k!=='bible')?chosen.k:'rhythms';
  document.getElementById('beginBtn').href=`reader.html?a=${areaKey}&c=${window._first.slug}&f=${fmt}&n=${encodeURIComponent(ctx.name)}`;
  document.getElementById('ctaTitle').textContent=`Begin Day One of ${window._first.t} \u2014 free.`;
  saveProfile();
}
</script>
"""

write("assessment.html", "Find My Path — The Lifetogether Assessment", BODY, active="path", head=HEAD, scripts=SCRIPTS)
