import tkinter as tk
from tkinter import messagebox


# 1. DATA DICTIONARIES & LISTS
# Juices and the price of a small cup
juices = {
    "Orange": 5.00,
    "Apple": 4.50,
    "Mango": 6.00,
    "Watermelon": 5.50,
}

# Sizes and their extra cost
sizes = {
    "Small": 0.00,
    "Regular": 1.00,
    "Large": 2.00,
}

# Extras and their extra cost
extras = {
    "No extra": 0.00,
    "Chia seeds": 1.00,
    "Protein": 2.00,
}

# List that stores every juice in the order
orders = []


# 2. CONSTANTS
# Colours
BG_COLOUR = "#fff8dc"        # pale cream background
TITLE_COLOUR = "#ff8c00"     # orange title
TEXT_COLOUR = "#2f4f2f"      # dark green text
MENU_COLOUR = "#ffe4b5"      # pale orange drop-down menu
LIST_COLOUR = "#ffffff"      # white order list
ADD_COLOUR = "#c8f0c8"       # pale green add button
REMOVE_COLOUR = "#ffd6d6"    # pale red remove and clear buttons

# Fonts
TITLE_FONT = ("Segoe UI", 20, "bold")
LABEL_FONT = ("Segoe UI", 13, "normal")
RADIO_FONT = ("Segoe UI", 12, "normal")
LIST_FONT = ("Segoe UI", 12, "normal")
BUTTON_FONT = ("Segoe UI", 12, "bold")


# 3. DEFINITIONS


def get_juice_price():
    """Adds up the juice, size and extra prices for one juice."""
    juice = juice_var.get()
    size = size_var.get()
    extra = extra_var.get()
    price = juices[juice] + sizes[size] + extras[extra]
    return price


def update_juice_price(*args):
    """Shows the price of the juice that is chosen right now."""
    price = get_juice_price()
    price_label.config(text=f"Price: ${price:.2f}")


def show_juice_orders():
    """Redraws the order list and the total so they match the orders list."""
    order_listbox.delete(0, tk.END)
    total = 0
    for juice in orders:
        order_listbox.insert(tk.END, f"{juice['juice']}, {juice['size']}, {juice['extra']}: ${juice['price']:.2f}")
        total = total + juice["price"]
    total_label.config(text=f"Total: ${total:.2f}")


def add_juice():
    """Adds the chosen juice to the orders list."""
    juice = {
        "juice": juice_var.get(),
        "size": size_var.get(),
        "extra": extra_var.get(),
        "price": get_juice_price(),
    }
    orders.append(juice)
    show_juice_orders()


def remove_juice():
    """Removes the juice that is selected in the order list."""
    selection = order_listbox.curselection()
    if not selection:
        messagebox.showinfo("Remove", "Click a juice in the order list first.")
    else:
        line_number = selection[0]
        del orders[line_number]
        show_juice_orders()


def clear_juice_orders():
    """Removes every juice from the orders list."""
    orders.clear()
    show_juice_orders()


# 4. TKINTER WIDGETS
# Main window
root = tk.Tk()
root.title("Juice Bar")
root.geometry("820x420")
root.config(bg=BG_COLOUR)

# --- LEFT SIDE: JUICE CHOICES ---

# Title
title_label = tk.Label(root)  # 1. create
title_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="w")  # 2. position
title_label.config(text="Juice Bar", font=TITLE_FONT, bg=BG_COLOUR, fg=TITLE_COLOUR)  # 3. configure

# Juice (radio buttons)
juice_label = tk.Label(root)  # 1. create
juice_label.grid(row=1, column=0, padx=10, pady=5, sticky="ne")  # 2. position
juice_label.config(text="Juice:", font=LABEL_FONT, bg=BG_COLOUR, fg=TEXT_COLOUR)  # 3. configure

juice_frame = tk.Frame(root)  # 1. create
juice_frame.grid(row=1, column=1, padx=10, pady=5, sticky="w")  # 2. position
juice_frame.config(bg=BG_COLOUR)  # 3. configure

juice_var = tk.StringVar(root)  # A. make
juice_var.set("Orange")  # B. set
juice_var.trace_add("write", update_juice_price)  # C. bind

for juice in juices.keys():
    juice_radio = tk.Radiobutton(juice_frame, variable=juice_var, value=juice)  # 1. create
    juice_radio.pack(anchor="w")  # 2. position
    juice_radio.config(text=f"{juice} (${juices[juice]:.2f})", font=RADIO_FONT,
                       bg=BG_COLOUR, fg=TEXT_COLOUR, activebackground=BG_COLOUR,
                       highlightthickness=0)  # 3. configure

# Size (drop-down menu)
size_label = tk.Label(root)  # 1. create
size_label.grid(row=2, column=0, padx=10, pady=5, sticky="e")  # 2. position
size_label.config(text="Size:", font=LABEL_FONT, bg=BG_COLOUR, fg=TEXT_COLOUR)  # 3. configure

