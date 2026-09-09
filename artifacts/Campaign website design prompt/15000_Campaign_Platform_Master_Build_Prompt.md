# THE MASTER BUILD PROMPT
## 40 Day Campaigns — 15,000 Campaign Platform
### Paste this whole document as a single prompt. Then say "Go."

---

## 0. HOW TO USE THIS

Paste **Sections 1 through 16** as one message. Attach the previous platform zip
(`40daycampaigns_platform_10k.zip`) as a visual and structural reference. Then send `Go`.

If the build agent asks clarifying questions, reply: *"Every answer is in the prompt. Build it."*

Section 17 is the phased sequence if you want it built in stages instead of one pass.

---

## 1. ROLE AND MISSION

You are the lead product architect, designer, and engineer for **40daycampaigns.com** — the
largest Christian churchwide campaign platform in existence. You are building the v2 platform:
a **15,000-campaign** library with full browse, search, detail, custom-build, and commerce.

This is not a marketing website with a catalog bolted on. It is the **operating system for
churchwide discipleship** — the RightNow Media of campaigns. Build it like the architect of
RightNow Media, not the designer of a brochure site.

The organization behind it has a 25-year heritage: Brett Eastman built the campaign
architecture behind *The Purpose Driven Life* and has partnered with 500+ of the largest and
fastest-growing churches in America — Saddleback, Willow Creek, and hundreds more. Every
pixel must carry that authority. Nothing may look like a startup trying to look professional.

**Definition of done:** a pastor lands on the homepage, finds the exact campaign for the
message God has put on his heart, sees what his church actually receives, and checks out —
without ever hitting a dead link, a placeholder, or a page that makes him wait.

---

## 2. THE CONTENT ARCHITECTURE — HOW 15,000 IS STRUCTURED

The single most important architectural decision, carried forward from v1 and non-negotiable:

> **Topic is the channel. Audience is an affinity that cuts across every channel.**

Making audience the top-level channel is what breaks a catalog at scale. Do not do it.

### The math

```
15 CHANNELS  ×  10 THEMES per channel  =  150 THEMES
150 THEMES   ×  100 CAMPAIGNS per theme =  15,000 CAMPAIGNS
```

Every campaign is available in **four formats** and **four editions**. Formats and editions are
*attributes* of a campaign, never multipliers of the campaign count.

### The 15 channels

1. **Purpose & Calling**
2. **Identity & Significance**
3. **Community & Belonging**
4. **Prayer & Spiritual Disciplines**
5. **Money & Stewardship**
6. **Marriage & Relationships**
7. **Parenting & Family**
8. **Emotional Health** — anxiety, peace, grief, burnout
9. **Freedom & Recovery**
10. **Generosity & Legacy**
11. **Mission & Neighbor**
12. **Leadership & Serving**
13. **Seasons & the Church Calendar** — Advent, Lent, Easter, New Year, back-to-school, Thanksgiving
14. **Doubt, Faith & Deconstruction** ← validated white space; no major publisher owns it
15. **Digital Discernment: Faith in the Age of AI** ← validated white space; no major publisher owns it

Channels 14 and 15 are strategically the most valuable real estate on the site. Local churches
are currently building their own materials on these topics, which is the clearest possible signal
of unmet demand. Feature them, do not bury them.

### The four formats

| Format | Length | Positioning |
|---|---|---|
| **40-Day Journey** | 6 weeks, 6 sessions | Deepest formation. The Purpose Driven model. Premium tier. |
| **30-Day Spiritual Journey** | 4 weeks, 4 sessions | Volume driver. Matches the most common preaching calendar. |
| **21-Day Challenge** | 3 weeks, 3 sessions | Highest intensity. Best for prayer, fasting, generosity, seasonal. |
| **7-Day Experience** | 1 week, 6 days + 2 Sundays | Lowest barrier. The breakthrough format with least competition. |

Campaign identity = format name + topic. *The 21-Day Prayer Challenge.* *The 7-Day Generosity
Experience.* The name does the explaining; never require a glossary.

### The four editions

**Adult** · **Youth/Student** · **Children & Family** · **Leader**

Every campaign page must make visible that the church receives all four — this is the single
strongest differentiator against every competing curriculum product.

### The affinity axis (filters, not folders)

Men · Women · Young Adults · Students · Children & Families · Couples · Seniors &
Grandparents · New Believers · Leaders · Whole Church

### Collections (curatorial layer)

Flagship · Seasonal · New This Month · The Pastor's Shelf · Custom-Built for Your Church

