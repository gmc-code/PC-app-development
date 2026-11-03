====================================================
ttk Progressbar
====================================================

| See: `<https://docs.python.org/3/library/tkinter.ttk.html#progressbar>`_

----

What is a Progressbar?
-------------------------

| A **Progressbar** is a bar that fills up to show how much of a job is done, like a download bar or a loading bar.
| It can also show a health bar, a battery level or a quiz score. tk has no Progressbar; it only comes with ttk.

----

Making a Progressbar
-----------------------

.. code-block:: python

    import tkinter as tk            # Load tkinter
    from tkinter import ttk         # Load the themed widgets

    root = tk.Tk()                  # Make the window
    root.geometry("300x200")
    root.title("My first Progressbar")

    bar = ttk.Progressbar(root, length=250, maximum=100, value=40)   # 1. Create it: 40 out of 100
    bar.pack(pady=40)                                                # 2. Place it

    root.mainloop()                 # Keep the window open

----

Progressbar options
----------------------

length
~~~~~~~~~~~~~~~~~~

| **What it does:** sets how long the bar is, in pixels.
| **How to write it:** ``length=250``

maximum and value
~~~~~~~~~~~~~~~~~~~~

| **What they do:** ``maximum`` is the number that means **full** (the default is 100). ``value`` is how full the bar is now.
| **How to write them:** ``maximum=10, value=7`` shows 7 out of 10.

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("maximum and value")

    ttk.Label(root, text="Quiz score: 7 out of 10").pack(pady=10)
    ttk.Progressbar(root, length=250, maximum=10, value=7).pack()

    ttk.Label(root, text="Download: 25 out of 100").pack(pady=10)
    ttk.Progressbar(root, length=250, value=25).pack()

    root.mainloop()

orient
~~~~~~~~~~~~~~~~~~

| **What it does:** chooses side-to-side (``"horizontal"``, the default) or up-and-down (``"vertical"``). A vertical bar fills from the bottom.
| **How to write it:** ``orient="vertical"``

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("orient")

    for level in [20, 50, 80]:
        ttk.Progressbar(root, orient="vertical", length=150, value=level).pack(side="left", padx=30)

    root.mainloop()

mode
~~~~~~~~~~~~~~~~~~

| **What it does:** chooses the kind of bar.
| **Values:**

- ``"determinate"`` - shows **how much** is done (the default).
- ``"indeterminate"`` - a block that slides back and forth to show "something is happening" when you do not know how long it will take.

| **How to write it:** ``mode="indeterminate"`` (use ``start()`` to make it move; see below).

variable
~~~~~~~~~~~~~~~~~~

| **What it does:** links the bar to a variable. Changing the variable with ``.set()`` changes the bar.
| **How to write it:** ``health = tk.IntVar(value=100)`` then ``variable=health``

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk


    def take_damage():
        health.set(max(health.get() - 10, 0))       # Go down 10, but not below 0


    def heal():
        health.set(100)


    root = tk.Tk()
    root.geometry("300x200")
    root.title("variable")

    health = tk.IntVar(value=100)

    ttk.Label(root, text="Health").pack(pady=5)
    ttk.Progressbar(root, length=250, variable=health).pack()
    ttk.Label(root, textvariable=health, font=("Arial", 16)).pack()

    ttk.Button(root, text="Take damage", command=take_damage).pack(pady=2)
    ttk.Button(root, text="Heal", command=heal).pack()

    root.mainloop()

----

Progressbar methods
----------------------

config(value=...)
~~~~~~~~~~~~~~~~~~~~

| **What it does:** changes how full the bar is. ``bar["value"]`` is a short way to read or change it.
| **How to write it:** ``bar.config(value=60)`` or ``bar["value"] = 60``

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk


    def answer_question():
        if bar["value"] < bar["maximum"]:
            bar["value"] = bar["value"] + 1
            count_label.config(text=f"Questions done: {int(bar['value'])} of 5")


    root = tk.Tk()
    root.geometry("300x200")
    root.title("value")

    bar = ttk.Progressbar(root, length=250, maximum=5, value=0)
    bar.pack(pady=20)

    count_label = ttk.Label(root, text="Questions done: 0 of 5")
    count_label.pack()

    ttk.Button(root, text="Answer a question", command=answer_question).pack(pady=10)

    root.mainloop()

step
~~~~~~~~~~~~~~~~~~

| **What it does:** adds an amount to the bar. When it goes past the maximum it starts again from 0.
| **How to write it:** ``bar.step(10)``

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("step")

    bar = ttk.Progressbar(root, length=250)
    bar.pack(pady=30)

    ttk.Button(root, text="Add 10", command=lambda: bar.step(10)).pack()

    root.mainloop()

