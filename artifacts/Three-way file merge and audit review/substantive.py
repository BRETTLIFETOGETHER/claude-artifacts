import json, difflib, re, sys
sys.path.insert(0, '.')
from findc import norm, locate, CTEXT
from loadp import load_paras
from rapidfuzz import fuzz

A = load_paras('A_base.md')
ATEXT = ' '.join(norm(x) for x in A)

STOPNOISE = re.compile(r'^[\-\u2022\u00b7\u2014\u2013\.\,\s\|\d]*$')

def in_a(q):
    q = norm(q)
    if len(q) < 15:
        return (0.0, '')
    al = fuzz.partial_ratio_alignment(q, ATEXT, score_cutoff=0)
    if al is None:
        return (0.0, '')
    sub = ATEXT[al.dest_start:al.dest_end]
    return (fuzz.ratio(q, sub) / 100.0, sub)

rows = json.load(open('BC_rows.json'))
out = []
for r in rows:
    if r['scC'] >= 0.985 or r['scC'] < 0.55:
        continue
    b = norm(r['b']); c = r['c']
    if '-----' in r['b']:
        continue
    bw = b.split(); cw = c.split()
    sm = difflib.SequenceMatcher(None, bw, cw, autojunk=False)
    subs = []
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag == 'equal':
            continue
        x = ' '.join(bw[i1:i2]); y = ' '.join(cw[j1:j2])
        # skip truncation at the very start/end of the matched window
        if i1 == 0 or i2 == len(bw):
            continue
        if STOPNOISE.match(x) and STOPNOISE.match(y):
            continue
        # skip if it's only a bullet/dash swap
        if x.strip('-•·. ') == y.strip('-•·. '):
            continue
        subs.append((tag, x, y))
    if not subs:
        continue
    sa, asub = in_a(r['b'])
    out.append({'pg': r['pg'], 'scC': r['scC'], 'scA': round(sa, 3),
                'b': r['b'], 'c': c, 'a': asub, 'subs': subs})

json.dump(out, open('SUBSTANTIVE.json', 'w'), indent=1)
print('substantive diffs:', len(out))
for r in out:
    print('=' * 70)
    print(f"PAGE {r['pg']}   B~C={r['scC']}   B~A={r['scA']}")
    for t, x, y in r['subs']:
        print(f"   [{t}]  B: '{x}'")
        print(f"          C: '{y}'")
