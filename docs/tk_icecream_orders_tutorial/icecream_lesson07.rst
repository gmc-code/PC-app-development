================================================
Adding ice creams to the order
================================================

.. image:: images/icecream_07.png
    :scale: 50

- **Objective**: Add the chosen ice cream to the ``orders`` list, show the order in a Listbox, and show the total.
- **Content**:

  - The order list and total label.
  - The Add to order button.
  - Storing each ice cream as a dictionary in the ``orders`` list.
  - Showing the orders and the total.

----

Adding the order list and total
--------------------------------------

| Place the following code below the order heading in Section "4. TKINTER WIDGETS".

.. code-block:: python

    # Order list
    order_listbox = tk.Listbox(root)  # 1. create
    order_listbox.grid(row=1, column=2, rowspan=4, columnspan=2, padx=10, pady=5, sticky="nsew")  # 2. position
    order_listbox.config(width=42, height=10, font=LIST_FONT, bg=LIST_COLOUR, fg=TEXT_COLOUR)  # 3. configure

    # Total cost of the order
    total_label = tk.Label(root)  # 1. create
    total_label.grid(row=5, column=2, columnspan=2, padx=10, pady=5, sticky="w")  # 2. position
    total_label.config(text="Total: $0.00", font=LABEL_FONT, bg=BG_COLOUR, fg=TEXT_COLOUR)  # 3. configure

- A ``Listbox`` shows a list of lines. Each line will be one ice cream in the order.
- ``rowspan=4, columnspan=2`` makes the Listbox cover rows 1 to 4 and columns 2 and 3.
- ``sticky="nsew"`` stretches it to fill all of those cells (north, south, east and west).
- ``width=42, height=10`` makes it 42 characters wide and 10 lines tall.
- ``total_label`` will show the cost of the whole order.

----

Adding the Add to order button
--------------------------------------

| Place the following code below the price label code, on the **left side** of Section "4. TKINTER WIDGETS".

.. code-block:: python

    # Add to order button
    add_button = tk.Button(root)  # 1. create
    add_button.grid(row=5, column=1, padx=10, pady=10, ipady=4, sticky="w")  # 2. position
    add_button.config(text="Add to order", width=14, font=BUTTON_FONT, bg=ADD_COLOUR, fg=TEXT_COLOUR)  # 3. configure
    add_button.config(command=add_ice_cream)  # 4. command

- The button uses all four widget steps: create, position, configure, then command.
- ``add_button.config(command=add_ice_cream)`` tells the button which function to run when it is clicked. There are no brackets after the name.
- ``ipady=4`` adds 4 pixels of space **inside** the button, making it taller and easier to click.

| The app will not run until the ``add_ice_cream`` function is written in the next step.

----

Storing each ice cream
--------------------------------------

| Each ice cream has a flavour, a container, a topping and a price.
| We store these four things together in a **dictionary**, then add that dictionary to the ``orders`` **list**.

.. code-block::
   :class: no-copybutton

    # One ice cream
    {"flavour": "Strawberry", "container": "Waffle cone", "topping": "Sprinkles", "price": 6.50}

    # The orders list after two ice creams are added
    orders = [
        {"flavour": "Strawberry", "container": "Waffle cone", "topping": "Sprinkles", "price": 6.50},
        {"flavour": "Vanilla", "container": "Cup", "topping": "No topping", "price": 4.00},
    ]

- ``orders[0]`` is the first ice cream.
- ``orders[0]["price"]`` is the price of the first ice cream, ``6.50``.

----

Writing the add_ice_cream function
--------------------------------------

| Place the following code in Section "3. DEFINITIONS", below ``update_ice_cream_price``.

.. code-block:: python

    def add_ice_cream():
        """Adds the chosen ice cream to the orders list."""
        ice_cream = {
            "flavour": flavour_var.get(),
            "container": container_var.get(),
            "topping": topping_var.get(),
            "price": get_ice_cream_price(),
        }
        orders.append(ice_cream)
        show_ice_cream_orders()

- ``ice_cream = { ... }`` makes a dictionary holding the user's choices and the price.
- ``orders.append(ice_cream)`` adds that dictionary to the end of the ``orders`` list.
- ``show_ice_cream_orders()`` redraws the Listbox so it shows the new ice cream.

----

Writing the show_ice_cream_orders function
---------------------------------------------

| Place the following code in Section "3. DEFINITIONS", **above** ``add_ice_cream``.

.. code-block:: python

    def show_ice_cream_orders():
        """Redraws the order list and the total so they match the orders list."""
        order_listbox.delete(0, tk.END)
        total = 0
        for ice_cream in orders:
            flavour = ice_cream["flavour"]
            container = ice_cream["container"]
            topping = ice_cream["topping"]
            price = ice_cream["price"]
            order_listbox.insert(tk.END, f"{flavour}, {container}, {topping}: ${price:.2f}")
            total = total + price
        total_label.config(text=f"Total: ${total:.2f}")

