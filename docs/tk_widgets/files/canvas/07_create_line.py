# tk Canvas - create_line

import tkinter as tk

root = tk.Tk()
root.geometry("320x240")
root.title("create_line")

canvas = tk.Canvas(root, width=300, height=200, bg="white")
canvas.pack(pady=10)

canvas.create_line(20, 30, 280, 30)                                     # Thin black line
canvas.create_line(20, 70, 280, 70, fill="red", width=5)                # Thick red line
canvas.create_line(20, 110, 280, 110, fill="blue", width=3, arrow="last")   # Arrow
canvas.create_line(20, 180, 80, 140, 140, 180, 200, 140, 260, 180,
                   fill="green", width=3)                               # Zig-zag

root.mainloop()
