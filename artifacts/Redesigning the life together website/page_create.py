from shell import write

HEAD = """
<style>
.cwrap{max-width:880px;margin:0 auto;padding:0 30px}
.stage{display:none;padding:64px 0 90px;animation:fadeUp .55s var(--ease)}
.stage.on{display:block}
@keyframes fadeUp{from{opacity:0;transform:translateY(16px)}to{opacity:1;transform:none}}
.crumbs{display:flex;gap:8px;align-items:center;font-size:11.5px;font-weight:700;letter-spacing:.13em;text-transform:uppercase;color:var(--mute);margin-bottom:30px;flex-wrap:wrap}
.crumbs b{color:var(--gold-deep)}
.crumbs i{font-style:normal;opacity:.4}
/* landing */
.cl-hero{padding:88px 0 80px}
.cl-hero .wrap{display:grid;grid-template-columns:1.05fr .95fr;gap:60px;align-items:center}
.pull{background:var(--paper);border:1px solid var(--line-soft);border-radius:26px 26px 120px 26px;box-shadow:var(--shadow-lg);padding:38px 40px;position:relative}
.pull .sun{position:absolute;top:-26px;right:34px;width:52px;height:52px;border-radius:26px 26px 10px 10px;background:var(--gold);display:flex;align-items:center;justify-content:center;color:#2B2008;font-size:22px;box-shadow:0 10px 24px rgba(156,114,40,.35)}
.pull blockquote{font-family:var(--display);font-style:italic;font-size:21px;line-height:1.5;color:var(--ink)}
.pull cite{display:block;font-style:normal;font-size:12px;font-weight:700;letter-spacing:.13em;text-transform:uppercase;color:var(--mute);margin-top:16px}
/* upload */
.up{background:var(--paper);border:1.5px dashed #CBBF9C;border-radius:22px;padding:34px;transition:border-color .2s}
.up:focus-within{border-color:var(--gold)}
.up textarea{width:100%;min-height:260px;border:0;resize:vertical;font-family:var(--ui);font-size:15px;line-height:1.7;color:var(--ink);background:transparent}
.up textarea:focus{outline:none}
.up-foot{display:flex;justify-content:space-between;align-items:center;gap:14px;flex-wrap:wrap;border-top:1px solid var(--line-soft);padding-top:18px;margin-top:8px}
.up-foot .wc{font-size:12.5px;color:var(--mute)}
/* analyzing / generating */
.proc{min-height:52vh;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center}
.proc .ring{width:104px;height:104px;border-radius:52px 52px 14px 14px;border:3px solid var(--gold-tint);border-top-color:var(--gold);animation:spin 1.1s linear infinite;margin-bottom:36px}
@keyframes spin{to{transform:rotate(360deg)}}
.proc .pline{font-family:var(--display);font-size:23px;font-weight:560;color:var(--ink);min-height:34px}
/* analysis confirm */
.an{display:flex;flex-direction:column;gap:18px;margin-top:8px}
.an-card{background:var(--paper);border:1px solid var(--line-soft);border-radius:18px;padding:22px 26px;box-shadow:0 4px 14px rgba(20,53,42,.05)}
.an-card .lbl{margin-bottom:10px;display:flex;justify-content:space-between;align-items:center}
.an-card .lbl .edit-note{font-size:11px;letter-spacing:.04em;text-transform:none;font-weight:600;color:var(--gold-deep)}
.an-card [contenteditable]{font-size:16px;line-height:1.6;color:var(--ink);border-radius:8px;padding:2px 4px;margin:-2px -4px}
.an-card [contenteditable]:hover{background:var(--gold-tint)}
.an-card [contenteditable]:focus{outline:2px solid var(--gold);background:#FFFDF6}
.an-card .vlist{display:flex;gap:9px;flex-wrap:wrap}
.an-card .vchip{background:var(--green-tint);color:var(--green-deep);font-weight:650;font-size:13.5px;padding:7px 14px;border-radius:999px}
.an-note{background:var(--gold-tint);border-radius:14px;padding:16px 20px;font-size:14px;color:#5E4A22;line-height:1.6}
/* output selection */
.outs{display:grid;grid-template-columns:1fr 1fr;gap:18px;margin-top:30px}
.out{position:relative;text-align:left;background:var(--paper);border:1.5px solid var(--line-soft);border-radius:18px;padding:26px 28px;transition:all .2s var(--ease)}
.out.avail{cursor:pointer}
.out.avail:hover{border-color:var(--gold);transform:translateY(-3px);box-shadow:var(--shadow)}
.out.soon{opacity:.62}
.out .otag{position:absolute;top:16px;right:16px}
.out b{display:block;font-family:var(--display);font-size:20px;font-weight:600;color:var(--ink);margin-bottom:6px}
.out span{font-size:14px;color:var(--body);line-height:1.55}
/* prefs */
.prefs{display:flex;flex-direction:column;gap:26px;margin-top:30px}
.prefs .row2{display:grid;grid-template-columns:1fr 1fr;gap:22px}
/* editor */
.ed{max-width:1150px;margin:0 auto;padding:0 30px}
.ed-top{display:flex;justify-content:space-between;align-items:center;gap:16px;flex-wrap:wrap;margin-bottom:26px}
.ed-top .meta{font-size:13px;color:var(--mute)}
.ed-grid{display:grid;grid-template-columns:250px 1fr;gap:28px;align-items:start}
.sess-tabs{display:flex;flex-direction:column;gap:8px;position:sticky;top:120px}
.stab{text-align:left;background:var(--paper);border:1.5px solid var(--line-soft);border-radius:13px;padding:14px 16px;transition:all .18s}
.stab:hover{border-color:var(--gold)}
.stab.sel{border-color:var(--gold);background:#FFFCF3;box-shadow:0 6px 16px rgba(196,147,60,.14)}
.stab .sn{font-size:10.5px;font-weight:800;letter-spacing:.14em;color:var(--gold-deep)}
.stab b{display:block;font-size:14px;color:var(--ink);margin-top:3px;line-height:1.3}
.doc{background:var(--paper);border:1px solid var(--line-soft);border-radius:22px;box-shadow:var(--shadow);overflow:hidden}
.doc-head{background:linear-gradient(120deg,#F5EBD4,#FBF5E6);padding:28px 36px;border-bottom:1px solid var(--line-soft)}
.doc-head .chip{margin-bottom:10px}
.doc-head h3{font-size:26px}
.doc-head .dsub{font-size:13px;color:var(--mute);margin-top:6px}
.doc-body{padding:14px 36px 34px}
.blk{padding:22px 0;border-bottom:1px solid var(--line-soft);position:relative}
.blk:last-child{border:0}
.blk .bh{display:flex;justify-content:space-between;align-items:center;margin-bottom:10px}
.blk .bh .lbl{margin:0}
.regen{font-size:12px;font-weight:700;color:var(--gold-deep);background:var(--gold-tint);border-radius:999px;padding:6px 13px;transition:all .18s}
.regen:hover{background:#EFDDB2}
.regen.spun{animation:pulse .5s var(--ease)}
@keyframes pulse{50%{transform:scale(.94)}}
.blk [contenteditable]{font-size:15.5px;line-height:1.75;color:var(--body);border-radius:10px;padding:4px 8px;margin:-4px -8px;white-space:pre-wrap}
.blk [contenteditable] b{color:var(--ink)}
.blk [contenteditable]:hover{background:#FBF8EE}
.blk [contenteditable]:focus{outline:2px solid var(--gold);background:#FFFDF6}
.yw{display:inline-flex;align-items:center;gap:5px;background:var(--gold-tint);border-radius:6px;padding:1px 8px;color:var(--gold-deep);font-weight:650;font-size:12px;white-space:nowrap;vertical-align:1px}
/* export */
.exp-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:20px;margin-top:34px}
.exp{background:var(--paper);border:1.5px solid var(--line-soft);border-radius:18px;padding:28px;text-align:center;transition:all .2s}
.exp:hover{border-color:var(--gold);transform:translateY(-3px);box-shadow:var(--shadow)}
.exp .ei{width:54px;height:54px;border-radius:27px 27px 10px 10px;margin:0 auto 16px;display:flex;align-items:center;justify-content:center;font-size:22px}
.exp b{display:block;font-size:16px;color:var(--ink);margin-bottom:5px}
.exp span{font-size:13px;color:var(--body)}
.next-cards{display:grid;grid-template-columns:1fr 1fr;gap:18px;margin-top:20px}
@media(max-width:920px){
  .cl-hero .wrap,.outs,.prefs .row2,.exp-grid,.next-cards{grid-template-columns:1fr}
  .ed-grid{grid-template-columns:1fr}
  .sess-tabs{position:static;flex-direction:row;overflow-x:auto;padding-bottom:6px}
  .stab{min-width:150px}
}
@media print{
  .util,header.site,footer.site,.ed-top,.sess-tabs,.regen,.crumbs{display:none!important}
  .stage{display:none!important}
  #st-editor.on,#printAll{display:block!important}
  .doc{box-shadow:none;border:0}
  body{background:#fff}
}
</style>
"""

