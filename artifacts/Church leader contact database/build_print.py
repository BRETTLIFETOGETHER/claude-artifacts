#!/usr/bin/env python3
"""Build print PDFs of the three Legacy Library documents.
Ivory ground (palette token), navy full-bleed covers, real Playfair/Cormorant,
grids flattened to blocks, interactivity replaced with print equivalents."""
import re
from bs4 import BeautifulSoup
from weasyprint import HTML
from pypdf import PdfReader

SRC = "/mnt/user-data/outputs/"
F = "/home/claude/fonts/"

FONTS = """
@font-face{font-family:'Playfair Display';src:url('%(f)sPlayfairDisplay-VF.ttf');font-weight:100 900;font-style:normal;}
@font-face{font-family:'Playfair Display';src:url('%(f)sPlayfairDisplay-Italic-VF.ttf');font-weight:100 900;font-style:italic;}
@font-face{font-family:'Cormorant Garamond';src:url('%(f)sCormorantGaramond-VF.ttf');font-weight:100 900;font-style:normal;}
@font-face{font-family:'Cormorant Garamond';src:url('%(f)sCormorantGaramond-Italic-VF.ttf');font-weight:100 900;font-style:italic;}
""" % {"f": F}

BASE = FONTS + """
@page{size:letter;margin:0.8in 0.85in 0.95in;background:#f4efe3;
  @bottom-left{content:"%(footleft)s";font-family:'Cormorant Garamond';font-style:italic;font-size:8.5pt;color:#5f6a7c;}
  @bottom-right{content:counter(page);font-family:'Playfair Display';font-size:9pt;color:#0b1726;}}
@page cover{margin:0;background:#0b1726;@bottom-left{content:none}@bottom-right{content:none}}
*{margin:0;padding:0;box-sizing:border-box;}
body{background:#f4efe3;color:#0b1726;font-family:'Cormorant Garamond',serif;font-size:10.5pt;line-height:1.55;}
.wrap{max-width:none;margin:0;padding:0;}
a{color:#0b1726;text-decoration:none;border-bottom:none;}
.cover{page:cover;width:8.5in;height:11in;padding:1.35in 1.15in;color:#ece7d8;page-break-after:always;position:relative;}
.cover .eyebrow{color:#c9a35c;}
.cover h1{font-family:'Playfair Display';font-weight:700;font-size:34pt;line-height:1.1;color:#ece7d8;margin:20pt 0 14pt;max-width:5.6in;}
.cover h1 em{font-style:italic;font-weight:400;color:#e3c186;}
.cover .rule{width:1.1in;height:2px;background:#c9a35c;margin:0 0 18pt;}
.cover .sub{font-size:13pt;color:#ece7d8;max-width:5.4in;line-height:1.5;}
.cover .date{position:absolute;bottom:1.15in;left:1.15in;font-size:9.5pt;color:#8b94a5;letter-spacing:.08em;}
.eyebrow{font-family:'Playfair Display';font-size:7.5pt;font-weight:700;letter-spacing:.3em;text-transform:uppercase;color:#c9a35c;}
h1{font-family:'Playfair Display';font-weight:700;font-size:20pt;line-height:1.15;margin:8pt 0 8pt;color:#0b1726;}
h1 em{font-style:italic;font-weight:400;color:#a07f45;}
h2{font-family:'Playfair Display';font-weight:600;font-size:14pt;margin-bottom:5pt;color:#0b1726;page-break-after:avoid;}
h3{font-family:'Playfair Display';font-weight:600;font-size:10.5pt;color:#0b1726;margin-bottom:3pt;page-break-after:avoid;}
.sub,.small,.note,.place,.who,.why,.contact{color:#5f6a7c;}
.sechead{font-family:'Playfair Display';font-size:8.5pt;font-weight:700;letter-spacing:.26em;text-transform:uppercase;color:#a07f45;padding:16pt 0 6pt;border-bottom:1.5px solid #c9a35c;margin-bottom:10pt;page-break-after:avoid;}
section{padding:0;}
.card{background:transparent;border:none;border-radius:0;border-top:1px solid rgba(160,127,69,.5);border-left:2px solid #c9a35c;padding:9pt 0 10pt 12pt;margin-top:10pt;page-break-inside:avoid;}
.printlab{font-family:'Playfair Display';font-size:8pt;font-weight:700;letter-spacing:.2em;text-transform:uppercase;color:#a07f45;margin:12pt 0 4pt;page-break-after:avoid;}
table{width:100%;border-collapse:collapse;font-size:9pt;}
th{font-family:'Playfair Display';font-size:7.5pt;font-weight:700;letter-spacing:.14em;text-transform:uppercase;color:#a07f45;text-align:left;padding:5pt 4pt;border-bottom:1.5px solid #c9a35c;}
td{padding:5pt 4pt;border-bottom:0.75px solid rgba(95,106,124,.35);vertical-align:top;}
footer{padding-top:14pt;color:#5f6a7c;font-size:8.5pt;border-top:1.5px solid #c9a35c;margin-top:16pt;}
"""

