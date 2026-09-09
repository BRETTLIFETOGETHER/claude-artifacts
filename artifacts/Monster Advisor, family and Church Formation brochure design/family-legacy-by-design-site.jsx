import React, { useState, useEffect } from "react";

const GREEN = "#1C3A2D";
const GREEN2 = "#26493A";
const GOLD = "#B4872C";
const GOLD_BRIGHT = "#D4AC5C";
const CREAM = "#F4EFE3";
const WHITE = "#FBF9F4";
const INK = "#20261F";
const SLATE = "#6E7568";
const LINE = "#DCD4BE";
const AMBER = "#C4791F";

const FONTS = `
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,600;0,700;0,900;1,500;1,600&family=Archivo:wght@500;600;700&family=Inter:wght@400;500;600;700&display=swap');
* { box-sizing: border-box; }
body { margin: 0; }
.fl-root { font-family: 'Inter', sans-serif; color: ${INK}; background: ${WHITE}; }
.fl-serif { font-family: 'Playfair Display', serif; }
.fl-label { font-family: 'Archivo', sans-serif; letter-spacing: 0.14em; text-transform: uppercase; }
.fl-eyebrow { display:flex; align-items:center; gap:10px; font-family:'Archivo',sans-serif; font-weight:600; font-size:12px; letter-spacing:0.18em; text-transform:uppercase; color:${GOLD}; }
.fl-eyebrow::before { content:''; width:26px; height:2px; background:${GOLD}; display:inline-block; }
.fl-eyebrow.on-dark { color:${GOLD_BRIGHT}; }
.fl-eyebrow.on-dark::before { background:${GOLD_BRIGHT}; }
.fl-nav-link { position:relative; background:none; border:none; cursor:pointer; font-family:'Archivo'; }
.fl-nav-link::after { content:''; position:absolute; left:0; right:0; bottom:-6px; height:1.5px; background:${GOLD_BRIGHT}; transform:scaleX(0); transition:transform .25s ease; }
.fl-nav-link:hover::after { transform:scaleX(1); }
.fl-nav-link.active::after { transform:scaleX(1); background:${GOLD}; }
.fl-card { transition: transform .35s cubic-bezier(.2,.7,.3,1), border-color .3s ease; }
.fl-card:hover { transform: translateY(-3px); }
.fl-btn-gold { transition: background .2s ease, color .2s ease, transform .2s ease; }
.fl-btn-gold:hover { transform: translateY(-1px); }
.fl-fade-in { animation: flFadeIn .5s ease both; }
@keyframes flFadeIn { from { opacity:0; transform:translateY(8px);} to {opacity:1; transform:translateY(0);} }
.fl-footer-link { background:none; border:none; cursor:pointer; text-align:left; padding:0; }
.fl-desktop-only { display: none; }
@media (min-width: 900px) { .fl-desktop-only { display: flex !important; } }
.fl-mobile-only { display: inline-block; }
@media (min-width: 900px) { .fl-mobile-only { display: none !important; } }
.fl-input { font-family:'Inter'; font-size:13px; padding:9px 12px; border:1px solid ${LINE}; border-radius:6px; outline:none; background:${WHITE}; }
.fl-input:focus { border-color:${GOLD}; }
.fl-tab { background:none; border:none; cursor:pointer; font-family:'Archivo'; font-weight:600; }
::selection { background: ${GOLD}; color: ${WHITE}; }
`;

const PAGES = [
  { id: "home", label: "Home" },
  { id: "titles", label: "Family Legacy Journeys" },
  { id: "library", label: "The Full Library" },
  { id: "domains", label: "Intelligence Categories" },
  { id: "core-flow", label: "The Core Flow" },
  { id: "journey-builder", label: "Journey Builder" },
  { id: "framework", label: "The Framework" },
  { id: "churches", label: "For Churches" },
  { id: "advisors", label: "For Advisors" },
  { id: "advisor-access", label: "Before You Say Yes" },
  { id: "assessments", label: "Assessments" },
  { id: "customization", label: "Customize & Deliver" },
  { id: "pricing", label: "Pricing" },
  { id: "portal", label: "Portal" },
  { id: "about", label: "About" },
];
function pageLabel(id) { const p = PAGES.find((p) => p.id === id); return p ? p.label : id; }

const NAV_GROUPS = [
  { label: "The System", items: ["titles", "library", "domains", "core-flow", "journey-builder", "framework"] },
  { label: "Get Started", items: ["churches", "advisors", "advisor-access", "assessments"] },
  { id: "customization" },
  { id: "pricing" },
  { id: "portal" },
  { id: "about" },
];

const TITLES = [
  { n: "1", title: "40 Days of Family Legacy", tag: "FLAGSHIP · THE FOUNDATIONAL TITLE", desc: "Clear, aspirational, and serious enough to command the attention of a high-capacity family already thinking about what they will leave behind. The flagship campaign built on the Family Legacy By Design curriculum." },
  { n: "2", title: "40 Days of What Matters Most", tag: "MIDLIFE INFLECTION · LEGACY AWAKENING", desc: "Cuts through every accomplishment a successful family has accumulated and asks the one question they've been postponing. The felt-need opener for families not yet using the legacy language." },
  { n: "3", title: "40 Days of Lasting Wealth", tag: "HIGH NET WORTH · VALUES TRANSFER", desc: "Reframes wealth as something that includes — but extends far beyond — financial assets. Values. Faith. Character. Every wealth manager talks about financial legacy. No wealth manager talks about this kind." },
  { n: "4", title: "40 Days of the Second Half", tag: "BOB BUFORD · HALFTIME FRAMEWORK", desc: "Speaks to the person who has won the first half of life by every external measure and is now asking what the second half is actually for." },
  { n: "5", title: "40 Days of Generational Faithfulness", tag: "PSALM 78 · DEUTERONOMY 6", desc: "The most theologically grounded title — rooted in the biblical theology of passing faith from one generation to the next. For families who want to transfer conviction, not just wealth." },
  { n: "6", title: "40 Days of the Wealthy Soul", tag: "NET WORTH VS. SOUL WORTH", desc: "The most provocative title — built on the tension between net worth and soul worth. For the family that has everything and privately wonders why it doesn't feel like enough." },
  { n: "7", title: "40 Days of What We Leave Behind", tag: "PARENTS · GRANDPARENTS · FOUNDERS", desc: "Emotionally resonant for every parent of adult children and every grandparent of young grandchildren. Honest, universal, impossible to ignore." },
  { n: "8", title: "40 Days of Family on Purpose", tag: "INTENTIONAL · STRATEGIC · FOUNDERS", desc: "Built on the language of intentionality. Appeals to business owners and founders who apply strategic thinking to every domain of their professional life — and want to apply it to their family for the first time." },
  { n: "9", title: "40 Days of the Blessed Life", tag: "DUAL MEANING · SPIRITUALLY CONVICTING", desc: "Draws on the dual meaning of blessed — financially prosperous and spiritually grounded — and invites families to examine which version of the blessed life they're actually building." },
  { n: "10", title: "40 Days of Enough", tag: "MOST COUNTERCULTURAL · DEEPEST WORK", desc: "The family willing to ask \u201cwhat is enough, and what comes after enough\u201d is ready for the deepest legacy work. Changes the conversation from accumulation to distribution, from achievement to faithfulness." },
  { n: "11", title: "21 Days to Remember", tag: "SHORT · A FIRST TASTE", desc: "A three-week entry point for a family not ready for the full forty days — remembering the story before doing anything else." },
  { n: "12", title: "30 Days of Family Governance", tag: "GOVERNANCE · SUCCESSION · DECISION-MAKING", desc: "For families ready to build the structures — a family council, a decision framework, a communication protocol — not just have the conversation once." },
];

