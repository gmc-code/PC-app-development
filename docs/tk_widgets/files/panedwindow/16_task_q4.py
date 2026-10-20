# tk PanedWindow - Tasks Q4

import tkinter as tk

root = tk.Tk()
root.geometry("300x200")
root.title("RGB")

panes = tk.PanedWindow(root, sashwidth=5)
panes.pack(fill="both", expand=True)

for colour in ["Red", "Green", "Blue"]:
    panes.add(tk.Label(panes, text=colour, bg=colour.lower(), fg="white"),
              minsize=50)

root.mainloop()
