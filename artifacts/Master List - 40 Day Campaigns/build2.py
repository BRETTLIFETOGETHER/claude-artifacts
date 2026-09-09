import json, re, unicodedata
from collections import Counter, defaultdict
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.formatting.rule import FormulaRule

rows = json.load(open('/home/claude/mtl/rows.json'))
SRC = "Big Big brett master lifetogether campaign platform (ChatGPT, 7/4/26)"
URL = "https://chatgpt.com/g/g-p-6854e87c7fd881919afc69ee813e65e1/c/6967ed51-42b0-832c-9447-cc9d35e9a8d0"

ALLCAPS2 = re.compile(r'\b[A-Z][A-Z0-9&\'\-]{2,}\s+[A-Z][A-Z0-9&\'\-]{2,}')
def sane_sub(s):
    if not s: return ''
    s = s.strip()
    if set(s) == {'_'} or s.startswith(('→', '👉', '*', '_')): return ''
    if re.match(r'^\d{1,3}[.)]\s', s): return ''
    if ALLCAPS2.search(s): return ''
    if len(s.split()) < 3: return ''
    return s

def norm(t):
    t = unicodedata.normalize('NFKD', t.lower())
    t = re.sub(r'[^a-z0-9 ]', ' ', t)
    t = re.sub(r'^(the|a|an) ', '', t)
    return re.sub(r'\s+', ' ', t).strip()

for r in rows:
    if r['intent'] == 'TAXONOMY': r['subtitle'] = ''
    r['subtitle'] = sane_sub(r['subtitle'])
    r['title'] = re.sub(r'\s*\(not scripts\)|\s*BOOK$', '', r['title']).strip()

titles = [r for r in rows if r['kind'] == 'TITLE' and r['level'] != 'Category Label']
taxo = [r for r in rows if r not in titles]

# ---------------------------------------------------------------- classification maps
TOPIC = [
    (r'\b(generosity|generous|giving|philanthrop|donor|tithe)\b', 'Generosity'),
    (r'\b(legacy|heir|inheritance|generation|grandparent|succession|estate)\b', 'Family Legacy'),
    (r'\b(steward|ownership|owns|entrust|manage god)\b', 'Stewardship'),
    (r'\b(money|financial|finance|wealth|budget|debt|invest|enough|contentment|margin)\b', 'Money'),
    (r'\b(marriage|married|spouse|couple)\b', 'Marriage'),
    (r'\b(parent|child|children|kids|teen|raising|family meeting|home)\b', 'Parenting'),
    (r'\b(business|company|entrepreneur|ceo|executive|marketplace|profit|work|vocation|calling)\b', 'Business'),
    (r'\b(leader|leadership|influence|team)\b', 'Leadership'),
    (r'\b(health|flourish|whole[- ]life|wellness|body|habits|rest)\b', 'Health & Flourishing'),
    (r'\b(purpose|design|made for|meaning|created)\b', 'Purpose'),
    (r'\b(small group|community|belong|fellowship|together|one another)\b', 'Small Groups'),
    (r'\b(church|congregation|pastor|sermon|ministry|mission|outreach|evangel)\b', 'Church Health'),
    (r'\b(prayer|pray)\b', 'Prayer'),
    (r'\b(disciple|grow|formation|spiritual|faith|christ|jesus|bible|scripture|worship|wisdom)\b', 'Spiritual Growth'),
    (r'\b(relationship|conflict|forgive|unity|trust)\b', 'Relationships'),
]
def topic_of(r):
    hay = f"{r['title']} {r['subtitle']} {r['category']}"
    for pat, t in TOPIC:
        if re.search(pat, hay, re.I): return t
    return 'Unclear'

def secondary_of(r):
    hay = f"{r['title']} {r['subtitle']} {r['category']}"
    hits = [t for pat, t in TOPIC if re.search(pat, hay, re.I)]
    return '; '.join(dict.fromkeys(hits[1:4]))

ADV = re.compile(r'\b(advisor|attorney|cpa|accountant|family office|wealth|planner|trusted guide|estate)\b', re.I)
FAM = re.compile(r'\b(family|families|heir|grandparent|parent|marriage|children|household)\b', re.I)
CHURCH = re.compile(r'\b(church|pastor|congregation|sermon|small group|churchwide|campaign|40 days)\b', re.I)
BIZ = re.compile(r'\b(business|ceo|executive|entrepreneur|owner|marketplace|company)\b', re.I)

