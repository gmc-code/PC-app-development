====================================================
tk geometry cost calculator
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

| grid is not responsive to window size changes.
| For grid, empty rows or columns are not allocated screen space.

----

grid
----------

| grid is not responsive to window size changes.
| For grid, empty rows or columns are not allocated screen space.
| Grid determines how much space a widget can occupy, not how much it does occupy.
| By default, widgets are placed in the middle of a grid cell.

Use the columnconfigure() and rowconfigure() methods to specify the weight of a column and a row of a grid.
Use grid() method to position a widget on a grid.
Use sticky option to align the position of the widget on a cell and define how the widget will be stretched.
Use ipadx, ipady and padx, pady to add internal and external paddings.

.. py:function:: widget.columnconfigure(column, option=value, ...)

    | configure the column properties of a widget container, typically a `Frame` or `Grid`. 
    | specify options such as minimum size, weight, and stretching behavior for the column within the container.


    - `widget`: The widget container (e.g., `Frame`, `Grid`) for which you want to configure the columns.
    - `column`: The index of the column you want to configure. Columns are indexed starting from 0.
    - `option=value`: Options you can specify for configuring the column. These options can include:
    - `minsize`: Specifies the minimum size of the column.
    - `weight`: Determines how much any extra space is distributed among columns. Columns with higher weights will get more space.
    - `uniform`: If set to a string value, columns with the same value will be of the same size.
    - `pad`: Specifies padding to add around the column.




