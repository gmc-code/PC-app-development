# ttk Sizegrip - Tasks Q1

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("300x200")
root.title("Resize me")

ttk.Sizegrip(root).pack(side="bottom", anchor="se")

root.mainloop()
