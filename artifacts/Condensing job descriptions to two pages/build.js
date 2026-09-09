const fs = require("fs");
const {
  Document, Packer, Paragraph, TextRun, AlignmentType, LevelFormat,
  HeadingLevel, Footer, Header, PageNumber, BorderStyle, PageBreak,
} = require("docx");

const NAVY = "1F3864";
const ACCENT = "2E75B6";

// ---- helpers ----
function h1(text) {
  return new Paragraph({
    heading: HeadingLevel.HEADING_1,
    spacing: { before: 0, after: 120 },
    border: { bottom: { style: BorderStyle.SINGLE, size: 8, color: ACCENT, space: 4 } },
    children: [new TextRun({ text })],
  });
}
function h2(text) {
  return new Paragraph({
    heading: HeadingLevel.HEADING_2,
    spacing: { before: 200, after: 80 },
    children: [new TextRun({ text })],
  });
}
function para(runs, opts = {}) {
  const children = Array.isArray(runs) ? runs : [new TextRun(runs)];
  return new Paragraph({ spacing: { after: 120 }, children, ...opts });
}
function bullet(text) {
  return new Paragraph({
    numbering: { reference: "bullets", level: 0 },
    spacing: { after: 80 },
    children: [new TextRun(text)],
  });
}
function metaLine(label, value) {
  return new Paragraph({
    spacing: { after: 40 },
    children: [
      new TextRun({ text: label + ":  ", bold: true }),
      new TextRun({ text: value }),
    ],
  });
}

// ---- role builder ----
function role({ title, summary, responsibilities, required, preferred, success }, first = false) {
  const out = [];
  out.push(new Paragraph({
    heading: HeadingLevel.HEADING_1,
    pageBreakBefore: !first,
    spacing: { before: 0, after: 120 },
    border: { bottom: { style: BorderStyle.SINGLE, size: 8, color: ACCENT, space: 4 } },
    children: [new TextRun({ text: title })],
  }));
  out.push(para([new TextRun({ text: summary, italics: true, color: "555555" })]));

  out.push(h2("What You'll Do"));
  // responsibilities may be grouped: array of {group, items} or flat array of strings
  if (responsibilities[0] && responsibilities[0].group) {
    responsibilities.forEach(g => {
      out.push(new Paragraph({
        spacing: { before: 80, after: 40 },
        children: [new TextRun({ text: g.group, bold: true, color: NAVY })],
      }));
      g.items.forEach(i => out.push(bullet(i)));
    });
  } else {
    responsibilities.forEach(i => out.push(bullet(i)));
  }

  out.push(h2("What You Bring"));
  required.forEach(i => out.push(bullet(i)));

  out.push(h2("Nice to Have"));
  preferred.forEach(i => out.push(bullet(i)));

  out.push(h2("What Success Looks Like"));
  success.forEach(i => out.push(bullet(i)));

  return out;
}

