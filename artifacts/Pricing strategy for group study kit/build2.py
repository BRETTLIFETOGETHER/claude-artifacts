import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

wb = openpyxl.Workbook()
ARIAL = "Arial"
BLUE = Font(name=ARIAL, size=10, color="0000FF")
BLACK = Font(name=ARIAL, size=10)
BLACKB = Font(name=ARIAL, size=10, bold=True)
GREEN = Font(name=ARIAL, size=10, color="008000")
WHITEB = Font(name=ARIAL, size=10, bold=True, color="FFFFFF")
TITLE = Font(name=ARIAL, size=14, bold=True, color="1F3864")
SUB = Font(name=ARIAL, size=10, italic=True, color="595959")
RED = Font(name=ARIAL, size=10, bold=True, color="C00000")
HDRFILL = PatternFill("solid", fgColor="1F3864")
SECFILL = PatternFill("solid", fgColor="D9E2F3")
YELLOW = PatternFill("solid", fgColor="FFFF00")
REDFILL = PatternFill("solid", fgColor="FCE4E4")
GREYFILL = PatternFill("solid", fgColor="F2F2F2")
thin = Side(style="thin", color="BFBFBF")
BOX = Border(left=thin, right=thin, top=thin, bottom=thin)
CUR = '$#,##0.00;($#,##0.00);-'
PCT = '0.0%;(0.0%);-'

def hdr(ws, row, labels, widths=None):
    for i, l in enumerate(labels, start=1):
        c = ws.cell(row=row, column=i, value=l)
        c.font = WHITEB; c.fill = HDRFILL; c.border = BOX
        c.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
    ws.row_dimensions[row].height = 32
    if widths:
        for i, w in enumerate(widths, start=1):
            ws.column_dimensions[get_column_letter(i)].width = w

def sect(ws, row, text, span):
    c = ws.cell(row=row, column=1, value=text)
    c.font = Font(name=ARIAL, size=10, bold=True, color="1F3864"); c.fill = SECFILL
    for i in range(2, span + 1):
        ws.cell(row=row, column=i).fill = SECFILL

def tb(ws, t, s):
    ws["A1"] = t; ws["A1"].font = TITLE
    ws["A2"] = s; ws["A2"].font = SUB

# ================= TAB 1: ASSUMPTIONS =================
ws = wb.active; ws.title = "Assumptions"
tb(ws, "RBI Pricing & Packaging Model — v2, built on actual print specs",
   "Rebuilt Aug 2026 from RBI_Campaign_Product_Print_Specs.xlsx. Supersedes the v1 straw-man. Status: PROPOSED.")
ws.column_dimensions["A"].width = 46
ws.column_dimensions["B"].width = 15
ws.column_dimensions["C"].width = 14
ws.column_dimensions["D"].width = 66

r = 4
ws.cell(row=r, column=1, value="LEGEND").font = BLACKB; r += 1
for a, b in [("BLUE", "You edit. Every lever is on this tab."),
             ("BLACK", "Formula — do not overwrite."),
             ("GREEN", "Pulled from another tab."),
             ("YELLOW fill", "Needs a real quote from Raj before this model is defensible.")]:
    ws.cell(row=r, column=1, value=a).font = BLACKB
    ws.cell(row=r, column=4, value=b).font = BLACK; r += 1

