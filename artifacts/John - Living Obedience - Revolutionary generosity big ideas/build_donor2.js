const pptxgen = require("pptxgenjs");

const NAVY = "12253F", DEEP = "0B1728", CREAM = "FAF7F0", WARM = "F2EDE1",
      GOLD = "B08B3F", CHAR = "2B2B2B", MUTE = "6E6A62", LINE = "D8D0C2", PALE = "E6E0D4";

const pres = new pptxgen();
pres.layout = "LAYOUT_WIDE";
pres.title = "Visionary Generosity — Donor & Partner Presentation";

const SER = "Georgia", SAN = "Calibri";

function motif(s, dark) {
  s.addShape(pres.ShapeType.ellipse, { x: 0.75, y: 6.9, w: 0.12, h: 0.12, fill: { color: GOLD } });
  s.addShape(pres.ShapeType.ellipse, { x: 0.96, y: 6.9, w: 0.12, h: 0.12, fill: { color: "FFFFFF", transparency: 100 }, line: { color: dark ? GOLD : LINE, width: 1 } });
}
function pageno(s, n, dark) {
  s.addText(String(n).padStart(2, "0"), { x: 12.1, y: 6.85, w: 0.5, h: 0.25, fontFace: SER, fontSize: 10, color: dark ? "6B6455" : "B4AC9C", align: "right", margin: 0 });
}
function eyebrow(s, t) {
  s.addText(t.toUpperCase(), { x: 0.75, y: 0.6, w: 9.5, h: 0.28, fontFace: SER, fontSize: 9.5, color: GOLD, charSpacing: 3.5, margin: 0 });
}
let N = 0;
function slide(mode, eb, title) {
  N++;
  const s = pres.addSlide();
  const isDark = mode === "dark";
  s.background = { color: isDark ? NAVY : (mode === "warm" ? WARM : CREAM) };
  if (eb) eyebrow(s, eb);
  if (title) s.addText(title, { x: 0.75, y: 1.0, w: 11.8, h: 0.85, fontFace: SER, fontSize: 28, bold: true, color: isDark ? "FFFFFF" : NAVY, margin: 0 });
  motif(s, isDark); pageno(s, N, isDark);
  return s;
}
function hairline(s, y, dark) {
  s.addShape(pres.ShapeType.line, { x: 0.75, y: y, w: 11.8, h: 0, line: { color: dark ? "2E4160" : LINE, width: 1 } });
}

/* 01 — COVER */
{
  const s = slide("dark");
  s.addText("The largest transfer of wealth\nin history is being handled\nby attorneys.",
    { x: 0.9, y: 1.85, w: 11.3, h: 2.7, fontFace: SER, fontSize: 37, bold: true, color: "FFFFFF", lineSpacing: 51, margin: 0 });
  s.addShape(pres.ShapeType.line, { x: 0.95, y: 4.8, w: 2.0, h: 0, line: { color: GOLD, width: 2.5 } });
  s.addText("VISIONARY GENEROSITY", { x: 0.9, y: 5.05, w: 10, h: 0.4, fontFace: SER, fontSize: 15, bold: true, color: GOLD, charSpacing: 2, margin: 0 });
  s.addText("A book, a framework, and a way to reach the families holding it", { x: 0.9, y: 5.5, w: 10, h: 0.4, fontFace: SER, fontSize: 15, italic: true, color: PALE, margin: 0 });
  s.addText("Developing with The Signatry  ·  Concept stage  ·  August 2026", { x: 0.9, y: 6.4, w: 10, h: 0.3, fontFace: SAN, fontSize: 10, color: "8C8578", margin: 0 });
  s.addNotes("Open on the problem, never on the book. If the first thing a donor hears is 'we wrote a book,' the conversation is already about us.");
}

/* 02 — THE PROBLEM — numbered stack, no cards */
{
  const s = slide("light", "The problem", "What is actually happening");
  const items = [
    ["Trillions are in motion", "Assets are moving between generations at a scale without precedent. Nearly all the professional energy around it aims at minimizing tax and preserving principal."],
    ["Values do not transfer automatically", "Estate plans move assets. They have never once moved a conviction. Families receive capital with no account of what it was for."],
    ["A generation of owners is exiting at once", "The eighteen months around a business sale determine the next thirty years of a family's giving — and almost nobody prepares an owner for them."]
  ];
  items.forEach((it, i) => {
    const y = 2.25 + i * 1.42;
    s.addText(String(i + 1).padStart(2, "0"), { x: 0.75, y: y, w: 1.0, h: 0.6, fontFace: SER, fontSize: 30, bold: true, color: GOLD, margin: 0 });
    s.addText(it[0], { x: 2.0, y: y + 0.02, w: 4.4, h: 0.9, fontFace: SER, fontSize: 17, bold: true, color: NAVY, margin: 0 });
    s.addText(it[1], { x: 6.7, y: y, w: 5.85, h: 1.1, fontFace: SAN, fontSize: 12.5, color: CHAR, lineSpacing: 19, margin: 0 });
    hairline(s, y + 1.18);
  });
  s.addNotes("Speak in orders of magnitude until figures are verified with The Signatry. No invented statistics.");
}

