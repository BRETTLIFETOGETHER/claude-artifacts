import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.formatting.rule import FormulaRule

SRC = "Big Big brett master lifetogether campaign platform (ChatGPT, 7/4/26)"
URL = "https://chatgpt.com/g/g-p-6854e87c7fd881919afc69ee813e65e1/c/6967ed51-42b0-832c-9447-cc9d35e9a8d0"

NAVY = "1F3864"; LIGHTNAVY = "D9E2F3"; BAND = "F2F5FA"
GREEN = "C6EFCE"; BLUE = "DDEBF7"; ORANGE = "FCE4D6"; PURPLE = "E4DFEC"; GREY = "E7E6E6"; RED = "FFC7CE"; YELLOW = "FFF2CC"

wb = openpyxl.Workbook()

# ---------------------------------------------------------------- LISTS
lists = wb.active; lists.title = "LISTS"
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
lists["A1"] = "Dropdown vocabularies — edit here and every dropdown in the workbook updates."
lists["A1"].font = Font(name="Arial", size=10, italic=True, color="7F7F7F")
for c, (head, vals) in enumerate(VOCAB.items(), start=1):
    cell = lists.cell(row=2, column=c, value=head)
    cell.font = Font(name="Arial", size=10, bold=True, color="FFFFFF")
    cell.fill = PatternFill("solid", fgColor=NAVY)
    cell.alignment = Alignment(wrap_text=True, vertical="center")
    for r, v in enumerate(vals, start=3):
        vc = lists.cell(row=r, column=c, value=v)
        vc.font = Font(name="Arial", size=10)
    lists.column_dimensions[get_column_letter(c)].width = 34
lists.freeze_panes = "A3"

def vrange(head):
    c = get_column_letter(list(VOCAB).index(head) + 1)
    n = len(VOCAB[head]) + 2
    return f"=LISTS!${c}$3:${c}${n}"

# ---------------------------------------------------------------- MASTER LIBRARY
ws = wb.create_sheet("MASTER LIBRARY")
HEADERS = ["ID", "Keep / Review / Archive", "Level", "Original Title", "Original Subtitle", "Recommended Title",
           "Recommended Subtitle", "Parent / Belongs To", "Slot", "Version Status", "Source-Stated Platform",
           "Proposed Platform (inference)", "Primary Audience", "Content Type", "Topic / Category", "Secondary Topics",
           "Title Family / Duplicate Group", "Quality / Readiness", "Existing vs Concept", "Originator",
           "Rights / Ownership Flag", "Source", "Source Line", "Source Link", "Source Context / Notes", "AI Notes",
           "HUMAN DECISION"]
WIDTHS = [10, 15, 20, 40, 46, 30, 34, 28, 12, 24, 22, 26, 24, 20, 20, 26, 24, 30, 20, 28, 32, 34, 11, 30, 56, 56, 22]

R = []  # rows
def row(**k):
    R.append([k.get(h, "") for h in
              ["id","keep","level","title","sub","rtitle","rsub","parent","slot","ver","splat","pplat","aud","ctype",
               "topic","sec","fam","q","exist","orig","rights","src","line","link","ctx","ai","dec"]])

C_ = dict(src=SRC, link=URL)

row(id="MTL-0001", keep="Review", level="Curriculum / Series", title="God Owns It All",
    parent="Financial Wisdom Ministry", ver="Only version in source", splat="Not stated in source",
    pplat="Financial Wisdom Ministry", aud="Church", ctype="Curriculum", topic="Stewardship", sec="Money; Generosity; Legacy",
    fam="GOD-OWNS-IT-ALL", q="A — Strong / Ready", exist="Existing / Confirmed", orig="Existing asset referenced",
    rights="RBI / client work — confirm rights", line=104,
    ctx="Source calls this the most mature asset: complete 6-session curriculum, leader guides, Ron's recorded transcripts, learning objectives, built on the original LifeWay study structure.",
    ai="The only asset in this file the source treats as finished. Everything else is downstream of it. Rights sit with RBI/Ron Blue and partly with LifeWay — confirm before listing it as a LifeTogether title.", **C_)

row(id="MTL-0002", keep="Review", level="Book / Chapter", title="Master Your Money",
    parent="Ron Blue (author)", ver="Only version in source", splat="Not stated in source", pplat="Unclear / Needs Review",
    aud="Individual Christian", ctype="Book", topic="Money", sec="Stewardship", fam="MASTER-YOUR-MONEY",
    q="D — Good But Better for Another Platform", exist="Existing / Confirmed", orig="Third-party owned",
    rights="Third-party owned — do not publish", line=61,
    ctx="Referenced as Ron Blue's existing book (6th edition) and as the 'HOW' layer of the ecosystem; source says the video scripts drifted from it.",
    ai="This is a published third-party title, not ours to name a product after. Keep it in the library as a RELATED ASSET row so we can map dependencies, not as a candidate title.", **C_)

row(id="MTL-0003", keep="Review", level="Curriculum / Series", title="Generous Living",
    sub="Turning a Weekend Experience into a Lifetime of Stewardship", parent="Generosity Ministry",
    ver="Competing subtitle", splat="Not stated in source", pplat="Generosity Ministry", aud="Individual Christian",
    ctype="Curriculum", topic="Generosity", sec="Stewardship", fam="GENEROUS-LIVING", q="B — Strong Concept / Needs Polish",
    exist="Appears Existing", orig="AI-generated on request", rights="Third-party adjacent — position around it", line=4825,
    ctx="Positioned as the follow-on to a Generous Giving weekend experience.",
    ai="Generous Living is also a Ron Blue title. Same words, three possible owners in this file — needs a rights call before it anchors a line.", **C_)

row(id="MTL-0004", keep="Review", level="Curriculum / Series", title="Generous Living",
    sub="Discovering the Joy of Open-Handed Stewardship", parent="Generosity Ministry", ver="Competing subtitle",
    splat="Not stated in source", pplat="Generosity Ministry", aud="Individual Christian", ctype="Curriculum",
    topic="Generosity", fam="GENEROUS-LIVING", q="C — Duplicate / Alternate", exist="Brainstorming",
    orig="AI-generated on request", rights="Third-party adjacent — position around it", line=14951,
    ctx="Generated ~10,000 lines later in a different list, with no reference back to the earlier subtitle.",
    ai="Same title, second subtitle, no awareness of the first. This is the dominant duplication pattern in the file — subtitle churn under a stable title, not competing titles.", **C_)

