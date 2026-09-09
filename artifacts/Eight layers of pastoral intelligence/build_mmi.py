# -*- coding: utf-8 -*-
import html as H
import mmi_data as D

def esc(s):
    return H.escape(s, quote=True)

CSS = """
:root{--blue:#1d4ed8;--blue-soft:#eff4ff;--ink:#0f172a;--mut:#5b6474;--line:#e3e8f0;--bg:#f5f7fb;--card:#ffffff;--good:#0f766e;}
*{box-sizing:border-box;margin:0;padding:0}
html{-webkit-text-size-adjust:100%}
body{font-family:'Inter',-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;background:var(--bg);color:var(--ink);line-height:1.55;font-size:15px}
.wrap{max-width:980px;margin:0 auto;padding:0 16px 64px}
.hdr{padding:34px 0 8px}
.eyebrow{font-size:11px;letter-spacing:.14em;text-transform:uppercase;color:var(--blue);font-weight:700}
h1{font-size:clamp(26px,6vw,40px);line-height:1.12;letter-spacing:-.02em;margin:10px 0 8px;font-weight:800}
h1 sup{font-size:.42em;font-weight:700;vertical-align:super}
.sub{font-size:16px;color:var(--mut);max-width:640px}
.chip{display:inline-block;margin-top:14px;font-size:11px;font-weight:700;letter-spacing:.06em;text-transform:uppercase;color:var(--blue);background:var(--blue-soft);border:1px solid #d3e0fb;border-radius:999px;padding:6px 12px}
.audbar{display:flex;gap:8px;overflow-x:auto;padding:18px 0 6px;-webkit-overflow-scrolling:touch}
.audbar::-webkit-scrollbar{display:none}
.audbtn{flex:0 0 auto;font:inherit;font-size:13px;font-weight:600;padding:8px 14px;border-radius:999px;border:1px solid var(--line);background:var(--card);color:var(--mut);cursor:pointer}
.audbtn.on{background:var(--blue);border-color:var(--blue);color:#fff}
.audtext{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:16px 18px;color:var(--ink);font-size:14.5px;margin-top:8px}
.tabs{position:sticky;top:0;z-index:20;background:var(--bg);display:flex;gap:8px;overflow-x:auto;padding:14px 0 12px;-webkit-overflow-scrolling:touch}
.tabs::-webkit-scrollbar{display:none}
.tab-btn{flex:0 0 auto;font:inherit;font-size:13px;font-weight:700;padding:9px 15px;border-radius:999px;border:1px solid var(--line);background:var(--card);color:var(--ink);cursor:pointer}
.tab-btn.on{background:var(--ink);border-color:var(--ink);color:#fff}
.panel{display:none;padding-top:10px}
.panel.on{display:block}
.card{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:18px;margin:12px 0}
.klabel{font-size:11px;letter-spacing:.12em;text-transform:uppercase;color:var(--blue);font-weight:700;margin-bottom:8px}
.big{font-size:19px;font-weight:800;line-height:1.3;letter-spacing:-.01em}
.mut{color:var(--mut)}
.small{font-size:13px}
.hours{display:flex;gap:12px;margin:14px 0}
.hcell{flex:1;background:var(--card);border:1px solid var(--line);border-radius:12px;padding:18px 14px;text-align:center}
.hcell .n{font-size:clamp(38px,10vw,64px);font-weight:800;letter-spacing:-.04em;line-height:1}
.hcell.hot{border-color:var(--blue);background:var(--blue-soft)}
.hcell.hot .n{color:var(--blue)}
.hcell .l{font-size:12px;color:var(--mut);margin-top:6px}
.doors{display:grid;grid-template-columns:1fr;gap:12px}
.door{border:1px solid var(--line);border-radius:12px;padding:16px;background:var(--card);position:relative}
.door.ch{border-color:var(--blue)}
.door .dl{font-size:11px;letter-spacing:.12em;text-transform:uppercase;font-weight:700;color:var(--mut)}
.door.ch .dl{color:var(--blue)}
.door .dn{font-size:17px;font-weight:800;margin:6px 0}
.door .tag{position:absolute;top:14px;right:14px;font-size:10px;font-weight:700;letter-spacing:.06em;text-transform:uppercase;color:var(--mut);border:1px solid var(--line);border-radius:999px;padding:3px 8px}
.door.ch .tag{color:var(--blue);border-color:#c7d7f8}
.rulebox{border-left:3px solid var(--blue);background:var(--blue-soft);border-radius:0 10px 10px 0;padding:12px 14px;font-size:14px;margin-top:12px}
.grid2{display:grid;grid-template-columns:1fr;gap:10px}
.ig{border:1px solid var(--line);border-radius:10px;padding:12px 14px;background:#fbfcfe}
.ig b{display:block;font-size:13px;margin-bottom:3px}
.ig .small{color:var(--mut)}
.rule{border:1px solid var(--line);border-radius:10px;padding:12px 14px;margin:8px 0;background:#fbfcfe}
.rule b{display:block;font-size:14px}
.rule .small{color:var(--mut);margin-top:3px}
.dcard{background:var(--card);border:1px solid var(--line);border-radius:12px;margin:10px 0;overflow:hidden}
.dhead{display:flex;align-items:baseline;gap:12px;width:100%;text-align:left;font:inherit;background:none;border:0;padding:16px 18px;cursor:pointer}
.dnum{font-size:12px;font-weight:800;color:var(--blue);letter-spacing:.06em}
.dname{font-size:16px;font-weight:800;flex:1}
.dq{font-size:12.5px;color:var(--mut);display:block;margin-top:2px;font-weight:500}
.dbody{display:none;padding:0 18px 18px;border-top:1px solid var(--line)}
.dcard.open .dbody{display:block}
.dbody p{margin:12px 0;font-size:14.5px}
.chips{display:flex;flex-wrap:wrap;gap:6px;margin:10px 0}
.chipx{font-size:12px;border:1px solid var(--line);border-radius:999px;padding:4px 10px;color:var(--mut);background:#fbfcfe}
.toolrow{margin:6px 0;font-size:13.5px;padding-left:14px;position:relative}
.toolrow:before{content:"";position:absolute;left:0;top:8px;width:6px;height:6px;border-radius:2px;background:var(--blue)}
.floor{border-left:3px solid var(--good);background:#f0faf8;border-radius:0 10px 10px 0;padding:10px 12px;font-size:13.5px;margin:12px 0}
.floor b{color:var(--good);font-size:11px;letter-spacing:.1em;text-transform:uppercase;display:block;margin-bottom:2px}
.keyline{font-size:15px;font-weight:700;font-style:italic;border-top:1px solid var(--line);padding-top:12px;margin-top:12px}
.caret{font-weight:800;color:var(--mut);transition:transform .15s;font-size:13px}
.dcard.open .caret{transform:rotate(90deg)}
.qblock{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:16px;margin:10px 0}
.qt{font-size:14.5px;font-weight:700;margin-bottom:10px}
.qn{color:var(--blue);font-weight:800;margin-right:6px}
.opts{display:grid;grid-template-columns:1fr;gap:6px}
.opt{font:inherit;font-size:13.5px;text-align:left;border:1px solid var(--line);border-radius:9px;background:#fbfcfe;padding:9px 12px;cursor:pointer;color:var(--ink)}
.opt.sel{border-color:var(--blue);background:var(--blue-soft);font-weight:600}
.scorebar{position:sticky;bottom:0;background:var(--ink);color:#fff;border-radius:12px;padding:14px 16px;margin-top:14px;display:flex;align-items:center;gap:14px;flex-wrap:wrap}
.scorebar .sn{font-size:26px;font-weight:800;letter-spacing:-.02em}
.scorebar .sl{font-size:12px;opacity:.75}
.scorebar button{margin-left:auto;font:inherit;font-size:12px;font-weight:700;border:1px solid rgba(255,255,255,.35);background:none;color:#fff;border-radius:999px;padding:7px 13px;cursor:pointer}
.bandout{border:1px solid var(--line);border-radius:12px;padding:16px;margin-top:12px;background:var(--card)}
.bandout .bn{font-size:17px;font-weight:800;color:var(--blue)}
.bandout .br{font-size:12px;color:var(--mut);font-weight:700;letter-spacing:.06em}
.bands{margin-top:14px}
.bandrow{border:1px solid var(--line);border-radius:10px;padding:12px 14px;margin:8px 0;background:#fbfcfe}
.bandrow b{font-size:14px}
.bandrow .rg{font-size:11px;color:var(--blue);font-weight:800;letter-spacing:.06em;margin-right:8px}
.bandrow .small{color:var(--mut);margin-top:3px}
.seatbar{display:flex;gap:8px;overflow-x:auto;padding-bottom:4px}
.seatbtn{flex:1 0 auto;font:inherit;font-size:13px;font-weight:700;padding:10px 14px;border-radius:10px;border:1px solid var(--line);background:var(--card);cursor:pointer}
.seatbtn.on{border-color:var(--blue);background:var(--blue-soft);color:var(--blue)}
.seatpanel{display:none}
.seatpanel.on{display:block}
.pathrow{display:flex;gap:12px;border-top:1px solid var(--line);padding:10px 0;font-size:14px}
.pathrow b{flex:0 0 84px;font-size:11px;letter-spacing:.08em;text-transform:uppercase;color:var(--blue);padding-top:2px}
.track{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:15px 16px;margin:9px 0}
.track .tt{font-size:15px;font-weight:800}
.track .tb{font-size:13.5px;color:var(--mut);margin-top:4px}
.tstat{float:right;font-size:10px;font-weight:800;letter-spacing:.06em;text-transform:uppercase;border-radius:999px;padding:4px 9px;margin-left:10px}
.st-built{background:#e8f6f3;color:var(--good);border:1px solid #bfe6de}
.st-worked{background:var(--blue-soft);color:var(--blue);border:1px solid #c7d7f8}
.st-conf{background:#f2f4f8;color:var(--mut);border:1px solid var(--line)}
.days{display:grid;grid-template-columns:repeat(2,1fr);gap:8px;margin-top:10px}
.day{border:1px solid var(--line);border-radius:9px;padding:9px 11px;font-size:13px;background:#fbfcfe}
.day b{color:var(--blue);margin-right:6px}
.jstage{background:var(--card);border:1px solid var(--line);border-radius:12px;margin:10px 0;overflow:hidden}
.jhead{display:flex;align-items:center;gap:12px;width:100%;text-align:left;font:inherit;background:none;border:0;padding:15px 16px;cursor:pointer}
.jnum{flex:0 0 30px;height:30px;border-radius:999px;background:var(--blue);color:#fff;font-weight:800;font-size:13px;display:flex;align-items:center;justify-content:center}
.jname{font-size:15px;font-weight:800;flex:1}
.jbody{display:none;padding:0 16px 15px 58px;font-size:14px;color:var(--ink)}
.jstage.open .jbody{display:block}
.price{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:16px;margin:10px 0}
.price .pt{font-size:15px;font-weight:800}
.price .pb{font-size:13.5px;color:var(--mut);margin:5px 0 10px}
.prow{display:flex;justify-content:space-between;border-top:1px solid var(--line);padding:8px 0;font-size:14px}
.prow b{font-weight:800}
.statrow{border:1px solid var(--line);border-radius:10px;padding:12px 14px;margin:8px 0;background:#fbfcfe;font-size:13.5px}
.statrow b{display:block;font-size:11px;letter-spacing:.1em;text-transform:uppercase;color:var(--blue);margin-bottom:3px}
.foot{margin-top:36px;padding-top:18px;border-top:1px solid var(--line);font-size:11.5px;color:var(--mut);letter-spacing:.04em;text-align:center}
@media(min-width:720px){
 body{font-size:16px}
 .grid2{grid-template-columns:1fr 1fr}
 .doors{grid-template-columns:1fr 1fr}
 .opts{grid-template-columns:1fr 1fr}
 .days{grid-template-columns:repeat(3,1fr)}
}
"""

