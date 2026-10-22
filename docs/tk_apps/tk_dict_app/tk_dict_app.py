# List Editor
# A Tkinter app that adds, changes, removes and sorts items in a Python list.

import tkinter as tk

# The list that the app modifies
items = ["apple", "banana", "cherry"]


def show_list():
    """Redraw the listbox so it matches the items list."""
    listbox.delete(0, tk.END)
    for item in items:
        listbox.insert(tk.END, item)
    count_label.config(text="Items in list: " + str(len(items)))


def get_selected_index():
    """Return the position of the selected item, or None if nothing is selected."""
    selection = listbox.curselection()
    if len(selection) == 0:
        message_label.config(text="Select an item first.")
        return None
    return selection[0]


def add_item():
    """Add the text in the entry box to the end of the list."""
    new_item = entry.get().strip()
    if new_item == "":
        message_label.config(text="Type something to add.")
        return
    items.append(new_item)
    entry.delete(0, tk.END)
    message_label.config(text="Added: " + new_item)
    show_list()


def change_item():
    """Replace the selected item with the text in the entry box."""
    index = get_selected_index()
    if index is None:
        return
    new_item = entry.get().strip()
    if new_item == "":
        message_label.config(text="Type the new value first.")
        return
    old_item = items[index]
    items[index] = new_item
    entry.delete(0, tk.END)
    message_label.config(text="Changed " + old_item + " to " + new_item)
    show_list()


def remove_item():
    """Remove the selected item from the list."""
    index = get_selected_index()
    if index is None:
        return
    removed = items.pop(index)
    message_label.config(text="Removed: " + removed)
    show_list()


def sort_items():
    """Sort the list into alphabetical order."""
    items.sort()
    message_label.config(text="List sorted A to Z.")
    show_list()


def clear_items():
    """Remove every item from the list."""
    items.clear()
    message_label.config(text="List cleared.")
    show_list()


def item_clicked(event):
    """When an item is clicked, copy it into the entry box so it can be changed."""
    selection = listbox.curselection()
    if len(selection) > 0:
        entry.delete(0, tk.END)
        entry.insert(0, items[selection[0]])


# ---------- Build the window ----------
window = tk.Tk()
window.title("List Editor")

title_label = tk.Label(window, text="List Editor", font=("Arial", 16, "bold"))
title_label.grid(row=0, column=0, columnspan=3, pady=10)

entry = tk.Entry(window, width=25, font=("Arial", 12))
entry.grid(row=1, column=0, columnspan=2, padx=10, pady=5)

add_button = tk.Button(window, text="Add", width=10, command=add_item)
add_button.grid(row=1, column=2, padx=10, pady=5)

# exportselection=False keeps the selected item highlighted
# even when you click in the entry box to type
listbox = tk.Listbox(window, width=30, height=10, font=("Arial", 12),
                     exportselection=False)
listbox.grid(row=2, column=0, columnspan=2, rowspan=4, padx=10, pady=5)
listbox.bind("<<ListboxSelect>>", item_clicked)

change_button = tk.Button(window, text="Change", width=10, command=change_item)
change_button.grid(row=2, column=2, padx=10)

remove_button = tk.Button(window, text="Remove", width=10, command=remove_item)
remove_button.grid(row=3, column=2, padx=10)

sort_button = tk.Button(window, text="Sort", width=10, command=sort_items)
sort_button.grid(row=4, column=2, padx=10)

clear_button = tk.Button(window, text="Clear", width=10, command=clear_items)
clear_button.grid(row=5, column=2, padx=10)

count_label = tk.Label(window, text="")
count_label.grid(row=6, column=0, columnspan=3)

message_label = tk.Label(window, text="", fg="blue")
message_label.grid(row=7, column=0, columnspan=3, pady=5)

show_list()
window.mainloop()