import React, { useState, useEffect } from "react";

const INK = "#191A16";
const INK2 = "#23241E";
const COPPER = "#BE6A32";
const COPPER_BRIGHT = "#E08A50";
const CREAM = "#FAF6EF";
const WHITE = "#FFFDF9";
const TXT = "#211F1A";
const SLATE = "#736F63";
const LINE = "#E3DCCC";

const FONTS = `
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,600;0,700;0,900;1,500;1,600&family=Archivo:wght@500;600;700&family=Inter:wght@400;500;600;700&display=swap');
* { box-sizing: border-box; }
body { margin: 0; }
.gc-root { font-family: 'Inter', sans-serif; color: ${TXT}; background: ${WHITE}; }
.gc-serif { font-family: 'Playfair Display', serif; }
.gc-label { font-family: 'Archivo', sans-serif; letter-spacing: 0.14em; text-transform: uppercase; }
.gc-eyebrow { display:flex; align-items:center; gap:10px; font-family:'Archivo',sans-serif; font-weight:600; font-size:12px; letter-spacing:0.18em; text-transform:uppercase; color:${COPPER}; }
.gc-eyebrow::before { content:''; width:26px; height:2px; background:${COPPER}; display:inline-block; }
.gc-eyebrow.on-dark { color:${COPPER_BRIGHT}; }
.gc-eyebrow.on-dark::before { background:${COPPER_BRIGHT}; }
.gc-nav-link { position:relative; background:none; border:none; cursor:pointer; font-family:'Archivo'; }
.gc-nav-link::after { content:''; position:absolute; left:0; right:0; bottom:-6px; height:1.5px; background:${COPPER_BRIGHT}; transform:scaleX(0); transition:transform .25s ease; }
.gc-nav-link:hover::after { transform:scaleX(1); }
.gc-nav-link.active::after { transform:scaleX(1); background:${COPPER}; }
.gc-card { transition: transform .35s cubic-bezier(.2,.7,.3,1), border-color .3s ease; }
.gc-card:hover { transform: translateY(-3px); }
.gc-btn { transition: background .2s ease, color .2s ease, transform .2s ease; }
.gc-btn:hover { transform: translateY(-1px); }
.gc-fade-in { animation: gcFadeIn .5s ease both; }
@keyframes gcFadeIn { from { opacity:0; transform:translateY(8px);} to {opacity:1; transform:translateY(0);} }
.gc-footer-link { background:none; border:none; cursor:pointer; text-align:left; padding:0; }
.gc-desktop-only { display: none; }
@media (min-width: 900px) { .gc-desktop-only { display: flex !important; } }
.gc-mobile-only { display: inline-block; }
@media (min-width: 900px) { .gc-mobile-only { display: none !important; } }
::selection { background: ${COPPER}; color: ${WHITE}; }
`;

const PAGES = [
  { id: "home", label: "Home" },
  { id: "formula", label: "The Formula" },
  { id: "elements", label: "The Elements" },
  { id: "campaigns", label: "Campaigns" },
  { id: "churches", label: "For Churches" },
  { id: "advisors", label: "For Advisors" },
  { id: "assessment", label: "Assessment" },
  { id: "about", label: "About" },
];
function pageLabel(id) { const p = PAGES.find((p) => p.id === id); return p ? p.label : id; }

const ELEMENTS = [
  { symbol: "Gt", name: "Gratitude", desc: "The reaction always starts here. Neuroscience confirms what Paul figured out in a prison cell — gratitude shifts the chemistry before generosity ever begins." },
  { symbol: "Tr", name: "Trust", desc: "What does money protect you from? What does it promise you that only God can actually deliver? Generosity that lasts is built on trust, not obligation." },
  { symbol: "Hb", name: "Habit", desc: "One decision doesn't change a family. A rhythm does. The daily and weekly practices that make generosity a reflex instead of an event." },
  { symbol: "Dv", name: "Donor-Advised Funds", desc: "A structured giving vehicle that lets high-capacity families and business owners give strategically, across years, with real tax and legacy benefits." },
  { symbol: "Cl", name: "Charitable LLCs", desc: "For business owners ready to connect the success of the company directly to Kingdom generosity at scale." },
  { symbol: "Fg", name: "Family Giving Plans", desc: "A shared decision-making framework so generosity becomes a family conversation and a family value, not one person's private decision." },
  { symbol: "Lg", name: "Legacy Giving", desc: "Generosity that continues after a family is gone — the giving decisions embedded into a will, a trust, or a foundation." },
  { symbol: "Ex", name: "Exit Giving", desc: "The moment a business is sold is one of the single largest generosity opportunities a family will ever have — and one of the most overlooked." },
];

