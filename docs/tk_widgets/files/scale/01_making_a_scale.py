# tk Scale - Making a Scale

import tkinter as tk            # Load the tkinter library

root = tk.Tk()                  # Make the window
root.geometry("300x200")        # Window size: 300 wide, 200 high
root.title("My first scale")    # Words in the title bar

volume_scale = tk.Scale(root, from_=0, to=100)  # 1. Create the scale
volume_scale.pack()                             # 2. Place it in the window

root.mainloop()                 # Keep the window open
