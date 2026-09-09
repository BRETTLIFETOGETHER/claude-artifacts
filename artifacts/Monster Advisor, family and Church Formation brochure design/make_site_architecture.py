import sys
sys.path.insert(0, "/home/claude/build")

PAGES = []
def add(html): PAGES.append(html)

def folio(chapter, num):
    return f'''<div class="folio"><div class="thread">{chapter}</div><div>{num:02d}</div></div>'''

def l1(text, note=""):
    n = f' <span class="tree-note">&mdash; {note}</span>' if note else ""
    return f'<div class="tree-l1">{text}{n}</div>'

def l2(text, note=""):
    n = f' <span class="tree-note">&mdash; {note}</span>' if note else ""
    return f'<div class="tree-l2">{text}{n}</div>'

def l3(text, tag=""):
    t = f'<span class="tag">{tag}</span>' if tag else ""
    return f'<div class="tree-l3">{text}{t}</div>'

# =================================================================
# PAGE 1 — COVER
# =================================================================
add(f'''
<div class="page navy">
  <div class="frame" style="display:flex; flex-direction:column; justify-content:flex-end;">
    <div style="font-family:'Archivo'; font-weight:600; font-size:9pt; letter-spacing:0.22em; color:#D9B876; margin-bottom:2.4in;">INTERNAL PLANNING DOCUMENT &middot; DRAFT FOR DISCUSSION</div>
    <h1 class="display" style="font-size:28pt; color:#FBF8F1;">Master Website Architecture</h1>
    <div style="height:0.14in;"></div>
    <div style="font-family:'Playfair'; font-style:italic; font-weight:600; font-size:15pt; color:#D9B876;">Version 1.0 &mdash; Pastor Track</div>
    <div style="height:0.24in;"></div>
    <p class="lede" style="font-size:10.3pt; color:rgba(251,248,241,0.8); max-width:5.6in;">
      A first working sitemap for LifeTogether&rsquo;s pastor-facing web presence &mdash; the
      Church Formation System, the 40 Day Campaigns&trade; platform, and the Biblical
      Purpose Library &mdash; integrating every brochure built so far into one architecture.
    </div>
    <div style="height:0.2in;"></div>
    <p style="font-family:'Inter'; font-size:9pt; color:rgba(251,248,241,0.55); font-style:italic;">
      A companion Version 2.0 will cover the Christian Advisor Network and the broader
      business/subscriber platform. This draft is meant to be marked up, not finalized.
    </p>
  </div>
</div>
''')

# =================================================================
# PAGE 2 — APPROACH & SCOPE
# =================================================================
add(f'''
<div class="page">
  <div class="frame">
    <div class="eyebrow">APPROACH &amp; SCOPE</div>
    <div style="height:0.2in;"></div>
    <h1 class="display" style="font-size:21pt; color:var(--navy);">Two tracks, built in order.</h1>
    <div style="height:0.16in;"></div>
    <p class="lede">
      Everything built so far &mdash; the Church Formation System, the Flagship Guidebook,
      the Campaign Builder Intensive, the Biblical Purpose Library &mdash; speaks to one
      audience: <b>senior pastors and ministry leaders.</b> That is Track One, and it is what
      this v1.0 architecture covers.
    </p>
    <p class="lede">
      The Christian Advisor Network speaks to a second, distinct audience &mdash; <b>Christian
      financial advisors</b> &mdash; with its own funnel, its own language, and likely its own
      subdomain or site section. Rather than force both into one v1.0 and lose clarity on
      either, this draft covers Track One completely and flags Track Two as a defined
      Version 2.0 to follow.
    </p>
    <div style="height:0.2in;"></div>
    <div class="takeaway">
      <span class="label">In this v1.0</span>
      Public marketing site for pastors &middot; the 40 Day Campaigns&trade; content platform &middot; the Church Formation System consulting funnel &middot; pricing &middot; a first pass at a member/subscriber portal.
    </div>
    <div style="height:0.16in;"></div>
    <div class="takeaway">
      <span class="label">Deferred to Version 2.0</span>
      Christian Advisor Network site or subdomain &middot; advisor member portal &middot; church-partnership tools for advisors &middot; any shared account system between the two audiences.
    </div>
    <div style="height:0.2in;"></div>
    <p style="font-family:'Inter'; font-size:9.4pt; color:var(--gray); font-style:italic;">
      This is a draft for discussion, not a build spec. Page 12 lists the open decisions this
      draft assumes an answer to &mdash; worth resolving before any of this goes to a developer.
    </p>
  </div>
  {folio("Approach & Scope", 2)}
</div>
''')

