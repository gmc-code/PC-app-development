# tk Button - Making a Button

import tkinter as tk            # Load the tkinter library

root = tk.Tk()                  # Make the window
root.geometry("300x200")        # Window size: 300 wide, 200 high
root.title("My first button")   # Words in the title bar

button = tk.Button(root, text="Click me")   # 1. Create the button
button.pack(pady=20)                        # 2. Place it in the window

root.mainloop()                 # Keep the window open
