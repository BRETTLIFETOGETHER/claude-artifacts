from shell import write

# ============================== BROWSE ==============================
B_HEAD = """
<style>
.bh-hero{padding:80px 0 56px}
.bh-hero .wrap{max-width:860px;text-align:center;margin:0 auto}
.search{max-width:560px;margin:34px auto 0;position:relative}
.search input{width:100%;font-family:var(--ui);font-size:16px;padding:18px 24px 18px 52px;border-radius:999px;
  border:1.5px solid var(--line);background:var(--paper);box-shadow:var(--shadow);color:var(--ink)}
.search input:focus{outline:none;border-color:var(--green);box-shadow:0 0 0 4px rgba(35,122,82,.12)}
.search .ic{position:absolute;left:22px;top:50%;transform:translateY(-50%);color:var(--mute)}
.search .hint{font-size:12.5px;color:var(--mute);margin-top:12px}
.shelf{display:grid;grid-template-columns:repeat(4,1fr);gap:26px}
.noRes{display:none;text-align:center;padding:40px 0;color:var(--mute);font-size:15px}
.chgrid{display:grid;grid-template-columns:repeat(4,1fr);gap:16px}
.chtile{position:relative;border-radius:16px;padding:22px 20px 18px;text-align:left;overflow:hidden;
  border:1px solid var(--line-soft);background:var(--paper);transition:transform .22s var(--ease),box-shadow .22s;display:block}
.chtile:hover{transform:translateY(-4px);box-shadow:var(--shadow)}
.chtile .swash{position:absolute;top:0;left:0;right:0;height:5px}
.chtile b{display:block;font-size:15px;font-weight:650;color:var(--ink);line-height:1.3;margin-bottom:5px;padding-right:34px}
.chtile span{font-size:12px;color:var(--mute)}
.chtile .cnew{position:absolute;top:14px;right:14px;font-size:9px;font-weight:800;letter-spacing:.12em;background:var(--ink);color:#F1E8CE;padding:4px 8px;border-radius:999px}
.seas{display:grid;grid-template-columns:repeat(3,1fr);gap:26px}
@media(max-width:1080px){.shelf,.chgrid{grid-template-columns:repeat(2,1fr)}.seas{grid-template-columns:1fr}}
@media(max-width:560px){.shelf,.chgrid{grid-template-columns:1fr}}
</style>
"""

B_BODY = """
<section class="bh-hero">
  <div class="wrap">
    <span class="eyebrow bare">The Campaign Library</span>
    <h1 class="mt16">One library.<br>A thousand <em>doors</em>.</h1>
    <p class="lede mt24" style="margin-left:auto;margin-right:auto">Twenty-three formation channels. Over a thousand titles, led by 383 hand-finished flagships — every one with a distinct scriptural backbone, ready to launch churchwide or walk personally.</p>
    <div class="search">
      <span class="ic">⌕</span>
      <input id="q" type="search" placeholder="Search the flagship shelf — try &ldquo;prayer&rdquo;, &ldquo;anxiety&rdquo;, &ldquo;marriage&rdquo;…" autocomplete="off">
      <p class="hint">Searching 24 featured flagships in this preview · the full platform searches the entire catalog</p>
    </div>
  </div>
</section>

<section class="band-white tight" id="flagships">
  <div class="wrap">
    <div class="sec-head" style="margin-bottom:40px">
      <span class="eyebrow gold" style="color:var(--gold-deep)">★ Editors&rsquo; Flagships</span>
      <h2>Hand-finished. <em class="gold">Grade&nbsp;AA.</em></h2>
      <p class="lede">Every flagship is fully built — devotional, group guide, sermon builds, youth and family editions — and certified through forty-five validation gates before it reaches this shelf.</p>
    </div>
    <div class="shelf" id="flagGrid"></div>
    <p class="noRes" id="noRes">Nothing on the flagship shelf matches that — the full platform searches all 16,000+ titles. Try &ldquo;prayer&rdquo;, &ldquo;family&rdquo;, or &ldquo;peace&rdquo;.</p>
  </div>
</section>

<section class="tight">
  <div class="wrap">
    <div class="sec-head" style="margin-bottom:36px">
      <span class="eyebrow">Browse by Formation Channel</span>
      <h2>Twenty-three channels.<br><em>Every</em> season of a life.</h2>
    </div>
    <div class="chgrid" id="chGrid"></div>
    <p class="small mt24">Counts reflect the live master catalog. Channel pages open in the full platform.</p>
  </div>
</section>

<section class="band-sand tight" id="seasonal">
  <div class="wrap">
    <div class="sec-head" style="margin-bottom:36px">
      <span class="eyebrow" style="color:var(--gold-deep)">Seasonal Collections</span>
      <h2>The calendar is a <em class="gold">catechism</em>.</h2>
      <p class="lede">Easter, the new year, generosity season — the moments your whole congregation is already paying attention. Launch into them.</p>
    </div>
    <div class="seas" id="seasGrid"></div>
  </div>
</section>

<section class="band-green tight">
  <div class="wrap" style="display:flex;justify-content:space-between;align-items:center;gap:26px;flex-wrap:wrap">
    <div>
      <h2 style="font-size:clamp(26px,3.2vw,38px)">Not sure which one?</h2>
      <p class="lede" style="color:#DCEBDD">Ten minutes with the assessment turns a thousand doors into three good ones — matched to you.</p>
    </div>
    <a class="btn btn-gold btn-lg" href="assessment.html">Find my path <span class="arrow">→</span></a>
  </div>
</section>
"""

