# ttk Combobox - textvariable

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("300x200")
root.title("textvariable")

pet = tk.StringVar(value="Dog")

ttk.Combobox(root, textvariable=pet, values=["Dog", "Cat", "Fish"],
             state="readonly").pack(pady=20)
ttk.Label(root, textvariable=pet, font=("Arial", 20)).pack()     # Shows the choice

root.mainloop()
