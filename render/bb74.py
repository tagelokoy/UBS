"""Render the Anodyne BB·74 cell with Blender (Cycles).

Builds the cell from spline/01-bb74-cell.md, lights it per spline/README.md and
renders a still with a transparent background and a soft contact shadow.

    blender -b -P render/bb74.py -- --out render/out/bb74.png
    blender -b -P render/bb74.py -- --out f.png --explode 0.6 --res 1600x900 --samples 64

--explode 0..1 slides the cap and its inner parts out along +X, the same moves
the site's scroll section uses. Units: 1 Blender unit = 10 mm (so 1 mm = 0.1).
"""
import bpy, bmesh, math, sys, os, argparse
from mathutils import Vector

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
argv = sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else []
ap = argparse.ArgumentParser()
ap.add_argument("--out", default=os.path.join(ROOT, "render", "out", "bb74.png"))
ap.add_argument("--explode", type=float, default=0.0)
ap.add_argument("--res", default="2400x1350")
ap.add_argument("--samples", type=int, default=256)
ap.add_argument("--turn", type=float, default=0.0, help="extra turn about the cell axis, degrees")
ap.add_argument("--view", default="hero", help="camera preset: " + ", ".join(
    ["hero", "button", "side", "top", "negative"]))
ap.add_argument("--az", type=float, help="camera azimuth, degrees (0 = front, + = toward the + end)")
ap.add_argument("--el", type=float, help="camera elevation, degrees")
ap.add_argument("--dist", type=float, help="camera distance, Blender units")
ap.add_argument("--tx", type=float, help="camera target along the cell, Blender units")
ap.add_argument("--blend", action="store_true", help="also save a .blend next to the image")
args = ap.parse_args(argv)

# camera presets: azimuth, elevation (degrees), distance, target x (Blender units)
VIEWS = {
    "hero":     (-20, 12, 26, 0.4),   # the brief's framing: a little above, a little left
    "button":   (62, 16, 22, 1.0),    # from the + end: cap, grooves and button face
    "side":     (0, 3, 26, 0.0),      # straight side-on
    "top":      (-30, 38, 26, 0.0),   # high three-quarter
    "negative": (-62, 14, 22, -1.0),  # from the negative end
}

MM = 0.1          # Blender units per mm
X0 = -34.5 * MM   # negative end; the cell is centred on the origin

# ---------------------------------------------------------------- scene
bpy.ops.wm.read_factory_settings(use_empty=True)
scene = bpy.context.scene
cell = bpy.data.objects.new("bb74", None)
scene.collection.objects.link(cell)


def hexcol(h, a=1.0):
    h = h.lstrip("#")
    srgb = [int(h[i:i + 2], 16) / 255 for i in (0, 2, 4)]
    lin = [c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4 for c in srgb]
    return (*lin, a)


def material(name, color, metal=0.0, rough=0.5, grain=0.0):
    m = bpy.data.materials.new(name)
    m.use_nodes = True
    nt = m.node_tree
    b = nt.nodes["Principled BSDF"]
    b.inputs["Base Color"].default_value = hexcol(color)
    b.inputs["Metallic"].default_value = metal
    b.inputs["Roughness"].default_value = rough
    if grain:  # bead-blast micro grain
        n = nt.nodes.new("ShaderNodeTexNoise")
        n.inputs["Scale"].default_value = 900.0
        n.inputs["Detail"].default_value = 2.0
        bump = nt.nodes.new("ShaderNodeBump")
        bump.inputs["Strength"].default_value = grain
        bump.inputs["Distance"].default_value = 0.002
        nt.links.new(n.outputs["Fac"], bump.inputs["Height"])
        nt.links.new(bump.outputs["Normal"], b.inputs["Normal"])
    return m


MAT = {
    "nickel": material("nickel", "#BFC3BF", 1.0, 0.28),
    "al-graphite": material("al-graphite", "#2A2D2B", 1.0, 0.3, grain=0.15),
    "al-graphite-dark": material("al-graphite-dark", "#1E2120", 1.0, 0.5),
    "al-silver": material("al-silver", "#C8CCC7", 1.0, 0.42, grain=0.15),
    "black-satin": material("black-satin", "#141716", 0.0, 0.6),
    "pcb": material("pcb", "#1B2A23", 0.0, 0.5),
    "chip": material("chip", "#07090A", 0.0, 0.3),
}


