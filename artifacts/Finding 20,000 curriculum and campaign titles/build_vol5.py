# -*- coding: utf-8 -*-
import io
from vol5_data import CATS
from build_vol4 import V4CSS, head, esc

TOTAL = sum(sum(len(t[1]) for t in c[4]) for c in CATS)
NCAT = len(CATS)

EXTRA = """
.explain{margin-top:20px;color:#e6dfd0}
.exp{margin-top:22px;background:var(--navy-2);border-left:2px solid var(--gold);padding:18px 22px}
.exp .label{display:block;margin-bottom:8px}
.exp p{margin:0;color:#ded6c6;font-size:18px}
"""

o = [head('Catalytic Sundays &mdash; Volume Five | LifeTogether', V4CSS + EXTRA)]
o.append('<div class="wrap cover"><span class="label">Catalytic Sundays &middot; Volume Five</span>')
o.append('<h1>The Challenge Library<em>Sundays That Ask People to Do Something</em></h1>')
o.append('<p class="dek">' + str(TOTAL) + ' messages built to start a challenge, run a challenge, and celebrate what happened &mdash; each category with the experience that makes it memorable.</p>')
o.append('<div class="brandline">LifeTogether &middot; 25 Years &middot; 500+ Churches &middot; 50M+ Campaigns</div></div>')

o.append('<div class="stats">')
for b, s in [(NCAT, "Categories"), (TOTAL, "Titles"), (100, "Short Challenges"), (80, "21-Day Tracks")]:
    o.append('<div class="stat"><b>' + str(b) + '</b><span>' + s + '</span></div>')
o.append('</div>')

o.append('<div class="block"><div class="wrap"><span class="label">The Shift</span>')
o.append('<h2>From <em>hearing</em> to doing</h2>')
o.append('<p class="drop">Everything in the first four volumes is a message. Everything in this one is an assignment. That is a meaningful difference: a congregation that is asked to do something for seven days, and then asked to report on it, forms differently than a congregation that is asked to consider something for thirty-five minutes. The sermon still matters, but here it functions as a starting gun rather than the whole event.</p>')
o.append('<p>Every category below carries an explainer and, more importantly, an experience &mdash; the specific, physical, stageable thing that turns a good message into a Sunday people describe to somebody else on Tuesday. Those are the parts churches usually improvise, and they are the parts people remember longest.</p>')
o.append('</div></div>')

o.append('<div class="block alt"><div class="wrap"><span class="label">Contents</span>')
o.append('<h2>Seven categories <em>at a glance</em></h2><div class="idx">')
for i, (name, expl, exper, hinge, tracks) in enumerate(CATS, 1):
    n = sum(len(t[1]) for t in tracks)
    o.append('<a href="#c' + str(i) + '"><span class="n">' + ('%02d' % i) + '</span><span class="t">' + esc(name) + '</span><span class="c">' + str(n) + '</span></a>')
o.append('</div></div></div>')

o.append('<div class="search"><div class="wrap">')
o.append('<input id="q" type="search" placeholder="Search all ' + str(TOTAL) + ' titles&hellip;" autocomplete="off">')
o.append('<div class="hits" id="hits">' + str(TOTAL) + ' titles</div></div></div>')

for i, (name, expl, exper, hinge, tracks) in enumerate(CATS, 1):
    o.append('<div class="cat-wrap" id="c' + str(i) + '"><div class="wrap cat">')
    o.append('<div class="num">' + ('%02d' % i) + '</div><h3>' + esc(name) + '</h3>')
    o.append('<p class="explain">' + esc(expl) + '</p>')
    o.append('<div class="exp"><span class="label">Make it an experience</span><p>' + exper + '</p></div>')
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
            hay = (t + ' ' + s + ' ' + name + ' ' + (tname or '')).lower().replace('"', '').replace('&middot;', '')
            o.append('<div class="entry" data-s="' + esc(hay) + '"><div class="i">' + ('%02d' % j) + '</div>')
            o.append('<div><div class="ti">' + esc(t) + '</div><div class="st">' + s + '</div></div></div>')
        o.append('</div></div>')
    o.append('</div></div>')

o.append('<div class="closing"><div class="wrap"><p class="q">A church does not launch a program on Easter morning. It releases a movement, and then spends the rest of the year proving it meant it.</p>')
o.append('<div class="attr">Brett Eastman &middot; LifeTogether</div></div></div>')
o.append('<footer><div class="wrap">LifeTogether Ministries &middot; Catalytic Sundays &middot; Volume Five &middot; ' + str(NCAT) + ' Categories &middot; ' + str(TOTAL) + ' Titles</div></footer>')
o.append('<script>' + __import__('build_vol4').JS + '</script></body></html>')

html = "\n".join(o)
with io.open('/mnt/user-data/outputs/catalytic-sundays-vol-5.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("VOL5 categories:", NCAT, "titles:", TOTAL, "bytes:", len(html))
