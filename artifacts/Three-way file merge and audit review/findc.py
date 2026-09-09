import re, json, unicodedata
from rapidfuzz import fuzz
from rapidfuzz.distance import Indel

def norm(s):
    s = unicodedata.normalize('NFKC', s)
    s = s.replace('\u2019', "'").replace('\u2018', "'")
    s = s.replace('\u201c', '"').replace('\u201d', '"')
    for d in '\u2014\u2013\u2012\u2212\u2010\u2011':
        s = s.replace(d, '-')
    s = re.sub(r'!\[\]\([^)]*\)(\{[^}]*\})?', '', s)
    s = re.sub(r'[*_>#`|\[\]]', '', s)
    s = re.sub(r'\s+', ' ', s)
    return s.strip().lower()

C = json.load(open('C_paras.json'))
# build continuous normalized stream with page map
stream = []
pagemap = []
for x in C:
    n = norm(x['text'])
    if not n:
        continue
    if stream:
        stream.append(' '); pagemap.append(x['page'])
    for ch in n:
        stream.append(ch); pagemap.append(x['page'])
CTEXT = ''.join(stream)

def locate(query, min_score=0.0):
    """Return (score 0-1, page, matched C substring) for best fuzzy substring match."""
    q = norm(query)
    q = re.sub(r'^\s*\d+[\.\)]\s*', '', q)
    if len(q) < 15:
        return (0.0, None, '')
    al = fuzz.partial_ratio_alignment(q, CTEXT, score_cutoff=0)
    if al is None:
        return (0.0, None, '')
    s, e = al.dest_start, al.dest_end
    sub = CTEXT[s:e]
    score = fuzz.ratio(q, sub) / 100.0
    pg = pagemap[min(s, len(pagemap) - 1)]
    return (score, pg, sub)
