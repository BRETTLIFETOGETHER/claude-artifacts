# -*- coding: utf-8 -*-
p = "/mnt/user-data/outputs/faith-through-art-studio.html"
s = open(p).read()

# ---------- 1. CSS additions ----------
css_anchor = "  .hide{display:none;}"
css_new = """  .hide{display:none;}
  .bubs{display:flex;flex-wrap:wrap;gap:7px;margin:.35rem 0 0;}
  .bub{
    font-family:inherit;font-size:.83rem;font-weight:500;padding:8px 14px;
    border:1px solid var(--line);background:#fff;color:var(--ink);
    border-radius:22px;cursor:pointer;line-height:1.3;text-align:left;
  }
  .bub:hover{border-color:var(--clay);}
  .bub.on{background:var(--plum);border-color:var(--plum);color:#fff;}
  .qb{border-top:1px solid var(--line);padding:15px 0;}
  .qb:first-child{border-top:none;padding-top:4px;}
  .qb .qt{font-weight:600;font-size:.94rem;margin:0;}
  .qb .qh{font-size:.76rem;color:var(--mut);margin:.1rem 0 0;}
  .oq{border-top:1px solid var(--line);padding:16px 0;}
  .oq:first-child{border-top:none;}
  .oq label{display:block;font-weight:600;font-size:.94rem;margin-bottom:.15rem;}
  .oq .hint{font-size:.78rem;color:var(--mut);margin:0 0 .45rem;}
  textarea{
    width:100%;min-height:78px;border:1px solid var(--line);border-radius:5px;
    padding:11px 12px;font-family:inherit;font-size:.9rem;line-height:1.55;
    color:var(--ink);background:#fff;resize:vertical;
  }
  textarea:focus{outline:none;border-color:var(--clay);}
  .conf{
    background:var(--vine);color:#EAF1EC;border-radius:6px;padding:18px 20px;margin-bottom:18px;
  }
  .conf h3{color:#fff;margin-bottom:.3rem;}
  .conf p{margin:0 0 .5rem;font-size:.85rem;opacity:.94;}
  .conf p:last-child{margin:0;}
  .cbrow{display:flex;gap:10px;align-items:flex-start;padding:8px 0;font-size:.86rem;}
  .cbrow input{margin-top:5px;flex:0 0 auto;width:16px;height:16px;accent-color:var(--clay);}
  .brief{background:#fff;border:1px solid var(--clay);border-radius:6px;padding:22px;}
  .brief h4{font-family:'Fraunces',Georgia,serif;font-size:.95rem;margin:1rem 0 .3rem;color:var(--clay);}
  .brief h4:first-child{margin-top:0;}
  .brief p{font-size:.88rem;margin:0 0 .4rem;}
  .brief .said{font-style:italic;color:var(--ink);border-left:2px solid var(--line);padding-left:12px;}"""
assert css_anchor in s
s = s.replace(css_anchor, css_new, 1)

# ---------- 2. New sections before PRICING ----------
sec_anchor = "<!-- PRICING -->"
sections = """<!-- PROFILE (BUBBLES) -->
<section class="sec hide" id="profileSec">
  <div class="wrap">
    <p class="eyebrow">Step Four \u00b7 About Three Minutes</p>
    <h2>Now let's make it yours</h2>
    <p class="mut small" style="max-width:40em;">Tap whatever is most true. There are no wrong answers and nothing here is a test \u2014 these choices decide how your daily readings get written: their length, their voice, how much Scripture they carry, and what you are actually asked to make.</p>
    <div class="card" id="bubQs"></div>
    <button class="btn" id="toStory">Continue \u2014 in your own words</button>
  </div>
</section>

<!-- OPEN-ENDED -->
<section class="sec hide" id="storySec">
  <div class="wrap">
    <p class="eyebrow">Step Five \u00b7 Optional, and the Part That Matters Most</p>
    <h2>In your own words</h2>

    <div class="conf">
      <h3>This is confidential.</h3>
      <p>What you write here is private. It is not published, not shown to other members, not used in marketing, not sold or shared with anyone, and never treated as sales intelligence. Kim and John read it only to prepare well for you \u2014 and only if you tick the first box below.</p>
      <p>Nothing is visible to another person unless you choose to share it or give someone access. You can ask for it to be deleted at any time and it will be, without a conversation about why.</p>
      <p>One honest limit: Kim is an artist and John is a pastor. Neither is a licensed counselor. If something you write suggests you are carrying more than a creative practice is built to hold, John may gently point you toward someone qualified. That is care, not rejection.</p>
    </div>

    <p class="mut small" style="max-width:40em;">Answer as many or as few as you like. One sentence is plenty. Half of these get skipped by most people, and the ones you do answer are what make a devotional feel written for you rather than at you.</p>
    <div class="card" id="openQs"></div>

    <div class="card">
      <h3>Before you send it</h3>
      <div class="cbrow"><input type="checkbox" id="c1"><label for="c1">Kim and John may read this in order to prepare my readings and any experience I book.</label></div>
      <div class="cbrow"><input type="checkbox" id="c2"><label for="c2">Do not share any part of this with anyone else, including in a group setting, without asking me first.</label></div>
      <div class="cbrow"><input type="checkbox" id="c3"><label for="c3">Delete my written answers once my current journey is finished.</label></div>
      <p class="tiny mut" style="margin:.6rem 0 0;">The second box is on by default in practice whether you tick it or not. It is here so you can see it in writing.</p>
    </div>

    <button class="btn" id="buildBrief">Show me my profile</button>
  </div>
</section>

<!-- BRIEF -->
<section class="sec hide" id="briefSec">
  <div class="wrap">
    <p class="eyebrow">Your Devotional Profile</p>
    <h2>What we'd write for you</h2>
    <p class="mut small">This is the brief a writer would work from. Nothing here goes anywhere until you say so.</p>
    <div id="briefBody"></div>
    <div style="margin-top:16px;display:flex;gap:10px;flex-wrap:wrap;">
      <button class="btn" onclick="window.print()">Print or save a copy</button>
      <button class="btn ghost" onclick="document.getElementById('storySec').scrollIntoView({behavior:'smooth'})">Go back and change something</button>
    </div>
  </div>
</section>

<!-- PRICING -->"""
assert sec_anchor in s
s = s.replace(sec_anchor, sections, 1)

