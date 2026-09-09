import re, json, unicodedata
from collections import defaultdict, Counter

SRC_PATH = '/mnt/user-data/uploads/Big_Big_brett_master_life_together.txt'
raw = open(SRC_PATH, encoding='utf-8-sig').read().replace('\r\n', '\n').replace('\r', '\n')
LINES = [l.strip() for l in raw.split('\n')]
N = len(LINES)

# ---------------------------------------------------------------- segments
brett_idx = [i for i, l in enumerate(LINES) if re.match(r'^Brett\s*:', l)]
segments = []
for k, i in enumerate(brett_idx):
    end = brett_idx[k + 1] if k + 1 < len(brett_idx) else N
    req = re.sub(r'^Brett\s*:\s*', '', LINES[i])
    j = i + 1
    while j < min(i + 6, end) and LINES[j] and not re.match(r'^(Thought for|Got it|Below|Here)', LINES[j]):
        req += ' ' + LINES[j]; j += 1
    segments.append({'start': i, 'end': end, 'req': req[:400], 'reqline': i})
segments.insert(0, {'start': 0, 'end': brett_idx[0], 'req': '(opening question) where is the latest and greatest work on the god owns it all curriculum and 40 day campaigns', 'reqline': 2})

TAXO_WORDS = ['life event', 'life events', 'affinity', 'felt need', 'life question', 'life season', 'top 50 categories',
              'top 100 categories', 'top 25 categories', 'categories that i am missing', 'trusted providers',
              'advisors serving', 'who else am i missing', 'top 50 themes', 'biblical topics', 'top 100 life',
              'most common life events', 'top 25 life seasons', 'master list of the top 100 categories', 'top 25 categories of affinity']
TITLE_WORDS = ['series titles', 'title and subtitle', 'title subtitle', 'titles for journeys', 'series title',
               'journey titles', '10 more in each', '20 more in each', '5 more under each', '50 more in each',
               'sample title', 'top 10 series', '10 in each category', 'series per purpose', 'title, subtitle',
               'create 10 series', 'give me 100 family', 'campaign', 'journeys that families']
BUILD_WORDS = ['build', 'create the curric', 'outline', 'devotional', 'curriculum', 'sessions', 'marketing',
               'expand', 'one page', 'two page', 'brochure', 'playbook', 'manual', 'description']

def seg_intent(req):
    r = req.lower()
    if any(w in r for w in TAXO_WORDS): return 'TAXONOMY'
    if any(w in r for w in TITLE_WORDS): return 'TITLES'
    if any(w in r for w in BUILD_WORDS): return 'BUILD'
    return 'STRATEGY'

for s in segments:
    s['intent'] = seg_intent(s['req'])

# ---------------------------------------------------------------- filters
SCAFFOLD = {'core truth', 'devotional reading', 'reflection questions', 'anchor scripture', 'key verse', 'scripture',
            'thought for the day', 'point to ponder', 'talk to god', 'action step', 'practice / prayer', 'prayer',
            'big idea', 'big ideas', 'subtitle', 'title', 'why', 'includes', 'examples', 'example', 'purpose',
            'mission', 'primary outcome', 'small group connection', 'sermon series', 'sessions', 'week 1', 'week 2',
            'day title', 'learning objectives', 'three key ideas', 'my recommendation', 'best six-session outline',
            'top 10 journeys', 'or', 'and', 'the platform', 'notes', 'summary', 'overview', 'format', 'structure',
            'goal', 'outcome', 'result', 'phase 1', 'phase 2', 'phase 3', 'step 1', 'step 2', 'step 3'}
STOPSTART = re.compile(r'^(why\b|subtitle\b|note[s]?\b|this |it |they |these |that |you |we |i |he |she |there |here |below|above|each |every |most |many |when |where |what if|because|so |but |and |or |if |the source|the goal|the point|best |use |add |include|create |build |make |write |give |see |example|for example|per |plus |also |however|meanwhile|therefore|in short|bottom line|key |core |main )', re.I)
BADEND = re.compile(r'[.;:,]$')
FRAGMENT = re.compile(r'\((?![^)]*\))|^\W|\bthis is ok\b|\betc\b\.?$', re.I)

