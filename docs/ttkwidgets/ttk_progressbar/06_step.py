# ttk Progressbar - step

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("300x200")
root.title("step")

bar = ttk.Progressbar(root, length=250)
bar.pack(pady=30)

ttk.Button(root, text="Add 10", command=lambda: bar.step(10)).pack()

root.mainloop()
