# -*- coding: utf-8 -*-
import re, unicodedata
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor
from reportlab.lib.enums import TA_LEFT, TA_CENTER
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (BaseDocTemplate, PageTemplate, Frame, Paragraph,
                                Spacer, Table, TableStyle, NextPageTemplate,
                                PageBreak, Flowable, KeepTogether)
from reportlab.lib.styles import ParagraphStyle
import oceans_data as D

# ---- brand tokens (Brett's site) ----
INK    = HexColor('#080e16'); NAVY = HexColor('#0b1726'); PANEL = HexColor('#132439')
GOLD   = HexColor('#c9a35c'); GOLDB = HexColor('#e3c186'); CREAM = HexColor('#ece7d8')
MUTED  = HexColor('#8b94a5'); PAPER = HexColor('#fdfcf9'); RULE  = HexColor('#d8d2c2')

# ---- fonts (variable TTFs register at default instance; fall back to core) ----
def reg(name, path, fb):
    try:
        pdfmetrics.registerFont(TTFont(name, path)); return name
    except Exception:
        return fb
DISPLAY = reg('Playfair', 'PlayfairDisplay.ttf', 'Times-Bold')
DISPI   = reg('PlayfairI', 'PlayfairDisplayItalic.ttf', 'Times-Italic')
BODY    = reg('Cormorant', 'CormorantGaramond.ttf', 'Times-Roman')
LABEL   = reg('Archivo', 'Archivo.ttf', 'Helvetica')

def S(t):  # sanitize to glyph-safe text
    t = t.replace('\u2019', "'").replace('\u2018', "'").replace('\u201c', '"').replace('\u201d', '"')
    t = t.replace('\u2013', '-').replace('\u2014', '-').replace('\u2026', '...').replace('\u2022', '-')
    t = ''.join(c for c in t if 31 < ord(c) < 0x2500 and unicodedata.category(c)[0] != 'C')
    return re.sub(r'\s+', ' ', t).strip()

def esc(t):
    return S(t).replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')

# ---- styles ----
def st(name, **kw):
    base = dict(fontName=BODY, fontSize=10.5, leading=14.5, textColor=INK, alignment=TA_LEFT)
    base.update(kw); return ParagraphStyle(name, **base)

sEyeC  = st('eyeC', fontName=LABEL, fontSize=8.5, leading=12, textColor=GOLD, alignment=TA_CENTER)
sTitC  = st('titC', fontName=DISPLAY, fontSize=40, leading=46, textColor=CREAM, alignment=TA_CENTER)
sSubC  = st('subC', fontName=DISPI, fontSize=15, leading=20, textColor=GOLDB, alignment=TA_CENTER)
sMetaC = st('metaC', fontName=LABEL, fontSize=8.5, leading=15, textColor=MUTED, alignment=TA_CENTER)
sCredC = st('credC', fontName=BODY, fontSize=11, leading=15, textColor=CREAM, alignment=TA_CENTER)

sEye   = st('eye', fontName=LABEL, fontSize=8, leading=11, textColor=GOLD)
sH1    = st('h1', fontName=DISPLAY, fontSize=21, leading=25, textColor=NAVY, spaceAfter=4)
sH2    = st('h2', fontName=DISPLAY, fontSize=13.5, leading=17, textColor=NAVY, spaceBefore=10, spaceAfter=3)
sBody  = st('body', spaceAfter=6)
sLede  = st('lede', fontName=DISPI, fontSize=12.5, leading=17, textColor=PANEL, spaceAfter=8)
sEntry = st('entry', fontSize=9.6, leading=12.6, spaceAfter=3.2)
sItem  = st('item', fontSize=8.7, leading=11.2, spaceAfter=1.4)
sNote  = st('note', fontName=LABEL, fontSize=7.6, leading=10.5, textColor=MUTED, spaceAfter=4)
sTblH  = st('tblh', fontName=LABEL, fontSize=7.8, leading=10, textColor=CREAM)
sTbl   = st('tbl', fontSize=9.6, leading=12)

