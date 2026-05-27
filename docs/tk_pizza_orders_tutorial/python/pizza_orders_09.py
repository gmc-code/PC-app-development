import tkinter as tk
from tkinter import messagebox


# 1. DATA DICTIONARIES & LISTS
# options with size
prices = {
    "Margherita": {"Small": 8, "Medium": 12, "Large": 15},
    "Veggie": {"Small": 9, "Medium": 12, "Large": 16},
    "Pepperoni": {"Small": 9, "Medium": 13, "Large": 17},
    "Hawaiian": {"Small": 10, "Medium": 14, "Large": 18},
    "Capriciossa": {"Small": 10, "Medium": 14, "Large": 18},
    "Mexican": {"Small": 10, "Medium": 14, "Large": 18},
    "BBQ Chicken": {"Small": 11, "Medium": 15, "Large": 19},
    "Meat Lovers": {"Small": 11, "Medium": 15, "Large": 19}
}

# Orders tracking list
orders = []


# 2. CONSTANTS & STYLES
# Fonts
LABEL_FONT = ("Helvetica", 12)
ENTRY_FONT = ("Helvetica", 14)
ORDER_FONT = ("Helvetica", 12)
RADIO_FONT = ("Helvetica", 12)
BUTTON_FONT = ("Helvetica", 14)  # Adjusted slightly for clean layout grid scaling

# Colors
BG_COLOR = "#f0f0f0"       # Light gray background
ENTRY_BG = "#ffffff"       # Entry box background
LIST_BG = "#ffffff"        # Listbox background
TOTAL_BG = "#c0f0c0"       # Total highlights
ADD_BG = "#c0f0c0"         # Add button
DELETE_BG = "#ffdae0"      # Delete / Cancel buttons
QUANTITY_BG = "#93ccea"    # Quantity background


# 3. DEFINITIONS / FUNCTIONS
def update_costs(*args):
    """Calculates and updates the real-time cost feedback labels."""
    pizza = pizza_var.get()
    size = size_var.get()
    quantity = quantity_var.get()

    if pizza and size:
        cost = prices[pizza][size]
        cost_display_var.set(f"Cost per pizza: ${cost}")
        order_cost_var.set(f"Order cost: ${cost * quantity}")


def add_order():
    """Validates input and adds the current selection to the order list."""
    customer = customer_entry.get()
    pizza = pizza_var.get()
    size = size_var.get()
    quantity = quantity_var.get()

    if not customer:
        messagebox.showerror("Input Error", "Please enter the customer name.")
        customer_entry.config(bg="pink")
    else:
        customer_entry.config(bg=ENTRY_BG)
        orders.append((customer, pizza, size, quantity))
        quantity_var.set(1)  # Reset quantity to default
        update_order_list()


def update_order_list():
    """Refreshes the listbox display and recalculates total cost."""
    order_list.delete(0, tk.END)
    total_cost = 0

    for order in orders:
        customer, pizza, size, quantity = order
        cost = prices[pizza][size] * quantity
        total_cost += cost
        order_list.insert(tk.END, f"{customer} - {quantity} {size} {pizza} - ${cost}")

    if orders:
        order_list.insert(tk.END, f"Total cost: ${total_cost}")
        # Color code the very last row (Total Cost line)
        # Get the index number of the very last item we just added
        last_row_index = tk.END
        order_list.itemconfig(last_row_index, bg=TOTAL_BG)


def delete_selected_pizza():
    """Removes the selected item from the order list."""
    order_selection = order_list.curselection()
    if not order_selection:
        messagebox.showerror("Input Error", "Please select a pizza to delete.")
    else:
        order_index = order_selection[0]
        # Block deleting the dynamic total line
        if order_index == order_list.size() - 1:
            messagebox.showerror("Input Error", "Cannot delete the total cost line.")
        else:
            del orders[order_index]
            update_order_list()


def cancel_order():
    """Clears all orders."""
    orders.clear()
    update_order_list()


# 4. TKINTER WIDGETS
# Create the main window
root = tk.Tk()
root.title("Pizza Ordering System")
root.geometry("900x600")
root.configure(bg=BG_COLOR)

# --- LEFT SIDE: SELECTIONS ---

# Customer Name
customer_label = tk.Label(root, text="Customer Name:")
customer_label.grid(row=0, column=0, padx=10, pady=5, sticky="e")
customer_label.config(font=LABEL_FONT, bg=BG_COLOR)

customer_entry = tk.Entry(root, width=20)
customer_entry.grid(row=0, column=1, padx=10, pady=5, ipady=3, sticky="w")
customer_entry.config(font=ENTRY_FONT, bg=ENTRY_BG)