def audience_of(r):
    hay = f"{r['req']} {r['category']} {r['title']}"
    if ADV.search(r['req']) or ADV.search(r['category']): return 'Financial Advisor'
    if BIZ.search(hay): return 'Business Owner'
    if re.search(r'\blegacy famil|families of wealth|affluent|high[- ]net', hay, re.I): return 'Legacy Family'
    if FAM.search(hay): return 'Family'
    if CHURCH.search(hay): return 'Church'
    if re.search(r'\bpastor\b', hay, re.I): return 'Senior Pastor'
    return 'Unclear'

def platform_of(r, topic, aud):
    t = r['title']
    if re.match(r'^\d{1,3} Days? (of|to)\b', t, re.I): return '40 Day Campaigns'
    if r['level'] == 'Platform / Brand': return 'Unclear / Needs Review'
    if topic == 'Family Legacy' and aud in ('Financial Advisor',): return 'Christian Advisor Network'
    if topic == 'Family Legacy': return 'Family Legacy Ministry'
    if topic == 'Generosity': return 'Generosity Ministry'
    if topic in ('Money', 'Stewardship'): return 'Financial Wisdom Ministry'
    if topic == 'Business': return 'Purpose Built Business'
    if topic == 'Health & Flourishing': return 'Flourishing Life Together'
    if topic in ('Church Health', 'Small Groups'): return 'Life Together / Church'
    if aud == 'Financial Advisor': return 'Christian Advisor Network'
    return 'Unclear / Needs Review'

CTYPE = {'Campaign': 'Campaign', 'Curriculum / Series': 'Curriculum', 'Session': 'Session',
         'Day / Devotional': 'Devotional', 'Tool / Asset': 'Tool', 'Assessment': 'Assessment',
         'Training': 'Training', 'Platform / Brand': 'Website / Brand'}

THIRD = [(r'\bmaster your money\b', 'Third-party owned — do not publish', 'Ron Blue (published book)'),
         (r'\bjourney of generosity\b', 'Third-party owned — do not publish', 'Generous Giving program'),
         (r'\b40 days of purpose\b|\bpurpose driven\b', 'Third-party owned — do not publish', 'Saddleback / Purpose Driven'),
         (r'\bgenerous living\b', 'Third-party adjacent — position around it', 'Also a Ron Blue title'),
         (r'\bfinancial peace\b', 'Third-party owned — do not publish', 'Ramsey Solutions title'),
         (r'\bgod owns it all\b', 'RBI / client work — confirm rights', 'Built with RBI / Ron Blue')]

def rights_of(r):
    for pat, flag, why in THIRD:
        if re.search(pat, r['title'], re.I): return flag, why
    if '™' in r['title'] or '™' in r['subtitle']: return 'Trademark unverified (™ applied in draft)', '™ applied in draft output'
    if re.search(r'\b(family legacy)\b', r['title'], re.I): return 'Partner-sensitive (Conway / Signatry / WCM)', 'Family Legacy naming overlaps Tom Conway framework'
    return 'LifeTogether — clear', ''

# ---------------------------------------------------------------- families / versions
fam = defaultdict(list)
for r in titles:
    key = f"{r['parent']}|{r['slot']}" if r['slot'] else norm(r['title'])
    r['famkey'] = key
    fam[key].append(r)

for key, group in fam.items():
    group.sort(key=lambda x: x['line'])
    subs = {norm(g['subtitle']) for g in group if g['subtitle']}
    for idx, g in enumerate(group):
        if len(group) == 1:
            g['ver'] = 'Only version in source'
        elif idx == len(group) - 1:
            g['ver'] = 'Latest in source'
        elif g['slot']:
            g['ver'] = 'Superseded draft'
        elif len(subs) > 1:
            g['ver'] = 'Competing subtitle'
        else:
            g['ver'] = 'Duplicate'
        g['famsize'] = len(group)

def quality_of(r):
    if r['rejected']: return "E — Archive / Probably Don't Use"
    if r['ver'] in ('Duplicate',): return 'C — Duplicate / Alternate'
    if r['ver'] in ('Superseded draft', 'Competing subtitle'): return 'C — Duplicate / Alternate'
    if len(r['title'].split()) < 2 or r['topic'] == 'Unclear' or r['aud'] == 'Unclear': return 'F — Human Review Needed'
    if r['subtitle']: return 'B — Strong Concept / Needs Polish'
    return 'F — Human Review Needed' if r['level'] in ('Platform / Brand',) else 'B — Strong Concept / Needs Polish'

