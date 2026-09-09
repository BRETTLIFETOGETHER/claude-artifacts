# -*- coding: utf-8 -*-
import os
from weasyprint import HTML
from pypdf import PdfReader
from wp_data import *

OUT = "/mnt/user-data/outputs"
os.makedirs(OUT, exist_ok=True)
TOTAL = 20

CSS = """
@page { size: Letter; margin: 0; }
* { box-sizing: border-box; }
body { margin: 0; font-family: 'Poppins'; font-weight: 300; color: #3A4553;
       font-size: 8.6pt; line-height: 1.44; }
.page { page-break-after: always; height: 11in; position: relative; overflow: hidden;
        background: #FFFFFF; }
.page.last { page-break-after: auto; }
.pad { padding: 0 0.78in; }

.foot { position: absolute; bottom: 0.36in; left: 0.78in; right: 0.78in; display: flex;
        justify-content: space-between; border-top: .6pt solid #E4E8ED; padding-top: 5pt;
        font-size: 6.2pt; letter-spacing: .14em; text-transform: uppercase; color: #A3ADBA; }
.rhead { display: flex; justify-content: space-between; align-items: baseline;
         padding: 0.46in 0.78in 0; }
.rhead .a { font-weight: 600; font-size: 6.4pt; letter-spacing: .24em; text-transform: uppercase;
            color: #B8873B; }
.rhead .b { font-family: 'Lora'; font-style: italic; font-size: 8.2pt; color: #A3ADBA; }

h2 { font-family: 'Lora'; font-weight: 600; font-size: 21pt; line-height: 1.1; color: #101B2E;
     margin: 6pt 0 0; letter-spacing: -.016em; }
h2.sm { font-size: 17pt; }
.kick { font-weight: 600; font-size: 6.6pt; letter-spacing: .26em; text-transform: uppercase;
        color: #B8873B; }
.dek { font-family: 'Lora'; font-style: italic; font-size: 10pt; line-height: 1.5; color: #5C6B7C;
       margin-top: 8pt; max-width: 5.4in; }
.prose { font-family: 'Lora'; font-size: 9.5pt; line-height: 1.62; color: #3A4553; }
.prose p { margin: 0 0 9pt; }
.hr { border-top: .6pt solid #E4E8ED; margin: 14pt 0; }
.lb { font-weight: 600; font-size: 6.4pt; letter-spacing: .2em; text-transform: uppercase;
      color: #101B2E; }
.sec { margin-top: 22pt; }

/* ---------------- cover ---------------- */
.cover { background: #101B2E; color: #fff; height: 11in; padding: 1.05in 0.78in 0;
         position: relative; }
.cover .type { font-weight: 600; font-size: 7pt; letter-spacing: .34em; text-transform: uppercase;
               color: #B8873B; }
.cover .rule { width: 52pt; border-top: 2.4pt solid #B8873B; margin: 15pt 0 26pt; }
.cover h1 { font-family: 'Lora'; font-weight: 600; font-size: 42pt; line-height: 1.03;
            margin: 0; letter-spacing: -.022em; }
.cover h1 em { font-style: normal; color: #7FA3D6; }
.cover .sub { font-family: 'Lora'; font-size: 13pt; color: #C3D2E4; margin-top: 20pt;
              max-width: 5in; line-height: 1.42; }
.cover .deck { font-size: 9.4pt; line-height: 1.62; color: #93A8C2; max-width: 4.9in;
               margin-top: 16pt; }
.cover .band { display: flex; margin-top: 34pt; }
.cover .band div { flex: 1; height: 8pt; }
.cover .base { position: absolute; bottom: 0.85in; left: 0.78in; right: 0.78in; }
.cover .toc { display: flex; border-top: .7pt solid rgba(255,255,255,.2); padding-top: 12pt; }
.cover .toc div { flex: 1; padding-right: 10pt; font-size: 6.6pt; color: #7E93AE; line-height: 1.4; }
.cover .toc b { display: block; font-weight: 600; font-size: 7pt; letter-spacing: .16em;
                text-transform: uppercase; color: #fff; margin-bottom: 3pt; }
.cover .org { font-weight: 600; font-size: 6.8pt; letter-spacing: .22em; text-transform: uppercase;
              color: #7FA3D6; margin-bottom: 15pt; }

/* ---------------- stats ---------------- */
.stats { display: flex; border-top: 1.6pt solid #101B2E; border-bottom: .6pt solid #E4E8ED; }
.stats div { flex: 1; padding: 11pt 8pt 12pt 0; }
.stats .n { font-family: 'Lora'; font-weight: 600; font-size: 22pt; color: #101B2E;
            line-height: 1; letter-spacing: -.02em; }
.stats .t { font-size: 6.6pt; letter-spacing: .1em; text-transform: uppercase; color: #7A8797;
            margin-top: 5pt; }

/* ---------------- two-column contrast ---------------- */
.vs { margin-top: 6pt; }
.vs .hd { display: flex; gap: 18pt; padding-bottom: 7pt; border-bottom: 1.2pt solid #101B2E; }
.vs .hd div { flex: 1; }
.vs .hd .l { font-weight: 600; font-size: 8.6pt; color: #B85C3B; letter-spacing: .04em; }
.vs .hd .r { font-weight: 600; font-size: 8.6pt; color: #2F6B45; letter-spacing: .04em; }
.vs .row { display: flex; gap: 18pt; padding: 8.4pt 0; border-bottom: .6pt solid #EDF0F3; }
.vs .row div { flex: 1; font-size: 8.4pt; line-height: 1.4; }
.vs .row .l { color: #8B97A5; }
.vs .row .r { color: #23303F; font-weight: 400; }

.core { background: #F5F7F9; border-left: 2.8pt solid #B8873B; padding: 16pt 20pt; margin-top: 18pt; }
.core div { font-family: 'Lora'; font-weight: 600; font-size: 14pt; color: #101B2E;
            line-height: 1.36; letter-spacing: -.01em; }

/* ---------------- generic lists ---------------- */
.cols2 { display: flex; gap: 22pt; }
.cols2 > div { flex: 1; }
.cols3 { display: flex; gap: 18pt; }
.cols3 > div { flex: 1; }
ul.tick { margin: 6pt 0 0; padding: 0; list-style: none; }
ul.tick li { font-size: 8.2pt; line-height: 1.38; padding: 3.4pt 0 3.4pt 12pt; position: relative;
             border-bottom: .5pt solid #EDF0F3; }
ul.tick li:before { content: "\\203A"; position: absolute; left: 0; color: #B8873B; font-size: 9pt;
                    top: 2.6pt; }
.chipwrap { display: flex; flex-wrap: wrap; margin-top: 7pt; }
.chip { font-size: 7.4pt; color: #3A4553; border: .6pt solid #DCE2E8; border-radius: 10pt;
        padding: 3.2pt 9pt; margin: 0 4pt 4pt 0; }
.chip.dark { background: #101B2E; color: #fff; border-color: #101B2E; }

/* ---------------- module + form tables ---------------- */
.mods { display: flex; flex-wrap: wrap; margin-top: 4pt; }
.mods div { width: 33.33%; font-size: 8pt; color: #3A4553; padding: 5pt 10pt 5pt 13pt;
            position: relative; border-bottom: .5pt solid #EDF0F3; }
.mods div:before { content: ""; position: absolute; left: 0; top: 9pt; width: 5pt; height: 5pt;
                   background: #B8873B; border-radius: 1pt; }
.forms { width: 100%; border-collapse: collapse; margin-top: 6pt; }
.forms td { padding: 6.4pt 0; border-bottom: .5pt solid #EDF0F3; font-size: 8.4pt;
            vertical-align: baseline; }
.forms td.a { font-weight: 500; color: #101B2E; }
.forms td.b { text-align: right; font-size: 7.4pt; color: #8B97A5; letter-spacing: .04em; }

/* ---------------- worked example ---------------- */
.example { border: .7pt solid #DCE2E8; border-top: 2.6pt solid #101B2E; padding: 14pt 16pt;
           margin-top: 12pt; }
.example .t { font-family: 'Lora'; font-weight: 600; font-size: 14pt; color: #101B2E; }
.example .s { font-size: 7.2pt; letter-spacing: .12em; text-transform: uppercase; color: #8B97A5;
              margin-top: 4pt; }
.arrow { text-align: center; font-size: 12pt; color: #C6CEd6; margin: 8pt 0; }

/* ---------------- library map ---------------- */
.arc { margin-top: 11pt; }
.arc .h { display: flex; align-items: baseline; gap: 9pt; padding-bottom: 4pt;
          border-bottom: 1pt solid; }
.arc .h .n { font-weight: 600; font-size: 9pt; letter-spacing: -.01em; }
.arc .h .d { flex: 1; font-size: 7.2pt; color: #8B97A5; }
.arc .h .r { font-size: 6.6pt; letter-spacing: .12em; color: #A3ADBA; }
.cl { display: flex; align-items: center; gap: 9pt; padding: 4.2pt 0;
      border-bottom: .5pt solid #F0F3F6; }
.cl .no { width: 15pt; font-size: 7pt; color: #A3ADBA; flex: none; text-align: right; }
.cl .nm { flex: 1; font-size: 8.2pt; color: #23303F; }
.cl .dots { flex: none; }
.cl .dots u { display: inline-block; width: 5.6pt; height: 5.6pt; border-radius: 50%;
              margin-left: 3pt; text-decoration: none; }

/* ---------------- taxonomy ---------------- */
.tax { display: flex; flex-wrap: wrap; }
.tx { width: 33.33%; padding: 0 12pt 12pt 0; break-inside: avoid; }
.tx .h { display: flex; align-items: baseline; gap: 5pt; border-top: 1.8pt solid;
         padding-top: 5pt; }
.tx .h .n { font-family: 'Lora'; font-weight: 600; font-size: 9.4pt; }
.tx .h .t { flex: 1; font-weight: 600; font-size: 7.6pt; color: #101B2E; line-height: 1.18; }
.tx ol { margin: 5pt 0 0; padding: 0; list-style: none; }
.tx li { font-size: 6.9pt; line-height: 1.36; color: #4A5766; padding: 1.1pt 0 1.1pt 13pt;
         position: relative; }
.tx li span { position: absolute; left: 0; color: #B4BEC9; font-size: 6.2pt; }

/* ---------------- layers ---------------- */
.stack { margin-top: 10pt; }
.ly { display: flex; align-items: center; gap: 12pt; padding: 9.6pt 13pt; margin-bottom: 4pt;
      border-left: 3.4pt solid; background: #F7F9FA; }
.ly .k { width: 42pt; flex: none; font-weight: 600; font-size: 6.6pt; letter-spacing: .16em;
         text-transform: uppercase; }
.ly .n { width: 128pt; flex: none; font-weight: 600; font-size: 9.2pt; color: #101B2E;
         line-height: 1.2; }
.ly .d { flex: 1; font-size: 7.8pt; line-height: 1.4; color: #5C6B7C; }

/* ---------------- overlays ---------------- */
.ov { display: flex; gap: 9pt; margin-top: 10pt; }
.ovc { flex: 1; border-top: 2.6pt solid; padding-top: 7pt; }
.ovc .n { font-weight: 600; font-size: 8.6pt; color: #101B2E; }
.ovc ul { margin: 5pt 0 0; padding: 0; list-style: none; }
.ovc li { font-size: 6.9pt; line-height: 1.46; color: #5C6B7C; }

/* ---------------- business models ---------------- */
.mg { margin-top: 13pt; }
.mg .h { display: flex; align-items: baseline; gap: 8pt; border-bottom: 1pt solid;
         padding-bottom: 4pt; }
.mg .h .n { font-weight: 600; font-size: 8.8pt; }
.mg .h .c { font-size: 6.6pt; letter-spacing: .14em; text-transform: uppercase; color: #A3ADBA; }
.mm { display: flex; gap: 12pt; padding: 7pt 0; border-bottom: .5pt solid #F0F3F6; }
.mm .a { width: 132pt; flex: none; font-weight: 500; font-size: 8.2pt; color: #101B2E;
         line-height: 1.24; }
.mm .b { flex: 1; font-size: 7.6pt; line-height: 1.42; color: #5C6B7C; }
.price { width: 100%; border-collapse: collapse; margin-top: 7pt; }
.price td { padding: 6pt 0; border-bottom: .5pt solid #EDF0F3; font-size: 8.4pt; }
.price td.b { text-align: right; font-family: 'Lora'; font-weight: 600; color: #101B2E; }

/* ---------------- readiness ---------------- */
.gauge { margin-top: 12pt; }
.gauge .row { margin-bottom: 14pt; }
.gauge .lbl { display: flex; justify-content: space-between; align-items: baseline; }
.gauge .lbl .a { font-weight: 500; font-size: 9pt; color: #101B2E; }
.gauge .lbl .b { font-family: 'Lora'; font-weight: 600; font-size: 12pt; }
.gauge .bar { height: 13pt; background: #EDF0F3; margin-top: 5pt; position: relative; }
.gauge .bar u { position: absolute; left: 0; top: 0; bottom: 0; display: block;
                text-decoration: none; }
.gauge .cap { font-size: 7.4pt; color: #8B97A5; margin-top: 4pt; line-height: 1.4; }

/* ---------------- roadmap ---------------- */
.phases { display: flex; align-items: flex-end; gap: 10pt; margin-top: 12pt; height: 108pt; }
.ph { flex: 1; text-align: center; }
.ph .bx { border-radius: 2pt 2pt 0 0; color: #fff; padding-top: 9pt; }
.ph .bx .n { font-family: 'Lora'; font-weight: 600; font-size: 19pt; line-height: 1; }
.ph .bx .t { font-size: 6.4pt; letter-spacing: .18em; text-transform: uppercase; margin-top: 4pt;
             color: rgba(255,255,255,.85); }
.ph .c { font-size: 7pt; color: #8B97A5; margin-top: 6pt; line-height: 1.34; }
.steps { display: flex; flex-wrap: wrap; margin-top: 6pt; }
.st { width: 50%; display: flex; gap: 9pt; padding: 6.6pt 14pt 6.6pt 0; }
.st .n { width: 17pt; height: 17pt; flex: none; border-radius: 50%; background: #101B2E;
         color: #fff; font-weight: 600; font-size: 7pt; text-align: center; line-height: 17pt; }
.st .t { flex: 1; font-size: 8.2pt; line-height: 1.36; color: #23303F; padding-top: 2pt; }
.warn { border: .7pt solid #E8D5CC; border-left: 2.8pt solid #B85C3B; background: #FCF8F6;
        padding: 12pt 15pt; margin-top: 6pt; }
.warn .k { font-weight: 600; font-size: 6.4pt; letter-spacing: .2em; text-transform: uppercase;
           color: #B85C3B; }
.warn p { margin: 5pt 0 0; font-size: 8.4pt; line-height: 1.48; color: #4A5766; }

/* ---------------- finale ---------------- */
.finale { background: #101B2E; color: #fff; padding: 34pt 0.78in; margin-top: 18pt; }
.finale .k { font-weight: 600; font-size: 6.8pt; letter-spacing: .28em; text-transform: uppercase;
             color: #B8873B; }
.finale h2 { font-family: 'Lora'; font-weight: 600; font-size: 19pt; line-height: 1.34;
             color: #fff; margin: 12pt 0 0; letter-spacing: -.01em; }
.finale p { font-size: 9.2pt; line-height: 1.6; color: #93A8C2; margin: 14pt 0 0; max-width: 5.3in; }
.launch { background: #101B2E; color: #fff; padding: 20pt 22pt; margin-top: 10pt; }
.launch .n { font-family: 'Lora'; font-weight: 600; font-size: 21pt; letter-spacing: -.014em; }
.launch .s { font-size: 7.6pt; letter-spacing: .14em; text-transform: uppercase; color: #7FA3D6;
             margin-top: 6pt; }
"""


