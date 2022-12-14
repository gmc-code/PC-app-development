import turtle as tur
import colorsys as cs

s = tur.Screen()
s.tracer(1000, 0)

tur.setup(800, 800)
tur.speed(0)
tur.width(5)
tur.bgcolor("black")
jval = 25
ival = 15
for j in range(jval):
    for i in range(ival):
        tur.color(cs.hsv_to_rgb(i / ival, j / jval, 1))
        tur.right(90)
        tur.circle(200 - j * 4, 90)
        tur.left(90)
        tur.circle(200 - j * 4, 90)
        tur.right(180)
        tur.circle(50, 24)
tur.hideturtle()
tur.done()
