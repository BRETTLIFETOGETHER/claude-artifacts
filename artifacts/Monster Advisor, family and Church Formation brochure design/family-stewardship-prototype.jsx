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
const GREEN = "#3F7D5C";
const AMBER = "#C4791F";

const FONTS = `
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,600;0,700;0,900;1,500;1,600&family=Archivo:wght@500;600;700&family=Inter:wght@400;500;600;700&display=swap');
* { box-sizing: border-box; }
body { margin: 0; }
.sw-root { font-family: 'Inter', sans-serif; color: ${INK}; background: ${WHITE}; min-height: 100vh; }
.sw-serif { font-family: 'Playfair Display', serif; }
.sw-label { font-family: 'Archivo', sans-serif; letter-spacing: 0.12em; text-transform: uppercase; }
.sw-btn { transition: background .2s ease, color .2s ease, transform .15s ease; cursor: pointer; }
.sw-btn:hover { transform: translateY(-1px); }
.sw-fade { animation: swFade .4s ease both; }
@keyframes swFade { from { opacity:0; transform:translateY(6px);} to {opacity:1; transform:translateY(0);} }
.sw-tab { background:none; border:none; cursor:pointer; font-family:'Archivo'; font-weight:600; }
.sw-input { font-family:'Inter'; font-size:13px; padding:9px 12px; border:1px solid ${LINE}; border-radius:6px; outline:none; background:${WHITE}; }
.sw-input:focus { border-color:${GOLD}; }
.sw-card { border:1px solid ${LINE}; border-radius:6px; background:${WHITE}; }
::selection { background:${GOLD}; color:${WHITE}; }
`;

const TABS = [
  { id: "dashboard", label: "Dashboard" },
  { id: "familymap", label: "Family Map" },
  { id: "retention", label: "Retention" },
  { id: "relational", label: "Relational Bonds" },
  { id: "aum", label: "AUM Growth" },
  { id: "steward", label: "Successor & Steward" },
  { id: "business", label: "Family Business" },
  { id: "stories", label: "Stories" },
];

/* ---------- shared bits ---------- */
function Eyebrow({ children }) {
  return <div className="sw-label" style={{ fontSize: 10.5, color: GOLD, display: "flex", alignItems: "center", gap: 8, marginBottom: 14 }}>
    <span style={{ width: 20, height: 2, background: GOLD, display: "inline-block" }} />{children}
  </div>;
}
function ModuleShell({ eyebrow, title, subtitle, children }) {
  return (
    <div className="sw-fade" style={{ maxWidth: 980, margin: "0 auto", padding: "44px 32px 80px" }}>
      <Eyebrow>{eyebrow}</Eyebrow>
      <h1 className="sw-serif" style={{ fontSize: 26, fontWeight: 700, color: NAVY, marginBottom: 8 }}>{title}</h1>
      {subtitle && <p style={{ fontSize: 14, color: SLATE, lineHeight: 1.6, maxWidth: 640, marginBottom: 28 }}>{subtitle}</p>}
      {children}
    </div>
  );
}
function Field({ label, children }) {
  return <div style={{ marginBottom: 14 }}>
    <div className="sw-label" style={{ fontSize: 9.5, color: SLATE, marginBottom: 5 }}>{label}</div>
    {children}
  </div>;
}

