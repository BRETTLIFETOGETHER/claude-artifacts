import React, { useState, useEffect } from "react";

const NAVY = "#101E38";
const NAVY2 = "#16274A";
const GOLD = "#B98D3E";
const GOLD_BRIGHT = "#D9B876";
const WHITE = "#FBF8F1";
const CREAM = "#F1EBDD";
const INK = "#1C2230";
const SLATE = "#767E8E";
const LINE = "#DCD4C0";
const GREEN = "#3F7D5C";
const AMBER = "#C4791F";

const FONTS = `
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,600;0,700;0,900;1,500;1,600&family=Archivo:wght@500;600;700&family=Inter:wght@400;500;600;700&display=swap');
* { box-sizing: border-box; }
body { margin: 0; }
.can-root { font-family: 'Inter', sans-serif; color: ${INK}; background: ${WHITE}; }
.can-serif { font-family: 'Playfair Display', serif; }
.can-label { font-family: 'Archivo', sans-serif; letter-spacing: 0.14em; text-transform: uppercase; }
.can-eyebrow { display:flex; align-items:center; gap:10px; font-family:'Archivo',sans-serif; font-weight:600; font-size:12px; letter-spacing:0.18em; text-transform:uppercase; color:${GOLD}; }
.can-eyebrow::before { content:''; width:26px; height:2px; background:${GOLD}; display:inline-block; }
.can-eyebrow.on-dark { color:${GOLD_BRIGHT}; }
.can-eyebrow.on-dark::before { background:${GOLD_BRIGHT}; }
.can-nav-link { position:relative; background:none; border:none; cursor:pointer; font-family:'Archivo'; }
.can-nav-link::after { content:''; position:absolute; left:0; right:0; bottom:-6px; height:1.5px; background:${GOLD_BRIGHT}; transform:scaleX(0); transition:transform .25s ease; }
.can-nav-link:hover::after { transform:scaleX(1); }
.can-nav-link.active::after { transform:scaleX(1); background:${GOLD}; }
.can-card { transition: transform .35s cubic-bezier(.2,.7,.3,1); }
.can-card:hover { transform: translateY(-3px); }
.can-btn-gold { transition: background .2s ease, color .2s ease, transform .2s ease; }
.can-btn-gold:hover { transform: translateY(-1px); }
.can-fade-in { animation: canFadeIn .5s ease both; }
@keyframes canFadeIn { from { opacity:0; transform:translateY(8px);} to {opacity:1; transform:translateY(0);} }
.can-rack-cell { transition: background .25s ease, border-color .25s ease; }
.can-explore-card { transition: transform .3s ease, border-color .3s ease; cursor:pointer; }
.can-explore-card:hover { transform: translateY(-4px); border-color: ${GOLD} !important; }
.can-footer-link { background:none; border:none; cursor:pointer; text-align:left; padding:0; }
.can-desktop-only { display: none; }
@media (min-width: 900px) { .can-desktop-only { display: flex !important; } }
.can-mobile-only { display: inline-block; }
@media (min-width: 900px) { .can-mobile-only { display: none !important; } }
.can-dropdown-panel { animation: canFadeIn .18s ease both; }
.can-locked-item { position:relative; opacity:0.55; }
.can-lock-badge { display:inline-flex; align-items:center; gap:4px; font-family:'Archivo'; font-weight:700; font-size:8.5px; letter-spacing:0.08em; color:${GOLD}; background:${CREAM}; border:1px solid ${GOLD}; border-radius:10px; padding:3px 8px; }
.can-free-badge { display:inline-flex; align-items:center; gap:4px; font-family:'Archivo'; font-weight:700; font-size:8.5px; letter-spacing:0.08em; color:#fff; background:${NAVY}; border-radius:10px; padding:3px 8px; }
.fjb-tab { background:none; border:none; cursor:pointer; font-family:'Archivo'; font-weight:600; }
.fjb-input { font-family:'Inter'; font-size:13px; padding:9px 12px; border:1px solid ${LINE}; border-radius:6px; outline:none; background:${WHITE}; }
.fjb-input:focus { border-color:${GOLD}; }
.fjb-card { border:1px solid ${LINE}; border-radius:6px; background:${WHITE}; }
::selection { background: ${GOLD}; color: ${WHITE}; }
`;

/* ---------------- NAV STRUCTURE ---------------- */
const PAGES = [
  { id: "home", label: "Home" },
  { id: "resources", label: "Breakthrough Resources" },
  { id: "rack", label: "Resource Rack" },
  { id: "assessments", label: "Assessments" },
  { id: "growth-series", label: "Advisor Growth Series" },
  { id: "business-leaders", label: "For Business Leader Clients" },
  { id: "purpose-built-business", label: "Purpose Built Business (Secular Edition)" },
  { id: "offerings-families", label: "Offerings for Families" },
  { id: "find-advisor", label: "Find an Advisor" },
  { id: "partnership", label: "Church Partnership" },
  { id: "membership", label: "Membership" },
  { id: "case-studies", label: "Success Stories" },
  { id: "faq", label: "FAQ" },
  { id: "about", label: "About" },
  { id: "fjb-overview", label: "Family Journey Builder" },
  { id: "fjb-map", label: "Family Map" },
  { id: "fjb-retention", label: "Retention" },
  { id: "fjb-relational", label: "Relational Bonds" },
  { id: "fjb-aum", label: "AUM Growth" },
  { id: "fjb-steward", label: "Successor & Steward Journey" },
  { id: "fjb-business", label: "Family Business" },
  { id: "fjb-stories", label: "Stories" },
  { id: "fjb-sources", label: "Sources" },
  { id: "fjb-finder", label: "Finder" },
  { id: "fjb-coaching", label: "Coaching" },
  { id: "fjb-scripts", label: "Scripts" },
  { id: "fjb-builders", label: "Builders" },
  { id: "fjb-habits", label: "Habits" },
  { id: "fjb-toolbox", label: "Toolbox" },
  { id: "fjb-library-builder", label: "Library Builder" },
  { id: "fjb-calendar", label: "Calendar" },
  { id: "fjb-cohort", label: "Cohort" },
  { id: "fjb-library", label: "Library" },
  { id: "fjb-publish", label: "Publish" },
];

const NAV_GROUPS = [
  { label: "The Toolbox", items: ["resources", "rack", "assessments", "growth-series", "business-leaders", "purpose-built-business"] },
  { label: "For Families", items: ["offerings-families", "find-advisor"] },
  { label: "Family Journey Builder", items: ["fjb-overview", "fjb-map", "fjb-retention", "fjb-relational", "fjb-aum", "fjb-steward", "fjb-business", "fjb-stories"] },
  { label: "Journey Toolkit — Guidance", items: ["fjb-sources", "fjb-finder", "fjb-coaching", "fjb-scripts", "fjb-builders", "fjb-habits"] },
  { label: "Journey Toolkit — Planning", items: ["fjb-toolbox", "fjb-library-builder", "fjb-calendar", "fjb-cohort", "fjb-library", "fjb-publish"] },
  { id: "partnership" },
  { id: "membership" },
  { label: "More", items: ["case-studies", "faq", "about"] },
];

function pageLabel(id) {
  const p = PAGES.find((p) => p.id === id);
  return p ? p.label : id;
}

/* ---------------- CORE DATA ---------------- */
const BREAKTHROUGHS = [
  { n: "01", title: "Faith & Practice Alignment Assessment™", desc: "See where faith, life, family, leadership, practice, and Kingdom impact are aligned — and build a 90-day growth plan.", detail: "A 50-question assessment with an automated scorecard covering personal spiritual health, marriage and family alignment, leadership capacity, practice vision, team culture, Kingdom impact, and succession readiness. You leave with personalized recommendations, a 90-day growth plan, and a coaching discussion guide." },
  { n: "02", title: "Christian Advisor Vision & Values Builder™", desc: "Create a fully custom vision, mission, values, client promise, team covenant, and ten-year legacy vision.", detail: "Produces a polished, advisor-branded document — The Vision and Values of [Practice Name] — covering your calling statement, five to seven core values, ideal client definition, client experience promise, and a ten-year legacy vision, ready to use on your website and in your brochure." },
  { n: "03", title: "Legacy Family Conversation System™", desc: "Turn financial-planning meetings into meaningful multi-generational conversations.", detail: "100 Legacy Questions, a Family Values Card Sort, a Legacy Timeline, a Family Story Interview, a Family Generosity Map, and an annual legacy review rhythm — the tools that open a deeper conversation than the balance sheet." },
  { n: "04", title: "Family Legacy Builder™", desc: "Help families transfer faith, wisdom, values, stories, generosity, and wealth.", detail: "Six movements — Remember Your Story, Clarify Your Values, Define Your Purpose, Prepare the Next Generation, Build a Generosity Legacy, Create the Family Legacy Plan — ending in a mission statement, a legacy letter, and a ten-year vision." },
  { n: "05", title: "40-Day Christian Advisor Growth Builder™", desc: "A guided faith-and-practice journey combining spiritual formation with practical growth actions.", detail: "Forty daily devotionals, six weekly videos, six masterclasses, a coaching guide, and an implementation workbook — a repeatable growth rhythm across faith, leadership, practice, clients, family legacy, and Kingdom impact." },
  { n: "06", title: "Advisor-Church Partnership Playbook™", desc: "Serve churches with wisdom, integrity, clear boundaries, and scalable ministry pathways.", detail: "A full partnership covenant — no selling from the platform, no church-member lists, no implied endorsement — plus the Five Levels of Church Partnership, from Resource Provider to Strategic Ministry Partner." },
  { n: "07", title: "Pastor Sermon & Seminar Library™", desc: "Equip pastors with biblically rich, pastorally sensitive teaching on stewardship, generosity, and legacy.", detail: "Six full sermon series — God Owns It All, Financial Wisdom for Real Life, The Generous Life, Built for Legacy, Faith Family & Finances, Wisdom for Every Season — plus 21 ready-to-teach seminars, each compliance-safe and no-sales." },
];

const RACK_CATEGORIES = [
  { name: "Faith & Spiritual Formation", items: [
    { t: "Faith and Finances", free: true }, { t: "Living with Uncertainty" }, { t: "The Discipline of Contentment" }, { t: "Discovering Your Calling" }, { t: "Spiritual Disciplines for Advisors" }, { t: "An Eternal Perspective on Wealth" }, { t: "Prayer and Financial Decisions" }, { t: "Faith Through Market Volatility" },
  ]},
  { name: "Marriage & Money", items: [
    { t: "Understanding Money Personalities", free: true }, { t: "Resolving Financial Conflict" }, { t: "Radical Transparency" }, { t: "Navigating Debt Together" }, { t: "Blended Family Finances" }, { t: "Aligning Retirement Expectations" }, { t: "The First Financial Conversation" }, { t: "Money Dates That Work" },
  ]},
  { name: "Parenting & Next Generation", items: [
    { t: "Raising Financially Wise Children", free: true }, { t: "Teaching Generosity Early" }, { t: "Age-Appropriate Responsibility" }, { t: "Avoiding Entitlement" }, { t: "Preparing Heirs for Wealth" }, { t: "The Grandparent's Influence" }, { t: "Allowance and Chores" }, { t: "College Without Compromise" },
  ]},
  { name: "Family Communication & Unity", items: [
    { t: "Running a Family Meeting", free: true }, { t: "Navigating Family Conflict" }, { t: "Building a Shared Vision" }, { t: "Family Governance Basics" }, { t: "Writing a Family Constitution" }, { t: "The Family Council Model" }, { t: "Planning a Legacy Retreat" }, { t: "When Siblings Disagree" },
  ]},
  { name: "Life Purpose & Calling", items: [
    { t: "Discovering Your Purpose", free: true }, { t: "Navigating Career Transition" }, { t: "Retirement Identity" }, { t: "The Power of Mentoring" }, { t: "A Framework for Life Planning" }, { t: "Multiplying Your Life Message" }, { t: "Second-Half Calling" }, { t: "Purpose Beyond Production" },
  ]},
  { name: "Financial Wisdom & Stewardship", items: [
    { t: "God Owns It All", free: true }, { t: "Living Within Margin" }, { t: "Freedom from Debt" }, { t: "Setting True Goals" }, { t: "A Biblical View of Saving" }, { t: "Faith-Based Investing" }, { t: "Defining Your Finish Line" }, { t: "Gratitude and Contentment" },
  ]},
  { name: "Generosity & Kingdom Impact", items: [
    { t: "The Family Giving Plan", free: true }, { t: "Philanthropy with Purpose" }, { t: "Donor-Advised Funds Explained" }, { t: "Giving to Missions Well" }, { t: "Starting a Family Foundation" }, { t: "Legacy Giving Strategies" }, { t: "Generosity as Worship" }, { t: "Teaching Kids to Give" },
  ]},
  { name: "Health, Wholeness & Resilience", items: [
    { t: "Whole-Life Stewardship", free: true }, { t: "Managing Financial Stress" }, { t: "Preventing Advisor Burnout" }, { t: "Navigating a Health Crisis" }, { t: "The Caregiving Season" }, { t: "Practicing Sabbath" }, { t: "Walking Through Grief" }, { t: "Building Resilience" },
  ]},
  { name: "Retirement & Major Transitions", items: [
    { t: "Retiring with Purpose", free: true }, { t: "Selling a Business Well" }, { t: "Walking Through Widowhood" }, { t: "Relocation Decisions" }, { t: "Navigating an Inheritance" }, { t: "The Empty Nest Season" }, { t: "End-of-Life Planning" }, { t: "A Second Career After 60" },
  ]},
  { name: "Family Legacy", items: [
    { t: "Writing a Legacy Letter", free: true }, { t: "Capturing Family Stories" }, { t: "Clarifying Family Values" }, { t: "The Ethical Will" }, { t: "Family History on Video" }, { t: "Passing Down Faith" }, { t: "A Legacy Beyond Money" }, { t: "Building a Family Archive" },
  ]},
  { name: "Business & Entrepreneurship Stewardship", items: [
    { t: "Stewarding a Growing Business" }, { t: "Faith-Based Leadership" }, { t: "Succession Planning for Owners" }, { t: "Generosity in the Workplace" }, { t: "Ethical Decision-Making" }, { t: "Building a Kingdom Culture" }, { t: "Exit Strategy with Purpose" }, { t: "Employee Care as Ministry" },
  ]},
  { name: "Workplace & Career Calling", items: [
    { t: "Finding Meaning at Work" }, { t: "Navigating a Layoff" }, { t: "Negotiating with Integrity" }, { t: "Work-Life Stewardship" }, { t: "Faith in the Marketplace" }, { t: "Mentoring Young Professionals" }, { t: "Calling in a Second Career" }, { t: "Excellence as Worship" },
  ]},
];
const RACK_TOTAL = RACK_CATEGORIES.reduce((sum, c) => sum + c.items.length, 0);
const RACK_FREE_COUNT = RACK_CATEGORIES.reduce((sum, c) => sum + c.items.filter((i) => i.free).length, 0);

const ASSESSMENTS = [
  { name: "Faith & Practice Alignment Assessment™", audience: "For Advisors", desc: "See where faith, family, leadership, and practice are aligned — and build a 90-day plan.", free: true },
  { name: "Whole-Life Stewardship Assessment™", audience: "For Client Families", desc: "Opens a meaningful conversation about faith, family, finances, health, purpose, and legacy.", free: true },
  { name: "Family Legacy Readiness Assessment™", audience: "For Client Families", desc: "Measures how prepared a family is to transfer wisdom, values, and wealth together." },
  { name: "Next-Generation Readiness Assessment™", audience: "For Client Families", desc: "Evaluates whether heirs are prepared for the responsibility they're about to receive." },
  { name: "Marriage & Money Alignment Assessment™", audience: "For Client Families", desc: "Surfaces where a couple's money personalities align, and where they don't yet." },
  { name: "Generosity Capacity Assessment™", audience: "For Client Families", desc: "Helps a family understand what they could give, and what's holding them back." },
  { name: "Practice Succession Readiness Assessment™", audience: "For Advisors", desc: "Scores how ready your practice is for a leadership or ownership transition." },
  { name: "Client Experience Assessment™", audience: "For Advisors", desc: "Benchmarks your client experience against the Network's best practices." },
  { name: "Retirement Purpose Assessment™", audience: "For Client Families", desc: "Helps a retiring client define identity and purpose beyond the paycheck." },
  { name: "Business Owner Stewardship Assessment™", audience: "For Client Families", desc: "Evaluates how a business owner's faith and values are showing up in the business." },
  { name: "Family Communication Health Assessment™", audience: "For Client Families", desc: "Diagnoses how well a family actually talks about money, values, and the future." },
  { name: "Team Culture & Stewardship Assessment™", audience: "For Advisors", desc: "Assesses whether your team's day-to-day culture matches your stated values." },
];
const ASSESSMENTS_FREE_COUNT = ASSESSMENTS.filter((a) => a.free).length;

