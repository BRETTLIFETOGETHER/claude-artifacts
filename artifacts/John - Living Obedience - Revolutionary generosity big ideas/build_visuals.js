const pptxgen = require("pptxgenjs");

const NAVY = "12253F", CREAM = "FAF7F0", GOLD = "B08B3F", CHAR = "2B2B2B", MUTE = "6E6A62", LINE = "D8D0C2";
const pres = new pptxgen();
pres.layout = "LAYOUT_WIDE";
pres.title = "Two Engines — Training Visuals";

function motif(s) {
  s.addShape(pres.ShapeType.ellipse, { x: 0.7, y: 6.85, w: 0.13, h: 0.13, fill: { color: GOLD } });
  s.addShape(pres.ShapeType.ellipse, { x: 0.92, y: 6.85, w: 0.13, h: 0.13, fill: { color: "FFFFFF", transparency: 100 }, line: { color: GOLD, width: 1 } });
}
function eyebrow(s, t) {
  s.addText(t.toUpperCase(), { x: 0.7, y: 0.55, w: 9, h: 0.3, fontFace: "Georgia", fontSize: 10, color: GOLD, charSpacing: 3, margin: 0 });
}
function light(title, eb) {
  const s = pres.addSlide(); s.background = { color: CREAM };
  if (eb) eyebrow(s, eb);
  if (title) s.addText(title, { x: 0.7, y: 0.95, w: 11.9, h: 0.9, fontFace: "Georgia", fontSize: 30, bold: true, color: NAVY, margin: 0 });
  motif(s); return s;
}
function dark(eb) {
  const s = pres.addSlide(); s.background = { color: NAVY };
  if (eb) eyebrow(s, eb);
  motif(s); return s;
}
function witness(name, dates, body, kicker, notes) {
  const s = pres.addSlide(); s.background = { color: NAVY };
  eyebrow(s, "witness");
  s.addText(name, { x: 0.9, y: 1.6, w: 11.4, h: 0.85, fontFace: "Georgia", fontSize: 40, bold: true, color: "FFFFFF", margin: 0 });
  s.addText(dates, { x: 0.9, y: 2.5, w: 11.4, h: 0.35, fontFace: "Calibri", fontSize: 13, color: "8C8578", margin: 0 });
  s.addText(body, { x: 0.9, y: 3.15, w: 8.6, h: 1.9, fontFace: "Calibri", fontSize: 16, color: "E6E0D4", lineSpacing: 27, margin: 0 });
  s.addShape(pres.ShapeType.line, { x: 0.95, y: 5.3, w: 2.2, h: 0, line: { color: GOLD, width: 2 } });
  s.addText(kicker, { x: 0.9, y: 5.55, w: 9.5, h: 0.6, fontFace: "Georgia", fontSize: 18, italic: true, color: GOLD, margin: 0 });
  motif(s); s.addNotes(notes);
}

/* 1 title */
{
  const s = dark();
  s.addText("TWO ENGINES", { x: 0.9, y: 2.5, w: 11.5, h: 1.0, fontFace: "Georgia", fontSize: 52, bold: true, color: "FFFFFF", charSpacing: 1, margin: 0 });
  s.addShape(pres.ShapeType.line, { x: 0.95, y: 3.7, w: 2.2, h: 0, line: { color: GOLD, width: 2 } });
  s.addText("Vision, obedience, and the generosity that follows", { x: 0.9, y: 3.95, w: 10, h: 0.5, fontFace: "Georgia", fontSize: 18, italic: true, color: "E6E0D4", margin: 0 });
  s.addText("Training visuals  ·  Advisors, pastors, and giving circles", { x: 0.9, y: 6.35, w: 10, h: 0.3, fontFace: "Calibri", fontSize: 11, color: "8C8578", margin: 0 });
  s.addNotes("Say the no-ask rule out loud in the first three minutes: nobody in this room will be asked for anything.");
}

/* 2 the rule */
{
  const s = light(null, "Before anything else");
  s.addText("Nobody asks for\nanything.", { x: 0.9, y: 2.0, w: 11.4, h: 2.0, fontFace: "Georgia", fontSize: 44, bold: true, color: NAVY, lineSpacing: 56, margin: 0 });
  s.addText("No pledge card. No follow-up call. No vehicle presentation. This is not politeness — it is the reason the room tells the truth. Everyone here has spent years being handled, and they can detect an ask through a wall.", { x: 0.9, y: 4.4, w: 9.8, h: 1.3, fontFace: "Calibri", fontSize: 15, color: CHAR, lineSpacing: 25, margin: 0 });
  s.addNotes("Do not soften this or make a joke of it. Say it and move on.");
}