BODY = """
<!-- LANDING -->
<section class="stage on" id="st-landing" style="padding:0">
  <div class="cl-hero">
    <div class="wrap">
      <div>
        <span class="eyebrow" style="color:var(--gold-deep)">For Pastors &amp; Leaders</span>
        <h1 class="mt16" style="font-size:clamp(38px,4.8vw,56px)">Don&rsquo;t let Sunday<br><em class="gold">end</em> on Sunday.</h1>
        <p class="lede mt24">You spent fifteen hours preparing that message. It deserves more than a Monday-morning fade. Upload one sermon and the platform builds the discipleship infrastructure around it — small group curriculum first, devotionals and full 40-day campaigns next — with your words kept visibly at the center.</p>
        <div class="mt32" style="display:flex;gap:14px;flex-wrap:wrap">
          <button class="btn btn-gold btn-lg" onclick="go('upload')">Start with one sermon <span class="arrow">→</span></button>
          <button class="btn btn-outline btn-lg" onclick="loadSample();go('upload')">Try it with a sample</button>
        </div>
        <p class="small mt16">Nothing is stored in this preview — it runs entirely on your device.</p>
      </div>
      <div class="pull rv">
        <span class="sun">✎</span>
        <blockquote>&ldquo;The sermon is the seed. The campaign is the field. Most churches plant on Sunday and never plow — this changes that.&rdquo;</blockquote>
        <cite>The Lifetogether Method · 25 years of churchwide campaigns</cite>
      </div>
    </div>
  </div>
</section>

<!-- UPLOAD -->
<section class="stage" id="st-upload">
  <div class="cwrap">
    <div class="crumbs"><b>1 · Upload</b><i>→</i><span>2 · Confirm</span><i>→</i><span>3 · Choose</span><i>→</i><span>4 · Shape</span><i>→</i><span>5 · Edit &amp; export</span></div>
    <h2>Bring the message<br>you already <em class="gold">preached</em>.</h2>
    <p class="lede mt16">Paste a transcript, your manuscript, or even rough notes. The more of your voice we have, the more of your voice survives into the curriculum.</p>
    <div class="up mt32">
      <textarea id="sermonTxt" placeholder="Paste your sermon here — transcript, manuscript, or notes…"></textarea>
      <div class="up-foot">
        <span class="wc" id="wc">0 words</span>
        <div style="display:flex;gap:12px;flex-wrap:wrap">
          <button class="btn btn-outline btn-sm" onclick="loadSample()">Use a sample sermon</button>
          <button class="btn btn-gold" id="analyzeBtn" onclick="analyze()">Read my sermon <span class="arrow">→</span></button>
        </div>
      </div>
    </div>
    <p class="small mt16">Word docs, PDFs, and audio upload land with the full platform — this preview works from pasted text.</p>
  </div>
</section>

<!-- ANALYZING -->
<section class="stage" id="st-analyzing">
  <div class="cwrap proc">
    <div class="ring"></div>
    <p class="pline" id="anLine">Reading your sermon…</p>
    <p class="small mt16">We read for meaning before we build — big idea, scripture spine, your key points.</p>
  </div>
</section>

<!-- ANALYSIS CONFIRM -->
<section class="stage" id="st-analysis">
  <div class="cwrap">
    <div class="crumbs"><span>1 · Upload</span><i>→</i><b>2 · Confirm</b><i>→</i><span>3 · Choose</span><i>→</i><span>4 · Shape</span><i>→</i><span>5 · Edit &amp; export</span></div>
    <h2>Here&rsquo;s what we <em class="gold">heard</em>.</h2>
    <p class="lede mt16">This is your teaching — correct anything we misread before we build on it. Every field is editable.</p>
    <div class="an mt32">
      <div class="an-card">
        <div class="lbl"><span>The big idea</span><span class="edit-note">✎ click to edit</span></div>
        <p contenteditable="true" id="aBig"></p>
      </div>
      <div class="an-card">
        <div class="lbl"><span>Scripture spine</span></div>
        <div class="vlist" id="aVerses"></div>
      </div>
      <div class="an-card">
        <div class="lbl"><span>Your key points</span><span class="edit-note">✎ click to edit</span></div>
        <div contenteditable="true" id="aPoints" style="font-size:16px;line-height:1.8;color:var(--ink)"></div>
      </div>
      <div class="an-card">
        <div class="lbl"><span>Tone we&rsquo;ll preserve</span><span class="edit-note">✎ click to edit</span></div>
        <p contenteditable="true" id="aTone"></p>
      </div>
      <div class="an-note" id="anNote"></div>
    </div>
    <div class="stage-nav" style="display:flex;justify-content:space-between;margin-top:34px">
      <button class="btn btn-ghost" onclick="go('upload')">← Back</button>
      <button class="btn btn-gold btn-lg" onclick="go('output')">Yes — that&rsquo;s my message <span class="arrow">→</span></button>
    </div>
  </div>
</section>

<!-- OUTPUT SELECTION -->
<section class="stage" id="st-output">
  <div class="cwrap">
    <div class="crumbs"><span>1 · Upload</span><i>→</i><span>2 · Confirm</span><i>→</i><b>3 · Choose</b><i>→</i><span>4 · Shape</span><i>→</i><span>5 · Edit &amp; export</span></div>
    <h2>What should this<br>message <em class="gold">become</em>?</h2>
    <div class="outs">
      <button class="out avail" onclick="go('prefs')">
        <span class="otag chip gold">Ready now</span>
        <b>Small Group Curriculum</b>
        <span>Session-by-session guides with discussion questions, practices, and prayer — the fastest way for Sunday to reach the living room.</span>
      </button>
      <div class="out soon">
        <span class="otag chip ink">Coming soon</span>
        <b>Daily Devotional</b>
        <span>Your series as a daily reading plan — 7, 21, 30, or 40 days in your congregation&rsquo;s hands.</span>
      </div>
      <div class="out soon">
        <span class="otag chip ink">Coming soon</span>
        <b>Leader Guide &amp; Training</b>
        <span>Host scripts, one-evening training, and care plans for the leaders you&rsquo;re about to raise up.</span>
      </div>
      <div class="out soon">
        <span class="otag chip ink">Coming soon</span>
        <b>Full 40-Day Campaign</b>
        <span>The complete churchwide architecture — pulpit, groups, and daily reading aligned around your series.</span>
      </div>
    </div>
    <p class="small mt24"><button class="btn btn-ghost" onclick="go('analysis')" style="padding:0">← Back to what we heard</button></p>
  </div>
</section>

<!-- PREFS -->
<section class="stage" id="st-prefs">
  <div class="cwrap">
    <div class="crumbs"><span>1 · Upload</span><i>→</i><span>2 · Confirm</span><i>→</i><span>3 · Choose</span><i>→</i><b>4 · Shape</b><i>→</i><span>5 · Edit &amp; export</span></div>
    <h2>Shape it for<br><em class="gold">your</em> church.</h2>
    <div class="prefs">
      <div>
        <label class="lbl">Number of sessions</label>
        <div class="pills" id="pSess">
          <button class="pill" data-v="4">4 sessions</button>
          <button class="pill sel" data-v="5">5 sessions</button>
          <button class="pill" data-v="6">6 sessions</button>
        </div>
      </div>
      <div>
        <label class="lbl">Primary audience</label>
        <div class="pills" id="pAud">
          <button class="pill sel" data-v="Adult groups">Adults</button>
          <button class="pill" data-v="Young adult groups">Young adults</button>
          <button class="pill" data-v="Student groups">Students</button>
          <button class="pill" data-v="Men&rsquo;s groups">Men</button>
          <button class="pill" data-v="Women&rsquo;s groups">Women</button>
        </div>
      </div>
      <div>
        <label class="lbl">Voice of the guide</label>
        <div class="pills" id="pTone">
          <button class="pill sel" data-v="warm">Warm &amp; pastoral</button>
          <button class="pill" data-v="direct">Direct &amp; challenging</button>
          <button class="pill" data-v="reflective">Reflective &amp; contemplative</button>
        </div>
      </div>
      <div class="row2">
        <div><label class="lbl">Church name</label><input class="input" id="pChurch" placeholder="Grace Community Church" value="Grace Community Church"></div>
        <div><label class="lbl">Pastor name</label><input class="input" id="pPastor" placeholder="Pastor Dave Miller" value="Pastor Dave Miller"></div>
      </div>
    </div>
    <div style="display:flex;justify-content:space-between;margin-top:38px">
      <button class="btn btn-ghost" onclick="go('output')">← Back</button>
      <button class="btn btn-gold btn-lg" onclick="generate()">Build my curriculum <span class="arrow">→</span></button>
    </div>
  </div>
</section>

<!-- GENERATING -->
<section class="stage" id="st-generating">
  <div class="cwrap proc">
    <div class="ring"></div>
    <p class="pline" id="genLine">Laying the scripture spine…</p>
    <p class="small mt16">Built from your message and the Lifetogether session architecture — your words stay marked throughout.</p>
  </div>
</section>

<!-- EDITOR -->
<section class="stage" id="st-editor">
  <div class="ed">
    <div class="ed-top">
      <div>
        <span class="eyebrow" style="color:var(--gold-deep)">5 · Edit &amp; export</span>
        <h2 style="font-size:clamp(26px,3vw,36px)" id="edTitle"></h2>
        <p class="meta" id="edMeta"></p>
      </div>
      <div style="display:flex;gap:12px;flex-wrap:wrap">
        <button class="btn btn-outline" onclick="go('prefs')">← Reshape</button>
        <button class="btn btn-gold" onclick="finishEdit()">Looks right — export <span class="arrow">→</span></button>
      </div>
    </div>
    <div class="ed-grid">
      <div class="sess-tabs" id="sessTabs"></div>
      <div class="doc" id="docPane"></div>
    </div>
  </div>
  <div id="printAll" style="display:none"></div>
</section>

<!-- EXPORT -->
<section class="stage" id="st-export">
  <div class="cwrap">
    <span class="eyebrow" style="color:var(--gold-deep)">Ready to share</span>
    <h2 class="mt16">Sunday just became<br>a <em class="gold">season</em>.</h2>
    <p class="lede mt16" id="expLede"></p>
    <div class="exp-grid">
      <button class="exp" onclick="downloadDoc()">
        <span class="ei" style="background:#E7EEF9;color:#2B5AA6">W</span>
        <b>Download for Word</b>
        <span>Editable .doc your team can brand and print.</span>
      </button>
      <button class="exp" onclick="window.print()">
        <span class="ei" style="background:#FBEAE4;color:#B5502F">⎙</span>
        <b>Print / Save as PDF</b>
        <span>Every session, formatted for leader packets.</span>
      </button>
      <button class="exp" onclick="alert('Canva hand-off connects in the full platform — your curriculum opens as a branded, editable design.')">
        <span class="ei" style="background:#EAF6F4;color:#1D8A7C">C</span>
        <b>Open in Canva</b>
        <span>Branded visuals in the full platform.</span>
      </button>
    </div>
    <div class="mt48">
      <h3>What this message could become next</h3>
      <div class="next-cards mt16">
        <div class="out soon" style="opacity:1;border-style:dashed">
          <b>The 40-day campaign of this series</b>
          <span>Daily readings, youth &amp; family editions, celebration Sunday — the full churchwide architecture. Rolling out to founding churches first.</span>
        </div>
        <div class="out soon" style="opacity:1;border-style:dashed">
          <b>Your church&rsquo;s formation library</b>
          <span>Every series you&rsquo;ve ever preached, transformed and searchable — a discipleship library in your own voice.</span>
        </div>
      </div>
      <div class="mt32" style="display:flex;gap:14px;flex-wrap:wrap">
        <a class="btn btn-gold btn-lg" href="pricing.html">See founding church pricing <span class="arrow">→</span></a>
        <button class="btn btn-outline btn-lg" onclick="go('editor')">← Back to the editor</button>
      </div>
    </div>
  </div>
</section>
"""

