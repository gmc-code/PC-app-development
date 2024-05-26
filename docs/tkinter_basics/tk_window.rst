====================================================
tk window
====================================================


Simple window
-----------------


| Below is the code to create a simple empty window. 

.. code-block:: python

    import tkinter as tk

    # Create the main application window
    window = tk.Tk()

    # Start the main event loop
    window.mainloop()

----

Window properties
-----------------------

.. code-block:: python

    import tkinter as tk

    # Create the main application window
    window = tk.Tk()
    window.title("Tkinter hello world")
    .. window.geometry('600x400')
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x-coord= 0
    y-coord= 0
    window.geometry("{}x{}+{}+{}".format(screen_width, screen_height, x-coord, y-coord))


    # Start the main event loop
    window.mainloop()

----

Certainly! Let's explore additional properties and attributes of the `Tk()` object in Tkinter, including geometry settings, default values, descriptions, and use case examples:

1. **Resizable (resizable()):**
   - **Default Value**: Both horizontally and vertically resizable.
   - **Description**: Determines whether the window can be resized by the user. You can set it using the `resizable()` method.
   - **Use Case Example**: If you want to create a fixed-size window, disable resizing by calling `window.resizable(False, False)`.

2. **Transparency (attributes('-alpha', 0.5)):**
   - **Description**: Sets the transparency level for the window. The value ranges from 0 (completely transparent) to 1 (fully opaque).
   - **Use Case Example**: Create a semi-transparent overlay window for visual effects or notifications.

3. **Icon Bitmap (iconbitmap()):**
   - **Description**: Sets a custom bitmap (icon) for the window. The bitmap file should be in `.ico` format.
   - **Use Case Example**: Assign a specific icon to your application window.

4. **Window State (state()):**
   - **Default Value**: `"normal"` (can also be `"iconic"` or `"withdrawn"`).
   - **Description**: Retrieves or sets the window state (normal, minimized, or withdrawn).
   - **Use Case Example**: Minimize or restore the window programmatically.

5. **Window Position (geometry()):**
   - **Description**: Specifies the window's position and size using the geometry specification: `widthxheight±x±y`.
   - **Use Case Example**: Set the initial position and dimensions of the window. For example, `root.geometry('800x600+100+50')` creates an 800x600 window positioned 100 pixels from the left and 50 pixels from the top.

6. **Window Title (title()):**
   - **Default Value**: `"tk"` (if not explicitly set).
   - **Description**: Sets the title displayed in the window's title bar.
   - **Use Case Example**: Give your application a meaningful title, e.g., `root.title('My Awesome App')`.

7. **Window Iconify (iconify()):**
   - **Description**: Minimizes the window (similar to clicking the minimize button).
   - **Use Case Example**: Implement a custom minimize button in your application.

8. **Window Deiconify (deiconify()):**
   - **Description**: Restores a minimized window to its normal state.
   - **Use Case Example**: Restore a minimized window when needed.

9. **Window Maximize (state('zoomed')):**
   - **Description**: Maximizes the window to fill the screen.
   - **Use Case Example**: Provide a "Maximize" button for users to expand the window.

10. **Window Withdraw (withdraw()):**
    - **Description**: Temporarily hides the window (similar to minimizing but without the taskbar icon).
    - **Use Case Example**: Hide the window during specific application states.

Remember that these attributes allow you to customize the behavior and appearance of your Tkinter window. Feel free to experiment with them to create a user-friendly interface for your application! 🖼️🔧

If you have any more questions or need further assistance, feel free to ask! 😊

Source: Conversation with Copilot, 27/05/2024
(1) An Essential Guide to Tkinter Window - Python Tutorial. https://www.pythontutorial.net/tkinter/tkinter-window/.
(2) Geometry Method in Python Tkinter - GeeksforGeeks. https://www.geeksforgeeks.org/python-geometry-method-in-tkinter/.
(3) Passing variables to Tkinter geometry method - Stack Overflow. https://stackoverflow.com/questions/27574854/passing-variables-to-tkinter-geometry-method.
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