const FAMILY_OFFERINGS = [
  { name: "Whole-Life Stewardship Assessment™", desc: "The natural first step — opens a conversation about faith, family, finances, health, purpose, and legacy, not just the portfolio." },
  { name: "Legacy Family Conversation System™", desc: "100 Legacy Questions, a Family Values Card Sort, a Legacy Timeline, and a Family Story Interview — tools that turn a planning meeting into a real conversation." },
  { name: "Family Legacy Builder™", desc: "A six-movement guided process helping a family remember their story, clarify values, and build a generosity legacy together." },
  { name: "Family Seminars", desc: "Ready-to-host evenings — Marriage and Money, Raising Financially Wise Children, Family Legacy Planning, Generous Living, Caring for Aging Parents, Creating a Family Mission Statement — each with a workbook and discussion guide." },
  { name: "Family Discussion Guides", desc: "Short, client-facing conversation starters pulled from the Resource Rack, built to be handed to a family after a meeting, not just discussed inside one." },
];

const GROWTH_SERIES_ADVISOR = {
  name: "40-Day Christian Advisor Growth Builder™",
  desc: "Forty daily devotionals, six weekly videos, six masterclasses, a coaching guide, and an implementation workbook across faith, leadership, practice, clients, family legacy, and Kingdom impact.",
};

const PURPOSE_LIBRARY_CAMPAIGNS = [
  { title: "A Life That Matters", length: "40 Days", desc: "Know God, belong, grow, serve, live sent, and multiply your life — the flagship introduction to the whole framework." },
  { title: "Made for More", length: "40 Days", desc: "Discover the life God designed you to live. Best for New Year renewal and a fresh sense of calling." },
  { title: "Your Life on Purpose", length: "30 Days", desc: "Align every part of your life with what matters most — built for busy professionals." },
  { title: "Designed to Flourish", length: "40 Days", desc: "Grow spiritually, relationally, personally, and purposefully — well suited to advisor and client audiences alike." },
  { title: "The Whole-Life Disciple", length: "40 Days", desc: "Follow Jesus in every role, relationship, and responsibility — for advisors ready to go deeper." },
  { title: "Your Next Faithful Chapter", length: "30 Days", desc: "Clarify your calling, refocus your priorities, and multiply your impact." },
  { title: "Living What Matters Most", length: "Short Series", desc: "Six biblical priorities that shape an extraordinary life." },
  { title: "Rooted", length: "Short Series", desc: "Building a faith that lasts through every season of life." },
  { title: "Living Fully Alive", length: "Short Series", desc: "Discovering the life Jesus came to give." },
];

const BUSINESS_LEADER_CAMPAIGNS = [
  { n: "1", title: "Seven Days of Purpose at Work", tag: "THE ENTRY CAMPAIGN · WIDEST REACH", desc: "The front door of the business leaders ministry. Every professional immediately self-identifies with this title because every professional is asking the purpose question about their work." },
  { n: "2", title: "Seven Days of Business as Mission", tag: "MOST THEOLOGICALLY ACTIVATING · BAM", desc: "Every business is a vehicle for kingdom advancement, every transaction an opportunity for witness, every employee a person entrusted to the employer's care." },
  { n: "3", title: "Seven Days of Faithful with Much", tag: "STEWARDSHIP-FOCUSED · PARABLE OF TALENTS", desc: "Every business leader has been given more than most — capital, influence, employees, networks. Asks whether it's being deployed in proportion to what's been received." },
  { n: "4", title: "Seven Days of The Excellent Way", tag: "EXCELLENCE + INTEGRITY + WITNESS", desc: "Built on Daniel 6:3. Excellence in professional life is one of the most powerful witnesses available to a Christian leader — made intentional and theological." },
  { n: "5", title: "Seven Days of Kingdom Entrepreneur", tag: "FOUNDERS · BUILDERS · VISIONARIES", desc: "Built for the founder whose entrepreneurial drive is the expression of a creative calling that images the God who creates." },
  { n: "6", title: "Seven Days of Built to Last", tag: "EXIT PLANNING · LEGACY", desc: "For the business leader thinking about succession and exit. Connects directly to the Family Legacy By Design conversation and The Signatry's succession planning tools." },
  { n: "7", title: "Seven Days of Generosity That Scales", tag: "HIGH-CAPACITY GIVING · THE SIGNATRY · DAF", desc: "Connects business success to kingdom generosity at scale — donor-advised funds, charitable LLCs, business exits as giving opportunities." },
  { n: "8", title: "Seven Days of Leading Well", tag: "SERVANT LEADERSHIP · MARK 10:45", desc: "The servant leadership campaign built for the professional context — the leader who actually serves becomes the most influential person in the room." },
  { n: "9", title: "Seven Days of The Second Half", tag: "BOB BUFORD · HALFTIME", desc: "The Halftime framework applied to the high-capacity leader asking: now that I've won the first half, what is the second half actually for?" },
];

const FAMILY_LEGACY_TITLES = [
  "40 Days of Family Legacy — the flagship, built on Tom Conway's Family Legacy By Design curriculum",
  "40 Days of What Matters Most — the felt-need opener for families new to legacy language",
  "40 Days of Lasting Wealth — reframes wealth as values, faith, and character, not just assets",
  "40 Days of the Second Half — built on Bob Buford's Halftime framework",
  "40 Days of Generational Faithfulness — rooted in Psalm 78:4 and Deuteronomy 6",
];

const PBB_JOURNEYS = [
  { n: "1", title: "Why Work Matters", tag: "THE ENTRY POINT · WIDEST REACH" },
  { n: "2", title: "Business as a Force for Good", tag: "PURPOSE BEYOND PROFIT" },
  { n: "3", title: "Deploying What You've Been Given", tag: "STEWARDSHIP · ACCOUNTABILITY" },
  { n: "4", title: "The Excellence Standard", tag: "INTEGRITY · WITNESS · CRAFT" },
  { n: "5", title: "The Builder's Calling", tag: "FOUNDERS · BUILDERS · VISIONARIES" },
  { n: "6", title: "Built to Last", tag: "SUCCESSION · EXIT · LEGACY" },
  { n: "7", title: "Generosity That Scales", tag: "HIGH-CAPACITY GIVING" },
  { n: "8", title: "The Servant Leadership Advantage", tag: "COUNTERINTUITIVE LEADERSHIP" },
  { n: "9", title: "The Second Half", tag: "SUCCESS TO SIGNIFICANCE" },
];

const SPECIALTIES = RACK_CATEGORIES.map((r) => r.name);

const PATHWAYS = [
  { key: "grow-yourself", label: "Grow Yourself", items: ["40-Day Growth Builder", "Alignment Assessment", "Spiritual formation", "Advisor devotionals"], recommend: [{ label: "Take the Alignment Assessment", page: "assessments" }, { label: "Start the 40-Day Growth Builder", page: "growth-series" }] },
  { key: "grow-practice", label: "Grow Your Practice", items: ["Practice Builder", "Vision and Values", "Marketing", "Client experience", "Team", "Succession"], recommend: [{ label: "Take the Client Experience Assessment", page: "assessments" }, { label: "Explore the Vision & Values Builder", page: "resources" }] },
  { key: "serve-families", label: "Serve Families", items: ["Family Legacy Builder", "Conversation guides", "Workshops", "Next generation", "Generosity", "Transitions"], recommend: [{ label: "See Offerings for Families", page: "offerings-families" }, { label: "Browse the Resource Rack", page: "rack" }] },
  { key: "partner-churches", label: "Partner with Churches", items: ["Playbook", "Pastor resources", "Sermons", "Seminars", "Small groups", "Campaigns"], recommend: [{ label: "See the Five Levels of Partnership", page: "partnership" }, { label: "Browse Pastor Seminars", page: "partnership" }] },
  { key: "build-community", label: "Build Community", items: ["Advisor groups", "Coaching", "Masterclasses", "Events", "Certification", "Regional networks"], recommend: [{ label: "Read Success Stories", page: "case-studies" }, { label: "See Membership FAQ", page: "faq" }] },
];

const LEVELS = [
  { n: "1", label: "Resource Provider", desc: "Articles, devotionals, PDFs, sermon-support resources." },
  { n: "2", label: "Seminar Partner", desc: "Financial wisdom, retirement, and legacy education." },
  { n: "3", label: "Small-Group Partner", desc: "Six-week studies, 21-day challenges, 40-day campaigns." },
  { n: "4", label: "Ministry Builder", desc: "Financial wisdom, legacy family, and generosity ministries." },
  { n: "5", label: "Strategic Ministry Partner", desc: "An annual plan across campaigns, training, and measurement." },
];

const PASTOR_FEARS = ["Prospecting disguised as ministry", "Implied endorsement of a business", "Pressure on church members", "Transactional financial content", "Loss of control or confidentiality"];
const ADVISOR_FEARS = ["Being viewed as salespeople", "Unclear expectations and boundaries", "Low pastor engagement", "Compliance concerns", "Unlimited free work expected"];

const PARTNER_STEPS = [
  { t: "Begin with Service, Not Sales", d: "Ask what pressures families face and what support the church needs." },
  { t: "Learn the Pastor's Vision", d: "Understand mission, discipleship, sermon calendar, groups, generosity philosophy, and concerns." },
  { t: "Offer One Practical Resource", d: "Start with a useful article, devotional, worksheet, research packet, or client-neutral seminar." },
  { t: "Establish Boundaries", d: "Clarify roles, privacy, referrals, branding, compliance, follow-up, and financial responsibilities." },
  { t: "Pilot a Small Experience", d: "Launch a low-risk, high-value event or short journey." },
  { t: "Measure Ministry Outcomes", d: "Track participation, family conversations, completed exercises, and transformation stories — not only leads." },
  { t: "Build an Annual Plan", d: "Create a four-quarter rhythm around wisdom, family, purpose, generosity, legacy, and year-end giving." },
];

const FIRST_PILOTS = ["7 Days of Financial Wisdom", "Marriage and Money Seminar", "Family Legacy Workshop", "Retirement with Purpose", "Generosity Conversation Night", "Business Owner Stewardship Roundtable"];

const SEMINARS = ["God Owns It All", "Financial Wisdom for Families", "Marriage and Money", "Raising Financially Wise Children", "Preparing Children for Wealth", "Retirement with Purpose", "Biblical Estate Planning", "Family Legacy Planning", "Generous Living", "Giving as a Family", "Navigating Financial Anxiety", "Caring for Aging Parents", "Wisdom for Widows", "Selling a Business Well", "Avoiding Family Conflict Around Inheritance", "Creating a Family Mission Statement", "Stewardship for Business Owners", "Legacy Letters and Family Stories", "Faith-Based Investing", "The Purpose of Prosperity", "Building a Multi-Generational Family Vision"];

const MOST_PROVIDE = ["Practice management", "Investment platforms", "Compliance", "Technology", "Marketing", "Networking"];
const NETWORK_ADDS = ["Spiritual formation", "Biblically sound financial wisdom", "Transferable client conversation tools", "Family legacy and next-generation resources", "Marriage and family content", "Generosity tools", "Church partnership systems", "Pastor sermon support", "Customizable campaigns", "Advisor-branded family journeys"];

const FAQS = [
  { q: "Will this feel salesy to my clients?", a: "No. Every resource is built around ministry-first conversations, not sales scripts. The Partnership Covenant that governs church relationships — no selling from the platform, no implied endorsement — reflects the same posture the Network expects in client work." },
  { q: "How much does membership cost?", a: "Membership tiers are organized around the Five Growth Pathways rather than a generic plan ladder. Specific pricing is confirmed during your application conversation, since it depends on which pathways matter most to your practice." },
  { q: "What's actually free before I join?", a: "Ten resources across the Resource Rack, two of the twelve assessments, and this whole site. Membership unlocks the remaining resources, assessments, and the growth series." },
  { q: "Do I need existing church relationships to join?", a: "No. The Church Partnership track is entirely optional. Many advisors join for the personal growth tools, the practice-building resources, and the Family Legacy systems alone." },
  { q: "Is this only useful for advisors who work with wealthy clients?", a: "No. The Resource Rack covers stewardship, generosity, and family legacy at every life stage and income level — the Marriage & Money and Parenting & Next Generation categories are used constantly with everyday clients." },
  { q: "What if a church partnership doesn't work out?", a: "The Five Levels model exists for exactly this reason — you begin at Level One, Resource Provider, and only advance when ministry value is proven on both sides. There is no pressure to move faster than trust allows." },
  { q: "Can my whole team use these resources?", a: "Team and practice-wide membership options exist. Ask about seats for your team during onboarding." },
  { q: "Is client or church information ever shared?", a: "No. Confidentiality is a core pillar of the Partnership Covenant — no church-member lists, no data sharing, no exceptions." },
  { q: "How is this different from generic biblical finance content?", a: "The foundation is Ron Blue's biblical financial wisdom, joined with LifeTogether's campaign and curriculum delivery systems — so what you get is a complete, transferable implementation kit for each resource, not just a set of principles to figure out how to use yourself." },
];

const CASE_STUDIES = [
  { practice: "Practice Name Placeholder", type: "Independent RIA · 3 advisors", resource: "40-Day Christian Advisor Growth Builder™", result: "Reported a [XX]% increase in client meetings that included a family-legacy conversation within the first quarter." },
  { practice: "Practice Name Placeholder", type: "Solo practice · Multi-generational clients", resource: "Legacy Family Conversation System™", result: "Used the 100 Legacy Questions to open next-generation planning conversations with [XX] long-tenured client families." },
  { practice: "Practice Name Placeholder", type: "Regional firm · 12 advisors", resource: "Advisor-Church Partnership Playbook™", result: "Reached Level 3, Small-Group Partner, with two local churches within eighteen months of starting at Level 1." },
];

const SAMPLE_ADVISORS = [
  { practice: "Heritage Financial Stewardship", city: "Franklin, TN", specialties: ["Family Legacy", "Financial Wisdom & Stewardship", "Retirement & Major Transitions"], bio: "Twelve years guiding families through generational transitions with a biblical stewardship framework." },
  { practice: "Cornerstone Wealth Partners", city: "Grand Rapids, MI", specialties: ["Marriage & Money", "Parenting & Next Generation"], bio: "Focused on young families building their first values-aligned financial plan together." },
  { practice: "Legacy Path Advisory", city: "Colorado Springs, CO", specialties: ["Generosity & Kingdom Impact", "Family Communication & Unity"], bio: "Works alongside donor-advised funds and family foundations pursuing generous, unified giving." },
];