B_SCRIPTS = """
<script>
document.addEventListener('DOMContentLoaded',()=>{
  renderCards('#flagGrid', FLAGSHIPS);
  const seas=[FLAG['easter'],FLAG['new-year'],FLAG['unplugged']];
  renderCards('#seasGrid', seas);
  document.getElementById('chGrid').innerHTML=CHANNELS.map(c=>`
    <a class="chtile" href="#flagships" title="${c.name}">
      <span class="swash" style="background:var(${c.v})"></span>
      ${c.isnew?'<span class="cnew">NEW</span>':''}
      <b>${c.name}</b><span>${c.n.toLocaleString()} titles</span>
    </a>`).join('');
  // live search over flagship shelf
  const q=document.getElementById('q');
  q.addEventListener('input',()=>{
    const t=q.value.trim().toLowerCase();
    const hits=FLAGSHIPS.filter(f=>!t||f.t.toLowerCase().includes(t)||f.s.toLowerCase().includes(t)||CH[f.ch].name.toLowerCase().includes(t));
    renderCards('#flagGrid',hits);
    document.getElementById('noRes').style.display=hits.length?'none':'block';
  });
});
</script>
"""

write("browse.html", "The Campaign Library — Browse by Channel | Lifetogether", B_BODY, active="campaigns", head=B_HEAD, scripts=B_SCRIPTS)


