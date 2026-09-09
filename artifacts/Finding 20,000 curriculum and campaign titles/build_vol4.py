# -*- coding: utf-8 -*-
import io
from vol4_data import CATS

def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

TOTAL = sum(sum(len(t[1]) for t in c[3]) for c in CATS)
NCAT = len(CATS)

BASE = """
:root{--navy:#101a33;--navy-2:#16213d;--navy-3:#1c2a4a;--gold:#b8934e;
--gold-lt:#d9bc82;--cream:#f7f3ea;--rule:rgba(184,147,78,.28)}
*{box-sizing:border-box}
body{margin:0;background:var(--navy);color:var(--cream);
font-family:'Cormorant Garamond',Georgia,serif;font-size:19px;line-height:1.65;
-webkit-text-size-adjust:100%}
.wrap{max-width:880px;margin:0 auto;padding:0 22px}
h1,h2,h3,h4{font-family:'Playfair Display',Georgia,serif;font-weight:600;line-height:1.15;margin:0}
.label{font-family:'Lato',system-ui,sans-serif;font-size:11px;letter-spacing:.22em;
text-transform:uppercase;color:var(--gold);font-weight:700}
.cover{padding:76px 0 58px;border-bottom:1px solid var(--rule);text-align:center}
.cover .label{display:block;margin-bottom:24px}
.cover h1{font-size:50px}
.cover h1 em{display:block;font-style:italic;font-size:26px;color:var(--gold-lt);
margin-top:12px;font-weight:400}
.cover .dek{font-size:20px;color:#e6dfd0;margin:24px auto 0;max-width:620px}
.brandline{font-family:'Lato',sans-serif;font-size:11px;letter-spacing:.18em;
text-transform:uppercase;color:#b9b0a0;margin-top:32px}
.stats{display:flex;flex-wrap:wrap;gap:1px;background:var(--rule);
border-top:1px solid var(--rule);border-bottom:1px solid var(--rule)}
.stat{flex:1 1 22%;min-width:118px;background:var(--navy);padding:24px 10px;text-align:center}
.stat b{display:block;font-family:'Playfair Display',serif;font-size:32px;
color:var(--gold-lt);font-weight:600}
.stat span{font-family:'Lato',sans-serif;font-size:10px;letter-spacing:.16em;
text-transform:uppercase;color:#b9b0a0}
.block{padding:54px 0;border-bottom:1px solid var(--rule)}
.block.alt{background:var(--navy-2)}
.block h2{font-size:32px;margin-bottom:6px}
.block h2 em{font-style:italic;color:var(--gold-lt)}
.block p{color:#e6dfd0;margin:16px 0 0}
.drop::first-letter{font-family:'Playfair Display',serif;float:left;font-size:62px;
line-height:.82;padding:6px 12px 0 0;color:var(--gold)}
.closing{padding:64px 0;text-align:center;background:var(--navy-2)}
.closing .q{font-family:'Playfair Display',serif;font-style:italic;font-size:26px;
color:var(--gold-lt);max-width:640px;margin:0 auto;line-height:1.4}
.closing .attr{font-family:'Lato',sans-serif;font-size:11px;letter-spacing:.2em;
text-transform:uppercase;color:#9d958a;margin-top:22px}
footer{padding:38px 0 58px;text-align:center;font-family:'Lato',sans-serif;
font-size:11px;letter-spacing:.14em;text-transform:uppercase;color:#8d8579}
@media(max-width:620px){
body{font-size:18px}
.cover{padding:52px 0 42px}.cover h1{font-size:33px}.cover h1 em{font-size:20px}
.block h2{font-size:27px}.stat b{font-size:27px}
}
"""

