================================================
6. Lists: keeping the order
================================================

- **Objective**: Store items in a list, add and remove items, loop through a list and add up a total. Store a dictionary for each item.
- **Skills for the orders app**: ``orders = []``, ``append()``, ``orders[0]``, ``len()``, ``del orders[1]``, ``clear()``, a list of dictionaries.

| This lesson has no window. The answers appear in the Python shell.

----

What is a list?
--------------------------------

| A **list** stores items **in order**, inside square brackets ``[ ]``.
| Each item has a position number called an **index**. The first item is index **0**.

.. code-block:: python

    order = ["Orange", "Apple"]
    print(order[0])                # prints Orange
    print(order[1])                # prints Apple
    print(len(order))              # prints 2, the number of items

----

Changing a list
--------------------------------

.. code-block:: python

    order = []                     # an empty list
    order.append("Orange")         # ["Orange"]
    order.append("Mango")          # ["Orange", "Mango"]
    order.append("Apple")          # ["Orange", "Mango", "Apple"]
    del order[1]                   # removes index 1: ["Orange", "Apple"]
    print(order)
    order.clear()                  # removes every item: []
    print(order)

.. list-table::
    :header-rows: 1
    :widths: 35 65

    * - Code
      - What it does
    * - ``orders = []``
      - Makes an empty list.
    * - ``orders.append(item)``
      - Adds an item to the **end** of the list.
    * - ``orders[0]``
      - Gets the first item.
    * - ``len(orders)``
      - Counts the items.
    * - ``del orders[1]``
      - Removes the item at index 1, the second item.
    * - ``orders.clear()``
      - Removes every item.

----

Adding up a total
--------------------------------

| A ``for`` loop can go through every item in a list. Start the total at 0, then add each price.

.. code-block:: python

    prices = [5.00, 4.50, 6.00]
    total = 0
    for price in prices:
        total = total + price
    print(f"Total: ${total:.2f}")      # prints Total: $15.50

- ``total = 0`` must come **before** the loop. If it was inside the loop, it would go back to 0 every time.
- ``total = total + price`` adds this price to the total so far.

----

A list of dictionaries
--------------------------------

| One juice has a name, a size and a price. A **dictionary** keeps them together.
| The **list** keeps every juice in the order. This is how the orders app stores its order.

.. code-block:: python

    orders = []

    juice = {"juice": "Mango", "size": "Large", "price": 8.00}
    orders.append(juice)

    juice = {"juice": "Apple", "size": "Small", "price": 4.50}
    orders.append(juice)

    print(orders[0]["juice"])          # prints Mango
    print(orders[1]["price"])          # prints 4.5

    total = 0
    for juice in orders:
        print(f"{juice['juice']}, {juice['size']}: ${juice['price']:.2f}")
        total = total + juice["price"]
    print(f"Total: ${total:.2f}")      # prints Total: $12.50

- ``orders[0]`` is the first juice, a dictionary.
- ``orders[0]["juice"]`` looks up the ``"juice"`` key in that dictionary.
- Inside an f-string that uses double quotation marks, use **single** quotation marks for the key: ``{juice['size']}``.

| Use each one for its job:

- **Dictionaries** look things up by name: "What does Mango cost?"
- **Lists** keep things in order: "What has the customer ordered so far?"

----

