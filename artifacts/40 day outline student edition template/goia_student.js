const {
  Document, Packer, Paragraph, TextRun, HeadingLevel,
  AlignmentType, BorderStyle, LevelFormat, PageNumber,
  ShadingType, WidthType
} = require('docx');
const fs = require('fs');

const BLUE = "1F4E79";
const ACCENT = "2E75B6";
const LIGHT = "D6E4F0";
const GOLD = "BF9000";

function h1(text) {
  return new Paragraph({
    heading: HeadingLevel.HEADING_1,
    spacing: { before: 400, after: 120 },
    border: { bottom: { style: BorderStyle.SINGLE, size: 6, color: ACCENT, space: 6 } },
    children: [new TextRun({ text, font: "Arial", size: 36, bold: true, color: BLUE })]
  });
}

function h2(text) {
  return new Paragraph({
    heading: HeadingLevel.HEADING_2,
    spacing: { before: 280, after: 80 },
    children: [new TextRun({ text, font: "Arial", size: 26, bold: true, color: ACCENT })]
  });
}

function h3(text) {
  return new Paragraph({
    spacing: { before: 200, after: 60 },
    children: [new TextRun({ text, font: "Arial", size: 22, bold: true, color: GOLD })]
  });
}

function dayEntry(day, title, subtitle, scriptures) {
  return [
    new Paragraph({
      spacing: { before: 160, after: 40 },
      children: [
        new TextRun({ text: `Day ${day} — `, font: "Arial", size: 20, bold: true, color: BLUE }),
        new TextRun({ text: title, font: "Arial", size: 20, bold: true }),
      ]
    }),
    new Paragraph({
      spacing: { before: 0, after: 20 },
      indent: { left: 360 },
      children: [new TextRun({ text: subtitle, font: "Arial", size: 20, italics: true, color: "444444" })]
    }),
    new Paragraph({
      spacing: { before: 0, after: 100 },
      indent: { left: 360 },
      children: [new TextRun({ text: scriptures, font: "Arial", size: 18, color: "666666" })]
    }),
  ];
}

function sectionIntro(text) {
  return new Paragraph({
    spacing: { before: 60, after: 160 },
    children: [new TextRun({ text, font: "Arial", size: 20, italics: true, color: "333333" })]
  });
}

function spacer() {
  return new Paragraph({ spacing: { before: 60, after: 60 }, children: [new TextRun("")] });
}

