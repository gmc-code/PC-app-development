# ttk LabelFrame - relief and borderwidth

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("300x200")
root.title("relief")

warning = ttk.LabelFrame(root, text="Warning", relief="solid", borderwidth=2, padding=10)
warning.pack(pady=30)
ttk.Label(warning, text="Save your work!").pack()

root.mainloop()
