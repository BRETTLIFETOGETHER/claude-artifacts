# -*- coding: utf-8 -*-
"""Layout C — Private Client Edition. Airy, sage + clay, Pagella serif, tick squares."""
from content import *

SAGE = "#63745E"
CLAY = "#A2775A"
INK = "#26302B"

CSS = """
@page {
  size: Letter; margin: 0.6in 0.68in 0.55in 0.68in;
  @bottom-left { content: "Family Legacy Intelligence\\2122";
    font-family: 'Poppins Light'; font-size: 6.2pt; letter-spacing: .22em;
    text-transform: uppercase; color: #A9AFA4; }
  @bottom-center { content: "\\2014  " counter(page) "  \\2014";
    font-family: 'Poppins Light'; font-size: 6.2pt; letter-spacing: .18em; color: #A9AFA4; }
  @bottom-right { content: "A Ten-Minute Conversation";
    font-family: 'Poppins Light'; font-size: 6.2pt; letter-spacing: .22em;
    text-transform: uppercase; color: #A9AFA4; }
}
* { box-sizing: border-box; }
body { margin: 0; font-family: 'TeX Gyre Pagella'; color: #26302B;
       font-size: 9.2pt; line-height: 1.38; }
.page { page-break-after: always; }
.page.last { page-break-after: auto; }
.trk { font-family: 'Poppins Light'; font-size: 6.6pt; letter-spacing: .3em;
       text-transform: uppercase; color: #A2775A; }

/* ---------- masthead ---------- */
.mast { padding-bottom: 4pt; }
.mast h1 { font-family: 'TeX Gyre Pagella'; font-weight: normal; font-size: 30pt;
           line-height: 1.02; margin: 12pt 0 0; color: #26302B; letter-spacing: -.012em; }
.mast h1 em { font-style: italic; color: #63745E; }
.hair { border-top: .6pt solid #D3D8CE; margin: 15pt 0 0; }
.deck { font-style: italic; font-size: 11pt; line-height: 1.45; color: #4E5A50;
        max-width: 4.9in; margin-top: 11pt; }
.aud { font-family: 'Poppins Light'; font-size: 6.4pt; letter-spacing: .2em;
       text-transform: uppercase; color: #8C9487; margin-top: 12pt; }

/* ---------- opening columns ---------- */
.open { display: flex; gap: 26pt; margin: 16pt 0 4pt; }
.open .a { flex: 1.4; }
.open .b { flex: 1; }
.open p { margin: 6pt 0 0; font-size: 8.6pt; line-height: 1.5; color: #48534A; }
.key { list-style: none; margin: 7pt 0 0; padding: 0; }
.key li { display: flex; gap: 8pt; padding: 2.6pt 0; border-bottom: .5pt solid #E6E9E1;
          font-size: 8.2pt; color: #48534A; }
.key li b { font-family: 'Poppins Light'; font-weight: normal; font-size: 8pt; color: #A2775A;
            width: 9pt; flex: none; }

/* ---------- sections ---------- */
.section { margin-top: 21pt; break-inside: avoid; }
.sec-head { display: flex; align-items: flex-start; gap: 13pt; }
.sec-head .no { font-family: 'Poppins Light'; font-weight: normal; font-size: 21pt;
                color: #C8D0C2; line-height: .92; flex: none; width: 30pt; letter-spacing: -.02em; }
.sec-head .tt { flex: 1; }
.sec-head .t { font-size: 14pt; line-height: 1.12; color: #26302B; letter-spacing: -.01em; }
.sec-head .q { font-style: italic; font-size: 8.6pt; color: #7A8579; margin-top: 3pt; }
.colhead { display: flex; justify-content: flex-end; align-items: center;
           margin: 9pt 0 1pt; border-bottom: .6pt solid #63745E; padding-bottom: 3.5pt; }
.colhead .lead { flex: 1; font-family: 'Poppins Light'; font-size: 6.2pt; letter-spacing: .22em;
                 text-transform: uppercase; color: #A9AFA4; }
.colhead u { display: block; width: 16pt; margin-left: 5pt; text-decoration: none;
             font-family: 'Poppins Light'; font-size: 6.6pt; color: #8C9487; text-align: center; }
.stmt { display: flex; align-items: center; padding: 7.2pt 0; border-bottom: .5pt solid #E6E9E1; }
.stmt .t { flex: 1; font-size: 9.1pt; line-height: 1.34; padding-right: 12pt; }
.stmt u { display: block; width: 16pt; height: 16pt; margin-left: 5pt; flex: none;
          border: .7pt solid #C0C7BA; text-decoration: none; }
.sec-score { display: flex; justify-content: flex-end; align-items: center; gap: 9pt;
             margin-top: 9pt; }
.sec-score .k { font-family: 'Poppins Light'; font-size: 6.4pt; letter-spacing: .22em;
                text-transform: uppercase; color: #63745E; }
.sec-score .v { width: 44pt; height: 17pt; border: .8pt solid #A2775A; }
.sec-score .d { font-size: 8.6pt; color: #8C9487; }

/* ---------- continuation head ---------- */
.runhead { display: flex; justify-content: space-between; align-items: baseline;
           border-bottom: .6pt solid #D3D8CE; padding-bottom: 5pt; }
.runhead .a { font-family: 'Poppins Light'; font-size: 6.6pt; letter-spacing: .3em;
              text-transform: uppercase; color: #A2775A; }
.runhead .b { font-style: italic; font-size: 8.6pt; color: #8C9487; }

/* ---------- scoring ---------- */
.scoretop { margin-top: 22pt; border-top: .6pt solid #D3D8CE; padding-top: 15pt; }
h2 { font-family: 'TeX Gyre Pagella'; font-weight: normal; font-size: 18pt; margin: 5pt 0 0;
     color: #26302B; letter-spacing: -.012em; }
h2 em { font-style: italic; color: #63745E; }
.sgrid { width: 100%; border-collapse: collapse; margin-top: 11pt; }
.sgrid td { padding: 5.6pt 0; border-bottom: .5pt solid #E6E9E1; font-size: 9pt; }
.sgrid td.no { width: 24pt; font-family: 'Poppins Light'; font-size: 7.4pt; color: #C0C7BA; }
.sgrid td.sc { width: 74pt; text-align: right; }
.sgrid .bx { display: inline-block; width: 40pt; height: 15pt; border: .7pt solid #C0C7BA;
             vertical-align: middle; }
.sgrid .of { font-size: 8.4pt; color: #8C9487; margin-left: 6pt; }
.total { display: flex; align-items: center; justify-content: flex-end; gap: 10pt;
         margin-top: 12pt; border-top: 1.6pt solid #26302B; border-bottom: .6pt solid #26302B;
         padding: 9pt 0; }
.total .k { flex: 1; font-family: 'Poppins Light'; font-size: 7.4pt; letter-spacing: .28em;
            text-transform: uppercase; color: #26302B; }
.total .bx { width: 54pt; height: 20pt; border: .8pt solid #A2775A; }
.total .of { font-size: 10pt; color: #8C9487; }
.two { display: flex; gap: 26pt; margin-top: 16pt; }
.two > div { flex: 1; }
.qlist { list-style: none; margin: 8pt 0 0; padding: 0; counter-reset: q; }
.qlist li { position: relative; padding-left: 19pt; margin-bottom: 7pt; font-size: 8.8pt;
            line-height: 1.4; counter-increment: q; }
.qlist li:before { content: "0" counter(q); position: absolute; left: 0; top: .8pt;
                   font-family: 'Poppins Light'; font-size: 7pt; color: #A2775A;
                   letter-spacing: .06em; }
.band { padding: 6pt 0; border-bottom: .5pt solid #E6E9E1; }
.band .r { font-family: 'Poppins Light'; font-size: 7pt; letter-spacing: .16em; color: #A2775A; }
.band .n { font-size: 9.6pt; color: #26302B; margin-top: 1pt; }
.band .d { font-size: 7.8pt; color: #6E7A6D; line-height: 1.38; margin-top: 2pt; }
.close { margin-top: 17pt; text-align: center; }
.close .q { font-style: italic; font-size: 10pt; color: #4E5A50; }
.close .s { font-family: 'Poppins Light'; font-size: 6.4pt; letter-spacing: .26em;
            text-transform: uppercase; color: #A9AFA4; margin-top: 6pt; }
"""


