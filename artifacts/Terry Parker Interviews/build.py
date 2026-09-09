import os, re, glob, markdown

OUT = "/mnt/user-data/outputs"

# title, subtitle, eyebrow, nav-section for each markdown source
META = {
 "The_Deep_Well_Family_Edition_Outline.md": ("The Deep Well", "Chapter outline and structure", "Manuscript · Family Edition"),
 "Deep_Well_Ch1_Ch5_Ch6.md": ("Chapters One, Five &amp; Six", "The First Thirty Feet · Before the Dry Year · Dig Your Own", "Manuscript · Drafted"),
 "Deep_Well_Ch3_Amos.md": ("Chapter Three", "Amos Carried the Water", "Manuscript · Drafted"),
 "Deep_Well_Ch4_and_40_Day_Outline.md": ("Chapter Four", "What He Never Said, and the forty-day companion", "Manuscript · Drafted"),
 "Advisor_Book_Ch7_The_Conversation_That_Costs_You.md": ("The Conversation That Costs You", "A Different Kind of Advisor · sample chapter", "Manuscript · Drafted"),
 "Different_Kind_of_Advisor_Three_Editions.md": ("A Different Kind of Advisor", "Six sessions, forty days, three editions", "Architecture"),
 "Two_Books_Instead_of_One_draft.md": ("Two Books Instead of One", "A fable about everything we try to keep", "Manuscript · Drafted"),
 "Deep_Well_Assessments_and_Tools.md": ("The Assessments", "Personal and family instruments, plus ten experiential tools", "Instrument · Print-Ready"),
 "Deep_Well_Toolbox_Expanded.md": ("The Toolbox", "Twenty-five tools, capture protocol, and journey catalog", "Instrument · Complete"),
 "Treasure_Principle_40_Day_Campaign_Proposal.md": ("The Treasure Principle · 40 Days", "A churchwide campaign proposal", "Proposal · Unsent"),
}

NAV = """<nav class="main">
      <div class="navitem"><span class="navlink">Begin</span><div class="mega"><h5>Start Here</h5>
        <a href="index.html">The Archive</a><a href="deep-well-brochure-navy.html">Find Your Starting Point</a><a href="deep-well-platform.html">Platform Overview</a></div></div>
      <div class="navitem"><span class="navlink">Manuscripts</span><div class="mega"><h5>Written Work</h5>
        <a href="The_Deep_Well_Family_Edition_Outline.html">The Deep Well · Outline</a><a href="Deep_Well_Ch1_Ch5_Ch6.html">Chapters One, Five &amp; Six</a><a href="Deep_Well_Ch3_Amos.html">Chapter Three · Amos</a><a href="Deep_Well_Ch4_and_40_Day_Outline.html">Chapter Four &amp; Forty Days</a><a href="Two_Books_Instead_of_One_draft.html">Two Books Instead of One</a></div></div>
      <div class="navitem"><span class="navlink">Advisor</span><div class="mega"><h5>Practitioner Edition</h5>
        <a href="Different_Kind_of_Advisor_Three_Editions.html">Three Editions</a><a href="Advisor_Book_Ch7_The_Conversation_That_Costs_You.html">The Conversation That Costs You</a><a href="case-studies-and-voices.html">Case Studies &amp; Voices</a></div></div>
      <div class="navitem"><span class="navlink">Instruments</span><div class="mega"><h5>Diagnostics &amp; Tools</h5>
        <a href="Deep_Well_Assessments_and_Tools.html">The Assessments</a><a href="Deep_Well_Toolbox_Expanded.html">The Toolbox</a><a href="family-library-interactive.html">Take the Assessment</a><a href="family-library.html">The Family Library</a></div></div>
      <div class="navitem"><span class="navlink">Operations</span><div class="mega"><h5>Build &amp; Partners</h5>
        <a href="Treasure_Principle_40_Day_Campaign_Proposal.html">Treasure Principle Proposal</a><a href="video-access-golive.html">Video, Access &amp; Go-Live</a><a href="deep-well-blue.html">Blue Prototype</a></div></div>
    </nav>"""

