import re, sys

F = "/mnt/user-data/outputs/Communication_30Days_5_Days02-30.md"
t = open(F, encoding="utf-8").read()

R = []

# DAY 2 -- replace invented anecdote with the 75 trusts family
R.append((
"I have sat across from families who had been with a firm for fifteen years and the firm did not know that the son had no interest in the business. Not because anybody lied. Because nobody asked, and there was no obvious moment to volunteer it.",
"""I once worked with a family worth over a billion dollars. They had a family office with four employees, three attorneys and two CPAs on retainer, and an annual planning meeting. When I attended one of those meetings I realized I was the only person in the room who had ever talked to their children.

That family had 75 trusts. All the lawyers were trustees. Nobody had communicated with the kids. The family office leader admitted they had the children sign their tax returns without letting them see the numbers, a paper over the page and a sign here.

Every technical question in that family had been answered by somebody expensive. Not one person had asked the children anything."""))

# DAY 4 -- strip invented personal admission and the four-second statistic
R.append((
"Count it once and you will never unsee it. Ask a real question and watch a clock. Most advisors last about four seconds. Four seconds is not enough time to think about anything.",
"Count it once and you will never unsee it. Ask a real question and watch a clock. Most of us fill the gap long before the person across the table has finished assembling anything, and then we take what we get as their answer."))

R.append((
"I am not asking you to become comfortable with silence. I have been doing this thirty years and I am not comfortable with it. I am asking you to stop treating your discomfort as information about the meeting.",
"I am not asking you to become comfortable with silence. I am asking you to stop treating your discomfort as information about the meeting."))

# DAY 5 -- strip invented autobiography
R.append((
"""I have been on the wrong side of this. Early on I could hold a room and I mistook that for doing my job well. It took a long time to work out that the families who trusted me most were not the ones I had impressed.

They were the ones I had asked something and then let finish.""",
"""Notice which of the three you would defend if somebody accused you of it. That is usually the one.

The families who trust you are not the ones you impressed. They are the ones you asked something and then let finish."""))

# DAY 6 -- replace invented comparative claim with sourced framing
R.append((
"""I have never met a family that fell apart because someone told a lie about the estate.

I have met plenty that fell apart on something everybody assumed.""",
"""Look at Tom's own list of what causes generational failure and notice what is on it. No foundation of faith. Lack of parental or grandparental modeling. Lack of clarity about the family legacy. Lack of communication among generations. Lack of intentionality. Lack of preparation of the next generation.

Not one of those is a lie. Every one of them is something nobody said."""))

# DAY 8 -- replace invented anecdote with the $45 million client
R.append((
"""I have watched happen, over and over, and it is why I keep saying this. The comfort is real and the comfort is temporary, and it is being purchased on credit. The interest is paid later by whoever is in the room when the thing finally has to be decided, usually under time pressure, often after a death, and always with less information than they would have had if somebody had spoken twenty years earlier.

I have sat in those rooms. The people in them are not angry about the money as often as you would think. They are angry that they are finding out now.""",
"""I met with a client who was worth about 45 million, most of it in real estate. He has four kids. I read his documents. He was giving 500,000 dollars to each of his four children and the rest to charity.

I asked him whether he had told his kids what he was doing. He said no. He had told them they should not expect to get anything.

His wife, by the way, did not approve of his plan. She wanted to give the children more than 500,000. He eventually raised it to a million each, and we did have the family meeting.

Here is the part that matters for this reading. Those children were not complaining that they were not getting more of his 45 million. They were excited about working together as a family to impact the world for Christ. The silence had been protecting them from something that turned out not to need protecting from."""))

# DAY 10 -- replace invented anecdote with the daughter who sued
R.append((
"""And the third reason is that time runs out unevenly. Health does not give notice. I have been called in on situations where the conversation everyone intended to have was now being reconstructed from documents by people who were also grieving.""",
"""Here is what the arithmetic looks like when it goes wrong. A father gave his business to his two sons and put an equivalent amount of assets into a trust for his daughter. At the time the business was worth 18 million, so each son received 9 million, and the trust was funded with 9 million. That was ten years before he died, and at the time it was fair.

Ten years later the sons had grown the business to 30 million. The daughter's trust was still at 9 million, and she had spent a significant portion of the income. She felt cheated and sued her brothers. The case went to mediation and cost that family over a million dollars in legal fees. She received a small additional settlement.

The planning was sound. Her father's intention had been fair when he made it. What was missing was every conversation in the intervening decade."""))

# DAY 11 -- strip invented anecdotes
R.append((
"Responding is what a client does in a meeting where they have decided how much to give you. It is cooperative. It is polite. The answers are accurate as far as they go, and you will leave with a full page of notes. I have had two hour meetings where I got nothing but responses and did not notice until I tried to write the summary and found I could not say anything about that family I could not have said beforehand.",
"Responding is what a client does in a meeting where they have decided how much to give you. It is cooperative. It is polite. The answers are accurate as far as they go, and you will leave with a full page of notes and nothing you could not have written beforehand."))

R.append((
"""I have been guilty of this more times than I would like to write down. The tell is that the meeting felt efficient.

Efficient meetings with families are usually meetings where nobody told me anything.""",
"""The tell is that the meeting felt efficient.

An efficient meeting with a family is usually a meeting where nobody told you anything."""))

# DAY 12 -- strip invented anecdote, keep principle
R.append((
"The room does some of it. I have watched the same conversation go differently on a different side of a table.",
"The room does some of it. The same conversation runs differently across a desk than it does across a kitchen table, and the difference is not atmosphere."))

