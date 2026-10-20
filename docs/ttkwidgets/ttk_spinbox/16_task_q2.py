# ttk Spinbox - Tasks Q2

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("300x200")
root.title("Tickets")

tickets_spinbox = ttk.Spinbox(root, from_=1, to=6, state="readonly",
                              font=("Arial", 20), width=4)
tickets_spinbox.set(2)
tickets_spinbox.pack(pady=30)

root.mainloop()
