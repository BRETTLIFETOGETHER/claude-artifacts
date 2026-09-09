# -*- coding: utf-8 -*-
"""Layout B — Six Pillars Edition. One signature color per dimension, full-bleed bands."""
from content import *

CSS = """
@page {
  size: Letter; margin: 0;
}
* { box-sizing: border-box; }
body { margin: 0; font-family: 'Poppins'; font-weight: 400; color: #2B3440;
       font-size: 8.6pt; line-height: 1.34; }
.page { page-break-after: always; height: 11in; position: relative; overflow: hidden; }
.page.last { page-break-after: auto; }
.pad { padding: 0 0.6in; }
.foot { position: absolute; bottom: 0.3in; left: 0.6in; right: 0.6in;
        display: flex; justify-content: space-between; align-items: center;
        font-size: 6.3pt; letter-spacing: .12em; text-transform: uppercase; color: #9AA5B1;
        border-top: .6pt solid #E3E8ED; padding-top: 5pt; }

/* ---------- masthead (full bleed) ---------- */
.hero { background: #16233A; color: #FFFFFF; padding: 26pt 0.6in 0; }
.hero .eyebrow { font-weight: 500; font-size: 7pt; letter-spacing: .3em; text-transform: uppercase;
                 color: #86A6D6; }
.hero h1 { font-weight: 600; font-size: 25pt; line-height: 1.06; margin: 7pt 0 0;
           letter-spacing: -.015em; }
.hero .deck { font-weight: 300; font-size: 9.6pt; line-height: 1.45; color: #C8D6E8;
              max-width: 5.3in; margin-top: 7pt; }
.hero .aud { font-weight: 500; font-size: 6.5pt; letter-spacing: .17em; text-transform: uppercase;
             color: #7E9CC9; margin-top: 10pt; }
.chips { display: flex; margin-top: 15pt; }
.chips div { flex: 1; height: 7pt; }

/* ---------- instructions strip ---------- */
.howto { background: #F4F6F9; padding: 12pt 0.6in 13pt; display: flex; gap: 18pt; }
.howto .a { flex: 1.25; }
.howto .b { flex: 1; }
.lbl { font-weight: 600; font-size: 6.5pt; letter-spacing: .2em; text-transform: uppercase;
       color: #16233A; margin-bottom: 4pt; }
.howto p { margin: 0; font-weight: 300; font-size: 8pt; line-height: 1.45; color: #46536A; }
.keyrow { display: flex; gap: 5pt; }
.keyrow div { flex: 1; text-align: center; }
.keyrow .n { width: 15pt; height: 15pt; margin: 0 auto 3pt; border-radius: 50%;
             background: #16233A; color: #fff; font-weight: 600; font-size: 7pt;
             line-height: 15pt; }
.keyrow .t { font-weight: 300; font-size: 6.3pt; line-height: 1.2; color: #46536A; }

/* ---------- sections ---------- */
.section { margin-top: 12pt; break-inside: avoid; }
.sec-head { display: flex; align-items: center; gap: 9pt; padding: 6pt 10pt;
            border-radius: 2pt; color: #FFFFFF; }
.sec-head .num { width: 17pt; height: 17pt; flex: none; border-radius: 50%;
                 background: rgba(255,255,255,.22); font-weight: 600; font-size: 8pt;
                 text-align: center; line-height: 17pt; }
.sec-head .tt { flex: 1; }
.sec-head .t { font-weight: 600; font-size: 10.6pt; letter-spacing: -.01em; line-height: 1.15; }
.sec-head .q { font-weight: 300; font-size: 7.4pt; color: rgba(255,255,255,.86); margin-top: 1pt; }
.rows { border: .6pt solid #E3E8ED; border-top: none; }
.stmt { display: flex; align-items: center; gap: 8pt; padding: 6.6pt 10pt; }
.stmt:nth-child(even) { background: #F8FAFB; }
.stmt .t { flex: 1; font-weight: 300; font-size: 8.5pt; line-height: 1.32; color: #2B3440; }
.scale { flex: none; white-space: nowrap; }
.scale i { display: inline-block; width: 14pt; height: 14pt; border: .8pt solid #C4CCD6;
           border-radius: 50%; margin-left: 3pt; font-style: normal; font-weight: 400;
           font-size: 6.8pt; color: #8B96A3; text-align: center; line-height: 12.6pt; }
.sec-foot { display: flex; justify-content: flex-end; align-items: center; gap: 7pt;
            padding: 5.5pt 10pt; border-top: .6pt dashed #D8DFE6; }
.sec-foot .k { font-weight: 600; font-size: 6.6pt; letter-spacing: .15em; text-transform: uppercase; }
.sec-foot .v { width: 34pt; height: 15pt; border: .9pt solid; border-radius: 2pt; }
.sec-foot .d { font-weight: 500; font-size: 7.4pt; color: #7C8794; }

/* ---------- continuation header ---------- */
.runhead { display: flex; justify-content: space-between; align-items: center;
           background: #16233A; color: #fff; padding: 8pt 0.6in; }
.runhead .a { font-weight: 600; font-size: 7.4pt; letter-spacing: .2em; text-transform: uppercase; }
.runhead .b { font-weight: 300; font-size: 7.4pt; color: #A9BFDA; letter-spacing: .04em; }

/* ---------- scoring ---------- */
.scorehead { margin-top: 14pt; }
.scorehead h2 { font-weight: 600; font-size: 15pt; color: #16233A; margin: 0;
                letter-spacing: -.015em; }
.scorehead p { font-weight: 300; font-size: 8pt; color: #5A6675; margin: 3pt 0 0; }
.prof { margin-top: 9pt; }
.prow { display: flex; align-items: center; gap: 8pt; padding: 4.6pt 0;
        border-bottom: .6pt solid #EDF0F3; }
.prow .sw { width: 8pt; height: 8pt; flex: none; border-radius: 2pt; }
.prow .nm { flex: 1; font-weight: 400; font-size: 8.2pt; color: #2B3440; }
.prow .bar { flex: none; display: flex; gap: 1.4pt; }
.prow .bar u { display: block; width: 6.6pt; height: 11pt; border: .55pt solid #DCE2E8;
               border-radius: 1pt; text-decoration: none; }
.prow .bx { flex: none; width: 30pt; height: 14pt; border: .9pt solid; border-radius: 2pt; }
.prow .of { flex: none; font-weight: 500; font-size: 7pt; color: #8B96A3; width: 20pt; }
.shade { font-weight: 300; font-size: 6.4pt; color: #9AA5B1; text-align: right; margin-top: 3pt;
         letter-spacing: .04em; }
.total { display: flex; align-items: center; gap: 12pt; margin-top: 11pt; padding: 10pt 14pt;
         background: #16233A; border-radius: 3pt; color: #fff; }
.total .k { font-weight: 600; font-size: 8.4pt; letter-spacing: .2em; text-transform: uppercase;
            flex: 1; }
.total .bx { width: 54pt; height: 22pt; background: #fff; border-radius: 2pt; }
.total .of { font-weight: 300; font-size: 11pt; color: #A9BFDA; }
.bands { display: flex; gap: 7pt; margin-top: 11pt; }
.bands .c { flex: 1; border: .6pt solid #E3E8ED; border-top: 2.6pt solid; border-radius: 2pt;
            padding: 7pt 8pt 8pt; }
.bands .r { font-weight: 600; font-size: 9.6pt; letter-spacing: -.01em; }
.bands .n { font-weight: 600; font-size: 7.4pt; color: #16233A; margin-top: 2pt; line-height: 1.2; }
.bands .d { font-weight: 300; font-size: 6.5pt; line-height: 1.34; color: #5A6675; margin-top: 3pt; }
.qbox { margin-top: 11pt; background: #F4F6F9; border-radius: 3pt; padding: 10pt 12pt; }
.qbox .intro { font-weight: 300; font-size: 7.8pt; color: #46536A; line-height: 1.4; }
.qs { display: flex; gap: 12pt; margin-top: 7pt; }
.qs .q { flex: 1; display: flex; gap: 6pt; }
.qs .q b { font-weight: 600; font-size: 12pt; color: #B9C6D6; line-height: 1; }
.qs .q span { font-weight: 400; font-size: 7.6pt; line-height: 1.32; color: #2B3440; }
"""


