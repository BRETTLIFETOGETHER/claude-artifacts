const {
  Document, Packer, Paragraph, TextRun,
  AlignmentType, BorderStyle, ShadingType, WidthType,
  Table, TableRow, TableCell, VerticalAlign
} = require('docx');
const fs = require('fs');

const NAVY = "1B3A5C";
const GOLD = "B8832A";
const LIGHT = "F4F8FC";
const WHITE = "FFFFFF";
const GRAY = "666666";
const LGRAY = "E8E8E8";

const movements = [
  {
    label: "MOVEMENT ONE",
    title: "The Question That Changes Everything",
    days_label: "Days 1–7",
    color: "1B3A5C",
    days: [
      { n: 1, title: "The Car Keys and the Kingdom", sub: "What Changes When the Owner Walks In" },
      { n: 2, title: "The Iceberg and the Invisible Life", sub: "Why What You Believe About Money Shows Up in Everything" },
      { n: 3, title: "Three Questions You've Been Asking Wrong", sub: "Trading \"Will I Ever Have Enough?\" for a Better Question" },
      { n: 4, title: "Money as Tool, Test, and Testimony", sub: "The Three Ways God Uses Your Finances to Shape You" },
      { n: 5, title: "Owners Grip. Stewards Receive.", sub: "What Open Hands Actually Feel Like" },
      { n: 6, title: "The Steward's Job Description", sub: "Using God's Resources to Accomplish God's Plans" },
      { n: 7, title: "The Faked Life", sub: "Why Stewardship Is the One Thing You Cannot Pretend" },
    ]
  },
  {
    label: "MOVEMENT TWO",
    title: "Principles That Don't Move",
    days_label: "Days 8–14",
    color: "1F5C7A",
    days: [
      { n: 8,  title: "The Principle That Makes All the Others Possible", sub: "Spending Less Than You Earn Is Not a Budget Tip — It's a Theology" },
      { n: 9,  title: "Giving Breaks What Accumulation Cannot", sub: "Why Generosity Is the Antidote to Money's Power Over You" },
      { n: 10, title: "The Dangerous Master", sub: "What Debt Does to Your Future Before the Future Arrives" },
      { n: 11, title: "The Ant Knows Something You Don't", sub: "Planning for What You Cannot See Is Called Wisdom, Not Worry" },
      { n: 12, title: "Every Goal Is a Statement of Faith", sub: "Why Nehemiah's Building Plan Is Also Your Financial Plan" },
      { n: 13, title: "The Longer Your View, the Better Your Decisions", sub: "Three Truths About Financial Decision-Making That Change Everything" },
      { n: 14, title: "The Checkbook That Doesn't Lie", sub: "When Your Spending Plan Becomes a Discipleship Document" },
    ]
  },
  {
    label: "MOVEMENT THREE",
    title: "Learning the Secret of Enough",
    days_label: "Days 15–21",
    color: "2D6E3E",
    days: [
      { n: 15, title: "The American Dream and the Paradox Inside It", sub: "More Choices Is Not the Same Thing as More Freedom" },
      { n: 16, title: "The Answer Was Always What You Already Have", sub: "Hebrews 13:5 and the Question That Finally Has an Answer" },
      { n: 17, title: "Materialism Is Not About How Much You Own", sub: "What a Mud Hut and a D Battery Taught Ron Blue About Worship" },
      { n: 18, title: "Contentment Is Learned, Not Inherited", sub: "The Apostle Paul Said He Had to Practice This — So Do You" },
      { n: 19, title: "Setting a Finish Line in a Culture That Never Does", sub: "The Freedom That Comes When You Decide \"This Is Enough\"" },
      { n: 20, title: "Provision, Contentment, Enjoyment", sub: "What 1 Timothy Says Is Actually the Right Christian Lifestyle" },
      { n: 21, title: "Your Spending Plan Is How You Show Up to the Conversation", sub: "Delayed Gratification Is the Only Way to Expand What's Available" },
    ]
  },
  {
    label: "MOVEMENT FOUR",
    title: "You Can't Take It With You — But You Can Send It Ahead",
    days_label: "Days 22–28",
    color: "6B3080",
    days: [
      { n: 22, title: "You're About to Talk About the Sensitive Thing", sub: "Why Giving Makes People Nervous and What That Reveals" },
      { n: 23, title: "The Five Reasons the Bible Says to Give", sub: "And the One That Surprised Even Ron Blue" },
      { n: 24, title: "Tithing Is the Training Wheels", sub: "What Happens When You Decide the Floor Is Just the Beginning" },
      { n: 25, title: "The Treasure Principle That Changes Everything", sub: "You Can't Take It With You — But You Can Send It Ahead" },
      { n: 26, title: "Howard Hughes and the Prison Money Built", sub: "What Happens to the Soul That Refuses to Give" },
      { n: 27, title: "Conduits, Not Containers", sub: "We Need the Money to Flow Through Us, Not Stop with Us" },
      { n: 28, title: "Joy Always Follows Generosity", sub: "Why This Is Not a Coincidence but a Design" },
    ]
  },
  {
    label: "MOVEMENT FIVE",
    title: "The Weight We Were Not Meant to Carry",
    days_label: "Days 29–33",
    color: "7A3A1A",
    days: [
      { n: 29, title: "You Are a Slave to Someone", sub: "The Question Is Only to Whom" },
      { n: 30, title: "Presuming on What Only God Knows", sub: "The Spiritual Danger Inside Every Loan Agreement" },
      { n: 31, title: "Getting In Is Easy. Getting Out Is a Different Story.", sub: "The Magic of Compounding Works Against You When You Owe" },
      { n: 32, title: "Financial Issues Are Symptoms of Heart Issues", sub: "What Your Debt and Your Tax Return Are Really Telling You" },
      { n: 33, title: "The Toothpaste and the Lesson You Can't Unlearn", sub: "Why the Time to Make Good Decisions Is Before You Need To" },
    ]
  },
  {
    label: "MOVEMENT SIX",
    title: "Faithful with Little, Trusted with Much",
    days_label: "Days 34–40",
    color: "1B3A5C",
    days: [
      { n: 34, title: "The Five Stages and Where You Are Right Now", sub: "Struggling, Surviving, Stable, Secure, or Surplus — And the One Way Through" },
      { n: 35, title: "The Magic Is Not What You Think", sub: "A Little Bit Over a Long Time Becomes a Lot" },
      { n: 36, title: "Net Worth Is a Measure of God's Provision", sub: "Not a Scoreboard. Not Your Identity. His." },
      { n: 37, title: "Stewardship Transforms Relationships", sub: "What Happens When Couples Pray Over the Spending Plan Together" },
      { n: 38, title: "Legacy Is Not What You Leave After You Die", sub: "It Is What You Live While You Are Alive" },
      { n: 39, title: "Write the Letter Your Family Needs to Read", sub: "The Most Valuable Thing You'll Leave Behind May Have No Dollar Amount" },
      { n: 40, title: "Well Done, Good and Faithful Servant", sub: "The Only Return on Investment That Will Matter When Everything Is Gone" },
    ]
  }
];

