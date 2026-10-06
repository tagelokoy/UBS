# Scene 3 · PB Stack power bank (PB-4)

**Where it goes on the site:** the PB Stack card, and possibly the "Use whatever cells you have" section. On scroll, the two modules separate from the core like a vertical exploded view, and you see that each module is just two slots and a small converter board.

**Spline file name:** `anodyne-pb4`

## What it should feel like

A small upright slab: a solid aluminium core on top with a sharp screen, and two clear modules below that show four cells, two green and two orange. It should look like a precision instrument that happens to be a power bank. The mixed colors are the point: they show at a glance that you can mix chemistries.

## Quick try with Spline AI (optional)

> A premium modular power bank standing upright, 100 mm wide, 130 mm tall, 28 mm deep. The top section is solid bead-blasted silver anodised aluminium with a small flush black glass display showing large white numbers and two USB-C ports on the top face. Below it, two stacked clear polycarbonate modules framed by thin aluminium end blocks, each holding two cylindrical battery cells lying horizontally: two bright green cells and two bright orange cells. Small flush Torx screws on the end blocks. Minimal industrial design, Teenage Engineering meets Apple, studio product shot, transparent background.

## Build it

The stack stands upright. Width runs along X (−50 to +50), height along Y (bottom at y = 0), depth along Z (−14 to +14; +Z faces the camera).

Total size of the PB-4: **100 wide × 130 tall × 28 deep**. From the bottom up: base 4 mm, module 2 at 4–54, module 1 at 54–104, core at 104–130. Each module is 50 mm tall, including a 0.6 mm shadow gap at its top.

### Core (top), group `pb-core`

| Part name | Shape | Size (mm) | Where | Material |
|---|---|---|---|---|
| `pb-core-body` | Rounded box, 5 mm radius on the four vertical edges, 0.6 mm chamfer on the top edges | 100 × 26 × 28 | y 104–130 | `al-silver` |
| `pb-display` | Box, 1 mm corner radius, flush with the front face | 36 × 18 (× 0.5) | Front face (+Z), left side: centered at x = −24, y = 117 | `display` with `assets/pb-display.png` |
| `pb-button` | Short cylinder, flush, with a concentric machined texture if you made one | Ø7 × 0.5 proud | Front face, x = +36, y = 117 | `al-silver` (concentric) |
| `pb-led` | Tiny cylinder | Ø1 | Front face, x = +26, y = 117 | white, unlit, soft glow |
| `pb-port-1`, `pb-port-2` | Rounded boxes (1.6 mm radius) cut into or placed flush on the **top** face, in dark `chip` | 8.9 × 3.2 openings | x = −14 and x = +14, centered in depth | `chip` |
| `pb-etch` | Text "ANODYNE  PB-4  140 W", monospace, 2 mm tall | — | Top face, in front of the ports | `etch` |

### Modules, groups `pb-mod-1` (upper) and `pb-mod-2` (lower)

Build one module, then duplicate it. Each module spans the full 100 × 49.4 × 28, with a 0.6 mm gap above it.

| Part name (in module 1; use `-2` suffixes for module 2) | Shape | Size (mm) | Where (x) | Material |
|---|---|---|---|---|
| `pb-mod-1-end-l` | Box, 0.6 mm chamfer on the outer edges; outer vertical edges rounded 5 mm to match the core | 4 × 49.4 × 28 | −50 to −46 | `al-silver` |
| `pb-mod-1-end-r` | Same, mirrored | 4 × 49.4 × 28 | +46 to +50 | `al-silver` |
| `pb-mod-1-front` | Clear panel | 92 × 49.4 × 2 | Between the end blocks, front face | `pc-clear` |
| `pb-mod-1-back` | Clear panel | 92 × 49.4 × 2 | Between the end blocks, back face | `pc-clear` |
| `pb-mod-1-top` / `pb-mod-1-bottom` | Thin clear plates closing the module | 92 × 1.5 × 24 | Top and bottom of the module | `pc-clear` |
| `pb-mod-1-board` | Upright PCB near the right end block | 1 × 44 × 20 | x = +40 | `pcb` |
| `pb-mod-1-coil-a`, `-coil-b` | Small boxes (the per-slot converters), one per slot | 4 × 4 × 3 | On the board, one level with each cell | `chip` |
| `pb-mod-1-screws` | Four Torx screw heads, flush | Ø2.4 | Front face of each end block, 8 mm from the top and bottom | `al-graphite` |
| `pb-mod-1-cell-a` | Copy of the `bb74` cell | Ø18.6 × 69 | Lying along X in the upper slot: x −44 to +25, centered 13 mm above the module's middle | as scene 1 |
| `pb-mod-1-cell-b` | Copy of the `bb74` cell | same | Lower slot, centered 13 mm below the module's middle | as scene 1 |
| `pb-mod-1-contacts` | Four thin nickel plates, one at each end of each slot | 0.4 × 8 × 8 | At x = −45 and x = +27 | `nickel` |

**Module 2** is the same, but its two cells use the orange wrap: material `wrap-lfp` with `assets/bb32-wrap.png`, and a second band at x 7.0–8.5 (LiFePO₄ cells have two bands). Name them `pb-mod-2-cell-a` and `pb-mod-2-cell-b`.

The cells are BB size in slots sized for B, so there's a few millimetres of air around them and a gap at the + end. Keep that gap; it shows the slots are universal.

### Base, `pb-base`

| Part name | Shape | Size (mm) | Where | Material |
|---|---|---|---|---|
| `pb-base` | Rounded box matching the core's corners | 100 × 4 × 28 | y 0–4 | `al-silver` |
| `pb-feet` | Two rubber strips | 80 × 0.8 × 4 | Under the base | `rubber` |

### Group structure

```
pb
├─ pb-core      (core body, display, button, led, ports, etch)
├─ pb-mod-1     (end blocks, panels, board, coils, screws, contacts, cell-a, cell-b)
├─ pb-mod-2     (same, with orange cells)
└─ pb-base      (base, feet)
```

On scroll, I move `pb-core` up and `pb-mod-2` + `pb-base` down to open the stack. Keep each group's origin at its own center.

## Camera and framing

- A three-quarter front view from the left, about 15° above the middle of the stack.
- You should see the front (screen, cells through the clear panels) and a sliver of the left end blocks with their screws.
- The screen should be readable at website size.
- The stack fills about 65% of the frame height, with room above and below for it to open.
- Contact-shadow plane under the base.
- Rim light from behind, so the clear panels show a thin bright edge and the cells glow through them.

## Frosted or clear?

Start with clear (`pc-clear`, blur 0). If the inside looks too busy, try blur 4–6 on the **back** panels only. The cells stay crisp from the front and the background softens.

## Done when

- [ ] Group structure as above, parts named exactly.
- [ ] Module 1 has green cells, module 2 has orange cells with two bands.
- [ ] The screen is crisp and glowing.
- [ ] Background is transparent and zoom is off in the export.
- [ ] You've sent me the `scene.splinecode` URL.
