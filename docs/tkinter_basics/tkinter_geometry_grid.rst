====================================================
tk geometry grid
====================================================

| The grid geometry manager allows you to arrange widgets within a window.
| See: https://tkdocs.com/tutorial/grid.html
| grid: see https://www.youtube.com/watch?v=IJ-iVnN09-8
| grid: see https://www.pythontutorial.net/tkinter/tkinter-grid/
| Layouts: https://www.youtube.com/watch?v=i577cFu8eBI&list=PLpMixYKO4EXflJFPhTvZOVAbs7lBdEBSa

----

grid
----------

| Each row and column in the grid is identified by an index. By default, the indices start at zero.
| The row and column indexes can have gaps. This is useful when you plan to add more widgets in the middle of the grid later.
| The intersection of a row and a column is called a cell. One widget can be placed in a cell.
| To place multiple widgets in a cell, use a Frame or LabelFrame to wrap the widgets and place the Frame or LabelFrame on the cell.
| The width of a column depends on the width of the widget it contains. 
| The height of a row depends on the height of the widgets contained within the row.


.. py:function:: widget.grid(row=index_r, column=index_c)

    | Use **grid()** method to position a widget on a grid at row index_r and column index_c.
    | e.g. widget.grid(row=0, column=0)


Options
~~~~~~~~~~~~

| Specify multiple rows and columns for widget uisng **rowspan** or **columnspan**.
| Specify cell alignment. Use the **sticky** option to align the position of the widget on a cell and define how the widget will be stretched.
| Specify padding. Use **ipadx**, **ipady** and **padx**, **pady** to add internal and external paddings.

.. py:function:: widget.grid(row=index_r, column=index_c, rowspan=n)

    | Specify number of rows, **n**, for a widget to span across
    | e.g. grid(row=0, column=0, rowspan=2) to span the widget across 2 rows.

.. py:function:: widget.grid(row=index_r, column=index_c, columnspan=n)

    | Specify number of columns, **n**, for a widget to span across
    | e.g. grid(row=0, column=0, columnspan=2) to span the widget across 2 columns.

.. py:function:: widget.grid(row=index_r, column=index_c, padx=n)

    | Add horizontal padding, **n** pixels, on both sides of the widget.
    | e.g. widget.grid(row=0, column=0, padx=10) to add 10 pixels of space on the left and on the right of the widget.

.. py:function:: widget.grid(row=index_r, column=index_c, pady=n)

    | Add vertical padding, **n** pixels, above and below the widget.
    | e.g. widget.grid(row=0, column=0, pady=10) to add 10 pixels of space above and below the widget.


.. py:function:: widget.grid(row=index_r, column=index_c, ipadx=n)

    | Add horizontal internal padding, **n** pixels, on both sides of the widget.
    | e.g. widget.grid(row=0, column=0, ipadx=10) to grow the widget to the left and right, by 10 pixels each.

.. py:function:: widget.grid(row=index_r, column=index_c, ipady=n)

    | Add vertical internal padding, **n** pixels, above and below the widget.
    | e.g. widget.grid(row=0, column=0, ipady=10) to grow the widget by 10 pixels above and below the widget.


----

notes
~~~~~~~~~~~~~~

| For grid, empty rows or columns are not allocated screen space.
| Grid determines how much space a widget can occupy, not how much it does occupy.
| By default, widgets are placed in the middle of a grid cell.

----

columnconfigure and rowconfigure
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| This is not recommended, except for special use cases, such as when designing GUIs that need to adapt to different screen sizes.
| The allows widgets to stretch in size when the window is resized.
| Use the columnconfigure() and rowconfigure() methods to specify the weight of a column and a row of a grid.

.. py:function:: widget.columnconfigure(column, option=value, ...)

    | Configure the column properties of a widget container, typically a `Frame` or `Grid`. 
    | `widget`: The widget container (e.g., `Frame`, `Grid`) for which to configure the columns.
    | `column`: The index of the column to configure, starting from 0. Use a tuple such as (0, 1, 2) for several columns.
    | Specify options such as minimum size, weight, and stretching behavior for the column within the container.
  
    - `option=value`: Options for configuring the column include:
    - `minsize`: Specifies the minimum size of the column.
    - `weight`: Resizes column on window resizing. Determines how much any extra space is distributed among columns. Columns with higher weights will get more space.
    - `uniform`: If set to a string value, columns with the same value will be of the same size.
    - `pad`: Specifies padding to add around the column.
    -  e.g. `window.columnconfigure(1, weight=2, pad=10)`

.. py:function:: widget.rowconfigure(row, option=value, ...)

    | Configure the row properties of a widget container, typically a `Frame` or `Grid`. 
    | Specify options such as minimum size, weight, and stretching behavior for the row within the container.

----

grid related methods
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:function:: widget.grid_bbox(column=None, row=None, col2=None, row2=None)

    | Returns a 4-tuple describing the bounding box of the widget area. 
    | The first two numbers returned are the x and y coordinates of the upper left corner of the area, and the second two numbers are the width and height.
    | If column and row arguments are passed in, the returned bounding box describes the area of the cell at that column and row. 
    | If col2 and row2 arguments are passed in, the returned bounding box describes the area of the grid from columns column to col2 inclusive, and from rows row to row2 inclusive.
    | For example, widget.grid_bbox(0, 0, 1, 1) returns the bounding box of four cells, not one.

.. py:function:: widget.grid_forget()

    | This makes the widget disappear from the screen. It still exists but isn't visible. 
    | Use .grid() it to make it appear again, but without its grid options.

.. py:function:: widget.grid_info()
    
    | Returns a dictionary whose keys are the widgets's option names, with the corresponding values of those options.

.. py:function:: widget.grid_location(x, y)

    | Given a coordinates (x, y) relative to the containing widget, this method returns a tuple (col, row) describing what cell of the grid system contains that screen coordinate.

.. py:function:: widget.grid_propagate()

    | Normally, all widgets propagate their dimensions, meaning that they adjust to fit the contents. 
    | However, sometimes you want to force a widget to be a certain size, regardless of the size of its contents. 
    | To do this, call widget.grid_propagate(0) where w is the widget whose size you want to force.

.. py:function:: widget.grid_remove()

    | This method is like .grid_forget(), but its grid options are remembered, so if you .grid() it again, it will use the same grid configuration options.

.. py:function:: widget.grid_size()

    | Returns a 2-tuple containing the number of columns and the number of rows, respectively, in the grid system.

.. py:function:: widget.grid_slaves(row=None, column=None)

    | Returns a list of the widgets managed by the given widget. 
    | If no arguments are provided, you will get a list of all the managed widgets. 
    | Use the row= argument to select only the widgets in one row, or the column= argument to select only the widgets in one column.


