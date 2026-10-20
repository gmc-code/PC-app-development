# tk Menu - tearoff

import tkinter as tk

root = tk.Tk()
root.geometry("300x200")
root.title("tearoff")

menubar = tk.Menu(root)
root.config(menu=menubar)

with_line = tk.Menu(menubar, tearoff=1)
with_line.add_command(label="Open")
menubar.add_cascade(label="Tearoff on", menu=with_line)

without_line = tk.Menu(menubar, tearoff=0)
without_line.add_command(label="Open")
menubar.add_cascade(label="Tearoff off", menu=without_line)

root.mainloop()
