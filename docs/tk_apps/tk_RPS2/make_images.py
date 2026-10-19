"""Draws the rock paper scissors images used by tk_rock_paper_scissors_v2.py."""
from PIL import Image, ImageDraw, ImageFont

S = 4                    # draw 4x bigger, then shrink for smooth edges
W = 120                  # drawing grid size
BG = {"win": "#4caf50", "lose": "#f44336", "tie": "#9e9e9e",
      "start": "#6750a4", "icon": "#ede7f6"}
WHITE = (255, 255, 255, 255)
ROCK = "#8d6e63"         # brown
ROCK_SHADE = "#5d4037"   # dark brown
BLADE = "#37474f"        # dark grey-blue
HANDLE = "#263238"       # very dark grey
PAPER_LINE = (0, 0, 0, 70)
PAPER_EDGE = "#9e9e9e"


def base(color):
    im = Image.new("RGBA", (W * S, W * S), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    d.rounded_rectangle([0, 0, W * S - 1, W * S - 1], radius=22 * S, fill=color)
    return im, d


def p(x, y):
    return (x * S, y * S)


def rock(d):
    pts = [(30, 70), (34, 46), (52, 32), (74, 34), (90, 48), (94, 70),
           (84, 88), (58, 94), (38, 88)]
    d.polygon([p(*q) for q in pts], fill=ROCK)
    shade = [(34, 76), (58, 82), (82, 74), (94, 70), (84, 88), (58, 94), (38, 88)]
    d.polygon([p(*q) for q in shade], fill=ROCK_SHADE)
    d.polygon([p(46, 44), p(56, 38), p(64, 42), p(54, 50)], fill="#a1887f")  # highlight


def paper(d):
    d.polygon([p(36, 22), p(74, 22), p(88, 36), p(88, 98), p(36, 98)],
              fill=WHITE, outline=PAPER_EDGE, width=2 * S)
    d.polygon([p(74, 22), p(74, 36), p(88, 36)], fill="#d6d6d6", outline=PAPER_EDGE)
    for y in (48, 60, 72, 84):
        d.line([p(44, y), p(80, y)], fill=PAPER_LINE, width=3 * S)


def scissors(d):
    d.polygon([p(42, 74), p(48, 80), p(92, 26), p(86, 24)], fill=BLADE)
    d.polygon([p(72, 80), p(78, 74), p(34, 24), p(28, 26)], fill=BLADE)
    for cx in (38, 82):
        d.ellipse([p(cx - 13, 78), p(cx + 13, 104)], outline=HANDLE, width=7 * S)
    d.ellipse([p(56, 49), p(64, 57)], fill="#b0bec5")


def question(d):
    f = ImageFont.truetype("DejaVuSans-Bold.ttf", 80 * S)
    d.text(p(60, 62), "?", font=f, fill=WHITE, anchor="mm")


DRAW = {"rock": rock, "paper": paper, "scissors": scissors}


def save(im, name, size):
    im.resize((size, size), Image.LANCZOS).save(f"rps_images/{name}.png")


for name, fn in DRAW.items():
    for result in ("win", "lose", "tie"):
        im, d = base(BG[result])
        fn(d)
        save(im, f"{name}_{result}", 120)
    im, d = base(BG["icon"])       # small icon for the button
    fn(d)
    save(im, f"{name}_icon", 64)
im, d = base(BG["start"])
question(d)
save(im, "question", 120)

if __name__ == "__main__":
    names = [f"{n}_{r}" for n in DRAW for r in ("win", "lose", "tie")] + ["question"]
    sheet = Image.new("RGB", (W * 5 + 60, W * 2 + 110), "white")
    for i, n in enumerate(names):
        im = Image.open(f"rps_images/{n}.png")
        sheet.paste(im, (10 + (i % 5) * (W + 10), 10 + (i // 5) * (W + 10)), im)
    for i, n in enumerate(DRAW):
        im = Image.open(f"rps_images/{n}_icon.png")
        sheet.paste(im, (10 + i * 80, 2 * (W + 10) + 10), im)
    sheet.save("sheet.png")
