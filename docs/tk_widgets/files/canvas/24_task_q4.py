# tk Canvas - Tasks Q4

import tkinter as tk


def up():
    canvas.move(square, 0, -10)


def down():
    canvas.move(square, 0, 10)


def left():
    canvas.move(square, -10, 0)


def right():
    canvas.move(square, 10, 0)


root = tk.Tk()
root.geometry("320x280")
root.title("Move the square")

canvas = tk.Canvas(root, width=300, height=200, bg="white")
canvas.pack(pady=5)

square = canvas.create_rectangle(130, 80, 170, 120, fill="green")

tk.Button(root, text="Up", command=up).pack(side="left", padx=10)
tk.Button(root, text="Down", command=down).pack(side="left", padx=10)
tk.Button(root, text="Left", command=left).pack(side="left", padx=10)
tk.Button(root, text="Right", command=right).pack(side="left", padx=10)

root.mainloop()
