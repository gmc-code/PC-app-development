import tkinter as tk

# Create the main application window
root = tk.Tk()
root.title("Resizable Window - Min Max Example")

# Set the minimum size (width, height)
root.minsize(200, 100)
# Set the maximum size (width, height)
root.maxsize(500, 500)

# Start the main event loop
root.mainloop()
