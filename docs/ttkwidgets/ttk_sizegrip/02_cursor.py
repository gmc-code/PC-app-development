# ttk Sizegrip - cursor

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("300x200")
root.title("cursor")

ttk.Sizegrip(root, cursor="sizing").pack(side="bottom", anchor="se")
ttk.Label(root, text="Point at the corner").pack(pady=60)

root.mainloop()
