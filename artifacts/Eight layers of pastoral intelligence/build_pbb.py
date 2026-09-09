# -*- coding: utf-8 -*-
import html as H
import json
import pbb_data as D
import pbb_data2 as D2

def esc(s):
    return H.escape(s, quote=True)

FONT_URL = "https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,500;0,700;0,800;0,900;1,500;1,600&family=Spectral:ital,wght@0,400;0,500;0,600;1,400&family=Archivo:wght@400;500;600;700&display=swap"

CSS = """
:root{--ink:#080e16;--navy:#0b1726;--navy-2:#0e1d30;--panel:#132439;--panel-2:#16293f;
--gold:#c9a35c;--gold-bright:#e3c186;--cream:#ece7d8;--muted:#8b94a5;--muted-dim:#5f6a7c;
--ivory:#f4efe3;--line:rgba(255,255,255,.08);--line-gold:rgba(201,163,92,.22);--maxw:1280px;}
*{box-sizing:border-box;margin:0;padding:0}
html{scroll-behavior:smooth;-webkit-text-size-adjust:100%}
body{background:var(--navy);color:var(--cream);font-family:'Spectral',Georgia,serif;font-weight:400;font-size:16px;line-height:1.6}
.wrap{max-width:var(--maxw);margin:0 auto;padding:0 32px}
@media(max-width:640px){.wrap{padding:0 20px}}
a{color:var(--gold-bright);text-decoration:none}
.eyebrow{font-family:'Archivo',sans-serif;font-size:11px;font-weight:600;letter-spacing:.22em;text-transform:uppercase;color:var(--gold)}
h1{font-family:'Playfair Display',serif;font-weight:800;font-size:clamp(40px,5.4vw,68px);line-height:1.04;letter-spacing:-.015em;color:var(--cream)}
h1 em,.h em{font-style:italic;font-weight:800;color:var(--gold-bright)}
.h{font-family:'Playfair Display',serif;font-weight:800;font-size:clamp(27px,3.4vw,42px);line-height:1.1;letter-spacing:-.012em;color:var(--cream);margin:14px 0 0}
.hdr{position:sticky;top:0;z-index:50;height:78px;background:rgba(11,23,38,.86);backdrop-filter:blur(14px);-webkit-backdrop-filter:blur(14px);border-bottom:1px solid var(--line-gold)}
.hdr .wrap{height:78px;display:flex;align-items:center;gap:26px}
.brand{font-family:'Playfair Display',serif;font-weight:700;font-size:21px;color:var(--cream);white-space:nowrap}
.brand em{font-style:italic;color:var(--gold-bright)}
.dot{display:inline-block;width:5px;height:5px;border-radius:50%;background:var(--gold);margin-left:5px;vertical-align:6px}
nav{margin-left:auto;display:flex;gap:20px;overflow-x:auto;-webkit-overflow-scrolling:touch}
nav::-webkit-scrollbar{display:none}
nav a{font-family:'Archivo',sans-serif;font-size:11px;font-weight:600;letter-spacing:.14em;text-transform:uppercase;color:var(--muted);white-space:nowrap}
nav a:hover{color:var(--gold-bright)}
.hero{background:radial-gradient(80% 120% at 78% -10%, rgba(201,163,92,.12), transparent 55%),linear-gradient(180deg, var(--navy-2), var(--navy));padding:84px 0 70px;border-bottom:1px solid var(--line-gold)}
.hero .sub{font-size:18px;color:var(--muted);max-width:640px;margin:22px 0 30px;font-weight:400}
.btnrow{display:flex;gap:12px;flex-wrap:wrap}
.btn{display:inline-block;font-family:'Archivo',sans-serif;font-size:13px;font-weight:600;letter-spacing:.06em;text-transform:uppercase;border-radius:3px;padding:14px 24px;background:var(--gold);color:var(--ink);border:1px solid var(--gold);cursor:pointer}
.btn.ghost{background:transparent;color:var(--gold-bright);border-color:var(--line-gold)}
.chipline{font-family:'Archivo',sans-serif;font-size:10.5px;font-weight:600;letter-spacing:.12em;text-transform:uppercase;color:var(--muted-dim);border:1px solid var(--line-gold);border-radius:3px;display:inline-block;padding:7px 12px;margin-top:30px}
.stats{display:grid;grid-template-columns:repeat(2,1fr);gap:1px;background:var(--line-gold);border:1px solid var(--line-gold);margin-top:44px}
@media(min-width:820px){.stats{grid-template-columns:repeat(4,1fr)}}
.stat{background:var(--panel);padding:26px 22px;text-align:left}
.stat .n{font-family:'Playfair Display',serif;font-weight:800;font-size:clamp(30px,3.6vw,44px);color:var(--gold);line-height:1}
.stat .l{font-family:'Archivo',sans-serif;font-size:11px;font-weight:600;letter-spacing:.1em;text-transform:uppercase;color:var(--muted);margin-top:8px}
section{padding:74px 0;border-bottom:1px solid var(--line-gold);scroll-margin-top:96px}
section.alt{background:var(--navy-2)}
.lede{font-size:17px;color:var(--muted);max-width:720px;margin:18px 0 0}
.prose p{max-width:760px;margin:18px 0;color:var(--cream)}
.pull{max-width:760px;margin:30px 0 6px;padding:20px 24px;background:rgba(201,163,92,.06);border-left:2px solid var(--gold);font-family:'Playfair Display',serif;font-style:italic;font-weight:500;font-size:20px;line-height:1.45;color:var(--gold-bright)}
.pgrid{display:grid;grid-template-columns:1fr;gap:1px;background:var(--line-gold);border:1px solid var(--line-gold);margin-top:34px}
@media(min-width:860px){.pgrid.two{grid-template-columns:1fr 1fr}}
.pnl{background:var(--panel);padding:30px 28px}
.pnl.alt2{background:var(--panel-2)}
.pname{font-family:'Playfair Display',serif;font-weight:700;font-size:24px;color:var(--cream)}
.ptag{font-family:'Archivo',sans-serif;font-size:10.5px;font-weight:600;letter-spacing:.16em;text-transform:uppercase;color:var(--gold);margin-top:5px}
.pbody{color:var(--muted);margin:14px 0 6px;font-size:15.5px}
.frow{display:flex;gap:16px;padding:13px 0;border-bottom:1px solid var(--line);font-size:15px}
.frow:last-child{border-bottom:0}
.frow b{font-family:'Archivo',sans-serif;font-size:11px;font-weight:600;letter-spacing:.1em;text-transform:uppercase;color:var(--gold-bright);flex:0 0 168px;padding-top:3px}
@media(max-width:560px){.frow{flex-direction:column;gap:4px}.frow b{flex:none}}
.fnote{font-family:'Archivo',sans-serif;font-size:10.5px;letter-spacing:.06em;color:var(--muted-dim);margin-top:14px;text-transform:uppercase}
.qblock{background:var(--panel);padding:24px 26px}
.qt{font-family:'Spectral',serif;font-weight:600;font-size:16.5px;color:var(--cream);margin-bottom:14px}
.qn{font-family:'Playfair Display',serif;font-weight:800;color:var(--gold);margin-right:10px}
.opts{display:grid;grid-template-columns:1fr;gap:8px}
@media(min-width:860px){.opts{grid-template-columns:1fr 1fr}}
.opt{font-family:'Spectral',serif;font-size:14.5px;text-align:left;background:var(--panel-2);border:1px solid var(--line);border-radius:3px;color:var(--cream);padding:11px 14px;cursor:pointer;line-height:1.4}
.opt.sel{border-color:var(--gold);background:rgba(201,163,92,.12);color:var(--gold-bright)}
.scorebar{margin-top:1px;background:var(--ink);border:1px solid var(--line-gold);padding:20px 26px;display:flex;align-items:center;gap:22px;flex-wrap:wrap}
.scorebar .sn{font-family:'Playfair Display',serif;font-weight:800;font-size:34px;color:var(--gold);line-height:1}
.scorebar .sl{font-family:'Archivo',sans-serif;font-size:11px;font-weight:600;letter-spacing:.1em;text-transform:uppercase;color:var(--muted)}
.reset{margin-left:auto;font-family:'Archivo',sans-serif;font-size:11px;font-weight:600;letter-spacing:.1em;text-transform:uppercase;background:transparent;border:1px solid var(--line-gold);border-radius:3px;color:var(--gold-bright);padding:9px 15px;cursor:pointer}
.bandout{background:rgba(201,163,92,.06);border:1px solid var(--line-gold);border-left:2px solid var(--gold);padding:22px 26px;margin-top:1px}
.bandout .br{font-family:'Archivo',sans-serif;font-size:10.5px;font-weight:600;letter-spacing:.16em;text-transform:uppercase;color:var(--gold)}
.bandout .bn{font-family:'Playfair Display',serif;font-style:italic;font-weight:700;font-size:24px;color:var(--gold-bright);margin:6px 0 8px}
.bandout p{color:var(--cream);font-size:15px;max-width:720px}
.bandkey{margin-top:28px}
.bandrow{display:flex;gap:16px;padding:13px 0;border-bottom:1px solid var(--line);font-size:15px}
.bandrow:last-child{border-bottom:0}
.bandrow .rg{font-family:'Archivo',sans-serif;font-size:11px;font-weight:600;letter-spacing:.1em;color:var(--gold);flex:0 0 76px;padding-top:3px}
.bandrow .bd b{font-family:'Playfair Display',serif;font-style:italic;font-weight:700;font-size:17px;color:var(--cream);display:block}
.bandrow .bd span{color:var(--muted);font-size:14.5px}
.confid{font-family:'Archivo',sans-serif;font-size:11px;letter-spacing:.08em;text-transform:uppercase;color:var(--muted-dim);margin-top:16px;max-width:720px;line-height:1.7}
.dimhead{background:var(--panel-2);padding:16px 26px;display:flex;align-items:baseline;gap:14px}
.dimhead .dn{font-family:'Playfair Display',serif;font-style:italic;font-weight:700;font-size:19px;color:var(--gold-bright)}
.dimhead .ds{font-family:'Archivo',sans-serif;font-size:11px;font-weight:600;letter-spacing:.1em;text-transform:uppercase;color:var(--muted);margin-left:auto}
.stmt{background:var(--panel);padding:16px 26px;display:flex;gap:18px;align-items:center;flex-wrap:wrap}
.stmt .tx{flex:1 1 300px;font-size:15px;color:var(--cream)}
.rate{display:flex;gap:6px}
.rbtn{width:38px;height:38px;font-family:'Archivo',sans-serif;font-size:13px;font-weight:600;background:var(--panel-2);border:1px solid var(--line);border-radius:3px;color:var(--muted);cursor:pointer}
.rbtn.sel{border-color:var(--gold);background:rgba(201,163,92,.14);color:var(--gold-bright)}
.scalekey{font-family:'Archivo',sans-serif;font-size:10.5px;letter-spacing:.08em;text-transform:uppercase;color:var(--muted-dim);margin-top:14px}
.seatbar{display:flex;gap:1px;background:var(--line-gold);border:1px solid var(--line-gold);margin-top:34px}
.seatbtn{flex:1;font-family:'Archivo',sans-serif;font-size:12px;font-weight:600;letter-spacing:.1em;text-transform:uppercase;background:var(--panel);border:0;color:var(--muted);padding:16px 10px;cursor:pointer}
.seatbtn.on{background:var(--panel-2);color:var(--gold-bright);box-shadow:none}
.seatpanel{display:none}
.seatpanel.on{display:block}
.seatq{font-family:'Playfair Display',serif;font-style:italic;font-weight:700;font-size:24px;color:var(--gold-bright);margin-top:0}
.dir{margin-top:30px;border-top:1px solid var(--line-gold)}
.dirrow{display:flex;gap:20px;padding:18px 0;border-bottom:1px solid var(--line)}
.dirrow .no{font-family:'Playfair Display',serif;font-weight:800;font-size:18px;color:var(--gold);flex:0 0 34px;padding-top:2px}
.dirrow .bd{flex:1}
.dirrow .tt{font-family:'Playfair Display',serif;font-weight:700;font-size:18px;color:var(--cream)}
.dirrow .st{font-family:'Spectral',serif;font-style:italic;font-size:14.5px;color:var(--muted);margin-top:3px}
.dirrow .mt{font-family:'Archivo',sans-serif;font-size:10.5px;font-weight:600;letter-spacing:.12em;text-transform:uppercase;color:var(--gold);flex:0 0 auto;text-align:right;padding-top:4px;white-space:nowrap}
@media(max-width:560px){.dirrow{flex-wrap:wrap}.dirrow .mt{flex-basis:100%;text-align:left;padding-left:54px}}
.chips{display:flex;flex-wrap:wrap;gap:8px;margin-top:18px}
.chip{font-family:'Archivo',sans-serif;font-size:11px;font-weight:500;letter-spacing:.06em;border:1px solid var(--line);border-radius:3px;color:var(--muted);padding:7px 12px}
.mathline{font-family:'Archivo',sans-serif;font-size:11px;font-weight:600;letter-spacing:.1em;text-transform:uppercase;color:var(--gold);margin-top:22px}
.steprow{background:var(--panel);padding:24px 26px;display:flex;gap:22px;flex-wrap:wrap;align-items:baseline}
.steprow .tt{font-family:'Playfair Display',serif;font-weight:700;font-size:19px;color:var(--cream);flex:1 1 240px}
.steprow .pr{font-family:'Playfair Display',serif;font-weight:800;font-size:19px;color:var(--gold);white-space:nowrap}
.steprow .by{font-family:'Archivo',sans-serif;font-size:10.5px;font-weight:600;letter-spacing:.12em;text-transform:uppercase;color:var(--muted);flex-basis:100%}
.steprow .bd{color:var(--muted);font-size:14.5px;flex-basis:100%}
.tierrow{background:var(--panel);padding:26px;display:flex;gap:18px;flex-wrap:wrap;align-items:baseline}
.tierrow .tt{font-family:'Playfair Display',serif;font-weight:700;font-size:21px;color:var(--cream);flex:0 0 150px}
.tierrow .hc{font-family:'Archivo',sans-serif;font-size:10.5px;font-weight:600;letter-spacing:.12em;text-transform:uppercase;color:var(--muted);flex:1}
.tierrow .pr{font-family:'Playfair Display',serif;font-weight:800;font-size:22px;color:var(--gold);white-space:nowrap}
.tierrow .bd{color:var(--muted);font-size:14px;flex-basis:100%}
.warn{background:rgba(201,163,92,.06);border:1px solid var(--line-gold);border-left:2px solid var(--gold);padding:18px 24px;margin-top:26px;font-family:'Archivo',sans-serif;font-size:11px;font-weight:600;letter-spacing:.08em;text-transform:uppercase;color:var(--gold-bright);line-height:1.8;max-width:860px}
.srow{background:var(--panel);padding:24px 26px}
.srow .tt{font-family:'Playfair Display',serif;font-weight:700;font-size:18px;color:var(--cream)}
.srow .stt{font-family:'Archivo',sans-serif;font-size:10.5px;font-weight:600;letter-spacing:.14em;text-transform:uppercase;color:var(--gold);margin:5px 0 10px}
.srow .bd{color:var(--muted);font-size:14.5px}
.statusrow{padding:16px 0;border-bottom:1px solid var(--line);max-width:860px}
.statusrow:last-child{border-bottom:0}
.statusrow b{font-family:'Archivo',sans-serif;font-size:11px;font-weight:600;letter-spacing:.14em;text-transform:uppercase;color:var(--gold);display:block;margin-bottom:5px}
.statusrow span{color:var(--muted);font-size:14.5px}
.acc{background:var(--panel)}
.ahead{display:flex;width:100%;text-align:left;border:0;background:none;padding:20px 26px;cursor:pointer;gap:16px;align-items:baseline;font:inherit}
.attl{font-family:'Playfair Display',serif;font-weight:700;font-size:19px;color:var(--cream);flex:1;line-height:1.25}
.aspn{display:block;font-family:'Spectral',serif;font-style:italic;font-weight:400;font-size:14px;color:var(--muted);margin-top:3px}
.ameta{font-family:'Archivo',sans-serif;font-size:11px;font-weight:600;letter-spacing:.1em;text-transform:uppercase;color:var(--gold);white-space:nowrap;padding-top:4px}
.acaret{font-family:'Archivo',sans-serif;font-weight:700;color:var(--gold-bright);transition:transform .15s}
.acc.open .acaret{transform:rotate(90deg)}
.abody{display:none;padding:0 26px 24px}
.acc.open .abody{display:block}
.stepli{padding:10px 0 10px 18px;border-bottom:1px solid var(--line);position:relative;font-size:15px;color:var(--cream)}
.stepli:last-child{border-bottom:0}
.stepli:before{content:"";position:absolute;left:0;top:19px;width:6px;height:6px;background:var(--gold)}
.jweek{margin:16px 0 4px;border-top:1px solid var(--line);padding-top:14px}
.jweek:first-of-type{border-top:0;margin-top:6px;padding-top:0}
.jwl{font-family:'Archivo',sans-serif;font-size:10.5px;font-weight:600;letter-spacing:.16em;text-transform:uppercase;color:var(--muted)}
.jwt{font-family:'Playfair Display',serif;font-style:italic;font-weight:700;font-size:18px;color:var(--gold-bright);margin:4px 0 10px}
.dayli{display:flex;gap:14px;padding:6px 0;font-size:14.5px;color:var(--cream);align-items:baseline}
.dayn{font-family:'Archivo',sans-serif;font-size:10px;font-weight:600;letter-spacing:.12em;text-transform:uppercase;color:var(--gold);flex:0 0 56px}
.dst{font-family:'Archivo',sans-serif;font-size:10px;font-weight:600;letter-spacing:.14em;text-transform:uppercase;color:var(--gold);margin-top:3px}
@media(max-width:560px){.ahead{flex-wrap:wrap}.ameta{flex-basis:100%;padding-top:0}}
.foot{padding:44px 0 60px;text-align:center;font-family:'Archivo',sans-serif;font-size:10.5px;font-weight:600;letter-spacing:.16em;text-transform:uppercase;color:var(--muted-dim)}
"""

