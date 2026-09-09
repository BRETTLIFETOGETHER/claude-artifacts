import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

NAVY = "12253F"
GOLD = "B08B3F"
CREAM = "FAF7F0"
LINE = "D8D0C2"

wb = openpyxl.Workbook()

thin = Side(style="thin", color=LINE)
border = Border(left=thin, right=thin, top=thin, bottom=thin)

def header_row(ws, row, headers, widths):
    for i, (h, w) in enumerate(zip(headers, widths), start=1):
        c = ws.cell(row=row, column=i, value=h)
        c.font = Font(name="Arial", size=10, bold=True, color="FFFFFF")
        c.fill = PatternFill("solid", fgColor=NAVY)
        c.alignment = Alignment(vertical="center", horizontal="left", wrap_text=True)
        c.border = border
        ws.column_dimensions[get_column_letter(i)].width = w
    ws.row_dimensions[row].height = 34

# ─────────────────────────────  SHEET 1  ─────────────────────────────
ws = wb.active
ws.title = "Influencer Roster"

ws["A1"] = "VISIONARY GENEROSITY — INFLUENCER ROSTER"
ws["A1"].font = Font(name="Arial", size=15, bold=True, color=NAVY)
ws["A2"] = ("Casting and sourcing table for the book, the workshop, and the endorsement strategy. "
            "Vision and Obedience scores are editorial judgments about what each figure DEMONSTRATES for teaching purposes — "
            "they are not assessments of the people. Scale 1–5. Status: Aug 2026.")
ws["A2"].font = Font(name="Arial", size=9, italic=True, color="6E6A62")
ws.merge_cells("A2:L2")
ws.row_dimensions[2].height = 28
ws["A3"] = "EDIT THESE COLUMNS AS YOU WORK: H (Story status) · I (Permission path) · K (Contact route) · L (Notes)"
ws["A3"].font = Font(name="Arial", size=9, bold=True, color=GOLD)

headers = ["Name", "Type", "Dominant engine", "Vision (1-5)", "Obedience (1-5)",
           "What they demonstrate", "Anchor chapter(s)", "Story status",
           "Permission path", "Endorsement", "Contact route", "Notes"]
widths = [26, 15, 15, 9, 10, 46, 15, 20, 24, 14, 22, 30]
header_row(ws, 5, headers, widths)

