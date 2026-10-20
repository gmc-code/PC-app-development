# tk PanedWindow - Tasks Q1

import tkinter as tk

root = tk.Tk()
root.geometry("300x200")
root.title("Panes")

panes = tk.PanedWindow(root)
panes.pack(fill="both", expand=True)

left_label = tk.Label(panes, text="Left", bg="yellow")
right_label = tk.Label(panes, text="Right", bg="orange")
panes.add(left_label)
panes.add(right_label)

root.mainloop()