def sec_head(eyebrow, ha, hem, lede=None):
    s = '<div class="eyebrow">' + esc(eyebrow) + '</div><div class="h">' + esc(ha) + '<em>' + esc(hem) + '</em></div>'
    if lede:
        s += '<p class="lede">' + esc(lede) + '</p>'
    return s

def build_header():
    s = ['<header class="hdr"><div class="wrap"><div class="brand">' + D.META["brand_a"] + '<em>' + D.META["brand_b"] + '</em><span class="dot"></span></div><nav>']
    for label, href in D.NAV:
        s.append('<a href="' + href + '">' + esc(label) + '</a>')
    s.append('</nav></div></header>')
    return "".join(s)

def build_hero():
    m = D.META
    s = ['<div class="hero"><div class="wrap">']
    s.append('<div class="eyebrow">' + esc(m["eyebrow"]) + '</div>')
    s.append('<h1>' + esc(m["h1_a"]) + '<em>' + esc(m["h1_em"]) + '</em></h1>')
    s.append('<p class="sub">' + esc(m["sub"]) + '</p>')
    s.append('<div class="btnrow"><a class="btn" href="' + m["cta1"][1] + '">' + esc(m["cta1"][0]) + '</a><a class="btn ghost" href="' + m["cta2"][1] + '">' + esc(m["cta2"][0]) + '</a></div>')
    s.append('<div class="stats">')
    for n, l in m["stats"]:
        s.append('<div class="stat"><div class="n">' + esc(n) + '</div><div class="l">' + esc(l) + '</div></div>')
    s.append('</div>')
    s.append('<div class="chipline">' + esc(m["status_chip"]) + '</div>')
    s.append('</div></div>')
    return "".join(s)

