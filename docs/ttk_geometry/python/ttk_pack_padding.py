import tkinter as tk
from tkinter import ttk

root = tk.Tk()

label1 = ttk.Label(root, text="Red")
label1.pack(ipadx=30, ipady=6)

label2 = ttk.Label(root, text="Purple")
label2.pack(pady=20, ipadx=8, ipady=12)

root.mainloop()