import re, json, unicodedata
from collections import Counter, defaultdict

SRC_PATH = '/mnt/user-data/uploads/Big_Big_brett_master_life_together.txt'
raw = open(SRC_PATH, encoding='utf-8-sig').read().replace('\r\n', '\n').replace('\r', '\n')
LINES = [l.strip() for l in raw.split('\n')]
N = len(LINES)

brett_idx = [i for i, l in enumerate(LINES) if re.match(r'^Brett\s*:', l)]
BRETT_LINES = set(brett_idx)
segments = []
for k, i in enumerate(brett_idx):
    end = brett_idx[k + 1] if k + 1 < len(brett_idx) else N
    req = re.sub(r'^Brett\s*:\s*', '', LINES[i])
    j = i + 1
    while j < min(i + 5, end) and LINES[j] and not re.match(r'^(Thought for|Got it|Below|Here|Short answer)', LINES[j]):
        req += ' ' + LINES[j]; j += 1
    segments.append({'start': i, 'end': end, 'req': re.sub(r'\s+', ' ', req)[:300], 'reqline': i})
segments.insert(0, {'start': 0, 'end': brett_idx[0],
                    'req': 'where is the latest and greatest work here on the god owns it all curriculum and 40 day campaigns?', 'reqline': 2})

TAXO_RE = re.compile(r'(affinity|life event|felt need|life question|life season|trusted (guide|provider|advisor)|biblical topic|top \d+ categories|categories of|master list of the top|who else am i missing|providers and advisors)', re.I)
TITLE_RE = re.compile(r'(title|subtitle|series|journey|campaign|theme)', re.I)
BUILD_RE = re.compile(r'(build|create|outline|devotional|curricul|session|marketing|expand|brochure|playbook|manual|one page|two page|description)', re.I)

for s in segments:
    r = s['req']
    if TAXO_RE.search(r) and not re.search(r'\b(titles?|subtitles?|series titles)\b', r, re.I):
        s['intent'] = 'TAXONOMY'
    elif TITLE_RE.search(r) and re.search(r'\b(titles?|subtitle|series|journeys?|campaigns?)\b', r, re.I) and re.search(r'\b(give|create|more|top \d+|\d+ more|sample|list)\b', r, re.I):
        s['intent'] = 'TITLES'
    elif BUILD_RE.search(r):
        s['intent'] = 'BUILD'
    else:
        s['intent'] = 'STRATEGY'

SCAFFOLD_PREFIX = ('core truth', 'devotional reading', 'reflection question', 'anchor scripture', 'key verse',
                   'scripture', 'thought for the day', 'point to ponder', 'talk to god', 'action step',
                   'practice / prayer', 'prayer', 'big idea', 'subtitle', 'title', 'why', 'includes', 'example',
                   'purpose statement', 'primary outcome', 'small group connection', 'sermon series', 'session outline',
                   'learning objective', 'three key idea', 'my recommendation', 'best six', 'top 10 journeys',
                   'day title', 'weekly challenge', 'discussion question', 'leader note', 'host note', 'video',
                   'teaching', 'closing', 'opening', 'recap', 'phase ', 'step ', 'week ', 'module ', 'part ',
                   'option a', 'option b', 'what exists', 'what it is not', 'bottom line', 'my favorite', 'best ')
ALLCAPS_RUN = re.compile(r'\b[A-Z][A-Z0-9&\'\-]{2,}(\s+[A-Z][A-Z0-9&\'\-]{2,}){2,}')
BADEND = re.compile(r'[.;:,]$')
STOPSTART = re.compile(r'^(this |it |they |these |that |you |we |i |he |she |there |here |below|above|each |every |most |many |when |where |because|so |but |and |or |if |use |add |include|see |per |plus |also |however|therefore|in short|no |not |never |always )', re.I)

def strip_paren(t):
    return re.sub(r'\([^)]*\)', '', t).strip()

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

