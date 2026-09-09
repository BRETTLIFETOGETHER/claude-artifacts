import re, json, subprocess, unicodedata

# use raw (non-layout) extraction for better paragraph reflow
paras = []  # (page, text)
for p in range(1, 130):
    t = subprocess.run(['pdftotext', '-f', str(p), '-l', str(p), 'C_current.pdf', '-'],
                       capture_output=True, text=True).stdout
    t = t.replace('\x0c', '')
    # join hyphen-broken lines
    t = re.sub(r'(\w)-\n(\w)', r'\1\2', t)
    blocks = re.split(r'\n\s*\n', t)
    for b in blocks:
        b = re.sub(r'\s*\n\s*', ' ', b)
        b = re.sub(r'\s+', ' ', b).strip()
        if b:
            paras.append({'page': p, 'text': b})

json.dump(paras, open('C_paras.json', 'w'), indent=1)
print('paras:', len(paras))
print('total words:', sum(len(x['text'].split()) for x in paras))
