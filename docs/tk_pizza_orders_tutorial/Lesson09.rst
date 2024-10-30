==================================================
Pizza 9: Final Touches and Styling
==================================================

.. image:: tk_pizza_orders_tutorial/images/pizza_9.png
    :scale: 67%

.. image:: tk_pizza_orders_tutorial/images/pizza_v1.png
    :scale: 67%

- **Objective**: Add final touches and improve the GUI styling.
- **Content**:

  - Adding Font and colour variables
  - Adding font and colour settings to tkinter widgets
  - Updating Pizza type to use prices dictionary
  - Final review and testing.

Adding Font and colour variables
--------------------------------

| Add this code at the top of the file under the prices dictionary.
| This allows the variables to be used to adjust colouring in the various functions, not just the tkinter objects code lines.

.. code-block:: python

    # Style configurations
    label_font = ("Helvetica", 12)
    entry_font = ("Helvetica", 14)
    order_font = ("Helvetica", 12)
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

Adding font and colour settings to tkinter widgets
----------------------------------------------------

| Add or adjust the code below for font and colour settings in each section for each widget.

.. code-block:: python

    # Create the main window
    root.configure(bg=text_bg)

    # Customer name
    tk.Label(root, text="Customer Name:", font=label_font, bg=text_bg).grid(row=0, column=0, padx=10, pady=5, sticky="e")
    customer_entry = tk.Entry(root, font=entry_font, bg=entry_bg)

    # Pizza type
    tk.Label(root, text="Pizza Type:", font=label_font, bg=text_bg).grid(row=1, column=0, padx=10, pady=5, sticky="e")

    pizza_frame = tk.Frame(root, bg=text_bg)

    for pizza in prices.keys():
        tk.Radiobutton(pizza_frame, text=pizza, variable=pizza_var, value=pizza, bg=text_bg).pack(anchor="w")

    # Pizza size
    tk.Label(root, text="Pizza Size:", font=label_font, bg=text_bg).grid(row=2, column=0, padx=10, pady=5, sticky="e")

    size_frame = tk.Frame(root, bg=text_bg)

    for pizza in prices.keys():
        tk.Radiobutton(pizza_frame, text=pizza, variable=pizza_var, value=pizza, bg=text_bg).pack(anchor="w")

    # Quantity
    tk.Label(root, text="Quantity:", font=label_font, bg=text_bg).grid(row=3, column=0, padx=10, pady=5, sticky="e")

    quantity_menu.config(bg=quantity_bg, fg=text_fg, activebackground=quantity_hover_bg, activeforeground=text_fg)  # for menu button

    quantity_menu["menu"].config(bg=quantity_bg, fg=text_fg)  # for menu items

    # Cost per pizza display
    tk.Label(root, textvariable=cost_display_var, font=label_font, bg=text_bg).grid(row=4, column=1, padx=10, pady=5, sticky="w")

    # Order cost display
    tk.Label(root, textvariable=order_cost_var, font=order_font, bg=text_bg).grid(row=5, column=1, padx=10, pady=5, sticky="w")

    # Add order button
    add_button = tk.Button(root, text="Add Order", command=add_order, bg=add_button_bg, fg=add_button_fg, activebackground=add_button_hover_bg)

    # Orders list
    tk.Label(root, text="Orders:", font=label_font, bg=text_bg).grid(row=0, column=2, padx=10, pady=5, sticky="w")
    order_list = tk.Listbox(root, width=50, bg=entry_bg)

    # Delete selected pizza button
    delete_pizza_button = tk.Button(root, text="Delete Selected Pizza", command=delete_selected_pizza, bg=delete_button_bg, fg=delete_button_fg, activebackground=delete_button_hover_bg)

    # Cancel whole order button
    cancel_order_button = tk.Button(root, text="Cancel Orders", command=cancel_order, bg=delete_button_bg, fg=delete_button_fg, activebackground=delete_button_hover_bg)


Adding color to the Orders list total
---------------------------------------

| Adjust the padding, alignment, and size of widgets to create a more polished look.

.. code-block:: python

    # Display orders
    def update_order_list():
        order_list.delete(0, tk.END)
        total_cost = 0
        for order in orders:
            customer, pizza, size, quantity = order
            cost = prices[pizza][size] * quantity
            total_cost += cost
            order_list.insert(tk.END, f"{customer} - {quantity} {size} {pizza}(s) - ${cost}")
        if orders:
            order_list.insert(tk.END, f"Total cost: ${total_cost}")
            # add color to last line of order list for total
            order_list.itemconfig(order_list.size() - 1, {"bg": order_list_total_bg, "selectbackground": order_list_total_selected_bg})


Adding hover color to buttons
---------------------------------------

| The **Add Order**, **Delete Selected Pizza** and **Cancel Orders** buttons require special code to change colour on hovering.

| **Add Order** button changes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    # Function to change color on hover
    def on_enter_add(e):
        add_button.config(bg=add_button_hover_bg)


    def on_leave_add(e):
        add_button.config(bg=add_button_bg)

    # Add order button
    # for hover color change:
    # Bind the hover events
    add_button.bind("<Enter>", on_enter_add)
    add_button.bind("<Leave>", on_leave_add)

| **Delete Selected Pizza** button changes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    # Function to change color on hover
    def on_enter_delete(e):
        delete_pizza_button.config(bg=delete_button_hover_bg)


    def on_leave_delete(e):
        delete_pizza_button.config(bg=delete_button_bg)


    # Delete selected pizza button
    # for hover color change:
    # Bind the hover events
    delete_pizza_button.bind("<Enter>", on_enter_delete)
    delete_pizza_button.bind("<Leave>", on_leave_delete)

| **Cancel Orders** button changes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    # Function to change color on hover
    def on_enter_cancel(e):
        cancel_order_button.config(bg=delete_button_hover_bg)


    def on_leave_cancel(e):
        cancel_order_button.config(bg=delete_button_bg)


    # Cancel whole order button
    # for hover color change:
    # Bind the hover events
    cancel_order_button.bind("<Enter>", on_enter_cancel)
    cancel_order_button.bind("<Leave>", on_leave_cancel)


Improving the customer_entry width
-----------------------------------------------------

- Adjust the width to set a wider customer entry field.
- Add internal vertical padding using `ipady`.

.. code-block:: python

    customer_entry = tk.Entry(root, font=entry_font, bg=entry_bg, width=20)
    customer_entry.grid(row=0, column=1, padx=10, pady=5, ipady=5)


Updating Pizza type to use prices dictionary
------------------------------------------------------

| Adjust "# Pizza type" code section to use keys from the prices dictionary instead of manual entries.
| This allows updating the pizza dictionary to flow through to the pizza options.

| Replace ``["Margherita", "Pepperoni", "Hawaiian", "Veggie", "BBQ Chicken"]`` with ``prices.keys()``.


.. code-block:: python

    for pizza in prices.keys():
        tk.Radiobutton(pizza_frame, text=pizza, variable=pizza_var, value=pizza, bg=text_bg).pack(anchor="w")

| Test these code changes by adding ot the prices dictionary.

.. code-block:: python

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

Final Review and Testing
-----------------------------------------

- Test the application to ensure all features work as expected.
- Make any necessary adjustments to improve functionality and user experience.
