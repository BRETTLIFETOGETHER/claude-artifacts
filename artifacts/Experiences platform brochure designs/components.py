# -*- coding: utf-8 -*-
import content as C

def env_rows():
    out = []
    for numeral, name, desc in C.ENVIRONMENTS:
        out.append(f'''
        <div class="env-row reveal">
          <div class="env-num">{numeral}</div>
          <div class="env-body">
            <h3>{name}</h3>
            <p>{desc}</p>
          </div>
        </div>''')
    return "".join(out)

def outcome_cols():
    out = []
    for name, desc in C.OUTCOMES:
        out.append(f'''
        <div class="outcome reveal">
          <h4>{name}</h4>
          <p>{desc}</p>
        </div>''')
    return "".join(out)

def rhythm_blocks():
    out = []
    for i, stage in enumerate(C.RHYTHM, start=1):
        items = "".join(f"<li>{it}</li>" for it in stage["items"])
        lead = f'<p class="rlead">{stage["lead"]}</p>' if stage.get("lead") else ""
        note = f'<p class="rnote">{stage["note"]}</p>' if stage.get("note") else ""
        out.append(f'''
        <div class="stage reveal">
          <div class="stage-mark">{i:02d}</div>
          <h3>{stage["name"]}</h3>
          {lead}
          <ul class="rlist">{items}</ul>
          {note}
          <p class="result"><span>Result</span>{stage["result"]}</p>
        </div>''')
    return "".join(out)

def branch_leaves():
    out = []
    for ed in C.ONE_MESSAGE_EDITIONS:
        out.append(f'<div class="leaf reveal">{ed}</div>')
    return "".join(out)

def edition_entries():
    out = []
    for name, desc, sub in C.EDITIONS:
        sub_html = ""
        if sub:
            sub_html = '<ul class="sub-list">' + "".join(f"<li>{s}</li>" for s in sub) + "</ul>"
        out.append(f'''
        <div class="edition reveal">
          <h4>{name}</h4>
          <p>{desc}</p>
          {sub_html}
        </div>''')
    return "".join(out)

def experience_rungs():
    out = []
    for exp in C.EXPERIENCES:
        fits = "".join(f"<li>{f}</li>" for f in exp["fits"])
        flow_html = ""
        if exp.get("flow"):
            flow_html = '<div class="flow">' + "".join(f'<span>{s}</span>' for s in exp["flow"]) + '</div>'
        flow_note = f'<p class="flow-note">{exp["flow_note"]}</p>' if exp.get("flow_note") else ""
        out.append(f'''
        <div class="rung reveal">
          <div class="rung-length">{exp["length"]}</div>
          <div class="rung-body">
            <h3>{exp["name"]}</h3>
            <p class="tag">{exp["tag"]}</p>
            <ul class="fits">{fits}</ul>
            {flow_html}
            {flow_note}
          </div>
        </div>''')
    return "".join(out)

def product_entries():
    out = []
    for name, desc, items in C.PRODUCTS:
        items_html = '<ul class="sub-list">' + "".join(f"<li>{i}</li>" for i in items) + "</ul>" if items else ""
        out.append(f'''
        <div class="product reveal">
          <h4>{name}</h4>
          <p>{desc}</p>
          {items_html}
        </div>''')
    return "".join(out)

def customization_entries():
    out = []
    for i, (name, desc, items) in enumerate(C.CUSTOMIZATION, start=1):
        items_html = '<ul class="sub-list">' + "".join(f"<li>{it}</li>" for it in items) + "</ul>" if items else ""
        out.append(f'''
        <div class="tier reveal">
          <div class="tier-num">{i:02d}</div>
          <div class="tier-body">
            <h4>{name}</h4>
            <p>{desc}</p>
            {items_html}
          </div>
        </div>''')
    return "".join(out)

def pod_items():
    return "".join(f"<li>{i}</li>" for i in C.POD["items"])

def finder_facets():
    return "".join(f'<span class="facet">{f}</span>' for f in C.FINDER["facets"])

def difference_pairs():
    out = []
    for a, b in C.DIFFERENCE_PAIRS:
        out.append(f'<div class="pair reveal"><span class="from">{a}</span><span class="arrow">\u2192</span><span class="to">{b}</span></div>')
    return "".join(out)

def imagine_lines():
    out = []
    for line in C.IMAGINE_CHAIN:
        out.append(f'<p class="imagine-line reveal">{line}</p>')
    return "".join(out)
