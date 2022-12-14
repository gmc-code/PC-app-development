import turtle as t

t.speed(0)
t.ht()
t.color("red", "yellow")
t.begin_fill()
while True:
    t.forward(200)
    t.left(144)
    if abs(t.pos()) < 1:
        print(t.pos())
        break
t.end_fill()
t.done()