/* 03 — CREDIT THE FIELD */
{
  const s = slide("warm", "What is already working", "The hard argument has been won");
  s.addText("Nothing here is a critique of this field. Several of these organizations shaped every conviction in the book, and their leaders are the people we most want to endorse it.",
    { x: 0.75, y: 1.95, w: 10.8, h: 0.6, fontFace: SAN, fontSize: 13.5, color: MUTE, margin: 0 });
  const four = [
    ["Generous Giving", "A room with no ask produces honesty no solicitation ever has. Privately funded since 2000 so it never has to ask."],
    ["National Christian Foundation", "Built asset-based giving into an institution, and taught a generation that the checkbook is the smallest room in the house."],
    ["The Gathering", "Proved that generous families do better work in each other's company than they ever do alone."],
    ["Ron Blue · Randy Alcorn", "Settled the theology. Ownership is the root question, and the heart follows the treasure rather than leading it."]
  ];
  const w = (11.8 - 0.9) / 4;
  four.forEach((f, i) => {
    const x = 0.75 + i * (w + 0.3);
    s.addShape(pres.ShapeType.line, { x: x, y: 2.85, w: w, h: 0, line: { color: GOLD, width: 2 } });
    s.addText(f[0], { x: x, y: 3.0, w: w, h: 0.75, fontFace: SER, fontSize: 14, bold: true, color: NAVY, margin: 0 });
    s.addText(f[1], { x: x, y: 3.85, w: w, h: 2.0, fontFace: SAN, fontSize: 11.5, color: CHAR, lineSpacing: 17, margin: 0 });
  });
}

/* 04 — THE GAP — big numerals */
{
  const s = slide("light", "The gap", "Three things nobody has built");
  const g = [
    ["The mechanism", "Families are told to be generous and never shown how, when nine-tenths of what they own is illiquid. Conviction without mechanism produces guilt, not gifts."],
    ["The vision half", "Every book addresses the heart. Almost none addresses sight — and a family gives in proportion to what it believes is at stake, not to what it holds."],
    ["A finish", "Donors are handed perpetual need. Nobody offers a finishable assignment, which is the only frame that reorganizes a balance sheet."]
  ];
  const w = (11.8 - 0.8) / 3;
  g.forEach((it, i) => {
    const x = 0.75 + i * (w + 0.4);
    s.addText("0" + (i + 1), { x: x, y: 2.2, w: w, h: 1.1, fontFace: SER, fontSize: 56, bold: true, color: "E3DCCC", margin: 0 });
    s.addText(it[0], { x: x, y: 3.35, w: w, h: 0.5, fontFace: SER, fontSize: 19, bold: true, color: NAVY, margin: 0 });
    s.addShape(pres.ShapeType.line, { x: x, y: 3.95, w: 1.1, h: 0, line: { color: GOLD, width: 2 } });
    s.addText(it[1], { x: x, y: 4.15, w: w, h: 1.9, fontFace: SAN, fontSize: 12.5, color: CHAR, lineSpacing: 20, margin: 0 });
  });
  s.addNotes("These three are the whole case. Everything after this slide is instrumentation.");
}

