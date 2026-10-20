# tk PanedWindow - Panes inside panes

import tkinter as tk

root = tk.Tk()
root.geometry("400x250")
root.title("Panes inside panes")

outer = tk.PanedWindow(root, orient="horizontal", sashwidth=5)
outer.pack(fill="both", expand=True)

outer.add(tk.Label(outer, text="Files", bg="lightblue"), width=100)

inner = tk.PanedWindow(outer, orient="vertical", sashwidth=5)     # Inside "outer"
outer.add(inner)

inner.add(tk.Label(inner, text="Code", bg="white"), height=150)
inner.add(tk.Label(inner, text="Output", bg="black", fg="white"))

root.mainloop()
