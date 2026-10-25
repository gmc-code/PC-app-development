import tkinter as tk


# 1. DATA DICTIONARIES & LISTS
# Ice cream flavours and the price of one scoop
flavours = {
    "Vanilla": 4.00,
    "Chocolate": 4.00,
    "Strawberry": 4.50,
    "Mint Choc Chip": 5.00,
    "Cookies and Cream": 5.50,
}

# Containers and their extra cost
containers = {
    "Cup": 0.00,
    "Plain cone": 0.50,
    "Waffle cone": 1.50,
}

# Toppings and their extra cost
toppings = {
    "No topping": 0.00,
    "Sprinkles": 0.50,
    "Chocolate sauce": 1.00,
    "Crushed nuts": 1.00,
}

# List that stores every ice cream in the order
orders = []


# 2. CONSTANTS
# Colours
BG_COLOUR = "#fff4e6"        # cream background
TITLE_COLOUR = "#d94f70"     # strawberry pink title
TEXT_COLOUR = "#4a2c2a"      # chocolate brown text
MENU_COLOUR = "#ffd6e0"      # pale pink drop-down menus
LIST_COLOUR = "#ffffff"      # white order list
ADD_COLOUR = "#c8f0c8"       # pale green add button
REMOVE_COLOUR = "#ffd6d6"    # pale red remove and clear buttons

# Fonts
TITLE_FONT = ("Segoe UI", 22, "bold")
LABEL_FONT = ("Segoe UI", 13, "normal")
RADIO_FONT = ("Segoe UI", 12, "normal")
LIST_FONT = ("Segoe UI", 12, "normal")
BUTTON_FONT = ("Segoe UI", 12, "bold")


# 3. DEFINITIONS
def get_ice_cream_price():
    """Adds up the flavour, container and topping prices for one ice cream."""
    flavour = flavour_var.get()
    container = container_var.get()
    topping = topping_var.get()
    price = flavours[flavour] + containers[container] + toppings[topping]
    return price


def update_ice_cream_price(*args):
    """Shows the price of the ice cream that is chosen right now."""
    price = get_ice_cream_price()
    price_label.config(text=f"Price: ${price:.2f}")


# 4. TKINTER WIDGETS
# Main window
root = tk.Tk()
root.title("Ice Cream Shop")
root.geometry("940x520")
root.config(bg=BG_COLOUR)

# --- LEFT SIDE: ICE CREAM CHOICES ---

# Title
title_label = tk.Label(root)  # 1. create
title_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="w")  # 2. position
title_label.config(text="Ice Cream Shop", font=TITLE_FONT, bg=BG_COLOUR, fg=TITLE_COLOUR)  # 3. configure

# Flavour (radio buttons)
flavour_label = tk.Label(root)  # 1. create
flavour_label.grid(row=1, column=0, padx=10, pady=5, sticky="ne")  # 2. position
flavour_label.config(text="Flavour:", font=LABEL_FONT, bg=BG_COLOUR, fg=TEXT_COLOUR)  # 3. configure

flavour_frame = tk.Frame(root)  # 1. create
flavour_frame.grid(row=1, column=1, padx=10, pady=5, sticky="w")  # 2. position
flavour_frame.config(bg=BG_COLOUR)  # 3. configure

flavour_var = tk.StringVar(root)  # A. make
flavour_var.set("Vanilla")  # B. set
flavour_var.trace_add("write", update_ice_cream_price)  # C. bind

for flavour in flavours.keys():
    flavour_radio = tk.Radiobutton(flavour_frame, variable=flavour_var, value=flavour)  # 1. create
    flavour_radio.pack(anchor="w")  # 2. position
    flavour_radio.config(text=f"{flavour} (${flavours[flavour]:.2f})", font=RADIO_FONT,
                         bg=BG_COLOUR, fg=TEXT_COLOUR, activebackground=BG_COLOUR,
                         highlightthickness=0)  # 3. configure

# Container (drop-down menu)
container_label = tk.Label(root)  # 1. create
container_label.grid(row=2, column=0, padx=10, pady=5, sticky="e")  # 2. position
container_label.config(text="Container:", font=LABEL_FONT, bg=BG_COLOUR, fg=TEXT_COLOUR)  # 3. configure

container_var = tk.StringVar(root)  # A. make
container_var.set("Cup")  # B. set
container_var.trace_add("write", update_ice_cream_price)  # C. bind

container_menu = tk.OptionMenu(root, container_var, "Cup")  # 1. create
container_menu.grid(row=2, column=1, padx=10, pady=5, sticky="w")  # 2. position
container_menu.config(width=16, font=LABEL_FONT, bg=MENU_COLOUR, fg=TEXT_COLOUR,
                      activebackground=MENU_COLOUR)  # 3. configure

container_choices = container_menu["menu"]
container_choices.config(font=LABEL_FONT, bg=MENU_COLOUR, fg=TEXT_COLOUR)
container_choices.delete(0)   # remove the starting choice
for container in containers.keys():
    container_choices.add_radiobutton(label=container, variable=container_var, value=container)

# Topping (drop-down menu)
topping_label = tk.Label(root)  # 1. create
topping_label.grid(row=3, column=0, padx=10, pady=5, sticky="e")  # 2. position
topping_label.config(text="Topping:", font=LABEL_FONT, bg=BG_COLOUR, fg=TEXT_COLOUR)  # 3. configure

topping_var = tk.StringVar(root)  # A. make
topping_var.set("No topping")  # B. set
topping_var.trace_add("write", update_ice_cream_price)  # C. bind

topping_menu = tk.OptionMenu(root, topping_var, "No topping")  # 1. create
topping_menu.grid(row=3, column=1, padx=10, pady=5, sticky="w")  # 2. position
topping_menu.config(width=16, font=LABEL_FONT, bg=MENU_COLOUR, fg=TEXT_COLOUR,
                    activebackground=MENU_COLOUR)  # 3. configure

topping_choices = topping_menu["menu"]
topping_choices.config(font=LABEL_FONT, bg=MENU_COLOUR, fg=TEXT_COLOUR)
topping_choices.delete(0)   # remove the starting choice
for topping in toppings.keys():
    topping_choices.add_radiobutton(label=topping, variable=topping_var, value=topping)

# Price of the chosen ice cream
price_label = tk.Label(root)  # 1. create
price_label.grid(row=4, column=1, padx=10, pady=5, sticky="w")  # 2. position
price_label.config(text="Price: $0.00", font=LABEL_FONT, bg=BG_COLOUR, fg=TEXT_COLOUR)  # 3. configure

# --- RIGHT SIDE: THE ORDER ---

# Order heading
order_heading = tk.Label(root)  # 1. create
order_heading.grid(row=0, column=2, columnspan=2, padx=10, pady=10, sticky="sw")  # 2. position
order_heading.config(text="Your order", font=LABEL_FONT, bg=BG_COLOUR, fg=TEXT_COLOUR)  # 3. configure


# 5. MAIN CODE
update_ice_cream_price()
root.mainloop()
