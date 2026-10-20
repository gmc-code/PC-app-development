# tk Label - Making a Label

import tkinter as tk            # Load the tkinter library

root = tk.Tk()                  # Make the window
root.geometry("300x200")        # Window size: 300 wide, 200 high
root.title("My first label")    # Words in the title bar

label = tk.Label(root, text="Hello, world!")   # 1. Create the label
label.pack()                                    # 2. Place it in the window

root.mainloop()                 # Keep the window open