/* 3 the two engines diagram */
{
  const s = light("Two engines drive generosity", "The framework");
  s.addShape(pres.ShapeType.ellipse, { x: 2.2, y: 2.3, w: 4.4, h: 3.4, fill: { color: "FFFFFF" }, line: { color: NAVY, width: 2 } });
  s.addShape(pres.ShapeType.ellipse, { x: 6.0, y: 2.3, w: 4.4, h: 3.4, fill: { color: "FFFFFF", transparency: 40 }, line: { color: GOLD, width: 2 } });
  s.addText("VISION", { x: 2.5, y: 3.2, w: 2.6, h: 0.4, fontFace: "Georgia", fontSize: 18, bold: true, color: NAVY, align: "center", margin: 0 });
  s.addText("what you can see,\nand how big it is", { x: 2.5, y: 3.7, w: 2.6, h: 0.9, fontFace: "Calibri", fontSize: 12, color: CHAR, align: "center", lineSpacing: 18, margin: 0 });
  s.addText("OBEDIENCE", { x: 7.5, y: 3.2, w: 2.6, h: 0.4, fontFace: "Georgia", fontSize: 18, bold: true, color: GOLD, align: "center", margin: 0 });
  s.addText("willingness to act\nbefore you can see", { x: 7.5, y: 3.7, w: 2.6, h: 0.9, fontFace: "Calibri", fontSize: 12, color: CHAR, align: "center", lineSpacing: 18, margin: 0 });
  s.addText("CATALYTIC", { x: 5.35, y: 3.75, w: 1.9, h: 0.4, fontFace: "Georgia", fontSize: 13, bold: true, color: NAVY, align: "center", margin: 0 });
  s.addText("Vision without obedience produces talk.     ·     Obedience without vision never becomes catalytic.", { x: 0.9, y: 6.05, w: 11.5, h: 0.4, fontFace: "Calibri", fontSize: 13, italic: true, color: MUTE, align: "center", margin: 0 });
  s.addNotes("Draw this on a whiteboard if you can rather than projecting it. The room retains what it watches being built.");
}

/* 4 failure modes */
{
  const s = light("Neither works alone", "Failure modes");
  const items = [
    { h: "Vision, no obedience", b: "Grand plans. Deferred gifts. A foundation that admires its own balance sheet. A wing with the family name above the door.\n\nThe failure is not stinginess. It is empire." },
    { h: "Obedience, no vision", b: "Faithful, consistent, scattered. Responds to whoever asks. Could have funded a movement and never saw one worth funding.\n\nThe failure is not disobedience. It is smallness." }
  ];
  const w = (11.9 - 0.4) / 2;
  items.forEach((it, i) => {
    const x = 0.7 + i * (w + 0.4);
    s.addShape(pres.ShapeType.rect, { x: x, y: 2.2, w: w, h: 3.6, fill: { color: "FFFFFF" }, line: { color: LINE, width: 1 } });
    s.addText(it.h, { x: x + 0.35, y: 2.5, w: w - 0.7, h: 0.5, fontFace: "Georgia", fontSize: 18, bold: true, color: NAVY, margin: 0 });
    s.addText(it.b, { x: x + 0.35, y: 3.15, w: w - 0.7, h: 2.4, fontFace: "Calibri", fontSize: 13.5, color: CHAR, lineSpacing: 21, margin: 0 });
  });
  s.addNotes("Ask the room which one they recognize in themselves. Do not ask them to answer aloud.");
}

/* 5 diagnostic */
{
  const s = light("Which engine is idling?", "The diagnostic");
  const rows = [
    ["I give consistently and could not say what it produced.", "I can describe what I am funding and why."],
    ["I have discussed a major gift for over two years.", "When I decide, I move within weeks."],
    ["My giving responds to requests.", "My giving originates with me."],
    ["I fund from a distance.", "I have visited the work in the last three years."],
    ["My family could not state what we are for.", "My family could state it in a sentence."]
  ];
  rows.forEach((r, i) => {
    const y = 2.15 + i * 0.82;
    s.addText(r[0], { x: 0.7, y: y, w: 5.3, h: 0.6, fontFace: "Calibri", fontSize: 13, color: CHAR, align: "right", margin: 0 });
    s.addText("/", { x: 6.2, y: y, w: 0.5, h: 0.6, fontFace: "Georgia", fontSize: 15, color: GOLD, align: "center", margin: 0 });
    s.addText(r[1], { x: 6.9, y: y, w: 5.6, h: 0.6, fontFace: "Calibri", fontSize: 13, color: CHAR, margin: 0 });
    s.addShape(pres.ShapeType.line, { x: 0.7, y: y + 0.62, w: 11.8, h: 0, line: { color: LINE, width: 1 } });
  });
  s.addNotes("Silent and individual. Five minutes. Do not have anyone share their answers — ask only which engine is idling.");
}

/* 6-11 witnesses */
witness("Humphrey Monmouth", "London cloth merchant · 1520s",
  "Saw an English Bible before one existed. Gave Tyndale money and a room in his own house, then used his merchant ships to move the printed New Testaments back into England.",
  "He paid for the Bible you own, and paid in a cell.",
  "A year in the Tower on more than twenty charges. Tyndale never bore that particular cost.");
witness("Lady Huntingdon", "English aristocrat · 1700s",
  "She could not preach and had no theological contribution to make. What she had was a house and a guest list — and the aristocracy would accept an invitation when they would never stand in a field.",
  "Vision arrives through the position you already hold.",
  "Use this one when the room contains people who think they have nothing to contribute but money.");
