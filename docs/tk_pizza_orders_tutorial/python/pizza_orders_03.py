import tkinter as tk

# 1. DATA DICTIONARIES & LISTS

# 2. CONSTANTS & STYLES

# 3. DEFINITIONS / FUNCTIONS

# 4. TKINTER WIDGETS
# Create the main window
root = tk.Tk()
root.title("Pizza Ordering System")
root.geometry("900x700")

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

pizza_frame = tk.Frame(root)
pizza_frame.grid(row=1, column=1, padx=10, pady=5, sticky="w")

for pizza in ["Margherita", "Pepperoni", "Hawaiian", "Veggie"]:
    radio_button = tk.Radiobutton(pizza_frame, text=pizza, variable=pizza_var, value=pizza)
    radio_button.pack(anchor="w")


# 5. MAIN CODE
# Run the application
root.mainloop()
