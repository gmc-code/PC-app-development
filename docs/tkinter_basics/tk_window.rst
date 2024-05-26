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
    window.geometry('600x400')

    # Start the main event loop
    window.mainloop()

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

17. **`padx` and `pady`:**
    - **Description**: These attributes allow you to add padding (extra space) around the window content. Useful for spacing widgets within the window.
    - **Use Case Example**: Create consistent spacing between widgets.

18. **`takefocus`:**
    - **Default Value**: `0`
    - **Description**: Determines whether the window can receive keyboard focus. Set it to `1` (True) or `0` (False) accordingly.
    - **Use Case Example**: Control whether the window responds to keyboard input.

19. **`visual`:**
    - **Description**: Specifies the visual display mode (e.g., "directcolor," "pseudocolor," etc.). Relevant for advanced graphics applications.
    - **Use Case Example**: If your application requires specific color rendering modes, set the appropriate visual.

