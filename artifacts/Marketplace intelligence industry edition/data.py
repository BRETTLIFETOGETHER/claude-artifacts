# -*- coding: utf-8 -*-
"""
LifeTogether Workplace Intelligence(TM) -- Master Directory data generator
Builds 40 workplace categories x 50 campaigns (title + subtitle only),
organized into the 5-section framework:
  1. Calling & Purpose
  2. Leadership & Character
  3. Stewardship & Excellence
  4. Relationships & Culture
  5. Legacy & Kingdom Impact
Plus: Flourishing Workplace (6-criteria series) and Purpose Based Business (themes only).
"""

SECTIONS = ["Calling & Purpose", "Leadership & Character", "Stewardship & Excellence",
            "Relationships & Culture", "Legacy & Kingdom Impact"]

# ---------- TEMPLATES (title, subtitle) per section. Use {role} {roles} {field} {place} {beneficiary} {tool} {pressure}
T_CALLING = [
    ("Called to {field_cap}", "Discovering God's purpose behind your work as a {role}"),
    ("The {role_cap}'s Calling", "Finding sacred meaning in {place}"),
    ("More Than a Job", "Seeing {field} as Kingdom work"),
    ("Made for This", "How your gifts as a {role} serve God's design"),
    ("Faith in {place_cap}", "Living for Christ where you work every day"),
    ("The Sacred Ordinary", "Recognizing God's presence in the daily work of {field}"),
    ("{field_cap} as Worship", "Offering your skill and labor to God"),
    ("Your Kingdom Assignment", "Why {field} is a calling, not just a career"),
    ("Behind {tool_cap}", "The eternal purpose hidden in daily {field}"),
    ("The {role_cap}'s Soul", "Protecting your heart while serving {beneficiary}"),
]
T_LEADERSHIP = [
    ("Leading with Integrity", "Character that holds up under pressure in {place}"),
    ("The Faithful {role_cap}", "Leading {beneficiary} with humility and truth"),
    ("Courage Under Pressure", "Staying faithful through {pressure}"),
    ("Leading Like Jesus", "A servant model for {roles}"),
    ("The Trusted {role_cap}", "Why character matters more than competence"),
    ("Wisdom in {field_cap}", "Making hard calls with a clear conscience"),
    ("Grace Under Fire", "Leading well when {pressure} tests you"),
    ("The Whole Leader", "Integrating faith, character, and competence"),
    ("Leading Through Change", "Steady faith in a shifting field of {field}"),
    ("Influence Worth Having", "Building trust as a {role} people can follow"),
]
T_STEWARDSHIP = [
    ("Excellence as Worship", "Bringing your best to {field} for God's glory"),
    ("Stewarding Your {tool_cap}", "Managing what's entrusted to you with wisdom"),
    ("The Excellent {role_cap}", "Doing skilled work as an offering"),
    ("Beyond Competence", "Excellence that reflects the Creator"),
    ("Faithful with Little", "Stewardship in the small details of {field}"),
    ("The Long Obedience", "Consistency and excellence over a whole career"),
    ("Guarding What Matters", "Ethics and integrity in {place}"),
    ("Working Unto the Lord", "Excellence when no one is watching"),
    ("The Craft of Faithfulness", "Mastering {field} as an act of devotion"),
    ("Stewarding Your Season", "Wise use of time, energy, and opportunity"),
]
T_RELATIONSHIPS = [
    ("Serving {beneficiary_cap} Well", "Seeing people the way God sees them"),
    ("Building Healthy Culture", "Relationships that make {place} thrive"),
    ("Beyond Transactions", "Turning {field} into real relationship"),
    ("The Listening {role_cap}", "Presence and empathy in daily work"),
    ("Grace for Difficult People", "Loving {beneficiary} even under pressure"),
    ("Teams That Trust Each Other", "Building unity in {place}"),
    ("Compassion Without Burnout", "Sustainable care for {beneficiary}"),
    ("Honest Conversations", "Truth-telling with grace in {field}"),
    ("Serving Before Selling", "Relationship first, results second"),
    ("The Ministry of Presence", "Showing up for {beneficiary} in hard moments"),
]
T_LEGACY = [
    ("Finish Well", "Building a legacy that outlasts your career in {field}"),
    ("Beyond the Paycheck", "Discovering eternal significance in {field}"),
    ("Building What Lasts", "Kingdom impact through your work as a {role}"),
    ("Your Monday Mission", "Every day in {place} as an act of mission"),
    ("The Legacy {role_cap}", "Shaping the next generation of {roles}"),
    ("Influence That Outlives You", "Multiplying faithful {roles}"),
    ("Kingdom Impact at Work", "How {field} becomes a mission field"),
    ("Called to Multiply", "Raising up the next generation in {field}"),
    ("The Long Game", "Faithfulness measured in decades, not quarters"),
    ("Sent to {place_cap}", "Living on mission exactly where God placed you"),
]
TEMPLATES = [T_CALLING, T_LEADERSHIP, T_STEWARDSHIP, T_RELATIONSHIPS, T_LEGACY]


