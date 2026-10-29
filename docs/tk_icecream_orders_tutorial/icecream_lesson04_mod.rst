================================================
Radio buttons for flavours
================================================

.. image:: images/icecream_04.png
    :scale: 50

- **Objective**: Make one radio button for each flavour.

----

What are radio buttons?
--------------------------------

- **Radio buttons** let the user pick **one** choice.
- A **StringVar** remembers which one was picked.
- A **loop** makes one button for each flavour in the dictionary.

----

Step 1: Add the label and frame
--------------------------------------

| Paste this below the title code, above ``# --- RIGHT SIDE``.

.. code-block:: python

    # Flavour (radio buttons)
    flavour_label = tk.Label(root)  # 1. create
    flavour_label.grid(row=1, column=0, padx=10, pady=5, sticky="ne")  # 2. position
    flavour_label.config(text="Flavour:", font=LABEL_FONT, bg=BG_COLOUR, fg=TEXT_COLOUR)  # 3. configure

    flavour_frame = tk.Frame(root)  # 1. create
    flavour_frame.grid(row=1, column=1, padx=10, pady=5, sticky="w")  # 2. position
    flavour_frame.config(bg=BG_COLOUR)  # 3. configure

- A **Frame** is an invisible box. The radio buttons go inside it.

----

Step 2: Add the variable
--------------------------------------

| Paste this below the frame code.

.. code-block:: python

    flavour_var = tk.StringVar(root)  # A. make
    flavour_var.set("Vanilla")  # B. set

- ``set("Vanilla")`` picks Vanilla when the app starts.

----

Step 3: Make the radio buttons
--------------------------------------

| Paste this below the variable code.

.. code-block:: python

    for flavour in flavours.keys():
        flavour_radio = tk.Radiobutton(flavour_frame, variable=flavour_var, value=flavour)  # 1. create
        flavour_radio.pack(anchor="w")  # 2. position
        flavour_radio.config(text=f"{flavour} (${flavours[flavour]:.2f})", font=RADIO_FONT,
                             bg=BG_COLOUR, fg=TEXT_COLOUR, activebackground=BG_COLOUR,
                             highlightthickness=0)  # 3. configure

- The loop runs **once for each flavour**.
- ``pack(anchor="w")`` stacks the buttons down the frame.
- The text shows the flavour and price, e.g. "Strawberry ($4.50)". ``:.2f`` means 2 decimal places.

| **Run it.** Five flavour buttons appear. Only one can be picked.

.. tip::

    Add ``"Salted Caramel": 5.50,`` to the ``flavours`` dictionary and run it again. A new button appears.

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

        How many flavours can be picked at once?

        [x] One | Correct. Radio buttons allow one choice.
        [ ] Two | Incorrect. Picking another switches the first off.
        [ ] As many as you like | Incorrect. That is a checkbutton.

    .. multichoice::

        What does flavour_var hold?

        [x] The flavour that is picked | Correct.
        [ ] The price of the flavour | Incorrect. Prices are in the dictionary.
        [ ] Every flavour | Incorrect. It holds one at a time.

    .. multichoice::

        How many radio buttons does the loop make?

        [x] One for each flavour in the dictionary | Correct.
        [ ] Always 3 | Incorrect. It depends on the dictionary.
        [ ] Only one | Incorrect. The loop runs more than once.

    .. multichoice::

        What does :.2f do?

        [x] Shows 2 decimal places | Correct. 4.5 shows as 4.50.
        [ ] Adds 2 to the number | Incorrect.
        [ ] Makes a whole number | Incorrect.

----

Fill in the gaps
--------------------------------

.. clozegroup::
    :nav-position: both
    :num-questions: 1
    :show-instant-feedback:


    .. cloze::
        :instructions: Make one radio button for each flavour.

        flavour_var = tk.@@StringVar | IntVar | Label@@(root)
        flavour_var.@@set | get | config@@("Vanilla")

        for flavour in flavours.@@keys | values | items@@():
            flavour_radio = tk.Radiobutton(flavour_frame, variable=@@flavour_var | flavour | flavours@@, value=flavour)
            flavour_radio.@@pack | grid | set@@(anchor="w")