/* =====================================================================
   DASHBOARD
===================================================================== */
function Dashboard({ setTab }) {
  const cards = [
    ["familymap", "Family Map", "Compare assessments across the family into one shared picture."],
    ["retention", "Retention", "Milestone tracking and the Next-Gen Bridge Journey."],
    ["relational", "Relational Bonds", "Meeting facilitator and multi-generational calendar."],
    ["aum", "AUM Growth", "Complete Financial Picture and Business Exit Readiness."],
    ["steward", "Successor & Steward Journey", "Covey-sequenced, built on the 17 Flourishing dimensions."],
    ["business", "Family Business", "Governance, roles, and readiness."],
    ["stories", "Stories", "Legacy, history, and value-based stories for the next generation."],
  ];
  return (
    <ModuleShell eyebrow="Family Stewardship Command Center" title="Seven modules. One family journey." subtitle="A live, interactive prototype — pick any module below.">
      <div style={{ display: "grid", gridTemplateColumns: "repeat(auto-fit, minmax(260px, 1fr))", gap: 16 }}>
        {cards.map(([id, t, d]) => (
          <div key={id} onClick={() => setTab(id)} className="sw-card sw-btn" style={{ padding: "22px 20px", background: CREAM }}>
            <div className="sw-serif" style={{ fontWeight: 700, fontSize: 16, color: NAVY, marginBottom: 6 }}>{t}</div>
            <div style={{ fontSize: 12.5, color: SLATE, lineHeight: 1.5, marginBottom: 12 }}>{d}</div>
            <div className="sw-label" style={{ fontSize: 10, color: GOLD, fontWeight: 700 }}>Open &rarr;</div>
          </div>
        ))}
      </div>
    </ModuleShell>
  );
}

