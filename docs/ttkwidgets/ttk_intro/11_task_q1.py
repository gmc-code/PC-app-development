# ttk widgets and styling - Tasks Q1

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("300x200")
root.title("ttk")

ttk.Label(root, text="Hello").pack(pady=10)
ttk.Button(root, text="OK").pack()

root.mainloop()
