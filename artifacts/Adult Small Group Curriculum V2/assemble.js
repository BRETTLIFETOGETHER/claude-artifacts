const { renderSession, allSessions, helpers, docx } = require('./build.js');
const {
  Document, Packer, Paragraph, TextRun, AlignmentType, BorderStyle, PageBreak,
  Table, TableRow, TableCell, WidthType, ShadingType, Header, Footer, PageNumber
} = docx;
const { sectionHeading, bodyPara, leadLine, numItem, plainLine, buildTable, INK, ACCENT, RULE, SHADE, CONTENT_W } = helpers;
const fs = require('fs');

function h1(text) {
  return new Paragraph({ pageBreakBefore: true, spacing: { before: 0, after: 60 },
    children: [new TextRun({ text, bold: true, color: ACCENT, size: 34, allCaps: true, font: "Calibri" })] });
}
function h1nobreak(text) {
  return new Paragraph({ spacing: { before: 220, after: 60 },
    children: [new TextRun({ text, bold: true, color: ACCENT, size: 34, allCaps: true, font: "Calibri" })] });
}
function sub(text) {
  return new Paragraph({ spacing: { after: 160 }, border: { bottom: { color: RULE, space: 4, style: BorderStyle.SINGLE, size: 6 } },
    children: [new TextRun({ text, italics: true, color: "4A5A62", size: 22, font: "Calibri" })] });
}
function bullet(text) {
  return new Paragraph({ spacing: { after: 80, line: 268 }, indent: { left: 360, hanging: 220 },
    children: [new TextRun({ text: "\u2022  ", color: ACCENT, size: 21, font: "Calibri" }), new TextRun({ text, color: INK, size: 21, font: "Calibri" })] });
}
function boldLead(name, rest) {
  return new Paragraph({ spacing: { after: 90, line: 268 },
    children: [new TextRun({ text: name + " ", bold: true, color: INK, size: 21, font: "Calibri" }), new TextRun({ text: rest, color: INK, size: 21, font: "Calibri" })] });
}
function fillLine(text) {
  return new Paragraph({ spacing: { after: 90, line: 276 }, children: [new TextRun({ text, color: INK, size: 21, font: "Calibri" })] });
}

const children = [];

// ---------------- COVER ----------------
children.push(new Paragraph({ spacing: { before: 2600, after: 40 }, alignment: AlignmentType.CENTER,
  children: [new TextRun({ text: "MASTER YOUR MONEY", bold: true, color: ACCENT, size: 64, font: "Calibri" })] }));
children.push(new Paragraph({ spacing: { after: 40 }, alignment: AlignmentType.CENTER,
  children: [new TextRun({ text: "Six Questions That Change How You Hold Everything", italics: true, color: "4A5A62", size: 26, font: "Calibri" })] }));
children.push(new Paragraph({ spacing: { before: 320, after: 40 }, alignment: AlignmentType.CENTER,
  children: [new TextRun({ text: "PARTICIPANT GUIDE", bold: true, color: INK, size: 28, allCaps: true, font: "Calibri" })] }));
children.push(new Paragraph({ spacing: { before: 1600, after: 0 }, alignment: AlignmentType.CENTER,
  children: [new TextRun({ text: "Featuring the teaching of Ron Blue", color: INK, size: 22, font: "Calibri" })] }));
children.push(new Paragraph({ spacing: { after: 0 }, alignment: AlignmentType.CENTER,
  children: [new TextRun({ text: "with Brett Eastman", color: "4A5A62", size: 20, font: "Calibri" })] }));
children.push(new Paragraph({ spacing: { before: 200 }, alignment: AlignmentType.CENTER,
  children: [new TextRun({ text: "A Resource of the Ron Blue Institute", italics: true, color: "4A5A62", size: 19, font: "Calibri" })] }));

