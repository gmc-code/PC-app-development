import tkinter as tk


def open_window():
    window = tk.Toplevel(root)
    window.title("Second Window")
    window.geometry("280x150")

    label = tk.Label(
        window,
        text="This is a Toplevel window",
        font=("Arial", 14)
    )

    label.pack(pady=30)


root = tk.Tk()
root.title("Toplevel Example")
root.geometry("300x200")

button = tk.Button(
    root,
    text="Open Window",
    command=open_window
)

button.pack(pady=50)

root.mainloop()