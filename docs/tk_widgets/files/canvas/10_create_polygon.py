# tk Canvas - create_polygon

import tkinter as tk

root = tk.Tk()
root.geometry("320x240")
root.title("create_polygon")

canvas = tk.Canvas(root, width=300, height=200, bg="white")
canvas.pack(pady=10)

canvas.create_polygon(60, 20, 110, 120, 10, 120, fill="purple")                 # Triangle
canvas.create_polygon(150, 120, 200, 40, 250, 120, 200, 180, fill="gold",
                      outline="black", width=2)                                 # Diamond

root.mainloop()