class Bkmk(Flowable):
    _n = 0
    def __init__(self, title, level=0):
        Flowable.__init__(self); self.t = title; self.lv = level
        Bkmk._n += 1; self.key = 'bk%d' % Bkmk._n
    def wrap(self, w, h): return (0, 0)
    def draw(self):
        c = self.canv; c.bookmarkPage(self.key)
        c.addOutlineEntry(S(self.t), self.key, self.lv, False)

class GoldRule(Flowable):
    def __init__(self, w=None, th=1.1, col=GOLD, sb=2, sa=8):
        Flowable.__init__(self); self.w = w; self.th = th; self.col = col
        self.spaceBefore = sb; self.spaceAfter = sa
    def wrap(self, aw, ah): self._w = self.w or aw; return (self._w, self.th)
    def draw(self):
        self.canv.setStrokeColor(self.col); self.canv.setLineWidth(self.th)
        self.canv.line(0, 0, self._w, 0)

def eyebrow(txt):
    return [Paragraph('<font name="%s">%s</font>' % (LABEL, esc(txt.upper())), sEye), GoldRule(w=44, sb=3, sa=10)]

# ---- page painters ----
PW, PH = letter
def paint_cover(cv, doc):
    cv.saveState(); cv.setFillColor(NAVY); cv.rect(0, 0, PW, PH, stroke=0, fill=1)
    cv.setStrokeColor(GOLD); cv.setLineWidth(1.2)
    cv.line(0.9*inch, PH-0.9*inch, PW-0.9*inch, PH-0.9*inch)
    cv.line(0.9*inch, 0.9*inch, PW-0.9*inch, 0.9*inch)
    cv.setFillColor(GOLD)
    cv.setFont(LABEL, 8); cv.drawCentredString(PW/2, 0.7*inch, 'L I F E T O G E T H E R   M I N I S T R I E S')
    cv.restoreState()

def paint_body(cv, doc):
    cv.saveState()
    cv.setStrokeColor(GOLD); cv.setLineWidth(0.8)
    cv.line(0.85*inch, 0.72*inch, PW-0.85*inch, 0.72*inch)
    cv.setFont(LABEL, 7.2); cv.setFillColor(MUTED)
    cv.drawString(0.85*inch, 0.56*inch, 'THE OCEANS LIBRARY - PLATFORM CENSUS v1 - AUGUST 2026')
    cv.setFillColor(NAVY); cv.drawRightString(PW-0.85*inch, 0.56*inch, '%d' % doc.page)
    cv.setFont(LABEL, 7.2); cv.setFillColor(MUTED)
    cv.drawRightString(PW-0.85*inch, PH-0.62*inch, 'oceans.com')
    cv.restoreState()

M = 0.85*inch
frame1 = [Frame(M, 0.95*inch, PW-2*M, PH-0.95*inch-1.05*inch, id='f1')]
gap = 0.28*inch; colw = (PW-2*M-gap)/2
frame2 = [Frame(M, 0.95*inch, colw, PH-2.0*inch, id='c1'),
          Frame(M+colw+gap, 0.95*inch, colw, PH-2.0*inch, id='c2')]

doc = BaseDocTemplate('/home/claude/oceans/OCEANS-Complete-Library-Census.pdf',
                      pagesize=letter, title='The OCEANS Library - Platform Census',
                      author='LifeTogether Ministries',
                      leftMargin=M, rightMargin=M)
doc.addPageTemplates([
    PageTemplate(id='Cover', frames=[Frame(1.1*inch, 1.2*inch, PW-2.2*inch, PH-2.4*inch, id='cf')], onPage=paint_cover),
    PageTemplate(id='Body', frames=frame1, onPage=paint_body),
    PageTemplate(id='TwoCol', frames=frame2, onPage=paint_body),
])

