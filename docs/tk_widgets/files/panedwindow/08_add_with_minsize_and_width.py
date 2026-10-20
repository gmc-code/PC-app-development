# tk PanedWindow - add with minsize and width

import tkinter as tk

root = tk.Tk()
root.geometry("400x200")
root.title("minsize")

panes = tk.PanedWindow(root, sashwidth=5)
panes.pack(fill="both", expand=True)

panes.add(tk.Label(panes, text="Menu", bg="lightblue"), width=100, minsize=80)
panes.add(tk.Label(panes, text="Main area", bg="white"), minsize=150)

root.mainloop()
