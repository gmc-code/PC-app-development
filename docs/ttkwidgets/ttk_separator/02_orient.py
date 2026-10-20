# ttk Separator - orient

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("300x200")
root.title("Vertical separator")

ttk.Label(root, text="Left side").pack(side="left", padx=30)

ttk.Separator(root, orient="vertical").pack(side="left", fill="y", pady=20)

ttk.Label(root, text="Right side").pack(side="left", padx=30)

root.mainloop()
