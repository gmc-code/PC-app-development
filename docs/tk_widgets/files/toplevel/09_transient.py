# tk Toplevel - transient

import tkinter as tk


def open_tools():
    tools = tk.Toplevel(root)
    tools.title("Tools")
    tools.geometry("150x150")
    tools.transient(root)               # Always stays in front of root
    tk.Button(tools, text="Pencil").pack(pady=5)
    tk.Button(tools, text="Eraser").pack(pady=5)


root = tk.Tk()
root.geometry("300x200")
root.title("transient")

tk.Button(root, text="Show tools", command=open_tools).pack(pady=60)

root.mainloop()
