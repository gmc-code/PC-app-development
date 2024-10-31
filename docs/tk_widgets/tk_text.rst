====================================================
tk text
====================================================

| See: https://www.geeksforgeeks.org/python-tkinter-text-widget/

----

Usage
---------------

| The `tkinter.Text` widget provides a versatile multi-line text area that you can use for various purposes.
| To create a multi-line text widget the general syntax is:

.. py:function:: text_widget  = tk.Text(parent, option=value)

    | parent is the window or frame object.
    | Options can be passed as parameters separated by commas.

----

Text widget with Scrollbar
--------------------------------

.. image:: images/text.png
        :scale: 100%

.. code-block:: python

    import tkinter as tk
    from tkinter import scrolledtext

    # Create the main window
    root = tk.Tk()
    root.title("Text Widget Example")

    # Create a Text widget with a scrollbar
    text_frame = tk.Frame(root)
    text_frame.pack(padx=10, pady=10, fill="both", expand=True)

    scrollbar = tk.Scrollbar(text_frame)
    scrollbar.pack(side="right", fill="y")

    text = tk.Text(text_frame, height=10, width=40, wrap="word", font=("Helvetica", 12), yscrollcommand=scrollbar.set)
    text.pack(padx=10, pady=10, fill="both", expand=True)

    scrollbar.config(command=text.yview)

    # Insert initial content
    initial_content = "\n".join([f"Line {i+1}" for i in range(15)])
    text.insert("1.0", initial_content)

    # Customize options
    text.config(
        bg="lightyellow",  # Background color
        fg="blue",  # Text color
        bd=2,  # Border width
        relief="solid",  # Border style
        insertbackground="blue",  # Insertion cursor color
        state="normal",  # Enable editing (use "disabled" to disable)
        highlightthickness=5,
        highlightcolor="red",
        padx=10,
        pady=10
    )

    # Run the main event loop
    root.mainloop()

----

