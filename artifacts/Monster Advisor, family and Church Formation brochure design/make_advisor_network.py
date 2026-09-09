import sys
sys.path.insert(0, "/home/claude/build")
from diagrams import step_chain_vertical, vertical_levels, fixed

PAGES = []
def add(html): PAGES.append(html)

def photo(caption, extra_style=""):
    return f'''<div class="photo" style="{extra_style}">
        <div class="corner tl"></div><div class="corner br"></div>
        <div class="cap">{caption}</div>
    </div>'''

def folio(chapter, num):
    return f'''<div class="folio"><div class="thread">{chapter}</div><div>{num:02d}</div></div>'''

def col_list(title, items):
    lis = "".join([f'<li>{i}</li>' for i in items])
    return f'<div class="col-block"><div class="col-title">{title}</div><ul class="col-list">{lis}</ul></div>'

def chips_static(items):
    return '<div style="display:flex; flex-wrap:wrap; gap:0.1in;">' + "".join([f'<div class="track-chip">{c}</div>' for c in items]) + '</div>'

# =================================================================
# PAGE 1 — COVER
# =================================================================
add(f'''
<div class="page navy">
  <div class="photo" style="position:absolute; inset:0; border-radius:0;">
    <div class="cap" style="right:0.68in; bottom:0.5in; left:auto; text-align:right; font-size:6.8pt;">PHOTOGRAPHY — ADVISOR IN CONVERSATION WITH A MULTI-GENERATIONAL FAMILY</div>
  </div>
  <div style="position:absolute; inset:0; background:linear-gradient(190deg, rgba(16,30,56,0.4) 0%, rgba(16,30,56,0.88) 55%, rgba(16,30,56,0.98) 100%);"></div>
  <div class="frame" style="display:flex; flex-direction:column; justify-content:flex-end;">
    <div style="font-family:'Archivo'; font-weight:600; font-size:9pt; letter-spacing:0.2em; color:#D9B876; margin-bottom:2in;">FOR CHRISTIAN FINANCIAL ADVISORS</div>
    <h1 class="display" style="font-size:26pt; color:#FBF8F1; line-height:1.15;">Build a Practice That Reflects Your Faith and Changes Families for Generations</h1>
    <div style="height:0.2in;"></div>
    <p style="font-family:'Playfair'; font-style:italic; font-weight:500; font-size:12.5pt; color:#D9B876; line-height:1.5;">
      Grow your faith. Build your practice. Serve families. Strengthen churches.
      Multiply Kingdom impact.
    </p>
    <div style="height:0.18in;"></div>
    <p class="lede" style="font-size:9.8pt; color:rgba(251,248,241,0.75);">
      A comprehensive growth, discipleship, client-engagement, family-legacy, and
      church-partnership platform created specifically for Christian financial advisors.
    </p>
    <div style="height:0.3in;"></div>
    <div style="display:flex; gap:0.3in;">
      <div class="gsm-mark"><div class="gsm-word">GROW</div><div class="gsm-sub">personally</div></div>
      <div class="gsm-mark"><div class="gsm-word">SERVE</div><div class="gsm-sub">families</div></div>
      <div class="gsm-mark"><div class="gsm-word">MULTIPLY</div><div class="gsm-sub">Kingdom impact</div></div>
    </div>
    <div style="height:0.4in;"></div>
    <div style="font-family:'Archivo'; font-weight:500; font-size:8pt; letter-spacing:0.1em; color:rgba(251,248,241,0.55);">CHRISTIAN ADVISOR NETWORK&trade;</div>
  </div>
</div>
''')

# =================================================================
# PAGE 2 — MORE THAN A PROFESSIONAL ASSOCIATION
# =================================================================
becomes = ["Stronger follower of Christ", "More effective practice leader", "Trusted guide to families", "Equipper of the next generation", "Strategic partner to pastors and churches", "Catalyst for biblical financial wisdom and generous living"]
enables = ["Personal and spiritual growth", "A differentiated, values-aligned practice", "Deeper and more meaningful client conversations", "Multi-generational family engagement", "Ethical, compliance-aware church partnerships", "Repeatable resources for every stage of service"]
add(f'''
<div class="page">
  <div class="frame">
    <div class="eyebrow">MORE THAN A PROFESSIONAL ASSOCIATION</div>
    <div style="height:0.2in;"></div>
    <h1 class="display" style="font-size:21pt; color:var(--navy);">A resource, relationship, training, and ministry ecosystem</h1>
    <div style="height:0.16in;"></div>
    <p class="lede">
      The Christian Advisor Network equips advisors with biblically sound resources they
      can use personally, professionally, with client families, and in partnership with
      local churches. It is designed to help Christian advisors become &mdash; and enable
      them to build:
    </p>
    <div style="height:0.2in;"></div>
    <div style="display:flex; gap:0.4in;">
      <div style="flex:1;">{col_list("WHO THE ADVISOR BECOMES", becomes)}</div>
      <div style="flex:1;">{col_list("WHAT THE PLATFORM ENABLES", enables)}</div>
    </div>
  </div>
  {folio("More Than a Professional Association", 2)}
</div>
''')

