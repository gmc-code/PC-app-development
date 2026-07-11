import tkinter as tk

root = tk.Tk()
root.title("Spinbox Example")
root.geometry("400x100")

value = tk.IntVar(value=5)

spinbox = tk.Spinbox(
    root,
    from_=0,
    to=10,
    increment=1,
    textvariable=value,
    width=4,
    font=("Arial", 16),
    bg="lightblue",
    fg="blue",
    activebackground="blue",
    borderwidth=1,
    relief="sunken",
    )

spinbox.pack(padx=10, pady=10)

root.mainloop()
