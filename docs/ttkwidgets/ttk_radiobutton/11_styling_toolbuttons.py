# ttk Radiobutton - Styling Toolbuttons

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("300x200")
root.title("Toolbutton style")

style = ttk.Style()
style.theme_use("clam")
style.configure("Level.Toolbutton", font=("Arial", 12), padding=8)
style.map("Level.Toolbutton", background=[("selected", "gold")])

level = tk.StringVar(value="Medium")

row = ttk.Frame(root)
row.pack(pady=40)
for choice in ["Easy", "Medium", "Hard"]:
    ttk.Radiobutton(row, text=choice, variable=level, value=choice,
                    style="Level.Toolbutton").pack(side="left", padx=2)

root.mainloop()
