import cairo
import math
import time
from pathlib import Path

WIDTH = 30
HEIGHT = 30
PIXEL_SCALE = 20


def create_surfaceSVG(filepath):
    # dateStr = (datetime.now()).strftime("%d%b%Y-%H%M%S")
    fileName = "spiro.svg"  # "spiro-" + dateStr + ".svg"
    surface = cairo.SVGSurface(filepath, WIDTH * PIXEL_SCALE, HEIGHT * PIXEL_SCALE)
    return surface


def create_ctx(surface):
    ctx = cairo.Context(surface)
    ctx.scale(PIXEL_SCALE, PIXEL_SCALE)
    ctx.set_source_rgb(1, 1, 1)
    ctx.rectangle(0, 0, WIDTH, HEIGHT)
    ctx.fill()
    ctx.translate(WIDTH / 2, HEIGHT / 2)
    return ctx


# Create the spirograph points
def create_spiro(a, b, d):
    dt = 0.01
    t = 0
    pts = []
    while t < 2 * math.pi * b / math.gcd(a, b):
        t += dt
        x = (a - b) * math.cos(t) + d * math.cos((a - b) / b * t)
        y = (a - b) * math.sin(t) - d * math.sin((a - b) / b * t)
        pts.append((x, y))
    return pts


# Draw the curve
def draw_spiro(ctx, a, b, d, color):
    ctx.set_line_width(0.1)
    ctx.set_source_rgb(*color)
    pts = create_spiro(a, b, d)
    ctx.move_to(pts[0][0], pts[0][1])
    for x, y in pts[1:]:
        ctx.line_to(x, y)
    ctx.stroke()
    return ctx


def spiro_files2(a1, a2, b1, b2, d1, d2, im_fol):
    imgfolderpath = Path(__file__).parent / im_fol
    for d in range(d1, d2):
        for a in range(a1, a2):
            for b in range(b1, b2):
                if a == b:
                    continue
                surface = create_surfaceSVG(imgfolderpath / "temp.SVG")
                ctx = create_ctx(surface)
                ctx = draw_spiro(ctx, a, b, d, (0, 0, 0.5))
                fileName = "spiro-" + str(100*a + 10*b + d) + ".png"
                time.sleep(0.2)
                surface.write_to_png(imgfolderpath / fileName)
                time.sleep(0.2)

def spiro_files_d(a, b, d1, d2, im_fol):
    imgfolderpath = Path(__file__).parent / im_fol
    for d in range(d1, d2):
        surface = create_surfaceSVG(imgfolderpath / "temp.SVG")
        ctx = create_ctx(surface)
        ctx = draw_spiro(ctx, a, b, d, (0, 0, 0.5))
        fileName = "spiro-" + str(100*a + 10*b + d) + ".png"
        time.sleep(0.2)
        surface.write_to_png(imgfolderpath / fileName)
        time.sleep(0.2)

# spiro_files(a1, a2, b1, b2, d1, d2, im_fol)
#spiro_files2(10, 20, 9, 10, 8, 9, "Spiro_a/")
spiro_files_d(10, 11, 0, 10, "Spiro_b/")
#spiro_files2(8, 9, 9, 10, 5, 15, "Spiro_d/")
