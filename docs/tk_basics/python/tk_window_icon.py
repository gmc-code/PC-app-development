import tkinter as tk

# Create the main window
root = tk.Tk()

# Set the title of the window
root.title("PC Tkinter Window")

# Set the size of the window
root.geometry("300x100")

# Set the window icon using a raw string
root.iconbitmap(r'docs/tk_basics/images/favicon.ico')

# Add a label to the window
label = tk.Label(root, text="Hello, PC Tkinter!")
label.pack(pady=20)

# Start the Tkinter event loop
root.mainloop()
