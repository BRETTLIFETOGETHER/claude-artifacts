const fs = require("fs");
const {
  Document, Packer, Paragraph, TextRun, AlignmentType, LevelFormat,
  HeadingLevel, Footer, PageNumber, BorderStyle,
} = require("docx");

const NAVY = "1F3864";
const ACCENT = "2E75B6";

function h1(text, pageBreak = false) {
  return new Paragraph({
    heading: HeadingLevel.HEADING_1,
    pageBreakBefore: pageBreak,
    spacing: { before: 0, after: 60 },
    children: [new TextRun({ text })],
  });
}
function rule() {
  return new Paragraph({
    spacing: { after: 160 },
    border: { bottom: { style: BorderStyle.SINGLE, size: 8, color: ACCENT, space: 2 } },
    children: [new TextRun({ text: "" })],
  });
}
function h2(text) {
  return new Paragraph({
    heading: HeadingLevel.HEADING_2,
    spacing: { before: 200, after: 70 },
    children: [new TextRun({ text })],
  });
}
function para(text) {
  return new Paragraph({ spacing: { after: 120 }, children: [new TextRun(text)] });
}
function bullet(text) {
  return new Paragraph({
    numbering: { reference: "bullets", level: 0 },
    spacing: { after: 60 },
    children: [new TextRun(text)],
  });
}
function metaLine(label, text) {
  return new Paragraph({
    spacing: { after: 60 },
    children: [
      new TextRun({ text: label + ":  ", bold: true, color: NAVY }),
      new TextRun({ text }),
    ],
  });
}
function roleMeta(text) {
  return new Paragraph({
    spacing: { after: 140 },
    children: [new TextRun({ text, italics: true, color: "555555" })],
  });
}

