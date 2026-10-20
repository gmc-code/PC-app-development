# tk PanedWindow - bg

import tkinter as tk

root = tk.Tk()
root.geometry("300x200")
root.title("bg")

panes = tk.PanedWindow(root, bg="red", sashwidth=6)
panes.pack(fill="both", expand=True)

panes.add(tk.Label(panes, text="Left", bg="white"))
panes.add(tk.Label(panes, text="Right", bg="white"))

root.mainloop()
