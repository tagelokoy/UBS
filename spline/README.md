# Spline briefs

Three 3D scenes for the Anodyne site, written so they can be built in Spline with as little time in the editor as possible. Build them, export each one, and send back the link. I'll wire them into the site.

| # | Scene | File | Rough time |
|---|-------|------|-----------|
| 1 | BB·74 cell | [01-bb74-cell.md](01-bb74-cell.md) | 20–30 min |
| 2 | CH-1 Pip charger | [02-ch1-pip.md](02-ch1-pip.md) | 30–45 min |
| 3 | PB Stack power bank | [03-pb-stack.md](03-pb-stack.md) | 45–60 min |

Start with the cell. It's the simplest, and the charger and power bank both reuse it: build it once, then copy it into the other two files.

## The look: a MacBook and a Teenage Engineering recorder had a baby

1. **Aluminium is the product.** Bead-blasted, anodised, cool silver. Big soft radii on the body (5–6 mm) and tiny crisp chamfers on the edges (0.4–0.6 mm). That pairing is most of what makes a MacBook look expensive.
2. **Color comes only from cells and screens.** Devices are silver, graphite and clear. No painted accents, no colored buttons.
3. **Clear polycarbonate wherever cells live**, so you always see what's inside.
4. **Honest fasteners.** Small flush Torx screws on end plates, placed on purpose, the way Teenage Engineering shows its screws.
5. **Small, sharp displays.** Black glass set flush into the metal, 1 mm corner radius, simple UI that glows. The UI images are ready in `assets/`.
6. **Tiny etched labels.** Monospace, uppercase, 1.5–2.5 mm tall, a slightly darker grey than the aluminium. Nothing bigger than that.
7. **Studio light.** One strong soft key light, a gentle fill, and a rim light behind the object to draw a bright line along the metal edges. That line is what sells "machined".

## Materials

Use these names for the materials in Spline so they can be reused across all three scenes.

| Material | Used for | Color | Settings (Spline "Physical" lighting) |
|---|---|---|---|
| `al-silver` | Device bodies | `#C8CCC7` | Metalness 1.0 · roughness 0.42 · add a Noise layer at 3–5% opacity, very fine scale, for bead-blast grain |
| `al-graphite` | Cell cap, small details | `#2A2D2B` | Metalness 1.0 · roughness 0.5 · same fine noise |
| `nickel` | Contacts, + button, cell bottom | `#BFC3BF` | Metalness 1.0 · roughness 0.18 |
| `pc-clear` | Clear panels and lids | tint `#E6EEEA` | Glass/transmission layer · IOR 1.58 · very light tint · blur 0. Frosted variant: blur 8–12 |
| `display` | Screens | `#050606` + UI image | Black glass, roughness 0.05. UI image on an **unlit** layer (no lighting) so it glows |
| `wrap-li` | Li-ion cell wrap | `#2FE070` + label image | Satin: roughness 0.38, metalness 0 |
| `wrap-lfp` | LiFePO₄ cell wrap | `#FF6A1A` + label image | Same as `wrap-li` |
| `black-satin` | Chemistry bands, insulator | `#141716` | Roughness 0.6 |
| `pcb` | Circuit boards | `#1B2A23` | Roughness 0.5 |
| `chip` | Tiny components | `#07090A` | Roughness 0.3 |
| `rubber` | Feet | `#1A1C1B` | Roughness 0.9 |
| `etch` | Laser-etched text on silver | `#7E847F` | Roughness 0.6, metalness 0.6 |

**Using Spline AI for textures (optional).** If you have the AI add-on, texture generation is a good use of it. Try:
- *"Seamless close-up of bead-blasted anodised aluminium, fine even micro-grain, cool neutral silver, no scratches, soft studio light"*
- *"Seamless machined concentric circle finish on aluminium, very fine grooves, like the face of a premium audio knob"*

## Conventions that let me drive the scenes from the page

- **Units:** 1 mm = 10 Spline units. All sizes in the briefs are in mm.
- **Axes:** Y is up. Cells lie along X with the + end pointing to +X.
- **Names matter.** Name every part exactly as listed in its brief; the page finds parts by name. Group parts as listed.
- **Keep parts separate.** Don't merge parts that the brief lists separately, even when they touch. Separate parts are what let the cell come apart as you scroll.
- **Pivot = center.** Leave each object's origin at its own center unless the brief says otherwise, for example the charger lid hinges along its back edge.
- **No animation needed.** I'll add motion in code: slow turn, hover tilt, and explode on scroll. If you want to play with Spline's own States and Events, go ahead, but it isn't required.

## Scene setup (same for all three)

- **Background:** transparent. The site's own background shows through.
- **Camera:** perspective with a narrow field of view (about 20–25°) so it looks like a long product-photo lens. Framing notes are in each brief.
- **Lights:**
  - *Key:* directional light from top-left-front, strong, soft shadows on.
  - *Fill:* from the right, about 30% of the key, no shadows.
  - *Rim:* from behind and above, aimed at the silhouette edges, about 60% of the key.
- **Contact shadow:** a flat plane under the object using `assets/contact-shadow.png` (transparent PNG) on an unlit layer, at about 60% opacity. It grounds the object without a floor.

## Export and send back

1. **Export → Code Export → Web** (the viewer embed).
2. In the export or play settings:
   - Background transparent.
   - Zoom **off**, so page scrolling isn't captured.
   - Pan off. Orbit can stay on.
3. Copy the scene URL. It ends in `scene.splinecode`.
4. Send me the URL for each scene. A screenshot of the result helps too.

The free plan shows a small "Built with Spline" badge on embeds. That's fine for a concept site.

## Assets

Ready-made images in `assets/`. Sources are in `assets/src/` if anything needs changing.

| File | Size | For |
|---|---|---|
| `bb74-wrap.png` | 2050 × 1962 | Wrap label for the green BB·74 |
| `bb32-wrap.png` | 2050 × 1962 | Wrap label for the orange BB·32 (power bank) |
| `pb-display.png` | 1140 × 570 | PB Stack screen, 2:1 |
| `ch1-display.png` | 960 × 720 | CH-1 Pip screen, 4:3 |
| `contact-shadow.png` | 1024 × 384 | Soft shadow plane under each product |

## If Spline eats too much time

These briefs are specific enough that I can build the same three scenes directly in code (three.js) instead. The result looks slightly less polished, but you'd spend no time in an editor. Just say so.
