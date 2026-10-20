# tk PanedWindow - Making a PanedWindow

import tkinter as tk            # Load the tkinter library

root = tk.Tk()                  # Make the window
root.geometry("300x200")        # Window size: 300 wide, 200 high
root.title("My first PanedWindow")

panes = tk.PanedWindow(root)                    # 1. Create the PanedWindow
panes.pack(fill="both", expand=True)            #    and fill the window

left_label = tk.Label(panes, text="Left", bg="lightblue")      # 2. Create the widgets
right_label = tk.Label(panes, text="Right", bg="lightgreen")

panes.add(left_label)                           # 3. Add them as panes
panes.add(right_label)

root.mainloop()                 # Keep the window open
