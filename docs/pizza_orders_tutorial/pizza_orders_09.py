import tkinter as tk
from tkinter import messagebox

# Define the prices for each pizza size
prices = {
    "Margherita": {"Small": 5, "Medium": 7, "Large": 10},
    "Pepperoni": {"Small": 6, "Medium": 8, "Large": 11},
    "Hawaiian": {"Small": 6, "Medium": 8, "Large": 11},
    "Veggie": {"Small": 5, "Medium": 7, "Large": 10},
    "BBQ Chicken": {"Small": 7, "Medium": 9, "Large": 12},
    "Meat Lovers": {"Small": 7, "Medium": 9, "Large": 12},
    "Capriciossa": {"Small": 6, "Medium": 8, "Large": 11},
    "Mexican": {"Small": 6, "Medium": 8, "Large": 11},
}

# Style configurations
label_font = ("Helvetica", 12)
entry_font = ("Helvetica", 14)
entry_bg = "#ffffff"  # white
text_bg = "#f0f0f0"  # Very light gray
text_fg = "#000000"  # black

quantity_bg = "#93ccea"  # Very soft blue
quantity_hover_bg = "#53aede"  # soft blue

order_list_total_bg = "#c0f0c0"  # Very soft lime green
order_list_total_selected_bg = "#5bd85b"  # moderate lime green

add_button_bg = "#c0f0c0"  # Very soft lime green
add_button_fg = "#000000"  # black
add_button_hover_bg = "#5bd85b"  # moderate lime green

delete_button_bg = "#ffdae0"  # very pale red
delete_button_fg = "#000000"  # black
delete_button_hover_bg = "#ffc1cb"  # very pale red


# orders
orders = []


# Costs
def update_costs(*args):
    pizza = pizza_var.get()
    size = size_var.get()
    quantity = int(quantity_var.get())
    if pizza and size:
        cost = prices[pizza][size]
        cost_display_var.set(f"Cost per pizza: ${cost}")
        if quantity:
            order_cost = cost * quantity
            order_cost_var.set(f"Order cost: ${order_cost}")


# order
def add_order():
    customer = customer_entry.get()
    pizza = pizza_var.get()
    size = size_var.get()
    quantity = int(quantity_var.get())
    if not customer:
        messagebox.showerror("Input Error", "Please enter the customer name.")
        customer_entry.config(bg="pink")
        return
    else:
        customer_entry.config(bg="white")
    orders.append((customer, pizza, size, quantity))
    quantity_var.set("1")
    update_order_list()


# Select order
def select_order(event):
    order_selection = order_list.curselection()
    if order_selection:
        order_index = order_selection[0]
        if order_index < len(orders):
            customer, pizza, size, quantity = orders[order_index]
            customer_entry.delete(0, tk.END)
            customer_entry.insert(0, customer)
            pizza_var.set(pizza)
            size_var.set(size)
            quantity_var.set(str(quantity))


# Delete selected pizza
def delete_selected_pizza():
    order_selection = order_list.curselection()
    if not order_selection:
        messagebox.showerror("Input Error", "Please select a pizza to delete.")
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
def update_order_list():
    order_list.delete(0, tk.END)
    total_cost = 0
    for order in orders:
        customer, pizza, size, quantity = order
        cost = prices[pizza][size] * quantity
        total_cost += cost
        order_list.insert(tk.END, f"{customer} ordered {quantity} {size} {pizza}(s) - ${cost}")
    if orders:
        order_list.insert(tk.END, f"Total cost: ${total_cost}")
        # add color to last line of order list for total
        order_list.itemconfig(order_list.size() - 1, {"bg": order_list_total_bg, "selectbackground": order_list_total_selected_bg})


# Create the main window
root = tk.Tk()
root.title("Pizza Ordering System")
root.configure(bg=text_bg)
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
for pizza in prices.keys():
    tk.Radiobutton(pizza_frame, text=pizza, variable=pizza_var, value=pizza, bg=text_bg).pack(anchor="w")

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

# Add order button
add_button = tk.Button(root, text="Add Order", command=add_order)
add_button.grid(row=6, column=1, padx=10, pady=10, ipadx=20, ipady=10, sticky="w")

# Orders list
tk.Label(root, text="Orders:").grid(row=0, column=2, padx=10, pady=5, sticky="w")
order_list = tk.Listbox(root, width=50, bg=entry_bg)
order_list.grid(row=1, column=2, rowspan=5, columnspan=2, padx=10, pady=5, sticky="nsew")
# add for reselectings chosen options:
order_list.bind('<<ListboxSelect>>', select_order)

# Delete selected pizza button
delete_pizza_button = tk.Button(root, text="Delete Selected Pizza", command=delete_selected_pizza)
delete_pizza_button.grid(row=6, column=2, padx=10, ipadx=20, ipady=10, pady=5, sticky="w")

# Cancel whole order button
cancel_order_button = tk.Button(root, text="Cancel Orders", command=cancel_order)
cancel_order_button.grid(row=6, column=3, padx=10, ipadx=20, ipady=10, pady=5, sticky="w")

# Run the application
root.mainloop()