def stmt_rows(sec):
    return "".join(
        '<div class="stmt"><div class="t">{}</div>'
        '<div class="scale"><i>1</i><i>2</i><i>3</i><i>4</i><i>5</i></div></div>'.format(s)
        for s in sec["items"])


def section_html(sec):
    return """
<div class="section">
  <div class="sec-head" style="background:{c}">
    <div class="num">{n}</div>
    <div class="tt"><div class="t">{title}</div><div class="q">{q}</div></div>
  </div>
  <div class="rows">
    {rows}
    <div class="sec-foot"><span class="k" style="color:{c}">Section Score</span>
      <span class="v" style="border-color:{c}"></span><span class="d">/ 20</span></div>
  </div>
</div>""".format(c=sec["color"], n=sec["n"], title=sec["title"], q=sec["q"], rows=stmt_rows(sec))


def foot(p):
    return ('<div class="foot"><span>Family Legacy Intelligence{tm} &nbsp;\u00b7&nbsp; '
            'The 10-Minute Family Legacy Assessment</span><span>Page {p} of 3</span></div>'
            ).format(tm=TM, p=p)


RUNHEAD = ('<div class="runhead"><div class="a">Family Legacy Intelligence{tm}</div>'
           '<div class="b">The 10-Minute Family Legacy Assessment</div></div>').format(tm=TM)


