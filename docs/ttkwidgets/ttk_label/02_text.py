# ttk Label - text

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("300x200")
root.title("text")

ttk.Label(root, text="Line one\nLine two").pack(pady=20)

root.mainloop()
