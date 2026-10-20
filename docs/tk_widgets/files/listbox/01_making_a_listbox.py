# tk Listbox - Making a Listbox

import tkinter as tk            # Load the tkinter library

root = tk.Tk()                  # Make the window
root.geometry("300x250")        # Window size: 300 wide, 250 high
root.title("My first listbox")  # Words in the title bar

fruit_list = tk.Listbox(root)           # 1. Create the listbox

fruit_list.insert(tk.END, "Apple")      # 2. Add items
fruit_list.insert(tk.END, "Banana")
fruit_list.insert(tk.END, "Cherry")

fruit_list.pack(pady=10)                # 3. Place it in the window

root.mainloop()                 # Keep the window open
