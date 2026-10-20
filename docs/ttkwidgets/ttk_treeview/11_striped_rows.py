# ttk Treeview - Striped rows

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("320x240")
root.title("Striped rows")

table = ttk.Treeview(root, columns=("day", "temp"), show="headings", height=7)
table.heading("day", text="Day")
table.heading("temp", text="Temperature (°C)")
table.tag_configure("odd", background="aliceblue")
table.tag_configure("even", background="white")

days = [("Mon", 22), ("Tue", 25), ("Wed", 19), ("Thu", 21), ("Fri", 28), ("Sat", 30), ("Sun", 26)]
for number, day in enumerate(days):
    if number % 2 == 0:
        table.insert("", tk.END, values=day, tags=("even",))
    else:
        table.insert("", tk.END, values=day, tags=("odd",))

table.pack(pady=10)

root.mainloop()
