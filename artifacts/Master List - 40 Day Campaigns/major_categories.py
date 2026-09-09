"""Adds the missing spine: every live title is assigned one of ~50 MAJOR CATEGORIES, the track tabs
group by that instead of the 2,088 raw source strings, and a printable Major Categories sheet lists
them all on two pages."""
import openpyxl, re, json
from collections import Counter, defaultdict

SRC = "/home/claude/mtl/Master_Title_Library_v21.xlsx"

# (major category, group, regex over category string + title + subtitle)
MAJOR = [
 ("Worship & Awe", "FORMATION", r"\bworship|awe|wonder|praise|adoration|reverence"),
 ("Prayer", "FORMATION", r"\bpray|prayer|intercession|fasting\b"),
 ("Bible & Scripture", "FORMATION", r"\bbible|scripture|book of|psalms?|proverbs|gospel of|epistle|old testament|new testament"),
 ("Life of Christ", "FORMATION", r"life of christ|red letter|jesus|sermon on the mount|parable|beatitude|resurrection|advent|easter|lent"),
 ("Discipleship & Growth", "FORMATION", r"disciple|spiritual growth|formation|maturity|follow(ing)? jesus|abide"),
 ("Spiritual Disciplines", "FORMATION", r"disciplines?|silence|solitude|meditation|journaling|devotional habit"),
 ("Identity in Christ", "FORMATION", r"identity|who i am|beloved|adopted|image of god|self[- ]worth"),
 ("Faith, Doubt & Apologetics", "FORMATION", r"doubt|apologetic|deconstruct|hard questions|skeptic|why believe"),
 ("Holy Spirit", "FORMATION", r"holy spirit|spirit[- ]led|gifts of the spirit|fruit of the spirit"),

 ("Small Groups & Belonging", "COMMUNITY", r"small group|belong|community|fellowship|connection|one another|lonel"),
 ("Church Health & Vision", "COMMUNITY", r"church health|church vision|vitality|values|mission statement|church culture|revitali"),
 ("Serving & Volunteers", "COMMUNITY", r"serv(e|ing|ant)|volunteer|ministry team|behind the scenes"),
 ("Membership & Next Steps", "COMMUNITY", r"membership|next steps|assimilation|new believer|first steps|foundations class"),
 ("Hospitality & Welcome", "COMMUNITY", r"hospitality|welcome|guest|table|neighbor"),

 ("Evangelism & the Gospel", "MISSION", r"evangel|gospel moment|salvation|share your faith|witness|invite|seeker|baptism"),
 ("Missions & Justice", "MISSION", r"mission(s|al)?\b|justice|mercy|compassion|poverty|orphan|global"),
 ("Kingdom Impact", "MISSION", r"kingdom impact|kingdom living|kingdom purpose|city|citywide|multiply"),

 ("Stewardship & Ownership", "MONEY", r"steward|ownership|god owns|entrust|manage god"),
 ("Generosity & Giving", "MONEY", r"generos|giving|giver|tithe|offering|philanthrop|donor"),
 ("Personal Finances & Budgeting", "MONEY", r"budget|financial plan|money management|spending|saving|invest"),
 ("Contentment & Enough", "MONEY", r"contentment|enough|comparison|greed|simplicity|consumer"),
 ("Debt & Financial Freedom", "MONEY", r"\bdebt|financial freedom|paycheck|margin|financial stress|financial peace"),
 ("Year-End & Occasion Giving", "MONEY", r"year[- ]end|thanksgiving|new year|first fruits|faith promise|state of the church|mid[- ]year"),
 ("Capital Campaigns & Building", "MONEY", r"capital campaign|building fund|expansion|raising the walls|pledge"),

 ("Marriage", "FAMILY", r"marriage|marri(ed|age)|spouse|husband|wife|couple|engaged"),
 ("Parenting", "FAMILY", r"parent|raising|children|kids|teen|adolescen|toddler"),
 ("Family Legacy & Generations", "FAMILY", r"legacy|generation|inheritance|heritage|ancestr|family story|family identity"),
 ("Heirs & Next Generation", "FAMILY", r"heir|next[- ]generation|responsible heirs|beneficiar|young adults? in the family"),
 ("Grief & Loss", "FAMILY", r"grief|loss|mourning|death|widow|funeral|goodbye"),
 ("Caregiving & Aging", "FAMILY", r"caregiv|aging|elder care|dementia|final season|second half|retirement"),
 ("Blended & Complex Families", "FAMILY", r"blended|stepfamily|divorce|estrange|reconcil|in-law|adoption|foster"),
 ("Family Rhythms & Traditions", "FAMILY", r"tradition|celebration|family meeting|family table|rhythms|milestone"),

 ("Work & Calling", "MARKETPLACE", r"\bwork\b|vocation|calling|monday|career|job|profession"),
 ("Business Ownership", "MARKETPLACE", r"business owner|entrepreneur|founder|company|profit|enterprise|marketplace"),
 ("Leadership Development", "MARKETPLACE", r"leader|leadership|influence|manager|executive|board"),
 ("Team & Culture", "MARKETPLACE", r"team|culture|employee|workplace|staff|hiring|engagement"),
 ("Succession & Exit", "MARKETPLACE", r"succession|exit|transition|post[- ]exit|sale of the business|governance"),

 ("Advisors & Trusted Guides", "ADVISOR", r"advisor|attorney|cpa|family office|wealth manager|trusted guide|practice"),
 ("UHNW Family Legacy", "ADVISOR", r"uhnw|high[- ]capacity|affluent|wealthy famil|family enterprise|family council|trust\b|estate"),

 ("Emotional Health & Anxiety", "WHOLE LIFE", r"anxiety|anxious|emotional health|mental health|depress|fear|worry|burnout|stress"),
 ("Whole-Life Health", "WHOLE LIFE", r"health|flourish|wellness|body|fitness|sleep|nutrition|habits"),
 ("Rest & Sabbath", "WHOLE LIFE", r"sabbath|rest|margin|hurry|busy|pace|digital|attention"),
 ("Addiction & Recovery", "WHOLE LIFE", r"addiction|recovery|sober|freedom from|compulsi"),
 ("Trauma & Healing", "WHOLE LIFE", r"trauma|healing|abuse|wound|forgiveness|shame"),
 ("Purpose & Meaning", "WHOLE LIFE", r"purpose|meaning|made for|design|significance|finish well|life plan"),

 ("Men", "LIFE STAGE", r"\bmen\b|man\b|masculin|father|husbands"),
 ("Women", "LIFE STAGE", r"\bwomen\b|woman\b|mother|wives|feminin"),
 ("Young Adults & Singles", "LIFE STAGE", r"young adult|single|dating|college|twenties|emerging adult"),
 ("Students & Youth", "LIFE STAGE", r"student|youth|high school|middle school|teenager"),
 ("Children & Family Ministry", "LIFE STAGE", r"children'?s ministry|kids ministry|elementary|preschool|nursery"),

 ("Seasonal & Holiday", "SEASONAL", r"christmas|easter|advent|lent|holy week|mother'?s day|father'?s day|graduation|summer|back to school|holiday"),
 ("Catalytic Sundays & Single Messages", "SEASONAL", r"catalytic sunday|single sunday|one[- ]week|stand[- ]alone message|vision sunday"),
 ("Service Moments & Elements", "SEASONAL", r"offertory|communion|invitation|altar call|dedication|testimony|transition|announcement"),
]
COMPILED = [(n, g, re.compile(p, re.I)) for n, g, p in MAJOR]
GROUP_ORDER = ["FORMATION", "COMMUNITY", "MISSION", "MONEY", "FAMILY", "MARKETPLACE", "ADVISOR",
               "WHOLE LIFE", "LIFE STAGE", "SEASONAL", "UNASSIGNED"]


