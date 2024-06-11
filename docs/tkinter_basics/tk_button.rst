====================================================
tk button
====================================================

| See: https://www.geeksforgeeks.org/python-creating-a-button-in-tkinter/?ref=lbp
| See: https://www.youtube.com/watch?v=8VoTtF-CxrM
| See: https://www.youtube.com/watch?v=mPQdJDVtev0

----

Usage
---------------

| The `tkinter.Button` widget provides a button.
| To create a button widget the general syntax is:

.. py:function:: button_widget = tk.Button(parent, option=value)

    | parent is the window or frame object. 
    | Options can be passed as parameters separated by commas.


STANDARD OPTIONS
~~~~~~~~~~~~~~~~~~~~~~~~~~~

    activebackground, activeforeground, anchor,
    background, bitmap, borderwidth, cursor,
    disabledforeground, font, foreground
    highlightbackground, highlightcolor,
    highlightthickness, image, justify,
    padx, pady, relief, repeatdelay,
    repeatinterval, takefocus, text,
    textvariable, underline, wraplength

WIDGET-SPECIFIC OPTIONS
~~~~~~~~~~~~~~~~~~~~~~~~~~~

    command, compound, default, height,
    overrelief, state, width


----

Code example
---------------

.. code-block:: python

    import tkinter as tk

    def button_clicked():
        print("Button clicked!")

    window = tk.Tk()

    # Creating a button with specified options
    button = tk.Button(window, 
                    text="Click Me", 
                    command=button_clicked,
                    activebackground="blue", 
                    activeforeground="white",
                    anchor="center",
                    bd=3,
                    bg="lightgray",
                    cursor="hand2",
                    disabledforeground="gray",
                    fg="black",
                    font=("Arial", 12),
                    height=2,
                    highlightbackground="black",
                    highlightcolor="green",
                    highlightthickness=2,
                    justify="center",
                    overrelief="raised",
                    padx=10,
                    pady=5,
                    width=15,
                    wraplength=100)

    button.pack(padx=20, pady=20)

    window.mainloop()