// Build rows for the table
function makeMovementHeaderRow(mov) {
  return new TableRow({
    children: [
      new TableCell({
        columnSpan: 3,
        shading: { fill: mov.color, type: ShadingType.CLEAR },
        margins: { top: 60, bottom: 60, left: 120, right: 120 },
        borders: {
          top: { style: BorderStyle.NONE }, bottom: { style: BorderStyle.NONE },
          left: { style: BorderStyle.NONE }, right: { style: BorderStyle.NONE }
        },
        children: [
          new Paragraph({
            children: [
              new TextRun({ text: `${mov.label}  ·  `, bold: true, size: 16, color: "FFFFFF", font: "Arial" }),
              new TextRun({ text: mov.title, bold: true, size: 16, color: "FFFFFF", font: "Arial" }),
              new TextRun({ text: `   ${mov.days_label}`, size: 15, color: "CCDDEE", font: "Arial", italics: true }),
            ],
            alignment: AlignmentType.LEFT
          })
        ]
      })
    ]
  });
}

function makeDayRow(day, shade) {
  const bg = shade ? "F7F9FC" : "FFFFFF";
  const cellBorders = {
    top: { style: BorderStyle.NONE }, bottom: { style: BorderStyle.NONE },
    left: { style: BorderStyle.NONE }, right: { style: BorderStyle.NONE }
  };
  const cellMargins = { top: 40, bottom: 40, left: 100, right: 80 };

  return new TableRow({
    children: [
      // Day number
      new TableCell({
        width: { size: 500, type: WidthType.DXA },
        shading: { fill: bg, type: ShadingType.CLEAR },
        borders: cellBorders,
        margins: cellMargins,
        verticalAlign: VerticalAlign.CENTER,
        children: [
          new Paragraph({
            alignment: AlignmentType.CENTER,
            children: [new TextRun({ text: String(day.n), bold: true, size: 17, color: NAVY, font: "Arial" })]
          })
        ]
      }),
      // Title
      new TableCell({
        width: { size: 4300, type: WidthType.DXA },
        shading: { fill: bg, type: ShadingType.CLEAR },
        borders: cellBorders,
        margins: cellMargins,
        verticalAlign: VerticalAlign.CENTER,
        children: [
          new Paragraph({
            children: [new TextRun({ text: day.title, bold: true, size: 17, color: "1A1A1A", font: "Arial" })]
          })
        ]
      }),
      // Subtitle
      new TableCell({
        width: { size: 4560, type: WidthType.DXA },
        shading: { fill: bg, type: ShadingType.CLEAR },
        borders: cellBorders,
        margins: cellMargins,
        verticalAlign: VerticalAlign.CENTER,
        children: [
          new Paragraph({
            children: [new TextRun({ text: day.subtitle || day.sub, italics: true, size: 16, color: GRAY, font: "Arial" })]
          })
        ]
      })
    ]
  });
}

