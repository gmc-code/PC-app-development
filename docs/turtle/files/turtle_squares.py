import turtle

s = turtle.Screen()
s.tracer(10, 0)
s.bgcolor("white")

t = turtle.Turtle()


def drawSquare(length):
    for i in range(4):
        t.forward(length)
        t.right(90)


# Draw 90 squares rotated 4 degrees
for i in range(90):
    drawSquare(100)
    t.right(4)

# Draw 45 squares rotated 8 degrees
for i in range(45):
    drawSquare(200)
    t.right(8)

turtle.done()
# window exit on click
