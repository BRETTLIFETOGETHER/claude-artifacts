import re
s=open('page_create.py').read()

# ================= CSS =================
s=s.replace("/* canva hand-off modal */","""/* pastor profile */
.pp-sec{background:#fff;border:1px solid var(--line);border-radius:3px;padding:26px 30px;margin-bottom:18px}
.pp-sec>b{font-size:16.5px;color:var(--ink);display:block;margin-bottom:4px}
.pp-sec>.sub{font-size:13.5px;color:var(--mute);margin-bottom:18px;display:block}
.pp-q{margin-bottom:18px}
.pp-q:last-child{margin-bottom:0}
.pp-priv{background:#F4F4EF;border-left:6px solid var(--lt-blue);border-radius:3px;padding:16px 20px;font-size:13.5px;color:#4A4A45;line-height:1.6;margin:0 0 22px}
.pp-done{display:none;background:#EAF0E2;border-left:6px solid var(--lt-green);border-radius:3px;padding:14px 18px;font-size:14px;color:#44622C;margin-bottom:18px}
.pp-grid{display:grid;grid-template-columns:1fr 1fr;gap:14px}
@media(max-width:760px){.pp-grid{grid-template-columns:1fr}}
/* canva hand-off modal */""")

# ================= PROFILE STAGE (before st-upload) =================
PROFILE_STAGE = '''
<!-- STAGE · PASTOR PROFILE -->
<section class="stage" id="st-pprofile">
  <div class="cwrap" style="max-width:860px">
    <span class="eyebrow">Pastor Profile · Church Intelligence</span>
    <h2 class="mt16">Four minutes that make<br>everything <em>yours.</em></h2>
    <p class="lede mt16">Every build gets shaped by this — your voice, your room, your outcomes. Click, don&rsquo;t compose: nothing here is an essay question.</p>
    <div class="pp-priv mt24"><b>For you and you only.</b> Your profile personalizes what the platform builds for you. It is never shared, never published, and never used for anything except your own builds. Every field is optional.</div>
    <div class="pp-done" id="ppDone">✓ Profile on file — saved on this device. Edit anything below and save again.</div>

    <div class="pp-sec">
      <b>You &amp; your church</b>
      <span class="sub">Things to know — so the build fits the room it&rsquo;s walking into.</span>
      <div class="pp-grid">
        <div class="pp-q"><label class="lbl">Your name</label><input class="input" id="ppName" placeholder="Pastor Dave Miller"></div>
        <div class="pp-q"><label class="lbl">Church name</label><input class="input" id="ppChurch" placeholder="Grace Community Church"></div>
      </div>
      <div class="pp-q"><label class="lbl">Weekly attendance</label>
        <div class="pills" data-pp="size">
          <button class="pill" data-v="100 or fewer">100 or fewer</button>
          <button class="pill" data-v="around 250">~250</button>
          <button class="pill" data-v="around 500">~500</button>
          <button class="pill" data-v="around 1,000">~1,000</button>
          <button class="pill" data-v="2,500 or more">2,500+</button>
        </div></div>
      <div class="pp-q"><label class="lbl">Tradition</label>
        <div class="pills" data-pp="denom">
          <button class="pill" data-v="Non-denominational">Non-denominational</button>
          <button class="pill" data-v="Baptist">Baptist</button>
          <button class="pill" data-v="Methodist / Wesleyan">Methodist / Wesleyan</button>
          <button class="pill" data-v="Presbyterian / Reformed">Presbyterian / Reformed</button>
          <button class="pill" data-v="Lutheran">Lutheran</button>
          <button class="pill" data-v="Pentecostal / Charismatic">Pentecostal / Charismatic</button>
          <button class="pill" data-v="Anglican / Episcopal">Anglican / Episcopal</button>
          <button class="pill" data-v="Another tradition">Another</button>
        </div></div>
      <div class="pp-q"><label class="lbl">Who&rsquo;s in front of you most weeks?</label>
        <div class="pills" data-pp="room">
          <button class="pill" data-v="mostly mature believers">Mostly mature believers</button>
          <button class="pill" data-v="a mixed room">A mixed room</button>
          <button class="pill" data-v="many exploring faith">Many exploring faith</button>
        </div></div>
    </div>

    <div class="pp-sec">
      <b>Your teaching</b>
      <span class="sub">Your voice, so the engine writes in it — not over it.</span>
      <div class="pp-q"><label class="lbl">Style <span style="text-transform:none;letter-spacing:0;font-weight:400">(pick up to two)</span></label>
        <div class="pills" data-ppm="style" data-max="2">
          <button class="pill multi" data-v="verse-by-verse">Verse-by-verse</button>
          <button class="pill multi" data-v="topical">Topical</button>
          <button class="pill multi" data-v="thematic series">Thematic series</button>
          <button class="pill multi" data-v="narrative & story-driven">Narrative &amp; story</button>
          <button class="pill multi" data-v="conversational">Conversational</button>
          <button class="pill multi" data-v="bold challenge">Bold challenge</button>
        </div></div>
      <div class="pp-grid">
        <div class="pp-q"><label class="lbl">Typical sermon length</label>
          <div class="pills" data-pp="length">
            <button class="pill" data-v="20–25 min">20–25</button>
            <button class="pill" data-v="30 min">30</button>
            <button class="pill" data-v="35–40 min">35–40</button>
            <button class="pill" data-v="45+ min">45+</button>
          </div></div>
        <div class="pp-q"><label class="lbl">Humor</label>
          <div class="pills" data-pp="humor">
            <button class="pill" data-v="none">None</button>
            <button class="pill" data-v="a little">A little</button>
            <button class="pill" data-v="regularly">Regularly</button>
          </div></div>
      </div>
      <div class="pp-q"><label class="lbl">How personal do you go?</label>
        <div class="pills" data-pp="personal">
          <button class="pill" data-v="guarded">Guarded</button>
          <button class="pill" data-v="selectively open">Selectively open</button>
          <button class="pill" data-v="openly — struggles included">Openly — struggles included</button>
        </div></div>
      <div class="pp-q"><label class="lbl">Voices that have shaped you <span style="text-transform:none;letter-spacing:0;font-weight:400">(tap any, add your own)</span></label>
        <div class="pills" data-ppm="voices" data-max="4">
          <button class="pill multi" data-v="Rick Warren">Rick Warren</button>
          <button class="pill multi" data-v="Max Lucado">Max Lucado</button>
          <button class="pill multi" data-v="Tony Evans">Tony Evans</button>
          <button class="pill multi" data-v="David Jeremiah">David Jeremiah</button>
          <button class="pill multi" data-v="Christine Caine">Christine Caine</button>
          <button class="pill multi" data-v="Craig Groeschel">Craig Groeschel</button>
          <button class="pill multi" data-v="Tim Keller">Tim Keller</button>
        </div>
        <input class="input mt8" id="ppVoicesX" placeholder="Others — commentaries, mentors, theologians…"></div>
    </div>

    <div class="pp-sec">
      <b>Your aims</b>
      <span class="sub">Every sermon leads somewhere. Tell the engine where you&rsquo;re leading.</span>
      <div class="pp-q"><label class="lbl">Primary outcomes <span style="text-transform:none;letter-spacing:0;font-weight:400">(up to three)</span></label>
        <div class="pills" data-ppm="outcomes" data-max="3">
          <button class="pill multi" data-v="take people deeper">Take people deeper</button>
          <button class="pill multi" data-v="move people into groups">Move people into groups</button>
          <button class="pill multi" data-v="mobilize for serving">Mobilize for serving</button>
          <button class="pill multi" data-v="reach people for Christ">Reach people for Christ</button>
          <button class="pill multi" data-v="strengthen families">Strengthen families</button>
          <button class="pill multi" data-v="grow generosity">Grow generosity</button>
          <button class="pill multi" data-v="raise up leaders">Raise up leaders</button>
        </div></div>
      <div class="pp-q"><label class="lbl">Gospel presentation</label>
        <div class="pills" data-pp="gospel">
          <button class="pill" data-v="every week">Every week</button>
          <button class="pill" data-v="when the text calls for it">When the text calls for it</button>
          <button class="pill" data-v="rarely — discipleship focus">Rarely — discipleship focus</button>
        </div></div>
    </div>

    <div class="pp-sec">
      <b>Things to bring</b>
      <span class="sub">All optional. Links and pastes only — nothing to compose. The more you bring, the more the platform sounds like you.</span>
      <div class="pp-grid">
        <div class="pp-q"><label class="lbl">Church website</label><input class="input" id="ppWeb" placeholder="https://…"></div>
        <div class="pp-q"><label class="lbl">Sermon library link <span style="text-transform:none;letter-spacing:0;font-weight:400">(YouTube, podcast, site)</span></label><input class="input" id="ppLib" placeholder="https://…"></div>
      </div>
      <div class="pp-q"><label class="lbl">Mission, vision &amp; values <span style="text-transform:none;letter-spacing:0;font-weight:400">(paste as-is)</span></label>
        <textarea class="input" id="ppMVV" rows="3" placeholder="Paste your church&rsquo;s mission, vision, and values…"></textarea></div>
      <div class="pp-q"><label class="lbl">Ten sermons that best carry your heart <span style="text-transform:none;letter-spacing:0;font-weight:400">(titles or links, one per line — even three helps)</span></label>
        <textarea class="input" id="ppTen" rows="3" placeholder="The sermons that best communicate your passion, theology, and philosophy of ministry…"></textarea></div>
    </div>

    <div class="stage-nav" style="display:flex;justify-content:space-between;gap:14px;flex-wrap:wrap">
      <button class="btn btn-ghost" onclick="go('landing')">← Back</button>
      <button class="btn btn-primary btn-lg" onclick="saveProfilePP()">Save my profile <span class="arrow">→</span></button>
    </div>
  </div>
</section>

'''
i=s.find('<!-- STAGE')  # first stage marker? ensure insertion before upload stage
u=s.find('<section class="stage" id="st-upload"')
s=s[:u]+PROFILE_STAGE+s[u:]