# =================================================================
# PAGE 3 — FULL SITEMAP (PUBLIC SITE)
# =================================================================
sitemap_public = f'''
{l1("Home")}
{l2("Hero: message &rarr; curriculum &rarr; community &rarr; movement")}
{l2("Three entry points: I'm a Pastor / Browse Campaigns / Work With Us")}

{l1("The Church Formation System&trade;", "consulting funnel")}
{l2("Why This Matters", "the problem + opportunity")}
{l2("How It Works")}
{l3("The Framework &amp; Five Environments")}
{l3("The Five-Stage Process (Discern &rarr; Mobilize)")}
{l3("The Campaign Lifecycle &amp; Content Library")}
{l3("AI as Ministry Multiplier")}
{l2("Crawl, Walk, Run", "the growth model")}
{l2("Case Studies")}
{l2("FAQ")}

{l1("40 Day Campaigns&trade;", "the content platform &mdash; 10,000 campaigns")}
{l2("Browse by Category", "mega-menu, ~25 categories")}
{l2("Browse by Format")}
{l3("7-Day Experience")}
{l3("21-Day Challenge")}
{l3("30-Day Journey")}
{l3("40-Day Campaign")}
{l2("Campaign Finder", "quiz / guided picker")}
{l2("Sample a Campaign", "Day 1 preview, free")}
{l2("The Biblical Purpose Library&trade;", "flagship collection")}
{l3("A Life That Matters (flagship)")}
{l3("Made for More / Your Life on Purpose")}
{l3("Designed to Flourish / The Whole-Life Disciple")}
{l3("Customize for Your Ministry (audience selector)")}
'''
add(f'''
<div class="page">
  <div class="frame">
    <div class="eyebrow">FULL SITEMAP &mdash; PART 1 OF 2</div>
    <div style="height:0.14in;"></div>
    <h1 class="display" style="font-size:18pt; color:var(--navy);">Public marketing site</h1>
    <div style="height:0.1in;"></div>
    <div class="tree">{sitemap_public}</div>
  </div>
  {folio("Full Sitemap", 3)}
</div>
''')

# =================================================================
# PAGE 4 — FULL SITEMAP (CONTINUED)
# =================================================================
sitemap_public_2 = f'''
{l1("Ways to Work With Us")}
{l2("Campaign Builder Intensive", "6-week, one-time")}
{l2("90-Day Accelerator")}
{l2("Annual Formation Partnership", "12-month, ongoing")}
{l2("Pricing")}
{l3("Campaign pricing (Tiers 1&ndash;4)")}
{l3("Platform subscription pricing (monthly/annual)")}

{l1("Resources")}
{l2("Download the Executive Overview")}
{l2("Download the Flagship Guidebook")}
{l2("Blog / Insights")}
{l2("Webinars", "e.g. First 100 Pastors")}

{l1("About")}
{l2("Our Story", "Brett Eastman, Purpose Driven heritage, 25 years")}
{l2("Our Team")}
{l2("Church Seminary&trade;", "training arm")}

{l1("Contact")}
{l2("Schedule a Strategy Conversation")}
{l2("Support")}
'''
add(f'''
<div class="page">
  <div class="frame">
    <div class="eyebrow">FULL SITEMAP &mdash; PART 2 OF 2</div>
    <div style="height:0.14in;"></div>
    <h1 class="display" style="font-size:18pt; color:var(--navy);">Public marketing site, continued</h1>
    <div style="height:0.1in;"></div>
    <div class="tree">{sitemap_public_2}</div>
  </div>
  {folio("Full Sitemap", 4)}
</div>
''')

