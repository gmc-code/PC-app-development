import tkinter as tk
from tkinter import messagebox

def show_custom_dialog():
    toplevel = tk.Toplevel(root)
    toplevel.title("Custom Dialog")
    toplevel.geometry("+100+100")  # Set the position (x=100, y=100)

    label = tk.Label(toplevel, text="Logged in successfully!")
    label.pack(padx=20, pady=10)

    ok_button = tk.Button(toplevel, text="OK", command=toplevel.destroy)
    ok_button.pack(pady=10)

root = tk.Tk()
root.geometry("300x200+10+10")
root.title("Main Window")

# Button to trigger the custom dialog
quit_button = tk.Button(root, text="Show_dialog", command=show_custom_dialog, width=14)
quit_button.pack(pady=80)

root.mainloop()
