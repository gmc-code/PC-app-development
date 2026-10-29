================================================
Removing and clearing the order
================================================

.. image:: images/icecream_08.png
    :scale: 50

- **Objective**: Remove one ice cream, or clear the whole order.

----

How it works
--------------------------------

- **Remove selected** deletes the ice cream the user clicked.
- **Clear order** empties the whole list.
- A **messagebox** pops up if nothing is clicked.

----

Step 1: Import messagebox
--------------------------------

| Replace ``# X`` with Block X.

.. code-block:: python
   :caption: Block X

    from tkinter import messagebox

----

Step 2: Add the remove and clear functions
---------------------------------------------

| Replace ``# Y`` with Block Y.

.. code-block:: python
   :caption: Block Y

    def remove_ice_cream():
        """Removes the ice cream that is selected in the order list."""
        selection = order_listbox.curselection()
        if not selection:
            messagebox.showinfo("Remove", "Click an ice cream in the order list first.")
        else:
            line_number = selection[0]
            del orders[line_number]
            show_ice_cream_orders()


    def clear_ice_cream_orders():
        """Removes every ice cream from the orders list."""
        orders.clear()
        show_ice_cream_orders()

- ``curselection()`` finds the line the user clicked. Line 0 is the first.
- ``del orders[line_number]`` removes that ice cream.
- ``orders.clear()`` removes them all.

----

Step 3: Add the buttons
--------------------------------

| Replace ``# Z`` with Block Z.

.. code-block:: python
   :caption: Block Z

    # Remove selected button
    remove_button = tk.Button(root)  # 1. create
    remove_button.grid(row=6, column=2, padx=10, pady=10, ipady=4, sticky="w")  # 2. position
    remove_button.config(text="Remove selected", width=14, font=BUTTON_FONT, bg=REMOVE_COLOUR, fg=TEXT_COLOUR)  # 3. configure
    remove_button.config(command=remove_ice_cream)  # 4. command

    # Clear order button
    clear_button = tk.Button(root)  # 1. create
    clear_button.grid(row=6, column=3, padx=10, pady=10, ipady=4, sticky="e")  # 2. position
    clear_button.config(text="Clear order", width=14, font=BUTTON_FONT, bg=REMOVE_COLOUR, fg=TEXT_COLOUR)  # 3. configure
    clear_button.config(command=clear_ice_cream_orders)  # 4. command

----

Step 4: Test the app
--------------------------------

.. list-table::
    :header-rows: 1
    :widths: 60 40

    * - Test
      - Expected result
    * - Pick Strawberry, Waffle cone, Sprinkles.
      - Price: $6.50
    * - Add three different ice creams.
      - Three lines. Correct total.
    * - Click the second line, then **Remove selected**.
      - That line goes. The total goes down.
    * - Click **Remove selected** with nothing clicked.
      - A message pops up.
    * - Click **Clear order**.
      - Empty list. Total: $0.00

----

Quiz
--------------------------------

.. mcqgroup::
    :nav_position: both
    :show-instant-feedback:
    :enable-instant-feedback:
    :shuffle_questions:
    :num_questions: 4

    .. multichoice::

        Why is from tkinter import messagebox needed?

        [x] To show a pop-up message | Correct.
        [ ] So buttons can be clicked | Incorrect.
        [ ] It isn't needed | Incorrect. showinfo would cause an error.

    .. multichoice::

        The user clicks the third line. What does curselection() give?

        [x] (2,) | Correct. Lines start at 0.
        [ ] (3,) | Incorrect. Lines start at 0.
        [ ] () | Incorrect. That means nothing is clicked.

    .. multichoice::

        What does del orders[line_number] do?

        [x] Removes one ice cream | Correct.
        [ ] Removes the whole list | Incorrect. clear() does that.
        [ ] Removes a flavour | Incorrect.

    .. multichoice::

        What does orders.clear() leave?

        [x] An empty list, [] | Correct.
        [ ] The first ice cream | Incorrect. Every item goes.
        [ ] Nothing, the list is deleted | Incorrect. The list still exists.

----

Fill in the gaps
--------------------------------

.. clozegroup::
    :nav-position: both
    :num-questions: 1
    :show-instant-feedback:


    .. cloze::
        :instructions: Remove the selected ice cream, or clear the order.

        def remove_ice_cream():
            selection = order_listbox.@@curselection | get | delete@@()
            if not selection:
                messagebox.showinfo("Remove", "Click an ice cream in the order list first.")
            else:
                line_number = selection[@@0 | 1 | -1@@]
                @@del | clear | remove@@ orders[line_number]
                show_ice_cream_orders()

        def clear_ice_cream_orders():
            orders.@@clear | delete | append@@()
            show_ice_cream_orders()
