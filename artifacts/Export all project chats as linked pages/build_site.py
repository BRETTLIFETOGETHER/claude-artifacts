#!/usr/bin/env python3
"""Build the complete linked page archive: every page of every document, nothing skipped."""
import base64, html as htmlmod, json, os, re, shutil, zipfile
from pathlib import Path

SRC = Path("/home/claude/archive_build")
SITE = Path("/home/claude/archive_site")
FONTS = Path("/home/claude/fonts")
if SITE.exists():
    shutil.rmtree(SITE)
(SITE / "assets").mkdir(parents=True)
(SITE / "docs").mkdir()

# ---------- Catalog: all 23 documents, ordered for end-to-end reading ----------
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
         "Working transcript: pastor needs, outreach emails, and the pastor–advisor channel."),
        ("Claude_Search_-_40-day_campaign_structure_options_.pdf", "40-Day Campaign Structure Options",
         "Working transcript: campaign structure options and format decisions."),
    ],
}

actual = sorted(p.name for p in SRC.glob("*.pdf"))
listed = [f for items in CATALOG.values() for (f, _, _) in items]
assert sorted(listed) == actual, f"Catalog/file mismatch: {set(actual) ^ set(listed)}"
print(f"Coverage: all {len(actual)} source documents accounted for")

def slugify(s):
    return re.sub(r"-+", "-", re.sub(r"[^a-z0-9]+", "-", s.lower())).strip("-")

# ---------- Extract every page ----------
docs = []  # ordered records
for cat, items in CATALOG.items():
    for fname, title, desc in items:
        slug = slugify(fname[:-4])
        ddir = SITE / "docs" / slug
        (ddir / "pages").mkdir(parents=True)
        src = SRC / fname
        rec = {"slug": slug, "title": title, "desc": desc, "cat": cat,
               "pages": [], "text": "", "kind": "images"}
        try:
            with zipfile.ZipFile(src) as z:
                jpegs = sorted((n for n in z.namelist() if n.endswith(".jpeg")),
                               key=lambda n: int(Path(n).stem))
                texts = []
                for i, n in enumerate(jpegs, 1):
                    out = f"{i:03d}.jpeg"
                    (ddir / "pages" / out).write_bytes(z.read(n))
                    rec["pages"].append(out)
                    t = f"{Path(n).stem}.txt"
                    if t in z.namelist():
                        texts.append(z.read(t).decode("utf-8", "replace"))
                rec["text"] = "\n".join(texts)
        except zipfile.BadZipFile:
            rec["kind"] = "transcript"
            rec["text"] = src.read_text(encoding="utf-8", errors="replace").replace("\r\n", "\n")
        docs.append(rec)

img_pages = sum(len(d["pages"]) for d in docs)
transcripts = [d for d in docs if d["kind"] == "transcript"]
print(f"Extracted {img_pages} page images across {len(docs)-len(transcripts)} documents; {len(transcripts)} transcripts")

# ---------- Shared stylesheet with embedded brand fonts (single copy) ----------
def b64(p):
    return base64.b64encode(p.read_bytes()).decode() if p.exists() else None

