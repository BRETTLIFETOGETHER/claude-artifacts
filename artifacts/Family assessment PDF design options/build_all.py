# -*- coding: utf-8 -*-
import os
from weasyprint import HTML
from pypdf import PdfReader
from fli_data import *
from fli_theme import BASE, wheel_svg, chips_html, foot, rhead, lines

OUT = "/mnt/user-data/outputs"
os.makedirs(OUT, exist_ok=True)

# ===================================================================== styles
COVER_CSS = """
.cover { background: #16233A; height: 11in; color: #fff; padding: 0.95in 0.72in 0; position: relative; }
.cover .brand { font-weight: 600; font-size: 7.4pt; letter-spacing: .3em; text-transform: uppercase;
                color: #86A6D6; }
.cover .goldrule { width: 46pt; border-top: 2.2pt solid #C9A66B; margin: 13pt 0 22pt; }
.cover .kick { font-family: 'Lora'; font-style: italic; font-size: 11pt; color: #C9A66B; }
.cover h1 { font-family: 'Lora'; font-weight: 600; font-size: 33pt; line-height: 1.06;
            margin: 9pt 0 0; letter-spacing: -.015em; }
.cover .promise { font-family: 'Lora'; font-size: 12.4pt; line-height: 1.5; color: #C8D6E8;
                  max-width: 4.9in; margin-top: 17pt; }
.cover .chips { display: flex; margin-top: 30pt; }
.cover .chips div { flex: 1; height: 9pt; }
.cover .base { position: absolute; bottom: 0.8in; left: 0.72in; right: 0.72in; }
.cover .base .l { font-weight: 500; font-size: 7pt; letter-spacing: .18em; text-transform: uppercase;
                  color: #7E9CC9; }
.cover .base .n { font-family: 'Lora'; font-style: italic; font-size: 9.4pt; color: #A9BFDA;
                  margin-top: 7pt; max-width: 4.6in; line-height: 1.5; }
.cover .idx { display: flex; gap: 0; margin-top: 26pt; border-top: .7pt solid rgba(255,255,255,.22);
              padding-top: 11pt; }
.cover .idx div { flex: 1; font-size: 6.8pt; letter-spacing: .06em; color: #8FA9C9; padding-right: 8pt; }
.cover .idx b { display: block; font-weight: 600; color: #fff; font-size: 7.2pt;
                letter-spacing: .16em; text-transform: uppercase; margin-bottom: 3pt; }
"""

