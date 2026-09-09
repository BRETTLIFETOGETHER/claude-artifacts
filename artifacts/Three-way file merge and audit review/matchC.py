import re, json, difflib, unicodedata
from collections import defaultdict

def norm(s):
    s = unicodedata.normalize('NFKC', s)
    s = s.replace('\u2019', "'").replace('\u2018', "'")
    s = s.replace('\u201c', '"').replace('\u201d', '"')
    for d in '\u2014\u2013\u2012\u2212\u2010\u2011':
        s = s.replace(d, '-')
    s = re.sub(r'!\[\]\([^)]*\)(\{[^}]*\})?', '', s)
    s = re.sub(r'[*_>#`|]', '', s)
    s = re.sub(r'^\s*\d+[\.\)]\s*', '', s)
    s = re.sub(r'\s+', ' ', s)
    return s.strip().lower()

def toks(s):
    return set(re.findall(r'[a-z0-9]{3,}', s))

C = json.load(open('C_paras.json'))
Cn = [norm(x['text']) for x in C]

# also build sliding windows of consecutive C paragraphs (layout splits paragraphs)
windows = []
for i in range(len(C)):
    for w in (1, 2, 3, 4):
        if i + w <= len(C) and len(set(C[k]['page'] for k in range(i, i + w))) <= 2:
            txt = ' '.join(Cn[i:i + w])
            windows.append((i, w, txt, C[i]['page']))

idx = defaultdict(set)
for k, (i, w, txt, pg) in enumerate(windows):
    for t in toks(txt):
        idx[t].add(k)

def find(query):
    q = norm(query)
    qt = toks(q)
    if not qt:
        return (0.0, None, None)
    cand = defaultdict(int)
    for t in qt:
        s = idx.get(t)
        if s and len(s) < 3000:
            for k in s:
                cand[k] += 1
    ranked = sorted(cand.items(), key=lambda kv: -kv[1])[:60]
    best = 0.0; bestk = None
    for k, _ in ranked:
        sc = difflib.SequenceMatcher(None, q, windows[k][2]).ratio()
        if sc > best:
            best = sc; bestk = k
    if bestk is None:
        return (0.0, None, None)
    i, w, txt, pg = windows[bestk]
    return (best, pg, txt)
