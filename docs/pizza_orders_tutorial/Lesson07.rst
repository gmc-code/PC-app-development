================================================
Pizza orders Lesson 7: Displaying Orders
================================================

- **Objective**: Display the list of orders.
- **Content**:

  - Adding a Listbox widget to display orders.
  - Formatting the orders display.
  - Updating the orders list dynamically.


Adding a Listbox Widget to Display Orders
------------------------------------------

.. code-block:: python

    # Orders list
    tk.Label(root, text="Orders:").grid(row=0, column=2, padx=10, pady=5, sticky="w")
    order_list = tk.Listbox(root, width=50)
    order_list.grid(row=1, column=2, rowspan=5, columnspan=2, padx=10, pady=5, sticky="nsew")

- ``tk.Label(root, text="Orders:").grid(row=0, column=2, padx=10, pady=5, sticky="w")``: Creates a label widget with the text "Orders:".
- ``order_list = tk.Listbox(root, width=50)``: Creates a Text widget to display the list of orders.
- ``order_list.grid(row=1, column=2, rowspan=5, columnspan=2, padx=10, pady=5, sticky="nsew"``: Positions the Text widget in the grid layout.


Formatting the Orders Display
----------------------------------

.. code-block:: python

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

- ``order_list.delete(1.0, tk.END)``: Clears the Text widget.
- ``order_list.insert(tk.END, f"{customer} ordered {quantity} {size} {pizza}(s) - ${cost}")``: Inserts the formatted order details into the Listbox widget.
- ``order_list.insert(tk.END, f"Total cost: ${total_cost}")``: Inserts the total cost at the end of the Listbox.


Updating the Orders List Dynamically
--------------------------------------------

- Call ``update_order_list()`` whenever an order is added.
- Add the code line below to add_order()

.. code-block:: python

    # add to add_order()
    update_order_list()
