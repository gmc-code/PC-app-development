tk Button Widget: Key Methods
==================================

The Tkinter `Button` widget includes essential methods for configuring its appearance, setting actions, and managing its behavior. Below is a curated list of the most commonly used methods.


config (or configure)
----------------------

The ``config`` method is used to set various configuration options for the button, such as `text`, `command`, and `state`.

Usage:
    .. code-block:: python

        button.config(option=value, ...)

Example:
    .. code-block:: python

        button.config(text="Click Me", command=callback_function, state="normal")

- **text**: Sets the label displayed on the button.
- **command**: Function to execute when the button is clicked.
- **state**: Sets the button state, e.g., `"normal"`, `"disabled"`.

----

invoke
------

The ``invoke`` method simulates a button click programmatically, triggering the associated command.

Usage:
    .. code-block:: python

        button.invoke()

Example:
    .. code-block:: python

        button.invoke()  # Calls the command function as if the button was clicked

----

bind
----

The ``bind`` method associates a callback function with a specific event, allowing custom handling of mouse and keyboard events on the button.

Usage:
    .. code-block:: python

        button.bind(event, callback)

- **event**: Specifies the event, e.g., `"<Button-1>"` for a left-click.
- **callback**: The function to call when the event occurs.

Example:
    .. code-block:: python

        def on_right_click(event):
            print("Right-click detected")

        button.bind("<Button-3>", on_right_click)  # Binds right-click to the callback function

----

Tkinter Button Events
-----------------------

Mouse Events
~~~~~~~~~~~~~~~~~~~

- **``<Button-1>``**: Left mouse button click.
- **``<Button-2>``**: Middle mouse button click.
- **``<Button-3>``**: Right mouse button click.
- **``<Double-Button-1>``**: Double-click with the left mouse button.
- **``<ButtonRelease-1>``**: Release of the left mouse button.
- **``<Enter>``**: Mouse pointer enters the widget.
- **``<Leave>``**: Mouse pointer leaves the widget.
- **``<Motion>``**: Mouse pointer moves within the widget.
- **``<MouseWheel>``**: Mouse wheel is scrolled.

Keyboard Events
~~~~~~~~~~~~~~~~~~~

- **``<KeyPress>``**: Any key is pressed.
- **``<KeyRelease>``**: Any key is released.
- **``<Return>``**: Enter key is pressed.
- **``<Escape>``**: Escape key is pressed.
- **``<Control-Key>``**: Control key is pressed along with another key (e.g., ``<Control-c>`` for Ctrl+C).

Focus Events
~~~~~~~~~~~~~~~~~~~

- **``<FocusIn>``**: Widget gains focus.
- **``<FocusOut>``**: Widget loses focus.

Window Events
~~~~~~~~~~~~~~~~~~~

- **``<Configure>``**: Widget is resized or moved.
- **``<Destroy>``**: Widget is destroyed.
- **``<Expose>``**: Part of the widget becomes visible after being covered.

Example Usage
~~~~~~~~~~~~~~~~~~~

Here's an example of how to bind some of these events to a button:

.. code-block:: python

    import tkinter as tk

    def on_click(event):
        print("Button clicked!")

    def on_double_click(event):
        print("Button double-clicked!")

    def on_enter(event):
        print("Mouse entered button area!")

    def on_leave(event):
        print("Mouse left button area!")

    root = tk.Tk()
    button = tk.Button(root, text="Click Me")
    button.bind("<Button-1>", on_click)
    button.bind("<Double-Button-1>", on_double_click)
    button.bind("<Enter>", on_enter)
    button.bind("<Leave>", on_leave)
    button.pack()

    root.mainloop()

----

flash
-----

The ``flash`` method provides visual feedback by making the button flash momentarily. This effect can be used to grab attention.

Usage:
    .. code-block:: python

        button.flash()

Example:
    .. code-block:: python

        button.flash()  # Causes the button to flash briefly

----

cget
----

The ``cget`` method retrieves the current value of a specific configuration option on the button.

Usage:
    .. code-block:: python

        value = button.cget("option")

Example:
    .. code-block:: python

        text = button.cget("text")  # Retrieves the text displayed on the button

- **option**: Name of the option to retrieve (e.g., `"text"`, `"state"`).

----

grid, pack, place
------------------

The layout methods ``grid``, ``pack``, and ``place`` control the placement of the button in the GUI.

- **grid**: Places the widget in a grid layout.
- **pack**: Packs the widget into its parent, using available space.
- **place**: Places the widget at an absolute position.

Usage:
    .. code-block:: python

        button.grid(row=0, column=1)
        button.pack(fill="both", expand=True)
        button.place(x=50, y=100)

Example:
    .. code-block:: python

        button.pack(pady=10)  # Packs the button with padding around it

----