# =================================================================
# PAGE 3 — THE CENTRAL PROMISE
# =================================================================
kit_items = ["Advisor PDF guide", "Small-group edition", "Client-facing PDF", "Seminar edition", "Advisor preparation notes", "Church partnership edition", "Client invitation email", "Senior pastor overview", "Client conversation script", "Presentation slides", "Discovery questions", "Social media copy", "Family discussion guide", "Website copy", "Interactive worksheet", "Short video scripts", "Follow-up email", "Customizable advisor-branded edition", "Next-step recommendations", "Measurement and follow-up tools"]
kit_html = "".join([f'<div class="kit-item"><span class="kit-check">&#10003;</span>{k}</div>' for k in kit_items])
add(f'''
<div class="page">
  <div class="frame">
    <div class="eyebrow">THE CENTRAL PROMISE</div>
    <div style="height:0.16in;"></div>
    <h1 class="display" style="font-size:18pt; color:var(--navy); line-height:1.3;">Everything a Christian advisor needs to grow personally and serve families meaningfully</h1>
    <div style="height:0.12in;"></div>
    <p class="lede" style="font-size:10pt;">
      The advisor no longer has to wonder what to send, what to say, how to begin the
      conversation, or how to serve the entire family. The Network provides the answer,
      the script, the exercise, the presentation, the follow-up, and the next step.
    </p>
    <div style="height:0.18in;"></div>
    <div style="font-family:'Archivo'; font-weight:600; font-size:9pt; letter-spacing:0.12em; color:var(--gold);">FROM CONTENT TO TRANSFORMATION</div>
    <p style="font-family:'Inter'; font-size:9.4pt; color:var(--gray); margin:0.06in 0 0.14in;">Every major resource includes a complete, transferable implementation kit.</p>
    <div class="kit-grid">{kit_html}</div>
    <div style="height:0.16in;"></div>
    <div class="takeaway">
      <span class="label">One resource, many uses</span>
      Personal growth &middot; client engagement &middot; family conversations &middot; team development &middot; church ministry
    </div>
  </div>
  {folio("The Central Promise", 3)}
</div>
''')

# =================================================================
# PAGE 4 — THE COMPLETE RESOURCE RACK
# =================================================================
rack = [
    ("1. Faith &amp; Spiritual Formation", "Faith and finances, uncertainty, contentment, calling, spiritual disciplines, eternal perspective."),
    ("2. Marriage &amp; Money", "Money personalities, conflict, transparency, debt, blended families, retirement expectations."),
    ("3. Parenting &amp; Next Generation", "Wise children, generosity, responsibility, entitlement, preparing heirs, grandparent influence."),
    ("4. Family Communication &amp; Unity", "Family meetings, conflict, shared vision, governance, constitutions, councils, legacy retreats."),
    ("5. Life Purpose &amp; Calling", "Purpose, career transition, retirement identity, mentoring, life planning, multiplying a life message."),
    ("6. Financial Wisdom &amp; Stewardship", "God owns it all, margin, debt, goals, saving, investing, finish lines, gratitude and contentment."),
    ("7. Generosity &amp; Kingdom Impact", "Family giving, philanthropy, donor-advised funds, missions, foundations, legacy giving."),
    ("8. Health, Wholeness &amp; Resilience", "Stress, burnout, health crises, caregiving, Sabbath, grief, resilience, whole-life stewardship."),
    ("9. Retirement &amp; Major Transitions", "Retirement, business sale, widowhood, relocation, inheritance, empty nesting, end-of-life planning."),
    ("10. Family Legacy", "Legacy letters, family stories, faith stories, values, traditions, ethical wills, family videos."),
]
rack_html = "".join([f'<div class="rack-cell"><div class="rack-title">{t}</div><div class="rack-desc">{d}</div></div>' for t, d in rack])
add(f'''
<div class="page">
  <div class="frame">
    <div class="eyebrow">THE COMPLETE RESOURCE RACK&trade;</div>
    <div style="height:0.16in;"></div>
    <h1 class="display" style="font-size:19pt; color:var(--navy);">A biblical resource for every conversation, transition, and family need</h1>
    <div style="height:0.06in;"></div>
    <p class="lede" style="font-size:9.6pt;">Christian advisors encounter issues that go far beyond investments. The Resource Rack equips them for the whole person, the whole family, and the whole journey.</p>
    <div style="height:0.14in;"></div>
    <div class="rack-grid">{rack_html}</div>
    <div style="height:0.14in;"></div>
    <div class="takeaway">
      <span class="label">The foundation</span>
      Ron Blue&rsquo;s biblical financial wisdom + LifeTogether&rsquo;s campaign, curriculum, conversation, personalization, and churchwide implementation systems.
    </div>
  </div>
  {folio("The Complete Resource Rack", 4)}
</div>
''')

