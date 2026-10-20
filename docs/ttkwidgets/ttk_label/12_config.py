# ttk Label - config

import tkinter as tk
from tkinter import ttk


def change():
    result_label.config(text="Changed!", foreground="white", background="green")


root = tk.Tk()
root.geometry("300x200")
root.title("config")

result_label = ttk.Label(root, text="Not changed yet", font=("Arial", 16), padding=5)
result_label.pack(pady=20)

ttk.Button(root, text="Change", command=change).pack()

root.mainloop()
