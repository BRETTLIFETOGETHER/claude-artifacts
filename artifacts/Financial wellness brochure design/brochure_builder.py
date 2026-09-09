# -*- coding: utf-8 -*-
"""Reusable LifeTogether collection-brochure builder.
Aesthetic direction borrowed from the Flourishing Series PDF.
Call build(collection, titles, out_html) then to_pdf(out_html, out_pdf)."""

import pathlib

GOLD = "#c9a13b"
GOLD_LT = "#dcc074"
NAVY = "#172542"
INK = "#1c1c1c"
CREAM = "#f9f5ec"


def _title_html(title, ti):
    return f"{title} <em>{ti}</em>".strip()


def _tags(tags, cls="tag"):
    return "".join(f'<span class="{cls}">{t}</span>' for t in tags)


def _overview_cards(titles, tier_badge="Tier&nbsp;1"):
    out = []
    for t in titles:
        out.append(f"""
        <div class="ov-card" style="--ac:{t['accent']};--tint:{t['tint']}">
          <div class="ov-num">{t['num']}</div>
          <div class="ov-body">
            <div class="ov-title">{_title_html(t['title'], t['title_italic'])}</div>
            <div class="ov-sub">{t['subtitles'][0]}</div>
            <div class="ov-badges"><span>30-Day</span><span>4-Session</span><span>{tier_badge}</span></div>
          </div>
        </div>""")
    return "\n".join(out)


def _session_cards(t):
    cells = []
    for s in t["sessions"]:
        cells.append(f"""
          <div class="sess">
            <div class="sess-head">
              <div class="sess-label">SESSION {s['n']}</div>
              <div class="sess-title">{_title_html(s['title'], s['ti'])}</div>
            </div>
            <div class="sess-verse">{s['verse']}</div>
            <p class="sess-line">{s['line']}</p>
          </div>""")
    return "\n".join(cells)


def _info_rows(info, tier_row="Tier 1 — top-demand category"):
    rows = ['<li><span class="ik">Format</span><span class="iv">30-Day Journey + 4-Session Small Group</span></li>']
    for k, v in info.items():
        rows.append(f'<li><span class="ik">{k}</span><span class="iv">{v}</span></li>')
    rows.append(f'<li><span class="ik">Tier</span><span class="iv">{tier_row}</span></li>')
    return "\n".join(rows)


def _subtitle_box(subs):
    items = "".join(f"<p>{s}</p>" for s in subs)
    return f'<div class="subbox"><div class="boxlabel">SUBTITLE OPTIONS</div>{items}</div>'


def _spread(t, tier_row="Tier 1 — top-demand category"):
    return f"""
  <section class="spread" style="--ac:{t['accent']};--ac-soft:{t['accent_soft']};--tint:{t['tint']}">
    <header class="band">
      <div class="band-num">{t['num']}</div>
      <div class="band-text">
        <div class="eyebrow gold">{t['eyebrow']}</div>
        <h2 class="band-title">{_title_html(t['title'], t['title_italic'])}</h2>
        <p class="strap">{t['strap']}</p>
      </div>
    </header>
    <div class="cols">
      <div class="col-main">
        <p class="pullquote">&ldquo;{t['quote']}&rdquo;</p>
        <p class="body"><span class="lede">The problem.</span> {t['problem']}</p>
        <p class="body"><span class="lede">The transformation.</span> {t['transformation']}</p>
        <div class="scripture">
          <div class="boxlabel light">CORE SCRIPTURE</div>
          <p class="verse">&ldquo;{t['scripture']}&rdquo;</p>
          <div class="verse-ref">— {t['scripture_ref']}</div>
        </div>
      </div>
      <aside class="col-side">
        <div class="infobox">
          <div class="boxlabel light">CAMPAIGN INFORMATION</div>
          <ul class="info">
            {_info_rows(t['info'], tier_row)}
          </ul>
        </div>
        {_subtitle_box(t['subtitles'])}
      </aside>
    </div>
    <div class="bigidea">
      <div class="boxlabel light">THE BIG IDEA</div>
      <p>{t['big_idea']}</p>
      <div class="tags">{_tags(t['tags'], "tag light")}</div>
    </div>
    <div class="curriculum">
      <div class="curr-label">SMALL-GROUP CURRICULUM — FOUR SESSIONS</div>
      <div class="sess-grid">
        {_session_cards(t)}
      </div>
    </div>
  </section>"""


