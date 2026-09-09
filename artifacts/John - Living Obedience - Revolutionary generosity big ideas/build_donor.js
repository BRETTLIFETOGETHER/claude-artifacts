const pptxgen = require("pptxgenjs");

const NAVY = "12253F", CREAM = "FAF7F0", GOLD = "B08B3F", CHAR = "2B2B2B", MUTE = "6E6A62", LINE = "D8D0C2";
const pres = new pptxgen();
pres.layout = "LAYOUT_WIDE";
pres.title = "Visionary Generosity — Donor & Partner Presentation";

function motif(s) {
  s.addShape(pres.ShapeType.ellipse, { x: 0.7, y: 6.85, w: 0.13, h: 0.13, fill: { color: GOLD } });
  s.addShape(pres.ShapeType.ellipse, { x: 0.92, y: 6.85, w: 0.13, h: 0.13, fill: { color: "FFFFFF", transparency: 100 }, line: { color: GOLD, width: 1 } });
}
function eyebrow(s, t) {
  s.addText(t.toUpperCase(), { x: 0.7, y: 0.55, w: 9.5, h: 0.3, fontFace: "Georgia", fontSize: 10, color: GOLD, charSpacing: 3, margin: 0 });
}
function light(title, eb) {
  const s = pres.addSlide(); s.background = { color: CREAM };
  if (eb) eyebrow(s, eb);
  if (title) s.addText(title, { x: 0.7, y: 0.95, w: 11.9, h: 0.9, fontFace: "Georgia", fontSize: 29, bold: true, color: NAVY, margin: 0 });
  motif(s); return s;
}
function dark(eb) {
  const s = pres.addSlide(); s.background = { color: NAVY };
  if (eb) eyebrow(s, eb);
  motif(s); return s;
}
function cards(s, items, y, h, sz) {
  const n = items.length, gap = 0.3, w = (11.9 - gap * (n - 1)) / n;
  items.forEach((it, i) => {
    const x = 0.7 + i * (w + gap);
    s.addShape(pres.ShapeType.rect, { x: x, y: y, w: w, h: h, fill: { color: "FFFFFF" }, line: { color: LINE, width: 1 } });
    s.addText(it.h, { x: x + 0.25, y: y + 0.28, w: w - 0.5, h: 0.62, fontFace: "Georgia", fontSize: 14, bold: true, color: NAVY, margin: 0 });
    s.addText(it.b, { x: x + 0.25, y: y + 0.98, w: w - 0.5, h: h - 1.25, fontFace: "Calibri", fontSize: sz || 11.5, color: CHAR, lineSpacing: 17, margin: 0 });
  });
}
function rows(s, data, y, labelW, gap) {
  data.forEach((r, i) => {
    const yy = y + i * (gap || 1.05);
    s.addShape(pres.ShapeType.rect, { x: 0.7, y: yy, w: 11.9, h: (gap || 1.05) - 0.15, fill: { color: "FFFFFF" }, line: { color: LINE, width: 1 } });
    s.addText(r[0], { x: 1.0, y: yy + 0.16, w: labelW, h: 0.6, fontFace: "Georgia", fontSize: 14, bold: true, color: NAVY, margin: 0 });
    s.addText(r[1], { x: 1.0 + labelW + 0.4, y: yy + 0.13, w: 11.9 - labelW - 1.0, h: (gap || 1.05) - 0.4, fontFace: "Calibri", fontSize: 12, color: CHAR, lineSpacing: 18, margin: 0 });
  });
}

/* 1 — COVER: the opportunity, not the product */
{
  const s = dark();
  s.addText("The largest transfer of wealth\nin history is being handled\nby attorneys.", { x: 0.9, y: 1.9, w: 11.4, h: 2.6, fontFace: "Georgia", fontSize: 38, bold: true, color: "FFFFFF", lineSpacing: 52, margin: 0 });
  s.addShape(pres.ShapeType.line, { x: 0.95, y: 4.75, w: 2.2, h: 0, line: { color: GOLD, width: 2 } });
  s.addText("Visionary Generosity  ·  A book, a framework, and a way to reach the families holding it", { x: 0.9, y: 5.0, w: 10.5, h: 0.5, fontFace: "Georgia", fontSize: 16, italic: true, color: "E6E0D4", margin: 0 });
  s.addText("Developing with The Signatry  ·  Concept stage  ·  August 2026", { x: 0.9, y: 6.35, w: 10.5, h: 0.3, fontFace: "Calibri", fontSize: 10.5, color: "8C8578", margin: 0 });
  s.addNotes("Open on the problem, never on the book. If the first thing a donor hears is 'we wrote a book,' the conversation is already about us.");
}

