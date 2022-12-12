import turtle as t

t.speed(0)
t.color("red", "yellow")
t.begin_fill()
while True:
    t.forward(100)
    t.left(70)
    if abs(t.pos()) < 1:
        break
t.end_fill()
t.done()
