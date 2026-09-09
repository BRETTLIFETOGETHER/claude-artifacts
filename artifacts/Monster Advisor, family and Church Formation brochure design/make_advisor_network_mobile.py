import sys
sys.path.insert(0, "/home/claude/build/mobile")
from components import *

S = []
def add(h): S.append(h)

add(hero(
    "FOR CHRISTIAN FINANCIAL ADVISORS",
    "Build a Practice That Reflects Your Faith and Changes Families for Generations",
    "Grow your faith. Build your practice. Serve families. Strengthen churches. Multiply Kingdom impact.",
    '<p class="hero-sub">A comprehensive growth, discipleship, client-engagement, family-legacy, and church-partnership platform created specifically for Christian financial advisors.</p>'
))

becomes = ["Stronger follower of Christ", "More effective practice leader", "Trusted guide to families", "Equipper of the next generation", "Strategic partner to pastors and churches", "Catalyst for biblical financial wisdom and generous living"]
enables = ["Personal and spiritual growth", "A differentiated, values-aligned practice", "Deeper and more meaningful client conversations", "Multi-generational family engagement", "Ethical, compliance-aware church partnerships", "Repeatable resources for every stage of service"]
add(section(f'''
  {eyebrow("MORE THAN A PROFESSIONAL ASSOCIATION")}
  <h2>A resource, relationship, training, and ministry ecosystem</h2>
  <p>The Christian Advisor Network equips advisors with biblically sound resources they
  can use personally, professionally, with client families, and in partnership with
  local churches.</p>
  {titled_list("Who the advisor becomes", becomes)}
  {titled_list("What the platform enables", enables)}
'''))

kit_items = ["Advisor PDF guide", "Small-group edition", "Client-facing PDF", "Seminar edition", "Advisor preparation notes", "Church partnership edition", "Client invitation email", "Senior pastor overview", "Client conversation script", "Presentation slides", "Discovery questions", "Social media copy", "Family discussion guide", "Website copy", "Interactive worksheet", "Short video scripts", "Follow-up email", "Customizable advisor-branded edition", "Next-step recommendations", "Measurement and follow-up tools"]
add(section(f'''
  {eyebrow("THE CENTRAL PROMISE")}
  <h2 class="on-dark">Everything a Christian advisor needs to grow personally and serve families meaningfully</h2>
  <p class="on-dark-p">The advisor no longer has to wonder what to send, what to say, how
  to begin the conversation, or how to serve the entire family. The Network provides the
  answer, the script, the exercise, the presentation, the follow-up, and the next step.</p>
  <p class="on-dark-p"><b>From content to transformation</b> &mdash; every major resource
  includes a complete, transferable implementation kit:</p>
  {chips(kit_items)}
  {takeaway("One resource, many uses", "Personal growth &middot; client engagement &middot; family conversations &middot; team development &middot; church ministry")}
''', dark=True))

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
rack_html = "".join([f'<div class="exp-row"><div class="exp-name">{t}</div><div class="exp-desc">{d}</div></div>' for t, d in rack])
add(section(f'''
  {eyebrow("THE COMPLETE RESOURCE RACK&trade;")}
  <h2>A biblical resource for every conversation, transition, and family need</h2>
  <p>Christian advisors encounter issues that go far beyond investments. The Resource
  Rack equips them for the whole person, the whole family, and the whole journey.</p>
  {rack_html}
  {takeaway("The foundation", "Ron Blue&rsquo;s biblical financial wisdom + LifeTogether&rsquo;s campaign, curriculum, conversation, personalization, and churchwide implementation systems.")}
'''))

breakthroughs = [
    ("1", "Faith &amp; Practice Alignment Assessment&trade;", "See where faith, life, family, leadership, practice, and Kingdom impact are aligned &mdash; and build a 90-day growth plan."),
    ("2", "Christian Advisor Vision &amp; Values Builder&trade;", "Create a fully custom vision, mission, values, client promise, team covenant, and ten-year legacy vision."),
    ("3", "Legacy Family Conversation System&trade;", "Turn financial-planning meetings into meaningful multi-generational conversations."),
    ("4", "Family Legacy Builder&trade;", "Help families transfer faith, wisdom, values, stories, generosity, and wealth."),
    ("5", "40-Day Christian Advisor Growth Builder&trade;", "A guided faith-and-practice journey combining spiritual formation with practical growth actions."),
    ("6", "Advisor-Church Partnership Playbook&trade;", "Serve churches with wisdom, integrity, clear boundaries, and scalable ministry pathways."),
    ("7", "Pastor Sermon &amp; Seminar Library&trade;", "Equip pastors with biblically rich, pastorally sensitive teaching on stewardship, generosity, and legacy."),
]
bt_html = "".join([f'<div class="numstep"><div class="numstep-n">{n}</div><div><div class="numstep-t">{t}</div><div class="numstep-d">{d}</div></div></div>' for n, t, d in breakthroughs])
add(section(f'''
  {eyebrow("THE SEVEN BREAKTHROUGH RESOURCES&trade;")}
  <h2>Flagship systems that solve major advisor problems and deepen client relationships</h2>
  {bt_html}
'''))

