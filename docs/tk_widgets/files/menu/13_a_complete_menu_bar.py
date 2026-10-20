# tk Menu - A complete menu bar

import tkinter as tk


def new():
    notes_box.delete("1.0", tk.END)


def about():
    notes_box.insert(tk.END, "\nNote Pad version 1.0")


def change_wrap():
    if wrap_on.get() == 1:
        notes_box.config(wrap="word")
    else:
        notes_box.config(wrap="none")


root = tk.Tk()
root.geometry("350x250")
root.title("Note Pad")

menubar = tk.Menu(root)
root.config(menu=menubar)

# File menu
file_menu = tk.Menu(menubar, tearoff=0)
file_menu.add_command(label="New", command=new)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.destroy)
menubar.add_cascade(label="File", menu=file_menu)

# View menu
wrap_on = tk.IntVar(value=1)
view_menu = tk.Menu(menubar, tearoff=0)
view_menu.add_checkbutton(label="Word wrap", variable=wrap_on, command=change_wrap)
menubar.add_cascade(label="View", menu=view_menu)

# Help menu
help_menu = tk.Menu(menubar, tearoff=0)
help_menu.add_command(label="About", command=about)
menubar.add_cascade(label="Help", menu=help_menu)

notes_box = tk.Text(root, wrap="word")
notes_box.pack(fill="both", expand=True)

root.mainloop()
