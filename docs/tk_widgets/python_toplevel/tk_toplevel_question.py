import tkinter as tk


def open_settings():

    settings = tk.Toplevel(root)
    settings.title("Settings Window")
    settings.geometry("300x200")

    label = tk.Label(
        settings,
        text="Settings",
        font=("Arial", 18)
    )

    label.pack(pady=50)


root = tk.Tk()
root.title("Toplevel Question")
root.geometry("300x200")


button = tk.Button(
    root,
    text="Open Settings",
    command=open_settings
)

button.pack(pady=50)


root.mainloop()
