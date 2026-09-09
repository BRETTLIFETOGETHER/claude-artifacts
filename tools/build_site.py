#!/usr/bin/env python3
"""Build the three-page artifact site: Deliverables / Source / Everything.

Pre-renders Markdown to HTML and code to highlighted HTML so every page is
fully static -- no CDN, no fetch, works from disk and from Netlify alike.
"""
import os, re, sys, json, html, shutil, urllib.parse, datetime

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from site_assets import CSS, JS

import markdown
from pygments import highlight
from pygments.lexers import get_lexer_by_name, TextLexer
from pygments.formatters import HtmlFormatter

ROOT  = os.path.expanduser('~/Desktop/claude-artifacts')
ART   = os.path.join(ROOT, 'artifacts')
VIEW  = os.path.join(ROOT, 'view')
ASSET = os.path.join(ROOT, 'assets')
META  = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'meta.json')

# Front-facing = a finished document a person reads.
DELIVERABLE_EXT = {'html', 'svg', 'md'}
LEXER = {'py': 'python', 'js': 'javascript', 'jsx': 'jsx', 'json': 'json',
         'css': 'css', 'gs': 'javascript', 'txt': 'text', 'md': 'markdown',
         'html': 'html', 'svg': 'xml'}

PAGES = [
    ('index.html',  'deliverable', 'Deliverables',
     'Finished, front-facing documents — web pages, rendered writing, and graphics.'),
    ('source.html', 'source', 'Source &amp; Build',
     'The machinery behind the deliverables — scripts, builders, and data files.'),
    ('all.html',    'all', 'Everything',
     'Every reconstructed artifact, unfiltered.'),
]

# --------------------------------------------------------------------------- utils
def q(s):
    return urllib.parse.quote(s)

def esc(s):
    return html.escape(s, quote=True)

def human(n):
    if n < 1024:            return f'{n} B'
    if n < 1024 * 1024:     return f'{n/1024:.0f} KB'
    return f'{n/1048576:.1f} MB'

def strip_markup(t):
    t = re.sub(r'<script[\s\S]*?</script>', ' ', t, flags=re.I)
    t = re.sub(r'<style[\s\S]*?</style>', ' ', t, flags=re.I)
    t = re.sub(r'<[^>]+>', ' ', t)
    t = html.unescape(t)
    return re.sub(r'\s+', ' ', t).strip()

def read(p):
    with open(p, 'r', encoding='utf-8', errors='replace') as f:
        return f.read()

# --------------------------------------------------------------------------- metadata
meta = json.load(open(META, encoding='utf-8'))
cmeta, fmeta = {}, {}
for c in meta:
    cmeta[c['dir']] = c
    for e in c['entries']:
        fmeta[(c['dir'], e['file'])] = e

# --------------------------------------------------------------------------- collect
records = []
for d in sorted(os.listdir(ART)):
    dp = os.path.join(ART, d)
    if not os.path.isdir(dp):
        continue
    for fn in sorted(os.listdir(dp)):
        fp = os.path.join(dp, fn)
        if not os.path.isfile(fp):
            continue
        ext = fn.rpartition('.')[2].lower()
        em  = fmeta.get((d, fn), {})
        records.append({
            'conv': d, 'file': fn, 'ext': ext, 'path': fp,
            'size': os.path.getsize(fp),
            'raw':  'artifacts/' + q(d) + '/' + q(fn),
            'kind': 'deliverable' if ext in DELIVERABLE_EXT else 'source',
            'desc': em.get('desc', ''), 'edits': em.get('edits', 0),
            'bash': em.get('bash', False), 'presented': em.get('presented', False),
            'srcpath': em.get('src_path', ''),
        })

by_conv = {}
for r in records:
    by_conv.setdefault(r['conv'], []).append(r)

print(f'collected {len(records)} files in {len(by_conv)} conversations')

# --------------------------------------------------------------------------- viewer pages
os.makedirs(VIEW, exist_ok=True)
md_engine = markdown.Markdown(extensions=[
    'extra', 'tables', 'fenced_code', 'sane_lists', 'toc', 'admonition'])
formatter = HtmlFormatter(nowrap=False, style='default', cssclass='hl')
formatter_dark = HtmlFormatter(nowrap=False, style='monokai', cssclass='hl')

def chrome(title, body, depth, extra_head=''):
    up = '../' * depth
    return f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="robots" content="noindex,nofollow">