CSS = """:root{--ink:#080e16;--navy:#0b1726;--navy-2:#0e1d30;--panel:#132439;--panel-2:#16293f;--gold:#c9a35c;--gold-bright:#e3c186;--cream:#ece7d8;--muted:#8b94a5;--muted-dim:#5f6a7c;--ivory:#f4efe3;--line:rgba(255,255,255,.08);--line-gold:rgba(201,163,92,.22);--maxw:1280px}
*{box-sizing:border-box}html{scroll-behavior:smooth}
body{margin:0;background:var(--navy);color:var(--cream);font-family:'Spectral',Georgia,serif;font-size:18px;line-height:1.68;-webkit-font-smoothing:antialiased}
.wrap{max-width:var(--maxw);margin:0 auto;padding:0 32px}
.read{max-width:760px;margin:0 auto;padding:0 32px}
header{position:sticky;top:0;z-index:300;height:78px;background:rgba(11,23,38,.86);backdrop-filter:blur(14px);border-bottom:1px solid var(--line-gold)}
.hdr{display:flex;align-items:center;justify-content:space-between;height:78px;gap:24px}
.brand{font-family:'Playfair Display',serif;font-weight:800;font-size:20px;letter-spacing:-.01em;color:var(--cream);text-decoration:none}
.brand span{color:var(--gold)}
nav.main{display:flex;align-items:center;gap:30px}
.navitem{position:relative}
.navlink{font-family:'Archivo',sans-serif;font-size:11px;font-weight:600;letter-spacing:.18em;text-transform:uppercase;color:var(--muted);text-decoration:none;cursor:pointer;padding:28px 0;display:inline-block;transition:color .18s ease}
.navitem:hover .navlink{color:var(--gold-bright)}
.mega{position:absolute;top:70px;left:-24px;min-width:288px;background:var(--panel);border:1px solid var(--line-gold);border-radius:10px;padding:22px 24px;opacity:0;visibility:hidden;transform:translateY(-6px);transition:opacity .18s ease,transform .18s ease,visibility .18s}
.navitem:hover .mega{opacity:1;visibility:visible;transform:translateY(0)}
.mega h5{font-family:'Archivo',sans-serif;font-size:10.5px;font-weight:700;letter-spacing:.18em;text-transform:uppercase;color:var(--gold);margin:0 0 12px}
.mega a{display:block;color:var(--cream);text-decoration:none;font-size:15px;padding:6px 0;opacity:.82}
.mega a:hover{color:var(--gold-bright);opacity:1}
.btn{font-family:'Archivo',sans-serif;font-size:13px;font-weight:600;letter-spacing:.06em;text-transform:uppercase;border-radius:3px;background:var(--gold);color:var(--ink);border:none;padding:13px 22px;text-decoration:none;display:inline-block;cursor:pointer;transition:background .18s ease}
.btn:hover{background:var(--gold-bright)}
.btn.ghost{background:transparent;color:var(--gold);border:1px solid var(--line-gold)}
.btn.ghost:hover{background:rgba(201,163,92,.06);color:var(--gold-bright)}
.hero{padding:96px 0 76px;background:radial-gradient(80% 120% at 78% -10%, rgba(201,163,92,.12), transparent 55%),linear-gradient(180deg,var(--navy-2),var(--navy));border-bottom:1px solid var(--line-gold)}
.eyebrow{font-family:'Archivo',sans-serif;font-size:11px;font-weight:600;letter-spacing:.22em;text-transform:uppercase;color:var(--gold);margin:0 0 20px}
.hero h1{font-family:'Playfair Display',serif;font-weight:800;font-size:clamp(40px,5.4vw,68px);line-height:1.04;letter-spacing:-.015em;color:var(--cream);margin:0 0 22px}
.hero .sub{font-family:'Playfair Display',serif;font-style:italic;font-size:22px;color:var(--gold-bright);margin:0}
article{padding:80px 0 100px}
article h1{font-family:'Playfair Display',serif;font-weight:800;font-size:38px;line-height:1.1;letter-spacing:-.015em;color:var(--cream);margin:64px 0 24px}
article h2{font-family:'Playfair Display',serif;font-weight:700;font-size:30px;line-height:1.16;letter-spacing:-.012em;color:var(--cream);margin:56px 0 20px;padding-top:36px;border-top:1px solid var(--line-gold)}
article h2:first-child{margin-top:0;padding-top:0;border-top:none}
article h3{font-family:'Playfair Display',serif;font-weight:700;font-size:23px;line-height:1.24;color:var(--cream);margin:44px 0 14px}
article h4{font-family:'Archivo',sans-serif;font-size:11px;font-weight:600;letter-spacing:.2em;text-transform:uppercase;color:var(--gold);margin:38px 0 14px}
article p{margin:0 0 22px;opacity:.92}
article em{color:var(--cream)}
article strong{color:var(--cream);font-weight:600}
article a{color:var(--gold-bright);text-decoration:none;border-bottom:1px solid var(--line-gold)}
article ul,article ol{padding-left:22px;margin:0 0 24px}
article li{margin-bottom:11px;opacity:.92}
article li::marker{color:var(--gold)}
article hr{border:none;height:1px;background:var(--line-gold);margin:52px 0}
article blockquote{font-family:'Playfair Display',serif;font-style:italic;font-weight:500;font-size:23px;line-height:1.44;color:var(--gold-bright);background:rgba(201,163,92,.06);border-left:2px solid var(--gold);padding:26px 30px;margin:36px 0}
article blockquote p{margin:0;opacity:1}
article table{width:100%;border-collapse:collapse;margin:8px 0 32px;font-size:16px}
article th{font-family:'Archivo',sans-serif;font-size:10.5px;font-weight:700;letter-spacing:.18em;text-transform:uppercase;color:var(--gold);text-align:left;padding:0 16px 13px 0;border-bottom:1px solid var(--line-gold)}
article td{padding:14px 16px 14px 0;border-bottom:1px solid var(--line);vertical-align:top;opacity:.9}
article code{font-family:'Archivo',sans-serif;font-size:14px;color:var(--gold-bright);background:rgba(201,163,92,.06);padding:2px 6px;border-radius:3px}
.pager{border-top:1px solid var(--line-gold);background:var(--ink)}
.pgrid2{display:grid;gap:1px;background:var(--line-gold);grid-template-columns:1fr 1fr}
.pgrid2 a{background:var(--panel);padding:34px 32px;text-decoration:none;color:inherit;transition:background .16s}
.pgrid2 a:hover{background:var(--panel-2)}
.pgrid2 .dirn{font-family:'Archivo',sans-serif;font-size:10px;font-weight:600;letter-spacing:.18em;text-transform:uppercase;color:var(--gold);margin-bottom:10px}
.pgrid2 .ttl{font-family:'Playfair Display',serif;font-weight:700;font-size:21px;color:var(--cream)}
.pgrid2 a.nxt{text-align:right}
footer{background:var(--ink);border-top:1px solid var(--line-gold);padding:56px 0 44px}
footer p{font-size:14px;color:var(--muted);margin:0 0 12px}
@media(max-width:900px){nav.main{display:none}.wrap,.read{padding:0 22px}article{padding:56px 0 70px}.pgrid2{grid-template-columns:1fr}.pgrid2 a.nxt{text-align:left}}"""

