const {
  Document, Packer, Paragraph, TextRun, HeadingLevel,
  AlignmentType, BorderStyle, WidthType, PageBreak, LevelFormat
} = require('docx');
const fs = require('fs');

// ─── HELPERS ──────────────────────────────────────────────────────────────────

function pageBreak() {
  return new Paragraph({ children: [new PageBreak()] });
}

function rule() {
  return new Paragraph({
    spacing: { before: 160, after: 160 },
    border: { bottom: { style: BorderStyle.SINGLE, size: 4, color: 'CCCCCC', space: 1 } },
    children: []
  });
}

function dayHeader(number, title, subtitle, verse) {
  return [
    new Paragraph({
      spacing: { before: 0, after: 60 },
      children: [new TextRun({ text: `Day ${number} \u2014 ${title}`, bold: true, size: 36, font: 'Georgia', color: '1F4E79' })]
    }),
    new Paragraph({
      spacing: { before: 0, after: 60 },
      children: [new TextRun({ text: subtitle, italics: true, size: 24, font: 'Arial', color: '555555' })]
    }),
    new Paragraph({
      spacing: { before: 0, after: 200 },
      children: [new TextRun({ text: verse.toUpperCase(), bold: true, size: 20, font: 'Arial', color: '888888', characterSpacing: 40 })]
    }),
  ];
}

function sectionLabel(text) {
  return new Paragraph({
    spacing: { before: 280, after: 80 },
    children: [new TextRun({ text: text.toUpperCase(), bold: true, size: 18, font: 'Arial', color: '1F4E79', characterSpacing: 60 })]
  });
}

function scripture(ref, text) {
  return [
    new Paragraph({
      spacing: { before: 80, after: 20 },
      children: [new TextRun({ text: ref, bold: true, size: 21, font: 'Arial' })]
    }),
    new Paragraph({
      spacing: { before: 0, after: 120 },
      indent: { left: 480 },
      children: [new TextRun({ text: `\u201C${text}\u201D`, italics: true, size: 21, font: 'Georgia' })]
    }),
  ];
}

function subhead(text) {
  return new Paragraph({
    spacing: { before: 220, after: 60 },
    children: [new TextRun({ text, bold: true, size: 24, font: 'Arial' })]
  });
}

function body(text) {
  return new Paragraph({
    spacing: { before: 60, after: 100 },
    children: [new TextRun({ text, size: 22, font: 'Georgia' })]
  });
}

function pullquote(text) {
  return new Paragraph({
    spacing: { before: 160, after: 160 },
    indent: { left: 560, right: 560 },
    border: { left: { style: BorderStyle.SINGLE, size: 12, color: '1F4E79', space: 10 } },
    children: [new TextRun({ text, italics: true, size: 23, font: 'Georgia', color: '1F4E79' })]
  });
}

function bold_body(label, rest) {
  return new Paragraph({
    spacing: { before: 60, after: 100 },
    children: [
      new TextRun({ text: label, bold: true, size: 22, font: 'Georgia' }),
      new TextRun({ text: rest, size: 22, font: 'Georgia' })
    ]
  });
}

function bullet(text) {
  return new Paragraph({
    spacing: { before: 40, after: 40 },
    numbering: { reference: 'bullets', level: 0 },
    children: [new TextRun({ text, size: 22, font: 'Georgia' })]
  });
}

function numbered(text) {
  return new Paragraph({
    spacing: { before: 40, after: 40 },
    numbering: { reference: 'numbers', level: 0 },
    children: [new TextRun({ text, size: 22, font: 'Georgia' })]
  });
}

function declaration(text) {
  return new Paragraph({
    spacing: { before: 120, after: 120 },
    indent: { left: 480, right: 480 },
    shading: { fill: 'EBF3FB', type: 'clear' },
    children: [new TextRun({ text: `\u201C${text}\u201D`, italics: true, size: 22, font: 'Georgia', color: '0C3A68' })]
  });
}

function optionHead(letter, title) {
  return new Paragraph({
    spacing: { before: 140, after: 40 },
    children: [
      new TextRun({ text: `Option ${letter} \u2014 `, bold: true, size: 22, font: 'Arial' }),
      new TextRun({ text: title, bold: true, italics: true, size: 22, font: 'Arial', color: '1F4E79' })
    ]
  });
}

function sp(before = 60) {
  return new Paragraph({ spacing: { before }, children: [] });
}

// ─── DAY 1 ────────────────────────────────────────────────────────────────────

