import React, { useState, useEffect } from "react";

const INK = "#1B1D22";
const INK2 = "#252932";
const STEEL = "#3D4653";
const BRONZE = "#A9743F";
const BRONZE_BRIGHT = "#C99A5E";
const WHITE = "#FAFAF8";
const CREAM = "#EFEDE7";
const TXT = "#22252A";
const SLATE = "#6B7280";
const LINE = "#DDDAD2";

const FONTS = `
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,600;0,700;0,900;1,500;1,600&family=Archivo:wght@500;600;700&family=Inter:wght@400;500;600;700&display=swap');
* { box-sizing: border-box; }
body { margin: 0; }
.pb-root { font-family: 'Inter', sans-serif; color: ${TXT}; background: ${WHITE}; }
.pb-serif { font-family: 'Playfair Display', serif; }
.pb-label { font-family: 'Archivo', sans-serif; letter-spacing: 0.14em; text-transform: uppercase; }
.pb-eyebrow { display:flex; align-items:center; gap:10px; font-family:'Archivo',sans-serif; font-weight:600; font-size:12px; letter-spacing:0.18em; text-transform:uppercase; color:${BRONZE}; }
.pb-eyebrow::before { content:''; width:26px; height:2px; background:${BRONZE}; display:inline-block; }
.pb-eyebrow.on-dark { color:${BRONZE_BRIGHT}; }
.pb-eyebrow.on-dark::before { background:${BRONZE_BRIGHT}; }
.pb-nav-link { position:relative; background:none; border:none; cursor:pointer; font-family:'Archivo'; }
.pb-nav-link::after { content:''; position:absolute; left:0; right:0; bottom:-6px; height:1.5px; background:${BRONZE_BRIGHT}; transform:scaleX(0); transition:transform .25s ease; }
.pb-nav-link:hover::after { transform:scaleX(1); }
.pb-nav-link.active::after { transform:scaleX(1); background:${BRONZE}; }
.pb-card { transition: transform .35s cubic-bezier(.2,.7,.3,1), border-color .3s ease; }
.pb-card:hover { transform: translateY(-3px); }
.pb-btn { transition: background .2s ease, color .2s ease, transform .2s ease; }
.pb-btn:hover { transform: translateY(-1px); }
.pb-fade { animation: pbFade .5s ease both; }
@keyframes pbFade { from { opacity:0; transform:translateY(8px);} to {opacity:1; transform:translateY(0);} }
.pb-footer-link { background:none; border:none; cursor:pointer; text-align:left; padding:0; }
.pb-desktop-only { display: none; }
@media (min-width: 900px) { .pb-desktop-only { display: flex !important; } }
.pb-mobile-only { display: inline-block; }
@media (min-width: 900px) { .pb-mobile-only { display: none !important; } }
::selection { background: ${BRONZE}; color: ${WHITE}; }
`;

const PAGES = [
  { id: "home", label: "Home" },
  { id: "campaigns", label: "The Nine Journeys" },
  { id: "companies", label: "For Companies" },
  { id: "leaders", label: "For Leaders" },
  { id: "assessment", label: "Assessment" },
  { id: "about", label: "About" },
];
function pageLabel(id) { const p = PAGES.find((p) => p.id === id); return p ? p.label : id; }

