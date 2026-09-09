# -*- coding: utf-8 -*-
import io
from kits import KITS

def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

def para(s):
    return "".join('<p>' + esc(p) + '</p>' for p in s.split("\n\n"))

N = len(KITS)
DAYS = sum(len(k["dev"]) for k in KITS)
STEPS = sum(len(k["grp"]["personal"]) + len(k["grp"]["family"]) + len(k["grp"]["group"]) for k in KITS)

CSS = """
:root{--navy:#101a33;--navy-2:#16213d;--navy-3:#1c2a4a;--gold:#b8934e;
--gold-lt:#d9bc82;--cream:#f7f3ea;--rule:rgba(184,147,78,.28)}
*{box-sizing:border-box}
body{margin:0;background:var(--navy);color:var(--cream);
font-family:'Cormorant Garamond',Georgia,serif;font-size:19px;line-height:1.68;
-webkit-text-size-adjust:100%}
.wrap{max-width:800px;margin:0 auto;padding:0 22px}
h1,h2,h3,h4,h5{font-family:'Playfair Display',Georgia,serif;font-weight:600;line-height:1.15;margin:0}
.label{font-family:'Lato',system-ui,sans-serif;font-size:11px;letter-spacing:.22em;
text-transform:uppercase;color:var(--gold);font-weight:700}
.cover{padding:78px 0 58px;border-bottom:1px solid var(--rule);text-align:center}
.cover .label{display:block;margin-bottom:24px}
.cover h1{font-size:50px}
.cover h1 em{display:block;font-style:italic;font-size:26px;color:var(--gold-lt);
margin-top:12px;font-weight:400}
.cover .dek{font-size:20px;color:#e6dfd0;margin:24px auto 0;max-width:600px}
.brandline{font-family:'Lato',sans-serif;font-size:11px;letter-spacing:.18em;
text-transform:uppercase;color:#b9b0a0;margin-top:32px}
.stats{display:flex;flex-wrap:wrap;gap:1px;background:var(--rule);
border-top:1px solid var(--rule);border-bottom:1px solid var(--rule)}
.stat{flex:1 1 25%;min-width:120px;background:var(--navy);padding:24px 12px;text-align:center}
.stat b{display:block;font-family:'Playfair Display',serif;font-size:34px;
color:var(--gold-lt);font-weight:600}
.stat span{font-family:'Lato',sans-serif;font-size:10px;letter-spacing:.18em;
text-transform:uppercase;color:#b9b0a0}
.block{padding:54px 0;border-bottom:1px solid var(--rule)}
.block.alt{background:var(--navy-2)}
.block h2{font-size:32px;margin-bottom:6px}
.block h2 em{font-style:italic;color:var(--gold-lt)}
.block p{color:#e6dfd0;margin:16px 0 0}
.drop::first-letter{font-family:'Playfair Display',serif;float:left;font-size:62px;
line-height:.82;padding:6px 12px 0 0;color:var(--gold)}
.spec{border:1px solid var(--rule);padding:22px;margin-top:26px;background:var(--navy-2)}
.spec .label{display:block;margin-bottom:12px}
.spec ol{margin:0;padding-left:20px;color:#ded6c6}
.spec li{margin-bottom:8px}
.kithead{padding:70px 0 0;border-top:2px solid var(--gold)}
.kithead .label{display:block;margin-bottom:10px}
.kithead h2{font-size:38px}
.kithead .ks{font-style:italic;color:#c8c0b2;font-size:20px;margin-top:8px}
.kithead .why{margin-top:18px;border-left:2px solid var(--gold);padding:4px 0 4px 18px;
color:#b6ac9d;font-size:17px}
.sec{padding:44px 0 0}
.sec .st{font-family:'Lato',sans-serif;font-size:10px;letter-spacing:.24em;
text-transform:uppercase;color:var(--gold);border-bottom:1px solid var(--rule);
padding-bottom:10px;margin-bottom:24px;font-weight:700}
.meta{border-top:1px solid rgba(184,147,78,.18);
border-bottom:1px solid rgba(184,147,78,.18);padding:14px 0;margin-bottom:20px}
.row{display:flex;gap:14px;padding:7px 0;align-items:baseline}
.row .k{font-family:'Lato',sans-serif;font-size:10px;letter-spacing:.16em;
text-transform:uppercase;color:var(--gold);min-width:82px;flex-shrink:0}
.row .v{flex:1;color:#efe9dc}
.row .v.idea{font-family:'Playfair Display',serif;font-size:21px;line-height:1.35;
color:var(--gold-lt);font-style:italic}
.mov{display:flex;gap:14px;padding:11px 0;border-bottom:1px solid rgba(184,147,78,.12)}
.mov .mn{font-family:'Playfair Display',serif;font-size:19px;color:var(--gold);
min-width:26px;flex-shrink:0}
.mov .mt{flex:1;color:#e6dfd0}
.panel{margin-top:18px;background:var(--navy-2);border-left:2px solid var(--gold);
padding:14px 18px}
.panel .label{display:block;margin-bottom:5px}
.panel p{margin:0;color:#ded6c6;font-size:18px}
.day{padding:26px 0;border-bottom:1px solid rgba(184,147,78,.16)}
.day .dn{font-family:'Lato',sans-serif;font-size:10px;letter-spacing:.2em;
text-transform:uppercase;color:var(--gold);margin-bottom:6px}
.day h5{font-size:24px}
.day .ref{font-family:'Lato',sans-serif;font-size:12px;letter-spacing:.1em;
color:var(--gold-lt);margin-top:5px}
.day .rd{margin-top:14px}
.day .rd p{margin:0 0 13px;color:#e9e2d4}
.day .rd p:last-child{margin-bottom:0}
.qa{margin-top:16px;display:flex;gap:12px;padding:9px 0;
border-top:1px solid rgba(184,147,78,.14)}
.qa .qk{font-family:'Lato',sans-serif;font-size:10px;letter-spacing:.16em;
text-transform:uppercase;color:var(--gold);min-width:64px;flex-shrink:0;padding-top:4px}
.qa .qv{flex:1;color:#ded6c6;font-size:18px}
.gq{display:flex;gap:14px;padding:11px 0;border-bottom:1px solid rgba(184,147,78,.12)}
.gq .gn{font-family:'Playfair Display',serif;font-size:18px;color:var(--gold);
min-width:24px;flex-shrink:0}
.gq .gt{flex:1;color:#e6dfd0}
.lanes{margin-top:28px;display:flex;flex-wrap:wrap;gap:1px;background:var(--rule);
border:1px solid var(--rule)}
.lane{flex:1 1 240px;background:var(--navy-2);padding:20px}
.lane .lh{font-family:'Lato',sans-serif;font-size:10px;letter-spacing:.2em;
text-transform:uppercase;color:var(--gold);font-weight:700;margin-bottom:12px}
.lane ul{margin:0;padding-left:18px;color:#ded6c6;font-size:17px}
.lane li{margin-bottom:9px}
.closing{padding:64px 0;text-align:center;background:var(--navy-2)}
.closing .q{font-family:'Playfair Display',serif;font-style:italic;font-size:26px;
color:var(--gold-lt);max-width:620px;margin:0 auto;line-height:1.4}
.closing .attr{font-family:'Lato',sans-serif;font-size:11px;letter-spacing:.2em;
text-transform:uppercase;color:#9d958a;margin-top:22px}
footer{padding:38px 0 58px;text-align:center;font-family:'Lato',sans-serif;
font-size:11px;letter-spacing:.14em;text-transform:uppercase;color:#8d8579}
@media(max-width:620px){
body{font-size:18px}
.cover{padding:52px 0 42px}.cover h1{font-size:33px}.cover h1 em{font-size:20px}
.block h2{font-size:27px}.kithead h2{font-size:29px}.day h5{font-size:22px}
.row{flex-direction:column;gap:3px}.row .k{min-width:0}
.row .v.idea{font-size:19px}.stat b{font-size:28px}
.qa{flex-direction:column;gap:3px}.qa .qk{min-width:0}
}
"""