def fill(tpl, v):
    title, sub = tpl
    ctx = dict(v)
    ctx["field_cap"] = v["field"][0].upper() + v["field"][1:]
    ctx["place_cap"] = v["place"][0].upper() + v["place"][1:]
    ctx["tool_cap"] = v["tool"][0].upper() + v["tool"][1:]
    ctx["beneficiary_cap"] = v["beneficiary"][0].upper() + v["beneficiary"][1:]
    ctx["role_cap"] = v["role"]
    return title.format(**ctx), sub.format(**ctx)


def build_category(vocab, seed_examples=None):
    """Returns dict: section -> list of (title, subtitle), 10 per section = 50 total."""
    out = {}
    for sec_name, tpl_list in zip(SECTIONS, TEMPLATES):
        entries = [fill(t, vocab) for t in tpl_list]
        out[sec_name] = entries
    if seed_examples:
        # splice a couple of the original example titles into Calling & Purpose for continuity
        out[SECTIONS[0]][0] = seed_examples[0]
        if len(seed_examples) > 1:
            out[SECTIONS[3]][0] = seed_examples[1]
    return out


# =========================================================================
# VOCAB for the 15 ORIGINAL categories that need expansion to 50
# =========================================================================
ORIGINAL_EXPAND = {
    "Healthcare Professionals": dict(
        vocab=dict(role="physician", roles="healthcare professionals", field="patient care",
                   place="the bedside", beneficiary="patients", tool="the stethoscope",
                   pressure="life-and-death decisions"),
        examples=[("Called to Care", "Seeing every patient as an image-bearer of God"),
                  ("Compassion Without Burnout", "Sustainable caregiving for the long haul")],
    ),
    "Educators & School Leaders": dict(
        vocab=dict(role="teacher", roles="educators", field="teaching", place="the classroom",
                   beneficiary="students", tool="the lesson plan", pressure="a classroom full of needs"),
        examples=[("Called to Teach", "Discovering God's purpose in shaping young minds"),
                  ("Every Student Matters", "Seeing each child the way God sees them")],
    ),
    "Technology, AI & Innovation": dict(
        vocab=dict(role="technologist", roles="technologists", field="building technology",
                   place="the dev team", beneficiary="users", tool="the algorithm",
                   pressure="the pace of innovation"),
        examples=[("Faith in an AI World", "Wisdom for building technology that serves people"),
                  ("Ethics in AI", "Building responsibly in a fast-moving field")],
    ),
    "Sales, Marketing & Customer Influence": dict(
        vocab=dict(role="sales professional", roles="sales and marketing professionals",
                   field="selling and influence", place="the sales floor", beneficiary="customers",
                   tool="the pitch", pressure="quota pressure"),
        examples=[("Selling with Integrity", "Influence that never compromises truth"),
                  ("Serving Before Selling", "Putting the customer's good ahead of the close")],
    ),
    "Real Estate, Construction & Skilled Trades": dict(
        vocab=dict(role="tradesperson", roles="builders and tradespeople", field="skilled work",
                   place="the job site", beneficiary="clients", tool="the toolbelt",
                   pressure="tight deadlines"),
        examples=[("Built on the Rock", "Building with integrity from the foundation up"),
                  ("Honest Work", "Craftsmanship that reflects the Creator")],
    ),
    "Government, Law & Public Service": dict(
        vocab=dict(role="public servant", roles="those in government and law", field="public service",
                   place="the halls of government", beneficiary="the public", tool="the gavel",
                   pressure="political pressure"),
        examples=[("Called to Serve", "Public office as a sacred trust"),
                  ("Justice and Mercy", "Holding both truth and grace in public life")],
    ),
    "Nonprofit, Ministry & Mission Leaders": dict(
        vocab=dict(role="ministry leader", roles="nonprofit and ministry leaders",
                   field="mission-driven work", place="the mission field", beneficiary="those you serve",
                   tool="the vision", pressure="limited resources"),
        examples=[("Leading the Mission", "Vision and endurance for the long haul"),
                  ("Ministry Without Burnout", "Sustainable leadership for those who serve others")],
    ),
    "Agriculture & Ranching": dict(
        vocab=dict(role="farmer", roles="farmers and ranchers", field="the land",
                   place="the fields", beneficiary="your family and community", tool="the harvest",
                   pressure="an uncertain season"),
        examples=[("Faith in the Fields", "Trusting God through every season"),
                  ("The Faithful Farmer", "Stewardship from sunrise to sunset")],
    ),
    "Hospitality & Tourism": dict(
        vocab=dict(role="hospitality professional", roles="hospitality professionals",
                   field="hospitality", place="the front desk", beneficiary="guests",
                   tool="the welcome", pressure="a fast-paced service season"),
        examples=[("Serving with Joy", "Hospitality that reflects Christ"),
                  ("The Welcoming Heart", "Making every guest feel valued")],
    ),
    "Government & Civic Leadership": dict(
        vocab=dict(role="civic leader", roles="civic leaders", field="community leadership",
                   place="city hall", beneficiary="your community", tool="your platform",
                   pressure="public scrutiny"),
        examples=[("Serving the Public Well", "Leadership with integrity in civic life"),
                  ("Hope for the City", "Seeking the flourishing of your community")],
    ),
    "Arts, Entertainment & Media": dict(
        vocab=dict(role="creative", roles="artists and creatives", field="creative work",
                   place="the studio", beneficiary="your audience", tool="the craft",
                   pressure="the pressure to perform"),
        examples=[("Created to Create", "Reflecting God's creativity through your art"),
                  ("Beyond Applause", "Finding identity in Christ, not the reviews")],
    ),
    "Transportation & Logistics": dict(
        vocab=dict(role="driver", roles="transportation professionals", field="the road",
                   place="the cab", beneficiary="those you deliver to", tool="the route",
                   pressure="long hours away from home"),
        examples=[("Driven by Purpose", "Honoring God on every journey"),
                  ("The Long Haul", "Endurance and faithfulness mile after mile")],
    ),
    "Science & Engineering": dict(
        vocab=dict(role="engineer", roles="scientists and engineers", field="discovery and design",
                   place="the lab", beneficiary="the people your work serves", tool="the blueprint",
                   pressure="the demand for certainty"),
        examples=[("Designed by God", "Discovering the Creator through creation"),
                  ("Faith and Discovery", "Integrating rigorous science and deep faith")],
    ),
    "Retail & Customer Service": dict(
        vocab=dict(role="associate", roles="retail and service professionals", field="customer service",
                   place="the counter", beneficiary="every customer", tool="the register",
                   pressure="a demanding shift"),
        examples=[("Serving Every Customer", "Reflecting Christ through everyday service"),
                  ("More Than Transactions", "Building real relationships at the counter")],
    ),
    "Ministry Staff & Church Employees": dict(
        vocab=dict(role="staff member", roles="ministry staff", field="serving the local church",
                   place="behind the scenes", beneficiary="the congregation", tool="your role",
                   pressure="an unseen workload"),
        examples=[("Serving Behind the Scenes", "Faithfulness that quietly builds the church"),
                  ("The Staff Journey", "Serving the church without losing your soul")],
    ),
}

