====================================================
tk geometry
====================================================

| The grid geometry manager allows you to arrange widgets within a window.
| See: https://tkdocs.com/tutorial/grid.html
| See: https://www.geeksforgeeks.org/python-pack-method-in-tkinter/?ref=lbp

| Pack: see https://www.youtube.com/watch?v=rbW1iJO1psk
| Pack with frames: https://www.youtube.com/watch?v=SsjEAWT-SMc
| place: see https://www.youtube.com/watch?v=bx0YmWFfsEI

| grid: see https://www.youtube.com/watch?v=IJ-iVnN09-8
| grid: see https://www.pythontutorial.net/tkinter/tkinter-grid/

----

geometry notes
--------------------

| pack is responsive to window size changes.

| place is not responsive to window size changes.
| Place uses absolute positioning. 

----

grid
----------

.. py:function:: widget.grid(row=index_r, column=index_c)

    | Use **grid()** method to position a widget on a grid at row index_r and column index_c.
    e.g grid(row=0, column=0)


Options
----------


| Place widgets in a row and column.
| Specify multiple rows and columns for widget.
| Specify cell alignment. Use the **sticky** option to align the position of the widget on a cell and define how the widget will be stretched.
| Specify padding. Use **ipadx**, **ipady** and **padx**, **pady** to add internal and external paddings.

.. py:function:: widget.grid(row=index_r, column=index_c, rowspan=n)

    | Specify number of rows, **n**, for a widget to span across
    | e.g. rowspan=2 to span the widget across 2 rows.

.. py:function:: widget.grid(row=index_r, column=index_c, columnspan=n)

    | Specify number of columns, **n**, for a widget to span across
    | e.g. columnspan=2 to span the widget across 2 columns.

.. py:function:: padx=pixels

    | Add horizontal padding on both sides of the widget.
    | e.g. padx=10 to add 10 pixels of space on the left and on the right of the widget.

.. py:function:: pady=pixels

    | Add vertical padding above and below the widget.
    | e.g. pady=10 to add 10 pixels of space above and below the widget.


.. py:function:: ipadx=pixels

    | Add horizontal internal padding on both sides of the widget.
    | e.g. ipadx=10 to grow the widget to the left and right, by 10 pixels each.

.. py:function:: ipady=pixels

    | Add vertical internal padding  above and below the widget.
    | e.g. ipady=10 to grow the widget by 10 pixels above and below the widget.


----

notes
------

| For grid, empty rows or columns are not allocated screen space.
| Grid determines how much space a widget can occupy, not how much it does occupy.
| By default, widgets are placed in the middle of a grid cell.

----

columnconfigure and rowconfigure
----------------------------------------

| Use the columnconfigure() and rowconfigure() methods to specify the weight of a column and a row of a grid.
| The allows widgets to stretch in size when the window is resized.
| Set the number of rows and columns.
| Set width and height of each row and column.

.. py:function:: widget.columnconfigure(column, option=value, ...)

    | configure the column properties of a widget container, typically a `Frame` or `Grid`. 
    | specify options such as minimum size, weight, and stretching behavior for the column within the container.

    - `widget`: The widget container (e.g., `Frame`, `Grid`) for which to configure the columns.
    - `column`: The index of the column to configure, starting from 0. Use a tuple such as (0, 1, 2) for several columns.
    - `option=value`: Options you can specify for configuring the column. These options can include:
    - `minsize`: Specifies the minimum size of the column.
    - `weight`: Resizes column on window resizing. Determines how much any extra space is distributed among columns. Columns with higher weights will get more space.
    - `uniform`: If set to a string value, columns with the same value will be of the same size.
    - `pad`: Specifies padding to add around the column.

.. py:function:: widget.rowconfigure(row, option=value, ...)

    | configure the row properties of a widget container, typically a `Frame` or `Grid`. 
    | specify options such as minimum size, weight, and stretching behavior for the row within the container.



