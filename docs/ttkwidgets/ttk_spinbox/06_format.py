# ttk Spinbox - format

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("300x200")
root.title("format")

price = ttk.Spinbox(root, from_=0, to=10, increment=0.5, format="%.2f")
price.set("0.00")
price.pack(pady=10)

minutes = ttk.Spinbox(root, from_=0, to=59, format="%02.0f", wrap=True, width=4)
minutes.set("00")
minutes.pack(pady=10)

root.mainloop()
