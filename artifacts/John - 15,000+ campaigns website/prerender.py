#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""SEO surface for a long-tail catalog.
Prerenders every Grade-AA flagship campaign as a real static page at /c/<slug>.html
with its own title, meta description, canonical URL, and Product JSON-LD, hydrating
through the same campaign.js. Also writes sitemap.xml and robots.txt.
The remaining ~16k campaigns stay client-rendered behind crawlable channel/theme pages."""
import json, os, sys, html
sys.path.insert(0, "/home/claude/build")
from strings import EN
import pages  # reuse the exact EN campaign template

SITE = "/home/claude/site"
SITE_URL = "https://40daycampaigns.com"
idx = json.load(open(f"{SITE}/data/meta.json"))
data = json.load(open(f"{SITE}/data/index.json"))
C = {k: i for i, k in enumerate(data["cols"])}
rows = data["rows"]
refs = data["refs"]

pages.CURRENT_FNAME[0] = None
base = pages.page_campaign(EN, "../")  # correct asset/nav paths from /c/

os.makedirs(f"{SITE}/c", exist_ok=True)
aa = [r for r in rows if r[C["g"]] == "AA"]
FMT_PRICE = {8: 849, 4: 649, 2: 449, 1: 249, 16: 549, 32: 149, 64: 199, 128: 1499}
def top_price(f):
    for bit in (8, 4, 2, 1, 16, 128, 64, 32):
        if f & bit: return FMT_PRICE[bit] + 200  # AA premium
    return 849

made = 0
for r in aa:
    slug, t, s = r[C["slug"]], r[C["t"]], r[C["s"]] or ""
    ref = refs[r[C["sb"]]] if 0 <= r[C["sb"]] < len(refs) else ""
    title = f"{t} — 40 Day Campaign | Lifetogether"
    desc = (s or f"A churchwide campaign anchored in {ref}.")
    desc = (desc[:150] + "…") if len(desc) > 152 else desc
    ld = json.dumps({"@context": "https://schema.org", "@type": "Product",
        "name": t, "description": desc,
        "brand": {"@type": "Brand", "name": "Lifetogether 40 Day Campaigns"},
        "offers": {"@type": "Offer", "priceCurrency": "USD",
                   "price": str(top_price(r[C["f"]])),
                   "availability": "https://schema.org/InStock",
                   "url": f"{SITE_URL}/c/{slug}.html"}}, ensure_ascii=False)
    page = base
    page = page.replace("<title>Campaign — 40 Day Campaigns</title>", f"<title>{html.escape(title)}</title>")
    page = page.replace('<meta name="description" content="' + html.escape(EN["desc"]) + '">',
                        f'<meta name="description" content="{html.escape(desc)}">')
    inject = (f'<link rel="canonical" href="{SITE_URL}/c/{slug}.html">\n'
              f'<script type="application/ld+json">{ld}</script>\n'
              f'<script>window.CAMPAIGN_ID="{r[C["id"]]}";</script>\n')
    page = page.replace('<link rel="stylesheet" href="../assets/css/fonts.css">',
                        inject + '<link rel="stylesheet" href="../assets/css/fonts.css">')
    open(f"{SITE}/c/{slug}.html", "w").write(page)
    made += 1

# ---------------- sitemap ----------------
STATIC = ["index.html","browse.html","finder.html","builder.html","formats.html","included.html",
 "pricing.html","how-it-works.html","for-pastors.html","for-churches.html","seasonal.html",
 "about.html","case-studies.html","faq.html","contact.html"]
urls = []
for pf in ("", "es/", "pt/"):
    urls += [f"{SITE_URL}/{pf}{f}" for f in STATIC]
urls += [f"{SITE_URL}/channel.html?c={i}" for i in range(idx["channels"])]
urls += [f"{SITE_URL}/c/{r[C['slug']]}.html" for r in aa]
sm = ['<?xml version="1.0" encoding="UTF-8"?>',
      '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
for u in urls:
    sm.append(f"<url><loc>{html.escape(u)}</loc></url>")
sm.append("</urlset>")
open(f"{SITE}/sitemap.xml", "w").write("\n".join(sm))
open(f"{SITE}/robots.txt", "w").write(f"User-agent: *\nAllow: /\nSitemap: {SITE_URL}/sitemap.xml\n")
print(f"prerendered {made} flagship pages · sitemap {len(urls)} URLs · robots.txt written")
