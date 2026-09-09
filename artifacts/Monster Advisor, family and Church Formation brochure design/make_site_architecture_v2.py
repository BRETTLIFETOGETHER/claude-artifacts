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
    <div style="font-family:'Playfair'; font-style:italic; font-weight:600; font-size:15pt; color:#D9B876;">Version 2.0 &mdash; Advisor Track</div>
    <div style="height:0.24in;"></div>
    <p class="lede" style="font-size:10.3pt; color:rgba(251,248,241,0.8); max-width:5.6in;">
      A first working sitemap for the Christian Advisor Network &mdash; the second of
      LifeTogether&rsquo;s two audiences, built with the same method as Version 1.0: every
      page traced back to a resource that already exists.
    </p>
    <div style="height:0.2in;"></div>
    <p style="font-family:'Inter'; font-size:9pt; color:rgba(251,248,241,0.55); font-style:italic;">
      Companion to Version 1.0 (Pastor Track). Read together, the two answer the
      integration questions Version 1.0 left open on its final page.
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
    <h1 class="display" style="font-size:21pt; color:var(--navy);">A different audience, the same shape.</h1>
    <div style="height:0.16in;"></div>
    <p class="lede">
      The Christian Advisor Network speaks to <b>Christian financial advisors</b>, not
      pastors &mdash; a different job title, a different daily problem, a different reason to
      show up on the site. But the underlying architecture pattern from Version 1.0 repeats
      almost exactly: a public funnel that builds a case, a content platform that delivers
      the product, and a member portal where the product actually gets used.
    </p>
    <div style="height:0.2in;"></div>
    <div class="takeaway">
      <span class="label">In this v2.0</span>
      Public marketing site for advisors &middot; the Seven Breakthrough Resources as a product hub &middot; the Complete Resource Rack as a browsable content library &middot; church-partnership tools &middot; membership pricing &middot; a first pass at the advisor member portal.
    </div>
    <div style="height:0.16in;"></div>
    <div class="takeaway">
      <span class="label">Where it touches Track One</span>
      The Pastor Sermon &amp; Seminar Library and the Church Partnership Playbook are the two places these tracks actually meet &mdash; an advisor here is trying to reach the same pastors Track One is built for. That overlap is a real integration decision, addressed on page 12.
    </div>
    <div style="height:0.2in;"></div>
    <p style="font-family:'Inter'; font-size:9.4pt; color:var(--gray); font-style:italic;">
      Same caveat as Version 1.0: this is a draft for discussion, not a build spec.
    </p>
  </div>
  {folio("Approach & Scope", 2)}
</div>
''')

# =================================================================
# PAGE 3 — FULL SITEMAP (PUBLIC SITE) PART 1
# =================================================================
sitemap_public = f'''
{l1("Home")}
{l2("Hero: Build a Practice That Reflects Your Faith and Changes Families for Generations")}
{l2("Three entry points: Grow Yourself / Serve Families / Partner with Churches")}
{l2("GROW &middot; SERVE &middot; MULTIPLY", "the three-word framework")}

{l1("More Than a Professional Association", "why this exists")}
{l2("Who the Advisor Becomes")}
{l2("What the Platform Enables")}
{l2("The Central Promise", "content to transformation")}

{l1("The Seven Breakthrough Resources&trade;", "the product hub")}
{l2("1. Faith &amp; Practice Alignment Assessment&trade;")}
{l2("2. Christian Advisor Vision &amp; Values Builder&trade;")}
{l2("3. Legacy Family Conversation System&trade;")}
{l2("4. Family Legacy Builder&trade;")}
{l2("5. 40-Day Christian Advisor Growth Builder&trade;")}
{l2("6. Advisor-Church Partnership Playbook&trade;")}
{l2("7. Pastor Sermon &amp; Seminar Library&trade;")}

