import tkinter as tk

# Create the main window
root = tk.Tk()
root.geometry("500x300")  # Set window size
root.title("Entry Example")  # Set window title

# Create the entry widget for input
name_entry = tk.Entry(root, font=('calibre', 24, 'normal'), width=20)
name_entry.pack(pady=20)  # Add some padding to the top

# Insert text into the Entry widget
name_entry.insert(0, "type name here ...")
# Automatically remove focus from Entry
root.focus_set()

# Run the main event loop
root.mainloop()
