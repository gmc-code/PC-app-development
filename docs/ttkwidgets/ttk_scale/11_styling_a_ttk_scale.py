# ttk Scale - Styling a ttk Scale

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("300x200")
root.title("Scale style")

style = ttk.Style()
style.theme_use("clam")
style.configure("Horizontal.TScale", troughcolor="lightyellow", background="orange",
                sliderlength=40)
style.configure("Blue.Horizontal.TScale", troughcolor="lightblue", background="navy")

ttk.Scale(root, from_=0, to=100, length=250).pack(pady=20)
ttk.Scale(root, from_=0, to=100, length=250, style="Blue.Horizontal.TScale").pack()

root.mainloop()