/* ---------------- SHARED UI ---------------- */
function Photo({ caption, style }) {
  return (
    <div style={{ position: "relative", overflow: "hidden", borderRadius: 3, background: `linear-gradient(135deg, ${NAVY2} 0%, #233A63 45%, #0E1930 100%)`, ...style }}>
      <div style={{ position: "absolute", inset: 0, backgroundImage: `repeating-linear-gradient(115deg, rgba(217,184,118,0.06) 0px, rgba(217,184,118,0.06) 1px, transparent 1px, transparent 30px)` }} />
      <div style={{ position: "absolute", top: 12, left: 12, width: 16, height: 16, borderTop: `1.4px solid rgba(217,184,118,0.85)`, borderLeft: `1.4px solid rgba(217,184,118,0.85)` }} />
      <div style={{ position: "absolute", bottom: 12, right: 12, width: 16, height: 16, borderBottom: `1.4px solid rgba(217,184,118,0.85)`, borderRight: `1.4px solid rgba(217,184,118,0.85)` }} />
      {caption && (
        <div style={{ position: "absolute", left: 14, bottom: 14, right: 40, fontFamily: "Archivo", fontWeight: 500, fontSize: 10, letterSpacing: "0.1em", textTransform: "uppercase", color: "rgba(251,248,241,0.6)" }}>
          {caption}
        </div>
      )}
    </div>
  );
}
function Eyebrow({ children, dark }) {
  return <div className={`can-eyebrow${dark ? " on-dark" : ""}`}>{children}</div>;
}
function LockBadge() { return <span className="can-lock-badge">&#128274; Members Only</span>; }
function FreeBadge() { return <span className="can-free-badge">Free</span>; }

/* ---------------- HEADER NAV (mega-menu) ---------------- */
function HeaderNav({ page, setPage, menuOpen, setMenuOpen, scrolled }) {
  const [openGroup, setOpenGroup] = useState(null);

  return (
    <div
      onMouseLeave={() => setOpenGroup(null)}
      style={{
        position: "sticky", top: 0, zIndex: 50,
        background: scrolled || page !== "home" ? "rgba(16,30,56,0.97)" : "transparent",
        borderBottom: `1px solid rgba(217,184,118,0.2)`,
        backdropFilter: "blur(6px)", transition: "background .3s ease",
      }}
    >
      <div style={{ maxWidth: 1240, margin: "0 auto", padding: "18px 28px", display: "flex", alignItems: "center", justifyContent: "space-between" }}>
        <button onClick={() => setPage("home")} className="can-serif" style={{ background: "none", border: "none", cursor: "pointer", fontWeight: 700, fontSize: 16.5, color: WHITE }}>
          Christian Advisor Network<span style={{ fontSize: 10, verticalAlign: "super" }}>™</span>
        </button>

        <div className="can-desktop-only" style={{ gap: 6, alignItems: "center" }}>
          {NAV_GROUPS.map((g, gi) => {
            if (g.id) {
              return (
                <button key={g.id} onClick={() => setPage(g.id)} className={`can-nav-link can-label${page === g.id ? " active" : ""}`}
                  style={{ fontSize: 10.8, fontWeight: 600, color: page === g.id ? GOLD_BRIGHT : "rgba(251,248,241,0.85)", padding: "8px 12px" }}>
                  {pageLabel(g.id)}
                </button>
              );
            }
            const isOpen = openGroup === gi;
            const containsActive = g.items.includes(page);
            return (
              <div key={g.label} style={{ position: "relative" }} onMouseEnter={() => setOpenGroup(gi)}>
                <button onClick={() => setOpenGroup(isOpen ? null : gi)} className={`can-nav-link can-label${containsActive ? " active" : ""}`}
                  style={{ fontSize: 10.8, fontWeight: 600, color: containsActive ? GOLD_BRIGHT : "rgba(251,248,241,0.85)", padding: "8px 12px" }}>
                  {g.label} {isOpen ? "\u2303" : "\u2304"}
                </button>
                {isOpen && (
                  <div className="can-dropdown-panel" style={{ position: "absolute", top: "100%", left: 0, background: NAVY, border: "1px solid rgba(217,184,118,0.25)", borderRadius: 6, minWidth: 220, padding: 8, boxShadow: "0 12px 28px rgba(0,0,0,0.35)" }}>
                    {g.items.map((id) => (
                      <button key={id} onClick={() => { setPage(id); setOpenGroup(null); }} className="can-footer-link can-label"
                        style={{ display: "block", width: "100%", fontSize: 11, fontWeight: 600, color: page === id ? GOLD_BRIGHT : "rgba(251,248,241,0.85)", padding: "10px 12px", borderRadius: 4 }}>
                        {pageLabel(id)}
                      </button>
                    ))}
                  </div>
                )}
              </div>
            );
          })}
        </div>

        <button onClick={() => setPage("membership")} className="can-btn-gold can-label can-desktop-only"
          style={{ background: GOLD, color: NAVY, border: "none", borderRadius: 22, padding: "9px 18px", fontSize: 10.5, fontWeight: 700, cursor: "pointer" }}>
          Join the Network
        </button>

        <button onClick={() => setMenuOpen((v) => !v)} className="can-mobile-only"
          style={{ background: "none", border: `1px solid rgba(217,184,118,0.5)`, borderRadius: 8, padding: "8px 12px", color: GOLD_BRIGHT, cursor: "pointer", fontSize: 13 }}>
          {menuOpen ? "Close" : "Menu"}
        </button>
      </div>

      {menuOpen && (
        <div style={{ background: NAVY, borderTop: `1px solid rgba(217,184,118,0.2)`, padding: "8px 28px 24px", maxHeight: "70vh", overflowY: "auto" }}>
          {PAGES.map((p) => (
            <div key={p.id} onClick={() => { setPage(p.id); setMenuOpen(false); }} className="can-label"
              style={{ padding: "12px 0", borderBottom: "1px solid rgba(217,184,118,0.15)", color: page === p.id ? GOLD_BRIGHT : "rgba(251,248,241,0.9)", fontSize: 12, cursor: "pointer" }}>
              {p.label}
            </div>
          ))}
          <div onClick={() => { setPage("membership"); setMenuOpen(false); }} className="can-label"
            style={{ marginTop: 16, background: GOLD, color: NAVY, textAlign: "center", padding: "12px 0", borderRadius: 24, fontSize: 12, fontWeight: 700, cursor: "pointer" }}>
            Join the Network
          </div>
        </div>
      )}
    </div>
  );
}

/* ---------------- FOOTER NAV ---------------- */
function FooterNav({ page, setPage }) {
  const utility = ["Privacy Policy", "Terms of Use", "Compliance Disclosures"];
  return (
    <div style={{ background: NAVY, borderTop: "1px solid rgba(217,184,118,0.15)" }}>
      <div style={{ maxWidth: 1240, margin: "0 auto", padding: "56px 28px 32px", display: "grid", gridTemplateColumns: "1.2fr 1fr 1fr 1fr 1fr", gap: 32 }}>
        <div>
          <div className="can-serif" style={{ fontWeight: 700, fontSize: 15.5, color: WHITE, marginBottom: 12 }}>
            Christian Advisor Network<span style={{ fontSize: 9, verticalAlign: "super" }}>™</span>
          </div>
          <p style={{ fontSize: 12, color: "rgba(251,248,241,0.6)", lineHeight: 1.6, maxWidth: 220 }}>
            Faithful Advisors. Flourishing Practices. Stronger Families. Healthier Churches. Lasting Legacies.
          </p>
        </div>
        {NAV_GROUPS.map((g) => {
          const items = g.id ? [g.id] : g.items;
          const heading = g.id ? pageLabel(g.id) : g.label;
          return (
            <div key={heading}>
              <div className="can-label" style={{ fontSize: 9.5, color: GOLD, marginBottom: 14 }}>{heading}</div>
              {items.map((id) => (
                <button key={id} onClick={() => setPage(id)} className="can-footer-link"
                  style={{ display: "block", fontSize: 12, color: page === id ? GOLD_BRIGHT : "rgba(251,248,241,0.72)", padding: "5px 0", cursor: "pointer" }}>
                  {pageLabel(id)}
                </button>
              ))}
            </div>
          );
        })}
      </div>
      <div style={{ maxWidth: 1240, margin: "0 auto", padding: "18px 28px", borderTop: "1px solid rgba(217,184,118,0.12)", display: "flex", justifyContent: "space-between", flexWrap: "wrap", gap: 16 }}>
        <div style={{ display: "flex", gap: 18, flexWrap: "wrap" }}>
          {utility.map((u) => (
            <div key={u} style={{ fontSize: 11, color: "rgba(251,248,241,0.4)" }}>{u} <span style={{ fontStyle: "italic" }}>(coming soon)</span></div>
          ))}
        </div>
        <div className="can-label" style={{ fontSize: 9.5, color: "rgba(251,248,241,0.45)" }}>DRAFT PREVIEW · NOT YET LIVE</div>
      </div>
    </div>
  );
}

/* ---------------- HOME ---------------- */
function HomePage({ setPage }) {
  const [seeMore, setSeeMore] = useState(false);
  const explore = [
    { id: "resources", label: "The Seven Breakthrough Resources", desc: "Flagship systems that solve major advisor problems." },
    { id: "rack", label: "The Resource Rack", desc: `${RACK_TOTAL} resources across 12 categories — ${RACK_FREE_COUNT} free to start.` },
    { id: "assessments", label: "Assessments", desc: `${ASSESSMENTS.length} assessments for advisors and client families.` },
    { id: "growth-series", label: "Advisor Growth Series", desc: "The 40-Day Growth Builder, plus the full Biblical Purpose Library." },
    { id: "business-leaders", label: "For Business Leader Clients", desc: "Nine campaigns launching a Christian business leaders ministry." },
    { id: "offerings-families", label: "Offerings for Families", desc: "What you actually hand your clients." },
    { id: "find-advisor", label: "Find an Advisor", desc: "A directory connecting families and churches with members." },
    { id: "fjb-overview", label: "Family Journey Builder", desc: "Seven live tools — Family Map, Retention, Relational Bonds, AUM Growth, Succession, Family Business, Stories." },
    { id: "partnership", label: "Church Partnership", desc: "Five levels, from resource provider to strategic partner." },
    { id: "case-studies", label: "Success Stories", desc: "What advisors are building with these resources." },
  ];

  return (
    <div className="can-fade-in">
      <div style={{ position: "relative", background: `linear-gradient(165deg, ${NAVY} 0%, #0E1930 100%)`, overflow: "hidden" }}>
        <div style={{ position: "absolute", inset: 0, opacity: 0.5, backgroundImage: `radial-gradient(circle at 78% 18%, rgba(185,141,62,0.16), transparent 45%)` }} />
        <div style={{ maxWidth: 1240, margin: "0 auto", padding: "88px 28px 90px", position: "relative" }}>
          <div style={{ maxWidth: 700 }}>
            <Eyebrow dark>For Christian Financial Advisors</Eyebrow>
            <h1 className="can-serif" style={{ fontSize: "clamp(32px, 5vw, 52px)", lineHeight: 1.08, fontWeight: 700, color: WHITE, margin: "26px 0 0" }}>
              Build a practice that reflects your faith and changes families for generations.
            </h1>
            <p className="can-serif" style={{ fontStyle: "italic", fontWeight: 500, fontSize: 19, color: GOLD_BRIGHT, marginTop: 26, lineHeight: 1.5, maxWidth: 560 }}>
              Grow your faith. Build your practice. Serve families. Strengthen churches. Multiply Kingdom impact.
            </p>
            <div style={{ display: "flex", gap: 16, marginTop: 40, flexWrap: "wrap" }}>
              <button onClick={() => setPage("rack")} className="can-btn-gold can-label" style={{ background: GOLD, color: NAVY, border: "none", borderRadius: 26, padding: "15px 30px", fontSize: 12, fontWeight: 700, cursor: "pointer" }}>
                Browse the Free Toolbox
              </button>
              <button onClick={() => setPage("find-advisor")} className="can-label" style={{ background: "transparent", color: WHITE, border: "1px solid rgba(251,248,241,0.35)", borderRadius: 26, padding: "15px 30px", fontSize: 12, fontWeight: 700, cursor: "pointer" }}>
                Find an Advisor
              </button>
            </div>
          </div>
          <div style={{ display: "flex", gap: 48, marginTop: 74, flexWrap: "wrap" }}>
            {[["GROW", "personally"], ["SERVE", "families"], ["MULTIPLY", "Kingdom impact"]].map(([w, s]) => (
              <div key={w}>
                <div className="can-serif" style={{ fontSize: 20, fontWeight: 700, color: GOLD_BRIGHT }}>{w}</div>
                <div className="can-label" style={{ fontSize: 10.5, color: "rgba(251,248,241,0.55)", marginTop: 4, fontWeight: 500 }}>{s}</div>
              </div>
            ))}
          </div>
        </div>
      </div>

      <div style={{ background: CREAM }}>
        <div style={{ maxWidth: 1240, margin: "0 auto", padding: "50px 28px", display: "flex", gap: 40, flexWrap: "wrap", justifyContent: "space-between" }}>
          <div><div className="can-serif" style={{ fontSize: 30, fontWeight: 700, color: NAVY }}>{RACK_TOTAL}+</div><div className="can-label" style={{ fontSize: 9.5, color: SLATE }}>Resources in the Rack</div></div>
          <div><div className="can-serif" style={{ fontSize: 30, fontWeight: 700, color: NAVY }}>{ASSESSMENTS.length}</div><div className="can-label" style={{ fontSize: 9.5, color: SLATE }}>Assessments</div></div>
          <div><div className="can-serif" style={{ fontSize: 30, fontWeight: 700, color: NAVY }}>7</div><div className="can-label" style={{ fontSize: 9.5, color: SLATE }}>Breakthrough Resources</div></div>
          <div><div className="can-serif" style={{ fontSize: 30, fontWeight: 700, color: NAVY }}>9</div><div className="can-label" style={{ fontSize: 9.5, color: SLATE }}>Growth Series Campaigns</div></div>
          <div><div className="can-serif" style={{ fontSize: 30, fontWeight: 700, color: NAVY }}>5</div><div className="can-label" style={{ fontSize: 9.5, color: SLATE }}>Church Partnership Levels</div></div>
        </div>
      </div>

      <div style={{ maxWidth: 1240, margin: "0 auto", padding: "90px 28px" }}>
        <Eyebrow>Explore the Platform</Eyebrow>
        <h2 className="can-serif" style={{ fontSize: "clamp(22px, 3vw, 28px)", fontWeight: 700, color: NAVY, margin: "20px 0 44px" }}>
          Everything, in one place.
        </h2>
        <div style={{ display: "grid", gridTemplateColumns: "repeat(auto-fit, minmax(260px, 1fr))", gap: 22 }}>
          {explore.map((e) => (
            <div key={e.id} onClick={() => setPage(e.id)} className="can-explore-card" style={{ border: `1px solid ${LINE}`, borderRadius: 4, padding: "26px 24px", background: CREAM }}>
              <div className="can-serif" style={{ fontWeight: 700, fontSize: 16.5, color: NAVY, marginBottom: 8, lineHeight: 1.3 }}>{e.label}</div>
              <div style={{ fontSize: 13, color: SLATE, lineHeight: 1.55, marginBottom: 14 }}>{e.desc}</div>
              <div className="can-label" style={{ fontSize: 10.5, color: GOLD, fontWeight: 700 }}>Explore &rarr;</div>
            </div>
          ))}
        </div>
      </div>

      <div style={{ maxWidth: 1240, margin: "0 auto", padding: "0 28px 90px" }}>
        <div style={{ borderTop: `1px solid ${LINE}`, paddingTop: 40, textAlign: "center" }}>
          <div className="can-serif" style={{ fontWeight: 700, fontSize: 18, color: NAVY, marginBottom: 10 }}>This library keeps growing.</div>
          <p style={{ fontSize: 13, color: SLATE, maxWidth: 480, margin: "0 auto 18px", lineHeight: 1.6 }}>
            What's live today is the start, not the ceiling. New resources, assessments, and campaigns are added regularly.
          </p>
          <button onClick={() => setSeeMore((v) => !v)} className="can-label"
            style={{ background: "none", border: `1px solid ${GOLD}`, color: GOLD, borderRadius: 20, padding: "10px 22px", fontSize: 10.5, fontWeight: 700, cursor: "pointer" }}>
            {seeMore ? "See Less" : "See More Coming"}
          </button>
          {seeMore && (
            <div className="can-fade-in" style={{ display: "grid", gridTemplateColumns: "repeat(auto-fit, minmax(220px, 1fr))", gap: 12, marginTop: 26, textAlign: "left" }}>
              {[
                "Seasonal campaigns — Thanksgiving, Christmas, Lent, New Year, summer",
                "Additional Family Legacy By Design titles for ultra-high-net-worth families",
                "Expanded Christian Business Leaders Ministry campaign arcs",
                "More assessments for client families in transition",
                "Regional advisor group directories",
                "Deeper Church Partnership measurement tools",
              ].map((t) => (
                <div key={t} style={{ fontSize: 12, color: INK, background: CREAM, borderLeft: `3px solid ${GOLD}`, padding: "12px 14px", lineHeight: 1.5 }}>{t}</div>
              ))}
            </div>
          )}
        </div>
      </div>

      <JoinBand setPage={setPage} />
    </div>
  );
}

/* ---------------- RESOURCES PAGE ---------------- */
function ResourcesPage() {
  const [openResource, setOpenResource] = useState("01");
  return (
    <PageShell eyebrow="The Seven Breakthrough Resources™" title="Flagship systems that solve major advisor problems and deepen client relationships.">
      <p style={{ color: SLATE, fontSize: 14, marginTop: -8, marginBottom: 30 }}>Tap any resource to see what's inside.</p>
      <div style={{ borderTop: `1px solid ${LINE}` }}>
        {BREAKTHROUGHS.map((r) => {
          const open = openResource === r.n;
          return (
            <div key={r.n} style={{ borderBottom: `1px solid ${LINE}` }}>
              <button onClick={() => setOpenResource(open ? null : r.n)}
                style={{ width: "100%", background: "none", border: "none", cursor: "pointer", textAlign: "left", padding: "24px 0", display: "flex", gap: 24, alignItems: "flex-start" }}>
                <div className="can-serif" style={{ fontSize: 22, fontWeight: 700, color: GOLD, width: 42, flexShrink: 0 }}>{r.n}</div>
                <div style={{ flex: 1 }}>
                  <div className="can-serif" style={{ fontSize: 17, fontWeight: 700, color: NAVY, lineHeight: 1.3 }}>{r.title}</div>
                  <div style={{ fontSize: 14, color: SLATE, marginTop: 6, lineHeight: 1.55 }}>{r.desc}</div>
                  {open && <div className="can-fade-in" style={{ fontSize: 13.5, color: INK, marginTop: 16, lineHeight: 1.65, background: CREAM, borderLeft: `3px solid ${GOLD}`, padding: "14px 18px" }}>{r.detail}</div>}
                </div>
                <div className="can-label" style={{ fontSize: 18, color: GOLD, flexShrink: 0 }}>{open ? "\u2013" : "+"}</div>
              </button>
            </div>
          );
        })}
      </div>
    </PageShell>
  );
}

/* ---------------- RESOURCE RACK PAGE (gated) ---------------- */
function RackPage({ setPage }) {
  const [activeCat, setActiveCat] = useState(null);
  return (
    <PageShell eyebrow="The Complete Resource Rack™" title="A biblical resource for every conversation, transition, and family need.">
      <div style={{ display: "flex", justifyContent: "space-between", alignItems: "flex-end", flexWrap: "wrap", gap: 12, marginBottom: 26 }}>
        <p style={{ color: SLATE, fontSize: 13.5, margin: 0, maxWidth: 520 }}>
          {RACK_FREE_COUNT} resources are free to preview right now. Membership unlocks all {RACK_TOTAL}, across all 12 categories.
        </p>
        <button onClick={() => setPage("membership")} className="can-btn-gold can-label" style={{ background: GOLD, color: NAVY, border: "none", borderRadius: 20, padding: "10px 18px", fontSize: 10.5, fontWeight: 700, cursor: "pointer" }}>
          Unlock Full Access
        </button>
      </div>
      {RACK_CATEGORIES.map((cat) => {
        const open = activeCat === cat.name;
        const freeInCat = cat.items.filter((i) => i.free).length;
        return (
          <div key={cat.name} style={{ borderTop: `1px solid ${LINE}` }}>
            <button onClick={() => setActiveCat(open ? null : cat.name)}
              style={{ width: "100%", background: "none", border: "none", cursor: "pointer", textAlign: "left", padding: "18px 0", display: "flex", justifyContent: "space-between", alignItems: "center", gap: 16 }}>
              <div>
                <div className="can-serif" style={{ fontWeight: 700, fontSize: 15.5, color: NAVY }}>{cat.name}</div>
                <div style={{ fontSize: 11, color: SLATE, marginTop: 3 }}>{cat.items.length} resources {freeInCat > 0 ? `· ${freeInCat} free` : ""}</div>
              </div>
              <div className="can-label" style={{ fontSize: 16, color: GOLD, flexShrink: 0 }}>{open ? "\u2013" : "+"}</div>
            </button>
            {open && (
              <div className="can-fade-in" style={{ display: "grid", gridTemplateColumns: "repeat(auto-fit, minmax(220px, 1fr))", gap: 10, paddingBottom: 22 }}>
                {cat.items.map((item) => (
                  <div key={item.t} className={item.free ? "" : "can-locked-item"} style={{ border: `1px solid ${LINE}`, borderRadius: 4, padding: "12px 14px", background: item.free ? WHITE : CREAM }}>
                    <div style={{ display: "flex", justifyContent: "space-between", alignItems: "flex-start", gap: 8 }}>
                      <div style={{ fontSize: 12.5, fontWeight: 600, color: NAVY, lineHeight: 1.4 }}>{item.t}</div>
                      {item.free ? <FreeBadge /> : <LockBadge />}
                    </div>
                  </div>
                ))}
              </div>
            )}
          </div>
        );
      })}
      <div style={{ marginTop: 40, textAlign: "center", background: NAVY, borderRadius: 4, padding: "40px 24px" }}>
        <div className="can-serif" style={{ fontWeight: 700, fontSize: 19, color: WHITE, marginBottom: 8 }}>{RACK_TOTAL - RACK_FREE_COUNT} more resources are waiting.</div>
        <p style={{ fontSize: 13, color: "rgba(251,248,241,0.75)", maxWidth: 440, margin: "0 auto 18px", lineHeight: 1.6 }}>Membership unlocks every category, including Business &amp; Entrepreneurship Stewardship and Workplace &amp; Career Calling.</p>
        <button onClick={() => setPage("membership")} className="can-btn-gold can-label" style={{ background: GOLD, color: NAVY, border: "none", borderRadius: 22, padding: "12px 26px", fontSize: 11, fontWeight: 700, cursor: "pointer" }}>Unlock Full Access</button>
      </div>
    </PageShell>
  );
}

/* ---------------- ASSESSMENTS PAGE (gated) ---------------- */
function AssessmentsPage({ setPage }) {
  const [started, setStarted] = useState({});
  return (
    <PageShell eyebrow="Assessments" title="A dozen assessments for advisors and the families they serve.">
      <p style={{ color: SLATE, fontSize: 13.5, marginTop: -8, marginBottom: 30, maxWidth: 560 }}>
        {ASSESSMENTS_FREE_COUNT} are free to take right now. The rest unlock with membership.
      </p>
      <div style={{ display: "grid", gridTemplateColumns: "repeat(auto-fit, minmax(280px, 1fr))", gap: 18 }}>
        {ASSESSMENTS.map((a) => (
          <div key={a.name} className={a.free ? "can-card" : "can-locked-item"} style={{ border: `1px solid ${LINE}`, borderRadius: 4, padding: "22px 22px", background: a.free ? WHITE : CREAM }}>
            <div style={{ display: "flex", justifyContent: "space-between", alignItems: "flex-start", gap: 10, marginBottom: 10 }}>
              <div className="can-label" style={{ fontSize: 9, color: GOLD }}>{a.audience}</div>
              {a.free ? <FreeBadge /> : <LockBadge />}
            </div>
            <div className="can-serif" style={{ fontWeight: 700, fontSize: 15.5, color: NAVY, lineHeight: 1.3, marginBottom: 8 }}>{a.name}</div>
            <div style={{ fontSize: 12.5, color: SLATE, lineHeight: 1.5 }}>{a.desc}</div>
            {a.free && (
              started[a.name] ? (
                <div className="can-fade-in can-label" style={{ marginTop: 16, textAlign: "center", fontSize: 10, fontWeight: 700, color: NAVY, background: CREAM, borderRadius: 20, padding: "9px 0" }}>
                  &#10003; Started — check your email
                </div>
              ) : (
                <button onClick={() => setStarted((s) => ({ ...s, [a.name]: true }))} className="can-label"
                  style={{ marginTop: 16, width: "100%", background: "none", border: `1px solid ${NAVY}`, color: NAVY, borderRadius: 20, padding: "9px 0", fontSize: 10, fontWeight: 700, cursor: "pointer" }}>
                  Take the Assessment
                </button>
              )
            )}
          </div>
        ))}
      </div>
      <div style={{ marginTop: 40, textAlign: "center", background: NAVY, borderRadius: 4, padding: "36px 24px" }}>
        <p style={{ fontSize: 13, color: "rgba(251,248,241,0.8)", maxWidth: 440, margin: "0 auto 16px", lineHeight: 1.6 }}>Unlock all twelve assessments, for you and for your client families, with membership.</p>
        <button onClick={() => setPage("membership")} className="can-btn-gold can-label" style={{ background: GOLD, color: NAVY, border: "none", borderRadius: 22, padding: "11px 24px", fontSize: 10.5, fontWeight: 700, cursor: "pointer" }}>Unlock Full Access</button>
      </div>
    </PageShell>
  );
}

/* ---------------- ADVISOR GROWTH SERIES PAGE ---------------- */
function GrowthSeriesPage({ setPage }) {
  return (
    <PageShell eyebrow="Advisor Growth Series" title="Series built for your own faith and formation, not just your practice.">
      <div style={{ border: `1px solid ${LINE}`, borderRadius: 4, padding: "26px 24px", background: CREAM, marginBottom: 50 }}>
        <div className="can-label" style={{ fontSize: 9, color: GOLD, marginBottom: 8 }}>Flagship</div>
        <div className="can-serif" style={{ fontWeight: 700, fontSize: 19, color: NAVY, marginBottom: 10 }}>{GROWTH_SERIES_ADVISOR.name}</div>
        <p style={{ fontSize: 13.5, color: INK, lineHeight: 1.65, maxWidth: 640 }}>{GROWTH_SERIES_ADVISOR.desc}</p>
      </div>

      <Eyebrow>Cross-Platform Access</Eyebrow>
      <h2 className="can-serif" style={{ fontSize: "clamp(19px, 3vw, 24px)", fontWeight: 700, color: NAVY, maxWidth: 640, margin: "18px 0 10px", lineHeight: 1.3 }}>
        Also included with membership: the LifeTogether Biblical Purpose Library™
      </h2>
      <p style={{ color: SLATE, fontSize: 13.5, lineHeight: 1.65, maxWidth: 620, marginBottom: 30 }}>
        The same campaign library built for pastors and churches — Know God, Belong, Grow, Serve, Live Sent, Multiply — is available to Network members for their own spiritual formation.
      </p>
      <div style={{ display: "grid", gridTemplateColumns: "repeat(auto-fit, minmax(260px, 1fr))", gap: 16 }}>
        {PURPOSE_LIBRARY_CAMPAIGNS.map((c) => (
          <div key={c.title} className="can-locked-item" style={{ border: `1px solid ${LINE}`, borderRadius: 4, padding: "18px 20px", background: WHITE }}>
            <div style={{ display: "flex", justifyContent: "space-between", alignItems: "flex-start", gap: 8, marginBottom: 8 }}>
              <div className="can-label" style={{ fontSize: 9, color: GOLD }}>{c.length}</div>
              <LockBadge />
            </div>
            <div className="can-serif" style={{ fontWeight: 700, fontSize: 14.5, color: NAVY, marginBottom: 6 }}>{c.title}</div>
            <div style={{ fontSize: 11.5, color: SLATE, lineHeight: 1.5 }}>{c.desc}</div>
          </div>
        ))}
      </div>
      <div style={{ marginTop: 40, textAlign: "center", background: NAVY, borderRadius: 4, padding: "36px 24px" }}>
        <p style={{ fontSize: 13, color: "rgba(251,248,241,0.8)", maxWidth: 460, margin: "0 auto 16px", lineHeight: 1.6 }}>Membership unlocks the full Biblical Purpose Library alongside every advisor-specific resource.</p>
        <button onClick={() => setPage("membership")} className="can-btn-gold can-label" style={{ background: GOLD, color: NAVY, border: "none", borderRadius: 22, padding: "11px 24px", fontSize: 10.5, fontWeight: 700, cursor: "pointer" }}>Unlock Full Access</button>
      </div>
    </PageShell>
  );
}

/* ---------------- BUSINESS LEADERS PAGE ---------------- */
function BusinessLeadersPage({ setPage }) {
  const [open, setOpen] = useState("1");
  return (
    <PageShell eyebrow="For Business Leader Clients" title="Campaigns that launch a Christian business leaders ministry.">
      <p style={{ color: SLATE, fontSize: 14, lineHeight: 1.7, maxWidth: 640, marginTop: -8, marginBottom: 20 }}>
        The marketplace is the largest unreached mission field inside most congregations. Nine campaigns, architected in sequence, to launch and sustain a business leaders community that meets monthly, holds each other accountable, and becomes the most generosity-generating ministry in the church — exactly the audience your business-owner clients belong to.
      </p>
      <div className="can-locked-item" style={{ display: "inline-flex", marginBottom: 34 }}><LockBadge /></div>

      <div style={{ borderTop: `1px solid ${LINE}` }}>
        {BUSINESS_LEADER_CAMPAIGNS.map((c) => {
          const isOpen = open === c.n;
          return (
            <div key={c.n} style={{ borderBottom: `1px solid ${LINE}` }}>
              <button onClick={() => setOpen(isOpen ? null : c.n)}
                style={{ width: "100%", background: "none", border: "none", cursor: "pointer", textAlign: "left", padding: "20px 0", display: "flex", gap: 20, alignItems: "flex-start" }}>
                <div className="can-serif" style={{ fontSize: 19, fontWeight: 700, color: GOLD, width: 30, flexShrink: 0 }}>{c.n}</div>
                <div style={{ flex: 1 }}>
                  <div className="can-serif" style={{ fontSize: 15.5, fontWeight: 700, color: NAVY, lineHeight: 1.3 }}>{c.title}</div>
                  <div className="can-label" style={{ fontSize: 8.5, color: GOLD, marginTop: 4 }}>{c.tag}</div>
                  {isOpen && <div className="can-fade-in" style={{ fontSize: 13, color: INK, marginTop: 12, lineHeight: 1.6, background: CREAM, borderLeft: `3px solid ${GOLD}`, padding: "12px 16px" }}>{c.desc}</div>}
                </div>
                <div className="can-label" style={{ fontSize: 16, color: GOLD, flexShrink: 0 }}>{isOpen ? "\u2013" : "+"}</div>
              </button>
            </div>
          );
        })}
      </div>

      <div style={{ marginTop: 50, background: NAVY, borderRadius: 4, padding: "34px 30px" }}>
        <Eyebrow dark>Family Legacy By Design</Eyebrow>
        <h2 className="can-serif" style={{ fontSize: "clamp(18px, 3vw, 22px)", fontWeight: 700, color: WHITE, margin: "16px 0 10px", lineHeight: 1.3 }}>
          Built on Tom Conway's Family Legacy By Design framework.
        </h2>
        <p style={{ fontSize: 13, color: "rgba(251,248,241,0.78)", lineHeight: 1.65, maxWidth: 620, marginBottom: 20 }}>
          "Seven Days of Built to Last" and the Family Legacy Builder both connect directly to this framework — the campaign architecture built specifically for ultra-high-net-worth families thinking about succession, exit, and what outlasts them.
        </p>
        <div style={{ display: "flex", flexDirection: "column", gap: 2 }}>
          {FAMILY_LEGACY_TITLES.map((t) => (
            <div key={t} style={{ fontSize: 12, color: "rgba(251,248,241,0.85)", padding: "9px 0", borderTop: "1px solid rgba(217,184,118,0.2)" }}>{t}</div>
          ))}
        </div>
      </div>

      <div style={{ marginTop: 40, textAlign: "center", background: CREAM, borderRadius: 4, padding: "40px 24px" }}>
        <p style={{ fontSize: 13, color: SLATE, maxWidth: 460, margin: "0 auto 16px", lineHeight: 1.6 }}>This entire catalog — plus the full Family Legacy By Design campaign library — unlocks with membership.</p>
        <button onClick={() => setPage("membership")} className="can-btn-gold can-label" style={{ background: GOLD, color: NAVY, border: "none", borderRadius: 22, padding: "12px 26px", fontSize: 11, fontWeight: 700, cursor: "pointer" }}>Unlock Full Access</button>
      </div>
    </PageShell>
  );
}

/* ---------------- PURPOSE BUILT BUSINESS HOOK PAGE ---------------- */
function PurposeBuiltBusinessHook({ setPage }) {
  const [openN, setOpenN] = useState(null);
  return (
    <PageShell eyebrow="Purpose Built Business™ — Secular Edition" title="The same architecture, for a secular or values-based audience.">
      <p style={{ color: SLATE, fontSize: 14, lineHeight: 1.7, maxWidth: 640, marginBottom: 24 }}>
        Purpose Built Business is a sister platform — the same nine-journey leadership development architecture as the Christian Business Leaders campaigns, reframed without a religious-language requirement. It's built for a client whose company or HR department needs a secular or interfaith-friendly leadership program, and it lives as its own branded experience.
      </p>
      <div style={{ background: NAVY, borderRadius: 4, padding: "26px 26px", marginBottom: 34 }}>
        <div className="can-label" style={{ fontSize: 10, color: GOLD_BRIGHT, marginBottom: 8 }}>Why this exists alongside the Christian edition</div>
        <p style={{ fontSize: 13, color: "rgba(251,248,241,0.85)", lineHeight: 1.65, margin: 0 }}>
          Not every client — or every client's company — wants explicitly religious framing, even when the underlying values (purpose, stewardship, excellence, generosity, servant leadership, legacy) are ones you already teach well. Purpose Built Business is that same substance, in language a secular HR department or a religiously mixed leadership team can bring in-house without friction.
        </p>
      </div>

      <div className="can-label" style={{ fontSize: 10, color: GOLD, marginBottom: 14 }}>The Nine Journeys</div>
      <div style={{ borderTop: `1px solid ${LINE}` }}>
        {PBB_JOURNEYS.map((j) => {
          const isOpen = openN === j.n;
          return (
            <div key={j.n} onClick={() => setOpenN(isOpen ? null : j.n)} style={{ borderBottom: `1px solid ${LINE}`, padding: "14px 0", cursor: "pointer", display: "flex", gap: 16, alignItems: "center" }}>
              <div className="can-serif" style={{ fontSize: 15, fontWeight: 700, color: GOLD, width: 24, flexShrink: 0 }}>{j.n}</div>
              <div style={{ flex: 1 }}>
                <div className="can-serif" style={{ fontWeight: 700, fontSize: 14 }}>{j.title}</div>
                <div className="can-label" style={{ fontSize: 8, color: SLATE, marginTop: 2 }}>{j.tag}</div>
              </div>
            </div>
          );
        })}
      </div>

      <div style={{ marginTop: 34, textAlign: "center", background: CREAM, borderRadius: 4, padding: "36px 24px" }}>
        <div className="can-serif" style={{ fontWeight: 700, fontSize: 18, color: NAVY, marginBottom: 10 }}>Purpose Built Business lives as its own site.</div>
        <p style={{ fontSize: 13, color: SLATE, maxWidth: 460, margin: "0 auto 16px", lineHeight: 1.6 }}>
          This page is the entry point — the full branded platform (nine journeys, corporate licensing, an assessment) is a separate experience for clients who need the secular framing specifically.
        </p>
        <button onClick={() => setPage("business-leaders")} className="can-btn-gold can-label" style={{ background: GOLD, color: NAVY, border: "none", borderRadius: 22, padding: "12px 26px", fontSize: 11, fontWeight: 700, cursor: "pointer" }}>See the Christian Edition</button>
      </div>
    </PageShell>
  );
}

/* ---------------- OFFERINGS FOR FAMILIES PAGE ---------------- */
function OfferingsFamiliesPage() {
  return (
    <PageShell eyebrow="Offerings for Families" title="What you actually hand your clients.">
      <p style={{ color: SLATE, fontSize: 14, lineHeight: 1.7, maxWidth: 620, marginTop: -8, marginBottom: 34 }}>
        Every resource below is client-facing — built to be handed to a family, not just discussed inside a meeting.
      </p>
      {FAMILY_OFFERINGS.map((o) => (
        <div key={o.name} style={{ borderTop: `1px solid ${LINE}`, padding: "20px 0" }}>
          <div className="can-serif" style={{ fontWeight: 700, fontSize: 16, color: NAVY, marginBottom: 6 }}>{o.name}</div>
          <div style={{ fontSize: 13, color: SLATE, lineHeight: 1.6, maxWidth: 620 }}>{o.desc}</div>
        </div>
      ))}
    </PageShell>
  );
}

/* ---------------- CHURCH PARTNERSHIP PAGE ---------------- */
function PartnershipPage() {
  return (
    <div className="can-fade-in">
      <div style={{ background: NAVY }}>
        <div style={{ maxWidth: 1240, margin: "0 auto", padding: "90px 28px" }}>
          <Eyebrow dark>Five Levels of Church Partnership</Eyebrow>
          <h1 className="can-serif" style={{ fontSize: "clamp(24px, 3vw, 32px)", fontWeight: 700, color: WHITE, maxWidth: 680, margin: "20px 0 0" }}>
            Begin with service. Build trust. Expand only when ministry value is proven.
          </h1>
          <div style={{ display: "flex", flexWrap: "wrap", gap: 0, marginTop: 50 }}>
            {LEVELS.map((l, i) => (
              <div key={l.n} style={{ flex: "1 1 180px", padding: "0 18px 0 0" }}>
                <div style={{ display: "flex", alignItems: "center", gap: 12, marginBottom: 14 }}>
                  <div style={{ width: 38, height: 38, borderRadius: "50%", border: `1.5px solid ${GOLD}`, display: "flex", alignItems: "center", justifyContent: "center", flexShrink: 0, background: "rgba(255,255,255,0.04)" }}>
                    <span className="can-serif" style={{ color: GOLD_BRIGHT, fontWeight: 700, fontSize: 15 }}>{l.n}</span>
                  </div>
                  {i < LEVELS.length - 1 && <div style={{ height: 1.5, background: "rgba(217,184,118,0.35)", flex: 1 }} />}
                </div>
                <div className="can-serif" style={{ fontSize: 14.5, fontWeight: 700, color: WHITE, marginBottom: 6 }}>{l.label}</div>
                <div style={{ fontSize: 12.5, color: "rgba(251,248,241,0.65)", lineHeight: 1.5 }}>{l.desc}</div>
              </div>
            ))}
          </div>
        </div>
      </div>

      <div style={{ maxWidth: 1240, margin: "0 auto", padding: "80px 28px" }}>
        <Eyebrow>The Partnership Covenant</Eyebrow>
        <h2 className="can-serif" style={{ fontSize: "clamp(20px, 3vw, 26px)", fontWeight: 700, color: NAVY, maxWidth: 640, margin: "20px 0 40px", lineHeight: 1.3 }}>
          Ministry first. Relationships second. Business outcomes, when appropriate, emerge through trust — never pressure.
        </h2>
        <div style={{ display: "grid", gridTemplateColumns: "repeat(auto-fit, minmax(260px, 1fr))", gap: 40 }}>
          <div>
            <div className="can-label" style={{ fontSize: 11, color: GOLD, marginBottom: 14 }}>What Pastors Fear</div>
            {PASTOR_FEARS.map((f) => <div key={f} style={{ padding: "10px 0", borderTop: `1px solid ${LINE}`, fontSize: 13.5 }}>{f}</div>)}
          </div>
          <div>
            <div className="can-label" style={{ fontSize: 11, color: GOLD, marginBottom: 14 }}>What Advisors Fear</div>
            {ADVISOR_FEARS.map((f) => <div key={f} style={{ padding: "10px 0", borderTop: `1px solid ${LINE}`, fontSize: 13.5 }}>{f}</div>)}
          </div>
        </div>
        <div style={{ marginTop: 30, background: CREAM, borderLeft: `3px solid ${GOLD}`, padding: "18px 22px", fontSize: 13.5, lineHeight: 1.7 }}>
          No selling from the platform &middot; No church-member lists &middot; No product promotion &middot; No implied endorsement &middot; Clear compliance standards &middot; Pastor oversight &middot; Voluntary participation &middot; Confidentiality &middot; Family-first service
        </div>
      </div>

      <div style={{ background: CREAM }}>
        <div style={{ maxWidth: 1240, margin: "0 auto", padding: "80px 28px" }}>
          <Eyebrow>How to Partner with a Local Church</Eyebrow>
          <h2 className="can-serif" style={{ fontSize: "clamp(20px, 3vw, 26px)", fontWeight: 700, color: NAVY, maxWidth: 640, margin: "20px 0 44px", lineHeight: 1.3 }}>
            A seven-step pathway from first conversation to annual ministry plan.
          </h2>
          <div>
            {PARTNER_STEPS.map((s, i) => (
              <div key={s.t} style={{ display: "flex", gap: 20, paddingBottom: i < PARTNER_STEPS.length - 1 ? 28 : 0 }}>
                <div style={{ display: "flex", flexDirection: "column", alignItems: "center", width: 34, flexShrink: 0 }}>
                  <div style={{ width: 34, height: 34, borderRadius: "50%", background: NAVY, color: GOLD_BRIGHT, display: "flex", alignItems: "center", justifyContent: "center", fontFamily: "Playfair Display", fontWeight: 700, fontSize: 14, flexShrink: 0 }}>{i + 1}</div>
                  {i < PARTNER_STEPS.length - 1 && <div style={{ width: 1.5, flex: 1, background: GOLD, opacity: 0.4, marginTop: 4 }} />}
                </div>
                <div style={{ paddingBottom: 4 }}>
                  <div className="can-serif" style={{ fontWeight: 700, fontSize: 15, color: NAVY, marginBottom: 4 }}>{s.t}</div>
                  <div style={{ fontSize: 13, color: SLATE, lineHeight: 1.55 }}>{s.d}</div>
                </div>
              </div>
            ))}
          </div>
          <div style={{ marginTop: 44, background: WHITE, border: `1px solid ${LINE}`, borderRadius: 4, padding: "22px 24px" }}>
            <div className="can-label" style={{ fontSize: 10, color: GOLD, marginBottom: 10 }}>A Good First Pilot</div>
            <div style={{ display: "flex", flexWrap: "wrap", gap: 8 }}>
              {FIRST_PILOTS.map((p) => <span key={p} className="can-label" style={{ fontSize: 10, color: NAVY, background: CREAM, border: `1px solid ${LINE}`, padding: "7px 12px", borderRadius: 16 }}>{p}</span>)}
            </div>
          </div>
        </div>
      </div>

      <div style={{ maxWidth: 1240, margin: "0 auto", padding: "80px 28px" }}>
        <Eyebrow>A Seminar for Every Season</Eyebrow>
        <h2 className="can-serif" style={{ fontSize: "clamp(20px, 3vw, 26px)", fontWeight: 700, color: NAVY, maxWidth: 640, margin: "20px 0 40px", lineHeight: 1.3 }}>
          Turn trusted teaching into practical family action.
        </h2>
        <div style={{ display: "grid", gridTemplateColumns: "repeat(auto-fit, minmax(220px, 1fr))", gap: "10px 20px" }}>
          {SEMINARS.map((s) => <div key={s} style={{ fontSize: 13, color: INK, padding: "10px 0", borderBottom: `1px solid ${LINE}` }}>{s}</div>)}
        </div>
        <div style={{ marginTop: 26, fontSize: 12.5, color: SLATE, lineHeight: 1.7 }}>
          Every seminar includes a pastor introduction, biblical foundation, advisor notes, participant workbook, discussion questions, exercises, next steps, follow-up resources, compliance-safe language, and a no-sales policy.
        </div>
      </div>
    </div>
  );
}

/* ---------------- MEMBERSHIP PAGE ---------------- */
function MembershipPage({ setPage }) {
  const [activePathway, setActivePathway] = useState(PATHWAYS[0].key);
  const current = PATHWAYS.find((p) => p.key === activePathway);
  return (
    <PageShell eyebrow="One Network. Five Growth Pathways." title="A clear member experience built around your real work.">
      <p style={{ color: SLATE, fontSize: 13.5, marginTop: -10, marginBottom: 22 }}>Choose the pathway closest to what you need right now — the recommendations below change with it.</p>
      <div style={{ display: "flex", gap: 10, marginTop: 0, flexWrap: "wrap", borderBottom: `1px solid ${LINE}` }}>
        {PATHWAYS.map((p) => {
          const active = activePathway === p.key;
          return (
            <button key={p.key} onClick={() => setActivePathway(p.key)} className="can-label"
              style={{ background: "none", border: "none", cursor: "pointer", padding: "12px 4px", marginRight: 22, fontSize: 11.5, fontWeight: 700, color: active ? NAVY : SLATE, borderBottom: active ? `2px solid ${GOLD}` : "2px solid transparent", marginBottom: -1 }}>
              {p.label}
            </button>
          );
        })}
      </div>
      <div className="can-fade-in" key={activePathway} style={{ marginTop: 30, display: "flex", flexWrap: "wrap", gap: 14 }}>
        {current.items.map((it) => (
          <div key={it} style={{ background: CREAM, borderLeft: `3px solid ${GOLD}`, padding: "16px 20px", fontFamily: "Playfair Display", fontWeight: 700, fontSize: 14.5, color: NAVY, minWidth: 180 }}>{it}</div>
        ))}
      </div>

      <div className="can-fade-in" key={"rec-" + activePathway} style={{ marginTop: 30, background: NAVY, borderRadius: 4, padding: "26px 26px" }}>
        <div className="can-label" style={{ fontSize: 10, color: GOLD_BRIGHT, marginBottom: 14 }}>Recommended for {current.label}</div>
        <div style={{ display: "flex", gap: 14, flexWrap: "wrap" }}>
          {current.recommend.map((r) => (
            <button key={r.label} onClick={() => setPage(r.page)} className="can-label"
              style={{ background: "rgba(255,255,255,0.06)", border: `1px solid ${GOLD}`, color: GOLD_BRIGHT, borderRadius: 20, padding: "10px 16px", fontSize: 10.5, fontWeight: 700, cursor: "pointer" }}>
              {r.label} &rarr;
            </button>
          ))}
        </div>
      </div>

      <div style={{ marginTop: 26, padding: "24px 26px", background: CREAM, borderRadius: 4 }}>
        <div className="can-label" style={{ fontSize: 10.5, color: GOLD, marginBottom: 8 }}>Pricing</div>
        <p style={{ color: INK, fontSize: 13.5, lineHeight: 1.7, margin: 0 }}>
          Membership tiers are organized around these five pathways rather than a generic plan ladder. Specific pricing is confirmed during your application conversation.
        </p>
        <button onClick={() => setPage("find-advisor")} className="can-btn-gold can-label" style={{ marginTop: 16, background: GOLD, color: NAVY, border: "none", borderRadius: 22, padding: "11px 22px", fontSize: 11, fontWeight: 700, cursor: "pointer" }}>
          Apply for Membership
        </button>
      </div>

      <div style={{ marginTop: 70 }}>
        <Eyebrow>The Strategic Advantage</Eyebrow>
        <h2 className="can-serif" style={{ fontSize: "clamp(20px, 3vw, 26px)", fontWeight: 700, color: NAVY, maxWidth: 600, margin: "20px 0 40px", lineHeight: 1.3 }}>
          What traditional advisor networks provide — and what is usually missing.
        </h2>
        <div style={{ display: "grid", gridTemplateColumns: "repeat(auto-fit, minmax(260px, 1fr))", gap: 40 }}>
          <div>
            <div className="can-label" style={{ fontSize: 11, color: SLATE, marginBottom: 14 }}>Most Advisor Networks Provide</div>
            {MOST_PROVIDE.map((m) => <div key={m} style={{ padding: "10px 0", borderTop: `1px solid ${LINE}`, fontSize: 13.5, color: SLATE }}>{m}</div>)}
          </div>
          <div>
            <div className="can-label" style={{ fontSize: 11, color: GOLD, marginBottom: 14 }}>The Christian Advisor Network Adds</div>
            {NETWORK_ADDS.map((m) => <div key={m} style={{ padding: "10px 0", borderTop: `1px solid ${LINE}`, fontSize: 13.5, color: INK, fontWeight: 500 }}>{m}</div>)}
          </div>
        </div>
      </div>
    </PageShell>
  );
}

/* ---------------- FIND AN ADVISOR PAGE ---------------- */
function FindAdvisorPage({ setPage }) {
  const [location, setLocation] = useState("");
  const [specialty, setSpecialty] = useState("All Specialties");
  const [searched, setSearched] = useState(false);
  const [requested, setRequested] = useState({});

  const filtered = SAMPLE_ADVISORS.filter((a) => {
    const matchesLocation = location.trim() === "" || a.city.toLowerCase().includes(location.trim().toLowerCase());
    const matchesSpecialty = specialty === "All Specialties" || a.specialties.includes(specialty);
    return matchesLocation && matchesSpecialty;
  });

  return (
    <div className="can-fade-in">
      <div style={{ background: `linear-gradient(165deg, ${NAVY} 0%, #0E1930 100%)` }}>
        <div style={{ maxWidth: 1240, margin: "0 auto", padding: "80px 28px 60px" }}>
          <Eyebrow dark>Find an Advisor</Eyebrow>
          <h1 className="can-serif" style={{ fontSize: "clamp(26px, 4vw, 38px)", fontWeight: 700, color: WHITE, maxWidth: 640, margin: "20px 0 0", lineHeight: 1.2 }}>
            Find a Christian financial advisor near you.
          </h1>
          <p style={{ color: "rgba(251,248,241,0.75)", fontSize: 14.5, marginTop: 16, maxWidth: 560, lineHeight: 1.6 }}>
            Search Christian Advisor Network members by location and specialty — every listed advisor operates under the Network's partnership covenant and compliance standards.
          </p>
          <div style={{ display: "flex", gap: 12, marginTop: 34, flexWrap: "wrap" }}>
            <input value={location} onChange={(e) => setLocation(e.target.value)} placeholder="City or state"
              style={{ flex: "1 1 220px", background: "rgba(255,255,255,0.06)", border: "1px solid rgba(217,184,118,0.35)", borderRadius: 8, padding: "13px 16px", color: WHITE, fontSize: 14, fontFamily: "Inter", outline: "none" }} />
            <select value={specialty} onChange={(e) => setSpecialty(e.target.value)}
              style={{ flex: "1 1 220px", background: "rgba(255,255,255,0.06)", border: "1px solid rgba(217,184,118,0.35)", borderRadius: 8, padding: "13px 16px", color: WHITE, fontSize: 14, fontFamily: "Inter", outline: "none" }}>
              <option style={{ color: INK }}>All Specialties</option>
              {SPECIALTIES.map((s) => <option key={s} style={{ color: INK }}>{s}</option>)}
            </select>
            <button onClick={() => setSearched(true)} className="can-btn-gold can-label" style={{ background: GOLD, color: NAVY, border: "none", borderRadius: 8, padding: "13px 26px", fontSize: 12, fontWeight: 700, cursor: "pointer" }}>Search Directory</button>
          </div>
        </div>
      </div>

      <div style={{ maxWidth: 1240, margin: "0 auto", padding: "60px 28px" }}>
        <p className="can-label" style={{ fontSize: 10.5, color: SLATE, marginBottom: 26 }}>
          {searched ? `${filtered.length} matching listing${filtered.length === 1 ? "" : "s"}` : "SAMPLE LISTINGS — SHOWING WHAT A REAL LISTING LOOKS LIKE"}
        </p>
        <div style={{ display: "grid", gridTemplateColumns: "repeat(auto-fit, minmax(280px, 1fr))", gap: 22 }}>
          {filtered.map((a, i) => (
            <div key={i} className="can-card" style={{ border: `1px solid ${LINE}`, borderRadius: 4, padding: "26px 24px", background: WHITE }}>
              <div className="can-label" style={{ fontSize: 9, color: GOLD, marginBottom: 12, border: `1px solid ${GOLD}`, display: "inline-block", padding: "3px 8px", borderRadius: 12 }}>Sample Listing</div>
              <div className="can-serif" style={{ fontWeight: 700, fontSize: 17, color: NAVY }}>{a.practice}</div>
              <div style={{ fontSize: 12.5, color: SLATE, marginTop: 4, marginBottom: 12 }}>{a.city}</div>
              <p style={{ fontSize: 13, color: INK, lineHeight: 1.55, marginBottom: 14 }}>{a.bio}</p>
              <div style={{ display: "flex", flexWrap: "wrap", gap: 6 }}>{a.specialties.map((s) => <span key={s} className="can-label" style={{ fontSize: 9, color: GOLD, background: CREAM, padding: "5px 9px", borderRadius: 10 }}>{s}</span>)}</div>
              {requested[a.practice] ? (
                <div className="can-fade-in can-label" style={{ marginTop: 18, textAlign: "center", fontSize: 10, fontWeight: 700, color: NAVY, background: CREAM, borderRadius: 20, padding: "10px 0" }}>&#10003; Request Sent</div>
              ) : (
                <button onClick={() => setRequested((r) => ({ ...r, [a.practice]: true }))} className="can-label" style={{ marginTop: 18, width: "100%", background: "none", border: `1px solid ${NAVY}`, color: NAVY, borderRadius: 20, padding: "10px 0", fontSize: 10.5, fontWeight: 700, cursor: "pointer" }}>Request an Introduction</button>
              )}
            </div>
          ))}
        </div>
        {filtered.length === 0 && <div style={{ textAlign: "center", padding: "50px 20px", color: SLATE, fontSize: 14 }}>No listings match that search yet.</div>}
        <div style={{ marginTop: 60, textAlign: "center", background: CREAM, borderRadius: 4, padding: "48px 24px" }}>
          <div className="can-serif" style={{ fontWeight: 700, fontSize: 20, color: NAVY, marginBottom: 10 }}>This directory is just getting started.</div>
          <p style={{ fontSize: 13.5, color: SLATE, maxWidth: 440, margin: "0 auto 20px", lineHeight: 1.6 }}>Be among the first advisors listed — membership includes a public profile churches and families can find.</p>
          <button onClick={() => setPage("membership")} className="can-btn-gold can-label" style={{ background: GOLD, color: NAVY, border: "none", borderRadius: 22, padding: "12px 26px", fontSize: 11, fontWeight: 700, cursor: "pointer" }}>List Your Practice</button>
        </div>
      </div>
    </div>
  );
}

/* ---------------- CASE STUDIES / FAQ / ABOUT ---------------- */
function CaseStudiesPage() {
  return (
    <PageShell eyebrow="Success Stories" title="What advisors are building.">
      <p style={{ color: SLATE, fontSize: 13, fontStyle: "italic", marginTop: -12, marginBottom: 30 }}>Stories below are shown in placeholder format, ready to be replaced with your practice's own results.</p>
      <div style={{ display: "grid", gridTemplateColumns: "repeat(auto-fit, minmax(280px, 1fr))", gap: 22 }}>
        {CASE_STUDIES.map((c, i) => (
          <div key={i} className="can-card" style={{ border: `1px solid ${LINE}`, borderRadius: 4, padding: "26px 24px", background: CREAM }}>
            <div className="can-serif" style={{ fontWeight: 700, fontSize: 16.5, color: NAVY, marginBottom: 4 }}>{c.practice}</div>
            <div className="can-label" style={{ fontSize: 9.5, color: SLATE, marginBottom: 14 }}>{c.type}</div>
            <div className="can-label" style={{ fontSize: 9.5, color: GOLD, marginBottom: 10 }}>{c.resource}</div>
            <p style={{ fontSize: 13, color: INK, lineHeight: 1.6, margin: 0 }}>{c.result}</p>
          </div>
        ))}
      </div>
    </PageShell>
  );
}

function FaqPage() {
  const [open, setOpen] = useState(0);
  return (
    <PageShell eyebrow="Frequently Asked Questions" title="Honest answers before you decide.">
      <div style={{ borderTop: `1px solid ${LINE}` }}>
        {FAQS.map((f, i) => {
          const isOpen = open === i;
          return (
            <div key={f.q} style={{ borderBottom: `1px solid ${LINE}` }}>
              <button onClick={() => setOpen(isOpen ? null : i)} style={{ width: "100%", background: "none", border: "none", cursor: "pointer", textAlign: "left", padding: "20px 0", display: "flex", justifyContent: "space-between", alignItems: "flex-start", gap: 16 }}>
                <div className="can-serif" style={{ fontWeight: 700, fontSize: 15.5, color: NAVY, lineHeight: 1.4 }}>{f.q}</div>
                <div className="can-label" style={{ fontSize: 16, color: GOLD, flexShrink: 0 }}>{isOpen ? "\u2013" : "+"}</div>
              </button>
              {isOpen && <div className="can-fade-in" style={{ fontSize: 13.5, color: SLATE, lineHeight: 1.65, paddingBottom: 22, maxWidth: 680 }}>{f.a}</div>}
            </div>
          );
        })}
      </div>
    </PageShell>
  );
}

function AboutPage() {
  return (
    <PageShell eyebrow="The Foundation" title="Ron Blue's biblical financial wisdom, joined to LifeTogether's campaign and curriculum systems.">
      <div style={{ display: "grid", gridTemplateColumns: "1.1fr 0.9fr", gap: 50, alignItems: "center", marginTop: 10 }}>
        <div>
          <p style={{ color: SLATE, fontSize: 14.5, lineHeight: 1.75 }}>
            Twenty-five years of churchwide campaign, curriculum, and small-group ministry experience — brought together into one platform built specifically for Christian financial advisors, and the pastors and families they serve.
          </p>
          <div style={{ marginTop: 24, fontFamily: "Archivo", fontWeight: 500, fontSize: 11, letterSpacing: "0.03em", color: SLATE, lineHeight: 2 }}>
            BRAND ARCHITECTURE: Christian Advisor Network™ &middot; Christian Advisor Growth Builder™ &middot; Family Legacy Builder™ &middot; Financial Wisdom Ministry™ &middot; Pastor and Church Resource Library™ &middot; Trusted Guide Academy™
          </div>
        </div>
        <Photo caption="Photography — Advisor's Office, Warm Light, Family Photo on Desk" style={{ height: 300 }} />
      </div>
    </PageShell>
  );
}

/* =====================================================================
   FAMILY JOURNEY BUILDER — seven live modules
===================================================================== */
function Field({ label, children }) {
  return <div style={{ marginBottom: 14 }}>
    <div className="can-label" style={{ fontSize: 9.5, color: SLATE, marginBottom: 5 }}>{label}</div>
    {children}
  </div>;
}
function ModuleShell({ eyebrow, title, subtitle, children }) {
  return (
    <div className="can-fade-in" style={{ maxWidth: 980, margin: "0 auto", padding: "60px 32px 90px" }}>
      <Eyebrow>{eyebrow}</Eyebrow>
      <h1 className="can-serif" style={{ fontSize: 26, fontWeight: 700, color: NAVY, marginBottom: 8, marginTop: 16 }}>{title}</h1>
      {subtitle && <p style={{ fontSize: 14, color: SLATE, lineHeight: 1.6, maxWidth: 640, marginBottom: 28 }}>{subtitle}</p>}
      {children}
    </div>
  );
}

function FjbOverview({ setPage }) {
  const cards = [
    ["fjb-map", "Family Map", "Compare assessments across the family into one shared picture."],
    ["fjb-retention", "Retention", "Milestone tracking and the Next-Gen Bridge Journey."],
    ["fjb-relational", "Relational Bonds", "Meeting facilitator and multi-generational calendar."],
    ["fjb-aum", "AUM Growth", "Complete Financial Picture and Business Exit Readiness."],
    ["fjb-steward", "Successor & Steward Journey", "Covey-sequenced, built on the 17 Flourishing dimensions."],
    ["fjb-business", "Family Business", "Governance, roles, and readiness."],
    ["fjb-stories", "Stories", "Legacy, history, and value-based stories for the next generation."],
  ];
  return (
    <ModuleShell eyebrow="Family Journey Builder" title="Seven modules. One family journey." subtitle="A fully customized plan beyond the finances — focused on relationships and family goals, individually and corporately. Pick any module below.">
      <div style={{ display: "grid", gridTemplateColumns: "repeat(auto-fit, minmax(260px, 1fr))", gap: 16 }}>
        {cards.map(([id, t, d]) => (
          <div key={id} onClick={() => setPage(id)} className="fjb-card can-card" style={{ padding: "22px 20px", background: CREAM, cursor: "pointer" }}>
            <div className="can-serif" style={{ fontWeight: 700, fontSize: 16, color: NAVY, marginBottom: 6 }}>{t}</div>
            <div style={{ fontSize: 12.5, color: SLATE, lineHeight: 1.5, marginBottom: 12 }}>{d}</div>
            <div className="can-label" style={{ fontSize: 10, color: GOLD, fontWeight: 700 }}>Open &rarr;</div>
          </div>
        ))}
      </div>
    </ModuleShell>
  );
}

const MAP_DIMENSIONS = ["Faith", "Family", "Finances", "Purpose", "Communication", "Generosity"];
function FjbFamilyMap() {
  const [a, setA] = useState(Object.fromEntries(MAP_DIMENSIONS.map(d => [d, 6])));
  const [b, setB] = useState(Object.fromEntries(MAP_DIMENSIONS.map(d => [d, 6])));
  const [names, setNames] = useState({ a: "Spouse A", b: "Spouse B" });
  const [generated, setGenerated] = useState(false);

  const starters = {
    Faith: "What would it look like for our faith to shape one more decision together this year?",
    Family: "What's one family rhythm we say we value but haven't actually protected?",
    Finances: "Where do we quietly see money differently, even if we've never said it out loud?",
    Purpose: "If we're honest, whose purpose has been driving our decisions lately?",
    Communication: "What's a conversation we keep almost having?",
    Generosity: "What would it feel like to give more than feels comfortable, together?",
  };

  return (
    <ModuleShell eyebrow="Family Journey Builder — Family Map" title="Compare assessments into one shared picture." subtitle="Enter scores (1–10) for two family members, then generate the map. Divergences of 3+ points get a suggested conversation starter.">
      <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: 24, marginBottom: 24 }}>
        {[["a", a, setA], ["b", b, setB]].map(([key, state, setState]) => (
          <div key={key} className="fjb-card" style={{ padding: 20 }}>
            <input className="fjb-input" style={{ width: "100%", marginBottom: 14, fontWeight: 700 }} value={names[key]}
              onChange={(e) => setNames((n) => ({ ...n, [key]: e.target.value }))} />
            {MAP_DIMENSIONS.map((d) => (
              <div key={d} style={{ marginBottom: 12 }}>
                <div style={{ display: "flex", justifyContent: "space-between", fontSize: 12, marginBottom: 3 }}>
                  <span>{d}</span><span style={{ fontWeight: 700, color: GOLD }}>{state[d]}</span>
                </div>
                <input type="range" min="1" max="10" value={state[d]} onChange={(e) => setState((s) => ({ ...s, [d]: Number(e.target.value) }))} style={{ width: "100%" }} />
              </div>
            ))}
          </div>
        ))}
      </div>
      <button onClick={() => setGenerated(true)} className="can-btn-gold can-label" style={{ background: GOLD, color: NAVY, border: "none", borderRadius: 22, padding: "12px 26px", fontSize: 11, fontWeight: 700, cursor: "pointer" }}>Generate Map</button>

      {generated && (
        <div className="can-fade-in" style={{ marginTop: 28 }}>
          {MAP_DIMENSIONS.map((d) => {
            const diff = Math.abs(a[d] - b[d]);
            const diverge = diff >= 3;
            return (
              <div key={d} style={{ borderTop: `1px solid ${LINE}`, padding: "14px 0" }}>
                <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center", marginBottom: 6 }}>
                  <span className="can-serif" style={{ fontWeight: 700, fontSize: 14 }}>{d}</span>
                  {diverge && <span className="can-label" style={{ fontSize: 9, color: AMBER, border: `1px solid ${AMBER}`, borderRadius: 10, padding: "2px 8px" }}>Divergence</span>}
                </div>
                <div style={{ display: "flex", gap: 6, alignItems: "center" }}>
                  <div style={{ flex: 1, height: 8, background: LINE, borderRadius: 4, position: "relative" }}>
                    <div style={{ position: "absolute", left: 0, top: 0, bottom: 0, width: `${a[d] * 10}%`, background: NAVY, borderRadius: 4, opacity: 0.85 }} />
                  </div>
                  <span style={{ fontSize: 10, width: 60 }}>{names.a}</span>
                </div>
                <div style={{ display: "flex", gap: 6, alignItems: "center", marginTop: 4 }}>
                  <div style={{ flex: 1, height: 8, background: LINE, borderRadius: 4, position: "relative" }}>
                    <div style={{ position: "absolute", left: 0, top: 0, bottom: 0, width: `${b[d] * 10}%`, background: GOLD, borderRadius: 4 }} />
                  </div>
                  <span style={{ fontSize: 10, width: 60 }}>{names.b}</span>
                </div>
                {diverge && <div style={{ marginTop: 8, fontSize: 12.5, fontStyle: "italic", color: NAVY, background: CREAM, padding: "8px 12px", borderLeft: `3px solid ${GOLD}` }}>{starters[d]}</div>}
              </div>
            );
          })}
        </div>
      )}
    </ModuleShell>
  );
}

