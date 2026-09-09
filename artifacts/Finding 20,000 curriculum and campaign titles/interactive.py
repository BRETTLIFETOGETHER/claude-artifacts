# -*- coding: utf-8 -*-

CSS = """
/* ---- global search ---- */
.gsearch{position:relative;margin-bottom:26px}
.gsearch input{width:100%;background:var(--navy-2);color:var(--cream);
border:1px solid var(--rule);border-radius:2px;padding:15px 16px;
font-family:'Cormorant Garamond',serif;font-size:19px}
.gsearch input::placeholder{color:#8d8579}
.gsearch input:focus{outline:none;border-color:var(--gold)}
.gmeta{font-family:'Lato',sans-serif;font-size:10px;letter-spacing:.16em;text-transform:uppercase;
color:#9d958a;margin-top:10px}
.gres{border-top:1px solid var(--rule);margin-top:14px}
.gres .gr{display:flex;gap:14px;align-items:baseline;padding:14px 2px;
border-bottom:1px solid rgba(184,147,78,.14);cursor:pointer;background:none;border-left:0;
border-right:0;border-top:0;width:100%;text-align:left;color:inherit;font-family:inherit}
.gres .gr:hover .grt{color:var(--gold-lt)}
.gres .gr:focus-visible{outline:2px solid var(--gold);outline-offset:-2px}
.gres .grc{font-family:'Lato',sans-serif;font-size:9px;letter-spacing:.14em;text-transform:uppercase;
color:var(--gold);min-width:150px;flex-shrink:0;padding-top:5px}
.gres .grb{flex:1}
.gres .grt{font-family:'Playfair Display',serif;font-size:20px;display:block}
.gres .grs{color:#a9a094;font-size:16px;margin-top:3px;display:block}
.gres .grf{font-family:'Lato',sans-serif;font-size:9px;letter-spacing:.14em;text-transform:uppercase;
color:var(--navy);background:var(--gold);padding:3px 8px;flex-shrink:0;font-weight:700}

/* ---- profile form ---- */
.pbar{position:sticky;top:0;z-index:20;background:var(--navy-3);border:1px solid var(--rule);
padding:16px 20px;margin-bottom:26px;display:flex;flex-wrap:wrap;gap:14px;align-items:center}
.pbar .ptrack{flex:1;min-width:160px;height:5px;background:var(--navy);border:1px solid var(--rule);
position:relative;overflow:hidden}
.pbar .pfill{position:absolute;left:0;top:0;bottom:0;background:var(--gold);width:0}
.pbar .pnum{font-family:'Lato',sans-serif;font-size:10px;letter-spacing:.16em;text-transform:uppercase;
color:var(--gold-lt);font-weight:700;flex-shrink:0}
.btn{background:var(--gold);color:var(--navy);border:0;font-family:'Lato',sans-serif;font-size:11px;
letter-spacing:.16em;text-transform:uppercase;padding:12px 20px;cursor:pointer;font-weight:700;
flex-shrink:0}
.btn:hover{background:var(--gold-lt)}
.btn:disabled{background:var(--navy-2);color:#6d675e;cursor:not-allowed;border:1px solid var(--rule)}
.btn:focus-visible{outline:2px solid var(--cream);outline-offset:2px}
.btn.ghost{background:none;color:var(--gold-lt);border:1px solid var(--gold)}
.btn.ghost:hover{background:var(--navy-3);color:var(--gold)}
.fld2{padding:16px 0;border-bottom:1px solid rgba(184,147,78,.14)}
.fld2 .flab{display:flex;gap:12px;align-items:baseline}
.fld2 .fnum{font-family:'Lato',sans-serif;font-size:11px;color:var(--gold);min-width:26px;flex-shrink:0}
.fld2 .ftit{font-family:'Playfair Display',serif;font-size:20px;flex:1}
.fld2 .fdone{font-family:'Lato',sans-serif;font-size:9px;letter-spacing:.14em;text-transform:uppercase;
color:var(--navy);background:var(--gold);padding:3px 8px;font-weight:700}
.fld2 .fhelp{color:#a9a094;font-size:16px;margin-top:5px;padding-left:38px;line-height:1.5}
.fld2 input[type=text],.fld2 input[type=url],.fld2 textarea{width:calc(100% - 38px);margin-left:38px;
margin-top:10px;background:var(--navy-2);color:var(--cream);border:1px solid var(--rule);
padding:11px 13px;font-family:'Cormorant Garamond',serif;font-size:17px;border-radius:2px}
.fld2 textarea{min-height:64px;resize:vertical}
.fld2 input:focus,.fld2 textarea:focus{outline:none;border-color:var(--gold)}
.chips{display:flex;flex-wrap:wrap;gap:7px;margin-top:11px;padding-left:38px}
.chip{background:var(--navy-3);border:1px solid rgba(184,147,78,.25);color:#ded6c6;
font-family:'Cormorant Garamond',serif;font-size:16px;padding:8px 14px;cursor:pointer;border-radius:2px}
.chip:hover{border-color:var(--gold)}
.chip.on{background:var(--gold);border-color:var(--gold);color:var(--navy);font-weight:600}
.chip:focus-visible{outline:2px solid var(--gold);outline-offset:2px}
.brief{background:var(--navy-3);border:1px solid var(--gold);padding:22px;margin-top:24px}
.brief h3{font-family:'Playfair Display',serif;font-size:24px;color:var(--gold-lt);margin-bottom:14px}
.brief pre{white-space:pre-wrap;font-family:'Courier New',monospace;font-size:14px;color:#ded6c6;
line-height:1.7;margin:0;max-height:420px;overflow-y:auto;background:var(--navy);
border:1px solid var(--rule);padding:18px}
.brief .brow{display:flex;gap:10px;flex-wrap:wrap;margin-top:16px}
.toast{position:fixed;left:50%;bottom:30px;transform:translateX(-50%);background:var(--gold);
color:var(--navy);font-family:'Lato',sans-serif;font-size:12px;letter-spacing:.12em;
text-transform:uppercase;padding:13px 24px;font-weight:700;z-index:200;box-shadow:0 4px 20px rgba(0,0,0,.4)}

/* ---- expandables ---- */
.exp2{border-bottom:1px solid rgba(184,147,78,.14)}
.exp2 .ehead{width:100%;background:none;border:0;color:inherit;font-family:inherit;text-align:left;
padding:15px 2px;cursor:pointer;display:flex;gap:14px;align-items:baseline}
.exp2 .ehead:hover .et2{color:var(--gold-lt)}
.exp2 .ehead:focus-visible{outline:2px solid var(--gold);outline-offset:-2px}
.exp2 .et2{font-family:'Playfair Display',serif;font-size:20px;flex:1}
.exp2 .esign{font-family:'Playfair Display',serif;font-size:22px;color:var(--gold);flex-shrink:0}
.exp2 .ebody{padding:4px 2px 18px 0;color:#ded6c6;font-size:17px;line-height:1.65}
.exp2 .ebody ul{margin:10px 0 0;padding-left:20px}
.exp2 .ebody li{margin-bottom:7px}

/* ---- builder ---- */
.bhero{border:2px solid var(--gold);background:var(--navy-2);padding:26px;margin-bottom:26px}
.bhero .bl2{font-family:'Lato',sans-serif;font-size:10px;letter-spacing:.2em;text-transform:uppercase;
color:var(--gold);font-weight:700}
.bhero h3{font-family:'Playfair Display',serif;font-size:30px;margin:10px 0 6px}
.bhero .bs2{font-style:italic;color:#c3bbad;font-size:19px}
.bspec{margin-top:20px;padding-top:16px;border-top:1px solid var(--rule)}
.bspec .brow2{display:flex;gap:14px;padding:9px 0}
.bspec .bk3{font-family:'Lato',sans-serif;font-size:10px;letter-spacing:.14em;text-transform:uppercase;
color:var(--gold-lt);min-width:150px;flex-shrink:0;padding-top:3px}
.bspec .bv3{flex:1;color:#e6dfd0;font-size:17px}
.kitgrp{margin-top:22px}
.kitgrp h4{font-family:'Lato',sans-serif;font-size:10px;letter-spacing:.2em;text-transform:uppercase;
color:var(--gold);font-weight:700;padding-bottom:9px;border-bottom:1px solid var(--rule)}
.kititem{display:flex;gap:12px;padding:11px 0;border-bottom:1px solid rgba(184,147,78,.1);align-items:center}
.kititem .kmark{width:16px;height:16px;border:1.5px solid var(--gold);flex-shrink:0;
display:flex;align-items:center;justify-content:center;color:var(--gold);font-size:11px}
.kititem .kmark.on{background:var(--gold);color:var(--navy)}
.kititem .kname{flex:1;color:#ded6c6;font-size:17px}
@media(max-width:620px){
.gres .grc{min-width:0;width:100%;padding-top:0;margin-bottom:3px}
.gres .gr{flex-wrap:wrap}
.fld2 input,.fld2 textarea,.chips{margin-left:0;width:100%;padding-left:0}
.fld2 .fhelp{padding-left:0}
.bspec .brow2{flex-direction:column;gap:3px}.bspec .bk3{min-width:0}
}
"""

