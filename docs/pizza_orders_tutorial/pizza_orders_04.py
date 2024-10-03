import tkinter as tk

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
pizza_frame = tk.Frame(root)
pizza_frame.grid(row=1, column=1, padx=10, pady=5, sticky="w")
for pizza in ["Margherita", "Pepperoni", "Hawaiian", "Veggie", "BBQ Chicken"]:
    tk.Radiobutton(pizza_frame, text=pizza, variable=pizza_var, value=pizza).pack(anchor="w")

# Pizza size
tk.Label(root, text="Pizza Size:").grid(row=2, column=0, padx=10, pady=5, sticky="e")
size_var = tk.StringVar(root)
size_var.set("Small")
size_frame = tk.Frame(root)
size_frame.grid(row=2, column=1, padx=10, pady=5, sticky="w")
for size in ["Small", "Medium", "Large"]:
    tk.Radiobutton(size_frame, text=size, variable=size_var, value=size).pack(anchor="w")

# Quantity
tk.Label(root, text="Quantity:").grid(row=3, column=0, padx=10, pady=5, sticky="e")
quantity_var = tk.StringVar(root)
quantity_var.set("1")
quantity_menu = tk.OptionMenu(root, quantity_var, "1", "2", "3", "4", "5")
quantity_menu.grid(row=3, column=1, padx=10, pady=5, sticky="w")


# Run the application
root.mainloop()
