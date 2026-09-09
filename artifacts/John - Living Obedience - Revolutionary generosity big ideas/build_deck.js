const pptxgen = require("pptxgenjs");

const NAVY = "12253F";
const CREAM = "FAF7F0";
const GOLD = "B08B3F";
const CHAR = "2B2B2B";
const MUTE = "6E6A62";
const LINE = "D8D0C2";

const pres = new pptxgen();
pres.layout = "LAYOUT_WIDE";
pres.author = "LifeTogether";
pres.title = "Visionary Generosity — Publisher Proposal";

const W = 13.3, H = 7.5;

// two-engine motif: one filled dot, one outlined dot
function motif(s, color) {
  s.addShape(pres.ShapeType.ellipse, { x: 0.7, y: 6.85, w: 0.13, h: 0.13, fill: { color: color || GOLD } });
  s.addShape(pres.ShapeType.ellipse, { x: 0.92, y: 6.85, w: 0.13, h: 0.13, fill: { color: "FFFFFF", transparency: 100 }, line: { color: color || GOLD, width: 1 } });
}

function eyebrow(s, txt, color) {
  s.addText(txt.toUpperCase(), { x: 0.7, y: 0.55, w: 8, h: 0.3, fontFace: "Georgia", fontSize: 10, color: color || GOLD, charSpacing: 3, margin: 0 });
}

function light(title, eb) {
  const s = pres.addSlide();
  s.background = { color: CREAM };
  if (eb) eyebrow(s, eb);
  if (title) s.addText(title, { x: 0.7, y: 0.95, w: 11.9, h: 0.9, fontFace: "Georgia", fontSize: 30, bold: true, color: NAVY, margin: 0 });
  motif(s);
  return s;
}

function dark(eb) {
  const s = pres.addSlide();
  s.background = { color: NAVY };
  if (eb) eyebrow(s, eb, GOLD);
  motif(s, GOLD);
  return s;
}

function rule(s, y) {
  s.addShape(pres.ShapeType.line, { x: 0.7, y: y, w: 11.9, h: 0, line: { color: LINE, width: 1 } });
}

function cards(s, items, y, h) {
  const n = items.length;
  const gap = 0.3;
  const w = (11.9 - gap * (n - 1)) / n;
  items.forEach((it, i) => {
    const x = 0.7 + i * (w + gap);
    s.addShape(pres.ShapeType.rect, { x: x, y: y, w: w, h: h, fill: { color: "FFFFFF" }, line: { color: LINE, width: 1 } });
    s.addText(it.h, { x: x + 0.25, y: y + 0.28, w: w - 0.5, h: 0.6, fontFace: "Georgia", fontSize: 14, bold: true, color: NAVY, margin: 0 });
    s.addText(it.b, { x: x + 0.25, y: y + 0.95, w: w - 0.5, h: h - 1.2, fontFace: "Calibri", fontSize: 11.5, color: CHAR, lineSpacing: 17, margin: 0 });
  });
}

/* 1 — TITLE */
{
  const s = dark();
  s.addText("VISIONARY", { x: 0.9, y: 2.0, w: 11.5, h: 0.95, fontFace: "Georgia", fontSize: 54, bold: true, color: "FFFFFF", charSpacing: 1, margin: 0 });
  s.addText("GENEROSITY", { x: 0.9, y: 2.85, w: 11.5, h: 0.95, fontFace: "Georgia", fontSize: 54, bold: true, color: GOLD, charSpacing: 1, margin: 0 });
  s.addShape(pres.ShapeType.line, { x: 0.95, y: 4.05, w: 2.2, h: 0, line: { color: GOLD, width: 2 } });
  s.addText("How Big Vision and a Settled Yes Fund the Work of God", { x: 0.9, y: 4.3, w: 9.5, h: 0.5, fontFace: "Georgia", fontSize: 17, italic: true, color: "E6E0D4", margin: 0 });
  s.addText("Steve French with Dale Armstrong  ·  The Signatry", { x: 0.9, y: 5.0, w: 9.5, h: 0.35, fontFace: "Calibri", fontSize: 13, color: "B9B2A4", margin: 0 });
  s.addText("Publisher proposal  ·  Concept stage  ·  August 2026", { x: 0.9, y: 6.4, w: 9.5, h: 0.3, fontFace: "Calibri", fontSize: 10.5, color: "8C8578", margin: 0 });
  s.addNotes("Status is on the title slide on purpose. Nothing here implies a signed agreement.");
}

