from shell import write

# ============================== LOGIN ==============================
L_HEAD = """
<style>
.login-wrap{max-width:980px;margin:0 auto;padding:70px 30px 100px;display:grid;grid-template-columns:1fr 1fr;gap:64px;align-items:center}
.login-card{background:#fff;border:1px solid var(--line);border-radius:3px;box-shadow:var(--shadow-lg);padding:42px}
.login-card h2{font-size:30px;margin-bottom:8px}
.login-card .sub{font-size:14.5px;color:var(--mute);margin-bottom:26px}
.login-card .fld{margin-bottom:18px}
.login-tabs{display:flex;gap:0;margin-bottom:28px;border-bottom:2px solid var(--line)}
.login-tabs button{font-family:var(--display);font-size:14px;font-weight:600;letter-spacing:.14em;text-transform:uppercase;padding:12px 20px;color:var(--mute);border-bottom:3px solid transparent;margin-bottom:-2px}
.login-tabs button.sel{color:var(--ink);border-bottom-color:var(--lt-green)}
.login-note{background:#F4F4EF;border:1px solid var(--line);border-radius:3px;padding:14px 18px;font-size:13px;color:#5A5A52;line-height:1.6;margin-top:22px}
.login-side .pt{display:flex;gap:14px;align-items:flex-start;margin-top:22px}
.login-side .pt i{width:34px;height:34px;flex-shrink:0;border-radius:2px;background:#EAF0E2;color:#5F8540;display:flex;align-items:center;justify-content:center;font-style:normal;font-weight:700}
.login-side .pt b{display:block;font-size:15.5px;color:var(--ink)}
.login-side .pt span{font-size:14px;color:var(--body);line-height:1.55}
@media(max-width:920px){.login-wrap{grid-template-columns:1fr;gap:40px}}
</style>
"""

L_BODY = """
<div class="login-wrap">
  <div class="login-side">
    <span class="eyebrow">Your Lifetogether account</span>
    <h1 class="mt16" style="font-size:clamp(34px,4.4vw,50px)">One library.<br><em>Yours</em> and ours.</h1>
    <p class="lede mt16">Sign in to keep everything in one place — the sermons you upload, the curriculum the platform builds from them, your assessment path, and the best of the Lifetogether flagship library.</p>
    <div class="pt"><i>✓</i><div><b>Upload your teaching library</b><span>Every sermon you bring in is saved, analyzed, and ready to become curriculum whenever you are.</span></div></div>
    <div class="pt"><i>✓</i><div><b>Keep what the platform builds</b><span>Generated curricula stay in your library — reopen, re-edit, and re-export any time.</span></div></div>
    <div class="pt"><i>✓</i><div><b>The best of Lifetogether, built in</b><span>The flagship shelf sits beside your own work — one library, both sources.</span></div></div>
  </div>
  <div class="login-card">
    <div class="login-tabs">
      <button class="sel" id="tabIn" onclick="tab('in')">Sign in</button>
      <button id="tabUp" onclick="tab('up')">Create account</button>
    </div>
    <h2 id="formTitle">Welcome back.</h2>
    <p class="sub" id="formSub">Your library is waiting.</p>
    <div class="fld" id="nameFld" style="display:none">
      <label class="lbl">Your name</label>
      <input class="input" id="fName" placeholder="Pastor Dave Miller">
    </div>
    <div class="fld" id="churchFld" style="display:none">
      <label class="lbl">Church</label>
      <input class="input" id="fChurch" placeholder="Grace Community Church">
    </div>
    <div class="fld">
      <label class="lbl">Email</label>
      <input class="input" id="fEmail" type="email" placeholder="you@yourchurch.org">
    </div>
    <div class="fld">
      <label class="lbl">Password</label>
      <input class="input" id="fPass" type="password" placeholder="••••••••">
    </div>
    <button class="btn btn-primary btn-lg" style="width:100%;justify-content:center" onclick="doAuth()">Enter my library <span class="arrow">→</span></button>
    <div class="login-note"><b>Prototype sign-in.</b> This preview stores your session on this device only — no server, no real password check. The production platform uses secure accounts with church-level roles.</div>
  </div>
</div>
"""