- ``order_listbox.delete(0, tk.END)`` clears every line from the Listbox, from line 0 to the end.
- ``total = 0`` starts the total at zero.
- ``for ice_cream in orders:`` repeats once for each ice cream in the list.
- ``ice_cream["flavour"]`` gets the flavour out of that ice cream's dictionary.
- ``order_listbox.insert(tk.END, ...)`` adds a line to the end of the Listbox.
- ``total = total + price`` adds this ice cream's price to the running total.
- After the loop, ``total_label`` shows the total of the whole order.

| The **list** holds the data. The **Listbox** only shows a copy of it.
| That is why the Listbox is cleared and redrawn from the list each time.

----

Showing the order when the app starts
---------------------------------------------

| Add this line in Section "5. MAIN CODE", below ``update_ice_cream_price()``.

.. code-block:: python

    show_ice_cream_orders()

| Run the code. Add three different ice creams and check that each price and the total are correct.

----

Quiz
--------------------------------

.. mcqgroup::
    :nav_position: both
    :show-instant-feedback:
    :enable-instant-feedback:
    :shuffle_questions:
    :num_questions: 6

    .. multichoice::

        What happens when the Add to order button is clicked?

        [x] add_ice_cream runs | Correct. command=add_ice_cream links the button to the function.
        [ ] The app closes | Incorrect. Nothing in the button closes the app.
        [ ] The flavours dictionary gets a new flavour | Incorrect. The dictionaries do not change.
        [ ] Nothing, because the button has no text | Incorrect. The text is set with config().

    .. multichoice::

        What is stored in the orders list?

        [ ] Strings of text from the Listbox | Incorrect. The Listbox shows text made from the list.
        [x] One dictionary for each ice cream | Correct. Each dictionary holds a flavour, container, topping and price.
        [ ] Only the prices | Incorrect. The choices are stored too.
        [ ] The radio buttons | Incorrect. The list holds data, not widgets.

    .. multichoice::

        orders[1]["topping"] gives:

        [ ] The topping of the first ice cream | Incorrect. The first ice cream is orders[0].
        [x] The topping of the second ice cream | Correct. Index 1 is the second item, and "topping" is the key.
        [ ] Every topping | Incorrect. It gives one value from one dictionary.
        [ ] The price of the second ice cream | Incorrect. That would be orders[1]["price"].

    .. multichoice::

        Why does show_ice_cream_orders start with order_listbox.delete(0, tk.END)?

        [x] To clear the old lines before redrawing every ice cream | Correct. Otherwise each ice cream would appear more than once.
        [ ] To delete the orders list | Incorrect. It only clears the Listbox, not the list.
        [ ] To close the Listbox | Incorrect. The Listbox stays in the window.
        [ ] To delete the last ice cream | Incorrect. It deletes every line, from 0 to the end.

    .. multichoice::

        Two ice creams cost $6.50 and $4.00. What does the total label show?

        [ ] Total: $6.50 | Incorrect. This is only the first ice cream.
        [ ] Total: $4.00 | Incorrect. This is only the second ice cream.
        [x] Total: $10.50 | Correct. The loop adds each price to the total.
        [ ] Total: $0.00 | Incorrect. The total is worked out from the list.

    .. multichoice::

        What does rowspan=4 do for the Listbox?

        [ ] Puts it in row 4 | Incorrect. row=1 sets the starting row.
        [ ] Shows 4 lines | Incorrect. height=10 sets the number of lines.
        [x] Makes it cover 4 rows of the grid | Correct. It covers rows 1, 2, 3 and 4.
        [ ] Adds 4 pixels of space | Incorrect. padx and pady add space.

----

Fill in the gaps
--------------------------------

.. clozegroup::
    :nav-position: both
    :num-questions: 2
    :show-instant-feedback:


    .. cloze::
        :instructions: Add the chosen ice cream to the orders list.

        def add_ice_cream():
            ice_cream = {
                "flavour": flavour_var.get(),
                "container": container_var.get(),
                "topping": topping_var.get(),
                "price": @@get_ice_cream_price() | update_ice_cream_price() | price_label@@,
            }
            orders.@@append | insert | clear@@(ice_cream)
            show_ice_cream_orders()

    .. cloze::
        :instructions: Show every ice cream in the Listbox and add up the total.

        def show_ice_cream_orders():
            order_listbox.@@delete | insert | clear@@(0, tk.END)
            total = 0
            for ice_cream in @@orders | flavours | order_listbox@@:
                price = ice_cream["@@price | flavour | total@@"]
                order_listbox.insert(tk.END, f"{ice_cream['flavour']}: ${price:.2f}")
                total = total @@+ | - | *@@ price
            total_label.config(text=f"Total: ${total:.2f}")
