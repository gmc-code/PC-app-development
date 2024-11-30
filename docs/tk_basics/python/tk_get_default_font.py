import tkinter as tk
from tkinter import font

root = tk.Tk()
window.title("Auto Exit Example")
window.withdraw() # method hides the window immediately after it is created.

# Retrieve the default font
default_font = font.nametofont("TkDefaultFont")
print(default_font.actual())
# {'family': 'Segoe UI', 'size': 9, 'weight': 'normal', 'slant': 'roman', 'underline': 0, 'overstrike': 0}

# Function to close the window
def close_window():
    window.destroy()

# Schedule the window to close after given milliseconds
window.after(200, close_window)

# Run the main loop
window.mainloop()
