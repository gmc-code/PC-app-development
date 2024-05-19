from tkinter import *
from tkinter import ttk


def calculate(feet):
    """
    Convert feet to meters.

    Parameters:
    feet (str): The number of feet to convert to meters.

    Returns:
    float: The equivalent number of meters rounded to 2 decimal places.
    """
    try:
        # feet = float(feet)
        # return round(0.3048 * feet, 2)
        return 0.3048 * feet
    except ValueError:
        pass




def set_meters():
    """
    Set the meters DoubleVar with the calculated meters from the feet DoubleVar.
    Then set the focus back to the feet_entry field.
    """
    meters_value = calculate(feet.get())
    meters.set(meters_value)
    meters_formatted = f"{meters_value:.2f}"
    ttk.Label(mainframe, text=meters_formatted).grid(column=2, row=2, sticky=(W, E))
    feet_entry.focus()


# Create the main window
root = Tk()
root.title("Feet to Meters")

# Create the main frame
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# Create the feet DoubleVar and entry field
feet = DoubleVar()
feet_entry = ttk.Entry(mainframe, width=7, textvariable=feet)
feet_entry.grid(column=2, row=1, sticky=(W, E))

# Create the meters DoubleVar and label
meters = DoubleVar()
ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=(W, E))

# Create the calculate button
ttk.Button(mainframe, text="Calculate", command=set_meters).grid(
    column=3, row=3, sticky=W
)

# Create the labels
ttk.Label(mainframe, text="feet").grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)
ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky=W)

# Configure the padding for all child widgets of mainframe
for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

# Set the initial focus to the feet_entry field
feet_entry.focus()

# Bind the return key to the set_meters function
root.bind("<Return>", lambda _: set_meters())

# Start the main event loop
root.mainloop()