row(id="MTL-0005", keep="Review", level="Campaign", title="40 Days of Financial Wisdom",
    sub="God Owns It All — A 40-Day Journey to Peace, Purpose, and Practical Stewardship",
    parent="God Owns It All", ver="Competing subtitle", splat="Not stated in source", pplat="Financial Wisdom Ministry",
    aud="Church", ctype="Campaign", topic="Stewardship", sec="Money; Generosity", fam="40-DAYS-FINANCIAL-WISDOM",
    q="B — Strong Concept / Needs Polish", exist="Proposed", orig="AI-generated on request",
    rights="RBI / client work — confirm rights", line=3533,
    ctx="Requested by Brett as a day-by-day outline with title, subtitle and big idea for each day.",
    ai="Uses the curriculum name as the subtitle. Decide which is the brand: is the campaign 'God Owns It All' with a 40-day format, or '40 Days of Financial Wisdom' built on the curriculum? The file never resolves this.", **C_)

row(id="MTL-0006", keep="Review", level="Campaign", title="40 Days of Financial Wisdom",
    sub="Discovering Peace, Purpose, and Freedom When God Owns It All", parent="God Owns It All",
    ver="Competing subtitle", splat="Not stated in source", pplat="Financial Wisdom Ministry", aud="Church",
    ctype="Campaign", topic="Stewardship", fam="40-DAYS-FINANCIAL-WISDOM", q="C — Duplicate / Alternate",
    exist="Proposed", orig="AI-generated on request", rights="RBI / client work — confirm rights", line=3748,
    ctx="Second subtitle produced ~200 lines after the first.",
    ai="Canonical subtitle needs picking. Recommend the shorter one; 'Peace, Purpose, and Practical Stewardship' has three nouns doing the work of one.", **C_)

row(id="MTL-0007", keep="Archive", level="Campaign", title="40 Days of Purpose", parent="Saddleback / Purpose Driven",
    ver="Only version in source", splat="Not stated in source", pplat="Unclear / Needs Review", aud="Church",
    ctype="Campaign", topic="Purpose", fam="40-DAYS-PURPOSE", q="E — Archive / Probably Don't Use",
    exist="Existing / Confirmed", orig="Third-party owned", rights="Third-party owned — do not publish", line=397,
    ctx="Brett asks for the devotional to be written 'in a style like the 40 days of purpose campaigns and the pdl' — used as a format reference throughout.",
    ai="Referenced 13 times as a model, never as a product we'd publish. It belongs in a FORMAT REFERENCE list, not the title library — otherwise a future search returns it as an available title.", **C_)

row(id="MTL-0008", keep="Archive", level="Campaign", title="Journey of Generosity", parent="Generous Giving",
    ver="Only version in source", splat="Not stated in source", pplat="Generosity Ministry", aud="Individual Christian",
    ctype="Journey", topic="Generosity", fam="JOURNEY-OF-GENEROSITY", q="E — Archive / Probably Don't Use",
    exist="Existing / Confirmed", orig="Third-party owned", rights="Third-party owned — do not publish", line=4820,
    ctx="Brett asked whether Generous Giving would want Journey of Generosity; the source answered that it is their flagship brand and recommended complementing it rather than copying it.",
    ai="The source already made this call. Capture it as a partner asset we build the next step for, not a title we own.", **C_)

row(id="MTL-0009", keep="Review", level="Campaign", title="40 Days of Worship",
    sub="Learning to Love God with Your Whole Life", parent="Biblical Purpose Library", ver="Latest in source",
    splat="Not stated in source", pplat="40 Day Campaigns", aud="Church", ctype="Campaign", topic="Worship",
    sec="Spiritual Growth; Discipleship", fam="40-DAYS-FIVE-PURPOSES", q="B — Strong Concept / Needs Polish",
    exist="Appears Existing", orig="AI-generated on request", rights="LifeTogether — clear", line=19241,
    ctx="One of the five biblical purposes set generated in response to 'build 10 title subtitle under each'.",
    ai="Almost certainly overlaps existing Biblical Purpose Library and 40 Day Campaign catalog entries. Do not import until this file is deduped against those two catalogs — otherwise the library gains a second 40 Days of Worship.", **C_)

row(id="MTL-0010", keep="Review", level="Campaign", title="40 Days of Worship", sub="Making Every Day an Offering to God",
    parent="Biblical Purpose Library", ver="Competing subtitle", splat="Not stated in source", pplat="40 Day Campaigns",
    aud="Church", ctype="Campaign", topic="Worship", fam="40-DAYS-FIVE-PURPOSES", q="C — Duplicate / Alternate",
    exist="Brainstorming", orig="AI-generated on request", rights="LifeTogether — clear", line=19633,
    ctx="Explicitly generated as one of 'Top 3 subtitle/angle options' for the same campaign.",
    ai="Deliberate option, not a duplicate. Options like these should live in a SUBTITLE OPTIONS block attached to the parent row, not as sibling rows that inflate the count.", **C_)

row(id="MTL-0011", keep="Review", level="Campaign", title="40 Days of Fellowship",
    sub="Building Authentic Community in a Lonely World", parent="Biblical Purpose Library", ver="Competing subtitle",
    splat="Not stated in source", pplat="40 Day Campaigns", aud="Church", ctype="Campaign", topic="Small Groups",
    sec="Church Health; Discipleship", fam="40-DAYS-FIVE-PURPOSES", q="B — Strong Concept / Needs Polish",
    exist="Appears Existing", orig="AI-generated on request", rights="LifeTogether — clear", line=19087,
    ctx="Alternate subtitle to the descriptive line at 19073 ('a churchwide journey to help people move from attendance to authentic biblical community').",
    ai="'Lonely World' is the strongest felt-need framing in the five-purpose set. Worth testing as the pattern for all five.", **C_)