r += 1
sect(ws, r, "1. PRINT COST BUILD-UP — the specs call for FULL COLOR INTERIOR throughout", 4); r += 1
hdr(ws, r, ["Assumption", "Value", "Unit", "Basis / note"]); r += 1
pr = [
 ("4/4 interior, uncoated writable — per page", 0.024, "$/page", "Full-color both sides. Spec sheet: 'Interior Ink: Full color' on every printed piece."),
 ("4/4 interior, 80# opaque 8.5x11 — per page", 0.038, "$/page", "Student Curriculum spec. Larger trim, heavier stock."),
 ("Separate cover, 4c, matte/writable finish", 0.50, "$/unit", "Spec: 'No gloss / writable finish' on all covers."),
 ("Perfect binding", 0.35, "$/unit", "Spec: perfect bound on all bound pieces."),
 ("Hardcover upcharge (case bind)", 2.75, "$/unit", "Spec lists hardcover option on 40-day and 30-day devotionals."),
 ("Freight-in from printer (allocated)", 0.22, "$/unit", "Printer to Raj's warehouse."),
 ("Overrun / spoilage reserve", 0.03, "% of print", "3%."),
]
p0 = r
for a, v, u, n in pr:
    ws.cell(row=r, column=1, value=a).font = BLACK
    c = ws.cell(row=r, column=2, value=v); c.font = BLUE; c.fill = YELLOW
    c.number_format = PCT if "%" in u else CUR
    ws.cell(row=r, column=3, value=u).font = BLACK
    ws.cell(row=r, column=4, value=n).font = SUB; r += 1

r += 1
sect(ws, r, "2. FULFILLMENT / 3PL — unchanged from v1, still needs Raj's rate card", 4); r += 1
hdr(ws, r, ["Assumption", "Value", "Unit", "Basis / note"]); r += 1
ff = [
 ("Kitting / assembly labor", 2.25, "$/kit", "ASK RAJ. Pre-built at receipt."),
 ("Pick fee — first unit in order", 2.75, "$/order", "ASK RAJ."),
 ("Carton + dunnage + label", 2.60, "$/order", "ASK RAJ. Branded carton is an upcharge."),
 ("Order transaction / admin fee", 1.25, "$/order", "ASK RAJ. Often hidden."),
 ("Outbound freight rate", 1.60, "$/lb", "ASK RAJ. Negotiated ground, avg zone 5."),
 ("Outbound freight minimum", 12.00, "$/order", "ASK RAJ. This minimum is what kills single-item shipments."),
 ("Storage", 22.00, "$/pallet/mo", "ASK RAJ. Not in unit math below — model separately."),
]
f0 = r
for a, v, u, n in ff:
    ws.cell(row=r, column=1, value=a).font = BLACK
    c = ws.cell(row=r, column=2, value=v); c.font = BLUE; c.fill = YELLOW; c.number_format = CUR
    ws.cell(row=r, column=3, value=u).font = BLACK
    ws.cell(row=r, column=4, value=n).font = SUB; r += 1

r += 1
sect(ws, r, "3. CHANNEL MIX", 4); r += 1
hdr(ws, r, ["Channel", "Net % of retail", "Mix %", "Note"]); r += 1
ch = [("Direct to church / RBI store", 1.00, 0.45, "Full retail, RBI pays fulfillment."),
      ("Church bulk (25% qty discount)", 0.75, 0.25, "Campaign orders 25+ units."),
      ("Christian trade", 0.45, 0.20, "50-55% discount, returnable."),
      ("Amazon / mass", 0.55, 0.10, "Varies by term.")]
c0 = r
for a, v, m, n in ch:
    ws.cell(row=r, column=1, value=a).font = BLACK
    x = ws.cell(row=r, column=2, value=v); x.font = BLUE; x.number_format = PCT
    y = ws.cell(row=r, column=3, value=m); y.font = BLUE; y.number_format = PCT; y.fill = YELLOW
    ws.cell(row=r, column=4, value=n).font = SUB; r += 1
ws.cell(row=r, column=1, value="Weighted net realization / Mix check").font = BLACKB
x = ws.cell(row=r, column=2, value=f"=SUMPRODUCT(B{c0}:B{c0+3},C{c0}:C{c0+3})/C{r}"); x.font = BLACKB; x.number_format = PCT
y = ws.cell(row=r, column=3, value=f"=SUM(C{c0}:C{c0+3})"); y.font = BLACKB; y.number_format = PCT
ws.cell(row=r, column=4, value="Mix must total 100%.").font = SUB
NET = f"Assumptions!$B${r}"; r += 2

