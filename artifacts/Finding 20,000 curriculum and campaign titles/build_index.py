# -*- coding: utf-8 -*-
import io
from build_vol4 import BASE, head, esc

V1 = "catalytic-sundays-easter-christmas.html"
V2 = "catalytic-sundays-calendar-strategic.html"
V3 = "catalyst-kit-vol-3.html"
V4 = "catalytic-sundays-vol-4.html"
OUT1 = "catalytic-sundays-outlines-vol-1.html"

# (display, file, anchor, count, note)
VOLUMES = [
("Volume One &mdash; The Easter and Christmas Arcs", V1,
 "320 titles across 16 categories. The two Sundays a church cannot improvise.", [
 ("Resurrection Sunday", "c1", 20, "Kit built"),
 ("Good Friday", "c2", 20, ""),
 ("Palm Sunday", "c3", 20, ""),
 ("Holy Week &amp; Maundy Thursday", "c4", 20, ""),
 ("Easter for the Skeptic", "c5", 20, ""),
 ("The Sunday After Easter", "c6", 20, ""),
 ("Ash Wednesday &amp; the Road to Lent", "c7", 20, ""),
 ("Easter for the Grieving", "c8", 20, ""),
 ("Christmas Eve", "c9", 20, "Outlined"),
 ("Christmas Day &amp; Christmas Sunday", "c10", 20, ""),
 ("Advent Sunday Singles", "c11", 20, ""),
 ("Christmas for the Skeptic", "c12", 20, ""),
 ("The Characters of the Nativity", "c13", 20, ""),
 ("Blue Christmas", "c14", 20, ""),
 ("After Christmas &amp; New Year", "c15", 20, ""),
 ("The Incarnation", "c16", 20, ""),
]),
("Volume Two &mdash; Calendar Locks and Strategic Weekends", V2,
 "400 titles across 8 weekends. Every category carries a campaign hinge.", [
 ("Mother's Day", "c1", 100, "5 tracks &middot; Kit built"),
 ("Father's Day", "c2", 100, "5 tracks"),
 ("Graduation", "c3", 100, "5 tracks"),
 ("End-of-Year Giving", "c4", 20, ""),
 ("Baptism Sunday", "c5", 20, ""),
 ("Baby Dedication &amp; Family Blessing", "c6", 20, ""),
 ("Series Launch &amp; Friends Sunday", "c7", 20, "Kit built"),
 ("Group Life Launch &amp; the Call to Serve", "c8", 20, "Kit built"),
]),
("Volume Four &mdash; The Working Calendar", V4,
 "375 titles across 15 categories. The Sundays between the holidays.", [
 ("Thanksgiving", "c1", 20, ""),
 ("Next Step Sundays", "c2", 60, "3 tracks"),
 ("Any Given Sunday", "c3", 20, ""),
 ("Communion Sundays", "c4", 25, ""),
 ("Prayer Sundays", "c5", 20, ""),
 ("Advent Kickoff", "c6", 20, "Launches 21-day devotional"),
 ("Lent Kickoff", "c7", 20, "Launches 40-day devotional"),
 ("Vision Sunday", "c8", 20, ""),
 ("New Year's Sunday", "c9", 20, ""),
 ("Serve Sunday", "c10", 20, ""),
 ("Connection Sunday", "c11", 20, ""),
 ("Pair Up and Group Up", "c12", 20, ""),
 ("Church at Home", "c13", 20, ""),
 ("Ask Sundays", "c14", 20, ""),
 ("Ministry Launch Sundays", "c15", 50, "One per ministry"),
]),
]

