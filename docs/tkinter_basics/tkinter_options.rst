====================================================
tkinter options
====================================================

Setting Options
----------------------------------------

| Options control things like the color and border width of a widget.
| Options can be set in three ways:

At object creation time
-------------------------

| At object creation time, using keyword arguments

.. code-block:: python

    button_1 = tk.Button(window, text="Button 1", fg="blue", bg="red")

After object creation
-------------------------

| After object creation, treating the option name like a dictionary index
.. code-block:: python

    button_1["fg"] = "red"
    button_1["bg"] = "blue"

| Use the config() method to update multiple attributes subsequent to object creation

.. code-block:: python

    button_1.config(fg="green", bg="yellow", font=("Arial", 24))

----

Example code
---------------

.. code-block:: python

    import tkinter as tk


    window = tk.Tk()
    window.title("pack side")
    window.geometry("250x150")

    button_1 = tk.Button(window, text="Button 1", fg="blue", bg="red")
    button_1.pack()

    button_2 = tk.Button(window, text="Button 2")
    button_2.pack()

    # Function to change the button's appearance
    def change_button():
        button_2.config(fg="green", bg="yellow", font=("Arial", 24))

    # Schedule the change_button function to run after 3000 milliseconds (3 seconds)
    window.after(3000, change_button)

    window.mainloop()


| This code users window.after function to make changes after a specified time after the window is opened.

.. function:: window.after(delay_ms, callback)

   Schedule a callback function to be called after a given time.

   :param delay_ms: The delay in milliseconds before the callback is called.
   :type delay_ms: int
   :param callback: The function to be called after the delay.
   :type callback: function