def build_argument():
    a = D.ARGUMENT
    s = ['<section id="argument"><div class="wrap">']
    s.append(sec_head(a["eyebrow"], a["head_a"], a["head_em"]))
    s.append('<div class="prose">')
    for p in a["paras"]:
        s.append('<p>' + esc(p) + '</p>')
    s.append('</div><div class="pull">' + esc(a["quote"]) + '</div>')
    s.append('</div></section>')
    return "".join(s)

def framework_panel(f, alt):
    cls = "pnl alt2" if alt else "pnl"
    s = ['<div class="' + cls + '"><div class="pname">' + esc(f["name"]) + '</div><div class="ptag">' + esc(f["tag"]) + '</div><p class="pbody">' + esc(f["body"]) + '</p>']
    for b, body in f["rows"]:
        s.append('<div class="frow"><b>' + esc(b) + '</b><span>' + esc(body) + '</span></div>')
    s.append('<div class="fnote">' + esc(f["note"]) + '</div></div>')
    return "".join(s)

def build_frameworks():
    fr = D.FRAMEWORKS
    s = ['<section id="frameworks" class="alt"><div class="wrap">']
    s.append(sec_head(fr["eyebrow"], fr["head_a"], fr["head_em"], fr["intro"]))
    s.append('<div class="pgrid two">' + framework_panel(fr["f1"], False) + framework_panel(fr["f2"], True) + '</div>')
    s.append('</div></section>')
    return "".join(s)