sect(ws, r, "4. TARGETS", 4); r += 1
hdr(ws, r, ["Assumption", "Value", "Unit", "Note"]); r += 1
ws.cell(row=r, column=1, value="Target contribution margin — kits").font = BLACK
t = ws.cell(row=r, column=2, value=0.45); t.font = BLUE; t.number_format = PCT
ws.cell(row=r, column=3, value="%").font = BLACK
ws.cell(row=r, column=4, value="After COGS AND fulfillment. Before marketing, royalty, merchant fees, 50/50 split.").font = SUB
TGT = f"Assumptions!$B${r}"

P = {i: f"Assumptions!$B${p0+i}" for i in range(len(pr))}
F = {i: f"Assumptions!$B${f0+i}" for i in range(len(ff))}

# ================= TAB 2: SKU MASTER =================
ws = wb.create_sheet("SKU Master")
tb(ws, "SKU Master — built from the actual spec sheet",
   "Page counts, trims and formats taken verbatim from RBI_Campaign_Product_Print_Specs.xlsx. Print cost is calculated from page count, not guessed.")
cols = ["SKU", "Product", "Trim", "Pages", "Interior", "Binding", "Printed / Digital",
        "Retail", "Print Cost", "Freight-In", "Landed COGS", "Margin $", "Margin %", "Ship Wt (lb)", "Spec source note"]
hdr(ws, 4, cols, [12, 32, 10, 8, 12, 20, 15, 11, 11, 10, 12, 11, 10, 11, 44])

# (sku, name, trim, pages, rate_idx, hardcover?, digital?, retail, wt, note)
skus = [
 ("XX-PG-40", "Participant Guide — 40-Day (6 sess.)", "7 x 9", 138, 0, 0, 0, 17.99, 0.62, "Spec: 125-150pp, separate cover, perfect bound, uncoated writable, full color."),
 ("XX-PG-30", "Participant Guide — 30-Day", "7 x 9", 125, 0, 0, 0, 16.99, 0.56, "Spec: 30-Day Small Group Curriculum, 'Both'. Page count assumed at MYM/GL 125."),
 ("XX-DV-40", "40-Day Devotional — paperback", "6 x 9", 220, 0, 0, 0, 18.99, 0.72, "Spec: 220pp, 6x9, perfect bound, full color interior."),
 ("XX-DV-40H", "40-Day Devotional — hardcover", "6 x 9", 220, 0, 1, 0, 26.99, 1.05, "Spec: 'Hardcover option' listed under Special Finishing."),
 ("XX-DV-30", "30-Day Devotional — paperback", "6 x 9", 175, 0, 0, 0, 16.99, 0.58, "Spec: 175pp, 6x9, hardcover option also available."),
 ("XX-SC-40", "Student Curriculum — 40-Day", "8.5 x 11", 75, 1, 0, 0, 14.99, 0.68, "Spec: 8.5x11, 75pp, 80# opaque, full color. GOIA + GL only."),
 ("XX-SD-40", "Student 40-Day Devotional", "6 x 9", 200, 0, 0, 0, 16.99, 0.68, "Spec: 150-175pp (GOIA) / 220pp (GL). Modeled at 200 mid-point — RECONCILE."),
 ("XX-LG-AD", "Adult Leader's Guide", "8.5 x 11", 0, 0, 0, 1, 0.00, 0.00, "Spec: DIGITAL ONLY. Included free with group video license."),
 ("XX-LG-ST", "Student Leader Resources", "8.5 x 11", 0, 0, 0, 1, 0.00, 0.00, "Spec: DIGITAL ONLY."),
 ("XX-LG-CH", "Children Leader Resources", "8.5 x 11", 0, 0, 0, 1, 0.00, 0.00, "Spec: DIGITAL ONLY. No children's devotional exists."),
 ("XX-CC-CH", "Children Curriculum Resources", "8.5 x 11", 0, 0, 0, 1, 0.00, 0.00, "Spec: DIGITAL / printable PDFs."),
 ("XX-SM-01", "Sunday Sermon Materials", "8.5 x 11", 0, 0, 0, 1, 0.00, 0.00, "Spec: digital PDF. Marked N on GOIA, Y on MYM and GL — RECONCILE."),
 ("XX-PM-01", "Promotional Materials", "Varies", 0, 0, 0, 1, 49.00, 0.00, "Spec: slides, graphics, bulletin and social assets."),
 ("XX-VD-01", "Video Curriculum — Group License", "Video", 0, 0, 0, 1, 49.00, 0.00, "Spec: video only, digital access. Zero COGS."),
 ("XX-VC-01", "Video Curriculum — Church License", "Video", 0, 0, 0, 1, 199.00, 0.00, "Unlimited groups, one campaign. Zero COGS."),
]

