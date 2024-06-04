====================================================
tk geometry pack
====================================================

| The pack geometry manager allows you to arrange widgets within a window.
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

.. py:function:: widget.pack(side=side)

    | The `side` option determines the position of the widget within its parent container.
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

- The `expand` option allows a widget to expand if the user resizes the frame.
- Example: To make a widget expand when the frame is resized:
  
.. code-block:: python

    import tkinter as tk

    window = tk.Tk()
    window.geometry('200x150')

    label = tk.Label(window, text="Expanding Label", bg="lightblue")
    label.pack(expand=True)
    # label.pack(expand=True, fill='y')
    # label.pack(expand=True, fill='x')
    # label.pack(expand=True, fill='both')

    window.mainloop()


**Fill**
~~~~~~~~~~~~~~~

- The `fill` option specifies how the widget should fill the available space. It can take values like `None`, `x`, `y`, or `both`.
- Example: To create two labels with different fill options:

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

 - These options control the internal padding (in pixels) along the x and y axes, respectively.
 - Example: The labels in the example demonstrate the use of `ipadx` and `ipady`.

**padx** and **pady**
~~~~~~~~~~~~~~~~~~~~~~~

 - These options provide external padding (in pixels) along the x and y axes, respectively.
 - Example: You can add external padding to widgets using `padx` and `pady`.


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

 - The `anchor` option specifies the position of the widget within its allocated space. It can take values like `'nw'` (top-left), `'center'`, or `'se'` (bottom-right).
 - Example: To create labels anchored at different positions:

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