def build_diagnostic():
    d = D.DIAG
    s = ['<section id="diagnostic"><div class="wrap">']
    s.append(sec_head(d["eyebrow"], d["head_a"], d["head_em"], d["intro"]))
    s.append('<div class="pgrid" style="margin-top:34px">')
    for qi, (qt, opts) in enumerate(D.DIAGNOSTIC):
        s.append('<div class="qblock"><div class="qt"><span class="qn">' + str(qi + 1).zfill(2) + '</span>' + esc(qt) + '</div><div class="opts">')
        for label, val in opts:
            s.append('<button type="button" class="opt" data-q="' + str(qi) + '" data-val="' + str(val) + '" onclick="dpick(this)">' + esc(label) + '</button>')
        s.append('</div></div>')
    s.append('</div>')
    s.append('<div class="scorebar"><div><span class="sn" id="d-score">0</span></div><div class="sl">of 48</div><div class="sl" id="d-prog">0 of 12 answered</div><button type="button" class="reset" onclick="dreset()">Reset</button></div>')
    s.append('<div class="bandout" id="d-band" style="display:none"><div class="br" id="d-band-range"></div><div class="bn" id="d-band-name"></div><p id="d-band-body"></p></div>')
    s.append('<div class="bandkey">')
    for lo, hi, name, body in D.BANDS:
        s.append('<div class="bandrow"><span class="rg">' + str(lo) + '\u2013' + str(hi) + '</span><span class="bd"><b>' + esc(name) + '</b><span>' + esc(body) + '</span></span></div>')
    s.append('</div>')
    s.append('<div class="pgrid" style="margin-top:30px"><div class="pnl"><div class="ptag">Discernment ' + D.EM + ' the lowest score is not automatically the first priority</div>')
    for name, q in D.DISCERNMENT:
        s.append('<div class="frow"><b>' + esc(name) + '</b><span>' + esc(q) + '</span></div>')
    s.append('</div></div>')
    s.append('<p class="confid">' + esc(d["confidential"]) + '</p>')
    s.append('</div></section>')
    return "".join(s)

