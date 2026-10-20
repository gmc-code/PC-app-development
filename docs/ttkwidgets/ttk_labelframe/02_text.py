# ttk LabelFrame - text

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("300x200")
root.title("text")

settings = ttk.LabelFrame(root, text="Settings", padding=10)
settings.pack(pady=20)

sound = tk.IntVar()
ttk.Checkbutton(settings, text="Sound on", variable=sound).pack()

root.mainloop()