const CAMPAIGNS = [
  { n: "1", title: "Why Work Matters", tag: "THE ENTRY POINT · WIDEST REACH", desc: "Every professional is already asking the purpose question about their work — this is the front door, the journey every leadership development program should start with." },
  { n: "2", title: "Business as a Force for Good", tag: "PURPOSE BEYOND PROFIT", desc: "Reframes the company as more than a revenue engine — every product a chance to serve, every employee a person entrusted to your care, every transaction a chance to build something that matters." },
  { n: "3", title: "Deploying What You've Been Given", tag: "STEWARDSHIP · ACCOUNTABILITY", desc: "Every leader has been given more than most — capital, influence, people, platforms. The question this journey sits with: am I deploying what I've been given in proportion to what I've received?" },
  { n: "4", title: "The Excellence Standard", tag: "INTEGRITY · WITNESS · CRAFT", desc: "History's most trusted leaders distinguished themselves through exceptional, consistent excellence. This journey makes that excellence intentional rather than accidental." },
  { n: "5", title: "The Builder's Calling", tag: "FOUNDERS · BUILDERS · VISIONARIES", desc: "For the founder whose drive isn't merely commercial — it's the expression of something they were made to create. A framework for the entrepreneurial instinct." },
  { n: "6", title: "Built to Last", tag: "SUCCESSION · EXIT · LEGACY", desc: "For the leader thinking about what happens to what they built when they're no longer running it. Connects directly into succession and exit planning conversations." },
  { n: "7", title: "Generosity That Scales", tag: "HIGH-CAPACITY GIVING", desc: "Connects business success to giving back at scale — structured philanthropy, donor-advised funds, and what it means to give proportionally to what you've built." },
  { n: "8", title: "The Servant Leadership Advantage", tag: "COUNTERINTUITIVE LEADERSHIP", desc: "The most disruptive leadership philosophy ever practiced is also the most effective: the leader who actually serves becomes the most trusted person in the room." },
  { n: "9", title: "The Second Half", tag: "SUCCESS TO SIGNIFICANCE", desc: "Built on the most important question successful people ask: now that I've won the first half, what is the second half actually for?" },
];

function Eyebrow({ children, dark }) { return <div className={`pb-eyebrow${dark ? " on-dark" : ""}`}>{children}</div>; }

function HeaderNav({ page, setPage, menuOpen, setMenuOpen, scrolled }) {
  return (
    <div style={{ position: "sticky", top: 0, zIndex: 50, background: scrolled || page !== "home" ? "rgba(27,29,34,0.97)" : "transparent", borderBottom: `1px solid rgba(169,116,63,0.25)`, backdropFilter: "blur(6px)", transition: "background .3s ease" }}>
      <div style={{ maxWidth: 1200, margin: "0 auto", padding: "18px 28px", display: "flex", alignItems: "center", justifyContent: "space-between" }}>
        <button onClick={() => setPage("home")} className="pb-serif" style={{ background: "none", border: "none", cursor: "pointer", fontWeight: 700, fontSize: 16.5, color: WHITE }}>Purpose Built Business<span style={{ fontSize: 10, verticalAlign: "super" }}>™</span></button>
        <div className="pb-desktop-only" style={{ gap: 22 }}>
          {PAGES.filter((p) => p.id !== "home").map((p) => (
            <button key={p.id} onClick={() => setPage(p.id)} className={`pb-nav-link pb-label${page === p.id ? " active" : ""}`} style={{ fontSize: 10.8, fontWeight: 600, color: page === p.id ? BRONZE_BRIGHT : "rgba(250,250,248,0.85)" }}>{p.label}</button>
          ))}
        </div>
        <button onClick={() => setPage("companies")} className="pb-btn pb-label pb-desktop-only" style={{ background: BRONZE, color: WHITE, border: "none", borderRadius: 22, padding: "9px 18px", fontSize: 10.5, fontWeight: 700, cursor: "pointer" }}>Bring This to Your Company</button>
        <button onClick={() => setMenuOpen((v) => !v)} className="pb-mobile-only" style={{ background: "none", border: `1px solid rgba(169,116,63,0.5)`, borderRadius: 8, padding: "8px 12px", color: BRONZE_BRIGHT, cursor: "pointer", fontSize: 13 }}>{menuOpen ? "Close" : "Menu"}</button>
      </div>
      {menuOpen && (
        <div style={{ background: INK, borderTop: `1px solid rgba(169,116,63,0.25)`, padding: "8px 28px 24px" }}>
          {PAGES.map((p) => (
            <div key={p.id} onClick={() => { setPage(p.id); setMenuOpen(false); }} className="pb-label" style={{ padding: "12px 0", borderBottom: "1px solid rgba(169,116,63,0.2)", color: page === p.id ? BRONZE_BRIGHT : "rgba(250,250,248,0.9)", fontSize: 12, cursor: "pointer" }}>{p.label}</div>
          ))}
          <div onClick={() => { setPage("companies"); setMenuOpen(false); }} className="pb-label" style={{ marginTop: 16, background: BRONZE, color: WHITE, textAlign: "center", padding: "12px 0", borderRadius: 24, fontSize: 12, fontWeight: 700, cursor: "pointer" }}>Bring This to Your Company</div>
        </div>
      )}
    </div>
  );
}

