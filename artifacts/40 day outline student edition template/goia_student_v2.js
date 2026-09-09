const {
  Document, Packer, Paragraph, TextRun, HeadingLevel,
  AlignmentType, BorderStyle, LevelFormat, PageNumber,
  ShadingType, WidthType, TableRow, TableCell, Table
} = require('docx');
const fs = require('fs');

const BLUE     = "1A3F6F";
const TEAL     = "1E7A8C";
const ORANGE   = "C0590A";
const GRAY     = "555555";
const LIGHTBG  = "EEF4FB";

// ── helpers ──────────────────────────────────────────────────────────

function cover() {
  return [
    new Paragraph({
      alignment: AlignmentType.CENTER,
      spacing: { before: 600, after: 60 },
      children: [new TextRun({ text: "GOD OWNS IT ALL", font: "Arial", size: 64, bold: true, color: BLUE })]
    }),
    new Paragraph({
      alignment: AlignmentType.CENTER,
      spacing: { before: 0, after: 60 },
      children: [new TextRun({ text: "Student Edition", font: "Arial", size: 36, bold: false, color: TEAL })]
    }),
    new Paragraph({
      alignment: AlignmentType.CENTER,
      spacing: { before: 0, after: 40 },
      children: [new TextRun({ text: "────────────────────────", font: "Arial", size: 20, color: "AAAAAA" })]
    }),
    new Paragraph({
      alignment: AlignmentType.CENTER,
      spacing: { before: 0, after: 600 },
      children: [new TextRun({ text: "40 Days to Change How You Think About Money", font: "Arial", size: 24, italics: true, color: GRAY })]
    }),
  ];
}

function rule() {
  return new Paragraph({
    spacing: { before: 40, after: 40 },
    border: { bottom: { style: BorderStyle.SINGLE, size: 4, color: "CCCCCC", space: 4 } },
    children: [new TextRun("")]
  });
}

function sp(before = 80, after = 80) {
  return new Paragraph({ spacing: { before, after }, children: [new TextRun("")] });
}

function sectionHeader(num, title, emoji, subtitle) {
  return [
    sp(300, 0),
    new Paragraph({
      spacing: { before: 0, after: 0 },
      children: [
        new TextRun({ text: `${emoji}  `, font: "Arial", size: 28 }),
        new TextRun({ text: `Week ${num}: `, font: "Arial", size: 28, bold: true, color: TEAL }),
        new TextRun({ text: title, font: "Arial", size: 28, bold: true, color: BLUE }),
      ]
    }),
    new Paragraph({
      spacing: { before: 60, after: 40 },
      border: { bottom: { style: BorderStyle.SINGLE, size: 6, color: TEAL, space: 6 } },
      children: [new TextRun({ text: subtitle, font: "Arial", size: 20, italics: true, color: GRAY })]
    }),
    sp(40, 0),
  ];
}

function day(n, title, hook, scripture) {
  return [
    new Paragraph({
      spacing: { before: 160, after: 0 },
      children: [
        new TextRun({ text: `Day ${n}  `, font: "Arial", size: 13, bold: true, color: TEAL, allCaps: true }),
        new TextRun({ text: title, font: "Arial", size: 22, bold: true, color: BLUE }),
      ]
    }),
    new Paragraph({
      spacing: { before: 20, after: 8 },
      indent: { left: 200 },
      children: [new TextRun({ text: hook, font: "Arial", size: 19, italics: true, color: GRAY })]
    }),
    new Paragraph({
      spacing: { before: 0, after: 60 },
      indent: { left: 200 },
      children: [new TextRun({ text: `📖 ${scripture}`, font: "Arial", size: 17, color: "888888" })]
    }),
  ];
}

function introBlurb(text) {
  return new Paragraph({
    spacing: { before: 80, after: 120 },
    shading: { fill: LIGHTBG, type: ShadingType.CLEAR },
    children: [new TextRun({ text, font: "Arial", size: 19, color: "333333" })]
  });
}