BROCHURE_CSS = COVER_CSS + """
.probs { margin-top: 4pt; }
.prob { display: flex; gap: 13pt; padding: 11pt 0; border-bottom: .6pt solid #EDF0F3; }
.prob .n { font-family: 'Lora'; font-weight: 600; font-size: 15pt; color: #D8DFE6; flex: none;
           width: 26pt; line-height: 1; }
.prob .t { flex: 1; }
.prob .h { font-family: 'Lora'; font-weight: 600; font-size: 11.4pt; color: #16233A;
           line-height: 1.2; }
.prob .d { font-size: 8.4pt; line-height: 1.48; color: #55616F; margin-top: 3.5pt; }

.pairs { display: flex; flex-wrap: wrap; margin-top: 6pt; }
.pair { width: 50%; padding: 9pt 14pt 9pt 0; }
.pair .row { display: flex; align-items: baseline; gap: 7pt; }
.pair .a { font-family: 'Lora'; font-weight: 600; font-size: 13pt; color: #16233A; }
.pair .b { font-size: 7.4pt; letter-spacing: .1em; text-transform: uppercase; color: #A9B4C0; }
.pair .c { font-family: 'Lora'; font-style: italic; font-size: 11pt; color: #7C8794; }
.pair .u { border-top: .6pt solid #EDF0F3; margin-top: 8pt; }

.quote { background: #F4F6F9; border-left: 2.6pt solid #C9A66B; padding: 13pt 16pt;
         margin-top: 14pt; }
.quote .q { font-family: 'Lora'; font-style: italic; font-size: 10.6pt; line-height: 1.5;
            color: #2B3440; }
.quote .a { font-weight: 500; font-size: 6.6pt; letter-spacing: .2em; text-transform: uppercase;
            color: #8A96A3; margin-top: 8pt; }

.wheelbox { margin-top: 10pt; padding: 6pt 0 0; }
.dims { display: flex; flex-wrap: wrap; margin-top: 8pt; }
.dim { width: 33.33%; padding: 8pt 12pt 8pt 0; }
.dim .h { display: flex; align-items: center; gap: 6pt; }
.dim .sw { width: 8pt; height: 8pt; border-radius: 2pt; flex: none; }
.dim .n { font-weight: 600; font-size: 8.2pt; color: #16233A; line-height: 1.2; }
.dim .q { font-family: 'Lora'; font-style: italic; font-size: 7.4pt; color: #6E7A87;
          margin-top: 3pt; line-height: 1.38; }

.ladder { display: flex; gap: 7pt; margin-top: 11pt; }
.ladder .c { flex: 1; border-top: 2.6pt solid; padding: 7pt 0 0; }
.ladder .r { font-family: 'Lora'; font-weight: 600; font-size: 11pt; }
.ladder .n { font-weight: 600; font-size: 7.2pt; color: #16233A; margin-top: 2pt; line-height: 1.22; }
.ladder .d { font-size: 6.4pt; line-height: 1.36; color: #5A6675; margin-top: 3pt; }

.inst { margin-top: 13pt; border: .6pt solid #E3E8ED; border-radius: 3pt; overflow: hidden; }
.inst .top { display: flex; align-items: center; gap: 10pt; padding: 8pt 12pt; color: #fff; }
.inst .top .no { font-family: 'Lora'; font-weight: 600; font-size: 13pt;
                 color: rgba(255,255,255,.55); flex: none; }
.inst .top .nm { flex: 1; font-weight: 600; font-size: 11pt; letter-spacing: -.01em; }
.inst .top .tm { font-size: 6.4pt; letter-spacing: .12em; text-transform: uppercase;
                 color: rgba(255,255,255,.8); flex: none; }
.inst .body { display: flex; gap: 14pt; padding: 10pt 12pt 11pt; }
.inst .body .col { flex: 1; }
.inst .lb { font-weight: 600; font-size: 6.2pt; letter-spacing: .2em; text-transform: uppercase;
            color: #9AA5B1; margin-bottom: 4pt; }
.inst .body p { margin: 0; font-size: 8pt; line-height: 1.45; color: #46536A; }
.inst ul { margin: 0; padding: 0; list-style: none; }
.inst li { font-size: 7.6pt; line-height: 1.4; color: #46536A; padding-left: 9pt;
           position: relative; margin-bottom: 2.6pt; }
.inst li:before { content: "\\2022"; position: absolute; left: 0; color: #C0C9D3; }

.jrn { display: flex; flex-wrap: wrap; margin-top: 6pt; }
.jcard { width: 50%; padding: 10pt 12pt 10pt 0; }
.jcard .in { border-top: 2.6pt solid; padding-top: 8pt; }
.jcard .k { font-weight: 600; font-size: 6.4pt; letter-spacing: .18em; text-transform: uppercase; }
.jcard .t { font-family: 'Lora'; font-weight: 600; font-style: italic; font-size: 13pt;
            color: #16233A; margin-top: 4pt; line-height: 1.16; }
.jcard .s { font-size: 7.2pt; color: #7C8794; margin-top: 3pt; }
.jcard ul { margin: 6pt 0 0; padding: 0; list-style: none; }
.jcard li { font-size: 7.3pt; line-height: 1.44; color: #55616F; padding-left: 9pt;
            position: relative; }
.jcard li:before { content: "\\2013"; position: absolute; left: 0; color: #C0C9D3; }

.steps { margin-top: 4pt; }
.step { display: flex; gap: 12pt; padding: 7.4pt 0; border-bottom: .6pt solid #EDF0F3; }
.step .n { width: 19pt; height: 19pt; flex: none; border-radius: 50%; background: #16233A;
           color: #fff; font-weight: 600; font-size: 7.4pt; text-align: center; line-height: 19pt; }
.step .t { flex: 1; }
.step .h { font-weight: 600; font-size: 9pt; color: #16233A; }
.step .d { font-size: 7.8pt; line-height: 1.44; color: #55616F; margin-top: 1.5pt; }

.caps { display: flex; flex-wrap: wrap; margin-top: 7pt; }
.caps div { width: 33.33%; font-size: 7.6pt; color: #46536A; padding: 3.4pt 10pt 3.4pt 10pt;
            position: relative; }
.caps div:before { content: "\\2713"; position: absolute; left: 0; color: #A9B4C0; font-size: 7pt; }

.finale { background: #16233A; color: #fff; padding: 26pt 0.72in; margin-top: 16pt; }
.finale .k { font-weight: 600; font-size: 6.8pt; letter-spacing: .26em; text-transform: uppercase;
             color: #C9A66B; }
.finale h2 { font-family: 'Lora'; font-weight: 600; font-size: 21pt; line-height: 1.14;
             margin: 8pt 0 0; letter-spacing: -.014em; }
.finale p { font-family: 'Lora'; font-size: 10.4pt; line-height: 1.55; color: #C8D6E8;
            margin: 12pt 0 0; max-width: 5.2in; }
.conf { border: .6pt solid #E3E8ED; border-left: 2.6pt solid #B85C3B; padding: 11pt 14pt;
        margin-top: 14pt; }
.conf .k { font-weight: 600; font-size: 6.4pt; letter-spacing: .2em; text-transform: uppercase;
           color: #B85C3B; }
.conf p { margin: 5pt 0 0; font-size: 8.2pt; line-height: 1.48; color: #46536A; }
"""