const roles = [
  {
    title: "Production & Publishing Coordinator",
    meta: "Full-time  \u2022  In-office (Rancho Santa Margarita, CA)  \u2022  Temp-to-hire welcome",
    intro: "Ideas move fast here \u2014 new curriculum, campaigns, devotionals, and family resources get invented and prototyped weekly. This role turns started into shipped. You'll take approved examples and established playbooks and carry them across the finish line, product after product, so the founders can keep building what's next.",
    doing: [
      "Execute established playbooks: build out finished pages, products, and courses in our platforms from approved examples.",
      "Populate and upgrade templates across product lines \u2014 for example, replacing weak photography with a fresh, curated set of a hundred better images.",
      "Assemble, format, and proof curriculum, campaign, and devotional files to match approved standards.",
      "Keep the template and asset library organized: naming, versions, files, and folders.",
      "Close loops without being chased; surface blockers early and specifically.",
    ],
    bring: [
      "A track record of finishing \u2014 shipped projects, not just started ones.",
      "Speed with new software; you pick up tools in days, not months.",
      "A meticulous eye for consistency against a reference standard.",
      "Clear, brief written communication.",
      "Comfort with AI-assisted production tools, or a real appetite to learn them fast.",
    ],
    nice: [
      "Christian publishing, church curriculum, or ministry media experience.",
      "Kajabi or another course/membership platform.",
      "Canva or similar design tools; photo curation.",
    ],
    success: [
      "Products move from eighty percent to shipped without founder involvement.",
      "The template and asset library stays current and easy to navigate.",
      "Rework drops because output matches the approved standard the first time.",
    ],
  },
  {
    title: "Operations & Executive Assistant",
    meta: "Full-time  \u2022  In-office (Rancho Santa Margarita, CA)  \u2022  Temp-to-hire welcome",
    intro: "A fast company generates a hundred small tasks a week \u2014 travel and hotels, logins and accounts, vendors, shipping, scheduling, event logistics. Right now the founders do them. Your job is to own that entire layer so completely that it stops being a topic of conversation.",
    doing: [
      "Own calendars, travel, and lodging end to end \u2014 research, book, confirm, adjust.",
      "Manage accounts, logins, subscriptions, and vendor coordination.",
      "Handle shipping, supplies, office operations, and event logistics.",
      "Support inbox triage and follow-ups for the founders.",
      "Keep records, receipts, and files organized and findable.",
    ],
    bring: [
      "Exceptional organization and follow-through \u2014 nothing you own gets dropped.",
      "Discretion; you'll see everything.",
      "A cheerful, service-hearted way of working at speed.",
      "Confidence across everyday tech: Google Workspace, spreadsheets, booking tools.",
    ],
    nice: [
      "Executive assistant, office management, or ministry operations experience.",
      "Event or travel coordination background.",
    ],
    success: [
      "Logistics stop appearing in founder conversations.",
      "Anything handed off comes back finished, with clear status along the way.",
      "Vendors, bookings, and accounts run without surprises.",
    ],
  },
  {
    title: "Project & Account Manager",
    meta: "Full-time  \u2022  In-office (Rancho Santa Margarita, CA)",
    intro: "This is the highest-gear seat on the team. You'll sit between founders who generate direction faster than most teams can absorb and the clients, partners, and specialists who need that direction turned into commitments, timelines, and finished work.",
    doing: [
      "Run project plans across many concurrent product builds; own status, sequence, and deadlines.",
      "Serve as the day-to-day interface for client and partner accounts \u2014 churches, institutes, and advisor organizations.",
      "Translate founder direction into briefs, task lists, and clean hand-offs to the team and to fractional specialists.",
      "Hold the weekly operating rhythm: what shipped, what's next, what's blocked.",
      "Protect scope \u2014 surface conflicts and trade-offs before they become surprises.",
    ],
    bring: [
      "Several years in project or account management running multiple simultaneous workstreams.",
      "Calm, high-capacity multitasking; changes of direction energize rather than rattle you.",
      "Excellent client-facing communication, written and spoken.",
      "Fluency with project tools and comfort using AI in daily work.",
    ],
    nice: [
      "Agency, publishing, or ministry-services background.",
      "Experience managing contractors or fractional specialists.",
    ],
    success: [
      "Clients always know status, and deadlines hold.",
      "Founder direction becomes team execution without the founder re-explaining it.",
      "Nothing important lives only in someone's head.",
    ],
  },
  {
    title: "Creative Content & Marketing Producer",
    meta: "Full-time  \u2022  In-office (Rancho Santa Margarita, CA)",
    intro: "We're not hiring a classically trained graphic designer \u2014 we're hiring a communicator with a great eye. Someone who can build the page, choose the photo, write the line, and know when it looks right, across a large and growing catalog of products.",
    doing: [
      "Build new product, marketing, and catalog pages from our established design system.",
      "Extend the template library \u2014 including photo-driven collection pages for family resources \u2014 so customers choose from approved designs.",
      "Curate photography and imagery; upgrade weak visuals across product lines.",
      "Write and polish customer-facing copy: pages, emails, product descriptions.",
      "Partner with fractional design specialists when a project needs deep design work.",
    ],
    bring: [
      "A portfolio that shows judgment \u2014 clean pages, strong images, clear words. Pedigree optional.",
      "Communication-led creativity: you write as well as you see.",
      "Fluency with modern creative tools (Canva-class design, AI image tools) and speed learning new ones.",
      "Low ego about revisions; fast and teachable.",
    ],
    nice: [
      "Marketing production experience: email, landing pages, social assets.",
      "Photography, photo editing, or art direction.",
      "Church, publishing, or nonprofit communications background.",
    ],
    success: [
      "New products launch with pages and assets that meet the house standard without founder rework.",
      "The approved-template catalog grows every month.",
      "Customers can see and choose exactly what they're buying.",
    ],
  },
];

function roleSection(r) {
  const out = [];
  out.push(h1(r.title, true));
  out.push(rule());
  out.push(roleMeta(r.meta));
  out.push(para(r.intro));
  out.push(h2("What You'll Do"));
  r.doing.forEach((t) => out.push(bullet(t)));
  out.push(h2("What You'll Bring"));
  r.bring.forEach((t) => out.push(bullet(t)));
  out.push(h2("Nice to Have"));
  r.nice.forEach((t) => out.push(bullet(t)));
  out.push(h2("What Success Looks Like"));
  r.success.forEach((t) => out.push(bullet(t)));
  return out;
}

