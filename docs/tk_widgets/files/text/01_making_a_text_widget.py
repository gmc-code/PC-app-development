# tk Text - Making a Text widget

import tkinter as tk            # Load the tkinter library

root = tk.Tk()                  # Make the window
root.geometry("300x200")        # Window size: 300 wide, 200 high
root.title("My first Text")     # Words in the title bar

text_box = tk.Text(root, width=30, height=6)    # 1. Create the box
text_box.pack(pady=10)                          # 2. Place it in the window

root.mainloop()                 # Keep the window open
