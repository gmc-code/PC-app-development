import tkinter as tk
from tkinter import ttk

# Create the main window
root = tk.Tk()
root.geometry("300x200")  # Set window size
root.title("ttk Label text")  # Set window title

# Create the themed label widget
label = ttk.Label(root, text="themed label text")

# Pack the label into the window
label.pack()

# Run the main event loop
root.mainloop()