const MILESTONE_TYPES = ["Birth", "Marriage", "Death", "Business Sale", "Retirement", "Health Event", "Graduation", "Inheritance"];
const OUTREACH = {
  Birth: "Send a handwritten note; ask if a custodial account conversation would help.",
  Marriage: "Introduce yourself to the new spouse; offer a no-pressure intro meeting.",
  Death: "Reach out personally within 48 hours; do not discuss assets yet.",
  "Business Sale": "Offer a liquidity-event planning conversation before the sale closes.",
  Retirement: "Schedule a purpose-and-income conversation, not just a withdrawal plan.",
  "Health Event": "Check in personally; ask if documents need review, not portfolio.",
  Graduation: "Send congratulations; offer a first financial-literacy conversation.",
  Inheritance: "Offer to walk the beneficiary through the Complete Financial Picture.",
};
const BRIDGE_STAGES = [
  ["Introduce", "Meet the adult children in a low-stakes, non-financial setting."],
  ["Include", "Invite them to observe one family meeting, without a formal role yet."],
  ["Educate", "Walk them through the Family Map and one Builder, at their pace."],
  ["Involve", "Give them one real, small decision to weigh in on."],
  ["Transition", "Formally introduce them as a party to the ongoing relationship."],
];
function FjbRetention() {
  const [milestones, setMilestones] = useState([
    { name: "Sarah's college graduation", type: "Graduation", date: "2026-05-15" },
  ]);
  const [form, setForm] = useState({ name: "", type: MILESTONE_TYPES[0], date: "" });
  const [stages, setStages] = useState(Array(BRIDGE_STAGES.length).fill(false));

  const addMilestone = () => {
    if (!form.name || !form.date) return;
    setMilestones((m) => [...m, form].sort((x, y) => x.date.localeCompare(y.date)));
    setForm({ name: "", type: MILESTONE_TYPES[0], date: "" });
  };
  const completedCount = stages.filter(Boolean).length;

  return (
    <ModuleShell eyebrow="Family Journey Builder — Retention" title="Milestone Tracker & the Next-Gen Bridge Journey" subtitle="Track the moments most likely to trigger a switch — and build the relationship with the next generation before any wealth transfers.">
      <div className="fjb-card" style={{ padding: 22, marginBottom: 30 }}>
        <div className="can-serif" style={{ fontWeight: 700, fontSize: 16, marginBottom: 14 }}>Milestone & Trigger Event Tracker</div>
        <div style={{ display: "flex", gap: 10, flexWrap: "wrap", marginBottom: 16 }}>
          <input className="fjb-input" placeholder="Milestone name" value={form.name} onChange={(e) => setForm((f) => ({ ...f, name: e.target.value }))} style={{ flex: "1 1 200px" }} />
          <select className="fjb-input" value={form.type} onChange={(e) => setForm((f) => ({ ...f, type: e.target.value }))} style={{ flex: "1 1 160px" }}>
            {MILESTONE_TYPES.map((t) => <option key={t}>{t}</option>)}
          </select>
          <input className="fjb-input" type="date" value={form.date} onChange={(e) => setForm((f) => ({ ...f, date: e.target.value }))} style={{ flex: "1 1 160px" }} />
          <button onClick={addMilestone} className="can-btn-gold can-label" style={{ background: NAVY, color: WHITE, border: "none", borderRadius: 6, padding: "9px 18px", fontSize: 11, fontWeight: 700, cursor: "pointer" }}>Add</button>
        </div>
        {milestones.map((m, i) => (
          <div key={i} style={{ borderTop: `1px solid ${LINE}`, padding: "12px 0" }}>
            <div style={{ display: "flex", justifyContent: "space-between" }}>
              <span style={{ fontWeight: 600, fontSize: 13.5 }}>{m.name}</span>
              <span className="can-label" style={{ fontSize: 9.5, color: GOLD }}>{m.type} &middot; {m.date}</span>
            </div>
            <div style={{ fontSize: 12, color: SLATE, marginTop: 4, fontStyle: "italic" }}>Suggested: {OUTREACH[m.type]}</div>
          </div>
        ))}
      </div>

      <div className="fjb-card" style={{ padding: 22 }}>
        <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center", marginBottom: 16 }}>
          <div className="can-serif" style={{ fontWeight: 700, fontSize: 16 }}>The Next-Gen Bridge Journey</div>
          <span className="can-label" style={{ fontSize: 10, color: GOLD }}>{completedCount}/5 stages</span>
        </div>
        <div style={{ height: 6, background: LINE, borderRadius: 3, marginBottom: 20 }}>
          <div style={{ height: 6, width: `${(completedCount / 5) * 100}%`, background: GOLD, borderRadius: 3, transition: "width .3s ease" }} />
        </div>
        {BRIDGE_STAGES.map(([t, d], i) => (
          <div key={t} onClick={() => setStages((s) => s.map((v, idx) => idx === i ? !v : v))}
            style={{ display: "flex", gap: 14, alignItems: "flex-start", padding: "10px 0", cursor: "pointer", borderTop: i > 0 ? `1px solid ${LINE}` : "none" }}>
            <div style={{ width: 22, height: 22, borderRadius: "50%", border: `1.5px solid ${stages[i] ? GREEN : GOLD}`, background: stages[i] ? GREEN : "transparent", flexShrink: 0, marginTop: 2, display: "flex", alignItems: "center", justifyContent: "center", color: WHITE, fontSize: 11 }}>
              {stages[i] ? "\u2713" : i + 1}
            </div>
            <div>
              <div style={{ fontWeight: 700, fontSize: 13.5, textDecoration: stages[i] ? "line-through" : "none", color: stages[i] ? SLATE : INK }}>{t}</div>
              <div style={{ fontSize: 12, color: SLATE, marginTop: 2 }}>{d}</div>
            </div>
          </div>
        ))}
      </div>
    </ModuleShell>
  );
}