const day1 = [
  ...dayHeader(1, 'The Question Underneath the Question', 'God Owns It All \u2014 And That Changes the Story', 'God\u2019s ownership is the place your heart can finally rest.'),

  sectionLabel("Today's Verses"),
  ...scripture('Psalm 24:1 (NIV)', 'The earth is the Lord\u2019s, and everything in it, the world, and all who live in it.'),
  ...scripture('Romans 11:36 (NIV)', 'For from him and through him and for him are all things. To him be the glory forever! Amen.'),

  sectionLabel('Opening'),

  body('Ron Blue was on a plane to Grand Rapids for a meeting with his editor when he glanced at the young woman in the seat beside him. She was well-dressed, maybe twenty years old, and leafing through one of those in-flight shopping catalogs \u2014 the kind that sells designer luggage and golf equipment and things no one actually needs at 35,000 feet. What stayed with Ron wasn\u2019t the catalog. It was her face. She looked miserable. Not just bored. Genuinely unhappy, the way someone looks when they\u2019ve been reaching for something for a long time and keep coming up just short.'),
  body('He thought about her for days afterward. And what he eventually concluded was this: whatever she was looking for in that catalog, she already had the answer to her question. She just didn\u2019t know yet that the answer wasn\u2019t in the catalog.'),
  body('That\u2019s a good place to start. Because most of us \u2014 at some point, in some way \u2014 have been that person. Reaching. Scrolling. Calculating. Wondering if the next raise, the next purchase, the paid-off card, the funded retirement account will finally produce the feeling we\u2019re after.'),
  body('We don\u2019t usually say it out loud. But the question is always running in the background: \u201CWill I be okay? Will I ever have enough? And if I do have enough \u2014 will it stay that way?\u201D'),
  body('Those are real questions. They deserve a real answer. And this forty-day journey starts by arguing that you\u2019ve been asking the right question in the wrong direction.'),

  subhead('The Three Wrong Questions'),

  body('Ron spent twenty-five years as a financial advisor. He sat with thousands of families \u2014 struggling ones, comfortable ones, wealthy ones \u2014 and he noticed that underneath every financial conversation, no matter the income level, the same three questions kept surfacing:'),
  bullet('Will I ever have enough?'),
  bullet('Will it continue to be enough?'),
  bullet('\u2026and how much is enough, anyway?'),
  body('These aren\u2019t wrong things to wonder. But Ron came to believe they were the wrong questions to lead with. Not because they\u2019re unimportant, but because they put you at the center of an equation you were never designed to solve. If you begin by asking \u201Cwill I have enough,\u201D you\u2019ve already assumed that you\u2019re the one responsible for making sure the answer is yes. And that assumption is where the weight comes from.'),
  body('He also noticed that the question beneath those questions was almost always one of three things: What will it take to feel successful? What will it take to feel significant? What will it take to feel secure? And the culture\u2019s answer is always the same: more. More income, more options, more cushion, more status, more things.'),
  body('Here is what forty years of financial advising taught him: more doesn\u2019t answer those questions. It moves them.'),

  subhead('The Three Right Questions'),

  body('Scripture offers three different questions \u2014 ones that actually lead somewhere:'),
  bullet('Who owns it?'),
  bullet('How much is enough (as a stewardship question, not a scarcity question)?'),
  bullet('Is the next steward chosen and prepared?'),
  body('That first question \u2014 \u201Cwho owns it?\u201D \u2014 changes everything downstream. If you answer it honestly, the weight shifts. Not because your circumstances change, but because your role changes. You stop being the owner responsible for guaranteeing outcomes, and you become a steward responsible for faithfulness. Those are very different jobs.'),
  body('Psalm 24:1 doesn\u2019t negotiate: \u201CThe earth is the Lord\u2019s, and everything in it.\u201D Romans 11:36 takes it further: everything is from him, through him, and for him. That\u2019s not just a theology sentence. It\u2019s a description of reality. And it means that your life \u2014 your income, your savings, your home, your plans, your family \u2014 none of it is self-originated or self-sustained. It was entrusted to you. You didn\u2019t create it. You\u2019re managing it for Someone who was here before it existed.'),

  pullquote('If God owns it, then you are not alone in carrying it. And if you are not alone in carrying it, the question changes from \u201CWill I be okay?\u201D to \u201CWhat does faithful look like today?\u201D'),

  subhead('What This Does to the Story'),

  body('Ron sometimes said that when he testified before a congressional subcommittee in the early 1990s, the senator asked him what he would tell the American family about their finances. Ron gave four principles. The senator picked up his pencil, wrote them down, and said, \u201CIt seems like those would work at any income level.\u201D Ron said, \u201CYou\u2019re right, senator \u2014 including the United States government.\u201D'),
  body('But those principles only work if they\u2019re built on the right foundation. And the foundation isn\u2019t discipline. It isn\u2019t willpower. It isn\u2019t a better budget. The foundation is a settled answer to the ownership question. Because the way you handle money always follows what you believe about money. Behavior follows belief. That\u2019s not motivational language \u2014 it\u2019s how formation actually works.'),
  body('If you believe your money is yours \u2014 earned by your effort, secured by your intelligence, protected by your planning \u2014 then every financial pressure becomes a personal verdict. Every unexpected expense feels like a threat. Every financial decision carries the weight of your future. And the result is exactly what Ron watched thousands of people carry into his office: not financial ignorance, but financial fear dressed up as responsibility.'),
  body('If you believe your money is God\u2019s \u2014 entrusted to you, accountable to him, managed on his behalf \u2014 then the weight redistributes. You still work hard. You still plan thoughtfully. You still take your responsibilities seriously. But you stop acting like everything is riding on you. Because it isn\u2019t. The Owner is steady. And a steady Owner means you can be faithful without being frantic.'),
  body('That\u2019s the re-ordering that Week 1 is after. Not a financial plan. A different starting place.'),

  sectionLabel('Think About It'),
  body('When something financial goes wrong \u2014 an unexpected bill, a income drop, an uncertain season \u2014 what is your first internal move? What do you reach for?'),
  body('The world\u2019s three questions (Will I have enough? Will it last? How much is enough?) assume you are the one responsible for the answers. What would it change in your daily life if you genuinely believed you weren\u2019t?'),
  body('Ron said that when he let God\u2019s ownership become his foundation, he found that it changed not just his finances but his contentment, his confidence, and his communication with his wife. Which of those three do you most need to change?'),

  sectionLabel('Exercises'),
  subhead('The Three Questions Inventory (10 minutes)'),
  body('Write short, honest answers.'),
  numbered('The financial question I carry most often is: (one sentence)'),
  numbered('Underneath it, what I\u2019m really asking is: (successful / significant / secure \u2014 circle the closest)'),
  numbered('The way I currently try to answer that question is: (more income / more savings / more control / more options / something else)'),
  numbered('If God is the Owner, what changes about who has to answer that question?'),

  subhead('The \u201Cfrom Him\u2019 Reset (2 minutes)'),
  body('Read Romans 11:36 slowly: \u201CFor from him and through him and for him are all things.\u201D Then answer:'),
  bullet('Where am I acting like the \u201Cfrom\u201D \u2014 like I\u2019m the source?'),
  bullet('Where am I living like it\u2019s \u201Cfor me\u201D rather than \u201Cfor him\u201D?'),
  bullet('What is one area I can return to God today?'),

  sectionLabel('Write This Declaration'),
  declaration('God, you are the Owner. Everything I have and everything I am belongs to you. I am not the source. I am not responsible for guaranteeing outcomes. Teach me to steward what you\u2019ve entrusted to me with open hands and a steady heart.'),

  sectionLabel('Next Steps'),
  body('Pick one. Keep it simple. Do it today.'),
  optionHead('A', 'The Quiet Transfer'),
  body('Choose one area you\u2019ve been carrying like an owner. Pray one sentence: \u201CFather, this belongs to you. Teach me to steward it.\u201D Don\u2019t perform it. Mean it.'),
  optionHead('B', 'The First Decision Pause'),
  body('Before your next money decision today \u2014 big or small \u2014 pause for ten seconds and say: \u201CGod, you\u2019re the Owner. Lead me.\u201D Then proceed with steadiness.'),
  optionHead('C', 'The Stewardship Conversation'),
  body('Tell one trusted person: \u201CI\u2019m thinking about what it would mean to actually live like God owns what I have. Will you ask me next week what changed?\u201D Accountability works when it\u2019s specific.'),

  sectionLabel('Closing Prayer'),
  body('Father, you are the source of every good gift, and you do not change. Forgive me for the ways I\u2019ve lived like everything depends on me. Today I return to the foundation: everything is from you, through you, and for you. Teach me to live with open hands \u2014 not passive, but trusting; not careless, but faithful. Give me wisdom for my next step and peace that doesn\u2019t require perfect outcomes. You are the Owner, and I am yours. Amen.'),
];

// ─── DAY 2 ────────────────────────────────────────────────────────────────────

