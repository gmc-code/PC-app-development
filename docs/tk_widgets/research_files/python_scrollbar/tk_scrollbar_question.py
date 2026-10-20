import tkinter as tk

root = tk.Tk()
root.title("Menu Question")
root.geometry("300x200")

# Create the menu bar
menubar = tk.Menu(root)
root.config(menu=menubar)

# Create the File menu
file_menu = tk.Menu(menubar, tearoff=0)

# Add the File menu to the menu bar
menubar.add_cascade(label="File", menu=file_menu)

# Add menu commands
file_menu.add_command(label="New")
file_menu.add_command(label="Open")
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.destroy)

root.mainloop()
