# ttk Label - Tasks Q2

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("300x200")
root.title("About me")

ttk.Label(root, text="Sam", font=("Arial", 24), foreground="white",
          background="purple").pack(pady=10)
ttk.Label(root, text="Pizza", relief="solid", borderwidth=2,
          padding=10).pack()

root.mainloop()