| ``step(10)`` adds 10 each click. After 100 the bar goes back to the start.

start and stop
~~~~~~~~~~~~~~~~~

| **What they do:** ``bar.start()`` makes the bar move by itself. ``bar.stop()`` stops it and empties it.
| **How to write them:** ``bar.start(20)`` moves every 20 milliseconds (a smaller number is faster).
| With ``mode="indeterminate"`` a block slides back and forth. With ``"determinate"`` the bar fills again and again.

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("start and stop")

    ttk.Label(root, text="Loading...").pack(pady=10)

    loading_bar = ttk.Progressbar(root, length=250, mode="indeterminate")
    loading_bar.pack()

    ttk.Button(root, text="Start", command=lambda: loading_bar.start(10)).pack(pady=5)
    ttk.Button(root, text="Stop", command=loading_bar.stop).pack()

    root.mainloop()

Filling the bar with after
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| ``root.after(milliseconds, function)`` runs a function after a short wait. If the function calls ``after`` again, it repeats. This fills the bar smoothly and **stops** when it is full.

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk


    def fill():
        if bar["value"] < 100:
            bar["value"] = bar["value"] + 2
            percent_label.config(text=f"{int(bar['value'])}%")
            root.after(50, fill)                    # Run again in 50 milliseconds
        else:
            percent_label.config(text="Download complete!")


    def begin():
        bar["value"] = 0
        fill()


    root = tk.Tk()
    root.geometry("300x200")
    root.title("Download")

    bar = ttk.Progressbar(root, length=250)
    bar.pack(pady=20)

    percent_label = ttk.Label(root, text="0%", font=("Arial", 14))
    percent_label.pack()

    ttk.Button(root, text="Download", command=begin).pack(pady=10)

    root.mainloop()

A countdown timer
~~~~~~~~~~~~~~~~~~~~

| The bar empties as the seconds count down.

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk

    seconds_left = 10


    def tick():
        global seconds_left
        if seconds_left > 0:
            seconds_left = seconds_left - 1
            timer_bar["value"] = seconds_left
            time_label.config(text=f"{seconds_left} seconds left")
            root.after(1000, tick)                  # 1000 milliseconds = 1 second
        else:
            time_label.config(text="Time's up!")


    root = tk.Tk()
    root.geometry("300x200")
    root.title("Countdown")

    timer_bar = ttk.Progressbar(root, length=250, maximum=10, value=10)
    timer_bar.pack(pady=30)

    time_label = ttk.Label(root, text="10 seconds left", font=("Arial", 16))
    time_label.pack()

    root.after(1000, tick)                          # Start counting after 1 second

    root.mainloop()

----

Styling a Progressbar
------------------------

| The style is ``"Horizontal.TProgressbar"`` (or ``"Vertical.TProgressbar"``). With the ``"clam"`` theme:

- ``background`` - the colour of the filled part
- ``troughcolor`` - the colour of the empty part
- ``thickness`` - how thick the bar is, in pixels
- ``bordercolor``, ``lightcolor``, ``darkcolor`` - the edges; set them to the same colour as ``background`` for a flat look

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("Progressbar style")

    style = ttk.Style()
    style.theme_use("clam")
    style.configure("Horizontal.TProgressbar", background="green", troughcolor="lightgray",
                    thickness=25)
    style.configure("Red.Horizontal.TProgressbar", background="red", lightcolor="red",
                    darkcolor="red", troughcolor="mistyrose", thickness=25)

    ttk.Label(root, text="Battery").pack(pady=5)
    ttk.Progressbar(root, length=250, value=80).pack()

    ttk.Label(root, text="Health").pack(pady=5)
    ttk.Progressbar(root, length=250, value=20, style="Red.Horizontal.TProgressbar").pack()

    root.mainloop()

Changing colour as it fills
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| Swap the style with ``config(style=...)`` when the value changes.

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk


    def update(value):
        level = int(float(value))
        bar["value"] = level
        if level < 30:
            bar.config(style="Low.Horizontal.TProgressbar")
        elif level < 70:
            bar.config(style="Mid.Horizontal.TProgressbar")
        else:
            bar.config(style="High.Horizontal.TProgressbar")


    root = tk.Tk()
    root.geometry("300x200")
    root.title("Traffic light bar")

    style = ttk.Style()
    style.theme_use("clam")
    style.configure("Low.Horizontal.TProgressbar", background="red", thickness=25)
    style.configure("Mid.Horizontal.TProgressbar", background="orange", thickness=25)
    style.configure("High.Horizontal.TProgressbar", background="green", thickness=25)

    bar = ttk.Progressbar(root, length=250, style="Low.Horizontal.TProgressbar")
    bar.pack(pady=20)

    ttk.Label(root, text="Drag the slider:").pack()
    ttk.Scale(root, from_=0, to=100, length=250, command=update).pack(pady=5)

    root.mainloop()

