# Scene 2 · CH-1 Pip single-cell charger

**Where it goes on the site:** the CH-1 card in the chargers section. The lid opens a little on hover, and the screen shows the cell charging.

**Spline file name:** `anodyne-ch1-pip`

## What it should feel like

A small bar of machined aluminium that looks like it was cut from the edge of a MacBook. A clear half-tube lid over a green cell, and one small, very sharp screen. It should feel like a quality pocket tool, heavy for its size. It takes any USB-C cable and fits on a keyring.

## Quick try with Spline AI (optional)

> A compact single battery charger, a solid bar of bead-blasted silver anodised aluminium 112 mm long, 28 mm wide and 14 mm tall with softly rounded long edges. A half-round trough along the top holds one green cylindrical battery cell, covered by a clear polycarbonate half-tube lid. At one end, a tiny flush black glass display showing a green circular charge gauge. A USB-C port in the end face and a small keyring hole at the other end. Minimal industrial design, Apple meets Teenage Engineering, studio product shot, transparent background.

## Build it

Body length runs along X, from x = 0 (keyring end) to x = 112 (USB-C end). Y is up and the bottom of the body sits at y = 0.

### Body

| Part name | How | Size (mm) | Material |
|---|---|---|---|
| `pip-body` | Rounded box. 5 mm radius on the four long edges, 0.6 mm chamfer on the top edges | 112 × 14 × 28 (L × H × W) | `al-silver` |
| (cut) trough | Boolean **subtract** a cylinder lying along X. Its axis is on the top face, so half of it cuts into the body | Ø23 × 80, from x = 8 to x = 88 | — |
| (cut) keyring hole | Boolean **subtract** a cylinder running across the width | Ø3, centered at x = 4, y = 7 | — |
| (cut) USB-C port | Boolean **subtract** a rounded box, 1.6 mm corner radius, from the x = 112 end face | 8.9 × 3.2 × 7 deep, centered at y = 7 | — |

If the booleans are fiddly, a simpler version is fine: skip the trough cut and let the cell and lid sit on top of the body. It will still read.

### Parts on and in the body

| Part name | Shape | Size (mm) | Where | Material |
|---|---|---|---|---|
| `pip-display` | Box, 1 mm corner radius, flush with the top face | 16 × 12 (× 0.5 thick) | Top face, centered at x = 100 | `display` with `assets/ch1-display.png` |
| `pip-contact-neg` | Box | 0.4 × 9 × 9 | Inside the trough at x = 8.5 (left wall) | `nickel` |
| `pip-contact-pos` | Box | 0.4 × 6 × 6 | Inside the trough at x = 87.5 (right wall) | `nickel` |
| `pip-cell` | Copy of the whole `bb74` group from scene 1 | Ø18.6 × 69 | Lying in the trough, negative end against `pip-contact-neg`, resting on the trough floor | as scene 1 |
| `pip-lid` | Clear half-tube (a tube with its lower half cut away) | Ø26 outside, 1.5 mm wall, 82 long | Over the trough, from x = 7 to x = 89 | `pc-clear` |
| `pip-screw-1`, `pip-screw-2` | Short cylinders with a tiny star (Torx) recess, flush | Ø2.4 | On the x = 0 end face, 6 mm apart | `al-graphite` |
| `pip-etch` | Text "CH-1 PIP · ANODYNE", monospace, 2 mm tall | — | On the long side face nearest the camera, right-aligned near the USB end | `etch` |
| `pip-feet` | Two thin rounded strips | 90 × 0.8 × 3 each | Bottom face | `rubber` |

**The lid's pivot:** set `pip-lid`'s origin (pivot) on its **back** long edge, the edge away from the camera. That line is the hinge; I'll rotate it open by 20–30° on hover. If you can't move the pivot, leave it and tell me, and I'll work around it.

**The cell** sits slightly low in the trough: the trough is sized for the bigger B cell, so a BB rests on the bottom with some air above and around it. That gap is deliberate. It shows the slot takes every size.

**The screen** must stay bright and sharp. Use the image on an unlit layer with no roughness or reflection layer on top. A slight reflection on the black glass around the UI is good; a reflection across the UI itself is not.

## Camera and framing

- A three-quarter view from the front-right, about 30° above the top face, so you see the top (cell, lid, screen) and the USB-C end face.
- The screen should be readable: the "82" and the green ring should be clear at website size.
- The object fills about 75% of the frame width.
- Contact-shadow plane under the body.

## Done when

- [ ] Every part is named as listed, all inside a group called `pip`.
- [ ] `pip-lid` hinges on its back edge, or you've told me it doesn't.
- [ ] The screen is crisp and glowing.
- [ ] Background is transparent and zoom is off in the export.
- [ ] You've sent me the `scene.splinecode` URL.