/* 05 — FRAMEWORK */
{
  const s = slide("light", "The instrument", "Two engines drive generosity");
  s.addShape(pres.ShapeType.ellipse, { x: 2.4, y: 2.35, w: 4.3, h: 3.1, fill: { color: "FFFFFF" }, line: { color: NAVY, width: 2 } });
  s.addShape(pres.ShapeType.ellipse, { x: 6.1, y: 2.35, w: 4.3, h: 3.1, fill: { color: "FFFFFF", transparency: 45 }, line: { color: GOLD, width: 2 } });
  s.addText("VISION", { x: 2.7, y: 3.15, w: 2.5, h: 0.4, fontFace: SER, fontSize: 17, bold: true, color: NAVY, align: "center", charSpacing: 1, margin: 0 });
  s.addText("what a family can see,\nand how big it is", { x: 2.7, y: 3.62, w: 2.5, h: 0.9, fontFace: SAN, fontSize: 11.5, color: CHAR, align: "center", lineSpacing: 17, margin: 0 });
  s.addText("OBEDIENCE", { x: 7.6, y: 3.15, w: 2.5, h: 0.4, fontFace: SER, fontSize: 17, bold: true, color: GOLD, align: "center", charSpacing: 1, margin: 0 });
  s.addText("willingness to act before\nthe outcome is visible", { x: 7.6, y: 3.62, w: 2.5, h: 0.9, fontFace: SAN, fontSize: 11.5, color: CHAR, align: "center", lineSpacing: 17, margin: 0 });
  s.addText("CATALYTIC", { x: 5.45, y: 3.72, w: 1.8, h: 0.4, fontFace: SER, fontSize: 11.5, bold: true, color: NAVY, align: "center", margin: 0 });
  hairline(s, 5.95);
  s.addText("Teachable in ninety seconds. It is the durable asset here — it outlives the book.",
    { x: 0.75, y: 6.1, w: 11.8, h: 0.4, fontFace: SAN, fontSize: 12.5, italic: true, color: MUTE, align: "center", margin: 0 });
}

/* 06 — WHAT IS BEING BUILT */
{
  const s = slide("warm", "What we are building", "The book is the front door, not the product");
  const b = [
    ["The book", "Eighteen chapters, three drafted. Historical patrons paired with living families whose numbers can be examined — plus the mechanics no other book supplies."],
    ["The workshop", "Five sessions, participant guide and teaching script complete. Church, advisor, family-office and overnight editions. Nobody is ever asked for anything."],
    ["The instruments", "A giving statement workbook, a family conversation guide, a liquidity worksheet, twenty-one days of prayer prompts. All drafted."],
    ["The campaign", "A forty-day congregational adaptation, carried through LifeTogether's existing church relationships."]
  ];
  b.forEach((it, i) => {
    const col = i % 2, row = Math.floor(i / 2);
    const x = 0.75 + col * 6.05, y = 2.2 + row * 2.15;
    s.addText(it[0], { x: x, y: y, w: 5.4, h: 0.5, fontFace: SER, fontSize: 18, bold: true, color: NAVY, margin: 0 });
    s.addShape(pres.ShapeType.line, { x: x, y: y + 0.58, w: 1.1, h: 0, line: { color: GOLD, width: 2 } });
    s.addText(it[1], { x: x, y: y + 0.78, w: 5.4, h: 1.3, fontFace: SAN, fontSize: 12.5, color: CHAR, lineSpacing: 19, margin: 0 });
  });
}

/* 07 — REACH */
{
  const s = slide("light", "How it travels", "Three channels that already exist");
  const ch = [
    ["Advisors", "The fastest route in the category. They already hold the relationship and the trust; most have simply never been given the question to ask."],
    ["Churches", "Twenty-five years of LifeTogether relationships. Pastors want to disciple their high-capacity families and have no material for it."],
    ["Families", "Peer to peer, in ask-free rooms. The slowest channel, and the one that produces the most durable change."]
  ];
  ch.forEach((c, i) => {
    const y = 2.3 + i * 1.35;
    s.addText(c[0], { x: 0.75, y: y, w: 2.6, h: 0.5, fontFace: SER, fontSize: 19, bold: true, color: NAVY, margin: 0 });
    s.addText(c[1], { x: 3.7, y: y - 0.05, w: 8.85, h: 1.0, fontFace: SAN, fontSize: 13, color: CHAR, lineSpacing: 20, margin: 0 });
    hairline(s, y + 1.1);
  });
  s.addText("We are not proposing to build an audience. We are proposing to serve people who already own one.",
    { x: 0.75, y: 6.2, w: 11.8, h: 0.4, fontFace: SER, fontSize: 14, italic: true, color: GOLD, margin: 0 });
}

/* 08 — THE PIVOT */
{
  const s = slide("dark", "The ask, stated plainly");
  s.addText("We are not asking anyone\nto fund a book.", { x: 0.9, y: 1.75, w: 11.3, h: 1.7, fontFace: SER, fontSize: 38, bold: true, color: "FFFFFF", lineSpacing: 50, margin: 0 });
  s.addShape(pres.ShapeType.line, { x: 0.95, y: 3.75, w: 2.0, h: 0, line: { color: GOLD, width: 2.5 } });
  s.addText("A publisher pays for a book. A publisher will not pay for the six missing stories, for putting the material into the hands of pastors and advisors who cannot buy it, for training facilitators, or for carrying it outside the English-speaking world.",
    { x: 0.9, y: 4.05, w: 10.4, h: 1.5, fontFace: SAN, fontSize: 15, color: PALE, lineSpacing: 25, margin: 0 });
  s.addText("Those four things are the multiplication.", { x: 0.9, y: 5.65, w: 10.4, h: 0.5, fontFace: SER, fontSize: 17, italic: true, color: GOLD, margin: 0 });
  s.addNotes("This slide is the whole meeting. Do not soften it, and do not put a number on it before this has landed.");
}