INTERVIEW_CSS = COVER_CSS + """
.cover.iv { background: #16233A; }
.why { margin-top: 2pt; }
.why .b { padding: 12pt 0; border-bottom: .6pt solid rgba(255,255,255,.16); }
.why .h { font-weight: 600; font-size: 7pt; letter-spacing: .2em; text-transform: uppercase;
          color: #C9A66B; }
.why p { margin: 5pt 0 0; font-size: 8.8pt; line-height: 1.52; color: #C8D6E8; max-width: 5.1in; }
.how { margin-top: 14pt; }
.how .h { font-weight: 600; font-size: 7pt; letter-spacing: .2em; text-transform: uppercase;
          color: #C9A66B; }
.how ul { margin: 7pt 0 0; padding: 0; list-style: none; display: flex; flex-wrap: wrap; }
.how li { width: 50%; font-size: 8.2pt; line-height: 1.42; color: #C8D6E8; padding: 4pt 14pt 4pt 12pt;
          position: relative; }
.how li:before { content: "\\2014"; position: absolute; left: 0; color: #6E8BB0; }
.perm { border: .7pt solid rgba(255,255,255,.28); padding: 11pt 13pt; margin-top: 15pt; }
.perm .h { font-weight: 600; font-size: 6.4pt; letter-spacing: .2em; text-transform: uppercase;
           color: #86A6D6; }
.perm p { margin: 5pt 0 0; font-family: 'Lora'; font-style: italic; font-size: 8.6pt;
          line-height: 1.5; color: #C8D6E8; }

.q { margin-top: 17pt; break-inside: avoid; }
.q .hd { display: flex; gap: 12pt; align-items: flex-start; }
.q .no { font-family: 'Lora'; font-weight: 600; font-size: 15pt; flex: none; width: 27pt;
         line-height: 1.02; }
.q .tx { flex: 1; }
.q .t { font-family: 'Lora'; font-weight: 600; font-size: 12pt; line-height: 1.24; color: #16233A;
        letter-spacing: -.008em; }
.q .p { font-size: 7.8pt; line-height: 1.44; color: #7C8794; margin-top: 4pt; }
.q .sp { margin: 9pt 0 0 39pt; }
.stmtbox { margin-top: 18pt; }
.stmtbox .k { font-weight: 600; font-size: 6.8pt; letter-spacing: .24em; text-transform: uppercase; }
.stmtbox h3 { font-family: 'Lora'; font-weight: 600; font-size: 16pt; color: #16233A;
              margin: 5pt 0 0; letter-spacing: -.012em; }
.pr { margin-top: 13pt; }
.pr .l { font-family: 'Lora'; font-style: italic; font-size: 10pt; color: #2B3440; margin-bottom: 6pt; }
"""

