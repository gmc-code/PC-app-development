import tkinter as tk
from tkinter import messagebox

# Define the prices for each T-shirt type
prices = {
    "Plain": {"Small": 10, "Medium": 12, "Large": 15},
    "Graphic": {"Small": 12, "Medium": 15, "Large": 18},
    "Custom Print": {"Small": 15, "Medium": 18, "Large": 22},
    "Sports": {"Small": 13, "Medium": 16, "Large": 20},
    "Vintage": {"Small": 14, "Medium": 17, "Large": 21},
}

# Style configurations
LABEL_FONT = ("Helvetica", 12)
ENTRY_FONT = ("Helvetica", 14)
ORDER_FONT = ("Helvetica", 12)
ENTRY_BG = "#ffffff"
TEXT_BG = "#f0f0f0"
TEXT_FG = "#000000"

QUANTITY_BG = "#93ccea"
QUANTITY_HOVER_BG = "#53aede"

ORDER_LIST_TOTAL_BG = "#c0f0c0"
ORDER_LIST_TOTAL_SELECTED_BG = "#5bd85b"

ADD_BUTTON_BG = "#c0f0c0"
ADD_BUTTON_FG = "#000000"
ADD_BUTTON_HOVER_BG = "#5bd85b"

DELETE_BUTTON_BG = "#ffdae0"
DELETE_BUTTON_FG = "#000000"
DELETE_BUTTON_HOVER_BG = "#ffc1cb"

# Orders list
orders = []

# Costs
def update_costs(*args):
    tshirt_type = tshirt_var.get()
    size = size_var.get()
    quantity = quantity_var.get()
    if tshirt_type and size:
        cost = prices[tshirt_type][size]
        cost_display_var.set(f"Cost per T-shirt: ${cost}")
        if quantity:
            order_cost = cost * quantity
            order_cost_var.set(f"Order cost: ${order_cost}")

# Add order
def add_order():
    customer = customer_entry.get()
    tshirt_type = tshirt_var.get()
    size = size_var.get()
    quantity = quantity_var.get()
    if not customer:
        messagebox.showerror("Input Error", "Please enter the customer name.")
        customer_entry.config(bg="pink")
        return
    else:
        customer_entry.config(bg="white")
    orders.append((customer, tshirt_type, size, quantity))
    quantity_var.set("1")
    update_order_list()

# Select order
def select_order(event):
    order_selection = order_list.curselection()
    if order_selection:
        order_index = order_selection[0]
        if order_index < len(orders):
            customer, tshirt_type, size, quantity = orders[order_index]
            customer_entry.delete(0, tk.END)
            customer_entry.insert(0, customer)
            tshirt_var.set(tshirt_type)
            size_var.set(size)
            quantity_var.set(str(quantity))

# Delete selected T-shirt
def delete_selected_tshirt():
    order_selection = order_list.curselection()
    if not order_selection:
        messagebox.showerror("Input Error", "Please select a T-shirt to delete.")
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
        customer, tshirt_type, size, quantity = order
        cost = prices[tshirt_type][size] * quantity
        total_cost += cost
        order_list.insert(tk.END, f"{customer} - {quantity} {size} {tshirt_type} - ${cost}")
    if orders:
        order_list.insert(tk.END, f"Total cost: ${total_cost}")
        order_list.itemconfig(order_list.size() - 1, {"bg": ORDER_LIST_TOTAL_BG, "selectbackground": ORDER_LIST_TOTAL_SELECTED_BG})

# Button hover functions
def on_enter_add(event):
    add_button.config(bg=ADD_BUTTON_HOVER_BG)

def on_leave_add(event):
    add_button.config(bg=ADD_BUTTON_BG)

def on_enter_delete(event):
    delete_tshirt_button.config(bg=DELETE_BUTTON_HOVER_BG)

def on_leave_delete(event):
    delete_tshirt_button.config(bg=DELETE_BUTTON_BG)

def on_enter_cancel(event):
    cancel_order_button.config(bg=DELETE_BUTTON_HOVER_BG)

def on_leave_cancel(event):
    cancel_order_button.config(bg=DELETE_BUTTON_BG)

