import tkinter as tk
from tkinter import messagebox

def show_info_message():
    window = tk.Tk()
    window.withdraw()  # Hide the main window

    # Show an information message box at position (x, y)
    x, y = 100, 100
    messagebox.showinfo("Login", "Logged in successfully!", icon=messagebox.INFO, parent=window)
    window.destroy()  # Close the hidden main window

# Call the function to display the message box
show_info_message()