const day2 = [
  pageBreak(),
  ...dayHeader(2, 'Rights Belong to the Owner', 'Surrendering Control Is Not Losing \u2014 It\u2019s Coming Home', 'God doesn\u2019t ask you to carry everything. He asks you to trust him first.'),

  sectionLabel("Today's Verses"),
  ...scripture('Proverbs 3:5\u20136 (NIV)', 'Trust in the Lord with all your heart and lean not on your own understanding; in all your ways submit to him, and he will make your paths straight.'),
  ...scripture('1 Peter 5:7 (CSB)', 'Casting all your cares on him, because he cares about you.'),

  sectionLabel('Opening'),

  body('Picture yourself at your boss\u2019s dinner table. He\u2019s invited a group of colleagues, and you\u2019re determined to make a good impression. The meal is ready. Your boss steps out of the kitchen and moves toward the head of the table. Before he can sit down, you walk past him and take the seat yourself.'),
  body('Nobody does that. Not because of a rule, but because the arrangement is obvious. In your boss\u2019s home, at his table, the head chair is his. You wait to be seated because he\u2019s the host.'),
  body('That\u2019s the picture the concept of the \u201Csecond chair\u201D is drawing. In every life, there is a first chair \u2014 the seat of ultimate authority. And the question isn\u2019t whether a first chair exists. It\u2019s who sits in it. If God sits there, you can live with steadiness. If you sit there, you may look capable on the outside while your soul quietly exhausts itself trying to hold everything together.'),

  subhead('The Difference Between Responsibility and Control'),

  body('This is where most people get stuck, because control and responsibility can look identical from the outside. Both involve hard work. Both involve planning. Both involve caring deeply about outcomes. The difference is what\u2019s driving them.'),
  body('Responsibility says: \u201CI\u2019ll do what\u2019s mine to do.\u201D'),
  body('Control says: \u201CI need to make sure nothing goes wrong.\u201D'),
  body('Responsibility works within the limits of being human. Control tries to live beyond those limits. And the difference between them, over time, is enormous. Responsibility produces diligence and a clear conscience. Control produces anxiety, irritability, and the quiet belief that if you ever stop holding everything together, everything will fall apart.'),
  body('Ron Blue watched this play out for decades in his financial planning practice. He worked with CEOs, surgeons, pastors, single parents, retired couples. And across all of them he noticed the same thing: the ones who lived with the most peace weren\u2019t the ones who had the most money. They were the ones who had settled the ownership question. They knew who the first chair belonged to \u2014 and they weren\u2019t trying to sit in it.'),

  subhead('What Stewardship Actually Means'),

  body('The word \u201Csteward\u201D sounds formal and old-fashioned, but its meaning is straightforward. A steward manages something that belongs to someone else. Ron spent many years managing investment accounts for clients. The assets he managed didn\u2019t belong to him or his firm. He had no right to them. His job was to find out what the clients wanted \u2014 their goals, their values, their priorities \u2014 and then faithfully manage those resources toward those ends. At some point, the client would want those assets back. Ron\u2019s term of stewardship would be over.'),
  body('That\u2019s the role. You literally possess much, but you own nothing. God benefits you by sharing his property with you. You have a responsibility to him to use it in a way that honors him. And at some point, he may take back whatever he chooses, whenever he chooses. That\u2019s not a threat. It\u2019s the nature of stewardship. Owners have rights. Stewards have responsibilities.'),
  body('Once this lands, something surprising happens: it\u2019s a relief. Because stewards are responsible for faithfulness, not for omniscience. You\u2019re responsible for obedience, not for outcomes. You\u2019re responsible for taking the next wise step, not for guaranteeing where every step leads. That\u2019s a lighter load. It\u2019s the load you were actually designed to carry.'),

  pullquote('Surrender isn\u2019t stepping into emptiness. It\u2019s stepping into the care of a steady Father. The seat you\u2019re being asked to give up was never designed for you in the first place.'),

  subhead('Why Surrender Feels Like Loss'),

  body('Here\u2019s the honest truth about why people resist this: surrender feels like losing something. Losing control. Losing options. Losing the ability to protect yourself and the people you love. And many times, the grip isn\u2019t rooted in selfishness. It\u2019s rooted in love. It\u2019s rooted in a genuine desire to be faithful, to provide, to not let people down.'),
  body('But even good desires become heavy burdens when they turn into demands. When \u201CI want to provide for my family\u201D becomes \u201CI am the reason my family is okay,\u201D the weight of that belief will quietly crush your peace \u2014 not because you don\u2019t love them, but because you\u2019ve taken on a role that belongs to God.'),
  body('Proverbs 3:5\u20136 cuts through this. \u201CTrust in the Lord with all your heart and lean not on your own understanding.\u201D Notice: it\u2019s not \u201Ctrust with part of your heart\u201D or \u201Ctrust in the areas where you don\u2019t have expertise.\u201D All your heart. In all your ways. The invitation is complete because partial trust produces divided living. When part of you trusts God and part of you trusts your own ability to guarantee outcomes, you feel pulled. You feel like generosity is both right and threatening. You feel like obedience is both clear and risky. That\u2019s what a divided heart produces.'),
  body('And then the promise: \u201Che will make your paths straight.\u201D That\u2019s not a guarantee that the path will be easy. It\u2019s a guarantee that you won\u2019t navigate it alone.'),

  subhead('Returning to the Second Chair'),

  body('You will drift. Everyone does. The goal of the next forty days isn\u2019t to never sit in the first chair again. The goal is to recognize when you\u2019ve done it and return quickly. Over time, that return becomes faster. Eventually it becomes reflexive. And when that happens \u2014 when your default is stewardship rather than control \u2014 you begin to notice something Ron described as the result of a life lived this way: contentment, confidence, clarity of communication, and consistency of behavior. Not as achievements. As fruit.'),
  body('That\u2019s the promise. Not that life becomes easy, but that you stop spending your energy fighting a battle that was never yours to win.'),

  sectionLabel('Think About It'),
  body('Where in your financial life do you currently feel the most pressure to \u201Cmake sure nothing goes wrong\u201D? What would responsibility \u2014 rather than control \u2014 look like there?'),
  body('When you imagine releasing control in one specific area to God, what emotion comes first: relief, fear, or something else? What does that emotion tell you about what you believe about God\u2019s trustworthiness?'),
  body('What\u2019s the difference between the kind of planning that reflects stewardship and the kind that reflects control? Can you think of an example from your own life of each?'),

  sectionLabel('Exercises'),
  subhead('The Second Chair Inventory (10 minutes)'),
  body('Write short, honest answers.'),
  numbered('The area where I\u2019m most likely sitting in the first chair right now is: (finances / career / family outcomes / the future / my reputation)'),
  numbered('The reason it\u2019s hard to give that chair up is: (I don\u2019t want to fail / I don\u2019t want to disappoint someone / I don\u2019t trust the outcome / I don\u2019t trust God with this specifically)'),
  numbered('One faithful step that would look like stewardship rather than control in that area is: (one concrete sentence)'),

  subhead('The Surrender Sentence (2 minutes)'),
  body('Complete these two lines and say them out loud:'),
  bullet('\u201CGod, you can have the first chair in __________.'),
  bullet('\u201CMy next faithful step as a steward is __________.'),

  sectionLabel('Write This Declaration'),
  declaration('God, you are first. I release the need to control outcomes. Teach me to be faithful with what you\u2019ve entrusted to me, and to trust you with what I cannot control. I take the second chair. Lead me from there.'),

  sectionLabel('Next Steps'),
  body('Pick one. Keep it doable. Do it today.'),
  optionHead('A', 'The First-Chair Pause'),
  body('Before your next financial decision, pause for ten seconds and say: \u201CGod, you\u2019re first. Lead me.\u201D Then decide with steadiness, not urgency.'),
  optionHead('B', 'The Control Release'),
  body('Write down one outcome you\u2019ve been trying to manage. Pray one sentence: \u201CFather, this belongs to you.\u201D Then identify one practical step that\u2019s actually yours to take \u2014 and take it without needing to control everything past that step.'),
  optionHead('C', 'The Honest Conversation'),
  body('Tell a trusted person one area where you\u2019ve been sitting in the first chair. Ask them to check in with you next week and ask: \u201CAre you letting God lead that, or are you still trying to run it yourself?\u201D'),

  sectionLabel('Closing Prayer'),
  body('Father, you are steady and you do not change like shifting shadows. Forgive me for the ways I\u2019ve tried to sit in the first chair \u2014 not out of rebellion, but out of fear that if I don\u2019t hold everything together, nothing will hold. Today I take the second chair. Teach me steady obedience. Give me wisdom for what is mine to do, and peace to trust you with what is not. Lead my decisions, shape my heart, and help me live as your steward with open hands. Amen.'),
];

// ─── DAY 3 ────────────────────────────────────────────────────────────────────

