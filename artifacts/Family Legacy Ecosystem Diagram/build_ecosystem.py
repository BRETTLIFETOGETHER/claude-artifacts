#!/usr/bin/env python3
"""Family Legacy Ecosystem Diagram generator.
Reference-styled against Print_version-FLBD_Report.pdf:
deep forest green, gold + terracotta accents, tree logo, Poppins headings,
soft rounded cards, angled green shapes. Self-contained HTML w/ embedded fonts.
"""
import base64, pathlib

FONTS = pathlib.Path("/home/claude/fonts")

def b64(name):
    return base64.b64encode((FONTS / name).read_bytes()).decode()

poppins_b = b64("Poppins-Bold.ttf")
poppins_sb = b64("Poppins-SemiBold.ttf")
poppins_m = b64("Poppins-Medium.ttf")
inter = b64("Inter.ttf")

# ---- Palette (sampled from the report) ----
INK      = "#1d2622"
FOREST   = "#0e3a2d"   # deep header / platform band
FOREST2  = "#15503c"
LEAF     = "#4a7c2f"   # olive/leaf green accent shapes
GOLD     = "#f5a623"   # primary accent
BRICK    = "#a04e3c"   # secondary accent / pill labels
CREAM    = "#f7f5f0"
CARD     = "#ffffff"
MUTE     = "#5d6b62"

# ---- Tree logo (white) — simple stylized family tree ----
def tree_logo(color="#ffffff", size=58):
    sw = 5
    branches = [
        "M50 60 C 46 48, 40 42, 30 36",
        "M50 60 C 54 48, 60 42, 70 36",
        "M50 56 C 48 46, 44 40, 36 50",
        "M50 56 C 52 46, 56 40, 64 50",
        "M50 52 C 50 42, 50 36, 50 26",
    ]
    paths = "".join(
        f'<path d="{d}" stroke="{color}" stroke-width="{sw}" stroke-linecap="round" fill="none"/>'
        for d in branches)
    return f'''<svg width="{size}" height="{size}" viewBox="0 0 100 100" fill="none" xmlns="http://www.w3.org/2000/svg">
      <g fill="{color}">
        <path d="M46 58 q4 -6 8 0 v28 a4 4 0 0 1 -8 0 z"/>
        {paths}
        <circle cx="50" cy="22" r="10"/>
        <circle cx="30" cy="33" r="8"/><circle cx="70" cy="33" r="8"/>
        <circle cx="34" cy="50" r="7"/><circle cx="66" cy="50" r="7"/>
        <circle cx="22" cy="46" r="6"/><circle cx="78" cy="46" r="6"/>
      </g>
    </svg>'''

def chip(text):
    return f'<span class="chip">{text}</span>'

# ---- Content data ----
audiences = [
    ("Legacy Families", "M16 11c1.66 0 3-1.34 3-3s-1.34-3-3-3-3 1.34-3 3 1.34 3 3 3zm-8 0c1.66 0 3-1.34 3-3S9.66 5 8 5 5 6.34 5 8s1.34 3 3 3zm0 2c-2.33 0-7 1.17-7 3.5V19h14v-2.5c0-2.33-4.67-3.5-7-3.5zm8 0c-.29 0-.62.02-.97.05 1.16.84 1.97 1.97 1.97 3.45V19h6v-2.5c0-2.33-4.67-3.5-7-3.5z",
     ["High-capacity families", "Multi-generational families",
      "Focused on stewardship, values,", "generosity &amp; succession"]),
    ("Christian Advisors", "M12 1L3 5v6c0 5.55 3.84 10.74 9 12 5.16-1.26 9-6.45 9-12V5l-9-4z",
     ["Wealth advisors &amp; financial planners", "Family office advisors",
      "Estate planners", "Professionals guiding families", "through legacy decisions"]),
    ("Affinity Groups", "M12 12c2.21 0 4-1.79 4-4s-1.79-4-4-4-4 1.79-4 4 1.79 4 4 4zm0 2c-2.67 0-8 1.34-8 4v2h16v-2c0-2.66-5.33-4-8-4z",
     ["Business Owners &middot; Attorneys &middot; CPAs", "Executive Coaches &middot; Counselors",
      "Donors &middot; Nonprofit Leaders", "Pastors &middot; Ministry Leaders &middot; Family Offices"]),
]