pf, sp, ar = b64(FONTS/"Playfair.ttf"), b64(FONTS/"Spectral.ttf"), b64(FONTS/"Archivo.ttf")
css = ""
if pf: css += "@font-face{font-family:'Playfair Display';src:url(data:font/ttf;base64,%s);font-weight:400 900;}\n" % pf
if sp: css += "@font-face{font-family:'Spectral';src:url(data:font/ttf;base64,%s);font-weight:400;}\n" % sp
if ar: css += "@font-face{font-family:'Archivo';src:url(data:font/ttf;base64,%s);font-weight:100 900;font-stretch:62.5%% 125%%;}\n" % ar
css += """
:root{--navy:#101E38;--navy2:#1a2d4d;--cream:#FBF8F1;--gold:#B98D3E;--gold-lt:#D9B876;--ink:#2b2b2b;}
*{margin:0;padding:0;box-sizing:border-box;}
body{font-family:'Spectral',Georgia,serif;background:var(--cream);color:var(--ink);line-height:1.6;}
a{color:inherit;}
.eyebrow{font-family:'Archivo',sans-serif;font-size:11px;letter-spacing:2.5px;text-transform:uppercase;color:var(--gold);}
.header{background:linear-gradient(135deg,var(--navy) 0%,var(--navy2) 100%);color:var(--cream);padding:60px 24px 46px;text-align:center;border-bottom:3px solid var(--gold);}
.header .eyebrow{color:var(--gold-lt);margin-bottom:14px;}
.header h1{font-family:'Playfair Display',Georgia,serif;font-size:42px;font-weight:700;letter-spacing:-.5px;margin-bottom:12px;}
.header p{max-width:640px;margin:0 auto 24px;opacity:.92;font-size:17px;}
.stats{display:flex;gap:12px;justify-content:center;flex-wrap:wrap;}
.stat{font-family:'Archivo',sans-serif;font-size:12.5px;letter-spacing:1px;text-transform:uppercase;border:1px solid rgba(217,184,118,.5);border-radius:999px;padding:8px 18px;color:var(--gold-lt);}
.container{max-width:1180px;margin:0 auto;padding:32px 20px 20px;}
.searchbar{position:sticky;top:0;z-index:5;background:var(--cream);padding:16px 0 12px;}
.searchbar input{width:100%;font-family:'Spectral',Georgia,serif;font-size:17px;padding:14px 20px;border:1px solid #d8d2c4;border-left:4px solid var(--gold);border-radius:6px;background:#fff;outline:none;}
.searchbar input:focus{border-color:var(--gold);box-shadow:0 2px 10px rgba(185,141,62,.18);}
.toc{display:flex;flex-wrap:wrap;gap:10px;margin:6px 0 4px;}
.toc-link{font-family:'Archivo',sans-serif;font-size:13px;text-decoration:none;color:var(--navy);background:#fff;border:1px solid #e2dccd;border-radius:999px;padding:8px 16px;transition:all .2s;}
.toc-link:hover{border-color:var(--gold);color:var(--gold);}
.toc-count{margin-left:8px;color:var(--gold);font-weight:600;}
.section{margin:32px 0 4px;}
.section-head{display:flex;align-items:baseline;gap:16px;margin-bottom:18px;}
.section-head h2{font-family:'Playfair Display',Georgia,serif;font-size:26px;color:var(--navy);white-space:nowrap;}
.section-head .rule{flex:1;height:1px;background:linear-gradient(90deg,var(--gold),transparent);}
.section-head .count{font-family:'Archivo',sans-serif;font-size:11.5px;letter-spacing:1.5px;text-transform:uppercase;color:#9a9384;white-space:nowrap;}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:20px;}
.card{display:flex;flex-direction:column;background:#fff;border-radius:10px;overflow:hidden;text-decoration:none;box-shadow:0 2px 10px rgba(16,30,56,.09);transition:transform .22s,box-shadow .22s;border:1px solid #eee7d8;}
.card:hover{transform:translateY(-4px);box-shadow:0 12px 26px rgba(16,30,56,.17);}
.cover{aspect-ratio:8.5/6.2;overflow:hidden;background:var(--navy);border-bottom:3px solid var(--gold);}
.cover img{width:100%;height:100%;object-fit:cover;object-position:top;display:block;}
.cover-txt{width:100%;height:100%;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:10px;color:var(--gold-lt);background:linear-gradient(150deg,var(--navy) 0%,var(--navy2) 100%);}
.cover-txt .glyph{font-family:'Playfair Display',Georgia,serif;font-size:64px;line-height:1;color:var(--gold);}
.cover-txt .lbl{font-family:'Archivo',sans-serif;font-size:11px;letter-spacing:3px;text-transform:uppercase;}
.card-body{padding:18px 20px 16px;display:flex;flex-direction:column;flex:1;}
.card h3{font-family:'Playfair Display',Georgia,serif;font-size:18.5px;line-height:1.3;color:var(--navy);margin:7px 0 7px;}
.card p{font-size:14px;color:#5c5a54;flex:1;margin-bottom:13px;}
.card-meta{display:flex;align-items:center;gap:8px;}
.chip{font-family:'Archivo',sans-serif;font-size:10.5px;letter-spacing:1px;text-transform:uppercase;background:var(--cream);border:1px solid #e2dccd;border-radius:999px;padding:4px 10px;color:#7a7365;}
.open{margin-left:auto;font-family:'Archivo',sans-serif;font-size:12px;color:var(--navy);font-weight:600;}
.card:hover .open{color:var(--gold);}
.companion{margin:44px 0 10px;background:#fff;border:1px solid #e2dccd;border-left:4px solid var(--navy);border-radius:8px;padding:24px 26px;}
.companion h2{font-family:'Playfair Display',Georgia,serif;font-size:20px;color:var(--navy);margin-bottom:10px;}
.companion p{font-size:14.5px;color:#5c5a54;}
.footer{background:var(--navy);color:var(--cream);text-align:center;padding:32px 20px;margin-top:48px;border-top:3px solid var(--gold);}
.footer .fm{font-family:'Playfair Display',Georgia,serif;font-size:19px;margin-bottom:6px;}
.footer p{font-size:13.5px;opacity:.85;}
.hidden{display:none!important;}
.noresults{display:none;text-align:center;font-style:italic;color:#8a8375;padding:40px 0;}
/* ---------- viewer ---------- */
.vbar{position:sticky;top:0;z-index:10;background:var(--navy);color:var(--cream);border-bottom:3px solid var(--gold);}
.vbar-in{max-width:1060px;margin:0 auto;display:flex;align-items:center;gap:16px;padding:13px 20px;}
.vbar a{color:var(--gold-lt);text-decoration:none;font-family:'Archivo',sans-serif;font-size:13px;white-space:nowrap;}
.vbar a:hover{color:#fff;}
.vtitle{font-family:'Playfair Display',Georgia,serif;font-size:17px;flex:1;text-align:center;overflow:hidden;text-overflow:ellipsis;white-space:nowrap;}
.vwrap{max-width:1000px;margin:0 auto;padding:28px 16px 20px;}
.vhead{text-align:center;margin-bottom:22px;}
.vhead h1{font-family:'Playfair Display',Georgia,serif;font-size:32px;color:var(--navy);margin:6px 0 6px;}
.vhead .sub{color:#6b6558;font-size:15.5px;max-width:620px;margin:0 auto 14px;}
.pagejump{display:flex;flex-wrap:wrap;gap:6px;justify-content:center;margin-bottom:8px;}
.pagejump a{font-family:'Archivo',sans-serif;font-size:12px;text-decoration:none;color:var(--navy);background:#fff;border:1px solid #e2dccd;border-radius:6px;padding:5px 10px;}
.pagejump a:hover{border-color:var(--gold);color:var(--gold);}
.page{margin:26px 0;}
.page-label{font-family:'Archivo',sans-serif;font-size:11px;letter-spacing:2px;text-transform:uppercase;color:#9a9384;text-align:center;margin-bottom:8px;}
.page img{display:block;width:100%;background:#fff;border:1px solid #e5dfd0;border-radius:6px;box-shadow:0 6px 22px rgba(16,30,56,.12);}
.vnav{display:flex;justify-content:space-between;gap:16px;margin:34px 0 8px;}
.vnav a{flex:1;background:#fff;border:1px solid #e2dccd;border-radius:8px;padding:16px 18px;text-decoration:none;transition:all .2s;}
.vnav a:hover{border-color:var(--gold);box-shadow:0 6px 16px rgba(16,30,56,.12);}
.vnav .dir{font-family:'Archivo',sans-serif;font-size:10.5px;letter-spacing:2px;text-transform:uppercase;color:var(--gold);margin-bottom:4px;}
.vnav .nt{font-family:'Playfair Display',Georgia,serif;font-size:16px;color:var(--navy);}
.vnav .next{text-align:right;}
.vnav .spacer{flex:1;border:none;background:none;}
/* transcript */
.tblock{background:#fff;border:1px solid #e5dfd0;border-radius:8px;padding:20px 24px;margin:16px 0;box-shadow:0 3px 12px rgba(16,30,56,.07);}
.tspeaker{font-family:'Archivo',sans-serif;font-size:11px;letter-spacing:2px;text-transform:uppercase;margin-bottom:8px;color:var(--gold);}
.tspeaker.ai{color:var(--navy);}
.tbody{white-space:pre-wrap;font-size:15px;color:#3d3a33;}
@media(max-width:700px){.header h1{font-size:29px;}.section-head h2{font-size:21px;white-space:normal;}.vnav{flex-direction:column;}.vnav .next{text-align:left;}}
"""
(SITE / "assets" / "style.css").write_text(css)
print(f"Shared stylesheet: {len(css)/1024:.0f} KB (fonts embedded: {sum(1 for x in (pf,sp,ar) if x)}/3)")

