# tk Menu - add_command

import tkinter as tk


def new_note():
    notes_box.delete("1.0", tk.END)


root = tk.Tk()
root.geometry("300x200")
root.title("add_command")

menubar = tk.Menu(root)
root.config(menu=menubar)

file_menu = tk.Menu(menubar, tearoff=0)
file_menu.add_command(label="New", command=new_note, accelerator="Ctrl+N")
file_menu.add_command(label="Exit", command=root.destroy)
menubar.add_cascade(label="File", menu=file_menu)

notes_box = tk.Text(root, height=8)
notes_box.insert("1.0", "Some notes...")
notes_box.pack(fill="both", expand=True)

root.mainloop()