const MEETING_TYPES = {
  "Annual Family Meeting": ["What went well this year as a family?", "What's one thing we should stop doing?", "What's our shared priority for next year?", "Who needs more support from the rest of us right now?"],
  "Values Conversation": ["What value did our parents/grandparents model best?", "What value do we want to be known for in twenty years?", "Where have we drifted from what we say we believe?"],
  "Business Update": ["What's the state of the business in plain language?", "What decision is coming that affects the family?", "Where do we need more transparency?"],
  "Generosity Planning": ["What causes matter most to each of us right now?", "Should we give individually or as a family this year?", "What would it look like to involve the kids in this decision?"],
  "Estate Review": ["Does everyone understand the current plan?", "Has anything changed that the plan doesn't reflect yet?", "What questions has no one asked out loud?"],
};
function FjbRelationalBonds() {
  const [meetingType, setMeetingType] = useState(Object.keys(MEETING_TYPES)[0]);
  const [dates, setDates] = useState([
    { name: "Mom's birthday", date: "2026-09-12", who: "Mother" },
    { name: "Anniversary", date: "2026-06-03", who: "Parents" },
  ]);
  const [form, setForm] = useState({ name: "", date: "", who: "" });

  const addDate = () => {
    if (!form.name || !form.date) return;
    setDates((d) => [...d, form].sort((a, b) => a.date.localeCompare(b.date)));
    setForm({ name: "", date: "", who: "" });
  };

  return (
    <ModuleShell eyebrow="Family Journey Builder — Relational Bonds" title="Family Meeting Facilitator & Multi-Generational Calendar" subtitle="Tools and planners for becoming part of the family's rhythm, not just its reviews.">
      <div className="fjb-card" style={{ padding: 22, marginBottom: 30 }}>
        <div className="can-serif" style={{ fontWeight: 700, fontSize: 16, marginBottom: 14 }}>Family Meeting Facilitator</div>
        <select className="fjb-input" value={meetingType} onChange={(e) => setMeetingType(e.target.value)} style={{ marginBottom: 16, width: "100%", maxWidth: 320 }}>
          {Object.keys(MEETING_TYPES).map((t) => <option key={t}>{t}</option>)}
        </select>
        <div className="can-label" style={{ fontSize: 9.5, color: GOLD, marginBottom: 8 }}>Suggested Agenda</div>
        {MEETING_TYPES[meetingType].map((q, i) => (
          <div key={i} style={{ display: "flex", gap: 10, padding: "8px 0", borderTop: `1px solid ${LINE}` }}>
            <span style={{ color: GOLD, fontWeight: 700, fontSize: 12 }}>{i + 1}</span>
            <span style={{ fontSize: 13 }}>{q}</span>
          </div>
        ))}
      </div>

      <div className="fjb-card" style={{ padding: 22 }}>
        <div className="can-serif" style={{ fontWeight: 700, fontSize: 16, marginBottom: 14 }}>Multi-Generational Calendar</div>
        <div style={{ display: "flex", gap: 10, flexWrap: "wrap", marginBottom: 16 }}>
          <input className="fjb-input" placeholder="Event name" value={form.name} onChange={(e) => setForm((f) => ({ ...f, name: e.target.value }))} style={{ flex: "1 1 180px" }} />
          <input className="fjb-input" placeholder="Who (e.g. Grandma)" value={form.who} onChange={(e) => setForm((f) => ({ ...f, who: e.target.value }))} style={{ flex: "1 1 160px" }} />
          <input className="fjb-input" type="date" value={form.date} onChange={(e) => setForm((f) => ({ ...f, date: e.target.value }))} style={{ flex: "1 1 160px" }} />
          <button onClick={addDate} className="can-btn-gold can-label" style={{ background: NAVY, color: WHITE, border: "none", borderRadius: 6, padding: "9px 18px", fontSize: 11, fontWeight: 700, cursor: "pointer" }}>Add</button>
        </div>
        {dates.map((d, i) => (
          <div key={i} style={{ display: "flex", justifyContent: "space-between", padding: "9px 0", borderTop: `1px solid ${LINE}`, fontSize: 13 }}>
            <span>{d.name} {d.who && <span style={{ color: SLATE }}>&middot; {d.who}</span>}</span>
            <span className="can-label" style={{ fontSize: 10, color: GOLD }}>{d.date}</span>
          </div>
        ))}
      </div>
    </ModuleShell>
  );
}

