# ttk Radiobutton - Tasks Q1

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("300x200")
root.title("Transport")

transport = tk.StringVar(value="Walk")

for choice in ["Bus", "Car", "Walk"]:
    ttk.Radiobutton(root, text=choice, variable=transport, value=choice).pack()

root.mainloop()