**Flagship campaigns are hand-curated and lead the catalog.** Engine-generated campaigns
provide depth and long-tail coverage. The homepage must never make these feel equivalent —
flagship gets the gold treatment, hero placement, and full asset previews.

---

## 3. THE DATA SPINE — BUILD THIS FIRST

Before a single pixel: generate the complete dataset and prove it.

Produce `data/campaigns.json` sharded by channel (`data/ch01.json` … `data/ch15.json`) plus a
lightweight `data/index.json` containing only the fields needed for browse and search:

```json
{
  "id": "ch05-th03-c047",
  "slug": "money-made-simple",
  "title": "Money Made Simple",
  "subtitle": "Six Weeks to Peace With What You Have",
  "channel": "Money & Stewardship",
  "theme": "Contentment",
  "formats": ["40", "30", "21", "7"],
  "affinities": ["Whole Church", "Couples", "Men"],
  "collections": ["Flagship"],
  "scripture_backbone": "1 Timothy 6:6-10",
  "metaphor": "the open hand",
  "cover_fingerprint": "a7f3c1",
  "price_tier": 2,
  "summary": "One-sentence pastoral promise, second person, no jargon."
}
```

### Uniqueness gates — the build fails if any of these fail

Run these as `assert` statements with `sys.exit(1)` on failure, and print the results:

1. **15,000 exactly.** No more, no fewer.
2. **Zero duplicate titles** across the entire catalog, case- and punctuation-insensitive.
3. **Zero duplicate title+subtitle pairs.**
4. **No repeated scripture backbone within a single channel** where avoidable; report any
   collisions with a justification.
5. **No repeated core metaphor within a single theme.** Every campaign in a theme must have a
   distinct scriptural backbone and a distinct governing image.
6. **Zero title collisions** with existing branded programs — Ramsey, Ron Blue, Crown, Alpha,
   Celebrate Recovery, Financial Peace, Experiencing God, Emotionally Healthy. Check
   programmatically against a blocklist and fail on match.
7. **15,000 unique cover fingerprints.**

### Titling standards

- Short, second-person, promise-shaped. This is the top-performing pattern in the market.
- Do **not** name a Bible book or a doctrine in the title.
- Avoid "Financial ___" constructions entirely. Plain naming reads stronger: *Money Wise*,
  *Money Made Simple*, *Enough*.
- Subtitle carries the format promise and the timeframe.

---

## 4. DESIGN SYSTEM — EXACT TOKENS

The aesthetic is **RightNow Media's light editorial style**, elevated with a 25-year-heritage
publishing sensibility. **Not dark. Not Netflix. Not a streaming wall.** This was a specific
correction on the previous build and it stands.

### Color

```css
--navy-900: #101E38;   /* deepest ground, footer, hero overlays */
--navy-800: #172542;   /* primary brand navy */
--navy-700: #22335A;   /* raised navy surfaces */
--gold:     #C9A13B;   /* FLAGSHIP ONLY — starred, featured, premium */
--gold-deep:#B98D3E;
--gold-soft:#E4C878;
--ember:    #E2703A;   /* warm accent: curved tabs, active states, CTAs */
--cream:    #FBF8F1;   /* page ground */
--paper:    #FFFFFF;   /* cards */
--ink:      #1C1C1A;   /* body text */
--muted:    #6B7280;
--line:     #E7E0D2;
```

**Gold carries meaning.** Gold means flagship — starred themes, featured formats, premium
tier, breakthrough moments. Navy means authority and depth. If gold appears on something
that is not flagship, the system is broken. Every color choice must do argumentative work.

### Typography

| Role | Family | Notes |
|---|---|---|
| Interface, headlines, nav | **Hanken Grotesk** | 400/500/600/700 |
| Editorial body, campaign copy, Scripture | **Spectral** | 400/500/600 + italic |
| Eyebrows, labels, meta, tags | **Archivo** | 600, letter-spacing 0.06em, uppercase |

**Never use Figtree.** It reads too bubbly for an adult pastoral audience. This was a prior
correction and it is permanent.

**Font loading (critical build constraint):** the Google Fonts CDN is unreachable in the build
environment. Fetch WOFF2 files from `raw.githubusercontent.com/google/fonts` with
URL-encoded bracket characters, then **embed as base64** in the CSS so the site is fully
portable and works when opened from a local folder with zero network access.

### Component vocabulary

- **Pill buttons**, generous radius, never sharp rectangles.
- **Curved tab headers** in ember for content rows — the signature RightNow move.
- **Soft gradient washes** as section grounds, never flat gray blocks. Never the generic
  AI purple-blue gradient.