const CAMPAIGNS = [
  { title: "40 Days of Generosity", tag: "YEAR-END BRIDGE · STEWARDSHIP LAUNCH", desc: "The most strategically positioned fall stewardship title — fall naturally flows into year-end giving, and this campaign creates the spiritual foundation that makes the giving invitation feel like a natural conclusion, not a financial ask." },
  { title: "40 Days of Enough", tag: "MOST COUNTERCULTURAL · DEEPEST WORK", desc: "The family willing to ask \u201cwhat is enough, and what comes after enough\u201d is ready for the deepest generosity work. Changes the conversation from accumulation to distribution." },
  { title: "Seven Days of Generosity That Scales", tag: "HIGH-CAPACITY GIVING · THE SIGNATRY · DAF", desc: "Connects business success to kingdom generosity at scale — donor-advised funds, charitable LLCs, and business exits as giving opportunities." },
  { title: "Seven Days of Abundance", tag: "SCARCITY TO KINGDOM ABUNDANCE", desc: "Moves people from scarcity thinking to kingdom abundance in every dimension of daily life — not prosperity theology, but a quality of life circumstances can't produce or destroy." },
];

function Eyebrow({ children, dark }) { return <div className={`gc-eyebrow${dark ? " on-dark" : ""}`}>{children}</div>; }

function HeaderNav({ page, setPage, menuOpen, setMenuOpen, scrolled }) {
  return (
    <div style={{ position: "sticky", top: 0, zIndex: 50, background: scrolled || page !== "home" ? "rgba(25,26,22,0.97)" : "transparent", borderBottom: `1px solid rgba(190,106,50,0.25)`, backdropFilter: "blur(6px)", transition: "background .3s ease" }}>
      <div style={{ maxWidth: 1200, margin: "0 auto", padding: "18px 28px", display: "flex", alignItems: "center", justifyContent: "space-between" }}>
        <button onClick={() => setPage("home")} className="gc-serif" style={{ background: "none", border: "none", cursor: "pointer", fontWeight: 700, fontSize: 16.5, color: WHITE }}>Generosity Chemistry<span style={{ fontSize: 10, verticalAlign: "super" }}>™</span></button>
        <div className="gc-desktop-only" style={{ gap: 20 }}>
          {PAGES.filter((p) => p.id !== "home").map((p) => (
            <button key={p.id} onClick={() => setPage(p.id)} className={`gc-nav-link gc-label${page === p.id ? " active" : ""}`} style={{ fontSize: 10.5, fontWeight: 600, color: page === p.id ? COPPER_BRIGHT : "rgba(255,253,249,0.85)" }}>{p.label}</button>
          ))}
        </div>
        <button onClick={() => setPage("churches")} className="gc-btn gc-label gc-desktop-only" style={{ background: COPPER, color: WHITE, border: "none", borderRadius: 22, padding: "9px 18px", fontSize: 10.5, fontWeight: 700, cursor: "pointer" }}>Start the Reaction</button>
        <button onClick={() => setMenuOpen((v) => !v)} className="gc-mobile-only" style={{ background: "none", border: `1px solid rgba(190,106,50,0.5)`, borderRadius: 8, padding: "8px 12px", color: COPPER_BRIGHT, cursor: "pointer", fontSize: 13 }}>{menuOpen ? "Close" : "Menu"}</button>
      </div>
      {menuOpen && (
        <div style={{ background: INK, borderTop: `1px solid rgba(190,106,50,0.25)`, padding: "8px 28px 24px" }}>
          {PAGES.map((p) => (
            <div key={p.id} onClick={() => { setPage(p.id); setMenuOpen(false); }} className="gc-label" style={{ padding: "12px 0", borderBottom: "1px solid rgba(190,106,50,0.2)", color: page === p.id ? COPPER_BRIGHT : "rgba(255,253,249,0.9)", fontSize: 12, cursor: "pointer" }}>{p.label}</div>
          ))}
          <div onClick={() => { setPage("churches"); setMenuOpen(false); }} className="gc-label" style={{ marginTop: 16, background: COPPER, color: WHITE, textAlign: "center", padding: "12px 0", borderRadius: 24, fontSize: 12, fontWeight: 700, cursor: "pointer" }}>Start the Reaction</div>
        </div>
      )}
    </div>
  );
}