r0 = 5; r = r0
for sku, name, trim, pages, ridx, hc, dig, retail, wt, note in skus:
    ws.cell(row=r, column=1, value=sku).font = BLACK
    ws.cell(row=r, column=2, value=name).font = BLACK
    ws.cell(row=r, column=3, value=trim).font = BLACK
    ws.cell(row=r, column=4, value=pages if pages else None).font = BLACK
    ws.cell(row=r, column=5, value="Digital" if dig else "4/4 full color").font = BLACK
    ws.cell(row=r, column=6, value="Digital PDF" if dig else ("Case bound" if hc else "Perfect bound")).font = BLACK
    ws.cell(row=r, column=7, value="Digital" if dig else "Both").font = BLACK
    c = ws.cell(row=r, column=8, value=retail); c.font = BLUE; c.number_format = CUR
    if dig:
        ws.cell(row=r, column=9, value=0).font = BLACK
        ws.cell(row=r, column=10, value=0).font = BLACK
    else:
        hcterm = f"+{P[4]}" if hc else ""
        ws.cell(row=r, column=9,
                value=f"=(D{r}*{P[ridx]}+{P[2]}+{P[3]}{hcterm})*(1+{P[6]})").font = BLACK
        ws.cell(row=r, column=10, value=f"={P[5]}").font = GREEN
    ws.cell(row=r, column=9).number_format = CUR
    ws.cell(row=r, column=10).number_format = CUR
    ws.cell(row=r, column=11, value=f"=I{r}+J{r}").font = BLACK
    ws.cell(row=r, column=12, value=f"=H{r}-K{r}").font = BLACK
    ws.cell(row=r, column=13, value=f"=IF(H{r}=0,0,L{r}/H{r})").font = BLACK
    for col, fmt in [(11, CUR), (12, CUR), (13, PCT)]:
        ws.cell(row=r, column=col).number_format = fmt
    c = ws.cell(row=r, column=14, value=wt); c.font = BLUE; c.number_format = '0.00'
    ws.cell(row=r, column=15, value=note).font = SUB
    if dig:
        for cc in range(1, 16): ws.cell(row=r, column=cc).fill = GREYFILL
    for cc in range(1, 16): ws.cell(row=r, column=cc).border = BOX
    r += 1
SR = {s[0]: r0 + i for i, s in enumerate(skus)}
last = r - 1
r += 1
ws.cell(row=r, column=1, value="Grey rows are digital-only per the spec sheet: zero print cost, zero weight, zero fulfillment. Only 7 physical SKUs per title now — down from 9 in the v1 straw-man.").font = SUB

# ================= TAB 3: KIT BUILDER =================
ws = wb.create_sheet("Kit Builder")
tb(ws, "Kit Builder — rebuilt on real specs",
   "Leader guides are digital per spec, so they no longer add print cost, weight, or sum-of-parts value to any kit.")
hdr(ws, 4, ["Kit", "Component", "Qty", "Unit Retail", "Ext. Retail", "Unit COGS", "Ext. COGS", "Unit Wt", "Ext. Wt"],
    [28, 36, 7, 12, 12, 12, 12, 10, 10])

