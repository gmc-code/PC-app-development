# ttk Frame - relief and borderwidth

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("300x250")
root.title("relief")

for style_name in ["solid", "raised", "sunken", "groove"]:
    frame = ttk.Frame(root, relief=style_name, borderwidth=3, padding=5)
    frame.pack(pady=4)
    ttk.Label(frame, text=style_name, width=12).pack()

root.mainloop()
