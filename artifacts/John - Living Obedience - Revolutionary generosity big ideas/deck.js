const fs = require('fs');
const pptxgen = require('pptxgenjs');
const C = JSON.parse(fs.readFileSync('/home/claude/rg/content.json', 'utf8'));

const NAVY = "1B2A4A";
const DEEP = "131F36";
const GOLD = "B08D42";
const GOLDL = "C8A85E";
const CREAM = "F7F5F0";
const INK = "20252E";
const GREY = "5A6272";
const WHITE = "FFFFFF";
const LINE = "D8D3C7";

const SER = "Cambria";
const SAN = "Calibri";

const pres = new pptxgen();
pres.layout = "LAYOUT_WIDE";
pres.author = "LifeTogether Ministries";
pres.title = "Revolutionary Generosity — Contributor Invitation";

const Wd = 13.33, Ht = 7.5;

function darkSlide() {
  const s = pres.addSlide();
  s.background = { color: DEEP };
  return s;
}
function lightSlide() {
  const s = pres.addSlide();
  s.background = { color: WHITE };
  return s;
}

function eyebrow(s, text, color) {
  s.addText(text.toUpperCase(), {
    x: 0.75, y: 0.46, w: 11.8, h: 0.3, margin: 0,
    fontFace: SAN, fontSize: 11, bold: true, charSpacing: 3,
    color: color || GOLD
  });
}

function title(s, text, color, opts) {
  opts = opts || {};
  s.addText(text, {
    x: 0.75, y: opts.y || 0.82, w: opts.w || 11.8, h: opts.h || 0.9, margin: 0,
    fontFace: SER, fontSize: opts.size || 34, bold: true,
    color: color || NAVY, valign: "top"
  });
}

function deck(s, text, color) {
  s.addText(text, {
    x: 0.75, y: 1.72, w: 11.4, h: 0.62, margin: 0,
    fontFace: SAN, fontSize: 15, color: color || GREY, valign: "top"
  });
}

function numCircle(s, n, x, y, size, fill, textColor) {
  s.addShape(pres.ShapeType.ellipse, {
    x: x, y: y, w: size, h: size,
    fill: { color: fill || GOLD }, line: { color: fill || GOLD, width: 0 }
  });
  s.addText(String(n), {
    x: x, y: y, w: size, h: size, margin: 0,
    fontFace: SER, fontSize: size > 0.5 ? 15 : 12, bold: true,
    color: textColor || WHITE, align: "center", valign: "middle"
  });
}

function card(s, x, y, w, h, fill) {
  s.addShape(pres.ShapeType.roundRect, {
    x: x, y: y, w: w, h: h, rectRadius: 0.06,
    fill: { color: fill || CREAM }, line: { color: LINE, width: 0.5 }
  });
}

function footnote(s, text, color) {
  s.addText(text, {
    x: 0.75, y: 6.92, w: 11.8, h: 0.3, margin: 0,
    fontFace: SAN, fontSize: 9.5, italic: true, color: color || "9AA0AC"
  });
}

/* ============ 1. Title ============ */
{
  const s = darkSlide();
  s.addShape(pres.ShapeType.line, {
    x: 1.6, y: 1.62, w: 10.13, h: 0, line: { color: GOLD, width: 1 }
  });
  s.addText("AN INVITATION TO THE PEOPLE WHO BUILT THIS MOVEMENT", {
    x: 0.75, y: 1.18, w: 11.8, h: 0.35, margin: 0, align: "center",
    fontFace: SAN, fontSize: 11.5, bold: true, charSpacing: 3.4, color: GOLDL
  });
  s.addText("Revolutionary Generosity", {
    x: 0.75, y: 2.25, w: 11.8, h: 1.0, margin: 0, align: "center",
    fontFace: SER, fontSize: 50, bold: true, color: WHITE
  });
  s.addText("How Families Give While They Live, Give More Than Cash,\nand Leave More Than Money", {
    x: 1.9, y: 3.42, w: 9.5, h: 0.9, margin: 0, align: "center",
    fontFace: SER, fontSize: 17, italic: true, color: "D9CBA8", lineSpacing: 26
  });
  s.addShape(pres.ShapeType.line, {
    x: 5.4, y: 4.62, w: 2.53, h: 0, line: { color: "3A4A6B", width: 1 }
  });
  s.addText("A book proposed for Steve French and Dale Armstrong  ·  The Signatry", {
    x: 0.75, y: 4.9, w: 11.8, h: 0.35, margin: 0, align: "center",
    fontFace: SAN, fontSize: 14, color: "9AA4B6"
  });
  s.addText("Concept brief prepared for discussion · not an approved project of The Signatry\nPrepared by Brett Eastman, LifeTogether Ministries · August 2026", {
    x: 0.75, y: 6.3, w: 11.8, h: 0.6, margin: 0, align: "center",
    fontFace: SAN, fontSize: 10, italic: true, color: "6E7A90", lineSpacing: 15
  });
  s.addNotes("Open by naming the status honestly: this is a concept, not an approved project. The room should know exactly what they are being asked to react to.");
}