row(id="MTL-0012", keep="Review", level="Day / Devotional", title="DAY 1 — The Question Beneath Every Other Question",
    parent="40 Days of Financial Wisdom", slot="Day 1", ver="Superseded draft", splat="Not stated in source",
    pplat="Financial Wisdom Ministry", aud="Individual Christian", ctype="Devotional", topic="Stewardship",
    fam="GOIA-DAY-01", q="C — Duplicate / Alternate", exist="Proposed", orig="AI-generated on request",
    rights="RBI / client work — confirm rights", line=175,
    ctx="First draft of Day 1, written before the Option B session reorder.",
    ai="Day 1 exists in 17 instances and 10 distinct titles across this file. Version, not variant.", **C_)

row(id="MTL-0013", keep="Review", level="Day / Devotional", title="DAY 1 — Ownership Changes the Pressure",
    sub="When ownership changes hands, the weight shifts to the Owner.", parent="40 Days of Financial Wisdom",
    slot="Day 1", ver="Latest in source", splat="Not stated in source", pplat="Financial Wisdom Ministry",
    aud="Individual Christian", ctype="Devotional", topic="Stewardship", fam="GOIA-DAY-01",
    q="B — Strong Concept / Needs Polish", exist="Proposed", orig="AI-generated on request",
    rights="RBI / client work — confirm rights", line=3539,
    ctx="Appears in the final title/subtitle/big-idea outline Brett requested for the 40-day track.",
    ai="Latest by document order, which is the only recency signal this file gives us. If a later chat revised Day 1 again, this row is wrong — which is why every row needs a source date.", **C_)

row(id="MTL-0014", keep="Review", level="Day / Devotional", title="DAY 1 — God Is the Owner. You're the Manager.",
    parent="40 Days of Financial Wisdom", slot="Day 1", ver="Superseded draft", splat="Not stated in source",
    pplat="Financial Wisdom Ministry", aud="Individual Christian", ctype="Devotional", topic="Stewardship",
    fam="GOIA-DAY-01", q="C — Duplicate / Alternate", exist="Proposed", orig="AI-generated on request",
    rights="RBI / client work — confirm rights", line=424,
    ctx="Rewritten in 'Ron Blue voice' after Brett asked for the PDL format in Ron's voice.",
    ai="Strongest plain-language version of the three. Worth reconsidering as canonical even though it is not the latest.", **C_)

row(id="MTL-0015", keep="Review", level="Day / Devotional", title="DAY 2 — You Are a Steward, Not an Owner",
    sub="Faithfulness is God's standard, not perfection.", parent="40 Days of Financial Wisdom", slot="Day 2",
    ver="Latest in source", splat="Not stated in source", pplat="Financial Wisdom Ministry", aud="Individual Christian",
    ctype="Devotional", topic="Stewardship", fam="GOIA-DAY-02", q="B — Strong Concept / Needs Polish", exist="Proposed",
    orig="AI-generated on request", rights="RBI / client work — confirm rights", line=3542,
    ctx="Day 2 of the final outline; earlier drafts used 'Why Ownership Changes Everything' and 'The Finish Line You Never Set'.",
    ai="Eight distinct Day 2 titles across the file.", **C_)

row(id="MTL-0016", keep="Review", level="Day / Devotional", title="Day 3: Our Church Story",
    parent="Unclear / Needs Review", slot="Day 3", ver="Needs version check", splat="Not stated in source",
    pplat="Unclear / Needs Review", aud="Church", ctype="Devotional", topic="Church Health", fam="CHURCH-STORY-DAY-03",
    q="F — Human Review Needed", exist="Brainstorming", orig="AI-generated on request", rights="LifeTogether — clear",
    line=23487,
    ctx="Appears in a church-vision/values day list near the end of the file, unrelated to the financial track.",
    ai="Same slot number as three other Day 3 titles from a different campaign. Slot numbers only mean something with a parent attached — any dedupe keyed on 'Day 3' alone will merge unrelated campaigns.", **C_)

row(id="MTL-0017", keep="Review", level="Curriculum / Series", title="Preparing Responsible Heirs",
    sub="Building Character Before Wealth", parent="Family Legacy series set", ver="Competing subtitle",
    splat="Not stated in source", pplat="Family Legacy Ministry", aud="Legacy Family", ctype="Curriculum",
    topic="Family Legacy", sec="Parenting; Stewardship", fam="PREPARING-RESPONSIBLE-HEIRS",
    q="B — Strong Concept / Needs Polish", exist="Proposed", orig="AI-generated on request", rights="Needs rights review",
    line=4005, ctx="From the 'top 10 series families and Christian financial advisors would want' list.",
    ai="Strongest title in the family legacy set. Three different subtitles for it appear in this file alone.", **C_)

row(id="MTL-0018", keep="Review", level="Curriculum / Series", title="Preparing Responsible Heirs",
    sub="Character Before Capital", parent="Family Legacy series set", ver="Competing subtitle",
    splat="Not stated in source", pplat="Family Legacy Ministry", aud="Legacy Family", ctype="Curriculum",
    topic="Family Legacy", fam="PREPARING-RESPONSIBLE-HEIRS", q="C — Duplicate / Alternate", exist="Proposed",
    orig="AI-generated on request", rights="Needs rights review", line=4172,
    ctx="Second subtitle, generated in a later expansion of the same list.",
    ai="'Character Before Capital' is the sharper line for an advisor audience; 'Before Wealth' is warmer for families. This is an edition decision, not a duplicate to delete.", **C_)

row(id="MTL-0019", keep="Review", level="Curriculum / Series", title="Preparing Responsible Heirs",
    sub="Building Character Before Capital", parent="Family Legacy series set", ver="Competing subtitle",
    splat="Not stated in source", pplat="Family Legacy Ministry", aud="Legacy Family", ctype="Curriculum",
    topic="Family Legacy", fam="PREPARING-RESPONSIBLE-HEIRS", q="C — Duplicate / Alternate", exist="Proposed",
    orig="AI-generated on request", rights="Needs rights review", line=4300,
    ctx="Third subtitle — a blend of the first two.",
    ai="Three near-identical subtitles produced 300 lines apart with no memory of each other. Canonical pick needed before any of this reaches a website.", **C_)

