import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

wb = openpyxl.Workbook()

ARIAL = "Arial"
BLUE = Font(name=ARIAL, size=10, color="0000FF")
BLUEB = Font(name=ARIAL, size=10, color="0000FF", bold=True)
BLACK = Font(name=ARIAL, size=10)
BLACKB = Font(name=ARIAL, size=10, bold=True)
GREEN = Font(name=ARIAL, size=10, color="008000")
WHITEB = Font(name=ARIAL, size=10, bold=True, color="FFFFFF")
TITLE = Font(name=ARIAL, size=14, bold=True, color="1F3864")
SUB = Font(name=ARIAL, size=10, italic=True, color="595959")
HDRFILL = PatternFill("solid", fgColor="1F3864")
SECFILL = PatternFill("solid", fgColor="D9E2F3")
YELLOW = PatternFill("solid", fgColor="FFFF00")
GREYFILL = PatternFill("solid", fgColor="F2F2F2")
thin = Side(style="thin", color="BFBFBF")
BOX = Border(left=thin, right=thin, top=thin, bottom=thin)

CUR = '$#,##0.00;($#,##0.00);-'
CUR0 = '$#,##0;($#,##0);-'
PCT = '0.0%;(0.0%);-'
NUM = '#,##0;(#,##0);-'

def hdr(ws, row, labels, widths=None):
    for i, l in enumerate(labels, start=1):
        c = ws.cell(row=row, column=i, value=l)
        c.font = WHITEB; c.fill = HDRFILL; c.border = BOX
        c.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
    ws.row_dimensions[row].height = 30
    if widths:
        for i, w in enumerate(widths, start=1):
            ws.column_dimensions[get_column_letter(i)].width = w

def sect(ws, row, text, span):
    c = ws.cell(row=row, column=1, value=text)
    c.font = Font(name=ARIAL, size=10, bold=True, color="1F3864"); c.fill = SECFILL
    for i in range(2, span+1):
        ws.cell(row=row, column=i).fill = SECFILL
    return row

def titleblock(ws, t, s):
    ws["A1"] = t; ws["A1"].font = TITLE
    ws["A2"] = s; ws["A2"].font = SUB
    ws.row_dimensions[1].height = 20

# ==========================================================
# TAB 1 — README & ASSUMPTIONS
# ==========================================================
ws = wb.active
ws.title = "Assumptions"
titleblock(ws, "RBI Pricing & Packaging Model — Master Assumptions",
           "Straw-man built Aug 2026 from RBI Campaign Pro-Forma (Year 1) + RBI Master Production Schedule. Status: PROPOSED — not approved.")

ws.column_dimensions["A"].width = 46
ws.column_dimensions["B"].width = 16
ws.column_dimensions["C"].width = 14
ws.column_dimensions["D"].width = 62

r = 4
ws.cell(row=r, column=1, value="HOW TO USE THIS FILE").font = BLACKB
r += 1
legend = [
    ("BLUE cells", "You edit these. Every input and lever lives here or on this tab."),
    ("BLACK cells", "Formulas. Do not overwrite."),
    ("GREEN cells", "Pulled from another tab in this workbook."),
    ("YELLOW fill", "Open question — needs a real quote or a decision before the pro forma is credible."),
]
for a, b in legend:
    ws.cell(row=r, column=1, value=a).font = BLACKB
    ws.cell(row=r, column=4, value=b).font = BLACK
    r += 1

r += 1
sect(ws, r, "1. PRINT / MANUFACTURING COST — needs Raj quote", 4); r += 1
hdr(ws, r, ["Assumption", "Value", "Unit", "Basis / note"]); r += 1
print_a = [
    ("Trade paperback, ~208pp, 5.5x8.5, 4c cover", 3.10, "$/unit", "Straw-man at 10K run. Pro forma used $5.00 blended. CONFIRM WITH RAJ."),
    ("Devotional, ~176pp, 5.5x8.5, 4c cover", 2.85, "$/unit", "40-day format. CONFIRM WITH RAJ."),
    ("Participant Guide, ~128pp, 7x9, 4c cover", 2.60, "$/unit", "6-session workbook w/ fill-in space. CONFIRM WITH RAJ."),
    ("Leader Guide, ~64pp, 7x9", 1.75, "$/unit", "CONFIRM WITH RAJ."),
    ("Campaign Handbook, ~96pp, 7x9", 2.20, "$/unit", "Pastor/church planning piece."),
    ("Children's Leader Kit (print + components)", 9.50, "$/unit", "Includes activity masters, poster, cards. Rough."),
    ("Freight-in from printer (allocated)", 0.22, "$/unit", "Printer to Raj's warehouse, per unit."),
    ("Print overrun / spoilage reserve", 0.03, "% of print", "3% standard."),
]
first_print = r
for a, v, u, n in print_a:
    ws.cell(row=r, column=1, value=a).font = BLACK
    c = ws.cell(row=r, column=2, value=v); c.font = BLUE; c.fill = YELLOW
    c.number_format = PCT if u == "% of print" else CUR
    ws.cell(row=r, column=3, value=u).font = BLACK
    ws.cell(row=r, column=4, value=n).font = SUB
    r += 1