# ============================== CAMPAIGN DETAIL ==============================
C_HEAD = """
<style>
.cd-hero{padding:80px 0 70px}
.cd-hero .wrap{display:grid;grid-template-columns:.9fr 1.1fr;gap:64px;align-items:center}
.cd-cover{width:min(360px,100%);margin:0 auto;border-radius:180px 180px 18px 18px;overflow:hidden;
  box-shadow:0 34px 80px rgba(20,53,42,.24);border:6px solid #fff;position:relative}
.cd-cover .cover{aspect-ratio:4/5}
.cd-meta{display:flex;gap:10px;flex-wrap:wrap;margin:22px 0 26px}
.editions{display:grid;grid-template-columns:repeat(4,1fr);gap:20px}
.ed-card{background:var(--paper);border:1px solid var(--line-soft);border-radius:18px;padding:26px 24px;box-shadow:var(--shadow);border-top:4px solid var(--green)}
.ed-card:nth-child(2){border-top-color:var(--c-prayer)}
.ed-card:nth-child(3){border-top-color:var(--c-family)}
.ed-card:nth-child(4){border-top-color:var(--gold)}
.ed-card b{font-family:var(--display);font-size:18px;font-weight:600;color:var(--ink);display:block;margin-bottom:12px}
.ed-card ul{list-style:none;display:flex;flex-direction:column;gap:8px}
.ed-card li{font-size:13.5px;color:var(--body);display:flex;gap:9px;align-items:flex-start}
.ed-card li::before{content:'✓';color:var(--green);font-weight:700;flex-shrink:0}
.arc{display:grid;grid-template-columns:repeat(5,1fr);gap:0;position:relative;margin-top:44px}
.arc::before{content:'';position:absolute;top:26px;left:9%;right:9%;height:2px;background:var(--line)}
.ph{text-align:center;position:relative;padding:0 12px}
.ph .pnum{width:52px;height:52px;border-radius:26px 26px 8px 8px;margin:0 auto 16px;position:relative;z-index:1;
  display:flex;align-items:center;justify-content:center;font-family:var(--display);font-weight:650;font-size:19px;color:#fff}
.ph b{display:block;font-size:15px;color:var(--ink);margin-bottom:6px}
.ph span{font-size:12.5px;color:var(--body);line-height:1.5}
.frame{background:var(--paper);border:1px solid var(--line-soft);border-radius:22px;padding:34px 38px;box-shadow:var(--shadow)}
.frame h3{margin-bottom:10px}
.frame p{font-size:15px;color:var(--body);line-height:1.7}
.rel{display:grid;grid-template-columns:repeat(3,1fr);gap:26px}
@media(max-width:1080px){.editions{grid-template-columns:repeat(2,1fr)}.arc{grid-template-columns:1fr;gap:22px}.arc::before{display:none}.rel{grid-template-columns:1fr}}
@media(max-width:920px){.cd-hero .wrap{grid-template-columns:1fr}}
@media(max-width:560px){.editions{grid-template-columns:1fr}}
</style>
"""