const ASSET_CATEGORIES = ["Investment Accounts", "Retirement Accounts", "Real Estate", "Business Interests", "Life Insurance", "Other Advisory Relationships"];
function FjbAumGrowth() {
  const [assets, setAssets] = useState(Object.fromEntries(ASSET_CATEGORIES.map((c) => [c, "unknown"])));
  const [exitScores, setExitScores] = useState({ "Financial readiness": 5, "Successor readiness": 5, "Legal & tax structure": 5, "Emotional readiness": 5, "Post-exit purpose": 5 });

  const managedCount = Object.values(assets).filter((v) => v === "managed").length;
  const avgExit = Object.values(exitScores).reduce((a, b) => a + b, 0) / Object.keys(exitScores).length;
  const exitLevel = avgExit < 4 ? "Early — mostly unexplored" : avgExit < 7 ? "Developing — real progress made" : "Advanced — largely exit-ready";

  return (
    <ModuleShell eyebrow="Family Journey Builder — AUM Growth" title="Complete Financial Picture & Business Exit Readiness" subtitle="Explicitly permission-based — this helps the family see the whole picture. It is never framed as prospecting.">
      <div className="fjb-card" style={{ padding: 22, marginBottom: 30 }}>
        <div style={{ display: "flex", justifyContent: "space-between", marginBottom: 14 }}>
          <div className="can-serif" style={{ fontWeight: 700, fontSize: 16 }}>Complete Financial Picture</div>
          <span className="can-label" style={{ fontSize: 10, color: GOLD }}>{managedCount}/{ASSET_CATEGORIES.length} currently managed here</span>
        </div>
        {ASSET_CATEGORIES.map((c) => (
          <div key={c} style={{ display: "flex", justifyContent: "space-between", alignItems: "center", padding: "10px 0", borderTop: `1px solid ${LINE}` }}>
            <span style={{ fontSize: 13 }}>{c}</span>
            <div style={{ display: "flex", gap: 6 }}>
              {["managed", "held elsewhere", "unknown"].map((opt) => (
                <button key={opt} onClick={() => setAssets((a) => ({ ...a, [c]: opt }))} className="can-label"
                  style={{ fontSize: 9, padding: "5px 10px", borderRadius: 12, border: `1px solid ${assets[c] === opt ? GOLD : LINE}`, background: assets[c] === opt ? GOLD : "transparent", color: assets[c] === opt ? WHITE : SLATE, cursor: "pointer" }}>
                  {opt}
                </button>
              ))}
            </div>
          </div>
        ))}
        <div style={{ marginTop: 14, fontSize: 11.5, color: SLATE, fontStyle: "italic" }}>Family consent required before any "held elsewhere" asset is discussed further.</div>
      </div>

      <div className="fjb-card" style={{ padding: 22 }}>
        <div style={{ display: "flex", justifyContent: "space-between", marginBottom: 14 }}>
          <div className="can-serif" style={{ fontWeight: 700, fontSize: 16 }}>Business Exit Readiness</div>
          <span className="can-label" style={{ fontSize: 10, color: GOLD }}>{exitLevel}</span>
        </div>
        {Object.entries(exitScores).map(([k, v]) => (
          <div key={k} style={{ marginBottom: 12 }}>
            <div style={{ display: "flex", justifyContent: "space-between", fontSize: 12.5, marginBottom: 3 }}>
              <span>{k}</span><span style={{ fontWeight: 700, color: GOLD }}>{v}/10</span>
            </div>
            <input type="range" min="1" max="10" value={v} onChange={(e) => setExitScores((s) => ({ ...s, [k]: Number(e.target.value) }))} style={{ width: "100%" }} />
          </div>
        ))}
      </div>
    </ModuleShell>
  );
}

