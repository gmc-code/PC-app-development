====================================================
Tkinter widgets
====================================================

Tkinter provides a collection of widgets that are used to build graphical user interfaces (GUIs). Widgets are the visible components of an application, such as buttons, labels, text boxes, menus, and list controls. Each widget is designed for a specific purpose and can be customised using configuration options such as colours, fonts, sizes, and event bindings.

Most widgets are created by passing a parent widget (typically a ``Tk`` window or ``Frame``) followed by optional keyword arguments.

.. py:function:: widget = tk.Widget(parent, option=value)

    | ``parent`` is the window or frame or container that will contain the widget.
    | Widget options are supplied as keyword arguments separated by commas.
    | e.g. ``button = tk.Button(root, text="OK")``

Widgets are typically positioned within their parent using one of Tkinter's geometry managers:

* ``pack()`` - Arranges widgets one after another.
* ``grid()`` - Arranges widgets in rows and columns.
* ``place()`` - Positions widgets using absolute or relative coordinates.

.. note::

    A widget should generally use only one geometry manager within the same parent container. Mixing ``pack()`` and ``grid()`` inside the same parent widget can produce unexpected results.

----

Common Tkinter widgets
----------------------

The following table lists the widgets available in the standard ``tkinter`` package.

.. list-table::
    :header-rows: 1
    :widths: 28 72

    * - Widget
      - Description
    * - ``Button``
      - A clickable button used to perform an action.
    * - ``Canvas``
      - A drawing surface for graphics, images, shapes and custom widgets.
    * - ``Checkbutton``
      - A check box that can be either selected or cleared.
    * - ``Entry``
      - A single-line text entry field.
    * - ``Frame``
      - A container used to group and organise other widgets.
    * - ``Label``
      - Displays text, images or other information.
    * - ``LabelFrame``
      - A frame with a title displayed along its border.
    * - ``Listbox``
      - Displays a list of selectable text items.
    * - ``Menu``
      - Creates application menus and context (popup) menus.
    * - ``Menubutton``
      - A button that displays an associated menu.
    * - ``Message``
      - Displays automatically wrapped multi-line text.
    * - ``OptionMenu``
      - Displays a drop-down list of choices.
    * - ``PanedWindow``
      - A container with resizable panes separated by draggable dividers.
    * - ``Radiobutton``
      - Allows one option to be selected from a group.
    * - ``Scale``
      - A slider used to select a numeric value.
    * - ``Scrollbar``
      - Provides horizontal or vertical scrolling for compatible widgets.
    * - ``Spinbox``
      - Allows selection of a value by typing or using increment/decrement arrows.
    * - ``Text``
      - A multi-line text editing widget with rich formatting support.
    * - ``Toplevel``
      - Creates an additional application window.

----

Themed ttk widgets
------------------

The ``tkinter.ttk`` module provides themed versions of many standard Tkinter widgets. These widgets adopt the native appearance of the operating system and are generally recommended for modern applications.

Common ``ttk`` widgets include:

* ``Button``
* ``Checkbutton``
* ``Combobox``
* ``Entry``
* ``Frame``
* ``Label``
* ``LabelFrame``
* ``Menubutton``
* ``Notebook``
* ``PanedWindow``
* ``Progressbar``
* ``Radiobutton``
* ``Scale``
* ``Scrollbar``
* ``Separator``
* ``Sizegrip``
* ``Spinbox``
* ``Treeview``

.. note::

    Some widgets, such as ``Canvas``, ``Text``, ``Listbox`` and ``Menu``, do not have themed ``ttk`` equivalents and continue to use their standard ``tkinter`` implementations.

----

Choosing the right widget
-------------------------

======================== ============================
Task                     Recommended widget
======================== ============================
Display text             ``Label``
Display long text        ``Message``
Single-line input        ``Entry``
Multi-line input         ``Text``
Choose one option        ``Radiobutton``
Choose many options      ``Checkbutton``
Choose from a list       ``Listbox`` or ``Combobox``
Numeric input            ``Spinbox`` or ``Scale``
Perform an action        ``Button``
Group widgets            ``Frame`` or ``LabelFrame``
Display graphics         ``Canvas``
Show hierarchical data   ``Treeview``
======================== ============================


