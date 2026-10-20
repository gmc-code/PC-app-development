# ttk Progressbar - maximum and value

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("300x200")
root.title("maximum and value")

ttk.Label(root, text="Quiz score: 7 out of 10").pack(pady=10)
ttk.Progressbar(root, length=250, maximum=10, value=7).pack()

ttk.Label(root, text="Download: 25 out of 100").pack(pady=10)
ttk.Progressbar(root, length=250, value=25).pack()

root.mainloop()
