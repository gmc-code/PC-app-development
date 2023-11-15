====================================================
tk button
====================================================

| This code creates a simple GUI application using the Tkinter library. 
| It displays a window with a label and a button. When the button is clicked, the text of the label changes. 
| The `mainloop` function starts the main event loop for the window, allowing it to respond to user interactions.


This code creates a simple GUI application using the Tkinter library in Python. It displays a window with a label and a button. When the button is clicked, the text of the label changes. The `mainloop` function starts the main event loop for the window, allowing it to respond to user interactions.


| Step 1: Import the Tkinter library

.. code-block:: python
            
    from tkinter import *

| Step 2: Create a new window

.. code-block:: python
            
    window = Tk()

| Step 3: Set the title of the window

.. code-block:: python
            
    window.title("Button to change label app")

| Step 4: Set the size of the window

.. code-block:: python
            
    window.geometry("350x400")

| Step 5: Create a new label widget and add it to the window

.. code-block:: python
            
    lbl = Label(window, text="Original text")

| Step 6: Position the label in the window using a grid layout

.. code-block:: python
            
    lbl.grid(column=0, row=0)

| Step 7: Define a function that changes the text of the label

.. code-block:: python
            
    def clicked():
        lbl.configure(text="Button changed text!")

| Step 8: Create a new button widget and add it to the window

.. code-block:: python
            
    btn = Button(window, text="Click Me to change text", command=clicked)

| Step 9: Position the button in the window using a grid layout

.. code-block:: python
            
    btn.grid(column=1, row=0)

| Step 10: Start the main event loop for the window
    
.. code-block:: python
            
    window.mainloop()

| Full code:

.. code-block:: python

   # Import all classes, functions, and variables from the Tkinter library
   from tkinter import *

   # Create a new window
   window = Tk()
   # Set the title of the window
   window.title("Button to change label app")
   # Set the size of the window
   window.geometry('350x400')

   # Create a new label widget and add it to the window
   lbl = Label(window, text="Original text")
   # Position the label in the window using a grid layout
   lbl.grid(column=0, row=0)

   # Define a function that changes the text of the label
   def clicked():
       lbl.configure(text="Button changed text!")

   # Create a new button widget and add it to the window
   btn = Button(window, text="Click Me to change text", command=clicked)
   # Position the button in the window using a grid layout
   btn.grid(column=1, row=0)

   # Start the main event loop for the window
   window.mainloop()