foundations = ["6 Core Coaching Series", "6 Family Series", "Family Legacy Curriculum",
               "Family Legacy Devotionals", "Family Legacy Workshops"]
editions = ["Business Owner", "Attorney", "CPA", "Advisor",
            "Family Office", "Executive Coach", "Pastor", "Counselor"]
libraries = ["Family Legacy", "Next Generations", "Purpose at Work", "Stewardship",
             "Generosity", "Financial Wisdom", "Multiplication", "Kingdom Impact"]
formats = ["6-Session Study", "4-Session Study", "21-Day Experience", "30-Day Experience",
           "40-Day Experience", "Workshop", "Devotional", "Family Conversation Guide"]
tools = ["Legacy Letters", "Family Covenant", "Family Meeting Guides",
         "Conflict Resolution Tools", "Gen 2 Conversation Guides", "Facilitation Scripts"]

def chips(items): return "".join(chip(i) for i in items)

audience_cards = ""
for name, icon, bullets in audiences:
    blist = "".join(f"<li>{b}</li>" for b in bullets)
    audience_cards += f'''
      <div class="aud-card">
        <div class="aud-ic"><svg viewBox="0 0 24 24" width="26" height="26"><path d="{icon}"/></svg></div>
        <h3>{name}</h3>
        <ul>{blist}</ul>
      </div>'''

