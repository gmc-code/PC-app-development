====================================================
tk window
====================================================

| See: https://tkdocs.com/tutorial/windows.html
| See: https://tcl.tk/man/tcl8.6/TkCmd/wm.htm
| See: https://www.pythontutorial.net/tkinter/tkinter-window/

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

.. py:function:: window.title('window_title')

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

.. image:: images/window_title.png
    :scale: 100%

----

Window size
-----------------------------

.. py:function:: window.geometry(widthxheight)

    | set the size of a tkinter window
    | width: The desired width of the window in pixels.
    | height: The desired height of the window in pixels.

| The code below sets the window size.

.. code-block:: python

    import tkinter as tk

    # Create the main window
    window = tk.Tk()
    window.title('Tkinter Window - size')
    window.geometry("600x400")

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

.. image:: images/window_bg_color.png
    :scale: 100%

----

| This will usually be all that is needed in setting up a tkinter window.
| Various more advanced features are given below for reference purposes.

----

Window size and position
-----------------------------

.. py:function:: window.geometry(widthxheight±x±y)

    | set the size and top left of a window
    | width: The desired width of the window in pixels.
    | height: The desired height of the window in pixels.
    | x: The horizontal position (+ for distance from the left edge of the screen; - from right) in pixels.
    | y: The vertical position (+ for distance from the top edge of the screen; - from bottom) in pixels.

.. py:function:: window.attributes('-topmost', True)

    | Use the window.attributes('-topmost', True) to make the window always stay on top.

.. py:function:: window.resizable(width_boolean,height_boolean)

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


.. code-block:: python

    import tkinter as tk

    window = tk.Tk()
    window.title('Tkinter Window - Centered')

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

Window options
-------------------

Here are the descriptions for each option in Tkinter's window options.

.. py:attribute:: attributes

    | Syntax: ``window.attributes("-attribute", value)``
    | Description: Configures advanced window attributes, such as making the window always on top, transparent, or fullscreen.
    | Example:
    | ``window.attributes("-topmost", True)``  (Keeps window on top)
    | ``window.attributes("-fullscreen", True)``  (Enables fullscreen mode)
    | ``window.attributes("-alpha", 0.8)``  (Sets window transparency)

.. py:attribute:: bg

    | Syntax: ``window.configure(bg="color")``
    | Description: Sets the background color of the window.
    | Default: SystemButtonFace RGB: (240, 240, 240)
    | Example: ``window.configure(bg="light yellow")``

.. py:attribute:: bd

    | Syntax: ``window.configure(bd=value)``
    | Description: Sets the border width around the window.
    | Default: 2
    | Example: ``window.configure(bd=5)``

.. py:attribute:: colormap

    | Syntax: ``window.configure(colormap="new_colormap")``
    | Description: Specifies a different colormap for the window, useful for advanced color manipulation.
    | Default: None
    | Example: ``window.configure(colormap="new_map")``

.. py:attribute:: cursor

    | Syntax: ``window.configure(cursor="cursor_type")``
    | Description: Changes the appearance of the mouse cursor when it is over the window.
    | Default: None
    | Example: ``window.configure(cursor="arrow")``

.. py:attribute:: geometry

    | Syntax: ``window.geometry("widthxheight+X+Y")``
    | Description: Sets the dimensions and position of the window on the screen.
    | Default: Automatically sized based on content.
    | Example: ``window.geometry("800x600+100+50")``

.. py:attribute:: height

    | Syntax: ``window.configure(height=value)``
    | Description: Sets the height of the window.
    | Default: Size based on content.
    | Example: ``window.configure(height=400)``

.. py:attribute:: highlightbackground

    | Syntax: ``window.configure(highlightbackground="color")``
    | Description: Sets the color of the highlight border when the window does not have focus.
    | Default: SystemButtonFace RGB: (240, 240, 240)
    | Example: ``window.configure(highlightbackground="gray")``

.. py:attribute:: highlightcolor

    | Syntax: ``window.configure(highlightcolor="color")``
    | Description: Specifies the color of the highlight border when the window has focus.
    | Default: SystemHighlight RGB: (0, 120, 215)
    | Example: ``window.configure(highlightcolor="blue")``

.. py:attribute:: highlightthickness

    | Syntax: ``window.configure(highlightthickness=value)``
    | Description: Sets the thickness of the highlight border.
    | Default: 1
    | Example: ``window.configure(highlightthickness=2)``

.. py:attribute:: iconbitmap

    | Syntax: ``window.iconbitmap("path_to_icon.ico")``
    | Description: Sets the icon for the window, usually displayed in the title bar and taskbar.
    | Default: Default Tkinter icon.
    | Example: ``window.iconbitmap("my_icon.ico")``

.. py:attribute:: maxsize

    | Syntax: ``window.maxsize(width, height)``
    | Description: Sets the maximum size of the window.
    | Default: No maximum limit.
    | Example: ``window.maxsize(1200, 800)``

