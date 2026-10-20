# ttk widgets and styling - Making your own style

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("300x220")
root.title("Custom styles")

style = ttk.Style()
style.theme_use("clam")
style.configure("TButton", font=("Arial", 12), padding=8)          # Every button
style.configure("Go.TButton", foreground="white", background="green")
style.configure("Danger.TButton", foreground="white", background="red")

ttk.Button(root, text="Normal").pack(pady=5)
ttk.Button(root, text="Start", style="Go.TButton").pack(pady=5)
ttk.Button(root, text="Delete", style="Danger.TButton").pack(pady=5)

root.mainloop()