const ADVISOR_JOURNEYS = [
  { title: "The First Conversation Journey", length: "7 Days", desc: "For an advisor about to raise legacy work with a family for the first time — how to open it without it feeling like a pitch." },
  { title: "The Multi-Generational Meeting Journey", length: "21 Days", desc: "Preparing to facilitate a real family meeting across generations — agenda design, seating the conversation, handling conflict in the room." },
  { title: "The Legacy Letter Facilitation Journey", length: "14 Days", desc: "Walking a client through writing their own legacy letter — the questions that unlock real writing, not a form letter." },
  { title: "The Advisor Certification Journey", length: "40 Days", desc: "The complete path to becoming a certified Family Legacy By Design facilitator — every domain, every tool, every diagnostic signal." },
];

const DOMAINS = [
  { name: "Identity & Story", desc: "Helps a family understand and articulate its own narrative — the foundation every other domain builds on." },
  { name: "Faith & Spiritual Heritage", desc: "Passes conviction, not just information, from one generation to the next." },
  { name: "Values & Vision", desc: "Turns unspoken assumptions into a shared, nameable family standard." },
  { name: "Relationships & Reconciliation", desc: "Repairs and strengthens the bonds that make every other domain sustainable." },
  { name: "Wealth & Stewardship", desc: "Reframes money as a tool for the family's purpose, not the purpose itself." },
  { name: "Parenting & Next Generation", desc: "Prepares heirs for responsibility before they receive it." },
  { name: "Governance & Succession", desc: "Gives the family a fair, durable way to make decisions together." },
  { name: "Generosity & Impact", desc: "Turns private resources into a shared family mission beyond itself." },
  { name: "Communication, Health & Emotional Systems", desc: "Builds the capacity to have hard conversations without breaking relationship." },
  { name: "Business, Property & Enterprise Legacy", desc: "Protects what the family built from becoming a source of division." },
  { name: "Global, Cultural & Digital Legacy", desc: "Carries family identity across geography, technology, and time." },
];

const CORE_FLOW = [
  ["DISCOVER", "What is happening in this family right now?"],
  ["DISCERN", "What matters most in this season?"],
  ["JOURNEY", "What experience will help the family grow?"],
  ["EQUIP", "What tools will help them act wisely?"],
  ["CREATE", "What tangible legacy artifact should be produced?"],
  ["ACTIVATE", "What will the family do in the next 90 days?"],
  ["REVIEW", "What changed as a result?"],
  ["CONTINUE", "What is the next best conversation or journey?"],
];

const STAGES = [
  { name: "Remember", desc: "Revisiting the family's story and where it came from.", days: ["Where We Began", "The Story Before Us", "Faces We Don't Want Forgotten", "What They Sacrificed", "A Memory Worth Keeping"] },
  { name: "Clarify", desc: "Naming what the family actually believes and values.", days: ["What We Actually Believe", "The Value We Never Named", "Where We've Drifted", "What We Want to Be Known For", "Saying It Out Loud"] },
  { name: "Prepare", desc: "Getting practical documents and structures in order.", days: ["What's Actually Written Down", "The Conversation We've Postponed", "Who Knows What We Know", "Closing the Gaps", "Ready, Not Rushed"] },
  { name: "Communicate", desc: "Having the conversations that matter most.", days: ["Starting the Hard Conversation", "Listening Before Explaining", "What the Next Generation Needs to Hear", "Making Space for Disagreement", "Ending Well"] },
  { name: "Give", desc: "Exploring generosity and impact together.", days: ["What We Could Give", "Giving as a Family, Not Just a Person", "The Cause That Matters Most", "Generosity as Identity", "A Plan Worth Keeping"] },
  { name: "Commit", desc: "Turning insight into an actual family commitment.", days: ["What Changes Starting Now", "Who Holds Us Accountable", "The First Ninety Days", "Reviewing What We Said", "A Commitment We'll Keep"] },
];

const LENGTH_CONFIG = {
  21: { weeks: 3, stageIdx: [0, 1, 3] },
  30: { weeks: 4, stageIdx: [0, 1, 3, 5] },
  40: { weeks: 6, stageIdx: [0, 1, 2, 3, 4, 5] },
};

const ASSESSMENTS = [
  { name: "Family Legacy Readiness Assessment™", desc: "Measures how prepared a family is to transfer wisdom, values, and wealth together.", dims: ["Story clarity", "Values alignment", "Communication health", "Governance structure", "Generosity practice"] },
  { name: "Next-Generation Readiness Assessment™", desc: "Evaluates whether heirs are prepared for the responsibility they're about to receive.", dims: ["Financial literacy", "Values internalization", "Decision-making experience", "Communication comfort", "Sense of calling"] },
  { name: "Family Communication Health Assessment™", desc: "Diagnoses how well a family actually talks about money, values, and the future.", dims: ["Conflict comfort", "Transparency", "Listening quality", "Meeting rhythm", "Follow-through"] },
  { name: "Generosity Capacity Assessment™", desc: "Helps a family understand what they could give, and what's holding them back.", dims: ["Giving clarity", "Shared decision-making", "Structural readiness", "Next-gen involvement", "Emotional freedom to give"] },
];

function Eyebrow({ children, dark }) { return <div className={`fl-eyebrow${dark ? " on-dark" : ""}`}>{children}</div>; }
function Field({ label, children }) { return <div style={{ marginBottom: 14 }}><div className="fl-label" style={{ fontSize: 9.5, color: SLATE, marginBottom: 5 }}>{label}</div>{children}</div>; }

/* ---------------- NAV ---------------- */
function HeaderNav({ page, setPage, menuOpen, setMenuOpen, scrolled }) {
  const [openGroup, setOpenGroup] = useState(null);
  return (
    <div onMouseLeave={() => setOpenGroup(null)} style={{ position: "sticky", top: 0, zIndex: 50, background: scrolled || page !== "home" ? "rgba(28,58,45,0.97)" : "transparent", borderBottom: `1px solid rgba(180,135,44,0.25)`, backdropFilter: "blur(6px)", transition: "background .3s ease" }}>
      <div style={{ maxWidth: 1200, margin: "0 auto", padding: "18px 28px", display: "flex", alignItems: "center", justifyContent: "space-between" }}>
        <button onClick={() => setPage("home")} className="fl-serif" style={{ background: "none", border: "none", cursor: "pointer", fontWeight: 700, fontSize: 15.5, color: WHITE }}>Family Legacy By Design<span style={{ fontSize: 9, verticalAlign: "super" }}>™</span></button>
        <div className="fl-desktop-only" style={{ gap: 4, alignItems: "center" }}>
          {NAV_GROUPS.map((g, gi) => {
            if (g.id) {
              return <button key={g.id} onClick={() => setPage(g.id)} className={`fl-nav-link fl-label${page === g.id ? " active" : ""}`} style={{ fontSize: 10.3, fontWeight: 600, color: page === g.id ? GOLD_BRIGHT : "rgba(251,249,244,0.85)", padding: "8px 10px" }}>{pageLabel(g.id)}</button>;
            }
            const isOpen = openGroup === gi;
            const containsActive = g.items.includes(page);
            return (
              <div key={g.label} style={{ position: "relative" }} onMouseEnter={() => setOpenGroup(gi)}>
                <button onClick={() => setOpenGroup(isOpen ? null : gi)} className={`fl-nav-link fl-label${containsActive ? " active" : ""}`} style={{ fontSize: 10.3, fontWeight: 600, color: containsActive ? GOLD_BRIGHT : "rgba(251,249,244,0.85)", padding: "8px 10px" }}>{g.label} {isOpen ? "\u2303" : "\u2304"}</button>
                {isOpen && (
                  <div style={{ position: "absolute", top: "100%", left: 0, background: GREEN, border: "1px solid rgba(180,135,44,0.3)", borderRadius: 6, minWidth: 210, padding: 8, boxShadow: "0 12px 28px rgba(0,0,0,0.35)" }}>
                    {g.items.map((id) => (
                      <button key={id} onClick={() => { setPage(id); setOpenGroup(null); }} className="fl-footer-link fl-label" style={{ display: "block", width: "100%", fontSize: 10.5, fontWeight: 600, color: page === id ? GOLD_BRIGHT : "rgba(251,249,244,0.85)", padding: "9px 12px", borderRadius: 4 }}>{pageLabel(id)}</button>
                    ))}
                  </div>
                )}
              </div>
            );
          })}
        </div>
        <button onClick={() => setPage("pricing")} className="fl-btn-gold fl-label fl-desktop-only" style={{ background: GOLD, color: WHITE, border: "none", borderRadius: 22, padding: "9px 18px", fontSize: 10.5, fontWeight: 700, cursor: "pointer" }}>See Pricing</button>
        <button onClick={() => setMenuOpen((v) => !v)} className="fl-mobile-only" style={{ background: "none", border: `1px solid rgba(180,135,44,0.5)`, borderRadius: 8, padding: "8px 12px", color: GOLD_BRIGHT, cursor: "pointer", fontSize: 13 }}>{menuOpen ? "Close" : "Menu"}</button>
      </div>
      {menuOpen && (
        <div style={{ background: GREEN, borderTop: `1px solid rgba(180,135,44,0.25)`, padding: "8px 28px 24px", maxHeight: "70vh", overflowY: "auto" }}>
          {PAGES.map((p) => (
            <div key={p.id} onClick={() => { setPage(p.id); setMenuOpen(false); }} className="fl-label" style={{ padding: "12px 0", borderBottom: "1px solid rgba(180,135,44,0.2)", color: page === p.id ? GOLD_BRIGHT : "rgba(251,249,244,0.9)", fontSize: 12, cursor: "pointer" }}>{p.label}</div>
          ))}
          <div onClick={() => { setPage("pricing"); setMenuOpen(false); }} className="fl-label" style={{ marginTop: 16, background: GOLD, color: WHITE, textAlign: "center", padding: "12px 0", borderRadius: 24, fontSize: 12, fontWeight: 700, cursor: "pointer" }}>See Pricing</div>
        </div>
      )}
    </div>
  );
}

