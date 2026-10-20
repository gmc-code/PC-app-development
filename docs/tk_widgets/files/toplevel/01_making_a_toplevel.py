# tk Toplevel - Making a Toplevel

import tkinter as tk            # Load the tkinter library


def open_window():
    new_window = tk.Toplevel(root)              # 1. Create the extra window
    new_window.title("Second window")           # 2. Title and size
    new_window.geometry("250x150")

    hello_label = tk.Label(new_window, text="Hello from the new window!")   # 3. "new_window"
    hello_label.pack(pady=40)


root = tk.Tk()                  # Make the main window
root.geometry("300x200")
root.title("Main window")

open_button = tk.Button(root, text="Open a new window", command=open_window)
open_button.pack(pady=60)

root.mainloop()                 # Keep the main window open
