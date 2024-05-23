import tkinter as tk
root = tk.Tk()
listbox = tk.Listbox(root)
listbox.insert(1, "Python")
listbox.insert(2, "Tkinter")
listbox.pack()
root.mainloop()