function FooterNav({ page, setPage }) {
  return (
    <div style={{ background: GREEN, borderTop: "1px solid rgba(180,135,44,0.2)" }}>
      <div style={{ maxWidth: 1200, margin: "0 auto", padding: "50px 24px 30px", display: "grid", gridTemplateColumns: "repeat(auto-fit, minmax(160px, 1fr))", gap: 28 }}>
        <div style={{ gridColumn: "1 / -1", maxWidth: 340, marginBottom: 8 }}>
          <div className="fl-serif" style={{ fontWeight: 700, fontSize: 16, color: WHITE, marginBottom: 10 }}>Family Legacy By Design<span style={{ fontSize: 9, verticalAlign: "super" }}>™</span></div>
          <p style={{ fontSize: 12.5, color: "rgba(251,249,244,0.65)", lineHeight: 1.6 }}>Built on Tom Conway's Family Legacy By Design framework, delivered through the Lifetogether campaign platform.</p>
        </div>
        {NAV_GROUPS.map((g) => {
          const items = g.id ? [g.id] : g.items;
          const heading = g.id ? pageLabel(g.id) : g.label;
          return (
            <div key={heading}>
              <div className="fl-label" style={{ fontSize: 9.5, color: GOLD_BRIGHT, marginBottom: 12 }}>{heading}</div>
              {items.map((id) => (
                <button key={id} onClick={() => setPage(id)} className="fl-footer-link" style={{ display: "block", fontSize: 12, color: page === id ? GOLD_BRIGHT : "rgba(251,249,244,0.72)", padding: "5px 0", cursor: "pointer" }}>{pageLabel(id)}</button>
              ))}
            </div>
          );
        })}
      </div>
      <div style={{ maxWidth: 1200, margin: "0 auto", padding: "18px 24px", borderTop: "1px solid rgba(180,135,44,0.15)", display: "flex", justifyContent: "space-between", flexWrap: "wrap", gap: 12 }}>
        <div className="fl-label" style={{ fontSize: 9, color: "rgba(251,249,244,0.45)" }}>FAMILY LEGACY BY DESIGN™ · A LIFETOGETHER PLATFORM</div>
        <div className="fl-label" style={{ fontSize: 9, color: "rgba(251,249,244,0.45)" }}>DRAFT PREVIEW · NOT YET LIVE</div>
      </div>
    </div>
  );
}

/* ---------------- HOME ---------------- */
function HomePage({ setPage }) {
  const explore = [
    { id: "titles", label: "Family Legacy Journeys", desc: "Twelve campaigns, ready to launch a legacy ministry." },
    { id: "domains", label: "Intelligence Categories", desc: "Eleven domains covering the whole of family formation." },
    { id: "journey-builder", label: "Journey Builder", desc: "Build a 21, 30, or 40-day journey with real session titles." },
    { id: "churches", label: "For Churches", desc: "Launch a family legacy cohort in your congregation." },
    { id: "advisors", label: "For Advisors", desc: "Bring this into your highest-capacity client relationships." },
    { id: "assessments", label: "Assessments", desc: "Take any of four assessments right now, no email required." },
    { id: "customization", label: "Customize & Deliver", desc: "Digital delivery or print-on-demand, tailored to your family." },
    { id: "pricing", label: "Pricing", desc: "What it costs to bring this to your church or practice." },
  ];
  return (
    <div className="fl-fade-in">
      <div style={{ position: "relative", background: `linear-gradient(165deg, ${GREEN} 0%, #12261D 100%)`, overflow: "hidden" }}>
        <div style={{ position: "absolute", inset: 0, opacity: 0.5, backgroundImage: `radial-gradient(circle at 78% 18%, rgba(180,135,44,0.16), transparent 45%)` }} />
        <div style={{ maxWidth: 1200, margin: "0 auto", padding: "80px 24px 80px", position: "relative" }}>
          <div style={{ maxWidth: 700 }}>
            <Eyebrow dark>For High-Capacity Families &amp; the Churches That Serve Them</Eyebrow>
            <h1 className="fl-serif" style={{ fontSize: "clamp(28px, 5vw, 46px)", lineHeight: 1.1, fontWeight: 700, color: WHITE, margin: "24px 0 0" }}>What no estate attorney, advisor, or wealth manager can offer — the soul of a family's legacy.</h1>
            <p className="fl-serif" style={{ fontStyle: "italic", fontWeight: 500, fontSize: 16.5, color: GOLD_BRIGHT, marginTop: 22, lineHeight: 1.5, maxWidth: 560 }}>Twelve journeys. Eleven domains. One framework. A conversation no balance sheet can measure.</p>
            <div style={{ display: "flex", gap: 14, marginTop: 34, flexWrap: "wrap" }}>
              <button onClick={() => setPage("journey-builder")} className="fl-btn-gold fl-label" style={{ background: GOLD, color: WHITE, border: "none", borderRadius: 26, padding: "14px 28px", fontSize: 11.5, fontWeight: 700, cursor: "pointer" }}>Build a Journey</button>
              <button onClick={() => setPage("domains")} className="fl-label" style={{ background: "transparent", color: WHITE, border: "1px solid rgba(251,249,244,0.35)", borderRadius: 26, padding: "14px 28px", fontSize: 11.5, fontWeight: 700, cursor: "pointer" }}>See All Domains</button>
            </div>
          </div>
        </div>
      </div>

      <div style={{ maxWidth: 1200, margin: "0 auto", padding: "80px 24px" }}>
        <Eyebrow>Explore the Platform</Eyebrow>
        <h2 className="fl-serif" style={{ fontSize: "clamp(20px, 3vw, 26px)", fontWeight: 700, color: GREEN, margin: "18px 0 36px" }}>Everything, unlocked.</h2>
        <div style={{ display: "grid", gridTemplateColumns: "repeat(auto-fit, minmax(240px, 1fr))", gap: 18 }}>
          {explore.map((e) => (
            <div key={e.id} onClick={() => setPage(e.id)} className="fl-card" style={{ border: `1px solid ${LINE}`, borderRadius: 4, padding: "22px 20px", background: CREAM, cursor: "pointer" }}>
              <div className="fl-serif" style={{ fontWeight: 700, fontSize: 15, color: GREEN, marginBottom: 6, lineHeight: 1.3 }}>{e.label}</div>
              <div style={{ fontSize: 12, color: SLATE, lineHeight: 1.5, marginBottom: 12 }}>{e.desc}</div>
              <div className="fl-label" style={{ fontSize: 10, color: GOLD, fontWeight: 700 }}>Explore &rarr;</div>
            </div>
          ))}
        </div>
      </div>
      <JoinBand setPage={setPage} />
    </div>
  );
}