const rows = [];

for (const mov of movements) {
  rows.push(makeMovementHeaderRow(mov));
  mov.days.forEach((day, i) => {
    rows.push(makeDayRow(day, i % 2 === 0));
  });
}

const table = new Table({
  width: { size: 9360, type: WidthType.DXA },
  columnWidths: [500, 4300, 4560],
  borders: {
    top: { style: BorderStyle.NONE }, bottom: { style: BorderStyle.NONE },
    left: { style: BorderStyle.NONE }, right: { style: BorderStyle.NONE },
    insideH: { style: BorderStyle.NONE }, insideV: { style: BorderStyle.NONE }
  },
  rows
});

const doc = new Document({
  styles: {
    default: { document: { run: { font: "Arial", size: 17 } } }
  },
  sections: [{
    properties: {
      page: {
        size: { width: 12240, height: 15840 },
        margin: { top: 720, right: 720, bottom: 720, left: 720 }
      }
    },
    children: [
      // Header
      new Paragraph({
        children: [
          new TextRun({ text: "GOD OWNS IT ALL", bold: true, size: 28, color: NAVY, font: "Arial" }),
          new TextRun({ text: "   ·   A 40-Day Devotional", size: 22, color: GOLD, font: "Arial", italics: true }),
        ],
        spacing: { before: 0, after: 80 }
      }),
      new Paragraph({
        border: { bottom: { style: BorderStyle.SINGLE, size: 8, color: GOLD, space: 1 } },
        spacing: { before: 0, after: 120 },
        children: []
      }),
      // Column headers
      new Table({
        width: { size: 9360, type: WidthType.DXA },
        columnWidths: [500, 4300, 4560],
        borders: {
          top: { style: BorderStyle.NONE }, bottom: { style: BorderStyle.SINGLE, size: 4, color: "CCCCCC" },
          left: { style: BorderStyle.NONE }, right: { style: BorderStyle.NONE },
          insideH: { style: BorderStyle.NONE }, insideV: { style: BorderStyle.NONE }
        },
        rows: [
          new TableRow({
            children: [
              new TableCell({
                width: { size: 500, type: WidthType.DXA },
                borders: { top: { style: BorderStyle.NONE }, bottom: { style: BorderStyle.SINGLE, size: 4, color: "CCCCCC" }, left: { style: BorderStyle.NONE }, right: { style: BorderStyle.NONE } },
                margins: { top: 20, bottom: 40, left: 100, right: 80 },
                children: [new Paragraph({ alignment: AlignmentType.CENTER, children: [new TextRun({ text: "DAY", bold: true, size: 14, color: GRAY, font: "Arial" })] })]
              }),
              new TableCell({
                width: { size: 4300, type: WidthType.DXA },
                borders: { top: { style: BorderStyle.NONE }, bottom: { style: BorderStyle.SINGLE, size: 4, color: "CCCCCC" }, left: { style: BorderStyle.NONE }, right: { style: BorderStyle.NONE } },
                margins: { top: 20, bottom: 40, left: 100, right: 80 },
                children: [new Paragraph({ children: [new TextRun({ text: "TITLE", bold: true, size: 14, color: GRAY, font: "Arial" })] })]
              }),
              new TableCell({
                width: { size: 4560, type: WidthType.DXA },
                borders: { top: { style: BorderStyle.NONE }, bottom: { style: BorderStyle.SINGLE, size: 4, color: "CCCCCC" }, left: { style: BorderStyle.NONE }, right: { style: BorderStyle.NONE } },
                margins: { top: 20, bottom: 40, left: 100, right: 80 },
                children: [new Paragraph({ children: [new TextRun({ text: "SUBTITLE", bold: true, size: 14, color: GRAY, font: "Arial" })] })]
              })
            ]
          })
        ]
      }),
      new Paragraph({ children: [], spacing: { before: 0, after: 60 } }),
      table,
      // Footer rule
      new Paragraph({
        border: { top: { style: BorderStyle.SINGLE, size: 6, color: GOLD, space: 1 } },
        spacing: { before: 120, after: 40 },
        children: []
      }),
      new Paragraph({
        children: [new TextRun({ text: "Ron Blue Institute  ·  God Owns It All  ·  40-Day Devotional Framework", size: 14, color: GRAY, font: "Arial", italics: true })],
        alignment: AlignmentType.CENTER
      })
    ]
  }]
});

Packer.toBuffer(doc).then(buffer => {
  fs.writeFileSync("/mnt/user-data/outputs/GOIA_40Day_Contents.docx", buffer);
  console.log("Done.");
}).catch(e => { console.error(e); process.exit(1); });
