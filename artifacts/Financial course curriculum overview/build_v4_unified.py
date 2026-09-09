# -*- coding: utf-8 -*-
"""Finances Complete Campaign Library — UNIFIED single document.
Catalog cover as the only title page; two intro pages; then every campaign that
has a 40-day map, in numeric order 1->100, each a flagship-style two-page spread
(overview + 40-day map); the 100-title library index and closing at the very end.
Maps are added in batches via the MAPS_* imports below; the document grows toward
all 100 as batches land."""
import pathlib
from build import (FONT_CSS, CSS, esc, cover_page,
                   overview_page_1, overview_page_2, campaign_map_page,
                   library_pages, closing_page, TOP10)
from build_v2_complete import ALL_ARCH
from data_maps_b1 import MAPS as MAPS_B1
from data_maps_b2 import MAPS as MAPS_B2
from data_maps_b3 import MAPS as MAPS_B3
from data_maps_b4 import MAPS as MAPS_B4
from data_maps_b5 import MAPS as MAPS_B5
from data_maps_b6 import MAPS as MAPS_B6
from data_maps_b7 import MAPS as MAPS_B7
from data_maps_b8 import MAPS as MAPS_B8
from data_maps_b9 import MAPS as MAPS_B9
from data_maps_b10 import MAPS as MAPS_B10
from data_maps_b11 import MAPS as MAPS_B11
from data_maps_b12 import MAPS as MAPS_B12
from data_maps_b13 import MAPS as MAPS_B13
from data_maps_b14 import MAPS as MAPS_B14
from data_maps_b15 import MAPS as MAPS_B15

# merge all map batches here as they are built
MAPS_ALL = {}
for batch in (MAPS_B1, MAPS_B2, MAPS_B3, MAPS_B4, MAPS_B5, MAPS_B6, MAPS_B7, MAPS_B8, MAPS_B9, MAPS_B10, MAPS_B11, MAPS_B12, MAPS_B13, MAPS_B14, MAPS_B15):
    MAPS_ALL.update(batch)

def overview_unified(c, pg):
    """Flagship-style overview page used for ALL campaigns (1-100), so every
    spread looks identical. Kicker names the flagship or the campaign's theme."""
    badge_cls = 't2' if c['tier'].startswith('Tier 2') else 't1'
    kick = "Flagship Campaign" if c['num'] <= 10 else c.get('group', 'Campaign')
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
    return f"""<div class="page">
  <div class="c-top">
    <div class="kicker gold">{esc(kick)} &nbsp;&middot;&nbsp; N<sup>o</sup> {c['num']:02d}</div>
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
  <div class="sess-grid" style="margin-bottom:14px;">{sess}</div>
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
    # all campaign dicts by number (flagships + the 90), maps attached
    by_num = {}
    for c in TOP10:          # flagships 1-10 (already carry movements)
        by_num[c['num']] = c
    for c in ALL_ARCH:       # 11-100
        by_num[c['num']] = c
    for num, movs in MAPS_ALL.items():
        if num in by_num:
            by_num[num]['movements'] = movs
    included = [by_num[n] for n in sorted(by_num)]   # ALL campaigns, numeric order

    # standardize the format options shown on every campaign:
    # drop the 4-Session option; keep 6-Session, 21-Day, 30-Day, 40-Day
    STD_FORMATS = ["6-Session", "21-Day", "30-Day", "40-Day"]
    for c in included:
        c['formats'] = list(STD_FORMATS)

    pages = [cover_page()]                       # single title page (unnumbered)
    pg = 2
    pages.append(overview_page_1(pg)); pg += 1   # The Finances Category
    pages.append(overview_page_2(pg)); pg += 1   # Built for Your Church / Workplace
    mapped = 0
    for c in included:
        pages.append(overview_unified(c, pg)); pg += 1
        if 'movements' in c:                     # full flagship-style 40-day map
            pages.append(campaign_map_page(c, pg)); pg += 1
            mapped += 1
    lib = library_pages(pg); pages.extend(lib); pg += len(lib)   # complete library index
    pages.append(closing_page(pg))               # closing CTA (keeps its .last)

    body = "\n".join(pages)
    html = (f"<!DOCTYPE html><html><head><meta charset='utf-8'>"
            f"<style>{FONT_CSS}{CSS}</style></head><body>{body}</body></html>")
    return html, len(pages), len(included), mapped

if __name__ == "__main__":
    html, n, ncampaigns, mapped = build_html()
    out = pathlib.Path('catalog_unified.html')
    out.write_text(html, encoding='utf-8')
    print(f"HTML written: {out} | pages: {n} | campaigns: {ncampaigns} | full spreads (with 40-day map): {mapped} | size {len(html)//1024} KB")