def looks_like_title(t):
    if not t: return False
    t = t.strip()
    if len(t) < 4 or len(t) > 110: return False
    low = t.lower().strip('*: ')
    if low in SCAFFOLD: return False
    if low.startswith(('day ', 'week ', 'session ', 'module ', 'part ')) and len(t.split()) <= 3: return False
    w = t.split()
    if len(w) > 16: return False
    if BADEND.search(t) and not t.endswith('?'): return False
    if STOPSTART.match(t): return False
    if re.match(r'^\d', t) and len(w) <= 3: return False
    caps = sum(1 for x in w if x[:1].isupper() or x[:1].isdigit() or not x[:1].isalpha())
    if caps / len(w) < 0.55: return False
    return True

def clean(t):
    t = t.strip().strip('*').strip()
    t = re.sub(r'^\d{1,3}[.)]\s*', '', t)
    t = re.sub(r'^[A-Z]\.\s+', '', t)
    t = re.sub(r'\s+', ' ', t).strip(' –—-')
    return t.strip()

def norm(t):
    t = unicodedata.normalize('NFKD', t.lower())
    t = re.sub(r'[^a-z0-9 ]', ' ', t)
    t = re.sub(r'^(the|a|an) ', '', t)
    return re.sub(r'\s+', ' ', t).strip()

NUM = re.compile(r'^\*?\s*(\d{1,3})[.)]\s+(.{3,120})$')
ALLCAPS = re.compile(r'^[A-Z0-9 &/\'\-\.,()]{6,60}$')
DAY = re.compile(r'^\*?\s*DAY\s+(\d{1,2})\s*[—–:\-]\s*(.+)$', re.I)
SESSION = re.compile(r'^\*?\s*SESSION\s+(\d{1,2})\s*[—–:\-]\s*(.+)$', re.I)
SUBLBL = re.compile(r'^Subtitle\s*:\s*(.+)$', re.I)
WHYLBL = re.compile(r'^(Why|Why it sells|Best angle|Best for|Note)\b', re.I)
SERIESCUE = re.compile(r'^(sermon series|six[- ]session|6[- ]session|sessions|session outline|six part outline)\s*:?\s*$', re.I)

TAXO_SECTION = re.compile(r'^(TOP \d+|.*LIFE EVENTS|.*AFFINITY|.*FELT NEEDS|.*LIFE QUESTIONS|.*LIFE SEASONS|.*TRUSTED (GUIDES?|PROVIDERS?|ADVISORS?)|.*CATEGORIES)\b', re.I)

# ---------------------------------------------------------------- extraction
rows = []
seen_line = set()

def add(line_no, title, subtitle, level, parent, seg, category, kind='TITLE', slot=''):
    if line_no in seen_line: return
    seen_line.add(line_no)
    rows.append(dict(line=line_no, title=title, subtitle=subtitle or '', level=level, parent=parent or '',
                     seg=seg, category=category or '', kind=kind, slot=slot))