# =============================================================== graphics
def svg_engine():
    """1 master tool x 13 modules x 5 overlays = hundreds of finished editions."""
    o = ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 720 268" width="100%">']
    mid = 140

    def cap(x, t, n):
        o.append('<text x="%d" y="26" font-family="Poppins" font-size="7.4" font-weight="600" '
                 'letter-spacing="1.9" fill="#101B2E" text-anchor="middle">%s</text>' % (x, t))
        o.append('<text x="%d" y="252" font-family="Lora" font-size="17" font-weight="600" '
                 'fill="#101B2E" text-anchor="middle">%s</text>' % (x, n))

    # stage 1 — one master tool
    o.append('<rect x="52" y="%d" width="84" height="56" rx="3" fill="#101B2E"/>' % (mid - 28))
    cap(94, "MASTER TOOL", "1")

    # stage 2 — 13 modules
    x2 = 224
    for i in range(13):
        y = mid - 71 + i * 11
        o.append('<rect x="%d" y="%d" width="96" height="7.4" rx="1.4" fill="#2B5C9B" '
                 'fill-opacity="%.2f"/>' % (x2 - 48, y, 0.42 + 0.045 * i))
    cap(x2, "CONTENT MODULES", "13")

    # stage 3 — 5 overlays
    x3 = 400
    cols = ["#2B5C9B", "#0F7A6C", "#B85C3B", "#6B4E9E", "#2F6B45"]
    for i, c in enumerate(cols):
        y = mid - 62 + i * 25
        o.append('<rect x="%d" y="%d" width="96" height="18" rx="2" fill="%s" '
                 'fill-opacity=".82"/>' % (x3 - 48, y, c))
    cap(x3, "OVERLAY SYSTEMS", "5")

    # stage 4 — finished editions grid
    x4 = 600
    for r in range(7):
        for c in range(6):
            o.append('<rect x="%d" y="%d" width="13" height="10" rx="1.2" fill="#101B2E" '
                     'fill-opacity="%.2f"/>' % (x4 - 52 + c * 18, mid - 74 + r * 15,
                                                0.16 + 0.10 * ((r + c) % 7)))
    cap(x4, "FINISHED EDITIONS", "\u221e")

    # operators
    for x, sym in ((178, "\u00d7"), (352, "\u00d7"), (516, "=")):
        o.append('<text x="%d" y="%d" font-family="Poppins" font-size="15" fill="#B8873B" '
                 'text-anchor="middle">%s</text>' % (x, mid + 6, sym))
    o.append('</svg>')
    return "".join(o)