OFFER_CSS = BASE + """
.hero{padding:0;}
.hero p.lead{font-size:11.5pt;max-width:6.2in;margin-bottom:7pt;}
.hero p.small{font-size:10pt;color:#5f6a7c;max-width:6.2in;}
.seven,.doors,.tiers,.evi .grid{display:block;}
.seven .card,.doors .card{margin-top:8pt;}
.seven .n,.door .tag{font-family:'Playfair Display';font-size:7pt;font-weight:700;letter-spacing:.16em;text-transform:uppercase;color:#a07f45;}
.seven p,.door p{font-size:9.5pt;color:#5f6a7c;margin-top:2pt;}
.boardcase p{font-size:10pt;margin-bottom:6pt;}
.boardcase p strong{color:#0b1726;font-weight:600;}
.quiz{margin-top:8pt;}
.q{display:block;border:none;border-bottom:0.75px solid rgba(95,106,124,.35);padding:6pt 0;page-break-inside:avoid;}
.q p{font-size:10pt;display:inline;}
.cb{display:inline-block;width:10pt;height:10pt;border:1.25px solid #0b1726;vertical-align:-1.5pt;margin-right:8pt;}
.scorekey{border-top:1px solid rgba(160,127,69,.5);border-left:2px solid #c9a35c;padding:8pt 0 8pt 12pt;margin-top:10pt;page-break-inside:avoid;}
.scorekey p{font-size:10pt;margin-bottom:5pt;}
.scorekey b{font-family:'Playfair Display';font-size:9.5pt;color:#0b1726;}
.tier .from{font-family:'Playfair Display';font-size:7.5pt;color:#5f6a7c;text-transform:uppercase;letter-spacing:.18em;}
.tier .price{font-family:'Playfair Display';font-size:17pt;font-weight:700;color:#0b1726;margin:2pt 0;}
.tier ul{list-style:none;margin-top:6pt;}
.tier li{font-size:9.5pt;padding:3.5pt 0 3.5pt 14pt;border-bottom:0.75px solid rgba(95,106,124,.3);position:relative;}
.tier li:before{content:"";position:absolute;left:1pt;top:7.5pt;width:5pt;height:5pt;background:#c9a35c;}
.tier li:last-child{border-bottom:none;}
.tier .note{font-size:9pt;font-style:italic;margin-top:6pt;}
.tier.flag{border-left-width:3px;}
details{margin-top:6pt;border-top:0.75px solid rgba(160,127,69,.5);padding-top:5pt;}
summary{font-family:'Playfair Display';font-size:8pt;font-weight:600;letter-spacing:.12em;text-transform:uppercase;color:#a07f45;list-style:none;}
details td.v{text-align:right;white-space:nowrap;font-family:'Playfair Display';font-size:8pt;color:#0b1726;}
.mathline{margin-top:6pt;font-size:9.5pt;border:1px solid #c9a35c;padding:6pt 8pt;color:#0b1726;}
.door .price{font-family:'Playfair Display';font-size:12pt;font-weight:700;color:#0b1726;margin:2pt 0 3pt;}
.evi{border-top:1.5px solid #c9a35c;border-bottom:1.5px solid #c9a35c;padding:12pt 0;margin-top:14pt;}
.evi p.intro{font-size:10.5pt;max-width:6.2in;margin-bottom:8pt;}
.evi .item{border-left:2px solid #c9a35c;padding:2pt 0 2pt 10pt;margin-bottom:8pt;page-break-inside:avoid;}
.evi .item b{display:block;font-family:'Playfair Display';font-size:10pt;font-weight:600;color:#0b1726;margin-bottom:2pt;}
.evi .item p{font-size:9.5pt;color:#5f6a7c;}
.why p{font-size:10.5pt;max-width:6.4in;margin-bottom:7pt;}
.cta .card{text-align:left;border-left:3px solid #c9a35c;}
.cta p{max-width:6.2in;margin:4pt 0 0;font-size:10.5pt;color:#5f6a7c;}
.contact{margin-top:8pt;font-size:9.5pt;}
"""

