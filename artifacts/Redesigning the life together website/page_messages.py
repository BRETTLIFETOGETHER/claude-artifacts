from shell import write

HEAD = """
<style>
.ms-hero{padding:76px 0 56px;text-align:center}
.ms-hero .wrap{max-width:900px}
.proof{display:flex;justify-content:center;gap:54px;flex-wrap:wrap;margin-top:36px;border-top:2px dotted #C9C9BE;padding-top:28px}
.proof b{font-family:var(--display);font-size:40px;color:var(--ink);display:block;line-height:1}
.proof span{font-family:var(--display);font-size:11px;letter-spacing:.2em;text-transform:uppercase;color:var(--mute)}
.msearch{max-width:560px;margin:30px auto 0;position:relative}
.msearch input{width:100%;font-family:var(--ui);font-size:16px;padding:16px 22px;border:2px solid var(--line);border-radius:3px;background:#fff}
.msearch input:focus{outline:none;border-color:var(--lt-green)}
.built{display:grid;grid-template-columns:repeat(4,1fr);gap:22px}
.bm{background:#fff;border:1px solid var(--line);border-top:6px solid var(--lt-orange);border-radius:3px;padding:24px;display:flex;flex-direction:column;text-align:left}
.bm .bcat{font-family:var(--display);font-size:10.5px;letter-spacing:.2em;text-transform:uppercase;color:var(--mute)}
.bm b{font-size:18px;color:var(--ink);margin:8px 0 5px;line-height:1.25}
.bm .bs{font-size:13.5px;color:var(--body);line-height:1.5}
.bm .bx{font-family:var(--display);font-size:11px;letter-spacing:.14em;color:var(--lt-green-deep);margin:12px 0 4px}
.bm .bb{font-size:13px;color:var(--body);font-style:italic;font-family:var(--wordmark)}
.bm .btn{margin-top:auto;justify-content:center;margin-top:16px}
.vchips{display:flex;gap:9px;flex-wrap:wrap;margin:0 0 26px}
.catgrid{display:grid;grid-template-columns:1fr 1fr;gap:18px}
.catcard{background:#fff;border:1px solid var(--line);border-radius:3px;overflow:hidden}
.catcard summary{list-style:none;cursor:pointer;padding:20px 24px}
.catcard summary::-webkit-details-marker{display:none}
.catcard .cn{display:flex;justify-content:space-between;align-items:center;gap:12px}
.catcard .cn b{font-size:17px;color:var(--ink)}
.catcard .cn .cnt{font-family:var(--display);font-size:11px;letter-spacing:.14em;color:var(--mute);white-space:nowrap}
.catcard .ce{font-size:13.5px;color:var(--body);line-height:1.55;margin-top:6px}
.catcard .cx{font-size:13px;color:var(--lt-green-deep);margin-top:10px;padding-left:12px;border-left:3px solid var(--lt-green)}
.catcard .titles{border-top:2px dotted #DDDDD5;padding:14px 24px 20px;max-height:340px;overflow:auto}
.trow{display:flex;justify-content:space-between;gap:12px;align-items:baseline;padding:8px 0;border-bottom:1px solid #F0F0EA}
.trow div b{font-size:14.5px;color:var(--ink);font-weight:600}
.trow div span{display:block;font-size:12.5px;color:var(--mute)}
.trow a{font-size:12px;font-weight:700;color:var(--lt-orange);white-space:nowrap}
.subhead{font-family:var(--display);font-size:11px;letter-spacing:.18em;text-transform:uppercase;color:var(--mute);margin:12px 0 4px}
.noRes{display:none;text-align:center;color:var(--mute);padding:30px 0}
@media(max-width:1080px){.built{grid-template-columns:repeat(2,1fr)}.catgrid{grid-template-columns:1fr}}
@media(max-width:560px){.built{grid-template-columns:1fr}}
</style>
"""

