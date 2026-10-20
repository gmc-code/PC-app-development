# tk Canvas - bind (mouse clicks)

import tkinter as tk


def draw_dot(event):
    x = event.x
    y = event.y
    canvas.create_oval(x - 3, y - 3, x + 3, y + 3, fill="blue", outline="")


root = tk.Tk()
root.geometry("320x240")
root.title("Paint")

canvas = tk.Canvas(root, width=300, height=200, bg="white", cursor="pencil")
canvas.pack(pady=10)

canvas.bind("<Button-1>", draw_dot)     # Click to draw a dot
canvas.bind("<B1-Motion>", draw_dot)    # Drag to draw a line of dots

root.mainloop()