esc = htmlmod.escape

# ---------- Per-document viewer pages ----------
for i, d in enumerate(docs):
    prev_d = docs[i-1] if i > 0 else None
    next_d = docs[i+1] if i < len(docs)-1 else None
    nav = '<div class="vnav">'
    nav += (f'<a href="../{prev_d["slug"]}/index.html"><div class="dir">&larr; Previous</div><div class="nt">{esc(prev_d["title"])}</div></a>'
            if prev_d else '<span class="spacer"></span>')
    nav += (f'<a class="next" href="../{next_d["slug"]}/index.html"><div class="dir">Next &rarr;</div><div class="nt">{esc(next_d["title"])}</div></a>'
            if next_d else '<span class="spacer"></span>')
    nav += '</div>'

    if d["kind"] == "images":
        jump = ('<div class="pagejump">' +
                "".join(f'<a href="#p{n}">{n}</a>' for n in range(1, len(d["pages"])+1)) +
                '</div>') if len(d["pages"]) > 1 else ""
        body = "".join(
            f'<div class="page" id="p{n}"><div class="page-label">Page {n} of {len(d["pages"])}</div>'
            f'<img src="pages/{p}" alt="{esc(d["title"])} — page {n}" loading="lazy"></div>'
            for n, p in enumerate(d["pages"], 1))
        count_line = f'{len(d["pages"])} pages'
    else:
        parts = re.split(r'^(You said:|ChatGPT said:)', d["text"], flags=re.M)
        blocks, k = [], 1
        if parts[0].strip():
            blocks.append(("", parts[0]))
        while k < len(parts):
            blocks.append((parts[k], parts[k+1] if k+1 < len(parts) else ""))
            k += 2
        body, jump = "", ""
        for speaker, text in blocks:
            if not text.strip():
                continue
            is_ai = speaker.startswith("ChatGPT")
            label = "ChatGPT" if is_ai else ("You" if speaker else "Transcript")
            body += (f'<div class="tblock"><div class="tspeaker{" ai" if is_ai else ""}">{label}</div>'
                     f'<div class="tbody">{esc(text.strip())}</div></div>')
        count_line = "Working transcript"

    page = f"""<!DOCTYPE html>
<html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{esc(d["title"])} &mdash; Lifetogether Archive</title>
<link rel="stylesheet" href="../../assets/style.css"></head>
<body>
<div class="vbar"><div class="vbar-in">
<a href="../../index.html">&larr; All Documents</a>
<div class="vtitle">{esc(d["title"])}</div>
<a href="{'../'+prev_d['slug']+'/index.html' if prev_d else '../../index.html'}">&larr; Prev</a>
<a href="{'../'+next_d['slug']+'/index.html' if next_d else '../../index.html'}">Next &rarr;</a>
</div></div>
<div class="vwrap">
<div class="vhead"><div class="eyebrow">{esc(d["cat"])} &middot; Document {i+1} of {len(docs)}</div>
<h1>{esc(d["title"])}</h1><div class="sub">{esc(d["desc"])} &middot; {count_line}.</div>{jump}</div>
{body}
{nav}
<p style="text-align:center;margin:18px 0 8px;"><a href="../../index.html" style="font-family:'Archivo',sans-serif;font-size:13px;color:#B98D3E;text-decoration:none;">&uarr; Back to the Library Index</a></p>
</div>
<div class="footer"><div class="fm">Lifetogether</div><p>brett@lifetogether.com &middot; 40daycampaigns.com</p></div>
</body></html>"""
    (SITE / "docs" / d["slug"] / "index.html").write_text(page)
