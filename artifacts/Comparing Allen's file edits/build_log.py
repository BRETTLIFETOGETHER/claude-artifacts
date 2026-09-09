import re, difflib, json, unicodedata

A = open('A.md').read().split('\n')   # Shared = edited/current
B = open('B.md').read().split('\n')   # July 21 = older snapshot
pages = open('shared.txt').read().split('\f')

def norm(s):
    s = s.replace('\\', '')
    s = s.replace('\u2019', "'").replace('\u2018', "'")
    s = s.replace('\u201c', '"').replace('\u201d', '"')
    s = s.replace('\u2014', '-').replace('\u2013', '-')
    s = re.sub(r'\*+', '', s)
    s = re.sub(r'\s+', ' ', s)
    return s.strip()

pages_n = [norm(p) for p in pages]

def find_page(text):
    t = norm(text)
    # try progressively shorter distinctive windows
    for start in (0, 20, 40):
        words = t.split()
        for length in (14, 10, 7):
            if len(words) < start + length:
                continue
            probe = ' '.join(words[start:start+length])
            hits = [i+1 for i, p in enumerate(pages_n) if probe in p]
            if len(hits) == 1:
                return hits[0], hits
            if len(hits) > 1:
                return hits[0], hits
    return None, []

# section map from page number
def section_for(pg):
    if pg is None: return '?'
    bounds_leader = [(2,4,'Leader Guide — Front Matter'),(5,11,'Leader Guide — Session 1'),
                     (12,18,'Leader Guide — Session 2'),(19,25,'Leader Guide — Session 3'),
                     (26,33,'Leader Guide — Session 4'),(34,40,'Leader Guide — Session 5'),
                     (41,48,'Leader Guide — Session 6')]
    bounds_part = [(50,51,'Participant Guide — Front Matter'),(52,57,'Participant Guide — Session 1'),
                   (58,62,'Participant Guide — Session 2'),(63,67,'Participant Guide — Session 3'),
                   (68,73,'Participant Guide — Session 4'),(74,78,'Participant Guide — Session 5'),
                   (79,84,'Participant Guide — Session 6')]
    for lo, hi, name in bounds_leader + bounds_part:
        if lo <= pg <= hi:
            return name
    return 'p.%d' % pg

TOKEN = re.compile(r'\S+|\s+')

def word_changes(old, new):
    o = norm(old).split()
    n = norm(new).split()
    sm = difflib.SequenceMatcher(None, o, n, autojunk=False)
    out = []
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag == 'equal':
            continue
        pre = ' '.join(o[max(0, i1-4):i1])
        post = ' '.join(o[i2:i2+4])
        out.append({
            'from': ' '.join(o[i1:i2]),
            'to': ' '.join(n[j1:j2]),
            'pre': pre, 'post': post, 'tag': tag
        })
    return out

sm = difflib.SequenceMatcher(None, B, A, autojunk=False)
records = []
for tag, i1, i2, j1, j2 in sm.get_opcodes():
    if tag != 'replace':
        continue
    for k in range(max(i2-i1, j2-j1)):
        old = B[i1+k] if i1+k < i2 else ''
        new = A[j1+k] if j1+k < j2 else ''
        if norm(old) == norm(new):
            continue
        pg, hits = find_page(new)
        records.append({'line': j1+k+1, 'page': pg, 'hits': hits,
                        'section': section_for(pg), 'old': old, 'new': new,
                        'changes': word_changes(old, new)})

json.dump(records, open('records.json', 'w'), indent=1)
print('records:', len(records))
print('unpaged:', sum(1 for r in records if r['page'] is None))
from collections import Counter
print(Counter(r['section'] for r in records))