kits = [
 ("PERSONAL KIT", "40-Day Devotional + Participant Guide. No trade book — spec says use the devotional.",
  [("XX-DV-40", 1), ("XX-PG-40", 1)], 32.99),
 ("GROUP KIT", "10 Participant Guides + group video license. Leader's Guide included digitally at no cost.",
  [("XX-PG-40", 10), ("XX-VD-01", 1), ("XX-LG-AD", 1)], 199.00),
 ("GROUP KIT PLUS", "Group Kit + 10 devotionals so every member runs the 40 days.",
  [("XX-PG-40", 10), ("XX-DV-40", 10), ("XX-VD-01", 1), ("XX-LG-AD", 1)], 349.00),
 ("STUDENT GROUP KIT", "10 Student Curriculum + video license + digital student leader resources.",
  [("XX-SC-40", 10), ("XX-VD-01", 1), ("XX-LG-ST", 1)], 169.00),
 ("CHURCH CAMPAIGN KIT", "One printed sample of every physical piece, plus full digital access.",
  [("XX-PG-40", 1), ("XX-DV-40", 1), ("XX-DV-30", 1), ("XX-PG-30", 1), ("XX-SC-40", 1), ("XX-SD-40", 1),
   ("XX-VC-01", 1), ("XX-PM-01", 1), ("XX-LG-AD", 1), ("XX-LG-ST", 1), ("XX-LG-CH", 1), ("XX-CC-CH", 1)], 249.00),
]

r = 5; ks = []
for kn, kd, comps, price in kits:
    sect(ws, r, f"{kn}  —  {kd}", 9); r += 1
    st = r
    for code, qty in comps:
        sr = SR[code]
        ws.cell(row=r, column=2, value=f"='SKU Master'!B{sr}").font = GREEN
        c = ws.cell(row=r, column=3, value=qty); c.font = BLUE
        ws.cell(row=r, column=4, value=f"='SKU Master'!H{sr}").font = GREEN
        ws.cell(row=r, column=5, value=f"=C{r}*D{r}").font = BLACK
        ws.cell(row=r, column=6, value=f"='SKU Master'!K{sr}").font = GREEN
        ws.cell(row=r, column=7, value=f"=C{r}*F{r}").font = BLACK
        ws.cell(row=r, column=8, value=f"='SKU Master'!N{sr}").font = GREEN
        ws.cell(row=r, column=9, value=f"=C{r}*H{r}").font = BLACK
        for col, fmt in [(4, CUR), (5, CUR), (6, CUR), (7, CUR), (8, '0.00'), (9, '0.00')]:
            ws.cell(row=r, column=col).number_format = fmt
        for cc in range(1, 10): ws.cell(row=r, column=cc).border = BOX
        r += 1
    en = r - 1
    ws.cell(row=r, column=2, value="SUM OF PARTS / LANDED COGS / SHIP WEIGHT").font = BLACKB
    ws.cell(row=r, column=5, value=f"=SUM(E{st}:E{en})").font = BLACKB
    ws.cell(row=r, column=7, value=f"=SUM(G{st}:G{en})").font = BLACKB
    ws.cell(row=r, column=9, value=f"=SUM(I{st}:I{en})").font = BLACKB
    for col, fmt in [(5, CUR), (7, CUR), (9, '0.00')]:
        ws.cell(row=r, column=col).number_format = fmt; ws.cell(row=r, column=col).fill = GREYFILL
    ks.append((kn, r, price)); r += 2

r += 1
ws.cell(row=r, column=1, value="KIT ECONOMICS").font = TITLE; r += 2
hdr(ws, r, ["Kit", "Sum of Parts", "Kit Price", "Discount", "Landed COGS",
            "Fulfillment", "Total Cost", "Contribution $", "Contribution %", "Verdict"])
for i, wd in enumerate([28, 13, 12, 11, 13, 13, 12, 14, 14, 40], start=1):
    if ws.column_dimensions[get_column_letter(i)].width < wd:
        ws.column_dimensions[get_column_letter(i)].width = wd
