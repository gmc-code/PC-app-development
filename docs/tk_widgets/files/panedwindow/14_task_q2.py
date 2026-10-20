# tk PanedWindow - Tasks Q2

import tkinter as tk

root = tk.Tk()
root.geometry("300x200")
root.title("Panes")

panes = tk.PanedWindow(root, orient="vertical", sashwidth=10)
panes.pack(fill="both", expand=True)

top_label = tk.Label(panes, text="Top", bg="yellow")
bottom_label = tk.Label(panes, text="Bottom", bg="orange")
panes.add(top_label)
panes.add(bottom_label)

root.mainloop()