HEAD = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title} — LifeTogether</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,500;0,700;0,800;0,900;1,500;1,600&family=Spectral:ital,wght@0,400;0,500;0,600;1,400&family=Archivo:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>{css}</style>
</head>
<body>
<header><div class="wrap hdr">
  <a class="brand" href="index.html">Life<span>together</span></a>
  {nav}
  <a class="btn ghost" href="index.html">The Archive</a>
</div></header>
<div class="hero"><div class="read">
  <p class="eyebrow">{eyebrow}</p>
  <h1>{title}</h1>
  <p class="sub">{sub}</p>
</div></div>
<article><div class="read">
{body}
</div></article>
<div class="pager"><div class="wrap"><div class="pgrid2">
  <a href="{prev_href}"><div class="dirn">Previous</div><div class="ttl">{prev_title}</div></a>
  <a class="nxt" href="{next_href}"><div class="dirn">Next</div><div class="ttl">{next_title}</div></a>
</div></div></div>
<footer><div class="wrap">
  <p style="font-family:'Playfair Display',serif;font-size:19px;color:var(--cream);margin-bottom:18px">LifeTogether &nbsp;·&nbsp; San Juan Capistrano</p>
  <p>Working document. Status language is deliberate: concept, exploratory, proposed, developing, pilot, active. Any quotation attributed to a named person is a draft written by us and approved by no one. Case studies are composites containing no real client detail. Third-party titles are unlicensed. Nothing here is tax or legal advice.</p>
