# -*- coding: utf-8 -*-
"""Convert the rendered catalog's 400 static course rows into clickable
drop-downs with a summary, facts, status chip, and a button to a full view."""

import re, html
from summaries import FLAGSHIP, compose

SRC = "/mnt/user-data/outputs/smallgroupseminary-framework-and-catalog.html"
s = open(SRC, encoding="utf-8").read()

# --- split off the catalog region so we never touch the essay's <ol class="steps"> ---
split_at = s.index('<div class="cat-head">')
head, cat = s[:split_at], s[split_at:]

TIER_OF = {"Foundation &nbsp;&middot;&nbsp; entry level": "Foundation",
           "Core &nbsp;&middot;&nbsp; the working middle": "Core",
           "Advanced &nbsp;&middot;&nbsp; depth and practicum": "Advanced"}

state = {"disc": "", "tier": "Foundation", "i": 0}

def track_disc(m):
    state["disc"] = m.group(1)
    return m.group(0)

def track_tier(m):
    state["tier"] = TIER_OF[m.group(1)]
    state["i"] = 0
    return '<p class="tier">%s</p><div class="courses">' % m.group(1)

ROW = re.compile(r'<li><span class="code">([^<]+)</span><span class="t">(.*?)'
                 r'<span class="s">(.*?)</span></span></li>', re.S)

def row(m):
    code, title, sub = m.group(1), m.group(2), m.group(3)
    tier, disc = state["tier"], state["disc"]
    i = state["i"]; state["i"] += 1
    flagship = code in FLAGSHIP
    built = (code == "ST 101")
    summary = FLAGSHIP[code] if flagship else compose(disc, tier, sub, i)
    if built:
        chip, cls, btn = "Built", "built", "Open full syllabus"
    elif flagship:
        chip, cls, btn = "In production", "prod", "See the course frame"
    else:
        chip, cls, btn = "Planned", "plan", "See the course frame"
    pre = {"Foundation": "None", "Core": "Foundation row", "Advanced": "Core row"}[tier]
    return (
      '<div class="crow" data-open="false">'
      '<button class="chead" aria-expanded="false"><span class="code">%s</span>'
      '<span class="t">%s<span class="s">%s</span></span><span class="chev">+</span></button>'
      '<div class="cbody"><p class="csum">%s</p>'
      '<div class="cfacts"><span>12 sessions</span><span>90 minutes</span><span>%s tier</span>'
      '<span>Prerequisite: %s</span><span class="chip %s">%s</span></div>'
      '<button class="cbtn" data-code="%s" data-title="%s" data-sub="%s" data-disc="%s" '
      'data-status="%s">%s &nbsp;&rarr;</button></div></div>'
      % (code, title, sub, summary, tier, pre, cls, chip, code,
         html.escape(title, quote=True), html.escape(sub, quote=True),
         html.escape(disc.replace("&amp;", "and"), quote=True), chip, btn))

cat = re.sub(r'<div class="disc-top"><span class="disc-num">[^<]+</span><h3>(.*?)</h3>',
             track_disc, cat)
cat = re.sub(r'<p class="tier">(.*?)</p><ol class="courses">', track_tier, cat)
n_before = len(ROW.findall(cat))
cat = ROW.sub(row, cat)
cat = cat.replace('</ol></div></div>', '</div></div></div>')

