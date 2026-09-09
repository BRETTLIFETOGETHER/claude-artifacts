const {
  Document, Packer, Paragraph, TextRun, HeadingLevel, AlignmentType,
  BorderStyle, Table, TableRow, TableCell, WidthType, ShadingType,
  Numbering, LevelFormat, PageBreak
} = require("docx");
const fs = require("fs");

const NAVY = "1F2937";
const GOLD = "9C6B1F";
const GREY = "5B6472";

function H1(text) {
  return new Paragraph({
    heading: HeadingLevel.HEADING_1,
    spacing: { before: 360, after: 160 },
    border: { bottom: { style: BorderStyle.SINGLE, size: 6, color: GOLD, space: 6 } },
    children: [new TextRun({ text, bold: true, color: NAVY, size: 30 })],
  });
}
function H2(text) {
  return new Paragraph({
    heading: HeadingLevel.HEADING_2,
    spacing: { before: 240, after: 100 },
    children: [new TextRun({ text, bold: true, color: NAVY, size: 24 })],
  });
}
function P(text, opts = {}) {
  return new Paragraph({
    spacing: { after: 160, line: 300 },
    children: [new TextRun({ text, size: 22, color: "222222", italics: !!opts.italics })],
  });
}
function Bullet(text) {
  return new Paragraph({
    spacing: { after: 90, line: 280 },
    bullet: { level: 0 },
    children: [new TextRun({ text, size: 22, color: "222222" })],
  });
}
function LabelBullet(label, text) {
  return new Paragraph({
    spacing: { after: 90, line: 280 },
    bullet: { level: 0 },
    children: [
      new TextRun({ text: label + " — ", bold: true, size: 22, color: NAVY }),
      new TextRun({ text, size: 22, color: "222222" }),
    ],
  });
}
function Quote(text) {
  return new Paragraph({
    spacing: { before: 120, after: 200, line: 300 },
    indent: { left: 360 },
    border: { left: { style: BorderStyle.SINGLE, size: 18, color: GOLD, space: 8 } },
    children: [new TextRun({ text, italics: true, size: 22, color: NAVY })],
  });
}

