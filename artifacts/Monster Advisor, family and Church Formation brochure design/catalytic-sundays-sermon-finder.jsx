import React, { useState } from "react";

const NAVY = "#101E38";
const NAVY2 = "#16274A";
const GOLD = "#B98D3E";
const GOLD_BRIGHT = "#D9B876";
const WHITE = "#FBF8F1";
const CREAM = "#F1EBDD";
const INK = "#1C2230";
const SLATE = "#767E8E";
const LINE = "#DCD4C0";

const FONTS = `
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,600;0,700;0,900;1,500;1,600&family=Archivo:wght@500;600;700&family=Inter:wght@400;500;600;700&display=swap');
* { box-sizing: border-box; }
body { margin: 0; }
.cs-root { font-family: 'Inter', sans-serif; color: ${INK}; background: ${WHITE}; min-height: 100vh; }
.cs-serif { font-family: 'Playfair Display', serif; }
.cs-label { font-family: 'Archivo', sans-serif; letter-spacing: 0.12em; text-transform: uppercase; }
.cs-input { font-family:'Inter'; font-size:13px; padding:11px 14px; border:1px solid ${LINE}; border-radius:8px; outline:none; background:${WHITE}; }
.cs-input:focus { border-color:${GOLD}; }
.cs-chip { font-family:'Archivo'; font-weight:600; font-size:10px; letter-spacing:0.04em; padding:7px 13px; border-radius:16px; cursor:pointer; border:1.5px solid ${LINE}; background:${WHITE}; color:${INK}; transition: all .15s ease; }
.cs-chip.active { border-color:${NAVY}; background:${NAVY}; color:${WHITE}; }
.cs-card { transition: transform .3s ease, border-color .3s ease; }
.cs-card:hover { transform: translateY(-3px); border-color: ${GOLD} !important; }
.cs-fade { animation: csFade .4s ease both; }
@keyframes csFade { from { opacity:0; transform:translateY(6px);} to {opacity:1; transform:translateY(0);} }
::selection { background: ${GOLD}; color: ${WHITE}; }
`;