def svg_overlay_stack():
    """A master edition with five overlays applied."""
    o = ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 620 300" width="100%">']
    rows = [("Master edition", "#8B97A5"), ("Branding", "#2B5C9B"), ("Audience", "#0F7A6C"),
            ("Values", "#B85C3B"), ("Content", "#6B4E9E"), ("Format", "#2F6B45")]
    for i, (name, col) in enumerate(rows):
        x = 40 + i * 21
        y = 224 - i * 38
        o.append('<rect x="%d" y="%d" width="178" height="46" rx="3" fill="#FFFFFF" '
                 'stroke="#DCE2E8" stroke-width=".8"/>' % (x, y))
        o.append('<rect x="%d" y="%d" width="5.4" height="46" rx="1.4" fill="%s"/>' % (x, y, col))
        o.append('<text x="%d" y="%d" font-family="Poppins" font-size="9" font-weight="500" '
                 'fill="#101B2E">%s</text>' % (x + 17, y + 28, name))
        o.append('<line x1="%d" y1="%d" x2="300" y2="%d" stroke="#E4E8ED" stroke-width=".7" '
                 'stroke-dasharray="2 2"/>' % (x + 178, y + 23, y + 23))
        lbl = "the neutral, universal baseline" if i == 0 else "overlay %d" % i
        o.append('<text x="308" y="%d" font-family="Poppins" font-size="7.4" fill="#8B97A5">%s</text>'
                 % (y + 26, lbl))
    o.append('<path d="M470 30 L482 30 L482 250 L470 250" fill="none" stroke="#B8873B" '
             'stroke-width="1"/>')
    o.append('<text x="492" y="134" font-family="Lora" font-size="11" font-weight="600" '
             'fill="#101B2E">One finished,</text>')
    o.append('<text x="492" y="149" font-family="Lora" font-size="11" font-weight="600" '
             'fill="#101B2E">personalized</text>')
    o.append('<text x="492" y="164" font-family="Lora" font-size="11" font-weight="600" '
             'fill="#101B2E">resource</text>')
    o.append('</svg>')
    return "".join(o)