CSS = """
.courses{margin:0;padding:0}
.crow{border-bottom:1px solid var(--rule)}
.chead{width:100%;display:flex;align-items:flex-start;gap:20px;background:none;border:none;
 text-align:left;padding:13px 0;cursor:pointer;font:inherit}
.chead:hover .t{color:var(--gold)}
.chead:focus-visible{outline:2px solid var(--gold);outline-offset:-2px}
.crow .code{flex:0 0 76px;font-family:"Lato",sans-serif;font-size:11px;font-weight:700;
 letter-spacing:.1em;color:var(--gold);padding-top:6px}
.crow .t{flex:1 1 auto;font-family:"Playfair Display",serif;font-size:18.5px;line-height:1.28;color:#1c2b3a}
.crow .s{display:block;font-family:"Cormorant Garamond",serif;font-style:italic;font-size:17.5px;
 color:var(--muted);margin-top:2px;letter-spacing:0}
.crow .chev{flex:0 0 20px;font-family:"Lato",sans-serif;color:var(--gold);font-size:16px;
 text-align:right;padding-top:4px}
.crow[data-open="true"] .chev{color:var(--body)}
.cbody{display:none;padding:2px 0 24px 96px}
.crow[data-open="true"] .cbody{display:block}
.csum{margin:0 0 16px;max-width:640px;font-size:18px}
.cfacts{display:flex;flex-wrap:wrap;align-items:center;margin-bottom:18px;row-gap:8px}
.cfacts span{font-family:"Lato",sans-serif;font-size:10px;letter-spacing:.13em;text-transform:uppercase;
 color:var(--muted);padding-right:15px;margin-right:15px;border-right:1px solid var(--rule)}
.cfacts span:last-child{border-right:none;padding-right:0;margin-right:0}
.chip{padding:4px 10px;font-weight:800}
.chip.built{background:var(--gold);color:#fff;border:none}
.chip.prod{border:1px solid var(--gold);color:var(--gold)}
.chip.plan{border:1px solid var(--rule);color:var(--muted)}
.cbtn{font-family:"Lato",sans-serif;font-weight:800;font-size:10px;letter-spacing:.18em;
 text-transform:uppercase;background:var(--ink);color:var(--gold-lt);border:none;padding:13px 22px;cursor:pointer}
.cbtn:hover{background:var(--gold);color:#fff}
.cbtn:focus-visible{outline:2px solid var(--gold);outline-offset:2px}
@media(max-width:620px){.chead{gap:10px}.crow .code{flex:0 0 62px}.cbody{padding-left:0}}
.mask{position:fixed;inset:0;background:rgba(10,20,32,.74);display:none;z-index:60;overflow-y:auto;padding:38px 16px}
.mask[data-on="true"]{display:block}
.modal{background:var(--parch);max-width:720px;margin:0 auto;padding:46px 46px 40px;position:relative}
.modal h3{font-size:clamp(25px,4vw,34px);line-height:1.1;margin-bottom:6px}
.modal .mcode{font-family:"Lato",sans-serif;font-weight:800;font-size:11px;letter-spacing:.24em;
 color:var(--gold);margin-bottom:12px}
.modal .msub{font-style:italic;color:var(--muted);font-size:19px;margin:0 0 20px}
.modal h5{font-family:"Lato",sans-serif;font-weight:800;font-size:10px;letter-spacing:.2em;
 text-transform:uppercase;color:var(--gold);border-bottom:1px solid var(--gold);padding-bottom:7px;margin:28px 0 12px}
.modal ol,.modal ul{margin:0;padding-left:20px}
.modal li{margin-bottom:7px}
.modal p{margin:0 0 14px}
.lrow{display:flex;gap:14px;padding:9px 0;border-bottom:1px solid var(--rule)}
.lrow b{flex:0 0 24px;font-family:"Lato",sans-serif;font-size:10px;color:var(--gold);padding-top:6px;font-weight:700}
.lrow span{flex:1;font-family:"Playfair Display",serif;font-size:17px;line-height:1.3}
.lrow i{display:block;font-family:"Cormorant Garamond",serif;font-size:16.5px;color:var(--muted);margin-top:1px}
.mclose{position:absolute;top:15px;right:18px;background:none;border:none;font-family:"Lato",sans-serif;
 font-size:11px;font-weight:800;letter-spacing:.16em;text-transform:uppercase;color:var(--muted);cursor:pointer}
.mclose:hover{color:var(--gold)}
@media(max-width:620px){.modal{padding:40px 22px 30px}}
@media print{.cbody{display:block!important}.chev,.cbtn,.mask{display:none!important}}
"""

