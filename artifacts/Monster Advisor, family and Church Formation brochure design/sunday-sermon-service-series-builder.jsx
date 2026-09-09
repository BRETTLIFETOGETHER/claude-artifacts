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

const FONTS = `
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,600;0,700;0,900;1,500;1,600&family=Archivo:wght@500;600;700&family=Inter:wght@400;500;600;700&display=swap');
* { box-sizing: border-box; }
body { margin: 0; }
.bb-root { font-family: 'Inter', sans-serif; color: ${INK}; background: ${WHITE}; min-height: 100vh; }
.bb-serif { font-family: 'Playfair Display', serif; }
.bb-label { font-family: 'Archivo', sans-serif; letter-spacing: 0.12em; text-transform: uppercase; }
.bb-input { font-family:'Inter'; font-size:13px; padding:10px 13px; border:1px solid ${LINE}; border-radius:7px; outline:none; background:${WHITE}; }
.bb-input:focus { border-color:${GOLD}; }
.bb-tab { background:none; border:none; cursor:pointer; font-family:'Archivo'; font-weight:700; }
.bb-btn { transition: transform .15s ease; cursor:pointer; }
.bb-btn:hover { transform: translateY(-1px); }
.bb-fade { animation: bbFade .35s ease both; }
@keyframes bbFade { from { opacity:0; transform:translateY(6px);} to {opacity:1; transform:translateY(0);} }
.bb-card { border:1px solid ${LINE}; border-radius:8px; background:${WHITE}; }
::selection { background: ${GOLD}; color: ${WHITE}; }
`;

const TOP_TABS = [
  ["sermon", "Sunday Sermon Builder"],
  ["service", "Service Builder"],
  ["series", "Series Builder"],
  ["library", "My Library"],
];

const CATALYTIC_CATEGORIES = [
  "Salvation & Response", "Baptism Sunday", "Vision & Future", "Generosity & Commitment",
  "Outreach & Invite", "Courage & Breakthrough", "Healing & Restoration", "New Beginnings",
  "Capital Campaign Kickoff", "Membership & Belonging", "Volunteer & Serve", "Prayer & Revival",
];

const TEN_THINGS = [
  "The Big Idea", "Primary + Supporting Scripture", "Full Outline", "Illustrations & Stories",
  "Application / Next Steps", "Small Group Discussion Questions", "Response / Call to Action",
  "Slide & Visual Outline", "Promotional / Social Copy", "Prayer Points",
];

const WORSHIP_ORDER = ["Welcome & Gathering Song", "Worship Set (2–3 songs)", "Announcements", "Offertory", "Worship Set (1–2 songs)", "Message", "Response Song / Altar Call", "Benediction"];

const OFFERTORY_PRAYERS = {
  "Salvation & Response": "Lord, before we bring You our gifts, we bring You ourselves — imperfect, but Yours. May what we give reflect what You've already given us in Christ. Amen.",
  "Baptism Sunday": "Father, as we witness these baptisms and bring our offering, we thank You that both are acts of the same surrender — a life laid down and a life given back. Amen.",
  "Vision & Future": "God, we give not because the vision needs our money, but because our hearts need to be shaped by what we treasure. Let this gift be an act of trust in where You're leading us. Amen.",
  "Generosity & Commitment": "Lord, You gave first. Every gift we bring is simply a response to Yours. Multiply what's given here for Your purposes, not ours. Amen.",
  "Outreach & Invite": "Father, let this offering open doors we can't yet see — for someone far from You to find their way home. Amen.",
  "Courage & Breakthrough": "God, give us the same courage to give boldly that You're asking us to have in every other area of our lives. Amen.",
  "Healing & Restoration": "Lord, as You restore what's broken in us, let this gift be a small act of restoration in someone else's story. Amen.",
  "New Beginnings": "Father, as we start this new season, let our giving start it too — with open hands, not clenched fists. Amen.",
  "Capital Campaign Kickoff": "God, what we build with these gifts will outlast us. Let it be built on trust in You, not in ourselves. Amen.",
  "Membership & Belonging": "Lord, as we welcome these new members into our family, let our giving reflect the family we're becoming together. Amen.",
  "Volunteer & Serve": "Father, just as we're asking people to give their time today, let this offering be our time and treasure given together. Amen.",
  "Prayer & Revival": "God, send whatever fire You want to send — starting with our willingness to hold nothing back, including this gift. Amen.",
};

