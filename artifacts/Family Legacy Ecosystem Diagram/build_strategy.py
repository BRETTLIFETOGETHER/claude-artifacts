# -*- coding: utf-8 -*-
import base64, pathlib
from fl_content import (AUDIENCE_VALUE, CATEGORIES, AFFINITIES, FORMATS,
                        CAMPAIGNS, CATALOG_MORE)

F = pathlib.Path("/home/claude/fonts")
def b64(n): return base64.b64encode((F/n).read_bytes()).decode()
poppins_b, poppins_sb, poppins_m, inter = b64("Poppins-Bold.ttf"), b64("Poppins-SemiBold.ttf"), b64("Poppins-Medium.ttf"), b64("Inter.ttf")

INK, FOREST, FOREST2, LEAF, GOLD, BRICK, CREAM, MUTE = (
    "#1d2622", "#0e3a2d", "#15503c", "#4a7c2f", "#f5a623", "#a04e3c", "#f7f5f0", "#5d6b62")

def tree(color="#ffffff", size=56):
    sw = 5
    br = ["M50 60 C 46 48, 40 42, 30 36","M50 60 C 54 48, 60 42, 70 36",
          "M50 56 C 48 46, 44 40, 36 50","M50 56 C 52 46, 56 40, 64 50","M50 52 C 50 42, 50 36, 50 26"]
    p = "".join(f'<path d="{d}" stroke="{color}" stroke-width="{sw}" stroke-linecap="round" fill="none"/>' for d in br)
    return f'''<svg width="{size}" height="{size}" viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg"><g fill="{color}">
      <path d="M46 58 q4 -6 8 0 v28 a4 4 0 0 1 -8 0 z"/>{p}
      <circle cx="50" cy="22" r="10"/><circle cx="30" cy="33" r="8"/><circle cx="70" cy="33" r="8"/>
      <circle cx="34" cy="50" r="7"/><circle cx="66" cy="50" r="7"/><circle cx="22" cy="46" r="6"/><circle cx="78" cy="46" r="6"/>
    </g></svg>'''

def brand(small=False):
    sz = 40 if small else 52
    fs = 15 if small else 18
    return f'''<div class="brand">{tree(size=sz)}<div class="bn">Family Legacy<span>BY DESIGN</span></div></div>'''

def label(txt, tag=""):
    t = f'<div class="tag">{tag}</div>' if tag else ''
    return f'<div class="seclabel"><div class="sq"></div><h2>{txt}</h2>{t}</div>'

PAGES = []

# ---------- 1. COVER ----------
PAGES.append(f'''<section class="sheet cover">
  <div class="cv-shape"></div><div class="cv-shape2"></div>
  <div class="cv-top">{brand()}<div class="cv-pres">A STRATEGIC OPPORTUNITY BRIEF</div></div>
  <div class="cv-mid">
    <div class="cv-kick">THE FAMILY LEGACY CATEGORY</div>
    <h1>From a campaign library<br>into a scalable<br><em>legacy ecosystem.</em></h1>
    <div class="cv-rule"></div>
    <p>How one body of work \u2014 grounded in Tom Conway\u2019s Multi-Generational Legacy Coaching Process \u2014
       becomes a multiplying platform serving families, the advisors who guide them, and the communities around them.</p>
  </div>
  <div class="cv-foot">
    <div class="cv-stats">
      <div class="cv-stat"><b>$124T</b><span>The Great Wealth Transfer through 2048</span></div>
      <div class="cv-stat"><b>10+</b><span>Flagship campaigns, with a deep catalog beneath</span></div>
      <div class="cv-stat"><b>8 \u00d7 8</b><span>Topics \u00d7 audiences = exponential reach</span></div>
    </div>
    <div class="cv-by">Prepared for ministry partners, advisors &amp; donors &nbsp;\u00b7&nbsp; Presented by <b>lifetogether</b></div>
  </div>
</section>''')

# ---------- 2. THE OPPORTUNITY ----------
PAGES.append(f'''<section class="sheet">
  {label("The Opportunity","Why now")}
  <div class="lead-band">
    <div class="lead-q">\u201cThe largest transfer of wealth in history is also the<br>greatest discipleship opportunity of our time.\u201d</div>
  </div>
  <div class="two-col">
    <div>
      <h3 class="ch">The wave is here</h3>
      <p>An estimated <b>$124 trillion</b> will change hands through 2048 \u2014 the largest wealth transfer ever recorded,
         with roughly <b>$105 trillion</b> flowing to heirs and <b>$18 trillion</b> to charity.
         More than half of it comes from the <b>2%</b> of households who are high-net-worth.</p>
      <p>Every one of those families is quietly asking the same questions: <i>Will our children be ready? What
         holds us together? Is there more to pass on than money?</i></p>
    </div>
    <div>
      <h3 class="ch">The gap nobody is filling</h3>
      <p>Families are transferring <b>wealth without wisdom</b> \u2014 handing heirs a fortune and no compass.
         Advisors are trained for the balance sheet, not the dinner table. Churches disciple individuals
         but rarely reach the family system.</p>
      <p>The result is the oldest problem in Scripture: a legacy left <b>by default</b> instead of <b>by design</b>.</p>
    </div>
  </div>
  <div class="answer">
    <div class="answer-ic">{tree(color=GOLD,size=46)}</div>
    <div>
      <h3>The Family Legacy category is the answer \u2014 and the doorway.</h3>
      <p>It equips families to transfer <b>wisdom before wealth</b>: to name their values, write a family mission,
         and hand on a living faith. And it does it through the proven 40-day campaign model that has already
         shaped thousands of churches \u2014 now aimed squarely at the family, and built to scale into an entire ecosystem.</p>
    </div>
  </div>
</section>''')

