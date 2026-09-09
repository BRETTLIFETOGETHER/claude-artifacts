import sys, re, json, unicodedata
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


# PDF stream with page map
P = json.load(open('C_paras.json'))
chars, pages = [], []
for x in P:
    n = norm(x['text'])
    if not n:
        continue
    if chars:
        chars.append(' '); pages.append(x['page'])
    for ch in n:
        chars.append(ch); pages.append(x['page'])
PTEXT = ''.join(chars)

D = load_paras('C_current.md')
out = []
for p in D:
    q = norm(p)
    if len(q.split()) < 8 or '-----' in p:
        continue
    al = fuzz.partial_ratio_alignment(q, PTEXT, score_cutoff=0)
    if al is None:
        out.append({'score': 0.0, 'page': None, 'docx': q, 'pdf': ''})
        continue
    sub = PTEXT[al.dest_start:al.dest_end]
    sc = fuzz.ratio(q, sub) / 100
    out.append({'score': round(sc, 3), 'page': pages[al.dest_start], 'docx': q, 'pdf': sub})

json.dump(out, open('DOCX_vs_PDF.json', 'w'), indent=1)
bad = [o for o in out if o['score'] < 0.93]
print('paragraphs checked:', len(out), ' diverging (<0.93):', len(bad))