def existing_of(r):
    if re.search(r'\b(god owns it all|master your money|journey of generosity|40 days of purpose)\b', r['title'], re.I):
        return 'Existing / Confirmed'
    if r['intent'] == 'BUILD': return 'Proposed'
    return 'Brainstorming'

def originator_of(r):
    for pat, flag, why in THIRD:
        if re.search(pat, r['title'], re.I) and 'Third-party owned' in flag: return 'Third-party owned'
    if r['brett']: return 'Brett-authored (his own turn)'
    return 'AI-generated on request'

for r in titles:
    r['topic'] = topic_of(r)
    r['sec'] = secondary_of(r)
    r['aud'] = audience_of(r)
    r['plat'] = platform_of(r, r['topic'], r['aud'])
    r['ctype'] = CTYPE.get(r['level'], 'Unknown')
    r['rights'], r['rightswhy'] = rights_of(r)
    r['q'] = quality_of(r)
    r['exist'] = existing_of(r)
    r['orig'] = originator_of(r)

titles.sort(key=lambda r: r['line'])
for n, r in enumerate(titles, start=1):
    r['id'] = f"MTL-{n:04d}"

def ai_note(r):
    n = []
    if r['rejected']:
        n.append("Generated before Brett's correction at line 13397 asking for titles that do NOT lead with 'Family Legacy'. Superseded by his own instruction.")
    if r['famsize'] > 1:
        n.append(f"{r['famsize']} instances of this title/slot in this file — canonical version needs picking.")
    if r['rightswhy']:
        n.append(r['rightswhy'] + '.')
    if not r['subtitle'] and r['level'] in ('Curriculum / Series', 'Campaign'):
        n.append('No subtitle in source.')
    if r['aud'] == 'Unclear' or r['topic'] == 'Unclear':
        n.append('Source does not make audience or topic clear.')
    if r['orig'] == 'Brett-authored (his own turn)':
        n.append("Appears inside Brett's own message rather than in generated output.")
    return ' '.join(n)

def ctx_note(r):
    req = r['req'][:150]
    cat = f"Section: {r['category']}. " if r['category'] else ''
    return f"{cat}Generated in response to: \"{req}\""

# ---------------------------------------------------------------- workbook
NAVY = "1F3864"; LIGHTNAVY = "D9E2F3"; BAND = "F2F5FA"
GREEN = "C6EFCE"; BLUE = "DDEBF7"; ORANGE = "FCE4D6"; PURPLE = "E4DFEC"; GREY = "E7E6E6"; RED = "FFC7CE"; YELLOW = "FFF2CC"
wb = openpyxl.Workbook()

VOCAB = {
    "Keep / Review / Archive": ["Keep", "Review", "Archive"],
    "Level": ["Platform / Brand", "Product Line", "Campaign", "Curriculum / Series", "Session", "Day / Devotional",
              "Book / Chapter", "Tool / Asset", "Assessment", "Training", "Category Label", "Positioning Line", "Fragment / Not a Title"],
    "Version Status": ["Only version in source", "Latest in source", "Superseded draft", "Competing subtitle",
                       "Competing name for same asset", "Duplicate", "Needs version check"],
    "Platform / Brand": ["Life Together / Church", "Sermon Library", "Pastor's Library", "40 Day Campaigns",
                         "Family Legacy by Design", "Family Legacy Ministry", "Christian Advisor Network",
                         "Generosity Ministry", "Financial Wisdom Ministry", "Purpose Built Business",
                         "Flourishing Life Together", "Small Group / Curriculum", "Multiple / Shared",
                         "Not stated in source", "Unclear / Needs Review"],
    "Primary Audience": ["Senior Pastor", "Pastor / Church Leader", "Executive Pastor", "Church", "Small Group Leader",
                         "Individual Christian", "Family", "Legacy Family", "Financial Advisor", "Christian Advisor",
                         "Trusted Guide (multi-profession)", "Business Owner", "Business Leader", "Donor", "Multiple", "Unclear"],
    "Content Type": ["Sermon", "Sermon Series", "Campaign", "Journey", "Curriculum", "Devotional", "Book", "Course",
                     "Session", "Assessment", "Tool", "Ministry", "Website / Brand", "Resource", "Article", "Training",
                     "Business Concept", "AI / Brainstorming Concept", "Unknown"],
    "Quality / Readiness": ["A — Strong / Ready", "B — Strong Concept / Needs Polish", "C — Duplicate / Alternate",
                            "D — Good But Better for Another Platform", "E — Archive / Probably Don't Use", "F — Human Review Needed"],
    "Existing vs Concept": ["Existing / Confirmed", "Appears Existing", "Proposed", "Brainstorming", "Unclear"],
    "Originator": ["Brett-authored (his own turn)", "Brett-selected (endorsed in his turn)", "AI-generated on request",
                   "Existing asset referenced", "Third-party owned", "Unclear"],
    "Rights / Ownership": ["LifeTogether — clear", "RBI / client work — confirm rights", "Third-party owned — do not publish",
                           "Third-party adjacent — position around it", "Trademark unverified (™ applied in draft)",
                           "Partner-sensitive (Conway / Signatry / WCM)", "Needs rights review"],
}
lists = wb.active; lists.title = "LISTS"
lists["A1"] = "Dropdown vocabularies — edit here and every dropdown updates."
lists["A1"].font = Font(name="Arial", size=10, italic=True, color="7F7F7F")
for c, (head, vals) in enumerate(VOCAB.items(), start=1):
    cell = lists.cell(row=2, column=c, value=head)
    cell.font = Font(name="Arial", size=10, bold=True, color="FFFFFF"); cell.fill = PatternFill("solid", fgColor=NAVY)
    cell.alignment = Alignment(wrap_text=True, vertical="center")
    for r_, v in enumerate(vals, start=3):
        lists.cell(row=r_, column=c, value=v).font = Font(name="Arial", size=10)
    lists.column_dimensions[get_column_letter(c)].width = 32
