================================================
Drop-down menus for containers and toppings
================================================

.. image:: images/icecream_05.png
    :scale: 50

- **Objective**: Add drop-down menus so the user can choose a container and a topping.
- **Content**:

  - What a drop-down menu is.
  - The container drop-down.
  - Adding the choices with a loop.
  - The topping drop-down.

----

What is a drop-down menu?
--------------------------------

| A **drop-down menu** shows one choice. When it is clicked, a list of choices drops down.
| It saves space compared with radio buttons, which is useful when there are lots of choices.
| In Tkinter a drop-down menu is called an ``OptionMenu``.

----

Adding the container drop-down
--------------------------------------

| Place the following code below the flavour radio buttons in Section "4. TKINTER WIDGETS".

.. code-block:: python

    # Container (drop-down menu)
    container_label = tk.Label(root)  # 1. create
    container_label.grid(row=2, column=0, padx=10, pady=5, sticky="e")  # 2. position
    container_label.config(text="Container:", font=LABEL_FONT, bg=BG_COLOUR, fg=TEXT_COLOUR)  # 3. configure

    container_var = tk.StringVar(root)  # A. make
    container_var.set("Cup")  # B. set

    container_menu = tk.OptionMenu(root, container_var, "Cup")  # 1. create
    container_menu.grid(row=2, column=1, padx=10, pady=5, sticky="w")  # 2. position
    container_menu.config(width=16, font=LABEL_FONT, bg=MENU_COLOUR, fg=TEXT_COLOUR,
                          activebackground=MENU_COLOUR)  # 3. configure

    container_choices = container_menu["menu"]
    container_choices.config(font=LABEL_FONT, bg=MENU_COLOUR, fg=TEXT_COLOUR)
    container_choices.delete(0)   # remove the starting choice
    for container in containers.keys():
        container_choices.add_radiobutton(label=container, variable=container_var, value=container)

1. **The label** "Container:" goes in row 2, column 0.

2. **The variable**:

   - ``container_var`` holds the container the user picks.
   - ``container_var.set("Cup")`` chooses Cup when the app starts.
   - The variable must be made **before** the ``OptionMenu``, because the menu needs it.

3. **The drop-down menu**:

   - ``tk.OptionMenu(root, container_var, "Cup")`` makes the menu. It must be given one choice to start with, so we give it ``"Cup"``.
   - ``width=16`` makes the menu 16 characters wide, so it does not change size when a longer choice is picked.
   - ``activebackground`` is the colour when the mouse is over the menu.

4. **The list of choices**:

   - ``container_choices = container_menu["menu"]`` gets the list that drops down, and gives it a short name.
   - ``container_choices.config(...)`` colours that list.
   - ``container_choices.delete(0)`` removes the starting choice (line 0). The loop will add it back, along with all the others.

----

Adding the choices with a loop
--------------------------------------

| This loop works just like the flavour radio buttons in :doc:`icecream_lesson04`.

.. code-block:: python

    for container in containers.keys():
        container_choices.add_radiobutton(label=container, variable=container_var, value=container)

- ``for container in containers.keys():`` repeats once for **each key** in the ``containers`` dictionary.
- ``add_radiobutton`` adds one choice to the list that drops down.
- ``label=container`` is the words the user sees.
- ``variable=container_var, value=container`` sets ``container_var`` to this container when the user picks it.

| Because the choices come from the dictionary, adding a new container to ``containers`` adds it to the menu as well.

----

Adding the topping drop-down
--------------------------------------

| The topping drop-down follows exactly the same pattern. Place this code below the container code.

.. code-block:: python

    # Topping (drop-down menu)
    topping_label = tk.Label(root)  # 1. create
    topping_label.grid(row=3, column=0, padx=10, pady=5, sticky="e")  # 2. position
    topping_label.config(text="Topping:", font=LABEL_FONT, bg=BG_COLOUR, fg=TEXT_COLOUR)  # 3. configure

    topping_var = tk.StringVar(root)  # A. make
    topping_var.set("No topping")  # B. set

    topping_menu = tk.OptionMenu(root, topping_var, "No topping")  # 1. create
    topping_menu.grid(row=3, column=1, padx=10, pady=5, sticky="w")  # 2. position
    topping_menu.config(width=16, font=LABEL_FONT, bg=MENU_COLOUR, fg=TEXT_COLOUR,
                        activebackground=MENU_COLOUR)  # 3. configure

    topping_choices = topping_menu["menu"]
    topping_choices.config(font=LABEL_FONT, bg=MENU_COLOUR, fg=TEXT_COLOUR)
    topping_choices.delete(0)   # remove the starting choice
    for topping in toppings.keys():
        topping_choices.add_radiobutton(label=topping, variable=topping_var, value=topping)