/* 2 — PREMISE */
{
  const s = light(null, "The book in one sentence");
  s.addText("Two engines drive generosity, and almost every book on the subject runs on only one.", { x: 0.9, y: 1.9, w: 11.4, h: 1.8, fontFace: "Georgia", fontSize: 30, color: NAVY, lineSpacing: 44, margin: 0 });
  rule(s, 4.1);
  s.addText("Vision is the pull — what a family can see, and how big it is. Obedience is the yes — the willingness to act before the outcome is visible. Vision without obedience produces talk. Obedience without vision produces faithfulness that never becomes catalytic.", { x: 0.9, y: 4.4, w: 10.6, h: 1.6, fontFace: "Calibri", fontSize: 15, color: CHAR, lineSpacing: 25, margin: 0 });
}

/* 3 — THE CATEGORY PROBLEM */
{
  const s = light("What the category keeps doing", "The gap");
  s.addText("Christian giving books argue for a percentage, a heart change, or a cause. Three things almost none of them do:", { x: 0.7, y: 2.0, w: 11.5, h: 0.6, fontFace: "Calibri", fontSize: 14.5, color: MUTE, margin: 0 });
  cards(s, [
    { h: "Explain the mechanism", b: "Nine-tenths of wealth sits outside cash. Almost all giving comes out of the checking account. Few books ever explain why, or what to do about it." },
    { h: "Criticize their own field", b: "The industry reports dollars raised and assets held — both inputs. A book from inside that field, saying so, does not currently exist." },
    { h: "Offer an ending", b: "Readers are handed perpetual need. Nobody offers a finishable assignment, which is the only frame that reorganizes a balance sheet." }
  ], 2.85, 3.4);
}

/* 4 — THESIS */
{
  const s = dark("The argument");
  s.addText("Diagnosis, then mechanism.", { x: 0.9, y: 1.5, w: 11.4, h: 0.8, fontFace: "Georgia", fontSize: 30, bold: true, color: "FFFFFF", margin: 0 });
  const rows = [
    ["VISION", "What a family can see. Sight precedes assignment — in Scripture and in every case study in the book.", "Fails alone as: talk, deferred gifts, buildings with a name on them."],
    ["OBEDIENCE", "The settled yes. Not compliance — ob-audire, to listen toward. Proximity, not rule-keeping.", "Fails alone as: faithful, scattered giving that never becomes catalytic."]
  ];
  rows.forEach((r, i) => {
    const y = 2.6 + i * 1.85;
    s.addText(r[0], { x: 0.9, y: y, w: 2.6, h: 0.4, fontFace: "Georgia", fontSize: 18, bold: true, color: GOLD, margin: 0 });
    s.addText(r[1], { x: 3.7, y: y, w: 5.0, h: 1.4, fontFace: "Calibri", fontSize: 13, color: "E6E0D4", lineSpacing: 21, margin: 0 });
    s.addText(r[2], { x: 8.9, y: y, w: 3.6, h: 1.4, fontFace: "Calibri", fontSize: 12, italic: true, color: "9A9285", lineSpacing: 20, margin: 0 });
  });
  s.addShape(pres.ShapeType.line, { x: 0.9, y: 4.35, w: 11.5, h: 0, line: { color: "2E4160", width: 1 } });
}

/* 5 — WHY NOW */
{
  const s = light("Three reasons the timing is right", "Why now");
  cards(s, [
    { h: "The transfer", b: "Tens of trillions are moving between generations over the next two decades, handled almost entirely by attorneys. No one is treating it as a discipleship event." },
    { h: "The owners", b: "A generation of Christian business owners is reaching exit age simultaneously. The eighteen months around a sale determine the next thirty years of their giving." },
    { h: "The advisors", b: "Kingdom-minded advisory has matured into a real channel. It did not exist at this scale when the category's foundational books were written." }
  ], 2.1, 3.7);
}

/* 6 — AUTHORS */
{
  const s = light("Conviction and mechanics, in one book", "The authors");
  cards(s, [
    { h: "Steve French", b: "President and CEO of The Signatry. Built and sold a legal-technology company working with firms in more than a dozen countries. Names a business failure, not a success, as the moment the ownership question was settled for him. Works daily on non-liquid asset giving with owners and attorneys." },
    { h: "Dale Armstrong", b: "Chief Revenue Officer at The Signatry. Nearly three decades in development and university advancement before joining. Has spent a career on the other side of the table, in the rooms where the generosity question either gets asked or doesn't." }
  ], 2.1, 3.7);
  s.addText("Platform figures to be verified with The Signatry before submission.", { x: 0.7, y: 6.05, w: 11.5, h: 0.3, fontFace: "Calibri", fontSize: 10.5, italic: true, color: MUTE, margin: 0 });
}

