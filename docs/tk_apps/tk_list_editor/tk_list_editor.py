import tkinter as tk

# Constants
BG_COLOR = "#ffffff"
TITLE_COLOR = "#212121"
TEXT_COLOR = "#444444"
PRIMARY_COLOR = "#2196f3"  # blue
SECONDARY_COLOR = "#e91e63"  # pink
BUTTON_FG_COLOR = "#ffffff"
LIST_BG_COLOR = "#f5f5f5"
TITLE_FONT = ("Arial", 28, "bold")
FONT_STYLE = ("Arial", 14)
BUTTON_FONT = ("Arial", 14)
LIST_FONT = ("Arial", 16)

# The list that the app changes
items = ["apple", "banana", "cherry"]


def show_list():
    """Redraws the listbox so it matches the items list."""
    item_listbox.delete(0, tk.END)
    for item in items:
        item_listbox.insert(tk.END, item)
    count_label.config(text="Items in list: " + str(len(items)))


def get_selected_index():
    """Returns the selected index, or None if nothing is selected."""
    selection = item_listbox.curselection()
    if len(selection) == 0:
        message_label.config(text="Select an item first.")
        return None
    return selection[0]


def add_item():
    """Adds the text in the entry box to the end of the list."""
    new_item = item_entry.get().strip()
    if new_item == "":
        message_label.config(text="Type something to add.")
        return
    items.append(new_item)
    item_entry.delete(0, tk.END)
    message_label.config(text="Added: " + new_item)
    show_list()


def change_item():
    """Replaces the selected item with the text in the entry box."""
    index = get_selected_index()
    if index is None:
        return
    new_item = item_entry.get().strip()
    if new_item == "":
        message_label.config(text="Type the new value first.")
        return
    old_item = items[index]
    items[index] = new_item
    item_entry.delete(0, tk.END)
    message_label.config(text="Changed " + old_item + " to " + new_item)
    show_list()


def remove_item():
    """Removes the selected item from the list."""
    index = get_selected_index()
    if index is None:
        return
    removed = items.pop(index)
    message_label.config(text="Removed: " + removed)
    show_list()


def sort_items():
    """Sorts the list into alphabetical order."""
    items.sort()
    message_label.config(text="List sorted A to Z.")
    show_list()


def clear_items():
    """Removes every item from the list."""
    items.clear()
    message_label.config(text="List cleared.")
    show_list()


def item_clicked(event):
    """Copies the clicked item into the entry box so it can be changed."""
    selection = item_listbox.curselection()
    if len(selection) > 0:
        item_entry.delete(0, tk.END)
        item_entry.insert(0, items[selection[0]])


# Create the main window
root = tk.Tk()
root.title("List editor")
root.geometry("520x480")
root.configure(bg=BG_COLOR)

# Create widgets
title_label = tk.Label(
    root, text="List Editor",
    bg=BG_COLOR, fg=TITLE_COLOR, font=TITLE_FONT)
instructions_label = tk.Label(
    root, text="Type an item or click one below.",
    bg=BG_COLOR, fg=TEXT_COLOR, font=FONT_STYLE)

item_entry = tk.Entry(root, width=20, font=LIST_FONT)

# exportselection=False keeps the selected item highlighted
# when the user clicks in the entry box to type
item_listbox = tk.Listbox(
    root, width=20, height=8,
    bg=LIST_BG_COLOR, fg=TEXT_COLOR, font=LIST_FONT,
    exportselection=False)

add_button = tk.Button(
    root, text="Add", width=8,
    bg=PRIMARY_COLOR, fg=BUTTON_FG_COLOR, font=BUTTON_FONT,
    command=add_item)
change_button = tk.Button(
    root, text="Change", width=8,
    bg=PRIMARY_COLOR, fg=BUTTON_FG_COLOR, font=BUTTON_FONT,
    command=change_item)
remove_button = tk.Button(
    root, text="Remove", width=8,
    bg=SECONDARY_COLOR, fg=BUTTON_FG_COLOR, font=BUTTON_FONT,
    command=remove_item)
sort_button = tk.Button(
    root, text="Sort", width=8,
    bg=PRIMARY_COLOR, fg=BUTTON_FG_COLOR, font=BUTTON_FONT,
    command=sort_items)
clear_button = tk.Button(
    root, text="Clear", width=8,
    bg=SECONDARY_COLOR, fg=BUTTON_FG_COLOR, font=BUTTON_FONT,
    command=clear_items)

count_label = tk.Label(
    root, text="",
    bg=BG_COLOR, fg=TEXT_COLOR, font=FONT_STYLE)
message_label = tk.Label(
    root, text="",
    bg=BG_COLOR, fg=PRIMARY_COLOR, font=FONT_STYLE)

# Run item_clicked() whenever the user selects an item in the listbox
item_listbox.bind("<<ListboxSelect>>", item_clicked)

# Share spare width equally between the 2 columns to keep the widgets centred
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)

# Place widgets in the window
title_label.grid(row=0, column=0, columnspan=2, pady=(20, 5))
instructions_label.grid(row=1, column=0, columnspan=2, pady=(0, 10))
item_entry.grid(row=2, column=0, padx=10, pady=5)
add_button.grid(row=2, column=1, padx=10, pady=5)
item_listbox.grid(row=3, column=0, rowspan=4, padx=10, pady=5)
change_button.grid(row=3, column=1, padx=10, pady=5)
remove_button.grid(row=4, column=1, padx=10, pady=5)
sort_button.grid(row=5, column=1, padx=10, pady=5)
clear_button.grid(row=6, column=1, padx=10, pady=5)
count_label.grid(row=7, column=0, columnspan=2, pady=(10, 0))
message_label.grid(row=8, column=0, columnspan=2, pady=5)

# Show the starting list
show_list()

# Start the main event loop
root.mainloop()