KIT_CSS = BASE + """
header{padding:0;}
header p{max-width:6.4in;color:#5f6a7c;font-size:10.5pt;}
h1{font-size:22pt;}
.rules p{font-size:10pt;margin-bottom:6pt;}
.rules b{color:#0b1726;font-weight:600;}
.mail{border-left-width:3px;}
.mail .meta{font-family:'Playfair Display';font-size:7.5pt;color:#a07f45;text-transform:uppercase;letter-spacing:.18em;font-weight:700;margin-bottom:2pt;}
.subjects{border:1px solid rgba(160,127,69,.55);padding:6pt 9pt;margin:7pt 0;font-size:9.5pt;}
.subjects b{font-family:'Playfair Display';color:#a07f45;display:block;margin-bottom:2pt;font-size:7pt;text-transform:uppercase;letter-spacing:.14em;}
.body-block{border:0.75px solid rgba(95,106,124,.4);border-left:2px solid #c9a35c;padding:9pt 11pt;margin-top:6pt;font-size:9.8pt;background:transparent;page-break-inside:avoid;}
.body-block p{margin-bottom:6pt;}
.body-block p:last-child{margin-bottom:0;}
.variant{font-family:'Playfair Display';font-size:7pt;font-weight:700;letter-spacing:.16em;text-transform:uppercase;color:#a07f45;display:block;margin:8pt 0 2pt;}
.note{font-size:9pt;font-style:italic;margin-top:6pt;}
.flagbox{border:1px solid #a07f45;padding:6pt 9pt;font-size:9.5pt;color:#0b1726;margin-top:8pt;page-break-inside:avoid;}
td.r{font-family:'Playfair Display';font-size:8pt;font-weight:600;color:#0b1726;white-space:nowrap;}
td .why{display:block;font-size:8.5pt;color:#5f6a7c;margin-top:1pt;font-style:italic;}
.legend{font-size:9.5pt;color:#5f6a7c;margin-top:8pt;}
.legend b{color:#0b1726;}
.legend code{border:0.75px solid rgba(160,127,69,.55);padding:0 3pt;font-size:8pt;color:#0b1726;font-family:'Playfair Display';}
"""