def build_flourishing():
    f = D.FLOUR
    s = ['<section id="flourishing" class="alt"><div class="wrap">']
    s.append(sec_head(f["eyebrow"], f["head_a"], f["head_em"], f["intro"]))
    s.append('<div class="scalekey">' + esc(" \u00b7 ".join(f["scale"])) + '</div>')
    s.append('<div class="pgrid" style="margin-top:24px">')
    idx = 0
    for di, (dim, stmts) in enumerate(D.FLOUR_DIMS):
        s.append('<div class="dimhead"><div class="dn">Flourishing ' + esc(dim) + '</div><div class="ds" id="fsub-' + str(di) + '">\u2013 / 20</div></div>')
        for st in stmts:
            s.append('<div class="stmt"><div class="tx">' + esc(st) + '</div><div class="rate">')
            for v in range(1, 6):
                s.append('<button type="button" class="rbtn" data-q="' + str(idx) + '" data-dim="' + str(di) + '" data-val="' + str(v) + '" onclick="fpick(this)">' + str(v) + '</button>')
            s.append('</div></div>')
            idx += 1
    s.append('</div>')
    s.append('<div class="scorebar"><div><span class="sn" id="f-score">0</span></div><div class="sl">of 120</div><div class="sl" id="f-prog">0 of 24 answered</div><button type="button" class="reset" onclick="freset()">Reset</button></div>')
    s.append('<div class="bandout" id="f-band" style="display:none"><div class="br" id="f-band-range"></div><div class="bn" id="f-band-name"></div><p id="f-band-body"></p></div>')
    s.append('<div class="bandkey">')
    for lo, hi, name, body in D.FLOUR_BANDS:
        s.append('<div class="bandrow"><span class="rg">' + str(lo) + '\u2013' + str(hi) + '</span><span class="bd"><b>' + esc(name) + '</b><span>' + esc(body) + '</span></span></div>')
    s.append('</div>')
    s.append('</div></section>')
    return "".join(s)

def build_seats():
    s = ['<section id="seats"><div class="wrap">']
    s.append(sec_head("Three Seats", "Owner, leader, ", "team.", D.SEATS_INTRO))
    s.append('<div class="seatbar">')
    for i, seat in enumerate(D.SEATS):
        cls = "seatbtn on" if i == 0 else "seatbtn"
        s.append('<button type="button" class="' + cls + '" id="seatbtn-' + seat["id"] + '" onclick="setSeat(\'' + seat["id"] + '\')">' + esc(seat["label"]) + '</button>')
    s.append('</div>')
    for i, seat in enumerate(D.SEATS):
        cls = "seatpanel on" if i == 0 else "seatpanel"
        s.append('<div class="' + cls + '" id="seat-' + seat["id"] + '"><div class="pgrid"><div class="pnl">')
        s.append('<div class="seatq">' + esc(seat["q"]) + '</div><p class="pbody">' + esc(seat["who"]) + '</p>')
        for b, body in seat["path"]:
            s.append('<div class="frow"><b>' + esc(b) + '</b><span>' + esc(body) + '</span></div>')
        s.append('</div></div></div>')
    # peer group
    p = D.PEER
    s.append('<div style="margin-top:64px">')
    s.append(sec_head(p["eyebrow"], p["head_a"], p["head_em"], p["intro"]))
    s.append('<div class="pull">' + esc(p["line"]) + '</div>')
    s.append('<div class="dir">')
    for i, (tt, st, ref, wks) in enumerate(p["studies"]):
        s.append('<div class="dirrow"><span class="no">' + str(i + 1).zfill(2) + '</span><span class="bd"><span class="tt">' + esc(tt) + '</span><div class="st">' + esc(st) + '</div></span><span class="mt">' + esc(ref) + ' \u00b7 ' + esc(wks) + '</span></div>')
    s.append('</div></div>')
    s.append('</div></section>')
    return "".join(s)

def build_library():
    L = D.LIBRARY
    s = ['<section id="library" class="alt"><div class="wrap">']
    s.append('<div class="eyebrow">' + esc(L["eyebrow"]) + '</div>')
    s.append('<div class="h">' + esc(L["head_a"]) + '<sup style="font-size:.5em">' + L["head_tm"] + '</sup><em>' + esc(L["head_em"]) + '</em></div>')
    s.append('<p class="lede">' + esc(L["intro"]) + '</p>')
    s.append('<div class="pgrid" style="margin-top:34px"><div class="pnl"><div class="ptag">' + esc(L["spine_head"]) + '</div><div class="chips">')
    for sp in L["spine"]:
        s.append('<span class="chip">' + esc(sp) + '</span>')
    s.append('</div></div></div>')
    s.append('<div class="dir">')
    for tt, body, count in L["parts"]:
        s.append('<div class="dirrow"><span class="bd"><span class="tt">' + esc(tt) + '</span><div class="st">' + esc(body) + '</div></span><span class="mt">' + esc(count) + '</span></div>')
    s.append('</div>')
    s.append('<div class="ptag" style="margin-top:30px">' + esc(L["verticals_head"]) + '</div><div class="chips">')
    for v in L["verticals"]:
        s.append('<span class="chip">' + esc(v) + '</span>')
    s.append('</div>')
    s.append('<div class="mathline">' + esc(L["math"]) + '</div>')
    s.append('</div></section>')
    return "".join(s)

