const {
  Document, Packer, Paragraph, TextRun, HeadingLevel, AlignmentType,
  Table, TableRow, TableCell, WidthType, ShadingType, BorderStyle, VerticalAlign
} = require("docx");

const NAVY = "1F3A5F";
const GOLD = "B08D57";
const INK = "2B2B2B";
const SOFTGREY = "6E6E6E";
const RULE = "D9D2C4";

const letter = { width: 12240, height: 15840 };

function rule() {
  return new Paragraph({
    spacing: { before: 120, after: 240 },
    border: { bottom: { color: RULE, space: 1, style: BorderStyle.SINGLE, size: 6 } },
    children: [new TextRun({ text: "", size: 2 })],
  });
}

function h1(text) {
  return new Paragraph({
    heading: HeadingLevel.HEADING_1,
    spacing: { before: 480, after: 160 },
    children: [new TextRun({ text, bold: true, color: NAVY, size: 30, font: "Georgia" })],
  });
}

function h2(text) {
  return new Paragraph({
    spacing: { before: 240, after: 100 },
    children: [new TextRun({ text, bold: true, color: GOLD, size: 22, font: "Georgia", allCaps: true, characterSpacing: 20 })],
  });
}

function body(text, opts = {}) {
  return new Paragraph({
    spacing: { after: 140, line: 300 },
    children: [new TextRun({ text, size: 22, color: INK, italics: !!opts.italics, bold: !!opts.bold })],
  });
}

function tagline(text) {
  return new Paragraph({
    spacing: { before: 80, after: 80 },
    children: [new TextRun({ text: `“${text}”`, size: 26, color: NAVY, bold: true, font: "Georgia" })],
  });
}

function bullet(text) {
  return new Paragraph({
    spacing: { after: 90 },
    bullet: { level: 0 },
    children: [new TextRun({ text, size: 22, color: INK })],
  });
}

function pillarRow(label) {
  return new Paragraph({
    spacing: { after: 60 },
    children: [new TextRun({ text: label, size: 24, color: NAVY, bold: true, font: "Georgia" })],
  });
}

function label(text) {
  return new Paragraph({
    spacing: { before: 160, after: 60 },
    children: [new TextRun({ text, size: 18, color: SOFTGREY, bold: true, allCaps: true, characterSpacing: 20 })],
  });
}

const doc = new Document({
  sections: [{
    properties: { page: { size: letter, margin: { top: 1080, bottom: 1080, left: 1260, right: 1260 } } },
    children: [

      new Paragraph({
        spacing: { before: 600, after: 60 },
        children: [new TextRun({ text: "LIFETOGETHER", bold: true, size: 44, color: NAVY, font: "Georgia", characterSpacing: 30 })],
      }),
      new Paragraph({
        spacing: { after: 40 },
        children: [new TextRun({ text: "BIBLICAL PURPOSE LIBRARY", size: 24, color: GOLD, bold: true, font: "Georgia", characterSpacing: 40 })],
      }),
      new Paragraph({
        spacing: { after: 300 },
        children: [new TextRun({ text: "Brand & Marketing Kit", size: 24, italics: true, color: SOFTGREY, font: "Georgia" })],
      }),
      rule(),

      h1("Positioning Statement"),
      body("For over 30 years, the five biblical purposes have shaped thousands of churches and inspired more than 50 million readers around the world. LifeTogether builds on those timeless foundations with a new generation of churchwide campaigns — designed to help your church go deeper, grow stronger, and reach further, in every season of life."),
      body("Founder Brett Eastman served on the original Purpose Driven ministry team and helped develop many of the original small-group resources. LifeTogether carries that same foundation forward — reimagined for the church today.", { italics: true }),

      h1("Tagline Options"),
      tagline("Timeless Purpose. Next Generation Church."),
      tagline("Rooted in the Past. Built for What's Next."),
      tagline("Every Purpose. Every Generation."),
      tagline("Deeper Roots. Wider Reach."),
      tagline("One Story. Every Church. Every Chapter."),
      tagline("Nobody Grows Alone."),

      h1("Brand Pillars"),
      pillarRow("Helping Churches Go Deeper."),
      pillarRow("Helping Disciples Grow Stronger."),
      pillarRow("Helping Every Person Discover a Life That Matters."),

      h1("Elevator Pitches"),
      label("Three Seconds"),
      body("Timeless purpose, built for today's church."),
      label("One Sentence"),
      body("LifeTogether turns 30 years of proven biblical purpose into churchwide campaigns your congregation can live out together — starting this Sunday."),
      label("Thirty Seconds"),
      body("For over three decades, the five biblical purposes have shaped thousands of churches and tens of millions of lives. LifeTogether takes that same foundation and builds something new: six-week churchwide campaigns — sermons, small groups, devotionals, and family resources — all working as one. No retrofitted material. No academic detour. Just a church, moving deeper into purpose, together."),

      h1("Website Hero Copy"),
      label("Headline"),
      body("A Life That Matters Starts Here.", { bold: true }),
      label("Subhead"),
      body("Six-week churchwide campaigns built on 30 years of proven biblical purpose — for every age, every stage, every church."),
      label("Call to Action"),
      body("Explore the Library   ·   Start a Campaign"),

      h1("Brochure Opening (Refined)"),
      body("For over 30 years, the five biblical purposes have helped shape thousands of churches and inspired more than 50 million readers around the world."),
      body("LifeTogether builds on those timeless foundations with a new generation of churchwide campaigns, devotionals, curriculum, and discipleship experiences — designed to help your church go deeper, wider, and further, in every purpose."),
      pillarRow("Helping Churches Go Deeper."),
      pillarRow("Helping Disciples Grow Stronger."),
      pillarRow("Helping Every Person Discover a Life That Matters."),

      h1("Social & Email One-Liners"),
      bullet("Nobody grows alone."),
      bullet("Six weeks. One church. One story."),
      bullet("Purpose isn't a season. It's a rhythm."),
      bullet("Every campaign. Every purpose. Every person."),
      bullet("Deeper roots grow stronger disciples."),
      bullet("Your next chapter starts on a Sunday."),
      bullet("Thirty years of proof. One new chapter."),
      bullet("Rooted in truth. Built for now."),
      bullet("Come as you are. Grow into who you're becoming."),
      bullet("The purposes haven't changed. Neither has the need."),

      h1("Voice DNA — Quick Reference"),
      bullet("Short lines. Fragments over full sentences."),
      bullet("Lead with the human need, not the doctrine."),
      bullet("Second person or collective — never “individuals” or “participants.”"),
      bullet("Name the ache briefly, then open the door to hope fast."),
      bullet("Invitational verbs: Discover, Join, Begin, Belong — never “required” or “must.”"),
      bullet("Reach for: journey, story, chapter, season, rooted, flourish, calling, legacy, together."),

    ],
  }],
});

Packer.toBuffer(doc).then((buf) => require("fs").writeFileSync("/home/claude/branding/LifeTogether_Brand_Marketing_Kit.docx", buf));
