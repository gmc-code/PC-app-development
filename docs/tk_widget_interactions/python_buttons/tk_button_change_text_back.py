# Import all classes, functions, and variables from the Tkinter library
from tkinter import *

# Create a new window
root = Tk()
# Set the title of the window
root.title("Button to change text label back")
# Set the size of the window
root.geometry("350x400")

# Create a new label widget and add it to the window
lbl = Label(root, text="Original text")
# Position the label in the window using a grid layout
lbl.grid(column=0, row=0)

# Initialize a flag to keep track of the label's state
is_original = True

# Define a function that changes the text of the label
def clicked():
    global is_original
    if is_original:
        lbl.configure(text="Button changed text!")
    else:
        lbl.configure(text="Original text")
    is_original = not is_original

# Create a new button widget and add it to the window
btn = Button(root, text="Click Me to change text", command=clicked)
# Position the button in the window using a grid layout
btn.grid(column=0, row=1)

# Start the main event loop for the window
root.mainloop()
