# Import all classes, functions, and variables from the Tkinter library
from tkinter import *

# Create a new window
window = Tk()
# Set the title of the window
window.title("Button to change text label")
# Set the size of the window
window.geometry("350x400")

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
btn.grid(column=0, row=1)

# Start the main event loop for the window
window.mainloop()
