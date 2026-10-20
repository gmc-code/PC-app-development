import tkinter as tk

root = tk.Tk()
root.title("Scale Question")

value = tk.IntVar(value=10)

scale = tk.Scale(
    root,
    from_=0,
    to=20,
    orient="vertical",
    variable=value,
    length=100
)

scale.pack(padx=10, pady=10)

root.mainloop()