r += 1
e0 = r
for kn, tr, price in ks:
    ws.cell(row=r, column=1, value=kn).font = BLACKB
    ws.cell(row=r, column=2, value=f"=E{tr}").font = BLACK
    c = ws.cell(row=r, column=3, value=price); c.font = BLUE; c.fill = YELLOW
    ws.cell(row=r, column=4, value=f"=IF(B{r}=0,0,1-C{r}/B{r})").font = BLACK
    ws.cell(row=r, column=5, value=f"=G{tr}").font = BLACK
    ws.cell(row=r, column=6, value=f"=INDEX(Fulfillment!$G$5:$G$9,MATCH(A{r},Fulfillment!$A$5:$A$9,0))").font = GREEN
    ws.cell(row=r, column=7, value=f"=E{r}+F{r}").font = BLACK
    ws.cell(row=r, column=8, value=f"=C{r}-G{r}").font = BLACKB
    ws.cell(row=r, column=9, value=f"=IF(C{r}=0,0,H{r}/C{r})").font = BLACKB
    ws.cell(row=r, column=10,
            value=f'=IF(I{r}>={TGT},"OK — clears target",IF(I{r}>0,"THIN — above cost, under target","LOSES MONEY — do not ship this way"))').font = BLACK
    for col, fmt in [(2, CUR), (3, CUR), (4, PCT), (5, CUR), (6, CUR), (7, CUR), (8, CUR), (9, PCT)]:
        ws.cell(row=r, column=col).number_format = fmt
    for cc in range(1, 11): ws.cell(row=r, column=cc).border = BOX
    r += 1
EM = {k[0]: e0 + i for i, k in enumerate(ks)}
r += 1
ws.cell(row=r, column=1, value="Contribution is after print, freight-in, kitting, pick, carton and outbound freight — before marketing, royalty, merchant fees and the 50/50 split. Halve again for RBI's share.").font = SUB

# ================= TAB 4: FULFILLMENT =================
ws = wb.create_sheet("Fulfillment")
tb(ws, "Fulfillment Cost Per Kit", "Rates all reference the Assumptions tab. Drop in Raj's rate card and the whole workbook re-prices.")
hdr(ws, 4, ["Kit", "Ship Weight (lb)", "Kitting", "Pick", "Carton + Label", "Order Admin",
            "Outbound Freight", "TOTAL"], [28, 16, 12, 12, 16, 13, 18, 14])
r = 5
for kn, tr, price in ks:
    ws.cell(row=r, column=1, value=kn).font = BLACKB
    ws.cell(row=r, column=2, value=f"='Kit Builder'!I{tr}+1").font = GREEN
    ws.cell(row=r, column=2).number_format = '0.00'
    ws.cell(row=r, column=3, value=f"={F[0]}").font = GREEN
    ws.cell(row=r, column=4, value=f"={F[1]}").font = GREEN
    ws.cell(row=r, column=5, value=f"={F[2]}").font = GREEN
    ws.cell(row=r, column=6, value=f"={F[3]}").font = GREEN
    ws.cell(row=r, column=7, value=f"=MAX({F[5]},B{r}*{F[4]})").font = BLACK
    x = ws.cell(row=r, column=8, value=f"=SUM(C{r}:G{r})"); x.font = BLACKB; x.fill = GREYFILL
    for col in range(3, 9): ws.cell(row=r, column=col).number_format = CUR
    for cc in range(1, 9): ws.cell(row=r, column=cc).border = BOX
    r += 1
r += 1
ws.cell(row=r, column=1, value="Ship weight adds 1.00 lb for carton and dunnage. The $12 freight minimum is why a light, low-priced kit is the worst thing you can ship one at a time.").font = SUB

