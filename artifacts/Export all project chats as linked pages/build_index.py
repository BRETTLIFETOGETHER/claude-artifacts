#!/usr/bin/env python3
"""Build the LifeTogether Complete Archive master index with verified links."""
import base64, os, re
from pathlib import Path
from pypdf import PdfReader

BUILD = Path("/home/claude/archive_build")
FONTS = Path("/home/claude/fonts")

# ---- Curated catalog: every one of the 23 project PDFs, organized ----
CATALOG = {
    "Campaign Catalogs & Libraries": [
        ("40Day_Campaign_Title_Catalog___Lifetogether.pdf", "40 Day Campaign Title Catalog",
         "The master title catalog for the platform — campaign titles organized across categories and themes."),
        ("The_Complete_Campaign_Catalog___Ten_Themes___Lifetogether.pdf", "The Complete Campaign Catalog — Ten Themes",
         "The full catalog organized around the ten foundational campaign themes."),
        ("Extended_Campaign_Library___Lifetogether.pdf", "Extended Campaign Library",
         "Expansion of the core library with additional campaigns across the category set."),
        ("Seasonal_Campaign_Catalog___Lifetogether.pdf", "Seasonal Campaign Catalog",
         "Calendar-anchored campaigns organized by church seasons and yearly rhythms."),
        ("18_More_Campaigns___Lifetogether_Complete_Library.pdf", "18 More Campaigns — Complete Library",
         "Eighteen additional campaigns extending the complete library."),
        ("Nine_More_Campaigns___Lifetogether_Platform_Library.pdf", "Nine More Campaigns — Platform Library",
         "Nine additional campaigns added to the platform library."),
        ("Lifetogether_Campaign_Packages.pdf", "Lifetogether Campaign Packages",
         "Pre-configured campaign packages organized by ministry need and audience."),
    ],
    "The Seven Day Experience": [
        ("The_Seven_Day_Experience___Lifetogether.pdf", "The Seven Day Experience",
         "The foundational seven-day on-ramp experience for churches and participants."),
        ("Nobody_Does_This_Alone___The_Seven_Day_Experience.pdf", "Nobody Does This Alone",
         "The Seven Day Experience framed around community and small-group connection."),
        ("The_Story_Engine___Lifetogether_Seven_Day_Experience.pdf", "The Story Engine",
         "The story-driven architecture behind the Seven Day Experience."),
        ("Seven_Days_of_Prayer___Lifetogether.pdf", "Seven Days of Prayer",
         "A prayer-focused seven-day devotional journey edition."),
    ],
    "Sales & Launch Playbooks": [
        ("Why_This_Changes_Everything___Lifetogether_Campaign_Platform.pdf", "Why This Changes Everything",
         "The core value story for the campaign platform and why it transforms church launches."),
        ("Do_Not_Launch_Your_Next_Series_Cold___Lifetogether.pdf", "Do Not Launch Your Next Series Cold",
         "The launch playbook: why every series needs a campaign runway, and how to build one."),
        ("Every_Objection__Every_Answer____Lifetogether.pdf", "Every Objection, Every Answer",
         "Complete objection-handling guide for pastor and church-leader conversations."),
        ("Each_One_Ask_One___Lifetogether.pdf", "Each One Ask One",
         "The grassroots invitation strategy for growing campaign participation person by person."),
    ],
    "Pastor Resources": [
        ("Lifetogether___For_Senior_Pastors.pdf", "For Senior Pastors",
         "Positioning and resources built specifically for the senior pastor audience."),
        ("The_First_100_Pastors_Webinar___Lifetogether.pdf", "The First 100 Pastors Webinar",
         "Webinar content and framing for the first one hundred pastor adopters."),
    ],
    "Investor & Partner Documents": [
        ("Lifetogether_Kingdom_Investor_OnePager.pdf", "Kingdom Investor One-Pager",
         "One-page investment opportunity for kingdom-minded investors."),
        ("Lifetogether_Kingdom_Investor_OnePager_md.pdf", "Kingdom Investor One-Pager (Edition 2)",
         "Companion edition of the Kingdom Investor one-pager."),
        ("Lifetogether_Donor_Edition_OnePager_md.pdf", "Donor Edition One-Pager",
         "Donor-facing one-pager with the impact story and giving pathway."),
        ("Lifetogether_Gloo_Partnership_Proposal_md.pdf", "Gloo Partnership Proposal",
         "Strategic partnership proposal for the Gloo platform."),
    ],
    "Research & Working Notes": [
        ("Chat_Search-40_Day_pastor_needs___emails_____pastor_advisor_.pdf", "Pastor Needs, Emails & Advisor Research",
         "Research capture on pastor needs, outreach emails, and the pastor–advisor channel."),
        ("Claude_Search_-_40-day_campaign_structure_options_.pdf", "40-Day Campaign Structure Options",
         "Analysis of campaign structure options and format recommendations."),
    ],
}