const day3 = [
  pageBreak(),
  ...dayHeader(3, '\u201CMine\u201D Is Not a Word \u2014 It\u2019s an Identity', 'Why Ownership Drift Is So Hard to Catch', 'Identity drifts when I forget where my strength came from.'),

  sectionLabel("Today's Verses"),
  ...scripture('Deuteronomy 8:17\u201318 (NIV)', 'You may say to yourself, \u201CMy power and the strength of my hands have produced this wealth for me.\u201D But remember the Lord your God, for it is he who gives you the ability to produce wealth.'),
  ...scripture('Luke 12:15 (ESV)', 'Take care, and be on your guard against all covetousness, for one\u2019s life does not consist in the abundance of his possessions.'),

  sectionLabel('Opening'),

  body('Ron Blue was on a trip to Africa with Cru Ministries in the mid-1970s. He\u2019d spent three years on Wall Street and seven years building a successful CPA practice. He thought he understood materialism. He thought it was an American problem \u2014 something born of abundance and advertising and keeping up with neighbors who drove nicer cars.'),
  body('Then he was standing with a pastor in Kenya, looking down at the man\u2019s mud hut. Ron asked him what he thought was the greatest barrier to the spread of the gospel in that part of the world. He expected the pastor to say transportation, or money, or tribalism. Instead the pastor said: materialism.'),
  body('Ron was confused. \u201CWhat do you mean by that?\u201D'),
  body('The pastor said: \u201CIf a man has a mud hut, he wants a stone hut. If he has a thatch roof, he wants a metal roof. If he\u2019s got one acre, he wants two acres. If he\u2019s got one cow, he wants two cows.\u201D'),
  body('Ron said later that he learned something right there that stayed with him for the rest of his life: materialism isn\u2019t unique to America. It isn\u2019t unique to wealth. It\u2019s unique to the human heart. And the word that lives at the center of it is very small. It\u2019s the word \u201Cmine.\u201D'),

  subhead('How \u201CMine\u201D Becomes \u201CMe\u201D'),

  body('The word \u201Cmine\u201D starts out as a simple description. My schedule. My work. My home. My savings. Used that way, it\u2019s neutral \u2014 shorthand for what I\u2019m responsible for managing. But Deuteronomy 8 identifies a slow, almost invisible shift that happens when things start going well: we begin to credit ourselves as the source.'),
  body('Not all at once. Not out loud. Just gradually. We start to believe our stability is the product of our own strength, our own discipline, our own hustle, our own good decisions. And when that happens, \u201Cmine\u201D stops being a description and starts being a claim. It becomes the place we go to feel safe. The thing we defend when it\u2019s threatened. The proof that we\u2019re okay.'),
  body('Deuteronomy calls this forgetting. And it\u2019s worth noticing that the Bible treats forgetting as a spiritual danger on the same level as outright rebellion. Because forgetting doesn\u2019t usually look like sin. It looks like success. It looks like confidence. It looks like \u201CI\u2019ve got this.\u201D'),
  body('The dangerous moment isn\u2019t when you consciously decide to take ownership from God. The dangerous moment is when you stop noticing that you have.'),

  subhead('The Identity Attachment'),

  body('Here\u2019s where the word \u201Cmine\u201D gets genuinely costly: when something is \u201Cmine,\u201D any threat to it feels like a threat to me. The financial pressure isn\u2019t just a financial pressure \u2014 it\u2019s a verdict on my worth. The setback isn\u2019t just a setback \u2014 it\u2019s evidence that I\u2019m failing. The comparison with someone who has more isn\u2019t just uncomfortable \u2014 it\u2019s destabilizing, because their \u201Cmore\u201D implies my \u201Cless,\u201D and \u201Cless\u201D has come to mean something about me.'),
  body('This is what Jesus is interrupting in Luke 12:15. He doesn\u2019t say possessions are evil. He says life doesn\u2019t consist in them. He\u2019s not shaming anyone for having things. He\u2019s protecting people from letting things define them. Because once your possessions become part of your identity, you can\u2019t hold them freely. You grip them. And a gripping hand is not a giving hand, a planning hand, or a peaceful hand. It\u2019s a defending hand.'),

  pullquote('The test isn\u2019t what you have. It\u2019s what you would lose yourself over if it disappeared. Where your identity is attached, there your anxiety will follow.'),

  subhead('The Path Back'),

  body('Deuteronomy 8 doesn\u2019t just warn. It offers a path: \u201CBut remember the Lord your God.\u201D Remembering is a spiritual practice. Not nostalgia \u2014 re-centering. Telling yourself the truth again before your heart starts telling you a different story. Remembering is how you return your footing when your identity starts leaning on the wrong thing.'),
  body('When you remember God, you stop acting like your resources are proof of your worth. You stop acting like your outcomes are your identity. You stop treating your savings account as the place you go to feel safe. Not because you become careless, but because you return to what\u2019s actually true: your value is anchored in God, not in what you\u2019ve accumulated.'),
  body('That\u2019s deeper than financial advice. It\u2019s the only way to hold money without being held by it.'),

  sectionLabel('Think About It'),
  body('When something in your financial life feels threatened \u2014 an income drop, an unexpected expense, a comparison that stings \u2014 what does it trigger in you? What does that reaction reveal about where your identity might be attached?'),
  body('Think about something you have that you would genuinely struggle to release if God asked you to: a lifestyle level, a savings milestone, a career status, a financial cushion. What does that tell you about where \u201Cmine\u201D has quietly become \u201Cme\u201D?'),
  body('Deuteronomy says the antidote to ownership drift is remembering. What is one specific thing you need to remember about God\u2019s faithfulness today that would loosen the grip?'),

  sectionLabel('Exercises'),
  subhead('The \u201CMine\u201D to \u201CMe\u201D Map (10 minutes)'),
  body('This exercise is about clarity, not guilt. Write honest answers.'),
  numbered('Something in my financial life that I would lose a piece of my identity over if I lost it: (not just inconvenienced \u2014 genuinely destabilized)'),
  numbered('What that thing represents to me is: (security / proof that I\u2019m doing okay / freedom / status / something else)'),
  numbered('If it disappeared tomorrow and God said \u201CI took it because it belongs to me,\u201D my honest response would be: (one sentence)'),
  numbered('One act of remembering I can practice today \u2014 naming something God provided that I didn\u2019t create: (one sentence)'),

  subhead('The Remembering Practice (2 minutes)'),
  body('Complete this sentence out loud if you can:'),
  bullet('\u201CGod, thank you for the strength you\u2019ve given me to __________.'),
  bullet('\u201CToday, I will remember you by __________.'),

  sectionLabel('Write This Declaration'),
  declaration('Lord, you are the Owner. My life is not defined by what I have. I remember that my strength comes from you, and I choose to hold what you\u2019ve entrusted to me with gratitude and open hands.'),

  sectionLabel('Next Steps'),
  body('Pick one. Keep it practical. Do it today.'),
  optionHead('A', 'The \u201CRemember\u201D Moment'),
  body('Take two minutes and write five things you have that you didn\u2019t create: your health, an opportunity, a relationship, a skill, provision in a hard season. Thank God for each one by name.'),
  optionHead('B', 'The Identity Reset'),
  body('The next time you catch yourself feeling unusually defensive, anxious, or competitive about something financial, pause and say: \u201CMy life does not consist in what I possess. God is my source.\u201D Then continue calmly.'),
  optionHead('C', 'The Open-Hand Decision'),
  body('Make one small decision today that reflects a lighter grip: delay an unnecessary purchase, simplify a choice you\u2019ve been overthinking, or do something quietly generous for someone else without drawing attention to it.'),

  sectionLabel('Closing Prayer'),
  body('Father, forgive me for the ways I\u2019ve quietly believed my strength and my planning are the source of my security. Thank you for every good gift you\u2019ve given me \u2014 including the ability to work, decide, and provide. Help me remember you today. Free me from letting possessions define my life. Teach me to hold what I have with gratitude and open hands, and give me a steady identity rooted in you rather than in what I\u2019ve accumulated. In Jesus\u2019 name, amen.'),
];

// ─── DAY 4 ────────────────────────────────────────────────────────────────────

const day4 = [
  pageBreak(),
  ...dayHeader(4, 'Owned and Loved', 'God\u2019s Ownership Is Personal, Not Corporate', 'God\u2019s ownership is not a claim. It\u2019s a rescue.'),

  sectionLabel("Today's Verses"),
  ...scripture('1 Corinthians 6:19\u201320 (NIV)', 'Do you not know that your bodies are temples of the Holy Spirit, who is in you, whom you have received from God? You are not your own; you were bought at a price. Therefore honor God with your bodies.'),
  ...scripture('Isaiah 43:1 (ESV)', 'But now thus says the Lord, he who created you, O Jacob, he who formed you, O Israel: \u201CFear not, for I have redeemed you; I have called you by name, you are mine.\u201D'),

  sectionLabel('Opening'),

  body('One of Ron Blue\u2019s clients was a physician in his late thirties when they first met. He was one of the early heart surgeons at a time when the procedure was still experimental, and he had made significant money. He and his wife had designed and built their dream home \u2014 a million-dollar property at a time when that was genuinely remarkable.'),
  body('He came to Ron with a question he clearly felt awkward asking: \u201CIs it okay for a Christian to live in a million-dollar home?\u201D'),
  body('Ron said he immediately thought of James 1:5 \u2014 \u201Cif any of you lacks wisdom, let him ask God\u201D \u2014 and turned the question back. \u201CWhat do you think God wants you to do?\u201D The doctor said he didn\u2019t know. Ron asked if he spent time every day in prayer and Scripture. The doctor admitted he didn\u2019t \u2014 he was in surgery by six in the morning and on call at night. Ron said, \u201CWhat are you doing at four in the morning? Generally sleeping? Then you don\u2019t have anything better to do. Get up and spend ten minutes asking God that question.\u201D'),
  body('He did. A year and a half later, Ron ran into the doctor\u2019s wife. She said: \u201CI don\u2019t know what you did to him, but he\u2019s now spending two or three hours every morning in prayer and Bible study.\u201D'),
  body('The doctor never asked Ron about the home again. That house became a center of ministry \u2014 hundreds of people came to faith there. He became a significant evangelical leader, the chairman of multiple international ministries. And the question he started with \u2014 \u201Cis it okay for a Christian to live here?\u201D \u2014 was replaced by the only question that ever really mattered: \u201CLord, what would you have me to do?\u201D'),
  body('That shift \u2014 from \u201Cis this allowed?\u201D to \u201Cwhat does faithfulness look like here?\u201D \u2014 is only possible when you understand something about the nature of God\u2019s ownership. It isn\u2019t corporate. It isn\u2019t impersonal. It doesn\u2019t come from a distance. It comes from someone who knows your name.'),

  subhead('Ownership as Rescue'),

  body('There\u2019s a reason some people hear \u201CGod owns it all\u201D and feel threatened rather than relieved. The word \u201Cowns\u201D can sound transactional. Like a claim on property rather than a relationship with a person. If your experience with authority has been harsh or conditional, the concept of ownership can feel like a loss: loss of freedom, loss of choice, loss of yourself.'),
  body('But 1 Corinthians 6:19\u201320 reframes the word entirely. \u201CYou are not your own \u2014 you were bought at a price.\u201D That\u2019s not God taking. That\u2019s God giving. The price isn\u2019t paid by you. It\u2019s paid for you. Ownership in the gospel is not a power move. It is a rescue story. He didn\u2019t purchase you to use you. He redeemed you to love you. He didn\u2019t claim you as a project. He claimed you as a person.'),
  body('That kind of ownership doesn\u2019t dehumanize you. It dignifies you. It says your life is valuable enough to be rescued. Your soul is important enough to be redeemed. Your story is worth reclaiming.'),

  subhead('Ownership as Belonging'),

  body('Then Isaiah puts it in the most personal language possible: \u201CI have called you by name, you are mine.\u201D'),
  body('God doesn\u2019t claim you like an asset. He calls you like a Father. He knows your name. He knows your story. He knows what you\u2019re carrying. And he says, \u201CYou belong to me.\u201D That sentence is not corporate language. It\u2019s family language. It\u2019s the kind of sentence you say when someone is scared, when they\u2019re uncertain, when they\u2019re tempted to believe they\u2019re alone.'),
  body('\u201CYou are mine\u201D is not a threat. It\u2019s a shelter.'),
  body('The phrase \u201Ccalled you by name\u201D matters more than it might seem. Because many people feel genuinely unknown \u2014 even in crowds, even in church, even in families. Many people carry private pressures that nobody sees. Many people are quietly exhausted from trying to appear strong. Isaiah is telling you that God\u2019s ownership isn\u2019t generic. It\u2019s personal. He doesn\u2019t merely own the universe; he knows his children. He doesn\u2019t just rule from a distance; he calls you by name.'),

  subhead('Ownership as Protection'),

  body('And here is where this matters practically for money and possessions: we often use financial resources to answer questions that only love can answer. We use money to feel secure. We use money to feel valuable. We use money to feel like we belong. But money can never give you what identity gives you. It can never love you back.'),
  body('Money can\u2019t tell you, \u201CI have called you by name.\u201D Money can\u2019t hold you when you\u2019re grieving. Money can\u2019t forgive you when you fail. Money can\u2019t keep its promises forever. And if you treat money as the place where you get safety and belonging, you\u2019ll always need more \u2014 more margin, more certainty, more options, more \u201Cjust in case.\u201D That\u2019s why even people with significant resources can feel unsettled. The issue is rarely the amount. It\u2019s the foundation.'),
  body('When God says \u201CYou are mine,\u201D he\u2019s relocating your worth from what you have to who holds you. He\u2019s relocating your security from your accumulation to his care. He\u2019s relocating your identity from what you produce to who you belong to. And that re-location changes everything about how you handle money \u2014 not because you now have rules, but because you now have a resting place.'),

  pullquote('Stewardship is not performance for approval. It is response to love. That changes everything about how you make decisions with money \u2014 not from fear, but from freedom.'),

  sectionLabel('Think About It'),
  body('Where does the idea of God\u2019s \u201Cownership\u201D of your life feel like a restriction rather than a rescue? What belief about God underlies that feeling?'),
  body('The physician Ron worked with eventually stopped asking \u201Cis this allowed?\u201D and started asking \u201CLord, what would you have me do?\u201D What would it look like for you to make that same shift in one specific area of your financial life?'),
  body('If your security truly came from God\u2019s care rather than from your accumulation, what would become easier to release today?'),

  sectionLabel('Exercises'),
  subhead('Ownership as Love (10 minutes)'),
  body('Write short answers. This is about receiving, not performing.'),
  numbered('The area where God\u2019s ownership feels most like a restriction rather than a rescue: (future / finances / family / reputation / plans)'),
  numbered('The fear underneath that feeling is: (loss / uncertainty / being forgotten / being controlled / not enough)'),
  numbered('The truth I want to receive today is: (I belong to God / I am not alone / God is steady / God redeemed me)'),
  numbered('One practical step that would reflect \u201CI belong to a loving Father\u201D rather than \u201CI must secure myself\u201D: (one sentence)'),

  subhead('Name and Belonging (2 minutes)'),
  body('Complete these out loud:'),
  bullet('\u201CGod, you have called me by name. Today I belong to you in __________.'),
  bullet('\u201CBecause I belong to you, I will take this next step: __________.'),

  sectionLabel('Write This Declaration'),
  declaration('Father, I belong to you. I am not my own, and I am not alone. Teach me to steward my life and my resources as a loved child \u2014 not from fear, but from trust in the One who called me by name.'),

  sectionLabel('Next Steps'),
  body('Pick one. Keep it simple. Do it today.'),
  optionHead('A', 'The Belonging Pause'),
  body('Before your next financial decision, pause and say: \u201CI belong to God.\u201D Then choose calmly and faithfully \u2014 not from what protects you, but from what honors him.'),
  optionHead('B', 'The Release List'),
  body('Write three things you\u2019ve been gripping \u2014 a fear, a plan, an outcome. Pray over each: \u201CFather, I\u2019m yours. This is yours too.\u201D Then release them without immediately picking them back up.'),
  optionHead('C', 'The Quiet Act'),
  body('Do one small act of generosity today that no one will see. Let it be a response to belonging, not a display of it.'),

  sectionLabel('Closing Prayer'),
  body('Father, thank you that your ownership is personal. You have redeemed me, called me by name, and made me yours. Forgive me for the ways I\u2019ve tried to find security and identity in what I can hold or control. Today I receive your love and your care. Teach me to live as your steward with a steady heart \u2014 faithful in what you\u2019ve entrusted to me, and surrendered in what I cannot control. I belong to you. Lead me. Amen.'),
];

