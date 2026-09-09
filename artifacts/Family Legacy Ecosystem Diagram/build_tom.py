# -*- coding: utf-8 -*-
import base64, pathlib
F = pathlib.Path("/home/claude/fonts")
def b64(n): return base64.b64encode((F/n).read_bytes()).decode()
playfair, playfair_i = b64("Playfair.ttf"), b64("Playfair-Italic.ttf")
garamond, garamond_i = b64("EBGaramond.ttf"), b64("EBGaramond-Italic.ttf")
poppins_sb, poppins_m, inter = b64("Poppins-SemiBold.ttf"), b64("Poppins-Medium.ttf"), b64("Inter.ttf")

INK, FOREST, FOREST2, LEAF, GOLD, GOLD2, BRICK, CREAM, MUTE = (
    "#21261f", "#0e3a2d", "#16513c", "#4a7c2f", "#f5a623", "#c79a45", "#a04e3c", "#f8f5ee", "#6a7268")

def tree(color="#ffffff", size=54):
    sw = 5
    br = ["M50 60 C 46 48, 40 42, 30 36","M50 60 C 54 48, 60 42, 70 36",
          "M50 56 C 48 46, 44 40, 36 50","M50 56 C 52 46, 56 40, 64 50","M50 52 C 50 42, 50 36, 50 26"]
    p = "".join(f'<path d="{d}" stroke="{color}" stroke-width="{sw}" stroke-linecap="round" fill="none"/>' for d in br)
    return f'''<svg width="{size}" height="{size}" viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg"><g fill="{color}">
      <path d="M46 58 q4 -6 8 0 v28 a4 4 0 0 1 -8 0 z"/>{p}
      <circle cx="50" cy="22" r="10"/><circle cx="30" cy="33" r="8"/><circle cx="70" cy="33" r="8"/>
      <circle cx="34" cy="50" r="7"/><circle cx="66" cy="50" r="7"/><circle cx="22" cy="46" r="6"/><circle cx="78" cy="46" r="6"/>
    </g></svg>'''

def brand_dark():
    return f'<div class="brand">{tree(color=FOREST,size=34)}<div class="bn">Family Legacy<span>BY DESIGN</span></div></div>'

def eyebrow(t): return f'<div class="eyebrow">{t}</div>'

P = []

# 1. COVER
P.append(f'''<section class="sheet cover">
  <div class="cv-shape"></div><div class="cv-shape2"></div>
  <div class="cv-head">{tree(size=50)}<div class="bn light">Family Legacy<span>BY DESIGN</span></div></div>
  <div class="cv-body">
    <div class="cv-eye">A VISION FOR THE PARTNERSHIP</div>
    <h1>The Path<br>Forward</h1>
    <div class="cv-rule"></div>
    <p class="cv-sub">How the work you have spent a lifetime building becomes a living ecosystem &mdash;
       one that puts clarity, alignment, and communication into the hands of the families and advisors
       who will never get an hour at your table.</p>
  </div>
  <div class="cv-foot">
    <div><span class="cv-lbl">PREPARED FOR</span><div class="cv-name">Tom Conway</div></div>
    <div class="cv-by"><span class="cv-lbl">PRESENTED BY</span><div class="cv-name">Brett Eastman &middot; Lifetogether</div></div>
  </div>
</section>''')

