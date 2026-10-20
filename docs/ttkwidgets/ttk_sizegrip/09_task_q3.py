# ttk Sizegrip - Tasks Q3

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("300x200")
root.title("Resize me")
root.minsize(200, 120)

ttk.Sizegrip(root).pack(side="bottom", anchor="se")

text_box = tk.Text(root)
text_box.pack(fill="both", expand=True)

root.mainloop()