# =================================================================
# PAGE 5 — THE SEVEN BREAKTHROUGH RESOURCES (navy divider)
# =================================================================
breakthroughs = [
    ("1", "Faith &amp; Practice Alignment Assessment&trade;", "See where faith, life, family, leadership, practice, and Kingdom impact are aligned &mdash; and build a 90-day growth plan."),
    ("2", "Christian Advisor Vision &amp; Values Builder&trade;", "Create a fully custom vision, mission, values, client promise, team covenant, and ten-year legacy vision."),
    ("3", "Legacy Family Conversation System&trade;", "Turn financial-planning meetings into meaningful multi-generational conversations."),
    ("4", "Family Legacy Builder&trade;", "Help families transfer faith, wisdom, values, stories, generosity, and wealth."),
    ("5", "40-Day Christian Advisor Growth Builder&trade;", "A guided faith-and-practice journey combining spiritual formation with practical growth actions."),
    ("6", "Advisor-Church Partnership Playbook&trade;", "Serve churches with wisdom, integrity, clear boundaries, and scalable ministry pathways."),
    ("7", "Pastor Sermon &amp; Seminar Library&trade;", "Equip pastors with biblically rich, pastorally sensitive teaching on stewardship, generosity, and legacy."),
]
bt_html = "".join([f'''
    <div class="bt-row">
      <div class="bt-num">{n}</div>
      <div><div class="bt-title">{t}</div><div class="bt-desc">{d}</div></div>
    </div>''' for n, t, d in breakthroughs])
add(f'''
<div class="page navy">
  <div class="frame">
    <div class="eyebrow">THE SEVEN BREAKTHROUGH RESOURCES&trade;</div>
    <div style="height:0.18in;"></div>
    <h1 class="display" style="font-size:19pt; color:#FBF8F1;">Flagship systems that solve major advisor problems and deepen client relationships</h1>
    <div style="height:0.2in;"></div>
    {bt_html}
  </div>
  {folio("The Seven Breakthrough Resources", 5)}
</div>
''')

# =================================================================
# PAGE 6 — 1+2: ALIGN THE ADVISOR, DEFINE THE PRACTICE
# =================================================================
assessment_items = ["50-question assessment", "Automated scorecard", "Personal spiritual health", "Marriage and family alignment", "Leadership capacity", "Practice vision and client experience", "Team culture and stewardship", "Kingdom impact and church engagement", "Succession readiness", "Personal and practice recommendations", "90-day growth plan", "Coaching discussion guide"]
values_items = ["Personal calling statement", "Practice vision and mission", "Five to seven core values", "Ideal client definition", "Distinctive value proposition", "Client experience promise", "Team culture covenant", "Kingdom impact goals", "Ten-year legacy vision", "Founder story and biblical foundations", "Website and brochure copy", "Annual vision review"]
add(f'''
<div class="page">
  <div class="frame">
    <div class="eyebrow">1 + 2 &mdash; ALIGN THE ADVISOR. DEFINE THE PRACTICE.</div>
    <div style="height:0.16in;"></div>
    <h1 class="display" style="font-size:18pt; color:var(--navy);">Two foundational systems for personal clarity and organizational distinction</h1>
    <div style="height:0.16in;"></div>
    <div style="display:flex; gap:0.35in;">
      <div style="flex:1;">{col_list("FAITH &amp; PRACTICE ALIGNMENT ASSESSMENT&trade;", assessment_items)}</div>
      <div style="flex:1;">{col_list("VISION &amp; VALUES BUILDER&trade;", values_items)}</div>
    </div>
    <div style="height:0.16in;"></div>
    <div class="takeaway">
      <span class="label">Custom, branded, and ready to use</span>
      Each advisor can receive a polished, advisor-branded document: <i>The Vision and Values of [Practice Name].</i>
    </div>
    <div style="height:0.12in;"></div>
    <div class="takeaway">
      <span class="label">Client adaptation</span>
      The Whole-Life Stewardship Assessment&trade; opens a meaningful conversation about faith, family, finances, health, purpose, generosity, future, and legacy.
    </div>
  </div>
  {folio("Align the Advisor, Define the Practice", 6)}
</div>
''')

