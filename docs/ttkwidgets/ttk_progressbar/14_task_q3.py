# ttk Progressbar - Tasks Q3

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("300x200")
root.title("Busy")

busy_bar = ttk.Progressbar(root, length=250, mode="indeterminate")
busy_bar.pack(pady=20)

ttk.Button(root, text="Start", command=lambda: busy_bar.start(10)).pack(pady=2)
ttk.Button(root, text="Stop", command=busy_bar.stop).pack()

root.mainloop()