// ---------------- TABLE OF CONTENTS ----------------
children.push(h1("Table of Contents"));
children.push(sub("Participant Guide"));
const tocFront = ["A Welcome From Ron Blue", "Using This Workbook", "Outline of Each Session"];
tocFront.forEach(t => children.push(fillLine(t)));
children.push(helpers.spacer(80));
const tocSessions = [
  ["SESSION 1", "THE OWNERSHIP QUESTION", "Who Really Owns It All?"],
  ["SESSION 2", "THE WISDOM QUESTION", "What Does the Bible Actually Say About Money?"],
  ["SESSION 3", "THE FREEDOM QUESTION", "How Do I Have True Financial Freedom?"],
  ["SESSION 4", "THE PLANNING QUESTION", "Where Do I Start?"],
  ["SESSION 5", "THE PURPOSE QUESTION", "What Is God Growing Through My Financial Life?"],
  ["SESSION 6", "THE GENEROSITY QUESTION", "Why Does Giving Change Everything?"]
];
tocSessions.forEach(s => {
  children.push(new Paragraph({ spacing: { before: 60, after: 0 }, children: [
    new TextRun({ text: s[0] + "  ", bold: true, color: ACCENT, size: 21, font: "Calibri" }),
    new TextRun({ text: s[1], bold: true, color: INK, size: 21, font: "Calibri" })
  ]}));
  children.push(new Paragraph({ spacing: { after: 60 }, children: [new TextRun({ text: s[2], italics: true, color: "4A5A62", size: 20, font: "Calibri" })] }));
});
children.push(helpers.spacer(80));
children.push(new Paragraph({ spacing: { before: 80, after: 60 }, children: [new TextRun({ text: "APPENDICES", bold: true, color: ACCENT, size: 22, allCaps: true, font: "Calibri" })] }));
["Small Group Agreement","Small Group Roster","Small Group Calendar","Weekly Check-In","Memory Verse Cards","Prayer and Praise Report","Frequently Asked Questions","About the Authors","About the Ron Blue Institute","What's Next"].forEach(t => children.push(fillLine(t)));
children.push(new Paragraph({ spacing: { before: 80, after: 60 }, children: [new TextRun({ text: "SMALL GROUP LEADERS", bold: true, color: ACCENT, size: 22, allCaps: true, font: "Calibri" })] }));
["Hosting an Open House","Leading for the First Time","Leadership Training 101","Notes"].forEach(t => children.push(fillLine(t)));

// ---------------- A WELCOME FROM RON BLUE ----------------
children.push(h1("A Welcome From Ron Blue"));
children.push(bodyPara("Friend,"));
[
  "There is a phrase on the cover of this study that deserves a second look before you begin: master your money. It sounds like a promise about control, as if the goal were to get on top of your finances and finally stay there. But that is not quite what I mean by it, and the difference matters.",
  "To master your money is not to accumulate enough of it that you stop worrying. I have known people with a great deal who never mastered a dollar of it, because the money was still the thing calling the shots, still setting the pace, still deciding their mood on any given morning. And I have known people with very little who had genuinely mastered what they had, because it had no power over them at all. Mastery was never about the size of the number.",
  "To master your money is to make sure it is serving you, and not the other way around. It is to be the one giving the orders instead of the one taking them. Most people have that backwards without realizing it. They think they are managing their money while their money is quietly managing them, their choices, their fears, even their sense of whether they will be okay.",
  "That is what these six weeks are for. Not a budgeting program, and not one ounce of guilt. Just the honest work of taking hold of something that has probably been holding you, so that money settles into its proper place and you get your freedom back. When that happens, what grows is not a bigger balance. It is contentment, and the quiet that comes with it.",
  "You do not need to have anything figured out to begin. You only need to be willing to take the first step.",
  "I am glad you are here. Let's get started."
].forEach(p => children.push(bodyPara(p)));
children.push(new Paragraph({ spacing: { before: 60, after: 20 }, children: [new TextRun({ text: "Ron Blue", bold: true, color: INK, size: 21, font: "Calibri" })] }));
children.push(new Paragraph({ spacing: { after: 120 }, children: [new TextRun({ text: "[Final letter to be confirmed by Ron Blue and the Ron Blue Institute.]", italics: true, color: "8A8A8A", size: 18, font: "Calibri" })] }));