C_BODY = """
<section class="cd-hero">
  <div class="wrap">
    <div class="cd-cover rv"><div class="cover" id="cdCover"></div></div>
    <div>
      <span class="chip gold">★ Flagship · Grade AA</span>
      <h1 class="mt16" style="font-size:clamp(38px,4.6vw,56px)">40 Days of<br><em>Life Together</em></h1>
      <p class="lede mt16">The flagship groups launch campaign — and the one this platform is named for. Forty days in which a congregation stops attending the same building and starts walking the same road: one church, one conversation, one season of daily life together.</p>
      <div class="cd-meta">
        <span class="chip"><i style="width:8px;height:8px;border-radius:50%;background:var(--c-community);display:inline-block"></i>&nbsp;Community &amp; Belonging</span>
        <span class="chip ink">40 days · also in 30/21/7</span>
        <span class="chip ink">Adult · Youth · Children &amp; Family · Leader</span>
        <span class="chip ink">EN · ES · PT</span>
      </div>
      <div style="display:flex;gap:14px;flex-wrap:wrap">
        <a class="btn btn-primary btn-lg" href="reader.html?a=community&c=life-together&f=40">Preview Day One free <span class="arrow">→</span></a>
        <a class="btn btn-outline btn-lg" href="pricing.html">Launch it at your church</a>
      </div>
    </div>
  </div>
</section>

<section class="band-white tight">
  <div class="wrap">
    <div class="sec-head">
      <span class="eyebrow">Every edition, ready on day one</span>
      <h2>The whole church.<br>The <em>same</em> forty days.</h2>
    </div>
    <div class="editions">
      <div class="ed-card rv"><b>Adult Edition</b><ul>
        <li>40 / 30 / 21 / 7-day devotional</li><li>Journal prompts &amp; prayers</li><li>Memory verse plan</li><li>Print &amp; digital masters</li></ul></div>
      <div class="ed-card rv"><b>Youth / Student Edition</b><ul>
        <li>Re-aimed daily readings</li><li>Leader talk sheets</li><li>Group icebreakers</li><li>Social graphics pack</li></ul></div>
      <div class="ed-card rv"><b>Children &amp; Family Edition</b><ul>
        <li>Family table talks</li><li>Kids&rsquo; activity pages</li><li>Parent cue cards</li><li>Family blessing liturgy</li></ul></div>
      <div class="ed-card rv"><b>Leader Kit</b><ul>
        <li>Host recruiting scripts</li><li>One-evening training</li><li>Session-by-session guide</li><li>Care &amp; follow-up plan</li></ul></div>
    </div>
    <p class="small mt24">Plus complete weekend message builds — title, texts, preaching ideas, and outline. Preach them in your voice.</p>
  </div>
</section>

<section class="tight">
  <div class="wrap">
    <div class="sec-head">
      <span class="eyebrow">The daily arc</span>
      <h2>Five phases. One <em>formation</em>.</h2>
      <p class="lede">Every Lifetogether campaign walks the same proven arc — the architecture beneath twenty-five years of churchwide movements.</p>
    </div>
    <div class="arc">
      <div class="ph rv"><span class="pnum" style="background:var(--c-purpose)">1</span><b>Invitation</b><span>Days 1–5 · A gentle on-ramp. Presence over readiness.</span></div>
      <div class="ph rv"><span class="pnum" style="background:var(--green)">2</span><b>Foundations</b><span>Days 6–15 · The scriptural backbone, laid one text at a time.</span></div>
      <div class="ph rv"><span class="pnum" style="background:var(--c-emotional)">3</span><b>Practice</b><span>Days 16–27 · Truth becomes habit — small, daily, repeatable.</span></div>
      <div class="ph rv"><span class="pnum" style="background:var(--c-family)">4</span><b>Perseverance</b><span>Days 28–35 · When novelty fades, formation begins.</span></div>
      <div class="ph rv"><span class="pnum" style="background:var(--gold)">5</span><b>Commissioning</b><span>Days 36–40 · Sent, not finished. The next season named.</span></div>
    </div>
  </div>
</section>

<section class="band-white tight">
  <div class="wrap grid2">
    <div class="frame rv">
      <span class="eyebrow" style="color:#5A53B8">The smallest structure</span>
      <h3 class="mt8">Spiritual Partner framework</h3>
      <p>Each participant is paired with one partner for the season — one text a day, one honest check-in a week. It is the smallest structure in the campaign and the one people mention most, five years later.</p>
    </div>
    <div class="frame rv">
      <span class="eyebrow" style="color:var(--gold-deep)">Landing the plane</span>
      <h3 class="mt8">Celebration Sunday</h3>
      <p>Every campaign ends with a stories-and-next-steps Sunday — baptism moments, group sign-ups for the next season, and a commissioning blessing. The full plan ships in the Leader Kit.</p>
    </div>
  </div>
</section>

<section class="tight">
  <div class="wrap">
    <div class="sec-head" style="margin-bottom:36px">
      <span class="eyebrow">Keep walking</span>
      <h2>Related <em>campaigns</em></h2>
    </div>
    <div class="rel" id="relGrid"></div>
  </div>
</section>

<section class="band-green tight">
  <div class="wrap" style="display:flex;justify-content:space-between;align-items:center;gap:26px;flex-wrap:wrap">
    <div>
      <h2 style="font-size:clamp(26px,3.2vw,38px)">Launch Life Together at your church.</h2>
      <p class="lede" style="color:#DCEBDD">Every edition, every build, every leader tool — ready before your next planning meeting.</p>
    </div>
    <a class="btn btn-gold btn-lg" href="pricing.html">See plans &amp; pricing <span class="arrow">→</span></a>
  </div>
</section>
"""

C_SCRIPTS = """
<script>
document.addEventListener('DOMContentLoaded',()=>{
  const f=FLAG['life-together'];
  document.getElementById('cdCover').innerHTML=coverSVG(f)+`<span class="cv-days">40 DAYS</span><span class="cv-star">★</span><span class="cv-title" style="font-size:24px">${f.t}</span>`;
  renderCards('#relGrid',[FLAG['better-together'],FLAG['prayer'],FLAG['beloved']]);
});
</script>
"""

write("campaign.html", "40 Days of Life Together — Flagship Campaign | Lifetogether", C_BODY, active="campaigns", head=C_HEAD, scripts=C_SCRIPTS)