function FooterNav({ page, setPage }) {
  return (
    <div style={{ background: INK, borderTop: "1px solid rgba(169,116,63,0.2)" }}>
      <div style={{ maxWidth: 1200, margin: "0 auto", padding: "50px 28px 30px", display: "grid", gridTemplateColumns: "1.3fr 1fr 1fr", gap: 36 }}>
        <div>
          <div className="pb-serif" style={{ fontWeight: 700, fontSize: 16, color: WHITE, marginBottom: 12 }}>Purpose Built Business<span style={{ fontSize: 9, verticalAlign: "super" }}>™</span></div>
          <p style={{ fontSize: 12.5, color: "rgba(250,250,248,0.6)", lineHeight: 1.6, maxWidth: 260 }}>Business with a why. Leadership with a legacy. A values-based leadership platform — a Lifetogether company.</p>
        </div>
        <div>
          <div className="pb-label" style={{ fontSize: 10, color: BRONZE_BRIGHT, marginBottom: 14 }}>Platform</div>
          {PAGES.filter((p) => p.id !== "home").map((p) => (
            <button key={p.id} onClick={() => setPage(p.id)} className="pb-footer-link" style={{ display: "block", fontSize: 12.5, color: page === p.id ? BRONZE_BRIGHT : "rgba(250,250,248,0.72)", padding: "5px 0", cursor: "pointer" }}>{p.label}</button>
          ))}
        </div>
        <div>
          <div className="pb-label" style={{ fontSize: 10, color: BRONZE_BRIGHT, marginBottom: 14 }}>Legal</div>
          {["Privacy Policy", "Terms of Use"].map((u) => <div key={u} style={{ fontSize: 12.5, color: "rgba(250,250,248,0.4)", padding: "5px 0" }}>{u} <span style={{ fontStyle: "italic" }}>(coming soon)</span></div>)}
        </div>
      </div>
      <div style={{ maxWidth: 1200, margin: "0 auto", padding: "18px 28px", borderTop: "1px solid rgba(169,116,63,0.12)", display: "flex", justifyContent: "space-between", flexWrap: "wrap", gap: 12 }}>
        <div className="pb-label" style={{ fontSize: 9.5, color: "rgba(250,250,248,0.45)" }}>PURPOSE BUILT BUSINESS™ · A LIFETOGETHER PLATFORM</div>
        <div className="pb-label" style={{ fontSize: 9.5, color: "rgba(250,250,248,0.45)" }}>DRAFT PREVIEW · NOT YET LIVE</div>
      </div>
    </div>
  );
}

