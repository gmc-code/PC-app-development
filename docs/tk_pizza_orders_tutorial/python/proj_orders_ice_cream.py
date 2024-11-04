import tkinter as tk
from tkinter import messagebox


# Define the prices for each type of ice cream and toppings
prices = {
    "Vanilla": 3.00,
    "Chocolate": 3.50,
    "Strawberry": 3.25,
    "Mint": 3.75,
}

toppings_prices = {
    "Sprinkles": 0.50,
    "Chocolate Sauce": 0.75,
    "Caramel Sauce": 0.75,
    "Nuts": 1.00,
    "Cherry": 0.50,
}

# Style configurations
LABEL_FONT = ("Helvetica", 12)
ENTRY_FONT = ("Helvetica", 14)
ORDER_FONT = ("Helvetica", 12)
ENTRY_BG = "#ffffff"  # white
TEXT_BG = "#f0f0f0"  # Very light gray
TEXT_FG = "#000000"  # black

QUANTITY_BG = "#93ccea"  # Very soft blue
QUANTITY_HOVER_BG = "#53aede"  # soft blue

ORDER_LIST_TOTAL_BG = "#c0f0c0"  # Very soft lime green
ORDER_LIST_TOTAL_SELECTED_BG = "#5bd85b"  # moderate lime green

ADD_BUTTON_BG = "#c0f0c0"  # Very soft lime green
ADD_BUTTON_FG = "#000000"  # black
ADD_BUTTON_HOVER_BG = "#5bd85b"  # moderate lime green

DELETE_BUTTON_BG = "#ffdae0"  # very pale red
DELETE_BUTTON_FG = "#000000"  # black
DELETE_BUTTON_HOVER_BG = "#ffc1cb"  # very pale red

# Orders list
orders = []

# Costs
def update_costs(*args):
    ice_cream = ice_cream_var.get()
    quantity = quantity_var.get()
    if ice_cream:
        cost = prices[ice_cream]
        cost_display_var.set(f"Cost per item: ${cost}")
        if quantity:
            order_cost = cost * quantity
            for topping, var in toppings_vars.items():
                if var.get():
                    order_cost += toppings_prices[topping] * quantity
            order_cost_var.set(f"Order cost: ${order_cost}")


def update_costs(*args):
    ice_cream = ice_cream_var.get()
    quantity = quantity_var.get()
    if ice_cream:
        # Base cost of the selected ice cream flavor
        base_cost = prices[ice_cream]

        # Calculate the total topping cost per item
        toppings_cost = sum(toppings_prices[topping] for topping, var in toppings_vars.items() if var.get())

        # Total cost per item including toppings
        cost_per_item = base_cost + toppings_cost
        cost_display_var.set(f"Cost per item: ${cost_per_item:.2f}")

        # Total order cost based on quantity
        order_cost = cost_per_item * quantity
        order_cost_var.set(f"Order cost: ${order_cost:.2f}")


# Add order
def add_order():
    customer = customer_entry.get()
    ice_cream = ice_cream_var.get()
    quantity = quantity_var.get()
    selected_toppings = [topping for topping, var in toppings_vars.items() if var.get()]
    if not customer:
        messagebox.showerror("Input Error", "Please enter the customer name.")
        customer_entry.config(bg="pink")
        return
    else:
        customer_entry.config(bg="white")
    orders.append((customer, ice_cream, quantity, selected_toppings))
    quantity_var.set("1")
    for var in toppings_vars.values():
        var.set(False)
    update_order_list()

# Select order
def select_order(event):
    order_selection = order_list.curselection()
    if order_selection:
        order_index = order_selection[0]
        if order_index < len(orders):
            customer, ice_cream, quantity, selected_toppings = orders[order_index]
            customer_entry.delete(0, tk.END)
            customer_entry.insert(0, customer)
            ice_cream_var.set(ice_cream)
            quantity_var.set(str(quantity))
            for topping, var in toppings_vars.items():
                var.set(topping in selected_toppings)

# Delete selected ice cream
def delete_selected_ice_cream():
    order_selection = order_list.curselection()
    if not order_selection:
        messagebox.showerror("Input Error", "Please select an ice cream item to delete.")
        return
    order_index = order_selection[0]
    if order_index == order_list.size() - 1:
        messagebox.showerror("Input Error", "Cannot delete the total cost line.")
        return
    del orders[order_index]
    update_order_list()

# Cancel whole order
def cancel_order():
    orders.clear()
    update_order_list()

# Display orders
# Display orders
def update_order_list():
    order_list.delete(0, tk.END)
    total_cost = 0
    for order in orders:
        customer, ice_cream, quantity, selected_toppings = order
        base_cost = prices[ice_cream]
        toppings_cost = sum(toppings_prices[topping] for topping in selected_toppings)
        item_cost = (base_cost + toppings_cost) * quantity  # Total cost per item with quantity
        total_cost += item_cost
        order_list.insert(tk.END, f"{customer} - {quantity} {ice_cream} with {', '.join(selected_toppings)} - ${item_cost:.2f}")

    # Display total cost if there are any orders
    if orders:
        order_list.insert(tk.END, f"Total cost: ${total_cost:.2f}")
        order_list.itemconfig(order_list.size() - 1, {"bg": ORDER_LIST_TOTAL_BG, "selectbackground": ORDER_LIST_TOTAL_SELECTED_BG})

# Hover color functions
def on_enter_add(e):
    add_button.config(bg=ADD_BUTTON_HOVER_BG)

def on_leave_add(e):
    add_button.config(bg=ADD_BUTTON_BG)

def on_enter_delete(e):
    delete_ice_cream_button.config(bg=DELETE_BUTTON_HOVER_BG)