function FooterNav({ page, setPage }) {
  return (
    <div style={{ background: INK, borderTop: "1px solid rgba(190,106,50,0.2)" }}>
      <div style={{ maxWidth: 1200, margin: "0 auto", padding: "50px 28px 30px", display: "grid", gridTemplateColumns: "1.3fr 1fr 1fr", gap: 36 }}>
        <div>
          <div className="gc-serif" style={{ fontWeight: 700, fontSize: 16, color: WHITE, marginBottom: 12 }}>Generosity Chemistry<span style={{ fontSize: 9, verticalAlign: "super" }}>™</span></div>
          <p style={{ fontSize: 12.5, color: "rgba(255,253,249,0.6)", lineHeight: 1.6, maxWidth: 260 }}>The reaction that happens when gratitude, trust, and habit meet a family's resources — a Lifetogether platform.</p>
        </div>
        <div>
          <div className="gc-label" style={{ fontSize: 10, color: COPPER_BRIGHT, marginBottom: 14 }}>Platform</div>
          {PAGES.filter((p) => p.id !== "home").map((p) => (
            <button key={p.id} onClick={() => setPage(p.id)} className="gc-footer-link" style={{ display: "block", fontSize: 12.5, color: page === p.id ? COPPER_BRIGHT : "rgba(255,253,249,0.72)", padding: "5px 0", cursor: "pointer" }}>{p.label}</button>
          ))}
        </div>
        <div>
          <div className="gc-label" style={{ fontSize: 10, color: COPPER_BRIGHT, marginBottom: 14 }}>Legal</div>
          {["Privacy Policy", "Terms of Use"].map((u) => <div key={u} style={{ fontSize: 12.5, color: "rgba(255,253,249,0.4)", padding: "5px 0" }}>{u} <span style={{ fontStyle: "italic" }}>(coming soon)</span></div>)}
        </div>
      </div>
      <div style={{ maxWidth: 1200, margin: "0 auto", padding: "18px 28px", borderTop: "1px solid rgba(190,106,50,0.15)", display: "flex", justifyContent: "space-between", flexWrap: "wrap", gap: 12 }}>
        <div className="gc-label" style={{ fontSize: 9.5, color: "rgba(255,253,249,0.45)" }}>GENEROSITYCHEMISTRY.COM · A LIFETOGETHER PLATFORM</div>
        <div className="gc-label" style={{ fontSize: 9.5, color: "rgba(255,253,249,0.45)" }}>DRAFT PREVIEW · NOT YET LIVE</div>
      </div>
    </div>
  );
}

