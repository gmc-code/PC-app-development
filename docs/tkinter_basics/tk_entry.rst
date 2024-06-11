====================================================
tk entry
====================================================

| See: https://www.geeksforgeeks.org/python-tkinter-entry-widget/?ref=lbp
| See: https://www.youtube.com/watch?v=8VoTtF-CxrM

----

Usage
---------------

| The `tkinter.Entry` widget provides a input field.
| To create an entry widget the general syntax is:

.. py:function:: entry_widget  = tk.Entry(parent, option=value)

    | parent is the window or frame object. 
    | Options can be passed as parameters separated by commas.


----

Code example
---------------

.. code-block:: python

    import tkinter as tk

    # Create the main window
    window = tk.Tk()
    window.geometry("400x250")  # Set window size
    window.title("Entry")  # Set window title

    # Create a StringVar to associate with the entry
    name_var = tk.StringVar()

    # Create the label widget with all options
    # creating a entry for input
    # name using widget Entry
    name_entry = tk.Entry(window, textvariable = name_var, font=('calibre',24,'normal'))

    # Pack the label into the window
    label.pack(pady=20)  # Add some padding to the top


    # Run the main event loop
    window.mainloop()

----

Option details
--------------------

| Options for a **Tkinter Entry widget** and what they do:

1. ``background`` (or ``bg``): Sets the normal background color displayed behind the text in the entry widget.
2. ``bd`` (or ``borderwidth``): Specifies the size of the border around the entry widget (default is 2 pixels).
3. ``cursor``: Determines the mouse cursor appearance when hovering over the entry widget.
4. ``disabledbackground``: Sets the background color when the entry widget is disabled.
5. ``disabledforeground``: Sets the text color when the entry widget is disabled.
6. ``exportselection``: Controls whether the selected text in the entry widget is automatically copied to the clipboard.
7. ``fg`` (or ``foreground``): Sets the text color.
8. ``font``: Specifies the font style for the text in the entry widget.
9. ``highlightbackground``: Color of the focus highlight when the entry widget is not focused.
10. ``highlightcolor``: Color of the focus highlight when the entry widget is focused.
11. ``highlightthickness``: Thickness of the focus highlight.
12. ``insertbackground``: Color of the insertion cursor (caret) when editing the entry widget.
13. ``insertborderwidth``: Border width around the insertion cursor.
14. ``insertofftime``: Specifies the time (in milliseconds) the insertion cursor remains off during blinking.
15. ``insertontime``: Specifies the time (in milliseconds) the insertion cursor remains on during blinking.
16. ``insertwidth``: Width of the insertion cursor.
17. ``invalidcommand``: Specifies a callback function to be called when the user enters invalid data.
18. ``invcmd``: An alias for `invalidcommand`.
19. ``justify``: Controls text alignment within the entry widget (e.g., `tk.LEFT`, `tk.CENTER`, `tk.RIGHT`).
20. ``readonlybackground``: Background color when the entry widget is read-only.
21. ``relief``: Specifies the border style (e.g., flat, raised, sunken).
22. ``selectbackground``: Background color of the selected text.
23. ``selectborderwidth``: Border width around the selected text.
24. ``selectforeground``: Text color of the selected text.
25. ``show``: Used for password entry; hides the actual characters and displays a specified character (e.g., asterisks).
26. ``state``: Determines whether the entry widget is active, disabled, or read-only (options: NORMAL, DISABLED, or READONLY).
27. ``takefocus``: Specifies whether the entry widget can receive focus during keyboard navigation.
28. ``textvariable``: Associates a `StringVar` instance to retrieve the current text from the entry widget.
29. ``validate``: Specifies when validation should occur (options: NONE, FOCUSIN, FOCUSOUT, or KEY).
30. ``validatecommand``: Associates a callback function to validate the input data.
31. ``vcmd``: An alias for `validatecommand`.
32. ``width``: Sets the width (number of characters) of the entry widget.
33. ``xscrollcommand``: Associates a horizontal scrollbar with the entry widget.

