import tkinter as tk
from tkinter import messagebox


# 1. DATA DICTIONARIES & LISTS
# Bubble tea drinks and the price of a regular drink
drinks = {
    "Classic Milk Tea": 5.50,
    "Brown Sugar Milk Tea": 6.50,
    "Taro Milk Tea": 6.50,
    "Matcha Latte": 7.00,
    "Mango Green Tea": 6.00,
    "Passionfruit Black Tea": 6.00,
}

# Sizes and their extra cost
sizes = {
    "Regular": 0.00,
    "Large": 1.00,
    "Jumbo": 2.00,
}

# Pearls and their extra cost
pearls = {
    "No pearls": 0.00,
    "Tapioca pearls": 0.80,
    "Popping boba": 1.00,
    "Coconut jelly": 1.00,
}

# Extras and their extra cost
extras = {
    "No extra": 0.00,
    "Cheese foam": 1.50,
    "Pudding": 1.20,
    "Extra shot of tea": 0.80,
}

# List that stores every bubble tea in the order
orders = []


# 2. CONSTANTS
# Colours
BG_COLOUR = "#f3ece4"        # milk tea background
TITLE_COLOUR = "#6b3e26"     # brown sugar title
TEXT_COLOUR = "#2e2a27"      # dark tapioca text
MENU_COLOUR = "#e3d3f2"      # taro purple drop-down menus
LIST_COLOUR = "#fffdf9"      # off-white order list
ADD_COLOUR = "#cfe8c4"       # matcha green add button
REMOVE_COLOUR = "#f6d0c4"    # peach remove and clear buttons

# Fonts
TITLE_FONT = ("Trebuchet MS", 24, "bold")
LABEL_FONT = ("Trebuchet MS", 13, "normal")
RADIO_FONT = ("Trebuchet MS", 12, "normal")
LIST_FONT = ("Trebuchet MS", 11, "normal")
BUTTON_FONT = ("Trebuchet MS", 12, "bold")


# 3. DEFINITIONS
def get_drink_price():
    """Adds up the drink, size, pearls and extra prices for one bubble tea."""
    drink = drink_var.get()
    size = size_var.get()
    pearl = pearl_var.get()
    extra = extra_var.get()
    price = drinks[drink] + sizes[size] + pearls[pearl] + extras[extra]
    return price


def update_drink_price(*args):
    """Shows the price of the bubble tea that is chosen right now."""
    price = get_drink_price()
    price_label.config(text=f"Price: ${price:.2f}")


def show_drink_orders():
    """Redraws the order list and the total so they match the orders list."""
    order_listbox.delete(0, tk.END)
    total = 0
    for bubble_tea in orders:
        drink = bubble_tea["drink"]
        size = bubble_tea["size"]
        pearl = bubble_tea["pearl"]
        extra = bubble_tea["extra"]
        price = bubble_tea["price"]
        order_listbox.insert(tk.END, f"{size} {drink}, {pearl}, {extra}: ${price:.2f}")
        total = total + price
    total_label.config(text=f"Total: ${total:.2f}")


def add_drink():
    """Adds the chosen bubble tea to the orders list."""
    bubble_tea = {
        "drink": drink_var.get(),
        "size": size_var.get(),
        "pearl": pearl_var.get(),
        "extra": extra_var.get(),
        "price": get_drink_price(),
    }
    orders.append(bubble_tea)
    show_drink_orders()


def remove_drink():
    """Removes the bubble tea that is selected in the order list."""
    selection = order_listbox.curselection()
    if not selection:
        messagebox.showinfo("Remove", "Click a bubble tea in the order list first.")
    else:
        line_number = selection[0]
        del orders[line_number]
        show_drink_orders()


def clear_drink_orders():
    """Removes every bubble tea from the orders list."""
    orders.clear()
    show_drink_orders()


# 4. TKINTER WIDGETS
# Main window
root = tk.Tk()
root.title("Bubble Tea Bar")
root.geometry("1180x600")
root.config(bg=BG_COLOUR)

