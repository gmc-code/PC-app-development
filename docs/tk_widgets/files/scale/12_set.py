# tk Scale - set

import tkinter as tk


def reset():
    volume_scale.set(50)


root = tk.Tk()
root.geometry("300x200")
root.title("set")

volume_scale = tk.Scale(root, from_=0, to=100, orient="horizontal", length=200)
volume_scale.set(50)        # Start in the middle
volume_scale.pack()

reset_button = tk.Button(root, text="Reset to 50", command=reset)
reset_button.pack(pady=10)

root.mainloop()