# ================= landing button =================
s=s.replace('''          <a class="btn btn-ghost btn-lg" href="messages.html">No message yet? Start from the Sermon Library →</a>''',
'''          <a class="btn btn-ghost btn-lg" href="messages.html">No message yet? Start from the Sermon Library →</a>
        </div>
        <div class="mt16">
          <button class="btn btn-outline" id="ppEntry" onclick="go('pprofile')">Complete your Pastor Profile · 4 minutes</button>''')

# ================= JS: state, handlers, wiring =================
s=s.replace("/* ---------- prototype account layer","""/* ---------- pastor profile ---------- */
function ppGet(){try{return JSON.parse(localStorage.getItem('lt_pastor_profile')||'null')}catch(e){return null}}
const PP={name:'',church:'',size:'',denom:'',room:'',style:[],length:'',humor:'',personal:'',voices:[],voicesx:'',outcomes:[],gospel:'',web:'',lib:'',mvv:'',ten:''};
function saveProfilePP(){
  PP.name=v('ppName');PP.church=v('ppChurch');PP.voicesx=v('ppVoicesX');
  PP.web=v('ppWeb');PP.lib=v('ppLib');PP.mvv=v('ppMVV');PP.ten=v('ppTen');
  localStorage.setItem('lt_pastor_profile',JSON.stringify({...PP,date:new Date().toISOString()}));
  ppSync();go('landing');
  function v(id){return (document.getElementById(id)||{}).value?.trim()||''}
}
function ppSync(){
  const p=ppGet();
  const e=document.getElementById('ppEntry');
  const d=document.getElementById('ppDone');
  if(!p)return;
  if(e){e.textContent='\\u2713 Pastor Profile on file \\u2014 edit';e.classList.remove('btn-outline');e.classList.add('btn-gold');}
  if(d)d.style.display='block';
  Object.assign(PP,p);
  const set=(id,val)=>{const el=document.getElementById(id);if(el)el.value=val||''};
  set('ppName',p.name);set('ppChurch',p.church);set('ppVoicesX',p.voicesx);
  set('ppWeb',p.web);set('ppLib',p.lib);set('ppMVV',p.mvv);set('ppTen',p.ten);
  document.querySelectorAll('[data-pp]').forEach(g=>{
    g.querySelectorAll('.pill').forEach(b=>b.classList.toggle('sel',b.dataset.v===p[g.dataset.pp]));
  });
  document.querySelectorAll('[data-ppm]').forEach(g=>{
    const arr=p[g.dataset.ppm]||[];
    g.querySelectorAll('.pill').forEach(b=>b.classList.toggle('sel',arr.includes(b.dataset.v)));
  });
}
document.addEventListener('DOMContentLoaded',()=>{
  document.querySelectorAll('[data-pp]').forEach(g=>{
    g.querySelectorAll('.pill').forEach(b=>b.addEventListener('click',()=>{
      g.querySelectorAll('.pill').forEach(x=>x.classList.remove('sel'));
      b.classList.add('sel');PP[g.dataset.pp]=b.dataset.v;
    }));
  });
  document.querySelectorAll('[data-ppm]').forEach(g=>{
    const max=+g.dataset.max||9;
    g.querySelectorAll('.pill').forEach(b=>b.addEventListener('click',()=>{
      const k=g.dataset.ppm;PP[k]=PP[k]||[];
      if(b.classList.contains('sel')){b.classList.remove('sel');PP[k]=PP[k].filter(x=>x!==b.dataset.v);}
      else{if(PP[k].length>=max){const f=PP[k].shift();const fb=g.querySelector(`[data-v="${f}"]`);if(fb)fb.classList.remove('sel');}
        b.classList.add('sel');PP[k].push(b.dataset.v);}
    }));
  });
  ppSync();
  const q=new URLSearchParams(location.search);
  if(q.get('profile')) go('pprofile');
});

/* ---------- prototype account layer""")

