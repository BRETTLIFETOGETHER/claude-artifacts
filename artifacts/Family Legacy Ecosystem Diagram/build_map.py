# -*- coding: utf-8 -*-
import base64, pathlib
F = pathlib.Path("/home/claude/fonts")
def b64(n): return base64.b64encode((F/n).read_bytes()).decode()
poppins_b, poppins_sb, poppins_m, inter = b64("Poppins-Bold.ttf"), b64("Poppins-SemiBold.ttf"), b64("Poppins-Medium.ttf"), b64("Inter.ttf")

INK, FOREST, FOREST2, LEAF, GOLD, BRICK, CREAM, MUTE = (
    "#1d2622","#0e3a2d","#15503c","#4a7c2f","#f5a623","#a04e3c","#f7f5f0","#5d6b62")

def tree(color="#ffffff", size=46):
    sw=5; br=["M50 60 C 46 48, 40 42, 30 36","M50 60 C 54 48, 60 42, 70 36",
        "M50 56 C 48 46, 44 40, 36 50","M50 56 C 52 46, 56 40, 64 50","M50 52 C 50 42, 50 36, 50 26"]
    p="".join(f'<path d="{d}" stroke="{color}" stroke-width="{sw}" stroke-linecap="round" fill="none"/>' for d in br)
    return f'''<svg width="{size}" height="{size}" viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg"><g fill="{color}">
      <path d="M46 58 q4 -6 8 0 v28 a4 4 0 0 1 -8 0 z"/>{p}
      <circle cx="50" cy="22" r="10"/><circle cx="30" cy="33" r="8"/><circle cx="70" cy="33" r="8"/>
      <circle cx="34" cy="50" r="7"/><circle cx="66" cy="50" r="7"/><circle cx="22" cy="46" r="6"/><circle cx="78" cy="46" r="6"/></g></svg>'''

# ---- decision tags ----
def tag(k):
    m={"set":("&#10003; set","tg-set"),"lean":("&#9680; leaning","tg-lean"),"open":("&#9711; open","tg-open")}
    t,c=m[k]; return f'<span class="tg {c}">{t}</span>'

# ---- renderers ----
def sec(n,title,sub=""):
    s=f'<div class="sec-sub">{sub}</div>' if sub else ''
    return f'<div class="sec"><div class="sec-n">{n:02d}</div><div><h2>{title}</h2>{s}</div></div>'
def sub(t,tg=""):
    return f'<div class="subh">{t}{(" "+tag(tg)) if tg else ""}</div>'
def chips(items, lead=None):
    out=""
    if lead: out+=f'<span class="chip lead">{lead}</span>'
    out+="".join(f'<span class="chip">{i}</span>' for i in items)
    return f'<div class="chiprow">{out}</div>'
def deflist(pairs):
    rows="".join(f'<div class="dl-row"><div class="dl-t">{t}</div><div class="dl-d">{d}</div></div>' for t,d in pairs)
    return f'<div class="dl">{rows}</div>'
def twocol(a_title,a,b_title,b):
    la="".join(f"<li>{x}</li>" for x in a); lb="".join(f"<li>{x}</li>" for x in b)
    return f'''<div class="twocol"><div><div class="tc-h">{a_title}</div><ul>{la}</ul></div>
      <div><div class="tc-h">{b_title}</div><ul>{lb}</ul></div></div>'''
def card(title, body, accent=GOLD):
    return f'<div class="card" style="--ac:{accent}"><div class="card-h">{title}</div>{body}</div>'
def note(t): return f'<div class="note">{t}</div>'

B=[]  # body blocks

# 1 — VISION
B.append(sec(1,"The Vision, in One Line","The north the whole build points to"))
B.append(card("The shift",
    '<p class="big">From a library of books &amp; workshops into a <b>scalable Family Legacy ecosystem &amp; membership platform</b> &mdash; one body of work, expressed in many forms, serving many audiences, expanding continually.</p>', FOREST))
B.append(sub("Three audiences it serves"))
B.append(chips(["Legacy Families &mdash; high-capacity, multi-generational","Christian Advisors &mdash; wealth, estate, family office, planning","Affinities &mdash; owners, next gen, widows, pastors, nonprofits"]))
B.append(sub("Tom&rsquo;s two goals (everything serves these)"))
B.append(chips(["1 &middot; Sell his content to the families who need it","2 &middot; Certify the advisors who carry it forward"], lead="NORTH STAR &mdash; whatever it takes to get an advisor to say yes"))
B.append(note('Pillar line: <b>&ldquo;Daily inspiration + weekly conversation = family transformation.&rdquo;</b>'))