// ---------------- USING THIS WORKBOOK ----------------
children.push(h1("Using This Workbook"));
children.push(bodyPara("This workbook is yours. Write in it, underline in it, argue with it in the margins. It is built to be used, not kept clean."));
children.push(bodyPara("Here is how to get the most out of it."));
[
  ["Bring it every week.", "Everything you need for the group session is inside: the story, the teaching notes, the questions, the exercise, and the week's readings. You will not need anything else, just a pen and a willingness to be open and honest."],
  ["You do not have to prepare.", "There is no homework before a session. Just show up. If you would like to read ahead, the Introduction and the opening story are a good place to start, but nothing is expected of you in advance."],
  ["Fill in the blanks as you watch.", "During the teaching video you will see a few blanks to complete as Ron speaks. They are there to help the key ideas stick, not to test you. If you miss one, leave it and catch it later."],
  ["The private pages are truly private.", "The Financial Wisdom Exercise and the short self-check in each session are for your eyes only. You will never be asked to read them aloud or share what you wrote. Some of it may be a little uncomfortable to see in your own handwriting. That is not a problem, it is the point. Honest transparency is where change begins."],
  ["Anything can be passed.", "If a question feels too personal, say \"pass.\" No explanation needed. A good group makes room for that, and you will never be pressed to share financial numbers or anything else you would rather keep private."],
  ["Use the daily readings during the week.", "Each session ends with that week's seven readings, which run alongside the Master Your Money 42-day devotional. The group meeting starts the conversation. The daily reading is where it settles in. Ten minutes a day will make a real difference on this journey."],
  ["If you miss a week, come back.", "The readings keep you connected even when you cannot make a meeting, and returning after one absence beats staying away. You will not be behind."]
].forEach(x => children.push(boldLead(x[0], x[1])));
children.push(bodyPara("The whole study is designed to be simple. Show up, be honest, try one step each week, and let God do the slow work of reshaping how you hold what he has given you."));

// ---------------- OUTLINE OF EACH SESSION ----------------
children.push(h1("Outline of Each Session"));
children.push(bodyPara("A typical session in the Master Your Money study includes the sections below. Reading through this now will give you a clear picture of where each meeting is headed."));
[
  ["MEMORY VERSE", "Each session opens with a memory verse that captures the heart of that week's question. Memorizing it is optional, but a single verse carried through the week has a way of reshaping how you see everything else."],
  ["INTRODUCTION", "A brief thought to prepare you for the session and get you thinking about the week's question before the group even begins."],
  ["OPENING STORY", "Every session opens with a story, because truth tends to land differently when you see it in a life before you hear it explained. Your host will read one aloud to set the theme."],
  ["COME TOGETHER", "Real growth on a subject as tender as money is built on trust, and trust grows when people share a little of their own story. This section opens the group with prayer and a couple of easy questions."],
  ["BUILDING A HEALTHY GROUP CULTURE", "A short set of commitments the group agrees to, so the room stays safe, honest, and free of pressure. You will set these in Session 1 and return to them each week."],
  ["LEARN TOGETHER", "Here you watch a short teaching from Ron Blue and begin to see how God's wisdom reframes your own financial life. You will take a few notes and fill in a handful of blanks as you go."],
  ["GROW TOGETHER", "A guided discussion that helps you weave what you are learning into how you actually live. With money, that means change, which grows through honest conversation over time."],
  ["FINANCIAL WISDOM EXERCISE", "Each session puts a practical exercise in your hands, something to work through quietly on your own. These pages are private, and you will never be asked to share them."],
  ["CIRCLES OF LIFE", "A moment to think about who else in your life might enjoy or benefit from this group. Financial wisdom is something almost everyone wrestles with and almost no one talks about."],
  ["NEXT STEPS", "One or two doable actions to carry the session out of the room and into your week. This is where a good conversation becomes a changed habit."],
  ["FAMILY CONVERSATION", "A few questions to take home to a spouse, a child, a parent, or a friend, so the week's theme reaches the people closest to you."],
  ["GOING DEEPER", "If your group has time and wants to go further, each session offers two additional passages and questions to study together or on your own."],
  ["THIS WEEK'S DEVOTIONAL READINGS", "Each week, seven readings from the Master Your Money devotional walk you through the same theme one day at a time, with a short verse and a prompt for each day."],
  ["CLOSE IN PRAYER", "Each session ends by praying for one another. You will share requests and record them on the Prayer and Praise Report so you can pray between meetings."]
].forEach(x => {
  children.push(new Paragraph({ spacing: { before: 100, after: 30 }, children: [new TextRun({ text: x[0], bold: true, color: ACCENT, size: 20, allCaps: true, font: "Calibri" })] }));
  children.push(bodyPara(x[1], { after: 40 }));
});