.. admonition:: Tasks

    #. Make an empty list called ``tacos``. Append "Beef", "Fish" and "Chicken". Print the list and how many items it has.
    #. Remove "Fish" from your list using ``del``, then print the list.
    #. Add up the prices in ``prices = [4.00, 5.50, 4.50, 1.50]`` with a loop. Print "Total: $15.50".
    #. Make an ``orders`` list with two dictionaries: a "Beef" taco with "Cheese" for 5.00, and a "Fish" taco with "No extra" for 5.50. Loop through it to print each line and the total.

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                .. code-block:: python

                    tacos = []
                    tacos.append("Beef")
                    tacos.append("Fish")
                    tacos.append("Chicken")
                    print(tacos)
                    print(len(tacos))

            .. tab-item:: Q2

                | "Fish" is index 1.

                .. code-block:: python

                    tacos = ["Beef", "Fish", "Chicken"]
                    del tacos[1]
                    print(tacos)

            .. tab-item:: Q3

                .. code-block:: python

                    prices = [4.00, 5.50, 4.50, 1.50]
                    total = 0
                    for price in prices:
                        total = total + price
                    print(f"Total: ${total:.2f}")

            .. tab-item:: Q4

                .. code-block:: python

                    orders = [
                        {"taco": "Beef", "extra": "Cheese", "price": 5.00},
                        {"taco": "Fish", "extra": "No extra", "price": 5.50},
                    ]

                    total = 0
                    for taco in orders:
                        print(f"{taco['taco']}, {taco['extra']}: ${taco['price']:.2f}")
                        total = total + taco["price"]
                    print(f"Total: ${total:.2f}")

----

Quiz
--------------------------------

.. mcqgroup::
    :nav_position: top
    :show-instant-feedback:
    :enable-instant-feedback:
    :shuffle_questions:
    :num_questions: 6

    .. multichoice::

        What does orders = [] make?

        [x] An empty list | Correct. Square brackets with nothing inside.
        [ ] An empty dictionary | Incorrect. That would be {}.
        [ ] A list with one item | Incorrect. There is nothing inside.
        [ ] An error | Incorrect. This is how to make an empty list.

    .. multichoice::

        order = ["Orange", "Apple", "Mango"]. What is order[1]?

        [ ] "Orange" | Incorrect. That is index 0.
        [x] "Apple" | Correct. Index 1 is the second item.
        [ ] "Mango" | Incorrect. That is index 2.
        [ ] An error | Incorrect. Index 1 exists.

    .. multichoice::

        Which line adds "Kiwi" to the end of order?

        [ ] order.add("Kiwi") | Incorrect. Lists do not have add.
        [x] order.append("Kiwi") | Correct. append adds to the end.
        [ ] order["Kiwi"] | Incorrect. That does not add an item.
        [ ] order.clear("Kiwi") | Incorrect. clear removes everything.

    .. multichoice::

        What does del order[0] do?

        [x] Removes the first item | Correct. Index 0 is the first item.
        [ ] Removes every item | Incorrect. clear() does that.
        [ ] Deletes the list | Incorrect. Only one item is removed.
        [ ] Removes the last item | Incorrect. The last item has the biggest index.

    .. multichoice::

        Why does total = 0 go before the for loop?

        [ ] Python needs it at the top of the file | Incorrect. It just needs to be before the loop.
        [x] Inside the loop it would go back to 0 each time | Correct. Set it once, then add to it.
        [ ] So the loop runs faster | Incorrect. It is about the answer, not speed.
        [ ] It does not matter | Incorrect. The total would be wrong.

    .. multichoice::

        orders = [{"juice": "Mango", "price": 8.00}]. What is orders[0]["price"]?

        [ ] "Mango" | Incorrect. That is the "juice" key.
        [x] 8.0 | Correct. orders[0] is the dictionary, then ["price"] gets its price.
        [ ] 0 | Incorrect. 0 is the index.
        [ ] An error | Incorrect. Both the index and the key exist.

----

Fill in the gaps
--------------------------------

.. clozegroup::
    :nav-position: top
    :num-questions: 2
    :show-instant-feedback:


    .. cloze::
        :instructions: Add two juices, remove the first one, then empty the list.

        order = @@[] | {} | ()@@
        order.@@append | add | insert@@("Orange")
        order.append("Mango")
        del order[@@0 | 1 | 2@@]
        order.@@clear | delete | empty@@()

    .. cloze::
        :instructions: Add up the price of every juice in the order.

        total = @@0 | 1 | total@@
        for juice in orders:
            total = total @@+ | - | =@@ juice["price"]
        print(f"Total: ${total:.2f}")