- The topping drop-down goes in row 3.
- Its choices come from the ``toppings`` dictionary.
- Every name starts with ``topping_`` so it is clear which part of the app it belongs to.

| Run the code. Click each drop-down menu and check that all the choices appear.

:download:`icecream_orders_05.py <python/icecream_orders_05.py>`

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

        What is a drop-down menu called in Tkinter?

        [ ] Radiobutton | Incorrect. A radio button shows every choice at once.
        [x] OptionMenu | Correct. An OptionMenu shows one choice and drops down a list of the others.
        [ ] Listbox | Incorrect. A Listbox shows a list of lines, such as the order.
        [ ] DropMenu | Incorrect. There is no widget called DropMenu.

    .. multichoice::

        Where do the choices in the container drop-down come from?

        [x] The keys of the containers dictionary | Correct. The loop adds one choice for each key.
        [ ] The values of the containers dictionary | Incorrect. The values are the prices.
        [ ] The flavours dictionary | Incorrect. The flavours are shown as radio buttons.
        [ ] They are typed into the OptionMenu one by one | Incorrect. Only the starting choice is typed in. The loop adds the rest.

    .. multichoice::

        Why must container_var be made before container_menu?

        [ ] Variables always go at the top of the program | Incorrect. It goes straight before the menu that uses it.
        [x] The OptionMenu needs the variable when it is created | Correct. container_var is passed in when the menu is made.
        [ ] It makes the menu pink | Incorrect. The colour comes from MENU_COLOUR.
        [ ] It does not matter | Incorrect. Python would give an error if the variable did not exist yet.

    .. multichoice::

        Why does the code use container_choices.delete(0)?

        [ ] To delete the containers dictionary | Incorrect. The dictionary does not change.
        [x] To remove the starting choice, so the loop does not add Cup twice | Correct. The loop adds every key, including Cup.
        [ ] To clear the order | Incorrect. The order is not touched.
        [ ] To make the menu narrower | Incorrect. width=16 sets the width.

    .. multichoice::

        What does add_radiobutton do?

        [ ] Adds a radio button to the window | Incorrect. It adds a choice inside the drop-down list.
        [x] Adds one choice to the list that drops down | Correct. Each time the loop runs, one more choice is added.
        [ ] Picks a container for the user | Incorrect. The user picks the container.
        [ ] Adds a new key to the dictionary | Incorrect. The dictionary does not change.

    .. multichoice::

        A new key "Choc-dipped cone": 2.00 is added to containers. What happens to the drop-down?

        [x] The new choice appears in the menu | Correct. The loop makes one choice for every key, so the menu always matches the dictionary.
        [ ] Nothing, unless it is typed into the OptionMenu too | Incorrect. The loop reads the keys from the dictionary.
        [ ] The program crashes | Incorrect. The loop works with any number of keys.
        [ ] It replaces Cup | Incorrect. It is added as a new choice.

----

Fill in the gaps
--------------------------------

.. clozegroup::
    :nav-position: both
    :num-questions: 1
    :show-instant-feedback:


    .. cloze::
        :instructions: Make the topping drop-down menu and add its choices.

        topping_var = tk.StringVar(root)
        topping_var.set("No topping")

        topping_menu = tk.@@OptionMenu | Radiobutton | Listbox@@(root, @@topping_var | toppings | topping_menu@@, "No topping")
        topping_menu.grid(row=3, column=1, padx=10, pady=5, sticky="w")

        topping_choices = topping_menu["menu"]
        topping_choices.@@delete | clear | remove@@(0)
        for topping in toppings.@@keys | values | set@@():
            topping_choices.add_radiobutton(label=topping, variable=topping_var, value=@@topping | toppings | topping_var@@)