lists.freeze_panes = "A3"
def vrange(head):
    c = get_column_letter(list(VOCAB).index(head) + 1)
    return f"LISTS!${c}$3:${c}${len(VOCAB[head]) + 2}"

ws = wb.create_sheet("MASTER LIBRARY")
HEADERS = ["ID", "Keep / Review / Archive", "Level", "Original Title", "Original Subtitle", "Recommended Title",
           "Recommended Subtitle", "Parent / Belongs To", "Slot", "Version Status", "Source-Stated Platform",
           "Proposed Platform (inference)", "Primary Audience", "Content Type", "Topic / Category", "Secondary Topics",
           "Title Family / Duplicate Group", "Quality / Readiness", "Existing vs Concept", "Originator",
           "Rights / Ownership Flag", "Source", "Source Line", "Source Link", "Source Context / Notes", "AI Notes",
           "HUMAN DECISION"]
WIDTHS = [10, 15, 20, 38, 42, 26, 30, 26, 12, 22, 20, 26, 22, 18, 20, 24, 26, 30, 20, 26, 30, 30, 11, 26, 40, 40, 22]
for c, h in enumerate(HEADERS, start=1):
    cell = ws.cell(row=1, column=c, value=h)
    cell.font = Font(name="Arial", size=10, bold=True, color="FFFFFF"); cell.fill = PatternFill("solid", fgColor=NAVY)
    cell.alignment = Alignment(wrap_text=True, vertical="center", horizontal="center")
    ws.column_dimensions[get_column_letter(c)].width = WIDTHS[c - 1]
ws.row_dimensions[1].height = 44

thin = Side(style="thin", color="D0D0D0")
for i, r in enumerate(titles, start=2):
    vals = [r['id'], 'Review', r['level'], r['title'], r['subtitle'], '', '', r['parent'], r['slot'], r['ver'],
            'Not stated in source', r['plat'], r['aud'], r['ctype'], r['topic'], r['sec'], r['famkey'][:60],
            r['q'], r['exist'], r['orig'], r['rights'], SRC, r['line'], URL, ctx_note(r), ai_note(r), '']
    if r['rejected'] or r['ver'] == 'Duplicate':
        vals[1] = 'Archive'
    for c, v in enumerate(vals, start=1):
        cell = ws.cell(row=i, column=c, value=v)
        cell.font = Font(name="Arial", size=10, bold=(c == 4))
        cell.alignment = Alignment(wrap_text=True, vertical="top")
        cell.border = Border(left=thin, right=thin, top=thin, bottom=thin)
    ws.cell(row=i, column=27).fill = PatternFill("solid", fgColor=YELLOW)
    longest = max(len(r['title']), len(r['subtitle']))
    ws.row_dimensions[i].height = 60 if longest > 70 else 45

LAST = len(titles) + 1
ws.auto_filter.ref = f"A1:AA{LAST}"
ws.freeze_panes = "D2"
for col, head in {"B": "Keep / Review / Archive", "C": "Level", "J": "Version Status", "K": "Platform / Brand",
                  "L": "Platform / Brand", "M": "Primary Audience", "N": "Content Type", "R": "Quality / Readiness",
                  "S": "Existing vs Concept", "T": "Originator", "U": "Rights / Ownership"}.items():
    dv = DataValidation(type="list", formula1=vrange(head), allow_blank=True, showDropDown=False)
    ws.add_data_validation(dv); dv.add(f"{col}2:{col}{LAST}")

