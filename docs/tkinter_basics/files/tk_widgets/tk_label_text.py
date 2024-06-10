import tkinter as tk

# Create the main window
window = tk.Tk()
window.geometry("300x200")  # Set window size
window.title("Label text")  # Set window title

# Create the label widget
label = tk.Label(window, text="label text")

# Pack the label into the window
label.pack()

# Run the main event loop
window.mainloop()
