from shell import write

HEAD = """
<style>
.rd{max-width:720px;margin:0 auto;padding:64px 30px 90px}
.rd-top{display:flex;justify-content:space-between;align-items:center;gap:16px;flex-wrap:wrap;margin-bottom:38px}
.rd-camp{display:flex;align-items:center;gap:13px}
.rd-camp .mini{width:44px;height:52px;border-radius:22px 22px 6px 6px;overflow:hidden;position:relative;flex-shrink:0}
.rd-camp .mini svg{position:absolute;inset:0;width:100%;height:100%}
.rd-camp b{font-family:var(--display);font-size:17px;font-weight:600;color:var(--ink);display:block;line-height:1.2}
.rd-camp span{font-size:11.5px;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:var(--mute)}
/* day arches */
.days{display:flex;gap:9px}
.dayarch{width:34px;height:44px;border-radius:17px 17px 5px 5px;border:1.5px solid var(--line);background:var(--paper);
  display:flex;align-items:center;justify-content:center;font-size:12.5px;font-weight:700;color:var(--mute);transition:all .3s var(--ease)}
.dayarch.cur{border-color:var(--green);background:var(--green-tint);color:var(--green-deep)}
.dayarch.done{background:var(--green);border-color:var(--green);color:#fff}
.dayarch.sun{border-style:dashed}
/* reading */
.greet{font-family:var(--display);font-size:clamp(34px,4.4vw,48px);font-weight:560;color:var(--ink);letter-spacing:-.01em;line-height:1.12}
.rd-date{font-size:12px;font-weight:700;letter-spacing:.16em;text-transform:uppercase;color:var(--mute);margin-bottom:14px}
.rd-body{font-size:17.5px;line-height:1.85;color:#3B4A41;margin-top:30px}
.rd-body p{margin-bottom:22px}
.rd-body .opener{font-family:var(--display);font-size:20px;font-style:italic;color:var(--ink)}
.verse{background:var(--paper);border:1px solid var(--line-soft);border-left:4px solid var(--green);border-radius:14px;
  padding:26px 30px;margin:34px 0}
.verse p{font-family:var(--display);font-style:italic;font-size:19.5px;line-height:1.6;color:var(--ink);margin:0}
.verse cite{display:block;font-style:normal;font-size:12px;font-weight:700;letter-spacing:.14em;text-transform:uppercase;color:var(--green-deep);margin-top:14px}
.rq{background:linear-gradient(150deg,#EDF4EA,#F8F3E3);border-radius:16px;padding:26px 30px;margin:30px 0}
.rq .lbl{margin-bottom:10px}
.rq p{font-size:16.5px;line-height:1.65;color:var(--ink);font-weight:550}
.pray{margin:30px 0}
.pray p{font-size:16.5px;line-height:1.8;color:#3B4A41;font-style:italic}
.sun-note{display:flex;gap:12px;align-items:flex-start;background:var(--gold-tint);border-radius:14px;padding:16px 20px;font-size:13.5px;color:#5E4A22;line-height:1.55;margin:30px 0}
.sun-note i{font-style:normal;font-size:16px}
.done-cta{margin-top:44px;text-align:center}
.done-msg{display:none;margin-top:26px;background:var(--paper);border:1px solid var(--line-soft);border-radius:18px;padding:30px;box-shadow:var(--shadow);animation:pop .5s var(--ease)}
.done-msg.show{display:block}
@keyframes pop{from{opacity:0;transform:translateY(10px)}to{opacity:1;transform:none}}
.done-msg b{font-family:var(--display);font-size:21px;font-weight:600;color:var(--ink);display:block;margin-bottom:8px}
.done-msg p{font-size:14.5px;color:var(--body);margin-bottom:20px}
.attr{margin-top:60px;padding-top:24px;border-top:1px solid var(--line-soft);font-size:11.5px;color:var(--mute);line-height:1.6}
@media(max-width:640px){.days{flex-wrap:wrap}.dayarch{width:30px;height:38px}}
</style>
"""

