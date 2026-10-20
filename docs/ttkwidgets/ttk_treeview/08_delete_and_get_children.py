# ttk Treeview - delete and get_children

import tkinter as tk
from tkinter import ttk


def delete_selected():
    for row_id in table.selection():
        table.delete(row_id)
    update_count()


def clear_all():
    for row_id in table.get_children():
        table.delete(row_id)
    update_count()


def update_count():
    count_label.config(text=f"Rows: {len(table.get_children())}")


root = tk.Tk()
root.geometry("320x280")
root.title("delete")

table = ttk.Treeview(root, columns=("job",), show="headings", height=5)
table.heading("job", text="Job")
for job in ["Feed the dog", "Do homework", "Tidy room", "Practise piano"]:
    table.insert("", tk.END, values=(job,))
table.pack(pady=5)

count_label = ttk.Label(root, text="")
count_label.pack()
update_count()

ttk.Button(root, text="Delete selected", command=delete_selected).pack(pady=2)
ttk.Button(root, text="Clear all", command=clear_all).pack()

root.mainloop()
