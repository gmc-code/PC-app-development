================================================
4. Dictionaries: choices and prices
================================================

- **Objective**: Store choices and their prices in a dictionary, look up a price, add prices together and loop through the keys.
- **Skills for the orders app**: ``{"Vanilla": 4.00}``, ``flavours["Vanilla"]``, adding prices, ``for flavour in flavours.keys():``.

| This lesson has no window. The code uses ``print()``, so the answers appear in the Python shell.

----

What is a dictionary?
--------------------------------

| A **dictionary** stores **pairs**. Each pair has a **key** and a **value**.
| Think of a price board: each juice (the key) has a price (the value).

.. code-block:: python

    juices = {"Orange": 5.00, "Apple": 4.50, "Mango": 6.00}
    print(juices)

- A dictionary goes inside curly brackets ``{ }``.
- A colon ``:`` joins each key to its value.
- A comma ``,`` goes between the pairs.
- The keys here are **strings**, so they have quotation marks. The prices are **numbers**, so they do not.

| A long dictionary is easier to read with one pair on each line. The comma after the last pair is allowed.

.. code-block:: python

    # Juices and the price of a regular cup
    juices = {
        "Orange": 5.00,
        "Apple": 4.50,
        "Mango": 6.00,
        "Watermelon": 5.50,
    }

----

Looking up a price
--------------------------------

| Write the dictionary name, then the key inside **square brackets**.

.. code-block:: python

    juices = {"Orange": 5.00, "Apple": 4.50, "Mango": 6.00}

    print(juices["Mango"])      # prints 6.0
    print(juices["Apple"])      # prints 4.5

- The key must be spelt **exactly** the same, including capital letters.
- ``juices["mango"]`` causes a ``KeyError``, because the key is ``"Mango"`` with a capital M.

----

Adding prices together
--------------------------------

| The orders app uses one dictionary for each kind of choice, then adds the prices.

.. code-block:: python

    juices = {"Orange": 5.00, "Apple": 4.50, "Mango": 6.00}
    sizes = {"Small": 0.00, "Regular": 1.00, "Large": 2.00}

    price = juices["Mango"] + sizes["Large"]
    print(price)                # prints 8.0

- The ``sizes`` values are the **extra** cost. A small costs nothing extra, so its value is ``0.00``.
- Each choice can also be stored in a variable first, then used as the key.

.. code-block:: python

    juices = {"Orange": 5.00, "Apple": 4.50, "Mango": 6.00}
    sizes = {"Small": 0.00, "Regular": 1.00, "Large": 2.00}

    juice = "Orange"
    size = "Regular"
    price = juices[juice] + sizes[size]
    print(price)                # prints 6.0

----

Looping through the keys
--------------------------------

| ``.keys()`` gives every key in the dictionary. A ``for`` loop uses each key in turn.

.. code-block:: python

    juices = {"Orange": 5.00, "Apple": 4.50, "Mango": 6.00}

    for juice in juices.keys():
        print(juice, juices[juice])

| This prints:

.. code-block::
   :class: no-copybutton

    Orange 5.0
    Apple 4.5
    Mango 6.0

- ``juice`` holds a different key each time round the loop.
- ``juices[juice]`` looks up the price of that key.
- The orders app uses a loop like this to make **one radio button for each flavour**. Add a flavour to the dictionary and a new radio button appears.

----