/* ---------------- TITLES (expanded) ---------------- */
function TitlesPage() {
  const [open, setOpen] = useState("1");
  return (
    <PageShell eyebrow="Family Legacy Journeys" title="Twelve journeys for launching a family legacy ministry.">
      <p style={{ color: SLATE, fontSize: 13.5, lineHeight: 1.7, maxWidth: 640, marginBottom: 26 }}>
        These titles speak to successful, accomplished, sophisticated families who have already heard every financial planning pitch — and offer what no estate attorney, financial advisor, or wealth manager can provide.
      </p>
      <div style={{ borderTop: `1px solid ${LINE}` }}>
        {TITLES.map((t) => {
          const isOpen = open === t.n;
          return (
            <div key={t.n} style={{ borderBottom: `1px solid ${LINE}` }}>
              <button onClick={() => setOpen(isOpen ? null : t.n)} style={{ width: "100%", background: "none", border: "none", cursor: "pointer", textAlign: "left", padding: "20px 0", display: "flex", gap: 18, alignItems: "flex-start" }}>
                <div className="fl-serif" style={{ fontSize: 18, fontWeight: 700, color: GOLD, width: 30, flexShrink: 0 }}>{t.n}</div>
                <div style={{ flex: 1 }}>
                  <div className="fl-serif" style={{ fontSize: 15.5, fontWeight: 700, color: GREEN, lineHeight: 1.3 }}>{t.title}</div>
                  <div className="fl-label" style={{ fontSize: 8, color: GOLD, marginTop: 4 }}>{t.tag}</div>
                  {isOpen && <div className="fl-fade-in" style={{ fontSize: 12.5, color: INK, marginTop: 12, lineHeight: 1.6, background: CREAM, borderLeft: `3px solid ${GOLD}`, padding: "12px 16px" }}>{t.desc}</div>}
                </div>
                <div className="fl-label" style={{ fontSize: 16, color: GOLD, flexShrink: 0 }}>{isOpen ? "\u2013" : "+"}</div>
              </button>
            </div>
          );
        })}
      </div>
    </PageShell>
  );
}

/* ---------------- DOMAINS (Intelligence Categories) ---------------- */
function DomainsPage() {
  return (
    <PageShell eyebrow="Intelligence Categories" title="Eleven domains. Every dimension of family formation and discipleship.">
      <p style={{ color: SLATE, fontSize: 13.5, lineHeight: 1.7, maxWidth: 640, marginBottom: 26 }}>
        Not separate silos — a connected ecosystem. Each domain builds on the others, and every domain shares the same eight-layer resource structure: Intelligence Brief, Discovery Assessment, 21-Day Journey, Four-Session Family Experience, Toolbox, Advisor Guide, Legacy Artifact, and Next Best Journey.
      </p>
      {DOMAINS.map((d, i) => (
        <div key={d.name} style={{ display: "flex", gap: 18, borderTop: `1px solid ${LINE}`, padding: "16px 0" }}>
          <div className="fl-serif" style={{ fontSize: 15, fontWeight: 700, color: GOLD, width: 28, flexShrink: 0 }}>{String(i + 1).padStart(2, "0")}</div>
          <div>
            <div className="fl-serif" style={{ fontWeight: 700, fontSize: 14.5, color: GREEN, marginBottom: 4 }}>{d.name}</div>
            <div style={{ fontSize: 12.5, color: INK, lineHeight: 1.55 }}>{d.desc}</div>
          </div>
        </div>
      ))}
    </PageShell>
  );
}

/* ---------------- CORE FLOW ---------------- */
function CoreFlowPage() {
  return (
    <div className="fl-fade-in">
      <div style={{ background: GREEN }}>
        <div style={{ maxWidth: 1200, margin: "0 auto", padding: "70px 24px" }}>
          <Eyebrow dark>The Core Flow of the System</Eyebrow>
          <h1 className="fl-serif" style={{ fontSize: "clamp(22px, 3vw, 30px)", fontWeight: 700, color: WHITE, maxWidth: 640, margin: "18px 0 0" }}>Every domain follows the same integrated progression.</h1>
          <div style={{ marginTop: 40 }}>
            {CORE_FLOW.map(([t, d], i) => (
              <div key={t} style={{ display: "flex", gap: 16, paddingBottom: i < CORE_FLOW.length - 1 ? 22 : 0 }}>
                <div style={{ display: "flex", flexDirection: "column", alignItems: "center", width: 32, flexShrink: 0 }}>
                  <div style={{ width: 32, height: 32, borderRadius: "50%", border: `1.5px solid ${GOLD_BRIGHT}`, color: GOLD_BRIGHT, display: "flex", alignItems: "center", justifyContent: "center", fontFamily: "Playfair Display", fontWeight: 700, fontSize: 13, flexShrink: 0 }}>{i + 1}</div>
                  {i < CORE_FLOW.length - 1 && <div style={{ width: 1.5, flex: 1, background: GOLD, opacity: 0.4, marginTop: 4 }} />}
                </div>
                <div style={{ paddingBottom: 4 }}>
                  <div className="fl-serif" style={{ fontWeight: 700, fontSize: 14.5, color: WHITE, marginBottom: 3 }}>{t}</div>
                  <div style={{ fontSize: 12.5, color: "rgba(251,249,244,0.72)" }}>{d}</div>
                </div>
              </div>
            ))}
          </div>
        </div>
      </div>
    </div>
  );
}

/* ---------------- JOURNEY BUILDER ---------------- */
function JourneyBuilderPage() {
  const [length, setLength] = useState(40);
  const [title, setTitle] = useState(TITLES[0].title);
  const [openWeek, setOpenWeek] = useState(0);
  const config = LENGTH_CONFIG[length];

  return (
    <ModuleShell eyebrow="Journey Builder" title="Build a 21, 30, or 40-day journey — with real weekly sessions and daily devotionals." subtitle="Pick a length and a title. The builder generates the week-by-week arc and sample daily devotional titles.">
      <div style={{ display: "flex", gap: 10, marginBottom: 16, flexWrap: "wrap" }}>
        {[21, 30, 40].map((l) => (
          <button key={l} onClick={() => { setLength(l); setOpenWeek(0); }} className="fl-tab" style={{ padding: "10px 20px", borderRadius: 20, border: `1.5px solid ${length === l ? GREEN : LINE}`, background: length === l ? GREEN : WHITE, color: length === l ? WHITE : INK, fontSize: 12, cursor: "pointer" }}>{l}-Day</button>
        ))}
      </div>
      <select className="fl-input" style={{ width: "100%", maxWidth: 400, marginBottom: 26 }} value={title} onChange={(e) => setTitle(e.target.value)}>
        {TITLES.map((t) => <option key={t.n}>{t.title}</option>)}
      </select>

      <div className="fl-fade-in" key={length + title}>
        <div className="fl-label" style={{ fontSize: 10, color: GOLD, marginBottom: 4 }}>{title}</div>
        <div className="fl-serif" style={{ fontSize: 18, fontWeight: 700, color: GREEN, marginBottom: 20 }}>{length} Days &middot; {config.weeks} Weeks</div>

        {config.stageIdx.map((si, wi) => {
          const stage = STAGES[si];
          const isOpen = openWeek === wi;
          return (
            <div key={wi} style={{ border: `1px solid ${LINE}`, borderRadius: 4, marginBottom: 12, overflow: "hidden" }}>
              <button onClick={() => setOpenWeek(isOpen ? null : wi)} style={{ width: "100%", background: isOpen ? CREAM : WHITE, border: "none", cursor: "pointer", textAlign: "left", padding: "16px 20px", display: "flex", justifyContent: "space-between", alignItems: "center" }}>
                <div>
                  <div className="fl-label" style={{ fontSize: 9, color: GOLD }}>Week {wi + 1}</div>
                  <div className="fl-serif" style={{ fontWeight: 700, fontSize: 15, color: GREEN }}>{title.replace(/^\d+ Days? (of|to) /i, "")} — {stage.name}</div>
                </div>
                <div className="fl-label" style={{ fontSize: 16, color: GOLD }}>{isOpen ? "\u2013" : "+"}</div>
              </button>
              {isOpen && (
                <div className="fl-fade-in" style={{ padding: "16px 20px", background: WHITE }}>
                  <div style={{ fontSize: 12, color: SLATE, marginBottom: 14, fontStyle: "italic" }}>{stage.desc}</div>
                  {stage.days.map((d, di) => (
                    <div key={d} style={{ display: "flex", gap: 10, padding: "7px 0", borderTop: di > 0 ? `1px solid ${LINE}` : "none", fontSize: 12.5 }}>
                      <span style={{ color: GOLD, fontWeight: 700 }}>Day {wi * 7 + di + 1}</span>
                      <span>{d}</span>
                    </div>
                  ))}
                  <div style={{ fontSize: 11, color: SLATE, fontStyle: "italic", marginTop: 8 }}>+ additional daily devotionals through Day {Math.min((wi + 1) * 7, length)}</div>
                </div>
              )}
            </div>
          );
        })}
      </div>
    </ModuleShell>
  );
}

