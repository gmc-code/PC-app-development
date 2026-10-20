# tk Listbox - Tasks Q3

import tkinter as tk


def add():
    name_list.insert(tk.END, name_entry.get())


root = tk.Tk()
root.geometry("300x300")
root.title("Names")

name_entry = tk.Entry(root)
name_entry.pack(pady=5)

add_button = tk.Button(root, text="Add", command=add)
add_button.pack()

name_list = tk.Listbox(root, height=8)
name_list.pack(pady=5)

root.mainloop()