# compact view: collapsible detail groups
for col in "FGHIJK":
    ws.column_dimensions[col].outlineLevel = 1; ws.column_dimensions[col].hidden = True
for col in "VWXYZ":
    ws.column_dimensions[col].outlineLevel = 1; ws.column_dimensions[col].hidden = True
ws.sheet_properties.outlinePr.summaryRight = True

rng = f"A2:AA{LAST}"
ws.conditional_formatting.add(rng, FormulaRule(formula=['AND(MOD(ROW(),2)=0,$A2<>"")'], fill=PatternFill("solid", bgColor=BAND)))
for letter, fill in [("A", GREEN), ("B", BLUE), ("C", ORANGE), ("D", PURPLE), ("E", GREY), ("F", RED)]:
    ws.conditional_formatting.add(f"R2:R{LAST}", FormulaRule(formula=[f'LEFT($R2,1)="{letter}"'], fill=PatternFill("solid", bgColor=fill)))
ws.conditional_formatting.add(f"U2:U{LAST}", FormulaRule(formula=['OR(ISNUMBER(SEARCH("Third-party",$U2)),ISNUMBER(SEARCH("Trademark",$U2)),ISNUMBER(SEARCH("Partner-sensitive",$U2)),ISNUMBER(SEARCH("Needs rights",$U2)))'], fill=PatternFill("solid", bgColor=RED)))
ws.conditional_formatting.add(f"S2:S{LAST}", FormulaRule(formula=['$S2="Existing / Confirmed"'], fill=PatternFill("solid", bgColor=GREEN)))
ws.conditional_formatting.add(f"C2:C{LAST}", FormulaRule(formula=['OR($C2="Platform / Brand",$C2="Campaign")'], fill=PatternFill("solid", bgColor=LIGHTNAVY)))

# ---------------------------------------------------------------- SUMMARY
sm = wb.create_sheet("SUMMARY")
for col, w in [("A", 44), ("B", 13), ("C", 3), ("D", 44), ("E", 13)]:
    sm.column_dimensions[col].width = w
sm["A1"] = "MASTER TITLE LIBRARY — SUMMARY"; sm["A1"].font = Font(name="Arial", size=14, bold=True, color=NAVY)
sm["A2"] = f"Source: {SRC}"; sm["A2"].font = Font(name="Arial", size=10, italic=True, color="7F7F7F")
sm["A3"] = "Yellow cells are yours: HUMAN DECISION on the master tab, Decision on REVIEW QUEUE. Everything else is Claude-filled and re-derivable."
sm["A3"].font = Font(name="Arial", size=10, italic=True, color="7F7F7F")
sm["A4"] = "Columns F–K and V–Z are collapsed by default. Click the + above the column headers to expand full detail."
sm["A4"].font = Font(name="Arial", size=10, italic=True, color="7F7F7F")
M = "'MASTER LIBRARY'"
def cif(col, val): return f'=COUNTIF({M}!${col}$2:${col}${LAST},"{val}")'
def block(r, c, heading, pairs):
    hc = sm.cell(row=r, column=c, value=heading)
    hc.font = Font(name="Arial", size=10, bold=True, color="FFFFFF"); hc.fill = PatternFill("solid", fgColor=NAVY)
    sm.cell(row=r, column=c + 1).fill = PatternFill("solid", fgColor=NAVY)
    for i, (label, formula) in enumerate(pairs, start=1):
        a = sm.cell(row=r + i, column=c, value=label); a.font = Font(name="Arial", size=10)
        b = sm.cell(row=r + i, column=c + 1, value=formula); b.font = Font(name="Arial", size=10)
        b.alignment = Alignment(horizontal="center")
        if i % 2 == 0:
            a.fill = PatternFill("solid", fgColor=BAND); b.fill = PatternFill("solid", fgColor=BAND)
    return r + len(pairs) + 2
r = 6
r = block(r, 1, "TOTALS", [("Total title records", f'=COUNTA({M}!$A$2:$A${LAST})')]
          + [(v, cif("B", v)) for v in VOCAB["Keep / Review / Archive"]]
          + [("Needing human review (F)", cif("R", "F — Human Review Needed")),
             ("Duplicates / alternates / superseded",
              f'=COUNTIF({M}!$J$2:$J${LAST},"Superseded draft")+COUNTIF({M}!$J$2:$J${LAST},"Competing subtitle")+COUNTIF({M}!$J$2:$J${LAST},"Duplicate")'),
             ("Taxonomy entries held on separate tab", len(taxo))])