r += 1
sect(ws, r, "2. FULFILLMENT / 3PL — every line item to get priced on the Raj call", 4); r += 1
hdr(ws, r, ["Assumption", "Value", "Unit", "Basis / note"]); r += 1
ff_a = [
    ("Inbound receiving", 35.00, "$/pallet", "ASK RAJ. Often billed per pallet or per carton — get both."),
    ("Storage", 22.00, "$/pallet/mo", "ASK RAJ. Campaign inventory sits 4-9 months. This is the silent killer."),
    ("Kitting / assembly labor", 2.25, "$/kit", "ASK RAJ. Pre-built at receipt is far cheaper than build-on-demand."),
    ("Pick fee — first unit in order", 2.75, "$/order", "ASK RAJ."),
    ("Pick fee — each additional unit", 0.45, "$/unit", "ASK RAJ."),
    ("Corrugate / carton", 1.85, "$/order", "ASK RAJ. Branded box is an upcharge — get it separately."),
    ("Dunnage / void fill", 0.40, "$/order", "ASK RAJ."),
    ("Label + documentation", 0.35, "$/order", "ASK RAJ."),
    ("Order transaction / admin fee", 1.25, "$/order", "ASK RAJ. Often hidden."),
    ("Outbound freight rate", 1.60, "$/lb", "ASK RAJ. Negotiated ground, avg zone 5."),
    ("Outbound freight minimum", 12.00, "$/order", "ASK RAJ."),
    ("Returns processing", 4.50, "$/return", "ASK RAJ."),
    ("Monthly account / WMS minimum", 250.00, "$/month", "ASK RAJ. Spread across volume; excluded from unit math below."),
    ("Assumed return rate — direct channel", 0.02, "% of units", "Direct-to-church is low-return."),
    ("Assumed return rate — trade channel", 0.20, "% of units", "Christian trade is fully returnable. Industry norm 15-25%."),
]
first_ff = r
for a, v, u, n in ff_a:
    ws.cell(row=r, column=1, value=a).font = BLACK
    c = ws.cell(row=r, column=2, value=v); c.font = BLUE; c.fill = YELLOW
    c.number_format = PCT if "%" in u else CUR
    ws.cell(row=r, column=3, value=u).font = BLACK
    ws.cell(row=r, column=4, value=n).font = SUB
    r += 1

r += 1
sect(ws, r, "3. CHANNEL DISCOUNT — what you actually collect on a $19 book", 4); r += 1
hdr(ws, r, ["Channel", "Net % of retail", "Mix %", "Basis / note"]); r += 1
ch_a = [
    ("Direct to church / RBI store", 1.00, 0.45, "Full retail. RBI pays fulfillment. Highest margin, hardest to build."),
    ("Church bulk order (25% qty discount)", 0.75, 0.25, "Campaign orders of 25+ units."),
    ("Christian trade (Christianbook, Lifeway)", 0.45, 0.20, "50-55% discount, returnable, freight on us."),
    ("Amazon / mass", 0.55, 0.10, "Varies by term. Non-returnable if sold on FBA vendor terms."),
]
first_ch = r
for a, v, m, n in ch_a:
    ws.cell(row=r, column=1, value=a).font = BLACK
    c = ws.cell(row=r, column=2, value=v); c.font = BLUE; c.number_format = PCT
    c2 = ws.cell(row=r, column=3, value=m); c2.font = BLUE; c2.number_format = PCT; c2.fill = YELLOW
    ws.cell(row=r, column=4, value=n).font = SUB
    r += 1
mix_row = r
ws.cell(row=r, column=1, value="Weighted net realization / Mix check").font = BLACKB
c = ws.cell(row=r, column=2, value=f"=SUMPRODUCT(B{first_ch}:B{first_ch+3},C{first_ch}:C{first_ch+3})/C{r}")
c.font = BLACKB; c.number_format = PCT
c2 = ws.cell(row=r, column=3, value=f"=SUM(C{first_ch}:C{first_ch+3})"); c2.font = BLACKB; c2.number_format = PCT
ws.cell(row=r, column=4, value="Mix must total 100%. The current pro forma implicitly assumes 100% direct at full retail.").font = SUB
r += 2