assessment_items = ["50-question assessment", "Automated scorecard", "Personal spiritual health", "Marriage and family alignment", "Leadership capacity", "Practice vision and client experience", "Team culture and stewardship", "Kingdom impact and church engagement", "Succession readiness", "Personal and practice recommendations", "90-day growth plan", "Coaching discussion guide"]
values_items = ["Personal calling statement", "Practice vision and mission", "Five to seven core values", "Ideal client definition", "Distinctive value proposition", "Client experience promise", "Team culture covenant", "Kingdom impact goals", "Ten-year legacy vision", "Founder story and biblical foundations", "Website and brochure copy", "Annual vision review"]
add(section(f'''
  {eyebrow("1 + 2 &middot; ALIGN THE ADVISOR, DEFINE THE PRACTICE")}
  <h2>Two foundational systems for personal clarity and organizational distinction</h2>
  {titled_list("Faith &amp; Practice Alignment Assessment&trade;", assessment_items)}
  {titled_list("Vision &amp; Values Builder&trade;", values_items)}
  {takeaway("Custom, branded, and ready to use", "Each advisor can receive a polished, advisor-branded document: <i>The Vision and Values of [Practice Name].</i>")}
  {takeaway("Client adaptation", "The Whole-Life Stewardship Assessment&trade; opens a meaningful conversation about faith, family, finances, health, purpose, generosity, future, and legacy.")}
'''))

legacy_conv_items = ["100 Legacy Questions", "Family Values Card Sort", "Legacy Timeline", "Family Story Interview", "Family Mission Builder", "Family Generosity Map", "Family Wisdom Inventory", "Next-Generation Readiness Assessment", "Family Meeting Agenda", "Annual Legacy Review"]
legacy_builder_items = ["1. Remember Your Story", "2. Clarify Your Values", "3. Define Your Purpose", "4. Prepare the Next Generation", "5. Build a Generosity Legacy", "6. Create the Family Legacy Plan", "Mission statement and legacy letter", "Family meeting rhythm", "Next-generation development plan", "Annual retreat and ten-year vision"]
add(section(f'''
  {eyebrow("3 + 4 &middot; TURN PLANNING INTO LEGACY")}
  <h2 class="on-dark">Move beyond asset transfer to the transfer of wisdom, faith, values, stories, and responsibility</h2>
  {pull_quote('&ldquo;Most financial planning focuses on what your family will receive. We also want to help you think about what your family will remember, what they will believe, and how they will be prepared.&rdquo;')}
  {titled_list("Legacy Family Conversation System&trade;", legacy_conv_items)}
  {titled_list("Family Legacy Builder&trade; &mdash; Six Movements", legacy_builder_items)}
  {takeaway("The difference", "The advisor becomes more than a manager of money. The advisor becomes a trusted guide who helps families prepare people, preserve unity, and build what lasts.")}
''', dark=True))

growth_areas = ["Faith and spiritual formation", "Personal leadership", "Practice growth", "Client relationships", "Family legacy", "Kingdom and church impact"]
daily_includes = ["Scripture", "Devotional teaching", "Advisor reflection", "Personal application", "Practice-building action", "Client conversation idea", "Prayer", "Team discussion option"]
supporting = ["40 daily devotionals", "Six weekly videos", "Six masterclasses", "Small-group guide", "Coaching guide", "Team edition", "Implementation workbook", "90-day growth plan", "Advisor accountability groups"]
add(section(f'''
  {eyebrow("5 &middot; THE 40-DAY CHRISTIAN ADVISOR GROWTH BUILDER&trade;")}
  <h2>A faith-and-practice-building journey</h2>
  <p>Forty days of spiritual formation, personal leadership, practice growth, client
  service, family legacy, and Kingdom impact.</p>
  {titled_list("Six areas of growth", growth_areas)}
  {titled_list("Each day includes", daily_includes)}
  <p><b>The supporting system:</b></p>
  {chips(supporting)}
  <p class="fine-print">Not inspiration alone &mdash; a repeatable growth rhythm that produces action, accountability, and implementation.</p>
'''))

