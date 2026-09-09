# -*- coding: utf-8 -*-
"""Finances Campaign Architecture — Volume 2, Part Two build."""
import pathlib
from build import FONT_CSS, CSS, esc, sprig
from build_v2 import EXTRA_CSS, campaign_arch_page   # reuse page template
from data_v2_batch2 import ARCH, GROUP_DESC

SECTION_START = 4   # these are the 4th-6th sections of the full Volume 2

def cover_v2b():
    return f"""<div class="page cover">
  <div class="frame"></div>
  <div class="topkick">A LifeTogether Campaign Catalog &nbsp;&middot;&nbsp; Volume Two</div>
  <div class="inner">
    <div class="sprigwrap">{sprig('#c9a35c',34)}</div>
    <h1>Finances</h1>
    <div class="sub1">Campaign Architecture</div>
    <div class="rule"></div>
    <div class="blurb">Expanded one-page blueprints for the campaigns behind the library &mdash; positioning, six-session structure, and a scriptural backbone for every title.</div>
    <div class="count">Part Two &nbsp;&middot;&nbsp; 19 Campaign Blueprints</div>
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

def build_html():
    order = []
    for c in ARCH:
        if c['group'] not in order:
            order.append(c['group'])
    pages = [cover_v2b()]
    pg = 2
    for offset, g in enumerate(order):
        idx = SECTION_START + offset
        members = [c for c in ARCH if c['group'] == g]
        pages.append(group_divider(g, len(members), idx, pg)); pg += 1
        for c in members:
            pages.append(campaign_arch_page(c, pg)); pg += 1
    pages[-1] = pages[-1].replace('class="page"', 'class="page last"', 1)
    body = "\n".join(pages)
    html = (f"<!DOCTYPE html><html><head><meta charset='utf-8'>"
            f"<style>{FONT_CSS}{CSS}{EXTRA_CSS}</style></head><body>{body}</body></html>")
    return html, len(pages)

if __name__ == "__main__":
    html, n = build_html()
    out = pathlib.Path('catalog_v2b.html')
    out.write_text(html, encoding='utf-8')
    print(f"HTML written: {out} | pages composed: {n} | size {len(html)//1024} KB")