ASSESS_CSS = COVER_CSS + """
.hero { background: #16233A; color: #fff; padding: 30pt 0.72in 0; }
.hero .eyebrow { font-weight: 600; font-size: 7pt; letter-spacing: .3em; text-transform: uppercase;
                 color: #86A6D6; }
.hero h1 { font-family: 'Lora'; font-weight: 600; font-size: 27pt; line-height: 1.06;
           margin: 8pt 0 0; letter-spacing: -.015em; }
.hero .deck { font-family: 'Lora'; font-size: 10.4pt; line-height: 1.48; color: #C8D6E8;
              max-width: 5.2in; margin-top: 8pt; }
.hero .chips { display: flex; margin-top: 16pt; }
.hero .chips div { flex: 1; height: 8pt; }
.howto { background: #F4F6F9; padding: 12pt 0.72in 13pt; display: flex; gap: 20pt; }
.howto .a { flex: 1.2; }
.howto .b { flex: 1; }
.lb { font-weight: 600; font-size: 6.4pt; letter-spacing: .2em; text-transform: uppercase;
      color: #16233A; margin-bottom: 5pt; }
.howto p { margin: 0; font-size: 8pt; line-height: 1.46; color: #46536A; }
.keyrow { display: flex; gap: 5pt; }
.keyrow > div { flex: 1; text-align: center; }
.keyrow .n { width: 15pt; height: 15pt; margin: 0 auto 3pt; border-radius: 50%;
             background: #16233A; color: #fff; font-weight: 600; font-size: 7pt; line-height: 15pt; }
.keyrow .t { font-size: 6.2pt; line-height: 1.22; color: #46536A; }
.note { font-size: 6.6pt; color: #5A6675; margin-top: 7pt; line-height: 1.34; }

.sec { margin-top: 14pt; break-inside: avoid; }
.sec .hd { display: flex; align-items: center; gap: 9pt; padding: 6pt 11pt; border-radius: 2pt;
           color: #fff; }
.sec .hd .no { width: 17pt; height: 17pt; flex: none; border-radius: 50%;
               background: rgba(255,255,255,.24); font-weight: 600; font-size: 8pt;
               text-align: center; line-height: 17pt; }
.sec .hd .tt { flex: 1; }
.sec .hd .t { font-weight: 600; font-size: 10.6pt; line-height: 1.16; letter-spacing: -.01em; }
.sec .hd .q { font-size: 7.4pt; color: rgba(255,255,255,.88); margin-top: 1pt; }
.rows { border: .6pt solid #E3E8ED; border-top: none; }
.row { display: flex; align-items: center; gap: 8pt; padding: 9.4pt 11pt; }
.row:nth-child(even) { background: #F8FAFB; }
.row .t { flex: 1; font-size: 8.5pt; line-height: 1.34; }
.scale { flex: none; white-space: nowrap; }
.scale i { display: inline-block; width: 14pt; height: 14pt; border: .8pt solid #C4CCD6;
           border-radius: 50%; margin-left: 3pt; font-style: normal; font-size: 6.8pt;
           color: #8B96A3; text-align: center; line-height: 12.6pt; }
.secfoot { display: flex; justify-content: flex-end; align-items: center; gap: 7pt;
           padding: 5.6pt 11pt; border-top: .6pt dashed #D8DFE6; }
.secfoot .k { font-weight: 600; font-size: 6.6pt; letter-spacing: .15em; text-transform: uppercase; }
.secfoot .v { width: 34pt; height: 15pt; border: .9pt solid; border-radius: 2pt; }
.secfoot .d { font-weight: 500; font-size: 7.4pt; color: #7C8794; }

.xfer { margin-top: 13pt; }
.xrow { display: flex; align-items: center; gap: 9pt; padding: 5pt 0;
        border-bottom: .6pt solid #EDF0F3; }
.xrow .sw { width: 8pt; height: 8pt; flex: none; border-radius: 2pt; }
.xrow .nm { flex: 1; font-size: 8.4pt; }
.xrow .bx { width: 34pt; height: 15pt; border: .9pt solid; border-radius: 2pt; flex: none; }
.xrow .of { font-weight: 500; font-size: 7pt; color: #8B96A3; width: 20pt; flex: none; }
.tot { display: flex; align-items: center; gap: 12pt; margin-top: 11pt; padding: 10pt 14pt;
       background: #16233A; border-radius: 3pt; color: #fff; }
.tot .k { font-weight: 600; font-size: 8.4pt; letter-spacing: .2em; text-transform: uppercase;
          flex: 1; }
.tot .bx { width: 54pt; height: 22pt; background: #fff; border-radius: 2pt; }
.tot .of { font-size: 11pt; color: #A9BFDA; }
.q3 { display: flex; gap: 14pt; margin-top: 12pt; }
.q3 .c { flex: 1; }
.q3 .n { font-weight: 600; font-size: 11pt; color: #C0C9D3; }
.q3 .x { font-size: 7.8pt; line-height: 1.4; margin-top: 2pt; }
"""

