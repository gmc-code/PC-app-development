import tkinter as tk

root = tk.Tk()
root.title("Coloured Menubutton Example")
root.geometry("300x200")

# Create the Menubutton
menubutton = tk.Menubutton(
    root,
    text="Colours",
    relief="raised"
)

# Create the menu
colour_menu = tk.Menu(menubutton, tearoff=0)

colour_menu.add_command(label="Red")
colour_menu.add_command(label="Green")
colour_menu.add_command(label="Blue")
colour_menu.add_separator()
colour_menu.add_command(label="Exit", command=root.destroy)

# Colour individual menu entries
colour_menu.entryconfig("Red", foreground="red")
colour_menu.entryconfig("Green", foreground="green")
colour_menu.entryconfig("Blue", foreground="blue")

menubutton.config(menu=colour_menu)

menubutton.pack(padx=20, pady=20)

root.mainloop()