BODY = """
<div class="rd">
  <div class="rd-top">
    <div class="rd-camp">
      <span class="mini" id="miniCover"></span>
      <span><b id="campT">40 Days of Purpose</b><span id="campCh">Day One · The Invitation</span></span>
    </div>
    <div class="days" id="dayRow"></div>
  </div>

  <p class="rd-date" id="rdDate"></p>
  <h1 class="greet" id="greet">Good morning.</h1>

  <div class="rd-body">
    <p class="opener" id="opener"></p>
    <p id="p1"></p>
    <p id="p2"></p>
    <p id="p3"></p>
  </div>

  <div class="verse">
    <p id="vTxt"></p>
    <cite id="vRef"></cite>
  </div>

  <div class="rq">
    <label class="lbl">Today&rsquo;s reflection</label>
    <p id="rq"></p>
  </div>

  <div class="pray">
    <label class="lbl">A prayer to carry</label>
    <p id="pr"></p>
  </div>

  <div class="sun-note"><i>☀</i><span><b>About Day 7.</b> The seventh day of every Lifetogether week lands on Sunday — a shorter reading that prepares you for the weekend message, so your daily walk and your church&rsquo;s teaching arrive at the same table.</span></div>

  <div class="done-cta">
    <button class="btn btn-primary btn-lg" id="doneBtn" onclick="markDone()">Mark today complete ✓</button>
    <div class="done-msg" id="doneMsg">
      <b>Day One is done. That&rsquo;s how every movement starts.</b>
      <p>Tomorrow: <span id="tmr"></span> In the full campaign, the next 39 days are waiting — along with the group guide, the weekend messages, and a whole church walking with you.</p>
      <div style="display:flex;gap:12px;justify-content:center;flex-wrap:wrap">
        <a class="btn btn-primary" href="campaign.html">Explore the full campaign</a>
        <a class="btn btn-outline" href="pricing.html">See plans</a>
      </div>
    </div>
  </div>

  <p class="attr">Scripture quotation taken from The Holy Bible, New International Version® NIV®. Copyright © 1973, 1978, 1984, 2011 by Biblica, Inc.™ Used by permission. All rights reserved worldwide. · This is a preview day. Progress in this prototype is not saved.</p>
</div>
"""

