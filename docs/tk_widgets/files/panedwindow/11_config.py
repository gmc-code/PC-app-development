# tk PanedWindow - config

import tkinter as tk


def flip():
    if panes.cget("orient") == "horizontal":
        panes.config(orient="vertical")
    else:
        panes.config(orient="horizontal")


root = tk.Tk()
root.geometry("300x250")
root.title("config")

panes = tk.PanedWindow(root, sashwidth=5)
panes.pack(fill="both", expand=True)

panes.add(tk.Label(panes, text="One", bg="lightblue"))
panes.add(tk.Label(panes, text="Two", bg="lightgreen"))

tk.Button(root, text="Flip", command=flip).pack(pady=5)

root.mainloop()
