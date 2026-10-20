# ttk Frame - width and height

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("300x200")
root.title("width and height")

empty = ttk.Frame(root, width=200, height=100, relief="solid", borderwidth=2)
empty.pack(pady=40)

root.mainloop()