// ─── DAY 5 ────────────────────────────────────────────────────────────────────

const day5 = [
  pageBreak(),
  ...dayHeader(5, 'Tool. Test. Testimony.', 'What God Is Doing With Your Money Right Now', 'Your trust shows up in your choices, not your intentions.'),

  sectionLabel("Today's Verses"),
  ...scripture('Matthew 6:21 (NIV)', 'For where your treasure is, there your heart will be also.'),
  ...scripture('Philippians 4:11\u201312 (NIV)', 'I am not saying this because I am in need, for I have learned to be content whatever the circumstances. I know what it is to be in need, and I know what it is to have plenty. I have learned the secret of being content in any and every situation.'),

  sectionLabel('Opening'),

  body('Ron Blue once asked a mega-church pastor a direct question: after forty years in financial services, he had come to believe that God\u2019s Word speaks authoritatively to every financial decision \u2014 gives wisdom for the process and principles for the decisions, at all times, under any circumstances. \u201CIt works as well in Africa as it does on Wall Street,\u201D Ron told him. \u201CIt works for a single mom and for a billionaire.\u201D'),
  body('The pastor\u2019s response surprised him. He said: \u201CIf that\u2019s the case, Ron, why is it that the church is not seen as the center of financial wisdom?\u201D'),
  body('Ron thought about that question for a long time. His answer had something to do with shame \u2014 the way money conversations in church settings often end up feeling guilt-based rather than grace-based. But underneath it was something else: most people don\u2019t actually understand what God is doing with their money. They think of their finances as a practical problem to solve. They don\u2019t see it as a spiritual formation process already in motion.'),
  body('But it is. God uses money in three specific ways in every believer\u2019s life. And once you understand those three ways, the daily experience of your finances \u2014 the tight months, the abundant ones, the decisions, the surprises \u2014 stops feeling like random noise and starts feeling like something with a shape.'),

  subhead('Money as a Tool'),

  body('The most straightforward way God uses money is as a tool \u2014 a resource that enables people to accomplish purposes. It funds families, builds organizations, sends missionaries, serves the poor, and creates margin to be generous. At this level, money is simply the means to an end. You use it, and it does things.'),
  body('But it\u2019s also a tool in God\u2019s hands to do things in you. The discipline of a budget isn\u2019t only about spending less. It\u2019s a practice of aligning your priorities with what you say you value. The habit of giving isn\u2019t only about meeting needs. It\u2019s a practice of trust \u2014 demonstrating to yourself and to God that he matters more than what you\u2019re releasing.'),
  body('Ron would say: if you let me look at your checkbook and your tax return and your credit card statements, I could tell you your goals, your values, and your priorities. Not because money is the most important thing in your life \u2014 but because the way you handle it tells the truth about what is.'),

  subhead('Money as a Test'),

  body('Paul says in Philippians 4 that he \u201Clearned\u201D to be content. Not that he felt content naturally. Not that his circumstances became easy. He learned it \u2014 through seasons of need and seasons of plenty \u2014 until contentment became a strength rather than a mood.'),
  body('That word \u201Clearned\u201D is important, because it tells you that contentment is not a personality trait. It\u2019s a formation outcome. And money is one of the primary classrooms where God teaches it. When you\u2019re in a tight season, you find out what you actually trust. When you\u2019re in an abundant season, you find out what you actually love. Both directions reveal the heart.'),
  body('The test isn\u2019t pass or fail. It\u2019s diagnostic. God isn\u2019t testing you to catch you out. He\u2019s testing you the way a good coach tests a player \u2014 to show you where you\u2019ve grown and where you still need formation. The unexpected expense isn\u2019t just an inconvenience. The financial uncertainty isn\u2019t just a problem. They\u2019re the test revealing what you genuinely believe about who owns it and whether he can be trusted.'),

  subhead('Money as a Testimony'),

  body('The third way God uses money is the one most people don\u2019t think about: as a testimony. Ron believed deeply \u2014 and said it often \u2014 that the world is living in confusion and fear and doubt, asking the same three wrong questions over and over. And the world has a right to look at Christians and see something different.'),
  body('Not better. Different. The person with less anxiety than the circumstances justify. The couple whose marriage doesn\u2019t fracture under financial pressure the way every other couple\u2019s does. The man who gives generously when it doesn\u2019t make mathematical sense. The woman who is genuinely content when the culture is constantly telling her she needs more. That\u2019s a testimony. It\u2019s not a sales pitch. It\u2019s a life that answers the world\u2019s questions by living from a different foundation.'),

  pullquote('Money has no voice, but it has a record. If someone followed you for thirty days and looked at your bank statements, what would they conclude about what you trust?'),

  body('Matthew 6:21 says treasure leads and the heart follows. Which means how you handle money is shaping your heart \u2014 right now, in ordinary weeks, in unremarkable decisions. That\u2019s not meant to make you paranoid about every purchase. It\u2019s meant to help you take your financial habits seriously as a spiritual formation practice. Because the habits are forming you whether you\u2019re paying attention or not.'),

  sectionLabel('Think About It'),
  body('Looking at the three uses of money \u2014 tool, test, testimony \u2014 which one feels most active in your life right now? What is God doing in that dimension?'),
  body('When you think about the word \u201Clearned\u201D in Philippians 4 \u2014 contentment as something practiced and formed rather than felt naturally \u2014 what season in your financial life has taught you the most? What did it teach?'),
  body('If your life is meant to be a testimony \u2014 showing the world that a different foundation produces a different kind of peace \u2014 what specific thing about how you handle money most clearly reflects that right now? What most clearly contradicts it?'),

  sectionLabel('Exercises'),
  subhead('The Tool/Test/Testimony Inventory (10 minutes)'),
  body('Write short, honest answers.'),
  numbered('One way money is functioning as a tool in my life right now \u2014 something God is accomplishing through it: (one sentence)'),
  numbered('One way money is currently functioning as a test \u2014 what my financial situation is revealing about what I trust: (one sentence)'),
  numbered('One way my financial life could be more clearly a testimony \u2014 if I changed one specific thing: (one sentence)'),
  numbered('The area where \u201Ctreasure leads and heart follows\u201D is most clearly true for me right now: (one sentence)'),

  subhead('The Trust Mirror (2 minutes)'),
  body('Answer these honestly:'),
  bullet('One spending or saving habit that most reveals what I actually prioritize: (one sentence)'),
  bullet('One choice I could make this week that would redirect my treasure and, over time, redirect my heart: (one sentence)'),

  sectionLabel('Write This Declaration'),
  declaration('Jesus, you are my Master. My treasure will follow you. Teach me to choose faithfulness over fear, and to use what you\u2019ve entrusted to me as a tool for your purposes, an open field for your formation, and a testimony to your faithfulness.'),

  sectionLabel('Next Steps'),
  body('Pick one. Keep it practical. Do it today.'),
  optionHead('A', 'The Pause-and-Choose Practice'),
  body('Before any non-essential purchase today, pause and ask: \u201CWhat is this decision revealing about what I trust?\u201D Then choose with clarity.'),
  optionHead('B', 'The Quiet Redirection'),
  body('Give a small amount today in a way no one else will see. Let it be a private act of redirecting your treasure \u2014 training your heart to follow.'),
  optionHead('C', 'The One-Category Look'),
  body('Pull up one month of bank or credit card statements. Don\u2019t analyze it. Just look at it and ask: \u201CIf a stranger looked at this, what would they conclude about what I value?\u201D Write one sentence in response.'),

  sectionLabel('Closing Prayer'),
  body('Father, thank you for using my finances to form me \u2014 through tools that accomplish purposes, tests that reveal my heart, and a testimony that can point others toward something better. Teach me to handle what you\u2019ve entrusted to me with the awareness that it is doing something in me, not just for me. Give me a contented heart that has learned \u2014 and keeps learning \u2014 what you taught Paul. And let my life, including my finances, be a quiet testimony to the world that you are enough. Amen.'),
];

