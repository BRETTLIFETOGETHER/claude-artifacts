# -*- coding: utf-8 -*-
import io
from data import EASTER, CHRISTMAS

def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

E_TOTAL = sum(len(c[2]) for c in EASTER)
C_TOTAL = sum(len(c[2]) for c in CHRISTMAS)
TOTAL = E_TOTAL + C_TOTAL
NCAT = len(EASTER) + len(CHRISTMAS)

CSS = """
:root{
  --navy:#101a33; --navy-2:#16213d; --navy-3:#1c2a4a;
  --gold:#b8934e; --gold-lt:#d9bc82; --cream:#f7f3ea;
  --rule:rgba(184,147,78,.28);
}
*{box-sizing:border-box}
body{margin:0;background:var(--navy);color:var(--cream);
  font-family:'Cormorant Garamond',Georgia,serif;font-size:19px;line-height:1.65;
  -webkit-text-size-adjust:100%}
.wrap{max-width:860px;margin:0 auto;padding:0 22px}
h1,h2,h3,.disp{font-family:'Playfair Display',Georgia,serif;font-weight:600;line-height:1.15;margin:0}
.label{font-family:'Lato',system-ui,sans-serif;font-size:11px;letter-spacing:.22em;
  text-transform:uppercase;color:var(--gold);font-weight:700}

/* cover */
.cover{padding:78px 0 62px;border-bottom:1px solid var(--rule);text-align:center}
.cover .label{display:block;margin-bottom:26px}
.cover h1{font-size:52px;color:var(--cream)}
.cover h1 em{display:block;font-style:italic;font-size:30px;color:var(--gold-lt);margin-top:12px;font-weight:400}
.cover .dek{font-size:21px;color:#e6dfd0;margin:26px auto 0;max-width:600px}
.brandline{font-family:'Lato',system-ui,sans-serif;font-size:11px;letter-spacing:.18em;
  text-transform:uppercase;color:#b9b0a0;margin-top:34px}

/* stats */
.stats{display:flex;flex-wrap:wrap;gap:1px;background:var(--rule);
  border-top:1px solid var(--rule);border-bottom:1px solid var(--rule)}
.stat{flex:1 1 25%;min-width:130px;background:var(--navy);padding:26px 14px;text-align:center}
.stat b{display:block;font-family:'Playfair Display',serif;font-size:36px;color:var(--gold-lt);font-weight:600}
.stat span{font-family:'Lato',system-ui,sans-serif;font-size:10px;letter-spacing:.18em;
  text-transform:uppercase;color:#b9b0a0}

/* blocks */
.block{padding:60px 0;border-bottom:1px solid var(--rule)}
.block.alt{background:var(--navy-2)}
.block h2{font-size:34px;margin-bottom:8px}
.block h2 em{font-style:italic;color:var(--gold-lt)}
.block p{color:#e6dfd0;margin:16px 0 0}
.drop::first-letter{font-family:'Playfair Display',serif;float:left;font-size:64px;
  line-height:.82;padding:6px 12px 0 0;color:var(--gold)}
.note{border-left:2px solid var(--gold);padding:6px 0 6px 20px;margin-top:28px;color:#ded6c6}
.note .label{display:block;margin-bottom:6px}

/* index */
.idx{margin-top:30px;border-top:1px solid var(--rule)}
.idx a{display:flex;justify-content:space-between;gap:16px;align-items:baseline;
  padding:15px 2px;border-bottom:1px solid rgba(184,147,78,.14);
  color:var(--cream);text-decoration:none}
.idx a:hover{color:var(--gold-lt)}
.idx .n{font-family:'Lato',sans-serif;font-size:11px;letter-spacing:.14em;color:var(--gold);
  min-width:30px}
.idx .t{flex:1;font-size:20px}
.idx .c{font-family:'Lato',sans-serif;font-size:11px;letter-spacing:.12em;color:#9d958a}

/* part head */
.parthead{padding:66px 0 0}
.parthead .label{display:block;margin-bottom:14px}
.parthead h2{font-size:42px}
.parthead .rule{height:1px;background:var(--rule);margin-top:26px}

/* category */
.cat{padding:52px 0 8px}
.cat .num{font-family:'Playfair Display',serif;font-size:15px;color:var(--gold);
  letter-spacing:.1em;margin-bottom:6px}
.cat h3{font-size:29px}
.cat .sub{color:#c8c0b2;font-size:18px;margin-top:8px;max-width:640px;font-style:italic}
.cat .count{font-family:'Lato',sans-serif;font-size:10px;letter-spacing:.18em;
  text-transform:uppercase;color:#9d958a;margin-top:14px}

/* entries */
.entries{margin-top:22px;border-top:1px solid var(--rule)}
.entry{display:flex;gap:16px;padding:14px 2px;border-bottom:1px solid rgba(184,147,78,.13)}
.entry .i{font-family:'Lato',sans-serif;font-size:11px;color:var(--gold);min-width:26px;
  padding-top:6px;letter-spacing:.08em}
.entry .body{flex:1}
.entry .ti{font-family:'Playfair Display',serif;font-size:21px;color:var(--cream);line-height:1.3}
.entry .st{font-size:17px;color:#c3bbad;margin-top:3px;line-height:1.45}
.entry.hide{display:none}

/* search */
.search{position:sticky;top:0;z-index:20;background:var(--navy-3);
  border-bottom:1px solid var(--rule);padding:12px 0}
.search input{width:100%;background:var(--navy);color:var(--cream);
  border:1px solid var(--rule);border-radius:2px;padding:12px 14px;
  font-family:'Cormorant Garamond',serif;font-size:18px}
.search input::placeholder{color:#8d8579}
.search .hits{font-family:'Lato',sans-serif;font-size:10px;letter-spacing:.16em;
  text-transform:uppercase;color:#9d958a;margin-top:8px}

/* closing */
.closing{padding:70px 0;text-align:center;background:var(--navy-2)}
.closing .q{font-family:'Playfair Display',serif;font-style:italic;font-size:27px;
  color:var(--gold-lt);max-width:640px;margin:0 auto;line-height:1.4}
.closing .attr{font-family:'Lato',sans-serif;font-size:11px;letter-spacing:.2em;
  text-transform:uppercase;color:#9d958a;margin-top:24px}
footer{padding:40px 0 60px;text-align:center;font-family:'Lato',sans-serif;
  font-size:11px;letter-spacing:.14em;text-transform:uppercase;color:#8d8579}

@media(max-width:620px){
  body{font-size:18px}
  .cover{padding:54px 0 44px}
  .cover h1{font-size:36px}
  .cover h1 em{font-size:22px}
  .cover .dek{font-size:19px}
  .block h2,.parthead h2{font-size:29px}
  .cat h3{font-size:25px}
  .entry .ti{font-size:19px}
  .stat b{font-size:29px}
  .idx .t{font-size:18px}
}
"""

