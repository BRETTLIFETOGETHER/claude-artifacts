import sys, re, json, difflib, unicodedata
sys.path.insert(0, '.')
from rapidfuzz import fuzz
from loadp import load_paras


def norm(s):
    s = unicodedata.normalize('NFKC', s)
    s = s.replace('\u2019', "'").replace('\u2018', "'")
    s = s.replace('\u201c', '"').replace('\u201d', '"')
    for d in '\u2014\u2013\u2012\u2212\u2010\u2011':
        s = s.replace(d, '-')
    s = re.sub(r'!\[\]\([^)]*\)(\{[^}]*\})?', '', s)
    s = re.sub(r'[*_>#`\[\]]', '', s)
    s = re.sub(r'\s+', ' ', s)
    return s.strip()


A = load_paras('A2_pg.md')
B = load_paras('B_pg.md')
C = load_paras('C_current.md')
An = [norm(x) for x in A]
Bn = [norm(x) for x in B]
Cn = [norm(x) for x in C]
ATEXT = ' \u00a7 '.join(An)

# --- align B and C by sequence, refined by similarity ---
sm = difflib.SequenceMatcher(None, [x.lower() for x in Bn], [x.lower() for x in Cn], autojunk=False)
pairs = []
for tag, i1, i2, j1, j2 in sm.get_opcodes():
    if tag == 'equal':
        for k in range(i2 - i1):
            pairs.append(('same', i1 + k, j1 + k))
    elif tag == 'replace':
        usedj = set()
        for i in range(i1, i2):
            best, bs = None, 0
            for j in range(j1, j2):
                if j in usedj:
                    continue
                s = fuzz.ratio(Bn[i].lower(), Cn[j].lower()) / 100
                if s > bs:
                    bs, best = s, j
            if best is not None and bs >= 0.60:
                usedj.add(best); pairs.append(('mod', i, best))
            else:
                pairs.append(('bonly', i, None))
        for j in range(j1, j2):
            if j not in usedj:
                pairs.append(('conly', None, j))
    elif tag == 'delete':
        for i in range(i1, i2):
            pairs.append(('bonly', i, None))
    elif tag == 'insert':
        for j in range(j1, j2):
            pairs.append(('conly', None, j))


def in_a(q):
    q = norm(q)
    if len(q) < 20:
        return 0.0
    al = fuzz.partial_ratio_alignment(q, ATEXT, score_cutoff=0)
    if al is None:
        return 0.0
    return fuzz.ratio(q, ATEXT[al.dest_start:al.dest_end]) / 100


NOISE = re.compile(r'^[\s\-\u2022\u00b7\.\,\|\d:]*$')

records = []
for kind, i, j in pairs:
    if kind == 'same':
        continue
    b = Bn[i] if i is not None else ''
    c = Cn[j] if j is not None else ''
    if '-----' in b or '-----' in c:
        continue
    if NOISE.match(b) and NOISE.match(c):
        continue
    if kind == 'mod':
        if b.lower() == c.lower():
            continue
        sa_b, sa_c = in_a(b), in_a(c)
        if sa_b >= 0.90 and sa_c < sa_b - 0.04:
            verdict = 'C_CHANGED'      # A agrees with B -> C is the innovator
        elif sa_c >= 0.90 and sa_b < sa_c - 0.04:
            verdict = 'B_CHANGED'      # A agrees with C -> B (Allen) is the innovator
        else:
            verdict = 'A_SILENT'
        records.append({'kind': 'mod', 'verdict': verdict, 'b': b, 'c': c,
                        'aB': round(sa_b, 3), 'aC': round(sa_c, 3),
                        'sim': round(fuzz.ratio(b.lower(), c.lower()) / 100, 3)})
    elif kind == 'bonly':
        if len(b.split()) < 5:
            continue
        records.append({'kind': 'bonly', 'verdict': 'IN_B_NOT_C', 'b': b, 'c': '',
                        'aB': round(in_a(b), 3), 'aC': 0.0, 'sim': 0.0})
    elif kind == 'conly':
        if len(c.split()) < 5:
            continue
        records.append({'kind': 'conly', 'verdict': 'IN_C_NOT_B', 'b': '', 'c': c,
                        'aB': 0.0, 'aC': round(in_a(c), 3), 'sim': 0.0})

json.dump(records, open('MERGE.json', 'w'), indent=1)
from collections import Counter
print('B paras:', len(B), ' C paras:', len(C))
print(Counter(r['verdict'] for r in records))
