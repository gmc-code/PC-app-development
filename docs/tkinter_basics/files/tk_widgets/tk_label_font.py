import tkinter as tk

# Create the main window
window = tk.Tk()
window.geometry("300x200")  # Set window size
window.title("Label font")  # Set window title

# Create the label widget with options
label = tk.Label(window, text="label text", font=("Arial", 24))

# Pack the label into the window
label.pack()

# Run the main event loop
window.mainloop()
