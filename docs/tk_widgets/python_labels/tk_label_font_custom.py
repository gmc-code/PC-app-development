import tkinter as tk
from tkinter import font

# Create the main window
window = tk.Tk()
window.title("Label Custom Font")

# Define the custom font
custom_font = font.Font(family="Comic Sans MS", size=20, weight="bold", slant="italic")

# Create a Label widget using the custom font
label = tk.Label(window, text="This is a label widget.", font=custom_font)
label.pack(padx=20, pady=20)

# Run the Tkinter event loop
window.mainloop()