L_SCRIPTS = """
<script>
let mode='in';
function tab(m){
  mode=m;
  document.getElementById('tabIn').classList.toggle('sel',m==='in');
  document.getElementById('tabUp').classList.toggle('sel',m==='up');
  document.getElementById('nameFld').style.display=m==='up'?'block':'none';
  document.getElementById('churchFld').style.display=m==='up'?'block':'none';
  document.getElementById('formTitle').textContent=m==='in'?'Welcome back.':'Start your library.';
  document.getElementById('formSub').textContent=m==='in'?'Your library is waiting.':'Free while the platform is in preview.';
}
function doAuth(){
  const email=document.getElementById('fEmail').value.trim();
  if(!email||!email.includes('@')){alert('Enter your email to continue.');return;}
  const existing=ltUser();
  const name=(mode==='up'?document.getElementById('fName').value.trim():'')||(existing&&existing.name)||email.split('@')[0].replace(/[._-]/g,' ').replace(/\\b\\w/g,c=>c.toUpperCase());
  const church=(mode==='up'?document.getElementById('fChurch').value.trim():'')||(existing&&existing.church)||'';
  ltSetUser({email,name,church,since:existing&&existing.since||new Date().toISOString()});
  location.href='library.html';
}
document.addEventListener('DOMContentLoaded',()=>{
  const u=ltUser();
  if(u){document.getElementById('fEmail').value=u.email;}
});
</script>
"""

write("login.html", "Sign In — Your Lifetogether Library", L_BODY, active="", head=L_HEAD, scripts=L_SCRIPTS)


# ============================== MY LIBRARY ==============================
LIB_HEAD = """
<style>
.lib{max-width:1180px;margin:0 auto;padding:60px 30px 100px}
.lib-top{display:flex;justify-content:space-between;align-items:flex-end;gap:20px;flex-wrap:wrap;margin-bottom:16px}
.lib-top .who{font-size:14px;color:var(--mute)}
.lib-bars{display:flex;gap:10px;flex-wrap:wrap;margin:26px 0 44px}
.lib-sec{margin-bottom:64px}
.lib-sec .sh{display:flex;justify-content:space-between;align-items:center;gap:16px;flex-wrap:wrap;margin-bottom:22px}
.itемs{}
.item-list{display:flex;flex-direction:column;gap:12px}
.itm{background:#fff;border:1px solid var(--line);border-left:6px solid var(--lt-blue);border-radius:3px;padding:20px 24px;display:flex;justify-content:space-between;align-items:center;gap:18px;flex-wrap:wrap}
.itm.sermon{border-left-color:var(--lt-green)}
.itm.cur{border-left-color:var(--lt-orange)}
.itm b{display:block;font-size:16.5px;color:var(--ink)}
.itm .meta{font-size:12.5px;color:var(--mute);margin-top:3px}
.itm .acts{display:flex;gap:10px;flex-wrap:wrap}
.empty{background:#F4F4EF;border:1px dashed #C9C9BE;border-radius:3px;padding:34px;text-align:center;color:var(--mute);font-size:15px}
.empty a{color:var(--lt-orange);font-weight:700}
.pathcard{background:#fff;border:1px solid var(--line);border-radius:3px;padding:26px 28px;display:flex;justify-content:space-between;align-items:center;gap:20px;flex-wrap:wrap}
.pathcard .dot{width:12px;height:12px;display:inline-block;margin-right:8px}
.shelf4{display:grid;grid-template-columns:repeat(4,1fr);gap:24px}
@media(max-width:1080px){.shelf4{grid-template-columns:repeat(2,1fr)}}
@media(max-width:560px){.shelf4{grid-template-columns:1fr}}
</style>
"""

