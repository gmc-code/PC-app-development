# ttk Button - Colours for hover and press

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("300x200")
root.title("map")

style = ttk.Style()
style.theme_use("clam")
style.configure("TButton", font=("Arial", 14), foreground="white", background="teal")
style.map("TButton",
          background=[("pressed", "darkslategray"), ("active", "mediumturquoise")],
          foreground=[("disabled", "gray")])

ttk.Button(root, text="Hover and press me").pack(pady=20)
ttk.Button(root, text="Turned off", state="disabled").pack()

root.mainloop()
