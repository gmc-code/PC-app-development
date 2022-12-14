import turtle
import math
import random

s = turtle.Screen()
s.bgcolor("black")
s.tracer(10, 0)


class CircleTurtle:
    def __init__(self, color="white"):
        self.t = turtle.Turtle()
        self.t.speed(0)
        self.t.color(color)  # set the color of turtle
        self.t.pendown()  # pen placed down

    def drawCircles(self, size, size_change, circ_range):
        for i in range(circ_range):
            self.t.circle(size)
            size = size - size_change

    def drawSpecial(self, size, size_change, circ_range, repeat):
        for i in range(repeat):
            self.drawCircles(size, size_change, circ_range)
            self.t.right(360 / repeat)


t_A = CircleTurtle(color="white")
t_A.drawSpecial(100, 4, 10, 10)
t_B = CircleTurtle(color="yellow")
t_B.drawSpecial(100, 10, 4, 10)
t_C = CircleTurtle(color="blue")
t_C.drawSpecial(100, 5, 4, 10)
t_D = CircleTurtle(color="orange")
t_D.drawSpecial(100, 19, 4, 10)
t_E = CircleTurtle(color="pink")
t_E.drawSpecial(100, 20, 4, 10)

# This keeps the turtle drawing on the screen!
turtle.done()