def build_overview():
    o = D.OVERVIEW; t = D.TWO_DOORS
    s = []
    s.append('<div class="hours"><div class="hcell"><div class="n">' + o["hours_left_num"] + '</div><div class="l">' + esc(o["hours_left_label"]) + '</div></div>')
    s.append('<div class="hcell hot"><div class="n">' + o["hours_right_num"] + '</div><div class="l">' + esc(o["hours_right_label"]) + '</div></div></div>')
    s.append('<div class="card"><div class="klabel">' + esc(o["insight_head"]) + '</div><div class="big">' + esc(o["insight_line"]) + '</div><p class="mut" style="margin-top:10px">' + esc(o["insight_body"]) + '</p><div class="keyline">' + esc(o["map_line"]) + '</div></div>')
    s.append('<div class="card"><div class="klabel">' + esc(o["pair_head"]) + '</div><p>' + esc(o["pair_body"]) + '</p></div>')
    # two doors
    s.append('<div class="card"><div class="klabel">' + esc(t["head"]) + '</div><div class="doors">')
    c = t["church"]
    s.append('<div class="door ch"><span class="tag">' + esc(c["tag"]) + '</span><div class="dl">' + esc(c["label"]) + '</div><div class="dn">' + esc(c["name"]) + '</div><div class="small mut">' + esc(c["body"]) + '</div></div>')
    c = t["company"]
    s.append('<div class="door"><span class="tag">' + esc(c["tag"]) + '</span><div class="dl">' + esc(c["label"]) + '</div><div class="dn">' + esc(c["name"]) + '</div><div class="small mut">' + esc(c["body"]) + '</div></div>')
    s.append('</div><div class="rulebox">' + esc(t["rule"]) + '</div></div>')
    # integration
    s.append('<div class="card"><div class="klabel">Wired into the platform</div><div class="grid2">')
    for name, body in D.INTEGRATION:
        s.append('<div class="ig"><b>' + esc(name) + '</b><span class="small">' + esc(body) + '</span></div>')
    s.append('</div></div>')
    # rules
    s.append('<div class="card"><div class="klabel">Six integrity rules \u2014 non-negotiable</div>')
    for b, body in D.RULES:
        s.append('<div class="rule"><b>' + esc(b) + '</b><div class="small">' + esc(body) + '</div></div>')
    s.append('</div>')
    return "".join(s)

