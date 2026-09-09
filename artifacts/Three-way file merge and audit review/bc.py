import sys, json, re, difflib
sys.path.insert(0, '.')
from findc import locate, norm, CTEXT
from loadp import load_paras
from rapidfuzz import fuzz

A = load_paras('A_base.md')
B = load_paras('B_pg.md')
An = [norm(x) for x in A]
ATEXT = ' '.join(An)

def in_a(query):
    q = norm(query)
    q = re.sub(r'^\s*\d+[\.\)]\s*', '', q)
    if len(q) < 15:
        return (0.0, '')
    al = fuzz.partial_ratio_alignment(q, ATEXT, score_cutoff=0)
    if al is None:
        return (0.0, '')
    sub = ATEXT[al.dest_start:al.dest_end]
    return (fuzz.ratio(q, sub) / 100.0, sub)

rows = []
for i, p in enumerate(B):
    n = norm(p)
    if len(n.split()) < 6:
        continue
    scC, pg, subC = locate(p)
    scA, subA = in_a(p)
    rows.append({'i': i, 'b': p, 'scC': round(scC, 4), 'pg': pg, 'c': subC,
                 'scA': round(scA, 4), 'a': subA})

json.dump(rows, open('BC_rows.json', 'w'), indent=1)
diff = [r for r in rows if r['scC'] < 0.985]
print('B paras compared:', len(rows), ' differing from C:', len(diff))
