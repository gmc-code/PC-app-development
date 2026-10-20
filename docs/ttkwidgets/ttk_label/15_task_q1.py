# ttk Label - Tasks Q1

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("300x200")
root.title("About me")

ttk.Label(root, text="Sam", font=("Arial", 24), foreground="white",
          background="purple").pack(pady=10)

root.mainloop()
