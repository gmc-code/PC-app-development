import tkinter as tk


print(tk.Tcl().eval('info patchlevel'))
# 8.6.15

root = tk.Tk()
print(root.tk.call("info", "patchlevel"))
# 8.6.15

root.destroy()