const children = [

  // Title
  new Paragraph({
    alignment: AlignmentType.CENTER,
    spacing: { before: 480, after: 120 },
    children: [new TextRun({ text: "GOD OWNS IT ALL", font: "Arial", size: 56, bold: true, color: BLUE })]
  }),
  new Paragraph({
    alignment: AlignmentType.CENTER,
    spacing: { before: 0, after: 80 },
    children: [new TextRun({ text: "STUDENT EDITION", font: "Arial", size: 36, bold: true, color: ACCENT })]
  }),
  new Paragraph({
    alignment: AlignmentType.CENTER,
    spacing: { before: 0, after: 80 },
    children: [new TextRun({ text: "40-Day Devotional Outline", font: "Arial", size: 26, italics: true, color: "555555" })]
  }),
  new Paragraph({
    alignment: AlignmentType.CENTER,
    spacing: { before: 0, after: 600 },
    children: [new TextRun({ text: "Based on Ron Blue's God Owns It All", font: "Arial", size: 20, color: "777777" })]
  }),

  // Intro
  h1("A Note to Students"),
  new Paragraph({
    spacing: { before: 80, after: 120 },
    children: [new TextRun({
      text: "Money is one of the most confusing — and most talked-about — topics in your world right now. Maybe you're earning your first paycheck. Maybe you're stressed about paying for college. Maybe you've seen your parents fight about finances. Maybe you just can't figure out why your money disappears so fast.",
      font: "Arial", size: 20
    })]
  }),
  new Paragraph({
    spacing: { before: 0, after: 120 },
    children: [new TextRun({
      text: "Here's the thing: Jesus talked about money more than almost any other topic. Not because money is the most important thing — but because the way you handle money reveals what you actually believe. These 40 days aren't about budgeting tips or getting rich. They're about answering one foundational question: if God owns it all, what does that change?",
      font: "Arial", size: 20
    })]
  }),
  new Paragraph({
    spacing: { before: 0, after: 240 },
    children: [new TextRun({
      text: "Give this 5 minutes a day. By Day 40, the way you think about money — and your whole life — will never be the same.",
      font: "Arial", size: 20, bold: true
    })]
  }),

  // HOW TO USE
  h1("How to Use These Devotionals"),
  new Paragraph({
    spacing: { before: 80, after: 80 },
    children: [new TextRun({ text: "Each day includes:", font: "Arial", size: 20, bold: true })]
  }),
  ...[
    "📖  Scripture — Read it slowly. Read it twice.",
    "💡  The Big Idea — The core truth for the day, translated into your world.",
    "🔗  Real Life — A story or scenario from student life: school, work, family, sports, social media.",
    "🔑  Key Thought — One sentence to carry with you.",
    "🙏  Reflect & Pray — One question to sit with. One short prayer to close.",
  ].map(line => new Paragraph({
    spacing: { before: 40, after: 40 },
    indent: { left: 360 },
    children: [new TextRun({ text: line, font: "Arial", size: 20 })]
  })),
  spacer(),

  // ===== SECTION I =====
  h1("SECTION I — THE OWNERSHIP QUESTION"),
  new Paragraph({
    alignment: AlignmentType.CENTER,
    spacing: { before: 60, after: 60 },
    children: [new TextRun({ text: "What Does It Really Mean If God Owns It All?", font: "Arial", size: 24, bold: true, italics: true, color: BLUE })]
  }),
  sectionIntro("Days 1–7 lay the foundation. Before you can make any good financial decision, you need to answer the most basic question: who does this actually belong to? The answer changes everything."),

  ...dayEntry(1, "The Foundation", "God owns it all — and that changes your story", "Romans 11:36; James 1:17"),
  ...dayEntry(2, "The Second Chair", "What it means to let God be in charge of what's 'yours'", "Proverbs 3:5–6; 1 Peter 5:7"),
  ...dayEntry(3, "Your Name on the Label", "Why saying 'It's mine' is the most dangerous habit you can develop", "Deuteronomy 8:17–18; Luke 12:15"),
  ...dayEntry(4, "Owned and Loved", "God's ownership isn't cold or distant — it's personal", "1 Corinthians 6:19–20; Isaiah 43:1"),
  ...dayEntry(5, "The Real Test", "What your money habits reveal about who you actually trust", "Matthew 6:21, 24; Proverbs 3:5–6"),
  ...dayEntry(6, "Anxiety and Ownership", "Most money stress is a control issue in disguise", "Matthew 6:33; Philippians 4:6–7"),
  ...dayEntry(7, "A New Default", "How to start thinking — and living — like a steward", "Colossians 1:16–17; Psalm 50:10–12"),

  spacer(),

  // ===== SECTION II =====
  h1("SECTION II — THE STEWARDSHIP QUESTION"),
  new Paragraph({
    alignment: AlignmentType.CENTER,
    spacing: { before: 60, after: 60 },
    children: [new TextRun({ text: "How Do I Learn to Be Faithful With What I Have?", font: "Arial", size: 24, bold: true, italics: true, color: BLUE })]
  }),
  sectionIntro("Days 8–14 move from idea to practice. Being a steward means managing someone else's stuff well. Whether you have $20 or $2,000, these days show you what faithfulness actually looks like in the real world of a student."),

  ...dayEntry(8, "The Measure of Success", "God grades on faithfulness, not outcomes", "1 Corinthians 4:2; Matthew 25:21"),
  ...dayEntry(9, "Small Things Count", "The way you handle $20 is training for the day you handle $20,000", "Luke 16:10–12; Zechariah 4:10"),
  ...dayEntry(10, "Money as a Tool", "Every spending choice is a value statement", "Matthew 6:19–21; Proverbs 4:26"),
  ...dayEntry(11, "Money as a Test", "What does your Venmo history say about your heart?", "Luke 12:34; Mark 10:21–22"),
  ...dayEntry(12, "Debt and the Future", "When you borrow, you're spending tomorrow's freedom today", "Proverbs 22:7; Romans 13:8"),
  ...dayEntry(13, "The Four Questions", "A biblical filter before you borrow — or buy on credit", "Luke 14:28–30; James 4:13–16"),
  ...dayEntry(14, "Taxes, Tips, and Honesty", "Faithfulness in small financial integrity moments", "Matthew 22:17–21; Romans 13:6–7"),

  spacer(),

  // ===== SECTION III =====
  h1("SECTION III — THE CONFIDENCE QUESTION"),
  new Paragraph({
    alignment: AlignmentType.CENTER,
    spacing: { before: 60, after: 60 },
    children: [new TextRun({ text: "Will I Be Okay?", font: "Arial", size: 24, bold: true, italics: true, color: BLUE })]
  }),
  sectionIntro("Days 15–21 tackle the fear underneath so many money decisions. Am I going to be okay? Will there be enough? These days give you a foundation for real confidence — not based on your bank balance, but on God's faithfulness."),

  ...dayEntry(15, "The Fear Beneath the Surface", "What the question 'Will I be okay?' is really asking", "Psalm 23:1; Isaiah 41:10"),
  ...dayEntry(16, "Seek First", "The confidence strategy Jesus actually gave you", "Matthew 6:31–33; Philippians 4:19"),
  ...dayEntry(17, "The Power of Margin", "Why a little breathing room changes everything", "Proverbs 21:20; Psalm 37:16"),
  ...dayEntry(18, "Four Habits That Build Strength", "Simple practices you can start right now, at your income level", "Proverbs 13:11; Proverbs 21:5"),
  ...dayEntry(19, "Money and Relationships", "Why your money habits affect every relationship you have", "Amos 3:3; Ephesians 4:25"),
  ...dayEntry(20, "Don't Buy Hope", "The trap of spending your way to security", "Proverbs 22:7; Luke 12:15"),
  ...dayEntry(21, "A Calm Next Step", "You don't need to solve everything today — just the next right thing", "Philippians 4:6–9; Proverbs 3:5–6"),

  spacer(),

  // ===== SECTION IV =====
  h1("SECTION IV — THE CONTENTMENT QUESTION"),
  new Paragraph({
    alignment: AlignmentType.CENTER,
    spacing: { before: 60, after: 60 },
    children: [new TextRun({ text: "How Much Is Enough?", font: "Arial", size: 24, bold: true, italics: true, color: BLUE })]
  }),
  sectionIntro("Days 22–28 go after one of the hardest questions in a culture built on 'more.' Social media was literally designed to make you feel like you don't have enough. These days help you define 'enough' before the world does it for you."),

  ...dayEntry(22, "Enough Is a Spiritual Word", "You don't find contentment — you learn it", "Philippians 4:11–13; Hebrews 13:5"),
  ...dayEntry(23, "The Paradox of More", "Why more options often creates more restlessness", "1 Timothy 6:6–10; Ecclesiastes 5:10"),
  ...dayEntry(24, "The Finish Line", "Defining 'enough' before your lifestyle drifts upward without you noticing", "Proverbs 30:8–9; Luke 12:16–21"),
  ...dayEntry(25, "Simplicity Is Not Smallness", "The freedom that comes from fewer masters", "Matthew 6:24; Galatians 5:1"),
  ...dayEntry(26, "Gratitude as a Weapon", "The fastest way to break comparison and complaining", "1 Thessalonians 5:18; Psalm 103:2–5"),
  ...dayEntry(27, "Comparison Is a Thief", "The scroll that steals your peace", "2 Corinthians 10:12; John 21:21–22"),
  ...dayEntry(28, "Peace in Any Season", "Contentment that actually survives bad weeks, broken things, and empty accounts", "Habakkuk 3:17–19; Psalm 16:5–6"),

  spacer(),

  // ===== SECTION V =====
  h1("SECTION V — THE GENEROSITY QUESTION"),
  new Paragraph({
    alignment: AlignmentType.CENTER,
    spacing: { before: 60, after: 60 },
    children: [new TextRun({ text: "How Does Giving Change Everything?", font: "Arial", size: 24, bold: true, italics: true, color: BLUE })]
  }),
  sectionIntro("Days 29–35 flip the script. Most students think generosity is for later — when they have 'real' money. These days show you that generosity is the one habit that can rewire your relationship with money right now, regardless of how much you have."),

  ...dayEntry(29, "God Is the First Giver", "Generosity starts in the gospel, not in your wallet", "John 3:16; Romans 8:32"),
  ...dayEntry(30, "Open Hands, Open Heart", "Why giving is the one practice that actually breaks money's grip on you", "Matthew 6:21; Luke 12:34"),
  ...dayEntry(31, "Cheerful, Not Pressured", "The kind of generosity God actually forms in you", "2 Corinthians 9:6–8; Exodus 35:21"),
  ...dayEntry(32, "Consistent Giving", "Percentage giving beats emotional giving every time", "1 Corinthians 16:2; Proverbs 3:9–10"),
  ...dayEntry(33, "Spontaneous Generosity", "Being ready to meet needs when God prompts — even when it's inconvenient", "Acts 4:32–35; Proverbs 19:17"),
  ...dayEntry(34, "Whole-Life Generosity", "Money is just one form — what about your time, your skills, your platform?", "Ephesians 2:10; Acts 20:35"),
  ...dayEntry(35, "The Joy That Returns", "The surprising fruit that comes from a generous life", "Proverbs 11:24–25; Isaiah 58:10–11"),

  spacer(),

  // ===== SECTION VI =====
  h1("SECTION VI — THE IMPACT QUESTION"),
  new Paragraph({
    alignment: AlignmentType.CENTER,
    spacing: { before: 60, after: 60 },
    children: [new TextRun({ text: "Making an Impact Today, Tomorrow, and Eternally", font: "Arial", size: 24, bold: true, italics: true, color: BLUE })]
  }),
  sectionIntro("Days 36–42 zoom out to the big picture. You are not too young to make a lasting impact. These days call you to think beyond your generation — to live, give, and invest in ways that will still matter long after you're gone."),

  ...dayEntry(36, "Treasure Has a Direction", "You're always investing in something — choose wisely", "Matthew 6:19–21; Colossians 3:1–2"),
  ...dayEntry(37, "Decide Before the Pressure Hits", "Pre-committed living: making your financial choices before the moment arrives", "Daniel 1:8; Psalm 119:112"),
  ...dayEntry(38, "Planned Generosity", "How to make your giving last beyond impulse", "Proverbs 21:5; Luke 14:28"),
  ...dayEntry(39, "Your Sphere of Influence", "Impact starts closer than you think — your family, your friend group, your school", "1 Timothy 5:8; Galatians 6:10"),
  ...dayEntry(40, "The Generous Body", "What happens when a whole community decides to live this way", "Acts 2:42–47; 2 Corinthians 8:1–5"),
  ...dayEntry(41, "Good News to the Poor", "Generosity and mission belong together — always have", "Luke 4:18–19; John 13:35"),
  ...dayEntry(42, "The Mark You Leave", "What will your life have meant? Impact today, tomorrow, and eternally", "1 Timothy 6:18–19; Hebrews 11:24–26"),

  spacer(),

  // ===== SECTION MAPPING TABLE =====
  h1("Section Overview: Adult Edition → Student Edition"),
  new Paragraph({
    spacing: { before: 80, after: 160 },
    children: [new TextRun({
      text: "Each section of the Student Edition maps directly to the adult God Owns It All curriculum while using language, illustrations, and scenarios grounded in student life.",
      font: "Arial", size: 20, italics: true
    })]
  }),

  ...[
    ["I — Ownership", "Days 1–7", "Who owns it? → Translates stewardship from mortgages/assets to first jobs, cars, college money"],
    ["II — Stewardship", "Days 8–14", "Faithfulness & Principles → Credit cards, student loans, first budget, spending choices"],
    ["III — Confidence", "Days 15–21", "Will I be OK? → College costs, future uncertainty, financial anxiety as a student"],
    ["IV — Contentment", "Days 22–28", "How much is enough? → Social media comparison, lifestyle inflation, FOMO"],
    ["V — Generosity", "Days 29–35", "Giving changes everything → Tithing first paycheck, time/talent, peer generosity culture"],
    ["VI — Impact", "Days 36–42", "Eternal perspective → Legacy thinking for 18–25 year olds, kingdom ROI"],
  ].map(([section, days, notes]) => new Paragraph({
    spacing: { before: 60, after: 60 },
    children: [
      new TextRun({ text: `${section}  `, font: "Arial", size: 20, bold: true, color: BLUE }),
      new TextRun({ text: `(${days})  `, font: "Arial", size: 20, bold: true, color: ACCENT }),
      new TextRun({ text: notes, font: "Arial", size: 20 }),
    ]
  })),

  spacer(),

  // ===== DEVOTIONAL FORMAT =====
  h1("Daily Devotional Format (Per Day)"),
  sectionIntro("Each of the 40+ days follows this consistent, student-tested structure. Total reading time: 4–6 minutes."),

  ...[
    ["📖 Scripture", "(NIV) — Short passage, 1–4 verses. Selected for accessibility and direct connection to the day's theme."],
    ["🎯 The Hook", "One opening sentence or question pulled from real student experience — a moment they'll recognize immediately."],
    ["💡 The Big Idea", "2–3 paragraphs max. Conversational, non-preachy tone. Connects the biblical truth directly to life at school, work, home, or on a phone screen."],
    ["🔑 Key Thought", "One sentence. Memorable. Transferable to a friend. Built to stick."],
    ["❓ Reflect", "One question. Not a quiz — a genuine invitation to sit with the truth."],
    ["🙏 Pray", "3–5 sentence guided prayer. Honest, conversational, not churchy."],
  ].map(([label, desc]) => [
    new Paragraph({
      spacing: { before: 120, after: 20 },
      children: [new TextRun({ text: label, font: "Arial", size: 20, bold: true })]
    }),
    new Paragraph({
      spacing: { before: 0, after: 60 },
      indent: { left: 360 },
      children: [new TextRun({ text: desc, font: "Arial", size: 20 })]
    }),
  ]).flat(),

  spacer(),

  // ===== TONE GUIDE =====
  h1("Tone & Voice Guide"),
  ...[
    ["✅ Write like this:", "Direct, warm, real. Like a trusted mentor talking, not lecturing. Short sentences. Honest about struggle. Assumes students are capable of depth."],
    ["❌ Not like this:", "Preachy. Guilt-heavy. 'Christianese' jargon without explanation. Condescending about age or experience. Overly simplified."],
    ["Student life examples to draw from:", "First job / minimum wage. Paying for gas. School lunch budget. Wanting the new phone. Comparing clothes. Venmoing friends. College application costs. Parents' financial stress. Giving at church for the first time."],
    ["Avoid adult examples like:", "Mortgages. 401(k) balances. Salary negotiations. Marriage finances (unless briefly referenced as future context)."],
  ].map(([label, desc]) => [
    new Paragraph({
      spacing: { before: 120, after: 20 },
      children: [new TextRun({ text: label, font: "Arial", size: 20, bold: true, color: BLUE })]
    }),
    new Paragraph({
      spacing: { before: 0, after: 60 },
      indent: { left: 360 },
      children: [new TextRun({ text: desc, font: "Arial", size: 20 })]
    }),
  ]).flat(),

];

const doc = new Document({
  styles: {
    default: { document: { run: { font: "Arial", size: 22 } } },
    paragraphStyles: [
      { id: "Heading1", name: "Heading 1", basedOn: "Normal", next: "Normal", quickFormat: true,
        run: { size: 36, bold: true, font: "Arial", color: BLUE },
        paragraph: { spacing: { before: 400, after: 120 }, outlineLevel: 0 } },
      { id: "Heading2", name: "Heading 2", basedOn: "Normal", next: "Normal", quickFormat: true,
        run: { size: 26, bold: true, font: "Arial", color: ACCENT },
        paragraph: { spacing: { before: 280, after: 80 }, outlineLevel: 1 } },
    ]
  },
  sections: [{
    properties: {
      page: {
        size: { width: 12240, height: 15840 },
        margin: { top: 1440, right: 1440, bottom: 1440, left: 1440 }
      }
    },
    children
  }]
});

Packer.toBuffer(doc).then(buf => {
  fs.writeFileSync('/mnt/user-data/outputs/GOIA_Student_Edition_40Day_Outline.docx', buf);
  console.log('Done!');
});
