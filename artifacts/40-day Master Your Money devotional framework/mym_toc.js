const { Document, Packer, Paragraph, TextRun, AlignmentType, ShadingType } = require('docx');
const fs = require('fs');

const days = [
  // Movement 1
  { movement: "MOVEMENT ONE: WHO REALLY OWNS THIS?  |  Days 1–7" },
  { day: 1,  title: "The Question Underneath Every Question", sub: "Why your financial anxiety may be a spiritual symptom" },
  { day: 2,  title: "You Possess Much, But You Own Nothing", sub: "The liberating difference between a steward and an owner" },
  { day: 3,  title: "Your Checkbook Knows the Truth", sub: "What your spending reveals about what you actually believe" },
  { day: 4,  title: "The Money That Sits on the Throne", sub: "How money becomes a false master — and how to dethrone it" },
  { day: 5,  title: "Every Spending Decision Is a Spiritual Decision", sub: "There is nothing more spiritual about a tithe check than a grocery run" },
  { day: 6,  title: "The Tool That Lost Its Power", sub: "When money becomes a servant instead of a master, everything changes" },
  { day: 7,  title: "Signing the Deed", sub: "The ownership transfer that changes the rest of your financial life" },

  // Movement 2
  { movement: "MOVEMENT TWO: WHERE ARE YOU, AND WILL YOU BE OKAY?  |  Days 8–14" },
  { day: 8,  title: "Will I Ever Have Enough?", sub: "The question underneath the spreadsheet that only one answer can settle" },
  { day: 9,  title: "Taking Stock Without Shame", sub: "How to look honestly at where you are — and why that honesty is a gift" },
  { day: 10, title: "What Is Actually Coming In, and Where Is It Going?", sub: "The cash flow conversation most people have been avoiding" },
  { day: 11, title: "The Five Stages — and Honest About Which One You're In", sub: "Struggling, Surviving, Stable, Secure, or Surplus: where are you really?" },
  { day: 12, title: "The Comparison Trap", sub: "Why neighbor-watching is one of the most expensive habits you have" },
  { day: 13, title: "How Much Is Enough?", sub: "The question that money can never answer but faith can" },
  { day: 14, title: "When Fear Rules, Peace Is Impossible", sub: "How settled ownership quiets the anxiety that money can't fix" },

  // Movement 3
  { movement: "MOVEMENT THREE: THE WISDOM THAT NEVER CHANGES  |  Days 15–21" },
  { day: 15, title: "Principles That Outlast Every Market", sub: "Why God's financial wisdom works when economic predictions don't" },
  { day: 16, title: "Spend Less Than You Earn — Always", sub: "The simplest financial principle is also the most violated" },
  { day: 17, title: "We Are in a Growth Process", sub: "Faithfulness is the goal — not a particular income or net worth" },
  { day: 18, title: "The Amount Is Not the Point", sub: "Why a retired pastor who never earned more than $8,000 a year mastered money" },
  { day: 19, title: "Avoid Debt Like the Plague", sub: "Why borrowing always costs more than you think — spiritually and financially" },
  { day: 20, title: "Faith Requires Action", sub: "The last biblical principle is also the one most people skip" },
  { day: 21, title: "Wisdom Is Always Transcendent, Transferable, Transformative, and Timeless", sub: "Why these principles work for anyone, anywhere, at any income level" },

  // Movement 4
  { movement: "MOVEMENT FOUR: THE PLAN THAT SETS YOU FREE  |  Days 22–28" },
  { day: 22, title: "Goals That Come from Prayer, Not Fear", sub: "How to set financial goals that God actually authored" },
  { day: 23, title: "The Four Barriers That Steal Your Future", sub: "Why most people never set goals — and what to do about it" },
  { day: 24, title: "Budget: The Word That Feels Like a Cage But Isn't", sub: "Why a spending plan is one of the most liberating things you can build" },
  { day: 25, title: "The Most Common Mistakes — and Why Smart People Make Them", sub: "A consumptive lifestyle, no budget, and driving to the poor house" },
  { day: 26, title: "Margin Is Not a Luxury — It Is Obedience", sub: "Why breathing room in your finances is a spiritual priority" },
  { day: 27, title: "The Sequential Strategy — One Step at a Time", sub: "Why the order of your financial priorities matters as much as the amount" },
  { day: 28, title: "Planning Is Not the Opposite of Faith", sub: "Why preparing for the future honors God rather than doubting Him" },

  // Movement 5
  { movement: "MOVEMENT FIVE: THE FREEDOM FOUND IN GIVING  |  Days 29–35" },
  { day: 29, title: "Generosity Is What Free People Do", sub: "You don't graduate into giving — you grow into it" },
  { day: 30, title: "Where Your Treasure Goes, Your Heart Follows", sub: "You don't wait to feel generous — you choose generosity and your heart catches up" },
  { day: 31, title: "Giving Breaks the Power of Money", sub: "Why the most financially anxious people are often the least generous" },
  { day: 32, title: "Decide Before You Give", sub: "Why generosity planned in advance is generosity that actually happens" },
  { day: 33, title: "Generosity Is for Every Stage — Not Just Surplus", sub: "The widow's offering was not a special exception — it was the standard" },
  { day: 34, title: "Giving Aligns Today with Eternity", sub: "The only financial action with eternal consequences" },
  { day: 35, title: "Open Hands, Quiet Strength", sub: "What contentment feels like when generosity is finally part of who you are" },

  // Movement 6
  { movement: "MOVEMENT SIX: FAITHFUL TO THE END — AND BEYOND  |  Days 36–40" },
  { day: 36, title: "You Never See a Hearse Pulling a U-Haul", sub: "What you cannot take with you — and what you can send ahead" },
  { day: 37, title: "Both Spouses Need to Hold the Whole Picture", sub: "What happens when one person carries all the financial knowledge" },
  { day: 38, title: "The Inheritance That Money Cannot Carry", sub: "What you pass on that outlasts any dollar figure in a will" },
  { day: 39, title: "Giving While You Can Still See It", sub: "Why Ron Blue believes most charitable giving should happen before death" },
  { day: 40, title: "Well Done, Good and Faithful Servant", sub: "The commendation is available to every steward who chooses faithfulness over fear" },
];