# =================================================================
# PAGE 7 — 3+4: TURN PLANNING INTO LEGACY
# =================================================================
legacy_conv_items = ["100 Legacy Questions", "Family Values Card Sort", "Legacy Timeline", "Family Story Interview", "Family Mission Builder", "Family Generosity Map", "Family Wisdom Inventory", "Next-Generation Readiness Assessment", "Family Meeting Agenda", "Annual Legacy Review"]
legacy_builder_items = ["1. Remember Your Story", "2. Clarify Your Values", "3. Define Your Purpose", "4. Prepare the Next Generation", "5. Build a Generosity Legacy", "6. Create the Family Legacy Plan", "Mission statement and legacy letter", "Family meeting rhythm", "Next-generation development plan", "Annual retreat and ten-year vision"]
add(f'''
<div class="page navy">
  <div class="frame">
    <div class="eyebrow">3 + 4 &mdash; TURN PLANNING INTO LEGACY</div>
    <div style="height:0.16in;"></div>
    <h1 class="display" style="font-size:18pt; color:#FBF8F1;">Move beyond asset transfer to the transfer of wisdom, faith, values, stories, and responsibility</h1>
    <div style="height:0.14in;"></div>
    <div class="pull-quote" style="font-size:12pt; color:#FBF8F1;"><span class="mark">&ldquo;</span>Most financial planning focuses on what your family will receive. We also want to help you think about what your family will remember, what they will believe, and how they will be prepared.<span class="mark">&rdquo;</span></div>
    <div style="height:0.18in;"></div>
    <div style="display:flex; gap:0.35in;">
      <div style="flex:1;">{col_list("LEGACY FAMILY CONVERSATION SYSTEM&trade;", legacy_conv_items)}</div>
      <div style="flex:1;">{col_list("FAMILY LEGACY BUILDER&trade; &mdash; SIX MOVEMENTS", legacy_builder_items)}</div>
    </div>
    <div style="height:0.14in;"></div>
    <div class="takeaway">
      <span class="label">The difference</span>
      The advisor becomes more than a manager of money. The advisor becomes a trusted guide who helps families prepare people, preserve unity, and build what lasts.
    </div>
  </div>
  {folio("Turn Planning into Legacy", 7)}
</div>
''')

# =================================================================
# PAGE 8 — 5: THE 40-DAY CHRISTIAN ADVISOR GROWTH BUILDER
# =================================================================
growth_areas = ["Faith and spiritual formation", "Personal leadership", "Practice growth", "Client relationships", "Family legacy", "Kingdom and church impact"]
daily_includes = ["Scripture", "Devotional teaching", "Advisor reflection", "Personal application", "Practice-building action", "Client conversation idea", "Prayer", "Team discussion option"]
supporting = ["40 daily devotionals", "Six weekly videos", "Six masterclasses", "Small-group guide", "Coaching guide", "Team edition", "Implementation workbook", "90-day growth plan", "Advisor accountability groups"]
add(f'''
<div class="page">
  <div class="frame">
    <div class="eyebrow">5 &mdash; THE 40-DAY CHRISTIAN ADVISOR GROWTH BUILDER&trade;</div>
    <div style="height:0.16in;"></div>
    <h1 class="display" style="font-size:19pt; color:var(--navy);">A faith-and-practice-building journey</h1>
    <div style="height:0.1in;"></div>
    <p class="lede" style="font-size:9.8pt;">Forty days of spiritual formation, personal leadership, practice growth, client service, family legacy, and Kingdom impact.</p>
    <div style="height:0.14in;"></div>
    <div style="display:flex; gap:0.35in;">
      <div style="flex:1;">{col_list("SIX AREAS OF GROWTH", growth_areas)}</div>
      <div style="flex:1;">{col_list("EACH DAY INCLUDES", daily_includes)}</div>
    </div>
    <div style="height:0.16in;"></div>
    <div style="font-family:'Archivo'; font-weight:600; font-size:9pt; letter-spacing:0.12em; color:var(--gold); margin-bottom:0.1in;">THE SUPPORTING SYSTEM</div>
    {chips_static(supporting)}
    <div style="height:0.14in;"></div>
    <p style="font-family:'Inter'; font-style:italic; font-size:9.6pt; color:var(--gray);">Not inspiration alone &mdash; a repeatable growth rhythm that produces action, accountability, and implementation.</p>
  </div>
  {folio("The 40-Day Christian Advisor Growth Builder", 8)}
</div>
''')

