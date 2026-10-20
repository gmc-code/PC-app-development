import tkinter as tk

# Create the main window
root = tk.Tk()
root.geometry("300x200")  # Set window size
root.title("Label font")  # Set window title

# Create the label widget with options
label = tk.Label(root, text="label text", font=("Arial", 24))

# Pack the label into the window
label.pack()

# Run the main event loop
root.mainloop()
