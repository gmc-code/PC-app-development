# ttk Combobox - width and font

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("300x200")
root.title("width and font")

country_box = ttk.Combobox(root, values=["Australia", "New Zealand", "Fiji"],
                           width=20, font=("Arial", 14))
country_box.set("Australia")
country_box.pack(pady=30)

root.mainloop()
