import sys, os, re, json, collections
sys.path.insert(0, '.')
from stream import iter_conversations

DEST = sys.argv[1] if len(sys.argv) > 1 else None   # None => dry run
HEREDOC = re.compile(
    r"(?:cat|tee)\s+(?:-a\s+)?>\s*'?\"?([^\s'\"<>|]+)'?\"?\s*<<\s*-?\s*'?\"?([A-Za-z_][A-Za-z0-9_]*)'?\"?[ \t]*\n")

def heredoc_writes(cmd):
    """Yield (path, body) for simple `cat > path <<'EOF' ... EOF` writes."""
    for m in HEREDOC.finditer(cmd):
        path, delim = m.group(1), m.group(2)
        rest = cmd[m.end():]
        end = re.search(r'^[ \t]*%s[ \t]*$' % re.escape(delim), rest, re.M)
        if end:
            yield path, rest[:end.start()]

def sanitize(s, fallback='untitled'):
    s = (s or '').strip().replace('/', '-').replace('\\', '-')
    s = re.sub(r'[\x00-\x1f<>:"|?*]', '', s)
    s = re.sub(r'\s+', ' ', s).strip(' .')
    return (s[:120].strip(' .') or fallback)

def apply_edit(text, old, new):
    """Exact match first, then a whitespace-tolerant fallback."""
    if old and old in text:
        FUZZ['exact'] += 1
        return text.replace(old, new, 1), True
    if not old:
        return text, False
    pat = re.compile(r'\s+'.join(re.escape(t) for t in old.split()))
    m = pat.search(text)
    if m:
        FUZZ['fuzzy'] += 1
        return text[:m.start()] + new + text[m.end():], True
    return text, False

stats = collections.Counter()
FUZZ = collections.Counter()
conv_records = []
seen_conv_names = collections.Counter()

for conv in iter_conversations():
    stats['conversations'] += 1
    files, bash_touched, presented = {}, set(), set()
    order = [0]
    msgs = sorted(conv.get('chat_messages') or [], key=lambda m: (m.get('created_at') or ''))

    def touch(path, source, _files=files, _order=order):
        rec = _files.get(path)
        if rec is None:
            _order[0] += 1
            rec = _files[path] = {'text': '', 'creates': 0, 'edits': 0, 'failed': 0,
                                  'order': _order[0], 'desc': '', 'source': source}
        return rec

    for m in msgs:
        for b in (m.get('content') or []):
            if b.get('type') != 'tool_use':
                continue
            name, inp = b.get('name'), b.get('input')
            if not isinstance(inp, dict):
                continue

            if name == 'create_file' and 'file_text' in inp and inp.get('path'):
                rec = touch(inp['path'], 'create_file')
                rec['text'] = inp['file_text']
                rec['creates'] += 1
                rec['source'] = 'create_file'
                if inp.get('description'):
                    rec['desc'] = inp['description']
                stats['create_calls'] += 1

            elif name == 'str_replace' and 'old_str' in inp:
                stats['edit_calls'] += 1
                rec = files.get(inp.get('path') or '')
                if rec is None:
                    stats['edit_no_create'] += 1
                    continue
                rec['text'], ok = apply_edit(rec['text'], inp.get('old_str') or '', inp.get('new_str') or '')
                if ok:
                    rec['edits'] += 1; stats['edit_applied'] += 1
                else:
                    rec['failed'] += 1; stats['edit_unmatched'] += 1

            elif name == 'present_files':
                for fp in (inp.get('filepaths') or []):
                    presented.add(fp)
                    stats['presented'] += 1

            elif name == 'bash_tool':
                cmd = str(inp.get('command') or inp.get('script') or '')
                for path, body in heredoc_writes(cmd):
                    rec = touch(path, 'heredoc')
                    rec['text'] = body
                    rec['creates'] += 1
                    stats['heredoc_writes'] += 1
                for p in files:
                    base = p.rsplit('/', 1)[-1]
                    if base and base in cmd:
                        bash_touched.add(p)

    # Keep create_file artifacts; keep heredoc files only if they were delivered to the user.
    keep = {p: r for p, r in files.items()
            if r['source'] == 'create_file' or p in presented
            or p.rsplit('/', 1)[-1] in {q.rsplit('/', 1)[-1] for q in presented}}
    if not keep:
        continue

    cname = sanitize(conv.get('name'), 'untitled-conversation')
    seen_conv_names[cname] += 1
    if seen_conv_names[cname] > 1:
        cname = f"{cname}-{seen_conv_names[cname]}"

    entries, used = [], collections.Counter()
    for p, rec in sorted(keep.items(), key=lambda kv: kv[1]['order']):
        base = p.rsplit('/', 1)[-1]
        stem, dot, ext = base.rpartition('.')
        if not dot:
            stem, ext = base, 'txt'
        stem = sanitize(stem, 'untitled')
        ext = re.sub(r'[^A-Za-z0-9]', '', ext)[:10] or 'txt'
        key = f"{stem}.{ext}"
        used[key] += 1
        if used[key] > 1:
            key = f"{stem}-{used[key]}.{ext}"
        entries.append({'file': key, 'title': base, 'src_path': p, 'text': rec['text'],
                        'creates': rec['creates'], 'edits': rec['edits'], 'failed': rec['failed'],
                        'desc': rec['desc'], 'source': rec['source'],
                        'presented': p in presented, 'bash': p in bash_touched})
        stats['artifacts'] += 1
        if rec['edits']:
            stats['artifacts_with_updates'] += 1
        if rec['creates'] > 1:
            stats['artifacts_rewritten'] += 1
        if p in bash_touched:
            stats['artifacts_bash_touched'] += 1
        if rec['source'] == 'heredoc':
            stats['artifacts_from_bash'] += 1

    conv_records.append({'name': conv.get('name') or 'Untitled', 'dir': cname,
                         'summary': conv.get('summary') or '',
                         'created_at': conv.get('created_at') or '',
                         'updated_at': conv.get('updated_at') or '',
                         'uuid': conv.get('uuid') or '', 'entries': entries})
    stats['conversations_with_artifacts'] += 1

