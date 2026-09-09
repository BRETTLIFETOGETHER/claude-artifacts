# -*- coding: utf-8 -*-
"""Finances Campaign Architecture — Volume 2 build (reuses Volume 1 engine)."""
import pathlib
from build import FONT_CSS, CSS, esc, sprig          # reuse V1 design system
from data_v2_batch1 import ARCH, GROUP_DESC

# ---- additional CSS just for Volume 2 elements -------------------------------
EXTRA_CSS = """
/* scriptural backbone chips */
.bb{display:flex;gap:6px;flex-wrap:wrap;}
.bb-chip{font-family:'Archivo',sans-serif;font-weight:600;font-size:7.6px;letter-spacing:.04em;
 background:var(--ever-pale);color:var(--ever);padding:3px 8px;border-radius:3px;}
/* group divider */
.divider{display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;}
.divider .dk{font-family:'Archivo',sans-serif;font-weight:700;letter-spacing:.3em;font-size:8.5px;
 text-transform:uppercase;color:var(--gold-deep);}
.divider .dnum{font-family:'Playfair',serif;font-weight:800;font-size:64px;color:var(--ever-pale);
 line-height:1;margin:6px 0 2px;}
.divider .dt{font-family:'Playfair',serif;font-weight:800;font-size:38px;color:var(--ever);
 line-height:1.05;max-width:6in;}
.divider .drule{width:90px;height:2px;background:linear-gradient(90deg,transparent,var(--gold),transparent);
 margin:20px auto;}
.divider .dd{font-family:'Spectral',serif;font-style:italic;font-size:13.5px;line-height:1.6;
 color:var(--ink2);max-width:5in;}
.divider .dcount{margin-top:22px;font-family:'Archivo',sans-serif;font-weight:700;font-size:8.5px;
 letter-spacing:.24em;text-transform:uppercase;color:var(--cream);background:var(--ever);
 padding:7px 16px;border-radius:2px;}
.divider .dsprig{margin-bottom:14px;}
"""

# ---- pages -------------------------------------------------------------------
def cover_v2():
    return f"""<div class="page cover">
  <div class="frame"></div>
  <div class="topkick">A LifeTogether Campaign Catalog &nbsp;&middot;&nbsp; Volume Two</div>
  <div class="inner">
    <div class="sprigwrap">{sprig('#c9a35c',34)}</div>
    <h1>Finances</h1>
    <div class="sub1">Campaign Architecture</div>
    <div class="rule"></div>
    <div class="blurb">Expanded one-page blueprints for the campaigns behind the library &mdash; positioning, six-session structure, and a scriptural backbone for every title.</div>
    <div class="count">Part One &nbsp;&middot;&nbsp; 21 Campaign Blueprints</div>
  </div>
  <div class="wm">
    <div class="lt">LifeTogether</div>
    <div class="tag">Churchwide &amp; Workplace Campaigns</div>
  </div>
</div>"""

def group_divider(group, count, idx, pg):
    return f"""<div class="page divider">
  <div class="dsprig">{sprig('var(--ever)',30)}</div>
  <div class="dk">Section {idx} &nbsp;&middot;&nbsp; The Complete Library, Expanded</div>
  <div class="dnum">{idx:02d}</div>
  <div class="dt">{esc(group)}</div>
  <div class="drule"></div>
  <div class="dd">{esc(GROUP_DESC[group])}</div>
  <div class="dcount">{count} Campaigns</div>
  <div class="foot-mark">LifeTogether &middot; Finances Campaign Catalog</div>
  <div class="pgnum">{pg:02d}</div>
</div>"""

def campaign_arch_page(c, pg):
    badge_cls = 't2' if c['tier'].startswith('Tier 2') else 't1'
    formats = "".join(f'<span class="pill">{esc(f)}</span>' for f in c['formats'])
    info = [
        ("The Felt Need", c['felt_need']),
        ("Why It Matters", c['why_matters']),
        ("The Core Problem", c['problem']),
        ("The Transformation", c['transformation']),
    ]
    info_html = "".join(
        f'<div class="info-card"><div class="lab">{esc(l)}</div><p>{esc(v)}</p></div>'
        for l, v in info)
    sess = ""
    for i, (st, sd) in enumerate(c['sessions'], 1):
        sess += (f'<div class="sess"><div class="n">{i}</div><div>'
                 f'<div class="st">{esc(st)}</div><div class="sd">{esc(sd)}</div></div></div>')
    chips = "".join(f'<span class="bb-chip">{esc(r)}</span>' for r in c['scriptures'])
    return f"""<div class="page">
  <div class="c-top">
    <div class="kicker">{esc(c['group'])} &nbsp;&middot;&nbsp; N<sup>o</sup> {c['num']:02d}</div>
    <span class="badge {badge_cls}">{esc(c['tier'])}</span>
  </div>
  <hr class="grule" style="margin:6px 0 12px;">
  <h1 class="c-title">{esc(c['title'])}</h1>
  <div class="c-tag">{esc(c['tagline'])}</div>
  <div class="scrip" style="margin:13px 0 13px;">
    <div class="q">&ldquo;{esc(c['core_text'])}&rdquo;</div>
    <div class="r">{esc(c['core_ref'])}</div>
  </div>
  <p class="c-lead" style="margin-bottom:13px;">{esc(c['marketing'])}</p>
  <div class="info2" style="margin-bottom:14px;">{info_html}</div>
  <div class="sec-h" style="margin-bottom:9px;">The Six-Session Small-Group Journey</div>
  <div class="sess-grid" style="margin-bottom:13px;">{sess}</div>
  <div class="sec-h" style="margin-bottom:8px;">Scriptural Backbone</div>
  <div class="bb" style="margin-bottom:14px;">{chips}</div>
  <hr class="hair" style="margin:0 0 11px;">
  <div class="foot-row">
    <div>
      <div style="font-family:'Archivo';font-weight:700;letter-spacing:.16em;font-size:7.2px;text-transform:uppercase;color:var(--ever2);margin-bottom:5px;">Available Formats</div>
      <div class="pills">{formats}</div>
    </div>
    <div class="aud-line">{esc(c['audience'])}</div>
  </div>
  <div class="foot-mark">LifeTogether &middot; Finances Campaign Catalog</div>
  <div class="pgnum">{pg:02d}</div>
</div>"""

def build_html():
    # group order as it appears in ARCH
    order = []
    for c in ARCH:
        if c['group'] not in order:
            order.append(c['group'])
    pages = [cover_v2()]
    pg = 2
    for idx, g in enumerate(order, 1):
        members = [c for c in ARCH if c['group'] == g]
        pages.append(group_divider(g, len(members), idx, pg)); pg += 1
        for c in members:
            pages.append(campaign_arch_page(c, pg)); pg += 1
    # last page: stop trailing blank
    pages[-1] = pages[-1].replace('class="page"', 'class="page last"', 1)
    body = "\n".join(pages)
    html = (f"<!DOCTYPE html><html><head><meta charset='utf-8'>"
            f"<style>{FONT_CSS}{CSS}{EXTRA_CSS}</style></head><body>{body}</body></html>")
    return html, len(pages)

if __name__ == "__main__":
    html, n = build_html()
    out = pathlib.Path('catalog_v2.html')
    out.write_text(html, encoding='utf-8')
    print(f"HTML written: {out} | pages composed: {n} | size {len(html)//1024} KB")
