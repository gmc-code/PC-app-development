====================================================
Dictionary with functions
====================================================

Dictionaries
-------------------

| A dictionary is a collection of ``key: value`` pairs. 
| All keys are unique; duplicate keys are not possible. 
| Keys can be an integer, float, string, Boolean (True or False) and even a tuple.
| To retrieve a value from a dictionary, use the key as an index.
| See: https://v2.scrimba.com/learn-python-c03/~014


Example dictionary
-------------------------

| The game_register dictionary uses {} brackets.
| Each key value pair is separated by a comma.
| Each key is followed by a colon, :.
| The first key value pair is 'googolplex': 100.
| There are 4 keys: 'googolplex', 'terminat0r', 'ace', 'teapot418'
| There are 4 values: 100, 27, 150, 0

.. code-block:: python

    game_register = {'googolplex': 100,
                    'terminat0r': 27,
                    'ace': 150,
                    'teapot418' : 0 } 


Example dictionary methods
----------------------------

.. code-block:: python

    game_register = {'googolplex': 100,
                    'terminat0r': 27,
                    'ace': 150,
                    'teapot418' : 0 }

    # print items as tuples in a list like format.
    items = game_register.items()
    print("items", items)
    
    # print keys
    keys = game_register.keys()
    print("keys", keys)

    # print values
    values = game_register.values()
    print("values", values)

    # Access elements
    value = game_register['ace']
    print('ace', value)
    value = game_register.get('ace')
    print('ace', value)

    # Retrieve a value for the key or default if not in dictionary
    value = game_register.get('aced', 0)
    print('aced', value)

    # Add or update and existing entry
    game_register['ace'] = 50
    value = game_register['ace']
    print('ace', value)

    # Delete an entry
    del game_register['ace']
    value = game_register.get('ace', "no entry")
    print('ace', value)

    # check if key exists
    key_exists = "googolplex" in game_register
    print("googolplex", key_exists)
    key_exists = "ace" in game_register
    print("ace", key_exists)

    # Delete all entries
    game_register.clear()
    dict_len = len(game_register)
    print("dict length", dict_len)


    # check if dictionary exists in local variables
    try:
        game_register
        print("The game_register dictionary still exists.")
    except NameError:
        print("The game_register dictionary has been deleted.")
    # Delete the dictionary
    del game_register
    # check if dictionary exists in local variables
    try:
        game_register
        print("The game_register dictionary still exists.")
    except NameError:
        print("The game_register dictionary has been deleted.")


----

Definition to get a dictionary value
-----------------------------------------

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


----

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


