# -*- coding: utf-8 -*-
"""Master Preaching Index -> PDF"""
import os
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (BaseDocTemplate, PageTemplate, Frame, Paragraph,
                                Spacer, Table, TableStyle, PageBreak, KeepTogether,
                                Flowable, NextPageTemplate)

from data_topics import TOPIC_FAMILIES, PEOPLE
from data_books import BOOKS
from data_passages import (PASSAGE_GROUPS, CHRISTIAN_YEAR, CIVIL_CALENDAR,
                           CHURCH_OCCASIONS, PASTORAL_OCCASIONS)

# ---------------------------------------------------------------- fonts
LIB = "/usr/share/fonts/truetype/liberation/"
GF = "/usr/share/fonts/truetype/google-fonts/"
pdfmetrics.registerFont(TTFont("Serif", LIB + "LiberationSerif-Regular.ttf"))
pdfmetrics.registerFont(TTFont("Serif-B", LIB + "LiberationSerif-Bold.ttf"))
pdfmetrics.registerFont(TTFont("Serif-I", LIB + "LiberationSerif-Italic.ttf"))
pdfmetrics.registerFont(TTFont("Serif-BI", LIB + "LiberationSerif-BoldItalic.ttf"))
pdfmetrics.registerFontFamily("Serif", normal="Serif", bold="Serif-B",
                              italic="Serif-I", boldItalic="Serif-BI")
pdfmetrics.registerFont(TTFont("Sans", GF + "Poppins-Regular.ttf"))
pdfmetrics.registerFont(TTFont("Sans-M", GF + "Poppins-Medium.ttf"))
pdfmetrics.registerFont(TTFont("Sans-B", GF + "Poppins-Bold.ttf"))
pdfmetrics.registerFontFamily("Sans", normal="Sans", bold="Sans-B", italic="Sans")

# ---------------------------------------------------------------- palette
INK = colors.HexColor("#080e16")
NAVY = colors.HexColor("#0b1726")
NAVY2 = colors.HexColor("#132439")
GOLD = colors.HexColor("#c9a35c")
GOLDB = colors.HexColor("#e3c186")
CREAM = colors.HexColor("#ece7d8")
CREAM2 = colors.HexColor("#f6f3ea")
MUTED = colors.HexColor("#6b7484")
RULE = colors.HexColor("#d8d2c2")

PW, PH = letter
MARGIN = 0.72 * inch

# ---------------------------------------------------------------- styles
def P(name, **kw):
    base = dict(name=name, fontName="Serif", fontSize=9.6, leading=13.6,
                textColor=INK, spaceAfter=7, alignment=TA_LEFT)
    base.update(kw)
    return ParagraphStyle(**base)

S = {
 "body": P("body", alignment=TA_JUSTIFY),
 "lead": P("lead", fontSize=11, leading=16, textColor=NAVY2, spaceAfter=11,
           alignment=TA_JUSTIFY),
 "h1": P("h1", fontName="Serif-B", fontSize=21, leading=24, textColor=NAVY,
         spaceAfter=3, spaceBefore=0),
 "h2": P("h2", fontName="Serif-B", fontSize=13.5, leading=17, textColor=NAVY,
         spaceBefore=15, spaceAfter=5),
 "h3": P("h3", fontName="Sans-B", fontSize=8, leading=11, textColor=GOLD,
         spaceBefore=12, spaceAfter=4),
 "eyebrow": P("eyebrow", fontName="Sans-M", fontSize=7.2, leading=10,
              textColor=GOLD, spaceAfter=3),
 "kicker": P("kicker", fontName="Sans-M", fontSize=7.2, leading=10,
             textColor=MUTED, spaceAfter=2),
 "deck": P("deck", fontName="Serif-I", fontSize=10.6, leading=15,
           textColor=MUTED, spaceAfter=13),
 "note": P("note", fontSize=8.6, leading=12, textColor=MUTED, spaceAfter=6),
 "tb": P("tb", fontSize=8.4, leading=11.4, spaceAfter=0),
 "tbb": P("tbb", fontName="Serif-B", fontSize=8.4, leading=11.4, spaceAfter=0),
 "tbi": P("tbi", fontName="Serif-I", fontSize=8.2, leading=11.2,
          textColor=NAVY2, spaceAfter=0),
 "th": P("th", fontName="Sans-M", fontSize=7, leading=9.5, textColor=CREAM,
         spaceAfter=0),
 "topic": P("topic", fontSize=8.6, leading=11.6, spaceAfter=0),
 "cover_t": P("cover_t", fontName="Serif-B", fontSize=38, leading=40,
              textColor=CREAM, spaceAfter=0, alignment=TA_LEFT),
 "cover_s": P("cover_s", fontName="Serif-I", fontSize=13.5, leading=19,
              textColor=GOLDB, spaceAfter=0),
 "cover_m": P("cover_m", fontName="Sans", fontSize=8, leading=13,
              textColor=colors.HexColor("#8b94a5"), spaceAfter=0),
 "cover_e": P("cover_e", fontName="Sans-M", fontSize=8.4, leading=12,
              textColor=GOLD, spaceAfter=0),
}

