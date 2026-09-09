# -*- coding: utf-8 -*-
"""Shared campaign page builders (detail + 40-day map)."""
BRAND = "Lifetogether"

def camp_detail(c):
    tags = "".join(f'<span class="tag">{t}</span>' for t in c['tags'])
    fmts = "".join(f'<span class="fmt">{f}</span>' for f in c['formats'])
    sessions = ""
    for i, (st, sd) in enumerate(c['sessions']):
        sessions += (f'<div class="sess"><div class="sn">Session {i+1}</div>'
                     f'<div class="st">{st}</div><div class="sd">{sd}</div></div>')
    scrips = ""
    for ref, note in c['scriptures']:
        scrips += (f'<div style="margin-bottom:4px; line-height:1.2;">'
                   f'<span style="font-family:Archivo;font-weight:700;font-size:7.6pt;'
                   f'color:var(--navy);letter-spacing:.03em;">{ref}</span> '
                   f'<span class="scrip" style="font-size:7.9pt;">&mdash; {note}</span></div>')
    return f"""
<div class="page">
  <div class="content">
    <div class="sec-head">
      <span class="kicker">Campaign {c['num']} &middot; {c['badge']}</span>
    </div>
    <h1 style="font-size:30pt; margin:5px 0 7px;">{c['title_html']}</h1>
    <p class="scrip" style="font-size:9.2pt; color:var(--ink2);">{c['scripture']}</p>
    <div style="margin:8px 0 9px;">{tags}</div>
    <p style="font-size:9.6pt; line-height:1.55; color:var(--ink);">{c['description']}</p>

    <div class="two" style="margin:11px 0 0;">
      <div class="lblbox">
        <div class="l">The Problem</div><p>{c['problem']}</p>
      </div>
      <div class="lblbox" style="border-left-color:var(--green2);">
        <div class="l" style="color:var(--green2);">The Transformation</div><p>{c['transform']}</p>
      </div>
    </div>

    <div style="margin-top:11px;">
      <div class="lblbox" style="border-left-color:var(--navy); background:var(--cream3);">
        <div class="l" style="color:var(--navy);">Why This Campaign Matters</div>
        <p style="font-size:8.8pt;">{c['why']}</p>
      </div>
    </div>

    <div class="divider" style="margin:13px 0 10px;"></div>
    <div class="kicker gr">Six-Session Small Group Outline</div>
    <div class="two" style="margin-top:8px;">{sessions}</div>

    <div class="divider" style="margin:11px 0 10px;"></div>
    <div class="colpair" style="gap:22px;">
      <div>
        <div class="kicker gr">Key Scriptures</div>
        <div style="margin-top:8px;">{scrips}</div>
      </div>
      <div>
        <div class="kicker gr">Suggested Formats</div>
        <div style="margin-top:8px;">{fmts}</div>
        <div class="kicker gr" style="margin-top:14px;">Intended Audience</div>
        <p class="scrip" style="margin-top:7px; font-size:8.6pt;">{c['audience_detail']}</p>
      </div>
    </div>

    <div class="lfooter">
      <span>Finances Campaign Catalog &middot; {c['title_plain']}</span>
      <span class="bk">{BRAND}</span>
    </div>
  </div>
</div>"""


def camp_map(c):
    movements = ""
    for header, sub, days in c['map']:
        dayshtml = ""
        for dn, dt, ds, refs in days:
            dayshtml += (f'<div class="day"><span class="dn">DAY {dn}</span> '
                         f'<span class="dt">{dt}</span>'
                         f'<div class="ds">{ds}</div>'
                         f'<div class="dref">{refs}</div></div>')
        movements += (f'<div class="movement"><div class="mv-head">{header}'
                      f'<span class="sub">{sub}</span></div>{dayshtml}</div>')
    return f"""
<div class="page">
  <div class="content">
    <div class="hbar">
      <div class="kicker">{c['title_plain']}</div>
      <h2>The 40-Day <span class="it">Engagement Map</span></h2>
      <div class="sub">Forty days of formation &mdash; daily title, focus, and Scripture. The architecture for devotionals, not the devotionals themselves.</div>
    </div>
    <div class="daymap" style="margin-top:14px;">{movements}</div>
    <div class="lfooter">
      <span>Finances Campaign Catalog &middot; {c['title_plain']} &middot; 40-Day Map</span>
      <span class="bk">{BRAND}</span>
    </div>
  </div>
</div>"""