# ================================================================== brochure
def brochure():
    probs = "".join(
        '<div class="prob"><div class="n">{i:02d}</div><div class="t"><div class="h">{h}</div>'
        '<div class="d">{d}</div></div></div>'.format(i=i, h=h, d=d)
        for i, (h, d) in enumerate(PROBLEMS, 1))

    pairs = "".join(
        '<div class="pair"><div class="row"><span class="a">{a}</span>'
        '<span class="b">before</span><span class="c">{b}</span></div><div class="u"></div></div>'.format(
            a=a, b=b) for a, b in BEFORE_PAIRS)

    dims = "".join(
        '<div class="dim"><div class="h"><span class="sw" style="background:{c}"></span>'
        '<span class="n">{n:02d}. {t}</span></div><div class="q">{q}</div></div>'.format(
            c=d["color"], n=d["n"], t=d["title"], q=d["q"]) for d in DIMENSIONS)

    ladder = "".join(
        '<div class="c" style="border-top-color:{c}"><div class="r" style="color:{c}">{r}</div>'
        '<div class="n">{n}</div><div class="d">{d}</div></div>'.format(r=r, n=n, c=c, d=d)
        for r, n, c, d in BANDS)

    def inst_card(x):
        return """
<div class="inst">
  <div class="top" style="background:{c}"><span class="no">{no}</span>
    <span class="nm">{nm}</span><span class="tm">{tm}</span></div>
  <div class="body">
    <div class="col"><div class="lb">Purpose</div><p>{pp}</p>
      <div class="lb" style="margin-top:9pt">What it produces</div><p>{pr}</p></div>
    <div class="col"><div class="lb">What it surfaces</div><ul>{ss}</ul></div>
  </div>
</div>""".format(c=x["color"], no=x["no"], nm=x["name"], tm=x["time"], pp=x["purpose"],
                 pr=x["produces"], ss="".join("<li>%s</li>" % s for s in x["surfaces"]))

    journeys = "".join(
        '<div class="jcard"><div class="in" style="border-top-color:{c}">'
        '<div class="k" style="color:{c}">{k}</div><div class="t">{t}</div>'
        '<div class="s">{s}</div><ul>{li}</ul></div></div>'.format(
            c=c, k=k, t=t, s=s, li="".join("<li>%s</li>" % i for i in items))
        for k, t, c, s, items in JOURNEYS)

    steps = "".join(
        '<div class="step"><div class="n">{i}</div><div class="t"><div class="h">{h}</div>'
        '<div class="d">{d}</div></div></div>'.format(i=i, h=h, d=d)
        for i, (h, d) in enumerate(STEPS, 1))

    caps = "".join("<div>%s</div>" % c for c in CAPTURE)

    sess = "".join(
        '<div class="dim" style="width:33.33%"><div class="h">'
        '<span class="sw" style="background:#2F6B45"></span><span class="n">Session {i}. {t}</span>'
        '</div><div class="q">{d}</div></div>'.format(i=i, t=t, d=d)
        for i, (t, d) in enumerate(SESSIONS, 1))

    return """<!DOCTYPE html><html><head><meta charset="utf-8"><style>{base}{css}</style></head><body>

<div class="cover">
  <div class="brand">{brand}</div>
  <div class="goldrule"></div>
  <div class="kick">An invitation for your family</div>
  <h1>Prepare the family,<br>not only the estate.</h1>
  <div class="promise">{promise}</div>
  <div class="chips">{chips}</div>
  <div class="base">
    <div class="l">{aud}</div>
    <div class="n">A private discovery experience: one assessment, four guided conversations,
      and a personalized legacy journey built from your family\u2019s own words.</div>
    <div class="idx">
      <div><b>The Problem</b>Why values do not transfer on their own</div>
      <div><b>The Assessment</b>Six dimensions, ten minutes</div>
      <div><b>The Conversations</b>Four guided interviews</div>
      <div><b>The Outcome</b>A personalized family journey</div>
    </div>
  </div>
</div>

<div class="page">
  <div class="pad">
    <div class="shead"><div class="k" style="color:#B85C3B">The Problem</div>
      <h2>Everything has been prepared<br>except the people.</h2>
      <div class="d">Five patterns show up in nearly every high-capacity Christian family \u2014
        regardless of how sophisticated the planning already is.</div></div>
    <div class="hr"></div>
    <div class="probs">{probs}</div>
    <div class="quote"><div class="q">&ldquo;{invite}&rdquo;</div>
      <div class="a">How advisors introduce this conversation</div></div>
  </div>
  {f2}
</div>

<div class="page">
  <div class="pad">
    <div class="shead"><div class="k" style="color:#2F6B45">The Opportunity</div>
      <h2>Transfer what matters<br>before you transfer what is measured.</h2>
      <div class="d">The advisor\u2019s role expands from helping a family transfer assets to
        helping the family transfer everything the assets were always meant to serve.</div></div>
    <div class="hr"></div>
    <div class="pairs">{pairs}</div>
    <div class="hr"></div>
    <div class="shead" style="margin-top:6pt"><h2 style="font-size:15pt">What a prepared family looks like</h2></div>
    <div class="dims" style="margin-top:4pt">
      <div class="dim"><div class="h"><span class="sw" style="background:#2B5C9B"></span>
        <span class="n">They know the story</span></div>
        <div class="q">The people, sacrifices, and turning points that shaped them are told, not assumed.</div></div>
      <div class="dim"><div class="h"><span class="sw" style="background:#0F7A6C"></span>
        <span class="n">They can name the values</span></div>
        <div class="q">Not attractive words \u2014 described in actual behavior, and visible in real decisions.</div></div>
      <div class="dim"><div class="h"><span class="sw" style="background:#B85C3B"></span>
        <span class="n">They can hold hard conversations</span></div>
        <div class="q">Difficult subjects can be discussed without withdrawing, attacking, or dividing.</div></div>
      <div class="dim"><div class="h"><span class="sw" style="background:#6B4E9E"></span>
        <span class="n">The heirs are being formed</span></div>
        <div class="q">Character and competence are developed before responsibility is transferred.</div></div>
      <div class="dim"><div class="h"><span class="sw" style="background:#A8811C"></span>
        <span class="n">The purpose is explained</span></div>
        <div class="q">The next generation knows why God entrusted these resources to this family.</div></div>
      <div class="dim"><div class="h"><span class="sw" style="background:#2F6B45"></span>
        <span class="n">The blessing is spoken</span></div>
        <div class="q">Wisdom, instruction, and blessing are recorded while they can still be given in person.</div></div>
    </div>
  </div>
  {f3}
</div>

<div class="page">
  <div class="pad">
    <div class="shead"><div class="k" style="color:#2B5C9B">The Assessment</div>
      <h2>Six dimensions of<br>Family Legacy Intelligence{tm}</h2>
      <div class="d">Twenty-four statements, rated one to five, completed together in about ten
        minutes. The result is not a grade. It is a picture of where your family is strong and
        where the first conversation should begin.</div></div>
    <div class="wheelbox">{wheel}</div>
    <div class="dims">{dims}</div>
    <div class="hr" style="margin:9pt 0"></div>
    <div class="lb" style="font-size:6.4pt;letter-spacing:.2em;color:#16233A">Reading the total score</div>
    <div class="ladder">{ladder}</div>
  </div>
  {f4}
</div>

<div class="page">
  <div class="pad">
    <div class="shead"><div class="k" style="color:#6B4E9E">The Instruments \u2014 One of Two</div>
      <h2>Five conversations,<br>in a deliberate order.</h2>
      <div class="d">Each instrument does one job and hands the next one something to work with.
        Nothing asks a family to be vulnerable before trust has been earned.</div></div>
    <div class="hr"></div>
    {i1}{i2}{i3}
  </div>
  {f5}
</div>

<div class="page">
  <div class="pad">
    <div class="shead"><div class="k" style="color:#6B4E9E">The Instruments \u2014 Two of Two</div>
      <h2>The private conversations,<br>and the one that reverses direction.</h2></div>
    <div class="hr"></div>
    {i4}{i5}
    <div class="hr" style="margin-top:16pt"></div>
    <div class="lb" style="color:#16233A">What the conversations are listening for</div>
    <div class="caps">{caps}</div>
  </div>
  {f6}
</div>

<div class="page">
  <div class="pad">
    <div class="shead"><div class="k" style="color:#A8811C">The Outcome</div>
      <h2>The Family Legacy<br>Journey Builder</h2>
      <div class="d">The assessment results, interview transcripts, photographs, Scriptures, and
        planning documents are placed into a secure builder that produces personalized
        resources \u2014 in your family\u2019s own language and voice.</div></div>
    <div class="hr"></div>
    <div class="jrn">{journeys}</div>
    <div class="hr"></div>
    <div class="lb" style="color:#16233A">The six-session whole-family experience</div>
    <div class="dims" style="margin-top:2pt">{sess}</div>
  </div>
  {f7}
</div>

<div class="page last">
  <div class="pad">
    <div class="shead"><div class="k" style="color:#16233A">The Process</div>
      <h2>How the experience works</h2>
      <div class="d">Offered to ten client families at a time, so that every conversation
        receives the attention it deserves.</div></div>
    <div class="hr"></div>
    <div class="steps">{steps}</div>
    <div class="conf"><div class="k">A commitment before we begin</div><p>{conf}</p></div>
  </div>
  <div class="finale">
    <div class="k">The Central Promise</div>
    <h2>{promise}</h2>
    <p>{closing}</p>
  </div>
  {f8}
</div>

</body></html>""".format(
        base=BASE, css=BROCHURE_CSS, brand=BRAND, promise=PROMISE, chips=chips_html(),
        aud=AUDIENCE, tm=TM, probs=probs, invite=INVITATION_QUOTE, pairs=pairs,
        wheel=wheel_svg(example=True, blank_note=False), dims=dims, ladder=ladder,
        i1=inst_card(INSTRUMENTS[0]), i2=inst_card(INSTRUMENTS[1]), i3=inst_card(INSTRUMENTS[2]),
        i4=inst_card(INSTRUMENTS[3]), i5=inst_card(INSTRUMENTS[4]), caps=caps,
        journeys=journeys, sess=sess, steps=steps, conf=CONFIDENTIALITY, closing=CLOSING_LINE,
        f2=foot(2, 8), f3=foot(3, 8), f4=foot(4, 8), f5=foot(5, 8), f6=foot(6, 8),
        f7=foot(7, 8), f8=foot(8, 8))


