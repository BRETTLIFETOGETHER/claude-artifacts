# -*- coding: utf-8 -*-
import json, html

data = json.load(open('/home/claude/final_ff/data.json'))

def esc(s):
    return html.escape(s, quote=False)

def gen_sample_html(domain, limit=10):
    out = []
    for i, (title, sub) in enumerate(domain['items'][:limit], start=1):
        out.append((title, sub))
    return out

# Just use domain 1 (Flourishing Foundations, 10 items) as the representative sample for all three
sample_domain = data[0]
print(sample_domain['name'], len(sample_domain['items']))
json.dump(sample_domain, open('/home/claude/final_ff/sample.json', 'w'))
