================================================
Constants: colours and fonts
================================================

.. image:: images/icecream_03.png
    :scale: 50

- **Objective**: Store the colours and fonts as constants, then use them to make the title and the order heading.
- **Content**:

  - What a constant is.
  - Colour codes.
  - Font tuples.
  - The title label and order heading.

----

What is a constant?
--------------------------------

| A **constant** is a variable whose value does not change while the program runs.
| Python programmers write constant names in **CAPITAL LETTERS**, so they are easy to spot.
| Keeping every colour and font as a constant in one place means you can change the look of the whole app by changing a few lines.

----

Adding the constants
--------------------------------

| Place the following code in Section "2. CONSTANTS", below the dictionaries and the list.

.. code-block:: python

    # Colours
    BG_COLOUR = "#fff4e6"        # cream background
    TITLE_COLOUR = "#d94f70"     # strawberry pink title
    TEXT_COLOUR = "#4a2c2a"      # chocolate brown text
    MENU_COLOUR = "#ffd6e0"      # pale pink drop-down menus
    LIST_COLOUR = "#ffffff"      # white order list
    ADD_COLOUR = "#c8f0c8"       # pale green add button
    REMOVE_COLOUR = "#ffd6d6"    # pale red remove and clear buttons

    # Fonts
    TITLE_FONT = ("Segoe UI", 22, "bold")
    LABEL_FONT = ("Segoe UI", 13, "normal")
    RADIO_FONT = ("Segoe UI", 12, "normal")
    LIST_FONT = ("Segoe UI", 12, "normal")
    BUTTON_FONT = ("Segoe UI", 12, "bold")

- **Colour codes** such as ``"#fff4e6"`` are hex codes. The six characters give the amount of **red**, **green** and **blue**, from ``00`` (none) to ``ff`` (full).
- ``"#ffffff"`` is white and ``"#000000"`` is black. Search for "colour picker" online to find codes for any colour.
- **Fonts** are written as a **tuple** of three things in round brackets: the font name, the size, and the style (``"normal"`` or ``"bold"``).
- The colours were chosen to match the product: cream, strawberry pink and chocolate brown.

----

Colouring the window
--------------------------------

| Add this line in Section "4. TKINTER WIDGETS", directly below ``root.geometry("940x520")``.

.. code-block:: python

    root.config(bg=BG_COLOUR)

- ``bg`` means **background**. The whole window is now cream.

----

Adding the title label
--------------------------------

| Place the following code below the main window code in Section "4. TKINTER WIDGETS".
| Notice the three lines: **create**, **position**, **configure**.
| The comments at the end of each line, such as ``# 1. create``, show the steps from :doc:`icecream_lesson01`. You can type them too.

.. code-block:: python

    # --- LEFT SIDE: ICE CREAM CHOICES ---

    # Title
    title_label = tk.Label(root)  # 1. create
    title_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="w")  # 2. position
    title_label.config(text="Ice Cream Shop", font=TITLE_FONT, bg=BG_COLOUR, fg=TITLE_COLOUR)  # 3. configure

1. **Create**: ``tk.Label(root)`` makes a label inside the window ``root``.
2. **Position**: ``grid(row=0, column=0, columnspan=2, ...)`` puts the label in the top row, covering columns 0 and 1.

   - ``padx=10`` and ``pady=10`` leave 10 pixels of space around the label.
   - ``sticky="w"`` pushes the label to the **west** (left) side of its cells.

3. **Configure**: ``config(...)`` sets the label's text, font and colours.

   - ``fg`` means **foreground**, which is the colour of the text.

----

Adding the order heading
--------------------------------

| The right side of the window will show the order. Place this code below the title code.

.. code-block:: python

    # --- RIGHT SIDE: THE ORDER ---

    # Order heading
    order_heading = tk.Label(root)  # 1. create
    order_heading.grid(row=0, column=2, columnspan=2, padx=10, pady=10, sticky="sw")  # 2. position
    order_heading.config(text="Your order", font=LABEL_FONT, bg=BG_COLOUR, fg=TEXT_COLOUR)  # 3. configure

- The heading goes in row 0, covering columns 2 and 3, just like the planning grid shows.
- ``sticky="sw"`` pushes it to the **south-west** (bottom left) of its cells, so it sits just above the order list.

| Run the code. The title and the heading should appear on a cream background.

:download:`icecream_orders_03.py <python/icecream_orders_03.py>`

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

        Why are constant names written in CAPITAL LETTERS?

        [x] So programmers can see they are constants that should not change | Correct. Capital letters are a naming habit that marks a constant.
        [ ] Python needs capital letters for colours | Incorrect. Python would still run with lower-case names.
        [ ] Capital letters make the text bigger | Incorrect. The font size sets how big the text is.
        [ ] So they run faster | Incorrect. The name does not change how fast the code runs.

    .. multichoice::

        Where do the constants go in the code?

        [ ] Above the imports | Incorrect. Imports always come first.
        [ ] After the widgets | Incorrect. Widgets use the constants, so the constants must come first.
        [x] After the dictionaries, before the definitions | Correct. This is Section 2 of the code.
        [ ] Inside each widget | Incorrect. Constants are kept together in one place.

    .. multichoice::

        What does fg=TITLE_COLOUR change?

        [ ] The background colour | Incorrect. bg sets the background colour.
        [x] The colour of the text | Correct. fg means foreground, which is the text colour.
        [ ] The font | Incorrect. font= sets the font.
        [ ] The size of the label | Incorrect. fg only sets a colour.

    .. multichoice::

        ("Segoe UI", 22, "bold") is a font tuple. What is 22?

        [ ] The colour | Incorrect. Colours are hex codes such as "#d94f70".
        [ ] The row number | Incorrect. Rows are set with grid().
        [x] The size of the text | Correct. The second item in a font tuple is its size.
        [ ] The number of letters | Incorrect. The text can be any length.

    .. multichoice::

        What does columnspan=2 do?

        [ ] Puts the widget in column 2 | Incorrect. column=2 does that.
        [x] Makes the widget cover two columns | Correct. The title covers columns 0 and 1.
        [ ] Adds 2 pixels of space | Incorrect. padx and pady add space.
        [ ] Makes two copies of the widget | Incorrect. There is still only one widget.

----

Fill in the gaps
--------------------------------

.. clozegroup::
    :nav-position: both
    :num-questions: 1
    :show-instant-feedback:


    .. cloze::
        :instructions: Create the title label, position it, then configure it.

        title_label = tk.@@Label | Button | Title@@(root)
        title_label.@@grid | config | place@@(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="w")
        title_label.@@config | grid | text@@(text="Ice Cream Shop", font=@@TITLE_FONT | TITLE_COLOUR | BG_COLOUR@@, bg=BG_COLOUR, fg=TITLE_COLOUR)
