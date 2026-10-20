# ttk Frame - style (colour)

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("300x200")
root.title("Frame colour")

style = ttk.Style()
style.configure("Blue.TFrame", background="lightblue")
style.configure("Blue.TLabel", background="lightblue")      # Label to match

blue_box = ttk.Frame(root, style="Blue.TFrame", padding=20)
blue_box.pack(pady=40)
ttk.Label(blue_box, text="A blue frame", style="Blue.TLabel").pack()

root.mainloop()
