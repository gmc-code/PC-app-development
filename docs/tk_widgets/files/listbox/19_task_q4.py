# tk Listbox - Tasks Q4

import tkinter as tk


def add():
    name_list.insert(tk.END, name_entry.get())


def remove():
    chosen = name_list.curselection()
    if chosen:
        name_list.delete(chosen[0])


root = tk.Tk()
root.geometry("300x320")
root.title("Names")

name_entry = tk.Entry(root)
name_entry.pack(pady=5)

add_button = tk.Button(root, text="Add", command=add)
add_button.pack()

name_list = tk.Listbox(root, height=8)
name_list.pack(pady=5)

remove_button = tk.Button(root, text="Remove", command=remove)
remove_button.pack()

root.mainloop()