r = block(r, 1, "BY QUALITY / READINESS", [(v, cif("R", v)) for v in VOCAB["Quality / Readiness"]])
r = block(r, 1, "BY EXISTING VS CONCEPT", [(v, cif("S", v)) for v in VOCAB["Existing vs Concept"]])
r = block(r, 1, "BY ORIGINATOR", [(v, cif("T", v)) for v in VOCAB["Originator"]])
r2 = 6
r2 = block(r2, 4, "BY LEVEL", [(v, cif("C", v)) for v in VOCAB["Level"]])
r2 = block(r2, 4, "BY PROPOSED PLATFORM / BRAND", [(v, cif("L", v)) for v in VOCAB["Platform / Brand"]])
r2 = block(r2, 4, "BY PRIMARY AUDIENCE", [(v, cif("M", v)) for v in VOCAB["Primary Audience"]])
r2 = block(r2, 4, "BY CONTENT TYPE", [(v, cif("N", v)) for v in VOCAB["Content Type"]])
r2 = block(r2, 4, "BY RIGHTS / OWNERSHIP FLAG", [(v, cif("U", v)) for v in VOCAB["Rights / Ownership"]])
sm.freeze_panes = "A6"

# ---------------------------------------------------------------- REVIEW QUEUE
rq = wb.create_sheet("REVIEW QUEUE")
RQH = ["Priority", "ID(s)", "Title / cluster", "Why it is in the queue", "The decision you actually have to make", "DECISION", "Decided by / date"]
RQW = [10, 22, 34, 50, 58, 24, 18]
CURATED = [
 ("1", "MTL-0001+", "God Owns It All", "Existing asset built with RBI, Ron Blue transcripts and LifeWay structure underneath it.",
  "Confirm what LifeTogether can publish, license or campaign-ify without a new agreement. Everything downstream inherits this answer."),
 ("1", "—", "Brand architecture", "In his own turns Brett asks what separates LifeTogether Productions from LifeTogether, whether these are separate sites on one platform, and how Family Legacy Ministry avoids stepping on Tom Conway's Family Legacy by Design.",
  "Answer these once. Until then the Proposed Platform column on 3,000 rows is inference, not fact."),
 ("1", "—", "™ symbols", "143 ™ marks across 80 names appear in this file, applied in draft output, including malformed ones like 'Design™'.",
  "Name the handful that go to a real trademark search. Every other ™ gets stripped."),
 ("2", "—", "Family Legacy XYZ block", "114 titles were generated as 'Family Legacy [Topic]' before Brett corrected the brief and asked for titles that do not lead with Family Legacy.",
  "Confirm the whole block is archived, not just deprioritized."),
 ("2", "—", "Five-purpose campaigns", "40 Days of Worship / Fellowship / Discipleship / Ministry / Mission almost certainly already exist in the Biblical Purpose Library and the 40 Day Campaign catalog.",
  "Dedupe against those catalogs before import, or accept two of every five-purpose campaign."),
 ("2", "—", "Trusted Guide brand", "Three competing wrappers for one asset within 120 lines: Library, Stewardship Library, Platform.",
  "Pick the wrapper. 'Trusted guide' is the strongest idea in the file and it currently has no settled name."),
 ("3", "—", "Taxonomy tab", "1,083 extracted items are life events, affinity groups, felt needs, questions and category labels — indexes, not titles.",
  "Confirm these stay on the TAXONOMY tab as the platform's filtering vocabulary rather than entering the title library."),
]
for c, h in enumerate(RQH, start=1):
    cell = rq.cell(row=1, column=c, value=h)
    cell.font = Font(name="Arial", size=10, bold=True, color="FFFFFF"); cell.fill = PatternFill("solid", fgColor=NAVY)
    cell.alignment = Alignment(wrap_text=True, vertical="center", horizontal="center")
    rq.column_dimensions[get_column_letter(c)].width = RQW[c - 1]
qrows = list(CURATED)
big = sorted([(k, v) for k, v in fam.items() if len(v) > 2], key=lambda kv: -len(kv[1]))[:18]
for k, g in big:
    ids = f"{g[0]['id']}–{g[-1]['id']}"
    qrows.append(("2", ids, g[0]['title'][:60], f"{len(g)} instances of this title or slot across the file; {len({norm(x['subtitle']) for x in g if x['subtitle']})} distinct subtitles.",
                  "Pick the canonical version, or split it into named editions."))