size_var = tk.StringVar(root)  # A. make
size_var.set("Small")  # B. set
size_var.trace_add("write", update_juice_price)  # C. bind

size_menu = tk.OptionMenu(root, size_var, "Small")  # 1. create
size_menu.grid(row=2, column=1, padx=10, pady=5, sticky="w")  # 2. position
size_menu.config(width=14, font=LABEL_FONT, bg=MENU_COLOUR, fg=TEXT_COLOUR,
                 activebackground=MENU_COLOUR)  # 3. configure

size_choices = size_menu["menu"]
size_choices.config(font=LABEL_FONT, bg=MENU_COLOUR, fg=TEXT_COLOUR)
size_choices.delete(0)   # remove the starting choice
for size in sizes.keys():
    size_choices.add_radiobutton(label=size, variable=size_var, value=size)

# Extra (drop-down menu)
extra_label = tk.Label(root)  # 1. create
extra_label.grid(row=3, column=0, padx=10, pady=5, sticky="e")  # 2. position
extra_label.config(text="Extra:", font=LABEL_FONT, bg=BG_COLOUR, fg=TEXT_COLOUR)  # 3. configure

extra_var = tk.StringVar(root)  # A. make
extra_var.set("No extra")  # B. set
extra_var.trace_add("write", update_juice_price)  # C. bind

extra_menu = tk.OptionMenu(root, extra_var, "No extra")  # 1. create
extra_menu.grid(row=3, column=1, padx=10, pady=5, sticky="w")  # 2. position
extra_menu.config(width=14, font=LABEL_FONT, bg=MENU_COLOUR, fg=TEXT_COLOUR,
                  activebackground=MENU_COLOUR)  # 3. configure

extra_choices = extra_menu["menu"]
extra_choices.config(font=LABEL_FONT, bg=MENU_COLOUR, fg=TEXT_COLOUR)
extra_choices.delete(0)   # remove the starting choice
for extra in extras.keys():
    extra_choices.add_radiobutton(label=extra, variable=extra_var, value=extra)

# Price of the chosen juice
price_label = tk.Label(root)  # 1. create
price_label.grid(row=4, column=1, padx=10, pady=5, sticky="w")  # 2. position
price_label.config(text="Price: $0.00", font=LABEL_FONT, bg=BG_COLOUR, fg=TEXT_COLOUR)  # 3. configure

# Add to order button
add_button = tk.Button(root)  # 1. create
add_button.grid(row=5, column=1, padx=10, pady=10, ipady=4, sticky="w")  # 2. position
add_button.config(text="Add to order", width=14, font=BUTTON_FONT, bg=ADD_COLOUR, fg=TEXT_COLOUR)  # 3. configure
add_button.config(command=add_juice)  # 4. command

# --- RIGHT SIDE: THE ORDER ---

# Order heading
order_heading = tk.Label(root)  # 1. create
order_heading.grid(row=0, column=2, columnspan=2, padx=10, pady=10, sticky="sw")  # 2. position
order_heading.config(text="Your order", font=LABEL_FONT, bg=BG_COLOUR, fg=TEXT_COLOUR)  # 3. configure

# Order list
order_listbox = tk.Listbox(root)  # 1. create
order_listbox.grid(row=1, column=2, rowspan=4, columnspan=2, padx=10, pady=5, sticky="nsew")  # 2. position
order_listbox.config(width=34, height=10, font=LIST_FONT, bg=LIST_COLOUR, fg=TEXT_COLOUR)  # 3. configure

# Total cost of the order
total_label = tk.Label(root)  # 1. create
total_label.grid(row=5, column=2, columnspan=2, padx=10, pady=5, sticky="w")  # 2. position
total_label.config(text="Total: $0.00", font=LABEL_FONT, bg=BG_COLOUR, fg=TEXT_COLOUR)  # 3. configure

# Remove selected button
remove_button = tk.Button(root)  # 1. create
remove_button.grid(row=6, column=2, padx=10, pady=10, ipady=4, sticky="w")  # 2. position
remove_button.config(text="Remove selected", width=14, font=BUTTON_FONT, bg=REMOVE_COLOUR, fg=TEXT_COLOUR)  # 3. configure
remove_button.config(command=remove_juice)  # 4. command

# Clear order button
clear_button = tk.Button(root)  # 1. create
clear_button.grid(row=6, column=3, padx=10, pady=10, ipady=4, sticky="e")  # 2. position
clear_button.config(text="Clear order", width=14, font=BUTTON_FONT, bg=REMOVE_COLOUR, fg=TEXT_COLOUR)  # 3. configure
clear_button.config(command=clear_juice_orders)  # 4. command


# 5. MAIN CODE
update_juice_price()
show_juice_orders()
root.mainloop()