# --- LEFT SIDE: BUBBLE TEA CHOICES ---

# Title
title_label = tk.Label(root)  # 1. create
title_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="w")  # 2. position
title_label.config(text="Bubble Tea Bar", font=TITLE_FONT, bg=BG_COLOUR, fg=TITLE_COLOUR)  # 3. configure

# Drink (radio buttons)
drink_label = tk.Label(root)  # 1. create
drink_label.grid(row=1, column=0, padx=10, pady=5, sticky="ne")  # 2. position
drink_label.config(text="Drink:", font=LABEL_FONT, bg=BG_COLOUR, fg=TEXT_COLOUR)  # 3. configure

drink_frame = tk.Frame(root)  # 1. create
drink_frame.grid(row=1, column=1, padx=10, pady=5, sticky="w")  # 2. position
drink_frame.config(bg=BG_COLOUR)  # 3. configure

drink_var = tk.StringVar(root)  # A. make
drink_var.set("Classic Milk Tea")  # B. set
drink_var.trace_add("write", update_drink_price)  # C. bind

for drink in drinks.keys():
    drink_radio = tk.Radiobutton(drink_frame, variable=drink_var, value=drink)  # 1. create
    drink_radio.pack(anchor="w")  # 2. position
    drink_radio.config(text=f"{drink} (${drinks[drink]:.2f})", font=RADIO_FONT,
                       bg=BG_COLOUR, fg=TEXT_COLOUR, activebackground=BG_COLOUR,
                       highlightthickness=0)  # 3. configure

# Size (drop-down menu)
size_label = tk.Label(root)  # 1. create
size_label.grid(row=2, column=0, padx=10, pady=5, sticky="e")  # 2. position
size_label.config(text="Size:", font=LABEL_FONT, bg=BG_COLOUR, fg=TEXT_COLOUR)  # 3. configure

size_var = tk.StringVar(root)  # A. make
size_var.set("Regular")  # B. set
size_var.trace_add("write", update_drink_price)  # C. bind

size_menu = tk.OptionMenu(root, size_var, "Regular")  # 1. create
size_menu.grid(row=2, column=1, padx=10, pady=5, sticky="w")  # 2. position
size_menu.config(width=16, font=LABEL_FONT, bg=MENU_COLOUR, fg=TEXT_COLOUR,
                 activebackground=MENU_COLOUR)  # 3. configure

size_choices = size_menu["menu"]
size_choices.config(font=LABEL_FONT, bg=MENU_COLOUR, fg=TEXT_COLOUR)
size_choices.delete(0)   # remove the starting choice
for size in sizes.keys():
    size_choices.add_radiobutton(label=size, variable=size_var, value=size)

# Pearls (drop-down menu)
pearl_label = tk.Label(root)  # 1. create
pearl_label.grid(row=3, column=0, padx=10, pady=5, sticky="e")  # 2. position
pearl_label.config(text="Pearls:", font=LABEL_FONT, bg=BG_COLOUR, fg=TEXT_COLOUR)  # 3. configure

pearl_var = tk.StringVar(root)  # A. make
pearl_var.set("No pearls")  # B. set
pearl_var.trace_add("write", update_drink_price)  # C. bind

pearl_menu = tk.OptionMenu(root, pearl_var, "No pearls")  # 1. create
pearl_menu.grid(row=3, column=1, padx=10, pady=5, sticky="w")  # 2. position
pearl_menu.config(width=16, font=LABEL_FONT, bg=MENU_COLOUR, fg=TEXT_COLOUR,
                  activebackground=MENU_COLOUR)  # 3. configure

pearl_choices = pearl_menu["menu"]
pearl_choices.config(font=LABEL_FONT, bg=MENU_COLOUR, fg=TEXT_COLOUR)
pearl_choices.delete(0)   # remove the starting choice
for pearl in pearls.keys():
    pearl_choices.add_radiobutton(label=pearl, variable=pearl_var, value=pearl)

