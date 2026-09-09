import re, difflib, json, sys, unicodedata
from collections import defaultdict

def load_paras(path):
    txt = open(path, encoding='utf-8').read()
    txt = re.sub(r'\\([\'"\[\]\*_#\.\-\\])', r'\1', txt)
    txt = txt.replace('\\\n', ' ')
    blocks = [b.strip() for b in re.split(r'\n\s*\n', txt)]
    out = []
    for b in blocks:
        b = re.sub(r'\s+', ' ', b).strip()
        if b:
            out.append(b)
    return out

def norm(s):
    s = unicodedata.normalize('NFKC', s)
    s = s.replace('\u2019', "'").replace('\u2018', "'")
    s = s.replace('\u201c', '"').replace('\u201d', '"')
    for d in '\u2014\u2013\u2012\u2212':
        s = s.replace(d, '-')
    s = re.sub(r'!\[\]\([^)]*\)(\{[^}]*\})?', '', s)
    s = re.sub(r'[*_>#`|]', '', s)
    s = re.sub(r'^\s*\d+\.\s*', '', s)
    s = re.sub(r'\s+', ' ', s)
    return s.strip().lower()

def toks(s):
    return set(re.findall(r'[a-z0-9]+', s))

A = load_paras(sys.argv[1]); B = load_paras(sys.argv[2])
An = [norm(x) for x in A]; Bn = [norm(x) for x in B]

# inverted index on rare-ish tokens for candidate generation
idx = defaultdict(set)
for j, b in enumerate(Bn):
    for t in toks(b):
        idx[t].add(j)

used = {}
pairs = []
for i, a in enumerate(An):
    at = toks(a)
    if not at:
        pairs.append((i, None, 0.0)); continue
    cand = defaultdict(int)
    for t in at:
        s = idx.get(t)
        if s and len(s) < 200:
            for j in s: cand[j] += 1
    ranked = sorted(cand.items(), key=lambda kv: -kv[1])[:40]
    best = None; bs = 0.0
    for j, _ in ranked:
        sc = difflib.SequenceMatcher(None, a, Bn[j]).ratio()
        if sc > bs: bs = sc; best = j
    pairs.append((i, best, bs))

# resolve conflicts: each B para claimed by best-scoring A
claim = {}
for i, j, sc in pairs:
    if j is None or sc < 0.60: continue
    if j not in claim or sc > claim[j][1]:
        claim[j] = (i, sc)
amatch = {v[0]: (j, v[1]) for j, v in claim.items()}

out = {'ident': [], 'mod': [], 'aonly': [], 'bonly': []}
for i, a in enumerate(A):
    if i in amatch:
        j, sc = amatch[i]
        if An[i] == Bn[j]:
            out['ident'].append({'i': i, 'j': j})
        else:
            out['mod'].append({'i': i, 'j': j, 'score': round(sc, 3), 'a': a, 'b': B[j]})
    else:
        out['aonly'].append({'i': i, 'a': a})
matched_b = set(amatch[i][0] for i in amatch)
for j, b in enumerate(B):
    if j not in matched_b:
        out['bonly'].append({'j': j, 'b': b})

json.dump(out, open(sys.argv[3], 'w'), indent=1)
print(f"A={len(A)} B={len(B)}  identical={len(out['ident'])} modified={len(out['mod'])} A-only={len(out['aonly'])} B-only={len(out['bonly'])}")
