# ttk Separator - With grid

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("300x200")
root.title("grid")

ttk.Label(root, text="Name").grid(row=0, column=0, padx=10, pady=5)
ttk.Label(root, text="Score").grid(row=0, column=1, padx=10, pady=5)

ttk.Separator(root).grid(row=1, column=0, columnspan=2, sticky="ew")

ttk.Label(root, text="Ava").grid(row=2, column=0, pady=2)
ttk.Label(root, text="95").grid(row=2, column=1, pady=2)
ttk.Label(root, text="Ben").grid(row=3, column=0, pady=2)
ttk.Label(root, text="88").grid(row=3, column=1, pady=2)

root.mainloop()
