====================================================
Login form: custom message box
====================================================

| This uses the same login form code as displayed on previous pages, but adds a customized messagebox that is centred over the window instead of the screen.

.. image:: images/tk_login.png
    :scale: 67%

----

Custom top level window for a message box
----------------------------------------------

Custom Messagebox Function
==========================

This section explains how the `custom_messagebox` function works, which is used to display a message box aligned precisely over the parent widget in a Tkinter application.

Code
------

.. code-block:: python

    def custom_messagebox(title, message, parent):
        """Custom messagebox aligned over the parent widget."""
        top = tk.Toplevel(parent)  # Create a new top-level window
        top.title(title)
        top.configure(bg=BG_COLOR)
        top.transient(parent)  # Keep it on top of the parent
        top.grab_set()  # Make it modal (block input to the parent)

        # Center the top-level window over the parent
        parent_x = parent.winfo_rootx()
        parent_y = parent.winfo_rooty()
        parent_width = parent.winfo_width()
        parent_height = parent.winfo_height()

        # Calculate position to center the messagebox over the parent
        top_width = 500
        top_height = 150
        x = parent_x + (parent_width // 2) - (top_width // 2)
        y = parent_y + (parent_height // 2) - (top_height // 2)

        top.geometry(f"{top_width}x{top_height}+{x}+{y}")

        # Create widgets inside the custom messagebox
        message_label = tk.Label(top, text=message, bg=BG_COLOR, fg=FG_COLOR, font=FONT_STYLE)
        ok_button = tk.Button(top, text="OK", bg=FG_BUTTON_COLOR, fg=FG_COLOR, font=FONT_STYLE, command=top.destroy)

        # Layout the widgets
        message_label.pack(expand=True, pady=20)
        ok_button.pack(pady=10)

Explanation
-------------

Creating a Toplevel Window
~~~~~~~~~~~~~~~~~~~~~~~~~~~

- `top = tk.Toplevel(parent)`: This creates a new top-level window, which behaves like a popup.
- `top.title(title)`: Sets the title of the messagebox window.
- `top.configure(bg=BG_COLOR)`: Configures the background color of the window to match the theme.

Making the Window Modal
~~~~~~~~~~~~~~~~~~~~~~~~~

 - `top.transient(parent)`: Ensures the messagebox stays on top of the parent window.
 - `top.grab_set()`: Activates a "grab" on the messagebox, preventing the user from interacting with the main window until the messagebox is closed.

Positioning the Messagebox over the Parent Window
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 - We use the following Tkinter methods to determine the position and size of the parent widget:
   - `winfo_rootx()` and `winfo_rooty()`: Get the top-left coordinates of the parent window on the screen.
   - `winfo_width()` and `winfo_height()`: Get the width and height of the parent widget.

Calculating the Centered Position
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 - We compute the `x` and `y` coordinates to align the messagebox in the center of the parent:
   - `x = parent_x + (parent_width // 2) - (top_width // 2)`
   - `y = parent_y + (parent_height // 2) - (top_height // 2)`
 - The messagebox is then positioned using:
   - `top.geometry(f"{top_width}x{top_height}+{x}+{y}")`

Creating the Messagebox Content
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 - A `Label` widget is used to display the message:
   - `message_label = tk.Label(top, text=message, bg=BG_COLOR, fg=FG_COLOR, font=FONT_STYLE)`
 - A `Button` widget is used to close the messagebox:
   - `ok_button = tk.Button(top, text="OK", bg=FG_BUTTON_COLOR, fg=FG_COLOR, font=FONT_STYLE, command=top.destroy)`

Packing the Widgets
~~~~~~~~~~~~~~~~~~~~~~~~~

 - `message_label.pack(expand=True, pady=20)`: Expands the label to fill available space and adds vertical padding.
 - `ok_button.pack(pady=10)`: Adds the OK button with some vertical padding.

Usage
~~~~~~~~~~~~~~

| This function can be used in any Tkinter application where you need a custom messagebox that is aligned directly over a specific parent widget.
| Here's how you can call the function:

.. code-block:: python

    custom_messagebox("Login", "Logged in successfully!", frame)

| This call creates a messagebox titled "Login" with the message "Logged in successfully!" positioned over the `frame` widget.

----

Full code
------------

.. code-block:: python

    import tkinter as tk

    # Constants
    BG_COLOR = "#333333"  # dark grey
    FG_COLOR = "#FFFFFF"   # white
    FG_BUTTON_COLOR = "#FF3399"  # bright pink
    FONT_STYLE = ("Arial", 24)
    USERNAME = "johns"
    PASSWORD = "123"


    def custom_messagebox(title, message, parent):
        """Custom messagebox aligned over the parent widget."""
        top = tk.Toplevel(parent)  # Create a new top-level window
        top.title(title)
        top.configure(bg=BG_COLOR)
        top.transient(parent)  # Keep it on top of the parent
        top.grab_set()  # Make it modal (block input to the parent)

        # Center the top-level window over the parent
        parent_x = parent.winfo_rootx()
        parent_y = parent.winfo_rooty()
        parent_width = parent.winfo_width()
        parent_height = parent.winfo_height()

        # Calculate position to center the messagebox over the parent
        top_width = 300
        top_height = 150
        x = parent_x + (parent_width // 2) - (top_width // 2)
        y = parent_y + (parent_height // 2) - (top_height // 2)

        top.geometry(f"{top_width}x{top_height}+{x}+{y}")

        # Create widgets inside the custom messagebox
        message_label = tk.Label(top, text=message, bg=BG_COLOR, fg=FG_COLOR, font=FONT_STYLE)
        ok_button = tk.Button(top, text="OK", bg=FG_BUTTON_COLOR, fg=FG_COLOR, font=FONT_STYLE, command=top.destroy)

        # Layout the widgets
        message_label.pack(expand=True, pady=20)
        ok_button.pack(pady=10)


    def login():
        entered_username = username_entry.get()
        entered_password = password_entry.get()
        if entered_username == USERNAME and entered_password == PASSWORD:
            custom_messagebox("Login", "Logged in successfully!", frame)
        else:
            custom_messagebox("Login Error", "Invalid login", frame)


    # Create the main window
    window = tk.Tk()
    window.title("Login form")
    window.geometry("540x440")
    window.configure(bg=BG_COLOR)

    # Create frame widget for other widgets
    frame = tk.Frame(window, bg=BG_COLOR)
    frame.place(relx=0.5, rely=0.5, anchor='center')  # Centering the frame inside the window

    # Create widgets inside the frame
    login_label = tk.Label(frame, text="Login", bg=BG_COLOR, fg=FG_BUTTON_COLOR, font=FONT_STYLE)
    username_label = tk.Label(frame, text="Username", bg=BG_COLOR, fg=FG_COLOR, font=FONT_STYLE)
    password_label = tk.Label(frame, text="Password", bg=BG_COLOR, fg=FG_COLOR, font=FONT_STYLE)
    username_entry = tk.Entry(frame, font=FONT_STYLE)
    password_entry = tk.Entry(frame, show="*", font=FONT_STYLE)
    login_button = tk.Button(frame, text="Login", bg=FG_BUTTON_COLOR, fg=FG_COLOR, font=FONT_STYLE, command=login)

    # Place widgets in the frame using grid layout
    login_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=20)
    username_label.grid(row=1, column=0, padx=10)
    password_label.grid(row=2, column=0, padx=10)
    username_entry.grid(row=1, column=1, pady=20)
    password_entry.grid(row=2, column=1, pady=20)
    login_button.grid(row=3, column=0, columnspan=2, pady=20)

    window.mainloop()