// ---- content ----
const roles = [
  {
    title: "1. Senior Administrative Coordinator",
    summary: "High-level executive and administrative support to leadership — managing calendars, meetings, documents, communications, and follow-through across our publishing, production, curriculum, and ministry work. The job is to bring order, clarity, and consistency to a fast-moving organization.",
    responsibilities: [
      { group: "Executive Support", items: [
        "Manage leadership calendars, scheduling, calls, and meetings.",
        "Prepare agendas, notes, and background materials; track outcomes, next steps, and follow-ups.",
        "Handle confidential information with discretion.",
      ]},
      { group: "Communication", items: [
        "Coordinate with team members, vendors, contractors, clients, and ministry partners.",
        "Draft, proofread, and format emails, documents, and internal communications.",
        "Ensure timely follow-up with internal and external stakeholders.",
      ]},
      { group: "Project & Document Support", items: [
        "Track project details, deadlines, and deliverables across initiatives.",
        "Maintain files in Google Drive, Docs, and Sheets with consistent naming and version control.",
        "Support vendor coordination and meeting logistics.",
      ]},
    ],
    required: [
      "Experience in administration, executive support, or office/project coordination.",
      "Strong organization and attention to detail.",
      "Excellent written and verbal communication.",
      "Able to juggle multiple priorities and deadlines with strong follow-through.",
      "Proficient with Google Workspace, calendars, and email.",
      "A warm, mature, service-oriented manner.",
    ],
    preferred: [
      "Supporting executives, founders, pastors, authors, or creative teams.",
      "Background in publishing, curriculum, nonprofit, ministry, production, or media.",
      "Familiarity with project management tools, Canva, AI tools, or CRMs.",
      "A track record of improving administrative systems and workflows.",
    ],
    success: [
      "Leadership is consistently prepared, organized, and supported.",
      "Calendars, documents, and follow-ups are handled accurately and on time.",
      "Files and project documents are organized and easy to locate.",
      "Leadership gains capacity for strategy, relationships, and content.",
    ],
  },
  {
    title: "2. Project Manager / Operations Manager",
    summary: "Turns leadership vision into organized plans and finished deliverables — building structure, timelines, and accountability across publishing, curriculum, campaigns, client work, and video production so projects keep moving without stalling.",
    responsibilities: [
      { group: "Project Ownership", items: [
        "Manage multiple projects from concept to execution to completion.",
        "Define scope, deliverables, timelines, milestones, and dependencies.",
        "Maintain project plans, trackers, and accountability systems.",
      ]},
      { group: "Team & Contractor Coordination", items: [
        "Coordinate leadership, staff, contractors, designers, writers, editors, and vendors.",
        "Run project meetings, document decisions, and follow up on action items.",
        "Communicate status, deadlines, and risks; surface bottlenecks and stalled tasks early.",
      ]},
      { group: "Operations & Process", items: [
        "Build repeatable systems, templates, and workflows.",
        "Improve internal communication, handoffs, and project tracking.",
      ]},
    ],
    required: [
      "Proven project, operations, or production-coordination experience.",
      "Strong planning and execution skills across several complex projects at once.",
      "Clear communication across different roles and personalities.",
      "Comfortable creating structure in an entrepreneurial environment.",
      "Proficient with Google Workspace and collaboration tools.",
      "Professional maturity, flexibility, and sound judgment.",
    ],
    preferred: [
      "Publishing, curriculum, ministry, media, nonprofit, or campaign experience.",
      "Familiarity with Asana, ClickUp, Monday.com, Trello, Notion, or Airtable.",
      "Experience working with authors, pastors, designers, editors, and vendors.",
      "A track record of building systems for growing organizations.",
    ],
    success: [
      "Projects have clear owners, timelines, and next steps — and keep moving.",
      "Fewer dropped details, missed deadlines, and unclear handoffs.",
      "Contractors and team members know what is due and when.",
      "Leadership is freed to focus on vision and relationships.",
    ],
  },
  {
    title: "3. AI & Technology Integration Specialist",
    summary: "Helps the team use AI, automation, and digital tools to produce content faster and operate more efficiently — translating emerging technology into practical, usable workflows for a non-technical team. Less about experimenting, more about shipping resources better.",
    responsibilities: [
      { group: "AI Workflow Development", items: [
        "Build AI-assisted workflows for content creation, editing, summarization, research, and repurposing.",
        "Use tools like ChatGPT and Claude to turn notes, transcripts, and outlines into usable drafts.",
        "Create prompt libraries, workflow templates, and documentation.",
      ]},
      { group: "Technology & Systems", items: [
        "Evaluate and implement AI tools, automation platforms, and integrations.",
        "Connect tools such as Google Workspace, AI platforms, and project management software.",
        "Automate repetitive tasks and reduce manual administrative work.",
      ]},
      { group: "Training & Knowledge", items: [
        "Train staff on AI tools and digital workflows in plain language.",
        "Organize institutional knowledge, reusable content, and project assets.",
      ]},
    ],
    required: [
      "Strong working knowledge of AI tools such as ChatGPT, Claude, or similar.",
      "Quick to learn new technology and apply it to practical needs.",
      "Able to design workflows, document processes, and train others.",
      "Strong problem-solving and written communication.",
      "Comfortable with Google Workspace and collaboration tools.",
    ],
    preferred: [
      "Experience with prompt engineering, automation, or systems implementation.",
      "Familiarity with Zapier, Make, Airtable, Notion, ClickUp, Canva, WordPress, Kajabi, or GoHighLevel.",
      "Background in publishing, curriculum, marketing, media, or digital products.",
      "Experience building SOPs, dashboards, templates, or resource libraries.",
    ],
    success: [
      "AI becomes a practical, repeatable part of daily work.",
      "Content development, editing, and research get faster.",
      "Prompt libraries and process documentation exist and stay current.",
      "Knowledge and reusable content are easy to access.",
    ],
  },
  {
    title: "4. Content & Production Coordinator",
    summary: "Coordinates publishing, curriculum, video, print, and digital projects from concept to completion — managing schedules, assets, vendors, and revisions so high-quality resources ship on time and with excellence.",
    responsibilities: [
      { group: "Production Coordination", items: [
        "Run production workflows for books, devotionals, curriculum, campaigns, video, and digital resources.",
        "Maintain production schedules, asset trackers, and deliverable lists.",
        "Track drafts, scripts, graphics, videos, and print files through review and approval.",
      ]},
      { group: "Creative & Vendor Coordination", items: [
        "Coordinate writers, editors, designers, video teams, and print vendors.",
        "Manage vendor quotes, timelines, file handoffs, and production specs.",
        "Handle video logistics: scripts, schedules, shot lists, edits, and final files.",
      ]},
      { group: "Asset & Deliverable Management", items: [
        "Maintain naming conventions, version control, and asset libraries.",
        "Prepare content for publication, print, digital distribution, or campaign use.",
      ]},
    ],
    required: [
      "Experience in production, content, or creative project coordination.",
      "Excellent organization and attention to detail.",
      "Able to manage multiple deadlines and deliverables at once.",
      "Strong communication with creatives, vendors, and stakeholders.",
      "Comfortable with digital file management and production tracking.",
      "Proficient with Google Workspace.",
    ],
    preferred: [
      "Christian publishing, church curriculum, or ministry/media production experience.",
      "Coordinating books, curriculum, sermon resources, campaigns, or downloads.",
      "Familiarity with Canva, Adobe tools, WordPress, course platforms, or DAM systems.",
      "Understanding of review cycles, proofing, approvals, and delivery.",
    ],
    success: [
      "Projects are scheduled, tracked, and completed with fewer delays.",
      "Assets and files are organized and easy to find.",
      "Vendors and contributors get timely, accurate information.",
      "Resources move smoothly from concept to final delivery.",
    ],
  },
];