const CLOSING_PRAYERS = {
  "Salvation & Response": "Lord, for everyone who said yes today, seal what You started. For everyone still deciding, keep drawing them gently. In Jesus' name, Amen.",
  "Baptism Sunday": "Father, thank You for every story we witnessed today. Hold these new believers close as they live out what they've just declared. Amen.",
  "Vision & Future": "God, write this vision on our hearts as we leave this room. Let it shape our week, not just our Sunday. Amen.",
  "Generosity & Commitment": "Lord, thank You for every hand raised, every card signed. Now help us live out what we just committed to. Amen.",
  "Outreach & Invite": "Father, go with everyone who came today for the first time. Let them feel how much You love them. Amen.",
  "Courage & Breakthrough": "God, whatever wall we've been facing, thank You for reminding us it's already coming down in Your timing. Amen.",
  "Healing & Restoration": "Lord, for every person carrying something heavy today, thank You that You carry it with them. Amen.",
  "New Beginnings": "Father, thank You for the fresh start we've just been reminded is always available. Help us actually take it. Amen.",
  "Capital Campaign Kickoff": "God, thank You for what we're building together. Let every brick of it point back to You. Amen.",
  "Membership & Belonging": "Lord, thank You for every new name added to our family today. Help us live like we actually belong to each other. Amen.",
  "Volunteer & Serve": "Father, thank You for every hand that will serve because of today. Multiply it for Your kingdom. Amen.",
  "Prayer & Revival": "God, don't let this be a moment we remember — let it be a movement we live. Amen.",
};

const BENEDICTIONS = {
  "Salvation & Response": "Go in the confidence that you are fully known and fully loved. May the God who began a good work in you today carry it to completion. Amen.",
  "Baptism Sunday": "Go as people who have died to the old and risen to the new. May the life you declared today be the life you actually live. Amen.",
  "Vision & Future": "Go carrying the vision you've just received. May God make it more than words — may He make it your life. Amen.",
  "Generosity & Commitment": "Go as people whose hands are open, not clenched. May God multiply what you've given far beyond what you can see. Amen.",
  "Outreach & Invite": "Go and be the invitation someone else needs this week. May God use your ordinary life to point to His extraordinary love. Amen.",
  "Courage & Breakthrough": "Go without fear. The same God who brought you breakthrough today goes with you into whatever's next. Amen.",
  "Healing & Restoration": "Go as people being made whole. What God started in you today, He will finish. Amen.",
  "New Beginnings": "Go into this new season with open hands and a clear conscience. The past does not get the final word. Amen.",
  "Capital Campaign Kickoff": "Go as builders, not just spectators. May what we start today outlast every one of us. Amen.",
  "Membership & Belonging": "Go as people who belong to each other, not just to a building. May this family carry you the rest of the week. Amen.",
  "Volunteer & Serve": "Go and use whatever you've been given for someone who needs it. Your part matters more than you think. Amen.",
  "Prayer & Revival": "Go and keep seeking. What started on your knees today doesn't have to end when you stand up. Amen.",
};

function Eyebrow({ children }) {
  return <div className="bb-label" style={{ fontSize: 10, color: GOLD, display: "flex", alignItems: "center", gap: 8, marginBottom: 8 }}>
    <span style={{ width: 18, height: 2, background: GOLD, display: "inline-block" }} />{children}
  </div>;
}

