# -*- coding: utf-8 -*-
import io, json

DATA = json.load(open('/home/claude/work/master_payload.json'))
NCAT = len(DATA["cats"])
NTIT = sum(sum(len(t["i"]) for t in c["t"]) for c in DATA["cats"])
NSERM = len(DATA["sermons"])

CSS = """
:root{--navy:#101a33;--navy-2:#16213d;--navy-3:#1c2a4a;--gold:#b8934e;
--gold-lt:#d9bc82;--cream:#f7f3ea;--rule:rgba(184,147,78,.28)}
*{box-sizing:border-box}
body{margin:0;background:var(--navy);color:var(--cream);
font-family:'Cormorant Garamond',Georgia,serif;font-size:19px;line-height:1.65;
-webkit-text-size-adjust:100%}
.wrap{max-width:860px;margin:0 auto;padding:0 22px}
h1,h2,h3,h4{font-family:'Playfair Display',Georgia,serif;font-weight:600;line-height:1.15;margin:0}
.label{font-family:'Lato',system-ui,sans-serif;font-size:11px;letter-spacing:.22em;
text-transform:uppercase;color:var(--gold);font-weight:700}
.cover{padding:54px 0 38px;text-align:center;border-bottom:1px solid var(--rule)}
.cover .label{display:block;margin-bottom:16px}
.cover h1{font-size:42px}
.cover h1 em{display:block;font-style:italic;font-size:22px;color:var(--gold-lt);margin-top:9px;font-weight:400}
.cover .dek{font-size:19px;color:#e6dfd0;margin:16px auto 0;max-width:580px}
.stats{display:flex;gap:1px;background:var(--rule);border-bottom:1px solid var(--rule)}
.stat{flex:1;min-width:0;background:var(--navy);padding:18px 6px;text-align:center}
.stat b{display:block;font-family:'Playfair Display',serif;font-size:27px;color:var(--gold-lt)}
.stat span{font-family:'Lato',sans-serif;font-size:9px;letter-spacing:.12em;
text-transform:uppercase;color:#b9b0a0}
.tabs{position:sticky;top:0;z-index:30;background:var(--navy-3);
border-bottom:1px solid var(--rule);overflow-x:auto;-webkit-overflow-scrolling:touch}
.tabs .inner{display:flex;max-width:860px;margin:0 auto;padding:0 12px}
.tab{flex:0 0 auto;background:none;border:0;color:#b9b0a0;font-family:'Lato',sans-serif;
font-size:11px;letter-spacing:.15em;text-transform:uppercase;padding:15px 14px;cursor:pointer;
border-bottom:2px solid transparent;white-space:nowrap;font-weight:700}
.tab.on{color:var(--gold-lt);border-bottom-color:var(--gold)}
.srch{padding:12px 0;border-bottom:1px solid var(--rule);background:var(--navy-2)}
.srch input{width:100%;background:var(--navy);color:var(--cream);border:1px solid var(--rule);
border-radius:2px;padding:11px 14px;font-family:'Cormorant Garamond',serif;font-size:18px}
.srch input::placeholder{color:#8d8579}
#view{padding:30px 0 70px}
.lead{color:#e6dfd0;margin:0 0 20px;font-size:19px}
.crumb{font-family:'Lato',sans-serif;font-size:10px;letter-spacing:.16em;text-transform:uppercase;
color:#8d8579;margin-bottom:14px}
.back{background:none;border:1px solid var(--rule);color:var(--gold-lt);font-family:'Lato',sans-serif;
font-size:10px;letter-spacing:.18em;text-transform:uppercase;padding:9px 16px;cursor:pointer;
margin-bottom:20px;font-weight:700}
.vol{font-family:'Lato',sans-serif;font-size:10px;letter-spacing:.2em;text-transform:uppercase;
color:var(--gold);padding:26px 0 8px;border-bottom:1px solid var(--rule);font-weight:700}
.item{display:flex;gap:13px;align-items:baseline;padding:15px 2px;
border-bottom:1px solid rgba(184,147,78,.14);cursor:pointer}
.item:hover .iname{color:var(--gold-lt)}
.item .inum{font-family:'Lato',sans-serif;font-size:11px;color:var(--gold);min-width:26px;flex-shrink:0}
.item .ibody{flex:1}
.item .iname{font-family:'Playfair Display',serif;font-size:21px;line-height:1.25}
.item .isub{color:#a9a094;font-size:17px;margin-top:3px;line-height:1.4}
.item .c{font-family:'Lato',sans-serif;font-size:11px;color:#9d958a;flex-shrink:0}
.item .arrow{color:var(--gold);font-size:19px;flex-shrink:0}
.item.hide{display:none}
.dh h2{font-size:33px}
.dh .df{font-style:italic;color:#c8c0b2;font-size:19px;margin-top:7px}
.intro{margin-top:18px;color:#e9e2d4;font-size:19px}
.xp{margin-top:20px;background:var(--navy-2);border-left:2px solid var(--gold);padding:16px 20px}
.xp b{font-family:'Lato',sans-serif;font-size:10px;letter-spacing:.18em;text-transform:uppercase;
color:var(--gold);display:block;margin-bottom:6px;font-weight:700}
.xp span{color:#ded6c6;font-size:18px}
.hinge{margin-top:18px;border:1px solid var(--rule)}
.hrow{display:flex;gap:14px;padding:11px 18px;border-bottom:1px solid rgba(184,147,78,.12)}
.hrow:last-child{border-bottom:0}
.hrow .k{font-family:'Lato',sans-serif;font-size:10px;letter-spacing:.14em;text-transform:uppercase;
color:var(--gold-lt);min-width:120px;flex-shrink:0;padding-top:3px}
.hrow .v{flex:1;color:#e6dfd0;font-size:17px}
.trk{font-family:'Playfair Display',serif;font-size:20px;color:var(--gold-lt);font-style:italic;
margin-top:26px;padding-bottom:6px;border-bottom:1px solid var(--rule)}
.meta{margin-top:18px;border-top:1px solid rgba(184,147,78,.18);
border-bottom:1px solid rgba(184,147,78,.18);padding:13px 0}
.row{display:flex;gap:13px;padding:6px 0;align-items:baseline}
.row .k{font-family:'Lato',sans-serif;font-size:10px;letter-spacing:.16em;text-transform:uppercase;
color:var(--gold);min-width:76px;flex-shrink:0}
.row .v{flex:1;color:#efe9dc}
.row .v.idea{font-family:'Playfair Display',serif;font-size:20px;color:var(--gold-lt);font-style:italic;line-height:1.35}
.sec{margin-top:28px}
.sec .sh{font-family:'Lato',sans-serif;font-size:10px;letter-spacing:.22em;text-transform:uppercase;
color:var(--gold);border-bottom:1px solid var(--rule);padding-bottom:9px;margin-bottom:6px;font-weight:700}
.sec .shn{font-family:'Cormorant Garamond',serif;font-size:17px;color:#9d958a;
text-transform:none;letter-spacing:0;font-weight:400;display:block;margin-top:6px;font-style:italic}
.mov{display:flex;gap:13px;padding:10px 0;border-bottom:1px solid rgba(184,147,78,.12)}
.mov .mn{font-family:'Playfair Display',serif;font-size:18px;color:var(--gold);min-width:22px;flex-shrink:0}
.mov .mt{flex:1;color:#e6dfd0;font-size:18px}
.day{display:flex;gap:13px;padding:11px 0;border-bottom:1px solid rgba(184,147,78,.12)}
.day .dn{font-family:'Lato',sans-serif;font-size:10px;letter-spacing:.14em;color:var(--gold);
min-width:50px;flex-shrink:0;padding-top:5px}
.day .dt{font-family:'Playfair Display',serif;font-size:19px}
.day .ds{color:#b6ac9d;font-size:17px;margin-top:2px;line-height:1.4}
.draft{margin-top:8px;background:var(--navy-2);border:1px solid var(--rule);padding:24px}
.draft p{margin:0 0 15px;color:#e9e2d4;font-size:18px;line-height:1.72}
.draft p:last-child{margin-bottom:0}
.draft p.slot{color:var(--gold);font-family:'Lato',sans-serif;font-size:11px;letter-spacing:.12em;
text-transform:uppercase;border-left:2px solid var(--gold);padding-left:14px;font-weight:700}
.ships{margin-top:30px;border:2px solid var(--gold);background:var(--navy-2)}
.ships .sht{font-family:'Playfair Display',serif;font-size:23px;color:var(--gold-lt);padding:20px 22px 5px}
.ships .shs{padding:0 22px 14px;color:#c3bbad;font-size:17px}
.ships .tier{border-top:1px solid var(--rule);padding:15px 22px}
.ships .tn{font-family:'Lato',sans-serif;font-size:10px;letter-spacing:.18em;text-transform:uppercase;
color:var(--gold);font-weight:700;margin-bottom:7px}
.ships ul{margin:0;padding-left:18px;color:#ded6c6}
.ships li{margin-bottom:6px;font-size:17px}
.card{border:1px solid var(--rule);background:var(--navy-2);padding:22px;margin-top:20px}
.card h3{font-size:22px;color:var(--gold-lt)}
.card p{margin-top:10px;color:#ded6c6;font-size:18px}
.step{padding:18px 0;border-bottom:1px solid rgba(184,147,78,.14)}
.step h4{font-size:21px;color:var(--gold-lt)}
.step p{margin-top:7px;color:#ded6c6;font-size:18px}
.mail{padding:16px 0;border-bottom:1px solid rgba(184,147,78,.13)}
.mail .mh{font-family:'Lato',sans-serif;font-size:10px;letter-spacing:.16em;text-transform:uppercase;
color:var(--gold);margin-bottom:5px}
.mail .ms{font-family:'Playfair Display',serif;font-size:19px}
.mail .mb{color:#ded6c6;font-size:17px;margin-top:6px;line-height:1.55}
footer{padding:32px 0 56px;text-align:center;font-family:'Lato',sans-serif;font-size:11px;
letter-spacing:.14em;text-transform:uppercase;color:#8d8579;border-top:1px solid var(--rule)}
@media(max-width:620px){
body{font-size:18px}.cover h1{font-size:29px}.cover h1 em{font-size:18px}
.dh h2{font-size:25px}.item .iname{font-size:20px}.stat b{font-size:22px}
.row{flex-direction:column;gap:2px}.row .k{min-width:0}
.hrow{flex-direction:column;gap:3px}.hrow .k{min-width:0}
.day{flex-direction:column;gap:2px}.day .dn{min-width:0}
.draft{padding:18px}
}
"""

