# -*- coding: utf-8 -*-
import io
from master_content import DRAFTS
from kits import KITS
from loop_content import FAMILY

K = KITS[0]  # He's Not Where You Left Him
FAM = FAMILY["He's Not Where You Left Him"]

CSS = """
@page{size:5.5in 8.5in;margin:0}
:root{--ink:#1a1a1a;--soft:#5a5550;--rule:#d8d2c6;--accent:#8a6d3b;--paper:#fdfbf6}
*{box-sizing:border-box}
body{margin:0;background:#3a3a3a;font-family:'Cormorant Garamond',Georgia,serif;color:var(--ink)}
.page{width:5.5in;height:8.5in;background:var(--paper);margin:0 auto 14px;padding:0.62in 0.58in;
position:relative;overflow:hidden;box-shadow:0 2px 14px rgba(0,0,0,.4)}
.pn{position:absolute;bottom:0.34in;left:0;right:0;text-align:center;
font-family:'Lato',sans-serif;font-size:7.5pt;letter-spacing:.14em;color:#a09a90}
h1,h2,h3{font-family:'Playfair Display',Georgia,serif;font-weight:600;margin:0;line-height:1.14}
.fld{background:#f2ead8;border-bottom:1px solid var(--accent);padding:0 3px}
.cov{display:flex;flex-direction:column;justify-content:center;text-align:center;height:100%}
.cov .ch{font-family:'Lato',sans-serif;font-size:8pt;letter-spacing:.3em;text-transform:uppercase;
color:var(--accent);margin-bottom:0.5in}
.cov h1{font-size:31pt;line-height:1.08}
.cov .sub{font-family:'Cormorant Garamond',serif;font-style:italic;font-size:13pt;
color:var(--soft);margin-top:14px}
.cov .rule{width:44px;height:1px;background:var(--accent);margin:0.4in auto}
.cov .days{font-family:'Lato',sans-serif;font-size:8pt;letter-spacing:.24em;
text-transform:uppercase;color:var(--soft)}
h2.ph{font-size:19pt;margin-bottom:4px}
.eyebrow{font-family:'Lato',sans-serif;font-size:7.5pt;letter-spacing:.22em;
text-transform:uppercase;color:var(--accent);margin-bottom:9px}
p{font-size:10.5pt;line-height:1.62;margin:0 0 10px;color:var(--ink)}
p.small{font-size:9.5pt;color:var(--soft)}
.hr{height:1px;background:var(--rule);margin:16px 0}
.sig{margin-top:20px}
.sigline{border-bottom:1px solid var(--ink);height:26px;margin-bottom:5px}
.siglbl{font-family:'Lato',sans-serif;font-size:7.5pt;letter-spacing:.14em;
text-transform:uppercase;color:var(--soft);margin-bottom:16px}
.grid{display:flex;flex-wrap:wrap;gap:7px;margin-top:14px}
.box{width:0.62in;height:0.62in;border:1px solid var(--rule);display:flex;
align-items:center;justify-content:center;font-family:'Lato',sans-serif;font-size:8pt;color:#b5aea3}
.dayhead{border-bottom:1px solid var(--rule);padding-bottom:9px;margin-bottom:13px}
.dayhead .dn{font-family:'Lato',sans-serif;font-size:7.5pt;letter-spacing:.22em;
text-transform:uppercase;color:var(--accent)}
.dayhead h3{font-size:17pt;margin-top:4px}
.dayhead .ref{font-family:'Lato',sans-serif;font-size:8pt;color:var(--soft);margin-top:4px;letter-spacing:.04em}
.q{font-family:'Playfair Display',serif;font-size:12pt;font-style:italic;
color:var(--accent);margin-bottom:12px;line-height:1.35}
.lines .ln{border-bottom:1px solid var(--rule);height:0.31in}
.do{border:1px solid var(--accent);padding:11px 13px;margin-top:16px;display:flex;gap:11px;align-items:flex-start}
.do .cb{width:15px;height:15px;border:1.5px solid var(--accent);flex-shrink:0;margin-top:2px}
.do .dl{font-family:'Lato',sans-serif;font-size:7pt;letter-spacing:.2em;text-transform:uppercase;
color:var(--accent);display:block;margin-bottom:4px}
.do .dt{font-size:10pt;line-height:1.5}
.fam{margin-top:15px;border-top:1px dashed var(--rule);padding-top:11px}
.fam .fl{font-family:'Lato',sans-serif;font-size:7pt;letter-spacing:.2em;
text-transform:uppercase;color:var(--soft);margin-bottom:5px}
.fam p{font-size:9.5pt;margin-bottom:5px}
.notes .ln{border-bottom:1px solid var(--rule);height:0.34in}
.back{display:flex;flex-direction:column;justify-content:center;height:100%;text-align:center}
.back h2{font-size:21pt;margin-bottom:12px}
.qr{width:1.5in;height:1.5in;border:1px dashed var(--accent);margin:0.28in auto;
display:flex;align-items:center;justify-content:center;font-family:'Lato',sans-serif;
font-size:7.5pt;letter-spacing:.12em;color:var(--accent);text-align:center;padding:10px;line-height:1.5}
.bar{background:#1c2a4a;color:#f7f3ea;padding:16px 22px;font-family:'Lato',sans-serif;
font-size:10pt;letter-spacing:.06em;max-width:5.5in;margin:0 auto 14px;line-height:1.6}
.bar b{color:#d9bc82;letter-spacing:.16em;text-transform:uppercase;font-size:8.5pt;
display:block;margin-bottom:5px}
@media print{
body{background:#fff}
.page{box-shadow:none;margin:0;page-break-after:always;break-after:page}
.bar{display:none}
}
"""

