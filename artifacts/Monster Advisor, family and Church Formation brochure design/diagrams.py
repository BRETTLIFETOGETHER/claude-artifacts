import math

GOLD = "#B98D3E"
GOLD_BRIGHT = "#D9B876"
NAVY = "#101E38"
NAVY2 = "#1B2C4F"
GRAY = "#8891A0"
LINE = "#DCD4C0"
CREAM = "#F1EBDD"
INK = "#1C2230"

# ---------------------------------------------------------------
# 1. BEFORE / AFTER CHAIN — page 4
# ---------------------------------------------------------------
def chain_diagram():
    labels = ["WEEKEND", "GROUPS", "DAILY", "FAMILY", "MISSION"]
    w, h = 860, 430
    n = len(labels)
    y_before = 92
    y_after = 330
    margin = 90
    span = w - 2 * margin
    xs = [margin + span * i / (n - 1) for i in range(n)]

    svg = [f'<svg viewBox="0 0 {w} {h}" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">']

    # BEFORE row — scattered, disconnected, slightly offset vertically, gray, no connectors
    offsets = [10, -14, 6, -10, 12]
    svg.append(f'<text x="0" y="{y_before-52}" font-family="Archivo" font-weight="600" font-size="13" letter-spacing="2.4" fill="{GRAY}">BEFORE — DISCONNECTED EFFORT</text>')
    for i, (x, lab) in enumerate(zip(xs, labels)):
        yy = y_before + offsets[i]
        svg.append(f'<circle cx="{x}" cy="{yy}" r="30" fill="none" stroke="{GRAY}" stroke-width="1.6" stroke-dasharray="3,5" />')
        svg.append(f'<text x="{x}" y="{yy+5}" text-anchor="middle" font-family="Archivo" font-weight="600" font-size="10.5" letter-spacing="0.5" fill="{GRAY}">{lab[:1]}</text>')
        svg.append(f'<text x="{x}" y="{yy+52}" text-anchor="middle" font-family="Archivo" font-weight="600" font-size="11.5" letter-spacing="1.6" fill="{INK}" opacity="0.55">{lab}</text>')

    # divider
    svg.append(f'<line x1="0" y1="{(y_before+y_after)//2 + 8}" x2="{w}" y2="{(y_before+y_after)//2+8}" stroke="{LINE}" stroke-width="1"/>')

    # AFTER row — connected by continuous gold thread
    svg.append(f'<text x="0" y="{y_after-52}" font-family="Archivo" font-weight="600" font-size="13" letter-spacing="2.4" fill="{GOLD}">AFTER — ONE CONNECTED SYSTEM</text>')
    path_pts = " ".join([f"{x},{y_after}" for x in xs])
    svg.append(f'<polyline points="{path_pts}" fill="none" stroke="{GOLD}" stroke-width="2.5" />')
    for i, (x, lab) in enumerate(zip(xs, labels)):
        svg.append(f'<circle cx="{x}" cy="{y_after}" r="32" fill="{NAVY}" />')
        svg.append(f'<circle cx="{x}" cy="{y_after}" r="32" fill="none" stroke="{GOLD}" stroke-width="1.6" />')
        svg.append(f'<text x="{x}" y="{y_after+5}" text-anchor="middle" font-family="Playfair" font-weight="700" font-size="13" fill="{GOLD_BRIGHT}">{i+1}</text>')
        svg.append(f'<text x="{x}" y="{y_after+56}" text-anchor="middle" font-family="Archivo" font-weight="700" font-size="12" letter-spacing="1.6" fill="{NAVY}">{lab}</text>')

    svg.append('</svg>')
    return "".join(svg)