{l1("The Complete Resource Rack&trade;", "the content library &mdash; 10 categories")}
{l3("Faith &amp; Spiritual Formation")}
{l3("Marriage &amp; Money")}
{l3("Parenting &amp; Next Generation")}
{l3("Family Communication &amp; Unity")}
{l3("Life Purpose &amp; Calling")}
{l3("Financial Wisdom &amp; Stewardship")}
{l3("Generosity &amp; Kingdom Impact")}
{l3("Health, Wholeness &amp; Resilience")}
{l3("Retirement &amp; Major Transitions")}
{l3("Family Legacy")}
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
{l1("Church Partnership", "the advisor's route to pastors")}
{l2("Five Levels of Church Partnership", "Resource Provider &rarr; Strategic Ministry Partner")}
{l2("How to Partner with a Local Church", "seven-step pathway")}
{l2("A Seminar for Every Season", "21 seminar titles")}
{l2("The Partnership Covenant", "what pastors fear, what advisors fear, the boundaries")}

{l1("Membership")}
{l2("Five Growth Pathways")}
{l3("Grow Yourself")}
{l3("Grow Your Practice")}
{l3("Serve Families")}
{l3("Partner with Churches")}
{l3("Build Community")}
{l2("Pricing &amp; Membership Tiers")}
{l2("The Strategic Advantage", "vs. traditional advisor networks")}

{l1("Resources")}
{l2("Download the brochure")}
{l2("Blog / Insights")}
{l2("Events &amp; Masterclasses")}

{l1("About")}
{l2("Our Story", "Ron Blue's biblical financial wisdom + LifeTogether's systems")}
{l2("Brand Architecture", "the trademark family")}

{l1("Join the Network")}
{l2("Membership application / onboarding")}
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
# PAGE 5 — MEMBER PORTAL
# =================================================================
sitemap_portal = f'''
{l1("My Resource Rack")}
{l2("Full library access", "by membership tier, all 10 categories")}
{l2("Implementation kits", "the 20-item transferable kit per resource")}
{l2("Client-facing editions", "ready to send")}

{l1("My Growth Journey")}
{l2("Faith &amp; Practice Alignment Assessment", "scorecard + 90-day plan")}
{l2("40-Day Growth Builder", "daily devotionals, videos, masterclasses")}
{l2("Coaching &amp; accountability groups")}

{l1("My Practice")}
{l2("Vision &amp; Values Builder", "advisor-branded document generator")}
{l2("Website &amp; brochure copy templates")}

{l1("My Family Legacy Tools")}
{l2("Legacy Family Conversation System", "100 Legacy Questions, card sort, timeline")}
{l2("Family Legacy Builder", "six-movement workspace")}
{l2("Client engagement tracker")}

{l1("My Church Partnerships")}
{l2("Partnership Playbook &amp; covenant templates")}
{l2("Seminar &amp; sermon library", "for sharing with pastor contacts")}
{l2("Partnership level tracker", "Level 1 &rarr; Level 5")}

{l1("Community &amp; Account")}
{l2("Advisor groups &amp; regional networks")}
{l2("Certification status")}
{l2("Membership &amp; billing")}
'''
add(f'''
<div class="page">
  <div class="frame">
    <div class="eyebrow">FULL SITEMAP &mdash; MEMBER PORTAL</div>
    <div style="height:0.14in;"></div>
    <h1 class="display" style="font-size:19pt; color:var(--navy);">Where the advisor actually works</h1>
    <div style="height:0.1in;"></div>
    <p class="lede" style="font-size:9.6pt;">
      Mirrors Version 1.0&rsquo;s split: the public site builds the case, the portal is the
      daily-use tool &mdash; five workspaces matching the Seven Breakthrough Resources plus
      community and account management.
    </p>
    <div style="height:0.14in;"></div>
    <div class="tree">{sitemap_portal}</div>
  </div>
  {folio("Full Sitemap", 5)}
</div>
''')