sect(ws, r, "4. OTHER ECONOMICS", 4); r += 1
hdr(ws, r, ["Assumption", "Value", "Unit", "Basis / note"]); r += 1
oth_a = [
    ("Author / RBI royalty on net receipts", 0.14, "%", "Set to 0 if royalty is inside the 50/50 profit share instead. DECIDE."),
    ("Marketing allocation", 0.10, "% of revenue", "Pro forma used 10%. Kept."),
    ("Merchant / payment processing", 0.029, "% of revenue", "2.9% + $0.30 typical Shopify/Stripe."),
    ("Target gross margin — individual SKUs", 0.55, "%", "Post-COGS, pre-fulfillment."),
    ("Target contribution margin — kits", 0.45, "%", "Post-COGS AND post-fulfillment. The number that matters."),
]
first_oth = r
for a, v, u, n in oth_a:
    ws.cell(row=r, column=1, value=a).font = BLACK
    c = ws.cell(row=r, column=2, value=v); c.font = BLUE; c.number_format = PCT
    ws.cell(row=r, column=3, value=u).font = BLACK
    ws.cell(row=r, column=4, value=n).font = SUB
    r += 1

# named refs for use elsewhere
A = {}
for i,(a,v,u,n) in enumerate(print_a): A["p"+str(i)] = f"Assumptions!$B${first_print+i}"
for i,(a,v,u,n) in enumerate(ff_a):    A["f"+str(i)] = f"Assumptions!$B${first_ff+i}"
for i,(a,v,u,n) in enumerate(oth_a):   A["o"+str(i)] = f"Assumptions!$B${first_oth+i}"
A["netreal"] = f"Assumptions!$B${mix_row}"

# ==========================================================
# TAB 2 — SKU MASTER
# ==========================================================
ws = wb.create_sheet("SKU Master")
titleblock(ws, "SKU Master — Every Item Sold Individually",
           "One row per sellable unit. Multiply across 6 campaign titles (GOIA, MYM, GL, Splitting Heirs, This Changes Everything, How Much Is Enough) = the full SKU count Raj must quote.")

cols = ["SKU Code", "Product", "Audience", "Format", "Pages",
        "Retail Price", "Print Cost", "Freight-In", "Landed COGS",
        "Gross Margin $", "Gross Margin %", "Ship Wt (lb)", "Notes"]
w = [14, 30, 12, 14, 8, 12, 11, 10, 12, 13, 12, 11, 40]
hdr(ws, 4, cols, w)

skus = [
    ("XX-BK-01", "Trade Book", "Adult", "Paperback", 208, 18.99, 0, 0.75, "Core trade title. Anchor of the personal kit."),
    ("XX-DV-01", "40-Day Devotional", "Adult", "Paperback", 176, 16.99, 1, 0.65, "Campaign engine. Highest churchwide volume."),
    ("XX-PG-01", "Participant Guide (6 sessions)", "Adult", "Workbook", 128, 17.99, 2, 0.55, "Includes streaming access code. The group unit."),
    ("XX-LG-01", "Leader Guide", "Adult", "Workbook", 64, 12.99, 3, 0.30, "Sold in group kit; rarely bought alone by a member."),
    ("XX-SD-01", "Student Devotional", "Student", "Paperback", 144, 14.99, 1, 0.55, "Youth edition, 40-day."),
    ("XX-SP-01", "Student Participant Guide", "Student", "Workbook", 112, 15.99, 2, 0.50, "6-session youth small group."),
    ("XX-SL-01", "Student Leader Guide", "Student", "Workbook", 64, 12.99, 3, 0.30, "Youth pastor facing."),
    ("XX-CK-01", "Children's Leader Kit", "Children", "Boxed", 0, 39.99, 5, 2.00, "Print + activity components. Phase 2 per schedule."),
    ("XX-CH-01", "Church Campaign Handbook", "Pastor", "Paperback", 96, 24.99, 4, 0.45, "Sermon outlines, 6-week plan, launch checklist."),
    ("XX-VD-01", "Video Series — Group License", "Group", "Digital", 0, 49.00, -1, 0.00, "One small group, one campaign. Zero COGS."),
    ("XX-VC-01", "Video Series — Church License", "Church", "Digital", 0, 199.00, -1, 0.00, "Unlimited groups, one campaign. Zero COGS."),
    ("XX-PR-01", "Promo Asset Pack", "Church", "Digital", 0, 49.00, -1, 0.00, "Logos, bumpers, invite cards, social. Zero COGS."),
]