# 2 — NAMING / VOCAB
B.append(sec(2,"Naming &amp; Vocabulary","The words we&rsquo;ve agreed on &mdash; so we stop re-deciding them"))
B.append(deflist([
    ("Library "+tag("lean"),"The subscription / platform you buy into (Family Legacy Library)."),
    ("Catalog "+tag("lean"),"Everything inside the library &mdash; the categories &times; titles."),
    ("Journey "+tag("set"),"Family-facing product. 30-day."),
    ("Training Series "+tag("set"),"Coach / advisor-facing product. 30-day."),
    ("Category "+tag("set"),"A topic (Family Legacy, Faith &amp; Finances, Generosity&hellip;)."),
    ("Affinity "+tag("set"),"A people group (widows, next gen, owners, couples&hellip;)."),
    ("Edition "+tag("set"),"An audience-tailored version &mdash; esp. Advisor Editions, by profession."),
    ("Certified Family Legacy Coach "+tag("set"),"The advisor designation earned through the platform."),
]))
B.append(sub("Use this / Avoid this"))
B.append(twocol("USE",
    ["<b>Faith &amp; Finances</b> for the finance category","<b>Following God</b> (not Obedience &mdash; too in-your-face)",
     "<b>Next Generations</b> (plural)","<b>Marketplace / Purpose at Work</b> (a category, not an affinity)",
     "<b>Kingdom Impact</b> for the Multiplication idea","<b>Legacy Families</b> (not &lsquo;ultra-high-net-worth&rsquo;)"],
    "AVOID",
    ["<b>Financial Wisdom</b> &mdash; reserved for Ron Blue / advisor side","<b>Financial Peace / Financial Keys</b> &mdash; Ramsey collision",
     "<b>Living Generously</b> &mdash; too close to &lsquo;Generous Living&rsquo;","<b>Collection</b> &mdash; reads like &lsquo;collection plate&rsquo;",
     "Stamping <b>&lsquo;40-day&rsquo;</b> on covers &mdash; flexibility is the feature","Weak taglines like &lsquo;give it away&rsquo;"]))
B.append(note('Idea parked for later: <b>Kingdom Intelligence</b> &mdash; &ldquo;how to use AI for God&rsquo;s glory.&rdquo; '+tag("open")))

# 3 — ARCHITECTURE
B.append(sec(3,"The Architecture","The content engine, on one page"))
B.append(sub("Foundations (the core IP)"))
B.append(chips(["6 Coaching Foundation Series","6 Family Foundation Series","Family Legacy Curriculum","Family Legacy Devotionals","Family Legacy Workshop"]))
B.append(sub("Editions &mdash; by profession (Advisor Editions)"))
B.append(chips(["Lawyer / Estate","Wealth Advisor","Family Office","CPA / Tax","Business Transition / M&amp;A","Executive Coach","Christian Counselor","Donor Development","Pastor / Ministry Leader","Family Legacy Coach"]))
B.append(sub("Affinities &mdash; by people (Family Affinity Series)"))
B.append(chips(["Next Gen / Students","Women&rsquo;s","Men&rsquo;s","Blended Family","Married Couples","Widow / Widowers","Single Again","Parenting &amp; Grandparenting","Multi-Generational","Aging Parents"]))
B.append(sub("Libraries &mdash; by topic (Campaign Libraries)"))
B.append(chips(["Family Legacy","Faith &amp; Finances","Stewardship","Generosity","Purpose at Work","Next Generations","Wisdom","Following God","Abundance","Kingdom Impact"]))
B.append(sub("Formats (the flexibility menu)"))
B.append(chips(["7-day","21-day","30-day","40-day","4-session","6-session","Workshop","Devotional","Family Conversation Guide"], lead="7-DAY is a priority &mdash; most pastors do one finance message a year"))
B.append(sub("Tools &amp; the badge"))
B.append(chips(["20 Advisor Tools (white papers)","Certified Family Legacy Coach"]))