for i, vals in enumerate(qrows, start=2):
    for c, v in enumerate(list(vals) + ["", ""], start=1):
        cell = rq.cell(row=i, column=c, value=v)
        cell.font = Font(name="Arial", size=10, bold=(c == 3))
        cell.alignment = Alignment(wrap_text=True, vertical="top", horizontal="center" if c == 1 else "left")
        cell.border = Border(left=thin, right=thin, top=thin, bottom=thin)
    rq.cell(row=i, column=6).fill = PatternFill("solid", fgColor=YELLOW)
    rq.cell(row=i, column=7).fill = PatternFill("solid", fgColor=YELLOW)
    rq.row_dimensions[i].height = 52
rq.auto_filter.ref = f"A1:G{len(qrows) + 1}"; rq.freeze_panes = "C2"

# ---------------------------------------------------------------- TAXONOMY
tx = wb.create_sheet("TAXONOMY")
TXH = ["Entry", "Index / Section", "Kind", "Source Line", "Note"]
for c, (h, w) in enumerate(zip(TXH, [40, 34, 22, 12, 50]), start=1):
    cell = tx.cell(row=1, column=c, value=h)
    cell.font = Font(name="Arial", size=10, bold=True, color="FFFFFF"); cell.fill = PatternFill("solid", fgColor="375623")
    cell.alignment = Alignment(wrap_text=True, vertical="center", horizontal="center")
    tx.column_dimensions[get_column_letter(c)].width = w
for i, r in enumerate(sorted(taxo, key=lambda x: x['line']), start=2):
    kind = 'Life event' if re.search(r'life event', r['category'], re.I) else (
           'Affinity group' if re.search(r'affinity', r['category'], re.I) else (
           'Trusted guide / provider' if re.search(r'trusted|provider|advisor', r['category'], re.I) else 'Category label'))
    vals = [r['title'], r['category'] or '(none stated)', kind, r['line'],
            'Filter vocabulary for the platform — not a title.']
    for c, v in enumerate(vals, start=1):
        cell = tx.cell(row=i, column=c, value=v)
        cell.font = Font(name="Arial", size=10); cell.alignment = Alignment(wrap_text=True, vertical="top")
        cell.border = Border(left=thin, right=thin, top=thin, bottom=thin)
    tx.row_dimensions[i].height = 30
tx.auto_filter.ref = f"A1:E{len(taxo) + 1}"; tx.freeze_panes = "A2"
tx.conditional_formatting.add(f"A2:E{len(taxo) + 1}", FormulaRule(formula=['MOD(ROW(),2)=0'], fill=PatternFill("solid", bgColor=BAND)))

# ---------------------------------------------------------------- NAMING + RIGHTS
nc = wb.create_sheet("NAMING CANDIDATES")
NCR = [("Pastor Intelligence", "___ Intelligence", 28, "Naming candidate", "Only one of fifteen with a worked positioning statement. Overlaps existing Ministry Intelligence."),
       ("Church Intelligence", "___ Intelligence", 24, "Naming candidate", "Coined in the same paragraph as its two siblings."),
       ("LifeTogether Intelligence", "___ Intelligence", 21, "Naming candidate", "Describes the real 25-year corpus; the name is new."),
       ("Ministry Intelligence", "___ Intelligence", 6, "Existing positioning", "The incumbent the other three have to beat."),
       ("Eleven one-mention Intelligence coinages", "___ Intelligence", 11, "Discard unless revived", "Discipleship, Biblical, Practice, Health, Group, Values, Stewardship, Leadership, Generation, Churchwide, Campaign."),
       ("The Trusted Guide Library™", "Trusted Guide", 3, "Naming candidate", "Shortest and strongest of the three wrappers."),
       ("The Trusted Guide Stewardship Library", "Trusted Guide", 1, "Alternate", "More descriptive, harder to say."),
       ("Trusted Guide Platform", "Trusted Guide", 8, "Alternate", "Used interchangeably with Library in the same passages."),
       ("Family Legacy Ministry", "Ministry sites", 62, "In use in source", "Brett flags in his own turn that this may worry Tom Conway."),
       ("Financial Wisdom Ministry", "Ministry sites", 31, "In use in source", "Consistent with existing Financial Wisdom Ministry work."),
       ("Generosity Ministry", "Ministry sites", 10, "In use in source", "He owns generosityministry.com."),
       ("LifeTogether Productions", "LifeTogether", 1, "Open question", "He asks what distinguishes it from LifeTogether; the file never answers.")]