def build_domains():
    s = ['<p class="mut" style="margin:6px 2px 4px">Six domains, each with sub-topics, tools, a stated floor, and the line. Tap a domain to open it.</p>']
    for i, d in enumerate(D.DOMAINS):
        s.append('<div class="dcard" id="dcard-' + str(i) + '">')
        s.append('<button class="dhead" type="button" onclick="toggleAcc(this.parentNode)"><span class="dnum">' + d["num"] + '</span><span class="dname">' + esc(d["name"]) + '<span class="dq">' + esc(d["q"]) + '</span></span><span class="caret">&#8250;</span></button>')
        s.append('<div class="dbody"><p>' + esc(d["body"]) + '</p>')
        s.append('<div class="chips">' + "".join('<span class="chipx">' + esc(x) + '</span>' for x in d["subs"]) + '</div>')
        s.append('<div class="klabel" style="margin-top:12px">Tools</div>')
        for tool in d["tools"]:
            s.append('<div class="toolrow">' + esc(tool) + '</div>')
        s.append('<div class="floor"><b>The floor</b>' + esc(d["floor"]) + '</div>')
        s.append('<div class="keyline">' + esc(d["line"]) + '</div>')
        s.append('</div></div>')
    return "".join(s)

def build_diag():
    s = ['<div class="card"><div class="klabel">The instrument</div><p>' + esc(D.DIAG_INTRO["purpose"]) + '</p><p class="small mut" style="margin-top:8px">' + esc(D.DIAG_INTRO["confidential"]) + '</p></div>']
    for qi, (qt, opts) in enumerate(D.DIAGNOSTIC):
        s.append('<div class="qblock"><div class="qt"><span class="qn">' + str(qi + 1).zfill(2) + '</span>' + esc(qt) + '</div><div class="opts">')
        for oi, (label, val) in enumerate(opts):
            s.append('<button type="button" class="opt" data-q="' + str(qi) + '" data-val="' + str(val) + '" onclick="pick(this)">' + esc(label) + '</button>')
        s.append('</div></div>')
    s.append('<div class="scorebar"><div><span class="sn" id="score-num">0</span><span class="sl"> / 48</span></div><div class="sl" id="score-prog">0 of 12 answered</div><button type="button" onclick="resetDiag()">Reset</button></div>')
    s.append('<div class="bandout" id="band-out" style="display:none"><div class="br" id="band-range"></div><div class="bn" id="band-name"></div><p class="small mut" id="band-body" style="margin-top:6px"></p></div>')
    s.append('<div class="bands"><div class="klabel" style="margin:14px 2px 4px">The four bands</div>')
    for lo, hi, name, body in D.BANDS:
        s.append('<div class="bandrow"><span class="rg">' + str(lo) + '\u2013' + str(hi) + '</span><b>' + esc(name) + '</b><div class="small">' + esc(body) + '</div></div>')
    s.append('</div>')
    s.append('<div class="card"><div class="klabel">Discernment \u2014 the lowest score is not automatically the first priority</div>')
    for name, q in D.DISCERNMENT:
        s.append('<div class="pathrow"><b>' + esc(name) + '</b><span>' + esc(q) + '</span></div>')
    s.append('</div>')
    return "".join(s)

