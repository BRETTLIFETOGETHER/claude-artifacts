# -*- coding: utf-8 -*-
"""Finances Campaign Architecture — Volume 2 COMPLETE (all 5 parts merged).
One cover, 14 section dividers numbered straight through, all 90 blueprints,
continuous page numbering."""
import pathlib
from build import FONT_CSS, CSS, esc, sprig
from build_v2 import EXTRA_CSS, campaign_arch_page   # reuse page template

import data_v2_batch1 as b1
import data_v2_batch2 as b2
import data_v2_batch3 as b3
import data_v2_batch4 as b4
import data_v2_batch5 as b5

ALL_ARCH = b1.ARCH + b2.ARCH + b3.ARCH + b4.ARCH + b5.ARCH
ALL_GROUP_DESC = {}
for mod in (b1, b2, b3, b4, b5):
    ALL_GROUP_DESC.update(mod.GROUP_DESC)

def cover():
    return f"""<div class="page cover">
  <div class="frame"></div>
  <div class="topkick">A LifeTogether Campaign Catalog &nbsp;&middot;&nbsp; Volume Two</div>
  <div class="inner">
    <div class="sprigwrap">{sprig('#c9a35c',34)}</div>
    <h1>Finances</h1>
    <div class="sub1">Campaign Architecture</div>
    <div class="rule"></div>
    <div class="blurb">A complete one-page blueprint for every campaign in the library beyond the flagship ten &mdash; positioning, six-session structure, and a scriptural backbone for all ninety, in fourteen thematic sections.</div>
    <div class="count">The Complete Library &nbsp;&middot;&nbsp; 90 Campaign Blueprints</div>
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
  <div class="dd">{esc(ALL_GROUP_DESC[group])}</div>
  <div class="dcount">{count} Campaigns</div>
  <div class="foot-mark">LifeTogether &middot; Finances Campaign Catalog</div>
  <div class="pgnum">{pg:02d}</div>
</div>"""

def build_html():
    # groups in order of first appearance across the combined list
    order = []
    for c in ALL_ARCH:
        if c['group'] not in order:
            order.append(c['group'])
    pages = [cover()]
    pg = 2
    for idx, g in enumerate(order, 1):
        members = [c for c in ALL_ARCH if c['group'] == g]
        pages.append(group_divider(g, len(members), idx, pg)); pg += 1
        for c in members:
            pages.append(campaign_arch_page(c, pg)); pg += 1
    pages[-1] = pages[-1].replace('class="page"', 'class="page last"', 1)
    body = "\n".join(pages)
    html = (f"<!DOCTYPE html><html><head><meta charset='utf-8'>"
            f"<style>{FONT_CSS}{CSS}{EXTRA_CSS}</style></head><body>{body}</body></html>")
    return html, len(pages), len(order)

if __name__ == "__main__":
    html, n, ngroups = build_html()
    out = pathlib.Path('catalog_v2_complete.html')
    out.write_text(html, encoding='utf-8')
    campaigns = len(ALL_ARCH)
    print(f"HTML written: {out} | pages: {n} | sections: {ngroups} | campaigns: {campaigns} | size {len(html)//1024} KB")
