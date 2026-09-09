# Build tools

Regenerating this site from the original Claude.ai export.

| Script | Role |
|---|---|
| `stream.py` | Incremental parser for the 335 MB `conversations.json` (never loads it whole) |
| `extract.py` | Replays `create_file` / `str_replace` tool calls in message order to reconstruct each artifact's final state |
| `site_assets.py` | CSS + JS for the site |
| `build_site.py` | Renders Markdown, highlights code, builds the three index pages and the search index |

## Usage

```bash
python3 -m venv venv && ./venv/bin/pip install markdown pygments
META_OUT=meta.json ./venv/bin/python extract.py /path/to/repo
./venv/bin/python build_site.py
```

`extract.py` is deterministic — re-running it over the same export produces
byte-identical output.

## Known limits

The export records tool *calls*, not the sandbox filesystem. Files written or
modified by shell commands can't be fully reconstructed; those are flagged
`shell-touched` in the UI. Binary deliverables (PDF, XLSX) have no text in the
export and are not recoverable.
