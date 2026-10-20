# ttk Button - Changing some buttons

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("300x200")
root.title("Some buttons")

style = ttk.Style()
style.theme_use("clam")
style.configure("Go.TButton", foreground="white", background="green", font=("Arial", 14))
style.configure("Stop.TButton", foreground="white", background="red", font=("Arial", 14))

ttk.Button(root, text="GO", style="Go.TButton").pack(pady=5)
ttk.Button(root, text="STOP", style="Stop.TButton").pack(pady=5)
ttk.Button(root, text="Normal button").pack(pady=5)

root.mainloop()