# ---- Verify complete coverage: no file skipped, no phantom links ----
actual = sorted(p.name for p in BUILD.glob("*.pdf"))
listed = sorted(f for items in CATALOG.values() for (f, _, _) in items)
missing_from_index = [f for f in actual if f not in listed]
phantom = [f for f in listed if f not in actual]
assert not missing_from_index, f"Files not in index: {missing_from_index}"
assert not phantom, f"Index links to missing files: {phantom}"
print(f"Coverage check passed: all {len(actual)} PDFs indexed, zero phantom links")

# ---- Real metadata per file ----
meta, total_pages = {}, 0
for f in actual:
    pages = len(PdfReader(BUILD / f).pages)
    mb = os.path.getsize(BUILD / f) / (1024 * 1024)
    meta[f] = (pages, mb)
    total_pages += pages
total_mb = sum(m[1] for m in meta.values())
print(f"Metadata: {len(actual)} documents, {total_pages} pages, {total_mb:.1f} MB")

# ---- Embed brand fonts ----
def b64font(name):
    p = FONTS / name
    return base64.b64encode(p.read_bytes()).decode() if p.exists() else None

pf, sp, ar = b64font("Playfair.ttf"), b64font("Spectral.ttf"), b64font("Archivo.ttf")
font_css = ""
if pf: font_css += f"@font-face{{font-family:'Playfair Display';src:url(data:font/ttf;base64,{pf});font-weight:400 900;}}\n"
if sp: font_css += f"@font-face{{font-family:'Spectral';src:url(data:font/ttf;base64,{sp});font-weight:400;}}\n"
if ar: font_css += f"@font-face{{font-family:'Archivo';src:url(data:font/ttf;base64,{ar});font-weight:100 900;font-stretch:62.5% 125%;}}\n"

# ---- Build index.html ----
def anchor(s):
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")

toc = "".join(
    f'<a class="toc-link" href="#{anchor(cat)}">{cat}<span class="toc-count">{len(items)}</span></a>'
    for cat, items in CATALOG.items()
)

sections = ""
for cat, items in CATALOG.items():
    cards = ""
    for fname, title, desc in items:
        pages, mb = meta[fname]
        cards += f"""
        <a class="card" href="{fname}">
          <div class="card-eyebrow">{cat}</div>
          <h3>{title}</h3>
          <p>{desc}</p>
          <div class="card-meta"><span class="chip">{pages} pages</span><span class="chip">{mb:.1f} MB</span><span class="open">Open PDF &rarr;</span></div>
        </a>"""
    sections += f"""
    <section class="section" id="{anchor(cat)}">
      <div class="section-head"><h2>{cat}</h2><span class="rule"></span><span class="count">{len(items)} documents</span></div>
      <div class="grid">{cards}
      </div>
    </section>"""

