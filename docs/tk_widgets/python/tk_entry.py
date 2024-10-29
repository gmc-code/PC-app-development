import tkinter as tk

# Create the main window
window = tk.Tk()
window.geometry("600x200")  # Set window size
window.title("Entry font")  # Set window title

# Create the entry widget with options
entry = tk.Entry(window, font=("calibri", 32), fg="blue", bg="lightyellow",
                 relief="solid", borderwidth=1)

# Pack the label into the window
entry.pack()

# Run the main event loop
window.mainloop()
