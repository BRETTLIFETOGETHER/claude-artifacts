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
    <div style="font-family:'Archivo'; font-weight:600; font-size:9pt; letter-spacing:0.22em; color:#D9B876; margin-bottom:2.4in;">INTERNAL STRATEGY DOCUMENT &middot; DRAFT FOR DISCUSSION</div>
    <h1 class="display" style="font-size:26pt; color:#FBF8F1; line-height:1.2;">The Subscription Library</h1>
    <div style="height:0.14in;"></div>
    <div style="font-family:'Playfair'; font-style:italic; font-weight:600; font-size:14pt; color:#D9B876;">What it takes to earn a yes &mdash; and where the four platforms hand off to each other</div>
    <div style="height:0.24in;"></div>
    <p class="lede" style="font-size:10.3pt; color:rgba(251,248,241,0.8); max-width:5.6in;">
      Answering two questions: what does the Christian Advisor Network actually need to be
      worth paying for, and how should it connect to Kingdom Advisors, the Church platform,
      Family Legacy By Design, and Financial Wisdom Ministry.
    </p>
  </div>
</div>
''')

# =================================================================
# PAGE 2 — THE BUSINESS MODEL, CONFIRMED
# =================================================================
add(f'''
<div class="page">
  <div class="frame">
    <div class="eyebrow">THE BUSINESS MODEL, CONFIRMED</div>
    <div style="height:0.2in;"></div>
    <h1 class="display" style="font-size:21pt; color:var(--navy);">You&rsquo;re not building a directory. You&rsquo;re building a library.</h1>
    <div style="height:0.16in;"></div>
    <p class="lede">
      That&rsquo;s a real and useful clarification, and it changes what the site should do. The
      Christian Advisor Network&rsquo;s job is to sell access to downloadable resources, courses,
      and materials &mdash; not to match advisors with clients, and not to certify or vet advisors.
      That work already belongs to Kingdom Advisors.
    </p>
    <div style="height:0.2in;"></div>
    <div class="takeaway">
      <span class="label">What this means for Find an Advisor</span>
      Retire the built-out directory (search, sample listings, &ldquo;List Your Practice&rdquo;). Replace it with a short, honest page: &ldquo;Looking for a Christian financial advisor, or ready to become one? Kingdom Advisors is the trusted network for that &mdash; visit kingdomadvisors.com.&rdquo; One clear outbound link, no competing directory.
    </div>
    <div style="height:0.16in;"></div>
    <div class="takeaway">
      <span class="label">Why this is the right call, not a compromise</span>
      A directory implies ongoing responsibility &mdash; vetting, moderation, dispute handling, liability. Referring that function to an established, trusted org lets the Network stay focused on the one thing it actually sells: content. Simpler scope, lower risk, and it&rsquo;s honest about who already does matching well.
    </div>
    <div style="height:0.16in;"></div>
    <p class="lede">
      Everything downstream of this page follows from that clarity. The subscription has to earn
      its price entirely on the strength of what&rsquo;s inside it &mdash; not on the promise of leads,
      matching, or a professional network.
    </p>
  </div>
  {folio("The Business Model, Confirmed", 2)}
</div>
''')

# =================================================================
# PAGE 3 — THE COMPREHENSIVE SUBSCRIPTION LIBRARY (Content Depth)
# =================================================================
content_items = [
    ("Resource Rack at real depth", "96 resources exist across 12 categories today. A library people pay to keep, not sample once, needs continuous additions — quarterly at minimum — so renewal feels justified every year, not just at signup."),
    ("All 12 assessments, fully built", "Only 2 of 12 have real content today (Alignment, Whole-Life Stewardship). The other 10 need actual questions, scoring logic, and output reports before they can be sold, not just named."),
    ("Video, not just PDF", "Every competitor in this space (RightNow Media, MasterClass, Ramsey+) leads with video. A library that's 100% text-and-PDF reads as a document dump, not a course platform, however well designed the pages are."),
    ("Courses with a start and finish", "The 40-Day Growth Builder is the only true 'course' — a defined beginning, middle, end, and completion state. Everything else in the Rack is a static reference. Subscribers pay more readily for something they can finish than something they can only browse."),
    ("Downloadable, editable templates", "The brand promise is 'client-facing PDF, ready to send.' That only holds if the actual editable files (not just descriptions of them) are in the account — Word, Canva, or PowerPoint sources, not just a locked PDF."),
]
rows = "".join([f'''
    <div style="border-top:1px solid var(--line); padding:0.16in 0;">
      <div style="font-family:'Playfair'; font-weight:700; font-size:12.5pt; color:var(--navy); margin-bottom:0.05in;">{t}</div>
      <div style="font-family:'Inter'; font-size:9.4pt; color:var(--ink); line-height:1.5;">{d}</div>
    </div>''' for t, d in content_items])
add(f'''
<div class="page">
  <div class="frame">
    <div class="eyebrow">THE COMPREHENSIVE LIBRARY &mdash; 1 OF 3: CONTENT DEPTH</div>
    <div style="height:0.18in;"></div>
    <h1 class="display" style="font-size:20pt; color:var(--navy);">What has to actually be inside the account.</h1>
    <div style="height:0.1in;"></div>
    {rows}
  </div>
  {folio("The Comprehensive Library", 3)}
