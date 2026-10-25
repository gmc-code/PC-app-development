================================================
Data: dictionaries and a list
================================================

- **Objective**: Store the ice cream choices and their prices in dictionaries, and make a list to hold the order.
- **Content**:

  - What a dictionary is.
  - The flavours, containers and toppings dictionaries.
  - Getting a price out of a dictionary.
  - What a list is.
  - The orders list.

| Nothing new appears in the window in this lesson. The data you add here is used by every later lesson.

----

What is a dictionary?
--------------------------------

| A **dictionary** stores pairs of information. Each pair has a **key** and a **value**.
| Think of the price board in an ice cream shop. Each flavour (the key) has a price (the value).

.. list-table::
    :header-rows: 1
    :widths: 50 50

    * - Key (flavour)
      - Value (price)
    * - "Vanilla"
      - 4.00
    * - "Chocolate"
      - 4.00
    * - "Strawberry"
      - 4.50

| In Python, a dictionary is written inside curly brackets ``{ }``.
| A colon ``:`` joins each key to its value. A comma ``,`` goes after each pair.

.. code-block:: python

    flavours = {"Vanilla": 4.00, "Chocolate": 4.00, "Strawberry": 4.50}

----

Adding the dictionaries
--------------------------------

| Place the following code in Section "1. DATA DICTIONARIES & LISTS".
| Writing one pair on each line makes a long dictionary easier to read.

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

- ``flavours`` holds the **product types**. Each flavour is a key, and the price of one scoop is its value.
- ``containers`` and ``toppings`` hold the **features**. Each value is the **extra** cost added to the price.
- A cup costs nothing extra, so its value is ``0.00``. "No topping" also costs ``0.00``.
- The keys are **strings**, so they go inside quotation marks. The prices are **numbers**, so they do not.

----

Getting a price out of a dictionary
---------------------------------------

| To find a value, write the dictionary name, then the key inside square brackets ``[ ]``.

.. code-block:: python

    print(flavours["Strawberry"])        # prints 4.5
    print(containers["Waffle cone"])     # prints 1.5

| Prices can be added together. This is how the app will work out the price of one ice cream.

.. code-block:: python

    price = flavours["Strawberry"] + containers["Waffle cone"] + toppings["Sprinkles"]
    print(price)                         # prints 6.5

| The key must be spelt **exactly** the same, including capital letters.
| ``flavours["vanilla"]`` causes a ``KeyError``, because the key is ``"Vanilla"`` with a capital V.

----

Looping through the keys
--------------------------------

| ``.keys()`` gives all the keys of a dictionary. A ``for`` loop can use each key in turn.
| The app uses this to make one radio button for each flavour.

.. code-block:: python

    for flavour in flavours.keys():
        print(flavour, flavours[flavour])

| This prints each flavour followed by its price.

----

What is a list?
--------------------------------

| A **list** stores items in order, inside square brackets ``[ ]``.
| Each item has a position number called an **index**. The first item is index 0.

.. code-block:: python

    scoops = ["Vanilla", "Chocolate"]
    scoops.append("Strawberry")    # adds to the end: ["Vanilla", "Chocolate", "Strawberry"]
    print(scoops[0])               # prints Vanilla
    print(len(scoops))             # prints 3, the number of items
    del scoops[1]                  # removes index 1: ["Vanilla", "Strawberry"]
    scoops.clear()                 # removes every item: []

----

Adding the orders list
--------------------------------

| Place the following code in Section "1. DATA DICTIONARIES & LISTS", below the dictionaries.
| The list starts **empty**. Each time the user clicks **Add to order**, one ice cream is added to it.

.. code-block:: python

    # List that stores every ice cream in the order
    orders = []

- ``orders = []`` makes an empty list called ``orders``.
- **Dictionaries** are for looking things up by name: "What does Strawberry cost?"
- **Lists** are for keeping things in order: "What has the customer ordered so far?"

:download:`icecream_orders_02.py <python/icecream_orders_02.py>`

----

Try it
--------------------------------

| Add these lines just above ``root.mainloop()``, run the program and read the output in the shell.
| Delete them when you are finished.

.. code-block:: python

    print(flavours["Mint Choc Chip"])
    print(flavours["Vanilla"] + toppings["Crushed nuts"])
    print(len(flavours))

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

        In "Vanilla": 4.00, which part is the key?

        [x] "Vanilla" | Correct. The key comes before the colon.
        [ ] 4.00 | Incorrect. 4.00 is the value, which comes after the colon.
        [ ] The colon | Incorrect. The colon joins the key to its value.
        [ ] The comma | Incorrect. The comma separates one pair from the next.

    .. multichoice::

        What does flavours["Cookies and Cream"] give?

        [ ] 5.00 | Incorrect. 5.00 is the price of Mint Choc Chip.
        [x] 5.50 | Correct. The value stored with the key "Cookies and Cream" is 5.50.
        [ ] "Cookies and Cream" | Incorrect. Square brackets give the value, not the key.
        [ ] A KeyError | Incorrect. The key exists, so its value is returned.

    .. multichoice::

        What does flavours["chocolate"] cause?

        [ ] It gives 4.00 | Incorrect. The key is "Chocolate" with a capital C.
        [x] A KeyError | Correct. Keys must match exactly, including capital letters.
        [ ] It adds chocolate to the dictionary | Incorrect. Square brackets on their own only look up a value.
        [ ] It gives 0 | Incorrect. A missing key causes an error, not 0.

    .. multichoice::

        What does flavours["Vanilla"] + containers["Waffle cone"] give?

        [ ] 4.00 | Incorrect. This is only the price of Vanilla.
        [ ] 1.50 | Incorrect. This is only the extra cost of a waffle cone.
        [x] 5.50 | Correct. 4.00 + 1.50 = 5.50.
        [ ] "VanillaWaffle cone" | Incorrect. The values are numbers, so they are added, not joined.

    .. multichoice::

        What does orders = [] make?

        [x] An empty list | Correct. Square brackets with nothing inside make an empty list.
        [ ] An empty dictionary | Incorrect. An empty dictionary uses curly brackets {}.
        [ ] A list with one item | Incorrect. There is nothing between the brackets.
        [ ] An error | Incorrect. This is the normal way to make an empty list.

    .. multichoice::

        Which line adds an ice cream to the end of the orders list?

        [ ] orders.add(ice_cream) | Incorrect. Lists do not have an add method.
        [x] orders.append(ice_cream) | Correct. append adds an item to the end of a list.
        [ ] orders[ice_cream] | Incorrect. Square brackets get an item; they do not add one.
        [ ] orders.clear(ice_cream) | Incorrect. clear removes every item from the list.

----

Fill in the gaps
--------------------------------

.. clozegroup::
    :nav-position: both
    :num-questions: 2
    :show-instant-feedback:


    .. cloze::
        :instructions: Make a dictionary of toppings and their prices.

        toppings = @@{ | [ | (@@
            "No topping": 0.00,
            "Sprinkles"@@: | = | ,@@ 0.50,
            "Chocolate sauce": 1.00,
        }

    .. cloze::
        :instructions: Print each flavour and its price, then add a scoop to the list.

        for flavour in flavours.@@keys | values | append@@():
            print(flavour, flavours@@[flavour] | (flavour) | .flavour@@)

        scoops = []
        scoops.@@append | add | keys@@("Vanilla")
