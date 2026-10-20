# tk Frame - Making a Frame

import tkinter as tk            # Load the tkinter library

root = tk.Tk()                  # Make the window
root.geometry("300x200")        # Window size: 300 wide, 200 high
root.title("My first frame")    # Words in the title bar

box = tk.Frame(root, bg="lightblue", padx=10, pady=10)  # 1. Create the frame
box.pack(pady=20)                                       # 2. Place it in the window

hello_label = tk.Label(box, text="I am inside the frame")   # 3. "box", not "root"
hello_label.pack()

ok_button = tk.Button(box, text="OK")                       # 3. "box", not "root"
ok_button.pack()

root.mainloop()                 # Keep the window open