/* ============ 2. What the movement already proved ============ */
{
  const s = lightSlide();
  eyebrow(s, "Start here");
  title(s, "Twenty-five years of work already won the hard argument");
  deck(s, "None of what follows is a critique of the field. It is an attempt to consolidate what the field already proved.");

  const items = [
    ["Generous Giving", "A room with no ask produces honesty that no solicitation ever has. Privately funded since 2000 precisely so it never has to ask."],
    ["National Christian Foundation", "The asset, not the paycheck, is where real generosity lives — and the giving vehicle can be built to serve that."],
    ["The Gathering", "Generous families do better work in each other's company than they ever do alone."],
    ["Ron Blue · Randy Alcorn", "Ownership is the root question, and the treasure moves before the heart follows it."]
  ];
  const cw = 2.72, gap = 0.28;
  items.forEach((it, i) => {
    const x = 0.75 + i * (cw + gap);
    card(s, x, 2.62, cw, 3.3);
    s.addText(it[0], {
      x: x + 0.24, y: 2.92, w: cw - 0.48, h: 0.72, margin: 0,
      fontFace: SER, fontSize: 14.5, bold: true, color: NAVY, valign: "top"
    });
    s.addText(it[1], {
      x: x + 0.24, y: 3.72, w: cw - 0.48, h: 2.0, margin: 0,
      fontFace: SAN, fontSize: 12.5, color: INK, lineSpacing: 17, valign: "top"
    });
  });
  footnote(s, "The book credits each of these by name. Acknowledgement is not a courtesy here — it is what makes it a movement book rather than a company book.");
  s.addNotes("Lead with the field's accomplishment, not with our idea. Every person in this room built one of these columns.");
}

/* ============ 3. The gap ============ */
{
  const s = lightSlide();
  eyebrow(s, "The gap");
  title(s, "What twenty-five years has not produced");

  card(s, 0.75, 2.15, 5.85, 4.05, CREAM);
  s.addText("WHAT EXISTS", {
    x: 1.05, y: 2.45, w: 5.25, h: 0.3, margin: 0,
    fontFace: SAN, fontSize: 10.5, bold: true, charSpacing: 3, color: GREY
  });
  s.addText([
    { text: "Retreats that change the heart in a weekend", options: { bullet: true, breakLine: true } },
    { text: "Vehicles that make an asset gift possible", options: { bullet: true, breakLine: true } },
    { text: "Conferences that gather the already-convinced", options: { bullet: true, breakLine: true } },
    { text: "Advisor training for the professionals who ask", options: { bullet: true, breakLine: true } },
    { text: "Excellent books on single pieces of the picture", options: { bullet: true } }
  ], {
    x: 1.05, y: 2.9, w: 5.25, h: 3.0, margin: 0,
    fontFace: SAN, fontSize: 14, color: INK, paraSpaceAfter: 10, lineSpacing: 19
  });

  s.addShape(pres.ShapeType.roundRect, {
    x: 6.95, y: 2.15, w: 5.6, h: 4.05, rectRadius: 0.06,
    fill: { color: NAVY }, line: { color: NAVY, width: 0 }
  });
  s.addText("WHAT DOESN'T", {
    x: 7.28, y: 2.45, w: 5.0, h: 0.3, margin: 0,
    fontFace: SAN, fontSize: 10.5, bold: true, charSpacing: 3, color: GOLDL
  });
  s.addText("One book a family can hand to their adult children — and an advisor can hand to a client — that carries the conviction and the mechanics in the same hundred pages.", {
    x: 7.28, y: 2.92, w: 5.0, h: 1.5, margin: 0,
    fontFace: SER, fontSize: 18, color: WHITE, lineSpacing: 27, valign: "top"
  });
  s.addText("The heart argument has been won in rooms. It has never been packaged for the kitchen table, and the kitchen table is where the next generation is either formed or lost.", {
    x: 7.28, y: 4.6, w: 5.0, h: 1.4, margin: 0,
    fontFace: SAN, fontSize: 13.5, color: "B9C0CE", lineSpacing: 19, valign: "top"
  });
  s.addNotes("This is the whole reason for the book. Do not oversell it — the room will either recognize the gap from their own experience or they won't.");
}

