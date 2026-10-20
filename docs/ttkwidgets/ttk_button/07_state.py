# ttk Button - state

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("300x200")
root.title("state")

ttk.Button(root, text="I work").pack(pady=10)
ttk.Button(root, text="I am turned off", state="disabled").pack(pady=10)

root.mainloop()