# Extra (drop-down menu)
extra_label = tk.Label(root)  # 1. create
extra_label.grid(row=4, column=0, padx=10, pady=5, sticky="e")  # 2. position
extra_label.config(text="Extra:", font=LABEL_FONT, bg=BG_COLOUR, fg=TEXT_COLOUR)  # 3. configure

extra_var = tk.StringVar(root)  # A. make
extra_var.set("No extra")  # B. set
extra_var.trace_add("write", update_drink_price)  # C. bind

extra_menu = tk.OptionMenu(root, extra_var, "No extra")  # 1. create
extra_menu.grid(row=4, column=1, padx=10, pady=5, sticky="w")  # 2. position
extra_menu.config(width=16, font=LABEL_FONT, bg=MENU_COLOUR, fg=TEXT_COLOUR,
                  activebackground=MENU_COLOUR)  # 3. configure

extra_choices = extra_menu["menu"]
extra_choices.config(font=LABEL_FONT, bg=MENU_COLOUR, fg=TEXT_COLOUR)
extra_choices.delete(0)   # remove the starting choice
for extra in extras.keys():
    extra_choices.add_radiobutton(label=extra, variable=extra_var, value=extra)

# Price of the chosen bubble tea
price_label = tk.Label(root)  # 1. create
price_label.grid(row=5, column=1, padx=10, pady=5, sticky="w")  # 2. position
price_label.config(text="Price: $0.00", font=LABEL_FONT, bg=BG_COLOUR, fg=TEXT_COLOUR)  # 3. configure

# Add to order button
add_button = tk.Button(root)  # 1. create
add_button.grid(row=6, column=1, padx=10, pady=10, ipady=4, sticky="w")  # 2. position
add_button.config(text="Add to order", width=14, font=BUTTON_FONT, bg=ADD_COLOUR, fg=TEXT_COLOUR)  # 3. configure
add_button.config(command=add_drink)  # 4. command

# --- RIGHT SIDE: THE ORDER ---

# Order heading
order_heading = tk.Label(root)  # 1. create
order_heading.grid(row=0, column=2, columnspan=2, padx=10, pady=10, sticky="sw")  # 2. position
order_heading.config(text="Your bubble tea order", font=LABEL_FONT, bg=BG_COLOUR, fg=TEXT_COLOUR)  # 3. configure

# Order list
order_listbox = tk.Listbox(root)  # 1. create
order_listbox.grid(row=1, column=2, rowspan=5, columnspan=2, padx=10, pady=5, sticky="nsew")  # 2. position
order_listbox.config(width=62, height=12, font=LIST_FONT, bg=LIST_COLOUR, fg=TEXT_COLOUR)  # 3. configure

# Total cost of the order
total_label = tk.Label(root)  # 1. create
total_label.grid(row=6, column=2, columnspan=2, padx=10, pady=5, sticky="w")  # 2. position
total_label.config(text="Total: $0.00", font=LABEL_FONT, bg=BG_COLOUR, fg=TEXT_COLOUR)  # 3. configure

# Remove selected button
remove_button = tk.Button(root)  # 1. create
remove_button.grid(row=7, column=2, padx=10, pady=10, ipady=4, sticky="w")  # 2. position
remove_button.config(text="Remove selected", width=14, font=BUTTON_FONT, bg=REMOVE_COLOUR, fg=TEXT_COLOUR)  # 3. configure
remove_button.config(command=remove_drink)  # 4. command

# Clear order button
clear_button = tk.Button(root)  # 1. create
clear_button.grid(row=7, column=3, padx=10, pady=10, ipady=4, sticky="e")  # 2. position
clear_button.config(text="Clear order", width=14, font=BUTTON_FONT, bg=REMOVE_COLOUR, fg=TEXT_COLOUR)  # 3. configure
clear_button.config(command=clear_drink_orders)  # 4. command


# 5. MAIN CODE
update_drink_price()
show_drink_orders()
root.mainloop()
