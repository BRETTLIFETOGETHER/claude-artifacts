# -*- coding: utf-8 -*-
"""Finances Complete Campaign Library — Volume 1 (Catalog) + Volume 2 (Architecture)
combined into ONE continuously-paginated document, catalog first."""
import pathlib
from build import (FONT_CSS, CSS, TOP10,
                   cover_page, overview_page_1, overview_page_2,
                   top10_overview_page, campaign_overview_page,
                   campaign_map_page, library_pages, closing_page)
from build_v2 import EXTRA_CSS, campaign_arch_page
from build_v2_complete import (cover as arch_cover, group_divider,
                               ALL_ARCH, ALL_GROUP_DESC)

def build_html():
    pages = []

    # ===== VOLUME 1 — CAMPAIGN CATALOG =====
    pages.append(cover_page())                       # physical 1 (unnumbered cover)
    pg = 2
    pages.append(overview_page_1(pg)); pg += 1
    pages.append(overview_page_2(pg)); pg += 1
    pages.append(top10_overview_page(pg)); pg += 1
    for c in TOP10:
        pages.append(campaign_overview_page(c, pg)); pg += 1
        pages.append(campaign_map_page(c, pg)); pg += 1
    lib = library_pages(pg); pages.extend(lib); pg += len(lib)
    # catalog closing page hardcodes .last; force a normal page break so Vol 2 starts fresh
    closing = closing_page(pg).replace('class="page last"', 'class="page"', 1)
    pages.append(closing); pg += 1                   # now pg = 30

    # ===== VOLUME 2 — CAMPAIGN ARCHITECTURE =====
    pages.append(arch_cover())                       # physical 30 (unnumbered cover)
    pg += 1                                           # next printed page = 31
    order = []
    for c in ALL_ARCH:
        if c['group'] not in order:
            order.append(c['group'])
    for idx, g in enumerate(order, 1):
        members = [c for c in ALL_ARCH if c['group'] == g]
        pages.append(group_divider(g, len(members), idx, pg)); pg += 1
        for c in members:
            pages.append(campaign_arch_page(c, pg)); pg += 1

    # final physical page stops the trailing blank
    pages[-1] = pages[-1].replace('class="page"', 'class="page last"', 1)

    body = "\n".join(pages)
    html = (f"<!DOCTYPE html><html><head><meta charset='utf-8'>"
            f"<style>{FONT_CSS}{CSS}{EXTRA_CSS}</style></head><body>{body}</body></html>")
    return html, len(pages)

if __name__ == "__main__":
    html, n = build_html()
    out = pathlib.Path('catalog_master.html')
    out.write_text(html, encoding='utf-8')
    print(f"HTML written: {out} | total pages: {n} | size {len(html)//1024} KB")
