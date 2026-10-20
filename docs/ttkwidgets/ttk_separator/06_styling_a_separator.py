# ttk Separator - Styling a Separator

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("300x200")
root.title("Separator style")

style = ttk.Style()
style.configure("Red.TSeparator", background="red")
style.configure("Thick.TFrame", background="navy")

ttk.Label(root, text="A red separator").pack(pady=5)
ttk.Separator(root, style="Red.TSeparator").pack(fill="x", padx=20, pady=5)

ttk.Label(root, text="A thick line (a Frame)").pack(pady=5)
ttk.Frame(root, height=6, style="Thick.TFrame").pack(fill="x", padx=20, pady=5)

root.mainloop()