# 2. THE HEART OF IT
P.append(f'''<section class="sheet">
  {brand_dark()}
  {eyebrow("THE HEART OF IT")}
  <h2 class="big">Families don&rsquo;t fail<br>at wealth. They fail<br>at <em>wisdom.</em></h2>
  <div class="lede2col">
    <p>Over the next two decades the largest transfer of wealth in history will move between
       generations. Most of it will not survive &mdash; not because the planning was poor, but because the
       <i>people</i> were not ready. Roughly seventy percent of wealth transitions fail by the second
       generation, ninety percent by the third.</p>
    <p>The breakdown is almost never financial. It is relational and spiritual. Families have a plan for
       their money and no plan for their people. The assets move; the alignment does not. And so a
       lifetime of provision quietly fractures the very family it was meant to bless.</p>
  </div>
  <div class="pull">&ldquo;Assets move. Alignment doesn&rsquo;t.&rdquo;</div>
  <div class="closing-note">
    <p>Tom, this is the gap your life&rsquo;s work was built to close. For three decades you have sat in living
       rooms helping families find <b>clarity, alignment, and communication</b> &mdash; helping them transfer
       not just wealth, but wisdom.</p>
    <p>The question in front of us now is a simple one: <i>how do we put what you do into the hands of the
       thousands of families &mdash; and the advisors who serve them &mdash; who will never get an hour at your
       kitchen table?</i></p>
  </div>
</section>''')

# 3. THE SHIFT
P.append(f'''<section class="sheet">
  {brand_dark()}
  {eyebrow("THE SHIFT")}
  <h2 class="big">From a shelf of books<br>to a <em>living ecosystem.</em></h2>
  <div class="lede2col">
    <p>Today, Family Legacy by Design is a remarkable collection &mdash; a coaching book, a family book, a
       filmed workshop, a six-session curriculum, a 40-day devotional, a training manual. All of it real,
       proven, and valuable.</p>
    <p>But a collection sits on a shelf. What families and advisors need is a <i>system they can step into</i>
       &mdash; one that meets them where they are, draws them deeper, and never stops growing.</p>
  </div>
  <div class="shift-row">
    <div class="shift-from"><span class="sh-lbl">TODAY</span><div class="sh-t">A library of<br>books &amp; workshops</div></div>
    <div class="shift-arrow">{tree(color=GOLD,size=40)}</div>
    <div class="shift-to"><span class="sh-lbl">FORWARD</span><div class="sh-t">A scalable legacy<br>ecosystem &amp; platform</div></div>
  </div>
  <div class="callout">
    <div class="callout-h">The shift in one sentence</div>
    <p>We take the body of work you have already built and turn it into a scalable Family Legacy ecosystem
       and membership platform &mdash; <b>one source, expressed in many forms, serving many audiences, expanding
       continually.</b></p>
    <div class="callout-tag">One body of work &nbsp;&middot;&nbsp; many doorways &nbsp;&middot;&nbsp; infinite room to grow</div>
  </div>
</section>''')

# 4. BUILT AROUND YOUR TWO GOALS
P.append(f'''<section class="sheet">
  {brand_dark()}
  {eyebrow("BUILT AROUND YOUR GOALS")}
  <h2 class="big">Two things matter most<br>to you. The whole system<br>serves <em>both.</em></h2>
  <div class="goals">
    <div class="goal">
      <div class="goal-n">01</div>
      <h3>Sell your content<br>&mdash; to the families who need it</h3>
      <p>The platform puts your books, curriculum, devotionals, and journeys directly into families&rsquo; hands
         &mdash; and into the hands of the advisors who serve them. Every resource is a doorway to the next: a
         devotional leads to a study, a study to a coached review, a review to a deeper relationship.</p>
    </div>
    <div class="goal">
      <div class="goal-n">02</div>
      <h3>Certify the advisors<br>&mdash; who carry it forward</h3>
      <p>The real engine is the advisor. The platform gives them a credible, faith-aligned designation &mdash;
         the <b>Certified Family Legacy Coach</b> &mdash; earned through your foundation curriculum and coaching
         journey, plus the tools they need to lead a family meeting, navigate the next-generation
         conversation, and add relational value their competitors simply cannot.</p>
    </div>
  </div>
  <div class="northstar">
    <div class="ns-h">THE NORTH STAR</div>
    <p>&ldquo;Whatever it takes to get an advisor to say <i>yes.</i>&rdquo; An advisor who says yes buys a pass, places it
       in the hands of the client families he already serves, and brings every one of them into your world.</p>
  </div>
</section>''')