# =================================================================
# PAGE 9 — 6: THE ADVISOR-CHURCH PARTNERSHIP PLAYBOOK
# =================================================================
pastor_fears = ["Prospecting disguised as ministry", "Implied endorsement of a business", "Pressure on church members", "Transactional financial content", "Unclear biblical or ministry alignment", "Targeting wealthy families", "Loss of control or confidentiality"]
advisor_fears = ["Being viewed as salespeople", "Unclear expectations and boundaries", "Low pastor engagement", "Compliance concerns", "Investing time without support", "Competing advisors", "Being expected to provide unlimited free work"]
add(f'''
<div class="page">
  <div class="frame">
    <div class="eyebrow">6 &mdash; THE CHRISTIAN ADVISOR-CHURCH PARTNERSHIP PLAYBOOK&trade;</div>
    <div style="height:0.16in;"></div>
    <h1 class="display" style="font-size:18pt; color:var(--navy);">Serve pastors and churches with wisdom, integrity, and clear boundaries</h1>
    <div style="height:0.16in;"></div>
    <div style="display:flex; gap:0.35in;">
      <div style="flex:1;">{col_list("WHAT PASTORS FEAR", pastor_fears)}</div>
      <div style="flex:1;">{col_list("WHAT ADVISORS FEAR", advisor_fears)}</div>
    </div>
    <div style="height:0.16in;"></div>
    <div class="takeaway">
      <span class="label">The partnership covenant</span>
      No selling from the platform &middot; No church-member lists &middot; No product promotion &middot; No implied endorsement &middot; Clear compliance standards &middot; Pastor oversight &middot; Voluntary participation &middot; Confidentiality &middot; Transparent expectations &middot; Family-first service
    </div>
    <div style="height:0.14in;"></div>
    <div class="pull-quote" style="font-size:13pt;">Ministry first. Relationships second. <span class="mark">Business outcomes, when appropriate, emerge through trust &mdash; never pressure.</span></div>
  </div>
  {folio("The Advisor-Church Partnership Playbook", 9)}
</div>
''')

# =================================================================
# PAGE 10 — FIVE LEVELS OF CHURCH PARTNERSHIP
# =================================================================
partnership_levels = [
    ("1", "Resource Provider", "Articles, devotionals, PDFs, family conversation guides, sermon-support resources."),
    ("2", "Seminar Partner", "Financial wisdom, retirement, family legacy, generosity, and estate-planning education."),
    ("3", "Small-Group Partner", "Six-week studies, 21-day challenges, 40-day campaigns, legacy and generous-living groups."),
    ("4", "Ministry Builder", "Financial wisdom, legacy family, generosity, business owner, widow, and young-family ministries."),
    ("5", "Strategic Ministry Partner", "An annual plan with campaigns, training, workshops, ministry measurement, and leadership planning."),
]
add(f'''
<div class="page">
  <div class="frame">
    <div class="eyebrow">FIVE LEVELS OF CHURCH PARTNERSHIP</div>
    <div style="height:0.16in;"></div>
    <h1 class="display" style="font-size:19pt; color:var(--navy);">Begin with service. Build trust. Expand only when ministry value is proven.</h1>
    <div style="height:0.1in;"></div>
    <div style="text-align:center;">{fixed(vertical_levels(partnership_levels), 7.1, 5.1)}</div>
    <div style="height:0.1in;"></div>
    <div class="takeaway">
      <span class="label">A good first pilot</span>
      7 Days of Financial Wisdom &middot; Marriage and Money Seminar &middot; Family Legacy Workshop &middot; Retirement with Purpose &middot; Generosity Conversation Night &middot; Business Owner Stewardship Roundtable
    </div>
  </div>
  {folio("Five Levels of Church Partnership", 10)}
</div>
''')

# =================================================================
# PAGE 11 — 7: THE PASTOR SERMON & SEMINAR LIBRARY
# =================================================================
sermon_cats = [
    ("God Owns It All", "The Owner and the Manager &middot; Freedom from Control &middot; Faithful with What Is in Your Hands &middot; Living for What Lasts"),
    ("Financial Wisdom for Real Life", "Wisdom Before Wealth &middot; The Freedom of Margin &middot; Debt, Desire, and Discipline &middot; Generosity That Changes the Heart"),
    ("The Generous Life", "The God Who Gives &middot; Rich Toward God &middot; Giving as Worship &middot; A Family Culture of Generosity"),
    ("Built for Legacy", "What Are You Really Leaving? &middot; Tell the Next Generation &middot; Passing Wisdom Before Wealth &middot; Finishing Faithfully"),
    ("Faith, Family &amp; Finances", "Marriage and Money &middot; Teaching Children to Steward &middot; Preparing Rather Than Entitling &middot; A Family on Mission"),
    ("Wisdom for Every Season", "Trusting God in Transition &middot; Purpose Beyond Your Profession &middot; Caring for Aging Parents &middot; Finishing Well"),
]
sermon_html = "".join([f'<div class="exp-row"><div class="exp-name">{t}</div><div class="exp-desc">{d}</div></div>' for t, d in sermon_cats])
add(f'''
<div class="page">
  <div class="frame">
    <div class="eyebrow">7 &mdash; THE PASTOR SERMON &amp; SEMINAR LIBRARY&trade;</div>
    <div style="height:0.14in;"></div>
    <h1 class="display" style="font-size:18pt; color:var(--navy);">Biblically rich, pastorally sensitive, transformational teaching resources</h1>
    <div style="height:0.12in;"></div>
    {sermon_html}
    <div style="height:0.14in;"></div>
    <div class="takeaway">
      <span class="label">Not generic financial talks</span>
      Resources help pastors preach biblical truth with clarity while giving families practical next steps for stewardship, generosity, unity, preparation, and legacy.
    </div>
  </div>
  {folio("The Pastor Sermon & Seminar Library", 11)}
</div>
''')

