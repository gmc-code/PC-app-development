import tkinter as tk


window = tk.Tk()
window.title("Name and age")
window.geometry('700x380')
window.configure(bg='#FFFFFF')


def place_name_age():
    """
    Takes the name and age and displays 2 sentences with them in it, in the GUI.
    """
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


def setup_gui():
    """
    Sets up the name and age GUI.
    Creates the main window, labels, entry fields, output text field and button.
    """
    #  create widgets
    name_label = tk.Label(window,
                          text="Name",
                          bg='#FFFFFF',
                          fg='#444444',
                          font=("Arial", 30))
    age_label = tk.Label(window,
                         text="Age",
                         bg='#FFFFFF',
                         fg='#444444',
                         font=("Arial", 30))
    name_entry = tk.Entry(window,
                          bg='#e5e5e5',
                          fg='#444444',
                          font=("Arial", 30))
    age_entry = tk.Entry(window,
                         bg='#e5e5e5',
                         fg='#444444',
                         font=("Arial", 30))

    name_age_button = tk.Button(window,
                                text="Name and Age",
                                bg='#FFFFFF',
                                fg='#444444',
                                font=("Arial", 30),
                                command=place_name_age)
    # TExt widget height=2 where height is in text rows.
    name_age_text = tk.Text(window,
                            height=2,
                            width=30,
                            bg='#e5e5e5',
                            fg='#444444',
                            font=("Arial", 30))

    # place widgets on window
    name_label.grid(row=0, column=0, sticky='e', padx=10, pady=10)
    name_entry.grid(row=0, column=1, sticky='w', padx=10, pady=10)

    age_label.grid(row=1, column=0, sticky='e', padx=10, pady=10)
    age_entry.grid(row=1, column=1, sticky='w', padx=10, pady=10)

    name_age_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)
    name_age_text.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

    # Start the main event loop
    window.mainloop()

# Call the setup function
setup_gui()