JS = """
/* ============ state ============ */
var PROFILE = {bring:{}, know:{}, church:'', pastor:''};
var OPEN = {};
var IMIN = {count:0, joined:false};

function profileCount(){
  var n = 0, i;
  for (i = 0; i < D.custom2.bring.length; i++){
    var bid = D.custom2.bring[i][0];
    if (PROFILE.bring[bid] && PROFILE.bring[bid].length > 1){ n++; }
  }
  for (i = 0; i < D.custom2.know.length; i++){
    var kid = D.custom2.know[i][0];
    var v = PROFILE.know[kid];
    if (v && (typeof v === 'string' ? v.length : v.length > 0)){ n++; }
  }
  if (PROFILE.church){ n++; }
  return n;
}
function profileTotal(){ return D.custom2.bring.length + D.custom2.know.length + 1; }
function hasProfile(){ return profileCount() >= 3; }
function know(id){
  var v = PROFILE.know[id];
  if (!v){ return ''; }
  return (typeof v === 'string') ? v : v.join(', ');
}
function toast(msg){
  var old = document.querySelector('.toast');
  if (old){ old.parentNode.removeChild(old); }
  var t = document.createElement('div');
  t.className = 'toast';
  t.textContent = msg;
  document.body.appendChild(t);
  setTimeout(function(){ if (t.parentNode){ t.parentNode.removeChild(t); } }, 2200);
}

/* ============ global search ============ */
function searchAll(q){
  var out = [], i, j, k;
  q = q.toLowerCase().trim();
  if (q.length < 2){ return out; }
  for (i = 0; i < D.cats.length; i++){
    var c = D.cats[i];
    for (j = 0; j < c.t.length; j++){
      for (k = 0; k < c.t[j].i.length; k++){
        var m = c.t[j].i[k];
        var hay = (m[0] + ' ' + m[1] + ' ' + c.n).toLowerCase();
        if (hay.indexOf(q) !== -1){
          out.push({cat:i, track:j, idx:k, title:m[0], sub:m[1], cname:c.n, built:sermonFor(m[0])});
          if (out.length >= 60){ return out; }
        }
      }
    }
  }
  return out;
}
function searchHTML(){
  var h = '<div class="gsearch"><input id="gq" type="search" value="' + esc2(st.q || '') +
          '" placeholder="Search all 5,155 messages by title, subject or category&hellip;" autocomplete="off"></div>';
  if (st.q && st.q.length >= 2){
    var r = searchAll(st.q);
    h += '<div class="gmeta">' + (r.length >= 60 ? '60+' : r.length) + ' match' + (r.length === 1 ? '' : 'es') + '</div>';
    if (r.length){
      h += '<div class="gres">';
      for (var i = 0; i < r.length; i++){
        h += '<button class="gr" data-sc="' + r[i].cat + '" data-st2="' + r[i].track + '" data-si="' + r[i].idx + '">';
        h += '<span class="grc">' + r[i].cname + '</span>';
        h += '<span class="grb"><span class="grt">' + r[i].title + '</span>';
        h += '<span class="grs">' + r[i].sub + '</span></span>';
        if (r[i].built >= 0){ h += '<span class="grf">Built</span>'; }
        h += '</button>';
      }
      h += '</div>';
    } else {
      h += '<div class="card"><h3>Nothing matched that</h3><p>Try a shorter word, a Bible book, or a season &mdash; Easter, funeral, prayer, giving, doubt.</p></div>';
    }
    return h;
  }
  return h;
}
function esc2(s){ return String(s).replace(/&/g,'&amp;').replace(/"/g,'&quot;').replace(/</g,'&lt;'); }

/* ============ profile form ============ */
function customView(){
  var C = D.custom2, i;
  var n = profileCount(), tot = profileTotal();
  var pct = Math.round((n / tot) * 100);
  var h = '<div class="pbar"><span class="pnum">' + n + ' of ' + tot + ' complete</span>';
  h += '<span class="ptrack"><span class="pfill" style="width:' + pct + '%"></span></span>';
  h += '<button class="btn" id="seebrief"' + (n < 3 ? ' disabled' : '') + '>See your brief</button>';
  h += '<button class="btn ghost" id="clearprof">Clear</button></div>';
  h += '<div class="big">' + C.line + '</div>';
  h += '<p class="lead">' + C.why + '</p>';

  h += '<div class="sec"><div class="sh">First, the basics</div>';
  h += '<div class="fld2"><div class="flab"><span class="fnum">&mdash;</span><span class="ftit">Your church and your name</span>';
  if (PROFILE.church){ h += '<span class="fdone">Saved</span>'; }
  h += '</div>';
  h += '<input type="text" class="pf-basic" data-f="church" value="' + esc2(PROFILE.church) + '" placeholder="Church name">';
  h += '<input type="text" class="pf-basic" data-f="pastor" value="' + esc2(PROFILE.pastor) + '" placeholder="Your name">';
  h += '</div></div>';

  h += '<div class="sec"><div class="sh">' + C.bring_head + '<span class="shn">' + C.bring_note + '</span></div>';
  for (i = 0; i < C.bring.length; i++){
    var b = C.bring[i], bv = PROFILE.bring[b[0]] || '';
    h += '<div class="fld2"><div class="flab"><span class="fnum">' + (i < 9 ? '0' : '') + (i+1) + '</span>';
    h += '<span class="ftit">' + b[1] + '</span>';
    if (bv.length > 1){ h += '<span class="fdone">Saved</span>'; }
    h += '</div><div class="fhelp">' + b[2] + '</div>';
    if (b[3] === 'text' || b[3] === 'file'){
      h += '<textarea class="pf-bring" data-b="' + b[0] + '" placeholder="' + esc2(b[4]) + '">' + esc2(bv) + '</textarea>';
    } else {
      h += '<input type="url" class="pf-bring" data-b="' + b[0] + '" value="' + esc2(bv) + '" placeholder="' + esc2(b[4]) + '">';
    }
    h += '</div>';
  }
  h += '</div>';
  h += '<div class="warn"><b>The one that matters most</b><p>' + C.gap + '</p></div>';
  h += '<div class="sec"><div class="sh">What we promise about your material</div>';
  for (var pv = 0; pv < D.profile.privacy.length; pv++){
    h += '<div class="hrow" style="border-bottom:1px solid rgba(184,147,78,.13)"><div class="k">' + D.profile.privacy[pv][0] + '</div>';
    h += '<div class="v">' + D.profile.privacy[pv][1] + '</div></div>';
  }
  h += '</div>';

  h += '<div class="sec"><div class="sh">' + C.know_head + '<span class="shn">' + C.know_note + '</span></div>';
  for (i = 0; i < C.know.length; i++){
    var kq = C.know[i], cur = PROFILE.know[kq[0]];
    var filled = cur && (typeof cur === 'string' ? cur.length : cur.length > 0);
    h += '<div class="fld2"><div class="flab"><span class="fnum">' + (i < 9 ? '0' : '') + (i+1) + '</span>';
    h += '<span class="ftit">' + kq[1] + '</span>';
    if (filled){ h += '<span class="fdone">Set</span>'; }
    h += '</div><div class="chips">';
    for (var o = 0; o < kq[2].length; o++){
      var opt = kq[2][o], on = false;
      if (kq[3]){ on = cur && cur.indexOf(opt) !== -1; }
      else { on = (cur === opt); }
      h += '<button class="chip' + (on ? ' on' : '') + '" data-k="' + kq[0] + '" data-o="' + esc2(opt) + '" data-multi="' + (kq[3] ? '1' : '0') + '">' + opt + '</button>';
    }
    h += '</div></div>';
  }
  h += '</div><div class="card"><h3>Set once, not every week</h3><p>' + C.honesty + '</p></div>';
  if (st.brief){ h += briefHTML(); }
  return h;
}

function briefText(){
  var C = D.custom2, L = [], i;
  L.push('CHURCH PROFILE');
  L.push('==============');
  L.push('Church: ' + (PROFILE.church || '[not given]'));
  L.push('Pastor: ' + (PROFILE.pastor || '[not given]'));
  L.push('');
  L.push('WHAT WE HAVE');
  L.push('------------');
  for (i = 0; i < C.bring.length; i++){
    var b = C.bring[i], v = PROFILE.bring[b[0]];
    L.push((v && v.length > 1 ? '[x] ' : '[ ] ') + b[1] + (v && v.length > 1 ? ': ' + v : ''));
  }
  L.push('');
  L.push('HOW YOU PREACH');
  L.push('--------------');
  for (i = 0; i < C.know.length; i++){
    var k = C.know[i], kv = know(k[0]);
    L.push(k[1]);
    L.push('    ' + (kv || '[not answered]'));
  }
  L.push('');
  L.push('Completed ' + profileCount() + ' of ' + profileTotal() + '.');
  L.push('Generated by The Sermon Library.');
  return L.join('\\n');
}
function briefHTML(){
  var h = '<div class="brief" id="briefbox"><h3>Your brief</h3>';
  h += '<p style="color:#c3bbad;font-size:17px;margin-bottom:14px">This is what gets used to build every message for your church. Copy it, save it, or keep filling it in &mdash; every answer makes the next draft sound more like you.</p>';
  h += '<pre id="briefpre">' + esc2(briefText()) + '</pre>';
  h += '<div class="brow"><button class="btn" id="copybrief">Copy the brief</button>';
  h += '<button class="btn ghost" id="gobuild">Build a message with this</button></div></div>';
  return h;
}

/* ============ builder ============ */
function builderView(){
  var t = st.build;
  if (!t){ return '<div class="card"><h3>Pick a message first</h3><p>Open the library, choose a message, and press Make it yours.</p></div>'; }
  var h = '<div class="bhero"><div class="bl2">' + t.cname + (PROFILE.church ? ' &middot; for ' + esc2(PROFILE.church) : '') + '</div>';
  h += '<h3>' + t.title + '</h3><div class="bs2">' + t.sub + '</div>';
  h += '<div class="bspec">';
  var spec = [
    ['Church', PROFILE.church || 'Not set &mdash; add it in Custom'],
    ['Purpose of the Sunday', know('purpose') || 'Not set'],
    ['Where it leads', know('leads') || 'Standalone'],
    ['The room', know('room') || 'Not set'],
    ['Length', know('length') || 'Not set'],
    ['Voice', know('voice') || 'Not set'],
    ['Humor', know('humor') || 'Not set'],
    ['How personal', know('personal') || 'Not set'],
    ['Already fixed', know('fixed') || 'Nothing'],
    ['They leave doing', know('action') || 'Not set']
  ];
  for (var s = 0; s < spec.length; s++){
    h += '<div class="brow2"><div class="bk3">' + spec[s][0] + '</div><div class="bv3">' + spec[s][1] + '</div></div>';
  }
  h += '</div></div>';
  var n = profileCount();
  if (n < 3){
    h += '<div class="warn"><b>Your profile is nearly empty</b><p>This will still build, and it will sound generic. Three answers is enough to change the draft noticeably. Ten of your own sermons changes it completely.</p></div>';
    h += '<p><button class="btn" data-go="custom">Fill in your profile</button></p>';
  }
  h += '<div class="sec"><div class="sh">What gets built<span class="shn">Twenty-five pieces. Everything ticked is shaped by the profile above; everything unticked needs more from you.</span></div>';
  for (var g = 0; g < D.kit25.length; g++){
    h += '<div class="kitgrp"><h4>' + D.kit25[g][0] + '</h4>';
    for (var k = 0; k < D.kit25[g][1].length; k++){
      var on = n >= 3;
      if (D.kit25[g][1][k].indexOf('Illustration') !== -1){ on = (PROFILE.bring.sermons || '').length > 1; }
      if (D.kit25[g][1][k].indexOf('pastor emails') !== -1){ on = !!PROFILE.pastor; }
      h += '<div class="kititem"><span class="kmark' + (on ? ' on' : '') + '">' + (on ? '&#10003;' : '') + '</span>';
      h += '<span class="kname">' + D.kit25[g][1][k] + '</span></div>';
    }
    h += '</div>';
  }
  h += '</div>';
  h += '<div class="card"><h3>What happens next</h3><p>A build takes about a week. We work from the profile, send a first draft for you to cut and correct, and ship the finished set as files you own. Nothing is published anywhere and nothing is shared with another church.</p></div>';
  h += '<p style="margin-top:18px"><button class="btn" id="reqbuild">Request this build</button>';
  h += ' <button class="btn ghost" data-go="price">See what it costs</button></p>';
  return h;
}

/* ============ expandable extras ============ */
var EXTRAS = [
 ['Deeper Bible study','The exegetical layer for this passage &mdash; the historical setting, the key words worth slowing down on, where the grammar carries weight, and the two or three commentary arguments worth knowing before you preach it. Roughly 1,200 words, written to be read once rather than studied.'],
 ['More passages','Four cross-purpose texts that illustrate the same idea from a different angle, each with a line on what it adds that the primary passage does not. Use one as a second reading, or as the place the message turns.'],
 ['More illustrations','Three opening ideas, three closings and two lighter ones &mdash; and above them, the four excavation questions that pull your own story out. The prompts matter more than the ideas. A borrowed illustration is the fastest way for a room to sense the sermon is not yours.'],
 ['The whole week','Seven daily readings built from this message, each about 150 words with one reflection question and one concrete action. Ships as a printable journal, seven ninety-second video scripts, and seven emails with one field for you to fill in.'],
 ['Build it for my church','Everything above, shaped by your profile &mdash; your length, your voice, how personal you go, what is already fixed in the service, and what you want people doing before they leave.']
];
function extrasHTML(){
  var h = '<div class="sec"><div class="sh">Go further with this message</div>';
  for (var i = 0; i < EXTRAS.length; i++){
    var open = !!OPEN['x' + i];
    h += '<div class="exp2"><button class="ehead" data-x2="' + i + '">';
    h += '<span class="et2">' + EXTRAS[i][0] + '</span>';
    h += '<span class="esign">' + (open ? '&minus;' : '+') + '</span></button>';
    if (open){
      h += '<div class="ebody">' + EXTRAS[i][1];
      if (i === 4){ h += '<br><br><button class="btn" id="mkmine">Make it yours</button>'; }
      h += '</div>';
    }
    h += '</div>';
  }
  return h + '</div>';
}
"""