def kit_html(i, k):
    o = []
    o.append('<div class="wrap kithead">')
    o.append('<span class="label">Catalyst Kit ' + ('%02d' % i) + ' &middot; ' + esc(k["cat"]) + '</span>')
    o.append('<h2>' + esc(k["t"]) + '</h2>')
    o.append('<p class="ks">' + esc(k["s"]) + '</p>')
    o.append('<p class="why">' + esc(k["why"]) + '</p>')
    o.append('</div>')

    # Sermon
    o.append('<div class="wrap sec"><div class="st">One &middot; The Sunday Message</div>')
    o.append('<div class="meta">')
    o.append('<div class="row"><div class="k">Text</div><div class="v">' + esc(k["x"]) + '</div></div>')
    o.append('<div class="row"><div class="k">Big Idea</div><div class="v idea">' + esc(k["b"]) + '</div></div>')
    o.append('</div>')
    for n, mv in enumerate(k["m"], 1):
        o.append('<div class="mov"><div class="mn">' + str(n) + '</div><div class="mt">' + esc(mv) + '</div></div>')
    o.append('<div class="panel"><span class="label">Where the story goes</span><p>' + esc(k["story"]) + '</p></div>')
    o.append('<div class="panel"><span class="label">The turn</span><p>' + esc(k["turn"]) + '</p></div>')
    o.append('<div class="panel"><span class="label">Close</span><p>' + esc(k["close"]) + '</p></div>')
    o.append('</div>')

    # Devotional
    o.append('<div class="wrap sec"><div class="st">Two &middot; The Seven-Day Devotional</div>')
    for n, (dt, ref, rd, q, act) in enumerate(k["dev"], 1):
        o.append('<div class="day"><div class="dn">Day ' + str(n) + '</div>')
        o.append('<h5>' + esc(dt) + '</h5>')
        o.append('<div class="ref">' + esc(ref) + ' (NIV)</div>')
        o.append('<div class="rd">' + para(rd) + '</div>')
        o.append('<div class="qa"><div class="qk">Reflect</div><div class="qv">' + esc(q) + '</div></div>')
        o.append('<div class="qa"><div class="qk">Do</div><div class="qv">' + esc(act) + '</div></div>')
        o.append('</div>')
    o.append('</div>')

    # Group session
    g = k["grp"]
    o.append('<div class="wrap sec"><div class="st">Three &middot; The Small Group Session</div>')
    o.append('<div class="panel"><span class="label">Open</span><p>' + esc(g["open"]) + '</p></div>')
    o.append('<div class="panel"><span class="label">Read together</span><p>' + esc(g["read"]) + '</p></div>')
    o.append('<div style="margin-top:24px"><span class="label">Discussion</span></div>')
    for n, q in enumerate(g["qs"], 1):
        o.append('<div class="gq"><div class="gn">' + str(n) + '</div><div class="gt">' + esc(q) + '</div></div>')
    o.append('<div class="lanes">')
    for lh, key in [("Next step &mdash; personal", "personal"),
                    ("Next step &mdash; family", "family"),
                    ("Next step &mdash; group", "group")]:
        o.append('<div class="lane"><div class="lh">' + lh + '</div><ul>')
        for s in g[key]:
            o.append('<li>' + esc(s) + '</li>')
        o.append('</ul></div>')
    o.append('</div></div>')
    return "\n".join(o)