html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Lifetogether &mdash; Complete Project Archive</title>
<style>
{font_css}
:root {{ --navy:#101E38; --navy2:#1a2d4d; --cream:#FBF8F1; --gold:#B98D3E; --gold-lt:#D9B876; --ink:#2b2b2b; }}
* {{ margin:0; padding:0; box-sizing:border-box; }}
body {{ font-family:'Spectral', Georgia, serif; background:var(--cream); color:var(--ink); line-height:1.6; }}
.header {{ background:linear-gradient(135deg, var(--navy) 0%, var(--navy2) 100%); color:var(--cream); padding:64px 24px 48px; text-align:center; border-bottom:3px solid var(--gold); }}
.header .eyebrow {{ font-family:'Archivo', sans-serif; font-size:12px; letter-spacing:3px; text-transform:uppercase; color:var(--gold-lt); margin-bottom:14px; }}
.header h1 {{ font-family:'Playfair Display', Georgia, serif; font-size:44px; font-weight:700; letter-spacing:-0.5px; margin-bottom:12px; }}
.header p {{ max-width:640px; margin:0 auto 26px; opacity:.92; font-size:17px; }}
.stats {{ display:flex; gap:12px; justify-content:center; flex-wrap:wrap; }}
.stat {{ font-family:'Archivo', sans-serif; font-size:13px; letter-spacing:1px; text-transform:uppercase; border:1px solid rgba(217,184,118,.5); border-radius:999px; padding:8px 18px; color:var(--gold-lt); }}
.container {{ max-width:1180px; margin:0 auto; padding:36px 20px 20px; }}
.searchbar {{ position:sticky; top:0; z-index:5; background:var(--cream); padding:18px 0 14px; }}
.searchbar input {{ width:100%; font-family:'Spectral', Georgia, serif; font-size:17px; padding:14px 20px; border:1px solid #d8d2c4; border-left:4px solid var(--gold); border-radius:6px; background:#fff; color:var(--ink); outline:none; }}
.searchbar input:focus {{ border-color:var(--gold); box-shadow:0 2px 10px rgba(185,141,62,.18); }}
.toc {{ display:flex; flex-wrap:wrap; gap:10px; margin:6px 0 8px; }}
.toc-link {{ font-family:'Archivo', sans-serif; font-size:13px; letter-spacing:.5px; text-decoration:none; color:var(--navy); background:#fff; border:1px solid #e2dccd; border-radius:999px; padding:8px 16px; transition:all .2s; }}
.toc-link:hover {{ border-color:var(--gold); color:var(--gold); }}
.toc-count {{ margin-left:8px; color:var(--gold); font-weight:600; }}
.section {{ margin:34px 0 6px; }}
.section-head {{ display:flex; align-items:baseline; gap:16px; margin-bottom:18px; }}
.section-head h2 {{ font-family:'Playfair Display', Georgia, serif; font-size:27px; color:var(--navy); white-space:nowrap; }}
.section-head .rule {{ flex:1; height:1px; background:linear-gradient(90deg, var(--gold), transparent); }}
.section-head .count {{ font-family:'Archivo', sans-serif; font-size:12px; letter-spacing:1.5px; text-transform:uppercase; color:#9a9384; white-space:nowrap; }}
.grid {{ display:grid; grid-template-columns:repeat(auto-fill, minmax(320px, 1fr)); gap:18px; }}
.card {{ display:flex; flex-direction:column; background:#fff; border-radius:8px; padding:22px 22px 18px; text-decoration:none; color:inherit; border-left:4px solid var(--gold); box-shadow:0 2px 8px rgba(16,30,56,.08); transition:transform .22s, box-shadow .22s; }}
.card:hover {{ transform:translateY(-4px); box-shadow:0 10px 22px rgba(16,30,56,.16); }}
.card-eyebrow {{ font-family:'Archivo', sans-serif; font-size:10.5px; letter-spacing:2px; text-transform:uppercase; color:var(--gold); margin-bottom:8px; }}
.card h3 {{ font-family:'Playfair Display', Georgia, serif; font-size:19px; line-height:1.3; color:var(--navy); margin-bottom:8px; }}
.card p {{ font-size:14.5px; color:#5c5a54; flex:1; margin-bottom:14px; }}
.card-meta {{ display:flex; align-items:center; gap:8px; }}
.chip {{ font-family:'Archivo', sans-serif; font-size:11px; letter-spacing:1px; text-transform:uppercase; background:var(--cream); border:1px solid #e2dccd; border-radius:999px; padding:4px 10px; color:#7a7365; }}
.open {{ margin-left:auto; font-family:'Archivo', sans-serif; font-size:12.5px; letter-spacing:.5px; color:var(--navy); font-weight:600; }}
.card:hover .open {{ color:var(--gold); }}
.companion {{ margin:44px 0 10px; background:#fff; border:1px solid #e2dccd; border-left:4px solid var(--navy); border-radius:8px; padding:24px 26px; }}
.companion h2 {{ font-family:'Playfair Display', Georgia, serif; font-size:20px; color:var(--navy); margin-bottom:10px; }}
.companion p {{ font-size:14.5px; color:#5c5a54; }}
.footer {{ background:var(--navy); color:var(--cream); text-align:center; padding:34px 20px; margin-top:48px; border-top:3px solid var(--gold); }}
.footer .fm {{ font-family:'Playfair Display', Georgia, serif; font-size:19px; margin-bottom:6px; }}
.footer p {{ font-size:13.5px; opacity:.85; }}
.hidden {{ display:none !important; }}
.noresults {{ display:none; text-align:center; font-style:italic; color:#8a8375; padding:40px 0; }}
@media (max-width:700px) {{ .header h1 {{ font-size:30px; }} .section-head h2 {{ font-size:22px; white-space:normal; }} }}
</style>
</head>
<body>
<div class="header">
  <div class="eyebrow">Lifetogether &middot; 40 Day Campaigns</div>
  <h1>Complete Project Archive</h1>
  <p>Every document in the project, in one linked library. Click any card to open the full PDF &mdash; all files travel inside this archive.</p>
  <div class="stats"><span class="stat">{len(actual)} Documents</span><span class="stat">{total_pages} Pages</span><span class="stat">{total_mb:.1f} MB</span><span class="stat">6 Collections</span></div>
</div>
<div class="container">
  <div class="searchbar"><input id="q" type="search" placeholder="Search the library &mdash; title, topic, or keyword&hellip;" aria-label="Search documents"></div>
  <div class="toc">{toc}</div>
  {sections}
  <div class="noresults" id="noresults">No documents match that search.</div>
  <div class="companion">
    <h2>Companion Deliverables From This Project</h2>
    <p>Delivered separately in their original working sessions and not stored in the project files: the full 40daycampaigns.com website build (37+ linked HTML pages &mdash; <em>40daycampaigns_platform_10k.zip</em>), the Spanish and Portuguese site editions, the twelve-page Family Legacy by Design site, and the 76-page <em>10,000 Campaigns &mdash; Master Strategy, Part&nbsp;1</em> PDF. Add any of those files to the project and they can be folded into this archive.</p>
  </div>
</div>
<div class="footer">
  <div class="fm">Lifetogether</div>
  <p>brett@lifetogether.com &middot; 40daycampaigns.com</p>
  <p style="margin-top:10px; opacity:.65;">Archive generated July 2026 &middot; Every link verified against archive contents</p>
</div>
<script>
(function() {{
  var q = document.getElementById('q');
  q.addEventListener('input', function() {{
    var t = q.value.trim().toLowerCase(), any = false;
    document.querySelectorAll('.card').forEach(function(c) {{
      var hit = !t || c.textContent.toLowerCase().indexOf(t) !== -1;
      c.classList.toggle('hidden', !hit);
      if (hit) any = true;
    }});
    document.querySelectorAll('.section').forEach(function(s) {{
      s.classList.toggle('hidden', s.querySelectorAll('.card:not(.hidden)').length === 0);
    }});
    document.getElementById('noresults').style.display = any ? 'none' : 'block';
  }});
}})();
</script>
</body>
</html>
"""

(BUILD / "index.html").write_text(html)
print(f"index.html written: {len(html)/1024:.0f} KB (fonts embedded: {sum(1 for x in (pf,sp,ar) if x)}/3)")
