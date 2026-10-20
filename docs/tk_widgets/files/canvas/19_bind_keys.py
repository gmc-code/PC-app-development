# tk Canvas - bind (keys)

import tkinter as tk


def left(event):
    canvas.move(player, -10, 0)


def right(event):
    canvas.move(player, 10, 0)


def up(event):
    canvas.move(player, 0, -10)


def down(event):
    canvas.move(player, 0, 10)


root = tk.Tk()
root.geometry("320x240")
root.title("Arrow keys")

canvas = tk.Canvas(root, width=300, height=200, bg="lightgreen")
canvas.pack(pady=10)

player = canvas.create_rectangle(140, 90, 160, 110, fill="blue")

root.bind("<Left>", left)
root.bind("<Right>", right)
root.bind("<Up>", up)
root.bind("<Down>", down)

root.mainloop()