function HomePage({ setPage }) {
  const explore = [
    { id: "formula", label: "The Formula", desc: "It doesn't begin with giving. It begins with the heart." },
    { id: "elements", label: "The Elements", desc: "Eight building blocks of generosity that lasts." },
    { id: "campaigns", label: "Campaigns", desc: "40 and 7-day journeys that start the reaction." },
    { id: "churches", label: "For Churches", desc: "Run a generosity campaign that doesn't feel like a fundraiser." },
    { id: "advisors", label: "For Advisors", desc: "Bring structured giving into client conversations." },
  ];
  return (
    <div className="gc-fade-in">
      <div style={{ position: "relative", background: `linear-gradient(165deg, ${INK} 0%, #0F100D 100%)`, overflow: "hidden" }}>
        <div style={{ position: "absolute", inset: 0, opacity: 0.55, backgroundImage: `radial-gradient(circle at 78% 18%, rgba(190,106,50,0.18), transparent 45%)` }} />
        <div style={{ maxWidth: 1200, margin: "0 auto", padding: "88px 28px 90px", position: "relative" }}>
          <div style={{ maxWidth: 700 }}>
            <Eyebrow dark>The Science of a Generous Life</Eyebrow>
            <h1 className="gc-serif" style={{ fontSize: "clamp(30px, 5vw, 48px)", lineHeight: 1.1, fontWeight: 700, color: WHITE, margin: "26px 0 0" }}>Generosity isn't a giving decision. It's a reaction.</h1>
            <p className="gc-serif" style={{ fontStyle: "italic", fontWeight: 500, fontSize: 17.5, color: COPPER_BRIGHT, marginTop: 24, lineHeight: 1.5, maxWidth: 560 }}>Gratitude, trust, and habit — combined — produce something scarcity thinking never could.</p>
            <div style={{ display: "flex", gap: 16, marginTop: 38, flexWrap: "wrap" }}>
              <button onClick={() => setPage("formula")} className="gc-btn gc-label" style={{ background: COPPER, color: WHITE, border: "none", borderRadius: 26, padding: "15px 30px", fontSize: 12, fontWeight: 700, cursor: "pointer" }}>See the Formula</button>
              <button onClick={() => setPage("campaigns")} className="gc-label" style={{ background: "transparent", color: WHITE, border: "1px solid rgba(255,253,249,0.35)", borderRadius: 26, padding: "15px 30px", fontSize: 12, fontWeight: 700, cursor: "pointer" }}>Browse Campaigns</button>
            </div>
          </div>
        </div>
      </div>

      <div style={{ maxWidth: 1200, margin: "0 auto", padding: "90px 28px" }}>
        <Eyebrow>Explore the Platform</Eyebrow>
        <h2 className="gc-serif" style={{ fontSize: "clamp(22px, 3vw, 28px)", fontWeight: 700, color: INK, margin: "20px 0 44px" }}>Where to start.</h2>
        <div style={{ display: "grid", gridTemplateColumns: "repeat(auto-fit, minmax(260px, 1fr))", gap: 22 }}>
          {explore.map((e) => (
            <div key={e.id} onClick={() => setPage(e.id)} className="gc-card" style={{ border: `1px solid ${LINE}`, borderRadius: 4, padding: "26px 24px", background: CREAM, cursor: "pointer" }}>
              <div className="gc-serif" style={{ fontWeight: 700, fontSize: 16.5, color: INK, marginBottom: 8, lineHeight: 1.3 }}>{e.label}</div>
              <div style={{ fontSize: 13, color: SLATE, lineHeight: 1.55, marginBottom: 14 }}>{e.desc}</div>
              <div className="gc-label" style={{ fontSize: 10.5, color: COPPER, fontWeight: 700 }}>Explore &rarr;</div>
            </div>
          ))}
        </div>
      </div>
      <JoinBand setPage={setPage} />
    </div>
  );
}

function FormulaPage() {
  return (
    <PageShell eyebrow="The Formula" title="It doesn't begin with giving. It begins with the heart.">
      <p style={{ color: SLATE, fontSize: 14.5, lineHeight: 1.75, maxWidth: 660, marginBottom: 34 }}>
        What does money mean to you? What does it protect you from? What does it promise you that only God can actually deliver? When a family works through those questions honestly, generosity becomes a natural overflow rather than an obligated response.
      </p>
      <div style={{ display: "flex", alignItems: "center", justifyContent: "center", gap: 18, flexWrap: "wrap", background: CREAM, borderRadius: 4, padding: "40px 24px", marginBottom: 40 }}>
        {["Gratitude", "+", "Trust", "+", "Habit", "=", "Generosity"].map((w, i) => (
          <div key={i} className={w === "+" || w === "=" ? "gc-serif" : "gc-serif"} style={{ fontSize: w === "+" || w === "=" ? 24 : 20, fontWeight: 700, color: w === "+" || w === "=" ? COPPER : INK }}>{w}</div>
        ))}
      </div>
      <p style={{ color: SLATE, fontSize: 13.5, lineHeight: 1.7, maxWidth: 640 }}>
        Every element on the next page is a way to strengthen one part of this equation — for a family, a business owner, or a congregation working through what generosity actually costs, and what it actually produces.
      </p>
    </PageShell>
  );
}

