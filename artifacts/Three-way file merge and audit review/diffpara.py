import re, difflib, json, sys, unicodedata

def load_paras(path):
    txt = open(path, encoding='utf-8').read()
    # unescape pandoc backslash escapes
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
    s = s.replace('\u2014', '-').replace('\u2013', '-').replace('\u2012','-').replace('\u2212','-')
    s = re.sub(r'[*_>#`]', '', s)
    s = re.sub(r'!\[\]\([^)]*\)\{[^}]*\}', '', s)
    s = re.sub(r'\s+', ' ', s)
    return s.strip().lower()

A = load_paras(sys.argv[1])
B = load_paras(sys.argv[2])
An = [norm(x) for x in A]
Bn = [norm(x) for x in B]

sm = difflib.SequenceMatcher(None, An, Bn, autojunk=False)
ops = sm.get_opcodes()

results = []
for tag, i1, i2, j1, j2 in ops:
    if tag == 'equal':
        continue
    results.append({'tag': tag, 'A': A[i1:i2], 'B': B[j1:j2], 'ai': i1, 'bi': j1})

# second pass: within replace blocks, try to pair up similar paragraphs
refined = []
for r in results:
    if r['tag'] == 'replace' and len(r['A']) and len(r['B']):
        used_b = set()
        pairs = []
        for a in r['A']:
            best = None; bestscore = 0; bestidx = None
            for k, b in enumerate(r['B']):
                if k in used_b: continue
                sc = difflib.SequenceMatcher(None, norm(a), norm(b)).ratio()
                if sc > bestscore:
                    bestscore = sc; best = b; bestidx = k
            if bestscore >= 0.55:
                used_b.add(bestidx); pairs.append(('mod', a, best, bestscore))
            else:
                pairs.append(('del', a, None, 0))
        for k, b in enumerate(r['B']):
            if k not in used_b:
                pairs.append(('add', None, b, 0))
        for p in pairs:
            refined.append({'tag': p[0], 'A': p[1], 'B': p[2], 'score': p[3], 'ai': r['ai'], 'bi': r['bi']})
    elif r['tag'] == 'delete':
        for a in r['A']:
            refined.append({'tag': 'del', 'A': a, 'B': None, 'score': 0, 'ai': r['ai'], 'bi': r['bi']})
    elif r['tag'] == 'insert':
        for b in r['B']:
            refined.append({'tag': 'add', 'A': None, 'B': b, 'score': 0, 'ai': r['ai'], 'bi': r['bi']})

json.dump(refined, open(sys.argv[3], 'w'), indent=1)
mods = [r for r in refined if r['tag']=='mod']
dels = [r for r in refined if r['tag']=='del']
adds = [r for r in refined if r['tag']=='add']
print(f'A paras: {len(A)}  B paras: {len(B)}')
print(f'MOD {len(mods)}  DEL {len(dels)}  ADD {len(adds)}')
