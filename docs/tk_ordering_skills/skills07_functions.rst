================================================
7. Functions: def and return
================================================

- **Objective**: Write functions with ``def``, describe them with a docstring, call them, and send back an answer with ``return``.
- **Skills for the orders app**: ``def get_ice_cream_price():``, docstrings, ``return price``, one function calling another.

| This lesson has no window. The answers appear in the Python shell.

----

What is a function?
--------------------------------

| A **function** (also called a **definition**) is a named block of code. It only runs when it is **called**.

.. code-block:: python

    def say_welcome():
        """Prints a welcome message."""
        print("Welcome to the Juice Bar!")
        print("What would you like?")


    say_welcome()
    say_welcome()

- ``def say_welcome():`` starts the function. Don't forget the brackets and the colon.
- The lines inside the function are **indented** (moved in by 4 spaces).
- The text inside ``""" """`` is a **docstring**. It says what the function does.
- ``say_welcome()`` **calls** the function, which runs its code. Here it runs twice.

----

Sending back an answer with return
--------------------------------------

| ``return`` sends a value back to the code that called the function.

.. code-block:: python

    juices = {"Orange": 5.00, "Apple": 4.50, "Mango": 6.00}
    sizes = {"Small": 0.00, "Regular": 1.00, "Large": 2.00}

    juice = "Mango"
    size = "Large"


    def get_juice_price():
        """Adds up the juice and size prices for one juice."""
        price = juices[juice] + sizes[size]
        return price


    price = get_juice_price()
    print(f"Price: ${price:.2f}")       # prints Price: $8.00

- ``get_juice_price()`` works out the price, then ``return price`` sends it back.
- ``price = get_juice_price()`` stores the answer that came back.
- After ``return``, the function stops.

----

One function calling another
--------------------------------------

| The orders app has one function that **works out** the price and another that **shows** it.

.. code-block:: python

    juices = {"Orange": 5.00, "Apple": 4.50, "Mango": 6.00}
    sizes = {"Small": 0.00, "Regular": 1.00, "Large": 2.00}

    juice = "Apple"
    size = "Regular"


    def get_juice_price():
        """Adds up the juice and size prices for one juice."""
        price = juices[juice] + sizes[size]
        return price


    def show_juice_price():
        """Prints the price of the chosen juice."""
        price = get_juice_price()
        print(f"{juice}, {size}: ${price:.2f}")


    show_juice_price()                  # prints Apple, Regular: $5.50

- Splitting the work into small functions makes each one easy to read and test.
- Name each function with a **verb**: ``get_``, ``show_``, ``add_``, ``remove_``.

----

Define first, then call
--------------------------------------

| Python reads from the top down. A function must be **defined before it is called**.

.. code-block::
   :class: no-copybutton

    say_hello()             # NameError: name 'say_hello' is not defined

    def say_hello():
        print("Hello")

| That is why the **definitions** section comes before the **widgets** section. A button needs its function to exist before the button is made.

----

.. admonition:: Tasks

    #. Write a function ``say_goodbye()`` with a docstring. It prints "Thanks for visiting the Taco Truck!". Call it.
    #. With ``tacos = {"Beef": 4.00, "Fish": 5.50}``, ``extras = {"No extra": 0.00, "Cheese": 1.00}``, ``taco = "Fish"`` and ``extra = "Cheese"``, write ``get_taco_price()`` that returns the price.
    #. Write ``show_taco_price()`` that calls ``get_taco_price()`` and prints "Fish, Cheese: $6.50".
    #. This code shows a ``NameError``. Why? Fix it.

       .. code-block::
          :class: no-copybutton

          show_total()

          def show_total():
              print("Total: $0.00")

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                .. code-block:: python

                    def say_goodbye():
                        """Prints a goodbye message."""
                        print("Thanks for visiting the Taco Truck!")


                    say_goodbye()

            .. tab-item:: Q2 and Q3

                .. code-block:: python

                    tacos = {"Beef": 4.00, "Fish": 5.50}
                    extras = {"No extra": 0.00, "Cheese": 1.00}

                    taco = "Fish"
                    extra = "Cheese"


                    def get_taco_price():
                        """Adds up the taco and extra prices."""
                        price = tacos[taco] + extras[extra]
                        return price


                    def show_taco_price():
                        """Prints the price of the chosen taco."""
                        price = get_taco_price()
                        print(f"{taco}, {extra}: ${price:.2f}")


                    show_taco_price()

            .. tab-item:: Q4

                | The function is called before it is defined. Move the call below the definition.

                .. code-block:: python

                    def show_total():
                        print("Total: $0.00")


                    show_total()

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

        When does the code inside a function run?

        [ ] As soon as Python reads def | Incorrect. def only makes the function.
        [x] When the function is called | Correct. e.g. say_welcome() runs it.
        [ ] Only once, at the end | Incorrect. It runs each time it is called.
        [ ] Never | Incorrect. It runs when called.

    .. multichoice::

        What is a docstring?

        [x] Text inside """ """ that says what the function does | Correct. It goes on the first line inside the function.
        [ ] A comment that starts with # | Incorrect. That is a normal comment.
        [ ] The function's name | Incorrect. The name comes after def.
        [ ] The value that is returned | Incorrect. return sends back a value.

    .. multichoice::

        What does return price do?

        [ ] Prints the price | Incorrect. print shows it on the screen.
        [x] Sends the price back to the code that called the function | Correct. The caller can store it in a variable.
        [ ] Deletes the price | Incorrect. It sends it back.
        [ ] Starts the function again | Incorrect. The function stops after return.

    .. multichoice::

        Which line calls a function called show_price?

        [ ] def show_price(): | Incorrect. That defines it.
        [ ] show_price | Incorrect. The brackets are needed to call it.
        [x] show_price() | Correct. The brackets call the function.
        [ ] call show_price | Incorrect. Python does not use the word call.

    .. multichoice::

        Why do definitions come before the widgets in the orders app?

        [x] A function must be defined before it is used | Correct. Buttons need their function to exist.
        [ ] Python reads from the bottom up | Incorrect. It reads from the top down.
        [ ] Definitions make the window | Incorrect. tk.Tk() makes the window.
        [ ] It looks neater | Incorrect. The code would not work the other way.

    .. multichoice::

        What is wrong with def get_price() with no colon?

        [ ] Nothing | Incorrect. The colon is needed.
        [ ] The brackets should be removed | Incorrect. The brackets are needed.
        [x] It needs a colon at the end: def get_price(): | Correct. Without it Python shows a SyntaxError.
        [ ] get_price is not allowed as a name | Incorrect. It is a good name.

----

Fill in the gaps
--------------------------------

.. clozegroup::
    :nav-position: top
    :num-questions: 2
    :show-instant-feedback:


    .. cloze::
        :instructions: Write a function that works out the price and sends it back.

        @@def | function | define@@ get_juice_price():
            """Adds up the juice and size prices for one juice."""
            price = juices[juice] + sizes[size]
            @@return | print | send@@ price

    .. cloze::
        :instructions: Call the price function and show the answer.

        def show_juice_price():
            """Prints the price of the chosen juice."""
            price = @@get_juice_price() | get_juice_price | def get_juice_price()@@
            print(f"Price: ${price:.2f}")


        @@show_juice_price() | show_juice_price | call show_juice_price@@
