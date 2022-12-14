import cairo
import math
from datetime import datetime
import time
from pathlib import Path

WIDTH = 30
HEIGHT = 30
PIXEL_SCALE = 20
imgfolderpath = Path(__file__).parent / "Images/"


def create_surfaceSVG():
    dateStr = (datetime.now()).strftime("%d%b%Y-%H%M%S")
    fileName = "spiro-" + dateStr + ".svg"
    surface = cairo.SVGSurface(
        imgfolderpath / fileName, WIDTH * PIXEL_SCALE, HEIGHT * PIXEL_SCALE
    )
    ctx = cairo.Context(surface)

    # surface = cairo.ImageSurface(
    #     cairo.FORMAT_RGB24, WIDTH * PIXEL_SCALE, HEIGHT * PIXEL_SCALE
    # )
    # ctx = cairo.Context(surface)
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


ctx = create_surfaceSVG()
draw_spiro(ctx, 16, 11, 7, (0, 0, 0.5))

for i in range(8, 16):
    ctx = create_surfaceSVG()
    draw_spiro(ctx, i, 11, 7, (0, 0, 0.5))

    # dateStr = (datetime.now()).strftime("%d%b%Y-%H%M%S")
    # fileName = "spiro-" + dateStr + ".png"

    # surface.write_to_png(fileName)
    time.sleep(1)