def looks_like_title(t):
    if not t: return False
    t = t.strip()
    core = strip_paren(t)
    low = core.lower().strip('*: ')
    if len(core) < 5 or len(core) > 105: return False
    if low.startswith(SCAFFOLD_PREFIX): return False
    w = core.split()
    if len(w) < 2 or len(w) > 15: return False
    if BADEND.search(core) and not core.endswith('?'): return False
    if STOPSTART.match(core): return False
    if ALLCAPS_RUN.search(core): return False
    caps = sum(1 for x in w if x[:1].isupper() or not x[:1].isalpha())
    if caps / len(w) < 0.55: return False
    return True

def ok_subtitle(t):
    if not t: return False
    t = t.strip()
    if len(t) < 8 or len(t) > 140: return False
    if ALLCAPS_RUN.search(t): return False
    if re.match(r'^(why|note|best|subtitle|includes|example|this |it |they )', t, re.I): return False
    if len(t.split()) > 22: return False
    return True

NUM = re.compile(r'^\*?\s*(\d{1,3})[.)]\s+(.{3,130})$')
DAY = re.compile(r'^\*?\s*DAY\s+(\d{1,2})\s*[—–:\-]\s*(.+)$', re.I)
SESSION = re.compile(r'^\*?\s*SESSION\s+(\d{1,2})\s*[—–:\-]\s*(.+)$', re.I)
SUBLBL = re.compile(r'^Subtitle\s*:\s*(.+)$', re.I)
WHYLBL = re.compile(r'^(Why|Best angle|Best for|Note|Big Idea|Small Group)\b', re.I)
SERIESCUE = re.compile(r'^(sermon series|six[- ]session|6[- ]session|sessions|session outline|six part outline|series)\s*:?\s*$', re.I)
TAXO_SECTION = re.compile(r'^(TOP \d+|.*LIFE EVENTS|.*AFFINITY|.*FELT NEEDS|.*LIFE QUESTIONS|.*LIFE SEASONS|.*TRUSTED (GUIDES?|PROVIDERS?|ADVISORS?)|.*PROVIDERS)\b', re.I)

rows, seen = [], set()

def add(line_no, title, subtitle, level, parent, seg, category, kind='TITLE', slot=''):
    key = (line_no,)
    if key in seen: return
    seen.add(key)
    rows.append(dict(line=line_no, title=title, subtitle=subtitle if ok_subtitle(subtitle) else '', level=level,
                     parent=parent or '', segline=seg['reqline'], req=seg['req'], intent=seg['intent'],
                     category=category or '', kind=kind, slot=slot))

