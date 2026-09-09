# -*- coding: utf-8 -*-
import io
from calendar_data import LOCKS, STRATEGIC

def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

LOCK_N = sum(sum(len(t[1]) for t in c[3]) for c in LOCKS)
STRAT_N = sum(len(c[3]) for c in STRATEGIC)
TOTAL = LOCK_N + STRAT_N
NCAT = len(LOCKS) + len(STRATEGIC)

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
.cover{padding:78px 0 60px;border-bottom:1px solid var(--rule);text-align:center}
.cover .label{display:block;margin-bottom:24px}
.cover h1{font-size:50px}
.cover h1 em{display:block;font-style:italic;font-size:27px;color:var(--gold-lt);
margin-top:12px;font-weight:400}
.cover .dek{font-size:20px;color:#e6dfd0;margin:24px auto 0;max-width:600px}
.brandline{font-family:'Lato',sans-serif;font-size:11px;letter-spacing:.18em;
text-transform:uppercase;color:#b9b0a0;margin-top:32px}
.stats{display:flex;flex-wrap:wrap;gap:1px;background:var(--rule);
border-top:1px solid var(--rule);border-bottom:1px solid var(--rule)}
.stat{flex:1 1 25%;min-width:130px;background:var(--navy);padding:24px 12px;text-align:center}
.stat b{display:block;font-family:'Playfair Display',serif;font-size:34px;
color:var(--gold-lt);font-weight:600}
.stat span{font-family:'Lato',sans-serif;font-size:10px;letter-spacing:.18em;
text-transform:uppercase;color:#b9b0a0}
.block{padding:56px 0;border-bottom:1px solid var(--rule)}
.block.alt{background:var(--navy-2)}
.block h2{font-size:32px;margin-bottom:6px}
.block h2 em{font-style:italic;color:var(--gold-lt)}
.block p{color:#e6dfd0;margin:16px 0 0}
.drop::first-letter{font-family:'Playfair Display',serif;float:left;font-size:62px;
line-height:.82;padding:6px 12px 0 0;color:var(--gold)}
.idx{margin-top:26px;border-top:1px solid var(--rule)}
.idx a{display:flex;justify-content:space-between;gap:16px;align-items:baseline;
padding:14px 2px;border-bottom:1px solid rgba(184,147,78,.14);
color:var(--cream);text-decoration:none}
.idx .n{font-family:'Lato',sans-serif;font-size:11px;letter-spacing:.14em;
color:var(--gold);min-width:30px}
.idx .t{flex:1;font-size:20px}
.idx .c{font-family:'Lato',sans-serif;font-size:11px;color:#9d958a}
.parthead{padding:64px 0 0}
.parthead .label{display:block;margin-bottom:12px}
.parthead h2{font-size:40px}
.parthead .rule{height:1px;background:var(--rule);margin-top:24px}
.cat{padding:50px 0 0}
.cat .num{font-family:'Playfair Display',serif;font-size:15px;color:var(--gold);
letter-spacing:.1em;margin-bottom:6px}
.cat h3{font-size:31px}
.cat .sub{color:#c8c0b2;font-size:18px;margin-top:8px;max-width:660px;font-style:italic}
.hinge{margin-top:26px;border:1px solid var(--rule);background:var(--navy-2)}
.hinge .hd{font-family:'Lato',sans-serif;font-size:10px;letter-spacing:.2em;
text-transform:uppercase;color:var(--gold);padding:12px 20px;
border-bottom:1px solid var(--rule);font-weight:700}
.hrow{display:flex;gap:16px;padding:13px 20px;border-bottom:1px solid rgba(184,147,78,.12)}
.hrow:last-child{border-bottom:0}
.hrow .k{font-family:'Lato',sans-serif;font-size:10px;letter-spacing:.14em;
text-transform:uppercase;color:var(--gold-lt);min-width:130px;flex-shrink:0;padding-top:4px}
.hrow .v{flex:1;color:#e6dfd0;font-size:18px}
.track{margin-top:34px}
.track h4{font-size:21px;color:var(--gold-lt);font-style:italic}
.track .tc{font-family:'Lato',sans-serif;font-size:10px;letter-spacing:.16em;
text-transform:uppercase;color:#9d958a;margin-top:5px}
.entries{margin-top:14px;border-top:1px solid var(--rule)}
.entry{display:flex;gap:14px;padding:13px 2px;border-bottom:1px solid rgba(184,147,78,.13)}
.entry .i{font-family:'Lato',sans-serif;font-size:11px;color:var(--gold);
min-width:24px;padding-top:6px}
.entry .ti{font-family:'Playfair Display',serif;font-size:20px;line-height:1.3}
.entry .st{font-size:17px;color:#c3bbad;margin-top:3px;line-height:1.45}
.entry.hide{display:none}
.search{position:sticky;top:0;z-index:20;background:var(--navy-3);
border-bottom:1px solid var(--rule);padding:12px 0}
.search input{width:100%;background:var(--navy);color:var(--cream);
border:1px solid var(--rule);border-radius:2px;padding:12px 14px;
font-family:'Cormorant Garamond',serif;font-size:18px}
.search input::placeholder{color:#8d8579}
.hits{font-family:'Lato',sans-serif;font-size:10px;letter-spacing:.16em;
text-transform:uppercase;color:#9d958a;margin-top:8px}
.closing{padding:66px 0;text-align:center;background:var(--navy-2)}
.closing .q{font-family:'Playfair Display',serif;font-style:italic;font-size:26px;
color:var(--gold-lt);max-width:640px;margin:0 auto;line-height:1.4}
.closing .attr{font-family:'Lato',sans-serif;font-size:11px;letter-spacing:.2em;
text-transform:uppercase;color:#9d958a;margin-top:22px}
footer{padding:38px 0 58px;text-align:center;font-family:'Lato',sans-serif;
font-size:11px;letter-spacing:.14em;text-transform:uppercase;color:#8d8579}
@media(max-width:620px){
body{font-size:18px}
.cover{padding:52px 0 42px}.cover h1{font-size:34px}.cover h1 em{font-size:21px}
.block h2,.parthead h2{font-size:28px}.cat h3{font-size:26px}
.entry .ti{font-size:19px}.stat b{font-size:28px}.idx .t{font-size:18px}
.hrow{flex-direction:column;gap:4px}.hrow .k{min-width:0}
}
"""

JS = """
(function(){
  var box=document.getElementById('q'), hits=document.getElementById('hits');
  var entries=document.querySelectorAll('.entry');
  var tracks=document.querySelectorAll('.track');
  var cats=document.querySelectorAll('.cat-wrap');
  box.addEventListener('input',function(){
    var v=box.value.toLowerCase().trim(), shown=0;
    for(var i=0;i<entries.length;i++){
      var ok=(v===''||entries[i].getAttribute('data-s').indexOf(v)!==-1);
      if(ok){entries[i].classList.remove('hide');shown++;}
      else{entries[i].classList.add('hide');}
    }
    for(var j=0;j<tracks.length;j++){
      var tv=tracks[j].querySelectorAll('.entry:not(.hide)').length;
      tracks[j].style.display=(tv===0&&v!=='')?'none':'';
    }
    for(var k=0;k<cats.length;k++){
      var cv=cats[k].querySelectorAll('.entry:not(.hide)').length;
      cats[k].style.display=(cv===0&&v!=='')?'none':'';
    }
    hits.textContent=(v==='')?(shown+' titles'):(shown+' of '+entries.length+' titles');
  });
})();
"""

def hinge_box(h):
    o = ['<div class="hinge"><div class="hd">The Campaign Hinge</div>']
    for k, key in [("Rolls into", "roll"), ("Giving moment", "give"),
                   ("Gospel moment", "gospel"), ("Call to action", "act")]:
        o.append('<div class="hrow"><div class="k">' + k + '</div><div class="v">' + esc(h[key]) + '</div></div>')
    o.append('</div>')
    return "\n".join(o)

def entries_block(items, ctx):
    o = ['<div class="entries">']
    for k, (t, s) in enumerate(items, 1):
        hay = (t + ' ' + s + ' ' + ctx).lower().replace('"', '')
        o.append('<div class="entry" data-s="' + esc(hay) + '"><div class="i">' + ('%02d' % k) + '</div>')
        o.append('<div><div class="ti">' + esc(t) + '</div><div class="st">' + esc(s) + '</div></div></div>')
    o.append('</div>')
    return "\n".join(o)

def lock_block(i, name, blurb, hinge, tracks):
    n = sum(len(t[1]) for t in tracks)
    o = ['<div class="cat-wrap" id="c' + str(i) + '"><div class="wrap cat">']
    o.append('<div class="num">' + ('%02d' % i) + '</div><h3>' + esc(name) + '</h3>')
    o.append('<p class="sub">' + esc(blurb) + '</p>')
    o.append(hinge_box(hinge))
    for tn, items in tracks:
        o.append('<div class="track"><h4>' + esc(tn) + '</h4>')
        o.append('<div class="tc">' + str(len(items)) + ' titles</div>')
        o.append(entries_block(items, name + ' ' + tn))
        o.append('</div>')
    o.append('</div></div>')
    return "\n".join(o)

def strat_block(i, name, blurb, hinge, items):
    o = ['<div class="cat-wrap" id="c' + str(i) + '"><div class="wrap cat">']
    o.append('<div class="num">' + ('%02d' % i) + '</div><h3>' + esc(name) + '</h3>')
    o.append('<p class="sub">' + esc(blurb) + '</p>')
    o.append(hinge_box(hinge))
    o.append('<div class="track"><div class="tc" style="margin-top:26px">' + str(len(items)) + ' titles</div>')
    o.append(entries_block(items, name))
    o.append('</div></div></div>')
    return "\n".join(o)

out = []
out.append('<!DOCTYPE html>')
out.append('<html lang="en"><head><meta charset="utf-8">')
out.append('<meta name="viewport" content="width=device-width, initial-scale=1">')
out.append('<title>Catalytic Sundays &mdash; The Calendar Locks &amp; Strategic Weekends | LifeTogether</title>')
out.append('<link rel="preconnect" href="https://fonts.googleapis.com">')
out.append('<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>')
out.append('<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,500;0,600;1,500&family=Cormorant+Garamond:ital,wght@0,400;0,600;1,400&family=Lato:wght@400;700&display=swap" rel="stylesheet">')
out.append('<style>' + CSS + '</style></head><body>')

out.append('<div class="wrap cover">')
out.append('<span class="label">Catalytic Sundays &middot; Volume Two</span>')
out.append('<h1>The Calendar Locks<em>and the Strategic Weekends</em></h1>')
out.append('<p class="dek">' + str(TOTAL) + ' standalone messages for the Sundays that anchor a church year &mdash; each one built to launch a season rather than fill a slot.</p>')
out.append('<div class="brandline">LifeTogether &middot; 25 Years &middot; 500+ Churches &middot; 50M+ Campaigns</div>')
out.append('</div>')

out.append('<div class="stats">')
for b, s in [(NCAT, "Categories"), (TOTAL, "Titles"), (LOCK_N, "Calendar Locks"), (STRAT_N, "Strategic")]:
    out.append('<div class="stat"><b>' + str(b) + '</b><span>' + s + '</span></div>')
out.append('</div>')

out.append('<div class="block"><div class="wrap">')
out.append('<span class="label">Why These Sundays</span>')
out.append('<h2>A Sunday is a <em>hinge</em>, not a slot</h2>')
out.append('<p class="drop">Most churches treat Mother&rsquo;s Day, Baptism Sunday, and the year-end offering as obligations on the calendar &mdash; things to get through rather than doors to walk through. That is an expensive habit. These are the weekends when people who never come are in the room, when the largest gifts of the year get decided, and when a first-time guest either connects or quietly disappears by March.</p>')
out.append('<p>Every category in this volume carries a campaign hinge: what the Sunday rolls into, where the giving moment sits, where the gospel gets preached, and the one specific action a person takes before they leave the building. A message without a hinge is a good morning. A message with one starts a season.</p>')
out.append('<p>Part One holds the three calendar locks &mdash; Mother&rsquo;s Day, Father&rsquo;s Day, and Graduation &mdash; at a hundred titles each, divided into five tracks of twenty so the depth stays honest rather than repetitive. Part Two holds five strategic weekends at twenty each. Together with the Easter and Christmas edition, the seasonal library now runs to 720 titles.</p>')
out.append('</div></div>')

out.append('<div class="block alt"><div class="wrap">')
out.append('<span class="label">Contents</span>')
out.append('<h2>Eight weekends <em>at a glance</em></h2><div class="idx">')
i = 0
for name, blurb, hinge, tracks in LOCKS:
    i += 1
    n = sum(len(t[1]) for t in tracks)
    out.append('<a href="#c' + str(i) + '"><span class="n">' + ('%02d' % i) + '</span><span class="t">' + esc(name) + '</span><span class="c">' + str(n) + '</span></a>')
for name, blurb, hinge, items in STRATEGIC:
    i += 1
    out.append('<a href="#c' + str(i) + '"><span class="n">' + ('%02d' % i) + '</span><span class="t">' + esc(name) + '</span><span class="c">' + str(len(items)) + '</span></a>')
out.append('</div></div></div>')

out.append('<div class="search"><div class="wrap">')
out.append('<input id="q" type="search" placeholder="Search all ' + str(TOTAL) + ' titles&hellip;" autocomplete="off">')
out.append('<div class="hits" id="hits">' + str(TOTAL) + ' titles</div></div></div>')

out.append('<div class="wrap parthead"><span class="label">Part One</span>')
out.append('<h2>The Calendar Locks</h2>')
out.append('<p style="color:#e6dfd0">Three weekends every church already puts on the calendar, at ' + str(LOCK_N) + ' titles across fifteen tracks.</p>')
out.append('<div class="rule"></div></div>')
i = 0
for name, blurb, hinge, tracks in LOCKS:
    i += 1
    out.append(lock_block(i, name, blurb, hinge, tracks))

out.append('<div class="wrap parthead"><span class="label">Part Two</span>')
out.append('<h2>The Strategic Weekends</h2>')
out.append('<p style="color:#e6dfd0">Five Sundays that carry disproportionate weight and are usually under-built. ' + str(STRAT_N) + ' titles, each category with its full campaign hinge.</p>')
out.append('<div class="rule"></div></div>')
for name, blurb, hinge, items in STRATEGIC:
    i += 1
    out.append(strat_block(i, name, blurb, hinge, items))

out.append('<div class="closing"><div class="wrap">')
out.append('<p class="q">A church does not launch a program on Easter morning. It releases a movement, and then spends the rest of the year proving it meant it.</p>')
out.append('<div class="attr">Brett Eastman &middot; LifeTogether</div></div></div>')
out.append('<footer><div class="wrap">LifeTogether Ministries &middot; Catalytic Sundays &middot; Volume Two &middot; ' + str(NCAT) + ' Weekends &middot; ' + str(TOTAL) + ' Titles</div></footer>')
out.append('<script>' + JS + '</script></body></html>')

html = "\n".join(out)
with io.open('/mnt/user-data/outputs/catalytic-sundays-calendar-strategic.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("categories:", NCAT, "locks:", LOCK_N, "strategic:", STRAT_N, "total:", TOTAL)
print("bytes:", len(html))