function HomePage({ setPage }) {
  const explore = [
    { id: "campaigns", label: "The Nine Journeys", desc: "The complete leadership development architecture, front door to finish." },
    { id: "companies", label: "For Companies", desc: "Bulk licensing for HR, L&D, and consulting engagements." },
    { id: "leaders", label: "For Leaders", desc: "The individual path — for a founder, executive, or professional going it alone first." },
    { id: "assessment", label: "Take the Assessment", desc: "Where are you already leading with purpose, and where are you drifting?" },
  ];
  return (
    <div className="pb-fade">
      <div style={{ position: "relative", background: `linear-gradient(165deg, ${INK} 0%, #101216 100%)`, overflow: "hidden" }}>
        <div style={{ position: "absolute", inset: 0, opacity: 0.5, backgroundImage: `radial-gradient(circle at 78% 18%, rgba(169,116,63,0.16), transparent 45%)` }} />
        <div style={{ maxWidth: 1200, margin: "0 auto", padding: "88px 28px 90px", position: "relative" }}>
          <div style={{ maxWidth: 700 }}>
            <Eyebrow dark>For Founders, Executives, and Leadership Teams</Eyebrow>
            <h1 className="pb-serif" style={{ fontSize: "clamp(30px, 5vw, 48px)", lineHeight: 1.1, fontWeight: 700, color: WHITE, margin: "26px 0 0" }}>Business with a why. Leadership with a legacy.</h1>
            <p className="pb-serif" style={{ fontStyle: "italic", fontWeight: 500, fontSize: 17.5, color: BRONZE_BRIGHT, marginTop: 24, lineHeight: 1.5, maxWidth: 560 }}>A nine-journey leadership development architecture — for the leader who wants the company to matter beyond the balance sheet.</p>
            <div style={{ display: "flex", gap: 16, marginTop: 38, flexWrap: "wrap" }}>
              <button onClick={() => setPage("campaigns")} className="pb-btn pb-label" style={{ background: BRONZE, color: WHITE, border: "none", borderRadius: 26, padding: "15px 30px", fontSize: 12, fontWeight: 700, cursor: "pointer" }}>See the Nine Journeys</button>
              <button onClick={() => setPage("assessment")} className="pb-label" style={{ background: "transparent", color: WHITE, border: "1px solid rgba(250,250,248,0.35)", borderRadius: 26, padding: "15px 30px", fontSize: 12, fontWeight: 700, cursor: "pointer" }}>Take the Assessment</button>
            </div>
          </div>
        </div>
      </div>

      <div style={{ maxWidth: 1200, margin: "0 auto", padding: "90px 28px" }}>
        <Eyebrow>Explore the Platform</Eyebrow>
        <h2 className="pb-serif" style={{ fontSize: "clamp(22px, 3vw, 28px)", fontWeight: 700, color: INK, margin: "20px 0 44px" }}>Where to start.</h2>
        <div style={{ display: "grid", gridTemplateColumns: "repeat(auto-fit, minmax(260px, 1fr))", gap: 22 }}>
          {explore.map((e) => (
            <div key={e.id} onClick={() => setPage(e.id)} className="pb-card" style={{ border: `1px solid ${LINE}`, borderRadius: 4, padding: "26px 24px", background: CREAM, cursor: "pointer" }}>
              <div className="pb-serif" style={{ fontWeight: 700, fontSize: 16.5, color: INK, marginBottom: 8, lineHeight: 1.3 }}>{e.label}</div>
              <div style={{ fontSize: 13, color: SLATE, lineHeight: 1.55, marginBottom: 14 }}>{e.desc}</div>
              <div className="pb-label" style={{ fontSize: 10.5, color: BRONZE, fontWeight: 700 }}>Explore &rarr;</div>
            </div>
          ))}
        </div>
      </div>
      <JoinBand setPage={setPage} />
    </div>
  );
}

function CampaignsPage() {
  const [open, setOpen] = useState("1");
  return (
    <PageShell eyebrow="The Nine Journeys" title="A complete leadership development architecture, front door to finish.">
      <p style={{ color: SLATE, fontSize: 14, lineHeight: 1.7, maxWidth: 640, marginTop: -8, marginBottom: 30 }}>
        Nine sequenced journeys, built to launch and sustain a leadership community that meets regularly, holds each other accountable, and becomes the most values-driven group in the organization.
      </p>
      <div style={{ borderTop: `1px solid ${LINE}` }}>
        {CAMPAIGNS.map((c) => {
          const isOpen = open === c.n;
          return (
            <div key={c.n} style={{ borderBottom: `1px solid ${LINE}` }}>
              <button onClick={() => setOpen(isOpen ? null : c.n)} style={{ width: "100%", background: "none", border: "none", cursor: "pointer", textAlign: "left", padding: "22px 0", display: "flex", gap: 22, alignItems: "flex-start" }}>
                <div className="pb-serif" style={{ fontSize: 20, fontWeight: 700, color: BRONZE, width: 34, flexShrink: 0 }}>{c.n}</div>
                <div style={{ flex: 1 }}>
                  <div className="pb-serif" style={{ fontSize: 16.5, fontWeight: 700, color: INK, lineHeight: 1.3 }}>{c.title}</div>
                  <div className="pb-label" style={{ fontSize: 8.5, color: BRONZE, marginTop: 5 }}>{c.tag}</div>
                  {isOpen && <div className="pb-fade" style={{ fontSize: 13.5, color: TXT, marginTop: 14, lineHeight: 1.65, background: CREAM, borderLeft: `3px solid ${BRONZE}`, padding: "14px 18px" }}>{c.desc}</div>}
                </div>
                <div className="pb-label" style={{ fontSize: 18, color: BRONZE, flexShrink: 0 }}>{isOpen ? "\u2013" : "+"}</div>
              </button>
            </div>
          );
        })}
      </div>
    </PageShell>
  );
}