JS = """
var D = window.__M__;
var st = {tab:'lib', cat:null, serm:null};

function sermonFor(name){
  for (var i = 0; i < D.sermons.length; i++){
    if (D.sermons[i].t === name){ return i; }
  }
  return -1;
}

function catList(){
  var h = '<p class="lead">Forty-eight categories. Tap one to read what it is for, how to make it memorable, and every message inside it.</p>';
  h += '<div class="srch"><input id="q" type="search" placeholder="Search categories&hellip;" autocomplete="off"></div>';
  var vol = '';
  for (var i = 0; i < D.cats.length; i++){
    var c = D.cats[i], n = 0;
    for (var t = 0; t < c.t.length; t++){ n += c.t[t].i.length; }
    if (c.v !== vol){ vol = c.v; h += '<div class="vol">' + vol + '</div>'; }
    h += '<div class="item cat" data-i="' + i + '" data-s="' + (c.n + ' ' + c.e).toLowerCase().replace(/"/g, '') + '">';
    h += '<span class="ibody"><span class="iname">' + c.n + '</span>';
    h += '<span class="isub">' + c.e + '</span></span>';
    h += '<span class="c">' + n + '</span><span class="arrow">&rsaquo;</span></div>';
  }
  return h;
}

function catDetail(i){
  var c = D.cats[i];
  var h = '<button class="back" id="bk">&larr; All categories</button>';
  h += '<div class="crumb">' + c.v + '</div>';
  h += '<div class="dh"><h2>' + c.n + '</h2></div>';
  h += '<p class="intro">' + c.e + '</p>';
  if (c.x){ h += '<div class="xp"><b>Make it an experience</b><span>' + c.x + '</span></div>'; }
  if (c.h){
    h += '<div class="hinge">';
    var keys = [['Rolls into','roll'],['Giving moment','give'],['Gospel moment','gospel'],['Call to action','act']];
    for (var k = 0; k < keys.length; k++){
      h += '<div class="hrow"><div class="k">' + keys[k][0] + '</div><div class="v">' + c.h[keys[k][1]] + '</div></div>';
    }
    h += '</div>';
  }
  for (var t = 0; t < c.t.length; t++){
    var tr = c.t[t];
    if (tr.n){ h += '<div class="trk">' + tr.n + '</div>'; }
    else { h += '<div class="sec"><div class="sh">' + tr.i.length + ' messages</div></div>'; }
    for (var j = 0; j < tr.i.length; j++){
      var si = sermonFor(tr.i[j][0]);
      h += '<div class="item' + (si >= 0 ? ' serm' : '') + '"' + (si >= 0 ? ' data-s2="' + si + '"' : '') + '>';
      h += '<span class="inum">' + (j < 9 ? '0' : '') + (j + 1) + '</span>';
      h += '<span class="ibody"><span class="iname">' + tr.i[j][0] + '</span>';
      h += '<span class="isub">' + tr.i[j][1] + '</span></span>';
      if (si >= 0){ h += '<span class="c">Built</span><span class="arrow">&rsaquo;</span>'; }
      h += '</div>';
    }
  }
  return h;
}

function shipsBlock(exp){
  var h = '<div class="ships"><div class="sht">If you download this message</div>';
  h += '<div class="shs">Twenty-five components in five tiers, plus the experiential ideas written for this message specifically.</div>';
  h += '<div class="tier"><div class="tn">The message</div><ul>';
  h += '<li>Full outline and the complete sermon draft above, as an editable document</li>';
  h += '<li>Landing lines written out: opening, transitions, and the last sentence</li>';
  h += '<li>Illustration slots, plus the excavation prompts that surface your own story</li>';
  h += '<li>Cross-purpose Scripture &mdash; four passages that illustrate the same idea</li>';
  h += '<li>Deeper study: exegetical notes and the commentary you did not have time for</li></ul></div>';
  h += '<div class="tier"><div class="tn">The experience &mdash; written for this message</div><ul>';
  for (var i = 0; i < exp.length; i++){ h += '<li>' + exp[i] + '</li>'; }
  h += '</ul></div>';
  h += '<div class="tier"><div class="tn">The service</div><ul>';
  h += '<li>Run sheet &mdash; minute by minute, with timings and handoffs</li>';
  h += '<li>PowerPoint and Keynote decks, title and lower-third graphics</li>';
  h += '<li>Cold open script, sixty seconds</li>';
  h += '<li>Worship set suggestions keyed to the big idea, in singable keys</li>';
  h += '<li>Prayer guide for the service and for the household</li></ul></div>';
  h += '<div class="tier"><div class="tn">The response</div><ul>';
  h += '<li>Bulletin insert, print-ready</li>';
  h += '<li>Commitment card, signed and collected in the room</li>';
  h += '<li>Invitation card and the three invite scripts</li>';
  h += '<li>Follow-up sequence: four texts or emails across the week</li>';
  h += '<li>What to count &mdash; the numbers that tell you it worked</li></ul></div>';
  h += '<div class="tier"><div class="tn">The week</div><ul>';
  h += '<li>Seven-day devotional, print and digital</li>';
  h += '<li>Seven iPhone video scripts and the seven pastor emails</li>';
  h += '<li>Printable participant journal, ready for a local printer</li>';
  h += '<li>Small group session with next steps for the person, family, and group</li>';
  h += '<li>Kids and student versions of the same big idea</li></ul></div>';
  return h + '</div>';
}

function sermDetail(i){
  var s = D.sermons[i];
  var h = '<button class="back" id="bk2">&larr; Back to ' + s.cat + '</button>';
  h += '<div class="crumb">' + s.cat + '</div>';
  h += '<div class="dh"><h2>' + s.t + '</h2><p class="df">' + s.s + '</p></div>';
  h += '<div class="meta"><div class="row"><div class="k">Text</div><div class="v">' + s.x + ' (NIV)</div></div>';
  h += '<div class="row"><div class="k">Big idea</div><div class="v idea">' + s.b + '</div></div></div>';
  h += '<div class="sec"><div class="sh">The outline</div>';
  for (var m = 0; m < s.m.length; m++){
    h += '<div class="mov"><div class="mn">' + (m + 1) + '</div><div class="mt">' + s.m[m] + '</div></div>';
  }
  h += '</div>';
  if (s.draft && s.draft.length){
    h += '<div class="sec"><div class="sh">The draft';
    h += '<span class="shn">The spine, written out. Roughly fifteen minutes as it stands. The bracketed slots are yours &mdash; drop your own stories in and it becomes a thirty-minute message in your voice.</span></div>';
    h += '<div class="draft">';
    for (var p = 0; p < s.draft.length; p++){
      var txt = s.draft[p];
      var isSlot = txt.charAt(0) === '[';
      h += '<p' + (isSlot ? ' class="slot"' : '') + '>' + txt + '</p>';
    }
    h += '</div></div>';
  }
  h += '<div class="sec"><div class="sh">Where the week goes &mdash; the seven daily devotions</div>';
  for (var d = 0; d < s.dev.length; d++){
    h += '<div class="day"><div class="dn">Day ' + (d + 1) + '</div><div>';
    h += '<div class="dt">' + s.dev[d][0] + '</div><div class="ds">' + s.dev[d][1] + '</div></div></div>';
  }
  h += '</div>';
  h += shipsBlock(s.exp);
  return h;
}

function studioView(){
  var h = '<p class="lead">Seven daily videos, shot in one sitting, delivered by email in the pastor\\'s own voice. The written devotional, the video scripts and these emails are one asset in three formats &mdash; written once, shipped three ways.</p>';
  h += '<div class="sec"><div class="sh">The five-step setup<span class="shn">Do steps one and two once. Steps three through five repeat every week and take ninety minutes.</span></div>';
  for (var i = 0; i < D.delivery.steps.length; i++){
    h += '<div class="step"><h4>' + D.delivery.steps[i][0] + '</h4><p>' + D.delivery.steps[i][1] + '</p></div>';
  }
  h += '</div>';
  h += '<div class="card"><h3>The six beats, ninety seconds each</h3><p><strong>Verse</strong> read, not paraphrased, ten seconds. <strong>Story</strong> &mdash; yours, one scene, thirty seconds. <strong>Teaching</strong>, twenty-five. <strong>Application</strong>, ten. <strong>Next step</strong> &mdash; something done today, ten. <strong>Prayer</strong>, one or two sentences, short enough to pray along with.</p></div>';
  h += '<div class="card"><h3>It has to come from him</h3><p>A devotional that arrives from the church sounds like a program. The same devotional arriving from a pastor with two sentences of his own on top sounds like a person who read it first and thought of you. That difference is worth more than production value, and it costs about four minutes a week.</p>';
  h += '<p>The system generates the email &mdash; sermon title, the day\\'s devotional, the video &mdash; and leaves one field blank. He writes two sentences. That is the entire ask, and it is the only part nobody can do for him.</p></div>';
  h += '<div class="sec"><div class="sh">Seven pastor emails, drafted<span class="shn">From the week built on <em>He\\'s Not Where You Left Him</em>. These are drafts in his voice to react to, not templates to send as written.</span></div>';
  for (var e = 0; e < D.delivery.emails.length; e++){
    var m = D.delivery.emails[e];
    h += '<div class="mail"><div class="mh">Day ' + m[0] + ' &middot; sends 6:00 a.m.</div>';
    h += '<div class="ms">Subject: ' + m[1] + '</div>';
    h += '<div class="mb">' + m[2] + '</div></div>';
  }
  return h + '</div>';
}

function render(){
  var v = document.getElementById('view'), h = '';
  if (st.tab === 'studio'){ h = studioView(); }
  else if (st.serm !== null){ h = sermDetail(st.serm); }
  else if (st.cat !== null){ h = catDetail(st.cat); }
  else { h = catList(); }
  v.innerHTML = '<div class="wrap">' + h + '</div>';
  window.scrollTo(0, 0);
  var cs = v.querySelectorAll('.item.cat');
  for (var i = 0; i < cs.length; i++){
    cs[i].onclick = function(){ st.cat = parseInt(this.getAttribute('data-i'), 10); st.serm = null; render(); };
  }
  var ss = v.querySelectorAll('.item.serm');
  for (var j = 0; j < ss.length; j++){
    ss[j].onclick = function(){ st.serm = parseInt(this.getAttribute('data-s2'), 10); render(); };
  }
  var b1 = document.getElementById('bk');
  if (b1){ b1.onclick = function(){ st.cat = null; render(); }; }
  var b2 = document.getElementById('bk2');
  if (b2){ b2.onclick = function(){ st.serm = null; render(); }; }
  var q = document.getElementById('q');
  if (q){
    q.oninput = function(){
      var val = q.value.toLowerCase().trim();
      var its = v.querySelectorAll('.item.cat');
      for (var k = 0; k < its.length; k++){
        var ok = (val === '' || its[k].getAttribute('data-s').indexOf(val) !== -1);
        if (ok){ its[k].classList.remove('hide'); } else { its[k].classList.add('hide'); }
      }
    };
  }
}

var tabs = document.querySelectorAll('.tab');
for (var t = 0; t < tabs.length; t++){
  tabs[t].onclick = function(){
    for (var k = 0; k < tabs.length; k++){ tabs[k].classList.remove('on'); }
    this.classList.add('on');
    st.tab = this.getAttribute('data-t');
    st.cat = null; st.serm = null;
    render();
  };
}
render();
"""