# ---------------------------------------------------------------
# 7. GENERIC CONNECTED STEP CHAIN (labels + captions) — reusable
# ---------------------------------------------------------------
def step_chain_diagram(steps):
    """steps: list of (label, caption) tuples"""
    n = len(steps)
    w, h = 960, 360
    margin = 90
    span = w - 2*margin
    xs = [margin + span*i/(n-1) for i in range(n)] if n > 1 else [w/2]
    y = 90
    svg = [f'<svg viewBox="0 0 {w} {h}" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">']
    path_pts = " ".join([f"{x},{y}" for x in xs])
    svg.append(f'<polyline points="{path_pts}" fill="none" stroke="{GOLD}" stroke-width="2.5"/>')
    for i in range(n-1):
        mx = (xs[i]+xs[i+1])/2
        svg.append(f'<polygon points="{mx-6:.1f},{y-6} {mx+7:.1f},{y} {mx-6:.1f},{y+6}" fill="{GOLD}"/>')
    for i, (x, (label, caption)) in enumerate(zip(xs, steps)):
        svg.append(f'<circle cx="{x}" cy="{y}" r="40" fill="{NAVY}" stroke="{GOLD}" stroke-width="1.8"/>')
        svg.append(f'<text x="{x}" y="{y+5}" text-anchor="middle" font-family="Playfair" font-weight="700" font-size="12.5" fill="{GOLD_BRIGHT}">{label}</text>')
        # wrap caption into lines of ~18 chars
        words = caption.split()
        lines, cur = [], ""
        for wd in words:
            trial = (cur + " " + wd).strip()
            if len(trial) > 20 and cur:
                lines.append(cur); cur = wd
            else:
                cur = trial
        if cur: lines.append(cur)
        ty = y + 66
        for ln in lines:
            svg.append(f'<text x="{x}" y="{ty}" text-anchor="middle" font-family="Inter" font-weight="400" font-size="10" fill="{INK}">{ln}</text>')
            ty += 15
    svg.append('</svg>')
    return "".join(svg)


# ---------------------------------------------------------------
# 8. GENERIC STAIRCASE (level label, title, caption) — reusable
# ---------------------------------------------------------------
def generic_staircase(levels):
    """levels: list of (num, title, caption) tuples, ascending"""
    n = len(levels)
    w, h = 960, 500
    step_w = w / n
    step_h_unit = 64
    base_y = 460
    svg = [f'<svg viewBox="0 0 {w} {h}" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">']
    svg.append(f'<line x1="0" y1="{base_y}" x2="{w}" y2="{base_y}" stroke="{LINE}" stroke-width="1"/>')
    for i, (num, title, caption) in enumerate(levels):
        step_top = base_y - (i+1)*step_h_unit
        x = 20 + i*step_w
        bw = step_w - 22
        svg.append(f'<rect x="{x:.1f}" y="{step_top}" width="{bw:.1f}" height="{base_y-step_top}" fill="{NAVY}" opacity="{0.5 + i*0.12:.2f}"/>')
        svg.append(f'<rect x="{x:.1f}" y="{step_top}" width="{bw:.1f}" height="3" fill="{GOLD}"/>')
        cx = x + bw/2
        svg.append(f'<text x="{cx:.1f}" y="{step_top-46}" text-anchor="middle" font-family="Archivo" font-weight="700" font-size="10.5" letter-spacing="1.8" fill="{GOLD}">LEVEL {num}</text>')
        # wrap title
        svg.append(f'<text x="{cx:.1f}" y="{step_top-25}" text-anchor="middle" font-family="Playfair" font-weight="700" font-size="13.5" fill="{INK}">{title}</text>')
        words = caption.split()
        lines, cur = [], ""
        for wd in words:
            trial = (cur + " " + wd).strip()
            if len(trial) > 22 and cur:
                lines.append(cur); cur = wd
            else:
                cur = trial
        if cur: lines.append(cur)
        dy = step_top - 25 - 16 - (len(lines)-1)*13
        for ln in lines:
            svg.append(f'<text x="{cx:.1f}" y="{dy:.1f}" text-anchor="middle" font-family="Inter" font-weight="400" font-size="9.3" fill="{GRAY}">{ln}</text>')
            dy += 13
    svg.append('</svg>')
    return "".join(svg)