// ---------------- SESSIONS ----------------
allSessions.forEach(s => { renderSession(s).forEach(el => children.push(el)); });

// ---------------- APPENDICES ----------------
children.push(h1("Appendices"));

// Small Group Agreement
children.push(h1nobreak("Small Group Agreement"));
children.push(new Paragraph({ spacing: { after: 30 }, children: [new TextRun({ text: "OUR PURPOSE", bold: true, color: ACCENT, size: 20, font: "Calibri" })] }));
children.push(bodyPara("To grow together as faithful stewards of everything God has entrusted to us, and to help each other do it with honesty and grace."));
children.push(new Paragraph({ spacing: { before: 60, after: 60 }, children: [new TextRun({ text: "OUR VALUES", bold: true, color: ACCENT, size: 20, font: "Calibri" })] }));
[
  ["Group Attendance", "To give priority to the group meeting, and to call or text if we will be late or absent. (Filling in the Group Calendar will help.)"],
  ["A Safe Environment", "To help create a place where people can be heard and feel loved, especially on a subject as tender as money. No quick fixes, no snap judgments, no advice nobody asked for."],
  ["No Numbers", "To never ask each other what we make, owe, give, or have saved. Dignity matters more than disclosure. What we are after is the heart, not the numbers."],
  ["Respect Differences", "To be gentle and gracious with each other's different backgrounds, seasons, temperaments, and levels of spiritual maturity. We are all works in progress."],
  ["Confidentiality", "To keep whatever is shared strictly within the group, and to speak with care about those outside it. What is said here stays here."],
  ["Freedom to Pass", "To make room for the quiet voices, and to let anyone pass on any question without needing to explain why."],
  ["Encouragement for Growth", "To be givers, not just takers. We want to grow, and to help each other take one faithful next step."],
  ["Shared Ownership", "To remember that this group belongs to all of us, and that each person will take on a small role or responsibility over the six weeks."],
  ["Rotating Hosts and Homes", "To encourage different people to host, and to share the responsibility of leading each meeting. (See the Group Calendar.)"]
].forEach(x => children.push(boldLead(x[0], x[1])));
children.push(new Paragraph({ spacing: { before: 80, after: 60 }, children: [new TextRun({ text: "OUR EXPECTATIONS", bold: true, color: ACCENT, size: 20, font: "Calibri" })] }));
[
  "Refreshments / mealtimes ____________________",
  "Childcare ____________________",
  "When we will meet (day of week) ____________________",
  "Where we will meet (place) ____________________",
  "We will begin at ______ and end at ______",
  "We will do our best to attend a worship service together. Our primary service time will be: ____________________",
  "We will follow the daily readings in the Master Your Money devotional between sessions.",
  "Date of this agreement ____________________",
  "Date we will review this agreement again ____________________"
].forEach(t => children.push(fillLine(t)));

// Small Group Roster
children.push(h1nobreak("Small Group Roster"));
children.push(bodyPara("Pass this around at your first meeting so everyone can stay connected between sessions. Ask someone to type it up and share it with the group during the week."));
children.push(buildTable(["Name","Phone","Email","Ministry / How they serve"], Array.from({length:10}, () => ["","","",""])));

// Small Group Calendar
children.push(h1nobreak("Small Group Calendar"));
children.push(bodyPara("Plan this together at your first meeting. Rotating homes and leaders helps everyone grow and keeps any one person from carrying the whole load. Do not leave the last row blank, decide before the final session what comes next."));
children.push(buildTable(
  ["Session","Date","Host / Home","Leading","Devotional Days"],
  [
    ["1 · The Ownership Question","","","","Days 1-7"],
    ["2 · The Wisdom Question","","","","Days 8-14"],
    ["3 · The Freedom Question","","","","Days 15-21"],
    ["4 · The Planning Question","","","","Days 22-28"],
    ["5 · The Purpose Question","","","","Days 29-35"],
    ["6 · The Generosity Question","","","","Days 36-42"],
    ["What's next?","","","",""]
  ]
));