----

Quick reference
-------------------

.. list-table::
    :header-rows: 1
    :widths: 25 45 30

    * - Option or method
      - What it does
      - Example
    * - ``length``
      - Length in pixels
      - ``length=250``
    * - ``maximum``
      - The number that means full
      - ``maximum=10``
    * - ``value``
      - How full the bar is
      - ``value=7``
    * - ``orient``
      - Side to side or up and down
      - ``orient="vertical"``
    * - ``mode``
      - Shows amount, or "busy" sliding block
      - ``mode="indeterminate"``
    * - ``variable``
      - Link to an IntVar
      - ``variable=health``
    * - ``bar["value"]``
      - Read or change the value
      - ``bar["value"] = 60``
    * - ``step()``
      - Add an amount
      - ``bar.step(10)``
    * - ``start()``, ``stop()``
      - Move by itself, stop moving
      - ``bar.start(20)``
    * - ``"Horizontal.TProgressbar"``
      - Style name
      - ``style.configure("Horizontal.TProgressbar", background="green")``

----

All Progressbar options
---------------------------

| Here is every option a ttk Progressbar can have, for reference. You will only need a few of them most of the time.

.. list-table::
    :header-rows: 1
    :widths: 25 45 30

    * - Option
      - What it does
      - Example
    * - ``class_``
      - A group name used to style many widgets at once (advanced). Written ``class_`` in Python
      - ``class_="Sidebar"``
    * - ``cursor``
      - Mouse pointer shape over it
      - ``cursor="hand2"``
    * - ``length``
      - How long the bar is (in pixels)
      - ``length=200``
    * - ``maximum``
      - The value that means full (default ``100``)
      - ``maximum=100``
    * - ``mode``
      - ``"determinate"`` (fills up to show progress) or ``"indeterminate"`` (a block bounces back and forth)
      - ``mode="indeterminate"``
    * - ``orient``
      - Which way it goes: ``"horizontal"`` or ``"vertical"``
      - ``orient="horizontal"``
    * - ``phase``
      - Used by some themes to animate the bar (rarely needed)
      - ``phase=0``
    * - ``style``
      - Name of the style that sets its look
      - ``style="Big.TProgressbar"``
    * - ``takefocus``
      - Whether the Tab key can move to it
      - ``takefocus=0``
    * - ``value``
      - How full the bar is right now
      - ``value=40``
    * - ``variable``
      - A variable that holds how full the bar is
      - ``variable=progress``

| ttk Progressbar has no ``bg``, ``fg`` or ``font`` options. Change its colours and fonts with a style, e.g. ``style.configure("Horizontal.TProgressbar", background="green")``.

----

Quiz
--------------------------------