// ─── DAY 6 ────────────────────────────────────────────────────────────────────

const day6 = [
  pageBreak(),
  ...dayHeader(6, 'Anxiety and Ownership', 'Worry Is Often a Control Issue', 'God doesn\u2019t ask you to carry tomorrow. He asks you to trust him today.'),

  sectionLabel("Today's Verses"),
  ...scripture('Matthew 6:33 (NIV)', 'But seek first his kingdom and his righteousness, and all these things will be given to you as well.'),
  ...scripture('Philippians 4:6\u20137 (ESV)', 'Do not be anxious about anything, but in everything by prayer and supplication with thanksgiving let your requests be made known to God. And the peace of God, which surpasses all understanding, will guard your hearts and your minds in Christ Jesus.'),

  sectionLabel('Opening'),

  body('When Ron Blue started his financial planning practice, he did what any sensible business owner does at the beginning: he went to the bank and arranged a $10,000 line of credit. That\u2019s how you start a business. You establish liquidity. You give yourself runway. You protect yourself against the unexpected.'),
  body('Then he felt a quiet but persistent conviction: you\u2019re going to start a practice that gives people financial advice, and you\u2019re going to begin with debt?'),
  body('He paraphrased it himself, later: \u201CI\u2019m paraphrasing God. And I said, I don\u2019t think that is either.\u201D'),
  body('So he canceled the line of credit. He had no backup. He had a family to feed. He had a business to start. And he had no idea what was going to happen.'),
  body('What happened next is the kind of story that\u2019s hard to tell without it sounding like a formula. But it isn\u2019t a formula. It\u2019s a testimony. Not long after he canceled the credit, a friend connected him with the head of training at Coca-Cola. The man asked Ron to develop and teach a financial seminar for retiring employees. He outlined the scope and asked what Ron would charge. Ron, who had never done this before, said he had no idea. The man did some quick calculations: $6,000 to develop it, $1,000 each time to teach it, four sessions. Total: $10,000. The exact amount Ron had given up. Paid in December so it could go into that year\u2019s budget.'),
  body('Ron didn\u2019t tell that story to argue that obedience always produces the exact number you surrendered. He told it to say something else: worry is almost always about control. And surrendering control is almost always what makes room for God to move.'),

  subhead('What Worry Is Actually Doing'),

  body('Most people don\u2019t choose worry because they enjoy it. They choose it because it feels like responsibility. It feels like staying alert. It feels like the mind\u2019s way of proving it cares. For many people, worry is how they demonstrate to themselves that they\u2019re not being careless, that they\u2019re staying ahead, that they\u2019re not naive.'),
  body('But Jesus, in Matthew 6, treats worry differently. He doesn\u2019t shame it. He diagnoses it. He shows that worry is fundamentally connected to ownership \u2014 specifically, to the assumption that the future belongs to you and that you must secure it. When you live like the future is yours to manage, your mind will work overtime trying to manage it. Not because you\u2019re faithless. Because that\u2019s what owning something feels like.'),
  body('There is a crucial difference between rehearsing and preparing. Preparing asks: what\u2019s mine to do today? It produces action. Rehearsing asks: what if this goes wrong, what if that changes, what if I can\u2019t handle what\u2019s coming? It produces fatigue. Preparing keeps you present. Rehearsing keeps you living in a future that doesn\u2019t exist yet, carrying weight for scenarios that may never arrive.'),
  body('Worry is rehearsal. And rehearsal, however well-intentioned, is a form of trying to sit in the first chair.'),

  subhead('What Jesus Actually Does'),

  body('In Matthew 6, Jesus doesn\u2019t say \u201Cstop worrying\u201D as if it\u2019s a simple decision. He builds a case. He points to birds and flowers \u2014 not to romanticize life, but to make a specific argument: if your Father sustains what you don\u2019t even think about most days, how much more is he present to what you actually need?'),
  body('Then he gives what may be the most practically actionable sentence in the entire Sermon on the Mount: \u201CSeek first his kingdom and his righteousness, and all these things will be given to you as well.\u201D That\u2019s not a spiritual platitude. It\u2019s a re-ordering of priorities that has concrete daily application. Seeking first means God\u2019s agenda shapes your decisions before your fear does. It means you don\u2019t wait until you feel safe to obey \u2014 you obey as a way of learning safety.'),
  body('Seeking first might mean you pray before you plan instead of after. It might mean you slow down a decision that fear is rushing. It might mean you choose honesty in a financial conversation you\u2019ve been avoiding. It might mean you adopt one wise habit that builds stability over time rather than trying to fix everything overnight. The shape of it varies. The direction is always the same: God\u2019s priorities before your anxiety\u2019s demands.'),

  pullquote('Worry doesn\u2019t carry what you\u2019re carrying. It just keeps you busy while you carry it alone. Prayer is the exchange: you bring it into the light, and the peace of God \u2014 which doesn\u2019t require everything to be solved \u2014 stands guard over what you brought.'),

  subhead('What Paul Adds'),

  body('Philippians 4:6\u20137 gives you a practice, not just a principle. \u201CIn everything, by prayer and supplication, with thanksgiving, let your requests be made known to God.\u201D That\u2019s not telling you to deny what\u2019s hard. It\u2019s telling you to bring what\u2019s hard into God\u2019s presence rather than carrying it inside your own head.'),
  body('Worry keeps it inside you. Prayer brings it into the light. And notice what the promise is: not that the problem disappears, but that the peace of God will guard your heart and mind. Peace as a guard. A stabilizing presence in the middle of real, unresolved circumstances. It doesn\u2019t require everything to be solved. It requires you to stop carrying it alone.'),
  body('A steady person makes wiser decisions than a pressured one. Steady people have more patience for the right step. Steady people can have difficult conversations without escalating them. Steady people can wait. Prayer doesn\u2019t make you passive. It makes you steadier. And steadiness, as it turns out, is one of the most practical financial skills you can develop.'),

  sectionLabel('Think About It'),
  body('Think about your biggest financial anxiety right now. Are you rehearsing it or preparing for it? What\u2019s the difference between those two postures in this specific situation?'),
  body('Ron canceled his security net and God provided the exact amount he\u2019d given up. That story isn\u2019t a formula, but it does illustrate something: what specific area of your financial life might God be inviting you to stop controlling and start trusting him with?'),
  body('\u201CSeek first his kingdom\u201D is a daily re-ordering. What would it look like in one practical decision you\u2019re currently facing \u2014 to let God\u2019s priorities shape your decision before your anxiety does?'),

  sectionLabel('Exercises'),
  subhead('The Worry-to-Prayer Inventory (10 minutes)'),
  body('Write short, honest answers.'),
  numbered('The financial concern I\u2019m rehearsing most often right now is: (one sentence)'),
  numbered('What I\u2019m trying to protect underneath that concern is: (security / stability / family / reputation / options)'),
  numbered('What is actually mine to do about this \u2014 the responsible step: (one sentence)'),
  numbered('What is God\u2019s to carry \u2014 what I need to stop trying to manage: (one sentence)'),

  subhead('The \u201CSeek First\u201D Practice (2 minutes)'),
  body('Complete these two lines:'),
  bullet('\u201CGod, today I\u2019m seeking your kingdom first in __________.'),
  bullet('\u201CMy next faithful step \u2014 not the whole plan, just the next step \u2014 is __________.'),

  sectionLabel('Write This Declaration'),
  declaration('Father, you are the Owner. I release tomorrow into your care. Teach me to seek you first today, and to take the next faithful step with a steady heart \u2014 preparing, not rehearsing; trusting, not controlling.'),

  sectionLabel('Next Steps'),
  body('Pick one. Keep it simple. Do it today.'),
  optionHead('A', 'The Prayer Swap'),
  body('Write down your most persistent financial worry in one sentence. Under it, write a one-sentence prayer giving it to God. Thank him for his care before anything has changed. Pray it twice today.'),
  optionHead('B', 'The Ten-Minute Boundary'),
  body('Set a ten-minute limit on scenario-thinking today. When your mind tries to run longer than that on \u201Cwhat if\u201D, stop and pray Philippians 4:6\u20137 instead. Literally read it out loud.'),
  optionHead('C', 'The One Faithful Step'),
  body('Identify one practical action that builds stability \u2014 a conversation you\u2019ve avoided, a plan you haven\u2019t started, one wise adjustment. Do it calmly today, without needing to solve everything past it.'),

  sectionLabel('Closing Prayer'),
  body('Father, you know what I\u2019m carrying and what I\u2019m afraid could happen. Thank you that you care for me personally and completely. Teach me to seek your kingdom first and to trust you with outcomes I can\u2019t control. Turn my rehearsing into preparing, and my pressure into wisdom. Guard my heart and my mind with your peace as I take the next faithful step. In Jesus\u2019 name, amen.'),
];