function CompaniesPage({ setPage }) {
  return (
    <PageShell eyebrow="For Companies" title="A values-driven leadership program, licensed for your organization.">
      <p style={{ color: SLATE, fontSize: 14.5, lineHeight: 1.75, maxWidth: 640, marginBottom: 30 }}>
        Built for HR, learning &amp; development, and consulting partners who want a complete, ready-to-run leadership development architecture — not another one-off workshop.
      </p>
      {[
        ["Bulk & Team Licensing", "License the full nine-journey library for your leadership team or entire organization, with facilitator guides included."],
        ["Corporate Bulk Purchase", "A leadership development journal tied to short video coaching segments — suited to HR departments and leadership development organizations buying in volume."],
        ["Consulting Partner Program", "For consultants and coaches who want to bring a complete, proven architecture into client engagements rather than building one from scratch."],
      ].map(([t, d]) => (
        <div key={t} className="pb-card" style={{ border: `1px solid ${LINE}`, borderRadius: 4, padding: "22px 24px", marginBottom: 16 }}>
          <div className="pb-serif" style={{ fontWeight: 700, fontSize: 15.5, color: INK, marginBottom: 8 }}>{t}</div>
          <div style={{ fontSize: 13, color: SLATE, lineHeight: 1.6 }}>{d}</div>
        </div>
      ))}
      <button onClick={() => setPage("about")} className="pb-btn pb-label" style={{ marginTop: 10, background: BRONZE, color: WHITE, border: "none", borderRadius: 22, padding: "12px 26px", fontSize: 11, fontWeight: 700, cursor: "pointer" }}>Start a Conversation</button>
    </PageShell>
  );
}

function LeadersPage({ setPage }) {
  return (
    <PageShell eyebrow="For Leaders" title="The individual path.">
      <p style={{ color: SLATE, fontSize: 14.5, lineHeight: 1.75, maxWidth: 640, marginBottom: 30 }}>
        For a founder, executive, or professional who wants to start alone before bringing it to a team. Same nine journeys, same depth, paced for one person.
      </p>
      <button onClick={() => setPage("assessment")} className="pb-btn pb-label" style={{ background: BRONZE, color: WHITE, border: "none", borderRadius: 22, padding: "12px 26px", fontSize: 11, fontWeight: 700, cursor: "pointer" }}>Take the Assessment</button>
    </PageShell>
  );
}

function AssessmentPage({ setPage }) {
  const [scores, setScores] = useState({ "Purpose clarity": 5, "Values alignment": 5, "Stewardship of influence": 5, "Legacy thinking": 5, "Servant leadership": 5 });
  const [done, setDone] = useState(false);
  const avg = Object.values(scores).reduce((a, b) => a + b, 0) / Object.keys(scores).length;
  return (
    <PageShell eyebrow="Assessment" title="Where are you already leading with purpose, and where are you drifting?">
      {Object.entries(scores).map(([k, v]) => (
        <div key={k} style={{ marginBottom: 16 }}>
          <div style={{ display: "flex", justifyContent: "space-between", fontSize: 13, marginBottom: 4 }}>
            <span>{k}</span><span style={{ fontWeight: 700, color: BRONZE }}>{v}/10</span>
          </div>
          <input type="range" min="1" max="10" value={v} onChange={(e) => setScores((s) => ({ ...s, [k]: Number(e.target.value) }))} style={{ width: "100%" }} />
        </div>
      ))}
      <button onClick={() => setDone(true)} className="pb-btn pb-label" style={{ background: BRONZE, color: WHITE, border: "none", borderRadius: 22, padding: "12px 26px", fontSize: 11, fontWeight: 700, cursor: "pointer" }}>See My Results</button>
      {done && (
        <div className="pb-fade" style={{ marginTop: 24, background: INK, borderRadius: 4, padding: "26px 26px" }}>
          <div className="pb-label" style={{ fontSize: 10, color: BRONZE_BRIGHT, marginBottom: 8 }}>Your Score</div>
          <div className="pb-serif" style={{ fontSize: 26, fontWeight: 700, color: WHITE, marginBottom: 10 }}>{avg.toFixed(1)} / 10</div>
          <p style={{ fontSize: 13, color: "rgba(250,250,248,0.8)", lineHeight: 1.6 }}>Start with Journey 1, Why Work Matters, then let your lowest score guide which journey to take next.</p>
        </div>
      )}
    </PageShell>
  );
}