Parameter syntax
----------------------

 .. py:function:: text_widget = tk.Text(parent, option=value)

    | parent is the window or frame object.
    | Options can be passed as parameters separated by commas.

    **Parameters:**

    .. py:attribute:: autoseparators

        | Syntax: ``text_widget = tk.Text(parent, autoseparators=1)``
        | Description: Enables automatic separator insertion when typing.
        | Default: 1
        | Example: ``text_widget = tk.Text(window, autoseparators=1)``

    .. py:attribute:: background

        | Syntax: ``text_widget = tk.Text(parent, background="color")``
        | Description: Sets the background color of the text widget.
        | Default: SystemWindow
        | Example: ``text_widget = tk.Text(window, background="lightyellow")``

    .. py:attribute:: bd

        | Syntax: ``text_widget = tk.Text(parent, bd=border_width)``
        | Description: Sets the border width of the text widget.
        | Default: 1
        | Example: ``text_widget = tk.Text(window, bd=2)``

    .. py:attribute:: bg

        | Syntax: ``text_widget = tk.Text(parent, bg="color")``
        | Description: Sets the background color of the text widget.
        | Default: SystemWindow
        | Example: ``text_widget = tk.Text(window, bg="lightyellow")``

    .. py:attribute:: blockcursor

        | Syntax: ``text_widget = tk.Text(parent, blockcursor=0)``
        | Description: Sets the cursor style; a block or normal cursor.
        | Default: 0
        | Example: ``text_widget = tk.Text(window, blockcursor=1)``

    .. py:attribute:: borderwidth

        | Syntax: ``text_widget = tk.Text(parent, borderwidth=width)``
        | Description: Sets the width of the border around the text widget.
        | Default: 1
        | Example: ``text_widget = tk.Text(window, borderwidth=2)``

    .. py:attribute:: cursor

        | Syntax: ``text_widget = tk.Text(parent, cursor="cursor_type")``
        | Description: Sets the mouse cursor when hovering over the text widget.
        | Default: xterm
        | Example: ``text_widget = tk.Text(window, cursor="hand2")``

    .. py:attribute:: endline

        | Syntax: ``text_widget = tk.Text(parent, endline="")``
        | Description: Sets the endline character for new lines.
        | Default: None
        | Example: ``text_widget = tk.Text(window, endline="\n")``

    .. py:attribute:: exportselection

        | Syntax: ``text_widget = tk.Text(parent, exportselection=1)``
        | Description: Allows the text selection to be copied to the clipboard.
        | Default: 1
        | Example: ``text_widget = tk.Text(window, exportselection=1)``

    .. py:attribute:: fg

        | Syntax: ``text_widget = tk.Text(parent, fg="color")``
        | Description: Sets the foreground color (text color) of the text widget.
        | Default: SystemWindowText
        | Example: ``text_widget = tk.Text(window, fg="black")``

    .. py:attribute:: font

        | Syntax: ``text_widget = tk.Text(parent, font=("font_name", size, "style"))``
        | Description: Specifies the font type, size, and style for the text.
        | Default: TkFixedFont
        | Example: ``text_widget = tk.Text(window, font=("Arial", 12, "italic"))``

    .. py:attribute:: foreground

        | Syntax: ``text_widget = tk.Text(parent, foreground="color")``
        | Description: Sets the foreground color (text color) of the text widget.
        | Default: SystemWindowText
        | Example: ``text_widget = tk.Text(window, foreground="black")``

    .. py:attribute:: height

        | Syntax: ``text_widget = tk.Text(parent, height=height_value)``
        | Description: Sets the height of the text widget in lines.
        | Default: 24
        | Example: ``text_widget = tk.Text(window, height=10)``

    .. py:attribute:: highlightbackground

        | Syntax: ``text_widget = tk.Text(parent, highlightbackground="color")``
        | Description: Sets the background color when the text widget does not have focus.
        | Default: SystemButtonFace
        | Example: ``text_widget = tk.Text(window, highlightbackground="gray")``

    .. py:attribute:: highlightcolor

        | Syntax: ``text_widget = tk.Text(parent, highlightcolor="color")``
        | Description: Sets the color of the highlight when the text widget has focus.
        | Default: SystemWindowFrame
        | Example: ``text_widget = tk.Text(window, highlightcolor="blue")``

    .. py:attribute:: highlightthickness

        | Syntax: ``text_widget = tk.Text(parent, highlightthickness=thickness)``
        | Description: Sets the thickness of the highlight border.
        | Default: 0
        | Example: ``text_widget = tk.Text(window, highlightthickness=2)``

    .. py:attribute:: inactiveselectbackground

        | Syntax: ``text_widget = tk.Text(parent, inactiveselectbackground="color")``
        | Description: Sets the background color for selected text when the widget is inactive.
        | Default: None
        | Example: ``text_widget = tk.Text(window, inactiveselectbackground="lightgray")``

    .. py:attribute:: insertbackground

        | Syntax: ``text_widget = tk.Text(parent, insertbackground="color")``
        | Description: Sets the color of the insertion cursor (caret).
        | Default: SystemWindowText
        | Example: ``text_widget = tk.Text(window, insertbackground="red")``

    .. py:attribute:: insertborderwidth

        | Syntax: ``text_widget = tk.Text(parent, insertborderwidth=width)``
        | Description: Sets the width of the border around the insertion cursor.
        | Default: 0
        | Example: ``text_widget = tk.Text(window, insertborderwidth=2)``

    .. py:attribute:: insertofftime

        | Syntax: ``text_widget = tk.Text(parent, insertofftime=milliseconds)``
        | Description: Sets the time the cursor stays off (in milliseconds).
        | Default: 300
        | Example: ``text_widget = tk.Text(window, insertofftime=500)``

    .. py:attribute:: insertontime

        | Syntax: ``text_widget = tk.Text(parent, insertontime=milliseconds)``
        | Description: Sets the time the cursor stays on (in milliseconds).
        | Default: 600
        | Example: ``text_widget = tk.Text(window, insertontime=800)``

    .. py:attribute:: insertunfocussed

        | Syntax: ``text_widget = tk.Text(parent, insertunfocussed="style")``
        | Description: Sets the style of the cursor when the widget is unfocused.
        | Default: none
        | Example: ``text_widget = tk.Text(window, insertunfocussed="underline")``

    .. py:attribute:: insertwidth

        | Syntax: ``text_widget = tk.Text(parent, insertwidth=width)``
        | Description: Sets the width of the insertion cursor.
        | Default: 2
        | Example: ``text_widget = tk.Text(window, insertwidth=5)``

    .. py:attribute:: maxundo

        | Syntax: ``text_widget = tk.Text(parent, maxundo=number)``
        | Description: Sets the maximum number of undo operations.
        | Default: 0 (unlimited)
        | Example: ``text_widget = tk.Text(window, maxundo=100)``

    .. py:attribute:: padx

        | Syntax: ``text_widget = tk.Text(parent, padx=padding_value)``
        | Description: Sets the horizontal padding within the text widget.
        | Default: 1
        | Example: ``text_widget = tk.Text(window, padx=10)``

    .. py:attribute:: pady

        | Syntax: ``text_widget = tk.Text(parent, pady=padding_value)``
        | Description: Sets the vertical padding within the text widget.
        | Default: 1
        | Example: ``text_widget = tk.Text(window, pady=10)``

    .. py:attribute:: relief

        | Syntax: ``text_widget = tk.Text(parent, relief="style")``
        | Description: Sets the border style of the text widget. Options include `flat`, `raised`, `sunken`, `groove`, `ridge`.
        | Default: sunken
        | Example: ``text_widget = tk.Text(window, relief="flat")``

    .. py:attribute:: selectbackground

        | Syntax: ``text_widget = tk.Text(parent, selectbackground="color")``
        | Description: Sets the background color of the selected text.
        | Default: SystemHighlight
        | Example: ``text_widget = tk.Text(window, selectbackground="lightblue")``

    .. py:attribute:: selectborderwidth

        | Syntax: ``text_widget = tk.Text(parent, selectborderwidth=width)``
        | Description: Sets the border width of the selection.
        | Default: 0
        | Example: ``text_widget = tk.Text(window, selectborderwidth=1)``

    .. py:attribute:: selectforeground

        | Syntax: ``text_widget = tk.Text(parent, selectforeground="color")``
        | Description: Sets the text color of the selected text.
        | Default: SystemHighlightText
        | Example: ``text_widget = tk.Text(window, selectforeground="white")``

    .. py:attribute:: setgrid

        | Syntax: ``text_widget = tk.Text(parent, setgrid=0)``
        | Description: Enables or disables grid lines in the text widget.
        | Default: 0
        | Example: ``text_widget = tk.Text(window, setgrid=1)``

    .. py:attribute:: spacing1

        | Syntax: ``text_widget = tk.Text(parent, spacing1=spacing_value)``
        | Description: Sets the spacing before paragraphs.
        | Default: 0
        | Example: ``text_widget = tk.Text(window, spacing1=5)``

    .. py:attribute:: spacing2

        | Syntax: ``text_widget = tk.Text(parent, spacing2=spacing_value)``
        | Description: Sets the spacing between lines.
        | Default: 0
        | Example: ``text_widget = tk.Text(window, spacing2=3)``

    .. py:attribute:: spacing3

        | Syntax: ``text_widget = tk.Text(parent, spacing3=spacing_value)``
        | Description: Sets the spacing after paragraphs.
        | Default: 0
        | Example: ``text_widget = tk.Text(window, spacing3=5)``

    .. py:attribute:: startline

        | Syntax: ``text_widget = tk.Text(parent, startline="")``
        | Description: Sets the starting line number for text.
        | Default: None
        | Example: ``text_widget = tk.Text(window, startline=1)``

    .. py:attribute:: state

        | Syntax: ``text_widget = tk.Text(parent, state="state_type")``
        | Description: Sets the state of the text widget. Options include `normal`, `disabled`, or `hidden`.
        | Default: normal
        | Example: ``text_widget = tk.Text(window, state="disabled")``

    .. py:attribute:: tabs

        | Syntax: ``text_widget = tk.Text(parent, tabs=tab_stops)``
        | Description: Sets tab stops for the text widget.
        | Default: None
        | Example: ``text_widget = tk.Text(window, tabs=4)``

    .. py:attribute:: tabstyle

        | Syntax: ``text_widget = tk.Text(parent, tabstyle="style")``
        | Description: Specifies the style for tab stops. Options include `tabular`.
        | Default: tabular
        | Example: ``text_widget = tk.Text(window, tabstyle="tabular")``

    .. py:attribute:: takefocus

        | Syntax: ``text_widget = tk.Text(parent, takefocus=1)``
        | Description: Allows the text widget to take focus on click.
        | Default: None
        | Example: ``text_widget = tk.Text(window, takefocus=1)``

    .. py:attribute:: undo

        | Syntax: ``text_widget = tk.Text(parent, undo=0)``
        | Description: Enables the undo feature for the text widget.
        | Default: 0
        | Example: ``text_widget = tk.Text(window, undo=1)``

    .. py:attribute:: width

        | Syntax: ``text_widget = tk.Text(parent, width=width_value)``
        | Description: Sets the width of the text widget in characters.
        | Default: 80
        | Example: ``text_widget = tk.Text(window, width=50)``

    .. py:attribute:: wrap

        | Syntax: ``text_widget = tk.Text(parent, wrap="mode")``
        | Description: Sets the text wrapping mode. Options are `none`, `char`, or `word`.
        | Default: char
        | Example: ``text_widget = tk.Text(window, wrap="word")``

    .. py:attribute:: xscrollcommand

        | Syntax: ``text_widget = tk.Text(parent, xscrollcommand=command)``
        | Description: Configures the command for horizontal scrolling.
        | Default: None
        | Example: ``text_widget = tk.Text(window, xscrollcommand=my_xscroll_command)``

    .. py:attribute:: yscrollcommand

        | Syntax: ``text_widget = tk.Text(parent, yscrollcommand=command)``
        | Description: Configures the command for vertical scrolling.
        | Default: None
        | Example: ``text_widget = tk.Text(window, yscrollcommand=my_yscroll_command)``
