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

# The dictionary that the app changes
# Each key is a fruit and each value is its colour
fruits = {"apple": "red", "banana": "yellow", "grape": "purple"}


def show_dict():
    """Redraws the listbox so it matches the fruits dictionary."""
    item_listbox.delete(0, tk.END)
    for key in fruits:
        item_listbox.insert(tk.END, key + ": " + fruits[key])
    count_label.config(text="Pairs in dictionary: " + str(len(fruits)))


def get_selected_key():
    """Returns the key of the selected line, or None if nothing is selected."""
    selection = item_listbox.curselection()
    if len(selection) == 0:
        message_label.config(text="Select a fruit first.")
        return None
    keys = list(fruits)
    return keys[selection[0]]


def add_pair():
    """Adds a new pair, or changes the value of a key already there."""
    key = key_entry.get().strip().lower()
    value = value_entry.get().strip()
    if key == "" or value == "":
        message_label.config(text="Type a fruit and a colour.")
        return
    if key in fruits:
        message_label.config(text="Changed " + key + " to " + value)
    else:
        message_label.config(text="Added: " + key)
    fruits[key] = value
    key_entry.delete(0, tk.END)
    value_entry.delete(0, tk.END)
    show_dict()


def look_up():
    """Shows the value for the key typed in the key box."""
    key = key_entry.get().strip().lower()
    if key in fruits:
        value_entry.delete(0, tk.END)
        value_entry.insert(0, fruits[key])
        message_label.config(text=key + " is " + fruits[key])
    else:
        message_label.config(text=key + " is not in the dictionary.")


def remove_pair():
    """Removes the selected key and its value from the dictionary."""
    key = get_selected_key()
    if key is None:
        return
    del fruits[key]
    message_label.config(text="Removed: " + key)
    show_dict()


def clear_dict():
    """Removes every key and value from the dictionary."""
    fruits.clear()
    message_label.config(text="Dictionary cleared.")
    show_dict()


def item_clicked(event):
    """Copies the clicked key and value into the entry boxes."""
    selection = item_listbox.curselection()
    if len(selection) > 0:
        key = list(fruits)[selection[0]]
        key_entry.delete(0, tk.END)
        key_entry.insert(0, key)
        value_entry.delete(0, tk.END)
        value_entry.insert(0, fruits[key])


# Create the main window
root = tk.Tk()
root.title("Dictionary editor")
root.geometry("560x520")
root.configure(bg=BG_COLOR)

# Create widgets
title_label = tk.Label(
    root, text="Dictionary Editor",
    bg=BG_COLOR, fg=TITLE_COLOR, font=TITLE_FONT)
instructions_label = tk.Label(
    root, text="Type a fruit and its colour.",
    bg=BG_COLOR, fg=TEXT_COLOR, font=FONT_STYLE)
key_label = tk.Label(
    root, text="Fruit (key)",
    bg=BG_COLOR, fg=TEXT_COLOR, font=FONT_STYLE)
value_label = tk.Label(
    root, text="Colour (value)",
    bg=BG_COLOR, fg=TEXT_COLOR, font=FONT_STYLE)

key_entry = tk.Entry(root, width=14, font=LIST_FONT)
value_entry = tk.Entry(root, width=14, font=LIST_FONT)

# exportselection=False keeps the selected line highlighted
# when the user clicks in an entry box to type
item_listbox = tk.Listbox(
    root, width=20, height=8,
    bg=LIST_BG_COLOR, fg=TEXT_COLOR, font=LIST_FONT,
    exportselection=False)

add_button = tk.Button(
    root, text="Add / Change", width=12,
    bg=PRIMARY_COLOR, fg=BUTTON_FG_COLOR, font=BUTTON_FONT,
    command=add_pair)
look_up_button = tk.Button(
    root, text="Look up", width=12,
    bg=PRIMARY_COLOR, fg=BUTTON_FG_COLOR, font=BUTTON_FONT,
    command=look_up)
remove_button = tk.Button(
    root, text="Remove", width=12,
    bg=SECONDARY_COLOR, fg=BUTTON_FG_COLOR, font=BUTTON_FONT,
    command=remove_pair)
clear_button = tk.Button(
    root, text="Clear", width=12,
    bg=SECONDARY_COLOR, fg=BUTTON_FG_COLOR, font=BUTTON_FONT,
    command=clear_dict)

count_label = tk.Label(
    root, text="",
    bg=BG_COLOR, fg=TEXT_COLOR, font=FONT_STYLE)
message_label = tk.Label(
    root, text="",
    bg=BG_COLOR, fg=PRIMARY_COLOR, font=FONT_STYLE)

# Run item_clicked() whenever the user selects a line in the listbox
item_listbox.bind("<<ListboxSelect>>", item_clicked)

# Share spare width equally between the 2 columns to keep the widgets centred
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)

# Place widgets in the window
title_label.grid(row=0, column=0, columnspan=2, pady=(20, 5))
instructions_label.grid(row=1, column=0, columnspan=2, pady=(0, 10))
key_label.grid(row=2, column=0, padx=10)
value_label.grid(row=2, column=1, padx=10)
key_entry.grid(row=3, column=0, padx=10, pady=5)
value_entry.grid(row=3, column=1, padx=10, pady=5)
item_listbox.grid(row=4, column=0, rowspan=4, padx=10, pady=5)
add_button.grid(row=4, column=1, padx=10, pady=5)
look_up_button.grid(row=5, column=1, padx=10, pady=5)
remove_button.grid(row=6, column=1, padx=10, pady=5)
clear_button.grid(row=7, column=1, padx=10, pady=5)
count_label.grid(row=8, column=0, columnspan=2, pady=(10, 0))
message_label.grid(row=9, column=0, columnspan=2, pady=5)

# Show the starting dictionary
show_dict()

# Start the main event loop
root.mainloop()
