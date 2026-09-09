# -*- coding: utf-8 -*-
import io
from outlines import RESURRECTION, CHRISTMAS_EVE

def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

TOTAL = len(RESURRECTION) + len(CHRISTMAS_EVE)

CSS = """
:root{--navy:#101a33;--navy-2:#16213d;--navy-3:#1c2a4a;--gold:#b8934e;
--gold-lt:#d9bc82;--cream:#f7f3ea;--rule:rgba(184,147,78,.28)}
*{box-sizing:border-box}
body{margin:0;background:var(--navy);color:var(--cream);
font-family:'Cormorant Garamond',Georgia,serif;font-size:19px;line-height:1.65;
-webkit-text-size-adjust:100%}
.wrap{max-width:800px;margin:0 auto;padding:0 22px}
h1,h2,h3{font-family:'Playfair Display',Georgia,serif;font-weight:600;line-height:1.15;margin:0}
.label{font-family:'Lato',system-ui,sans-serif;font-size:11px;letter-spacing:.22em;
text-transform:uppercase;color:var(--gold);font-weight:700}
.cover{padding:76px 0 60px;border-bottom:1px solid var(--rule);text-align:center}
.cover .label{display:block;margin-bottom:24px}
.cover h1{font-size:50px}
.cover h1 em{display:block;font-style:italic;font-size:28px;color:var(--gold-lt);
margin-top:12px;font-weight:400}
.cover .dek{font-size:20px;color:#e6dfd0;margin:24px auto 0;max-width:580px}
.brandline{font-family:'Lato',sans-serif;font-size:11px;letter-spacing:.18em;
text-transform:uppercase;color:#b9b0a0;margin-top:32px}
.block{padding:56px 0;border-bottom:1px solid var(--rule)}
.block.alt{background:var(--navy-2)}
.block h2{font-size:32px;margin-bottom:6px}
.block h2 em{font-style:italic;color:var(--gold-lt)}
.block p{color:#e6dfd0;margin:16px 0 0}
.drop::first-letter{font-family:'Playfair Display',serif;float:left;font-size:62px;
line-height:.82;padding:6px 12px 0 0;color:var(--gold)}
.spec{border:1px solid var(--rule);padding:24px;margin-top:28px}
.spec .label{display:block;margin-bottom:12px}
.spec ol{margin:0;padding-left:20px;color:#ded6c6}
.spec li{margin-bottom:7px}
.parthead{padding:64px 0 0}
.parthead .label{display:block;margin-bottom:12px}
.parthead h2{font-size:40px}
.parthead .rule{height:1px;background:var(--rule);margin-top:24px}
.serm{padding:46px 0;border-bottom:1px solid var(--rule)}
.serm .num{font-family:'Lato',sans-serif;font-size:11px;letter-spacing:.2em;
color:var(--gold);margin-bottom:8px}
.serm h3{font-size:30px}
.serm .sub{font-style:italic;color:#c8c0b2;font-size:19px;margin-top:6px}
.meta{margin-top:22px;border-top:1px solid rgba(184,147,78,.18);
border-bottom:1px solid rgba(184,147,78,.18);padding:16px 0}
.row{display:flex;gap:14px;padding:7px 0;align-items:baseline}
.row .k{font-family:'Lato',sans-serif;font-size:10px;letter-spacing:.16em;
text-transform:uppercase;color:var(--gold);min-width:82px;flex-shrink:0}
.row .v{flex:1;color:#efe9dc}
.row .v.idea{font-family:'Playfair Display',serif;font-size:21px;line-height:1.35;
color:var(--gold-lt);font-style:italic}
.movs{margin-top:24px}
.movs .label{display:block;margin-bottom:12px}
.mov{display:flex;gap:14px;padding:11px 0;border-bottom:1px solid rgba(184,147,78,.12)}
.mov .mn{font-family:'Playfair Display',serif;font-size:19px;color:var(--gold);
min-width:26px;flex-shrink:0}
.mov .mt{flex:1;color:#e6dfd0}
.panel{margin-top:22px;background:var(--navy-2);border-left:2px solid var(--gold);
padding:16px 20px}
.panel .label{display:block;margin-bottom:6px}
.panel p{margin:0;color:#ded6c6;font-size:18px}
.bl{margin-top:18px;font-family:'Lato',sans-serif;font-size:13px;color:#a9a094;
letter-spacing:.04em}
.bl b{color:var(--gold);font-weight:700;letter-spacing:.16em;font-size:10px;
text-transform:uppercase;display:block;margin-bottom:4px}
.closing{padding:66px 0;text-align:center;background:var(--navy-2)}
.closing .q{font-family:'Playfair Display',serif;font-style:italic;font-size:26px;
color:var(--gold-lt);max-width:620px;margin:0 auto;line-height:1.4}
.closing .attr{font-family:'Lato',sans-serif;font-size:11px;letter-spacing:.2em;
text-transform:uppercase;color:#9d958a;margin-top:22px}
footer{padding:38px 0 58px;text-align:center;font-family:'Lato',sans-serif;
font-size:11px;letter-spacing:.14em;text-transform:uppercase;color:#8d8579}
@media(max-width:620px){
body{font-size:18px}
.cover{padding:52px 0 42px}.cover h1{font-size:34px}.cover h1 em{font-size:21px}
.block h2,.parthead h2{font-size:28px}.serm h3{font-size:25px}
.row{flex-direction:column;gap:3px}.row .k{min-width:0}
.row .v.idea{font-size:19px}
}
"""