# =============================================================== helpers
def foot(p, right=""):
    return ('<div class="foot"><span>%s</span><span>%s</span><span>Page %d of %d</span></div>'
            % ("Create Once. Configure Many Ways.", right, p, TOTAL))


def rhead(sec):
    return ('<div class="rhead"><div class="a">%s</div>'
            '<div class="b">Strategy White Paper</div></div>' % sec)


def page(sec, body, n, last=False):
    return ('<div class="page%s">%s<div class="pad">%s</div>%s</div>'
            % (" last" if last else "", rhead(sec), body, foot(n)))


def ul(items, cls="tick"):
    return '<ul class="%s">%s</ul>' % (cls, "".join("<li>%s</li>" % i for i in items))


def chips(items, dark=False):
    c = "chip dark" if dark else "chip"
    return '<div class="chipwrap">%s</div>' % "".join(
        '<span class="%s">%s</span>' % (c, i) for i in items)


def arc_of(cn):
    for name, col, (a, b), d in ARCS:
        if a <= cn <= b:
            return name, col
    return "", "#101B2E"


# =============================================================== pages
def build():
    P = []

    # 1 — cover
    P.append("""
<div class="cover">
  <div class="type">{doctype}</div>
  <div class="rule"></div>
  <h1>{ta}<br><em>{tb}</em></h1>
  <div class="sub">{sub}</div>
  <div class="deck">{deck}</div>
  <div class="band">{band}</div>
  <div class="base">
    <div class="org">LifeTogether {em} The Human Side of Wealth</div>
    <div class="toc">
      <div><b>The Choice</b>Custom shop or publishing platform</div>
      <div><b>Four Assets</b>Library, modules, engine, fulfillment</div>
      <div><b>200 Tools</b>Twenty collections, five arcs</div>
      <div><b>The Model</b>Ten revenue paths and pricing</div>
      <div><b>The Build</b>Twenty-five tools first</div>
    </div>
  </div>
</div>""".format(doctype=DOCTYPE, ta=TITLE_A, tb=TITLE_B, sub=SUBTITLE, deck=DECK, em=EM,
                 band="".join('<div style="background:%s"></div>' % c
                              for _, c, _, _ in ARCS)))

    # 2 — executive summary
    stats = "".join('<div><div class="n">%s</div><div class="t">%s</div></div>' % (n, t)
                    for n, t in STATS)
    P.append(page("Executive Summary", """
    <div style="height:26pt"></div>
    <div class="kick">Executive Summary</div>
    <h2>The opportunity is not two hundred products.<br>It is one system that produces them.</h2>
    <div style="height:16pt"></div>
    <div class="stats">{stats}</div>
    <div style="height:16pt"></div>
    <div class="prose">{paras}</div>
    """.format(stats=stats, paras="".join("<p>%s</p>" % p for p in EXEC)), 2))

    # 3 — the strategic choice
    rows = "".join('<div class="row"><div class="l">%s</div><div class="r">%s</div></div>' % (l, r)
                   for l, r in CHOICE)
    P.append(page("The Strategic Choice", """
    <div class="sec"><div class="kick">The Strategic Choice</div>
      <h2>Two businesses that look identical<br>from the outside.</h2>
      <div class="dek">Both sell beautiful resources to advisors and families. Only one of them
        gets easier, cheaper, and more valuable with every project delivered.</div></div>
    <div class="hr"></div>
    <div class="vs">
      <div class="hd"><div class="l">The Custom Shop</div><div class="r">The Publishing Platform</div></div>
      {rows}
    </div>
    <div class="core">{core}</div>
    <div style="margin-top:16pt" class="prose">
      <p>The difference is not ambition or craft. It is whether the intellectual property is
      written once into a structured system, or written again into every deliverable. Everything
      that follows in this paper is a consequence of that single decision.</p>
    </div>
    """.format(rows=rows, core="".join("<div>%s</div>" % c for c in CORE)), 3))

    # 4 — multiplication engine
    P.append(page("The Multiplication Engine", """
    <div class="sec"><div class="kick">How It Works</div>
      <h2>The multiplication engine</h2>
      <div class="dek">One methodology. Thirteen interchangeable content modules. Five overlay
        systems. Ten output formats. A single master tool becomes hundreds of distinct,
        finished editions without anyone rewriting it.</div></div>
    <div style="margin-top:22pt">{svg}</div>
    <div class="hr"></div>
    <div class="cols3">
      <div><div class="lb">What stays fixed</div>
        <div style="font-size:8.2pt;line-height:1.5;color:#5C6B7C;margin-top:6pt">The methodology,
          the questions, the exercises, the outcomes. This is the approved intellectual property
          and it is authored once, to a professional editorial standard.</div></div>
      <div><div class="lb">What varies</div>
        <div style="font-size:8.2pt;line-height:1.5;color:#5C6B7C;margin-top:6pt">Which modules
          appear, in what order, at what depth, in whose voice, under whose brand, for which
          audience, in which format, at which length.</div></div>
      <div><div class="lb">Why it compounds</div>
        <div style="font-size:8.2pt;line-height:1.5;color:#5C6B7C;margin-top:6pt">Every new
          module, overlay, and template improves every tool in the library at once. Growth is
          multiplicative rather than additive.</div></div>
    </div>
    """.format(svg=svg_engine()), 4))

    # 5 — asset one
    P.append(page("Asset One", """
    <div class="sec"><div class="kick">Asset One of Four</div>
      <h2>The Master Tool Library</h2>
      <div class="dek">A professionally written and designed library of reusable intellectual
        property, authored first in neutral, broadly usable language so that a single
        methodology can serve very different institutions.</div></div>
    <div class="hr"></div>
    <div class="lb">Who a neutral master edition can serve</div>
    {aud}
    <div class="hr"></div>
    <div class="cols2">
      <div>
        <div class="lb">One master tool</div>
        <div class="example" style="margin-top:8pt">
          <div class="t">Family Values Discovery Guide</div>
          <div class="s">Master methodology \u00b7 Collection 2</div>
        </div>
        <div style="font-size:8.2pt;line-height:1.5;color:#5C6B7C;margin-top:12pt">
          You are not writing ten different products. You are writing one strong framework
          with carefully designed variations \u2014 and the framework is the asset that appreciates.
        </div>
      </div>
      <div>
        <div class="lb">Ten editions from it</div>
        {eds}
      </div>
    </div>
    """.format(aud=chips(AUDIENCES), eds=ul(EDITIONS)), 5))

    # 6 — asset two
    forms = "".join('<tr><td class="a">%s</td><td class="b">%s</td></tr>' % (a, b) for a, b in FORMS)
    P.append(page("Asset Two", """
    <div class="sec"><div class="kick">Asset Two of Four</div>
      <h2>The Modular Content System</h2>
      <div class="dek">Every tool is assembled from reusable components that can be included,
        removed, reordered, or personalized. Without this, you are a custom publishing company.
        With it, you are a platform.</div></div>
    <div class="hr"></div>
    <div class="lb">The thirteen standard modules</div>
    <div class="mods">{mods}</div>
    <div class="hr"></div>
    <div class="lb">The same underlying tool becomes</div>
    <table class="forms">{forms}</table>
    """.format(mods="".join("<div>%s</div>" % m for m in MODULES), forms=forms), 6))

    # 7 — asset three
    P.append(page("Asset Three", """
    <div class="sec"><div class="kick">Asset Three of Four</div>
      <h2>The Personalization Engine</h2>
      <div class="dek">The system decides which content belongs in each finished resource. The
        material remains rooted in the approved library; its selection, sequence, and
        presentation are what change.</div></div>
    <div class="hr"></div>
    <div class="lb">Fifteen personalization inputs</div>
    {inp}
    <div class="hr"></div>
    <div class="lb">Worked example</div>
    <div class="cols2" style="margin-top:8pt">
      <div>
        <div style="font-size:8.2pt;color:#5C6B7C;line-height:1.5">A family completes its
          assessments and indicates four priorities:</div>
        {pri}
      </div>
      <div>
        <div class="example" style="margin-top:0">
          <div class="t">The Henderson Family<br>Legacy Journey</div>
          <div class="s">A customized 30-day journal</div>
        </div>
        <div style="font-size:7.4pt;letter-spacing:.14em;text-transform:uppercase;color:#8B97A5;margin-top:11pt">
          Drawing selected material from</div>
        <div style="font-size:8pt;line-height:1.62;color:#3A4553;margin-top:5pt">{draws}</div>
      </div>
    </div>
    <div style="font-size:8.2pt;line-height:1.5;color:#5C6B7C;margin-top:12pt">
      The finished journal carries the family name, an advisor introduction, the family\u2019s own
      stated priorities, recommended meeting dates, and the exercises selected for their
      situation \u2014 generated, not assembled by hand.</div>
    """.format(inp=chips(PERSON_INPUTS), pri=ul(WORKED_PRIORITIES),
               draws=" \u00b7 ".join(WORKED_DRAWS)), 7))

    # 8 — asset four
    pod = "".join('<tr><td class="a" style="font-family:Lora;font-weight:600;font-size:11pt;'
                  'color:#101B2E;width:56pt">%s</td><td style="font-size:8.2pt;color:#5C6B7C">%s</td></tr>'
                  % (n, t) for n, t in POD)
    P.append(page("Asset Four", """
    <div class="sec"><div class="kick">Asset Four of Four</div>
      <h2>Publishing and Fulfillment</h2>
      <div class="dek">The same generated resource must be able to leave the system as a file,
        a booklet, a workbook, or a hardcover book \u2014 in a run of one or a run of ten thousand.</div></div>
    <div class="hr"></div>
    <div class="cols2">
      <div><div class="lb">Digital publishing</div>{dig}</div>
      <div><div class="lb">Print publishing</div>{prt}</div>
    </div>
    <div class="hr"></div>
    <div class="lb">Print-on-demand at any scale</div>
    <table class="forms" style="margin-top:8pt">{pod}</table>
    """.format(dig=ul(DIGITAL), prt=ul(PRINT), pod=pod), 8))

    # 9 — library map
    arcs_html = []
    for name, col, (a, b), desc in ARCS:
        rows = []
        for cn, cname, items in COLLECTIONS:
            if a <= cn <= b:
                dots = "".join('<u style="background:%s;opacity:%.2f"></u>' % (col, 0.34 + i * 0.07)
                               for i in range(10))
                rows.append('<div class="cl"><span class="no">%02d</span>'
                            '<span class="nm">%s</span><span class="dots">%s</span></div>'
                            % (cn, cname, dots))
        arcs_html.append(
            '<div class="arc"><div class="h" style="border-color:%s">'
            '<span class="n" style="color:%s">%s</span><span class="d">%s</span>'
            '<span class="r">COLLECTIONS %02d\u2013%02d</span></div>%s</div>'
            % (col, col, name, desc, a, b, "".join(rows)))
    P.append(page("The Library Map", """
    <div class="sec"><div class="kick">The Library</div>
      <h2>Two hundred tools, twenty collections,<br>five arcs of family life.</h2>
      <div class="dek">The library should not feel like a warehouse. Grouping the twenty
        collections into five arcs gives an advisor a mental model they can hold \u2014 and gives
        the personalization engine a coherent sequence to recommend.</div></div>
    <div style="height:4pt"></div>
    {arcs}
    """.format(arcs="".join(arcs_html)), 9))

    # 10, 11 — taxonomy
    def tax_block(sub):
        out = []
        for cn, cname, items in sub:
            _, col = arc_of(cn)
            lis = "".join('<li><span>%02d</span>%s</li>' % (i, t)
                          for i, t in enumerate(items, (cn - 1) * 10 + 1))
            out.append('<div class="tx"><div class="h" style="border-color:%s">'
                       '<span class="n" style="color:%s">%02d</span>'
                       '<span class="t">%s</span></div><ol>%s</ol></div>'
                       % (col, col, cn, cname, lis))
        return '<div class="tax">%s</div>' % "".join(out)

    P.append(page("The Taxonomy", """
    <div class="sec" style="margin-top:18pt"><div class="kick">The Taxonomy \u2014 One of Two</div>
      <h2 class="sm">Collections one through ten</h2></div>
    <div class="hr" style="margin:10pt 0"></div>
    {t}
    """.format(t=tax_block(COLLECTIONS[:10])), 10))

    P.append(page("The Taxonomy", """
    <div class="sec" style="margin-top:18pt"><div class="kick">The Taxonomy \u2014 Two of Two</div>
      <h2 class="sm">Collections eleven through twenty</h2></div>
    <div class="hr" style="margin:10pt 0"></div>
    {t}
    """.format(t=tax_block(COLLECTIONS[10:])), 11))

    # 12 — overlays
    ovs = "".join('<div class="ovc" style="border-color:%s"><div class="n">%s</div>%s</div>'
                  % (c, n, "<ul>%s</ul>" % "".join("<li>%s</li>" % i for i in items))
                  for n, c, items in OVERLAYS)
    P.append(page("The Overlay System", """
    <div class="sec"><div class="kick">The Overlay System</div>
      <h2>Universal is not the same as bland.</h2>
      <div class="dek">The master editions should be universal, not generic in a weak sense.
        Strong concepts, proven questions, practical exercises, professional language, clear
        outcomes, adaptable examples \u2014 and a neutral baseline the platform then dresses.</div></div>
    <div style="margin-top:14pt">{svg}</div>
    <div class="hr" style="margin:10pt 0"></div>
    <div class="ov">{ovs}</div>
    """.format(svg=svg_overlay_stack(), ovs=ovs), 12))

    # 13 — architecture
    lys = "".join('<div class="ly" style="border-color:%s"><span class="k" style="color:%s">%s</span>'
                  '<span class="n">%s</span><span class="d">%s</span></div>' % (c, c, k, n, d)
                  for k, n, c, d in LAYERS)
    P.append(page("Product Architecture", """
    <div class="sec"><div class="kick">Product Architecture</div>
      <h2>Six layers</h2>
      <div class="dek">Each layer depends on the one beneath it. Most content companies build
        layers five and six and never build one through four \u2014 which is precisely why their
        work does not compound.</div></div>
    <div class="hr"></div>
    <div class="stack">{lys}</div>
    <div class="warn">
      <div class="k">The load-bearing layer</div>
      <p>Layer 1 is the only layer that cannot be bought, outsourced, or regenerated. Two hundred
      approved tools, written to a consistent editorial standard and structured for reuse, is the
      asset. Everything above it is a way of arranging that asset for a particular reader.</p>
    </div>
    """.format(lys=lys), 13))

    # 14 — journal
    P.append(page("The Journal Opportunity", """
    <div class="sec"><div class="kick">Flagship Product</div>
      <h2>The custom journal</h2>
      <div class="dek">Custom journals could become the most visible and valuable product on the
        platform \u2014 tangible, personal, gift-worthy, and naturally recurring.</div></div>
    <div class="hr"></div>
    <div class="example">
      <div class="t">The Anderson Family Legacy Journal</div>
      <div class="s">Prepared by Smith Family Wealth</div>
    </div>
    <div class="cols2" style="margin-top:16pt">
      <div><div class="lb">What it contains</div>{c}</div>
      <div><div class="lb">What the advisor orders</div>{o}
        <div style="font-size:8.2pt;line-height:1.5;color:#5C6B7C;margin-top:14pt">
          An annually updated edition converts a one-time deliverable into recurring revenue and
          a tangible client experience the family keeps on a shelf rather than in a folder.</div>
      </div>
    </div>
    """.format(c=ul(JOURNAL_CONTENTS), o=ul(JOURNAL_ORDERS)), 14))

    # 15 — curriculum
    sess = "".join('<div class="mm"><div class="a">Session %d. %s</div><div class="b">%s</div></div>'
                   % (i, t, d) for i, (t, d) in enumerate(SESSIONS, 1))
    P.append(page("The Curriculum Opportunity", """
    <div class="sec"><div class="kick">Flagship Product</div>
      <h2>The custom curriculum</h2>
      <div class="dek">The same platform produces complete, brandable curriculum \u2014 the highest
        contract value and the most defensible enterprise relationship.</div></div>
    <div class="hr"></div>
    <div class="lb">Six-Session Family Legacy Curriculum</div>
    <div style="margin-top:4pt">{sess}</div>
    <div class="hr"></div>
    <div class="cols2">
      <div><div class="lb">Each curriculum includes</div>{parts}</div>
      <div><div class="lb">Brandable for</div>{brands}
        <div style="font-size:8.2pt;line-height:1.5;color:#5C6B7C;margin-top:12pt">
          One curriculum, authored once, becomes seven institutional products \u2014 each of which
          feels custom-built to the organization that licenses it.</div></div>
    </div>
    """.format(sess=sess, parts=ul(CURRIC_PARTS), brands=ul(CURRIC_BRANDS)), 15))

    # 16 — business models
    groups = []
    for gname, gcol, models in MODEL_GROUPS:
        mm = "".join('<div class="mm"><div class="a">%s</div><div class="b">%s</div></div>' % (a, b)
                     for a, b in models)
        groups.append('<div class="mg"><div class="h" style="border-color:%s">'
                      '<span class="n" style="color:%s">%s</span>'
                      '<span class="c">%d models</span></div>%s</div>'
                      % (gcol, gcol, gname, len(models), mm))
    P.append(page("Revenue Models", """
    <div class="sec" style="margin-top:16pt"><div class="kick">The Business Model</div>
      <h2 class="sm">Ten ways the same library earns</h2>
      <div class="dek">Grouped by revenue behavior rather than by customer, because the mix
        determines the valuation more than the total does.</div></div>
    {groups}
    """.format(groups="".join(groups)), 16))

    # 17 — pricing + readiness
    pr = "".join('<tr><td>%s</td><td class="b">%s</td></tr>' % (a, b) for a, b in PRICING)
    P.append(page("Pricing and Position", """
    <div class="sec"><div class="kick">Unit Economics</div>
      <h2 class="sm">Per-family publishing</h2>
      <div class="dek">Indicative ranges. Final pricing depends on depth, printing, production,
        facilitation, and the degree of customization.</div></div>
    <table class="price">{pr}</table>
    <div class="hr"></div>
    <div class="sec" style="margin-top:6pt"><div class="kick">Honest Assessment</div>
      <h2 class="sm">How far away this is</h2></div>
    <div class="gauge">
      <div class="row">
        <div class="lbl"><span class="a">Underlying content concepts already in hand</span>
          <span class="b" style="color:#2F6B45">30\u201340%</span></div>
        <div class="bar"><u style="width:35%;background:#2F6B45"></u></div>
        <div class="cap">Spread across existing books, campaigns, journeys, advisor materials,
          family legacy resources, and expert partnerships. You are not starting from zero.</div>
      </div>
      <div class="row">
        <div class="lbl"><span class="a">Toward a functioning, repeatable publishing platform</span>
          <span class="b" style="color:#B85C3B">10\u201315%</span></div>
        <div class="bar"><u style="width:12.5%;background:#B85C3B"></u></div>
        <div class="cap">The content still has to be standardized, modularized, tagged, designed,
          personalized, and connected to production. The gap is executional, not conceptual.</div>
      </div>
    </div>
    <div class="cols2" style="margin-top:6pt">
      <div><div class="lb" style="color:#2F6B45">What is already true</div>{have}</div>
      <div><div class="lb" style="color:#B85C3B">What is still missing</div>{gaps}</div>
    </div>
    """.format(pr=pr, have=ul(HAVE), gaps=ul(GAPS)), 17))

    # 18 — sequenced build
    heights = [46, 62, 80, 100]
    cols = ["#2B5C9B", "#0F7A6C", "#6B4E9E", "#101B2E"]
    caps = ["Prove the model with the tools advisors ask for most",
            "Extend into the variations the pilots actually request",
            "Scale once modules and templates are stable",
            "Complete the taxonomy with demand already proven"]
    phs = "".join('<div class="ph"><div class="bx" style="background:%s;height:%dpt">'
                  '<div class="n">%s</div><div class="t">%s</div></div>'
                  '<div class="c">%s</div></div>' % (c, h, n, t, cap)
                  for (n, t), h, c, cap in zip(PHASES, heights, cols, caps))
    sts = "".join('<div class="st"><div class="n">%d</div><div class="t">%s</div></div>' % (i, s)
                  for i, s in enumerate(STEPS, 1))
    P.append(page("The Sequenced Build", """
    <div class="sec"><div class="kick">Execution</div>
      <h2>Build twenty-five tools completely<br>before building two hundred badly.</h2></div>
    <div class="warn">
      <div class="k">What not to do</div>
      <p>Do not begin by writing and designing two hundred finished thirty-page PDFs individually.
      That consumes enormous time and money while producing a library that may never be used \u2014
      and it produces it in exactly the unstructured form that prevents personalization later.</p>
    </div>
    <div class="hr"></div>
    <div class="lb">Library growth</div>
    <div class="phases">{phs}</div>
    <div class="hr"></div>
    <div class="lb">The eight execution steps</div>
    <div class="steps">{sts}</div>
    """.format(phs=phs, sts=sts), 18))

    # 19 — launch
    P.append(page("Recommended Launch", """
    <div class="sec"><div class="kick">Recommended Launch</div>
      <h2 class="sm">Where to start</h2></div>
    <div class="launch">
      <div class="n">{ln}{tm}</div>
      <div class="s">{ls}{tm}</div>
    </div>
    <div class="cols2" style="margin-top:18pt">
      <div><div class="lb">Initial custom outputs</div>{outs}</div>
      <div><div class="lb">Initial library</div>
        <div style="font-family:Lora;font-weight:600;font-size:26pt;color:#101B2E;margin-top:8pt;line-height:1">25</div>
        <div style="font-size:7.4pt;letter-spacing:.14em;text-transform:uppercase;color:#8B97A5;margin-top:4pt">proven tools</div>
        <div class="lb" style="margin-top:20pt">Initial customers</div>{cust}</div>
    </div>
    """.format(ln=LAUNCH_NAME, ls=LAUNCH_SUB, tm=TM, outs=ul(LAUNCH_OUTPUTS),
               cust=ul(LAUNCH_CUSTOMERS)), 19))

    # 20 — closing
    P.append("""
<div class="page last">
  {rh}
  <div class="pad">
    <div class="sec" style="margin-top:40pt"><div class="kick">The Promise</div>
      <h2>The clearest way to say<br>what this is.</h2></div>
    <div class="hr"></div>
    <div class="prose" style="font-size:12pt;line-height:1.62;color:#23303F">
      <p>{promise}</p>
    </div>
  </div>
  <div class="finale">
    <div class="k">Why It Matters</div>
    <h2>{closing}</h2>
    <p>Create once. Configure many ways. Personalize for every organization and family.
      Publish digitally or in print.</p>
  </div>
  {ft}
</div>""".format(rh=rhead("The Promise"), promise=PROMISE, closing=CLOSING, ft=foot(20)))

    return ('<!DOCTYPE html><html><head><meta charset="utf-8"><style>%s</style></head><body>%s'
            '</body></html>' % (CSS, "".join(P)))


if __name__ == "__main__":
    path = os.path.join(OUT, "White-Paper-Create-Once-Configure-Many-Ways.pdf")
    HTML(string=build()).write_pdf(path)
    r = PdfReader(path)
    print("pages: %d (expected %d)  %.0f x %.0f pt" % (
        len(r.pages), TOTAL, r.pages[0].mediabox.width, r.pages[0].mediabox.height))