SCRIPTS = r"""
<script>
const AREAS={
 purpose:{v:'Ephesians 2:10',
  vt:'For we are God\u2019s handiwork, created in Christ Jesus to do good works, which God prepared in advance for us to do.',
  rq:'If you believed \u2014 really believed \u2014 that this season\u2019s work was prepared in advance for you, what is one thing you would stop apologizing for, and one thing you would start?',
  pr:'Father, before I had a plan, You had a purpose. Today I trade the question \u201Cwhat am I doing with my life?\u201D for a better one: \u201Cwhat did You prepare for me to walk into today?\u201D Open my eyes to it. Amen.',
  tmr:'\u201CThe Assignment Underneath\u201D \u2014 why your role and your calling are not the same thing.'},
 rhythms:{v:'Psalm 46:10',
  vt:'He says, \u201CBe still, and know that I am God; I will be exalted among the nations, I will be exalted in the earth.\u201D',
  rq:'What is the loudest thing in your ordinary day \u2014 and what would ten unhurried minutes before it cost you? What might they give you?',
  pr:'Lord, I have practiced hurry for years; today I practice stillness for ten minutes. Meet me in the quiet I keep avoiding. Amen.',
  tmr:'\u201CThe Anchor Hour\u201D \u2014 finding the one fixed point a daily rhythm can hang on.'},
 community:{v:'Ecclesiastes 4:9',
  vt:'Two are better than one, because they have a good return for their labor.',
  rq:'Who was the last person you let see you \u2014 not the presentable version, the real one? What made that possible?',
  pr:'God, You have never once designed a life to be carried alone \u2014 including mine. Give me the courage today to be one degree more known than I was yesterday. Amen.',
  tmr:'\u201CThe Table Rule\u201D \u2014 why proximity comes before depth, and how to find your people.'},
 peace:{v:'Isaiah 26:3',
  vt:'You will keep in perfect peace those whose minds are steadfast, because they trust in you.',
  rq:'When the anxious thought arrives today \u2014 and it will \u2014 what is one true sentence you can set next to it?',
  pr:'Father, I am not asking You to remove every storm today. I am asking You to keep my mind while I walk through it. Steady what races. Quiet what shouts. Amen.',
  tmr:'\u201CNaming the Weather\u201D \u2014 the ancient practice of telling God exactly how it is.'},
 stewardship:{v:'Psalm 24:1',
  vt:'The earth is the LORD\u2019s, and everything in it, the world, and all who live in it.',
  rq:'If everything you manage \u2014 the account, the calendar, the house, the influence \u2014 already belongs to God, what changes about the decision you\u2019ve been putting off?',
  pr:'Lord, everything I called mine this morning was Yours before I woke. Make me a faithful manager today \u2014 openhanded, unafraid, and free. Amen.',
  tmr:'\u201CThe Owner\u2019s Meeting\u201D \u2014 the one question that reorders every financial decision.'},
 family:{v:'Joshua 24:15',
  vt:'But as for me and my household, we will serve the LORD.',
  rq:'What is one thing you want the people who come after you to know \u2014 and when did you last say it out loud to them?',
  pr:'God, let my home be the first place my faith is real, not the last. Give me one honest moment at our table today \u2014 and the presence of mind not to waste it. Amen.',
  tmr:'\u201CThe Story They\u2019re Hearing\u201D \u2014 what the next generation is actually learning from your house.'}
};

document.addEventListener('DOMContentLoaded',()=>{
  const q=new URLSearchParams(location.search);
  const areaK=q.get('a')||'purpose';
  const A=AREAS[areaK]||AREAS.purpose;
  const camp=FLAG[q.get('c')]||FLAG[({purpose:'purpose',rhythms:'prayer',community:'life-together',peace:'living-light',stewardship:'god-owns-it-all',family:'a-life-worth'})[areaK]]||FLAG['purpose'];
  const nm=(q.get('n')||'').trim();
  const fmt=q.get('f')||'40';

  // header
  document.getElementById('miniCover').innerHTML=coverSVG(camp);
  document.getElementById('campT').textContent=camp.t;
  document.getElementById('campCh').textContent=`Day One \u00b7 The Invitation \u00b7 ${fmt}-day path`;
  document.getElementById('rdDate').textContent=new Date().toLocaleDateString('en-US',{weekday:'long',month:'long',day:'numeric'});
  document.getElementById('greet').innerHTML=nm?`Good morning, ${nm}.`:'Good morning.';

  // day arches: 7 for the first week
  document.getElementById('dayRow').innerHTML=Array.from({length:7},(_,i)=>
    `<span class="dayarch ${i===0?'cur':''} ${i===6?'sun':''}" id="d${i}">${i+1}</span>`).join('');

  // reading — Invitation phase, campaign title woven in
  document.getElementById('opener').textContent=`Every long walk begins the same way: someone decides that today is Day One.`;
  document.getElementById('p1').innerHTML=`Welcome to <b>${camp.t}</b>. Not the idea of it \u2014 the actual first day, the one you\u2019re standing in right now. Over the next ${fmt} days this path asks for something small and almost embarrassing in its simplicity: about ten minutes, most mornings, in the same chair if you can manage it. A short reading. One honest question. A prayer you can carry out the door.`;
  document.getElementById('p2').innerHTML=`Here is what those minutes are for. Formation \u2014 the slow shaping of a life \u2014 almost never happens in the big moments. It happens in returns. The returning to the chair, the returning to the page, the returning to God with today\u2019s version of yourself, unedited. ${nm?nm+', y':'Y'}ou don\u2019t need to feel ready. Day One has never once required readiness; it only requires presence.`;
  document.getElementById('p3').innerHTML=`So before anything else \u2014 before the reflection below, before you decide whether you\u2019ll tell anyone you\u2019ve started \u2014 take one breath and let this be true: you are here. The rest of ${camp.t} will be built out of mornings exactly like this one.`;

  document.getElementById('vTxt').textContent='\u201C'+A.vt+'\u201D';
  document.getElementById('vRef').textContent=A.v+' (NIV)';
  document.getElementById('rq').textContent=A.rq;
  document.getElementById('pr').textContent=A.pr;
  document.getElementById('tmr').textContent=A.tmr;
});
function markDone(){
  document.getElementById('d0').classList.remove('cur');
  document.getElementById('d0').classList.add('done');
  document.getElementById('doneBtn').style.display='none';
  document.getElementById('doneMsg').classList.add('show');
}
</script>
"""

write("reader.html", "Day One — Lifetogether Daily Reader", BODY, active="", head=HEAD, scripts=SCRIPTS)