/* 7 — READER */
{
  const s = light("Who this is written for", "The reader");
  const rows = [
    ["Owners approaching an exit", "Within five years of a sale. The highest-stakes, least-served reader in the category."],
    ["Families two years past one", "Liquid, purposeless, and quietly guarding a pile. Nobody has written for this moment."],
    ["Households with assets and no plan", "More than they need, and no framework for deciding what it is for."],
    ["Advisors and their clients", "The distribution channel that already owns the relationship and the trust."]
  ];
  rows.forEach((r, i) => {
    const y = 2.15 + i * 1.05;
    s.addShape(pres.ShapeType.rect, { x: 0.7, y: y, w: 11.9, h: 0.9, fill: { color: "FFFFFF" }, line: { color: LINE, width: 1 } });
    s.addText(r[0], { x: 1.0, y: y + 0.16, w: 4.3, h: 0.6, fontFace: "Georgia", fontSize: 14, bold: true, color: NAVY, margin: 0 });
    s.addText(r[1], { x: 5.5, y: y + 0.2, w: 6.8, h: 0.6, fontFace: "Calibri", fontSize: 12.5, color: CHAR, margin: 0 });
  });
}

/* 8 — COMPETITION */
{
  const s = light("What it is not", "The competitive set");
  const rows = [
    ["Gospel Patrons — Rinehart", "History of three patrons. Ours pairs them with living families and supplies the mechanism he doesn't."],
    ["The Treasure Principle — Alcorn", "The heart argument, made in ninety pages. Ours starts where his ends and adds the vision half."],
    ["Infectious Generosity — Anderson", "Secular, about spread. Ours is about compounding, and it is explicitly Christian."],
    ["Generous Giving / NCF content", "Experience and education, not a book. Both are endorsers before they are competitors."]
  ];
  rows.forEach((r, i) => {
    const y = 2.15 + i * 1.05;
    s.addText(r[0], { x: 0.7, y: y, w: 4.6, h: 0.5, fontFace: "Georgia", fontSize: 14, bold: true, color: NAVY, margin: 0 });
    s.addText(r[1], { x: 5.5, y: y, w: 7.1, h: 0.8, fontFace: "Calibri", fontSize: 12.5, color: CHAR, lineSpacing: 19, margin: 0 });
    s.addShape(pres.ShapeType.line, { x: 0.7, y: y + 0.9, w: 11.9, h: 0, line: { color: LINE, width: 1 } });
  });
}

/* 9 — STRUCTURE */
{
  const s = light("Four parts, sixteen chapters, 64,000 words", "Structure");
  const parts = [
    { h: "I · The Two Engines", b: "Ch 1–4. The plateau, the prophetic question, the settled yes, and the failure mode: vision without obedience becomes empire." },
    { h: "II · Where Vision Comes From", b: "Ch 5–8. Proximity, the size of the assignment, God's rate of return, and vision as something given rather than generated." },
    { h: "III · The Patron's Craft", b: "Ch 9–12. Back the person, fund before it's provable, fund the unglamorous middle, stay behind the curtain." },
    { h: "IV · A Family That Can Say Yes", b: "Ch 13–16. Capacity, speed, the family that sees together, and the last check." }
  ];
  cards(s, parts, 2.1, 3.7);
}

/* 10 — SAMPLES */
{
  const s = light("Two chapters drafted", "Samples available");
  cards(s, [
    { h: "Ch 7 · God's Rate of Return", b: "The argument chapter. Reframes giving from subtraction to allocation, makes the book's original exegetical turn on the parable of the sower, and places the anti-prosperity guardrail mid-chapter rather than in a footnote." },
    { h: "Ch 3 · Counting the Wrong Things", b: "The credibility chapter. A donor-advised-fund CEO argues that his own industry reports the wrong numbers — dollars raised and assets held are both inputs. Included so a reader can see the authors criticize their own field." }
  ], 2.1, 3.5);
  s.addText("Both are attached in full.", { x: 0.7, y: 5.85, w: 11.5, h: 0.3, fontFace: "Calibri", fontSize: 12, italic: true, color: MUTE, margin: 0 });
}

