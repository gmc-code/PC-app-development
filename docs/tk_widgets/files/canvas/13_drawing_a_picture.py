# tk Canvas - Drawing a picture

import tkinter as tk

root = tk.Tk()
root.geometry("320x240")
root.title("House")

canvas = tk.Canvas(root, width=300, height=200, bg="skyblue")
canvas.pack(pady=10)

canvas.create_rectangle(0, 160, 300, 200, fill="green", outline="")         # Grass
canvas.create_oval(230, 20, 280, 70, fill="yellow", outline="")             # Sun
canvas.create_rectangle(80, 90, 200, 170, fill="tan")                       # House
canvas.create_polygon(70, 90, 140, 40, 210, 90, fill="brown")               # Roof
canvas.create_rectangle(125, 125, 155, 170, fill="maroon")                  # Door

root.mainloop()
