================================================
Project: make it your own
================================================

.. image:: images/bubble_tea_exemplar.png
    :scale: 50

| *Example: the Ice Cream Shop changed into a Bubble Tea Bar.*

- **Objective**: Change the Ice Cream Shop app into an ordering app for a product you choose.
- **Content**:

  - The project brief.
  - The marking rubric.
  - Step 1: Plan.
  - Step 2: Copy and rename.
  - Step 3: Change the data.
  - Step 4: Customise the look.
  - Step 5: Test and check.

----

The project brief
--------------------------------

| Choose a product that people order with choices. Your app must let the user:

- pick a **product type** using **radio buttons**,
- pick **features** using **drop-down menus**,
- see the **price**,
- **add** items to an order, **remove** an item and **clear** the order,
- see the **total** of the order.

| Product ideas:

.. list-table::
    :widths: 33 33 34

    * - Bubble tea
      - Burgers
      - Pizza
    * - Smoothies
      - Sushi
      - Phone cases
    * - Sneakers
      - Birthday cakes
      - Tacos
    * - Pet grooming
      - Coffee
      - Skateboards

----

The marking rubric
--------------------------------

.. list-table::
    :header-rows: 1
    :widths: 16 28 28 28

    * - Criteria
      - Level 1
      - Level 2
      - Level 3
    * - Code order
      - Imports are placed at the top of the code, followed by data dictionaries.
      - Constants are placed after dictionaries.
      - Definitions are placed after constants, before any tkinter widgets.
    * - Code grouping for widgets
      - Positioning of each widget using grid or pack methods follows the code lines for each widget creation.
      - Code for configuration of text and colour of a widget follows positioning code.
      - Event binding of user interactions to a widget via variables follows the code lines for the variable.
    * - Variable naming and comments
      - Variables are renamed appropriately based on the product.
      - All variables and comments refer to the product.
      - Definitions renamed to refer to the product.
    * - Data dictionary
      - The data dictionary has 1 to 2 product types and 1 to 2 features with their prices.
      - The data dictionary has 3 to 4 product types and 2 to 3 features with their prices.
      - The data dictionary has 5 or more product types and 3 or more features with their prices.
    * - Product choices
      - Window and product labels refer to the product.
      - Radio buttons display product choices.
      - Drop-downs provide choice to the user.
    * - Customisation
      - A few colour constants have been modified.
      - Modified font constants.
      - Widget colours and fonts have been customised such that the design is visually consistent and engaging.
    * - Functionality
      - Radio buttons function as expected.
      - Drop-downs function as expected.
      - Order buttons and the order list function as expected.

----

Step 1: Plan
--------------------------------

| Fill in the three planning sheets **before** you change any code.

#. **Data plan**: list your product types and features, with a price for each.

   - Level 3 needs **5 or more** product types and **3 or more** features with prices.

#. **Planning grid**: draw where each widget will go. Write each widget's variable name inside its box.
#. **Widget plan**: list each widget with its row, column, text, colours and font.

.. image:: images/my_product_data_plan_blank.png
    :scale: 40

.. image:: images/my_product_grid_blank.png
    :scale: 40

.. image:: images/my_product_widget_plan_blank.png
    :scale: 40

| Use the Ice Cream Shop plans as examples:

.. image:: images/icecream_data_plan.png
    :scale: 40

----

Step 2: Copy and rename
--------------------------------

#. Save a copy of your finished ``icecream_orders.py`` with a new name, e.g. ``bubble_tea_orders.py``.
#. Fill in the **renaming plan**. Every name with "ice cream", "flavour", "container" or "topping" in it needs a new name that fits your product.

.. image:: images/my_product_rename_plan.png
    :scale: 40

3. Use **Find and Replace** (Ctrl+H) to change **one name at a time**. Run the app after each change to check it still works.
4. Change the **comments** and **docstrings** too, so they talk about your product.
5. Change the **definition names**, e.g. ``get_ice_cream_price`` becomes ``get_drink_price``. Remember to change every place the name is used, including ``command=`` and ``trace_add``.

| Example renames for a bubble tea app:

.. list-table::
    :header-rows: 1
    :widths: 50 50

    * - Ice cream app
      - Bubble tea app
    * - ``flavours``
      - ``drinks``
    * - ``flavour_var``
      - ``drink_var``
    * - ``containers``, ``container_menu``
      - ``sizes``, ``size_menu``
    * - ``get_ice_cream_price``
      - ``get_drink_price``
    * - ``add_ice_cream``
      - ``add_drink``
    * - ``# Ice cream flavours and the price of one scoop``
      - ``# Bubble tea drinks and the price of a regular drink``

