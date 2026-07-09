================================================
Multi-Choice Directive Documentation
================================================

The multichoice directive creates an interactive multiple-choice question format. Users can select one or more choices, validate their answers, and receive instant feedback alongside custom written explanations.

Syntax
-------------------

.. code-block:: rst

    .. multichoice::

        Question text goes here...

        [x] Correct option text | Feedback message for correct answer.
        [ ] Incorrect option text | Feedback message for incorrect answer.

Options for the multichoice directive
--------------------------------------

.. list-table::
   :widths: 25 10 65
   :header-rows: 1

   * - Option
     - Type
     - Description
   * - ``:no-letters:``
     - flag
     - If present, hides the alphabetical choice indicators (A, B, C...).
   * - ``:no-shuffle:``
     - flag
     - | If present, forces the multiple choice options to
       | stay fixed in their declared order instead of being randomized.
   * - ``:theme:``
     - string
     - | If present, set the visual theme.
       | Options are ``light`` (default) or ``dark``.


| Shuffling: Unless ``:no-shuffle:`` is declared, choices are automatically randomized on page render and on Reset button clicks to elimin  position-based pattern guessing.
| Selection Engine: The directive automatically changes selection inputs from single-choice radio buttons to multi-choice checkboxes if more than one option is marked correct ``[x]``.
| Visual Badges: Once the evaluation button is selected, clear inline indicator icons (✓, ✕) show up next to each answer option along with context explanations.

----

Example 1: Single Correct (Default)
------------------------------------

| The default configuration renders with automatic letter assignments (A, B, C...) and randomized positioning.

.. code-block:: rst

    .. multichoice::

        Which of these does an equality check in Python?

        [x] == | Correct.
        [ ] = | Incorrect. That does assignment
        [ ] !== | Incorrect. Not equals to
        [ ] <= | Incorrect. Less than or equals to

.. multichoice::

    Which of these does an equality check in Python?

    [x] == | Correct.
    [ ] = | Incorrect. That does assignment
    [ ] !== | Incorrect. Not equals to
    [ ] <= | Incorrect. Less than or equals to

----

Example 2: Single Correct (No Letters)
---------------------------------------

| The following example demonstrates hiding the prefix alphabetical list labeling characters by using the ``:no-letters:`` option flag.

.. code-block:: rst

    .. multichoice::
        :no-letters:

        What is the correct way to print "Hello, World" in Python?

        [x] print("Hello, World") | Correct. print requires brackets.
        [ ] print "Hello, World"
        [ ] echo "Hello, World"
        [ ] echo(Hello, World)

.. multichoice::
    :no-letters:

    What is the correct way to print "Hello, World" in Python?

    [x] print("Hello, World") | Correct. print requires brackets.
    [ ] print "Hello, World"
    [ ] echo "Hello, World"
    [ ] echo(Hello, World)

----

Example 3: Single Correct (Unshuffled)
---------------------------------------

| The following example demonstrates freezing the item choices in their explicitly declared ordering layout via the ``:no-shuffle:`` option flag.

.. code-block:: rst

    .. multichoice::
        :no-shuffle:

        Which of these are valid variable names in Python?

        [x] my_var | Correct. Valid variable name
        [ ] var | Incorrect. Cannot start with a number
        [ ] @var | Incorrect. Cannot start with a symbol
        [ ] my-var | Incorrect. Hyphens are not allowed

.. multichoice::
    :no-shuffle:

    Which of these are valid variable names in Python?

    [x] my_var | Correct. Valid variable name
    [ ] var | Incorrect. Cannot start with a number
    [ ] @var | Incorrect. Cannot start with a symbol
    [ ] my-var | Incorrect. Hyphens are not allowed

----

Example 4: Code Block Layout Inside Question
--------------------------------------------

| The following example demonstrates how to include a code block inside the question text.
| Dark theme is used here to better highlight the code snippet.

.. code-block:: rst

    .. multichoice::
        :theme: dark

        What is the output of the following code?

        .. code-block:: python

            x = 5
            y = 2
            print(x ** y)

        [x] 25 | Correct: `**` is exponentiation, so output is 25
        [ ] 5^2
        [ ] 10
        [ ] 7

.. multichoice::
    :theme: dark

    What is the output of the following code?

    .. code-block:: python

        x = 5
        y = 2
        print(x ** y)

    [x] 25 | Correct: `**` is exponentiation, so output is 25
    [ ] 5^2
    [ ] 10
    [ ] 7

----

Example 5: Code Block Layout Inside Responses
------------------------------------------------

| The following example demonstrates how to include a code block inside the response text.

.. code-block:: rst

    .. multichoice::

        A student wants to display the word "ABC" such that the final character 'C' is removed right away, followed by a brief half-second pause. Which option is correct?
        [ ] .. code-block:: python

                display.show("ABC")
                sleep(500)
            | Incorrect. This does not use clear parameters or clear commands, leaving 'C' stuck on screen.
        [x] .. code-block:: python

                display.show("ABC", clear=True)
                sleep(500)
            | Correct. It automatically removes the last character via clear=True and pauses for 500ms (half a second).
        [ ] .. code-block:: python

                display.show("ABC", clear=False)
                sleep(50)
            | Incorrect. This explicitly stops the character from being cleared, and pauses for only 50ms.
        [ ] .. code-block:: python

                display.show("ABC", delay=500)
            | Incorrect. This merely slows the timing between characters to 500ms instead of creating a final blank screen pause.


.. multichoice::

    A student wants to display the word "ABC" such that the final character 'C' is removed right away, followed by a brief half-second pause. Which option is correct?
    [ ] .. code-block:: python

            display.show("ABC")
            sleep(500)
        | Incorrect. This does not use clear parameters or clear commands, leaving 'C' stuck on screen.
    [x] .. code-block:: python

            display.show("ABC", clear=True)
            sleep(500)
        | Correct. It automatically removes the last character via clear=True and pauses for 500ms (half a second).
    [ ] .. code-block:: python

            display.show("ABC", clear=False)
            sleep(50)
        | Incorrect. This explicitly stops the character from being cleared, and pauses for only 50ms.
    [ ] .. code-block:: python

            display.show("ABC", delay=500)
        | Incorrect. This merely slows the timing between characters to 500ms instead of creating a final blank screen pause.


----

Example 6: Multiple Correct Answers
-----------------------------------

| Checking more than one correct bracket item ``[x]`` automatically swaps from a radio selections to checkboxes.

.. code-block:: rst

    .. multichoice::

        Which of the following are Python data types?

        [x] int | Integer type
        [x] str | String type
        [ ] html | Not a Python type
        [x] float | Floating-point number

.. multichoice::

    Which of the following are Python data types?

    [x] int | Integer type
    [x] str | String type
    [ ] html | Not a Python type
    [x] float | Floating-point number