const cover = [
  new Paragraph({
    spacing: { after: 40 },
    children: [new TextRun({ text: "LifeTogether", bold: true, size: 44, color: NAVY })],
  }),
  new Paragraph({
    spacing: { after: 220 },
    border: { bottom: { style: BorderStyle.SINGLE, size: 8, color: ACCENT, space: 4 } },
    children: [new TextRun({ text: "Open Roles \u2014 2026", size: 28, color: ACCENT })],
  }),
  para("LifeTogether is a twenty-five-year-old Christian publishing and curriculum organization in Rancho Santa Margarita, California. We've served more than five hundred churches and helped put campaign resources in the hands of tens of millions of people. Today we build churchwide campaigns, small-group curriculum, financial-discipleship resources, and family-legacy tools \u2014 a large catalog produced by a small team that uses modern AI tools every day and moves at a pace most publishers can't match."),
  para("A word about how we work. We move fast and change direction often; a left turn on Tuesday is normal here, not a crisis. We prize speed, teachability, and low ego over pedigree, and we care as much about whether we enjoy working together as we do about a r\u00e9sum\u00e9 \u2014 we laugh a lot, and we intend to keep it that way."),
  metaLine("Location", "Rancho Santa Margarita, CA \u2014 in-office during business hours"),
  metaLine("Employment", "Full-time; temp-to-hire welcome for the Production and Operations roles"),
  metaLine("Compensation", "Based on role, experience, and structure"),
  metaLine("Faith", "LifeTogether is a religious organization; personal Christian faith and alignment with our mission is a requirement of employment"),
  new Paragraph({
    spacing: { before: 160, after: 0 },
    children: [new TextRun({
      text: "Every role calls for someone organized, proactive, and digitally fluent \u2014 a finisher who works well in a fast-moving setting and is glad to serve a faith-based mission and its ministry partners.",
    })],
  }),
];

const children = [...cover];
roles.forEach((r) => children.push(...roleSection(r)));

const doc = new Document({
  styles: {
    default: { document: { run: { font: "Arial", size: 22 } } },
    paragraphStyles: [
      { id: "Heading1", name: "Heading 1", basedOn: "Normal", next: "Normal", quickFormat: true,
        run: { size: 30, bold: true, font: "Arial", color: NAVY },
        paragraph: { spacing: { before: 0, after: 60 }, outlineLevel: 0 } },
      { id: "Heading2", name: "Heading 2", basedOn: "Normal", next: "Normal", quickFormat: true,
        run: { size: 22, bold: true, font: "Arial", color: ACCENT },
        paragraph: { spacing: { before: 200, after: 70 }, outlineLevel: 1 } },
    ],
  },
  numbering: {
    config: [
      { reference: "bullets", levels: [
        { level: 0, format: LevelFormat.BULLET, text: "\u2022", alignment: AlignmentType.LEFT,
          style: { paragraph: { indent: { left: 540, hanging: 270 } } } },
      ]},
    ],
  },
  sections: [{
    properties: {
      page: {
        size: { width: 12240, height: 15840 },
        margin: { top: 1080, right: 1080, bottom: 1080, left: 1080 },
      },
    },
    footers: {
      default: new Footer({ children: [new Paragraph({
        alignment: AlignmentType.CENTER,
        children: [
          new TextRun({ text: "LifeTogether  \u2022  ", color: "999999", size: 18 }),
          new TextRun({ text: "Page ", color: "999999", size: 18 }),
          new TextRun({ children: [PageNumber.CURRENT], color: "999999", size: 18 }),
        ],
      })] }),
    },
    children,
  }],
});

Packer.toBuffer(doc).then((buffer) => {
  fs.writeFileSync("/home/claude/LifeTogether-Open-Roles-2026.docx", buffer);
  console.log("written");
});
