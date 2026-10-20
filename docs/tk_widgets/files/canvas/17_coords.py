# tk Canvas - coords

import tkinter as tk


def where():
    x1, y1, x2, y2 = canvas.coords(box)
    result_label.config(text=f"Top-left corner is at ({x1}, {y1})")


def move():
    canvas.move(box, 15, 10)


def home():
    canvas.coords(box, 10, 10, 60, 60)      # Back to the start


root = tk.Tk()
root.geometry("320x300")
root.title("coords")

canvas = tk.Canvas(root, width=300, height=200, bg="white")
canvas.pack(pady=5)

box = canvas.create_rectangle(10, 10, 60, 60, fill="orange")

button_row = tk.Frame(root)
button_row.pack()
tk.Button(button_row, text="Move", command=move).pack(side="left", padx=5)
tk.Button(button_row, text="Where?", command=where).pack(side="left", padx=5)
tk.Button(button_row, text="Home", command=home).pack(side="left", padx=5)

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