V4CSS = BASE + """
.idx{margin-top:26px;border-top:1px solid var(--rule)}
.idx a{display:flex;justify-content:space-between;gap:16px;align-items:baseline;
padding:14px 2px;border-bottom:1px solid rgba(184,147,78,.14);
color:var(--cream);text-decoration:none}
.idx .n{font-family:'Lato',sans-serif;font-size:11px;letter-spacing:.14em;
color:var(--gold);min-width:30px}
.idx .t{flex:1;font-size:20px}
.idx .c{font-family:'Lato',sans-serif;font-size:11px;color:#9d958a}
.cat{padding:52px 0 0;border-top:1px solid var(--rule)}
.cat .num{font-family:'Playfair Display',serif;font-size:15px;color:var(--gold);margin-bottom:6px}
.cat h3{font-size:31px}
.cat .sub{color:#c8c0b2;font-size:18px;margin-top:8px;max-width:680px;font-style:italic}
.hinge{margin-top:24px;border:1px solid var(--rule);background:var(--navy-2)}
.hinge .hd{font-family:'Lato',sans-serif;font-size:10px;letter-spacing:.2em;
text-transform:uppercase;color:var(--gold);padding:12px 20px;
border-bottom:1px solid var(--rule);font-weight:700}
.hrow{display:flex;gap:16px;padding:12px 20px;border-bottom:1px solid rgba(184,147,78,.12)}
.hrow:last-child{border-bottom:0}
.hrow .k{font-family:'Lato',sans-serif;font-size:10px;letter-spacing:.14em;
text-transform:uppercase;color:var(--gold-lt);min-width:126px;flex-shrink:0;padding-top:4px}
.hrow .v{flex:1;color:#e6dfd0;font-size:18px}
.track{margin-top:30px}
.track h4{font-size:21px;color:var(--gold-lt);font-style:italic}
.track .tc{font-family:'Lato',sans-serif;font-size:10px;letter-spacing:.16em;
text-transform:uppercase;color:#9d958a;margin-top:5px}
.entries{margin-top:14px;border-top:1px solid var(--rule)}
.entry{display:flex;gap:14px;padding:13px 2px;border-bottom:1px solid rgba(184,147,78,.13)}
.entry .i{font-family:'Lato',sans-serif;font-size:11px;color:var(--gold);min-width:24px;padding-top:6px}
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
@media(max-width:620px){
.cat h3{font-size:26px}.entry .ti{font-size:19px}.idx .t{font-size:18px}
.hrow{flex-direction:column;gap:4px}.hrow .k{min-width:0}
}
"""

JS = """
(function(){
  var box=document.getElementById('q'),hits=document.getElementById('hits');
  var e=document.querySelectorAll('.entry'),tr=document.querySelectorAll('.track'),
      cw=document.querySelectorAll('.cat-wrap');
  box.addEventListener('input',function(){
    var v=box.value.toLowerCase().trim(),n=0;
    for(var i=0;i<e.length;i++){
      var ok=(v===''||e[i].getAttribute('data-s').indexOf(v)!==-1);
      if(ok){e[i].classList.remove('hide');n++;}else{e[i].classList.add('hide');}
    }
    for(var j=0;j<tr.length;j++){
      tr[j].style.display=(tr[j].querySelectorAll('.entry:not(.hide)').length===0&&v!=='')?'none':'';}
    for(var k=0;k<cw.length;k++){
      cw[k].style.display=(cw[k].querySelectorAll('.entry:not(.hide)').length===0&&v!=='')?'none':'';}
    hits.textContent=(v==='')?(n+' titles'):(n+' of '+e.length+' titles');
  });
})();
"""

def head(title, css):
    return ('<!DOCTYPE html><html lang="en"><head><meta charset="utf-8">'
      '<meta name="viewport" content="width=device-width, initial-scale=1">'
      '<title>' + title + '</title>'
      '<link rel="preconnect" href="https://fonts.googleapis.com">'
      '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
      '<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,500;0,600;1,500'
      '&family=Cormorant+Garamond:ital,wght@0,400;0,600;1,400&family=Lato:wght@400;700&display=swap" rel="stylesheet">'
      '<style>' + css + '</style></head><body>')

# ============ VOLUME FOUR ============
o = [head('Catalytic Sundays &mdash; Volume Four | LifeTogether', V4CSS)]
o.append('<div class="wrap cover"><span class="label">Catalytic Sundays &middot; Volume Four</span>')
o.append('<h1>The Working Calendar<em>Fifteen Sundays a Church Actually Runs On</em></h1>')
o.append('<p class="dek">' + str(TOTAL) + ' standalone messages for communion, prayer, vision, serving, connection, ministry launches, and the asks in between.</p>')
o.append('<div class="brandline">LifeTogether &middot; 25 Years &middot; 500+ Churches &middot; 50M+ Campaigns</div></div>')

