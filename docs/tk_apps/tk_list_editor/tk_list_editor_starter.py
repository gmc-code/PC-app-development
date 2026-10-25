# List editor - starter file
#
# Work through the worksheet in order:
#   Step 3      fill in the items list
#   Step 4      add the missing options to each widget (title_label is done)
#   Step 5      run the program to check the layout
#   Steps 6-8   replace each "pass" with the function's code
#   Step 9      add command= to each button
#
# The program runs straight away: the widgets are there in their simplest
# form and each function only has "pass". The buttons do nothing until Steps 6-9.

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
# Step 3: add "apple", "banana" and "cherry"
items = []


def show_list():
    """Redraws the listbox so it matches the items list."""
    # Step 6
    pass


def get_selected_index():
    """Returns the selected index, or None if nothing is selected."""
    # Step 7
    pass


def add_item():
    """Adds the text in the entry box to the end of the list."""
    # Step 7
    pass


def change_item():
    """Replaces the selected item with the text in the entry box."""
    # Step 7
    pass


def remove_item():
    """Removes the selected item from the list."""
    # Step 7
    pass


def sort_items():
    """Sorts the list into alphabetical order."""
    # Step 8
    pass


def clear_items():
    """Removes every item from the list."""
    # Step 8
    pass


def item_clicked(event):
    """Copies the clicked item into the entry box so it can be changed."""
    # Step 8
    pass


# Create the main window
root = tk.Tk()
root.title("List editor")
root.geometry("520x480")
root.configure(bg=BG_COLOR)

# Create widgets (Step 4)
# Each widget below is in its simplest form, so the program already runs.
# Add the missing options to each one, using title_label as your guide:
#   line 1: what it shows (text and size)
#   line 2: how it looks (colours and font)
#   line 3: any extra setting, e.g. command= (buttons get this in Step 9)

# Example - done for you
title_label = tk.Label(
    root, text="List Editor",
    bg=BG_COLOR, fg=TITLE_COLOR, font=TITLE_FONT)

# Label - add: bg=BG_COLOR, fg=TEXT_COLOR, font=FONT_STYLE
instructions_label = tk.Label(
    root, text="Type an item or click one below.")

# Entry box - add: width=20, font=LIST_FONT
item_entry = tk.Entry(root)

# Listbox - add: width=20, height=8,
#                bg=LIST_BG_COLOR, fg=TEXT_COLOR, font=LIST_FONT,
#                exportselection=False
# exportselection=False keeps the selected item highlighted
# when the user clicks in the entry box to type
item_listbox = tk.Listbox(root)

# Buttons - add: width=8, fg=BUTTON_FG_COLOR, font=BUTTON_FONT
#   and bg=PRIMARY_COLOR (blue) or bg=SECONDARY_COLOR (pink) as shown
add_button = tk.Button(
    root, text="Add")                     # blue
change_button = tk.Button(
    root, text="Change")                  # blue
remove_button = tk.Button(
    root, text="Remove")                  # pink
sort_button = tk.Button(
    root, text="Sort")                    # blue
clear_button = tk.Button(
    root, text="Clear")                   # pink

# Bottom labels - add: bg=BG_COLOR, font=FONT_STYLE
#   count_label also gets fg=TEXT_COLOR
#   message_label also gets fg=PRIMARY_COLOR
count_label = tk.Label(
    root, text="")
message_label = tk.Label(
    root, text="")

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
