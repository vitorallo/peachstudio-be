#!/usr/bin/env python3
"""
PEACH STUDIO — logo generator.

Builds every logo asset from one source of truth so the brand mark and the
pixel wordmark always stay in sync. The wordmark is emitted as plain <rect>
pixels (no font dependency), so the logo renders identically anywhere — web,
slides, print, a t-shirt — without Silkscreen installed.

Run:  python3 build-logo.py
Out:  logo/*.svg
"""

import os

OUT = os.path.join(os.path.dirname(__file__), "logo")

# — Brand colors (mirror tokens.css) —
CLAY = "#C2603A"   # peach body
LEAF = "#5E7C2F"   # leaf
INK  = "#211D18"   # primary text / mono mark
SOFT = "#57514A"   # secondary text ("STUDIO")
CREAM = "#F3F0E9"  # reversed mark on dark

# ── The peach mark, on a 20px pixel grid (viewBox 0..240 x 0..220) ──
# Returns the inner <g> markup given a peach color and leaf color.
def mark_paths(peach, leaf):
    leaf_px = [(140, 0, 60, 20), (100, 20, 80, 20)]
    peach_px = [
        (60, 40, 40, 20), (120, 40, 40, 20),
        (40, 60, 60, 20), (120, 60, 60, 20),
        (20, 80, 180, 100),
        (40, 180, 140, 20),
        (60, 200, 100, 20),
    ]
    leaf_r = "".join(f'<rect x="{x}" y="{y}" width="{w}" height="{h}"/>' for x, y, w, h in leaf_px)
    peach_r = "".join(f'<rect x="{x}" y="{y}" width="{w}" height="{h}"/>' for x, y, w, h in peach_px)
    return (f'<g fill="{leaf}">{leaf_r}</g>'
            f'<g fill="{peach}">{peach_r}</g>')

MARK_W, MARK_H = 240, 220   # with the built-in translate(10,0) padding below

# ── 5×7 pixel alphabet for the wordmark ──
GLYPHS = {
    "P": ["11110", "10001", "10001", "11110", "10000", "10000", "10000"],
    "E": ["11111", "10000", "10000", "11110", "10000", "10000", "11111"],
    "A": ["01110", "10001", "10001", "11111", "10001", "10001", "10001"],
    "C": ["01111", "10000", "10000", "10000", "10000", "10000", "01111"],
    "H": ["10001", "10001", "10001", "11111", "10001", "10001", "10001"],
    "S": ["01111", "10000", "10000", "01110", "00001", "00001", "11110"],
    "T": ["11111", "00100", "00100", "00100", "00100", "00100", "00100"],
    "U": ["10001", "10001", "10001", "10001", "10001", "10001", "01110"],
    "D": ["11110", "10001", "10001", "10001", "10001", "10001", "11110"],
    "I": ["11111", "00100", "00100", "00100", "00100", "00100", "11111"],
    "O": ["01110", "10001", "10001", "10001", "10001", "10001", "01110"],
    " ": ["00000"] * 7,
}

GLYPH_W, GLYPH_H = 5, 7   # in cells
LETTER_GAP = 1            # cells between letters
SPACE_W = 3               # cells for a space


def word_pixels(text, px):
    """Yield (x, y, w, h) rects for `text` rendered at `px` per cell.
    Returns (rects, total_width_in_px)."""
    rects = []
    cx = 0  # cursor in cells
    for ch in text:
        if ch == " ":
            cx += SPACE_W + LETTER_GAP
            continue
        rows = GLYPHS[ch]
        for r, row in enumerate(rows):
            for c, bit in enumerate(row):
                if bit == "1":
                    rects.append(((cx + c) * px, r * px, px, px))
        cx += GLYPH_W + LETTER_GAP
    width = (cx - LETTER_GAP) * px
    return rects, width


def wordmark_group(px, x0=0, y0=0, peach_fill=INK, studio_fill=SOFT):
    """Build the two-tone 'PEACH STUDIO' wordmark group + its pixel size.
    peach_fill/studio_fill let callers flip to reversed (cream) colors."""
    peach_rects, peach_w = word_pixels("PEACH", px)
    # start STUDIO after PEACH + one space
    studio_offset = peach_w + (SPACE_W + LETTER_GAP) * px
    studio_rects, studio_w = word_pixels("STUDIO", px)
    total_w = studio_offset + studio_w
    total_h = GLYPH_H * px

    p = "".join(f'<rect x="{x0+x}" y="{y0+y}" width="{w}" height="{h}"/>' for x, y, w, h in peach_rects)
    s = "".join(f'<rect x="{x0+studio_offset+x}" y="{y0+y}" width="{w}" height="{h}"/>' for x, y, w, h in studio_rects)
    g = f'<g fill="{peach_fill}">{p}</g><g fill="{studio_fill}">{s}</g>'
    return g, total_w, total_h