/* 09 — WORKSTREAMS */
{
  const s = slide("light", "Where a gift goes", "Four workstreams");
  const ws = [
    ["Sourcing", "Six missing stories — three at ordinary income levels, three from outside the US and UK. Field time, interviews, translation, permissions.", "Without these the book proves a narrower claim than it makes."],
    ["Distribution", "Copies into the hands of pastors and advisors who will use the material and would not buy it.", "Measured in placements that convert to workshops, not units shipped."],
    ["Facilitator training", "Certification for the first cohort of facilitators.", "Certification protects the no-ask discipline as the workshop outgrows its authors."],
    ["Global editions", "Translation and cultural adaptation beyond English.", "The next decade of growth is more likely global than American."]
  ];
  ws.forEach((w, i) => {
    const y = 2.15 + i * 1.15;
    s.addText(w[0], { x: 0.75, y: y, w: 2.5, h: 0.5, fontFace: SER, fontSize: 15, bold: true, color: NAVY, margin: 0 });
    s.addText(w[1], { x: 3.45, y: y - 0.02, w: 5.3, h: 0.9, fontFace: SAN, fontSize: 11.5, color: CHAR, lineSpacing: 17, margin: 0 });
    s.addText(w[2], { x: 9.0, y: y - 0.02, w: 3.55, h: 0.9, fontFace: SAN, fontSize: 11, italic: true, color: MUTE, lineSpacing: 17, margin: 0 });
    hairline(s, y + 0.95);
  });
  s.addText("Scope by workstream is defined. Budget to be set with The Signatry before external use.",
    { x: 0.75, y: 6.85, w: 11.8, h: 0.3, fontFace: SAN, fontSize: 9.5, italic: true, color: MUTE, margin: 0 });
}

/* 10 — MEASUREMENT */
{
  const s = slide("warm", "Measurement", "What we will report, and what we won't");
  const cols = [
    ["We will report", "Stories sourced and permissioned.\nWorkshops held, and where.\nFacilitators certified.\nCopies placed with pastors and advisors.\nTranslations completed.\n\nEvery number independently verifiable.", NAVY],
    ["We will not claim", "Dollars moved as a result of this work.\n\nWe cannot attribute a family's giving to a book they read, and any organization telling you otherwise is selling you a number it invented.", GOLD]
  ];
  cols.forEach((c, i) => {
    const x = 0.75 + i * 6.05;
    s.addText(c[0], { x: x, y: 2.2, w: 5.4, h: 0.5, fontFace: SER, fontSize: 19, bold: true, color: c[2], margin: 0 });
    s.addShape(pres.ShapeType.line, { x: x, y: 2.8, w: 5.4, h: 0, line: { color: LINE, width: 1 } });
    s.addText(c[1], { x: x, y: 3.0, w: 5.4, h: 2.6, fontFace: SAN, fontSize: 12.5, color: CHAR, lineSpacing: 21, margin: 0 });
  });
  s.addText("At twelve months we will ask families three anonymous, voluntary questions: did you set a finish line, did you give a non-cash asset for the first time, did your family hold the conversation.",
    { x: 0.75, y: 5.95, w: 11.8, h: 0.7, fontFace: SAN, fontSize: 12, italic: true, color: MUTE, lineSpacing: 19, margin: 0 });
  s.addNotes("The refusal to overclaim is the credibility of this slide. A donor at this level has heard inflated attribution before and will notice its absence.");
}

/* 11 — TEAM */
{
  const s = slide("light", "The team", "Conviction and mechanics, in one place");
  const t = [
    ["Steve French", "President and CEO, The Signatry", "Built and sold a company before he ever ran a foundation. Names a business failure, not a success, as the moment the ownership question was settled for him."],
    ["Dale Armstrong", "Chief Revenue Officer, The Signatry", "Nearly three decades in development and advancement — a career spent in the rooms where the generosity question either gets asked or doesn't."],
    ["LifeTogether", "Curriculum and campaigns", "Twenty-five years of churchwide campaigns and small-group curriculum, with existing relationships across hundreds of churches. Figures to be verified before external use."]
  ];
  const w = (11.8 - 0.8) / 3;
  t.forEach((p, i) => {
    const x = 0.75 + i * (w + 0.4);
    s.addText(p[0], { x: x, y: 2.3, w: w, h: 0.5, fontFace: SER, fontSize: 19, bold: true, color: NAVY, margin: 0 });
    s.addText(p[1], { x: x, y: 2.85, w: w, h: 0.4, fontFace: SAN, fontSize: 11, color: GOLD, margin: 0 });
    s.addShape(pres.ShapeType.line, { x: x, y: 3.35, w: 1.1, h: 0, line: { color: LINE, width: 1.5 } });
    s.addText(p[2], { x: x, y: 3.55, w: w, h: 2.2, fontFace: SAN, fontSize: 12.5, color: CHAR, lineSpacing: 20, margin: 0 });
  });
}