/* 11 — EVIDENCE */
{
  const s = light("Documented, permissioned, and testable", "The evidence base");
  s.addText("Every story in the manuscript is drawn from published material. Nothing is reconstructed and no quotation is invented.", { x: 0.7, y: 2.0, w: 11.5, h: 0.6, fontFace: "Calibri", fontSize: 14, color: MUTE, margin: 0 });
  cards(s, [
    { h: "Historical", b: "Monmouth and Tyndale. Lady Huntingdon and Whitefield. Thornton and Newton. Public domain." },
    { h: "Mid-century", b: "R.G. LeTourneau's reversed tithe. Stanley Tam's transfer of ownership. Widely published." },
    { h: "Living families", b: "Barnhart, Green, Haverkamp, Trogden, and four-generation Signatry families. Permissions in process." },
    { h: "The authors", b: "French's failure and his own exit regret, distributed across chapters 1, 13, and 16." }
  ], 2.8, 3.3);
}

/* 12 — PLATFORM */
{
  const s = light("The book is the front door, not the product", "Platform");
  const rows = [
    ["Two Engines workshop", "Four sessions, participant guide and teaching script complete. Church, advisor, family-office, and overnight editions."],
    ["Four participant tools", "Kingdom Giving Statement, family conversation guide, legacy and liquidity worksheet, twenty-one days of prayer prompts. Drafted."],
    ["Churchwide campaign", "Forty-day congregational adaptation through LifeTogether's existing church relationships."],
    ["Advisor channel", "The fastest distribution route in the category — advisors already hold the relationship and the trust."]
  ];
  rows.forEach((r, i) => {
    const y = 2.15 + i * 1.05;
    s.addShape(pres.ShapeType.rect, { x: 0.7, y: y, w: 11.9, h: 0.9, fill: { color: "FFFFFF" }, line: { color: LINE, width: 1 } });
    s.addText(r[0], { x: 1.0, y: y + 0.16, w: 3.9, h: 0.6, fontFace: "Georgia", fontSize: 14, bold: true, color: NAVY, margin: 0 });
    s.addText(r[1], { x: 5.1, y: y + 0.13, w: 7.2, h: 0.7, fontFace: "Calibri", fontSize: 12, color: CHAR, lineSpacing: 18, margin: 0 });
  });
}

/* 13 — DERIVATIVES */
{
  const s = light("Derivative rights and the product family", "What follows the book");
  cards(s, [
    { h: "Study guide", b: "Sixteen sessions, three questions and one action step each. Written alongside the manuscript, not after it." },
    { h: "Workbook edition", b: "The four tools bound as a companion volume for family offices and advisor cohorts." },
    { h: "Church campaign", b: "Forty-day adaptation with sermon support, small-group curriculum, and a family edition." },
    { h: "Advisor edition", b: "The mechanism chapters, recut for professionals who need to raise the question with clients." }
  ], 2.1, 3.6);
}

/* 14 — ASK */
{
  const s = dark("The ask");
  s.addText("What we're seeking", { x: 0.9, y: 1.5, w: 11.4, h: 0.8, fontFace: "Georgia", fontSize: 30, bold: true, color: "FFFFFF", margin: 0 });
  const items = [
    ["Editorial partner", "A publisher who wants the category argument, not another stewardship title."],
    ["Timeline", "Manuscript twelve months from agreement. Two chapters drafted; five prioritized for first draft."],
    ["Rights", "Trade rights sought. Curriculum, workshop, and campaign derivatives retained."],
    ["Open decision", "Single narrator recommended, with the second author's material attributed throughout."]
  ];
  items.forEach((r, i) => {
    const y = 2.55 + i * 0.95;
    s.addText(r[0], { x: 0.9, y: y, w: 3.4, h: 0.4, fontFace: "Georgia", fontSize: 15, bold: true, color: GOLD, margin: 0 });
    s.addText(r[1], { x: 4.6, y: y, w: 7.9, h: 0.7, fontFace: "Calibri", fontSize: 13, color: "E6E0D4", lineSpacing: 20, margin: 0 });
  });
  s.addText("Concept stage. No agreement in place with any publisher or co-author as of this document.", { x: 0.9, y: 6.4, w: 11.4, h: 0.3, fontFace: "Calibri", fontSize: 10.5, italic: true, color: "8C8578", margin: 0 });
}

pres.writeFile({ fileName: "/mnt/user-data/outputs/Visionary-Generosity-Publisher-Proposal.pptx" })
  .then(() => console.log("deck written"));
