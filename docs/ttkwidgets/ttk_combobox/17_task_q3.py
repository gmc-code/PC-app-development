# ttk Combobox - Tasks Q3

import tkinter as tk
from tkinter import ttk


def change_colour(event):
    root.config(bg=colour_box.get())


root = tk.Tk()
root.geometry("300x200")
root.title("Colours")

colour_box = ttk.Combobox(root, values=["white", "pink", "orange", "lightgreen",
                                        "skyblue"], state="readonly")
colour_box.set("white")
colour_box.pack(pady=30)
colour_box.bind("<<ComboboxSelected>>", change_colour)

root.mainloop()