PROPOSED = [
("Fall Launch &amp; Back to School", "The second-biggest reset of the year. Families re-enter routine in late August, which makes it the strongest group-launch window after January and the one most churches sleep through."),
("Pentecost Sunday", "The birthday of the church, almost universally under-preached in evangelical congregations. A whole category on the Spirit, power, and the sending."),
("Memorial Day &amp; Veterans Sunday", "Honor, sacrifice, freedom, and grief, handled with care rather than avoided. High attendance among people who rarely come."),
("Church Anniversary &amp; Founder's Sunday", "Remembering the story, honoring the people who built it, and handing the next chapter to a younger generation. Pairs naturally with a legacy giving moment."),
("Building Milestones", "Groundbreaking, dedication, first service in a new space, mortgage burning. Rare, emotional, and almost always improvised because no library exists."),
("Crisis Response Sundays", "The message written in forty-eight hours after a local tragedy, a national event, or a loss inside the congregation. Every pastor needs these and nobody has them ready."),
("Sanctity of Life &amp; Justice Sundays", "The hard-topic Sunday, written with conviction and pastoral care so it can be preached without splitting a room."),
("Ordination, Commissioning &amp; Pastor Appreciation", "Setting people apart, sending staff, honoring leaders, and installing elders. Ceremony without a script is how these usually go."),
("Fifth Sunday, Guest Speaker &amp; Pulpit Supply", "The drop-in Sunday. A guest, an intern's first message, or the week the pastor is out. Overlaps with Any Given Sunday but built for someone who does not know the congregation."),
("Sending &amp; Multiplication Sundays", "Launching a campus, commissioning a plant team, sending missionaries. The Sundays where a church gives away its best people on purpose."),
]

CSS = BASE + """
.volhead{padding:56px 0 0;border-top:2px solid var(--gold)}
.volhead .label{display:block;margin-bottom:10px}
.volhead h2{font-size:34px}
.volhead .vd{color:#c8c0b2;font-size:19px;margin-top:8px;font-style:italic}
.volhead .open{display:inline-block;margin-top:18px;font-family:'Lato',sans-serif;
font-size:11px;letter-spacing:.18em;text-transform:uppercase;color:var(--navy);
background:var(--gold);padding:11px 22px;text-decoration:none;font-weight:700}
.dir{margin-top:26px;border-top:1px solid var(--rule)}
.dir a{display:flex;gap:14px;align-items:baseline;padding:15px 2px;
border-bottom:1px solid rgba(184,147,78,.14);color:var(--cream);text-decoration:none}
.dir a:hover{color:var(--gold-lt)}
.dir .n{font-family:'Lato',sans-serif;font-size:11px;letter-spacing:.14em;
color:var(--gold);min-width:30px;flex-shrink:0}
.dir .t{flex:1;font-size:20px}
.dir .note{font-family:'Lato',sans-serif;font-size:10px;letter-spacing:.12em;
text-transform:uppercase;color:var(--gold-lt);flex-shrink:0}
.dir .c{font-family:'Lato',sans-serif;font-size:12px;color:#9d958a;
min-width:38px;text-align:right;flex-shrink:0}
.kitcard{margin-top:26px;border:1px solid var(--rule);background:var(--navy-2);padding:24px}
.kitcard h3{font-size:25px;color:var(--gold-lt)}
.kitcard p{margin-top:12px;color:#ded6c6;font-size:18px}
.kitcard .open{display:inline-block;margin-top:18px;font-family:'Lato',sans-serif;
font-size:11px;letter-spacing:.18em;text-transform:uppercase;color:var(--navy);
background:var(--gold);padding:11px 22px;text-decoration:none;font-weight:700}
.prop{display:flex;gap:16px;padding:18px 0;border-bottom:1px solid rgba(184,147,78,.14)}
.prop .pn{font-family:'Playfair Display',serif;font-size:20px;color:var(--gold);
min-width:32px;flex-shrink:0}
.prop .pb h4{font-size:22px}
.prop .pb p{margin-top:6px;color:#c8c0b2;font-size:18px}
.flag{margin-top:28px;border-left:2px solid var(--gold);padding:8px 0 8px 20px}
.flag .label{display:block;margin-bottom:8px}
.flag p{margin:0 0 12px;color:#ded6c6}
.flag p:last-child{margin-bottom:0}
@media(max-width:620px){
.volhead h2{font-size:27px}.dir .t{font-size:18px}.dir .note{display:none}
}
"""

TOTAL_ALL = 320 + 400 + 375

o = [head('Catalytic Sundays &mdash; Master Directory | LifeTogether', CSS)]
o.append('<div class="wrap cover"><span class="label">LifeTogether &middot; The Single-Message Library</span>')
o.append('<h1>Catalytic Sundays<em>Master Directory</em></h1>')
o.append('<p class="dek">Every category, every count, every volume &mdash; one page that opens the whole library.</p>')
o.append('<div class="brandline">LifeTogether &middot; 25 Years &middot; 500+ Churches &middot; 50M+ Campaigns</div></div>')

o.append('<div class="stats">')
for b, s in [(39, "Categories"), (TOTAL_ALL, "Titles"), (40, "Full Outlines"), (4, "Catalyst Kits")]:
    o.append('<div class="stat"><b>' + str(b) + '</b><span>' + s + '</span></div>')