.. admonition:: Tasks

    #. Make a dictionary called ``tacos`` with "Beef": 4.00, "Chicken": 4.50 and "Fish": 5.50. Print the price of a fish taco.
    #. Make a dictionary called ``extras`` with "No extra": 0.00, "Cheese": 1.00 and "Guacamole": 1.50. Print the price of a chicken taco with guacamole.
    #. Use a ``for`` loop to print every taco and its price.
    #. This code causes a ``KeyError``. Why? Fix it.

       .. code-block::
          :class: no-copybutton

          tacos = {"Beef": 4.00, "Chicken": 4.50, "Fish": 5.50}
          print(tacos["beef"])

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                .. code-block:: python

                    tacos = {"Beef": 4.00, "Chicken": 4.50, "Fish": 5.50}
                    print(tacos["Fish"])

            .. tab-item:: Q2

                .. code-block:: python

                    tacos = {"Beef": 4.00, "Chicken": 4.50, "Fish": 5.50}
                    extras = {"No extra": 0.00, "Cheese": 1.00, "Guacamole": 1.50}
                    price = tacos["Chicken"] + extras["Guacamole"]
                    print(price)

            .. tab-item:: Q3

                .. code-block:: python

                    tacos = {"Beef": 4.00, "Chicken": 4.50, "Fish": 5.50}
                    for taco in tacos.keys():
                        print(taco, tacos[taco])

            .. tab-item:: Q4

                | The key is ``"Beef"`` with a capital B. Keys must match exactly.

                .. code-block:: python

                    tacos = {"Beef": 4.00, "Chicken": 4.50, "Fish": 5.50}
                    print(tacos["Beef"])

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

        In "Apple": 4.50, which part is the key?

        [x] "Apple" | Correct. The key comes before the colon.
        [ ] 4.50 | Incorrect. 4.50 is the value.
        [ ] The colon | Incorrect. The colon joins the key to its value.
        [ ] The comma | Incorrect. Commas go between pairs.

    .. multichoice::

        Which brackets does a dictionary use?

        [ ] ( ) | Incorrect. Round brackets make a tuple.
        [ ] [ ] | Incorrect. Square brackets make a list.
        [x] { } | Correct. Dictionaries use curly brackets.
        [ ] < > | Incorrect. These are not used for dictionaries.

    .. multichoice::

        juices = {"Orange": 5.00, "Mango": 6.00}. What does juices["Mango"] give?

        [ ] "Mango" | Incorrect. Square brackets give the value.
        [x] 6.0 | Correct. The value stored with "Mango" is 6.00.
        [ ] 5.0 | Incorrect. That is the price of Orange.
        [ ] A KeyError | Incorrect. The key exists.

    .. multichoice::

        What does juices["orange"] cause when the key is "Orange"?

        [ ] It gives 5.0 | Incorrect. The capital letter does not match.
        [x] A KeyError | Correct. Keys must match exactly, including capitals.
        [ ] It adds orange to the dictionary | Incorrect. Looking up does not add.
        [ ] It gives 0 | Incorrect. A missing key causes an error.

    .. multichoice::

        juices = {"Apple": 4.50} and sizes = {"Large": 2.00}. What is juices["Apple"] + sizes["Large"]?

        [ ] 4.5 | Incorrect. That is only the apple juice.
        [ ] 2.0 | Incorrect. That is only the size.
        [x] 6.5 | Correct. 4.50 + 2.00 = 6.50.
        [ ] "AppleLarge" | Incorrect. The values are numbers, so they are added.

    .. multichoice::

        What does for juice in juices.keys(): do?

        [x] Repeats once for each key in the dictionary | Correct. juice holds a different key each time.
        [ ] Repeats once for each price | Incorrect. .keys() gives the keys, not the prices.
        [ ] Deletes each key | Incorrect. It only reads them.
        [ ] Repeats forever | Incorrect. It stops after the last key.

----

Fill in the gaps
--------------------------------

.. clozegroup::
    :nav-position: both
    :num-questions: 2
    :show-instant-feedback:


    .. cloze::
        :instructions: Make a dictionary of sizes and look up a price.

        sizes = @@{ | [ | (@@
            "Small": 0.00,
            "Large"@@: | = | ;@@ 2.00,
        }
        print(sizes@@["Large"] | ("Large") | .Large@@)

    .. cloze::
        :instructions: Print every juice and its price.

        for juice in juices.@@keys | values | prices@@():
            print(juice, juices@@[juice] | (juice) | .juice@@)
