import tkinter as tk
import re

def validate_email(event):
    # Get the current value of the entry widget
    email = entry.get()
    # Define the regex pattern for a valid email address
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if re.match(pattern, email) or email == "":
        error_label.config(text="")  # Clear the error message
    else:
        error_label.config(text="Invalid email address")  # Display the error message

root = tk.Tk()
root.title("Email Validation Example")
root.geometry("500x300")  # Set window size

entry = tk.Entry(root, font=("Arial",24))
entry.pack(pady=10)

# Bind the Leave event to the validate_email function
entry.bind("<Leave>", validate_email)

# Create a label to display error messages
error_label = tk.Label(root, text="", fg="red")
error_label.pack()

root.mainloop()
