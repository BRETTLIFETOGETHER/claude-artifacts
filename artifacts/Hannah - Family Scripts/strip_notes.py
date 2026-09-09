#!/usr/bin/env python3
import re, os

OUT = "/mnt/user-data/outputs"

BOOKS = {
 "Book1_Overview": ("BOOK 1 — OVERVIEW", "Family Legacy by Design",
   "Leading Your Family from Legacy by Default to Legacy by Design"),
 "Book2_Clarity": ("BOOK 2 — CLARITY", "What Will You Do With What You've Been Given?",
   "Discovering Your Family's Values, Purpose, and Direction"),
 "Book3_Alignment": ("BOOK 3 — ALIGNMENT", "Getting on the Same Page as a Family",
   "Aligning Your Values, Decisions, and Direction Around What Matters Most"),
 "Book4_Communication": ("BOOK 4 — COMMUNICATION", "Conversations That Matter",
   "Why Families Don't Talk\u2014and How to Start"),
 "Book5_Meetings": ("BOOK 5 — MEETINGS", "Family Meetings That Bring You Together",
   "Creating a Space for Honest Conversations, Alignment, and Growth"),
 "Book6_NextGen": ("BOOK 6 — NEXT GENERATION", "Raising the Next Generation",
   "Helping Your Children Grow in Wisdom, Purpose, and Responsibility"),
}

# H2 sections to delete entirely (through to the next H1 or H2)
KILL = ["RUNTIME AND STORY BUDGET", "SESSION TITLES", "THE STRUCTURAL DIFFERENCE",
        "THE BOUNDARY", "DEFAULTS SET FOR THIS BUILD", "STORY CUES",
        "BUILD NOTES", "FLAGGED IN THIS BUILD"]

for stem, (bookline, title, subtitle) in BOOKS.items():
    src = f"{OUT}/{stem}_Family_All_Sessions.md"
    t = open(src, encoding="utf-8").read()

    # cut everything before the first session, rebuild the header
    first = t.find("# 🎬 SESSION 1")
    header = (f"# FAMILY FOUNDATION SERIES\n\n## {bookline}\n\n"
              f"# {title}\n\n### {subtitle}\n\n")
    t = header + t[first:]

    # drop killed H2 sections wherever they still appear
    for k in KILL:
        t = re.sub(rf"\n## {re.escape(k)}.*?(?=\n#[^#]|\n## |\Z)", "\n", t, flags=re.S)

    # drop source attribution lines under session headers
    t = re.sub(r"\n\*Source:[^\n]*\n", "\n", t)

    # drop internal blockquotes (DECISION / NOTE / attribution), keep Scripture
    t = re.sub(r"\n> \*\*(DECISION|NOTE|Attribution note)[^\n]*(\n>[^\n]*)*", "", t)

    # drop alternate case study blocks
    t = re.sub(r"\n\*\*ALTERNATE CASE STUDIES\.\*\*.*?(?=\n\*\*THIS WEEK)", "\n", t, flags=re.S)

    # tidy whitespace
    t = re.sub(r"\n{3,}", "\n\n", t).strip() + "\n"

    dst = f"{OUT}/SCRIPT_{stem}.md"
    open(dst, "w", encoding="utf-8").write(t)

    sess = len(re.findall(r"^# 🎬 SESSION", t, re.M))
    scrip = len(re.findall(r"^> \*\*Scripture", t, re.M))
    tom = len(re.findall(r"\[TOM —", t)); br = len(re.findall(r"\[BRETT —", t))
    cs = len(re.findall(r"\*\*CASE STUDY", t)); wk = len(re.findall(r"\*\*THIS WEEK", t))
    print(f"{stem:22} {len(t.split()):5}w  sessions {sess}  scripture {scrip}  "
          f"TOM {tom}  BRETT {br}  case {cs}  week {wk}")
