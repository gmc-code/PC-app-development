# ttk Spinbox - Styling a ttk Spinbox

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("300x200")
root.title("Spinbox style")

style = ttk.Style()
style.theme_use("clam")
style.configure("TSpinbox", fieldbackground="lightyellow", foreground="darkgreen",
                arrowcolor="darkgreen", arrowsize=16, padding=5)

level = ttk.Spinbox(root, from_=1, to=10, width=5, font=("Arial", 16))
level.set(1)
level.pack(pady=40)

root.mainloop()