function AboutPage() {
  return (
    <PageShell eyebrow="About" title="A values-based leadership platform, built on twenty-five years of formation work.">
      <p style={{ color: SLATE, fontSize: 14.5, lineHeight: 1.75, maxWidth: 640 }}>
        Purpose Built Business draws on the same campaign architecture used in Lifetogether's church-facing work, reframed for a secular and corporate audience — values-driven leadership development without a religious framing requirement.
      </p>
    </PageShell>
  );
}

function PageShell({ eyebrow, title, children }) {
  return (
    <div className="pb-fade" style={{ maxWidth: 1200, margin: "0 auto", padding: "80px 28px 100px" }}>
      <Eyebrow>{eyebrow}</Eyebrow>
      <h1 className="pb-serif" style={{ fontSize: "clamp(24px, 3.4vw, 34px)", fontWeight: 700, color: INK, maxWidth: 720, margin: "20px 0 30px", lineHeight: 1.25 }}>{title}</h1>
      {children}
    </div>
  );
}
function JoinBand({ setPage }) {
  return (
    <div style={{ background: `linear-gradient(200deg, ${INK2} 0%, #101216 100%)`, textAlign: "center" }}>
      <div style={{ maxWidth: 640, margin: "0 auto", padding: "90px 28px" }}>
        <Eyebrow dark>Bring This to Your Company</Eyebrow>
        <h2 className="pb-serif" style={{ fontSize: "clamp(24px, 4vw, 34px)", fontWeight: 700, color: WHITE, margin: "20px 0 0", lineHeight: 1.2 }}>What would it look like if your leadership team actually finished something together?</h2>
        <button onClick={() => setPage("companies")} className="pb-btn pb-label" style={{ marginTop: 30, background: BRONZE, color: WHITE, border: "none", borderRadius: 28, padding: "16px 36px", fontSize: 12.5, fontWeight: 700, cursor: "pointer" }}>For Companies</button>
      </div>
    </div>
  );
}

export default function PurposeBuiltBusinessSite() {
  const [page, setPage] = useState("home");
  const [menuOpen, setMenuOpen] = useState(false);
  const [scrolled, setScrolled] = useState(false);
  useEffect(() => { const f = () => setScrolled(window.scrollY > 24); window.addEventListener("scroll", f); return () => window.removeEventListener("scroll", f); }, []);
  useEffect(() => { window.scrollTo(0, 0); }, [page]);
  return (
    <div className="pb-root">
      <style>{FONTS}</style>
      <HeaderNav page={page} setPage={setPage} menuOpen={menuOpen} setMenuOpen={setMenuOpen} scrolled={scrolled} />
      {page === "home" && <HomePage setPage={setPage} />}
      {page === "campaigns" && <CampaignsPage />}
      {page === "companies" && <CompaniesPage setPage={setPage} />}
      {page === "leaders" && <LeadersPage setPage={setPage} />}
      {page === "assessment" && <AssessmentPage setPage={setPage} />}
      {page === "about" && <AboutPage />}
      <FooterNav page={page} setPage={setPage} />
    </div>
  );
}
