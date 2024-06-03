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

----

Option details
--------------------

Certainly! Let's explore the various options for a **Tkinter Entry widget** and what they do:

1. **`background (bg)`**: Specifies the normal background color displayed behind the label and indicator of the entry widget¹.
2. **`borderwidth (bd)`**: Determines the size of the border around the indicator. The default value is 2 pixels¹.
3. **`cursor`**: Sets the cursor type when hovering over the entry widget.
4. **`exportselection`**: Controls whether the selected text in the entry widget is automatically exported to the clipboard.
5. **`foreground (fg)`**: Defines the color used to render the text inside the entry widget.
6. **`font`**: Specifies the font used for displaying the text.
7. **`highlightbackground`**: Sets the color of the focus highlight when the entry widget is not focused.
8. **`highlightcolor`**: Determines the color of the focus highlight when the entry widget is focused.
9. **`highlightthickness`**: Specifies the thickness of the focus highlight border.
10. **`insertbackground`**: Sets the color of the insertion cursor (the blinking vertical line indicating the insertion point).
11. **`insertborderwidth`**: Determines the size of the border around the insertion cursor.
12. **`insertofftime`**: Specifies the time (in milliseconds) the insertion cursor remains off during blinking.
13. **`insertontime`**: Specifies the time (in milliseconds) the insertion cursor remains on during blinking.
14. **`insertwidth`**: Sets the width of the insertion cursor.
15. **`invalidcommand (invcmd)`**: Associates a callback function to be called when the user enters invalid data.
16. **`justify`**: Controls how the text is justified if it contains multiple lines (options: CENTER, LEFT, or RIGHT).
17. **`relief`**: Determines the border style (e.g., FLAT, SUNKEN, RAISED, etc.).
18. **`selectbackground`**: Sets the background color of the selected text.
19. **`selectborderwidth`**: Determines the size of the border around the selected text.
20. **`selectforeground`**: Defines the color of the selected text.
21. **`show`**: Normally, the characters that the user types appear in the entry. To create a password entry that echoes each character as an asterisk, set `show="*"`¹.
22. **`state`**: Controls whether the entry widget is editable or read-only (options: NORMAL, DISABLED, or READONLY).
23. **`takefocus`**: Determines whether the entry widget can receive focus.
24. **`textvariable`**: Associates a `StringVar` instance to retrieve the current text from the entry widget.
25. **`validate`**: Specifies when validation should occur (options: NONE, FOCUSIN, FOCUSOUT, or KEY).
26. **`validatecommand (vcmd)`**: Associates a callback function to validate the input data.
27. **`width`**: Sets the width of the entry widget in characters.
28. **`xscrollcommand`**: Associates a horizontal scrollbar with the entry widget.