r0 = 5
r = r0
for code, prod, aud, fmt, pages, retail, pidx, wt, note in skus:
    ws.cell(row=r, column=1, value=code).font = BLACK
    ws.cell(row=r, column=2, value=prod).font = BLACK
    ws.cell(row=r, column=3, value=aud).font = BLACK
    ws.cell(row=r, column=4, value=fmt).font = BLACK
    ws.cell(row=r, column=5, value=pages if pages else None).font = BLACK
    c = ws.cell(row=r, column=6, value=retail); c.font = BLUE; c.number_format = CUR
    if pidx >= 0:
        c = ws.cell(row=r, column=7, value=f"={A['p'+str(pidx)]}*(1+{A['p7']})")
        c.font = GREEN
        ws.cell(row=r, column=8, value=f"={A['p6']}").font = GREEN
    else:
        ws.cell(row=r, column=7, value=0).font = BLACK
        ws.cell(row=r, column=8, value=0).font = BLACK
    ws.cell(row=r, column=7).number_format = CUR
    ws.cell(row=r, column=8).number_format = CUR
    ws.cell(row=r, column=9, value=f"=G{r}+H{r}").font = BLACK
    ws.cell(row=r, column=9).number_format = CUR
    ws.cell(row=r, column=10, value=f"=F{r}-I{r}").font = BLACK
    ws.cell(row=r, column=10).number_format = CUR
    ws.cell(row=r, column=11, value=f"=IF(F{r}=0,0,J{r}/F{r})").font = BLACK
    ws.cell(row=r, column=11).number_format = PCT
    c = ws.cell(row=r, column=12, value=wt); c.font = BLUE; c.number_format = '0.00'
    ws.cell(row=r, column=13, value=note).font = SUB
    for cc in range(1, 14):
        ws.cell(row=r, column=cc).border = BOX
    r += 1
last_sku = r - 1

r += 1
ws.cell(row=r, column=2, value="Sum of all print retail (one of each adult+student+pastor print item)").font = BLACKB
ws.cell(row=r, column=6, value=f"=SUM(F{r0}:F{last_sku})").font = BLACKB
ws.cell(row=r, column=6).number_format = CUR
r += 2
ws.cell(row=r, column=1, value="SKU COUNT MATH FOR RAJ").font = BLACKB
r += 1
for line in [
    "12 SKUs above x 6 campaign titles = 72 line items, of which 54 are physical and must be printed, stored, picked and packed.",
    "Add 5 kit SKUs per title (Personal, Group, Group Plus, Church Campaign, Student Group) = 30 more, each requiring its own kitted, barcoded carton.",
    "Total: ~102 SKUs at full build-out. Raj needs the physical count (54 print + 30 kits = 84) to quote storage and kitting honestly.",
    "Replace XX with title code: GOIA, MYM, GL, SPH, TCE, HME. ISBN 979-8-9977337-0-4 (GOIA devotional) and -1-1 (GOIA curriculum) already assigned per production schedule.",
]:
    ws.cell(row=r, column=1, value="• " + line).font = BLACK
    r += 1

# ==========================================================
# TAB 3 — KIT BUILDER
# ==========================================================
ws = wb.create_sheet("Kit Builder")
titleblock(ws, "Kit Builder — Component Roll-Up, True Landed Cost, and Price",
           "Contribution margin here is AFTER fulfillment. This is the number that tells you whether $199 loses money.")

kitcols = ["Kit", "Component", "Qty", "Unit Retail", "Ext. Retail", "Unit COGS", "Ext. COGS", "Unit Wt", "Ext. Wt"]
kw = [26, 34, 7, 13, 13, 12, 12, 10, 10]
hdr(ws, 4, kitcols, kw)

SKUROW = {code: r0 + i for i, (code, *_rest) in enumerate(skus)}

kits = [
    ("PERSONAL KIT", "Book + Devotional + Participant Guide. The individual buys this once.",
     [("XX-BK-01", 1), ("XX-DV-01", 1), ("XX-PG-01", 1)], 44.99),
    ("GROUP KIT", "10 Participant Guides + 2 Leader Guides + group video license. Industry standard is 10, not 8.",
     [("XX-PG-01", 10), ("XX-LG-01", 2), ("XX-VD-01", 1)], 199.00),
    ("GROUP KIT PLUS", "Group Kit + 10 devotionals so every member runs the 40 days.",
     [("XX-PG-01", 10), ("XX-LG-01", 2), ("XX-DV-01", 10), ("XX-VD-01", 1)], 329.00),
    ("STUDENT GROUP KIT", "10 Student Participant Guides + 2 Student Leader Guides + video license.",
     [("XX-SP-01", 10), ("XX-SL-01", 2), ("XX-VD-01", 1)], 179.00),
    ("CHURCH CAMPAIGN KIT", "One of everything a pastor needs to see and run the campaign. The Purpose Driven analog.",
     [("XX-CH-01", 1), ("XX-BK-01", 1), ("XX-DV-01", 1), ("XX-PG-01", 1), ("XX-LG-01", 1),
      ("XX-SD-01", 1), ("XX-SP-01", 1), ("XX-SL-01", 1), ("XX-CK-01", 1),
      ("XX-VC-01", 1), ("XX-PR-01", 1)], 299.00),
]

