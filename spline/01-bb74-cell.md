# Scene 1 · BB·74 cell

**Where it goes on the site:** the hero, replacing the flat drawing of the cell. The cell turns slowly, tilts toward the cursor, and comes apart along its axis as you scroll, showing the protection board and NFC chip inside the cap.

**Spline file name:** `anodyne-bb74`

## What it should feel like

A precision object, not a commodity battery. Satin green wrap with crisp black print, a machined graphite cap like the crown of a good watch, and a polished nickel + button. In the hero shot it should read clearly as a battery, and look more expensive than any battery you've seen.

## Quick try with Spline AI (optional)

Text-to-3D won't give separate parts, so it can't come apart on scroll. It's still useful for a look test before building:

> A single cylindrical lithium battery cell lying on its side, 18 mm diameter and 69 mm long, product photography. Satin bright green wrap with a large black printed label "BB·74". The positive end is a short dark graphite anodised aluminium collar with a small polished nickel button terminal. One thin raised black band near the flat negative end. Premium, minimal, industrial design, Teenage Engineering meets Apple. Soft studio light, transparent background.

## Build it (the version I can animate)

All parts are cylinders lying along the X axis. Negative end at x = 0, positive end at x = 69 mm. The cell's diameter is 18.6 mm.

| Part name | Shape | Size (mm) | Position along X (mm) | Material |
|---|---|---|---|---|
| `bb74-negative` | Cylinder | Ø17.4 × 0.3 | 0 – 0.3 | `nickel` |
| `bb74-wrap` | Cylinder, 0.8 mm bevel on the negative edge | Ø18.6 × 60.7 | 0.3 – 61.0 | `wrap-li` with `assets/bb74-wrap.png` |
| `bb74-band` | Cylinder (thin ring) | Ø18.8 × 1.5 | 4.0 – 5.5 | `black-satin` |
| `bb74-cap` | Cylinder, 0.4 mm chamfer on the outer + edge | Ø18.6 × 6.6 | 61.0 – 67.6 | `al-graphite` |
| `bb74-insulator` | Cylinder | Ø12 × 0.2 | 67.6 – 67.8 | `black-satin` |
| `bb74-button` | Cylinder, 0.4 mm fillet on top edge | Ø7.0 × 1.2 | 67.8 – 69.0 | `nickel` |

Put all of them in a group called `bb74`, centered on the world origin.

**The band** is 0.1 mm proud of the wrap on purpose. UBS chemistry bands are raised so you can feel them. It should catch a thin highlight from the rim light.

**The wrap label.** Apply `assets/bb74-wrap.png` as an image layer on top of the green.
- The image's width runs along the cell and its height wraps around it.
- The label is printed twice, half a turn apart, so one copy always faces the camera whichever way the cell turns.
- If the text comes out sideways or stretched, rotate the image 90° in the layer settings, or swap its X/Y scale. The left side of the image (the empty strip) belongs at the negative end, next to the band.

**Cap detail (nice to have).** Two fine grooves around the cap, at x = 63 and x = 65. Thin rings, Ø18.65 × 0.3, in slightly darker graphite are enough. This is the watch-crown detail.

### Inside the cap (for the scroll animation)

These sit hidden inside `bb74-cap`. When the page scrolls, I slide them out along +X so the cap opens like the exploded drawing on the site. Keep them inside the cap, stacked in this order:

| Part name | Shape | Size (mm) | Center at x (mm) | Material |
|---|---|---|---|---|
| `bb74-ntc` | Box | 2 × 1 × 1 | 61.5 | `chip` |
| `bb74-nfc` | Disc with a 3 × 3 × 0.6 box on top | Ø9 × 0.4 | 62.5 | `pcb`, box `chip` |
| `bb74-board` | Disc with three small boxes (2×2, 3×1.5, 1.5×1.5, 0.6 tall) | Ø16 × 1.0 | 64.0 | `pcb`, boxes `chip` |
| `bb74-ptc` | Ring (torus or tube) | Ø14 outside, Ø8 inside, 0.6 thick | 66.5 | `al-silver` |

Put each part's small boxes inside that part's group so they move together.

## Camera and framing

- The cell lies horizontally with the + end to the right.
- Turn the cell about its own axis so the big "BB·74" faces the camera.
- The camera sits about 12° above the cell and about 20° to the left of straight-on, so you see a little of the negative end's flat face.
- The cell fills about 80% of the frame width, with a little extra room on the right for the parts to slide out.
- Contact-shadow plane just under the cell, stretched to about 1.3× the cell length.

## Lights

The shared setup from the README. One extra: make sure the rim light draws a line along the top edge of the cap chamfer and the button's fillet. The metal parts should sparkle a little and the wrap should stay soft.

## Optional: the orange variant

If you want the page to switch the cell between chemistries, add a second wrap material `wrap-lfp` with `assets/bb32-wrap.png`, and a second band `bb74-band-2` at x 7.0–8.5, hidden by default. LiFePO₄ cells have two bands. I can swap them from code, but skip this on the first pass.

## Done when

- [ ] Group `bb74` contains every part listed, named exactly.
- [ ] The label reads correctly and "BB·74" faces the camera.
- [ ] Background is transparent and zoom is off in the export.
- [ ] You've sent me the `scene.splinecode` URL.
