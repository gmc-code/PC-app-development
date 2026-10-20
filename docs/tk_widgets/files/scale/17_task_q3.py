# tk Scale - Tasks Q3

import tkinter as tk


def show_volume(value):
    volume_label.config(text="Volume: " + value)


root = tk.Tk()
root.geometry("300x200")
root.title("Volume")

volume_scale = tk.Scale(root, from_=0, to=100, orient="horizontal",
                        length=250, command=show_volume)
volume_scale.pack()

volume_label = tk.Label(root, text="Volume: 0", font=("Arial", 14))
volume_label.pack(pady=10)

root.mainloop()
