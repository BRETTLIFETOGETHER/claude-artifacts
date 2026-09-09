#!/usr/bin/env python3
"""40daycampaigns.com v2 data spine.
Source of truth: Brett's Updated_40_Day_Campaign_Master__4_.xlsx (17,443 rows).
Nothing is invented; every catalog row traces to a Master ID."""
import pandas as pd, json, re, hashlib, sys, unicodedata
from collections import defaultdict, Counter

SRC = "/mnt/user-data/uploads/Updated_40_Day_Campaign_Master__4_.xlsx"
OUT = "/home/claude/site/data"

# ---------------------------------------------------------------- channels
CHANNELS = [
 ("purpose-calling",            "Purpose & Calling"),
 ("identity-significance",      "Identity & Significance"),
 ("community-belonging",        "Community & Belonging"),
 ("prayer-worship",             "Prayer, Worship & Disciplines"),
 ("money-stewardship",          "Money & Stewardship"),
 ("generosity-legacy",          "Generosity & Legacy"),
 ("family-legacy",              "Family Legacy & Generations"),
 ("marriage-relationships",     "Marriage & Relationships"),
 ("parenting-family",           "Parenting & Family"),
 ("emotional-health",           "Emotional Health"),
 ("health-healing",             "Health, Healing & Care"),
 ("freedom-recovery",           "Freedom & Recovery"),
 ("seasons-of-life",            "Seasons of Life"),
 ("work-marketplace",           "Work & Marketplace"),
 ("leadership-serving",         "Leadership & Serving"),
 ("church-vision-values",       "Church Vision & Values"),
 ("ministries-nonprofits",      "Ministries & Nonprofits"),
 ("mission-neighbor",           "Mission & Neighbor"),
 ("church-calendar",            "Seasons & the Church Calendar"),
 ("life-of-christ",             "Life of Christ & Red Letter"),
 ("bible-studies",              "Bible & Scripture Studies"),
 ("doubt-honest-faith",         "Doubt & Honest Faith"),
 ("digital-discernment",        "Digital Discernment & Faith in the Age of AI"),
]
CIDX = {name: i for i, (_, name) in enumerate(CHANNELS)}

def C(name): return CIDX[name]

# exact / prefix category -> channel  (cleaned-segment match, lowercase)
CAT_MAP = {}
def m(ch, *keys):
    for k in keys: CAT_MAP[k.lower()] = C(ch)

m("Life of Christ & Red Letter","life of christ","red letter","the sermon on the mount","pastor sermon series sessions")
m("Purpose & Calling","five purposes campaign library","biblical purpose weekly movements","purpose / calling / meaning",
  "purpose & calling","purpose / calling /","following jesus","discipleship","spiritual growth / discipleship",
  "obedience","faith","flourishing","one-year initiatives","fresh biblical-purpose channel","a church on mission",
  "high-adoption churchwide 40-day campaigns","best series","spiritual formation & discipleship","semi-custom campaigns",
  "custom 40-day campaign themes","assessments")
m("Identity & Significance","identity in christ","identity: who you are in christ","identity")
m("Community & Belonging","community & belonging","small group life","small groups","fellowship","friendship & relational health",
  "hospitality","church-wide belonging & inclusion","community & unity","men's ministry","women's ministry","men","women",
  "unity groups","better together","500 small group curriculum series","top discovery channels","membership")
m("Prayer, Worship & Disciplines","prayer","personal prayer life","corporate & intercessory prayer","prayer & intimacy with god",
  "spiritual habits","personal spiritual disciplines","spiritual disciplines","sabbath / rest","worship","worship & the arts",
  "hearing god's voice","holy spirit","the holy spirit","spiritual warfare","fasting","liturgical / lectionary",
  "family & household spiritual rhythms","renewal & spiritual awakening")
m("Money & Stewardship","financial wisdom ministry campaign library","financial freedom & debt","financial wisdom webinar library",
  "money & financial peace","finances","stewardship","abundance","financial freedom titles","stewardship titles",
  "biblical financial discipleship series title","40-day financial wisdom devotional","wisdom / decision-making series title option",
  "financial stewardship campaigns","stewardship, generosity & finances","money wise","faith and finances",
  "finances, stewardship & generosity","christian financial advisor titles","financial freedom / biblical wisdom title option")