row(id="MTL-0020", keep="Review", level="Curriculum / Series", title="Family Stewardship",
    sub="Building a Family That Manages God's Resources Together", parent="Family Legacy series set",
    ver="Latest in source", splat="Not stated in source", pplat="Family Legacy Ministry", aud="Family",
    ctype="Curriculum", topic="Family Legacy", sec="Stewardship; Parenting", fam="FAMILY-STEWARDSHIP",
    q="A — Strong / Ready", exist="Proposed", orig="Brett-selected (endorsed in his turn)", rights="Needs rights review",
    line=3949, ctx="Appears inside Brett's own message, quoted back with the note that parents immediately understand it.",
    ai="One of the few titles in this file that passed through Brett's hands rather than being generated at him. Treat that as a stronger signal than any quality rating.", **C_)

row(id="MTL-0021", keep="Review", level="Tool / Asset", title="The Family Legacy Roadmap™",
    parent="Family Legacy by Design", ver="Only version in source", splat="Not stated in source",
    pplat="Family Legacy by Design", aud="Legacy Family", ctype="Tool", topic="Family Legacy", sec="Stewardship",
    fam="FAMILY-LEGACY-ROADMAP", q="B — Strong Concept / Needs Polish", exist="Proposed", orig="AI-generated on request",
    rights="Trademark unverified (™ applied in draft)", line=7017,
    ctx="Described as a personalized living roadmap tracking a family across 10–20 years; called a seventh pillar no one else offers.",
    ai="The ™ was applied in draft output, not by counsel. 143 ™ marks across 80 names appear in this file, including malformed ones like 'Design™'. Strip every ™ on import and re-apply only after a real clearance decision.", **C_)

row(id="MTL-0022", keep="Review", level="Tool / Asset", title="Preparing Responsible Heirs™",
    sub="A birth-to-adulthood development roadmap for the next generation.", parent="Family Legacy by Design",
    ver="Competing name for same asset", splat="Not stated in source", pplat="Family Legacy by Design",
    aud="Financial Advisor", ctype="Tool", topic="Family Legacy", fam="PREPARING-RESPONSIBLE-HEIRS",
    q="F — Human Review Needed", exist="Proposed", orig="AI-generated on request",
    rights="Trademark unverified (™ applied in draft)", line=7659,
    ctx="Listed as an advisor tool in the platform tool set.",
    ai="Same name as MTL-0017 but at a different level — a six-session series in one place, a trademarked advisor tool in another. Level conflation like this is the reason the library needs a Level column; without it, one name silently becomes two products.", **C_)

row(id="MTL-0023", keep="Review", level="Assessment", title="Family Stewardship Assessment™",
    sub="A 10-minute diagnostic that identifies strengths and growth areas in ownership, communication, generosity, and heir readiness.",
    parent="Christian Advisor Network", ver="Latest in source", splat="Not stated in source",
    pplat="Christian Advisor Network", aud="Financial Advisor", ctype="Assessment", topic="Family Legacy",
    sec="Stewardship; Generosity", fam="FAMILY-STEWARDSHIP-ASSESSMENT", q="A — Strong / Ready", exist="Proposed",
    orig="Brett-selected (endorsed in his turn)", rights="Trademark unverified (™ applied in draft)", line=7191,
    ctx="Brett describes the same 10-minute family diagnostic in his own message at line 6686 and returns to it repeatedly as the advisor's entry point.",
    ai="Overlaps the existing Ten-Minute Family Legacy Assessment in Family Legacy Intelligence. Check whether this is a second name for the same instrument before it ships under two names.", **C_)

row(id="MTL-0024", keep="Review", level="Platform / Brand", title="The Trusted Guide Library™",
    sub="Equipping the trusted guides who disciple the world's most influential Christian families.",
    parent="Christian Advisor Network", ver="Competing name for same asset", splat="Not stated in source",
    pplat="Christian Advisor Network", aud="Trusted Guide (multi-profession)", ctype="Website / Brand",
    topic="Family Legacy", sec="Stewardship; Leadership", fam="TRUSTED-GUIDE-BRAND", q="B — Strong Concept / Needs Polish",
    exist="Proposed", orig="AI-generated on request", rights="Trademark unverified (™ applied in draft)", line=6313,
    ctx="Emerged after Brett wrote that he is creating the discipleship library for every trusted guide who serves affluent Christian families.",
    ai="'Trusted guide' is the most durable idea in this file — it names the buyer across advisors, attorneys, CPAs, family offices and pastors. The brand wrapper around it is unsettled: Library, Stewardship Library, and Platform all appear.", **C_)

row(id="MTL-0025", keep="Review", level="Platform / Brand", title="The Trusted Guide Stewardship Library",
    sub="Premium discipleship resources for advisors, pastors, attorneys, CPAs, family offices, and generosity leaders.",
    parent="Christian Advisor Network", ver="Competing name for same asset", splat="Not stated in source",
    pplat="Christian Advisor Network", aud="Trusted Guide (multi-profession)", ctype="Website / Brand",
    topic="Family Legacy", fam="TRUSTED-GUIDE-BRAND", q="C — Duplicate / Alternate", exist="Brainstorming",
    orig="AI-generated on request", rights="Needs rights review", line=6193,
    ctx="Appears 120 lines before the shorter version, in the same brand-development stretch.",
    ai="Two names for one asset, minutes apart. Belongs in NAMING CANDIDATES until Brett picks; carrying both in the master library implies two products exist.", **C_)

row(id="MTL-0026", keep="Review", level="Platform / Brand", title="Pastor Intelligence",
    sub="Turns your passive sermon library into a scalable ministry platform.", parent="Pastor's Library",
    ver="Latest in source", splat="Not stated in source", pplat="Pastor's Library", aud="Senior Pastor",
    ctype="Website / Brand", topic="Church Health", sec="Discipleship; Small Groups", fam="INTELLIGENCE-BRANDS",
    q="B — Strong Concept / Needs Polish", exist="Proposed", orig="AI-generated on request", rights="Needs rights review",
    line=21681,
    ctx="Positioned at the end of the file as one leg of a three-part stack with Church Intelligence and LifeTogether Intelligence.",
    ai="Strongest of the fifteen '___ Intelligence' coinages in this file, and the only one with a worked positioning statement. Overlaps the existing Ministry Intelligence positioning — same idea, different name.", **C_)