# =================================================================
# PAGE 12 — A SEMINAR FOR EVERY SEASON
# =================================================================
seminars = ["God Owns It All", "Financial Wisdom for Families", "Marriage and Money", "Raising Financially Wise Children", "Preparing Children for Wealth", "Retirement with Purpose", "Biblical Estate Planning", "Family Legacy Planning", "Generous Living", "Giving as a Family", "Navigating Financial Anxiety", "Caring for Aging Parents", "Wisdom for Widows", "Selling a Business Well", "Avoiding Family Conflict Around Inheritance", "Creating a Family Mission Statement", "Stewardship for Business Owners", "Legacy Letters and Family Stories", "Faith-Based Investing", "The Purpose of Prosperity", "Building a Multi-Generational Family Vision"]
sem_html = "".join([f'<div class="aud-cell">{s}</div>' for s in seminars])
add(f'''
<div class="page">
  <div class="frame">
    <div class="eyebrow">A SEMINAR FOR EVERY SEASON</div>
    <div style="height:0.16in;"></div>
    <h1 class="display" style="font-size:19pt; color:var(--navy);">Turn trusted teaching into practical family action</h1>
    <div style="height:0.14in;"></div>
    <div class="aud-grid">{sem_html}</div>
    <div style="height:0.16in;"></div>
    <div class="takeaway">
      <span class="label">Every seminar includes</span>
      Pastor introduction &middot; Biblical foundation &middot; Advisor notes &middot; Participant workbook &middot; Discussion questions &middot; Exercises &middot; Next steps &middot; Follow-up resources &middot; Compliance-safe language &middot; No-sales policy
    </div>
  </div>
  {folio("A Seminar for Every Season", 12)}
</div>
''')

# =================================================================
# PAGE 13 — HOW TO PARTNER WITH A LOCAL CHURCH
# =================================================================
partner_steps = [
    ("BEGIN WITH SERVICE, NOT SALES", "Ask what pressures families face and what support the church needs."),
    ("LEARN THE PASTOR'S VISION", "Understand mission, discipleship, sermon calendar, groups, generosity philosophy, and concerns."),
    ("OFFER ONE PRACTICAL RESOURCE", "Start with a useful article, devotional, worksheet, research packet, or client-neutral seminar."),
    ("ESTABLISH BOUNDARIES", "Clarify roles, privacy, referrals, branding, compliance, follow-up, and financial responsibilities."),
    ("PILOT A SMALL EXPERIENCE", "Launch a low-risk, high-value event or short journey."),
    ("MEASURE MINISTRY OUTCOMES", "Track participation, family conversations, completed exercises, and transformation stories &mdash; not only leads."),
    ("BUILD AN ANNUAL PLAN", "Create a four-quarter rhythm around wisdom, family, purpose, generosity, legacy, and year-end giving."),
]
add(f'''
<div class="page navy">
  <div class="frame">
    <div class="eyebrow">HOW TO PARTNER WITH A LOCAL CHURCH</div>
    <div style="height:0.12in;"></div>
    <h1 class="display" style="font-size:18pt; color:#FBF8F1;">A seven-step pathway from first conversation to annual ministry plan</h1>
    <div style="height:0.1in;"></div>
    <div style="text-align:center;">{fixed(step_chain_vertical(partner_steps), 7.1, 6.6)}</div>
  </div>
  {folio("How to Partner with a Local Church", 13)}
</div>
''')

# =================================================================
# PAGE 14 — ONE NETWORK, FIVE GROWTH PATHWAYS
# =================================================================
pathways = [
    ("Grow Yourself", "40-Day Growth Builder &middot; Alignment Assessment &middot; Spiritual formation &middot; Advisor devotionals"),
    ("Grow Your Practice", "Practice Builder &middot; Vision and Values &middot; Marketing &middot; Client experience &middot; Team &middot; Succession"),
    ("Serve Families", "Family Legacy Builder &middot; Conversation guides &middot; Workshops &middot; Next generation &middot; Generosity &middot; Transitions"),
    ("Partner with Churches", "Playbook &middot; Pastor resources &middot; Sermons &middot; Seminars &middot; Small groups &middot; Campaigns &middot; Ministry systems"),
    ("Build Community", "Advisor groups &middot; Coaching &middot; Masterclasses &middot; Events &middot; Certification &middot; Regional networks"),
]
path_html = "".join([f'<div class="offer-card" style="margin-bottom:0.18in;"><div style="width:26px;height:2px;background:var(--gold);margin-bottom:0.1in;"></div><div style="font-family:\'Playfair\'; font-weight:700; font-size:13.5pt; color:var(--navy);">{t}</div><div style="font-family:\'Inter\'; font-size:9.2pt; color:var(--ink); margin-top:0.06in; line-height:1.5;">{d}</div></div>' for t, d in pathways])
add(f'''
<div class="page">
  <div class="frame">
    <div class="eyebrow">ONE NETWORK. FIVE GROWTH PATHWAYS.</div>
    <div style="height:0.16in;"></div>
    <h1 class="display" style="font-size:19pt; color:var(--navy);">A clear member experience built around the advisor&rsquo;s real work</h1>
    <div style="height:0.16in;"></div>
    {path_html}
    <div style="height:0.1in;"></div>
    <div class="takeaway">
      <span class="label">Homepage message</span>
      Build a Practice That Reflects Your Faith and Changes Families for Generations. The growth, client-engagement, family-legacy, and church-partnership platform built specifically for Christian financial advisors.
    </div>
  </div>
  {folio("One Network, Five Growth Pathways", 14)}
</div>
''')