m("Generosity & Legacy","generosity","generosity & stewardship","generosity / stewardship cluster","capital campaigns",
  "vision & capital campaign","generosityministry.com titles","generosity / campaign closing architecture","kin partner series concepts",
  "kin project / product tracker","kin master reference","legacy & generational faith","financial planning & legacy")
m("Family Legacy & Generations","god owns it all","family legacy journeys","family legacy campaigns","family legacy",
  "families of wealth series","family identity and story","faith and spiritual heritage","family values and vision",
  "marriage and family leadership","wisdom, mentoring, and life experience","wealth, stewardship, and responsibility",
  "generosity and family impact","succession, governance, and legacy planning","family flourishing and whole-life well-being",
  "family leadership and influence","family learning and wisdom","family adventure and shared experiences","family kingdom impact",
  "succession by design curriculum","top 25 affinity groups for family legacy ministry","top series family office leaders would want",
  "family legacy platform tools","family legacy journey finder","uhnw legacy family series","christian estate attorneys",
  "seasons of life")  # GOIA sub-branch handled by parent segment first
m("Marriage & Relationships","marriage","marriage & relationships","relationships","marriage preparation & engaged couples",
  "sexuality & purity","relationships and reconciliation","family, marriage & parenting")
m("Parenting & Family","parenting","family & parenting","parenting young children","parenting teens & young adults",
  "blended & step families","adoption & foster care","family discipleship","parenting and preparing the next generation","family")
m("Emotional Health","anxiety & mental health","mental & emotional health","peace / anxiety / emotional health","grief & loss",
  "grief / loss","hope in hard times","trauma & emotional healing","rest, margin & burnout","suffering & unanswered prayer",
  "waiting seasons & delayed dreams","anxiety, fear & emotional wellness","grief, suffering & hard seasons","grace, peace & rest",
  "emotional & mental health","hope","joy & gratitude")
m("Health, Healing & Care","physical health & the body","chronic illness & suffering in the body","special needs & disability ministry",
  "caregiving for aging parents","whole life health","healing & wholeness")
m("Freedom & Recovery","addiction recovery","recovery / freedom","freedom & breakthrough","grace & forgiveness","faith over fear",
  "transformation & life change","surrender & total trust","courage & boldness")
m("Seasons of Life","top 25 seasons of life series","life stages","singleness & the waiting season","widowhood & starting over",
  "divorce recovery & co-parenting","young adults / singles","military, first responder & frontline families",
  "immigrant & multicultural faith","new beginnings & fresh starts","next-generations","students / youth","children / kids")
m("Work & Marketplace","work, career & marketplace faith","marketplace / purpose at work","business leader & business owner campaign titles",
  "business / hr / team culture series","business leader ceo employee felt-need series","corporate / business market campaign titles",
  "talent development campaigns","innovation & continuous improvement campaigns","remote & hybrid work campaigns",
  "customer success campaigns","sales & business development campaigns","strategic planning campaigns","change management campaigns",
  "diversity, unity & belonging campaigns","founder & ownership campaigns","talent development builder™","then build industry builders",
  "business / corporate market names","faith & work / marketplace leadership builder™","marketplace & faith at work",
  "advisor client campaign library","high-capacity client / advisor campaigns","medium-size business / owner campaigns",
  "christian advisor series library","christian advisor practice growth","christian advisor seminar library",
  "top series cpas would want to give clients","top series: advisors to christian business owners","women advisor series title option",
  "top 25 series for ministry development officers","wisdom / decision making","wisdom & discernment")
m("Leadership & Serving","church leadership development","church leadership","leadership","leadership & influence",
  "volunteer mobilization & serving culture","volunteer campaigns (11–25)","serving others & compassion","serving","ministry",
  "youth & next generation ministry","talent? no","adult bible fellowship / adult sunday school builder","leadership, calling & vision")
m("Church Vision & Values","mission / vision / values","church mission / vision / values","church values framework",
  "church culture & mission ownership","church vision & all in","church health & multiplication","church planting & multisite expansion",
  "revival & spiritual awakening","church re-engagement / welcome back","baptism & new member assimilation",
  "church anniversary & milestone celebration","denominational / network campaigns","culture titles","priority mvv framework",
  "multiplication","church engagement","why these 10 categories?","rename + split rules","master channels / transcript channels",
  "transcript priority no","every campaign gets tagged")
