F = "/mnt/user-data/outputs/Communication_30Days_5_Days02-30.md"
t = open(F, encoding="utf-8").read()
R = []

# ---- Soften remaining unsourced experiential claims to sourced or neutral framing ----
R.append((
"I have come to think of this as the most solvable barrier in the set, and the most consistently unaddressed. You can hand a family an opening. Almost nobody does.",
"Of the four, this is the most solvable and the most consistently unaddressed. You can hand a family an opening. Almost nobody does."))

R.append((
"The families I have watched come apart were rarely the ones who refused this conversation.",
"The families who come apart are rarely the ones who refused this conversation."))

R.append((
"That family is not unusual. I would say it is the most common situation I encounter, and the parents in it are almost always people who did the harder part well.",
"That family is not unusual. The parents in it are almost always people who did the harder part well."))

R.append((
"I have found that advisors believe they are already doing this, and mostly they are not, and the reason is that",
"Most advisors believe they are already doing this, and mostly they are not, and the reason is that"))

R.append((
"I have watched advisors miss this for entire careers, and the reason is straightforward.",
"This is easy to miss for an entire career, and the reason is straightforward."))

R.append((
"I have come to think pace is the most underrated instrument an advisor has, and the reason is that it is invisible.",
"Pace is the most underrated instrument an advisor has, and the reason is that it is invisible."))

R.append((
"I have watched that pattern hold in family after family, and it still surprises the families every time, so let me say plainly what is going on.",
"That pattern holds in family after family, and it still surprises the families every time, so let me say plainly what is going on."))

# ---- DAY 25: add the Smith family meeting, sourced ----
R.append((
"""But a forced outcome in a family conversation is worse than no outcome, because it is a real decision made by people who had not finished understanding each other, and it will be relitigated at exactly the worst moment.""",
"""But a forced outcome in a family conversation is worse than no outcome, because it is a real decision made by people who had not finished understanding each other, and it will be relitigated at exactly the worst moment.

Here is what watching the room actually buys you. In the dental practice family, the invisible elephant was the practice itself, which was the most valuable asset on their balance sheet and the thing nobody would name. That meeting included tears and raised voices. On a scale of one to ten it began at a five with the initial tension, dropped to a three as the frustrations came out, and ended at an eight.

It ended at an eight because the elephant became visible and the underlying issues got addressed. If I had been managing that room toward an outcome, I would have intervened at the three."""))

# ---- DAY 30: add the grandfather story, sourced ----
R.append((
"""John 13:34 is a strange verse to call new, and Jesus calls it new anyway, because the standard has changed. Not love one another well, or love one another as you love yourself. As I have loved you.""",
"""I want to leave you with one thing I did once that I would do again in every family I serve.

I worked with a family where the first generation was 92, the second was 65, and the third were in their thirties and forties. The grandmother had dementia, and her husband cared for her all the way to the end. She died at 91, and I went to her funeral. Her son stood up and told a wonderful story about her.

Sitting there I thought, grandpa is still over there and he is still alive.

So I met with every one of the grandchildren and gave them an outline of what to think about. Each of them wrote a two page paper about their grandfather. Then we held a family meeting, and he had no idea it was coming. One at a time they stood in front of his chair and read out loud what they had written about him.

There was not a dry eye in the place.

They could have gotten up at the funeral and said the same words. It meant something entirely different that they said it to him.

John 13:34 is a strange verse to call new, and Jesus calls it new anyway, because the standard has changed. Not love one another well, or love one another as you love yourself. As I have loved you."""))

applied, missed = 0, []
for old, new in R:
    if old in t:
        t = t.replace(old, new, 1); applied += 1
    else:
        missed.append(old[:70])
open(F, "w", encoding="utf-8").write(t)
print("applied:", applied, "of", len(R))
for m in missed: print("MISSED:", m)