witness("John Thornton", "Merchant · 1700s",
  "Backed John Newton when Newton was a customs official with a criminal past and a drawer of unpublished verse. Placed him in a pulpit, gave him counsel and rest, pressed him to publish the hymns.",
  "He did not fund the work. He funded the man.",
  "One of those hymns was Amazing Grace. Let the room make that connection themselves.");
witness("R.G. LeTourneau", "Industrialist · 1888–1969",
  "Seventh-grade education, nearly 300 inventions, and a reversed tithe — ninety percent given, ten percent kept. He began at thirty, deeply in debt, pledging from underneath a six-figure loss.",
  "The extreme cases all arrived one step at a time.",
  "The point is increments, not heroism. Nobody starts at ninety percent.");
witness("Alan & Katherine Barnhart", "Barnhart Crane & Rigging · Memphis",
  "Two years of Scripture study before any decision. Income capped in year one, when there was almost nothing to cap. Half of profits out, half reinvested. In 2007 they gave the company away.",
  "Not a bigger heart. A structure, and twenty-five years.",
  "Fifty thousand in year one — more than Alan's salary. A million a month decades later.");
witness("April & Craig Chapman", "Software engineers · Seattle",
  "Two early windfalls launched their giving, and they eventually gave away half of what they earned. Her framing inverts the usual question entirely.",
  "The question was never how much to give.",
  "It is how much to keep. Save this one for last — it lands hardest after the room has been impressed by large numbers.");

/* 12 what they gave */
{
  const s = light("What they gave that was not money", "The pattern");
  const items = ["A room", "A guest list", "A shipping network", "A pulpit", "A recruitment conversation", "Two years of study"];
  const w = (11.9 - 0.3 * 2) / 3;
  items.forEach((t, i) => {
    const col = i % 3, row = Math.floor(i / 3);
    const x = 0.7 + col * (w + 0.3), y = 2.4 + row * 1.9;
    s.addShape(pres.ShapeType.rect, { x: x, y: y, w: w, h: 1.5, fill: { color: "FFFFFF" }, line: { color: LINE, width: 1 } });
    s.addText(t, { x: x, y: y + 0.5, w: w, h: 0.5, fontFace: "Georgia", fontSize: 17, bold: true, color: NAVY, align: "center", margin: 0 });
  });
  s.addText("Which of these do you have?", { x: 0.7, y: 6.15, w: 11.9, h: 0.4, fontFace: "Georgia", fontSize: 16, italic: true, color: GOLD, align: "center", margin: 0 });
  s.addNotes("Build this list from the room rather than presenting it. This is the section that makes the material usable where capacity varies widely.");
}

/* 13 adapting */
{
  const s = light("Same material, three rooms", "Adapting this");
  const rows = [
    ["Advisors", "Add a seventh witness — a professional who raised the question and changed a family's trajectory. Shift the closing from what do you have to what could you ask."],
    ["Pastors", "Lead with Huntingdon and Thornton, not Barnhart. High-capacity families need to see relational patronage before financial patronage, or it reads as a campaign preamble."],
    ["Giving circles", "One witness a month, scored and discussed, with a rotating member bringing a seventh of their own. The version with the longest life."]
  ];
  rows.forEach((r, i) => {
    const y = 2.2 + i * 1.35;
    s.addShape(pres.ShapeType.rect, { x: 0.7, y: y, w: 11.9, h: 1.15, fill: { color: "FFFFFF" }, line: { color: LINE, width: 1 } });
    s.addText(r[0], { x: 1.0, y: y + 0.35, w: 2.4, h: 0.5, fontFace: "Georgia", fontSize: 16, bold: true, color: NAVY, margin: 0 });
    s.addText(r[1], { x: 3.7, y: y + 0.22, w: 8.6, h: 0.9, fontFace: "Calibri", fontSize: 12.5, color: CHAR, lineSpacing: 19, margin: 0 });
  });
}

/* 14 close */
{
  const s = dark();
  s.addText("Whose best work is still\nahead of them —", { x: 0.9, y: 2.3, w: 11.4, h: 1.6, fontFace: "Georgia", fontSize: 34, bold: true, color: "FFFFFF", lineSpacing: 46, margin: 0 });
  s.addText("and are you close enough to know?", { x: 0.9, y: 3.95, w: 11.4, h: 0.7, fontFace: "Georgia", fontSize: 34, bold: true, color: GOLD, margin: 0 });
  s.addText("Every witness is drawn from published sources. Nothing here is reconstructed.", { x: 0.9, y: 6.35, w: 11.4, h: 0.3, fontFace: "Calibri", fontSize: 10.5, italic: true, color: "8C8578", margin: 0 });
  s.addNotes("Close on the question. No summary, no recap, no ask.");
}

pres.writeFile({ fileName: "/mnt/user-data/outputs/Two-Engines-Training-Visuals.pptx" }).then(() => console.log("ok"));