LIB_BODY = """
<div class="lib">
  <div class="lib-top">
    <div>
      <span class="eyebrow">My Library</span>
      <h1 class="mt16" style="font-size:clamp(32px,4.2vw,48px)" id="libGreet">Your library.</h1>
      <p class="who" id="libWho"></p>
    </div>
    <div style="display:flex;gap:12px;flex-wrap:wrap">
      <a class="btn btn-primary" href="create.html">Upload a sermon</a>
      <button class="btn btn-outline" onclick="ltSignOut()">Sign out</button>
    </div>
  </div>
  <div class="lib-bars">
    <span class="lbl-bar green">My Uploads</span>
    <span class="lbl-bar orange">My Curriculum</span>
    <span class="lbl-bar blue">My Path</span>
    <span class="lbl-bar gray">Lifetogether Flagships</span>
  </div>

  <div class="lib-sec">
    <div class="sh"><h3>Uploaded sermons</h3><span class="small">Saved on this device in the preview</span></div>
    <div class="item-list" id="sermonList"></div>
  </div>

  <div class="lib-sec">
    <div class="sh"><h3>Generated curriculum</h3><span class="small">Reopen to edit or export again</span></div>
    <div class="item-list" id="curList"></div>
  </div>

  <div class="lib-sec">
    <div class="sh"><h3>My path</h3></div>
    <div id="pathHost"></div>
  </div>

  <div class="lib-sec">
    <div class="sh"><h3>The best of Lifetogether</h3><a class="btn btn-outline btn-sm" href="browse.html">Full library →</a></div>
    <div class="shelf4" id="bestShelf"></div>
  </div>
</div>
"""

LIB_SCRIPTS = """
<script>
document.addEventListener('DOMContentLoaded',()=>{
  const u=ltUser();
  if(!u){location.href='login.html';return;}
  const first=u.name.split(' ')[0];
  document.getElementById('libGreet').innerHTML=`${first}&rsquo;s library.`;
  document.getElementById('libWho').textContent=`${u.email}${u.church?' · '+u.church:''}`;

  // sermons
  const sermons=ltGet('lt_sermons');
  document.getElementById('sermonList').innerHTML = sermons.length ? sermons.map(s=>`
    <div class="itm sermon">
      <div><b>${s.title}</b><span class="meta">${s.words} words · uploaded ${new Date(s.date).toLocaleDateString()}</span></div>
      <div class="acts">
        <a class="btn btn-primary btn-sm" href="create.html?draft=${s.id}">Build from this</a>
        <button class="btn btn-outline btn-sm" onclick="ltDel('lt_sermons','${s.id}');location.reload()">Remove</button>
      </div>
    </div>`).join('') :
    `<div class="empty">No sermons yet. <a href="create.html">Upload your first message</a> — it saves here automatically.</div>`;

  // curricula
  const curs=ltGet('lt_curricula');
  document.getElementById('curList').innerHTML = curs.length ? curs.map(c=>`
    <div class="itm cur">
      <div><b>${c.title}</b><span class="meta">${c.sessions} sessions · ${c.church} · saved ${new Date(c.date).toLocaleDateString()}</span></div>
      <div class="acts">
        <a class="btn btn-primary btn-sm" href="create.html?cur=${c.id}">Reopen in the studio</a>
        <button class="btn btn-outline btn-sm" onclick="ltDel('lt_curricula','${c.id}');location.reload()">Remove</button>
      </div>
    </div>`).join('') :
    `<div class="empty">Nothing generated yet. Build a curriculum from any uploaded sermon and it will live here.</div>`;

  // path
  const pf=JSON.parse(localStorage.getItem('lt_profile')||'null');
  document.getElementById('pathHost').innerHTML = pf ? `
    <div class="pathcard">
      <div><b style="font-family:var(--display);font-size:19px;letter-spacing:.05em;text-transform:uppercase;color:var(--ink)"><span class="dot" style="background:var(${pf.v})"></span>${pf.area}</b>
      <div class="small" style="margin-top:4px">Taken ${new Date(pf.date).toLocaleDateString()} · ${pf.fmt}-day path · first campaign: ${pf.camp}</div></div>
      <a class="btn btn-primary btn-sm" href="reader.html?a=${pf.k}&c=${pf.slug}&f=${pf.fmt}&n=${encodeURIComponent(pf.name||'')}">Continue Day One →</a>
    </div>` :
    `<div class="empty">You haven&rsquo;t taken the assessment yet. <a href="assessment.html">Find your path</a> in about ten minutes.</div>`;

  // best of shelf
  renderCards('#bestShelf',[FLAG['life-together'],FLAG['prayer'],FLAG['purpose'],FLAG['god-owns-it-all'],FLAG['living-light'],FLAG['a-life-worth'],FLAG['soul-care'],FLAG['proverbs']]);
});
</script>
"""

write("library.html", "My Library — Lifetogether", LIB_BODY, active="", head=LIB_HEAD, scripts=LIB_SCRIPTS)