BODY = """
<section class="ms-hero">
  <div class="wrap">
    <span class="eyebrow bare">The Sermon Library · Catalytic Sundays</span>
    <h1 class="mt16">They come for a sermon.<br>They leave with a <em>strategy.</em></h1>
    <p class="lede mt24" style="margin:24px auto 0">A sermon is one hour. A Sunday is a season. Browse the message library free — every title, every angle — then let one message become the whole week: the service, the dailies, the group room, the students, and the household, pointed at the same next step.</p>
    <div class="proof" id="proofRow"></div>
    <div class="msearch"><input id="mq" type="search" placeholder="Search 5,155 message titles — try &ldquo;prodigal&rdquo;, &ldquo;anxiety&rdquo;, &ldquo;money&rdquo;…" autocomplete="off"></div>
  </div>
</section>

<section class="band-white tight">
  <div class="wrap">
    <div class="sec-head" style="margin-bottom:32px">
      <span class="eyebrow" style="color:var(--lt-orange)">Built and ready</span>
      <h2>Eight messages, fully <em>finished.</em></h2>
      <p class="lede">Complete builds — outline, draft, devotional week, family edition, service kit. Open one in the studio and this Sunday&rsquo;s whole kit is minutes away.</p>
    </div>
    <div class="built" id="builtGrid"></div>
  </div>
</section>

<section class="tight">
  <div class="wrap">
    <div class="sec-head" style="margin-bottom:24px">
      <span class="eyebrow">Browse the library</span>
      <h2>Seventy-three categories.<br>Every Sunday <em>covered.</em></h2>
    </div>
    <div class="vchips pills" id="vchips"></div>
    <div class="catgrid" id="catGrid"></div>
    <p class="noRes" id="mNoRes">No titles match — try a broader word.</p>
    <p class="small mt24">Every title and outline is free to browse. The kit around it — the twenty-five pieces — is what the platform builds.</p>
  </div>
</section>

<section class="band-green tight">
  <div class="wrap" style="display:flex;justify-content:space-between;align-items:center;gap:26px;flex-wrap:wrap">
    <div>
      <h2 style="font-size:clamp(24px,3vw,34px);color:#fff">Have this week&rsquo;s message already?</h2>
      <p class="lede" style="color:#E4EFD8">Drop it in the studio and the kit builds around your words instead.</p>
    </div>
    <a class="btn btn-primary btn-lg" href="create.html">Open the studio <span class="arrow">→</span></a>
  </div>
</section>
"""

SCRIPTS = """
<script src="assets/msglib.js"></script>
<script>
document.addEventListener('DOMContentLoaded',()=>{
  const L=window.MSGLIB;
  document.getElementById('proofRow').innerHTML=L.proof.map(p=>`<div><b>${p[0]}</b><span>${p[1]}</span></div>`).join('');
  // eight built messages
  document.getElementById('builtGrid').innerHTML=L.sermons.map((s,i)=>`
    <div class="bm">
      <span class="bcat">${s.cat}</span>
      <b>${s.t}</b>
      <span class="bs">${s.s}</span>
      <span class="bx">${s.x}</span>
      <span class="bb">&ldquo;${s.b}&rdquo;</span>
      <a class="btn btn-primary btn-sm" href="create.html?msg=${i}">Build this week&rsquo;s kit →</a>
    </div>`).join('');
  // verticals + categories
  const verts=[...new Set(L.cats.map(c=>c.v))];
  let curV=verts[0];
  const vc=document.getElementById('vchips');
  vc.innerHTML=verts.map(v=>`<button class="pill ${v===curV?'sel':''}" data-v="${v}">${v}</button>`).join('');
  vc.querySelectorAll('.pill').forEach(b=>b.addEventListener('click',()=>{
    curV=b.dataset.v;vc.querySelectorAll('.pill').forEach(x=>x.classList.remove('sel'));b.classList.add('sel');
    document.getElementById('mq').value='';renderCats();
  }));
  function count(c){return c.t.reduce((a,g)=>a+g.i.length,0)}
  function catCard(c,ci,openAll,filter){
    const groups=c.t.map(g=>{
      let rows=g.i.map((m,mi)=>({t:m[0],s:m[1],g:g.n,mi}));
      if(filter)rows=rows.filter(r=>(r.t+' '+r.s).toLowerCase().includes(filter));
      if(!rows.length)return '';
      return (g.n?`<p class="subhead">${g.n}</p>`:'')+rows.map(r=>`
        <div class="trow"><div><b>${r.t}</b><span>${r.s}</span></div>
        <a href="create.html?seed=${encodeURIComponent(c.n+'|'+r.t+'|'+r.s)}">Use this →</a></div>`).join('');
    }).join('');
    if(filter&&!groups)return '';
    return `<details class="catcard" ${openAll?'open':''}>
      <summary><div class="cn"><b>${c.n}</b><span class="cnt">${count(c)} titles</span></div>
        <p class="ce">${c.e}</p>
        <p class="cx"><b>The catalytic move:</b> ${c.x}</p></summary>
      <div class="titles">${groups||''}</div>
    </details>`;
  }
  function renderCats(filter){
    const host=document.getElementById('catGrid');
    let cats=filter?L.cats:L.cats.filter(c=>c.v===curV);
    const html=cats.map((c,ci)=>catCard(c,ci,!!filter,filter)).filter(Boolean).join('');
    host.innerHTML=html;
    document.getElementById('mNoRes').style.display=html?'none':'block';
  }
  renderCats();
  document.getElementById('mq').addEventListener('input',e=>{
    const t=e.target.value.trim().toLowerCase();
    renderCats(t||undefined);
  });
});
</script>
"""

write("messages.html", "The Sermon Library — 5,155 Catalytic Messages | Lifetogether", BODY, active="messages", head=HEAD, scripts=SCRIPTS)
