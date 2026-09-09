# -*- coding: utf-8 -*-
# Family Legacy Campaign — the complete 40 days.
# Regenerates Week One with extended navigation and builds Weeks Two–Six,
# Sessions Two–Six, week hubs, and the Day Forty family meeting.
import pathlib, re, importlib.util

# ---- import build.py for Week One content dicts + base CSS (fonts embedded)
spec = importlib.util.spec_from_file_location("bp", "/home/claude/flbd/build.py")
bp = importlib.util.module_from_spec(spec)
spec.loader.exec_module(bp)   # side effect: rewrites site/ week-one; harmless

OUT = pathlib.Path("/home/claude/flbd/site_full")
OUT.mkdir(exist_ok=True)
CSSNAME = "flbd-campaign.css"

EXTRA_CSS = r"""
/* ---------- full-campaign additions ---------- */
.weeknav{display:flex;flex-wrap:wrap;gap:.45rem;margin:1.4rem 0 0}
.weeknav a{font-size:.85rem;font-weight:600;text-decoration:none;color:var(--ink);background:var(--paper);border:1px solid var(--line);border-radius:999px;padding:.38rem .85rem}
.weeknav a:hover{border-color:var(--gold)}
.weeknav a[aria-current="page"]{background:var(--green);border-color:var(--green);color:var(--paper)}
.card.gold40{grid-column:1/-1;background:var(--gold);border-color:var(--gold);color:#241D0E}
.card.gold40 h3{color:#241D0E;font-size:1.5rem}
.card.gold40 p{color:#43350F;max-width:62ch}
.card.gold40 .dn{color:#6B4F0E}
.card.gold40 .go{margin-top:.4rem;color:#241D0E;font-weight:700}
.order{counter-reset:mo;margin:.4rem 0 0;max-width:62ch}
.order div{counter-increment:mo;display:grid;grid-template-columns:34px 1fr;gap:.7rem;padding:.8rem 0;border-bottom:1px solid var(--line);align-items:start}
.order div:last-child{border-bottom:0}
.order div::before{content:counter(mo);font-family:'Besley',serif;font-weight:800;color:var(--gold-ink);font-size:1.15rem;line-height:1.4}
.order b{font-family:'Besley',serif;font-weight:700;font-size:1.1rem;color:var(--green-deep);display:block}
.order p{font-size:1rem;line-height:1.6;color:var(--ink)}
"""

(OUT / CSSNAME).write_text(bp.CSS + EXTRA_CSS, encoding="utf-8")