function ElementsPage() {
  const [open, setOpen] = useState(null);
  return (
    <PageShell eyebrow="The Elements" title="Eight building blocks of generosity that lasts.">
      <div style={{ display: "grid", gridTemplateColumns: "repeat(auto-fit, minmax(220px, 1fr))", gap: 16 }}>
        {ELEMENTS.map((el) => {
          const isOpen = open === el.symbol;
          return (
            <div key={el.symbol} onClick={() => setOpen(isOpen ? null : el.symbol)} className="gc-card" style={{ border: `2px solid ${isOpen ? COPPER : LINE}`, borderRadius: 6, padding: "20px 18px", cursor: "pointer", background: WHITE }}>
              <div style={{ display: "flex", justifyContent: "space-between", alignItems: "flex-start" }}>
                <div className="gc-serif" style={{ fontSize: 26, fontWeight: 700, color: COPPER }}>{el.symbol}</div>
                <div className="gc-label" style={{ fontSize: 16, color: COPPER }}>{isOpen ? "\u2013" : "+"}</div>
              </div>
              <div className="gc-serif" style={{ fontWeight: 700, fontSize: 14.5, color: INK, marginTop: 10, marginBottom: isOpen ? 10 : 0 }}>{el.name}</div>
              {isOpen && <div className="gc-fade-in" style={{ fontSize: 12, color: SLATE, lineHeight: 1.55 }}>{el.desc}</div>}
            </div>
          );
        })}
      </div>
    </PageShell>
  );
}

function CampaignsPage({ setPage }) {
  return (
    <PageShell eyebrow="Campaigns" title="40 and 7-day journeys that start the reaction.">
      {CAMPAIGNS.map((c) => (
        <div key={c.title} style={{ borderTop: `1px solid ${LINE}`, padding: "22px 0" }}>
          <div className="gc-serif" style={{ fontWeight: 700, fontSize: 17, color: INK, marginBottom: 5 }}>{c.title}</div>
          <div className="gc-label" style={{ fontSize: 9, color: COPPER, marginBottom: 8 }}>{c.tag}</div>
          <div style={{ fontSize: 13, color: SLATE, lineHeight: 1.6, maxWidth: 620 }}>{c.desc}</div>
        </div>
      ))}
      <div style={{ marginTop: 40, textAlign: "center", background: CREAM, borderRadius: 4, padding: "36px 24px" }}>
        <p style={{ fontSize: 13, color: SLATE, maxWidth: 440, margin: "0 auto 16px", lineHeight: 1.6 }}>Bring one of these campaigns to your church's next stewardship season.</p>
        <button onClick={() => setPage("churches")} className="gc-btn gc-label" style={{ background: COPPER, color: WHITE, border: "none", borderRadius: 22, padding: "11px 24px", fontSize: 10.5, fontWeight: 700, cursor: "pointer" }}>For Churches</button>
      </div>
    </PageShell>
  );
}

function ChurchesPage({ setPage }) {
  return (
    <PageShell eyebrow="For Churches" title="A generosity campaign that doesn't feel like a fundraiser.">
      <p style={{ color: SLATE, fontSize: 14.5, lineHeight: 1.75, maxWidth: 640, marginBottom: 30 }}>
        The key to a campaign that works is that it doesn't begin with giving. It begins with the heart — six weeks of teaching, small group discussion, and daily devotional reinforcement, working through what money means before ever asking for it.
      </p>
      <div className="gc-card" style={{ border: `1px solid ${LINE}`, borderRadius: 4, padding: "26px 24px", marginBottom: 20 }}>
        <div className="gc-label" style={{ fontSize: 9, color: COPPER, marginBottom: 8 }}>Best Season</div>
        <div className="gc-serif" style={{ fontWeight: 700, fontSize: 16, color: INK, marginBottom: 8 }}>Fall, as a Year-End Bridge</div>
        <p style={{ fontSize: 13, color: SLATE, lineHeight: 1.6 }}>Fall naturally flows into year-end giving — a generosity campaign creates the spiritual foundation that makes the giving invitation feel like the natural conclusion, not a financial ask.</p>
      </div>
      <button onClick={() => setPage("about")} className="gc-btn gc-label" style={{ background: COPPER, color: WHITE, border: "none", borderRadius: 22, padding: "12px 26px", fontSize: 11, fontWeight: 700, cursor: "pointer" }}>Start the Reaction</button>
    </PageShell>
  );
}

function AdvisorsPage({ setPage }) {
  return (
    <PageShell eyebrow="For Advisors" title="Bring structured giving into client conversations.">
      <p style={{ color: SLATE, fontSize: 14.5, lineHeight: 1.75, maxWidth: 640, marginBottom: 30 }}>
        Donor-advised funds, charitable LLCs, legacy giving, and exit giving all live in The Elements — the same tools Christian Advisor Network members already use, indexed here around the generosity conversation specifically.
      </p>
      <button onClick={() => setPage("elements")} className="gc-btn gc-label" style={{ background: COPPER, color: WHITE, border: "none", borderRadius: 22, padding: "12px 26px", fontSize: 11, fontWeight: 700, cursor: "pointer" }}>See the Elements</button>
    </PageShell>
  );
}