# =================================================================
# PAGE 15 — THE STRATEGIC ADVANTAGE
# =================================================================
most_provide = ["Practice management", "Investment platforms", "Compliance", "Technology", "Marketing", "Networking"]
network_adds = ["Spiritual formation", "Biblically sound financial wisdom", "Transferable client conversation tools", "Family legacy and next-generation resources", "Marriage and family content", "Generosity tools", "Church partnership systems", "Pastor sermon support", "Customizable campaigns", "Advisor-branded family journeys"]
add(f'''
<div class="page navy">
  <div class="frame">
    <div class="eyebrow">THE STRATEGIC ADVANTAGE</div>
    <div style="height:0.16in;"></div>
    <h1 class="display" style="font-size:19pt; color:#FBF8F1;">What traditional advisor networks provide &mdash; and what is usually missing</h1>
    <div style="height:0.16in;"></div>
    <div style="display:flex; gap:0.35in;">
      <div style="flex:1;">{col_list("MOST ADVISOR NETWORKS PROVIDE", most_provide)}</div>
      <div style="flex:1;">{col_list("THE CHRISTIAN ADVISOR NETWORK ADDS", network_adds)}</div>
    </div>
    <div style="height:0.16in;"></div>
    <div class="takeaway">
      <span class="label">A differentiated promise</span>
      We help Christian advisors grow personally, build thriving practices, deepen client relationships, serve entire families, partner with churches, and multiply Kingdom impact.
    </div>
    <div style="height:0.12in;"></div>
    <p style="font-family:'Archivo'; font-weight:500; font-size:8.4pt; letter-spacing:0.04em; color:rgba(251,248,241,0.55); line-height:1.7;">
      BRAND ARCHITECTURE: Christian Advisor Network&trade; &middot; Christian Advisor Growth Builder&trade; &middot;
      Christian Advisor Practice Builder&trade; &middot; Family Legacy Builder&trade; &middot; Financial Wisdom Ministry&trade; &middot;
      Pastor and Church Resource Library&trade; &middot; Trusted Guide Academy&trade;
    </p>
  </div>
  {folio("The Strategic Advantage", 15)}
</div>
''')

# =================================================================
# PAGE 16 — CLOSING: ULTIMATE ADVISOR MEMBERSHIP PROMISE
# =================================================================
promises = [
    "Something meaningful to send every client",
    "Something useful to discuss in every meeting",
    "Something timely for every family transition",
    "Something biblically sound for every financial question",
    "Something valuable for every generation",
    "Something practical to offer every pastor",
    "Something transformational to launch in every church",
]
promise_html = "".join([f'<div class="check-item-navy"><span class="check-mark">&#10003;</span>{p}</div>' for p in promises])
add(f'''
<div class="page navy">
  <div class="photo" style="position:absolute; inset:0; border-radius:0;">
    <div class="cap" style="right:0.68in; bottom:0.5in; left:auto; text-align:right; font-size:6.8pt;">PHOTOGRAPHY — ADVISOR'S OFFICE, WARM LIGHT, FAMILY PHOTO ON DESK</div>
  </div>
  <div style="position:absolute; inset:0; background:linear-gradient(190deg, rgba(16,30,56,0.5) 0%, rgba(16,30,56,0.92) 55%, rgba(16,30,56,0.98) 100%);"></div>
  <div class="frame" style="display:flex; flex-direction:column; justify-content:flex-end;">
    <div class="eyebrow">THE ULTIMATE ADVISOR MEMBERSHIP PROMISE</div>
    <div style="height:0.16in;"></div>
    <h1 class="display" style="font-size:20pt; color:#FBF8F1;">Something meaningful for every client, every family, every transition, and every church.</h1>
    <div style="height:0.16in;"></div>
    {promise_html}
    <div style="height:0.24in;"></div>
    <div class="takeaway">
      <span class="label">Join the Network</span>
      Grow Your Faith. Grow Your Practice. Grow Your Impact.
    </div>
  </div>
  {folio("The Ultimate Advisor Membership Promise", 16)}
</div>
''')

