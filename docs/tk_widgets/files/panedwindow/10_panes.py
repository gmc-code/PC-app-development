# tk PanedWindow - panes

import tkinter as tk

root = tk.Tk()
root.geometry("300x200")
root.title("panes")

panes = tk.PanedWindow(root)
panes.pack(fill="both", expand=True)

panes.add(tk.Label(panes, text="A", bg="pink"))
panes.add(tk.Label(panes, text="B", bg="lightblue"))
panes.add(tk.Label(panes, text="C", bg="lightgreen"))

count_label = tk.Label(root, text=f"Number of panes: {len(panes.panes())}")
count_label.pack()

root.mainloop()