rows = [
    # BOTH ENGINES
    ["Alan & Katherine Barnhart", "Living family", "Both", 5, 5,
     "Two-year Scripture study before any decision; income capped in year one; give half / reinvest half; company into a charitable trust in 2007",
     "3, 7, 11, 12", "Documented public", "NCF + Generous Giving", "High", "Via NCF", "The book's spine story. Appears in 4+ chapters."],
    ["David & Barbara Green", "Living family", "Both", 5, 5,
     "Vision for Scripture access at global scale; ownership moved into a mission-oriented trust the family cannot reach",
     "8, 10, 15", "Documented public", "Zondervan + Bill High", "Medium", "Via Bill High", "Book excerpt permissions run through Zondervan."],
    ["R.G. LeTourneau", "Mid-century", "Both", 4, 5,
     "Pledged from underneath a six-figure loss; climbed by increments to a reversed tithe — 90% given, 10% kept",
     "4, 7, 10", "Public domain", "None needed", "Deceased", "n/a", "Best evidence that the extreme cases arrived incrementally."],
    ["Stanley Tam", "Mid-century", "Both", 4, 5,
     "Made God the legal owner of his company in 1936 and became its employee; well over $100M eventually to missions",
     "8, 10", "Widely published", "Standard attribution", "Deceased", "n/a", "Category-defining owner-transfer story; predates the modern movement."],
    ["Bob Buford", "Mid-century", "Both", 5, 4,
     "Organized the second half of life around the hundredfold; funded leaders rather than programs",
     "2, 7, 9", "Widely published", "Leadership Network est.", "Deceased", "n/a", "Brett's own 25-year mentor — the strongest personal claim to this material."],
    ["S. Truett Cathy", "Mid-century", "Both", 4, 4,
     "Vision expressed through people; the closed Sunday as obedience that cost real money weekly",
     "6, 16", "Widely published", "Chick-fil-A / family", "Deceased", "Family foundation", "Already in the 40 Days of Generosity lineage."],
    ["The Maclellan family", "Movement", "Both", 5, 4,
     "Three generations of vision; funded Generous Giving privately so it would never have to ask",
     "13, 14", "Documented public", "Maclellan Foundation", "High", "Via Generous Giving", "Obedience expressed structurally — the no-ask endowment."],
    ["Selina, Countess of Huntingdon", "Historical", "Both", 5, 4,
     "Could not preach, so filled a drawing room with aristocracy who would never stand in a field to hear Whitefield",
     "8, 12", "Public domain", "None needed", "Deceased", "n/a", "The best 'vision is given, not generated' story in the book."],
    ["Humphrey Monmouth", "Historical", "Both", 5, 5,
     "Funded and housed Tyndale, moved printed New Testaments on his merchant ships, served a year in the Tower for it",
     "2, 10", "Public domain", "None needed", "Deceased", "n/a", "Rinehart owns this lane — differentiate or credit clearly."],
    # VISION-DOMINANT
    ["Rick Warren", "Author/leader", "Vision", 5, 3,
     "Enlarged what a congregation believed was at stake; giving followed the vision rather than the appeal",
     "6", "Published material only", "Direct permission req'd", "Medium", "Direct / agent", "Use published work only. No reconstructed quotes."],
    ["Steve French", "Author", "Vision", 5, 4,
     "Family vision spanning generations; giving reframed as investment at a return no market offers",
     "1, 13, 16", "Podcast + Signatry", "Internal", "Author", "Direct", "Exit-regret story needs his confirmation before use."],
    ["Bill High", "Movement", "Vision", 5, 3,
     "Built the institution, then made the founder stories transferable through writing",
     "8, 15", "Documented public", "Direct", "High", "Direct", "Signatry founder; also the Green co-author and the bridge to Zondervan."],
    ["Daryl Heald", "Movement", "Vision", 5, 3,
     "Carried the Journey of Generosity to ~100,000 people across 90 countries and 40 languages",
     "18 (Exp.) / global", "Documented public", "Generosity Path", "High", "Via Maclellan", "The global chapter is his. Also a Generous Giving co-founder."],
    ["John Thornton", "Historical", "Vision", 5, 3,
     "Placed Newton in an influential pulpit, gave counsel and rest, pressed him to publish the hymns",
     "9, 12", "Public domain", "None needed", "Deceased", "n/a", "The 'back the person, not the project' anchor."],
    ["Josh Kwan", "Movement", "Vision", 4, 3,
     "Convening as a vision instrument — a table of peers raises what any individual believes is possible",
     "14 (collab.)", "Needs sourcing", "Direct", "High", "Via The Gathering", "Needs a specific, permissioned story rather than a general reference."],
    ["Peter Greer", "Author/leader", "Vision", 4, 3,
     "A gift can compound economically rather than simply being spent",
     "7 (Exp.)", "Published material", "Direct", "High", "Via HOPE Intl", "Also the sharpest available voice on the spiritual danger of doing good."],
    ["Henry Kaestner", "Movement", "Vision", 4, 3,
     "Built the channel where faith-driven entrepreneurs encounter this; pushes past giving toward gospel transformation",
     "6, 14", "Documented public", "Direct", "High", "Faith Driven", "Strong distribution ally as well as an endorser."],
    ["David Wills", "Movement", "Vision", 4, 3,
     "A career at NCF explaining what asset-level vision makes possible",
     "5, 13", "Documented public", "Via NCF", "High", "Via NCF", "President Emeritus; also the gatekeeper relationship for Barnhart material."],
    # OBEDIENCE-DOMINANT
    ["George Müller", "Historical", "Obedience", 3, 5,
     "Orphanages funded without a single appeal; records kept precisely so the claim could be tested",
     "10 (Exp.)", "Public domain", "None needed", "Deceased", "n/a", "The paradigm case. Underused in this category."],
    ["Hudson Taylor", "Historical", "Obedience", 3, 5,
     "A mission built on the same conviction at greater personal cost",
     "10 (Exp.)", "Public domain", "None needed", "Deceased", "n/a", "Pairs with Müller; do not use both in the same chapter."],
    ["April & Craig Chapman", "Living family", "Obedience", 4, 5,
     "Two engineers, two windfalls, and a decision to give away half of what they earned; the keep question rather than the give question",
     "3, 19 (Exp.)", "Podcast, documented", "Direct + Generous Giving", "High", "Direct", "First choice for the foreword. Competitor and ally simultaneously."],
    ["Todd Harper", "Movement", "Obedience", 3, 5,
     "Two decades arguing the giver is the primary beneficiary, in rooms where nobody is permitted to ask",
     "13, 19 (Exp.)", "Documented public", "Generous Giving", "High", "Via Generous Giving", "Co-founder. Essential to the no-ask discipline the book borrows."],
    ["Brent Haverkamp", "Living family", "Obedience", 3, 5,
     "Gave one property before selling it rather than selling two to cover the gift and the tax",
     "13", "Signatry published", "Internal — a phone call", "Low", "Via Signatry", "The single page advisors will photocopy."],
    ["David & Casey Trogden", "Living family", "Obedience", 3, 4,
     "Began with used medical equipment bound for Haiti; grew into private stock gifted ahead of a sale",
     "5, 13", "Signatry published", "Internal — a phone call", "Low", "Via Signatry", "Best proof that asset giving starts small and physical."],
    ["Sean & Angela Kouplen", "Living family", "Obedience", 3, 4,
     "Generosity running through the business itself rather than alongside it",
     "12 (Exp.)", "Signatry published", "Internal — a phone call", "Low", "Via Signatry", "Useful for the business-engine chapter."],
]