const children = [];

// Page header
children.push(new Paragraph({
  children: [new TextRun({ text: "MASTER YOUR MONEY", font: "Georgia", size: 28, bold: true, color: "1A3A5C" })],
  alignment: AlignmentType.CENTER,
  spacing: { before: 0, after: 40 }
}));
children.push(new Paragraph({
  children: [new TextRun({ text: "A 40-Day Devotional Journey  —  Contents at a Glance", font: "Georgia", size: 20, italics: true, color: "B8860B" })],
  alignment: AlignmentType.CENTER,
  spacing: { before: 0, after: 120 }
}));

// Thin rule
children.push(new Paragraph({
  children: [new TextRun({ text: "", font: "Arial", size: 2 })],
  spacing: { before: 0, after: 100 },
  border: { bottom: { style: "single", size: 4, color: "B8860B", space: 1 } }
}));

days.forEach(item => {
  if (item.movement) {
    // Movement header row
    children.push(new Paragraph({
      children: [new TextRun({ text: item.movement, font: "Georgia", size: 16, bold: true, color: "FFFFFF" })],
      spacing: { before: 100, after: 0 },
      shading: { fill: "1A3A5C", type: ShadingType.CLEAR }
    }));
  } else {
    // Day row
    children.push(new Paragraph({
      children: [
        new TextRun({ text: `${item.day}  `, font: "Georgia", size: 17, bold: true, color: "B8860B" }),
        new TextRun({ text: item.title, font: "Georgia", size: 17, bold: true, color: "111111" }),
        new TextRun({ text: "  —  ", font: "Georgia", size: 16, color: "999999" }),
        new TextRun({ text: item.sub, font: "Georgia", size: 16, italics: true, color: "555555" }),
      ],
      spacing: { before: 32, after: 32 },
      indent: { left: 200 }
    }));
  }
});

// Footer rule
children.push(new Paragraph({
  children: [new TextRun({ text: "", size: 2 })],
  spacing: { before: 100, after: 40 },
  border: { top: { style: "single", size: 4, color: "B8860B", space: 1 } }
}));
children.push(new Paragraph({
  children: [new TextRun({ text: "Based on the teaching of Ron Blue and the Ron Blue Institute  ·  Master Your Money curriculum", font: "Georgia", size: 15, italics: true, color: "888888" })],
  alignment: AlignmentType.CENTER,
  spacing: { before: 0, after: 0 }
}));

const doc = new Document({
  styles: { default: { document: { run: { font: "Georgia", size: 17 } } } },
  sections: [{
    properties: {
      page: {
        size: { width: 12240, height: 15840 },
        margin: { top: 720, right: 900, bottom: 720, left: 900 }
      }
    },
    children
  }]
});

Packer.toBuffer(doc).then(buf => {
  fs.writeFileSync("/mnt/user-data/outputs/MYM_40Day_Contents.docx", buf);
  console.log("Done");
});