print(json.dumps(dict(sorted(stats.items())), indent=2))
print('match modes:', dict(FUZZ))
if not DEST:
    sys.exit(0)

# ---------- write ----------
art = os.path.join(DEST, 'artifacts')
os.makedirs(art, exist_ok=True)
written = 0
for cr in conv_records:
    d = os.path.join(art, cr['dir'])
    os.makedirs(d, exist_ok=True)
    for e in cr['entries']:
        with open(os.path.join(d, e['file']), 'w', encoding='utf-8') as fh:
            fh.write(e['text'])
        written += 1

conv_records.sort(key=lambda c: c['created_at'])
lines = [
    '# Claude Artifacts',
    '',
    f"Extracted from a Claude.ai data export (`conversations.json`, {stats['conversations']} conversations).",
    f"**{stats['artifacts']} artifacts** recovered across **{stats['conversations_with_artifacts']} conversations**; "
    f"{stats['artifacts_with_updates']} had incremental edits replayed onto them.",
    '',
    '## Index',
    '',
]
for cr in conv_records:
    date = (cr['created_at'] or '')[:10]
    lines += [f"### {cr['name']}", '', f"*{date} — {len(cr['entries'])} artifact(s)*", '']
    for e in cr['entries']:
        rel = f"artifacts/{cr['dir']}/{e['file']}".replace(' ', '%20')
        flags = []
        if e['edits']:
            flags.append(f"{e['edits']} edit{'s' if e['edits'] != 1 else ''} applied")
        if e['creates'] > 1:
            flags.append(f"rewritten {e['creates']}x")
        if e['failed']:
            flags.append(f"{e['failed']} edit(s) unmatched")
        if e['bash']:
            flags.append('also modified by shell — may be incomplete')
        note = f" — {e['desc']}" if e['desc'] else ''
        suffix = f" _({'; '.join(flags)})_" if flags else ''
        lines.append(f"- [`{e['title']}`]({rel}){note}{suffix}")
    lines.append('')

lines += [
    '## Notes on fidelity',
    '',
    'This export is a newer-format Claude.ai export: it contains no `<antArtifact>` tags and no',
    '`artifacts` tool calls. Deliverables are produced instead by the file tools',
    '`create_file` (create/rewrite), `str_replace` (update), and `present_files` (deliver).',
    'Each file here is the final state after replaying every `create_file` and `str_replace`',
    'for that path in message order.',
    '',
    f"- {stats['edit_applied']} of {stats['edit_calls']} `str_replace` edits were replayed successfully.",
    f"- {stats['edit_no_create']} edits targeted files that were never created via `create_file` "
    '(they were written by shell commands inside the sandbox), so those files could not be reconstructed.',
    f"- {stats['edit_unmatched']} edits did not match the reconstructed text and were skipped.",
    f"- {stats['artifacts_bash_touched']} files were also modified by shell commands; the export records the",
    '  commands but not the resulting file contents, so those versions may lag the true final state.',
    f"- {stats['presented']} file deliveries were recorded overall. Many delivered files (PDFs, XLSX, and",
    '  outputs generated by scripts) have no text content in the export and therefore cannot be recovered.',
    '',
]
meta_out = os.environ.get('META_OUT')
if meta_out:
    with open(meta_out, 'w', encoding='utf-8') as fh:
        json.dump([{**cr, 'entries': [{k: v for k, v in e.items() if k != 'text'}
                                      for e in cr['entries']]} for cr in conv_records], fh, indent=1)
    print('META ->', meta_out)

with open(os.path.join(DEST, 'README.md'), 'w', encoding='utf-8') as fh:
    fh.write('\n'.join(lines))
print(f"WROTE {written} files under {art}")