# ---- computed stats ----
summit = [tuple(l.split('~', 1)) for l in D.SUMMIT_SERMONS.strip().split('\n')]
mclean = [tuple(l.split('~', 1)) for l in D.MCLEAN_SERMONS.strip().split('\n')]
assert len(summit) == 137 and len(mclean) == 80, (len(summit), len(mclean))
contribs = sorted(D.CONTRIBUTORS, key=lambda c: c[1].lower())
nC = len(contribs)
churches = [c for c in contribs if c[2] == 'C']
minis    = [c for c in contribs if c[2] == 'M']
shows    = [c for c in contribs if c[2] == 'S']
ser_eps  = sum(s[1] for s in D.SERIES)

story = []
# ================= COVER =================
story.append(Spacer(1, 1.5*inch))
story.append(Paragraph('L I F E T O G E T H E R   x   O C E A N S', sEyeC))
story.append(Spacer(1, 26))
story.append(Paragraph('The OCEANS Library', sTitC))
story.append(Spacer(1, 12))
story.append(Paragraph('A census of every contributor, sermon and podcast<br/>on the oceans.com platform', sSubC))
story.append(Spacer(1, 40))
t = Table([[Paragraph('<font color="#c9a35c">%d</font><br/><font size="7.5" color="#8b94a5">CONTRIBUTORS</font>' % nC, ParagraphStyle('k', fontName=DISPLAY, fontSize=24, leading=26, textColor=GOLD, alignment=TA_CENTER)),
            Paragraph('<font color="#c9a35c">4</font><br/><font size="7.5" color="#8b94a5">CONTENT TYPES</font>', ParagraphStyle('k2', fontName=DISPLAY, fontSize=24, leading=26, textColor=GOLD, alignment=TA_CENTER)),
            Paragraph('<font color="#c9a35c">217</font><br/><font size="7.5" color="#8b94a5">MESSAGES FULLY INDEXED</font>', ParagraphStyle('k3', fontName=DISPLAY, fontSize=24, leading=26, textColor=GOLD, alignment=TA_CENTER))]],
          colWidths=[(PW-2.2*inch)/3.0]*3)
t.setStyle(TableStyle([('VALIGN', (0,0), (-1,-1), 'TOP')]))
story.append(t)
story.append(Spacer(1, 46))
story.append(Paragraph('WORKING CENSUS - VERSION 1<br/>COMPILED FROM THE LIVE PUBLIC SITE - AUGUST 17, 2026<br/>PREPARED FOR THE LIFETOGETHER x OCEANS DIRECTORY CONVERSATION', sMetaC))
story.append(Spacer(1, 16))
story.append(Paragraph('Prepared by Brett Eastman - LifeTogether Ministries', sCredC))
story.append(NextPageTemplate('Body')); story.append(PageBreak())

# ================= ABOUT =================
story.append(Bkmk('About This Census'))
story += eyebrow('How to read this document')
story.append(Paragraph('About This Census', sH1))
story.append(Paragraph('One document, one question: what does OCEANS actually hold?', sLede))
story.append(Paragraph('OCEANS (oceans.com) is a streaming directory of sermons and faith podcasts drawn from '
    'contributing churches, ministries and shows. This census was compiled directly from the live public site on '
    'August 17, 2026. Everything in it is transcribed from what the platform itself displays; nothing is estimated '
    'or filled in from memory. Where a number could not be verified on the page, it is not stated.', sBody))
story.append(Paragraph('The platform organizes content into four types: full-length <b>Sermons</b> (which is also '
    'where podcast episodes live), <b>Shorts</b> (roughly 30-second to 3-minute clips), <b>Series</b> (sermons '
    'grouped into preaching series), and <b>Podcasts</b> (show-level feeds). This census counts full-length '
    'messages as the primary unit and reports shorts separately.', sBody))
