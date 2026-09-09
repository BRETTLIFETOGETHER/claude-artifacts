import json
from reportlab.lib.pagesizes import letter
from reportlab.lib.colors import HexColor
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER
from reportlab.pdfgen import canvas as canvasmod
from reportlab.platypus import Paragraph

C = json.load(open('/home/claude/rg/content.json'))

W, H = letter
NAVY = HexColor('#1B2A4A')
DEEP = HexColor('#131F36')
GOLD = HexColor('#B08D42')
GOLDD = HexColor('#8A6D2F')
INK = HexColor('#20252E')
GREY = HexColor('#5A6272')
CREAM = HexColor('#F7F5F0')
WHITE = HexColor('#FFFFFF')

ML, MR = 78, 78
CW = W - ML - MR

c = canvasmod.Canvas('/home/claude/rg/Revolutionary-Generosity-20-Big-Ideas.pdf', pagesize=letter)
c.setTitle('Revolutionary Generosity: 20 Big Ideas')
c.setAuthor('LifeTogether Ministries')

st_body = ParagraphStyle('body', fontName='Times-Roman', fontSize=10.6, leading=15.2,
                         textColor=INK, alignment=TA_LEFT)
st_q = ParagraphStyle('q', fontName='Times-Italic', fontSize=10.2, leading=14.2,
                      textColor=GOLDD, alignment=TA_LEFT)
st_intro = ParagraphStyle('intro', fontName='Times-Roman', fontSize=11.4, leading=17.4,
                          textColor=INK, alignment=TA_LEFT)
st_partsub = ParagraphStyle('partsub', fontName='Times-Italic', fontSize=10.6, leading=15.0,
                            textColor=GREY, alignment=TA_LEFT)
st_cover_sub = ParagraphStyle('cs', fontName='Times-Italic', fontSize=15, leading=22,
                              textColor=HexColor('#D9CBA8'), alignment=TA_CENTER)


def tracked(cv, text, x, y, font, size, color, track, center_width=None):
    cv.setFont(font, size)
    cv.setFillColor(color)
    total = sum(cv.stringWidth(ch, font, size) + track for ch in text) - track
    if center_width is not None:
        x = x + (center_width - total) / 2.0
    for ch in text:
        cv.drawString(x, y, ch)
        x += cv.stringWidth(ch, font, size) + track
    return total


def para_h(p, width):
    return p.wrapOn(c, width, 2000)[1]


def draw_para(p, x, y_top, width):
    h = p.wrapOn(c, width, 2000)[1]
    p.drawOn(c, x, y_top - h)
    return h


# ---------------- Cover ----------------
c.setFillColor(DEEP)
c.rect(0, 0, W, H, stroke=0, fill=1)

c.setStrokeColor(GOLD)
c.setLineWidth(1.1)
c.line(ML, H - 130, W - MR, H - 130)

tracked(c, 'THE SIGNATRY  \u00b7  A CONCEPT BRIEF', 0, H - 118, 'Helvetica-Bold', 8.4,
        HexColor('#C8A85E'), 3.4, center_width=W)

c.setFont('Times-Bold', 50)
c.setFillColor(WHITE)
c.drawCentredString(W / 2, H - 276, 'Revolutionary')
c.drawCentredString(W / 2, H - 336, 'Generosity')

c.setStrokeColor(GOLD)
c.setLineWidth(0.8)
c.line(W / 2 - 46, H - 374, W / 2 + 46, H - 374)

p = Paragraph('How Families Give While They Live,<br/>Give More Than Cash, and Leave More Than Money', st_cover_sub)
draw_para(p, ML, H - 402, CW)

tracked(c, '20 BIG IDEAS', 0, H - 512, 'Helvetica-Bold', 13, HexColor('#C8A85E'), 6.5, center_width=W)

c.setFont('Times-Italic', 12.6)
c.setFillColor(HexColor('#B9C0CE'))
c.drawCentredString(W / 2, H - 552, 'The twenty convictions behind a generation of generous families \u2014')
c.drawCentredString(W / 2, H - 571, 'and the twenty questions that put each one to work.')

