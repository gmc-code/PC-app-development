# tk Canvas - Tasks Q3

import tkinter as tk

root = tk.Tk()
root.geometry("320x340")
root.title("Snowman")

canvas = tk.Canvas(root, width=300, height=300, bg="lightblue")
canvas.pack(pady=10)

canvas.create_oval(90, 170, 210, 290, fill="white")      # Bottom
canvas.create_oval(110, 95, 190, 175, fill="white")      # Middle
canvas.create_oval(120, 40, 180, 100, fill="white")      # Head
canvas.create_polygon(150, 65, 150, 75, 175, 70, fill="orange")  # Nose

root.mainloop()
