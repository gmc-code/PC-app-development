====================================================
ttk geometry pack
====================================================

| The pack geometry manager allows you to arrange widgets within a root.
| See: `<https://www.pythontutorial.net/tkinter/tkinter-pack/>`_
| See: `<https://www.geeksforgeeks.org/python-pack-method-in-tkinter/?ref=lbp>`_

| Layouts: `<https://www.youtube.com/watch?v=i577cFu8eBI&list=PLpMixYKO4EXflJFPhTvZOVAbs7lBdEBSa>`_
| Pack: see `<https://www.youtube.com/watch?v=rbW1iJO1psk>`_
| Pack with frames: `<https://www.youtube.com/watch?v=SsjEAWT-SMc>`_

----

pack
--------------------

| Pack is responsive to window size changes.
| By default, the pack geometry manager places widgets vertically from top to bottom.

.. py:function:: widget.pack()

    | Use **pack()** to pack widgets vertically from top to bottom.
    | e.g. widget.pack()

----

Options for the `pack()` geometry manager
-----------------------------------------------

**padding**
~~~~~~~~~~~~~

.. py:function:: widget.pack(ipadx=x, ipady=y)

    | The `ipadx` value is an integer, x. The `ipady` value is an integer, y.
    | These options control the **internal** padding (in pixels) along the x and y axes.
    | Example: widget.pack(ipadx=10) adds 10px internal padding on each side.


.. py:function:: widget.pack(padx=x, pady=y)

    | The `padx` value is an integer, x. The `pady` value is an integer, y.
    | These options control the **external** padding (in pixels) along the x and y axes.
    | Example: widget.pack(padx=10) adds 10px external padding on each side.


.. image:: images/pack_padding.png
    :scale: 100%

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk

    root = tk.Tk()

    label1 = ttk.Label(root, text="Red")
    label1.pack(ipadx=30, ipady=6)

    label2 = ttk.Label(root, text="Purple")
    label2.pack(pady=20, ipadx=8, ipady=12)

    root.mainloop()


**Anchor**
~~~~~~~~~~~~~~~~~~

.. py:function:: widget.pack(anchor=anchor_string)

    | `anchor_string` can take values "n", "s", "e", "w", "ne", "nw", "se", "sw", "center".
    | e.g. `'nw'` (top-left), `'center'`, or `'se'` (bottom-right)
    | The `anchor` option specifies the position of the widget within its allocated space.
    | Example: widget.pack(anchor='nw') positions the widget at the top-left corner.

Example: Labels anchored at different positions:

.. image:: images/pack_anchor.png
    :scale: 100%

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk

    root = tk.Tk()
    root.title("pack anchor")
    root.geometry('250x150')

    label1 = ttk.Label(root, text="Top-Left")
    label1.pack(anchor='nw')

    label2 = ttk.Label(root, text="Center")
    label2.pack(anchor='center')

    label3 = ttk.Label(root, text="Bottom-Right")
    label3.pack(anchor='se')

    root.mainloop()


**Side**
~~~~~~~~~~~

.. py:function:: widget.pack(side=side_string)

    | The `side_string` option determines the position of the widget within its parent container.
    | Valid values: `left`, `right`, `top`, `bottom`.
    | e.g. widget.pack(side="left")

Example: Buttons positioned on different sides of a frame:

.. image:: images/pack_side.png
    :scale: 100%

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk

    root = tk.Tk()
    root.title("pack side")
    root.geometry("250x150")

    button1 = ttk.Button(text="Left")
    button1.pack(side="left")

    button2 = ttk.Button(text="Top")
    button2.pack(side="top")

    button3 = ttk.Button(text="Right")
    button3.pack(side="right")

    button4 = ttk.Button(text="Bottom")
    button4.pack(side="bottom")

    root.mainloop()


**Expand**
~~~~~~~~~~~~~~~~

.. py:function:: widget.pack(expand=boolean)

    | The `boolean` value is `True` or `False`.
    | e.g. `widget.pack(expand=True)` to allow a widget to expand when the window is resized.
    | The `expand` option allocates extra space to the widget.


**Fill**
~~~~~~~~~~~~~~~

.. py:function:: widget.pack(fill=fill_string)

    | The `fill_string` value is `None`, `x`, `y`, or `both`.
    | The `fill` option specifies how the widget should fill the available space.

Example: Use `expand=True` so fill options are visible.

.. image:: images/pack_fill_x.png
    :scale: 100%

.. image:: images/pack_fill_y.png
    :scale: 100%

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk

    root = tk.Tk()
    root.title("pack fill x")
    root.geometry("250x150")

    label = ttk.Label(root, text="Expanding Label")
    label.pack(expand=True, fill='x')

    root.mainloop()
