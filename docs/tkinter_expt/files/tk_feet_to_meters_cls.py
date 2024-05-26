from tkinter import *
from tkinter import ttk

class FeetToMeters:
    """
    A class to convert feet to meters using a simple GUI.
    """

    def __init__(self, window):
        """
        Initialize the class with a window window.
        """
        self.window = window
        self.setup_ui()

    def setup_ui(self):
        """
        Set up the user interface for the application.
        """
        # Set the title of the window
        self.window.title("Feet to Meters")

        # Create a frame within the window
        mainframe = ttk.Frame(self.window, padding="3 3 12 12")
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        self.window.columnconfigure(0, weight=1)
        self.window.rowconfigure(0, weight=1)

        # Create a StringVar for feet input
        self.feet = StringVar()
        self.feet_entry = ttk.Entry(mainframe, width=7, textvariable=self.feet)
        self.feet_entry.grid(column=2, row=1, sticky=(W, E))

        # Create a StringVar for meters output
        self.meters = StringVar()

        # Create a label to display the meters output
        ttk.Label(mainframe, textvariable=self.meters).grid(
            column=2, row=2, sticky=(W, E)
        )

        # Create a button to calculate the conversion
        ttk.Button(mainframe, text="Calculate", command=self.set_meters).grid(
            column=3, row=3, sticky=W
        )

        # Create labels for the input and output
        ttk.Label(mainframe, text="feet").grid(column=3, row=1, sticky=W)
        ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)
        ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky=W)

        # Configure grid padding for all children of mainframe
        for child in mainframe.winfo_children():
            child.grid_configure(padx=5, pady=5)

        # Set focus to the feet entry field
        self.feet_entry.focus()
        self.window.bind("<Return>", self.set_meters)

    def calculate(self, feet):
        """
        Convert feet to meters.

        Parameters:
        feet (str): The number of feet to convert to meters.

        Returns:
        float: The equivalent number of meters rounded to 2 decimal places.
        """
        try:
            # Convert feet to meters and round to 2 decimal places
            meters = round(0.3048 * feet, 2)
            return meters
        except ValueError:
            pass

    def set_meters(self, *args):
        """
        Set the meters StringVar with the calculated meters from the feet StringVar.
        Then set the focus back to the feet_entry field.
        """
        self.meters.set(self.calculate(float(self.feet.get())))
        self.feet_entry.focus()


# Create a Tk window widget
window = Tk()

# Create an instance of the FeetToMeters class
FeetToMeters(window)

# Start the Tk event loop
window.mainloop()