</div>
''')

# =================================================================
# PAGE 4 — TRUST & CREDIBILITY SIGNALS
# =================================================================
trust_items = [
    ("A real, named endorsement", "Ron Blue's name is the foundation of the whole brand, but nothing on the site is a direct quote from him. One paragraph, attributed, changes the site from 'inspired by' to 'built with.'"),
    ("Real case studies, not placeholders", "Every success story on the site is currently marked '[XX]%' and 'Practice Name Placeholder.' That's honest, but it can't stay that way past the first handful of real members — it reads as unproven the longer it sits."),
    ("A visible community, even without a directory", "Retiring the public advisor directory doesn't mean retiring community. A private members-only cohort (not public-facing) gives subscribers something a static library alone can't: other advisors doing the same work."),
    ("A certificate or credential on completion", "Finishing the 40-Day Growth Builder or a full assessment track should produce something an advisor can point to — a certificate, a badge, a LinkedIn-shareable credential. This is the single highest-leverage addition for word-of-mouth growth."),
    ("Compliance sign-off, not just a 'coming soon' label", "The Compliance Disclosures page is still a stub. For an audience of SEC/FINRA-regulated advisors, this is not a nice-to-have before charging money — it's close to a blocker."),
]
rows2 = "".join([f'''
    <div style="border-top:1px solid var(--line); padding:0.16in 0;">
      <div style="font-family:'Playfair'; font-weight:700; font-size:12.5pt; color:var(--navy); margin-bottom:0.05in;">{t}</div>
      <div style="font-family:'Inter'; font-size:9.4pt; color:var(--ink); line-height:1.5;">{d}</div>
    </div>''' for t, d in trust_items])
add(f'''
<div class="page">
  <div class="frame">
    <div class="eyebrow">THE COMPREHENSIVE LIBRARY &mdash; 2 OF 3: TRUST &amp; CREDIBILITY</div>
    <div style="height:0.18in;"></div>
    <h1 class="display" style="font-size:20pt; color:var(--navy);">What makes a regulated professional believe this is real.</h1>
    <div style="height:0.1in;"></div>
    {rows2}
  </div>
  {folio("The Comprehensive Library", 4)}