# ---------- 3. WHY THIS MATTERS TO EVERYONE ----------
def aud_card(t, ic, body):
    return f'''<div class="vcard">
      <div class="vic"><svg viewBox="0 0 24 24" width="22" height="22"><path d="{ic}"/></svg></div>
      <h4>{t}</h4><p>{body}</p></div>'''
cards = "".join(aud_card(*a) for a in AUDIENCE_VALUE)
PAGES.append(f'''<section class="sheet">
  {label("Why This Matters \u2014 To Everyone","One category, five reasons to build it")}
  <p class="sub-intro">A campaign library only matters if the people who could champion it can see themselves in it.
     Here is the case for each audience whose \u201cyes\u201d moves this forward.</p>
  <div class="vgrid">{cards}</div>
  <div class="keyq">If Brett handed this to Tom Conway, a senior pastor, a ministry partner, or a donor \u2014
     <b>would they immediately see the opportunity and want to build it?</b> Every page that follows is built to earn that yes.</div>
</section>''')

# ---------- 4. CATEGORIES vs AFFINITIES ----------
def col_chips(items, cls):
    return "".join(f'<span class="mchip {cls}">{i}</span>' for i in items)
PAGES.append(f'''<section class="sheet">
  {label("Two Dimensions, One Library","Categories \u00d7 Affinities")}
  <p class="sub-intro">The library is built on two axes at once. <b>Categories</b> are topics \u2014 what the campaign is about.
     <b>Affinities</b> are audiences \u2014 who it\u2019s built for. The same content, re-voiced for a new audience, becomes a new product.</p>
  <div class="ca-grid">
    <div class="ca-box cat">
      <div class="ca-head">CATEGORIES <span>topics</span></div>
      <div class="chiprow">{col_chips(CATEGORIES,"cat")}</div>
    </div>
    <div class="ca-x">\u00d7</div>
    <div class="ca-box aff">
      <div class="ca-head">AFFINITIES <span>audiences</span></div>
      <div class="chiprow">{col_chips(AFFINITIES,"aff")}</div>
    </div>
  </div>
  <div class="ca-result">
    <div class="ca-eq">Every campaign lives at an intersection</div>
    <div class="ca-examples">
      <span><b>Family Legacy</b> \u00d7 <b>Business Owners</b> = Business Owner Edition</span>
      <span><b>Family Legacy</b> \u00d7 <b>Advisors</b> = Advisor Edition</span>
      <span><b>Family Legacy</b> \u00d7 <b>Family Offices</b> = Family Office Edition</span>
    </div>
    <p>One library, two dimensions, exponential reach. A handful of strong categories, re-voiced across a dozen
       affinities, becomes hundreds of tailored resources \u2014 each one feeling purpose-built for the reader who opens it.</p>
  </div>
</section>''')

# ---------- 5. THE ECOSYSTEM / DOORWAY ----------
PAGES.append(f'''<section class="sheet">
  {label("Think Ecosystem, Not Campaign","The category is a doorway")}
  <p class="sub-intro">Family Legacy isn\u2019t a shelf of studies. It\u2019s the front door to the <b>Family Legacy by Design</b>
     ecosystem \u2014 a path that draws a family deeper, and gives advisors and churches a place to lead them.</p>
  <div class="eco">
    <div class="eco-band aud"><span class="eco-t">Audiences</span>
      <div class="eco-items"><span>Legacy Families</span><span>Christian Advisors</span><span>Affinity Groups</span></div></div>
    <div class="eco-arrow">access through &darr;</div>
    <div class="eco-band plat"><span class="eco-t">The Membership Platform</span>
      <div class="eco-items"><span>Resources for families</span><span>Tools &amp; certification for advisors</span><span>Specialized editions</span><span>&infin; new libraries added</span></div></div>
    <div class="eco-arrow">powered by &darr;</div>
    <div class="eco-band eng"><span class="eco-t">The Content Engine</span>
      <div class="eco-items"><span>Foundations</span><span>&times; Affinity Editions</span><span>&times; Campaign Libraries</span><span>&rarr; Formats</span><span>+ Advisor Tools</span></div></div>
  </div>
  <div class="ip-strip">
    <div class="ip-h">Built on Tom Conway\u2019s intellectual property</div>
    <div class="ip-items">
      <span>Multi-Generational Legacy Coaching Process</span><span>The Five Areas of Legacy</span>
      <span>The F.A.M.I.L.Y. Review</span><span>Family Mission &amp; Values</span>
      <span>Generational Discipleship</span><span>Legacy Conversations &amp; Letters</span><span>Advisor Tools</span>
    </div>
    <p>A family that starts with a 6-session study can be drawn into a devotional, a coached F.A.M.I.L.Y. Review,
       an advisor relationship, and ultimately the membership platform. The campaign is the first step of a long journey.</p>
  </div>
</section>''')

