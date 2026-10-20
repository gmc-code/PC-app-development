# tk Scrollbar - Making a Scrollbar

import tkinter as tk            # Load the tkinter library

root = tk.Tk()                  # Make the window
root.geometry("300x200")        # Window size: 300 wide, 200 high
root.title("My first scrollbar")

scrollbar = tk.Scrollbar(root)                      # 1. Create the scrollbar
scrollbar.pack(side="right", fill="y")              #    down the right side

number_list = tk.Listbox(root, yscrollcommand=scrollbar.set)    # 2. Widget -> scrollbar
number_list.pack(side="left", fill="both", expand=True)

scrollbar.config(command=number_list.yview)         # 3. Scrollbar -> widget

for number in range(1, 101):
    number_list.insert(tk.END, f"Item {number}")

root.mainloop()                 # Keep the window open