<title>{esc(title)}</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{up}assets/site.css">{extra_head}
</head><body>
{body}
<script src="{up}assets/site.js" defer></script>
</body></html>"""

def badges(r):
    out = []
    if r['presented']:
        out.append('<span class="b ok" title="This file was delivered to you in the conversation">delivered</span>')
    if r['edits']:
        out.append(f'<span class="b" title="Incremental edits replayed onto this file">{r["edits"]} edit'
                   f'{"s" if r["edits"] != 1 else ""}</span>')
    if r['bash']:
        out.append('<span class="b warn" title="Also modified by shell commands the export does not record — '
                   'this reconstruction may lag the true final version">shell-touched</span>')
    return ''.join(out)

viewer_count = 0
for r in records:
    ext = r['ext']
    if ext in ('html', 'svg'):
        r['href'] = r['raw']          # already a live document
        continue

    text = read(r['path'])
    cm = cmeta.get(r['conv'], {})
    if ext == 'md':
        md_engine.reset()
        inner = f'<article class="doc">{md_engine.convert(text)}</article>'
    else:
        try:
            lx = get_lexer_by_name(LEXER.get(ext, 'text'))
        except Exception:
            lx = TextLexer()
        inner = f'<div class="codewrap">{highlight(text, lx, formatter)}</div>'

    body = f"""<header class="vhead"><div class="wrap">
<div class="crumb"><a href="../../index.html">← All artifacts</a> &nbsp;·&nbsp; {esc(r['conv'])}</div>
<h1>{esc(r['file'])}</h1>
<div class="meta"><span class="ext e-{esc(ext)}">{esc(ext)}</span>{badges(r)}
<span class="b">{human(r['size'])}</span>
<a class="btn" href="../../{r['raw']}" download>Download raw</a>
<button class="btn" id="theme" type="button">Theme</button></div>
{f'<p class="crumb" style="margin-top:9px">{esc(r["desc"])}</p>' if r['desc'] else ''}
</div></header>
{inner}
<footer><div class="wrap">Reconstructed from <code>{esc(r['srcpath'] or r['file'])}</code></div></footer>"""

    outdir = os.path.join(VIEW, r['conv'])
    os.makedirs(outdir, exist_ok=True)
    outfp = os.path.join(outdir, r['file'] + '.html')
    with open(outfp, 'w', encoding='utf-8') as f:
        f.write(chrome(r['file'], body, 2))
    r['href'] = 'view/' + q(r['conv']) + '/' + q(r['file'] + '.html')
    viewer_count += 1

print(f'rendered {viewer_count} viewer pages')

# --------------------------------------------------------------------------- search index
idx = []
for r in records:
    body = read(r['path'])
    if r['ext'] in ('html', 'svg'):
        body = strip_markup(body)
    else:
        body = re.sub(r'\s+', ' ', body)
    idx.append({'k': r['raw'], 't': body[:2000]})
with open(os.path.join(ROOT, 'search-index.json'), 'w', encoding='utf-8') as f:
    json.dump(idx, f, separators=(',', ':'))
print(f'search index: {os.path.getsize(os.path.join(ROOT,"search-index.json"))/1048576:.1f} MB')

# --------------------------------------------------------------------------- index pages
def conv_date(d):
    return (cmeta.get(d, {}).get('created_at') or '')[:10]

def render_page(fname, scope, label, blurb):
    rows, tot_files, tot_convs, ext_counts = [], 0, 0, {}
    order = sorted(by_conv.keys(), key=lambda d: (conv_date(d), d.lower()))
    for d in order:
        items = [r for r in by_conv[d] if scope == 'all' or r['kind'] == scope]
        if not items:
            continue
        tot_convs += 1
        lis = []
        for r in items:
            tot_files += 1
            ext_counts[r['ext']] = ext_counts.get(r['ext'], 0) + 1
            lis.append(
                f'<li data-n="{esc(r["file"].lower())}" data-ext="{esc(r["ext"])}" '
                f'data-k="{esc(r["raw"])}">'
                f'<span class="ext e-{esc(r["ext"])}">{esc(r["ext"])}</span>'
                f'<span class="fname"><a href="{r["href"]}">{esc(r["file"])}</a></span>'
                f'<span class="badges">{badges(r)}</span>'
                f'<span class="sz">{human(r["size"])}</span></li>')
        cm = cmeta.get(d, {})
        summ = cm.get('summary', '')
        sblock = (f'<details class="sum"><summary>Conversation summary</summary>'
                  f'<div class="body">{esc(summ)}</div></details>') if summ else ''
        total_sz = sum(r['size'] for r in items)
        rows.append(
            f'<section class="conv" data-n="{esc(d.lower())}" data-d="{esc(conv_date(d))}" '
            f'data-c="{len(items)}" data-sz="{total_sz}">'
            f'<h2>{esc(d)}<span class="date">{esc(conv_date(d))}</span>'
            f'<span class="ct">{len(items)}</span></h2>{sblock}'
            f'<ul class="files">{"".join(lis)}</ul></section>')

    chips = ''.join(
        f'<button class="chip" data-ext="{esc(e)}" aria-pressed="false" type="button">'
        f'{esc(e)}<span class="c">{n}</span></button>'
        for e, n in sorted(ext_counts.items(), key=lambda kv: -kv[1]))

    tab_parts = []
    for fn, sc, lb, _ in PAGES:
        cur = ' aria-current="page"' if fn == fname else ''
        n = sum(1 for r in records if sc == 'all' or r['kind'] == sc)
        tab_parts.append(f'<a href="{fn}"{cur}>{lb}<span class="n">{n}</span></a>')
    tabs = ''.join(tab_parts)

    words = sum(len(read(r['path']).split())
                for r in records if scope == 'all' or r['kind'] == scope)
    dates = [conv_date(d) for d in by_conv if conv_date(d)]

    body = f"""<header class="top"><div class="wrap">