# ---------------------------------------------------------------- week meta
WEEKS = {
 1: dict(hub="Week_One_Family_Legacy.html",  name="Waking Up to Legacy", kick="Week One \u00b7 Waking Up to Legacy",
   dek="Waking up to the legacy already in motion \u2014 seven short readings, and the family\u2019s first conversation.",
   intro="Week One does one thing: it wakes the household up. The readings move from the legacy your family is already leaving, to the five areas where legacy really lives, to the honest numbers behind failed inheritances \u2014 and then to grace, to the table, and to the posture that makes a first conversation safe. By week\u2019s end, your family has sat down together once, on purpose. That is the whole assignment, and it is enough."),
 2: dict(hub="Week_Two_Family_Legacy.html",  name="Clarity", kick="Week Two \u00b7 Clarity",
   dek="Before a family can align, each person has to get clear \u2014 on time, treasure, name, and the sentence a life is writing.",
   intro="Clarity is the first of the three words this whole work stands on \u2014 clarity, alignment, communication \u2014 and it starts with the person in the mirror, not the people at the table. This week each member of the family does their own quiet accounting: numbering the days, following the treasure, weighing the family name, and writing it plain \u2014 until it all condenses into one sentence you could hand your grandchildren. Session Two is where the sentences get read aloud."),
 3: dict(hub="Week_Three_Family_Legacy.html", name="Alignment", kick="Week Three \u00b7 Alignment",
   dek="A family that knows its story and names its values can finally pull in one direction \u2014 with God holding the center.",
   intro="Alignment is not agreement on everything; it is agreement on the few things that govern everything. This week the family checks its foundation, goes back for the story it came from, names where it has been walking in two directions, and braids the third strand into the cord. By the Story Table on Session night, three family values are chosen out loud \u2014 and one house makes the old Joshua declaration its own."),
 4: dict(hub="Week_Four_Family_Legacy.html", name="Communication", kick="Week Four \u00b7 Communication",
   dek="The week the postponed conversation finally happens \u2014 hearts turned home, truth in love, and the books opened.",
   intro="Everything the first three weeks built comes due here, because clarity and alignment travel on communication or they do not travel at all. This week hearts turn toward home, truth learns to wear love, the soft answer gets rehearsed, and the conversation named back on Day Four finally gets its hour. The week ends at Open Books \u2014 the family money conversation most households have never once had."),
 5: dict(hub="Week_Five_Family_Legacy.html", name="The Wider Circle", kick="Week Five \u00b7 The Wider Circle",
   dek="Legacy was never meant to stop at the property line \u2014 work, blessing, and giving carry it into the world.",
   intro="Two of the five areas wait outside the front door: the business legacy and the charitable one. This week the family settles whose it all is, looks at daily work as more than a paycheck, traces the blessings that arrived through its own line, and practices the open hand. At the Giving Table, the family chooses one gift to give together \u2014 youngest voice first."),
 6: dict(hub="Week_Six_Family_Legacy.html", name="The Family Meeting", kick="Week Six \u00b7 The Family Meeting",
   dek="Forty days of noticing, naming, and talking converge on one table, one statement, one blessing \u2014 and one sealed envelope.",
   intro="Everything in the folder \u2014 the one-sentence legacies, the three values, the elders\u2019 answers, the giving decision \u2014 now gets composed into a single page: the Family Legacy Statement. The readings this week commit the plan, gather the elder\u2019s charge, name the true finish line, and count the heritage already in hand. Session Six drafts the statement. And on Day Forty, the family holds the meeting this whole journey promised \u2014 where the envelope from Week One is finally opened."),
}

