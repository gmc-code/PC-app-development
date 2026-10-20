# tk OptionMenu - Making an OptionMenu

import tkinter as tk            # Load the tkinter library

root = tk.Tk()                  # Make the window
root.geometry("300x200")        # Window size: 300 wide, 200 high
root.title("My first OptionMenu")

flavour = tk.StringVar(value="Vanilla")     # 1. Variable with the starting choice

flavour_menu = tk.OptionMenu(root, flavour, "Vanilla", "Chocolate", "Strawberry")   # 2. Create
flavour_menu.pack(pady=20)                  # 3. Place it in the window

root.mainloop()                 # Keep the window open
