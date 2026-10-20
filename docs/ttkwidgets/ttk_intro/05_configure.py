# ttk widgets and styling - configure

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("300x200")
root.title("configure")

style = ttk.Style()
style.theme_use("clam")
style.configure("TLabel", font=("Arial", 16), foreground="navy")
style.configure("TButton", font=("Arial", 12, "bold"), padding=10)
style.configure("TEntry", fieldbackground="lightyellow")

ttk.Label(root, text="Name:").pack(pady=5)
ttk.Entry(root).pack()
ttk.Button(root, text="Submit").pack(pady=10)

root.mainloop()
