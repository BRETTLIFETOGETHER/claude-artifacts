# -*- coding: utf-8 -*-
"""Shared visual system + the Legacy Wheel graphic."""
import math
from fli_data import DIMENSIONS, TM

BASE = """
@page { size: Letter; margin: 0; }
* { box-sizing: border-box; }
body { margin: 0; font-family: 'Poppins'; font-weight: 300; color: #2B3440;
       font-size: 9pt; line-height: 1.42; }
.page { page-break-after: always; height: 11in; position: relative; overflow: hidden;
        background: #FFFFFF; }
.page.last { page-break-after: auto; }
.pad { padding: 0 0.72in; }
h1, h2, h3, .serif { font-family: 'Lora'; }

.trk { font-family: 'Poppins'; font-weight: 600; font-size: 6.6pt; letter-spacing: .24em;
       text-transform: uppercase; }
.foot { position: absolute; bottom: 0.34in; left: 0.72in; right: 0.72in;
        display: flex; justify-content: space-between; align-items: center;
        border-top: .6pt solid #E3E8ED; padding-top: 5pt;
        font-size: 6.2pt; letter-spacing: .13em; text-transform: uppercase; color: #9AA5B1; }

/* running head on interior pages */
.rhead { display: flex; justify-content: space-between; align-items: center;
         padding: 9pt 0.72in; color: #fff; }
.rhead .a { font-weight: 600; font-size: 7.2pt; letter-spacing: .2em; text-transform: uppercase; }
.rhead .b { font-family: 'Lora'; font-style: italic; font-size: 8.4pt; color: rgba(255,255,255,.82); }

/* section heads */
.shead { margin-top: 20pt; }
.shead .k { font-family: 'Poppins'; font-weight: 600; font-size: 6.6pt; letter-spacing: .24em;
            text-transform: uppercase; }
.shead h2 { font-weight: 600; font-size: 19pt; line-height: 1.1; margin: 5pt 0 0;
            color: #16233A; letter-spacing: -.014em; }
.shead .d { font-family: 'Lora'; font-style: italic; font-size: 9.6pt; color: #5A6675;
            margin-top: 5pt; max-width: 5.3in; line-height: 1.42; }
.hr { border-top: .6pt solid #E3E8ED; margin: 13pt 0; }
"""

# ------------------------------------------------------------------ the wheel
def wheel_svg(example=False, scores=None, size=(560, 430), r=124, label_pt=8.4,
              blank_note=True):
    """Hexagonal radar chart of the six legacy dimensions."""
    W, H = size
    cx, cy = W / 2.0, H / 2.0 - 6
    angles = [-90, -30, 30, 90, 150, 210]
    rings = [4, 8, 12, 16, 20]

    def pt(ang, rad):
        a = math.radians(ang)
        return (cx + rad * math.cos(a), cy + rad * math.sin(a))

    out = ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" width="100%%">' % (W, H)]

    # concentric rings
    for i, ring in enumerate(rings):
        rad = r * ring / 20.0
        pts = " ".join("%.2f,%.2f" % pt(a, rad) for a in angles)
        last = (i == len(rings) - 1)
        out.append('<polygon points="%s" fill="%s" stroke="%s" stroke-width="%s"/>' % (
            pts, "#FBFCFD" if last else "none", "#16233A" if last else "#DCE3EA",
            "1.1" if last else ".7"))

    # spokes
    for a in angles:
        x, y = pt(a, r)
        out.append('<line x1="%.2f" y1="%.2f" x2="%.2f" y2="%.2f" stroke="#DCE3EA" '
                   'stroke-width=".7"/>' % (cx, cy, x, y))

    # ring value labels along the upper-right spoke
    for ring in rings:
        rad = r * ring / 20.0
        x, y = pt(-30, rad)
        out.append('<text x="%.2f" y="%.2f" font-family="Poppins" font-size="6.2" '
                   'fill="#A9B4C0" text-anchor="middle">%d</text>' % (x + 7, y - 3, ring))

    # example plot
    if example or scores:
        sc = scores or [16, 13, 11, 9, 15, 7]
        pts = " ".join("%.2f,%.2f" % pt(a, r * s / 20.0) for a, s in zip(angles, sc))
        out.append('<polygon points="%s" fill="#16233A" fill-opacity=".08" stroke="#16233A" '
                   'stroke-width="1.4" stroke-dasharray="4 2.5"/>' % pts)
        for a, s, d in zip(angles, sc, DIMENSIONS):
            x, y = pt(a, r * s / 20.0)
            out.append('<circle cx="%.2f" cy="%.2f" r="3.6" fill="%s"/>' % (x, y, d["color"]))

    # vertex markers + labels
    for a, d in zip(angles, DIMENSIONS):
        x, y = pt(a, r)
        out.append('<circle cx="%.2f" cy="%.2f" r="4.6" fill="%s"/>' % (x, y, d["color"]))
        out.append('<circle cx="%.2f" cy="%.2f" r="4.6" fill="none" stroke="#fff" '
                   'stroke-width="1.3"/>' % (x, y))
        lx, ly = pt(a, r + 20)
        if a == -90:
            anchor, dy = "middle", -14
        elif a == 90:
            anchor, dy = "middle", 12
        elif a in (-30, 30):
            anchor, dy = "start", (-2 if a == -30 else 6)
        else:
            anchor, dy = "end", (-2 if a == 210 else 6)
        l1, l2 = d["wheel"]
        out.append('<text x="%.2f" y="%.2f" font-family="Poppins" font-size="6" '
                   'letter-spacing="1.3" fill="%s" text-anchor="%s">%02d</text>' % (
                       lx, ly + dy - 9, anchor, d["color"], d["n"]))
        out.append('<text x="%.2f" y="%.2f" font-family="Poppins" font-size="%s" '
                   'font-weight="500" fill="#2B3440" text-anchor="%s">%s</text>' % (
                       lx, ly + dy, label_pt, anchor, l1))
        out.append('<text x="%.2f" y="%.2f" font-family="Poppins" font-size="%s" '
                   'font-weight="500" fill="#2B3440" text-anchor="%s">%s</text>' % (
                       lx, ly + dy + label_pt + 1.6, label_pt, anchor, l2))

    if blank_note:
        out.append('<text x="%.2f" y="%.2f" font-family="Poppins" font-size="6.4" '
                   'fill="#B4BEC9" text-anchor="middle">%s</text>' % (
                       cx, H - 4, "Plot each section score, then connect the points"))
    out.append('</svg>')
    return "".join(out)


def chips_html():
    return "".join('<div style="background:{}"></div>'.format(d["color"]) for d in DIMENSIONS)


def foot(page, total, right=None):
    return ('<div class="foot"><span>Family Legacy Intelligence{tm}</span>'
            '<span>{r}</span><span>Page {p} of {t}</span></div>').format(
        tm=TM, p=page, t=total, r=right or "")


def rhead(color, left, right):
    return ('<div class="rhead" style="background:{c}"><div class="a">{l}</div>'
            '<div class="b">{r}</div></div>').format(c=color, l=left, r=right)


def lines(n, gap=19, color="#D8DFE6"):
    """Ruled writing space."""
    return "".join('<div style="height:{g}pt;border-bottom:.6pt solid {c}"></div>'.format(
        g=gap, c=color) for _ in range(n))
