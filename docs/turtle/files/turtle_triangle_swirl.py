import turtle
import time

s = turtle.Screen()
s.tracer(10, 0)
s.bgcolor("white")

t = turtle.Turtle()
# t.shape("turtle")
t.color("blue")
t.speed(0)
t.hideturtle()

# The angle to turn for a triangle is 121 degrees
# if you turn just over it, then you get the shifting shape!
# try other angles
# the angle to turn for a square is 90
# the angle to turn for a pentagon is 72
# so, try 91 and 73!


### bonus
# can you think of a way to use variables to compute the angle for any number of sides?
# let's say the number of sides is n = 5
# what woudl the angle be?
for k in range(121, 150):
    for i in range(400):
        t.forward(i)
        t.left(k)
    time.sleep(0.5)
    t.reset()
    t.color("blue")
    t.width(2.5)
    t.speed(0)
    t.hideturtle()

turtle.done()
# window exit on click