/* ============ 4. Who is waiting ============ */
{
  const s = lightSlide();
  eyebrow(s, "The reader");
  title(s, "Four people who are waiting for it");

  const rows = [
    ["The owner with an event coming", "Within five years of a sale, and nobody has told him that sequence — not generosity — determines the size of the gift."],
    ["The family with capacity and no practice", "They give faithfully. Their four adult children have never once decided where real money went."],
    ["The advisor who has never asked", "Not the buyer, but the fastest channel to the first two — and he will only pass it on if it sells nothing."],
    ["The pastor with families he is afraid to disciple", "He has never discipled the third row about money because every conversation he can imagine sounds like an ask."]
  ];
  rows.forEach((r, i) => {
    const y = 2.28 + i * 1.12;
    numCircle(s, i + 1, 0.78, y + 0.06, 0.52);
    s.addText(r[0], {
      x: 1.62, y: y, w: 4.3, h: 0.7, margin: 0,
      fontFace: SER, fontSize: 15.5, bold: true, color: NAVY, valign: "top"
    });
    s.addText(r[1], {
      x: 6.1, y: y + 0.02, w: 6.45, h: 0.85, margin: 0,
      fontFace: SAN, fontSize: 13, color: INK, lineSpacing: 18, valign: "top"
    });
    if (i < 3) {
      s.addShape(pres.ShapeType.line, {
        x: 0.78, y: y + 0.94, w: 11.77, h: 0, line: { color: "E6E3DC", width: 0.75 }
      });
    }
  });
  s.addNotes("Priority order matters. The owner is the reader whose life the book most concretely changes.");
}

/* ============ 5. The three breaks ============ */
{
  const s = lightSlide();
  eyebrow(s, "The argument");
  title(s, "Revolutionary is not a temperament. It is three specific breaks.");
  deck(s, "Each is teachable. None requires more income. All three are ordinary decisions most families never got around to making.");

  const breaks = [
    ["Give while\nyou live", "Giving at death is a transaction. Giving during life is a discipleship — you see the outcome, correct your mistakes, and your children watch you do it."],
    ["Give more\nthan cash", "Most wealth isn't in the checking account. Most giving is. That single mismatch is the largest unclaimed opportunity in Christian philanthropy."],
    ["Leave more\nthan money", "Generosity is not inherited, it is rehearsed. A family that decides together raises adult children who give."]
  ];
  const cw = 3.78, gap = 0.42;
  breaks.forEach((b, i) => {
    const x = 0.75 + i * (cw + gap);
    card(s, x, 2.68, cw, 3.34);
    numCircle(s, i + 1, x + 0.32, 2.42, 0.54);
    s.addText(b[0], {
      x: x + 0.32, y: 3.18, w: cw - 0.64, h: 1.0, margin: 0,
      fontFace: SER, fontSize: 21, bold: true, color: NAVY, lineSpacing: 27, valign: "top"
    });
    s.addText(b[1], {
      x: x + 0.32, y: 4.32, w: cw - 0.64, h: 1.5, margin: 0,
      fontFace: SAN, fontSize: 13, color: INK, lineSpacing: 18, valign: "top"
    });
  });
  s.addNotes("The subtitle is the argument. If a contributor disagrees with one of these three, that is the conversation worth having today.");
}