function AssessmentPage({ setPage }) {
  const [taken, setTaken] = useState(false);
  return (
    <PageShell eyebrow="Assessment" title="Generosity Capacity Assessment™">
      <p style={{ color: SLATE, fontSize: 14.5, lineHeight: 1.75, maxWidth: 620, marginBottom: 24 }}>Helps a family understand what they could give, and what's holding them back.</p>
      {taken ? (
        <div className="gc-fade-in gc-label" style={{ background: CREAM, borderRadius: 20, padding: "14px 0", textAlign: "center", fontSize: 11, fontWeight: 700, color: INK, maxWidth: 300 }}>&#10003; Started — check your email</div>
      ) : (
        <button onClick={() => setTaken(true)} className="gc-btn gc-label" style={{ background: COPPER, color: WHITE, border: "none", borderRadius: 22, padding: "12px 26px", fontSize: 11, fontWeight: 700, cursor: "pointer" }}>Take the Assessment</button>
      )}
    </PageShell>
  );
}

function AboutPage() {
  return (
    <PageShell eyebrow="About" title="A Lifetogether platform for the generosity conversation.">
      <p style={{ color: SLATE, fontSize: 14.5, lineHeight: 1.75, maxWidth: 640 }}>
        Built from twenty-five years of churchwide campaign experience, applied specifically to the conversation churches are often least equipped to lead well — money, trust, and what it means to have enough.
      </p>
    </PageShell>
  );
}

function PageShell({ eyebrow, title, children }) {
  return (
    <div className="gc-fade-in" style={{ maxWidth: 1200, margin: "0 auto", padding: "80px 28px 100px" }}>
      <Eyebrow>{eyebrow}</Eyebrow>
      <h1 className="gc-serif" style={{ fontSize: "clamp(24px, 3.4vw, 34px)", fontWeight: 700, color: INK, maxWidth: 720, margin: "20px 0 30px", lineHeight: 1.25 }}>{title}</h1>
      {children}
    </div>
  );
}
function JoinBand({ setPage }) {
  return (
    <div style={{ background: `linear-gradient(200deg, ${INK2} 0%, #0F100D 100%)`, textAlign: "center" }}>
      <div style={{ maxWidth: 640, margin: "0 auto", padding: "90px 28px" }}>
        <Eyebrow dark>Start the Reaction</Eyebrow>
        <h2 className="gc-serif" style={{ fontSize: "clamp(24px, 4vw, 34px)", fontWeight: 700, color: WHITE, margin: "20px 0 0", lineHeight: 1.2 }}>What does your family — or your congregation — actually believe about enough?</h2>
        <button onClick={() => setPage("churches")} className="gc-btn gc-label" style={{ marginTop: 30, background: COPPER, color: WHITE, border: "none", borderRadius: 28, padding: "16px 36px", fontSize: 12.5, fontWeight: 700, cursor: "pointer" }}>For Churches</button>
      </div>
    </div>
  );
}

export default function GenerosityChemistrySite() {
  const [page, setPage] = useState("home");
  const [menuOpen, setMenuOpen] = useState(false);
  const [scrolled, setScrolled] = useState(false);
  useEffect(() => { const f = () => setScrolled(window.scrollY > 24); window.addEventListener("scroll", f); return () => window.removeEventListener("scroll", f); }, []);
  useEffect(() => { window.scrollTo(0, 0); }, [page]);
  return (
    <div className="gc-root">
      <style>{FONTS}</style>
      <HeaderNav page={page} setPage={setPage} menuOpen={menuOpen} setMenuOpen={setMenuOpen} scrolled={scrolled} />
      {page === "home" && <HomePage setPage={setPage} />}
      {page === "formula" && <FormulaPage />}
      {page === "elements" && <ElementsPage />}
      {page === "campaigns" && <CampaignsPage setPage={setPage} />}
      {page === "churches" && <ChurchesPage setPage={setPage} />}
      {page === "advisors" && <AdvisorsPage setPage={setPage} />}
      {page === "assessment" && <AssessmentPage setPage={setPage} />}
      {page === "about" && <AboutPage />}
      <FooterNav page={page} setPage={setPage} />
    </div>
  );
}
