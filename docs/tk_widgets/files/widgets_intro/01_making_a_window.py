# Tkinter widgets - Making a window

import tkinter as tk            # Load the tkinter library and call it "tk"

root = tk.Tk()                  # Make the main window, called "root"
root.geometry("300x200")        # Window size: 300 pixels wide, 200 pixels high
root.title("My app")            # Words in the title bar

# Widgets go here

root.mainloop()                 # Keep the window open until the user closes it