pastor_fears = ["Prospecting disguised as ministry", "Implied endorsement of a business", "Pressure on church members", "Transactional financial content", "Unclear biblical or ministry alignment", "Targeting wealthy families", "Loss of control or confidentiality"]
advisor_fears = ["Being viewed as salespeople", "Unclear expectations and boundaries", "Low pastor engagement", "Compliance concerns", "Investing time without support", "Competing advisors", "Being expected to provide unlimited free work"]
add(section(f'''
  {eyebrow("6 &middot; THE ADVISOR-CHURCH PARTNERSHIP PLAYBOOK&trade;")}
  <h2>Serve pastors and churches with wisdom, integrity, and clear boundaries</h2>
  {titled_list("What pastors fear", pastor_fears)}
  {titled_list("What advisors fear", advisor_fears)}
  {takeaway("The partnership covenant", "No selling from the platform &middot; No church-member lists &middot; No product promotion &middot; No implied endorsement &middot; Clear compliance standards &middot; Pastor oversight &middot; Voluntary participation &middot; Confidentiality &middot; Transparent expectations &middot; Family-first service")}
  {pull_quote('Ministry first. Relationships second. <span class="gold">Business outcomes, when appropriate, emerge through trust &mdash; never pressure.</span>')}
'''))

partnership_levels = [
    ("RESOURCE PROVIDER", "Articles, devotionals, PDFs, family conversation guides, sermon-support resources."),
    ("SEMINAR PARTNER", "Financial wisdom, retirement, family legacy, generosity, and estate-planning education."),
    ("SMALL-GROUP PARTNER", "Six-week studies, 21-day challenges, 40-day campaigns, legacy and generous-living groups."),
    ("MINISTRY BUILDER", "Financial wisdom, legacy family, generosity, business owner, widow, and young-family ministries."),
    ("STRATEGIC MINISTRY PARTNER", "An annual plan with campaigns, training, workshops, ministry measurement, and leadership planning."),
]
add(section(f'''
  {eyebrow("FIVE LEVELS OF CHURCH PARTNERSHIP")}
  <h2 class="on-dark">Begin with service. Build trust. Expand only when ministry value is proven.</h2>
  {stack_steps(partnership_levels)}
  {takeaway("A good first pilot", "7 Days of Financial Wisdom &middot; Marriage and Money Seminar &middot; Family Legacy Workshop &middot; Retirement with Purpose &middot; Generosity Conversation Night &middot; Business Owner Stewardship Roundtable")}
''', dark=True))

sermon_cats = [
    ("God Owns It All", "The Owner and the Manager &middot; Freedom from Control &middot; Faithful with What Is in Your Hands &middot; Living for What Lasts"),
    ("Financial Wisdom for Real Life", "Wisdom Before Wealth &middot; The Freedom of Margin &middot; Debt, Desire, and Discipline &middot; Generosity That Changes the Heart"),
    ("The Generous Life", "The God Who Gives &middot; Rich Toward God &middot; Giving as Worship &middot; A Family Culture of Generosity"),
    ("Built for Legacy", "What Are You Really Leaving? &middot; Tell the Next Generation &middot; Passing Wisdom Before Wealth &middot; Finishing Faithfully"),
    ("Faith, Family &amp; Finances", "Marriage and Money &middot; Teaching Children to Steward &middot; Preparing Rather Than Entitling &middot; A Family on Mission"),
    ("Wisdom for Every Season", "Trusting God in Transition &middot; Purpose Beyond Your Profession &middot; Caring for Aging Parents &middot; Finishing Well"),
]
sermon_html = "".join([f'<div class="exp-row"><div class="exp-name">{t}</div><div class="exp-desc">{d}</div></div>' for t, d in sermon_cats])
add(section(f'''
  {eyebrow("7 &middot; THE PASTOR SERMON &amp; SEMINAR LIBRARY&trade;")}
  <h2>Biblically rich, pastorally sensitive, transformational teaching resources</h2>
  {sermon_html}
  {takeaway("Not generic financial talks", "Resources help pastors preach biblical truth with clarity while giving families practical next steps for stewardship, generosity, unity, preparation, and legacy.")}
'''))

seminars = ["God Owns It All", "Financial Wisdom for Families", "Marriage and Money", "Raising Financially Wise Children", "Preparing Children for Wealth", "Retirement with Purpose", "Biblical Estate Planning", "Family Legacy Planning", "Generous Living", "Giving as a Family", "Navigating Financial Anxiety", "Caring for Aging Parents", "Wisdom for Widows", "Selling a Business Well", "Avoiding Family Conflict Around Inheritance", "Creating a Family Mission Statement", "Stewardship for Business Owners", "Legacy Letters and Family Stories", "Faith-Based Investing", "The Purpose of Prosperity", "Building a Multi-Generational Family Vision"]
add(section(f'''
  {eyebrow("A SEMINAR FOR EVERY SEASON")}
  <h2>Turn trusted teaching into practical family action</h2>
  {chips(seminars)}
  {takeaway("Every seminar includes", "Pastor introduction &middot; Biblical foundation &middot; Advisor notes &middot; Participant workbook &middot; Discussion questions &middot; Exercises &middot; Next steps &middot; Follow-up resources &middot; Compliance-safe language &middot; No-sales policy")}
'''))