# ================================================================ interviews
def interview(iv):
    C = iv["color"]
    total = 5

    def qblock(i, q, p, nlines=7):
        return """
<div class="q">
  <div class="hd"><div class="no" style="color:{c}">{i:02d}</div>
    <div class="tx"><div class="t">{q}</div><div class="p">{p}</div></div></div>
  <div class="sp">{lines}</div>
</div>""".format(c=C, i=i, q=q, p=p, lines=lines(nlines))

    def qpage(idxs, pageno, last=False, extra=""):
        body = "".join(qblock(i + 1, *iv["questions"][i]) for i in idxs)
        return """
<div class="page{lc}">
  {rh}
  <div class="pad">{body}{extra}</div>
  {ft}
</div>""".format(lc=" last" if last else "", rh=rhead(C, iv["title"], iv["subtitle"]),
                 body=body, extra=extra, ft=foot(pageno, total))

    nlines = 4 if len(iv["closing"]) <= 3 else 3
    prompts = "".join(
        '<div class="pr"><div class="l">{l}</div>{ln}</div>'.format(l=l, ln=lines(nlines))
        for l in iv["closing"])
    closing = """
<div class="stmtbox">
  <div class="k" style="color:{c}">In your own words</div>
  <h3>{t}</h3>
  {p}
</div>""".format(c=C, t=iv["closing_title"], p=prompts)

    whys = "".join('<div class="b"><div class="h">{h}</div><p>{p}</p></div>'.format(h=h, p=p)
                   for h, p in iv["why"])
    hows = "".join("<li>%s</li>" % h for h in iv["how"])

    cover = """
<div class="cover iv" style="background:{c}">
  <div class="brand" style="color:rgba(255,255,255,.72)">{brand}</div>
  <div class="goldrule"></div>
  <div class="kick" style="color:rgba(255,255,255,.9)">{kick}</div>
  <h1>{title}</h1>
  <div class="promise" style="color:rgba(255,255,255,.9);font-size:11.4pt;max-width:5.1in">{sub}</div>
  <div style="font-family:'Lora';font-style:italic;font-size:10.4pt;color:rgba(255,255,255,.82);
       max-width:5in;margin-top:13pt;line-height:1.5">{deck}</div>
  <div class="why">{whys}</div>
  <div class="how"><div class="h" style="color:rgba(255,255,255,.9)">How to use these pages</div>
    <ul>{hows}</ul></div>
  <div class="perm"><div class="h" style="color:rgba(255,255,255,.82)">On recording</div>
    <p>{perm}</p></div>
</div>""".format(c=C, brand=BRAND, kick=iv["kicker"], title=iv["title"], sub=iv["subtitle"],
                 deck=iv["deck"], whys=whys, hows=hows, perm=PERMISSION)

    return """<!DOCTYPE html><html><head><meta charset="utf-8"><style>{base}{css}</style></head><body>
{cover}
{p2}{p3}{p4}{p5}
</body></html>""".format(
        base=BASE, css=INTERVIEW_CSS, cover=cover,
        p2=qpage([0, 1, 2], 2), p3=qpage([3, 4, 5], 3), p4=qpage([6, 7, 8], 4),
        p5=qpage([9], 5, last=True, extra=closing))


