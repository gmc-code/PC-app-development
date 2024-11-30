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

    button_1 = tk.Button(root, text="Button 1", fg="blue", bg="red")

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

.. grid:: 2
   :gutter: 0
   :margin: 0
   :padding: 0

   .. grid-item-card::

      initial
      ^^^
      .. image:: images/button_config_initial.png
        :scale: 100%

   .. grid-item-card::

      changed by config
      ^^^
      .. image:: images/button_config.png
        :scale: 100%


|
| The code below uses the config method to change the appearance of the button.

.. code-block:: python

    import tkinter as tk


    root = tk.Tk()
    root.title("pack side")
    root.geometry("250x150")

    button_1 = tk.Button(root, text="Button 1", fg="blue", bg="red")
    button_1.pack()

    button_2 = tk.Button(root, text="Button 2")
    button_2.pack()

    # Function to change the button's appearance
    def change_button():
        button_2.config(fg="green", bg="yellow", font=("Arial", 24))

    # Schedule the change_button function to run after 3000 milliseconds (3 seconds)
    root.after(3000, change_button)

    root.mainloop()


| This code users root.after function to make changes after a specified time after the window is opened.

.. function:: root.after(delay_ms, callback)

   Schedule a callback function to be called after a given time.

   :param delay_ms: The delay in milliseconds before the callback is called.
   :type delay_ms: int
   :param callback: The function to be called after the delay.
   :type callback: function
