# ttk Combobox - state

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("300x200")
root.title("state")

ttk.Label(root, text="Type or pick:").pack()
any_box = ttk.Combobox(root, values=["Red", "Green", "Blue"])
any_box.pack(pady=5)

ttk.Label(root, text="Pick only:").pack()
pick_box = ttk.Combobox(root, values=["Red", "Green", "Blue"], state="readonly")
pick_box.set("Red")
pick_box.pack(pady=5)

root.mainloop()