/* =====================================================================
   FAMILY MAP
===================================================================== */
const MAP_DIMENSIONS = ["Faith", "Family", "Finances", "Purpose", "Communication", "Generosity"];
function FamilyMap() {
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
    <ModuleShell eyebrow="Family Map" title="Compare assessments into one shared picture." subtitle="Enter scores (1–10) for two family members, then generate the map. Divergences of 3+ points get a suggested conversation starter.">
      <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: 24, marginBottom: 24 }}>
        {[["a", a, setA], ["b", b, setB]].map(([key, state, setState]) => (
          <div key={key} className="sw-card" style={{ padding: 20 }}>
            <input className="sw-input" style={{ width: "100%", marginBottom: 14, fontWeight: 700 }} value={names[key]}
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
      <button onClick={() => setGenerated(true)} className="sw-btn sw-label" style={{ background: GOLD, color: WHITE, border: "none", borderRadius: 22, padding: "12px 26px", fontSize: 11, fontWeight: 700 }}>Generate Map</button>

      {generated && (
        <div className="sw-fade" style={{ marginTop: 28 }}>
          {MAP_DIMENSIONS.map((d) => {
            const diff = Math.abs(a[d] - b[d]);
            const diverge = diff >= 3;
            return (
              <div key={d} style={{ borderTop: `1px solid ${LINE}`, padding: "14px 0" }}>
                <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center", marginBottom: 6 }}>
                  <span className="sw-serif" style={{ fontWeight: 700, fontSize: 14 }}>{d}</span>
                  {diverge && <span className="sw-label" style={{ fontSize: 9, color: AMBER, border: `1px solid ${AMBER}`, borderRadius: 10, padding: "2px 8px" }}>Divergence</span>}
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

/* =====================================================================
   RETENTION — Milestone Tracker + Next-Gen Bridge
===================================================================== */
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

function Retention() {
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
    <ModuleShell eyebrow="Retention" title="Milestone Tracker & the Next-Gen Bridge Journey" subtitle="Track the moments most likely to trigger a switch — and build the relationship with the next generation before any wealth transfers.">
      <div className="sw-card" style={{ padding: 22, marginBottom: 30 }}>
        <div className="sw-serif" style={{ fontWeight: 700, fontSize: 16, marginBottom: 14 }}>Milestone & Trigger Event Tracker</div>
        <div style={{ display: "flex", gap: 10, flexWrap: "wrap", marginBottom: 16 }}>
          <input className="sw-input" placeholder="Milestone name" value={form.name} onChange={(e) => setForm((f) => ({ ...f, name: e.target.value }))} style={{ flex: "1 1 200px" }} />
          <select className="sw-input" value={form.type} onChange={(e) => setForm((f) => ({ ...f, type: e.target.value }))} style={{ flex: "1 1 160px" }}>
            {MILESTONE_TYPES.map((t) => <option key={t}>{t}</option>)}
          </select>
          <input className="sw-input" type="date" value={form.date} onChange={(e) => setForm((f) => ({ ...f, date: e.target.value }))} style={{ flex: "1 1 160px" }} />
          <button onClick={addMilestone} className="sw-btn sw-label" style={{ background: NAVY, color: WHITE, border: "none", borderRadius: 6, padding: "9px 18px", fontSize: 11, fontWeight: 700 }}>Add</button>
        </div>
        {milestones.map((m, i) => (
          <div key={i} style={{ borderTop: `1px solid ${LINE}`, padding: "12px 0" }}>
            <div style={{ display: "flex", justifyContent: "space-between" }}>
              <span style={{ fontWeight: 600, fontSize: 13.5 }}>{m.name}</span>
              <span className="sw-label" style={{ fontSize: 9.5, color: GOLD }}>{m.type} &middot; {m.date}</span>
            </div>
            <div style={{ fontSize: 12, color: SLATE, marginTop: 4, fontStyle: "italic" }}>Suggested: {OUTREACH[m.type]}</div>
          </div>
        ))}
      </div>

      <div className="sw-card" style={{ padding: 22 }}>
        <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center", marginBottom: 16 }}>
          <div className="sw-serif" style={{ fontWeight: 700, fontSize: 16 }}>The Next-Gen Bridge Journey</div>
          <span className="sw-label" style={{ fontSize: 10, color: GOLD }}>{completedCount}/5 stages</span>
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

/* =====================================================================
   RELATIONAL BONDS — Meeting Facilitator + Multi-Gen Calendar
===================================================================== */
const MEETING_TYPES = {
  "Annual Family Meeting": ["What went well this year as a family?", "What's one thing we should stop doing?", "What's our shared priority for next year?", "Who needs more support from the rest of us right now?"],
  "Values Conversation": ["What value did our parents/grandparents model best?", "What value do we want to be known for in twenty years?", "Where have we drifted from what we say we believe?"],
  "Business Update": ["What's the state of the business in plain language?", "What decision is coming that affects the family?", "Where do we need more transparency?"],
  "Generosity Planning": ["What causes matter most to each of us right now?", "Should we give individually or as a family this year?", "What would it look like to involve the kids in this decision?"],
  "Estate Review": ["Does everyone understand the current plan?", "Has anything changed that the plan doesn't reflect yet?", "What questions has no one asked out loud?"],
};
function RelationalBonds() {
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
    <ModuleShell eyebrow="Relational Bonds" title="Family Meeting Facilitator & Multi-Generational Calendar" subtitle="Tools and planners for becoming part of the family's rhythm, not just its reviews.">
      <div className="sw-card" style={{ padding: 22, marginBottom: 30 }}>
        <div className="sw-serif" style={{ fontWeight: 700, fontSize: 16, marginBottom: 14 }}>Family Meeting Facilitator</div>
        <select className="sw-input" value={meetingType} onChange={(e) => setMeetingType(e.target.value)} style={{ marginBottom: 16, width: "100%", maxWidth: 320 }}>
          {Object.keys(MEETING_TYPES).map((t) => <option key={t}>{t}</option>)}
        </select>
        <div className="sw-label" style={{ fontSize: 9.5, color: GOLD, marginBottom: 8 }}>Suggested Agenda</div>
        {MEETING_TYPES[meetingType].map((q, i) => (
          <div key={i} style={{ display: "flex", gap: 10, padding: "8px 0", borderTop: `1px solid ${LINE}` }}>
            <span style={{ color: GOLD, fontWeight: 700, fontSize: 12 }}>{i + 1}</span>
            <span style={{ fontSize: 13 }}>{q}</span>
          </div>
        ))}
      </div>

      <div className="sw-card" style={{ padding: 22 }}>
        <div className="sw-serif" style={{ fontWeight: 700, fontSize: 16, marginBottom: 14 }}>Multi-Generational Calendar</div>
        <div style={{ display: "flex", gap: 10, flexWrap: "wrap", marginBottom: 16 }}>
          <input className="sw-input" placeholder="Event name" value={form.name} onChange={(e) => setForm((f) => ({ ...f, name: e.target.value }))} style={{ flex: "1 1 180px" }} />
          <input className="sw-input" placeholder="Who (e.g. Grandma)" value={form.who} onChange={(e) => setForm((f) => ({ ...f, who: e.target.value }))} style={{ flex: "1 1 160px" }} />
          <input className="sw-input" type="date" value={form.date} onChange={(e) => setForm((f) => ({ ...f, date: e.target.value }))} style={{ flex: "1 1 160px" }} />
          <button onClick={addDate} className="sw-btn sw-label" style={{ background: NAVY, color: WHITE, border: "none", borderRadius: 6, padding: "9px 18px", fontSize: 11, fontWeight: 700 }}>Add</button>
        </div>
        {dates.map((d, i) => (
          <div key={i} style={{ display: "flex", justifyContent: "space-between", padding: "9px 0", borderTop: `1px solid ${LINE}`, fontSize: 13 }}>
            <span>{d.name} {d.who && <span style={{ color: SLATE }}>&middot; {d.who}</span>}</span>
            <span className="sw-label" style={{ fontSize: 10, color: GOLD }}>{d.date}</span>
          </div>
        ))}
      </div>
    </ModuleShell>
  );
}

/* =====================================================================
   AUM GROWTH — Complete Financial Picture + Exit Readiness
===================================================================== */
const ASSET_CATEGORIES = ["Investment Accounts", "Retirement Accounts", "Real Estate", "Business Interests", "Life Insurance", "Other Advisory Relationships"];
function AumGrowth() {
  const [assets, setAssets] = useState(Object.fromEntries(ASSET_CATEGORIES.map((c) => [c, "unknown"])));
  const [exitScores, setExitScores] = useState({ "Financial readiness": 5, "Successor readiness": 5, "Legal & tax structure": 5, "Emotional readiness": 5, "Post-exit purpose": 5 });

  const managedCount = Object.values(assets).filter((v) => v === "managed").length;
  const avgExit = Object.values(exitScores).reduce((a, b) => a + b, 0) / Object.keys(exitScores).length;
  const exitLevel = avgExit < 4 ? "Early — mostly unexplored" : avgExit < 7 ? "Developing — real progress made" : "Advanced — largely exit-ready";

  return (
    <ModuleShell eyebrow="AUM Growth" title="Complete Financial Picture & Business Exit Readiness" subtitle="Explicitly permission-based — this helps the family see the whole picture. It is never framed as prospecting.">
      <div className="sw-card" style={{ padding: 22, marginBottom: 30 }}>
        <div style={{ display: "flex", justifyContent: "space-between", marginBottom: 14 }}>
          <div className="sw-serif" style={{ fontWeight: 700, fontSize: 16 }}>Complete Financial Picture</div>
          <span className="sw-label" style={{ fontSize: 10, color: GOLD }}>{managedCount}/{ASSET_CATEGORIES.length} currently managed here</span>
        </div>
        {ASSET_CATEGORIES.map((c) => (
          <div key={c} style={{ display: "flex", justifyContent: "space-between", alignItems: "center", padding: "10px 0", borderTop: `1px solid ${LINE}` }}>
            <span style={{ fontSize: 13 }}>{c}</span>
            <div style={{ display: "flex", gap: 6 }}>
              {["managed", "held elsewhere", "unknown"].map((opt) => (
                <button key={opt} onClick={() => setAssets((a) => ({ ...a, [c]: opt }))} className="sw-label"
                  style={{ fontSize: 9, padding: "5px 10px", borderRadius: 12, border: `1px solid ${assets[c] === opt ? GOLD : LINE}`, background: assets[c] === opt ? GOLD : "transparent", color: assets[c] === opt ? WHITE : SLATE, cursor: "pointer" }}>
                  {opt}
                </button>
              ))}
            </div>
          </div>
        ))}
        <div style={{ marginTop: 14, fontSize: 11.5, color: SLATE, fontStyle: "italic" }}>Family consent required before any "held elsewhere" asset is discussed further.</div>
      </div>

      <div className="sw-card" style={{ padding: 22 }}>
        <div style={{ display: "flex", justifyContent: "space-between", marginBottom: 14 }}>
          <div className="sw-serif" style={{ fontWeight: 700, fontSize: 16 }}>Business Exit Readiness</div>
          <span className="sw-label" style={{ fontSize: 10, color: GOLD }}>{exitLevel}</span>
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

/* =====================================================================
   SUCCESSOR & STEWARD JOURNEY
===================================================================== */
const FLOURISHING_17 = ["Joy","Health","Purpose","Character","Relationships","Faith","Family","Work","Business","Marketplace","Finances","Leadership","Community","Resilience","Growth","Generosity","Legacy"];
const STEWARD_STAGES = [
  ["Identity & Purpose", "Life Message Builder + Family Values Builder — who am I becoming as a steward, not a skills checklist."],
  ["Priority", "A protected, recurring block of time for succession work, defended against whatever feels urgent."],
  ["Small, Sustained Habits", "Two-minute starting habits, stacked onto existing family rituals, tracked with a readiness scorecard."],
  ["Collaboration", "Family council practice built on understanding-first listening and win-win framing."],
];
function StewardJourney() {
  const [stage, setStage] = useState(0);
  const [focusDims, setFocusDims] = useState([]);

  const toggleDim = (d) => setFocusDims((f) => f.includes(d) ? f.filter((x) => x !== d) : f.length < 4 ? [...f, d] : f);

  return (
    <ModuleShell eyebrow="Successor & Steward Journey" title="Sequenced Covey's way. Built to stick with habit science." subtitle="Identity → Priority → Habits → Collaboration — and a development plan drawn from the 17 Flourishing dimensions.">
      <div style={{ display: "flex", gap: 8, marginBottom: 24, flexWrap: "wrap" }}>
        {STEWARD_STAGES.map((s, i) => (
          <button key={s[0]} onClick={() => setStage(i)} className="sw-tab"
            style={{ padding: "10px 16px", borderRadius: 20, border: `1.5px solid ${stage === i ? NAVY : LINE}`, background: stage === i ? NAVY : WHITE, color: stage === i ? WHITE : INK, fontSize: 11 }}>
            {i + 1}. {s[0]}
          </button>
        ))}
      </div>
      <div className="sw-card sw-fade" key={stage} style={{ padding: 24, marginBottom: 30 }}>
        <div className="sw-serif" style={{ fontWeight: 700, fontSize: 18, color: NAVY, marginBottom: 10 }}>{STEWARD_STAGES[stage][0]}</div>
        <div style={{ fontSize: 13.5, color: INK, lineHeight: 1.6 }}>{STEWARD_STAGES[stage][1]}</div>
      </div>

      <div className="sw-card" style={{ padding: 22 }}>
        <div className="sw-serif" style={{ fontWeight: 700, fontSize: 16, marginBottom: 6 }}>Build the Development Plan</div>
        <div style={{ fontSize: 12.5, color: SLATE, marginBottom: 14 }}>Choose up to four Flourishing dimensions to focus this successor's development plan on.</div>
        <div style={{ display: "flex", flexWrap: "wrap", gap: 8, marginBottom: 16 }}>
          {FLOURISHING_17.map((d) => (
            <button key={d} onClick={() => toggleDim(d)} className="sw-label"
              style={{ fontSize: 10, padding: "7px 12px", borderRadius: 14, border: `1px solid ${focusDims.includes(d) ? GOLD : LINE}`, background: focusDims.includes(d) ? GOLD : "transparent", color: focusDims.includes(d) ? WHITE : INK, cursor: "pointer" }}>
              {d}
            </button>
          ))}
        </div>
        {focusDims.length > 0 && (
          <div className="sw-fade" style={{ background: CREAM, borderLeft: `3px solid ${GOLD}`, padding: "12px 16px", fontSize: 12.5 }}>
            This successor's plan will draw from: <b>{focusDims.join(", ")}</b> — reusing existing Flourishing LifeTogether content, no new curriculum required.
          </div>
        )}
      </div>
    </ModuleShell>
  );
}

/* =====================================================================
   FAMILY BUSINESS
===================================================================== */
const GOVERNANCE_ITEMS = ["Written family employment policy", "Board of advisors or directors", "Family communication protocol", "Documented succession plan", "Regular family business meetings", "Conflict resolution process"];
const ROLES = ["CEO / Leadership", "Finance", "Operations", "Board Seat", "Advisory Only"];
function FamilyBusiness() {
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
    <ModuleShell eyebrow="Family Business" title="Governance, roles, and readiness." subtitle="A shared picture of how the family business is actually structured — and who's ready for what.">
      <div className="sw-card" style={{ padding: 22, marginBottom: 30 }}>
        <div style={{ display: "flex", justifyContent: "space-between", marginBottom: 14 }}>
          <div className="sw-serif" style={{ fontWeight: 700, fontSize: 16 }}>Governance Checklist</div>
          <span className="sw-label" style={{ fontSize: 10, color: GOLD }}>{govCount}/{GOVERNANCE_ITEMS.length}</span>
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

      <div className="sw-card" style={{ padding: 22 }}>
        <div className="sw-serif" style={{ fontWeight: 700, fontSize: 16, marginBottom: 14 }}>Role Readiness</div>
        <div style={{ display: "flex", gap: 10, flexWrap: "wrap", marginBottom: 16 }}>
          <input className="sw-input" placeholder="Family member name" value={form.name} onChange={(e) => setForm((f) => ({ ...f, name: e.target.value }))} style={{ flex: "1 1 200px" }} />
          <select className="sw-input" value={form.role} onChange={(e) => setForm((f) => ({ ...f, role: e.target.value }))} style={{ flex: "1 1 160px" }}>
            {ROLES.map((r) => <option key={r}>{r}</option>)}
          </select>
          <button onClick={addMember} className="sw-btn sw-label" style={{ background: NAVY, color: WHITE, border: "none", borderRadius: 6, padding: "9px 18px", fontSize: 11, fontWeight: 700 }}>Add</button>
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

/* =====================================================================
   STORIES
===================================================================== */
const STORY_PROMPTS = [
  "Tell about a time your family showed generosity even when it was hard.",
  "What's a decision an earlier generation made that still shapes the family today?",
  "Describe a moment you saw a family value actually lived out, not just talked about.",
  "What's a family story about failure that taught something important?",
  "What's something your grandparents believed that you want your grandchildren to know?",
];
const VALUE_TAGS = ["Faith", "Generosity", "Perseverance", "Integrity", "Family", "Work Ethic"];
function Stories() {
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
    <ModuleShell eyebrow="Stories" title="Legacy, history, and value-based stories." subtitle="Helping the next generation build on and understand the family's why — captured once, available to everyone after.">
      <div className="sw-card" style={{ padding: 22, marginBottom: 30 }}>
        <Field label="Prompt">
          <select className="sw-input" value={prompt} onChange={(e) => setPrompt(e.target.value)} style={{ width: "100%" }}>
            {STORY_PROMPTS.map((p) => <option key={p}>{p}</option>)}
          </select>
        </Field>
        <div style={{ display: "flex", gap: 10, marginBottom: 14 }}>
          <div style={{ flex: 1 }}>
            <Field label="Who's telling it"><input className="sw-input" style={{ width: "100%" }} value={teller} onChange={(e) => setTeller(e.target.value)} placeholder="e.g. Grandma Ruth" /></Field>
          </div>
          <div style={{ flex: 1 }}>
            <Field label="Value it reflects">
              <select className="sw-input" style={{ width: "100%" }} value={tag} onChange={(e) => setTag(e.target.value)}>
                {VALUE_TAGS.map((v) => <option key={v}>{v}</option>)}
              </select>
            </Field>
          </div>
        </div>
        <Field label="The story">
          <textarea className="sw-input" style={{ width: "100%", minHeight: 90, fontFamily: "Inter" }} value={text} onChange={(e) => setText(e.target.value)} placeholder="Write it the way you'd tell it out loud..." />
        </Field>
        <button onClick={saveStory} className="sw-btn sw-label" style={{ background: GOLD, color: WHITE, border: "none", borderRadius: 22, padding: "11px 24px", fontSize: 11, fontWeight: 700 }}>Save to the Family Library</button>
      </div>

      <div className="sw-label" style={{ fontSize: 10, color: GOLD, marginBottom: 12 }}>{stories.length} {stories.length === 1 ? "story" : "stories"} in the library</div>
      {stories.map((s, i) => (
        <div key={i} className="sw-card" style={{ padding: 18, marginBottom: 12 }}>
          <div style={{ display: "flex", justifyContent: "space-between", marginBottom: 8 }}>
            <span className="sw-serif" style={{ fontWeight: 700, fontSize: 14 }}>{s.teller}</span>
            <span className="sw-label" style={{ fontSize: 9, color: GOLD, background: CREAM, padding: "3px 9px", borderRadius: 10 }}>{s.tag}</span>
          </div>
          <div style={{ fontSize: 11, color: SLATE, fontStyle: "italic", marginBottom: 8 }}>{s.prompt}</div>
          <div style={{ fontSize: 13, color: INK, lineHeight: 1.55 }}>{s.text}</div>
        </div>
      ))}
    </ModuleShell>
  );
}

/* =====================================================================
   APP SHELL
===================================================================== */
export default function FamilyStewardshipPrototype() {
  const [tab, setTab] = useState("dashboard");
  const [menuOpen, setMenuOpen] = useState(false);

  return (
    <div className="sw-root">
      <style>{FONTS}</style>
      <div style={{ background: NAVY, borderBottom: `1px solid rgba(217,184,118,0.25)` }}>
        <div style={{ maxWidth: 1180, margin: "0 auto", padding: "16px 28px", display: "flex", alignItems: "center", justifyContent: "space-between" }}>
          <button onClick={() => setTab("dashboard")} className="sw-serif sw-btn" style={{ background: "none", border: "none", color: WHITE, fontWeight: 700, fontSize: 15.5 }}>Family Stewardship&trade;</button>
          <div style={{ display: "none", gap: 4 }} className="sw-desktop-nav">
            {TABS.map((t) => (
              <button key={t.id} onClick={() => setTab(t.id)} className="sw-tab"
                style={{ padding: "8px 12px", fontSize: 10.5, color: tab === t.id ? GOLD_BRIGHT : "rgba(251,248,241,0.75)", borderBottom: tab === t.id ? `2px solid ${GOLD}` : "2px solid transparent" }}>
                {t.label}
              </button>
            ))}
          </div>
          <button onClick={() => setMenuOpen((v) => !v)} className="sw-mobile-nav-btn" style={{ background: "none", border: `1px solid rgba(217,184,118,0.5)`, borderRadius: 6, padding: "7px 12px", color: GOLD_BRIGHT, cursor: "pointer", fontSize: 12 }}>
            {menuOpen ? "Close" : "Menu"}
          </button>
        </div>
        {menuOpen && (
          <div style={{ padding: "0 28px 16px" }}>
            {TABS.map((t) => (
              <div key={t.id} onClick={() => { setTab(t.id); setMenuOpen(false); }} className="sw-label"
                style={{ padding: "10px 0", borderTop: "1px solid rgba(217,184,118,0.15)", color: tab === t.id ? GOLD_BRIGHT : "rgba(251,248,241,0.85)", fontSize: 11, cursor: "pointer" }}>
                {t.label}
              </div>
            ))}
          </div>
        )}
      </div>

      {tab === "dashboard" && <Dashboard setTab={setTab} />}
      {tab === "familymap" && <FamilyMap />}
      {tab === "retention" && <Retention />}
      {tab === "relational" && <RelationalBonds />}
      {tab === "aum" && <AumGrowth />}
      {tab === "steward" && <StewardJourney />}
      {tab === "business" && <FamilyBusiness />}
      {tab === "stories" && <Stories />}

      <style>{`
        @media (min-width: 860px) {
          .sw-desktop-nav { display: flex !important; }
          .sw-mobile-nav-btn { display: none !important; }
        }
      `}</style>
    </div>
  );
}