# DAY 15 -- replace invented anecdotes with Tom's own sourced story
R.append((
"""You cannot perform your way past this. I have seen advisors with immaculate technique whose families never gave them anything, and I have seen a man ask a clumsy question and get an honest answer because everyone in the room could tell he actually wanted to know.

So the question is not how to appear interested. It is whether you are.""",
"""You cannot perform your way past this, and I know that from the wrong side of it.

Years ago I was teaching a Sunday School class on financial stewardship while I was secretly struggling with credit card debt. I was saying all the right things and I was not living them. The weight of that hypocrisy was crushing. Eventually I told my wife. I am teaching what I am not practicing, I said. We made a plan and it took two years of sacrifice to get out.

Nobody in that class had audited my statements. What I remember is how heavy it was to stand in front of people and say true things that were not true of me.

So the question is not how to appear interested. It is whether you are."""))

# DAY 16 -- replace constructed illustration with the two brothers
R.append((
"Take a business worth twelve million. To the father who built it, that is not an asset. It is the proof that a decision he made at twenty-nine was correct, and it is the thing he will be remembered by. To the son who came in at twenty-four, it is a career, a set of relationships, and the reason he lives in a town he might not otherwise have chosen. To the daughter who did not join, it is the thing that had her father's attention. To the daughter-in-law, it is a source of risk that her household cannot diversify away from.",
"""I think of two brothers I worked with who inherited equal amounts from their father's estate, about 500,000 dollars each. Same amount, same source.

The first brother saw the inheritance as his father's final gift of love. He paid off his mortgage, set aside college funds for his kids, increased his giving to church and charity, and invested the rest conservatively. Dad worked hard for this money, he told me. I want to honor that sacrifice by using it wisely. Ten years later he is financially free, generous, and content.

The second brother saw it as his ticket to the good life. He quit his job, bought a boat and a sports car, and started living as though the money would never run out. Within three years it was gone, and he was bitter. That money ruined my life, he told me.

It was not the money that ruined his life. It was what he believed about the money."""))

# DAY 17 -- replace constructed mechanism with the sibling rivalry family
R.append((
"Now watch what happens next if nobody is running the room. The person who feels contradicted responds. The response is defensive, because they were not expecting to have to defend anything. The defensiveness is heard as escalation, so the first person hardens, and within ninety seconds a family that had a difference now has a conflict, and everyone will remember it as the day someone said something.",
"""One family I worked with struggled with exactly this. The oldest brother felt entitled to more because he had worked in the family business. The younger sister felt overlooked because she had moved away and pursued a different career. The middle child just wanted everyone to get along and avoided conflict at all costs.

Every conversation about the estate turned into a minefield. Old hurts resurfaced. Accusations flew, and the parents were heartbroken.

We brought in a skilled facilitator who helped them address the real issues beneath the surface. It was not about money. It was about feeling valued, respected, and loved. The oldest brother admitted he had used the business as a way to gain his father's approval. The younger sister confessed she had felt like the black sheep for choosing a different path. The middle child learned to stop playing peacemaker and start speaking truth."""))

# DAY 19 -- strip invented admission
R.append((
"You can get a family to agreement in an afternoon if you are skilled and they are tired. I have done it. The signatures are real",
"You can get a family to agreement in an afternoon if you are skilled and they are tired. The signatures are real"))

# DAY 20 -- strip invented frequency claim
R.append((
"Let us take a moment and make sure we understand what is being said, which I have used hundreds of times and which works because it gives everyone a legitimate reason to stop.",
"Let us take a moment and make sure we understand what is being said. It works because it gives everyone in the room a legitimate reason to stop."))

# DAY 23 -- replace invented anecdote with the Smith meeting setup
R.append((
"""That is what an unstated purpose costs you. Forty minutes of a defended room.""",
"""When I ran the first family meeting for a family who owned a dental practice, I opened by telling the four children exactly what the meeting was for. The objective is for your mom and dad to communicate to you what their hopes and dreams are, and to get your input on some decisions they need to make regarding the family, the business, and the estate plan. Then we set ground rules. Speak one at a time, listen respectfully, ask questions freely.

None of that is impressive. All of it is load bearing, because it replaced whatever those four adults had privately decided the meeting was about on the drive over."""))

# DAY 28 -- strip invented claim
R.append((
"It is fifteen conversations, and I have never met a family that had fifteen and came apart.",
"It is fifteen conversations, and a family that has had fifteen of them is a different family from the one that had one."))

# DAY 29 -- replace invented claim with sourced material
R.append((
"""I have watched families I would have described as harmonious come apart in eight months, and in every case the harmony was real. It just had not been tested, and nobody had thought to test it while it was cheap to do so.""",
"""Think about the father who divided his business between his sons and funded an equivalent trust for his daughter. On the day he did it, that family was harmonious and the arrangement was fair. Nobody objected, because nothing had happened yet that anyone could object to. Ten years of silence later it cost them a lawsuit and a million dollars in legal fees.

The harmony was real. It had simply never been tested, and nobody thought to test it while testing was still cheap."""))

applied, missed = 0, []
for old, new in R:
    if old in t:
        t = t.replace(old, new, 1); applied += 1
    else:
        missed.append(old[:70])

open(F, "w", encoding="utf-8").write(t)
print("applied:", applied, "of", len(R))
for m in missed: print("MISSED:", m)