/* ============ 6. The twenty ideas ============ */
{
  const s = lightSlide();
  eyebrow(s, "The structure");
  title(s, "Twenty ideas, five movements");

  const colw = 2.34, gap = 0.19;
  C.parts.forEach((part, i) => {
    const x = 0.75 + i * (colw + gap);
    s.addShape(pres.ShapeType.roundRect, {
      x: x, y: 2.1, w: colw, h: 0.86, rectRadius: 0.05,
      fill: { color: NAVY }, line: { color: NAVY, width: 0 }
    });
    s.addText("PART " + part.num.toUpperCase(), {
      x: x + 0.16, y: 2.2, w: colw - 0.32, h: 0.24, margin: 0,
      fontFace: SAN, fontSize: 9, bold: true, charSpacing: 2.4, color: GOLDL
    });
    s.addText(part.name, {
      x: x + 0.16, y: 2.44, w: colw - 0.32, h: 0.46, margin: 0,
      fontFace: SER, fontSize: 13, bold: true, color: WHITE, valign: "top"
    });

    const items = C.chapters.filter(c => c.part === i + 1);
    items.forEach((ch, j) => {
      const y = 3.12 + j * 0.94;
      s.addText(("0" + ch.n).slice(-2), {
        x: x, y: y, w: 0.42, h: 0.3, margin: 0,
        fontFace: SER, fontSize: 13, bold: true, color: GOLD
      });
      s.addText(ch.title, {
        x: x + 0.42, y: y - 0.02, w: colw - 0.42, h: 0.86, margin: 0,
        fontFace: SAN, fontSize: 11.5, color: INK, lineSpacing: 15, valign: "top"
      });
    });
  });
  footnote(s, "Full premise, anchor voice, story requirement and reader action for each of the twenty are in the outline document.");
  s.addNotes("Do not read the grid aloud. Point at the part a given contributor's work anchors and let them find their own name.");
}

/* ============ 7. The no-ask rule ============ */
{
  const s = darkSlide();
  eyebrow(s, "Why you can lend your name to this", GOLDL);
  title(s, "The rule that keeps it from being a brochure", WHITE);
  s.addText("A book by the CEO and Chief Revenue Officer of a donor advised fund sponsor carries a credibility tax. The defense is not a disclaimer. It is a set of constraints, borrowed from this movement's own best practice, that hold through the whole manuscript.", {
    x: 0.75, y: 1.74, w: 11.6, h: 0.72, margin: 0,
    fontFace: SAN, fontSize: 14, color: "B9C0CE", lineSpacing: 20, valign: "top"
  });

  const rules = [
    "No vehicle is sold in the body. Every mechanism is explained in the appendix and recommended nowhere.",
    "No Signatry story runs without an equal number sourced from outside the organization.",
    "Every mechanics chapter ends on the reader's decision, never on a service that would make it easier.",
    "The one claim the authors make about their own institution — measure how fast money leaves — is proposed as an industry standard, with their own numbers published beside it.",
    "Endorsements are sought from peers who compete with The Signatry for the same families. If they decline, it is not yet a movement book."
  ];
  rules.forEach((r, i) => {
    const y = 2.72 + i * 0.79;
    numCircle(s, i + 1, 0.78, y, 0.44, GOLD, DEEP);
    s.addText(r, {
      x: 1.48, y: y - 0.06, w: 10.9, h: 0.7, margin: 0,
      fontFace: SAN, fontSize: 13.5, color: WHITE, lineSpacing: 19, valign: "top"
    });
  });
  s.addNotes("This is the trust slide. If contributors believe rule five, they will say yes to everything else.");
}