# ---------------------------------------------------------------- days 8–14
DAYS2 = {
8: dict(
 slug="Day_Eight_Family_Legacy.html",
 title="Number the Days",
 dek="Clarity begins with arithmetic nobody wants to do \u2014 and everybody is freed by doing.",
 sv="So teach us to number our days, that we may apply our hearts unto wisdom.",
 sref="Psalm 90:12 \u00b7 KJV",
 card="Do the Saturday math \u2014 a numbered horizon is where wisdom starts.",
 body=[
"Let me put my accountant\u2019s hat on for a moment and ask you to do a small piece of arithmetic. Take the age you can reasonably hope to reach \u2014 be generous with yourself \u2014 subtract your age today, and multiply what\u2019s left by fifty-two. That is roughly the number of Saturdays you have remaining. I have watched people do this math at a conference table, and I can tell you the room always goes quiet. Not because the number is small. Because it is a number at all.",
"Moses prayed for exactly this. \u201cTeach us to number our days\u201d \u2014 not to dread them, number them \u2014 \u201cthat we may apply our hearts unto wisdom.\u201d Notice the order of that sentence. The counting comes first; the wisdom follows. An unnumbered life feels infinite, and infinite things never require decisions. That is why the family conversation keeps sliding to someday. Someday is what a calendar looks like when no one has counted it.",
"Here is what I have noticed at the tables where the counting finally happens: nothing gets sadder, and everything gets clearer. The father who counts his Saturdays stops assuming there will be a better season to take his son fishing. The grandmother who counts hers writes the letter this month instead of intending it for years. Deadlines, it turns out, are a form of love. They tell the heart what actually matters, because they take away the luxury of everything mattering later.",
"This week is about clarity, and clarity is personal before it is ever shared. Before your family can align around anything, you have to know what you yourself are living for \u2014 and there is no honest answer to that question on an unlimited timeline. So we start where Moses started: with the number.",
"Do the math today. Write the number down where you will see it. It is not morbid. It is the doorway wisdom has always used.",
 ],
 q="If you took your remaining Saturdays seriously, what would move to the top of the list \u2014 this month, not someday?",
 step="Do the Saturday math and write the number at the top of a fresh page. Under it, write the first three things the number makes urgent. This page begins your legacy folder \u2014 it all comes to the table on Day Forty.",
 prayer="Lord, teach me to number my days \u2014 not to fear them, but to spend them. Take someday out of my vocabulary this week. Amen.",
 adv="You already run this conversation in disguise every time you model retirement horizons and life expectancy. This week, run it undisguised. The Saturday math takes ninety seconds in a review meeting, and it converts more someday clients into scheduled family conversations than any brochure you will ever hand out.",
 ask="Ask one client: \u201cCan I show you a number that changed how I think about my own calendar?\u201d",
),
9: dict(
 slug="Day_Nine_Family_Legacy.html",
 title="Follow the Treasure",
 dek="You don\u2019t find out what a family loves by asking. You find out by auditing.",
 sv="For where your treasure is, there will your heart be also.",
 sref="Matthew 6:21 \u00b7 KJV",
 card="The calendar and the statement never lie \u2014 run the treasure audit before you write a word.",
 body=[
"There are two documents that will tell you the truth about your family faster than any heart-to-heart conversation: the calendar and the bank statement. I have spent a career reading the second one, and I will tell you a professional secret \u2014 people\u2019s money always confesses. We say we value what we say we value. Our statements say what we actually value, line by line, month after month, without a trace of embarrassment.",
"Jesus put the principle in a single sentence, and notice which direction it runs: \u201cwhere your treasure is, there will your heart be also.\u201d We usually quote it backward, as though the heart leads and the treasure follows. He said the opposite. The treasure leads. Put your treasure somewhere \u2014 your money, your hours, your best attention \u2014 and your heart will pack its bags and move there. Which means the two documents on your kitchen counter are not just records of the past. They are maps of where your heart is currently headed.",
"So today\u2019s clarity work is an audit, and I mean that in the friendliest professional sense. Sit down with last month \u2014 one calendar, one statement \u2014 and read them like an outsider would. If a stranger inherited these two documents and nothing else, what would they conclude this family treasures? Write down the honest answer, even if it stings a little. Especially if it stings a little.",
"Now, hear me the way I mean it: this is not a guilt exercise. Some of what you find will be good news \u2014 evidence of faithfulness you have stopped noticing because it became routine. The mortgage that shelters people you love. The line item for the church. The Tuesday that always belongs to your daughter. Clarity means seeing all of it, the treasure well placed and the treasure that drifted.",
"Because here is the quiet hope inside the hard verse: if treasure leads and the heart follows, then the heart can be led. Move the treasure on purpose, and the heart comes along. That is not a theory. That is Tuesday.",
 ],
 q="If a stranger read your last month\u2019s calendar and statement, what would they say your family treasures?",
 step="Run the audit tonight: one month of calendar, one month of statement. Write two findings in the folder \u2014 one place your treasure is exactly where you want your heart, and one place you\u2019re ready to move it.",
 prayer="Father, I\u2019ve heard my own money confess tonight. Thank You for what it said that was faithful. Give me the courage to move what needs moving \u2014 and let my heart follow. Amen.",
 adv="You hold the second document already \u2014 you see where the treasure actually goes. This week, invite one client to read their own statement through Matthew 6:21 instead of through performance. \u201cIf this statement were the only evidence, what would it say your family loves?\u201d It is the most clarifying question in the review book, and it costs nothing.",
 ask="Try it gently: \u201cWould you be open to reading last quarter\u2019s statement a different way \u2014 not for returns, but for treasure?\u201d",
),
10: dict(
 slug="Day_Ten_Family_Legacy.html",
 title="The Weight of a Name",
 dek="Your family\u2019s most valuable asset never appears on a statement \u2014 and it transfers automatically.",
 sv="A good name is rather to be chosen than great riches, and loving favour rather than silver and gold.",
 sref="Proverbs 22:1 \u00b7 KJV",
 card="The name transfers whether you plan it or not \u2014 weigh what yours has come to mean.",
 body=[
"There is one asset every family transfers with perfect efficiency \u2014 no probate, no taxes, no paperwork, no delay. The name. Your children walked into their first classroom already carrying it. They will walk into rooms you will never see, decades from now, and it will still be arriving ahead of them, opening some doors and closing others. Solomon ran the comparison and published his finding: a good name outvalues great riches. Not equals \u2014 outvalues. And he was a man in a position to price both.",
"I have sat with families where the name was worth more than the estate, and I have sat with families where the estate spent its first decade paying down what the name had come to mean. A name is simply a reputation compounding across generations \u2014 every kept promise a deposit, every cut corner a withdrawal, interest accruing on both. The town, the industry, the church, the neighborhood: they have all been keeping the ledger for years, whether or not the family ever looked at it.",
"So today, look at it. Not your grandfather\u2019s name and not your children\u2019s \u2014 yours, the stretch of the ledger you have been writing. When your family\u2019s name comes up in a room you are not in, what three words follow it? Answer honestly. If you genuinely don\u2019t know, that itself is worth knowing \u2014 and there may be someone in your life brave enough to tell you if you ask.",
"Then turn the question forward, because this is the clarity that matters: what three words do you want to follow the name after you have handed it on? Generous. Honest. Safe \u2014 as in, that family is safe to deal with, safe to confide in, safe to be small around. Write your three down. You are not describing the name today. You are choosing what you will spend the rest of your Saturdays depositing into it.",
"The riches your family transfers will be counted once, at settlement. The name gets counted every day, forever. Choose accordingly \u2014 that is all Solomon was saying.",
 ],
 q="What three words follow your family\u2019s name today \u2014 and what three do you want to follow it in thirty years?",
 step="Write both sets of three words in the folder: the honest today-words, and the chosen tomorrow-words. Circle the one tomorrow-word that will cost you the most to make true. That circle is this month\u2019s work.",
 prayer="Lord, You know what our name has come to mean \u2014 the deposits and the withdrawals alike. Redeem what needs redeeming, and help me spend my remaining days making the name a blessing to carry. Amen.",
 adv="Every advisor manages riches; almost none ever ask about the name. This week, ask one founding-generation client what they want their family\u2019s name to mean in the town in thirty years \u2014 then be quiet. You will learn more about their real estate plan in that silence than in any questionnaire they have ever filled out for you.",
 ask="Ask them: \u201cThirty years from now, when your family\u2019s name comes up in this town \u2014 what do you want the next sentence to be?\u201d",
),
11: dict(
 slug="Day_Eleven_Family_Legacy.html",
 title="Write It Plain",
 dek="An unwritten legacy is a wish. Ink is where intention starts becoming inheritance.",
 sv="Write the vision, and make it plain upon tables, that he may run that readeth it.",
 sref="Habakkuk 2:2 \u00b7 KJV",
 card="Vision goes on paper so the next runner can carry it \u2014 five plain lines, today.",
 body=[
"When God had something He intended to outlast the man He said it to, He gave a standing instruction: write it down. Not remember it, not feel deeply about it \u2014 write it, and write it plain, so that the one who reads it can run with it. I love the practicality of that verse. The vision is not written for the visionary. It is written for the runner \u2014 the next person, the one who has to carry it after you have stopped explaining it in person.",
"Thirty years of professional life have made me a believer in the same instruction, for a humbler reason: unwritten things do not survive the person who holds them. I have watched it at settlement tables more times than I can count. The intentions were real. The values were real. The love was real. But none of it was written anywhere except inside the one heart that had just left the room \u2014 and a family cannot inherit the inside of a heart. They inherit what made it onto paper, and they guess at the rest. The guessing is where families come apart.",
"Notice, too, the word plain. Habakkuk wasn\u2019t told to write something impressive. Plain means the reader doesn\u2019t stumble. Your family does not need your legacy in polished paragraphs; they need it in sentences a teenager could read at a kitchen table and understand without a lawyer present. Fancy is for documents that protect assets. Plain is for words that carry hearts.",
"So today the folder gets its first real page of vision. Five lines \u2014 that\u2019s the whole assignment. What I believe. What I\u2019m building. What I hope this family becomes. What I\u2019m grateful for. What I want to say to the ones who come after me. One plain sentence under each. Do not polish; you are not publishing today, you are surveying. The polishing comes later in the journey, when the family writes together.",
"You have spent three days getting clear \u2014 the number, the treasure, the name. Today clarity does the thing clarity is for: it becomes legible to someone besides you.",
 ],
 q="If your family could read only five plain sentences from you \u2014 not hear, read \u2014 what would they need to say?",
 step="Write the five lines in the folder tonight, one plain sentence each: believe, building, becoming, grateful, and a word to those who come after. Ugly first drafts welcome. Ink beats intention.",
 prayer="Lord, You wrote Your covenant down for us; teach me to write mine down for them. Make my vision plain enough for the next runner to carry. Amen.",
 adv="Your clients\u2019 binders are full of written instruments and empty of written intent \u2014 the what fully documented, the why entirely oral. Offer one client a single-page \u201cletter of intent\u201d exercise alongside their documents this month. It is not legal work, it is legacy work, and it is the page the heirs will actually read twice.",
 ask="Offer it plainly: \u201cYour documents say what happens. Would you give me one page, in your own words, on why?\u201d",
),
12: dict(
 slug="Day_Twelve_Family_Legacy.html",
 title="The Wisdom Transfer",
 dek="The most expensive lessons in your life were paid for once. Handing them down means nobody pays twice.",
 sv="Wisdom is the principal thing; therefore get wisdom: and with all thy getting get understanding.",
 sref="Proverbs 4:7 \u00b7 KJV",
 card="Wealth without wisdom is a loaded gift \u2014 write down the three lessons that cost you most.",
 body=[
"Proverbs 4 is a father talking to his son about inheritance, and it is striking what he leads with. Not the fields, not the flocks, not the accounts \u2014 wisdom. \u201cWisdom is the principal thing.\u201d The old word principal is doing quiet work in that sentence, and my profession can\u2019t help but notice it: the principal is the sum everything else grows from. This father is telling his boy that wisdom is the asset, and everything else in the estate is interest.",
"Here is why that ordering matters so much, and why I have come to believe the wisdom transfer must run ahead of the wealth transfer, not behind it. Wealth is stored decisions \u2014 years of judgment, restraint, courage, and recovery, compressed into numbers. Hand someone the numbers without the judgment that produced them, and you have not given them your success. You have given them a loaded instrument and no training. The research we looked at in Week One \u2014 the heirs who were never prepared \u2014 that is this page. Preparation is not paperwork. Preparation is wisdom, delivered early and in person.",
"But the wisdom in your house did not come free, and that is the part families forget to say out loud. Every piece of real wisdom you own has a receipt attached \u2014 the business decision that taught you which handshakes to trust, the season of debt that taught you what interest really costs, the fracture with someone you loved that taught you how pride negotiates. You paid full price for those lessons, in years and in tears. When the lesson gets handed down, the next generation gets it at no charge. When it doesn\u2019t, they pay retail all over again \u2014 same tuition, same pain, one generation later.",
"So today\u2019s clarity work is to itemize the principal. Three lessons \u2014 the three that cost you the most to learn. Write each one down along with what it cost, because the price tag is what makes the lesson stick when it\u2019s told. Not \u201cbe careful with debt\u201d \u2014 that\u2019s a poster. \u201cHere is the year debt owned our house, and here is what it took to buy it back\u201d \u2014 that\u2019s an inheritance.",
"You will get the chance to hand one of these across the table before this journey ends. Today, just get them on paper \u2014 principal first, like the father said.",
 ],
 q="What is the most expensive lesson you own \u2014 and has anyone in the next generation ever heard the whole story of what it cost?",
 step="Write three lessons in the folder, each with its price tag: what you learned, and what learning it cost you. Star the one your family most needs and has never fully heard.",
 prayer="Father, You let none of my tuition go to waste \u2014 every hard season taught me something worth handing on. Give me the humility to tell the whole story, price tag included. Amen.",
 adv="You have watched wealth arrive on unprepared heirs, and you know how that story runs. Preparation is a service line, not a sentiment: propose one \u201clessons meeting\u201d to a client family this quarter \u2014 the founding generation telling the next the three decisions that built the estate, with you facilitating. It will outperform any product meeting you hold this year.",
 ask="Ask the founders: \u201cYour heirs will inherit your results. Who is scheduled to hand them your reasoning?\u201d",
),
13: dict(
 slug="Day_Thirteen_Family_Legacy.html",
 title="One Sentence",
 dek="Five days of accounting condense into a single line \u2014 the sentence your life is writing.",
 sv="For to me to live is Christ, and to die is gain.",
 sref="Philippians 1:21 \u00b7 KJV",
 card="Paul\u2019s whole legacy fit in nine words \u2014 this is the day you draft yours.",
 body=[
"A man sat in a Roman prison, unsure whether he would leave it alive, and wrote his life down in nine words: \u201cFor to me to live is Christ, and to die is gain.\u201d No estate to speak of. No heirs of his body. And yet twenty centuries later, families on the far side of the world \u2014 yours, this week \u2014 are still living off the interest of that one sentence. Paul understood something about legacy that all our documents keep missing: what survives is not the inventory. What survives is the sentence.",
"Every life is writing one, whether or not it ever gets said aloud. Live long enough around a person and you can read it \u2014 the sentence underneath their choices, the one their calendar and their statement and their name have been spelling out for years. For some it is a sentence they would be proud to sign. For others it is a sentence that got written by default, one unexamined year at a time. This week\u2019s whole work \u2014 the Saturdays, the treasure, the name, the five plain lines, the lessons \u2014 has been quarrying the stone. Today you carve.",
"Here is the form, and I hold it loosely: \u201cTo live, for me, is ______ \u2014 so that ______.\u201d The first blank is your center; the second is your aim beyond yourself. But do not let the form fight you. What matters is the test every strong legacy sentence has to pass: Is it true \u2014 would the people who live with you recognize it? Is it plain \u2014 could a twelve-year-old repeat it? And is it yours \u2014 or is it a greeting card wearing your name? A borrowed sentence blesses nobody. A true one, however rough, can steer a family for a hundred years.",
"Expect the first draft to embarrass you a little. Mine did. Write it anyway, then say it out loud in an empty room \u2014 the ear catches what the eye forgives. Cross out every word doing no work. What is left, copy onto a card. Not a page this time. A card, sized to be carried \u2014 because tomorrow you weigh it, and this week your family hears it.",
"Nine words held a man steady in a Roman prison. Yours does not need to be immortal. It needs to be true, and it needs to be written \u2014 today.",
 ],
 q="If your life keeps going exactly as it is, what sentence is it currently writing \u2014 and is that the sentence you mean?",
 step="Draft your legacy sentence and copy the honest version onto a card for the folder: \u201cTo live, for me, is ___ \u2014 so that ___.\u201d Say it aloud once before you sleep. It gets read at the table this week.",
 prayer="Lord, You know the sentence my years have actually been writing. Where it is true, seal it; where it drifted, help me revise while there is still ink. Let my line point at You. Amen.",
 adv="Every client you serve is one sentence underneath a hundred pages of documents \u2014 and most have never been asked for it. This week, ask one: \u201cIf your whole legacy had to fit in a single sentence your grandchildren would repeat, what is it?\u201d Write down their exact words. That sentence is the investment policy statement behind the investment policy statement.",
 ask="Ask them, and then wait: \u201cWhat\u2019s the one sentence you\u2019d want your grandchildren to finish this way \u2014 \u2018Our family believed\u2026\u2019?\u201d",
),
14: dict(
 slug="Day_Fourteen_Family_Legacy.html",
 title="The Audience of One",
 dek="Before the sentence gets read at your table, carry it to the only review that finally matters.",
 sv="Well done, thou good and faithful servant: thou hast been faithful over a few things\u2026 enter thou into the joy of thy lord.",
 sref="Matthew 25:21 \u00b7 KJV",
 card="Two words are the finish line \u2014 read your sentence to the audience of One before the table hears it.",
 body=[
"At the end of the parable of the talents, the master reviews his servants, and the faithful ones hear the same two words: well done. Notice what the words are attached to \u2014 not the size of the return, but the faithfulness of the handling. The five-talent man and the two-talent man receive the identical commendation, syllable for syllable. Heaven\u2019s review, it turns out, is not graded on assets under management. It is graded on stewardship of whatever was entrusted \u2014 few things or many.",
"I have come to believe those two words are the true finish line of this entire journey, and I want to say plainly why. Everything we have done this week \u2014 numbering days, auditing treasure, weighing the name, writing it plain, pricing the lessons, carving the sentence \u2014 can be done for an audience of family, and that is good. But family is not the final audience. Long after the estate settles and the name fades and even the sentence is forgotten, each of us stands before One \u2014 and the deepest hope of this work is not a tidy transfer. It is that you and everyone at your table would hear well done.",
"That changes how you should read the card you wrote yesterday. So today, before your family hears your sentence at the table this week, read it to God first. Find ten unhurried minutes. Put the card in front of you and ask the honest version of the question: Lord, is this a sentence You could say well done over? Not \u2014 is it impressive. Not \u2014 will it land well at the table. Is it faithful? Does it steward what You actually placed in my hands: this family, these years, this name, these lessons, this treasure?",
"Sit with whatever comes back. Sometimes it is a quiet yes, and the card is ready. Sometimes one word needs to change \u2014 a word you wrote for the audience of the room instead of the audience of One. Change it without grief; that is not failure, that is the review working. This is the meeting every other meeting in this campaign is rehearsing for.",
"Tomorrow, Week Three begins and the work turns from the mirror to the table \u2014 from clarity to alignment. You are ready for that turn precisely to the degree that today\u2019s ten minutes were honest. One audience first. Then the family.",
 ],
 q="Is your legacy sentence written for the room \u2014 or for the review?",
 step="Take ten unhurried minutes with your card and the audience of One. Ask: is this faithful? Revise the one word that was written for applause, if there is one. Then the card is sealed for the table.",
 prayer="Master, I bring You my few things \u2014 this family, these years, this sentence. I am not asking You to call it impressive. I am asking You to help me make it faithful, so that one day I hear the two words. Amen.",
 adv="Kingdom-minded clients carry a question they rarely say in a financial office: does God approve of how I\u2019m handling this? You cannot answer it for them \u2014 but you can make room for it. This week, close one review by asking what \u201cfaithful\u201d would look like for their wealth, not just \u201coptimal.\u201d The clients who light up at that question are your legacy families.",
 ask="Close one meeting with: \u201cSet performance aside for a second \u2014 what would faithful look like for this money?\u201d",
),
}
print("Part A loaded:", len(DAYS2), "Week Two days")