<div class="brand"><h1>Claude Artifacts</h1><span class="sub">{esc(blurb)}</span></div>
<nav class="tabs">{tabs}</nav></div></header>
<div class="wrap">
<div class="stats">
<div class="stat"><div class="v">{tot_files:,}</div><div class="k">Files</div></div>
<div class="stat"><div class="v">{tot_convs:,}</div><div class="k">Conversations</div></div>
<div class="stat"><div class="v">{words/1000:,.0f}k</div><div class="k">Words</div></div>
<div class="stat"><div class="v">{min(dates) if dates else ''} – {max(dates) if dates else ''}</div>
<div class="k">Date range</div></div>
</div>
<div class="toolbar">
  <div class="searchrow">
    <input id="q" type="search" placeholder="Search filenames and contents…  ( / to focus )" autocomplete="off">
    <button class="btn" id="expand" type="button">Expand all</button>
    <button class="btn" id="theme" type="button">Theme</button>
  </div>
  <div class="chips">{chips}<span class="spacer"></span>
    <select class="sort" id="sort" aria-label="Sort conversations">
      <option value="old">Oldest first</option><option value="new">Newest first</option>
      <option value="name">A–Z</option><option value="count">Most files</option>
      <option value="size">Largest</option>
    </select>
  </div>
  <div id="count"></div>
</div>
{''.join(rows)}
<div class="empty hide" id="empty">No files match that search.</div>
<footer>Reconstructed from a Claude.ai data export ·
<a href="README.md">README</a> ·
<a href="https://github.com/BRETTLIFETOGETHER/claude-artifacts">Repository</a></footer>
</div>"""
    with open(os.path.join(ROOT, fname), 'w', encoding='utf-8') as f:
        f.write(chrome('Claude Artifacts — ' + label.replace('&amp;', '&'), body, 0))
    return tot_files

os.makedirs(ASSET, exist_ok=True)
light_hl = formatter.get_style_defs('.hl')
dark_hl_media = formatter_dark.get_style_defs(':root:not([data-theme="light"]) .hl')
dark_hl_attr  = formatter_dark.get_style_defs(':root[data-theme="dark"] .hl')
with open(os.path.join(ASSET, 'site.css'), 'w', encoding='utf-8') as f:
    f.write(CSS
            + '\n/* ---- syntax highlighting: light ---- */\n' + light_hl
            + '\n/* ---- syntax highlighting: dark (system) ---- */\n'
            + '@media (prefers-color-scheme:dark){\n' + dark_hl_media + '\n}\n'
            + '\n/* ---- syntax highlighting: dark (explicit toggle) ---- */\n'
            + dark_hl_attr + '\n')
with open(os.path.join(ASSET, 'site.js'), 'w', encoding='utf-8') as f:
    f.write(JS)

for fn, sc, lb, bl in PAGES:
    n = render_page(fn, sc, lb, bl)
    print(f'  {fn:14s} {n:5d} files')

# --------------------------------------------------------------------------- extras
with open(os.path.join(ROOT, '404.html'), 'w', encoding='utf-8') as f:
    f.write(chrome('Not found', """<div class="wrap"><div class="empty">
<h1 style="font-family:Fraunces,Georgia,serif">Page not found</h1>
<p>That file isn't here. Try the <a href="/index.html">deliverables index</a>,
the <a href="/source.html">source index</a>, or
<a href="/all.html">everything</a>.</p></div></div>""", 0))
with open(os.path.join(ROOT, 'robots.txt'), 'w', encoding='utf-8') as f:
    f.write('User-agent: *\nDisallow: /\n')
print('wrote 404.html, robots.txt')
