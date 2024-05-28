import tkinter as tk


# Create the main application window
window = tk.Tk()
window.title("Tkinter hello world - place")
window.geometry("600x400")

# Define widgets
label = tk.Label(window, text="Hello World!")
button = tk.Button(window, text="Quit", command=window.destroy)

# Place widgets using x and y coordinates
label.place(x=250, y=0)
button.place(x=270, y=22)

# Start the main event loop
window.mainloop()