for c, (h, w) in enumerate(zip(["Coined Name", "Family", "Mentions in source", "Status", "Notes"], [36, 22, 16, 24, 60]), start=1):
    cell = nc.cell(row=1, column=c, value=h)
    cell.font = Font(name="Arial", size=10, bold=True, color="FFFFFF"); cell.fill = PatternFill("solid", fgColor=NAVY)
    cell.alignment = Alignment(wrap_text=True, vertical="center", horizontal="center")
    nc.column_dimensions[get_column_letter(c)].width = w
for i, vals in enumerate(NCR, start=2):
    for c, v in enumerate(vals, start=1):
        cell = nc.cell(row=i, column=c, value=v)
        cell.font = Font(name="Arial", size=10, bold=(c == 1))
        cell.alignment = Alignment(wrap_text=True, vertical="top", horizontal="center" if c == 3 else "left")
        cell.border = Border(left=thin, right=thin, top=thin, bottom=thin)
    nc.row_dimensions[i].height = 40
nc.auto_filter.ref = f"A1:E{len(NCR) + 1}"; nc.freeze_panes = "A2"

rf = wb.create_sheet("RIGHTS FLAGS")
RFR = [("Purpose Driven / 40 Days of Purpose / PDL", 72, "Saddleback / Rick Warren", "Format and cadence Brett wants matched.", "Format reference. Never a title row."),
       ("Ron Blue", 64, "Ron Blue / RBI", "Voice, transcripts and theological spine of the financial track.", "Every derived title carries an RBI flag."),
       ("Master Your Money", 10, "Ron Blue (published book)", "Named as the 'HOW' layer and as a curriculum gap.", "Related asset row only."),
       ("Generous Living", 5, "Ron Blue / ambiguous", "Used as a LifeTogether curriculum name in two places.", "Rights call before it anchors a line."),
       ("Journey of Generosity", 6, "Generous Giving", "The source advises complementing it, not copying it.", "Partner asset. Archived as a title."),
       ("LifeWay", 8, "LifeWay", "The original Bible study structure under God Owns It All.", "Note the dependency on the parent row."),
       ("The Signatry", 23, "The Signatry", "Explored as a subscription partner.", "Prospective opportunity. Not a partnership."),
       ("Tom Conway / Family Legacy by Design", 7, "Tom Conway", "Brett asks how Family Legacy Ministry avoids taking concepts Tom developed.", "Every 'Family Legacy' title is flagged partner-sensitive."),
       ("Paul Black / WCM", 3, "WCM", "Named as a route to legacy families.", "Relationship, not a channel."),
       ("C12 / Convene / FCCI / CBMC / NCF / Kingdom Advisors", 12, "Various", "Affinity organizations that could carry resources.", "Distribution prospects. No titles attach yet."),
       ("™ symbols", 143, "Nobody yet", "80 distinct names carry ™, including 'Design™' and 'Assets™'.", "Strip on import; re-apply after clearance.")]
for c, (h, w) in enumerate(zip(["Third-party name or asset", "Mentions", "Whose it is", "How this file uses it", "Import rule"], [30, 12, 30, 50, 44]), start=1):
    cell = rf.cell(row=1, column=c, value=h)
    cell.font = Font(name="Arial", size=10, bold=True, color="FFFFFF"); cell.fill = PatternFill("solid", fgColor="9E2A2B")
    cell.alignment = Alignment(wrap_text=True, vertical="center", horizontal="center")
    rf.column_dimensions[get_column_letter(c)].width = w
for i, vals in enumerate(RFR, start=2):
    for c, v in enumerate(vals, start=1):
        cell = rf.cell(row=i, column=c, value=v)
        cell.font = Font(name="Arial", size=10, bold=(c == 1))
        cell.alignment = Alignment(wrap_text=True, vertical="top", horizontal="center" if c == 2 else "left")
        cell.border = Border(left=thin, right=thin, top=thin, bottom=thin)
    rf.row_dimensions[i].height = 40
rf.auto_filter.ref = f"A1:E{len(RFR) + 1}"; rf.freeze_panes = "A2"

wb.move_sheet("LISTS", offset=6)
out = "/home/claude/mtl/Master_Title_Library_v1_PHASE1.xlsx"
wb.save(out)
print("titles:", len(titles), "taxonomy:", len(taxo))
print(Counter(r['q'] for r in titles))
print(Counter(r['plat'] for r in titles).most_common(8))
print("saved", out)