.. mcqgroup::
    :nav_position: top
    :show-instant-feedback:
    :enable-instant-feedback:
    :shuffle_questions:
    :num_questions: 20

    .. multichoice::

        What is a Progressbar?

        [x] A bar that fills up to show how much of a job is done | Correct. Like a download bar.
        [ ] A slider the user drags | Incorrect. That is a Scale.
        [ ] A list of steps | Incorrect. Not a list.
        [ ] A timer | Incorrect. It shows progress.

    .. multichoice::

        What does length=300 do?

        [ ] Sets the maximum | Incorrect. maximum does that.
        [x] Makes the bar 300 pixels long | Correct. length sets its size.
        [ ] Fills it to 300 | Incorrect. value fills it.
        [ ] Sets the speed | Incorrect. Not related.

    .. multichoice::

        What does maximum=100 mean?

        [x] A value of 100 means the bar is full | Correct. 100 is the default.
        [ ] The bar is 100 pixels | Incorrect. length does that.
        [ ] It fills in 100 seconds | Incorrect. Not about time.
        [ ] It can only be used 100 times | Incorrect. Not related.

    .. multichoice::

        If maximum=50 and value=25, how full is the bar?

        [ ] Full | Incorrect. 25 of 50 is half.
        [x] Half full | Correct. 25 is half of 50.
        [ ] A quarter full | Incorrect. That would be 12.5.
        [ ] Empty | Incorrect. 25 is more than 0.

    .. multichoice::

        What does orient="vertical" do?

        [ ] Makes it go left to right | Incorrect. That is horizontal.
        [x] Makes the bar stand up and fill from the bottom | Correct. vertical goes up and down.
        [ ] Hides it | Incorrect. It sets direction.
        [ ] Makes it bounce | Incorrect. mode does that.

    .. multichoice::

        What does mode="determinate" do?

        [x] Fills the bar to show how much is done | Correct. Use it when you know the progress.
        [ ] Bounces a block back and forth | Incorrect. That is indeterminate.
        [ ] Hides the bar | Incorrect. It shows progress.
        [ ] Stops the bar | Incorrect. stop does that.

    .. multichoice::

        When should mode="indeterminate" be used?

        [ ] When the progress is known exactly | Incorrect. Use determinate.
        [x] When you do not know how long the job will take | Correct. A block moves back and forth.
        [ ] Never | Incorrect. It is useful.
        [ ] Only when vertical | Incorrect. Any direction.

    .. multichoice::

        What does variable=progress do?

        [ ] Sets the colour | Incorrect. A style does that.
        [x] Links the bar to a variable, so progress.set(50) fills it | Correct. The bar follows the variable.
        [ ] Sets the length | Incorrect. length does that.
        [ ] Names the bar | Incorrect. It links a variable.

    .. multichoice::

        Which line fills the bar to 75?

        [x] bar.config(value=75) | Correct. Or bar["value"] = 75.
        [ ] bar.set(75) | Incorrect. Progressbars have no set method.
        [ ] bar.fill(75) | Incorrect. Not a method.
        [ ] bar.value(75) | Incorrect. Not a method.

    .. multichoice::

        What does bar.step(10) do?

        [ ] Sets the value to 10 | Incorrect. It adds.
        [x] Adds 10 to the value | Correct. step moves it forward.
        [ ] Moves 10 pixels | Incorrect. It adds to the value.
        [ ] Takes 10 away | Incorrect. It adds.

    .. multichoice::

        What happens when step goes past maximum?

        [ ] An error happens | Incorrect. No error.
        [x] It goes back to the start and keeps going | Correct. The value wraps round.
        [ ] It stops at maximum | Incorrect. It wraps.
        [ ] The bar disappears | Incorrect. It wraps.

    .. multichoice::

        What does bar.start() do?

        [x] Makes the bar move by itself | Correct. It keeps stepping on a timer.
        [ ] Sets the value to 0 | Incorrect. It starts moving.
        [ ] Opens a window | Incorrect. It moves the bar.
        [ ] Only works in determinate mode | Incorrect. It is often used with indeterminate.

    .. multichoice::

        What does bar.stop() do?

        [ ] Deletes the bar | Incorrect. It stops moving.
        [x] Stops the bar moving on its own | Correct. It ends start().
        [ ] Fills the bar | Incorrect. It stops.
        [ ] Closes the program | Incorrect. It stops the bar.

    .. multichoice::

        What does start(20) mean?

        [ ] Start at 20 | Incorrect. It sets the timing.
        [x] Move one step every 20 milliseconds | Correct. The number is the time between steps.
        [ ] Move 20 steps | Incorrect. It sets the timing.
        [ ] Start in 20 seconds | Incorrect. Milliseconds between steps.

    .. multichoice::

        How can root.after fill the bar a bit at a time?

        [x] A function adds to value, then calls root.after(100, itself) until full | Correct. after repeats the function.
        [ ] root.after fills it at once | Incorrect. It waits, then runs.
        [ ] root.after stops the bar | Incorrect. It runs a function later.
        [ ] It cannot | Incorrect. It can.

    .. multichoice::

        For a 10-second countdown, what should maximum be?

        [ ] 100 | Incorrect. Use the number of seconds.
        [x] 10 | Correct. One step for each second.
        [ ] 1 | Incorrect. Too small.
        [ ] 60 | Incorrect. That is a minute.

    .. multichoice::

        How do you change the bar colour?

        [ ] bar.config(bg="green") | Incorrect. ttk has no bg.
        [x] style.configure("Horizontal.TProgressbar", background="green") | Correct. The bar colour comes from the style.
        [ ] bar.colour("green") | Incorrect. Not a method.
        [ ] bar.config(fill="green") | Incorrect. Not an option.

    .. multichoice::

        Which style name is used for a horizontal Progressbar?

        [x] "Horizontal.TProgressbar" | Correct. The direction is part of the name.
        [ ] "TProgressbar" | Incorrect. It needs the direction.
        [ ] "Progress" | Incorrect. Not the name.
        [ ] "TBar" | Incorrect. Not the name.

    .. multichoice::

        How can the bar change colour as it fills?

        [ ] It does it by itself | Incorrect. You must change it.
        [x] Check the value and switch the bar to a different style | Correct. e.g. red style when low, green when high.
        [ ] Use mode="colour" | Incorrect. Not a mode.
        [ ] It cannot | Incorrect. It can, with styles.

    .. multichoice::

        Can the user drag a Progressbar?

        [ ] Yes | Incorrect. It only shows progress.
        [x] No, it only shows progress; use a Scale for dragging | Correct. The program controls it.
        [ ] Only when vertical | Incorrect. Still no.
        [ ] Only in indeterminate mode | Incorrect. Still no.