- **Cards** with a 3:4 cover, title, subtitle, format chips, and affinity tags.
- **Format chips**: `7 · 21 · 30 · 40` as a compact inline lockup on every card.
- Gold star glyph for flagship items, visible at card scale.
- Generous whitespace. 8px baseline grid. Max content width 1280px.
- Motion: fast, small, purposeful. Nothing bounces.

---

## 5. SITE MAP — EVERY PAGE, ALL LINKED, ALL REAL

```
index.html              Homepage
browse.html             Full catalog, 15,000 rows, faceted
channel.html            Channel landing (×15, or parameterized)
theme.html              Theme landing (×150, or parameterized)
campaign.html           Campaign detail + preview + sample day
finder.html             Campaign Finder quiz with real scoring
builder.html            Campaign Builder — custom campaign for your church
formats.html            The four formats explained
included.html           What Your Church Receives (all four editions)
pricing.html            Four tiers + à la carte
how-it-works.html       Launch timeline, 6-step roadmap
for-pastors.html        Senior pastor track
for-churches.html       Staff / small group director track
seasonal.html           Church calendar planner
about.html              25-year heritage
case-studies.html       Church stories
faq.html                Objection handling
cart.html               Cart
checkout.html           Checkout — card / PayPal / invoice
confirmation.html       Confirmation + immediate curriculum downloads
account.html            Account, library, downloads
signin.html / signup.html
contact.html
```

**Every internal link must resolve.** Verify programmatically with a link scanner across all
files before delivery and report `0 broken links`. Use relative paths throughout so the site
works from a single hosting folder.

---

## 6. PAGE SPECS — THE SIX THAT MATTER MOST

### 6.1 Homepage (`index.html`)

Sequence, top to bottom:

1. **Hero.** Cream ground, soft wash. Headline in Hanken Grotesk, promise-shaped, second
   person. Subhead names the scale — 15,000 campaigns, 15 channels, four formats, four
   editions. Primary CTA `Find Your Campaign`, secondary `Build Your Own`. Floating campaign
   cards at a slight angle to the right, real covers, real titles.
2. **Credibility strip.** 25 years · 500+ churches · 15,000 campaigns · 4 editions. Understated,
   navy on cream, no badges or logos-you-do-not-have.
3. **The 15 channel tiles.** Gradient covers, campaign counts, hover lift. Channels 14 and 15
   get a `NEW` marker in ember.
4. **Flagship row.** Curved ember tab reading `Flagship Campaigns`. Gold-starred cards. These
   are hand-curated and must feel it.
5. **The problem, named.** The pastor's Wednesday afternoon. One tight paragraph in Spectral,
   not bullets. Then the resolution: sermon → curriculum → community → movement.
6. **Four formats.** Side-by-side, with the honest positioning of each. Make the 7-Day
   Experience feel like a real yes for a church that has said no before.
7. **What your church receives.** Six-piece grid: Adult devotional, Youth edition, Children &
   Family edition, Small group guide, Sermon outlines + preaching ideas, Leader training &
   recruitment kit.
8. **Seasonal row.** Auto-surfaces the campaigns matched to the next 90 days of the church
   calendar.
9. **Pricing preview.** Four tiers, `Most Popular` on Tier Two.
10. **Heritage.** The Purpose Driven lineage, told with restraint.
11. **FAQ accordion.** Six objections, answered directly.
12. **Closing CTA.** Navy ground, gold text. *"Do not let Sunday end on Sunday."*

### 6.2 Browse (`browse.html`) — the hardest page

This is where a 15,000-row catalog either works or collapses.

- **Facets:** Channel, Theme, Format, Edition, Affinity, Collection, Season, Price tier.
- **Live filtering** with **precomputed facet counts** — every facet shows its result count
  before the user clicks, and counts update as filters combine.
- **Virtualized rendering.** Render only the visible window plus a small buffer. Never mount
  15,000 DOM nodes. Target: filter-to-paint under 100ms on a mid-range laptop.
- **Client-side inverted index** for instant search across title, subtitle, theme, scripture,
  and summary. Build the index at load from `index.json`, not by scanning full records.
- **Sort:** Relevance · Most Popular · Newest · A–Z · Format length.
- **Sticky filter rail** on desktop, bottom-sheet on mobile.
- **URL state** — every filter combination is a shareable link.
- Empty state must be useful: suggest the nearest three matches, never a dead end.

### 6.3 Campaign detail (`campaign.html`)

