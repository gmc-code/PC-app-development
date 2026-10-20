# ttk Button - Tasks Q4

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("300x200")
root.title("Delete")

style = ttk.Style()
style.theme_use("clam")
style.configure("Danger.TButton", foreground="white", background="red")
style.map("Danger.TButton", background=[("pressed", "darkred")])

ttk.Button(root, text="Delete", style="Danger.TButton").pack(pady=10)
ttk.Button(root, text="Cancel").pack()

root.mainloop()