for s in segments:
    a, b, intent = s['start'], s['end'], s['intent']
    category, last_campaign, series_mode, prev_num, prev_row_idx = '', '', False, 0, None
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
            if len(strip_paren(t).split()) >= 2 and not ALLCAPS_RUN.search(t):
                add(i, t, sub, 'Day / Devotional', last_campaign or category, s, category, 'TITLE', f"Day {m.group(1)}")
            i += 1; continue

        m = SESSION.match(L)
        if m:
            t = clean(m.group(2))
            if looks_like_title(t):
                add(i, t, '', 'Session', last_campaign or category, s, category, 'TITLE', f"Session {m.group(1)}")
            i += 1; continue

        if SERIESCUE.match(L):
            series_mode = True; prev_num = 0; i += 1; continue

        if TAXO_SECTION.match(L) and len(L.split()) <= 9:
            category = clean(L); series_mode = False; prev_num = 0; i += 1; continue

        m = NUM.match(L)
        if m:
            num = int(m.group(1))
            body = clean(m.group(2))
            # counter restart -> the previous numbered item was a category header
            if num == 1 and prev_num > 1 and prev_row_idx is not None:
                pr = rows[prev_row_idx]
                category = pr['title']
                pr['level'] = 'Category Label'; pr['kind'] = 'TAXONOMY'
            prev_num = num
            nxt = LINES[i + 1] if i + 1 < b else ''
            nxt2 = LINES[i + 2] if i + 2 < b else ''
            title, sub, consumed = body, '', 1

            sm = SUBLBL.match(nxt)
            if sm:
                sub = sm.group(1).strip(); consumed = 2
                if WHYLBL.match(nxt2): consumed = 3
            elif re.search(r'\s[—–]\s', body):
                parts = re.split(r'\s[—–]\s', body, 1)
                if looks_like_title(parts[0]) and ok_subtitle(parts[1]):
                    title, sub = parts[0].strip(), parts[1].strip()
            elif nxt and not NUM.match(nxt) and not WHYLBL.match(nxt) and not SERIESCUE.match(nxt) and ok_subtitle(nxt):
                # audience-label pattern: short generic label, then title, then subtitle
                if (len(body.split()) <= 5 and looks_like_title(nxt) and ok_subtitle(nxt2)
                        and not re.search(r'\b(40 days|days of|god|legacy|family|money|wealth|faith|purpose|generous|steward)\b', body, re.I)):
                    category = body
                    add(i + 1, clean(nxt), nxt2, 'Curriculum / Series', '', s, category)
                    prev_row_idx = len(rows) - 1
                    i += 3; continue
                sub = nxt; consumed = 2

            if not looks_like_title(title):
                i += consumed; continue

            kind = 'TAXONOMY' if intent == 'TAXONOMY' else 'TITLE'
            if series_mode and last_campaign:
                add(i, title, sub, 'Session', last_campaign, s, category, kind, f"Session {num}")
            else:
                if re.match(r'^\d{1,3}[- ]Days?\b|^\d{1,3} Days? (of|to)\b', title, re.I):
                    lvl = 'Campaign'; last_campaign = title
                elif re.search(r'\bassessment\b', title, re.I): lvl = 'Assessment'
                elif re.search(r'\b(toolkit|builder|planner|roadmap|template|workbook|dashboard|kit|scorecard)\b', title, re.I): lvl = 'Tool / Asset'
                elif re.search(r'\b(manual|training|playbook|certification|academy|course)\b', title, re.I): lvl = 'Training'
                elif re.search(r'\b(library|platform|network|studio|intelligence|productions|ministry\.com)\b', title, re.I): lvl = 'Platform / Brand'
                elif kind == 'TAXONOMY': lvl = 'Category Label'
                else: lvl = 'Curriculum / Series'
                add(i, title, sub, lvl, '', s, category, kind)
            prev_row_idx = len(rows) - 1 if rows and rows[-1]['line'] == i else prev_row_idx
            i += consumed; continue

        if intent == 'TITLES' and i + 1 < b:
            nxt = LINES[i + 1]
            if looks_like_title(L) and ok_subtitle(nxt) and not NUM.match(nxt) and not SUBLBL.match(nxt):
                if re.match(r'^\d{1,3} Days? (of|to)\b', L, re.I):
                    last_campaign = clean(L)
                    add(i, clean(L), nxt, 'Campaign', '', s, category)
                    prev_row_idx = len(rows) - 1
                    i += 2; continue
        i += 1

# ---- Brett-rejected "Family Legacy XYZ" naming block
REJECT_LINE = next((i for i, l in enumerate(LINES) if 'don' in l.lower() and 'family legacy xyz' in l.lower()), None)
for r in rows:
    r['rejected'] = bool(REJECT_LINE and r['line'] < REJECT_LINE and re.match(r'^Family Legacy \w', r['title']))

for r in rows:
    r['brett'] = r['line'] in BRETT_LINES or (r['line'] - 1) in BRETT_LINES

print("rows:", len(rows), "| reject-block:", sum(r['rejected'] for r in rows), "| reject line:", REJECT_LINE)
print(Counter(r['level'] for r in rows).most_common())
print(Counter(r['kind'] for r in rows))
print(Counter(s['intent'] for s in segments))
print("with subtitle:", sum(1 for r in rows if r['subtitle']))
json.dump(rows, open('/home/claude/mtl/rows.json', 'w'))
for r in rows[:8] + rows[1200:1210] + rows[2600:2610]:
    print(f"{r['line']:6d} [{r['level'][:16]:16s}] {r['title'][:52]:54s} | {r['subtitle'][:40]:42s} | cat={r['category'][:22]}")