o = []
o.append('<!DOCTYPE html><html lang="en"><head><meta charset="utf-8">')
o.append('<meta name="viewport" content="width=device-width, initial-scale=1">')
o.append('<title>Seven-Day Journal &mdash; Brandable Template | LifeTogether</title>')
o.append('<link rel="preconnect" href="https://fonts.googleapis.com">')
o.append('<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>')
o.append('<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,500;0,600;1,500&family=Cormorant+Garamond:ital,wght@0,400;0,600;1,400&family=Lato:wght@400;700&display=swap" rel="stylesheet">')
o.append('<style>' + CSS + '</style></head><body>')

o.append('<div class="bar"><b>How to use this template</b>')
o.append('Twenty pages, 5.5 x 8.5 inches, laid out for saddle-stitch on letter paper folded in half. '
         'Every shaded field is yours to replace. Print to PDF at actual size, hand it to any local printer, '
         'and ask for 70lb uncoated text with a 100lb cover. This bar does not print.</div>')

def page(inner, num=None):
    o.append('<div class="page">' + inner + ('<div class="pn">' + str(num) + '</div>' if num else '') + '</div>')

# COVER
page('<div class="cov"><div class="ch"><span class="fld">[ YOUR CHURCH NAME ]</span></div>'
     '<h1>' + K["t"] + '</h1>'
     '<div class="sub">' + K["s"] + '</div>'
     '<div class="rule"></div>'
     '<div class="days">A Seven-Day Journey</div></div>')

# p2 welcome
page('<div class="eyebrow">Before you begin</div><h2 class="ph">A word from your pastor</h2>'
     '<div class="hr"></div>'
     '<p><span class="fld">[ REPLACE THIS PAGE. One hundred words, first person, written by the pastor. '
     'Say why you chose this passage for this church in this season. Do not make it good. Make it yours. '
     'This is the single highest-leverage page in the booklet and it takes about ten minutes to write. ]</span></p>'
     '<p class="small">Seven days. Ten minutes each. Read the page, answer the one question, do the one thing. '
     'If you miss a day, do not go back and catch up &mdash; just pick up where the calendar is. '
     'Nobody has ever finished one of these by making up lost days.</p>', 2)