out = []
out.append('<!DOCTYPE html>')
out.append('<html lang="en"><head><meta charset="utf-8">')
out.append('<meta name="viewport" content="width=device-width, initial-scale=1">')
out.append('<title>The Catalyst Kit &mdash; One Sunday, Seven Days, One Room | LifeTogether</title>')
out.append('<link rel="preconnect" href="https://fonts.googleapis.com">')
out.append('<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>')
out.append('<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,500;0,600;1,500&family=Cormorant+Garamond:ital,wght@0,400;0,600;1,400&family=Lato:wght@400;700&display=swap" rel="stylesheet">')
out.append('<style>' + CSS + '</style></head><body>')

out.append('<div class="wrap cover">')
out.append('<span class="label">Catalytic Sundays &middot; Volume Three</span>')
out.append('<h1>The Catalyst Kit<em>One Sunday. Seven Days. One Room.</em></h1>')
out.append('<p class="dek">The forty-day campaign architecture compressed into a single week &mdash; message, daily devotional, and a group session that sends people somewhere.</p>')
out.append('<div class="brandline">LifeTogether &middot; 25 Years &middot; 500+ Churches &middot; 50M+ Campaigns</div>')
out.append('</div>')

out.append('<div class="stats">')
for b, s in [(N, "Complete Kits"), (DAYS, "Devotional Days"), (N, "Group Sessions"), (STEPS, "Next Steps")]:
    out.append('<div class="stat"><b>' + str(b) + '</b><span>' + s + '</span></div>')
