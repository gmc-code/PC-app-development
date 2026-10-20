# tk Radiobutton - select and invoke

import tkinter as tk


def show():
    result_label.config(text="Size: " + size.get())


root = tk.Tk()
root.geometry("300x200")
root.title("select and invoke")

size = tk.StringVar(value="none")

small_radio = tk.Radiobutton(root, text="Small", variable=size, value="Small", command=show)
small_radio.pack()
large_radio = tk.Radiobutton(root, text="Large", variable=size, value="Large", command=show)
large_radio.pack()

result_label = tk.Label(root, text="")
result_label.pack(pady=10)

large_radio.invoke()        # Choose "Large" and run show() at the start

root.mainloop()
