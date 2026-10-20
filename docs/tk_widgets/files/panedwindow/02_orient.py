# tk PanedWindow - orient

import tkinter as tk

root = tk.Tk()
root.geometry("300x200")
root.title("orient")

panes = tk.PanedWindow(root, orient="vertical")
panes.pack(fill="both", expand=True)

panes.add(tk.Label(panes, text="Top", bg="pink"))
panes.add(tk.Label(panes, text="Bottom", bg="lightyellow"))

root.mainloop()