ORIGINAL_EXPAND["Marketplace Ministry Leaders"] = dict(
    vocab=dict(role="marketplace leader", roles="marketplace ministry leaders",
               field="everyday work", place="your workplace", beneficiary="your coworkers",
               tool="your influence", pressure="the divide between Sunday and Monday"),
    examples=None,
)

# Manufacturing and Marketplace Ministry already have 25 -- keep original 25 titles, generate 25 MORE to reach 50
MANUFACTURING_ORIGINAL_25 = [
    ("Built to Last", "Building products, people, and purpose"),
    ("The Faithful Builder", "Honoring God through quality work"),
    ("Excellence Every Day", "Glorifying God through craftsmanship"),
    ("Factory Faith", "Living Christ in the workplace"),
    ("Leading the Production Line", "Leadership where it matters"),
    ("Purpose Behind Production", "Seeing eternal value in everyday work"),
    ("Stewarding Operations", "Managing resources with wisdom"),
    ("The Industrial Disciple", "Following Jesus on the factory floor"),
    ("Work Worth Doing", "Bringing dignity to labor"),
    ("Beyond Efficiency", "Building people while building products"),
    ("Faith Under Pressure", "Trusting God through deadlines"),
    ("The Excellent Craftsman", "Excellence as worship"),
    ("Building Better Teams", "Leadership that develops people"),
    ("Hands That Honor God", "Working with integrity"),
    ("Purpose in Production", "More than making things"),
    ("The Stewarded Workplace", "Managing people and resources well"),
    ("Strength and Service", "Leadership through humility"),
    ("Called to Build", "God's purpose in industry"),
    ("Faith That Works", "Living biblical values daily"),
    ("Leading with Character", "Integrity that influences"),
    ("The Productive Life", "Stewardship of time and talent"),
    ("Serving Through Work", "Work as ministry"),
    ("Building Kingdom Culture", "Transforming workplaces"),
    ("The Maker's Calling", "Reflecting the Creator"),
    ("Legacy on the Factory Floor", "Work that outlives you"),
]
MARKETPLACE_MINISTRY_ORIGINAL_25 = [
    ("Monday Matters", "Connecting Sunday faith to Monday work"),
    ("The Marketplace Disciple", "Following Christ at work"),
    ("Faith Beyond Sunday", "Living missionally at work"),
    ("Kingdom at Work", "Every profession matters"),
    ("Work Is Worship", "Honoring God through vocation"),
    ("The Sent Worker", "Living on mission in the marketplace"),
    ("Business as Ministry", "Every workplace a mission field"),
    ("Called to Influence", "Using work for Kingdom impact"),
    ("Faith in Every Profession", "Christ in every career"),
    ("Workplace Revival", "Transforming culture through discipleship"),
    ("Purpose Beyond the Paycheck", "Discovering eternal significance"),
    ("Your Monday Mission", "Seeing every workday as ministry"),
    ("Marketplace Light", "Bringing hope into your profession"),
    ("Kingdom Influence at Work", "Leading with Christlike character"),
    ("Work That Worships", "Excellence as an act of devotion"),
    ("The Vocation Journey", "Discovering God's calling through work"),
    ("Faithful Where You Are", "Serving God in your current assignment"),
    ("Mission in the Marketplace", "Reaching people through everyday relationships"),
    ("The Whole-Life Disciple", "Integrating faith, family, and work"),
    ("Beyond Career Success", "Pursuing significance over status"),
    ("Workplace Witness", "Sharing Christ through character and compassion"),
    ("Every Desk an Altar", "Offering your daily work to God"),
    ("Influence That Lasts", "Building an eternal legacy through your vocation"),
    ("The Kingdom Professional", "Living with integrity and purpose"),
    ("Called to the Marketplace", "Embracing your profession as God's assignment"),
]

