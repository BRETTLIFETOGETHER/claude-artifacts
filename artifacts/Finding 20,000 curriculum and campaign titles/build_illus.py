# -*- coding: utf-8 -*-
import io, json
from illus_data import THEMES, BOOKS, PASSAGES

NSETS = len(THEMES) + len(BOOKS) + len(PASSAGES)
NIDEAS = sum((len(e["o"]) + len(e["c"]) + len(e["h"]) + len(e["x"]))
             for e in THEMES + BOOKS + PASSAGES)
NPROMPT = sum(len(e["p"]) for e in THEMES + BOOKS + PASSAGES)

# ---- Devotional studio: 7 shootable scripts derived from the Resurrection kit ----
STUDIO = {
"title":"He's Not Where You Left Him",
"cat":"Resurrection Sunday",
"days":[
{"d":1,"t":"Spices in Your Hands","v":"Luke 24:1",
 "story":"Tell about a time you prepared carefully for an outcome that had already changed. Keep it under thirty seconds.",
 "teach":"They brought burial spices to a tomb that was already empty. Grief organizes. It makes arrangements, sets alarms, and shows up on time &mdash; all of it aimed at a version of the story God had already moved past.",
 "app":"You are probably carrying something you have quietly decided is finished.",
 "next":"Write down the one outcome you have accepted as settled. Do not solve it. Just name it.",
 "pray":"Father, show me where I have stopped expecting you to move. Amen."},
{"d":2,"t":"Very Early in the Morning","v":"Luke 24:1",
 "story":"Describe a season when you did the right thing without feeling anything at all.",
 "teach":"Luke tells us twice that it was dark. Nobody was watching. There was no crowd to perform for and no reason to go except love.",
 "app":"There is a kind of faithfulness that only happens early, and it rarely feels like faith while you are doing it.",
 "next":"Do one faithful thing today that nobody will see or thank you for.",
 "pray":"Lord, meet me in the part of this that nobody sees. Amen."},
{"d":3,"t":"The Stone Was Already Moved","v":"Luke 24:2",
 "story":"Tell about a problem you rehearsed the whole way there that turned out to be handled.",
 "teach":"They worried about the stone the entire walk. It was far too heavy for them and they knew it. They went anyway. And Scripture gives us no scene of the stone moving &mdash; God did it before they arrived and did not feel the need to let them watch.",
 "app":"Some of what you are dreading has already been dealt with. You will not know until you get there.",
 "next":"Make the call, send the message, or ask the question you have been avoiding.",
 "pray":"God, I am tired of carrying what you have already moved. Amen."},
{"d":4,"t":"They Did Not Find the Body","v":"Luke 24:3",
 "story":"Name something that is gone from your life that you did not recognize as grace at the time.",
 "teach":"The turning point of human history is described as an absence. Good news does not always arrive as an addition. Sometimes it arrives as a subtraction.",
 "app":"We are trained to look for God in what appears. It is worth learning to look for him in what disappears.",
 "next":"Name one thing you no longer carry that you carried five years ago. Thank God for the absence.",
 "pray":"Thank you for what you have taken away. Amen."},
{"d":5,"t":"Why Look Among the Dead?","v":"Luke 24:5",
 "story":"Describe a place you kept returning to hoping to feel something you used to feel there.",
 "teach":"The angels are not scolding these women. They are pointing out that the search is aimed at the wrong location.",
 "app":"Everyone has a tomb they revisit. An old version of yourself. A season when you felt closest to God, which you now visit the way people visit a grave.",
 "next":"Say out loud where you have been looking. Then ask God where he actually is.",
 "pray":"Jesus, I have been looking in the wrong place. Show me where you are. Amen."},
{"d":6,"t":"Remember How He Told You","v":"Luke 24:6-7",
 "story":"Share a promise from Scripture you have known for years and never actually leaned on.",
 "teach":"Jesus had told them. Plainly, more than once, before it happened. The resurrection was not new information on Sunday morning. It was old information nobody could hold.",
 "app":"The cure for standing in front of the wrong tomb is usually not new revelation. It is remembering what he already said.",
 "next":"Find that promise, write it out by hand, and put it where you will see it tomorrow.",
 "pray":"Lord, help me believe what you have already told me. Amen."},
{"d":7,"t":"Then They Remembered","v":"Luke 24:8-9",
 "story":"Tell about someone who told you something true that you did not receive well at first.",
 "teach":"Remembering gets its own sentence, and then Luke immediately says they went and told. They were not believed &mdash; the apostles thought it was nonsense &mdash; and they told it anyway.",
 "app":"Something is true, we remember it, and remembering moves us toward people. That is the whole shape of the Christian life.",
 "next":"Tell one person one true thing about what God has done. Today.",
 "pray":"Give me the words and the nerve. Amen."},
]}

