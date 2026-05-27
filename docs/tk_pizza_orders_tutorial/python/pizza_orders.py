import tkinter as tk
from tkinter import messagebox

# 1. DATA DICTIONARIES
# 4 options with 3 sizes each
prices = {
    "Margherita": {"Small": 5, "Medium": 7, "Large": 10},
    "Pepperoni": {"Small": 6, "Medium": 8, "Large": 11},
    "Hawaiian": {"Small": 6, "Medium": 8, "Large": 11},
    "Veggie": {"Small": 5, "Medium": 7, "Large": 10}
}

# 2. CONSTANTS & STYLES
LABEL_FONT = ("Helvetica", 12)
ENTRY_FONT = ("Helvetica", 14)
ORDER_FONT = ("Helvetica", 12)
RADIO_FONT = ("Helvetica", 12)
BUTTON_FONT = ("Helvetica", 18)

# Colors
BG_COLOR = "#f0f0f0"       # Light gray background
WHITE_BG = "#ffffff"       # Entry box background
GREEN_BG = "#c0f0c0"       # Add button & total highlights
RED_BG = "#ffdae0"         # Delete / Cancel buttons
BLUE_BG = "#93ccea"        # Quantity background

# Orders tracking list
orders = []


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
        customer_entry.config(bg=WHITE_BG)
        orders.append((customer, pizza, size, quantity))
        quantity_var.set(0)  # Reset quantity to default
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
        order_list.itemconfig(tk.END, {"bg": GREEN_BG})


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
root.configure(bg=BG_COLOR)
root.geometry("900x600")

# --- LEFT SIDE: INPUT CONTROLS ---

# Customer Name
customer_label = tk.Label(root, text="Customer Name:", font=LABEL_FONT, bg=BG_COLOR)
customer_label.grid(row=0, column=0, padx=10, pady=5, sticky="e")
customer_entry = tk.Entry(root, font=ENTRY_FONT, bg=WHITE_BG, width=20)
customer_entry.grid(row=0, column=1, padx=10, pady=5, ipady=3, sticky="w")

# Pizza Type (Radio buttons)
pizza_label = tk.Label(root, text="Pizza Type:", font=LABEL_FONT, bg=BG_COLOR)
pizza_label.grid(row=1, column=0, padx=10, pady=5, sticky="ne")
pizza_var = tk.StringVar(root)
pizza_var.set("Margherita")
pizza_var.trace_add("write", update_costs)

pizza_frame = tk.Frame(root, bg=BG_COLOR)
pizza_frame.grid(row=1, column=1, padx=10, pady=5, sticky="w")
for pizza in prices.keys():
    radio_button = tk.Radiobutton(pizza_frame, text=pizza, variable=pizza_var, value=pizza, font=RADIO_FONT, bg=BG_COLOR)
    radio_button.pack(anchor="w")

# Pizza Size (Radio buttons)
pizza_label = tk.Label(root, text="Pizza Size:", font=LABEL_FONT, bg=BG_COLOR)
pizza_label.grid(row=2, column=0, padx=10, pady=5, sticky="ne")
size_var = tk.StringVar(root)
size_var.set("Small")
size_var.trace_add("write", update_costs)

size_frame = tk.Frame(root, bg=BG_COLOR)
size_frame.grid(row=2, column=1, padx=10, pady=5, sticky="w")
for size in ["Small", "Medium", "Large"]:
    radio_button = tk.Radiobutton(size_frame, text=size, variable=size_var, value=size, font=RADIO_FONT, bg=BG_COLOR)
    radio_button.pack(anchor="w")

# Quantity (Dropdown Menu)
quanitity_label = tk.Label(root, text="Quantity:", font=LABEL_FONT, bg=BG_COLOR)
quanitity_label.grid(row=3, column=0, padx=10, pady=5, sticky="e")
quantity_var = tk.IntVar(root)
quantity_var.set(1)
quantity_var.trace_add("write", update_costs)

quantity_menu = tk.OptionMenu(root, quantity_var, 1, 2, 3, 4, 5)
quantity_menu.grid(row=3, column=1, padx=10, pady=5, sticky="w")
quantity_menu.config(bg=BLUE_BG, activebackground=BLUE_BG)

# Dynamic Price Displays
# Cost per pizza display
cost_display_var = tk.StringVar(root)
cost_display_var.set("Cost per pizza: $5")
cost_label = tk.Label(root, textvariable=cost_display_var, font=LABEL_FONT, bg=BG_COLOR)
cost_label.grid(row=4, column=1, padx=10, pady=5, sticky="w")
# order cost display
order_cost_var = tk.StringVar(root)
order_cost_var.set("Order cost: $0")
order_cost_label = tk.Label(root, textvariable=order_cost_var, font=LABEL_FONT, bg=BG_COLOR)
order_cost_label.grid(row=5, column=1, padx=10, pady=5, sticky="w")

# Action Button: Add Order
add_button = tk.Button(root, text="Add Order", command=add_order, font=BUTTON_FONT,bg=GREEN_BG, activebackground=GREEN_BG, width=15)
add_button.grid(row=6, column=1, padx=10, pady=15, ipady=5, sticky="w")


# --- RIGHT SIDE: ORDER DISPLAY & MANAGEMENT ---

# Order List Label & Listbox
orders_label = tk.Label(root, text="Current Orders:", font=LABEL_FONT, bg=BG_COLOR)
orders_label.grid(row=0, column=2, padx=10, pady=5, sticky="w")
order_list = tk.Listbox(root, font=ORDER_FONT, width=45, height=12, bg=WHITE_BG)
order_list.grid(row=1, column=2, rowspan=5, columnspan=2, padx=10, pady=5, sticky="nsew")

# Action Button: Delete Selected
delete_pizza_button = tk.Button(root, text="Delete Selected", command=delete_selected_pizza, font=BUTTON_FONT, bg=RED_BG, activebackground=RED_BG)
delete_pizza_button.grid(row=6, column=2, padx=10, pady=15, ipady=5, sticky="w")

# Action Button: Cancel All Orders
cancel_order_button = tk.Button(root, text="Cancel All Orders", command=cancel_order, font=BUTTON_FONT,bg=RED_BG, activebackground=RED_BG)
cancel_order_button.grid(row=6, column=3, padx=10, pady=15, ipady=5, sticky="e")

# 5. Main code
# Initialize price calculations display on startup
update_costs()

# Run application
root.mainloop()
