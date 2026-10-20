# ttk Combobox - justify and foreground

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("300x200")
root.title("justify")

size_box = ttk.Combobox(root, values=["Small", "Medium", "Large"], justify="center",
                        foreground="purple", font=("Arial", 14))
size_box.set("Medium")
size_box.pack(pady=30)

root.mainloop()