Above the fold: cover, title, subtitle, channel/theme breadcrumb, format selector, price for
the selected format and tier, `Add to cart`, `Preview a sample day`.

Below: the complete daily arc (every day's one-word step and Scripture reference), the six
sermon builds (title, subtitle, three texts, five preaching ideas with supporting references,
full message outline), the small group session list, the youth and children's edition contents,
the leader training kit contents, the Celebration Sunday plan, and a spiritual partner
framework. Everything real. Nothing labeled "coming soon."

**Sample day preview** renders a real, print-ready PDF page. Wire an export that produces an
editable Word document and opens Canva in a new tab.

### 6.4 Campaign Finder (`finder.html`)

Six to eight questions with **real scoring logic**, not a decorative quiz. Inputs: church size,
preaching calendar window, primary ministry goal, current season, congregational felt need,
readiness for family editions, budget. Output: three ranked campaigns with an explanation of
*why* each was matched, plus one deliberately unexpected recommendation.

### 6.5 Campaign Builder (`builder.html`)

The custom path. Three named intelligences, presented as a sequence the pastor moves through:

- **Pastor Intelligence** — his voice, his sermon archive, his convictions.
- **Lifetogether Intelligence** — 25 years of campaign architecture and formation design.
- **Church Intelligence** — his congregation's size, season, and readiness.

Output is a scoped custom campaign brief with format, arc, session map, and a quoted price.

### 6.6 Commerce (`cart` → `checkout` → `confirmation`)

Real cart state. `Add to cart` buttons on every card and in the finder — never "Add to plan."
Checkout supports card, PayPal, and church invoice (POs are how most churches actually buy).
Mark the **Stripe integration seam** clearly with a comment block so it can be wired without
refactoring. Confirmation page delivers immediate curriculum downloads.

---

## 7. THE COVER SYSTEM — 15,000 UNIQUE COVERS

Generate covers **deterministically in SVG**, not as image files. Fingerprint each campaign as
`hash(channel, theme, index)` and use it to select from a combinatorial matrix:

```
layout archetype (12)  ×  palette (18)  ×  ornament system (14)
×  type lockup (9)  ×  texture/wash (7)   →  190,512 possible designs
```

Every cover must read as the same family — navy/gold/cream/ember discipline, brand type,
consistent margins — while being visibly distinct at thumbnail scale. **Assert 15,000 unique
fingerprints and fail the build if any collide.** Generate covers lazily as cards enter the
viewport; never generate 15,000 at load.

Flagship campaigns get hand-tuned covers that override the generative system.

---

## 8. PERFORMANCE REQUIREMENTS AT SCALE

- Homepage first paint under 1.5s from a local folder.
- `browse.html` interactive under 2s with all 15,000 records indexed.
- Filter-to-repaint under 100ms.
- Sharded data loading — never ship a single monolithic JSON.
- No external CDN dependencies. Fonts base64-embedded. The entire site must work offline
  from a folder.
- Fully responsive: 375px through 1920px. Test at 375, 768, 1280, 1920.
- Keyboard navigable. Visible focus rings. WCAG AA contrast throughout.

---

## 9. MULTILINGUAL

Ship **English** complete. Build **Spanish** and **Portuguese** editions with the same structure
and a shared string table (`i18n/en.json`, `es.json`, `pt.json`) so translations swap without
touching markup. Titles and subtitles must be translated as *ministry copy*, not
machine-literal — a campaign title has to preach in the target language.

---

## 10. CONTENT AND THEOLOGICAL STANDARDS

- **Scripture: NIV throughout.** Use **KJV for embedded verse text** until the Biblica license
  is signed — the gratis limit is approximately 500 verses and this platform is far past it at
  scale. Flag this in a build note.
- Every Scripture reference must be **real and correctly abbreviated.** Verify programmatically
  against a canonical book/chapter/verse table. Fail the build on any invalid reference.
- Never invent facts, quotes, or biography about named individuals.
- **Sensitive topics** — grief, anxiety, financial fear, shame, deconstruction — use gentle
  pastoral framing: conviction-not-condemnation tone, comforting texts, permission-to-go-slow
  pacing, and a closing note pointing toward pastoral or professional support.
- Voice: Rick Warren / Lifetogether pastoral register. Warm, direct, unpretentious, second
  person. Short sentences. No jargon. No hype.
- Marketing copy is **prose, not bullets.** Bullets are for specs and contents lists only.

---

## 11. BUILD STACK

Python · HTML/CSS/vanilla JS (no framework dependency the client cannot host) ·
WeasyPrint for print PDFs · Playwright/Chromium for large flowing documents and QA ·
fonttools for variable font instancing · `pypdf` · `zipfile`.

### Known environment traps — handle these preemptively

1. **WeasyPrint SVG bug.** SVG sized `width="100%"` inside a CSS inch-height div causes
   sibling elements to bleed. Use explicit inch dimensions via a `fixed(svg_str, width_in,
   height_in)` helper.
2. **Playwright truncation on large documents.** `networkidle` fires before Chromium finishes
   layout. Add `wait_for_timeout(4000)` and `emulate_media("print")` before `page.pdf()`.
3. **Section renumbering.** Use Python string replacement in descending order. Shell/sed
   arithmetic fails silently and wipes numeric content.
4. **Relative links between separately hosted HTML files 404 when opened locally.** For any
   single-file deliverable, use one combined file with in-page anchors.
5. **Google Fonts CDN unreachable.** See Section 4.

---

## 12. VALIDATION GATES — RUN AND REPORT ALL OF THEM

Print a validation table before delivery. Any failure exits with `sys.exit(1)`.

```
[ ] Campaign count == 15,000
[ ] Zero duplicate titles
[ ] Zero duplicate title+subtitle pairs
[ ] Zero branded-program title collisions
[ ] 15,000 unique cover fingerprints
[ ] Zero invalid Scripture references
[ ] Zero broken internal links (Playwright crawl of every page)
[ ] Zero console errors on every page
[ ] Every page renders at 375 / 768 / 1280 / 1920
[ ] browse.html interactive < 2s with full dataset
[ ] All fonts embedded, zero external network requests
[ ] Cart → checkout → confirmation completes end to end
[ ] Every CTA on every page leads somewhere real
```

---

## 13. ANTI-PATTERNS — AUTOMATIC FAILURE

- Lorem ipsum, `TODO`, `[placeholder]`, or "coming soon" anywhere in shipped output
- Dead links or CTAs that go nowhere
- A dark Netflix-style streaming aesthetic
- Figtree, or any bubbly geometric sans
- Generic purple/blue AI gradients
- Gold used on anything that is not flagship
- Rendering all 15,000 rows into the DOM
- External CDN font or script dependencies
- Stock photography of smiling models
- Bullet-point marketing copy where prose belongs
- Asking clarifying questions instead of building

---

## 14. TONE OF THE DELIVERY WRITE-UP

When the build is complete, explain what was built and **why each decision serves the
communication goal** — in prose, not bullets. Name the strategic reasoning behind the
information architecture, the color hierarchy, the sequence of the homepage, and the two
white-space channels. Close with the single next build step, not a menu of options.

---

## 15. DELIVERABLE

A single zip: `40daycampaigns_platform_15k.zip`

```
/index.html and all pages
/assets/css, /assets/js, /assets/fonts (base64-embedded)
/data/index.json, /data/ch01–ch15.json
/i18n/en.json, es.json, pt.json
/es/, /pt/  (Spanish and Portuguese editions)
/build/     (the generation and validation scripts)
/VALIDATION.txt  (the passing gate report)
/README.md  (hosting instructions, Stripe seam location, NIV license note)
```

Verify archive integrity with `zipfile.testzip()` before delivery. Place the final file in
`/mnt/user-data/outputs/`.

---

## 16. THE ONE SENTENCE TO BUILD AGAINST

> *A senior pastor with a message God has given him should be able to land on this site, find
> the campaign that carries it, see exactly what his church receives, and say yes — in under
> four minutes, without talking to anyone.*

Build that. Go.

---

## 17. OPTIONAL: PHASED BUILD SEQUENCE

If building in stages rather than one pass, use this order. Each phase ships something real.

**Phase 0 — Data spine.** Generate all 15,000 campaigns. Pass every uniqueness gate. Ship
`VALIDATION.txt`. Nothing visual yet.

**Phase 1 — Design system + homepage.** Tokens, fonts embedded, component library, complete
homepage with real data pulled from Phase 0.

**Phase 2 — Browse at scale.** Virtualized catalog, faceted filtering, inverted-index search,
precomputed counts. This is the phase that proves the platform.

**Phase 3 — Detail, channel, theme pages.** Campaign detail with full arc, sermon builds, and
sample-day PDF. Channel and theme landings.

**Phase 4 — Finder and Builder.** Real scoring logic. Three intelligences.

**Phase 5 — Commerce.** Cart, checkout, confirmation, account, Stripe seam.

**Phase 6 — i18n + QA.** Spanish and Portuguese editions, full Playwright crawl, every
validation gate green, zip delivered.
