====================================================
Turtle start
====================================================

| Watch: https://www.youtube.com/watch?v=N8SGEWSL3EI

----

Screen methods
----------------------------------------

s = turtle.Screen()
s.bgcolor(color)
s.title(text)
----

Keep screen open
----------------------------------------

| turtle.done() keeps the window open

----

Turtle methods
----------------------------------------

| t = Turtle() create a new Turtle object and open its window
| t.home() move the turtle to (0, 0), pointing east
| t.pendown() lower the pen for drawing (t.down())
| t.penup() raise the pen (t.up())
| t.isdown() return True if the pen is down
| t.pensize(k) set linewidth to k pixels
| t.heading() return the current direction (angle)
| t.setheading(d) change heading to direction d
| t.position() return the current position at a tuple (x, y)
| t.goto(x, y) move to coordinates (x, y)
| t.left(d) turn left, anticlockwise, d degrees
| t.right(d) turn right, clockwise, d degrees
| t.speed(n) how fast the turtle moves (0 .. 10)
| t.setx(n) set the turtle.s x coordinate, leave y unchanged
| t.sety(n) set the turtle.s y coordinate, leave x unchanged
| t.forward(n) move in the current direction n pixels
| t.backward(n) move in the reverse direction n pixels

| t.pencolor(r, g, b) change the color to the specified RGB value or named color
| t.pencolor(r, g, b) change the color to the specified RGB value or named color

| t.begin_fill(): The starting point is remembered for a filled polygon.
| t.end_fill(): Current fill color is filled after closing the polygon.

| t.dot(): Dot is left at the current position.
| t.stamp(): Impression of turtle shape is left at the current position.
| t.Shape(): Standard shapes are 'turtle', 'classic', 'arrow' or 'circle'.


| t.write(s, font) write a message to the screen you can specify font and size, e.g., "font=('Arial', 8, normal)"