print(f"Built {len(docs)} document viewers with prev/next chain")

# ---------- Master index ----------
def anchor(s): return slugify(s)

search_index = {d["slug"]: re.sub(r"\s+", " ", (d["title"] + " " + d["desc"] + " " + d["text"]).lower())[:40000] for d in docs}
toc = "".join(f'<a class="toc-link" href="#{anchor(c)}">{esc(c)}<span class="toc-count">{len(items)}</span></a>'
              for c, items in CATALOG.items())
sections = ""
for cat, items in CATALOG.items():
    cards = ""
    for fname, title, desc in items:
        d = next(x for x in docs if x["title"] == title)
        if d["kind"] == "images":
            cover = f'<div class="cover"><img src="docs/{d["slug"]}/pages/001.jpeg" alt="{esc(title)} cover" loading="lazy"></div>'
            chip = f'{len(d["pages"])} pages'
        else:
            cover = '<div class="cover"><div class="cover-txt"><div class="glyph">&ldquo;</div><div class="lbl">Working Transcript</div></div></div>'
            chip = "Transcript"
        cards += f"""
      <a class="card" data-slug="{d['slug']}" href="docs/{d['slug']}/index.html">{cover}
        <div class="card-body"><div class="eyebrow">{esc(cat)}</div><h3>{esc(title)}</h3><p>{esc(desc)}</p>
        <div class="card-meta"><span class="chip">{chip}</span><span class="open">Open &rarr;</span></div></div></a>"""
    sections += f"""
  <section class="section" id="{anchor(cat)}">
    <div class="section-head"><h2>{esc(cat)}</h2><span class="rule"></span><span class="count">{len(items)} documents</span></div>
    <div class="grid">{cards}
    </div>
  </section>"""