def build_seats():
    s = ['<div class="seatbar">']
    for i, seat in enumerate(D.SEATS):
        cls = "seatbtn on" if i == 0 else "seatbtn"
        s.append('<button type="button" class="' + cls + '" id="seatbtn-' + seat["id"] + '" onclick="setSeat(\'' + seat["id"] + '\')">' + esc(seat["label"]) + '</button>')
    s.append('</div>')
    for i, seat in enumerate(D.SEATS):
        cls = "seatpanel on" if i == 0 else "seatpanel"
        s.append('<div class="' + cls + '" id="seat-' + seat["id"] + '">')
        s.append('<div class="card"><div class="klabel">The question</div><div class="big">' + esc(seat["q"]) + '</div><p class="mut" style="margin-top:10px">' + esc(seat["who"]) + '</p>')
        s.append('<div style="margin-top:12px">')
        for label, body in seat["path"]:
            s.append('<div class="pathrow"><b>' + esc(label) + '</b><span>' + esc(body) + '</span></div>')
        s.append('</div></div></div>')
    s.append('<div class="rulebox">' + esc(D.SEAT_NOTE) + '</div>')
    return "".join(s)

def stat_class(stat):
    low = stat.lower()
    if "worked" in low: return "st-worked"
    if "built" in low: return "st-built"
    return "st-conf"

