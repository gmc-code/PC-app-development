# ttk widgets and styling - Tasks Q4

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("300x200")
root.title("ttk")

style = ttk.Style()
style.theme_use("clam")
style.configure("TButton", foreground="white", background="orange",
                font=("Arial", 14))
style.map("TButton", background=[("active", "red")])

ttk.Button(root, text="OK").pack(pady=10)
ttk.Button(root, text="Cancel").pack()

root.mainloop()