const CATEGORIES = [
  { name: "Salvation & Response", items: [
    ["The Sunday You Say Yes", "Altar call, decision Sunday"],
    ["One Decision", "Altar call, new believers"],
    ["The Invitation", "Outreach, evangelism"],
    ["Today Is the Day", "Urgency, decision Sunday"],
    ["Coming Home", "Prodigal, outreach"],
    ["The Door Is Open", "Invite Sunday, outreach"],
    ["No More Waiting", "Decision Sunday"],
    ["Cross the Line", "Response, commitment"],
    ["Your Moment", "Altar call"],
  ]},
  { name: "Baptism Sunday", items: [
    ["Going Under, Coming Up New", "Baptism Sunday"],
    ["The Public Yes", "Baptism Sunday"],
    ["Buried and Raised", "Baptism Sunday, Romans 6"],
    ["Your Story, Told in Water", "Baptism testimonies"],
    ["The Sunday You Declare It", "Baptism Sunday"],
  ]},
  { name: "Vision & Future", items: [
    ["The Sunday We Say Where We're Going", "Vision Sunday, annual kickoff"],
    ["One Church, One Future", "Vision Sunday"],
    ["Vision Sunday", "Annual vision cast"],
    ["What We're Building Together", "Vision, capital campaign lead-in"],
    ["The Next Chapter Starts Today", "New season, vision"],
  ]},
  { name: "Generosity & Commitment", items: [
    ["The Sunday We Give", "Commitment Sunday"],
    ["Commitment Sunday", "Pledge Sunday, generosity"],
    ["What Faith Costs", "Sacrificial giving"],
    ["The Pledge", "Capital campaign commitment"],
    ["Beyond Comfortable", "Generosity, stretch giving"],
  ]},
  { name: "Outreach & Invite", items: [
    ["The Sunday to Bring Someone", "Invite Sunday"],
    ["He Is Risen", "Easter Sunday"],
    ["The Reason for the Season", "Christmas Sunday"],
    ["Come As You Are", "Outreach, seeker-friendly"],
    ["The Empty Seat, Filled", "Invite Sunday"],
  ]},
  { name: "Courage & Breakthrough", items: [
    ["The Sunday Fear Loses", "Courage, breakthrough"],
    ["Breakthrough", "Breakthrough Sunday"],
    ["The Wall Comes Down", "Breakthrough, Jericho theme"],
    ["Step Out", "Faith, courage"],
    ["Your Red Sea Moment", "Breakthrough, Exodus theme"],
  ]},
  { name: "Healing & Restoration", items: [
    ["The Sunday You're Made Whole", "Healing Sunday"],
    ["Restoration Sunday", "Healing, restoration"],
    ["What Was Broken", "Healing, testimony"],
    ["The Healing Line", "Prayer for healing service"],
    ["New Again", "Restoration"],
  ]},
  { name: "New Beginnings", items: [
    ["The Sunday You Start Over", "New Year Sunday"],
    ["A Clean Page", "New Year"],
    ["New Year, New You, Same God", "New Year kickoff"],
    ["The Reset", "New Year, new season"],
    ["Day One", "New Year, new beginnings"],
  ]},
  { name: "Capital Campaign Kickoff", items: [
    ["The Sunday We Build", "Capital campaign kickoff"],
    ["Bigger Than Us", "Capital campaign vision"],
    ["The Ground We're Standing On", "Building/relocation campaign"],
    ["What We Leave the Next Generation", "Capital campaign, legacy"],
    ["Kickoff Sunday", "Capital campaign launch"],
  ]},
  { name: "Membership & Belonging", items: [
    ["The Sunday You Belong", "Membership Sunday"],
    ["Welcome Home", "New member Sunday"],
    ["One Family", "Membership, belonging"],
    ["The Sunday You're Officially In", "Membership class kickoff"],
    ["Rooted Here", "Membership, commitment"],
  ]},
  { name: "Volunteer & Serve", items: [
    ["The Sunday You Step Up", "Volunteer recruitment"],
    ["Every Seat, a Server", "Serve team recruitment"],
    ["Find Your Place", "Spiritual gifts, serving"],
    ["The Sunday We All Serve", "Serve Sunday, community outreach"],
    ["Your Part to Play", "Volunteer Sunday"],
  ]},
  { name: "Prayer & Revival", items: [
    ["The Sunday Everything Changes", "Revival Sunday"],
    ["Revival Starts Here", "Revival kickoff"],
    ["On Our Knees", "Prayer Sunday"],
    ["The Sunday We Seek First", "Prayer, revival"],
    ["Fire Falls", "Revival, Pentecost theme"],
  ]},
];
const TOTAL = CATEGORIES.reduce((sum, c) => sum + c.items.length, 0);

function Eyebrow({ children }) {
  return <div className="cs-label" style={{ fontSize: 10.5, color: GOLD, display: "flex", alignItems: "center", gap: 8, marginBottom: 6 }}>
    <span style={{ width: 20, height: 2, background: GOLD, display: "inline-block" }} />{children}
  </div>;
}