def build_formation():
    s = ['<div class="card"><p>' + esc(D.FORMATION_INTRO) + '</p></div>']
    for title, body, stat, kind in D.TRACKS:
        s.append('<div class="track"><span class="tstat ' + stat_class(stat) + '">' + esc(stat) + '</span><div class="tt">' + esc(title) + '</div><div class="tb">' + esc(body) + '</div></div>')
    dv = D.DEVO
    s.append('<div class="card"><div class="klabel">' + esc(dv["head"]) + '</div><p class="small mut">' + esc(dv["body"]) + '</p><div class="days">')
    for day, txt in dv["days"]:
        s.append('<div class="day"><b>' + esc(day) + '</b>' + esc(txt) + '</div>')
    s.append('</div></div>')
    s.append('<div class="card"><div class="klabel">' + esc(D.STORY["head"]) + '</div><p>' + esc(D.STORY["body"]) + '</p></div>')
    s.append('<div class="card"><div class="klabel">' + esc(D.SERMON_MAP["head"]) + '</div><p class="small mut">' + esc(D.SERMON_MAP["body"]) + '</p></div>')
    return "".join(s)

def build_journey():
    s = ['<div class="card"><p>' + esc(D.JOURNEY_INTRO) + '</p></div>']
    for num, name, body in D.JOURNEY:
        s.append('<div class="jstage"><button class="jhead" type="button" onclick="toggleAcc(this.parentNode)"><span class="jnum">' + num + '</span><span class="jname">' + esc(name) + '</span><span class="caret">&#8250;</span></button><div class="jbody">' + esc(body) + '</div></div>')
    return "".join(s)

