# ttk Separator - Tasks Q3

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("300x200")
root.title("Side by side")

ttk.Label(root, text="Cats").pack(side="left", padx=40)
ttk.Separator(root, orient="vertical").pack(side="left", fill="y", pady=20)
ttk.Label(root, text="Dogs").pack(side="left", padx=40)

root.mainloop()
