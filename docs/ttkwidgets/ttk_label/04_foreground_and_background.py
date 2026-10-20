# ttk Label - foreground and background

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("300x200")
root.title("foreground and background")

ttk.Label(root, text="Blue on yellow", font=("Arial", 18),
          foreground="blue", background="yellow").pack(pady=40)

root.mainloop()