function bodyText(text) {
  return new Paragraph({
    spacing: { before: 60, after: 80 },
    children: [new TextRun({ text, font: "Arial", size: 20, color: "222222" })]
  });
}

function sectionQ(big) {
  return new Paragraph({
    alignment: AlignmentType.CENTER,
    spacing: { before: 80, after: 80 },
    children: [new TextRun({ text: `"${big}"`, font: "Arial", size: 26, bold: true, italics: true, color: ORANGE })]
  });
}

// ── document ─────────────────────────────────────────────────────────

const children = [

  ...cover(),

  // ── INTRO ─────────────────────────────────────────────────
  new Paragraph({
    spacing: { before: 0, after: 40 },
    children: [new TextRun({ text: "Hey — before you start", font: "Arial", size: 28, bold: true, color: BLUE })]
  }),
  rule(),
  sp(60, 0),

  bodyText("You've probably heard adults talk about money your whole life. Save more. Spend less. Don't go into debt. And maybe some of that has actually sunk in — or maybe it's just background noise by now."),
  bodyText("These 40 days aren't another lecture about money. They're about one question that Jesus asked way more than people realize:"),
  sectionQ("Who does this actually belong to?"),
  bodyText("Because here's the thing — if God actually owns everything, that doesn't just change how you handle a paycheck. It changes how you handle your whole life."),
  bodyText("Five minutes a day. That's all this takes. Read it in bed, on the bus, before practice, whenever. There's a scripture, a real-life scenario you'll recognize, one big idea, and a short prayer. No homework. No pop quiz."),
  bodyText("Just 40 days that might change how you think — about money, about God, and about yourself."),

  sp(40, 0),
  new Paragraph({
    spacing: { before: 60, after: 120 },
    children: [new TextRun({ text: "What each day looks like:", font: "Arial", size: 20, bold: true, color: BLUE })]
  }),
  ...[
    ["📖  Scripture", "A short passage — read it slow, maybe twice."],
    ["💥  The Scenario", "A real situation you've probably been in."],
    ["💡  The Big Idea", "The one thing to take away that day."],
    ["🔑  Key Thought", "One sentence. Say it out loud. Send it to a friend."],
    ["🙏  Reflect + Pray", "One honest question. One short prayer."],
  ].map(([label, desc]) => new Paragraph({
    spacing: { before: 40, after: 40 },
    indent: { left: 360 },
    children: [
      new TextRun({ text: label + "  —  ", font: "Arial", size: 19, bold: true }),
      new TextRun({ text: desc, font: "Arial", size: 19, color: GRAY }),
    ]
  })),

  sp(60, 0),
  rule(),

  // ══════════════════════════════════════════════════════════
  // WEEK 1
  // ══════════════════════════════════════════════════════════
  ...sectionHeader(1, "Who's Really in Charge?", "🏠", "Days 1–7  ·  The Ownership Question"),
  sectionQ("What does it actually mean if God owns it all?"),
  introBlurb("Before anything else in these 40 days, we have to answer one question. Not a trick question — but one that will change literally every other decision you make. Who owns your stuff? Your money, your time, your future? Most of us say \"God\" — but live like the answer is \"me.\" Week 1 is about closing that gap."),

  ...day(1, "It All Belongs to God — So What?",
    "You just got paid. It's YOUR money. You earned it. ...Or did you?",
    "Romans 11:36 · James 1:17"),

  ...day(2, "Riding Shotgun",
    "What if being in control isn't actually the goal?",
    "Proverbs 3:5–6 · 1 Peter 5:7"),

  ...day(3, "\"Mine\" Is the Most Dangerous Word",
    "You say it about your phone, your car, your money. Here's why that's a problem.",
    "Deuteronomy 8:17–18 · Luke 12:15"),

  ...day(4, "Owned — But Not Like That",
    "God owns everything. But that doesn't make him a landlord. It makes him a Father.",
    "1 Corinthians 6:19–20 · Isaiah 43:1"),

  ...day(5, "Your Money Reveals Your Trust",
    "Forget what you say you believe. Look at where your money goes.",
    "Matthew 6:21, 24 · Proverbs 3:5–6"),

  ...day(6, "Money Stress Is Usually a Control Problem",
    "Why do you get so anxious about money? This day might explain it.",
    "Matthew 6:33 · Philippians 4:6–7"),

  ...day(7, "Thinking Like a Manager, Not an Owner",
    "The difference between owning something and taking care of something is everything.",
    "Colossians 1:16–17 · Psalm 50:10–12"),

  sp(80, 0),
  rule(),

  // ══════════════════════════════════════════════════════════
  // WEEK 2
  // ══════════════════════════════════════════════════════════
  ...sectionHeader(2, "Handling What You Have", "📋", "Days 8–14  ·  The Stewardship Question"),
  sectionQ("How do I actually be faithful with what I've got right now?"),
  introBlurb("Stewardship sounds like a church word. But it just means taking care of something that belongs to someone else. Whether you have $20 or $2,000, you're already practicing stewardship — the question is whether you're doing it well. Week 2 is super practical. First jobs. First budgets. The real cost of \"buy now, pay later.\""),

  ...day(8, "God Doesn't Grade on Results",
    "You didn't get a raise. The business failed. Did you still pass?",
    "1 Corinthians 4:2 · Matthew 25:21"),

  ...day(9, "How You Handle $20 Is the Point",
    "Every athlete knows: how you practice is how you play. Same with money.",
    "Luke 16:10–12 · Zechariah 4:10"),

  ...day(10, "Every Purchase Is a Statement",
    "Where your money goes tells the world — and God — what you actually care about.",
    "Matthew 6:19–21 · Proverbs 4:26"),

  ...day(11, "What Does Your Phone's Payment App Say About You?",
    "Forget a diary. Your spending history is already telling your story.",
    "Luke 12:34 · Mark 10:21–22"),

  ...day(12, "Debt Borrows From Your Future Self",
    "\"I'll pay it off later\" is one of the most expensive phrases you can say.",
    "Proverbs 22:7 · Romans 13:8"),

  ...day(13, "Four Questions Before You Borrow",
    "There IS a biblical filter for going into debt. Here it is.",
    "Luke 14:28–30 · James 4:13–16"),

  ...day(14, "Honesty in the Small Things",
    "Claiming the wrong amount on taxes. Under-reporting your hours. Why the small stuff matters more than you think.",
    "Matthew 22:17–21 · Romans 13:6–7"),

  sp(80, 0),
  rule(),

  // ══════════════════════════════════════════════════════════
  // WEEK 3
  // ══════════════════════════════════════════════════════════
  ...sectionHeader(3, "Will I Be Okay?", "😰", "Days 15–21  ·  The Confidence Question"),
  sectionQ("What if God's provision actually IS enough?"),
  introBlurb("College. Jobs. The economy. Your parents' money stress bleeding into yours. Lots of students carry serious financial anxiety, even if they don't call it that. Week 3 is about where real confidence actually comes from — and spoiler: it's not from having a lot of money."),

  ...day(15, "The Real Question Behind the Worry",
    "\"Will I be okay?\" is about money on the surface. What is it actually about?",
    "Psalm 23:1 · Isaiah 41:10"),

  ...day(16, "The Strategy Jesus Actually Gave You",
    "Not a budget worksheet. Not a side hustle. Something way more foundational.",
    "Matthew 6:31–33 · Philippians 4:19"),

  ...day(17, "Why Breathing Room Changes Everything",
    "Margin isn't just a financial idea. It's a spiritual one.",
    "Proverbs 21:20 · Psalm 37:16"),

  ...day(18, "Four Habits to Start Right Now",
    "You don't need a six-figure salary to start these. You just need to start.",
    "Proverbs 13:11 · Proverbs 21:5"),

  ...day(19, "Money and Your Relationships",
    "Why your money habits are already affecting the people around you — even if you don't see it.",
    "Amos 3:3 · Ephesians 4:25"),

  ...day(20, "You Can't Buy Your Way to Peace",
    "Why the new thing never actually makes you feel more secure.",
    "Proverbs 22:7 · Luke 12:15"),

  ...day(21, "One Next Step",
    "You don't have to figure it all out today. What's the one thing you can do?",
    "Philippians 4:6–9 · Proverbs 3:5–6"),

  sp(80, 0),
  rule(),

  // ══════════════════════════════════════════════════════════
  // WEEK 4
  // ══════════════════════════════════════════════════════════
  ...sectionHeader(4, "How Much Is Enough?", "📱", "Days 22–28  ·  The Contentment Question"),
  sectionQ("What if you decided what \"enough\" looks like before Instagram did?"),
  introBlurb("This might be the most countercultural week in the whole 40 days. You live in a world designed — literally designed by algorithms — to make you feel like you don't have enough. Week 4 is about learning contentment before your lifestyle gets away from you. The students who figure this out early? They are rare. And free."),

  ...day(22, "Contentment Isn't a Feeling — It's a Skill",
    "Paul said he LEARNED to be content. Which means it took time. Which means you can learn it too.",
    "Philippians 4:11–13 · Hebrews 13:5"),

  ...day(23, "More Choices, More Restless",
    "Why the generation with the most options is also one of the most anxious.",
    "1 Timothy 6:6–10 · Ecclesiastes 5:10"),

  ...day(24, "Draw Your Finish Line Before You Start the Race",
    "What does \"enough\" look like for you? Define it now, before your lifestyle drifts.",
    "Proverbs 30:8–9 · Luke 12:16–21"),

  ...day(25, "Simple Doesn't Mean Small",
    "Choosing less stuff isn't a failure. It might actually be the freest you've ever been.",
    "Matthew 6:24 · Galatians 5:1"),

  ...day(26, "Gratitude Is a Weapon",
    "One of the fastest ways to break the comparison spiral? This. Right here.",
    "1 Thessalonians 5:18 · Psalm 103:2–5"),

  ...day(27, "The Scroll That Steals Your Peace",
    "Comparison is a thief. And your phone is its best tool.",
    "2 Corinthians 10:12 · John 21:21–22"),

  ...day(28, "Content Even When Things Are Hard",
    "What does contentment look like when your account is low and nothing is going right?",
    "Habakkuk 3:17–19 · Psalm 16:5–6"),

  sp(80, 0),
  rule(),

  // ══════════════════════════════════════════════════════════
  // WEEK 5
  // ══════════════════════════════════════════════════════════
  ...sectionHeader(5, "Give It Away?", "🎁", "Days 29–35  ·  The Generosity Question"),
  sectionQ("What if generosity isn't something you do LATER — it's something you start NOW?"),
  introBlurb("Most students think: I'll give when I have more. But here's what nobody tells you — the habit of generosity is WAY harder to build later than it is to start now. And the side effect of giving? It literally breaks money's power over you. Week 5 might flip everything you thought about giving."),

  ...day(29, "God Went First",
    "Before you ever gave anything, God gave everything. That changes the whole conversation.",
    "John 3:16 · Romans 8:32"),

  ...day(30, "Why Giving Is the One Thing That Breaks the Grip",
    "You can't serve two masters. But you CAN choose which one loses.",
    "Matthew 6:21 · Luke 12:34"),

  ...day(31, "No One Should Guilt You Into Giving",
    "God isn't interested in your money if it comes with resentment. Here's the kind of giving he actually loves.",
    "2 Corinthians 9:6–8 · Exodus 35:21"),

  ...day(32, "Consistent Beats Emotional Every Time",
    "The high of giving $100 once versus giving $10 every week. Which one actually forms you?",
    "1 Corinthians 16:2 · Proverbs 3