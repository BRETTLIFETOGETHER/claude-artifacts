# -*- coding: utf-8 -*-
import json, html

data = json.load(open('/home/claude/final_ff/data.json'))

def esc(s):
    return html.escape(s, quote=False)

roman = ["I","II","III","IV","V","VI","VII","VIII","IX","X"]

catalog_html = []
counter = 1
for i, d in enumerate(data):
    catalog_html.append(f'''
<div class="category">
  <div class="cat-head">
    <span class="cat-num">{roman[i]}</span>
    <div>
      <h3>{esc(d['name'])}</h3>
      <p class="cat-sub">{esc(d['sub'])}</p>
    </div>
  </div>
  <div class="specimen-list">''')
    for title, sub in d['items']:
        catalog_html.append(f'''
    <div class="specimen">
      <span class="n">{counter:03d}</span>
      <div>
        <div class="t">{esc(title)}</div>
        <div class="s">{esc(sub)}</div>
      </div>
    </div>''')
        counter += 1
    catalog_html.append('</div>\n</div>')

open('/home/claude/final_ff/catalog_block.html', 'w').write("\n".join(catalog_html))
print("wrote", counter - 1, "entries")