// Weekly Check-In
children.push(h1nobreak("Weekly Check-In"));
children.push(bodyPara("Real change with money rarely happens alone, and it rarely happens by accident. Pair up with one other person in the group as check-in partners for these six weeks. Each week, take a few minutes to tell each other the one step you are taking and how the last one went. It only takes a few minutes, and it is often the difference between a good conversation and a changed habit."));
children.push(bodyPara("You will not share numbers, just your next step and how it is going."));
children.push(fillLine("My Name: ____________________"));
children.push(fillLine("My Partner's Name: ____________________"));
children.push(buildTable(
  ["", "My Step This Week", "How It Went"],
  [
    ["Week 1 · Ownership","",""],
    ["Week 2 · Wisdom","",""],
    ["Week 3 · Freedom","",""],
    ["Week 4 · Planning","",""],
    ["Week 5 · Purpose","",""],
    ["Week 6 · Generosity","",""]
  ]
));

// Memory Verse Cards
children.push(h1nobreak("Memory Verse Cards"));
children.push(bodyPara("One verse per session. Keep each week's verse somewhere you will see it. By the end of six weeks you will have carried all six. All verses are NIV."));
const cards = [
  ["SESSION ONE \u00B7 The Ownership Question", "\u201CYours, Lord, is the greatness and the power and the glory and the majesty and the splendor, for everything in heaven and earth is yours.\u201D", "1 Chronicles 29:11"],
  ["SESSION TWO \u00B7 The Wisdom Question", "\u201CIf any of you lacks wisdom, you should ask God, who gives generously to all without finding fault, and it will be given to you.\u201D", "James 1:5"],
  ["SESSION THREE \u00B7 The Freedom Question", "\u201CKeep your lives free from the love of money and be content with what you have, because God has said, \u2018Never will I leave you; never will I forsake you.\u2019\u201D", "Hebrews 13:5"],
  ["SESSION FOUR \u00B7 The Planning Question", "\u201CCommit to the Lord whatever you do, and he will establish your plans.\u201D", "Proverbs 16:3"],
  ["SESSION FIVE \u00B7 The Purpose Question", "\u201CBut seek first his kingdom and his righteousness, and all these things will be given to you as well.\u201D", "Matthew 6:33"],
  ["SESSION SIX \u00B7 The Generosity Question", "\u201CEach of you should give what you have decided in your heart to give, not reluctantly or under compulsion, for God loves a cheerful giver.\u201D", "2 Corinthians 9:7"]
];
cards.forEach(c => {
  children.push(new Paragraph({
    spacing: { before: 60, after: 0 },
    border: { top: { color: RULE, style: BorderStyle.DASHED, size: 4, space: 6 }, bottom: { color: RULE, style: BorderStyle.DASHED, size: 4, space: 6 }, left: { color: RULE, style: BorderStyle.DASHED, size: 4, space: 6 }, right: { color: RULE, style: BorderStyle.DASHED, size: 4, space: 6 } },
    children: [new TextRun({ text: c[0], bold: true, color: ACCENT, size: 19, font: "Calibri" })]
  }));
  children.push(new Paragraph({ spacing: { after: 10, line: 276 }, children: [new TextRun({ text: c[1], italics: true, color: INK, size: 20, font: "Calibri" })] }));
  children.push(new Paragraph({ spacing: { after: 120 }, children: [new TextRun({ text: c[2], bold: true, color: INK, size: 19, font: "Calibri" })] }));
});

// Prayer and Praise Report
children.push(h1nobreak("Prayer and Praise Report"));
children.push(bodyPara("Each week, share how the group can pray for you, and write down what others share. Then pray during the week, not just in the room. When God answers, come back and fill in the last column. By the end of six weeks you will have a record of what he did."));
children.push(buildTable(["Date","Name","Prayer Request","Praise / Answer"], Array.from({length:12}, () => ["","","",""])));