DATA = {"themes":THEMES, "books":BOOKS, "passages":PASSAGES, "studio":STUDIO}

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
.cover{padding:62px 0 46px;text-align:center;border-bottom:1px solid var(--rule)}
.cover .label{display:block;margin-bottom:20px}
.cover h1{font-size:46px}
.cover h1 em{display:block;font-style:italic;font-size:24px;color:var(--gold-lt);
margin-top:10px;font-weight:400}
.cover .dek{font-size:19px;color:#e6dfd0;margin:20px auto 0;max-width:600px}
.stats{display:flex;flex-wrap:wrap;gap:1px;background:var(--rule);border-bottom:1px solid var(--rule)}
.stat{flex:1 1 22%;min-width:110px;background:var(--navy);padding:20px 8px;text-align:center}
.stat b{display:block;font-family:'Playfair Display',serif;font-size:30px;color:var(--gold-lt)}
.stat span{font-family:'Lato',sans-serif;font-size:10px;letter-spacing:.14em;
text-transform:uppercase;color:#b9b0a0}
.tabs{position:sticky;top:0;z-index:30;background:var(--navy-3);
border-bottom:1px solid var(--rule);overflow-x:auto;-webkit-overflow-scrolling:touch}
.tabs .inner{display:flex;max-width:860px;margin:0 auto;padding:0 12px}
.tab{flex:0 0 auto;background:none;border:0;color:#b9b0a0;
font-family:'Lato',sans-serif;font-size:11px;letter-spacing:.16em;text-transform:uppercase;
padding:17px 16px;cursor:pointer;border-bottom:2px solid transparent;white-space:nowrap;font-weight:700}
.tab.on{color:var(--gold-lt);border-bottom-color:var(--gold)}
#view{padding:34px 0 70px}
.lead{color:#e6dfd0;margin:0 0 22px;font-size:19px}
.grid{border-top:1px solid var(--rule)}
.item{display:flex;gap:14px;align-items:baseline;padding:16px 2px;
border-bottom:1px solid rgba(184,147,78,.14);cursor:pointer}
.item:hover .iname{color:var(--gold-lt)}
.item .inum{font-family:'Lato',sans-serif;font-size:11px;letter-spacing:.14em;
color:var(--gold);min-width:28px;flex-shrink:0}
.item .ibody{flex:1}
.item .iname{font-family:'Playfair Display',serif;font-size:22px;line-height:1.25}
.item .iframe{color:#a9a094;font-size:17px;margin-top:4px;line-height:1.45}
.item .arrow{color:var(--gold);font-size:20px;flex-shrink:0}
.back{background:none;border:1px solid var(--rule);color:var(--gold-lt);
font-family:'Lato',sans-serif;font-size:10px;letter-spacing:.18em;text-transform:uppercase;
padding:9px 16px;cursor:pointer;margin-bottom:24px;font-weight:700}
.dh h2{font-size:34px}
.dh .df{font-style:italic;color:#c8c0b2;font-size:19px;margin-top:8px}
.sec{margin-top:32px}
.sec .sh{font-family:'Lato',sans-serif;font-size:10px;letter-spacing:.22em;
text-transform:uppercase;color:var(--gold);border-bottom:1px solid var(--rule);
padding-bottom:9px;margin-bottom:8px;font-weight:700}
.idea{padding:14px 0;border-bottom:1px solid rgba(184,147,78,.12)}
.idea .it{font-family:'Playfair Display',serif;font-size:20px;color:var(--cream)}
.idea .id{color:#c3bbad;font-size:17px;margin-top:4px;line-height:1.5}
.xr{display:flex;gap:14px;padding:13px 0;border-bottom:1px solid rgba(184,147,78,.12)}
.xr .xk{font-family:'Lato',sans-serif;font-size:12px;letter-spacing:.06em;
color:var(--gold-lt);min-width:126px;flex-shrink:0;padding-top:3px}
.xr .xv{flex:1;color:#ded6c6;font-size:17px}
.own{margin-top:32px;border:2px solid var(--gold);background:var(--navy-2);padding:22px}
.own .oh{font-family:'Playfair Display',serif;font-size:24px;color:var(--gold-lt)}
.own .os{color:#c3bbad;font-size:17px;margin-top:6px}
.own ol{margin:16px 0 0;padding-left:20px;color:#e9e2d4}
.own li{margin-bottom:11px;font-size:18px}
.card{border:1px solid var(--rule);background:var(--navy-2);padding:22px;margin-top:22px}
.card h3{font-size:23px;color:var(--gold-lt)}
.card p{margin-top:10px;color:#ded6c6;font-size:18px}
.card ul,.card ol{margin:14px 0 0;padding-left:20px;color:#ded6c6}
.card li{margin-bottom:8px;font-size:18px}
.script{border-top:1px solid var(--rule);padding:24px 0}
.script .sd{font-family:'Lato',sans-serif;font-size:10px;letter-spacing:.2em;
text-transform:uppercase;color:var(--gold);margin-bottom:5px}
.script h4{font-size:23px}
.script .sv{font-family:'Lato',sans-serif;font-size:12px;color:var(--gold-lt);margin-top:4px}
.beat{display:flex;gap:14px;padding:10px 0;border-bottom:1px solid rgba(184,147,78,.1)}
.beat .bk{font-family:'Lato',sans-serif;font-size:10px;letter-spacing:.16em;
text-transform:uppercase;color:var(--gold);min-width:86px;flex-shrink:0;padding-top:4px}
.beat .bv{flex:1;color:#e6dfd0;font-size:18px}
footer{padding:34px 0 56px;text-align:center;font-family:'Lato',sans-serif;
font-size:11px;letter-spacing:.14em;text-transform:uppercase;color:#8d8579;
border-top:1px solid var(--rule)}
@media(max-width:620px){
body{font-size:18px}.cover h1{font-size:31px}.cover h1 em{font-size:19px}
.dh h2{font-size:27px}.item .iname{font-size:20px}.stat b{font-size:25px}
.xr{flex-direction:column;gap:3px}.xr .xk{min-width:0}
.beat{flex-direction:column;gap:3px}.beat .bk{min-width:0}
}
"""

JS = """
var D = window.__LIB__;
var state = {tab:'themes', item:null};

function esc(s){return String(s);}

function listView(key, lead){
  var arr = D[key], h = '<p class="lead">' + lead + '</p><div class="grid">';
  for (var i = 0; i < arr.length; i++){
    h += '<div class="item" data-k="' + key + '" data-i="' + i + '">';
    h += '<span class="inum">' + (i < 9 ? '0' : '') + (i + 1) + '</span>';
    h += '<span class="ibody"><span class="iname">' + arr[i].n + '</span>';
    h += '<span class="iframe">' + arr[i].f + '</span></span>';
    h += '<span class="arrow">&rsaquo;</span></div>';
  }
  return h + '</div>';
}

function ideaBlock(title, items){
  var h = '<div class="sec"><div class="sh">' + title + '</div>';
  for (var i = 0; i < items.length; i++){
    h += '<div class="idea"><div class="it">' + items[i][0] + '</div>';
    h += '<div class="id">' + items[i][1] + '</div></div>';
  }
  return h + '</div>';
}

function detailView(key, idx){
  var e = D[key][idx];
  var h = '<button class="back" id="bk">&larr; Back</button>';
  h += '<div class="dh"><h2>' + e.n + '</h2><p class="df">' + e.f + '</p></div>';
  h += '<div class="own"><div class="oh">Make it yours first</div>';
  h += '<div class="os">Answer these before you read a single idea below. The story that comes out of these questions will beat anything written for you, because it happened to you.</div><ol>';
  for (var i = 0; i < e.p.length; i++){ h += '<li>' + e.p[i] + '</li>'; }
  h += '</ol></div>';
  h += ideaBlock('Opening ideas', e.o);
  h += ideaBlock('Closing ideas', e.c);
  h += ideaBlock('Lighter ideas', e.h);
  h += '<div class="sec"><div class="sh">Cross-purpose Scripture</div>';
  for (var j = 0; j < e.x.length; j++){
    h += '<div class="xr"><div class="xk">' + e.x[j][0] + '</div><div class="xv">' + e.x[j][1] + '</div></div>';
  }
  return h + '</div>';
}

function studioView(){
  var s = D.studio;
  var h = '<p class="lead">Seven daily videos, shot in one sitting in under an hour, on the phone already in your pocket. The written seven-day devotional and this shooting script are the same asset in two formats &mdash; write once, ship twice.</p>';
  h += '<div class="card"><h3>The one-hour shoot</h3><ul>';
  h += '<li>One location, one camera position, phone horizontal on anything stable. Window light to your left or right, never behind you.</li>';
  h += '<li>Change your shirt between each day. Two minutes of wardrobe is what makes seven videos shot in an hour look like seven days.</li>';
  h += '<li>Ninety seconds each. If a take runs past two minutes, stop and restart rather than fixing it in the edit.</li>';
  h += '<li>Do not memorize. Know the six beats and talk. The stumbles are what make it feel like a person.</li>';
  h += '<li>Record all seven, then watch none of them until you are finished. Reviewing between takes is what turns an hour into four.</li>';
  h += '</ul></div>';
  h += '<div class="card"><h3>The six beats</h3><ol>';
  h += '<li><strong>Verse</strong> &mdash; read it, do not paraphrase it. Ten seconds.</li>';
  h += '<li><strong>Story</strong> &mdash; yours, thirty seconds, one scene only.</li>';
  h += '<li><strong>Teaching</strong> &mdash; what the passage actually says. Twenty-five seconds.</li>';
  h += '<li><strong>Application</strong> &mdash; the sentence that makes it theirs. Ten seconds.</li>';
  h += '<li><strong>Next step</strong> &mdash; something done today, not considered. Ten seconds.</li>';
  h += '<li><strong>Prayer</strong> &mdash; one or two sentences. Short enough to pray along with.</li>';
  h += '</ol></div>';
  h += '<div class="card"><h3>Worked example</h3><p>Seven scripts drawn from <em>' + s.title + '</em> &mdash; ' + s.cat + '. The story beat is left as a prompt on purpose. That is the one part nobody can write for you.</p></div>';
  for (var i = 0; i < s.days.length; i++){
    var d = s.days[i];
    h += '<div class="script"><div class="sd">Day ' + d.d + '</div><h4>' + d.t + '</h4>';
    h += '<div class="sv">' + d.v + ' (NIV)</div>';
    h += '<div class="beat"><div class="bk">Verse</div><div class="bv">Read ' + d.v + ' aloud.</div></div>';
    h += '<div class="beat"><div class="bk">Story</div><div class="bv">' + d.story + '</div></div>';
    h += '<div class="beat"><div class="bk">Teaching</div><div class="bv">' + d.teach + '</div></div>';
    h += '<div class="beat"><div class="bk">Application</div><div class="bv">' + d.app + '</div></div>';
    h += '<div class="beat"><div class="bk">Next step</div><div class="bv">' + d.next + '</div></div>';
    h += '<div class="beat"><div class="bk">Prayer</div><div class="bv">' + d.pray + '</div></div>';
    h += '</div>';
  }
  return h;
}

function buildView(){
  var h = '<p class="lead">Every illustration set in this library opens with the same four questions, because the goal was never to hand a pastor a story. It was to get his own out of him. A borrowed illustration is the fastest way for a congregation to sense that the person in front of them is preaching somebody else\\'s sermon.</p>';
  h += '<div class="card"><h3>The excavation method</h3><ol>';
  h += '<li><strong>Name the emotion, not the topic.</strong> Do not search your memory for a story about grace. Search it for a time you were relieved. The emotion is indexed; the doctrine is not.</li>';
  h += '<li><strong>Find the room.</strong> Where were you standing? What were you holding? Specificity is what makes a story land, and it is the first thing that gets lost in retelling.</li>';
  h += '<li><strong>Locate the turn.</strong> Every usable story has one moment where it changed. Find it and build the whole thing toward it.</li>';
  h += '<li><strong>Cut the ending you want.</strong> Most preachers over-resolve. If the real story did not end tidily, do not tidy it. The room can tell.</li>';
  h += '<li><strong>Get permission.</strong> If anyone else is in it, read it to them first. This is not a courtesy, it is a rule.</li>';
  h += '</ol></div>';
  h += '<div class="card"><h3>Four rules for using someone else\\'s illustration</h3><ol>';
  h += '<li>Attribute it. Out loud, in the moment. "I heard a story about..." costs you nothing and buys you everything.</li>';
  h += '<li>Never tell it in first person. Not once, not to make it flow better.</li>';
  h += '<li>Use it as a seed, not a script. Take the structure, replace the details with something you have actually seen.</li>';
  h += '<li>One per message. A sermon made of other people\\'s stories has no author.</li>';
  h += '</ol></div>';
  h += '<div class="card"><h3>Where to look when you have nothing</h3><ul>';
  h += '<li>Your own last seven days. The best illustration in most sermons happened on Tuesday.</li>';
  h += '<li>The counseling conversation you cannot use. Change everything, get permission, or write the emotion without the case.</li>';
  h += '<li>What your children said. Reliable, universal, and requires their permission by about age eight.</li>';
  h += '<li>The thing you were wrong about. Congregations trust a preacher who has publicly changed his mind.</li>';
  h += '<li>The Scripture itself. The cross-purpose passages in every set exist because the best illustration of a biblical idea is usually another biblical story.</li>';
  h += '</ul></div>';
  return h;
}

function render(){
  var v = document.getElementById('view');
  var h = '';
  if (state.item !== null){
    h = detailView(state.item[0], state.item[1]);
  } else if (state.tab === 'themes'){
    h = listView('themes', 'Twelve themes, each with opening, closing, and lighter ideas, four cross-purpose passages, and the questions that pull your own story out.');
  } else if (state.tab === 'books'){
    h = listView('books', 'Ten books of the Bible, each framed by what it is actually about before the ideas begin.');
  } else if (state.tab === 'passages'){
    h = listView('passages', 'Four passages preached so often they have gone invisible. Each one opened back up.');
  } else if (state.tab === 'studio'){
    h = studioView();
  } else {
    h = buildView();
  }
  v.innerHTML = '<div class="wrap">' + h + '</div>';
  window.scrollTo(0, 0);
  var items = v.querySelectorAll('.item');
  for (var i = 0; i < items.length; i++){
    items[i].onclick = function(){
      state.item = [this.getAttribute('data-k'), parseInt(this.getAttribute('data-i'), 10)];
      render();
    };
  }
  var bk = document.getElementById('bk');
  if (bk){ bk.onclick = function(){ state.item = null; render(); }; }
}

var tabs = document.querySelectorAll('.tab');
for (var t = 0; t < tabs.length; t++){
  tabs[t].onclick = function(){
    for (var k = 0; k < tabs.length; k++){ tabs[k].classList.remove('on'); }
    this.classList.add('on');
    state.tab = this.getAttribute('data-t');
    state.item = null;
    render();
  };
}
render();
"""

o = []
o.append('<!DOCTYPE html><html lang="en"><head><meta charset="utf-8">')
o.append('<meta name="viewport" content="width=device-width, initial-scale=1">')
o.append('<title>The Master Illustration Library | LifeTogether</title>')
o.append('<link rel="preconnect" href="https://fonts.googleapis.com">')
o.append('<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>')
o.append('<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,500;0,600;1,500&family=Cormorant+Garamond:ital,wght@0,400;0,600;1,400&family=Lato:wght@400;700&display=swap" rel="stylesheet">')
o.append('<style>' + CSS + '</style></head><body>')

o.append('<div class="wrap cover"><span class="label">LifeTogether &middot; Preaching Resources</span>')
o.append('<h1>The Master Illustration Library<em>Find one. Or better, find yours.</em></h1>')
o.append('<p class="dek">Opening, closing, and lighter ideas by theme, by book, and by passage &mdash; each set built to surface the pastor&rsquo;s own story before it offers anyone else&rsquo;s.</p></div>')

o.append('<div class="stats">')
for b, s in [(NSETS, "Illustration Sets"), (NIDEAS, "Ideas &amp; Cross-Refs"),
             (NPROMPT, "Excavation Prompts"), (7, "Video Scripts")]:
    o.append('<div class="stat"><b>' + str(b) + '</b><span>' + s + '</span></div>')
o.append('</div>')

o.append('<div class="tabs"><div class="inner">')
for key, lbl, on in [("themes", "By Theme", True), ("books", "By Book", False),
                     ("passages", "By Passage", False), ("studio", "Devotional Studio", False),
                     ("build", "Build Your Own", False)]:
    o.append('<button class="tab' + (' on' if on else '') + '" data-t="' + key + '">' + lbl + '</button>')
o.append('</div></div>')

o.append('<div id="view"></div>')
o.append('<footer><div class="wrap">LifeTogether Ministries &middot; The Master Illustration Library &middot; ' + str(NSETS) + ' Sets &middot; ' + str(NIDEAS) + ' Ideas</div></footer>')
o.append('<script>window.__LIB__ = ' + json.dumps(DATA) + ';</script>')
o.append('<script>' + JS + '</script>')
o.append('</body></html>')

html = "\n".join(o)
with io.open('/mnt/user-data/outputs/master-illustration-library.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("sets:", NSETS, "ideas+refs:", NIDEAS, "prompts:", NPROMPT, "bytes:", len(html))
