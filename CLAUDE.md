# UBS / Anodyne: notes for Claude

## What this repo is

- **UBS (Universal Battery System):** a concept for an open standard for rechargeable cells. The full summary is in `README.md`.
- **Anodyne:** a fictional hardware brand that builds for UBS. Every product ships without cells.
- **`index.html`:** the whole website in one self-contained file (inline CSS and JS, Google Fonts only). It is published with GitHub Pages from `main` at https://tagelokoy.github.io/UBS/.

## Working on the site

- Keep it a single file with no build step.
- Colors are CSS tokens on `:root` with a dark theme. The layout has to work at phone width.
- Drawings are inline SVG generated in the script at the bottom of the file. The `cell()` helper draws a UBS cell.
- Devices are grey. Color comes only from cells: `--li` green `#2FE070` for Li-ion, `--lfp` orange `#FF6A1A` for LiFePO₄.
- Copy is plain and direct. No marketing filler.

## 3D with Spline (MCP)

The Spline desktop app exposes an MCP server. When it's connected (check with `/mcp`), use it to build the scenes described in `spline/`:

1. Read `spline/README.md` first. It holds the style, the materials, the units (1 mm = 10 units), the lighting, and the export settings.
2. Build the scenes in this order: `spline/01-bb74-cell.md`, then `02-ch1-pip.md`, then `03-pb-stack.md`. The cell is reused in the other two.
3. **Part names must match the briefs exactly.** The site drives the scenes by name: explode on scroll, lid hinge, slow turn.
4. Label and screen images are in `spline/assets/`. Their sources are in `spline/assets/src/`.
5. After each scene, get the exported `scene.splinecode` URL and wire it into `index.html`:
   - Lazy-load it when the section scrolls into view.
   - Keep the existing SVG drawing as the fallback and as the poster shown before the scene loads.
   - Respect `prefers-reduced-motion`.
   - Don't let the scene capture page scroll or zoom.
6. Check the result on an iPad before it's merged to `main`. Keep to at most three live 3D scenes on the page.

## Git

- `main` is the live site. GitHub Pages deploys from it, so every change on `main` is public within a minute or two.
- Don't commit to `main` directly. Work on a branch, push it, and open a pull request. The owner merges it when it's ready to go live.
- Before starting, pull the latest `main`. Another Claude session may be working on the same repo.