focus_set
---------

The ``focus_set`` method sets the focus on the button, allowing it to receive keyboard events.

Usage:
    .. code-block:: python

        button.focus_set()

Example:
    .. code-block:: python

        button.focus_set()  # Sets focus to the button

----

unbind
------

The ``unbind`` method removes an event binding from the button.

Usage:
    .. code-block:: python

        button.unbind(event)

- **event**: The event to remove, such as `"<Button-1>"`.

Example:
    .. code-block:: python

        button.unbind("<Button-1>")  # Removes left-click binding from the button

----

destroy
-------

The ``destroy`` method deletes the button widget from the GUI.

Usage:
    .. code-block:: python

        button.destroy()

Example:
    .. code-block:: python

        button.destroy()  # Removes the button from the interface

----

Tkinter Button Widget: Grouped Methods by Function
--------------------------------------------------------

Event Handling and Scheduling
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- **after**: Schedules a function to run after a specified delay in milliseconds.
- **after_cancel**: Cancels a function scheduled with ``after``.
- **after_idle**: Runs a function as soon as the Tkinter event loop is idle.
- **after_info**: Retrieves information about scheduled ``after`` events.
- **bind**: Binds an event to a widget-specific callback function.
- **bind_all**: Binds an event to all widgets.
- **bind_class**: Binds an event to all widgets of a specific class.
- **bindtags**: Manages event binding tags for the widget.
- **event_add**: Adds virtual events to the event bindings.
- **event_delete**: Deletes virtual events from the event bindings.
- **event_generate**: Simulates an event for the widget.
- **event_info**: Provides information on virtual events.
- **flash**: Temporarily flashes the widget for visual feedback.

Focus and Selection
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- **focus**: Sets the input focus to the widget.
- **focus_displayof**: Returns the widget that has focus in the display.
- **focus_force**: Forces focus onto the widget.
- **focus_get**: Retrieves the widget that currently has focus.
- **focus_lastfor**: Returns the last widget that held the focus.
- **focus_set**: Sets focus explicitly on the widget.
- **selection_clear**: Clears the selection in the widget.
- **selection_get**: Gets the selection content.
- **selection_handle**: Defines a function to handle selections.
- **selection_own**: Takes ownership of the selection.
- **selection_own_get**: Returns the current owner of the selection.

Clipboard Operations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- **clipboard_append**: Appends text to the system clipboard.
- **clipboard_clear**: Clears the system clipboard.
- **clipboard_get**: Retrieves text from the system clipboard.

Geometry Management (Grid, Pack, Place)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- **columnconfigure**: Configures grid column properties.
- **config**: Sets one or more widget options.
- **configure**: Alias for ``config``.
- **grid**: Places the widget in a grid.
- **grid_anchor**: Sets the anchor for the grid layout.
- **grid_bbox**: Returns the bounding box for the widget's grid area.
- **grid_columnconfigure**: Configures a column in the grid.
- **grid_configure**: Configures the grid options for the widget.
- **grid_forget**: Removes the widget from the grid without deleting it.
- **grid_info**: Returns information about the grid layout.
- **grid_location**: Returns grid coordinates of a point.
- **grid_propagate**: Controls whether the grid can resize the widget.
- **grid_remove**: Temporarily removes the widget from the grid.
- **grid_rowconfigure**: Configures a row in the grid.
- **grid_size**: Returns the size of the grid.
- **grid_slaves**: Returns the widgets managed by the grid manager.
- **pack**: Packs the widget into its parent.
- **pack_configure**: Configures options for the ``pack`` geometry manager.
- **pack_forget**: Unpacks the widget from the layout.
- **pack_info**: Returns information on the ``pack`` layout.
- **pack_propagate**: Controls whether ``pack`` can resize the widget.
- **pack_slaves**: Returns children managed by the ``pack`` geometry manager.
- **place**: Places the widget at an absolute position.
- **place_configure**: Configures options for the ``place`` geometry manager.
- **place_forget**: Unplaces the widget from the layout.
- **place_info**: Returns information on the ``place`` layout.
- **place_slaves**: Returns children managed by the ``place`` geometry manager.
- **propagate**: Controls geometry propagation of the widget.
- **forget**: Removes the widget from the screen but doesn't destroy it.

Display and Layer Control
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- **anchor**: Sets the position of text or images within the widget.
- **bbox**: Returns bounding box coordinates of a specified item.
- **lift**: Raises the widget above sibling widgets.
- **location**: Returns the screen coordinates of the widget.
- **lower**: Lowers the widget below sibling widgets.
- **tkraise**: Raises the widget in the stacking order.