# 5. ECOSYSTEM DIAGRAM
P.append(f'''<section class="sheet">
  {brand_dark()}
  {eyebrow("THE ECOSYSTEM AT A GLANCE")}
  <h2 class="med">Three audiences. One platform.<br>An engine that never stops.</h2>
  <div class="eco">
    <div class="eco-aud">
      <div class="ea"><div class="ea-t">Legacy Families</div><div class="ea-d">High-capacity, multi-generational households</div></div>
      <div class="ea"><div class="ea-t">Christian Advisors</div><div class="ea-d">Wealth, estate, family-office, planning</div></div>
      <div class="ea"><div class="ea-t">Affinities</div><div class="ea-d">Owners, next gen, widows, pastors &amp; more</div></div>
    </div>
    <div class="eco-link">they all enter through</div>
    <div class="eco-plat">
      <div class="ep-t">The Membership Platform</div>
      <div class="ep-d">Resources for families &middot; tools &amp; certification for advisors &middot; specialized editions for affinities &middot; new libraries added continually</div>
    </div>
    <div class="eco-link">continuously fed by</div>
    <div class="eco-eng">
      <div class="ee-t">The Content Engine</div>
      <div class="ee-row"><span>Foundations</span><span class="x">&times;</span><span>Editions</span><span class="x">&times;</span><span>Libraries</span><span class="x">&rarr;</span><span>Formats</span><span class="plus">+ Advisor Tools</span></div>
    </div>
  </div>
  <p class="eco-foot">A handful of foundations, re-voiced across audiences and topics and expressed in many formats,
     becomes thousands of tailored resources &mdash; all delivered through one platform, to the three audiences
     positioned to carry legacy, and fund the Kingdom, for generations.</p>
</section>''')

# 6. YOUR WORK, ORGANIZED
def org_block(label, items, accent):
    chips = "".join(f'<span class="ochip">{i}</span>' for i in items)
    return f'''<div class="org" style="--ac:{accent}">
      <div class="org-l">{label}</div><div class="org-chips">{chips}</div></div>'''
P.append(f'''<section class="sheet">
  {brand_dark()}
  {eyebrow("ORDER IN THE ABUNDANCE")}
  <h2 class="med">Everything you&rsquo;ve built,<br>in one clear architecture.</h2>
  <p class="org-intro">We have, in your words, a dump truck of assets. The breakthrough isn&rsquo;t more content &mdash;
     it&rsquo;s organizing it so it scales. Here is the whole thing on a single page.</p>
  {org_block("THE FOUNDATIONS", ["Coaching Foundation Series (6)","Family Foundation Series (6)","Filmed Workshop","Training Manual"], FOREST)}
  {org_block("THE EDITIONS", ["Advisor Editions &mdash; by profession","Attorney","CPA","Wealth Advisor","Family Office","Pastor","Counselor","Donor Dev."], BRICK)}
  {org_block("THE AFFINITIES", ["Family Affinity Series &mdash; by people","Next Gen","Women&rsquo;s","Men&rsquo;s","Blended","Married","Widowed","Parenting","Multi-Gen"], LEAF)}
  {org_block("THE LIBRARIES", ["Campaign Libraries &mdash; by topic","Family Legacy","Faith &amp; Finances","Stewardship","Generosity","Purpose at Work","Next Generations","Wisdom","Following God"], GOLD2)}
  {org_block("THE FORMATS", ["Journeys &mdash; families &middot; 30-day","Training Series &mdash; coaches &middot; 30-day","4 &amp; 6-session studies","7 / 21 / 40-day","Workshops","Family Conversation Guides"], FOREST2)}
  {org_block("THE TOOLS &amp; THE BADGE", ["Advisor Tools &mdash; Legacy Letters, Family Covenant, Meeting Guides, Gen-2 Conversations, Facilitation Scripts","Certified Family Legacy Coach"], GOLD)}
</section>''')