/* ---------------- FRAMEWORK ---------------- */
function FrameworkPage() {
  return (
    <PageShell eyebrow="The Framework" title="Why legacy work is different from estate planning.">
      <p style={{ color: SLATE, fontSize: 14, lineHeight: 1.7, maxWidth: 640, marginBottom: 26 }}>
        Most financial planning focuses on what a family will receive. Family Legacy By Design focuses on what a family will remember, what they will believe, and how they will be prepared — before the money ever changes hands.
      </p>
      <div style={{ display: "grid", gridTemplateColumns: "repeat(auto-fit, minmax(230px, 1fr))", gap: 18, marginBottom: 40 }}>
        {[
          ["Strengthens Families at Every Stage", "Equips parents, grandparents, couples, and singles with biblical tools to define, protect, and pass down their values — not just their valuables."],
          ["Builds Multi-Generational Discipleship", "Becomes a catalyst for discipling children and adult children in a way no single Sunday sermon can produce."],
          ["Prevents Financial and Relational Drift", "Helps families proactively clarify purpose and guard unity instead of waiting for crisis."],
          ["Opens Doors to High-Capacity Families", "Speaks directly to business owners, founders, and wealth builders."],
        ].map(([t, d]) => (
          <div key={t} style={{ borderTop: `2px solid ${GOLD}`, paddingTop: 12 }}>
            <div className="fl-serif" style={{ fontWeight: 700, fontSize: 14, color: GREEN, marginBottom: 6, lineHeight: 1.3 }}>{t}</div>
            <div style={{ fontSize: 12, color: SLATE, lineHeight: 1.5 }}>{d}</div>
          </div>
        ))}
      </div>
      <div style={{ background: GREEN, borderRadius: 4, padding: "28px 26px" }}>
        <Eyebrow dark>The Platform Principle</Eyebrow>
        <p className="fl-serif" style={{ fontStyle: "italic", fontSize: 15.5, color: WHITE, lineHeight: 1.5, marginTop: 14, maxWidth: 600 }}>
          &ldquo;The campaign is not separate from the ministry launch. The campaign IS the ministry launch.&rdquo;
        </p>
      </div>
    </PageShell>
  );
}

/* ---------------- CHURCHES ---------------- */
function ChurchesPage({ setPage }) {
  return (
    <PageShell eyebrow="For Churches" title="Launch a family legacy cohort in your congregation.">
      <p style={{ color: SLATE, fontSize: 14, lineHeight: 1.7, maxWidth: 640, marginBottom: 26 }}>
        Every ministry a church wants to build needs a moment of ignition. Family Legacy is that campaign for the demographic most churches never fully reach.
      </p>
      {[
        ["1. Choose Your Opening Title", "Start with 40 Days of Family Legacy as the flagship, or 21 Days to Remember as a lighter first taste."],
        ["2. Run the Campaign", "Weekend teaching, small group curriculum, and daily devotionals build theological conviction."],
        ["3. Celebration Sunday", "Stories from families who did the work prove what the campaign promised is real."],
        ["4. Launch the Cohort", "A quarterly gathering of high-capacity families around values, calling, and generational faithfulness."],
      ].map(([t, d], i) => (
        <div key={t} style={{ display: "flex", gap: 18, paddingBottom: i < 3 ? 22 : 0 }}>
          <div style={{ width: 32, height: 32, borderRadius: "50%", background: GREEN, color: GOLD_BRIGHT, display: "flex", alignItems: "center", justifyContent: "center", fontFamily: "Playfair Display", fontWeight: 700, fontSize: 13, flexShrink: 0 }}>{i + 1}</div>
          <div>
            <div className="fl-serif" style={{ fontWeight: 700, fontSize: 14.5, color: GREEN, marginBottom: 3 }}>{t.slice(3)}</div>
            <div style={{ fontSize: 12.5, color: SLATE, lineHeight: 1.5, maxWidth: 540 }}>{d}</div>
          </div>
        </div>
      ))}
      <div style={{ marginTop: 34, textAlign: "center", background: CREAM, borderRadius: 4, padding: "34px 22px" }}>
        <div className="fl-serif" style={{ fontWeight: 700, fontSize: 17, color: GREEN, marginBottom: 8 }}>Ready to talk through what this looks like?</div>
        <button onClick={() => setPage("pricing")} className="fl-btn-gold fl-label" style={{ background: GOLD, color: WHITE, border: "none", borderRadius: 22, padding: "11px 24px", fontSize: 10.5, fontWeight: 700, cursor: "pointer" }}>See Pricing</button>
      </div>
    </PageShell>
  );
}

/* ---------------- ADVISORS (expanded with journeys) ---------------- */
function AdvisorsPage({ setPage }) {
  return (
    <PageShell eyebrow="For Advisors" title="Bring this into your highest-capacity client relationships.">
      <p style={{ color: SLATE, fontSize: 14, lineHeight: 1.7, maxWidth: 640, marginBottom: 26 }}>
        Family Legacy By Design is a natural extension of the Christian Advisor Network's Legacy Family Conversation System and Family Legacy Builder — the same framework, deployed through a campaign rhythm instead of a single meeting.
      </p>
      <div className="fl-label" style={{ fontSize: 10, color: GOLD, marginBottom: 14 }}>Advisor Journeys</div>
      {ADVISOR_JOURNEYS.map((j) => (
        <div key={j.title} className="fl-card" style={{ border: `1px solid ${LINE}`, borderRadius: 4, padding: "18px 20px", marginBottom: 12 }}>
          <div style={{ display: "flex", justifyContent: "space-between", marginBottom: 6 }}>
            <div className="fl-serif" style={{ fontWeight: 700, fontSize: 14.5, color: GREEN }}>{j.title}</div>
            <span className="fl-label" style={{ fontSize: 9, color: GOLD }}>{j.length}</span>
          </div>
          <div style={{ fontSize: 12.5, color: SLATE, lineHeight: 1.5 }}>{j.desc}</div>
        </div>
      ))}
      <button onClick={() => setPage("advisor-access")} className="fl-btn-gold fl-label" style={{ marginTop: 10, background: "none", border: `1px solid ${GREEN}`, color: GREEN, borderRadius: 22, padding: "11px 22px", fontSize: 10.5, fontWeight: 700, cursor: "pointer" }}>What to Understand Before Full Access &rarr;</button>
    </PageShell>
  );
}