</div>
''')

# =================================================================
# PAGE 5 — CONVERSION & RETENTION MECHANICS
# =================================================================
conv_items = [
    ("A reason to come back monthly", "A library with zero new content past launch gets used once and forgotten. New resource, new assessment, or new seminar added on a visible monthly cadence is what turns a one-time purchase into a renewal."),
    ("A clear free-to-paid moment", "The 10-free/96-total pattern is already built and works well — the missing piece is a specific trigger, like an email at 'you've viewed your 8th free resource' nudging toward membership before someone drifts away."),
    ("Founding-member pricing with a real deadline", "A 'Founding Advisor Cohort' at a locked-in rate for the first 50 or 100 members creates urgency without discounting the ongoing price — and gives early members a status reason to join now instead of later."),
    ("Team and firm-level pricing, not just solo", "Advisors at regional firms (12+ advisors, per your own case study placeholder) need a per-seat or firm-wide option. Solo-only pricing caps the size of every deal before it starts."),
    ("An annual, not just monthly, option", "Annual billing at a discount is standard for content subscriptions and meaningfully improves cash flow and reduces churn — worth having from day one, not added later."),
]
rows3 = "".join([f'''
    <div style="border-top:1px solid var(--line); padding:0.16in 0;">
      <div style="font-family:'Playfair'; font-weight:700; font-size:12.5pt; color:var(--navy); margin-bottom:0.05in;">{t}</div>
      <div style="font-family:'Inter'; font-size:9.4pt; color:var(--ink); line-height:1.5;">{d}</div>
    </div>''' for t, d in conv_items])
add(f'''
<div class="page">
  <div class="frame">
    <div class="eyebrow">THE COMPREHENSIVE LIBRARY &mdash; 3 OF 3: CONVERSION &amp; RETENTION</div>
    <div style="height:0.18in;"></div>
    <h1 class="display" style="font-size:20pt; color:var(--navy);">What actually gets someone to pay, and to keep paying.</h1>
    <div style="height:0.1in;"></div>
    {rows3}
  </div>
  {folio("The Comprehensive Library", 5)}
</div>
''')

# =================================================================
# PAGE 6 — AM I MISSING AN OPPORTUNITY?
# =================================================================
add(f'''
<div class="page navy">
  <div class="frame">
    <div class="eyebrow">AM I MISSING AN OPPORTUNITY?</div>
    <div style="height:0.2in;"></div>
    <h1 class="display" style="font-size:21pt; color:#FBF8F1;">Yes &mdash; three, specifically.</h1>
    <div style="height:0.18in;"></div>
    <div class="takeaway">
      <span class="label">1. The certificate is worth more than it looks</span>
      A completion credential for the 40-Day Growth Builder costs almost nothing to build and does two things at once: gives a subscriber a reason to actually finish (completion, not just access, is the real value of a course), and turns every graduate into a walking advertisement when they post it.
    </div>
    <div style="height:0.16in;"></div>
    <div class="takeaway">
      <span class="label">2. The referral relationship with Kingdom Advisors can run both directions</span>
      Right now the plan is a one-way outbound link. Worth a direct conversation with Kingdom Advisors about becoming their recommended content and training partner &mdash; their members need exactly what this library sells, and you need exactly the audience they already have. That's a partnership conversation, not just a courtesy link.
    </div>
    <div style="height:0.16in;"></div>
    <div class="takeaway">
      <span class="label">3. Firms are a bigger opportunity than solo advisors</span>
      Every price point on the site today reads as built for one person. A 12-advisor regional firm buying one firm-wide license is a materially larger and stickier sale than 12 individual signups &mdash; and it's the same content, just packaged and priced differently.
    </div>
  </div>
  {folio("Am I Missing an Opportunity?", 6)}
</div>
''')

# =================================================================
# PAGE 7 — THE CROSS-PLATFORM REFERRAL STRATEGY
# =================================================================
referral_tree = f'''
{l1("Christian Advisor Network", "the hub for advisors")}
{l2("Refers OUT to Kingdom Advisors", "for advisor matching &amp; certification")}
{l2("Refers IN from the Church platform", "when a pastor's page mentions advisor partnership")}
{l2("Cross-sells", "Family Legacy By Design and Financial Wisdom Ministry as bundled or add-on access")}

{l1("The Church Platform", "40 Day Campaigns / Church Formation System")}
{l2("Refers OUT to Christian Advisor Network", "on the Church Partnership pages, for pastors seeking vetted advisor content")}
{l2("Refers OUT to Family Legacy By Design", "as the flagship campaign for high-capacity families")}

{l1("Family Legacy By Design")}
{l2("Refers OUT to Christian Advisor Network", "already built — the 'For Advisors' page")}
{l2("Refers OUT to the Church Platform", "for the full 40-day campaign delivery mechanism")}

{l1("Financial Wisdom Ministry", "not yet built")}
{l2("Would refer OUT to Christian Advisor Network", "for the advisor-facing version of the same content")}
{l2("Would refer OUT to the Church Platform", "for the 40 Days of Financial Wisdom and Generous Living campaigns")}
'''
add(f'''
<div class="page">
  <div class="frame">
    <div class="eyebrow">THE CROSS-PLATFORM REFERRAL STRATEGY</div>
    <div style="height:0.16in;"></div>
    <h1 class="display" style="font-size:19pt; color:var(--navy);">Four platforms, one family, deliberate handoffs.</h1>
    <div style="height:0.14in;"></div>
    <div class="tree">{referral_tree}</div>
  </div>
  {folio("The Cross-Platform Referral Strategy", 7)}
