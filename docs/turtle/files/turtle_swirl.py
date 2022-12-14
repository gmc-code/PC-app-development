# rainbow turtle
# https://www.safaribooksonline.com/library/cover/9781491951071/360h/
#
import turtle

colors = ["red", "purple", "blue", "green", "yellow", "orange"]

s = turtle.Screen()
s.tracer(1, 0)
s.bgcolor("white")


t = turtle.Turtle()
t.speed(10)
# turtle.bgcolor('black')


def drawRainbow():
    for x in range(360):
        t.pencolor(colors[x % 6])
        t.width(x / 100)
        t.forward(x)
        t.right(55)


drawRainbow()
turtle.done()
# window exit on click
