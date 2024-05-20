====================================================
tk entry
====================================================

| See: https://www.geeksforgeeks.org/python-tkinter-entry-widget/?ref=lbp


.. code-block:: python

    import tkinter as tk

    # Create the main window
    root = tk.Tk()
    root.geometry("400x250")  # Set window size
    root.title("Welcome to My App")  # Set window title

    # Create a StringVar to associate with the entry
    name_var = tk.StringVar()

    # Create the label widget with all options
    # creating a entry for input
    # name using widget Entry
    name_entry = tk.Entry(root,textvariable = name_var, font=('calibre',10,'normal'))

    # Pack the label into the window
    label.pack(pady=20)  # Add some padding to the top


    # Run the main event loop
    root.mainloop()


root.mainloop()
