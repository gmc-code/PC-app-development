import tkinter as tk
from tkinter import font

# Create the main window
root = tk.Tk()
root.title("Entry Example")
root.geometry("400x300")

# Define the custom font
custom_font = font.Font(family="Comic Sans MS", size=20, weight="normal", slant="roman")

# First Entry widget
entry = tk.Entry(root, font=custom_font, bg="#fafafa", fg="#2f2f2f", bd=2, relief="sunken", justify="left", width=20)
# ipadx does not put move the left justification, so is omitted.
entry.pack(padx=20, pady=20, ipady=5)

# Insert text into the Entry widget
entry.insert(0, "AbCdEf 123456")
# Automatically remove focus from Entry
root.focus_set()


# Run the Tkinter event loop
root.mainloop()