/* 12 — RISKS */
{
  const s = slide("light", "Risks, stated", "What could go wrong");
  const r = [
    ["It reads as a house book", "Written by a fund sponsor's leadership, it could be dismissed as promotional.", "No vehicle sold in the manuscript. Mechanics confined to appendices. Endorsements sought from organizations that compete with The Signatry."],
    ["The stories don't clear", "Several anchors depend on permissions held by other institutions.", "Permissions opened before drafting rather than after, with an alternate identified for every anchor."],
    ["The workshop scales badly", "The no-ask rule is easy to state and easy to break under commercial pressure.", "Certification required for eighteen months before any open release."]
  ];
  r.forEach((x, i) => {
    const y = 2.25 + i * 1.45;
    s.addText(x[0], { x: 0.75, y: y, w: 3.1, h: 0.8, fontFace: SER, fontSize: 15, bold: true, color: NAVY, margin: 0 });
    s.addText(x[1], { x: 4.1, y: y, w: 3.8, h: 1.0, fontFace: SAN, fontSize: 12, color: CHAR, lineSpacing: 18, margin: 0 });
    s.addText(x[2], { x: 8.2, y: y, w: 4.35, h: 1.1, fontFace: SAN, fontSize: 11.5, italic: true, color: MUTE, lineSpacing: 18, margin: 0 });
    hairline(s, y + 1.2);
  });
  s.addText("MITIGATION →", { x: 8.2, y: 1.9, w: 4.35, h: 0.3, fontFace: SER, fontSize: 9.5, color: GOLD, charSpacing: 2, margin: 0 });
}

/* 13 — STEWARDSHIP */
{
  const s = slide("warm", "Stewardship", "How a gift would be held");
  const st = [
    ["No solicitation inside the work", "Not in the book, not in a workshop, not in a follow-up call. A partner's gift funds the work; it does not buy access to the room."],
    ["Restricted by workstream", "Funds tracked against the four workstreams and reported against them, rather than absorbed into general operations."],
    ["Named or anonymous — your choice", "There is a chapter in this book arguing that anonymity protects the giver. We would be embarrassed to ask you to violate it."]
  ];
  st.forEach((x, i) => {
    const y = 2.35 + i * 1.4;
    s.addText(x[0], { x: 0.75, y: y, w: 4.6, h: 0.8, fontFace: SER, fontSize: 16, bold: true, color: NAVY, margin: 0 });
    s.addText(x[1], { x: 5.8, y: y - 0.02, w: 6.75, h: 1.1, fontFace: SAN, fontSize: 12.5, color: CHAR, lineSpacing: 20, margin: 0 });
    hairline(s, y + 1.15);
  });
}

/* 14 — CLOSE */
{
  const s = slide("dark");
  s.addText("What would be true\nwhen the work is done?", { x: 0.9, y: 2.25, w: 11.3, h: 1.8, fontFace: SER, fontSize: 37, bold: true, color: "FFFFFF", lineSpacing: 51, margin: 0 });
  s.addShape(pres.ShapeType.line, { x: 0.95, y: 4.35, w: 2.0, h: 0, line: { color: GOLD, width: 2.5 } });
  s.addText("A family that adopts an ending stops asking how much to give this year and starts asking when the work could be finished. That question reorganizes a balance sheet faster than any sermon.",
    { x: 0.9, y: 4.6, w: 10.2, h: 1.2, fontFace: SAN, fontSize: 15, color: PALE, lineSpacing: 25, margin: 0 });
  s.addText("Concept stage. No agreement in place with any publisher. Nothing in this document implies endorsement by any organization named.",
    { x: 0.9, y: 6.4, w: 11.3, h: 0.3, fontFace: SAN, fontSize: 9.5, italic: true, color: "8C8578", margin: 0 });
  s.addNotes("Close on the question, not on the ask. If slide 8 landed it does not need repeating.");
}

pres.writeFile({ fileName: "/mnt/user-data/outputs/Visionary-Generosity-Donor-Presentation.pptx" }).then(() => console.log("ok"));
