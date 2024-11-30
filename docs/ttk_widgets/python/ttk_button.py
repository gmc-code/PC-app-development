import tkinter as tk
from tkinter import ttk

# Create the tkinter window
root = tk.Tk()
root.title('ttk button')
root.geometry("800x400")
root.resizable(True, True)

# Set the theme to 'alt'
style = ttk.Style()
style.theme_use('alt')

# Configure the TButton style
style.configure('TButton', font=('Helvetica', 36), background='red', foreground='white', width=20, borderwidth=1, focusthickness=3, focuscolor='none')

# Create a ttk Button
button = ttk.Button(root, text='Custom Button')
button.place(x=100, y=100)  # Adjust the position as needed

# Start the tkinter event loop
root.mainloop()