def build_process():
    P = D.PROCESS
    s = ['<section id="process"><div class="wrap">']
    s.append(sec_head(P["eyebrow"], P["head_a"], P["head_em"], P["intro"]))
    s.append('<div class="pgrid" style="margin-top:34px">')
    for tt, pr, by, bd in P["steps"]:
        s.append('<div class="steprow"><span class="tt">' + esc(tt) + '</span><span class="pr">' + esc(pr) + '</span><span class="by">' + esc(by) + '</span><span class="bd">' + esc(bd) + '</span></div>')
    s.append('</div><div class="pull">' + esc(P["rhythm"]) + '</div>')
    s.append('</div></section>')
    return "".join(s)

def build_pricing():
    P = D.PRICING
    s = ['<section id="pricing"><div class="wrap">']
    s.append(sec_head(P["eyebrow"], P["head_a"], P["head_em"], P["intro"]))
    s.append('<div class="pgrid" style="margin-top:34px">')
    for tt, hc, pr, bd in P["tiers"]:
        s.append('<div class="tierrow"><span class="tt">' + esc(tt) + '</span><span class="hc">' + esc(hc) + '</span><span class="pr">' + esc(pr) + '</span><span class="bd">' + esc(bd) + '</span></div>')
    s.append('</div>')
    s.append('<div class="ptag" style="margin-top:36px">' + esc(P["models_head"]) + '</div><div class="dir">')
    for i, (tt, bd) in enumerate(P["models"]):
        s.append('<div class="dirrow"><span class="no">' + str(i + 1).zfill(2) + '</span><span class="bd"><span class="tt">' + esc(tt) + '</span><div class="st">' + esc(bd) + '</div></span></div>')
    s.append('</div>')
    s.append('</div></section>')
    return "".join(s)

def build_strategy():
    S = D.STRATEGY
    s = ['<section id="strategy"><div class="wrap">']
    s.append(sec_head(S["eyebrow"], S["head_a"], S["head_em"]))
    s.append('<div class="warn">' + esc(S["warn"]) + '</div>')
    s.append('<div class="pgrid" style="margin-top:30px">')
    for tt, stat, bd in S["rows"]:
        s.append('<div class="srow"><div class="tt">' + esc(tt) + '</div><div class="stt">' + esc(stat) + '</div><div class="bd">' + esc(bd) + '</div></div>')
    s.append('</div>')
    s.append('<div class="ptag" style="margin-top:36px">' + esc(S["notes_head"]) + '</div><div class="dir">')
    for tt, bd in S["notes"]:
        s.append('<div class="dirrow"><span class="bd"><span class="tt">' + esc(tt) + '</span><div class="st">' + esc(bd) + '</div></span></div>')
    s.append('</div>')
    # status
    st = D.STATUS
    s.append('<div style="margin-top:56px"><div class="eyebrow">' + esc(st["eyebrow"]) + '</div><div style="margin-top:14px;border-top:1px solid var(--line-gold)">')
    for b, body in st["rows"]:
        s.append('<div class="statusrow"><b>' + esc(b) + '</b><span>' + esc(body) + '</span></div>')
    s.append('</div></div>')
    s.append('</div></section>')
    return "".join(s)

def build_launch():
    L = D2.LAUNCH
    s = ['<section id="launch" class="alt"><div class="wrap">']
    s.append(sec_head(L["eyebrow"], L["head_a"], L["head_em"], L["intro"]))
    s.append('<div class="seatbar" style="margin-top:34px">')
    for i, d in enumerate(D2.LAUNCH_DOORS):
        cls = "seatbtn on" if i == 0 else "seatbtn"
        s.append('<button type="button" class="' + cls + '" id="doorbtn-' + d["id"] + '" onclick="setDoor(\'' + d["id"] + '\')">' + esc(d["label"]) + '</button>')
    s.append('</div>')
    for i, d in enumerate(D2.LAUNCH_DOORS):
        cls = "seatpanel on" if i == 0 else "seatpanel"
        s.append('<div class="' + cls + '" id="door-' + d["id"] + '">')
        s.append('<p class="lede" style="margin-top:22px">' + esc(d["sub"]) + '</p>')
        s.append('<div class="pgrid" style="margin-top:22px">')
        for (pt, meta, steps) in d["phases"]:
            s.append('<div class="acc"><button type="button" class="ahead" onclick="toggleAcc(this.parentNode)"><span class="attl">' + esc(pt) + '</span><span class="ameta">' + esc(meta) + '</span><span class="acaret">&#8250;</span></button><div class="abody">')
            for st in steps:
                s.append('<div class="stepli">' + esc(st) + '</div>')
            s.append('</div></div>')
        s.append('</div>')
        s.append('<div class="pgrid" style="margin-top:22px"><div class="pnl alt2"><div class="ptag">' + esc(d["rules_head"]) + '</div>')
        for r in d["rules"]:
            s.append('<div class="stepli">' + esc(r) + '</div>')
        s.append('</div></div>')
        s.append('</div>')
    s.append('</div></section>')
    return "".join(s)

