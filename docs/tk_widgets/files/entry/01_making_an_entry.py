# tk Entry - Making an Entry

import tkinter as tk            # Load the tkinter library

root = tk.Tk()                  # Make the window
root.geometry("300x200")        # Window size: 300 wide, 200 high
root.title("My first entry")    # Words in the title bar

entry = tk.Entry(root)          # 1. Create the entry
entry.pack(pady=20)             # 2. Place it in the window, 20 pixels from the top

root.mainloop()                 # Keep the window open