def build():
    chips = "".join('<div style="background:{}"></div>'.format(s["color"]) for s in SECTIONS)
    keyrow = "".join('<div><div class="n">{}</div><div class="t">{}</div></div>'.format(k, v)
                     for k, v in SCALE)
    p1 = "".join(section_html(SECTIONS[i]) for i in GROUPS[0])
    p2 = "".join(section_html(SECTIONS[i]) for i in GROUPS[1])
    p3 = "".join(section_html(SECTIONS[i]) for i in GROUPS[2])

    prof = "".join(
        '<div class="prow"><span class="sw" style="background:{c}"></span>'
        '<span class="nm">{n}</span>'
        '<span class="bar">{bar}</span>'
        '<span class="bx" style="border-color:{c}"></span><span class="of">/ 20</span></div>'.format(
            c=s["color"], n="{}. {}".format(s["n"], s["short"]), bar="<u></u>" * 20)
        for s in SECTIONS)

    bands = "".join(
        '<div class="c" style="border-top-color:{c}"><div class="r" style="color:{c}">{r}</div>'
        '<div class="n">{n}</div><div class="d">{d}</div></div>'.format(
            c=c, r=r, n=n, d=d)
        for (r, n, d), c in zip(BANDS, ["#2F6B45", "#A8811C", "#B85C3B", "#6B4E9E"]))

    qs = "".join('<div class="q"><b>{}</b><span>{}</span></div>'.format(i, q)
                 for i, q in enumerate(QUESTIONS, 1))

    return """<!DOCTYPE html><html><head><meta charset="utf-8"><style>{css}</style></head><body>

<div class="page">
  <div class="hero">
    <div class="eyebrow">Family Legacy Intelligence{tm}</div>
    <h1>{subtitle}</h1>
    <div class="deck">{deck}</div>
    <div class="aud">{aud}</div>
    <div class="chips">{chips}</div>
  </div>
  <div class="howto">
    <div class="a"><div class="lbl">Before You Begin</div><p>{preamble}</p></div>
    <div class="b"><div class="lbl">How to Rate \u2014 {instr_short}</div>
      <div class="keyrow">{keyrow}</div></div>
  </div>
  <div class="pad">{p1}</div>
  {foot1}
</div>

<div class="page">
  {runhead}
  <div class="pad">{p2}</div>
  {foot2}
</div>

<div class="page last">
  {runhead}
  <div class="pad">
    {p3}
    <div class="scorehead">
      <h2>Your Family Legacy Profile</h2>
      <p>Transfer each section score below, then shade the bar to see the shape of your family\u2019s legacy at a glance.</p>
    </div>
    <div class="prof">{prof}</div>
    <div class="shade">Shade one cell per point \u00b7 20 cells = full section score</div>
    <div class="total"><span class="k">Total Score</span><span class="bx"></span>
      <span class="of">/ 120</span></div>
    <div class="bands">{bands}</div>
    <div class="qbox">
      <div class="lbl">Choosing Your First Priority</div>
      <div class="intro">{discern}</div>
      <div class="qs">{qs}</div>
    </div>
  </div>
  {foot3}
</div>

</body></html>""".format(css=CSS, tm=TM, subtitle=SUBTITLE, deck=DECK, aud=AUDIENCE, chips=chips,
                         preamble=PREAMBLE, instr_short="answer for today, not someday",
                         keyrow=keyrow, p1=p1, p2=p2, p3=p3, prof=prof, bands=bands,
                         discern=DISCERN_INTRO, qs=qs, runhead=RUNHEAD,
                         foot1=foot(1), foot2=foot(2), foot3=foot(3))
