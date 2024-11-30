# see https://coolors.co/contrast-checker/cce4ff-0212a2

import tkinter as tk
from tkinter import font

# Create the main window
window = tk.Tk()
window.title("Entry Alphabet Example")
window.geometry("400x300")

# Define the custom font
custom_font = font.Font(family="Comic Sans MS", size=20, weight="normal", slant="roman")

# First Entry widget
entry = tk.Entry(window, font=custom_font, bg="#eff1db", fg="#4B0082", bd=2, relief="sunken", justify="left", width=20)
# ipadx does not put move the left justification, so is omitted.
entry.pack(padx=20, pady=20, ipady=5)


# Run the Tkinter event loop
window.mainloop()
