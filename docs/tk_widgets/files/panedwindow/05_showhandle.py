# tk PanedWindow - showhandle

import tkinter as tk

root = tk.Tk()
root.geometry("300x200")
root.title("showhandle")

panes = tk.PanedWindow(root, showhandle=True, sashwidth=6)
panes.pack(fill="both", expand=True)

panes.add(tk.Label(panes, text="Left", bg="lightblue"))
panes.add(tk.Label(panes, text="Right", bg="lightgreen"))

root.mainloop()
