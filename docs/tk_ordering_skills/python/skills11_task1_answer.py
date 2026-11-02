import tkinter as tk


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


# 2. CONSTANTS
BG_COLOUR = "#fff8dc"        # pale cream background
TEXT_COLOUR = "#2f4f2f"      # dark green text
MENU_COLOUR = "#ffe4b5"      # pale orange drop-down menu

LABEL_FONT = ("Segoe UI", 13, "normal")
RADIO_FONT = ("Segoe UI", 12, "normal")


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


# 4. TKINTER WIDGETS
# Main window
root = tk.Tk()
root.title("Juice Bar")
root.geometry("500x300")
root.config(bg=BG_COLOUR)

# Juice (radio buttons)
juice_label = tk.Label(root)  # 1. create
juice_label.grid(row=0, column=0, padx=10, pady=10, sticky="ne")  # 2. position
juice_label.config(text="Juice:", font=LABEL_FONT, bg=BG_COLOUR, fg=TEXT_COLOUR)  # 3. configure

juice_frame = tk.Frame(root)  # 1. create
juice_frame.grid(row=0, column=1, padx=10, pady=10, sticky="w")  # 2. position
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
size_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")  # 2. position
size_label.config(text="Size:", font=LABEL_FONT, bg=BG_COLOUR, fg=TEXT_COLOUR)  # 3. configure

size_var = tk.StringVar(root)  # A. make
size_var.set("Small")  # B. set
size_var.trace_add("write", update_juice_price)  # C. bind

size_menu = tk.OptionMenu(root, size_var, "Small")  # 1. create
size_menu.grid(row=1, column=1, padx=10, pady=5, sticky="w")  # 2. position
size_menu.config(width=12, font=LABEL_FONT, bg=MENU_COLOUR, fg=TEXT_COLOUR,
                 activebackground=MENU_COLOUR)  # 3. configure

size_choices = size_menu["menu"]
size_choices.config(font=LABEL_FONT, bg=MENU_COLOUR, fg=TEXT_COLOUR)
size_choices.delete(0)   # remove the starting choice
for size in sizes.keys():
    size_choices.add_radiobutton(label=size, variable=size_var, value=size)

extra_label = tk.Label(root)  # 1. create
extra_label.grid(row=2, column=0, padx=10, pady=5, sticky="e")  # 2. position
extra_label.config(text="Extra:", font=LABEL_FONT, bg=BG_COLOUR, fg=TEXT_COLOUR)  # 3. configure

extra_var = tk.StringVar(root)  # A. make
extra_var.set("No extra")  # B. set
extra_var.trace_add("write", update_juice_price)  # C. bind

extra_menu = tk.OptionMenu(root, extra_var, "No extra")  # 1. create
extra_menu.grid(row=2, column=1, padx=10, pady=5, sticky="w")  # 2. position
extra_menu.config(width=12, font=LABEL_FONT, bg=MENU_COLOUR, fg=TEXT_COLOUR,
                  activebackground=MENU_COLOUR)  # 3. configure

extra_choices = extra_menu["menu"]
extra_choices.config(font=LABEL_FONT, bg=MENU_COLOUR, fg=TEXT_COLOUR)
extra_choices.delete(0)   # remove the starting choice
for extra in extras.keys():
    extra_choices.add_radiobutton(label=extra, variable=extra_var, value=extra)

# Price of the chosen juice
price_label = tk.Label(root)  # 1. create
price_label.grid(row=3, column=1, padx=10, pady=10, sticky="w")  # 2. position
price_label.config(text="Price: $0.00", font=LABEL_FONT, bg=BG_COLOUR, fg=TEXT_COLOUR)  # 3. configure


# 5. MAIN CODE
update_juice_price()
root.mainloop()
