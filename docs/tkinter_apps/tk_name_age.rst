====================================================
tk name age
====================================================

.. image:: images/tk_name_age.png
    :scale: 100%

| This code outputs the user name and age in sentence form once the user has input their name and age.    
| This code creates a simple GUI application using the Tkinter library. 
| It displays a window with Label, Entry, Text and Button widgets
| The `mainloop` function starts the main event loop for the window, allowing it to respond to user interactions.

----

grid
-------

| The grid rows and columns both start at 0.

| The sticky='e' option specifies that the widget should stick to the east (right) side of its grid cell. 
| This means that if the cell is larger than the widget, the widget will be right-aligned within the cell.

| The padx=10 option adds 10 pixels of padding on the left and right (horizontal) sides of the widget.
| The pady=10 option adds 10 pixels of padding on the top and bottom (vertical) sides of the widget.


----

place_name_age
---------------

| `name = name_entry.get()` uses the get() method to get the text value of the Entry widget.

| Default values of "John Smith" and "16" are used if no name or age is entered.

| The delete method of a Text widget requires the line.column as the first argument. e.g. `1.0` in `name_age_text.delete(1.0, 'end')`
| `tk.END` or `'end'` can be used as the second argument to cause the deletion to go to the end of the widget.
| The insert method of a Text widget requires the line.column as the first argument. e.g. `1.0` in `name_age_text.insert(1.0, 'new text')`

| `f'My name is {name}. \nI am {age} years old.'` uses `\n` for a line break so the 2 sentences are on two lines.

----

Full code
------------

.. code-block:: python

    import tkinter as tk


    window = tk.Tk()
    window.title("Name and age")
    window.geometry('700x380')
    window.configure(bg='#FFFFFF')


    def place_name_age():
        # get name
        name = name_entry.get()
        if name == "":
            name = "John Smith"
        # get age
        age = age_entry.get()
        if age == "":
            age = "16"
        # clear name_age_text 1.0 represents line.column or line 1 character 0, tk.END or 'end' can be used.
        name_age_text.delete(1.0, 'end')
        # insert name age using f string, \n is a line break; 
        name_age_text.insert(1.0, f'My name is {name}. \nI am {age} years old.')
        
        
    #  create widgets
    name_label = tk.Label(window, text="Name",
                                bg='#FFFFFF', fg='#444444', font=("Arial", 30))
    age_label = tk.Label(window, text="Age",
                                bg='#FFFFFF', fg='#444444', font=("Arial", 30))
    name_entry = tk.Entry(window, bg='#e5e5e5', fg='#444444', font=("Arial", 30))
    age_entry = tk.Entry(window, bg='#e5e5e5', fg='#444444', font=("Arial", 30))

    name_age_button =tk.Button(window, text="Name and Age",
                                bg='#FFFFFF', fg='#444444', font=("Arial", 30), command=place_name_age)
    # TExt widget height=2 where height is in text rows.
    name_age_text = tk.Text(window, height=2, width=30, bg='#e5e5e5', fg='#444444', font=("Arial", 30))


    # place widgets on window
    name_label.grid(row=0, column=0, sticky='e', padx=10, pady=10)
    name_entry.grid(row=0, column=1, sticky='w', padx=10, pady=10)

    age_label.grid(row=1, column=0, sticky='e', padx=10, pady=10)
    age_entry.grid(row=1, column=1, sticky='w', padx=10, pady=10)

    name_age_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)
    name_age_text.grid(row=3, column=0, columnspan=2, padx=10, pady=10)


    # Start the main event loop
    window.mainloop()