// FAQ
children.push(h1nobreak("Frequently Asked Questions"));
[
  ["WHAT DO WE DO ON THE FIRST NIGHT?", "Keep it light before it goes deep. A coffee, a dinner, or a good dessert is a great way to start, because trust is what this study runs on, and trust starts with a relaxed room. Walk through the Small Group Agreement together, and say the promise out loud early: no one will ever be asked what they make, owe, give, or have saved. Name a few friends each of you might invite. Mostly, though, just enjoy each other before the study begins."],
  ["WHERE DO WE FIND NEW MEMBERS?", "Pray, then brainstorm. Have the group list people from work, church, the neighborhood, your kids' school, the gym, and family, then invite several of them. Money is something nearly everyone wrestles with and almost no one talks about openly, so more people than you would expect are quietly hoping for a place like this. Do not worry about the room getting too full. You can always split into two circles after the video and come back together to pray."],
  ["HOW LONG WILL THIS GROUP MEET?", "This study runs six weeks. Most groups meet weekly, which keeps momentum going and means a missed meeting is not a missed month. At the end of the six weeks, decide together whether to keep going. Some groups move into another study and stay together for years; others are a stepping-stone to something else. Either way, decide before the last night what comes next, so the momentum has somewhere to go."],
  ["CAN WE DO THIS STUDY ON OUR OWN?", "Absolutely. One of the best ways to do it is with just a couple of friends, or even one other couple. Have a quiet dinner, watch the session, and talk it through. Jesus is present even where two or three gather (Matthew 18:20), and honest conversations about money often go deeper in a smaller room."],
  ["WHAT IF SOMEONE SHARES SOMETHING HEAVY, OR THE GROUP HITS A HARD MOMENT?", "This study touches real fear, real debt, and real regret, so expect some weighty moments. When someone shares something hard, the group's job is to receive it, not fix it. Do not rush to advice or a verse that ties it up. Sit with them. If someone needs more help than a group can give, the leader can follow up privately and point them toward the right resources."],
  ["WHO IS THE LEADER?", "Most groups have one, but the healthiest groups rotate hosting and leading. That way everyone grows and no one carries it alone. You do not need to be a financial expert to lead. In fact, a host who admits they are still figuring money out builds more trust than one who has it all together. This guide, and the Holy Spirit, will keep things on track even as leaders rotate."],
  ["HOW DO WE HANDLE CHILDCARE?", "Carefully, and openly. This is the single most common thing that keeps people from coming, so talk about it as a group rather than leaving each family to solve it alone. Options that work: adults meet in one room while a shared sitter watches the kids in another; or one home hosts the kids and a nearby home hosts the adults; or families simply make their own arrangements. The best approach is to name the problem together and solve it together."]
].forEach(x => {
  children.push(new Paragraph({ spacing: { before: 100, after: 40 }, children: [new TextRun({ text: x[0], bold: true, color: ACCENT, size: 20, font: "Calibri" })] }));
  children.push(bodyPara(x[1]));
});

// About the Authors
children.push(h1nobreak("About the Authors"));
children.push(bodyPara("Ron Blue has spent more than forty-five years helping people understand what God's Word says about money. He founded one of the first financial planning firms built explicitly on biblical principles, has written extensively on stewardship and generosity, and has taught these truths to hundreds of thousands of people around the world. His conviction runs through everything in this study: God owns it all, we are managers of what belongs to him, and settling that one question changes everything downstream."));
children.push(new Paragraph({ spacing: { after: 120 }, children: [new TextRun({ text: "[final bio and credits to be confirmed]", italics: true, color: "8A8A8A", size: 18, font: "Calibri" })] }));
children.push(bodyPara("Brett Eastman spent years overseeing small-group ministry at one of the country's largest churches before founding Lifetogether, where he has built small-group curriculum used by churches around the world. His conviction is that the deepest change happens not in a lecture but in a circle of people learning to follow God with their whole lives, including their money. He brought that approach to Master Your Money, shaping Ron's teaching into honest conversation around the table."));
children.push(new Paragraph({ spacing: { after: 120 }, children: [new TextRun({ text: "[final bio and credits to be confirmed]", italics: true, color: "8A8A8A", size: 18, font: "Calibri" })] }));