DIR_CSS = BASE + """
header.m{padding:0;border-bottom:none;}
.stand{font-size:11pt;max-width:6.4in;}
.date{margin-top:8pt;font-size:9pt;color:#5f6a7c;letter-spacing:.04em;}
.census{display:flex;border-top:1.5px solid #c9a35c;border-bottom:1.5px solid #c9a35c;margin-top:10pt;page-break-inside:avoid;}
.census div{flex:1 1 25%;padding:8pt 8pt;border-right:0.75px solid rgba(160,127,69,.4);}
.census div:last-child{border-right:none;}
.census .n{font-family:'Playfair Display';font-size:16pt;color:#0b1726;display:block;line-height:1;}
.census .l{font-size:7.5pt;letter-spacing:.1em;text-transform:uppercase;color:#5f6a7c;margin-top:3pt;display:block;}
.secintro{padding:4pt 0;font-size:10pt;max-width:6.4in;color:#5f6a7c;}
article.e{padding:10pt 0 10pt 12pt;border-top:1px solid rgba(160,127,69,.5);border-left:2px solid #c9a35c;margin-top:10pt;page-break-inside:avoid;}
.etop{display:block;}
.num{font-family:'Playfair Display';font-size:8pt;color:#a07f45;letter-spacing:.1em;}
h2{font-size:14pt;margin:3pt 0 1pt;}
.who{font-size:9.5pt;margin-bottom:2pt;}
.who b{color:#0b1726;font-weight:600;}
.place{font-size:8pt;letter-spacing:.1em;text-transform:uppercase;margin-bottom:6pt;}
.lbl{font-family:'Playfair Display';font-size:7pt;font-weight:700;letter-spacing:.2em;text-transform:uppercase;color:#a07f45;margin:8pt 0 3pt;page-break-after:avoid;}
.rank{font-size:9.5pt;font-style:italic;padding-left:8pt;border-left:1.5px solid rgba(160,127,69,.6);margin-bottom:3pt;}
table.lk td{padding:3.5pt 2pt;font-size:8.8pt;}
table.lk td.k{width:40%;font-size:7.5pt;letter-spacing:.1em;text-transform:uppercase;color:#5f6a7c;padding-right:8pt;}
.bench{padding:8pt 0 2pt;}
.bench h3{font-size:11pt;margin:8pt 0 2pt;}
.bench p{font-size:9.5pt;color:#5f6a7c;max-width:6.4in;}
.meth p{margin:7pt 0;font-size:10.5pt;max-width:6.5in;}
.meth p b{font-family:'Playfair Display';font-size:10pt;color:#0b1726;}
table.roster{margin:8pt 0;}
table.roster td{font-size:8.8pt;padding:4pt 4pt;}
td.att{font-family:'Playfair Display';font-size:8pt;color:#0b1726;white-space:nowrap;}
td.st{font-size:7pt;letter-spacing:.08em;text-transform:uppercase;color:#5f6a7c;white-space:nowrap;}
td.st.p{color:#a07f45;font-weight:700;}
.contact{color:#5f6a7c;font-size:8.5pt;font-style:italic;}
article.e{page-break-inside:auto;}
article.e .lbl, article.e .rank, article.e table.lk{page-break-inside:avoid;}
"""

def cover_html(eyebrow, title, sub, date):
    return ('<div class="cover"><span class="eyebrow">' + eyebrow + '</span>'
            '<h1>' + title + '</h1><div class="rule"></div>'
            '<p class="sub">' + sub + '</p>'
            '<div class="date">' + date + '</div></div>')

def strip_scripts_links(soup):
    for t in soup.find_all('script'): t.decompose()
    for t in soup.find_all('link'): t.decompose()

def build(fname, css, cover, out, transforms):
    soup = BeautifulSoup(open(SRC + fname).read(), 'html.parser')
    strip_scripts_links(soup)
    style = soup.find('style'); style.string = css
    transforms(soup)
    body = soup.find('body')
    body.insert(0, BeautifulSoup(cover, 'html.parser'))
    html = str(soup)
    open('/home/claude/print-' + fname, 'w').write(html)
    HTML(string=html, base_url='/home/claude/').write_pdf(SRC + out)
    r = PdfReader(SRC + out)
    n = len(r.pages)
    shorts = []
    for i, p in enumerate(r.pages):
        t = p.extract_text() or ''
        if i > 0 and i < n - 1 and len(t) < 500:
            shorts.append((i + 1, len(t)))
    print(out, '| pages:', n, '| short interior pages:', shorts if shorts else 'none')