| **Watch out:** replace longer names first. If you replace ``flavour`` before ``flavour_var``, you may get strange names.

----

Step 3: Change the data
--------------------------------

| Change the dictionaries in Section "1. DATA DICTIONARIES & LISTS" to match your data plan.

- Each **key** is a choice the user sees. Each **value** is its price.
- Update the ``.set(...)`` line for each variable. The starting choice must be spelt **exactly** like a key in the dictionary.
- Update the window title, the title label and the order heading.

Adding a third feature drop-down
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| The ice cream app has two features (containers and toppings). Level 3 needs **3 or more**.
| To add a third feature, change the code in **five** places. The bubble tea example adds ``extras``.

1. **Section 1**: add a new dictionary.

    .. code-block::
        :class: no-copybutton

        # Extras and their extra cost
        extras = {
            "No extra": 0.00,
            "Cheese foam": 1.50,
            "Pudding": 1.20,
            "Extra shot of tea": 0.80,
        }

2. **Section 4**: copy a whole drop-down block and change every name. Put it in the next empty row.

    .. code-block::
        :class: no-copybutton

        # Extra (drop-down menu)
        extra_label = tk.Label(root)  # 1. create
        extra_label.grid(row=4, column=0, padx=10, pady=5, sticky="e")  # 2. position
        extra_label.config(text="Extra:", font=LABEL_FONT, bg=BG_COLOUR, fg=TEXT_COLOUR)  # 3. configure

        extra_var = tk.StringVar(root)  # A. make
        extra_var.set("No extra")  # B. set
        extra_var.trace_add("write", update_drink_price)  # C. bind

        extra_menu = tk.OptionMenu(root, extra_var, "No extra")  # 1. create
        extra_menu.grid(row=4, column=1, padx=10, pady=5, sticky="w")  # 2. position
        extra_menu.config(width=16, font=LABEL_FONT, bg=MENU_COLOUR, fg=TEXT_COLOUR,
                            activebackground=MENU_COLOUR)  # 3. configure

        extra_choices = extra_menu["menu"]
        extra_choices.config(font=LABEL_FONT, bg=MENU_COLOUR, fg=TEXT_COLOUR)
        extra_choices.delete(0)   # remove the starting choice
        for extra in extras.keys():
            extra_choices.add_radiobutton(label=extra, variable=extra_var, value=extra)

3. **Section 4**: move the widgets below it down one row. Add 1 to the ``row=`` of the price label, the add button, the total label and the two bottom buttons, and change the Listbox to ``rowspan=5``.
4. **The price function**: add the new feature's price.

    .. code-block::
        :class: no-copybutton

        extra = extra_var.get()
        price = drinks[drink] + sizes[size] + pearls[pearl] + extras[extra]

5. **The add and show functions**: store the new choice in each item's dictionary and show it in the Listbox line.

    .. code-block::
        :class: no-copybutton

        "extra": extra_var.get(),

----

Step 4: Customise the look
--------------------------------

| Change the constants in Section "2. CONSTANTS" so the app looks like your product.

- Pick colours that match your product. A bubble tea app might use milk tea brown, taro purple and matcha green.
- Keep text dark on a light background (or light on dark) so it is easy to read.
- Use the **same** few colours across the whole app so it looks consistent.
- Change the font constants. Fonts on school computers include ``"Segoe UI"``, ``"Trebuchet MS"``, ``"Verdana"``, ``"Georgia"`` and ``"Comic Sans MS"``.
- Check that long names still fit. Make the window, the drop-downs (``width=``) or the Listbox wider if they do not.

----

Step 5: Test and check
--------------------------------

| Test the app with the same tests as :doc:`icecream_lesson08`, using your own product.
| Then check your code against the rubric:

.. list-table::
    :header-rows: 1
    :widths: 80 20

    * - Check
      - Done
    * - Imports are at the top, then dictionaries, then constants, then definitions, then widgets.
      -
    * - Each widget is created, then positioned with grid() or pack(), then configured with config().
      -
    * - Each button's command is set after it is configured.
      -
    * - Each trace_add line comes straight after the lines that make its variable.
      -
    * - Every variable, definition and comment refers to my product. There is no "ice cream" left.
      -
    * - I have 5 or more product types and 3 or more features, each with a price.
      -
    * - The window title and labels name my product.
      -
    * - Radio buttons show the product types. Drop-downs show the features.
      -
    * - My colours and fonts are changed and look consistent.
      -
    * - Radio buttons, drop-downs, the price, the order buttons, the order list and the total all work.
      -

| Search your code for "ice", "cream", "flavour", "container" and "topping" (Ctrl+F). If you find any, rename them.