# =========================================================================
# VOCAB for the 20 NEW categories
# =========================================================================
NEW_CATEGORIES = {
    "Physicians": dict(role="physician", roles="physicians", field="medicine",
                        place="the exam room", beneficiary="patients", tool="the diagnosis",
                        pressure="life-and-death decisions"),
    "Dentists": dict(role="dentist", roles="dentists", field="dental care",
                      place="the treatment chair", beneficiary="patients", tool="the exam light",
                      pressure="a packed schedule of anxious patients"),
    "Nurses": dict(role="nurse", roles="nurses", field="patient care",
                    place="the bedside", beneficiary="patients", tool="the chart",
                    pressure="back-to-back twelve-hour shifts"),
    "Therapists & Counselors": dict(role="therapist", roles="therapists and counselors",
                                     field="emotional and spiritual care", place="the counseling room",
                                     beneficiary="clients", tool="the listening ear",
                                     pressure="carrying others' pain"),
    "Accountants & CPAs": dict(role="accountant", roles="accountants and CPAs", field="the numbers",
                                place="the ledger", beneficiary="clients", tool="the balance sheet",
                                pressure="tax season deadlines"),
    "Architects": dict(role="architect", roles="architects", field="design", place="the drafting table",
                        beneficiary="the communities you build for", tool="the blueprint",
                        pressure="competing demands of client and budget"),
    "Commercial Real Estate": dict(role="commercial broker", roles="commercial real estate professionals",
                                    field="commercial real estate", place="the negotiating table",
                                    beneficiary="clients and tenants", tool="the deal",
                                    pressure="high-stakes negotiations"),
    "Insurance Professionals": dict(role="insurance professional", roles="insurance professionals",
                                     field="risk and protection", place="the claims desk",
                                     beneficiary="policyholders", tool="the policy",
                                     pressure="delivering hard news"),
    "Bankers": dict(role="banker", roles="bankers", field="banking", place="the branch",
                     beneficiary="depositors and borrowers", tool="the ledger",
                     pressure="the weight of others' money"),
    "Private Equity & Venture Capital": dict(role="investor", roles="private equity and venture professionals",
                                              field="capital allocation", place="the deal room",
                                              beneficiary="founders and portfolio companies",
                                              tool="the term sheet", pressure="the pressure to return capital"),
    "Family Office Executives": dict(role="family office executive", roles="family office executives",
                                      field="stewarding generational wealth", place="the family office",
                                      beneficiary="the families you serve", tool="the trust document",
                                      pressure="the weight of generational expectations"),
    "Engineers": dict(role="engineer", roles="engineers", field="engineering", place="the design review",
                       beneficiary="the people who rely on what you build", tool="the blueprint",
                       pressure="the demand for precision"),
    "Scientists": dict(role="scientist", roles="scientists", field="research", place="the laboratory",
                        beneficiary="the world your discoveries serve", tool="the data",
                        pressure="the pursuit of an elusive answer"),
    "University Faculty": dict(role="professor", roles="university faculty", field="teaching and research",
                                place="the lecture hall", beneficiary="students",
                                tool="the syllabus", pressure="publish-or-perish pressure"),
    "Coaches & Consultants": dict(role="coach", roles="coaches and consultants", field="advising others",
                                   place="the coaching session", beneficiary="clients",
                                   tool="the framework", pressure="the demand for results"),
    "Human Resources": dict(role="HR leader", roles="human resources professionals",
                             field="people and culture", place="the HR office",
                             beneficiary="every employee", tool="the policy handbook",
                             pressure="being caught in the middle"),
    "Manufacturing Executives": dict(role="operations executive", roles="manufacturing executives",
                                      field="operations", place="the plant floor",
                                      beneficiary="your workforce", tool="the production line",
                                      pressure="margin and deadline pressure"),
    "Franchise Owners": dict(role="franchise owner", roles="franchise owners", field="running the business",
                              place="the storefront", beneficiary="your staff and customers",
                              tool="the brand standard", pressure="thin margins"),
    "Restaurant & Hospitality Owners": dict(role="restaurateur", roles="restaurant and hospitality owners",
                                             field="hospitality", place="the dining room",
                                             beneficiary="guests and staff", tool="the menu",
                                             pressure="a brutal service rush"),
    "Agriculture & Food Producers": dict(role="food producer", roles="agriculture and food producers",
                                          field="feeding people", place="the field and the plant",
                                          beneficiary="the families your food reaches", tool="the harvest",
                                          pressure="forces outside your control"),
}