/* ---------------- SERMON BUILDER ---------------- */
function SermonBuilder({ library }) {
  const [source, setSource] = useState("category");
  const [category, setCategory] = useState(CATALYTIC_CATEGORIES[0]);
  const [libItem, setLibItem] = useState(library[0]?.title || "");
  const [checked, setChecked] = useState({});
  const [built, setBuilt] = useState(false);

  const toggleCheck = (item) => setChecked((c) => ({ ...c, [item]: !c[item] }));
  const checkedCount = Object.values(checked).filter(Boolean).length;

  return (
    <div className="bb-fade">
      <Eyebrow>Sunday Sermon Builder</Eyebrow>
      <h2 className="bb-serif" style={{ fontSize: 22, fontWeight: 700, color: NAVY, marginBottom: 6 }}>Build a custom edition from any of the 12 categories.</h2>
      <p style={{ fontSize: 12.5, color: SLATE, marginBottom: 20 }}>Includes the worship order, offertory prayer, closing prayer, and benediction — plus the ten supporting elements every sermon needs.</p>

      <div style={{ display: "flex", gap: 8, marginBottom: 16 }}>
        <button onClick={() => setSource("category")} className="bb-tab" style={{ padding: "8px 16px", borderRadius: 16, border: `1.5px solid ${source === "category" ? NAVY : LINE}`, background: source === "category" ? NAVY : WHITE, color: source === "category" ? WHITE : INK, fontSize: 11 }}>From a Category</button>
        <button onClick={() => setSource("library")} className="bb-tab" style={{ padding: "8px 16px", borderRadius: 16, border: `1.5px solid ${source === "library" ? NAVY : LINE}`, background: source === "library" ? NAVY : WHITE, color: source === "library" ? WHITE : INK, fontSize: 11 }}>From My Library</button>
      </div>

      {source === "category" ? (
        <select className="bb-input" style={{ width: "100%", maxWidth: 360, marginBottom: 18 }} value={category} onChange={(e) => { setCategory(e.target.value); setBuilt(false); setChecked({}); }}>
          {CATALYTIC_CATEGORIES.map((c) => <option key={c}>{c}</option>)}
        </select>
      ) : (
        <select className="bb-input" style={{ width: "100%", maxWidth: 360, marginBottom: 18 }} value={libItem} onChange={(e) => { setLibItem(e.target.value); setBuilt(false); setChecked({}); }}>
          {library.map((l) => <option key={l.title}>{l.title}</option>)}
        </select>
      )}

      <button onClick={() => setBuilt(true)} className="bb-btn bb-label" style={{ background: GOLD, color: WHITE, border: "none", borderRadius: 22, padding: "11px 24px", fontSize: 11, fontWeight: 700 }}>Build This Sunday</button>

      {built && (
        <div className="bb-fade" style={{ marginTop: 26 }}>
          <div className="bb-card" style={{ padding: 20, marginBottom: 14, background: CREAM }}>
            <div className="bb-serif" style={{ fontWeight: 700, fontSize: 16, color: NAVY, marginBottom: 4 }}>
              {source === "category" ? category : libItem}
            </div>
            <div className="bb-label" style={{ fontSize: 9, color: SLATE }}>{source === "category" ? "Catalytic Sunday" : "Built from your personal library"}</div>
          </div>

          <div className="bb-card" style={{ padding: 20, marginBottom: 14 }}>
            <div className="bb-label" style={{ fontSize: 9.5, color: GOLD, marginBottom: 10 }}>Worship Order</div>
            {WORSHIP_ORDER.map((w, i) => (
              <div key={w} style={{ display: "flex", gap: 10, padding: "7px 0", borderTop: i > 0 ? `1px solid ${LINE}` : "none", fontSize: 12.5 }}>
                <span style={{ color: GOLD, fontWeight: 700 }}>{i + 1}</span><span>{w}</span>
              </div>
            ))}
          </div>

          {source === "category" && (
            <>
              <div className="bb-card" style={{ padding: 20, marginBottom: 14 }}>
                <div className="bb-label" style={{ fontSize: 9.5, color: GOLD, marginBottom: 8 }}>Offertory Prayer</div>
                <p style={{ fontSize: 13, fontStyle: "italic", color: NAVY, lineHeight: 1.6, margin: 0 }}>{OFFERTORY_PRAYERS[category]}</p>
              </div>
              <div className="bb-card" style={{ padding: 20, marginBottom: 14 }}>
                <div className="bb-label" style={{ fontSize: 9.5, color: GOLD, marginBottom: 8 }}>Closing Prayer</div>
                <p style={{ fontSize: 13, fontStyle: "italic", color: NAVY, lineHeight: 1.6, margin: 0 }}>{CLOSING_PRAYERS[category]}</p>
              </div>
              <div className="bb-card" style={{ padding: 20, marginBottom: 14 }}>
                <div className="bb-label" style={{ fontSize: 9.5, color: GOLD, marginBottom: 8 }}>Benediction</div>
                <p style={{ fontSize: 13, fontStyle: "italic", color: NAVY, lineHeight: 1.6, margin: 0 }}>{BENEDICTIONS[category]}</p>
              </div>
            </>
          )}

          <div className="bb-card" style={{ padding: 20 }}>
            <div style={{ display: "flex", justifyContent: "space-between", marginBottom: 10 }}>
              <div className="bb-label" style={{ fontSize: 9.5, color: GOLD }}>The Ten Supporting Elements</div>
              <span className="bb-label" style={{ fontSize: 9, color: SLATE }}>{checkedCount}/10 built</span>
            </div>
            {TEN_THINGS.map((t) => (
              <div key={t} onClick={() => toggleCheck(t)} style={{ display: "flex", gap: 12, alignItems: "center", padding: "8px 0", borderTop: `1px solid ${LINE}`, cursor: "pointer" }}>
                <div style={{ width: 17, height: 17, borderRadius: 4, border: `1.5px solid ${checked[t] ? GREEN : LINE}`, background: checked[t] ? GREEN : "transparent", display: "flex", alignItems: "center", justifyContent: "center", color: WHITE, fontSize: 9, flexShrink: 0 }}>{checked[t] ? "\u2713" : ""}</div>
                <span style={{ fontSize: 12.5 }}>{t}</span>
              </div>
            ))}
          </div>
        </div>
      )}
    </div>
  );
}