# Create the main window
root = tk.Tk()
root.title("T-Shirt Ordering System")
root.configure(bg=TEXT_BG)
root.geometry("900x600")

# Customer name
tk.Label(root, text="Customer Name:", font=LABEL_FONT, bg=TEXT_BG).grid(row=0, column=0, padx=10, pady=5, sticky="e")
customer_entry = tk.Entry(root, font=ENTRY_FONT, bg=ENTRY_BG, width=20)
customer_entry.grid(row=0, column=1, padx=10, pady=5, ipady=5)

# T-shirt type
tk.Label(root, text="T-Shirt Type:", font=LABEL_FONT, bg=TEXT_BG).grid(row=1, column=0, padx=10, pady=5, sticky="e")
tshirt_var = tk.StringVar(root)
tshirt_var.set("Plain")
tshirt_var.trace_add("write", update_costs)
tshirt_frame = tk.Frame(root, bg=TEXT_BG)
tshirt_frame.grid(row=1, column=1, padx=10, pady=5, sticky="w")
for tshirt_type in prices.keys():
    tk.Radiobutton(tshirt_frame, text=tshirt_type, variable=tshirt_var, value=tshirt_type, bg=TEXT_BG).pack(anchor="w")

# T-shirt size
tk.Label(root, text="Size:", font=LABEL_FONT, bg=TEXT_BG).grid(row=2, column=0, padx=10, pady=5, sticky="e")
size_var = tk.StringVar(root)
size_var.set("Small")
size_var.trace_add("write", update_costs)
size_frame = tk.Frame(root, bg=TEXT_BG)
size_frame.grid(row=2, column=1, padx=10, pady=5, sticky="w")
for size in ["Small", "Medium", "Large"]:
    tk.Radiobutton(size_frame, text=size, variable=size_var, value=size, bg=TEXT_BG).pack(anchor="w")

# Quantity
tk.Label(root, text="Quantity:", font=LABEL_FONT, bg=TEXT_BG).grid(row=3, column=0, padx=10, pady=5, sticky="e")
quantity_var = tk.StringVar(root)
quantity_var.set("1")
quantity_var.trace_add("write", update_costs)
quantity_menu = tk.OptionMenu(root, quantity_var, "1", "2", "3", "4", "5")
quantity_menu.grid(row=3, column=1, padx=10, pady=5, sticky="w")
quantity_menu.config(bg=QUANTITY_BG, fg=TEXT_FG, activebackground=QUANTITY_HOVER_BG, activeforeground=TEXT_FG)
quantity_menu["menu"].config(bg=QUANTITY_BG, fg=TEXT_FG)

# Cost per T-shirt display
cost_display_var = tk.StringVar(root)
cost_display_var.set("Cost per T-shirt: $0")
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
order_list = tk.Listbox(root, font=ORDER_FONT, width=50, bg=ENTRY_BG)
order_list.grid(row=1, column=2, rowspan=5, columnspan=2, padx=10, pady=5, sticky="nsew")
order_list.bind("<<ListboxSelect>>", select_order)

# Delete selected T-shirt button
delete_tshirt_button = tk.Button(root, text="Delete Selected T-shirt", command=delete_selected_tshirt, bg=DELETE_BUTTON_BG, fg=DELETE_BUTTON_FG, activebackground=DELETE_BUTTON_HOVER_BG)
delete_tshirt_button.grid(row=6, column=2, padx=10, pady=5, ipadx=20, ipady=10, sticky="w")
delete_tshirt_button.bind("<Enter>", on_enter_delete)
delete_tshirt_button.bind("<Leave>", on_leave_delete)

# Cancel whole order button
cancel_order_button = tk.Button(root, text="Cancel Orders", command=cancel_order, bg=DELETE_BUTTON_BG, fg=DELETE_BUTTON_FG, activebackground=DELETE_BUTTON_HOVER_BG)
cancel_order_button.grid(row=6, column=3, padx=10, pady=5, ipadx=20, ipady=10, sticky="w")
cancel_order_button.bind("<Enter>", on_enter_cancel)
cancel_order_button.bind("<Leave>", on_leave_cancel)

# Run the application
root.mainloop()