def build_journeys():
    M = D2.JOURNEYS_META
    s = ['<section id="journeys"><div class="wrap">']
    s.append(sec_head(M["eyebrow"], M["head_a"], M["head_em"], M["intro"]))
    s.append('<div class="pgrid" style="margin-top:34px">')
    for j in D2.JOURNEYS:
        s.append('<div class="acc" id="' + j["id"] + '"><button type="button" class="ahead" onclick="toggleAcc(this.parentNode)"><span class="attl">' + esc(j["name"]) + '<span class="aspn">' + esc(j["spine"]) + '</span></span><span class="ameta">' + esc(j["price"]) + '</span><span class="acaret">&#8250;</span></button><div class="abody">')
        s.append('<div class="ptag">' + esc(j["buyer"]) + '</div><p class="pbody">' + esc(j["body"]) + '</p>')
        day = 0
        for (wl, wt, days) in j["weeks"]:
            s.append('<div class="jweek"><span class="jwl">' + esc(wl) + '</span><div class="jwt">' + esc(wt) + '</div>')
            for dt in days:
                day += 1
                s.append('<div class="dayli"><span class="dayn">Day ' + str(day).zfill(2) + '</span><span>' + esc(dt) + '</span></div>')
            s.append('</div>')
        s.append('</div></div>')
    s.append('</div>')
    s.append('<div class="pull">' + esc(M["rhythm"]) + '</div>')
    R = D2.ROSTER
    s.append('<div style="margin-top:56px"><div class="ptag">' + esc(R["head"]) + '</div><p class="lede" style="margin-top:10px">' + esc(R["intro"]) + '</p><div class="dir">')
    for (tt, ln, dst, bd) in R["rows"]:
        s.append('<div class="dirrow"><span class="bd"><span class="tt">' + esc(tt) + '</span><div class="dst">' + esc(dst) + '</div><div class="st">' + esc(bd) + '</div></span><span class="mt">' + esc(ln) + '</span></div>')
    s.append('</div><p class="lede" style="margin-top:16px">' + esc(R["note"]) + '</p></div>')
    s.append('</div></section>')
    return "".join(s)

def build_founding():
    F = D2.FOUNDING
    s = ['<section id="founding" class="alt"><div class="wrap">']
    s.append(sec_head(F["eyebrow"], F["head_a"], F["head_em"]))
    s.append('<div class="prose">')
    for p in F["argument"]:
        s.append('<p>' + esc(p) + '</p>')
    s.append('</div>')
    s.append('<div class="pgrid two" style="margin-top:30px">')
    s.append('<div class="pnl"><div class="ptag">' + esc(F["gives_head"]) + '</div>')
    for g in F["gives"]:
        s.append('<div class="stepli">' + esc(g) + '</div>')
    s.append('</div><div class="pnl alt2"><div class="ptag">' + esc(F["asks_head"]) + '</div>')
    for a in F["asks"]:
        s.append('<div class="stepli">' + esc(a) + '</div>')
    s.append('</div></div>')
    s.append('<div class="pull">' + esc(F["math"]) + '</div>')
    s.append('<div style="margin-top:44px"><div class="ptag">' + esc(F["toggle_head"]) + '</div>')
    s.append('<div class="seatbar" style="margin-top:16px;max-width:560px">')
    order = ["faith", "values"]
    for i, k in enumerate(order):
        ed = F["editions"][k]
        cls = "seatbtn on" if i == 0 else "seatbtn"
        s.append('<button type="button" class="' + cls + '" id="edbtn-' + k + '" onclick="setEdition(\'' + k + '\')">' + esc(ed["label"]) + '</button>')
    s.append('</div>')
    for i, k in enumerate(order):
        ed = F["editions"][k]
        cls = "seatpanel on" if i == 0 else "seatpanel"
        s.append('<div class="' + cls + '" id="ed-' + k + '"><div class="pgrid" style="margin-top:1px"><div class="pnl"><div class="jwt" style="margin-top:0">' + esc(ed["week"]) + '</div>')
        for n, dt in enumerate(ed["days"]):
            s.append('<div class="dayli"><span class="dayn">Day ' + str(6 + n).zfill(2) + '</span><span>' + esc(dt) + '</span></div>')
        s.append('</div></div></div>')
    s.append('<p class="lede" style="margin-top:16px;max-width:760px">' + esc(F["toggle_note"]) + '</p>')
    s.append('</div>')
    s.append('</div></section>')
    return "".join(s)

