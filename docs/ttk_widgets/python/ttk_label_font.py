import tkinter as tk
from tkinter import ttk

# Create the main window
root = tk.Tk()
root.geometry("300x200")  # Set window size
root.title("ttk Label font")  # Set window title

# Create the label widget with options
label = ttk.Label(root, text="themed text", font=("Arial", 24))

# Pack the label into the window
label.pack()

# Run the main event loop
root.mainloop()
