====================================================
tk geometry place
====================================================

| The place geometry manager allows you to arrange widgets within a window using absolute positions.
| place: see https://www.youtube.com/watch?v=bx0YmWFfsEI
| Layouts: https://www.youtube.com/watch?v=i577cFu8eBI&list=PLpMixYKO4EXflJFPhTvZOVAbs7lBdEBSa

----

place
--------------------

| place is not responsive to window size changes.
| Place uses absolute positioning. 

.. py:function:: widget.place(x=x_coord, y=y_coord)

    | Use **place()** method to place a widget with its top left at the x and y coordinates..
    | e.g. widget.place(x=50, y=100)


.. code-block:: python

    import tkinter as tk

    # window
    window=tk.Tk()
    window.title('Layout intro')
    window.geometry('600x400')

    # widgets 
    label1=tk.Label(window, text='Label 1', background='red')
    label2=tk.Label(window, text='Label 2', background='green')

    # place
    label1.place(x=100 , y=100, width=200, height=100)
    label2.place(x=200 , y=200, width=200, height=100)

    # run
    window.mainloop()


options
--------------

See: https://www.pythontutorial.net/tkinter/tkinter-place/
