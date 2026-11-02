import tkinter as tk


# 1. DATA DICTIONARIES & LISTS
# List that stores every juice in the order
orders = []


# 2. CONSTANTS
BG_COLOUR = "#fff8dc"        # pale cream background
TEXT_COLOUR = "#2f4f2f"      # dark green text
ADD_COLOUR = "#c8f0c8"       # pale green add button
REMOVE_COLOUR = "#ffd6d6"    # pale red clear button

LABEL_FONT = ("Segoe UI", 13, "normal")
BUTTON_FONT = ("Segoe UI", 12, "bold")


# 3. DEFINITIONS


def show_juice_count():
    """Shows how many juices are in the order, and the last one added."""
    count_label.config(text=f"Juices ordered: {len(orders)}")
    if len(orders) > 0:
        last_label.config(text=f"Last juice: {orders[-1]}")
    else:
        last_label.config(text="Last juice: none")


def add_orange():
    """Adds an orange juice to the order."""
    orders.append("Orange")
    show_juice_count()


def clear_juice_orders():
    """Removes every juice from the order."""
    orders.clear()
    show_juice_count()


# 4. TKINTER WIDGETS
# Main window
root = tk.Tk()
root.title("Juice Bar")
root.geometry("500x300")
root.config(bg=BG_COLOUR)

# Count of juices
count_label = tk.Label(root)  # 1. create
count_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="w")  # 2. position
count_label.config(text="Juices ordered: 0", font=LABEL_FONT, bg=BG_COLOUR, fg=TEXT_COLOUR)  # 3. configure

# Add button
add_button = tk.Button(root)  # 1. create
add_button.grid(row=1, column=0, padx=10, pady=10, ipady=4, sticky="w")  # 2. position
add_button.config(text="Add orange juice", width=16, font=BUTTON_FONT, bg=ADD_COLOUR, fg=TEXT_COLOUR)  # 3. configure
add_button.config(command=add_orange)  # 4. command

# Clear button
clear_button = tk.Button(root)  # 1. create
clear_button.grid(row=1, column=1, padx=10, pady=10, ipady=4, sticky="w")  # 2. position
clear_button.config(text="Clear order", width=16, font=BUTTON_FONT, bg=REMOVE_COLOUR, fg=TEXT_COLOUR)  # 3. configure
clear_button.config(command=clear_juice_orders)  # 4. command

last_label = tk.Label(root)  # 1. create
last_label.grid(row=3, column=0, columnspan=2, padx=10, pady=5, sticky="w")  # 2. position
last_label.config(text="Last juice: none", font=LABEL_FONT, bg=BG_COLOUR, fg=TEXT_COLOUR)  # 3. configure


# 5. MAIN CODE
show_juice_count()
root.mainloop()
