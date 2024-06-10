import tkinter as tk


# Create the main application window
window = tk.Tk()
window.title("hello world - place")
window.geometry("300x200")

# Define widgets
label = tk.Label(window, text="Hello World!")
button = tk.Button(window, text="Quit", command=window.destroy)

# Place widgets using x and y coordinates
label.place(x=50, y=20)
button.place(x=70, y=42)

# Start the main event loop
window.mainloop()
