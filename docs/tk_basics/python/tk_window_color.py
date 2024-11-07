import tkinter as tk

# Create the main window
root = tk.Tk()

# Set window options
root.configure(highlightbackground='red', highlightcolor='green', highlightthickness=5)

# Create a label
label = tk.Label(root, text="Hello, Tkinter!")
label.pack(padx=10, pady=10)

# Create a button
button = tk.Button(root, text="Click Me")
button.pack(padx=10, pady=10)

# Ensure the window can take focus
# root.focus_set()

# Run the application
root.mainloop()