/* 2 — THE PROBLEM */
{
  const s = light("What is actually happening", "The problem");
  cards(s, [
    { h: "Trillions in motion", b: "Assets are moving between generations on a scale without precedent. Nearly all the professional energy around it is aimed at minimizing tax and preserving principal." },
    { h: "Values do not transfer automatically", b: "Estate plans move assets. They have never once moved a conviction. Families receive capital with no account of what it was for." },
    { h: "A generation of owners is exiting at once", b: "The eighteen months around a business sale determine the next thirty years of a family's giving — and almost nobody prepares an owner for them." }
  ], 2.1, 3.6);
  s.addNotes("Do not use invented statistics. Speak in orders of magnitude until verified figures are agreed with The Signatry.");
}

/* 3 — CREDIT THE FIELD FIRST */
{
  const s = light("The hard argument has already been won", "What is working");
  s.addText("None of what follows is a critique of this field. Several of these organizations have shaped every conviction in the book, and their leaders are the people we most want to endorse it.", { x: 0.7, y: 2.0, w: 11.5, h: 0.7, fontFace: "Calibri", fontSize: 14, color: MUTE, margin: 0 });
  cards(s, [
    { h: "Generous Giving", b: "Proved that a room with no ask produces honesty no solicitation ever has. Privately funded since 2000 precisely so it never has to ask." },
    { h: "National Christian Foundation", b: "Built asset-based giving into an institution, and taught a generation that the checkbook is the smallest room in the house." },
    { h: "The Gathering", b: "Demonstrated that generous families do better work in each other's company than they ever do alone." },
    { h: "Ron Blue · Randy Alcorn", b: "Settled the theology. Ownership is the root question, and the heart follows the treasure rather than leading it." }
  ], 2.85, 3.3);
}

/* 4 — THE GAP */
{
  const s = light("Three things nobody has built", "The gap");
  rows(s, [
    ["The mechanism", "Families are told to be generous and never shown how, when nine-tenths of what they own is illiquid. Conviction without mechanism produces guilt, not gifts."],
    ["The vision half", "Every book addresses the heart. Almost none addresses sight — and a family gives in proportion to what it believes is at stake, not to what it holds."],
    ["A finish", "Donors are handed perpetual need. Nobody offers a finishable assignment, which is the only frame that reorganizes a balance sheet."]
  ], 2.15, 3.1, 1.35);
  s.addNotes("These three are the whole case. Everything after this slide is instrumentation.");
}

/* 5 — THE FRAMEWORK */
{
  const s = light("Two engines drive generosity", "The instrument");
  s.addShape(pres.ShapeType.ellipse, { x: 2.2, y: 2.3, w: 4.4, h: 3.2, fill: { color: "FFFFFF" }, line: { color: NAVY, width: 2 } });
  s.addShape(pres.ShapeType.ellipse, { x: 6.0, y: 2.3, w: 4.4, h: 3.2, fill: { color: "FFFFFF", transparency: 40 }, line: { color: GOLD, width: 2 } });
  s.addText("VISION", { x: 2.5, y: 3.15, w: 2.6, h: 0.4, fontFace: "Georgia", fontSize: 17, bold: true, color: NAVY, align: "center", margin: 0 });
  s.addText("what a family can see,\nand how big it is", { x: 2.5, y: 3.62, w: 2.6, h: 0.9, fontFace: "Calibri", fontSize: 11.5, color: CHAR, align: "center", lineSpacing: 17, margin: 0 });
  s.addText("OBEDIENCE", { x: 7.5, y: 3.15, w: 2.6, h: 0.4, fontFace: "Georgia", fontSize: 17, bold: true, color: GOLD, align: "center", margin: 0 });
  s.addText("willingness to act before\nthe outcome is visible", { x: 7.5, y: 3.62, w: 2.6, h: 0.9, fontFace: "Calibri", fontSize: 11.5, color: CHAR, align: "center", lineSpacing: 17, margin: 0 });
  s.addText("CATALYTIC", { x: 5.35, y: 3.7, w: 1.9, h: 0.4, fontFace: "Georgia", fontSize: 12, bold: true, color: NAVY, align: "center", margin: 0 });
  s.addText("Teachable in ninety seconds. It is the durable asset here — it outlives the book.", { x: 0.7, y: 5.9, w: 11.9, h: 0.4, fontFace: "Calibri", fontSize: 13, italic: true, color: MUTE, align: "center", margin: 0 });
}

