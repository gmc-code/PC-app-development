# ttk PanedWindow - Making a ttk PanedWindow

import tkinter as tk            # Load tkinter
from tkinter import ttk         # Load the themed widgets

root = tk.Tk()                  # Make the window
root.geometry("300x200")
root.title("My first ttk PanedWindow")

panes = ttk.PanedWindow(root, orient="horizontal")     # 1. Create the PanedWindow
panes.pack(fill="both", expand=True)                   #    and fill the window

left_box = tk.Listbox(panes)                           # 2. Widgets for each pane
left_box.insert(tk.END, "Drag the line")
right_box = tk.Text(panes)
right_box.insert("1.0", "between the panes")

panes.add(left_box)                                    # 3. Add them as panes
panes.add(right_box)

root.mainloop()                 # Keep the window open
