====================================================
Dictionary with functions
====================================================

Dictionaries
-------------------

| A dictionary is a collection of ``key: value`` pairs. 
| All keys are unique; duplicate keys are not possible. 
| Keys can be an integer, float, string, Boolean (True or False) and even a tuple.
| A key can be used to retrieve a value from a dictionary.
| See: https://v2.scrimba.com/learn-python-c03/~014


Example dictionary
-------------------------

| The dictionary uses {} brackets.
| Each key value pair is separated by a comma.
| Each key is followed by a colon :

| Below is a dictionary of car details.

.. code-block:: python

    car_dictionary = {"brand": "Ford", "model": "Mustang", "year": 1965}

| The first key value pair is "brand": "Ford".
| There are 3 keys: "brand", "model", "year".
| There are 3 corresponding values: "Ford", "Mustang", 1965.

----

Looking up dictionary values by key
--------------------------------------

.. py:function:: value = dictionary[key]

    | Get the value of a specific key in a dictionary.
    | Raises an error if the key doesn't exist, so a try-except block is needed.

Example:

.. code-block:: python

    car_dictionary = {"brand": "Ford", "model": "Mustang", "year": 1965}

    # key exists
    value = car_dictionary["brand"]
    print(value)

    # key doesn't exist
    try:
        value = car_dictionary["brands"]
        print(value)
    except KeyError:
        print("not a valid key")

----

Looking up dictionary values by the get method
----------------------------------------------------

.. py:function:: value = dictionary.get(key)

    | Get the value of a specific key in a dictionary.
    | Returns None if the key does not exist.

Example:

.. code-block:: python

    car_dictionary = {"brand": "Ford", "model": "Mustang", "year": 1965}

    # without default
    value = car_dictionary.get("brand")
    print(value)

    # without default; returns None
    value = car_dictionary.get("brands")
    print(value)

    # with default
    value = car_dictionary.get("brands", "not a valid key")
    print(value)

----

Check if key is in dictionary
-------------------------------

.. py:function:: key in dictionary

    | Returns True if the key is among the keys of the dictionary; False if not.

Example:

.. code-block:: python

    car_dictionary = {"brand": "Ford", "model": "Mustang", "year": 1965}

    # key exists
    key_exists = "model" in car_dictionary
    print(key_exists)

    # key doesn't exists
    key_exists = "models" in car_dictionary
    print(key_exists)

----

Definition to get a dictionary value
-----------------------------------------

Create a dictionary
~~~~~~~~~~~~~~~~~~~~~~

| Below are hex values for colours in the rainbow:

| red is #FF0000
| orange is #FFA500
| yellow is #FFFF00
| green is #008000
| blue is #0000FF
| indigo is #4B0082
| violet is #EE82EE 

.. admonition:: Tasks

    #. Create a dictionary, rainbow_colors, with the colour name as the key and the hex value as the value.

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                Create a dictionary, rainbow_colors, with the colour name as the key and the hex value as the value.

                .. code-block:: python

                     # Dictionary with rainbow colors
                    rainbow_colors = {
                        "red": "#FF0000",
                        "orange": "#FFA500",
                        "yellow": "#FFFF00",
                        "green": "#008000",
                        "blue": "#0000FF",
                        "indigo": "#4B0082",
                        "violet": "#EE82EE"
                    }

User input
~~~~~~~~~~~~~~~~

| For user input see: https://www.w3schools.com/python/ref_func_input.asp

.. admonition:: Tasks

    #. Create a user input that refers to all the possible colors and stores it in the variable, user_color.

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                Create a user input that refers to all the possible colors and stores it in the variable, user_color

                .. code-block:: python

                    user_color = input("Enter a color from the rainbow (red, orange, yellow, green, blue, indigo, violet): ")


Hex colour function
~~~~~~~~~~~~~~~~~~~~~~

A scaffold of a simple function to return the hex value of a colour is below.

.. code-block:: python

    def return_hex_color(user_color):
        # Convert the input to lowercase for case-insensitivity
        user_color = ______________________.lower()

        # Check if the input color exists in the rainbow_colors dictionary
        if user_color in ______________________:
            return rainbow_colors[______________________]
        else:
            return "not a valid colour of the rainbow"


.. admonition:: Tasks

    #. Complete the function to return the hex colour for a named colour.

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                Complete the function to return the hex colour for a named colour.

                .. code-block:: python

                    def return_hex_color(user_color):
                        # Convert the input to lowercase for case-insensitivity
                        user_color = user_color.lower()

                        # Check if the input color exists in the rainbow_colors dictionary
                        if user_color in rainbow_colors:
                            return rainbow_colors[user_color]
                        else:
                            return "not a valid colour of the rainbow"

Final code
~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Exercise

    Create a python file that gets user input and prints the hex colour for the color name the user inputs.
    Example output: ``The hexadecimal value for green is #008000.``

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                Create a python file that gets user input and prints the hex colour for the color name the user inputs.
                Example output: ``The hexadecimal value for green is #008000.``

                .. code-block:: python

                    # Dictionary with rainbow colors
                    rainbow_colors = {
                        "red": "#FF0000",
                        "orange": "#FFA500",
                        "yellow": "#FFFF00",
                        "green": "#008000",
                        "blue": "#0000FF",
                        "indigo": "#4B0082",
                        "violet": "#EE82EE"
                    }

                    user_color = input('Enter a rainbow color (red, orange, yellow, green, blue, indigo, violet): ')

                    def return_hex_color(user_color):
                        # Convert the input to lowercase for case-insensitivity
                        user_color = user_color.lower()

                        # Check if the input color exists in the rainbow_colors dictionary
                        if user_color in rainbow_colors:
                            return rainbow_colors[user_color]
                        else:
                            return "not a valid colour of the rainbow"

                    hex_val = return_hex_color(user_color)
                    print(f"The hexadecimal value for {user_color} is {hex_val}")
