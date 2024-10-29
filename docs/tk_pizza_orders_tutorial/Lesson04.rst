==============================================================
Pizza 4: Adding Radio Buttons and OptionMenu
==============================================================

- **Objective**: Add radio buttons for selecting pizza sizes and the OptionMenu for quantity.
- **Content**:

  - Creating and positioning radio buttons for Pizza sizes.
  - Introduction to OptionMenu.
  - Creating and positioning the OptionMenu for selecting the quantity of pizzas.

Creating and Positioning Radio Buttons for Pizza Sizes
-------------------------------------------------------

| This code sets up a GUI for selecting a pizza size using radio buttons. The selected pizza size is stored in the `size_var` variable. The `pack` method ensures that the radio buttons are neatly aligned within the `size_frame`, making the GUI intuitive and easy to use.

.. code-block:: python

    # Pizza size
    tk.Label(root, text="Pizza Size:").grid(row=2, column=0, padx=10, pady=5, sticky="e")
    size_var = tk.StringVar(root)
    size_var.set("Small")
    size_frame = tk.Frame(root)
    size_frame.grid(row=3, column=1, padx=10, pady=5, sticky="w")
    for size in ["Small", "Medium", "Large"]:
        tk.Radiobutton(size_frame, text=size, variable=size_var, value=size).pack(anchor="w")


1. **Label Creation**:

    .. code-block:: python

        tk.Label(root, text="Pizza Size:").grid(row=2, column=0, padx=10, pady=5, sticky="e")

    - This line creates a label widget with the text "Pizza Size:".
    - The `grid` method places the label in the third row (`row=2`), first column (`column=0`) of the grid layout.
    - `padx` and `pady` add padding around the label for better spacing.
    - `sticky="e"` aligns the label to the east (right side) of its grid cell.

2. **StringVar Initialization**:

    .. code-block:: python

        size_var = tk.StringVar(root)
        size_var.set("Small")

    - `size_var` is a `StringVar` object that holds the value of the selected pizza size.
    - `size_var.set("Small")` sets the default value to "Small".

3. **Frame Creation**:

    .. code-block:: python

        size_frame = tk.Frame(root)
        size_frame.grid(row=3, column=1, padx=10, pady=5, sticky="w")

    - This creates a frame widget to contain the radio buttons.
    - The `grid` method places the frame in the fourth row (`row=3`), second column (`column=1`) of the grid layout.
    - `sticky="w"` aligns the frame to the west (left side) of its grid cell.

4. **Radio Buttons Creation**:

    .. code-block:: python

        for size in ["Small", "Medium", "Large"]:
            tk.Radiobutton(size_frame, text=size, variable=size_var, value=size).pack(anchor="w")

    - This loop creates a radio button for each pizza size in the list.
    - Each `Radiobutton` is placed inside `size_frame`.
    - `text=size` sets the label of the radio button.
    - `variable=size_var` links the radio button to the `size_var` variable.
    - `value=size` sets the value of `size_var` when the radio button is selected.
    - `pack(anchor="w")` arranges the radio buttons vertically, aligned to the left.



Creating and Positioning the OptionMenu
--------------------------------------------

| This code sets up a GUI for selecting a quantity using an `OptionMenu`. OptionMenu is a dropdown menu that allows users to select one option from a list of quantities of pizzas. The selected quantity is stored in the `quantity_var` variable. The `grid` method ensures that the label and the `OptionMenu` are neatly aligned within the grid layout.

.. code-block:: python

    # Quantity
    tk.Label(root, text="Quantity:").grid(row=3, column=0, padx=10, pady=5, sticky="e")
    quantity_var = tk.StringVar(root)
    quantity_var.set("1")
    quantity_menu = tk.OptionMenu(root, quantity_var, "1", "2", "3", "4", "5")
    quantity_menu.grid(row=4, column=1, padx=10, pady=5, sticky="w")

1. **Label Creation**:

    .. code-block:: python

        tk.Label(root, text="Quantity:").grid(row=3, column=0, padx=10, pady=5, sticky="e")

    - This line creates a label widget with the text "Quantity:".
    - The `grid` method places the label in the fourth row (`row=3`), first column (`column=0`) of the grid layout.
    - `padx` and `pady` add padding around the label for better spacing.
    - `sticky="e"` aligns the label to the east (right side) of its grid cell.

2. **StringVar Initialization**:

    .. code-block:: python

        quantity_var = tk.StringVar(root)
        quantity_var.set("1")

    - `quantity_var` is a `StringVar` object that holds the value of the selected quantity.
    - `quantity_var.set("1")` sets the default value to "1".

3. **OptionMenu Creation**:

    .. code-block:: python

        quantity_menu = tk.OptionMenu(root, quantity_var, "1", "2", "3", "4", "5")
        quantity_menu.grid(row=4, column=1, padx=10, pady=5, sticky="w")

    - This creates an `OptionMenu` widget for selecting a quantity.
    - The `OptionMenu` is associated with the `root` window and linked to the `quantity_var` variable.
    - The options available in the menu are "1", "2", "3", "4", and "5".
    - The `grid` method places the `OptionMenu` in the fifth row (`row=4`), second column (`column=1`) of the grid layout.
    - `padx` and `pady` add padding around the menu for better spacing.
    - `sticky="w"` aligns the menu to the west (left side) of its grid cell.