/* ============ 8. The ask ============ */
{
  const s = lightSlide();
  eyebrow(s, "What we are asking of you");
  title(s, "Four ways in, and you choose the one that fits");

  const asks = [
    ["A conversation", "Ninety minutes, recorded. Your material in your own words, so the book quotes a person rather than paraphrasing a legacy."],
    ["A story", "One giver you have watched, with their permission. Stories are the scarce resource in this book — not ideas."],
    ["A read", "One chapter, the one closest to your work, marked up honestly before it is final."],
    ["A blessing", "A foreword or an endorsement, if the manuscript earns it. Nobody is asked to commit to that today."]
  ];
  const cw = 2.9, gap = 0.28;
  asks.forEach((a, i) => {
    const x = 0.75 + i * (cw + gap);
    card(s, x, 2.4, cw, 2.85, WHITE);
    numCircle(s, i + 1, x + 0.28, 2.14, 0.52);
    s.addText(a[0], {
      x: x + 0.28, y: 2.86, w: cw - 0.56, h: 0.42, margin: 0,
      fontFace: SER, fontSize: 17, bold: true, color: NAVY, valign: "top"
    });
    s.addText(a[1], {
      x: x + 0.28, y: 3.38, w: cw - 0.56, h: 1.6, margin: 0,
      fontFace: SAN, fontSize: 12.5, color: INK, lineSpacing: 17, valign: "top"
    });
  });

  s.addShape(pres.ShapeType.roundRect, {
    x: 0.75, y: 5.56, w: 11.8, h: 0.94, rectRadius: 0.05,
    fill: { color: CREAM }, line: { color: LINE, width: 0.5 }
  });
  s.addText("Nobody is asked for money, and nothing in this book will ever ask your donors for theirs. Your organization is named and credited whether or not you contribute.", {
    x: 1.1, y: 5.78, w: 11.1, h: 0.55, margin: 0,
    fontFace: SER, fontSize: 14.5, italic: true, color: NAVY, valign: "top"
  });
  s.addNotes("Keep the ask small and specific. Ninety minutes is the real ask; everything else is optional.");
}

/* ============ 9. Where it goes ============ */
{
  const s = lightSlide();
  eyebrow(s, "Distribution");
  title(s, "The book is the seed, not the harvest");
  deck(s, "Distribution is part of the design, not an afterthought. Four channels already own the trust — none of them has to be built from scratch.");

  const chans = [
    ["Advisors", "The professional standing at the gate. A book he can hand a client without embarrassment travels further than any campaign."],
    ["Churches", "A six-session guide for small groups and a series a pastor can preach without attaching an offering to it."],
    ["Families and family offices", "The benchmark worked through in an evening, then again with the adult children."],
    ["The movement's own rooms", "Retreats, gatherings, and study groups that already convene exactly this reader."]
  ];
  chans.forEach((ch, i) => {
    const y = 2.5 + i * 1.06;
    s.addShape(pres.ShapeType.roundRect, {
      x: 0.75, y: y, w: 11.8, h: 0.88, rectRadius: 0.05,
      fill: { color: i % 2 === 0 ? CREAM : WHITE }, line: { color: LINE, width: 0.5 }
    });
    s.addText(ch[0], {
      x: 1.08, y: y + 0.18, w: 3.1, h: 0.52, margin: 0,
      fontFace: SER, fontSize: 15.5, bold: true, color: NAVY, valign: "middle"
    });
    s.addText(ch[1], {
      x: 4.3, y: y + 0.12, w: 8.0, h: 0.64, margin: 0,
      fontFace: SAN, fontSize: 12.8, color: INK, lineSpacing: 17, valign: "middle"
    });
  });
  s.addNotes("Ask the room who already owns the audience. Do not propose building a channel anyone here already has.");
}