def assign(cat, title, sub, topic):
    hay = f"{cat} {title} {sub}"
    for name, group, pat in COMPILED:
        if pat.search(hay):
            return name, group
    return "Not yet categorized", "UNASSIGNED"


if __name__ == "__main__":
    wb = openpyxl.load_workbook(SRC, read_only=True)
    ws = wb["MASTER LIBRARY"]
    hdr = [c.value for c in next(ws.iter_rows(min_row=1, max_row=1))]
    C = {h: i for i, h in enumerate(hdr)}
    counts, examples, subs = Counter(), defaultdict(list), Counter()
    groups = {}
    n = 0
    for r in ws.iter_rows(min_row=2, values_only=True):
        if not r[0] or r[C["Keep / Review / Archive"]] == "Archive":
            continue
        n += 1
        name, group = assign(str(r[C["Parent / Belongs To"]] or ""), str(r[3] or ""), str(r[4] or ""),
                             str(r[C["Topic / Category"]] or ""))
        counts[name] += 1
        groups[name] = group
        if r[4]:
            subs[name] += 1
        if len(examples[name]) < 2:
            examples[name].append(str(r[3]))
    print("live rows:", n, "| major categories used:", len(counts))
    for g in GROUP_ORDER:
        names = [x for x, _, _ in COMPILED if groups.get(x) == g] + (["Not yet categorized"] if g == "UNASSIGNED" else [])
        tot = sum(counts[x] for x in names if x in counts)
        print(f"\n{g}  ({tot:,})")
        for x in names:
            if counts.get(x):
                print(f"   {counts[x]:6,d}  {x:34s} {100*subs[x]//max(1,counts[x]):3d}% sub   e.g. {examples[x][0][:44]}")
    json.dump({"counts": counts, "groups": groups, "subs": subs,
               "examples": {k: v for k, v in examples.items()}}, open("/home/claude/mtl/major_cats.json", "w"))