# =================================================================
# PAGE 17 — BACK COVER
# =================================================================
add(f'''
<div class="page navy">
  <div class="frame" style="display:flex; flex-direction:column; justify-content:space-between; align-items:center; text-align:center;">
    <div></div>
    <div>
      <div style="font-family:'Archivo'; font-weight:600; font-size:9.5pt; letter-spacing:0.24em; color:#D9B876;">CHRISTIAN ADVISOR NETWORK&trade;</div>
      <div style="height:0.26in;"></div>
      <h1 class="display" style="font-size:20pt; color:#FBF8F1;">Faithful Advisors. Flourishing Practices.<br/>Stronger Families. Healthier Churches.<br/>Lasting Legacies.</h1>
      <div style="height:0.3in;"></div>
      <div style="width:30px; height:2px; background:#B98D3E; margin:0 auto;"></div>
      <div style="height:0.2in;"></div>
      <div style="font-family:'Archivo'; font-weight:500; font-size:9pt; letter-spacing:0.08em; color:rgba(251,248,241,0.75);">LIFETOGETHER.COM &nbsp;&middot;&nbsp; BRETT@LIFETOGETHER.COM</div>
    </div>
    <div style="font-family:'Archivo'; font-weight:500; font-size:7.4pt; letter-spacing:0.1em; color:rgba(251,248,241,0.4);">A LIFETOGETHER PLATFORM</div>
  </div>
</div>
''')

# =================================================================
# ASSEMBLE
# =================================================================
with open("/home/claude/build/portrait_style.css") as f:
    base_css = f.read()

extra_css = '''
.gsm-mark{ text-align:center; }
.gsm-word{ font-family:'Playfair'; font-weight:700; font-size:15pt; color:#D9B876; letter-spacing:0.04em; }
.gsm-sub{ font-family:'Archivo'; font-weight:500; font-size:8pt; letter-spacing:0.06em; color:rgba(251,248,241,0.65); margin-top:0.03in; }

.col-block{ }
.col-title{ font-family:'Archivo'; font-weight:700; font-size:9pt; letter-spacing:0.1em; color:var(--gold); margin-bottom:0.12in; }
.dark .col-title, .page.navy .col-title{ color:var(--gold-bright); }
.col-list{ list-style:none; }
.col-list li{ font-family:'Inter'; font-size:9.2pt; color:var(--ink); line-height:1.5; padding:0.06in 0; border-top:1px solid var(--line); position:relative; padding-left:0.16in; }
.col-list li::before{ content:'\\2013'; position:absolute; left:0; color:var(--gold); }
.page.navy .col-list li{ color:rgba(251,248,241,0.88); border-top:1px solid rgba(217,184,118,0.25); }

.kit-grid{ display:grid; grid-template-columns:1fr 1fr; gap:0.05in 0.2in; }
.kit-item{ display:flex; align-items:baseline; gap:0.1in; font-family:'Inter'; font-size:8.6pt; color:var(--ink); padding:0.04in 0; }
.kit-check{ color:var(--gold); font-weight:700; }

.rack-grid{ display:grid; grid-template-columns:1fr 1fr; gap:0.14in 0.2in; }
.rack-cell{ background:var(--cream); border-left:3px solid var(--gold); padding:0.14in 0.16in; }
.rack-title{ font-family:'Playfair'; font-weight:700; font-size:10.3pt; color:var(--navy); margin-bottom:0.04in; line-height:1.2; }
.rack-desc{ font-family:'Inter'; font-size:8pt; color:var(--ink); line-height:1.4; }

.bt-row{ display:flex; gap:0.2in; padding:0.14in 0; border-top:1px solid rgba(217,184,118,0.25); }
.bt-row:first-child{ border-top:none; padding-top:0; }
.bt-num{ font-family:'Playfair'; font-weight:700; font-size:18pt; color:var(--gold); width:0.4in; flex-shrink:0; }
.bt-title{ font-family:'Playfair'; font-weight:700; font-size:12pt; color:#FBF8F1; margin-bottom:0.04in; line-height:1.25; }
.bt-desc{ font-family:'Inter'; font-size:9pt; color:rgba(251,248,241,0.78); line-height:1.5; }

.check-item-navy{ display:flex; align-items:baseline; gap:0.12in; padding:0.07in 0; border-top:1px solid rgba(217,184,118,0.25); font-family:'Inter'; font-size:9.6pt; color:rgba(251,248,241,0.92); }
.check-item-navy:first-child{ border-top:none; }
.check-item-navy .check-mark{ color:var(--gold-bright); font-weight:700; }
'''

html = f'''<!DOCTYPE html>
<html><head><meta charset="utf-8">
<style>{base_css}{extra_css}</style></head>
<body>{"".join(PAGES)}</body></html>'''

with open("/home/claude/build/advisor_network.html", "w") as f:
    f.write(html)
print("Pages:", len(PAGES))