# =================================================================
# PAGE 5 — MEMBER / SUBSCRIBER PORTAL
# =================================================================
sitemap_portal = f'''
{l1("My Library")}
{l2("Active campaigns", "licensed / in progress")}
{l2("Full catalog access", "by subscription tier")}
{l2("Downloads", "PDF, print files, video, slides")}

{l1("Campaign Workspace")}
{l2("Branding kit", "logo, colors, church name applied")}
{l2("Editable editions", "InDesign / Canva source files")}
{l2("Launch calendar &amp; promotion assets")}
{l2("Leader training videos")}

{l1("Account")}
{l2("Subscription &amp; billing")}
{l2("Team members / staff seats")}
{l2("Church profile")}

{l1("Support")}
{l2("Help center")}
{l2("Book a coaching call", "Partnership tier")}
'''
add(f'''
<div class="page">
  <div class="frame">
    <div class="eyebrow">FULL SITEMAP &mdash; MEMBER / SUBSCRIBER PORTAL</div>
    <div style="height:0.14in;"></div>
    <h1 class="display" style="font-size:19pt; color:var(--navy);">Where the product actually lives</h1>
    <div style="height:0.1in;"></div>
    <p class="lede" style="font-size:9.6pt;">
      The marketing site sells the vision. The portal is where a subscribing church actually
      uses what they bought &mdash; this is the part a platform like Kajabi or Mighty Networks
      would host natively, distinct from the marketing pages above.
    </p>
    <div style="height:0.14in;"></div>
    <div class="tree">{sitemap_portal}</div>
  </div>
  {folio("Full Sitemap", 5)}
</div>
''')

# =================================================================
# PAGE 6 — DEEP DIVE: HOMEPAGE & CHURCH FORMATION SYSTEM HUB
# =================================================================
add(f'''
<div class="page">
  <div class="frame">
    <div class="eyebrow">SECTION DEEP-DIVE</div>
    <div style="height:0.16in;"></div>
    <h1 class="display" style="font-size:19pt; color:var(--navy);">Home &amp; the Church Formation System hub</h1>
    <div style="height:0.14in;"></div>
    <p class="lede">
      The homepage&rsquo;s job is triage: get a pastor to the right door in one look. Three
      doors, matching the three ways people already arrive &mdash; searching for a solution to
      the sermon-doesn&rsquo;t-stick problem, browsing for campaign content, or ready to talk
      about working together.
    </p>
    <div style="height:0.16in;"></div>
    <div class="takeaway">
      <span class="label">Content source</span>
      The homepage and Church Formation System hub draw directly from the Flagship Guidebook&rsquo;s narrative arc: the problem, the opportunity, the framework, the five-stage process &mdash; condensed to web-page length, with the guidebook offered as a full download.
    </div>
    <div style="height:0.16in;"></div>
    <div class="takeaway">
      <span class="label">Design note</span>
      Every sub-page here (Framework, Five Environments, Five-Stage Process, Campaign Lifecycle, Content Library, AI Multiplier) already exists as a fully written, fully designed page in the Flagship brochure. This is a content-porting job, not new writing.
    </div>
    <div style="height:0.16in;"></div>
    <div class="takeaway">
      <span class="label">Primary conversions</span>
      Download the Executive Overview (email capture) &middot; Schedule a Strategy Conversation &middot; Browse 40 Day Campaigns
    </div>
  </div>
  {folio("Home & Church Formation System Hub", 6)}
</div>
''')

