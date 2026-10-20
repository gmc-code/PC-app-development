# tk Checkbutton - Making a Checkbutton

import tkinter as tk            # Load the tkinter library

root = tk.Tk()                  # Make the window
root.geometry("300x200")        # Window size: 300 wide, 200 high
root.title("My first checkbutton")

cheese = tk.IntVar()            # 1. Variable: 1 = ticked, 0 = not ticked

cheese_check = tk.Checkbutton(root, text="Cheese", variable=cheese)   # 2. Create it
cheese_check.pack(pady=20)      # 3. Place it in the window

root.mainloop()                 # Keep the window open
