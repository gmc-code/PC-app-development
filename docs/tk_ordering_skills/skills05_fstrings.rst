================================================
5. f-strings: showing prices
================================================

- **Objective**: Join words and numbers with an f-string, and show money with 2 decimal places.
- **Skills for the ice cream app**: ``f"Price: ${price:.2f}"``, ``f"{flavour} (${flavours[flavour]:.2f})"``.

| This lesson has no window. The answers appear in the Python shell.

----

The problem with prices
--------------------------------

| Python drops zeros at the end of a decimal number.

.. code-block:: python

    price = 6.50
    print(price)            # prints 6.5, not 6.50

| A shop always shows prices with **2 decimal places**, like $6.50. An f-string fixes this.

----

What is an f-string?
--------------------------------

| An **f-string** is a string with an ``f`` in front of the first quotation mark.
| Python fills in anything inside curly brackets ``{ }``.

.. code-block:: python

    juice = "Mango"
    price = 6.5
    print(f"{juice} costs ${price:.2f}")       # prints Mango costs $6.50

- ``{juice}`` is replaced by the value of ``juice``.
- ``{price:.2f}`` is replaced by the price with **2** decimal places. ``f`` stands for a decimal (float) number.
- The ``$`` is outside the curly brackets, so it is printed as a normal dollar sign.

.. list-table::
    :header-rows: 1
    :widths: 40 30 30

    * - Code
      - Shows
      - Why
    * - ``f"${6.5:.2f}"``
      - $6.50
      - Two decimal places.
    * - ``f"${4:.2f}"``
      - $4.00
      - Whole numbers get .00 added.
    * - ``f"${5.678:.2f}"``
      - $5.68
      - It rounds to two decimal places.
    * - ``f"${6.5}"``
      - $6.5
      - Without ``:.2f`` the zero is dropped.

----

f-strings with dictionaries
--------------------------------

| The ice cream app puts a dictionary look-up inside the curly brackets.

.. code-block:: python

    juices = {"Orange": 5.00, "Apple": 4.50, "Mango": 6.00}

    for juice in juices.keys():
        print(f"{juice} (${juices[juice]:.2f})")

| This prints:

.. code-block::
   :class: no-copybutton

    Orange ($5.00)
    Apple ($4.50)
    Mango ($6.00)

- Inside an f-string, ``juices[juice]`` looks up the price, then ``:.2f`` shows it with 2 decimal places.
- The round brackets are just printed. They are outside the curly brackets.

----

Building a line of an order
--------------------------------

| An f-string can fill in many values in one line. The ice cream app makes each line of the order like this.

.. code-block:: python

    juice = "Apple"
    size = "Large"
    price = 6.5
    print(f"{juice}, {size}: ${price:.2f}")     # prints Apple, Large: $6.50

----

.. admonition:: Tasks

    #. Store ``taco = "Fish"`` and ``price = 5.5``. Print "Fish taco: $5.50" using an f-string.
    #. Print ``total = 12`` as "Total: $12.00".
    #. Use a loop and an f-string to print every taco in ``tacos = {"Beef": 4.00, "Chicken": 4.50, "Fish": 5.50}`` like "Beef ($4.00)".
    #. This prints "Price: {price}" instead of the price. Why? Fix it.

       .. code-block::
          :class: no-copybutton

          price = 4.5
          print("Price: {price}")

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                .. code-block:: python

                    taco = "Fish"
                    price = 5.5
                    print(f"{taco} taco: ${price:.2f}")

            .. tab-item:: Q2

                .. code-block:: python

                    total = 12
                    print(f"Total: ${total:.2f}")

            .. tab-item:: Q3

                .. code-block:: python

                    tacos = {"Beef": 4.00, "Chicken": 4.50, "Fish": 5.50}
                    for taco in tacos.keys():
                        print(f"{taco} (${tacos[taco]:.2f})")

            .. tab-item:: Q4

                | The ``f`` is missing at the front, so Python does not fill in the curly brackets. Add ``:.2f`` to show 2 decimal places.

                .. code-block:: python

                    price = 4.5
                    print(f"Price: ${price:.2f}")

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

        What makes a string an f-string?

        [x] An f in front of the first quotation mark | Correct. f"..." tells Python to fill in the curly brackets.
        [ ] An f at the end | Incorrect. The f goes at the front.
        [ ] Curly brackets on their own | Incorrect. Without the f they are just printed.
        [ ] Using print | Incorrect. print shows any string.

    .. multichoice::

        price = 6.5. What does print(f"${price:.2f}") show?

        [ ] $6.5 | Incorrect. :.2f adds the second decimal place.
        [x] $6.50 | Correct. :.2f shows 2 decimal places.
        [ ] $6.50f | Incorrect. The f is part of the format, not printed.
        [ ] ${price:.2f} | Incorrect. The f-string fills it in.

    .. multichoice::

        What does f"${4:.2f}" show?

        [ ] $4 | Incorrect. :.2f adds decimal places.
        [ ] $4.0 | Incorrect. It shows two decimal places.
        [x] $4.00 | Correct. Whole numbers get .00 added.
        [ ] $0.04 | Incorrect. The number does not change.

    .. multichoice::

        In f"{juice} costs ${price:.2f}", why is the $ printed?

        [x] It is outside the curly brackets | Correct. Only the parts inside { } are filled in.
        [ ] Python adds it to every price | Incorrect. You must type it.
        [ ] .2f adds it | Incorrect. .2f only sets the decimal places.
        [ ] It is not printed | Incorrect. It is printed.

    .. multichoice::

        What does f"${5.678:.2f}" show?

        [ ] $5.67 | Incorrect. It rounds, so 5.678 becomes 5.68.
        [x] $5.68 | Correct. It rounds to two decimal places.
        [ ] $5.678 | Incorrect. :.2f keeps only two decimal places.
        [ ] $6.00 | Incorrect. It rounds to two places, not to a whole number.

    .. multichoice::

        juice = "Apple". What does print("{juice}") show?

        [ ] Apple | Incorrect. Without the f the brackets are not filled in.
        [x] {juice} | Correct. It needs an f in front to be an f-string.
        [ ] An error | Incorrect. It is a normal string.
        [ ] juice | Incorrect. The curly brackets are printed too.

----

Fill in the gaps
--------------------------------

.. clozegroup::
    :nav-position: both
    :num-questions: 2
    :show-instant-feedback:


    .. cloze::
        :instructions: Show the price with 2 decimal places.

        price = 6.5
        print(@@f | s | p@@"Price: ${price@@:.2f | .2f: | :2@@}")

    .. cloze::
        :instructions: Show each juice and its price.

        for juice in juices.keys():
            print(f"@@{juice} | (juice) | [juice]@@ (${juices[juice]:.2f})")