# ---------- 6. CAMPAIGN FLEXIBILITY ----------
def fmt_card(name, desc):
    return f'<div class="fcard"><div class="fname">{name}</div><div class="fdesc">{desc}</div></div>'
fcards = "".join(fmt_card(*f) for f in FORMATS)
PAGES.append(f'''<section class="sheet">
  {label("One Campaign, Many Experiences","Built-in flexibility")}
  <p class="sub-intro">A single campaign isn\u2019t one product \u2014 it\u2019s a source. The same body of teaching flexes to fit
     the moment, the audience, and the ministry context. Take the flagship, <b>Family Legacy</b>:</p>
  <div class="flex-hub">
    <div class="hub-core">{tree(color="#fff",size=40)}<span>Family<br>Legacy</span></div>
    <div class="hub-note">becomes &rarr;</div>
  </div>
  <div class="fgrid">{fcards}</div>
  <div class="flex-foot">Every title in the category carries the same flexibility \u2014 so one investment in content
     serves the church-wide campaign, the small group, the personal devotional, and the advisor-led family workshop alike.</div>
</section>''')

# ---------- 7..16  CAMPAIGN PAGES ----------
def sess_rows(sessions):
    out = ""
    for i,(t,d) in enumerate(sessions, 1):
        out += f'<div class="sess"><div class="sn">{i}</div><div><div class="st">{t}</div><div class="sd">{d}</div></div></div>'
    return out
def chips(items, cls="need"):
    return "".join(f'<span class="ch-{cls}">{i}</span>' for i in items)

for c in CAMPAIGNS:
    PAGES.append(f'''<section class="sheet camp">
      <div class="camp-hd">
        <div class="camp-rank">{c['rank']:02d}</div>
        <div class="camp-ttl"><div class="camp-cat">FAMILY LEGACY \u00b7 FLAGSHIP CAMPAIGN</div>
          <h2>{c['title']}</h2><div class="camp-tag">{c['tag']}</div></div>
        {brand(small=True)}
      </div>
      <div class="camp-body">
        <div class="camp-L">
          <div class="blk prob"><div class="blk-h">The Core Problem</div><p>{c['problem']}</p></div>
          <div class="blk prom"><div class="blk-h">The Transformation Promise</div><p>{c['promise']}</p></div>
          <div class="blk why"><div class="blk-h">Why This Campaign Matters</div><p>{c['why']}</p></div>
        </div>
        <div class="camp-R">
          <div class="mini"><div class="mini-h">Felt Needs</div><div class="chiprow">{chips(c['needs'],"need")}</div></div>
          <div class="mini"><div class="mini-h">Intended Audience</div><p class="aud-line">{c['audience']}</p></div>
          <div class="mini"><div class="mini-h">Ministry Outcomes</div><ul class="out">{"".join(f"<li>{o}</li>" for o in c['outcomes'])}</ul></div>
        </div>
      </div>
      <div class="arch">
        <div class="arch-h"><span>Expanded Campaign Architecture</span><span class="arch-fmt">6 Sessions \u00b7 40-Day Journey \u00b7 flexes to 4-session, 21/30-day, workshop &amp; devotional</span></div>
        <div class="sessgrid">{sess_rows(c['sessions'])}</div>
      </div>
      <div class="camp-foot">
        <div class="cf-h">A doorway into the ecosystem</div>
        <div class="cf-path">
          <span class="cf-step on">This campaign</span><span class="cf-ar">&rarr;</span>
          <span class="cf-step">Devotional</span><span class="cf-ar">&rarr;</span>
          <span class="cf-step">Coached F.A.M.I.L.Y. Review</span><span class="cf-ar">&rarr;</span>
          <span class="cf-step">Advisor relationship</span><span class="cf-ar">&rarr;</span>
          <span class="cf-step end">Membership platform</span>
        </div>
      </div>
    </section>''')