story.append(Paragraph('Coverage in this version', sH2))
rows = [[Paragraph('<b>LAYER</b>', sTblH), Paragraph('<b>STATUS IN v1</b>', sTblH)],
    [Paragraph('Contributor roster - every church, ministry and show on the platform', sTbl), Paragraph('<b>Complete</b> (%d contributors)' % nC, sTbl)],
    [Paragraph('Platform architecture - content types, navigation, search model', sTbl), Paragraph('<b>Complete</b>', sTbl)],
    [Paragraph('Title-level libraries - The Summit Church and McLean Bible Church', sTbl), Paragraph('<b>Complete</b> (137 + 80 messages, Exhibits A-B)', sTbl)],
    [Paragraph('Series index', sTbl), Paragraph('Captured: 20 series / %d episodes (platform holds more)' % ser_eps, sTbl)],
    [Paragraph('Title-level libraries - remaining %d contributors' % (nC-2), sTbl), Paragraph('Pending: platform export or continued crawl (p. 12)', sTbl)]]
tb = Table(rows, colWidths=[3.9*inch, 2.9*inch])
tb.setStyle(TableStyle([('BACKGROUND', (0,0), (-1,0), NAVY), ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ('TOPPADDING', (0,0), (-1,-1), 5), ('BOTTOMPADDING', (0,0), (-1,-1), 5),
    ('LEFTPADDING', (0,0), (-1,-1), 7), ('LINEBELOW', (0,1), (-1,-1), 0.5, RULE)]))
story.append(tb)
story.append(Spacer(1, 8))
story.append(Paragraph('Why v1 stops where it does: the site renders each contributor page as a complete list, '
    'but there is no public master index across all %d libraries. Two contributor libraries are indexed here in '
    'full to establish the item-level layer; page 12 lays out the one-step path to 100 percent coverage.' % nC, sBody))
story.append(PageBreak())

# ================= PLATFORM AT A GLANCE =================
story.append(Bkmk('The Platform at a Glance'))
story += eyebrow('oceans.com')
story.append(Paragraph('The Platform at a Glance', sH1))
story.append(Paragraph('"Messages for whatever you\'re facing."', sLede))
story.append(Paragraph('OCEANS positions itself as felt-need retrieval, not channel browsing. The home page leads '
    'with a single question - <i>"What are you carrying today?"</i> - and this promise: <i>"%s"</i> '
    'Six felt-need doors sit under the search box: %s.' % (esc(D.PLATFORM['search_promise']),
    esc(', '.join(D.PLATFORM['felt_needs']))), sBody))
story.append(Paragraph('Structure', sH2))
story.append(Paragraph('Navigation: %s. Contributors join through a public speaker-intake funnel ("Join OCEANS"), '
    'which means the roster below is designed to grow.' % esc(' - '.join(D.PLATFORM['nav'])), sBody))
story.append(Paragraph('Scale evidence captured', sH2))
for e in D.SCALE_EVIDENCE:
    story.append(Paragraph('- ' + esc(e), sBody))
story.append(Paragraph('What an honest total looks like: with %d live contributors and anchor libraries running '
    '80-137 full-length messages, the platform plausibly holds a few thousand full-length messages plus shorts. '
    'That is a bounded working read, not a count; the precise total comes with the export on page 12.' % nC, sBody))
story.append(Paragraph('Top 10 this week (week of August 17, 2026)', sH2))
for i, x in enumerate(D.TOP10, 1):
    story.append(Paragraph('%d. %s' % (i, esc(x)), sEntry))
story.append(PageBreak())

# ================= CONTRIBUTOR DIRECTORY =================
story.append(Bkmk('The Contributor Directory'))
story += eyebrow('The census core - complete roster')
story.append(Paragraph('The Contributor Directory', sH1))
story.append(Paragraph('Every contributor live on oceans.com as of August 17, 2026: %d in all - %d churches, '
    '%d ministries and voices, %d podcasts and shows. Descriptions are the platform\'s own, condensed; '
    '"no profile posted" means the platform shows none.' % (nC, len(churches), len(minis), len(shows)), sBody))
