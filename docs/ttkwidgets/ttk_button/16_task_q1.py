# ttk Button - Tasks Q1

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("300x200")
root.title("ttk Buttons")

click_button = ttk.Button(root, text="Click me", width=15, padding=10)
click_button.pack(pady=20)

root.mainloop()
