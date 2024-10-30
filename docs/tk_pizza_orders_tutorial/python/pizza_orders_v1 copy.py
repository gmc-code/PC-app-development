import tkinter as tk
from tkinter import messagebox


# Create the main window
root = tk.Tk()
root.title("Pizza Ordering System")
root.configure(bg=text_bg)
root.geometry("900x600")

# Customer name
tk.Label(root, text="Customer Name:", font=label_font, bg=text_bg).grid(row=0, column=0, padx=10, pady=5, sticky="e")
customer_entry = tk.Entry(root, font=entry_font, bg=entry_bg, width=20)
customer_entry.grid(row=0, column=1, padx=10, pady=5, ipady=5)

# Pizza type
tk.Label(root, text="Pizza Type:", font=label_font, bg=text_bg).grid(row=1, column=0, padx=10, pady=5, sticky="e")
pizza_var = tk.StringVar(root)
pizza_var.set("Margherita")
pizza_var.trace_add("write", update_costs)
pizza_frame = tk.Frame(root, bg=text_bg)
pizza_frame.grid(row=1, column=1, padx=10, pady=5, sticky="w")
for pizza in prices.keys():
    tk.Radiobutton(pizza_frame, text=pizza, variable=pizza_var, value=pizza, bg=text_bg).pack(anchor="w")

# Pizza size
tk.Label(root, text="Pizza Size:", font=label_font, bg=text_bg).grid(row=2, column=0, padx=10, pady=5, sticky="e")
size_var = tk.StringVar(root)
size_var.set("Small")
size_var.trace_add("write", update_costs)
size_frame = tk.Frame(root, bg=text_bg)
size_frame.grid(row=2, column=1, padx=10, pady=5, sticky="w")
for size in ["Small", "Medium", "Large"]:
    tk.Radiobutton(size_frame, text=size, variable=size_var, value=size, bg=text_bg).pack(anchor="w")

# Quantity
tk.Label(root, text="Quantity:", font=label_font, bg=text_bg).grid(row=3, column=0, padx=10, pady=5, sticky="e")
quantity_var = tk.StringVar(root)
quantity_var.set("1")
quantity_var.trace_add("write", update_costs)
quantity_menu = tk.OptionMenu(root, quantity_var, "1", "2", "3", "4", "5")
quantity_menu.grid(row=3, column=1, padx=10, pady=5, sticky="w")
# add color
quantity_menu.config(bg=quantity_bg, fg=text_fg, activebackground=quantity_hover_bg, activeforeground=text_fg)  # for menu button
quantity_menu["menu"].config(bg=quantity_bg, fg=text_fg)  # for menu items

# Cost per pizza display
cost_display_var = tk.StringVar(root)
cost_display_var.set("Cost per pizza: $0")
tk.Label(root, textvariable=cost_display_var, font=label_font, bg=text_bg).grid(row=4, column=1, padx=10, pady=5, sticky="w")

# Order cost display
order_cost_var = tk.StringVar(root)
order_cost_var.set("Order cost: $0")
tk.Label(root, textvariable=order_cost_var, font=label_font, bg=text_bg).grid(row=5, column=1, padx=10, pady=5, sticky="w")



# Add order button
add_button = tk.Button(root, text="Add Order", command=add_order, bg=add_button_bg, fg=add_button_fg, activebackground=add_button_hover_bg)
add_button.grid(row=6, column=1, padx=10, pady=10, ipadx=20, ipady=10, sticky="w")
# for hover color change:
# Bind the hover events
add_button.bind("<Enter>", on_enter_add)
add_button.bind("<Leave>", on_leave_add)


# Orders list
tk.Label(root, text="Orders:", font=label_font, bg=text_bg).grid(row=0, column=2, padx=10, pady=5, sticky="w")
order_list = tk.Listbox(root, font=order_font, width=50, bg=entry_bg)
order_list.grid(row=1, column=2, rowspan=5, columnspan=2, padx=10, pady=5, sticky="nsew")
# add for reselectings chosen options:
order_list.bind("<<ListboxSelect>>", select_order)



# Delete selected pizza button
delete_pizza_button = tk.Button(root, text="Delete Selected Pizza", command=delete_selected_pizza, bg=delete_button_bg, fg=delete_button_fg, activebackground=delete_button_hover_bg)
delete_pizza_button.grid(row=6, column=2, padx=10, ipadx=20, ipady=10, pady=5, sticky="w")
# for hover color change:
# Bind the hover events
delete_pizza_button.bind("<Enter>", on_enter_delete)
delete_pizza_button.bind("<Leave>", on_leave_delete)


# Cancel whole order button
cancel_order_button = tk.Button(root, text="Cancel Orders", command=cancel_order, bg=delete_button_bg, fg=delete_button_fg, activebackground=delete_button_hover_bg)
cancel_order_button.grid(row=6, column=3, padx=10, ipadx=20, ipady=10, pady=5, sticky="w")
# for hover color change:
# Bind the hover events
cancel_order_button.bind("<Enter>", on_enter_cancel)
cancel_order_button.bind("<Leave>", on_leave_cancel)


# Run the application
root.mainloop()