# ---------- 17. THE CATALOG UNDERNEATH ----------
more = "".join(f'<span class="mchip cat">{t}</span>' for t in CATALOG_MORE)
PAGES.append(f'''<section class="sheet">
  {label("The Catalog Underneath","The Top 10 are the tip")}
  <p class="sub-intro">The ten flagship campaigns are the visible front of a much deeper catalog. Beneath them sit dozens
     more titles in the same category \u2014 each one a doorway for a different family, season, or felt need.</p>
  <div class="depth">
    <div class="depth-row top"><span class="dl">FLAGSHIP \u00b7 TOP 10</span><div class="chiprow">{"".join(f'<span class="mchip gold">{c["title"]}</span>' for c in CAMPAIGNS)}</div></div>
    <div class="depth-row"><span class="dl">DEEPER CATALOG \u00b7 11\u201320</span><div class="chiprow">{more}</div></div>
    <div class="depth-row faint"><span class="dl">AND BEYOND</span><div class="chiprow"><span class="mchip ghost">+ continually expanding</span><span class="mchip ghost">+ affinity editions</span><span class="mchip ghost">+ new categories</span></div></div>
  </div>
  <div class="rapid">
    <div class="rapid-h">Generated rapidly, by design</div>
    <p>Because every campaign shares one architecture \u2014 problem, promise, felt needs, audience, outcomes, six sessions \u2014
       new titles and affinity editions can be drafted in hours, not months, with AI-assisted production. The catalog isn\u2019t
       a fixed inventory; it\u2019s a <b>growing system</b> that compounds with every addition.</p>
  </div>
</section>''')

# ---------- 18. THE BUILD / CTA ----------
PAGES.append(f'''<section class="sheet cta">
  <div class="cta-shape"></div>
  <div class="cta-in">
    {brand()}
    <div class="cta-kick">THE INVITATION</div>
    <h1>Build Family Legacy as the<br>flagship of the ecosystem.</h1>
    <div class="cv-rule"></div>
    <div class="cta-steps">
      <div class="cta-step"><b>1</b><div><h4>Prove the model</h4><p>Develop the Top 10 Family Legacy campaigns to full \u201cbeef\u201d \u2014 problem, promise, architecture, and formats \u2014 as the proof-of-concept for the whole library.</p></div></div>
      <div class="cta-step"><b>2</b><div><h4>Open the doorways</h4><p>Add affinity editions (Advisor, Business Owner, Family Office) and connect each campaign into the F.A.M.I.L.Y. Review and coaching path.</p></div></div>
      <div class="cta-step"><b>3</b><div><h4>Stand up the platform</h4><p>Bring families, advisors, and affinity groups onto one membership platform \u2014 and keep adding libraries.</p></div></div>
    </div>
    <div class="cta-close">
      <p>This is not a catalog. It\u2019s the start of a scalable Family Legacy ecosystem \u2014 a way to transfer
         <b>wisdom before wealth</b> to a generation, and to mobilize the families and advisors positioned to fund the Kingdom.</p>
      <div class="cta-by">Family Legacy by Design &nbsp;\u00b7&nbsp; Presented by <b>lifetogether</b></div>
    </div>
  </div>
</section>''')

