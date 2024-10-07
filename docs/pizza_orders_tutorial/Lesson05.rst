=========================================================
Pizza 5: Adding Costs
=========================================================

- **Objective**: Add costs.
- **Content**:

  - Define prices for pizzas
  - Adding Cost Display Fields
  - Calculating the cost based on selection.
  - Updating costs dynamically based on selections.


Define prices for pizzas
------------------------------

.. code-block:: python

    # Define the prices for each pizza size
    prices = {
        "Margherita": {"Small": 5, "Medium": 7, "Large": 10},
        "Pepperoni": {"Small": 6, "Medium": 8, "Large": 11},
        "Hawaiian": {"Small": 6, "Medium": 8, "Large": 11},
        "Veggie": {"Small": 5, "Medium": 7, "Large": 10},
        "BBQ Chicken": {"Small": 7, "Medium": 9, "Large": 12}
    }


Adding Cost Display Fields
------------------------------

.. code-block:: python

    # Cost per pizza display
    cost_display_var = tk.StringVar(root)
    cost_display_var.set("Cost per pizza: $0")
    tk.Label(root, textvariable=cost_display_var).grid(row=4, column=1, padx=10, pady=5, sticky="w")

- ``cost_display_var = tk.StringVar(root)``: Creates a StringVar to hold the cost per pizza.
- ``cost_display_var.set("Cost per pizza: $0")``: Sets the initial value of the cost display.
- ``tk.Label(root, textvariable=cost_display_var)``: Creates a label that displays the cost per pizza.

.. code-block:: python

    # Cost per pizza display
    order_cost_var = tk.StringVar(root)
    order_cost_var.set("Order cost: $0")
    tk.Label(root, textvariable=order_cost_var).grid(row=5, column=1, padx=10, pady=5, sticky="w")

- ``order_cost_var = tk.StringVar(root)``: Creates a StringVar to hold the order cost.
- ``order_cost_var.set("Order cost: $0")``: Sets the initial value of the order cost display.
- ``tk.Label(root, textvariable=order_cost_var)``: Creates a label that displays the order cost.


Calculating the cost based on selection.
-------------------------------------------------

- You can use the ``update_costs`` to calculate the cost of a pizza and the Order cost.

.. code-block:: python

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



Updating Costs Dynamically Based on Selections
------------------------------------------------------

- Use the ``trace_add`` method of ``StringVar`` to update the costs whenever the pizza type, size, or quantity changes.

.. code-block:: python

   pizza_var.trace_add("write", update_costs)
   size_var.trace_add("write", update_costs)
   quantity_var.trace_add("write", update_costs)

- Add this to the code below previous lines of code dealing with ``pizza_var``.

.. code-block:: python

    pizza_var.trace_add("write", update_costs)

- Add this to the code below previous lines of code dealing with ``size_var``.

.. code-block:: python

    size_var.trace_add("write", update_costs)

- Add this to the code below previous lines of code dealing with ``quantity_var``.

.. code-block:: python

    quantity_var.trace_add("write", update_costs)


