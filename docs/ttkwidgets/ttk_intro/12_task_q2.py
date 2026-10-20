# ttk widgets and styling - Tasks Q2

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("300x200")
root.title("ttk")

style = ttk.Style()
style.theme_use("clam")
style.configure("TButton", foreground="white", background="orange",
                font=("Arial", 14))

ttk.Label(root, text="Hello").pack(pady=10)
ttk.Button(root, text="OK").pack()

root.mainloop()
