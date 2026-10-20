# tk Label - wraplength and justify

import tkinter as tk

root = tk.Tk()
root.geometry("300x200")
root.title("wraplength")

label = tk.Label(
    root,
    text="This is a long sentence that will not fit on one line, so it wraps.",
    font=("Arial", 14),
    wraplength=200,
    justify="left",
)
label.pack(pady=20)

root.mainloop()