def wrap_material():
    """Satin green wrap with the label image. Coordinates are computed in the shader
    from object space: image width runs along the cell (+X), image height wraps
    around it, and "BB·74" faces +Z (the camera side)."""
    m = bpy.data.materials.new("wrap-li")
    m.use_nodes = True
    nt, L = m.node_tree, m.node_tree.links
    b = nt.nodes["Principled BSDF"]
    b.inputs["Roughness"].default_value = 0.38
    tc = nt.nodes.new("ShaderNodeTexCoord")
    sep = nt.nodes.new("ShaderNodeSeparateXYZ")
    L.new(tc.outputs["Object"], sep.inputs[0])
    # u = (x - start) / length, in object space where the wrap is centred on 0
    u = nt.nodes.new("ShaderNodeMapRange")
    u.inputs["From Min"].default_value = -30.35 * MM
    u.inputs["From Max"].default_value = 30.35 * MM
    L.new(sep.outputs["X"], u.inputs["Value"])
    # v = fract(1.01 - atan2(z, y) / 2pi): label copy centred on +Z, text upright
    at = nt.nodes.new("ShaderNodeMath"); at.operation = "ARCTAN2"
    L.new(sep.outputs["Z"], at.inputs[0]); L.new(sep.outputs["Y"], at.inputs[1])
    dv = nt.nodes.new("ShaderNodeMath"); dv.operation = "MULTIPLY"
    dv.inputs[1].default_value = -1 / (2 * math.pi)
    L.new(at.outputs[0], dv.inputs[0])
    ad = nt.nodes.new("ShaderNodeMath"); ad.operation = "ADD"
    ad.inputs[1].default_value = 1.01
    L.new(dv.outputs[0], ad.inputs[0])
    fr = nt.nodes.new("ShaderNodeMath"); fr.operation = "FRACT"
    L.new(ad.outputs[0], fr.inputs[0])
    comb = nt.nodes.new("ShaderNodeCombineXYZ")
    L.new(u.outputs["Result"], comb.inputs["X"]); L.new(fr.outputs[0], comb.inputs["Y"])
    img = nt.nodes.new("ShaderNodeTexImage")
    img.image = bpy.data.images.load(os.path.join(ROOT, "spline", "assets", "bb74-wrap.png"))
    img.interpolation = "Cubic"
    img.extension = "EXTEND"
    L.new(comb.outputs[0], img.inputs["Vector"])
    L.new(img.outputs["Color"], b.inputs["Base Color"])
    return m


MAT["wrap-li"] = wrap_material()


def cylinder(name, d_mm, x_from, x_to, mat, bevel_mm=0.0, segs=160, parent=None):
    """A cylinder along X from x_from to x_to (mm from the negative end)."""
    r, h = d_mm / 2 * MM, (x_to - x_from) * MM
    me = bpy.data.meshes.new(name)
    bm = bmesh.new()
    bmesh.ops.create_cone(bm, cap_ends=True, segments=segs, radius1=r, radius2=r, depth=h)
    bmesh.ops.rotate(bm, verts=bm.verts, cent=(0, 0, 0),
                     matrix=__import__("mathutils").Matrix.Rotation(math.radians(90), 3, "Y"))
    for f in bm.faces:
        f.smooth = abs(f.normal.x) < 0.5
    bm.to_mesh(me); bm.free()
    ob = bpy.data.objects.new(name, me)
    scene.collection.objects.link(ob)
    ob.location = (X0 + (x_from + x_to) / 2 * MM, 0, 0)
    ob.parent = parent or cell
    me.materials.append(MAT[mat])
    if bevel_mm:
        bv = ob.modifiers.new("bevel", "BEVEL")
        bv.width = bevel_mm * MM
        bv.segments = 4
        bv.limit_method = "ANGLE"
        bv.harden_normals = True
    return ob


def box(name, w, h, d, x_c, y=0.0, z=0.0, mat="chip", parent=None):
    """A box, sizes in mm, centred at x_c mm from the negative end."""
    me = bpy.data.meshes.new(name)
    bm = bmesh.new()
    bmesh.ops.create_cube(bm, size=1.0)
    bmesh.ops.scale(bm, vec=(w * MM, h * MM, d * MM), verts=bm.verts)
    bm.to_mesh(me); bm.free()
    ob = bpy.data.objects.new(name, me)
    scene.collection.objects.link(ob)
    ob.location = (X0 + x_c * MM, y * MM, z * MM)
    ob.parent = parent or cell
    me.materials.append(MAT[mat])
    return ob


