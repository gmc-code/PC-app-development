import turtle

s = turtle.Screen()
s.tracer(0, 0)
s.bgcolor("black")

t = turtle.Turtle()


colors = ["red", "purple", "blue", "green", "orange", "yellow"]

t.speed(0)
t.hideturtle()

h = turtle.heading()

for i in range(6):
    for x in range(180):
        t.pencolor(colors[x % len(colors)])
        t.width(1)
        t.forward(x)
        t.left(59)
    t.penup()
    t.goto(0, 0)
    h += 60
    t.setheading(h)
    t.pendown()

# This keeps the turtle drawing on the screen!

turtle.done()
