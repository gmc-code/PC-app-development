import tkinter as tk
from tkinter import messagebox


# 1. DATA DICTIONARIES & LISTS
# Juices and their prices
juices = {
    "Orange": 5.00,
    "Apple": 4.50,
    "Mango": 6.00,
}

# List that stores every juice in the order
orders = []


# 2. CONSTANTS
BG_COLOUR = "#fff8dc"        # pale cream background
TEXT_COLOUR = "#2f4f2f"      # dark green text
LIST_COLOUR = "#ffffff"      # white order list
ADD_COLOUR = "#c8f0c8"       # pale green add button
REMOVE_COLOUR = "#ffd6d6"    # pale red remove and clear buttons

LABEL_FONT = ("Segoe UI", 13, "normal")
RADIO_FONT = ("Segoe UI", 12, "normal")
LIST_FONT = ("Segoe UI", 12, "normal")
BUTTON_FONT = ("Segoe UI", 12, "bold")


# 3. DEFINITIONS


def show_juice_orders():
    """Redraws the order list, the total and the count."""
    order_listbox.delete(0, tk.END)
    total = 0
    for juice in orders:
        order_listbox.insert(tk.END, f"{juice['juice']}: ${juice['price']:.2f}")
        total = total + juice["price"]
    total_label.config(text=f"Total: ${total:.2f}")
    count_label.config(text=f"Juices: {len(orders)}")


def add_juice():
    """Adds the chosen juice to the orders list."""
    juice = {
        "juice": juice_var.get(),
        "price": juices[juice_var.get()],
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
root.geometry("620x320")
root.config(bg=BG_COLOUR)

# --- LEFT SIDE: JUICE CHOICE ---

# Juice (radio buttons)
juice_frame = tk.Frame(root)  # 1. create
juice_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nw")  # 2. position
juice_frame.config(bg=BG_COLOUR)  # 3. configure

juice_var = tk.StringVar(root)  # A. make
juice_var.set("Orange")  # B. set

for juice in juices.keys():
    juice_radio = tk.Radiobutton(juice_frame, variable=juice_var, value=juice)  # 1. create
    juice_radio.pack(anchor="w")  # 2. position
    juice_radio.config(text=f"{juice} (${juices[juice]:.2f})", font=RADIO_FONT,
                       bg=BG_COLOUR, fg=TEXT_COLOUR, activebackground=BG_COLOUR,
                       highlightthickness=0)  # 3. configure

# Add to order button
add_button = tk.Button(root)  # 1. create
add_button.grid(row=1, column=0, padx=10, pady=10, ipady=4, sticky="w")  # 2. position
add_button.config(text="Add to order", width=14, font=BUTTON_FONT, bg=ADD_COLOUR, fg=TEXT_COLOUR)  # 3. configure
add_button.config(command=add_juice)  # 4. command

# --- RIGHT SIDE: THE ORDER ---

# Order list
order_listbox = tk.Listbox(root)  # 1. create
order_listbox.grid(row=0, column=1, columnspan=2, padx=10, pady=10, sticky="nsew")  # 2. position
order_listbox.config(width=30, height=8, font=LIST_FONT, bg=LIST_COLOUR, fg=TEXT_COLOUR)  # 3. configure

# Total cost of the order
total_label = tk.Label(root)  # 1. create
total_label.grid(row=1, column=1, columnspan=2, padx=10, pady=5, sticky="w")  # 2. position
total_label.config(text="Total: $0.00", font=LABEL_FONT, bg=BG_COLOUR, fg=TEXT_COLOUR)  # 3. configure

count_label = tk.Label(root)  # 1. create
count_label.grid(row=3, column=1, columnspan=2, padx=10, pady=5, sticky="w")  # 2. position
count_label.config(text="Juices: 0", font=LABEL_FONT, bg=BG_COLOUR, fg=TEXT_COLOUR)  # 3. configure

# Remove selected button
remove_button = tk.Button(root)  # 1. create
remove_button.grid(row=4, column=1, padx=10, pady=10, ipady=4, sticky="w")  # 2. position
remove_button.config(text="Remove selected", width=14, font=BUTTON_FONT, bg=REMOVE_COLOUR, fg=TEXT_COLOUR)  # 3. configure
remove_button.config(command=remove_juice)  # 4. command

# Clear order button
clear_button = tk.Button(root)  # 1. create
clear_button.grid(row=4, column=2, padx=10, pady=10, ipady=4, sticky="e")  # 2. position
clear_button.config(text="Clear order", width=14, font=BUTTON_FONT, bg=REMOVE_COLOUR, fg=TEXT_COLOUR)  # 3. configure
clear_button.config(command=clear_juice_orders)  # 4. command


# 5. MAIN CODE
show_juice_orders()
root.mainloop()
