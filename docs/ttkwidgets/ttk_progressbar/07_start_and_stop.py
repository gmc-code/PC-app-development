# ttk Progressbar - start and stop

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("300x200")
root.title("start and stop")

ttk.Label(root, text="Loading...").pack(pady=10)

loading_bar = ttk.Progressbar(root, length=250, mode="indeterminate")
loading_bar.pack()

ttk.Button(root, text="Start", command=lambda: loading_bar.start(10)).pack(pady=5)
ttk.Button(root, text="Stop", command=loading_bar.stop).pack()

root.mainloop()