def on_leave_delete(e):
    delete_ice_cream_button.config(bg=DELETE_BUTTON_BG)

def on_enter_cancel(e):
    cancel_order_button.config(bg=DELETE_BUTTON_HOVER_BG)

def on_leave_cancel(e):
    cancel_order_button.config(bg=DELETE_BUTTON_BG)

# Create the main window
root = tk.Tk()
root.title("Ice Cream Ordering System")
root.configure(bg=TEXT_BG)
root.geometry("1080x600")

# Customer name
tk.Label(root, text="Customer Name:", font=LABEL_FONT, bg=TEXT_BG).grid(row=0, column=0, padx=10, pady=5, sticky="e")
customer_entry = tk.Entry(root, font=ENTRY_FONT, bg=ENTRY_BG, width=15)
customer_entry.grid(row=0, column=1, padx=10, pady=5, ipady=5)

# Ice cream type
tk.Label(root, text="Ice Cream Type:", font=LABEL_FONT, bg=TEXT_BG).grid(row=1, column=0, padx=10, pady=5, sticky="e")
ice_cream_var = tk.StringVar(root)
ice_cream_var.set("Vanilla")
ice_cream_var.trace_add("write", update_costs)
ice_cream_frame = tk.Frame(root, bg=TEXT_BG)
ice_cream_frame.grid(row=1, column=1, padx=10, pady=5, sticky="w")
for ice_cream in prices.keys():
    tk.Radiobutton(ice_cream_frame, text=ice_cream, variable=ice_cream_var, value=ice_cream, bg=TEXT_BG).pack(anchor="w")

# Quantity
tk.Label(root, text="Quantity:", font=LABEL_FONT, bg=TEXT_BG).grid(row=2, column=0, padx=10, pady=5, sticky="e")
quantity_var = tk.StringVar(root)
quantity_var.set("1")
quantity_var.trace_add("write", update_costs)
quantity_menu = tk.OptionMenu(root, quantity_var, "1", "2", "3", "4", "5")
quantity_menu.grid(row=2, column=1, padx=10, pady=5, sticky="w")
quantity_menu.config(bg=QUANTITY_BG, fg=TEXT_FG, activebackground=QUANTITY_HOVER_BG, activeforeground=TEXT_FG)
quantity_menu["menu"].config(bg=QUANTITY_BG, fg=TEXT_FG)

# Toppings
tk.Label(root, text="Toppings:", font=LABEL_FONT, bg=TEXT_BG).grid(row=3, column=0, padx=10, pady=5, sticky="e")
toppings_frame = tk.Frame(root, bg=TEXT_BG)
toppings_frame.grid(row=3, column=1, padx=10, pady=5, sticky="w")
toppings_vars = {}
for topping in toppings_prices.keys():
    var = tk.BooleanVar()
    var.trace_add("write", update_costs)  # Update costs when topping is selected/deselected
    tk.Checkbutton(toppings_frame, text=topping, variable=var, bg=TEXT_BG).pack(anchor="w")
    toppings_vars[topping] = var

# Cost per item display
cost_display_var = tk.StringVar(root)
cost_display_var.set("Cost per item: $0")
tk.Label(root, textvariable=cost_display_var, font=LABEL_FONT, bg=TEXT_BG).grid(row=4, column=1, padx=10, pady=5, sticky="w")

# Order cost display
order_cost_var = tk.StringVar(root)
order_cost_var.set("Order cost: $0")
tk.Label(root, textvariable=order_cost_var, font=LABEL_FONT, bg=TEXT_BG).grid(row=5, column=1, padx=10, pady=5, sticky="w")

# Add order button
add_button = tk.Button(root, text="Add Order", command=add_order, bg=ADD_BUTTON_BG, fg=ADD_BUTTON_FG, activebackground=ADD_BUTTON_HOVER_BG)
add_button.grid(row=6, column=1, padx=10, pady=10, ipadx=20, ipady=10, sticky="w")
add_button.bind("<Enter>", on_enter_add)
add_button.bind("<Leave>", on_leave_add)

# Orders list
tk.Label(root, text="Orders:", font=LABEL_FONT, bg=TEXT_BG).grid(row=0, column=2, padx=10, pady=5, sticky="w")
order_list = tk.Listbox(root, font=ORDER_FONT, width=80, bg=ENTRY_BG)
order_list.grid(row=1, column=2, rowspan=5, columnspan=2, padx=10, pady=5, sticky="nsew")
order_list.bind("<<ListboxSelect>>", select_order)

# Delete selected ice cream button
delete_ice_cream_button = tk.Button(root, text="Delete Selected Ice Cream", command=delete_selected_ice_cream, bg=DELETE_BUTTON_BG, fg=DELETE_BUTTON_FG, activebackground=DELETE_BUTTON_HOVER_BG)
delete_ice_cream_button.grid(row=6, column=2, padx=10, ipadx=20, ipady=10, pady=5, sticky="w")
delete_ice_cream_button.bind("<Enter>", on_enter_delete)
delete_ice_cream_button.bind("<Leave>", on_leave_delete)

# Cancel whole order button
cancel_order_button = tk.Button(root, text="Cancel Orders", command=cancel_order, bg=DELETE_BUTTON_BG, fg=DELETE_BUTTON_FG, activebackground=DELETE_BUTTON_HOVER_BG)
cancel_order_button.grid(row=6, column=3, padx=10, ipadx=20, ipady=10, pady=5, sticky="w")
cancel_order_button.bind("<Enter>", on_enter_cancel)
cancel_order_button.bind("<Leave>", on_leave_cancel)

# Run the application
root.mainloop()