/* ============ 10. Sequence ============ */
{
  const s = lightSlide();
  eyebrow(s, "Sequence");
  title(s, "What happens, and in what order");

  const phases = [
    ["Now", "Authorship confirmed", "French and Armstrong decide whether this is theirs, and whether it is a Signatry project or a personal one. Nothing below moves until this does."],
    ["Next 90 days", "Voices and stories", "Twenty to thirty recorded conversations. Forty usable stories, half sourced outside The Signatry."],
    ["Months 4–9", "Part Two first", "The mechanics section is drafted first — most specific, least contested, and the part a publisher reads to decide."],
    ["Months 9–18", "Manuscript and companions", "Remaining parts, the benchmark, the six-session guide, the advisor and family editions."]
  ];
  phases.forEach((ph, i) => {
    const x = 0.75 + i * 3.06;
    s.addShape(pres.ShapeType.ellipse, {
      x: x, y: 2.42, w: 0.3, h: 0.3,
      fill: { color: i === 0 ? GOLD : NAVY }, line: { color: WHITE, width: 0 }
    });
    if (i < 3) {
      s.addShape(pres.ShapeType.line, {
        x: x + 0.34, y: 2.57, w: 2.64, h: 0, line: { color: "DCD8CE", width: 1.25 }
      });
    }
    s.addText(ph[0].toUpperCase(), {
      x: x, y: 2.9, w: 2.8, h: 0.26, margin: 0,
      fontFace: SAN, fontSize: 10, bold: true, charSpacing: 2.4, color: GOLD
    });
    s.addText(ph[1], {
      x: x, y: 3.2, w: 2.8, h: 0.62, margin: 0,
      fontFace: SER, fontSize: 16.5, bold: true, color: NAVY, valign: "top"
    });
    s.addText(ph[2], {
      x: x, y: 3.94, w: 2.8, h: 1.9, margin: 0,
      fontFace: SAN, fontSize: 12.5, color: INK, lineSpacing: 17, valign: "top"
    });
  });
  footnote(s, "Status today: concept. Not proposed to a publisher, not budgeted, and not yet an approved project of The Signatry.");
  s.addNotes("Be scrupulous about the status line. Overstating where this stands is the fastest way to lose this room.");
}

/* ============ 11. Close ============ */
{
  const s = darkSlide();
  s.addShape(pres.ShapeType.line, {
    x: 1.6, y: 1.42, w: 10.13, h: 0, line: { color: GOLD, width: 1 }
  });
  s.addText("THE NEXT STEP", {
    x: 0.75, y: 1.0, w: 11.8, h: 0.3, margin: 0, align: "center",
    fontFace: SAN, fontSize: 11.5, bold: true, charSpacing: 3.4, color: GOLDL
  });
  s.addText("Ninety minutes, on the record,\nabout the thing you already gave your life to.", {
    x: 1.2, y: 2.1, w: 10.9, h: 1.5, margin: 0, align: "center",
    fontFace: SER, fontSize: 31, bold: true, color: WHITE, lineSpacing: 46
  });
  s.addText("If this movement is going to hand the next generation more than a set of retreats and a set of vehicles, someone has to put the whole argument in one place. We would rather it carried your fingerprints than approximated them.", {
    x: 2.15, y: 4.0, w: 9.0, h: 1.1, margin: 0, align: "center",
    fontFace: SAN, fontSize: 14.5, color: "B9C0CE", lineSpacing: 22, valign: "top"
  });
  s.addShape(pres.ShapeType.line, {
    x: 5.4, y: 5.4, w: 2.53, h: 0, line: { color: "3A4A6B", width: 1 }
  });
  s.addText("Revolutionary Generosity", {
    x: 0.75, y: 5.62, w: 11.8, h: 0.44, margin: 0, align: "center",
    fontFace: SER, fontSize: 19, bold: true, color: WHITE
  });
  s.addText("Concept brief prepared for discussion · not an approved project of The Signatry", {
    x: 0.75, y: 6.7, w: 11.8, h: 0.3, margin: 0, align: "center",
    fontFace: SAN, fontSize: 10, italic: true, color: "6E7A90"
  });
  s.addNotes("Close on the ask, not on the vision. Ninety minutes is the only thing anyone has to say yes to today.");
}

pres.writeFile({ fileName: '/home/claude/rg/Revolutionary-Generosity-Contributor-Deck.pptx' })
  .then(() => console.log('deck written'));