r = 5
kit_summary = []
for kname, kdesc, comps, price in kits:
    sect(ws, r, f"{kname}  —  {kdesc}", 9)
    r += 1
    start = r
    for code, qty in comps:
        sr = SKUROW[code]
        ws.cell(row=r, column=1, value="").font = BLACK
        ws.cell(row=r, column=2, value=f"='SKU Master'!B{sr}").font = GREEN
        c = ws.cell(row=r, column=3, value=qty); c.font = BLUE
        ws.cell(row=r, column=4, value=f"='SKU Master'!F{sr}").font = GREEN
        ws.cell(row=r, column=5, value=f"=C{r}*D{r}").font = BLACK
        ws.cell(row=r, column=6, value=f"='SKU Master'!I{sr}").font = GREEN
        ws.cell(row=r, column=7, value=f"=C{r}*F{r}").font = BLACK
        ws.cell(row=r, column=8, value=f"='SKU Master'!L{sr}").font = GREEN
        ws.cell(row=r, column=9, value=f"=C{r}*H{r}").font = BLACK
        for col, fmt in [(4, CUR), (5, CUR), (6, CUR), (7, CUR), (8, '0.00'), (9, '0.00')]:
            ws.cell(row=r, column=col).number_format = fmt
        for cc in range(1, 10):
            ws.cell(row=r, column=cc).border = BOX
        r += 1
    end = r - 1
    ws.cell(row=r, column=2, value="TOTAL IF BOUGHT SEPARATELY / LANDED COGS / SHIP WEIGHT").font = BLACKB
    ws.cell(row=r, column=5, value=f"=SUM(E{start}:E{end})").font = BLACKB
    ws.cell(row=r, column=7, value=f"=SUM(G{start}:G{end})").font = BLACKB
    ws.cell(row=r, column=9, value=f"=SUM(I{start}:I{end})").font = BLACKB
    for col, fmt in [(5, CUR), (7, CUR), (9, '0.00')]:
        ws.cell(row=r, column=col).number_format = fmt
        ws.cell(row=r, column=col).fill = GREYFILL
    kit_summary.append((kname, r, price))
    r += 2

# --- Kit economics block ---
r += 1
ws.cell(row=r, column=1, value="KIT ECONOMICS — DOES $199 LOSE MONEY?").font = TITLE
r += 2
econ_cols = ["Kit", "Sum of Parts", "Kit Price", "Discount to Buyer",
             "Landed COGS", "Fulfillment Cost", "Total Cost",
             "Contribution $", "Contribution %", "Verdict"]
ew = [26, 13, 12, 15, 13, 16, 12, 14, 14, 34]
hdr(ws, r, econ_cols, None)
for i, wd in enumerate(ew, start=1):
    if ws.column_dimensions[get_column_letter(i)].width < wd:
        ws.column_dimensions[get_column_letter(i)].width = wd
r += 1
econ_start = r
for kname, trow, price in kit_summary:
    ws.cell(row=r, column=1, value=kname).font = BLACKB
    ws.cell(row=r, column=2, value=f"=E{trow}").font = BLACK
    c = ws.cell(row=r, column=3, value=price); c.font = BLUE; c.fill = YELLOW
    ws.cell(row=r, column=4, value=f"=IF(B{r}=0,0,1-C{r}/B{r})").font = BLACK
    ws.cell(row=r, column=5, value=f"=G{trow}").font = BLACK
    ws.cell(row=r, column=6, value=f"=INDEX(Fulfillment!$H$5:$H$9,MATCH(A{r},Fulfillment!$A$5:$A$9,0))").font = GREEN
    ws.cell(row=r, column=7, value=f"=E{r}+F{r}").font = BLACK
    ws.cell(row=r, column=8, value=f"=C{r}-G{r}").font = BLACKB
    ws.cell(row=r, column=9, value=f"=IF(C{r}=0,0,H{r}/C{r})").font = BLACKB
    ws.cell(row=r, column=10, value=f'=IF(I{r}>={A["o4"]},"OK — clears target",IF(I{r}>0,"THIN — above cost but under target","LOSES MONEY — reprice"))').font = BLACK
    for col, fmt in [(2, CUR), (3, CUR), (4, PCT), (5, CUR), (6, CUR), (7, CUR), (8, CUR), (9, PCT)]:
        ws.cell(row=r, column=col).number_format = fmt
    for cc in range(1, 11):
        ws.cell(row=r, column=cc).border = BOX
    r += 1