const FLOURISHING_17 = ["Joy","Health","Purpose","Character","Relationships","Faith","Family","Work","Business","Marketplace","Finances","Leadership","Community","Resilience","Growth","Generosity","Legacy"];
const STEWARD_STAGES = [
  ["Identity & Purpose", "Life Message Builder + Family Values Builder — who am I becoming as a steward, not a skills checklist."],
  ["Priority", "A protected, recurring block of time for succession work, defended against whatever feels urgent."],
  ["Small, Sustained Habits", "Two-minute starting habits, stacked onto existing family rituals, tracked with a readiness scorecard."],
  ["Collaboration", "Family council practice built on understanding-first listening and win-win framing."],
];
function FjbStewardJourney() {
  const [stage, setStage] = useState(0);
  const [focusDims, setFocusDims] = useState([]);

  const toggleDim = (d) => setFocusDims((f) => f.includes(d) ? f.filter((x) => x !== d) : f.length < 4 ? [...f, d] : f);

  return (
    <ModuleShell eyebrow="Family Journey Builder — Successor & Steward Journey" title="Sequenced Covey's way. Built to stick with habit science." subtitle="Identity → Priority → Habits → Collaboration — and a development plan drawn from the 17 Flourishing dimensions.">
      <div style={{ display: "flex", gap: 8, marginBottom: 24, flexWrap: "wrap" }}>
        {STEWARD_STAGES.map((s, i) => (
          <button key={s[0]} onClick={() => setStage(i)} className="fjb-tab"
            style={{ padding: "10px 16px", borderRadius: 20, border: `1.5px solid ${stage === i ? NAVY : LINE}`, background: stage === i ? NAVY : WHITE, color: stage === i ? WHITE : INK, fontSize: 11, cursor: "pointer" }}>
            {i + 1}. {s[0]}
          </button>
        ))}
      </div>
      <div className="fjb-card can-fade-in" key={stage} style={{ padding: 24, marginBottom: 30 }}>
        <div className="can-serif" style={{ fontWeight: 700, fontSize: 18, color: NAVY, marginBottom: 10 }}>{STEWARD_STAGES[stage][0]}</div>
        <div style={{ fontSize: 13.5, color: INK, lineHeight: 1.6 }}>{STEWARD_STAGES[stage][1]}</div>
      </div>

      <div className="fjb-card" style={{ padding: 22 }}>
        <div className="can-serif" style={{ fontWeight: 700, fontSize: 16, marginBottom: 6 }}>Build the Development Plan</div>
        <div style={{ fontSize: 12.5, color: SLATE, marginBottom: 14 }}>Choose up to four Flourishing dimensions to focus this successor's development plan on.</div>
        <div style={{ display: "flex", flexWrap: "wrap", gap: 8, marginBottom: 16 }}>
          {FLOURISHING_17.map((d) => (
            <button key={d} onClick={() => toggleDim(d)} className="can-label"
              style={{ fontSize: 10, padding: "7px 12px", borderRadius: 14, border: `1px solid ${focusDims.includes(d) ? GOLD : LINE}`, background: focusDims.includes(d) ? GOLD : "transparent", color: focusDims.includes(d) ? WHITE : INK, cursor: "pointer" }}>
              {d}
            </button>
          ))}
        </div>
        {focusDims.length > 0 && (
          <div className="can-fade-in" style={{ background: CREAM, borderLeft: `3px solid ${GOLD}`, padding: "12px 16px", fontSize: 12.5 }}>
            This successor's plan will draw from: <b>{focusDims.join(", ")}</b> — reusing existing Flourishing LifeTogether content, no new curriculum required.
          </div>
        )}
      </div>
    </ModuleShell>
  );
}

