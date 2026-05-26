import tkinter as tk

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
pizza_var = tk.StringVar(root, value="Margherita")


pizza_frame = tk.Frame(root)
pizza_frame.grid(row=1, column=1, padx=10, pady=5, sticky="w")
for pizza in ["Margherita", "Pepperoni", "Hawaiian", "Veggie"]:
    radio_button = tk.Radiobutton(pizza_frame, text=pizza, variable=pizza_var, value=pizza)
    radio_button.pack(anchor="w")


# Pizza Size (Radio buttons)
pizza_label = tk.Label(root, text="Pizza Size:")
pizza_label.grid(row=2, column=0, padx=10, pady=5, sticky="ne")
size_var = tk.StringVar(root)
size_var.set("Small")

size_frame = tk.Frame(root)
size_frame.grid(row=2, column=1, padx=10, pady=5, sticky="w")
for size in ["Small", "Medium", "Large"]:
    radio_button = tk.Radiobutton(size_frame, text=size, variable=size_var, value=size)
    radio_button.pack(anchor="w")


# Quantity (Dropdown Menu)
quanitity_label = tk.Label(root, text="Quantity:")
quanitity_label.grid(row=3, column=0, padx=10, pady=5, sticky="e")
quantity_var = tk.IntVar(root)
quantity_var.set(0)

quantity_menu = tk.OptionMenu(root, quantity_var, 0, 1, 2, 3, 4, 5)
quantity_menu.grid(row=3, column=1, padx=10, pady=5, sticky="w")


# Run the application
root.mainloop()