row(id="MTL-0027", keep="Review", level="Platform / Brand", title="Church Intelligence",
    sub="The wisdom of the global church: biblical foundations, historic practices, current best thinking.",
    parent="Pastor's Library", ver="Latest in source", splat="Not stated in source", pplat="Pastor's Library",
    aud="Pastor / Church Leader", ctype="Website / Brand", topic="Church Health", fam="INTELLIGENCE-BRANDS",
    q="F — Human Review Needed", exist="Brainstorming", orig="AI-generated on request", rights="Needs rights review",
    line=21570,
    ctx="Second layer of the proposed three-part intelligence stack.",
    ai="Coined in the same paragraph as its two siblings. Fifteen '___ Intelligence' names appear in this file; twelve appear exactly once. Import them as naming candidates or the Platform column will be populated with brands that never existed.", **C_)

row(id="MTL-0028", keep="Review", level="Platform / Brand", title="LifeTogether Intelligence",
    sub="LifeTogether's 25+ years of campaign, curriculum, small group, devotional, video and publishing experience.",
    parent="Life Together / Church", ver="Latest in source", splat="Not stated in source", pplat="Life Together / Church",
    aud="Multiple", ctype="Website / Brand", topic="Discipleship", fam="INTELLIGENCE-BRANDS",
    q="F — Human Review Needed", exist="Brainstorming", orig="AI-generated on request", rights="Needs rights review",
    line=21572, ctx="Third layer of the proposed stack, describing the existing LifeTogether corpus as a data asset.",
    ai="This one describes something real (the 25-year library) with a name that does not exist yet. Separate the asset from the brand before deciding.", **C_)

row(id="MTL-0029", keep="Review", level="Training", title="The Trusted Guide Facilitator Manual™",
    sub="A complete guide for advisors, pastors, attorneys and family office leaders.", parent="Christian Advisor Network",
    ver="Only version in source", splat="Not stated in source", pplat="Christian Advisor Network",
    aud="Trusted Guide (multi-profession)", ctype="Training", topic="Family Legacy", sec="Leadership",
    fam="TRUSTED-GUIDE-BRAND", q="B — Strong Concept / Needs Polish", exist="Proposed", orig="AI-generated on request",
    rights="Trademark unverified (™ applied in draft)", line=7665,
    ctx="Listed eighth in the platform tool set; the source argues it is the hardest piece for a competitor to replicate.",
    ai="Brett pasted this list back into the conversation at line 8110 and asked for one-page editions, which is the closest thing to endorsement in this file.", **C_)

row(id="MTL-0030", keep="Review", level="Tool / Asset", title="Family Meeting Toolkit",
    parent="Christian Advisor Network", ver="Needs version check", splat="Not stated in source",
    pplat="Christian Advisor Network", aud="Financial Advisor", ctype="Tool", topic="Family Legacy",
    sec="Relationships", fam="FAMILY-MEETING-TOOLKIT", q="B — Strong Concept / Needs Polish", exist="Proposed",
    orig="Brett-selected (endorsed in his turn)", rights="Trademark unverified (™ applied in draft)", line=6553,
    ctx="Appears 20 times across the file, including in Brett's own list of flagship advisor resources at line 6863.",
    ai="Casing drifts across instances (Family meeting toolkit / family meeting toolkit / Family Meeting Toolkit™). Normalize casing on import and record it as one row, not twenty.", **C_)

row(id="MTL-0031", keep="Archive", level="Fragment / Not a Title",
    title="The finish line you never set (this is OK here because finish lines start with", parent="40 Days of Financial Wisdom",
    slot="Day 2", ver="Needs version check", splat="Not stated in source", pplat="Unclear / Needs Review",
    aud="Unclear", ctype="Unknown", topic="Stewardship", fam="GOIA-DAY-02", q="E — Archive / Probably Don't Use",
    exist="Unclear", orig="AI-generated on request", rights="LifeTogether — clear", line=650,
    ctx="A day title with the model's parenthetical reasoning attached, wrapped mid-sentence by the export.",
    ai="Included deliberately as a specimen. A regex-only extraction pulls thousands of these; every row needs the raw source line kept so a human can tell a title from a sentence fragment.", **C_)

row(id="MTL-0032", keep="Review", level="Campaign", title="40 Days of Whole-Life Faith",
    sub="Following Jesus with Your Worship, Relationships, Character, Gifts, and Influence",
    parent="Biblical Purpose Library", ver="Latest in source", splat="Not stated in source", pplat="40 Day Campaigns",
    aud="Church", ctype="Campaign", topic="Discipleship", sec="Purpose; Spiritual Growth", fam="40-DAYS-FIVE-PURPOSES",
    q="A — Strong / Ready", exist="Proposed", orig="AI-generated on request", rights="LifeTogether — clear", line=18434,
    ctx="Generated in the five-purposes campaign set; the subtitle names all five purposes in one line.",
    ai="The clearest campaign-level expression of the five purposes in this file, and the natural umbrella over the five individual campaigns.", **C_)

# write header + rows
for c, h in enumerate(HEADERS, start=1):
    cell = ws.cell(row=1, column=c, value=h)
    cell.font = Font(name="Arial", size=10, bold=True, color="FFFFFF")
    cell.fill = PatternFill("solid", fgColor=NAVY)
    cell.alignment = Alignment(wrap_text=True, vertical="center", horizontal="center")
    ws.column_dimensions[get_column_letter(c)].width = WIDTHS[c-1]
ws.row_dimensions[1].height = 46

thin = Side(style="thin", color="BFBFBF")
for r, vals in enumerate(R, start=2):
    for c, v in enumerate(vals, start=1):
        cell = ws.cell(row=r, column=c, value=v)
        cell.font = Font(name="Arial", size=10)
        cell.alignment = Alignment(wrap_text=True, vertical="top")
        cell.border = Border(left=thin, right=thin, top=thin, bottom=thin)
    ws.cell(row=r, column=4).font = Font(name="Arial", size=10, bold=True)
    ws.cell(row=r, column=27).fill = PatternFill("solid", fgColor=YELLOW)
    ws.row_dimensions[r].height = 62

LAST = 600
ws.auto_filter.ref = f"A1:AA{LAST}"
ws.freeze_panes = "D2"