// ─── DAY 7 ────────────────────────────────────────────────────────────────────

const day7 = [
  pageBreak(),
  ...dayHeader(7, 'You\u2019re Different, Not Better', 'What a Surrendered Life Looks Like to the World', 'Stewardship is not a one-time decision. It is a daily return.'),

  sectionLabel("Today's Verses"),
  ...scripture('Colossians 1:16\u201317 (NIV)', 'For in him all things were created: things in heaven and on earth, visible and invisible, whether thrones or powers or rulers or authorities; all things have been created through him and for him. He is before all things, and in him all things hold together.'),
  ...scripture('1 Timothy 6:6 (NIV)', 'But godliness with contentment is great gain.'),

  sectionLabel('Opening'),

  body('Ron Blue had a client in his early years as a financial planner \u2014 a physician who had built enormous wealth and then made a decision that Ron watched play out over decades. He capped his lifestyle at the level he\u2019d been living when he finished medical school. Everything above that, he gave away. He went on mission trips to Haiti. He funded hospitals. He invested in people he\u2019d never meet.'),
  body('Over time, Ron noticed the man trading his Porsche for a Honda. Physicians, as a rule, don\u2019t drive Hondas into the physician\u2019s parking lot. This one did. He had to park down the street.'),
  body('And Ron noticed something about him that he came to believe was the most reliable indicator he ever found of financial health: the man was content. Not resigned. Not performing contentment for an audience. Actually, genuinely, visibly at peace with his finances, his life, and his God. His wife was the same. His marriage had a quality of communication that Ron observed in almost no one else he worked with.'),
  body('At the same time, Ron had another client: the CEO of a major grocery chain who lived in a trailer park. Not because he had to. Because he chose to. He had also capped his lifestyle at a level far below what his income could support, and he gave the rest away.'),
  body('These two men couldn\u2019t have looked more different. One lived in a million-dollar home. One lived in a trailer park. But they had arrived at the same place by the same path: on their knees, asking God what enough looked like for them. And both of them, Ron said, were genuinely free.'),
  body('That\u2019s what Week 1 has been building toward. Not a financial framework. A different kind of person.'),

  subhead('The World Is Watching'),

  body('Ron believed \u2014 deeply and consistently \u2014 that one of the most powerful testimonies a Christian can have in a confused, restless culture is simply this: being different. Not better. Different. Not superior \u2014 calmer. Not wealthier \u2014 more content. Not without pressure \u2014 but handling pressure from a foundation that produces steadiness rather than panic.'),
  body('The world, he said, has a right to look at Christians and ask: why are they different? Why do they have a quality of peace that doesn\u2019t depend on the market going up? Why does their marriage not crack under financial pressure the way everyone else\u2019s does? Why are they generous when it doesn\u2019t make mathematical sense? Why do they seem okay with enough?'),
  body('Those questions, if they get asked, are an open door. And they only get asked when the life behind them is actually different. Claimed beliefs that produce the same restlessness as everyone else\u2019s don\u2019t open any doors.'),

  subhead('What Stewardship Produces'),

  body('Colossians 1:16\u201317 is one of the most stabilizing passages in the Bible: all things were created through him and for him, and in him all things hold together. That last phrase changes the daily experience of your finances. Your life is not held together by your vigilance. It\u2019s not held together by your perfect plan. It\u2019s not held together by your ability to anticipate every turn. It is held together by someone stronger, steadier, and wiser than you.'),
  body('That doesn\u2019t cancel your responsibility. It relocates your confidence. And relocated confidence produces a particular kind of person \u2014 the kind who can take wise action without acting like every decision carries the weight of their future. The kind who can plan without being mastered by the plan. The kind who can be faithful without carrying the impossible burden of certainty.'),
  body('A steward asks different questions than an owner.'),
  body('An owner asks: \u201CHow do I protect what\u2019s mine?\u201D A steward asks: \u201CHow do I honor God with what\u2019s entrusted to me?\u201D'),
  body('An owner asks: \u201CHow do I stay in control?\u201D A steward asks: \u201CWhat is the next faithful step?\u201D'),
  body('An owner asks: \u201CWhat if it goes wrong?\u201D A steward asks: \u201CWho is holding this with me?\u201D'),
  body('Those questions, asked daily, form a person over time. Not dramatically. Quietly. The way any habit forms: through repetition, one ordinary decision at a time, until the new thing starts to feel normal.'),

  pullquote('Your old default was: I have to hold this together. Your new default is: God holds all things together, and I am faithful with what\u2019s in my hands today. That shift doesn\u2019t happen once. It happens every morning.'),

  subhead('The Daily Return'),

  body('You will drift. Everyone does. The goal of these seven days has not been to eliminate drift. It\u2019s been to introduce a new default \u2014 a place to return to when you notice you\u2019ve drifted. The difference between a mature steward and an immature one isn\u2019t that the mature one never wanders. It\u2019s that they return faster.'),
  body('A daily reset is how that return becomes quick. It doesn\u2019t have to be complicated. One sentence before the day starts. One pause before a decision. One prayer when your grip tightens. \u201CGod, you\u2019re the Owner. I\u2019m your steward. Lead me today.\u201D Then the next faithful step. Not the whole plan. Just the next step.'),
  body('Ron said he saw, in the lives of people who lived this way, four things consistently: contentment, confidence, clarity of communication \u2014 especially in marriages \u2014 and consistency of behavior. Not as achievements they worked toward. As fruit that grew naturally when the foundation was right.'),
  body('That\u2019s the promise of Week 1. Not that your finances will immediately improve. Not that your circumstances will change. But that when the foundation shifts \u2014 when you genuinely answer the ownership question differently \u2014 everything built on it changes too. The way you handle money. The way you talk to your spouse about it. The way you face the next hard season. The way you hold what you have.'),
  body('Different, not better. But genuinely, visibly, surprisingly different.'),

  sectionLabel('Think About It'),
  body('Think about someone you know \u2014 or have heard of \u2014 who handles money with genuine peace. What is it about the way they live that produces that quality? What would you need to believe to live that way?'),
  body('The physician in the Honda and the CEO in the trailer park arrived at the same place by the same path: on their knees, asking God what enough looked like for them. Have you ever spent time asking that question? What came up?'),
  body('Ron described four fruits of a life lived with God\u2019s ownership as its foundation: contentment, confidence, clarity of communication, consistency of behavior. Which of these is most missing in your financial life right now? What would it take to begin cultivating it?'),

  sectionLabel('Exercises'),
  subhead('The Daily Reset Plan (10 minutes)'),
  body('Write short, practical answers.'),
  numbered('The moment in my day when I most often drift back into owner thinking: (morning / before a purchase / in a hard conversation / when something unexpected happens)'),
  numbered('My old default in that moment: (tighten / avoid / overthink / react / try harder)'),
  numbered('My new steward response could be: (one sentence)'),
  numbered('One simple practice I can repeat this week to build the new default: (pause + one sentence prayer / write a sentence / ask one question / review one category)'),

  subhead('The Steward Questions (2 minutes)'),
  body('Answer these quickly, then carry them into your day:'),
  bullet('\u201CIf God owns it all, what is mine to do today?'),
  bullet('\u201CIf Christ holds all things together, what can I release?'),

  sectionLabel('Write This Declaration'),
  declaration('God, you are the Owner. I am your steward. Today I will practice open hands, take the next faithful step, and trust you to hold what I cannot. I am different because of whose I am. Not better \u2014 different.'),

  sectionLabel('Next Steps'),
  body('Pick one. Keep it simple. Do it today.'),
  optionHead('A', 'The Morning Return'),
  body('Before you check your phone, pray: \u201CGod, you own it all. Lead me today.\u201D Then take one small faithful step \u2014 not a perfect plan, just the next thing.'),
  optionHead('B', 'The Decision Pause'),
  body('Before your next money decision, pause for ten seconds and ask: \u201CWhat would a steward do right now?\u201D Then choose calmly.'),
  optionHead('C', 'The End-of-Day Review'),
  body('Tonight, ask yourself two questions: \u201CWhere did I live like a steward today?\u201D and \u201CWhere did I drift back into ownership?\u201D Thank God for one win. Surrender one drift. Then rest.'),

  sectionLabel('Closing Prayer'),
  body('Father, thank you that I am not the owner of my life. Thank you that in Christ, all things hold together \u2014 not by my vigilance, but by your power. Forgive me for the ways I live as if everything depends on me. Teach me a new default: open hands, steady trust, faithful obedience. Help me remember your ownership not just in moments of worship, but throughout the day \u2014 in the ordinary decisions, the unexpected pressures, the daily chances to be genuinely different. Give me wisdom for what is mine to do, peace for what is not, and the courage to take the next faithful step. Amen.'),
];

