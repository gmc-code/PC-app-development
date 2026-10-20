import tkinter as tk

root = tk.Tk()
root.title("Menubutton Example")
root.geometry("300x200")

menubutton = tk.Menubutton(
    root,
    text="Options",
    relief="raised"
)

# Create the menu owned by the Menubutton
menu = tk.Menu(menubutton, tearoff=0)

menu.add_command(label="Option 1")
menu.add_command(label="Option 2")
menu.add_separator()
menu.add_command(label="Exit", command=root.destroy)

# Attach the menu
menubutton.config(menu=menu)

menubutton.pack(padx=20, pady=20)

root.mainloop()