def svg(width, height, body, extra=""):
    return (f'<?xml version="1.0" encoding="UTF-8"?>\n'
            f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" '
            f'viewBox="0 0 {width} {height}" shape-rendering="crispEdges"{extra}>\n{body}\n</svg>\n')


def write(name, content):
    path = os.path.join(OUT, name)
    with open(path, "w") as f:
        f.write(content)
    print("wrote", os.path.relpath(path))


def main():
    os.makedirs(OUT, exist_ok=True)

    # 1) Color mark (peach + leaf), transparent background
    body = f'<g transform="translate(10,0)">{mark_paths(CLAY, LEAF)}</g>'
    write("peach-mark.svg", svg(MARK_W, MARK_H, body))

    # 2) Monochrome ink mark (one-color, for stamps / dark-on-light)
    body = f'<g transform="translate(10,0)">{mark_paths(INK, INK)}</g>'
    write("peach-mark-ink.svg", svg(MARK_W, MARK_H, body))

    # 3) Reversed mark (cream, for dark backgrounds)
    body = f'<g transform="translate(10,0)">{mark_paths(CREAM, CREAM)}</g>'
    write("peach-mark-cream.svg", svg(MARK_W, MARK_H, body))

    # 4) Favicon — color mark, square, padded
    body = f'<g transform="translate(10,10)">{mark_paths(CLAY, LEAF)}</g>'
    write("favicon.svg", svg(240, 240, body))

    # 5) Wordmark only (two-tone pixel PEACH STUDIO)
    PX = 8
    g, w, h = wordmark_group(PX)
    write("wordmark.svg", svg(w, h, g))

    # 6) Horizontal lockup — mark + wordmark, vertically centered
    def horizontal(peach_fill, studio_fill):
        PX = 8
        gap = 28
        mark_h = 160                  # render height of mark in the lockup
        scale = mark_h / MARK_H
        mark_w = MARK_W * scale
        wg, ww, wh = wordmark_group(PX, peach_fill=peach_fill, studio_fill=studio_fill)
        total_w = mark_w + gap + ww
        total_h = mark_h
        mark_g = (f'<g transform="translate(0,0) scale({scale:.4f})">'
                  f'<g transform="translate(10,0)">{mark_paths(CLAY, LEAF)}</g></g>')
        word_y = (total_h - wh) / 2
        word_g = f'<g transform="translate({mark_w + gap:.2f},{word_y:.2f})">{wg}</g>'
        return svg(round(total_w), round(total_h), mark_g + word_g)

    write("lockup-horizontal.svg", horizontal(INK, SOFT))
    # Reversed: cream wordmark for dark backgrounds (mark keeps its color)
    write("lockup-horizontal-reversed.svg", horizontal(CREAM, CREAM))

    # 7) Stacked lockup — mark centered above wordmark
    def stacked(peach_fill, studio_fill):
        PX = 7
        mark_h = 150
        scale = mark_h / MARK_H
        mark_w = MARK_W * scale
        wg, ww, wh = wordmark_group(PX, peach_fill=peach_fill, studio_fill=studio_fill)
        pad_between = 26
        total_w = max(mark_w, ww)
        total_h = mark_h + pad_between + wh
        mark_x = (total_w - mark_w) / 2
        mark_g = (f'<g transform="translate({mark_x:.2f},0) scale({scale:.4f})">'
                  f'<g transform="translate(10,0)">{mark_paths(CLAY, LEAF)}</g></g>')
        word_x = (total_w - ww) / 2
        word_g = f'<g transform="translate({word_x:.2f},{mark_h + pad_between})">{wg}</g>'
        return svg(round(total_w), round(total_h), mark_g + word_g)

    write("lockup-stacked.svg", stacked(INK, SOFT))
    write("lockup-stacked-reversed.svg", stacked(CREAM, CREAM))

    print("done.")


if __name__ == "__main__":
    main()
