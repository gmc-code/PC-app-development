================================================
Add Orders
================================================

.. image:: images/pizza_6.png
    :scale: 67

- **Objective**: Add functionality to add orders.
- **Content**:

  - Creating an add order button.
  - Writing the `add_order` function.
  - Validating input and updating the order list.

----

Creating an Add Order Button
------------------------------------

| Place the following code below the other widget code in Section "4. TKINTER WIDGETS".
| This code creates a button labeled "Add Order" that, when clicked, will call the `add_order` function to process the current order details.

.. code-block:: python

    # Add order button
    add_button = tk.Button(root, text="Add Order", command=add_order,width=15)
    add_button.grid(row=6, column=1, padx=10, pady=15, ipady=5, sticky="w")

- ``tk.Button(root, text="Add Order", command=add_order, bg=button_bg, fg=button_fg)``: Creates a button with the text "Add Order" and assigns the ``add_order`` function to be called when the button is clicked.
- ``.grid(row=6, column=1, padx=10, pady=10, ipadx=20, ipady=10, sticky="w")``: Positions the button in the grid layout.

----

Importing messagebox
---------------------------------------

| Add an import line for the messsagebox that is needed if no customer name is entered.


.. code-block:: python

    from tkinter import messagebox

----

Adding an Orders List
---------------------------------------

| Place the following code below the code in Section "# 1. DATA DICTIONARIES & LISTS".
| Add a list variable, orders, to keep track of orders.
| Orders will be added as tuples of (customer, pizza, size, quantity).
| Place this near the top of the code under the dictionaries or constants, before the definitions.

.. code-block:: python

    # Orders tracking list
    orders = []

----

Writing the ``add_order`` Function
---------------------------------------

| Place the following code in Section "3. DEFINITIONS / FUNCTIONS".
| This function, `add_order`, is responsible for validating input and adding the current selection to the order list.
| It retrieves the customer name, pizza type, size, and quantity from the respective widgets.
| If the customer name is not entered, it shows an error message and highlights the entry field.
| If the input is valid, it adds the order to the list and resets the quantity to 0.


.. code-block:: python

    def add_order():
        """Validates input and adds the current selection to the order list."""
        customer = customer_entry.get()
        pizza = pizza_var.get()
        size = size_var.get()
        quantity = quantity_var.get()

        if not customer:
            messagebox.showerror("Input Error", "Please enter the customer name.")
            customer_entry.config(bg="pink")
        else:
            customer_entry.config(bg="white")
            orders.append((customer, pizza, size, quantity))
            quantity_var.set(1)  # Reset quantity to default



- ``add_order``: Function to add an order to the list.
- ``customer = customer_entry.get()``: Retrieves the customer name from the entry widget.
- ``pizza = pizza_var.get()``: Retrieves the selected pizza type.
- ``size = size_var.get()``: Retrieves the selected pizza size.
- ``quantity = quantity_var.get()``: Retrieves the selected quantity string as an integer.
- ``messagebox.showerror("Input Error", "Please enter the customer name.")``: Displays an error message if the customer name is not entered.
- ``orders.append((customer, pizza, size, quantity))``: Adds the order to the list of orders.
- ``quantity_var.set("0")``: Resets the quantity to 0.