# ================================================================ assessment
def assessment():
    def rows(d):
        return "".join(
            '<div class="row"><div class="t">{t}</div>'
            '<div class="scale"><i>1</i><i>2</i><i>3</i><i>4</i><i>5</i></div></div>'.format(t=t)
            for t in d["items"])

    def sec(d):
        return """
<div class="sec">
  <div class="hd" style="background:{c}"><div class="no">{n}</div>
    <div class="tt"><div class="t">{t}</div><div class="q">{q}</div></div></div>
  <div class="rows">{rows}
    <div class="secfoot"><span class="k" style="color:{c}">Section Score</span>
      <span class="v" style="border-color:{c}"></span><span class="d">/ 20</span></div></div>
</div>""".format(c=d["color"], n=d["n"], t=d["title"], q=d["q"], rows=rows(d))

    keyrow = "".join('<div><div class="n">{}</div><div class="t">{}</div></div>'.format(k, v)
                     for k, v in SCALE)
    xfer = "".join(
        '<div class="xrow"><span class="sw" style="background:{c}"></span>'
        '<span class="nm">{n:02d}. {t}</span><span class="bx" style="border-color:{c}"></span>'
        '<span class="of">/ 20</span></div>'.format(c=d["color"], n=d["n"], t=d["title"])
        for d in DIMENSIONS)
    ladder = "".join(
        '<div class="c" style="border-top-color:{c}"><div class="r" style="color:{c}">{r}</div>'
        '<div class="n">{n}</div><div class="d">{d}</div></div>'.format(r=r, n=n, c=c, d=d)
        for r, n, c, d in BANDS)
    q3 = "".join('<div class="c"><div class="n">0{i}</div><div class="x">{q}</div></div>'.format(
        i=i, q=q) for i, q in enumerate(QUESTIONS3, 1))

    return """<!DOCTYPE html><html><head><meta charset="utf-8"><style>{base}{css}
.ladder {{ display:flex; gap:7pt; margin-top:11pt; }}
.ladder .c {{ flex:1; border-top:2.6pt solid; padding:7pt 0 0; }}
.ladder .r {{ font-family:'Lora'; font-weight:600; font-size:11pt; }}
.ladder .n {{ font-weight:600; font-size:7.2pt; color:#16233A; margin-top:2pt; line-height:1.22; }}
.ladder .d {{ font-size:6.4pt; line-height:1.36; color:#5A6675; margin-top:3pt; }}
</style></head><body>

<div class="page">
  <div class="hero">
    <div class="eyebrow">{brand}</div>
    <h1>The Ten-Minute Family<br>Legacy Assessment</h1>
    <div class="deck">{promise}</div>
    <div class="chips">{chips}</div>
  </div>
  <div class="howto">
    <div class="a"><div class="lb">Before you begin</div><p>{pre}</p></div>
    <div class="b"><div class="lb">How to rate</div><div class="keyrow">{keyrow}</div>
      <div class="note">{instr}</div></div>
  </div>
  <div class="pad">{s1}{s2}</div>
  {f1}
</div>

<div class="page">
  {rh}
  <div class="pad">{s3}{s4}{s5}</div>
  {f2}
</div>

<div class="page">
  {rh}
  <div class="pad">
    {s6}
    <div class="shead" style="margin-top:16pt"><div class="k" style="color:#16233A">Step One</div>
      <h2 style="font-size:16pt">Carry each section score here</h2></div>
    <div class="xfer">{xfer}</div>
    <div class="tot"><span class="k">Total Score</span><span class="bx"></span>
      <span class="of">/ 120</span></div>
  </div>
  {f3}
</div>

<div class="page last">
  {rh}
  <div class="pad">
    <div class="shead" style="margin-top:14pt"><div class="k" style="color:#16233A">Step Two</div>
      <h2 style="font-size:18pt">Your family legacy profile</h2>
      <div class="d">Plot each section score on the matching spoke, then connect the points.
        The shape tells you more than the total does.</div></div>
    <div style="margin-top:6pt">{wheel}</div>
    <div class="hr" style="margin:8pt 0"></div>
    <div class="lb" style="color:#16233A">Reading your total</div>
    <div class="ladder">{ladder}</div>
    <div class="hr" style="margin:13pt 0 9pt"></div>
    <div class="lb" style="color:#16233A">Before you choose where to begin</div>
    <p style="font-size:8pt;line-height:1.44;color:#55616F;margin:0">{discern}</p>
    <div class="q3">{q3}</div>
  </div>
  {f4}
</div>

</body></html>""".format(
        base=BASE, css=ASSESS_CSS, brand=BRAND, promise=PROMISE, chips=chips_html(),
        pre=PREAMBLE, keyrow=keyrow, instr=INSTRUCTIONS,
        s1=sec(DIMENSIONS[0]), s2=sec(DIMENSIONS[1]), s3=sec(DIMENSIONS[2]),
        s4=sec(DIMENSIONS[3]), s5=sec(DIMENSIONS[4]), s6=sec(DIMENSIONS[5]),
        rh=rhead("#16233A", BRAND, "The Ten-Minute Family Legacy Assessment"),
        xfer=xfer, wheel=wheel_svg(blank_note=True), ladder=ladder,
        discern=DISCERN_INTRO, q3=q3,
        f1=foot(1, 4), f2=foot(2, 4), f3=foot(3, 4), f4=foot(4, 4))


# ====================================================================== main
if __name__ == "__main__":
    jobs = [("01-Family-Legacy-Intelligence-Overview-Brochure.pdf", brochure(), 8),
            ("02-Assessment-Standalone.pdf", assessment(), 4)]
    for iv in INTERVIEWS:
        jobs.append(("Interview-%s.pdf" % iv["slug"].title().replace("-", "-"),
                     interview(iv), 5))
    for name, html, expect in jobs:
        path = os.path.join(OUT, name)
        HTML(string=html).write_pdf(path)
        n = len(PdfReader(path).pages)
        print("%-52s %2d pages  %s" % (name, n, "OK" if n == expect else "!! expected %d" % expect))