# ---------- 3. JS additions ----------
js_anchor = "drawSegs(); drawTiers(); drawCal(); drawLadder();"
js_new = r"""
// ---------- Step Four: personalization bubbles ----------
var BUBS = [
 {q:'When everything is too much, what actually helps?', h:'Choose all that are true.', m:true,
  o:['Silence','Being outdoors','Scripture','One trusted friend','Making something with my hands','Music','Moving my body']},
 {q:'Where do you most reliably meet God?', h:'Or, if that language is not yours \u2014 where do you feel most awake?', m:true,
  o:['In words and reading','In images and beauty','In nature','In music','In serving someone','In silence','I am not sure anymore']},
 {q:'When will you honestly do this?', h:'Be realistic rather than aspirational.', m:false,
  o:['Early morning','Midday','Evening','Late at night','It changes \u2014 meet me where I am']},
 {q:'How long should a day take?', h:'', m:false,
  o:['Five minutes','Ten to fifteen','Twenty to thirty','As long as it takes']},
 {q:'What voice helps you most?', h:'', m:false,
  o:['Gentle and tender','Direct and clear','Story-driven','Rooted and teaching-heavy','Playful and light']},
 {q:'How much Scripture do you want?', h:'There is no wrong answer here and no judgment attached to any of them.', m:false,
  o:['One verse, held closely','A short passage','A full chapter to sit in','Very little \u2014 give me the principle underneath']},
 {q:'What are you drawn to make?', h:'Choose all that appeal.', m:true,
  o:['Color and abstraction','Landscape and place','Words and lettering','Symbols and icons','Faces and figures','No idea \u2014 surprise me']},
 {q:'How much have you painted before?', h:'', m:false,
  o:['Never','Not since school','I dabble','I have a regular practice','I do this professionally']},
 {q:'What do you have on hand?', h:'We will write around whatever you already own.', m:true,
  o:['Watercolor','Acrylic','Ink or pen','Pastels or charcoal','Paper and a pencil only','Nothing yet']},
 {q:'Where are you with God right now?', h:'Answer honestly. This changes how the readings are written, and every one of these answers is welcome here.', m:false,
  o:['Steady and close','Going through the motions','Distant, and honest about it','Hurt by church, still looking','Not sure what I believe \u2014 here for the beauty']},
 {q:'Who is doing this alongside you?', h:'', m:true,
  o:['Just me','A friend','My spouse','A small group','My family','Nobody yet, but I would like that']},
 {q:'Thirty days from now, what would make this worth it?', h:'Choose up to three.', m:true,
  o:['A finished piece I am proud of','A habit that stuck','Something finally named','Some peace','Feeling close to God again','Something to give away','A conversation I have been avoiding']}
];

var OPENQ = [
 {q:'What season are you in right now?', h:'In your own words \u2014 not the tidy version.'},
 {q:'Tell me about a moment you would call a turning point.', h:'It can be recent or forty years old. Good or hard.'},
 {q:'What are you carrying that you have not said out loud?', h:'You can write it here and never say it to anyone. That still counts.'},
 {q:'What breakthrough are you hoping for?', h:'The thing you would call an answer if it came.'},
 {q:'What has been the hardest part of this last year?', h:''},
 {q:'What would a finish line look like?', h:'If this went as well as it possibly could, what would be true when you got to the end?'},
 {q:'Is there a verse, a phrase, a song, or a place that keeps coming back to you?', h:'Even if you do not know why it keeps returning.'},
 {q:'Who are you doing this for, besides yourself?', h:''},
 {q:'What do you want to be able to say a year from now?', h:'Write the sentence you hope will be true.'},
 {q:'What have I not asked that matters?', h:'This is often the most useful box on the page.'}
];

var CLOSE = [
 'This season, the truest sentence about my life is\u2026',
 'What I most want to hear is\u2026',
 'If I made one thing this year that mattered, it would be\u2026'
];

var bAns = [];
for (var q=0;q<BUBS.length;q++){ bAns.push([]); }

function drawBubs(){
  var h = '';
  for (var i=0;i<BUBS.length;i++){
    var B = BUBS[i];
    h += '<div class="qb"><p class="qt">' + B.q + '</p>';
    if (B.h){ h += '<p class="qh">' + B.h + '</p>'; }
    h += '<div class="bubs">';
    for (var j=0;j<B.o.length;j++){
      var on = (bAns[i].indexOf(B.o[j]) > -1) ? ' on' : '';
      h += '<button class="bub' + on + '" onclick="tapBub(' + i + ',' + j + ')">' + B.o[j] + '</button>';
    }
    h += '</div></div>';
  }
  el('bubQs').innerHTML = h;
}

function tapBub(i, j){
  var v = BUBS[i].o[j];
  var at = bAns[i].indexOf(v);
  if (BUBS[i].m){
    if (at > -1){ bAns[i].splice(at,1); } else { bAns[i].push(v); }
  } else {
    bAns[i] = (at > -1) ? [] : [v];
  }
  drawBubs();
}

function drawOpen(){
  var h = '';
  for (var i=0;i<OPENQ.length;i++){
    h += '<div class="oq"><label for="o' + i + '">' + OPENQ[i].q + '</label>';
    if (OPENQ[i].h){ h += '<p class="hint">' + OPENQ[i].h + '</p>'; }
    h += '<textarea id="o' + i + '" placeholder="However much or little you want."></textarea></div>';
  }
  h += '<div class="oq"><label>Finish these three, if you can.</label>';
  h += '<p class="hint">Short is better than complete.</p>';
  for (var c=0;c<CLOSE.length;c++){
    h += '<p class="hint" style="margin:.5rem 0 .2rem;color:var(--ink);font-weight:500;">' + CLOSE[c] + '</p>';
    h += '<textarea id="cl' + c + '" style="min-height:52px;"></textarea>';
  }
  h += '</div>';
  el('openQs').innerHTML = h;
}

el('toStory').onclick = function(){
  el('storySec').classList.remove('hide');
  el('storySec').scrollIntoView({behavior:'smooth'});
};

el('buildBrief').onclick = function(){
  var h = '<div class="brief">';
  var A = AUD[seg];
  h += '<h4>Who this is for</h4><p>' + A.n + '</p>';

  var lbl = ['What helps under pressure','Where they come alive','When they will read',
    'Length','Voice','Scripture weight','Drawn to make','Experience','Supplies on hand',
    'Where they are with God','Doing this alongside','What would make it worth it'];
  h += '<h4>How to write for them</h4>';
  for (var i=0;i<BUBS.length;i++){
    var v = bAns[i].length ? bAns[i].join(', ') : '\u2014 not answered';
    h += '<p><strong>' + lbl[i] + ':</strong> ' + v + '</p>';
  }

  var any = false, sh = '';
  for (var k=0;k<OPENQ.length;k++){
    var t = el('o' + k).value.replace(/^\s+|\s+$/g,'');
    if (t){ any = true; sh += '<p><strong>' + OPENQ[k].q + '</strong></p><p class="said">' + t + '</p>'; }
  }
  for (var c=0;c<CLOSE.length;c++){
    var t2 = el('cl' + c).value.replace(/^\s+|\s+$/g,'');
    if (t2){ any = true; sh += '<p><strong>' + CLOSE[c] + '</strong></p><p class="said">' + t2 + '</p>'; }
  }
  h += '<h4>In their own words</h4>';
  h += any ? sh : '<p class="mut">Left blank \u2014 which is completely fine. The readings will still be shaped by everything above.</p>';

  var perms = [];
  if (el('c1').checked){ perms.push('Kim and John may read this to prepare'); }
  if (el('c2').checked){ perms.push('Not to be shared with anyone else without asking first'); }
  if (el('c3').checked){ perms.push('Delete written answers when this journey ends'); }
  h += '<h4>Permissions</h4>';
  h += perms.length ? '<p>' + perms.join('. ') + '.</p>'
    : '<p class="mut">No permissions granted \u2014 nothing here will be read by anyone until you say so.</p>';
  h += '<p class="tiny mut" style="margin-top:1rem;">Confidential. Held securely, never published, never used as sales intelligence, and deleted on request.</p>';
  h += '</div>';

  el('briefBody').innerHTML = h;
  el('briefSec').classList.remove('hide');
  el('briefSec').scrollIntoView({behavior:'smooth'});
};

drawSegs(); drawTiers(); drawCal(); drawLadder(); drawBubs(); drawOpen();"""
assert js_anchor in s
s = s.replace(js_anchor, js_new, 1)

# ---------- 4. reveal profile section after result ----------
res_anchor = "  el('resultSec').scrollIntoView({behavior:'smooth'});"
res_new = """  el('resultSec').scrollIntoView({behavior:'smooth'});
  el('profileSec').classList.remove('hide');"""
assert res_anchor in s
s = s.replace(res_anchor, res_new, 1)

open(p, "w").write(s)
print("patched, bytes:", len(s))
