# tk Canvas - move

import tkinter as tk


def move_right():
    canvas.move(ball, 20, 0)


def move_down():
    canvas.move(ball, 0, 20)


root = tk.Tk()
root.geometry("320x280")
root.title("move")

canvas = tk.Canvas(root, width=300, height=200, bg="white")
canvas.pack(pady=5)

ball = canvas.create_oval(10, 10, 50, 50, fill="red")

tk.Button(root, text="Right", command=move_right).pack(side="left", padx=40)
tk.Button(root, text="Down", command=move_down).pack(side="left")

root.mainloop()