# 7. THE BREAKTHROUGH
P.append(f'''<section class="sheet">
  {brand_dark()}
  {eyebrow("WHY NOW")}
  <h2 class="big">What took six months<br>now takes <em>a week.</em></h2>
  <div class="lede2col">
    <p>For years, building one of these resources meant months of writing, design, and production. That is
       why the catalog stayed small and the vision stayed on the shelf. The cost of creation kept the dream
       in the future tense.</p>
    <p>That has changed. Drawing on twenty-five years of Lifetogether curriculum, your framework, and the
       best voices in the field, we can now draft a complete campaign &mdash; overview, sessions, scripture,
       facilitator scripts, and a 40-day journey &mdash; in days, not months.</p>
  </div>
  <div class="pull">&ldquo;It was never about pressing buttons.<br>It&rsquo;s knowing <i>which</i> button to press.&rdquo;</div>
  <div class="closing-note">
    <p>The skill isn&rsquo;t the technology &mdash; it is the judgment. Knowing which of a thousand possible resources a
       real pastor, advisor, or family actually needs. Pulling from the best of <b>your work, ours, and
       theirs.</b> Shaping a raw outline into something with a soul.</p>
    <p>That is what makes this defensible. And that is what makes it scale: the work of months, now measured
       in days &mdash; without losing the heart that made it worth doing.</p>
  </div>
</section>''')

# 8. WHERE WE ARE / NEXT
def status_list(items):
    return "".join(f'<li>{i}</li>' for i in items)
P.append(f'''<section class="sheet last">
  {brand_dark()}
  {eyebrow("WHERE WE ARE")}
  <h2 class="med">Closer than it has<br>ever been.</h2>
  <div class="status">
    <div class="st-col">
      <div class="st-h">In hand &amp; underway</div>
      <ul>{status_list([
        "Foundation Series &mdash; four of six filmed; scripts ready; next shoot scheduled",
        "Family editions &amp; 30-day journeys in production",
        "Advisor tools drafted as white papers &mdash; starting with the Legacy Letter",
        "A 16-email advisor campaign built and ready to send",
        "Website &amp; client portal expansion underway"])}</ul>
    </div>
    <div class="st-col">
      <div class="st-h">The next 60&ndash;90 days</div>
      <ul>{status_list([
        "Complete the foundation curriculum &amp; coaching journeys",
        "Stand up the membership platform with the certification path",
        "Build the campaign-library proof titles",
        "Mock-ups ready for the August 12&ndash;13 workshop",
        "Begin advisor onboarding toward certification"])}</ul>
    </div>
  </div>
  <div class="final">
    <div class="final-rule"></div>
    <p>Tom &mdash; this is your life&rsquo;s work, made multipliable. The framework is proven. The assets exist. The
       cost of building has collapsed. What remains is to put it in front of the families and advisors who
       have been waiting for exactly this.</p>
    <div class="final-tag">{tree(color=GOLD,size=30)}<span>Daily inspiration &nbsp;+&nbsp; weekly conversation &nbsp;=&nbsp; family transformation.</span></div>
    <div class="final-by">Family Legacy by Design &nbsp;&middot;&nbsp; Presented by <b>lifetogether</b></div>
  </div>
</section>''')