const doc = new Document({
  numbering: {
    config: [{
      reference: "bullets",
      levels: [{ level: 0, format: LevelFormat.BULLET, text: "\u2022", alignment: AlignmentType.LEFT,
        style: { paragraph: { indent: { left: 360, hanging: 260 } } } }],
    }],
  },
  sections: [{
    properties: { page: { size: { width: 12240, height: 15840 }, margin: { top: 1440, bottom: 1440, left: 1350, right: 1350 } } },
    children: [
      // Title block
      new Paragraph({ spacing: { before: 800, after: 60 }, alignment: AlignmentType.LEFT,
        children: [new TextRun({ text: "A WHITE PAPER FOR FAMILY OFFICE LEADERSHIP", bold: true, color: GOLD, size: 20 })] }),
      new Paragraph({ spacing: { before: 120, after: 200 },
        children: [new TextRun({ text: "The AI and Automation Question for Family Offices", bold: true, color: NAVY, size: 44 })] }),
      new Paragraph({ spacing: { after: 500 },
        children: [new TextRun({ text: "Adopting New Tools Without Losing the Personal Touch That Defines You", italics: true, color: GREY, size: 26 })] }),

      H1("Executive Summary"),
      P("Every family office is being asked the same question right now, whether or not anyone has said it out loud: should we be using AI, and how far should that go? The pressure is real. Reporting is getting more complex, cyber threats are getting sharper, staff time is scarce, and the family is reading the same headlines everyone else is reading."),
      P("This paper does not argue for or against adoption. It argues for a specific way of deciding — one that treats technology as a tool for protecting and extending what makes a family office valuable in the first place, rather than a force that quietly erodes it. The office that gets this right will move faster, cost less to run, and be trusted more, not less. The office that gets it wrong will save some hours and lose something the family can feel but can't quite name."),

      H1("1. The Question Behind the Question"),
      P("\u201cShould we adopt AI\u201d is rarely the real question a family office is wrestling with. The real question is usually one of these:"),
      Bullet("Can we modernize without the family feeling like they've been handed off to a system?"),
      Bullet("Can we compete for talent and efficiency without exposing the family to new risk?"),
      Bullet("Can we prove we're still worth what we cost, in an era when a robo-advisor can produce a report in seconds?"),
      P("Framed that way, the question stops being about technology at all. It becomes a question about what the office is actually for. A family office earns its keep through judgment, discretion, and relationship — the things a family cannot get from a bank, an RIA, or a piece of software. Any adoption decision should be tested against a single standard: does this tool protect more time and attention for the things only a human can do, or does it quietly replace the reason the family hired people instead of a platform?"),

      H1("2. What's Actually at Risk on Both Sides"),
      H2("The cost of waiting"),
      Bullet("Reporting and reconciliation that takes days instead of hours, at a time when families increasingly expect real-time visibility."),
      Bullet("A cybersecurity posture built for a smaller, simpler operation than the one you're actually running today."),
      Bullet("Staff spending senior judgment on work a well-configured tool could handle, while the relationship work that actually justifies the office's cost gets squeezed into whatever time is left."),
      Bullet("A widening gap between what the rising generation expects from any service provider and what the office can currently deliver."),
      H2("The cost of moving too fast"),
      Bullet("Sensitive family information — health, estate, conflict, succession — entered into tools without a clear, deliberate answer to where that data goes and who can see it."),
      Bullet("A family that feels like a queue of requests rather than a relationship, because the tone of every interaction has quietly shifted to match the tool."),
      Bullet("Automation applied to a judgment call that actually needed a human being to sit with the discomfort of it — a distribution request tangled in family conflict, a succession conversation, a moment that called for presence, not efficiency."),
      Bullet("Vendor risk taken on without the same diligence the office would apply to any other advisor with access to the family's affairs."),

      H1("3. A Framework for Deciding What to Automate"),
      P("Sort every candidate for automation into one of three zones before adopting it. This alone prevents most of the damage family offices report after moving too fast."),
      LabelBullet("Zone One — Automate Freely", "Work that is repetitive, low-risk if imperfect, and invisible to the family when done well: document filing and retrieval, calendar and travel logistics, routine reconciliation, first-pass report assembly, meeting transcription for internal use."),
      LabelBullet("Zone Two — Automate With Oversight", "Work where a tool can do the first draft but a person must review before anything reaches the family: investment research summaries, tax document preparation, compliance monitoring, communication drafts, cybersecurity alerting."),
      LabelBullet("Zone Three — Never Automate", "Work where the human presence is the entire point: family meetings, succession and estate conversations, conflict mediation, delivering difficult news, discretion calls about what one family member should know about another, anything touching grief, addiction, estrangement, or a family's hardest seasons."),
      P("The mistake most offices make isn't choosing the wrong zone for an individual task — it's skipping the exercise entirely and adopting tools function by function, vendor by vendor, without ever stepping back to ask which zone they're actually operating in."),

      H1("4. Where AI Genuinely Helps Today"),
      Bullet("Aggregating multi-custodian reporting into a single, accurate view faster than any manual process."),
      Bullet("Flagging anomalies in transactions or communications before they become real problems."),
      Bullet("Drafting first-pass summaries of dense investment materials for a principal's time-constrained review."),
      Bullet("Managing document retention and retrieval across decades of family and entity records."),
      Bullet("Strengthening — not replacing — cybersecurity monitoring, which is exactly where family offices are most exposed."),
      Bullet("Capturing and organizing family history and interview material so it's actually usable later, rather than sitting in a drawer of old recordings."),

      H1("5. Where the Personal Touch Must Stay Human"),
      P("These are not places to \u201cuse AI carefully.\u201d They are places not to use it at all, regardless of how capable the tool becomes."),
      Bullet("The conversation where a family member is told something they don't want to hear."),
      Bullet("Any moment that requires reading a room, a relationship, or a family history the software has no access to."),
      Bullet("Succession and legacy conversations, where the value is entirely in the presence, not the efficiency."),
      Bullet("Conflict between family members, where the office's neutrality has to be felt, not just claimed."),
      Bullet("The judgment call about what one part of the family should be told about another — this is a trust decision, not a data question."),

      H1("6. Data Security and Confidentiality: The Non-Negotiables"),
      P("Family offices are already a disproportionately attractive cyber target relative to their size, precisely because they hold enormous sensitive information with historically thin security budgets. Every new tool multiplies that exposure unless these are answered in writing before adoption, not after:"),
      Bullet("Where does the family's data actually live once it enters this tool, and who else can access it?"),
      Bullet("Does the vendor train its models on your data, and can that be contractually prohibited?"),
      Bullet("What happens to the data if you stop using the tool?"),
      Bullet("Would you be comfortable if the family asked you these exact questions directly?"),
      P("If the honest answer to the last question is no, the tool isn't ready for family data yet, regardless of how much time it would save."),

      H1("7. A 90-Day First Step"),
      P("Start narrow. Start in Zone One. Prove it before expanding."),
      LabelBullet("Days 1\u201330", "Sort your current workload into the three zones. Pick one Zone One task to automate — something low-risk and currently consuming real staff time."),
      LabelBullet("Days 31\u201360", "Run it in parallel with the existing manual process. Measure time saved and error rate honestly. Ask the questions in Section 6 of any vendor involved."),
      LabelBullet("Days 61\u201390", "Retire the manual process only if the parallel run earned it. Document what you learned. Choose the next candidate — still from Zone One or a well-bounded Zone Two task — before touching anything in Zone Three."),
      P("This is deliberately unglamorous. The offices that adopt well are rarely the ones that moved fastest — they're the ones that never had to walk anything back after a family noticed."),

      H1("8. Ten Questions to Ask Before Adopting Any New Tool"),
      Bullet("Which zone does this task belong in, and does the tool match that zone?"),
      Bullet("What would we tell the family we're doing with this, if they asked directly?"),
      Bullet("Who reviews the output before it reaches a family member?"),
      Bullet("What happens to our data if this vendor is acquired or shuts down?"),
      Bullet("Does this tool make our smallest team member more capable, or does it make them replaceable?"),
      Bullet("Have we tested this on a low-stakes task before trusting it with a high-stakes one?"),
      Bullet("Does adopting this change the tone of how we interact with the family, even subtly?"),
      Bullet("What's our rollback plan if this doesn't work the way we expect?"),
      Bullet("Who on our team actually understands this well enough to catch it if it's wrong?"),
      Bullet("A year from now, will this have given us more time for the family, or less?"),

      H1("Closing: Technology as a Tool for Deeper Relationship"),
      Quote("The families who stay with a family office for decades don't stay because of the reporting software. They stay because someone who genuinely knows them picked up the phone."),
      P("The right question was never \u201cAI or no AI.\u201d It's whether every tool your office adopts leaves more room for that phone call, or less. Used well, automation is what protects the personal touch — it clears away the work that was never the reason the family hired you, so the people on your team can spend their best hours on the work that was."),
      P("That is the positive direction worth moving in: not the fastest adoption, and not the most cautious refusal, but the discipline of asking, every time, which zone this belongs in — and refusing to let convenience make that call for you."),
    ],
  }],
});

Packer.toBuffer(doc).then((buf) => {
  fs.writeFileSync("/mnt/user-data/outputs/family-office-ai-automation-white-paper.docx", buf);
  console.log("written");
});
