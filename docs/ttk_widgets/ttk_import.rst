====================================================
Importing tkinter themed widgets
====================================================

| In **Tkinter**, themed widgets play a crucial role in determining the "look and feel" of all the widgets.
| See: Tkinter ttk Themed Widgets - Python Tutorial. https://www.pythontutorial.net/tkinter/tkinter-ttk/.
| See: TkDocs Tutorial - Styles and Themes. https://tkdocs.com/tutorial/styles.html.
| See: Tkinter Themes - python tutorials. https://python-tutorials.in/tkinter-themes/.
| See: How to Change Tkinter Theme from One to Another - Python Tutorial. https://www.pythontutorial.net/tkinter/tkinter-theme/.


**Classic Tk Widgets**:
----------------------------

   - These widgets were introduced in 1991 and are part of the original Tkinter library.
   - They have a consistent appearance across platforms but lack the native look and feel.
   - Examples include buttons, labels, entry fields, and scrollbars.

**Themed Tk Widgets (ttk)**:
-----------------------------------

   - Added in 2007 with Tk 8.5, these widgets are an improved version of the classic ones.
   - They aim to separate widget behavior from appearance through a styling system.
   - Themed widgets adapt to the native look and feel of the platform where the program runs.
   - They are imported from the `tkinter.ttk` module.
   - Examples of themed widgets include buttons, checkbuttons, entry fields, and more.

**Advantages of Using Themed Widgets**:
-------------------------------------------------

   - **Behavior-Appearance Separation**: Themed widgets separate code that implements behavior from appearance.
   - **Native Look & Feel**: They provide a native look on different platforms.
   - **Simplified State-Specific Behavior**: ttk widgets simplify state-specific widget behavior.

**Common Themed Widgets**:
----------------------------------

   - Button
   - Checkbutton
   - Entry
   - Frame
   - Label
   - LabelFrame
   - Menubutton
   - PanedWindow
   - Radiobutton
   - Scale
   - Scrollbar
   - Spinbox

1. **New ttk Widgets**:
------------------------------

   - Combobox
   - Notebook
   - Progressbar
   - Separator
   - Sizegrip
   - Treeview


----

Import themed widgets module
----------------------------------------

.. py:function:: from tkinter import ttk

    | This imports the themed module.
    | Refer to themed widgets like this: ttk.Label

| The code below used a standard tk widget and the themed widget.

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk

    root = tk.Tk()

    tk.Label(root, text='Classic Label').pack()
    ttk.Label(root, text='Themed Label').pack()

    window.mainloop()