# 4 — CATEGORIES & CATALOG
B.append(sec(4,"Categories &amp; the Catalog","~10 categories &times; ~100 titles each = thousands of journeys"))
B.append(sub("Family Legacy &mdash; Top 10"))
B.append(chips(["Family Legacy","Leaving a Lasting Legacy","Generations","Faith for Generations","Family by Design","Legacy Living","Blessing the Next Generation","The Generational Life","Building a Spiritual Legacy","Passing Faith Forward"], lead="FLAGSHIP"))
B.append(sub("Family Legacy &mdash; deeper catalog (11&ndash;20)"))
B.append(chips(["Family Legacy by Design","Family Mission","The Legacy Family","Spiritual Inheritance","Legacy Conversations","Blessing Your Children","Family Values","Heritage of Faith","Legacy Journey","The Family Table"]))
B.append(note("Same Top-10-then-the-rest pattern repeats for every category. Build the best 10 first; the rest are names that get filled in over time."))

# 5 — CAMPAIGN PAGE FORMAT
B.append(sec(5,"The Campaign Page Format","The structure to &lsquo;crack&rsquo; once, then button-press for the rest"))
B.append(deflist([
    ("1 &middot; Overview / Brief","Marketing-forward: why this &amp; why now, the problem, the transformation, what&rsquo;s unique, felt needs, audience &amp; best season, key outcomes."),
    ("2 &middot; Six Sessions","Each with title + subtitle (minimum), <b>anchor scripture</b>, and the biblical backbone / big idea. (This is the &lsquo;more beef&rsquo;.)"),
    ("3 &middot; 40-Day Outline","Every day a title + subtitle, aligned to the six sessions."),
    ("4 &middot; 10-Minute Group Scripts","The &lsquo;secret sauce&rsquo; &mdash; a draft of the facilitator&rsquo;s 10 minutes. Never been produced."),
]))
B.append(note("Session 1 script always includes the group agreement and the &ldquo;who else would benefit from joining us?&rdquo; invite &mdash; the mechanic that historically doubled groups week 1 to week 2."))

# 6 — ADVISOR TOOLS
B.append(sec(6,"The 20 Advisor Tools","The lever for the advisor &lsquo;yes&rsquo; &mdash; 3-page white papers, Legacy Letter first"))
B.append(chips(["Legacy Letters","Family Covenant","Family Meeting Guides","Conflict Resolution Tools","Gen-2 Conversation Guides","Facilitation Scripts","The Stewardship Review","The Contentment Plan","The Family Giving Plan","Giving While Living","Faith-Based Financial Plan","From Portfolio to Purpose","The Christian Client Journey","God Owns It All &mdash; Client Services"], lead="START: Legacy Letter"))
B.append(note("~50 generated &rarr; pick the best 20. Each becomes a clean 3-page PDF: what it is, why it matters, how to use it. Free samples, then subscribe for the full set."))

# 7 — TOM'S IP INVENTORY
B.append(sec(7,"Tom&rsquo;s IP Inventory","The &lsquo;dump truck of assets&rsquo;, accounted for"))
B.append(sub("Coaching Foundation Series &mdash; 6 sessions"))
B.append(chips(["Family Legacy Overview","Family Clarity","Legacy Planning","Family Mission, Vision &amp; Values","Family Meetings","Family Alignment"]))
B.append(sub("Family Legacy Business Series &mdash; 10 (Heritage Forum / Donner, Ron Blue forewords)"))
B.append(chips(["The Family Constitution","Kingdom First, Family Always","Calling &amp; Contribution","Crisis &amp; Redemption","The Power of Prayer in the Boardroom","Guarding the Gate","Generational Transfer w/o Trauma","Finish Well","Kingdom Legacy","Growth &amp; Flourishing"]))
B.append(sub("Ministry Track &mdash; 3"))
B.append(chips(["How to Launch a Family Legacy Ministry","Coaching Family Legacy Ministry Leaders","Leading a Family Legacy Small Group"]))
B.append(sub("Ron Blue &mdash; ultra-high-net-worth (3)"))
B.append(chips(["Splitting Heirs","How Much Is Enough / God Owns It All","Generous Living"]))
B.append(sub("Masterclass Platform 2.0 &mdash; 12-part video library (sample sessions)"))
B.append(chips(["Living by Design, Not Default","Passing Down Faith, Not Just Finances","The Art of Family Conversations","Generosity That Outlives You","Succession with Significance","Finishing Well, Beginning Again","The Five Capitals of Lasting Legacy"]))
B.append(sub("Also in hand"))
B.append(chips(["Trade Book (Coaching Edition)","Family Edition","12-Session Filmed Workshop","40 Days of Family Legacy (devo + video + study guide)","Training Manual"]))

