====================================================
tk geometry pack
====================================================

| The pack geometry manager allows you to arrange widgets within a window.
| See: https://www.pythontutorial.net/tkinter/tkinter-pack/
| See: https://www.geeksforgeeks.org/python-pack-method-in-tkinter/?ref=lbp

| Layouts: https://www.youtube.com/watch?v=i577cFu8eBI&list=PLpMixYKO4EXflJFPhTvZOVAbs7lBdEBSa
| Pack: see https://www.youtube.com/watch?v=rbW1iJO1psk
| Pack with frames: https://www.youtube.com/watch?v=SsjEAWT-SMc

----

pack
--------------------

| Pack is responsive to window size changes.
| By default, the pack geometry manager places widgets in one direction vertically from top to bottom.

.. py:function:: widget.pack()

    | Use **pack()** method to pack a widget in one direction vertically from top to bottom.
    | e.g. widget.pack()

----

Options for the `pack()` geometry manager
-----------------------------------------------

**Side**
~~~~~~~~~~~

.. py:function:: widget.pack(side=side_string)

    | The `side_string` option determines the position of the widget within its parent container.
    | It can take values like `left`, `right`, `top`, or `bottom`.
    | e.g. widget.pack(side="left")

| Example: To create four buttons positioned on different sides of a frame:

.. code-block:: python

    import tkinter as tk

    window = tk.Tk()
    window.geometry('250x150')

    button1 = tk.Button(text="Left")
    button1.pack(side="left")

    button2 = tk.Button(text="Top")
    button2.pack(side="top")

    button3 = tk.Button(text="Right")
    button3.pack(side="right")

    button4 = tk.Button(text="Bottom")
    button4.pack(side="bottom")

    window.mainloop()


**Expand**
~~~~~~~~~~~~~~~~

.. py:function:: widget.pack(expand=boolean)

    | The `boolean` value is `True` or `False`.
    | e.g. `widget.pack(expand=True)` to make a widget expand when the frame is resized
    | The `expand` option allows a widget to expand if the user resizes the frame.
  
.. code-block:: python

    import tkinter as tk

    window = tk.Tk()
    window.geometry('200x150')

    label = tk.Label(window, text="Expanding Label", bg="lightblue")
    label.pack(expand=True)
    window.mainloop()


**Fill**
~~~~~~~~~~~~~~~

.. py:function:: widget.pack(fill=fill_string)

    | The `fill_string` value is `None`, `x`, `y`, or `both`.
    | The `fill` option specifies how the widget should fill the available space. 

Example: To create two labels with different fill options:

.. code-block:: python

    import tkinter as tk

    window = tk.Tk()
    window.geometry('200x150')

    label = tk.Label(window, text="Expanding Label", bg="lightblue")
    # label.pack(expand=True)
    label.pack(expand=True, fill='y')
    # label.pack(expand=True, fill='x')
    # label.pack(expand=True, fill='both')

    window.mainloop()

~~~~~~~~~~~~~
padding
~~~~~~~~~~~~~

**ipadx** and **ipady**
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:function:: widget.pack(ipadx=x, ipady=y)

    | The `ipadx` value is an integer, x. The `ipady` value is an integer, y.
    | These options control the internal padding (in pixels) along the x and y axes, respectively.
    | Example: widget.pack(ipadx=10) has internal padding of 10 in the x direction on each side of the widget.

**padx** and **pady**
~~~~~~~~~~~~~~~~~~~~~~~

.. py:function:: widget.pack(padx=x, pady=y)

    | The `padx` value is an integer, x. The `pady` value is an integer, y.
    | These options control the external padding (in pixels) along the x and y axes, respectively.
    | Example: widget.pack(padx=10) has external padding of 10 in the x direction on each side of the widget.


.. code-block:: python

    import tkinter as tk

    window = tk.Tk()

    label1 = tk.Label(window, text="Red", bg="red", fg="white")
    label1.pack(ipadx=30, ipady=6)

    label2 = tk.Label(window, text="Purple", bg="purple", fg="white")
    label2.pack(pady=20, ipadx=8, ipady=12)

    window.mainloop()



**Anchor**
~~~~~~~~~~~~~~~~~~

.. py:function:: widget.pack(anchor=anchor_string)

    | `anchor_string` can take values "n", "s", "e", "w", "ne", "nw", "se", "sw", "center".
    | eg. `'nw'` (top-left), `'center'`, or `'se'` (bottom-right)
    | The `anchor` option specifies the position of the widget within its allocated space. 
    | Example: widget.pack(ipadx=10) has internal padding of 10 in the x direction on each side of the widget.

Example: To create labels anchored at different positions:

.. code-block:: python

    import tkinter as tk


    window = tk.Tk()
    window.geometry('200x150')

    label1 = tk.Label(window, text="Top-Left", bg="lightblue")
    label1.pack(anchor='nw')

    label2 = tk.Label(window, text="Center", bg="lightgreen")
    label2.pack(anchor='center')

    label3 = tk.Label(window, text="Bottom-Right", bg="lightpink")
    label3.pack(anchor='se')

    window.mainloop()