/* ---------------- SERVICE BUILDER ---------------- */
const SERVICE_ELEMENT_OPTIONS = ["Welcome & Gathering Song", "Worship Set", "Announcements", "Offertory", "Communion", "Baptisms", "Message", "Response Song", "Testimony / Story", "Benediction"];
function ServiceBuilder({ library }) {
  const [elements, setElements] = useState([
    { name: "Welcome & Gathering Song", minutes: 5 },
    { name: "Worship Set", minutes: 15 },
    { name: "Announcements", minutes: 3 },
    { name: "Offertory", minutes: 4 },
    { name: "Message", minutes: 32 },
    { name: "Response Song", minutes: 4 },
    { name: "Benediction", minutes: 1 },
  ]);
  const [sermonSource, setSermonSource] = useState(library[0]?.title || "");

  const addElement = (name) => setElements((e) => [...e, { name, minutes: 5 }]);
  const removeElement = (idx) => setElements((e) => e.filter((_, i) => i !== idx));
  const setMinutes = (idx, m) => setElements((e) => e.map((el, i) => i === idx ? { ...el, minutes: m } : el));
  const total = elements.reduce((sum, e) => sum + e.minutes, 0);

  return (
    <div className="bb-fade">
      <Eyebrow>Service Builder</Eyebrow>
      <h2 className="bb-serif" style={{ fontSize: 22, fontWeight: 700, color: NAVY, marginBottom: 6 }}>Build the full order of service.</h2>
      <p style={{ fontSize: 12.5, color: SLATE, marginBottom: 20 }}>Add, remove, and time every element — the sermon slot pulls directly from your personal library.</p>

      <div className="bb-card" style={{ padding: 20, marginBottom: 16 }}>
        <div className="bb-label" style={{ fontSize: 9.5, color: GOLD, marginBottom: 8 }}>Sermon Slot — Pulled From My Library</div>
        <select className="bb-input" style={{ width: "100%" }} value={sermonSource} onChange={(e) => setSermonSource(e.target.value)}>
          {library.map((l) => <option key={l.title}>{l.title}</option>)}
        </select>
      </div>

      <div className="bb-card" style={{ padding: 20, marginBottom: 16 }}>
        <div style={{ display: "flex", justifyContent: "space-between", marginBottom: 12 }}>
          <div className="bb-label" style={{ fontSize: 9.5, color: GOLD }}>Order of Service</div>
          <span className="bb-label" style={{ fontSize: 10, color: NAVY, fontWeight: 700 }}>{total} min total</span>
        </div>
        {elements.map((el, i) => (
          <div key={i} style={{ display: "flex", gap: 10, alignItems: "center", padding: "8px 0", borderTop: i > 0 ? `1px solid ${LINE}` : "none" }}>
            <span style={{ color: GOLD, fontWeight: 700, fontSize: 12, width: 16 }}>{i + 1}</span>
            <span style={{ fontSize: 12.5, flex: 1 }}>{el.name === "Message" ? sermonSource : el.name}</span>
            <input type="number" className="bb-input" style={{ width: 56, padding: "5px 8px", textAlign: "center" }} value={el.minutes} onChange={(e) => setMinutes(i, Number(e.target.value))} />
            <span style={{ fontSize: 10, color: SLATE }}>min</span>
            <button onClick={() => removeElement(i)} style={{ background: "none", border: "none", color: SLATE, cursor: "pointer", fontSize: 14 }}>&times;</button>
          </div>
        ))}
      </div>

      <div className="bb-label" style={{ fontSize: 9.5, color: GOLD, marginBottom: 8 }}>Add an Element</div>
      <div style={{ display: "flex", flexWrap: "wrap", gap: 8 }}>
        {SERVICE_ELEMENT_OPTIONS.map((opt) => (
          <button key={opt} onClick={() => addElement(opt)} className="bb-label" style={{ fontSize: 10, padding: "7px 13px", borderRadius: 14, border: `1px solid ${LINE}`, background: WHITE, cursor: "pointer" }}>+ {opt}</button>
        ))}
      </div>
    </div>
  );
}

