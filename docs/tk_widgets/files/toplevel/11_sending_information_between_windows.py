# tk Toplevel - Sending information between windows

import tkinter as tk


def open_settings():
    settings = tk.Toplevel(root)
    settings.title("Settings")
    settings.geometry("250x130")
    settings.grab_set()

    tk.Label(settings, text="New name:").pack(pady=5)
    name_entry = tk.Entry(settings)
    name_entry.pack()

    def save():
        name_label.config(text="Player: " + name_entry.get())     # Change the main window
        settings.destroy()

    tk.Button(settings, text="Save", command=save).pack(pady=10)


root = tk.Tk()
root.geometry("300x200")
root.title("Game")

name_label = tk.Label(root, text="Player: ???", font=("Arial", 16))
name_label.pack(pady=30)

tk.Button(root, text="Change name", command=open_settings).pack()

root.mainloop()
