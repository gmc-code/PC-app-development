import tkinter as tk

# Create the main application window
window = tk.Tk()
window.title("Resizable Window - Min Max Example")

# Set the minimum size (width, height)
window.minsize(200, 100)
# Set the maximum size (width, height)
window.maxsize(500, 500)

# Start the main event loop
window.mainloop()