c.setStrokeColor(HexColor('#3A4A6B'))
c.setLineWidth(0.6)
c.line(ML + 60, 152, W - MR - 60, 152)
c.setFont('Times-Roman', 11.4)
c.setFillColor(HexColor('#9AA4B6'))
c.drawCentredString(W / 2, 126, 'Steve French  \u00b7  Dale Armstrong')
c.setFont('Times-Italic', 8.6)
c.setFillColor(HexColor('#6E7A90'))
c.drawCentredString(W / 2, 100, 'Concept brief prepared for discussion \u00b7 not an approved project of The Signatry')
c.showPage()

# ---------------- Page 2: how to use ----------------
c.setFillColor(WHITE)
c.rect(0, 0, W, H, stroke=0, fill=1)
c.setFillColor(CREAM)
c.rect(0, H - 132, W, 132, stroke=0, fill=1)

tracked(c, 'BEFORE YOU BEGIN', ML, H - 74, 'Helvetica-Bold', 8.6, GOLDD, 3.2)
c.setFont('Times-Bold', 25)
c.setFillColor(NAVY)
c.drawString(ML, H - 108, 'Twenty ideas, and what to do with them')

y = H - 176
blocks = [
    "The generosity movement has spent twenty-five years winning the argument about the heart. What it has rarely done is put the conviction and the mechanics in one place, in language a family can read together on a Sunday afternoon. These twenty ideas are that attempt.",
    "Four of them are about ownership and fear \u2014 the questions underneath every giving decision. Four are about what you actually own, which for most families is not what sits in the checking account. Four are about the household, because generosity is not inherited, it is rehearsed. Four are about the rooms and relationships that either produce generous families or quietly prevent them. The last four are about what the whole thing is for.",
    "Each idea ends with a question. The questions are the point. Read the ideas in an hour if you like, but give the questions a year \u2014 and answer them out loud, with the people who will inherit whatever you decide.",
]
for b in blocks:
    p = Paragraph(b, st_intro)
    y -= draw_para(p, ML, y, CW) + 16

y -= 26
c.setStrokeColor(HexColor('#DCD8CE'))
c.setLineWidth(0.7)
c.line(ML, y, W - MR, y)
y -= 34

tracked(c, 'THE FIVE MOVEMENTS', ML, y, 'Helvetica-Bold', 8.6, GOLDD, 3.2)
y -= 26
for i, part in enumerate(C['parts']):
    c.setFont('Times-Bold', 13.4)
    c.setFillColor(GOLD)
    c.drawString(ML, y, 'Part %s' % part['num'])
    c.setFillColor(NAVY)
    c.drawString(ML + 68, y, part['name'])
    y -= 17
    p = Paragraph(part['premise'], st_partsub)
    y -= draw_para(p, ML + 68, y, CW - 68) + 16

c.setFont('Times-Italic', 9)
c.setFillColor(GREY)
c.drawCentredString(W / 2, 56, 'Revolutionary Generosity \u00b7 20 Big Ideas')
c.showPage()


# ---------------- Idea pages ----------------
def page_header(part, cont=False):
    c.setFillColor(WHITE)
    c.rect(0, 0, W, H, stroke=0, fill=1)
    c.setFillColor(NAVY)
    c.rect(0, H - 96, W, 96, stroke=0, fill=1)
    tracked(c, 'PART %s' % part['num'].upper(), ML, H - 44, 'Helvetica-Bold', 8.4,
            HexColor('#C8A85E'), 3.6)
    c.setFont('Times-Bold', 21)
    c.setFillColor(WHITE)
    c.drawString(ML, H - 76, part['name'] + (' (continued)' if cont else ''))
    return H - 142


def footer(n):
    c.setStrokeColor(HexColor('#E2E0DA'))
    c.setLineWidth(0.6)
    c.line(ML, 66, W - MR, 66)
    c.setFont('Times-Italic', 8.6)
    c.setFillColor(GREY)
    c.drawString(ML, 50, 'Revolutionary Generosity \u00b7 20 Big Ideas')
    c.setFont('Times-Roman', 8.6)
    c.drawRightString(W - MR, 50, str(n))


pageno = 3
NUMW = 44
BODYW = CW - NUMW

TOP = H - 138
FOOT = 96

