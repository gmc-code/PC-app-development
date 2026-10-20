# ttk widgets and styling - Tasks Q3

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("300x200")
root.title("ttk")

style = ttk.Style()
style.configure("Big.TLabel", font=("Arial", 30))

ttk.Label(root, text="Big", style="Big.TLabel").pack(pady=10)
ttk.Label(root, text="Normal").pack()

root.mainloop()