export default function CatalyticSundaysFinder() {
  const [query, setQuery] = useState("");
  const [cat, setCat] = useState("All Categories");
  const catNames = ["All Categories", ...CATEGORIES.map((c) => c.name)];

  const filtered = CATEGORIES
    .filter((c) => cat === "All Categories" || c.name === cat)
    .map((c) => ({
      ...c,
      items: c.items.filter(([title, use]) => {
        const q = query.toLowerCase();
        return !q || title.toLowerCase().includes(q) || use.toLowerCase().includes(q) || c.name.toLowerCase().includes(q);
      }),
    }))
    .filter((c) => c.items.length > 0);
  const resultCount = filtered.reduce((sum, c) => sum + c.items.length, 0);

  return (
    <div className="cs-root">
      <style>{FONTS}</style>

      <div style={{ background: `linear-gradient(165deg, ${NAVY} 0%, #0E1930 100%)` }}>
        <div style={{ maxWidth: 900, margin: "0 auto", padding: "60px 28px 46px" }}>
          <div className="cs-label" style={{ fontSize: 10.5, color: GOLD_BRIGHT, display: "flex", alignItems: "center", gap: 8, marginBottom: 20 }}>
            <span style={{ width: 20, height: 2, background: GOLD_BRIGHT, display: "inline-block" }} />THE FIFTH FORMAT
          </div>
          <h1 className="cs-serif" style={{ fontSize: "clamp(26px, 4.5vw, 38px)", fontWeight: 700, color: WHITE, lineHeight: 1.15, margin: 0 }}>
            Catalytic Sundays — the Sermon Finder
          </h1>
          <p className="cs-serif" style={{ fontStyle: "italic", fontWeight: 500, fontSize: 15.5, color: GOLD_BRIGHT, marginTop: 16, lineHeight: 1.5, maxWidth: 560 }}>
            One Sunday. One decisive moment. {TOTAL} titles across {CATEGORIES.length} categories — search by title, use case, or theme.
          </p>
          <div style={{ display: "flex", gap: 10, marginTop: 30, flexWrap: "wrap" }}>
            <input
              className="cs-input"
              style={{ flex: "1 1 260px", background: "rgba(255,255,255,0.06)", borderColor: "rgba(217,184,118,0.35)", color: WHITE }}
              placeholder="Search titles, occasions, themes..."
              value={query}
              onChange={(e) => setQuery(e.target.value)}
            />
          </div>
        </div>
      </div>

      <div style={{ maxWidth: 900, margin: "0 auto", padding: "34px 28px 90px" }}>
        <div style={{ display: "flex", flexWrap: "wrap", gap: 8, marginBottom: 10 }}>
          {catNames.map((c) => (
            <button key={c} onClick={() => setCat(c)} className={`cs-chip${cat === c ? " active" : ""}`}>
              {c}
            </button>
          ))}
        </div>
        <div className="cs-label" style={{ fontSize: 10, color: SLATE, marginBottom: 24 }}>
          {resultCount} matching title{resultCount === 1 ? "" : "s"}
        </div>

        {filtered.map((c) => (
          <div key={c.name} className="cs-fade" style={{ marginBottom: 30 }}>
            <div className="cs-serif" style={{ fontWeight: 700, fontSize: 16, color: NAVY, marginBottom: 12 }}>{c.name}</div>
            <div style={{ display: "grid", gridTemplateColumns: "repeat(auto-fit, minmax(240px, 1fr))", gap: 12 }}>
              {c.items.map(([title, use]) => (
                <div key={title} className="cs-card" style={{ border: `1px solid ${LINE}`, borderRadius: 6, padding: "16px 18px", background: CREAM }}>
                  <div className="cs-serif" style={{ fontWeight: 700, fontSize: 14, color: NAVY, marginBottom: 6, lineHeight: 1.3 }}>{title}</div>
                  <div className="cs-label" style={{ fontSize: 9, color: GOLD }}>{use}</div>
                </div>
              ))}
            </div>
          </div>
        ))}

        {resultCount === 0 && (
          <div style={{ textAlign: "center", padding: "50px 20px", color: SLATE, fontSize: 14 }}>
            No titles match that search.
          </div>
        )}

        <div style={{ marginTop: 30, background: NAVY, borderRadius: 6, padding: "22px 24px" }}>
          <div className="cs-label" style={{ fontSize: 9.5, color: GOLD_BRIGHT, marginBottom: 8 }}>What a Catalytic Sunday is</div>
          <p style={{ fontSize: 12.5, color: "rgba(251,248,241,0.85)", lineHeight: 1.6, margin: 0 }}>
            The shortest format in the ladder — one message, built for maximum immediate response, not a multi-day arc. Where a 40-Day campaign builds conviction over six weeks, a Catalytic Sunday is the single decisive moment: an altar call, a baptism service, a capital campaign kickoff, a vision Sunday.
          </p>
        </div>
      </div>
    </div>
  );
}
