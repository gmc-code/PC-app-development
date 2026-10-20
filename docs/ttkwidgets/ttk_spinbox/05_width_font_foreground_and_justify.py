# ttk Spinbox - width, font, foreground and justify

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("300x200")
root.title("width and font")

score_spinbox = ttk.Spinbox(root, from_=0, to=99, width=4, font=("Arial", 24),
                            foreground="navy", justify="center")
score_spinbox.set(0)
score_spinbox.pack(pady=30)

root.mainloop()
