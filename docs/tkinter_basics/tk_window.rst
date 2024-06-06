====================================================
tk window
====================================================

See: https://tkdocs.com/tutorial/windows.html
See: https://tcl.tk/man/tcl8.6/TkCmd/wm.htm
See: https://www.pythontutorial.net/tkinter/tkinter-window/

----

Simple window
-----------------

.. py:function:: tkinter.Tk()

    | Create the main application window.
    | Common usage is **window = tk.Tk()**.

.. py:function:: window.mainloop()

    | Runs an infinite loop that continuously processes events (such as button clicks, keypresses, and mouse movements) and updates the GUI accordingly.
    | While the main loop is active, any code after the mainloop() call will not execute until the window is closed.
    | Essentially, it keeps the GUI alive and responsive.

| Below is the code to create a simple empty window. 

.. code-block:: python

    import tkinter as tk

    # Create the main application window
    window = tk.Tk()

    # Start the main event loop
    window.mainloop()

----

Window title
-----------------

.. py:function:: title('window_title')

    | The method window.title() sets the title of the window.
    | The argument 'window_title' specifies the text that will appear in the title bar of the window.


.. code-block:: python

    import tkinter as tk


    # Create the main application window
    window = tk.Tk()
    # set the window title
    window.title('Tkinter Window title')

    # Start the main event loop
    window.mainloop()

----

Window size and position
-----------------------------

.. py:function:: geometry(widthxheight)

    | set the size and top left of a window
    | width: The desired width of the window in pixels.
    | height: The desired height of the window in pixels.

.. py:function:: attributes('-topmost', True)

    | Use the window.attributes('-topmost', True) to make the window always stay on top.

.. py:function:: resizable(width_boolean,height_boolean)

    | Determines whether the window can be resized by the user.
    | To create a fixed-size window, disable resizing by calling `window.resizable(False, False)`
    | The default, `window.resizable(True, True)`, makes the window both horizontally and vertically resizable.

| The code below sets the window size and position, sets the window to stay on top of others and prevents resizing.

.. code-block:: python

    import tkinter as tk


    window = tk.Tk()
    window.title('Tkinter Window - size and position')
    window_width = 400
    window_height = 300
    left_x = 200
    top_y = 50
    # set the size and position of the window
    window.geometry(f'{window_width}x{window_height}+{left_x}+{top_y}')
    # set window to stay topmost
    window.attributes('-topmost', True)
    # set window size to be static or un resizable
    window.resizable(False, False)

    window.mainloop()

----

Window centered
-----------------------

.. py:function:: window.winfo_screenwidth()

    | returns the width of the screen (or monitor) where the specified widget (usually a Tkinter window) is located.

.. py:function:: window.winfo_screenheight()

    | returns the height of the screen (or monitor) where the specified widget (usually a Tkinter window) is located.


.. py:function:: geometry(widthxheight±x±y)

    | set the size and top left of a window
    | width: The desired width of the window in pixels.
    | height: The desired height of the window in pixels.
    | x: The horizontal position (+ for distance from the left edge of the screen; - from right) in pixels.
    | y: The vertical position (+ for distance from the top edge of the screen; - from bottom) in pixels.


.. code-block:: python

    import tkinter as tk


    window = tk.Tk()
    window.title('Tkinter Window - Center')

    window_width = 600
    window_height = 400

    # get the screen dimension
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
                
    # find the center point
    center_x = int(screen_width/2 - window_width/2)
    center_y = int(screen_height/2 - window_height/2)

    # set the position of the window to the center of the screen, using top left position
    window.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

    window.mainloop()

----

Window width and height
--------------------------

.. py:function:: window.winfo_width()

    | returns the width of the Tkinter window.

.. py:function:: window.winfo_height()

    | returns the height of the Tkinter window.

.. py:function:: update_idletasks()

    | The `update_idletasks()` method is used to process pending idle tasks in a Tkinter window without handling other events.
    | `update_idletasks()` focuses solely on idle tasks which typically involve geometry management and widget redrawing.
    | It's particularly useful when you want to refresh the window's appearance without triggering additional event processing.


| The code below has definitions to set the width or height of the window.

.. code-block:: python

   import tkinter as tk


    def window_set_height(window, height):
        # Wait for the window to be fully initialized
        window.update_idletasks()
        window.geometry(f"{window.winfo_width()}x{height}")


    def window_set_width(window, width):
        # Wait for the window to be fully initialized
        window.update_idletasks()
        window.geometry(f"{width}x{window.winfo_height()}")


    window = tk.Tk()
    window.title("Tkinter Window - set width or height")

    # set the top left position to 250,50
    window.geometry(f"+{250}+{50}")
    window_set_width(window, 1000)
    window_set_height(window, 250)

    window.mainloop()

----

Min Max window size
--------------------------

.. py:function:: window.minsize(width, height)

    | Set the minimum size `(width, height)`.

.. py:function:: window.maxsize()

    | Set the maximum size `(width, height)`.


| The code below sets the minimum and maximum size of the window.

.. code-block:: python

    import tkinter as tk

    # Create the main application window
    window = tk.Tk()
    window.title("Resizable Window - Min Max Example")

    # Set the minimum size (width, height)
    window.minsize(200, 100)
    # Set the maximum size (width, height)
    window.maxsize(500, 500)

    # Start the main event loop
    window.mainloop()


----

Background color
--------------------

| Online color picker see: https://www.w3schools.com/colors/colors_picker.asp
| See: https://pickcoloronline.com/
| See: https://htmlcolorcodes.com/color-chart/
| See: https://www.w3schools.com/colors/colors_names.asp

.. py:function:: window.configure(bg=color)

    | Sets the background color of the window. 
    | `color` is a color name (e.g. "white"), hexadecimal value (e.g. "#FFFFFF").


| The code below sets the window background color to a light yellow color.

.. code-block:: python

    import tkinter as tk

    # Create the main application window
    window = tk.Tk()
    window.title("Light Yellow Background")

    # Set the background color to light yellow
    window.configure(bg="light yellow")

    # Start the main event loop
    window.mainloop()

