import tkinter as tk
from tkinter import ttk

# Create the tkinter window
window = tk.Tk()
window.title('ttk button')
window.geometry("800x400")
window.resizable(True, True)

# Set the theme to 'alt'
style = ttk.Style()
style.theme_use('alt')

# Configure the TButton style
style.configure('TButton', font=('Helvetica', 36), background='red', foreground='white', width=20, borderwidth=1, focusthickness=3, focuscolor='none')

# Create a ttk Button
button = ttk.Button(window, text='Custom Button')
button.place(x=100, y=100)  # Adjust the position as needed

# Start the tkinter event loop
window.mainloop()