m("Ministries & Nonprofits","christian nonprofit campaign builder","ministry campaign builder™","new category: ministry campaign builder™",
  "radio / television ministry campaign builder","affinity group / ministry network builder","partnership campaigns",
  "church partnership campaigns","digital engagement campaigns","storytelling & testimony campaigns","prayer campaigns",
  "500 ministry campaigns","donor","nonprofit")
m("Mission & Neighbor","mission","mission / outreach / kingdom impact","global missions & the nations","justice & mercy",
  "racial reconciliation & unity","creation care & stewardship of the earth","invite & outreach","evangelism & harvest season",
  "evangelism & missions","evangelism & mission","biblical justice & community impact","testimony / story campaigns",
  "kingdom living & impact","new believers & baptism","new believer","christ-centered & biblical living")
m("Seasons & the Church Calendar","the top 100 catalytic sundays","catalytic sunday master catalog categories","annual calendar sundays",
  "the top 25 annual church calendar sundays","seasonal ministry launch sundays","catalytic ministry launch sundays",
  "holiday series / lent / advent","new year 21-day / 30-day starter campaigns","summer 30-day journeys",
  "summer 21-day growth challenges","signature sermons / big-day messages","every catalytic sunday includes",
  "\"on any given sunday\"","additional strategic sundays","part 1","part 2","part 3")
m("Bible & Scripture Studies","bible book campaigns","biblical character campaigns","bible stories / key passages","bible studies",
  "faith in action · james","rebuilding · nehemiah","spiritual warfare · armor of god","sunday school / adult education",
  "heaven & eternity","grace","the gospel","pillar three","pillar four","seminary")
m("Doubt & Honest Faith","doubt & wrestling with faith","doubt, questions & honest faith","faith & trust")
m("Digital Discernment & Faith in the Age of AI","technology, screens & digital life","digital discernment & faith in the age of ai",
  "digital discernment")

KEYWORDS = [  # (regex on title+category+feltneed, channel) — rescue pass, ordered
 (r"\bred letter|life of christ|sermon on the mount|beatitude", "Life of Christ & Red Letter"),
 (r"catalytic|sunday launch|advent|lent\b|easter|christmas|thanksgiving|new year|mother'?s day|father'?s day|back.to.school|good friday|palm sunday|pentecost", "Seasons & the Church Calendar"),
 (r"advisor|cpa\b|ria\b|client|practice growth|wealth manager", "Work & Marketplace"),
 (r"donor|nonprofit|ministry network|radio|television|parachurch", "Ministries & Nonprofits"),
 (r"legacy|estate|heir|inherit|succession|family office|generational wealth|god owns it all|goia", "Family Legacy & Generations"),
 (r"gener(ous|osity)|tith|capital campaign|kingdom invest", "Generosity & Legacy"),
 (r"money|financ|debt|budget|steward|wealth|provision|contentment", "Money & Stewardship"),
 (r"marri|husband|wife|couple|engag|wedding|purity|sexual", "Marriage & Relationships"),
 (r"parent|\bmom\b|\bdad\b|father|mother|kids?\b|children|family devotion|foster|adopt", "Parenting & Family"),
 (r"anxi|worry|fear|grief|loss|depress|mental|burnout|stress|peace\b|rest\b|hope\b|suffer|lament", "Emotional Health"),
 (r"body|health|illness|disab|caregiv|cancer|healing", "Health, Healing & Care"),
 (r"addict|recovery|freedom|breakthrough|forgiv|shame|habit|porn", "Freedom & Recovery"),
 (r"single|widow|divorce|retire|empty nest|college|graduat|military|veteran|immigrant|life stage|season of life", "Seasons of Life"),
 (r"work\b|career|job\b|business|marketplace|office|employee|leader.?ship at work|entrepreneur|vocation", "Work & Marketplace"),
 (r"volunteer|serve|serving|leader|elder|deacon|staff|team\b|coach", "Leadership & Serving"),
 (r"vision|values|mission statement|culture|membership|assimilat|baptism|plant|multisite|revival|awaken", "Church Vision & Values"),
 (r"evangel|outreach|invit|mission|justice|mercy|reconcil|neighbor|nations|witness|share (your|the) faith", "Mission & Neighbor"),
 (r"doubt|deconstruct|question|skeptic|wrestl", "Doubt & Honest Faith"),
 (r"\bai\b|artificial intelligence|screen|digital|technology|phone|social media|algorithm", "Digital Discernment & Faith in the Age of AI"),
 (r"pray|worship|fast(ing)?|sabbath|devotion|quiet time|spirit\b|holy spirit|presence", "Prayer, Worship & Disciplines"),
 (r"identity|who (you|i) are|belov|significan|enough\b|image of god", "Identity & Significance"),
 (r"belong|community|friend|group|table|together|alone|connect", "Community & Belonging"),
 (r"bible|scripture|book of|study of|psalm|proverbs|gospel of|epistle|james\b|nehemiah|romans|philippians", "Bible & Scripture Studies"),
 (r"purpose|calling|why (you|i)|meaning|follow(ing)? jesus|disciple", "Purpose & Calling"),
]