# =================================================================
# PAGE 6 — DEEP DIVE: HOMEPAGE & CENTRAL PROMISE
# =================================================================
add(f'''
<div class="page">
  <div class="frame">
    <div class="eyebrow">SECTION DEEP-DIVE</div>
    <div style="height:0.16in;"></div>
    <h1 class="display" style="font-size:19pt; color:var(--navy);">Home &amp; the Central Promise</h1>
    <div style="height:0.14in;"></div>
    <p class="lede">
      An advisor lands here with a specific frustration: too many good conversations he
      doesn&rsquo;t know how to start, and a practice that looks like every other practice. The
      homepage&rsquo;s job is to name that frustration fast, then prove there&rsquo;s a complete,
      ready-to-use system waiting &mdash; not another course to finish someday.
    </p>
    <div style="height:0.16in;"></div>
    <div class="takeaway">
      <span class="label">Content source</span>
      Directly from the Christian Advisor Network brochure&rsquo;s opening sections &mdash; More Than a Professional Association, The Central Promise, and the twenty-item implementation kit checklist. No new writing required.
    </div>
    <div style="height:0.16in;"></div>
    <div class="takeaway">
      <span class="label">Design note</span>
      &ldquo;One resource, many uses&rdquo; is the line worth making a recurring visual motif across the site &mdash; personal growth, client engagement, family conversations, team development, church ministry, all from the same underlying resource.
    </div>
    <div style="height:0.16in;"></div>
    <div class="takeaway">
      <span class="label">Primary conversions</span>
      Take the Faith &amp; Practice Alignment Assessment (low-commitment first step) &middot; Download the brochure &middot; Join the Network
    </div>
  </div>
  {folio("Home & Central Promise", 6)}
</div>
''')

# =================================================================
# PAGE 7 — DEEP DIVE: SEVEN BREAKTHROUGH RESOURCES + RESOURCE RACK
# =================================================================
add(f'''
<div class="page navy">
  <div class="frame">
    <div class="eyebrow">SECTION DEEP-DIVE</div>
    <div style="height:0.16in;"></div>
    <h1 class="display" style="font-size:18pt; color:#FBF8F1;">The Seven Breakthrough Resources &amp; the Resource Rack</h1>
    <div style="height:0.14in;"></div>
    <p class="lede">
      This is the platform&rsquo;s equivalent of Track One&rsquo;s 40 Day Campaigns catalog: the
      part that behaves like a real content library, not a brochure. Two structures sit
      side by side &mdash; seven flagship, deep-dive systems, and a ten-category rack of
      shorter topical resources underneath them.
    </p>
    <div style="height:0.16in;"></div>
    <div class="takeaway">
      <span class="label">Two ways to browse</span>
      By flagship resource (the seven numbered systems, each a destination page with its own sub-navigation) and by life topic (the ten Resource Rack categories) &mdash; an advisor with a client crisis this week should find the right resource by topic before he ever thinks in terms of &ldquo;which numbered system.&rdquo;
    </div>
    <div style="height:0.16in;"></div>
    <div class="takeaway">
      <span class="label">Every resource page needs</span>
      The full implementation kit made visible and downloadable in place &mdash; advisor guide, client-facing PDF, conversation script, presentation slides, follow-up email, and the rest &mdash; matching the &ldquo;from content to transformation&rdquo; promise exactly.
    </div>
  </div>
  {folio("Seven Breakthrough Resources & Resource Rack", 7)}
</div>
''')

# =================================================================
# PAGE 8 — DEEP DIVE: CHURCH PARTNERSHIP + MEMBERSHIP PRICING
# =================================================================
add(f'''
<div class="page">
  <div class="frame">
    <div class="eyebrow">SECTION DEEP-DIVE</div>
    <div style="height:0.16in;"></div>
    <h1 class="display" style="font-size:18pt; color:var(--navy);">Church Partnership &amp; Membership</h1>
    <div style="height:0.14in;"></div>
    <p class="lede">
      Church Partnership is the section doing the most delicate work on the whole site:
      it has to reassure a skeptical pastor reading over an advisor&rsquo;s shoulder as much as
      it motivates the advisor. The Five Levels model exists precisely so nobody has to
      guess how much trust has been earned yet.
    </p>
    <div style="height:0.16in;"></div>
    <div class="takeaway">
      <span class="label">Content source</span>
      The Advisor-Church Partnership Playbook section of the brochure &mdash; What Pastors Fear / What Advisors Fear, the Partnership Covenant, the Five Levels, the seven-step pathway, and the 21-seminar list &mdash; all fully written already.
    </div>
    <div style="height:0.16in;"></div>
    <div class="takeaway">
      <span class="label">Recommended structure</span>
      Lead with the Partnership Covenant and &ldquo;what pastors fear&rdquo; before anything else on this page &mdash; a pastor who lands here needs to see the guardrails before the opportunity, or the whole section reads as exactly the pitch he&rsquo;s worried about.
    </div>
    <div style="height:0.16in;"></div>
    <div class="takeaway">
      <span class="label">Membership pricing</span>
      One membership tier structure, most naturally organized around the Five Growth Pathways (Grow Yourself, Grow Your Practice, Serve Families, Partner with Churches, Build Community) rather than a generic Basic/Pro/Enterprise ladder &mdash; the pathways are already the differentiator, so the pricing page should use their language.
    </div>
  </div>
  {folio("Church Partnership & Membership", 8)}
</div>
''')