def build_pricing():
    s = ['<div class="card"><p>' + esc(D.PRICING_INTRO) + '</p></div>']
    for title, body, rows in D.PRICING:
        s.append('<div class="price"><div class="pt">' + esc(title) + '</div><div class="pb">' + esc(body) + '</div>')
        for label, val in rows:
            s.append('<div class="prow"><span>' + esc(label) + '</span><b>' + esc(val) + '</b></div>')
        s.append('</div>')
    s.append('<div class="card"><div class="klabel">Status \u2014 stated honestly</div>')
    for b, body in D.STATUS:
        s.append('<div class="statrow"><b>' + esc(b) + '</b>' + esc(body) + '</div>')
    s.append('</div>')
    return "".join(s)

TABS = [
    ("ov", "Overview", build_overview),
    ("dom", "Six Domains", build_domains),
    ("diag", "Diagnostic", build_diag),
    ("seats", "Three Seats", build_seats),
    ("form", "Formation Library", build_formation),
    ("journey", "The Owner's Journey", build_journey),
    ("price", "Pricing & Status", build_pricing),
]

JS = (
"var answers=[null,null,null,null,null,null,null,null,null,null,null,null];\n"
"var BANDS=" + repr([[b[0], b[1], b[2], b[3]] for b in [(lo, hi, n, bd) for lo, hi, n, bd in __import__('mmi_data').BANDS]]).replace("'", '"') + ";\n"
"function showTab(id){\n"
"  var btns=document.querySelectorAll('.tab-btn');\n"
"  var i;\n"
"  for(i=0;i<btns.length;i++){btns[i].className=btns[i].id==='tabbtn-'+id?'tab-btn on':'tab-btn';}\n"
"  var ps=document.querySelectorAll('.panel');\n"
"  for(i=0;i<ps.length;i++){ps[i].className=ps[i].id==='panel-'+id?'panel on':'panel';}\n"
"}\n"
"function setAud(id){\n"
"  var btns=document.querySelectorAll('.audbtn');\n"
"  var i;\n"
"  for(i=0;i<btns.length;i++){btns[i].className=btns[i].id==='audbtn-'+id?'audbtn on':'audbtn';}\n"
"  var ts=document.querySelectorAll('.audtext');\n"
"  for(i=0;i<ts.length;i++){ts[i].style.display=ts[i].id==='audtext-'+id?'block':'none';}\n"
"}\n"
"function toggleAcc(card){\n"
"  if(card.className.indexOf('open')>-1){card.className=card.className.replace(' open','');}\n"
"  else{card.className=card.className+' open';}\n"
"}\n"
"function mmiBand(score){\n"
"  var i;\n"
"  for(i=0;i<BANDS.length;i++){if(score>=BANDS[i][0]&&score<=BANDS[i][1]){return BANDS[i];}}\n"
"  return null;\n"
"}\n"
"function mmiScore(){\n"
"  var t=0,n=0,i;\n"
"  for(i=0;i<answers.length;i++){if(answers[i]!==null){t+=answers[i];n++;}}\n"
"  return {total:t,answered:n};\n"
"}\n"
"function pick(btn){\n"
"  var q=parseInt(btn.getAttribute('data-q'),10);\n"
"  var v=parseInt(btn.getAttribute('data-val'),10);\n"
"  answers[q]=v;\n"
"  var opts=document.querySelectorAll('.opt[data-q=\"'+q+'\"]');\n"
"  var i;\n"
"  for(i=0;i<opts.length;i++){opts[i].className='opt';}\n"
"  btn.className='opt sel';\n"
"  renderScore();\n"
"}\n"
"function renderScore(){\n"
"  var s=mmiScore();\n"
"  document.getElementById('score-num').textContent=String(s.total);\n"
"  document.getElementById('score-prog').textContent=String(s.answered)+' of 12 answered';\n"
"  var out=document.getElementById('band-out');\n"
"  if(s.answered===12){\n"
"    var b=mmiBand(s.total);\n"
"    document.getElementById('band-range').textContent='Your band \u00b7 '+b[0]+'\u2013'+b[1];\n"
"    document.getElementById('band-name').textContent=b[2];\n"
"    document.getElementById('band-body').textContent=b[3];\n"
"    out.style.display='block';\n"
"  } else {out.style.display='none';}\n"
"}\n"
"function resetDiag(){\n"
"  var i;\n"
"  for(i=0;i<answers.length;i++){answers[i]=null;}\n"
"  var opts=document.querySelectorAll('.opt');\n"
"  for(i=0;i<opts.length;i++){opts[i].className='opt';}\n"
"  renderScore();\n"
"}\n"
"function setSeat(id){\n"
"  var btns=document.querySelectorAll('.seatbtn');\n"
"  var i;\n"
"  for(i=0;i<btns.length;i++){btns[i].className=btns[i].id==='seatbtn-'+id?'seatbtn on':'seatbtn';}\n"
"  var ps=document.querySelectorAll('.seatpanel');\n"
"  for(i=0;i<ps.length;i++){ps[i].className=ps[i].id==='seat-'+id?'seatpanel on':'seatpanel';}\n"
"}\n"
"window.mmiBand=mmiBand;window.mmiScore=mmiScore;window.mmiPick=pick;window.mmiReset=resetDiag;\n"
)