JS = """
(function(){
  var box = document.getElementById('q');
  var hits = document.getElementById('hits');
  var entries = document.querySelectorAll('.entry');
  var cats = document.querySelectorAll('.cat-wrap');
  box.addEventListener('input', function(){
    var v = box.value.toLowerCase().trim();
    var shown = 0;
    for (var i = 0; i < entries.length; i++){
      var hay = entries[i].getAttribute('data-s');
      var ok = (v === '' || hay.indexOf(v) !== -1);
      if (ok){ entries[i].classList.remove('hide'); shown++; }
      else { entries[i].classList.add('hide'); }
    }
    for (var j = 0; j < cats.length; j++){
      var vis = cats[j].querySelectorAll('.entry:not(.hide)').length;
      cats[j].style.display = (vis === 0 && v !== '') ? 'none' : '';
    }
    hits.textContent = (v === '') ? (shown + ' titles') : (shown + ' of ' + entries.length + ' titles');
  });
})();
"""

def cat_block(idx, name, blurb, items):
    o = []
    o.append('<div class="cat-wrap" id="c' + str(idx) + '">')
    o.append('<div class="wrap cat">')
    o.append('<div class="num">' + ('%02d' % idx) + '</div>')
    o.append('<h3>' + esc(name) + '</h3>')
    o.append('<p class="sub">' + esc(blurb) + '</p>')
    o.append('<div class="count">' + str(len(items)) + ' single-Sunday titles</div>')
    o.append('<div class="entries">')
    for k, (t, s) in enumerate(items, 1):
        hay = (t + ' ' + s + ' ' + name).lower().replace('"', '')
        o.append('<div class="entry" data-s="' + esc(hay) + '">')
        o.append('<div class="i">' + ('%02d' % k) + '</div>')
        o.append('<div class="body"><div class="ti">' + esc(t) + '</div>')
        o.append('<div class="st">' + esc(s) + '</div></div>')
        o.append('</div>')
    o.append('</div></div></div>')
    return "\n".join(o)

out = []
out.append('<!DOCTYPE html>')
out.append('<html lang="en"><head><meta charset="utf-8">')
out.append('<meta name="viewport" content="width=device-width, initial-scale=1">')
out.append('<title>Catalytic Sundays &mdash; Easter &amp; Christmas Edition | LifeTogether</title>')
out.append('<link rel="preconnect" href="https://fonts.googleapis.com">')
out.append('<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>')
out.append('<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,500;0,600;1,500&family=Cormorant+Garamond:ital,wght@0,400;0,600;1,400&family=Lato:wght@400;700&display=swap" rel="stylesheet">')
out.append('<style>' + CSS + '</style></head><body>')

# COVER
out.append('<div class="wrap cover">')
out.append('<span class="label">The Campaign Format System &middot; Single-Message Library</span>')
out.append('<h1>Catalytic Sundays<em>Easter &amp; Christmas Edition</em></h1>')
out.append('<p class="dek">' + str(TOTAL) + ' standalone messages for the two Sundays that carry the most weight in the church year &mdash; and for every service that surrounds them.</p>')
out.append('<div class="brandline">LifeTogether &middot; 25 Years &middot; 500+ Churches &middot; 50M+ Campaigns</div>')
out.append('</div>')

