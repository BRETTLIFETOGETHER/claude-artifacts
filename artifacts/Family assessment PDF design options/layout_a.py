# -*- coding: utf-8 -*-
"""Layout A — Heritage Edition. Navy + brass, cream stock, Lora serif."""
from content import *

CSS = """
@page {
  size: Letter;
  margin: 0.55in 0.62in 0.5in 0.62in;
  @bottom-left { content: "Family Legacy Intelligence\\2122  \\00B7  10-Minute Family Assessment";
    font-family: 'Poppins'; font-size: 6.4pt; letter-spacing: .09em;
    text-transform: uppercase; color: #9C8B72; }
  @bottom-right { content: counter(page) " of 3";
    font-family: 'Poppins'; font-size: 6.4pt; letter-spacing: .09em; color: #9C8B72; }
}
* { box-sizing: border-box; }
html { background: #FBF8F2; }
body { margin: 0; font-family: 'Lora'; color: #1B2E45; background: #FBF8F2;
       font-size: 8.9pt; line-height: 1.32; }
.page { page-break-after: always; }
.page.last { page-break-after: auto; }

/* ---------- masthead ---------- */
.mast { text-align: center; padding-bottom: 9pt; }
.rule-dbl { border-top: 2.6pt solid #14263C; border-bottom: 0.7pt solid #14263C;
            height: 3.2pt; margin-bottom: 11pt; }
.eyebrow { font-family: 'Poppins'; font-weight: 500; font-size: 7pt; letter-spacing: .28em;
           text-transform: uppercase; color: #A67C3D; }
h1 { font-family: 'Lora'; font-weight: 600; font-size: 25pt; letter-spacing: -.005em;
     margin: 5pt 0 0; color: #14263C; line-height: 1.05; }
.sub { font-family: 'Lora'; font-style: italic; font-size: 11.2pt; color: #4A6178; margin-top: 4pt; }
.orn { margin: 8pt auto 7pt; width: 88pt; border-top: .7pt solid #C9B99C; position: relative; }
.orn:after { content: "\\2726"; position: absolute; top: -6.5pt; left: 50%; margin-left: -5pt;
             color: #A67C3D; font-size: 8pt; background: #FBF8F2; padding: 0 4pt; }
.deck { font-size: 9.4pt; color: #2E465C; max-width: 5.2in; margin: 0 auto; line-height: 1.45; }
.aud { font-family: 'Poppins'; font-size: 6.6pt; letter-spacing: .17em; text-transform: uppercase;
       color: #8A7455; margin-top: 8pt; }

/* ---------- intro / instructions ---------- */
.intro { display: flex; gap: 16pt; margin: 12pt 0 13pt; padding: 11pt 13pt;
         background: #F4EFE4; border-left: 2.4pt solid #A67C3D; }
.intro p { margin: 0; font-size: 8.2pt; line-height: 1.44; color: #3A4F63; }
.intro .col-a { flex: 1.32; }
.intro .col-b { flex: 1; border-left: .7pt solid #DCCFB6; padding-left: 14pt; }
.lbl { font-family: 'Poppins'; font-weight: 600; font-size: 6.6pt; letter-spacing: .2em;
       text-transform: uppercase; color: #A67C3D; margin-bottom: 4pt; }
.scale-key { list-style: none; margin: 0; padding: 0; }
.scale-key li { font-size: 7.7pt; color: #3A4F63; margin-bottom: 1.6pt; }
.scale-key b { font-family: 'Poppins'; font-weight: 600; color: #14263C; font-size: 7pt;
               display: inline-block; width: 12pt; }

/* ---------- sections ---------- */
.section { margin-top: 13pt; break-inside: avoid; }
.sec-head { display: flex; align-items: flex-start; gap: 9pt;
            border-bottom: 1.1pt solid #14263C; padding-bottom: 5pt; }
.num { width: 21pt; height: 21pt; flex: none; border: .9pt solid #A67C3D; border-radius: 50%;
       color: #A67C3D; font-family: 'Lora'; font-weight: 600; font-size: 9.5pt;
       text-align: center; line-height: 19.5pt; }
.sec-title { font-family: 'Lora'; font-weight: 600; font-size: 12.6pt; color: #14263C;
             line-height: 1.12; margin: 1pt 0 0; }
.sec-q { font-style: italic; font-size: 8.4pt; color: #6A7F92; margin-top: 2.5pt; }
.stmt { display: flex; align-items: baseline; gap: 8pt; padding: 5.4pt 0 4.6pt;
        border-bottom: .5pt dotted #C9B99C; }
.stmt .t { flex: 1; font-size: 8.9pt; line-height: 1.34; }
.stmt .i { font-family: 'Poppins'; font-weight: 500; font-size: 6.6pt; color: #B09A78;
           flex: none; width: 12pt; }
.scale { flex: none; white-space: nowrap; }
.scale i { display: inline-block; width: 14.5pt; height: 14.5pt; border: .8pt solid #A9BACB;
           border-radius: 50%; margin-left: 3.2pt; font-family: 'Poppins'; font-style: normal;
           font-size: 6.9pt; color: #7C93A8; text-align: center; line-height: 13.2pt; }
.sec-score { display: flex; justify-content: flex-end; align-items: center; gap: 8pt;
             margin-top: 6pt; }
.sec-score .k { font-family: 'Poppins'; font-weight: 600; font-size: 6.8pt; letter-spacing: .16em;
                text-transform: uppercase; color: #14263C; }
.sec-score .v { font-family: 'Lora'; font-size: 9.5pt; color: #14263C;
                border-bottom: 1pt solid #14263C; width: 46pt; text-align: center; }
.sec-score .d { font-family: 'Lora'; font-size: 9pt; color: #8A7455; }

/* ---------- page 3 scoring ---------- */
.divide { margin: 16pt 0 0; border-top: 2.6pt solid #14263C; border-bottom: .7pt solid #14263C;
          height: 3.2pt; }
h2 { font-family: 'Lora'; font-weight: 600; font-size: 15pt; color: #14263C;
     margin: 12pt 0 2pt; text-align: center; }
.h2sub { font-style: italic; font-size: 8.4pt; color: #6A7F92; text-align: center;
         margin-bottom: 10pt; }
.score-grid { width: 100%; border-collapse: collapse; }
.score-grid td { padding: 5.2pt 0; border-bottom: .5pt dotted #C9B99C; font-size: 9pt;
                 vertical-align: middle; }
.score-grid td.rn { width: 26pt; font-family: 'Poppins'; font-weight: 600; font-size: 7pt;
                    color: #A67C3D; letter-spacing: .1em; }
.score-grid td.sc { width: 82pt; text-align: right; }
.score-grid .box { display: inline-block; width: 40pt; border-bottom: 1pt solid #14263C;
                   height: 12pt; }
.score-grid .of { font-size: 8.4pt; color: #8A7455; margin-left: 5pt; }
.total { display: flex; align-items: center; justify-content: space-between;
         margin-top: 11pt; padding: 9pt 14pt; background: #14263C; color: #FBF8F2; }
.total .k { font-family: 'Poppins'; font-weight: 600; font-size: 8pt; letter-spacing: .2em;
            text-transform: uppercase; }
.total .v { font-family: 'Lora'; font-size: 12pt; }
.total .v span { display: inline-block; width: 62pt; border-bottom: 1pt solid #C9A66B;
                 margin-right: 5pt; }
.two { display: flex; gap: 18pt; margin-top: 13pt; }
.two > div { flex: 1; }
.qlist { list-style: none; margin: 6pt 0 0; padding: 0; counter-reset: q; }
.qlist li { position: relative; padding-left: 17pt; margin-bottom: 6pt; font-size: 8.5pt;
            line-height: 1.38; counter-increment: q; }
.qlist li:before { content: counter(q); position: absolute; left: 0; top: -.5pt;
                   font-family: 'Lora'; font-weight: 600; font-size: 10.5pt; color: #C9A66B; }
.band { padding: 5.6pt 0; border-top: .5pt dotted #C9B99C; }
.band:first-of-type { border-top: none; padding-top: 1pt; }
.band .r { font-family: 'Poppins'; font-weight: 600; font-size: 7pt; letter-spacing: .12em;
           color: #A67C3D; }
.band .n { font-family: 'Lora'; font-weight: 600; font-size: 9.4pt; color: #14263C; }
.band .d { font-size: 7.7pt; color: #56697D; line-height: 1.36; margin-top: 1.5pt; }
.closing { margin-top: 14pt; text-align: center; font-style: italic; font-size: 8.6pt;
           color: #4A6178; border-top: .7pt solid #C9B99C; padding-top: 9pt; }
"""


