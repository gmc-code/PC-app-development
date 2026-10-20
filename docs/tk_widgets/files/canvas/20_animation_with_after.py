# tk Canvas - Animation with after

import tkinter as tk

speed = 4


def animate():
    global speed
    canvas.move(ball, speed, 0)
    x1, y1, x2, y2 = canvas.coords(ball)
    if x2 >= 300 or x1 <= 0:         # Hit an edge?
        speed = -speed              # Bounce: go the other way
    root.after(20, animate)         # Run again in 20 milliseconds


root = tk.Tk()
root.geometry("320x240")
root.title("Bouncing ball")

canvas = tk.Canvas(root, width=300, height=200, bg="white")
canvas.pack(pady=10)

ball = canvas.create_oval(10, 80, 50, 120, fill="red")

animate()                           # Start the animation

root.mainloop()