/* ---------------- ADVISOR ACCESS (before you say yes) ---------------- */
function AdvisorAccessPage({ setPage }) {
  const considerations = [
    ["This is formation, not advice", "Nothing in this system replaces legal, tax, or financial advice — it prepares families for those conversations, and prepares you to have the ones that are actually yours to have."],
    ["Full access means full responsibility", "All-access unlocks every domain, every assessment, and every family's data across your relationships. That's a real trust commitment, not just a feature unlock."],
    ["Know your lane before you start", "Each domain includes explicit boundaries of expertise — read them before the first family conversation, not after a hard one."],
    ["Family consent governs everything", "A family's Sources, assessments, and legacy artifacts are theirs. Full access to the platform does not mean unrestricted access to any specific family's content without their invitation."],
    ["This is a multi-year relationship tool", "The system is built for a family engaged over years, not a single high-pressure session. Plan your practice's capacity accordingly."],
    ["Certification is available, and worth doing first", "The Advisor Certification Journey exists specifically so you're facilitating with real skill before you're facilitating with full access."],
  ];
  return (
    <PageShell eyebrow="Before You Say Yes to All Access" title="What advisors need to understand before committing to full access.">
      {considerations.map(([t, d], i) => (
        <div key={t} style={{ display: "flex", gap: 16, borderTop: `1px solid ${LINE}`, padding: "16px 0" }}>
          <div className="fl-serif" style={{ fontSize: 14, fontWeight: 700, color: GOLD, width: 24, flexShrink: 0 }}>{i + 1}</div>
          <div>
            <div className="fl-serif" style={{ fontWeight: 700, fontSize: 14, color: GREEN, marginBottom: 4 }}>{t}</div>
            <div style={{ fontSize: 12.5, color: INK, lineHeight: 1.55 }}>{d}</div>
          </div>
        </div>
      ))}
      <div style={{ marginTop: 26, background: GREEN, borderRadius: 4, padding: "24px 24px" }}>
        <p style={{ fontSize: 12.5, color: "rgba(251,249,244,0.85)", lineHeight: 1.6, margin: 0 }}>None of this is meant to slow you down — it's meant to make sure full access is actually the right starting point, not just the most available one.</p>
      </div>
    </PageShell>
  );
}

/* ---------------- ASSESSMENTS (fully interactive, no email) ---------------- */
function AssessmentsPage() {
  const [active, setActive] = useState(null);
  const [scores, setScores] = useState({});
  const [submitted, setSubmitted] = useState(false);

  const startAssessment = (a) => {
    setActive(a);
    setScores(Object.fromEntries(a.dims.map((d) => [d, 5])));
    setSubmitted(false);
  };
  const avg = active ? Object.values(scores).reduce((x, y) => x + y, 0) / active.dims.length : 0;

  if (active) {
    return (
      <ModuleShell eyebrow="Assessments" title={active.name} subtitle={active.desc}>
        {!submitted ? (
          <div className="fl-card" style={{ padding: 24 }}>
            {active.dims.map((d) => (
              <div key={d} style={{ marginBottom: 16 }}>
                <div style={{ display: "flex", justifyContent: "space-between", fontSize: 13, marginBottom: 4 }}>
                  <span>{d}</span><span style={{ fontWeight: 700, color: GOLD }}>{scores[d]}/10</span>
                </div>
                <input type="range" min="1" max="10" value={scores[d]} onChange={(e) => setScores((s) => ({ ...s, [d]: Number(e.target.value) }))} style={{ width: "100%" }} />
              </div>
            ))}
            <button onClick={() => setSubmitted(true)} className="fl-btn-gold fl-label" style={{ background: GOLD, color: WHITE, border: "none", borderRadius: 22, padding: "11px 24px", fontSize: 11, fontWeight: 700, cursor: "pointer" }}>See My Results</button>
          </div>
        ) : (
          <div className="fl-fade-in">
            <div style={{ background: GREEN, borderRadius: 4, padding: "26px 26px", marginBottom: 20 }}>
              <div className="fl-label" style={{ fontSize: 10, color: GOLD_BRIGHT, marginBottom: 8 }}>Your Score</div>
              <div className="fl-serif" style={{ fontSize: 28, fontWeight: 700, color: WHITE }}>{avg.toFixed(1)} / 10</div>
            </div>
            {Object.entries(scores).sort((a, b) => a[1] - b[1]).map(([k, v], i) => (
              <div key={k} style={{ padding: "10px 0", borderTop: `1px solid ${LINE}`, display: "flex", justifyContent: "space-between", fontSize: 13 }}>
                <span>{i === 0 ? "\u2b50 " : ""}{k}</span><span style={{ fontWeight: 700, color: GOLD }}>{v}/10</span>
              </div>
            ))}
            <p style={{ fontSize: 12, color: SLATE, fontStyle: "italic", marginTop: 14 }}>Lowest score above is the most natural place to start.</p>
            <button onClick={() => setActive(null)} className="fl-label" style={{ marginTop: 14, background: "none", border: `1px solid ${GREEN}`, color: GREEN, borderRadius: 20, padding: "9px 18px", fontSize: 10.5, fontWeight: 700, cursor: "pointer" }}>Back to All Assessments</button>
          </div>
        )}
      </ModuleShell>
    );
  }

  return (
    <ModuleShell eyebrow="Assessments" title="Where is this family's legacy work actually ready to begin?" subtitle="All four are unlocked — take any of them right now. Results show immediately, no email required.">
      <div style={{ display: "grid", gridTemplateColumns: "repeat(auto-fit, minmax(250px, 1fr))", gap: 16 }}>
        {ASSESSMENTS.map((a) => (
          <div key={a.name} className="fl-card" style={{ border: `1px solid ${LINE}`, borderRadius: 4, padding: "20px 20px", background: WHITE }}>
            <div className="fl-serif" style={{ fontWeight: 700, fontSize: 14.5, color: GREEN, marginBottom: 8, lineHeight: 1.3 }}>{a.name}</div>
            <div style={{ fontSize: 12, color: SLATE, lineHeight: 1.5, marginBottom: 14 }}>{a.desc}</div>
            <button onClick={() => startAssessment(a)} className="fl-label" style={{ width: "100%", background: "none", border: `1px solid ${GREEN}`, color: GREEN, borderRadius: 20, padding: "9px 0", fontSize: 10, fontWeight: 700, cursor: "pointer" }}>Take the Assessment</button>
          </div>
        ))}
      </div>
    </ModuleShell>
  );
}

/* ---------------- CUSTOMIZATION & DELIVERY ---------------- */
function CustomizationPage() {
  return (
    <PageShell eyebrow="Customize &amp; Deliver" title="How this becomes your church's, or your practice's, own.">
      <div className="fl-label" style={{ fontSize: 10, color: GOLD, marginBottom: 12 }}>Customization</div>
      {[
        ["Pastor or advisor introduction", "Record or write a personal welcome that opens every session."],
        ["Local stories woven in", "Replace placeholder illustrations with real stories from your own families."],
        ["Branding applied throughout", "Your church or practice's colors, logo, and voice on every piece."],
        ["Length and depth adjusted", "Use the Journey Builder to select 21, 30, or 40 days based on your calendar."],
      ].map(([t, d]) => (
        <div key={t} style={{ borderTop: `1px solid ${LINE}`, padding: "14px 0" }}>
          <div className="fl-serif" style={{ fontWeight: 700, fontSize: 14, color: GREEN, marginBottom: 3 }}>{t}</div>
          <div style={{ fontSize: 12.5, color: SLATE }}>{d}</div>
        </div>
      ))}

      <div className="fl-label" style={{ fontSize: 10, color: GOLD, margin: "30px 0 12px" }}>Delivery</div>
      <div style={{ display: "grid", gridTemplateColumns: "repeat(auto-fit, minmax(240px, 1fr))", gap: 16 }}>
        <div className="fl-card" style={{ border: `1px solid ${LINE}`, borderRadius: 4, padding: 22 }}>
          <div className="fl-serif" style={{ fontWeight: 700, fontSize: 15.5, color: GREEN, marginBottom: 8 }}>Digital Delivery</div>
          <p style={{ fontSize: 12.5, color: SLATE, lineHeight: 1.55 }}>Every session, devotional, and tool delivered through the platform — searchable, always up to date, ready the moment a family or advisor needs it.</p>
        </div>
        <div className="fl-card" style={{ border: `1px solid ${LINE}`, borderRadius: 4, padding: 22 }}>
          <div className="fl-serif" style={{ fontWeight: 700, fontSize: 15.5, color: GREEN, marginBottom: 8 }}>Print on Demand</div>
          <p style={{ fontSize: 12.5, color: SLATE, lineHeight: 1.55 }}>A bound, printed journal for families and advisors who want the physical experience — produced per order, no minimum print run required.</p>
        </div>
      </div>
    </PageShell>
  );
}

