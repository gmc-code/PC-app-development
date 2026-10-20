# ttk Spinbox - Tasks Q1

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("300x200")
root.title("Tickets")

tickets_spinbox = ttk.Spinbox(root, from_=1, to=6)
tickets_spinbox.set(2)
tickets_spinbox.pack(pady=30)

root.mainloop()