# prefs prefill from profile + analysis chip
s=s.replace("""function goPrefs(){""","""function goPrefs(){
  const p=ppGet();
  if(p){
    if(p.church&&!document.getElementById('pChurch').value)document.getElementById('pChurch').value=p.church;
    if(p.name&&!document.getElementById('pPastor').value)document.getElementById('pPastor').value=p.name;
  }""") if "function goPrefs(){" in s else s

# analysis screen chip
s=s.replace("""  document.getElementById('aTone').textContent=analysis.tone;""",
"""  document.getElementById('aTone').textContent=analysis.tone;
  try{
    const p=ppGet();
    const host=document.getElementById('aTone').parentElement;
    let chip=document.getElementById('ppChip');
    if(p&&!chip){
      chip=document.createElement('p');chip.id='ppChip';chip.className='mt8';
      chip.innerHTML=`<span class="chip gold">\\u2713 Pastor Profile applied</span> <span class="small">${[p.style&&p.style.length?p.style.join(' + '):null,p.humor?p.humor+' humor':null,p.room||null].filter(Boolean).join(' \\u00b7 ')} \\u2014 the platform engine reads the full profile.</span>`;
      host.appendChild(chip);
    }
  }catch(e){}""")

open('page_create.py','w').write(s)
print("profile stage installed")