# p3 commitment
page('<div class="eyebrow">Page three</div><h2 class="ph">I\'m in.</h2><div class="hr"></div>'
     '<p>Sign this in the service, with a pen, while everyone else is signing theirs. '
     'Then write down one person who will ask you about it on Wednesday.</p>'
     '<div class="sig"><div class="sigline"></div><div class="siglbl">Name</div>'
     '<div class="sigline"></div><div class="siglbl">Date I start</div>'
     '<div class="sigline"></div><div class="siglbl">My spiritual partner &mdash; the person walking this with me</div></div>'
     '<p class="small">Scan the code on the back page to enroll and send your partner their own copy.</p>', 3)

# p4 tracker
page('<div class="eyebrow">Page four</div><h2 class="ph">Seven days</h2><div class="hr"></div>'
     '<p>Check the box each morning. That is the whole system.</p>'
     '<div class="grid">' + "".join('<div class="box">' + str(i) + '</div>' for i in range(1, 8)) + '</div>'
     '<div class="hr"></div>'
     '<p class="small">Day four is where most people stop. That is not a character problem, it is simply '
     'where the novelty runs out and the habit has not formed yet. If you get past day four you will '
     'almost certainly finish.</p>', 4)

# 7 day spreads
pg = 5
for i, (dt, ref, rd, q, act) in enumerate(K["dev"], 1):
    left = ('<div class="dayhead"><div class="dn">Day ' + str(i) + '</div><h3>' + dt + '</h3>'
            '<div class="ref">' + ref + ' &middot; NIV</div></div>')
    for para in rd.split("\n\n"):
        left += '<p>' + para + '</p>'
    page(left, pg); pg += 1
    right = ('<div class="eyebrow">Day ' + str(i) + ' &mdash; respond</div>'
             '<div class="q">' + q + '</div><div class="lines">' + ('<div class="ln"></div>' * 7) + '</div>'
             '<div class="do"><div class="cb"></div><div><span class="dl">Do this today</span>'
             '<span class="dt">' + act + '</span></div></div>'
             '<div class="fam"><div class="fl">At the table tonight &mdash; optional</div>'
             '<p><strong>Ask:</strong> ' + FAM[i-1][0] + '</p>'
             '<p><strong>Say:</strong> ' + FAM[i-1][1] + '</p>'
             '<p><strong>Do:</strong> ' + FAM[i-1][2] + '</p></div>')
    page(right, pg); pg += 1

# notes
page('<div class="eyebrow">Page ' + str(pg) + '</div><h2 class="ph">Notes</h2><div class="hr"></div>'
     '<div class="notes">' + ('<div class="ln"></div>' * 17) + '</div>', pg); pg += 1
page('<div class="notes" style="padding-top:0.1in">' + ('<div class="ln"></div>' * 19) + '</div>', pg); pg += 1

# back
page('<div class="back"><div class="eyebrow">You finished</div>'
     '<h2>Do not stop here.</h2>'
     '<p class="small">Seven days changed something small. Six weeks in a room with five other people '
     'changes something that stays changed.</p>'
     '<div class="qr">[ QR CODE ]<br>Enroll, invite<br>your partner,<br>join a group</div>'
     '<p class="small"><span class="fld">[ CELEBRATION SUNDAY &mdash; DATE ]</span><br>'
     'Come ready to tell us what happened.</p>'
     '<div class="hr"></div>'
     '<p class="small"><span class="fld">[ CHURCH NAME ]</span><br>'
     '<span class="fld">[ address &middot; website ]</span></p></div>')

o.append('</body></html>')

html = "\n".join(o)
with io.open('/mnt/user-data/outputs/catalytic-journal-template.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("pages:", html.count('class="page"'), "bytes:", len(html))
