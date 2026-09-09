#!/usr/bin/env python3
import re, glob, os

OUT = "/mnt/user-data/outputs"
FILES = sorted(glob.glob(f"{OUT}/Book*_Family_All_Sessions.md"))

BUDGET = """## RUNTIME AND STORY BUDGET

**Target: 20 minutes per session.** At the series speaking rate of 186 words per minute that is about 3,700 finished words.

Script delivers roughly 1,800. That leaves an improv budget of about 1,900 words, which is **three stories at 450 to 550 words each.** Filmed sessions expanded 2.4x to 3.3x over script, so without a budget these land at 28 to 30 minutes.

**Three slots per session, positioned.**

| Slot | Position | Target |
| --- | --- | --- |
| STORY 1 | Open, before the teaching gets going | 450 to 550 words |
| STORY 2 | Mid, at the turn where the session gets hard | 450 to 550 words |
| STORY 3 | Close, landing the point | 450 to 550 words |

Slots are marked in the copy. A fourth story puts the session over. Dropping one lands it near 16 minutes, which is acceptable.

**Shoot the stories direct to camera as separate takes.** That makes them cuttable for length, reusable across both editions, and usable as standalone assets. It turns runtime from a scripting problem into an edit-room problem.

---
"""

def fix(path):
    t = open(path, encoding="utf-8").read()
    name = os.path.basename(path).split("_")[0]

    # 1. house convention for case studies
    t = t.replace("**SCENARIO ONE.**", "**CASE STUDY 1.**")
    t = t.replace("**SCENARIO TWO.**", "**CASE STUDY 2.**")

    # 2. insert runtime budget after the front-matter title block
    anchor = re.search(r"\*\*Curriculum subtitle:.*?\n", t)
    if anchor and "RUNTIME AND STORY BUDGET" not in t:
        i = anchor.end()
        t = t[:i] + "\n" + BUDGET + t[i:]

    # 3. per-session: relabel cues, insert missing slots, add a BRETT cue
    parts = re.split(r"(\n# 🎬 SESSION \d)", t)
    rebuilt = [parts[0]]
    for k in range(1, len(parts), 2):
        head, body = parts[k], parts[k + 1]

        # relabel existing TOM cues in order
        cues = list(re.finditer(r"`\[TOM: (.*?)\]`", body, re.S))
        labels = ["STORY 1 (OPEN)", "STORY 2 (MID)", "STORY 3 (CLOSE)"]
        for n, m in enumerate(reversed(cues)):
            idx = len(cues) - 1 - n
            lab = labels[idx] if idx < 3 else f"RESERVE {idx-2}"
            new = f"`[TOM — {lab}, 450 to 550 words: {m.group(1).strip()}]`"
            body = body[:m.start()] + new + body[m.end():]

        have = len(cues)
        # insert missing slots at safe anchors
        if have < 2:
            cs1 = body.find("**CASE STUDY 1.**")
            if cs1 > 0:
                lab = labels[have]
                slot = f"`[TOM — {lab}, 450 to 550 words: a family you have sat with that illustrates this. Bring a real one.]`\n\n"
                body = body[:cs1] + slot + body[cs1:]
                have += 1
        if have < 3:
            tw = body.find("**THIS WEEK.**")
            if tw > 0:
                lab = labels[have]
                slot = f"`[TOM — {lab}, 450 to 550 words: the story that lands this session. Bring a real one.]`\n\n"
                body = body[:tw] + slot + body[tw:]
                have += 1

        # add one BRETT cue before THIS WEEK if none present
        if "[BRETT" not in body:
            tw = body.find("**THIS WEEK.**")
            if tw > 0:
                slot = ("`[BRETT — optional, 200 to 300 words: your own story here if you have one "
                        "for this session. Keep it shorter than Tom's.]`\n\n")
                body = body[:tw] + slot + body[tw:]

        rebuilt += [head, body]

    t = "".join(rebuilt)
    open(path, "w", encoding="utf-8").write(t)

    tom = len(re.findall(r"\[TOM —", t)); br = len(re.findall(r"\[BRETT —", t))
    cs = len(re.findall(r"\*\*CASE STUDY", t))
    print(f"{name:8} TOM slots: {tom:3}   BRETT slots: {br:2}   case studies: {cs:2}")

for f in FILES:
    fix(f)