Widget Information
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- **cget**: Retrieves the current value of a widget configuration option.
- **info**: Retrieves information about the widget's options.
- **info_patchlevel**: Returns the Tkinter patch level.
- **keys**: Returns a list of all configuration options for the widget.
- **winfo_atom**: Converts a string to a Tkinter atom.
- **winfo_atomname**: Converts an atom to a string.
- **winfo_cells**: Returns the number of cells in the widget's colormap.
- **winfo_children**: Returns a list of the widget's children.
- **winfo_class**: Returns the widget class name.
- **winfo_colormapfull**: Checks if the colormap is full.
- **winfo_containing**: Returns the widget at a specific screen location.
- **winfo_depth**: Returns the color depth of the widget.
- **winfo_exists**: Checks if the widget exists.
- **winfo_fpixels**: Converts a distance to floating-point pixels.
- **winfo_geometry**: Returns the widget's geometry string.
- **winfo_height**: Returns the widget's height in pixels.
- **winfo_id**: Returns the widget's unique identifier.
- **winfo_interps**: Returns a list of Tcl interpreters.
- **winfo_ismapped**: Checks if the widget is mapped.
- **winfo_manager**: Returns the widget's geometry manager.
- **winfo_name**: Returns the widget's name.
- **winfo_parent**: Returns the widget's parent name.
- **winfo_pathname**: Returns the widget's full path.
- **winfo_pixels**: Converts a distance to integer pixels.
- **winfo_pointerx**: Returns the x-coordinate of the pointer.
- **winfo_pointerxy**: Returns the pointer coordinates.
- **winfo_pointery**: Returns the y-coordinate of the pointer.
- **winfo_reqheight**: Returns the widget's requested height.
- **winfo_reqwidth**: Returns the widget's requested width.
- **winfo_rgb**: Returns the RGB color value.
- **winfo_rootx**: Returns the widget's x-coordinate relative to root.
- **winfo_rooty**: Returns the widget's y-coordinate relative to root.
- **winfo_screen**: Returns the screen's name.
- **winfo_screencells**: Returns the number of cells in the screen colormap.
- **winfo_screendepth**: Returns the screen color depth.
- **winfo_screenheight**: Returns the screen height in pixels.
- **winfo_screenmmheight**: Returns the screen height in mm.
- **winfo_screenmmwidth**: Returns the screen width in mm.
- **winfo_screenvisual**: Returns the screen visual class.
- **winfo_screenwidth**: Returns the screen width in pixels.
- **winfo_server**: Returns the server information.
- **winfo_toplevel**: Returns the top-level widget.
- **winfo_viewable**: Checks if the widget is visible.
- **winfo_visual**: Returns the visual class for the widget.
- **winfo_visualid**: Returns the widget's visual ID.
- **winfo_visualsavailable**: Returns available visuals.
- **winfo_vrootheight**: Returns the virtual root window height.
- **winfo_vrootwidth**: Returns the virtual root window width.
- **winfo_vrootx**: Returns the x-offset for the virtual root.
- **winfo_vrooty**: Returns the y-offset for the virtual root.
- **winfo_width**: Returns the widget's width in pixels.
- **winfo_x**: Returns the widget's x-coordinate.
- **winfo_y**: Returns the widget's y-coordinate.

Control and State Management
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- **invoke**: Simulates a button click programmatically.
- **deletecommand**: Deletes a Tcl command.
- **destroy**: Removes the widget from the GUI.
- **quit**: Exits the Tkinter application.
- **send**: Sends a command to another application.
- **setvar**: Sets a Tcl variable to a specific value.
- **getvar**: Returns the value of a Tcl variable.
- **busy**: Simulates a busy cursor on the widget.
- **busy_cget**: Gets a configuration option for the busy state.
- **busy_config**: Configures busy state options.
- **busy_configure**: Sets configuration for the busy state.
- **busy_current**: Checks if the current widget is busy.
- **busy_forget**: Resets the widget from a busy state.
- **busy_hold**: Temporarily applies the busy state to a widget.
- **busy_status**: Checks the busy status of the widget.

Tk and System Interaction
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- **mainloop**: Starts the Tkinter event loop.
- **register**: Registers a Python function as a Tcl command.
- **tk_bisque**: Applies the Bisque color scheme to the app.
- **tk_busy**: Sets the entire application to a busy state.
- **tk_focusFollowsMouse**: Sets focus to follow the mouse.
- **tk_focusNext**: Moves focus to the next widget.
- **tk_focusPrev**: Moves focus to the previous widget.
- **tk_setPalette**: Changes the application's color palette.
- **tk_strictMotif**: Toggles strict Motif compliance.

Waiting and Updates
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- **update**: Updates the widget immediately.
- **update_idletasks**: Updates idle tasks without processing events.
- **wait_variable**: Waits until a variable is modified.
- **wait_visibility**: Waits until the widget is visible.
- **wait_window**: Waits until a window is destroyed.