r += 1
ws.cell(row=r, column=1, value="Note: Contribution % is after print, freight-in, kitting, pick/pack, carton and outbound freight — but before marketing, royalty, merchant fees and the 50/50 publisher split. Halve it again for RBI's take.").font = SUB

# ==========================================================
# TAB 4 — FULFILLMENT (RAJ)
# ==========================================================
ws = wb.create_sheet("Fulfillment")
titleblock(ws, "Fulfillment Cost Per Kit — The Raj Model",
           "Every cell in the Rate column comes from the Assumptions tab. Replace those with Raj's real quote and this whole workbook re-prices itself.")

fcols = ["Kit", "Ship Weight (lb)", "Kitting", "Pick & Pack", "Carton + Dunnage + Label",
         "Order Admin", "Outbound Freight", "TOTAL FULFILLMENT"]
hdr(ws, 4, fcols, [26, 16, 12, 14, 24, 13, 18, 20])

kit_names = [k[0] for k in kit_summary]
kit_totrows = {k[0]: k[1] for k in kit_summary}

r = 5
for kname in kit_names:
    trow = kit_totrows[kname]
    units_formula = f"=SUMIF('Kit Builder'!$A$1:$A${trow},\"\",'Kit Builder'!$C$1:$C${trow})"
    ws.cell(row=r, column=1, value=kname).font = BLACKB
    ws.cell(row=r, column=2, value=f"='Kit Builder'!I{trow}+1").font = GREEN
    ws.cell(row=r, column=2).number_format = '0.00'
    ws.cell(row=r, column=3, value=f"={A['f2']}").font = GREEN
    ws.cell(row=r, column=4, value=f"={A['f3']}+{A['f4']}*0").font = GREEN
    ws.cell(row=r, column=5, value=f"={A['f5']}+{A['f6']}+{A['f7']}").font = GREEN
    ws.cell(row=r, column=6, value=f"={A['f8']}").font = GREEN
    ws.cell(row=r, column=7, value=f"=MAX({A['f10']},B{r}*{A['f9']})").font = BLACK
    ws.cell(row=r, column=8, value=f"=SUM(C{r}:G{r})").font = BLACKB
    for col in range(3, 9):
        ws.cell(row=r, column=col).number_format = CUR
    ws.cell(row=r, column=8).fill = GREYFILL
    for cc in range(1, 9):
        ws.cell(row=r, column=cc).border = BOX
    r += 1

r += 1
ws.cell(row=r, column=1, value="Ship weight adds 1.00 lb for carton and dunnage. A kit ships as ONE pick, which is why kitting at receipt beats picking 12 loose items per order.").font = SUB
r += 2
ws.cell(row=r, column=1, value="THE $172 BOX — WHAT TO ASK RAJ").font = BLACKB
r += 1
for line in [
    "You mentioned a box that showed up costing $172. That is almost certainly a multi-kit carton or a freight-in shipment, not a single retail order. Make him break it apart on the call.",
    "The number you need is not 'what did the box cost.' It is: landed cost of one Group Kit, delivered to one church, all-in. If that is $28, you can price at $199 and clear $100+.",
    "Get storage quoted separately and in writing. Campaign inventory sits for months. At $22/pallet/month across six titles, storage alone can eat a full point of margin before a single kit ships.",
    "Ask for the rate card AND the exception list. The exception list is where the hidden charges live: oversize, address correction, residential surcharge, peak season, minimum monthlies, rush pick.",
]:
    ws.cell(row=r, column=1, value="• " + line).font = BLACK
    ws.merge_cells(start_row=r, start_column=1, end_row=r, end_column=8)
    ws.cell(row=r, column=1).alignment = Alignment(wrap_text=True, vertical="top")
    ws.row_dimensions[r].height = 28
    r += 1

# ==========================================================
# TAB 5 — PRO FORMA DRIVERS
# ==========================================================
ws = wb.create_sheet("Pro Forma Drivers")
titleblock(ws, "Corrected Drivers for Laura's Pro Forma",
           "These replace the flat '$15 avg sale price / $5-6 COGS' assumptions in the current Year 1 model.")

ws.column_dimensions["A"].width = 44
for col in "BCDEFG":
    ws.column_dimensions[col].width = 16
ws.column_dimensions["H"].width = 52