o = []
o.append('<!DOCTYPE html><html lang="en"><head><meta charset="utf-8">')
o.append('<meta name="viewport" content="width=device-width, initial-scale=1">')
o.append('<title>Catalytic Sundays &mdash; The Master File | LifeTogether</title>')
o.append('<link rel="preconnect" href="https://fonts.googleapis.com">')
o.append('<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>')
o.append('<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,500;0,600;1,500&family=Cormorant+Garamond:ital,wght@0,400;0,600;1,400&family=Lato:wght@400;700&display=swap" rel="stylesheet">')
o.append('<style>' + CSS + '</style></head><body>')
o.append('<div class="wrap cover"><span class="label">LifeTogether &middot; The Master File</span>')
o.append('<h1>Catalytic Sundays<em>Every category. Every message. All the way down.</em></h1>')
o.append('<p class="dek">Tap a category to see what it is for. Tap a message to see the outline, the draft, and what arrives when you download it.</p></div>')
o.append('<div class="stats">')
for b, s in [(NCAT, "Categories"), (NTIT, "Messages"), (NSERM, "Full Drafts"), (25, "Kit Parts")]:
    o.append('<div class="stat"><b>' + str(b) + '</b><span>' + s + '</span></div>')
o.append('</div>')
o.append('<div class="tabs"><div class="inner">')
o.append('<button class="tab on" data-t="lib">The Library</button>')
o.append('<button class="tab" data-t="studio">Devotional Studio</button>')
o.append('</div></div><div id="view"></div>')
o.append('<footer><div class="wrap">LifeTogether Ministries &middot; Catalytic Sundays &middot; The Master File &middot; ' + str(NCAT) + ' Categories &middot; ' + str(NTIT) + ' Messages</div></footer>')
o.append('<script>window.__M__ = ' + json.dumps(DATA) + ';</script>')
o.append('<script>' + JS + '</script></body></html>')

html = "\n".join(o)
with io.open('/mnt/user-data/outputs/catalytic-sundays-MASTER.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("categories:", NCAT, "messages:", NTIT, "drafts:", NSERM, "bytes:", len(html))