def build():
    parts = []
    parts.append('<!DOCTYPE html><html lang="en"><head><meta charset="utf-8">')
    parts.append('<meta name="viewport" content="width=device-width,initial-scale=1">')
    parts.append('<title>Marketplace Ministry Intelligence \u2014 The Church Door</title>')
    parts.append('<link rel="preconnect" href="https://fonts.googleapis.com"><link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">')
    parts.append('<style>' + CSS + '</style></head><body><div class="wrap">')
    m = D.META
    parts.append('<div class="hdr"><div class="eyebrow">' + esc(m["eyebrow"]) + '</div>')
    parts.append('<h1>' + esc(m["title"]) + '<sup>' + m["tm"] + '</sup></h1>')
    parts.append('<div class="sub">' + esc(m["subtitle"]) + '</div>')
    parts.append('<span class="chip">' + esc(m["status_chip"]) + '</span></div>')
    # audience segmentation
    parts.append('<div class="audbar">')
    for i, a in enumerate(D.AUDIENCES):
        cls = "audbtn on" if i == 0 else "audbtn"
        parts.append('<button type="button" class="' + cls + '" id="audbtn-' + a["id"] + '" onclick="setAud(\'' + a["id"] + '\')">' + esc(a["label"]) + '</button>')
    parts.append('</div>')
    for i, a in enumerate(D.AUDIENCES):
        style = '' if i == 0 else ' style="display:none"'
        parts.append('<div class="audtext" id="audtext-' + a["id"] + '"' + style + '>' + esc(a["text"]) + '</div>')
    # tabs
    parts.append('<div class="tabs">')
    for i, (tid, label, _) in enumerate(TABS):
        cls = "tab-btn on" if i == 0 else "tab-btn"
        parts.append('<button type="button" class="' + cls + '" id="tabbtn-' + tid + '" onclick="showTab(\'' + tid + '\')">' + esc(label) + '</button>')
    parts.append('</div>')
    for i, (tid, label, fn) in enumerate(TABS):
        cls = "panel on" if i == 0 else "panel"
        parts.append('<div class="' + cls + '" id="panel-' + tid + '">' + fn() + '</div>')
    parts.append('<div class="foot">' + esc(D.FOOTER) + '</div>')
    parts.append('</div><script>' + JS + '</script></body></html>')
    return "".join(parts)

if __name__ == "__main__":
    out = build()
    path = "/mnt/user-data/outputs/marketplace-ministry-intelligence.html"
    with open(path, "w", encoding="utf-8") as f:
        f.write(out)
    print("wrote", path, len(out), "bytes")
    # quick sanity: brace balance in the JS block
    js = JS
    print("js braces", js.count("{") == js.count("}"), "parens", js.count("(") == js.count(")"))
