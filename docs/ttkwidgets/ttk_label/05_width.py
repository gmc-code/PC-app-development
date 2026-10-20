# ttk Label - width

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("300x200")
root.title("width")

ttk.Label(root, text="Wide label", width=25, background="lightblue").pack(pady=40)

root.mainloop()
