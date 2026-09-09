const {
  Document, Packer, Paragraph, TextRun, HeadingLevel,
  AlignmentType, BorderStyle, ShadingType, WidthType,
  Table, TableRow, TableCell, PageBreak
} = require('docx');
const fs = require('fs');

// ─── Helpers ──────────────────────────────────────────────────────────────────

function spacer(pts = 120) {
  return new Paragraph({ children: [new TextRun('')], spacing: { before: pts, after: 0 } });
}

function body(text, opts = {}) {
  return new Paragraph({
    children: [new TextRun({ text, font: 'Georgia', size: 24, ...opts })],
    spacing: { before: 120, after: 120, line: 336 },
    alignment: AlignmentType.LEFT,
  });
}

function bodyBold(text) {
  return new Paragraph({
    children: [new TextRun({ text, font: 'Georgia', size: 24, bold: true })],
    spacing: { before: 120, after: 120, line: 336 },
  });
}

// Mixed paragraph: some bold, some normal
function bodyMixed(runs) {
  return new Paragraph({
    children: runs.map(r =>
      new TextRun({ font: 'Georgia', size: 24, ...r })
    ),
    spacing: { before: 120, after: 120, line: 336 },
  });
}

function sectionLabel(text) {
  return new Paragraph({
    children: [new TextRun({ text, font: 'Arial', size: 20, bold: true, color: '2E6DA4', allCaps: true })],
    spacing: { before: 280, after: 80 },
  });
}

function verseBlock(ref, text) {
  return new Paragraph({
    children: [
      new TextRun({ text: `${ref} — `, font: 'Georgia', size: 22, bold: true, italics: true }),
      new TextRun({ text, font: 'Georgia', size: 22, italics: true }),
    ],
    spacing: { before: 80, after: 80, line: 310 },
    indent: { left: 720, right: 720 },
    border: {
      left: { style: BorderStyle.SINGLE, size: 12, color: '2E6DA4', space: 8 }
    }
  });
}

function pullQuote(text) {
  return new Paragraph({
    children: [new TextRun({ text, font: 'Georgia', size: 26, bold: true, italics: true, color: '2E6DA4' })],
    spacing: { before: 200, after: 200, line: 340 },
    indent: { left: 360, right: 360 },
    alignment: AlignmentType.CENTER,
  });
}

function affirmation(text) {
  return new Paragraph({
    children: [new TextRun({ text, font: 'Georgia', size: 24, bold: true, italics: true })],
    spacing: { before: 160, after: 160, line: 336 },
    indent: { left: 360 },
    border: {
      left: { style: BorderStyle.SINGLE, size: 18, color: '8B6914', space: 10 }
    }
  });
}

function exerciseQuestion(num, label, prompt) {
  return new Paragraph({
    children: [
      new TextRun({ text: `${num}. ${label}: `, font: 'Georgia', size: 24, bold: true }),
      new TextRun({ text: prompt, font: 'Georgia', size: 24, italics: true, color: '555555' }),
    ],
    spacing: { before: 120, after: 40, line: 310 },
    indent: { left: 360 },
  });
}

function bullet(text) {
  return new Paragraph({
    children: [new TextRun({ text, font: 'Georgia', size: 24 })],
    spacing: { before: 60, after: 60, line: 310 },
    indent: { left: 720, hanging: 360 },
    numbering: undefined,
    bullet: { level: 0 },
  });
}

function optionBlock(letter, title, text) {
  return new Paragraph({
    children: [
      new TextRun({ text: `Option ${letter} — ${title}: `, font: 'Georgia', size: 24, bold: true }),
      new TextRun({ text, font: 'Georgia', size: 24 }),
    ],
    spacing: { before: 100, after: 100, line: 310 },
    indent: { left: 360 },
  });
}

function reflectQ(text) {
  return new Paragraph({
    children: [new TextRun({ text, font: 'Georgia', size: 24, italics: true })],
    spacing: { before: 100, after: 40, line: 310 },
    indent: { left: 360 },
  });
}

// ─── Document ─────────────────────────────────────────────────────────────────