# =================================================================
# PAGE 7 — DEEP DIVE: 40 DAY CAMPAIGNS PLATFORM
# =================================================================
add(f'''
<div class="page navy">
  <div class="frame">
    <div class="eyebrow">SECTION DEEP-DIVE</div>
    <div style="height:0.16in;"></div>
    <h1 class="display" style="font-size:19pt; color:#FBF8F1;">40 Day Campaigns&trade; &mdash; the platform, not the brochure</h1>
    <div style="height:0.14in;"></div>
    <p class="lede">
      This is the part of the site that behaves like RightNow Media or MasterClass, not a
      brochure site: a searchable, filterable catalog of thousands of campaigns across
      formats and categories, with a mega-menu doing the heavy lifting.
    </p>
    <div style="height:0.16in;"></div>
    <div class="takeaway">
      <span class="label">Two ways to browse</span>
      By category (the ~25 mega-menu categories already mapped) and by format (7-Day Experience, 21-Day Challenge, 30-Day Journey, 40-Day Campaign) &mdash; a pastor with a calendar constraint should find a format that fits before he ever picks a topic.
    </div>
    <div style="height:0.16in;"></div>
    <div class="takeaway">
      <span class="label">The Campaign Finder</span>
      A short guided quiz (season of the church year, calendar length available, theme) that recommends 2&ndash;3 campaigns &mdash; the entry point for a pastor who doesn&rsquo;t yet know what he&rsquo;s looking for.
    </div>
    <div style="height:0.16in;"></div>
    <div class="takeaway">
      <span class="label">Open dependency</span>
      This section needs the mega-menu wiring and the de-duplication pass across the campaign titles directory to be finished before it can go live as designed &mdash; both already identified as in-progress work.
    </div>
  </div>
  {folio("40 Day Campaigns Platform", 7)}
</div>
''')

# =================================================================
# PAGE 8 — DEEP DIVE: WAYS TO WORK WITH US + PRICING
# =================================================================
add(f'''
<div class="page">
  <div class="frame">
    <div class="eyebrow">SECTION DEEP-DIVE</div>
    <div style="height:0.16in;"></div>
    <h1 class="display" style="font-size:18pt; color:var(--navy);">Ways to Work With Us &amp; Pricing</h1>
    <div style="height:0.14in;"></div>
    <p class="lede">
      Two different pricing models live side by side here, and the page needs to make the
      distinction obvious rather than confusing: <b>campaign pricing</b> (one-time, per
      campaign, Tiers 1&ndash;4) and <b>platform subscription pricing</b> (ongoing, monthly or
      annual, unlocks the library).
    </p>
    <div style="height:0.16in;"></div>
    <div class="takeaway">
      <span class="label">Content source</span>
      The Campaign Builder Intensive brochure&rsquo;s investment overview table, and the existing four-tier campaign pricing sheet (Tier 1 entry, Tier 2 anchor, Tier 3 premium, Tier 4 production engagement), both already fully designed &mdash; this page combines them into one coherent pricing story instead of two separate documents.
    </div>
    <div style="height:0.16in;"></div>
    <div class="takeaway">
      <span class="label">Recommended structure</span>
      Lead with campaign pricing (lower commitment, easier yes) &rarr; introduce platform subscription as the natural next step for a church that licenses more than one or two campaigns &rarr; present the three consulting offerings (Intensive / Accelerator / Partnership) as the premium, high-touch path for churches building an original campaign.
    </div>
  </div>
  {folio("Ways to Work With Us & Pricing", 8)}
</div>
''')

# =================================================================
# PAGE 9 — CONTENT MAPPING TABLE
# =================================================================
mapping_rows = [
    ("Executive Overview", "Homepage hero + downloadable PDF gate"),
    ("The Church Formation System (19-page)", "Church Formation System hub, condensed across sub-pages"),
    ("Flagship Guidebook (23-page)", "Full source content for the CFS hub + downloadable PDF"),
    ("Campaign Builder Intensive (15-page)", "Ways to Work With Us &rarr; Campaign Builder Intensive page"),
    ("Biblical Purpose Library (13-page)", "40 Day Campaigns &rarr; Biblical Purpose Library section"),
    ("MASTER Unified Guide (28-page)", "Internal reference; keeps messaging consistent across the site"),
    ("Campaign pricing sheet (Tiers 1&ndash;4)", "Pricing page"),
    ("Platform research (Kajabi / Mighty Networks / Subsplash)", "Informs the Member Portal technology decision &mdash; see page 11"),
]
map_html = "".join([f'''
    <div class="exp-row">
      <div class="exp-name">{a}</div>
      <div class="exp-desc">&rarr; {b}</div>
    </div>''' for a, b in mapping_rows])