# dropdowns
DV = {"B": "Keep / Review / Archive", "C": "Level", "J": "Version Status", "K": "Platform / Brand",
      "L": "Platform / Brand", "M": "Primary Audience", "N": "Content Type", "R": "Quality / Readiness",
      "S": "Existing vs Concept", "T": "Originator", "U": "Rights / Ownership"}
for col, head in DV.items():
    dv = DataValidation(type="list", formula1=vrange(head).replace("=", ""), allow_blank=True, showDropDown=False)
    ws.add_data_validation(dv)
    dv.add(f"{col}2:{col}{LAST}")

rng = f"A2:AA{LAST}"
ws.conditional_formatting.add(rng, FormulaRule(formula=[f'AND(MOD(ROW(),2)=0,$A2<>"")'], fill=PatternFill("solid", bgColor=BAND), stopIfTrue=False))
for letter, fill in [("A", GREEN), ("B", BLUE), ("C", ORANGE), ("D", PURPLE), ("E", GREY), ("F", RED)]:
    ws.conditional_formatting.add(f"R2:R{LAST}", FormulaRule(formula=[f'LEFT($R2,1)="{letter}"'], fill=PatternFill("solid", bgColor=fill)))
ws.conditional_formatting.add(f"U2:U{LAST}", FormulaRule(formula=['OR(ISNUMBER(SEARCH("Third-party",$U2)),ISNUMBER(SEARCH("Trademark",$U2)),ISNUMBER(SEARCH("Needs rights",$U2)))'], fill=PatternFill("solid", bgColor=RED)))
ws.conditional_formatting.add(f"S2:S{LAST}", FormulaRule(formula=['$S2="Existing / Confirmed"'], fill=PatternFill("solid", bgColor=GREEN)))
ws.conditional_formatting.add(f"C2:C{LAST}", FormulaRule(formula=['OR($C2="Platform / Brand",$C2="Product Line")'], fill=PatternFill("solid", bgColor=LIGHTNAVY)))
ws.conditional_formatting.add(f"C2:C{LAST}", FormulaRule(formula=['$C2="Fragment / Not a Title"'], fill=PatternFill("solid", bgColor=RED)))

# ---------------------------------------------------------------- SUMMARY
sm = wb.create_sheet("SUMMARY")
sm.column_dimensions["A"].width = 46; sm.column_dimensions["B"].width = 14
sm.column_dimensions["C"].width = 4;  sm.column_dimensions["D"].width = 46; sm.column_dimensions["E"].width = 14
def title_cell(ws_, cellref, text, size=14):
    ws_[cellref] = text
    ws_[cellref].font = Font(name="Arial", size=size, bold=True, color=NAVY)
def block(ws_, r, c, heading, pairs):
    hc = ws_.cell(row=r, column=c, value=heading)
    hc.font = Font(name="Arial", size=10, bold=True, color="FFFFFF")
    hc.fill = PatternFill("solid", fgColor=NAVY)
    ws_.cell(row=r, column=c+1).fill = PatternFill("solid", fgColor=NAVY)
    for i, (label, formula) in enumerate(pairs, start=1):
        a = ws_.cell(row=r+i, column=c, value=label); a.font = Font(name="Arial", size=10)
        b = ws_.cell(row=r+i, column=c+1, value=formula); b.font = Font(name="Arial", size=10)
        b.alignment = Alignment(horizontal="center")
        if i % 2 == 0:
            a.fill = PatternFill("solid", fgColor=BAND); b.fill = PatternFill("solid", fgColor=BAND)
    return r + len(pairs) + 2

M = "'MASTER LIBRARY'"
def cif(col, val): return f'=COUNTIF({M}!${col}$2:${col}${LAST},"{val}")'

title_cell(sm, "A1", "MASTER TITLE LIBRARY — SUMMARY")
sm["A2"] = f"Source in this build: {SRC}"
sm["A2"].font = Font(name="Arial", size=10, italic=True, color="7F7F7F")
sm["A3"] = "Yellow cells are yours: HUMAN DECISION on the master tab, and the Decision column on REVIEW QUEUE. Everything else is Claude-filled and re-derivable on the next ingest."
sm["A3"].font = Font(name="Arial", size=10, italic=True, color="7F7F7F")
sm["A4"] = "All counts below are live formulas over MASTER LIBRARY rows 2–600."
sm["A4"].font = Font(name="Arial", size=10, italic=True, color="7F7F7F")

r = 6
r = block(sm, r, 1, "TOTALS", [("Total title records", f'=COUNTA({M}!$A$2:$A${LAST})')] +
          [(v, cif("B", v)) for v in VOCAB["Keep / Review / Archive"]] +
          [("Needing human review (F)", cif("R", "F — Human Review Needed")),
           ("Duplicates / alternates / competing versions",
            f'=COUNTIF({M}!$J$2:$J${LAST},"Superseded draft")+COUNTIF({M}!$J$2:$J${LAST},"Competing subtitle")+COUNTIF({M}!$J$2:$J${LAST},"Competing name for same asset")+COUNTIF({M}!$J$2:$J${LAST},"Duplicate")')])
r = block(sm, r, 1, "BY QUALITY / READINESS", [(v, cif("R", v)) for v in VOCAB["Quality / Readiness"]])
r = block(sm, r, 1, "BY EXISTING VS CONCEPT", [(v, cif("S", v)) for v in VOCAB["Existing vs Concept"]])
r = block(sm, r, 1, "BY ORIGINATOR", [(v, cif("T", v)) for v in VOCAB["Originator"]])

r2 = 6
r2 = block(sm, r2, 4, "BY LEVEL", [(v, cif("C", v)) for v in VOCAB["Level"]])
r2 = block(sm, r2, 4, "BY PROPOSED PLATFORM / BRAND", [(v, cif("L", v)) for v in VOCAB["Platform / Brand"]])
r2 = block(sm, r2, 4, "BY PRIMARY AUDIENCE", [(v, cif("M", v)) for v in VOCAB["Primary Audience"]])
r2 = block(sm, r2, 4, "BY CONTENT TYPE", [(v, cif("N", v)) for v in VOCAB["Content Type"]])
r2 = block(sm, r2, 4, "BY RIGHTS / OWNERSHIP FLAG", [(v, cif("U", v)) for v in VOCAB["Rights / Ownership"]])
sm.freeze_panes = "A6"