# Pizza Type (Radio buttons)
pizza_label = tk.Label(root, text="Pizza Type:")
pizza_label.grid(row=1, column=0, padx=10, pady=5, sticky="ne")
pizza_label.config(font=LABEL_FONT, bg=BG_COLOR)

pizza_var = tk.StringVar(root)
pizza_var.set("Margherita")
pizza_var.trace_add("write", update_costs)

pizza_frame = tk.Frame(root)
pizza_frame.grid(row=1, column=1, padx=10, pady=5, sticky="w")
pizza_frame.config(bg=BG_COLOR)

for pizza in prices.keys():
    radio_button = tk.Radiobutton(pizza_frame, text=pizza, variable=pizza_var, value=pizza)
    radio_button.pack(anchor="w")
    radio_button.config(font=RADIO_FONT, bg=BG_COLOR)

# Pizza Size (Radio buttons)
size_label = tk.Label(root, text="Pizza Size:")
size_label.grid(row=2, column=0, padx=10, pady=5, sticky="ne")
size_label.config(font=LABEL_FONT, bg=BG_COLOR)

size_var = tk.StringVar(root)
size_var.set("Small")
size_var.trace_add("write", update_costs)

size_frame = tk.Frame(root)
size_frame.grid(row=2, column=1, padx=10, pady=5, sticky="w")
size_frame.config(bg=BG_COLOR)

for size in ["Small", "Medium", "Large"]:
    radio_button = tk.Radiobutton(size_frame, text=size, variable=size_var, value=size)
    radio_button.pack(anchor="w")
    radio_button.config(font=RADIO_FONT, bg=BG_COLOR)

# Quantity (Dropdown Menu)
quantity_label = tk.Label(root, text="Quantity:")
quantity_label.grid(row=3, column=0, padx=10, pady=5, sticky="e")
quantity_label.config(font=LABEL_FONT, bg=BG_COLOR)

quantity_var = tk.IntVar(root)
quantity_var.set(1)
quantity_var.trace_add("write", update_costs)

quantity_menu = tk.OptionMenu(root, quantity_var, 1, 2, 3, 4, 5, 6)
quantity_menu.grid(row=3, column=1, padx=10, pady=5, sticky="w")
quantity_menu.config(bg=QUANTITY_BG, activebackground=QUANTITY_BG)
quantity_menu["menu"].config(bg=QUANTITY_BG)  # for menu items

# Dynamic Price Displays
# Cost per pizza display
cost_display_var = tk.StringVar(root)
cost_display_var.set("Cost per pizza: $8")

cost_label = tk.Label(root, textvariable=cost_display_var)
cost_label.grid(row=4, column=1, padx=10, pady=5, sticky="w")
cost_label.config(font=LABEL_FONT, bg=BG_COLOR)

# order cost display
order_cost_var = tk.StringVar(root)
order_cost_var.set("Order cost: $8")

order_cost_label = tk.Label(root, textvariable=order_cost_var)
order_cost_label.grid(row=5, column=1, padx=10, pady=5, sticky="w")
order_cost_label.config(font=LABEL_FONT, bg=BG_COLOR)

# Action Button: Add Order
add_button = tk.Button(root, text="Add Order", command=add_order, width=15)
add_button.grid(row=6, column=1, padx=10, pady=15, ipady=5, sticky="w")
add_button.config(font=BUTTON_FONT, bg=ADD_BG)


# --- RIGHT SIDE: ORDER DISPLAY & MANAGEMENT ---

# Order List Label & Listbox
orders_label = tk.Label(root, text="Current Orders:")
orders_label.grid(row=0, column=2, padx=10, pady=5, sticky="w")
orders_label.config(font=LABEL_FONT, bg=BG_COLOR)

order_list = tk.Listbox(root, width=45, height=12)
order_list.grid(row=1, column=2, rowspan=5, columnspan=2, padx=10, pady=5, sticky="nsew")
order_list.config(font=ORDER_FONT, bg=LIST_BG, activestyle="none", highlightthickness=0)

# Action Button: Delete Selected
delete_pizza_button = tk.Button(root, text="Delete Selected", command=delete_selected_pizza)
delete_pizza_button.grid(row=6, column=2, padx=10, pady=15, ipady=5, sticky="w")
delete_pizza_button.config(font=BUTTON_FONT, bg=DELETE_BG)

# Action Button: Cancel All Orders
cancel_order_button = tk.Button(root, text="Cancel All Orders", command=cancel_order)
cancel_order_button.grid(row=6, column=3, padx=10, pady=15, ipady=5, sticky="e")
cancel_order_button.config(font=BUTTON_FONT, bg=DELETE_BG)


# 5. MAIN CODE
# Run the application
root.mainloop()
