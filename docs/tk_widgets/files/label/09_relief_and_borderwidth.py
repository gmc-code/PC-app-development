# tk Label - relief and borderwidth

import tkinter as tk

root = tk.Tk()
root.geometry("300x300")
root.title("relief")

for style in ["flat", "solid", "raised", "sunken", "groove", "ridge"]:
    label = tk.Label(root, text=style, width=15, relief=style, borderwidth=3)
    label.pack(pady=5)

root.mainloop()
