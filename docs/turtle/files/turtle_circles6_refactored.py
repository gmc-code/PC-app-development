import turtle
import math
import random

s = turtle.Screen()
s.bgcolor("black")
s.tracer(10, 0)


def create_turtle(color="white"):
    t = turtle.Turtle()
    t.speed(0)
    t.color(color)  # set the color of turtle; no shape is set
    t.pendown()  # pen placed down
    return t  # returns the turtle player object.


def drawCircles(t, size, size_change, circ_range):
    for i in range(circ_range):
        t.circle(size)
        size = size - size_change


def drawSpecial(t, size, size_change, circ_range, repeat):
    for i in range(repeat):
        drawCircles(t, size, size_change, circ_range)
        t.right(360 / repeat)


t_A = create_turtle(color="white")
drawSpecial(t_A, 100, 4, 10, 10)
t_B = create_turtle(color="yellow")
drawSpecial(t_B, 100, 10, 4, 10)
t_C = create_turtle(color="blue")
drawSpecial(t_C, 100, 5, 4, 10)
t_D = create_turtle(color="orange")
drawSpecial(t_D, 100, 19, 4, 10)
t_E = create_turtle(color="pink")
drawSpecial(t_E, 100, 20, 4, 10)

# This keeps the turtle drawing on the screen!
turtle.done()