JS = r"""
<div class="mask" id="mask" role="dialog" aria-modal="true" aria-labelledby="mtitle">
 <div class="modal"><button class="mclose" id="mclose">Close &times;</button>
 <div id="mbody"></div></div></div>
<script>
var ST101 = {
 desc:"Most Christians have absorbed a great deal of doctrine without ever being taught how doctrine actually works. They know what their church believes. They are far less sure where those beliefs came from, how they were tested, which of them are worth dividing over, and what any of it has to do with a Tuesday afternoon in a hospital corridor.<br><br>This course does not attempt to teach the doctrines. That is what the eleven courses after it are for. This one teaches a person how to hold one.",
 outcomes:["Explain in plain language what doctrine is, where it comes from, and what it is for.",
  "Trace a single teaching from biblical text through theological synthesis to confessional statement.",
  "Distinguish first, second, and third order convictions, and explain why that distinction keeps congregations together.",
  "Apply a repeatable four-step method for testing whether a doctrinal claim is sound.",
  "Describe how doctrine functions pastorally in suffering, in decision-making, in worship, and at a deathbed.",
  "Teach one doctrine clearly to another person and receive feedback on it."],
 texts:["The Apostles' Creed and the Nicene Creed, provided in the workbook",
  "One accessible survey of Christian belief, roughly 120 pages assigned",
  "Athanasius, On the Incarnation, for students on the depth track"],
 lessons:[["The Question Under the Question","Everyone already has a theology. The only question is whether it was chosen or absorbed."],
  ["Where Doctrine Comes From","A teaching is not invented. It is gathered, from many texts, over a long time."],
  ["Revelation","Christian doctrine is a response to a God who speaks first."],
  ["Scripture as the Rule","To be under a text is a specific and unusual thing to agree to."],
  ["The Rule of Faith","Before there was a creed, there was a summary the church handed down by mouth."],
  ["The Creeds","The words that held, and the century-long fight it took to find them."],
  ["Confessions and Catechisms","Why churches wrote it all down again, in their own words, for their own people."],
  ["First, Second, and Third Things","Theological triage is the skill that keeps congregations together."],
  ["Testing a Doctrine","A repeatable method, so you are not dependent on whoever spoke last."],
  ["Doctrine in the Pew","What any of this has to do with a hospital corridor."],
  ["When Doctrine Goes Wrong","Heresy, drift, and the pastoral cost of both."],
  ["Teaching What You Believe","You do not know a doctrine until you have handed it to somebody else."]]
};

function esc(t){return t;}

function fullST101(code,title,sub){
  var h = '<div class="mcode">'+code+' &nbsp;&middot;&nbsp; Full syllabus</div><h3 id="mtitle">'+title+'</h3>'+
    '<p class="msub">'+sub+'</p><p>'+ST101.desc+'</p>'+
    '<h5>Learning outcomes</h5><ol>';
  for(var i=0;i<ST101.outcomes.length;i++){h+='<li>'+ST101.outcomes[i]+'</li>';}
  h += '</ol><h5>Texts</h5><ul>';
  for(var j=0;j<ST101.texts.length;j++){h+='<li>'+ST101.texts[j]+'</li>';}
  h += '</ul><h5>The twelve lessons</h5>';
  for(var k=0;k<ST101.lessons.length;k++){
    var n = (k+1)<10 ? '0'+(k+1) : ''+(k+1);
    h += '<div class="lrow"><b>'+n+'</b><span>'+ST101.lessons[k][0]+'<i>'+ST101.lessons[k][1]+'</i></span></div>';
  }
  h += '<h5>Also built</h5><p>Full teaching script for Lesson One, participant workbook, facilitator guide, '+
       'and the four delivery editions. These live in the standalone ST 101 build file.</p>';
  return h;
}

function frame(code,title,sub,disc,status){
  return '<div class="mcode">'+code+' &nbsp;&middot;&nbsp; Course frame</div><h3 id="mtitle">'+title+'</h3>'+
   '<p class="msub">'+sub+'</p>'+
   '<p>A course in '+disc+'. The syllabus for this one has not been drafted yet, so what follows is '+
   'the standard frame every course in this program is built to. Nothing here is specific to this title.</p>'+
   '<h5>Status</h5><p><b>'+status+'.</b> '+
   (status === 'In production'
     ? 'Part of the twenty-course Year One row, one per discipline, which is the first block being written.'
     : 'In the catalog, not yet in the build queue. Churches can request it, and requests set the build order.')+
   '</p>'+
   '<h5>Every course ships with</h5><ul>'+
   '<li>Twelve sessions of ninety minutes, in the six-stage shape: open, three movements, discuss, close</li>'+
   '<li>Participant workbook with the exercises and reading plan</li>'+
   '<li>Facilitator guide and a full teaching script for every session</li>'+
   '<li>Four delivery editions from one build: self-study, small group, church class, church-branded</li>'+
   '<li>Reading of roughly 140 pages, with a heavier primary-source list for the depth track</li></ul>'+
   '<h5>Each session carries</h5><ul><li>A big idea stated in one sentence</li><li>A key text</li>'+
   '<li>Three teaching movements</li><li>Two discussion questions, never three</li>'+
   '<li>One exercise done outside the session</li></ul>'+
   '<p style="font-family:Lato,sans-serif;font-size:13px;color:var(--muted);border-top:1px solid var(--rule);'+
   'padding-top:14px;margin-top:26px">See ST 101 for a course built all the way out. It is the pattern '+
   'the other three hundred and ninety-nine are written against.</p>';
}

var mask = document.getElementById('mask'), mbody = document.getElementById('mbody'), lastFocus = null;
function closeModal(){ mask.setAttribute('data-on','false'); if(lastFocus) lastFocus.focus(); }
document.getElementById('mclose').addEventListener('click', closeModal);
mask.addEventListener('click', function(e){ if(e.target === mask) closeModal(); });
document.addEventListener('keydown', function(e){ if(e.key === 'Escape') closeModal(); });

document.addEventListener('click', function(e){
  var head = e.target.closest ? e.target.closest('.chead') : null;
  if(head){
    var r = head.parentNode, open = r.getAttribute('data-open') === 'true';
    r.setAttribute('data-open', open ? 'false' : 'true');
    head.setAttribute('aria-expanded', open ? 'false' : 'true');
    head.querySelector('.chev').textContent = open ? '+' : '\u2013';
    return;
  }
  var b = e.target.closest ? e.target.closest('.cbtn') : null;
  if(b){
    lastFocus = b;
    var c = b.getAttribute('data-code'), t = b.getAttribute('data-title'),
        u = b.getAttribute('data-sub'), d = b.getAttribute('data-disc'),
        st = b.getAttribute('data-status');
    mbody.innerHTML = (c === 'ST 101') ? fullST101(c,t,u) : frame(c,t,u,d,st);
    mask.setAttribute('data-on','true');
    mask.scrollTop = 0;
    document.getElementById('mclose').focus();
  }
});
</script>
"""

out = head + cat
out = out.replace("</style>", CSS + "\n</style>", 1)
out = out.replace("</body>", JS + "\n</body>", 1)

# refresh the catalog intro line to mention the interaction
out = out.replace(
 "Doubled to twenty courses per discipline, with ten disciplines added that were not on the\nprevious list. Numbered in registrar order so depth is visible at a glance.",
 "Doubled to twenty courses per discipline, with ten disciplines added that were not on the\nprevious list. Click any course to open its summary, then open the full syllabus.")

open(SRC, "w", encoding="utf-8").write(out)
print("rows converted:", n_before)
print("crow count:", out.count('<div class="crow"'))
print("flagship summaries used:", sum(1 for k in FLAGSHIP if 'data-code="%s"' % k in out))
print("bytes:", len(out))
