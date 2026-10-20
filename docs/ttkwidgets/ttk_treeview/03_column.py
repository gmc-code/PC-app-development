# ttk Treeview - column

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("350x200")
root.title("heading and column")

table = ttk.Treeview(root, columns=("name", "year", "house"), show="headings", height=4)

table.heading("name", text="Name", anchor="w")
table.heading("year", text="Year", anchor="center")
table.heading("house", text="House", anchor="center")

table.column("name", width=150, anchor="w")
table.column("year", width=60, anchor="center")
table.column("house", width=100, anchor="center")

students = [("Ava Smith", 7, "Red"), ("Ben Lee", 8, "Blue"), ("Chloe Ng", 7, "Gold")]
for student in students:
    table.insert("", tk.END, values=student)

table.pack(pady=10)

root.mainloop()
