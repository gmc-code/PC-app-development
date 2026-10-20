# ttk Scrollbar - With a Canvas

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("300x200")
root.title("Canvas")

scrollbar = ttk.Scrollbar(root)
scrollbar.pack(side="right", fill="y")

canvas = tk.Canvas(root, bg="white", scrollregion=(0, 0, 300, 1000),
                   yscrollcommand=scrollbar.set)
canvas.pack(side="left", fill="both", expand=True)
scrollbar.config(command=canvas.yview)

for y in range(0, 1000, 100):
    canvas.create_text(120, y + 50, text=f"{y} pixels down", font=("Arial", 14))

root.mainloop()