// About the Ron Blue Institute
children.push(h1nobreak("About the Ron Blue Institute"));
children.push(bodyPara("The Ron Blue Institute exists to make biblical financial wisdom accessible to everyone, teaching that God owns it all and equipping people to manage his resources faithfully. Its work spans education, curriculum, professional training, and practical tools, including the Live, Give, Owe, Grow spending plan used in this study and other resources such as the Treasure Target."));
children.push(new Paragraph({ spacing: { after: 120 }, children: [new TextRun({ text: "[Organizational description to be confirmed: founding and history, mission statement, key programs and audiences served, and website and contact information.]", italics: true, color: "8A8A8A", size: 18, font: "Calibri" })] }));

// What's Next
children.push(h1nobreak("What's Next"));
children.push(bodyPara("The six weeks end. The journey does not."));
children.push(bodyPara("You have just spent six weeks on the subject most people never talk about honestly, and something got built here that is worth continuing. Before your last meeting, decide together what comes next, and put a date on it."));
children.push(bodyPara("A few directions worth considering:"));
[
  ["Keep meeting.", "Move into another study together and stay in the rhythm you have built. The trust you have now took six weeks to earn. Do not let it cool."],
  ["Take a step as a group.", "Do a thirty-day spending track together, plan a shared act of generosity, or set finish lines and check in on them. Some of the deepest growth happens after the study, when the ideas become practice."],
  ["Run it again as hosts.", "Invite people who were not here and lead a new group through Master Your Money yourselves. You already know it works. Now you get to hand it to someone else."],
  ["Go deeper on the practical side.", "If your church offers a class or a next step on the financial tools, this is a natural time to take it."]
].forEach(x => children.push(boldLead(x[0], x[1])));
children.push(bodyPara("And keep the daily rhythm going. The forty-two days end, but the posture does not have to: money held with open hands, as a tool rather than a master."));

// ---------------- SMALL GROUP LEADERS ----------------
children.push(h1("Small Group Leaders"));
children.push(sub("Key resources to help your leadership experience be the best it can be."));

children.push(h1nobreak("Hosting an Open House"));
children.push(bodyPara("If you are starting a new group, consider hosting an open house before your first formal meeting. Even if you have only two to four core members, it is a great way to break the ice and to prayerfully consider who else might be open to joining you over the next six weeks. You can use this kickoff to hand out workbooks, spend time getting to know each other, talk through what each person is hoping for, and pray together. A simple meal or good dessert always makes it more fun."));
children.push(bodyPara("After people introduce themselves and share how they ended up here, warm up with a few icebreaker questions:"));
children.push(bullet("What is a good money habit, or a bad one, that you picked up from the way you grew up?"));
children.push(bullet("What is one thing you love about your church or your community?"));
children.push(bullet("What is something about your life growing up that most people here do not know?"));
children.push(bodyPara("Next, ask everyone what they are hoping to get out of this study. This is a good moment to walk through the Small Group Agreement and talk about each person's expectations. It is also the moment to say the promise that shapes the whole study out loud: no one will ever be asked what they make, owe, give, or have saved. Naming that at the very start is often what lets people relax and say yes."));
children.push(bodyPara("Finally, set an open chair or two in the center of your group, and explain that each represents someone who would benefit from this group but who is not here yet. Ask everyone to pray about inviting someone over the next few weeks. You can skip this kickoff if your time is limited, but you will gain a lot by taking the time to connect before the study begins."));