CSS = f'''
@font-face{{font-family:'Playfair';src:url(data:font/ttf;base64,{playfair}) format('truetype');font-weight:400 900;}}
@font-face{{font-family:'Playfair';src:url(data:font/ttf;base64,{playfair_i}) format('truetype');font-weight:400 900;font-style:italic;}}
@font-face{{font-family:'Garamond';src:url(data:font/ttf;base64,{garamond}) format('truetype');font-weight:400 800;}}
@font-face{{font-family:'Garamond';src:url(data:font/ttf;base64,{garamond_i}) format('truetype');font-weight:400 800;font-style:italic;}}
@font-face{{font-family:'Poppins';src:url(data:font/ttf;base64,{poppins_sb}) format('truetype');font-weight:600;}}
@font-face{{font-family:'Poppins';src:url(data:font/ttf;base64,{poppins_m}) format('truetype');font-weight:500;}}
@font-face{{font-family:'Inter';src:url(data:font/ttf;base64,{inter}) format('truetype');font-weight:400 700;}}
*{{margin:0;padding:0;box-sizing:border-box;}}
:root{{--ink:{INK};--forest:{FOREST};--forest2:{FOREST2};--leaf:{LEAF};--gold:{GOLD};--gold2:{GOLD2};--brick:{BRICK};--cream:{CREAM};--mute:{MUTE};}}
html,body{{background:#cdd3cd;font-family:'Garamond',serif;color:var(--ink);-webkit-font-smoothing:antialiased;}}
.sheet{{width:816px;height:1056px;background:var(--cream);margin:0 auto;position:relative;overflow:hidden;
  padding:64px 72px;page-break-after:always;}}
.sheet.last{{page-break-after:auto;}}
.brand{{display:flex;align-items:center;gap:9px;margin-bottom:30px;}}
.brand .bn{{font-family:'Poppins';font-weight:600;color:var(--forest);font-size:14px;line-height:1;}}
.brand .bn span{{display:block;font-weight:500;font-size:8.5px;letter-spacing:.16em;color:var(--gold2);margin-top:3px;}}
.eyebrow{{font-family:'Poppins';font-weight:600;font-size:12px;letter-spacing:.24em;color:var(--brick);margin-bottom:20px;}}
h2.big{{font-family:'Playfair';font-weight:800;font-size:50px;line-height:1.04;color:var(--forest);letter-spacing:-.5px;margin-bottom:30px;}}
h2.med{{font-family:'Playfair';font-weight:800;font-size:40px;line-height:1.08;color:var(--forest);letter-spacing:-.3px;margin-bottom:24px;}}
h2 em{{font-style:italic;color:var(--gold2);font-weight:800;}}
.lede2col{{column-count:2;column-gap:34px;margin-bottom:30px;}}
.lede2col p{{font-size:18px;line-height:1.5;color:#2f3a31;margin-bottom:12px;}}
.lede2col i{{font-style:italic;}} .lede2col b{{font-weight:700;color:var(--forest);}}
.pull{{font-family:'Playfair';font-style:italic;font-weight:500;font-size:30px;color:var(--forest);text-align:center;
  border-top:1px solid var(--gold2);border-bottom:1px solid var(--gold2);padding:24px 0;margin:8px 0 30px;line-height:1.25;}}
.pull i{{color:var(--brick);}}
.closing-note p{{font-size:18px;line-height:1.55;color:#2f3a31;margin-bottom:14px;}}
.closing-note b{{font-weight:700;color:var(--forest);}} .closing-note i{{font-style:italic;}}

/* COVER */
.cover{{background:var(--forest);color:#fff;padding:74px 72px;display:flex;flex-direction:column;}}
.cv-shape{{position:absolute;top:-140px;right:-180px;width:560px;height:680px;background:var(--leaf);opacity:.18;transform:skewX(-17deg);}}
.cv-shape2{{position:absolute;bottom:-180px;left:-140px;width:460px;height:600px;background:var(--forest2);opacity:.6;transform:skewX(-15deg);}}
.cv-head{{display:flex;align-items:center;gap:11px;position:relative;z-index:2;}}
.cv-head .bn{{font-family:'Poppins';font-weight:600;font-size:16px;color:#fff;line-height:1;}}
.cv-head .bn span{{display:block;font-weight:500;font-size:9px;letter-spacing:.18em;color:#bcd2c2;margin-top:3px;}}
.cv-body{{position:relative;z-index:2;margin-top:auto;margin-bottom:auto;}}
.cv-eye{{font-family:'Poppins';font-weight:600;font-size:13px;letter-spacing:.26em;color:var(--gold);margin-bottom:22px;}}
.cover h1{{font-family:'Playfair';font-weight:800;font-size:88px;line-height:.98;letter-spacing:-1.5px;}}
.cv-rule{{width:96px;height:4px;background:var(--gold);margin:30px 0;}}
.cv-sub{{font-family:'Garamond';font-size:21px;line-height:1.5;color:#e4ede6;max-width:560px;}}
.cv-foot{{position:relative;z-index:2;display:flex;justify-content:space-between;align-items:flex-end;
  border-top:1px solid rgba(255,255,255,.2);padding-top:24px;}}
.cv-lbl{{font-family:'Poppins';font-weight:600;font-size:10px;letter-spacing:.2em;color:#a9c6b3;display:block;margin-bottom:6px;}}
.cv-name{{font-family:'Playfair';font-size:22px;color:#fff;}}
.cv-by{{text-align:right;}}

/* SHIFT */
.shift-row{{display:flex;align-items:stretch;gap:0;margin:6px 0 30px;}}
.shift-from,.shift-to{{flex:1;border-radius:14px;padding:24px 26px;display:flex;flex-direction:column;justify-content:center;}}
.shift-from{{background:#efeadf;}} .shift-to{{background:var(--forest);}}
.shift-arrow{{display:flex;align-items:center;justify-content:center;padding:0 22px;}}
.sh-lbl{{font-family:'Poppins';font-weight:600;font-size:10px;letter-spacing:.2em;margin-bottom:9px;display:block;}}
.shift-from .sh-lbl{{color:var(--mute);}} .shift-to .sh-lbl{{color:var(--gold);}}
.sh-t{{font-family:'Playfair';font-weight:700;font-size:24px;line-height:1.12;}}
.shift-from .sh-t{{color:var(--forest);}} .shift-to .sh-t{{color:#fff;}}
.callout{{background:#fff;border-radius:16px;padding:28px 32px;border-left:6px solid var(--gold);box-shadow:0 10px 26px rgba(14,58,45,.08);}}
.callout-h{{font-family:'Poppins';font-weight:600;font-size:11px;letter-spacing:.18em;color:var(--brick);margin-bottom:12px;}}
.callout p{{font-size:20px;line-height:1.5;color:#2f3a31;}} .callout b{{font-weight:700;color:var(--forest);}}
.callout-tag{{font-family:'Playfair';font-style:italic;font-size:18px;color:var(--gold2);margin-top:16px;}}

/* GOALS */
.goals{{display:grid;grid-template-columns:1fr 1fr;gap:24px;margin-bottom:28px;}}
.goal{{background:#fff;border-radius:16px;padding:28px 28px 30px;box-shadow:0 10px 24px rgba(14,58,45,.08);border-top:5px solid var(--forest);}}
.goal:last-child{{border-top-color:var(--gold);}}
.goal-n{{font-family:'Playfair';font-weight:800;font-size:40px;color:var(--gold2);line-height:1;margin-bottom:12px;}}
.goal h3{{font-family:'Playfair';font-weight:700;font-size:24px;line-height:1.12;color:var(--forest);margin-bottom:14px;}}
.goal p{{font-size:17px;line-height:1.5;color:#2f3a31;}} .goal b{{font-weight:700;color:var(--brick);}}
.northstar{{background:var(--forest);border-radius:16px;padding:26px 32px;color:#fff;position:relative;overflow:hidden;}}
.northstar:after{{content:"";position:absolute;right:-40px;top:-30px;width:240px;height:200%;background:var(--gold);opacity:.10;transform:skewX(-17deg);}}
.ns-h{{font-family:'Poppins';font-weight:600;font-size:11px;letter-spacing:.2em;color:var(--gold);margin-bottom:12px;position:relative;z-index:2;}}
.northstar p{{font-size:20px;line-height:1.5;color:#eaf2ec;position:relative;z-index:2;}} .northstar i{{font-style:italic;color:#fff;}}

/* ECOSYSTEM */
.eco{{margin:6px 0 24px;}}
.eco-aud{{display:grid;grid-template-columns:repeat(3,1fr);gap:16px;}}
.ea{{background:#fff;border-radius:13px;padding:18px 18px;text-align:center;box-shadow:0 8px 18px rgba(14,58,45,.07);border-top:4px solid var(--leaf);}}
.ea-t{{font-family:'Playfair';font-weight:700;font-size:20px;color:var(--forest);margin-bottom:6px;}}
.ea-d{{font-size:14.5px;line-height:1.35;color:var(--mute);}}
.eco-link{{text-align:center;font-family:'Poppins';font-weight:500;font-size:11px;letter-spacing:.14em;text-transform:uppercase;color:var(--brick);padding:13px 0;}}
.eco-plat{{background:var(--forest);border-radius:13px;padding:22px 26px;text-align:center;}}
.ep-t{{font-family:'Playfair';font-weight:700;font-size:24px;color:#fff;margin-bottom:8px;}}
.ep-d{{font-size:15px;color:#bcd2c2;line-height:1.4;}}
.eco-eng{{background:#efeadf;border-radius:13px;padding:22px 26px;text-align:center;}}
.ee-t{{font-family:'Playfair';font-weight:700;font-size:22px;color:var(--brick);margin-bottom:12px;}}
.ee-row{{display:flex;flex-wrap:wrap;align-items:center;justify-content:center;gap:10px;}}
.ee-row span{{font-family:'Poppins';font-weight:600;font-size:14px;color:var(--forest);background:#fff;border-radius:8px;padding:7px 13px;}}
.ee-row .x{{background:none;color:var(--gold2);font-size:18px;padding:0 2px;}}
.ee-row .plus{{background:var(--gold);color:#5a3a00;}}
.eco-foot{{font-size:17.5px;line-height:1.55;color:#2f3a31;text-align:center;max-width:640px;margin:0 auto;}}

/* ORGANIZED */
.org-intro{{font-size:18px;line-height:1.5;color:#2f3a31;margin-bottom:22px;max-width:660px;}}
.org{{display:flex;gap:18px;align-items:flex-start;padding:13px 0;border-bottom:1px solid #e3ddcf;}}
.org:last-child{{border-bottom:none;}}
.org-l{{flex:none;width:166px;font-family:'Poppins';font-weight:600;font-size:11.5px;letter-spacing:.1em;color:var(--ac);padding-top:5px;}}
.org-chips{{display:flex;flex-wrap:wrap;gap:7px;}}
.ochip{{font-family:'Inter';font-size:12.5px;font-weight:500;color:#3a463f;background:#fff;border:1px solid #e3ddcf;border-radius:7px;padding:6px 11px;line-height:1.2;}}
.org-chips .ochip:first-child{{background:var(--ac);color:#fff;border-color:var(--ac);font-weight:600;}}

/* STATUS */
.status{{display:grid;grid-template-columns:1fr 1fr;gap:30px;margin-bottom:30px;}}
.st-h{{font-family:'Playfair';font-weight:700;font-size:22px;color:var(--forest);margin-bottom:14px;padding-bottom:10px;border-bottom:2px solid var(--gold);}}
.status ul{{list-style:none;}}
.status li{{font-size:16.5px;line-height:1.45;color:#2f3a31;padding-left:20px;position:relative;margin-bottom:11px;}}
.status li:before{{content:"";position:absolute;left:0;top:9px;width:7px;height:7px;border-radius:50%;background:var(--gold);}}
.final{{margin-top:auto;}}
.final-rule{{width:100%;height:1px;background:var(--gold2);margin-bottom:22px;}}
.final p{{font-family:'Garamond';font-size:19px;line-height:1.55;color:#2f3a31;margin-bottom:20px;}}
.final-tag{{display:flex;align-items:center;gap:12px;margin-bottom:18px;}}
.final-tag span{{font-family:'Playfair';font-style:italic;font-weight:600;font-size:20px;color:var(--forest);}}
.final-by{{font-family:'Poppins';font-weight:500;font-size:13px;color:var(--mute);}} .final-by b{{color:var(--forest);font-weight:600;}}
'''

HTML = "<!doctype html><html lang='en'><head><meta charset='utf-8'><style>"+CSS+"</style></head><body>"+"".join(P)+"</body></html>"
out = pathlib.Path("/home/claude/tom_vision.html")
out.write_text(HTML, encoding="utf-8")
print("wrote", out, len(HTML), "bytes;", len(P), "pages")
