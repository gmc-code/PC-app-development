# ttk Entry - Styling a ttk Entry

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("300x200")
root.title("Entry style")

style = ttk.Style()
style.theme_use("clam")
style.configure("TEntry", fieldbackground="lightyellow", foreground="navy", padding=5)
style.configure("Wrong.TEntry", fieldbackground="mistyrose")

ttk.Entry(root, font=("Arial", 14)).pack(pady=10)
ttk.Entry(root, font=("Arial", 14), style="Wrong.TEntry").pack(pady=10)

root.mainloop()