</div></footer>
</body>
</html>"""

# reading order for prev/next
ORDER = [
 ("index.html", "The Archive"),
 ("deep-well-brochure-navy.html", "Find Your Starting Point"),
 ("deep-well-platform.html", "The Platform Overview"),
 ("The_Deep_Well_Family_Edition_Outline.html", "The Deep Well · Outline"),
 ("Deep_Well_Ch1_Ch5_Ch6.html", "Chapters One, Five &amp; Six"),
 ("Deep_Well_Ch3_Amos.html", "Chapter Three · Amos"),
 ("Deep_Well_Ch4_and_40_Day_Outline.html", "Chapter Four &amp; Forty Days"),
 ("Different_Kind_of_Advisor_Three_Editions.html", "A Different Kind of Advisor"),
 ("Advisor_Book_Ch7_The_Conversation_That_Costs_You.html", "The Conversation That Costs You"),
 ("Two_Books_Instead_of_One_draft.html", "Two Books Instead of One"),
 ("Deep_Well_Assessments_and_Tools.html", "The Assessments"),
 ("Deep_Well_Toolbox_Expanded.html", "The Toolbox"),
 ("Treasure_Principle_40_Day_Campaign_Proposal.html", "Treasure Principle · 40 Days"),
 ("family-library.html", "The Family Library"),
 ("family-library-interactive.html", "The Interactive Library"),
 ("case-studies-and-voices.html", "Case Studies &amp; Voices"),
 ("video-access-golive.html", "Video, Access &amp; Go-Live"),
 ("deep-well-blue.html", "Blue Prototype"),
]
IDX = {h: i for i, (h, t) in enumerate(ORDER)}

md = markdown.Markdown(extensions=["tables", "attr_list", "sane_lists"])

built = []
for src, (title, sub, eyebrow) in META.items():
    path = os.path.join(OUT, src)
    if not os.path.exists(path):
        print("MISSING", src); continue
    text = open(path, encoding="utf-8").read()
    # drop the leading H1 and the following italic subtitle line; the hero carries them
    lines = text.split("\n")
    while lines and (lines[0].strip() == "" or lines[0].startswith("# ") or lines[0].startswith("### ") or lines[0].startswith("*")):
        if lines[0].startswith("### ") or lines[0].startswith("# ") or lines[0].startswith("*") or lines[0].strip() == "":
            lines.pop(0)
        else:
            break
    body = md.reset().convert("\n".join(lines))
    out_name = src.replace(".md", ".html")
    i = IDX.get(out_name, 0)
    p = ORDER[i - 1] if i > 0 else ORDER[-1]
    n = ORDER[i + 1] if i < len(ORDER) - 1 else ORDER[0]
    html = HEAD.format(title=title, sub=sub, eyebrow=eyebrow, css=CSS, nav=NAV,
                       body=body, prev_href=p[0], prev_title=p[1],
                       next_href=n[0], next_title=n[1])
    open(os.path.join(OUT, out_name), "w", encoding="utf-8").write(html)
    built.append(out_name)

print("built", len(built), "reading pages")
for b in built:
    print("  ", b)
