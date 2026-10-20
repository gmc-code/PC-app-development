# ttk Button - Changing every button

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("300x200")
root.title("Every button")

style = ttk.Style()
style.theme_use("clam")
style.configure("TButton", font=("Arial", 14), foreground="white",
                background="purple", padding=10)

ttk.Button(root, text="One").pack(pady=5)
ttk.Button(root, text="Two").pack(pady=5)

root.mainloop()
