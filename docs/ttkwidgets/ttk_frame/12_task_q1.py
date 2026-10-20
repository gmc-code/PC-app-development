# ttk Frame - Tasks Q1

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("300x200")
root.title("Frames")

box = ttk.Frame(root, padding=20, relief="solid", borderwidth=1)
box.pack(pady=20)
ttk.Label(box, text="Hello").pack()

root.mainloop()
