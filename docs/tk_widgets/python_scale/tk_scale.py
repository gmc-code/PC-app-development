import tkinter as tk

root = tk.Tk()
root.title("Scale Example")

value = tk.IntVar(value=50)

scale = tk.Scale(
    root,
    from_=0,
    to=100,
    orient="horizontal",
    variable=value,
    length=300
)

scale.pack(padx=10, pady=10)

root.mainloop()