const doc = new Document({
  styles: {
    default: {
      document: { run: { font: 'Georgia', size: 24 } }
    },
    paragraphStyles: [
      {
        id: 'Heading1', name: 'Heading 1', basedOn: 'Normal', next: 'Normal', quickFormat: true,
        run: { size: 40, bold: true, font: 'Arial', color: '1A3D6B' },
        paragraph: { spacing: { before: 0, after: 120 }, outlineLevel: 0 }
      },
      {
        id: 'Heading2', name: 'Heading 2', basedOn: 'Normal', next: 'Normal', quickFormat: true,
        run: { size: 28, bold: true, font: 'Arial', color: '2E6DA4' },
        paragraph: { spacing: { before: 240, after: 80 }, outlineLevel: 1 }
      },
    ]
  },
  numbering: {
    config: [
      {
        reference: 'bullets',
        levels: [{ level: 0, format: 'bullet', text: '\u2022', alignment: AlignmentType.LEFT,
          style: { paragraph: { indent: { left: 720, hanging: 360 } } } }]
      },
      {
        reference: 'numbers',
        levels: [{ level: 0, format: 'decimal', text: '%1.', alignment: AlignmentType.LEFT,
          style: { paragraph: { indent: { left: 720, hanging: 360 } } } }]
      }
    ]
  },
  sections: [{
    properties: {
      page: {
        size: { width: 12240, height: 15840 },
        margin: { top: 1440, right: 1296, bottom: 1440, left: 1296 }
      }
    },
    children: [

      // ── Header: Week / Day label ──────────────────────────────────────────
      new Paragraph({
        children: [new TextRun({ text: 'WEEK ONE — THE OWNERSHIP QUESTION', font: 'Arial', size: 18, allCaps: true, color: '888888' })],
        spacing: { before: 0, after: 40 },
      }),
      new Paragraph({
        children: [],
        border: { bottom: { style: BorderStyle.SINGLE, size: 4, color: 'CCCCCC', space: 1 } },
        spacing: { before: 0, after: 200 },
      }),

      // ── Day title ─────────────────────────────────────────────────────────
      new Paragraph({
        heading: HeadingLevel.HEADING_1,
        children: [new TextRun({ text: 'Day 1 — The Foundation', font: 'Arial', size: 40, bold: true, color: '1A3D6B' })],
        spacing: { before: 0, after: 40 },
      }),
      new Paragraph({
        children: [new TextRun({ text: 'God Owns It All — And That Changes the Story', font: 'Arial', size: 28, bold: true, color: '2E6DA4' })],
        spacing: { before: 0, after: 80 },
      }),

      // ── Theme statement ───────────────────────────────────────────────────
      pullQuote('GOD\'S OWNERSHIP IS THE PLACE YOUR HEART CAN FINALLY REST.'),

      // ── Daily Inspiration placeholder ─────────────────────────────────────
      new Paragraph({
        children: [
          new TextRun({ text: 'Daily Inspiration', font: 'Arial', size: 20, bold: true }),
          new TextRun({ text: '  |  Watch today\'s short video: ', font: 'Arial', size: 20, color: '555555' }),
          new TextRun({ text: 'https://placeholder.url/goia/day-1', font: 'Arial', size: 20, color: '2E6DA4' }),
        ],
        spacing: { before: 80, after: 200 },
      }),

      // ── Scripture ─────────────────────────────────────────────────────────
      sectionLabel('Today\'s Verses'),
      verseBlock('Romans 11:36 (NIV)', '"For from him and through him and for him are all things. To him be the glory forever! Amen."'),
      spacer(80),
      verseBlock('James 1:17 (ESV)', '"Every good gift and every perfect gift is from above… with whom there is no variation or shadow due to change."'),
      spacer(200),

      // ══════════════════════════════════════════════════════════════════════
      // NARRATIVE
      // ══════════════════════════════════════════════════════════════════════

      // OPENING STORY
      sectionLabel('Opening Story'),
      body('Ron Blue tells a story that has stayed with him for decades. A seminary professor retired after a life spent teaching theology — a man who never earned more than $10,000 a year. When he and his wife moved into an assisted living facility, his daughter worried he might run out of money and asked Ron to go check on him. Ron sat down and asked the man to walk him through his finances. What he discovered was unexpected: through decades of careful saving and one wise investment, the professor had accumulated more than $1.5 million.'),
      body('But that wasn\'t the part that stayed with Ron. It was what the professor said when asked what he\'d learned from his life. He paused and then told one small story. Early in his ministry, when he and his wife were young and in seminary, they had an infant daughter and almost nothing in the bank. Every Friday the milkman came — $2 for the week\'s milk. One particular Friday they had no money at all. The milkman was coming up the back walk just as someone knocked at the front door. The professor went to the front, and a neighbor from upstairs handed him $2. She said God had put it on her heart at church Wednesday night, and she\'d been slow to act on it.'),
      body('He smiled at the memory. Two dollars. Two separate people. Perfect timing. "God will always provide," he told Ron. "That\'s what I learned."'),
      body('That man had spent his whole life practicing a posture that most people only talk about. He didn\'t act like the owner. He acted like a steward — careful with what was entrusted, open-handed with what wasn\'t his to clutch.'),
      spacer(160),

      // SECTION 1: When Ownership Changes, Everything Settles
      new Paragraph({
        heading: HeadingLevel.HEADING_2,
        children: [new TextRun({ text: 'When Ownership Changes, Everything Settles', font: 'Arial', size: 28, bold: true, color: '2E6DA4' })],
      }),
      body('There is a question that sits underneath many questions: Who is responsible for holding all of this together? When life feels heavy, the heart reaches for control. Not always in obvious ways. Sometimes it looks like overthinking. Sometimes it looks like clenching — tightening plans, tightening timelines, tightening expectations — fueled by a quiet assumption: If I don\'t manage everything, everything will fall apart.'),
      body('If you\'ve ever felt that assumption rise up, you\'re not abnormal. You\'re human. Most people don\'t realize how often they\'re working to create peace through control. And to be fair, there are seasons when responsibility feels genuinely heavy — when the margin is thin, when decisions matter, when the future feels uncertain. But the deeper issue is rarely the number of decisions. It\'s the story you believe about who has to carry the outcome.'),
      body('There\'s a kind of responsibility God gives, and there\'s a kind of weight we take on ourselves. God-given responsibility produces diligence and humility — it keeps you present, faithful, and grounded. Self-assigned weight produces a different kind of strain: a quiet fear that even good days might not be enough. In one posture, you can breathe. In the other, you\'re always one thing away from falling behind.'),
      body('The foundation of this journey is a different starting point. God is not merely involved. God is the source, the sustainer, and the goal. Romans 11:36 says it with stunning plainness: "For from him and through him and for him are all things." That is ownership language. It means your life is not self-originated, self-maintained, or self-directed. The story is not finally about what you can produce, protect, or control. It is about what God has begun, what God is carrying, and what God intends.'),
      body('That changes the story because so much of what feels like stress comes from taking a role you were never assigned. You were never asked to be the source. You were never asked to be the final provider or to guarantee outcomes. You were invited to trust the One who sees the whole landscape — and then take wise steps as a steward.'),
      spacer(120),

      // SECTION 2: The Giver Behind the Gifts
      new Paragraph({
        heading: HeadingLevel.HEADING_2,
        children: [new TextRun({ text: 'The Giver Behind the Gifts', font: 'Arial', size: 28, bold: true, color: '2E6DA4' })],
      }),
      body('James 1:17 adds tenderness to the truth of Romans 11: "Every good gift and every perfect gift is from above." The foundation is not only that God is sovereign. It is that God is generous. If what you have is received rather than manufactured, the posture of the heart begins to change. Gratitude can replace entitlement. Trust begins to confront fear. Open hands become possible — not because you are careless, but because you are no longer trying to act as the source.'),
      body('Some people hear "God owns it all" and feel threatened. They imagine God\'s ownership as distance — a corporate claim. But James reminds us that God\'s ownership is personal. He is a Father who gives, not a ruler who withholds. He is steady, not shifting. He does not change like shifting shadows. Your life is not anchored to something unstable; it is anchored to Someone faithful.'),
      affirmation('Here is the re-ordering that has to happen at the beginning: God is the source. My life belongs to Him. Trust replaces control. Write that down if it helps. Return to it when the grip tightens.'),
      body('When you trust the gifts more than the Giver, you\'ll always feel like you might lose your foundation. But when you trust the Giver, you can hold the gifts with open hands. Open hands don\'t mean you don\'t care. They mean you\'ve stopped treating your resources as a savior.'),
      spacer(120),

      // SECTION 3: Control in Disguise
      new Paragraph({
        heading: HeadingLevel.HEADING_2,
        children: [new TextRun({ text: 'Control in Disguise', font: 'Arial', size: 28, bold: true, color: '2E6DA4' })],
      }),
      body('Here is a hard but freeing thought: much of what feels like responsibility is actually self-reliance dressed up as wisdom. It can feel noble. It can feel mature. But when it pushes God to the margins and places the weight of "all things" on your shoulders, it will eventually crush your peace. Freedom doesn\'t come from finally becoming strong enough to manage everything. It comes from finally stopping the pretense that you were meant to.'),
      body('Control can feel like love — "I\'m doing this for my family." It can feel like maturity — "I\'m being responsible." It can feel like preparedness — "I\'m staying ahead." But control often becomes a substitute for trust. Not because you don\'t believe, but because self-reliance has been practiced for so long it feels normal.'),
      body('The seminary professor\'s $2 story is small. That\'s the point. God didn\'t show up with a dramatic windfall. He sent a neighbor with $2 on a Friday afternoon. And a man who had learned not to act like the owner recognized it for what it was: provision, perfectly timed, from the One who already knew the need.'),
      body('That is what faithful stewardship looks like from the inside. Not dramatic. Not always visible. Just a steady refusal to grip what isn\'t yours to hold.'),
      spacer(120),

      // SECTION 4: Your Role Is Faithfulness
      new Paragraph({
        heading: HeadingLevel.HEADING_2,
        children: [new TextRun({ text: 'Your Role Is Faithfulness', font: 'Arial', size: 28, bold: true, color: '2E6DA4' })],
      }),
      body('You may still have real decisions to make. You may still need wisdom and need to take responsibility seriously. But you don\'t have to do it with clenched hands and a clenched heart. You can do it with steadiness — because the Owner is steady.'),
      body('Faithful people don\'t always know what happens next. They don\'t always have a guarantee. They learn to take the next right step in the right spirit — without demanding the illusion of certainty. That is what changes the story. Your role is not to carry everything. Your role is to be faithful with what\'s in your hands today.'),
      affirmation('Faithful stewardship doesn\'t mean perfect outcomes. It means the next right step, in the right spirit, with open hands.'),
      body('Everything else we\'ll explore together — stewardship, contentment, generosity, wisdom, long-term direction — depends on what you believe about ownership. Skip the foundation and you\'ll build your life on control. Control always cracks. Start with ownership, and you can build on trust. Trust holds.'),
      body('Quietly, simply, return to the foundation today. Let ownership settle the argument in your soul. Let trust become your first step.'),
      spacer(200),

      // ══════════════════════════════════════════════════════════════════════
      // REFLECT
      // ══════════════════════════════════════════════════════════════════════
      new Paragraph({
        children: [],
        border: { top: { style: BorderStyle.SINGLE, size: 4, color: '2E6DA4', space: 1 } },
        spacing: { before: 200, after: 0 },
      }),
      sectionLabel('Think About It'),
      reflectQ('Who has been the "source" in your life story so far — in the way you actually think and decide, not just the way you talk about it?'),
      spacer(40),
      reflectQ('What would change if you approached your finances and your future as a steward — someone managing what belongs to another — rather than as the owner?'),
      spacer(40),
      reflectQ('Where have you seen something that looked like the seminary professor\'s $2 story in your own life — a small, precise provision that could only have come from God?'),
      spacer(200),

      // ══════════════════════════════════════════════════════════════════════
      // EXERCISES
      // ══════════════════════════════════════════════════════════════════════
      sectionLabel('Exercises'),

      new Paragraph({
        heading: HeadingLevel.HEADING_2,
        children: [new TextRun({ text: 'Exercise 1: The Ownership Inventory', font: 'Arial', size: 26, bold: true, color: '2E6DA4' })],
        spacing: { before: 200, after: 60 },
      }),
      body('Take 10 minutes and write honest, short answers. The goal is clarity, not guilt.'),
      exerciseQuestion('1', 'The area of life I\'m most likely to grip tightly', '(money / plans / family / future / reputation / comfort)'),
      exerciseQuestion('2', 'The story I tell myself to justify that grip', '(responsibility / wisdom / "no one else will" / fear)'),
      exerciseQuestion('3', 'The deeper desire underneath it', '(stability / control / certainty / approval / safety)'),
      exerciseQuestion('4', 'One stewardship step I can practice this week', '(one sentence)'),
      spacer(120),

      new Paragraph({
        heading: HeadingLevel.HEADING_2,
        children: [new TextRun({ text: 'Exercise 2: The "From / Through / For" Reset', font: 'Arial', size: 26, bold: true, color: '2E6DA4' })],
        spacing: { before: 200, after: 60 },
      }),
      body('Read Romans 11:36 slowly — "from him… through him… for him…" — then answer:'),
      new Paragraph({
        children: [new TextRun({ text: '\u2022  Where am I acting like the "from" (the source) right now?', font: 'Georgia', size: 24 })],
        spacing: { before: 60, after: 40, line: 310 },
        indent: { left: 720, hanging: 360 },
      }),
      new Paragraph({
        children: [new TextRun({ text: '\u2022  Where am I acting like the "through" (the sustainer) right now?', font: 'Georgia', size: 24 })],
        spacing: { before: 60, after: 40, line: 310 },
        indent: { left: 720, hanging: 360 },
      }),
      new Paragraph({
        children: [new TextRun({ text: '\u2022  What would it look like to re-aim one area "for Him" today?', font: 'Georgia', size: 24 })],
        spacing: { before: 60, after: 40, line: 310 },
        indent: { left: 720, hanging: 360 },
      }),
      spacer(200),

      // ── Declaration ───────────────────────────────────────────────────────
      sectionLabel('Write This Declaration'),
      body('Write this out by hand. Then read it aloud slowly.'),
      new Paragraph({
        children: [new TextRun({
          text: '"God, You are the Owner. Everything I have and everything I am belongs to You. Teach me to steward what You\'ve entrusted to me with open hands and a steady heart."',
          font: 'Georgia', size: 24, bold: true, italics: true,
        })],
        spacing: { before: 120, after: 200, line: 336 },
        indent: { left: 360, right: 360 },
        shading: { fill: 'EEF4FA', type: ShadingType.CLEAR },
        border: {
          top: { style: BorderStyle.SINGLE, size: 6, color: '2E6DA4', space: 8 },
          bottom: { style: BorderStyle.SINGLE, size: 6, color: '2E6DA4', space: 8 },
          left: { style: BorderStyle.SINGLE, size: 6, color: '2E6DA4', space: 8 },
          right: { style: BorderStyle.SINGLE, size: 6, color: '2E6DA4', space: 8 },
        }
      }),

      // ══════════════════════════════════════════════════════════════════════
      // NEXT STEPS
      // ══════════════════════════════════════════════════════════════════════
      sectionLabel('Next Steps'),
      body('Pick one. Keep it practical. Do it today.'),
      spacer(60),

      optionBlock('A', 'The Quiet Transfer',
        'Choose one area you\'ve been gripping. Pray one sentence: "Father, this belongs to You. Teach me to steward it." Say it and mean it — that\'s the whole point.'),
      spacer(60),
      optionBlock('B', 'The First Decision Pause',
        'Before your next money decision — big or small — stop for ten seconds and say, "God, You\'re the Owner. Lead me." Then proceed with steadiness.'),
      spacer(60),
      optionBlock('C', 'The Stewardship Conversation',
        'Start one calm conversation with your spouse or a trusted friend: "Here\'s the area I feel most responsible for. Will you pray with me about trusting God here?"'),
      spacer(200),

      // ── Closing Prayer ────────────────────────────────────────────────────
      sectionLabel('Closing Prayer'),
      new Paragraph({
        children: [new TextRun({
          text: 'Father, You are the source of every good gift, and You do not change. Forgive me for the ways I\'ve tried to carry life like it all depends on me. Today I return to the foundation: everything is from You, through You, and for You. Teach me to live with open hands — not passive, but trusting; not careless, but faithful. Give me wisdom for my next step and peace that doesn\'t rely on perfect outcomes. You are the Owner, and I am Yours. Amen.',
          font: 'Georgia', size: 24, italics: true,
        })],
        spacing: { before: 120, after: 120, line: 336 },
        indent: { left: 360, right: 360 },
      }),

      // ── EDITORIAL NOTE FOR PRODUCTION ────────────────────────────────────
      spacer(240),
      new Paragraph({
        children: [],
        border: { top: { style: BorderStyle.DASHED, size: 4, color: 'AAAAAA', space: 1 } },
        spacing: { before: 80, after: 0 },
      }),
      new Paragraph({
        children: [new TextRun({ text: 'EDITORIAL NOTES — FOR PRODUCTION TEAM', font: 'Arial', size: 18, bold: true, allCaps: true, color: 'CC4400' })],
        spacing: { before: 100, after: 60 },
      }),
      new Paragraph({
        children: [new TextRun({ text: 'Story placeholder: ', font: 'Arial', size: 20, bold: true, color: '555555' }),
          new TextRun({ text: 'The seminary professor / milkman story in the opening is drawn from Ron\'s Session 1 transcript (RBI filmed). It is used here as a real story. Please confirm with client whether this is cleared for use in this format, or whether a brief "as Ron tells it" attribution is preferred.', font: 'Arial', size: 20, color: '555555' })],
        spacing: { before: 40, after: 80, line: 310 },
      }),
      new Paragraph({
        children: [new TextRun({ text: 'Story request for Days 2–7: ', font: 'Arial', size: 20, bold: true, color: '555555' }),
          new TextRun({ text: 'See story request sheet below. Each day benefits from one opening anecdote (3–4 sentences) drawn from a real client or real life. Please pull stories matching the themes listed.', font: 'Arial', size: 20, color: '555555' })],
        spacing: { before: 40, after: 80, line: 310 },
      }),
    ]
  }]
});

Packer.toBuffer(doc).then(buffer => {
  fs.writeFileSync('/mnt/user-data/outputs/GOIA_Day1_Revised.docx', buffer);
  console.log('Done');
});
