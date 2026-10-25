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

for flavour in flavours.keys():
    flavour_radio = tk.Radiobutton(flavour_frame, variable=flavour_var, value=flavour)  # 1. create
    flavour_radio.pack(anchor="w")  # 2. position
    flavour_radio.config(text=f"{flavour} (${flavours[flavour]:.2f})", font=RADIO_FONT,
                         bg=BG_COLOUR, fg=TEXT_COLOUR, activebackground=BG_COLOUR,
                         highlightthickness=0)  # 3. configure

# --- RIGHT SIDE: THE ORDER ---

# Order heading
order_heading = tk.Label(root)  # 1. create
order_heading.grid(row=0, column=2, columnspan=2, padx=10, pady=10, sticky="sw")  # 2. position
order_heading.config(text="Your order", font=LABEL_FONT, bg=BG_COLOUR, fg=TEXT_COLOUR)  # 3. configure


# 5. MAIN CODE
root.mainloop()