out.append('</div>')

out.append('<div class="block"><div class="wrap">')
out.append('<span class="label">What Changed</span>')
out.append('<h2>A single Sunday just became <em>a campaign</em></h2>')
out.append('<p class="drop">A sermon reaches a person for thirty-five minutes and then competes with the rest of their life. A sermon followed by seven days of reading and a room where someone asks how it went is a different instrument entirely. That is the whole logic of the forty-day campaign, and there is no reason it only works at forty days. Compressed to a week, it becomes the smallest complete unit of the campaign system &mdash; and the most likely thing a hesitant church will actually say yes to.</p>')
out.append('<p>The kit is deliberately finite. Seven days is short enough that a person who has never finished a devotional will finish this one, and short enough that a pastor can run four of them in a year without building a season around each. The group session lands after the devotional rather than before it, so people arrive having already done the work rather than hearing it for the first time.</p>')
out.append('<p>Every session ends in three lanes, because a next step that only addresses the individual leaves the two systems with the most leverage untouched. What you decide alone, what your household decides, and what the group decides together are different commitments with different failure rates, and the group lane is the one that actually holds.</p>')
out.append('<div class="spec"><span class="label">The kit, in nine parts</span><ol>')
for s in ["The Sunday message &mdash; text, big idea, movements, illustration slot, turn, close",
          "Seven devotional days, each with a reading of roughly 150 words",
          "A reflection question per day",
          "A concrete action per day &mdash; something done, not considered",
          "An opening question for the group that anyone can answer",
          "A shared Scripture reading",
          "Five discussion questions that follow the week rather than repeat the sermon",
          "Three next steps for the person",
          "Three for the family, and three for the group"]:
    out.append('<li>' + s + '</li>')
out.append('</ol></div>')
out.append('<p>Four kits follow, chosen because they stress the format differently: the flagship Easter message, the hardest pastoral Sunday on the calendar, the invitation Sunday that has to fill a room, and the connection Sunday that has to keep it full.</p>')
out.append('</div></div>')

for i, k in enumerate(KITS, 1):
    out.append(kit_html(i, k))

out.append('<div class="closing"><div class="wrap">')
out.append('<p class="q">A church does not launch a program on Easter morning. It releases a movement, and then spends the rest of the year proving it meant it.</p>')
out.append('<div class="attr">Brett Eastman &middot; LifeTogether</div></div></div>')
out.append('<footer><div class="wrap">LifeTogether Ministries &middot; The Catalyst Kit &middot; Volume Three &middot; ' + str(N) + ' Kits &middot; ' + str(DAYS) + ' Devotional Days</div></footer>')
out.append('</body></html>')

html = "\n".join(out)
with io.open('/mnt/user-data/outputs/catalyst-kit-vol-3.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("kits:", N, "days:", DAYS, "next steps:", STEPS, "bytes:", len(html))