def flat_new_25(vocab):
    """25 additional flat titles (no section headers) drawn across all 5 template families."""
    picks = []
    for tpl_list in TEMPLATES:
        picks.extend(tpl_list[5:10])  # take the second half of each template family (5 x 5 = 25)
    return [fill(t, vocab) for t in picks]


MANUFACTURING_VOCAB = dict(role="plant leader", roles="manufacturing and operations leaders",
                            field="production", place="the factory floor", beneficiary="your team",
                            tool="the production line", pressure="deadline pressure")
MARKETPLACE_MINISTRY_VOCAB = dict(role="marketplace leader", roles="marketplace ministry leaders",
                                   field="everyday work", place="your workplace",
                                   beneficiary="your coworkers", tool="your influence",
                                   pressure="the divide between Sunday and Monday")


def get_all_categories():
    """Returns list of (category_name, kind, payload)
       kind = 'sectioned' -> payload is dict[section] = [(title,sub) x10]
       kind = 'flat50'    -> payload is list of 50 (title,sub), first 25 are 'founding', next 25 'expansion'
    """
    cats = []
    for name, info in ORIGINAL_EXPAND.items():
        sec = build_category(info["vocab"], info.get("examples"))
        cats.append((name, "sectioned", sec))
    cats.append(("Manufacturing & Industrial Leaders", "flat50",
                 MANUFACTURING_ORIGINAL_25 + flat_new_25(MANUFACTURING_VOCAB)))
    cats.append(("Marketplace Ministry Leaders", "flat50",
                 MARKETPLACE_MINISTRY_ORIGINAL_25 + flat_new_25(MARKETPLACE_MINISTRY_VOCAB)))
    for name, vocab in NEW_CATEGORIES.items():
        sec = build_category(vocab)
        cats.append((name, "sectioned", sec))
    return cats