def clean_cat(raw):
    s = str(raw)
    s = re.sub(r"™", "", s)
    parts = [p.strip() for p in re.split(r"\s*[>|]\s*", s) if p.strip()]
    out = []
    for p in parts:
        p = re.sub(r"^\d+[\.\)]?\s*", "", p)          # strip "22 " / "1. "
        p = re.sub(r"\s*\(\d+[^)]*\)\s*$", "", p)      # strip "(25)"
        p = re.sub(r"\s*\(top \d+\)\s*$", "", p, flags=re.I)
        p = re.sub(r"\s*\(add \d+\)\s*$", "", p, flags=re.I)
        if p: out.append(p)
    return out

def map_channel(row):
    segs = clean_cat(row["Category"])
    for seg in segs:                       # left-to-right: parent wins
        sl = seg.lower()
        if sl in CAT_MAP: return CAT_MAP[sl], seg, segs
        for key, ci in CAT_MAP.items():    # prefix
            if sl.startswith(key) or key.startswith(sl) and len(sl) > 6:
                return ci, seg, segs
    hay = " ".join([str(row["Campaign Title"]), str(row["Category"]),
                    str(row.get("Core Felt Need / Theme","")), str(row.get("Format / Product Type",""))]).lower()
    for rx, ch in KEYWORDS:
        if re.search(rx, hay): return C(ch), segs[-1] if segs else "General", segs
    return None, segs[-1] if segs else "General", segs

# ---------------------------------------------------------------- theme label
GENERIC = {"best series","example categories","best umbrella idea","five new major categories",
  "small group master brochure","custom 40-day campaign themes","the top 100 catalytic sundays",
  "on any given sunday","\"on any given sunday\"","god owns it all / legacy campaign builder",
  "five purposes campaign library","mission / vision / values","god owns it all"}
def theme_label(segs, ch_name):
    for seg in reversed(segs):
        sl = seg.lower().strip()
        if sl in GENERIC: continue
        if re.search(r"missing|would actually|you'?re also|why i think|recommendation|these \d+ categories|still missing|becomes a competitive", sl):
            continue
        if len(seg) > 64: continue
        return seg
    return ch_name.split(" & ")[0]

# ---------------------------------------------------------------- attributes
AFF = ["Whole Church","Men","Women","Young Adults","Students","Children & Families","Couples",
       "Seniors & Grandparents","New Believers","Leaders","Advisors & Clients","Business Owners"]
AFF_RX = [(r"whole church|churchwide|congregation|everyone|all ages",0),(r"\bmen\b|men's|husband|father|dad",1),
 (r"\bwomen\b|women's|wife|mother|mom",2),(r"young adult|20s|30s|college|emerging adult",3),
 (r"student|youth|teen|high school|middle school",4),(r"child|kids|family|families|household|parent",5),
 (r"couple|marri|engag",6),(r"senior|grandparent|second half|retire|aging|empty nest",7),
 (r"new believer|seeker|baptism|next step|welcome",8),(r"leader|staff|elder|pastor|volunteer|coach|director",9),
 (r"advisor|cpa|ria|planner|attorney|client",10),(r"business|owner|ceo|executive|entrepreneur|employee|workplace|team",11)]
def affinities(row, ci):
    hay = f"{row.get('Best For / Audience','')} {row.get('Category','')} {row['Campaign Title']}".lower()
    bits = 0
    for rx, i in AFF_RX:
        if re.search(rx, hay): bits |= 1 << i
    if ci in (C("Work & Marketplace"),): bits |= 1<<11
    if not bits & 0b1111111110: bits |= 1  # default whole church
    return bits or 1

