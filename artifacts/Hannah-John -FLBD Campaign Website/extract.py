import re, sys
from bs4 import BeautifulSoup

def clean(path, out):
    html = open(path, encoding='utf-8', errors='ignore').read()
    # remove data: URIs (fonts/images) to shrink
    html = re.sub(r'url\(data:[^)]*\)', 'url(DATA)', html)
    html = re.sub(r'src="data:[^"]*"', 'src="DATA"', html)
    soup = BeautifulSoup(html, 'html.parser')
    for tag in soup(['script']):
        tag.decompose()

    lines = []
    lines.append(f"TITLE: {soup.title.string if soup.title else 'NONE'}")

    # design tokens from CSS
    css = ' '.join(s.get_text() for s in soup.find_all('style'))
    colors = sorted(set(re.findall(r'#[0-9a-fA-F]{6}\b', css)))
    fonts = sorted(set(re.findall(r"font-family:\s*'([^']+)'", css)))
    vars_ = sorted(set(re.findall(r'(--[\w-]+)\s*:\s*([^;]{1,40})', css)))
    lines.append(f"FONTS: {fonts}")
    lines.append(f"COLORS({len(colors)}): {colors[:40]}")
    lines.append("CSS VARS: " + '; '.join(f"{k}={v.strip()}" for k, v in vars_[:40]))
    lines.append("=" * 60)

    # structural text walk: headings + text
    body = soup.body or soup
    seen = set()
    for el in body.find_all(['h1','h2','h3','h4','h5','h6','p','li','a','button','blockquote','figcaption','span','div']):
        # only leaf-ish elements to avoid duplicates
        if el.find(['h1','h2','h3','h4','p','li','blockquote']):
            continue
        txt = ' '.join(el.get_text(' ', strip=True).split())
        if not txt or len(txt) < 2:
            continue
        key = (el.name, txt)
        if key in seen:
            continue
        seen.add(key)
        if el.name in ('h1','h2','h3','h4','h5','h6'):
            lines.append(f"\n[{el.name.upper()}] {txt}")
        elif el.name in ('a','button'):
            if len(txt) < 80:
                lines.append(f"  <btn/link> {txt}")
        elif el.name == 'blockquote':
            lines.append(f"  <quote> {txt}")
        else:
            if el.name in ('span','div') and len(txt) > 200:
                continue  # big containers already covered by leaves
            lines.append(f"  {txt}")
    open(out, 'w').write('\n'.join(lines))
    print(f"{path} -> {out}: {len(lines)} lines")

for name in ['Family_Legacy_Ecosystem_Diagram', 'Wisdom_Driven_Life', 'Family_Legacy_Collection']:
    clean(f'/mnt/user-data/uploads/{name}.html', f'/home/claude/tom/{name}.txt')