# 8 — BUSINESS MODEL & CERT
B.append(sec(8,"Business Model &amp; Certification","How it sustains itself"))
B.append(sub("Pricing ladder",""))
B.append(deflist([
    ("Basic &mdash; single-campaign license","~$1,000. Digital, delivered in 3&ndash;5 business days even pre-built."),
    ("Semi-custom &mdash; church","Tailored edition, 5&ndash;10 business days."),
    ("Annual subscription","~$2,500. The recurring-revenue engine; full library access."),
    ("Fully-custom advisor edition","3&ndash;6 weeks; client-branded journeys."),
]))
B.append(note("Numbers illustrative "+tag("open")+". Model is Kajabi-style SaaS via the Christian Advisor Network. Tom&rsquo;s constraint: it <b>must sustain itself</b> &mdash; no more donor money beyond what&rsquo;s committed."))
B.append(sub("Certified Family Legacy Coach &mdash; the path"))
B.append(chips(["6-week cohort","+ the curriculum","+ the course","+ the 30-day coaching journey"], lead="REQUIRED: the overview &mdash; Clarity, Alignment, Communication"))
B.append(note("Next Gen &amp; Family Meetings are optional add-ons; the overview series is the required core."))

# 9 — MARKETING & WORKSHOP
B.append(sec(9,"Marketing &amp; the Workshop","The urgent clock"))
B.append(card("The target",
    '<p class="big">~<b>25 financial planners</b> registered for the <b>Aug 12&ndash;13</b> Southern California workshop &mdash; ~<b>7 weeks</b> out.</p>', BRICK))
B.append(sub("Email campaign &mdash; 16 emails over 7 weeks"))
B.append(twocol("PLAN",
    ["~7 value-add national newsletters","+ 3 local (West Coast) sends","Two voices: faith-forward (warm) &amp; values-based (broad)","Saturday ~6:00am is the proven slot","Send one out <b>today</b> (momentum)"],
    "LEVERS / LESSONS",
    ["Subject line is the #1 lever; curiosity beats descriptive","Click-through is the real challenge, not opens","QA every link &mdash; a broken link once cost ~762 clicks","Add a webinar or two to drive registration","Hire a marketer; LinkedIn + the lists"]))
B.append(note("Lists in hand: ~298k total &mdash; Christian Advisor Network ~90k, CFP ~69.8k, Big-6 ~33k, CKA/KA ~5k, RIA ~22k. Reach goals: 30k advisors / 30k families / 30k churches."))

# 10 — PRODUCTION
B.append(sec(10,"Production Pipeline","Why this is suddenly buildable"))
B.append(card("The breakthrough",
    '<p class="big">What took <b>six months</b> now takes <b>about a week</b>.</p>'
    '<p>AI cleanup &rarr; Atticus / Vellum or Fiverr for fast pagination &rarr; InDesign template + human proofing (widows, orphans, hyphenation). ~$300&ndash;$1,500 per book after the template is built.</p>', FOREST))
B.append(note('&ldquo;It was never about pressing buttons &mdash; it&rsquo;s knowing <b>which</b> button to press,&rdquo; pulling from your work, ours, and theirs.'))
B.append(note('<b>Process fix to lock in:</b> keep ONE master content source so good copy &amp; verses stop getting lost when chats reshuffle versions.'))

# 11 — STATUS
B.append(sec(11,"Status","Where things actually stand"))
B.append(twocol("IN HAND / UNDERWAY",
    ["Foundation Series &mdash; 4 of 6 filmed; scripts for the rest; shoot in ~4 weeks","Family editions &amp; 30-day journeys in production","Advisor tools being drafted as white papers","16-email campaign built (in Claude HTML; not yet in Mailchimp)","Website &amp; client portal expansion underway","Trailers loaded to the site"],
    "NEXT 60&ndash;90 DAYS",
    ["Finish the foundation curriculum &amp; coaching journeys","Stand up the membership platform + certification path","Build the campaign-library proof titles","Mock-ups ready for Aug 12&ndash;13","Begin advisor onboarding toward certification"]))

# 12 — OPEN QUESTIONS
B.append(sec(12,"Open Questions","The parking lot &mdash; decisions still to lock"))
opens=["Final naming: Library vs. Catalog vs. Platform",
 "30-day vs. 40-day as the standard (leaning 30; 40 for the flagship Family Legacy / Family by Design)",
 "Which titles are church/consumer vs. legacy-family",
 "Do we launch a Family Legacy Ministry (church track)? &mdash; Brett wants it; not pushing Tom",
 "&lsquo;Series&rsquo; in edition names, or drop it",
 "Final category list &amp; which titles to surface first",
 "Pricing numbers ($ per license / subscription)",
 "Discount deadline date &mdash; needed to give the urgency emails real teeth"]