# ---------------------------------------------------------------- flowables
class HRule(Flowable):
    def __init__(self, w=None, color=GOLD, thick=1.6, space=6):
        Flowable.__init__(self); self.w = w; self.c = color
        self.t = thick; self.s = space
    def wrap(self, aw, ah):
        self._w = self.w or aw
        return (self._w, self.t + self.s)
    def draw(self):
        self.canv.setStrokeColor(self.c); self.canv.setLineWidth(self.t)
        self.canv.line(0, self.s, self._w, self.s)

class Band(Flowable):
    """Coloured full-width band holding a paragraph."""
    def __init__(self, text, style, bg=CREAM2, bar=GOLD, pad=9):
        Flowable.__init__(self); self.text = text; self.style = style
        self.bg = bg; self.bar = bar; self.pad = pad
    def wrap(self, aw, ah):
        self._w = aw
        self.p = Paragraph(self.text, self.style)
        pw, ph = self.p.wrap(aw - self.pad * 2 - 5, ah)
        self._h = ph + self.pad * 2
        return (aw, self._h)
    def draw(self):
        c = self.canv
        c.setFillColor(self.bg); c.rect(0, 0, self._w, self._h, stroke=0, fill=1)
        c.setFillColor(self.bar); c.rect(0, 0, 3, self._h, stroke=0, fill=1)
        self.p.drawOn(c, self.pad + 5, self.pad)

# ---------------------------------------------------------------- page furniture
def cover_page(canv, doc):
    canv.saveState()
    canv.setFillColor(NAVY); canv.rect(0, 0, PW, PH, stroke=0, fill=1)
    canv.setFillColor(NAVY2)
    canv.rect(0, PH - 2.2 * inch, PW, 2.2 * inch, stroke=0, fill=1)
    # gold hairlines
    canv.setStrokeColor(GOLD); canv.setLineWidth(2.2)
    canv.line(MARGIN, PH - 2.2 * inch, PW - MARGIN, PH - 2.2 * inch)
    canv.setStrokeColor(colors.HexColor("#243a55")); canv.setLineWidth(0.6)
    for i in range(8):
        y = 1.55 * inch + i * 5
        canv.line(MARGIN, y, MARGIN + 1.6 * inch, y)
    canv.restoreState()

def inner_page(canv, doc):
    canv.saveState()
    canv.setStrokeColor(RULE); canv.setLineWidth(0.5)
    canv.line(MARGIN, 0.62 * inch, PW - MARGIN, 0.62 * inch)
    canv.setFont("Sans", 6.6); canv.setFillColor(MUTED)
    canv.drawString(MARGIN, 0.45 * inch,
                    "THE MASTER PREACHING INDEX  \u00b7  LIFETOGETHER  \u00b7  REFERENCE ARCHITECTURE v1")
    canv.setFont("Sans-M", 7.4); canv.setFillColor(NAVY)
    canv.drawRightString(PW - MARGIN, 0.45 * inch, str(canv.getPageNumber()))
    canv.restoreState()

# ---------------------------------------------------------------- helpers
def tbl(data, widths, header=True, banded=True, valign="TOP", gridcolor=RULE):
    t = Table(data, colWidths=widths, repeatRows=1 if header else 0)
    cmds = [
        ("VALIGN", (0, 0), (-1, -1), valign),
        ("LEFTPADDING", (0, 0), (-1, -1), 6),
        ("RIGHTPADDING", (0, 0), (-1, -1), 6),
        ("TOPPADDING", (0, 0), (-1, -1), 4.5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4.5),
        ("LINEBELOW", (0, 0), (-1, -1), 0.4, gridcolor),
    ]
    if header:
        cmds += [("BACKGROUND", (0, 0), (-1, 0), NAVY),
                 ("TOPPADDING", (0, 0), (-1, 0), 5.5),
                 ("BOTTOMPADDING", (0, 0), (-1, 0), 5.5),
                 ("LINEBELOW", (0, 0), (-1, 0), 0, NAVY)]
    if banded:
        start = 1 if header else 0
        for i in range(start, len(data)):
            if (i - start) % 2 == 1:
                cmds.append(("BACKGROUND", (0, i), (-1, i), CREAM2))
    t.setStyle(TableStyle(cmds))
    return t

def head(story, eyebrow, title, deck=None):
    story.append(Paragraph(eyebrow, S["eyebrow"]))
    story.append(Paragraph(title, S["h1"]))
    story.append(HRule(w=1.35 * inch, thick=2.2, space=8))
    if deck:
        story.append(Paragraph(deck, S["deck"]))

def para(story, *texts):
    for t in texts:
        story.append(Paragraph(t, S["body"]))
