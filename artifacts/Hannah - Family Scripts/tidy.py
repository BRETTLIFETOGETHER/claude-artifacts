#!/usr/bin/env python3
import re, sys

src = '/mnt/user-data/outputs/Book2_Clarity_Family_All_Sessions.md'
lines = open(src, encoding='utf-8').read().split('\n')

out = []
buf = []

def flush():
    if buf:
        out.append(' '.join(x.strip() for x in buf))
        buf.clear()

for ln in lines:
    s = ln.rstrip()
    st = s.strip()
    # drop standalone horizontal rules (but not table separators)
    if st == '---':
        flush()
        continue
    # structural lines stay on their own line
    if (st.startswith('#') or st.startswith('|') or st.startswith('>')
            or st == '' or re.fullmatch(r'\*\*[A-Za-z ]+: [A-Z]+\*\*', st)
            or st.startswith('*Source:')):
        flush()
        out.append(s)
        continue
    buf.append(s)
flush()

# collapse 3+ blank lines to one blank line
txt = '\n'.join(out)
txt = re.sub(r'\n{3,}', '\n\n', txt)
open(src, 'w', encoding='utf-8').write(txt.strip() + '\n')

print('dividers removed, paragraphs unwrapped')
print('lines:', len(txt.split(chr(10))))
print('words:', len(txt.split()))
