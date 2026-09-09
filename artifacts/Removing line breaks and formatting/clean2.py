import re

path = 'unpacked/word/document.xml'
x = open(path, encoding='utf-8').read()

EMOJI = '\U0001F3AC\U0001F449'

# ---- 1. strip emojis (and the single space that follows) inside <w:t> ----
def strip_emoji(m):
    return m.group(1) + re.sub('[' + EMOJI + ']\u0020?', '', m.group(2)) + m.group(3)

x = re.sub(r'(<w:t[^>]*>)(.*?)(</w:t>)', strip_emoji, x, flags=re.S)

# ---- 2. rejoin the header sentence that was split across two paragraphs ----
x = x.replace(
    'BOOK 5 - MEETINGS - Design intentional family meetings that create rhythm, clarity,</w:t>',
    'BOOK 5 - MEETINGS - Design intentional family meetings that create rhythm, clarity, '
    'and shared direction over time.</w:t>', 1)

PARA_RE = r'<w:p\b(?:(?!<w:p\b).)*?</w:p>|<w:p\b[^>]*/>'


def text_of(p):
    return ''.join(re.findall(r'<w:t[^>]*>(.*?)</w:t>', p, re.S))


for p in re.findall(PARA_RE, x, re.S):
    if text_of(p).strip() == 'and shared direction over time.':
        x = x.replace(p, '', 1)
        break

# ---- 3. remove divider rules and blank paragraphs; keep page breaks ----
rules = blanks = pagebreaks = 0
for p in re.findall(PARA_RE, x, re.S):
    if text_of(p).strip():
        continue
    if 'w:type="page"' in p:
        pagebreaks += 1
        continue
    if 'o:hr="t"' in p:
        x = x.replace(p, '', 1)
        rules += 1
        continue
    if '<w:drawing' in p or '<w:pict' in p or '<w:sectPr' in p:
        continue
    x = x.replace(p, '', 1)
    blanks += 1

open(path, 'w', encoding='utf-8').write(x)

print('horizontal-rule dividers removed:', rules)
print('blank paragraphs removed:', blanks)
print('page-break paragraphs preserved:', pagebreaks)
print('emoji remaining:', sum(x.count(c) for c in EMOJI))
print('hr remaining:', x.count('o:hr="t"'))