# ================= TAB 5: SPEC DELTAS =================
ws = wb.create_sheet("Spec Deltas")
tb(ws, "What Changed — v1 straw-man vs. the actual spec sheet", "Read this before anyone reuses a v1 number.")
ws.column_dimensions["A"].width = 34
ws.column_dimensions["B"].width = 30
ws.column_dimensions["C"].width = 30
ws.column_dimensions["D"].width = 62
hdr(ws, 4, ["Item", "v1 straw-man", "Actual spec", "Economic consequence"])
r = 5
d = [
 ("Trade book", "$18.99, 208pp, anchor of Personal Kit",
  "Does not exist — 'No separate trade book for these campaign kits; use devotionals'",
  "Personal Kit loses its highest-margin component. The devotional has to carry both the retail and the campaign job."),
 ("40-Day Devotional", "176pp, 5.5 x 8.5, 1-color interior", "220pp, 6 x 9, FULL COLOR interior, hardcover option",
  "Print cost roughly doubles. This is the single largest cost change in the model."),
 ("Interior ink", "Assumed 1-color throughout", "Full color on every printed piece, uncoated writable",
  "4/4 uncoated runs about 2.5x a 1-color interior. Every landed COGS figure in v1 was low."),
 ("Adult Leader's Guide", "$12.99 printed, 2 per Group Kit", "DIGITAL ONLY",
  "Removes ~$8.80 of COGS and 0.60 lb from the Group Kit — but also removes $25.98 from the sum-of-parts anchor."),
 ("Children's edition", "$39.99 printed boxed kit", "DIGITAL ONLY, and no children's devotional exists",
  "Church Campaign Kit loses its heaviest perceived-value item. Kit gets lighter and cheaper but harder to justify at a premium."),
 ("30-Day products", "Not modeled at all", "30-Day Devotional (175pp) AND 30-Day Curriculum, both printed",
  "Two additional physical SKUs per title. Raj's SKU count goes up; so does storage."),
 ("Student Curriculum", "$15.99, 112pp, 7 x 9", "8.5 x 11, 75pp, 80# opaque, full color",
  "Bigger trim, heavier stock. This one piece IS in the Crown format — see the note on positioning."),
 ("Student devotional page count", "144pp", "GOIA says 150-175pp; GL says 220pp",
  "The two sheets disagree. Modeled at 200 as a placeholder. Reconcile before quoting."),
 ("Sermon materials", "Assumed included", "Marked N on GOIA, Y on Master Your Money and Generous Living",
  "Inconsistent across titles. If GOIA genuinely ships without sermon materials it is a weaker church-wide offer."),
 ("Student & children editions", "Assumed all titles", "Master Your Money sheet lists neither",
  "Consistent with the production schedule, which has no MYM student or children rows. So MYM cannot be sold as a whole-church campaign."),
 ("Quantity per bundle", "10 per group kit", "Field is blank on every row except Church Campaign Kit = 1",
  "The most important field on the spec sheet is empty. Raj cannot quote kitting without it."),
]
for a, b, c, e in d:
    ws.cell(row=r, column=1, value=a).font = BLACKB
    ws.cell(row=r, column=2, value=b).font = BLACK
    ws.cell(row=r, column=3, value=c).font = RED
    ws.cell(row=r, column=4, value=e).font = BLACK
    for cc in range(1, 5):
        ws.cell(row=r, column=cc).alignment = Alignment(wrap_text=True, vertical="top")
        ws.cell(row=r, column=cc).border = BOX
    ws.row_dimensions[r].height = 46
    r += 1

r += 1
ws.cell(row=r, column=1, value="OPEN QUESTIONS THE SPEC SHEET DOES NOT ANSWER").font = BLACKB; r += 1
for q in [
 "Quantity per bundle — blank on nearly every row. This is the number Raj needs first.",
 "Cover paper weight — TBD on every single piece. Cannot get a firm print quote without it.",
 "Church Campaign Kit box dimensions — 'TBD', with only the note that all three titles use the same size box.",
 "Campaign Handbook — appears in the production schedule as a deliverable but is absent from the print specs entirely.",
 "Hardcover — listed as an option with no decision, no price, and no volume split against paperback.",
]:
    ws.cell(row=r, column=1, value="• " + q).font = BLACK
    ws.merge_cells(start_row=r, start_column=1, end_row=r, end_column=4)
    ws.cell(row=r, column=1).alignment = Alignment(wrap_text=True)
    r += 1

for s in wb.worksheets:
    s.sheet_view.showGridLines = False
    s.freeze_panes = "A5"

wb.save("/home/claude/rbi/RBI_Pricing_Model_v2.xlsx")
print("saved")
