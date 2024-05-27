====================================================
tk window
====================================================

See: https://www.pythontutorial.net/tkinter/tkinter-window/

----

Simple window
-----------------

.. py:function:: tk.Tk()

   	| Create the main application window.

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

.. py:function:: geometry(widthxheight±x±y)

    | set the size and top left of a window
	| width: The desired width of the window in pixels.
    | height: The desired height of the window in pixels.
    | x: The horizontal position (+ for distance from the left edge of the screen; - from right) in pixels.
    | y: The vertical position (+ for distance from the top edge of the screen; - from bottom) in pixels.

.. py:function:: attributes('-topmost', True)

    | Use the window.attributes('-topmost', True) to make the window always stay on top.

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
-----------------------

.. py:function:: window.winfo_width()

    | returns the width of the Tkinter window.

.. py:function:: window.winfo_height()

	| returns the height of the Tkinter window.

.. py:function:: update_idletasks()

	| The update_idletasks() method is used to process pending idle tasks in a Tkinter window without handling other events.
	| update_idletasks() focuses solely on idle tasks which typically involve geometry management and widget redrawing.
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

Main properties
--------------------

| Main  properties and attributes of the `Tk()` object in Tkinter:
| explore root.attributes('-topmost', True)  # Always on top

1. **geometry(widthxheight±x±y):**
   
   - **Description**: Specifies the window's position and size using the geometry specification: `widthxheight±x±y`.
   - **Use Case Example**: Set the initial position and dimensions of the window. For example, `root.geometry('800x600+100+50')` creates an 800x600 window positioned 100 pixels from the left and 50 pixels from the top.

2. **title("tk"):**
   
   - **Default Value**: `"tk"` (if not explicitly set).
   - **Description**: Sets the window title displayed in the window's title bar.
   - **Use Case Example**: Give your application a meaningful title, e.g., `root.title('My Awesome App')`.

3. **resizable(width_boolean,height_boolean):**
   
   - **Default Value**: Both horizontally and vertically resizable.
   - **Description**: Determines whether the window can be resized by the user. You can set it resizable using `window.resizable(True, True)` method.
   - **Use Case Example**: If you want to create a fixed-size window, disable resizing by calling `window.resizable(False, False)`.

4. **attributes('-alpha', 0.5):**
   
   - **Description**: Sets the transparency level for the window. The value ranges from 0 (completely transparent) to 1 (fully opaque).
   - **Use Case Example**: Create a semi-transparent overlay window for visual effects or notifications.

5. **iconbitmap():**
   
   - **Description**: Sets a custom bitmap (icon) for the window. The bitmap file should be in `.ico` format.
   - **Use Case Example**: Assign a specific icon to your application window.

6. **state("normal"):**
   
   - **Default Value**: `"normal"` (can also be `"iconic"` or `"withdrawn"` or `"zoomed"`.).
   - **Description**: Retrieves or sets the window state (normal, minimized, or withdrawn).
   - **Use Case Example**: Minimize or restore the window programmatically.

7. **iconify():**
   
   - **Description**: Minimizes the window (similar to clicking the minimize button).
   - **Use Case Example**: Implement a custom minimize button in your application.

8. **deiconify():**
   
   - **Description**: Restores a minimized window to its normal state.
   - **Use Case Example**: Restore a minimized window when needed.

9.  **state('zoomed'):**
   
   - **Description**: Maximizes the window to fill the screen.
   - **Use Case Example**: Provide a "Maximize" button for users to expand the window.

10. **withdraw():**
   
    - **Description**: Temporarily hides the window (similar to minimizing but without the taskbar icon).
    - **Use Case Example**: Hide the window during specific application states.

----

Some of the options and attributes associated with the `Tk()` class in Tkinter:

1. **`bd` (borderwidth):**
   
   - **Default Value**: `0`
   - **Description**: Specifies the width of the border around the window. You can set it using the `borderwidth` attribute.
   - **Use Case Example**: If you want to create a custom window border, adjust the `borderwidth` accordingly.

2. **`class`:**
   
   - **Description**: This attribute allows you to set a custom class name for the main window. It can be useful for styling or identifying the window in your application.
   - **Use Case Example**: When applying CSS-like styles to the window, you can use a specific class name.

3. **`menu`:**
   
   - **Description**: The `menu` attribute allows you to associate a menu widget (such as a dropdown menu) with the main window. You can create custom menus and attach them to the window.
   - **Use Case Example**: Create a menu bar with options like "File," "Edit," and "Help" for your application.

4. **`relief`:**
   
   - **Default Value**: `"flat"`
   - **Description**: Determines the appearance of the window border. Common values include "flat," "raised," "sunken," and "groove." You can set the relief style using this attribute.
   - **Use Case Example**: Choose a relief style that matches your application's visual design.

5. **`screen`:**
   
   - **Description**: Specifies the screen where the window should appear. You can use this attribute to position the window on a specific monitor in a multi-monitor setup.
   - **Use Case Example**: If your application spans multiple screens, set the `screen` attribute accordingly.

6. **`use`:**
   
   - **Description**: This attribute is related to the use of the window. For example, you can set it to "yes" or "true" to enable the window or "no" or "false" to disable it.
   - **Use Case Example**: Control whether the window is active or inactive based on user interactions.

7. **`background` (or `bg`):**
   
   - **Description**: Sets the background color of the window. You can provide a color name, hexadecimal value, or use predefined colors like "white," "red," etc.
   - **Use Case Example**: Customize the window background to match your application theme.

8. **`colormap`:**
   
   - **Description**: Specifies the colormap to use for rendering colors. It's relevant when working with color palettes.
   - **Use Case Example**: Advanced graphics applications may require specific colormaps.

9. **`container`:**
   
   - **Description**: In the context of the `Tk()` class, this term doesn't directly apply. However, you can create a container (frame) within the window to organize widgets.
   - **Use Case Example**: Use frames to group related widgets together.

10. **`cursor`:**
   
    - **Description**: Determines the mouse cursor shape when hovering over the window. You can set it to various predefined cursor types (e.g., "arrow," "hand2," "cross," etc.).
    - **Use Case Example**: Change the cursor appearance based on the context (e.g., pointer over a button).

11. **`height` and `width`:**
   
    - **Description**: These attributes define the initial dimensions (height and width) of the window. You can set them explicitly when creating the window.
    - **Use Case Example**: Set the desired window size for your application.

12. **`highlightbackground` and `highlightcolor`:**
   
    - **Description**: These attributes control the color of the focus highlight when the window is active. You can customize them to match your application's theme.
    - **Use Case Example**: Highlight the active window or focused widgets.

13. **`highlightthickness`:**
   
    - **Default Value**: `0`
    - **Description**: Specifies the width of the focus highlight border. You can adjust it to make the focus border more or less prominent.
    - **Use Case Example**: Add a subtle border around focused widgets.

14. **`padx` and `pady`:**
   
    - **Description**: These attributes allow you to add padding (extra space) around the window content. Useful for spacing widgets within the window.
    - **Use Case Example**: Create consistent spacing between widgets.

15. **`takefocus`:**
   
    - **Default Value**: `0`
    - **Description**: Determines whether the window can receive keyboard focus. Set it to `1` (True) or `0` (False) accordingly.
    - **Use Case Example**: Control whether the window responds to keyboard input.

16. **`visual`:**
   
    - **Description**: Specifies the visual display mode (e.g., "directcolor," "pseudocolor," etc.). Relevant for advanced graphics applications.
    - **Use Case Example**: If your application requires specific color rendering modes, set the appropriate visual.

