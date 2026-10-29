================================================
Showing the price
================================================

.. image:: images/icecream_06.png
    :scale: 50

- **Objective**: Show the price, and update it when a choice changes.

----

How it works
--------------------------------

- A **function** adds up the three prices from the dictionaries.
- A **label** shows the price.
- **Binding** runs the function every time a choice changes.

.. code-block::
   :class: no-copybutton

    # Strawberry + Waffle cone + Sprinkles
    4.50 + 1.50 + 0.50 = 6.50

----

Step 1: Add the price functions
--------------------------------

| Replace ``# N`` with Block N.

.. code-block:: python
   :caption: Block N

    def get_ice_cream_price():
        """Adds up the flavour, container and topping prices for one ice cream."""
        flavour = flavour_var.get()
        container = container_var.get()
        topping = topping_var.get()
        price = flavours[flavour] + containers[container] + toppings[topping]
        return price


    def update_ice_cream_price(*args):
        """Shows the price of the ice cream that is chosen right now."""
        price = get_ice_cream_price()
        price_label.config(text=f"Price: ${price:.2f}")

- ``.get()`` reads the current choice.
- ``return price`` sends the answer back.
- ``update_ice_cream_price`` puts the price on the label.

----

Step 2: Add the price label
--------------------------------

| Replace ``# O`` with Block O.

.. code-block:: python
   :caption: Block O

    # Price of the chosen ice cream
    price_label = tk.Label(root)  # 1. create
    price_label.grid(row=4, column=1, padx=10, pady=5, sticky="w")  # 2. position
    price_label.config(text="Price: $0.00", font=LABEL_FONT, bg=BG_COLOUR, fg=TEXT_COLOUR)  # 3. configure

----

Step 3: Bind the choices
--------------------------------

| Each placeholder sits **straight after** the ``.set(...)`` line of its variable.

| Replace ``# P`` with Block P.

.. code-block:: python
   :caption: Block P

    flavour_var.trace_add("write", update_ice_cream_price)  # C. bind

| Replace ``# Q`` with Block Q.

.. code-block:: python
   :caption: Block Q

    container_var.trace_add("write", update_ice_cream_price)  # C. bind

| Replace ``# R`` with Block R.

.. code-block:: python
   :caption: Block R

    topping_var.trace_add("write", update_ice_cream_price)  # C. bind

- Now the price updates whenever a choice changes.

----

Step 4: Show the price at the start
--------------------------------------

| Replace ``# S`` with Block S.

.. code-block:: python
   :caption: Block S

    update_ice_cream_price()

| **Run it.** A Vanilla cup shows $4.00. Change a choice and the price changes.

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

        What does flavour_var.get() give?

        [x] The flavour picked right now | Correct.
        [ ] The price of the flavour | Incorrect. Prices are in the dictionary.
        [ ] Every flavour | Incorrect. It holds one flavour.

    .. multichoice::

        Mint Choc Chip in a Plain cone with Chocolate sauce costs:

        [x] $6.50 | Correct. 5.00 + 0.50 + 1.00 = 6.50.
        [ ] $5.00 | Incorrect. That is only the flavour.
        [ ] $7.50 | Incorrect. A plain cone is 0.50.

    .. multichoice::

        What does trace_add("write", update_ice_cream_price) do?

        [x] Runs the function every time the choice changes | Correct.
        [ ] Runs the function once | Incorrect. It runs every time.
        [ ] Adds a new flavour | Incorrect.

    .. multichoice::

        Why is update_ice_cream_price() in the main code?

        [x] To show the right price when the app opens | Correct.
        [ ] To close the app | Incorrect.
        [ ] It isn't needed | Incorrect. The label would say $0.00.

----

Fill in the gaps
--------------------------------

.. clozegroup::
    :nav-position: both
    :num-questions: 1
    :show-instant-feedback:


    .. cloze::
        :instructions: Work out the price of one ice cream.

        def get_ice_cream_price():
            flavour = flavour_var.@@get | set | trace_add@@()
            container = container_var.get()
            topping = topping_var.get()
            price = flavours[@@flavour | container | topping@@] + containers[container] + toppings[topping]
            @@return | print | def@@ price