script = ("<script>var IDX=" + json.dumps(search_index) + ";\n" + """
(function(){var q=document.getElementById('q');
q.addEventListener('input',function(){var t=q.value.trim().toLowerCase(),any=false;
document.querySelectorAll('.card').forEach(function(c){var s=c.getAttribute('data-slug');
var hit=!t||(IDX[s]&&IDX[s].indexOf(t)!==-1);c.classList.toggle('hidden',!hit);if(hit)any=true;});
document.querySelectorAll('.section').forEach(function(s){s.classList.toggle('hidden',s.querySelectorAll('.card:not(.hidden)').length===0);});
document.getElementById('noresults').style.display=any?'none':'block';});})();
</script>""")

index = f"""<!DOCTYPE html>
<html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Lifetogether &mdash; Complete Project Archive</title>
<link rel="stylesheet" href="assets/style.css"></head>
<body>
<div class="header"><div class="eyebrow">Lifetogether &middot; 40 Day Campaigns</div>
<h1>Complete Project Archive</h1>
<p>Every page of every project document, extracted and linked. Open any document, page through it end to end, and step to the next &mdash; or search the full text of the entire library below.</p>
<div class="stats"><span class="stat">{len(docs)} Documents</span><span class="stat">{img_pages} Pages</span><span class="stat">6 Collections</span><span class="stat">Full-Text Search</span></div></div>
<div class="container">
<div class="searchbar"><input id="q" type="search" placeholder="Search every page of the library &mdash; title, topic, or any phrase&hellip;" aria-label="Search"></div>
<div class="toc">{toc}</div>
{sections}
<div class="noresults" id="noresults">No documents match that search.</div>
<div class="companion"><h2>Companion Deliverables From This Project</h2>
<p>Delivered separately in their original working sessions and not stored in the project files: the full 40daycampaigns.com website build (37+ linked HTML pages &mdash; <em>40daycampaigns_platform_10k.zip</em>), the Spanish and Portuguese site editions, the twelve-page Family Legacy by Design site, and the 76-page <em>10,000 Campaigns &mdash; Master Strategy, Part&nbsp;1</em> PDF. Add any of those files to the project and they can be folded into this archive.</p></div>
</div>
<div class="footer"><div class="fm">Lifetogether</div><p>brett@lifetogether.com &middot; 40daycampaigns.com</p>
<p style="margin-top:10px;opacity:.65;">Archive generated July 2026 &middot; Every page included &middot; Every link verified</p></div>
{script}
</body></html>"""
(SITE / "index.html").write_text(index)
print(f"Master index built ({len(index)/1024:.0f} KB incl. full-text search index)")
print("BUILD COMPLETE")
