import tkinter as tk


# Create the main application window
root = tk.Tk()
root.title("hello world - place")
root.geometry("300x200")

# Define widgets
label = tk.Label(root, text="Hello World!")
button = tk.Button(root, text="Quit", command=root.destroy)

# Place widgets using x and y coordinates
label.place(x=50, y=20)
button.place(x=70, y=42)

# Start the main event loop
root.mainloop()
