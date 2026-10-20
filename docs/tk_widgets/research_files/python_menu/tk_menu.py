import tkinter as tk

root = tk.Tk()
root.title("Menu Example")
root.geometry("300x200")

# Create the menu bar.
menubar = tk.Menu(root)
root.config(menu=menubar)

# Create the File menu.
file_menu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=file_menu)

# Add menu commands.
file_menu.add_command(label="Exit", command=root.destroy)

root.mainloop()