r = 6
for row in rows:
    for i, v in enumerate(row, start=1):
        c = ws.cell(row=r, column=i, value=v)
        c.font = Font(name="Arial", size=10)
        c.alignment = Alignment(vertical="top", wrap_text=(i in (6, 12)))
        c.border = border
        if i in (4, 5):
            c.alignment = Alignment(vertical="top", horizontal="center")
        if i == 3:
            fill = {"Both": "E8EEF6", "Vision": "FAF3E4", "Obedience": "EFF3EC"}[v]
            c.fill = PatternFill("solid", fgColor=fill)
    ws.row_dimensions[r].height = 44
    r += 1

# totals
tr = r + 1
ws.cell(row=tr, column=1, value="TOTALS").font = Font(name="Arial", size=10, bold=True, color=NAVY)
ws.cell(row=tr, column=4, value=f"=ROUND(AVERAGE(D6:D{r-1}),2)").font = Font(name="Arial", size=10, bold=True)
ws.cell(row=tr, column=5, value=f"=ROUND(AVERAGE(E6:E{r-1}),2)").font = Font(name="Arial", size=10, bold=True)
ws.cell(row=tr, column=6, value=f"=COUNTA(A6:A{r-1})&\" figures on the roster\"").font = Font(name="Arial", size=10, bold=True)
ws.freeze_panes = "A6"
ws.auto_filter.ref = f"A5:L{r-1}"

# ─────────────────────────────  SHEET 2  ─────────────────────────────
gs = wb.create_sheet("Gap Analysis")
gs["A1"] = "WHERE THE ROSTER IS THIN"
gs["A1"].font = Font(name="Arial", size=15, bold=True, color=NAVY)
gs["A2"] = ("The roster is strong and lopsided. These counts pull live from the roster sheet. "
            "The book's cover claims generosity is available to anyone; the current cast proves something narrower.")
gs["A2"].font = Font(name="Arial", size=9, italic=True, color="6E6A62")
gs.merge_cells("A2:E2")

header_row(gs, 4, ["Dimension", "Count", "Share", "The problem this creates", "Recommended fix"], [30, 10, 10, 52, 46])

