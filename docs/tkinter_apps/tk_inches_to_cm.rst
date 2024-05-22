====================================================
tk inches to cm
====================================================

.. image:: images/tk_inches_to_cm_converter.png
    :scale: 67%
    
    
| This code converts inches to cm.   
| This code creates a simple GUI application using the Tkinter library. 
| It displays a window with Label, Entry, Text and Button widgets

----

convert_inches_to_cm
---------------

| ``convert_inches_to_cm()`` uses a try and except block to catch errors due to non numeric entries.
| See: https://www.w3schools.com/python/python_try_except.asp
| The delete method of a Text widget requires the line.column as the first argument. e.g. ``1.0`` in ``c_text.delete(1.0, 'end')``
| ``tk.END`` or ``'end'`` can be used as the second argument to cause the deletion to go to the end of the widget.
| The insert method of a Text widget requires the line.column as the first argument. e.g. ``1.0`` in ``cm_text.insert(1.0, f'{cm:.2f}')``
| ``cm_text.insert(1.0, f'{cm:.2f}')`` uses ``:.2f`` to format the celsius float to 2 decimal places.
| For string formatting see: https://www.w3schools.com/python/ref_string_format.asp

----

Full code
------------

.. code-block:: python

    import tkinter as tk

    # Constants
    BG_COLOR = "#333333"
    FG_COLOR = "#FFFFFF"
    BUTTON_COLOR = "#FF3399"
    FONT_STYLE = ("Arial", 16)


    def convert_inches_to_cm():
        """
        Converts inches to cm and displays the result in the GUI.

        Reads the inches value from the input field, performs the conversion to cm,
        and updates the result in the output text widget.

        Raises:
            ValueError: If the input is not a valid float.
        """
        try:
            inches = float(inches_entry.get())
            cm = inches * 2.54
            cm_text.delete(1.0, "end")  # Clear any previous result
            cm_text.insert(1.0, f"{cm:.2f}")
        except ValueError:
            cm_text.delete(1.0, "end")
            cm_text.insert(1.0, "Invalid input.")


    # Create the main window
    window = tk.Tk()
    window.title("Inches to cm Converter")
    window.geometry("300x200")
    window.configure(bg=BG_COLOR)

    # Create widgets
    inches_label = tk.Label(window, text="inches", bg=BG_COLOR, fg=FG_COLOR, font=FONT_STYLE)
    inches_entry = tk.Entry(window, width=10, font=FONT_STYLE)
    cm_label = tk.Label(window, text="cm", bg=BG_COLOR, fg=FG_COLOR, font=FONT_STYLE)
    # height of 1 is one text row
    cm_text = tk.Text(window, height=1, width=10, font=FONT_STYLE)
    convert_button = tk.Button(window, text="Convert", width=20, bg=BUTTON_COLOR, fg=FG_COLOR, font=FONT_STYLE, command=convert_inches_to_cm)

    # Place widgets in the window
    inches_label.grid(row=0, column=0, sticky="e", padx=10, pady=10)
    inches_entry.grid(row=0, column=1, sticky="w", padx=10, pady=10)
    cm_label.grid(row=2, column=0, sticky="e", padx=10, pady=10)
    cm_text.grid(row=2, column=1, sticky="w", padx=10, pady=10)
    convert_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

    # Start the main event loop
    window.mainloop()