JS = (
"var dAns=[null,null,null,null,null,null,null,null,null,null,null,null];\n"
"var fAns=[];var i0;for(i0=0;i0<24;i0++){fAns.push(null);}\n"
"var DB=" + json.dumps([[b[0], b[1], b[2], b[3]] for b in D.BANDS]) + ";\n"
"var FB=" + json.dumps([[b[0], b[1], b[2], b[3]] for b in D.FLOUR_BANDS]) + ";\n"
"function pbbBand(s){var i;for(i=0;i<DB.length;i++){if(s>=DB[i][0]&&s<=DB[i][1]){return DB[i];}}return null;}\n"
"function pbbFlourBand(s){var i;for(i=0;i<FB.length;i++){if(s>=FB[i][0]&&s<=FB[i][1]){return FB[i];}}return null;}\n"
"function dpick(btn){\n"
"  var q=parseInt(btn.getAttribute('data-q'),10);\n"
"  var v=parseInt(btn.getAttribute('data-val'),10);\n"
"  dAns[q]=v;\n"
"  var opts=document.querySelectorAll('.opt[data-q=\"'+q+'\"]');\n"
"  var i;for(i=0;i<opts.length;i++){opts[i].className='opt';}\n"
"  btn.className='opt sel';\n"
"  dRender();\n"
"}\n"
"function dRender(){\n"
"  var t=0,n=0,i;\n"
"  for(i=0;i<dAns.length;i++){if(dAns[i]!==null){t+=dAns[i];n++;}}\n"
"  document.getElementById('d-score').textContent=String(t);\n"
"  document.getElementById('d-prog').textContent=String(n)+' of 12 answered';\n"
"  var out=document.getElementById('d-band');\n"
"  if(n===12){var b=pbbBand(t);\n"
"    document.getElementById('d-band-range').textContent='Your band \u00b7 '+b[0]+'\u2013'+b[1];\n"
"    document.getElementById('d-band-name').textContent=b[2];\n"
"    document.getElementById('d-band-body').textContent=b[3];\n"
"    out.style.display='block';\n"
"  } else {out.style.display='none';}\n"
"}\n"
"function dreset(){\n"
"  var i;for(i=0;i<dAns.length;i++){dAns[i]=null;}\n"
"  var opts=document.querySelectorAll('.opt');\n"
"  for(i=0;i<opts.length;i++){opts[i].className='opt';}\n"
"  dRender();\n"
"}\n"
"function fpick(btn){\n"
"  var q=parseInt(btn.getAttribute('data-q'),10);\n"
"  var v=parseInt(btn.getAttribute('data-val'),10);\n"
"  fAns[q]=v;\n"
"  var btns=document.querySelectorAll('.rbtn[data-q=\"'+q+'\"]');\n"
"  var i;for(i=0;i<btns.length;i++){btns[i].className='rbtn';}\n"
"  btn.className='rbtn sel';\n"
"  fRender();\n"
"}\n"
"function fRender(){\n"
"  var t=0,n=0,i,d;\n"
"  var subs=[0,0,0,0,0,0];var cnt=[0,0,0,0,0,0];\n"
"  for(i=0;i<fAns.length;i++){\n"
"    d=Math.floor(i/4);\n"
"    if(fAns[i]!==null){t+=fAns[i];n++;subs[d]+=fAns[i];cnt[d]++;}\n"
"  }\n"
"  document.getElementById('f-score').textContent=String(t);\n"
"  document.getElementById('f-prog').textContent=String(n)+' of 24 answered';\n"
"  for(d=0;d<6;d++){\n"
"    var el=document.getElementById('fsub-'+d);\n"
"    el.textContent=(cnt[d]===4?String(subs[d]):'\u2013')+' / 20';\n"
"  }\n"
"  var out=document.getElementById('f-band');\n"
"  if(n===24){var b=pbbFlourBand(t);\n"
"    document.getElementById('f-band-range').textContent='Your band \u00b7 '+b[0]+'\u2013'+b[1];\n"
"    document.getElementById('f-band-name').textContent=b[2];\n"
"    document.getElementById('f-band-body').textContent=b[3];\n"
"    out.style.display='block';\n"
"  } else {out.style.display='none';}\n"
"}\n"
"function freset(){\n"
"  var i;for(i=0;i<fAns.length;i++){fAns[i]=null;}\n"
"  var btns=document.querySelectorAll('.rbtn');\n"
"  for(i=0;i<btns.length;i++){btns[i].className='rbtn';}\n"
"  fRender();\n"
"}\n"
"function setSeat(id){\n"
"  var btns=document.querySelectorAll('[id^=\"seatbtn-\"]');\n"
"  var i;for(i=0;i<btns.length;i++){btns[i].className=btns[i].id==='seatbtn-'+id?'seatbtn on':'seatbtn';}\n"
"  var ps=document.querySelectorAll('[id^=\"seat-\"]');\n"
"  for(i=0;i<ps.length;i++){ps[i].className=ps[i].id==='seat-'+id?'seatpanel on':'seatpanel';}\n"
"}\n"
"function toggleAcc(el){\n"
"  if(el.className.indexOf('open')>-1){el.className=el.className.replace(' open','');}\n"
"  else{el.className=el.className+' open';}\n"
"}\n"
"function setDoor(id){\n"
"  var btns=document.querySelectorAll('[id^=\"doorbtn-\"]');\n"
"  var i;for(i=0;i<btns.length;i++){btns[i].className=btns[i].id==='doorbtn-'+id?'seatbtn on':'seatbtn';}\n"
"  var ps=document.querySelectorAll('[id^=\"door-\"]');\n"
"  for(i=0;i<ps.length;i++){ps[i].className=ps[i].id==='door-'+id?'seatpanel on':'seatpanel';}\n"
"}\n"
"function setEdition(id){\n"
"  var btns=document.querySelectorAll('[id^=\"edbtn-\"]');\n"
"  var i;for(i=0;i<btns.length;i++){btns[i].className=btns[i].id==='edbtn-'+id?'seatbtn on':'seatbtn';}\n"
"  var ps=document.querySelectorAll('[id^=\"ed-\"]');\n"
"  for(i=0;i<ps.length;i++){ps[i].className=ps[i].id==='ed-'+id?'seatpanel on':'seatpanel';}\n"
"}\n"
"window.pbbBand=pbbBand;window.pbbFlourBand=pbbFlourBand;window.pbbDReset=dreset;window.pbbFReset=freset;window.pbbToggle=toggleAcc;\n"
)

def build():
    parts = []
    parts.append('<!DOCTYPE html><html lang="en"><head><meta charset="utf-8">')
    parts.append('<meta name="viewport" content="width=device-width,initial-scale=1">')
    parts.append('<title>Purpose Built Business \u2014 The Company Door \u00b7 LifeTogether</title>')
    parts.append('<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="' + FONT_URL + '" rel="stylesheet">')
    parts.append('<style>' + CSS + '</style></head><body>')
    parts.append(build_header())
    parts.append(build_hero())
    parts.append(build_argument())
    parts.append(build_frameworks())
    parts.append(build_diagnostic())
    parts.append(build_flourishing())
    parts.append(build_seats())
    parts.append(build_launch())
    parts.append(build_journeys())
    parts.append(build_library())
    parts.append(build_pricing())
    parts.append(build_founding())
    parts.append(build_strategy())
    parts.append('<div class="foot">' + esc(D.FOOTER) + '</div>')
    parts.append('<script>' + JS + '</script></body></html>')
    return "".join(parts)

if __name__ == "__main__":
    out = build()
    path = "/mnt/user-data/outputs/purpose-built-business.html"
    with open(path, "w", encoding="utf-8") as f:
        f.write(out)
    print("wrote", path, len(out), "bytes")
    print("js braces", JS.count("{") == JS.count("}"), "parens", JS.count("(") == JS.count(")"))
    print("backticks in file:", out.count("`"))
