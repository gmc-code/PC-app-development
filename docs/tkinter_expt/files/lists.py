import tkinter as tk
window = tk.Tk()
listbox = tk.Listbox(window)
listbox.insert(1, "Python")
listbox.insert(2, "Tkinter")
listbox.pack()
window.mainloop()