# ---------------------------------------------------------------
# 2. RADIAL ECOSYSTEM DIAGRAM — page 6
# ---------------------------------------------------------------
def ecosystem_diagram():
    items = [
        "Small Group\nCurriculum", "Daily\nDevotionals", "Family\nConversations",
        "Leadership\nDevelopment", "Ministry\nTraining", "Podcasts",
        "Video\nStudies", "Published\nBooks", "Future\nCampaigns",
    ]
    w, h = 900, 620
    cx, cy = w/2, h/2 + 6
    R = 235
    r_node = 74
    n = len(items)
    svg = [f'<svg viewBox="0 0 {w} {h}" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">']

    # spokes first (so nodes sit on top)
    coords = []
    for i in range(n):
        angle = -math.pi/2 + 2*math.pi*i/n
        x = cx + R*math.cos(angle)
        y = cy + R*math.sin(angle)
        coords.append((x, y, angle))
        svg.append(f'<line x1="{cx:.1f}" y1="{cy:.1f}" x2="{x:.1f}" y2="{y:.1f}" stroke="{GOLD}" stroke-width="1.3" opacity="0.55"/>')

    # outer thin ring
    svg.append(f'<circle cx="{cx}" cy="{cy}" r="{R}" fill="none" stroke="{LINE}" stroke-width="1"/>')

    # center node
    svg.append(f'<circle cx="{cx}" cy="{cy}" r="86" fill="{NAVY}" />')
    svg.append(f'<circle cx="{cx}" cy="{cy}" r="86" fill="none" stroke="{GOLD}" stroke-width="2"/>')
    svg.append(f'<text x="{cx}" y="{cy-8}" text-anchor="middle" font-family="Archivo" font-weight="600" font-size="10.5" letter-spacing="2" fill="{GOLD_BRIGHT}">SUNDAY\'S</text>')
    svg.append(f'<text x="{cx}" y="{cy+16}" text-anchor="middle" font-family="Playfair" font-weight="700" font-size="21" fill="#FBF8F1">Message</text>')

    # outer nodes
    for (x, y, angle), label in zip(coords, items):
        lines = label.split("\n")
        svg.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="50" fill="#FBF8F1" stroke="{GOLD}" stroke-width="1.4"/>')
        ty = y - (len(lines)-1)*7
        for ln in lines:
            svg.append(f'<text x="{x:.1f}" y="{ty:.1f}" text-anchor="middle" font-family="Archivo" font-weight="600" font-size="10.3" letter-spacing="0.3" fill="{NAVY}">{ln}</text>')
            ty += 14

    svg.append('</svg>')
    return "".join(svg)