def stmt_rows(sec):
    return "".join(
        '<div class="stmt"><div class="t">{}</div><u></u><u></u><u></u><u></u><u></u></div>'.format(s)
        for s in sec["items"])


def section_html(sec):
    return """
<div class="section">
  <div class="sec-head">
    <div class="no">{no:02d}</div>
    <div class="tt"><div class="t">{title}</div><div class="q">{q}</div></div>
  </div>
  <div class="colhead"><div class="lead">Rate each statement</div>
    <u>1</u><u>2</u><u>3</u><u>4</u><u>5</u></div>
  {rows}
  <div class="sec-score"><span class="k">Section Score</span><span class="v"></span><span class="d">/ 20</span></div>
</div>""".format(no=sec["n"], title=sec["title"], q=sec["q"], rows=stmt_rows(sec))


RUNHEAD = ('<div class="runhead"><div class="a">Family Legacy Intelligence{tm}</div>'
           '<div class="b">The Ten-Minute Family Legacy Assessment</div></div>').format(tm=TM)


def build():
    key = "".join('<li><b>{}</b><span>{}</span></li>'.format(k, v) for k, v in SCALE)
    p1 = "".join(section_html(SECTIONS[i]) for i in GROUPS[0])
    p2 = "".join(section_html(SECTIONS[i]) for i in GROUPS[1])
    p3 = "".join(section_html(SECTIONS[i]) for i in GROUPS[2])

    rows = "".join(
        '<tr><td class="no">{no:02d}</td><td>{t}</td>'
        '<td class="sc"><span class="bx"></span><span class="of">/ 20</span></td></tr>'.format(
            no=s["n"], t=s["short"]) for s in SECTIONS)

    bands = "".join(
        '<div class="band"><div class="r">{r}</div><div class="n">{n}</div>'
        '<div class="d">{d}</div></div>'.format(r=r, n=n, d=d) for r, n, d in BANDS)

    questions = "".join('<li>{}</li>'.format(q) for q in QUESTIONS)

    return """<!DOCTYPE html><html><head><meta charset="utf-8"><style>{css}</style></head><body>

<div class="page">
  <div class="mast">
    <div class="trk">Family Legacy Intelligence{tm}</div>
    <h1>The Ten-Minute<br><em>Family Legacy</em> Assessment</h1>
    <div class="hair"></div>
    <div class="deck">{deck}</div>
    <div class="aud">{aud}</div>
  </div>
  <div class="open">
    <div class="a"><div class="trk">Before You Begin</div><p>{preamble}</p></div>
    <div class="b"><div class="trk">The Scale</div><ul class="key">{key}</ul></div>
  </div>
  {p1}
</div>

<div class="page">{runhead}{p2}</div>

<div class="page last">
  {runhead}
  {p3}
  <div class="scoretop">
    <div class="trk">Discerning Your First Legacy Priority</div>
    <h2>Where does your family <em>begin?</em></h2>
    <table class="sgrid">{rows}</table>
    <div class="total"><span class="k">Total Score</span><span class="bx"></span><span class="of">/ 120</span></div>
    <div class="two">
      <div>
        <div class="trk">Three Questions</div>
        <p style="font-size:8.2pt;line-height:1.45;color:#6E7A6D;margin:7pt 0 0">{discern}</p>
        <ol class="qlist">{questions}</ol>
      </div>
      <div>
        <div class="trk">Reading Your Total</div>
        <div style="margin-top:6pt">{bands}</div>
      </div>
    </div>
    <div class="close">
      <div class="q">&ldquo;Have we prepared the people as carefully as we have prepared the documents?&rdquo;</div>
      <div class="s">Legacy by design, not by default</div>
    </div>
  </div>
</div>

</body></html>""".format(css=CSS, tm=TM, deck=DECK, aud=AUDIENCE, preamble=PREAMBLE, key=key,
                         p1=p1, p2=p2, p3=p3, rows=rows, discern=DISCERN_INTRO,
                         questions=questions, bands=bands, runhead=RUNHEAD)