F7,F21,F30,F40,FST,F1 = 1,2,4,8,16,32
def formats(row, ci, tier):
    t = f"{row.get('Format / Product Type','')} {row.get('Tier','')} {row['Campaign Title']} {row.get('Subtitle','')}".lower()
    if "catalytic sunday" in t or ci == C("Seasons & the Church Calendar") and "sunday" in t and "campaign" not in t:
        pass
    f = 0
    if re.search(r"7.day|seven.day", t): f |= F7
    if re.search(r"21.day", t): f |= F21
    if re.search(r"30.day", t): f |= F30
    if re.search(r"40.day", t): f |= F40
    if re.search(r"six.session|6.session|study series|bible study|small group series|curriculum series|sunday school|seminary|course", t): f |= FST
    if "catalytic sunday" in t: f |= F1
    if not f: f = F7|F21|F30|F40          # campaign default: all four
    if ci == C("Life of Christ & Red Letter") and not f & FST: f |= FST
    return f

SEASONS = ["Advent","Christmas","New Year","Lent","Easter","Pentecost","Mother's Day","Father's Day",
           "Summer","Back to School","Thanksgiving"]
SEA_RX = [r"advent",r"christmas",r"new year",r"\blent\b|ash wednesday|good friday|palm sunday|holy week",
          r"easter|resurrection",r"pentecost",r"mother'?s day",r"father'?s day",r"\bsummer\b",
          r"back.to.school|fall kick|fall launch",r"thanksgiv|gratitude sunday|harvest"]
def season_of(row):
    hay = f"{row['Campaign Title']} {row.get('Subtitle','')} {row.get('Category','')}".lower()
    for i, rx in enumerate(SEA_RX):
        if re.search(rx, hay): return i
    return -1

def slugify(s):
    s = unicodedata.normalize("NFKD", str(s)).encode("ascii","ignore").decode()
    s = re.sub(r"[^a-z0-9]+","-", s.lower()).strip("-")
    return s[:60] or "campaign"

BRAND_BLOCK = ["financial peace","experiencing god","celebrate recovery","emotionally healthy",
  "master your money never enough","the purpose driven life","dave ramsey","crown financial","alpha course"]