o.append('<div class="stats">')
for b, s in [(NCAT, "Categories"), (TOTAL, "Titles"), (50, "Ministry Launches"), (15, "Campaign Hinges")]:
    o.append('<div class="stat"><b>' + str(b) + '</b><span>' + s + '</span></div>')
o.append('</div>')

o.append('<div class="block"><div class="wrap"><span class="label">What This Volume Covers</span>')
o.append('<h2>The Sundays between <em>the holidays</em></h2>')
o.append('<p class="drop">Easter and Christmas take care of themselves in the sense that no pastor forgets them. The Sundays in this volume are the ones that quietly decide whether a church grows: the communion service that gets six rushed minutes, the vision message written on Saturday night, the ministry launch that dies because nobody knew what to sign up for. These are not lesser Sundays. They are the operating system.</p>')
o.append('<p>Every category carries its campaign hinge &mdash; what it rolls into, where the giving sits, where the gospel gets preached, and the one action taken before anyone leaves the building. The Ministry Launch category runs fifty deep, one message per ministry, because the Sunday that introduces a ministry determines whether it has leaders in eighteen months.</p>')
o.append('</div></div>')

o.append('<div class="block alt"><div class="wrap"><span class="label">Contents</span>')
o.append('<h2>Fifteen categories <em>at a glance</em></h2><div class="idx">')
for i, (name, blurb, hinge, tracks) in enumerate(CATS, 1):
    n = sum(len(t[1]) for t in tracks)
    o.append('<a href="#c' + str(i) + '"><span class="n">' + ('%02d' % i) + '</span><span class="t">' + esc(name) + '</span><span class="c">' + str(n) + '</span></a>')
o.append('</div></div></div>')

o.append('<div class="search"><div class="wrap">')
o.append('<input id="q" type="search" placeholder="Search all ' + str(TOTAL) + ' titles&hellip;" autocomplete="off">')
o.append('<div class="hits" id="hits">' + str(TOTAL) + ' titles</div></div></div>')

for i, (name, blurb, hinge, tracks) in enumerate(CATS, 1):
    o.append('<div class="cat-wrap" id="c' + str(i) + '"><div class="wrap cat">')
    o.append('<div class="num">' + ('%02d' % i) + '</div><h3>' + esc(name) + '</h3>')
    o.append('<p class="sub">' + esc(blurb) + '</p>')
    o.append('<div class="hinge"><div class="hd">The Campaign Hinge</div>')
    for k, key in [("Rolls into", "roll"), ("Giving moment", "give"),
                   ("Gospel moment", "gospel"), ("Call to action", "act")]:
        o.append('<div class="hrow"><div class="k">' + k + '</div><div class="v">' + esc(hinge[key]) + '</div></div>')
    o.append('</div>')
    for tname, items in tracks:
        o.append('<div class="track">')
        if tname:
            o.append('<h4>' + esc(tname) + '</h4>')
        o.append('<div class="tc" style="margin-top:' + ('5px' if tname else '24px') + '">' + str(len(items)) + ' titles</div>')
        o.append('<div class="entries">')
        for j, (t, s) in enumerate(items, 1):
            hay = (t + ' ' + s + ' ' + name + ' ' + (tname or '')).lower().replace('"', '')
            o.append('<div class="entry" data-s="' + esc(hay) + '"><div class="i">' + ('%02d' % j) + '</div>')
            o.append('<div><div class="ti">' + esc(t) + '</div><div class="st">' + esc(s) + '</div></div></div>')
        o.append('</div></div>')
    o.append('</div></div>')

o.append('<div class="closing"><div class="wrap"><p class="q">A church does not launch a program on Easter morning. It releases a movement, and then spends the rest of the year proving it meant it.</p>')
o.append('<div class="attr">Brett Eastman &middot; LifeTogether</div></div></div>')
o.append('<footer><div class="wrap">LifeTogether Ministries &middot; Catalytic Sundays &middot; Volume Four &middot; ' + str(NCAT) + ' Categories &middot; ' + str(TOTAL) + ' Titles</div></footer>')
o.append('<script>' + JS + '</script></body></html>')

html4 = "\n".join(o)
with io.open('/mnt/user-data/outputs/catalytic-sundays-vol-4.html', 'w', encoding='utf-8') as f:
    f.write(html4)
print("VOL4 categories:", NCAT, "titles:", TOTAL, "bytes:", len(html4))