def ring(name, d_out, d_in, x_c, t_mm, mat, parent=None):
    me = bpy.data.meshes.new(name)
    bm = bmesh.new()
    Rot = __import__("mathutils").Matrix.Rotation(math.radians(90), 3, "Y")
    a = bmesh.ops.create_circle(bm, cap_ends=False, segments=128, radius=d_out / 2 * MM)["verts"]
    b = bmesh.ops.create_circle(bm, cap_ends=False, segments=128, radius=d_in / 2 * MM)["verts"]
    edges = list({e for v in a + b for e in v.link_edges})
    face = bmesh.ops.bridge_loops(bm, edges=edges)["faces"]
    ext = bmesh.ops.extrude_face_region(bm, geom=face)
    bmesh.ops.translate(bm, vec=(0, 0, t_mm * MM),
                        verts=[g for g in ext["geom"] if isinstance(g, bmesh.types.BMVert)])
    bmesh.ops.translate(bm, vec=(0, 0, -t_mm * MM / 2), verts=bm.verts)
    bmesh.ops.recalc_face_normals(bm, faces=bm.faces)
    bmesh.ops.rotate(bm, verts=bm.verts, cent=(0, 0, 0), matrix=Rot)
    bm.to_mesh(me); bm.free()
    ob = bpy.data.objects.new(name, me)
    scene.collection.objects.link(ob)
    ob.location = (X0 + x_c * MM, 0, 0)
    ob.parent = parent or cell
    me.materials.append(MAT[mat])
    return ob


def group(name, x_c):
    e = bpy.data.objects.new(name, None)
    scene.collection.objects.link(e)
    e.parent = cell
    e.location = (0, 0, 0)
    return e


# ---------------------------------------------------------------- the cell
cylinder("bb74-negative", 17.4, 0.0, 0.3, "nickel")
cylinder("bb74-wrap", 18.6, 0.3, 61.0, "wrap-li", bevel_mm=0.8)
cylinder("bb74-band", 18.8, 4.0, 5.5, "black-satin", bevel_mm=0.15)
cap = cylinder("bb74-cap", 18.6, 61.0, 67.6, "al-graphite", bevel_mm=0.4)
grooves = [cylinder("bb74-groove-%d" % i, 18.65, x - 0.15, x + 0.15, "al-graphite-dark")
           for i, x in ((1, 63.0), (2, 65.0))]
ins = cylinder("bb74-insulator", 12.0, 67.6, 67.8, "black-satin")
btn = cylinder("bb74-button", 7.0, 67.8, 69.0, "nickel", bevel_mm=0.4)

ntc = box("bb74-ntc", 2, 1, 1, 61.5)
nfc = group("bb74-nfc", 62.5)
cylinder("bb74-nfc-disc", 9.0, 62.3, 62.7, "pcb", parent=nfc)
box("bb74-nfc-chip", 0.6, 3, 3, 63.0, parent=nfc)
board = group("bb74-board", 64.0)
cylinder("bb74-board-disc", 16.0, 63.5, 64.5, "pcb", parent=board)
box("bb74-board-chip-1", 0.6, 2, 2, 64.8, 2.5, -2.5, parent=board)
box("bb74-board-chip-2", 0.6, 1.5, 3, 64.8, -3.0, -1.0, parent=board)
box("bb74-board-chip-3", 0.6, 1.5, 1.5, 64.8, 1.0, 3.5, parent=board)
ptc = ring("bb74-ptc", 14.0, 8.0, 66.5, 0.6, "al-silver")

# explode: same moves as the site (mm)
e = max(0.0, min(1.0, args.explode))
for ob, d in [(ntc, 3), (nfc, 7), (board, 11.5), (ptc, 16)] + [(o, 20) for o in [cap, ins, btn] + grooves]:
    ob.location.x += d * MM * e
cell.location.x = -10 * MM * e
cell.rotation_euler.x = math.radians(args.turn)

