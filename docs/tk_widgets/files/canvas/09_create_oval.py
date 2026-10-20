# tk Canvas - create_oval

import tkinter as tk

root = tk.Tk()
root.geometry("320x240")
root.title("create_oval")

canvas = tk.Canvas(root, width=300, height=200, bg="white")
canvas.pack(pady=10)

canvas.create_oval(20, 50, 180, 150, fill="lightgreen")      # Oval: 160 wide, 100 high
canvas.create_oval(200, 50, 280, 130, fill="red")            # Circle: 80 wide, 80 high

root.mainloop()
