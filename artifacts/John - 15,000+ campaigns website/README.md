# 40daycampaigns.com — v2 Platform Build (17,443-row master)

A complete, self-contained static site: **16,379 browsable campaigns & studies** plus **940 nested
Red Letter sessions** (17,319 active items), built entirely from
`Updated_40_Day_Campaign_Master__4_.xlsx` — every catalog entry traces to a Master ID; nothing
was invented. English at the root, Spanish under `/es/`, Portuguese under `/pt/`.

## Run it
No build step, no server, no network. Open `index.html` from this folder, or upload the folder
as-is to any static host (Netlify, Vercel, S3+CloudFront, cPanel). All fonts are base64-embedded;
there are zero external requests. Data ships as `.js` files so the site also works from `file://`.

## What's inside
- `*.html` — 24 pages ×3 languages (72 files): home, browse, channel/theme/campaign (parameterized),
  finder, builder, formats, included, pricing, how-it-works, for-pastors, for-churches, seasonal,
  about, case-studies, faq, cart, checkout, confirmation, account, signin/signup, contact.
- `assets/css` — design system (`site.css`) + embedded fonts (`fonts.css`: Hanken Grotesk,
  Spectral, Archivo — subset for EN/ES/PT).
- `assets/js` — `covers.js` (deterministic SVG cover engine, gold reserved for flagship),
  `app.js` (data layer, cart, pricing), `browse.js` (virtualized 16k-row catalog, inverted-index
  search, faceted filters, URL state), `campaign.js` (detail pages: daily arc, sermon builds,
  sample-day print/Word/Canva exports), `flows.js` (finder, builder, cart→checkout→confirmation,
  account).
- `data/` — `index.js` (compact catalog, 2.3 MB), 23 per-channel shards loaded on demand,
  `scripture.js` (verified reference pools + word banks), `meta.js`, plus `.json` twins of everything.
- `i18n/` — the full string tables per language.
- `build/` — the reproducible pipeline (see below).
- `VALIDATION.txt` — every gate, pass/fail, with counts.

## Data provenance
17,443 source rows → **excluded 124**: 81 third-party Market Benchmark products (reference-only per
the master's Conflict Flags), 36 rows marked "Do not build now", 7 structural DOCX headers.
940 "Life of Christ Supporting Content" rows are **nested** under their 150 Red Letter parent
series (visible on those campaign pages), leaving 16,379 top-level entries. The 304 rows flagged
"Do Not Send to AI Yet" are included as browsable listings only — the flag governs AI content
generation, which was not applied to them. Twenty source rows echo third-party program names
("Financial Peace", "Experiencing God", …); they are retained per the master's own Build Decisions
and listed in VALIDATION.txt for rename review.

## Taxonomy
23 channels derived from the real category structure (the 15-channel spec was a floor, not a
ceiling): the master's own families demanded Life of Christ & Red Letter, Family Legacy &
Generations, Work & Marketplace, Church Vision & Values, Ministries & Nonprofits, Seasons of Life,
Health/Healing & Care, and Bible & Scripture Studies as first-class channels, plus the two
validated white-space channels — **Doubt & Honest Faith** and **Digital Discernment & Faith in
the Age of AI** — marked NEW on the homepage. 1,742 themes sit beneath them. Audience is an
affinity filter, never a channel.

## Stripe seam
`assets/js/flows.js`, in the checkout block, contains a marked comment titled
**STRIPE INTEGRATION SEAM** with the exact fetch call to swap in. Until it is wired, checkout
validates, stores the order locally, unlocks the four starter downloads (real, editable .doc files
generated client-side), and routes to confirmation — so the flow is demonstrable end-to-end today.

## Scripture standard
All references are named to the NIV standard and validated against a canonical verse-count table
at build time (461 distinct refs; zero invalid). Where verse text is embedded in generated
documents, wording stays paraphrase/KJV-safe pending the Biblica NIV license flagged for platform
scale. 2,352 rows sit in themes larger than their channel's verified pool, so backbone references
repeat there in spaced rotation — disclosed in VALIDATION.txt rather than papered over with
invented citations.

## Languages
ES and PT are full editions: navigation, marketing pages, channel and format names, commerce,
and legal strings are translated in ministry register. **Campaign titles remain English** —
translating 16,379 titles is an editorial ministry-copy pass, not a build step; the string tables
in `/i18n` are ready to receive them.

## Regenerating from the master
From `build/` in order: `generate_data.py` (taxonomy, exclusions, nesting, attributes) →
`emit_site_data.py` (Scripture assignment, shards, index) → `fonts.py` (fetch + subset + embed) →
`pages.py` (all 72 pages) → `node smoke.js` → `validate.py` (writes VALIDATION.txt, exits non-zero
on any hard failure). Requires Python 3 with pandas, fonttools, brotli, beautifulsoup4, and Node
with jsdom. Note: the build container's network allowlist blocks Chromium downloads, so runtime
verification uses jsdom; run a Playwright crawl in CI once hosted.
