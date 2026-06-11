# PEACH STUDIO — Brand & Design System

The single source of truth for the PEACH STUDIO identity. Use it for the
website, decks, social, email, print, swag — anything that carries the name.

Open **`styleguide.html`** in a browser for the visual version of everything below.

```
brand/
├── DESIGN-SYSTEM.md          ← you are here
├── styleguide.html           ← visual reference (open in a browser)
├── tokens.css                ← CSS custom properties — copy into any project
├── tokens.json               ← same tokens, machine-readable (Figma, scripts)
├── build-logo.py             ← regenerates every logo file from one source
└── logo/
    ├── peach-mark.svg                 color mark (peach + leaf)
    ├── peach-mark-ink.svg             one-color ink mark
    ├── peach-mark-cream.svg           reversed mark (for dark backgrounds)
    ├── favicon.svg                    square, padded — browser tabs / app icon
    ├── wordmark.svg                   "PEACH STUDIO" pixel wordmark only
    ├── lockup-horizontal.svg          mark + wordmark, side by side  ← default
    ├── lockup-horizontal-reversed.svg same, cream text for dark backgrounds
    ├── lockup-stacked.svg             mark above wordmark
    ├── lockup-stacked-reversed.svg    same, for dark backgrounds
    └── png/                           ready-to-drop raster exports (transparent)
```

---

## 1 · The logo

The mark is a **pixel-art peach with a leaf**, drawn on a strict 20px grid with
flat color and crisp (non-antialiased) edges. It echoes the blocky, 8-bit feel
of retro game sprites — a nod to the studio's "build real tools, have fun doing
it" character. The wordmark "PEACH STUDIO" is set in **Silkscreen**, a pixel
typeface, and is shipped as outlined pixels (plain SVG rectangles) so it renders
identically everywhere without the font installed.

### Anatomy
- **Mark** — peach body in clay `#C2603A`, leaf in `#5E7C2F`.
- **Wordmark** — "PEACH" in ink `#211D18` (bold), "STUDIO" in soft ink `#57514A`.
  The two-tone split keeps the studio name quiet and the brand name loud.

### Which file to use
| Context | File |
|---|---|
| Default, most places | `logo/lockup-horizontal.svg` |
| Narrow / square space (avatar, stamp) | `logo/lockup-stacked.svg` |
| Dark background | `*-reversed.svg` variants |
| Icon only (favicon, app icon, watermark) | `logo/peach-mark.svg` / `favicon.svg` |
| Single-color print / engraving / embroidery | `logo/peach-mark-ink.svg` |
| Raster for slides / social / email | `logo/png/*.png` (transparent) |

### Clear space & minimum size
- **Clear space:** keep at least the height of one peach "pixel" (1/11 of the
  mark's width) clear on all sides. When in doubt, more air.
- **Minimum size:** mark no smaller than **24px** tall on screen; full lockup no
  smaller than **120px** wide so the pixel letters stay legible.

### Don'ts
- Don't recolor the mark outside the palette (no gradients, no drop shadows on
  the mark itself, no outlines).
- Don't stretch, rotate, or skew — pixels must stay square.
- Don't re-typeset the wordmark in a non-pixel font, and don't anti-alias /
  blur it. Pixel edges are the whole point.
- Don't place the color mark on a busy photo — use a reversed lockup or a solid
  panel.

### Regenerating the logo
All logo files are generated from `build-logo.py` (the pixel grid and the 5×7
pixel alphabet live there). To change the mark or wordmark, edit that script and
run:

```bash
cd brand && python3 build-logo.py
```

PNG exports are re-rendered from the SVGs through a headless browser (see the
note at the bottom of this file).

---

## 2 · Color

Warm clay on cream — the palette is intentionally low-contrast and analog, never
stark black-on-white.

