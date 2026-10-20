# tk Canvas - Tasks Q1

import tkinter as tk

root = tk.Tk()
root.geometry("320x240")
root.title("Drawing")

canvas = tk.Canvas(root, width=300, height=200, bg="white")
canvas.pack(pady=10)

canvas.create_line(0, 0, 300, 200, fill="red")

root.mainloop()
