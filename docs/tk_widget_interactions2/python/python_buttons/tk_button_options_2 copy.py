import tkinter as tk


# Create a new window
root = tk.Tk()
# Set the title of the window
root.title("Button formatting")
# Set the size of the window
root.geometry("350x400")

def button_clicked():
    print("Button clicked!")


# Creating a button with specified options
# Create a new button widget and add it to the window
button = tk.Button(root,
                # Set the text displayed on the button
                text="Click Me",
                # Set the function to be called when the button is clicked
                command=button_clicked,
                # Set the background color when the button is active (clicked)
                activebackground="blue",
                # Set the text color when the button is active (clicked)
                activeforeground="white",
                # Set the alignment of the text within the button
                anchor="center",
                # Set the border width of the button
                bd=3,
                # Set the background color of the button
                bg="lightgray",
                # Set the cursor that appears when hovering over the button
                cursor="hand2",
                # Set the text color when the button is disabled
                disabledforeground="gray",
                # Set the text color of the button
                fg="black",
                # Set the font of the button text
                font=("Arial", 14),
                # Set the height of the button
                height=2,
                # Set the color of the button's highlight border
                highlightbackground="black",
                # Set the color of the highlight when the button is focused
                highlightcolor="red",
                # Set the thickness of the highlight border
                highlightthickness=2,
                # Set the justification of the text within the button
                justify="center",
                # Set the relief style of the button when it is pressed
                overrelief="raised",
                # Set the padding around the text inside the button (horizontal)
                padx=10,
                # Set the padding around the text inside the button (vertical)
                pady=5,
                # Set the width of the button
                width=15,
                # Set the maximum line length for the text before wrapping
                wraplength=50)


button.pack(padx=20, pady=20)

root.mainloop()
