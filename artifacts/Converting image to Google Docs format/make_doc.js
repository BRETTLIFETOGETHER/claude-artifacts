const {
  Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell,
  WidthType, ShadingType, AlignmentType, HeadingLevel, BorderStyle, VerticalAlign
} = require('docx');
const fs = require('fs');

const rows = [
  ["1", "Oceans.com", "Chad Price", "40 Days of Whispers"],
  ["2", "Hobby Lobby", "Mart Green", "The Great Commission"],
  ["3", "Excellence in Giving", "Al Muller", "Giving Pledge / Intentional Giving"],
  ["4", "Signatry", "Dale Armstrong, Steve French", "Generosity Campaign"],
  ["4", "Impact Foundation", "Jeff Johns, Amy Mince", "40 Days of Impact Investing"],
  ["5", "Oceans Church", "Mark Francey", "40 Days of New Life, 40 Days of New Hope"],
  ["6", "Faith Fi", "Rob West", "Faith & Finances"],
  ["6", "Generous Giving", "Todd Harper", "40 Days of Abundance"],
  ["6", "Timothy Project", "Rick Reynolds", "Timothy Project"],
  ["7", "Blue Trust", "Russ Crosson", "40 Days of Giving"],
  ["7", "Masters Program", "Jeff Smith / Bob Shank", "40 Days of Life Mastery"],
  ["8", "Generous Giving", "April Chapman", "40 Days of Generosity"],
  ["8", "Purpose Driven Life", "Rick Warren", "Family Legacy / Stewardship"],
  ["9", "Kingdom Advisors", "Sharon Epps", "Redeeming Money"],
  ["9", "Chick-fil-A", "Dan Cathy", "Generosity Factor"],
  ["10", "New Horizons", "Steve & Greg", "40 Days of Kingdom Giving"],
  ["10", "Compass", "Howard Dayton", "30 Days Finances"],
  ["11", "Revolutionary Philanthropy", "Darryl Heald", "Campaign"],
  ["11", "Convene", "Greg Leith", "Work / Life Balance"],
  ["12", "Solving World's Problems", "Foreman & Kaestner", "Global Impact"],
  ["13", "Christian Stewardship Network", "Chris Goulard", "Stewardship, Generosity"],
  ["13", "C12 Group", "Mike Sharrow", "Work Balance"],
  ["14", "Hobby Lobby / Green", "David Green", "Generous Life"],
  ["14", "Doing Good Better", "Steve Kaloper", "Doing Good Better"],
  ["15", "Living On the Edge", "Chip Ingram", "Generosity Series"],
  ["16", "Women Doing Well", "Julie", "Doing Better Together"],
  ["16", "Bill High", "Bill High", "Generosity Campaign"],
  ["17", "National Christian Foundation", "", "Generosity Campaign"],
  ["18", "Flourishing Families", "David Wills", ""],
  ["18", "Ron Blue Institute", "Ron Blue", "God Owns Your Business"],
  ["20", "Kingdom Economy", "Dale Ahlquist", "Kingdom Economy"],
  ["20", "Lead Like Jesus", "Ken Blanchard", "Lead Like Jesus"],
  ["22", "Movement Mortgage", "Casey Crawford", "40 Days of Movement"],
  ["22", "His Legacy Book", "David York", ""],
  ["23", "FamilyPassion.com", "", "40 Days of Passion"],
  ["25", "Treasure Principle", "Randy Alcorn", ""],
  ["26", "Generous Church", "Patrick Johnson", ""],
  ["27", "Peach State Trucks", "Rick Reynolds", "Purpose Built Business"],
  ["28", "Strategic Resource Group", "Danny Johnson", ""],
  ["29", "Faith Driven Investors", "Justin Forman", "Solving Life's Greatest Problems"],
  ["30", "Bixly", "Adam Temple", "40 Day Campaigns"],
  ["31", "Priority Living", "Bob Shank", "Dream your Calling"],
];

const COLS = [1000, 2900, 2400, 3780];
const NAVY = "1F3864";
const LIGHT = "DCE6F1";

const thinBorder = { style: BorderStyle.SINGLE, size: 4, color: "AFC0D8" };
const cellBorders = { top: thinBorder, bottom: thinBorder, left: thinBorder, right: thinBorder };

function headerCell(text, i) {
  return new TableCell({
    width: { size: COLS[i], type: WidthType.DXA },
    shading: { type: ShadingType.CLEAR, fill: NAVY, color: "auto" },
    borders: cellBorders,
    verticalAlign: VerticalAlign.CENTER,
    margins: { top: 80, bottom: 80, left: 100, right: 100 },
    children: [new Paragraph({
      alignment: i === 0 ? AlignmentType.CENTER : AlignmentType.LEFT,
      spacing: { before: 20, after: 20 },
      children: [new TextRun({ text, bold: true, color: "FFFFFF", size: 21, font: "Calibri" })],
    })],
  });
}

function bodyCell(text, i, shaded) {
  return new TableCell({
    width: { size: COLS[i], type: WidthType.DXA },
    shading: shaded ? { type: ShadingType.CLEAR, fill: LIGHT, color: "auto" } : undefined,
    borders: cellBorders,
    verticalAlign: VerticalAlign.CENTER,
    margins: { top: 60, bottom: 60, left: 100, right: 100 },
    children: [new Paragraph({
      alignment: i === 0 ? AlignmentType.CENTER : AlignmentType.LEFT,
      spacing: { before: 20, after: 20 },
      children: [new TextRun({ text, size: 21, font: "Calibri", bold: i === 1 })],
    })],
  });
}

const table = new Table({
  columnWidths: COLS,
  width: { size: COLS.reduce((a, b) => a + b, 0), type: WidthType.DXA },
  rows: [
    new TableRow({
      tableHeader: true,
      children: ["Priority", "Organization / Partner", "Contact", "Campaign"].map(headerCell),
    }),
    ...rows.map((r, idx) => new TableRow({
      children: r.map((c, i) => bodyCell(c, i, idx % 2 === 1)),
    })),
  ],
});

const doc = new Document({
  styles: {
    default: { document: { run: { font: "Calibri", size: 22 } } },
  },
  sections: [{
    properties: {
      page: {
        size: { width: 12240, height: 15840 },
        margin: { top: 1080, bottom: 1080, left: 1080, right: 1080 },
      },
    },
    children: [
      new Paragraph({
        alignment: AlignmentType.CENTER,
        spacing: { after: 120 },
        children: [new TextRun({ text: "Win Win Kingdom Partners", bold: true, size: 40, color: NAVY, font: "Calibri" })],
      }),
      new Paragraph({
        alignment: AlignmentType.CENTER,
        spacing: { after: 300 },
        border: { bottom: { style: BorderStyle.SINGLE, size: 6, color: NAVY, space: 6 } },
        children: [new TextRun({ text: "Priority partner and campaign list", italics: true, size: 20, color: "555555", font: "Calibri" })],
      }),
      table,
      new Paragraph({ spacing: { before: 300 }, children: [new TextRun({ text: "" })] }),
    ],
  }],
});

Packer.toBuffer(doc).then((buf) => {
  fs.writeFileSync('/mnt/user-data/outputs/Win-Win-Kingdom-Partners.docx', buf);
  console.log('written');
});
