import tkinter as tk

# Create the main window
window = tk.Tk()
window.geometry("400x400")  # Set window size
window.title("Label Testing")  # Set window title

# Create the label widget with options
label = tk.Label(window, text="label text", fg="blue", bg="lightyellow", font=(
    "Arial", 24, "bold"), justify="center", padx=100, pady=20, relief="solid", borderwidth=1)

# Pack the label into the window
label.pack(padx=20, pady=20)  # Add some padding to the top and side

# Run the main event loop
window.mainloop()