### Core
| Token | Hex | Use |
|---|---|---|
| `cream` | `#F3F0E9` | page background |
| `cream-deep` | `#ECE7DC` | alternate section background |
| `surface` | `#FBFAF6` | cards, raised panels |
| `ink` | `#211D18` | primary text, mono logo mark |
| `ink-soft` | `#57514A` | secondary text |
| `ink-faint` | `#8A847B` | labels, captions, tertiary |
| `line` | `#DED7C9` | hairlines, borders |

### Clay accents
| Token | Hex | Use |
|---|---|---|
| `clay` | `#C2603A` | primary accent, peach body |
| `clay-deep` | `#A84E2C` | hover, italic serif emphasis |
| `clay-bright` | `#D9693E` | CTA button fill |
| `clay-tint` | `#EDDFD4` | soft tinted panels |
| `leaf` | `#5E7C2F` | logo leaf (and only the leaf) |

**Rules of thumb:** cream backgrounds, ink text, clay for one accent per view.
Clay is a spice, not a base — a single clay CTA or italic phrase carries more
weight than clay everywhere. Reserve `leaf` green for the logo.

---

## 3 · Typography

Three voices, each with one job:

- **Newsreader** (serif) — display headlines. Light weight (400–500), tight
  letter-spacing, italic in `clay-deep` for emphasis (e.g. *"…to life?"*).
- **Hanken Grotesk** (sans) — body copy, navigation, buttons. Friendly,
  legible, weights 400–700.
- **IBM Plex Mono** — eyebrows / kickers (uppercase, `0.22em` tracking),
  metadata, code.
- **Silkscreen** (pixel) — **logo wordmark only.** Don't use it for body text or
  headings; it belongs to the logo.

### Load (web)
```html
<link href="https://fonts.googleapis.com/css2?family=Newsreader:ital,opsz,wght@0,6..72,400;0,6..72,500;1,6..72,400;1,6..72,500&family=Hanken+Grotesk:wght@400;500;600;700&family=IBM+Plex+Mono:wght@400;500&family=Silkscreen:wght@400;700&display=swap" rel="stylesheet">
```

### Scale
Fluid `clamp()` sizes (min, preferred, max) live in `tokens.css` as
`--ps-display`, `--ps-h1`, `--ps-h2`, `--ps-h3`, `--ps-lead`, `--ps-body`,
`--ps-small`, `--ps-eyebrow`.

### The eyebrow pattern
The recurring kicker above section titles: mono, uppercase, `0.22em` tracking,
`clay-deep`, preceded by a short clay rule. Example: `— CREATIVE AI, DEV & SECURITY STUDIO`.

---

## 4 · Spacing, radius, elevation, motion

- **Spacing** scale: 8 / 16 / 24 / 48 / 72 / 120. Sections breathe with
  `--ps-section-y` (≈72–150px). Content max-width 1180px, fluid gutter.
- **Radius:** 14 / 16 / 22px for panels; `100px` pill for buttons and tags.
- **Shadows** are warm and soft (brown-tinted, never gray/black). Four levels in
  `tokens.css`; the CTA glow is clay-tinted.
- **Motion:** one easing curve everywhere — `cubic-bezier(0.22, 1, 0.36, 1)` —
  at ~0.3s. Buttons lift 2px on hover; arrows nudge 4px.

---

## 5 · Components (from the live site)

- **Buttons** — pill-shaped. Primary = ink fill / cream text → clay-deep on
  hover. Clay = `clay-bright` fill / white text with a clay glow. Ghost =
  transparent with a `line` border. All lift 2px on hover.
- **Cards** — `surface` fill, `line` border, large radius, soft warm shadow.
- **Eyebrow + serif title + sans intro** is the standard section header stack.

The canonical implementation is the website stylesheet at `../styles.css`;
`tokens.css` here is the portable extract for new projects.

---

## Note on PNG exports

PNGs in `logo/png/` are rasterized from the SVGs via a headless browser so the
pixel edges stay crisp and the background is transparent (dark variants sit on
ink `#211D18`). To re-export after changing the logo, re-run `build-logo.py`,
then re-render `_export.html` (the export harness) — or just use the SVGs, which
are resolution-independent and the preferred format everywhere they're supported.
