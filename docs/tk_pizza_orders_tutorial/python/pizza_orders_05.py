import tkinter as tk

# 1. DATA DICTIONARIES & LISTS
# options with size
prices = {
    "Margherita": {"Small": 8, "Medium": 12, "Large": 15},
    "Pepperoni": {"Small": 9, "Medium": 13, "Large": 17},
    "Hawaiian": {"Small": 10, "Medium": 14, "Large": 18},
    "Veggie": {"Small": 9, "Medium": 12, "Large": 16}
}

# 2. CONSTANTS & STYLES


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


# 4. TKINTER WIDGETS
# Create the main window
root = tk.Tk()
root.title("Pizza Ordering System")
root.geometry("900x600")

# Customer Name
customer_label = tk.Label(root, text="Customer Name:")
customer_label.grid(row=0, column=0, padx=10, pady=5, sticky="e")

customer_entry = tk.Entry(root, width=20)
customer_entry.grid(row=0, column=1, padx=10, pady=5, ipady=3, sticky="w")

# Pizza Type (Radio buttons)
pizza_label = tk.Label(root, text="Pizza Type:")
pizza_label.grid(row=1, column=0, padx=10, pady=5, sticky="ne")

pizza_var = tk.StringVar(root)
pizza_var.set("Margherita")
pizza_var.trace_add("write", update_costs)

pizza_frame = tk.Frame(root)
pizza_frame.grid(row=1, column=1, padx=10, pady=5, sticky="w")

for pizza in ["Margherita", "Pepperoni", "Hawaiian", "Veggie"]:
    radio_button = tk.Radiobutton(
        pizza_frame, text=pizza, variable=pizza_var, value=pizza)
    radio_button.pack(anchor="w")

# Pizza Size (Radio buttons)
size_label = tk.Label(root, text="Pizza Size:")
size_label.grid(row=2, column=0, padx=10, pady=5, sticky="ne")

size_var = tk.StringVar(root)
size_var.set("Small")
size_var.trace_add("write", update_costs)

size_frame = tk.Frame(root)
size_frame.grid(row=2, column=1, padx=10, pady=5, sticky="w")

for size in ["Small", "Medium", "Large"]:
    radio_button = tk.Radiobutton(
        size_frame, text=size, variable=size_var, value=size)
    radio_button.pack(anchor="w")

# Quantity (Dropdown Menu)
quanitity_label = tk.Label(root, text="Quantity:")
quanitity_label.grid(row=3, column=0, padx=10, pady=5, sticky="e")

quantity_var = tk.IntVar(root)
quantity_var.set(1)
quantity_var.trace_add("write", update_costs)

quantity_menu = tk.OptionMenu(root, quantity_var, 1, 2, 3, 4, 5, 6)
quantity_menu.grid(row=3, column=1, padx=10, pady=5, sticky="w")

# Dynamic Price Displays
# Cost per pizza display
cost_display_var = tk.StringVar(root)
cost_display_var.set("Cost per pizza: $8")

cost_label = tk.Label(root, textvariable=cost_display_var)
cost_label.grid(row=4, column=1, padx=10, pady=5, sticky="w")

# order cost display
order_cost_var = tk.StringVar(root)
order_cost_var.set("Order cost: $8")

order_cost_label = tk.Label(root, textvariable=order_cost_var)
order_cost_label.grid(row=5, column=1, padx=10, pady=5, sticky="w")


# 5. MAIN CODE
# Run the application
root.mainloop()