----

Fill in the gaps
--------------------------------

.. clozegroup::
    :nav-position: top
    :num-questions: 5
    :show-instant-feedback:


    .. cloze::
        :instructions: Make a Progressbar.

        bar = ttk.@@Progressbar | Scale | Scrollbar@@(root, @@length | width | size@@=300, @@maximum | to | max@@=100)
        bar.pack(pady=10)

    .. cloze::
        :instructions: Fill the bar from code.

        bar.config(@@value | fill | level@@=50)
        bar.@@step | add | move@@(10)

    .. cloze::
        :instructions: Make a bouncing bar.

        busy = ttk.Progressbar(root, @@mode | style | type@@="indeterminate")
        busy.@@start | run | go@@(20)
        busy.@@stop | end | pause@@()

    .. cloze::
        :instructions: Fill the bar with after.

        def fill():
            if bar["value"] < 100:
                bar["value"] = bar["value"] + @@10 | 100 | 0@@
                root.@@after | wait | sleep@@(200, fill)

    .. cloze::
        :instructions: Colour the bar green.

        style = ttk.Style()
        style.configure("@@Horizontal.TProgressbar | TProgressbar.Horizontal | Progress@@", @@background | bg | colour@@="green")

----

.. admonition:: Tasks

    #. Make a window titled "Progress" that is 300x200 with a Progressbar 250 pixels long showing 3 out of 5.
    #. Add a button "Next" that adds 1 to the bar each time it is clicked, and a label that shows the value.
    #. Make an indeterminate Progressbar with "Start" and "Stop" buttons.
    #. Make a Progressbar that fills by itself from 0 to 100 using ``after`` when the program starts, then shows "Ready!" in a label.

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                .. code-block:: python

                    import tkinter as tk
                    from tkinter import ttk

                    root = tk.Tk()
                    root.geometry("300x200")
                    root.title("Progress")

                    bar = ttk.Progressbar(root, length=250, maximum=5, value=3)
                    bar.pack(pady=40)

                    root.mainloop()

            .. tab-item:: Q2

                .. code-block:: python

                    import tkinter as tk
                    from tkinter import ttk


                    def next_step():
                        if bar["value"] < 5:
                            bar["value"] = bar["value"] + 1
                            value_label.config(text=f"{int(bar['value'])} of 5")


                    root = tk.Tk()
                    root.geometry("300x200")
                    root.title("Progress")

                    bar = ttk.Progressbar(root, length=250, maximum=5, value=3)
                    bar.pack(pady=20)

                    value_label = ttk.Label(root, text="3 of 5")
                    value_label.pack()

                    ttk.Button(root, text="Next", command=next_step).pack(pady=10)

                    root.mainloop()

            .. tab-item:: Q3

                .. code-block:: python

                    import tkinter as tk
                    from tkinter import ttk

                    root = tk.Tk()
                    root.geometry("300x200")
                    root.title("Busy")

                    busy_bar = ttk.Progressbar(root, length=250, mode="indeterminate")
                    busy_bar.pack(pady=20)

                    ttk.Button(root, text="Start", command=lambda: busy_bar.start(10)).pack(pady=2)
                    ttk.Button(root, text="Stop", command=busy_bar.stop).pack()

                    root.mainloop()

            .. tab-item:: Q4

                .. code-block:: python

                    import tkinter as tk
                    from tkinter import ttk


                    def fill():
                        if bar["value"] < 100:
                            bar["value"] = bar["value"] + 5
                            root.after(100, fill)
                        else:
                            status_label.config(text="Ready!")


                    root = tk.Tk()
                    root.geometry("300x200")
                    root.title("Loading")

                    bar = ttk.Progressbar(root, length=250)
                    bar.pack(pady=30)

                    status_label = ttk.Label(root, text="Loading...", font=("Arial", 16))
                    status_label.pack()

                    fill()

                    root.mainloop()
