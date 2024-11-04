==================================================
Pizza 10: Extensions
==================================================

- **Objective**: Extend the pizza ordering system.
- **Content**:

  - Extend the pizza ordering system.

Add customer address
--------------------------------

.. code-block:: python

    tk.Label(root, text="Address:").grid(row=1, column=0, padx=10, pady=5)
    address_entry = tk.Entry(root)
    address_entry.grid(row=1, column=1, padx=10, pady=5)


Add descriptions
--------------------------------

| There are several standard types of pizza that are popular around the world. Here are some of the most well-known varieties:

1. **Margherita**: Diced tomato, mozzarella, oregano.
2. **Pepperoni**: Pepperoni slices, mozzarella.
3. **Hawaiian**: Leg ham, mozzarella, pineapple.
4. **Veggie**: Mushrooms, roasted peppers, Spanish onion, olives, pineapple, garlic, oregano
5. **BBQ Chicken**: Barbecue sauce, grilled chicken, red onions.
6. **Meat Lovers**: Leg ham, mild salami, marinated chicken, bacon, BBQ sauce.
7. **Capriciossa**: Leg ham, mushrooms, olives, anchovies.
8. **Supreme**: Leg ham, mild salami, roasted peppers, Spanish onion, olives, mushrooms.
9.  **Mexican**: Salami, roasted peppers, Spanish onion, olives, oregano, garlic, chilli
10. **Four Cheese**: A blend of four different cheeses, often including mozzarella, cheddar, parmesan, and gorgonzola.


Add crust type
-------------------------------------------------------

- Creating radio buttons for crust types:

.. code-block:: python

    tk.Label(root, text="Crust type:").grid(row=5, column=0, padx=10, pady=5, sticky="e")
    crust_var = tk.StringVar(root)
    crust_var.set("Thin")
    crust_frame = tk.Frame(root)
    crust_frame.grid(row=5, column=1, padx=10, pady=5, sticky="w")
    for crust in ["Thin", "Thick", "Stuffed"]:
        tk.Radiobutton(crust_frame, text=crust, variable=crust_var, value=crust).pack(anchor="w")

----

Add drinks
--------------------------------

.. code-block:: python

    tk.Label(root, text="Drink:").grid(row=5, column=0, padx=10, pady=5, sticky="e")
    drink_var = tk.StringVar(root)
    drink_var.set("Coke")
    drink_frame = tk.Frame(root)
    drink_frame.grid(row=5, column=1, padx=10, pady=5, sticky="w")
    for drink in ["Coke", "Pepsi", "Orange", "Lemonade", "Water"]:
        tk.Radiobutton(drink_frame, text=drink, variable=drink_var, value=drink).pack(anchor="w")


.. code-block:: python

    drink_quantity_var = tk.IntVar(root)
    drink_quantity_var.set("1")
    drink_quantity_menu = tk.OptionMenu(root, drink_quantity_var, *[str(i) for i in range(1, 11)])
    drink_quantity_menu.grid(row=6, column=1, padx=10, pady=5, sticky="w")


.. code-block:: python

   drink_cost_var = tk.StringVar(root)
   drink_cost_var.set("Cost per drink: $0")
   tk.Label(root, textvariable=drink_cost_var).grid(row=6, column=1, padx=10, pady=5, sticky="w")
