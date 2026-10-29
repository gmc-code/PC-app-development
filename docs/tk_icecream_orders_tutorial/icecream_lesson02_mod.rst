================================================
Data: dictionaries and a list
================================================

- **Objective**: Store the choices and prices, and make a list for the order.

| Nothing new appears in the window yet. Later lessons use this data.

----

Dictionaries and lists
--------------------------------

| A **dictionary** stores pairs: a **key** and its **value**.

.. code-block:: python
   :class: no-copybutton

    flavours = {"Vanilla": 4.00, "Strawberry": 4.50}
    print(flavours["Strawberry"])     # prints 4.5

| A **list** stores items in order.

.. code-block:: python
   :class: no-copybutton

    orders = []                       # an empty list
    orders.append("Vanilla")          # adds to the end

- Keys must be spelt **exactly** right, including capitals.
- Dictionaries look things up. Lists keep things in order.

----

Step 1: Add the dictionaries
--------------------------------

| Paste this under ``# 1. DATA DICTIONARIES & LISTS``.

.. code-block:: python

    # Ice cream flavours and the price of one scoop
    flavours = {
        "Vanilla": 4.00,
        "Chocolate": 4.00,
        "Strawberry": 4.50,
        "Mint Choc Chip": 5.00,
        "Cookies and Cream": 5.50,
    }

    # Containers and their extra cost
    containers = {
        "Cup": 0.00,
        "Plain cone": 0.50,
        "Waffle cone": 1.50,
    }

    # Toppings and their extra cost
    toppings = {
        "No topping": 0.00,
        "Sprinkles": 0.50,
        "Chocolate sauce": 1.00,
        "Crushed nuts": 1.00,
    }

- Keys are words, so they go in quotation marks. Prices are numbers, so they don't.

----

Step 2: Add the orders list
--------------------------------

| Paste this below the dictionaries.

.. code-block:: python

    # List that stores every ice cream in the order
    orders = []

| **Run it.** The window looks the same, with no errors.

----

Quiz
--------------------------------

.. mcqgroup::
    :nav_position: both
    :show-instant-feedback:
    :enable-instant-feedback:
    :shuffle_questions:
    :num_questions: 5

    .. multichoice::

        In "Vanilla": 4.00, which part is the key?

        [x] "Vanilla" | Correct. The key comes before the colon.
        [ ] 4.00 | Incorrect. 4.00 is the value.
        [ ] The colon | Incorrect. The colon joins the key and value.

    .. multichoice::

        What does flavours["Cookies and Cream"] give?

        [x] 5.50 | Correct.
        [ ] 5.00 | Incorrect. That is Mint Choc Chip.
        [ ] "Cookies and Cream" | Incorrect. It gives the value, not the key.

    .. multichoice::

        What does flavours["chocolate"] cause?

        [x] A KeyError | Correct. The key is "Chocolate" with a capital C.
        [ ] It gives 4.00 | Incorrect. The capital letter is missing.
        [ ] It gives 0 | Incorrect. A missing key causes an error.

    .. multichoice::

        What does orders = [] make?

        [x] An empty list | Correct.
        [ ] An empty dictionary | Incorrect. That uses {}.
        [ ] An error | Incorrect. This is how to make an empty list.

    .. multichoice::

        Which line adds an ice cream to the end of the list?

        [x] orders.append(ice_cream) | Correct.
        [ ] orders.add(ice_cream) | Incorrect. Lists use append.
        [ ] orders.clear(ice_cream) | Incorrect. clear empties the list.

----

Fill in the gaps
--------------------------------

.. clozegroup::
    :nav-position: both
    :num-questions: 1
    :show-instant-feedback:


    .. cloze::
        :instructions: Make a dictionary of toppings, then add a scoop to a list.

        toppings = @@{ | [ | (@@
            "No topping": 0.00,
            "Sprinkles"@@: | = | ,@@ 0.50,
        }

        scoops = []
        scoops.@@append | add | keys@@("Vanilla")