.. py:attribute:: menu

    | Syntax: ``window.configure(menu=menu_widget)``
    | Description: Sets a menu widget as the menu for this window.
    | Default: None
    | Example: ``window.configure(menu=my_menu)``

.. py:attribute:: minsize

    | Syntax: ``window.minsize(width, height)``
    | Description: Sets the minimum size of the window.
    | Default: No minimum limit.
    | Example: ``window.minsize(300, 200)``

.. py:attribute:: padx

    | Syntax: ``window.configure(padx=value)``
    | Description: Adds horizontal padding inside the window.
    | Default: 0
    | Example: ``window.configure(padx=10)``

.. py:attribute:: pady

    | Syntax: ``window.configure(pady=value)``
    | Description: Adds vertical padding inside the window.
    | Default: 0
    | Example: ``window.configure(pady=10)``

.. py:attribute:: relief

    | Syntax: ``window.configure(relief="style")``
    | Description: Defines the border style of the window (e.g., flat, raised, sunken).
    | Default: flat
    | Example: ``window.configure(relief="sunken")``

.. py:attribute:: resizable

    | Syntax: ``window.resizable(width=True/False, height=True/False)``
    | Description: Controls whether the window can be resized horizontally or vertically.
    | Default: Both width and height are resizable (True, True).
    | Example: ``window.resizable(width=False, height=True)``

.. py:attribute:: state

    | Syntax: ``window.state("state")``
    | Description: Sets the window's state to either normal, icon (minimized), or zoomed (maximized).
    | Default: normal
    | Example: ``window.state("zoomed")``

.. py:attribute:: takefocus

    | Syntax: ``window.configure(takefocus=True/False)``
    | Description: Indicates whether the window can receive focus when tabbed to.
    | Default: True for most windows.
    | Example: ``window.configure(takefocus=False)``

.. py:attribute:: title

    | Syntax: ``window.title("title_text")``
    | Description: Sets the title of the window displayed in the title bar.
    | Default: Usually empty or "tk" for `Tk` root windows.
    | Example: ``window.title("My Application")``

.. py:attribute:: visual

    | Syntax: ``window.configure(visual="visual_type")``
    | Description: Specifies the visual type, typically for advanced graphics.
    | Default: None
    | Example: ``window.configure(visual="truecolor")``

.. py:attribute:: width

    | Syntax: ``window.configure(width=value)``
    | Description: Sets the width of the window.
    | Default: Size based on content.
    | Example: ``window.configure(width=500)``


----

Window attributes
-------------------

Here are the descriptions for each setting in Tkinter's window attributes.

.. py:attribute:: window.attributes

    | Syntax: ``window.attributes("-attribute", value)``
    | Description: Configures advanced window attributes, such as making the window always on top, transparent, or fullscreen.
    | Example:
    | ``window.attributes("-topmost", True)``  (Keeps window on top)
    | ``window.attributes("-fullscreen", True)``  (Enables fullscreen mode)
    | ``window.attributes("-alpha", 0.8)``  (Sets window transparency)

.. py:attribute:: -alpha

    | Syntax: ``window.attributes("-alpha", value)``
    | Description: Sets the transparency level of the window. Values range from 0 (fully transparent) to 1 (fully opaque).
    | Default: 1 (fully opaque)
    | Example: ``window.attributes("-alpha", 0.8)``

.. py:attribute:: -fullscreen

    | Syntax: ``window.attributes("-fullscreen", True/False)``
    | Description: Enables or disables fullscreen mode for the window.
    | Default: False
    | Example: ``window.attributes("-fullscreen", True)``

.. py:attribute:: -topmost

    | Syntax: ``window.attributes("-topmost", True/False)``
    | Description: Keeps the window on top of all other windows if set to True.
    | Default: False
    | Example: ``window.attributes("-topmost", True)``

.. py:attribute:: -disabled

    | Syntax: ``window.attributes("-disabled", True/False)``
    | Description: Disables user interaction with the window when set to True, making it unresponsive.
    | Default: False
    | Example: ``window.attributes("-disabled", True)``

.. py:attribute:: -toolwindow

    | Syntax: ``window.attributes("-toolwindow", True/False)``
    | Description: Configures the window to be displayed as a tool window with a smaller title bar (Windows only).
    | Default: False
    | Example: ``window.attributes("-toolwindow", True)``

.. py:attribute:: -transparentcolor

    | Syntax: ``window.attributes("-transparentcolor", "color")``
    | Description: Sets a specific color to be transparent in the window, creating a "cutout" effect for that color (Windows only).
    | Default: None
    | Example: ``window.attributes("-transparentcolor", "white")``

.. py:attribute:: -zoomed

    | Syntax: ``window.attributes("-zoomed", True/False)``
    | Description: Opens the window in a maximized (zoomed) state if set to True (Windows only).
    | Default: False
    | Example: ``window.attributes("-zoomed", True)``
