import re

path = 'unpacked/word/document.xml'
x = open(path, encoding='utf-8').read()
orig = x

# ---- 1. strip emojis (and the space that follows them) inside <w:t> ----
EMOJI = '\U0001F3AC\U0001F449'


def strip_emoji(m):
    body = m.group(2)
    body = re.sub('[' + EMOJI + ']\u0020?', '', body)
    return m.group(1) + body + m.group(3)


x = re.sub(r'(<w:t[^>]*>)(.*?)(</w:t>)', strip_emoji, x, flags=re.S)

# ---- 2. rejoin the sentence split across two paragraphs at the top ----
x = x.replace(
    'BOOK 5 - MEETINGS - Design intentional family meetings that create rhythm, clarity,</w:t>',
    'BOOK 5 - MEETINGS - Design intentional family meetings that create rhythm, clarity, '
    'and shared direction over time.</w:t>', 1)

paras = re.findall(r'<w:p\b(?:(?!<w:p\b).)*?</w:p>|<w:p\b[^>]*/>', x, re.S)


def text_of(p):
    return ''.join(re.findall(r'<w:t[^>]*>(.*?)</w:t>', p, re.S))


# remove the now-duplicated trailing half of that sentence
for p in paras:
    if text_of(p).strip() == 'and shared direction over time.':
        x = x.replace(p, '', 1)
        break

# ---- 3. delete empty paragraphs, but keep any that carry a page break ----
paras = re.findall(r'<w:p\b(?:(?!<w:p\b).)*?</w:p>|<w:p\b[^>]*/>', x, re.S)
removed = 0
kept_pagebreaks = 0
for p in paras:
    if text_of(p).strip():
        continue
    if 'w:type="page"' in p:
        kept_pagebreaks += 1
        continue
    if '<w:drawing' in p or '<w:pict' in p or '<w:sectPr' in p:
        continue
    x = x.replace(p, '', 1)
    removed += 1

open(path, 'w', encoding='utf-8').write(x)

# ---- 4. give paragraphs a little breathing room so removing blanks
#         doesn't render as a solid wall of text ----
spath = 'unpacked/word/styles.xml'
s = open(spath, encoding='utf-8').read()
s = s.replace('<w:pPrDefault><w:pPr><w:spacing w:line="276" w:lineRule="auto"/></w:pPr></w:pPrDefault>',
              '<w:pPrDefault><w:pPr><w:spacing w:after="120" w:line="276" w:lineRule="auto"/></w:pPr></w:pPrDefault>', 1)
open(spath, 'w', encoding='utf-8').write(s)

print('empty paragraphs removed:', removed)
print('page-break paragraphs preserved:', kept_pagebreaks)
print('emoji remaining:', sum(x.count(c) for c in EMOJI))
