# ttk Treeview - height

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("320x200")
root.title("height")

table = ttk.Treeview(root, columns=("number", "square"), show="headings", height=5)
table.heading("number", text="Number")
table.heading("square", text="Square")

for number in range(1, 21):
    table.insert("", tk.END, values=(number, number * number))

table.pack(pady=10)

root.mainloop()