/* 6 — WHAT IS BEING BUILT */
{
  const s = light("A book is the front door, not the product", "What we are building");
  cards(s, [
    { h: "The book", b: "Eighteen chapters. Three drafted. Historical patrons paired with living families whose numbers can be examined, plus the mechanics no other book supplies." },
    { h: "The workshop", b: "Five sessions, participant guide and teaching script complete. Church, advisor, family-office, and overnight editions. No one is ever asked for anything." },
    { h: "The instruments", b: "A giving statement workbook, a family conversation guide, a liquidity worksheet, twenty-one days of prayer prompts. All drafted." },
    { h: "The campaign", b: "A forty-day congregational adaptation through LifeTogether's existing church relationships." }
  ], 2.1, 3.6);
}

/* 7 — REACH */
{
  const s = light("Three channels that already exist", "How it travels");
  rows(s, [
    ["Advisors", "The fastest route in the category. Advisors already hold the relationship and the trust; most have simply never been given the question to ask."],
    ["Churches", "LifeTogether has spent twenty-five years in relationship with churches. Pastors want to disciple their high-capacity families and have no material for it."],
    ["Families", "Peer to peer, in ask-free rooms. The slowest channel and the one that produces the most durable change."]
  ], 2.15, 3.1, 1.35);
  s.addText("We are not proposing to build an audience. We are proposing to serve people who already own one.", { x: 0.7, y: 6.15, w: 11.9, h: 0.4, fontFace: "Calibri", fontSize: 13, italic: true, color: MUTE, margin: 0 });
}

/* 8 — THE HONEST PIVOT */
{
  const s = dark("The ask, stated plainly");
  s.addText("We are not asking anyone\nto fund a book.", { x: 0.9, y: 1.7, w: 11.4, h: 1.7, fontFace: "Georgia", fontSize: 36, bold: true, color: "FFFFFF", lineSpacing: 48, margin: 0 });
  s.addText("A publisher pays for a book. A publisher will not pay for the six missing stories, for putting the material into the hands of pastors and advisors who cannot buy it, for training facilitators, or for carrying it outside the English-speaking world.", { x: 0.9, y: 3.8, w: 10.6, h: 1.5, fontFace: "Calibri", fontSize: 15, color: "E6E0D4", lineSpacing: 25, margin: 0 });
  s.addText("Those four things are the multiplication. They are what we are asking a partner to fund.", { x: 0.9, y: 5.5, w: 10.6, h: 0.5, fontFace: "Georgia", fontSize: 16, italic: true, color: GOLD, margin: 0 });
  s.addNotes("This slide is the whole meeting. Do not soften it, and do not put a number on it before the previous slide has landed.");
}

/* 9 — FUNDABLE WORK */
{
  const s = light("Four workstreams", "Where a gift goes");
  rows(s, [
    ["Sourcing", "Six missing stories — three at ordinary income levels, three from outside the US and UK. Field time, interviews, translation, permissions. Without these the book proves a narrower claim than it makes."],
    ["Distribution", "Copies into the hands of pastors and advisors who will use the material and would not buy it. Measured in placements that convert to workshops, not in units shipped."],
    ["Facilitator training", "Certification for the first cohort. Certification is what protects the no-ask discipline as the workshop scales beyond the people who wrote it."],
    ["Global editions", "Translation and cultural adaptation. The next decade of growth in this movement is more likely to come from the global church than from another wave of American exits."]
  ], 2.05, 2.9, 1.18);
  s.addText("Scope by workstream is defined. Budget to be set with The Signatry before this document is used externally.", { x: 0.7, y: 6.9, w: 11.9, h: 0.3, fontFace: "Calibri", fontSize: 10, italic: true, color: MUTE, margin: 0 });
}

