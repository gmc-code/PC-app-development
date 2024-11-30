import tkinter as tk

# Create the main window
window = tk.Tk()
window.geometry("500x300")  # Set window size
window.title("Entry Example")  # Set window title

# Create the entry widget for input
name_entry = tk.Entry(window, font=('calibre', 24, 'normal'), width=20)
name_entry.pack(pady=20)  # Add some padding to the top

# Run the main event loop
window.mainloop()