for s in segments:
    a, b = s['start'], s['end']
    category = ''
    last_campaign = ''
    series_mode = False
    i = a
    while i < b:
        L = LINES[i]
        if not L or set(L) == {'_'}:
            i += 1; continue

        m = DAY.match(L)
        if m:
            t = clean(m.group(2)); sub = ''
            if i + 1 < b:
                sm = SUBLBL.match(LINES[i + 1])
                if sm: sub = sm.group(1).strip()
            if looks_like_title(t) or len(t.split()) > 2:
                add(i, t, sub, 'Day / Devotional', last_campaign or category, s, category, slot=f"Day {m.group(1)}")
            i += 1; continue

        m = SESSION.match(L)
        if m:
            t = clean(m.group(2))
            if looks_like_title(t):
                add(i, t, '', 'Session', last_campaign or category, s, category, slot=f"Session {m.group(1)}")
            i += 1; continue

        if SERIESCUE.match(L):
            series_mode = True; i += 1; continue

        if TAXO_SECTION.match(L) and len(L.split()) <= 9:
            category = clean(L); series_mode = False; i += 1; continue

        # section header: unnumbered, short, title-case or allcaps, followed by a numbered item
        if (not NUM.match(L)) and len(L.split()) <= 7 and i + 1 < b and NUM.match(LINES[i + 1]) \
           and not SUBLBL.match(L) and not WHYLBL.match(L) and (ALLCAPS.match(L) or L.istitle() or '&' in L):
            if looks_like_title(L) or ALLCAPS.match(L):
                category = clean(L); series_mode = False
                i += 1; continue

        m = NUM.match(L)
        if m:
            body = clean(m.group(2))
            nxt = LINES[i + 1] if i + 1 < b else ''
            nxt2 = LINES[i + 2] if i + 2 < b else ''
            sub = ''
            title = body
            consumed = 1

            sm = SUBLBL.match(nxt)
            if sm:
                sub = sm.group(1).strip(); consumed = 2
                if WHYLBL.match(nxt2): consumed = 3
            elif ' — ' in body or ' – ' in body:
                parts = re.split(r'\s[—–]\s', body, 1)
                if len(parts) == 2 and looks_like_title(parts[0]):
                    title, sub = parts[0].strip(), parts[1].strip()
            elif nxt and not NUM.match(nxt) and not WHYLBL.match(nxt) and looks_like_title(nxt) is False and len(nxt.split()) <= 18 and nxt[:1].isupper() and not BADEND.search(nxt):
                sub = nxt; consumed = 2
            elif nxt and not NUM.match(nxt) and looks_like_title(nxt) and nxt2 and not NUM.match(nxt2) and not WHYLBL.match(nxt2) and len(nxt2.split()) <= 18:
                # audience-label pattern: numbered line is a group, next is title, next2 is subtitle
                if len(body.split()) <= 6 and not re.search(r'\b(40 days|days of|journey|legacy|stewardship|generosity|purpose|life|family|god|faith|money|wealth)\b', body, re.I):
                    category = body
                    add(i + 1, clean(nxt), nxt2, 'Curriculum / Series', '', s, category)
                    i += 3; continue
                sub = nxt; consumed = 2
            elif nxt and not NUM.match(nxt) and not WHYLBL.match(nxt) and 2 <= len(nxt.split()) <= 18 and nxt[:1].isupper() and not BADEND.search(nxt) and not SERIESCUE.match(nxt):
                sub = nxt; consumed = 2

            kind = 'TAXONOMY' if (s['intent'] == 'TAXONOMY' or TAXO_SECTION.match(category or '')) else 'TITLE'
            if series_mode and last_campaign:
                lvl = 'Session'
                slot = f"Session {m.group(1)}"
                if looks_like_title(title):
                    add(i, title, sub, lvl, last_campaign, s, category, kind, slot)
                i += consumed; continue

            if looks_like_title(title):
                if re.match(r'^\d{1,3} Days? (of|to)\b', title, re.I) or re.match(r'^40 Days\b', title, re.I):
                    lvl = 'Campaign'; last_campaign = title
                elif re.search(r'\bassessment\b', title, re.I): lvl = 'Assessment'
                elif re.search(r'\b(toolkit|builder|planner|roadmap|template|workbook|dashboard|guide|kit)\b', title, re.I): lvl = 'Tool / Asset'
                elif re.search(r'\b(manual|training|playbook|certification|academy)\b', title, re.I): lvl = 'Training'
                elif re.search(r'\b(library|platform|network|studio|intelligence|productions)\b', title, re.I): lvl = 'Platform / Brand'
                elif kind == 'TAXONOMY': lvl = 'Category Label'
                else: lvl = 'Curriculum / Series'
                add(i, title, sub, lvl, last_campaign if lvl == 'Session' else '', s, category, kind)
            i += consumed; continue

        # unnumbered title followed by subtitle, inside a TITLES segment
        if s['intent'] == 'TITLES' and i + 1 < b:
            nxt = LINES[i + 1]
            if looks_like_title(L) and nxt and not NUM.match(nxt) and not SUBLBL.match(nxt) and not WHYLBL.match(nxt) \
               and 3 <= len(nxt.split()) <= 18 and nxt[:1].isupper() and not BADEND.search(nxt) and not looks_like_title(nxt) is False:
                if re.match(r'^\d{1,3} Days? (of|to)\b', L, re.I):
                    add(i, clean(L), nxt, 'Campaign', '', s, category); last_campaign = clean(L)
                    i += 2; continue
        i += 1

print("raw extracted:", len(rows))
print(Counter(r['kind'] for r in rows))
print(Counter(r['level'] for r in rows).most_common())
print(Counter(s['intent'] for s in segments))
json.dump([{k: (v['reqline'] if k == 'seg' else v) for k, v in r.items()} for r in rows], open('/home/claude/mtl/rows_raw.json', 'w'))
json.dump([{k: v for k, v in s.items()} for s in segments], open('/home/claude/mtl/segs.json', 'w'))
for r in rows[:15] + rows[900:915] + rows[2000:2015]:
    print(f"{r['line']:6d} [{r['level'][:14]:14s}] {r['title'][:58]:60s} | {r['subtitle'][:44]}")