partner_steps = [
    ("BEGIN WITH SERVICE, NOT SALES", "Ask what pressures families face and what support the church needs."),
    ("LEARN THE PASTOR'S VISION", "Understand mission, discipleship, sermon calendar, groups, generosity philosophy, and concerns."),
    ("OFFER ONE PRACTICAL RESOURCE", "Start with a useful article, devotional, worksheet, research packet, or client-neutral seminar."),
    ("ESTABLISH BOUNDARIES", "Clarify roles, privacy, referrals, branding, compliance, follow-up, and financial responsibilities."),
    ("PILOT A SMALL EXPERIENCE", "Launch a low-risk, high-value event or short journey."),
    ("MEASURE MINISTRY OUTCOMES", "Track participation, family conversations, completed exercises, and transformation stories &mdash; not only leads."),
    ("BUILD AN ANNUAL PLAN", "Create a four-quarter rhythm around wisdom, family, purpose, generosity, legacy, and year-end giving."),
]
add(section(f'''
  {eyebrow("HOW TO PARTNER WITH A LOCAL CHURCH")}
  <h2 class="on-dark">A seven-step pathway from first conversation to annual ministry plan</h2>
  {stack_steps(partner_steps)}
''', dark=True))

pathways = [
    ("Grow Yourself", "40-Day Growth Builder &middot; Alignment Assessment &middot; Spiritual formation &middot; Advisor devotionals"),
    ("Grow Your Practice", "Practice Builder &middot; Vision and Values &middot; Marketing &middot; Client experience &middot; Team &middot; Succession"),
    ("Serve Families", "Family Legacy Builder &middot; Conversation guides &middot; Workshops &middot; Next generation &middot; Generosity &middot; Transitions"),
    ("Partner with Churches", "Playbook &middot; Pastor resources &middot; Sermons &middot; Seminars &middot; Small groups &middot; Campaigns &middot; Ministry systems"),
    ("Build Community", "Advisor groups &middot; Coaching &middot; Masterclasses &middot; Events &middot; Certification &middot; Regional networks"),
]
add(section(f'''
  {eyebrow("ONE NETWORK, FIVE GROWTH PATHWAYS")}
  <h2>A clear member experience built around the advisor&rsquo;s real work</h2>
  {"".join([offer_card(t,"",d) for t,d in pathways])}
  {takeaway("Homepage message", "Build a Practice That Reflects Your Faith and Changes Families for Generations. The growth, client-engagement, family-legacy, and church-partnership platform built specifically for Christian financial advisors.")}
'''))

most_provide = ["Practice management", "Investment platforms", "Compliance", "Technology", "Marketing", "Networking"]
network_adds = ["Spiritual formation", "Biblically sound financial wisdom", "Transferable client conversation tools", "Family legacy and next-generation resources", "Marriage and family content", "Generosity tools", "Church partnership systems", "Pastor sermon support", "Customizable campaigns", "Advisor-branded family journeys"]
add(section(f'''
  {eyebrow("THE STRATEGIC ADVANTAGE")}
  <h2 class="on-dark">What traditional advisor networks provide &mdash; and what is usually missing</h2>
  {titled_list("Most advisor networks provide", most_provide)}
  {titled_list("The Christian Advisor Network adds", network_adds)}
  {takeaway("A differentiated promise", "We help Christian advisors grow personally, build thriving practices, deepen client relationships, serve entire families, partner with churches, and multiply Kingdom impact.")}
  <p class="fine-print">Brand architecture: Christian Advisor Network&trade; &middot; Christian Advisor Growth Builder&trade; &middot; Christian Advisor Practice Builder&trade; &middot; Family Legacy Builder&trade; &middot; Financial Wisdom Ministry&trade; &middot; Pastor and Church Resource Library&trade; &middot; Trusted Guide Academy&trade;</p>
''', dark=True))

promises = [
    "Something meaningful to send every client",
    "Something useful to discuss in every meeting",
    "Something timely for every family transition",
    "Something biblically sound for every financial question",
    "Something valuable for every generation",
    "Something practical to offer every pastor",
    "Something transformational to launch in every church",
]
add(closing(
    "THE ULTIMATE ADVISOR MEMBERSHIP PROMISE",
    "Something meaningful for every client, every family, every transition, and every church.",
    "<br>".join(promises) + "<br><br>Grow Your Faith. Grow Your Practice. Grow Your Impact.",
    cta_text="Join the Network",
    footer_mark="CHRISTIAN ADVISOR NETWORK&trade; &middot; A LIFETOGETHER PLATFORM"
))

html = assemble("Christian Advisor Network", "".join(S))
with open("/home/claude/build/mobile/advisor_network_mobile.html", "w", encoding="utf-8") as f:
    f.write(html)
print("Sections:", len(S), "size:", len(html))