def sermon(i, d):
    o = []
    o.append('<div class="wrap serm">')
    o.append('<div class="num">' + ('%02d' % i) + '</div>')
    o.append('<h3>' + esc(d["t"]) + '</h3>')
    o.append('<p class="sub">' + esc(d["s"]) + '</p>')
    o.append('<div class="meta">')
    o.append('<div class="row"><div class="k">Text</div><div class="v">' + esc(d["x"]) + '</div></div>')
    o.append('<div class="row"><div class="k">Big Idea</div><div class="v idea">' + esc(d["b"]) + '</div></div>')
    o.append('</div>')
    o.append('<div class="movs"><span class="label">Movements</span>')
    for n, mv in enumerate(d["m"], 1):
        o.append('<div class="mov"><div class="mn">' + str(n) + '</div><div class="mt">' + esc(mv) + '</div></div>')
    o.append('</div>')
    o.append('<div class="panel"><span class="label">Where the story goes</span><p>' + esc(d["story"]) + '</p></div>')
    o.append('<div class="panel"><span class="label">The turn</span><p>' + esc(d["turn"]) + '</p></div>')
    o.append('<div class="panel"><span class="label">Close</span><p>' + esc(d["close"]) + '</p></div>')
    o.append('<div class="bl"><b>Bulletin line</b>' + esc(d["bl"]) + '</div>')
    o.append('</div>')
    return "\n".join(o)

out = []
out.append('<!DOCTYPE html>')
out.append('<html lang="en"><head><meta charset="utf-8">')
out.append('<meta name="viewport" content="width=device-width, initial-scale=1">')
out.append('<title>Catalytic Sundays &mdash; Sermon Outline Volume One | LifeTogether</title>')
out.append('<link rel="preconnect" href="https://fonts.googleapis.com">')
out.append('<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>')
out.append('<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,500;0,600;1,500&family=Cormorant+Garamond:ital,wght@0,400;0,600;1,400&family=Lato:wght@400;700&display=swap" rel="stylesheet">')
out.append('<style>' + CSS + '</style></head><body>')

out.append('<div class="wrap cover">')
out.append('<span class="label">Catalytic Sundays &middot; Outline Volume One</span>')
out.append('<h1>The Preaching Kit<em>Resurrection Sunday &amp; Christmas Eve</em></h1>')
out.append('<p class="dek">' + str(TOTAL) + ' complete sermon outlines &mdash; text, big idea, movements, illustration slot, application, close, and bulletin line.</p>')
out.append('<div class="brandline">LifeTogether &middot; 25 Years &middot; 500+ Churches &middot; 50M+ Campaigns</div>')
out.append('</div>')

out.append('<div class="block"><div class="wrap">')
out.append('<span class="label">What This Is</span>')
out.append('<h2>A title is inventory. <em>This</em> is the product.</h2>')
out.append('<p class="drop">A list of sermon titles is worth something to a pastor staring at a blank calendar in January. It is worth considerably more when each title arrives with a text already chosen, a big idea already stated in one sentence, three movements that actually move, and a named place where the story goes. That is the difference between a catalog a church browses and a resource a church renews.</p>')
out.append('<p>This volume proves the format on the two categories that carry the most weight: Resurrection Sunday and Christmas Eve. Every outline follows the same seven-part shape, which means the remaining categories can be batched against this master without drifting.</p>')
out.append('<p>These are outlines, not manuscripts. The illustration slot is deliberately a slot &mdash; it names the kind of story that belongs there and leaves the story itself to the preacher, because a borrowed illustration is the fastest way for a congregation to know their pastor is reading someone else&rsquo;s sermon. Scripture references are NIV. Verify every text against your own Bible before you preach it.</p>')
out.append('<div class="spec"><span class="label">The seven-part shape</span><ol>')
for s in ["Text &mdash; the primary passage, chosen rather than assembled",
          "Big idea &mdash; the whole sermon in one sentence",
          "Movements &mdash; three or four, each one moving somewhere new",
          "Where the story goes &mdash; the kind of illustration the slot needs",
          "The turn &mdash; what the listener does about it",
          "Close &mdash; the last line, written first",
          "Bulletin line &mdash; the promotional sentence"]:
    out.append('<li>' + s + '</li>')
out.append('</ol></div>')
out.append('</div></div>')

out.append('<div class="wrap parthead"><span class="label">Part One</span>')
out.append('<h2>Resurrection Sunday</h2>')
out.append('<p style="color:#e6dfd0">Twenty complete outlines for the highest-attendance, highest-stakes Sunday of the year.</p>')
out.append('<div class="rule"></div></div>')
for i, d in enumerate(RESURRECTION, 1):
    out.append(sermon(i, d))

out.append('<div class="wrap parthead"><span class="label">Part Two</span>')
out.append('<h2>Christmas Eve</h2>')
out.append('<p style="color:#e6dfd0">Twenty complete outlines for candlelight, for full rooms, and for the most unchurched crowd a pastor will face all year.</p>')
out.append('<div class="rule"></div></div>')
for i, d in enumerate(CHRISTMAS_EVE, 1):
    out.append(sermon(i, d))

out.append('<div class="closing"><div class="wrap">')
out.append('<p class="q">A church does not launch a program on Easter morning. It releases a movement, and then spends the rest of the year proving it meant it.</p>')
out.append('<div class="attr">Brett Eastman &middot; LifeTogether</div>')
out.append('</div></div>')
out.append('<footer><div class="wrap">LifeTogether Ministries &middot; Catalytic Sundays &middot; Outline Volume One &middot; ' + str(TOTAL) + ' Complete Outlines</div></footer>')
out.append('</body></html>')

html = "\n".join(out)
with io.open('/mnt/user-data/outputs/catalytic-sundays-outlines-vol-1.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("outlines:", TOTAL, "bytes:", len(html))
