==============================================================
Pizza orders Lesson 4: Adding Radio Buttons and OptionMenu
==============================================================

- **Objective**: Add radio buttons for selecting pizza sizes and the OptionMenu for quantity.
- **Content**:

  - Creating and positioning radio buttons for Pizza sizes.
  - Introduction to OptionMenu.
  - Creating and positioning the OptionMenu for selecting the quantity of pizzas.

Creating and Positioning Radio Buttons for Pizza Sizes
-------------------------------------------------------

.. code-block:: python

    # Pizza size
    tk.Label(root, text="Pizza Size:", font=label_font, bg="#f0f0f0").grid(row=2, column=0, padx=10, pady=5, sticky="e")
    size_var = tk.StringVar(root)
    size_var.set("Small")
    size_frame = tk.Frame(root)
    size_frame.grid(row=3, column=1, padx=10, pady=5, sticky="w")
    for size in ["Small", "Medium", "Large"]:
        tk.Radiobutton(size_frame, text=size, variable=size_var, value=size).pack(anchor="w")

- ``tk.Label(root, text="Pizza Size:").grid(row=3, column=0, padx=10, pady=5, sticky="e")``: Creates a label widget with the text "Pizza Size:".
- ``size_var = tk.StringVar(root)``: Creates a StringVar to hold the value of the selected size.
- ``size_var.set("Small")``: Sets the default value of the size radio button group.
- ``size_frame = tk.Frame(root)``: Creates a frame to contain the size radio buttons.
- ``.grid(row=2, column=1, padx=10, pady=5, sticky="w")``: Positions the frame in the grid layout.
- ``tk.Radiobutton(size_frame, text=size, variable=size_var, value=size)``: Creates a radio button for each size, associating it with the StringVar.


Creating and Positioning the OptionMenu
--------------------------------------------

- OptionMenu is a dropdown menu that allows users to select one option from a list of quantities of pizzas.

.. code-block:: python

    # Quantity
    tk.Label(root, text="Quantity:").grid(row=3, column=0, padx=10, pady=5, sticky="e")
    quantity_var = tk.StringVar(root)
    quantity_var.set("1")
    quantity_menu = tk.OptionMenu(root, quantity_var, "1", "2", "3", "4", "5")
    quantity_menu.grid(row=4, column=1, padx=10, pady=5, sticky="w")

- ``tk.Label(root, text="Quantity:").grid(row=3, column=0, padx=10, pady=5, sticky="e")``: Creates a label widget with the text "Quantity:".
- ``quantity_var = tk.StringVar(root)``: Creates a StringVar to hold the selected quantity.
- ``quantity_var.set("1")``: Sets the default value of the OptionMenu.
- ``tk.OptionMenu(root, quantity_var, "1", "2", "3", "4", "5")``: Creates an OptionMenu with options from 1 to 5.
- ``quantity_menu.grid(row=4, column=1, padx=10, pady=5, sticky="w")``: Positions the OptionMenu in the grid layout.