// ─── BUILD DOCUMENT ───────────────────────────────────────────────────────────

const doc = new Document({
  styles: {
    default: {
      document: { run: { font: 'Georgia', size: 22 } }
    },
    paragraphStyles: [
      {
        id: 'Heading1', name: 'Heading 1', basedOn: 'Normal', next: 'Normal', quickFormat: true,
        run: { size: 36, bold: true, font: 'Georgia', color: '1F4E79' },
        paragraph: { spacing: { before: 0, after: 60 }, outlineLevel: 0 }
      }
    ]
  },
  numbering: {
    config: [
      {
        reference: 'bullets',
        levels: [{
          level: 0, format: LevelFormat.BULLET, text: '\u2022',
          alignment: AlignmentType.LEFT,
          style: { paragraph: { indent: { left: 560, hanging: 280 } } }
        }]
      },
      {
        reference: 'numbers',
        levels: [{
          level: 0, format: LevelFormat.DECIMAL, text: '%1.',
          alignment: AlignmentType.LEFT,
          style: { paragraph: { indent: { left: 560, hanging: 280 } } }
        }]
      }
    ]
  },
  sections: [{
    properties: {
      page: {
        size: { width: 12240, height: 15840 },
        margin: { top: 1440, right: 1440, bottom: 1440, left: 1440 }
      }
    },
    children: [
      // Title
      new Paragraph({
        alignment: AlignmentType.CENTER,
        spacing: { before: 720, after: 160 },
        children: [new TextRun({ text: 'GOD OWNS IT ALL', bold: true, size: 44, font: 'Georgia', color: '1F4E79' })]
      }),
      new Paragraph({
        alignment: AlignmentType.CENTER,
        spacing: { before: 0, after: 80 },
        children: [new TextRun({ text: 'Days 1\u20137 \u2014 Revised Draft', size: 26, font: 'Arial', color: '555555', italics: true })]
      }),
      new Paragraph({
        alignment: AlignmentType.CENTER,
        spacing: { before: 0, after: 80 },
        children: [new TextRun({ text: 'The Ownership Question: What does it really mean if God owns it all?', size: 22, font: 'Arial', color: '777777' })]
      }),
      new Paragraph({
        alignment: AlignmentType.CENTER,
        spacing: { before: 120, after: 720 },
        children: [new TextRun({ text: 'Writing Team Working Document \u2014 Not for Distribution', size: 18, font: 'Arial', color: '999999' })]
      }),
      rule(),
      // Editor note
      new Paragraph({
        spacing: { before: 120, after: 80 },
        children: [new TextRun({ text: 'Notes on this revision:', bold: true, size: 20, font: 'Arial' })]
      }),
      new Paragraph({
        spacing: { before: 40, after: 40 },
        numbering: { reference: 'numbers', level: 0 },
        children: [new TextRun({ text: 'Every day now opens with a Ron Blue story or direct teaching from the transcripts, sourced to specific session and timestamp in the master source document.', size: 20, font: 'Arial' })]
      }),
      new Paragraph({
        spacing: { before: 40, after: 40 },
        numbering: { reference: 'numbers', level: 0 },
        children: [new TextRun({ text: 'All bold \u201CI must\u2026\u201D first-person affirmations have been removed and replaced with integrated prose or second-person questions.', size: 20, font: 'Arial' })]
      }),
      new Paragraph({
        spacing: { before: 40, after: 40 },
        numbering: { reference: 'numbers', level: 0 },
        children: [new TextRun({ text: 'Exercises in Days 1\u20133 have been differentiated so each day advances the reader rather than repeating the same grip inventory.', size: 20, font: 'Arial' })]
      }),
      new Paragraph({
        spacing: { before: 40, after: 40 },
        numbering: { reference: 'numbers', level: 0 },
        children: [new TextRun({ text: 'The duplicate sentence in Day 1 (\u201CI must define faithful\u201D) and the illogical \u201Cbank account\u201D reference in Day 2 have been corrected.', size: 20, font: 'Arial' })]
      }),
      new Paragraph({
        spacing: { before: 40, after: 40 },
        numbering: { reference: 'numbers', level: 0 },
        children: [new TextRun({ text: 'Day 4 superscript verse-number error removed. Day 5 \u201Ctestifies\u201D phrase rewritten to avoid potential attribution issue.', size: 20, font: 'Arial' })]
      }),
      new Paragraph({
        spacing: { before: 40, after: 40 },
        numbering: { reference: 'numbers', level: 0 },
        children: [new TextRun({ text: 'Day 6 \u201Cbackground music\u201D metaphor (editor-flagged) replaced with \u201Crehearsal\u201D framing, which is more precise and more useful.', size: 20, font: 'Arial' })]
      }),
      new Paragraph({
        spacing: { before: 40, after: 40 },
        numbering: { reference: 'numbers', level: 0 },
        children: [new TextRun({ text: 'Day 7 retitled and refocused as testimony rather than recap; the two-clients illustration (Bloomington transcript) added to close the week.', size: 20, font: 'Arial' })]
      }),
      rule(),
      pageBreak(),
      ...day1,
      ...day2,
      ...day3,
      ...day4,
      ...day5,
      ...day6,
      ...day7,
    ]
  }]
});

Packer.toBuffer(doc).then(buf => {
  fs.writeFileSync('/mnt/user-data/outputs/GOIA_Days_1-7_Revised.docx', buf);
  console.log('Done');
});