def main():
    df = pd.read_excel(SRC, sheet_name="Updated Master")
    n0 = len(df); assert n0 == 17443, n0

    cf = df["Conflict Flag"].fillna("")
    bd = df["Build Decision"].fillna("")
    excl_ref  = cf.str.contains("copyright|trademark", case=False)
    excl_nb   = bd.str.contains("Do not build now", case=False)
    excluded  = df[excl_ref | excl_nb]
    active    = df[~(excl_ref | excl_nb)].copy()

    support_mask = active["Tier"].fillna("").eq("Life of Christ Supporting Content")
    support = active[support_mask]
    top     = active[~support_mask].copy()

    # channel + theme
    unmapped = []
    rows = []
    for _, r in top.iterrows():
        ci, seg, segs = map_channel(r)
        if ci is None:
            unmapped.append((r["Master ID"], r["Category"], r["Campaign Title"])); ci = C("Purpose & Calling")
        rows.append((r, ci, theme_label(segs, CHANNELS[ci][1])))

    # consolidate themes per channel (cap label variety: merge case/punct dupes)
    theme_key = lambda ci, lbl: (ci, re.sub(r"[^a-z0-9]+"," ", lbl.lower()).strip())
    theme_reg = {}; themes = []
    for r, ci, lbl in rows:
        k = theme_key(ci, lbl)
        if k not in theme_reg:
            theme_reg[k] = len(themes); themes.append([ci, lbl, slugify(lbl)])
    # dedupe theme slugs
    seen = {}
    for t in themes:
        s = t[2]; n = seen.get(s,0)+1; seen[s]=n
        if n>1: t[2] = f"{s}-{n}"

    # supporting sessions -> parent by series segment
    by_title_ch = defaultdict(list)
    for i,(r,ci,lbl) in enumerate(rows):
        by_title_ch[(ci, str(r["Campaign Title"]).strip().lower())].append(i)
    nests = defaultdict(list); orphans = []
    for _, s in support.iterrows():
        segs = clean_cat(s["Category"])
        parent = None
        loc = C("Life of Christ & Red Letter")
        for seg in segs:
            hit = by_title_ch.get((loc, seg.strip().lower()))
            if hit: parent = hit[0]; break
        if parent is None: orphans.append(s)
        else: nests[parent].append({"t": str(s["Campaign Title"]), "s": None if pd.isna(s["Subtitle"]) else str(s["Subtitle"]),
                                    "id": s["Master ID"], "w": segs[-1] if segs else ""})
    for o in orphans:   # keep every row: orphaned support becomes top-level in LoC
        r = o; ci = C("Life of Christ & Red Letter")
        rows.append((r, ci, theme_label(clean_cat(r["Category"]), "Red Letter")))
        k = theme_key(ci, rows[-1][2])
        if k not in theme_reg: theme_reg[k]=len(themes); themes.append([ci, rows[-1][2], slugify(rows[-1][2])])

    # fingerprints (unique 6-hex, probed)
    used_fp = set()
    def fp_of(mid):
        h = hashlib.sha1(mid.encode()).hexdigest(); i = 0
        while h[i:i+6] in used_fp: i += 1
        used_fp.add(h[i:i+6]); return h[i:i+6]

    # slugs unique
    used_slug = Counter()
    def slug_of(t):
        s = slugify(t); used_slug[s]+=1
        return s if used_slug[s]==1 else f"{s}-{used_slug[s]}"

    grade_pt = {"AA":4,"A":3,"A or AA":3,"B":2}
    NEW_SRC = ("Pasted text(9)","Pasted text(11)","Pasted text(12)")
    out_rows = []; brand_hits = []
    for r, ci, lbl in rows:
        ti = theme_reg[theme_key(ci,lbl)]
        title = str(r["Campaign Title"]).strip()
        sub   = None if pd.isna(r.get("Subtitle")) else str(r["Subtitle"]).strip()
        g  = str(r.get("Priority Grade") or "").strip()
        pt = grade_pt.get(g, 1)
        fset = formats(r, ci, r.get("Tier"))
        flag = 0
        bdv = str(r.get("Build Decision") or "")
        if "flagship" in bdv or "most strategic" in bdv: flag |= 1
        se = season_of(r)
        if se >= 0 or "catalytic sunday" in str(r.get("Format / Product Type","")).lower(): flag |= 2
        if any(str(r.get("Source Document","")).startswith(p) for p in NEW_SRC): flag |= 4
        if g == "AA": flag |= 8
        tl = title.lower()
        for b in BRAND_BLOCK:
            if b in tl: brand_hits.append((r["Master ID"], title))
        out_rows.append({"id": r["Master ID"], "slug": slug_of(title), "t": title, "s": sub,
            "ch": ci, "th": ti, "f": fset, "af": affinities(r, ci), "co": flag, "g": g or "—",
            "pt": pt, "fp": fp_of(r["Master ID"]), "se": se,
            "aud": str(r.get("Best For / Audience") or "").strip()[:140] or None,
            "fn":  None if pd.isna(r.get("Core Felt Need / Theme")) else str(r["Core Felt Need / Theme"]).strip()[:160],
            "ns": 0})
    idmap = {o["id"]: k for k, o in enumerate(out_rows)}
    for pi, kids in nests.items():
        mid = rows[pi][0]["Master ID"]; out_rows[idmap[mid]]["ns"] = len(kids)

    stats = {
        "source_rows": n0, "excluded_reference": int(excl_ref.sum()), "excluded_notbuild": int(excl_nb.sum()),
        "supporting_nested": sum(len(v) for v in nests.values()), "supporting_orphans": len(orphans),
        "catalog": len(out_rows), "active_total": len(out_rows) + sum(len(v) for v in nests.values()),
        "channels": len(CHANNELS), "themes": len(themes), "unmapped_keyword_fallback": len(unmapped),
        "flagship": sum(1 for o in out_rows if o["co"] & 1), "seasonal": sum(1 for o in out_rows if o["co"] & 2),
        "new": sum(1 for o in out_rows if o["co"] & 4), "shelf": sum(1 for o in out_rows if o["co"] & 8),
        "brand_collisions": brand_hits[:20], "brand_collision_count": len(brand_hits),
    }
    ch_counts = Counter(o["ch"] for o in out_rows)
    stats["per_channel"] = {CHANNELS[i][1]: ch_counts[i] for i in range(len(CHANNELS))}

    import os; os.makedirs(OUT, exist_ok=True)
    json.dump({"rows": out_rows, "themes": themes, "nests": {rows[pi][0]["Master ID"]: kids for pi,kids in nests.items()},
               "stats": stats}, open("/home/claude/build/spine.json","w"))
    print(json.dumps(stats, indent=1)[:3000])
    if unmapped[:12]:
        print("\nFallback-mapped sample:"); [print(" ", u) for u in unmapped[:12]]

if __name__ == "__main__": main()