def build(collection, titles, out_html):
    c = collection
    tier_row = c.get("tier_row", "Tier 1 — top-demand category")
    tier_badge = c.get("tier_badge", "Tier&nbsp;1")
    stats = c.get("stats", [
        {"big": "10", "lab": "Tier-One Campaigns"},
        {"big": "30", "lab": "Day Journey Each"},
        {"big": "40", "lab": "Small-Group Sessions"},
        {"big": "2", "lab": "Audiences · Church &amp; Work"},
    ])
    cover_strip = "".join(
        f'<div><div class="cs-big">{s["big"]}</div><div class="cs-lab">{s["lab"]}</div></div>'
        for s in stats)
    spreads = "\n".join(_spread(t, tier_row) for t in titles)
    overview = _overview_cards(titles, tier_badge)
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{c['doc_title']}</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,500;0,600;0,700;0,800;1,500;1,600;1,700&family=Spectral:ital,wght@0,300;0,400;0,500;0,600;1,400;1,500&family=Archivo:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>
  :root{{ --gold:{GOLD}; --gold-lt:{GOLD_LT}; --navy:{NAVY}; --ink:{INK}; --cream:{CREAM}; }}
  *{{box-sizing:border-box;}}
  html{{-webkit-text-size-adjust:100%;}}
  body{{margin:0; background:#e7e2d6; color:var(--ink); font-family:'Spectral',Georgia,serif; line-height:1.6; -webkit-font-smoothing:antialiased;}}
  .page{{max-width:940px; margin:0 auto; background:#fff; box-shadow:0 1px 60px rgba(20,30,55,.14);}}
  .eyebrow{{font-family:'Archivo',sans-serif; font-weight:600; font-size:11px; letter-spacing:.28em; text-transform:uppercase;}}
  .gold{{color:var(--gold);}}
  em{{font-style:italic;}}

  .cover{{background:radial-gradient(120% 90% at 78% -10%, rgba(201,161,59,.20), transparent 55%), linear-gradient(160deg,#1c2c50 0%, var(--navy) 55%, #111d36 100%); color:#f3eee2; padding:88px 70px 64px; position:relative; overflow:hidden;}}
  .cover::before{{content:""; position:absolute; left:0; right:0; top:0; height:6px; background:linear-gradient(90deg,var(--gold),var(--gold-lt));}}
  .cover .eyebrow{{color:var(--gold-lt); margin-bottom:38px;}}
  .cover h1{{font-family:'Playfair Display',serif; font-weight:700; font-size:104px; line-height:.94; margin:0 0 26px; letter-spacing:-.02em;}}
  .cover h1 em{{color:var(--gold-lt); font-weight:600;}}
  .cover .deck{{font-size:21px; line-height:1.55; max-width:600px; color:#e6ddc9; font-weight:300; margin:0 0 46px;}}
  .cover-strip{{display:flex; gap:0; border-top:1px solid rgba(220,192,116,.32); padding-top:26px; flex-wrap:wrap;}}
  .cover-strip div{{flex:1 1 0; min-width:140px; padding:4px 22px 4px 0; border-right:1px solid rgba(220,192,116,.18);}}
  .cover-strip div:last-child{{border-right:0;}}
  .cs-big{{font-family:'Playfair Display',serif; font-size:38px; color:var(--gold-lt); line-height:1;}}
  .cs-lab{{font-family:'Archivo',sans-serif; font-size:10.5px; letter-spacing:.18em; text-transform:uppercase; color:#cdc3ac; margin-top:8px;}}

  .frame{{padding:66px 70px 60px; background:var(--cream);}}
  .frame .section-eyebrow{{color:var(--gold); margin-bottom:22px; display:block;}}
  .frame-quote{{background:var(--navy); color:#efe9da; border-radius:3px; padding:34px 40px; margin:0 0 46px; position:relative;}}
  .frame-quote::before{{content:""; position:absolute; left:0; top:0; bottom:0; width:4px; background:linear-gradient(var(--gold),var(--gold-lt));}}
  .frame-quote .boxlabel{{margin-bottom:14px;}}
  .frame-quote p{{font-family:'Spectral',serif; font-style:italic; font-size:18.5px; line-height:1.62; margin:0; color:#f1ead9;}}
  .frame-intro p{{font-size:17px; line-height:1.72; margin:0 0 18px; color:#33312c;}}

  .overview{{padding:56px 70px 64px; background:#fff;}}
  .overview h3{{font-family:'Playfair Display',serif; font-weight:600; font-size:30px; margin:0 0 6px; color:var(--navy);}}
  .overview .sub{{font-size:15px; color:#6f6a5d; margin:0 0 34px; font-style:italic;}}
  .ov-grid{{display:grid; grid-template-columns:1fr 1fr; gap:16px;}}
  .ov-card{{display:flex; gap:18px; align-items:stretch; background:var(--tint); border-radius:4px; overflow:hidden; border:1px solid rgba(0,0,0,.05);}}
  .ov-num{{flex:0 0 56px; background:var(--ac); color:#fff; font-family:'Playfair Display',serif; font-size:30px; font-weight:600; display:flex; align-items:center; justify-content:center;}}
  .ov-body{{padding:14px 18px 14px 0;}}
  .ov-title{{font-family:'Playfair Display',serif; font-size:21px; color:var(--navy); line-height:1.1;}}
  .ov-title em{{color:var(--ac);}}
  .ov-sub{{font-size:12.5px; color:#5f5a4f; margin:5px 0 9px; font-style:italic; line-height:1.4;}}
  .ov-badges span{{font-family:'Archivo',sans-serif; font-size:9px; letter-spacing:.1em; text-transform:uppercase; background:rgba(0,0,0,.06); color:#4a463d; padding:3px 8px; border-radius:20px; margin-right:5px;}}

  .spread{{background:var(--tint); padding:0 0 58px;}}
  .band{{background:var(--ac); color:#fff; padding:46px 70px 40px; display:flex; gap:30px; align-items:flex-start; position:relative; overflow:hidden;}}
  .band::after{{content:""; position:absolute; left:0; right:0; bottom:0; height:4px; background:linear-gradient(90deg,var(--gold),var(--gold-lt));}}
  .band-num{{font-family:'Playfair Display',serif; font-size:118px; font-weight:700; line-height:.8; color:rgba(255,255,255,.14); margin-top:-6px; flex:0 0 auto;}}
  .band-text{{padding-top:8px;}}
  .band .eyebrow{{color:var(--gold-lt); margin-bottom:14px; display:block;}}
  .band-title{{font-family:'Playfair Display',serif; font-weight:700; font-size:52px; margin:0 0 14px; line-height:1; letter-spacing:-.01em;}}
  .band-title em{{color:var(--gold-lt); font-weight:600;}}
  .strap{{font-size:16.5px; line-height:1.55; max-width:620px; color:rgba(255,255,255,.86); margin:0; font-style:italic; font-weight:300;}}

  .cols{{display:grid; grid-template-columns:1.55fr 1fr; gap:34px; padding:44px 70px 0;}}
  .pullquote{{font-family:'Playfair Display',serif; font-style:italic; font-weight:500; font-size:26px; line-height:1.32; color:var(--ac); margin:0 0 26px; letter-spacing:-.01em;}}
  .body{{font-size:15.5px; line-height:1.72; margin:0 0 18px; color:#322f2a;}}
  .lede{{font-family:'Archivo',sans-serif; font-weight:700; font-size:11px; letter-spacing:.12em; text-transform:uppercase; color:var(--ac); margin-right:6px;}}
  .scripture{{background:var(--ac); color:#f3eee2; border-radius:3px; padding:26px 30px; margin-top:28px;}}
  .scripture .verse{{font-family:'Spectral',serif; font-style:italic; font-size:17px; line-height:1.55; margin:0 0 12px; color:#f4eedd;}}
  .verse-ref{{font-family:'Archivo',sans-serif; font-size:11px; letter-spacing:.14em; text-transform:uppercase; color:var(--gold-lt);}}

  .col-side > div{{margin-bottom:18px;}}
  .infobox{{background:var(--ac); color:#eee; border-radius:3px; padding:22px 24px;}}
  .info{{list-style:none; margin:0; padding:0;}}
  .info li{{display:flex; flex-direction:column; padding:9px 0; border-bottom:1px solid rgba(255,255,255,.12);}}
  .info li:last-child{{border-bottom:0; padding-bottom:0;}}
  .ik{{font-family:'Archivo',sans-serif; font-size:9.5px; letter-spacing:.16em; text-transform:uppercase; color:var(--gold-lt); margin-bottom:3px;}}
  .iv{{font-size:13.5px; line-height:1.4; color:#f2eee4;}}
  .subbox{{background:#fff; border:1px solid rgba(0,0,0,.08); border-left:3px solid var(--gold); border-radius:3px; padding:20px 22px;}}
  .subbox p{{font-style:italic; font-size:13.5px; line-height:1.4; margin:0 0 10px; color:#4f4a40;}}
  .subbox p:last-child{{margin-bottom:0;}}

  .boxlabel{{font-family:'Archivo',sans-serif; font-weight:700; font-size:10px; letter-spacing:.2em; text-transform:uppercase; color:var(--ac); margin-bottom:12px;}}
  .boxlabel.light{{color:var(--gold-lt);}}

  .bigidea{{margin:36px 70px 0; background:var(--ac-soft); color:#f4efe4; border-radius:3px; padding:32px 38px;}}
  .bigidea p{{font-family:'Playfair Display',serif; font-style:italic; font-weight:500; font-size:22px; line-height:1.42; margin:0 0 20px; color:#f6f0e3; letter-spacing:-.005em;}}
  .tags{{display:flex; flex-wrap:wrap; gap:8px;}}
  .tag{{font-family:'Archivo',sans-serif; font-size:10.5px; letter-spacing:.06em; background:rgba(255,255,255,.10); color:#efe8d8; padding:5px 12px; border-radius:20px; border:1px solid rgba(255,255,255,.16);}}

  .curriculum{{margin:40px 70px 0;}}
  .curr-label{{font-family:'Archivo',sans-serif; font-weight:700; font-size:10.5px; letter-spacing:.24em; text-transform:uppercase; color:var(--ac); border-bottom:1px solid rgba(0,0,0,.12); padding-bottom:12px; margin-bottom:20px;}}
  .sess-grid{{display:grid; grid-template-columns:1fr 1fr; gap:16px;}}
  .sess{{background:#fff; border:1px solid rgba(0,0,0,.07); border-radius:4px; overflow:hidden;}}
  .sess-head{{background:var(--ac); color:#fff; padding:14px 18px 13px;}}
  .sess-label{{font-family:'Archivo',sans-serif; font-size:9px; letter-spacing:.2em; text-transform:uppercase; color:var(--gold-lt); margin-bottom:5px;}}
  .sess-title{{font-family:'Playfair Display',serif; font-size:19px; line-height:1.05;}}
  .sess-title em{{color:var(--gold-lt);}}
  .sess-verse{{font-family:'Archivo',sans-serif; font-size:10.5px; letter-spacing:.1em; text-transform:uppercase; color:var(--ac); padding:13px 18px 0;}}
  .sess-line{{font-size:13.5px; line-height:1.55; color:#403c34; padding:6px 18px 18px; margin:0; font-style:italic;}}

  .closing{{background:radial-gradient(120% 100% at 20% 0%, rgba(201,161,59,.18), transparent 55%), linear-gradient(150deg,#1b2b4f, var(--navy) 60%, #101c34); color:#f1ebdc; padding:80px 70px 70px; position:relative;}}
  .closing::before{{content:""; position:absolute; left:0; right:0; top:0; height:6px; background:linear-gradient(90deg,var(--gold),var(--gold-lt));}}
  .closing .eyebrow{{color:var(--gold-lt); margin-bottom:26px; display:block;}}
  .closing h2{{font-family:'Playfair Display',serif; font-weight:700; font-size:64px; line-height:.98; margin:0 0 32px; letter-spacing:-.02em;}}
  .closing h2 em{{color:var(--gold-lt); font-weight:600;}}
  .closing .cbody{{max-width:620px;}}
  .closing .cbody p{{font-size:17px; line-height:1.7; color:#e3dac6; margin:0 0 18px; font-weight:300;}}
  .cta{{margin-top:42px; padding-top:30px; border-top:1px solid rgba(220,192,116,.3);}}
  .cta-label{{font-family:'Archivo',sans-serif; font-weight:700; font-size:11px; letter-spacing:.26em; text-transform:uppercase; color:var(--gold-lt); margin-bottom:14px;}}
  .cta-line{{font-family:'Playfair Display',serif; font-style:italic; font-size:27px; line-height:1.3; color:#f4eede; margin:0;}}

  .footer{{background:#0e1830; color:#9aa3b6; font-family:'Archivo',sans-serif; font-size:11px; letter-spacing:.1em; padding:20px 70px; text-align:center;}}
  .footer .gold{{color:var(--gold-lt);}}

  @media(max-width:760px){{
    .cover{{padding:60px 30px 44px;}}
    .cover h1{{font-size:62px;}}
    .frame,.overview,.closing{{padding-left:30px; padding-right:30px;}}
    .band{{padding:34px 30px 30px; flex-direction:column; gap:8px;}}
    .band-num{{font-size:74px;}}
    .band-title{{font-size:38px;}}
    .cols{{grid-template-columns:1fr; padding:32px 30px 0; gap:24px;}}
    .bigidea,.curriculum{{margin-left:30px; margin-right:30px;}}
    .sess-grid,.ov-grid{{grid-template-columns:1fr;}}
    .closing h2{{font-size:44px;}}
    .footer{{padding:18px 24px;}}
  }}
  @media print{{
    body{{background:#fff;}}
    .page{{box-shadow:none; max-width:none;}}
    .spread, .cover, .frame, .overview, .closing{{page-break-inside:avoid; break-inside:avoid;}}
    .spread{{page-break-before:always;}}
    .cover,.closing,.band,.scripture,.infobox,.bigidea,.sess-head,.frame-quote,.ov-num{{-webkit-print-color-adjust:exact; print-color-adjust:exact;}}
  }}
  @page{{margin:0;}}
</style>
</head>
<body>
<div class="page">
  <section class="cover">
    <div class="eyebrow">{c['eyebrow']}</div>
    <h1>{c['title_line1']}<br><em>{c['title_line2_italic']}</em></h1>
    <p class="deck">{c['deck']}</p>
    <div class="cover-strip">
      {cover_strip}
    </div>
  </section>

  <section class="frame">
    <span class="eyebrow section-eyebrow">THE GOVERNING FRAMEWORK</span>
    <div class="frame-quote">
      <div class="boxlabel light">{c['framework_label']}</div>
      <p>{c['framework']}</p>
    </div>
    <div class="frame-intro">
      <p>{c['intro'][0]}</p>
      <p>{c['intro'][1]}</p>
    </div>
  </section>

  <section class="overview">
    <h3>{c['overview_title']}</h3>
    <p class="sub">{c['overview_sub']}</p>
    <div class="ov-grid">
      {overview}
    </div>
  </section>

  {spreads}

  <section class="closing">
    <span class="eyebrow">WHY THIS CAMPAIGN MATTERS</span>
    <h2>{c['closing_title_a']}<br><em>{c['closing_title_b_italic']}</em></h2>
    <div class="cbody">
      <p>{c['closing_body'][0]}</p>
      <p>{c['closing_body'][1]}</p>
    </div>
    <div class="cta">
      <div class="cta-label">{c['cta_label']}</div>
      <p class="cta-line">{c['cta_line']}</p>
    </div>
  </section>

  <div class="footer"><span class="gold">Lifetogether</span> &nbsp;·&nbsp; {c['contact']}</div>
</div>
</body>
</html>"""
    pathlib.Path(out_html).write_text(html, encoding="utf-8")
    return html


def to_pdf(out_html, out_pdf):
    from playwright.sync_api import sync_playwright
    src = pathlib.Path(out_html).resolve().as_uri()
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page(viewport={"width": 940, "height": 1247}, device_scale_factor=2)
        pg.goto(src)
        pg.wait_for_timeout(1800)
        pg.emulate_media(media="print")
        pg.pdf(path=out_pdf, width="940px", height="1247px", print_background=True,
               margin={"top": "0", "bottom": "0", "left": "0", "right": "0"})
        b.close()
    return out_pdf
