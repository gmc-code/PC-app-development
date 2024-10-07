=============================================================
Pizza 3: Adding Radio Buttons for Pizza Types
=============================================================

- **Objective**: Add radio buttons for selecting pizza types.
- **Content**:

  - Introduction to radio buttons.
  - Creating and positioning radio buttons for Pizza Type.
  - Using StringVar to manage radio button values.


Introduction to Radio Buttons
--------------------------------

- Radio buttons allow users to select one option from a set of mutually exclusive options.

Creating and Positioning Radio Buttons for Pizza Type
----------------------------------------------------------------

.. code-block:: python

    # Pizza type
    tk.Label(root, text="Pizza Type:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
    pizza_var = tk.StringVar(root)
    pizza_var.set("Margherita")
    pizza_frame = tk.Frame(root)
    pizza_frame.grid(row=2, column=1, padx=10, pady=5, sticky="w")
    for pizza in ["Margherita", "Pepperoni", "Hawaiian", "Veggie", "BBQ Chicken"]:
        tk.Radiobutton(pizza_frame, text=pizza, variable=pizza_var, value=pizza).pack(anchor="w")

- ``tk.Label(root, text="Pizza Type:").grid(row=1, column=0, padx=10, pady=5, sticky="e")``: Creates a label widget with the text "Pizza Type:".
- ``pizza_var = tk.StringVar(root)``: Creates a StringVar to hold the value of the selected radio button.
- ``pizza_var.set("Margherita")``: Sets the default value of the radio button group.
- ``pizza_frame = tk.Frame(root)``: Creates a frame to contain the radio buttons.
- ``pizza_frame.grid(row=2, column=1, padx=10, pady=5, sticky="w")``: Positions the frame in the grid layout.
- ``tk.Radiobutton(pizza_frame, text=pizza, variable=pizza_var, value=pizza)``: Creates a radio button with the specified text and value, and associates it with the StringVar.

Using StringVar to Manage Radio Button Values
----------------------------------------------------------------

- ``StringVar`` is a Tkinter variable class that holds a string value.
- It is used to manage the value of a group of radio buttons.


