# ttk LabelFrame - Tasks Q2

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("300x200")
root.title("Profile")

about = ttk.LabelFrame(root, text="About you", padding=10, labelanchor="n")
about.pack(pady=20)
ttk.Label(about, text="Name:").pack()
ttk.Entry(about).pack()

root.mainloop()