# ---------------------------------------------------------------- stage
floor_z = -9.3 * MM  # cell bottom (radius 9.3 mm)
me = bpy.data.meshes.new("contact-shadow")
bm = bmesh.new()
bmesh.ops.create_grid(bm, x_segments=1, y_segments=1, size=100.0)
bm.to_mesh(me); bm.free()
floor = bpy.data.objects.new("contact-shadow", me)
scene.collection.objects.link(floor)
floor.rotation_euler = (0, 0, 0)
floor.location = (0, 0, floor_z)
floor.is_shadow_catcher = True

# Blender is Z-up and the camera sits on the -Y side. The label faces +Z in object
# space, so tip the cell 90° about its axis to turn the label toward the camera.
cell.rotation_euler.x += math.radians(90)


def area(name, loc, power, size, color="#FFFFFF"):
    ld = bpy.data.lights.new(name, "AREA")
    ld.energy = power
    ld.size = size
    ld.color = hexcol(color)[:3]
    ob = bpy.data.objects.new(name, ld)
    scene.collection.objects.link(ob)
    ob.location = loc
    c = ob.constraints.new("TRACK_TO")
    c.target = cell
    c.track_axis = "TRACK_NEGATIVE_Z"
    c.up_axis = "UP_Y"
    return ob


area("key", (-6, -6, 7), 900, 5.0)
area("fill", (8, -3, 1.5), 270, 4.0)
area("rim", (1, 7, 6), 650, 2.5, "#F2F6FF")
area("rim-low", (-3, 6, 0.5), 200, 2.0, "#F2F6FF")
area("top", (0, 1, 9), 500, 9.0)  # big overhead softbox: something for the metal to reflect

world = bpy.data.worlds.new("studio")
world.use_nodes = True
world.node_tree.nodes["Background"].inputs["Color"].default_value = hexcol("#9AA19C")
world.node_tree.nodes["Background"].inputs["Strength"].default_value = 0.6
scene.world = world

# camera: a preset, with any of its numbers overridden from the command line
v_az, v_el, v_dist, v_tx = VIEWS[args.view]
if args.view == "hero" and e > 0:
    v_dist, v_tx = 30.0, 0.0
v_az = v_az if args.az is None else args.az
v_el = v_el if args.el is None else args.el
v_dist = v_dist if args.dist is None else args.dist
v_tx = v_tx if args.tx is None else args.tx
target = bpy.data.objects.new("cam-target", None)
scene.collection.objects.link(target)
target.location = (v_tx, 0, 0)
cam_d = bpy.data.cameras.new("hero-camera")
cam_d.lens = 85
cam_d.sensor_width = 36
cam = bpy.data.objects.new("hero-camera", cam_d)
scene.collection.objects.link(cam)
dist = v_dist
el, az = math.radians(v_el), math.radians(v_az)
cam.location = (target.location.x + dist * math.cos(el) * math.sin(az),
                -dist * math.cos(el) * math.cos(az),
                dist * math.sin(el))
tc = cam.constraints.new("TRACK_TO")
tc.target = target
tc.track_axis = "TRACK_NEGATIVE_Z"
tc.up_axis = "UP_Y"
scene.camera = cam

# ---------------------------------------------------------------- render
r = scene.render
r.engine = "CYCLES"
w, h = (int(v) for v in args.res.lower().split("x"))
r.resolution_x, r.resolution_y, r.resolution_percentage = w, h, 100
r.film_transparent = True
r.image_settings.file_format = "PNG"
r.image_settings.color_mode = "RGBA"
scene.cycles.samples = args.samples
scene.cycles.use_denoising = True
try:
    # PBR Neutral keeps base colours true, so the wrap stays brand green
    scene.view_settings.view_transform = "Khronos PBR Neutral"
except TypeError:
    pass
try:
    prefs = bpy.context.preferences.addons["cycles"].preferences
    prefs.compute_device_type = "METAL"
    prefs.get_devices()
    for d in prefs.devices:
        d.use = True
    scene.cycles.device = "GPU"
except Exception as ex:  # CPU fallback
    print("GPU unavailable:", ex)

os.makedirs(os.path.dirname(os.path.abspath(args.out)), exist_ok=True)
r.filepath = os.path.abspath(args.out)
if args.blend:
    bpy.ops.wm.save_as_mainfile(filepath=os.path.splitext(r.filepath)[0] + ".blend")
bpy.ops.render.render(write_still=True)
print("Wrote", r.filepath)