/* ---------------- PRICING ---------------- */
function PricingPage({ setPage }) {
  const tiers = [
    { name: "Single Journey", price: "One-time license", desc: "License one Family Legacy journey for a single church campaign or advisor engagement.", features: ["One journey, any length", "Digital delivery", "Basic customization"] },
    { name: "Church Partnership", price: "Annual license", desc: "Full journey library, cohort tools, and ongoing support for launching and sustaining a legacy ministry.", features: ["All twelve journeys", "Cohort &amp; churches tools", "Full customization", "Print-on-demand available"], featured: true },
    { name: "Advisor All-Access", price: "Annual membership", desc: "Every domain, every assessment, every advisor journey — for a practice building this into client relationships at scale.", features: ["All domains &amp; assessments", "Advisor Certification Journey", "Client-branded delivery", "Priority support"] },
  ];
  return (
    <PageShell eyebrow="Pricing" title="What it costs to bring this to your church or practice.">
      <div style={{ display: "grid", gridTemplateColumns: "repeat(auto-fit, minmax(240px, 1fr))", gap: 18 }}>
        {tiers.map((t) => (
          <div key={t.name} className="fl-card" style={{ border: t.featured ? `2px solid ${GOLD}` : `1px solid ${LINE}`, borderRadius: 6, padding: 24, background: t.featured ? CREAM : WHITE }}>
            {t.featured && <div className="fl-label" style={{ fontSize: 9, color: GOLD, marginBottom: 10 }}>Most Common</div>}
            <div className="fl-serif" style={{ fontWeight: 700, fontSize: 17, color: GREEN, marginBottom: 4 }}>{t.name}</div>
            <div className="fl-label" style={{ fontSize: 9.5, color: SLATE, marginBottom: 14 }}>{t.price}</div>
            <p style={{ fontSize: 12, color: INK, lineHeight: 1.55, marginBottom: 16 }}>{t.desc}</p>
            {t.features.map((f) => <div key={f} style={{ fontSize: 11.5, color: SLATE, padding: "6px 0", borderTop: `1px solid ${LINE}` }}>&middot; {f}</div>)}
          </div>
        ))}
      </div>
      <p style={{ fontSize: 12, color: SLATE, fontStyle: "italic", marginTop: 20 }}>Specific figures are confirmed during your strategy conversation and depend on church or practice size.</p>
      <button onClick={() => setPage("advisor-access")} className="fl-btn-gold fl-label" style={{ marginTop: 14, background: GOLD, color: WHITE, border: "none", borderRadius: 22, padding: "12px 26px", fontSize: 11, fontWeight: 700, cursor: "pointer" }}>What Advisors Should Know First</button>
    </PageShell>
  );
}

/* ---------------- ABOUT ---------------- */
function AboutPage() {
  return (
    <PageShell eyebrow="About" title="Built on Tom Conway's Family Legacy By Design curriculum.">
      <p style={{ color: SLATE, fontSize: 14, lineHeight: 1.7, maxWidth: 640 }}>
        Delivered through the Lifetogether campaign platform — twenty-five years of churchwide campaign, curriculum, and small-group ministry experience, applied to the one demographic most churches have never fully reached.
      </p>
    </PageShell>
  );
}

/* ---------------- LIBRARY (200 journeys, 24 categories) ---------------- */
function LibraryPage() {
  const [query, setQuery] = useState("");
  const [cat, setCat] = useState("All Categories");
  const [lenFilter, setLenFilter] = useState("All Lengths");
  const catNames = ["All Categories", ...LIBRARY_CATEGORIES.map((c) => c.name)];

  const filtered = LIBRARY_CATEGORIES
    .filter((c) => cat === "All Categories" || c.name === cat)
    .map((c) => ({ ...c, items: c.items.filter((i) => {
      const matchesQuery = !query || i.t.toLowerCase().includes(query.toLowerCase()) || c.name.toLowerCase().includes(query.toLowerCase());
      const matchesLen = lenFilter === "All Lengths" || i.len === Number(lenFilter);
      return matchesQuery && matchesLen;
    }) }))
    .filter((c) => c.items.length > 0);
  const total = filtered.reduce((sum, c) => sum + c.items.length, 0);

  return (
    <PageShell eyebrow="The Full Library" title={`${LIBRARY_TOTAL} journeys across ${LIBRARY_CATEGORIES.length} categories.`}>
      <p style={{ color: SLATE, fontSize: 13, lineHeight: 1.65, maxWidth: 620, marginBottom: 22 }}>
        Every category follows the same eight-layer resource structure. Search by title, category, or browse everything unlocked below.
      </p>
      <div style={{ display: "flex", gap: 10, flexWrap: "wrap", marginBottom: 10 }}>
        <input className="fl-input" placeholder="Search titles..." value={query} onChange={(e) => setQuery(e.target.value)} style={{ flex: "1 1 220px" }} />
        <select className="fl-input" value={cat} onChange={(e) => setCat(e.target.value)} style={{ flex: "1 1 200px" }}>
          {catNames.map((c) => <option key={c}>{c}</option>)}
        </select>
        <select className="fl-input" value={lenFilter} onChange={(e) => setLenFilter(e.target.value)} style={{ flex: "1 1 140px" }}>
          {["All Lengths", "21", "30", "40"].map((l) => <option key={l}>{l === "All Lengths" ? l : l + " Days"}</option>)}
        </select>
      </div>
      <div className="fl-label" style={{ fontSize: 9.5, color: GOLD, marginBottom: 20 }}>{total} matching journey{total === 1 ? "" : "s"}</div>

      {filtered.map((c) => (
        <div key={c.name} style={{ marginBottom: 26 }}>
          <div className="fl-serif" style={{ fontWeight: 700, fontSize: 15, color: GREEN, marginBottom: 4 }}>{c.name}</div>
          <div style={{ display: "grid", gridTemplateColumns: "repeat(auto-fit, minmax(220px, 1fr))", gap: "6px 16px" }}>
            {c.items.map((i) => (
              <div key={i.t} style={{ display: "flex", justifyContent: "space-between", padding: "8px 0", borderTop: `1px solid ${LINE}`, fontSize: 12.5 }}>
                <span>{i.t}</span>
                <span className="fl-label" style={{ fontSize: 8.5, color: SLATE }}>{i.len}d</span>
              </div>
            ))}
          </div>
        </div>
      ))}
      {total === 0 && <div style={{ textAlign: "center", padding: "40px 20px", color: SLATE, fontSize: 13 }}>No journeys match that search.</div>}
    </PageShell>
  );
}