for pi, part in enumerate(C['parts']):
    items = [x for x in C['chapters'] if x['part'] == pi + 1]
    heights = []
    for ch in items:
        pb = Paragraph(ch['magnet'], st_body)
        pq = Paragraph('<b>The question:</b> ' + ch['question'], st_q)
        heights.append(32 + para_h(pb, BODYW) + 9 + para_h(pq, BODYW))
    slack = (TOP - FOOT) - sum(heights)
    gap = max(30.0, min(62.0, slack / max(1, len(items) - 1))) if slack > 0 else 30.0

    y = page_header(part)
    cont = False
    for ch in items:
        pb = Paragraph(ch['magnet'], st_body)
        pq = Paragraph('<b>The question:</b> ' + ch['question'], st_q)
        need = 32 + para_h(pb, BODYW) + 9 + para_h(pq, BODYW)
        if y - need < FOOT:
            footer(pageno); pageno += 1; c.showPage()
            cont = True
            y = page_header(part, cont)
        c.setFont('Times-Bold', 20)
        c.setFillColor(GOLD)
        c.drawString(ML, y - 15, '%02d' % ch['n'])
        c.setFont('Times-Bold', 14.2)
        c.setFillColor(NAVY)
        c.drawString(ML + NUMW, y - 14, ch['title'])
        y -= 32
        y -= draw_para(pb, ML + NUMW, y, BODYW) + 9
        c.setStrokeColor(HexColor('#E7E1D2'))
        c.setLineWidth(2.0)
        qh = para_h(pq, BODYW - 12)
        c.line(ML + NUMW - 1, y, ML + NUMW - 1, y - qh)
        y -= draw_para(pq, ML + NUMW + 11, y, BODYW - 12) + gap
    footer(pageno); pageno += 1; c.showPage()

# ---------------- Closing ----------------
c.setFillColor(DEEP)
c.rect(0, 0, W, H, stroke=0, fill=1)
c.setStrokeColor(GOLD)
c.setLineWidth(1.0)
c.line(ML, H - 130, W - MR, H - 130)
tracked(c, 'THE NEXT STEP', 0, H - 118, 'Helvetica-Bold', 8.6, HexColor('#C8A85E'), 3.4, center_width=W)

c.setFont('Times-Bold', 31)
c.setFillColor(WHITE)
c.drawCentredString(W / 2, H - 200, 'Twenty questions,')
c.drawCentredString(W / 2, H - 238, 'one evening, one family.')

st_close = ParagraphStyle('close', fontName='Times-Roman', fontSize=11.6, leading=18.4,
                          textColor=HexColor('#C3CBDA'), alignment=TA_CENTER)
p = Paragraph(
    'Every idea in this brief ends with a question, and the twenty questions together make a benchmark. '
    'Work through them with your spouse, then with your adult children, then with whoever advises you. '
    'You will find out quickly which of the twenty you have already settled, which you have been avoiding, '
    'and which one is worth the next decade.', st_close)
draw_para(p, ML + 40, H - 286, CW - 80)

c.setStrokeColor(HexColor('#3A4A6B'))
c.setLineWidth(0.6)
c.line(W / 2 - 60, H - 420, W / 2 + 60, H - 420)

st_close2 = ParagraphStyle('close2', fontName='Times-Italic', fontSize=11.2, leading=17.6,
                           textColor=HexColor('#9AA4B6'), alignment=TA_CENTER)
p = Paragraph(
    'The full argument \u2014 the stories behind each idea, the mechanics almost no one is taught, '
    'and the six-session guide for families, small groups, and advisor study groups \u2014 is the book '
    'this brief was drawn from.', st_close2)
draw_para(p, ML + 50, H - 452, CW - 100)

c.setFont('Times-Bold', 15.4)
c.setFillColor(WHITE)
c.drawCentredString(W / 2, 232, 'Revolutionary Generosity')
c.setFont('Times-Italic', 10.6)
c.setFillColor(HexColor('#C8A85E'))
c.drawCentredString(W / 2, 210, 'Steve French \u00b7 Dale Armstrong')

c.setStrokeColor(HexColor('#3A4A6B'))
c.line(ML + 60, 150, W - MR - 60, 150)
c.setFont('Times-Italic', 8.6)
c.setFillColor(HexColor('#6E7A90'))
c.drawCentredString(W / 2, 128, 'Concept brief prepared for discussion \u00b7 not an approved project of The Signatry')
c.showPage()

c.save()
print('magnet pdf written')