o.append('</div>')

o.append('<div class="block"><div class="wrap"><span class="label">How to Use This</span>')
o.append('<h2>One page, <em>the whole library</em></h2>')
o.append('<p class="drop">Every category below links straight into the volume that holds it. Counts are honest and match the actual files. Where a category has been built past the title stage &mdash; a full outline, or a complete Catalyst Kit with a seven-day devotional and a group session &mdash; it is marked, so nobody has to guess what is finished and what is inventory.</p>')
o.append('<p>Keep all five files in one folder and every link on this page works offline.</p>')
o.append('</div></div>')

for vname, vfile, vdesc, cats in VOLUMES:
    n = sum(c[2] for c in cats)
    o.append('<div class="wrap volhead"><span class="label">' + str(len(cats)) + ' Categories &middot; ' + str(n) + ' Titles</span>')
    o.append('<h2>' + vname + '</h2><p class="vd">' + vdesc + '</p>')
    o.append('<a class="open" href="' + vfile + '">Open the volume</a>')
    o.append('<div class="dir">')
    for i, (cn, anchor, cc, note) in enumerate(cats, 1):
        o.append('<a href="' + vfile + '#' + anchor + '"><span class="n">' + ('%02d' % i) + '</span>')
        o.append('<span class="t">' + cn + '</span>')
        if note:
            o.append('<span class="note">' + note + '</span>')
        o.append('<span class="c">' + str(cc) + '</span></a>')
    o.append('</div></div>')

o.append('<div class="block alt" style="margin-top:56px"><div class="wrap">')
o.append('<span class="label">Built Past the Title Stage</span>')
o.append('<h2>Outlines and <em>Catalyst Kits</em></h2>')
o.append('<div class="kitcard"><h3>Outline Volume One</h3>')
o.append('<p>40 complete sermon outlines &mdash; all 20 Resurrection Sunday titles and all 20 Christmas Eve titles. Text, big idea, movements, illustration slot, the turn, the close, and a bulletin line for each.</p>')
o.append('<a class="open" href="' + OUT1 + '">Open the outlines</a></div>')
o.append('<div class="kitcard"><h3>The Catalyst Kit &mdash; Volume Three</h3>')
o.append('<p>Four complete kits. Each one takes a single Sunday and extends it into a seven-day devotional and a small group session with next steps for the person, the family, and the group. The forty-day campaign architecture compressed into one week.</p>')
o.append('<a class="open" href="' + V3 + '">Open the kits</a></div>')
o.append('</div></div>')

o.append('<div class="block"><div class="wrap"><span class="label">Proposed</span>')
o.append('<h2>Ten more categories <em>worth building</em></h2>')
o.append('<p>None of these exist yet. They are listed in the order I would build them.</p>')
for i, (pn, pd) in enumerate(PROPOSED, 1):
    o.append('<div class="prop"><div class="pn">' + ('%02d' % i) + '</div><div class="pb">')
    o.append('<h4>' + pn + '</h4><p>' + pd + '</p></div></div>')
o.append('<div class="flag"><span class="label">Not a category &mdash; a product</span>')
o.append('<p>The custom devotional built from a pastor\'s own sermon archive does not belong on the list above, because it is not a Sunday. It is a service. A church hands over ten years of Easter messages and receives a thirty-day devotional in their own pastor\'s voice, drawn from what he already preached.</p>')
o.append('<p>That is the same engine as the backlist digitization strategy, pointed at a smaller and much easier first sale. Thirty Days to Easter and Thirty Days to Christmas are the two obvious first editions, and a church that buys one will buy the other every year without being asked.</p>')
o.append('</div></div></div>')

o.append('<div class="closing"><div class="wrap"><p class="q">A church does not launch a program on Easter morning. It releases a movement, and then spends the rest of the year proving it meant it.</p>')
o.append('<div class="attr">Brett Eastman &middot; LifeTogether</div></div></div>')
o.append('<footer><div class="wrap">LifeTogether Ministries &middot; Catalytic Sundays &middot; Master Directory &middot; 39 Categories &middot; ' + str(TOTAL_ALL) + ' Titles</div></footer>')
o.append('</body></html>')

html = "\n".join(o)
with io.open('/mnt/user-data/outputs/catalytic-sundays-INDEX.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("INDEX built. total titles:", TOTAL_ALL, "bytes:", len(html))