HTML = f'''<!doctype html><html lang="en"><head><meta charset="utf-8">
<style>
@font-face{{font-family:'Poppins';src:url(data:font/ttf;base64,{poppins_b}) format('truetype');font-weight:700;}}
@font-face{{font-family:'Poppins';src:url(data:font/ttf;base64,{poppins_sb}) format('truetype');font-weight:600;}}
@font-face{{font-family:'Poppins';src:url(data:font/ttf;base64,{poppins_m}) format('truetype');font-weight:500;}}
@font-face{{font-family:'Inter';src:url(data:font/ttf;base64,{inter}) format('truetype');font-weight:400 700;}}
*{{margin:0;padding:0;box-sizing:border-box;}}
:root{{--ink:{INK};--forest:{FOREST};--forest2:{FOREST2};--leaf:{LEAF};--gold:{GOLD};--brick:{BRICK};--cream:{CREAM};--mute:{MUTE};}}
html,body{{background:#dfe3df;font-family:'Inter',sans-serif;color:var(--ink);-webkit-font-smoothing:antialiased;}}
.page{{width:1400px;margin:0 auto;background:var(--cream);position:relative;overflow:hidden;}}
h1,h2,h3,.font-p{{font-family:'Poppins',sans-serif;}}

/* ---------- HEADER ---------- */
.hdr{{position:relative;background:var(--forest);padding:34px 60px 40px;overflow:hidden;}}
.hdr:after{{content:"";position:absolute;top:0;right:-120px;width:520px;height:200%;
  background:var(--leaf);transform:skewX(-20deg);opacity:.30;}}
.hdr:before{{content:"";position:absolute;bottom:-60px;right:120px;width:360px;height:200%;
  background:var(--forest2);transform:skewX(-20deg);opacity:.55;}}
.brandrow{{display:flex;align-items:center;gap:14px;position:relative;z-index:2;}}
.brandrow .bn{{font-family:'Poppins';font-weight:700;color:#fff;line-height:.98;font-size:19px;}}
.brandrow .bn span{{font-weight:500;font-size:13px;color:#cfe0d4;letter-spacing:.06em;display:block;}}
.hdr h1{{position:relative;z-index:2;color:#fff;font-size:50px;font-weight:700;line-height:1.02;margin-top:20px;letter-spacing:-.5px;}}
.hdr .sub{{position:relative;z-index:2;color:#e7efe8;font-size:17px;margin-top:12px;max-width:760px;font-weight:400;}}
.hdr .sub b{{color:var(--gold);font-weight:600;}}
.goldrule{{width:88px;height:5px;background:var(--gold);border-radius:3px;margin-top:18px;position:relative;z-index:2;}}

.body{{padding:38px 60px 0;}}

/* ---------- section label ---------- */
.seclabel{{display:flex;align-items:center;gap:13px;margin:4px 0 20px;}}
.seclabel .sq{{width:18px;height:18px;background:var(--gold);border-radius:4px;flex:none;}}
.seclabel h2{{font-size:25px;font-weight:700;color:var(--forest);letter-spacing:-.3px;}}
.seclabel .tag{{margin-left:auto;font-size:12.5px;color:var(--mute);font-weight:500;font-family:'Poppins';
  background:#ece9e1;padding:6px 14px;border-radius:20px;}}

/* ---------- audience cards ---------- */
.aud-grid{{display:grid;grid-template-columns:repeat(3,1fr);gap:22px;}}
.aud-card{{background:var(--card);border-radius:18px;padding:24px 24px 22px;
  box-shadow:0 10px 26px rgba(14,58,45,.09);border-top:5px solid var(--leaf);}}
.aud-card .aud-ic{{width:50px;height:50px;border-radius:13px;background:#eef3ec;
  display:flex;align-items:center;justify-content:center;margin-bottom:14px;}}
.aud-card .aud-ic svg{{fill:var(--forest);}}
.aud-card h3{{font-size:20px;font-weight:600;color:var(--forest);margin-bottom:11px;}}
.aud-card ul{{list-style:none;}}
.aud-card li{{font-size:14px;color:var(--ink);line-height:1.55;padding-left:18px;position:relative;}}
.aud-card li:before{{content:"";position:absolute;left:0;top:8px;width:7px;height:7px;border-radius:50%;background:var(--gold);}}

/* ---------- flow connector ---------- */
.flow{{display:flex;flex-direction:column;align-items:center;margin:22px 0 8px;}}
.flow .ftxt{{font-family:'Poppins';font-weight:600;font-size:13px;letter-spacing:.12em;
  text-transform:uppercase;color:var(--brick);margin-bottom:6px;}}
.flow .arrow{{width:0;height:0;border-left:13px solid transparent;border-right:13px solid transparent;
  border-top:15px solid var(--gold);}}
.flow .stem{{width:3px;height:14px;background:var(--gold);}}

/* ---------- platform band ---------- */
.platform{{position:relative;background:var(--forest);border-radius:22px;padding:30px 36px 32px;
  overflow:hidden;box-shadow:0 16px 34px rgba(14,58,45,.22);}}
.platform:after{{content:"";position:absolute;top:-40px;left:-60px;width:300px;height:200%;
  background:var(--leaf);opacity:.16;transform:skewX(-18deg);}}
.platform .phead{{display:flex;align-items:center;gap:14px;position:relative;z-index:2;margin-bottom:6px;}}
.platform .phead .pl-ic{{width:46px;height:46px;border-radius:12px;background:rgba(245,166,35,.18);
  display:flex;align-items:center;justify-content:center;}}
.platform h2{{color:#fff;font-size:26px;font-weight:700;}}
.platform .psub{{color:#bcd2c2;font-size:14px;position:relative;z-index:2;margin-bottom:20px;}}
.lanes{{display:grid;grid-template-columns:repeat(4,1fr);gap:16px;position:relative;z-index:2;}}
.lane{{background:rgba(255,255,255,.07);border:1px solid rgba(255,255,255,.14);border-radius:13px;padding:15px 16px;}}
.lane .lh{{font-family:'Poppins';font-weight:600;color:var(--gold);font-size:14px;margin-bottom:5px;}}
.lane p{{color:#e6efe8;font-size:13px;line-height:1.5;}}
.lane.add{{background:rgba(245,166,35,.14);border-color:rgba(245,166,35,.45);}}
.lane.add .lh{{color:#ffd089;}}
.infinity{{font-family:'Poppins';font-weight:700;}}

/* ---------- engine ---------- */
.engine{{background:var(--card);border-radius:22px;padding:28px 30px 26px;
  box-shadow:0 10px 26px rgba(14,58,45,.10);border:1px solid #e8e4da;}}
.mult{{display:grid;grid-template-columns:1fr 30px 1fr 30px 1fr 38px 1fr;align-items:stretch;gap:0;}}
.op{{display:flex;align-items:center;justify-content:center;font-family:'Poppins';font-weight:700;
  font-size:30px;color:var(--gold);}}
.eblock{{background:#f5f3ec;border-radius:15px;padding:16px 16px 15px;border-top:4px solid var(--forest);
  display:flex;flex-direction:column;}}
.eblock.out{{border-top-color:var(--brick);background:#faf4f1;}}
.eblock .ehead{{font-family:'Poppins';font-weight:600;font-size:15.5px;color:var(--forest);margin-bottom:3px;}}
.eblock.out .ehead{{color:var(--brick);}}
.eblock .ekick{{font-size:11px;letter-spacing:.08em;text-transform:uppercase;color:var(--mute);
  font-family:'Poppins';font-weight:600;margin-bottom:11px;}}
.chipwrap{{display:flex;flex-wrap:wrap;gap:6px;}}
.chip{{background:#fff;border:1px solid #ddd7ca;border-radius:7px;padding:5px 9px;font-size:11.5px;
  color:var(--ink);font-weight:500;line-height:1.2;}}
.eblock.out .chip{{border-color:#e7cbc1;}}

.toolsbar{{margin-top:18px;background:linear-gradient(90deg,#143d31,#0e3a2d);border-radius:15px;
  padding:17px 22px;display:flex;align-items:center;gap:22px;position:relative;overflow:hidden;}}
.toolsbar:after{{content:"";position:absolute;right:-40px;top:0;width:200px;height:300%;
  background:var(--gold);opacity:.10;transform:skewX(-18deg);}}
.toolsbar .tl-label{{flex:none;max-width:185px;position:relative;z-index:2;}}
.toolsbar .tl-label .h{{font-family:'Poppins';font-weight:700;color:#fff;font-size:17px;line-height:1.1;}}
.toolsbar .tl-label .k{{color:var(--gold);font-size:11px;font-family:'Poppins';font-weight:600;
  letter-spacing:.07em;text-transform:uppercase;margin-top:3px;}}
.toolsbar .chipwrap{{position:relative;z-index:2;}}
.toolsbar .chip{{background:rgba(255,255,255,.10);border-color:rgba(255,255,255,.22);color:#eef4ef;}}

.scalenote{{display:flex;align-items:center;gap:10px;margin-top:14px;justify-content:center;
  font-family:'Poppins';font-weight:600;font-size:13.5px;color:var(--forest);}}
.scalenote .pill{{background:var(--gold);color:#5a3a00;border-radius:20px;padding:4px 13px;font-size:12.5px;}}

/* ---------- equation strip ---------- */
.eq{{margin:26px 0 0;text-align:center;font-family:'Poppins';font-weight:600;color:var(--forest2);
  font-size:15px;line-height:1.7;}}
.eq b{{color:var(--brick);font-weight:700;}}
.eq .x{{color:var(--gold);font-weight:700;}}

/* ---------- footer ---------- */
.foot{{margin-top:30px;background:var(--forest);padding:20px 60px;display:flex;align-items:center;
  justify-content:space-between;}}
.foot .pres{{color:#cfe0d4;font-size:13px;font-family:'Poppins';font-weight:500;}}
.foot .pres b{{color:#fff;font-weight:700;}}
.foot .lt{{color:#fff;font-family:'Poppins';font-weight:700;font-size:18px;}}
.foot .lt .t{{color:var(--gold);}}
</style></head>
<body>
<div class="page">

  <!-- HEADER -->
  <div class="hdr">
    <div class="brandrow">{tree_logo()}<div class="bn">Family Legacy<br><span>BY DESIGN</span></div></div>
    <h1>The Family Legacy Ecosystem</h1>
    <div class="sub">From a library of books &amp; workshops into a <b>scalable content ecosystem</b> and <b>membership platform</b> &mdash; one engine serving families, advisors, and the communities around them.</div>
    <div class="goldrule"></div>
  </div>

  <div class="body">

    <!-- AUDIENCES -->
    <div class="seclabel"><div class="sq"></div><h2>Who the Ecosystem Serves</h2>
      <div class="tag">Three primary audiences</div></div>
    <div class="aud-grid">{audience_cards}</div>

    <div class="flow"><div class="ftxt">All access the ecosystem through</div><div class="stem"></div><div class="arrow"></div></div>

    <!-- PLATFORM -->
    <div class="platform">
      <div class="phead">
        <div class="pl-ic"><svg viewBox="0 0 24 24" width="24" height="24" fill="{GOLD}"><path d="M4 6h16v2H4zm0 5h16v2H4zm0 5h16v2H4z"/></svg></div>
        <h2>The Membership Platform</h2>
      </div>
      <div class="psub">The unifying hub where every audience accesses the right resources &mdash; and where the catalog never stops growing.</div>
      <div class="lanes">
        <div class="lane"><div class="lh">Legacy Families</div><p>Access curriculum, devotionals, workshops &amp; conversation guides.</p></div>
        <div class="lane"><div class="lh">Christian Advisors</div><p>Access advisor tools, facilitation resources &amp; certification.</p></div>
        <div class="lane"><div class="lh">Affinity Groups</div><p>Access specialized editions built for their profession.</p></div>
        <div class="lane add"><div class="lh"><span class="infinity">&infin;</span> Always Expanding</div><p>New campaign libraries &amp; editions added continually.</p></div>
      </div>
    </div>

    <div class="flow"><div class="ftxt">Continuously powered by</div><div class="stem"></div><div class="arrow"></div></div>

    <!-- ENGINE -->
    <div class="seclabel"><div class="sq"></div><h2>The Content Engine</h2>
      <div class="tag">How a fixed core scales into an endless catalog</div></div>

    <div class="engine">
      <div class="mult">
        <div class="eblock">
          <div class="ehead">Family Legacy Foundations</div>
          <div class="ekick">The Core IP</div>
          <div class="chipwrap">{chips(foundations)}</div>
        </div>
        <div class="op">&times;</div>
        <div class="eblock">
          <div class="ehead">Affinity Editions</div>
          <div class="ekick">Tailored by audience</div>
          <div class="chipwrap">{chips(editions)}</div>
        </div>
        <div class="op">&times;</div>
        <div class="eblock">
          <div class="ehead">Campaign Libraries</div>
          <div class="ekick">Tailored by theme</div>
          <div class="chipwrap">{chips(libraries)}</div>
        </div>
        <div class="op">&rarr;</div>
        <div class="eblock out">
          <div class="ehead">Content Formats</div>
          <div class="ekick">Delivered as</div>
          <div class="chipwrap">{chips(formats)}</div>
        </div>
      </div>

      <div class="toolsbar">
        <div class="tl-label"><div class="h">Advisor Tools</div><div class="k">Professional &amp; certification layer</div></div>
        <div class="chipwrap">{chips(tools)}</div>
      </div>

      <div class="scalenote"><span class="pill">Scalability</span>
        A handful of foundations &times; editions &times; libraries &times; formats = thousands of tailored resources from one body of work.</div>
    </div>

    <div class="eq">
      <b>Foundations</b> <span class="x">&times;</span> <b>Affinity Editions</b> <span class="x">&times;</span> <b>Campaign Libraries</b> <span class="x">&times;</span> <b>Formats</b> <span class="x">&rarr;</span> delivered through <b>one membership platform</b> to <b>families, advisors &amp; affinity groups.</b>
    </div>
  </div>

  <!-- FOOTER -->
  <div class="foot">
    <div class="pres">Family Legacy by Design &nbsp;&bull;&nbsp; A long-term vision for a scalable legacy content ecosystem</div>
    <div class="pres">Presented by <span class="lt">life<span class="t">together</span></span></div>
  </div>

</div>
</body></html>'''

out = pathlib.Path("/home/claude/family_legacy_ecosystem.html")
out.write_text(HTML, encoding="utf-8")
print("wrote", out, len(HTML), "bytes")