/* ---------------- SERIES BUILDER ---------------- */
const LENGTH_WEEKS = { 21: 3, 30: 4, 40: 6 };
function SeriesBuilder({ library }) {
  const [length, setLength] = useState(40);
  const [weeks, setWeeks] = useState(Array(6).fill("").map((_, i) => i === 0 ? "Week 1 — Foundations" : ""));

  const weekCount = LENGTH_WEEKS[length];
  const setWeek = (i, val) => setWeeks((w) => w.map((x, idx) => idx === i ? val : x));
  const pullFromLibrary = (i, title) => setWeek(i, title);

  return (
    <div className="bb-fade">
      <Eyebrow>Series Builder</Eyebrow>
      <h2 className="bb-serif" style={{ fontSize: 22, fontWeight: 700, color: NAVY, marginBottom: 6 }}>Plan a multi-week series, pulling from your library week by week.</h2>
      <div style={{ display: "flex", gap: 8, marginBottom: 20 }}>
        {[21, 30, 40].map((l) => (
          <button key={l} onClick={() => setLength(l)} className="bb-tab" style={{ padding: "9px 18px", borderRadius: 18, border: `1.5px solid ${length === l ? NAVY : LINE}`, background: length === l ? NAVY : WHITE, color: length === l ? WHITE : INK, fontSize: 11 }}>{l}-Day ({LENGTH_WEEKS[l]} weeks)</button>
        ))}
      </div>

      {Array.from({ length: weekCount }).map((_, i) => (
        <div key={i} className="bb-card" style={{ padding: 18, marginBottom: 12 }}>
          <div className="bb-label" style={{ fontSize: 9, color: GOLD, marginBottom: 8 }}>Week {i + 1}</div>
          <input className="bb-input" style={{ width: "100%", marginBottom: 10 }} placeholder="Week theme or title" value={weeks[i] || ""} onChange={(e) => setWeek(i, e.target.value)} />
          <div style={{ display: "flex", flexWrap: "wrap", gap: 6 }}>
            {library.map((l) => (
              <button key={l.title} onClick={() => pullFromLibrary(i, l.title)} className="bb-label" style={{ fontSize: 9, padding: "5px 10px", borderRadius: 10, border: `1px solid ${LINE}`, background: CREAM, cursor: "pointer" }}>Pull: {l.title}</button>
            ))}
          </div>
        </div>
      ))}
    </div>
  );
}

