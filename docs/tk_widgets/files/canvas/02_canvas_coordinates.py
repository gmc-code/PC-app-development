# tk Canvas - Canvas coordinates

import tkinter as tk

root = tk.Tk()
root.geometry("320x240")
root.title("Coordinates")

canvas = tk.Canvas(root, width=300, height=200, bg="white")
canvas.pack(pady=10)

canvas.create_text(30, 15, text="(0, 0)")
canvas.create_text(265, 15, text="(300, 0)")
canvas.create_text(30, 185, text="(0, 200)")
canvas.create_text(150, 100, text="(150, 100)")

root.mainloop()