add(f'''
<div class="page">
  <div class="frame">
    <div class="eyebrow">CONTENT MAPPING</div>
    <div style="height:0.16in;"></div>
    <h1 class="display" style="font-size:19pt; color:var(--navy);">What already exists, and where it goes</h1>
    <div style="height:0.14in;"></div>
    <p class="lede" style="font-size:9.6pt;">Nothing in this architecture requires new writing to launch a first version &mdash; every page above has a direct source document already built.</p>
    <div style="height:0.1in;"></div>
    {map_html}
  </div>
  {folio("Content Mapping", 9)}
</div>
''')

# =================================================================
# PAGE 10 — NAVIGATION & MEGA-MENU CONCEPT
# =================================================================
nav_items = ["The Church Formation System", "40 Day Campaigns", "Ways to Work With Us", "Resources", "About"]
add(f'''
<div class="page">
  <div class="frame">
    <div class="eyebrow">NAVIGATION &amp; MEGA-MENU CONCEPT</div>
    <div style="height:0.16in;"></div>
    <h1 class="display" style="font-size:19pt; color:var(--navy);">Five items in the primary nav. Everything else lives inside them.</h1>
    <div style="height:0.14in;"></div>
    <div class="chip-row-static">{"".join([f'<div class="track-chip">{n}</div>' for n in nav_items])}</div>
    <div style="height:0.2in;"></div>
    <p class="lede" style="font-size:9.6pt;">
      &ldquo;40 Day Campaigns&rdquo; is the one item that needs a true mega-menu &mdash; a
      dropdown showing categories down one side and formats down the other, since that&rsquo;s
      the only section with enough depth (10,000 campaigns) to need it. Everything else can
      be a simple dropdown with 3&ndash;5 links.
    </p>
    <div style="height:0.16in;"></div>
    <div class="takeaway">
      <span class="label">Mobile consideration</span>
      The mega-menu collapses to an accordion on mobile &mdash; category list first, format filter as a secondary toggle, matching the pattern already used in the iPhone library editions built this month.
    </div>
    <div style="height:0.16in;"></div>
    <div class="takeaway">
      <span class="label">A secondary utility nav</span>
      Log In / My Library (portal access) and Schedule a Conversation (CTA) sit outside the primary nav, top-right, on every page &mdash; consistent regardless of which of the five sections a visitor is in.
    </div>
  </div>
  {folio("Navigation & Mega-Menu Concept", 10)}
</div>
''')

# =================================================================
# PAGE 11 — PLATFORM & TECHNOLOGY PATH
# =================================================================
add(f'''
<div class="page navy">
  <div class="frame">
    <div class="eyebrow">PLATFORM &amp; TECHNOLOGY PATH</div>
    <div style="height:0.16in;"></div>
    <h1 class="display" style="font-size:19pt; color:#FBF8F1;">This is a subscription platform first, a website second.</h1>
    <div style="height:0.14in;"></div>
    <p class="lede">
      The earlier platform research already reached a clear recommendation: this behaves
      like RightNow Media or MasterClass &mdash; a B2B content subscription business &mdash; not
      a typical church app. That distinction should drive the build, not just the marketing.
    </p>
    <div style="height:0.18in;"></div>
    <div class="takeaway">
      <span class="label">Recommended MVP path</span>
      Kajabi for the marketing site + member portal + subscription billing in one system &mdash; live in weeks, no developer required, proven at the Growth tier (roughly $199/mo, 50 products, unlimited landing pages).
    </div>
    <div style="height:0.16in;"></div>
    <div class="takeaway">
      <span class="label">Community-forward alternative</span>
      Mighty Networks Pro, if pastor community/cohort features (forums, leader discussion spaces) matter from day one &mdash; a true white-label branded app, closer to the RightNow Media feel, at a higher monthly cost.
    </div>
    <div style="height:0.16in;"></div>
    <div class="takeaway">
      <span class="label">Sequencing</span>
      Launch the first 20&ndash;30 subscribing churches on the MVP platform to prove the model, then evaluate a proprietary build once revenue and investor capital support it &mdash; not before.
    </div>
  </div>
  {folio("Platform & Technology Path", 11)}
</div>
''')