// ---- assemble document ----
const cover = [
  new Paragraph({
    spacing: { after: 40 },
    children: [new TextRun({ text: "LifeTogether", bold: true, size: 44, color: NAVY })],
  }),
  new Paragraph({
    spacing: { after: 200 },
    border: { bottom: { style: BorderStyle.SINGLE, size: 8, color: ACCENT, space: 4 } },
    children: [new TextRun({ text: "Staffing Overview", size: 28, color: ACCENT })],
  }),
  para([new TextRun("We're a Christian publishing, curriculum, production, and ministry organization. We create books, devotionals, church campaigns, small group curriculum, leadership resources, video training, and print and digital products. The environment is mission-driven, entrepreneurial, and fast-moving.")]),
  para([new TextRun("We're hiring for the four roles below. Each helps us increase execution capacity, strengthen follow-through, and complete more high-quality resources.")]),
  metaLine("Location", "Primarily in-office preferred"),
  metaLine("Employment", "Full-time preferred for initial hires; fractional, contract, or temp-to-hire considered for specialized roles"),
  metaLine("Compensation", "Based on role, experience, and structure"),
  new Paragraph({
    spacing: { before: 160, after: 0 },
    children: [new TextRun({
      text: "All roles call for someone organized, detail-oriented, proactive, and digitally fluent, who works well in a fast-moving setting and is comfortable supporting a faith-based mission and ministry partners.",
    })],
  }),
];

const children = [...cover];
roles.forEach((r) => children.push(...role(r, false)));

const doc = new Document({
  styles: {
    default: { document: { run: { font: "Arial", size: 24 } }, paragraph: { spacing: { line: 264 } } },
    paragraphStyles: [
      { id: "Heading1", name: "Heading 1", basedOn: "Normal", next: "Normal", quickFormat: true,
        run: { size: 32, bold: true, font: "Arial", color: NAVY },
        paragraph: { spacing: { before: 0, after: 160 }, outlineLevel: 0 } },
      { id: "Heading2", name: "Heading 2", basedOn: "Normal", next: "Normal", quickFormat: true,
        run: { size: 24, bold: true, font: "Arial", color: ACCENT },
        paragraph: { spacing: { before: 260, after: 100 }, outlineLevel: 1 } },
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
  fs.writeFileSync("/home/claude/LifeTogether-Staffing.docx", buffer);
  console.log("written");
});
