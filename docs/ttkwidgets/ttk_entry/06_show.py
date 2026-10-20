# ttk Entry - show

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("300x200")
root.title("show")

ttk.Label(root, text="Password:").pack(pady=5)
ttk.Entry(root, show="*", font=("Arial", 14)).pack()

root.mainloop()