def stmt_rows(sec):
    out = []
    for i, s in enumerate(sec["items"], 1):
        out.append(
            '<div class="stmt"><div class="i">{:02d}</div><div class="t">{}</div>'
            '<div class="scale"><i>1</i><i>2</i><i>3</i><i>4</i><i>5</i></div></div>'.format(i, s))
    return "".join(out)


def section_html(sec):
    return """
<div class="section">
  <div class="sec-head">
    <div class="num">{roman}</div>
    <div>
      <div class="sec-title">{title}</div>
      <div class="sec-q">{q}</div>
    </div>
  </div>
  {rows}
  <div class="sec-score"><span class="k">Section Score</span><span class="v">&nbsp;</span><span class="d">/ 20</span></div>
</div>""".format(roman=sec["roman"], title=sec["title"], q=sec["q"], rows=stmt_rows(sec))


def build():
    scale_key = "".join('<li><b>{}</b>{}</li>'.format(k, v) for k, v in SCALE)
    p1_sections = "".join(section_html(SECTIONS[i]) for i in GROUPS[0])
    p2_sections = "".join(section_html(SECTIONS[i]) for i in GROUPS[1])
    p3_sections = "".join(section_html(SECTIONS[i]) for i in GROUPS[2])

    rows = "".join(
        '<tr><td class="rn">{roman}</td><td>{t}</td>'
        '<td class="sc"><span class="box"></span><span class="of">/ 20</span></td></tr>'.format(
            roman=s["roman"], t=s["short"]) for s in SECTIONS)

    bands = "".join(
        '<div class="band"><span class="r">{r}</span> &nbsp;<span class="n">{n}</span>'
        '<div class="d">{d}</div></div>'.format(r=r, n=n, d=d) for r, n, d in BANDS)

    questions = "".join('<li>{}</li>'.format(q) for q in QUESTIONS)

    return """<!DOCTYPE html><html><head><meta charset="utf-8"><style>{css}</style></head><body>

<div class="page">
  <div class="rule-dbl"></div>
  <div class="mast">
    <div class="eyebrow">Family Legacy Intelligence{tm}</div>
    <h1>{subtitle}</h1>
    <div class="orn"></div>
    <div class="deck">{deck}</div>
    <div class="aud">{aud}</div>
  </div>
  <div class="intro">
    <div class="col-a">
      <div class="lbl">Before You Begin</div>
      <p>{preamble}</p>
      <p style="margin-top:6pt">{instructions}</p>
    </div>
    <div class="col-b">
      <div class="lbl">The Scale</div>
      <ul class="scale-key">{scale_key}</ul>
    </div>
  </div>
  {p1}
</div>

<div class="page">{p2}</div>

<div class="page last">
  {p3}
  <div class="divide"></div>
  <h2>Discerning Your First Legacy Priority</h2>
  <div class="h2sub">Carry each section score into the summary below.</div>
  <table class="score-grid">{rows}</table>
  <div class="total"><span class="k">Total Score</span><span class="v"><span></span>/ 120</span></div>
  <div class="two">
    <div>
      <div class="lbl">Three Questions to Weigh</div>
      <p style="font-size:8.1pt;line-height:1.4;color:#56697D;margin:5pt 0 0">{discern}</p>
      <ol class="qlist">{questions}</ol>
    </div>
    <div>
      <div class="lbl">Reading Your Total</div>
      <div style="margin-top:5pt">{bands}</div>
    </div>
  </div>
  <div class="closing">A family does not drift into legacy. It is chosen, spoken, and passed forward on purpose.</div>
</div>

</body></html>""".format(css=CSS, tm=TM, subtitle=SUBTITLE, deck=DECK, aud=AUDIENCE,
                         preamble=PREAMBLE, instructions=INSTRUCTIONS, scale_key=scale_key,
                         p1=p1_sections, p2=p2_sections, p3=p3_sections, rows=rows,
                         discern=DISCERN_INTRO, questions=questions, bands=bands)