story.append(NextPageTemplate('TwoCol')); story.append(PageBreak())

def entry(i, c):
    _id, name, typ, blurb = c
    tag = {'C': 'CHURCH', 'M': 'MINISTRY', 'S': 'SHOW'}[typ]
    b = esc(blurb) if blurb else '<i>No profile posted.</i>'
    return Paragraph('<font color="#c9a35c">%02d</font>&nbsp;&nbsp;<b>%s</b> '
                     '<font name="%s" size="6.3" color="#8b94a5">%s - ID %d</font><br/>%s'
                     % (i, esc(name), LABEL, tag, _id, b), sEntry)

for i, c in enumerate(contribs, 1):
    story.append(entry(i, c))
story.append(NextPageTemplate('Body')); story.append(PageBreak())

# ================= SERIES + PODCASTS =================
story.append(Bkmk('Series & Podcasts'))
story += eyebrow('Grouping layers')
story.append(Paragraph('Series & Podcasts', sH1))
story.append(Paragraph('Series - captured index', sH2))
story.append(Paragraph('The Series tab groups messages into preaching series. The first render of the public '
    'index lists 20 series totaling %d episodes; the list scrolls deeper, so this is the captured slice, '
    'not the whole layer.' % ser_eps, sBody))
rows = [[Paragraph('<b>SERIES</b>', sTblH), Paragraph('<b>EP.</b>', sTblH), Paragraph('<b>CONTRIBUTOR</b>', sTblH)]]
for s in D.SERIES:
    rows.append([Paragraph(esc(s[0]), sTbl), Paragraph(str(s[1]), sTbl), Paragraph(esc(s[2]), sTbl)])
tb = Table(rows, colWidths=[3.55*inch, 0.5*inch, 2.75*inch], repeatRows=1)
tb.setStyle(TableStyle([('BACKGROUND', (0,0), (-1,0), NAVY), ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ('TOPPADDING', (0,0), (-1,-1), 3), ('BOTTOMPADDING', (0,0), (-1,-1), 3),
    ('LEFTPADDING', (0,0), (-1,-1), 6), ('LINEBELOW', (0,1), (-1,-1), 0.4, RULE)]))
story.append(tb)
story.append(Spacer(1, 5))
story.append(Paragraph('Also on the home-page series rail: %s.' % esc('; '.join(D.SERIES_EXTRA)), sNote))
story.append(Paragraph('Podcasts - the show layer', sH2))
story.append(Paragraph('Twelve of the %d contributors are podcast-first shows: %s. The Podcasts tab surfaces '
    'latest episodes across shows; cadence is weekly or faster for active shows. Episode-level enumeration '
    'for the shows arrives with the export.' % (nC, esc(', '.join(s[1] for s in shows))), sBody))
story.append(Paragraph('Captured library counts', sH2))
rows = [[Paragraph('<b>CONTRIBUTOR</b>', sTblH), Paragraph('<b>MESSAGES</b>', sTblH), Paragraph('<b>SHORTS</b>', sTblH), Paragraph('<b>NOTE</b>', sTblH)]]
for n, sm, sh, note in D.CAPTURED_COUNTS:
    rows.append([Paragraph(esc(n), sTbl), Paragraph(str(sm), sTbl), Paragraph(str(sh), sTbl), Paragraph(esc(note), sTbl)])
tb = Table(rows, colWidths=[2.1*inch, 0.85*inch, 0.7*inch, 3.15*inch], repeatRows=1)
tb.setStyle(TableStyle([('BACKGROUND', (0,0), (-1,0), NAVY), ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ('TOPPADDING', (0,0), (-1,-1), 4), ('BOTTOMPADDING', (0,0), (-1,-1), 4),
    ('LEFTPADDING', (0,0), (-1,-1), 6), ('LINEBELOW', (0,1), (-1,-1), 0.4, RULE)]))
story.append(tb)
story.append(PageBreak())