const GOVERNANCE_ITEMS = ["Written family employment policy", "Board of advisors or directors", "Family communication protocol", "Documented succession plan", "Regular family business meetings", "Conflict resolution process"];
const ROLES = ["CEO / Leadership", "Finance", "Operations", "Board Seat", "Advisory Only"];
function FjbFamilyBusiness() {
  const [governance, setGovernance] = useState(Object.fromEntries(GOVERNANCE_ITEMS.map((g) => [g, false])));
  const [members, setMembers] = useState([{ name: "Eldest child", role: "CEO / Leadership", readiness: 5 }]);
  const [form, setForm] = useState({ name: "", role: ROLES[0] });

  const govCount = Object.values(governance).filter(Boolean).length;
  const addMember = () => {
    if (!form.name) return;
    setMembers((m) => [...m, { name: form.name, role: form.role, readiness: 5 }]);
    setForm({ name: "", role: ROLES[0] });
  };
  const setReadiness = (i, v) => setMembers((m) => m.map((mem, idx) => idx === i ? { ...mem, readiness: v } : mem));

  return (
    <ModuleShell eyebrow="Family Journey Builder — Family Business" title="Governance, roles, and readiness." subtitle="A shared picture of how the family business is actually structured — and who's ready for what.">
      <div className="fjb-card" style={{ padding: 22, marginBottom: 30 }}>
        <div style={{ display: "flex", justifyContent: "space-between", marginBottom: 14 }}>
          <div className="can-serif" style={{ fontWeight: 700, fontSize: 16 }}>Governance Checklist</div>
          <span className="can-label" style={{ fontSize: 10, color: GOLD }}>{govCount}/{GOVERNANCE_ITEMS.length}</span>
        </div>
        {GOVERNANCE_ITEMS.map((g) => (
          <div key={g} onClick={() => setGovernance((s) => ({ ...s, [g]: !s[g] }))} style={{ display: "flex", gap: 12, alignItems: "center", padding: "9px 0", borderTop: `1px solid ${LINE}`, cursor: "pointer" }}>
            <div style={{ width: 18, height: 18, borderRadius: 4, border: `1.5px solid ${governance[g] ? GREEN : LINE}`, background: governance[g] ? GREEN : "transparent", display: "flex", alignItems: "center", justifyContent: "center", color: WHITE, fontSize: 10, flexShrink: 0 }}>
              {governance[g] ? "\u2713" : ""}
            </div>
            <span style={{ fontSize: 13 }}>{g}</span>
          </div>
        ))}
      </div>

      <div className="fjb-card" style={{ padding: 22 }}>
        <div className="can-serif" style={{ fontWeight: 700, fontSize: 16, marginBottom: 14 }}>Role Readiness</div>
        <div style={{ display: "flex", gap: 10, flexWrap: "wrap", marginBottom: 16 }}>
          <input className="fjb-input" placeholder="Family member name" value={form.name} onChange={(e) => setForm((f) => ({ ...f, name: e.target.value }))} style={{ flex: "1 1 200px" }} />
          <select className="fjb-input" value={form.role} onChange={(e) => setForm((f) => ({ ...f, role: e.target.value }))} style={{ flex: "1 1 160px" }}>
            {ROLES.map((r) => <option key={r}>{r}</option>)}
          </select>
          <button onClick={addMember} className="can-btn-gold can-label" style={{ background: NAVY, color: WHITE, border: "none", borderRadius: 6, padding: "9px 18px", fontSize: 11, fontWeight: 700, cursor: "pointer" }}>Add</button>
        </div>
        {members.map((m, i) => (
          <div key={i} style={{ padding: "12px 0", borderTop: `1px solid ${LINE}` }}>
            <div style={{ display: "flex", justifyContent: "space-between", marginBottom: 4 }}>
              <span style={{ fontWeight: 600, fontSize: 13 }}>{m.name} <span style={{ color: SLATE, fontWeight: 400 }}>&middot; {m.role}</span></span>
              <span style={{ fontWeight: 700, color: GOLD, fontSize: 12 }}>{m.readiness}/10</span>
            </div>
            <input type="range" min="1" max="10" value={m.readiness} onChange={(e) => setReadiness(i, Number(e.target.value))} style={{ width: "100%" }} />
          </div>
        ))}
      </div>
    </ModuleShell>
  );
}

const STORY_PROMPTS = [
  "Tell about a time your family showed generosity even when it was hard.",
  "What's a decision an earlier generation made that still shapes the family today?",
  "Describe a moment you saw a family value actually lived out, not just talked about.",
  "What's a family story about failure that taught something important?",
  "What's something your grandparents believed that you want your grandchildren to know?",
];
const VALUE_TAGS = ["Faith", "Generosity", "Perseverance", "Integrity", "Family", "Work Ethic"];
function FjbStories() {
  const [prompt, setPrompt] = useState(STORY_PROMPTS[0]);
  const [text, setText] = useState("");
  const [tag, setTag] = useState(VALUE_TAGS[0]);
  const [teller, setTeller] = useState("");
  const [stories, setStories] = useState([
    { teller: "Grandma Ruth", tag: "Perseverance", prompt: STORY_PROMPTS[3], text: "During the '82 recession, she kept the shop open by working the counter herself for two years rather than laying anyone off." },
  ]);

  const saveStory = () => {
    if (!text.trim() || !teller.trim()) return;
    setStories((s) => [{ teller, tag, prompt, text }, ...s]);
    setText(""); setTeller("");
  };

  return (
    <ModuleShell eyebrow="Family Journey Builder — Stories" title="Legacy, history, and value-based stories." subtitle="Helping the next generation build on and understand the family's why — captured once, available to everyone after.">
      <div className="fjb-card" style={{ padding: 22, marginBottom: 30 }}>
        <Field label="Prompt">
          <select className="fjb-input" value={prompt} onChange={(e) => setPrompt(e.target.value)} style={{ width: "100%" }}>
            {STORY_PROMPTS.map((p) => <option key={p}>{p}</option>)}
          </select>
        </Field>
        <div style={{ display: "flex", gap: 10, marginBottom: 14 }}>
          <div style={{ flex: 1 }}>
            <Field label="Who's telling it"><input className="fjb-input" style={{ width: "100%" }} value={teller} onChange={(e) => setTeller(e.target.value)} placeholder="e.g. Grandma Ruth" /></Field>
          </div>
          <div style={{ flex: 1 }}>
            <Field label="Value it reflects">
              <select className="fjb-input" style={{ width: "100%" }} value={tag} onChange={(e) => setTag(e.target.value)}>
                {VALUE_TAGS.map((v) => <option key={v}>{v}</option>)}
              </select>
            </Field>
          </div>
        </div>
        <Field label="The story">
          <textarea className="fjb-input" style={{ width: "100%", minHeight: 90, fontFamily: "Inter" }} value={text} onChange={(e) => setText(e.target.value)} placeholder="Write it the way you'd tell it out loud..." />
        </Field>
        <button onClick={saveStory} className="can-btn-gold can-label" style={{ background: GOLD, color: WHITE, border: "none", borderRadius: 22, padding: "11px 24px", fontSize: 11, fontWeight: 700, cursor: "pointer" }}>Save to the Family Library</button>
      </div>

      <div className="can-label" style={{ fontSize: 10, color: GOLD, marginBottom: 12 }}>{stories.length} {stories.length === 1 ? "story" : "stories"} in the library</div>
      {stories.map((s, i) => (
        <div key={i} className="fjb-card" style={{ padding: 18, marginBottom: 12 }}>
          <div style={{ display: "flex", justifyContent: "space-between", marginBottom: 8 }}>
            <span className="can-serif" style={{ fontWeight: 700, fontSize: 14 }}>{s.teller}</span>
            <span className="can-label" style={{ fontSize: 9, color: GOLD, background: CREAM, padding: "3px 9px", borderRadius: 10 }}>{s.tag}</span>
          </div>
          <div style={{ fontSize: 11, color: SLATE, fontStyle: "italic", marginBottom: 8 }}>{s.prompt}</div>
          <div style={{ fontSize: 13, color: INK, lineHeight: 1.55 }}>{s.text}</div>
        </div>
      ))}
    </ModuleShell>
  );
}

/* ---------------- SHARED SHELL + JOIN BAND ---------------- */
function PageShell({ eyebrow, title, children }) {
  return (
    <div className="can-fade-in" style={{ maxWidth: 1240, margin: "0 auto", padding: "80px 28px 100px" }}>
      <Eyebrow>{eyebrow}</Eyebrow>
      <h1 className="can-serif" style={{ fontSize: "clamp(24px, 3.4vw, 34px)", fontWeight: 700, color: NAVY, maxWidth: 720, margin: "20px 0 30px", lineHeight: 1.25 }}>{title}</h1>
      {children}
    </div>
  );
}
function JoinBand({ setPage }) {
  return (
    <div style={{ background: `linear-gradient(200deg, ${NAVY2} 0%, #0E1930 100%)`, textAlign: "center" }}>
      <div style={{ maxWidth: 640, margin: "0 auto", padding: "90px 28px" }}>
        <Eyebrow dark>Join the Network</Eyebrow>
        <h2 className="can-serif" style={{ fontSize: "clamp(24px, 4vw, 34px)", fontWeight: 700, color: WHITE, margin: "20px 0 0", lineHeight: 1.2 }}>Grow your faith. Grow your practice. Grow your impact.</h2>
        <button onClick={() => setPage("membership")} className="can-btn-gold can-label" style={{ marginTop: 30, background: GOLD, color: NAVY, border: "none", borderRadius: 28, padding: "16px 36px", fontSize: 12.5, fontWeight: 700, cursor: "pointer" }}>Apply for Membership</button>
      </div>
    </div>
  );
}

/* ---------------- APP ---------------- */
export default function ChristianAdvisorNetworkSite() {
  const [page, setPage] = useState("home");
  const [menuOpen, setMenuOpen] = useState(false);
  const [scrolled, setScrolled] = useState(false);

  useEffect(() => {
    const onScroll = () => setScrolled(window.scrollY > 24);
    window.addEventListener("scroll", onScroll);
    return () => window.removeEventListener("scroll", onScroll);
  }, []);

  useEffect(() => { window.scrollTo(0, 0); }, [page]);

  return (
    <div className="can-root">
      <style>{FONTS}</style>
      <HeaderNav page={page} setPage={setPage} menuOpen={menuOpen} setMenuOpen={setMenuOpen} scrolled={scrolled} />

      {page === "home" && <HomePage setPage={setPage} />}
      {page === "resources" && <ResourcesPage />}
      {page === "rack" && <RackPage setPage={setPage} />}
      {page === "assessments" && <AssessmentsPage setPage={setPage} />}
      {page === "growth-series" && <GrowthSeriesPage setPage={setPage} />}
      {page === "business-leaders" && <BusinessLeadersPage setPage={setPage} />}
      {page === "purpose-built-business" && <PurposeBuiltBusinessHook setPage={setPage} />}
      {page === "offerings-families" && <OfferingsFamiliesPage />}
      {page === "partnership" && <PartnershipPage />}
      {page === "membership" && <MembershipPage setPage={setPage} />}
      {page === "find-advisor" && <FindAdvisorPage setPage={setPage} />}
      {page === "case-studies" && <CaseStudiesPage />}
      {page === "faq" && <FaqPage />}
      {page === "about" && <AboutPage />}
      {page === "fjb-overview" && <FjbOverview setPage={setPage} />}
      {page === "fjb-map" && <FjbFamilyMap />}
      {page === "fjb-retention" && <FjbRetention />}
      {page === "fjb-relational" && <FjbRelationalBonds />}
      {page === "fjb-aum" && <FjbAumGrowth />}
      {page === "fjb-steward" && <FjbStewardJourney />}
      {page === "fjb-business" && <FjbFamilyBusiness />}
      {page === "fjb-stories" && <FjbStories />}
      {page === "fjb-sources" && <FjbSources />}
      {page === "fjb-finder" && <FjbFinder />}
      {page === "fjb-coaching" && <FjbCoaching />}
      {page === "fjb-scripts" && <FjbScripts />}
      {page === "fjb-builders" && <FjbBuilders />}
      {page === "fjb-habits" && <FjbHabits />}
      {page === "fjb-toolbox" && <FjbToolbox />}
      {page === "fjb-library-builder" && <FjbLibraryBuilder />}
      {page === "fjb-calendar" && <FjbCalendar />}
      {page === "fjb-cohort" && <FjbCohort />}
      {page === "fjb-library" && <FjbLibrary />}
      {page === "fjb-publish" && <FjbPublish />}

      <FooterNav page={page} setPage={setPage} />
    </div>
  );
}