# =================================================================
# PAGE 9 — CONTENT MAPPING TABLE
# =================================================================
mapping_rows = [
    ("Christian Advisor Network brochure (17-page)", "Full source content for the entire public site"),
    ("The Central Promise &amp; implementation kit checklist", "Homepage + a recurring &ldquo;what you get&rdquo; motif across every resource page"),
    ("The Complete Resource Rack (10 categories)", "Resource Rack browse page + Member Portal library"),
    ("The Seven Breakthrough Resources", "Seven individual product pages, each with its own Member Portal workspace"),
    ("Five Levels of Church Partnership", "Church Partnership page, staged as a visual pathway"),
    ("How to Partner with a Local Church (7 steps)", "Church Partnership page, secondary diagram"),
    ("A Seminar for Every Season (21 titles)", "Church Partnership &rarr; seminar library sub-page"),
    ("The Strategic Advantage", "Membership / pricing page, positioning section"),
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
    <p class="lede" style="font-size:9.6pt;">As with Track One, every page in this architecture already has a source document. This is a porting job first, a writing job second.</p>
    <div style="height:0.1in;"></div>
    {map_html}
  </div>
  {folio("Content Mapping", 9)}
</div>
''')

# =================================================================
# PAGE 10 — NAVIGATION CONCEPT
# =================================================================
nav_items = ["The Seven Breakthrough Resources", "The Resource Rack", "Church Partnership", "Membership", "About"]
add(f'''
<div class="page">
  <div class="frame">
    <div class="eyebrow">NAVIGATION CONCEPT</div>
    <div style="height:0.16in;"></div>
    <h1 class="display" style="font-size:19pt; color:var(--navy);">Five items again &mdash; a deliberate echo of Track One.</h1>
    <div style="height:0.14in;"></div>
    <div class="chip-row-static">{"".join([f'<div class="track-chip">{n}</div>' for n in nav_items])}</div>
    <div style="height:0.2in;"></div>
    <p class="lede" style="font-size:9.6pt;">
      &ldquo;The Resource Rack&rdquo; is this track&rsquo;s mega-menu candidate &mdash; ten categories
      is enough depth to warrant a dropdown with topic previews rather than a plain link
      list, though nowhere near the scale of Track One&rsquo;s 10,000-campaign catalog.
    </p>
    <div style="height:0.16in;"></div>
    <div class="takeaway">
      <span class="label">Utility nav</span>
      Log In / My Resource Rack (portal access) and Join the Network (CTA) sit top-right on every page, mirroring Track One&rsquo;s Log In / My Library pattern exactly &mdash; useful if these ever share a design system or account layer.
    </div>
    <div style="height:0.16in;"></div>
    <div class="takeaway">
      <span class="label">Shared visual language, separate voice</span>
      Same navy/gold/Playfair system as Track One is recommended for brand consistency, but the copy voice shifts &mdash; more direct and practice-oriented, less pastoral &mdash; which the brochure already models well.
    </div>
  </div>
  {folio("Navigation Concept", 10)}
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
    <h1 class="display" style="font-size:19pt; color:#FBF8F1;">The same MVP platform, a second product on it.</h1>
    <div style="height:0.14in;"></div>
    <p class="lede">
      Track One&rsquo;s recommendation holds here without much change: a subscription
      content platform (Kajabi, or Mighty Networks if community matters more) can host
      a second membership product alongside the pastor-facing one, rather than requiring
      an entirely separate system.
    </p>
    <div style="height:0.18in;"></div>
    <div class="takeaway">
      <span class="label">Recommended approach</span>
      One platform account, two membership products &mdash; &ldquo;40 Day Campaigns&rdquo; and &ldquo;Christian Advisor Network&rdquo; as separate offers/subscriptions within the same Kajabi or Mighty Networks instance, rather than two unrelated platform accounts.
    </div>
    <div style="height:0.16in;"></div>
    <div class="takeaway">
      <span class="label">Why this matters</span>
      Advisors and pastors will eventually need to interact (Church Partnership is built on exactly that relationship) &mdash; a shared backend makes a future cross-referral or shared-resource feature possible later without a re-platform.
    </div>
    <div style="height:0.16in;"></div>
    <div class="takeaway">
      <span class="label">Sequencing</span>
      Validate the Pastor Track subscriber base first, then layer the Advisor Track membership on the same infrastructure once billing and content delivery are proven.
    </div>
  </div>
  {folio("Platform & Technology Path", 11)}
</div>
''')

# =================================================================
# PAGE 12 — INTEGRATION QUESTIONS & WHAT'S NEXT
# =================================================================
questions = [
    "Same domain (lifetogether.com/advisors) or a distinct domain for the Christian Advisor Network? Affects SEO, trust signals, and how separately the brand needs to feel.",
    "Shared login between the pastor platform and the advisor platform, or fully separate accounts? (Version 1.0 raised this too &mdash; answering it here should resolve both at once.)",
    "Does an advisor's Church Partnership activity ever surface inside the Pastor Track's site (e.g. a directory of vetted advisor partners a pastor could browse)? That would be a genuine cross-track feature, not just shared branding.",
    "Is membership tiered (e.g. individual advisor vs. team/practice-wide), and does that change what the Member Portal needs to support (multiple seats, practice branding)?",
    "What is the actual go-live scope &mdash; all Seven Breakthrough Resources at once, or a curated launch set (e.g. the Alignment Assessment and the 40-Day Growth Builder first, as the two lowest-friction entry points)?",
]
q_html = "".join([f'<div class="faq"><div class="faq-q" style="font-size:10.5pt;">{i+1}. {q}</div></div>' for i, q in enumerate(questions)])
add(f'''
<div class="page">
  <div class="frame">
    <div class="eyebrow">INTEGRATION QUESTIONS &amp; WHAT&rsquo;S NEXT</div>
    <div style="height:0.16in;"></div>
    <h1 class="display" style="font-size:18pt; color:var(--navy);">Where the two tracks actually meet</h1>
    <div style="height:0.14in;"></div>
    {q_html}
    <div style="height:0.2in;"></div>
    <div class="takeaway">
      <span class="label">With both drafts on the table</span>
      Version 1.0 and Version 2.0 can now be reviewed side by side as one master architecture &mdash; the next useful step is probably a single combined document that shows both sitemaps plus the answers to the integration questions above, once those are decided.
    </div>
  </div>
  {folio("Integration Questions & What's Next", 12)}
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
      <h1 class="display" style="font-size:20pt; color:#FBF8F1;">Version 2.0 &mdash; mark it up too.</h1>
      <div style="height:0.18in;"></div>
      <p class="lede" style="max-width:4.4in; margin:0 auto;">
        Both tracks are now drafted. Whenever you&rsquo;re ready, the next step is deciding the
        integration questions on page 12 &mdash; then we can merge both into one master site
        architecture document.
      </p>
      <div style="height:0.3in;"></div>
      <div style="width:30px; height:2px; background:#B98D3E; margin:0 auto;"></div>
    </div>
    <div style="font-family:'Archivo'; font-weight:500; font-size:7.4pt; letter-spacing:0.1em; color:rgba(251,248,241,0.4);">MASTER WEBSITE ARCHITECTURE &middot; VERSION 2.0 &middot; ADVISOR TRACK</div>
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

with open("/home/claude/build/site_architecture_v2.html", "w") as f:
    f.write(html)
print("Pages:", len(PAGES))
