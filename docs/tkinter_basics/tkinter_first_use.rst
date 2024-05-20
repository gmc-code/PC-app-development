====================================================
tkinter first use
====================================================


| Below is a sample Hello World app. 

.. code-block:: python

    import tkinter as tk


    # Create the main application window
    window = tk.Tk()
    window.title("Tkinter hello world")
    window.geometry('600x400')

    # define widgets
    label = tk.Label(window, text="Hello World!")
    button = tk.Button(window, text="Quit", command=window.destroy)

    # place widgets
    label.grid(row=0, column=0)
    button.grid(row=0, column=0)

    # Start the main event loop
    window.mainloop()

----

Code details
---------------

| Overall, this code creates a simple **Tkinter** application with a window, a label displaying "Hello World!", and a button that allows the user to quit the application.

| ``import tkinter as tk``: imports the **Tkinter** library and assigns it an alias (``tk``). By doing this, you can use the ``tk`` prefix to access various **Tkinter** classes and functions throughout your code.

| ``window = tk.Tk()``: Here, a new **Tkinter** application window is created. The ``Tk()`` constructor initializes the main application window. 
| You can customize this window by setting properties such as its title, size, and other attributes.

| ``window.title("Tkinter hello world")``: sets the title of the application window to "Tkinter hello world". 
| You can replace this string with any other title you'd like for your application.

| ``window.geometry('600x400')``: The ``geometry()`` method defines the initial size of the window. 
| In this case, the window will be 600 pixels wide and 400 pixels tall.

| ``label = tk.Label(window, text="Hello World!")``: A label widget is created with the text "Hello World!". 
| Labels are used to display static text or messages in the GUI. The ``label`` variable holds a reference to this widget.

| ``button = tk.Button(window, text="Quit", command=window.destroy)``: A button widget is created with the label "Quit". 
| When this button is clicked, the ``window.destroy()`` method is called, which closes the application window. 
| The ``button`` variable holds a reference to this widget.

| ``label.grid(column=0, row=0)``: The ``grid()`` method is used to place the ``label`` widget in the first row (row 0) and first column (column 0) of the window's grid layout. 
| You can adjust the row and column indices to position widgets as needed.

| ``button.grid(column=1, row=0)``: Similarly, the ``button`` widget is placed in the first row (row 0) and second column (column 1) of the grid layout.

| ``window.mainloop()``: starts the main event loop, which keeps the application running and responsive.
| It listens for user interactions (such as button clicks) and updates the GUI accordingly.