r = 4
sect(ws, r, "A. WHAT THE CURRENT PRO FORMA IS MISSING", 8); r += 1
issues = [
    ("No fulfillment line at all", "COGS is print only ($5-6). Pick, pack, kitting, storage and outbound freight are nowhere in the model. On a $15 book that is 15-25% of revenue, unmodeled."),
    ("Assumes 100% direct at full retail", "Every row uses Avg Sale Price = $15 on a $15 retail item. Trade and bulk channels net 45-75% of that."),
    ("Curriculum priced at $20 but modeled at $15", "The Retail column says $20 for every curriculum row; the Avg Sale Price column says $15. Pick one."),
    ("No returns reserve", "Christian trade is fully returnable. 15-25% is normal and it hits revenue AND costs a return-processing fee."),
    ("Identical rows produce different splits", "How Much Is Enough / Large / Consumer / Book shows $102,000 per side. The identical Generous Living row shows $51,000. Same inputs, different output — a formula is broken."),
    ("Pub dates precede finished manuscripts", "Pro forma shows Jan/Feb 2026 pub dates. Production schedule shows GOIA curriculum final delivery Aug 13 2026 and MYM Aug 19 2026. Year 1 revenue timing has to shift right."),
    ("No kit SKUs modeled", "The model sells books and curriculum as loose units. The actual business sells kits, which carry different price points, different margins and different fulfillment."),
]
hdr(ws, r, ["Issue", "", "", "", "", "", "", "Why it matters"]); r += 1
for a, b in issues:
    ws.cell(row=r, column=1, value=a).font = BLACKB
    ws.cell(row=r, column=8, value=b).font = BLACK
    ws.cell(row=r, column=8).alignment = Alignment(wrap_text=True, vertical="top")
    ws.row_dimensions[r].height = 30
    r += 1

r += 1
sect(ws, r, "B. REPLACEMENT DRIVERS — plug these into the model", 8); r += 1
hdr(ws, r, ["Driver", "Personal Kit", "Group Kit", "Group Kit Plus", "Student Kit", "Church Kit", "", "Note"]); r += 1

econ_map = {n: econ_start + i for i, (n, _t, _p) in enumerate(kit_summary)}
order = ["PERSONAL KIT", "GROUP KIT", "GROUP KIT PLUS", "STUDENT GROUP KIT", "CHURCH CAMPAIGN KIT"]

driver_rows = [
    ("List price", "C", CUR, "Straw-man. Steve to stress-test against Outreach/Lifeway comps."),
    ("Landed COGS", "E", CUR, "Print + freight-in + spoilage."),
    ("Fulfillment cost", "F", CUR, "From the Fulfillment tab. Replace with Raj's quote."),
    ("Contribution $ (gross)", "H", CUR, "Before marketing, royalty, merchant fees, publisher split."),
    ("Contribution %", "I", PCT, "Target is 45%+."),
]
for label, col, fmt, note in driver_rows:
    ws.cell(row=r, column=1, value=label).font = BLACKB
    for i, kn in enumerate(order):
        er = econ_map[kn]
        c = ws.cell(row=r, column=2 + i, value=f"='Kit Builder'!{col}{er}")
        c.font = GREEN; c.number_format = fmt
    ws.cell(row=r, column=8, value=note).font = SUB
    r += 1

# net-of-channel line
ws.cell(row=r, column=1, value="Net price after channel mix").font = BLACKB
for i, kn in enumerate(order):
    er = econ_map[kn]
    c = ws.cell(row=r, column=2 + i, value=f"='Kit Builder'!C{er}*{A['netreal']}")
    c.font = BLACK; c.number_format = CUR
ws.cell(row=r, column=8, value="Kit price x weighted net realization from the Assumptions tab.").font = SUB
netrow = r
r += 1
ws.cell(row=r, column=1, value="TRUE contribution after channel").font = BLACKB
for i, kn in enumerate(order):
    er = econ_map[kn]
    c = ws.cell(row=r, column=2 + i,
                value=f"=B{netrow}-'Kit Builder'!G{er}" if i == 0 else f"={get_column_letter(2+i)}{netrow}-'Kit Builder'!G{er}")
    c.font = BLACKB; c.number_format = CUR
    c.fill = GREYFILL
ws.cell(row=r, column=8, value="This is the honest number. If it goes negative, the channel mix is the problem, not the price.").font = SUB
truerow = r
r += 1
ws.cell(row=r, column=1, value="RBI share (50% of contribution)").font = BLACKB
for i, kn in enumerate(order):
    c = ws.cell(row=r, column=2 + i, value=f"={get_column_letter(2+i)}{truerow}*0.5")
    c.font = BLACK; c.number_format = CUR
ws.cell(row=r, column=8, value="Per the 50/50 publisher/RBI structure in the existing pro forma.").font = SUB
r += 2