/* 10 — MEASUREMENT */
{
  const s = light("What we will report, and what we won't", "Measurement");
  cards(s, [
    { h: "We will report", b: "Stories sourced and permissioned. Workshops held and where. Facilitators certified. Copies placed with pastors and advisors. Translations completed. Every number verifiable." },
    { h: "We will not claim", b: "Dollars moved as a result of this work. We cannot attribute a family's giving to a book they read, and any organization telling you otherwise is selling you a number it invented." },
    { h: "What we will ask families", b: "Anonymous and voluntary, at twelve months: did you set a finish line, did you give a non-cash asset for the first time, did your family hold the conversation." }
  ], 2.1, 3.6);
  s.addNotes("The refusal to overclaim is the credibility of this slide. A donor in this space has heard inflated attribution before and will notice its absence.");
}

/* 11 — WHY THIS TEAM */
{
  const s = light("Conviction and mechanics, in one place", "The team");
  cards(s, [
    { h: "Steve French", b: "President and CEO of The Signatry. Built and sold a company before he ever ran a foundation. Names a business failure, not a success, as the moment the ownership question was settled for him." },
    { h: "Dale Armstrong", b: "Chief Revenue Officer at The Signatry. Nearly three decades in development and advancement — a career spent in the rooms where the generosity question either gets asked or doesn't." },
    { h: "LifeTogether", b: "Twenty-five years building churchwide campaigns and small-group curriculum, with existing relationships across hundreds of churches. Platform figures to be verified before external use." }
  ], 2.1, 3.6);
}

/* 12 — RISKS */
{
  const s = light("What could go wrong", "Risks, stated");
  rows(s, [
    ["It reads as a house book", "Written by a fund sponsor's leadership, it could be dismissed as promotional. Mitigation: no vehicle sold in the manuscript, mechanics confined to appendices, and endorsements sought from organizations that compete with The Signatry."],
    ["The stories don't clear", "Several anchors depend on permissions held by others. Mitigation: permissions opened before drafting rather than after, with an alternate identified for every anchor."],
    ["The workshop scales badly", "The no-ask rule is easy to state and easy to break under commercial pressure. Mitigation: certification for eighteen months before open release."]
  ], 2.15, 3.1, 1.5);
}

/* 13 — STEWARDSHIP */
{
  const s = light("How a gift would be held", "Stewardship");
  rows(s, [
    ["No solicitation inside the work", "Not in the book, not in a workshop, not in a follow-up call. A partner's gift funds the work and does not buy access to the room."],
    ["Restricted by workstream", "Funds tracked against the four workstreams and reported against them, not absorbed into general operations."],
    ["Named or anonymous, your choice", "There is a chapter in this book arguing that anonymity protects the giver. We would be embarrassed to ask you to violate it."]
  ], 2.15, 3.1, 1.35);
}

/* 14 — CLOSE */
{
  const s = dark();
  s.addText("What would be true\nwhen the work is done?", { x: 0.9, y: 2.2, w: 11.4, h: 1.8, fontFace: "Georgia", fontSize: 36, bold: true, color: "FFFFFF", lineSpacing: 50, margin: 0 });
  s.addText("A family that adopts an ending stops asking how much to give this year and starts asking when the work could be finished. That question reorganizes a balance sheet faster than any sermon.", { x: 0.9, y: 4.35, w: 10.4, h: 1.2, fontFace: "Calibri", fontSize: 15, color: "E6E0D4", lineSpacing: 25, margin: 0 });
  s.addText("Concept stage. No agreement in place with any publisher. Nothing in this document implies endorsement by any organization named.", { x: 0.9, y: 6.35, w: 11.4, h: 0.3, fontFace: "Calibri", fontSize: 10, italic: true, color: "8C8578", margin: 0 });
  s.addNotes("Close on the question, not on the ask. If the ask was clear on slide 8 it does not need repeating here.");
}

pres.writeFile({ fileName: "/mnt/user-data/outputs/Visionary-Generosity-Donor-Presentation.pptx" }).then(() => console.log("ok"));