# =========================================================================
# FLOURISHING WORKPLACE -- 6-criteria framework (reused from the LifeTogether
# Flourishing series: Flourishing with God / Together / from Within /
# through Contribution / for Others / Across Generations)
# =========================================================================
FLOURISHING_WEEKS = [
    "Flourishing with God",
    "Flourishing Together",
    "Flourishing from Within",
    "Flourishing through Contribution",
    "Flourishing for Others",
    "Flourishing Across Generations",
]

FLOURISHING_WORKPLACE_SERIES = [
    ("Flourishing at Work", "The whole-life framework for thriving in your vocation"),
    ("The Flourishing Leader", "Leading a team that flourishes, not just performs"),
    ("The Flourishing Team", "Building a culture where people actually thrive"),
    ("Flourishing Through Burnout", "Recovering a sustainable rhythm for demanding seasons"),
    ("The Flourishing Career", "A whole-life view of vocation, ambition, and rest"),
    ("Flourishing in Transition", "Thriving through a job change, promotion, or layoff"),
    ("The Flourishing Entrepreneur", "Building a company without losing your soul"),
    ("Flourishing Under Pressure", "Steady thriving in high-stakes, high-stress work"),
    ("The Flourishing Workplace Culture", "Shaping an organization where people flourish"),
    ("Flourishing for the Next Generation", "Building a workplace legacy that outlasts you"),
]

# =========================================================================
# PURPOSE BASED BUSINESS -- 5 purposes as the weekly framework
# (Worship / Fellowship / Discipleship / Ministry / Mission,
#  reused from the Biblical Purpose Library, applied to the business context)
# =========================================================================
PURPOSE_WEEKS = [
    ("Worship", "Knowing God at the Center of Your Business"),
    ("Fellowship", "Belonging to a Team, Not Just a Company"),
    ("Discipleship", "Growing in Character as a Business Leader"),
    ("Ministry", "Serving Employees, Customers, and Community"),
    ("Mission", "Living Sent in the Marketplace"),
]

# Theme ideas only -- NOT expanded into full 50-campaign catalogs yet.
PURPOSE_BASED_BUSINESS_THEMES = [
    ("Purpose Built", "The five purposes, reframed for the business owner"),
    ("The Purpose-Driven Company", "Building an organization on more than profit"),
    ("Five Purposes, One Business", "A whole-company framework for lasting impact"),
    ("The Purpose-Built Leader", "Leading yourself before you lead your company"),
    ("Purpose Beyond Profit", "Discovering what your business is really for"),
    ("The Purpose-Built Team", "Aligning your people around more than a paycheck"),
    ("Purpose in Every Department", "Applying the five purposes company-wide"),
    ("The Purpose-Built Founder", "Starting and scaling with eternal values"),
]

if __name__ == "__main__":
    cats = get_all_categories()
    total = 0
    for name, kind, payload in cats:
        if kind == "sectioned":
            n = sum(len(v) for v in payload.values())
        else:
            n = len(payload)
        total += n
    print(f"{len(cats)} categories, {total} total campaigns generated")
    print(f"Flourishing Workplace series: {len(FLOURISHING_WORKPLACE_SERIES)}")
    print(f"Purpose Based Business themes: {len(PURPOSE_BASED_BUSINESS_THEMES)}")