B.append('<div class="opens">'+"".join(f'<div class="op">{tag("open")} {o}</div>' for o in opens)+'</div>')

BODY = "".join(B)

CSS_COMMON = f'''
@font-face{{font-family:'Poppins';src:url(data:font/ttf;base64,{poppins_b}) format('truetype');font-weight:700;}}
@font-face{{font-family:'Poppins';src:url(data:font/ttf;base64,{poppins_sb}) format('truetype');font-weight:600;}}
@font-face{{font-family:'Poppins';src:url(data:font/ttf;base64,{poppins_m}) format('truetype');font-weight:500;}}
@font-face{{font-family:'Inter';src:url(data:font/ttf;base64,{inter}) format('truetype');font-weight:400 700;}}
*{{margin:0;padding:0;box-sizing:border-box;}}
:root{{--ink:{INK};--forest:{FOREST};--forest2:{FOREST2};--leaf:{LEAF};--gold:{GOLD};--brick:{BRICK};--cream:{CREAM};--mute:{MUTE};}}
h1,h2,h3,.fp{{font-family:'Poppins',sans-serif;}}
body{{font-family:'Inter',sans-serif;color:var(--ink);-webkit-font-smoothing:antialiased;}}
'''

COVER = f'''<!doctype html><html><head><meta charset="utf-8"><style>{CSS_COMMON}
html,body{{margin:0;}}
.cover{{width:8.5in;height:11in;background:var(--forest);color:#fff;position:relative;overflow:hidden;padding:0.85in 0.8in;display:flex;flex-direction:column;}}
.s1{{position:absolute;top:-1.4in;right:-1.6in;width:5.4in;height:7in;background:var(--leaf);opacity:.2;transform:skewX(-17deg);}}
.s2{{position:absolute;bottom:-1.7in;left:-1.3in;width:4.4in;height:6in;background:var(--forest2);opacity:.6;transform:skewX(-15deg);}}
.head{{display:flex;align-items:center;gap:11px;position:relative;z-index:2;}}
.head .bn{{font-family:'Poppins';font-weight:600;font-size:16px;color:#fff;line-height:1;}}
.head .bn span{{display:block;font-weight:500;font-size:9px;letter-spacing:.18em;color:#bcd2c2;margin-top:3px;}}
.mid{{position:relative;z-index:2;margin-top:auto;margin-bottom:auto;}}
.eye{{font-family:'Poppins';font-weight:600;font-size:12px;letter-spacing:.24em;color:var(--gold);margin-bottom:18px;}}
h1{{font-family:'Poppins';font-weight:700;font-size:52px;line-height:1.04;letter-spacing:-1px;}}
.rule{{width:90px;height:5px;background:var(--gold);border-radius:3px;margin:24px 0;}}
.sub{{font-size:18px;line-height:1.55;color:#e4ede6;max-width:5.4in;}}
.foot{{position:relative;z-index:2;border-top:1px solid rgba(255,255,255,.2);padding-top:18px;display:flex;justify-content:space-between;align-items:center;}}
.foot .l{{font-size:13px;color:#bcd2c2;}} .foot .l b{{color:#fff;}}
.pill{{font-family:'Poppins';font-weight:600;font-size:11px;letter-spacing:.1em;color:#5a3a00;background:var(--gold);border-radius:20px;padding:7px 14px;}}
</style></head><body><div class="cover"><div class="s1"></div><div class="s2"></div>
  <div class="head">{tree(size=46)}<div class="bn">Family Legacy<span>BY DESIGN</span></div></div>
  <div class="mid">
    <div class="eye">INTERNAL WORKING REFERENCE</div>
    <h1>Master Notes<br>&amp; Build Map</h1>
    <div class="rule"></div>
    <div class="sub">Everything we&rsquo;ve talked through &mdash; the vision, the vocabulary, the architecture, the catalog, the tools, the model, the marketing, and the open questions &mdash; captured in one place, so nothing gets lost between conversations.</div>
  </div>
  <div class="foot"><div class="l">Family Legacy by Design &nbsp;&middot;&nbsp; <b>Lifetogether</b></div>
    <div class="pill">CAPTURE + PRESENT</div></div>
</div></body></html>'''

