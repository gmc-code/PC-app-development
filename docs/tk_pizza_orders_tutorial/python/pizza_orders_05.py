import tkinter as tk

# Define the prices for each pizza size
prices = {
    "Margherita": {"Small": 5, "Medium": 7, "Large": 10},
    "Pepperoni": {"Small": 6, "Medium": 8, "Large": 11},
    "Hawaiian": {"Small": 6, "Medium": 8, "Large": 11},
    "Veggie": {"Small": 5, "Medium": 7, "Large": 10},
    "BBQ Chicken": {"Small": 7, "Medium": 9, "Large": 12},
}


# Costs
def update_costs(*args):
    pizza = pizza_var.get()
    size = size_var.get()
    quantity = quantity_var.get()
    if pizza and size:
        cost = prices[pizza][size]
        cost_display_var.set(f"Cost per pizza: ${cost}")
        if quantity:
            order_cost = cost * quantity
            order_cost_var.set(f"Order cost: ${order_cost}")


# Create the main window
root = tk.Tk()
root.title("Pizza Ordering System")
root.geometry("900x600")

# Customer name
tk.Label(root, text="Customer Name:").grid(row=0, column=0, padx=10, pady=5)
customer_entry = tk.Entry(root)
customer_entry.grid(row=0, column=1, padx=10, pady=5)

# Pizza type
tk.Label(root, text="Pizza Type:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
pizza_var = tk.StringVar(root)
pizza_var.set("Margherita")
pizza_var.trace_add("write", update_costs)
pizza_frame = tk.Frame(root)
pizza_frame.grid(row=1, column=1, padx=10, pady=5, sticky="w")
for pizza in ["Margherita", "Pepperoni", "Hawaiian", "Veggie", "BBQ Chicken"]:
    tk.Radiobutton(pizza_frame, text=pizza, variable=pizza_var, value=pizza).pack(anchor="w")

# Pizza size
tk.Label(root, text="Pizza Size:").grid(row=2, column=0, padx=10, pady=5, sticky="e")
size_var = tk.StringVar(root)
size_var.set("Small")
size_var.trace_add("write", update_costs)
size_frame = tk.Frame(root)
size_frame.grid(row=2, column=1, padx=10, pady=5, sticky="w")
for size in ["Small", "Medium", "Large"]:
    tk.Radiobutton(size_frame, text=size, variable=size_var, value=size).pack(anchor="w")

# Quantity
tk.Label(root, text="Quantity:").grid(row=3, column=0, padx=10, pady=5, sticky="e")
quantity_var = tk.StringVar(root)
quantity_var.set("1")
quantity_var.trace_add("write", update_costs)
quantity_menu = tk.OptionMenu(root, quantity_var, "1", "2", "3", "4", "5")
quantity_menu.grid(row=3, column=1, padx=10, pady=5, sticky="w")

# Cost per pizza display
cost_display_var = tk.StringVar(root)
cost_display_var.set("Cost per pizza: $0")
tk.Label(root, textvariable=cost_display_var).grid(row=4, column=1, padx=10, pady=5, sticky="w")

# Order cost display
order_cost_var = tk.StringVar(root)
order_cost_var.set("Order cost: $0")
tk.Label(root, textvariable=order_cost_var).grid(row=5, column=1, padx=10, pady=5, sticky="w")


# Run the application
root.mainloop()