n = len(rows)
gaps = [
    ["Both engines", f'=COUNTIF(\'Influencer Roster\'!C6:C{r-1},"Both")', None,
     "Only these carry the book's full thesis. Everything else illustrates half of it.",
     "Protect these nine. Do not dilute them across too many chapters."],
    ["Vision-dominant", f'=COUNTIF(\'Influencer Roster\'!C6:C{r-1},"Vision")', None,
     "Well covered. Skews toward movement leaders rather than families.",
     "Fine as is."],
    ["Obedience-dominant", f'=COUNTIF(\'Influencer Roster\'!C6:C{r-1},"Obedience")', None,
     "Thinnest group, and three of them are Signatry families — a house-book risk.",
     "Add two obedience stories from outside the Signatry orbit."],
    ["Living families", f'=COUNTIF(\'Influencer Roster\'!B6:B{r-1},"Living family")', None,
     "These carry the contemporary credibility. Every one is a US household with assets.",
     "Source three at ordinary income levels."],
    ["Historical", f'=COUNTIF(\'Influencer Roster\'!B6:B{r-1},"Historical")', None,
     "Five figures — and three of them are the exact three in Gospel Patrons.",
     "Credit Rinehart openly; add one patron he does not use."],
    ["Movement leaders", f'=COUNTIF(\'Influencer Roster\'!B6:B{r-1},"Movement")', None,
     "Strong for endorsements, weak as narrative — leaders explain, families demonstrate.",
     "Use these for blurbs, not for anchor stories."],
]
gr = 5
for g in gaps:
    gs.cell(row=gr, column=1, value=g[0]).font = Font(name="Arial", size=10, bold=True)
    gs.cell(row=gr, column=2, value=g[1]).font = Font(name="Arial", size=10)
    gs.cell(row=gr, column=3, value=f"=ROUND(B{gr}/{n}*100,0)&\"%\"").font = Font(name="Arial", size=10)
    gs.cell(row=gr, column=4, value=g[3]).font = Font(name="Arial", size=10)
    gs.cell(row=gr, column=5, value=g[4]).font = Font(name="Arial", size=10)
    for col in range(1, 6):
        cc = gs.cell(row=gr, column=col)
        cc.alignment = Alignment(vertical="top", wrap_text=True)
        cc.border = border
    gs.row_dimensions[gr].height = 34
    gr += 1

gr += 1
gs.cell(row=gr, column=1, value="THE FOUR GAPS THAT MATTER").font = Font(name="Arial", size=12, bold=True, color=GOLD)
gr += 1
named = [
    ["Geography", "Twenty-three of twenty-five are American or British. The book argues this is a work of the Spirit rather than a byproduct of American surplus — the cast currently argues the opposite.",
     "Two stories from outside the US/UK. Heald's network is the fastest route to both."],
    ["Income level", "Almost every living figure is a business owner or an heir. A reader at ordinary income will conclude, correctly, that the book was not written for him.",
     "Three ordinary-income stories, one placed no later than chapter 2."],
    ["Gender", "Huntingdon and the Luke 8 women aside, the roster is men and 'and-wife' pairings. Katherine Barnhart and April Chapman are named participants, not supporting characters.",
     "Interview the wives directly. Give at least two women a story in their own right."],
    ["Source concentration", "Six figures come through The Signatry and four through NCF/Generous Giving. Concentration makes this read as a house book to anyone paying attention.",
     "Cap Signatry-sourced anchors at four; seek two anchors with no institutional tie."],
]
for nm in named:
    gs.cell(row=gr, column=1, value=nm[0]).font = Font(name="Arial", size=10, bold=True, color=NAVY)
    gs.cell(row=gr, column=2, value=nm[1]).font = Font(name="Arial", size=10)
    gs.merge_cells(start_row=gr, start_column=2, end_row=gr, end_column=4)
    gs.cell(row=gr, column=5, value=nm[2]).font = Font(name="Arial", size=10, italic=True)
    for col in range(1, 6):
        cc = gs.cell(row=gr, column=col)
        cc.alignment = Alignment(vertical="top", wrap_text=True)
        cc.border = border
    gs.row_dimensions[gr].height = 52
    gr += 1

wb.save("/mnt/user-data/outputs/Generosity-Influencer-Roster.xlsx")
print("saved")
