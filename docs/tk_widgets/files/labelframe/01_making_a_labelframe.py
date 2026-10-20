# tk LabelFrame - Making a LabelFrame

import tkinter as tk            # Load the tkinter library

root = tk.Tk()                  # Make the window
root.geometry("300x200")        # Window size: 300 wide, 200 high
root.title("My first LabelFrame")

details = tk.LabelFrame(root, text="Your details", padx=10, pady=10)  # 1. Create it
details.pack(pady=20)                                                 # 2. Place it

name_label = tk.Label(details, text="Name:")        # 3. "details", not "root"
name_label.pack()

name_entry = tk.Entry(details)                      # 3. "details", not "root"
name_entry.pack()

root.mainloop()                 # Keep the window open