# STATS
out.append('<div class="stats">')
for b, s in [(NCAT, "Categories"), (TOTAL, "Titles"), (E_TOTAL, "Easter"), (C_TOTAL, "Christmas")]:
    out.append('<div class="stat"><b>' + str(b) + '</b><span>' + s + '</span></div>')
out.append('</div>')

# INTRO
out.append('<div class="block"><div class="wrap">')
out.append('<span class="label">Why This Library Exists</span>')
out.append('<h2>The two Sundays you <em>cannot</em> improvise</h2>')
out.append('<p class="drop">Every church builds series. Almost no church builds Easter and Christmas the same way, because these two Sundays do not behave like the rest of the calendar. They are not week three of anything. Each one has to stand entirely on its own, in front of the largest and least-churched room a pastor will face all year, with a message that has been preached ten thousand times and still has to land like the first time.</p>')
out.append('<p>The existing Catalytic Sundays library holds 510 standalone titles distilled from the thirty thematic campaign categories. It is a strong collection. It also contains no Easter titles and no Christmas titles, because those categories were built around themes rather than dates. This edition closes that gap.</p>')
out.append('<p>Sixteen categories, twenty titles each, every one written to carry a full service by itself. No series runway, no devotional required, no small-group companion assumed. Eight categories run the Easter arc from Ash Wednesday through the Sunday after. Eight run the Christmas arc from Advent through the first Sunday of the new year. The two guest categories &mdash; Easter for the Skeptic and Christmas for the Skeptic &mdash; are written for the person who was dragged in by family and is deciding, somewhere around the third song, whether any of this is real.</p>')
out.append('<div class="note"><span class="label">How to use a Catalytic Sunday</span>')
out.append('<p style="margin-top:0"><strong>As a standalone:</strong> one message, one Sunday, complete in itself. <strong>As a launch:</strong> open a season with the single biggest idea, then let a 40-day, 30-day, 21-day, or 7-day format carry the follow-through. <strong>As a capstone:</strong> close the arc with its most concentrated statement.</p></div>')
out.append('</div></div>')

# INDEX
out.append('<div class="block alt"><div class="wrap">')
out.append('<span class="label">Contents</span>')
out.append('<h2>Sixteen categories <em>at a glance</em></h2>')
out.append('<div class="idx">')
i = 0
for name, blurb, items in EASTER:
    i += 1
    out.append('<a href="#c' + str(i) + '"><span class="n">' + ('%02d' % i) + '</span><span class="t">' + esc(name) + '</span><span class="c">' + str(len(items)) + '</span></a>')
for name, blurb, items in CHRISTMAS:
    i += 1
    out.append('<a href="#c' + str(i) + '"><span class="n">' + ('%02d' % i) + '</span><span class="t">' + esc(name) + '</span><span class="c">' + str(len(items)) + '</span></a>')
out.append('</div></div></div>')

# SEARCH
out.append('<div class="search"><div class="wrap">')
out.append('<input id="q" type="search" placeholder="Search all ' + str(TOTAL) + ' titles and subtitles&hellip;" autocomplete="off">')
out.append('<div class="hits" id="hits">' + str(TOTAL) + ' titles</div>')
out.append('</div></div>')

# PART ONE
out.append('<div class="wrap parthead"><span class="label">Part One</span>')
out.append('<h2>The Easter Arc</h2>')
out.append('<p style="color:#e6dfd0">Eight categories, ' + str(E_TOTAL) + ' titles &mdash; from the ashes that open Lent to the Sunday after Easter, when the crowd is gone and the follow-through decides whether any of it held.</p>')
out.append('<div class="rule"></div></div>')
i = 0
for name, blurb, items in EASTER:
    i += 1
    out.append(cat_block(i, name, blurb, items))

# PART TWO
out.append('<div class="wrap parthead"><span class="label">Part Two</span>')
out.append('<h2>The Christmas Arc</h2>')
out.append('<p style="color:#e6dfd0">Eight categories, ' + str(C_TOTAL) + ' titles &mdash; from the first candle of Advent to the first Sunday of the new year, including the two services most churches under-resource: the skeptic\'s Christmas and the grieving one.</p>')
out.append('<div class="rule"></div></div>')
for name, blurb, items in CHRISTMAS:
    i += 1
    out.append(cat_block(i, name, blurb, items))

# CLOSING
out.append('<div class="closing"><div class="wrap">')
out.append('<p class="q">A church does not launch a program on Easter morning. It releases a movement, and then spends the rest of the year proving it meant it.</p>')
out.append('<div class="attr">Brett Eastman &middot; LifeTogether</div>')
out.append('</div></div>')

out.append('<footer><div class="wrap">LifeTogether Ministries &middot; Catalytic Sundays &middot; Easter &amp; Christmas Edition &middot; ' + str(NCAT) + ' Categories &middot; ' + str(TOTAL) + ' Titles</div></footer>')
out.append('<script>' + JS + '</script>')
out.append('</body></html>')

html = "\n".join(out)
with io.open('/mnt/user-data/outputs/catalytic-sundays-easter-christmas.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("categories:", NCAT)
print("easter:", E_TOTAL, "christmas:", C_TOTAL, "total:", TOTAL)
print("bytes:", len(html))