/* ---------------- PORTAL (member / logged-in experience) ---------------- */
function PortalPage() {
  const [tab, setTab] = useState("family");
  const portalTabs = [
    ["family", "My Family"],
    ["progress", "My Journey Progress"],
    ["results", "My Assessment Results"],
    ["artifacts", "My Legacy Artifacts"],
    ["account", "Account"],
  ];
  return (
    <ModuleShell eyebrow="Portal" title="The member experience — what a family or advisor sees once inside." subtitle="This is a preview of the logged-in portal, separate from the public site above.">
      <div style={{ display: "flex", gap: 8, marginBottom: 24, flexWrap: "wrap" }}>
        {portalTabs.map(([id, label]) => (
          <button key={id} onClick={() => setTab(id)} className="fl-tab" style={{ padding: "9px 16px", borderRadius: 18, border: `1.5px solid ${tab === id ? GREEN : LINE}`, background: tab === id ? GREEN : WHITE, color: tab === id ? WHITE : INK, fontSize: 11, cursor: "pointer" }}>{label}</button>
        ))}
      </div>

      {tab === "family" && (
        <div className="fl-fade-in fl-card" style={{ border: `1px solid ${LINE}`, borderRadius: 4, padding: 24 }}>
          <div className="fl-serif" style={{ fontWeight: 700, fontSize: 17, color: GREEN, marginBottom: 6 }}>The Anderson Family</div>
          <div style={{ fontSize: 12.5, color: SLATE, marginBottom: 18 }}>4 family members &middot; Member since 2025</div>
          {["Robert Anderson (Founder)", "Linda Anderson (Founder)", "James Anderson (Next-Gen)", "Grace Anderson (Next-Gen)"].map((m) => (
            <div key={m} style={{ padding: "9px 0", borderTop: `1px solid ${LINE}`, fontSize: 13 }}>{m}</div>
          ))}
        </div>
      )}

      {tab === "progress" && (
        <div className="fl-fade-in">
          <div className="fl-card" style={{ border: `1px solid ${LINE}`, borderRadius: 4, padding: 22, marginBottom: 14 }}>
            <div style={{ display: "flex", justifyContent: "space-between", marginBottom: 10 }}>
              <div className="fl-serif" style={{ fontWeight: 700, fontSize: 15, color: GREEN }}>40 Days of Family Legacy</div>
              <span className="fl-label" style={{ fontSize: 9.5, color: GOLD }}>Day 24 of 40</span>
            </div>
            <div style={{ height: 6, background: LINE, borderRadius: 3 }}><div style={{ height: 6, width: "60%", background: GOLD, borderRadius: 3 }} /></div>
          </div>
          <div className="fl-card" style={{ border: `1px solid ${LINE}`, borderRadius: 4, padding: 22 }}>
            <div style={{ display: "flex", justifyContent: "space-between", marginBottom: 10 }}>
              <div className="fl-serif" style={{ fontWeight: 700, fontSize: 15, color: GREEN }}>21 Days of Generosity</div>
              <span className="fl-label" style={{ fontSize: 9.5, color: GOLD }}>Not started</span>
            </div>
            <div style={{ height: 6, background: LINE, borderRadius: 3 }}><div style={{ height: 6, width: "0%", background: GOLD, borderRadius: 3 }} /></div>
          </div>
        </div>
      )}

      {tab === "results" && (
        <div className="fl-fade-in">
          {ASSESSMENTS.map((a) => (
            <div key={a.name} style={{ display: "flex", justifyContent: "space-between", padding: "12px 0", borderTop: `1px solid ${LINE}`, fontSize: 13 }}>
              <span>{a.name}</span>
              <span style={{ fontWeight: 700, color: GOLD }}>{(Math.random() * 3 + 6).toFixed(1)}/10</span>
            </div>
          ))}
        </div>
      )}

      {tab === "artifacts" && (
        <div className="fl-fade-in">
          {["Family Mission Statement", "Spiritual Legacy Letter (Robert)", "Family Values Card Set"].map((a) => (
            <div key={a} className="fl-card" style={{ border: `1px solid ${LINE}`, borderRadius: 4, padding: 18, marginBottom: 10, display: "flex", justifyContent: "space-between", alignItems: "center" }}>
              <span className="fl-serif" style={{ fontWeight: 700, fontSize: 13.5 }}>{a}</span>
              <span className="fl-label" style={{ fontSize: 9, color: GOLD }}>View / Download</span>
            </div>
          ))}
        </div>
      )}

      {tab === "account" && (
        <div className="fl-fade-in fl-card" style={{ border: `1px solid ${LINE}`, borderRadius: 4, padding: 22 }}>
          <div style={{ fontSize: 13, padding: "8px 0" }}>Plan: <b>Church Partnership</b></div>
          <div style={{ fontSize: 13, padding: "8px 0", borderTop: `1px solid ${LINE}` }}>Renews: January 2027</div>
          <div style={{ fontSize: 13, padding: "8px 0", borderTop: `1px solid ${LINE}` }}>Seats used: 3 of 10</div>
        </div>
      )}
    </ModuleShell>
  );
}

/* ---------------- SHARED ---------------- */
function PageShell({ eyebrow, title, children }) {
  return (
    <div className="fl-fade-in" style={{ maxWidth: 1200, margin: "0 auto", padding: "60px 24px 90px" }}>
      <Eyebrow>{eyebrow}</Eyebrow>
      <h1 className="fl-serif" style={{ fontSize: "clamp(22px, 3.4vw, 30px)", fontWeight: 700, color: GREEN, maxWidth: 700, margin: "18px 0 26px", lineHeight: 1.25 }}>{title}</h1>
      {children}
    </div>
  );
}
function ModuleShell({ eyebrow, title, subtitle, children }) {
  return (
    <div className="fl-fade-in" style={{ maxWidth: 900, margin: "0 auto", padding: "60px 24px 90px" }}>
      <Eyebrow>{eyebrow}</Eyebrow>
      <h1 className="fl-serif" style={{ fontSize: "clamp(22px, 3.4vw, 28px)", fontWeight: 700, color: GREEN, marginBottom: 8, marginTop: 18 }}>{title}</h1>
      {subtitle && <p style={{ fontSize: 13, color: SLATE, lineHeight: 1.6, maxWidth: 600, marginBottom: 26 }}>{subtitle}</p>}
      {children}
    </div>
  );
}
function JoinBand({ setPage }) {
  return (
    <div style={{ background: `linear-gradient(200deg, ${GREEN2} 0%, #12261D 100%)`, textAlign: "center" }}>
      <div style={{ maxWidth: 640, margin: "0 auto", padding: "80px 24px" }}>
        <Eyebrow dark>Start a Conversation</Eyebrow>
        <h2 className="fl-serif" style={{ fontSize: "clamp(22px, 4vw, 30px)", fontWeight: 700, color: WHITE, margin: "18px 0 0", lineHeight: 1.2 }}>What are you building here, and what will outlast it?</h2>
        <button onClick={() => setPage("pricing")} className="fl-btn-gold fl-label" style={{ marginTop: 26, background: GOLD, color: WHITE, border: "none", borderRadius: 28, padding: "15px 32px", fontSize: 12, fontWeight: 700, cursor: "pointer" }}>See Pricing</button>
      </div>
    </div>
  );
}

export default function FamilyLegacyByDesignSite() {
  const [page, setPage] = useState("home");
  const [menuOpen, setMenuOpen] = useState(false);
  const [scrolled, setScrolled] = useState(false);
  useEffect(() => { const f = () => setScrolled(window.scrollY > 24); window.addEventListener("scroll", f); return () => window.removeEventListener("scroll", f); }, []);
  useEffect(() => { window.scrollTo(0, 0); }, [page]);
  return (
    <div className="fl-root">
      <style>{FONTS}</style>
      <HeaderNav page={page} setPage={setPage} menuOpen={menuOpen} setMenuOpen={setMenuOpen} scrolled={scrolled} />
      {page === "home" && <HomePage setPage={setPage} />}
      {page === "titles" && <TitlesPage />}
      {page === "library" && <LibraryPage />}
      {page === "domains" && <DomainsPage />}
      {page === "core-flow" && <CoreFlowPage />}
      {page === "journey-builder" && <JourneyBuilderPage />}
      {page === "framework" && <FrameworkPage />}
      {page === "churches" && <ChurchesPage setPage={setPage} />}
      {page === "advisors" && <AdvisorsPage setPage={setPage} />}
      {page === "advisor-access" && <AdvisorAccessPage setPage={setPage} />}
      {page === "assessments" && <AssessmentsPage />}
      {page === "customization" && <CustomizationPage />}
      {page === "pricing" && <PricingPage setPage={setPage} />}
      {page === "portal" && <PortalPage />}
      {page === "about" && <AboutPage />}
      <FooterNav page={page} setPage={setPage} />
    </div>
  );
}
