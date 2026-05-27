====================================================
Using Entry Boxes in Tkinter
====================================================

The ``tk.Entry`` widget creates a text box that allows users to type in information (like names, ages, or scores).

----

Validating Input (Numbers Only)
--------------------------------

| Sometimes you want to force the user to type *only* numbers (for example, when asking for an age).
| We can block letters from being typed entirely.

To do this, we use two special settings:
* ``validate='key'``: Checks the text every single time a key is pressed.
* ``validatecommand``: Tells Tkinter which function to use to check the text.
* ``'%P'``: A special code that tells Tkinter to pass the **proposed new text** to our function *before* it appears on the screen.

Simple Number Validation
~~~~~~~~~~~~~~~~~~~~~~~~~

This script only allows the user to type numbers. If they press a letter key, nothing will happen!

.. code-block:: python

    import tkinter as tk

    def check_number(new_text):
        # Allow the box to be empty, OR check if the new text is a number
        if new_text == "" or new_text.isdigit():
            return True   # True means "allow the change"
        else:
            return False  # False means "reject the keystroke"

    root = tk.Tk()
    root.title("Numbers Only")
    root.geometry("400x200")

    # Register our validation function with Tkinter
    vcmd = (root.register(check_number), '%P')

    # Create the entry box with validation turned on
    entry = tk.Entry(root, font=("Arial", 20), validate='key', validatecommand=vcmd)
    entry.pack(pady=40)

    root.mainloop()

----

.. admonition:: Tasks

    1. Modify the validation rules so that a user can type a number, but limits the entry to a maximum of 2 digits total.

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Task 1 Solution

                We use ``len(new_text)`` to ensure the user cannot type more than 2 characters.

                .. code-block:: python

                    import tkinter as tk

                    def validate_two_digits(new_text):
                        if new_text == "":
                            return True  # Allow deleting text completely
                        # Check if it is a number AND has 2 or fewer digits
                        if new_text.isdigit() and len(new_text) <= 2:
                            return True
                        else:
                            return False  # Reject letters or a 3rd digit

                    root = tk.Tk()
                    root.title("2-Digit Validator")
                    root.geometry("400x200")

                    vcmd = (root.register(validate_two_digits), '%P')

                    entry = tk.Entry(root, font=("Arial", 20), validate='key', validatecommand=vcmd)
                    entry.pack(pady=40)

                    root.mainloop()


    2. Modify the validation rules so that the entry box accepts numbers, but limits the entry to a maximum age of 120.

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Task 2 Solution

                We can convert ``new_text`` into an integer using ``int()`` to check if it fits within our 0-120 range.

                .. code-block:: python

                    import tkinter as tk

                    def validate_age(new_text):
                        if new_text == "":
                            return True  # Allow deleting text completely
                        if new_text.isdigit():
                            age = int(new_text)
                            # Only allow if the number is between 0 and 120
                            if 0 <= age <= 120:
                                return True
                            else:
                                return False
                        else:
                            return False   # Reject letters

                    root = tk.Tk()
                    root.title("Age Validator (0-120)")
                    root.geometry("400x200")

                    vcmd = (root.register(validate_age), '%P')

                    entry = tk.Entry(root, font=("Arial", 20), validate='key', validatecommand=vcmd)
                    entry.pack(pady=40)

                    root.mainloop()

    3. Modify the validation rules so that the entry box only accepts numbers from -9 to +9.

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Task 3 Solution

                We allow the user to type a single ``-`` or ``+`` sign first, and then check if the total value is between -9 and +9.

                .. code-block:: python

                    import tkinter as tk

                    def validate_range(new_text):
                        if new_text == "":
                            return True  # Allow deleting text completely
                        # Allow just a minus or plus sign so the user can start typing
                        if new_text in ["-", "+"]:
                            return True
                        # Check if the text is a valid number
                        try:
                            num = int(new_text)
                            # Only allow if the number is between -9 and +9
                            return -9 <= num <= 9
                        except ValueError:
                            return False  # Reject letters or invalid symbols

                    root = tk.Tk()
                    root.title("Single Digit Validator (-9 to +9)")
                    root.geometry("400x200")

                    vcmd = (root.register(validate_range), '%P')

                    entry = tk.Entry(root, font=("Arial", 20), validate='key', validatecommand=vcmd)
                    entry.pack(pady=40)

                    root.mainloop()
