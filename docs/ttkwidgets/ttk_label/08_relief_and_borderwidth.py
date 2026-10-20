# ttk Label - relief and borderwidth

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("300x200")
root.title("relief")

ttk.Label(root, text="Border", font=("Arial", 16), relief="solid", borderwidth=2,
          padding=10).pack(pady=40)

root.mainloop()