# =================================================================
# PAGE 12 — OPEN QUESTIONS & WHAT'S NEXT
# =================================================================
questions = [
    "Does the Christian Advisor Network live on lifetogether.com as a section, or on its own domain? (Affects nav, branding, and account systems.)",
    "Is there one login across the pastor platform and the advisor platform, or are they fully separate?",
    "How much of the 40 Day Campaigns catalog is public/browsable vs. gated behind a subscription?",
    "Does Church Seminary get its own top-level nav item, or does it live under Resources/About for now?",
    "What is the actual go-live scope for v1 &mdash; full catalog, or a curated launch set (e.g. the Biblical Purpose Library plus a handful of flagship campaigns)?",
]
q_html = "".join([f'<div class="faq"><div class="faq-q" style="font-size:11pt;">{i+1}. {q}</div></div>' for i, q in enumerate(questions)])
add(f'''
<div class="page">
  <div class="frame">
    <div class="eyebrow">OPEN QUESTIONS &amp; WHAT&rsquo;S NEXT</div>
    <div style="height:0.16in;"></div>
    <h1 class="display" style="font-size:19pt; color:var(--navy);">Worth deciding before this goes to a developer</h1>
    <div style="height:0.14in;"></div>
    {q_html}
    <div style="height:0.2in;"></div>
    <div class="takeaway">
      <span class="label">Version 2.0 preview</span>
      The Christian Advisor Network follows the same method: a public funnel (Why This Matters &rarr; The Seven Breakthrough Resources &rarr; Ways to Partner &rarr; Pricing), a member portal (the Resource Rack, the 40-Day Growth Builder, Church Partnership tools), and its own content-mapping table &mdash; built once Track One&rsquo;s open questions are resolved.
    </div>
  </div>
  {folio("Open Questions & What's Next", 12)}
</div>
''')

# =================================================================
# PAGE 13 — BACK COVER
# =================================================================
add(f'''
<div class="page navy">
  <div class="frame" style="display:flex; flex-direction:column; justify-content:space-between; align-items:center; text-align:center;">
    <div></div>
    <div>
      <div style="font-family:'Archivo'; font-weight:600; font-size:9.5pt; letter-spacing:0.24em; color:#D9B876;">LIFETOGETHER</div>
      <div style="height:0.26in;"></div>
      <h1 class="display" style="font-size:20pt; color:#FBF8F1;">Version 1.0 &mdash; mark it up.</h1>
      <div style="height:0.18in;"></div>
      <p class="lede" style="max-width:4.4in; margin:0 auto;">
        This draft is meant to be argued with. Flag what&rsquo;s wrong, what&rsquo;s missing, and
        what should move &mdash; then we build Version 2.0 for the Advisor Track next.
      </p>
      <div style="height:0.3in;"></div>
      <div style="width:30px; height:2px; background:#B98D3E; margin:0 auto;"></div>
    </div>
    <div style="font-family:'Archivo'; font-weight:500; font-size:7.4pt; letter-spacing:0.1em; color:rgba(251,248,241,0.4);">MASTER WEBSITE ARCHITECTURE &middot; VERSION 1.0 &middot; PASTOR TRACK</div>
  </div>
</div>
''')

# =================================================================
# ASSEMBLE
# =================================================================
with open("/home/claude/build/portrait_style.css") as f:
    base_css = f.read()
with open("/home/claude/build/sitemap_style.css") as f:
    tree_css = f.read()

extra_css = '''
.chip-row-static{ display:flex; flex-wrap:wrap; gap:0.12in; }
'''

html = f'''<!DOCTYPE html>
<html><head><meta charset="utf-8">
<style>{base_css}{tree_css}{extra_css}</style></head>
<body>{"".join(PAGES)}</body></html>'''

with open("/home/claude/build/site_architecture.html", "w") as f:
    f.write(html)
print("Pages:", len(PAGES))
