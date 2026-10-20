# tk Radiobutton - Making a group of Radiobuttons

import tkinter as tk            # Load the tkinter library

root = tk.Tk()                  # Make the window
root.geometry("300x200")        # Window size: 300 wide, 200 high
root.title("My first radiobuttons")

drink = tk.StringVar(value="Water")     # 1. One shared variable. "Water" is chosen at the start

water_radio = tk.Radiobutton(root, text="Water", variable=drink, value="Water")   # 2. Create
juice_radio = tk.Radiobutton(root, text="Juice", variable=drink, value="Juice")
milk_radio = tk.Radiobutton(root, text="Milk", variable=drink, value="Milk")

water_radio.pack()              # 3. Place them
juice_radio.pack()
milk_radio.pack()

root.mainloop()                 # Keep the window open