# The interactive engine is large; kept in a separate JS string for clarity.
SCRIPTS = r"""
<script>
/* ================= SAMPLE SERMON ================= */
const SAMPLE = `More Than a Job — Pastor Dave Miller, Grace Community Church

Let me tell you about two carpenters. Both of them showed up to the same job site every morning for thirty years. Somebody once asked the first one what he did for a living, and he said, "I cut wood and drive nails." They asked the second one the same question, and he said, "I build homes where families grow up."

Same tools. Same hours. Same sawdust in their hair at the end of the day. Completely different lives.

Here is what I want you to hear this morning: you are not an accident looking for a reason. Paul writes in Ephesians 2:10 that we are God's handiwork, created in Christ Jesus to do good works, which God prepared in advance for us to do. Prepared in advance. Before you had a resume, God had an assignment.

Most of us have been taught to divide our week — the sacred part on Sunday and the secular part Monday through Friday. But the Bible never makes that division. When God placed Adam in the garden, the very first thing He gave him was work — to tend it and keep it. Work came before the fall. Work is not the curse; it is part of the calling.

So point one this morning: you are made on purpose, for purpose. Not the job title. The assignment underneath the job title.

Point two: your work is worship. Colossians 3:23 — whatever you do, work at it with all your heart, as working for the Lord, not for human masters. Whatever you do. Paul was writing to servants doing work nobody applauded. He didn't say, quit and go do something spiritual. He said, do this — as worship.

I think of Nancy, one of our members, a nurse over at St. Joseph's. Thirty-one years on the night shift. She told me once, "Pastor, I used to think I was just changing IV bags. Now I pray for every patient in every room I walk into. Same rooms. Different job." Nancy understands something the two carpenters teach us: the assignment underneath the assignment.

Point three: your Monday is a mission field. Jesus said in Matthew 5:16, let your light shine before others, that they may see your good deeds and glorify your Father in heaven. The people you work with may never walk into this building. But every Monday, you walk into theirs.

So here is my challenge this week. Don't change your job. Change your answer. When somebody asks what you do — and this week, somebody will — I want you to answer with the assignment, not the task. Ask God this simple question every morning before your feet hit the floor: who is on my schedule today that You have been waiting to love through me?

You are God's handiwork. Created on purpose, for purpose, with work prepared in advance. Sunday is where we say it. Monday is where we prove it. Let's pray.`;

/* ================= PRE-BAKED ANALYSIS ================= */
const SAMPLE_ANALYSIS = {
  big:'You are not an accident looking for a reason — God prepared your work, and your Monday, in advance.',
  verses:['Ephesians 2:10','Colossians 3:23','Genesis 2:15','Matthew 5:16'],
  points:['<b>1.</b> You are made on purpose, for purpose — the assignment underneath the job title.<br><b>2.</b> Your work is worship — whatever you do, done for the Lord.<br><b>3.</b> Your Monday is a mission field — your coworkers may never enter the church, but you enter their world weekly.'],
  tone:'Warm, direct, and story-driven — the two carpenters and Nancy the night-shift nurse carry the message.',
  quotes:['You are not an accident looking for a reason.','Before you had a resume, God had an assignment.','Don\u2019t change your job. Change your answer.','Sunday is where we say it. Monday is where we prove it.']
};

/* ================= SESSION LIBRARY (built from the sermon) ================= */
function sessionLib(q){ return [
 {t:'Made on Purpose', v:'Ephesians 2:10', aim:'Discover that purpose precedes performance — God\u2019s assignment came before your resume.',
  connect:[`Go around the circle: when you were ten years old, what did you want to be when you grew up? What happened to that answer?`,
           `Share the story of a job you\u2019ve held — best or worst. What made it feel meaningful, or meaningless?`],
  recap:`Pastor opened with the two carpenters — same tools, same hours, completely different lives — and anchored the series in Ephesians 2:10: we are God\u2019s handiwork, created in Christ Jesus to do good works, <i>prepared in advance</i>. His line to carry into this session: <span class="yw">✎ your words</span> \u201C${q[0]}\u201D`,
  discuss:[`Read Ephesians 2:10 aloud together. Which word or phrase lands hardest on you today — \u201Chandiwork,\u201D \u201Ccreated,\u201D or \u201Cprepared in advance\u201D? Why?`,
   `The first carpenter said \u201CI cut wood and drive nails.\u201D The second said \u201CI build homes where families grow up.\u201D Which answer sounds more like the one you give — honestly?`,
   `Pastor said, \u201C${q[1]}\u201D What would change this week if you actually believed that?`,
   `Where is the line between healthy ambition and finding your identity in your work? How do you know when you\u2019ve crossed it?`,
   `What is one \u201Cgood work prepared in advance\u201D that might already be sitting in your ordinary week?`],
  practice:`Before your feet hit the floor each morning this week, ask one question: \u201CWho is on my schedule today that God has been waiting to love through me?\u201D Write down one name each day.`,
  pray:{warm:`Close by thanking God for one specific person in the group and the work they do. Let gratitude set the tone for the week.`,
        direct:`Have each person name their workplace out loud. Pray over each one as a mission field — by name, without hurry.`,
        reflective:`Sit in ninety seconds of silence with Ephesians 2:10. Then let anyone who wishes finish this sentence in prayer: \u201CLord, You prepared\u2026\u201D`},
  between:`Read Genesis 2:15 and Psalm 139:13–16. Note where work appears in the story before anything goes wrong.`},
 {t:'Work as Worship', v:'Colossians 3:23', aim:'Reframe every task — applauded or invisible — as something offered to the Lord.',
  connect:[`What is the most invisible task in your week — the one nobody would notice unless you stopped doing it?`,
           `Who is the hardest \u201Chuman master\u201D you\u2019ve ever worked for? (No names required.) What did that season teach you?`],
  recap:`Colossians 3:23 was written to people doing work nobody applauded — and Paul didn\u2019t tell them to escape it, but to offer it: whatever you do, work at it with all your heart, as working for the Lord. Pastor\u2019s summary: <span class="yw">✎ your words</span> \u201CSame rooms. Different job.\u201D — Nancy, thirty-one years on the night shift.`,
  discuss:[`Read Colossians 3:22–24. Paul is writing to servants. How does that context change the weight of \u201Cwhatever you do\u201D?`,
   `Nancy prays for every patient in every room. What would the \u201CNancy version\u201D of your job look like — concretely?`,
   `Where do you most feel the difference between working \u201Cfor human masters\u201D and \u201Cfor the Lord\u201D? What triggers the switch?`,
   `Is there a task you\u2019ve been doing resentfully that could be done as worship instead? What would need to change — the task, or you?`,
   `What does \u201Cwith all your heart\u201D permit — and what does it not require? (Hint: it is not a verse about overwork.)`],
  practice:`Choose your most invisible task this week. Each time you do it, offer it in a one-sentence silent prayer. Notice by Friday what has shifted.`,
  pray:{warm:`Thank God together for work itself — even the parts that are hard — and for the people your work quietly serves.`,
        direct:`Confess out loud, in a word or phrase, where each of you has been working for applause. Receive Colossians 3:24 as the group\u2019s answer.`,
        reflective:`Read Colossians 3:23 three times slowly, with a minute of quiet between readings. Let the room stay unhurried.`},
  between:`Read Colossians 3:22–4:1 in one sitting. Note every phrase addressed to the powerful, not just the servants.`},
 {t:'The Original Job Description', v:'Genesis 2:15', aim:'See that work precedes the fall — it belongs to the blessing, not the curse.',
  connect:[`If all your bills were permanently paid tomorrow, what would you still choose to do with your weekdays? What does your answer reveal?`,
           `What\u2019s a piece of work — a meal, a garden, a spreadsheet, a repair — you\u2019ve finished and simply enjoyed looking at?`],
  recap:`Before there was a fall, there was a garden — and a job. God placed Adam in Eden \u201Cto work it and take care of it.\u201D Pastor put it plainly: <span class="yw">✎ your words</span> \u201CWork came before the fall. Work is not the curse; it is part of the calling.\u201D`,
  discuss:[`Read Genesis 2:15 and Genesis 3:17–19 side by side. What exactly changed about work at the fall — and what didn\u2019t?`,
   `\u201CTend and keep\u201D is gardener\u2019s language. What are you tending in this season of life? What are you keeping?`,
   `How does it change your Monday to know work was God\u2019s idea before it was an economic necessity?`,
   `Where have you experienced the \u201Cthorns and thistles\u201D side of work most sharply? How do you keep that from having the last word?`,
   `Sabbath is part of the same creation story. What does your pattern of rest say about who you believe holds the garden?`],
  practice:`Do one piece of work this week slowly enough to enjoy it — then stop, look at it, and thank God for the strange gift of getting to make things.`,
  pray:{warm:`Pray for each member\u2019s \u201Cgarden\u201D — the specific patch of the world entrusted to them this season.`,
        direct:`Ask God plainly for endurance where work is thorny right now — naming the thorn out loud if you\u2019re willing.`,
        reflective:`Picture your workplace in your mind\u2019s eye. Silently walk through it with Jesus for two minutes. Close with one sentence each.`},
  between:`Read Ecclesiastes 2:24–25 and 3:12–13. Notice how often \u201Ceat, drink, and find satisfaction in work\u201D is called a gift of God.`},
 {t:'Light in the Workplace', v:'Matthew 5:16', aim:'Recognize your Monday as a mission field — presence before persuasion.',
  connect:[`Who was a \u201Clight\u201D in a workplace you\u2019ve been part of? What did they actually do — specifically?`,
           `What percentage of your coworkers, honestly, do you think have a Christian they trust enough to talk to about faith?`,
  ],
  recap:`Jesus\u2019 image was a lamp on a stand — visible, useful, unhidden. Pastor\u2019s point: the people you work with may never walk into the church building, but every Monday you walk into theirs. <span class="yw">✎ your words</span> \u201CThe assignment underneath the assignment.\u201D`,
  discuss:[`Read Matthew 5:14–16. Jesus says \u201Clet your light shine,\u201D not \u201Cmake your light shine.\u201D What\u2019s the difference in practice?`,
   `\u201CThat they may see your good deeds\u201D — what good deeds are actually visible in your workplace? What would your coworkers say you\u2019re known for?`,
   `Where is the line between shining and showing off? Between appropriate witness and workplace pressure?`,
   `Who is one person on your schedule this week who seems far from God? What would loving them well — without an agenda — look like?`,
   `Pastor\u2019s challenge was to change your answer, not your job: \u201C${q[2]}\u201D What is your new answer when someone asks what you do?`],
  practice:`Write the new answer — the assignment, not the task — on a card. Use it at least once this week when someone asks what you do. Report back next session.`,
  pray:{warm:`Pray by name (first names only) for one coworker each. Ask God to let each of you be safe light this week.`,
        direct:`Ask God for one open door this week — and the courage to walk through it without pushing anyone else through theirs.`,
        reflective:`Light a candle if you have one. Sit with Matthew 5:16 while it burns for two minutes. End with the Lord\u2019s Prayer together.`},
  between:`Read 1 Peter 3:15–16 and Colossians 4:5–6. Note the seasoning: gentleness, respect, grace, salt.`},
 {t:'The Long Obedience', v:'Galatians 6:9', aim:'Build the rhythms that keep purpose alive after the series ends.',
  connect:[`What\u2019s something you once started with enthusiasm that quietly faded? What actually made the difference in the things that stuck?`,
           `Which practice from the past month — the morning question, the invisible-task prayer, the new answer — has taken root the most?`],
  recap:`Every campaign ends; the calling doesn\u2019t. Galatians 6:9 says let us not become weary in doing good, for at the proper time we will reap a harvest if we do not give up. This session turns four weeks of ideas into one sustainable rule of life.`,
  discuss:[`Read Galatians 6:9–10. What does \u201Cthe proper time\u201D suggest about harvests you can\u2019t see yet?`,
   `Which of this series\u2019 three points — made on purpose, work as worship, Monday as mission — most needs a structure in your life, not just a memory?`,
   `What is one rhythm (daily question, weekly prayer walk, monthly check-in with a friend) you will commit to for the next ninety days?`,
   `Who in this group will you give permission to ask you about it? Set it now, out loud.`,
   `If this group kept meeting, what would you want to walk through next?`],
  practice:`Write a one-sentence rule of life for your work: \u201CBecause I am God\u2019s handiwork, I will ____ every ____.\u201D Share it with your spiritual partner before Sunday.`,
  pray:{warm:`Close the series by praying a blessing over each person\u2019s workplace, spoken by the person to their left.`,
        direct:`Commission one another: stand, and speak Matthew 5:16 over the group as a sending, not a suggestion.`,
        reflective:`End in unhurried silence, then pray the prayer of examen over the whole series: where was God? what is He asking now?`},
  between:`Celebrate. Share a meal as a group before the next series begins — no curriculum, just the table.`},
 {t:'Commissioned to Monday', v:'Matthew 28:19–20', aim:'Send the group — Sunday is where we say it; Monday is where we prove it.',
  connect:[`As we close the series: what is one sentence you\u2019ll carry from these weeks? Go around the circle — no passing.`,
           `What surprised you most about this group over these sessions?`],
  recap:`The Great Commission was given to ordinary people heading back to ordinary places. Pastor\u2019s closing line is the group\u2019s sending: <span class="yw">✎ your words</span> \u201C${q[3]}\u201D`,
  discuss:[`Read Matthew 28:16–20. Verse 17 says \u201Cbut some doubted\u201D — and Jesus commissioned them anyway. What does that make possible for you?`,
   `\u201CAll authority\u201D comes before \u201Ctherefore go.\u201D How does the order of those sentences steady you for Monday?`,
   `Where is your \u201Call nations\u201D — the specific hallway, job site, inbox, or classroom you\u2019re being sent to?`,
   `What would it look like for this group to commission each other — practically, not just ceremonially?`,
   `Ninety days from now, what do you hope is different because these weeks happened?`],
  practice:`Each person names their Monday mission field out loud. The group responds together: \u201CAnd surely He is with you always.\u201D Then go — and this week, prove it.`,
  pray:{warm:`Lay hands (or simply stretch a hand toward) each member in turn and pray a sending blessing over their week.`,
        direct:`Pray Matthew 28:19–20 as a group charge, then each person answers aloud: \u201CSend me.\u201D`,
        reflective:`Close with two minutes of gratitude in silence, then speak one word each: the word you\u2019re taking into Monday.`},
  between:`This is the sending. Next step: pastor announces the next churchwide campaign — and this group signs up together.`}
];}

/* ================= STATE ================= */
let analysis=null, isSample=false, cur=0;
const prefs={sess:5,aud:'Adult groups',tone:'warm',church:'Grace Community Church',pastor:'Pastor Dave Miller'};
let sessions=[];

function show(id){document.querySelectorAll('.stage').forEach(s=>s.classList.remove('on'));
  document.getElementById(id).classList.add('on');window.scrollTo({top:0});}
function go(k){show('st-'+k)}

function loadSample(){
  document.getElementById('sermonTxt').value=SAMPLE;isSample=true;wcount();
}
document.addEventListener('DOMContentLoaded',()=>{
  const ta=document.getElementById('sermonTxt');
  ta.addEventListener('input',()=>{isSample=false;wcount()});
  ['pSess','pAud','pTone'].forEach(id=>{
    document.querySelectorAll('#'+id+' .pill').forEach(p=>p.addEventListener('click',()=>{
      document.querySelectorAll('#'+id+' .pill').forEach(x=>x.classList.remove('sel'));
      p.classList.add('sel');
      if(id==='pSess')prefs.sess=+p.dataset.v;
      if(id==='pAud')prefs.aud=p.dataset.v;
      if(id==='pTone')prefs.tone=p.dataset.v;
    }));
  });
});
function wcount(){
  const n=document.getElementById('sermonTxt').value.trim().split(/\s+/).filter(Boolean).length;
  document.getElementById('wc').textContent=n+' words';
}

/* ================= ANALYSIS ================= */
const BOOKS='Genesis|Exodus|Leviticus|Numbers|Deuteronomy|Joshua|Judges|Ruth|Samuel|Kings|Chronicles|Ezra|Nehemiah|Esther|Job|Psalm|Psalms|Proverbs|Ecclesiastes|Song|Isaiah|Jeremiah|Lamentations|Ezekiel|Daniel|Hosea|Joel|Amos|Obadiah|Jonah|Micah|Nahum|Habakkuk|Zephaniah|Haggai|Zechariah|Malachi|Matthew|Mark|Luke|John|Acts|Romans|Corinthians|Galatians|Ephesians|Philippians|Colossians|Thessalonians|Timothy|Titus|Philemon|Hebrews|James|Peter|Jude|Revelation';
function analyze(){
  const txt=document.getElementById('sermonTxt').value.trim();
  if(txt.split(/\s+/).length<40){alert('Give us a bit more to read — at least a paragraph or two of your message.');return;}
  show('st-analyzing');
  const lines=['Reading your sermon\u2026','Finding the big idea\u2026','Tracing the scripture spine\u2026','Listening for your voice\u2026'];
  let i=0;const el=document.getElementById('anLine');
  const t=setInterval(()=>{i++;if(i<lines.length){el.textContent=lines[i]}else{clearInterval(t);buildAnalysis(txt)}},900);
}
function buildAnalysis(txt){
  if(isSample){analysis={...SAMPLE_ANALYSIS};}
  else{
    const vre=new RegExp('\\b((?:[1-3]\\s)?(?:'+BOOKS+'))\\s?(\\d+(?::\\d+(?:[\u2013-]\\d+)?)?)','g');
    const verses=[...new Set([...txt.matchAll(vre)].map(m=>m[1]+' '+m[2]))].slice(0,6);
    const sents=txt.replace(/\s+/g,' ').split(/(?<=[.!?])\s/).filter(s=>s.length>40&&s.length<220);
    const big=(sents.find(s=>/\byou\b/i.test(s))||sents[0]||'The heart of your message.').trim();
    const pts=sents.filter(s=>/\b(God|Jesus|Christ|Lord)\b/.test(s)).slice(0,3);
    analysis={big,verses:verses.length?verses:['Add your key passages'],
      points:[pts.map((p,i)=>`<b>${i+1}.</b> ${p}`).join('<br>')||'<b>1.</b> Edit these to match your outline.'],
      tone:'Warm and direct \u2014 refine this to match your voice.',
      quotes:[big, sents[1]||big, sents[2]||big, sents[3]||big]};
  }
  document.getElementById('aBig').textContent=analysis.big;
  document.getElementById('aVerses').innerHTML=analysis.verses.map(v=>`<span class="vchip">${v}</span>`).join('');
  document.getElementById('aPoints').innerHTML=analysis.points[0];
  document.getElementById('aTone').textContent=analysis.tone;
  document.getElementById('anNote').innerHTML=isSample
    ?'<b>Sample mode.</b> This is a demonstration sermon. In the full platform, the analysis runs on Lifetogether\u2019s formation engine and the scripture spine is verified against the licensed NIV corpus before anything is generated.'
    :'<b>Prototype analysis.</b> This preview reads your text with lightweight on-device logic. The full platform runs Lifetogether\u2019s formation engine \u2014 and always shows you this confirmation step before building.';
  show('st-analysis');
}

/* ================= GENERATE ================= */
function generate(){
  prefs.church=document.getElementById('pChurch').value.trim()||'Your Church';
  prefs.pastor=document.getElementById('pPastor').value.trim()||'Your Pastor';
  analysis.big=document.getElementById('aBig').textContent.trim();
  show('st-generating');
  const lines=['Laying the scripture spine\u2026','Drafting sessions in your voice\u2026','Marking your words\u2026','Setting practices and prayers\u2026'];
  let i=0;const el=document.getElementById('genLine');
  const t=setInterval(()=>{i++;if(i<lines.length){el.textContent=lines[i]}else{clearInterval(t);buildDoc()}},900);
}
function buildDoc(){
  const lib=sessionLib(analysis.quotes);
  const pick={4:[0,1,3,5],5:[0,1,2,3,5],6:[0,1,2,3,4,5]}[prefs.sess];
  sessions=pick.map(i=>JSON.parse(JSON.stringify(lib[i])));
  cur=0;
  document.getElementById('edTitle').textContent='More Than a Job \u2014 Small Group Curriculum';
  if(!isSample) document.getElementById('edTitle').textContent='Your Series \u2014 Small Group Curriculum';
  document.getElementById('edMeta').textContent=`${prefs.sess} sessions \u00b7 ${prefs.aud} \u00b7 ${prefs.church} \u00b7 from the teaching of ${prefs.pastor}`;
  renderTabs();renderSession();
  show('st-editor');
}
function renderTabs(){
  document.getElementById('sessTabs').innerHTML=sessions.map((s,i)=>`
    <button class="stab ${i===cur?'sel':''}" onclick="cur=${i};renderTabs();renderSession()">
      <span class="sn">SESSION ${i+1}</span><b>${s.t}</b>
    </button>`).join('');
}
const altConnect={};
function renderSession(){
  const s=sessions[cur];
  const ci=altConnect[cur]||0;
  document.getElementById('docPane').innerHTML=`
    <div class="doc-head">
      <span class="chip gold">Session ${cur+1} of ${sessions.length} \u00b7 ${s.v}</span>
      <h3 contenteditable="true" onblur="sessions[${cur}].t=this.textContent">${s.t}</h3>
      <p class="dsub">${prefs.aud} \u00b7 ${prefs.church} \u00b7 from the teaching of ${prefs.pastor}</p>
    </div>
    <div class="doc-body">
      <div class="blk"><div class="bh"><label class="lbl">The aim</label></div>
        <p contenteditable="true" onblur="sessions[${cur}].aim=this.textContent">${s.aim}</p></div>
      <div class="blk"><div class="bh"><label class="lbl">Connect · 10 min</label>
        <button class="regen" onclick="regenConnect(this)">\u21bb Try another</button></div>
        <p contenteditable="true" id="connectBlk">${s.connect[ci%s.connect.length]}</p></div>
      <div class="blk"><div class="bh"><label class="lbl">From Sunday · 5 min</label></div>
        <p contenteditable="true">${s.recap}</p></div>
      <div class="blk"><div class="bh"><label class="lbl">Discuss · 35 min</label></div>
        <p contenteditable="true">${s.discuss.map((q,i)=>`<b>${i+1}.</b> ${q}`).join('<br><br>')}</p></div>
      <div class="blk"><div class="bh"><label class="lbl">Practice · this week</label></div>
        <p contenteditable="true">${s.practice}</p></div>
      <div class="blk"><div class="bh"><label class="lbl">Pray · 10 min</label></div>
        <p contenteditable="true">${s.pray[prefs.tone]}</p></div>
      <div class="blk"><div class="bh"><label class="lbl">Between sessions</label></div>
        <p contenteditable="true">${s.between}</p></div>
    </div>`;
}
function regenConnect(btn){
  btn.classList.remove('spun');void btn.offsetWidth;btn.classList.add('spun');
  altConnect[cur]=(altConnect[cur]||0)+1;
  const s=sessions[cur];
  document.getElementById('connectBlk').innerHTML=s.connect[altConnect[cur]%s.connect.length];
}
function finishEdit(){
  document.getElementById('expLede').textContent=
    `${sessions.length} sessions are ready for ${prefs.church} \u2014 built from ${prefs.pastor==='Your Pastor'?'your':'Pastor '+prefs.pastor.replace(/^Pastor\s+/i,'')+'\u2019s'} own message, edited by you, ready for your leaders.`;
  buildPrint();
  show('st-export');
}
/* print + word export */
function docHTML(){
  return sessions.map((s,i)=>`
    <div style="page-break-after:always;font-family:Georgia,serif;max-width:680px;margin:0 auto 40px">
      <p style="font-size:11px;letter-spacing:2px;color:#9C7228;font-weight:bold">SESSION ${i+1} \u00b7 ${s.v.toUpperCase()}</p>
      <h2 style="font-size:26px;color:#14352A;margin:6px 0 2px">${s.t}</h2>
      <p style="font-size:12px;color:#777">${prefs.aud} \u00b7 ${prefs.church} \u00b7 from the teaching of ${prefs.pastor}</p>
      <h4 style="color:#237A52">The aim</h4><p>${s.aim}</p>
      <h4 style="color:#237A52">Connect \u00b7 10 min</h4><p>${s.connect[(altConnect[i]||0)%s.connect.length]}</p>
      <h4 style="color:#237A52">From Sunday \u00b7 5 min</h4><p>${s.recap.replace(/<span class="yw">[^<]*<\/span>/g,'[your words] ')}</p>
      <h4 style="color:#237A52">Discuss \u00b7 35 min</h4><p>${s.discuss.map((q,qi)=>`<b>${qi+1}.</b> ${q}`).join('<br><br>')}</p>
      <h4 style="color:#237A52">Practice \u00b7 this week</h4><p>${s.practice}</p>
      <h4 style="color:#237A52">Pray \u00b7 10 min</h4><p>${s.pray[prefs.tone]}</p>
      <h4 style="color:#237A52">Between sessions</h4><p>${s.between}</p>
    </div>`).join('');
}
function buildPrint(){document.getElementById('printAll').innerHTML=docHTML();}
function downloadDoc(){
  const html=`<html xmlns:w="urn:schemas-microsoft-com:office:word"><head><meta charset="utf-8"><title>Curriculum</title></head><body>${docHTML()}</body></html>`;
  const blob=new Blob(['\ufeff',html],{type:'application/msword'});
  const a=document.createElement('a');
  a.href=URL.createObjectURL(blob);
  a.download='Small-Group-Curriculum.doc';a.click();URL.revokeObjectURL(a.href);
}
</script>
"""

write("create.html", "For Pastors & Leaders — Transform a Sermon | Lifetogether", BODY, active="pastors", head=HEAD, scripts=SCRIPTS)
