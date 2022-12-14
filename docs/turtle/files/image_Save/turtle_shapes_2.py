import turtle
from math import cos, sin, tan, pi
from datetime import datetime
from PIL import Image


window = turtle.Screen()
window.screensize(1000, 1000)
window.tracer(72, 0)

pen = turtle.Turtle()
pen.hideturtle()
pen.pensize(3)
pen.penup()

angle = 0
theta = 0.01
a = -7
b = -17
c = 27
d = -4
steps = int(250 * pi / theta)
turtle.tracer(0, 0)

for t in range(0, steps):

    angle += theta
    x = (-cos(a * angle / d) - cos(b * angle / d) + cos(c * angle / d)) * 150
    y = (-sin(a * angle / d) - sin(b * angle / d) + sin(c * angle / d)) * 150

    pen.goto(x, y)
    pen.pendown()
turtle.update()

# date = (datetime.now()).strftime("%d%b%Y-%H%M%S")
# fileName = "turtle-" + date

screen = turtle.Screen()
screen.setup(1000, 1000)
# turtle = turtle.Turtle(visible=False)
screen.tracer(False)
screen.tracer(True)
# canvas = screen.getcanvas()
# canvas.postscript(file=fileName + ".eps", width=1000, height=1000)

# img = Image.open(fileName + ".eps")
# img.save(fileName + ".jpg")
turtle.done()
print("it is done")
