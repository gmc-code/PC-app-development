import tkinter as tk
from tkinter import font

# Create the main window
root = tk.Tk()
root.title("Formatted Label Example")
root.geometry("500x300")

# Define the custom font
custom_font = font.Font(family="Comic Sans MS", size=20, weight="bold", slant="italic")

# Create the Label widget with the specified formatting, border, padding, and anchor options
label = tk.Label(root, text="This is a label widget.", font=custom_font, bg="#e0b0ff", fg="purple",
                 bd=2, relief="raised", padx=10, pady=10, anchor="nw", width=300, height=2)
label.pack(padx=20, pady=20)

# Run the Tkinter event loop
root.mainloop()