# ================= LIBRARY: profile card =================
s=open('page_account.py').read()
s=s.replace("""  <div class="lib-sec">
    <div class="sh"><h3>My path</h3></div>
    <div id="pathHost"></div>
  </div>""","""  <div class="lib-sec">
    <div class="sh"><h3>My path</h3></div>
    <div id="pathHost"></div>
  </div>

  <div class="lib-sec">
    <div class="sh"><h3>Pastor Profile</h3><span class="small">For you and you only — shapes every build</span></div>
    <div id="ppHost"></div>
  </div>""")
s=s.replace("""  // best of shelf""","""  // pastor profile card
  const pp=JSON.parse(localStorage.getItem('lt_pastor_profile')||'null');
  document.getElementById('ppHost').innerHTML = pp ? `
    <div class="pathcard">
      <div><b style="font-size:16.5px;color:var(--ink)">✓ Profile on file${pp.church?' · '+pp.church:''}</b>
      <div class="small" style="margin-top:4px">${[pp.style&&pp.style.length?pp.style.join(' + '):null,pp.size||null,pp.room||null,(pp.outcomes&&pp.outcomes.length?('aims: '+pp.outcomes.join(', ')):null)].filter(Boolean).join(' · ')||'Saved'}</div></div>
      <a class="btn btn-outline btn-sm" href="create.html?profile=1">Edit profile</a>
    </div>` : `
    <div class="empty">No profile yet. <a href="create.html?profile=1">Four minutes of clicks</a> makes every build sound like you — your voice, your room, your outcomes.</div>`;
  // best of shelf""")
open('page_account.py','w').write(s)
print("library profile card")
