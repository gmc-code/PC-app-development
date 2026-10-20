# ttk Frame - Tasks Q3

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("300x200")
root.title("Frames")

style = ttk.Style()
style.configure("Pink.TFrame", background="pink")

pink_box = ttk.Frame(root, width=200, height=100, style="Pink.TFrame")
pink_box.pack(pady=40)

root.mainloop()
