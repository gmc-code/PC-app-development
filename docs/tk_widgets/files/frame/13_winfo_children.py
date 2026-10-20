# tk Frame - winfo_children

import tkinter as tk


def disable_all():
    for widget in controls.winfo_children():
        widget.config(state="disabled")


root = tk.Tk()
root.geometry("300x200")
root.title("winfo_children")

controls = tk.Frame(root)
controls.pack(pady=10)
tk.Button(controls, text="Up").pack()
tk.Button(controls, text="Down").pack()
tk.Button(controls, text="Left").pack()

tk.Button(root, text="Game over", command=disable_all).pack(pady=10)

root.mainloop()
