# ttk Scale - set

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("300x200")
root.title("set")

volume_scale = ttk.Scale(root, from_=0, to=100, length=250)
volume_scale.pack(pady=20)

for amount in [0, 50, 100]:
    ttk.Button(root, text=f"Set to {amount}",
               command=lambda amount=amount: volume_scale.set(amount)).pack(pady=2)

root.mainloop()
