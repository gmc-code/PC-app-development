# ttk widgets and styling - map

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("300x200")
root.title("map")

style = ttk.Style()
style.theme_use("clam")
style.configure("Fancy.TButton", font=("Arial", 14), foreground="white", background="blue")
style.map("Fancy.TButton",
          background=[("pressed", "navy"), ("active", "deepskyblue")],
          foreground=[("pressed", "yellow")])

ttk.Button(root, text="Hover, then press", style="Fancy.TButton").pack(pady=60)

root.mainloop()