# ---------------- ASSEMBLE ----------------
CSS = f'''
@font-face{{font-family:'Poppins';src:url(data:font/ttf;base64,{poppins_b}) format('truetype');font-weight:700;}}
@font-face{{font-family:'Poppins';src:url(data:font/ttf;base64,{poppins_sb}) format('truetype');font-weight:600;}}
@font-face{{font-family:'Poppins';src:url(data:font/ttf;base64,{poppins_m}) format('truetype');font-weight:500;}}
@font-face{{font-family:'Inter';src:url(data:font/ttf;base64,{inter}) format('truetype');font-weight:400 700;}}
*{{margin:0;padding:0;box-sizing:border-box;}}
:root{{--ink:{INK};--forest:{FOREST};--forest2:{FOREST2};--leaf:{LEAF};--gold:{GOLD};--brick:{BRICK};--cream:{CREAM};--mute:{MUTE};}}
html,body{{background:#cdd3cd;font-family:'Inter',sans-serif;color:var(--ink);-webkit-font-smoothing:antialiased;}}
h1,h2,h3,h4,.fp{{font-family:'Poppins',sans-serif;}}
.sheet{{width:816px;height:1056px;background:var(--cream);margin:0 auto;position:relative;overflow:hidden;
  padding:46px 56px;page-break-after:always;}}
.sheet:last-child{{page-break-after:auto;}}

.brand{{display:flex;align-items:center;gap:11px;}}
.brand .bn{{font-family:'Poppins';font-weight:700;color:#fff;font-size:18px;line-height:1;}}
.brand .bn span{{display:block;font-weight:500;font-size:10.5px;letter-spacing:.16em;color:#cfe0d4;margin-top:3px;}}

.seclabel{{display:flex;align-items:center;gap:12px;margin-bottom:16px;}}
.seclabel .sq{{width:17px;height:17px;background:var(--gold);border-radius:4px;flex:none;}}
.seclabel h2{{font-size:27px;font-weight:700;color:var(--forest);letter-spacing:-.4px;}}
.seclabel .tag{{margin-left:auto;font-size:11.5px;color:var(--mute);font-weight:500;font-family:'Poppins';
  background:#ece9e1;padding:6px 13px;border-radius:18px;}}
.sub-intro{{font-size:14.5px;line-height:1.6;color:#33403a;max-width:680px;margin-bottom:22px;}}
.ch{{font-size:16px;font-weight:600;color:var(--forest);margin-bottom:7px;}}

/* COVER */
.cover{{background:var(--forest);color:#fff;display:flex;flex-direction:column;padding:54px 56px 46px;}}
.cv-shape{{position:absolute;top:-120px;right:-160px;width:520px;height:640px;background:var(--leaf);opacity:.22;transform:skewX(-18deg);}}
.cv-shape2{{position:absolute;bottom:-160px;left:-120px;width:420px;height:560px;background:var(--forest2);opacity:.55;transform:skewX(-16deg);}}
.cv-top{{display:flex;align-items:center;justify-content:space-between;position:relative;z-index:2;}}
.cv-pres{{font-family:'Poppins';font-weight:600;font-size:11px;letter-spacing:.18em;color:var(--gold);}}
.cv-mid{{position:relative;z-index:2;margin-top:auto;margin-bottom:auto;}}
.cv-kick{{font-family:'Poppins';font-weight:600;letter-spacing:.2em;font-size:13px;color:#a9c6b3;margin-bottom:16px;}}
.cover h1{{font-size:54px;font-weight:700;line-height:1.04;letter-spacing:-1px;}}
.cover h1 em{{color:var(--gold);font-style:normal;}}
.cv-rule{{width:90px;height:5px;background:var(--gold);border-radius:3px;margin:24px 0;}}
.cv-mid p{{font-size:16px;line-height:1.6;color:#e3ede5;max-width:600px;}}
.cv-foot{{position:relative;z-index:2;}}
.cv-stats{{display:flex;gap:20px;margin-bottom:24px;}}
.cv-stat{{flex:1;background:rgba(255,255,255,.06);border:1px solid rgba(255,255,255,.14);border-radius:13px;padding:16px 16px;}}
.cv-stat b{{font-family:'Poppins';font-weight:700;font-size:28px;color:var(--gold);display:block;}}
.cv-stat span{{font-size:12px;color:#d4e0d7;line-height:1.4;display:block;margin-top:5px;}}
.cv-by{{font-size:12.5px;color:#bcd2c2;border-top:1px solid rgba(255,255,255,.16);padding-top:16px;}}
.cv-by b,.cv-stat b+span b{{color:#fff;}}

/* OPPORTUNITY */
.lead-band{{background:var(--forest);border-radius:16px;padding:26px 30px;margin-bottom:24px;position:relative;overflow:hidden;}}
.lead-band:after{{content:"";position:absolute;right:-40px;top:-30px;width:240px;height:200%;background:var(--gold);opacity:.10;transform:skewX(-18deg);}}
.lead-q{{font-family:'Poppins';font-weight:600;color:#fff;font-size:21px;line-height:1.35;position:relative;z-index:2;}}
.two-col{{display:grid;grid-template-columns:1fr 1fr;gap:30px;margin-bottom:24px;}}
.two-col p{{font-size:13.5px;line-height:1.6;color:#36433c;margin-bottom:10px;}}
.two-col b{{color:var(--forest);}}
.answer{{display:flex;gap:18px;align-items:flex-start;background:#fff;border-radius:16px;padding:24px 26px;
  border-left:6px solid var(--gold);box-shadow:0 8px 22px rgba(14,58,45,.10);}}
.answer-ic{{flex:none;width:64px;height:64px;border-radius:14px;background:#eef3ec;display:flex;align-items:center;justify-content:center;}}
.answer h3{{font-size:18px;color:var(--forest);font-weight:700;margin-bottom:8px;}}
.answer p{{font-size:13.5px;line-height:1.6;color:#36433c;}}
.answer b{{color:var(--brick);}}

/* AUDIENCE VALUE */
.vgrid{{display:grid;grid-template-columns:1fr 1fr;gap:16px;}}
.vcard{{background:#fff;border-radius:14px;padding:18px 20px;box-shadow:0 7px 18px rgba(14,58,45,.07);border-top:4px solid var(--leaf);}}
.vcard:nth-child(5){{grid-column:1 / span 2;border-top-color:var(--gold);}}
.vic{{width:42px;height:42px;border-radius:11px;background:#eef3ec;display:flex;align-items:center;justify-content:center;margin-bottom:11px;}}
.vic svg{{fill:var(--forest);}}
.vcard h4{{font-size:16px;font-weight:600;color:var(--forest);margin-bottom:7px;}}
.vcard p{{font-size:12.8px;line-height:1.55;color:#3a463f;}}
.keyq{{margin-top:20px;background:#f0ece2;border-radius:13px;padding:18px 22px;font-size:13.5px;line-height:1.6;color:#3a463f;
  border-left:5px solid var(--brick);}}
.keyq b{{color:var(--brick);}}

/* CATEGORIES x AFFINITIES */
.ca-grid{{display:grid;grid-template-columns:1fr 44px 1fr;align-items:stretch;gap:0;margin-bottom:24px;}}
.ca-box{{background:#fff;border-radius:15px;padding:20px;box-shadow:0 7px 18px rgba(14,58,45,.07);}}
.ca-box.cat{{border-top:5px solid var(--forest);}}
.ca-box.aff{{border-top:5px solid var(--brick);}}
.ca-x{{display:flex;align-items:center;justify-content:center;font-family:'Poppins';font-weight:700;font-size:34px;color:var(--gold);}}
.ca-head{{font-family:'Poppins';font-weight:700;font-size:15px;color:var(--forest);letter-spacing:.04em;margin-bottom:14px;}}
.ca-box.aff .ca-head{{color:var(--brick);}}
.ca-head span{{font-weight:500;font-size:11px;color:var(--mute);letter-spacing:.1em;text-transform:uppercase;margin-left:8px;}}
.chiprow{{display:flex;flex-wrap:wrap;gap:7px;}}
.mchip{{border-radius:8px;padding:6px 11px;font-size:12px;font-weight:500;font-family:'Inter';line-height:1.2;}}
.mchip.cat{{background:#eaf0e8;color:var(--forest);border:1px solid #d3e0d2;}}
.mchip.aff{{background:#f6ebe7;color:var(--brick);border:1px solid #eccfc6;}}
.mchip.gold{{background:#fdf1dc;color:#8a5a06;border:1px solid #f3d79b;}}
.mchip.ghost{{background:transparent;color:var(--mute);border:1px dashed #bcc4bd;}}
.ca-result{{background:var(--forest);border-radius:15px;padding:22px 26px;color:#fff;position:relative;overflow:hidden;}}
.ca-result:after{{content:"";position:absolute;left:-40px;bottom:-40px;width:240px;height:200%;background:var(--leaf);opacity:.16;transform:skewX(-18deg);}}
.ca-eq{{font-family:'Poppins';font-weight:600;color:var(--gold);font-size:13px;letter-spacing:.06em;text-transform:uppercase;margin-bottom:12px;position:relative;z-index:2;}}
.ca-examples{{display:flex;flex-direction:column;gap:6px;margin-bottom:14px;position:relative;z-index:2;}}
.ca-examples span{{font-size:14px;color:#eaf2ec;}}
.ca-examples b{{color:#fff;font-weight:600;}}
.ca-result p{{font-size:13px;line-height:1.6;color:#d7e3da;position:relative;z-index:2;}}

/* ECOSYSTEM */
.eco{{margin-bottom:20px;}}
.eco-band{{border-radius:13px;padding:15px 20px;display:flex;align-items:center;gap:18px;}}
.eco-band .eco-t{{font-family:'Poppins';font-weight:700;font-size:14px;flex:none;width:150px;}}
.eco-items{{display:flex;flex-wrap:wrap;gap:8px;}}
.eco-items span{{font-size:12px;border-radius:7px;padding:5px 10px;font-weight:500;}}
.eco-band.aud{{background:#fff;border:1px solid #e1ddd1;}}
.eco-band.aud .eco-t{{color:var(--forest);}} .eco-band.aud .eco-items span{{background:#eef3ec;color:var(--forest);}}
.eco-band.plat{{background:var(--forest);}} .eco-band.plat .eco-t{{color:var(--gold);}}
.eco-band.plat .eco-items span{{background:rgba(255,255,255,.10);color:#eaf2ec;}}
.eco-band.eng{{background:#f0ece2;border:1px solid #e1ddd1;}} .eco-band.eng .eco-t{{color:var(--brick);}}
.eco-band.eng .eco-items span{{background:#fff;color:#3a463f;border:1px solid #e3ddcf;}}
.eco-arrow{{text-align:center;font-family:'Poppins';font-weight:600;font-size:11px;letter-spacing:.1em;text-transform:uppercase;color:var(--gold);padding:7px 0;}}
.ip-strip{{background:#fff;border-radius:15px;padding:22px 26px;box-shadow:0 7px 18px rgba(14,58,45,.07);border-top:5px solid var(--gold);}}
.ip-h{{font-family:'Poppins';font-weight:700;color:var(--forest);font-size:16px;margin-bottom:13px;}}
.ip-items{{display:flex;flex-wrap:wrap;gap:8px;margin-bottom:14px;}}
.ip-items span{{background:#eef3ec;color:var(--forest);border:1px solid #d3e0d2;border-radius:8px;padding:6px 11px;font-size:12px;font-weight:500;}}
.ip-strip p{{font-size:13px;line-height:1.6;color:#3a463f;}}

/* FLEXIBILITY */
.flex-hub{{display:flex;align-items:center;justify-content:center;gap:18px;margin:6px 0 20px;}}
.hub-core{{width:120px;height:120px;border-radius:50%;background:var(--forest);color:#fff;display:flex;flex-direction:column;
  align-items:center;justify-content:center;gap:4px;box-shadow:0 10px 24px rgba(14,58,45,.22);}}
.hub-core span{{font-family:'Poppins';font-weight:700;font-size:15px;text-align:center;line-height:1.1;}}
.hub-note{{font-family:'Poppins';font-weight:600;color:var(--gold);font-size:15px;}}
.fgrid{{display:grid;grid-template-columns:1fr 1fr;gap:13px;}}
.fcard{{background:#fff;border-radius:12px;padding:14px 17px;box-shadow:0 6px 15px rgba(14,58,45,.06);border-left:4px solid var(--leaf);}}
.fname{{font-family:'Poppins';font-weight:600;color:var(--forest);font-size:14.5px;margin-bottom:3px;}}
.fdesc{{font-size:12.3px;line-height:1.5;color:#46524b;}}
.flex-foot{{margin-top:20px;background:#f0ece2;border-radius:13px;padding:16px 20px;font-size:13px;line-height:1.6;color:#3a463f;border-left:5px solid var(--gold);}}

/* CAMPAIGN PAGES */
.camp{{padding:40px 50px;}}
.camp-hd{{display:flex;align-items:center;gap:18px;background:var(--forest);border-radius:16px;padding:20px 24px;margin-bottom:18px;position:relative;overflow:hidden;}}
.camp-hd:after{{content:"";position:absolute;right:-30px;top:-40px;width:200px;height:240%;background:var(--leaf);opacity:.18;transform:skewX(-18deg);}}
.camp-rank{{font-family:'Poppins';font-weight:700;font-size:46px;color:var(--gold);line-height:1;flex:none;position:relative;z-index:2;}}
.camp-ttl{{flex:1;position:relative;z-index:2;}}
.camp-cat{{font-family:'Poppins';font-weight:600;font-size:10.5px;letter-spacing:.16em;color:#a9c6b3;margin-bottom:4px;}}
.camp-ttl h2{{color:#fff;font-size:30px;font-weight:700;line-height:1;letter-spacing:-.4px;}}
.camp-tag{{color:var(--gold);font-size:14px;font-style:italic;font-family:'Inter';margin-top:5px;}}
.camp-hd .brand{{position:relative;z-index:2;}}
.camp-body{{display:grid;grid-template-columns:1.25fr 1fr;gap:16px;margin-bottom:16px;}}
.blk{{border-radius:12px;padding:14px 16px;margin-bottom:12px;}}
.blk:last-child{{margin-bottom:0;}}
.blk-h{{font-family:'Poppins';font-weight:700;font-size:11px;letter-spacing:.08em;text-transform:uppercase;margin-bottom:6px;}}
.blk p{{font-size:13px;line-height:1.55;color:#36433c;}}
.blk.prob{{background:#f6ebe7;border-left:4px solid var(--brick);}} .blk.prob .blk-h{{color:var(--brick);}}
.blk.prom{{background:#eef3ec;border-left:4px solid var(--leaf);}} .blk.prom .blk-h{{color:var(--leaf);}}
.blk.why{{background:#fdf3e1;border-left:4px solid var(--gold);}} .blk.why .blk-h{{color:#b07a0c;}}
.camp-R{{display:flex;flex-direction:column;gap:12px;}}
.mini{{background:#fff;border-radius:12px;padding:13px 15px;box-shadow:0 5px 13px rgba(14,58,45,.06);}}
.mini-h{{font-family:'Poppins';font-weight:700;font-size:11px;letter-spacing:.08em;text-transform:uppercase;color:var(--forest);margin-bottom:8px;}}
.ch-need{{display:inline-block;background:#f0ece2;color:#5a4a3a;border-radius:7px;padding:5px 9px;font-size:11.5px;margin:0 5px 5px 0;}}
.aud-line{{font-size:12.5px;color:#3a463f;line-height:1.5;}}
.out{{list-style:none;}}
.out li{{font-size:12.5px;color:#36433c;line-height:1.5;padding-left:16px;position:relative;margin-bottom:3px;}}
.out li:before{{content:"";position:absolute;left:0;top:7px;width:6px;height:6px;border-radius:50%;background:var(--gold);}}
.arch{{background:var(--forest);border-radius:14px;padding:18px 22px;position:relative;overflow:hidden;}}
.arch:after{{content:"";position:absolute;left:-40px;bottom:-40px;width:220px;height:200%;background:var(--leaf);opacity:.14;transform:skewX(-18deg);}}
.arch-h{{display:flex;align-items:baseline;justify-content:space-between;margin-bottom:13px;position:relative;z-index:2;}}
.arch-h span:first-child{{font-family:'Poppins';font-weight:700;color:#fff;font-size:15px;}}
.arch-fmt{{font-size:10.5px;color:#a9c6b3;font-family:'Poppins';font-weight:500;max-width:330px;text-align:right;}}
.sessgrid{{display:grid;grid-template-columns:1fr 1fr;gap:9px;position:relative;z-index:2;}}
.sess{{display:flex;gap:10px;align-items:flex-start;background:rgba(255,255,255,.07);border:1px solid rgba(255,255,255,.12);border-radius:10px;padding:10px 12px;}}
.sn{{flex:none;width:24px;height:24px;border-radius:7px;background:var(--gold);color:#5a3a00;font-family:'Poppins';font-weight:700;font-size:12px;display:flex;align-items:center;justify-content:center;}}
.st{{font-family:'Poppins';font-weight:600;color:#fff;font-size:13px;line-height:1.2;}}
.sd{{font-size:11px;color:#bcd2c2;line-height:1.35;margin-top:2px;}}

.camp-foot{{margin-top:14px;background:#f0ece2;border-radius:13px;padding:15px 20px;border-left:5px solid var(--brick);}}
.cf-h{{font-family:'Poppins';font-weight:700;font-size:11px;letter-spacing:.1em;text-transform:uppercase;color:var(--brick);margin-bottom:11px;}}
.cf-path{{display:flex;align-items:center;flex-wrap:wrap;gap:7px;}}
.cf-step{{background:#fff;border:1px solid #ddd7ca;border-radius:20px;padding:6px 13px;font-size:11.5px;font-weight:500;color:#46524b;font-family:'Poppins';}}
.cf-step.on{{background:var(--forest);color:#fff;border-color:var(--forest);}}
.cf-step.end{{background:var(--gold);color:#5a3a00;border-color:var(--gold);font-weight:600;}}
.cf-ar{{color:var(--brick);font-family:'Poppins';font-weight:700;font-size:14px;}}

/* CATALOG DEPTH */
.depth{{display:flex;flex-direction:column;gap:14px;margin-bottom:22px;}}
.depth-row{{background:#fff;border-radius:13px;padding:15px 18px;box-shadow:0 6px 15px rgba(14,58,45,.06);}}
.depth-row.top{{border-left:5px solid var(--gold);}}
.depth-row.faint{{background:transparent;box-shadow:none;border:1px dashed #c2cabf;}}
.dl{{display:block;font-family:'Poppins';font-weight:700;font-size:10.5px;letter-spacing:.12em;color:var(--mute);margin-bottom:10px;}}
.rapid{{background:var(--forest);border-radius:15px;padding:22px 26px;color:#fff;position:relative;overflow:hidden;}}
.rapid:after{{content:"";position:absolute;right:-40px;top:-30px;width:240px;height:200%;background:var(--gold);opacity:.10;transform:skewX(-18deg);}}
.rapid-h{{font-family:'Poppins';font-weight:700;color:var(--gold);font-size:16px;margin-bottom:10px;position:relative;z-index:2;}}
.rapid p{{font-size:13.5px;line-height:1.65;color:#e0ebe2;position:relative;z-index:2;}}
.rapid b{{color:#fff;}}

/* CTA */
.cta{{background:var(--forest);color:#fff;padding:50px 56px;}}
.cta-shape{{position:absolute;top:-140px;right:-160px;width:520px;height:640px;background:var(--leaf);opacity:.2;transform:skewX(-18deg);}}
.cta-in{{position:relative;z-index:2;height:100%;display:flex;flex-direction:column;}}
.cta-kick{{font-family:'Poppins';font-weight:600;letter-spacing:.2em;font-size:12px;color:var(--gold);margin:26px 0 12px;}}
.cta h1{{font-size:42px;font-weight:700;line-height:1.06;letter-spacing:-.6px;}}
.cta-steps{{margin:18px 0 auto;display:flex;flex-direction:column;gap:14px;}}
.cta-step{{display:flex;gap:16px;align-items:flex-start;background:rgba(255,255,255,.06);border:1px solid rgba(255,255,255,.14);border-radius:13px;padding:16px 20px;}}
.cta-step b{{flex:none;width:38px;height:38px;border-radius:10px;background:var(--gold);color:#5a3a00;font-family:'Poppins';font-weight:700;font-size:18px;display:flex;align-items:center;justify-content:center;}}
.cta-step h4{{font-size:16px;font-weight:600;color:#fff;margin-bottom:4px;}}
.cta-step p{{font-size:13px;line-height:1.55;color:#d4e0d7;}}
.cta-close{{border-top:1px solid rgba(255,255,255,.16);padding-top:20px;}}
.cta-close p{{font-size:15px;line-height:1.6;color:#e6efe8;margin-bottom:16px;}}
.cta-close b{{color:var(--gold);}}
.cta-by{{font-size:12.5px;color:#bcd2c2;}} .cta-by b{{color:#fff;}}
'''

HTML = "<!doctype html><html lang='en'><head><meta charset='utf-8'><style>" + CSS + "</style></head><body>" + "".join(PAGES) + "</body></html>"
out = pathlib.Path("/home/claude/family_legacy_strategy.html")
out.write_text(HTML, encoding="utf-8")
print("wrote", out, len(HTML), "bytes;", len(PAGES), "pages")
