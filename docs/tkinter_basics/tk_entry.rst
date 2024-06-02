====================================================
tk entry
====================================================

| See: https://www.geeksforgeeks.org/python-tkinter-entry-widget/?ref=lbp
| See: https://www.youtube.com/watch?v=8VoTtF-CxrM&list=PLs3IFJPw3G9KL3huzPS7g-0PCbS7Auc7I&index=3


----

Usage
---------------

| The `tkinter.Entry` widget provides a button.
| To create an entry widget the general syntax is:

.. py:function:: entry_widget  = tk.Entry(parent, option=value)

    | parent is the window or frame object. 
    | Options can be passed as parameters separated by commas.


STANDARD OPTIONS
~~~~~~~~~~~~~~~~~~~~~~~~~~~

    background, bd, bg, borderwidth, cursor,
    exportselection, fg, font, foreground, highlightbackground,
    highlightcolor, highlightthickness, insertbackground,
    insertborderwidth, insertofftime, insertontime, insertwidth,
    invalidcommand, invcmd, justify, relief, selectbackground,
    selectborderwidth, selectforeground, show, state, takefocus,
    textvariable, validate, validatecommand, vcmd, width,
    xscrollcommand.

----

Code example
---------------

.. code-block:: python

    import tkinter as tk

    # Create the main window
    window = tk.Tk()
    window.geometry("400x250")  # Set window size
    window.title("Welcome to My App")  # Set window title

    # Create a StringVar to associate with the entry
    name_var = tk.StringVar()

    # Create the label widget with all options
    # creating a entry for input
    # name using widget Entry
    name_entry = tk.Entry(window, textvariable = name_var, font=('calibre',10,'normal'))

    # Pack the label into the window
    label.pack(pady=20)  # Add some padding to the top


    # Run the main event loop
    window.mainloop()



