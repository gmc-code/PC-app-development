import tkinter as tk
from tkinter import messagebox

# Define the prices for each type of event ticket
prices = {
    "Concert": {"VIP": 150, "Regular": 100, "Student": 80},
    "Theater": {"VIP": 120, "Regular": 80, "Student": 60},
    "Sporting Event": {"VIP": 200, "Regular": 150, "Student": 100},
    "Festival": {"VIP": 180, "Regular": 120, "Student": 90},
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
    event = event_var.get()
    ticket_type = ticket_var.get()
    quantity = quantity_var.get()
    if event and ticket_type:
        cost = prices[event][ticket_type]
        cost_display_var.set(f"Cost per ticket: ${cost}")
        if quantity:
            order_cost = cost * quantity
            order_cost_var.set(f"Order cost: ${order_cost}")

# Add order
def add_order():
    customer = customer_entry.get()
    event = event_var.get()
    ticket_type = ticket_var.get()
    quantity = quantity_var.get()
    if not customer:
        messagebox.showerror("Input Error", "Please enter the customer name.")
        customer_entry.config(bg="pink")
        return
    else:
        customer_entry.config(bg="white")
    orders.append((customer, event, ticket_type, quantity))
    quantity_var.set("1")
    update_order_list()

# Select order
def select_order(event):
    order_selection = order_list.curselection()
    if order_selection:
        order_index = order_selection[0]
        if order_index < len(orders):
            customer, event, ticket_type, quantity = orders[order_index]
            customer_entry.delete(0, tk.END)
            customer_entry.insert(0, customer)
            event_var.set(event)
            ticket_var.set(ticket_type)
            quantity_var.set(str(quantity))

# Delete selected ticket
def delete_selected_ticket():
    order_selection = order_list.curselection()
    if not order_selection:
        messagebox.showerror("Input Error", "Please select a ticket item to delete.")
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
        customer, event, ticket_type, quantity = order
        cost = prices[event][ticket_type] * quantity
        total_cost += cost
        order_list.insert(tk.END, f"{customer} - {quantity} {ticket_type} tickets for {event} - ${cost}")
    if orders:
        order_list.insert(tk.END, f"Total cost: ${total_cost}")
        order_list.itemconfig(order_list.size() - 1, {"bg": ORDER_LIST_TOTAL_BG, "selectbackground": ORDER_LIST_TOTAL_SELECTED_BG})

# Hover color functions
def on_enter_add(event):
    add_button.config(bg=ADD_BUTTON_HOVER_BG)

def on_leave_add(event):
    add_button.config(bg=ADD_BUTTON_BG)

def on_enter_delete(event):
    delete_ticket_button.config(bg=DELETE_BUTTON_HOVER_BG)

def on_leave_delete(event):
    delete_ticket_button.config(bg=DELETE_BUTTON_BG)

def on_enter_cancel(event):
    cancel_order_button.config(bg=DELETE_BUTTON_HOVER_BG)

def on_leave_cancel(event):
    cancel_order_button.config(bg=DELETE_BUTTON_BG)

# Create the main window
root = tk.Tk()
root.title("Event Ticket Ordering System")
root.configure(bg=TEXT_BG)
root.geometry("900x600")

# Customer name
tk.Label(root, text="Customer Name:", font=LABEL_FONT, bg=TEXT_BG).grid(row=0, column=0, padx=10, pady=5, sticky="e")
customer_entry = tk.Entry(root, font=ENTRY_FONT, bg=ENTRY_BG, width=20)
customer_entry.grid(row=0, column=1, padx=10, pady=5, ipady=5)

# Event type
tk.Label(root, text="Event Type:", font=LABEL_FONT, bg=TEXT_BG).grid(row=1, column=0, padx=10, pady=5, sticky="e")
event_var = tk.StringVar(root)
event_var.set("Concert")
event_var.trace_add("write", update_costs)
event_frame = tk.Frame(root, bg=TEXT_BG)
event_frame.grid(row=1, column=1, padx=10, pady=5, sticky="w")
for event in prices.keys():
    tk.Radiobutton(event_frame, text=event, variable=event_var, value=event, bg=TEXT_BG).pack(anchor="w")

# Ticket type
tk.Label(root, text="Ticket Type:", font=LABEL_FONT, bg=TEXT_BG).grid(row=2, column=0, padx=10, pady=5, sticky="e")
ticket_var = tk.StringVar(root)
ticket_var.set("VIP")
ticket_var.trace_add("write", update_costs)
ticket_frame = tk.Frame(root, bg=TEXT_BG)
ticket_frame.grid(row=2, column=1, padx=10, pady=5, sticky="w")
for ticket_type in ["VIP", "Regular", "Student"]:
    tk.Radiobutton(ticket_frame, text=ticket_type, variable=ticket_var, value=ticket_type, bg=TEXT_BG).pack(anchor="w")

# Quantity
tk.Label(root, text="Quantity:", font=LABEL_FONT, bg=TEXT_BG).grid(row=3, column=0, padx=10, pady=5, sticky="e")
quantity_var = tk.StringVar(root)
quantity_var.set("1")
quantity_var.trace_add("write", update_costs)
quantity_menu = tk.OptionMenu(root, quantity_var, "1", "2", "3", "4", "5")
quantity_menu.grid(row=3, column=1, padx=10, pady=5, sticky="w")
quantity_menu.config(bg=QUANTITY_BG, fg=TEXT_FG, activebackground=QUANTITY_HOVER_BG, activeforeground=TEXT_FG)
quantity_menu["menu"].config(bg=QUANTITY_BG, fg=TEXT_FG)

# Cost per ticket display
cost_display_var = tk.StringVar(root)
cost_display_var.set("Cost per ticket: $0")
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

# Delete selected ticket button
delete_ticket_button = tk.Button(root, text="Delete Selected Ticket", command=delete_selected_ticket, bg=DELETE_BUTTON_BG, fg=DELETE_BUTTON_FG, activebackground=DELETE_BUTTON_HOVER_BG)
delete_ticket_button.grid(row=6, column=2, padx=10, pady=5, ipadx=20, ipady=10, sticky="w")
delete_ticket_button.bind("<Enter>", on_enter_delete)
delete_ticket_button.bind("<Leave>", on_leave_delete)

# Cancel whole order button
cancel_order_button = tk.Button(root, text="Cancel Orders", command=cancel_order, bg=DELETE_BUTTON_BG, fg=DELETE_BUTTON_FG, activebackground=DELETE_BUTTON_HOVER_BG)
cancel_order_button.grid(row=6, column=3, padx=10, pady=5, ipadx=20, ipady=10, sticky="w")
cancel_order_button.bind("<Enter>", on_enter_cancel)
cancel_order_button.bind("<Leave>", on_leave_cancel)

# Run the application
root.mainloop()