# ---------------------------------------------------------------- REVIEW QUEUE
rq = wb.create_sheet("REVIEW QUEUE")
RQH = ["ID", "Original Title", "Level", "Why it is in the queue", "The decision you actually have to make", "DECISION", "Decided by / date"]
RQW = [10, 42, 22, 58, 66, 26, 20]
RQ = [
 ("MTL-0001", "God Owns It All", "Curriculum / Series", "Existing asset built with RBI, Ron Blue transcripts and LifeWay structure underneath it.",
  "Confirm what LifeTogether can publish, license or campaign-ify without a new agreement. Everything downstream inherits this answer."),
 ("MTL-0002", "Master Your Money", "Book / Chapter", "Third-party published title carried through the file as an ecosystem layer.",
  "Related asset row or out of the library entirely?"),
 ("MTL-0005", "40 Days of Financial Wisdom", "Campaign", "Two competing subtitles, and the campaign name competes with the curriculum name.",
  "Is the churchwide campaign called God Owns It All or 40 Days of Financial Wisdom? One is the brand, one is the format."),
 ("MTL-0008", "Journey of Generosity", "Campaign", "Generous Giving's flagship program name.",
  "Confirm we position around it rather than building anything under that name."),
 ("MTL-0009", "40 Days of Worship", "Campaign", "Almost certainly already exists in the Biblical Purpose Library and the 40 Day Campaign catalog.",
  "Dedupe this file against those two catalogs before import, or accept two of every five-purpose campaign."),
 ("MTL-0013", "DAY 1 — Ownership Changes the Pressure", "Day / Devotional", "Ten distinct Day 1 titles across 17 instances.",
  "Pick the canonical Day 1, or confirm 'latest in document order' is a good enough rule for day-level rows."),
 ("MTL-0016", "Day 3: Our Church Story", "Day / Devotional", "Slot number matches three other Day 3 titles from a different campaign; parent unknown.",
  "Name its parent campaign, or archive it."),
 ("MTL-0017", "Preparing Responsible Heirs", "Curriculum / Series", "Three competing subtitles in one file.",
  "Choose one, or declare 'Before Wealth' the family edition and 'Before Capital' the advisor edition."),
 ("MTL-0021", "The Family Legacy Roadmap™", "Tool / Asset", "™ applied in draft output; 80 distinct ™ names appear in this file.",
  "Which names, if any, go to a trademark search? Everything else loses the symbol."),
 ("MTL-0022", "Preparing Responsible Heirs™", "Tool / Asset", "Same name used as a six-session series and as an advisor tool.",
  "One name, one level. Which is it?"),
 ("MTL-0023", "Family Stewardship Assessment™", "Assessment", "Overlaps the existing Ten-Minute Family Legacy Assessment.",
  "Same instrument under a new name, or a genuinely different diagnostic?"),
 ("MTL-0024", "The Trusted Guide Library™", "Platform / Brand", "Three competing brand names for one asset within 120 lines.",
  "Pick the wrapper: Trusted Guide Library, Trusted Guide Stewardship Library, or Trusted Guide Platform."),
 ("MTL-0026", "Pastor Intelligence", "Platform / Brand", "Fifteen '___ Intelligence' coinages in this file; this one overlaps existing Ministry Intelligence positioning.",
  "Is Pastor Intelligence a rename of Ministry Intelligence, a product inside it, or a separate brand?"),
 ("MTL-0028", "LifeTogether Intelligence", "Platform / Brand", "Names a real asset (the 25-year library) with a brand that does not exist yet.",
  "Separate the asset from the brand before either goes on a site."),
 ("—", "Architecture questions Brett raised in this chat", "Platform / Brand",
  "Brett asks in his own turns what separates LifeTogether Productions from LifeTogether, whether these are separate websites on one platform, and how Family Legacy Ministry avoids stepping on Family Legacy by Design.",
  "The Platform column cannot be trusted until these are answered. Answer them once, here, and the whole library classifies cleanly."),
]
for c, h in enumerate(RQH, start=1):
    cell = rq.cell(row=1, column=c, value=h)
    cell.font = Font(name="Arial", size=10, bold=True, color="FFFFFF")
    cell.fill = PatternFill("solid", fgColor=NAVY)
    cell.alignment = Alignment(wrap_text=True, vertical="center", horizontal="center")
    rq.column_dimensions[get_column_letter(c)].width = RQW[c-1]
rq.row_dimensions[1].height = 34
for r_, vals in enumerate(RQ, start=2):
    for c, v in enumerate(list(vals) + ["", ""], start=1):
        cell = rq.cell(row=r_, column=c, value=v)
        cell.font = Font(name="Arial", size=10, bold=(c == 2))
        cell.alignment = Alignment(wrap_text=True, vertical="top")
        cell.border = Border(left=thin, right=thin, top=thin, bottom=thin)
    rq.cell(row=r_, column=6).fill = PatternFill("solid", fgColor=YELLOW)
    rq.cell(row=r_, column=7).fill = PatternFill("solid", fgColor=YELLOW)
    rq.row_dimensions[r_].height = 58
rq.auto_filter.ref = f"A1:G{len(RQ)+1}"
rq.freeze_panes = "B2"
rq.conditional_formatting.add(f"A2:G{len(RQ)+40}", FormulaRule(formula=['AND(MOD(ROW(),2)=0,$A2<>"")'], fill=PatternFill("solid", bgColor=BAND)))