sect(ws, r, "C. VOLUME REBUILD — same units, honest revenue", 8); r += 1
ws.cell(row=r, column=1, value="Current Year 1 model: 8,460 groups x ~213,000 units per campaign at $15 = $3,195,000 revenue.").font = BLACK
r += 1
ws.cell(row=r, column=1, value="Recut as kits: if those same 8,460 groups each buy one Group Kit at $199, that is $1,683,540 in kit revenue —").font = BLACK
r += 1
ws.cell(row=r, column=1, value="lower top line, but every unit is accounted for, fulfillment is priced in, and the number survives a due-diligence question.").font = BLACK
r += 2
ws.cell(row=r, column=1, value="Recommendation: model BOTH. Kits are the church motion. Individual SKUs are the consumer/trade motion. They are different businesses with different margins.").font = BLACKB

# ==========================================================
# TAB 6 — INDUSTRY BENCHMARKS
# ==========================================================
ws = wb.create_sheet("Benchmarks")
titleblock(ws, "Industry Benchmarks — The 'Ask Chad' Answers",
           "Researched Aug 2026. Sources listed. Use these to defend the pack size and the kit contents.")

ws.column_dimensions["A"].width = 40
ws.column_dimensions["B"].width = 58
ws.column_dimensions["C"].width = 44

hdr(ws, 4, ["Question", "Answer", "Source / evidence"])
r = 5
bench = [
    ("Standard units per small group pack — has 8 changed?",
     "YES — the industry standard is now 10, not 8. Lifeway's Bible Studies for Life Premium Bundle ships 10 Personal Study Guides, 2 Leader Guides, 2 commentaries and 1 leader pack, with instructions to add extras for groups over 10. Baptist Publishing House's DiscipleWay starter kit is 10 copies + 1 leader guide.",
     "Lifeway.com product pages, Fall/Summer/Spring 2026 bundles; baptistpublishinghouse.com"),
    ("Why 10 and not 8?",
     "10 is a psychological ordering unit, prices cleanly, and covers the group plus 2 spares for late joiners — which is how leaders actually order. It also lets you print a round number and avoids the leader having to place a second order mid-campaign.",
     "Lifeway bundle copy explicitly tells leaders to add extras above 10."),
    ("Do publishers include TWO leader guides?",
     "Yes, increasingly. Lifeway ships 2 per bundle and says the second exists to encourage apprentice/co-leader development and group multiplication. Copy the practice — it costs you ~$3.50 and it is a group-multiplication feature you can name in the sales copy.",
     "Lifeway Premium Bundle description."),
    ("What discount do bundles carry vs. buying separately?",
     "5-10% off the separate-item total is the published norm, tiered across bundle levels. Your straw-man kits are discounted 20-25%, which is more aggressive — defensible as a launch position, but know you are leaving margin on the table versus the category.",
     "Lifeway tiered bundle system (Enhanced / Premium)."),
    ("What is actually in a Purpose Driven-style campaign starter kit?",
     "Not 25 items. The 40 Days of Prayer starter kit is roughly: small group DVD with 6 video sessions plus a bonus lesson, an all-in-one participant workbook, a flash drive of customizable campaign resources (logos, web banners), a free downloadable sermon series, and sample poster, bookmark and sticker. That is 5-6 real components. Saddleback has become deliberately utilitarian — most support material moved online.",
     "store.pastors.com, 40 Days of Prayer Campaign Starter Kit."),
    ("What did the 40 Days in the Word kit add?",
     "Daily video devotionals behind a login, a DVD-driven small group curriculum, weekend sermon outlines, and a workbook with journal pages for the 40 days. The kit also carried a promo code for a free download of the message series.",
     "markhowelllive.com campaign review."),
    ("What does the broader category put in a church campaign kit?",
     "Christianbook's category description: sermon helps for pastors, small group leader guides, video presentations, marketing materials (bulletin inserts, posters), and planning tools. Outreach's kits follow the same shape — customizable sermons, a leader planning guide, resource video, PowerPoint templates, promo tools, branded web graphics.",
     "christianbook.com church-wide curriculum page; outreach.com campaign kits."),
    ("Implication for RBI",
     "Your Church Campaign Kit is competitive at 11 components — more physical content than Saddleback ships. The differentiation is that yours spans adult, student AND children in one box, and it is financial content, which carries a higher willingness to pay than a generic 40-day study.",
     "Comparison of the above."),
]
for q, a, s in bench:
    ws.cell(row=r, column=1, value=q).font = BLACKB
    ws.cell(row=r, column=2, value=a).font = BLACK
    ws.cell(row=r, column=3, value=s).font = SUB
    for cc in (1, 2, 3):
        ws.cell(row=r, column=cc).alignment = Alignment(wrap_text=True, vertical="top")
        ws.cell(row=r, column=cc).border = BOX
    ws.row_dimensions[r].height = 78
    r += 1

for sheet in wb.worksheets:
    sheet.sheet_view.showGridLines = False
    sheet.freeze_panes = "A5"

wb.save("/home/claude/rbi/RBI_Pricing_and_Packaging_Model.xlsx")
print("saved")
