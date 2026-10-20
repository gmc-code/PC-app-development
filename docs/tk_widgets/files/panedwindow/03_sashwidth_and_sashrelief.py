# tk PanedWindow - sashwidth and sashrelief

import tkinter as tk

root = tk.Tk()
root.geometry("300x200")
root.title("sashwidth")

panes = tk.PanedWindow(root, sashwidth=10, sashrelief="raised")
panes.pack(fill="both", expand=True)

panes.add(tk.Label(panes, text="Drag the", bg="lightblue"))
panes.add(tk.Label(panes, text="thick sash", bg="lightgreen"))

root.mainloop()
