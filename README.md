# UBS — Universal Battery System

A concept for an open standard for rechargeable cells, and a website for **Anodyne**, a fictional brand that builds hardware for it.

Open `index.html` in a browser. It is a single self-contained file with no build step. Fonts come from Google Fonts, and everything else is inline.

## The idea

Cells should outlive the devices they power. Devices ship without batteries, you keep a pool of standard cells, and a charger tracks each cell's health no matter which device it lived in.

## UBS draft 0.3 (as shown on the site)

| § | Part | Proposal |
|---|------|----------|
| 1 | Sizes | **BBB** (14500 base, Ø14.5 × 53.0 mm) · **BB** (18650, Ø18.6 × 69.0 mm) · **B** (21700, Ø21.7 × 75.0 mm). Button top only. Fixed outer size includes protection. **A** reserved for a larger future size. |
| 2 | Chemistry | **Green + 1 band** = Li-ion (3.6 V) · **Orange + 2 bands** = LiFePO₄ (3.2 V) · **Blue + 3 bands** = sodium-ion (reserved). Bands make it readable without color vision and by touch. Devices must accept 2.0–4.2 V per cell. |
| 3 | Protection | Mandatory in every cell: overcharge, over-discharge, over-current, short circuit, temperature. |
| 4 | Passport | NFC tag + fuel gauge in the cap, antenna on ferrite under the wrap. Signed identity, rating, live charge and current, cycles, health. Read by phone (tap cell after cell), even through a clear device housing while in use. No extra contacts. |
| 5 | Rating code | Two digits, like IP67. First digit = energy class, second = power class. `BB·74` = BB cell, ≥ 12 Wh, ≥ 35 W continuous. Devices print a minimum, for example `UBS BB · P5`. |
| 6 | Bays (optional) | Universal slots, each with its own DC/DC converter feeding a shared bus. Mix sizes, chemistries and health. Costs about 8% efficiency. Proposal: slots flip polarity so cells go in either way round. |
| 7 | Return credit | Any UBS seller takes back any UBS cell for €3 off new UBS cells. NFC marks the cell returned (no double claims, no fakes) and tells recyclers the chemistry. Funded by makers paying €3 per cell sold into a shared pool. A condition of using the UBS mark. |

**Energy class** (Wh, from capacity × nominal voltage): 0 < 2 · 1 ≥ 2 · 2 ≥ 3 · 3 ≥ 4.5 · 4 ≥ 6 · 5 ≥ 8 · 6 ≥ 10 · 7 ≥ 12 · 8 ≥ 15 · 9 ≥ 18

**Power class** (W, from continuous current × nominal voltage): 0 < 5 · 1 ≥ 5 · 2 ≥ 10 · 3 ≥ 20 · 4 ≥ 35 · 5 ≥ 50 · 6 ≥ 75 · 7 ≥ 100 · 8 ≥ 125 · 9 ≥ 150

## Anodyne products on the site

- **Cells:** BBB·22, BBB·11, BB·74, BB·66, BB·32, B·94, B·88, B·53
- **FL-1 Wick:** flashlight with a clear body window
- **PB Stack:** modular clear power bank (PB-2 / PB-4 / PB-8) with per-slot converters
- **SD-1 Spindle:** long clear screwdriver holding two BB cells end to end, runs on one or two
- **RX-1 Relay:** DAB+/FM survival radio with a three-slot bay, solar and crank
- **CH-1 Pip / CH-4 Quad / CH-12 Barrel:** chargers, from a USB-C stick to a rotating 12-chamber barrel
- **Pool app:** reads any UBS cell over NFC

Every product ships empty.

## Why now

Tool brands already run one battery across their own tools (Ryobi ONE+, Makita LXT, Milwaukee M18, DeWalt), and alliances like Bosch's Power for All and Metabo's CAS share one across several brands. UBS makes that idea public, the way USB-C replaced proprietary chargers. EU rules also require user-replaceable batteries in most portable appliances from February 2027.

## 3D (Spline)

Briefs for three 3D scenes (BB·74 cell, CH-1 Pip, PB Stack), with ready-made label and display images, are in [`spline/`](spline/README.md).

## Open questions

Keeping BBB out of AA devices, NFC on metal cans and in metal devices, reading many cells quickly, independent rating verification, in-device charging rules, bay efficiency, whether any-way-in slots should be required, credit versus cash for returns, and sodium-ion's 0 V storage versus the over-discharge rule.
