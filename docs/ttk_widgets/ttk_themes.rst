====================================================
ttk Themes Introduction
====================================================

| Unlike standard Tkinter widgets, `ttk` (Themed Tkinter) widgets separate their logic from their visual appearance.
| A **Theme** is a collection of styles that defines the overall look and feel of all widgets across an entire application.

| Vista is the default theme in Tkinter on windows.
| For best results in style customization, use the 'clam' theme.

----

Current theme
--------------------

.. py:function:: current_theme = style.theme_use()

    | Retrieves the name of the theme currently being used by the application.
    | Return value is a string (e.g., 'vista').

**Example Code:**

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk

    root = tk.Tk()
    style = ttk.Style()

    # Get the theme currently in use
    current = style.theme_use()
    print(f"Current active theme: {current}")


----


All themes
--------------------

.. py:function:: available_themes = style.theme_names()

    | Retrieves a tuple containing the names of all available themes built into your system's Tkinter engine.
    | Return value is a tuple of strings (e.g., 'winnative', 'clam', 'alt', 'default', 'classic', 'vista', 'xpnative').

**Example Code:**

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk

    root = tk.Tk()
    style = ttk.Style()

    # Get all themes available on this machine
    all_themes = style.theme_names()
    print(f"Available themes: {all_themes}")


----

Set theme
--------------------

| The clam theme is a good default for new applications since it is simple and is most customizable.

.. py:function:: style.theme_use(theme_name)

    | Changes the current application theme to the specified theme name.
    | ``theme_name`` must be a string matching one of the names returned by ``style.theme_names()``.

**Example Code:**

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk

    root = tk.Tk()
    style = ttk.Style()

    # Switch the application's appearance to the 'clam' theme
    style.theme_use("clam")

    # Create a button to see the new theme in action
    button = ttk.Button(root, text="Themed Button")
    button.pack(padx=20, pady=20)

    root.mainloop()



