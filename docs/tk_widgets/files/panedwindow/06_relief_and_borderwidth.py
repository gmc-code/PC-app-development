# tk PanedWindow - relief and borderwidth

import tkinter as tk

root = tk.Tk()
root.geometry("300x200")
root.title("relief")

panes = tk.PanedWindow(root, relief="solid", borderwidth=2)
panes.pack(fill="both", expand=True, padx=10, pady=10)

panes.add(tk.Label(panes, text="Left", bg="lightblue"))
panes.add(tk.Label(panes, text="Right", bg="lightgreen"))

root.mainloop()