# ---------- OFFER ----------
def t_offer(soup):
    # remove hero + CTA button rows; keep contact
    for d in soup.select('.btnrow'): d.decompose()
    # remove segmentation buttons; show all audience blocks with labels
    for d in soup.select('.seg'): d.decompose()
    labels = {'aud-pastor': 'For the Senior Pastor &mdash; the seven things this preserves',
              'aud-board': 'For the Elder Board and Executive Pastor',
              'aud-funder': 'For the Legacy Funder'}
    for aid, lab in labels.items():
        blk = soup.find(id=aid)
        if blk:
            blk['class'] = ['aud', 'show']
            blk['style'] = 'display:block'
            tag = soup.new_tag('div'); tag['class'] = 'printlab'
            tag.append(BeautifulSoup(lab, 'html.parser')); blk.insert_before(tag)
    sh = soup.find('div', class_='sechead')
    if sh and 'Who' in sh.get_text(): sh.string = 'The Case, Seat by Seat'
    # quiz: buttons -> checkboxes; intro reword; score button + result -> printed key
    for q in soup.select('.q'):
        b = q.find('button')
        if b:
            cb = soup.new_tag('span'); cb['class'] = 'cb'
            p = q.find('p'); p.insert(0, cb); b.decompose()
    sub = soup.select('#ready .sub')
    if sub: sub[0].string = "Six honest questions. Check what's true, then read the key below."
    for b in soup.find_all('button', class_='btn'): b.decompose()
    res = soup.find(id='result')
    key = ('<div class="scorekey"><p><b>Zero to two checks:</b> start with a conversation. The library may still be forming, '
           'or the season may not be right yet &mdash; and if the honest answer is wait, we will say so.</p>'
           '<p><b>Three or four:</b> start with the Audit. Map exactly what exists, rank the top ten series, '
           'take the roadmap &mdash; with the fee credited toward anything built next.</p>'
           '<p><b>Five or six:</b> the full Architecture will not be too big for what you have. Begin with the Audit '
           'as the on-ramp, but plan the conversation at the Architecture or Full System level.</p></div>')
    if res: res.replace_with(BeautifulSoup(key, 'html.parser'))
    # open the line-item details
    for d in soup.find_all('details'):
        d['open'] = ''
        s = d.find('summary')
        if s: s.string = 'The line-item breakdown'
    # mailto -> plain
    for a in soup.find_all('a', href=True):
        if a['href'].startswith('mailto'): a.replace_with(a.get_text())
        elif a['href'].startswith('#'): a.replace_with(a.get_text())

build('legacy-library-offer.html', OFFER_CSS,
      cover_html('LifeTogether &middot; The Senior Pastor Legacy Library',
                 'Your Life Message Deserves More Than a <em>Retirement Party.</em>',
                 'A complete engagement for senior pastors with fifteen or more years of ministry: capture, organize, publish, and multiply the library you have already built. Three tiers, six doors in, one roadmap.',
                 'Print edition &middot; August 2026 &middot; LifeTogether Ministries'),
      'legacy-library-offer.pdf', t_offer)

# ---------- KIT ----------
def t_kit(soup):
    for b in soup.select('.copybtn'): b.decompose()
    for a in soup.find_all('a', href=True):
        a.replace_with(a.get_text())

build('legacy-library-outreach-kit.html', KIT_CSS,
      cover_html('LifeTogether &middot; The Legacy Library &middot; Internal',
                 'The Outreach <em>Kit</em>',
                 'Three emails, merge-ready &mdash; the opening ask, the gatekeeper&rsquo;s version, and the webinar invitation &mdash; with the provenance rules and the record-by-record routing for the live list. Internal working document; the emails travel, this page does not.',
                 'Draft v1 &middot; August 2026 &middot; Not pastor-facing'),
      'legacy-library-outreach-kit.pdf', t_kit)

# ---------- DIRECTORY ----------
def t_dir(soup):
    # strip back-to-index links
    for a in soup.find_all('a', class_='up'):
        par = a.find_parent('p')
        (par or a).decompose()
    # companion-doc line instead of relative link
    for a in soup.find_all('a', href=True):
        if a['href'] == 'legacy-library-offer.html':
            a.replace_with('the companion document, The Legacy Library Offer')
        elif a['href'].startswith('#'):
            a.replace_with(a.get_text())
        else:
            a.replace_with(a.get_text())  # URLs already shown as text
    # thead so roster headers repeat across pages
    for tbl in soup.find_all('table', class_='roster'):
        first = tbl.find('tr')
        if first and first.find('th'):
            th = soup.new_tag('thead'); first.wrap(th)

build('legacy-library-directory.html', DIR_CSS,
      cover_html('LifeTogether &middot; Ministry Intelligence &middot; Field Research &middot; Volume II',
                 'The Legacy Library <em>Directory</em>',
                 'The megachurch cut of the master file &mdash; 101 records, 94 distinct churches, filed at 7,100 to 11,867 in weekend attendance. Nine productized libraries profiled with live sources; every church accounted for.',
                 'Compiled August 26, 2026 &middot; Printed edition'),
      'legacy-library-directory.pdf', t_dir)

print('done')
