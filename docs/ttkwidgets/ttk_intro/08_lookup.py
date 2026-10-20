# ttk widgets and styling - lookup

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("300x200")
root.title("lookup")

style = ttk.Style()
style.configure("Big.TLabel", font=("Arial", 24))

font_used = style.lookup("Big.TLabel", "font")
ttk.Label(root, text="Big text", style="Big.TLabel").pack(pady=20)
ttk.Label(root, text="The font is: " + str(font_used)).pack()

root.mainloop()