# ---------------------------------------------------------------- NAMING CANDIDATES
nc = wb.create_sheet("NAMING CANDIDATES")
NCH = ["Coined Name", "Family", "Mentions in this source", "Distinct siblings coined alongside it", "Status", "Notes"]
NCW = [36, 24, 14, 20, 26, 66]
NCR = [
 ("Pastor Intelligence", "___ Intelligence", 28, 15, "Naming candidate", "Only one of the fifteen with a worked positioning statement. Overlaps existing Ministry Intelligence."),
 ("Church Intelligence", "___ Intelligence", 24, 15, "Naming candidate", "Coined in the same paragraph as its two siblings."),
 ("LifeTogether Intelligence", "___ Intelligence", 21, 15, "Naming candidate", "Describes the real 25-year corpus; the name itself is new."),
 ("Ministry Intelligence", "___ Intelligence", 6, 15, "Existing positioning", "Already in use as platform positioning — the incumbent the other three have to beat."),
 ("Discipleship / Biblical / Practice / Health / Group / Values / Stewardship / Leadership / Generation / Churchwide / Campaign Intelligence", "___ Intelligence", 11, 15, "Discard unless revived", "Eleven names, one mention each, all generated in the same stretch. Volume, not architecture."),
 ("The Trusted Guide Library™", "Trusted Guide", 3, 3, "Naming candidate", "Shortest and strongest of the three wrappers."),
 ("The Trusted Guide Stewardship Library", "Trusted Guide", 1, 3, "Alternate", "More descriptive, harder to say."),
 ("Trusted Guide Platform", "Trusted Guide", 8, 3, "Alternate", "Used interchangeably with Library in the same passages — decide whether it is a library or a platform."),
 ("Family Legacy Ministry", "Family Legacy", 62, 3, "In use in source", "Brett flags in his own turn that this may worry Tom Conway given Family Legacy by Design."),
 ("Financial Wisdom Ministry", "Ministry sites", 31, 3, "In use in source", "Consistent with the existing Financial Wisdom Ministry work."),
 ("Generosity Ministry", "Ministry sites", 10, 3, "In use in source", "Brett notes he owns generosityministry.com."),
 ("LifeTogether Productions", "LifeTogether", 1, 2, "Open question", "Brett asks in his own turn what distinguishes it from LifeTogether; the file never answers."),
]
for c, h in enumerate(NCH, start=1):
    cell = nc.cell(row=1, column=c, value=h)
    cell.font = Font(name="Arial", size=10, bold=True, color="FFFFFF")
    cell.fill = PatternFill("solid", fgColor=NAVY)
    cell.alignment = Alignment(wrap_text=True, vertical="center", horizontal="center")
    nc.column_dimensions[get_column_letter(c)].width = NCW[c-1]
for r_, vals in enumerate(NCR, start=2):
    for c, v in enumerate(vals, start=1):
        cell = nc.cell(row=r_, column=c, value=v)
        cell.font = Font(name="Arial", size=10, bold=(c == 1))
        cell.alignment = Alignment(wrap_text=True, vertical="top", horizontal="center" if c in (3, 4) else "left")
        cell.border = Border(left=thin, right=thin, top=thin, bottom=thin)
    nc.row_dimensions[r_].height = 44
nc.auto_filter.ref = f"A1:F{len(NCR)+1}"; nc.freeze_panes = "A2"
nc["A" + str(len(NCR)+3)] = "Mention counts are literal string counts in the source file. A name coined once, beside four alternatives, is an option — not a brand."
nc["A" + str(len(NCR)+3)].font = Font(name="Arial", size=10, italic=True, color="7F7F7F")

# ---------------------------------------------------------------- RIGHTS FLAGS
rf = wb.create_sheet("RIGHTS FLAGS")
RFH = ["Third-party name or asset", "Mentions in this source", "Whose it is", "How this file uses it", "Import rule"]
RFW = [30, 14, 34, 62, 50]
RFR = [
 ("Purpose Driven / 40 Days of Purpose / PDL", 72, "Saddleback / Rick Warren", "Used throughout as the format and cadence Brett wants matched.", "Format reference list. Never a title row."),
 ("Ron Blue", 64, "Ron Blue / RBI", "Voice, teaching transcripts, and the theological spine of the financial track.", "Every derived title carries an RBI rights flag."),
 ("Master Your Money", 10, "Ron Blue (published book)", "Named as the 'HOW' layer and as a gap in the curriculum.", "Related asset row only."),
 ("Generous Living", 5, "Ron Blue (published title) / ambiguous", "Used as a LifeTogether curriculum name in two places.", "Rights call before it anchors a line."),
 ("Journey of Generosity", 6, "Generous Giving", "The source explicitly advises complementing it, not copying it.", "Partner asset. Archive as a title."),
 ("LifeWay", 8, "LifeWay", "The original Bible study structure under God Owns It All.", "Note the dependency on the parent row."),
 ("The Signatry", 23, "The Signatry", "Explored as a subscription partner whose families would get access.", "Prospective opportunity. Not a partnership."),
 ("Tom Conway / Family Legacy by Design", 7, "Tom Conway", "Brett asks in his own turn how Family Legacy Ministry avoids taking concepts Tom developed.", "Partner-sensitive. Flag every legacy title derived from his framework."),
 ("Paul Black / WCM", 3, "WCM", "Named as a route to legacy families.", "Relationship, not a channel. No title inherits it."),
 ("C12 / Convene / FCCI / CBMC / NCF / Kingdom Advisors", 12, "Various", "Listed as affinity organizations that could carry resources.", "Distribution prospects. No titles attach yet."),
 ("™ symbols", 143, "Nobody yet", "80 distinct names carry ™ in draft output, including malformed ones like 'Design™' and 'Assets™'.", "Strip on import. Re-apply only after a clearance decision."),
]
for c, h in enumerate(RFH, start=1):
    cell = rf.cell(row=1, column=c, value=h)
    cell.font = Font(name="Arial", size=10, bold=True, color="FFFFFF")
    cell.fill = PatternFill("solid", fgColor="9E2A2B")
    cell.alignment = Alignment(wrap_text=True, vertical="center", horizontal="center")
    rf.column_dimensions[get_column_letter(c)].width = RFW[c-1]
for r_, vals in enumerate(RFR, start=2):
    for c, v in enumerate(vals, start=1):
        cell = rf.cell(row=r_, column=c, value=v)
        cell.font = Font(name="Arial", size=10, bold=(c == 1))
        cell.alignment = Alignment(wrap_text=True, vertical="top", horizontal="center" if c == 2 else "left")
        cell.border = Border(left=thin, right=thin, top=thin, bottom=thin)
    rf.row_dimensions[r_].height = 44
rf.auto_filter.ref = f"A1:E{len(RFR)+1}"; rf.freeze_panes = "A2"

wb.move_sheet("LISTS", offset=5)
wb.save("/home/claude/mtl/Master_Title_Library_SCHEMA_v1.xlsx")
print("saved")
