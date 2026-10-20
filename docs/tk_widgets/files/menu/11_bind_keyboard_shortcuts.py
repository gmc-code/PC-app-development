# tk Menu - bind (keyboard shortcuts)

import tkinter as tk


def clear(event=None):
    notes_box.delete("1.0", tk.END)


root = tk.Tk()
root.geometry("300x200")
root.title("Shortcuts")

menubar = tk.Menu(root)
root.config(menu=menubar)

edit_menu = tk.Menu(menubar, tearoff=0)
edit_menu.add_command(label="Clear", command=clear, accelerator="Ctrl+L")
menubar.add_cascade(label="Edit", menu=edit_menu)

root.bind("<Control-l>", clear)         # Make Ctrl+L work

notes_box = tk.Text(root)
notes_box.insert("1.0", "Press Ctrl+L to clear me")
notes_box.pack(fill="both", expand=True)

root.mainloop()