# ================= EXHIBIT A =================
sH1x = st('h1x', fontName=DISPLAY, fontSize=16.5, leading=20, textColor=NAVY, spaceAfter=3)
sBlrb = st('blrb', fontSize=9.2, leading=12.2, spaceAfter=8)

def exhibit(letter_, name, items, shorts_n, shorts_sample, blurb):
    out = [NextPageTemplate('TwoCol'), PageBreak(), Bkmk('Exhibit %s - %s' % (letter_, name))]
    out += eyebrow('Exhibit %s - complete title index' % letter_)
    out.append(Paragraph(name, sH1x))
    out.append(Paragraph(blurb, sBlrb))
    out.append(GoldRule(w=44, col=RULE, sb=0, sa=8))
    for i, (dur, ttl) in enumerate(items, 1):
        d = ('&nbsp;&nbsp;<font color="#8b94a5">%s</font>' % dur) if dur else ''
        out.append(Paragraph('<font color="#c9a35c">%03d</font>&nbsp;&nbsp;%s%s' % (i, esc(ttl), d), sItem))
    out.append(Spacer(1, 6))
    out.append(Paragraph('SHORTS - %d ON PLATFORM (SAMPLE OF %d BELOW; FULL LIST ARRIVES WITH THE EXPORT)'
                         % (shorts_n, len(shorts_sample)), sNote))
    for x in shorts_sample:
        out.append(Paragraph('- ' + esc(x), sItem))
    out.append(NextPageTemplate('Body')); out.append(PageBreak())
    return out

story += exhibit('A', 'The Summit Church', summit, D.SUMMIT_SHORTS_COUNT, D.SUMMIT_SHORTS_SAMPLE,
    'The platform\'s largest captured church library: all 137 full-length messages (sermons and Whole Disciple '
    'Podcast episodes) as listed on contributor page 1, with durations where the platform displays them. '
    'Voices include J.D. Greear, Bryan Loritts, Curtis Andrusko and John Muller.')
story += exhibit('B', 'McLean Bible Church', mclean, D.MCLEAN_SHORTS_COUNT, D.MCLEAN_SHORTS_SAMPLE,
    'All 80 full-length messages as listed on contributor page 4 - David Platt, Mike Kelsey, Eric Saunders and '
    'Nate Reed - spanning series including Kingmaker, Seen, Vision 2030, Image of the Invisible, The Word of God, '
    'How to Fight in the Dark, and God\'s Good Design.')

# ================= COMPLETING THE CENSUS =================
story.append(Bkmk('Completing the Census'))
story += eyebrow('From v1 to 100 percent')
story.append(Paragraph('Completing the Census', sH1))
story.append(Paragraph('Two paths take this document from a verified census to the complete item-level library.', sLede))
story.append(Paragraph('Path one - the platform export (recommended).', sH2))
story.append(Paragraph('One catalog export from the OCEANS team closes every gap in a day. Fields to request, '
    'in order of importance: <b>content ID - title - contributor - speaker - type</b> (sermon / podcast episode / '
    'short) <b>- series - publish date - duration - URL</b>. CSV or JSON, either works. From that file LifeTogether '
    'can return the full indexed library as a companion volume to this census, organized by contributor and by '
    'series, within one working day.', sBody))
story.append(Paragraph('Path two - continued crawl.', sH2))
story.append(Paragraph('Each contributor page renders its complete library publicly, so the remaining %d '
    'libraries can be captured the same way Exhibits A and B were - accurate but slower, and always a snapshot '
    'of a platform that is actively ingesting new content.' % (nC-2), sBody))
story.append(Spacer(1, 14)); story.append(GoldRule())
story.append(Paragraph('Prepared by LifeTogether Ministries - 25 years, 500+ church relationships, 50M+ campaign '
    'resources distributed. Compiled for the LifeTogether x OCEANS directory conversation. Status: prospective '
    'collaboration; this document records what the platform holds and implies no partnership terms.', sNote))

doc.build(story)
print('PAGES OK')