/* ---------------- MY LIBRARY ---------------- */
function MyLibrary({ library, setLibrary }) {
  const [title, setTitle] = useState("");
  const [date, setDate] = useState("");

  const add = () => {
    if (!title.trim()) return;
    setLibrary((l) => [...l, { title, date: date || "Undated" }]);
    setTitle(""); setDate("");
  };

  return (
    <div className="bb-fade">
      <Eyebrow>My Library</Eyebrow>
      <h2 className="bb-serif" style={{ fontSize: 22, fontWeight: 700, color: NAVY, marginBottom: 6 }}>Your personal sermon library — feeds every builder above.</h2>
      <p style={{ fontSize: 12.5, color: SLATE, marginBottom: 20 }}>Add a past sermon or note here, and it becomes available to pull into the Sermon, Service, and Series builders.</p>

      <div className="bb-card" style={{ padding: 20, marginBottom: 20 }}>
        <div style={{ display: "flex", gap: 10, flexWrap: "wrap" }}>
          <input className="bb-input" placeholder="Sermon title" value={title} onChange={(e) => setTitle(e.target.value)} style={{ flex: "1 1 220px" }} />
          <input className="bb-input" placeholder="Date (optional)" value={date} onChange={(e) => setDate(e.target.value)} style={{ flex: "1 1 140px" }} />
          <button onClick={add} className="bb-btn bb-label" style={{ background: NAVY, color: WHITE, border: "none", borderRadius: 6, padding: "10px 18px", fontSize: 11, fontWeight: 700 }}>Add</button>
        </div>
      </div>

      {library.map((l, i) => (
        <div key={i} style={{ display: "flex", justifyContent: "space-between", padding: "12px 0", borderTop: `1px solid ${LINE}`, fontSize: 13 }}>
          <span>{l.title}</span>
          <span className="bb-label" style={{ fontSize: 9.5, color: GOLD }}>{l.date}</span>
        </div>
      ))}
    </div>
  );
}

/* ---------------- APP ---------------- */
export default function SundaySermonServiceSeriesBuilder() {
  const [tab, setTab] = useState("sermon");
  const [library, setLibrary] = useState([
    { title: "Hope in Hard Times — March 2", date: "Mar 2, 2025" },
    { title: "Notes on Romans 8", date: "Undated" },
    { title: "The Weight of Wealth — Stewardship Series Wk 3", date: "Sep 14, 2025" },
  ]);

  return (
    <div className="bb-root">
      <style>{FONTS}</style>
      <div style={{ background: `linear-gradient(165deg, ${NAVY} 0%, #0E1930 100%)` }}>
        <div style={{ maxWidth: 860, margin: "0 auto", padding: "40px 28px 24px" }}>
          <div className="bb-label" style={{ fontSize: 10, color: GOLD_BRIGHT, marginBottom: 10 }}>SUNDAY BUILDERS</div>
          <h1 className="bb-serif" style={{ fontSize: "clamp(22px, 4vw, 30px)", fontWeight: 700, color: WHITE, margin: 0 }}>Sermon. Service. Series. One library.</h1>
        </div>
        <div style={{ maxWidth: 860, margin: "0 auto", padding: "0 28px 20px", display: "flex", gap: 6, flexWrap: "wrap" }}>
          {TOP_TABS.map(([id, label]) => (
            <button key={id} onClick={() => setTab(id)} className="bb-tab" style={{ padding: "9px 16px", borderRadius: 18, fontSize: 11, border: `1.5px solid ${tab === id ? GOLD : "rgba(217,184,118,0.3)"}`, background: tab === id ? GOLD : "transparent", color: tab === id ? NAVY : "rgba(251,248,241,0.8)" }}>{label}</button>
          ))}
        </div>
      </div>

      <div style={{ maxWidth: 860, margin: "0 auto", padding: "30px 28px 80px" }}>
        {tab === "sermon" && <SermonBuilder library={library} />}
        {tab === "service" && <ServiceBuilder library={library} />}
        {tab === "series" && <SeriesBuilder library={library} />}
        {tab === "library" && <MyLibrary library={library} setLibrary={setLibrary} />}
      </div>
    </div>
  );
}