DOC = f'''<!doctype html><html><head><meta charset="utf-8"><style>{CSS_COMMON}
body{{background:#fff;font-size:13px;line-height:1.5;}}
.sec{{display:flex;gap:14px;align-items:flex-start;margin:30px 0 14px;padding-top:14px;border-top:2px solid var(--gold);break-inside:avoid;}}
.sec:first-child{{margin-top:0;padding-top:0;border-top:none;}}
.sec-n{{font-family:'Poppins';font-weight:700;font-size:30px;color:var(--gold);line-height:.9;flex:none;}}
.sec h2{{font-size:21px;font-weight:700;color:var(--forest);letter-spacing:-.2px;}}
.sec-sub{{font-size:12.5px;color:var(--mute);margin-top:3px;}}
.subh{{font-family:'Poppins';font-weight:600;font-size:12px;letter-spacing:.04em;color:var(--brick);margin:14px 0 9px;text-transform:uppercase;}}
.chiprow{{display:flex;flex-wrap:wrap;gap:7px;margin-bottom:6px;break-inside:avoid;}}
.chip{{background:#f1efe8;border:1px solid #e0dccf;border-radius:7px;padding:6px 11px;font-size:12px;font-weight:500;color:#36433c;line-height:1.2;}}
.chip.lead{{background:var(--forest);color:#fff;border-color:var(--forest);font-weight:600;font-family:'Poppins';font-size:11px;letter-spacing:.03em;}}
.dl{{display:flex;flex-direction:column;gap:0;margin-bottom:6px;}}
.dl-row{{display:flex;gap:16px;padding:9px 0;border-bottom:1px solid #eceae2;break-inside:avoid;}}
.dl-row:last-child{{border-bottom:none;}}
.dl-t{{flex:none;width:2.35in;font-family:'Poppins';font-weight:600;font-size:12.5px;color:var(--forest);}}
.dl-d{{font-size:12.5px;color:#3a463f;line-height:1.45;}}
.twocol{{display:grid;grid-template-columns:1fr 1fr;gap:24px;margin-bottom:6px;break-inside:avoid;}}
.tc-h{{font-family:'Poppins';font-weight:700;font-size:11px;letter-spacing:.1em;color:var(--mute);margin-bottom:8px;}}
.twocol ul{{list-style:none;}}
.twocol li{{font-size:12.3px;line-height:1.45;color:#36433c;padding-left:15px;position:relative;margin-bottom:6px;}}
.twocol li:before{{content:"";position:absolute;left:0;top:7px;width:5px;height:5px;border-radius:50%;background:var(--gold);}}
.twocol b{{color:var(--forest);font-weight:600;}}
.card{{background:var(--ac);border-radius:13px;padding:18px 22px;margin:6px 0 8px;color:#fff;break-inside:avoid;}}
.card .card-h{{font-family:'Poppins';font-weight:600;font-size:11px;letter-spacing:.16em;text-transform:uppercase;opacity:.85;margin-bottom:8px;}}
.card .big{{font-family:'Poppins';font-weight:500;font-size:18px;line-height:1.35;}}
.card .big b{{font-weight:700;}}
.card p{{font-size:13px;line-height:1.5;margin-top:8px;color:rgba(255,255,255,.92);}}
.note{{background:#fbf5e8;border-left:4px solid var(--gold);border-radius:9px;padding:11px 15px;font-size:12.3px;line-height:1.5;color:#46412f;margin:8px 0;break-inside:avoid;}}
.note b{{color:var(--brick);}}
.tg{{font-family:'Poppins';font-weight:600;font-size:9.5px;letter-spacing:.03em;border-radius:12px;padding:2px 8px;white-space:nowrap;vertical-align:middle;}}
.tg-set{{background:#e4efe2;color:#2f6b3a;}} .tg-lean{{background:#fdeecd;color:#9a6a08;}} .tg-open{{background:#ece9e3;color:#6a6256;}}
.opens{{display:flex;flex-direction:column;gap:7px;}}
.op{{background:#f7f5f0;border:1px solid #e6e2d8;border-radius:9px;padding:10px 13px;font-size:12.5px;color:#36433c;break-inside:avoid;}}
</style></head><body>{BODY}</body></html>'''

pathlib.Path("/home/claude/map_cover.html").write_text(COVER,encoding="utf-8")
pathlib.Path("/home/claude/map_body.html").write_text(DOC,encoding="utf-8")
print("wrote cover + body;", len(B), "body blocks")