</div>
''')

# =================================================================
# PAGE 8 — WHAT CHANGES ON THE LIVE SITE
# =================================================================
changes = [
    ("Replace Find an Advisor", "Remove the search/filter directory and sample listings. Replace with a single referral page and an outbound link to Kingdom Advisors."),
    ("Add a Kingdom Advisors mention to the footer", "A short, permanent line — 'Looking for an advisor, or want to become one? Visit Kingdom Advisors.' — so it's never buried."),
    ("Add cross-platform links to the nav or footer", "Simple outbound cards to the Church platform, Family Legacy By Design, and (once built) Financial Wisdom Ministry — positioned as 'Also from LifeTogether,' not folded into the main nav."),
    ("Build the completion certificate", "A simple downloadable/shareable credential for finishing the 40-Day Growth Builder — the single highest-leverage item on this list relative to effort."),
    ("Add firm-level pricing language to Membership", "Even before final pricing is set, the Membership page should mention team seats exist as an option, so a firm doesn't bounce assuming it's solo-only."),
]
rows4 = "".join([f'''
    <div style="border-top:1px solid var(--line); padding:0.15in 0;">
      <div style="font-family:'Playfair'; font-weight:700; font-size:12pt; color:var(--navy); margin-bottom:0.04in;">{t}</div>
      <div style="font-family:'Inter'; font-size:9.2pt; color:var(--ink); line-height:1.5;">{d}</div>
    </div>''' for t, d in changes])
add(f'''
<div class="page">
  <div class="frame">
    <div class="eyebrow">WHAT CHANGES ON THE LIVE SITE</div>
    <div style="height:0.18in;"></div>
    <h1 class="display" style="font-size:20pt; color:var(--navy);">Five concrete edits, ready whenever you say go.</h1>
    <div style="height:0.1in;"></div>
    {rows4}
    <div style="height:0.24in;"></div>
    <div class="takeaway">
      <span class="label">What I'd do first</span>
      The Find an Advisor replacement and the footer cross-platform links are both quick, low-risk edits to the site already built. The certificate and firm pricing are slightly bigger but still same-session work. Financial Wisdom Ministry as a full platform is its own build, sized like Family Legacy By Design or Generosity Chemistry.
    </div>
  </div>
  {folio("What Changes on the Live Site", 8)}
</div>
''')

# =================================================================
# PAGE 9 — BACK COVER
# =================================================================
add(f'''
<div class="page navy">
  <div class="frame" style="display:flex; flex-direction:column; justify-content:space-between; align-items:center; text-align:center;">
    <div></div>
    <div>
      <div style="font-family:'Archivo'; font-weight:600; font-size:9.5pt; letter-spacing:0.24em; color:#D9B876;">LIFETOGETHER</div>
      <div style="height:0.26in;"></div>
      <h1 class="display" style="font-size:20pt; color:#FBF8F1;">Tell me which to build first.</h1>
      <div style="height:0.18in;"></div>
      <p class="lede" style="max-width:4.6in; margin:0 auto;">
        The five site edits, the completion certificate, or the Financial Wisdom Ministry
        platform &mdash; any of them can be next.
      </p>
      <div style="height:0.3in;"></div>
      <div style="width:30px; height:2px; background:#B98D3E; margin:0 auto;"></div>
    </div>
    <div style="font-family:'Archivo'; font-weight:500; font-size:7.4pt; letter-spacing:0.1em; color:rgba(251,248,241,0.4);">THE SUBSCRIPTION LIBRARY &middot; STRATEGY DRAFT</div>
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

html = f'''<!DOCTYPE html>
<html><head><meta charset="utf-8">
<style>{base_css}{tree_css}</style></head>
<body>{"".join(PAGES)}</body></html>'''

with open("/home/claude/build/subscription_library.html", "w") as f:
    f.write(html)
print("Pages:", len(PAGES))
