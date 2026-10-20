# ttk Button - width

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("300x200")
root.title("width")

ttk.Button(root, text="Yes", width=15).pack(pady=5)
ttk.Button(root, text="No", width=15).pack(pady=5)
ttk.Button(root, text="Maybe", width=15).pack(pady=5)

root.mainloop()