children.push(h1nobreak("Leading for the First Time"));
children.push(bodyPara("Sweaty palms are a healthy sign. Scripture says God is gracious to the humble, so remember who is really in control. Those who lead with a soft heart, and sweaty palms, are the ones God tends to speak through."));
[
  ["You do not have to be an expert.", "This is the one that stops people from leading a money study, so hear it clearly. You are not the teacher, and you are not a financial advisor. The video carries the teaching, this guide carries the questions, and a host who admits they have not figured money out either will earn more trust in one night than an expert earns in six weeks."],
  ["Seek support.", "Ask a co-leader or a friend to pray with you and walk through the session beforehand. Reading it ahead helps you anticipate where the harder, more honest moments might come, especially around debt, fear, and giving."],
  ["Prepare, prepare, prepare.", "Go through the session more than once. Watch the teaching segment ahead of time. Read the opening story aloud so it lands when you read it to the group. Do not wait until the last minute."],
  ["Guard the room.", "Your most important job is not asking questions, it is protecting the people answering them. Keep confidentiality sacred, hold the no-numbers promise, and gently redirect the well-meaning member who starts giving financial advice. Safety is what makes honesty possible."],
  ["Let silence do its work.", "After you ask a question, wait longer than feels comfortable. Count to ten. Silence usually means people are thinking, and most leaders rescue it far too soon. The best thing you can say is often \"tell me more about that.\""],
  ["Share what God is doing in you.", "You do not have to have arrived. When you are honest about your own struggle with money and control, you give everyone else permission to be honest too."],
  ["Prayerfully consider who is next.", "As the weeks go on, notice who in your group might host or lead down the road. Make it an invitation, and expect God to do the rest."]
].forEach(x => children.push(boldLead(x[0], x[1])));

children.push(h1nobreak("Leadership Training 101"));
children.push(bodyPara("Congratulations. You are leading a group, and that is one of the most valuable things anyone does in a church. Here are a few principles that will carry you through the six weeks."));
[
  ["Remember you are not alone.", "God is with you, and so is your church. You are not carrying this by yourself, and you are not responsible for having the answers. Your job is to create a place where people can be honest, not to be the expert in the room."],
  ["Do not leave home without it.", "Bring your guide every week, glance through the session ahead of time, and keep a pen handy for prayer requests. A little preparation is the difference between leading the session and reading it."],
  ["Rotate and share.", "Healthy groups rotate homes and leaders. It develops everyone, keeps you from burning out, and quietly raises up the next leaders. Use the Small Group Calendar to plan who hosts and who leads each week."],
  ["Protect the two promises.", "Confidentiality and no numbers. Say both out loud in the first meeting, and guard them all six weeks. Everything else in this study depends on people believing the room is safe."],
  ["The curriculum drives the group, not you.", "You do not have to carry the night. Trust the flow of each session, the questions, the exercise, the story. They do the work if you let them."],
  ["Subgroup when you grow.", "If your group gets big, split into two circles for discussion after the video, then come back together for prayer. Do not let the group get so large that the quiet voices disappear."],
  ["Pray for your people by name.", "Between meetings, pray through the requests on the Prayer and Praise Report. A leader who prays for the group all week leads differently than one who only shows up on the night."],
  ["Decide what is next before it ends.", "A group that finishes well goes somewhere. Before the last session, know what comes next, another study, a serving step, or simply continuing to meet, and be ready to say it out loud with a date."]
].forEach(x => children.push(boldLead(x[0], x[1])));

children.push(h1nobreak("Notes"));
for (let i = 0; i < 10; i++) {
  children.push(new Paragraph({ spacing: { after: 160 }, border: { bottom: { color: RULE, style: BorderStyle.SINGLE, size: 4, space: 2 } }, children: [new TextRun({ text: "", size: 21 })] }));
}

// ---------------- DOCUMENT ----------------
const doc = new Document({
  creator: "Ron Blue Institute",
  title: "Master Your Money — Participant Guide",
  styles: { default: { document: { run: { font: "Calibri", size: 21, color: INK } } } },
  sections: [{
    properties: { page: { size: { width: 12240, height: 15840 }, margin: { top: 1440, bottom: 1440, left: 1440, right: 1440 } } },
    footers: { default: new Footer({ children: [ new Paragraph({ alignment: AlignmentType.CENTER, children: [ new TextRun({ text: "Master Your Money  \u00B7  Participant Guide  \u00B7  ", color: "8A8A8A", size: 16, font: "Calibri" }), new TextRun({ children: [PageNumber.CURRENT], color: "8A8A8A", size: 16, font: "Calibri" }) ] }) ] }) },
    children
  }]
});

Packer.toBuffer(doc).then(buf => {
  fs.writeFileSync('/home/claude/MasterYourMoney_ParticipantGuide.docx', buf);
  console.log('WROTE docx, bytes:', buf.length);
});
