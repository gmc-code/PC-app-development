# tk Spinbox - Making a Spinbox

import tkinter as tk            # Load the tkinter library

root = tk.Tk()                  # Make the window
root.geometry("300x200")        # Window size: 300 wide, 200 high
root.title("My first spinbox")  # Words in the title bar

tickets_spinbox = tk.Spinbox(root, from_=1, to=10)  # 1. Create the spinbox
tickets_spinbox.pack(pady=20)                       # 2. Place it in the window

root.mainloop()                 # Keep the window open
