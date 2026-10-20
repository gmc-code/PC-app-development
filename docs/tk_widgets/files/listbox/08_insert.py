# tk Listbox - insert

import tkinter as tk


def add_item():
    shopping_list.insert(tk.END, item_entry.get())     # Add what was typed
    item_entry.delete(0, tk.END)                        # Clear the entry


root = tk.Tk()
root.geometry("300x300")
root.title("insert")

item_entry = tk.Entry(root)
item_entry.pack(pady=5)

add_button = tk.Button(root, text="Add to list", command=add_item)
add_button.pack()

shopping_list = tk.Listbox(root, height=8)
shopping_list.pack(pady=5)

root.mainloop()