# ---------------------------------------------------------------
# 3. FORMATION WHEEL — page 8
# ---------------------------------------------------------------
def wheel_diagram():
    segs = [
        ("Weekend", "The message is preached\nwith clarity and conviction."),
        ("Groups", "The message is discussed\nin circles of real relationship."),
        ("Daily", "The message becomes a\ndaily rhythm of reflection."),
        ("Family", "The message shapes\nconversation around the table."),
        ("Mission", "The message moves\noutward into action."),
    ]
    w, h = 900, 620
    cx, cy = w/2, h/2 + 10
    R_outer = 260
    R_inner = 140
    n = len(segs)
    svg = [f'<svg viewBox="0 0 {w} {h}" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">']

    def polar(r, deg):
        rad = math.radians(deg - 90)
        return cx + r*math.cos(rad), cy + r*math.sin(rad)

    seg_angle = 360/n
    # wedge dividers
    for i in range(n):
        deg = i*seg_angle
        x1, y1 = polar(R_inner, deg)
        x2, y2 = polar(R_outer+18, deg)
        svg.append(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{LINE}" stroke-width="1"/>')

    svg.append(f'<circle cx="{cx}" cy="{cy}" r="{R_outer}" fill="none" stroke="{GOLD}" stroke-width="1.4" opacity="0.5"/>')
    svg.append(f'<circle cx="{cx}" cy="{cy}" r="{R_inner}" fill="none" stroke="{GOLD}" stroke-width="1.4" opacity="0.6"/>')

    # rotating arrow ticks along outer ring to suggest continuous motion
    for i in range(n):
        deg = i*seg_angle + seg_angle/2
        x, y = polar(R_outer+18, deg)
        svg.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="3.2" fill="{GOLD}"/>')

    # center hub
    svg.append(f'<circle cx="{cx}" cy="{cy}" r="{R_inner-18}" fill="{NAVY}"/>')
    svg.append(f'<text x="{cx}" y="{cy-6}" text-anchor="middle" font-family="Archivo" font-weight="600" font-size="10" letter-spacing="2.4" fill="{GOLD_BRIGHT}">ONE</text>')
    svg.append(f'<text x="{cx}" y="{cy+16}" text-anchor="middle" font-family="Playfair" font-weight="700" font-size="17" fill="#FBF8F1">Formation</text>')
    svg.append(f'<text x="{cx}" y="{cy+34}" text-anchor="middle" font-family="Playfair" font-weight="700" font-size="17" fill="#FBF8F1">Path</text>')

    # labels at mid-radius between inner and outer
    R_label = (R_inner + R_outer)/2 + 8
    for i, (name, desc) in enumerate(segs):
        deg = i*seg_angle + seg_angle/2
        x, y = polar(R_label, deg)
        svg.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="4" fill="{GOLD}"/>')
        # place name label further out, radially oriented but kept horizontal for legibility
        lx, ly = polar(R_outer + 46, deg)
        anchor = "middle"
        svg.append(f'<text x="{lx:.1f}" y="{ly:.1f}" text-anchor="{anchor}" font-family="Playfair" font-weight="700" font-size="15" fill="{NAVY}">{name}</text>')

    svg.append('</svg>')
    return "".join(svg)


# ---------------------------------------------------------------
# 4. STAIRCASE — Crawl / Walk / Run / Multiply — page 12
# ---------------------------------------------------------------
def staircase_diagram():
    levels = [
        ("01", "Use Ours", "Launch proven Lifetogether\ncampaigns as they are."),
        ("02", "Customize Ours", "Adapt content and language\nto your church's voice."),
        ("03", "Build Yours", "Create original campaigns from\nyour pastor's own messages."),
        ("04", "Publish Yours", "Package your campaigns for\nother churches to license."),
        ("05", "Multiply Yours", "Train other pastors to build\nwithin your formation system."),
    ]
    w, h = 900, 520
    n = len(levels)
    step_w = 150
    step_h_unit = 62
    base_y = 470
    left_pad = 30
    svg = [f'<svg viewBox="0 0 {w} {h}" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">']

    # baseline
    svg.append(f'<line x1="0" y1="{base_y}" x2="{w}" y2="{base_y}" stroke="{LINE}" stroke-width="1"/>')

    for i, (num, title, desc) in enumerate(levels):
        step_top = base_y - (i+1)*step_h_unit
        x = left_pad + i*step_w
        # riser + tread as a solid navy block
        svg.append(f'<rect x="{x}" y="{step_top}" width="{step_w-14}" height="{base_y-step_top}" fill="{NAVY}" opacity="{0.55 + i*0.11:.2f}"/>')
        svg.append(f'<rect x="{x}" y="{step_top}" width="{step_w-14}" height="3" fill="{GOLD}"/>')
        # number + title above the step tread
        svg.append(f'<text x="{x+ (step_w-14)/2:.1f}" y="{step_top-42}" text-anchor="middle" font-family="Archivo" font-weight="700" font-size="11" letter-spacing="2" fill="{GOLD}">LEVEL {num}</text>')
        svg.append(f'<text x="{x+ (step_w-14)/2:.1f}" y="{step_top-20}" text-anchor="middle" font-family="Playfair" font-weight="700" font-size="16.5" fill="{INK}">{title}</text>')
        # description lines beneath the step number, wrapped manually
        desc_lines = desc.split("\n")
        ty = step_top - 2 + 14
        # place description centered on the step face, white-ish text if step tall enough (only for last two)
        # Instead place descriptions above title area in smaller muted text stacked
        dy = step_top - 62
        for ln in desc_lines:
            svg.append(f'<text x="{x+(step_w-14)/2:.1f}" y="{dy:.1f}" text-anchor="middle" font-family="Inter" font-weight="400" font-size="9.6" fill="{GRAY}">{ln}</text>')
            dy -= 13

    svg.append('</svg>')
    return "".join(svg)


# ---------------------------------------------------------------
# 5. MESSAGE -> CURRICULUM -> COMMUNITY -> MOVEMENT — page 15
# ---------------------------------------------------------------
def message_movement_diagram():
    nodes = ["Message", "Curriculum", "Community", "Movement"]
    w, h = 900, 300
    n = len(nodes)
    margin = 120
    span = w - 2*margin
    xs = [margin + span*i/(n-1) for i in range(n)]
    y = 150
    svg = [f'<svg viewBox="0 0 {w} {h}" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">']

    path_pts = " ".join([f"{x},{y}" for x in xs])
    svg.append(f'<polyline points="{path_pts}" fill="none" stroke="{GOLD}" stroke-width="2.5"/>')

    # arrowheads between nodes
    for i in range(n-1):
        mx = (xs[i]+xs[i+1])/2
        svg.append(f'<polygon points="{mx-6:.1f},{y-6} {mx+7:.1f},{y} {mx-6:.1f},{y+6}" fill="{GOLD}"/>')

    for i, (x, label) in enumerate(zip(xs, nodes)):
        r = 54 if i in (0, n-1) else 46
        fill = NAVY if i in (0, n-1) else "#FBF8F1"
        stroke = GOLD
        txt_fill = GOLD_BRIGHT if i in (0, n-1) else NAVY
        svg.append(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{fill}" stroke="{stroke}" stroke-width="1.6"/>')
        svg.append(f'<text x="{x}" y="{y+6}" text-anchor="middle" font-family="Playfair" font-weight="700" font-size="15.5" fill="{txt_fill}">{label}</text>')
        svg.append(f'<text x="{x}" y="{y+r+26}" text-anchor="middle" font-family="Archivo" font-weight="600" font-size="10" letter-spacing="2" fill="{GRAY}">STAGE {i+1}</text>')

    svg.append('</svg>')
    return "".join(svg)


# ---------------------------------------------------------------
# 6. SIMPLE FORMATION TIMELINE — page 13 (18-24 month roadmap)
# ---------------------------------------------------------------
def timeline_diagram():
    stops = [
        ("Months 1–3", "Launch your first\ncampaign with our library"),
        ("Months 4–9", "Customize campaigns to\nyour church's voice"),
        ("Months 10–15", "Build original campaigns\nfrom your own messages"),
        ("Months 16–20", "Publish your campaigns\nfor other churches"),
        ("Months 21–24", "Train other pastors inside\nyour formation system"),
    ]
    w, h = 900, 210
    n = len(stops)
    margin = 60
    span = w - 2*margin
    xs = [margin + span*i/(n-1) for i in range(n)]
    y = 58
    svg = [f'<svg viewBox="0 0 {w} {h}" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">']
    svg.append(f'<line x1="{xs[0]}" y1="{y}" x2="{xs[-1]}" y2="{y}" stroke="{GOLD}" stroke-width="2"/>')
    for x, (period, desc) in zip(xs, stops):
        svg.append(f'<circle cx="{x}" cy="{y}" r="6" fill="{NAVY}" stroke="{GOLD}" stroke-width="1.6"/>')
        svg.append(f'<text x="{x}" y="{y-18}" text-anchor="middle" font-family="Archivo" font-weight="700" font-size="10.5" letter-spacing="1.2" fill="{GOLD}">{period}</text>')
        dy = y + 26
        for ln in desc.split("\n"):
            svg.append(f'<text x="{x}" y="{dy}" text-anchor="middle" font-family="Inter" font-weight="400" font-size="9.8" fill="{INK}">{ln}</text>')
            dy += 14
    svg.append('</svg>')
    return "".join(svg)
