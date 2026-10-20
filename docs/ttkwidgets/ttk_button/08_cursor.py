# ttk Button - cursor

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("300x200")
root.title("cursor")

ttk.Button(root, text="Point at me", cursor="hand2").pack(pady=40)

root.mainloop()
